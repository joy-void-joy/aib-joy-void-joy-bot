#!/usr/bin/env python3
"""Comprehensive calibration analysis for forecasts and retrodictions.

Calibration is the primary diagnostic: it tells you WHERE you're wrong.
Brier/log scores are outcome metrics (what the tournament scores).

Binary: ECE, MCE, reliability diagram, overconfidence detection, Wilson CIs.
Numeric: PIT histogram, K-S uniformity test, coverage statistics.

Examples:
    uv run python .claude/plugins/aib/scripts/calibration_analysis.py summary
    uv run python .claude/plugins/aib/scripts/calibration_analysis.py binary --source retrodict
    uv run python .claude/plugins/aib/scripts/calibration_analysis.py numeric
    uv run python .claude/plugins/aib/scripts/calibration_analysis.py export -o cal.json
"""

import json
import math
from datetime import datetime
from pathlib import Path
from typing import Annotated

import typer
from pydantic import BaseModel

app = typer.Typer(help="Calibration analysis and diagnostics")

FORECASTS_PATH = Path("./notes/forecasts")
RETRODICT_PATH = Path("./notes/retrodict")
REPORTS_PATH = Path("./notes/feedback_loop")


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


class BucketStats(BaseModel):
    bucket_label: str
    count: int
    predicted_mean: float
    actual_rate: float
    gap: float
    ci_lower: float
    ci_upper: float
    significant: bool


class BinaryCalibration(BaseModel):
    n_forecasts: int
    ece: float
    mce: float
    mce_bucket: str
    overconfidence_score: float
    avg_brier: float
    avg_log_score: float
    buckets: list[BucketStats]
    source: str


class PitCalibration(BaseModel):
    n_forecasts: int
    bin_frequencies: list[float]
    ks_statistic: float
    ks_pvalue: float
    coverage_90: float
    coverage_50: float
    source: str


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def _load_jsons(base_path: Path, version: str | None = None) -> list[dict]:
    """Load all forecast JSON files from a directory tree.

    Expects structure: base_path/{post_id}/{timestamp}.json
    For each post_id, loads ALL files (not just latest) so we can
    deduplicate later based on context.

    If version is provided, only returns forecasts with matching agent_version.
    """
    results = []
    if not base_path.exists():
        return results
    for post_dir in base_path.iterdir():
        if not post_dir.is_dir():
            continue
        for filepath in post_dir.glob("*.json"):
            try:
                data = json.loads(filepath.read_text())
                if "question_type" in data and "timestamp" in data:
                    if version and data.get("agent_version", "") != version:
                        continue
                    results.append(data)
            except Exception:
                continue
    return results


def _dedup_latest(forecasts: list[dict], key_fields: tuple[str, ...]) -> list[dict]:
    """Keep only the latest forecast per key (by timestamp)."""
    latest: dict[tuple, dict] = {}
    for f in forecasts:
        key = tuple(f.get(k) for k in key_fields)
        existing = latest.get(key)
        if existing is None or f.get("timestamp", "") > existing.get("timestamp", ""):
            latest[key] = f
    return list(latest.values())


def load_binary_data(
    source: str = "all", version: str | None = None
) -> list[tuple[float, bool]]:
    """Load resolved binary forecasts as (probability, outcome) pairs."""
    forecasts: list[dict] = []

    if source in ("all", "live"):
        for f in _load_jsons(FORECASTS_PATH, version):
            if (
                f.get("question_type") == "binary"
                and f.get("resolution") in ("yes", "no")
                and f.get("probability") is not None
            ):
                forecasts.append(f)

    if source in ("all", "retrodict"):
        retro = _load_jsons(RETRODICT_PATH, version)
        retro = _dedup_latest(retro, ("post_id", "retrodict_date"))
        for f in retro:
            if f.get("question_type") != "binary":
                continue
            if f.get("probability") is None:
                continue
            resolution = f.get("resolution")
            if resolution not in ("yes", "no"):
                comp = f.get("comparison") or {}
                actual = comp.get("actual_value")
                if actual is None:
                    continue
                resolution = (
                    "yes"
                    if str(actual).lower() in ("true", "yes", "1", "1.0")
                    else "no"
                )
            forecasts.append({**f, "resolution": resolution})

    if source in ("all",):
        forecasts = _dedup_latest(forecasts, ("post_id",))

    return [(f["probability"], f["resolution"] == "yes") for f in forecasts]


