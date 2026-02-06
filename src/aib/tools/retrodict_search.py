"""Web search for retrodict mode using Exa with date filtering.

This module provides a web search tool that uses Exa's publishedBefore filter
to return only results published before the cutoff date. This prevents
"future leak" where the agent finds information about events that haven't
happened yet from its perspective.

The cutoff_date parameter is NOT visible to the agent - it's injected by the
retrodict PreToolUse hook. This keeps the sandboxing invisible to the agent.
"""

import logging
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.config import settings
from aib.tools.exa import exa_search
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


class WebSearchInput(BaseModel):
    """Input for web search.

    Note: cutoff_date is injected by the retrodict hook, not visible to agent.
    """

    query: str = Field(min_length=1, description="Search query")
    num_results: int = Field(default=10, ge=1, le=20, description="Number of results")
    # Hidden from agent - injected by retrodict hook
    cutoff_date: str | None = Field(
        default=None,
        description="Internal: cutoff date injected by retrodict hook.",
    )


class SearchResult(TypedDict):
    """A search result."""

    title: str
    url: str
    snippet: str | None


@tool(
    "web_search",
    "Search the web for information. Returns titles, URLs, and snippets.",
    # cutoff_date is injected by retrodict hook, but must be in schema
    # to avoid being stripped by SDK/MCP validation
    {"query": str, "num_results": int, "cutoff_date": str},
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
    cutoff_date = validated_input.cutoff_date

    # Check if Exa is available
    if not settings.exa_api_key:
        return mcp_error(
            "Web search unavailable: EXA_API_KEY not configured. "
            "Use search_arxiv for academic papers or wikipedia for encyclopedic content."
        )

    try:
        logger.info("[WebSearch] Searching for: %s (cutoff: %s)", search_query, cutoff_date)

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


def create_retrodict_search_server():
    """Create MCP server with web search tool."""
    return create_mcp_server(
        "search",
        tools=[web_search],
    )
