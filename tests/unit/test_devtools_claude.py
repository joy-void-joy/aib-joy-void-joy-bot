"""Behavior tests for the `lup-devtools claude` runner's arg forwarding.

The `claude` group routes any non-subcommand invocation through `run` so
`claude <args>` forwards straight to the `claude` CLI, while real subcommands
(`usage`) still dispatch. These stub the exec and pin which args reach the
runner versus which dispatch a subcommand.
"""

from pathlib import Path

import pytest
import typer
from typer.testing import CliRunner

import aib.devtools.claude as claude_mod
from aib.devtools.claude import Account, Registry, app, resolve_config_dir

runner = CliRunner()


@pytest.fixture
def forwarded(monkeypatch: pytest.MonkeyPatch) -> list[list[str]]:
    """Capture the `extra_args` of each `run_claude` call; stub the exec."""
    calls: list[list[str]] = []

    def fake_run_claude(
        profile: str | None,
        model: str | None,
        no_tools: bool,
        no_plugin: bool,
        with_prompt: bool,
        extra_args: list[str],
    ) -> None:
        calls.append(extra_args)

    monkeypatch.setattr(claude_mod, "run_claude", fake_run_claude)
    return calls


def test_bare_flag_forwards_to_claude(forwarded: list[list[str]]) -> None:
    result = runner.invoke(app, ["--resume"])
    assert result.exit_code == 0, result.output
    assert forwarded == [["--resume"]]


def test_subcommand_like_args_forward(forwarded: list[list[str]]) -> None:
    result = runner.invoke(app, ["mcp", "list"])
    assert result.exit_code == 0, result.output
    assert forwarded == [["mcp", "list"]]


def test_explicit_run_forwards_without_dashes(forwarded: list[list[str]]) -> None:
    result = runner.invoke(app, ["run", "--resume"])
    assert result.exit_code == 0, result.output
    assert forwarded == [["--resume"]]


def test_no_args_launches_with_defaults(forwarded: list[list[str]]) -> None:
    result = runner.invoke(app, [])
    assert result.exit_code == 0, result.output
    assert forwarded == [[]]


def test_usage_subcommand_is_not_forwarded(forwarded: list[list[str]]) -> None:
    result = runner.invoke(app, ["usage", "--help"])
    assert result.exit_code == 0, result.output
    assert forwarded == []


class TestResolveConfigDir:
    def test_default_when_no_registry(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.setattr(claude_mod, "REGISTRY_PATH", tmp_path / "profiles.json")
        assert resolve_config_dir() == claude_mod.DEFAULT_CONFIG_DIR

    def test_named_profile(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        registry_path = tmp_path / "profiles.json"
        registry = Registry(profiles={"work": Account(config_dir=str(tmp_path))})
        registry_path.write_text(registry.model_dump_json())
        monkeypatch.setattr(claude_mod, "REGISTRY_PATH", registry_path)
        assert resolve_config_dir("work") == tmp_path

    def test_active_profile_when_unnamed(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        registry_path = tmp_path / "profiles.json"
        registry = Registry(
            profiles={"work": Account(config_dir=str(tmp_path))}, active="work"
        )
        registry_path.write_text(registry.model_dump_json())
        monkeypatch.setattr(claude_mod, "REGISTRY_PATH", registry_path)
        assert resolve_config_dir() == tmp_path

    def test_unknown_profile_exits(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.setattr(claude_mod, "REGISTRY_PATH", tmp_path / "profiles.json")
        with pytest.raises(typer.Exit):
            resolve_config_dir("nope")
