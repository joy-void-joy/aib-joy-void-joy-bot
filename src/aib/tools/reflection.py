"""Reflection tool for forecasting sessions.

Replaces write_meta with a structured, iterative checkpoint tool.
Takes the agent's current factors and tentative logit, computes the
factor-implied probability, and returns the gap. Each call appends a
timestamped entry to reflection.yaml in the session directory.

After computing metrics, calls a Sonnet reviewer sub-agent that
reviews the forecast with access to the full reasoning trace, past
forecasts, and web search.
"""

import logging
import math
from collections.abc import Callable
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, cast

import aiofiles
from pydantic import BaseModel, Field

from claude_agent_sdk import tool

from aib.agent.hooks import HooksConfig
from aib.agent.models import BinaryEstimate, Factor, NumericEstimate, NumericSupport
from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

NEUTRAL_THRESHOLD = 0.1


# --- Input Model ---


class ReflectionInput(BaseModel):
    """Structured input for the reflection tool."""

    factors: list[Factor] = Field(
        description=(
            "Key evidence items with logit values and confidence. "
            "Same format as your final forecast factors."
        )
    )
    tentative_estimate: BinaryEstimate | NumericEstimate = Field(
        description=(
            "Your synthesized estimate. "
            "Binary: {logit, probability}. "
            "Numeric/discrete: {center, low, high}."
        ),
    )
    assessment: str = Field(
        description=(
            "Freeform narrative assessment of the evidence. Structure however "
            "fits the question: pro/con for binary, scenario analysis for "
            "numeric, uncertainty decomposition, key tensions, etc."
        ),
    )
    calibration_notes: str | None = Field(
        default=None,
        description="Base rates, status quo assessment, hedging check.",
    )
    key_uncertainties: str | None = Field(
        default=None,
        description="What you're most uncertain about and what would change your mind.",
    )
    tool_audit: str = Field(
        description=(
            "Which tools provided useful information, which returned "
            "empty results, and which had actual failures."
        ),
    )
    update_triggers: str | None = Field(
        default=None,
        description="Events that would move your forecast significantly.",
    )
    process_reflection: str = Field(
        description=(
            "How did the forecasting system feel to use — not what you "
            "did, but how the scaffolding supported you. What felt rigid "
            "or lacking, what felt smooth? What tools are missing that "
            "would have helped? What subagents would have been useful? "
            "Did the prompt guide you well or lead you astray for this "
            "question type? Where did you hit friction — a tool returning "
            "junk, a forced workaround, a missing capability?"
        ),
    )


# --- Output Models ---


class FactorBreakdown(BaseModel):
    """Per-factor effective logit computation."""

    description: str
    supports: str | float | NumericSupport | None = None
    logit: float
    confidence: float
    effective_logit: float
    conditional: str | None = None


class OutcomeBreakdown(BaseModel):
    """Per-outcome factor aggregation for MC questions."""

    outcome: str
    factor_count: int
    logit_sum: float
    factors: list[FactorBreakdown]


class NumericDistributionMetrics(BaseModel):
    """Distribution-level consistency metrics for numeric/discrete questions."""

    implied_median: float
    implied_p10: float
    implied_p90: float
    median_gap: float
    median_gap_pct: float
    spread_ratio: float


class ReflectionOutput(BaseModel):
    """Computed feedback from a reflection checkpoint."""

    factor_count: int
    factor_sum: float
    tentative_logit: float | None = None
    logit_gap: float | None = None
    neutral_factor_count: int
    factor_breakdown: list[FactorBreakdown]
    dominant_factor: str | None = None
    dominant_effective_logit: float | None = None

    # Binary-specific
    factor_implied_probability: float | None = None
    tentative_probability: float | None = None
    gap_pp: float | None = None

    # MC: per-outcome aggregation
    outcome_breakdown: list[OutcomeBreakdown] | None = None

    # Numeric/discrete: distribution-level metrics
    distribution_metrics: NumericDistributionMetrics | None = None

    # Sources consulted so far (populated from infrastructure)
    sources: list[str] = Field(default_factory=list)

    # Reviewer (populated by Sonnet sub-agent)
    reviewer_critique: str | None = None


