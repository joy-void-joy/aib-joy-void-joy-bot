"""Unified search and content retrieval tools.

Provides web search (via Haiku sub-agent + API augmentation), Exa AI search,
AskNews search, Wikipedia, and URL content fetching. All "find/retrieve
information" tools live here.

In retrodict mode, API-augmented results are trusted (handlers validate cutoff
internally). Non-API results are validated via Wayback Machine.
"""

import asyncio
import json
import logging
from typing import Any, Literal, TypedDict

import httpx
from asknews_sdk.dto.news import SearchResponseDictItem
from asknews_sdk.errors import RateLimitExceededError as AskNewsRateLimitError
from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    HookCallback,
    HookInput,
    HookJSONOutput,
    HookMatcher,
    ResultMessage,
    SdkMcpTool,
    tool,
)
from claude_agent_sdk.types import HookContext
from pydantic import BaseModel, Field

from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.arxiv_search import fetch_arxiv, search_arxiv
from aib.tools.exa import exa_search
from aib.tools.extract import extract_with_prompt
from aib.tools.fetch_http import fetch_live
from aib.tools.fetch_routes import SUGGEST_ONLY, domain_dispatch
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry
from aib.tools.throttle import asknews_throttle, exa_throttle, wikipedia_throttle
from aib.tools.wayback import (
    WaybackRateLimitError,
    check_wayback_availability,
    fetch_wayback_content,
)
from aib.tools.wikipedia import (
    WIKIPEDIA_API_URL,
    WIKIPEDIA_HEADERS,
    extract_intro as _extract_intro,
    fetch_wikipedia_historical as _fetch_wikipedia_historical_content,
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
                "Wayback: dropping %s (no pre-cutoff snapshot)",
                result["url"],
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
        constraint_text = "\n\nConstraints:\n" + "\n".join(
            f"- {c}" for c in constraints
        )

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
                augmented,
                cutoff_date,
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


# --- Exa Search Tool ---


class SearchExaInput(BaseModel):
    query: str
    num_results: int = settings.search_default_limit
    published_before: str | None = Field(
        default=None,
        description="ISO date (YYYY-MM-DD) to filter results published before this date.",
    )
    livecrawl: str = Field(
        default="always",
        description="Livecrawl mode: 'always', 'fallback', or 'never'.",
    )


@tool(
    "search_exa",
    (
        "Search the web using Exa AI-powered search. Returns raw results with titles, URLs, and snippets. "
        f"Results are cached for 5 minutes. Optional num_results (default: {settings.search_default_limit}).\n\n"
        "Examples:\n"
        '  search_exa(query="EU AI Act implementation timeline 2026")\n'
        '  search_exa(query="MSFT earnings Q1 2026 results", num_results=10)\n'
        '  search_exa(query="Germany coalition government formation", published_before="2026-01-15")\n'
        "Use diverse query formulations — the same topic found with different keywords produces richer results."
    ),
    SearchExaInput.model_json_schema(),
)
@tracked("search_exa")
async def search_exa(args: dict[str, Any]) -> dict[str, Any]:
    """Search using Exa and return raw results (cached)."""
    try:
        validated = SearchExaInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    num_results = validated.num_results
    cutoff = retrodict_cutoff.get()
    published_before = (
        cutoff.isoformat() if cutoff is not None else validated.published_before
    )
    livecrawl = "never" if cutoff is not None else validated.livecrawl

    logger.info(
        "search_exa actual params: published_before=%s, livecrawl=%s",
        published_before,
        livecrawl,
    )

    try:
        async with exa_throttle:
            formatted = await exa_search(
                query, num_results, published_before, livecrawl
            )
        return mcp_success(formatted)
    except Exception as e:
        logger.exception("Exa search failed")
        return mcp_error(f"Search failed: {e}")


# --- News Search Tool ---


class SearchNewsInput(BaseModel):
    query: str
    num_results: int = settings.search_default_limit


@tool(
    "search_news",
    (
        "Search for recent news using AskNews API. Returns raw news results with headlines, sources, and summaries. "
        f"Optional num_results (default: {settings.news_default_limit})."
    ),
    SearchNewsInput.model_json_schema(),
)
@tracked("search_news")
async def search_news(args: dict[str, Any]) -> dict[str, Any]:
    """Search news using AskNews SDK and return formatted results."""
    try:
        validated = SearchNewsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    if retrodict_cutoff.get() is not None:
        return mcp_error(
            "search_news is currently unavailable. "
            "Use search_exa or web_search instead."
        )

    query = validated.query
    num_results = validated.num_results

    @with_retry(
        max_attempts=3,
        min_wait=10,
        max_wait=30,
        extra_exceptions=(AskNewsRateLimitError,),
    )
    async def _fetch_news(
        strategy: Literal["latest news", "news knowledge", "default"],
        n_articles: int,
    ) -> list[SearchResponseDictItem]:
        from asknews_sdk import AsyncAskNewsSDK

        api_key = settings.asknews_api_key
        client_id = settings.asknews_client_id
        client_secret = settings.asknews_client_secret

        if api_key:
            ask_ctx = AsyncAskNewsSDK(api_key=api_key, scopes={"news"})
        elif client_id and client_secret:
            ask_ctx = AsyncAskNewsSDK(
                client_id=client_id,
                client_secret=client_secret,
                scopes={"news"},
            )
        else:
            raise ValueError("AskNews credentials not configured")

        async with ask_ctx as ask:
            response = await ask.news.search_news(
                query=query,
                n_articles=n_articles,
                return_type="both",
                strategy=strategy,
            )
        return response.as_dicts or []

    try:
        async with asknews_throttle:
            hot_articles = await _fetch_news("latest news", min(num_results, 6))
        async with asknews_throttle:
            historical_articles = await _fetch_news("news knowledge", num_results)
    except Exception as e:
        logger.exception("News search failed")
        return mcp_error(f"News search failed: {e}")

    seen: set[str] = set()
    all_articles: list[SearchResponseDictItem] = []
    for article in hot_articles + historical_articles:
        aid = str(article.article_id)
        if aid not in seen:
            seen.add(aid)
            all_articles.append(article)

    all_articles.sort(key=lambda a: a.pub_date, reverse=True)

    if not all_articles:
        return mcp_success({"query": query, "results": "No articles were found.\n"})

    formatted = "Here are the relevant news articles:\n\n"
    for article in all_articles:
        pub_date = article.pub_date.strftime("%B %d, %Y %I:%M %p")
        formatted += (
            f"**{article.eng_title}**\n"
            f"{article.summary}\n"
            f"Language: {article.language}\n"
            f"Published: {pub_date}\n"
            f"Source: [{article.source_id}]({article.article_url})\n\n"
        )

    return mcp_success({"query": query, "results": formatted})


# --- Wikipedia Tool ---


class WikipediaInput(BaseModel):
    """Unified Wikipedia tool input."""

    query: str
    mode: Literal["search", "summary", "full"] = "search"
    num_results: int = settings.search_default_limit
    prompt: str | None = Field(
        default=None,
        description="Extract specific information from the article (summary/full modes only).",
    )


@tool(
    "wikipedia",
    (
        "Search Wikipedia or fetch article content. "
        "Modes: 'search' (default) finds articles matching query; "
        "'summary' fetches article intro by exact title; "
        "'full' fetches entire article by exact title. "
        f"For search mode, optional num_results (default: {settings.search_default_limit}).\n\n"
        "Examples:\n"
        '  wikipedia(query="European Central Bank") → search for articles\n'
        '  wikipedia(query="European Central Bank", mode="summary") → get article intro\n'
        '  wikipedia(query="List of recessions in the United States", mode="full") → full article\n'
        '  wikipedia(query="European Central Bank", mode="summary", prompt="What is the current interest rate?") → extract specific info\n'
        "Two-step workflow: search first to find the right article title, then summary/full to read it. "
        "Optional 'prompt' extracts specific information via Haiku (summary/full modes only)."
    ),
    WikipediaInput.model_json_schema(),
)
@tracked("wikipedia")
async def wikipedia(args: dict[str, Any]) -> dict[str, Any]:
    """Unified Wikipedia search and article fetching."""
    try:
        validated = WikipediaInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    mode = validated.mode
    num_results = validated.num_results
    cutoff = retrodict_cutoff.get()
    cutoff_date = cutoff.isoformat() if cutoff is not None else None

    if mode == "search":

        @with_retry(max_attempts=3)
        async def _search() -> list[dict[str, Any]]:
            async with httpx.AsyncClient(
                timeout=settings.http_timeout_seconds,
                headers=WIKIPEDIA_HEADERS,
            ) as client:
                search_response = await client.get(
                    WIKIPEDIA_API_URL,
                    params={
                        "action": "query",
                        "list": "search",
                        "srsearch": query,
                        "srlimit": num_results,
                        "format": "json",
                        "utf8": 1,
                    },
                )
                search_response.raise_for_status()
                search_data = search_response.json()

                results = []
                for item in search_data.get("query", {}).get("search", []):
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")
                    snippet = snippet.replace('<span class="searchmatch">', "")
                    snippet = snippet.replace("</span>", "")

                    results.append(
                        {
                            "title": title,
                            "snippet": snippet,
                            "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                            "word_count": item.get("wordcount", 0),
                        }
                    )

                return results

        try:
            async with wikipedia_throttle:
                results = await _search()

            if cutoff_date and results:
                historical_results = []
                for result in results:
                    try:
                        historical = await _fetch_wikipedia_historical_content(
                            result["title"], cutoff_date
                        )
                        snippet = _extract_intro(historical["extract"])[:500]
                        if len(snippet) == 500:
                            snippet = snippet.rsplit(" ", 1)[0] + "..."
                        historical_results.append(
                            {
                                "title": historical["title"],
                                "snippet": snippet,
                                "url": historical["url"],
                                "revision_timestamp": historical["revision_timestamp"],
                            }
                        )
                    except ValueError as e:
                        logger.debug("Skipping %s: %s", result["title"], e)
                        continue
                if not historical_results and results:
                    return mcp_error(f"No Wikipedia articles found for '{query}'.")
                results = historical_results

            return mcp_success({"query": query, "mode": mode, "results": results})
        except Exception as e:
            logger.exception("Wikipedia search failed")
            return mcp_error(f"Wikipedia search failed: {e}")

    else:
        if cutoff_date:
            try:
                async with wikipedia_throttle:
                    historical = await _fetch_wikipedia_historical_content(
                        query, cutoff_date
                    )
                extract = historical["extract"]
                if mode == "summary":
                    extract = _extract_intro(extract)
                if validated.prompt:
                    extract = await extract_with_prompt(
                        extract, validated.prompt, historical["url"]
                    )
                return mcp_success(
                    {
                        "title": historical["title"],
                        "url": historical["url"],
                        "extract": extract,
                        "mode": mode,
                        "revision_id": historical["revision_id"],
                        "revision_timestamp": historical["revision_timestamp"],
                        "revision_date": historical["revision_timestamp"][:10],
                    }
                )
            except Exception as e:
                logger.exception("Wikipedia historical fetch failed")
                return mcp_error(f"Wikipedia historical fetch failed: {e}")

        @with_retry(max_attempts=3)
        async def _fetch() -> dict[str, Any]:
            async with httpx.AsyncClient(
                timeout=settings.http_timeout_seconds,
                headers=WIKIPEDIA_HEADERS,
            ) as client:
                response = await client.get(
                    WIKIPEDIA_API_URL,
                    params={
                        "action": "query",
                        "titles": query,
                        "prop": "extracts|info",
                        "exintro": mode == "summary",
                        "explaintext": True,
                        "inprop": "url",
                        "redirects": 1,
                        "format": "json",
                        "utf8": 1,
                    },
                )
                response.raise_for_status()
                data = response.json()

                pages = data.get("query", {}).get("pages", {})
                if not pages:
                    raise ValueError(f"Article not found: {query}")

                page_id = next(iter(pages))
                if page_id == "-1":
                    raise ValueError(f"Article not found: {query}")

                page = pages[page_id]
                extract = page.get("extract", "")
                url = page.get(
                    "fullurl",
                    f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}",
                )

                return {
                    "title": page.get("title", query),
                    "url": url,
                    "extract": extract,
                    "mode": mode,
                }

        try:
            async with wikipedia_throttle:
                result = await _fetch()
            if validated.prompt:
                result["extract"] = await extract_with_prompt(
                    result["extract"], validated.prompt, result["url"]
                )
            return mcp_success(result)
        except Exception as e:
            logger.exception("Wikipedia article fetch failed")
            return mcp_error(f"Wikipedia article fetch failed: {e}")


