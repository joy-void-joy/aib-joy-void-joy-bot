"""Prediction market and Metaculus platform tools.

Prediction market tools fetch current prices from Polymarket, Manifold, and
Kalshi to provide additional signal for forecasting.

Metaculus tools provide direct API access to the Metaculus forecasting platform:
question details, tournament listings, search, coherence links, and CP history.
"""

import ast
import asyncio
import logging
from datetime import date, datetime, time, timedelta, timezone
from typing import Annotated, Any, TypedDict

import httpx
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query, tool
from claude_agent_sdk.types import McpSdkServerConfig
from pydantic import BaseModel, Field, field_validator

from metaculus import ApiFilter, BinaryQuestion
from metaculus.models import AggregationMethod

from aib.clients.metaculus import get_client as get_metaculus_client
from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.cache import cached
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class MarketQueryInput(BaseModel):
    """Input for market price tools."""

    query: str = Field(min_length=1)
    limit: int = Field(default=settings.market_default_limit, ge=1, le=50)


class KalshiEventInput(BaseModel):
    """Input for fetching a single Kalshi event with all its markets."""

    event_ticker: str = Field(min_length=1)


# --- Output Schemas ---


class MarketPrice(TypedDict):
    """Price information from a prediction market."""

    market_title: str
    probability: float  # 0-1, derived from price
    volume: float | None  # Trading volume if available
    url: str
    source: str  # "polymarket", "manifold", or "kalshi"
    description: str | None  # Resolution criteria / market description


class KalshiMarketPrice(MarketPrice):
    """Kalshi market price with ticker identifiers for drill-down.

    Use event_ticker with kalshi_event to get all bracket markets.
    Use market_ticker with kalshi_history for historical prices.
    """

    market_ticker: str
    event_ticker: str
    rules_primary: str | None  # Kalshi resolution rules


class KalshiEventMarket(TypedDict):
    """A single bracket market within a Kalshi event."""

    ticker: str
    title: str
    probability: float
    volume: float | None
    strike_type: str | None  # "greater", "less", "between", etc.
    floor_strike: float | None
    cap_strike: float | None
    url: str
    rules_primary: str | None  # Resolution rules for this bracket