# --- Reviewer Models ---


class ReviewVerdict(StrEnum):
    approve = "approve"
    warn = "warn"
    fail = "fail"


class ReviewResult(BaseModel):
    """Structured output from the reviewer sub-agent."""

    verdict: ReviewVerdict
    assessment: str = Field(
        description="Your full analysis. Explain what you checked, what you "
        "found, and why you reached your verdict. Be thorough — this is "
        "the agent's primary feedback for improving its forecast.",
    )


class ReviewState(BaseModel):
    """Shared state between reflection tool and StructuredOutput hook."""

    model_config = {"frozen": False}

    consecutive_fails: int = 0
    last_verdict: ReviewVerdict | None = None
    last_review: ReviewResult | None = None

    @property
    def passed(self) -> bool:
        if self.last_verdict is None:
            return False
        if self.last_verdict in (ReviewVerdict.approve, ReviewVerdict.warn):
            return True
        return self.consecutive_fails >= 3

    def record(self, result: ReviewResult) -> None:
        self.last_verdict = result.verdict
        self.last_review = result
        if result.verdict == ReviewVerdict.fail:
            self.consecutive_fails += 1
        else:
            self.consecutive_fails = 0


# --- Computation ---


def _compute_distribution_metrics(
    breakdown: list[FactorBreakdown],
    tentative: NumericEstimate,
) -> NumericDistributionMetrics | None:
    """Compute distribution-level consistency for numeric/discrete factors.

    Uses abs(effective_logit) as the weight for each factor's center/range.
    """
    pairs: list[tuple[NumericSupport, float]] = [
        (fb.supports, abs(fb.effective_logit))
        for fb in breakdown
        if isinstance(fb.supports, NumericSupport)
    ]
    if not pairs:
        return None

    total_weight = sum(w for _, w in pairs)
    if total_weight == 0:
        return None

    implied_median = sum(s.center * w for s, w in pairs) / total_weight
    implied_p10 = sum(s.low * w for s, w in pairs) / total_weight
    implied_p90 = sum(s.high * w for s, w in pairs) / total_weight

    implied_range = implied_p90 - implied_p10
    tentative_range = tentative.high - tentative.low
    median_gap = tentative.center - implied_median
    median_gap_pct = (median_gap / implied_range * 100) if implied_range > 0 else 0.0
    spread_ratio = (tentative_range / implied_range) if implied_range > 0 else 0.0

    return NumericDistributionMetrics(
        implied_median=implied_median,
        implied_p10=implied_p10,
        implied_p90=implied_p90,
        median_gap=median_gap,
        median_gap_pct=median_gap_pct,
        spread_ratio=spread_ratio,
    )


