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
from claude_agent_sdk import tool
from claude_agent_sdk.types import McpSdkServerConfig
from pydantic import BaseModel, ConfigDict, Field, field_validator

from metaculus import ApiFilter, BinaryQuestion
from metaculus.models import AggregationMethod

from aib.clients.metaculus import get_client as get_metaculus_client
from aib.config import settings
from aib.tools.redact import redact_future_info
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
    history_days: int | None = Field(
        default=7,
        ge=0,
        le=90,
        description="Days of price history to include (default 7). Set to 0 or null to disable.",
    )


class KalshiEventInput(BaseModel):
    """Input for fetching a single Kalshi event with all its markets."""

    event_ticker: str = Field(min_length=1)


# --- Output Schemas ---


class HistoryPoint(TypedDict):
    """A single daily price point in market history."""

    date: str
    probability: float


class MarketPrice(TypedDict):
    """Price information from a prediction market."""

    market_title: str
    probability: float  # 0-1, derived from price
    volume: float | None  # Trading volume if available
    url: str
    source: str  # "polymarket", "manifold", or "kalshi"
    description: str | None  # Resolution criteria / market description
    market_id: str | None  # Platform-specific ID for drill-down/history
    recent_history: list[HistoryPoint] | None  # Daily prices over recent days


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
async def _search_polymarket(query: str) -> list[PolymarketEventData]:
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
        return [PolymarketEventData.model_validate(e) for e in response.json()]


def _coerce_to_list(value: Any) -> list[Any] | None:
    """Coerce a Polymarket API field to a list, parsing string literals if needed.

    The Gamma API sometimes returns list fields (outcomePrices, clobTokenIds)
    as JSON-encoded strings instead of native lists.
    """
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        try:
            parsed = ast.literal_eval(value)
            if isinstance(parsed, list):
                return parsed
            return [parsed]
        except (ValueError, SyntaxError):
            return [value]
    return None


def _extract_float(value: Any) -> float | None:
    """Extract a float from potentially nested/stringified API data."""
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            parsed = ast.literal_eval(value)
            return _extract_float(parsed)
        except (ValueError, SyntaxError):
            try:
                return float(value)
            except ValueError:
                return None
    if isinstance(value, list) and value:
        return _extract_float(value[0])
    return None


# --- API Response Models ---


class PolymarketMarketData(BaseModel):
    """Parsed market data from a Polymarket Gamma API event."""

    model_config = ConfigDict(populate_by_name=True)

    outcome_prices: list[float] = Field(validation_alias="outcomePrices", default=[])
    clob_token_ids: list[str] = Field(validation_alias="clobTokenIds", default=[])
    volume: float | None = None
    description: str | None = None

    @field_validator("outcome_prices", mode="before")
    @classmethod
    def coerce_prices(cls, v: Any) -> list[float]:
        items = _coerce_to_list(v)
        if not items:
            return []
        return [f for item in items if (f := _extract_float(item)) is not None]

    @field_validator("clob_token_ids", mode="before")
    @classmethod
    def coerce_token_ids(cls, v: Any) -> list[str]:
        items = _coerce_to_list(v)
        if not items:
            return []
        return [str(item) for item in items]

    @property
    def yes_price(self) -> float | None:
        return self.outcome_prices[0] if self.outcome_prices else None


class PolymarketEventData(BaseModel):
    """Parsed event from the Polymarket Gamma API."""

    title: str = "Unknown"
    slug: str = ""
    description: str | None = None
    markets: list[PolymarketMarketData] = []

    @property
    def first_market(self) -> PolymarketMarketData | None:
        return self.markets[0] if self.markets else None


class PolymarketPricePoint(BaseModel):
    """A single price point from Polymarket CLOB history."""

    t: int = 0
    p: float = 0.5


class ManifoldMarketData(BaseModel):
    """Parsed market from the Manifold API."""

    model_config = ConfigDict(populate_by_name=True)

    id: str = ""
    question: str = "Unknown"
    probability: float = 0.5
    volume: float | None = None
    url: str = ""
    slug: str = ""
    text_description: str | None = Field(
        validation_alias="textDescription", default=None
    )
    description_text: str | None = Field(validation_alias="description", default=None)

    @property
    def effective_description(self) -> str | None:
        return self.text_description or self.description_text

    @property
    def effective_url(self) -> str:
        return self.url or f"https://manifold.markets/{self.slug}"


