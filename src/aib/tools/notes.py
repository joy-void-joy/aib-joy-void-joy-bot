"""Structured notes tool for forecasting research and reasoning.

Notes are stored as JSON files with consistent schema for easy search and retrieval.
Supports list, search, read, write, and write_meta operations.

The write_meta mode writes meta-reflections to the session directory. This is
write-only by design - the agent cannot read meta-reflections from other sessions.
"""

import asyncio
import logging
import re
import uuid
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Literal

import aiofiles
from pydantic import BaseModel, Field

from claude_agent_sdk import tool

from aib.tools.mcp_server import create_mcp_server

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

NOTES_BASE_PATH = Path("./notes")
SESSIONS_PATH = NOTES_BASE_PATH / "sessions"


class NoteType(str, Enum):
    """Types of notes that can be created."""

    research = "research"  # Web search findings, collected sources
    finding = "finding"  # Key facts discovered during research
    estimate = "estimate"  # Fermi estimates, calculations, quantitative analysis
    reasoning = "reasoning"  # Logical analysis, factor assessment, arguments
    source = "source"  # Reference to external source with summary


class Note(BaseModel):
    """A structured note with metadata for searchability."""

    id: str = Field(default_factory=lambda: uuid.uuid4().hex[:12])
    type: NoteType
    topic: str = Field(description="Short topic/title for the note")
    summary: str = Field(
        description="1-2 sentence summary, always shown in search results"
    )
    content: str = Field(description="Full details, only returned on explicit read")
    sources: list[str] = Field(default_factory=list, description="URLs or references")
    confidence: float | None = Field(
        default=None, ge=0, le=1, description="Confidence level for estimates"
    )
    question_id: int | None = Field(
        default=None, description="Associated Metaculus question ID"
    )
    report_path: str | None = Field(
        default=None, description="Path to detailed .md report file if any"
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class NoteSummary(BaseModel):
    """Lightweight note representation for list/search results."""

    id: str
    type: NoteType
    topic: str
    summary: str
    question_id: int | None = None
    has_report: bool = False


# --- Input Types ---


class NotesInput(BaseModel):
    """Input for notes tool."""

    mode: Literal["list", "search", "read", "write", "write_meta", "write_report"]
    # For list
    type_filter: str | None = None
    question_id: int | None = None
    # For search
    query: str | None = None
    # For read
    id: str | None = None
    # For write (structured JSON notes)
    type: str | None = None
    topic: str | None = None
    summary: str | None = None
    content: str | None = None
    sources: list[str] = Field(default_factory=list)
    confidence: float | None = Field(default=None, ge=0, le=1)
    report_path: str | None = None
    # For write_meta (meta-reflections - session-scoped)
    # session_id is injected by server, not provided by agent
    # For write_report (long markdown reports - question-scoped)
    post_id: int | None = None
    title: str | None = None  # Used for report filename slug


# --- Storage Helpers ---


def _get_notes_dir(base: Path = NOTES_BASE_PATH) -> Path:
    """Get the notes storage directory, creating if needed."""
    notes_dir = base / "structured"
    notes_dir.mkdir(parents=True, exist_ok=True)
    return notes_dir


async def _load_all_notes(base: Path = NOTES_BASE_PATH) -> list[Note]:
    """Load all notes from storage (async)."""
    notes_dir = _get_notes_dir(base)
    notes: list[Note] = []

    # Get list of files (sync glob is fine for small directories)
    filepaths = list(notes_dir.glob("*.json"))

    async def load_one(filepath: Path) -> Note | None:
        try:
            async with aiofiles.open(filepath, encoding="utf-8") as f:
                content = await f.read()
            return Note.model_validate_json(content)
        except Exception as e:
            logger.warning("Failed to load note %s: %s", filepath, e)
            return None

    # Load all notes concurrently
    results = await asyncio.gather(*[load_one(fp) for fp in filepaths])
    notes = [n for n in results if n is not None]

    return notes


async def _save_note(note: Note, base: Path = NOTES_BASE_PATH) -> Path:
    """Save a note to storage (async)."""
    notes_dir = _get_notes_dir(base)
    filepath = notes_dir / f"{note.id}.json"
    async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
        await f.write(note.model_dump_json(indent=2))
    return filepath


def _note_to_summary(note: Note) -> NoteSummary:
    """Convert a Note to a lightweight summary."""
    return NoteSummary(
        id=note.id,
        type=note.type,
        topic=note.topic,
        summary=note.summary,
        question_id=note.question_id,
        has_report=note.report_path is not None,
    )


# --- Tool Implementation ---


_NOTES_TOOL_DESCRIPTION = """\
Manage notes for forecasting research. Choose the right mode for your content:

## Modes

### write (structured JSON notes - SEARCHABLE)
Use for: Facts, estimates, findings you want to find later via search.
Required: type, topic, summary, content
Optional: sources, confidence, question_id

Types: research, finding, estimate, reasoning, source

Example:
  notes(mode="write", type="finding", topic="Tesla Q1 base rate",
        summary="Historical Q1 deliveries average 15% below annual run rate",
        content="Full analysis...", question_id=41906)

### write_meta (meta-reflection - REQUIRED)
Use for: Your REQUIRED meta-reflection before final output.
Required: content (your full meta-reflection markdown)

This is write-only - you cannot read meta from other sessions.
Write your reflection on: research process, tool effectiveness, reasoning quality,
calibration notes, and what you'd do differently.

Example:
  notes(mode="write_meta", content="# Meta-Reflection\\n\\n## Executive Summary...")

### write_report (long markdown - readable by future sessions)
Use for: In-depth research reports (>500 words) worth preserving.
Required: post_id, content
Optional: title (for filename)

Example:
  notes(mode="write_report", post_id=41906, title="NYC funding analysis",
        content="# Deep Analysis of NYC Federal Funding...")

### list (browse notes)
Optional: type_filter, question_id

### search (find notes by query)
Required: query
Optional: type_filter

### read (get full note content)
Required: id (note ID from list/search)

## When to Use What

| Content Type | Mode | Searchable? | Readable? |
|-------------|------|-------------|-----------|
| Short facts/estimates | write | Yes | Yes |
| Meta-reflection | write_meta | No | No (write-only) |
| Long research report | write_report | No | Yes |
"""


def _create_notes_tool(
    session_id: str | None = None, notes_base: Path | None = None
):
    """Create the notes tool with optional session context.

    Args:
        session_id: The session ID for write_meta mode. If None, write_meta is disabled.
        notes_base: Override base path for all notes storage. When set, reads/writes
            are scoped to this directory (used in retrodict mode for isolation).
    """
    _base = notes_base or NOTES_BASE_PATH
    _sessions = _base / "sessions"

    @tool(
        "notes",
        _NOTES_TOOL_DESCRIPTION,
        {
            "mode": str,
            "type_filter": str,
            "question_id": int,
            "query": str,
            "id": str,
            "type": str,
            "topic": str,
            "summary": str,
            "content": str,
            "sources": list,
            "confidence": float,
            "report_path": str,
            "post_id": int,
            "title": str,
        },
    )
    @tracked("notes")
    async def notes_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Manage notes for forecasting research."""
        try:
            validated = NotesInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        mode = validated.mode

        if mode == "list":
            return await _list_notes(
                type_filter=validated.type_filter,
                question_id=validated.question_id,
                base=_base,
            )
        elif mode == "search":
            query = validated.query
            if not query:
                return mcp_error("Search mode requires 'query' parameter")
            return await _search_notes(
                query=query,
                type_filter=validated.type_filter,
                base=_base,
            )
        elif mode == "read":
            note_id = validated.id
            if not note_id:
                return mcp_error("Read mode requires 'id' parameter")
            return await _read_note(note_id, base=_base)
        elif mode == "write":
            return await _write_note(validated, base=_base)
        elif mode == "write_meta":
            if not session_id:
                return mcp_error("write_meta is not available in this context")
            return await _write_meta(session_id, validated.content or "", sessions_base=_sessions)
        elif mode == "write_report":
            return await _write_report(validated, base=_base)
        else:
            return mcp_error(
                f"Unknown mode: {mode}. Use 'list', 'search', 'read', 'write', "
                "'write_meta', or 'write_report'."
            )

    return notes_tool


async def _list_notes(
    type_filter: str | None = None,
    question_id: int | None = None,
    base: Path = NOTES_BASE_PATH,
) -> dict[str, Any]:
    """List notes with optional filtering."""
    notes = await _load_all_notes(base)

    # Apply filters
    if type_filter:
        try:
            note_type = NoteType(type_filter)
            notes = [n for n in notes if n.type == note_type]
        except ValueError:
            valid_types = [t.value for t in NoteType]
            return mcp_error(
                f"Invalid type_filter: {type_filter}. Valid: {valid_types}"
            )

    if question_id is not None:
        notes = [n for n in notes if n.question_id == question_id]

    # Sort by created_at descending (newest first)
    notes.sort(key=lambda n: n.created_at, reverse=True)

    summaries = [_note_to_summary(n).model_dump() for n in notes]

    return mcp_success(
        {
            "notes": summaries,
            "count": len(summaries),
            "filters": {
                "type": type_filter,
                "question_id": question_id,
            },
        }
    )


async def _search_notes(
    query: str,
    type_filter: str | None = None,
    base: Path = NOTES_BASE_PATH,
) -> dict[str, Any]:
    """Search notes by query, returning summaries only."""
    notes = await _load_all_notes(base)

    # Apply type filter first
    if type_filter:
        try:
            note_type = NoteType(type_filter)
            notes = [n for n in notes if n.type == note_type]
        except ValueError:
            valid_types = [t.value for t in NoteType]
            return mcp_error(
                f"Invalid type_filter: {type_filter}. Valid: {valid_types}"
            )

    # Search in topic, summary, and content
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    results = []

    for note in notes:
        searchable = f"{note.topic} {note.summary} {note.content}"
        matches = list(pattern.finditer(searchable))
        if matches:
            results.append((note, len(matches)))

    # Sort by match count descending
    results.sort(key=lambda x: x[1], reverse=True)

    summaries = [
        {**_note_to_summary(note).model_dump(), "match_count": count}
        for note, count in results[:20]
    ]

    return mcp_success(
        {
            "query": query,
            "results": summaries,
            "total_matches": len(results),
        }
    )


async def _read_note(note_id: str, base: Path = NOTES_BASE_PATH) -> dict[str, Any]:
    """Read full note content by ID."""
    notes_dir = _get_notes_dir(base)
    filepath = notes_dir / f"{note_id}.json"

    if not filepath.exists():
        return mcp_error(f"Note not found: {note_id}")

    try:
        async with aiofiles.open(filepath, encoding="utf-8") as f:
            content = await f.read()
        note = Note.model_validate_json(content)
        return mcp_success(note.model_dump(mode="json"))
    except Exception as e:
        logger.exception("Failed to read note")
        return mcp_error(f"Failed to read note: {e}")


async def _write_note(validated: NotesInput, base: Path = NOTES_BASE_PATH) -> dict[str, Any]:
    """Create a new structured note."""
    # Validate required fields
    required_fields = {
        "type": validated.type,
        "topic": validated.topic,
        "summary": validated.summary,
        "content": validated.content,
    }
    missing = [f for f, v in required_fields.items() if not v]
    if missing:
        return mcp_error(f"Write mode requires: {', '.join(missing)}")

    # Validate note type
    note_type_str = validated.type or ""
    try:
        note_type = NoteType(note_type_str)
    except ValueError:
        valid_types = [t.value for t in NoteType]
        return mcp_error(f"Invalid type: {note_type_str}. Valid: {valid_types}")

    # Create note
    note = Note(
        type=note_type,
        topic=validated.topic or "",
        summary=validated.summary or "",
        content=validated.content or "",
        sources=validated.sources,
        confidence=validated.confidence,
        question_id=validated.question_id,
        report_path=validated.report_path,
    )

    # Save
    filepath = await _save_note(note, base)
    logger.info("Created note %s at %s", note.id, filepath)

    return mcp_success(
        {
            "id": note.id,
            "type": note.type.value,
            "topic": note.topic,
            "message": "Note created successfully",
        }
    )


def _slugify(text: str, max_length: int = 50) -> str:
    """Convert text to a filesystem-safe slug."""
    # Lowercase and replace spaces/special chars with underscores
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[-\s]+", "_", slug).strip("_")
    return slug[:max_length]


def _parse_session_id(session_id: str) -> tuple[str, str]:
    """Parse session_id into (post_id, timestamp) components.

    Session ID format: <post_id>_<timestamp> (e.g., "41906_20260202_002119")
    or "sub_<timestamp>" for sub-forecasts.
    """
    if session_id.startswith("sub_"):
        return ("0", session_id[4:])

    parts = session_id.split("_", 1)
    if len(parts) == 2:
        return (parts[0], parts[1])
    return (session_id, "unknown")


async def _write_meta(
    session_id: str, content: str, sessions_base: Path = SESSIONS_PATH
) -> dict[str, Any]:
    """Write meta-reflection to the session directory.

    Meta-reflections are write-only by design. The agent cannot read meta from
    other sessions, which prevents anchoring/biasing from past reflections.
    """
    if not content or not content.strip():
        return mcp_error("write_meta requires 'content' parameter with your reflection")

    # Parse session_id to get path: notes/sessions/<post_id>/<timestamp>/
    post_id, timestamp = _parse_session_id(session_id)
    session_dir = sessions_base / post_id / timestamp
    session_dir.mkdir(parents=True, exist_ok=True)

    filepath = session_dir / "meta.md"

    try:
        async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
            await f.write(content)

        logger.info("Wrote meta-reflection to %s", filepath)

        return mcp_success(
            {
                "path": str(filepath),
                "session_id": session_id,
                "message": "Meta-reflection saved successfully",
            }
        )
    except Exception as e:
        logger.exception("Failed to write meta-reflection")
        return mcp_error(f"Failed to write meta-reflection: {e}")


async def _write_report(validated: NotesInput, base: Path = NOTES_BASE_PATH) -> dict[str, Any]:
    """Write a long markdown report for a question.

    Reports are stored in notes/research/<post_id>/ and ARE readable by future
    sessions. Use this for in-depth research that should be discoverable.
    """
    if not validated.post_id:
        return mcp_error("write_report requires 'post_id' parameter")
    if not validated.content or not validated.content.strip():
        return mcp_error("write_report requires 'content' parameter")

    # Generate filename
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    title_slug = _slugify(validated.title or "report")
    filename = f"{timestamp}_{title_slug}.md"

    # Create directory
    report_dir = base / "research" / str(validated.post_id)
    report_dir.mkdir(parents=True, exist_ok=True)

    filepath = report_dir / filename

    try:
        async with aiofiles.open(filepath, "w", encoding="utf-8") as f:
            await f.write(validated.content)

        logger.info("Wrote report to %s", filepath)

        return mcp_success(
            {
                "path": str(filepath),
                "post_id": validated.post_id,
                "filename": filename,
                "message": "Report saved successfully",
            }
        )
    except Exception as e:
        logger.exception("Failed to write report")
        return mcp_error(f"Failed to write report: {e}")


# --- MCP Server Factory ---


def create_notes_server(
    session_id: str | None = None, notes_base: Path | None = None
):
    """Create the notes MCP server with session context.

    Args:
        session_id: Session ID for write_meta mode. Format: "<post_id>_<timestamp>".
            If None, write_meta mode is disabled.
        notes_base: Override base path for notes storage (retrodict isolation).

    Returns:
        MCP server configured with the notes tool.
    """
    return create_mcp_server(
        name="notes",
        version="3.0.0",
        tools=[_create_notes_tool(session_id, notes_base=notes_base)],
    )


# Default server without session (for backwards compatibility)
notes_server = create_notes_server()