# --- Fetch URL Tool ---

_MAX_CONTENT = 10_000


class FetchUrlInput(BaseModel):
    url: str = Field(min_length=1, description="The URL to fetch content from")
    prompt: str | None = Field(
        default=None,
        description="What information to extract from the page",
    )


@tool(
    "fetch_url",
    (
        "Fetch and extract content from a URL. "
        "Automatically extracts readable text, renders JavaScript pages via Playwright, "
        "and routes known domains to specialized tools "
        "(Yahoo Finance, arXiv, Wikipedia, FRED, Polymarket). "
        "If a prompt is provided, uses an LLM to extract specific information. "
        "Prefer this over WebFetch for URL fetching."
    ),
    FetchUrlInput.model_json_schema(),
)
@tracked("fetch_url")
async def fetch_url(args: dict[str, Any]) -> dict[str, Any]:
    """Unified fetch: domain dispatch → http/wayback → trafilatura → playwright → prompt."""
    try:
        inp = FetchUrlInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    url, prompt = inp.url, inp.prompt

    for domain_key, hint in SUGGEST_ONLY.items():
        if domain_key in url.lower():
            return mcp_error(f"fetch_url is not optimal for this domain. {hint}")

    dispatched = await domain_dispatch(url)
    if dispatched is not None:
        return dispatched

    if retrodict_cutoff.get() is not None:
        content = await _fetch_retrodict(url)
    else:
        content = await fetch_live(url)

    if isinstance(content, dict):
        return content

    if prompt:
        try:
            content = await extract_with_prompt(content, prompt, url)
        except Exception as e:
            logger.warning("Prompt extraction failed for %s: %s", url, e)
            content = f"[Prompt extraction failed, returning raw content]\n\n{content}"

    return mcp_success({"url": url, "content": content[:_MAX_CONTENT]})


