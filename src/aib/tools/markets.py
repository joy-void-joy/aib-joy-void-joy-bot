"""Prediction market tools for price signals.

These tools fetch current prices from prediction markets to provide
additional signal for forecasting. Market prices reflect aggregated
wisdom of traders with financial incentives.
"""

import ast
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
        "Get historical Polymarket price at a specific timestamp. "
        "Requires the market token ID (not slug). Returns the price closest "
        "to but not after the given timestamp. Use for retrodict mode."
    ),
    {"market_id": str, "timestamp": int},
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
        "Get historical Manifold market price at a specific timestamp. "
        "Reconstructs price from bet history. Requires the contract ID. "
        "Returns the probability just after the last bet before the timestamp. "
        "Use for retrodict mode."
    ),
    {"market_id": str, "timestamp": int},
)
@tracked("manifold_history")
async def manifold_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get historical Manifold price at a timestamp."""
    try:
        validated = HistoricalPriceInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    contract_id = validated.market_id
    # Manifold uses milliseconds
    target_ts_ms = validated.timestamp * 1000

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


# --- Yahoo Finance API ---


class StockQueryInput(BaseModel):
    """Input for stock price tool."""

    symbol: str = Field(min_length=1, max_length=10)
    period: str = Field(
        default="1mo"
    )  # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    end_date: str | None = Field(default=None)  # YYYY-MM-DD format, for retrodict mode


class StockPrice(TypedDict):
    """Price information for a stock."""

    symbol: str
    name: str
    current_price: float | None
    previous_close: float | None
    change_percent: float | None
    currency: str
    market_cap: float | None
    fifty_two_week_high: float | None
    fifty_two_week_low: float | None


@tool(
    "stock_price",
    (
        "Get current stock price and key metrics for a ticker symbol using Yahoo Finance. "
        "Returns current price, previous close, 52-week range, and market cap. "
        "Use for stock price comparison questions."
    ),
    {"symbol": str, "period": str},
)
@tracked("stock_price")
async def stock_price(args: dict[str, Any]) -> dict[str, Any]:
    """Get stock price from Yahoo Finance."""
    try:
        validated = StockQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    symbol = validated.symbol.upper()

    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)
        info = ticker.info

        if not info or info.get("regularMarketPrice") is None:
            return mcp_error(f"No data found for symbol: {symbol}")

        result: StockPrice = {
            "symbol": symbol,
            "name": info.get("shortName", info.get("longName", symbol)),
            "current_price": info.get("regularMarketPrice"),
            "previous_close": info.get("previousClose"),
            "change_percent": info.get("regularMarketChangePercent"),
            "currency": info.get("currency", "USD"),
            "market_cap": info.get("marketCap"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
        }

        return mcp_success(result)

    except Exception as e:
        logger.exception("Yahoo Finance lookup failed")
        return mcp_error(f"Yahoo Finance lookup failed for {symbol}: {e}")


@tool(
    "stock_history",
    (
        "Get historical stock prices for a ticker symbol. "
        "Returns OHLCV data for the specified period. "
        "Periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max. "
        "Optional end_date (YYYY-MM-DD) to cap data at a specific date. "
        "Use for analyzing price trends and volatility."
    ),
    {"symbol": str, "period": str, "end_date": str},
)
@tracked("stock_history")
async def stock_history(args: dict[str, Any]) -> dict[str, Any]:
    """Get historical stock prices from Yahoo Finance."""
    try:
        validated = StockQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    symbol = validated.symbol.upper()
    period = validated.period
    end_date = validated.end_date

    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)

        # If end_date is provided, use start/end instead of period
        if end_date:
            from datetime import datetime, timedelta

            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            # Calculate start date based on period
            period_days = {
                "1d": 1,
                "5d": 5,
                "1mo": 30,
                "3mo": 90,
                "6mo": 180,
                "1y": 365,
                "2y": 730,
                "5y": 1825,
            }
            days = period_days.get(period, 365)
            start_dt = end_dt - timedelta(days=days)
            hist = ticker.history(start=start_dt.strftime("%Y-%m-%d"), end=end_date)
        else:
            hist = ticker.history(period=period)

        if hist.empty:
            return mcp_error(f"No historical data found for symbol: {symbol}")

        # Convert to list of dicts for JSON serialization
        # Reset index to make date a column, then convert to records
        hist_reset = hist.reset_index()
        hist_reset["Date"] = hist_reset["Date"].dt.strftime("%Y-%m-%d")

        records: list[dict[str, object]] = hist_reset[
            ["Date", "Open", "High", "Low", "Close", "Volume"]
        ].to_dict("records")  # pyright: ignore[reportCallIssue]

        # Rename keys to lowercase and limit to last 30
        formatted: list[dict[str, object]] = [
            {
                "date": r["Date"],
                "open": r["Open"],
                "high": r["High"],
                "low": r["Low"],
                "close": r["Close"],
                "volume": r["Volume"],
            }
            for r in records[-30:]  # Limit to last 30 days
        ]

        return mcp_success(
            {
                "symbol": symbol,
                "period": period,
                "data_points": len(records),
                "first_date": formatted[0]["date"] if formatted else None,
                "last_date": formatted[-1]["date"] if formatted else None,
                "history": formatted,
            }
        )

    except Exception as e:
        logger.exception("Yahoo Finance history lookup failed")
        return mcp_error(f"Yahoo Finance history lookup failed for {symbol}: {e}")


# --- MCP Server ---

markets_server = create_mcp_server(
    name="markets",
    version="1.0.0",
    tools=[
        polymarket_price,
        manifold_price,
        polymarket_history,
        manifold_history,
        stock_price,
        stock_history,
    ],
)
