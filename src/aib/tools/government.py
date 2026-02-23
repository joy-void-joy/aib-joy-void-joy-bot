"""US government data tools: BLS (Bureau of Labor Statistics) and Census/ACS.

These tools fetch official government statistics for questions about
employment, inflation, demographics, and housing.
"""

import logging
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- BLS Input/Output Schemas ---

_BLS_SERIES_GUIDE = (
    "Common series IDs: "
    "LNS14000000 (U-3 unemployment rate), "
    "LNS13327709 (U-6 unemployment rate), "
    "LNS11300000 (labor force participation rate), "
    "CES0000000001 (total nonfarm payrolls), "
    "CUUR0000SA0 (CPI-U, all items, not seasonally adjusted), "
    "CUSR0000SA0 (CPI-U, all items, seasonally adjusted), "
    "WPSFD4 (PPI, finished goods), "
    "JTS000000000000000JOR (JOLTS job openings rate)."
)


class BLSSeriesInput(BaseModel):
    """Input for BLS time series data."""

    series_ids: list[str] = Field(
        min_length=1,
        max_length=25,
        description=f"BLS series IDs to fetch. {_BLS_SERIES_GUIDE}",
    )
    start_year: int | None = Field(
        default=None,
        description="Start year (YYYY). Default: 5 years ago.",
    )
    end_year: int | None = Field(
        default=None,
        description="End year (YYYY). Default: current year.",
    )


class BLSObservation(TypedDict):
    """A single BLS data point."""

    year: str
    period: str
    period_name: str
    value: str


class BLSSeriesResult(TypedDict):
    """Result for a single BLS series."""

    series_id: str
    observations: list[BLSObservation]
    latest_value: str | None
    latest_period: str | None


# --- Census Input/Output Schemas ---

_CENSUS_VARIABLES_GUIDE = (
    "Common variable codes: "
    "B01003_001E (total population), "
    "B19013_001E (median household income), "
    "B25077_001E (median home value), "
    "B01002_001E (median age), "
    "B23025_005E (unemployed population), "
    "B25064_001E (median gross rent), "
    "B15003_022E (population with bachelor's degree), "
    "B27001_001E (health insurance coverage universe)."
)


class CensusDataInput(BaseModel):
    """Input for Census/ACS data retrieval."""

    variables: list[str] = Field(
        min_length=1,
        max_length=25,
        description=f"Census variable codes to fetch. {_CENSUS_VARIABLES_GUIDE}",
    )
    geography: str = Field(
        default="state",
        description=(
            "Geography level: 'state', 'county', 'tract', 'place', "
            "'congressional_district'. Default: state."
        ),
    )
    state: str | None = Field(
        default=None,
        description=(
            "State FIPS code or two-letter abbreviation (e.g., '06' or 'CA' for California). "
            "Required for county/tract/place queries. Use '*' for all states."
        ),
    )
    county: str | None = Field(
        default=None,
        description="County FIPS code (e.g., '037' for Los Angeles County). Use '*' for all counties.",
    )
    year: int | None = Field(
        default=None,
        description="Data year (2009-2023 for ACS 5-year). Default: latest available.",
    )
    dataset: str = Field(
        default="acs5",
        description="Census dataset: 'acs5' (5-year, most detail), 'acs1' (1-year, most recent). Default: acs5.",
    )


class CensusRecord(TypedDict):
    """A single Census data record."""

    NAME: str
    state: str
    values: dict[str, str | None]


# --- BLS Tools ---


@tool(
    "bls_series",
    (
        "Get time series data from the Bureau of Labor Statistics. "
        "Returns monthly/quarterly observations for up to 25 series. "
        "Covers employment, inflation (CPI), producer prices (PPI), "
        "productivity, and wages. "
        f"{_BLS_SERIES_GUIDE} "
        "Data typically lags 1-2 months. More granular than FRED for BLS-specific data."
    ),
    BLSSeriesInput.model_json_schema(),
)
@tracked("bls_series")
async def bls_series(args: dict[str, Any]) -> dict[str, Any]:
    """Get BLS time series data."""
    try:
        validated = BLSSeriesInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    from datetime import date

    cutoff = retrodict_cutoff.get()
    reference_year = cutoff.year if cutoff else date.today().year
    start_year = validated.start_year or (reference_year - 5)
    end_year = validated.end_year or reference_year

    if cutoff and end_year > cutoff.year:
        end_year = cutoff.year

    try:
        import bls

        api_key = settings.bls_api_key
        kwargs: dict[str, Any] = {
            "startyear": start_year,
            "endyear": end_year,
        }
        if api_key:
            kwargs["key"] = api_key

        df = bls.get_series(validated.series_ids, **kwargs)

        # Client-side date filter: BLS API returns full years, so in retrodict
        # mode we must drop observations after the cutoff month.
        if cutoff is not None and df is not None and not df.empty:
            df = df[df.index <= cutoff.isoformat()]

        results: list[BLSSeriesResult] = []

        if df is not None and not df.empty:
            for series_id in validated.series_ids:
                if series_id in df.columns:
                    series_data = df[series_id].dropna()
                    observations: list[BLSObservation] = []
                    for idx, value in series_data.items():
                        observations.append(
                            {
                                "year": str(idx.year),
                                "period": f"M{idx.month:02d}",
                                "period_name": idx.strftime("%B"),
                                "value": str(value),
                            }
                        )

                    latest = observations[-1] if observations else None
                    results.append(
                        {
                            "series_id": series_id,
                            "observations": observations[-60:],
                            "latest_value": latest["value"] if latest else None,
                            "latest_period": (
                                f"{latest['year']}-{latest['period']}"
                                if latest
                                else None
                            ),
                        }
                    )
                else:
                    results.append(
                        {
                            "series_id": series_id,
                            "observations": [],
                            "latest_value": None,
                            "latest_period": None,
                        }
                    )
        else:
            for series_id in validated.series_ids:
                results.append(
                    {
                        "series_id": series_id,
                        "observations": [],
                        "latest_value": None,
                        "latest_period": None,
                    }
                )

        return mcp_success(
            {
                "start_year": start_year,
                "end_year": end_year,
                "series_count": len(results),
                "series": results,
            }
        )

    except Exception as e:
        logger.exception("BLS series fetch failed")
        return mcp_error(f"BLS data fetch failed: {e}")


