"""Financial data tools for economic indicators and time series.

These tools provide direct API access to financial data sources,
avoiding the need for web scraping which often fails on JS-heavy sites.
"""

import logging
from datetime import date, datetime, timedelta
import math
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

import numpy as np

from aib.retrodict_context import retrodict_cutoff
from aib.config import settings
from aib.tools.cache import cached
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class FredSeriesInput(BaseModel):
    """Input for FRED series lookup."""

    series_id: str = Field(min_length=1, max_length=50)
    observation_start: str | None = Field(
        default=None, description="Start date (YYYY-MM-DD). Default: 30 days ago"
    )
    observation_end: str | None = Field(
        default=None, description="End date (YYYY-MM-DD). Default: today"
    )
    limit: int | None = Field(
        default=30,
        ge=1,
        description="Max observations to return (from end of range). Default: 30. Set to null for all observations.",
    )


class FredSearchInput(BaseModel):
    """Input for FRED series search."""

    query: str = Field(min_length=1)
    limit: int = Field(default=10, ge=1, le=50)


# --- Output Schemas ---


class FredObservation(TypedDict):
    """A single FRED observation."""

    date: str
    value: float | None


class FredSeriesInfo(TypedDict):
    """Metadata about a FRED series."""

    id: str
    title: str
    frequency: str
    units: str
    seasonal_adjustment: str
    last_updated: str


class RegimeStats(TypedDict):
    """Regime detection output for a FRED time series."""

    stable_since: str
    stable_mean: float
    stable_std: float
    observations_in_regime: int
    prior_regime_mean: float | None
    shift_magnitude: float | None
    shift_direction: str | None


# --- FRED API Tools ---


class RateFuture(TypedDict):
    """A single rate futures contract."""

    symbol: str
    month: str
    implied_rate: float


class RateFuturesCurve(TypedDict):
    """Rate futures curve for interest rate series."""

    contracts: list[RateFuture]
    current_rate: float
    months_ahead: int


_RATE_SERIES_TO_FUTURES: dict[str, str] = {
    "DTB4WK": "ZQ",
    "DTB3": "ZQ",
    "DTB6": "ZQ",
    "DGS1MO": "ZQ",
    "DGS3MO": "ZQ",
    "DGS6MO": "ZQ",
    "DGS1": "ZQ",
    "DGS2": "ZQ",
    "FEDFUNDS": "ZQ",
    "EFFR": "ZQ",
    "SOFR": "ZQ",
    "PRIME": "ZQ",
}


_REGIME_SENSITIVITY_FLOOR = 0.02


def _detect_regime(observations: list[FredObservation]) -> RegimeStats | None:
    """Detect the current stable regime via backward expansion.

    Starting from the last 3 non-null observations, grows backward as long as
    each new observation is within max(3 * window_std, sensitivity_floor) of
    the window mean. Returns None if fewer than 5 non-null observations.
    """
    values: list[tuple[str, float]] = [
        (obs["date"], obs["value"]) for obs in observations if obs["value"] is not None
    ]
    if len(values) < 5:
        return None

    # Start from the last 3 observations
    window: list[float] = [v for _, v in values[-3:]]
    stable_start_idx = len(values) - 3

    # Expand backward
    for i in range(len(values) - 4, -1, -1):
        _, val = values[i]
        window_mean = sum(window) / len(window)
        window_std = (sum((x - window_mean) ** 2 for x in window) / len(window)) ** 0.5
        threshold = max(3 * window_std, _REGIME_SENSITIVITY_FLOOR)
        if abs(val - window_mean) > threshold:
            break
        window.append(val)
        stable_start_idx = i

    stable_values = [v for _, v in values[stable_start_idx:]]
    stable_mean = sum(stable_values) / len(stable_values)
    stable_std = (
        sum((x - stable_mean) ** 2 for x in stable_values) / len(stable_values)
    ) ** 0.5

    prior_mean: float | None = None
    shift_mag: float | None = None
    shift_dir: str | None = None

    if stable_start_idx > 0:
        prior_values = [v for _, v in values[:stable_start_idx]]
        if prior_values:
            prior_mean = sum(prior_values) / len(prior_values)
            shift_mag = abs(stable_mean - prior_mean)
            shift_dir = "up" if stable_mean > prior_mean else "down"

    return RegimeStats(
        stable_since=values[stable_start_idx][0],
        stable_mean=round(stable_mean, 6),
        stable_std=round(stable_std, 6),
        observations_in_regime=len(stable_values),
        prior_regime_mean=round(prior_mean, 6) if prior_mean is not None else None,
        shift_magnitude=round(shift_mag, 6) if shift_mag is not None else None,
        shift_direction=shift_dir,
    )


def _fetch_rate_futures(
    series_id: str,
    current_value: float,
    cutoff: date | None,
) -> RateFuturesCurve | None:
    """Fetch Fed Funds futures curve and convert to implied rates.

    Uses the ZQ=F continuous contract to discover the front month via
    _fetch_futures_curve, then derives implied_rate = 100 - price for
    each contract.
    """
    futures_root = _RATE_SERIES_TO_FUTURES.get(series_id)
    if futures_root is None:
        return None

    import yfinance as yf

    try:
        ticker = yf.Ticker(f"{futures_root}=F")
        info = ticker.info
        if not info:
            return None

        curve = _fetch_futures_curve(info, cutoff)
        if curve is None:
            return None

        curve_contracts = curve.get("contracts")
        if not curve_contracts:
            return None

        contracts: list[RateFuture] = [
            RateFuture(
                symbol=c["symbol"],
                month=c["month"],
                implied_rate=round(100.0 - c["price"], 4),
            )
            for c in curve_contracts
        ]

        if len(contracts) < 2:
            return None

        return RateFuturesCurve(
            contracts=contracts,
            current_rate=current_value,
            months_ahead=len(contracts),
        )
    except Exception:
        logger.debug("Rate futures fetch failed for %s", series_id)
        return None


