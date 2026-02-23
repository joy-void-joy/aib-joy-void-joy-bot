"""Aggregate metrics across all forecasts."""

import json
from collections import defaultdict

import typer

from aib.paths import iter_forecast_files

app = typer.Typer(no_args_is_help=True)


def load_all_forecasts(version: str | None = None) -> list[dict]:
    """Load all forecast files, optionally filtered by agent version."""
    forecasts: list[dict] = []
    for forecast_file in iter_forecast_files(version=version):
        try:
            data = json.loads(forecast_file.read_text())
            data["_file"] = str(forecast_file)
            data["_post_id"] = forecast_file.parent.name
            forecasts.append(data)
        except (json.JSONDecodeError, OSError):
            continue
    return forecasts


@app.command("summary")
def summary(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Show aggregate summary of all forecasts."""
    forecasts = load_all_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    total = len(forecasts)
    with_metrics = sum(1 for f in forecasts if f.get("tool_metrics"))
    with_tokens = sum(1 for f in forecasts if f.get("token_usage"))
    submitted = sum(1 for f in forecasts if f.get("submitted_at"))
    resolved = sum(1 for f in forecasts if f.get("resolution"))

    typer.echo(f"\n=== Forecast Summary ({total} total) ===\n")
    typer.echo(f"With metrics: {with_metrics} ({100 * with_metrics / total:.0f}%)")
    typer.echo(f"With tokens:  {with_tokens} ({100 * with_tokens / total:.0f}%)")
    typer.echo(f"Submitted:    {submitted} ({100 * submitted / total:.0f}%)")
    typer.echo(f"Resolved:     {resolved} ({100 * resolved / total:.0f}%)")

    total_cost = sum(
        f.get("tool_metrics", {}).get("total_cost_usd", 0) or 0
        for f in forecasts
        if f.get("tool_metrics")
    )
    for f in forecasts:
        if not f.get("tool_metrics") and f.get("cost_usd"):
            total_cost += f.get("cost_usd", 0) or 0

    typer.echo(f"\nTotal cost:   ${total_cost:.2f}")

    total_input = 0
    total_output = 0
    total_cache_read = 0
    for f in forecasts:
        usage = f.get("token_usage", {})
        if usage:
            total_input += usage.get("input_tokens", 0) or 0
            total_output += usage.get("output_tokens", 0) or 0
            total_cache_read += usage.get("cache_read_input_tokens", 0) or 0

    if total_input or total_output:
        typer.echo("\nTokens:")
        typer.echo(f"  Input:      {total_input:,}")
        typer.echo(f"  Output:     {total_output:,}")
        typer.echo(f"  Cache read: {total_cache_read:,}")
        typer.echo(f"  Total:      {total_input + total_output:,}")


@app.command("tools")
def tools(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Show tool usage aggregates."""
    forecasts = load_all_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    tool_stats: dict[str, dict[str, int | float]] = defaultdict(
        lambda: {"calls": 0, "errors": 0, "total_ms": 0}
    )

    for f in forecasts:
        metrics = f.get("tool_metrics", {})
        by_tool = metrics.get("by_tool", {})
        for tool_name, data in by_tool.items():
            tool_stats[tool_name]["calls"] += data.get("call_count", 0)
            tool_stats[tool_name]["errors"] += data.get("error_count", 0)
            avg_ms = data.get("avg_duration_ms", 0)
            count = data.get("call_count", 0)
            tool_stats[tool_name]["total_ms"] += avg_ms * count

    if not tool_stats:
        typer.echo("No tool metrics found")
        return

    typer.echo("\n=== Tool Usage Summary ===\n")
    typer.echo(f"{'Tool':<30} {'Calls':>8} {'Errors':>8} {'Err%':>8} {'Avg ms':>10}")
    typer.echo("-" * 70)

    for tool_name in sorted(tool_stats.keys(), key=lambda t: -tool_stats[t]["calls"]):
        stats = tool_stats[tool_name]
        calls = int(stats["calls"])
        errors = int(stats["errors"])
        err_pct = (100 * errors / calls) if calls > 0 else 0
        avg_ms = stats["total_ms"] / calls if calls > 0 else 0
        err_indicator = " !" if err_pct > 10 else ""
        typer.echo(
            f"{tool_name:<30} {calls:>8} {errors:>8} {err_pct:>7.1f}%{err_indicator} {avg_ms:>9.0f}"
        )


@app.command("by-type")
def by_type(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Show metrics grouped by question type."""
    forecasts = load_all_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    by_qtype: dict[str, list[dict]] = defaultdict(list)
    for f in forecasts:
        qtype = f.get("question_type", "unknown")
        by_qtype[qtype].append(f)

    typer.echo("\n=== Metrics by Question Type ===\n")

    for qtype, qforecasts in sorted(by_qtype.items()):
        count = len(qforecasts)
        with_metrics = sum(1 for f in qforecasts if f.get("tool_metrics"))
        total_calls = sum(
            f.get("tool_metrics", {}).get("total_tool_calls", 0) or 0
            for f in qforecasts
        )
        avg_calls = total_calls / count if count > 0 else 0

        typer.echo(f"{qtype}:")
        typer.echo(f"  Count: {count}")
        typer.echo(f"  With metrics: {with_metrics}")
        typer.echo(f"  Avg tool calls: {avg_calls:.1f}")
        typer.echo()


@app.command("errors")
def errors(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Show forecasts with high error rates."""
    forecasts = load_all_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    with_errors = []
    for f in forecasts:
        metrics = f.get("tool_metrics", {})
        total_errors = metrics.get("total_errors", 0)
        if total_errors and total_errors > 0:
            with_errors.append(
                {
                    "post_id": f.get("_post_id"),
                    "title": (f.get("question_title") or "Unknown")[:40],
                    "errors": total_errors,
                    "by_tool": metrics.get("by_tool", {}),
                }
            )

    if not with_errors:
        typer.echo("No forecasts with errors found")
        return

    with_errors.sort(key=lambda x: -x["errors"])

    typer.echo(f"\n=== Forecasts with Errors ({len(with_errors)} total) ===\n")

    for item in with_errors[:20]:
        typer.echo(f"Post {item['post_id']}: {item['errors']} errors - {item['title']}")
        for tool_name, tool_data in item["by_tool"].items():
            errs = tool_data.get("error_count", 0)
            if errs > 0:
                typer.echo(f"  - {tool_name}: {errs}")
