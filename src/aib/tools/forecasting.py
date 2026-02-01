"""Forecasting research tools - pure capabilities without LLM calls.

These tools are exposed as an in-process MCP server for the forecasting agent.
All tools return raw data; Claude does the reasoning.
"""

import logging
from asyncio import Semaphore
from typing import Annotated, Any, Literal

import httpx
from claude_agent_sdk import create_sdk_mcp_server, tool
from pydantic import BaseModel, Field, field_validator

from forecasting_tools import (
    ApiFilter,
    BinaryQuestion,
    MetaculusApi,
)
from forecasting_tools.ai_models.exa_searcher import ExaSearcher
from forecasting_tools.helpers.asknews_searcher import AskNewsSearcher

from aib.agent.history import load_past_forecasts
from aib.config import settings
from aib.tools.cache import cached
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)

# Rate limiting semaphores
_metaculus_semaphore = Semaphore(settings.metaculus_max_concurrent)
_search_semaphore = Semaphore(settings.search_max_concurrent)


# --- Input Schemas (Pydantic models with runtime validation) ---


class SearchExaInput(BaseModel):
    query: str
    num_results: int = settings.search_default_limit


class SearchNewsInput(BaseModel):
    query: str
    num_results: int = settings.search_default_limit


class GetMetaculusQuestionsInput(BaseModel):
    """Input for fetching one or more Metaculus questions."""

    post_id_list: Annotated[list[int], Field(min_length=1, max_length=20)]

    @field_validator("post_id_list", mode="before")
    @classmethod
    def coerce_to_list(cls, v: Any) -> list[int]:
        """Coerce various input formats to list[int].

        Accepts:
        - list[int]: [123, 456] → used as-is
        - int: 123 → [123]
        - str (single): "123" → [123]
        - str (comma-separated): "123, 456" → [123, 456]
        """
        if isinstance(v, list):
            return [int(x) for x in v]
        if isinstance(v, int):
            return [v]
        if isinstance(v, str):
            if "," in v:
                return [int(x.strip()) for x in v.split(",")]
            return [int(v)]
        raise ValueError(f"Cannot coerce {type(v).__name__} to list[int]")


class ListTournamentQuestionsInput(BaseModel):
    tournament_id: int | str
    num_questions: int = settings.tournament_default_limit


class SearchMetaculusInput(BaseModel):
    query: str
    num_results: int = settings.metaculus_default_limit


class CoherenceLinksInput(BaseModel):
    post_id: int


class WikipediaInput(BaseModel):
    """Unified Wikipedia tool input."""

    query: str
    mode: Literal["search", "summary", "full"] = "search"
    num_results: int = settings.search_default_limit


class PredictionHistoryInput(BaseModel):
    post_id: int


# --- Cached API helpers ---


@cached(ttl=300)
@with_retry(max_attempts=3)
async def _fetch_metaculus_question(post_id: int) -> dict[str, object]:
    """Fetch a single Metaculus question (cached).

    Args:
        post_id: The Metaculus post ID.

    Returns:
        Dict with question details including community prediction if available.
    """
    question = MetaculusApi.get_question_by_post_id(post_id)
    if isinstance(question, list):
        question = question[0]

    result: dict[str, object] = {
        "post_id": question.id_of_post,
        "title": question.question_text,
        "type": question.get_question_type(),
        "url": question.page_url,
        "background_info": question.background_info,
        "resolution_criteria": question.resolution_criteria,
        "fine_print": question.fine_print,
        "num_forecasters": question.num_forecasters,
    }

    # Include community prediction for binary questions
    if isinstance(question, BinaryQuestion):
        result["community_prediction"] = question.community_prediction_at_access_time
    else:
        result["community_prediction"] = None

    if hasattr(question, "options"):
        result["options"] = getattr(question, "options", None)
    if hasattr(question, "lower_bound"):
        result["lower_bound"] = getattr(question, "lower_bound", None)
    if hasattr(question, "upper_bound"):
        result["upper_bound"] = getattr(question, "upper_bound", None)

    return result


# --- Pure Data Tools (Metaculus API) ---


