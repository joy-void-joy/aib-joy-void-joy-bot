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

import typer
from lup.devtools.harness.composition import NativeTargets
from lup.devtools.py.app import SUBAPP as PY_SUBAPP
from lup.devtools.report.app import create_report_app
from lup.devtools.subapps import SubApp, compose, subapp
from lup.devtools.sync import SUBAPP as SYNC_SUBAPP

from aib.devtools.agent import app as agent_app
from aib.devtools.analysis import app as analysis_app
from aib.devtools.api import app as api_app
from aib.devtools.calibration import app as calibration_app
from aib.devtools.claude import app as claude_app
from aib.devtools.dev import app as dev_app
from aib.devtools.git import app as git_app
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

NO_GENERATED_TREES = NativeTargets(builders={})
"""This project generates no native harness tree.

Everything under `.claude/plugins/aib/` is hand-maintained, so `report` has
no targets to check for drift and no writers to run — it reports on the
surfaces that do exist here (open notes, unlanded branches, resolver state)
and finds nothing to say about generation."""

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
    subapp("dev", "Development tools", dev_app),
    subapp("git", "Git operations for forecasts", git_app),
    subapp("health", "Service health checks", health_app),
    subapp("migration", "One-time data migrations", migration_app),
    subapp("version", "Agent version management", version_app),
    subapp("worldview", "Worldview store management", worldview_app),
    PY_SUBAPP,
    SYNC_SUBAPP,
    subapp(
        "report",
        "Everything left to implement, across every surface",
        create_report_app(NO_GENERATED_TREES, []),
    ),
]

compose(app, SUBAPPS)

if __name__ == "__main__":
    app()
