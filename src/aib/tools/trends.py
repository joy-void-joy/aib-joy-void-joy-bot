"""Google Trends tools for search interest data.

These tools fetch Google Trends data to provide signal for questions
about search interest, trending topics, and relative popularity.
"""

import logging
import statistics
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


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


class TailStats(TypedDict, total=False):
    """Trailing-window statistics for regime detection."""

    stable_tail_days: int
    stable_tail_range: StableTailRange
    peak: ValuePoint
    trough: ValuePoint
    drawdown_from_peak_pct: float
    trailing_change_stats: ChangeStats
    trailing_volatility: float


class NewsItem(TypedDict):
    """A recent news headline related to a trends topic."""

    title: str
    url: str
    published_date: str | None


class _TrendsResultOptional(TypedDict, total=False):
    tail_stats: TailStats
    recent_news: list[NewsItem]


class TrendsResult(_TrendsResultOptional):
    """Result from Google Trends query."""

    keyword: str
    timeframe: str
    geo: str
    data_points: int
    latest_value: int | None
    max_value: int
    min_value: int
    average_value: float
    trend_direction: str  # "up", "down", "stable"
    change_stats: ChangeStats
    history: list[TrendDataPoint]
    related: RelatedQueries | None


# --- Google Trends API ---


def _calculate_change_stats(values: list[int], threshold: int = 3) -> ChangeStats:
    """Compute period-over-period change statistics from a time series.

    Uses ±threshold to match MiniBench resolution criteria: changes within
    the threshold count as "no_change", not as increases or decreases.
    """
    increases = decreases = no_change = 0
    for i in range(1, len(values)):
        diff = values[i] - values[i - 1]
        if diff > threshold:
            increases += 1
        elif diff < -threshold:
            decreases += 1
        else:
            no_change += 1
    total = increases + decreases + no_change
    result: ChangeStats = {
        "increases": increases,
        "decreases": decreases,
        "no_change": no_change,
        "total": total,
        "increase_rate": round(increases / total, 3) if total else 0.0,
        "decrease_rate": round(decreases / total, 3) if total else 0.0,
        "no_change_rate": round(no_change / total, 3) if total else 0.0,
        "threshold": threshold,
    }
    return result


def _calculate_trend_direction(values: list[int]) -> str:
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
    elif change_pct < -0.15:
        return "down"
    else:
        return "stable"


