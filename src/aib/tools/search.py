"""Unified search and content retrieval tools.

Provides web search (via Haiku sub-agent + API augmentation), Exa AI search,
Wikipedia, arXiv, and URL content fetching. All "find/retrieve information"
tools live here. AskNews is served by a separate remote MCP server.

Search snippets are always fetched from actual page content, not from the
search engine. API-augmented results get snippets from api_data; others are
fetched live (or from the Wayback Machine in retrodict mode).
"""

import asyncio
import json
import logging
from collections.abc import Iterator
from typing import Any, Literal, TypedDict
from urllib.parse import unquote

import httpx
from claude_agent_sdk import AssistantMessage, ResultMessage
from lup.hooks import (
    LupHookInput,
    create_capture_hook,
    create_tool_allowlist_hook,
    merge_hooks,
)
from pydantic import BaseModel, Field

from aib.agent.client import AupRefusalError
from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.arxiv_search import fetch_arxiv, search_arxiv
from aib.tools.metrics import costs
from aib.tools.exa import ExaResult, exa_search
from aib.tools.extract import extract_with_prompt
from aib.tools.fetch_http import FetchResult, fetch_live
from lup.mcp import ToolError, ToolResponse, lup_tool, response_text
from lup.resilience.retry import with_retry
from lup.tool_routes import routes
from lup.types import JsonValue
from aib.tools.throttle import exa_throttle, wikipedia_throttle
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


# The PreToolUse tool filter this file used to build by hand is
# `lup.hooks.create_tool_allowlist_hook` — same reason for existing
# (bypassPermissions ignores allowed_tools), and its denial names the tools
# that ARE available so the sub-agent can re-plan instead of retrying.


class WebSearchInput(BaseModel):
    """Input for web search (matches WebSearch interface)."""

    query: str = Field(min_length=1, description="Search query")
    allowed_domains: list[str] | None = Field(
        default=None, description="Only include results from these domains"
    )
    blocked_domains: list[str] | None = Field(
        default=None, description="Never include results from these domains"
    )


class SearchLink(TypedDict):
    """One link a WebSearch result carried, captured for the sources list."""

    title: str
    url: str


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


def _snippet_from_api_data(api_data: dict[str, Any]) -> str | None:
    """Extract a short text snippet from an MCP api_data response.

    Parses the JSON payload and looks for common text fields
    (extract, abstract, summary, description), falling back to a
    truncated version of the raw JSON text.
    """
    _TEXT_FIELDS = ("extract", "abstract", "summary", "description", "content")

    content_blocks = api_data.get("content", [])
    if not content_blocks:
        return None

    raw_text = content_blocks[0].get("text", "")
    if not raw_text:
        return None

    try:
        payload = json.loads(raw_text)
    except (json.JSONDecodeError, TypeError):
        return raw_text[:500]

    if isinstance(payload, dict):
        for field in _TEXT_FIELDS:
            value = payload.get(field)
            if isinstance(value, str) and len(value) > 20:
                return value[:500]

    return raw_text[:500]


async def _wayback_filter_non_api_results(
    results: list[AugmentedSearchResult],
    cutoff_date: str,
) -> list[AugmentedSearchResult]:
    """Wayback-validate only non-API-augmented search results.

    API-augmented results have their snippets replaced with text extracted
    from api_data (handlers validate cutoff internally via retrodict_cutoff
    ContextVar). Non-API results get full Wayback validation: dropped if no
    pre-cutoff snapshot, snippets replaced with Wayback-extracted content.
    Both paths prevent future data leaks from search engine snippets.
    """
    wayback_ts = cutoff_date.replace("-", "")

    async def _validate_one(
        result: AugmentedSearchResult,
    ) -> AugmentedSearchResult | None:
        if result["api_data"] is not None:
            safe_snippet = _snippet_from_api_data(result["api_data"])
            if safe_snippet is not None:
                result["snippet"] = safe_snippet
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


async def _fetch_live_snippets(
    results: list[AugmentedSearchResult],
) -> list[AugmentedSearchResult]:
    """Populate snippets from actual page content for non-API results.

    API-augmented results get snippets from api_data. Non-API results
    get snippets fetched from the live page via fetch_live.
    """

    async def _fetch_one(
        result: AugmentedSearchResult,
    ) -> AugmentedSearchResult:
        if result["api_data"] is not None:
            safe_snippet = _snippet_from_api_data(result["api_data"])
            if safe_snippet is not None:
                result["snippet"] = safe_snippet
            return result

        fetched = await fetch_live(result["url"])
        if isinstance(fetched, FetchResult):
            result["snippet"] = fetched.text[:500]
        return result

    return list(await asyncio.gather(*[_fetch_one(r) for r in results]))