def load_numeric_data(
    source: str = "all",
    version: str | None = None,
) -> list[tuple[dict[int, float], float, tuple[float, float] | None]]:
    """Load resolved numeric/discrete forecasts.

    Returns (percentiles, actual_value, confidence_interval) tuples.
    """
    forecasts: list[dict] = []

    if source in ("all", "live"):
        for f in _load_jsons(FORECASTS_PATH, version):
            if f.get("question_type") not in ("numeric", "discrete"):
                continue
            if f.get("percentiles") is None:
                continue
            resolution = f.get("resolution")
            if resolution is None:
                continue
            try:
                float(resolution)
            except (ValueError, TypeError):
                continue
            forecasts.append(f)

    if source in ("all", "retrodict"):
        retro = _load_jsons(RETRODICT_PATH, version)
        retro = _dedup_latest(retro, ("post_id", "retrodict_date"))
        for f in retro:
            if f.get("question_type") not in ("numeric", "discrete"):
                continue
            if f.get("percentiles") is None:
                continue
            resolution = f.get("resolution")
            comp = f.get("comparison") or {}
            actual = comp.get("actual_value") if resolution is None else resolution
            if actual is None:
                continue
            try:
                float(actual)
            except (ValueError, TypeError):
                continue
            forecasts.append({**f, "_actual": float(actual)})

    if source in ("all",):
        forecasts = _dedup_latest(forecasts, ("post_id",))

    results = []
    for f in forecasts:
        pct_raw = f["percentiles"]
        pct = {int(k): float(v) for k, v in pct_raw.items()}
        actual = f.get("_actual")
        if actual is None:
            res = f.get("resolution")
            if res is None:
                continue
            actual = float(res)
        ci = f.get("confidence_interval")
        ci_tuple = (float(ci[0]), float(ci[1])) if ci and len(ci) == 2 else None
        results.append((pct, actual, ci_tuple))

    return results


# ---------------------------------------------------------------------------
# Binary calibration metrics
# ---------------------------------------------------------------------------


