"""Weather forecast tools via Open-Meteo API.

Provides medium-range (up to 16 days) weather forecasts. Uses Open-Meteo's
free API — no API key required.
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Any, TypedDict

import numpy as np
import openmeteo_requests
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.decorator import ToolError, mcp_tool

logger = logging.getLogger(__name__)


# --- Input / Output Schemas ---


class LocationInput(BaseModel):
    """A location to query."""

    latitude: float = Field(description="Latitude (-90 to 90)")
    longitude: float = Field(description="Longitude (-180 to 180)")
    name: str = Field(
        default="",
        description="Optional human-readable location name for the response.",
    )


class WeatherForecastInput(BaseModel):
    """Input for weather forecast query."""

    locations: list[LocationInput] = Field(
        min_length=1,
        max_length=20,
        description=(
            "Locations to query. For a single location, pass a one-element list. "
            "For regional scans (e.g. weather-dependent Google Trends questions), "
            "pass cities across the affected region. Max 20."
        ),
    )
    forecast_days: int = Field(
        default=16,
        ge=1,
        le=16,
        description="Number of forecast days (1-16). Default: 16.",
    )


class DailyForecast(TypedDict):
    """A single day's forecast data."""

    date: str
    temp_min_c: float
    temp_max_c: float
    temp_min_f: float
    temp_max_f: float
    precipitation_mm: float


# --- Open-Meteo API ---


async def query_open_meteo(
    latitude: float, longitude: float, forecast_days: int
) -> list[DailyForecast]:
    """Query Open-Meteo API for daily forecasts."""
    om = openmeteo_requests.AsyncClient()
    params: dict[str, Any] = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_min", "temperature_2m_max", "precipitation_sum"],
        "forecast_days": forecast_days,
        "timezone": "auto",
        "temperature_unit": "celsius",
    }

    responses = await om.weather_api(
        "https://api.open-meteo.com/v1/forecast", params=params
    )
    response = responses[0]

    daily = response.Daily()
    if daily is None:
        return []

    temp_min = daily.Variables(0)
    temp_max = daily.Variables(1)
    precip = daily.Variables(2)

    if temp_min is None or temp_max is None or precip is None:
        return []

    result: list[DailyForecast] = []
    time_range = range(daily.Time(), daily.TimeEnd(), daily.Interval())
    temp_min_values = temp_min.ValuesAsNumpy()
    temp_max_values = temp_max.ValuesAsNumpy()
    precip_values = precip.ValuesAsNumpy()

    for i, ts in enumerate(time_range):
        dt = datetime.fromtimestamp(ts, tz=timezone.utc).date()
        t_min = float(temp_min_values[i])
        t_max = float(temp_max_values[i])
        p = float(precip_values[i]) if not np.isnan(precip_values[i]) else 0.0

        result.append(
            DailyForecast(
                date=dt.isoformat(),
                temp_min_c=round(t_min, 1),
                temp_max_c=round(t_max, 1),
                temp_min_f=round(t_min * 9 / 5 + 32, 1),
                temp_max_f=round(t_max * 9 / 5 + 32, 1),
                precipitation_mm=round(p, 1),
            )
        )

    return result


def summarize_forecasts(name: str, forecasts: list[DailyForecast]) -> dict[str, Any]:
    """Build a location summary from daily forecasts."""
    return {
        "location": name,
        "forecast_days": len(forecasts),
        "daily": forecasts,
        "min_temp_c": min(f["temp_min_c"] for f in forecasts),
        "max_temp_c": max(f["temp_max_c"] for f in forecasts),
        "total_precipitation_mm": round(
            sum(f["precipitation_mm"] for f in forecasts), 1
        ),
    }


@mcp_tool(
    "weather_forecast",
    (
        "Get weather forecasts for one or more locations (up to 16 days ahead). "
        "Returns daily min/max temperatures (°C and °F) and precipitation (mm). "
        "Uses Open-Meteo API (free, no API key). "
        "Useful for weather-dependent questions — call for relevant locations "
        "to check whether extreme weather is expected in the forecast window. "
        "Pass multiple locations for regional scans (e.g. cities across a region "
        "for weather-related Google Trends questions). Max 20 locations per call."
    ),
)
async def weather_forecast(params: WeatherForecastInput) -> dict[str, Any]:
    """Get weather forecasts for one or more locations."""
    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        raise ToolError("Weather forecast not available (data source unavailable)")

    try:
        tasks = [
            query_open_meteo(loc.latitude, loc.longitude, params.forecast_days)
            for loc in params.locations
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        location_results: list[dict[str, Any]] = []
        for loc, result in zip(params.locations, results):
            if isinstance(result, BaseException):
                logger.warning("Weather query failed for %s: %s", loc.name, result)
                continue
            if not result:
                continue
            name = loc.name or f"{loc.latitude}, {loc.longitude}"
            location_results.append(summarize_forecasts(name, result))

        if not location_results:
            raise ToolError("No forecast data returned from Open-Meteo")

        if len(location_results) == 1:
            return location_results[0]

        return {
            "locations_queried": len(params.locations),
            "locations_returned": len(location_results),
            "forecast_days": params.forecast_days,
            "by_location": location_results,
        }

    except ToolError:
        raise
    except Exception as e:
        logger.exception("Weather forecast query failed")
        raise ToolError(f"Weather forecast failed: {e}") from e