@tool(
    "get_metaculus_questions",
    (
        "Fetch details for one or more Metaculus questions. "
        "Pass post_id_list as a list of integer post IDs (e.g., [12345] or [12345, 67890]). "
        "Returns question details including title, description, resolution criteria, "
        "fine print, and community prediction (if available). "
        "Note: Community predictions are NOT available in the AIB tournament. "
        "Maximum 20 questions per request."
    ),
    {"post_id_list": list},
)
@tracked("get_metaculus_questions")
async def get_metaculus_questions(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch one or more Metaculus questions (cached for 5 minutes)."""
    import asyncio

    try:
        validated = GetMetaculusQuestionsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    post_ids = validated.post_id_list

    async def fetch_one(post_id: int) -> dict[str, Any]:
        """Fetch a single question with error handling."""
        try:
            async with _metaculus_semaphore:
                return await _fetch_metaculus_question(post_id)
        except Exception as e:
            return {"post_id": post_id, "error": str(e)}

    try:
        results = await asyncio.gather(*[fetch_one(pid) for pid in post_ids])
        # For single question, return directly; for multiple, wrap in list
        if len(results) == 1:
            return mcp_success(results[0])
        return mcp_success({"questions": list(results)})
    except Exception as e:
        logger.exception("Failed to fetch Metaculus questions")
        return mcp_error(f"Failed to fetch questions: {e}")


@tool(
    "list_tournament_questions",
    (
        "List open questions from a specific Metaculus tournament. "
        "Common IDs: 32916 (AIB Spring 2026), 'minibench' (MiniBench), 32921 (Metaculus Cup). "
        f"Optional num_questions (default: {settings.tournament_default_limit})."
    ),
    {"tournament_id": int, "num_questions": int},
)
@tracked("list_tournament_questions")
async def list_tournament_questions(args: dict[str, Any]) -> dict[str, Any]:
    """List questions from a tournament."""
    try:
        validated = ListTournamentQuestionsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    tournament_id = validated.tournament_id
    num_questions = validated.num_questions

    try:
        async with _metaculus_semaphore:
            questions = MetaculusApi.get_all_open_questions_from_tournament(
                tournament_id
            )
            questions = questions[:num_questions]

            results = [
                {
                    "post_id": q.id_of_post,
                    "title": q.question_text,
                    "type": q.get_question_type(),
                    "url": q.page_url,
                }
                for q in questions
            ]

        return mcp_success(results)
    except Exception as e:
        logger.exception("Failed to list tournament questions")
        return mcp_error(f"Failed to list questions: {e}")


@tool(
    "search_metaculus",
    (
        "Search Metaculus questions by text query. Returns matching questions with IDs, titles, and types. "
        f"Optional num_results (default: {settings.metaculus_default_limit})."
    ),
    {"query": str, "num_results": int},
)
@tracked("search_metaculus")
async def search_metaculus(args: dict[str, Any]) -> dict[str, Any]:
    """Search Metaculus questions by text."""
    try:
        validated = SearchMetaculusInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    num_results = validated.num_results

    @with_retry(max_attempts=3)
    async def _search() -> list[dict[str, Any]]:
        api_filter = ApiFilter(other_url_parameters={"search": query})
        questions = await MetaculusApi.get_questions_matching_filter(
            api_filter=api_filter,
            num_questions=num_results,
        )

        results = []
        for q in questions:
            community_pred = (
                q.community_prediction_at_access_time
                if isinstance(q, BinaryQuestion)
                else None
            )
            results.append(
                {
                    "post_id": q.id_of_post,
                    "title": q.question_text,
                    "type": q.get_question_type(),
                    "url": q.page_url,
                    "community_prediction": community_pred,
                }
            )
        return results

    try:
        async with _metaculus_semaphore:
            results = await _search()
        return mcp_success(results)
    except Exception as e:
        logger.exception("Metaculus search failed")
        return mcp_error(f"Search failed: {e}")


@tool(
    "get_coherence_links",
    "Get questions related to this one via coherence links. Used for consistency checking between related forecasts.",
    {"post_id": int},
)
@tracked("get_coherence_links")
async def get_coherence_links(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch coherence links for a question."""
    try:
        validated = CoherenceLinksInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    post_id = validated.post_id
    try:
        from forecasting_tools.helpers.metaculus_client import MetaculusClient

        async with _metaculus_semaphore:
            client = MetaculusClient()
            links = client.get_links_for_question(post_id)
            results = [
                {
                    "question1_id": link.question1_id,
                    "question2_id": link.question2_id,
                    "direction": link.direction,
                    "strength": link.strength,
                    "type": link.type,
                }
                for link in links
            ]
        return mcp_success(results)
    except Exception as e:
        logger.exception("Failed to fetch coherence links")
        return mcp_error(f"Failed to fetch links: {e}")


# --- Pure Search Tools (Raw Results, No LLM Summarization) ---


@cached(ttl=300)
@with_retry(max_attempts=3)
async def _exa_search(query: str, num_results: int) -> list[dict[str, Any]]:
    """Execute an Exa search (cached for 5 minutes).

    Args:
        query: Search query string.
        num_results: Number of results to return.

    Returns:
        List of search result dicts with title, url, snippet, etc.
    """
    searcher = ExaSearcher(
        include_text=True,
        include_highlights=True,
        num_results=num_results,
    )
    results = await searcher.invoke(query)

    return [
        {
            "title": r.title,
            "url": r.url,
            "snippet": r.text[:500] if r.text else None,
            "highlights": r.highlights[:3] if r.highlights else None,
            "published_date": r.published_date,
            "score": r.score,
        }
        for r in results
    ]


@tool(
    "search_exa",
    (
        "Search the web using Exa AI-powered search. Returns raw results with titles, URLs, and snippets. "
        f"Results are cached for 5 minutes. Optional num_results (default: {settings.search_default_limit})."
    ),
    {"query": str, "num_results": int},
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

    try:
        async with _search_semaphore:
            formatted = await _exa_search(query, num_results)
        return mcp_success(formatted)
    except Exception as e:
        logger.exception("Exa search failed")
        return mcp_error(f"Search failed: {e}")


@tool(
    "search_news",
    (
        "Search for recent news using AskNews API. Returns raw news results with headlines, sources, and summaries. "
        "Note: The num_results parameter is currently ignored (upstream library limitation)."
    ),
    {"query": str},
)
@tracked("search_news")
async def search_news(args: dict[str, Any]) -> dict[str, Any]:
    """Search news using AskNews and return raw results.

    Note: The underlying AskNewsSearcher from forecasting-tools does not support
    num_results parameter. To add this feature, either use the raw AskNews SDK
    directly or contribute the feature upstream to forecasting-tools.
    See to_port/main_with_no_framework.py call_asknews() for SDK usage example.
    """
    try:
        validated = SearchNewsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query

    @with_retry(max_attempts=3)
    async def _search() -> str:
        searcher = AskNewsSearcher()
        return await searcher.get_formatted_news_async(query)

    try:
        async with _search_semaphore:
            results = await _search()
        return mcp_success({"query": query, "results": results})
    except Exception as e:
        logger.exception("News search failed")
        return mcp_error(f"News search failed: {e}")


# Wikipedia API base URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


@tool(
    "wikipedia",
    (
        "Search Wikipedia or fetch article content. "
        "Modes: 'search' (default) finds articles matching query; "
        "'summary' fetches article intro by exact title; "
        "'full' fetches entire article by exact title. "
        f"For search mode, optional num_results (default: {settings.search_default_limit})."
    ),
    {"query": str, "mode": str, "num_results": int},
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

    if mode == "search":
        # Search for articles
        @with_retry(max_attempts=3)
        async def _search() -> list[dict[str, Any]]:
            async with httpx.AsyncClient(
                timeout=settings.http_timeout_seconds
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
                    # Remove HTML tags from snippet
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
            async with _search_semaphore:
                results = await _search()
            return mcp_success({"query": query, "mode": mode, "results": results})
        except Exception as e:
            logger.exception("Wikipedia search failed")
            return mcp_error(f"Wikipedia search failed: {e}")

    else:
        # Fetch article content (summary or full)
        @with_retry(max_attempts=3)
        async def _fetch() -> dict[str, Any]:
            async with httpx.AsyncClient(
                timeout=settings.http_timeout_seconds
            ) as client:
                response = await client.get(
                    WIKIPEDIA_API_URL,
                    params={
                        "action": "query",
                        "titles": query,  # query is the article title in this mode
                        "prop": "extracts|info",
                        "exintro": mode == "summary",
                        "explaintext": True,
                        "inprop": "url",
                        "format": "json",
                        "utf8": 1,
                    },
                )
                response.raise_for_status()
                data = response.json()

                pages = data.get("query", {}).get("pages", {})
                if not pages:
                    return {"error": f"Article not found: {query}"}

                page_id = next(iter(pages))
                if page_id == "-1":
                    return {"error": f"Article not found: {query}"}

                page = pages[page_id]
                extract = page.get("extract", "")
                url = page.get(
                    "fullurl",
                    f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}",
                )

                # Truncate very long articles (>50k chars)
                max_chars = 50000
                truncated = len(extract) > max_chars
                if truncated:
                    extract = (
                        extract[:max_chars]
                        + "\n\n[Article truncated - full text exceeds 50,000 characters]"
                    )

                return {
                    "title": page.get("title", query),
                    "url": url,
                    "extract": extract,
                    "mode": mode,
                    "truncated": truncated,
                    "original_length": len(page.get("extract", "")),
                }

        try:
            async with _search_semaphore:
                result = await _fetch()
            return mcp_success(result)
        except Exception as e:
            logger.exception("Wikipedia article fetch failed")
            return mcp_error(f"Wikipedia article fetch failed: {e}")


@tool(
    "get_prediction_history",
    (
        "Get past forecasts made for a Metaculus question. Returns your previous "
        "forecasts with timestamps, probabilities/medians, and summaries. "
        "Useful for tracking how your forecasts evolved and learning from resolved questions."
    ),
    {"post_id": int},
)
@tracked("get_prediction_history")
async def get_prediction_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get past forecasts for a question from local storage."""
    try:
        validated = PredictionHistoryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    post_id = validated.post_id

    try:
        forecasts = load_past_forecasts(post_id)

        if not forecasts:
            return mcp_success({"post_id": post_id, "forecasts": [], "count": 0})

        # Convert to serializable format
        results = []
        for f in forecasts:
            result: dict[str, Any] = {
                "timestamp": f.timestamp,
                "question_type": f.question_type,
                "summary": f.summary,
                "resolution": f.resolution,
            }

            if f.question_type == "binary":
                result["probability"] = f.probability
                result["logit"] = f.logit
            elif f.question_type == "multiple_choice":
                result["probabilities"] = f.probabilities
            elif f.question_type in ("numeric", "discrete"):
                result["median"] = f.median
                result["confidence_interval"] = f.confidence_interval
                result["percentiles"] = f.percentiles

            results.append(result)

        return mcp_success(
            {
                "post_id": post_id,
                "question_title": forecasts[0].question_title,
                "forecasts": results,
                "count": len(results),
            }
        )
    except Exception as e:
        logger.exception("Failed to load prediction history")
        return mcp_error(f"Failed to load history: {e}")


# --- Create MCP Server ---

# Build tool list conditionally based on available credentials
_forecasting_tools = [
    # Metaculus data tools
    get_metaculus_questions,  # Unified: handles single or batch
    list_tournament_questions,
    search_metaculus,
    get_coherence_links,
    get_prediction_history,
    # Search tools (raw results, cached)
    wikipedia,  # Unified: search, summary, or full article
]

# Only include search_exa if Exa API key is configured
if settings.exa_api_key:
    _forecasting_tools.append(search_exa)
else:
    logger.info("search_exa tool disabled: EXA_API_KEY not configured")

# Only include search_news if AskNews credentials are configured
if settings.asknews_client_id and settings.asknews_client_secret:
    _forecasting_tools.append(search_news)
else:
    logger.info("search_news tool disabled: ASKNEWS_CLIENT_ID/SECRET not configured")

forecasting_server = create_sdk_mcp_server(
    name="forecasting",
    version="4.0.0",
    tools=_forecasting_tools,
)