def websearch_links(event: LupHookInput) -> list[SearchLink]:
    """Every {title, url} link a WebSearch tool result carried.

    The extract half of `lup.hooks.create_capture_hook`: lup owns the
    accumulator and the PostToolUse wiring, and this says what is worth
    keeping out of one response.
    """

    def links() -> Iterator[SearchLink]:
        try:
            payload = json.loads(event.tool_result)
        except (json.JSONDecodeError, TypeError):
            return
        if not isinstance(payload, dict):
            return
        # lup: ignore[dict-get] — the provider's own WebSearch response
        for item in payload.get("results", []):
            if not isinstance(item, dict):
                continue
            for link in item.get("content", []):  # lup: ignore[dict-get] — same
                if isinstance(link, dict) and link.get("url"):  # lup: ignore[dict-get]
                    yield SearchLink(
                        title=str(link.get("title", "")),  # lup: ignore[dict-get]
                        url=str(link["url"]),
                    )

    return list(links())


async def _raw_web_search(
    search_query: str,
    cutoff_date: str | None = None,
    allowed_domains: list[str] | None = None,
    blocked_domains: list[str] | None = None,
) -> list[SearchResult]:
    """One-shot web search via a minimal Haiku sub-agent with WebSearch.

    Haiku invokes the WebSearch tool; a PostToolUse hook captures the raw
    result URLs. Snippets are populated later by _fetch_live_snippets or
    _wayback_filter_non_api_results.
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

    from aib.agent.client import build_client
    from aib.agent.display import make_agent_prefix, print_block

    capture = create_capture_hook("WebSearch", websearch_links)
    captured_links = capture["captured"]
    prefix = make_agent_prefix("websearch", search_query)

    async with build_client(
        model="haiku",
        permission_mode="bypassPermissions",
        allowed_tools=["WebSearch"],
        hooks=merge_hooks(
            create_tool_allowlist_hook(["WebSearch"]),
            capture["hooks"],
        ),
        system_prompt="You are a web search assistant. Use WebSearch to find information.",
    ) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    print_block(block, prefix=prefix)
            if isinstance(message, ResultMessage):
                logger.debug(
                    "[WebSearch] sub-agent result: subtype=%s turns=%d is_error=%s",
                    message.subtype,
                    message.num_turns,
                    message.is_error,
                )
                if message.total_cost_usd is not None:
                    costs.record("web_search", message.total_cost_usd)

    seen_urls: set[str] = set()
    results: list[SearchResult] = []
    for link in captured_links:
        url = link["url"]
        if url not in seen_urls:
            seen_urls.add(url)
            results.append(
                SearchResult(
                    title=link.get("title", ""),
                    url=url,
                    snippet=None,
                )
            )

    if not results:
        logger.warning("[WebSearch] no results for query=%s", search_query)

    return results


async def _augment_with_api_data(
    results: list[SearchResult],
) -> list[AugmentedSearchResult]:
    """Augment search results with structured API data from recognized domains.

    For each result URL, checks the registry every tool registers itself
    against. Matching URLs have their specialized tool handler called in
    parallel. Redirected domains get a hint string instead.
    """

    async def _augment_one(result: SearchResult) -> AugmentedSearchResult:
        url = result["url"]
        augmented = AugmentedSearchResult(
            title=result["title"],
            url=url,
            snippet=result["snippet"],
            api_data=None,
            hint=None,
        )

        advice = routes.advice(url)
        if advice is not None:
            augmented["hint"] = advice
            return augmented

        try:
            api_result = await routes.dispatch(url)
            if api_result is not None and not api_result.get("is_error"):
                augmented["api_data"] = dict(api_result)
        except Exception as e:
            logger.warning("API augmentation failed for %s: %s", url, e)

        return augmented

    augmented = await asyncio.gather(*[_augment_one(r) for r in results])
    return list(augmented)


class WebSearchOutput(BaseModel):
    """Search results for one query, each augmented where a tool knows better."""

    query: str
    results: list[AugmentedSearchResult]


@lup_tool(
    (
        "Search the web for information. Returns titles, URLs, and snippets. "
        "When results match known data sources (stock quotes, arXiv, Wikipedia, "
        "FRED, prediction markets), automatically includes structured API data. "
        "Supports allowed_domains/blocked_domains for domain filtering. "
        "Prefer this over WebSearch."
    ),
    name="web_search",
)
async def web_search(params: WebSearchInput) -> WebSearchOutput:
    """Perform web search via SDK sub-agent with API augmentation.

    Augments all results first, then in retrodict mode applies Wayback
    validation only to results that lack API data (API-augmented results
    are safe since specialized handlers manage time-appropriateness).
    """
    if params.allowed_domains and params.blocked_domains:
        raise ToolError("Cannot use both allowed_domains and blocked_domains.")

    cutoff = retrodict_cutoff.get()
    cutoff_date = cutoff.isoformat() if cutoff else None

    try:
        logger.info(
            "[WebSearch] query=%s cutoff=%s domains=%s",
            params.query,
            cutoff_date,
            params.allowed_domains or params.blocked_domains,
        )

        results = await _raw_web_search(
            params.query,
            cutoff_date,
            params.allowed_domains,
            params.blocked_domains,
        )

        augmented = await _augment_with_api_data(results)

        if cutoff_date:
            augmented = await _wayback_filter_non_api_results(
                augmented,
                cutoff_date,
            )
        else:
            augmented = await _fetch_live_snippets(augmented)

        logger.info("[WebSearch] Returning %d results", len(augmented))
        return WebSearchOutput(query=params.query, results=augmented)

    except BaseException as e:
        cause = e
        if isinstance(e, BaseExceptionGroup):
            cause = e.exceptions[0] if e.exceptions else e
        logger.exception("Web search failed: %s", cause)
        raise ToolError(
            "Web search is temporarily unavailable. "
            "Try again with a different query, or use alternative tools."
        ) from e


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


class SearchExaOutput(BaseModel):
    """Exa's own result records, passed through as the vendor shaped them."""

    query: str
    results: list[ExaResult]


