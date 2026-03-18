"""Forecasting agent using Claude Agent SDK."""

import dataclasses
import json
import logging
import sys
import textwrap
from datetime import date
from pathlib import Path
from collections.abc import Sequence
from typing import Any, TypedDict, cast

from claude_agent_sdk.types import HookContext, SyncHookJSONOutput

from claude_agent_sdk import (
    AssistantMessage,
    ContentBlock,
    HookInput,
    HookMatcher,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ThinkingBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)


from aib.agent.client import build_client
from aib.agent.display import (
    normalize_content as _normalize_content,
    print_block,
    stream_log as _stream_log,
)
from aib.agent.history import (
    save_forecast,
)
from aib.agent.sources import extract_sources
from aib.agent.hooks import HooksConfig, merge_hooks
from aib.agent.meta_hooks import create_structured_output_hooks
from aib.agent.retrodict import create_retrodict_hooks, get_modified_input
from aib.retrodict_context import effective_now, retrodict_cutoff
from aib.tools.fetch_http import downloads_dir
from aib.tools.reflection import ReviewState
from aib.agent.tool_policy import ToolPolicy
from aib.agent.models import (
    CreditExhaustedError,
    Forecast,
    ForecastMeta,
    ForecastOutput,
    ForecastSummary,
    MultipleChoiceForecast,
    NumericForecast,
    TokenUsage,
    create_forecast_model,
)
from aib.agent.numeric import (
    DistributionComponent,
    MixtureDistributionConfig,
    mixture_components_to_cdf,
    percentiles_to_cdf,
)
from aib.agent.prompts import get_forecasting_system_prompt, get_type_specific_guidance
from aib.config import settings
from aib.agent.session import ForecastSession, reset_session, set_session
from aib.paths import (
    RUNTIME_LOGS_PATH,
    TRACES_PATH,
    forecasts_dir,
    sessions_dir,
    trace_logs_dir,
)
from aib.tools.metrics import get_metrics_summary, log_metrics_summary
from aib.tools.sandbox import Sandbox

logger = logging.getLogger(__name__)

_PRESET_TEMPLATE = (Path(__file__).parent / "claude_code_preset.txt").read_text()


def _build_system_prompt(
    *,
    cutoff: date | None,
    tool_docs: str | None,
    sandbox_shared_dir: str,
    session_dir: str,
    question_type: str = "binary",
) -> str:
    """Build full system prompt from template + forecasting prompt.

    In retrodict mode, substitutes the cutoff date for {{DATE}} so the
    agent believes "today" is the blind date, preventing future leak.
    """
    effective_date = cutoff.isoformat() if cutoff else date.today().isoformat()
    base = _PRESET_TEMPLATE.replace("{{DATE}}", effective_date).replace(
        "{{WORKING_DIRECTORY}}", str(Path.cwd())
    )
    return (
        base
        + "\n\n"
        + get_forecasting_system_prompt(
            tool_docs=tool_docs,
            retrodict=cutoff is not None,
            sandbox_shared_dir=sandbox_shared_dir,
            session_dir=session_dir,
            question_type=question_type,
        )
    )


class ContextOverrides(TypedDict, total=False):
    description: str
    resolution_criteria: str
    fine_print: str


class ReasoningLogger:
    """Accumulates agent reasoning for feedback loop analysis.

    Writes to notes/traces/<version>/logs/ which is committed to git but NOT accessible
    to the agent during runtime.
    """

    def __init__(self, log_path: Path, question_title: str) -> None:
        self.log_path = log_path
        self.lines: list[str] = []
        self._pending_inputs: dict[str, tuple[str, dict]] = {}
        self.lines.append(f"# Reasoning Log: {question_title}\n")
        self.lines.append(f"*Generated: {effective_now().isoformat()}*\n\n")

    def format_block(self, block: ContentBlock) -> str:
        """Format a content block as markdown."""
        match block:
            case ThinkingBlock():
                return f"## 💭 Thinking\n\n{block.thinking}\n"
            case TextBlock():
                return f"## 💬 Response\n\n{block.text}\n"
            case ToolUseBlock():
                self._pending_inputs[block.id] = (block.name, block.input or {})
                return f"## 🔧 Tool: {block.name}\n\n"
            case ToolResultBlock():
                parts: list[str] = []
                tool_use_id = block.tool_use_id
                original = self._pending_inputs.pop(tool_use_id, None)
                actual_input = get_modified_input(tool_use_id)
                if actual_input is None and original is not None:
                    actual_input = original[1]
                if actual_input:
                    input_str = json.dumps(actual_input, indent=2)
                    parts.append(f"```json\n{input_str}\n```\n")
                content_str = _normalize_content(block.content)
                wrapped = "\n".join(
                    textwrap.fill(line, width=200) for line in content_str.splitlines()
                )
                parts.append(f"### 📋 Result\n\n```\n{wrapped}\n```\n")
                return "\n".join(parts)
            case _:
                return f"## ❓ {type(block).__name__}\n\n{block}\n"

    def log_block(self, block: ContentBlock) -> None:
        """Add a formatted block to the log."""
        self.lines.append(self.format_block(block))

    def save(self) -> None:
        """Write accumulated log to file."""
        self.log_path.write_text("\n".join(self.lines), encoding="utf-8")
        logger.info("Saved reasoning log to %s", self.log_path)


