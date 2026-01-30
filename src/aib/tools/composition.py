"""Composition tools for parallel research, market search, and sub-forecasting.

These tools enable the main forecasting agent to:
- Run multiple research queries in parallel
- Run multiple market searches in parallel
- Decompose questions and forecast sub-questions in parallel
"""

import asyncio
import json
import logging
import statistics
from typing import Any, TypedDict

from claude_agent_sdk import create_sdk_mcp_server, tool

from forecasting_tools.ai_models.exa_searcher import ExaSearcher
from forecasting_tools.helpers.asknews_searcher import AskNewsSearcher

from aib.tools.markets import _search_manifold, _search_polymarket

logger = logging.getLogger(__name__)


# --- Run Forecast Reference (set by core.py) ---

# Reference to run_forecast function - set by core.py to avoid circular import
_run_forecast_fn: Any = None


def set_run_forecast_fn(fn: Any) -> None:
    """Set the run_forecast function reference.

    Called by core.py after run_forecast is defined to enable
    spawn_subquestions to recursively call the forecasting agent.
    """
    global _run_forecast_fn
    _run_forecast_fn = fn


# --- Input Schemas ---


class ResearchTask(TypedDict):
    """A single research task for parallel execution."""

    query: str
    source: str  # "exa" or "news"


class ParallelResearchInput(TypedDict):
    """Input for parallel_research tool."""

    tasks: list[ResearchTask]


class SubQuestion(TypedDict):
    """A sub-question for parallel forecasting."""

    question: str
    context: str  # How this relates to the parent question
    weight: float  # Weight in final aggregation (0-1)


class SpawnSubquestionsInput(TypedDict):
    """Input for spawn_subquestions tool."""

    subquestions: list[SubQuestion]
    aggregation_method: str  # "weighted_average", "geometric_mean", "median", "all"


class MarketTask(TypedDict):
    """A single market search task for parallel execution."""

    query: str
    source: str  # "polymarket" or "manifold"


class ParallelMarketSearchInput(TypedDict):
    """Input for parallel_market_search tool."""

    tasks: list[MarketTask]


# --- Output Schemas ---


class ResearchResult(TypedDict):
    """Result from a single research task."""

    query: str
    source: str
    results: list[dict[str, Any]]
    error: str | None


class SubForecastResult(TypedDict):
    """Result from a single sub-forecast."""

    question: str
    probability: float
    reasoning: str
    weight: float


class AggregatedResult(TypedDict):
    """Aggregated result from spawn_subquestions."""

    subforecasts: list[SubForecastResult]
    weighted_average: float
    geometric_mean: float
    median: float


class MarketSearchResult(TypedDict):
    """Result from a single market search task."""

    query: str
    source: str
    markets: list[dict[str, Any]]
    error: str | None


# --- Helper Functions ---


async def _run_exa_search(query: str, num_results: int = 10) -> list[dict[str, Any]]:
    """Run a single Exa search."""
    searcher = ExaSearcher(
        include_text=True,
        include_highlights=True,
        num_results=num_results,
    )
    results = await searcher.invoke(query)

    formatted = []
    for r in results:
        formatted.append(
            {
                "title": r.title,
                "url": r.url,
                "snippet": r.text[:500] if r.text else None,
                "highlights": r.highlights[:3] if r.highlights else None,
                "published_date": str(r.published_date) if r.published_date else None,
            }
        )
    return formatted


async def _run_news_search(query: str) -> str:
    """Run a single news search."""
    searcher = AskNewsSearcher()
    return await searcher.get_formatted_news_async(query)


# --- Tools ---


