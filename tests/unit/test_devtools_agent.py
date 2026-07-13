"""Tests for `lup-devtools agent serve-tools` tool collection and selection."""

from typer.testing import CliRunner

from aib.agent.resolver import build_research_tool_groups
from aib.devtools.agent import app

runner = CliRunner()


def test_list_prints_all_research_tools() -> None:
    result = runner.invoke(app, ["serve-tools", "--list"])
    assert result.exit_code == 0, result.output
    listed = result.output.splitlines()
    expected = [
        tool.name for group in build_research_tool_groups().values() for tool in group
    ]
    assert listed == expected
    assert "web_search" in listed


def test_list_single_group() -> None:
    result = runner.invoke(app, ["serve-tools", "--list", "--server", "trends"])
    assert result.exit_code == 0, result.output
    listed = result.output.splitlines()
    assert listed == [t.name for t in build_research_tool_groups()["trends"]]


def test_unknown_group_errors() -> None:
    result = runner.invoke(app, ["serve-tools", "--list", "--server", "nope"])
    assert result.exit_code == 1
    assert "unknown tool group" in result.output


def test_research_groups_are_session_free() -> None:
    groups = build_research_tool_groups()
    assert {"search", "financial", "government", "markets", "trends"} <= set(groups)
    assert all(group for group in groups.values())
