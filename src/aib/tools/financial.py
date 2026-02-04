"""Financial data tools for economic indicators and time series.

These tools provide direct API access to financial data sources,
avoiding the need for web scraping which often fails on JS-heavy sites.
"""

import logging
from datetime import datetime, timedelta
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.config import settings
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.validation import validate_input

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


# --- FRED API Tools ---


@tool(
    "fred_series",
    (
        "Get historical data for a FRED (Federal Reserve Economic Data) series. "
        "Common series: DGS10 (10-year Treasury), DGS3MO (3-month Treasury), "
        "FEDFUNDS (Fed Funds Rate), UNRATE (Unemployment), CPIAUCSL (CPI). "
        "Returns recent observations and series metadata."
    ),
    {"series_id": str, "observation_start": str, "observation_end": str},
)
@tracked("fred_series")
async def fred_series(args: dict[str, Any]) -> dict[str, Any]:
    """Get FRED series data."""
    validated = validate_input(FredSeriesInput, args)
    if isinstance(validated, dict):
        return validated

    api_key = settings.fred_api_key
    if not api_key:
        return mcp_error(
            "FRED_API_KEY not configured. Get a free key at https://fred.stlouisfed.org/docs/api/api_key.html"
        )

    series_id = validated.series_id.upper()

    # Default to last 30 days
    end_date = validated.observation_end or datetime.now().strftime("%Y-%m-%d")
    start_date = validated.observation_start or (
        datetime.now() - timedelta(days=30)
    ).strftime("%Y-%m-%d")

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
            obs_list.append({
                "date": str(date)[:10],
                "value": float(value) if not (value != value) else None,  # Handle NaN
            })

        # Get latest non-null value
        latest_value = None
        latest_date = None
        for obs in reversed(obs_list):
            if obs["value"] is not None:
                latest_value = obs["value"]
                latest_date = obs["date"]
                break

        series_info: FredSeriesInfo = {
            "id": series_id,
            "title": str(info.get("title", series_id)),
            "frequency": str(info.get("frequency", "Unknown")),
            "units": str(info.get("units", "Unknown")),
            "seasonal_adjustment": str(info.get("seasonal_adjustment", "Unknown")),
            "last_updated": str(info.get("last_updated", ""))[:10],
        }

        return mcp_success({
            "series": series_info,
            "latest_value": latest_value,
            "latest_date": latest_date,
            "observation_start": start_date,
            "observation_end": end_date,
            "data_points": len(obs_list),
            "observations": obs_list[-30:],  # Limit to last 30
        })

    except Exception as e:
        logger.exception("FRED series lookup failed")
        return mcp_error(f"FRED series lookup failed for {series_id}: {e}")


@tool(
    "fred_search",
    (
        "Search for FRED series by keyword. Use to find the correct series ID "
        "for economic indicators. Returns series IDs, titles, and descriptions."
    ),
    {"query": str, "limit": int},
)
@tracked("fred_search")
async def fred_search(args: dict[str, Any]) -> dict[str, Any]:
    """Search for FRED series."""
    validated = validate_input(FredSearchInput, args)
    if isinstance(validated, dict):
        return validated

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
            return mcp_success({
                "query": validated.query,
                "results": [],
                "total_found": 0,
            })

        # Convert to list of dicts (results is a DataFrame)
        series_list = []
        for idx, row in results.head(validated.limit).iterrows():
            series_list.append({
                "id": str(idx),
                "title": str(row.get("title", "")),
                "frequency": str(row.get("frequency", "")),
                "units": str(row.get("units", "")),
                "popularity": int(row.get("popularity") or 0),
            })

        return mcp_success({
            "query": validated.query,
            "results": series_list,
            "total_found": len(results),
        })

    except Exception as e:
        logger.exception("FRED search failed")
        return mcp_error(f"FRED search failed: {e}")


# --- Common FRED Series Reference ---
# This is documentation for the agent, not code

COMMON_FRED_SERIES = """
Common FRED Series IDs:

Treasury Yields:
- DGS1MO: 1-Month Treasury
- DGS3MO: 3-Month Treasury
- DGS6MO: 6-Month Treasury
- DGS1: 1-Year Treasury
- DGS2: 2-Year Treasury
- DGS3: 3-Year Treasury
- DGS5: 5-Year Treasury
- DGS7: 7-Year Treasury
- DGS10: 10-Year Treasury
- DGS20: 20-Year Treasury
- DGS30: 30-Year Treasury

Interest Rates:
- FEDFUNDS: Federal Funds Rate
- PRIME: Bank Prime Loan Rate
- MORTGAGE30US: 30-Year Mortgage Rate

Economic Indicators:
- UNRATE: Unemployment Rate
- CPIAUCSL: Consumer Price Index
- GDP: Gross Domestic Product
- PAYEMS: Total Nonfarm Payrolls
- INDPRO: Industrial Production Index
- HOUST: Housing Starts
- RSAFS: Retail Sales

Exchange Rates:
- DEXUSEU: US/Euro Exchange Rate
- DEXJPUS: Japan/US Exchange Rate
- DTWEXBGS: Trade Weighted Dollar Index

Stock Market:
- SP500: S&P 500 Index
- NASDAQCOM: NASDAQ Composite
- DJIA: Dow Jones Industrial Average
"""


# --- MCP Server ---

# Build tool list conditionally based on available credentials.
# Tools are gated at BOTH layers:
# 1. MCP server registration (here) - so agent doesn't discover unavailable tools
# 2. allowed_tools in core.py - defense in depth
_financial_tools = []

if settings.fred_api_key:
    _financial_tools.extend([fred_series, fred_search])
else:
    logger.info("FRED tools disabled: FRED_API_KEY not configured")

financial_server = create_mcp_server(
    name="financial",
    version="1.0.0",
    tools=_financial_tools,
)
