"""Forecasting research tools - pure capabilities without LLM calls.

These tools are exposed as an in-process MCP server for the forecasting agent.
All tools return raw data; Claude does the reasoning.
"""

import json
import logging
from asyncio import Semaphore
from typing import Any, Required, TypedDict

import httpx
from claude_agent_sdk import create_sdk_mcp_server, tool

from forecasting_tools import (
    ApiFilter,
    BinaryQuestion,
    MetaculusApi,
)
from forecasting_tools.ai_models.exa_searcher import ExaSearcher
from forecasting_tools.helpers.asknews_searcher import AskNewsSearcher

from aib.config import settings
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)

# Rate limiting semaphores
_metaculus_semaphore = Semaphore(settings.metaculus_max_concurrent)
_search_semaphore = Semaphore(settings.search_max_concurrent)


# --- Input Schemas ---


class SearchExaInput(TypedDict, total=False):
    query: Required[str]
    num_results: int


class SearchNewsInput(TypedDict, total=False):
    query: Required[str]
    num_results: int


class MetaculusQuestionInput(TypedDict):
    post_id: int


class ListTournamentQuestionsInput(TypedDict, total=False):
    tournament_id: Required[int | str]
    num_questions: int


class SearchMetaculusInput(TypedDict, total=False):
    query: Required[str]
    num_results: int


class CommunityPredictionInput(TypedDict):
    post_id: int


class CoherenceLinksInput(TypedDict):
    post_id: int


class SearchWikipediaInput(TypedDict, total=False):
    query: Required[str]
    num_results: int


# --- Helper ---


def _success(result: Any) -> dict[str, Any]:
    """Return successful MCP response with JSON-encoded result."""
    return {"content": [{"type": "text", "text": json.dumps(result, default=str)}]}


def _error(message: str) -> dict[str, Any]:
    """Return error MCP response."""
    return {"content": [{"type": "text", "text": message}], "is_error": True}


# --- Pure Data Tools (Metaculus API) ---


@tool(
    "get_metaculus_question",
    "Fetch details about a Metaculus question including title, description, resolution criteria, and fine print.",
    {"post_id": int},
)
async def get_metaculus_question(args: MetaculusQuestionInput) -> dict[str, Any]:
    """Fetch Metaculus question details."""
    post_id = args["post_id"]

    @with_retry(max_attempts=3)
    async def _fetch() -> dict[str, object]:
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
        }

        if hasattr(question, "options"):
            result["options"] = getattr(question, "options", None)
        if hasattr(question, "lower_bound"):
            result["lower_bound"] = getattr(question, "lower_bound", None)
        if hasattr(question, "upper_bound"):
            result["upper_bound"] = getattr(question, "upper_bound", None)

        return result

    try:
        async with _metaculus_semaphore:
            result = await _fetch()
        return _success(result)
    except Exception as e:
        logger.exception("Failed to fetch Metaculus question")
        return _error(f"Failed to fetch question: {e}")


@tool(
    "list_tournament_questions",
    (
        "List open questions from a specific Metaculus tournament. "
        "Common IDs: 32916 (AIB Spring 2026), 'minibench' (MiniBench), 32921 (Metaculus Cup). "
        f"Optional num_questions (default: {settings.tournament_default_limit})."
    ),
    {"tournament_id": int, "num_questions": int},
)
async def list_tournament_questions(
    args: ListTournamentQuestionsInput,
) -> dict[str, Any]:
    """List questions from a tournament."""
    tournament_id = args["tournament_id"]
    num_questions = args.get("num_questions", settings.tournament_default_limit)

    try:
        questions = MetaculusApi.get_all_open_questions_from_tournament(tournament_id)
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

        return _success(results)
    except Exception as e:
        logger.exception("Failed to list tournament questions")
        return _error(f"Failed to list questions: {e}")


@tool(
    "search_metaculus",
    (
        "Search Metaculus questions by text query. Returns matching questions with IDs, titles, and types. "
        f"Optional num_results (default: {settings.metaculus_default_limit})."
    ),
    {"query": str, "num_results": int},
)
async def search_metaculus(args: SearchMetaculusInput) -> dict[str, Any]:
    """Search Metaculus questions by text."""
    query = args["query"]
    num_results = args.get("num_results", settings.metaculus_default_limit)

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
        return _success(results)
    except Exception as e:
        logger.exception("Metaculus search failed")
        return _error(f"Search failed: {e}")