@tool(
    "fred_series",
    (
        "Get historical data for a FRED (Federal Reserve Economic Data) series. "
        "Returns observations and series metadata. Set observation_start/observation_end to control the date range.\n\n"
        "For known interest rate series (FEDFUNDS, DTB4WK, SOFR, etc.), automatically "
        "includes rate_futures with market-implied rate path from Fed Funds futures.\n\n"
        "Common series IDs:\n"
        "  Treasury: DGS1MO, DGS3MO, DGS6MO, DGS1, DGS2, DGS5, DGS10, DGS20, DGS30\n"
        "  Rates: FEDFUNDS (Fed Funds), PRIME (Prime Rate), MORTGAGE30US (30yr Mortgage)\n"
        "  Economy: UNRATE (Unemployment), CPIAUCSL (CPI), GDP, PAYEMS (Nonfarm Payrolls), "
        "INDPRO (Industrial Production), HOUST (Housing Starts), RSAFS (Retail Sales)\n"
        "  FX: DEXUSEU (USD/EUR), DEXJPUS (JPY/USD), DTWEXBGS (Trade-Weighted Dollar)\n"
        "  Markets: SP500, NASDAQCOM, DJIA\n\n"
        "Examples:\n"
        '  fred_series(series_id="DGS10") → last 30 days of 10-year Treasury yields\n'
        '  fred_series(series_id="UNRATE", observation_start="2024-01-01") → unemployment from Jan 2024 to now\n'
        '  fred_series(series_id="CPIAUCSL", observation_start="2024-01-01", observation_end="2025-06-01") → CPI for a specific window\n'
        "Use fred_search first if you don't know the series ID."
    ),
    FredSeriesInput.model_json_schema(),
)
@tracked("fred_series")
async def fred_series(args: dict[str, Any]) -> dict[str, Any]:
    """Get FRED series data."""
    try:
        validated = FredSeriesInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    api_key = settings.fred_api_key
    if not api_key:
        return mcp_error(
            "FRED_API_KEY not configured. Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html"
        )

    series_id = validated.series_id.upper()

    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        end_date = cutoff.isoformat()
        start_date = (
            validated.observation_start or (cutoff - timedelta(days=30)).isoformat()
        )
    else:
        reference_date = datetime.now().date()
        end_date = validated.observation_end or reference_date.isoformat()
        start_date = (
            validated.observation_start
            or (reference_date - timedelta(days=30)).isoformat()
        )

    try:
        from fredapi import Fred

        fred = Fred(api_key=api_key)

        # Get series info
        info = fred.get_series_info(series_id)

        # Get observations
        observations = fred.get_series(
            series_id,
            observation_start=start_date,
            observation_end=end_date,
        )

        # Convert to list of dicts
        obs_list: list[FredObservation] = []
        for date, value in observations.items():
            obs_list.append(
                {
                    "date": str(date)[:10],
                    "value": float(value)
                    if not (value != value)
                    else None,  # Handle NaN
                }
            )

        # Get latest non-null value
        latest_value = None
        latest_date = None
        for obs in reversed(obs_list):
            if obs["value"] is not None:
                latest_value = obs["value"]
                latest_date = obs["date"]
                break

        if cutoff is not None and latest_value is None:
            return mcp_error(f"No observations available for {series_id}.")

        raw_updated = str(info.get("last_updated", ""))[:10]
        if cutoff is not None and raw_updated > cutoff.isoformat():
            raw_updated = cutoff.isoformat()

        series_info: FredSeriesInfo = {
            "id": series_id,
            "title": str(info.get("title", series_id)),
            "frequency": str(info.get("frequency", "Unknown")),
            "units": str(info.get("units", "Unknown")),
            "seasonal_adjustment": str(info.get("seasonal_adjustment", "Unknown")),
            "last_updated": raw_updated,
        }

        result_data: dict[str, Any] = {
            "series": series_info,
            "latest_value": latest_value,
            "latest_date": latest_date,
            "observation_start": start_date,
            "observation_end": end_date,
            "data_points": len(obs_list),
            "observations": obs_list[-validated.limit :]
            if validated.limit
            else obs_list,
        }

        regime = _detect_regime(obs_list)
        if regime is not None:
            result_data["regime_stats"] = regime

        if latest_value is not None:
            rate_futures = _fetch_rate_futures(series_id, latest_value, cutoff)
            if rate_futures is not None:
                result_data["rate_futures"] = rate_futures

        return mcp_success(result_data)

    except Exception as e:
        logger.exception("FRED series lookup failed")
        return mcp_error(f"FRED series lookup failed for {series_id}: {e}")


def _enrich_fred_top_result(fred: object, top: dict[str, object]) -> None:
    """Fetch latest observation for the top search result (best-effort)."""
    try:
        series_id = str(top.get("id", ""))
        if not series_id:
            return
        obs = fred.get_series(series_id)  # type: ignore[union-attr]
        if obs is None or obs.empty:
            return
        obs = obs.dropna()
        if obs.empty:
            return
        top["latest_value"] = float(obs.iloc[-1])
        top["latest_date"] = str(obs.index[-1])[:10]
    except Exception:
        pass


@tool(
    "fred_search",
    (
        "Search FRED for economic data series by keyword. USE THIS when you don't know "
        "the series ID for an economic indicator — search for 'inflation', 'GDP', "
        "'unemployment', 'interest rate', 'CPI', etc. to find the right series ID, "
        "then use fred_series to get the actual data. "
        "Automatically includes the latest observation for the top result.\n\n"
        "Examples:\n"
        '  fred_search(query="SOFR rate") → find the series ID for SOFR + latest value\n'
        '  fred_search(query="housing starts seasonally adjusted") → find HOUST or similar\n'
        "Two-step workflow: fred_search to find the ID, then fred_series to get data."
    ),
    FredSearchInput.model_json_schema(),
)
@tracked("fred_search")
async def fred_search(args: dict[str, Any]) -> dict[str, Any]:
    """Search for FRED series."""
    try:
        validated = FredSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    api_key = settings.fred_api_key
    if not api_key:
        return mcp_error(
            "FRED_API_KEY not configured. Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html"
        )

    try:
        from fredapi import Fred

        fred = Fred(api_key=api_key)

        # Search for series
        results = fred.search(validated.query)

        if results is None or len(results) == 0:
            return mcp_success(
                {
                    "query": validated.query,
                    "results": [],
                    "total_found": 0,
                }
            )

        # Convert to list of dicts (results is a DataFrame)
        series_list = []
        for idx, row in results.head(validated.limit).iterrows():
            series_list.append(
                {
                    "id": str(idx),
                    "title": str(row.get("title", "")),
                    "frequency": str(row.get("frequency", "")),
                    "units": str(row.get("units", "")),
                    "popularity": int(row.get("popularity") or 0),
                }
            )

        if series_list:
            _enrich_fred_top_result(fred, series_list[0])

        return mcp_success(
            {
                "query": validated.query,
                "results": series_list,
                "total_found": len(results),
            }
        )

    except Exception as e:
        logger.exception("FRED search failed")
        return mcp_error(f"FRED search failed: {e}")