class ManifoldBet(BaseModel):
    """A single bet from the Manifold API."""

    model_config = ConfigDict(populate_by_name=True)

    created_time: int = Field(validation_alias="createdTime", default=0)
    prob_after: float | None = Field(validation_alias="probAfter", default=None)
    prob_before: float | None = Field(validation_alias="probBefore", default=None)

    @property
    def probability(self) -> float:
        if self.prob_after is not None:
            return self.prob_after
        if self.prob_before is not None:
            return self.prob_before
        return 0.5


class KalshiMarketData(BaseModel):
    """Parsed market from the Kalshi API."""

    ticker: str = ""
    title: str = ""
    yes_sub_title: str = ""
    last_price_dollars: float | None = None
    yes_ask_dollars: float | None = None
    yes_bid_dollars: float | None = None
    volume_fp: float | None = None
    created_time: str | None = None
    strike_type: str | None = None
    floor_strike: float | None = None
    cap_strike: float | None = None
    rules_primary: str | None = None

    @property
    def probability(self) -> float | None:
        if self.last_price_dollars is not None:
            return self.last_price_dollars
        if self.yes_ask_dollars is not None and self.yes_bid_dollars is not None:
            return (self.yes_ask_dollars + self.yes_bid_dollars) / 2.0
        return None


class KalshiEventData(BaseModel):
    """Parsed event from the Kalshi API."""

    event_ticker: str = ""
    title: str = "Unknown"
    sub_title: str | None = None
    markets: list[KalshiMarketData] = []


class KalshiCandlestick(BaseModel):
    """A single candlestick from the Kalshi API."""

    end_period_ts: int = 0
    price_dollars: float | None = None
    yes_close_dollars: float | None = None

    @property
    def close_price(self) -> float | None:
        if self.price_dollars is not None:
            return self.price_dollars
        return self.yes_close_dollars


def parse_polymarket_event(event: PolymarketEventData) -> MarketPrice | None:
    """Parse a Polymarket event into a MarketPrice."""
    market = event.first_market
    if market is None:
        return None

    if market.yes_price is None:
        logger.warning("No price for event %s", event.slug)
        return None

    return {
        "market_title": event.title,
        "probability": market.yes_price,
        "volume": market.volume,
        "url": f"https://polymarket.com/event/{event.slug}",
        "source": "polymarket",
        "description": event.description or market.description,
        "market_id": market.clob_token_ids[0] if market.clob_token_ids else None,
        "recent_history": None,
    }


async def _polymarket_event_at_cutoff(
    event: PolymarketEventData,
    cutoff: date,
) -> MarketPrice | None:
    """Get historical price for a Polymarket event at the cutoff date."""
    market = event.first_market
    if market is None or not market.clob_token_ids:
        return None
    token_id = market.clob_token_ids[0]
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    start_ts = cutoff_unix - (30 * 24 * 60 * 60)
    try:
        history = await _fetch_polymarket_history(token_id, start_ts, cutoff_unix)
    except Exception:
        return None
    if not history:
        return None
    closest = max(
        (p for p in history if p.t <= cutoff_unix),
        key=lambda p: p.t,
        default=None,
    )
    if closest is None:
        return None
    return {
        "market_title": event.title,
        "probability": closest.p,
        "volume": market.volume,
        "url": f"https://polymarket.com/event/{event.slug}",
        "source": "polymarket",
        "description": None,
        "market_id": token_id,
        "recent_history": None,
    }


async def _augment_polymarket_history(results: list[MarketPrice], days: int) -> None:
    """Augment Polymarket results with recent price history in-place."""
    now_ts = int(datetime.now(tz=timezone.utc).timestamp())
    start_ts = now_ts - (days * 86400)

    async def _add_one(result: MarketPrice) -> None:
        token_id = result.get("market_id")
        if not token_id:
            return
        try:
            history = await _fetch_polymarket_history(token_id, start_ts, now_ts)
            if not history:
                return
            by_day: dict[str, float] = {}
            for p in history:
                day = datetime.fromtimestamp(p.t, tz=timezone.utc).strftime("%Y-%m-%d")
                by_day[day] = round(p.p, 3)
            result["recent_history"] = [
                {"date": d, "probability": p} for d, p in sorted(by_day.items())
            ]
        except Exception:
            pass

    await asyncio.gather(*[_add_one(r) for r in results])


