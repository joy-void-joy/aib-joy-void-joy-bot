"""Root CLI app composing all sub-apps.

Two halves: what this project has of its own — forecasting analysis,
calibration, scoring, the worldview store — and what lup ships for any
project built on it. The lup half is declared by each module beside its own
Typer app, so composing it is naming the declarations rather than repeating
their names and help text here.

`resolved()` lets the second half win on a shared name, which is how this
project keeps its own `trace` and `version` (forecast traces and the release
ritual) over lup's session-trace and bare-bump versions of the same names.
"""

from pathlib import Path

import typer
from lup.devtools.dev.app import create_dev_app
from lup.devtools.harness.app import create_harness_app
from lup.devtools.py.app import SUBAPP as PY_SUBAPP
from lup.devtools.report.app import create_report_app
from lup.devtools.subapps import SubApp, compose, subapp
from lup.devtools.sync import SUBAPP as SYNC_SUBAPP

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
from aib.devtools.trace import app as trace_app
from aib.devtools.version import app as version_app
from aib.devtools.worldview import app as worldview_app

app = typer.Typer(
    help="lup-devtools: forecasting analysis and development tools",
    pretty_exceptions_show_locals=False,
    no_args_is_help=True,
)

HARNESS_APP = create_harness_app(TARGETS, REPOSITORY_WIDE, profiles=profile_directory())
"""Generate and check the native tree this project's declarations compile to.

`report` reads the same targets, so what it calls stale drift and what
`harness check` refuses are one computation rather than two that can
disagree. Every skill this project ships is declared, so every one of them
belongs to both targets and drifts or regenerates with them."""

DEV_APP = create_dev_app(
    declared=dev.declared,
    native_targets=TARGETS,
    repository_writers=REPOSITORY_WIDE,
    guidance=guidance_document(),
    relocate_roots=[Path("src"), Path("tests")],
)
dev.extend(DEV_APP)
"""The library's development tree, wired over what this project declares.

Composed rather than replaced: the workflow the commands express — a worktree,
a gate, a PR, a pass over the notes — is not this project's to hold an opinion
about, and every one it declined to compose was one it then did not have.
`extend` mounts the single moment that is this project's own."""

SUBAPPS: list[SubApp] = [
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
    subapp("version", "Agent version management", version_app),
    subapp("worldview", "Worldview store management", worldview_app),
    PY_SUBAPP,
    SYNC_SUBAPP,
    subapp("harness", "Generate and check the native harness", HARNESS_APP),
    subapp(
        "report",
        "Everything left to implement, across every surface",
        create_report_app(TARGETS, REPOSITORY_WIDE),
    ),
]

compose(app, SUBAPPS)

if __name__ == "__main__":
    app()
