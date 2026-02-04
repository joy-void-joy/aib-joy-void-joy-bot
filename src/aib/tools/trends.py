"""Google Trends tools for search interest data.

These tools fetch Google Trends data to provide signal for questions
about search interest, trending topics, and relative popularity.
"""

import logging
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

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
            "Time range. Options: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', "
            "'today 1-m', 'today 3-m', 'today 12-m', 'today 5-y', 'all'"
        ),
    )
    geo: str = Field(
        default="",
        description="Geographic region (ISO 3166-1 alpha-2). Empty for worldwide.",
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


# --- Output Schemas ---


class TrendDataPoint(TypedDict):
    """A single data point in the trends time series."""

    date: str
    value: int  # 0-100 relative interest


class TrendsResult(TypedDict):
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
    history: list[TrendDataPoint]


# --- Google Trends API ---


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


@tool(
    "google_trends",
    (
        "Get Google Trends interest over time for a search term. "
        "Returns relative search interest (0-100) over the specified timeframe. "
        "Useful for questions about search trends, popularity, and public interest. "
        "Timeframes: 'now 1-H', 'now 4-H', 'now 1-d', 'now 7-d', 'today 1-m', "
        "'today 3-m', 'today 12-m', 'today 5-y', 'all'. "
        "Geo: ISO country code (e.g., 'US', 'GB') or empty for worldwide."
    ),
    {"keyword": str, "timeframe": str, "geo": str},
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

    try:
        from pytrends.request import TrendReq

        # Initialize pytrends
        pytrends = TrendReq(hl="en-US", tz=360)

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
            "history": history,
        }

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
    {"keywords": list, "timeframe": str, "geo": str},
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

    try:
        from pytrends.request import TrendReq

        # Initialize pytrends
        pytrends = TrendReq(hl="en-US", tz=360)

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


@tool(
    "google_trends_related",
    (
        "Get related queries and topics for a search term from Google Trends. "
        "Returns 'top' (most searched) and 'rising' (fastest growing) related queries. "
        "Useful for understanding what people search alongside a topic."
    ),
    {"keyword": str, "timeframe": str, "geo": str},
)
@tracked("google_trends_related")
async def google_trends_related(args: dict[str, Any]) -> dict[str, Any]:
    """Get related queries for a keyword from Google Trends."""
    try:
        validated = TrendsQueryInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    keyword = validated.keyword
    timeframe = validated.timeframe
    geo = validated.geo

    try:
        from pytrends.request import TrendReq

        # Initialize pytrends
        pytrends = TrendReq(hl="en-US", tz=360)

        # Build payload
        pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)

        # Get related queries
        related = pytrends.related_queries()

        if not related or keyword not in related:
            return mcp_success(
                {
                    "keyword": keyword,
                    "timeframe": timeframe,
                    "geo": geo or "worldwide",
                    "top_queries": [],
                    "rising_queries": [],
                }
            )

        kw_data = related[keyword]

        # Parse top queries
        top_queries: list[dict[str, Any]] = []
        if kw_data.get("top") is not None and not kw_data["top"].empty:
            top_df = kw_data["top"].head(10)
            top_queries = [
                {"query": row["query"], "value": int(row["value"])}
                for _, row in top_df.iterrows()
            ]

        # Parse rising queries
        rising_queries: list[dict[str, Any]] = []
        if kw_data.get("rising") is not None and not kw_data["rising"].empty:
            rising_df = kw_data["rising"].head(10)
            rising_queries = [
                {"query": row["query"], "value": str(row["value"])}  # Can be "Breakout"
                for _, row in rising_df.iterrows()
            ]

        return mcp_success(
            {
                "keyword": keyword,
                "timeframe": timeframe,
                "geo": geo or "worldwide",
                "top_queries": top_queries,
                "rising_queries": rising_queries,
            }
        )

    except Exception as e:
        logger.exception("Google Trends related queries failed")
        return mcp_error(f"Google Trends related queries failed for '{keyword}': {e}")


# --- MCP Server ---

trends_server = create_mcp_server(
    name="trends",
    version="1.0.0",
    tools=[
        google_trends,
        google_trends_compare,
        google_trends_related,
    ],
)
