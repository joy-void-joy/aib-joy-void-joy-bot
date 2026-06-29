"""Worldview manager — maintenance sub-agent for the worldview store.

Spawns a sub-agent that has full read/write access to the worldview store
via dedicated MCP tools. The sub-agent decides what to do — cleanup,
deduplicate, link research to forecasts, reconcile contradictions, and
trigger AI resolution for ready subforecasts. All semantic judgments are
made by the agent rather than by keyword heuristics.
"""

import asyncio
import logging
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Literal

from claude_agent_sdk import AssistantMessage, ResultMessage
from claude_agent_sdk.types import TextBlock
from pydantic import BaseModel, Field

from aib.agent.client import REMOVE, build_client
from aib.tools.metrics import get_collector
from aib.agent.display import make_agent_prefix, print_block
from aib.agent.hooks import create_allowed_tools_hook
from aib.agent.nested import NestedAgentReport
from aib.agent.resolver import (
    QuestionForResolution,
    ResolutionVerdict,
    resolve_question,
)
from aib.paths import WORLDVIEW_PATH
from aib.tools.decorator import ToolError, mcp_tool
from aib.tools.mcp_server import create_mcp_server
from aib.worldview.lookup import (
    all_slugs,
    archive_entry,
    commit_worldview,
    iter_forecast_entries,
    iter_research_entries,
    load_forecast_entry,
    load_research_entry,
    resolve_forecast_entry,
    save_forecast_entry,
    supersede_entry,
)
from aib.worldview.models import (
    EntryState,
    WorldviewForecastEntry,
)

logger = logging.getLogger(__name__)


def score_binary_forecast(probability: float, resolution: float) -> float:
    """Brier score for a binary forecast."""
    return (probability - resolution) ** 2


# ── Structural helpers (no semantic judgment) ────────────────────


def find_resolvable_forecasts() -> list[WorldviewForecastEntry]:
    """Return forecast entries with resolvable_after <= now and not yet resolved."""
    now = datetime.now(timezone.utc)
    return [
        e
        for e in iter_forecast_entries()
        if not e.resolved
        and e.resolvable_after is not None
        and e.resolvable_after <= now
        and e.state != EntryState.resolved
    ]


async def resolve_ready_forecasts(
    *,
    dry_run: bool = False,
    min_confidence: float = 0.7,
    max_concurrent: int = 3,
) -> list[dict[str, object]]:
    """Run AI resolution on every forecast whose resolvable_after has passed.

    Structural sweep — no semantic judgment. For dedup/linking/contradiction
    maintenance, use the worldview_manager sub-agent instead.
    """
    resolvable = find_resolvable_forecasts()
    if not resolvable:
        return []

    semaphore = asyncio.Semaphore(max_concurrent)
    results: list[dict[str, object]] = []

    async def resolve_one(entry: WorldviewForecastEntry) -> dict[str, object]:
        question = QuestionForResolution(
            post_id=entry.parent_post_id or 0,
            question_title=entry.question,
            question_type=entry.question_type,
            resolution_criteria=entry.summary,
            fine_print="",
            description=entry.reasoning or "",
        )
        try:
            async with semaphore:
                report = await resolve_question(question)
                verdict = report.payload or ResolutionVerdict(
                    resolved=False,
                    resolution=None,
                    confidence=0.0,
                    reason="Agent produced no structured output",
                    sources=[],
                )
        except (RuntimeError, ValueError) as exc:
            logger.exception("Resolution failed for %s", entry.slug)
            return {
                "slug": entry.slug,
                "question": entry.question,
                "resolved": False,
                "error": f"{type(exc).__name__}: {exc}",
            }

        record: dict[str, object] = {
            "slug": entry.slug,
            "question": entry.question,
            "resolved": verdict.resolved,
            "confidence": verdict.confidence,
            "reason": verdict.reason,
        }

        if not verdict.resolved or verdict.confidence < min_confidence:
            return record
        if verdict.resolution is None:
            return record
        if not isinstance(verdict.resolution, (int, float)):
            logger.warning(
                "Resolver for %s returned non-numeric resolution %r; skipping",
                entry.slug,
                verdict.resolution,
            )
            return record

        resolution = float(verdict.resolution)
        score: float | None = None
        if entry.question_type == "binary" and entry.probability is not None:
            score = score_binary_forecast(entry.probability, resolution)

        if not dry_run:
            resolve_forecast_entry(
                entry.slug,
                resolution=resolution,
                resolution_source="worldview_auto_resolver",
                score=score,
            )

        record["resolution"] = resolution
        record["score"] = score
        return record

    coros = [resolve_one(e) for e in resolvable]
    results = await asyncio.gather(*coros)
    return results


