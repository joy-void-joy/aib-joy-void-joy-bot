"""Premortem reviewer tool for forecasting sessions.

Independent Opus sub-agent that reviews the forecasting agent's evidence
chain and forces adversarial self-examination before it commits to a
probability. Gates StructuredOutput.

Requires reflection() to have been called first — reads the cached
ReflectionInput from ReviewState to build the reviewer prompt.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import aiofiles
from pydantic import BaseModel, Field, ValidationError

from claude_agent_sdk import TextBlock, ToolUseBlock, tool

from aib.agent.hooks import HooksConfig
from aib.agent.nested import NestedAgentReport
from aib.agent.models import (
    BinaryEstimate,
    MultipleChoiceEstimate,
    NumericEstimate,
    NumericSupport,
)
from aib.agent.session import ReviewResult, ReviewState, ReviewVerdict
from aib.paths import WORLDVIEW_PATH
from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import get_collector, tracked
from aib.tools.responses import mcp_error, mcp_success

if TYPE_CHECKING:
    from aib.tools.reflection import ReflectionInput

logger = logging.getLogger(__name__)


# --- Input Model ---


class PremortemInput(BaseModel):
    """Forces the agent to argue against itself before final submission."""

    counterargument: str = Field(
        description=(
            "The strongest case AGAINST your forecast. What would a smart "
            "disagreer say? Construct the most compelling argument for the "
            "opposite conclusion, citing specific evidence from your research. "
            "Not a token gesture — a real attempt to break your own forecast."
        ),
    )
    what_would_change_my_mind: str = Field(
        description=(
            "Name specific, concrete evidence that would shift your probability "
            "by at least 10pp. Not vague scenarios — what data, announcement, "
            "or observation would you need to see? Be concrete enough that you "
            "could set up an alert for it."
        ),
    )
    confidence_in_estimate: float = Field(
        ge=0.0,
        le=1.0,
        description=(
            "How confident are you that your probability is within 10pp of the "
            "true value? 0.9 = very confident, 0.5 = could easily be wrong."
        ),
    )


# --- Reviewer System Prompt ---


_REVIEWER_SYSTEM_PROMPT = """\
You verify a forecasting agent's evidence chain before it commits \
to a probability. Your job is to catch concrete errors that would \
make the forecast wrong and to challenge the probability when the \
evidence doesn't support it. You do not research the question \
independently — you work from the agent's trace, factors, and \
adversarial self-examination.

## What to check

- **Hallucinated evidence** — A factor's core claim has NO support \
  in the research trace. Read the trace carefully. Focus on whether \
  the *conclusion* is grounded, not whether every specific detail \
  matches verbatim. Only flag as hallucination when the core claim \
  itself — the thing that moves the forecast — has no trace support.

- **Double-counting** — Two or more factors that draw on the same \
  underlying evidence. Name both factors and the shared source.

- **Wrong-direction factor** — A factor's logit sign contradicts \
  its own description. Do NOT flag factors where you simply \
  disagree with the magnitude.

- **Contradictory assessment** — The narrative assessment reaches \
  a conclusion that contradicts what the factors collectively say.

- **Missing resolution criteria** — If the question section shows \
  resolution criteria as MISSING, check whether the trace shows \
  an attempt to recover them (e.g., a fetch_url call for the \
  Metaculus question page). If the agent did not attempt recovery, \
  this is always at least a **warn** — the agent's prompt \
  explicitly requires fetching the page. Question titles can be \
  misleading; resolution criteria define what actually counts as \
  YES/NO, what source is authoritative, and what edge cases apply.

- **Resolution misalignment** — When resolution criteria ARE \
  provided, check whether the factors and assessment engage with \
  the specific terms. Examples: criteria cite a specific source \
  but the agent used a different one; criteria define a threshold \
  the agent didn't evaluate; criteria specify a timeframe the \
  factors ignore.

