"""Structured notes tool for forecasting research and reasoning.

Notes are stored as JSON files with consistent schema for easy search and retrieval.
Supports list, search, read, and write operations.
"""

import logging
import re
import uuid
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Literal, Required, TypedDict

from pydantic import BaseModel, Field

from claude_agent_sdk import create_sdk_mcp_server, tool

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

NOTES_BASE_PATH = Path("./notes")


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
    summary: str = Field(description="1-2 sentence summary, always shown in search results")
    content: str = Field(description="Full details, only returned on explicit read")
    sources: list[str] = Field(default_factory=list, description="URLs or references")
    confidence: float | None = Field(
        default=None, ge=0, le=1, description="Confidence level for estimates"
    )
    question_id: int | None = Field(default=None, description="Associated Metaculus question ID")
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


class NotesInput(TypedDict, total=False):
    mode: Required[Literal["list", "search", "read", "write"]]
    # For list
    type_filter: str  # Filter by NoteType
    question_id: int  # Filter by question
    # For search
    query: str
    # For read
    id: str
    # For write
    type: str
    topic: str
    summary: str
    content: str
    sources: list[str]
    confidence: float
    report_path: str


# --- Storage Helpers ---


def _get_notes_dir() -> Path:
    """Get the notes storage directory, creating if needed."""
    notes_dir = NOTES_BASE_PATH / "structured"
    notes_dir.mkdir(parents=True, exist_ok=True)
    return notes_dir


def _load_all_notes() -> list[Note]:
    """Load all notes from storage."""
    notes_dir = _get_notes_dir()
    notes = []

    for filepath in notes_dir.glob("*.json"):
        try:
            content = filepath.read_text(encoding="utf-8")
            note = Note.model_validate_json(content)
            notes.append(note)
        except Exception as e:
            logger.warning("Failed to load note %s: %s", filepath, e)

    return notes


def _save_note(note: Note) -> Path:
    """Save a note to storage."""
    notes_dir = _get_notes_dir()
    filepath = notes_dir / f"{note.id}.json"
    filepath.write_text(note.model_dump_json(indent=2), encoding="utf-8")
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


@tool(
    "notes",
    (
        "Manage structured notes for forecasting research. "
        "Modes: 'list' shows note summaries (filterable by type/question), "
        "'search' finds notes by query (returns summaries only), "
        "'read' gets full note content by ID, "
        "'write' creates a new structured note."
    ),
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
    },
)
@tracked("notes")
async def notes_tool(args: NotesInput) -> dict[str, Any]:
    """Manage structured notes for forecasting research."""
    mode = args["mode"]

    if mode == "list":
        return await _list_notes(
            type_filter=args.get("type_filter"),
            question_id=args.get("question_id"),
        )
    elif mode == "search":
        query = args.get("query")
        if not query:
            return mcp_error("Search mode requires 'query' parameter")
        return await _search_notes(
            query=query,
            type_filter=args.get("type_filter"),
        )
    elif mode == "read":
        note_id = args.get("id")
        if not note_id:
            return mcp_error("Read mode requires 'id' parameter")
        return await _read_note(note_id)
    elif mode == "write":
        return await _write_note(args)
    else:
        return mcp_error(
            f"Unknown mode: {mode}. Use 'list', 'search', 'read', or 'write'."
        )


async def _list_notes(
    type_filter: str | None = None,
    question_id: int | None = None,
) -> dict[str, Any]:
    """List notes with optional filtering."""
    notes = _load_all_notes()

    # Apply filters
    if type_filter:
        try:
            note_type = NoteType(type_filter)
            notes = [n for n in notes if n.type == note_type]
        except ValueError:
            valid_types = [t.value for t in NoteType]
            return mcp_error(f"Invalid type_filter: {type_filter}. Valid: {valid_types}")

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
) -> dict[str, Any]:
    """Search notes by query, returning summaries only."""
    notes = _load_all_notes()

    # Apply type filter first
    if type_filter:
        try:
            note_type = NoteType(type_filter)
            notes = [n for n in notes if n.type == note_type]
        except ValueError:
            valid_types = [t.value for t in NoteType]
            return mcp_error(f"Invalid type_filter: {type_filter}. Valid: {valid_types}")

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


async def _read_note(note_id: str) -> dict[str, Any]:
    """Read full note content by ID."""
    notes_dir = _get_notes_dir()
    filepath = notes_dir / f"{note_id}.json"

    if not filepath.exists():
        return mcp_error(f"Note not found: {note_id}")

    try:
        content = filepath.read_text(encoding="utf-8")
        note = Note.model_validate_json(content)
        return mcp_success(note.model_dump(mode="json"))
    except Exception as e:
        logger.exception("Failed to read note")
        return mcp_error(f"Failed to read note: {e}")


async def _write_note(args: NotesInput) -> dict[str, Any]:
    """Create a new structured note."""
    # Validate required fields
    required = ["type", "topic", "summary", "content"]
    missing = [f for f in required if not args.get(f)]
    if missing:
        return mcp_error(f"Write mode requires: {', '.join(missing)}")

    # Validate note type
    note_type_str = args.get("type", "")
    try:
        note_type = NoteType(note_type_str)
    except ValueError:
        valid_types = [t.value for t in NoteType]
        return mcp_error(f"Invalid type: {note_type_str}. Valid: {valid_types}")

    # Create note
    note = Note(
        type=note_type,
        topic=args.get("topic", ""),
        summary=args.get("summary", ""),
        content=args.get("content", ""),
        sources=args.get("sources", []),
        confidence=args.get("confidence"),
        question_id=args.get("question_id"),
        report_path=args.get("report_path"),
    )

    # Save
    filepath = _save_note(note)
    logger.info("Created note %s at %s", note.id, filepath)

    return mcp_success(
        {
            "id": note.id,
            "type": note.type.value,
            "topic": note.topic,
            "message": "Note created successfully",
        }
    )


# --- MCP Server ---

notes_server = create_sdk_mcp_server(
    name="notes",
    version="2.0.0",
    tools=[
        notes_tool,
    ],
)
