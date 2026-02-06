"""Forecasting research tools - pure capabilities without LLM calls.

These tools are exposed as an in-process MCP server for the forecasting agent.
All tools return raw data; Claude does the reasoning.
"""

import logging
from asyncio import Semaphore
from typing import Annotated, Any, Literal

import httpx
from claude_agent_sdk import tool

from aib.tools.mcp_server import create_mcp_server
from pydantic import BaseModel, Field, field_validator

from metaculus import ApiFilter, BinaryQuestion

from aib.agent.history import load_past_forecasts
from aib.clients.metaculus import get_client as get_metaculus_client
from aib.config import settings
from aib.tools.cache import cached
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)

# --- Rate Limiting ---
#
# These semaphores are intentionally global (module-level) to enforce rate limits
# across ALL concurrent forecast sessions, including subforecasts spawned by
# spawn_subquestions. This prevents exceeding API rate limits when running
# multiple forecasts in parallel.
#
# Behavior:
# - Main forecast and all subforecasts share the same semaphore slots
# - If max_concurrent=5 and main forecast uses 2 slots, subforecasts get 3
# - Subforecasts may queue waiting for slots
#
# Configure via environment:
# - AIB_METACULUS_MAX_CONCURRENT (default: 5)
# - AIB_SEARCH_MAX_CONCURRENT (default: 3)

_metaculus_semaphore = Semaphore(settings.metaculus_max_concurrent)
_search_semaphore = Semaphore(settings.search_max_concurrent)


# --- Input Schemas (Pydantic models with runtime validation) ---


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


class SearchNewsInput(BaseModel):
    query: str
    num_results: int = settings.search_default_limit


class GetMetaculusQuestionsInput(BaseModel):
    """Input for fetching one or more Metaculus questions."""

    post_id_list: Annotated[list[int], Field(min_length=1, max_length=20)]
    # Hidden from agent - injected by retrodict hook to hide current CP
    cutoff_date: str | None = None

    @field_validator("post_id_list", mode="before")
    @classmethod
    def coerce_to_list(cls, v: Any) -> list[int]:
        """Coerce various input formats to list[int].

        Accepts:
        - list[int]: [123, 456] → used as-is
        - int: 123 → [123]
        - str (single): "123" → [123]
        - str (comma-separated): "123, 456" → [123, 456]
        - str (Python list literal): "[123, 456]" → [123, 456]
        """
        if isinstance(v, list):
            return [int(x) for x in v]
        if isinstance(v, int):
            return [v]
        if isinstance(v, str):
            v = v.strip()
            # Handle Python list literal strings like "[123, 456]"
            if v.startswith("[") and v.endswith("]"):
                import ast

                parsed = ast.literal_eval(v)
                if isinstance(parsed, list):
                    return [int(x) for x in parsed]
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
    """Input for fetching coherence links."""

    question_id: int = Field(description="Metaculus question ID (not post ID)")


class CPHistoryInput(BaseModel):
    """Input for fetching community prediction history."""

    question_id: int = Field(description="Metaculus question ID (not post ID)")
    days: int = Field(default=30, description="Number of days of history to fetch")
    before: str | None = Field(
        default=None,
        description="Optional cutoff date (YYYY-MM-DD). Data after this date is excluded.",
    )


class WikipediaInput(BaseModel):
    """Unified Wikipedia tool input."""

    query: str
    mode: Literal["search", "summary", "full"] = "search"
    num_results: int = settings.search_default_limit
    # Hidden from agent - injected by retrodict hook for historical lookups
    cutoff_date: str | None = None


class PredictionHistoryInput(BaseModel):
    post_id: int


# --- Cached API helpers ---


def _question_to_dict(question: Any, *, hide_cp: bool = False) -> dict[str, object]:
    """Convert a MetaculusQuestion to a serializable dict.

    Note: Returns both post_id and question_id. These are different:
    - post_id: Used for URLs and local storage (e.g., metaculus.com/questions/{post_id})
    - question_id: Used for certain API endpoints (get_coherence_links, get_cp_history)

    Args:
        question: MetaculusQuestion object.
        hide_cp: If True, exclude community_prediction (for retrodict mode).
    """
    result: dict[str, object] = {
        "post_id": question.id_of_post,
        "question_id": question.id_of_question,  # Needed for get_coherence_links, get_cp_history
        "title": question.question_text,
        "type": question.get_question_type(),
        "url": question.page_url,
        "background_info": question.background_info,
        "resolution_criteria": question.resolution_criteria,
        "fine_print": question.fine_print,
        "num_forecasters": question.num_forecasters,
    }

    # Include community prediction for binary questions (unless hidden for retrodict)
    if hide_cp:
        result["community_prediction"] = None
    elif isinstance(question, BinaryQuestion):
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


