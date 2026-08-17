# lup: ignore[any-type, dict-get]
# pandas, pytrends and Exa all answer untyped; the shapes below are what this
# module promises its caller, read key by key at that boundary.
"""Google Trends tools for search interest data.

These tools fetch Google Trends data to provide signal for questions
about search interest, trending topics, and relative popularity.
"""

import logging
import statistics
from itertools import takewhile
from typing import Any, Literal, TypedDict, cast

import pandas as pd
from pydantic import BaseModel, Field
from pytrends.exceptions import TooManyRequestsError
from pytrends.request import TrendReq
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from aib.retrodict_context import retrodict_cutoff
from aib.tools.throttle import trends_throttle
from lup.mcp import ToolError, lup_tool

logger = logging.getLogger(__name__)

type TrendDirection = Literal["up", "down", "stable", "insufficient_data"]


# --- Input Schemas ---


class TrendsQueryInput(BaseModel):
    """Input for Google Trends interest over time."""

    keyword: str = Field(min_length=1, description="Search term to get trends for")
    timeframe: str = Field(
        default="today 3-m",
        description=(
            "Time range. Presets: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', "
            "'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all'. "
            "Custom date range: 'YYYY-MM-DD YYYY-MM-DD' (e.g. '2026-01-24 2026-02-23'). "
            "Use custom ranges to match resolution URLs exactly."
        ),
    )
    geo: str = Field(
        default="",
        description="Geographic region (ISO 3166-1 alpha-2). Empty for worldwide.",
    )
    tz: int = Field(
        default=360,
        description=(
            "Timezone offset in minutes from UTC. Default 360 (CST/UTC-6). "
            "Use 0 for UTC — required when matching SerpAPI resolution scripts that specify tz=0."
        ),
    )
    include_related: bool = Field(
        default=True,
        description="Include top and rising related queries. Default: True.",
    )


class TrendsCompareInput(BaseModel):
    """Input for comparing multiple search terms."""

    keywords: list[str] = Field(
        min_length=1,
        max_length=5,
        description="List of search terms to compare (max 5)",
    )
    timeframe: str = Field(default="today 3-m")
    geo: str = Field(default="")
    tz: int = Field(default=360)


# --- Output Schemas ---


class TrendDataPoint(TypedDict):
    """A single data point in the trends time series."""

    date: str
    value: int  # 0-100 relative interest


class ChangeStats(TypedDict):
    """Period-over-period change statistics from the time series."""

    increases: int
    decreases: int
    no_change: int
    total: int
    increase_rate: float
    decrease_rate: float
    no_change_rate: float
    threshold: int


class RelatedQueries(TypedDict):
    """Related queries from Google Trends."""

    top_queries: list[dict[str, Any]]
    rising_queries: list[dict[str, Any]]


class ValuePoint(TypedDict):
    """A notable value point in the trends time series."""

    value: int
    date: str
    days_ago: int


class StableTailRange(TypedDict):
    """Min/max values within the stable tail."""

    low: int
    high: int


class TailStats(BaseModel):
    """Trailing-window statistics for regime detection.

    Every field is optional because each answers only when the series is long
    enough to support it — a three-point history has a peak but no trailing
    volatility.
    """

    stable_tail_days: int | None = None
    stable_tail_range: StableTailRange | None = None
    peak: ValuePoint | None = None
    trough: ValuePoint | None = None
    drawdown_from_peak_pct: float | None = None
    trailing_change_stats: ChangeStats | None = None
    trailing_volatility: float | None = None


class NewsItem(TypedDict):
    """A recent news headline related to a trends topic."""

    title: str
    url: str
    published_date: str | None


class TrendsResult(BaseModel):
    """Result from Google Trends query."""

    keyword: str
    timeframe: str
    geo: str
    data_points: int
    latest_value: int | None
    max_value: int
    min_value: int
    average_value: float
    trend_direction: TrendDirection
    change_stats: ChangeStats
    history: list[TrendDataPoint]
    related: RelatedQueries | None
    tail_stats: TailStats | None = None
    recent_news: list[NewsItem] | None = None


class TrendsEmpty(BaseModel):
    """Google Trends returned nothing for this query."""

    keyword: str
    timeframe: str
    geo: str
    data_points: int = 0
    message: str = "No data available for this query"
    history: list[TrendDataPoint] = []


