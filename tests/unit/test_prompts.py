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
        # Core methodology sections
        assert "## Research Principles" in prompt
        assert "## Output Format" in prompt
        assert "Nothing Ever Happens" in prompt
        assert "Resolution Criteria" in prompt

    def test_tool_docs_included_when_provided(self) -> None:
        """Tool docs are appended to prompt when provided."""
        tool_docs = "## Available Tools\n\n- **test_tool**: A test tool"
        prompt = get_forecasting_system_prompt(tool_docs=tool_docs)
        assert "## Available Tools" in prompt
        assert "test_tool" in prompt

    def test_tool_docs_not_included_by_default(self) -> None:
        """Without tool_docs, prompt has no tool section."""
        prompt = get_forecasting_system_prompt()
        # Base prompt doesn't have tool listing (tools are dynamically generated)
        assert "## Available Tools" not in prompt