# --- Company Financials (yfinance) ---


_FALLBACK_EARNINGS_LAG = timedelta(days=45)


def _build_earnings_release_map(ticker_obj: object) -> dict[date, date]:
    """Map fiscal period-end dates to their actual earnings release dates.

    Returns {period_end: earnings_release_date} built from yfinance
    earnings_dates. Falls back to empty dict on any error.
    """
    import yfinance as yf

    if not isinstance(ticker_obj, yf.Ticker):
        return {}
    try:
        df = ticker_obj.get_earnings_dates(limit=40)
        if df is None or df.empty:
            return {}
    except Exception:
        return {}

    import pandas as pd

    eh = ticker_obj.get_earnings_history()
    if eh is None or not isinstance(eh, pd.DataFrame) or eh.empty:
        return {}

    release_map: dict[date, date] = {}
    for idx in eh.index:
        quarter_end: date
        if hasattr(idx, "date"):
            quarter_end = idx.date()
        elif isinstance(idx, str):
            quarter_end = datetime.strptime(idx, "%Y-%m-%d").date()
        else:
            continue

        for earnings_dt in df.index:
            edt: date = (
                earnings_dt.date() if hasattr(earnings_dt, "date") else earnings_dt
            )
            if abs((edt - quarter_end).days) <= 60:
                release_map[quarter_end] = edt
                break

    return release_map


def _period_available_before(
    period_end: date, cutoff: date, release_map: dict[date, date]
) -> bool:
    """Check if a fiscal period's data would have been public before cutoff."""
    release_date = release_map.get(period_end)
    if release_date is not None:
        return release_date <= cutoff
    return period_end + _FALLBACK_EARNINGS_LAG <= cutoff


class CompanyFinancialsInput(BaseModel):
    """Input for company financial data lookup."""

    ticker: str = Field(
        min_length=1,
        max_length=10,
        description="Stock ticker symbol (e.g., GOOG, AAPL, MSFT)",
    )
    period: str = Field(
        default="quarterly",
        description="'quarterly' or 'annual'",
    )


@tool(
    "company_financials",
    (
        "Get quarterly or annual income statements for a public company. "
        "USE THIS FIRST for any earnings/revenue forecast question — provides "
        "historical revenue, net income, EPS, and growth trends. "
        "Ticker symbols: GOOG (Alphabet), AAPL (Apple), LLY (Eli Lilly), etc. "
        "For regional/segment breakdowns, supplement with search_exa on earnings press releases.\n\n"
        "Examples:\n"
        '  company_financials(ticker="MSFT") → last 8 quarters of income statements\n'
        '  company_financials(ticker="GOOG", period="annual") → last 8 years of annual financials\n'
        "Returns: Revenue, Net Income, EPS, Operating Income, Gross Profit, etc. per period."
    ),
    CompanyFinancialsInput.model_json_schema(),
)
@tracked("company_financials")
async def company_financials(args: dict[str, Any]) -> dict[str, Any]:
    """Get company financial statements via yfinance."""
    try:
        validated = CompanyFinancialsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    try:
        import yfinance as yf

        ticker = yf.Ticker(validated.ticker.upper())

        if validated.period == "annual":
            income = ticker.financials
        else:
            income = ticker.quarterly_financials

        if income is None or income.empty:
            return mcp_error(f"No financial data found for {validated.ticker.upper()}")

        cutoff = retrodict_cutoff.get()
        if cutoff is not None:
            release_map = _build_earnings_release_map(ticker)
            income = income.loc[
                :,
                [
                    col
                    for col in income.columns
                    if _period_available_before(
                        col.date() if hasattr(col, "date") else col,
                        cutoff,
                        release_map,
                    )
                ],
            ]
            if income.empty:
                return mcp_error(
                    f"No financial data available for {validated.ticker.upper()}"
                )

        # Convert DataFrame to serializable format
        # Columns are dates, rows are line items
        periods: list[dict[str, Any]] = []
        for col in income.columns:
            period_data: dict[str, Any] = {"period_end": str(col)[:10]}
            for row_name in income.index:
                value = income.loc[row_name, col]
                if value == value:  # not NaN
                    period_data[str(row_name)] = float(value)
            periods.append(period_data)

        # Also get basic info
        info = ticker.info or {}

        return mcp_success(
            {
                "ticker": validated.ticker.upper(),
                "company_name": info.get("shortName", validated.ticker.upper()),
                "period_type": validated.period,
                "num_periods": len(periods),
                "financials": periods[:8],  # Last 8 periods
            }
        )

    except Exception as e:
        logger.exception("Company financials lookup failed")
        return mcp_error(f"Failed to fetch financials for {validated.ticker}: {e}")


# --- Stock Price Tools (Yahoo Finance) ---


class StockPriceInput(BaseModel):
    """Input for stock price with optional history."""

    symbol: str = Field(min_length=1, max_length=10)
    history_days: int | None = Field(
        default=30,
        ge=1,
        le=365,
        description=(
            "Include daily closing prices for this many days. "
            "Default 30. Set to null to skip."
        ),
    )


class StockQueryInput(BaseModel):
    """Input for stock history tool."""

    symbol: str = Field(min_length=1, max_length=10)
    period: str = Field(
        default="1mo"
    )  # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    end_date: str | None = Field(default=None)


class DailyClose(TypedDict):
    """A single day's closing price."""

    date: str
    close: float


class PricePoint(TypedDict):
    """A notable price point in recent history."""

    date: str
    close: float
    days_ago: int


class TrailingReturns(TypedDict, total=False):
    """Percentage returns over trailing windows."""

    five_day: float
    ten_day: float
    twenty_day: float