class KeywordComparison(BaseModel):
    """One keyword's standing within a comparison."""

    latest_value: int | None
    max_value: int
    average_value: float
    trend_direction: TrendDirection


class TrendsCompareResult(BaseModel):
    """Relative interest across the compared keywords."""

    keywords: list[str]
    timeframe: str
    geo: str
    data_points: int
    comparison: dict[str, KeywordComparison]
    highest_average: str | None


class TrendsCompareEmpty(BaseModel):
    """Google Trends returned nothing for this comparison."""

    keywords: list[str]
    timeframe: str
    geo: str
    message: str = "No data available for this query"
    comparison: dict[str, KeywordComparison] = {}


# --- Google Trends API ---


def calculate_change_stats(values: list[int], threshold: int = 3) -> ChangeStats:
    """Compute period-over-period change statistics from a time series.

    Uses ±threshold to match MiniBench resolution criteria: changes within
    the threshold count as "no_change", not as increases or decreases.
    """
    diffs = [values[i] - values[i - 1] for i in range(1, len(values))]
    increases = sum(1 for d in diffs if d > threshold)
    decreases = sum(1 for d in diffs if d < -threshold)
    total = len(diffs)
    no_change = total - increases - decreases

    return ChangeStats(
        increases=increases,
        decreases=decreases,
        no_change=no_change,
        total=total,
        increase_rate=round(increases / total, 3) if total else 0.0,
        decrease_rate=round(decreases / total, 3) if total else 0.0,
        no_change_rate=round(no_change / total, 3) if total else 0.0,
        threshold=threshold,
    )


def calculate_trend_direction(values: list[int]) -> TrendDirection:
    """Determine trend direction from recent values."""
    if len(values) < 3:
        return "insufficient_data"

    # Compare last quarter to first quarter
    quarter_size = max(len(values) // 4, 1)
    first_quarter_avg = sum(values[:quarter_size]) / quarter_size
    last_quarter_avg = sum(values[-quarter_size:]) / quarter_size

    if first_quarter_avg == 0:
        return "up" if last_quarter_avg > 0 else "stable"

    change_pct = (last_quarter_avg - first_quarter_avg) / first_quarter_avg

    if change_pct > 0.15:
        return "up"
    if change_pct < -0.15:
        return "down"
    return "stable"


def stable_tail_length(values: list[int], threshold: int) -> int:
    """How many trailing points move by no more than *threshold* each step."""
    n = len(values)
    steps = (abs(values[i] - values[i - 1]) for i in range(n - 1, 0, -1))
    return sum(1 for _ in takewhile(lambda step: step <= threshold, steps))


def trough_point(values: list[int], dates: list[str]) -> ValuePoint | None:
    """The lowest reading, ignoring the leading zeros before a term existed."""
    first_nonzero = next((i for i, v in enumerate(values) if v > 0), 0)
    nonzero_values = values[first_nonzero:]
    if not nonzero_values:
        return None
    nonzero_dates = dates[first_nonzero:]
    min_val = min(nonzero_values)
    min_idx = nonzero_values.index(min_val)
    return ValuePoint(
        value=min_val,
        date=nonzero_dates[min_idx],
        days_ago=len(values) - 1 - (first_nonzero + min_idx),
    )


def compute_tail_stats(
    history: list[TrendDataPoint], threshold: int = 3
) -> TailStats | None:
    """Compute trailing-window statistics for regime detection.

    Returns None if history has fewer than 3 points.
    """
    if len(history) < 3:
        return None

    values = [p["value"] for p in history]
    dates = [p["date"] for p in history]
    n = len(values)

    stable_count = stable_tail_length(values, threshold)
    tail_values = values[n - stable_count - 1 :] if stable_count else []

    max_val = max(values)
    max_idx = values.index(max_val)

    trailing_window = min(7, n)
    trailing_values = values[-trailing_window:] if trailing_window >= 2 else []
    diffs = [
        trailing_values[i] - trailing_values[i - 1] for i in range(1, len(trailing_values))
    ]

    return TailStats(
        stable_tail_days=stable_count or None,
        stable_tail_range=(
            StableTailRange(low=min(tail_values), high=max(tail_values))
            if tail_values
            else None
        ),
        peak=ValuePoint(value=max_val, date=dates[max_idx], days_ago=n - 1 - max_idx),
        trough=trough_point(values, dates),
        drawdown_from_peak_pct=(
            round((values[-1] - max_val) / max_val * 100, 1) if max_val > 0 else None
        ),
        trailing_change_stats=(
            calculate_change_stats(trailing_values, threshold)
            if trailing_values
            else None
        ),
        trailing_volatility=(
            round(statistics.stdev(diffs), 2) if trailing_window >= 3 else None
        ),
    )


@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=60, min=60, max=300),
    retry=retry_if_exception_type(TooManyRequestsError),
    reraise=True,
)
def fetch_trends_data(
    keywords: list[str], timeframe: str, geo: str, tz: int
) -> tuple[TrendReq, pd.DataFrame]:
    """Fetch Google Trends data with retry on rate limits."""
    pytrends = TrendReq(hl="en-US", tz=tz)
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
    df = cast(pd.DataFrame, pytrends.interest_over_time())
    return pytrends, df


