"""Forecasting agent using Claude Agent SDK."""

import dataclasses
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, cast

from claude_agent_sdk.types import HookContext

import httpx
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ContentBlock,
    HookMatcher,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ThinkingBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

from aib.agent.history import (
    format_history_for_context,
    load_past_forecasts,
    save_forecast,
)
from aib.agent.models import (
    CreditExhaustedError,
    Forecast,
    ForecastMeta,
    ForecastOutput,
    MultipleChoiceForecast,
    NumericForecast,
    TokenUsage,
)
from aib.agent.numeric import (
    DistributionComponent,
    MixtureDistributionConfig,
    mixture_components_to_cdf,
    percentiles_to_cdf,
)
from aib.agent.prompts import get_forecasting_system_prompt, get_type_specific_guidance
from aib.agent.subagents import SUBAGENTS
from aib.config import settings
from aib.tools.composition import composition_server, set_run_forecast_fn
from aib.tools.financial import financial_server
from aib.tools.forecasting import forecasting_server
from aib.tools.markets import markets_server
from aib.tools.notes import notes_server
from aib.tools.trends import trends_server
from aib.tools.metrics import get_metrics_summary, log_metrics_summary, reset_metrics
from aib.tools.sandbox import Sandbox

logger = logging.getLogger(__name__)

METACULUS_API_BASE = "https://www.metaculus.com/api"


def _optional_tools(condition: bool | str | None, tools: list[str]) -> list[str]:
    """Return tools list if condition is truthy, else empty list.

    Used to conditionally include MCP tools based on API key availability.
    """
    return tools if condition else []


def print_block(block: ContentBlock) -> None:
    """Print a content block with appropriate emoji prefix."""
    match block:
        case ThinkingBlock():
            print(f"💭 {block.thinking}")
        case TextBlock():
            print(f"💬 {block.text}")
        case ToolUseBlock():
            input_str = json.dumps(block.input, indent=2) if block.input else ""
            print(f"🔧 {block.name} [{block.id}]")
            if input_str:
                print(input_str)
        case ToolResultBlock():
            # Note: block.is_error is unreliable (SDK bug doesn't propagate MCP isError)
            content_preview = _truncate_content(block.content, max_len=500)
            print(f"📋 Result [{block.tool_use_id}]: {content_preview}")
        case _:
            print(f"❓ {type(block).__name__}: {block}")


def _truncate_content(content: str | list | None, max_len: int = 500) -> str:
    """Truncate content for display, handling various content types."""
    if content is None:
        return "(empty)"
    if isinstance(content, list):
        # MCP-style content blocks
        texts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item.get("text", ""))
        content = "\n".join(texts)
    if len(content) > max_len:
        return content[:max_len] + "..."
    return content


class ReasoningLogger:
    """Accumulates agent reasoning for feedback loop analysis.

    Writes to notes/logs/ which is committed to git but NOT accessible
    to the agent during runtime.
    """

    def __init__(self, log_path: Path, question_title: str) -> None:
        self.log_path = log_path
        self.lines: list[str] = []
        self.lines.append(f"# Reasoning Log: {question_title}\n")
        self.lines.append(f"*Generated: {datetime.now().isoformat()}*\n\n")

    def format_block(self, block: ContentBlock) -> str:
        """Format a content block as markdown."""
        match block:
            case ThinkingBlock():
                return f"## 💭 Thinking\n\n{block.thinking}\n"
            case TextBlock():
                return f"## 💬 Response\n\n{block.text}\n"
            case ToolUseBlock():
                input_str = json.dumps(block.input, indent=2) if block.input else ""
                result = f"## 🔧 Tool: {block.name}\n\n"
                if input_str:
                    result += f"```json\n{input_str}\n```\n"
                return result
            case ToolResultBlock():
                content_str = _truncate_content(block.content, max_len=2000)
                return f"### 📋 Result\n\n```\n{content_str}\n```\n"
            case _:
                return f"## ❓ {type(block).__name__}\n\n{block}\n"

    def log_block(self, block: ContentBlock) -> None:
        """Add a formatted block to the log."""
        self.lines.append(self.format_block(block))

    def save(self) -> None:
        """Write accumulated log to file."""
        self.log_path.write_text("\n".join(self.lines), encoding="utf-8")
        logger.info("Saved reasoning log to %s", self.log_path)