- **Pre-publication event** — If a factor claims an event already \
  satisfies the resolution criteria AND the question's Published \
  date is AFTER that event, determine which case applies:
  \
  **Case 1 — Resolution criteria specify an explicit start date \
  BEFORE published_at** (e.g., "on or after Feb 24" when \
  published_at is March 13): Events within that window are \
  legitimate. Verify the event falls within the stated range and \
  that the primary source confirms the claim. Not a problem.
  \
  **Case 2 — No explicit start date, or start date >= \
  published_at** (typical "Will X happen before Y?" questions): \
  The agent should NOT treat the pre-publication event as already \
  resolving the question. If the pre-publication event is the \
  dominant factor and the probability would collapse without it, \
  this is a **fail**. The event can still be used as base-rate \
  evidence (e.g., "high recent frequency"), \
  but the forecast must be built on forward-looking probability \
  from published_at to resolution. Common rationalizations that \
  do NOT override Case 2: "bot-generated question", "literal \
  reading of criteria."

- **Regime-spanning data window** (numeric/discrete only) — If the \
  agent ran a Monte Carlo simulation or computed drift/volatility from \
  historical data, check whether the data window includes a structural \
  break (e.g., a rate level change after a policy decision, a price \
  regime shift after a major event). If the trace shows the agent \
  used data spanning two clearly different regimes to estimate drift, \
  this is a **warn** — the drift estimate is contaminated by the \
  regime transition, not representative of current dynamics.

- **Weak counterargument** — The agent's submitted counterargument \
  is a token gesture rather than a real attempt to break its own \
  forecast. Examples: restating the conclusion in negative form, \
  naming only hypothetical scenarios with no evidentiary basis, \
  or citing evidence already discounted in the factors. A strong \
  counterargument constructs a coherent alternative story a smart \
  disagreer would actually tell. If the counterargument is weak, \
  this is a **warn** — the agent hasn't genuinely argued against \
  itself.

- **Overconfident self-assessment** — The agent's \
  confidence_in_estimate is inconsistent with the evidence quality. \
  If the agent reports 0.9 confidence but the factors are thin, \
  the anchor is uncertain, or the research left major gaps open, \
  this is a **warn**. Calibrated self-confidence requires acknowledging \
  uncertainty that actually exists.

- **Probability assessment** — After reviewing the factors and \
  trace, form your own independent probability estimate based on \
  the evidence. If your estimate meaningfully differs from the \
  agent's tentative probability, this is a **fail** — state what \
  you think the probability should be and why. Don't just flag the \
  gap; explain what evidence the agent is over- or under-weighting. \
  Common failure modes: hedging toward round numbers without \
  evidentiary support, anchoring on an intuition that isn't captured \
  in any factor, double-discounting uncertainty already reflected in \
  factor confidence values, or ignoring strong evidence that should \
  dominate the estimate.

- **Anchor divergence** — The agent states an anchor (reference \
  class base rate) and a final probability. If they diverge \
  significantly, check whether the factors justify the distance. \
  Large departures from well-sourced anchors need strong, verified \
  evidence — not an accumulation of mild narrative factors. If the \
  agent's three weakest factors were removed and the probability \
  would snap back toward the anchor, the departure may be \
  narrative-driven rather than evidence-driven. This is a **warn** \
  if the anchor is well-sourced and the departure exceeds ~20pp \
  without a single strong factor (|logit| >= 2.0) driving it.

## What NOT to check

- Whether the agent did enough research (but resolution criteria \
  recovery IS your concern)
- Scenarios the agent could have researched but didn't

## Verdicts

- **fail** — A core claim is fabricated (no trace support) AND \
  correcting it would change the forecast; OR the probability is \
  meaningfully wrong given the evidence (state your estimate).
- **warn** — An error that doesn't affect the forecast direction. \
  Includes: unsupported details when the underlying conclusion is \
  well-grounded, missing resolution criteria with no recovery \
  attempt, weak counterargument, overconfident self-assessment, or \
  factors that don't clearly map to the resolution criteria's \
  specific terms.