def append_metrics_to_reflection(
    meta_file: Path,
    *,
    metrics: dict[str, Any] | None,
    duration_seconds: float | None,
    cost_usd: float | None,
    token_usage: TokenUsage | None,
    log_path: Path | None,
    post_id: int,
    question_id: int,
    sources: list[str] | None = None,
) -> None:
    """Append programmatic metrics to a meta-reflection file.

    This injects actual tool metrics, timing, and cost data into the
    agent-written meta-reflection, creating a complete document with
    both qualitative assessment and quantitative data.
    """
    lines = [
        "",
        "---",
        "",
        "## Programmatic Metrics",
        "",
        "*Auto-generated - do not edit manually*",
        "",
    ]

    # Basic info
    lines.append(f"- **Post ID**: {post_id}")
    lines.append(f"- **Question ID**: {question_id}")

    # Timing and cost
    if duration_seconds is not None:
        minutes = duration_seconds / 60
        lines.append(
            f"- **Session Duration**: {duration_seconds:.1f}s ({minutes:.1f} min)"
        )
    if cost_usd is not None:
        lines.append(f"- **Cost**: ${cost_usd:.4f}")

    # Token usage
    if token_usage:
        input_tokens = token_usage.get("input_tokens", 0)
        output_tokens = token_usage.get("output_tokens", 0)
        cache_read = token_usage.get("cache_read_input_tokens", 0)
        cache_create = token_usage.get("cache_creation_input_tokens", 0)
        total = input_tokens + output_tokens
        lines.append(
            f"- **Tokens**: {total:,} total ({input_tokens:,} in, {output_tokens:,} out)"
        )
        if cache_read or cache_create:
            lines.append(f"  - Cache: {cache_read:,} read, {cache_create:,} created")

    # Log path
    if log_path and log_path.exists():
        lines.append(f"- **Log File**: `{log_path}`")

    # Tool metrics summary
    if metrics:
        total_calls = metrics.get("total_tool_calls", 0)
        total_errors = metrics.get("total_errors", 0)
        error_rate = metrics.get("overall_error_rate", "0%")

        lines.append("")
        lines.append("### Tool Calls")
        lines.append("")
        lines.append(f"- **Total**: {total_calls} calls")
        lines.append(f"- **Errors**: {total_errors} ({error_rate})")

        # Per-tool breakdown
        by_tool = metrics.get("by_tool", {})
        if by_tool:
            lines.append("")
            lines.append("| Tool | Calls | Errors | Avg Time |")
            lines.append("|------|-------|--------|----------|")
            for tool_name, tool_data in sorted(by_tool.items()):
                calls = tool_data.get("call_count", 0)
                errors = tool_data.get("error_count", 0)
                avg_ms = tool_data.get("avg_duration_ms", 0)
                error_indicator = " ⚠️" if errors > 0 else ""
                lines.append(
                    f"| {tool_name} | {calls} | {errors}{error_indicator} | {avg_ms:.0f}ms |"
                )

    # Sources consulted
    if sources:
        lines.append("")
        lines.append("### Sources Consulted")
        lines.append("")
        for source in sources[:20]:  # Limit to 20 to avoid bloat
            # Truncate long URLs/queries for readability
            display = source if len(source) <= 80 else source[:77] + "..."
            lines.append(f"- {display}")
        if len(sources) > 20:
            lines.append(f"- ... and {len(sources) - 20} more")

    # Append to file
    try:
        with open(meta_file, "a", encoding="utf-8") as f:
            f.write("\n".join(lines))
        logger.info("Appended metrics to meta-reflection %s", meta_file)
    except Exception as e:
        logger.warning("Failed to append metrics to %s: %s", meta_file, e)


@dataclasses.dataclass
class NotesConfig:
    """Notes folder configuration with explicit RW/RO separation."""

    session: Path
    forecasts: Path
    reasoning_log: Path  # For feedback loop (agent cannot access)
    rw: list[Path]
    ro: list[Path]

    @property
    def all_dirs(self) -> list[Path]:
        return self.rw + self.ro


def setup_notes_folder(
    post_id: int, timestamp: str, *, retrodict: bool = False
) -> NotesConfig:
    """Create session-specific notes folder structure.

    Structure (RW = this session can write, RO = read historical only):
    - notes/traces/<ver>/sessions/<post_id>/<ts>/   (RW) - session work + meta
    - notes/traces/<ver>/forecasts/<post_id>/<ts>/  (RW, blocked in retrodict)
    - notes/traces/                                  (RO, blocked in retrodict)

    In retrodict mode, read access to traces/ is blocked to prevent
    "future leak" from past forecasts.

    Args:
        post_id: Metaculus post ID (the URL identifier, e.g., 41976). Use 0 for sub-forecasts.
        timestamp: Timestamp string (format: YYYYMMDD_HHMMSS).
        retrodict: If True, block read access to historical data directories.

    Returns:
        NotesConfig with RW and RO directories separated.
    """

    session_path = sessions_dir() / str(post_id) / timestamp
    cur_forecasts_dir = forecasts_dir()
    forecasts_path = cur_forecasts_dir / str(post_id) / timestamp
    logs_path = trace_logs_dir()

    session_path.mkdir(parents=True, exist_ok=True)
    logs_path.mkdir(parents=True, exist_ok=True)

    reasoning_log = logs_path / f"{post_id}_{timestamp}.md"

    if retrodict:
        return NotesConfig(
            session=session_path,
            forecasts=session_path,
            reasoning_log=reasoning_log,
            rw=[session_path],
            ro=[],
        )

    forecasts_path.mkdir(parents=True, exist_ok=True)

    return NotesConfig(
        session=session_path,
        forecasts=forecasts_path,
        reasoning_log=reasoning_log,
        rw=[session_path, forecasts_path],
        ro=[TRACES_PATH],
    )