# ── Maintenance sub-agent MCP tools ──────────────────────────────


class ListEntriesInput(BaseModel):
    """Input for wv_list_entries."""

    kind: Literal["research", "forecast", "all"] = Field(
        default="all",
        description="Which kind of entries to list.",
    )
    include_superseded: bool = Field(
        default=False,
        description="Include entries already marked as superseded.",
    )


@mcp_tool(
    "wv_list_entries",
    (
        "List worldview entries with summary info (slug, kind, query/question, "
        "state, updated_at, tags, resolvable_after). Call this first to see "
        "what exists; then use wv_read_entry to drill into specific entries."
    ),
)
async def wv_list_entries(args: ListEntriesInput) -> dict[str, object]:
    """List worldview entries (summaries only)."""
    entries: list[dict[str, object]] = []

    if args.kind in ("research", "all"):
        for r in iter_research_entries():
            if not args.include_superseded and r.state == EntryState.superseded:
                continue
            entries.append(
                {
                    "slug": r.slug,
                    "kind": "research",
                    "query": r.query,
                    "state": r.state.value,
                    "updated_at": r.updated_at.isoformat(),
                    "stale_after": r.stale_after.isoformat(),
                }
            )

    if args.kind in ("forecast", "all"):
        for f in iter_forecast_entries():
            if not args.include_superseded and f.state == EntryState.superseded:
                continue
            entries.append(
                {
                    "slug": f.slug,
                    "kind": "forecast",
                    "question": f.question,
                    "question_type": f.question_type,
                    "state": f.state.value,
                    "parent_post_id": f.parent_post_id,
                    "resolvable_after": (
                        f.resolvable_after.isoformat() if f.resolvable_after else None
                    ),
                    "resolved": f.resolved,
                    "updated_at": f.updated_at.isoformat(),
                    "stale_after": f.stale_after.isoformat(),
                    "tags": list(f.tags),
                }
            )

    return {"count": len(entries), "entries": entries}


class ReadEntryInput(BaseModel):
    """Input for wv_read_entry."""

    slug: str = Field(description="Slug of the entry to read.")
    kind: Literal["research", "forecasts"]


@mcp_tool(
    "wv_read_entry",
    (
        "Read a worldview entry in full. Use this to inspect details before "
        "deciding to archive, supersede, tag, or resolve it."
    ),
)
async def wv_read_entry(args: ReadEntryInput) -> dict[str, object]:
    """Read a worldview entry in full."""
    if args.kind == "research":
        entry = load_research_entry(args.slug)
    else:
        entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Entry {args.slug!r} ({args.kind}) not found")
    return entry.model_dump(mode="json")


class ArchiveEntryInput(BaseModel):
    """Input for wv_archive_entry."""

    slug: str
    kind: Literal["research", "forecasts"]
    reason: str = Field(
        description="Why this entry is being archived (e.g., 'resolved', 'past 2xTTL').",
    )


@mcp_tool(
    "wv_archive_entry",
    (
        "Move an entry to the worldview archive directory. Use for resolved "
        "entries or ones clearly past their stale window. Include a reason."
    ),
)
async def wv_archive_entry(args: ArchiveEntryInput) -> dict[str, object]:
    """Archive a worldview entry."""
    success = archive_entry(args.slug, args.kind)
    if not success:
        raise ToolError(f"Entry {args.slug!r} ({args.kind}) not found")
    logger.info(
        "Maintenance agent archived %s %s: %s", args.kind, args.slug, args.reason
    )
    return {"archived": args.slug, "kind": args.kind, "reason": args.reason}


class SupersedeEntryInput(BaseModel):
    """Input for wv_supersede_entry."""

    older_slug: str
    newer_slug: str
    kind: Literal["research", "forecasts"]
    reason: str = Field(
        description="Why the older entry is superseded by the newer one.",
    )


