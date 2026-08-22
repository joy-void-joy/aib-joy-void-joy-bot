"""What this project publishes through its native target, and what writes it.

The builders and the selector are the library's; named here is only what is
this project's own — the settings its plugin ships beside, and the fact that
it publishes no documents or verbatim assets of its own.
"""

from pathlib import Path

from lup.devtools.harness.composition import (
    NativeTargets,
    claude_composition,
    codex_composition,
    local_profile_directory,
)
from lup.devtools.harness.drift import RepositoryWriter
from lup.devtools.harness.generate import NativeHarnessComposition, ProjectContent
from lup.runtime.profiles import ProfileDirectory
from lup.workspace.paths import project_root

from aib.devtools.harness.catalog import portable_harness
from aib.runtime import select_runtime
from aib.devtools.harness.content.docs.catalog import DOCUMENTS
from aib.devtools.harness.content.settings import project_settings


def project_content(root: Path) -> ProjectContent:
    """Everything this repository publishes beside its compiled plugin tree.

    The documents are what the always-loaded guidance points at rather than
    carries: the guidance has a hard byte budget, past which a runtime
    silently truncates it. No verbatim assets — the library's own `docs/` are
    about building on lup, and this project reads them where they are rather
    than republishing a copy that goes stale on the next release.
    """
    harness = portable_harness(root=root)
    return ProjectContent(
        harness=harness,
        documents=DOCUMENTS,
        settings=project_settings(harness.plugins[0]),
    )


def profile_directory() -> ProfileDirectory:
    """The accounts this checkout keeps, under ``.lup/profiles``.

    Per-checkout rather than the operator's personal registry, so an A/B arm
    naming a profile reaches the same account whoever runs it. Whose accounts
    they are is the selected runtime's login to say, which is what keeps a
    name registered here resolving to a home the session it opens can use.
    """
    return local_profile_directory(project_root(), select_runtime().login)


def claude_target(root: Path) -> NativeHarnessComposition:
    """This project's content, compiled through the Claude adapter.

    No installer guidance is passed: that argument is a template's offer of
    its own guidance to a downstream, and this project is nobody's starting
    point.
    """
    return claude_composition(root, project_content(root))


def codex_target(root: Path) -> NativeHarnessComposition:
    """This project's content, compiled through the Codex adapter.

    The same declarations the Claude tree compiles from. It has to be
    generated rather than assumed: Codex refuses a session-level tool
    allowlist and session hooks, and governs through the policy dispatcher
    its harness tree installs — so this tree is the only place a Codex
    session meets the permission policy this project declares.
    """
    return codex_composition(root, project_content(root))


TARGETS = NativeTargets(builders={"claude": claude_target, "codex": codex_target})
"""Every native runtime this project generates a tree for, by CLI selector."""


REPOSITORY_WIDE: list[RepositoryWriter] = []
"""The writers declared beside the harness: none.

The rule reference and the CI workflow the library can write are both
declined: this repository's gate is its tracked `.githooks/`, and its rules
are read in the library that enforces them.

The command reference is the one repository-wide file this project does
publish, and it is wired in `devtools/main.py` rather than here — it walks the
composed CLI, which is a thing only the composition root has."""
