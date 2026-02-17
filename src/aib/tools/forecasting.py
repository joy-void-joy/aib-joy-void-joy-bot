"""Forecasting research tools - pure capabilities without LLM calls.

These tools are exposed as an in-process MCP server for the forecasting agent.
All tools return raw data; Claude does the reasoning.
"""

import logging
import asyncio
from datetime import datetime, timezone
from typing import Annotated, Any, Literal, TypedDict

import httpx
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query, tool


from claude_agent_sdk import SdkMcpTool
from claude_agent_sdk.types import McpSdkServerConfig

from aib.tools.mcp_server import create_mcp_server
from pydantic import BaseModel, Field, field_validator

from metaculus import ApiFilter, BinaryQuestion
from metaculus.models import AggregationMethod

from aib.retrodict_context import retrodict_cutoff
from aib.agent.history import load_past_forecasts
from aib.clients.metaculus import get_client as get_metaculus_client
from aib.config import settings
from aib.tools.cache import cached
from aib.tools.exa import exa_search
from aib.tools.extract import extract_with_prompt
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry
from aib.tools.wikipedia import (
    WIKIPEDIA_API_URL,
    WIKIPEDIA_HEADERS,
    extract_intro as _extract_intro,
    fetch_wikipedia_historical as _fetch_wikipedia_historical_content,
)

logger = logging.getLogger(__name__)

# --- Rate Limiting ---
#
# Semaphores enforce rate limits across concurrent forecast sessions.
# They are lazily created per-event-loop to avoid "bound to a different event loop"
# errors when asyncio.run() creates fresh loops (e.g., tournament mode).

_semaphore_store: dict[str, asyncio.Semaphore] = {}


def _get_semaphore(name: str, limit: int) -> asyncio.Semaphore:
    """Get or create a semaphore for the current event loop."""
    loop = asyncio.get_running_loop()
    key = f"{name}_{id(loop)}"
    if key not in _semaphore_store:
        _semaphore_store[key] = asyncio.Semaphore(limit)
    return _semaphore_store[key]


def _search_semaphore() -> asyncio.Semaphore:
    return _get_semaphore("search", settings.search_max_concurrent)


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

    question_id: int = Field(
        description="Metaculus question ID or post ID (auto-detected)"
    )
    days: int = Field(default=30, description="Number of days of history to fetch")


class WikipediaInput(BaseModel):
    """Unified Wikipedia tool input."""

    query: str
    mode: Literal["search", "summary", "full"] = "search"
    num_results: int = settings.search_default_limit
    prompt: str | None = Field(
        default=None,
        description="Extract specific information from the article (summary/full modes only).",
    )


class PredictionHistoryInput(BaseModel):
    post_id: int


# --- Output Schemas ---


class QuestionDict(TypedDict, total=False):
    """Metaculus question data returned by _question_to_dict."""

    post_id: int
    question_id: int
    title: str
    type: str
    url: str
    background_info: str | None
    resolution_criteria: str | None
    fine_print: str | None
    num_forecasters: int
    community_prediction: float | None
    options: list[str] | None
    lower_bound: float | None
    upper_bound: float | None


class CPHistoryEntry(BaseModel):
    """A single CP data point in the history."""

    timestamp: str
    community_prediction: float


class CPHistoryResponse(BaseModel):
    """Response from the get_cp_history tool."""

    question_id: int
    days_requested: int
    data_points: int
    history: list[CPHistoryEntry]
    note: str | None = None


# --- Retrodict text redaction ---