class KalshiEvent(TypedDict):
    """A Kalshi event with its bracket markets."""

    event_ticker: str
    event_title: str
    markets: list[KalshiEventMarket]
    url: str
    description: str | None  # Event description / resolution criteria


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
                       The API sometimes returns the entire field as a string literal.

    Returns:
        The parsed YES price (first element) as a float, or None if parsing fails.
    """
    if not outcome_prices:
        return None

    def _coerce_to_list(value: Any) -> list[Any] | None:
        """Coerce value to list, parsing string literals if needed."""
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            try:
                parsed = ast.literal_eval(value)
                if isinstance(parsed, list):
                    return parsed
                # Single value parsed (e.g., "0.5" -> 0.5)
                return [parsed]
            except (ValueError, SyntaxError):
                # Not a valid literal, treat as single string value
                return [value]
        return None

    def _extract_scalar(value: Any) -> float | int | str | None:
        """Extract a scalar value, unwrapping nested structures."""
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            try:
                parsed = ast.literal_eval(value)
                # Recurse if we got a container
                if isinstance(parsed, list):
                    return _extract_scalar(parsed[0]) if parsed else None
                return parsed if isinstance(parsed, (int, float)) else None
            except (ValueError, SyntaxError):
                # Not a valid literal, return as-is for float() to try
                return value
        if isinstance(value, list) and value:
            return _extract_scalar(value[0])
        return None

    try:
        prices = _coerce_to_list(outcome_prices)
        if not prices:
            return None

        scalar = _extract_scalar(prices[0])
        if scalar is None:
            return None

        return float(scalar)
    except (ValueError, TypeError, IndexError, KeyError):
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
        "description": event.get("description") or market.get("description"),
    }


async def _polymarket_event_at_cutoff(
    event: dict[str, Any],
    cutoff: date,
) -> MarketPrice | None:
    """Get historical price for a Polymarket event at the cutoff date."""
    markets = event.get("markets", [])
    if not markets:
        return None
    market = markets[0]
    token_ids = market.get("clobTokenIds", [])
    if not token_ids:
        return None
    token_id = token_ids[0]
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    start_ts = cutoff_unix - (30 * 24 * 60 * 60)
    try:
        history = await _fetch_polymarket_history(token_id, start_ts, cutoff_unix)
    except Exception:
        return None
    if not history:
        return None
    closest = max(
        (p for p in history if p.get("t", 0) <= cutoff_unix),
        key=lambda p: p.get("t", 0),
        default=None,
    )
    if closest is None:
        return None
    return {
        "market_title": event.get("title", "Unknown"),
        "probability": closest.get("p", 0.5),
        "volume": market.get("volume"),
        "url": f"https://polymarket.com/event/{event.get('slug', '')}",
        "source": "polymarket",
        "description": None,
    }


@tool(
    "polymarket_price",
    (
        "Search Polymarket for prediction markets and return current prices. "
        "Returns YES price as probability, trading volume, and URL. "
        f"Optional limit (default: {settings.market_default_limit}).\n\n"
        "Examples:\n"
        "  polymarket_price(query='US election 2026') → find election markets\n"
        "  polymarket_price(query='Fed rate cut') → find Fed policy markets\n"
        "Check volume before trusting — low-volume markets (<$1k) may be stale."
    ),
    MarketQueryInput.model_json_schema(),
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

    cutoff = retrodict_cutoff.get()

    try:
        events = await _search_polymarket(query)

        if not events:
            return mcp_success({"markets": [], "query": query})

        results: list[MarketPrice] = []
        for event in events[:limit]:
            if cutoff is not None:
                parsed = await _polymarket_event_at_cutoff(event, cutoff)
            else:
                parsed = parse_polymarket_event(event)
            if parsed is not None:
                results.append(parsed)

        if not results and cutoff is not None:
            return mcp_error(
                f"Found markets for '{query}' but no price data is available."
            )

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
        "description": market.get("textDescription") or market.get("description"),
    }


async def _manifold_market_at_cutoff(
    market: dict[str, Any],
    cutoff: date,
) -> MarketPrice | None:
    """Get historical price for a Manifold market at the cutoff date."""
    contract_id = market.get("id")
    if not contract_id:
        return None
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    cutoff_ms = cutoff_unix * 1000
    try:
        bets = await _fetch_manifold_bets(contract_id, cutoff_ms)
    except Exception:
        return None
    if not bets:
        return None
    relevant = max(
        (b for b in bets if b.get("createdTime", 0) <= cutoff_ms),
        key=lambda b: b.get("createdTime", 0),
        default=None,
    )
    if relevant is None:
        return None
    prob = relevant.get("probAfter", relevant.get("probBefore", 0.5))
    return {
        "market_title": market.get("question", "Unknown"),
        "probability": prob,
        "volume": market.get("volume"),
        "url": market.get("url", f"https://manifold.markets/{market.get('slug', '')}"),
        "source": "manifold",
        "description": None,
    }


@tool(
    "manifold_price",
    (
        "Search Manifold Markets for prediction markets and return current prices. "
        "Returns probability, trading volume (in mana), and URL. "
        f"Optional limit (default: {settings.market_default_limit})."
    ),
    MarketQueryInput.model_json_schema(),
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
    cutoff = retrodict_cutoff.get()

    try:
        markets = await _search_manifold(query)

        if not markets:
            return mcp_success({"markets": [], "query": query})

        results: list[MarketPrice] = []
        for m in markets[:limit]:
            if cutoff is not None:
                parsed = await _manifold_market_at_cutoff(m, cutoff)
            else:
                parsed = parse_manifold_market(m)
            if parsed is not None:
                results.append(parsed)

        return mcp_success({"markets": results, "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Manifold API error")
        return mcp_error(f"Manifold API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Manifold search failed")
        return mcp_error(f"Manifold search failed: {e}")


# --- Historical Market APIs (for retrodict mode) ---


class HistoricalPriceInput(BaseModel):
    """Input for historical market price tools."""

    market_id: str = Field(min_length=1)
    timestamp: int = Field(description="Unix timestamp in seconds")


class HistoricalPrice(TypedDict):
    """Historical price at a specific timestamp."""

    market_id: str
    timestamp: int
    probability: float
    source: str


POLYMARKET_CLOB_API = "https://clob.polymarket.com"


@with_retry(max_attempts=3)
async def _fetch_polymarket_history(
    token_id: str, start_ts: int, end_ts: int
) -> list[dict[str, Any]]:
    """Fetch price history from Polymarket CLOB API."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{POLYMARKET_CLOB_API}/prices-history",
            params={
                "market": token_id,
                "startTs": start_ts,
                "endTs": end_ts,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data.get("history", [])


@tool(
    "polymarket_history",
    (
        "Get historical Polymarket price at a specific past timestamp. "
        "USE THIS to see how prediction market sentiment evolved over time — "
        "useful for understanding trend direction. Get the token ID from polymarket_price first, "
        "then query specific timestamps. Returns price closest to but not after the timestamp."
    ),
    HistoricalPriceInput.model_json_schema(),
)
@tracked("polymarket_history")
async def polymarket_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get historical Polymarket price at a timestamp."""
    try:
        validated = HistoricalPriceInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    token_id = validated.market_id
    target_ts = validated.timestamp
    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
        target_ts = min(target_ts, cutoff_unix)

    try:
        # Fetch history around the target timestamp
        # Use a 30-day window before the target
        start_ts = target_ts - (30 * 24 * 60 * 60)
        history = await _fetch_polymarket_history(token_id, start_ts, target_ts)

        if not history:
            return mcp_error(f"No historical data found for market {token_id}")

        # Find the closest price at or before target timestamp
        closest_point = None
        for point in history:
            point_ts = point.get("t", 0)
            if point_ts <= target_ts:
                if closest_point is None or point_ts > closest_point.get("t", 0):
                    closest_point = point

        if closest_point is None:
            return mcp_error(
                f"No price data found before timestamp {target_ts} for market {token_id}"
            )

        result: HistoricalPrice = {
            "market_id": token_id,
            "timestamp": closest_point.get("t", 0),
            "probability": closest_point.get("p", 0.5),
            "source": "polymarket",
        }
        return mcp_success(result)

    except httpx.HTTPStatusError as e:
        logger.exception("Polymarket history API error")
        return mcp_error(f"Polymarket API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Polymarket history lookup failed")
        return mcp_error(f"Polymarket history lookup failed: {e}")


@with_retry(max_attempts=3)
async def _fetch_manifold_bets(
    contract_id: str, before_time: int, limit: int = 1000
) -> list[dict[str, Any]]:
    """Fetch bets from Manifold to reconstruct historical prices."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{MANIFOLD_API}/bets",
            params={
                "contractId": contract_id,
                "beforeTime": before_time,
                "limit": limit,
            },
        )
        response.raise_for_status()
        return response.json()