def _path_is_under(file_path: str, allowed_dirs: list[Path]) -> bool:
    """Check if a file path is under one of the allowed directories."""
    try:
        path = Path(file_path).resolve()
    except (OSError, ValueError):
        return False

    for allowed in allowed_dirs:
        try:
            path.relative_to(allowed.resolve())
            return True
        except ValueError:
            continue
    return False


def create_permission_hooks(
    rw_dirs: list[Path],
    ro_dirs: list[Path],
) -> HooksConfig:
    """Create permission hooks with directory-based access control.

    Args:
        rw_dirs: Directories where Write/Edit/Read are allowed
        ro_dirs: Additional directories where only Read is allowed

    Returns:
        Hooks configuration dict for ClaudeAgentOptions.
    """
    all_readable = rw_dirs + ro_dirs

    async def permission_hook(
        input_data: Any,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> dict[str, Any]:
        """Control tool access based on directory permissions."""
        if input_data.get("hook_event_name") != "PreToolUse":
            return {}

        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})
        hook_event = input_data["hook_event_name"]

        def deny(reason: str) -> dict[str, Any]:
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }

        def allow() -> dict[str, Any]:
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                }
            }

        # Write: allow in RW directories only
        if tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            if not file_path:
                return {}  # Let SDK handle missing required param
            if _path_is_under(file_path, rw_dirs):
                return allow()
            return deny(f"Write denied. Allowed: {[str(d) for d in rw_dirs]}")

        # Bash: SDK sandbox config handles this via autoAllowBashIfSandboxed
        # No explicit denial needed here

        # File edit operations: only allowed in RW directories
        if tool_name == "Edit":
            file_path = tool_input.get("file_path", "")
            if not file_path:
                return {}  # Let SDK handle missing required param

            if _path_is_under(file_path, rw_dirs):
                return allow()
            return deny(f"Write denied. Allowed: {[str(d) for d in rw_dirs]}")

        # Read: requires file_path, must be in readable directories
        if tool_name == "Read":
            file_path = tool_input.get("file_path", "")
            if not file_path:
                return {}  # Let SDK handle missing required param

            if _path_is_under(file_path, all_readable):
                return allow()
            return deny(f"Read denied. Allowed: {[str(d) for d in all_readable]}")

        # Glob/Grep: require explicit path in readable directories (no cwd default)
        if tool_name in ("Glob", "Grep"):
            file_path = tool_input.get("path", "")
            if not file_path:
                return deny(
                    f"Path required for {tool_name}. "
                    f"Specify path in: {[str(d) for d in all_readable]}"
                )

            if _path_is_under(file_path, all_readable):
                return allow()
            return deny(
                f"{tool_name} denied. Allowed: {[str(d) for d in all_readable]}"
            )

        # Auto-allow everything else (WebSearch, WebFetch, MCP tools, Task)
        # These are already filtered by allowed_tools in options
        return allow()

    return {
        "PreToolUse": [HookMatcher(hooks=[permission_hook])],  # type: ignore[list-item]
    }