- **approve** — No errors found, or only trivial issues.

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

## Worldview store

You have Read, Glob, and Grep access to the worldview store at:

  {worldview_dir}/

This contains persisted research and sub-forecasts from the agent's \
current and prior sessions. Use it for three consistency checks:

- **Binary vs numeric consistency** — If the agent is forecasting a \
  binary threshold question (e.g., "Will X exceed 2,000?"), search \
  `{worldview_dir}/forecasts/` for a numeric sub-forecast on the \
  same underlying quantity. If one exists and has a CDF, the binary \
  probability should be consistent with the CDF-implied threshold \
  probability. Flag meaningful gaps (>10pp) as a **fail** — the \
  agent should derive the binary probability from the CDF, not \
  reason about it independently.

- **Cross-question consistency** — Search for worldview forecast \
  entries related to the current question (by keyword overlap in \
  question titles or tags). If you find entries that make \
  contradictory predictions about the same underlying quantity or \
  event, flag as a **warn**.

- **Research contradictions** — Search `{worldview_dir}/research/` \
  for entries whose key_facts or data_points contradict factual \
  claims in the agent's factors. If worldview research says X but a \
  factor assumes not-X, and the research entry is fresh (state is \
  "fresh"), this is a **warn**. If the contradiction would change \
  the forecast direction, it's a **fail**.