async def _fetch_retrodict(url: str) -> dict[str, Any] | str:
    """Fetch in retrodict mode via Wayback Machine."""
    cutoff = retrodict_cutoff.get()
    assert cutoff is not None
    ts = cutoff.strftime("%Y%m%d")

    try:
        snapshot = await check_wayback_availability(
            url,
            ts,
            validate_before_cutoff=True,
            raise_on_rate_limit=True,
        )
    except WaybackRateLimitError:
        return mcp_error(
            f"Wayback rate limited for {url}. Try again shortly, "
            "or use web_search to find alternative sources."
        )

    if snapshot is None:
        return mcp_error(
            f"No archived snapshot for {url}. "
            "Try web_search to find alternative sources."
        )

    content = await fetch_wayback_content(url, ts)
    if content is None:
        return mcp_error(
            f"Content extraction failed for {url}. "
            "May be a PDF, image, or JS-rendered page. "
            "Try web_search for alternative sources."
        )

    return content


# --- MCP Server ---

_BASE_SEARCH_TOOLS = [
    web_search,
    wikipedia,
    fetch_url,
    search_arxiv,
    fetch_arxiv,
]

_OPTIONAL_SEARCH_TOOLS: list[SdkMcpTool[Any]] = []

if settings.exa_api_key:
    _OPTIONAL_SEARCH_TOOLS.append(search_exa)
else:
    logger.info("search_exa tool disabled: EXA_API_KEY not configured")

if settings.asknews_api_key or (
    settings.asknews_client_id and settings.asknews_client_secret
):
    _OPTIONAL_SEARCH_TOOLS.append(search_news)
else:
    logger.info("search_news tool disabled: ASKNEWS credentials not configured")


def create_search_server() -> Any:
    """Create MCP server with all search and content retrieval tools.

    In retrodict mode, excludes search_exa and search_news.
    """
    tools = list(_BASE_SEARCH_TOOLS)
    is_retrodict = retrodict_cutoff.get() is not None
    excluded_in_retrodict = (search_exa, search_news)
    for t in _OPTIONAL_SEARCH_TOOLS:
        if is_retrodict and t in excluded_in_retrodict:
            logger.info("%s excluded in retrodict mode", t.name)
            continue
        tools.append(t)

    return create_mcp_server(
        "search",
        version="2.0.0",
        tools=tools,
    )
