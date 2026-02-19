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
from pathlib import Path
from typing import Any, cast

import aiofiles
from pydantic import BaseModel, Field

from claude_agent_sdk import tool

from aib.agent.hooks import HooksConfig
from aib.agent.models import Factor
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
    tentative_logit: float = Field(
        description="Your current synthesized log-odds estimate."
    )
    tentative_probability: float = Field(
        description=(
            "Your current probability estimate (0.0-1.0). "
            "For binary: your forecast probability. "
            "For MC: probability of the most likely option. "
            "This is the number you plan to submit."
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
    next_steps: str | None = Field(
        default=None,
        description="What you plan to research or verify next.",
    )
    skip_reviewer: bool = Field(
        default=False,
        description="Skip the reviewer sub-agent. Use for simple questions where computed metrics suffice.",
    )


# --- Output Models ---


class FactorBreakdown(BaseModel):
    """Per-factor effective logit computation."""

    description: str
    supports: str | float | None = None
    logit: float
    confidence: float
    effective_logit: float
    conditional: str | None = None


class OutcomeBreakdown(BaseModel):
    """Per-outcome factor aggregation for non-binary questions."""

    outcome: str | float
    factor_count: int
    logit_sum: float
    factors: list[FactorBreakdown]


class ReflectionOutput(BaseModel):
    """Computed feedback from a reflection checkpoint."""

    factor_count: int
    factor_sum: float
    tentative_logit: float
    logit_gap: float
    neutral_factor_count: int
    factor_breakdown: list[FactorBreakdown]
    dominant_factor: str | None = None
    dominant_effective_logit: float | None = None

    # Binary-specific
    factor_implied_probability: float | None = None
    tentative_probability: float | None = None
    gap_pp: float | None = None

    # Non-binary: per-outcome aggregation
    outcome_breakdown: list[OutcomeBreakdown] | None = None

    # Sources consulted so far (populated from infrastructure)
    sources: list[str] = Field(default_factory=list)

    # Reviewer critique (populated by Sonnet sub-agent)
    reviewer_critique: str | None = None


# --- Computation ---


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

    output = ReflectionOutput(
        factor_count=len(inp.factors),
        factor_sum=factor_sum,
        tentative_logit=inp.tentative_logit,
        logit_gap=inp.tentative_logit - factor_sum,
        neutral_factor_count=neutral_count,
        factor_breakdown=breakdown,
        dominant_factor=dominant.description if dominant else None,
        dominant_effective_logit=dominant.effective_logit if dominant else None,
    )

    if question_type == "binary":
        output.factor_implied_probability = 1 / (1 + math.exp(-factor_sum))
        output.tentative_probability = inp.tentative_probability
        output.gap_pp = (inp.tentative_probability - output.factor_implied_probability) * 100
    else:
        # Group factors by supported outcome
        from collections import defaultdict

        by_outcome: dict[str | float, list[FactorBreakdown]] = defaultdict(list)
        for fb in breakdown:
            if fb.supports is not None:
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
You audit a forecasting agent's reasoning before it commits to a \
probability. Your job is to catch errors — in either direction.

Underconfidence is as costly as overconfidence. An agent that \
hedges toward 50% when evidence supports 25% loses just as many \
Brier points as one that claims 5% when evidence supports 25%.

Don't recommend a specific probability. The agent owns the number.

## What to flag

**Errors that inflate confidence (push away from 50%):**
- A factor coded in the wrong direction (name it)
- Confidence on a factor the evidence doesn't support
- Two factors double-counting the same underlying evidence

**Errors that deflate confidence (push toward 50%):**
- Tentative probability closer to 50% than factor-implied, \
  without an explicit factor justifying the adjustment
- Weak "hedge factors" added for balance rather than because \
  they carry real evidentiary weight — a factor with logit \
  +/-0.3 and confidence 0.5 contributes almost nothing and \
  may exist only to feel even-handed
- Assessment narrative that reads as strongly directional while \
  the probability sits near 50%

**Structural issues (either direction):**
- The assessment narrative contradicting its own factors
- An implicit assumption not captured in the factor list
- A scenario missing from the factors that could materially \
  shift the estimate (up to 2 — one in each direction)

If you don't find real issues, say so briefly and stop. Be direct \
and specific — name the factor, cite the number, explain the error.

## Past forecasts

You have Read, Glob, and Grep access to resolved forecasts at:

  {traces_dir}/forecasts/<post_id>/<timestamp>.json

Each JSON has: probability, logit, factors, resolution (null if \
unresolved, "yes"/"no" for binary, number for numeric). If you \
spot a calibration pattern, cite the specific forecasts and \
outcomes.

## Format

Write like a colleague reviewing a draft — direct, specific, \
concise. No praise unless there's genuinely nothing to flag.
"""


def _build_reviewer_prompt(
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_context: dict[str, Any] | None,
    trace_file: Path | None,
) -> str:
    """Build the prompt for the reviewer sub-agent."""
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

    factors_text = "\n".join(
        (f"- [{f.supports}] " if f.supports is not None else "- ")
        + f"{f.description} "
        + f"(logit={f.logit:+.1f}, confidence={f.confidence}, "
        + f"effective={f.logit * f.confidence:+.2f})"
        for f in inp.factors
    )
    sections.append(f"## Factors\n\n{factors_text}")

    if computed.factor_implied_probability is not None:
        sections.append(
            f"## Probabilities\n\n"
            f"Factor-implied: {computed.factor_implied_probability:.1%}\n"
            f"Agent's probability: {computed.tentative_probability:.1%}\n"
            f"Gap: {computed.gap_pp:+.1f}pp"
        )
    elif computed.outcome_breakdown:
        lines = []
        for ob in computed.outcome_breakdown:
            lines.append(f"- {ob.outcome}: {ob.factor_count} factors, logit sum = {ob.logit_sum:.2f}")
        sections.append("## Per-Outcome Breakdown\n\n" + "\n".join(lines))

    sections.append(f"## Assessment\n\n{inp.assessment}")
    sections.append(f"## Tool Audit\n\n{inp.tool_audit}")

    if inp.next_steps:
        sections.append(f"## Agent's Planned Next Steps\n\n{inp.next_steps}")

    if trace_file:
        sections.append(
            f"## Research Trace\n\n"
            f"The agent's research trace is at `{trace_file}`. "
            f"It covers the research phase (tool calls, web searches, "
            f"data gathering) up to when the agent called reflection. "
            f"The assessment and factors above summarize the agent's "
            f"conclusions from this research."
        )

    return "\n\n".join(sections)


def _build_reviewer_hooks(traces_dir: Path | None) -> HooksConfig:
    """Build permission hooks restricting the reviewer to past forecasts."""
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

    if traces_dir is None:
        return hooks

    resolved_dir = traces_dir.resolve()

    def _deny(reason: str) -> HookJSONOutput:
        return SyncHookJSONOutput(
            hookSpecificOutput=PreToolUseHookSpecificOutput(
                hookEventName="PreToolUse",
                permissionDecision="deny",
                permissionDecisionReason=reason,
            ),
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
                return _deny(
                    f"Path required. Browse past forecasts at: {traces_dir}",
                )
            try:
                resolved = Path(file_path).resolve()
                resolved.relative_to(resolved_dir)
            except (ValueError, OSError):
                return _deny(
                    f"Access restricted to: {traces_dir}",
                )

        return SyncHookJSONOutput()

    path_hooks: HooksConfig = {
        "PreToolUse": [HookMatcher(hooks=[path_hook])],
    }
    return merge_hooks(hooks, path_hooks)


async def _run_reviewer(
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_context: dict[str, Any] | None,
    trace_file: Path | None,
    traces_dir: Path | None,
) -> str | None:
    """Call a Sonnet sub-agent to review the forecast.

    The reviewer has Read/Glob/Grep access to past forecasts and
    WebFetch for additional research.

    Returns the reviewer's freeform critique, or None on failure.
    """
    from claude_agent_sdk import (
        AssistantMessage as _AssistantMessage,
        ClaudeAgentOptions,
        ClaudeSDKClient,
        ResultMessage,
    )
    from claude_agent_sdk.types import HookEvent, HookMatcher as HookMatcherType

    from aib.agent.display import print_block

    prompt = _build_reviewer_prompt(inp, computed, question_context, trace_file)

    system_prompt = _REVIEWER_SYSTEM_PROMPT.format(
        traces_dir=traces_dir or "(not available)",
    )

    add_dirs: list[str | Path] = []
    if traces_dir and traces_dir.exists():
        add_dirs.append(traces_dir)

    reviewer_hooks: dict[HookEvent, list[HookMatcherType]] = cast(
        dict[HookEvent, list[HookMatcherType]],
        _build_reviewer_hooks(traces_dir),
    )

    options = ClaudeAgentOptions(
        model="sonnet",
        allowed_tools=["Read", "Glob", "Grep", "WebFetch"],
        permission_mode="bypassPermissions",
        system_prompt=system_prompt,
        hooks=reviewer_hooks,
        add_dirs=add_dirs,
        extra_args={"no-session-persistence": None},
    )

    try:
        result_text = ""
        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)
            async for message in client.receive_response():
                if isinstance(message, _AssistantMessage):
                    for block in message.content:
                        print_block(block, prefix="  ↳ [reviewer] ")
                elif isinstance(message, ResultMessage) and message.result:
                    result_text = message.result
        return result_text or None
    except Exception:
        logger.exception("Reviewer sub-agent failed")
        return None


# --- Tool ---

_REFLECTION_DESCRIPTION = """\
Checkpoint your reasoning by committing to factors, a logit, and a probability.

Returns: factor-consistency metrics, per-outcome breakdowns (for MC/numeric),
sources consulted, and an independent reviewer audit that checks for errors
in both directions (overconfidence AND underconfidence/hedging).

Call at least once before your final StructuredOutput. Use skip_reviewer=True
for intermediate checkpoints where you only need metrics.

Example:
  reflection(
    factors=[
      {"description": "Strong trend in data", "logit": 1.5, "confidence": 0.8},
      {"description": "Status quo persistence", "logit": -0.5, "confidence": 0.7}
    ],
    tentative_logit=0.8,
    tentative_probability=0.69,
    assessment="Data shows consistent upward trend across 3 sources, but the historical base rate for this type of change is only 30%.",
    tool_audit="search_exa provided good results. fetch_url failed on the government stats page (403).",
    process_reflection="Web search and FRED covered what I needed. Numeric CDF step felt like guessing.",
    next_steps="Will check the official government release schedule next."
  )
"""


def _create_reflection_tool(
    session_dir: Path | None,
    question_type: str,
    get_sources: Callable[[], list[str]] | None = None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
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

        # Run the reviewer sub-agent
        if not validated.skip_reviewer:
            try:
                critique = await _run_reviewer(
                    validated, computed, question_context, trace_file, traces_dir,
                )
                computed.reviewer_critique = critique
            except Exception:
                logger.exception("Reviewer failed, continuing without critique")

        try:
            filepath = await _append_reflection(
                session_dir, validated, computed, question_type
            )
            logger.info("Appended reflection entry to %s", filepath)
        except Exception as e:
            logger.exception("Failed to write reflection")
            return mcp_error(f"Failed to write reflection: {e}")

        return mcp_success(computed.model_dump(exclude_none=True))

    return reflection_tool


def create_reflection_server(
    session_dir: Path | None = None,
    question_type: str = "binary",
    get_sources: Callable[[], list[str]] | None = None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
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

    Returns:
        MCP server configured with the reflection tool.
    """
    return create_mcp_server(
        name="notes",
        version="5.0.0",
        tools=[
            _create_reflection_tool(
                session_dir,
                question_type,
                get_sources,
                get_trace,
                question_context,
                traces_dir,
            )
        ],
    )
