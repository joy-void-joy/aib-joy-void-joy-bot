"""Prediction market tools for price signals.

These tools fetch current prices from prediction markets to provide
additional signal for forecasting. Market prices reflect aggregated
wisdom of traders with financial incentives.
"""

import json
import logging
from typing import Any, Required, TypedDict

import httpx
from claude_agent_sdk import create_sdk_mcp_server, tool

from aib.config import settings
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class MarketQueryInput(TypedDict, total=False):
    """Input for market price tools."""

    query: Required[str]
    limit: int


# --- Output Schemas ---


class MarketPrice(TypedDict):
    """Price information from a prediction market."""

    market_title: str
    probability: float  # 0-1, derived from price
    volume: float | None  # Trading volume if available
    url: str
    source: str  # "polymarket" or "manifold"


# --- Helper ---


def _success(result: Any) -> dict[str, Any]:
    """Return successful MCP response with JSON-encoded result."""
    return {"content": [{"type": "text", "text": json.dumps(result, default=str)}]}


def _error(message: str) -> dict[str, Any]:
    """Return error MCP response."""
    return {"content": [{"type": "text", "text": message}], "is_error": True}


# --- Polymarket API ---

POLYMARKET_GAMMA_API = "https://gamma-api.polymarket.com"


@with_retry(max_attempts=3)
async def _search_polymarket(query: str) -> list[dict[str, Any]]:
    """Search Polymarket for markets matching query."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{POLYMARKET_GAMMA_API}/events",
            params={
                "title_contains": query,
                "active": "true",
                "limit": 10,
            },
        )
        response.raise_for_status()
        return response.json()


@tool(
    "polymarket_price",
    (
        "Search Polymarket for prediction markets and return current prices. "
        "Returns YES price as probability, trading volume, and URL. "
        f"Optional limit (default: {settings.market_default_limit})."
    ),
    {"query": str, "limit": int},
)
async def polymarket_price(args: MarketQueryInput) -> dict[str, Any]:
    """Search Polymarket and return market prices."""
    query = args["query"]
    limit = args.get("limit", settings.market_default_limit)

    try:
        events = await _search_polymarket(query)

        if not events:
            return _success({"markets": [], "query": query})

        results: list[MarketPrice] = []
        for event in events[:limit]:
            markets = event.get("markets", [])
            if not markets:
                continue

            market = markets[0]
            outcome_prices = market.get("outcomePrices", [])
            yes_price = float(outcome_prices[0]) if outcome_prices else 0.5

            results.append(
                {
                    "market_title": event.get("title", "Unknown"),
                    "probability": yes_price,
                    "volume": market.get("volume"),
                    "url": f"https://polymarket.com/event/{event.get('slug', '')}",
                    "source": "polymarket",
                }
            )

        return _success({"markets": results, "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Polymarket API error")
        return _error(f"Polymarket API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Polymarket search failed")
        return _error(f"Polymarket search failed: {e}")


# --- Manifold Markets API ---

MANIFOLD_API = "https://api.manifold.markets/v0"


@with_retry(max_attempts=3)
async def _search_manifold(query: str) -> list[dict[str, Any]]:
    """Search Manifold Markets for markets matching query."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{MANIFOLD_API}/search-markets",
            params={
                "term": query,
                "limit": 10,
                "filter": "open",
                "sort": "score",
            },
        )
        response.raise_for_status()
        return response.json()


@tool(
    "manifold_price",
    (
        "Search Manifold Markets for prediction markets and return current prices. "
        "Returns probability, trading volume (in mana), and URL. "
        f"Optional limit (default: {settings.market_default_limit})."
    ),
    {"query": str, "limit": int},
)
async def manifold_price(args: MarketQueryInput) -> dict[str, Any]:
    """Search Manifold Markets and return market prices."""
    query = args["query"]
    limit = args.get("limit", settings.market_default_limit)

    try:
        markets = await _search_manifold(query)

        if not markets:
            return _success({"markets": [], "query": query})

        results: list[MarketPrice] = []
        for market in markets[:limit]:
            probability = market.get("probability", 0.5)
            volume = market.get("volume")

            results.append(
                {
                    "market_title": market.get("question", "Unknown"),
                    "probability": probability,
                    "volume": volume,
                    "url": market.get(
                        "url", f"https://manifold.markets/{market.get('slug', '')}"
                    ),
                    "source": "manifold",
                }
            )

        return _success({"markets": results, "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Manifold API error")
        return _error(f"Manifold API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Manifold search failed")
        return _error(f"Manifold search failed: {e}")


# --- MCP Server ---

markets_server = create_sdk_mcp_server(
    name="markets",
    version="1.0.0",
    tools=[
        polymarket_price,
        manifold_price,
    ],
)
