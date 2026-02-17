"""Prediction market tools for price signals.

These tools fetch current prices from prediction markets to provide
additional signal for forecasting. Market prices reflect aggregated
wisdom of traders with financial incentives.
"""

import ast
import logging
from datetime import date, datetime, time, timedelta
from typing import Any, TypedDict

import httpx
from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from claude_agent_sdk.types import McpSdkServerConfig

from aib.tools.mcp_server import create_mcp_server

from aib.retrodict_context import retrodict_cutoff
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


# --- Yahoo Finance API ---


class StockQueryInput(BaseModel):
    """Input for stock price tool."""

    symbol: str = Field(min_length=1, max_length=10)
    period: str = Field(
        default="1mo"
    )  # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    end_date: str | None = Field(default=None)


class StockHistoryEntry(TypedDict):
    """Single OHLCV data point for stock history."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float


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
        "Use for stock price comparison questions.\n\n"
        "Examples:\n"
        "  stock_price(symbol='AAPL') → current Apple price and metrics\n"
        "  stock_price(symbol='^VIX') → current VIX level\n"
        "  stock_price(symbol='^GSPC') → current S&P 500 level"
    ),
    StockQueryInput.model_json_schema(),
)
@tracked("stock_price")
async def stock_price(args: dict[str, Any]) -> dict[str, Any]:
    """Get stock price from Yahoo Finance."""
    try:
        validated = StockQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    symbol = validated.symbol.upper()
    cutoff = retrodict_cutoff.get()

    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)

        if cutoff is not None:
            end_str = cutoff.isoformat()
            start_str = (cutoff - timedelta(days=5)).isoformat()
            hist = ticker.history(start=start_str, end=end_str)
            if hist.empty:
                return mcp_error(f"No recent data found for {symbol}")
            last_row = hist.iloc[-1]
            result: StockPrice = {
                "symbol": symbol,
                "name": ticker.info.get("shortName", symbol),
                "current_price": float(last_row["Close"]),
                "previous_close": float(hist.iloc[-2]["Close"])
                if len(hist) > 1
                else None,
                "change_percent": None,
                "currency": ticker.info.get("currency", "USD"),
                "market_cap": None,
                "fifty_two_week_high": None,
                "fifty_two_week_low": None,
            }
            return mcp_success(result)

        info = ticker.info

        if not info or info.get("regularMarketPrice") is None:
            return mcp_error(f"No data found for symbol: {symbol}")

        result = {
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
        "Use for analyzing price trends and volatility.\n\n"
        "Examples:\n"
        "  stock_history(symbol='AAPL', period='3mo') → 3 months of Apple OHLCV\n"
        "  stock_history(symbol='^GSPC', period='1y') → 1 year of S&P 500\n"
        "  stock_history(symbol='^VIX', period='6mo') → 6 months of VIX for volatility analysis\n"
        "  stock_history(symbol='GC=F', period='3mo') → 3 months of gold futures\n"
        "Feed the output to execute_code for Monte Carlo simulation or rolling volatility analysis."
    ),
    StockQueryInput.model_json_schema(),
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
    cutoff = retrodict_cutoff.get()
    end_date = cutoff.isoformat() if cutoff is not None else validated.end_date

    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)

        # If end_date is provided, use start/end instead of period
        if end_date:
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


# --- MCP Server ---

_ALL_MARKET_TOOLS = [
    polymarket_price,
    manifold_price,
    kalshi_price,
    polymarket_history,
    manifold_history,
    kalshi_history,
    kalshi_event,
    stock_price,
    stock_history,
]


def create_markets_server() -> McpSdkServerConfig:
    """Create the markets MCP server."""
    return create_mcp_server(
        name="markets",
        version="1.0.0",
        tools=_ALL_MARKET_TOOLS,
    )


markets_server = create_markets_server()
