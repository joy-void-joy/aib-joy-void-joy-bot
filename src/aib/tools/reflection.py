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

# Maximum trace length passed to the reviewer (chars).
_MAX_TRACE_LEN = 100_000


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
    logit: float
    confidence: float
    effective_logit: float


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

    # Non-binary
    factor_direction: str | None = None
    factor_strength: float | None = None

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
                logit=f.logit,
                confidence=f.confidence,
                effective_logit=f.logit * f.confidence,
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
        output.tentative_probability = 1 / (1 + math.exp(-inp.tentative_logit))
        output.gap_pp = (output.tentative_probability - output.factor_implied_probability) * 100
    else:
        output.factor_direction = (
            "positive" if factor_sum > 0 else "negative" if factor_sum < 0 else "neutral"
        )
        output.factor_strength = abs(factor_sum)

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


# --- Reviewer ---


_REVIEWER_SYSTEM_PROMPT = """\
You are a forecast reviewer — a thoughtful colleague reviewing a \
forecast before submission.

## Your role

Review the forecasting agent's reasoning process and provide feedback. \
Focus on the QUALITY OF REASONING, not on the question itself. Do not \
research the question independently, do not form your own opinion about \
the outcome, and do not provide your own probability estimate. Your job \
is to evaluate whether the agent's process was sound, not to second-guess \
its conclusion.

## What you receive

You receive the full reasoning trace: every thought, tool call, and \
result from the forecasting agent's session. Read it carefully to \
understand the research path and analytical choices.

## Historical data

You have Read, Glob, and Grep access to the agent's past work at:

  {traces_dir}/

This directory has three subdirectories:

### forecasts/<post_id>/<timestamp>.json
Structured forecast outputs. Each JSON contains:
- question_title, question_type (binary, numeric, multiple_choice, ...)
- probability (0-1 for binary), logit, factors (list of evidence items)
- resolution: null if unresolved, "yes"/"no" for binary, a number for \
numeric
- summary, sources_consulted, tool_metrics, token_usage

Use these for calibration analysis: how accurate were past forecasts at \
similar probability levels? Does the agent tend to be over- or \
underconfident on this question type?

### sessions/<post_id>/<timestamp>/
Session workspace for each forecast. Contains:
- reflection.yaml — the agent's self-assessment with factors, assessment, \
tool audit, and computed metrics
- Scratch files the agent saved during research

### logs/<post_id>_<timestamp>.md
Full reasoning logs in markdown — every thinking block, tool call, and \
result. Large files (50k+ chars). Only read these if you need to \
understand the detailed reasoning behind a specific past forecast.

### How to explore
- Glob("{traces_dir}/forecasts/**/*.json") — list all forecast JSONs
- Grep("resolution", path="{traces_dir}/forecasts/") — find resolved \
forecasts
- Read a specific JSON to inspect factors and probability
- Grep("question_type.*binary", path="{traces_dir}/forecasts/") — \
filter by type

## What to cover

**General impression**: How does the reasoning feel overall? Was the \
research thorough and well-directed, or scattered? Did the agent pursue \
the right angles for this type of question?

**Strengths**: What was done well? Solid evidence, good tool usage, \
appropriate analytical frame.

**Gaps**: What evidence might be missing? What searches weren't done \
that should have been? Do the factors all derive from the same source \
or angle? Was a key data source overlooked?

**Calibration — both directions**: Is the agent being too confident OR \
too cautious? Look for:
- Hedging toward 50% when evidence supports a stronger position \
(underconfidence is as bad as overconfidence)
- Extreme probabilities (>90% or <10%) without overwhelming evidence
- Check past forecasts for patterns at similar probability levels

**Direction**: What would you adjust? Frame as a suggestion: \
"I think the probability could be higher/lower because..." or \
"The reasoning looks solid, I wouldn't change anything."

Be specific. Reference factors, tool results, or past forecasts by name.
"""


def _build_reviewer_prompt(
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_context: dict[str, Any] | None,
    trace: str,
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
        f"- {f.description} (logit={f.logit}, confidence={f.confidence}, "
        f"effective={f.logit * f.confidence:.2f})"
        for f in inp.factors
    )
    sections.append(f"## Factors\n\n{factors_text}")

    if computed.factor_implied_probability is not None:
        sections.append(
            f"Factor-implied probability: {computed.factor_implied_probability:.1%}\n"
            f"Tentative probability: {computed.tentative_probability:.1%}\n"
            f"Gap: {computed.gap_pp:+.1f}pp"
        )
    else:
        sections.append(
            f"Factor direction: {computed.factor_direction}\n"
            f"Factor strength: {computed.factor_strength:.2f}"
        )

    sections.append(f"## Assessment\n\n{inp.assessment}")
    sections.append(f"## Tool Audit\n\n{inp.tool_audit}")

    if trace:
        sections.append(f"## Full Reasoning Trace\n\n{trace[:_MAX_TRACE_LEN]}")

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
    trace: str,
    traces_dir: Path | None,
) -> str | None:
    """Call a Sonnet sub-agent to review the forecast.

    The reviewer has Read/Glob/Grep access to past forecasts and
    WebFetch for additional research.

    Returns the reviewer's freeform critique, or None on failure.
    """
    from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, ResultMessage
    from claude_agent_sdk.types import HookEvent, HookMatcher as HookMatcherType

    prompt = _build_reviewer_prompt(inp, computed, question_context, trace)

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
                if isinstance(message, ResultMessage) and message.result:
                    result_text = message.result
        return result_text or None
    except Exception:
        logger.exception("Reviewer sub-agent failed")
        return None


# --- Tool ---

_REFLECTION_DESCRIPTION = """\
Checkpoint your reasoning by providing your current factors and tentative logit.

Returns computed analysis: factor-implied probability (for binary), gap between
your tentative estimate and what your factors imply, per-factor breakdown,
sources consulted, AND a reviewer critique from an independent sub-agent that
checks for blind spots, calibration issues, and underconfidence.

Call this at least once before your final StructuredOutput. You can call it
multiple times as your analysis evolves.

Example:
  reflection(
    factors=[
      {"description": "Strong trend in data", "logit": 1.5, "confidence": 0.8},
      {"description": "Status quo persistence", "logit": -0.5, "confidence": 0.7}
    ],
    tentative_logit=0.8,
    assessment="Data shows consistent upward trend across 3 sources, but the historical base rate for this type of change is only 30%. The trend is recent (last 6 months) so may not persist.",
    tool_audit="search_exa provided good results for recent data. fetch_url failed on the government stats page (403). FRED had no relevant series.",
    process_reflection="Felt well-supported on the research phase — web search and FRED covered what I needed. But the numeric CDF step felt like guessing; I had point estimates but no good way to translate them into a distribution shape. A tool that fits distributions from historical forecast errors would remove a lot of friction there."
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

        # Run the reviewer sub-agent
        trace = get_trace() if get_trace else ""
        try:
            critique = await _run_reviewer(
                validated, computed, question_context, trace, traces_dir,
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