To search: `Grep("keyword", path="{worldview_dir}/", glob="*.json")` \
or `Glob("{worldview_dir}/forecasts/*.json")`. Each JSON entry has \
fields: question, question_type, probability, cdf, factors, summary, \
state, key_facts (research), data_points (research).
"""


# --- Prompt Building ---


def build_tool_metrics_section(summary: dict[str, Any]) -> str:
    """Render the programmatic tool-call metrics for the reviewer.

    The reviewer uses this as ground truth when cross-checking the agent's
    narrative tool_audit field.
    """
    lines = [
        "## Tool Metrics (ground truth)",
        "",
        (
            f"Session: {summary['total_tool_calls']} calls, "
            f"{summary['total_errors']} errors "
            f"({summary['overall_error_rate']} error rate)."
        ),
        "",
        "Per tool (name, calls, error rate, avg ms):",
    ]
    for name, m in sorted(summary.get("by_tool", {}).items()):
        lines.append(
            f"- {name}: {m['call_count']} calls, {m['error_rate']} errors, "
            f"{m['avg_duration_ms']:.0f}ms avg"
        )
    lines.append("")
    lines.append(
        "Flag any claim in the agent's tool_audit that disagrees with these "
        "numbers (e.g. 'no tool failures' when the error count above is non-zero)."
    )
    return "\n".join(lines)


def build_reviewer_prompt(
    reflection_input: ReflectionInput,
    premortem_input: PremortemInput,
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
        published_at = question_context.get("published_at", "")
        close_time = question_context.get("scheduled_close_time", "")
        resolve_time = question_context.get("scheduled_resolve_time", "")
        header = f"## Question\n\nTitle: {title}\nType: {qtype}"
        if published_at:
            header += f"\nPublished: {published_at}"
        if close_time:
            header += f"\nCloses: {close_time}"
        if resolve_time:
            header += f"\nResolves: {resolve_time}"
        sections.append(header)
        if resolution and not resolution.startswith("MISSING"):
            sections.append(f"Resolution criteria: {resolution}")
        else:
            sections.append(
                "Resolution criteria: MISSING (agent should have fetched the question page)"
            )
        if fine_print and not fine_print.startswith("MISSING"):
            sections.append(f"Fine print: {fine_print}")

    factor_lines: list[str] = []
    for i, f in enumerate(reflection_input.factors, 1):
        if isinstance(f.supports, NumericSupport):
            prefix = f"{i}. [{f.supports.center} ({f.supports.low}–{f.supports.high})] "
        elif f.supports is not None:
            prefix = f"{i}. [{f.supports}] "
        else:
            prefix = f"{i}. "
        factor_lines.append(
            f"{prefix}{f.description} (logit={f.logit:+.1f}, confidence={f.confidence})"
        )
    sections.append("## Factors\n\n" + "\n".join(factor_lines))

    if reflection_input.anchor:
        sections.append(f"## Anchor\n\n{reflection_input.anchor}")

    sections.append(f"## Assessment\n\n{reflection_input.assessment}")

    estimate = reflection_input.tentative_estimate
    if isinstance(estimate, BinaryEstimate):
        sections.append(
            f"## Tentative estimate\n\nProbability: {estimate.probability:.1%}"
        )
    elif isinstance(estimate, NumericEstimate):
        sections.append(
            f"## Tentative estimate\n\n"
            f"Center: {estimate.center}, Range: {estimate.low}–{estimate.high}"
        )
    elif isinstance(estimate, MultipleChoiceEstimate):
        prob_lines = [
            f"  {opt}: {p:.1%}" for opt, p in sorted(estimate.probabilities.items())
        ]
        sections.append(
            "## Tentative estimate\n\nProbabilities:\n" + "\n".join(prob_lines)
        )

    sections.append(
        "## Agent's adversarial self-examination\n\n"
        f"**Counterargument:** {premortem_input.counterargument}\n\n"
        f"**What would change my mind:** {premortem_input.what_would_change_my_mind}\n\n"
        f"**Confidence in estimate (0-1):** {premortem_input.confidence_in_estimate:.2f}"
    )

    if reflection_input.tool_audit:
        sections.append(
            f"## Tool audit (agent's narrative)\n\n{reflection_input.tool_audit}"
        )

    metrics_summary = get_collector().get_summary()
    if metrics_summary.get("total_tool_calls", 0) > 0:
        sections.append(build_tool_metrics_section(metrics_summary))

    if trace_file:
        sections.append(
            f"## Research Trace\n\n"
            f"The agent's full reasoning trace is at `{trace_file}`. "
            f"Read it to verify factual claims in the factors above."
        )

    return "\n\n".join(sections)


def build_reviewer_hooks(allowed_dirs: list[Path]) -> HooksConfig:
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

    allowed = [
        "Read",
        "Glob",
        "Grep",
        "mcp__search__web_search",
        "mcp__search__fetch_url",
        "StructuredOutput",
    ]
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
        return any(resolved == d or resolved.is_relative_to(d) for d in resolved_dirs)

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


# --- Trace File Writing ---


async def write_trace_file(session_dir: Path, trace: str) -> Path:
    """Write the reasoning trace to a file for the reviewer to Read."""
    filepath = session_dir / "trace_at_premortem.md"
    session_dir.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
        await f.write(trace)
    return filepath


# --- Reviewer Invocation ---


async def run_reviewer(
    reflection_input: ReflectionInput,
    premortem_input: PremortemInput,
    question_context: dict[str, Any] | None,
    trace_file: Path | None,
    traces_dir: Path | None,
) -> NestedAgentReport[ReviewResult]:
    """Call an Opus sub-agent to review the forecast.

    Returns a NestedAgentReport wrapping the ReviewResult (or None if
    the sub-agent failed), the agent's final text block, and any error.
    """
    from claude_agent_sdk import (
        AssistantMessage as _AssistantMessage,
        ResultMessage,
    )
    from claude_agent_sdk.types import HookEvent, HookMatcher as HookMatcherType

    from aib.agent.client import build_client
    from aib.agent.display import make_agent_prefix, print_block

    prompt = build_reviewer_prompt(
        reflection_input, premortem_input, question_context, trace_file
    )

    system_prompt = _REVIEWER_SYSTEM_PROMPT.format(
        trace_file=trace_file or "(not available)",
        traces_dir=traces_dir or "(not available)",
        worldview_dir=WORLDVIEW_PATH,
    )

    add_dirs: list[str | Path] = [WORLDVIEW_PATH]
    hook_dirs: list[Path] = [WORLDVIEW_PATH]
    if traces_dir and traces_dir.exists():
        add_dirs.append(traces_dir)
        hook_dirs.append(traces_dir)
    if trace_file:
        add_dirs.append(trace_file.parent)
        hook_dirs.append(trace_file.parent)

    reviewer_hooks: dict[HookEvent, list[HookMatcherType]] = cast(
        dict[HookEvent, list[HookMatcherType]],
        build_reviewer_hooks(hook_dirs),
    )

    from aib.config import settings
    from aib.tools.search import fetch_url, web_search

    search_servers = {
        "search": create_mcp_server("search", tools=[web_search, fetch_url]),
    }

    try:
        structured_output: dict[str, Any] | None = None
        so_tool_blocks: list[ToolUseBlock] = []
        text_blocks: list[str] = []
        review_label = question_context.get("title") if question_context else None
        prefix = make_agent_prefix("premortem", review_label)
        async with build_client(
            model=settings.model,
            allowed_tools=[
                "Read",
                "Glob",
                "Grep",
                "mcp__search__web_search",
                "mcp__search__fetch_url",
            ],
            mcp_servers=search_servers,
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
                        print_block(block, prefix=prefix)
                        if (
                            isinstance(block, ToolUseBlock)
                            and block.name == "StructuredOutput"
                        ):
                            so_tool_blocks.append(block)
                        elif isinstance(block, TextBlock):
                            text_blocks.append(block.text)
                elif isinstance(message, ResultMessage):
                    structured_output = message.structured_output
                    if message.total_cost_usd is not None:
                        get_collector().record_cost("premortem", message.total_cost_usd)

        final_text = text_blocks[-1] if text_blocks else ""

        if structured_output:
            return NestedAgentReport[ReviewResult](
                payload=ReviewResult.model_validate(structured_output),
                final_text=final_text,
            )

        if so_tool_blocks:
            last_block = so_tool_blocks[-1]
            try:
                json_output = last_block.input["json_output"]
                result = ReviewResult.model_validate(json_output)
                logger.warning(
                    "Recovered premortem verdict from ToolUseBlock fallback: %s",
                    result.verdict,
                )
                return NestedAgentReport[ReviewResult](
                    payload=result,
                    final_text=final_text,
                )
            except (KeyError, ValidationError):
                logger.warning(
                    "Premortem reviewer produced %d StructuredOutput blocks but "
                    "none could be parsed as ReviewResult",
                    len(so_tool_blocks),
                )

        return NestedAgentReport[ReviewResult](
            final_text=final_text,
            error="reviewer produced no parseable structured output",
        )
    except Exception as e:
        logger.exception("Premortem reviewer sub-agent failed")
        return NestedAgentReport[ReviewResult](
            error=f"{type(e).__name__}: {e}",
        )


# --- Tool ---

_PREMORTEM_DESCRIPTION = """\
Run the premortem reviewer before submitting your final forecast.

