"""Web search for retrodict mode using Exa with date filtering.

This module provides a web search tool that uses Exa's publishedBefore filter
to return only results published before the cutoff date. This prevents
"future leak" where the agent finds information about events that haven't
happened yet from its perspective.

The cutoff date is read from the retrodict_cutoff ContextVar, keeping
the sandboxing invisible to the agent.
"""

import logging
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.config import settings
from aib.tools.exa import exa_search
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import fetch_wayback_content

logger = logging.getLogger(__name__)


class WebSearchInput(BaseModel):
    """Input for web search."""

    query: str = Field(min_length=1, description="Search query")
    num_results: int = Field(default=10, ge=1, le=20, description="Number of results")


class FetchInput(BaseModel):
    """Input for page fetch."""

    url: str = Field(min_length=1, description="URL to fetch content from")
    prompt: str = Field(default="", description="What information to extract")


class SearchResult(TypedDict):
    """A search result."""

    title: str
    url: str
    snippet: str | None


@tool(
    "web_search",
    "Search the web for information. Returns titles, URLs, and snippets.",
    {"query": str, "num_results": int},
)
@tracked("web_search")
async def web_search(args: dict[str, Any]) -> dict[str, Any]:
    """Perform web search with date filtering via Exa.

    If cutoff_date is provided (injected by retrodict hook), uses Exa's
    publishedBefore filter to only return results from before that date.
    """
    try:
        validated_input = WebSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    search_query = validated_input.query
    num_results = validated_input.num_results
    cutoff = retrodict_cutoff.get()
    cutoff_date = cutoff.isoformat() if cutoff is not None else None

    # Check if Exa is available
    if not settings.exa_api_key:
        return mcp_error(
            "Web search unavailable: EXA_API_KEY not configured. "
            "Use search_arxiv for academic papers or wikipedia for encyclopedic content."
        )

    try:
        logger.info(
            "[WebSearch] Searching for: %s (cutoff: %s)", search_query, cutoff_date
        )

        # Use Exa with publishedBefore filter and livecrawl=never for retrodict
        exa_results = await exa_search(
            query=search_query,
            num_results=num_results,
            published_before=cutoff_date,
            livecrawl="never" if cutoff_date else "always",
        )

        logger.info("[WebSearch] Got %d results from Exa", len(exa_results))

        # Convert to SearchResult format
        results: list[SearchResult] = []
        for r in exa_results:
            results.append(
                SearchResult(
                    title=r.get("title") or r.get("url") or "",
                    url=r.get("url") or "",
                    snippet=r.get("snippet"),
                )
            )

        return mcp_success({"query": search_query, "results": results})

    except Exception as e:
        logger.exception("Web search failed")
        return mcp_error(f"Search failed: {e}")


@tool(
    "fetch",
    "Fetch and extract text content from a URL. Returns clean text from the page.",
    {"url": str, "prompt": str},
)
@tracked("fetch")
async def fetch(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch URL content via Wayback Machine for retrodict mode."""
    try:
        validated_input = FetchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    cutoff = retrodict_cutoff.get()
    if cutoff is None:
        return mcp_error("fetch is only available in retrodict mode")

    wayback_ts = cutoff.strftime("%Y%m%d")

    try:
        content = await fetch_wayback_content(validated_input.url, wayback_ts)
        if content is None:
            return mcp_error("No archived version available for this URL.")

        return mcp_success({"url": validated_input.url, "content": content})
    except Exception as e:
        logger.exception("Fetch failed for %s", validated_input.url)
        return mcp_error(f"Fetch failed: {e}")


def create_retrodict_search_server():
    """Create MCP server with web search and fetch tools."""
    return create_mcp_server(
        "search",
        tools=[web_search, fetch],
    )
