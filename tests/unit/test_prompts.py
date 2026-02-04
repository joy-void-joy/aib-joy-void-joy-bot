"""Tests for system prompt generation."""

from datetime import datetime

from aib.agent.prompts import get_forecasting_system_prompt


class TestForecastingSystemPrompt:
    """Tests for get_forecasting_system_prompt()."""

    def test_default_uses_current_date(self) -> None:
        """Without forecast_date, prompt uses today's date."""
        prompt = get_forecasting_system_prompt()
        today = datetime.now().strftime("%Y-%m-%d")
        assert f"Today's date is {today}" in prompt

    def test_forecast_date_override(self) -> None:
        """forecast_date parameter overrides the date in the prompt."""
        retrodict_date = datetime(2025, 6, 15)
        prompt = get_forecasting_system_prompt(forecast_date=retrodict_date)
        assert "Today's date is 2025-06-15" in prompt
        # Should NOT contain today's actual date
        today = datetime.now().strftime("%Y-%m-%d")
        if today != "2025-06-15":
            assert f"Today's date is {today}" not in prompt

    def test_prompt_contains_expected_sections(self) -> None:
        """Prompt includes key forecasting guidance sections."""
        prompt = get_forecasting_system_prompt()
        assert "## Tools" in prompt
        assert "## Output Format" in prompt
        assert "Nothing Ever Happens" in prompt
        assert "Resolution Criteria" in prompt