Requires reflection() to have been called first — the reviewer reads your
most recent reflection input (factors, assessment, tentative estimate) and
combines it with the adversarial fields you provide here.

**What you must provide:**
- **counterargument** — The strongest case AGAINST your forecast. Argue it
  seriously — if a smart disagreer looked at the same evidence, what would
  their coherent alternative story be?
- **what_would_change_my_mind** — Specific evidence that would shift your
  probability by ≥10pp. Not vague scenarios; concrete observables.
- **confidence_in_estimate** — 0-1 scale. How confident that your probability
  is within 10pp of the true value?

**Gate behavior:** The reviewer returns approve, warn, or fail. On **fail**,
this tool returns an error — fix the issues and call premortem() again.
StructuredOutput is blocked until premortem returns approve or warn (or after
3 consecutive fails, the gate auto-approves as an escape hatch).

Call premortem() exactly once per forecast, after your final reflection() call.
"""


def create_premortem_tool(
    session_dir: Path | None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
    review_state: ReviewState | None = None,
):
    """Create the premortem tool with session context."""

    @tool("premortem", _PREMORTEM_DESCRIPTION, PremortemInput)
    @tracked("premortem")
    async def premortem_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Run the premortem reviewer and gate StructuredOutput."""
        try:
            validated = PremortemInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        if session_dir is None or review_state is None:
            return mcp_error("premortem is not available in this context")

        if not review_state.reflection_done:
            return mcp_error(
                "You must call reflection() before premortem(). "
                "Commit to your factors and tentative estimate first."
            )

        reflection_input = review_state.last_reflection_input

        trace_file: Path | None = None
        if get_trace:
            trace = get_trace()
            if trace:
                trace_file = await write_trace_file(session_dir, trace)

        if retrodict_cutoff.get() is not None:
            review_state.record(
                ReviewResult(
                    verdict=ReviewVerdict.approve,
                    assessment="Reviewer unavailable; auto-approved.",
                ),
                reflection_input=reflection_input,
            )
            return mcp_success(
                {
                    "verdict": "approve",
                    "assessment": "Reviewer unavailable; auto-approved.",
                }
            )

        review_result: ReviewResult | None = None
        try:
            review_report = await run_reviewer(
                reflection_input,
                validated,
                question_context,
                trace_file,
                traces_dir,
            )
            review_result = review_report.payload
        except Exception:
            logger.exception("Premortem reviewer crashed")

        if review_result is None:
            logger.warning("Premortem reviewer returned None — auto-approving")
            review_state.record(
                ReviewResult(
                    verdict=ReviewVerdict.approve,
                    assessment="Reviewer unavailable; auto-approved.",
                ),
                reflection_input=reflection_input,
            )
            return mcp_success(
                {
                    "verdict": "approve",
                    "assessment": "Reviewer unavailable; auto-approved.",
                }
            )

        review_state.record(review_result, reflection_input=reflection_input)
        logger.info(
            "Premortem verdict: %s (consecutive_fails=%d)",
            review_result.verdict,
            review_state.consecutive_fails,
        )

        if review_result.verdict == ReviewVerdict.fail:
            if review_state.passed:
                logger.warning(
                    "Escape hatch: force-approving after %d consecutive fails",
                    review_state.consecutive_fails,
                )
                return mcp_success(
                    {
                        "verdict": "fail",
                        "assessment": review_result.assessment,
                        "note": (
                            f"Force-approved after {review_state.consecutive_fails} "
                            f"consecutive reviewer failures."
                        ),
                    }
                )
            return mcp_error(
                f"REVIEWER FAILED: {review_result.assessment}\n\n"
                f"Fix the issues above, then call premortem() again."
            )

        return mcp_success(
            {
                "verdict": review_result.verdict.value,
                "assessment": review_result.assessment,
            }
        )

    return premortem_tool


def create_premortem_server(
    session_dir: Path | None = None,
    get_trace: Callable[[], str] | None = None,
    question_context: dict[str, Any] | None = None,
    traces_dir: Path | None = None,
    review_state: ReviewState | None = None,
):
    """Create the premortem MCP server with session context.

    Args:
        session_dir: Session directory for trace file storage.
            If None, premortem is disabled.
        get_trace: Callback returning the full reasoning trace as markdown.
            Passed to the reviewer sub-agent for context.
        question_context: Question details (title, type, resolution criteria).
            Passed to the reviewer for informed critique.
        traces_dir: Directory with past forecast JSONs.
            The reviewer gets read access to browse historical performance.
        review_state: Shared state for gate coordination with reflection
            and the StructuredOutput hook.
    """
    return create_mcp_server(
        name="premortem",
        version="1.0.0",
        tools=[
            create_premortem_tool(
                session_dir,
                get_trace,
                question_context,
                traces_dir,
                review_state,
            )
        ],
    )
