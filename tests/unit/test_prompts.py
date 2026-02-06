"""Tests for system prompt generation."""

from datetime import datetime

from aib.agent.prompts import get_forecasting_system_prompt


class TestForecastingSystemPrompt:
    """Tests for get_forecasting_system_prompt()."""

    def test_no_date_in_prompt(self) -> None:
        """Prompt does not inject a date (model knows it from system context)."""
        prompt = get_forecasting_system_prompt()
        assert "Today's date is" not in prompt

    def test_forecast_date_accepted_but_unused(self) -> None:
        """forecast_date parameter is accepted for caller compatibility."""
        retrodict_date = datetime(2025, 6, 15)
        prompt = get_forecasting_system_prompt(forecast_date=retrodict_date)
        assert "Today's date is" not in prompt

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