def compute_reflection(
    inp: ReflectionInput,
    question_type: str,
) -> ReflectionOutput:
    """Compute factor analysis and return structured feedback."""
    breakdown: list[FactorBreakdown] = []
    for f in inp.factors:
        breakdown.append(
            FactorBreakdown(
                description=f.description,
                supports=f.supports,
                logit=f.logit,
                confidence=f.confidence,
                effective_logit=f.logit * f.confidence,
                conditional=f.conditional,
            )
        )

    factor_sum = sum(fb.effective_logit for fb in breakdown)
    neutral_count = sum(1 for f in inp.factors if abs(f.logit) < NEUTRAL_THRESHOLD)
    dominant = max(breakdown, key=lambda fb: abs(fb.effective_logit), default=None)

    estimate = inp.tentative_estimate
    if isinstance(estimate, BinaryEstimate):
        tentative_logit: float | None = estimate.logit
        logit_gap: float | None = tentative_logit - factor_sum
    else:
        tentative_logit = None
        logit_gap = None

    output = ReflectionOutput(
        factor_count=len(inp.factors),
        factor_sum=factor_sum,
        tentative_logit=tentative_logit,
        logit_gap=logit_gap,
        neutral_factor_count=neutral_count,
        factor_breakdown=breakdown,
        dominant_factor=dominant.description if dominant else None,
        dominant_effective_logit=dominant.effective_logit if dominant else None,
    )

    if question_type == "binary" and isinstance(estimate, BinaryEstimate):
        output.factor_implied_probability = 1 / (1 + math.exp(-factor_sum))
        output.tentative_probability = estimate.probability
        output.gap_pp = (estimate.probability - output.factor_implied_probability) * 100
    elif question_type in ("numeric", "discrete"):
        assert isinstance(estimate, NumericEstimate)
        output.distribution_metrics = _compute_distribution_metrics(breakdown, estimate)
    elif question_type == "multiple_choice":
        from collections import defaultdict

        by_outcome: dict[str, list[FactorBreakdown]] = defaultdict(list)
        for fb in breakdown:
            if isinstance(fb.supports, str):
                by_outcome[fb.supports].append(fb)

        output.outcome_breakdown = [
            OutcomeBreakdown(
                outcome=outcome,
                factor_count=len(factors),
                logit_sum=sum(fb.effective_logit for fb in factors),
                factors=factors,
            )
            for outcome, factors in by_outcome.items()
        ]

    return output


# --- File Writing ---


async def _append_reflection(
    session_dir: Path,
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_type: str,
) -> Path:
    """Append a timestamped reflection entry to reflection.yaml."""
    import yaml

    filepath = session_dir / "reflection.yaml"
    session_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = (
        {"timestamp": timestamp, "question_type": question_type}
        | inp.model_dump(exclude_none=True)
        | {"computed": computed.model_dump(exclude_none=True)}
    )

    content = "---\n" + yaml.dump(
        entry, default_flow_style=False, sort_keys=False, allow_unicode=True
    )

    async with aiofiles.open(filepath, "a", encoding="utf-8") as f:
        await f.write(content)

    return filepath


async def _write_trace_file(session_dir: Path, trace: str) -> Path:
    """Write the reasoning trace to a file for the reviewer to Read."""
    filepath = session_dir / "trace.md"
    session_dir.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
        await f.write(trace)
    return filepath


# --- Reviewer ---


_REVIEWER_SYSTEM_PROMPT = """\
You verify a forecasting agent's evidence chain before it commits \
to a probability. Your job is to catch concrete errors that would \
make the forecast wrong. You do not research the question \
independently or form your own probability estimate.

## What to check

- **Hallucinated evidence** — A factor cites a specific fact \
  (quote, statistic, date, event) that is NOT supported by any \
  source in the research trace. Read the trace carefully. If the \
  claim isn't grounded in a tool result, flag it.

- **Double-counting** — Two or more factors that draw on the same \
  underlying evidence. Name both factors and the shared source.

- **Wrong-direction factor** — A factor's logit sign contradicts \
  its own description. Do NOT flag factors where you simply \
  disagree with the magnitude.

- **Contradictory assessment** — The narrative assessment reaches \
  a conclusion that contradicts what the factors collectively say.

## What NOT to check

- The probability value or factor-probability gap
- Whether the agent did enough research
- Whether factor magnitudes are appropriate
- Missing scenarios or considerations
- Calibration or base rates

## Verdicts

- **fail** — You found a concrete error above that could \
  materially affect the forecast.
- **warn** — Something looks off but you're not certain it's wrong.
- **approve** — No errors found.

If you find no errors, approve and stop. Do not manufacture \
concerns. Be specific: name the factor, quote the claim, explain \
what you checked in the trace.

## Research trace

The agent's full reasoning trace is at `{trace_file}`. Read it to \
verify that factual claims in factors are grounded in actual tool \
results.

## Historical data

You have Read, Glob, and Grep access to past forecasts at:

  {traces_dir}/

Use `Glob("{traces_dir}/forecasts/**/*.json")` to list them. Each \
JSON has question_title, probability, factors, and resolution. \
Use these to check for patterns — repeated errors, systematic \
biases on this question type, or similar past forecasts.
"""


