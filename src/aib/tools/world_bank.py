"""World Bank economic data tools.

Provides access to World Bank indicators via the wbgapi library.
No API key required. Covers international economic data that FRED
(US-focused) and yfinance (company-focused) cannot.
"""

import logging
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Input Schemas ---


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

    query: str = Field(min_length=1, description="Search term (e.g. 'GDP growth', 'inflation')")
    limit: int = Field(default=10, ge=1, le=50)


# --- Output Schemas ---


class WBObservation(TypedDict):
    year: int
    value: float | None


class WBIndicatorInfo(TypedDict):
    id: str
    name: str


# --- Tools ---


@tool(
    "world_bank_indicator",
    (
        "Get time series data for a World Bank indicator and country. "
        "USE THIS for international economic data that FRED doesn't cover — "
        "GDP growth, inflation, trade, population for non-US countries.\n\n"
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

    from datetime import date

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
            observations.append({
                "year": year,
                "value": row["value"],
            })

        observations.sort(key=lambda o: o["year"])

        latest_value: float | None = None
        latest_year: int | None = None
        for obs in reversed(observations):
            if obs["value"] is not None:
                latest_value = obs["value"]
                latest_year = obs["year"]
                break

        return mcp_success({
            "indicator": indicator_info,
            "country": country,
            "start_year": start_year,
            "end_year": end_year,
            "latest_value": latest_value,
            "latest_year": latest_year,
            "data_points": len(observations),
            "observations": observations,
        })

    except Exception as e:
        logger.exception("World Bank indicator fetch failed")
        return mcp_error(
            f"Failed to fetch {validated.indicator} for {validated.country}: {e}"
        )


@tool(
    "world_bank_search",
    (
        "Search World Bank indicators by keyword. USE THIS when you need "
        "international economic data but don't know the indicator code.\n\n"
        "Examples:\n"
        '  world_bank_search(query="GDP growth") → find GDP growth indicator codes\n'
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
        results: list[WBIndicatorInfo] = []
        for item in results_iter:
            results.append({
                "id": item["id"],
                "name": item["value"],
            })
            if len(results) >= validated.limit:
                break

        return mcp_success({
            "query": validated.query,
            "results": results,
            "total_found": len(results),
        })

    except Exception as e:
        logger.exception("World Bank search failed")
        return mcp_error(f"World Bank search failed: {e}")


# --- MCP Server ---

world_bank_server = create_mcp_server(
    name="world_bank",
    tools=[world_bank_indicator, world_bank_search],
)
