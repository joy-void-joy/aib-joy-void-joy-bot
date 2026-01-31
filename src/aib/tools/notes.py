"""Notes browsing tools for exploring research and forecast history.

Provides tools to list, search, and read notes created during forecasting sessions.
"""

import logging
import re
from pathlib import Path
from typing import Any, Required, TypedDict

from claude_agent_sdk import create_sdk_mcp_server, tool

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

# Base path for notes storage
NOTES_BASE_PATH = Path("./notes")


class BrowseNotesInput(TypedDict, total=False):
    mode: Required[str]  # "list", "search", or "read"
    path: str  # For list: subdirectory to list; For read: file path
    query: str  # For search: search query


@tool(
    "browse_notes",
    (
        "Browse notes from past forecasting sessions. "
        "Modes: 'list' shows files in a directory with first-line summaries, "
        "'search' finds notes containing a query, "
        "'read' returns the full content of a note file."
    ),
    {"mode": str, "path": str, "query": str},
)
@tracked("browse_notes")
async def browse_notes(args: BrowseNotesInput) -> dict[str, Any]:
    """Browse, search, and read notes from forecasting sessions."""
    mode = args["mode"]

    if mode == "list":
        return await _list_notes(args.get("path", ""))
    elif mode == "search":
        query = args.get("query")
        if not query:
            return mcp_error("Search mode requires 'query' parameter")
        return await _search_notes(query)
    elif mode == "read":
        path = args.get("path")
        if not path:
            return mcp_error("Read mode requires 'path' parameter")
        return await _read_note(path)
    else:
        return mcp_error(f"Unknown mode: {mode}. Use 'list', 'search', or 'read'.")


async def _list_notes(subpath: str) -> dict[str, Any]:
    """List notes in a directory with first-line summaries."""
    target_dir = NOTES_BASE_PATH / subpath if subpath else NOTES_BASE_PATH

    if not target_dir.exists():
        return mcp_error(f"Directory not found: {subpath or 'notes/'}")

    if not target_dir.is_dir():
        return mcp_error(f"Not a directory: {subpath}")

    results = []

    # List subdirectories first
    for item in sorted(target_dir.iterdir()):
        if item.is_dir():
            # Count files in subdirectory
            file_count = len(list(item.glob("**/*.*")))
            results.append(
                {
                    "name": item.name,
                    "type": "directory",
                    "path": str(item.relative_to(NOTES_BASE_PATH)),
                    "file_count": file_count,
                }
            )

    # Then list files
    for item in sorted(target_dir.iterdir()):
        if item.is_file():
            # Get first line as summary
            try:
                content = item.read_text(encoding="utf-8")
                first_line = content.split("\n")[0].strip()
                # Remove markdown heading prefix
                if first_line.startswith("#"):
                    first_line = first_line.lstrip("#").strip()
                # Truncate if too long
                if len(first_line) > 100:
                    first_line = first_line[:97] + "..."
            except Exception:
                first_line = "[Could not read file]"

            results.append(
                {
                    "name": item.name,
                    "type": "file",
                    "path": str(item.relative_to(NOTES_BASE_PATH)),
                    "summary": first_line,
                    "size_bytes": item.stat().st_size,
                }
            )

    return mcp_success(
        {
            "directory": subpath or "notes/",
            "items": results,
            "count": len(results),
        }
    )


async def _search_notes(query: str) -> dict[str, Any]:
    """Search all notes for a query string."""
    results = []
    pattern = re.compile(re.escape(query), re.IGNORECASE)

    for filepath in NOTES_BASE_PATH.glob("**/*.*"):
        if not filepath.is_file():
            continue

        try:
            content = filepath.read_text(encoding="utf-8")
            matches = list(pattern.finditer(content))

            if matches:
                # Get context around first match
                first_match = matches[0]
                start = max(0, first_match.start() - 50)
                end = min(len(content), first_match.end() + 50)
                context = content[start:end].replace("\n", " ")

                if start > 0:
                    context = "..." + context
                if end < len(content):
                    context = context + "..."

                results.append(
                    {
                        "path": str(filepath.relative_to(NOTES_BASE_PATH)),
                        "match_count": len(matches),
                        "context": context,
                    }
                )
        except Exception as e:
            logger.debug("Could not search %s: %s", filepath, e)

    # Sort by match count (most matches first)
    results.sort(key=lambda x: x["match_count"], reverse=True)

    return mcp_success(
        {
            "query": query,
            "results": results[:20],  # Limit to 20 results
            "total_matches": len(results),
        }
    )


async def _read_note(path: str) -> dict[str, Any]:
    """Read the full content of a note file."""
    filepath = NOTES_BASE_PATH / path

    if not filepath.exists():
        return mcp_error(f"File not found: {path}")

    if not filepath.is_file():
        return mcp_error(f"Not a file: {path}")

    # Security check: ensure path is within notes directory
    try:
        filepath.resolve().relative_to(NOTES_BASE_PATH.resolve())
    except ValueError:
        return mcp_error("Access denied: path is outside notes directory")

    try:
        content = filepath.read_text(encoding="utf-8")

        # Truncate very long files
        max_chars = 50000
        truncated = len(content) > max_chars
        if truncated:
            content = (
                content[:max_chars]
                + "\n\n[Content truncated - file exceeds 50,000 characters]"
            )

        return mcp_success(
            {
                "path": path,
                "content": content,
                "truncated": truncated,
                "size_bytes": filepath.stat().st_size,
            }
        )
    except Exception as e:
        logger.exception("Failed to read note file")
        return mcp_error(f"Failed to read file: {e}")


# --- MCP Server ---

notes_server = create_sdk_mcp_server(
    name="notes",
    version="1.0.0",
    tools=[
        browse_notes,
    ],
)
