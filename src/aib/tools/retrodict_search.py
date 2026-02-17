"""Web search and fetch tools for the search MCP server.

Provides web_search and fetch tools backed by SDK WebSearch and a page content
extraction pipeline. Interface matches the built-in WebSearch/WebFetch tools.
"""

import asyncio
import json
import logging
from typing import Any, TypedDict

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    HookCallback,
    HookInput,
    HookJSONOutput,
    HookMatcher,
    ResultMessage,
    tool,
)
from aib.tools.extract import extract_with_prompt
from claude_agent_sdk.types import HookContext
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import (
    WaybackRateLimitError,
    check_wayback_availability,
    fetch_wayback_content,
)

logger = logging.getLogger(__name__)


def _make_tool_filter_hook(allowed: frozenset[str]) -> HookCallback:
    """Create a PreToolUse hook that only allows the specified tools.

    Needed because bypassPermissions ignores allowed_tools.
    """

    async def hook(
        input_data: HookInput,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> HookJSONOutput:
        raw: dict[str, Any] = dict(input_data)
        if raw.get("hook_event_name") != "PreToolUse":
            return {}
        tool_name = str(raw.get("tool_name", ""))
        decision = "allow" if tool_name in allowed else "deny"
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
            }
        }

    return hook


class WebSearchInput(BaseModel):
    """Input for web search (matches WebSearch interface)."""

    query: str = Field(min_length=1, description="Search query")
    allowed_domains: list[str] | None = Field(
        default=None, description="Only include results from these domains"
    )
    blocked_domains: list[str] | None = Field(
        default=None, description="Never include results from these domains"
    )


class FetchInput(BaseModel):
    """Input for page fetch (matches WebFetch interface)."""

    url: str = Field(min_length=1, description="The URL to fetch content from")
    prompt: str = Field(
        default="",
        description="What information to extract from the page",
    )


class SearchResult(TypedDict):
    """A search result."""

    title: str
    url: str
    snippet: str | None


class _SearchResultItem(BaseModel):
    title: str
    url: str
    snippet: str


class _SearchResultsOutput(BaseModel):
    results: list[_SearchResultItem]


async def _wayback_filter_results(
    results: list[SearchResult],
    cutoff_date: str,
) -> list[SearchResult]:
    """Validate search results via Wayback Machine and replace snippets.

    Drops results without a pre-cutoff Wayback snapshot. Replaces snippets
    with Wayback-extracted content to prevent future data leaks.

    Args:
        results: Search results to validate.
        cutoff_date: YYYY-MM-DD cutoff date.

    Returns:
        Filtered results with Wayback-derived snippets.
    """
    wayback_ts = cutoff_date.replace("-", "")
    tasks = [fetch_wayback_content(r["url"], wayback_ts) for r in results]
    contents = await asyncio.gather(*tasks)

    validated: list[SearchResult] = []
    for result, content in zip(results, contents):
        if content is None:
            logger.warning(
                "Wayback validate: dropping %s (no pre-cutoff snapshot)",
                result.get("url", "?"),
            )
            continue
        result["snippet"] = content[:500]
        validated.append(result)

    logger.info(
        "[Retrodict] Wayback validated %d/%d search results",
        len(validated),
        len(results),
    )

    return validated


async def _raw_web_search(
    search_query: str,
    cutoff_date: str,
    allowed_domains: list[str] | None = None,
    blocked_domains: list[str] | None = None,
) -> list[SearchResult]:
    """One-shot web search via a minimal Haiku sub-agent with WebSearch.

    Returns raw results without Wayback validation.
    """
    constraints: list[str] = [
        f"Focus on information published before {cutoff_date}. "
        "Include date context in your search query."
    ]
    if allowed_domains:
        constraints.append(
            f"Pass allowed_domains={json.dumps(allowed_domains)} to WebSearch."
        )
    elif blocked_domains:
        constraints.append(
            f"Pass blocked_domains={json.dumps(blocked_domains)} to WebSearch."
        )

    constraint_text = "\n\nConstraints:\n" + "\n".join(f"- {c}" for c in constraints)

    prompt = (
        f"Search the web for: {search_query}{constraint_text}\n\n"
        "Return the search results."
    )

    options = ClaudeAgentOptions(
        model="haiku",
        permission_mode="bypassPermissions",
        allowed_tools=["WebSearch"],
        hooks={
            "PreToolUse": [
                HookMatcher(
                    hooks=[
                        _make_tool_filter_hook(
                            frozenset({"WebSearch", "StructuredOutput"})
                        )
                    ]
                )
            ],
        },
        system_prompt=(
            "You are a web search assistant. Use WebSearch to find information, "
            "then return the results with title, url, and snippet for each."
        ),
        output_format={
            "type": "json_schema",
            "schema": _SearchResultsOutput.model_json_schema(),
        },
        extra_args={"no-session-persistence": None},
    )

    data: dict[str, Any] | None = None
    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, ResultMessage):
                logger.debug(
                    "[WebSearch] sub-agent result: subtype=%s turns=%d is_error=%s",
                    message.subtype,
                    message.num_turns,
                    message.is_error,
                )
                if data is None:
                    if message.structured_output:
                        data = message.structured_output
                    elif message.result:
                        data = json.loads(message.result)

    if not data or not isinstance(data.get("results"), list):
        logger.warning(
            "[WebSearch] sub-agent returned no structured results for query=%s",
            search_query,
        )
        return []

    return [
        SearchResult(
            title=item.get("title", ""),
            url=item["url"],
            snippet=item.get("snippet"),
        )
        for item in data["results"]
        if isinstance(item, dict) and item.get("url")
    ]