@tool(
    "manifold_history",
    (
        "Get historical Manifold market price at a specific past timestamp. "
        "USE THIS to track how Manifold probability changed over time. "
        "Get the contract ID from manifold_price first, then query timestamps. "
        "Returns probability just after the last bet before the given timestamp."
    ),
    HistoricalPriceInput.model_json_schema(),
)
@tracked("manifold_history")
async def manifold_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get historical Manifold price at a timestamp."""
    try:
        validated = HistoricalPriceInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    contract_id = validated.market_id
    target_ts = validated.timestamp
    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
        target_ts = min(target_ts, cutoff_unix)
    # Manifold uses milliseconds
    target_ts_ms = target_ts * 1000

    try:
        # Fetch bets before the target time
        bets = await _fetch_manifold_bets(contract_id, target_ts_ms)

        if not bets:
            return mcp_error(f"No bet history found for contract {contract_id}")

        # Bets are returned newest-first, so find the oldest bet
        # that is still before our target time
        # Each bet has probBefore and probAfter - we want probAfter
        # of the most recent bet before our target
        relevant_bet = None
        for bet in bets:
            bet_time = bet.get("createdTime", 0)
            if bet_time <= target_ts_ms:
                if relevant_bet is None or bet_time > relevant_bet.get(
                    "createdTime", 0
                ):
                    relevant_bet = bet

        if relevant_bet is None:
            return mcp_error(
                f"No bets found before timestamp {validated.timestamp} for contract {contract_id}"
            )

        # Use probAfter as the price after this bet
        prob = relevant_bet.get("probAfter", relevant_bet.get("probBefore", 0.5))

        result: HistoricalPrice = {
            "market_id": contract_id,
            "timestamp": relevant_bet.get("createdTime", 0) // 1000,
            "probability": prob,
            "source": "manifold",
        }
        return mcp_success(result)

    except httpx.HTTPStatusError as e:
        logger.exception("Manifold history API error")
        return mcp_error(f"Manifold API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Manifold history lookup failed")
        return mcp_error(f"Manifold history lookup failed: {e}")


# --- Kalshi API ---

KALSHI_API = "https://api.elections.kalshi.com/trade-api/v2"


def _series_ticker_from_market(ticker: str) -> str:
    """Extract series ticker from a market ticker (e.g. 'KXFED' from 'KXFED-26APR')."""
    return ticker.split("-")[0]


def _parse_kalshi_probability(market: dict[str, Any]) -> float | None:
    """Extract probability from a Kalshi market's dollar-string price fields.

    Tries last_price_dollars first (most recent trade), then yes_ask/yes_bid
    midpoint as fallback.
    """
    last_price = market.get("last_price_dollars")
    if last_price is not None:
        try:
            return float(last_price)
        except (ValueError, TypeError):
            pass

    yes_ask = market.get("yes_ask_dollars")
    yes_bid = market.get("yes_bid_dollars")
    if yes_ask is not None and yes_bid is not None:
        try:
            return (float(yes_ask) + float(yes_bid)) / 2.0
        except (ValueError, TypeError):
            pass

    return None


def _kalshi_matches_query(event: dict[str, Any], query_words: list[str]) -> bool:
    """Check if a Kalshi event matches all query words (AND logic, case-insensitive).

    Searches event title, sub_title, and all market yes_sub_title fields.
    """
    text_parts: list[str] = [
        event.get("title", ""),
        event.get("sub_title", ""),
    ]
    for m in event.get("markets", []):
        text_parts.append(m.get("yes_sub_title", ""))
        text_parts.append(m.get("title", ""))
    combined = " ".join(text_parts).lower()
    return all(w in combined for w in query_words)


@with_retry(max_attempts=3)
async def _fetch_kalshi_events(
    query: str, *, status: str | None = "open"
) -> list[dict[str, Any]]:
    """Fetch events from Kalshi API with client-side text filtering."""
    params: dict[str, str | int] = {
        "with_nested_markets": "true",
        "limit": 200,
    }
    if status is not None:
        params["status"] = status
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{KALSHI_API}/events",
            params=params,
        )
        response.raise_for_status()
        data = response.json()
        events: list[dict[str, Any]] = data.get("events", [])

    query_words = query.lower().split()
    return [e for e in events if _kalshi_matches_query(e, query_words)]


@with_retry(max_attempts=3)
async def _fetch_kalshi_event(event_ticker: str) -> dict[str, Any]:
    """Fetch a single Kalshi event with all its markets."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{KALSHI_API}/events/{event_ticker}",
            params={"with_nested_markets": "true"},
        )
        response.raise_for_status()
        return response.json().get("event", {})