# --- Census Tools ---


def _resolve_state_fips(state_input: str) -> str:
    """Resolve a state abbreviation or FIPS code to a FIPS code."""
    if state_input == "*":
        return "*"

    if len(state_input) == 2 and state_input.isalpha():
        import us as us_module

        state_obj = us_module.states.lookup(state_input)
        if state_obj and state_obj.fips:
            return state_obj.fips
        return state_input

    return state_input


@tool(
    "census_data",
    (
        "Get Census Bureau / American Community Survey (ACS) data. "
        "Returns demographic, economic, and housing data at various geographic levels. "
        f"{_CENSUS_VARIABLES_GUIDE} "
        "Geographic levels: state, county, tract, place, congressional_district. "
        "ACS 5-year estimates (2009-2023) have the most geographic detail. "
        "ACS 1-year estimates are more recent but limited to areas with 65k+ population."
    ),
    CensusDataInput.model_json_schema(),
)
@tracked("census_data")
async def census_data(args: dict[str, Any]) -> dict[str, Any]:
    """Get Census/ACS data."""
    try:
        validated = CensusDataInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    api_key = settings.census_api_key
    if not api_key:
        return mcp_error(
            "Census API key not configured. "
            "Set CENSUS_API_KEY (free at https://api.census.gov/data/key_signup.html)."
        )

    cutoff = retrodict_cutoff.get()
    year = validated.year
    if cutoff:
        cap = cutoff.year
        if year is None or year > cap:
            year = cap

    try:
        from census import Census

        c = Census(api_key, year=year) if year else Census(api_key)

        dataset = getattr(c, validated.dataset, None)
        if dataset is None:
            return mcp_error(
                f"Unknown dataset '{validated.dataset}'. Use 'acs5' or 'acs1'."
            )

        fields = ("NAME", *validated.variables)

        state_fips = _resolve_state_fips(validated.state) if validated.state else None

        if validated.geography == "state":
            target = state_fips or "*"
            data = dataset.state(fields, target)

        elif validated.geography == "county":
            if not state_fips:
                return mcp_error("State is required for county-level queries.")
            county = validated.county or "*"
            data = dataset.state_county(fields, state_fips, county)

        elif validated.geography == "tract":
            if not state_fips or not validated.county:
                return mcp_error(
                    "State and county are required for tract-level queries."
                )
            data = dataset.state_county_tract(fields, state_fips, validated.county, "*")

        elif validated.geography == "place":
            if not state_fips:
                return mcp_error("State is required for place-level queries.")
            data = dataset.state_place(fields, state_fips, "*")

        elif validated.geography == "congressional_district":
            if not state_fips:
                return mcp_error(
                    "State is required for congressional district queries."
                )
            data = dataset.state_congressional_district(fields, state_fips, "*")

        else:
            return mcp_error(
                f"Unknown geography '{validated.geography}'. "
                "Use: state, county, tract, place, congressional_district."
            )

        records: list[CensusRecord] = []
        for row in data[:100]:
            records.append(
                {
                    "NAME": row.get("NAME", ""),
                    "state": row.get("state", ""),
                    "values": {var: row.get(var) for var in validated.variables},
                }
            )

        return mcp_success(
            {
                "dataset": validated.dataset,
                "year": year or "latest",
                "geography": validated.geography,
                "variables": validated.variables,
                "record_count": len(records),
                "records": records,
            }
        )

    except Exception as e:
        logger.exception("Census data fetch failed")
        return mcp_error(f"Census data fetch failed: {e}")


# --- MCP Server ---


def create_government_server():
    """Create MCP server with US government data tools (BLS + Census)."""
    tools = [bls_series]

    if settings.census_api_key:
        tools.append(census_data)
    else:
        logger.info("Census tools disabled: CENSUS_API_KEY not configured")

    return create_mcp_server(
        name="government",
        version="1.0.0",
        tools=tools,
    )