@mcp_tool(
    "wv_supersede_entry",
    (
        "Mark an older entry as superseded by a newer one. Use only when two "
        "entries genuinely cover the same question (not just share keywords). "
        "Include a reason explaining why they are redundant."
    ),
)
async def wv_supersede_entry(args: SupersedeEntryInput) -> dict[str, object]:
    """Supersede an older worldview entry with a newer one."""
    if args.older_slug == args.newer_slug:
        raise ToolError("older_slug and newer_slug must differ")

    success = supersede_entry(args.older_slug, args.kind, args.newer_slug)
    if not success:
        raise ToolError(f"Entry {args.older_slug!r} ({args.kind}) not found")
    logger.info(
        "Maintenance agent superseded %s %s by %s: %s",
        args.kind,
        args.older_slug,
        args.newer_slug,
        args.reason,
    )
    return {
        "superseded": args.older_slug,
        "superseded_by": args.newer_slug,
        "kind": args.kind,
        "reason": args.reason,
    }


class ReconcileInput(BaseModel):
    """Input for wv_reconcile."""

    claim: str = Field(
        description=(
            "The disputed factual claim to re-research, phrased as a precise "
            "current-state question (e.g., 'What is the current status of the "
            "Knesset dissolution bill as of today?')."
        ),
    )
    conflicting_slugs: list[str] = Field(
        description=(
            "Slugs of the research entries that disagree and should be "
            "superseded by the fresh, authoritative entry."
        ),
    )
    ttl: str = Field(
        default="1d",
        description="Cache lifetime for the reconciled entry (6h, 12h, 1d, 3d, 7d, 14d).",
    )


@mcp_tool(
    "wv_reconcile",
    (
        "Reconcile a contradiction by re-researching the disputed claim and "
        "superseding the stale entries with one fresh, authoritative entry. "
        "The fresh research captures the current state of the world; if sources "
        "genuinely disagree, it records the range rather than forcing a single "
        "value. Use this instead of merely noting a contradiction — the store "
        "should converge on one current truth per fact."
    ),
)
async def wv_reconcile(args: ReconcileInput) -> dict[str, object]:
    """Re-research a disputed claim and supersede the conflicting entries."""
    from aib.tools.research import ResearchQuestion, run_single_research

    missing = [s for s in args.conflicting_slugs if load_research_entry(s) is None]
    if missing:
        raise ToolError(f"Conflicting slugs not found: {', '.join(missing)}")

    result = await run_single_research(
        ResearchQuestion(query=args.claim, ttl=args.ttl),
        all_slugs(),
    )
    if result.entry is None:
        raise ToolError(f"Re-research failed: {result.error or 'no entry produced'}")

    new_slug = result.entry.slug
    superseded: list[str] = []
    for slug in args.conflicting_slugs:
        if slug == new_slug:
            continue
        if supersede_entry(slug, "research", new_slug):
            superseded.append(slug)
    logger.info("Maintenance agent reconciled %s into %s", superseded, new_slug)
    return {
        "reconciled_into": new_slug,
        "superseded": superseded,
        "claim": args.claim,
    }


class TagForecastInput(BaseModel):
    """Input for wv_tag_forecast."""

    slug: str = Field(description="Slug of the forecast entry to tag.")
    tags: list[str] = Field(
        description=(
            "Tags to add. Tags are merged with existing tags. "
            "Use 'research:<slug>' to link a research entry to this forecast."
        ),
    )


@mcp_tool(
    "wv_tag_forecast",
    (
        "Add tags to a forecast entry. Commonly used to link research to "
        "forecasts with a 'research:<slug>' tag. Tags are merged into the "
        "existing tag set. Only forecast entries are taggable."
    ),
)
async def wv_tag_forecast(args: TagForecastInput) -> dict[str, object]:
    """Add tags to a forecast entry."""
    forecast = load_forecast_entry(args.slug)
    if forecast is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")
    merged = sorted(set(forecast.tags) | set(args.tags))
    save_forecast_entry(forecast.model_copy(update={"tags": merged}))
    return {"slug": args.slug, "tags": merged}


class ResolveForecastInput(BaseModel):
    """Input for wv_resolve_forecast."""

    slug: str
    resolution: float = Field(
        description=(
            "Resolution value. For binary: 1.0 for YES, 0.0 for NO. "
            "For numeric: the actual resolved value."
        ),
    )
    source: str = Field(
        description="Where the resolution came from (e.g., 'ai_resolver', 'manual').",
    )


