"""Web search with Wayback validation for retrodict mode.

This module provides a web search tool that:
1. Uses the Claude Agent SDK to perform a web search (URLs only)
2. Validates each result URL existed before a cutoff date via Wayback Machine
3. Fetches title/snippet from the archived version (not current web)
4. Returns only results that pass temporal validation with historical metadata

The cutoff_date parameter is NOT visible to the agent - it's injected by the
retrodict PreToolUse hook. This keeps the sandboxing invisible to the agent.
"""

import asyncio
import logging
from typing import Any, TypedDict, cast

import httpx
import trafilatura
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    tool,
)
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import check_wayback_availability, rewrite_to_wayback

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


class WebSearchResponse(BaseModel):
    """Structured response from the web search sub-agent."""

    urls: list[str] = Field(default_factory=list, description="List of result URLs")


async def _perform_web_search(search_query: str, num_results: int) -> list[str]:
    """Use Claude Agent SDK to perform a web search, returning URLs only.

    Args:
        search_query: Search query.
        num_results: Number of results to request.

    Returns:
        List of URLs from search results.
    """
    options = ClaudeAgentOptions(
        model="claude-haiku-4-5-20251001",
        allowed_tools=["WebSearch"],
        output_format={
            "type": "json_schema",
            "schema": WebSearchResponse.model_json_schema(),
        },
    )

    prompt = (
        f"Search the web for: {search_query}\n\nReturn up to {num_results} result URLs."
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, ResultMessage) and message.structured_output:
                response = WebSearchResponse.model_validate(message.structured_output)
                return response.urls

    return []


async def _fetch_wayback_metadata(url: str, timestamp: str) -> SearchResult | None:
    """Fetch title and snippet from a Wayback Machine archived page.

    Uses trafilatura to extract structured metadata from the archived HTML.

    Args:
        url: Original URL.
        timestamp: Wayback timestamp (YYYYMMDD).

    Returns:
        SearchResult with title/snippet if successful, None otherwise.
    """
    wayback_url = rewrite_to_wayback(url, timestamp)

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(wayback_url, follow_redirects=True)
            if response.status_code != 200:
                logger.debug(
                    "Wayback fetch failed for %s: %d", url, response.status_code
                )
                return None

            result = trafilatura.bare_extraction(
                response.text, url=wayback_url, with_metadata=True, as_dict=True
            )
            if not result:
                logger.debug("trafilatura extraction failed for %s", url)
                return None

            doc = cast(dict[str, Any], result)
            title = doc.get("title") or url
            snippet = doc.get("description")
            if not snippet and doc.get("text"):
                snippet = doc["text"][:200]

            return SearchResult(title=title, url=url, snippet=snippet)

    except Exception as e:
        logger.debug("Failed to fetch Wayback metadata for %s: %s", url, e)
        return None


async def _validate_and_fetch_results(
    urls: list[str], cutoff_timestamp: str
) -> list[SearchResult]:
    """Validate URLs via Wayback and fetch metadata from archived pages.

    Args:
        urls: List of URLs to validate.
        cutoff_timestamp: Wayback timestamp format (YYYYMMDD).

    Returns:
        List of validated results with metadata from Wayback.
    """
    validated: list[SearchResult] = []

    async def check_and_fetch(url: str) -> SearchResult | None:
        if not url:
            return None

        availability = await check_wayback_availability(url, cutoff_timestamp)
        if not availability:
            return None

        actual_timestamp = availability.get("timestamp", cutoff_timestamp)
        return await _fetch_wayback_metadata(url, actual_timestamp)

    tasks = [check_and_fetch(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, dict):
            validated.append(result)
        elif isinstance(result, Exception):
            logger.warning("Wayback check/fetch failed: %s", result)

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
    results via Wayback Machine and fetches metadata from archived pages.
    Otherwise, returns results directly from web search.
    """
    try:
        validated_input = WebSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    search_query = validated_input.query
    num_results = validated_input.num_results
    cutoff_date = validated_input.cutoff_date

    try:
        # Perform web search via Agent SDK (returns URLs only)
        logger.info("[WebSearch] Searching for: %s", search_query)
        search_urls = await _perform_web_search(search_query, num_results * 2)
        logger.info("[WebSearch] Got %d URLs from search", len(search_urls))

        if not search_urls:
            return mcp_success({"query": search_query, "results": []})

        # If cutoff_date is provided, validate via Wayback and fetch metadata
        if cutoff_date:
            cutoff_timestamp = cutoff_date.replace("-", "")
            validated_results = await _validate_and_fetch_results(
                search_urls, cutoff_timestamp
            )
            logger.info(
                "[WebSearch] %d/%d URLs passed validation",
                len(validated_results),
                len(search_urls),
            )
            results = validated_results[:num_results]
        else:
            # No cutoff - return URLs only (normal mode would need different handling)
            # For now, just return URLs as results without metadata
            results = [
                SearchResult(title=url, url=url, snippet=None)
                for url in search_urls[:num_results]
            ]

        return mcp_success({"query": search_query, "results": results})

    except asyncio.CancelledError:
        logger.warning("Web search cancelled for query: %s", search_query)
        return mcp_error("Search was cancelled (timeout or parent context cancelled)")
    except Exception as e:
        logger.exception("Web search failed")
        return mcp_error(f"Search failed: {e}")


def create_retrodict_search_server():
    """Create MCP server with web search tool."""
    return create_mcp_server(
        "search",
        tools=[web_search],
    )
