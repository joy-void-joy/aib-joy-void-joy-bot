"""Variant registry, trace keying, and the env a variant hands its child process."""

from pathlib import Path

import pytest

from aib.variants import (
    EFFORT_LEVELS,
    VARIANTS_PATH,
    Variant,
    VariantRegistry,
    load_registry,
    select_variants,
    variant_env,
)


def write_registry(path: Path, registry: VariantRegistry) -> Path:
    path.write_text(registry.model_dump_json(), encoding="utf-8")
    return path


class TestVariantValidation:
    def test_name_may_not_contain_a_path_separator(self) -> None:
        """The name becomes a directory suffix, so a separator would escape the trace tree."""
        with pytest.raises(ValueError, match="contains"):
            Variant(name="a/b")

    def test_name_may_not_be_empty(self) -> None:
        with pytest.raises(ValueError, match="must not be empty"):
            Variant(name="")

    def test_name_allows_dotted_versions(self) -> None:
        assert Variant(name="5.6-sol_x").name == "5.6-sol_x"

    def test_unknown_effort_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="must be one of"):
            Variant(name="v", effort="xmax")

    @pytest.mark.parametrize("effort", EFFORT_LEVELS)
    def test_known_efforts_are_accepted(self, effort: str) -> None:
        assert Variant(name="v", effort=effort).effort == effort


class TestTraceKeying:
    def test_variant_gets_its_own_version_directory(self) -> None:
        assert Variant(name="sonnet-max").trace_version("6.4.0") == "6.4.0+sonnet-max"

    def test_variant_directory_is_not_valid_semver(self) -> None:
        """Keeps experimental arms out of the released version's aggregates."""
        from aib.paths import parse_semver

        assert parse_semver(Variant(name="x").trace_version("6.4.0")) is None
        assert parse_semver("6.4.0") == (6, 4, 0)

    def test_baseline_version_is_untouched_without_a_variant(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from lup.workspace.paths import agent_version

        from aib.config import settings
        from aib.paths import trace_version

        monkeypatch.setattr(settings, "trace_variant", None)
        assert trace_version() == agent_version()

    def test_variant_shifts_the_write_directory(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from lup.workspace.paths import agent_version

        from aib.config import settings
        from aib.paths import forecasts_dir, sessions_dir

        monkeypatch.setattr(settings, "trace_variant", "arm")
        assert forecasts_dir().parent.name == f"{agent_version()}+arm"
        assert sessions_dir().parent.name == f"{agent_version()}+arm"

    def test_explicit_version_still_overrides(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from aib.config import settings
        from aib.paths import forecasts_dir

        monkeypatch.setattr(settings, "trace_variant", "arm")
        assert forecasts_dir("1.2.3").parent.name == "1.2.3"


class TestRegistry:
    def test_missing_file_reads_as_empty(self, tmp_path: Path) -> None:
        assert load_registry(tmp_path / "absent.json").variants == []

    def test_select_preserves_the_requested_order(self, tmp_path: Path) -> None:
        path = write_registry(
            tmp_path / "variants.json",
            VariantRegistry(variants=[Variant(name="a"), Variant(name="b")]),
        )
        assert [v.name for v in select_variants(["b", "a"], path)] == ["b", "a"]

    def test_unknown_variant_lists_the_registered_ones(self, tmp_path: Path) -> None:
        path = write_registry(
            tmp_path / "variants.json",
            VariantRegistry(variants=[Variant(name="baseline")]),
        )
        with pytest.raises(KeyError, match="registered: baseline"):
            select_variants(["nope"], path)


class TestVariantEnv:
    def test_bare_variant_only_sets_the_trace_label(self) -> None:
        assert variant_env(Variant(name="baseline")) == {
            "AIB_TRACE_VARIANT": "baseline"
        }

    def test_overrides_map_to_the_settings_env_names(self) -> None:
        env = variant_env(
            Variant(name="v", model="sonnet", effort="max", profile="alt")
        )
        assert env == {
            "AIB_TRACE_VARIANT": "v",
            "AIB_MODEL": "sonnet",
            "CLAUDE_CODE_EFFORT_LEVEL": "max",
            "AIB_PROFILE": "alt",
        }

    def test_a_topology_reaches_the_child_that_reads_it(self) -> None:
        """The arm runs in its own process, so the choice travels as env."""
        assert variant_env(Variant(name="v", research="direct"))["AIB_RESEARCH"] == (
            "direct"
        )

    def test_an_unstated_topology_leaves_the_child_on_the_default(self) -> None:
        """An arm saying nothing about research must not pin it either way."""
        assert "AIB_RESEARCH" not in variant_env(Variant(name="v", model="sonnet"))

    def test_the_name_the_arm_exports_is_the_one_settings_reads(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """The two halves of the chain agree, which nothing else checks.

        A variant hands its child an environment and the child builds its own
        `Settings`; between them the name is written twice, in two files. A
        mismatch would not fail — the child would read the default and run the
        shipped topology under the experiment's label, which is the arm
        quietly measuring its own control.
        """
        from aib.agent.tool_policy import ToolPolicy
        from aib.config import Settings

        exported = variant_env(Variant(name="v", research="direct"))
        for name, value in exported.items():
            monkeypatch.setenv(name, value)

        settings = Settings(metaculus_token="unused-here")

        assert settings.research == "direct"
        assert ToolPolicy.from_settings(settings).research == "direct"


class TestRegisteredVariants:
    """The arms this repository actually has registered.

    Which arms exist is pinned in `test_runtime_selection.py`; what is asked
    here is whether the topology arm is shaped to measure anything.
    """

    def test_the_topology_arm_differs_from_baseline_in_one_field(self) -> None:
        """An arm differing in two things measures neither of them."""
        registry = load_registry(VARIANTS_PATH)
        baseline = registry.by_name("baseline")
        arm = registry.by_name("direct-research")

        assert arm.research == "direct"
        assert baseline.research is None
        assert (arm.model, arm.effort, arm.profile, arm.runtime) == (
            baseline.model,
            baseline.effort,
            baseline.profile,
            baseline.runtime,
        )