@tool(
    "parallel_research",
    (
        "Run multiple search queries in parallel. Each task specifies a query and "
        "source ('exa' for web search, 'news' for recent news). Returns all results "
        "together for efficient batch research."
    ),
    ParallelResearchInput,
)
async def parallel_research(args: ParallelResearchInput) -> dict[str, Any]:
    """Run multiple research tasks concurrently."""
    tasks = args["tasks"]

    if not tasks:
        return {
            "content": [{"type": "text", "text": "No research tasks provided"}],
            "is_error": True,
        }

    async def run_task(task: ResearchTask) -> ResearchResult:
        """Execute a single research task."""
        query = task["query"]
        source = task["source"]

        try:
            if source == "exa":
                results = await _run_exa_search(query)
                return {
                    "query": query,
                    "source": source,
                    "results": results,
                    "error": None,
                }
            elif source == "news":
                # News returns formatted string, wrap in list
                news_result = await _run_news_search(query)
                return {
                    "query": query,
                    "source": source,
                    "results": [{"formatted_news": news_result}],
                    "error": None,
                }
            else:
                return {
                    "query": query,
                    "source": source,
                    "results": [],
                    "error": f"Unknown source: {source}",
                }
        except Exception as e:
            logger.exception("Research task failed: %s", query)
            return {
                "query": query,
                "source": source,
                "results": [],
                "error": str(e),
            }

    # Run all tasks concurrently
    results = await asyncio.gather(*[run_task(t) for t in tasks])

    return {
        "content": [{"type": "text", "text": json.dumps(list(results), default=str)}]
    }


@tool(
    "parallel_market_search",
    (
        "Search multiple prediction markets in parallel. Each task specifies a query and "
        "source ('polymarket' or 'manifold'). Returns all market results together for "
        "efficient batch lookups. Use this when you need to check multiple related markets."
    ),
    ParallelMarketSearchInput,
)
async def parallel_market_search(args: ParallelMarketSearchInput) -> dict[str, Any]:
    """Run multiple market search tasks concurrently."""
    tasks = args["tasks"]

    if not tasks:
        return {
            "content": [{"type": "text", "text": "No market tasks provided"}],
            "is_error": True,
        }

    async def run_task(task: MarketTask) -> MarketSearchResult:
        """Execute a single market search task."""
        query = task["query"]
        source = task["source"]

        try:
            if source == "polymarket":
                events = await _search_polymarket(query)
                markets = []
                for event in events[:5]:
                    event_markets = event.get("markets", [])
                    if not event_markets:
                        continue
                    market = event_markets[0]
                    outcome_prices = market.get("outcomePrices", [])
                    yes_price = float(outcome_prices[0]) if outcome_prices else 0.5
                    markets.append(
                        {
                            "title": event.get("title", "Unknown"),
                            "probability": yes_price,
                            "volume": market.get("volume"),
                            "url": f"https://polymarket.com/event/{event.get('slug', '')}",
                        }
                    )
                return {
                    "query": query,
                    "source": source,
                    "markets": markets,
                    "error": None,
                }
            elif source == "manifold":
                raw_markets = await _search_manifold(query)
                markets = []
                for m in raw_markets[:5]:
                    markets.append(
                        {
                            "title": m.get("question", "Unknown"),
                            "probability": m.get("probability", 0.5),
                            "volume": m.get("volume"),
                            "url": m.get(
                                "url", f"https://manifold.markets/{m.get('slug', '')}"
                            ),
                        }
                    )
                return {
                    "query": query,
                    "source": source,
                    "markets": markets,
                    "error": None,
                }
            else:
                return {
                    "query": query,
                    "source": source,
                    "markets": [],
                    "error": f"Unknown source: {source}. Use 'polymarket' or 'manifold'.",
                }
        except Exception as e:
            logger.exception("Market search task failed: %s", query)
            return {
                "query": query,
                "source": source,
                "markets": [],
                "error": str(e),
            }

    # Run all tasks concurrently
    results = await asyncio.gather(*[run_task(t) for t in tasks])

    return {
        "content": [{"type": "text", "text": json.dumps(list(results), default=str)}]
    }


def _error_response(message: str) -> dict[str, Any]:
    """Return error MCP response."""
    return {"content": [{"type": "text", "text": message}], "is_error": True}


