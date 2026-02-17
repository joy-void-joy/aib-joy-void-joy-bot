"""Meta-reflection tool for forecasting sessions.

Writes meta-reflections to the session directory. This is write-only by
design — the agent cannot read meta-reflections from other sessions,
which prevents anchoring/biasing from past reflections.
"""

import logging
from pathlib import Path
from typing import Any

import aiofiles
from pydantic import BaseModel, Field

from claude_agent_sdk import tool

from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


class WriteMetaInput(BaseModel):
    """Input for the write_meta tool."""

    content: str = Field(description="Your full meta-reflection markdown")


_WRITE_META_DESCRIPTION = """\
Write your REQUIRED meta-reflection before providing your final forecast.

This is write-only — you cannot read meta from other sessions.
Write your reflection on: research process, tool effectiveness, reasoning quality,
calibration notes, and what you'd do differently.

Example:
  write_meta(content="# Meta-Reflection\\n\\n## Executive Summary...")
"""


async def _write_meta(session_dir: Path, content: str) -> dict[str, Any]:
    """Write meta-reflection to the session directory."""
    if not content or not content.strip():
        return mcp_error("write_meta requires 'content' parameter with your reflection")

    session_dir.mkdir(parents=True, exist_ok=True)
    filepath = session_dir / "meta.md"

    try:
        async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
            await f.write(content)

        logger.info("Wrote meta-reflection to %s", filepath)

        return mcp_success(
            {
                "path": str(filepath),
                "message": "Meta-reflection saved successfully",
            }
        )
    except Exception as e:
        logger.exception("Failed to write meta-reflection")
        return mcp_error(f"Failed to write meta-reflection: {e}")


def _create_write_meta_tool(session_dir: Path | None = None):
    """Create the write_meta tool with session context.

    Args:
        session_dir: The session directory for meta-reflection storage.
            If None, write_meta is disabled.
    """

    @tool(
        "write_meta",
        _WRITE_META_DESCRIPTION,
        WriteMetaInput,
    )
    @tracked("write_meta")
    async def write_meta_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Write meta-reflection for the current forecasting session."""
        try:
            validated = WriteMetaInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        if session_dir is None:
            return mcp_error("write_meta is not available in this context")

        return await _write_meta(session_dir, validated.content)

    return write_meta_tool


def create_write_meta_server(session_dir: Path | None = None):
    """Create the write_meta MCP server with session context.

    Args:
        session_dir: Session directory for meta-reflection storage.
            If None, write_meta is disabled.

    Returns:
        MCP server configured with the write_meta tool.
    """
    return create_mcp_server(
        name="notes",
        version="3.0.0",
        tools=[_create_write_meta_tool(session_dir)],
    )
