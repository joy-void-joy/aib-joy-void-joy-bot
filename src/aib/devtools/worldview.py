"""Worldview store CLI commands.

Browse, inspect, and maintain the worldview store (notes/worldview/).
"""

import asyncio
import time
from datetime import datetime, timezone

import typer

from aib.paths import WORLDVIEW_PATH
from aib.worldview.lookup import (
    commit_worldview,
    iter_forecast_entries,
    iter_research_entries,
    load_forecast_entry,
    load_research_entry,
)
from aib.worldview.models import EntryState

app = typer.Typer(no_args_is_help=True)


def state_icon(state: EntryState) -> str:
    icons = {
        EntryState.fresh: "●",
        EntryState.stale: "○",
        EntryState.superseded: "⊘",
        EntryState.resolved: "✓",
    }
    return icons.get(state, "?")


def age_label(dt: datetime) -> str:
    delta = datetime.now(timezone.utc) - dt
    hours = delta.total_seconds() / 3600
    if hours < 1:
        return f"{int(delta.total_seconds() / 60)}m"
    if hours < 24:
        return f"{hours:.0f}h"
    return f"{delta.days}d"


@app.command("list")
def list_entries(
    kind: str = typer.Option(
        "all", "--kind", "-k", help="Filter: research, forecasts, all"
    ),
    state: str = typer.Option(
        "active", "--state", "-s", help="Filter: fresh, stale, all, active"
    ),
) -> None:
    """Show all worldview entries with state and staleness."""
    if not WORLDVIEW_PATH.exists():
        typer.echo("No worldview store found.")
        raise typer.Exit(0)

    entries: list[tuple[str, str, EntryState, str, str, datetime]] = []

    if kind in ("all", "research"):
        for e in iter_research_entries():
            entries.append(
                (
                    "research",
                    e.slug,
                    e.state,
                    e.query[:60],
                    age_label(e.updated_at),
                    e.updated_at,
                )
            )

    if kind in ("all", "forecasts"):
        for e in iter_forecast_entries():
            entries.append(
                (
                    "forecast",
                    e.slug,
                    e.state,
                    e.question[:60],
                    age_label(e.updated_at),
                    e.updated_at,
                )
            )

    if state == "active":
        entries = [e for e in entries if e[2] in (EntryState.fresh, EntryState.stale)]
    elif state != "all":
        entries = [e for e in entries if e[2].value == state]

    entries.sort(key=lambda e: e[5], reverse=True)

    if not entries:
        typer.echo("No entries found.")
        raise typer.Exit(0)

    typer.echo(f"{'':2} {'Type':10} {'Age':5} {'State':12} {'Question'}")
    typer.echo("─" * 80)
    for kind_label, slug, entry_state, question, age, *_ in entries:
        icon = state_icon(entry_state)
        typer.echo(
            f"{icon:2} {kind_label:10} {age:5} {entry_state.value:12} {question}"
        )
        typer.echo(f"   {slug}")


@app.command("show")
def show_entry(
    slug: str = typer.Argument(..., help="Entry slug to display"),
) -> None:
    """Display a single worldview entry."""
    entry = load_forecast_entry(slug)
    kind = "forecast"
    if entry is None:
        entry = load_research_entry(slug)
        kind = "research"
    if entry is None:
        typer.echo(f"Entry not found: {slug}")
        raise typer.Exit(1)

    typer.echo(f"\n=== {kind.title()} Entry: {slug} ===\n")
    typer.echo(entry.model_dump_json(indent=2))


