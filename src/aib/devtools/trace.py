"""Trace forecasts to logs and metrics.

Combines forecast tracing (linking forecast → log → metrics)
and log filtering (extracting agent reasoning from noisy logs).
"""

import json
import re
from pathlib import Path

import typer

from aib.paths import RUNTIME_LOGS_PATH, find_latest_forecast_file, iter_forecast_dirs

app = typer.Typer(no_args_is_help=True)


# ---------------------------------------------------------------------------
# Forecast tracing
# ---------------------------------------------------------------------------


def find_forecast(post_id: int) -> dict | None:
    """Find the latest forecast for a post ID."""
    latest = find_latest_forecast_file(post_id)
    if latest is None:
        return None
    return json.loads(latest.read_text())


def find_log(post_id: int) -> Path | None:
    """Find the log directory for a post ID."""
    log_dir = RUNTIME_LOGS_PATH / str(post_id)
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

    log_dir = find_log(post_id)
    if log_dir:
        log_files = list(log_dir.glob("*.log"))
        typer.echo(f"Logs directory: {log_dir}")
        typer.echo(f"  Files: {len(log_files)}")
        for lf in sorted(log_files)[-3:]:
            typer.echo(f"    - {lf.name} ({lf.stat().st_size} bytes)")


@app.command("list")
def list_forecasts(
    limit: int = typer.Option(20, "-n", "--limit", help="Number of forecasts to show"),
) -> None:
    """List recent forecasts with their metrics summary."""
    forecasts: list[dict] = []
    for post_dir in iter_forecast_dirs():
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
            except (json.JSONDecodeError, OSError):
                continue

    forecasts.sort(key=lambda x: x["timestamp"], reverse=True)
    forecasts = forecasts[:limit]

    if not forecasts:
        typer.echo("No forecasts found")
        return

    typer.echo(
        f"\n{'Post ID':<8} {'Timestamp':<16} {'Calls':<6} {'M':<2} {'L':<2} Title"
    )
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
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Show forecasts with tool errors."""
    errors_found: list[dict] = []
    for post_dir in iter_forecast_dirs(version=version):
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
            except (json.JSONDecodeError, OSError):
                continue

    if not errors_found:
        typer.echo("No forecasts with errors found")
        return

    errors_found.sort(key=lambda x: x["total_errors"], reverse=True)
    errors_found = errors_found[:limit]

    ver_label = f" (version: {version})" if version else ""
    typer.echo(f"\n{'Post':<8} {'Errors':<8} Title{ver_label}")
    typer.echo("-" * 60)
    for e in errors_found:
        typer.echo(f"{e['post_id']:<8} {e['total_errors']:<8} {e['title']}")

        for tool_name, tool_metrics in e["by_tool"].items():
            if tool_metrics.get("error_count", 0) > 0:
                typer.echo(
                    f"  └─ {tool_name}: {tool_metrics['error_count']} errors "
                    f"({tool_metrics.get('error_rate', 'N/A')})"
                )


# ---------------------------------------------------------------------------
# Log filtering
# ---------------------------------------------------------------------------

STREAM_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
    r"INFO aib\.agent\.stream: "
    r"(THINKING|TEXT|TOOL_USE|TOOL_RESULT|SYSTEM|USER_MESSAGE)"
    r"(.*)"
)

COLORS = {
    "THINKING": typer.colors.CYAN,
    "TEXT": typer.colors.WHITE,
    "TOOL_USE": typer.colors.YELLOW,
    "TOOL_RESULT": typer.colors.GREEN,
    "SYSTEM": typer.colors.MAGENTA,
}

MAX_RESULT_LEN = 500


def _find_log_file(post_id: int) -> Path | None:
    """Find the log file for a given post ID."""
    candidates = sorted(RUNTIME_LOGS_PATH.glob(f"{post_id}_*/*.log"), reverse=True)
    return candidates[0] if candidates else None


def _parse_stream_lines(log_path: Path) -> list[tuple[str, str, str]]:
    """Parse log file into (timestamp, event_type, content) tuples."""
    events: list[tuple[str, str, str]] = []
    current_event: tuple[str, str, str] | None = None
    continuation_lines: list[str] = []

    for line in log_path.read_text().splitlines():
        match = STREAM_PATTERN.match(line)
        if match:
            if current_event:
                full_content = current_event[2] + "\n".join(continuation_lines)
                events.append((current_event[0], current_event[1], full_content))
                continuation_lines = []

            timestamp = match.group(1)
            event_type = match.group(2)
            rest = match.group(3).strip()
            current_event = (timestamp, event_type, rest)
        elif (
            current_event and not line.startswith("2026-") and not line.startswith("20")
        ):
            continuation_lines.append(line)

    if current_event:
        full_content = current_event[2] + "\n".join(continuation_lines)
        events.append((current_event[0], current_event[1], full_content))

    return events


def _format_tool_use(content: str) -> str:
    """Format TOOL_USE event for display."""
    match = re.match(r"\[(\w+)\] ([\w_]+): (.*)", content, re.DOTALL)
    if match:
        tool_name = match.group(2)
        args_str = match.group(3).strip()
        try:
            args = json.loads(args_str)
            args_compact = json.dumps(args, separators=(",", ":"))
            if len(args_compact) > 120:
                args_compact = args_compact[:117] + "..."
            return f"{tool_name}({args_compact})"
        except (json.JSONDecodeError, ValueError):
            return f"{tool_name}({args_str[:120]})"
    return content[:200]


def _format_tool_result(content: str, max_len: int) -> str:
    """Format TOOL_RESULT event for display."""
    match = re.match(r"\[(\w+)\]: (.*)", content, re.DOTALL)
    if match:
        result = match.group(2).strip()
        if len(result) > max_len:
            result = result[:max_len] + f"... [{len(result)} chars total]"
        return result
    if len(content) > max_len:
        return content[:max_len] + f"... [{len(content)} chars total]"
    return content


@app.command("log")
def show_log(
    post_id: int = typer.Argument(help="Post ID to show trace for"),
    full: bool = typer.Option(False, help="Show full tool results (no truncation)"),
    tools_only: bool = typer.Option(
        False, "--tools-only", help="Show only tool calls and results"
    ),
    no_color: bool = typer.Option(False, "--no-color", help="Disable colored output"),
) -> None:
    """Show filtered reasoning trace from forecast log."""
    log_path = _find_log_file(post_id)
    if not log_path:
        typer.echo(f"No log found for post {post_id}")
        raise typer.Exit(1)

    events = _parse_stream_lines(log_path)

    result_max = 100_000 if full else MAX_RESULT_LEN
    skip_types = {"USER_MESSAGE"}
    if tools_only:
        skip_types |= {"THINKING", "TEXT", "SYSTEM"}

    typer.echo(f"--- Trace: {log_path} ({len(events)} events) ---\n")

    for timestamp, event_type, content in events:
        if event_type in skip_types:
            continue
        if event_type == "SYSTEM" and "[init]" in content:
            continue

        color = None if no_color else COLORS.get(event_type)
        time_short = timestamp.split(",")[0].split(" ")[1]

        if event_type == "THINKING":
            header = f"[{time_short}] THINKING"
            text = content[:2000] if not full else content
            typer.secho(header, fg=color, bold=True)
            typer.echo(text)
            typer.echo()

        elif event_type == "TEXT":
            header = f"[{time_short}] AGENT"
            typer.secho(header, fg=color, bold=True)
            typer.echo(content[:2000] if not full else content)
            typer.echo()

        elif event_type == "TOOL_USE":
            formatted = _format_tool_use(content)
            typer.secho(f"[{time_short}] CALL ", fg=color, bold=True, nl=False)
            typer.echo(formatted)

        elif event_type == "TOOL_RESULT":
            formatted = _format_tool_result(content, result_max)
            if "error" in formatted.lower() or "failed" in formatted.lower():
                typer.secho(f"  => ERROR: {formatted}", fg=typer.colors.RED)
            else:
                typer.secho("  => ", fg=color, nl=False)
                typer.echo(formatted[:200] if not full else formatted)


@app.command("logs")
def list_logs() -> None:
    """List all available log directories."""
    if not RUNTIME_LOGS_PATH.exists():
        typer.echo("No logs directory found")
        raise typer.Exit(1)

    dirs = sorted(RUNTIME_LOGS_PATH.iterdir())
    for d in dirs:
        if d.is_dir():
            logs = list(d.glob("*.log"))
            size = sum(f.stat().st_size for f in logs)
            typer.echo(f"  {d.name}  ({len(logs)} logs, {size // 1024}KB)")
