"""Subforecast tool — spawn independent sub-forecasts with worldview persistence.

Replaces spawn_subquestions (composition.py). Each sub-forecast gets its own
full forecasting agent (research, computation, calibration). Results are
persisted to the worldview store for reuse and resolution tracking.

Supports:
- List input → parallel execution via asyncio.gather
- Bounded recursion (max_depth default 1, cap 3)
- Worldview persistence (from_forecast_output conversion)
- Amend mode (patch probability/CDF/factors without re-running)
- CDF threshold extraction for binary derivation
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta, timezone

from pydantic import BaseModel, Field, ValidationError

from aib.agent.session import get_session
from aib.paths import WORLDVIEW_TRACES_PATH
from aib.retrodict_context import retrodict_cutoff
from aib.tools.decorator import ToolError, mcp_tool
from aib.worldview.lookup import (
    all_slugs,
    amend_forecast_entry,
    commit_worldview,
    load_forecast_entry,
    save_forecast_entry,
)
from aib.worldview.models import (
    NumericBounds,
    WorldviewForecastEntry,
    from_forecast_output,
    make_slug,
)

logger = logging.getLogger(__name__)

MAX_DEPTH_CAP = 3

TTL_PRESETS: dict[str, timedelta] = {
    "6h": timedelta(hours=6),
    "12h": timedelta(hours=12),
    "1d": timedelta(days=1),
    "3d": timedelta(days=3),
    "7d": timedelta(days=7),
    "14d": timedelta(days=14),
}

DEFAULT_TTL = "3d"


# ── Input schemas ────────────────────────────────────────────────


class SubforecastSpec(BaseModel):
    """Specification for a single sub-forecast."""

    question: str = Field(description="The forecasting question to answer.")
    context: str = Field(
        default="",
        description="Additional context (resolution criteria, background).",
    )
    question_type: str = Field(
        default="binary",
        description="Question type: binary, numeric, discrete, multiple_choice.",
    )
    options: list[str] = Field(
        default_factory=list,
        description="Options for multiple_choice questions.",
    )
    numeric_bounds: NumericBounds = Field(
        default_factory=NumericBounds,
        description="Bounds for numeric/discrete questions.",
    )
    ttl: str = Field(
        default=DEFAULT_TTL,
        description=(
            "How long before this sub-forecast goes stale. "
            "Options: 6h, 12h, 1d, 3d, 7d, 14d."
        ),
    )
    resolvable_after: str | None = Field(
        default=None,
        description=(
            "ISO datetime when ground truth becomes knowable. "
            "Triggers AI resolution sweep after this date."
        ),
    )
    tags: list[str] = Field(
        default_factory=list,
        description="Tags for categorization and linking.",
    )


class SubforecastInput(BaseModel):
    """Input for the subforecast tool."""

    specs: list[SubforecastSpec] = Field(
        min_length=1,
        description="List of sub-forecast specifications to run in parallel.",
    )
    max_depth: int = Field(
        default=1,
        description=(
            "Maximum recursion depth. 1 = no nesting (default). "
            "Higher values allow sub-forecasts to spawn their own sub-forecasts. Cap: 3."
        ),
    )
    amend: str | None = Field(
        default=None,
        description=(
            "Slug of an existing forecast entry to patch. "
            "Updates specific fields without re-running the forecast pipeline. "
            "Provide the updates in the first spec's context field as JSON."
        ),
    )


# ── Output schemas ───────────────────────────────────────────────


class SubforecastResult(BaseModel):
    """Result from a single sub-forecast."""

    question: str
    entry: WorldviewForecastEntry | None = None
    error: str | None = None


class SubforecastOutput(BaseModel):
    """Output from the subforecast tool."""

    results: list[dict[str, object]]
    successful_count: int
    failed_count: int


# ── Single sub-forecast runner ───────────────────────────────────


def build_question_context(spec: SubforecastSpec) -> dict[str, object]:
    """Build a question context dict from a SubforecastSpec."""
    context: dict[str, object] = {
        "title": spec.question,
        "type": spec.question_type,
        "description": spec.context,
        "resolution_criteria": "",
        "fine_print": "",
    }

    if spec.question_type == "multiple_choice" and spec.options:
        context["options"] = spec.options
    elif spec.question_type in ("numeric", "discrete"):
        bounds = spec.numeric_bounds
        if bounds.range_min is not None or bounds.range_max is not None:
            context["numeric_bounds"] = bounds.model_dump(exclude_none=True)

    return context


async def run_single_subforecast(
    spec: SubforecastSpec,
    effective_depth: int,
    slug: str,
    parent_post_id: int | None,
) -> SubforecastResult:
    """Run a single sub-forecast with worldview persistence."""
    session = get_session()
    if session.run_forecast_fn is None:
        return SubforecastResult(
            question=spec.question,
            error="run_forecast not configured on session",
        )

    context = build_question_context(spec)
    child_depth = effective_depth - 1
    allow_spawn = child_depth > 0
    entry_depth = session.current_depth
    parent_slug = session.parent_slug

    try:
        forecast = await session.run_forecast_fn(
            question_context=context,
            allow_spawn=allow_spawn,
            subforecast_depth=child_depth if allow_spawn else 0,
            current_depth=entry_depth + 1,
            parent_slug=slug,
        )

        # Persist to worldview store
        ttl = TTL_PRESETS.get(spec.ttl, TTL_PRESETS[DEFAULT_TTL])
        now = datetime.now(timezone.utc)

        resolvable_after: datetime | None = None
        if spec.resolvable_after:
            try:
                resolvable_after = datetime.fromisoformat(spec.resolvable_after)
            except ValueError:
                logger.warning("Invalid resolvable_after: %s", spec.resolvable_after)

        entry = from_forecast_output(
            forecast,
            slug=slug,
            stale_after=now + ttl,
            resolvable_after=resolvable_after,
            parent_post_id=parent_post_id,
            parent_slug=parent_slug,
            depth=entry_depth,
            tags=spec.tags,
        )

        # Store numeric bounds from the spec (ForecastOutput doesn't carry them)
        # — needed for CDF threshold extraction
        bounds = spec.numeric_bounds
        if bounds.range_min is not None or bounds.range_max is not None:
            entry = entry.model_copy(update={"numeric_bounds": bounds})

        save_forecast_entry(entry)

        if retrodict_cutoff.get() is None:
            trace_dir = WORLDVIEW_TRACES_PATH / slug
            trace_dir.mkdir(parents=True, exist_ok=True)
            meta = (
                f"# Subforecast: {spec.question}\n\n"
                f"- **Slug**: {slug}\n"
                f"- **Type**: {spec.question_type}\n"
                f"- **Depth**: {entry_depth}\n"
                f"- **Parent post**: {parent_post_id}\n"
                f"- **Parent slug**: {parent_slug or '—'}\n"
                f"- **Created**: {entry.created_at.isoformat()}\n\n"
                f"## Summary\n\n{forecast.summary}\n\n"
                f"## Reasoning\n\n{forecast.reasoning}\n"
            )
            (trace_dir / "meta.md").write_text(meta, encoding="utf-8")
            (trace_dir / "summary.json").write_text(
                entry.model_dump_json(indent=2), encoding="utf-8"
            )

        commit_worldview(f"subforecast: {spec.question[:60]}")

        return SubforecastResult(question=spec.question, entry=entry)

    except (ValueError, RuntimeError, OSError, ValidationError) as e:
        logger.exception("Sub-forecast failed: %s", spec.question)
        return SubforecastResult(
            question=spec.question,
            error=f"{type(e).__name__}: {e}",
        )


# ── Amend handler ────────────────────────────────────────────────


def handle_amend(slug: str, updates_json: str) -> SubforecastResult:
    """Patch fields on an existing forecast entry."""
    try:
        updates = json.loads(updates_json)
    except json.JSONDecodeError as e:
        return SubforecastResult(
            question="",
            error=f"Invalid JSON in amend updates: {e}",
        )

    allowed_fields = {
        "probability",
        "probabilities",
        "median",
        "confidence_interval",
        "percentiles",
        "cdf",
        "factors",
        "summary",
        "reasoning",
        "tags",
    }
    filtered = {k: v for k, v in updates.items() if k in allowed_fields}
    if not filtered:
        return SubforecastResult(
            question="",
            error=f"No amendable fields in updates. Allowed: {sorted(allowed_fields)}",
        )

    result = amend_forecast_entry(
        slug, filtered, reason="manual amend via subforecast tool"
    )
    if result is None:
        return SubforecastResult(
            question="",
            error=f"Forecast entry '{slug}' not found",
        )

    commit_worldview(f"subforecast amend: {slug}")

    return SubforecastResult(question=result.question, entry=result)


# ── CDF threshold extraction ────────────────────────────────────


def extract_cdf_threshold(slug: str, threshold: float) -> float | None:
    """Extract P(value > threshold) from a worldview forecast entry's CDF.

    Returns the probability that the value exceeds the threshold,
    or None if the entry doesn't exist or has no CDF.
    """
    entry = load_forecast_entry(slug)
    if entry is None or entry.cdf is None or entry.numeric_bounds is None:
        return None

    bounds = entry.numeric_bounds
    if bounds.range_min is None or bounds.range_max is None:
        return None

    lower_f = bounds.range_min
    upper_f = bounds.range_max
    n_points = len(entry.cdf)
    if n_points < 2 or upper_f <= lower_f:
        return None

    # Linear interpolation on the CDF
    fraction = (threshold - lower_f) / (upper_f - lower_f)
    index = fraction * (n_points - 1)

    if index <= 0:
        cdf_at_threshold = entry.cdf[0]
    elif index >= n_points - 1:
        cdf_at_threshold = entry.cdf[-1]
    else:
        lo_idx = int(index)
        hi_idx = lo_idx + 1
        frac = index - lo_idx
        cdf_at_threshold = entry.cdf[lo_idx] + frac * (
            entry.cdf[hi_idx] - entry.cdf[lo_idx]
        )

    return 1.0 - cdf_at_threshold


# ── MCP Tool ─────────────────────────────────────────────────────


@mcp_tool(
    "subforecast",
    "Spawn independent sub-forecasts, each with its own full pipeline (research, "
    "computation, calibration). Results are persisted to the worldview store for "
    "reuse and resolution tracking.\n\n"
    "**Use subforecast() for forward-looking predictions**: 'What WILL happen?' "
    "'How many X by date Y?' Any question needing a probability distribution.\n\n"
    "**Do NOT use for data gathering**: Use research() instead for backward-looking "
    "factual questions.\n\n"
    "Pass multiple specs to forecast them in parallel.\n\n"
    "**Decomposition patterns:**\n"
    "- Conditional chain: P(A and B) = P(A) × P(B|A)\n"
    "- Revenue segments: forecast each, then sum\n"
    "- Binary from numeric: spawn numeric subforecast, extract CDF threshold\n\n"
    "Example (conditional chain):\n"
    "  subforecast(specs=[\n"
    '    {question: "Will Country X apply to join Org Y by mid-2026?", '
    'question_type: "binary"},\n'
    '    {question: "If applied, will all members approve?", '
    'question_type: "binary"}\n'
    "  ])\n"
    "  Then multiply: P(join) = P(apply) × P(approve|apply).\n\n"
    "Example (binary from numeric — resolves binary/numeric inconsistency):\n"
    '  subforecast(specs=[{question: "How many US measles cases by April 24?", '
    'question_type: "numeric", numeric_bounds: {range_min: 0, range_max: 10000}, '
    'ttl: "6h", resolvable_after: "2026-04-25"}])\n'
    "  Then read the CDF: P(>2000) from the worldview entry.\n\n"
    "Amend an existing entry without re-running:\n"
    '  subforecast(amend="us-measles-cases-apr24-e9d4f7a2",\n'
    '             specs=[{context: \'{"probability": 0.62, '
    '"summary": "Adjusted to match CDF"}\'}])\n',
)
async def subforecast(args: SubforecastInput) -> SubforecastOutput:
    """Run parallel sub-forecasts with worldview persistence."""

    # Handle amend mode (no sub-agent needed)
    if args.amend:
        updates_json = args.specs[0].context if args.specs else "{}"
        result = handle_amend(args.amend, updates_json)
        return SubforecastOutput(
            results=[result.model_dump(exclude_none=True)],
            successful_count=0 if result.error else 1,
            failed_count=1 if result.error else 0,
        )

    # Compute effective depth, respecting session cap
    session = get_session()
    input_depth = min(args.max_depth, MAX_DEPTH_CAP)
    if session.subforecast_depth is not None:
        input_depth = min(input_depth, session.subforecast_depth)
    if input_depth <= 0:
        raise ToolError("Cannot spawn sub-forecasts: recursion depth exhausted")

    parent_post_id = session.post_id

    existing = all_slugs()
    slugs: list[str] = []
    for spec in args.specs:
        slug = make_slug(spec.question, existing)
        existing.add(slug)
        slugs.append(slug)

    tasks = [
        run_single_subforecast(spec, input_depth, slug, parent_post_id)
        for spec, slug in zip(args.specs, slugs)
    ]
    results = await asyncio.gather(*tasks)

    errors = [r for r in results if r.error is not None]
    successful = [r for r in results if r.error is None]

    if not successful:
        error_msgs = [r.error for r in errors]
        raise ToolError(f"All sub-forecasts failed: {error_msgs}")

    return SubforecastOutput(
        results=[r.model_dump(exclude_none=True) for r in results],
        successful_count=len(successful),
        failed_count=len(errors),
    )


# ── CDF threshold tool ──────────────────────────────────────────


class ThresholdInput(BaseModel):
    """Input for extracting a binary probability from a numeric CDF."""

    slug: str = Field(
        description="Slug of a numeric worldview forecast entry with a CDF."
    )
    threshold: float = Field(
        description="The threshold value to check P(value > threshold)."
    )


class ThresholdOutput(BaseModel):
    """Result of CDF threshold extraction."""

    slug: str
    threshold: float
    probability_exceeds: float | None = None
    error: str | None = None


@mcp_tool(
    "extract_cdf_threshold",
    "Extract P(value > threshold) from a numeric worldview forecast entry's CDF.\n\n"
    "Use this after spawning a numeric subforecast to derive binary probabilities.\n"
    "For example, if you have a numeric subforecast for 'How many measles cases by "
    "April 24?' and need to answer 'Will measles exceed 2,000?', call:\n"
    "  extract_cdf_threshold(slug='measles-cases-apr24-xxxx', threshold=2000)\n"
    "Returns P(>2000) which you can use as a strong anchor for the binary forecast.",
)
async def extract_cdf_threshold_tool(args: ThresholdInput) -> ThresholdOutput:
    """Extract binary probability from a numeric CDF."""
    prob = extract_cdf_threshold(args.slug, args.threshold)
    if prob is None:
        return ThresholdOutput(
            slug=args.slug,
            threshold=args.threshold,
            error=f"Cannot extract threshold: entry '{args.slug}' not found, has no CDF, or has no numeric bounds",
        )
    return ThresholdOutput(
        slug=args.slug,
        threshold=args.threshold,
        probability_exceeds=prob,
    )
