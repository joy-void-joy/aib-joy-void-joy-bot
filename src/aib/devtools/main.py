"""Root CLI app composing all sub-apps.

Two halves: what this project has of its own — forecasting analysis,
calibration, scoring, the worldview store — and what lup ships for any
project built on it. The lup half is declared by each module beside its own
Typer app, so composing it is naming the declarations rather than repeating
their names and help text here.

`resolved()` lets the second half win on a shared name, which is how this
project keeps its own `trace` — forecast traces rather than session traces —
over lup's. `version` is not among them: the release ritual it once replaced
that tree for now lives in the library, and this project mounts only the one
command that has to know where its own version used to be declared.
"""

from pathlib import Path

import typer
from lup.devtools.dev.app import create_dev_app
from lup.devtools.dev.commands import write_command_reference
from lup.devtools.roster import DevtoolsDeclarations
from lup.devtools.subapps import SubApp, compose, subapp
from lup.devtools.version import SUBAPP as LIBRARY_VERSION

from aib.devtools.agent import app as agent_app
from aib.devtools.analysis import app as analysis_app
from aib.devtools.api import app as api_app
from aib.devtools.calibration import app as calibration_app
from aib.devtools.claude import app as claude_app
import aib.devtools.dev as dev
from aib.devtools.git import app as git_app
from aib.devtools.harness.composition import (
    REPOSITORY_WIDE,
    TARGETS,
    profile_directory,
)
from aib.devtools.harness.content.guidance import document as guidance_document
from aib.devtools.health import app as health_app
from aib.devtools.migration import app as migration_app
from aib.devtools.queue import app as queue_app
from aib.devtools.resolution import app as resolution_app
from aib.devtools.scores import app as scores_app
from aib.devtools.subapps import RETIRED_SUBAPPS, agent_prompt
from aib.devtools.trace import app as trace_app
import aib.devtools.version as version
from aib.devtools.worldview import app as worldview_app

app = typer.Typer(
    help="lup-devtools: forecasting analysis and development tools",
    pretty_exceptions_show_locals=False,
    no_args_is_help=True,
)


def command_reference(root: Path | None = None, *, check: bool = False) -> Path:
    """Write or verify the reference for every command this CLI serves.

    Reads ``app`` when it runs rather than taking it as an argument: the
    declarations below are built before the sub-apps are mounted onto it, and
    a repository writer runs long after both. Wired from the composition root
    because that is the only module that has the whole CLI — a writer declared
    beside the other two would have to import this one, which nothing does.
    """
    return write_command_reference(app, root, check=check)


DECLARED = DevtoolsDeclarations(
    dev=dev.declared,
    targets=TARGETS,
    repository_writers=[*REPOSITORY_WIDE, command_reference],
    guidance=guidance_document(),
    prompt=agent_prompt,
    profiles=profile_directory(),
)
"""Everything the library's sub-apps need to know about this repository.

Each field is a fact this project already held for another reason, which is
what lets the roster itself stop being this project's to write.

One set of targets reaches both `harness` and `report` from here, so what
one calls stale drift and what the other refuses are a single computation
rather than two that can disagree.
"""

DEV_APP = create_dev_app(
    declared=DECLARED.dev,
    native_targets=DECLARED.targets,
    repository_writers=DECLARED.repository_writers,
    guidance=DECLARED.guidance,
    relocate_roots=DECLARED.relocate_roots,
)
dev.extend(DEV_APP)
version.extend(LIBRARY_VERSION.app)
"""The library's development tree, wired over what this project declares.

Composed rather than replaced: the workflow the commands express — a worktree,
a gate, a PR, a pass over the notes — is not this project's to hold an opinion
about, and every one it declined to compose was one it then did not have.
`extend` mounts the moments that are this project's own.

Built from :data:`DECLARED` field for field, which is what makes the entry
that replaces the roster's `dev` the app the roster would have built — plus
the commands mounted onto it. Restating the arguments beside the declaration
they come from is how the two drift, and it already had them stating one
thing twice."""

PROJECT_SUBAPPS: list[SubApp] = [
    subapp("agent", "Agent tool serving for Claude Code", agent_app),
    subapp("claude", "Run Claude Code for this project (+ usage)", claude_app),
    subapp("analysis", "Forecast analysis and feedback loop", analysis_app),
    subapp("calibration", "Calibration analysis and diagnostics", calibration_app),
    subapp("scores", "Unified scores table", scores_app),
    subapp("queue", "Forecasting queue and priorities", queue_app),
    subapp("resolution", "Resolution updates", resolution_app),
    subapp("trace", "Forecast tracing and log analysis", trace_app),
    subapp("api", "API inspection and debugging", api_app),
    subapp("dev", "Worktrees, branches, and pre-flight checks", DEV_APP),
    subapp("git", "Git operations for forecasts", git_app),
    subapp("health", "Service health checks", health_app),
    subapp("migration", "One-time data migrations", migration_app),
    subapp("worldview", "Worldview store management", worldview_app),
]
"""The sub-apps only this project has, because only it has their subject.

`dev` and `trace` name library sub-apps deliberately: an added entry naming a
default replaces it, which is how this project keeps forecast traces over
session traces, and the library's dev tree with its own commands mounted on.

`version` is absent because it is no longer replaced. Its one project-specific
command is mounted onto the library's tree instead, the way `dev`'s is.
"""

compose(app, RETIRED_SUBAPPS.over(DECLARED.roster(), PROJECT_SUBAPPS))

if __name__ == "__main__":
    app()