@lup_tool(
    (
        "Search the web using Exa AI-powered search. Returns raw results with titles, URLs, and snippets. "
        f"Results are cached for 5 minutes. Optional num_results (default: {settings.search_default_limit}).\n\n"
        "Examples:\n"
        '  search_exa(query="EU AI Act implementation timeline 2026")\n'
        '  search_exa(query="MSFT earnings Q1 2026 results", num_results=10)\n'
        '  search_exa(query="Germany coalition government formation", published_before="2026-01-15")\n'
        "Use diverse query formulations — the same topic found with different keywords produces richer results."
    ),
    name="search_exa",
)
async def search_exa(params: SearchExaInput) -> SearchExaOutput:
    """Search using Exa and return raw results (cached)."""
    cutoff = retrodict_cutoff.get()
    published_before = (
        cutoff.isoformat() if cutoff is not None else params.published_before
    )
    livecrawl = "never" if cutoff is not None else params.livecrawl

    logger.info(
        "search_exa actual params: published_before=%s, livecrawl=%s",
        published_before,
        livecrawl,
    )

    async with exa_throttle.slot():
        formatted = await exa_search(
            params.query,
            params.num_results,
            published_before=published_before,
            livecrawl=livecrawl,
        )
    return SearchExaOutput(query=params.query, results=formatted)


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


def _parse_asknews_articles(
    result: object,
) -> list[dict[str, str]]:
    """Parse article data from an AskNews CallToolResult."""
    articles: list[dict[str, str]] = []

    content_blocks = getattr(result, "content", [])
    for block in content_blocks:
        text = getattr(block, "text", None)
        if not text:
            continue
        try:
            data = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            continue

        items: list[dict[str, str]] = []
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            for key in ("results", "articles", "data"):
                candidate = data.get(key)
                if isinstance(candidate, list):
                    items = candidate
                    break

        for item in items:
            if isinstance(item, dict) and item.get("title"):
                title = str(item["title"])
                articles.append(
                    {
                        "title": title,
                        "snippet": str(
                            item.get(
                                "snippet",
                                item.get("summary", item.get("extract", "")),
                            )
                        ),
                        "url": str(
                            item.get(
                                "url",
                                f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}",
                            )
                        ),
                    }
                )

    return articles