def _compute_tail_stats(
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

    stats = TailStats()

    # --- Stable tail: consecutive days at end where |day-over-day| <= threshold ---
    stable_count = 0
    for i in range(n - 1, 0, -1):
        if abs(values[i] - values[i - 1]) <= threshold:
            stable_count += 1
        else:
            break

    if stable_count > 0:
        tail_values = values[n - stable_count - 1 :]
        stats["stable_tail_days"] = stable_count
        stats["stable_tail_range"] = StableTailRange(
            low=min(tail_values), high=max(tail_values)
        )

    # --- Peak and trough ---
    max_val = max(values)
    max_idx = values.index(max_val)
    stats["peak"] = ValuePoint(
        value=max_val, date=dates[max_idx], days_ago=n - 1 - max_idx
    )

    # Trough: lowest value excluding leading zeros
    first_nonzero = 0
    for i, v in enumerate(values):
        if v > 0:
            first_nonzero = i
            break
    nonzero_values = values[first_nonzero:]
    nonzero_dates = dates[first_nonzero:]
    if nonzero_values:
        min_val = min(nonzero_values)
        min_idx_in_nonzero = nonzero_values.index(min_val)
        abs_idx = first_nonzero + min_idx_in_nonzero
        stats["trough"] = ValuePoint(
            value=min_val,
            date=nonzero_dates[min_idx_in_nonzero],
            days_ago=n - 1 - abs_idx,
        )

    # --- Drawdown from peak ---
    latest = values[-1]
    if max_val > 0:
        stats["drawdown_from_peak_pct"] = round((latest - max_val) / max_val * 100, 1)

    # --- Trailing change stats and volatility (last 7 days) ---
    trailing_window = min(7, n)
    if trailing_window >= 2:
        trailing_values = values[-trailing_window:]
        stats["trailing_change_stats"] = _calculate_change_stats(
            trailing_values, threshold
        )
        if trailing_window >= 3:
            diffs = [
                trailing_values[i] - trailing_values[i - 1]
                for i in range(1, len(trailing_values))
            ]
            stats["trailing_volatility"] = round(statistics.stdev(diffs), 2)

    return stats


def _fetch_related_queries(pytrends: Any, keyword: str) -> RelatedQueries | None:
    """Fetch related queries using an existing pytrends session."""
    try:
        related = pytrends.related_queries()
        if not related or keyword not in related:
            return None

        kw_data = related[keyword]
        top_queries: list[dict[str, Any]] = []
        if kw_data.get("top") is not None and not kw_data["top"].empty:
            top_queries = [
                {"query": row["query"], "value": int(row["value"])}
                for _, row in kw_data["top"].head(10).iterrows()
            ]

        rising_queries: list[dict[str, Any]] = []
        if kw_data.get("rising") is not None and not kw_data["rising"].empty:
            rising_queries = [
                {"query": row["query"], "value": str(row["value"])}
                for _, row in kw_data["rising"].head(10).iterrows()
            ]

        if not top_queries and not rising_queries:
            return None

        return {"top_queries": top_queries, "rising_queries": rising_queries}
    except Exception:
        logger.warning("Related queries failed for '%s'", keyword, exc_info=True)
        return None


async def _fetch_recent_news(
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


@tool(
    "google_trends",
    (
        "Get Google Trends interest over time for a search term. "
        "Returns relative search interest (0-100) over the specified timeframe, "
        "plus top and rising related queries (included by default). "
        "Useful for questions about search trends, popularity, and public interest. "
        "Timeframes: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', "
        "'today 3-m', 'today 12-m', 'today 5-y', 'all', or 'YYYY-MM-DD YYYY-MM-DD' for exact ranges. "
        "Geo: ISO country code (e.g., 'US', 'GB') or empty for worldwide. "
        "Tz: timezone offset in minutes (default 360=CST). Use tz=0 to match SerpAPI resolution scripts."
    ),
    TrendsQueryInput.model_json_schema(),
)
@tracked("google_trends")
async def google_trends(args: dict[str, Any]) -> dict[str, Any]:
    """Get Google Trends interest over time for a keyword."""
    try:
        validated = TrendsQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    keyword = validated.keyword
    timeframe = validated.timeframe
    geo = validated.geo
    tz = validated.tz

    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        from aib.agent.retrodict import _cap_trends_timeframe

        timeframe = _cap_trends_timeframe(timeframe, cutoff)

    try:
        from pytrends.request import TrendReq

        pytrends = TrendReq(hl="en-US", tz=tz)

        # Build payload
        pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)

        # Get interest over time
        df = pytrends.interest_over_time()

        if df.empty:
            return mcp_success(
                {
                    "keyword": keyword,
                    "timeframe": timeframe,
                    "geo": geo or "worldwide",
                    "data_points": 0,
                    "message": "No data available for this query",
                    "history": [],
                }
            )

        # Extract values (exclude isPartial column)
        if keyword not in df.columns:
            return mcp_error(f"Keyword '{keyword}' not found in response")

        import pandas as pd

        values = df[keyword].tolist()
        dates = [d.strftime("%Y-%m-%d") for d in pd.DatetimeIndex(df.index)]

        # Build history
        history: list[TrendDataPoint] = [
            {"date": d, "value": int(v)} for d, v in zip(dates, values)
        ]

        # Limit history to last 50 points for response size
        if len(history) > 50:
            history = history[-50:]

        # Fetch related queries on the same session (no extra payload needed)
        related: RelatedQueries | None = None
        if validated.include_related:
            related = _fetch_related_queries(pytrends, keyword)

        result: TrendsResult = {
            "keyword": keyword,
            "timeframe": timeframe,
            "geo": geo or "worldwide",
            "data_points": len(values),
            "latest_value": int(values[-1]) if values else None,
            "max_value": int(max(values)) if values else 0,
            "min_value": int(min(values)) if values else 0,
            "average_value": round(sum(values) / len(values), 1) if values else 0,
            "trend_direction": _calculate_trend_direction([int(v) for v in values]),
            "change_stats": _calculate_change_stats([int(v) for v in values]),
            "history": history,
            "related": related,
        }

        tail_stats = _compute_tail_stats(history)
        if tail_stats is not None:
            result["tail_stats"] = tail_stats

        if result["latest_value"] is not None and result["latest_value"] >= 10:
            recent_news = await _fetch_recent_news(keyword)
            if recent_news:
                result["recent_news"] = recent_news

        return mcp_success(result)

    except Exception as e:
        logger.exception("Google Trends lookup failed")
        return mcp_error(f"Google Trends lookup failed for '{keyword}': {e}")


@tool(
    "google_trends_compare",
    (
        "Compare Google Trends interest for multiple search terms. "
        "Returns relative search interest (0-100) for up to 5 terms. "
        "Values are relative to each other within the comparison. "
        "Useful for comparing popularity of different topics or candidates."
    ),
    TrendsCompareInput.model_json_schema(),
)
@tracked("google_trends_compare")
async def google_trends_compare(args: dict[str, Any]) -> dict[str, Any]:
    """Compare Google Trends interest for multiple keywords."""
    try:
        validated = TrendsCompareInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    keywords = validated.keywords
    timeframe = validated.timeframe
    geo = validated.geo
    tz = validated.tz

    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        from aib.agent.retrodict import _cap_trends_timeframe

        timeframe = _cap_trends_timeframe(timeframe, cutoff)

    try:
        from pytrends.request import TrendReq

        pytrends = TrendReq(hl="en-US", tz=tz)

        # Build payload with all keywords
        pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)

        # Get interest over time
        df = pytrends.interest_over_time()

        if df.empty:
            return mcp_success(
                {
                    "keywords": keywords,
                    "timeframe": timeframe,
                    "geo": geo or "worldwide",
                    "message": "No data available for this query",
                    "comparison": {},
                }
            )

        # Build comparison results
        comparison: dict[str, dict[str, Any]] = {}
        for kw in keywords:
            if kw in df.columns:
                values = df[kw].tolist()
                comparison[kw] = {
                    "latest_value": int(values[-1]) if values else None,
                    "max_value": int(max(values)) if values else 0,
                    "average_value": round(sum(values) / len(values), 1)
                    if values
                    else 0,
                    "trend_direction": _calculate_trend_direction(
                        [int(v) for v in values]
                    ),
                }

        # Find the "winner" - highest average
        if comparison:
            winner = max(
                comparison.keys(), key=lambda k: comparison[k]["average_value"]
            )
        else:
            winner = None

        return mcp_success(
            {
                "keywords": keywords,
                "timeframe": timeframe,
                "geo": geo or "worldwide",
                "data_points": len(df) if not df.empty else 0,
                "comparison": comparison,
                "highest_average": winner,
            }
        )

    except Exception as e:
        logger.exception("Google Trends comparison failed")
        return mcp_error(f"Google Trends comparison failed: {e}")


# --- MCP Server ---


def create_trends_server():
    """Create MCP server with Google Trends tools."""
    return create_mcp_server(
        name="trends",
        version="1.0.0",
        tools=[
            google_trends,
            google_trends_compare,
        ],
    )
