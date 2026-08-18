"""Profile resolution against the accounts this checkout keeps.

Selection order is explicit name, then the directory's active profile, then
whatever configuration home the environment already selected. Each test points
the module at a temp directory, so the developer's real `.lup/profiles` is
never read and never written.

The origin is the same one `lup-devtools harness profile` curates. That is what
these tests are really pinning: a name that command registers has to be a name
`--profile` resolves, because a second registry for one of them to be missing
from is exactly how a forecast ends up on an account nobody selected.
"""

from pathlib import Path

import pytest
from lup.adapters.claude.login import CLAUDE_CONFIG_DIR
from lup.devtools.harness.composition import local_profile_directory

import aib.profiles as profiles
from aib.runtime import select_runtime
from aib.profiles import (
    UnknownProfileError,
    active_profile,
    known_profiles,
    profile_env,
    resolve_config_dir,
)


@pytest.fixture
def checkout(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    """Point the module at an empty temp checkout and return its root."""
    monkeypatch.setattr(
        profiles,
        "PROFILES",
        local_profile_directory(tmp_path, select_runtime().login),
    )
    return tmp_path


def add(name: str) -> Path:
    """Register a profile the way the command tree does, and return its home."""
    return profiles.PROFILES.add(name).config_dir


def test_a_checkout_keeping_no_accounts_resolves_nothing(checkout: Path) -> None:
    """None means inherit: pinning a default here would override the session."""
    assert resolve_config_dir() is None
    assert profile_env() == {}
    assert known_profiles() == []
    assert active_profile() is None


def test_a_named_profile_resolves_to_its_own_home(checkout: Path) -> None:
    home = add("work")

    assert resolve_config_dir("work") == home
    assert home.is_relative_to(checkout)


def test_the_first_profile_added_answers_for_an_unnamed_caller(checkout: Path) -> None:
    home = add("work")

    assert active_profile() == "work"
    assert resolve_config_dir() == home


def test_an_explicit_name_beats_the_active_one(checkout: Path) -> None:
    add("work")
    other = add("alt")

    assert active_profile() == "work"
    assert resolve_config_dir("alt") == other


def test_selecting_a_profile_moves_what_an_unnamed_caller_gets(checkout: Path) -> None:
    add("work")
    other = add("alt")

    profiles.PROFILES.use("alt")

    assert active_profile() == "alt"
    assert resolve_config_dir() == other


def test_an_unknown_name_raises_rather_than_falling_back(checkout: Path) -> None:
    """Falling back would run the forecast on an account nobody asked for."""
    add("work")

    with pytest.raises(UnknownProfileError):
        resolve_config_dir("nope")


def test_the_unknown_message_carries_the_roster_that_would_answer(
    checkout: Path,
) -> None:
    add("work")
    add("alt")

    with pytest.raises(UnknownProfileError) as raised:
        resolve_config_dir("nope")

    message = str(raised.value)
    assert "nope" in message
    assert "work" in message
    assert "alt" in message


def test_profile_env_points_a_session_at_the_selected_home(checkout: Path) -> None:
    home = add("work")

    assert profile_env("work") == {CLAUDE_CONFIG_DIR: str(home)}


def test_known_profiles_lists_every_account_the_checkout_keeps(checkout: Path) -> None:
    add("work")
    add("alt")

    assert known_profiles() == ["alt", "work"]


def test_the_directory_is_the_one_the_command_tree_curates(checkout: Path) -> None:
    """Registered through the directory, resolved through the module: one origin."""
    home = profiles.PROFILES.add("work").config_dir

    assert resolve_config_dir("work") == home
    assert "work" in known_profiles()