def wilson_ci(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score confidence interval for a proportion."""
    if total == 0:
        return (0.0, 1.0)
    p_hat = successes / total
    denom = 1 + z * z / total
    center = (p_hat + z * z / (2 * total)) / denom
    spread = z * math.sqrt((p_hat * (1 - p_hat) + z * z / (4 * total)) / total) / denom
    return (max(0.0, center - spread), min(1.0, center + spread))


def brier_score(prob: float, outcome: bool) -> float:
    return (prob - (1.0 if outcome else 0.0)) ** 2


def log_score(prob: float, outcome: bool) -> float:
    p = max(0.001, min(0.999, prob))
    return math.log(p) if outcome else math.log(1 - p)


def compute_binary_calibration(
    data: list[tuple[float, bool]], n_buckets: int = 10, source: str = "all"
) -> BinaryCalibration:
    """Compute full binary calibration metrics."""
    buckets_data: dict[int, list[tuple[float, bool]]] = {
        i: [] for i in range(n_buckets)
    }

    for prob, outcome in data:
        idx = min(n_buckets - 1, int(prob * n_buckets))
        buckets_data[idx].append((prob, outcome))

    bucket_stats: list[BucketStats] = []
    ece_sum = 0.0
    mce = 0.0
    mce_bucket_label = ""
    overconf_sum = 0.0
    overconf_count = 0

    for i in range(n_buckets):
        entries = buckets_data[i]
        lo = i / n_buckets
        hi = (i + 1) / n_buckets
        label = f"{lo:.0%}-{hi:.0%}"

        if not entries:
            continue

        count = len(entries)
        predicted_mean = sum(p for p, _ in entries) / count
        actual_yes = sum(1 for _, o in entries if o)
        actual_rate = actual_yes / count

        gap = actual_rate - predicted_mean
        ci_lo, ci_hi = wilson_ci(actual_yes, count)
        significant = predicted_mean < ci_lo or predicted_mean > ci_hi

        bucket_stats.append(
            BucketStats(
                bucket_label=label,
                count=count,
                predicted_mean=round(predicted_mean, 4),
                actual_rate=round(actual_rate, 4),
                gap=round(gap, 4),
                ci_lower=round(ci_lo, 4),
                ci_upper=round(ci_hi, 4),
                significant=significant,
            )
        )

        abs_gap = abs(gap)
        ece_sum += count * abs_gap
        if abs_gap > mce:
            mce = abs_gap
            mce_bucket_label = label

        for prob, outcome in entries:
            confidence = max(prob, 1 - prob)
            correct = (prob >= 0.5) == outcome
            overconf_sum += confidence - (1.0 if correct else 0.0)
            overconf_count += 1

    n = len(data)
    ece = ece_sum / n if n > 0 else 0.0

    brier_scores = [brier_score(p, o) for p, o in data]
    log_scores = [log_score(p, o) for p, o in data]

    return BinaryCalibration(
        n_forecasts=n,
        ece=round(ece, 4),
        mce=round(mce, 4),
        mce_bucket=mce_bucket_label,
        overconfidence_score=round(
            overconf_sum / overconf_count if overconf_count > 0 else 0.0, 4
        ),
        avg_brier=round(sum(brier_scores) / n if n > 0 else 0.0, 4),
        avg_log_score=round(sum(log_scores) / n if n > 0 else 0.0, 4),
        buckets=bucket_stats,
        source=source,
    )


# ---------------------------------------------------------------------------
# Numeric calibration (PIT)
# ---------------------------------------------------------------------------


def pit_from_percentiles(percentiles: dict[int, float], actual: float) -> float:
    """Approximate CDF(actual) by interpolating between stored percentiles.

    Extrapolates linearly below p10 (to CDF=0) and above p90 (to CDF=1),
    using the slope of the nearest segment.
    """
    sorted_pcts = sorted(percentiles.items())
    pct_levels = [p / 100.0 for p, _ in sorted_pcts]
    pct_values = [v for _, v in sorted_pcts]

    if not pct_levels:
        return 0.5

    if actual <= pct_values[0]:
        if len(pct_values) >= 2:
            slope = (
                (pct_levels[1] - pct_levels[0]) / (pct_values[1] - pct_values[0])
                if pct_values[1] != pct_values[0]
                else 0.0
            )
            pit = pct_levels[0] - slope * (pct_values[0] - actual)
        else:
            pit = pct_levels[0] / 2
        return max(0.0, pit)

    if actual >= pct_values[-1]:
        if len(pct_values) >= 2:
            slope = (
                (pct_levels[-1] - pct_levels[-2]) / (pct_values[-1] - pct_values[-2])
                if pct_values[-1] != pct_values[-2]
                else 0.0
            )
            pit = pct_levels[-1] + slope * (actual - pct_values[-1])
        else:
            pit = (1.0 + pct_levels[-1]) / 2
        return min(1.0, pit)

    for i in range(len(pct_values) - 1):
        if pct_values[i] <= actual <= pct_values[i + 1]:
            if pct_values[i + 1] == pct_values[i]:
                return (pct_levels[i] + pct_levels[i + 1]) / 2
            frac = (actual - pct_values[i]) / (pct_values[i + 1] - pct_values[i])
            return pct_levels[i] + frac * (pct_levels[i + 1] - pct_levels[i])

    return 0.5


def compute_pit_calibration(
    data: list[tuple[dict[int, float], float, tuple[float, float] | None]],
    n_bins: int = 10,
    source: str = "all",
) -> PitCalibration:
    """Compute PIT histogram and uniformity test."""
    pit_values: list[float] = []
    within_90 = 0
    within_50 = 0
    has_ci = 0

    for pct, actual, ci in data:
        pit = pit_from_percentiles(pct, actual)
        pit_values.append(pit)

        if ci is not None:
            has_ci += 1
            if ci[0] <= actual <= ci[1]:
                within_90 += 1

        p20, p40 = pct.get(20), pct.get(40)
        p60, p80 = pct.get(60), pct.get(80)
        p25 = (
            p20 + (p40 - p20) * 0.25
            if p20 is not None and p40 is not None
            else pct.get(25)
        )
        p75 = (
            p60 + (p80 - p60) * 0.75
            if p60 is not None and p80 is not None
            else pct.get(75)
        )
        if p25 is not None and p75 is not None:
            if p25 <= actual <= p75:
                within_50 += 1

    bin_counts = [0] * n_bins
    for pit in pit_values:
        idx = min(n_bins - 1, int(pit * n_bins))
        bin_counts[idx] += 1
    n = len(pit_values)
    bin_freq = [c / n if n > 0 else 0.0 for c in bin_counts]

    ks_stat = 0.0
    ks_pvalue = 1.0
    if n >= 3:
        try:
            from scipy.stats import kstest

            result = kstest(pit_values, "uniform")
            ks_stat = float(result.statistic)
            ks_pvalue = float(result.pvalue)
        except ImportError:
            sorted_pit = sorted(pit_values)
            for i, v in enumerate(sorted_pit):
                d1 = abs(v - i / n)
                d2 = abs(v - (i + 1) / n)
                ks_stat = max(ks_stat, d1, d2)

    return PitCalibration(
        n_forecasts=n,
        bin_frequencies=[round(f, 4) for f in bin_freq],
        ks_statistic=round(ks_stat, 4),
        ks_pvalue=round(ks_pvalue, 4),
        coverage_90=round(within_90 / has_ci if has_ci > 0 else 0.0, 4),
        coverage_50=round(within_50 / n if n > 0 else 0.0, 4),
        source=source,
    )


# ---------------------------------------------------------------------------
# ASCII visualizations
# ---------------------------------------------------------------------------


def render_reliability_diagram(cal: BinaryCalibration) -> str:
    """ASCII reliability diagram: predicted vs actual with CI bars."""
    lines = [f"  Reliability Diagram (n={cal.n_forecasts})"]
    lines.append("")

    height = 11
    width = 10
    grid: list[list[str]] = [[" "] * (width + 1) for _ in range(height)]

    for bucket in cal.buckets:
        lo_str = bucket.bucket_label.split("-")[0]
        col = int(float(lo_str.strip("%")) / 100 * width)
        col = min(col, width - 1)

        actual_row = height - 1 - round(bucket.actual_rate * (height - 1))
        actual_row = max(0, min(height - 1, actual_row))

        marker = "!" if bucket.significant else "#"
        grid[actual_row][col] = marker

    for row in range(height):
        pct = (height - 1 - row) / (height - 1) * 100
        label = f"{pct:>4.0f}% |"

        diag_col = round(pct / 100 * width)
        if 0 <= diag_col <= width - 1 and grid[row][diag_col] == " ":
            grid[row][diag_col] = "."

        lines.append(f"{label} {''.join(grid[row])}")

    lines.append("       +" + "-" * (width + 1))
    lines.append(
        "        "
        + " ".join(
            f"{i * 10}" if i * 10 < 100 else "100" for i in range(0, width + 1, 2)
        )
    )
    lines.append("            Predicted (%)")
    lines.append("")
    lines.append(
        "  # = actual rate   . = perfect calibration   ! = significant deviation"
    )

    return "\n".join(lines)


def render_pit_histogram(pit: PitCalibration) -> str:
    """ASCII PIT histogram: bars should be uniform height if well-calibrated."""
    lines = [f"  PIT Histogram (n={pit.n_forecasts})"]
    lines.append("")

    max_freq = max(pit.bin_frequencies) if pit.bin_frequencies else 0.1
    bar_height = 8
    expected = 1.0 / len(pit.bin_frequencies) if pit.bin_frequencies else 0.1

    for row in range(bar_height, 0, -1):
        threshold = row / bar_height * max_freq * 1.1
        cells = []
        for freq in pit.bin_frequencies:
            if freq >= threshold:
                cells.append("##")
            else:
                cells.append("  ")
        expected_marker = ""
        if abs(threshold - expected) < max_freq * 1.1 / bar_height / 2:
            expected_marker = " <-- expected (uniform)"
        lines.append(f"  {''.join(cells)}{expected_marker}")

    n_bins = len(pit.bin_frequencies)
    lines.append("  " + "--" * n_bins)
    labels = " ".join(f".{i}" for i in range(n_bins))
    lines.append(f"  {labels}")
    lines.append("        PIT value")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


@app.command("binary")
def binary_cmd(
    source: Annotated[
        str, typer.Option("--source", "-s", help="all, live, or retrodict")
    ] = "all",
    buckets: Annotated[
        int, typer.Option("--buckets", "-b", help="Number of calibration buckets")
    ] = 10,
    version: Annotated[
        str | None, typer.Option("--version", "-v", help="Filter by agent version")
    ] = None,
) -> None:
    """Binary forecast calibration analysis."""
    data = load_binary_data(source, version)
    if not data:
        typer.echo("No resolved binary forecasts found.")
        typer.echo(
            "Run 'resolution_update.py check' or retrodict some questions first."
        )
        raise typer.Exit(1)

    cal = compute_binary_calibration(data, n_buckets=buckets, source=source)

    ver_label = f", version: {version}" if version else ""
    typer.echo(
        f"\n=== Binary Calibration ({cal.n_forecasts} forecasts, source: {source}{ver_label}) ===\n"
    )

    if cal.n_forecasts < 20:
        typer.echo(
            f"  WARNING: Only {cal.n_forecasts} forecasts. "
            "Results are noisy — interpret with caution.\n"
        )

    typer.echo(f"  ECE (Expected Calibration Error): {cal.ece:.4f}")
    typer.echo(
        f"  MCE (Maximum Calibration Error):  {cal.mce:.4f}  (bucket: {cal.mce_bucket})"
    )
    direction = (
        "overconfident"
        if cal.overconfidence_score > 0.02
        else "underconfident"
        if cal.overconfidence_score < -0.02
        else "balanced"
    )
    typer.echo(
        f"  Overconfidence score:             {cal.overconfidence_score:+.4f}  ({direction})"
    )
    typer.echo(
        f"  Avg Brier score:                  {cal.avg_brier:.4f}  (0.25 = random)"
    )
    typer.echo(
        f"  Avg Log score:                    {cal.avg_log_score:.4f}  (-0.69 = random)"
    )

    typer.echo("\n--- Per-Bucket Calibration ---\n")
    typer.echo(
        f"  {'Bucket':<10} {'N':>4} {'Predicted':>10} {'Actual':>8} {'Gap':>8} {'95% CI':>16} {'Sig':>4}"
    )
    typer.echo("  " + "-" * 62)

    for b in cal.buckets:
        sig = " !" if b.significant else ""
        typer.echo(
            f"  {b.bucket_label:<10} {b.count:>4} "
            f"{b.predicted_mean:>9.1%} {b.actual_rate:>7.1%} {b.gap:>+7.1%} "
            f"[{b.ci_lower:.1%}, {b.ci_upper:.1%}]{sig:>4}"
        )

    typer.echo("")
    typer.echo(render_reliability_diagram(cal))


@app.command("numeric")
def numeric_cmd(
    source: Annotated[
        str, typer.Option("--source", "-s", help="all, live, or retrodict")
    ] = "all",
    version: Annotated[
        str | None, typer.Option("--version", "-v", help="Filter by agent version")
    ] = None,
) -> None:
    """Numeric/discrete forecast calibration via PIT analysis."""
    data = load_numeric_data(source, version)
    if not data:
        typer.echo("No resolved numeric/discrete forecasts found.")
        typer.echo("Run retrodictions on numeric questions first.")
        raise typer.Exit(1)

    pit = compute_pit_calibration(data, source=source)

    ver_label = f", version: {version}" if version else ""
    typer.echo(
        f"\n=== Numeric Calibration ({pit.n_forecasts} forecasts, source: {source}{ver_label}) ===\n"
    )

    if pit.n_forecasts < 10:
        typer.echo(
            f"  WARNING: Only {pit.n_forecasts} forecasts. "
            "PIT test has low power — interpret with caution.\n"
        )

    typer.echo(f"  K-S statistic:  {pit.ks_statistic:.4f}  (0 = perfectly uniform)")
    typer.echo(
        f"  K-S p-value:    {pit.ks_pvalue:.4f}  (< 0.05 = significantly non-uniform)"
    )

    if pit.coverage_90 > 0:
        typer.echo(f"  90% CI coverage: {pit.coverage_90:.0%}  (should be ~90%)")
    if pit.coverage_50 > 0:
        typer.echo(f"  50% CI coverage: {pit.coverage_50:.0%}  (should be ~50%)")

    typer.echo(
        "\n--- PIT Bin Frequencies (should each be ~{:.0%}) ---\n".format(
            1 / len(pit.bin_frequencies) if pit.bin_frequencies else 0.1
        )
    )

    for i, freq in enumerate(pit.bin_frequencies):
        bar_len = int(
            freq
            * 50
            / (max(pit.bin_frequencies) if max(pit.bin_frequencies) > 0 else 1)
        )
        expected = 1 / len(pit.bin_frequencies)
        marker = " <" if abs(freq - expected) > expected else ""
        typer.echo(
            f"  [{i / 10:.1f}-{(i + 1) / 10:.1f}) {freq:>5.1%} {'#' * bar_len}{marker}"
        )

    typer.echo("")
    typer.echo(render_pit_histogram(pit))


@app.command("summary")
def summary_cmd(
    source: Annotated[
        str, typer.Option("--source", "-s", help="all, live, or retrodict")
    ] = "all",
    version: Annotated[
        str | None, typer.Option("--version", "-v", help="Filter by agent version")
    ] = None,
) -> None:
    """Combined calibration summary for feedback loop sessions."""
    ver_label = f" (version: {version})" if version else ""
    typer.echo(f"\n=== Calibration Summary{ver_label} ===\n")

    binary_data = load_binary_data(source, version)
    numeric_data = load_numeric_data(source, version)

    if not binary_data and not numeric_data:
        typer.echo("  No resolved forecasts found (binary or numeric).")
        typer.echo("  Run retrodictions to build calibration data.")
        raise typer.Exit(1)

    if binary_data:
        cal = compute_binary_calibration(binary_data, source=source)
        typer.echo(f"  BINARY ({cal.n_forecasts} forecasts)")
        if cal.n_forecasts < 20:
            typer.echo("    (low N — noisy)")
        typer.echo(f"    ECE: {cal.ece:.4f}    MCE: {cal.mce:.4f} ({cal.mce_bucket})")
        direction = (
            "overconfident"
            if cal.overconfidence_score > 0.02
            else "underconfident"
            if cal.overconfidence_score < -0.02
            else "balanced"
        )
        typer.echo(f"    Bias: {direction} ({cal.overconfidence_score:+.4f})")
        typer.echo(f"    Brier: {cal.avg_brier:.4f}    Log: {cal.avg_log_score:.4f}")

        problem_buckets = [b for b in cal.buckets if b.significant]
        if problem_buckets:
            typer.echo(
                f"    Problem buckets: {', '.join(b.bucket_label for b in problem_buckets)}"
            )
        typer.echo("")
    else:
        typer.echo("  BINARY: No resolved forecasts\n")

    if numeric_data:
        pit = compute_pit_calibration(numeric_data, source=source)
        typer.echo(f"  NUMERIC ({pit.n_forecasts} forecasts)")
        if pit.n_forecasts < 10:
            typer.echo("    (low N — noisy)")
        uniform_str = "uniform" if pit.ks_pvalue > 0.05 else "NON-UNIFORM"
        typer.echo(f"    PIT: {uniform_str} (K-S p={pit.ks_pvalue:.3f})")
        if pit.coverage_90 > 0:
            typer.echo(f"    90% CI coverage: {pit.coverage_90:.0%} (target: 90%)")
        typer.echo("")
    else:
        typer.echo("  NUMERIC: No resolved forecasts\n")

    total = len(binary_data) + len(numeric_data)
    if total < 20:
        typer.echo(
            f"  Overall: {total} data points — need more retrodictions for reliable calibration"
        )
    else:
        typer.echo(f"  Overall: {total} data points")


@app.command("export")
def export_cmd(
    output: Annotated[
        Path | None, typer.Option("-o", "--output", help="Output file path")
    ] = None,
    source: Annotated[str, typer.Option("--source", "-s")] = "all",
    version: Annotated[
        str | None, typer.Option("--version", "-v", help="Filter by agent version")
    ] = None,
) -> None:
    """Export calibration data to JSON."""
    binary_data = load_binary_data(source, version)
    numeric_data = load_numeric_data(source, version)

    result: dict = {
        "generated_at": datetime.now().isoformat(),
        "source": source,
        "version": version,
    }

    if binary_data:
        cal = compute_binary_calibration(binary_data, source=source)
        result["binary"] = cal.model_dump()

    if numeric_data:
        pit = compute_pit_calibration(numeric_data, source=source)
        result["numeric"] = pit.model_dump()

    if output is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = REPORTS_PATH / f"{timestamp}_calibration_analysis.json"

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2))
    typer.echo(f"Exported calibration data to {output}")


if __name__ == "__main__":
    app()
