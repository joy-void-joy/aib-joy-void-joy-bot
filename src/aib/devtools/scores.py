"""Unified scores table CLI.

Thin CLI wrapper around aib.scoring for interactive use.
"""

import json
import select
import statistics
import sys
import termios
import tty
from datetime import datetime
from pathlib import Path

import typer

from aib.devtools.track_record import load_scores
from aib.paths import (
    load_all_forecast_jsons,
    parse_semver,
    parse_timestamp,
    resolve_version,
)
from aib.scoring import load_all_score_rows
from aib.version import AGENT_VERSION

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
def show(
    post_id: int | None = typer.Option(
        None, "--post-id", "-p", help="Filter by post ID"
    ),
    version: str | None = typer.Option(
        AGENT_VERSION, "--version", "-v", help="Agent version (default: current)"
    ),
    all_versions: bool = typer.Option(
        False, "--all-versions", help="Include all versions"
    ),
    source: str | None = typer.Option(
        None, "--source", "-s", help="Filter by source (live/retrodict)"
    ),
    resolved_only: bool = typer.Option(False, "--resolved", help="Only show resolved"),
) -> None:
    """Show the scores table (formatted)."""
    effective, warning = resolve_version(version, all_versions)
    if warning:
        typer.echo(warning)
    rows = load_all_score_rows(versions=effective)
    if not rows:
        typer.echo("No forecast data found.")
        raise typer.Exit(1)

    if post_id is not None:
        rows = [r for r in rows if r["post_id"] == str(post_id)]
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
def summary(
    version: str | None = typer.Option(
        AGENT_VERSION, "--version", "-v", help="Agent version (default: current)"
    ),
    all_versions: bool = typer.Option(
        False, "--all-versions", help="Include all versions"
    ),
) -> None:
    """Aggregate statistics by type, source, and version."""
    effective, warning = resolve_version(version, all_versions)
    if warning:
        typer.echo(warning)
    rows = load_all_score_rows(versions=effective)
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
def regression(
    version: str | None = typer.Option(
        AGENT_VERSION, "--version", "-v", help="Agent version (default: current)"
    ),
    all_versions: bool = typer.Option(
        False, "--all-versions", help="Include all versions"
    ),
) -> None:
    """Show latest scores for curated regression suite questions."""
    if not REGRESSION_SUITE_PATH.exists():
        typer.echo("No regression suite found at notes/regression_suite.json")
        raise typer.Exit(1)

    effective, warning = resolve_version(version, all_versions)
    if warning:
        typer.echo(warning)
    suite = json.loads(REGRESSION_SUITE_PATH.read_text())
    rows = load_all_score_rows(versions=effective)

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
        AGENT_VERSION, "--version", "-v", help="Agent version (default: current)"
    ),
    all_versions: bool = typer.Option(
        False, "--all-versions", help="Include all versions"
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
    """Show best and worst forecasts."""
    effective, warning = resolve_version(version, all_versions)
    if warning:
        typer.echo(warning)
    rows = load_all_score_rows(versions=effective)
    if not rows:
        typer.echo("No forecast data found.")
        raise typer.Exit(1)

    resolved = [r for r in rows if r["resolved"] == "True"]
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


def _build_strip(
    by_version: dict[str, list[float]],
    version_dates: dict[str, str],
    scraped_at: str,
    term_width: int,
) -> str:
    """Build a horizontal scatter strip chart + summary table."""

    def sort_key(v: str) -> tuple[int, ...]:
        sv = parse_semver(v)
        return sv if sv else (0, 0, 0)

    versions_sorted = sorted(by_version.keys(), key=sort_key)

    version_stats: list[tuple[str, int, float, float, float, float]] = []
    for v in versions_sorted:
        scores = by_version[v]
        n = len(scores)
        avg = statistics.mean(scores)
        std = statistics.stdev(scores) if n > 1 else 0.0
        version_stats.append((v, n, avg, std, min(scores), max(scores)))

    all_scores = [s for v in versions_sorted for s in by_version[v]]
    score_min = min(all_scores)
    score_max = max(all_scores)
    margin = max((score_max - score_min) * 0.03, 1.0)
    range_min = score_min - margin
    range_max = score_max + margin
    score_range = range_max - range_min

    label_width = max(len(f"v{s[0]} (n={s[1]:>2})") for s in version_stats)
    value_width = 14
    chart_width = max(20, term_width - label_width - value_width - 4)

    def to_pos(score: float) -> int:
        return max(
            0, min(chart_width - 1, round((score - range_min) / score_range * (chart_width - 1)))
        )

    if range_max < 0:
        zero_pos = chart_width
    elif range_min > 0:
        zero_pos = -1
    else:
        zero_pos = to_pos(0.0)

    GREEN = "\033[32m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    lines: list[str] = [
        f"{BOLD}Peer score by version (higher is better){RESET}",
        "",
    ]

    for v, n, avg, std, _, _ in version_stats:
        label = f"v{v} (n={n:>2})".ljust(label_width)

        counts: dict[int, int] = {}
        for s in by_version[v]:
            pos = to_pos(s)
            counts[pos] = counts.get(pos, 0) + 1

        parts: list[str] = []
        for col in range(chart_width):
            count = counts.get(col, 0)
            if count > 0:
                color = GREEN if col >= zero_pos else RED
                char = "●" if count == 1 else str(min(count, 9))
                parts.append(f"{color}{char}{RESET}")
            elif col == zero_pos:
                parts.append(f"{DIM}│{RESET}")
            else:
                parts.append(" ")
        row = "".join(parts)

        lines.append(f"  {label} {row}  {avg:>6.1f} ±{std:>3.0f}")

    scale_pad = " " * (label_width + 3)
    ruler = list("─" * chart_width)
    if 0 <= zero_pos < chart_width:
        ruler[zero_pos] = "┼"
    labels = [" "] * chart_width
    lo = f"{score_min:.0f}"
    for i, ch in enumerate(lo):
        if i < chart_width:
            labels[i] = ch
    hi = f"{score_max:.0f}"
    hi_start = chart_width - len(hi)
    for i, ch in enumerate(hi):
        if hi_start + i >= 0:
            labels[hi_start + i] = ch
    if 0 <= zero_pos < chart_width:
        z_start = max(0, zero_pos - 1)
        z_end = min(chart_width, zero_pos + 2)
        overlap = any(labels[j] != " " for j in range(z_start, z_end))
        if not overlap:
            labels[zero_pos] = "0"
    lines.append(f"{scale_pad}{DIM}{''.join(ruler)}{RESET}")
    lines.append(f"{scale_pad}{DIM}{''.join(labels)}{RESET}")

    lines.append("")
    lines.append(f"Scraped: {scraped_at}")
    lines.append("")
    lines.append(
        f"{'Version':<12} {'Date':<12} {'N':>4}  "
        f"{'Avg':>8}  {'Std':>8}  {'Min':>8}  {'Max':>8}"
    )
    lines.append("-" * 72)
    for v, n, avg, std, mn, mx in version_stats:
        d = version_dates.get(v, "-")
        lines.append(
            f"v{v:<11} {d:<12} {n:>4}  "
            f"{avg:>8.2f}  {std:>8.2f}  {mn:>8.2f}  {mx:>8.2f}"
        )
    lines.append("\nPeer score: higher is better  ● individual forecast  2-9 overlapping")

    return "\n".join(lines)