@with_retry(max_attempts=3)
async def _fetch_kalshi_candlestick(
    series_ticker: str,
    market_ticker: str,
    start_ts: int,
    end_ts: int,
) -> list[dict[str, Any]]:
    """Fetch candlestick data for a Kalshi market."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{KALSHI_API}/series/{series_ticker}/markets/{market_ticker}/candlesticks",
            params={
                "start_ts": start_ts,
                "end_ts": end_ts,
                "period_interval": 1440,
            },
        )
        response.raise_for_status()
        return response.json().get("candlesticks", [])


async def _kalshi_market_at_cutoff(
    market: dict[str, Any], cutoff: date
) -> float | None:
    """Get historical price for a Kalshi market at the retrodict cutoff.

    Returns None if the market was created after the cutoff or if no
    candlestick data is available.
    """
    created_time = market.get("created_time")
    if created_time:
        try:
            created_dt = datetime.fromisoformat(created_time.replace("Z", "+00:00"))
            cutoff_dt = datetime.combine(cutoff, time())
            if created_dt.replace(tzinfo=None) > cutoff_dt:
                return None
        except (ValueError, TypeError):
            pass

    ticker = market.get("ticker", "")
    series_ticker = _series_ticker_from_market(ticker)
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    start_ts = cutoff_unix - (30 * 24 * 60 * 60)

    try:
        candles = await _fetch_kalshi_candlestick(
            series_ticker, ticker, start_ts, cutoff_unix
        )
    except Exception:
        return None

    if not candles:
        return None

    closest = max(
        (c for c in candles if c.get("end_period_ts", 0) <= cutoff_unix),
        key=lambda c: c.get("end_period_ts", 0),
        default=None,
    )
    if closest is None:
        return None

    close_price = closest.get("price_dollars")
    if close_price is not None:
        try:
            return float(close_price)
        except (ValueError, TypeError):
            pass

    yes_close = closest.get("yes_close_dollars")
    if yes_close is not None:
        try:
            return float(yes_close)
        except (ValueError, TypeError):
            pass

    return None


@tool(
    "kalshi_price",
    (
        "Search Kalshi (CFTC-regulated event contracts exchange) for prediction markets. "
        "Strong coverage of economic/policy events: Fed rate decisions, CPI, GDP, jobs reports. "
        "Returns YES price as probability, trading volume, and URL. "
        f"Optional limit (default: {settings.market_default_limit}).\n\n"
        "Examples:\n"
        "  kalshi_price(query='Fed rate') → find Fed funds rate markets\n"
        "  kalshi_price(query='CPI inflation') → find CPI markets\n"
        "  kalshi_price(query='GDP') → find GDP growth markets\n"
        "Use kalshi_event to drill into bracket markets for numeric distributions."
    ),
    MarketQueryInput.model_json_schema(),
)
@tracked("kalshi_price")
async def kalshi_price(args: dict[str, Any]) -> dict[str, Any]:
    """Search Kalshi and return market prices."""
    try:
        validated = MarketQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    query = validated.query
    limit = validated.limit
    cutoff = retrodict_cutoff.get()

    try:
        if cutoff is not None:
            events = await _fetch_kalshi_events(query, status=None)
        else:
            events = await _fetch_kalshi_events(query, status="open")

        if not events:
            return mcp_success({"markets": [], "query": query})

        results: list[KalshiMarketPrice] = []
        for event in events[:limit]:
            event_tick = event.get("event_ticker", "")
            for market in event.get("markets", []):
                if cutoff is not None:
                    prob = await _kalshi_market_at_cutoff(market, cutoff)
                    if prob is None:
                        continue
                else:
                    prob = _parse_kalshi_probability(market)
                    if prob is None:
                        continue

                ticker = market.get("ticker", "")
                results.append(
                    {
                        "market_title": market.get(
                            "title", event.get("title", "Unknown")
                        ),
                        "probability": prob,
                        "volume": market.get("volume_fp"),
                        "url": f"https://kalshi.com/markets/{ticker}",
                        "source": "kalshi",
                        "description": market.get("rules_primary"),
                        "market_ticker": ticker,
                        "event_ticker": event_tick,
                        "rules_primary": market.get("rules_primary"),
                    }
                )

        return mcp_success({"markets": results[:limit], "query": query})

    except httpx.HTTPStatusError as e:
        logger.exception("Kalshi API error")
        return mcp_error(f"Kalshi API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Kalshi search failed")
        return mcp_error(f"Kalshi search failed: {e}")


@tool(
    "kalshi_event",
    (
        "Get all bracket markets within a Kalshi event. Events like 'Fed funds rate March' "
        "have multiple bracket markets forming a probability distribution — very valuable "
        "for numeric CDF questions. Returns event title and all markets with probabilities, "
        "bracket info (strike_type, floor_strike, cap_strike), and volumes.\n\n"
        "Get event tickers from kalshi_price results, then drill in:\n"
        "  kalshi_event(event_ticker='KXFED-26MAR12') → all Fed rate brackets for March"
    ),
    KalshiEventInput.model_json_schema(),
)
@tracked("kalshi_event")
async def kalshi_event(args: dict[str, Any]) -> dict[str, Any]:
    """Get all markets in a Kalshi event."""
    try:
        validated = KalshiEventInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    event_ticker = validated.event_ticker
    cutoff = retrodict_cutoff.get()

    try:
        event = await _fetch_kalshi_event(event_ticker)
        if not event:
            return mcp_error(f"Event not found: {event_ticker}")

        event_markets: list[KalshiEventMarket] = []
        for market in event.get("markets", []):
            if cutoff is not None:
                prob = await _kalshi_market_at_cutoff(market, cutoff)
                if prob is None:
                    continue
            else:
                prob = _parse_kalshi_probability(market)
                if prob is None:
                    continue

            ticker = market.get("ticker", "")
            event_markets.append(
                {
                    "ticker": ticker,
                    "title": market.get("title", market.get("yes_sub_title", "")),
                    "probability": prob,
                    "volume": market.get("volume_fp"),
                    "strike_type": market.get("strike_type"),
                    "floor_strike": market.get("floor_strike"),
                    "cap_strike": market.get("cap_strike"),
                    "url": f"https://kalshi.com/markets/{ticker}",
                    "rules_primary": market.get("rules_primary"),
                }
            )

        result: KalshiEvent = {
            "event_ticker": event_ticker,
            "event_title": event.get("title", "Unknown"),
            "markets": event_markets,
            "url": f"https://kalshi.com/events/{event_ticker}",
            "description": event.get("sub_title"),
        }
        return mcp_success(result)

    except httpx.HTTPStatusError as e:
        logger.exception("Kalshi API error")
        return mcp_error(f"Kalshi API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Kalshi event fetch failed")
        return mcp_error(f"Kalshi event fetch failed: {e}")


@tool(
    "kalshi_history",
    (
        "Get historical Kalshi market price at a specific past timestamp via candlestick data. "
        "USE THIS to track how Kalshi probability changed over time. "
        "Get the market ticker from kalshi_price first, then query specific timestamps. "
        "Returns the closing price of the last daily candle at or before the timestamp."
    ),
    HistoricalPriceInput.model_json_schema(),
)
@tracked("kalshi_history")
async def kalshi_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get historical Kalshi price at a timestamp."""
    try:
        validated = HistoricalPriceInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    market_ticker = validated.market_id
    target_ts = validated.timestamp
    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
        target_ts = min(target_ts, cutoff_unix)

    series_ticker = _series_ticker_from_market(market_ticker)
    start_ts = target_ts - (30 * 24 * 60 * 60)

    try:
        candles = await _fetch_kalshi_candlestick(
            series_ticker, market_ticker, start_ts, target_ts
        )

        if not candles:
            return mcp_error(f"No historical data found for market {market_ticker}")

        closest = max(
            (c for c in candles if c.get("end_period_ts", 0) <= target_ts),
            key=lambda c: c.get("end_period_ts", 0),
            default=None,
        )
        if closest is None:
            return mcp_error(
                f"No price data found before timestamp {target_ts} for market {market_ticker}"
            )

        price = closest.get("price_dollars") or closest.get("yes_close_dollars")
        if price is None:
            return mcp_error(f"No price in candlestick data for {market_ticker}")

        result: HistoricalPrice = {
            "market_id": market_ticker,
            "timestamp": closest.get("end_period_ts", 0),
            "probability": float(price),
            "source": "kalshi",
        }
        return mcp_success(result)

    except httpx.HTTPStatusError as e:
        logger.exception("Kalshi history API error")
        return mcp_error(f"Kalshi API error: {e.response.status_code}")
    except Exception as e:
        logger.exception("Kalshi history lookup failed")
        return mcp_error(f"Kalshi history lookup failed: {e}")