def _build_reviewer_prompt(
    inp: ReflectionInput,
    question_context: dict[str, Any] | None,
    trace_file: Path | None,
) -> str:
    """Build the prompt for the reviewer sub-agent.

    Deliberately excludes probability metrics to prevent gap commentary.
    """
    sections: list[str] = []

    if question_context:
        title = question_context.get("title", "Unknown")
        qtype = question_context.get("type", "unknown")
        resolution = question_context.get("resolution_criteria", "")
        fine_print = question_context.get("fine_print", "")
        sections.append(f"## Question\n\nTitle: {title}\nType: {qtype}")
        if resolution:
            sections.append(f"Resolution criteria: {resolution}")
        if fine_print:
            sections.append(f"Fine print: {fine_print}")

    factor_lines: list[str] = []
    for i, f in enumerate(inp.factors, 1):
        if isinstance(f.supports, NumericSupport):
            prefix = f"{i}. [{f.supports.center} ({f.supports.low}–{f.supports.high})] "
        elif f.supports is not None:
            prefix = f"{i}. [{f.supports}] "
        else:
            prefix = f"{i}. "
        factor_lines.append(
            f"{prefix}{f.description} "
            f"(logit={f.logit:+.1f}, confidence={f.confidence})"
        )
    sections.append("## Factors\n\n" + "\n".join(factor_lines))

    sections.append(f"## Assessment\n\n{inp.assessment}")

    if trace_file:
        sections.append(
            f"## Research Trace\n\n"
            f"The agent's full reasoning trace is at `{trace_file}`. "
            f"Read it to verify factual claims in the factors above."
        )

    return "\n\n".join(sections)


def _build_reviewer_hooks(allowed_dirs: list[Path]) -> HooksConfig:
    """Build permission hooks restricting the reviewer to specific directories."""
    from claude_agent_sdk import HookMatcher
    from claude_agent_sdk.types import (
        HookContext,
        HookInput,
        HookJSONOutput,
        PreToolUseHookSpecificOutput,
        SyncHookJSONOutput,
    )

    from aib.agent.hooks import create_allowed_tools_hook, merge_hooks

    allowed = ["Read", "Glob", "Grep", "WebFetch", "StructuredOutput"]
    hooks = create_allowed_tools_hook(allowed)

    if not allowed_dirs:
        return hooks

    resolved_dirs = [d.resolve() for d in allowed_dirs]

    def _deny(reason: str) -> HookJSONOutput:
        return SyncHookJSONOutput(
            hookSpecificOutput=PreToolUseHookSpecificOutput(
                hookEventName="PreToolUse",
                permissionDecision="deny",
                permissionDecisionReason=reason,
            ),
        )

    def _is_under_allowed(path: Path) -> bool:
        resolved = path.resolve()
        return any(
            resolved == d or resolved.is_relative_to(d)
            for d in resolved_dirs
        )

    async def path_hook(
        input_data: HookInput,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> HookJSONOutput:
        if input_data.get("hook_event_name") != "PreToolUse":
            return SyncHookJSONOutput()

        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})

        if tool_name in ("Read", "Glob", "Grep"):
            file_path = tool_input.get("file_path") or tool_input.get("path", "")
            if not file_path:
                dirs = ", ".join(str(d) for d in allowed_dirs)
                return _deny(f"Path required. Allowed directories: {dirs}")
            if not _is_under_allowed(Path(file_path)):
                dirs = ", ".join(str(d) for d in allowed_dirs)
                return _deny(f"Access restricted to: {dirs}")

        return SyncHookJSONOutput()

    path_hooks: HooksConfig = {
        "PreToolUse": [HookMatcher(hooks=[path_hook])],
    }
    return merge_hooks(hooks, path_hooks)


