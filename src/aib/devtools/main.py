"""Root CLI app composing all sub-apps."""

import typer

from aib.devtools.api import app as api_app
from aib.devtools.calibration import app as calibration_app
from aib.devtools.dev import app as dev_app
from aib.devtools.feedback import app as feedback_app
from aib.devtools.git import app as git_app
from aib.devtools.health import app as health_app
from aib.devtools.metrics import app as metrics_app
from aib.devtools.queue import app as queue_app
from aib.devtools.resolution import app as resolution_app
from aib.devtools.scores import app as scores_app
from aib.devtools.trace import app as trace_app
from aib.devtools.version import app as version_app

app = typer.Typer(
    help="aib-devtools: forecasting analysis and development tools",
    pretty_exceptions_show_locals=False,
    no_args_is_help=True,
)

app.add_typer(
    calibration_app, name="calibration", help="Calibration analysis and diagnostics"
)
app.add_typer(scores_app, name="scores", help="Unified scores table")
app.add_typer(queue_app, name="queue", help="Forecasting queue and priorities")
app.add_typer(resolution_app, name="resolution", help="Resolution updates")
app.add_typer(feedback_app, name="feedback", help="Feedback collection")
app.add_typer(trace_app, name="trace", help="Forecast tracing and log analysis")
app.add_typer(metrics_app, name="metrics", help="Aggregate metrics")
app.add_typer(api_app, name="api", help="API inspection and debugging")
app.add_typer(dev_app, name="dev", help="Development tools")
app.add_typer(git_app, name="git", help="Git operations for forecasts")
app.add_typer(health_app, name="health", help="Service health checks")
app.add_typer(version_app, name="version", help="Agent version management")

if __name__ == "__main__":
    app()
