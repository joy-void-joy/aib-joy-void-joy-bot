"""arXiv paper search tool.

Provides access to academic papers from arXiv.org with reliable publication
dates. Useful for retrodict mode where date filtering is important.

Uses the arxiv Python library: https://pypi.org/project/arxiv/
"""

import logging
from datetime import datetime
from typing import Any

import arxiv
from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


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
        "Search arXiv for academic papers. Returns paper titles, abstracts, authors, "
        "and publication dates. Useful for scientific and technical research where "
        "publication dates are important. Supports arXiv query syntax: "
        "au:lastname (author), ti:word (title), cat:category (e.g., cs.AI). "
        "Results sorted by relevance. Max 50 results."
    ),
    {"query": str, "max_results": int, "cutoff_date": str},
)
@tracked("search_arxiv")
async def search_arxiv(args: dict[str, Any]) -> dict[str, Any]:
    """Search arXiv for academic papers."""
    try:
        validated = SearchArxivInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    cutoff: datetime | None = None
    if validated.cutoff_date:
        cutoff = datetime.strptime(validated.cutoff_date, "%Y-%m-%d")

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


def create_arxiv_server():
    """Create MCP server with arXiv tool."""
    return create_mcp_server("arxiv", tools=[search_arxiv])


arxiv_server = create_arxiv_server()