@tool(
    "get_community_prediction",
    "Get the current community prediction for a Metaculus question. Returns the aggregated forecast from other predictors.",
    {"post_id": int},
)
async def get_community_prediction(args: CommunityPredictionInput) -> dict[str, Any]:
    """Fetch community prediction for a question."""
    post_id = args["post_id"]
    try:
        question = MetaculusApi.get_question_by_post_id(post_id)
        if isinstance(question, list):
            question = question[0]

        community_pred = (
            question.community_prediction_at_access_time
            if isinstance(question, BinaryQuestion)
            else None
        )
        result = {
            "post_id": question.id_of_post,
            "title": question.question_text,
            "type": question.get_question_type(),
            "community_prediction": community_pred,
            "num_forecasters": question.num_forecasters,
        }

        return _success(result)
    except Exception as e:
        logger.exception("Failed to fetch community prediction")
        return _error(f"Failed to fetch prediction: {e}")


@tool(
    "get_coherence_links",
    "Get questions related to this one via coherence links. Used for consistency checking between related forecasts.",
    {"post_id": int},
)
async def get_coherence_links(args: CoherenceLinksInput) -> dict[str, Any]:
    """Fetch coherence links for a question."""
    post_id = args["post_id"]
    try:
        from forecasting_tools.helpers.metaculus_client import MetaculusClient

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
        return _success(results)
    except Exception as e:
        logger.exception("Failed to fetch coherence links")
        return _error(f"Failed to fetch links: {e}")


# --- Pure Search Tools (Raw Results, No LLM Summarization) ---


@tool(
    "search_exa",
    (
        "Search the web using Exa AI-powered search. Returns raw results with titles, URLs, and snippets. "
        f"Optional num_results (default: {settings.search_default_limit})."
    ),
    {"query": str, "num_results": int},
)
async def search_exa(args: SearchExaInput) -> dict[str, Any]:
    """Search using Exa and return raw results."""
    query = args["query"]
    num_results = args.get("num_results", settings.search_default_limit)

    @with_retry(max_attempts=3)
    async def _search() -> list[dict[str, Any]]:
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

    try:
        async with _search_semaphore:
            formatted = await _search()
        return _success(formatted)
    except Exception as e:
        logger.exception("Exa search failed")
        return _error(f"Search failed: {e}")


@tool(
    "search_news",
    (
        "Search for recent news using AskNews API. Returns raw news results with headlines, sources, and summaries. "
        f"Optional num_results (default: {settings.news_default_limit})."
    ),
    {"query": str, "num_results": int},
)
async def search_news(args: SearchNewsInput) -> dict[str, Any]:
    """Search news using AskNews and return raw results."""
    query = args["query"]
    # TODO: forecasting-tools AskNewsSearcher doesn't support num_results.
    # To fix, either use raw AskNews SDK or contribute upstream.
    # See to_port/main_with_no_framework.py call_asknews() for SDK usage.
    _ = args.get("num_results", settings.news_default_limit)

    @with_retry(max_attempts=3)
    async def _search() -> str:
        searcher = AskNewsSearcher()
        return await searcher.get_formatted_news_async(query)

    try:
        async with _search_semaphore:
            results = await _search()
        return _success({"query": query, "results": results})
    except Exception as e:
        logger.exception("News search failed")
        return _error(f"News search failed: {e}")


# Wikipedia API base URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


@tool(
    "search_wikipedia",
    (
        "Search Wikipedia for articles matching a query. Returns article titles, snippets, and URLs. "
        "Useful for finding base rates, historical data, and reference classes. "
        f"Optional num_results (default: {settings.search_default_limit})."
    ),
    {"query": str, "num_results": int},
)
async def search_wikipedia(args: SearchWikipediaInput) -> dict[str, Any]:
    """Search Wikipedia and return article summaries."""
    query = args["query"]
    num_results = args.get("num_results", settings.search_default_limit)

    @with_retry(max_attempts=3)
    async def _search() -> list[dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            # Search for pages
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
                snippet = snippet.replace("<span class=\"searchmatch\">", "")
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
        return _success({"query": query, "results": results})
    except Exception as e:
        logger.exception("Wikipedia search failed")
        return _error(f"Wikipedia search failed: {e}")


# --- Create MCP Server ---

forecasting_server = create_sdk_mcp_server(
    name="forecasting",
    version="2.0.0",
    tools=[
        # Metaculus data tools
        get_metaculus_question,
        list_tournament_questions,
        search_metaculus,
        get_community_prediction,  # Not available in AIB, but useful for other tournaments
        get_coherence_links,
        # Search tools (raw results)
        search_exa,
        search_news,
        search_wikipedia,
    ],
)