async def _asknews_wikipedia_search(query: str) -> list[dict[str, str]]:
    """Search Wikipedia via AskNews semantic/vector search (best-effort).

    Calls the AskNews remote MCP server's search_wikipedia tool directly.
    Returns a list of {title, snippet, url} dicts, or empty list on failure.
    """
    api_key = settings.asknews_api_key
    if not api_key:
        return []

    try:
        from aib.tools.asknews import _call_remote

        text = await _call_remote(api_key, "search_wikipedia", {"query": query})
        data = json.loads(text)
        items: list[dict[str, str]] = []
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            for key in ("results", "articles", "data"):
                candidate = data.get(key)
                if isinstance(candidate, list):
                    items = candidate
                    break
        return [
            {
                "title": a["title"],
                "snippet": a.get("snippet", ""),
                "url": a.get("url", ""),
            }
            for a in items
            if isinstance(a, dict) and "title" in a
        ]
    except Exception:
        logger.debug("AskNews Wikipedia search failed", exc_info=True)
        return []


class WikipediaSearchOutput(BaseModel):
    """Articles matching a query — the answer to `mode="search"`.

    A hit always carries a title, snippet and url, and then whichever extras
    the search that produced it has: a word count from keyword search, a
    `source` label from AskNews's semantic search, a `revision_timestamp`
    from a retrodict search. Declaring the envelope and passing the records
    through keeps all three intact rather than flattening them to their
    intersection.
    """

    query: str
    mode: Literal["search"] = "search"
    results: list[dict[str, JsonValue]]


class WikipediaArticle(BaseModel):
    """One article's text — the answer to `mode="summary"` or `mode="full"`.

    `extract` is a whole article in full mode, so it is declared plainly as
    a string: that is what lets `guard_result` spill an oversized one to
    disk and hand back a pointer instead of losing it to truncation.

    The revision fields are the retrodict answer, naming which historical
    revision was read; a live fetch leaves them unset.
    """

    title: str
    url: str
    extract: str
    mode: Literal["summary", "full"]
    revision_id: int | None = None
    revision_timestamp: str | None = None
    revision_date: str | None = None


