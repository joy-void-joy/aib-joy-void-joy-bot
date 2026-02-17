"""Unified web search with API augmentation.

Wraps Claude's built-in WebSearch via a Haiku sub-agent. For search results
whose URLs match known data sources (Yahoo Finance, arXiv, FRED, Polymarket,
etc.), automatically fetches structured API data in parallel.

In retrodict mode, API-augmented results are trusted (handlers validate cutoff
internally). Non-API results are validated via Wayback Machine.
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
from claude_agent_sdk.types import HookContext
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import fetch_wayback_content

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


class SearchResult(TypedDict):
    """A raw search result from the sub-agent."""

    title: str
    url: str
    snippet: str | None


class AugmentedSearchResult(TypedDict):
    """A search result with optional structured API data."""

    title: str
    url: str
    snippet: str | None
    api_data: dict[str, Any] | None
    hint: str | None


class _SearchResultItem(BaseModel):
    title: str
    url: str
    snippet: str


class _SearchResultsOutput(BaseModel):
    results: list[_SearchResultItem]


async def _wayback_filter_non_api_results(
    results: list[AugmentedSearchResult],
    cutoff_date: str,
) -> list[AugmentedSearchResult]:
    """Wayback-validate only non-API-augmented search results.

    API-augmented results are kept as-is (handlers validate cutoff internally
    via retrodict_cutoff ContextVar). Non-API results get full Wayback
    validation: dropped if no pre-cutoff snapshot, snippets replaced with
    Wayback-extracted content to prevent future data leaks.
    """
    wayback_ts = cutoff_date.replace("-", "")

    async def _validate_one(
        result: AugmentedSearchResult,
    ) -> AugmentedSearchResult | None:
        if result["api_data"] is not None:
            return result

        content = await fetch_wayback_content(result["url"], wayback_ts)
        if content is None:
            logger.warning(
                "Wayback: dropping %s (no pre-cutoff snapshot)", result["url"],
            )
            return None
        result["snippet"] = content[:500]
        return result

    validated_or_none = await asyncio.gather(
        *[_validate_one(r) for r in results],
    )
    validated = [r for r in validated_or_none if r is not None]

    logger.info(
        "[Retrodict] Wayback validated %d/%d non-API results",
        len(validated),
        len(results),
    )
    return validated


async def _raw_web_search(
    search_query: str,
    cutoff_date: str | None = None,
    allowed_domains: list[str] | None = None,
    blocked_domains: list[str] | None = None,
) -> list[SearchResult]:
    """One-shot web search via a minimal Haiku sub-agent with WebSearch.

    Returns raw results without Wayback validation or API augmentation.
    """
    constraints: list[str] = []
    if cutoff_date:
        constraints.append(
            f"Focus on information published before {cutoff_date}. "
            "Include date context in your search query."
        )
    if allowed_domains:
        constraints.append(
            f"Pass allowed_domains={json.dumps(allowed_domains)} to WebSearch."
        )
    elif blocked_domains:
        constraints.append(
            f"Pass blocked_domains={json.dumps(blocked_domains)} to WebSearch."
        )

    constraint_text = ""
    if constraints:
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


async def _augment_with_api_data(
    results: list[SearchResult],
) -> list[AugmentedSearchResult]:
    """Augment search results with structured API data from recognized domains.

    For each result URL, checks against domain routes (fetch_routes.py).
    Matching URLs have their specialized tool handler called in parallel.
    SUGGEST_ONLY domains get a hint string instead.
    """
    from aib.tools.fetch_routes import SUGGEST_ONLY, get_routes

    routes = get_routes()

    async def _augment_one(result: SearchResult) -> AugmentedSearchResult:
        url = result["url"]
        augmented = AugmentedSearchResult(
            title=result["title"],
            url=url,
            snippet=result["snippet"],
            api_data=None,
            hint=None,
        )

        for domain, hint in SUGGEST_ONLY.items():
            if domain in url.lower():
                augmented["hint"] = hint
                return augmented

        for route in routes:
            match = route.pattern.search(url)
            if match:
                params = route.param_builder(match)
                try:
                    api_result = await route.handler(params)
                    if not api_result.get("is_error"):
                        augmented["api_data"] = api_result
                except Exception as e:
                    logger.warning("API augmentation failed for %s: %s", url, e)
                return augmented

        return augmented

    augmented = await asyncio.gather(*[_augment_one(r) for r in results])
    return list(augmented)


@tool(
    "web_search",
    (
        "Search the web for information. Returns titles, URLs, and snippets. "
        "When results match known data sources (stock quotes, arXiv, Wikipedia, "
        "FRED, prediction markets), automatically includes structured API data. "
        "Supports allowed_domains/blocked_domains for domain filtering. "
        "Prefer this over WebSearch."
    ),
    WebSearchInput.model_json_schema(),
)
@tracked("web_search")
async def web_search(args: dict[str, Any]) -> dict[str, Any]:
    """Perform web search via SDK sub-agent with API augmentation.

    Augments all results first, then in retrodict mode applies Wayback
    validation only to results that lack API data (API-augmented results
    are safe since specialized handlers manage time-appropriateness).
    """
    try:
        validated = WebSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    if validated.allowed_domains and validated.blocked_domains:
        return mcp_error("Cannot use both allowed_domains and blocked_domains.")

    cutoff = retrodict_cutoff.get()
    cutoff_date = cutoff.isoformat() if cutoff else None

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

        augmented = await _augment_with_api_data(results)

        if cutoff_date:
            augmented = await _wayback_filter_non_api_results(
                augmented, cutoff_date,
            )

        logger.info("[WebSearch] Returning %d results", len(augmented))
        return mcp_success({"query": validated.query, "results": augmented})

    except BaseException as e:
        cause = e
        if isinstance(e, BaseExceptionGroup):
            cause = e.exceptions[0] if e.exceptions else e
        logger.exception("Web search failed: %s", cause)
        return mcp_error(
            "Web search is temporarily unavailable. "
            "Try again with a different query, or use alternative tools."
        )


def create_search_server() -> Any:
    """Create MCP server with web search tool."""
    return create_mcp_server(
        "search",
        tools=[web_search],
    )
