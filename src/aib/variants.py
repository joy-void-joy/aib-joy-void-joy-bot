"""Named agent configurations for A/B comparison.

A variant is one point in the configuration space the tournament score is
sensitive to — model, reasoning effort, and the account it runs on. Variants
are registered in `notes/variants.json` so an experiment is reviewable and
repeatable rather than reconstructed from shell history.

Each variant runs as its own process. `settings.model` is a process-global
read from many modules, so two variants sharing an interpreter would fight
over it; separate processes also isolate the Docker sandbox, the retrodict
context vars, and a crash in one arm of the experiment.
"""

from pathlib import Path
from typing import Self

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from lup.workspace.paths import notes_path

from aib.config import ResearchTopology

VARIANTS_PATH = notes_path() / "variants.json"

NAME_ALLOWED = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")

EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")


class Variant(BaseModel):
    """One named agent configuration under test."""

    model_config = ConfigDict(frozen=True)

    name: str = Field(description="Label; also the trace directory suffix.")
    model: str | None = Field(
        default=None,
        description="Model alias or full ID. None inherits AIB_MODEL.",
    )
    effort: str | None = Field(
        default=None,
        description=f"Reasoning effort, one of {EFFORT_LEVELS}. None inherits the default.",
    )
    profile: str | None = Field(
        default=None,
        description="Claude account from .lup/profiles. Distinct accounts let arms run concurrently without sharing a rate limit.",
    )
    runtime: str | None = Field(
        default=None,
        description="Runtime this arm opens sessions through. None inherits the default.",
    )
    research: ResearchTopology | None = Field(
        default=None,
        description="'delegated' reaches the data tools through a research sub-agent; 'direct' mounts them on the forecaster. None inherits the default.",
    )
    note: str = Field(default="", description="Why this variant is being tested.")

    @field_validator("name")
    @classmethod
    def check_name_is_path_safe(cls, value: str) -> str:
        """The name becomes a directory suffix, so reject separators outright."""
        if not value:
            raise ValueError("variant name must not be empty")
        illegal = sorted(set(value) - NAME_ALLOWED)
        if illegal:
            raise ValueError(
                f"variant name {value!r} contains {''.join(illegal)!r}; "
                "allowed characters are letters, digits, '-', '_' and '.'"
            )
        return value

    @field_validator("effort")
    @classmethod
    def check_effort_is_known(cls, value: str | None) -> str | None:
        if value is not None and value not in EFFORT_LEVELS:
            raise ValueError(f"effort {value!r} must be one of {EFFORT_LEVELS}")
        return value

    @field_validator("runtime")
    @classmethod
    def check_runtime_is_known(cls, value: str | None) -> str | None:
        from aib.runtime import RUNTIMES

        if value is not None and value not in RUNTIMES:
            known = ", ".join(sorted(RUNTIMES))
            raise ValueError(f"runtime {value!r} must be one of {known}")
        return value

    def trace_version(self, agent_version: str) -> str:
        """The trace directory this variant writes to."""
        return f"{agent_version}+{self.name}"


class VariantRegistry(BaseModel):
    """The registered experiment configurations, as stored on disk."""

    variants: list[Variant] = Field(default_factory=list)
    baseline: str | None = Field(
        default=None,
        description="Name of the arm the others are read against. None leaves the control unstated.",
    )

    def by_name(self, name: str) -> Variant:
        for variant in self.variants:
            if variant.name == name:
                return variant
        known = ", ".join(v.name for v in self.variants) or "none"
        raise KeyError(f"unknown variant {name!r} (registered: {known})")

    def baseline_variant(self) -> Variant | None:
        """The arm the others are read against, where the registry names one."""
        return None if self.baseline is None else self.by_name(self.baseline)

    @model_validator(mode="after")
    def check_baseline_is_registered(self) -> Self:
        """A control naming no arm reads as a comparison that cannot be made."""
        if self.baseline is None:
            return self
        if self.baseline not in {v.name for v in self.variants}:
            known = ", ".join(v.name for v in self.variants) or "none"
            raise ValueError(
                f"baseline {self.baseline!r} is not registered (registered: {known})"
            )
        return self


def load_registry(path: Path = VARIANTS_PATH) -> VariantRegistry:
    """Read the variant registry; a missing file reads as empty."""
    if not path.exists():
        return VariantRegistry()
    return VariantRegistry.model_validate_json(path.read_text(encoding="utf-8"))


def select_variants(names: list[str], path: Path = VARIANTS_PATH) -> list[Variant]:
    """Resolve variant names against the registry, preserving the given order."""
    registry = load_registry(path)
    return [registry.by_name(name) for name in names]


def variant_env(variant: Variant) -> dict[str, str]:
    """Environment overrides that pin a child process to this variant."""
    env = {"AIB_TRACE_VARIANT": variant.name}
    if variant.model is not None:
        env["AIB_MODEL"] = variant.model
    if variant.effort is not None:
        env["CLAUDE_CODE_EFFORT_LEVEL"] = variant.effort
    if variant.profile is not None:
        env["AIB_PROFILE"] = variant.profile
    if variant.runtime is not None:
        env["AIB_RUNTIME"] = variant.runtime
    if variant.research is not None:
        env["AIB_RESEARCH"] = variant.research
    return env