class SummaryStats(TypedDict, total=False):
    """Derived statistics computed from recent price history."""

    drawdown_from_52w_high_pct: float
    distance_from_52w_low_pct: float
    trailing_returns: TrailingReturns
    trailing_volatility_20d: float
    trailing_mean_return_20d: float
    recent_low: PricePoint
    recent_high: PricePoint
    max_bounce_from_recent_low_pct: float


class FuturesContract(TypedDict):
    """A single futures contract month."""

    symbol: str
    month: str
    price: float


class FuturesCurve(TypedDict, total=False):
    """Term structure for futures symbols."""

    contracts: list[FuturesContract]
    structure: str
    front_month_symbol: str


class ShockAlert(TypedDict):
    """Alert when a large single-day move is detected in recent history."""

    event: str
    daily_return_pct: float
    comparable_events: int
    median_forward_return_pct: float
    pct_positive: float
    horizon_days: int


class _StockPriceOptional(TypedDict, total=False):
    summary_stats: SummaryStats
    futures_curve: FuturesCurve
    shock_alert: ShockAlert


class StockPrice(_StockPriceOptional):
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
    recent_history: list[DailyClose] | None


class ReturnDistribution(TypedDict):
    """Percentile distribution of returns."""

    mean: float
    median: float
    std: float
    p10: float
    p25: float
    p75: float
    p90: float
    min: float
    max: float


class StockConditionalReturnsInput(BaseModel):
    """Input for conditional return analysis."""

    trigger_type: str = Field(
        default="drawdown",
        description=(
            "'drawdown' (default): forward returns when price is down >= threshold "
            "from 52-week high. 'single_day': forward returns after a single-day "
            "move exceeding threshold."
        ),
    )
    drawdown_pct: float = Field(
        default=15.0,
        ge=3.0,
        le=80.0,
        description=(
            "For drawdown: threshold from 52-week high (%). "
            "For single_day: minimum absolute daily return (%). "
            "E.g. 5 means 'down >=5% in one day' or 'down >=5% from 52w high'."
        ),
    )
    horizon_days: int = Field(
        ge=1,
        le=60,
        description="Forward horizon in trading days to measure returns.",
    )
    reference_index: str = Field(
        default="^GSPC",
        description="Index or ticker to analyze. Default: S&P 500. Also: ^DJI, ^IXIC, ^RUT, BZ=F, CL=F.",
    )


class ConditionalReturnStats(TypedDict):
    """Historical return distribution conditioned on drawdown magnitude."""

    reference_index: str
    condition: str
    horizon_days: int
    total_events: int
    pct_positive: float
    return_distribution: ReturnDistribution
    data_period: str


def _augment_stock_history(ticker: object, result: StockPrice, days: int) -> None:
    """Add recent daily closing prices to a stock price result (best-effort)."""
    try:
        if days <= 5:
            period = "5d"
        elif days <= 30:
            period = "1mo"
        elif days <= 90:
            period = "3mo"
        elif days <= 180:
            period = "6mo"
        else:
            period = "1y"
        hist = ticker.history(period=period)  # type: ignore[union-attr]
        if hist is not None and not hist.empty:
            result["recent_history"] = [
                DailyClose(
                    date=idx.strftime("%Y-%m-%d"),
                    close=round(float(row["Close"]), 2),
                )
                for idx, row in hist.tail(days).iterrows()
            ]
    except Exception:
        pass


def _compute_summary_stats(result: StockPrice) -> SummaryStats | None:
    """Compute derived statistics from a stock price result.

    Returns None if recent_history is missing or too short.
    """
    history = result.get("recent_history")
    if not history or len(history) < 2:
        return None

    closes = [entry["close"] for entry in history]
    current = closes[-1]
    n = len(closes)

    stats = SummaryStats()

    # Drawdown from 52w high and distance from 52w low
    high = result.get("fifty_two_week_high")
    low = result.get("fifty_two_week_low")
    if high and high > 0:
        stats["drawdown_from_52w_high_pct"] = (current - high) / high * 100
    if low and low > 0:
        stats["distance_from_52w_low_pct"] = (current - low) / low * 100

    # Trailing returns over standard windows
    returns = TrailingReturns()
    if n > 5:
        returns["five_day"] = (closes[-1] - closes[-6]) / closes[-6] * 100
    if n > 10:
        returns["ten_day"] = (closes[-1] - closes[-11]) / closes[-11] * 100
    if n > 20:
        returns["twenty_day"] = (closes[-1] - closes[-21]) / closes[-21] * 100
    if returns:
        stats["trailing_returns"] = returns

    # Daily log returns for volatility / mean
    log_returns = [
        math.log(closes[i] / closes[i - 1])
        for i in range(max(1, n - 20), n)
        if closes[i - 1] > 0
    ]
    if len(log_returns) >= 5:
        mean_ret = sum(log_returns) / len(log_returns)
        variance = sum((r - mean_ret) ** 2 for r in log_returns) / len(log_returns)
        stats["trailing_volatility_20d"] = math.sqrt(variance) * 100
        stats["trailing_mean_return_20d"] = mean_ret * 100

    # Recent low and high within the history window
    min_close = min(closes)
    min_idx = closes.index(min_close)
    stats["recent_low"] = PricePoint(
        date=history[min_idx]["date"],
        close=min_close,
        days_ago=n - 1 - min_idx,
    )

    max_close = max(closes)
    max_idx = closes.index(max_close)
    stats["recent_high"] = PricePoint(
        date=history[max_idx]["date"],
        close=max_close,
        days_ago=n - 1 - max_idx,
    )

    # Max bounce from recent low (max close after the low vs the low)
    if min_idx < n - 1 and min_close > 0:
        post_low_max = max(closes[min_idx + 1 :])
        stats["max_bounce_from_recent_low_pct"] = (
            (post_low_max - min_close) / min_close * 100
        )

    return stats


_SHOCK_THRESHOLD_PCT = 4.0
_SHOCK_HORIZON_DAYS = 10