def fetch_related_queries(pytrends: Any, keyword: str) -> RelatedQueries | None:
    """Fetch related queries using an existing pytrends session."""
    try:
        related = pytrends.related_queries()
        if not related or keyword not in related:
            return None

        kw_data = related[keyword]
        top_queries = (
            [
                {"query": row["query"], "value": int(row["value"])}
                for _, row in kw_data["top"].head(10).iterrows()
            ]
            if kw_data.get("top") is not None and not kw_data["top"].empty
            else []
        )
        rising_queries = (
            [
                {"query": row["query"], "value": str(row["value"])}
                for _, row in kw_data["rising"].head(10).iterrows()
            ]
            if kw_data.get("rising") is not None and not kw_data["rising"].empty
            else []
        )

        if not top_queries and not rising_queries:
            return None

        return RelatedQueries(
            top_queries=top_queries, rising_queries=rising_queries
        )
    except Exception:
        logger.warning("Related queries failed for '%s'", keyword, exc_info=True)
        return None


async def fetch_recent_news(
    keyword: str, max_results: int = 5
) -> list[NewsItem] | None:
    """Fetch recent news headlines for an elevated trends topic via Exa."""
    from datetime import datetime, timedelta, timezone

    from aib.tools.exa import exa_search

    try:
        cutoff = retrodict_cutoff.get()
        if cutoff is not None:
            reference = datetime(
                cutoff.year, cutoff.month, cutoff.day, tzinfo=timezone.utc
            )
        else:
            reference = datetime.now(timezone.utc)
        after_date = (reference - timedelta(hours=48)).strftime("%Y-%m-%d")

        results = await exa_search(
            query=f"{keyword} news",
            num_results=max_results,
            published_after=after_date,
            livecrawl="always",
        )
        items = [
            NewsItem(
                title=r["title"] or "",
                url=r["url"] or "",
                published_date=r["published_date"],
            )
            for r in results
            if r.get("title")
        ]
        return items or None
    except Exception:
        logger.debug("News augmentation failed for '%s'", keyword, exc_info=True)
        return None