@mcp_tool(
    "wv_resolve_forecast",
    (
        "Set the resolution for a worldview forecast entry. Use only after "
        "you have verified the resolution from a reliable source. Automatically "
        "computes the Brier score for binary forecasts."
    ),
)
async def wv_resolve_forecast(args: ResolveForecastInput) -> dict[str, object]:
    """Resolve a worldview forecast entry."""
    entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")

    score: float | None = None
    if entry.question_type == "binary" and entry.probability is not None:
        score = score_binary_forecast(entry.probability, args.resolution)

    resolve_forecast_entry(
        args.slug,
        resolution=args.resolution,
        resolution_source=args.source,
        score=score,
    )
    return {
        "resolved": args.slug,
        "resolution": args.resolution,
        "source": args.source,
        "score": score,
    }


class AiResolveForecastInput(BaseModel):
    """Input for wv_ai_resolve_forecast."""

    slug: str = Field(description="Slug of the forecast entry to resolve via AI.")


@mcp_tool(
    "wv_ai_resolve_forecast",
    (
        "Run the AI resolver agent on a forecast entry. Returns the resolver's "
        "verdict with confidence and reasoning. Use this for subforecasts where "
        "resolvable_after has passed. Review the verdict before calling "
        "wv_resolve_forecast to record it."
    ),
)
async def wv_ai_resolve_forecast(
    args: AiResolveForecastInput,
) -> dict[str, object]:
    """Run AI resolution on a worldview forecast entry."""
    entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")

    question = QuestionForResolution(
        post_id=entry.parent_post_id or 0,
        question_title=entry.question,
        question_type=entry.question_type,
        resolution_criteria=entry.summary,
        fine_print="",
        description=entry.reasoning or "",
    )
    report = await resolve_question(question)
    verdict = report.payload or ResolutionVerdict(
        resolved=False,
        resolution=None,
        confidence=0.0,
        reason="Agent produced no structured output",
        sources=[],
    )
    return verdict.model_dump(mode="json")


# ── Sub-agent runner ──────────────────────────────────────────────


MAINTENANCE_TOOLS = [
    wv_list_entries,
    wv_read_entry,
    wv_archive_entry,
    wv_supersede_entry,
    wv_reconcile,
    wv_tag_forecast,
    wv_resolve_forecast,
    wv_ai_resolve_forecast,
]

MAINTENANCE_TOOL_NAMES = [
    "mcp__worldview_maintenance__wv_list_entries",
    "mcp__worldview_maintenance__wv_read_entry",
    "mcp__worldview_maintenance__wv_archive_entry",
    "mcp__worldview_maintenance__wv_supersede_entry",
    "mcp__worldview_maintenance__wv_reconcile",
    "mcp__worldview_maintenance__wv_tag_forecast",
    "mcp__worldview_maintenance__wv_resolve_forecast",
    "mcp__worldview_maintenance__wv_ai_resolve_forecast",
]


