"""Named account selection, over the accounts this checkout keeps.

Whose accounts they are is the selected runtime's login to say: it names the
subdirectory each takes inside a profile and the variable that points a CLI
at one, so a checkout running either runtime keeps both under one name.

The accounts live under `.lup/profiles` in the checkout rather than in the
operator's home, so an A/B arm naming a profile reaches the same account
whoever runs it. `lup-devtools harness profile` curates this same directory,
which is the point: a name that command registers is a name `--profile` can
select, and there is no second registry for one of them to be missing from.

Selection order is explicit name, then the directory's active profile, then
whatever configuration home the environment already selected. A checkout that
keeps no accounts resolves nothing and leaves that inherited home alone.
"""

from pathlib import Path

from lup.devtools.harness.composition import local_profile_directory
from lup.runtime.profiles import ProfileDirectory, UnknownProfile
from lup.workspace.paths import project_root

from aib.runtime import select_runtime

PROFILES: ProfileDirectory = local_profile_directory(
    project_root(), select_runtime().login
)
"""The accounts this checkout keeps, as the one directory every caller reads."""

UnknownProfileError = UnknownProfile
"""A name no profile answers to, under the name this project already catches."""


def resolve_config_dir(name: str | None = None) -> Path | None:
    """The configuration home a name selects, or None to inherit one."""
    return PROFILES.launch_home(name)


def profile_env(name: str | None = None) -> dict[str, str]:
    """Env mapping that points an Agent SDK session at the selected account.

    Empty when nothing is selected, so a session inherits the home its
    environment already names rather than being pinned to a default one.
    """
    home = resolve_config_dir(name)
    return {} if home is None else dict(select_runtime().login.environment(home))


def known_profiles() -> list[str]:
    """Profile names this checkout keeps, in the directory's display order."""
    return [profile.name for profile in PROFILES.entries()]


def active_profile() -> str | None:
    """The profile answering for a caller naming none, if there is one."""
    selected = PROFILES.active()
    return None if selected is None else selected.name
