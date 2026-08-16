"""Profile resolution against lup's machine-wide account registry.

Selection order is explicit name, then the registry's active profile, then
`~/.claude`. Each test points the store at a temp registry so the developer's
real `~/.lup/profiles.json` is never read.
"""

from pathlib import Path

import pytest
from lup.adapters.claude.profile_store import Account, AccountFile, Registry

import aib.profiles as profiles
from aib.profiles import (
    CLAUDE_CONFIG_DIR,
    UnknownProfileError,
    active_profile,
    known_profiles,
    profile_env,
    resolve_config_dir,
)


@pytest.fixture
def registry_path(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    """Point the module store at an empty temp registry and return its path."""
    path = tmp_path / "profiles.json"
    monkeypatch.setattr(profiles, "STORE", AccountFile(registry_path=path))
    return path


def write_registry(path: Path, registry: Registry) -> None:
    path.write_text(registry.model_dump_json())


def test_default_when_no_registry(registry_path: Path) -> None:
    assert resolve_config_dir() == Path.home() / ".claude"


def test_named_profile(registry_path: Path, tmp_path: Path) -> None:
    write_registry(
        registry_path,
        Registry(profiles={"work": Account(config_dir=str(tmp_path))}),
    )
    assert resolve_config_dir("work") == tmp_path


def test_active_profile_when_unnamed(registry_path: Path, tmp_path: Path) -> None:
    write_registry(
        registry_path,
        Registry(profiles={"work": Account(config_dir=str(tmp_path))}, active="work"),
    )
    assert resolve_config_dir() == tmp_path


def test_explicit_name_beats_active(registry_path: Path, tmp_path: Path) -> None:
    other = tmp_path / "other"
    write_registry(
        registry_path,
        Registry(
            profiles={
                "work": Account(config_dir=str(tmp_path)),
                "personal": Account(config_dir=str(other)),
            },
            active="work",
        ),
    )
    assert resolve_config_dir("personal") == other


def test_unknown_profile_raises(registry_path: Path) -> None:
    with pytest.raises(UnknownProfileError):
        resolve_config_dir("nope")


def test_unknown_profile_message_lists_known(
    registry_path: Path, tmp_path: Path
) -> None:
    write_registry(
        registry_path,
        Registry(profiles={"work": Account(config_dir=str(tmp_path))}),
    )
    with pytest.raises(UnknownProfileError, match="known: work"):
        resolve_config_dir("nope")


def test_profile_env_points_at_the_config_home(
    registry_path: Path, tmp_path: Path
) -> None:
    write_registry(
        registry_path,
        Registry(profiles={"work": Account(config_dir=str(tmp_path))}),
    )
    assert profile_env("work") == {CLAUDE_CONFIG_DIR: str(tmp_path)}


def test_known_profiles_are_sorted(registry_path: Path, tmp_path: Path) -> None:
    write_registry(
        registry_path,
        Registry(
            profiles={
                "work": Account(config_dir=str(tmp_path)),
                "alt": Account(config_dir=str(tmp_path)),
            }
        ),
    )
    assert known_profiles() == ["alt", "work"]


def test_active_profile_reads_the_registry(registry_path: Path, tmp_path: Path) -> None:
    write_registry(
        registry_path,
        Registry(profiles={"work": Account(config_dir=str(tmp_path))}, active="work"),
    )
    assert active_profile() == "work"
