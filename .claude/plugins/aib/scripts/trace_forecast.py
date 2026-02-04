#!/usr/bin/env python3
"""Trace a forecast to its log and metrics.

Links forecast ID → saved forecast → log file → tool metrics.
Useful for debugging and feedback loop analysis.
"""

import json
from pathlib import Path

import typer

app = typer.Typer(help="Trace forecast to log and metrics")

FORECASTS_PATH = Path("./notes/forecasts")
LOGS_PATH = Path("./logs")


def find_forecast(post_id: int) -> dict | None:
    """Find the latest forecast for a post ID."""
    question_dir = FORECASTS_PATH / str(post_id)
    if not question_dir.exists():
        return None

    forecast_files = sorted(question_dir.glob("*.json"))
    if not forecast_files:
        return None

    latest = forecast_files[-1]
    return json.loads(latest.read_text())


def find_log(post_id: int) -> Path | None:
    """Find the log directory for a post ID."""
    log_dir = LOGS_PATH / str(post_id)
    if log_dir.exists():
        return log_dir
    return None


@app.command("show")
def show(
    post_id: int = typer.Argument(..., help="Metaculus post ID"),
    verbose: bool = typer.Option(False, "-v", "--verbose", help="Show full metrics"),
) -> None:
    """Show forecast trace for a post ID."""
    forecast = find_forecast(post_id)
    if not forecast:
        typer.echo(f"No forecast found for post {post_id}")
        raise typer.Exit(1)

    typer.echo(f"\n=== Forecast for Post {post_id} ===")
    typer.echo(f"Question: {forecast.get('question_title', 'Unknown')}")
    typer.echo(f"Type: {forecast.get('question_type', 'Unknown')}")
    typer.echo(f"Timestamp: {forecast.get('timestamp', 'Unknown')}")

    if forecast.get("probability") is not None:
        typer.echo(f"Probability: {forecast['probability']:.1%}")
    if forecast.get("logit") is not None:
        typer.echo(f"Logit: {forecast['logit']:+.2f}")

    # Tool metrics
    typer.echo("\n--- Tool Metrics ---")
    metrics = forecast.get("tool_metrics")
    if metrics:
        typer.echo(f"Total tool calls: {metrics.get('total_tool_calls', 'N/A')}")
        typer.echo(f"Total errors: {metrics.get('total_errors', 'N/A')}")
        typer.echo(
            f"Session duration: {metrics.get('session_duration_seconds', 'N/A')}s"
        )

        if verbose and metrics.get("by_tool"):
            typer.echo("\nBy tool:")
            for tool_name, tool_metrics in metrics["by_tool"].items():
                typer.echo(
                    f"  {tool_name}: "
                    f"{tool_metrics.get('call_count', 0)} calls, "
                    f"{tool_metrics.get('error_rate', '0%')} errors, "
                    f"avg {tool_metrics.get('avg_duration_ms', 0):.1f}ms"
                )
    else:
        typer.echo("No metrics available (legacy forecast)")

    # Log path
    typer.echo("\n--- Log Files ---")
    log_path = forecast.get("log_path")
    if log_path:
        typer.echo(f"Saved log: {log_path}")
        if Path(log_path).exists():
            typer.echo(f"  Size: {Path(log_path).stat().st_size} bytes")
        else:
            typer.echo("  (file not found)")
    else:
        typer.echo("No log path saved (legacy forecast)")

    # Find logs directory
    log_dir = find_log(post_id)
    if log_dir:
        log_files = list(log_dir.glob("*.log"))
        typer.echo(f"Logs directory: {log_dir}")
        typer.echo(f"  Files: {len(log_files)}")
        for lf in sorted(log_files)[-3:]:  # Show last 3
            typer.echo(f"    - {lf.name} ({lf.stat().st_size} bytes)")


@app.command("list")
def list_forecasts(
    limit: int = typer.Option(20, "-n", "--limit", help="Number of forecasts to show"),
) -> None:
    """List recent forecasts with their metrics summary."""
    if not FORECASTS_PATH.exists():
        typer.echo("No forecasts directory found")
        raise typer.Exit(1)

    # Collect all forecasts with timestamps
    forecasts = []
    for post_dir in FORECASTS_PATH.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in post_dir.glob("*.json"):
            try:
                data = json.loads(forecast_file.read_text())
                forecasts.append(
                    {
                        "post_id": post_dir.name,
                        "timestamp": data.get("timestamp", ""),
                        "title": data.get("question_title", "Unknown")[:50],
                        "has_metrics": data.get("tool_metrics") is not None,
                        "has_log": data.get("log_path") is not None,
                        "tool_calls": (
                            data.get("tool_metrics", {}).get("total_tool_calls", 0)
                            if data.get("tool_metrics")
                            else 0
                        ),
                    }
                )
            except Exception:
                continue

    # Sort by timestamp descending
    forecasts.sort(key=lambda x: x["timestamp"], reverse=True)
    forecasts = forecasts[:limit]

    if not forecasts:
        typer.echo("No forecasts found")
        return

    typer.echo(f"\n{'Post ID':<8} {'Timestamp':<16} {'Calls':<6} {'M':<2} {'L':<2} Title")
    typer.echo("-" * 80)
    for f in forecasts:
        metrics_indicator = "✓" if f["has_metrics"] else "-"
        log_indicator = "✓" if f["has_log"] else "-"
        typer.echo(
            f"{f['post_id']:<8} {f['timestamp']:<16} {f['tool_calls']:<6} "
            f"{metrics_indicator:<2} {log_indicator:<2} {f['title']}"
        )

    typer.echo(f"\nShowing {len(forecasts)} most recent forecasts")
    typer.echo("M = has metrics, L = has log path")


@app.command("errors")
def show_errors(
    limit: int = typer.Option(10, "-n", "--limit", help="Number of forecasts to check"),
) -> None:
    """Show forecasts with tool errors."""
    if not FORECASTS_PATH.exists():
        typer.echo("No forecasts directory found")
        raise typer.Exit(1)

    errors_found = []
    for post_dir in FORECASTS_PATH.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                metrics = data.get("tool_metrics", {})
                if metrics.get("total_errors", 0) > 0:
                    errors_found.append(
                        {
                            "post_id": post_dir.name,
                            "title": data.get("question_title", "Unknown")[:40],
                            "total_errors": metrics.get("total_errors", 0),
                            "by_tool": metrics.get("by_tool", {}),
                        }
                    )
            except Exception:
                continue

    if not errors_found:
        typer.echo("No forecasts with errors found")
        return

    errors_found.sort(key=lambda x: x["total_errors"], reverse=True)
    errors_found = errors_found[:limit]

    typer.echo(f"\n{'Post':<8} {'Errors':<8} Title")
    typer.echo("-" * 60)
    for e in errors_found:
        typer.echo(f"{e['post_id']:<8} {e['total_errors']:<8} {e['title']}")

        # Show which tools had errors
        for tool_name, tool_metrics in e["by_tool"].items():
            if tool_metrics.get("error_count", 0) > 0:
                typer.echo(
                    f"  └─ {tool_name}: {tool_metrics['error_count']} errors "
                    f"({tool_metrics.get('error_rate', 'N/A')})"
                )


if __name__ == "__main__":
    app()