@tool(
    "spawn_subquestions",
    (
        "Decompose a forecasting question into sub-questions and forecast each in "
        "parallel. Each sub-question gets its own forecasting agent with full research "
        "capabilities. Returns individual forecasts plus aggregated probabilities. "
        "Use when a question naturally breaks into independent parts. "
        "Sub-forecasts cannot spawn further subquestions (prevents infinite recursion)."
    ),
    SpawnSubquestionsInput,
)
async def spawn_subquestions(args: SpawnSubquestionsInput) -> dict[str, Any]:
    """Spawn parallel sub-forecasters for decomposed questions.

    Recursively calls run_forecast() for each sub-question with allow_spawn=False
    to prevent infinite recursion.
    """
    if _run_forecast_fn is None:
        return _error_response(
            "run_forecast not configured - call set_run_forecast_fn first"
        )

    subquestions = args["subquestions"]
    aggregation_method = args.get("aggregation_method", "weighted_average")

    if not subquestions:
        return _error_response("No subquestions provided")

    # Validate weights
    total_weight = sum(sq["weight"] for sq in subquestions)
    if abs(total_weight - 1.0) > 0.01:
        return _error_response(f"Weights must sum to 1.0, got {total_weight}")

    async def run_subforecast(sq: SubQuestion) -> dict[str, Any]:
        """Execute a single sub-forecast."""
        # Build context for the sub-question
        context = {
            "title": sq["question"],
            "type": "binary",  # Sub-questions are binary by default
            "description": sq["context"],
            "resolution_criteria": "",
            "fine_print": "",
        }
        try:
            result = await _run_forecast_fn(
                question_context=context,
                allow_spawn=False,  # Prevent infinite recursion
            )
            return {
                "question": sq["question"],
                "probability": result.probability,
                "summary": result.summary,
                "weight": sq["weight"],
                "error": None,
            }
        except Exception as e:
            logger.exception("Sub-forecast failed: %s", sq["question"])
            return {
                "question": sq["question"],
                "probability": None,
                "summary": None,
                "weight": sq["weight"],
                "error": str(e),
            }

    # Run all sub-forecasts in parallel
    results = await asyncio.gather(*[run_subforecast(sq) for sq in subquestions])

    # Filter successful results for aggregation
    successful = [r for r in results if r["probability"] is not None]
    errors = [r for r in results if r["error"] is not None]

    if not successful:
        error_msgs = [e["error"] for e in errors]
        return _error_response(f"All sub-forecasts failed: {error_msgs}")

    # Aggregate probabilities
    probabilities = [r["probability"] for r in successful]
    weights = [r["weight"] for r in successful]

    # Re-normalize weights if some forecasts failed
    if len(successful) < len(subquestions):
        total = sum(weights)
        weights = [w / total for w in weights]

    aggregated = aggregate_probabilities(probabilities, weights, aggregation_method)

    output = {
        "subforecasts": list(results),
        "aggregated_probability": aggregated,
        "aggregation_method": aggregation_method,
        "successful_count": len(successful),
        "failed_count": len(errors),
    }

    return {"content": [{"type": "text", "text": json.dumps(output, default=str)}]}


def aggregate_probabilities(
    probabilities: list[float],
    weights: list[float],
    method: str = "weighted_average",
) -> float:
    """Aggregate sub-forecast probabilities.

    Args:
        probabilities: List of probability estimates (0-1)
        weights: Corresponding weights (must sum to 1)
        method: Aggregation method

    Returns:
        Aggregated probability
    """
    if method == "weighted_average":
        return sum(p * w for p, w in zip(probabilities, weights, strict=True))
    elif method == "geometric_mean":
        # Geometric mean: product^(1/n), but weighted
        # Use log transform for numerical stability
        import math

        log_probs = [
            math.log(p) * w for p, w in zip(probabilities, weights, strict=True)
        ]
        return math.exp(sum(log_probs))
    elif method == "median":
        return statistics.median(probabilities)
    else:
        raise ValueError(f"Unknown aggregation method: {method}")


# --- MCP Server ---

composition_server = create_sdk_mcp_server(
    name="composition",
    version="1.0.0",
    tools=[
        parallel_research,
        parallel_market_search,
        spawn_subquestions,
    ],
)