def create_websearch_nudge_hooks() -> HooksConfig:
    """PostToolUse hook that nudges the agent to prefer web_search over WebSearch."""

    async def nudge_hook(
        input_data: HookInput,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> SyncHookJSONOutput:
        if input_data.get("hook_event_name") != "PostToolUse":
            return SyncHookJSONOutput()
        if input_data.get("tool_name") != "WebSearch":
            return SyncHookJSONOutput()

        return SyncHookJSONOutput(
            systemMessage=(
                "Tip: Prefer mcp__search__web_search over WebSearch. "
                "It provides structured results with automatic API data "
                "for recognized domains (stock prices, arXiv, Wikipedia, "
                "FRED, prediction markets)."
            )
        )

    return {
        "PostToolUse": [HookMatcher(hooks=[nudge_hook])],
    }


def create_webfetch_nudge_hooks() -> HooksConfig:
    """PostToolUse hook that nudges the agent to prefer fetch_url over WebFetch."""

    async def nudge_hook(
        input_data: HookInput,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> SyncHookJSONOutput:
        if input_data.get("hook_event_name") != "PostToolUse":
            return SyncHookJSONOutput()
        if input_data.get("tool_name") != "WebFetch":
            return SyncHookJSONOutput()

        return SyncHookJSONOutput(
            systemMessage=(
                "Tip: Prefer mcp__search__fetch_url over WebFetch. "
                "It provides automatic text extraction, JavaScript rendering "
                "via Playwright, and domain-specific API routing."
            )
        )

    return {
        "PostToolUse": [HookMatcher(hooks=[nudge_hook])],
    }


def create_suggest_only_nudge_hooks() -> HooksConfig:
    """PostToolUse hook that nudges the agent toward structured APIs for known domains."""
    from aib.tools.fetch_routes import SUGGEST_ONLY

    async def nudge_hook(
        input_data: HookInput,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> SyncHookJSONOutput:
        if input_data.get("hook_event_name") != "PostToolUse":
            return SyncHookJSONOutput()
        if input_data.get("tool_name") != "mcp__search__fetch_url":
            return SyncHookJSONOutput()

        tool_input = input_data.get("tool_input", {})
        url = (tool_input.get("url") or "").lower()
        for domain_key, hint in SUGGEST_ONLY.items():
            if domain_key in url:
                return SyncHookJSONOutput(systemMessage=f"Tip: {hint}")
        return SyncHookJSONOutput()

    return {
        "PostToolUse": [HookMatcher(hooks=[nudge_hook])],
    }


async def fetch_question(question_id: int) -> dict:
    """Fetch question details from Metaculus API."""
    from aib.clients.metaculus import get_client

    client = get_client()
    return await client.fetch_post_json(question_id)


def build_question_context(post_data: dict) -> dict:
    """Extract relevant question data for the agent prompt."""
    question = post_data.get("question", {})
    question_type = question.get("type", "binary")

    context = {
        "title": question.get("title", "Unknown"),
        "type": question_type,
        "description": post_data.get("description")
        or question.get("description")
        or "MISSING — fetch the Metaculus question page for background info.",
        "resolution_criteria": question.get("resolution_criteria")
        or "MISSING — fetch the Metaculus question page to recover. Titles can be misleading; resolution criteria define what actually counts.",
        "fine_print": question.get("fine_print")
        or "MISSING — fetch the Metaculus question page to recover.",
        "scheduled_close_time": question.get("scheduled_close_time"),
        # Cadence tracking fields
        "published_at": post_data.get("published_at"),
        "scheduled_resolve_time": question.get("scheduled_resolve_time"),
    }

    if question_type == "multiple_choice":
        context["options"] = question.get("options", [])

    if question_type in ("numeric", "discrete"):
        scaling = question.get("scaling", {})
        context["numeric_bounds"] = {
            "range_min": scaling.get("range_min"),
            "range_max": scaling.get("range_max"),
            "open_lower_bound": question.get("open_lower_bound", False),
            "open_upper_bound": question.get("open_upper_bound", False),
            "zero_point": scaling.get("zero_point"),  # For log-scaled questions
            # Nominal bounds: more intuitive display values for discrete questions
            # (e.g., "0 to 10" instead of internal scaling values)
            "nominal_lower_bound": scaling.get("nominal_lower_bound"),
            "nominal_upper_bound": scaling.get("nominal_upper_bound"),
            # Unit of measure for clearer prompts
            "unit": question.get("unit") or "",
        }
        # For discrete questions, CDF size is inbound_outcome_count + 1
        if question_type == "discrete":
            inbound_outcome_count = scaling.get("inbound_outcome_count")
            if inbound_outcome_count is not None:
                context["numeric_bounds"]["cdf_size"] = inbound_outcome_count + 1

    return context


def build_trace(
    messages: Sequence[AssistantMessage | UserMessage],
    title: str = "",
    exclude_tools: frozenset[str] = frozenset(),
) -> str:
    """Build a markdown trace from conversation messages.

    Args:
        messages: Conversation messages (assistant and user) to format.
            ToolUseBlock arrives in AssistantMessage, ToolResultBlock
            arrives in UserMessage — both are needed for a complete trace.
        title: Question title for the log header.
        exclude_tools: Tool names whose ToolUseBlock/ToolResultBlock pairs
            should be omitted from the trace. Uses the same id-tracking
            pattern as extract_sources: when a ToolUseBlock.name matches,
            its id is recorded and the corresponding ToolResultBlock is
            also skipped.
    """
    excluded_ids: set[str] = set()
    rl = ReasoningLogger(Path("/dev/null"), title)
    for msg in messages:
        content = msg.content
        if isinstance(content, str):
            continue
        for block in content:
            if isinstance(block, ToolUseBlock) and block.name in exclude_tools:
                excluded_ids.add(block.id)
                continue
            if isinstance(block, ToolResultBlock) and block.tool_use_id in excluded_ids:
                continue
            rl.log_block(block)
    return "\n".join(rl.lines)


REVIEWER_SYSTEM_PROMPT = textwrap.dedent("""\
    You are reviewing a forecasting agent's trace. Produce a structured review
    covering tool usage, workflow quality, reasoning quality, and a condensed
    narrative suitable for posting as a Metaculus comment.

    ## condensed_reasoning

    Write a clear, well-structured narrative covering everything: what research
    was done, key evidence found, and how the conclusion was reached.
    Use markdown: **bold** for key figures, bullet lists for evidence,
    `inline code` for tickers/identifiers. Use ## subtitles (## Research,
    ## Key Evidence, ## Conclusion) but no top-level # title.
    First-person voice: 'I researched...', 'I found...', 'I concluded...'.

    ## tool_audit

    For each tool the agent used, write a compact one-line assessment in
    by_tool. Format: "N calls, M errors (cause), impact: none/minor/significant,
    value: high/medium/low/wasted, [notes]". Keep each entry to one line —
    these get aggregated across many forecasts.

    Also note capability_gaps (tools the agent needed but didn't have)
    and subtle_bugs (tools that didn't error but produced misleading results).

    ## workflow

    Assess information gathering strategy, structured reasoning quality,
    self-correction ability, and efficiency.

    ## reasoning

    Rate evidence quality, logical coherence, and calibration sense (1-5 each).
    List strengths and weaknesses.

    ## pipeline

    Note any MCP errors, sandbox issues, token waste, or prompt problems.

    ## future_leak (retrodict only)

    If the trace is from a retrodict session, check whether the agent accessed
    information from after the retrodict cutoff date. Verdict: CLEAN, SUSPECT,
    or LEAKED with specific evidence.
""")


async def review_forecast_trace(
    trace: str,
    question_title: str,
    session_dir: Path,
    structured_output: dict[str, Any] | None = None,
    is_retrodict: bool = False,
) -> ForecastSummary | None:
    """Review a forecast trace with Opus, producing a ForecastSummary.

    Writes the trace to a file and gives Opus the Read tool so it can
    access the full trace without truncation. Saves summary.json to
    the session directory.
    """
    trace_file = session_dir / "trace_for_condensation.md"
    session_dir.mkdir(parents=True, exist_ok=True)
    trace_file.write_text(trace, encoding="utf-8")

    forecast_block = ""
    if structured_output:
        forecast_block = (
            "\n\nThe agent's final submitted forecast:\n"
            f"```json\n{json.dumps(structured_output, indent=2)}\n```\n"
            "Your condensed_reasoning narrative MUST match this forecast. "
            "Do not infer a different conclusion — report what the agent "
            "actually concluded."
        )

    retrodict_instruction = ""
    if is_retrodict:
        retrodict_instruction = (
            "\n\nThis is a RETRODICT trace. You MUST populate the future_leak "
            "field. Check whether the agent accessed any information from "
            "after the retrodict cutoff date."
        )

    prompt = (
        f"Question: {question_title}\n\n"
        f"Read the full forecast trace from: {trace_file}\n"
        f"Then produce the structured review.{forecast_block}"
        f"{retrodict_instruction}"
    )

    try:
        result_output: dict[str, Any] | None = None
        async with build_client(
            model="opus",
            system_prompt=REVIEWER_SYSTEM_PROMPT,
            allowed_tools=["Read"],
            permission_mode="bypassPermissions",
            output_format={
                "type": "json_schema",
                "schema": ForecastSummary.model_json_schema(),
            },
        ) as client:
            await client.query(prompt)
            async for message in client.receive_response():
                if isinstance(message, ResultMessage):
                    result_output = message.structured_output
        if result_output:
            summary = ForecastSummary.model_validate(result_output)
            summary_file = session_dir / "summary.json"
            summary_file.write_text(summary.model_dump_json(indent=2), encoding="utf-8")
            logger.info("Saved forecast summary to %s", summary_file)
            return summary
        return None
    except Exception:
        logger.exception("Forecast review failed")
        return None


async def run_forecast(
    question_id: int | None = None,
    *,
    question_context: dict | None = None,
    allow_spawn: bool = True,
    context_overrides: ContextOverrides | None = None,
) -> ForecastOutput:
    """Run the forecasting agent on a question.

    Args:
        question_id: Metaculus post ID (for top-level forecasts)
        question_context: Pre-built context dict (for sub-forecasts from spawn_subquestions)
        allow_spawn: Whether this forecast can spawn subquestions (False for sub-forecasts)

    Returns:
        ForecastOutput with the forecast results.

    Note:
        Retrodict mode is controlled via the retrodict_cutoff ContextVar.
        When set, all tools restrict data to before the cutoff date.
    """
    # Generate session ID for notes and logging
    # Format: <post_id>_<timestamp> for traceability
    timestamp = effective_now().strftime("%Y%m%d_%H%M%S")
    if question_id is not None:
        session_id = f"{question_id}_{timestamp}"
    else:
        # Sub-forecasts use timestamp-based ID since they don't have a real question_id
        session_id = f"sub_{timestamp}"

    # Create session-scoped state (metrics, run_forecast_fn, modified_inputs)
    session = ForecastSession(run_forecast_fn=run_forecast)
    set_session(session)

    # Either fetch question or use provided context
    # Note: question_id arg is actually the post_id from the URL
    post_id: int = question_id or 0
    actual_question_id: int = 0

    if question_context is not None:
        context = question_context
        question_title = context.get("title", "Sub-question")
        question_type = context.get("type", "binary")
        # Sub-forecasts don't have real IDs
        actual_question_id = context.get("question_id", 0)
        logger.info(
            "Starting sub-forecast session %s for: %s", session_id, question_title
        )
    elif question_id is not None:
        logger.info("Starting forecast session %s for post %d", session_id, question_id)
        post_data = await fetch_question(question_id)
        question = post_data.get("question", {})
        question_title = question.get("title", "Unknown")
        question_type = question.get("type", "binary")
        # Extract the actual question ID (different from post ID)
        actual_question_id = question.get("id", 0)
        if actual_question_id == 0:
            raise ValueError(
                f"Could not extract question ID from post {question_id}. "
                "The API response may be malformed."
            )
        logger.info("Post %d maps to question ID %d", question_id, actual_question_id)
        context = build_question_context(post_data)
    else:
        raise ValueError("Either question_id or question_context must be provided")

    if context_overrides:
        context.update(context_overrides)

    # Setup notes folder (using post_id for directory structure)
    # In retrodict mode, block read access to historical data
    cutoff = retrodict_cutoff.get()
    notes = setup_notes_folder(post_id, timestamp, retrodict=cutoff is not None)
    logger.info("Notes folder: %s", notes.session)

    # Get type-specific output schema and guidance
    mc_options = context.get("options") if question_type == "multiple_choice" else None
    model_class = create_forecast_model(question_type, mc_options)
    output_schema = model_class.model_json_schema()
    type_guidance = get_type_specific_guidance(question_type, context)

    prompt = f"Analyze this forecasting question and provide your forecast:\n\n{json.dumps(context, indent=2)}\n\n{type_guidance}"

    print(f"\n{'─' * 60}")
    print(prompt)
    print(f"{'─' * 60}\n")

    collected_text: list[str] = []
    assistant_messages: list[AssistantMessage] = []
    all_messages: list[AssistantMessage | UserMessage] = []
    result: ResultMessage | None = None

    # Setup unified log file: captures ALL log output (stream, tools, HTTP, etc.)
    log_path = (
        RUNTIME_LOGS_PATH / session_id / effective_now().strftime("%Y%m%d-%H%M%S.log")
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    _log_handler = logging.FileHandler(log_path)
    _log_handler.setLevel(logging.DEBUG)
    _log_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    )
    logging.getLogger().addHandler(_log_handler)

    # Session-specific scratch directory for sandbox file exchange
    sandbox_shared_dir = RUNTIME_LOGS_PATH / session_id / "sandbox-shared"
    sandbox_shared_dir.mkdir(parents=True, exist_ok=True)

    # Per-session downloads directory (PDFs, arXiv papers, etc.)
    session_downloads = RUNTIME_LOGS_PATH / session_id / "downloads"
    session_downloads.mkdir(parents=True, exist_ok=True)
    downloads_token = downloads_dir.set(session_downloads)

    # Determine sandbox network mode for retrodict
    sandbox_network_mode = "pypi_only" if cutoff else "bridge"
    if cutoff:
        logger.info(
            "Retrodict mode: restricting data to before %s",
            cutoff.isoformat(),
        )

    with Sandbox(
        session_id=session_id,
        shared_dir=sandbox_shared_dir,
        network_mode=sandbox_network_mode,
        fake_date=cutoff,
    ) as sandbox:
        # Sandbox shared dir for scratch work + session-specific notes directories
        rw_dirs = [sandbox_shared_dir, session_downloads] + notes.rw
        ro_dirs = notes.ro

        # Create base permission hooks
        permission_hooks = create_permission_hooks(rw_dirs=rw_dirs, ro_dirs=ro_dirs)

        # Nudge agent toward fetch_url when it uses WebFetch
        hooks = merge_hooks(permission_hooks, create_webfetch_nudge_hooks())

        # Nudge agent toward structured APIs for SUGGEST_ONLY domains
        hooks = merge_hooks(hooks, create_suggest_only_nudge_hooks())

        # Nudge agent toward web_search when it uses WebSearch (live mode only;
        # in retrodict mode, WebSearch is denied entirely by retrodict hooks)
        if not cutoff:
            hooks = merge_hooks(hooks, create_websearch_nudge_hooks())

        # Compose with retrodict hooks if in retrodict mode
        if cutoff:
            retrodict_hooks = create_retrodict_hooks()
            hooks = merge_hooks(hooks, retrodict_hooks)

        # Shared reviewer state: reflection tool records verdicts,
        # StructuredOutput hook checks them.
        review_state = ReviewState() if post_id > 0 else None

        # StructuredOutput hook: unwrap {"parameter": {...}} + reviewer gate.
        # Must be LAST PreToolUse hook (CLI bug #15897: updatedInput is
        # discarded when later hooks overwrite the result).
        hooks = merge_hooks(hooks, create_structured_output_hooks(review_state))

        # Centralized tool policy determines MCP servers and allowed tools
        policy = ToolPolicy.from_settings(settings)

        # Create MCP servers first so we can extract tool descriptions
        mcp_servers = policy.get_mcp_servers(
            sandbox,
            session_dir=notes.session,
            question_type=question_type,
            get_sources=lambda: extract_sources(all_messages),
            get_trace=lambda: build_trace(
                all_messages,
                question_title,
                exclude_tools=frozenset({"mcp__notes__reflection"}),
            ),
            question_context=context,
            traces_dir=forecasts_dir().parent if cutoff is None else None,
            review_state=review_state,
        )

        try:
            async with build_client(
                model=settings.model,
                system_prompt=_build_system_prompt(
                    cutoff=cutoff,
                    tool_docs=policy.get_tool_docs(
                        mcp_servers, allow_spawn=allow_spawn
                    ),
                    sandbox_shared_dir=str(sandbox_shared_dir),
                    session_dir=str(notes.session),
                    question_type=question_type,
                ),
                max_thinking_tokens=128_000 - 1,
                permission_mode="bypassPermissions",
                hooks=hooks,
                sandbox={
                    "enabled": True,
                    "autoAllowBashIfSandboxed": True,
                    "allowUnsandboxedCommands": False,
                },
                mcp_servers=mcp_servers,
                add_dirs=[
                    *notes.all_dirs,
                    sandbox_shared_dir,
                    session_downloads,
                    Path.home() / ".claude" / "projects",
                ],
                allowed_tools=policy.get_allowed_tools(allow_spawn=allow_spawn),
                output_format={
                    "type": "json_schema",
                    "schema": output_schema,
                },
            ) as client:
                await client.query(prompt)

                async for message in client.receive_response():
                    match message:
                        case AssistantMessage():
                            assistant_messages.append(message)
                            all_messages.append(message)
                            for block in message.content:
                                print_block(block)
                                match block:
                                    case TextBlock():
                                        collected_text.append(block.text)
                                        # Check for credit exhaustion
                                        credit_error = (
                                            CreditExhaustedError.from_message(
                                                block.text
                                            )
                                        )
                                        if credit_error:
                                            raise credit_error
                                    case ThinkingBlock():
                                        pass
                                    case ToolUseBlock():
                                        pass
                                    case ToolResultBlock():
                                        pass
                                    case _:
                                        logger.debug(
                                            "Unhandled content block: %s",
                                            type(block).__name__,
                                        )
                        case ResultMessage():
                            result = message
                            if message.is_error:
                                raise RuntimeError(f"Agent error: {message.result}")
                        case SystemMessage():
                            _stream_log.info(
                                "SYSTEM [%s]: %s",
                                message.subtype,
                                json.dumps(message.data, indent=2),
                            )
                        case UserMessage():
                            all_messages.append(message)
                            _stream_log.info(
                                "USER_MESSAGE: %s",
                                _normalize_content(message.content),
                            )
                            if isinstance(message.content, list):
                                for block in message.content:
                                    print_block(block)
                        case _:
                            print(f"📨 {type(message).__name__}: {message}")
                            logger.debug(
                                "Unhandled message type: %s", type(message).__name__
                            )
        except Exception as exc:
            if post_id > 0 and (collected_text or all_messages):
                try:
                    save_forecast(
                        question_id=actual_question_id,
                        post_id=post_id,
                        question_title=question_title,
                        question_type=question_type,
                        summary=f"PARTIAL: {type(exc).__name__}: {exc}",
                        factors=[],
                        reasoning="\n".join(collected_text),
                        sources_consulted=extract_sources(all_messages),
                        partial=True,
                        retrodict_date=cutoff.isoformat() if cutoff else None,
                    )
                except Exception:
                    logger.warning("Failed to save partial forecast")
            logging.getLogger().removeHandler(_log_handler)
            _log_handler.close()
            raise
        finally:
            downloads_dir.reset(downloads_token)
            reset_session()

    if result is None:
        raise RuntimeError("No result received from agent")

    # Post-session Opus review (replaces Sonnet condensation)
    forecast_summary = await review_forecast_trace(
        build_trace(all_messages, question_title),
        question_title,
        notes.session,
        structured_output=result.structured_output,
        is_retrodict=cutoff is not None,
    )

    # Extract structured forecast based on question type
    output = ForecastOutput(
        question_id=actual_question_id,
        post_id=post_id,
        question_title=question_title,
        question_type=question_type,
        question_category=ForecastOutput.classify_category(
            question_title, question_type
        ),
        summary="No forecast produced",
        factors=[],
        reasoning=next(
            (
                block.text
                for msg in reversed(assistant_messages)
                for block in reversed(msg.content)
                if isinstance(block, TextBlock)
            ),
            "",
        ),
        condensed_reasoning=(
            forecast_summary.condensed_reasoning if forecast_summary else None
        ),
        sources_consulted=extract_sources(all_messages),
        duration_seconds=(result.duration_ms / 1000) if result.duration_ms else None,
        cost_usd=result.total_cost_usd,
        token_usage=cast(TokenUsage, result.usage) if result.usage else None,
        retrodict_date=cutoff,
    )

    if result.structured_output:
        forecast = model_class.model_validate(result.structured_output)

        if isinstance(forecast, Forecast):
            output.summary = forecast.summary
            output.factors = forecast.factors
            output.logit = forecast.logit
            output.probability = forecast.probability
            output.probability_from_logit = forecast.probability_from_logit

            # Check for consistency issues
            consistency_warnings = forecast.check_consistency()
            for warning in consistency_warnings:
                logger.warning("Consistency check: %s", warning)
        elif isinstance(forecast, NumericForecast):
            output.summary = forecast.summary
            output.factors = forecast.factors
            output.median = forecast.median
            output.confidence_interval = forecast.confidence_interval
            output.percentiles = forecast.get_percentile_dict()

            # Generate CDF from percentiles or mixture components
            bounds = context.get("numeric_bounds", {})
            if (
                bounds.get("range_min") is not None
                and bounds.get("range_max") is not None
            ):
                try:
                    if forecast.uses_mixture_mode and forecast.components:
                        # Mixture distribution mode
                        mixture_config = MixtureDistributionConfig(
                            components=[
                                DistributionComponent(
                                    scenario=c.scenario,
                                    mode=c.mode,
                                    lower_bound=c.lower_bound,
                                    upper_bound=c.upper_bound,
                                    weight=c.weight,
                                )
                                for c in forecast.components
                            ],
                            question_lower_bound=bounds["range_min"],
                            question_upper_bound=bounds["range_max"],
                            open_lower_bound=bounds.get("open_lower_bound", False),
                            open_upper_bound=bounds.get("open_upper_bound", False),
                            zero_point=bounds.get("zero_point"),
                        )
                        expected_cdf_size = bounds.get("cdf_size", 201)
                        output.cdf = mixture_components_to_cdf(
                            mixture_config,
                            cdf_size=expected_cdf_size,
                        )
                        output.cdf_size = expected_cdf_size
                        logger.info(
                            "Generated %d-point CDF from %d mixture components",
                            len(output.cdf),
                            len(forecast.components),
                        )
                    elif output.percentiles:
                        # Traditional percentile mode
                        expected_cdf_size = bounds.get("cdf_size", 201)
                        output.cdf = percentiles_to_cdf(
                            output.percentiles,
                            upper_bound=bounds["range_max"],
                            lower_bound=bounds["range_min"],
                            open_upper_bound=bounds.get("open_upper_bound", False),
                            open_lower_bound=bounds.get("open_lower_bound", False),
                            zero_point=bounds.get("zero_point"),
                            cdf_size=expected_cdf_size,
                        )
                        output.cdf_size = expected_cdf_size
                        logger.info(
                            "Generated %d-point CDF from percentiles", len(output.cdf)
                        )
                    else:
                        logger.warning(
                            "No percentiles or components for CDF generation"
                        )
                        output.cdf = None
                except Exception as e:
                    logger.exception("Failed to generate CDF: %s", e)
                    print(f"CDF generation failed: {e}", file=sys.stderr)
                    output.cdf = None
        elif isinstance(forecast, MultipleChoiceForecast):
            output.summary = forecast.summary
            output.factors = forecast.factors
            output.probabilities = forecast.probabilities
    else:
        logger.warning("No structured output; using default forecast")
        if question_type == "binary":
            output.logit = 0.0
            output.probability = 0.5
        elif question_type in ("numeric", "discrete"):
            output.median = 0.0
            output.confidence_interval = (0.0, 0.0)
        elif question_type == "multiple_choice":
            output.probabilities = {}

    # Log tool metrics summary
    log_metrics_summary()
    metrics = get_metrics_summary()
    output.tool_metrics = metrics

    # Check for reflection (required for top-level forecasts)
    if post_id > 0:
        reflection_file = notes.session / "reflection.yaml"

        # Extract subagents from tool metrics
        subagents_used = []
        if metrics and "by_tool" in metrics:
            for tool_name in metrics["by_tool"]:
                if tool_name == "spawn_subquestions":
                    subagents_used.append("(via spawn_subquestions)")

        if reflection_file.exists():
            output.meta = ForecastMeta(
                meta_file_path=str(reflection_file),
                tools_used_count=metrics.get("total_calls", 0) if metrics else 0,
                subagents_used=subagents_used,
            )
            logger.info("Found reflection at %s", reflection_file)

            append_metrics_to_reflection(
                reflection_file,
                metrics=metrics,
                duration_seconds=output.duration_seconds,
                cost_usd=output.cost_usd,
                token_usage=output.token_usage,
                log_path=log_path if log_path.exists() else None,
                post_id=post_id,
                question_id=actual_question_id,
                sources=output.sources_consulted,
            )
        else:
            logger.error(
                "MISSING REFLECTION for post %d. "
                "Agent failed to call notes(reflection) before final output. "
                "Expected at: %s",
                post_id,
                reflection_file,
            )
            output.meta = ForecastMeta(
                meta_file_path=None,
                tools_used_count=metrics.get("total_calls", 0) if metrics else 0,
                subagents_used=subagents_used,
            )

    # Auto-save forecast to history (for top-level forecasts only)
    if post_id > 0 and actual_question_id > 0:
        try:
            save_kwargs = {
                "question_id": actual_question_id,
                "post_id": post_id,
                "question_title": question_title,
                "question_type": question_type,
                "summary": output.summary,
                "factors": [f.model_dump() for f in output.factors],
                "probability": output.probability,
                "logit": output.logit,
                "probabilities": output.probabilities,
                "median": output.median,
                "confidence_interval": output.confidence_interval,
                "percentiles": output.percentiles,
                "cdf": output.cdf,
                "numeric_bounds": context.get("numeric_bounds"),
                "tool_metrics": metrics,
                "token_usage": output.token_usage,
                "log_path": str(log_path) if log_path.exists() else None,
                "question_published_at": context.get("published_at"),
                "question_close_time": context.get("scheduled_close_time"),
                "question_scheduled_resolve_time": context.get(
                    "scheduled_resolve_time"
                ),
                "reasoning": output.reasoning,
                "sources_consulted": output.sources_consulted,
                "resolution_criteria": context.get("resolution_criteria"),
                "fine_print": context.get("fine_print"),
            }

            save_forecast(
                **save_kwargs,
                retrodict_date=cutoff.isoformat() if cutoff else None,
            )
        except Exception as e:
            logger.warning("Failed to auto-save forecast: %s", e)

    # Record revision history from reviewer interactions
    if review_state and review_state.history:
        output.revision_history = review_state.history

    logging.getLogger().removeHandler(_log_handler)
    _log_handler.close()

    return output