# --- Metaculus Input Schemas ---


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
            if v.startswith("[") and v.endswith("]"):
                import ast as _ast

                parsed = _ast.literal_eval(v)
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


# --- Metaculus Output Schemas ---


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


# --- Metaculus Helpers ---


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
        "question_id": question.id_of_question,
        "title": question.question_text,
        "type": question.get_question_type(),
        "url": question.page_url,
        "background_info": question.background_info,
        "resolution_criteria": question.resolution_criteria,
        "fine_print": question.fine_print,
        "num_forecasters": question.num_forecasters,
    }

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
    now = datetime.now(tz=timezone.utc)
    earliest_dt = now - timedelta(days=days)

    for point in aggregation.history:
        if not point.centers:
            continue
        cp = point.centers[0]
        ts_dt = datetime.fromtimestamp(point.start_time, tz=timezone.utc)

        if cutoff_dt is not None and ts_dt > cutoff_dt:
            filtered_count += 1
            continue

        if ts_dt < earliest_dt:
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

    try:
        await client.fetch_post_json(input_id)
        _post_id_cache[input_id] = input_id
        return input_id
    except Exception:
        pass

    resolved = await _resolve_question_to_post_id(input_id)
    if resolved is not None:
        _post_id_cache[input_id] = resolved
    return resolved


async def _fetch_aggregation(post_id: int) -> AggregationMethod:
    """Fetch CP history from the aggregation_explorer endpoint."""
    client = get_metaculus_client()
    return await client.fetch_aggregation_history(post_id)


# --- Metaculus Tools ---


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

    search_query = validated.query
    num_results = validated.num_results

    try:
        client = get_metaculus_client()
        api_filter = ApiFilter(other_url_parameters={"search": search_query})
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


# --- MCP Server ---

_PREDICTION_MARKET_TOOLS = [
    polymarket_price,
    manifold_price,
    kalshi_price,
    polymarket_history,
    manifold_history,
    kalshi_history,
    kalshi_event,
]

_METACULUS_TOOLS = [
    get_metaculus_questions,
    list_tournament_questions,
    search_metaculus,
    get_coherence_links,
    get_cp_history,
]


def create_markets_server() -> McpSdkServerConfig:
    """Create the markets MCP server with prediction market and Metaculus tools."""
    return create_mcp_server(
        name="markets",
        version="2.0.0",
        tools=_PREDICTION_MARKET_TOOLS + _METACULUS_TOOLS,
    )
