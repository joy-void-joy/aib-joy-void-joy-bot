"""US government data tools: BLS (Bureau of Labor Statistics) and Census/ACS.

These tools fetch official government statistics for questions about
employment, inflation, demographics, and housing.
"""

import logging
from datetime import date
from typing import Any, TypedDict

import httpx
from pydantic import BaseModel, Field

from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.decorator import ToolError, mcp_tool
from aib.tools.retry import with_retry

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

BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

MONTH_NAMES = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


@with_retry(max_attempts=3)
async def fetch_bls_series(
    series_ids: list[str],
    start_year: int,
    end_year: int,
    api_key: str | None = None,
) -> dict[str, list[BLSObservation]]:
    """Fetch raw BLS time series data via the public API.

    Returns a dict mapping series_id to a sorted list of observations.
    Handles the BLS 20-year-per-request limit by chunking.
    """
    all_observations: dict[str, list[BLSObservation]] = {sid: [] for sid in series_ids}

    chunk_start = start_year
    while chunk_start <= end_year:
        chunk_end = min(chunk_start + 19, end_year)

        payload: dict[str, Any] = {
            "seriesid": series_ids,
            "startyear": str(chunk_start),
            "endyear": str(chunk_end),
        }
        if api_key:
            payload["registrationkey"] = api_key

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(BLS_API_URL, json=payload)
            response.raise_for_status()
            data = response.json()

        if data.get("status") != "REQUEST_SUCCEEDED":
            for msg in data.get("message", []):
                logger.warning("BLS API: %s", msg)
            raise RuntimeError(f"BLS API status: {data.get('status')}")

        for series in data.get("Results", {}).get("series", []):
            sid = series["seriesID"]
            if sid not in all_observations:
                continue
            for item in series.get("data", []):
                period = item.get("period", "")
                if period == "M13":
                    continue
                value = item.get("value", "")
                if value in ("-", ""):
                    continue
                try:
                    float(value)
                except ValueError:
                    continue
                year = item.get("year", "")
                month_num = int(period[1:]) if period.startswith("M") else 0
                all_observations[sid].append(
                    BLSObservation(
                        year=year,
                        period=period,
                        period_name=(
                            MONTH_NAMES[month_num]
                            if 1 <= month_num <= 12
                            else item.get("periodName", period)
                        ),
                        value=value,
                    )
                )

        chunk_start = chunk_end + 1

    for sid in all_observations:
        all_observations[sid].sort(key=lambda o: (o["year"], o["period"]))

    return all_observations


@mcp_tool(
    "bls_series",
    (
        "Get time series data from the Bureau of Labor Statistics. "
        "Returns monthly/quarterly observations for up to 25 series. "
        "Covers employment, inflation (CPI), producer prices (PPI), "
        "productivity, and wages. "
        f"{_BLS_SERIES_GUIDE} "
        "Data typically lags 1-2 months. More granular than FRED for BLS-specific data."
    ),
)
async def bls_series(params: BLSSeriesInput) -> dict[str, Any]:
    """Get BLS time series data."""
    cutoff = retrodict_cutoff.get()
    reference_year = cutoff.year if cutoff else date.today().year
    start_year = params.start_year or (reference_year - 5)
    end_year = params.end_year or reference_year

    if cutoff and end_year > cutoff.year:
        end_year = cutoff.year

    all_obs = await fetch_bls_series(
        params.series_ids,
        start_year,
        end_year,
        settings.bls_api_key,
    )

    results: list[BLSSeriesResult] = []
    for series_id in params.series_ids:
        observations = all_obs.get(series_id, [])

        if cutoff is not None:
            cutoff_period = f"M{cutoff.month:02d}"
            cutoff_year = str(cutoff.year)
            observations = [
                o
                for o in observations
                if (o["year"], o["period"]) <= (cutoff_year, cutoff_period)
            ]

        observations = observations[-60:]
        latest = observations[-1] if observations else None
        results.append(
            BLSSeriesResult(
                series_id=series_id,
                observations=observations,
                latest_value=latest["value"] if latest else None,
                latest_period=(
                    f"{latest['year']}-{latest['period']}" if latest else None
                ),
            )
        )

    return {
        "start_year": start_year,
        "end_year": end_year,
        "series_count": len(results),
        "series": results,
    }


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


@mcp_tool(
    "census_data",
    (
        "Get Census Bureau / American Community Survey (ACS) data. "
        "Returns demographic, economic, and housing data at various geographic levels. "
        f"{_CENSUS_VARIABLES_GUIDE} "
        "Geographic levels: state, county, tract, place, congressional_district. "
        "ACS 5-year estimates (2009-2023) have the most geographic detail. "
        "ACS 1-year estimates are more recent but limited to areas with 65k+ population."
    ),
)
async def census_data(params: CensusDataInput) -> dict[str, Any]:
    """Get Census/ACS data."""
    api_key = settings.census_api_key
    if not api_key:
        raise ToolError(
            "Census API key not configured. "
            "Set CENSUS_API_KEY (free at https://api.census.gov/data/key_signup.html)."
        )

    cutoff = retrodict_cutoff.get()
    year = params.year
    if cutoff:
        cap = cutoff.year
        if year is None or year > cap:
            year = cap

    from census import Census

    c = Census(api_key, year=year) if year else Census(api_key)

    dataset = getattr(c, params.dataset, None)
    if dataset is None:
        raise ToolError(f"Unknown dataset '{params.dataset}'. Use 'acs5' or 'acs1'.")

    fields = ("NAME", *params.variables)

    state_fips = _resolve_state_fips(params.state) if params.state else None

    if params.geography == "state":
        target = state_fips or "*"
        data = dataset.state(fields, target)

    elif params.geography == "county":
        if not state_fips:
            raise ToolError("State is required for county-level queries.")
        county = params.county or "*"
        data = dataset.state_county(fields, state_fips, county)

    elif params.geography == "tract":
        if not state_fips or not params.county:
            raise ToolError("State and county are required for tract-level queries.")
        data = dataset.state_county_tract(fields, state_fips, params.county, "*")

    elif params.geography == "place":
        if not state_fips:
            raise ToolError("State is required for place-level queries.")
        data = dataset.state_place(fields, state_fips, "*")

    elif params.geography == "congressional_district":
        if not state_fips:
            raise ToolError("State is required for congressional district queries.")
        data = dataset.state_congressional_district(fields, state_fips, "*")

    else:
        raise ToolError(
            f"Unknown geography '{params.geography}'. "
            "Use: state, county, tract, place, congressional_district."
        )

    records: list[CensusRecord] = []
    for row in data[:100]:
        records.append(
            {
                "NAME": row.get("NAME", ""),
                "state": row.get("state", ""),
                "values": {var: row.get(var) for var in params.variables},
            }
        )

    return {
        "dataset": params.dataset,
        "year": year or "latest",
        "geography": params.geography,
        "variables": params.variables,
        "record_count": len(records),
        "records": records,
    }