def _load_strip_data(min_n: int) -> tuple[dict[str, list[float]], str] | None:
    """Load and aggregate peer scores by version. Returns None if no data."""
    data = load_scores()
    if not data:
        return None

    peer_by_post: dict[int, float] = {}
    for rec in data.get("records", []):
        pid = rec.get("post_id")
        score = rec.get("score")
        if pid is not None and score is not None:
            peer_by_post[int(pid)] = float(score)

    version_by_post: dict[int, str] = {}
    for d in load_all_forecast_jsons():
        pid = d.get("post_id")
        v = d.get("agent_version")
        if isinstance(pid, int) and v:
            version_by_post[pid] = str(v)

    by_version: dict[str, list[float]] = {}
    for pid, score in peer_by_post.items():
        v = version_by_post.get(pid, "")
        if not v:
            continue
        by_version.setdefault(v, []).append(score)

    by_version = {v: s for v, s in by_version.items() if len(s) >= min_n}
    if not by_version:
        return None

    scraped_at = data.get("scraped_at", "")[:19]
    return by_version, scraped_at


SCATTER_EPOCH = datetime(2026, 2, 1)
ScatterPoint = tuple[float, float, str, int]  # (day_offset, peer_score, version, post_id)


def _load_scatter_data() -> tuple[list[ScatterPoint], list[ScatterPoint], dict[str, list[float]], str] | None:
    """Load scored forecasts for two scatter plots.

    Returns (baseline_by_forecast_date, peer_by_resolution_date,
    version_forecast_dates, scraped_at).
    """
    from datetime import timezone

    data = load_scores()
    if not data:
        return None

    forecast_by_post: dict[int, dict[str, object]] = {}
    for forecast in load_all_forecast_jsons():
        pid = forecast.get("post_id")
        if isinstance(pid, int):
            prev = forecast_by_post.get(pid)
            if prev is None or prev.get("agent_version") is None:
                forecast_by_post[pid] = forecast

    version_forecast_dates: dict[str, list[float]] = {}
    for forecast in forecast_by_post.values():
        version = forecast.get("agent_version") or "0.0.0"
        ts_str = forecast.get("timestamp")
        if isinstance(ts_str, str):
            try:
                dt = parse_timestamp(ts_str)
            except ValueError:
                continue
            day_offset = (dt - SCATTER_EPOCH).total_seconds() / 86400
            version_forecast_dates.setdefault(str(version), []).append(day_offset)

    baseline_points: list[ScatterPoint] = []
    peer_points: list[ScatterPoint] = []

    for rec in data.get("records", []):
        pid = rec.get("post_id")
        peer_score = rec.get("score")
        if pid is None or peer_score is None:
            continue
        pid = int(pid)

        forecast = forecast_by_post.get(pid, {})
        version = forecast.get("agent_version") or "0.0.0"

        ts_str = forecast.get("timestamp")
        if isinstance(ts_str, str):
            try:
                dt = parse_timestamp(ts_str)
            except ValueError:
                dt = None
            if dt is not None:
                day_offset = (dt - SCATTER_EPOCH).total_seconds() / 86400
                baseline = forecast.get("baseline_score")
                if isinstance(baseline, (int, float)):
                    baseline_points.append(
                        (day_offset, float(baseline), str(version), pid)
                    )

        score_ts = rec.get("score_timestamp")
        if score_ts:
            dt_res = datetime.fromtimestamp(
                float(score_ts), tz=timezone.utc
            ).replace(tzinfo=None)
            day_offset_res = (dt_res - SCATTER_EPOCH).total_seconds() / 86400
            peer_points.append(
                (day_offset_res, float(peer_score), str(version), pid)
            )

    if not baseline_points and not peer_points:
        return None

    scraped_at = data.get("scraped_at", "")[:19]
    return baseline_points, peer_points, version_forecast_dates, scraped_at