@lup_tool(
    (
        "Search Wikipedia or fetch article content. "
        "Search mode combines keyword and semantic search for broader coverage. "
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
    name="wikipedia",
)
async def wikipedia(
    params: WikipediaInput,
) -> WikipediaSearchOutput | WikipediaArticle:
    """Unified Wikipedia search and article fetching."""
    query = params.query
    mode = params.mode
    num_results = params.num_results
    cutoff = retrodict_cutoff.get()
    cutoff_date = cutoff.isoformat() if cutoff is not None else None

    if mode == "search":

        @with_retry(max_attempts=3)
        # lup: ignore[any-type] — MediaWiki/AskNews hit records, passed through
        async def keyword_search() -> list[dict[str, Any]]:
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

        if not cutoff_date and settings.asknews_api_key:
            async with wikipedia_throttle.slot():
                wiki_results, asknews_results = await asyncio.gather(
                    keyword_search(),
                    _asknews_wikipedia_search(query),
                )
            seen_titles = {r["title"].lower().strip() for r in wiki_results}
            for ar in asknews_results:
                if ar["title"].lower().strip() not in seen_titles:
                    seen_titles.add(ar["title"].lower().strip())
                    wiki_results.append(
                        {
                            "title": ar["title"],
                            "snippet": ar.get("snippet", ""),
                            "url": ar["url"],
                            "word_count": 0,
                            "source": "semantic",
                        }
                    )
            results = wiki_results
        else:
            async with wikipedia_throttle.slot():
                results = await keyword_search()

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
                raise ToolError(f"No Wikipedia articles found for '{query}'.")
            results = historical_results

        return WikipediaSearchOutput(query=query, results=results)

    else:
        if cutoff_date:
            async with wikipedia_throttle.slot():
                historical = await _fetch_wikipedia_historical_content(
                    query, cutoff_date
                )
            extract = historical["extract"]
            if mode == "summary":
                extract = _extract_intro(extract)
            if params.prompt:
                extract = await extract_with_prompt(
                    extract, params.prompt, historical["url"]
                )
            return WikipediaArticle(
                title=historical["title"],
                url=historical["url"],
                extract=extract,
                mode=mode,
                revision_id=historical["revision_id"],
                revision_timestamp=historical["revision_timestamp"],
                revision_date=historical["revision_timestamp"][:10],
            )

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
                        "titles": unquote(query),
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

        async with wikipedia_throttle.slot():
            result = await _fetch()
        extract = result["extract"]
        if params.prompt:
            extract = await extract_with_prompt(
                extract, params.prompt, result["url"]
            )
        return WikipediaArticle(
            title=result["title"],
            url=result["url"],
            extract=extract,
            mode=mode,
        )


# --- Fetch URL Tool ---

_MAX_CONTENT = 10_000


class FetchUrlInput(BaseModel):
    url: str = Field(min_length=1, description="The URL to fetch content from")
    prompt: str | None = Field(
        default=None,
        description="What information to extract from the page",
    )


def unwrap_mcp_response(response: ToolResponse) -> JsonValue:
    """Extract the raw payload a routed tool answered with.

    A route dispatches to another tool, which returns an MCP tool result —
    the text of which is that tool's own JSON. Unwrapping it here lets
    `lup_tool` re-wrap the whole thing once, rather than nesting one tool
    result inside another.
    """
    text = response_text(response)
    if "is_error" in response and response["is_error"]:
        raise ToolError(text or "Unknown error")
    return json.loads(text or "{}")


class FetchedPage(BaseModel):
    """A page's extracted text, plus whatever structure came with it.

    `content` is declared plainly as a string so `guard_result` can spill an
    oversized page to disk instead of letting it be truncated on the wire.
    `routed` is the answer of the tool a URL route reached instead — the
    shape belongs to that tool, so it crosses as its own payload.
    """

    url: str
    content: str = ""
    title: str = ""
    structured_data: list[str] = []
    routed: JsonValue = None


@lup_tool(
    (
        "Fetch and extract content from a URL. "
        "Automatically extracts readable text, renders JavaScript pages via Playwright, "
        "and routes known domains to specialized tools "
        "(Yahoo Finance, arXiv, Wikipedia, FRED, Polymarket). "
        "Without a prompt, returns the full extracted text. "
        "With a prompt, uses an LLM to extract specific information "
        "and surfaces relevant links for follow-up research. "
        "Prefer this over WebFetch for URL fetching."
    ),
    name="fetch_url",
)
async def fetch_url(params: FetchUrlInput) -> FetchedPage:
    """Unified fetch: domain dispatch -> http/wayback -> trafilatura -> playwright -> prompt."""
    url, prompt = params.url, params.prompt

    dispatched = await routes.dispatch(url)
    if dispatched is not None:
        return FetchedPage(url=url, routed=unwrap_mcp_response(dispatched))

    if retrodict_cutoff.get() is not None:
        result = await _fetch_retrodict(url)
    else:
        result = await fetch_live(url)

    if isinstance(result, dict):
        return FetchedPage(url=url, routed=unwrap_mcp_response(result))

    if isinstance(result, FetchResult):
        text, title = result.text, result.title
    else:
        text, title = result, ""

    if prompt:
        try:
            text = await extract_with_prompt(text, prompt, url)
        except AupRefusalError:
            logger.warning(
                "Content extraction refused for %s, returning raw content", url
            )
            text = f"[Prompt extraction failed, returning raw content]\n\n{text}"
        except Exception as e:
            logger.warning("Prompt extraction failed for %s: %s", url, e)
            text = f"[Prompt extraction failed, returning raw content]\n\n{text}"

    return FetchedPage(
        url=url,
        content=text[:_MAX_CONTENT],
        title=title,
        structured_data=result.data if isinstance(result, FetchResult) else [],
    )


async def _fetch_retrodict(url: str) -> FetchResult | str:
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
    except WaybackRateLimitError as e:
        raise ToolError(
            f"Wayback rate limited for {url}. Try again shortly, "
            "or use web_search to find alternative sources."
        ) from e

    if snapshot is None:
        raise ToolError(
            f"No archived snapshot for {url}. "
            "Try web_search to find alternative sources."
        )

    content = await fetch_wayback_content(url, ts)
    if content is None:
        raise ToolError(
            f"Content extraction failed for {url}. "
            "May be a PDF, image, or JS-rendered page. "
            "Try web_search for alternative sources."
        )

    return content


# --- Exported tool lists (for server construction) ---

BASE_SEARCH_TOOLS = [
    web_search,
    wikipedia,
    fetch_url,
    search_arxiv,
    fetch_arxiv,
]

OPTIONAL_SEARCH_TOOLS = [search_exa] if settings.exa_api_key else []

if not settings.exa_api_key:
    logger.info("search_exa tool disabled: EXA_API_KEY not configured")