MAINTENANCE_SYSTEM_PROMPT = """\
You are the maintenance agent for the worldview store.

The worldview store holds two kinds of entries:
- **Research entries**: factual findings from the research sub-agent, keyed by slug.
- **Forecast entries**: subforecasts produced by the forecasting pipeline, keyed by slug.

Your job is to keep the store organized and accurate. You have these tools:
- `wv_list_entries` — see all entries with summary info
- `wv_read_entry` — read a specific entry in full
- `wv_archive_entry` — move an entry to the archive directory
- `wv_supersede_entry` — mark an older entry as superseded by a newer one
- `wv_reconcile` — re-research a disputed claim and supersede the stale entries
- `wv_tag_forecast` — add tags to a forecast (used to link research to forecasts)
- `wv_ai_resolve_forecast` — run the AI resolver on a forecast (returns a verdict)
- `wv_resolve_forecast` — record a resolution you have verified

## Tasks to perform

1. **Cleanup** — Archive entries that are already resolved, or clearly past
   their stale window. These clutter the store without providing value. Only
   archive when you are confident the entry is no longer useful.

2. **Deduplication** — If two entries genuinely cover the same question (not
   just share words), keep the newer one and supersede the older. Be strict:
   only supersede when the redundancy is clear after reading both entries.
   Related-but-distinct entries should both be kept.

3. **Linking research to forecasts** — When a research entry contains data
   that is the primary evidence for a specific forecast, tag the forecast
   with `research:<slug>`. Do not link loosely — only when the research
   directly underpins the forecast.

4. **Reconciling contradictions** — If multiple research entries report
   different values for the same metric, reconcile them with `wv_reconcile`:
   pass the disputed claim as a precise current-state question along with the
   conflicting slugs. This re-researches the claim and supersedes the stale
   entries with one fresh, authoritative entry. If the world is genuinely
   contested, the fresh research records the range — that is the resolved
   state, so do not re-flag it. The store should converge on one current
   truth per fact; never defer a disagreement.

5. **Resolving ready forecasts** — For subforecasts where `resolvable_after`
   has passed and `resolved` is false, call `wv_ai_resolve_forecast`. Review
   the verdict. If the resolver is confident and the reasoning holds up, call
   `wv_resolve_forecast` to record it. If the verdict is uncertain or the
   reasoning is thin, skip it and leave it unresolved — the next sweep will
   re-attempt it once more evidence is available.

## Guidelines

- **Be thoughtful.** Skip uncertain cases rather than acting on weak signals.
- **Read before acting.** List first, then read the specific entries you care
  about before archiving, superseding, or tagging.
- **Don't touch every entry.** Sweep, act on the clear cases, and stop. A
  maintenance run should leave the store cleaner than it found it, not
  rewritten end-to-end.
- **Keep coherence local.** After reconciling or refreshing an entry, only
  re-check entries that directly touch the same entity or metric — don't
  re-audit the whole store.
- **Write a final summary** describing what you did and why, including any
  contradictions you reconciled. Your caller reads this summary to understand
  the sweep.
"""


class MaintenanceSummary(BaseModel):
    """Structured summary returned by the maintenance sub-agent."""

    actions_taken: list[str] = Field(
        default_factory=list,
        description="Human-readable list of concrete actions taken this sweep.",
    )
    contradictions_reconciled: list[str] = Field(
        default_factory=list,
        description="Contradictions reconciled by re-researching the disputed claim.",
    )
    skipped: list[str] = Field(
        default_factory=list,
        description="Cases considered but skipped (with brief reason).",
    )
    notes: str = Field(
        default="",
        description="Any additional observations about the store.",
    )


async def run_maintenance_agent(
    focus: str | None = None,
    dry_run: bool = False,
) -> NestedAgentReport[MaintenanceSummary]:
    """Spawn the maintenance sub-agent and return its structured summary."""
    WORLDVIEW_PATH.mkdir(parents=True, exist_ok=True)

    prompt_parts = [
        "Run a maintenance sweep over the worldview store.",
    ]
    if focus:
        prompt_parts.append(f"\nFocus for this sweep: {focus}")
    if dry_run:
        prompt_parts.append(
            "\nDRY RUN: describe what you would do but do not call any "
            "write tools (archive, supersede, tag, resolve). Your summary "
            "should list the actions you would have taken."
        )
    prompt_parts.append(
        "\nWhen you are finished, emit a structured summary describing what "
        "you did and any contradictions you reconciled."
    )
    prompt = "\n".join(prompt_parts)

    output_format = {
        "type": "json_schema",
        "schema": MaintenanceSummary.model_json_schema(),
    }

    maintenance_server = create_mcp_server(
        "worldview_maintenance", tools=MAINTENANCE_TOOLS
    )

    allowed_tools = list(MAINTENANCE_TOOL_NAMES)
    if dry_run:
        # Strip write tools for dry runs; agent can still list and read.
        allowed_tools = [
            name
            for name in allowed_tools
            if "wv_list_entries" in name or "wv_read_entry" in name
        ]
    allowed_tools.append("StructuredOutput")

    from aib.config import settings

    summary: MaintenanceSummary | None = None
    text_blocks: list[str] = []
    prefix = make_agent_prefix("worldview", focus)

    async with build_client(
        model=settings.model,
        system_prompt=MAINTENANCE_SYSTEM_PROMPT,
        permission_mode="bypassPermissions",
        cwd=str(WORLDVIEW_PATH),
        extra_args={"no-session-persistence": REMOVE},
        allowed_tools=allowed_tools,
        hooks=create_allowed_tools_hook(allowed_tools),
        output_format=output_format,
        mcp_servers={"worldview_maintenance": maintenance_server},
    ) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    print_block(block, prefix=prefix)
                    if isinstance(block, TextBlock):
                        text_blocks.append(block.text)
            if isinstance(message, ResultMessage):
                if message.total_cost_usd is not None:
                    get_collector().record_cost(
                        "worldview_manager", message.total_cost_usd
                    )
                if message.structured_output:
                    summary = MaintenanceSummary.model_validate(
                        message.structured_output
                    )

    return NestedAgentReport[MaintenanceSummary](
        payload=summary,
        final_text=text_blocks[-1] if text_blocks else "",
    )