async def _run_reviewer(
    inp: ReflectionInput,
    question_context: dict[str, Any] | None,
    trace_file: Path | None,
    traces_dir: Path | None,
) -> ReviewResult | None:
    """Call a Sonnet sub-agent to review the forecast.

    Returns structured ReviewResult, or None on failure.
    """
    from claude_agent_sdk import (
        AssistantMessage as _AssistantMessage,
        ResultMessage,
    )
    from claude_agent_sdk.types import HookEvent, HookMatcher as HookMatcherType

    from aib.agent.client import build_client
    from aib.agent.display import print_block

    prompt = _build_reviewer_prompt(inp, question_context, trace_file)

    system_prompt = _REVIEWER_SYSTEM_PROMPT.format(
        trace_file=trace_file or "(not available)",
        traces_dir=traces_dir or "(not available)",
    )

    add_dirs: list[str | Path] = []
    hook_dirs: list[Path] = []
    if traces_dir and traces_dir.exists():
        add_dirs.append(traces_dir)
        hook_dirs.append(traces_dir)
    if trace_file:
        add_dirs.append(trace_file.parent)
        hook_dirs.append(trace_file.parent)

    reviewer_hooks: dict[HookEvent, list[HookMatcherType]] = cast(
        dict[HookEvent, list[HookMatcherType]],
        _build_reviewer_hooks(hook_dirs),
    )

    try:
        structured_output: dict[str, Any] | None = None
        async with build_client(
            model="sonnet",
            allowed_tools=["Read", "Glob", "Grep", "WebFetch"],
            permission_mode="bypassPermissions",
            system_prompt=system_prompt,
            hooks=reviewer_hooks,
            add_dirs=add_dirs,
            output_format={
                "type": "json_schema",
                "schema": ReviewResult.model_json_schema(),
            },
        ) as client:
            await client.query(prompt)
            async for message in client.receive_response():
                if isinstance(message, _AssistantMessage):
                    for block in message.content:
                        print_block(block, prefix="  ↳ [reviewer] ")
                elif isinstance(message, ResultMessage):
                    structured_output = message.structured_output

        if structured_output:
            return ReviewResult.model_validate(structured_output)
        return None
    except Exception:
        logger.exception("Reviewer sub-agent failed")
        return None


# --- Tool ---

_REFLECTION_DESCRIPTION = """\
Checkpoint your reasoning by committing to factors and a tentative estimate.

Returns: factor-consistency metrics, distribution metrics (for numeric/discrete),
per-outcome breakdowns (for MC), sources consulted, and an independent reviewer
verdict.

**Gate behavior:** An independent reviewer checks your evidence chain and
returns approve, warn, or fail. On fail, this tool returns an error — fix the
issues and call reflection() again. StructuredOutput is blocked until the
reviewer approves. After 3 consecutive fails, the gate auto-approves.

Binary example:
  reflection(
    factors=[
      {"description": "Strong trend in data", "logit": 1.5, "confidence": 0.8},
      {"description": "Status quo persistence", "logit": -0.5, "confidence": 0.7}
    ],
    tentative_estimate={"logit": 0.8, "probability": 0.69},
    assessment="Data shows consistent upward trend, but base rate is only 30%.",
    ...
  )

Numeric example:
  reflection(
    factors=[
      {"description": "Historical avg is 145", "supports": {"center": 145, "low": 140, "high": 150}, "logit": 1.0, "confidence": 0.9},
      {"description": "Recent uptick suggests higher", "supports": {"center": 152, "low": 148, "high": 158}, "logit": 0.8, "confidence": 0.7}
    ],
    tentative_estimate={"center": 148, "low": 142, "high": 155},
    assessment="Historical data centers around 145 but recent trend pushes higher.",
    ...
  )
"""


