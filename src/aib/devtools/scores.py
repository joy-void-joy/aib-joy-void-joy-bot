"""Unified scores table CLI.

Thin CLI wrapper around aib.scoring for interactive use.
"""

import json
from pathlib import Path

import typer

from aib.scoring import (
    CSV_COLUMNS,
    load_all_score_rows,
)

app = typer.Typer(no_args_is_help=True)

REGRESSION_SUITE_PATH = Path("./notes/regression_suite.json")

META_PATTERNS = [
    "community prediction",
    "will the cp ",
    "will cp ",
]


def _is_meta(title: str) -> bool:
    t = title.lower()
    return any(p in t for p in META_PATTERNS)


@app.command()
def build(
    output: Path = typer.Option("scores.csv", "-o", help="Output CSV path"),
) -> None:
    """Rebuild the scores CSV from all forecast/retrodict JSONs."""
    import csv

    rows = load_all_score_rows()

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
    rows = load_all_score_rows()
    if not rows:
        typer.echo("No forecast data found.")
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
    rows = load_all_score_rows()
    if not rows:
        typer.echo("No forecast data found.")
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
    rows = load_all_score_rows()
    if not rows:
        typer.echo("No forecast data found.")
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
    """Show latest scores for curated regression suite questions."""
    if not REGRESSION_SUITE_PATH.exists():
        typer.echo("No regression suite found at notes/regression_suite.json")
        raise typer.Exit(1)

    suite = json.loads(REGRESSION_SUITE_PATH.read_text())
    rows = load_all_score_rows()

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


@app.command()
def extremes(
    top_n: int = typer.Option(10, "-n", help="Number of best/worst to show"),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
    source: str | None = typer.Option(
        None, "--source", "-s", help="Filter by source (live/retrodict)"
    ),
    non_meta: bool = typer.Option(False, "--non-meta", help="Exclude meta-predictions"),
    meta_only: bool = typer.Option(False, "--meta-only", help="Only meta-predictions"),
    qtype: str | None = typer.Option(
        None, "--type", "-t", help="Filter by question type (binary/numeric)"
    ),
) -> None:
    """Show best and worst forecasts across all versions."""
    rows = load_all_score_rows()
    if not rows:
        typer.echo("No forecast data found.")
        raise typer.Exit(1)

    resolved = [r for r in rows if r["resolved"] == "True"]

    if version:
        resolved = [r for r in resolved if r.get("agent_version", "") == version]
    if source:
        resolved = [r for r in resolved if r["source"] == source]
    if non_meta:
        resolved = [r for r in resolved if not _is_meta(r.get("question_title", ""))]
    if meta_only:
        resolved = [r for r in resolved if _is_meta(r.get("question_title", ""))]
    if qtype:
        resolved = [r for r in resolved if r["question_type"] == qtype]

    binary = [r for r in resolved if r.get("brier")]
    if binary:
        binary.sort(key=lambda x: float(x["brier"]))

        typer.echo(f"\n=== TOP {top_n} BEST BINARY (lowest Brier) ===")
        _print_binary_rows(binary[:top_n])

        typer.echo(f"\n=== TOP {top_n} WORST BINARY (highest Brier) ===")
        _print_binary_rows(binary[-top_n:])

        typer.echo("\n=== BINARY SUMMARY BY VERSION ===")
        by_ver: dict[str, list[float]] = {}
        for r in binary:
            v = r.get("agent_version", "?") or "?"
            by_ver.setdefault(v, []).append(float(r["brier"]))

        for v in sorted(by_ver.keys()):
            scores = sorted(by_ver[v])
            avg = sum(scores) / len(scores)
            scores_str = ", ".join(f"{s:.3f}" for s in scores)
            typer.echo(f"  v{v}: avg={avg:.3f} n={len(scores)} [{scores_str}]")

    numeric = [
        r
        for r in resolved
        if r["question_type"] in ("numeric", "discrete") and r.get("norm_error")
    ]
    if numeric:
        in_ci = sum(1 for r in numeric if r.get("within_ci") == "True")
        pct = in_ci / len(numeric) * 100 if numeric else 0
        norm_vals = [float(r["norm_error"]) for r in numeric]
        avg_norm = sum(norm_vals) / len(norm_vals)

        typer.echo(
            f"\n=== NUMERIC: {in_ci}/{len(numeric)} within 90% CI ({pct:.0f}%), "
            f"avg norm_error={avg_norm:.2f} ==="
        )

        numeric.sort(key=lambda x: float(x["norm_error"]))
        typer.echo(f"\n--- Best {top_n} (lowest norm_error) ---")
        _print_numeric_rows(numeric[:top_n])

        typer.echo(f"\n--- Worst {top_n} (highest norm_error) ---")
        _print_numeric_rows(numeric[-top_n:])

        ci_misses = [r for r in numeric if r.get("within_ci") == "False"]
        if ci_misses:
            typer.echo(f"\n--- CI Misses ({len(ci_misses)}) ---")
            _print_numeric_rows(ci_misses)

        inner_50 = sum(1 for r in numeric if float(r["norm_error"]) < 0.5)
        inner_pct = inner_50 / len(numeric) * 100
        typer.echo(
            f"\n--- Sharpness: {inner_50}/{len(numeric)} ({inner_pct:.0f}%) "
            f"within inner 50% of CI (ideal ~50%) ---"
        )
        if inner_pct > 70:
            typer.echo("  --> CDFs are too WIDE (over-dispersed)")
        elif inner_pct < 30:
            typer.echo("  --> CDFs are too NARROW (under-dispersed)")


def _print_binary_rows(rows: list[dict[str, str]]) -> None:
    for r in rows:
        ver = r.get("agent_version", "?") or "?"
        brier = float(r["brier"])
        prob = r.get("probability", "?")
        res = r.get("resolution", "?")
        pid = r.get("post_id", "?")
        title = r.get("question_title", "")[:78]
        meta = " [META]" if _is_meta(title) else ""
        typer.echo(f"  Brier={brier:.3f} v{ver} post={pid} prob={prob} res={res}{meta}")
        typer.echo(f"    {title}")


def _print_numeric_rows(rows: list[dict[str, str]]) -> None:
    for r in rows:
        ver = r.get("agent_version", "?") or "?"
        ne = r.get("norm_error", "")
        ne_str = f"{float(ne):.2f}" if ne else "?"
        median = r.get("median", "?")
        res = r.get("resolution", "?")
        pid = r.get("post_id", "?")
        ci = r.get("within_ci", "")
        ci_str = "Y" if ci == "True" else "N" if ci == "False" else "?"
        title = r.get("question_title", "")[:78]
        typer.echo(
            f"  NE={ne_str} v{ver} post={pid} median={median} res={res} CI={ci_str}"
        )
        typer.echo(f"    {title}")