def _detect_shock(
    symbol: str, recent_history: list[DailyClose], cutoff: date | None
) -> ShockAlert | None:
    """Detect large single-day moves and compute recovery stats from history.

    Scans the last 5 days of recent_history for moves > _SHOCK_THRESHOLD_PCT.
    If found, fetches 5 years of history for the same symbol and computes
    forward return statistics after comparable single-day shocks.
    """
    if not recent_history or len(recent_history) < 2:
        return None

    # Scan last 5 days for a shock
    shock_idx: int | None = None
    shock_return: float = 0.0
    lookback = min(5, len(recent_history) - 1)
    for i in range(len(recent_history) - 1, len(recent_history) - 1 - lookback, -1):
        prev_close = recent_history[i - 1]["close"]
        if prev_close <= 0:
            continue
        daily_ret = (recent_history[i]["close"] - prev_close) / prev_close * 100
        if abs(daily_ret) >= _SHOCK_THRESHOLD_PCT:
            shock_idx = i
            shock_return = daily_ret
            break

    if shock_idx is None:
        return None

    shock_date = recent_history[shock_idx]["date"]
    direction = "drop" if shock_return < 0 else "spike"
    event = f"{shock_date} {direction}: {shock_return:+.1f}%"

    # Fetch longer history to find comparable events
    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)
        if cutoff is not None:
            hist = ticker.history(
                start=(cutoff - timedelta(days=5 * 365)).isoformat(),
                end=cutoff.isoformat(),
            )
        else:
            hist = ticker.history(period="5y")

        if hist is None or len(hist) < 252 + _SHOCK_HORIZON_DAYS:
            return ShockAlert(
                event=event,
                daily_return_pct=round(shock_return, 2),
                comparable_events=0,
                median_forward_return_pct=0.0,
                pct_positive=0.0,
                horizon_days=_SHOCK_HORIZON_DAYS,
            )

        closes: np.ndarray[Any, np.dtype[np.floating[Any]]] = np.asarray(
            hist["Close"].values, dtype=float
        )
        daily_returns = np.diff(closes) / closes[:-1] * 100

        # Find comparable shocks (same direction, similar magnitude)
        threshold = abs(shock_return)
        if shock_return < 0:
            event_indices = np.where(daily_returns <= -threshold)[0]
        else:
            event_indices = np.where(daily_returns >= threshold)[0]

        # Compute forward returns with minimum spacing
        forward_returns: list[float] = []
        last_event = -_SHOCK_HORIZON_DAYS
        for idx in event_indices:
            close_idx = idx + 1  # daily_returns[idx] is the return from idx to idx+1
            if close_idx + _SHOCK_HORIZON_DAYS >= len(closes):
                continue
            if idx - last_event < _SHOCK_HORIZON_DAYS:
                continue
            last_event = idx
            fwd = (
                (closes[close_idx + _SHOCK_HORIZON_DAYS] - closes[close_idx])
                / closes[close_idx]
                * 100
            )
            forward_returns.append(float(fwd))

        if not forward_returns:
            return ShockAlert(
                event=event,
                daily_return_pct=round(shock_return, 2),
                comparable_events=0,
                median_forward_return_pct=0.0,
                pct_positive=0.0,
                horizon_days=_SHOCK_HORIZON_DAYS,
            )

        returns_arr = np.array(forward_returns)
        return ShockAlert(
            event=event,
            daily_return_pct=round(shock_return, 2),
            comparable_events=len(forward_returns),
            median_forward_return_pct=round(float(np.median(returns_arr)), 2),
            pct_positive=round(
                float(np.sum(returns_arr > 0)) / len(returns_arr) * 100, 1
            ),
            horizon_days=_SHOCK_HORIZON_DAYS,
        )

    except Exception:
        logger.debug("Shock detection history fetch failed for %s", symbol)
        return ShockAlert(
            event=event,
            daily_return_pct=round(shock_return, 2),
            comparable_events=0,
            median_forward_return_pct=0.0,
            pct_positive=0.0,
            horizon_days=_SHOCK_HORIZON_DAYS,
        )


_FUTURES_MONTH_CODES = {
    1: "F",
    2: "G",
    3: "H",
    4: "J",
    5: "K",
    6: "M",
    7: "N",
    8: "Q",
    9: "U",
    10: "V",
    11: "X",
    12: "Z",
}

_FUTURES_MONTH_NAMES = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}


def _fetch_futures_curve(
    info: dict[str, Any], cutoff: date | None
) -> FuturesCurve | None:
    """Fetch nearby futures contracts to build a term structure.

    Uses the underlyingSymbol from a =F ticker to determine the root,
    exchange, and current front month, then fetches the next 3 contracts.
    """
    import yfinance as yf

    underlying = info.get("underlyingSymbol", "")
    if not underlying or "." not in underlying:
        return None

    # Parse: e.g. "BZK26.NYM" → root="BZ", month_code="K", year=26, exchange="NYM"
    base, exchange = underlying.rsplit(".", 1)
    if len(base) < 3:
        return None

    root = base[:-3]
    front_month_code = base[-3]
    try:
        front_year = int(base[-2:])
    except ValueError:
        return None

    # Map month code back to month number
    code_to_month = {v: k for k, v in _FUTURES_MONTH_CODES.items()}
    front_month = code_to_month.get(front_month_code)
    if front_month is None:
        return None

    contracts: list[FuturesContract] = []

    # Fetch front month + next 3 contracts
    for offset in range(4):
        m = (front_month - 1 + offset) % 12 + 1
        y = front_year + (front_month - 1 + offset) // 12
        code = _FUTURES_MONTH_CODES[m]
        symbol = f"{root}{code}{y:02d}.{exchange}"
        month_label = f"{_FUTURES_MONTH_NAMES[m]} 20{y:02d}"

        try:
            ticker = yf.Ticker(symbol)
            if cutoff is not None:
                hist = ticker.history(
                    start=(cutoff - timedelta(days=5)).isoformat(),
                    end=cutoff.isoformat(),
                )
            else:
                hist = ticker.history(period="5d")

            if hist is not None and not hist.empty:
                last_close = float(hist["Close"].iloc[-1])
                contracts.append(
                    FuturesContract(
                        symbol=symbol,
                        month=month_label,
                        price=round(last_close, 2),
                    )
                )
        except Exception:
            continue

    if len(contracts) < 2:
        return None

    # Determine term structure direction
    prices = [c["price"] for c in contracts]
    if prices[-1] > prices[0]:
        structure = "contango"
    elif prices[-1] < prices[0]:
        structure = "backwardation"
    else:
        structure = "flat"

    return FuturesCurve(
        contracts=contracts,
        structure=structure,
        front_month_symbol=underlying,
    )


