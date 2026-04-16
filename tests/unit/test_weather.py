"""Tests for weather forecast tool helpers."""

from datetime import date

from aib.retrodict_context import retrodict_cutoff
from aib.tools.weather import DailyForecast, summarize_forecasts


def _make_forecast(
    dt: str,
    temp_min_c: float = 0.0,
    temp_max_c: float = 10.0,
    precip_mm: float = 0.0,
) -> DailyForecast:
    return DailyForecast(
        date=dt,
        temp_min_c=temp_min_c,
        temp_max_c=temp_max_c,
        temp_min_f=round(temp_min_c * 9 / 5 + 32, 1),
        temp_max_f=round(temp_max_c * 9 / 5 + 32, 1),
        precipitation_mm=precip_mm,
    )


class TestSummarizeForecasts:
    def test_basic_summary(self) -> None:
        forecasts = [
            _make_forecast(
                "2026-03-29", temp_min_c=-2.0, temp_max_c=8.0, precip_mm=5.0
            ),
            _make_forecast(
                "2026-03-30", temp_min_c=1.0, temp_max_c=12.0, precip_mm=0.0
            ),
            _make_forecast(
                "2026-03-31", temp_min_c=3.0, temp_max_c=15.0, precip_mm=2.3
            ),
        ]
        result = summarize_forecasts("Chicago", forecasts)

        assert result["location"] == "Chicago"
        assert result["forecast_days"] == 3
        assert result["min_temp_c"] == -2.0
        assert result["max_temp_c"] == 15.0
        assert result["total_precipitation_mm"] == 7.3
        assert len(result["daily"]) == 3

    def test_single_day(self) -> None:
        forecasts = [_make_forecast("2026-04-01", temp_min_c=5.0, temp_max_c=5.0)]
        result = summarize_forecasts("Test", forecasts)

        assert result["min_temp_c"] == 5.0
        assert result["max_temp_c"] == 5.0
        assert result["forecast_days"] == 1

    def test_precipitation_rounding(self) -> None:
        forecasts = [
            _make_forecast("2026-04-01", precip_mm=0.1),
            _make_forecast("2026-04-02", precip_mm=0.2),
        ]
        result = summarize_forecasts("Test", forecasts)
        assert result["total_precipitation_mm"] == 0.3


class TestRetrodictExclusion:
    def test_retrodict_excludes_weather(self) -> None:
        """Weather tool should raise ToolError in retrodict mode."""
        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            # The MCP tool wraps the function; call the inner async function
            # via the tool's handler. We just verify the policy exclusion.
            from aib.agent.tool_policy import WEATHER_TOOLS, ToolPolicy

            policy = ToolPolicy()
            for tool in WEATHER_TOOLS:
                assert not policy.is_tool_available(tool)
        finally:
            retrodict_cutoff.reset(token)

    def test_weather_available_normally(self) -> None:
        from aib.agent.tool_policy import WEATHER_TOOLS, ToolPolicy

        policy = ToolPolicy()
        for tool in WEATHER_TOOLS:
            assert policy.is_tool_available(tool)


class TestDailyForecast:
    def test_fahrenheit_conversion(self) -> None:
        f = _make_forecast("2026-04-01", temp_min_c=0.0, temp_max_c=100.0)
        assert f["temp_min_f"] == 32.0
        assert f["temp_max_f"] == 212.0

    def test_negative_temps(self) -> None:
        f = _make_forecast("2026-04-01", temp_min_c=-40.0, temp_max_c=-40.0)
        assert f["temp_min_f"] == -40.0
        assert f["temp_max_f"] == -40.0