@tool(
    "web_search",
    (
        "Search the web for information. Returns titles, URLs, and snippets. "
        "Supports allowed_domains/blocked_domains for domain filtering."
    ),
    WebSearchInput.model_json_schema(),
)
@tracked("web_search")
async def web_search(args: dict[str, Any]) -> dict[str, Any]:
    """Perform web search via SDK sub-agent with optional Wayback validation.

    In retrodict mode, validates results via Wayback Machine to ensure
    only pre-cutoff content is returned.
    """
    try:
        validated = WebSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    if validated.allowed_domains and validated.blocked_domains:
        return mcp_error("Cannot use both allowed_domains and blocked_domains.")

    cutoff = retrodict_cutoff.get()
    assert cutoff is not None, "web_search requires retrodict mode"
    cutoff_date = cutoff.isoformat()

    try:
        logger.info(
            "[WebSearch] query=%s cutoff=%s domains=%s",
            validated.query,
            cutoff_date,
            validated.allowed_domains or validated.blocked_domains,
        )

        results = await _raw_web_search(
            validated.query,
            cutoff_date,
            validated.allowed_domains,
            validated.blocked_domains,
        )
        results = await _wayback_filter_results(results, cutoff_date)

        logger.info("[WebSearch] Returning %d results", len(results))
        return mcp_success({"query": validated.query, "results": results})

    except BaseException as e:
        cause = e
        if isinstance(e, BaseExceptionGroup):
            cause = e.exceptions[0] if e.exceptions else e
        logger.exception("Web search failed: %s", cause)
        return mcp_error(
            "Web search is temporarily unavailable. "
            "Try again with a different query, or use alternative tools."
        )


@tool(
    "fetch",
    (
        "Fetch and extract content from a URL. "
        "If a prompt is provided, extracts specific information from the page."
    ),
    FetchInput.model_json_schema(),
)
@tracked("fetch")
async def fetch(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch URL content via Wayback Machine for retrodict mode.

    Handles specific failure modes:
    - No archived snapshot: suggests alternatives
    - Rate limiting (429): advises retry
    - Extraction failure: returns raw content
    """
    try:
        validated = FetchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    cutoff = retrodict_cutoff.get()
    if cutoff is None:
        return mcp_error("fetch is not available in this context.")

    wayback_ts = cutoff.strftime("%Y%m%d")

    # Step 1: Check availability (surfaces rate-limit vs no-snapshot)
    try:
        snapshot = await check_wayback_availability(
            validated.url,
            wayback_ts,
            validate_before_cutoff=True,
            raise_on_rate_limit=True,
        )
    except WaybackRateLimitError:
        return mcp_error(
            f"Unable to fetch {validated.url}. The page may be temporarily "
            "unavailable. Try again shortly, or use web_search to find "
            "alternative sources."
        )

    if snapshot is None:
        return mcp_error(
            f"Unable to access content at {validated.url}. "
            "The page may not be available. "
            "Try web_search to find alternative sources with the same information, "
            "or try a different URL for this content."
        )

    # Step 2: Fetch the content
    try:
        content = await fetch_wayback_content(validated.url, wayback_ts)
    except WaybackRateLimitError:
        return mcp_error(
            f"Unable to fetch {validated.url}. The page may be temporarily "
            "unavailable. Try again shortly."
        )

    if content is None:
        return mcp_error(
            f"Content extraction failed for {validated.url}. "
            "The page may be a PDF, image, or JavaScript-rendered content. "
            "Try web_search to find alternative sources."
        )

    # Step 3: If prompt provided, use LLM to extract relevant information
    if validated.prompt:
        try:
            extracted = await extract_with_prompt(
                content, validated.prompt, validated.url
            )
            return mcp_success(
                {
                    "url": validated.url,
                    "content": extracted,
                }
            )
        except Exception as e:
            logger.warning("Prompt extraction failed for %s: %s", validated.url, e)
            # Fall through to return raw content

    return mcp_success({"url": validated.url, "content": content[:10000]})


def create_retrodict_search_server() -> Any:
    """Create MCP server with web search and fetch tools."""
    return create_mcp_server(
        "search",
        tools=[web_search, fetch],
    )