# ── Standalone refresh loop ───────────────────────────────────────


@contextmanager
def worldview_research_session() -> Iterator[None]:
    """Enter a session with research MCP servers for standalone worldview work.

    Refresh and reconcile both run the research sub-agent, which reads its data
    tools from the active session. Outside a forecast there is no session, so we
    build the data-gathering servers (no sandbox — fact lookup needs no code
    execution) and enter a session for the duration of the sweep.
    """
    from aib.agent.session import ForecastSession, reset_session, set_session
    from aib.agent.tool_policy import ToolPolicy
    from aib.config import settings

    policy = ToolPolicy.from_settings(settings)
    session = ForecastSession(research_mcp_servers=policy.get_research_mcp_servers())
    set_session(session)
    try:
        yield
    finally:
        reset_session()


class WorldviewRefreshReport(BaseModel):
    """Result of one standalone worldview refresh cycle."""

    refreshed: int = 0
    refresh_errors: list[str] = Field(default_factory=list)
    maintenance: MaintenanceSummary | None = None
    committed: bool = False


async def run_worldview_refresh(*, max_concurrent: int = 3) -> WorldviewRefreshReport:
    """Run one full worldview cycle: refresh stale research, then maintenance.

    Re-researches every stale research entry on its own TTL clock, then spawns
    the maintenance agent to reconcile contradictions, link research, and
    resolve ready forecasts. Both run inside a research-capable session.
    """
    from aib.tools.research import refresh_stale_entries

    with worldview_research_session():
        refresh_results = await refresh_stale_entries(max_concurrent=max_concurrent)
        report = await run_maintenance_agent()

    committed = commit_worldview("worldview: refresh + maintenance sweep")
    return WorldviewRefreshReport(
        refreshed=sum(1 for r in refresh_results if r.entry is not None),
        refresh_errors=[r.error for r in refresh_results if r.error],
        maintenance=report.payload,
        committed=committed,
    )


# ── Top-level MCP tool ────────────────────────────────────────────


class WorldviewManagerInput(BaseModel):
    """Input for the worldview_manager tool."""

    focus: str | None = Field(
        default=None,
        description=(
            "Optional focus for this sweep (e.g., 'resolve ready forecasts only', "
            "'find duplicates in research'). Leave blank for a full sweep."
        ),
    )
    dry_run: bool = Field(
        default=False,
        description="If true, the agent reports what it would do without making changes.",
    )


class WorldviewManagerOutput(BaseModel):
    """Output from the worldview_manager tool."""

    summary: MaintenanceSummary | None = None
    dry_run: bool = False
    committed: bool = False


@mcp_tool(
    "worldview_manager",
    (
        "Run maintenance on the worldview store. Spawns a sub-agent that has "
        "full read/write access to worldview entries and decides what to do: "
        "archive resolved/expired entries, supersede duplicates, link research "
        "to forecasts, reconcile contradictions, and trigger AI resolution for "
        "ready subforecasts. Run this at the start or end of a tournament batch.\n\n"
        "Use focus='...' to scope the sweep (e.g., 'resolve ready forecasts'). "
        "Use dry_run=true to preview actions without making changes."
    ),
)
async def worldview_manager(args: WorldviewManagerInput) -> WorldviewManagerOutput:
    """Run worldview store maintenance via a sub-agent."""
    report = await run_maintenance_agent(focus=args.focus, dry_run=args.dry_run)

    committed = False
    if not args.dry_run:
        committed = commit_worldview("worldview: maintenance sweep")

    return WorldviewManagerOutput(
        summary=report.payload,
        dry_run=args.dry_run,
        committed=committed,
    )