async def _redact_future_info(text: str, cutoff_date: str) -> str:
    """Use haiku to remove references to events after the cutoff date."""
    if not text or len(text) < 20:
        return text

    prompt = (
        f"Remove any references to events, dates, or outcomes that occur after {cutoff_date}. "
        f"Keep all other content unchanged. Return ONLY the redacted text, nothing else.\n\n"
        f"Text:\n{text}"
    )
    options = ClaudeAgentOptions(
        model="sonnet",
        allowed_tools=[],
        system_prompt=(
            "You redact temporal information from text. Remove sentences or clauses "
            "that reference events after the given date. Preserve everything else verbatim. "
            "Return only the redacted text."
        ),
        extra_args={"no-session-persistence": None},
    )
    try:
        result_text = None
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, ResultMessage) and message.result:
                result_text = message.result
        return result_text or text
    except Exception:
        logger.warning("Fine-print redaction failed, returning original")
        return text


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
    GetMetaculusQuestionsInput.model_json_schema(),
)
@tracked("get_metaculus_questions")
async def get_metaculus_questions(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch one or more Metaculus questions (cached for 5 minutes)."""
    try:
        validated = GetMetaculusQuestionsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    post_ids = validated.post_id_list
    cutoff = retrodict_cutoff.get()

    async def _apply_retrodict_filters(result: dict[str, Any]) -> dict[str, Any]:
        """Apply CP hiding and fine_print redaction for retrodict mode."""
        if cutoff is None:
            return result
        result = dict(result)
        if "community_prediction" in result:
            result["community_prediction"] = None
        fine_print = result.get("fine_print")
        if isinstance(fine_print, str) and len(fine_print) > 20:
            result["fine_print"] = await _redact_future_info(fine_print, str(cutoff))
        return result

    async def fetch_one(post_id: int) -> dict[str, Any]:
        """Fetch a single question, auto-detecting if a question_id was passed."""
        try:
            result = await _fetch_metaculus_question(post_id)
            return await _apply_retrodict_filters(result)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                resolved = await _resolve_question_to_post_id(post_id)
                if resolved:
                    try:
                        result = await _fetch_metaculus_question(resolved)
                        return await _apply_retrodict_filters(result)
                    except Exception as retry_err:
                        return {
                            "post_id": post_id,
                            "error": f"Resolved question {post_id} → post {resolved}, but fetch failed: {retry_err}",
                        }
                return {
                    "post_id": post_id,
                    "error": f"ID {post_id} not found. You may have passed a question_id instead of a post_id. Use list_tournament_questions to find correct post IDs.",
                }
            return {"post_id": post_id, "error": f"HTTP {e.response.status_code}: {e}"}
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
    ListTournamentQuestionsInput.model_json_schema(),
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
        client = get_metaculus_client()
        questions = await client.get_all_open_questions_from_tournament(tournament_id)

        cutoff = retrodict_cutoff.get()
        if cutoff is not None:
            cutoff_dt = datetime.combine(cutoff, datetime.min.time()).replace(
                tzinfo=timezone.utc
            )
            questions = [
                q
                for q in questions
                if q.published_time is None or q.published_time <= cutoff_dt
            ]

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
    SearchMetaculusInput.model_json_schema(),
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
        client = get_metaculus_client()
        api_filter = ApiFilter(other_url_parameters={"search": query})
        questions = await client.get_questions_matching_filter(
            api_filter=api_filter,
            num_questions=num_results,
        )

        cutoff = retrodict_cutoff.get()

        if cutoff is not None:
            cutoff_dt = datetime.combine(cutoff, datetime.min.time()).replace(
                tzinfo=timezone.utc
            )
            questions = [
                q
                for q in questions
                if q.published_time is None or q.published_time <= cutoff_dt
            ]

        results = [
            {
                "post_id": q.id_of_post,
                "question_id": q.id_of_question,
                "title": q.question_text,
                "type": q.get_question_type(),
                "url": q.page_url,
                "community_prediction": (
                    None
                    if cutoff is not None
                    else (
                        q.community_prediction_at_access_time
                        if isinstance(q, BinaryQuestion)
                        else None
                    )
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
        "Get Metaculus questions that are logically related to this one. "
        "USE THIS to check if your forecast is consistent with related questions — "
        "e.g., if you forecast 80% on 'Will X happen by 2027?', your forecast on "
        "'Will X happen by 2026?' should be ≤80%. "
        "Requires question_id (not post_id) — get this from get_metaculus_questions."
    ),
    CoherenceLinksInput.model_json_schema(),
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


def _format_timestamp(raw_ts: object) -> str:
    """Convert a Unix timestamp (float) or ISO string to ISO 8601."""
    if isinstance(raw_ts, (int, float)):
        return datetime.fromtimestamp(raw_ts, tz=timezone.utc).isoformat()
    return str(raw_ts)


def _build_cp_history_response(
    aggregation: AggregationMethod,
    question_id: int,
    days: int,
    cutoff_dt: datetime | None,
) -> CPHistoryResponse:
    """Build a typed CP history response from aggregation data."""
    entries: list[CPHistoryEntry] = []
    filtered_count = 0

    for point in aggregation.history:
        if not point.centers:
            continue
        cp = point.centers[0]

        if cutoff_dt is not None:
            ts_dt = datetime.fromtimestamp(point.start_time, tz=timezone.utc)
            if ts_dt > cutoff_dt:
                filtered_count += 1
                continue

        entries.append(
            CPHistoryEntry(
                timestamp=_format_timestamp(point.start_time),
                community_prediction=cp,
            )
        )

    if filtered_count > 0:
        cutoff_date = retrodict_cutoff.get()
        logger.info(
            "[Retrodict] CP history: filtered %d points after %s",
            filtered_count,
            cutoff_date,
        )

    note = None
    if filtered_count > 0 and len(entries) == 0:
        note = (
            "No historical CP data is available yet. "
            "This is expected when the question was recently published."
        )

    return CPHistoryResponse(
        question_id=question_id,
        days_requested=days,
        data_points=len(entries),
        history=entries,
        note=note,
    )


_post_id_cache: dict[int, int] = {}


async def _resolve_question_to_post_id(question_id: int) -> int | None:
    """Resolve a Metaculus question_id to its post_id."""
    try:
        client = get_metaculus_client()
        data = await client.fetch_question_json(question_id)
        post_id = data.get("post_id") or data.get("post", {}).get("id")
        if post_id:
            logger.info("Resolved question %d → post %d", question_id, post_id)
        return post_id
    except Exception:
        logger.exception("Failed to resolve question_id %d to post_id", question_id)
        return None


async def _ensure_post_id(input_id: int) -> int | None:
    """Resolve any Metaculus ID to a post_id.

    Successful results are cached. Failures are NOT cached so transient
    errors (429 rate limits) don't permanently break CP history lookups.
    Uses MetaculusClient.fetch_post_json which has built-in retry logic.
    """
    if input_id in _post_id_cache:
        return _post_id_cache[input_id]

    client = get_metaculus_client()

    # Try as post_id first (most common case) — uses retry
    try:
        post_json = await client.fetch_post_json(input_id)
        q = post_json.get("question", {})
        question_id = q.get("id")
        if question_id is None or question_id == input_id:
            _post_id_cache[input_id] = input_id
            return input_id
        # input_id collided with a different post — fall through
    except Exception:
        pass

    # Try resolving as question_id
    resolved = await _resolve_question_to_post_id(input_id)
    if resolved is not None:
        _post_id_cache[input_id] = resolved
    return resolved


async def _fetch_aggregation(post_id: int) -> AggregationMethod:
    """Fetch CP history from the aggregation_explorer endpoint.

    Works for both open and resolved questions.
    """
    client = get_metaculus_client()
    return await client.fetch_aggregation_history(post_id)


@tool(
    "get_cp_history",
    (
        "Fetch historical community prediction (CP) data for a question. "
        "ESSENTIAL for meta-prediction questions ('Will CP be above X%?') — "
        "shows CP trajectory over time to predict future movements. "
        "Also useful for checking consensus shifts on any question. "
        "Pass any Metaculus ID (question_id or post_id) — auto-detected. "
        "Note: Returns the UNDERLYING question's CP, not the meta-question's own CP.\n\n"
        "Examples:\n"
        "  get_cp_history(question_id=41906) → last 30 days of CP\n"
        "  get_cp_history(question_id=41906, days=90) → last 90 days\n"
        "For meta-predictions: pass the UNDERLYING question's ID (from the meta-question's description), "
        "not the meta-question's own ID."
    ),
    CPHistoryInput.model_json_schema(),
)
@tracked("get_cp_history")
async def get_cp_history(args: dict[str, Any]) -> dict[str, Any]:
    """Fetch community prediction history for a question."""
    try:
        validated = CPHistoryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    input_id = validated.question_id
    days = min(validated.days, 365)

    cutoff_dt = None
    cutoff_date = retrodict_cutoff.get()
    if cutoff_date is not None:
        cutoff_dt = datetime.combine(cutoff_date, datetime.min.time()).replace(
            tzinfo=timezone.utc
        )

    post_id = await _ensure_post_id(input_id)
    if post_id is None:
        return mcp_error(f"Could not resolve ID {input_id} to a valid post.")

    try:
        aggregation = await _fetch_aggregation(post_id)
        response = _build_cp_history_response(aggregation, input_id, days, cutoff_dt)
        return mcp_success(response.model_dump())
    except Exception as e:
        logger.exception("Failed to fetch CP history for post %d", post_id)
        return mcp_error(f"Failed to fetch CP history: {e}")


# --- Pure Search Tools (Raw Results, No LLM Summarization) ---


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
        async with _search_semaphore():
            formatted = await exa_search(
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

    @with_retry(max_attempts=3)
    async def _search() -> str:
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
            hot_response = await ask.news.search_news(
                query=query,
                n_articles=min(num_results, 6),
                return_type="both",
                strategy="latest news",
            )

            historical_response = await ask.news.search_news(
                query=query,
                n_articles=num_results,
                return_type="both",
                strategy="news knowledge",
            )

        # Deduplicate by article_id, preserving order
        seen: set[str] = set()
        all_articles = []
        for articles in (hot_response.as_dicts, historical_response.as_dicts):
            if not articles:
                continue
            for article in articles:
                aid = str(article.article_id)
                if aid not in seen:
                    seen.add(aid)
                    all_articles.append(article)

        all_articles.sort(key=lambda a: a.pub_date, reverse=True)

        if not all_articles:
            return "No articles were found.\n"

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

        return formatted

    try:
        async with _search_semaphore():
            results = await _search()
        return mcp_success({"query": query, "results": results})
    except Exception as e:
        logger.exception("News search failed")
        return mcp_error(f"News search failed: {e}")


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
            async with _search_semaphore():
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
                        logger.debug("Skipping %s: %s", result["title"], e)
                        continue
                if not historical_results and results:
                    return mcp_error(
                        f"No Wikipedia articles found for '{query}'."
                    )
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
                async with _search_semaphore():
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
            async with _search_semaphore():
                result = await _fetch()
            if validated.prompt:
                result["extract"] = await extract_with_prompt(
                    result["extract"], validated.prompt, result["url"]
                )
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
    PredictionHistoryInput.model_json_schema(),
)
@tracked("get_prediction_history")
async def get_prediction_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get past forecasts for a question from local storage."""
    try:
        validated = PredictionHistoryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    post_id = validated.post_id
    cutoff = retrodict_cutoff.get()

    try:
        forecasts = load_past_forecasts(post_id)

        if cutoff is not None:
            cutoff_str = cutoff.isoformat()
            forecasts = [f for f in forecasts if f.timestamp < cutoff_str]

        if not forecasts:
            return mcp_success({"post_id": post_id, "forecasts": [], "count": 0})

        # Convert to serializable format
        results = []
        for f in forecasts:
            result: dict[str, Any] = {
                "timestamp": f.timestamp,
                "question_type": f.question_type,
                "summary": f.summary,
            }
            if cutoff is None:
                result["resolution"] = f.resolution

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

_OPTIONAL_FORECASTING_TOOLS: list[SdkMcpTool[Any]] = []

# Wikipedia (no API key required)
_OPTIONAL_FORECASTING_TOOLS.append(wikipedia)

if settings.exa_api_key:
    _OPTIONAL_FORECASTING_TOOLS.append(search_exa)
else:
    logger.info("search_exa tool disabled: EXA_API_KEY not configured")

if settings.asknews_api_key or (
    settings.asknews_client_id and settings.asknews_client_secret
):
    _OPTIONAL_FORECASTING_TOOLS.append(search_news)
else:
    logger.info("search_news tool disabled: ASKNEWS credentials not configured")


def create_forecasting_server() -> McpSdkServerConfig:
    """Create the forecasting MCP server.

    In retrodict mode, excludes search_exa and search_news (no date filtering).
    """
    tools = list(_BASE_FORECASTING_TOOLS)
    is_retrodict = retrodict_cutoff.get() is not None
    excluded_in_retrodict = (search_exa, search_news)
    for t in _OPTIONAL_FORECASTING_TOOLS:
        if is_retrodict and t in excluded_in_retrodict:
            logger.info("%s excluded in retrodict mode", t.name)
            continue
        tools.append(t)

    return create_mcp_server(
        name="forecasting",
        version="4.0.0",
        tools=tools,
    )


# Default server for backwards compatibility
forecasting_server = create_forecasting_server()
