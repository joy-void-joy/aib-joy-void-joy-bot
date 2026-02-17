"""arXiv paper search tool.

Provides access to academic papers from arXiv.org with reliable publication
dates. Useful for retrodict mode where date filtering is important.

Uses the arxiv Python library: https://pypi.org/project/arxiv/
"""

import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Any, TypedDict

import arxiv
import httpx
import trafilatura
from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff

from claude_agent_sdk.types import McpSdkServerConfig

from aib.tools.extract import extract_with_prompt
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


class ArxivPaper(TypedDict):
    """Parsed arXiv paper data."""

    id: str
    title: str
    summary: str | None
    authors: list[str]
    published: str
    updated: str | None
    categories: list[str]
    primary_category: str
    pdf_url: str | None


class SearchArxivInput(BaseModel):
    """Input for arXiv search."""

    query: str = Field(description="Search query (supports arXiv query syntax)")
    max_results: int = Field(
        default=10, ge=1, le=50, description="Maximum results to return"
    )
    # Hidden from agent - injected by retrodict hook
    cutoff_date: str | None = Field(
        default=None, description="Only return papers submitted before this date"
    )


def _result_to_dict(result: arxiv.Result, cutoff: datetime | None) -> dict[str, Any]:
    """Convert arXiv Result to serializable dict."""
    published = result.published
    if cutoff and published > cutoff:
        return {}  # Skip papers after cutoff

    return {
        "id": result.entry_id,
        "title": result.title,
        "summary": result.summary[:500] if result.summary else None,
        "authors": [str(a) for a in result.authors],
        "published": published.strftime("%Y-%m-%d"),
        "updated": result.updated.strftime("%Y-%m-%d") if result.updated else None,
        "categories": result.categories,
        "primary_category": result.primary_category,
        "pdf_url": result.pdf_url,
    }


@tool(
    "search_arxiv",
    (
        "Search arXiv for academic papers. USE THIS for questions about AI benchmarks, "
        "scientific discoveries, medical research, climate science, or any topic where "
        "peer-reviewed research provides base rates or expert analysis. "
        "Returns titles, abstracts, authors, dates. "
        "Supports arXiv query syntax: au:lastname, ti:word, cat:cs.AI. Max 50 results.\n\n"
        "Examples:\n"
        "  search_arxiv(query='GPT-5 benchmark performance') → find AI capability papers\n"
        "  search_arxiv(query='cat:cs.AI AND ti:reasoning', max_results=20) → AI reasoning papers\n"
        "  search_arxiv(query='au:hinton AND ti:capsule') → papers by author on topic"
    ),
    SearchArxivInput.model_json_schema(),
)
@tracked("search_arxiv")
async def search_arxiv(args: dict[str, Any]) -> dict[str, Any]:
    """Search arXiv for academic papers."""
    try:
        validated = SearchArxivInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    retrodict_date = retrodict_cutoff.get()
    cutoff: datetime | None = None
    if retrodict_date is not None:
        cutoff = datetime.combine(retrodict_date, datetime.min.time())

    try:
        # Use arxiv library - fetch more results if filtering by date
        fetch_count = validated.max_results * 2 if cutoff else validated.max_results

        search = arxiv.Search(
            query=validated.query,
            max_results=fetch_count,
            sort_by=arxiv.SortCriterion.Relevance,
        )

        client = arxiv.Client()
        results: list[dict[str, Any]] = []

        for result in client.results(search):
            paper = _result_to_dict(result, cutoff)
            if paper:  # Skip empty (filtered) results
                results.append(paper)
                if len(results) >= validated.max_results:
                    break

        if not results:
            return mcp_success({"query": validated.query, "results": [], "count": 0})

        return mcp_success(
            {"query": validated.query, "results": results, "count": len(results)}
        )
    except Exception as e:
        logger.exception("arXiv search failed")
        return mcp_error(f"Search failed: {e}")


