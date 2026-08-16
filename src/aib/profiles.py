"""Named Claude account selection, backed by lup's profile registry.

The registry lives at `~/.lup/profiles.json` — machine-wide and shared with
other lup projects, because Claude accounts are reused across projects. A
profile names a Claude configuration home; pointing a session at one selects
the account, its subscription, and its rate limits.

Selection order is explicit name, then the registry's active profile, then
`~/.claude`.
"""

from pathlib import Path

from lup.adapters.claude.login import CLAUDE_CONFIG_DIR
from lup.adapters.claude.profile_store import AccountFile

STORE = AccountFile()


class UnknownProfileError(Exception):
    """A named profile is absent from the registry."""


def resolve_config_dir(name: str | None = None) -> Path:
    """Resolve a Claude config home for a profile name."""
    try:
        return STORE.resolve_config_dir(name)
    except KeyError as error:
        known = ", ".join(known_profiles()) or "none"
        raise UnknownProfileError(
            f"unknown profile {name!r} in {STORE.registry_path} (known: {known})"
        ) from error


def profile_env(name: str | None = None) -> dict[str, str]:
    """Env mapping that points an Agent SDK session at the selected account."""
    return {CLAUDE_CONFIG_DIR: str(resolve_config_dir(name))}


def known_profiles() -> list[str]:
    """Profile names registered on this machine."""
    return sorted(STORE.load_registry().profiles)


def active_profile() -> str | None:
    """The profile marked active in the registry, if any."""
    return STORE.load_registry().active
