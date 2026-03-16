"""Unified scores table CLI.

Thin CLI wrapper around aib.scoring for interactive use.
Also hosts the Metaculus track-record scraping logic (Playwright headless
browser extraction of React internals from the profile page).
"""

import asyncio
import json
import select
import statistics
import sys
import termios
import tty
from datetime import datetime
from pathlib import Path
from typing import Literal

import typer

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


def refresh_scrape() -> None:
    """Scrape track record and update local forecast JSONs with scores/resolutions."""
    try:
        raw = asyncio.run(fetch_scores(DEFAULT_USER_ID))
        records = raw.get("records")
        resolve_scraped(records if isinstance(records, list) else [])
    except Exception:
        pass


PROFILE_URL = "https://www.metaculus.com/accounts/profile/{user_id}/track-record/"
DEFAULT_USER_ID = 290661

EXTRACT_JS = """
() => {
    const svgs = document.querySelectorAll("svg");
    let chart = null;
    for (const svg of svgs) {
        const p = svg.parentElement;
        if (p && p.className && p.className.toString().includes("VictoryContainer")
            && parseInt(svg.getAttribute("width") || "0") > 500) {
            chart = svg;
            break;
        }
    }
    if (!chart) {
        for (const svg of svgs) {
            if (svg.querySelectorAll("path").length > 100) {
                chart = svg;
                break;
            }
        }
    }
    if (!chart) return { error: "no_chart" };

    const fk = Object.keys(chart).find(k => k.startsWith("__reactFiber"));
    if (!fk) return { error: "no_fiber" };

    let fiber = chart[fk];
    let data = null;
    let username = "";
    let depth = 0;

    while (fiber && depth < 60) {
        const props = fiber.memoizedProps || fiber.pendingProps;
        if (props) {
            const src = props.scatterPlot || props.score_scatter_plot;
            if (src && Array.isArray(src)) {
                data = src;
                username = props.username || "";
                break;
            }
        }
        fiber = fiber.return;
        depth++;
    }
    if (!data || !data.length) return { error: "no_data" };

    return {
        username,
        records: data.map(q => {
            const r = {};
            for (const [k, v] of Object.entries(q)) {
                if (typeof v !== "function" && typeof v !== "object") r[k] = v;
            }
            return r;
        })
    };
}
"""


async def fetch_scores(user_id: int) -> dict[str, object]:
    """Launch headless browser, navigate to track record, extract React data."""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        raise RuntimeError(
            "playwright not installed. Run: uv add playwright && playwright install chromium"
        )

    url = PROFILE_URL.format(user_id=user_id)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
        )
        await page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        try:
            await page.wait_for_selector(
                "svg[class*='VictoryContainer'], svg",
                state="attached",
                timeout=45_000,
            )
        except Exception:
            await browser.close()
            raise RuntimeError("Chart did not render within 45s")

        await page.wait_for_timeout(5_000)
        result = await page.evaluate(EXTRACT_JS)
        await browser.close()

    if isinstance(result, dict) and "error" in result:
        errors = {
            "no_chart": "No score scatter plot found on page",
            "no_fiber": "Cannot access React internals",
            "no_data": "Score data array is empty",
        }
        raise RuntimeError(errors.get(str(result["error"]), str(result["error"])))

    return result


def normalize_resolution(raw: str) -> str | float:
    """Normalize a scraped resolution string to forecast JSON format."""
    s = raw.strip()
    low = s.lower()
    if low in ("yes", "no"):
        return low
    try:
        return float(s)
    except ValueError:
        return s