@lup_tool(
    (
        "Get Google Trends interest over time for a search term. Returns relative "
        "search interest (0-100) over the requested window, period-over-period "
        "change statistics, trailing-window regime statistics, and — when interest "
        "is elevated — recent news headlines explaining the movement.\n\n"
        "**Timeframe.** Presets cover the common windows; a custom "
        "'YYYY-MM-DD YYYY-MM-DD' range matches a resolution URL exactly, which is "
        "what a resolution-sensitive question needs.\n\n"
        "**Regime nuance.** A decayed spike and a flat baseline look alike in the "
        "latest value alone; tail_stats separates them, and a re-spike is common "
        "in weather- and event-driven terms, meaning a new weather system can "
        "re-spike search interest after a prior spike has decayed.\n\n"
        "**Resolution mechanism nuance.** Directional-change questions usually "
        "resolve via SerpAPI rather than the pytrends-derived values this tool "
        "returns. Small numeric differences between the two sources can flip the "
        "outcome across the threshold when the measured interest level sits near "
        "the baseline floor. Always query with tz=0 and the exact resolution "
        "date range, and leave meaningful probability on outcomes that a small "
        "measurement shift would produce."
    ),
    name="google_trends",
)
async def google_trends(params: TrendsQueryInput) -> TrendsResult | TrendsEmpty:
    """Get Google Trends interest over time for a keyword."""
    keyword = params.keyword
    timeframe = params.timeframe
    geo = params.geo
    tz = params.tz

    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        from aib.agent.retrodict import cap_trends_timeframe

        timeframe = cap_trends_timeframe(timeframe, cutoff)

    try:
        async with trends_throttle.slot():
            pytrends, df = fetch_trends_data([keyword], timeframe, geo, tz)

        if df.empty:
            return TrendsEmpty(
                keyword=keyword, timeframe=timeframe, geo=geo or "worldwide"
            )

        if keyword not in df.columns:
            raise ToolError(f"Keyword '{keyword}' not found in response")

        values = df[keyword].tolist()
        dates = [d.strftime("%Y-%m-%d") for d in pd.DatetimeIndex(df.index)]

        history: list[TrendDataPoint] = [
            TrendDataPoint(date=d, value=int(v)) for d, v in zip(dates, values)
        ]

        # Limit history to last 50 points for response size
        history = history[-50:]

        related = (
            fetch_related_queries(pytrends, keyword) if params.include_related else None
        )
        ints = [int(v) for v in values]
        latest_value = int(values[-1]) if values else None

        recent_news = (
            await fetch_recent_news(keyword)
            if latest_value is not None and latest_value >= 10
            else None
        )

        return TrendsResult(
            keyword=keyword,
            timeframe=timeframe,
            geo=geo or "worldwide",
            data_points=len(values),
            latest_value=latest_value,
            max_value=int(max(values)) if values else 0,
            min_value=int(min(values)) if values else 0,
            average_value=round(sum(values) / len(values), 1) if values else 0,
            trend_direction=calculate_trend_direction(ints),
            change_stats=calculate_change_stats(ints),
            history=history,
            related=related,
            tail_stats=compute_tail_stats(history),
            recent_news=recent_news,
        )

    except ToolError:
        raise
    except Exception as e:
        logger.exception("Google Trends lookup failed")
        raise ToolError(f"Google Trends lookup failed for '{keyword}': {e}") from e


@lup_tool(
    (
        "Compare Google Trends interest for multiple search terms. "
        "Returns relative search interest (0-100) for up to 5 terms. "
        "Values are relative to each other within the comparison. "
        "Useful for comparing popularity of different topics or candidates."
    ),
    name="google_trends_compare",
)
async def google_trends_compare(
    params: TrendsCompareInput,
) -> TrendsCompareResult | TrendsCompareEmpty:
    """Compare Google Trends interest for multiple keywords."""
    keywords = params.keywords
    timeframe = params.timeframe
    geo = params.geo
    tz = params.tz

    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        from aib.agent.retrodict import cap_trends_timeframe

        timeframe = cap_trends_timeframe(timeframe, cutoff)

    try:
        async with trends_throttle.slot():
            _, df = fetch_trends_data(keywords, timeframe, geo, tz)

        if df.empty:
            return TrendsCompareEmpty(
                keywords=keywords, timeframe=timeframe, geo=geo or "worldwide"
            )

        def compared(kw: str) -> KeywordComparison:
            values = df[kw].tolist()
            return KeywordComparison(
                latest_value=int(values[-1]) if values else None,
                max_value=int(max(values)) if values else 0,
                average_value=round(sum(values) / len(values), 1) if values else 0,
                trend_direction=calculate_trend_direction([int(v) for v in values]),
            )

        comparison = {kw: compared(kw) for kw in keywords if kw in df.columns}

        winner = (
            max(comparison.keys(), key=lambda k: comparison[k].average_value)
            if comparison
            else None
        )

        return TrendsCompareResult(
            keywords=keywords,
            timeframe=timeframe,
            geo=geo or "worldwide",
            data_points=len(df),
            comparison=comparison,
            highest_average=winner,
        )

    except ToolError:
        raise
    except Exception as e:
        logger.exception("Google Trends comparison failed")
        raise ToolError(f"Google Trends comparison failed: {e}") from e
