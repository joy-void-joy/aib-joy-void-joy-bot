"""Prediction market tools for price signals.

These tools fetch current prices from prediction markets to provide
additional signal for forecasting. Market prices reflect aggregated
wisdom of traders with financial incentives.
"""

import json
import logging
from typing import Any, TypedDict

import httpx
from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server

from aib.config import settings
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class MarketQueryInput(BaseModel):
    """Input for market price tools."""

    query: str = Field(min_length=1)
    limit: int = Field(default=settings.market_default_limit, ge=1, le=50)


# --- Output Schemas ---


class MarketPrice(TypedDict):
    """Price information from a prediction market."""

    market_title: str
    probability: float  # 0-1, derived from price
    volume: float | None  # Trading volume if available
    url: str
    source: str  # "polymarket" or "manifold"


# --- Polymarket API ---

POLYMARKET_GAMMA_API = "https://gamma-api.polymarket.com"


@with_retry(max_attempts=3)
async def _search_polymarket(query: str) -> list[dict[str, Any]]:
    """Search Polymarket for markets matching query."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
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


def _parse_yes_price(outcome_prices: Any) -> float | None:
    """Parse YES price from various Polymarket API response formats.

    Args:
        outcome_prices: The outcomePrices field from Polymarket API.
                       Can be a list of floats, strings, or string-encoded lists.

    Returns:
        The parsed YES price (first element) as a float, or None if parsing fails.
    """
    if not outcome_prices:
        return None
    try:
        price_value = outcome_prices[0]
        if isinstance(price_value, (int, float)):
            return float(price_value)
        if isinstance(price_value, str):
            # Handle string representation of list (API sometimes returns this)
            if price_value.startswith("["):
                parsed = json.loads(price_value.replace("'", '"'))
                return float(parsed[0]) if parsed else None
            return float(price_value)
        return None
    except (ValueError, TypeError, json.JSONDecodeError, IndexError, KeyError):
        return None


def parse_polymarket_event(event: dict[str, Any]) -> MarketPrice | None:
    """Parse a Polymarket event into a MarketPrice.

    Args:
        event: Raw event dict from Polymarket API

    Returns:
        MarketPrice if the event has valid market data, None otherwise.
        Returns None instead of falling back to 0.5 when price parsing fails.
    """
    markets = event.get("markets", [])
    if not markets:
        return None

    market = markets[0]
    outcome_prices = market.get("outcomePrices", [])

    yes_price = _parse_yes_price(outcome_prices)
    if yes_price is None:
        logger.warning(
            "Could not parse outcomePrices for event %s: %s",
            event.get("slug", "unknown"),
            outcome_prices,
        )
        return None

    return {
        "market_title": event.get("title", "Unknown"),
        "probability": yes_price,
        "volume": market.get("volume"),
        "url": f"https://polymarket.com/event/{event.get('slug', '')}",
        "source": "polymarket",
    }


@tool(
    "polymarket_price",
    (
        "Search Polymarket for prediction markets and return current prices. "
        "Returns YES price as probability, trading volume, and URL. "
        f"Optional limit (default: {settings.market_default_limit})."
    ),
    {"query": str, "limit": int},
)
@tracked("polymarket_price")
async def polymarket_price(args: dict[str, Any]) -> dict[str, Any]:
    """Search Polymarket and return market prices."""
    try:
        validated = MarketQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    limit = validated.limit

    try:
        events = await _search_polymarket(query)

        if not events:
            return mcp_success({"markets": [], "query": query})

        results: list[MarketPrice] = []
        for event in events[:limit]:
            parsed = parse_polymarket_event(event)
            if parsed is not None:
                results.append(parsed)

        return mcp_success({"markets": results, "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Polymarket API error")
        return mcp_error(f"Polymarket API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Polymarket search failed")
        return mcp_error(f"Polymarket search failed: {e}")


# --- Manifold Markets API ---

MANIFOLD_API = "https://api.manifold.markets/v0"


@with_retry(max_attempts=3)
async def _search_manifold(query: str) -> list[dict[str, Any]]:
    """Search Manifold Markets for markets matching query."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
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


def parse_manifold_market(market: dict[str, Any]) -> MarketPrice:
    """Parse a Manifold market into a MarketPrice.

    Args:
        market: Raw market dict from Manifold API

    Returns:
        MarketPrice with parsed data
    """
    return {
        "market_title": market.get("question", "Unknown"),
        "probability": market.get("probability", 0.5),
        "volume": market.get("volume"),
        "url": market.get("url", f"https://manifold.markets/{market.get('slug', '')}"),
        "source": "manifold",
    }


@tool(
    "manifold_price",
    (
        "Search Manifold Markets for prediction markets and return current prices. "
        "Returns probability, trading volume (in mana), and URL. "
        f"Optional limit (default: {settings.market_default_limit})."
    ),
    {"query": str, "limit": int},
)
@tracked("manifold_price")
async def manifold_price(args: dict[str, Any]) -> dict[str, Any]:
    """Search Manifold Markets and return market prices."""
    try:
        validated = MarketQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    limit = validated.limit

    try:
        markets = await _search_manifold(query)

        if not markets:
            return mcp_success({"markets": [], "query": query})

        results: list[MarketPrice] = [parse_manifold_market(m) for m in markets[:limit]]

        return mcp_success({"markets": results, "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Manifold API error")
        return mcp_error(f"Manifold API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Manifold search failed")
        return mcp_error(f"Manifold search failed: {e}")


# --- MCP Server ---

markets_server = create_mcp_server(
    name="markets",
    version="1.0.0",
    tools=[
        polymarket_price,
        manifold_price,
    ],
)