def resolve_scraped(
    records: list[dict[str, object]],
    version: str | None = None,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Write peer_score, score_timestamp, resolution, baseline_score to forecast JSONs."""
    from aib.agent.history import _update_forecast_json
    from aib.paths import iter_forecast_files, iter_retrodict_files
    from aib.scoring import compute_baseline_score

    scores_by_post: dict[int, dict[str, object]] = {}
    for rec in records:
        pid = rec.get("post_id")
        if isinstance(pid, int):
            scores_by_post[pid] = rec

    updated = 0
    unchanged = 0

    for post_id, rec in sorted(scores_by_post.items()):
        raw_res = rec.get("question_resolution")
        peer = rec.get("score")
        score_ts = rec.get("score_timestamp")

        if raw_res is None or str(raw_res).strip() == "":
            continue

        resolution = normalize_resolution(str(raw_res))

        files = list(iter_forecast_files(post_id, version=version)) + list(
            iter_retrodict_files(post_id, version=version)
        )
        for f in files:
            forecast = json.loads(f.read_text())

            updates: dict[str, object] = {}

            if forecast.get("resolution") is None:
                updates["resolution"] = resolution
                updates["resolution_source"] = "scrape"
            if peer is not None and forecast.get("peer_score") is None:
                updates["peer_score"] = peer
            if score_ts is not None and forecast.get("score_timestamp") is None:
                updates["score_timestamp"] = score_ts

            if forecast.get("baseline_score") is None:
                merged = {**forecast, **updates}
                baseline = compute_baseline_score(merged)
                if baseline is not None:
                    updates["baseline_score"] = baseline

            if not updates:
                unchanged += 1
                continue

            if dry_run:
                typer.echo(f"  {post_id}: {updates}")
            else:
                if _update_forecast_json(f, **updates):
                    typer.echo(f"  {post_id}: {updates}")
            updated += 1

    return updated, unchanged


@app.command()
def scrape(
    user_id: int = typer.Option(
        DEFAULT_USER_ID, "--user-id", "-u", help="Metaculus user ID"
    ),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Only update forecasts for this version"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Scrape track record and update forecast JSONs with peer scores."""
    typer.echo(f"Scraping track record for user {user_id}...")

    data = asyncio.run(fetch_scores(user_id))
    records = data.get("records")
    assert isinstance(records, list)
    typer.echo(f"Scraped {len(records)} records")

    scores = [r["score"] for r in records if r.get("score") is not None]
    if scores:
        avg = sum(scores) / len(scores)
        typer.echo(f"Avg peer score: {avg:.4f} (n={len(scores)})")

    updated, unchanged = resolve_scraped(records, version, dry_run)
    typer.echo(f"\nUpdated: {updated}, Unchanged: {unchanged}")
    if dry_run:
        typer.echo("(dry run)")


@app.command()
def show(
    post_ids: list[int] = typer.Argument(None, help="Post IDs to filter by"),
    post_id: list[int] = typer.Option(
        [], "--post-id", "-p", help="Filter by post ID(s); repeatable"
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
    no_refresh: bool = typer.Option(
        False, "--no-refresh", help="Skip track-record scrape"
    ),
) -> None:
    """Show the scores table (formatted)."""
    all_post_ids = list(post_id) + (post_ids or [])
    if not no_refresh:
        refresh_scrape()
    widen = all_versions or len(all_post_ids) > 0
    effective, warning = resolve_version(version, widen)
    if warning:
        typer.echo(warning)
    rows = load_all_score_rows(versions=effective)
    if not rows:
        typer.echo("No forecast data found.")
        raise typer.Exit(1)

    if all_post_ids:
        pid_strs = {str(p) for p in all_post_ids}
        rows = [r for r in rows if r["post_id"] in pid_strs]
        rows.sort(
            key=lambda r: (
                parse_semver(r.get("agent_version", "") or "0.0.0") or (0, 0, 0),
                r.get("timestamp", ""),
            ),
            reverse=True,
        )
    if source:
        rows = [r for r in rows if r["source"] == source]
    if resolved_only:
        rows = [r for r in rows if r["resolved"] == "True"]

    if not rows:
        typer.echo("No matching rows.")
        return

    typer.echo(
        f"\n{'ID':<8} {'Src':<6} {'Ver':<6} {'Type':<8} "
        f"{'Brier':<8} {'LogS':<8} {'AbsErr':<8} {'NormErr':<8} "
        f"{'Res':<6} {'Title'}"
    )
    typer.echo("-" * 116)

    for r in rows:
        brier = r.get("brier", "")
        log_s = r.get("log_score", "")
        abs_err = r.get("abs_error", "")
        norm_err = r.get("norm_error", "")
        brier_str = f"{float(brier):.4f}" if brier else "-"
        log_str = f"{float(log_s):.4f}" if log_s else "-"
        abs_str = f"{float(abs_err):.2f}" if abs_err else "-"
        norm_str = f"{float(norm_err):.2f}" if norm_err else "-"
        res = r.get("resolution", "")[:6] if r["resolved"] == "True" else "-"
        ver = r.get("agent_version", "")[:6] or "-"
        typer.echo(
            f"{r['post_id']:<8} {r['source']:<6} {ver:<6} {r['question_type']:<8} "
            f"{brier_str:<8} {log_str:<8} {abs_str:<8} {norm_str:<8} "
            f"{res:<6} {r['question_title'][:40]}"
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
    no_refresh: bool = typer.Option(
        False, "--no-refresh", help="Skip track-record scrape"
    ),
) -> None:
    """Aggregate statistics by type, source, and version."""
    if not no_refresh:
        refresh_scrape()
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
    no_refresh: bool = typer.Option(
        False, "--no-refresh", help="Skip track-record scrape"
    ),
) -> None:
    """Compare scores between two agent versions on overlapping questions."""
    if not no_refresh:
        refresh_scrape()
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
    no_refresh: bool = typer.Option(
        False, "--no-refresh", help="Skip track-record scrape"
    ),
) -> None:
    """Show latest scores for curated regression suite questions."""
    if not no_refresh:
        refresh_scrape()
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
    no_refresh: bool = typer.Option(
        False, "--no-refresh", help="Skip track-record scrape"
    ),
) -> None:
    """Show best and worst forecasts."""
    if not no_refresh:
        refresh_scrape()
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
    term_width: int,
    color_map: dict[str, int] | None = None,
    version_totals: dict[str, int] | None = None,
    score_mode: ScoreMode = "peer",
) -> str:
    """Build a horizontal scatter strip chart + summary table."""

    def sort_key(v: str) -> tuple[int, ...]:
        sv = parse_semver(v)
        return sv if sv else (0, 0, 0)

    all_versions = set(by_version.keys())
    if version_totals:
        all_versions |= version_totals.keys()
    versions_sorted = sorted(all_versions, key=sort_key)

    version_stats: list[tuple[str, int, float, float, float, float]] = []
    for v in versions_sorted:
        scores = by_version.get(v, [])
        n = len(scores)
        if n > 0:
            avg = statistics.mean(scores)
            std = statistics.stdev(scores) if n > 1 else 0.0
            version_stats.append((v, n, avg, std, min(scores), max(scores)))
        else:
            version_stats.append((v, 0, 0.0, 0.0, 0.0, 0.0))

    all_scores = sorted(s for v in versions_sorted for s in by_version.get(v, []))
    if not all_scores:
        all_scores = [0.0]
    n_scores = len(all_scores)
    q1 = all_scores[n_scores // 4]
    q3 = all_scores[3 * n_scores // 4]
    iqr = q3 - q1
    clip_lo = min(q1 - 2.0 * iqr, 0.0)
    clip_hi = max(q3 + 2.0 * iqr, 0.0)
    score_min = max(min(all_scores), clip_lo)
    score_max = min(max(all_scores), clip_hi)
    margin = max((score_max - score_min) * 0.03, 1.0)
    range_min = score_min - margin
    range_max = score_max + margin
    score_range = range_max - range_min

    def _date_short(v: str) -> str:
        d = version_dates.get(v, "")
        return d[5:] if len(d) >= 10 else (d or "—")

    def _label(v: str, n: int) -> str:
        ds = _date_short(v)
        total = version_totals.get(v) if version_totals else None
        if total is not None:
            return f"v{v} {ds} {n}/{total}"
        return f"v{v} {ds} (n={n:>2})"

    label_width = max(len(_label(s[0], s[1])) for s in version_stats)
    value_width = 23
    chart_width = max(20, term_width - label_width - value_width - 4)

    def to_pos(score: float) -> int:
        return max(
            0,
            min(
                chart_width - 1,
                round((score - range_min) / score_range * (chart_width - 1)),
            ),
        )

    if range_max < 0:
        zero_pos = chart_width
    elif range_min > 0:
        zero_pos = -1
    else:
        zero_pos = to_pos(0.0)

    if color_map is None:
        colors = _pick_colors(len(versions_sorted))
        color_map = dict(zip(versions_sorted, colors))

    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    lines: list[str] = [
        f"{BOLD}{'Baseline' if score_mode == 'baseline' else 'Peer'} score by version (higher is better){RESET}",
        "",
    ]

    for v, n, avg, std, mn, mx in version_stats:
        label = _label(v, n).ljust(label_width)
        c = color_map.get(v)
        ansi = f"\033[38;5;{c}m" if c is not None else ""

        if n > 0:
            counts: dict[int, int] = {}
            for s in by_version.get(v, []):
                pos = to_pos(s)
                counts[pos] = counts.get(pos, 0) + 1

            parts: list[str] = []
            for col in range(chart_width):
                count = counts.get(col, 0)
                if count > 0:
                    char = "●" if count == 1 else str(min(count, 9))
                    parts.append(f"{ansi}{char}{RESET}")
                elif col == zero_pos:
                    parts.append(f"{DIM}│{RESET}")
                else:
                    parts.append(" ")
            row = "".join(parts)
            stats = f"{avg:>5.1f} ±{std:>3.0f}  {mn:>4.0f}‥{mx:>4.0f}"
            lines.append(f"  {ansi}{label}{RESET} {row}  {stats}")
        else:
            empty = list(" " * chart_width)
            if 0 <= zero_pos < chart_width:
                empty[zero_pos] = f"{DIM}│{RESET}"
            lines.append(f"  {ansi}{label}{RESET} {''.join(empty)}")

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

    lines.append(f"\n{DIM}● individual  2-9 overlapping  avg ±std  min‥max{RESET}")

    return "\n".join(lines)


def _load_peer_data() -> dict[int, tuple[float, str]]:
    """Load one peer score per post_id, deduped (first with version wins).

    Returns {post_id: (peer_score, version)}.  Missing version defaults to "0.0.0".
    """
    best: dict[int, dict[str, object]] = {}
    for forecast in load_all_forecast_jsons():
        pid = forecast.get("post_id")
        if not isinstance(pid, int):
            continue
        peer = forecast.get("peer_score")
        if not isinstance(peer, (int, float)):
            continue
        prev = best.get(pid)
        if prev is None or prev.get("agent_version") is None:
            best[pid] = forecast

    result: dict[int, tuple[float, str]] = {}
    for pid, f in best.items():
        peer = f.get("peer_score")
        if not isinstance(peer, (int, float)):
            continue
        version = f.get("agent_version") or "0.0.0"
        result[pid] = (float(peer), str(version))
    return result


def _load_strip_data(
    min_n: int,
    score_mode: ScoreMode = "peer",
) -> dict[str, list[float]] | None:
    """Aggregate scores by version, applying min_n filter."""
    if score_mode == "peer":
        peer_data = _load_peer_data()
        by_version: dict[str, list[float]] = {}
        for peer_score, version in peer_data.values():
            by_version.setdefault(version, []).append(peer_score)
    else:
        by_version = _load_baseline_strip_data()

    by_version = {v: s for v, s in by_version.items() if len(s) >= min_n}
    if not by_version:
        return None

    return by_version


def _load_baseline_strip_data() -> dict[str, list[float]]:
    """Aggregate baseline scores by version (deduped by post_id)."""
    best: dict[int, dict[str, object]] = {}
    for forecast in load_all_forecast_jsons():
        pid = forecast.get("post_id")
        if not isinstance(pid, int):
            continue
        baseline = forecast.get("baseline_score")
        if not isinstance(baseline, (int, float)):
            continue
        prev = best.get(pid)
        if prev is None or prev.get("agent_version") is None:
            best[pid] = forecast

    by_version: dict[str, list[float]] = {}
    for f in best.values():
        baseline = f.get("baseline_score")
        if not isinstance(baseline, (int, float)):
            continue
        version = str(f.get("agent_version") or "0.0.0")
        by_version.setdefault(version, []).append(float(baseline))
    return by_version


SCATTER_EPOCH = datetime(2026, 2, 1)
ScatterPoint = tuple[float, float, str, int]  # (day_offset, score, version, post_id)

ScoreMode = Literal["baseline", "peer"]

TrendPoint = tuple[
    float, float, float, float, str, int
]  # (forecast_day, resolved_day, baseline_score, peer_score, version, post_id)


def _load_trend_data() -> tuple[list[TrendPoint], dict[str, list[float]]] | None:
    """Load scored forecasts for trend scatter plots.

    Returns (points, version_forecast_dates). Each point carries both dates
    and both scores so the caller can project to any chart configuration.
    """
    from datetime import timezone

    forecast_by_post: dict[int, dict[str, object]] = {}
    for forecast in load_all_forecast_jsons():
        pid = forecast.get("post_id")
        if isinstance(pid, int):
            prev = forecast_by_post.get(pid)
            if prev is None or prev.get("agent_version") is None:
                forecast_by_post[pid] = forecast

    peer_data = _load_peer_data()

    version_forecast_dates: dict[str, list[float]] = {}
    points: list[TrendPoint] = []

    for pid, forecast in forecast_by_post.items():
        version = str(forecast.get("agent_version") or "0.0.0")

        ts_str = forecast.get("timestamp")
        if not isinstance(ts_str, str):
            continue
        try:
            dt = parse_timestamp(ts_str)
        except ValueError:
            continue
        fc_offset = (dt - SCATTER_EPOCH).total_seconds() / 86400
        version_forecast_dates.setdefault(version, []).append(fc_offset)

        baseline = forecast.get("baseline_score")
        score_ts = forecast.get("score_timestamp")
        if (
            not isinstance(baseline, (int, float))
            or not isinstance(score_ts, (int, float))
            or pid not in peer_data
        ):
            continue

        peer_score, _ = peer_data[pid]
        dt_res = datetime.fromtimestamp(score_ts, tz=timezone.utc).replace(tzinfo=None)
        res_offset = (dt_res - SCATTER_EPOCH).total_seconds() / 86400
        points.append(
            (fc_offset, res_offset, float(baseline), peer_score, version, pid)
        )

    if not points:
        return None

    return points, version_forecast_dates


SATURATED_RING = [
    196,
    202,
    208,
    214,
    220,
    226,
    190,
    154,
    118,
    82,
    46,
    47,
    48,
    49,
    50,
    51,
    45,
    39,
    33,
    27,
    21,
    57,
    93,
    129,
    165,
    201,
    200,
    199,
    198,
    197,
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


def _version_color_map_and_totals() -> tuple[dict[str, int], dict[str, int]]:
    """Stable version→color mapping and per-version forecast totals (deduped by post)."""
    post_versions: dict[int, str] = {}
    for d in load_all_forecast_jsons():
        pid = d.get("post_id")
        if not isinstance(pid, int):
            continue
        v = d.get("agent_version") or "0.0.0"
        if isinstance(v, str) and pid not in post_versions:
            post_versions[pid] = v

    totals: dict[str, int] = {}
    for v in post_versions.values():
        totals[v] = totals.get(v, 0) + 1

    all_versions = sorted(totals, key=lambda v: parse_semver(v) or (0, 0, 0))
    colors = _pick_colors(len(all_versions))
    return dict(zip(all_versions, colors)), totals


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
            [p[0] for p in vp],
            [p[1] for p in vp],
            marker="dot",
            color=color,
        )

    n_yticks = max(3, chart_height // 3)
    step = (y_hi - y_lo) / max(1, n_yticks)
    yticks: list[float] = []
    v = 0.0
    while v >= y_lo:
        yticks.append(v)
        v -= step
    v = step
    while v <= y_hi:
        yticks.append(v)
        v += step
    yticks.sort()
    plt.yticks(yticks, [f"{v:.0f}" for v in yticks])
    plt.ylim(yticks[0], yticks[-1])

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
    points: list[TrendPoint],
    version_forecast_dates: dict[str, list[float]],
    term_width: int,
    term_height: int,
    min_n: int = 0,
    score_mode: ScoreMode = "baseline",
) -> str:
    """Build two stacked scatter charts: score by forecast date, score by resolution date."""
    full_color_map, _ = _version_color_map_and_totals()
    all_versions_raw = set(p[4] for p in points) | set(version_forecast_dates)
    if min_n > 0:
        all_versions_raw = {
            v
            for v in all_versions_raw
            if len(version_forecast_dates.get(v, [])) >= min_n
        }
    color_map = {v: full_color_map.get(v, 7) for v in all_versions_raw}
    filtered = [p for p in points if p[4] in all_versions_raw] if min_n > 0 else points
    chart_height = max(8, (term_height - 8) // 2)

    label = "Baseline" if score_mode == "baseline" else "Peer"
    ylabel = "baseline" if score_mode == "baseline" else "peer"

    def _score(p: TrendPoint) -> float:
        return p[2] if score_mode == "baseline" else p[3]

    by_forecast: list[ScatterPoint] = [(p[0], _score(p), p[4], p[5]) for p in filtered]
    by_resolved: list[ScatterPoint] = [(p[1], _score(p), p[4], p[5]) for p in filtered]

    parts: list[str] = []
    if by_forecast:
        parts.append(
            _build_scatter(
                by_forecast,
                f"{label} score by forecast date",
                ylabel,
                term_width,
                chart_height,
                color_map,
            )
        )
    if by_resolved:
        parts.append(
            _build_scatter(
                by_resolved,
                f"{label} score by resolution date",
                ylabel,
                term_width,
                chart_height,
                color_map,
            )
        )

    resolved_by_version: dict[str, int] = {}
    scores_by_version: dict[str, list[float]] = {}
    for p in filtered:
        v = p[4]
        resolved_by_version[v] = resolved_by_version.get(v, 0) + 1
        scores_by_version.setdefault(v, []).append(_score(p))

    legend_entries: list[tuple[str, int]] = []
    for v in sorted(color_map, key=lambda v: parse_semver(v) or (0, 0, 0)):
        color = color_map[v]
        total = len(version_forecast_dates.get(v, []))
        if not total:
            continue
        resolved = resolved_by_version.get(v, 0)
        scores = scores_by_version.get(v, [])
        avg = statistics.mean(scores) if scores else 0.0
        std = statistics.stdev(scores) if len(scores) > 1 else 0.0
        ansi = f"\033[38;5;{color}m"
        text = f"v{v} {resolved}/{total}  {avg:>5.1f} ±{std:.0f}"
        legend_entries.append((f"{ansi}{text}\033[0m", len(text)))

    if legend_entries:
        col_width = max(vl for _, vl in legend_entries) + 3
        cols = max(1, term_width // col_width)
        rows: list[str] = []
        for i in range(0, len(legend_entries), cols):
            chunk = legend_entries[i : i + cols]
            cells = [entry + " " * (col_width - vl) for entry, vl in chunk]
            rows.append("".join(cells).rstrip())
        parts.append("\n".join(rows))
    return "\n\n".join(parts)


def _sleep_or_keypress(seconds: int) -> str | None:
    """Sleep for `seconds`, returning the key pressed or None on timeout."""
    old = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        elapsed = 0.0
        while elapsed < seconds:
            ready, _, _ = select.select([sys.stdin], [], [], 0.2)
            if ready:
                ch = sys.stdin.read(1)
                return ch
            elapsed += 0.2
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
    return None


@app.command()
def strip(
    min_n: int = typer.Option(
        0, "--min-n", help="Minimum scored forecasts to include a version"
    ),
    no_watch: bool = typer.Option(
        False, "--no-watch", help="Disable watch mode (default: refresh every 10m)"
    ),
    interval: int = typer.Option(
        600, "--interval", "-i", help="Watch refresh interval in seconds"
    ),
) -> None:
    """Strip plot of scores by agent version (from track record)."""
    from datetime import datetime

    from rich.console import Console, Group
    from rich.live import Live
    from rich.text import Text

    from aib.devtools.version import load_version_dates

    console = Console()
    watch = not no_watch
    version_dates = load_version_dates()
    mode: ScoreMode = "baseline"

    def build_output() -> str:
        by_version = _load_strip_data(min_n, mode) or {}
        cmap, totals = _version_color_map_and_totals()
        if not by_version and not totals:
            return f"No versions with >= {min_n} scored forecasts."
        return _build_strip(
            by_version,
            version_dates,
            console.width,
            cmap,
            totals,
            mode,
        )

    if not watch:
        refresh_scrape()
        by_version = _load_strip_data(min_n, mode) or {}
        cmap, totals = _version_color_map_and_totals()
        if not by_version and not totals:
            typer.echo("No track record data.")
            raise typer.Exit(1)
        output = _build_strip(
            by_version,
            version_dates,
            console.width,
            cmap,
            totals,
            mode,
        )
        print()
        print(output)
        return

    refresh_scrape()
    output = build_output()
    timestamp = Text(
        f"  updated {datetime.now().strftime('%H:%M:%S')}"
        f"  ·  [{mode}]  ·  s to toggle  ·  esc to quit",
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
                key = _sleep_or_keypress(interval)
                if key == "\x1b":
                    break
                if key == "s":
                    mode = "peer" if mode == "baseline" else "baseline"
                    output = build_output()
                else:
                    refresh_scrape()
                    output = build_output()
            except KeyboardInterrupt:
                break
            timestamp = Text(
                f"  updated {datetime.now().strftime('%H:%M:%S')}"
                f"  ·  [{mode}]  ·  s to toggle  ·  esc to quit",
                style="dim",
            )
            live.update(Group(Text.from_ansi(output), timestamp))


@app.command()
def trend(
    min_n: int = typer.Option(
        0, "--min-n", help="Minimum forecasts to include a version"
    ),
    no_watch: bool = typer.Option(
        False, "--no-watch", help="Disable watch mode (default: refresh every 10m)"
    ),
    interval: int = typer.Option(
        600, "--interval", "-i", help="Watch refresh interval in seconds"
    ),
) -> None:
    """Scatter plot of peer scores over time, colored by agent version."""
    from datetime import datetime

    from rich.console import Console, Group
    from rich.live import Live
    from rich.text import Text

    console = Console()
    watch = not no_watch

    mode: ScoreMode = "baseline"

    def build_output() -> str:
        result = _load_trend_data()
        if not result:
            return "No scored forecasts found."
        pts, ver_dates = result
        return _build_trend_output(
            pts,
            ver_dates,
            console.width,
            console.height,
            min_n,
            mode,
        )

    if not watch:
        refresh_scrape()
        print()
        print(build_output())
        return

    refresh_scrape()
    output = build_output()
    timestamp = Text(
        f"  updated {datetime.now().strftime('%H:%M:%S')}"
        f"  ·  [{mode}]  ·  s to toggle  ·  esc to quit",
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
                key = _sleep_or_keypress(interval)
                if key == "\x1b":
                    break
                if key == "s":
                    mode = "peer" if mode == "baseline" else "baseline"
                    output = build_output()
                else:
                    refresh_scrape()
                    output = build_output()
            except KeyboardInterrupt:
                break
            timestamp = Text(
                f"  updated {datetime.now().strftime('%H:%M:%S')}"
                f"  ·  [{mode}]  ·  s to toggle  ·  esc to quit",
                style="dim",
            )
            live.update(Group(Text.from_ansi(output), timestamp))
