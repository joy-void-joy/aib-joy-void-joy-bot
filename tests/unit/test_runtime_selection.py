"""Tests for which runtime this project's sessions open through."""

import pytest
from pydantic import ValidationError

from aib.runtime import RUNTIMES, UnknownRuntimeError, select_runtime
from aib.variants import Variant, load_registry, variant_env


class TestRuntimeRegistry:
    def test_both_providers_are_selectable(self) -> None:
        assert sorted(RUNTIMES) == ["claude", "codex"]

    def test_each_runtime_carries_a_login_and_an_opener(self) -> None:
        """A Runtime is the whole selection, not just a session opener."""
        for runtime in RUNTIMES.values():
            assert runtime.login is not None
            assert callable(runtime.open)


class TestSelectRuntime:
    def test_a_named_runtime_wins(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("aib.runtime.settings.runtime", "claude")
        assert select_runtime("codex") is RUNTIMES["codex"]

    def test_the_setting_answers_when_nothing_is_named(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr("aib.runtime.settings.runtime", "codex")
        assert select_runtime() is RUNTIMES["codex"]

    def test_an_unknown_runtime_is_rejected(self) -> None:
        with pytest.raises(UnknownRuntimeError, match="gpt"):
            select_runtime("gpt")


class TestVariantRuntime:
    def test_an_arm_carries_its_runtime_into_the_child(self) -> None:
        variant = Variant(
            name="gpt-5.6-sol",
            model="openai/gpt-5.6-sol",
            runtime="codex",
        )
        assert variant_env(variant)["AIB_RUNTIME"] == "codex"

    def test_an_arm_naming_no_runtime_inherits(self) -> None:
        assert "AIB_RUNTIME" not in variant_env(Variant(name="baseline"))

    def test_an_arm_naming_an_unknown_runtime_is_rejected(self) -> None:
        with pytest.raises(ValidationError, match="claude, codex"):
            Variant(name="broken", runtime="gpt")


class TestShippedRegistry:
    """The registry this repository ships is what `forecast ab` reads."""

    def test_it_validates(self) -> None:
        """Every arm the repository means to keep is still registered.

        Stated as a subset rather than as the list. An experiment is added
        by registering an arm, and a test that fails on the addition is one
        whoever adds it edits without reading — which is how the arm that
        was silently *dropped* would go through too.
        """
        registered = {v.name for v in load_registry().variants}

        assert registered >= {"opus", "chatgpt-sol"}

    def test_the_arms_differ_in_runtime(self) -> None:
        registry = load_registry()
        runtimes = {v.name: v.runtime for v in registry.variants}

        assert runtimes["opus"] == "claude"
        assert runtimes["chatgpt-sol"] == "codex"

    def test_each_arm_traces_somewhere_of_its_own(self) -> None:
        """Two arms writing one directory would pool the comparison away."""
        registered = load_registry().variants
        traces = {v.trace_version("7.0.0") for v in registered}

        assert len(traces) == len(registered)
        assert all(trace.startswith("7.0.0+") for trace in traces)
