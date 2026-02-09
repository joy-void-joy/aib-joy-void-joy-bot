#!/usr/bin/env python3
"""Unified scores table CLI.

Thin CLI wrapper around aib.scoring for interactive use.
"""

import json
from pathlib import Path

import typer

from aib.scoring import (
    CSV_COLUMNS,
    SCORES_CSV_PATH,
    load_all_score_rows,
    read_scores_csv,
)

app = typer.Typer(help="Unified scores table for forecasts and retrodictions")

REGRESSION_SUITE_PATH = Path("./notes/regression_suite.json")


@app.command()
def build(
    output: Path = typer.Option(SCORES_CSV_PATH, "-o", help="Output CSV path"),
) -> None:
    """Rebuild the scores CSV from all forecast/retrodict JSONs."""
    rows = load_all_score_rows()

    import csv

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    resolved = sum(1 for r in rows if r["resolved"] == "True")
    live = sum(1 for r in rows if r["source"] == "live")
    retro = sum(1 for r in rows if r["source"] == "retrodict")
    typer.echo(f"Wrote {len(rows)} rows to {output}")
    typer.echo(f"  Live: {live}, Retrodict: {retro}, Resolved: {resolved}")


@app.command()
def show(
    post_id: int | None = typer.Option(
        None, "--post-id", "-p", help="Filter by post ID"
    ),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
    source: str | None = typer.Option(
        None, "--source", "-s", help="Filter by source (live/retrodict)"
    ),
    resolved_only: bool = typer.Option(False, "--resolved", help="Only show resolved"),
) -> None:
    """Show the scores table (formatted)."""
    rows = read_scores_csv()
    if not rows:
        typer.echo("No scores.csv found. Run 'build' first.")
        raise typer.Exit(1)

    if post_id is not None:
        rows = [r for r in rows if r["post_id"] == str(post_id)]
    if version:
        rows = [r for r in rows if r.get("agent_version", "") == version]
    if source:
        rows = [r for r in rows if r["source"] == source]
    if resolved_only:
        rows = [r for r in rows if r["resolved"] == "True"]

    if not rows:
        typer.echo("No matching rows.")
        return

    typer.echo(
        f"\n{'ID':<8} {'Src':<6} {'Ver':<6} {'Type':<8} "
        f"{'Brier':<8} {'LogS':<8} {'Res':<6} {'Title'}"
    )
    typer.echo("-" * 100)

    for r in rows:
        brier = r.get("brier", "")
        log_s = r.get("log_score", "")
        brier_str = f"{float(brier):.4f}" if brier else "-"
        log_str = f"{float(log_s):.4f}" if log_s else "-"
        res = r.get("resolution", "")[:6] if r["resolved"] == "True" else "-"
        ver = r.get("agent_version", "")[:6] or "-"
        typer.echo(
            f"{r['post_id']:<8} {r['source']:<6} {ver:<6} {r['question_type']:<8} "
            f"{brier_str:<8} {log_str:<8} {res:<6} {r['question_title'][:45]}"
        )

    typer.echo(f"\nTotal: {len(rows)} rows")


@app.command()
def summary() -> None:
    """Aggregate statistics by type, source, and version."""
    rows = read_scores_csv()
    if not rows:
        typer.echo("No scores.csv found. Run 'build' first.")
        raise typer.Exit(1)

    typer.echo(f"\n=== Scores Summary ({len(rows)} total rows) ===\n")

    for src in ("live", "retrodict"):
        src_rows = [r for r in rows if r["source"] == src]
        resolved = [r for r in src_rows if r["resolved"] == "True"]
        briers = [float(r["brier"]) for r in resolved if r.get("brier")]
        typer.echo(
            f"{src.upper()}: {len(src_rows)} forecasts, {len(resolved)} resolved"
        )
        if briers:
            typer.echo(
                f"  Avg Brier: {sum(briers) / len(briers):.4f} (n={len(briers)})"
            )
        typer.echo()

    versions: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        v = r.get("agent_version", "") or "unknown"
        versions.setdefault(v, []).append(r)

    if len(versions) > 1 or "unknown" not in versions:
        typer.echo("By version:")
        for v, v_rows in sorted(versions.items()):
            resolved = [r for r in v_rows if r["resolved"] == "True"]
            briers = [float(r["brier"]) for r in resolved if r.get("brier")]
            brier_str = f"avg Brier {sum(briers) / len(briers):.4f}" if briers else ""
            typer.echo(
                f"  {v}: {len(v_rows)} forecasts, {len(resolved)} resolved {brier_str}"
            )
        typer.echo()

    typer.echo("By type:")
    types: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        types.setdefault(r["question_type"], []).append(r)

    for qtype, t_rows in sorted(types.items()):
        resolved = [r for r in t_rows if r["resolved"] == "True"]
        typer.echo(f"  {qtype}: {len(t_rows)} forecasts, {len(resolved)} resolved")