def append_metrics_to_meta_reflection(
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


def get_output_schema_for_question(
    question_type: str,
) -> tuple[type[Forecast | NumericForecast | MultipleChoiceForecast], dict]:
    """Return (model_class, json_schema) for question type.

    Args:
        question_type: Type of question (binary, numeric, discrete, multiple_choice)

    Returns:
        Tuple of (model class, JSON schema dict) for the appropriate forecast type.
    """
    if question_type == "multiple_choice":
        return MultipleChoiceForecast, MultipleChoiceForecast.model_json_schema()
    elif question_type in ("numeric", "discrete"):
        return NumericForecast, NumericForecast.model_json_schema()
    else:  # binary is default
        return Forecast, Forecast.model_json_schema()


# Notes folder base path
NOTES_BASE_PATH = Path("./notes")

# Logs folder base path
LOGS_BASE_PATH = Path("./logs")


@dataclasses.dataclass
class NotesConfig:
    """Notes folder configuration with explicit RW/RO separation."""

    session: Path
    research: Path
    forecasts: Path
    reasoning_log: Path  # For feedback loop (agent cannot access)
    rw: list[Path]
    ro: list[Path]

    @property
    def all_dirs(self) -> list[Path]:
        return self.rw + self.ro


def setup_notes_folder(session_id: str, post_id: int) -> NotesConfig:
    """Create session-specific notes folder structure.

    Structure (RW = this session can write, RO = read historical only):
    - notes/sessions/<session_id>/            (RW)
    - notes/research/<post_id>/<timestamp>/   (RW)
    - notes/forecasts/<post_id>/<timestamp>/  (RW)
    - notes/meta/                             (RW)
    - notes/research/                         (RO)
    - notes/forecasts/                        (RO)
    - notes/structured/                       (RO - notes tool writes here)
    - notes/logs/                             (NO ACCESS - for feedback loop only)

    Args:
        session_id: Unique session identifier.
        post_id: Metaculus post ID (the URL identifier, e.g., 41976). Use 0 for sub-forecasts.

    Returns:
        NotesConfig with RW and RO directories separated.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    session_path = NOTES_BASE_PATH / "sessions" / session_id
    research_base = NOTES_BASE_PATH / "research"
    research_path = research_base / str(post_id) / timestamp
    forecasts_base = NOTES_BASE_PATH / "forecasts"
    forecasts_path = forecasts_base / str(post_id) / timestamp
    meta_path = NOTES_BASE_PATH / "meta"
    structured_path = NOTES_BASE_PATH / "structured"
    logs_path = NOTES_BASE_PATH / "logs"

    session_path.mkdir(parents=True, exist_ok=True)
    research_path.mkdir(parents=True, exist_ok=True)
    forecasts_path.mkdir(parents=True, exist_ok=True)
    meta_path.mkdir(parents=True, exist_ok=True)
    logs_path.mkdir(parents=True, exist_ok=True)

    # Reasoning log file for this session (agent cannot access notes/logs/)
    reasoning_log = logs_path / f"{post_id}_{timestamp}.md"

    return NotesConfig(
        session=session_path,
        research=research_path,
        forecasts=forecasts_path,
        reasoning_log=reasoning_log,
        rw=[session_path, research_path, forecasts_path, meta_path],
        ro=[research_base, forecasts_base, structured_path],
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
) -> dict[str, Any]:
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


async def fetch_question(question_id: int, token: str | None = None) -> dict:
    """Fetch question details from Metaculus API."""
    headers = {"Authorization": f"Token {token}"} if token else {}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{METACULUS_API_BASE}/posts/{question_id}/",
            headers=headers,
        )
        response.raise_for_status()
        return response.json()


def build_question_context(post_data: dict) -> dict:
    """Extract relevant question data for the agent prompt."""
    question = post_data.get("question", {})
    question_type = question.get("type", "binary")

    context = {
        "title": question.get("title", "Unknown"),
        "type": question_type,
        "description": post_data.get("description") or question.get("description", ""),
        "resolution_criteria": question.get("resolution_criteria", ""),
        "fine_print": question.get("fine_print", ""),
        "scheduled_close_time": question.get("scheduled_close_time"),
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


def extract_sources(messages: list[AssistantMessage]) -> list[str]:
    """Extract web sources from tool use blocks."""
    sources = []
    for msg in messages:
        for block in msg.content:
            if isinstance(block, ToolUseBlock) and block.name in (
                "WebSearch",
                "WebFetch",
                "mcp__forecasting__search_exa",
                "mcp__forecasting__search_news",
            ):
                if isinstance(block.input, dict):
                    source = block.input.get("url") or block.input.get("query")
                    if source:
                        sources.append(str(source))
    return sources


async def run_forecast(
    question_id: int | None = None,
    *,
    question_context: dict | None = None,
    allow_spawn: bool = True,
) -> ForecastOutput:
    """Run the forecasting agent on a question.

    Args:
        question_id: Metaculus post ID (for top-level forecasts)
        question_context: Pre-built context dict (for sub-forecasts from spawn_subquestions)
        allow_spawn: Whether this forecast can spawn subquestions (False for sub-forecasts)

    Returns:
        ForecastOutput with the forecast results.
    """
    # Generate session ID based on question_id for persistence
    if question_id is not None:
        session_id = str(question_id)
    else:
        # Sub-forecasts use timestamp-based ID since they don't have a real question_id
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Reset metrics for this forecast session
    reset_metrics()

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

    # Setup notes folder (using post_id for directory structure)
    notes = setup_notes_folder(session_id, post_id)
    logger.info("Notes folder: %s", notes.session)

    # Get type-specific output schema and guidance
    model_class, output_schema = get_output_schema_for_question(question_type)
    type_guidance = get_type_specific_guidance(question_type, context)

    # Load past forecasts for this question (if any)
    history_context = ""
    if post_id > 0:
        past_forecasts = load_past_forecasts(post_id)
        if past_forecasts:
            history_context = format_history_for_context(past_forecasts)
            logger.info(
                "Loaded %d past forecasts for post %d",
                len(past_forecasts),
                post_id,
            )

    prompt = f"Analyze this forecasting question and provide your forecast:\n\n{json.dumps(context, indent=2)}\n\n{type_guidance}"
    if history_context:
        prompt += f"\n\n{history_context}"

    collected_text: list[str] = []
    collected_thinking: list[str] = []
    assistant_messages: list[AssistantMessage] = []
    result: ResultMessage | None = None

    # Setup thinking log file (verbose, gitignored)
    thinking_log_path = (
        LOGS_BASE_PATH / session_id / datetime.now().strftime("%Y%m%d_%H%M%S.log")
    )
    thinking_log_path.parent.mkdir(parents=True, exist_ok=True)

    # Setup reasoning logger (committed, for feedback loop)
    reasoning_logger = ReasoningLogger(notes.reasoning_log, question_title)

    with Sandbox() as sandbox:
        # tmp/ for scratch work + session-specific notes directories
        rw_dirs = [Path("tmp")] + notes.rw
        ro_dirs = notes.ro
        hooks = create_permission_hooks(rw_dirs=rw_dirs, ro_dirs=ro_dirs)

        options = ClaudeAgentOptions(
            model=settings.model,
            system_prompt={
                "type": "preset",
                "preset": "claude_code",
                "append": get_forecasting_system_prompt(),
            },
            max_thinking_tokens=64_000 - 1,
            permission_mode="bypassPermissions",
            hooks=hooks,  # type: ignore[arg-type]
            sandbox={
                "enabled": True,
                "autoAllowBashIfSandboxed": True,
                "allowUnsandboxedCommands": False,
            },
            mcp_servers={
                "forecasting": forecasting_server,
                "financial": financial_server,
                "sandbox": sandbox.create_mcp_server(),
                "composition": composition_server,
                "markets": markets_server,
                "notes": notes_server,
                "trends": trends_server,
            },
            agents=SUBAGENTS,
            add_dirs=[str(d) for d in notes.all_dirs],
            # Built-in tools + MCP tools (conditionally include spawn_subquestions)
            allowed_tools=[
                # Built-in tools
                "WebSearch",
                "WebFetch",
                # File tools for notes (directory-restricted via hooks)
                "Read",
                "Write",
                "Glob",
                # Bash (sandboxed via SDK config)
                "Bash",
                # Metaculus tools (only if token is configured)
                *(
                    [
                        "mcp__forecasting__get_metaculus_questions",
                        "mcp__forecasting__list_tournament_questions",
                        "mcp__forecasting__search_metaculus",
                        "mcp__forecasting__get_coherence_links",
                        "mcp__forecasting__get_prediction_history",
                        "mcp__forecasting__get_cp_history",
                    ]
                    if settings.metaculus_token
                    else []
                ),
                # Search tools (conditional on API credentials)
                *_optional_tools(
                    settings.exa_api_key,
                    ["mcp__forecasting__search_exa"],
                ),
                *_optional_tools(
                    settings.asknews_client_id and settings.asknews_client_secret,
                    ["mcp__forecasting__search_news"],
                ),
                "mcp__forecasting__wikipedia",  # Unified: search, summary, or full
                # Financial data tools (conditional on API credentials)
                *_optional_tools(
                    settings.fred_api_key,
                    ["mcp__financial__fred_series", "mcp__financial__fred_search"],
                ),
                # Sandbox tools (in-process Docker sandbox)
                "mcp__sandbox__execute_code",
                "mcp__sandbox__install_package",
                # Composition tools
                # spawn_subquestions only available for top-level forecasts
                *(["mcp__composition__spawn_subquestions"] if allow_spawn else []),
                # Prediction market tools
                "mcp__markets__polymarket_price",
                "mcp__markets__manifold_price",
                # Stock market tools (no API key required)
                "mcp__markets__stock_price",
                "mcp__markets__stock_history",
                # Google Trends tools (no API key required)
                "mcp__trends__google_trends",
                "mcp__trends__google_trends_compare",
                "mcp__trends__google_trends_related",
                # Notes browsing tools
                "mcp__notes__notes",
                # Subagent spawning
                "Task",
            ],
            output_format={
                "type": "json_schema",
                "schema": output_schema,
            },
        )

        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)

            async for message in client.receive_response():
                match message:
                    case AssistantMessage():
                        assistant_messages.append(message)
                        for block in message.content:
                            print_block(block)
                            reasoning_logger.log_block(block)
                            match block:
                                case TextBlock():
                                    collected_text.append(block.text)
                                    # Check for credit exhaustion
                                    credit_error = CreditExhaustedError.from_message(
                                        block.text
                                    )
                                    if credit_error:
                                        raise credit_error
                                case ThinkingBlock():
                                    collected_thinking.append(block.thinking)
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
                        logger.info(
                            "System message [%s]: %s",
                            message.subtype,
                            json.dumps(message.data, indent=2),
                        )
                    case UserMessage():
                        if isinstance(message.content, list):
                            for block in message.content:
                                print_block(block)
                                reasoning_logger.log_block(block)
                    case _:
                        print(f"📨 {type(message).__name__}: {message}")
                        logger.debug(
                            "Unhandled message type: %s", type(message).__name__
                        )

    if result is None:
        raise RuntimeError("No result received from agent")

    # Save thinking log (verbose, gitignored)
    if collected_thinking:
        thinking_log_content = "\n\n---\n\n".join(collected_thinking)
        thinking_log_path.write_text(thinking_log_content, encoding="utf-8")
        logger.info("Saved thinking log to %s", thinking_log_path)

    # Save reasoning log (committed, for feedback loop)
    reasoning_logger.save()

    # Extract structured forecast based on question type
    output = ForecastOutput(
        question_id=actual_question_id,
        post_id=post_id,
        question_title=question_title,
        question_type=question_type,
        summary="No forecast produced",
        factors=[],
        reasoning="".join(collected_text),
        sources_consulted=extract_sources(assistant_messages),
        duration_seconds=(result.duration_ms / 1000) if result.duration_ms else None,
        cost_usd=result.total_cost_usd,
        token_usage=cast(TokenUsage, result.usage) if result.usage else None,
    )

    if result.structured_output:
        forecast = model_class.model_validate(result.structured_output)
        output.summary = forecast.summary
        output.factors = forecast.factors

        if isinstance(forecast, Forecast):
            output.logit = forecast.logit
            output.probability = forecast.probability
            output.probability_from_logit = forecast.probability_from_logit

            # Check for consistency issues
            consistency_warnings = forecast.check_consistency()
            for warning in consistency_warnings:
                logger.warning("Consistency check: %s", warning)
        elif isinstance(forecast, NumericForecast):
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
                    output.cdf = None
        elif isinstance(forecast, MultipleChoiceForecast):
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

    # Search for meta-reflection markdown files (required for top-level forecasts)
    if post_id > 0:
        meta_dir = Path("./notes/meta")
        meta_files = []

        if meta_dir.exists():
            # Find files matching _q<post_id>_ pattern (agent writes using post_id)
            pattern = f"_q{post_id}_"
            meta_files = [f for f in meta_dir.glob("*.md") if pattern in f.name]
            # Sort by filename (timestamp prefix) descending
            meta_files.sort(key=lambda f: f.name, reverse=True)

        # Extract subagents from tool metrics
        subagents_used = []
        if metrics and "by_tool" in metrics:
            for tool_name in metrics["by_tool"]:
                if tool_name == "Task":
                    subagents_used.append("(via Task)")

        if meta_files:
            meta_file = meta_files[0]
            output.meta = ForecastMeta(
                meta_file_path=str(meta_file),
                tools_used_count=metrics.get("total_calls", 0) if metrics else 0,
                subagents_used=subagents_used,
            )
            logger.info("Found meta-reflection %s for post %d", meta_file.name, post_id)

            # Inject programmatic metrics into the meta-reflection
            append_metrics_to_meta_reflection(
                meta_file,
                metrics=metrics,
                duration_seconds=output.duration_seconds,
                cost_usd=output.cost_usd,
                token_usage=output.token_usage,
                log_path=thinking_log_path if thinking_log_path.exists() else None,
                post_id=post_id,
                question_id=actual_question_id,
                sources=output.sources_consulted,
            )
        else:
            # Meta-reflection is required - log error but don't fail the forecast
            logger.error(
                "MISSING META-REFLECTION for post %d. "
                "Agent failed to write a meta-reflection to notes/meta/ before final output. "
                "This is a required step for tracking process reflection.",
                post_id,
            )
            output.meta = ForecastMeta(
                meta_file_path=None,
                tools_used_count=metrics.get("total_calls", 0) if metrics else 0,
                subagents_used=subagents_used,
            )

    # Auto-save forecast to history (for top-level forecasts only)
    if post_id > 0 and actual_question_id > 0:
        try:
            save_forecast(
                question_id=actual_question_id,
                post_id=post_id,
                question_title=question_title,
                question_type=question_type,
                summary=output.summary,
                factors=[f.model_dump() for f in output.factors],
                probability=output.probability,
                logit=output.logit,
                probabilities=output.probabilities,
                median=output.median,
                confidence_interval=output.confidence_interval,
                percentiles=output.percentiles,
                tool_metrics=metrics,
                token_usage=output.token_usage,
                log_path=str(thinking_log_path) if thinking_log_path.exists() else None,
            )
        except Exception as e:
            logger.warning("Failed to auto-save forecast: %s", e)

    return output


# Wire up spawn_subquestions to use run_forecast recursively
set_run_forecast_fn(run_forecast)