@tool(
    "stock_price",
    (
        "Get current stock price and key metrics for a ticker symbol using Yahoo Finance. "
        "Returns current price, previous close, 52-week range, market cap, and recent "
        "daily closing prices (last 30 days by default). "
        "For futures symbols (e.g. BZ=F, CL=F, GC=F), also returns a futures_curve "
        "with nearby contract prices and term structure (contango/backwardation).\n\n"
        "Examples:\n"
        "  stock_price(symbol='AAPL') → current Apple price, metrics, and 30-day history\n"
        "  stock_price(symbol='BZ=F') → Brent crude price, 30-day history, and futures curve\n"
        "  stock_price(symbol='^GSPC') → current S&P 500 level with recent history"
    ),
    StockPriceInput.model_json_schema(),
)
@tracked("stock_price")
async def stock_price(args: dict[str, Any]) -> dict[str, Any]:
    """Get stock price from Yahoo Finance."""
    try:
        validated = StockPriceInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    symbol = validated.symbol.upper()
    cutoff = retrodict_cutoff.get()

    try:
        import yfinance as yf

        ticker = yf.Ticker(symbol)

        if cutoff is not None:
            end_str = cutoff.isoformat()
            start_52w = (cutoff - timedelta(days=365)).isoformat()
            hist_52w = ticker.history(start=start_52w, end=end_str)
            if hist_52w.empty:
                return mcp_error(f"No recent data found for {symbol}")

            all_closes: list[float] = hist_52w["Close"].tolist()
            all_dates: list[str] = [str(d.date()) for d in hist_52w.index.tolist()]
            history_days = validated.history_days or 30
            recent = [
                DailyClose(date=d, close=c)
                for d, c in zip(all_dates[-history_days:], all_closes[-history_days:])
            ]

            result: StockPrice = {
                "symbol": symbol,
                "name": ticker.info.get("shortName", symbol),
                "current_price": all_closes[-1],
                "previous_close": all_closes[-2] if len(all_closes) > 1 else None,
                "change_percent": None,
                "currency": ticker.info.get("currency", "USD"),
                "market_cap": None,
                "fifty_two_week_high": max(all_closes),
                "fifty_two_week_low": min(all_closes),
                "recent_history": recent if recent else None,
            }

            summary = _compute_summary_stats(result)
            if summary is not None:
                result["summary_stats"] = summary

            if recent:
                shock = _detect_shock(symbol, recent, cutoff)
                if shock is not None:
                    result["shock_alert"] = shock

            if symbol.endswith("=F"):
                curve = _fetch_futures_curve(ticker.info, cutoff)
                if curve is not None:
                    result["futures_curve"] = curve

            return mcp_success(result)

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
            "recent_history": None,
        }

        if cutoff is None and validated.history_days:
            _augment_stock_history(ticker, result, validated.history_days)

        summary = _compute_summary_stats(result)
        if summary is not None:
            result["summary_stats"] = summary

        history = result.get("recent_history")
        if history:
            shock = _detect_shock(symbol, history, cutoff)
            if shock is not None:
                result["shock_alert"] = shock

        if symbol.endswith("=F"):
            curve = _fetch_futures_curve(info, cutoff)
            if curve is not None:
                result["futures_curve"] = curve

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

        if end_date:
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
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

        hist_reset = hist.reset_index()
        hist_reset["Date"] = hist_reset["Date"].dt.strftime("%Y-%m-%d")

        records: list[dict[str, object]] = hist_reset[
            ["Date", "Open", "High", "Low", "Close", "Volume"]
        ].to_dict("records")  # pyright: ignore[reportCallIssue]

        formatted: list[dict[str, object]] = [
            {
                "date": r["Date"],
                "open": r["Open"],
                "high": r["High"],
                "low": r["Low"],
                "close": r["Close"],
                "volume": r["Volume"],
            }
            for r in records[-30:]
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


# --- Conditional Returns ---


@cached(ttl=3600)
async def _fetch_index_closes(symbol: str, end_date: str | None) -> list[DailyClose]:
    """Fetch max daily close history for an index.

    Returns a list of DailyClose sorted by date. Cached for 1 hour.
    """
    import yfinance as yf

    ticker = yf.Ticker(symbol)
    kwargs: dict[str, str] = {"period": "max"}
    if end_date is not None:
        kwargs = {"start": "1960-01-01", "end": end_date}
    hist = ticker.history(**kwargs)
    if hist is None or hist.empty:
        return []
    closes: list[float] = hist["Close"].tolist()
    dates: list[str] = [str(d.date()) for d in hist.index.tolist()]
    return [DailyClose(date=d, close=c) for d, c in zip(dates, closes)]


def _compute_conditional_return_stats(
    closes: list[DailyClose],
    drawdown_pct: float,
    horizon_days: int,
) -> ConditionalReturnStats | str:
    """Compute forward return distribution conditioned on drawdown magnitude.

    Returns ConditionalReturnStats on success, or an error message string.
    """
    if len(closes) < 252 + horizon_days:
        return "Insufficient data: need at least 252 + horizon_days data points"

    close_arr = np.array([e["close"] for e in closes])
    date_arr = [e["date"] for e in closes]

    rolling_high = np.empty_like(close_arr)
    for i in range(len(close_arr)):
        start = max(0, i - 251)
        rolling_high[i] = close_arr[start : i + 1].max()

    drawdown = (close_arr - rolling_high) / rolling_high * 100

    threshold = -drawdown_pct
    events: list[int] = []
    for i in range(252, len(close_arr) - horizon_days):
        if drawdown[i] <= threshold:
            if not events or (i - events[-1]) > horizon_days:
                events.append(i)

    if not events:
        return f"No events found where drawdown >= {drawdown_pct}%"

    forward_returns: list[float] = []
    for idx in events:
        future_idx = idx + horizon_days
        ret = (close_arr[future_idx] - close_arr[idx]) / close_arr[idx] * 100
        forward_returns.append(float(ret))

    returns_arr = np.array(forward_returns)
    positive_count = int(np.sum(returns_arr > 0))

    return ConditionalReturnStats(
        reference_index="",
        condition=f"52-week drawdown >= {drawdown_pct}%",
        horizon_days=horizon_days,
        total_events=len(forward_returns),
        pct_positive=positive_count / len(forward_returns) * 100,
        return_distribution=ReturnDistribution(
            mean=float(np.mean(returns_arr)),
            median=float(np.median(returns_arr)),
            std=float(np.std(returns_arr, ddof=1)) if len(returns_arr) > 1 else 0.0,
            p10=float(np.percentile(returns_arr, 10)),
            p25=float(np.percentile(returns_arr, 25)),
            p75=float(np.percentile(returns_arr, 75)),
            p90=float(np.percentile(returns_arr, 90)),
            min=float(np.min(returns_arr)),
            max=float(np.max(returns_arr)),
        ),
        data_period=f"{date_arr[0]} to {date_arr[-1]}",
    )


def _compute_single_day_shock_stats(
    closes: list[DailyClose],
    threshold_pct: float,
    horizon_days: int,
) -> ConditionalReturnStats | str:
    """Compute forward return distribution after single-day moves exceeding threshold.

    Looks for days where the absolute daily return >= threshold_pct, then
    measures the forward return over horizon_days after each event.
    """
    if len(closes) < 252 + horizon_days:
        return "Insufficient data: need at least 252 + horizon_days data points"

    close_arr = np.array([e["close"] for e in closes], dtype=float)
    date_arr = [e["date"] for e in closes]

    daily_returns = np.diff(close_arr) / close_arr[:-1] * 100

    # Find single-day shocks (negative direction: drops)
    neg_events: list[int] = []
    pos_events: list[int] = []
    for i in range(len(daily_returns)):
        if daily_returns[i] <= -threshold_pct:
            neg_events.append(i)
        elif daily_returns[i] >= threshold_pct:
            pos_events.append(i)

    # Use whichever direction has more events, or negative by default
    if len(neg_events) >= len(pos_events):
        event_indices = neg_events
        direction = "drop"
    else:
        event_indices = pos_events
        direction = "spike"

    if not event_indices:
        return f"No single-day moves >= {threshold_pct}% found in history"

    # Compute forward returns with minimum spacing
    forward_returns: list[float] = []
    last_event = -horizon_days
    for idx in event_indices:
        close_idx = idx + 1  # daily_returns[idx] = return from idx to idx+1
        if close_idx + horizon_days >= len(close_arr):
            continue
        if idx - last_event < horizon_days:
            continue
        last_event = idx
        fwd = (
            (close_arr[close_idx + horizon_days] - close_arr[close_idx])
            / close_arr[close_idx]
            * 100
        )
        forward_returns.append(float(fwd))

    if not forward_returns:
        return f"No single-day {direction}s >= {threshold_pct}% with sufficient forward data"

    returns_arr = np.array(forward_returns)
    positive_count = int(np.sum(returns_arr > 0))

    return ConditionalReturnStats(
        reference_index="",
        condition=f"single-day {direction} >= {threshold_pct}%",
        horizon_days=horizon_days,
        total_events=len(forward_returns),
        pct_positive=positive_count / len(forward_returns) * 100,
        return_distribution=ReturnDistribution(
            mean=float(np.mean(returns_arr)),
            median=float(np.median(returns_arr)),
            std=float(np.std(returns_arr, ddof=1)) if len(returns_arr) > 1 else 0.0,
            p10=float(np.percentile(returns_arr, 10)),
            p25=float(np.percentile(returns_arr, 25)),
            p75=float(np.percentile(returns_arr, 75)),
            p90=float(np.percentile(returns_arr, 90)),
            min=float(np.min(returns_arr)),
            max=float(np.max(returns_arr)),
        ),
        data_period=f"{date_arr[0]} to {date_arr[-1]}",
    )


@tool(
    "stock_conditional_returns",
    (
        "Get the empirical distribution of forward returns conditioned on market events. "
        "Two trigger types:\n\n"
        "  trigger_type='drawdown' (default): Forward returns when price is down >= "
        "threshold from 52-week high. E.g. 'when the S&P 500 is down >=25% from its "
        "52-week high, what does the next 10 days look like?'\n\n"
        "  trigger_type='single_day': Forward returns after a single-day move exceeding "
        "threshold. E.g. 'when Brent crude drops >=5% in one day, what does the next "
        "10 days look like?' Use this to quantify mean-reversion after shocks.\n\n"
        "Works with any ticker: indices (^GSPC), stocks (AAPL), futures (BZ=F, CL=F)."
    ),
    StockConditionalReturnsInput.model_json_schema(),
)
@tracked("stock_conditional_returns")
async def stock_conditional_returns(args: dict[str, Any]) -> dict[str, Any]:
    try:
        validated = StockConditionalReturnsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    cutoff = retrodict_cutoff.get()
    end_date = cutoff.isoformat() if cutoff is not None else None

    try:
        closes = await _fetch_index_closes(validated.reference_index, end_date)
        if not closes:
            return mcp_error(f"No data found for: {validated.reference_index}")

        if validated.trigger_type == "single_day":
            result = _compute_single_day_shock_stats(
                closes, validated.drawdown_pct, validated.horizon_days
            )
        else:
            result = _compute_conditional_return_stats(
                closes, validated.drawdown_pct, validated.horizon_days
            )

        if isinstance(result, str):
            return mcp_error(result)

        result["reference_index"] = validated.reference_index
        return mcp_success(result)

    except Exception as e:
        logger.exception("Conditional return analysis failed")
        return mcp_error(f"Conditional return analysis failed: {e}")


# --- World Bank Tools ---


class WorldBankIndicatorInput(BaseModel):
    """Input for World Bank indicator data."""

    indicator: str = Field(
        min_length=1,
        description=(
            "World Bank indicator code (e.g. NY.GDP.MKTP.KD.ZG for GDP growth, "
            "FP.CPI.TOTL.ZG for inflation). Use world_bank_search to find codes."
        ),
    )
    country: str = Field(
        min_length=2,
        max_length=3,
        description="ISO 3166-1 alpha-3 country code (e.g. DEU, BRA, IND, CHN, USA)",
    )
    start_year: int | None = Field(
        default=None,
        description="Start year (default: 10 years ago)",
    )
    end_year: int | None = Field(
        default=None,
        description="End year (default: current year)",
    )


class WorldBankSearchInput(BaseModel):
    """Input for World Bank indicator search."""

    query: str = Field(
        min_length=1, description="Search term (e.g. 'GDP growth', 'inflation')"
    )
    limit: int = Field(default=10, ge=1, le=50)


class WBObservation(TypedDict):
    year: int
    value: float | None


class WBIndicatorInfo(TypedDict):
    id: str
    name: str


@tool(
    "world_bank_indicator",
    (
        "Get time series data for a World Bank indicator and country. "
        "USE THIS for non-US economic data — FRED only covers US data, so questions "
        "about other countries need World Bank. Covers GDP growth, inflation, trade, "
        "population, and 16,000+ indicators for 200+ countries.\n\n"
        "Common indicators:\n"
        "  NY.GDP.MKTP.KD.ZG — GDP growth (annual %)\n"
        "  FP.CPI.TOTL.ZG — Inflation, consumer prices (annual %)\n"
        "  SL.UEM.TOTL.ZS — Unemployment (% of labor force)\n"
        "  NE.TRD.GNFS.ZS — Trade (% of GDP)\n"
        "  SP.POP.TOTL — Population, total\n\n"
        "Use world_bank_search first if you don't know the indicator code."
    ),
    WorldBankIndicatorInput.model_json_schema(),
)
@tracked("world_bank_indicator")
async def world_bank_indicator(args: dict[str, Any]) -> dict[str, Any]:
    """Get World Bank indicator data for a country."""
    try:
        validated = WorldBankIndicatorInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    import wbgapi as wb  # type: ignore[import-untyped]

    cutoff = retrodict_cutoff.get()

    reference_year = cutoff.year if cutoff is not None else date.today().year
    end_year = validated.end_year or reference_year
    start_year = validated.start_year or (end_year - 10)

    if cutoff is not None and end_year > cutoff.year:
        end_year = cutoff.year

    try:
        info = wb.series.get(validated.indicator)
        if info is None:
            return mcp_error(f"Indicator '{validated.indicator}' not found.")
        indicator_info: WBIndicatorInfo = {
            "id": str(info["id"]),
            "name": str(info["value"]),
        }
    except Exception as e:
        return mcp_error(f"Indicator '{validated.indicator}' not found: {e}")

    try:
        country = validated.country.upper()
        time_range = f"YR{start_year}:YR{end_year}"
        data = list(
            wb.data.fetch(
                validated.indicator,
                country,
                time=time_range,
            )
        )

        observations: list[WBObservation] = []
        for row in data:
            year_str: str = row["time"]
            year = int(year_str.replace("YR", ""))
            observations.append(
                {
                    "year": year,
                    "value": row["value"],
                }
            )

        observations.sort(key=lambda o: o["year"])

        latest_value: float | None = None
        latest_year: int | None = None
        for obs in reversed(observations):
            if obs["value"] is not None:
                latest_value = obs["value"]
                latest_year = obs["year"]
                break

        return mcp_success(
            {
                "indicator": indicator_info,
                "country": country,
                "start_year": start_year,
                "end_year": end_year,
                "latest_value": latest_value,
                "latest_year": latest_year,
                "data_points": len(observations),
                "observations": observations,
            }
        )

    except Exception as e:
        logger.exception("World Bank indicator fetch failed")
        return mcp_error(
            f"Failed to fetch {validated.indicator} for {validated.country}: {e}"
        )


def _enrich_wb_top_result(wb: object, top: dict[str, object]) -> None:
    """Fetch latest global (WLD) value for the top search result (best-effort)."""
    try:
        indicator_id = str(top.get("id", ""))
        if not indicator_id:
            return
        data = list(wb.data.fetch(indicator_id, "WLD", mrnev=1))  # type: ignore[union-attr]
        if data and data[0].get("value") is not None:
            top["latest_value"] = data[0]["value"]
            year_str: str = data[0].get("time", "")
            if year_str:
                top["latest_year"] = int(year_str.replace("YR", ""))
    except Exception:
        pass


@tool(
    "world_bank_search",
    (
        "Search World Bank indicators by keyword. USE THIS when forecasting "
        "non-US economic questions — FRED only covers US data, World Bank covers "
        "200+ countries. Automatically includes the latest global value for the top result.\n\n"
        "Examples:\n"
        '  world_bank_search(query="GDP growth") → find indicator codes + latest global value\n'
        '  world_bank_search(query="inflation consumer prices") → find CPI indicators\n'
        "Two-step workflow: world_bank_search to find the code, then "
        "world_bank_indicator to get data."
    ),
    WorldBankSearchInput.model_json_schema(),
)
@tracked("world_bank_search")
async def world_bank_search(args: dict[str, Any]) -> dict[str, Any]:
    """Search for World Bank indicators by keyword."""
    try:
        validated = WorldBankSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    try:
        import wbgapi as wb  # type: ignore[import-untyped]

        results_iter = wb.series.list(q=validated.query)
        results: list[dict[str, object]] = []
        for item in results_iter:
            results.append(
                {
                    "id": item["id"],
                    "name": item["value"],
                }
            )
            if len(results) >= validated.limit:
                break

        if results:
            _enrich_wb_top_result(wb, results[0])

        return mcp_success(
            {
                "query": validated.query,
                "results": results,
                "total_found": len(results),
            }
        )

    except Exception as e:
        logger.exception("World Bank search failed")
        return mcp_error(f"World Bank search failed: {e}")


# --- MCP Server ---

_financial_tools = [
    company_financials,
    stock_price,
    stock_history,
    stock_conditional_returns,
]

if settings.fred_api_key:
    _financial_tools.extend([fred_series, fred_search])
else:
    logger.info("FRED tools disabled: FRED_API_KEY not configured")

_financial_tools.extend([world_bank_indicator, world_bank_search])


def create_financial_server():
    """Create the financial MCP server with all economic/financial data tools."""
    return create_mcp_server(
        name="financial",
        version="2.0.0",
        tools=_financial_tools,
    )