SATURATED_RING = [
    196, 202, 208, 214, 220, 226,
    190, 154, 118, 82, 46,
    47, 48, 49, 50, 51,
    45, 39, 33, 27, 21,
    57, 93, 129, 165, 201,
    200, 199, 198, 197,
]


def _pick_colors(n: int) -> list[int]:
    """Pick *n* maximally-spaced colors from the saturated 256-color ring."""
    ring = SATURATED_RING
    if n <= 0:
        return []
    if n >= len(ring):
        return list(ring[:n])
    step = len(ring) / n
    return [ring[int(i * step) % len(ring)] for i in range(n)]



def _build_scatter(
    points: list[ScatterPoint],
    title_label: str,
    ylabel: str,
    term_width: int,
    chart_height: int,
    color_map: dict[str, int],
) -> str:
    """Build a single scatter chart panel, colored by version."""
    import plotext as plt
    from datetime import timedelta

    x_all = [p[0] for p in points]
    y_all = [p[1] for p in points]

    sorted_y = sorted(y_all)
    n = len(sorted_y)
    q1 = sorted_y[n // 4]
    q3 = sorted_y[3 * n // 4]
    iqr = q3 - q1
    y_lo = q1 - 2.0 * iqr
    y_hi = q3 + 2.0 * iqr
    clipped = sum(1 for y in y_all if y < y_lo or y > y_hi)
    y_lo = min(y_lo, 0.0)
    y_hi = max(y_hi, 0.0)

    by_version: dict[str, list[ScatterPoint]] = {}
    for p in points:
        by_version.setdefault(p[2], []).append(p)

    plt.clear_figure()
    plt.theme("dark")

    for v, color in color_map.items():
        vp = by_version.get(v)
        if not vp:
            continue
        plt.scatter(
            [p[0] for p in vp], [p[1] for p in vp],
            marker="dot", color=color,
        )

    plt.ylim(y_lo, y_hi)

    x_min, x_max = min(x_all), max(x_all)
    n_ticks = min(6, max(3, term_width // 20))
    step = (x_max - x_min) / max(1, n_ticks - 1)
    tick_pos = [x_min + i * step for i in range(n_ticks)]
    tick_labels = [
        (SCATTER_EPOCH + timedelta(days=d)).strftime("%d/%m") for d in tick_pos
    ]
    plt.xticks(tick_pos, tick_labels)

    plt.hline(0, color="gray+")

    avg = statistics.mean(y_all)
    clip_note = f"  ({clipped} clipped)" if clipped else ""
    plt.title(f"{title_label}  ·  n={len(points)}  avg={avg:.1f}{clip_note}")
    plt.ylabel(ylabel)
    plt.plotsize(max(40, term_width - 10), max(8, chart_height))

    return plt.build()


def _build_trend_output(
    baseline_points: list[ScatterPoint],
    peer_points: list[ScatterPoint],
    version_forecast_dates: dict[str, list[float]],
    scraped_at: str,
    term_width: int,
    term_height: int,
) -> str:
    """Build two stacked scatter charts: baseline by forecast date, peer by resolution date."""
    all_versions = sorted(
        set(p[2] for p in baseline_points + peer_points) | set(version_forecast_dates),
        key=lambda v: parse_semver(v) or (0, 0, 0),
    )
    colors = _pick_colors(len(all_versions))
    color_map = dict(zip(all_versions, colors))
    chart_height = max(8, (term_height - 8) // 2)
    parts: list[str] = []

    if baseline_points:
        parts.append(
            _build_scatter(
                baseline_points,
                "Baseline score by forecast date",
                "baseline",
                term_width,
                chart_height,
                color_map,
            )
        )

    if peer_points:
        parts.append(
            _build_scatter(
                peer_points,
                "Peer score by resolution date",
                "peer",
                term_width,
                chart_height,
                color_map,
            )
        )

    resolved_by_version: dict[str, int] = {}
    for p in peer_points:
        v = p[2]
        resolved_by_version[v] = resolved_by_version.get(v, 0) + 1

    legend_entries: list[tuple[str, int]] = []
    for v, color in color_map.items():
        total = len(version_forecast_dates.get(v, []))
        if not total:
            continue
        resolved = resolved_by_version.get(v, 0)
        ansi = f"\033[38;5;{color}m"
        text = f"v{v} {resolved}/{total}"
        legend_entries.append((f"{ansi}{text}\033[0m", len(text)))

    if legend_entries:
        visible_total = sum(vl for _, vl in legend_entries)
        n = len(legend_entries)
        remaining = max(0, term_width - visible_total)
        gap = remaining // max(1, n - 1) if n > 1 else 0
        parts.append((" " * gap).join(entry for entry, _ in legend_entries))
    parts.append(f"Scraped: {scraped_at}")
    return "\n\n".join(parts)


def _sleep_or_escape(seconds: int) -> bool:
    """Sleep for `seconds`, returning True immediately if Escape is pressed."""
    old = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        elapsed = 0.0
        while elapsed < seconds:
            ready, _, _ = select.select([sys.stdin], [], [], 0.2)
            if ready:
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    return True
            elapsed += 0.2
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
    return False


@app.command()
def strip(
    min_n: int = typer.Option(
        3, "--min-n", help="Minimum scored forecasts to include a version"
    ),
    no_watch: bool = typer.Option(
        False, "--no-watch", help="Disable watch mode (default: refresh every 10m)"
    ),
    interval: int = typer.Option(
        600, "--interval", "-i", help="Watch refresh interval in seconds"
    ),
) -> None:
    """Strip plot of peer scores by agent version (from track record)."""
    import asyncio
    from datetime import datetime

    from rich.console import Console, Group
    from rich.live import Live
    from rich.text import Text

    from aib.devtools.track_record import (
        DEFAULT_USER_ID,
        fetch_scores,
        save_scores,
    )
    from aib.devtools.version import load_version_dates

    console = Console()
    watch = not no_watch
    version_dates = load_version_dates()

    def refresh_scrape() -> None:
        try:
            raw = asyncio.run(fetch_scores(DEFAULT_USER_ID))
            save_scores(raw, DEFAULT_USER_ID)
        except Exception:
            pass

    def build_output() -> str:
        result = _load_strip_data(min_n)
        if not result:
            return f"No versions with >= {min_n} scored forecasts."
        by_version, scraped_at = result
        return _build_strip(
            by_version, version_dates, scraped_at, console.width
        )

    if not watch:
        result = _load_strip_data(min_n)
        if not result:
            typer.echo("No track record data.")
            raise typer.Exit(1)
        by_version, scraped_at = result
        output = _build_strip(
            by_version, version_dates, scraped_at, console.width
        )
        print()
        print(output)
        return

    refresh_scrape()
    output = build_output()
    timestamp = Text(
        f"  updated {datetime.now().strftime('%H:%M:%S')}"
        f"  ·  every {interval}s  ·  esc to quit",
        style="dim",
    )

    with Live(
        Group(Text.from_ansi(output), timestamp),
        console=console,
        refresh_per_second=1,
        screen=True,
    ) as live:
        while True:
            try:
                if _sleep_or_escape(interval):
                    break
                refresh_scrape()
                output = build_output()
            except KeyboardInterrupt:
                break
            timestamp = Text(
                f"  updated {datetime.now().strftime('%H:%M:%S')}"
                f"  ·  every {interval}s  ·  esc to quit",
                style="dim",
            )
            live.update(Group(Text.from_ansi(output), timestamp))


@app.command()
def trend(
    no_watch: bool = typer.Option(
        False, "--no-watch", help="Disable watch mode (default: refresh every 10m)"
    ),
    interval: int = typer.Option(
        600, "--interval", "-i", help="Watch refresh interval in seconds"
    ),
) -> None:
    """Scatter plot of peer scores over time, colored by agent version."""
    import asyncio
    from datetime import datetime

    from rich.console import Console, Group
    from rich.live import Live
    from rich.text import Text

    from aib.devtools.track_record import (
        DEFAULT_USER_ID,
        fetch_scores,
        save_scores,
    )

    console = Console()
    watch = not no_watch

    def refresh_scrape() -> None:
        try:
            raw = asyncio.run(fetch_scores(DEFAULT_USER_ID))
            save_scores(raw, DEFAULT_USER_ID)
        except Exception:
            pass

    def build_output() -> str:
        result = _load_scatter_data()
        if not result:
            return "No scored forecasts found."
        baseline_pts, peer_pts, ver_dates, scraped_at = result
        return _build_trend_output(
            baseline_pts, peer_pts, ver_dates, scraped_at, console.width, console.height
        )

    if not watch:
        result = _load_scatter_data()
        if not result:
            typer.echo("No scored forecasts found.")
            raise typer.Exit(1)
        baseline_pts, peer_pts, ver_dates, scraped_at = result
        output = _build_trend_output(
            baseline_pts, peer_pts, ver_dates, scraped_at, console.width, console.height
        )
        print()
        print(output)
        return

    refresh_scrape()
    output = build_output()
    timestamp = Text(
        f"  updated {datetime.now().strftime('%H:%M:%S')}"
        f"  ·  every {interval}s  ·  esc to quit",
        style="dim",
    )

    with Live(
        Group(Text.from_ansi(output), timestamp),
        console=console,
        refresh_per_second=1,
        screen=True,
    ) as live:
        while True:
            try:
                if _sleep_or_escape(interval):
                    break
                refresh_scrape()
                output = build_output()
            except KeyboardInterrupt:
                break
            timestamp = Text(
                f"  updated {datetime.now().strftime('%H:%M:%S')}"
                f"  ·  every {interval}s  ·  esc to quit",
                style="dim",
            )
            live.update(Group(Text.from_ansi(output), timestamp))