@app.command()
def compare(
    version_a: str = typer.Argument(help="First version to compare"),
    version_b: str = typer.Argument(help="Second version to compare"),
) -> None:
    """Compare scores between two agent versions on overlapping questions."""
    rows = read_scores_csv()
    if not rows:
        typer.echo("No scores.csv found. Run 'build' first.")
        raise typer.Exit(1)

    a_rows = {r["post_id"]: r for r in rows if r.get("agent_version", "") == version_a}
    b_rows = {r["post_id"]: r for r in rows if r.get("agent_version", "") == version_b}

    overlap = set(a_rows.keys()) & set(b_rows.keys())
    if not overlap:
        typer.echo(f"No overlapping questions between {version_a} and {version_b}.")
        return

    typer.echo(
        f"\n=== Comparison: {version_a} vs {version_b} ({len(overlap)} questions) ===\n"
    )
    typer.echo(
        f"{'ID':<8} {'Type':<8} {'Brier_A':<10} {'Brier_B':<10} {'Delta':<10} {'Title'}"
    )
    typer.echo("-" * 100)

    a_better = 0
    b_better = 0
    tied = 0
    a_briers: list[float] = []
    b_briers: list[float] = []

    for pid in sorted(overlap):
        ra = a_rows[pid]
        rb = b_rows[pid]
        ba = ra.get("brier", "")
        bb = rb.get("brier", "")

        if ba and bb:
            ba_f, bb_f = float(ba), float(bb)
            a_briers.append(ba_f)
            b_briers.append(bb_f)
            delta = bb_f - ba_f
            delta_str = f"{delta:+.4f}"
            if delta < -0.001:
                b_better += 1
            elif delta > 0.001:
                a_better += 1
            else:
                tied += 1
        else:
            ba_f = float(ba) if ba else None
            bb_f = float(bb) if bb else None
            delta_str = "-"

        ba_str = f"{ba_f:.4f}" if ba_f is not None else "-"
        bb_str = f"{bb_f:.4f}" if bb_f is not None else "-"
        title = ra.get("question_title", "")[:40]
        typer.echo(
            f"{pid:<8} {ra['question_type']:<8} "
            f"{ba_str:<10} {bb_str:<10} {delta_str:<10} {title}"
        )

    typer.echo(
        f"\n{version_a} better: {a_better}, {version_b} better: {b_better}, tied: {tied}"
    )
    if a_briers and b_briers:
        avg_a = sum(a_briers) / len(a_briers)
        avg_b = sum(b_briers) / len(b_briers)
        typer.echo(f"Avg Brier: {version_a}={avg_a:.4f}, {version_b}={avg_b:.4f}")


@app.command()
def regression() -> None:
    """Show latest scores for curated regression suite questions.

    Reads notes/regression_suite.json and displays the most recent score for
    each question, enabling quick comparison across agent versions.
    """
    if not REGRESSION_SUITE_PATH.exists():
        typer.echo("No regression suite found at notes/regression_suite.json")
        raise typer.Exit(1)

    suite = json.loads(REGRESSION_SUITE_PATH.read_text())
    rows = read_scores_csv()

    typer.echo(f"\n=== Regression Suite ({len(suite)} questions) ===\n")
    typer.echo(
        f"{'ID':<8} {'Ver':<6} {'Type':<8} "
        f"{'Brier':<8} {'LogS':<8} {'AbsErr':<10} {'CI?':<5} {'Note'}"
    )
    typer.echo("-" * 110)

    scored = 0
    unscored = 0
    post_ids_to_retrodict: list[int] = []

    for item in suite:
        pid = item["post_id"]
        note = item.get("note", "")[:40]

        matching = [r for r in rows if r.get("post_id") == str(pid)]
        if not matching:
            typer.echo(
                f"{pid:<8} {'—':<6} {item['type']:<8} {'—':<8} {'—':<8} {'—':<10} {'—':<5} {note}"
            )
            unscored += 1
            post_ids_to_retrodict.append(pid)
            continue

        latest = matching[-1]
        ver = latest.get("agent_version", "")[:6] or "—"
        brier = latest.get("brier", "")
        log_s = latest.get("log_score", "")
        abs_err = latest.get("abs_error", "")
        within = latest.get("within_ci", "")

        brier_str = f"{float(brier):.4f}" if brier else "—"
        log_str = f"{float(log_s):.4f}" if log_s else "—"
        err_str = f"{float(abs_err):.2f}" if abs_err else "—"
        ci_str = within[:5] if within else "—"

        typer.echo(
            f"{pid:<8} {ver:<6} {item['type']:<8} "
            f"{brier_str:<8} {log_str:<8} {err_str:<10} {ci_str:<5} {note}"
        )
        scored += 1

    typer.echo(f"\nScored: {scored}/{len(suite)}")

    if post_ids_to_retrodict:
        ids = " ".join(str(pid) for pid in post_ids_to_retrodict)
        typer.echo(f"\nMissing retrodictions:\n  uv run forecast retrodict {ids}")


if __name__ == "__main__":
    app()
