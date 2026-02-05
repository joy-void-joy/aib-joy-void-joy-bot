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
import re
from typing import Any, TypedDict

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    TextBlock,
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


def _parse_search_results(response_text: str) -> list[dict[str, Any]]:
    """Parse search results from agent response.

    Args:
        response_text: The agent's response text containing search results.

    Returns:
        List of dicts with 'url', 'title', and 'snippet' keys.
    """
    results: list[dict[str, Any]] = []

    # Look for markdown links: [title](url)
    link_pattern = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")
    for match in link_pattern.finditer(response_text):
        title = match.group(1)
        url = match.group(2)
        end_pos = match.end()
        snippet_match = re.search(
            r"[:\-\s]+(.{20,200}?)(?:\n|$)", response_text[end_pos : end_pos + 300]
        )
        snippet = snippet_match.group(1).strip() if snippet_match else None

        results.append({
            "title": title,
            "url": url,
            "snippet": snippet,
        })

    # Also look for bare URLs
    url_pattern = re.compile(r"(?<!\()(https?://[^\s\)]+)(?!\))")
    seen_urls = {r["url"] for r in results}
    for match in url_pattern.finditer(response_text):
        url = match.group(1)
        if url not in seen_urls:
            results.append({
                "title": url,
                "url": url,
                "snippet": None,
            })
            seen_urls.add(url)

    return results


async def _perform_web_search(search_query: str, num_results: int) -> str:
    """Use Claude Agent SDK to perform a web search.

    Args:
        search_query: Search query.
        num_results: Number of results to request.

    Returns:
        The agent's response text containing search results.
    """
    options = ClaudeAgentOptions(
        model="claude-sonnet-4-20250514",
        allowed_tools=["WebSearch"],
    )

    result_text = ""
    async for message in query(
        prompt=(
            f"Search the web for: {search_query}\n\n"
            f"Return up to {num_results} relevant results. "
            "For each result, provide the title, URL, and a brief snippet. "
            "Format as a list with markdown links."
        ),
        options=options,
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    result_text += block.text

    return result_text


async def _validate_results_via_wayback(
    results: list[dict[str, Any]], cutoff_timestamp: str
) -> list[SearchResult]:
    """Validate search results by checking Wayback availability.

    Args:
        results: List of search results to validate.
        cutoff_timestamp: Wayback timestamp format (YYYYMMDD).

    Returns:
        List of validated results.
    """
    validated: list[SearchResult] = []

    async def check_one(result: dict[str, Any]) -> SearchResult | None:
        url = result.get("url", "")
        if not url:
            return None

        availability = await check_wayback_availability(url, cutoff_timestamp)
        if availability:
            return SearchResult(
                title=result.get("title", url),
                url=url,
                snippet=result.get("snippet"),
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
    (
        "Search the web for information. Returns titles, URLs, and snippets."
    ),
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
        # Perform web search via Agent SDK
        logger.info("[WebSearch] Searching for: %s", search_query)
        search_response = await _perform_web_search(search_query, num_results * 2)

        # Parse results from response
        parsed_results = _parse_search_results(search_response)
        logger.info(
            "[WebSearch] Parsed %d results from search", len(parsed_results)
        )

        if not parsed_results:
            return mcp_success({
                "query": search_query,
                "results": [],
            })

        # If cutoff_date is provided, validate via Wayback
        if cutoff_date:
            cutoff_timestamp = cutoff_date.replace("-", "")
            validated_results = await _validate_results_via_wayback(
                parsed_results, cutoff_timestamp
            )
            logger.info(
                "[WebSearch] %d/%d results passed validation",
                len(validated_results),
                len(parsed_results),
            )
            results = validated_results[:num_results]
        else:
            # No cutoff - return all results (normal mode)
            results = [
                SearchResult(
                    title=r.get("title", r.get("url", "")),
                    url=r.get("url", ""),
                    snippet=r.get("snippet"),
                )
                for r in parsed_results[:num_results]
            ]

        return mcp_success({
            "query": search_query,
            "results": results,
        })

    except Exception as e:
        logger.exception("Web search failed")
        return mcp_error(f"Search failed: {e}")


def create_retrodict_search_server():
    """Create MCP server with web search tool."""
    return create_mcp_server(
        "search",
        tools=[web_search],
    )