async def _augment_manifold_history(results: list[MarketPrice], days: int) -> None:
    """Augment Manifold results with recent price history in-place."""
    now_ms = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

    async def _add_one(result: MarketPrice) -> None:
        contract_id = result.get("market_id")
        if not contract_id:
            return
        try:
            bets = await _fetch_manifold_bets(contract_id, now_ms, limit=500)
            if not bets:
                return
            cutoff_ms = now_ms - (days * 86400 * 1000)
            by_day: dict[str, float] = {}
            for b in bets:
                if b.created_time < cutoff_ms:
                    continue
                day = datetime.fromtimestamp(
                    b.created_time / 1000, tz=timezone.utc
                ).strftime("%Y-%m-%d")
                by_day[day] = round(b.probability, 3)
            if by_day:
                result["recent_history"] = [
                    {"date": d, "probability": p} for d, p in sorted(by_day.items())
                ]
        except Exception:
            pass

    await asyncio.gather(*[_add_one(r) for r in results])


async def _augment_kalshi_history(results: list[KalshiMarketPrice], days: int) -> None:
    """Augment Kalshi results with recent price history in-place."""
    now_ts = int(datetime.now(tz=timezone.utc).timestamp())
    start_ts = now_ts - (days * 86400)

    async def _add_one(result: KalshiMarketPrice) -> None:
        ticker = result.get("market_ticker")
        if not ticker:
            return
        series = _series_ticker_from_market(ticker)
        try:
            candles = await _fetch_kalshi_candlestick(series, ticker, start_ts, now_ts)
            if not candles:
                return
            result["recent_history"] = [
                {
                    "date": datetime.fromtimestamp(
                        c.end_period_ts, tz=timezone.utc
                    ).strftime("%Y-%m-%d"),
                    "probability": round(c.close_price, 3),
                }
                for c in candles
                if c.close_price is not None
            ]
        except Exception:
            pass

    await asyncio.gather(*[_add_one(r) for r in results])