class FetchArxivInput(BaseModel):
    """Input for fetching an arXiv paper."""

    paper_id: str = Field(
        description=(
            "arXiv paper ID (e.g. '2301.12345' or '2301.12345v2'). "
            "Also accepts full URLs like 'https://arxiv.org/abs/2301.12345'."
        ),
    )
    prompt: str | None = Field(
        default=None,
        description="Extract specific information from the paper (HTML only).",
    )


_ARXIV_ID_PATTERN = re.compile(
    r"(?:https?://arxiv\.org/(?:abs|html|pdf)/)?(\d{4}\.\d{4,5}(?:v\d+)?)"
)
_ARXIV_TIMEOUT = 30.0
_PDF_DIR = Path("tmp/arxiv")


def _parse_arxiv_id(raw: str) -> str | None:
    """Extract a bare arXiv ID from a URL or raw ID string."""
    m = _ARXIV_ID_PATTERN.search(raw)
    return m.group(1) if m else None


@tool(
    "fetch_arxiv",
    (
        "Fetch an arXiv paper's full text. Tries HTML first (fast, searchable); "
        "if unavailable, downloads the PDF and returns the file path for reading.\n\n"
        "Use search_arxiv first to find paper IDs, then fetch_arxiv to read them.\n\n"
        "Optional 'prompt' extracts specific information via Haiku (HTML only).\n\n"
        "Examples:\n"
        "  fetch_arxiv(paper_id='2301.12345') → full paper text\n"
        "  fetch_arxiv(paper_id='2301.12345', prompt='What datasets were used?') → targeted extraction"
    ),
    FetchArxivInput.model_json_schema(),
)
@tracked("fetch_arxiv")
async def fetch_arxiv(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch full arXiv paper content (HTML preferred, PDF fallback)."""
    try:
        validated = FetchArxivInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    paper_id = _parse_arxiv_id(validated.paper_id)
    if not paper_id:
        return mcp_error(
            f"Could not parse arXiv ID from '{validated.paper_id}'. "
            "Expected format: '2301.12345' or 'https://arxiv.org/abs/2301.12345'."
        )

    # Step 1: Try HTML version
    html_url = f"https://arxiv.org/html/{paper_id}"
    async with httpx.AsyncClient(
        timeout=_ARXIV_TIMEOUT, follow_redirects=True
    ) as client:
        try:
            resp = await client.get(html_url)
            if resp.status_code == 200 and "text/html" in resp.headers.get(
                "content-type", ""
            ):
                text = trafilatura.extract(resp.text) or ""
                if len(text) > 500:
                    content = text
                    if validated.prompt:
                        content = await extract_with_prompt(
                            content, validated.prompt, html_url
                        )
                    return mcp_success(
                        {
                            "paper_id": paper_id,
                            "format": "html",
                            "url": html_url,
                            "content": content[:30000],
                        }
                    )
        except httpx.HTTPError:
            logger.debug("HTML fetch failed for %s, trying PDF", paper_id)

        # Step 2: Download PDF
        pdf_url = f"https://arxiv.org/pdf/{paper_id}"
        try:
            resp = await client.get(pdf_url)
            resp.raise_for_status()
        except httpx.HTTPError as e:
            return mcp_error(f"Failed to fetch paper {paper_id}: {e}")

    _PDF_DIR.mkdir(parents=True, exist_ok=True)
    pdf_path = _PDF_DIR / f"{paper_id.replace('/', '_')}.pdf"
    pdf_path.write_bytes(resp.content)

    return mcp_success(
        {
            "paper_id": paper_id,
            "format": "pdf",
            "url": pdf_url,
            "pdf_path": str(pdf_path.resolve()),
            "hint": (
                f"PDF downloaded to {pdf_path.resolve()}. "
                "Use the Read tool to read the PDF content."
            ),
        }
    )


def create_arxiv_server() -> McpSdkServerConfig:
    """Create MCP server with arXiv tools."""
    return create_mcp_server("arxiv", tools=[search_arxiv, fetch_arxiv])


arxiv_server = create_arxiv_server()