def _create_reflection_tool(
    session_dir: Path | None,
    question_type: str,
    get_sources: Callable[[], list[str]] | None = None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
    review_state: ReviewState | None = None,
):
    """Create the reflection tool with session context."""

    @tool("reflection", _REFLECTION_DESCRIPTION, ReflectionInput)
    @tracked("reflection")
    async def reflection_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Compute and log a reflection checkpoint."""
        try:
            validated = ReflectionInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        if session_dir is None:
            return mcp_error("reflection is not available in this context")

        computed = compute_reflection(validated, question_type)

        # Inject sources from infrastructure
        if get_sources is not None:
            computed.sources = get_sources()

        # Write trace file for reviewer
        trace_file: Path | None = None
        if session_dir and get_trace:
            trace = get_trace()
            if trace:
                trace_file = await _write_trace_file(session_dir, trace)

        # Run the reviewer sub-agent (disabled in retrodict to prevent leaks)
        review_result: ReviewResult | None = None
        if retrodict_cutoff.get() is None:
            try:
                review_result = await _run_reviewer(
                    validated,
                    question_context,
                    trace_file,
                    traces_dir,
                )
                if review_result:
                    computed.reviewer_critique = review_result.assessment
            except Exception:
                logger.exception("Reviewer failed, continuing without critique")
        elif review_state is not None:
            # Auto-approve in retrodict mode (reviewer disabled)
            review_state.record(ReviewResult(
                verdict=ReviewVerdict.approve,
                assessment="Auto-approved (retrodict mode).",
            ))

        # Record verdict for StructuredOutput gate
        if review_result and review_state is not None:
            review_state.record(review_result)

        # On reviewer crash, auto-approve so the agent isn't stuck
        if review_result is None and review_state is not None and retrodict_cutoff.get() is None:
            review_state.record(ReviewResult(
                verdict=ReviewVerdict.approve,
                assessment="Reviewer unavailable; auto-approved.",
            ))

        # Always write reflection.yaml (even on fail) for logging
        try:
            filepath = await _append_reflection(
                session_dir, validated, computed, question_type
            )
            logger.info("Appended reflection entry to %s", filepath)
        except Exception as e:
            logger.exception("Failed to write reflection")
            return mcp_error(f"Failed to write reflection: {e}")

        result_data = computed.model_dump(exclude_none=True)

        # Gate: fail verdict → tool error (unless escape hatch)
        if review_result and review_result.verdict == ReviewVerdict.fail:
            if review_state and review_state.passed:
                result_data["reviewer_note"] = (
                    f"Force-approved after {review_state.consecutive_fails} "
                    f"consecutive reviewer failures."
                )
                return mcp_success(result_data)

            return mcp_error(
                f"REVIEWER FAILED: {review_result.assessment}\n\n"
                f"Fix the issues above, then call reflection() again."
            )

        return mcp_success(result_data)

    return reflection_tool


def create_reflection_server(
    session_dir: Path | None = None,
    question_type: str = "binary",
    get_sources: Callable[[], list[str]] | None = None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
    review_state: ReviewState | None = None,
):
    """Create the reflection MCP server with session context.

    Args:
        session_dir: Session directory for reflection storage.
            If None, reflection is disabled.
        question_type: The question type for this forecast session.
        get_sources: Callback returning sources consulted so far.
            Called at reflection time to inject into output.
        get_trace: Callback returning the full reasoning trace as markdown.
            Passed to the reviewer sub-agent for context.
        question_context: Question details (title, type, resolution criteria).
            Passed to the reviewer for informed critique.
        traces_dir: Directory with past forecast JSONs.
            The reviewer gets read access to browse historical performance.
        review_state: Shared state for reviewer gate coordination
            with the StructuredOutput hook.
    """
    return create_mcp_server(
        name="notes",
        version="6.0.0",
        tools=[
            _create_reflection_tool(
                session_dir,
                question_type,
                get_sources,
                get_trace,
                question_context,
                traces_dir,
                review_state,
            )
        ],
    )
