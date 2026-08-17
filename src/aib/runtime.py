"""Which runtime this project's agent sessions open through.

An application that names a provider in more than one place can be changed in
only one of them: the sessions it opens would come from Codex while the login
its profiles administer still belonged to Claude. A :class:`Runtime` is the
whole selection — what a session opens through, and where that runtime keeps
a login — so this module is the only place either provider is named.

The two are not interchangeable in what they will accept. Claude takes a
session-level tool allowlist and session hooks; Codex refuses both and
governs through the policy dispatcher in its `.codex/` harness tree. A caller
therefore states what it wants in the portable vocabulary of
:class:`~lup.runtime.selection.SessionRequest` and lets the selected runtime
answer, rather than building either runtime's own configuration by hand.
"""

from lup.adapters.claude.selection import CLAUDE_RUNTIME
from lup.adapters.codex.selection import CODEX_RUNTIME
from lup.runtime.selection import Runtime

from aib.config import settings

RUNTIMES: dict[str, Runtime] = {
    "claude": CLAUDE_RUNTIME,
    "codex": CODEX_RUNTIME,
}
"""Every runtime this project opens sessions through, by the name that selects it."""


class UnknownRuntimeError(ValueError):
    """A named runtime is not one this project selects."""


def select_runtime(name: str | None = None) -> Runtime:
    """Resolve the runtime a session opens through.

    Resolving a name here rather than at session start turns an unregistered
    one into an immediate error instead of a failure partway through a
    forecast.
    """
    selected = name if name is not None else settings.runtime
    runtime = RUNTIMES.get(selected)
    if runtime is None:
        known = ", ".join(sorted(RUNTIMES))
        raise UnknownRuntimeError(f"unknown runtime {selected!r} (known: {known})")
    return runtime