@tool(
    "polymarket_price",
    (
        "Search Polymarket for prediction markets and return current prices "
        "with recent price history (default 7 days). "
        "Returns YES price as probability, trading volume, URL, and daily price trend. "
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

        if cutoff is None and validated.history_days:
            await _augment_polymarket_history(results, validated.history_days)

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
async def _search_manifold(query: str) -> list[ManifoldMarketData]:
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
        return [ManifoldMarketData.model_validate(m) for m in response.json()]


def parse_manifold_market(market: ManifoldMarketData) -> MarketPrice:
    """Parse a Manifold market into a MarketPrice."""
    return {
        "market_title": market.question,
        "probability": market.probability,
        "volume": market.volume,
        "url": market.effective_url,
        "source": "manifold",
        "description": market.effective_description,
        "market_id": market.id or None,
        "recent_history": None,
    }


async def _manifold_market_at_cutoff(
    market: ManifoldMarketData,
    cutoff: date,
) -> MarketPrice | None:
    """Get historical price for a Manifold market at the cutoff date."""
    if not market.id:
        return None
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    cutoff_ms = cutoff_unix * 1000
    try:
        bets = await _fetch_manifold_bets(market.id, cutoff_ms)
    except Exception:
        return None
    if not bets:
        return None
    relevant = max(
        (b for b in bets if b.created_time <= cutoff_ms),
        key=lambda b: b.created_time,
        default=None,
    )
    if relevant is None:
        return None
    return {
        "market_title": market.question,
        "probability": relevant.probability,
        "volume": market.volume,
        "url": market.effective_url,
        "source": "manifold",
        "description": None,
        "market_id": market.id or None,
        "recent_history": None,
    }


@tool(
    "manifold_price",
    (
        "Search Manifold Markets for prediction markets and return current prices "
        "with recent price history (default 7 days). "
        "Returns probability, trading volume (in mana), URL, and daily price trend. "
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

        if cutoff is None and validated.history_days:
            await _augment_manifold_history(results, validated.history_days)

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
) -> list[PolymarketPricePoint]:
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
        return [PolymarketPricePoint.model_validate(p) for p in data.get("history", [])]


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

        closest_point = max(
            (p for p in history if p.t <= target_ts),
            key=lambda p: p.t,
            default=None,
        )

        if closest_point is None:
            return mcp_error(
                f"No price data found before timestamp {target_ts} for market {token_id}"
            )

        result: HistoricalPrice = {
            "market_id": token_id,
            "timestamp": closest_point.t,
            "probability": closest_point.p,
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
) -> list[ManifoldBet]:
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
        return [ManifoldBet.model_validate(b) for b in response.json()]


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

        relevant_bet = max(
            (b for b in bets if b.created_time <= target_ts_ms),
            key=lambda b: b.created_time,
            default=None,
        )

        if relevant_bet is None:
            return mcp_error(
                f"No bets found before timestamp {validated.timestamp} for contract {contract_id}"
            )

        result: HistoricalPrice = {
            "market_id": contract_id,
            "timestamp": relevant_bet.created_time // 1000,
            "probability": relevant_bet.probability,
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


def _kalshi_matches_query(event: KalshiEventData, query_words: list[str]) -> bool:
    """Check if a Kalshi event matches all query words (AND logic, case-insensitive)."""
    text_parts = [event.title, event.sub_title or ""]
    for m in event.markets:
        text_parts.append(m.yes_sub_title)
        text_parts.append(m.title)
    combined = " ".join(text_parts).lower()
    return all(w in combined for w in query_words)


@with_retry(max_attempts=3)
async def _fetch_kalshi_events(
    query: str, *, status: str | None = "open"
) -> list[KalshiEventData]:
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
        events = [KalshiEventData.model_validate(e) for e in data.get("events", [])]

    query_words = query.lower().split()
    return [e for e in events if _kalshi_matches_query(e, query_words)]


@with_retry(max_attempts=3)
async def _fetch_kalshi_event(event_ticker: str) -> KalshiEventData:
    """Fetch a single Kalshi event with all its markets."""
    async with httpx.AsyncClient(timeout=settings.http_timeout_seconds) as client:
        response = await client.get(
            f"{KALSHI_API}/events/{event_ticker}",
            params={"with_nested_markets": "true"},
        )
        response.raise_for_status()
        return KalshiEventData.model_validate(response.json().get("event", {}))


@with_retry(max_attempts=3)
async def _fetch_kalshi_candlestick(
    series_ticker: str,
    market_ticker: str,
    start_ts: int,
    end_ts: int,
) -> list[KalshiCandlestick]:
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
        return [
            KalshiCandlestick.model_validate(c)
            for c in response.json().get("candlesticks", [])
        ]


async def _kalshi_market_at_cutoff(
    market: KalshiMarketData, cutoff: date
) -> float | None:
    """Get historical price for a Kalshi market at the retrodict cutoff.

    Returns None if the market was created after the cutoff or if no
    candlestick data is available.
    """
    if market.created_time:
        try:
            created_dt = datetime.fromisoformat(
                market.created_time.replace("Z", "+00:00")
            )
            cutoff_dt = datetime.combine(cutoff, time())
            if created_dt.replace(tzinfo=None) > cutoff_dt:
                return None
        except (ValueError, TypeError):
            pass

    series_ticker = _series_ticker_from_market(market.ticker)
    cutoff_unix = int(datetime.combine(cutoff, time()).timestamp())
    start_ts = cutoff_unix - (30 * 24 * 60 * 60)

    try:
        candles = await _fetch_kalshi_candlestick(
            series_ticker, market.ticker, start_ts, cutoff_unix
        )
    except Exception:
        return None

    if not candles:
        return None

    closest = max(
        (c for c in candles if c.end_period_ts <= cutoff_unix),
        key=lambda c: c.end_period_ts,
        default=None,
    )
    if closest is None:
        return None

    return closest.close_price


@tool(
    "kalshi_price",
    (
        "Search Kalshi (CFTC-regulated event contracts exchange) for prediction markets "
        "with recent price history (default 7 days). "
        "Strong coverage of economic/policy events: Fed rate decisions, CPI, GDP, jobs reports. "
        "Returns YES price as probability, trading volume, URL, and daily price trend. "
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
            for market in event.markets:
                if cutoff is not None:
                    prob = await _kalshi_market_at_cutoff(market, cutoff)
                    if prob is None:
                        continue
                else:
                    prob = market.probability
                    if prob is None:
                        continue

                results.append(
                    {
                        "market_title": market.title or event.title,
                        "probability": prob,
                        "volume": market.volume_fp,
                        "url": f"https://kalshi.com/markets/{market.ticker}",
                        "source": "kalshi",
                        "description": market.rules_primary,
                        "market_id": market.ticker,
                        "recent_history": None,
                        "market_ticker": market.ticker,
                        "event_ticker": event.event_ticker,
                        "rules_primary": market.rules_primary,
                    }
                )

        limited = results[:limit]

        if cutoff is None and validated.history_days:
            await _augment_kalshi_history(limited, validated.history_days)

        return mcp_success({"markets": limited, "query": query})

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
        for market in event.markets:
            if cutoff is not None:
                prob = await _kalshi_market_at_cutoff(market, cutoff)
                if prob is None:
                    continue
            else:
                prob = market.probability
                if prob is None:
                    continue

            event_markets.append(
                {
                    "ticker": market.ticker,
                    "title": market.title or market.yes_sub_title,
                    "probability": prob,
                    "volume": market.volume_fp,
                    "strike_type": market.strike_type,
                    "floor_strike": market.floor_strike,
                    "cap_strike": market.cap_strike,
                    "url": f"https://kalshi.com/markets/{market.ticker}",
                    "rules_primary": market.rules_primary,
                }
            )

        result: KalshiEvent = {
            "event_ticker": event_ticker,
            "event_title": event.title,
            "markets": event_markets,
            "url": f"https://kalshi.com/events/{event_ticker}",
            "description": event.sub_title,
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
            (c for c in candles if c.end_period_ts <= target_ts),
            key=lambda c: c.end_period_ts,
            default=None,
        )
        if closest is None:
            return mcp_error(
                f"No price data found before timestamp {target_ts} for market {market_ticker}"
            )

        if closest.close_price is None:
            return mcp_error(f"No price in candlestick data for {market_ticker}")

        result: HistoricalPrice = {
            "market_id": market_ticker,
            "timestamp": closest.end_period_ts,
            "probability": closest.close_price,
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

    post_id: int = Field(
        description="Metaculus post ID (the number in the URL, e.g. metaculus.com/questions/{post_id})"
    )


class CPHistoryInput(BaseModel):
    """Input for fetching community prediction history."""

    post_id: int = Field(
        description="Metaculus post ID (the number in the URL, e.g. metaculus.com/questions/{post_id})"
    )
    days: int = Field(default=30, ge=1, le=365)


# --- Metaculus Output Schemas ---


class QuestionDict(TypedDict, total=False):
    """Metaculus question data returned by _question_to_dict."""

    post_id: int
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

    post_id: int
    title: str
    url: str
    days_requested: int
    data_points: int
    history: list[CPHistoryEntry]
    note: str | None = None


# --- Metaculus Helpers ---


def _question_to_dict(question: Any, *, hide_cp: bool = False) -> dict[str, object]:
    """Convert a MetaculusQuestion to a serializable dict.

    Args:
        question: MetaculusQuestion object.
        hide_cp: If True, exclude community_prediction (for retrodict mode).
    """
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
    post_id: int,
    title: str,
    url: str,
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
        post_id=post_id,
        title=title,
        url=url,
        days_requested=days,
        data_points=len(entries),
        history=entries,
        note=note,
    )


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
            result["fine_print"] = await redact_future_info(fine_print, str(cutoff))
        return result

    async def fetch_one(post_id: int) -> dict[str, Any]:
        """Fetch a single question by post_id."""
        try:
            result = await _fetch_metaculus_question(post_id)
            return await _apply_retrodict_filters(result)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return {
                    "post_id": post_id,
                    "error": f"Post {post_id} not found. Use list_tournament_questions to find correct post IDs.",
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
        "Pass the post_id (the number in the Metaculus URL).\n\n"
        "Examples:\n"
        "  get_coherence_links(post_id=42135) → find related questions"
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

    post_id = validated.post_id
    try:
        client = get_metaculus_client()
        question = await client.get_question_by_post_id(post_id)
        if isinstance(question, list):
            question = question[0]
        links = await client.get_links_for_question(question.id_of_question)
        results = [
            {
                "post_id_1": link.question1.id_of_post,
                "title_1": link.question1.question_text,
                "post_id_2": link.question2.id_of_post,
                "title_2": link.question2.question_text,
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
        "Pass the post_id (the number in the Metaculus URL). "
        "Note: Returns the UNDERLYING question's CP, not the meta-question's own CP.\n\n"
        "Examples:\n"
        "  get_cp_history(post_id=42135) → last 30 days of CP\n"
        "  get_cp_history(post_id=42135, days=90) → last 90 days\n"
        "For meta-predictions: pass the UNDERLYING question's post_id "
        "(from the meta-question's description), not the meta-question's own post_id."
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

    post_id = validated.post_id
    days = validated.days

    cutoff_dt = None
    cutoff_date = retrodict_cutoff.get()
    if cutoff_date is not None:
        cutoff_dt = datetime.combine(cutoff_date, datetime.min.time()).replace(
            tzinfo=timezone.utc
        )

    try:
        question_data = await _fetch_metaculus_question(post_id)
        title = str(question_data.get("title", ""))
        url = str(question_data.get("url", ""))
        aggregation = await _fetch_aggregation(post_id)
        response = _build_cp_history_response(
            aggregation, post_id, title, url, days, cutoff_dt
        )
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
