"""Web search with Wayback validation for retrodict mode.

This module provides a web search tool that:
1. Uses the Claude Agent SDK to perform a web search
2. Validates each result URL existed before a cutoff date via Wayback Machine
3. Returns only results that pass temporal validation

The cutoff_date parameter is NOT visible to the agent - it's injected by the
retrodict PreToolUse hook. This keeps the sandboxing invisible to the agent.
"""

import asyncio
import logging
from typing import Any, TypedDict

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ResultMessage,
    query,
    tool,
)
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import check_wayback_availability

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


class SearchResultItem(BaseModel):
    """A single search result from the sub-agent."""

    title: str = Field(description="Title of the search result")
    url: str = Field(description="URL of the search result")
    snippet: str | None = Field(default=None, description="Brief snippet from the page")


class WebSearchResponse(BaseModel):
    """Structured response from the web search sub-agent."""

    results: list[SearchResultItem] = Field(
        default_factory=list, description="List of search results"
    )


async def _perform_web_search(
    search_query: str, num_results: int
) -> list[SearchResultItem]:
    """Use Claude Agent SDK to perform a web search with structured output.

    Args:
        search_query: Search query.
        num_results: Number of results to request.

    Returns:
        List of search result items.
    """
    options = ClaudeAgentOptions(
        model="claude-sonnet-4-20250514",
        allowed_tools=["WebSearch"],
        output_format={
            "type": "json_schema",
            "schema": WebSearchResponse.model_json_schema(),
        },
    )

    async for message in query(
        prompt=(
            f"Search the web for: {search_query}\n\n"
            f"Return up to {num_results} relevant results with title, URL, and snippet."
        ),
        options=options,
    ):
        if isinstance(message, ResultMessage) and message.structured_output:
            response = WebSearchResponse.model_validate(message.structured_output)
            return response.results

    logger.warning("No structured output received from web search")
    return []


async def _validate_results_via_wayback(
    results: list[SearchResultItem], cutoff_timestamp: str
) -> list[SearchResult]:
    """Validate search results by checking Wayback availability.

    Args:
        results: List of search results to validate.
        cutoff_timestamp: Wayback timestamp format (YYYYMMDD).

    Returns:
        List of validated results.
    """
    validated: list[SearchResult] = []

    async def check_one(result: SearchResultItem) -> SearchResult | None:
        if not result.url:
            return None

        availability = await check_wayback_availability(result.url, cutoff_timestamp)
        if availability:
            return SearchResult(
                title=result.title or result.url,
                url=result.url,
                snippet=result.snippet,
            )
        return None

    tasks = [check_one(r) for r in results]
    check_results = await asyncio.gather(*tasks, return_exceptions=True)

    for check_result in check_results:
        if isinstance(check_result, dict):
            validated.append(check_result)
        elif isinstance(check_result, Exception):
            logger.warning("Wayback check failed: %s", check_result)

    return validated


@tool(
    "web_search",
    ("Search the web for information. Returns titles, URLs, and snippets."),
    # cutoff_date is injected by retrodict hook, but must be in schema
    # to avoid being stripped by SDK/MCP validation
    {"query": str, "num_results": int, "cutoff_date": str},
)
@tracked("web_search")
async def web_search(args: dict[str, Any]) -> dict[str, Any]:
    """Perform web search with optional temporal validation.

    If cutoff_date is provided (injected by retrodict hook), validates
    results via Wayback Machine. Otherwise, returns results directly.
    """
    try:
        validated_input = WebSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    search_query = validated_input.query
    num_results = validated_input.num_results
    cutoff_date = validated_input.cutoff_date

    try:
        # Perform web search via Agent SDK (returns structured results)
        logger.info("[WebSearch] Searching for: %s", search_query)
        search_results = await _perform_web_search(search_query, num_results * 2)
        logger.info("[WebSearch] Got %d results from search", len(search_results))

        if not search_results:
            return mcp_success(
                {
                    "query": search_query,
                    "results": [],
                }
            )

        # If cutoff_date is provided, validate via Wayback
        if cutoff_date:
            cutoff_timestamp = cutoff_date.replace("-", "")
            validated_results = await _validate_results_via_wayback(
                search_results, cutoff_timestamp
            )
            logger.info(
                "[WebSearch] %d/%d results passed validation",
                len(validated_results),
                len(search_results),
            )
            results = validated_results[:num_results]
        else:
            # No cutoff - return all results (normal mode)
            results = [
                SearchResult(
                    title=r.title or r.url,
                    url=r.url,
                    snippet=r.snippet,
                )
                for r in search_results[:num_results]
            ]

        return mcp_success(
            {
                "query": search_query,
                "results": results,
            }
        )

    except Exception as e:
        logger.exception("Web search failed")
        return mcp_error(f"Search failed: {e}")


def create_retrodict_search_server():
    """Create MCP server with web search tool."""
    return create_mcp_server(
        "search",
        tools=[web_search],
    )
