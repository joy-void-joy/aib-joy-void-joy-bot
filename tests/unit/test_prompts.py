"""Tests for system prompt generation."""

from aib.agent.prompts import get_forecasting_system_prompt


class TestForecastingSystemPrompt:
    """Tests for get_forecasting_system_prompt()."""

    def test_prompt_contains_expected_sections(self) -> None:
        """Prompt includes key forecasting guidance sections."""
        prompt = get_forecasting_system_prompt()
        assert "## Core Principles" in prompt
        assert "## Output Format" in prompt
        assert "## STEP 4: Calibration" in prompt
        assert "## Meta-Predictions" in prompt

    def test_prompt_does_not_contain_date(self) -> None:
        """Prompt should not mention today's date (avoids agent self-restricting)."""
        prompt = get_forecasting_system_prompt()
        assert "Today's date" not in prompt

    def test_tool_docs_included_when_provided(self) -> None:
        """Tool docs are appended to prompt when provided."""
        tool_docs = "## Available Tools\n\n- **test_tool**: A test tool"
        prompt = get_forecasting_system_prompt(tool_docs=tool_docs)
        assert "## Available Tools" in prompt
        assert "test_tool" in prompt

    def test_tool_docs_not_included_by_default(self) -> None:
        """Without tool_docs, prompt has no tool section."""
        prompt = get_forecasting_system_prompt()
        assert "## Available Tools" not in prompt

    def test_subagents_rendered_from_descriptions(self) -> None:
        """Subagent descriptions come from the descriptions dict."""
        agents = {
            "test_agent": "A test agent for testing",
        }
        prompt = get_forecasting_system_prompt(subagents=agents)
        assert "**test_agent**" in prompt
        assert "A test agent for testing" in prompt

    def test_no_subagents_shows_placeholder(self) -> None:
        """Without subagents, prompt shows a placeholder."""
        prompt = get_forecasting_system_prompt()
        assert "No subagents configured" in prompt