@app.command("maintain")
def maintain(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Preview without changes"
    ),
    focus: str | None = typer.Option(
        None,
        "--focus",
        help="Optional focus for the sweep (e.g., 'resolve ready forecasts only')",
    ),
) -> None:
    """Spawn the worldview maintenance sub-agent for a full sweep."""
    from aib.tools.worldview_manager import run_maintenance_agent

    typer.echo("Running worldview maintenance sub-agent...")
    summary = asyncio.run(run_maintenance_agent(focus=focus, dry_run=dry_run)).payload

    if summary is None:
        typer.echo("Sub-agent produced no summary.")
        return

    typer.echo(f"\nActions taken ({len(summary.actions_taken)}):")
    for action in summary.actions_taken:
        typer.echo(f"  • {action}")

    if summary.contradictions_reconciled:
        typer.echo(
            f"\nContradictions reconciled ({len(summary.contradictions_reconciled)}):"
        )
        for c in summary.contradictions_reconciled:
            typer.echo(f"  ⚠ {c}")

    if summary.skipped:
        typer.echo(f"\nSkipped ({len(summary.skipped)}):")
        for s in summary.skipped:
            typer.echo(f"  – {s}")

    if summary.notes:
        typer.echo(f"\nNotes: {summary.notes}")

    if dry_run:
        typer.echo("\n(dry run — no changes made)")


@app.command("loop")
def loop(
    interval: int = typer.Option(
        30, "--interval", help="Minutes between refresh cycles."
    ),
    max_concurrent: int = typer.Option(
        3, "--max-concurrent", help="Concurrent research agents during refresh."
    ),
) -> None:
    """Run the always-on worldview loop: refresh stale entries, then maintain.

    Each cycle re-researches every stale research entry on its own TTL clock,
    then runs the maintenance agent to reconcile contradictions, link research,
    and resolve ready forecasts. Runs independently of forecasting.
    """
    from aib.tools.worldview_manager import run_worldview_refresh

    typer.echo(f"Starting worldview refresh loop (every {interval}m). Ctrl-C to stop.")
    while True:
        cycle_start = time.time()
        report = asyncio.run(run_worldview_refresh(max_concurrent=max_concurrent))

        typer.echo(f"\n[{datetime.now(timezone.utc):%H:%M:%S UTC}] cycle complete")
        typer.echo(f"  Refreshed: {report.refreshed}")
        if report.refresh_errors:
            typer.echo(f"  Refresh errors: {len(report.refresh_errors)}")
        maintenance = report.maintenance
        if maintenance is not None:
            typer.echo(f"  Maintenance actions: {len(maintenance.actions_taken)}")
            if maintenance.contradictions_reconciled:
                typer.echo(
                    f"  Contradictions reconciled: "
                    f"{len(maintenance.contradictions_reconciled)}"
                )
        elapsed = int(time.time() - cycle_start)
        typer.echo(f"  Cycle took {elapsed}s; sleeping {interval}m.")
        time.sleep(interval * 60)


@app.command("resolve")
def resolve(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Preview without changes"
    ),
    min_confidence: float = typer.Option(
        0.7, "--min-confidence", help="AI confidence threshold"
    ),
) -> None:
    """Check sub-forecasts for AI resolution where resolvable_after < now."""
    from aib.tools.worldview_manager import (
        find_resolvable_forecasts,
        resolve_ready_forecasts,
    )

    resolvable = find_resolvable_forecasts()
    if not resolvable:
        typer.echo("No resolvable worldview forecasts found.")
        raise typer.Exit(0)

    typer.echo(f"Found {len(resolvable)} resolvable subforecasts:")
    for e in resolvable:
        typer.echo(f"  {e.slug}: {e.question[:60]}")
        typer.echo(f"    type={e.question_type}, resolvable_after={e.resolvable_after}")

    typer.echo(f"\nRunning AI resolution (min_confidence={min_confidence})...")
    results = asyncio.run(
        resolve_ready_forecasts(dry_run=dry_run, min_confidence=min_confidence)
    )

    resolved_count = sum(1 for r in results if r.get("resolved") and "resolution" in r)
    typer.echo(f"\nChecked: {len(results)}, Resolved: {resolved_count}")

    for r in results:
        slug = r.get("slug")
        if r.get("error"):
            typer.echo(f"  ✗ {slug}: {r['error']}")
        elif r.get("resolved") and "resolution" in r:
            typer.echo(
                f"  ✓ {slug}: {r['resolution']} "
                f"(confidence={r.get('confidence')}, score={r.get('score')})"
            )
        else:
            typer.echo(f"  - {slug}: not resolved (confidence={r.get('confidence')})")

    if not dry_run and resolved_count > 0:
        commit_worldview("worldview: AI resolution sweep")

    if dry_run:
        typer.echo("\n(dry run — no changes made)")
