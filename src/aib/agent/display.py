"""Content block display and stream logging utilities.

Extracted from core.py to avoid circular imports — tools that need
print_block can import from here without pulling in the full agent.
"""

import itertools
import json
import logging

from rich.console import Console
from rich.style import Style

from claude_agent_sdk import (
    ContentBlock,
    TextBlock,
    ThinkingBlock,
    ToolResultBlock,
    ToolUseBlock,
)

_TOOL_COLORS = [
    "cyan",
    "green",
    "yellow",
    "magenta",
    "blue",
    "red",
    "bright_cyan",
    "bright_green",
    "bright_yellow",
    "bright_magenta",
    "bright_blue",
    "bright_red",
]
_color_cycle = itertools.cycle(_TOOL_COLORS)
_agent_color_cycle = itertools.cycle(_TOOL_COLORS)
_id_to_color: dict[str, str] = {}
_console = Console(highlight=False, markup=False)
stream_log = logging.getLogger("aib.agent.stream")


def _normalize_content(content: str | list | None) -> str:
    """Convert MCP content blocks to a plain string."""
    if content is None:
        return "(empty)"
    if isinstance(content, list):
        texts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item.get("text", ""))
        return "\n".join(texts)
    return content


def _truncate_str(value: str, max_len: int = 500) -> str:
    if len(value) > max_len:
        return value[:max_len] + "..."
    return value


def _truncate_str_fields(obj: object, max_len: int = 500) -> object:
    """Recursively truncate string values in a JSON-like structure."""
    if isinstance(obj, dict):
        return {k: _truncate_str_fields(v, max_len) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_truncate_str_fields(item, max_len) for item in obj]
    if isinstance(obj, str):
        return _truncate_str(obj, max_len)
    return obj


def _format_tool_result(content: str | list | None, max_len: int = 500) -> str:
    """Format tool result content for display.

    If the content parses as a JSON dict, pretty-print it with string fields
    truncated. Otherwise fall back to plain truncation.
    """
    text = _normalize_content(content)
    try:
        parsed = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return _truncate_str(text, max_len)
    truncated = _truncate_str_fields(parsed, max_len)
    return json.dumps(truncated, indent=2)


def truncate_content(content: str | list | None, max_len: int = 500) -> str:
    """Normalize and truncate content for display."""
    text = _normalize_content(content)
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text


def normalize_content(content: str | list | None) -> str:
    """Convert MCP content blocks to a plain string."""
    return _normalize_content(content)


def _truncate_label(label: str, max_len: int = 30) -> str:
    """Clean and truncate a label for use inside an agent prefix tag."""
    cleaned = label.replace("\n", " ").strip()
    return cleaned[: max_len - 3] + "..." if len(cleaned) > max_len else cleaned


def make_agent_prefix(agent_type: str, label: str | None = None) -> str:
    """Build an ANSI-colored prefix like '  ↳ [research: <label>] ' for a nested sub-agent.

    Each call picks the next color from a cycle so parallel/sequential
    sub-agent instances can be visually distinguished. Call once per
    sub-agent launch and reuse the returned prefix across all print_block
    calls for that instance.
    """
    tag = f"[{agent_type}: {_truncate_label(label)}]" if label else f"[{agent_type}]"
    return f"  ↳ {Style(color=next(_agent_color_cycle)).render(tag)} "


def print_block(block: ContentBlock, prefix: str = "") -> None:
    """Print a content block with appropriate emoji prefix and log it.

    Args:
        block: The content block to print.
        prefix: Optional prefix for visual nesting (e.g. "  ↳ [search] ").
    """
    match block:
        case ThinkingBlock():
            print(f"{prefix}💭 {block.thinking}")
            stream_log.info("%sTHINKING: %s", prefix, block.thinking)
        case TextBlock():
            print(f"{prefix}💬 {block.text}")
            stream_log.info("%sTEXT: %s", prefix, block.text)
        case ToolUseBlock():
            color = next(_color_cycle)
            _id_to_color[block.id] = color
            print(f"{prefix}🔧 {block.name} ", end="")
            _console.print(f"[{block.id}]", style=color)
            if block.input:
                print(json.dumps(block.input, indent=2))
            stream_log.info(
                "%sTOOL_USE [%s] %s: %s",
                prefix,
                block.id,
                block.name,
                json.dumps(block.input) if block.input else "",
            )
        case ToolResultBlock():
            color = _id_to_color.pop(block.tool_use_id, "default")
            formatted = _format_tool_result(block.content)
            print(f"{prefix}📋 Result ", end="")
            _console.print(f"[{block.tool_use_id}]", style=color)
            print(formatted)
            stream_log.info(
                "%sTOOL_RESULT [%s]: %s",
                prefix,
                block.tool_use_id,
                formatted,
            )
        case _:
            print(f"{prefix}❓ {type(block).__name__}: {block}")
            stream_log.info("%sUNKNOWN: %s: %s", prefix, type(block).__name__, block)
