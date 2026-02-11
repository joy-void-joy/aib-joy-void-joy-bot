"""Content block display and stream logging utilities.

Extracted from core.py to avoid circular imports — tools that need
print_block can import from here without pulling in the full agent.
"""

import itertools
import json
import logging

from rich.console import Console

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


def truncate_content(content: str | list | None, max_len: int = 500) -> str:
    """Normalize and truncate content for display."""
    text = _normalize_content(content)
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text


def normalize_content(content: str | list | None) -> str:
    """Convert MCP content blocks to a plain string."""
    return _normalize_content(content)


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
            print(f"{prefix}📋 Result ", end="")
            _console.print(f"[{block.tool_use_id}]", style=color, end="")
            print(": ", end="")
            print(truncate_content(block.content, max_len=500))
            stream_log.info(
                "%sTOOL_RESULT [%s]: %s",
                prefix,
                block.tool_use_id,
                _normalize_content(block.content),
            )
        case _:
            print(f"{prefix}❓ {type(block).__name__}: {block}")
            stream_log.info("%sUNKNOWN: %s: %s", prefix, type(block).__name__, block)
