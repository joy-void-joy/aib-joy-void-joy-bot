"""Which model a run actually opens, from wherever the name arrived.

`resolve_model` was reached from one command's `--model` option, so a name
given any other way stayed an alias and was handed to the runtime to resolve
by its own table. The two tables do not agree: `opus` here carries the 1M
context window and the runtime's does not, so an A/B arm naming `opus` ran a
shorter window than the configuration it was the control for.
"""

import pytest

from aib.config import MODEL_ALIASES, Settings, resolve_model
from aib.variants import Variant, variant_env

TOKEN = "unused-in-these-tests"


def settings_with(monkeypatch: pytest.MonkeyPatch, **environment: str) -> Settings:
    """Settings as a child process would build them, from the environment."""
    for name, value in environment.items():
        monkeypatch.setenv(name, value)
    return Settings(metaculus_token=TOKEN)


def test_an_alias_from_the_environment_is_resolved(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The path an A/B arm uses, and the one the resolution did not cover."""
    settings = settings_with(monkeypatch, AIB_MODEL="opus")

    assert settings.model == "claude-opus-5[1m]"


def test_the_arm_that_named_opus_runs_what_the_default_runs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A control arm has to be the configuration it is controlling for.

    Both halves through their real routes: the variant exports what it
    exports, and the child reads what it reads. An arm running a shorter
    context window than the default would report a difference that was
    partly the window.
    """
    exported = variant_env(Variant(name="baseline", model="opus"))
    for name, value in exported.items():
        monkeypatch.setenv(name, value)

    assert (
        Settings(metaculus_token=TOKEN).model == Settings.model_fields["model"].default
    )


@pytest.mark.parametrize("alias", sorted(MODEL_ALIASES))
def test_every_alias_resolves_wherever_it_is_named(
    alias: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The table is the answer for the environment as much as for a flag."""
    assert settings_with(monkeypatch, AIB_MODEL=alias).model == MODEL_ALIASES[alias]


def test_a_full_id_passes_through_untouched(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """An OpenRouter-style id is not an alias and must not be rewritten."""
    named = "openrouter/some-vendor/some-model-9"

    assert settings_with(monkeypatch, AIB_MODEL=named).model == named


def test_resolution_is_idempotent() -> None:
    """Settings resolve on construction and a caller may resolve again.

    `cli.py` assigns a resolved name onto an already-built Settings, which
    pydantic does not re-validate; resolving twice has to be safe rather than
    merely unlikely.
    """
    for alias, resolved in MODEL_ALIASES.items():
        assert resolve_model(resolve_model(alias)) == resolved
