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
    meta = "meta"  # Process reflection notes


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
    mode: Required[Literal["list", "search", "read", "write", "write_report", "write_meta"]]
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
    # For write_report
    markdown_content: str
    # For write_meta
    tools_used: list[str]
    tools_not_used: list[str]
    tools_missing: list[str]
    prompt_issues: list[str]
    suggestions: list[str]
    reflection: str
    effective_tools: list[str]  # Tools that actually helped (vs just used)
    question_title: str  # Question title for context in note


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
        "'write' creates a new structured note, "
        "'write_report' creates a markdown report file + linked note, "
        "'write_meta' creates a process reflection note."
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
        "markdown_content": str,
        "tools_used": list,
        "tools_not_used": list,
        "tools_missing": list,
        "prompt_issues": list,
        "suggestions": list,
        "reflection": str,
        "effective_tools": list,
        "question_title": str,
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
    elif mode == "write_report":
        return await _write_report(args)
    elif mode == "write_meta":
        return await _write_meta(args)
    else:
        return mcp_error(
            f"Unknown mode: {mode}. Use 'list', 'search', 'read', 'write', "
            "'write_report', or 'write_meta'."
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


def _slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[-\s]+", "-", slug).strip("-")
    return slug[:50]


async def _write_report(args: NotesInput) -> dict[str, Any]:
    """Create a markdown report file and linked note.

    Writes markdown to notes/sessions/<question_id>/<topic_slug>_<timestamp>.md
    and creates a Note with report_path pointing to the file.
    """
    # Validate required fields
    required = ["topic", "summary", "markdown_content", "question_id"]
    missing = [f for f in required if not args.get(f)]
    if missing:
        return mcp_error(f"write_report mode requires: {', '.join(missing)}")

    topic = args.get("topic", "")
    summary = args.get("summary", "")
    markdown_content = args.get("markdown_content", "")
    question_id = args.get("question_id")
    sources = args.get("sources", [])

    # Create session directory
    session_dir = NOTES_BASE_PATH / "sessions" / str(question_id)
    session_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    topic_slug = _slugify(topic)
    filename = f"{topic_slug}_{timestamp}.md"
    report_path = session_dir / filename

    # Write markdown file
    report_path.write_text(markdown_content, encoding="utf-8")
    logger.info("Created report at %s", report_path)

    # Create linked note
    relative_path = f"sessions/{question_id}/{filename}"
    note = Note(
        type=NoteType.research,
        topic=topic,
        summary=summary,
        content=f"See report: {relative_path}",
        sources=sources,
        question_id=question_id,
        report_path=relative_path,
    )

    _save_note(note)
    logger.info("Created note %s linking to report", note.id)

    return mcp_success(
        {
            "id": note.id,
            "topic": topic,
            "report_path": str(report_path),
            "relative_path": relative_path,
            "message": "Report and linked note created successfully",
        }
    )


async def _write_meta(args: NotesInput) -> dict[str, Any]:
    """Create a comprehensive process reflection note with markdown report.

    Writes a detailed markdown file to notes/meta/<timestamp>_<slug>.md
    and creates a linked Note for searchability.
    """
    # Validate required fields
    if not args.get("question_id"):
        return mcp_error("write_meta mode requires: question_id")
    if not args.get("tools_used"):
        return mcp_error("write_meta mode requires: tools_used")

    question_id = args.get("question_id")
    question_title = args.get("question_title", "")
    tools_used = args.get("tools_used", [])
    tools_not_used = args.get("tools_not_used", [])
    tools_missing = args.get("tools_missing", [])
    effective_tools = args.get("effective_tools", [])
    prompt_issues = args.get("prompt_issues", [])
    suggestions = args.get("suggestions", [])
    reflection = args.get("reflection", "")

    # Create meta directory
    meta_dir = NOTES_BASE_PATH / "meta"
    meta_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename: <timestamp>_q<id>_<slug>.md
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    title_slug = _slugify(question_title) if question_title else "forecast"
    filename = f"{timestamp}_q{question_id}_{title_slug}.md"
    meta_path = meta_dir / filename

    # Build comprehensive markdown content
    md_lines = [
        f"# Process Reflection: Q{question_id}",
        "",
    ]

    if question_title:
        md_lines.extend([f"**Question:** {question_title}", ""])

    md_lines.extend([
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ])

    # Executive summary
    md_lines.extend([
        "## Executive Summary",
        "",
        f"- **Tools Used:** {len(tools_used)}",
        f"- **Effective Tools:** {len(effective_tools)}",
        f"- **Tools Not Used:** {len(tools_not_used)}",
        f"- **Missing Capabilities:** {len(tools_missing)}",
        f"- **Prompt Issues:** {len(prompt_issues)}",
        f"- **Suggestions:** {len(suggestions)}",
        "",
    ])

    # Reflection section (up front for visibility)
    if reflection:
        md_lines.extend([
            "## Reflection",
            "",
            reflection,
            "",
        ])

    # Tools analysis
    md_lines.extend([
        "## Tool Usage Analysis",
        "",
        "### Tools Used",
        "",
    ])
    if tools_used:
        for tool_name in tools_used:
            md_lines.append(f"- {tool_name}")
    else:
        md_lines.append("*No tools recorded*")
    md_lines.append("")

    if effective_tools:
        md_lines.extend([
            "### Effective Tools",
            "",
            "These tools provided the most value for this forecast:",
            "",
        ])
        for tool_name in effective_tools:
            md_lines.append(f"- {tool_name}")
        md_lines.append("")

    if tools_not_used:
        md_lines.extend([
            "### Tools Not Used",
            "",
            "Available tools that were not utilized:",
            "",
        ])
        for tool_name in tools_not_used:
            md_lines.append(f"- {tool_name}")
        md_lines.append("")

    if tools_missing:
        md_lines.extend([
            "### Missing Capabilities",
            "",
            "Tools or capabilities that would have been helpful:",
            "",
        ])
        for tool_name in tools_missing:
            md_lines.append(f"- {tool_name}")
        md_lines.append("")

    # Process issues and improvements
    if prompt_issues or suggestions:
        md_lines.extend([
            "## Process Improvements",
            "",
        ])

    if prompt_issues:
        md_lines.extend([
            "### Prompt Issues",
            "",
            "Confusion or unclear guidance encountered:",
            "",
        ])
        for issue in prompt_issues:
            md_lines.append(f"- {issue}")
        md_lines.append("")

    if suggestions:
        md_lines.extend([
            "### Suggestions",
            "",
            "Recommendations for system improvement:",
            "",
        ])
        for suggestion in suggestions:
            md_lines.append(f"- {suggestion}")
        md_lines.append("")

    # Write markdown file
    markdown_content = "\n".join(md_lines)
    meta_path.write_text(markdown_content, encoding="utf-8")
    logger.info("Created meta report at %s", meta_path)

    # Build summary for note
    summary_parts = [f"Used {len(tools_used)} tools"]
    if effective_tools:
        summary_parts.append(f"{len(effective_tools)} effective")
    if tools_missing:
        summary_parts.append(f"{len(tools_missing)} missing")
    if prompt_issues:
        summary_parts.append(f"{len(prompt_issues)} issues")
    summary = ", ".join(summary_parts)

    # Create linked note for searchability
    relative_path = f"meta/{filename}"
    topic = f"Process reflection for Q{question_id}"
    if question_title:
        topic = f"Process reflection: {question_title[:50]}"

    note = Note(
        type=NoteType.meta,
        topic=topic,
        summary=summary,
        content=f"See report: {relative_path}",
        question_id=question_id,
        report_path=relative_path,
    )

    _save_note(note)
    logger.info("Created meta note %s linking to %s", note.id, relative_path)

    return mcp_success(
        {
            "id": note.id,
            "type": "meta",
            "topic": note.topic,
            "summary": summary,
            "report_path": str(meta_path),
            "relative_path": relative_path,
            "message": "Process reflection report created successfully",
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