@cached(ttl=300)
async def _fetch_metaculus_question(post_id: int) -> dict[str, object]:
    """Fetch a single Metaculus question (cached, native async)."""
    client = get_metaculus_client()
    question = await client.get_question_by_post_id(post_id)
    if isinstance(question, list):
        question = question[0]
    return _question_to_dict(question)


# --- Pure Data Tools (Metaculus API) ---


@tool(
    "get_metaculus_questions",
    (
        "Fetch details for one or more Metaculus questions by their POST ID. "
        "Pass post_id_list as a list of integer post IDs (e.g., [12345] or [12345, 67890]). "
        "IMPORTANT: These are QUESTION post IDs, not tournament IDs. "
        "To find question IDs, use list_tournament_questions first. "
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
    hide_cp = validated.cutoff_date is not None  # Hide CP in retrodict mode

    async def fetch_one(post_id: int) -> dict[str, Any]:
        """Fetch a single question with error handling."""
        try:
            async with _metaculus_semaphore:
                result = await _fetch_metaculus_question(post_id)
                # Hide community prediction in retrodict mode
                if hide_cp and "community_prediction" in result:
                    result = dict(result)  # Don't modify cached result
                    result["community_prediction"] = None
                return result
        except Exception as e:
            return {"post_id": post_id, "error": str(e)}

    try:
        results = await asyncio.gather(*[fetch_one(pid) for pid in post_ids])
        # For single question, return directly; for multiple, wrap in list
        if len(results) == 1:
            result = results[0]
            if "error" in result:
                return mcp_error(
                    f"Failed to fetch question {result['post_id']}: {result['error']}"
                )
            return mcp_success(result)
        return mcp_success({"questions": list(results)})
    except Exception as e:
        logger.exception("Failed to fetch Metaculus questions")
        return mcp_error(f"Failed to fetch questions: {e}")


@tool(
    "list_tournament_questions",
    (
        "List open questions from a specific Metaculus tournament. "
        "Common TOURNAMENT IDs (not question IDs): "
        "32916 (AIB Spring 2026), 'minibench' (MiniBench), 32921 (Metaculus Cup). "
        "Returns question post IDs that can be used with get_metaculus_questions. "
        f"Optional num_questions (default: {settings.tournament_default_limit})."
    ),
    {"tournament_id": int, "num_questions": int},
)
@tracked("list_tournament_questions")
async def list_tournament_questions(args: dict[str, Any]) -> dict[str, Any]:
    """List questions from a tournament (native async)."""
    try:
        validated = ListTournamentQuestionsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    tournament_id = validated.tournament_id
    num_questions = validated.num_questions

    try:
        async with _metaculus_semaphore:
            client = get_metaculus_client()
            questions = await client.get_all_open_questions_from_tournament(
                tournament_id
            )
            questions = questions[:num_questions]

            results = [
                {
                    "post_id": q.id_of_post,
                    "question_id": q.id_of_question,
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
    """Search Metaculus questions by text (native async)."""
    try:
        validated = SearchMetaculusInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    num_results = validated.num_results

    try:
        async with _metaculus_semaphore:
            client = get_metaculus_client()
            api_filter = ApiFilter(other_url_parameters={"search": query})
            questions = await client.get_questions_matching_filter(
                api_filter=api_filter,
                num_questions=num_results,
            )

            results = [
                {
                    "post_id": q.id_of_post,
                    "question_id": q.id_of_question,
                    "title": q.question_text,
                    "type": q.get_question_type(),
                    "url": q.page_url,
                    "community_prediction": (
                        q.community_prediction_at_access_time
                        if isinstance(q, BinaryQuestion)
                        else None
                    ),
                }
                for q in questions
            ]

        return mcp_success(results)
    except Exception as e:
        logger.exception("Metaculus search failed")
        return mcp_error(f"Search failed: {e}")


@tool(
    "get_coherence_links",
    (
        "Get questions related to this one via coherence links. "
        "Used for consistency checking between related forecasts. "
        "Note: Requires question_id (not post_id) - get this from get_metaculus_questions."
    ),
    {"question_id": int},
)
@tracked("get_coherence_links")
async def get_coherence_links(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch coherence links for a question (native async)."""
    try:
        validated = CoherenceLinksInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    question_id = validated.question_id
    try:
        async with _metaculus_semaphore:
            client = get_metaculus_client()
            links = await client.get_links_for_question(question_id)
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


@tool(
    "get_cp_history",
    (
        "Fetch historical community prediction (CP) data for a question. "
        "Useful for meta-prediction questions about CP movements. "
        "Returns timestamped CP values over the requested period. "
        "Note: Requires question_id (not post_id) - get this from get_metaculus_questions."
    ),
    # `before` is injected by retrodict hook but must be in schema to avoid being stripped
    {"question_id": int, "days": int, "before": str},
)
@tracked("get_cp_history")
async def get_cp_history(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch community prediction history for a question."""
    try:
        validated = CPHistoryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    question_id = validated.question_id
    days = min(validated.days, 365)
    before_cutoff = validated.before

    # Parse cutoff date if provided (for retrodict mode filtering)
    cutoff_dt = None
    if before_cutoff:
        try:
            from datetime import datetime, timezone

            cutoff_dt = datetime.strptime(before_cutoff, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )
        except ValueError:
            return mcp_error(
                f"Invalid 'before' date format: {before_cutoff}. Use YYYY-MM-DD."
            )

    try:
        async with _metaculus_semaphore:
            async with httpx.AsyncClient(
                timeout=settings.http_timeout_seconds,
                headers={"Authorization": f"Token {settings.metaculus_token}"},
            ) as client:
                response = await client.get(
                    f"https://www.metaculus.com/api/questions/{question_id}/aggregate-history/",
                    params={"days": days},
                )
                response.raise_for_status()
                data = response.json()

        history = data.get("history", [])
        results = []
        filtered_count = 0
        for entry in history:
            timestamp = entry.get("start_time") or entry.get("end_time")
            centers = entry.get("centers", [])
            if centers and len(centers) > 0:
                cp = centers[0]
                if cp is not None:
                    # Filter by cutoff date if specified
                    if cutoff_dt and timestamp:
                        from datetime import datetime

                        ts_dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                        if ts_dt > cutoff_dt:
                            filtered_count += 1
                            continue

                    results.append(
                        {
                            "timestamp": timestamp,
                            "community_prediction": round(cp, 4),
                        }
                    )

        if filtered_count > 0:
            logger.info(
                "[Retrodict] CP history: filtered %d points after %s",
                filtered_count,
                before_cutoff,
            )

        return mcp_success(
            {
                "question_id": question_id,
                "days_requested": days,
                "data_points": len(results),
                "history": results,
            }
        )
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return mcp_error(
                f"Question {question_id} not found or has no CP history. "
                "Note: This tool needs the question_id (internal ID), not the post_id (URL ID)."
            )
        logger.exception("Failed to fetch CP history")
        return mcp_error(f"Failed to fetch CP history: {e}")
    except Exception as e:
        logger.exception("Failed to fetch CP history")
        return mcp_error(f"Failed to fetch CP history: {e}")


# --- Pure Search Tools (Raw Results, No LLM Summarization) ---


@cached(ttl=300)
@with_retry(max_attempts=3)
async def _exa_search(
    query: str,
    num_results: int,
    published_before: str | None = None,
    livecrawl: str = "always",
) -> list[dict[str, Any]]:
    """Execute an Exa search (cached for 5 minutes).

    Args:
        query: Search query string.
        num_results: Number of results to return.
        published_before: Optional ISO date (YYYY-MM-DD) to filter results.
        livecrawl: Livecrawl mode ('always', 'fallback', 'never').

    Returns:
        List of search result dicts with title, url, snippet, etc.
    """
    api_key = settings.exa_api_key
    if not api_key:
        raise ValueError("EXA_API_KEY not configured")

    url = "https://api.exa.ai/search"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": api_key,
    }
    payload: dict[str, Any] = {
        "query": query,
        "type": "auto",
        "useAutoprompt": True,
        "numResults": num_results,
        "livecrawl": livecrawl,
        "contents": {
            "text": {"includeHtmlTags": False},
            "highlights": {
                "query": query,
                "numSentences": 4,
                "highlightsPerUrl": 3,
            },
        },
    }

    if published_before:
        payload["publishedBefore"] = f"{published_before}T23:59:59.999Z"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

    results = []
    for r in data.get("results", []):
        published_date = r.get("publishedDate")
        if published_date and isinstance(published_date, str):
            published_date = published_date.rstrip("Z")

        results.append(
            {
                "title": r.get("title"),
                "url": r.get("url"),
                "snippet": (r.get("text") or "")[:500] or None,
                "highlights": r.get("highlights", [])[:3] or None,
                "published_date": published_date,
                "score": r.get("score"),
            }
        )
    return results


@tool(
    "search_exa",
    (
        "Search the web using Exa AI-powered search. Returns raw results with titles, URLs, and snippets. "
        f"Results are cached for 5 minutes. Optional num_results (default: {settings.search_default_limit})."
    ),
    # `published_before` and `livecrawl` are injected by retrodict hook but must be in schema
    {"query": str, "num_results": int, "published_before": str, "livecrawl": str},
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
    published_before = validated.published_before
    livecrawl = validated.livecrawl

    try:
        async with _search_semaphore:
            formatted = await _exa_search(
                query, num_results, published_before, livecrawl
            )
        return mcp_success(formatted)
    except Exception as e:
        logger.exception("Exa search failed")
        return mcp_error(f"Search failed: {e}")


@tool(
    "search_news",
    (
        "Search for recent news using AskNews API. Returns raw news results with headlines, sources, and summaries. "
        f"Optional num_results (default: {settings.news_default_limit})."
    ),
    {"query": str, "num_results": int},
)
@tracked("search_news")
async def search_news(args: dict[str, Any]) -> dict[str, Any]:
    """Search news using AskNews SDK and return formatted results."""
    try:
        validated = SearchNewsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    num_results = validated.num_results

    @with_retry(max_attempts=3)
    async def _search() -> str:
        from asknews_sdk import AskNewsSDK

        client_id = settings.asknews_client_id
        client_secret = settings.asknews_client_secret
        if not client_id or not client_secret:
            raise ValueError("AskNews credentials not configured")

        ask = AskNewsSDK(
            client_id=client_id,
            client_secret=client_secret,
            scopes={"news"},
        )

        # Get latest news (within past 48 hours)
        hot_response = ask.news.search_news(
            query=query,
            n_articles=min(num_results, 6),
            return_type="both",
            strategy="latest news",
        )

        # Get historical news (up to 60 days back)
        historical_response = ask.news.search_news(
            query=query,
            n_articles=num_results,
            return_type="both",
            strategy="news knowledge",
        )

        formatted = "Here are the relevant news articles:\n\n"

        for articles, _ in [
            (hot_response.as_dicts, "Latest"),
            (historical_response.as_dicts, "Historical"),
        ]:
            if not articles:
                continue
            articles_list = [a.__dict__ for a in articles]
            articles_list.sort(key=lambda x: x.get("pub_date", ""), reverse=True)

            for article in articles_list:
                pub_date = article.get("pub_date")
                if pub_date:
                    try:
                        pub_date = pub_date.strftime("%B %d, %Y %I:%M %p")
                    except (AttributeError, ValueError):
                        pub_date = str(pub_date)

                formatted += (
                    f"**{article.get('eng_title', 'Untitled')}**\n"
                    f"{article.get('summary', 'No summary')}\n"
                    f"Language: {article.get('language', 'unknown')}\n"
                    f"Published: {pub_date or 'unknown'}\n"
                    f"Source: [{article.get('source_id', 'unknown')}]({article.get('article_url', '')})\n\n"
                )

        if "articles" not in formatted.lower() or formatted.count("**") == 0:
            formatted += "No articles were found.\n"

        return formatted

    try:
        async with _search_semaphore:
            results = await _search()
        return mcp_success({"query": query, "results": results})
    except Exception as e:
        logger.exception("News search failed")
        return mcp_error(f"News search failed: {e}")


# Wikipedia API (historical support via aib.tools.wikipedia)
from aib.tools.wikipedia import (
    WIKIPEDIA_API_URL,
    WIKIPEDIA_HEADERS,
    extract_intro as _extract_intro,
    fetch_wikipedia_historical as _fetch_wikipedia_historical_content,
)


@tool(
    "wikipedia",
    (
        "Search Wikipedia or fetch article content. "
        "Modes: 'search' (default) finds articles matching query; "
        "'summary' fetches article intro by exact title; "
        "'full' fetches entire article by exact title. "
        f"For search mode, optional num_results (default: {settings.search_default_limit})."
    ),
    # cutoff_date is injected by retrodict hook, must be in schema for validation
    {"query": str, "mode": str, "num_results": int, "cutoff_date": str},
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
    cutoff_date = validated.cutoff_date

    if mode == "search":
        # Search for articles
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

            # In retrodict mode, replace snippets with historical content
            if cutoff_date and results:
                historical_results = []
                for result in results:
                    try:
                        historical = await _fetch_wikipedia_historical_content(
                            result["title"], cutoff_date
                        )
                        # Extract a snippet from the historical content
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
                        # Article didn't exist at cutoff_date, skip it
                        logger.debug("Skipping %s: %s", result["title"], e)
                        continue
                results = historical_results

            return mcp_success({"query": query, "mode": mode, "results": results})
        except Exception as e:
            logger.exception("Wikipedia search failed")
            return mcp_error(f"Wikipedia search failed: {e}")

    else:
        # Fetch article content (summary or full)
        # In retrodict mode, use historical fetch
        if cutoff_date:
            try:
                async with _search_semaphore:
                    historical = await _fetch_wikipedia_historical_content(
                        query, cutoff_date
                    )
                extract = historical["extract"]
                if mode == "summary":
                    extract = _extract_intro(extract)
                return mcp_success(
                    {
                        "title": historical["title"],
                        "url": historical["url"],
                        "extract": extract,
                        "mode": mode,
                        "revision_id": historical["revision_id"],
                        "revision_timestamp": historical["revision_timestamp"],
                        "cutoff_date": cutoff_date,
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
                        "titles": query,  # query is the article title in this mode
                        "prop": "extracts|info",
                        "exintro": mode == "summary",
                        "explaintext": True,
                        "inprop": "url",
                        "redirects": 1,  # Follow Wikipedia redirects
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

# Build tool list conditionally based on available credentials.
# Tools are gated at BOTH layers:
# 1. MCP server registration (here) - so agent doesn't discover unavailable tools
# 2. allowed_tools in core.py - defense in depth
_BASE_FORECASTING_TOOLS = [
    # Metaculus data tools (always available - uses METACULUS_TOKEN which is required)
    get_metaculus_questions,
    list_tournament_questions,
    search_metaculus,
    get_coherence_links,
    get_cp_history,
    get_prediction_history,
]

_OPTIONAL_FORECASTING_TOOLS: list[Any] = []

# Wikipedia (no API key required)
_OPTIONAL_FORECASTING_TOOLS.append(wikipedia)

if settings.exa_api_key:
    _OPTIONAL_FORECASTING_TOOLS.append(search_exa)
else:
    logger.info("search_exa tool disabled: EXA_API_KEY not configured")

if settings.asknews_client_id and settings.asknews_client_secret:
    _OPTIONAL_FORECASTING_TOOLS.append(search_news)
else:
    logger.info("search_news tool disabled: ASKNEWS credentials not configured")


def create_forecasting_server(*, exclude_wikipedia: bool = False) -> Any:
    """Create the forecasting MCP server.

    Args:
        exclude_wikipedia: If True, exclude wikipedia tool (for retrodict mode).
            Wikipedia articles contain post-cutoff information.

    Returns:
        McpSdkServerConfig for use with ClaudeAgentOptions.mcp_servers.
    """
    tools = list(_BASE_FORECASTING_TOOLS)
    for tool in _OPTIONAL_FORECASTING_TOOLS:
        if exclude_wikipedia and tool.name == "wikipedia":
            continue
        tools.append(tool)

    return create_mcp_server(
        name="forecasting",
        version="4.0.0",
        tools=tools,
    )


# Default server for backwards compatibility
forecasting_server = create_forecasting_server()
