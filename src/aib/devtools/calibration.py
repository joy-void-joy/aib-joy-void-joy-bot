"""Calibration analysis and diagnostics.

Binary: ECE, MCE, reliability diagram, overconfidence detection, Wilson CIs.
Numeric: PIT histogram, K-S uniformity test, coverage statistics.
CDF sharpness analysis for numeric forecasts.
Basic calibration reports: Brier/log scores, bucket tables.
"""

import json
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Annotated

import typer
from pydantic import BaseModel

from aib.paths import FEEDBACK_PATH as REPORTS_PATH
from aib.paths import (
    iter_forecast_dirs,
    iter_retrodict_dirs,
    load_all_forecast_jsons,
    load_all_retrodict_jsons,
)

app = typer.Typer(no_args_is_help=True)


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


def _load_jsons(*, retrodict: bool = False, version: str | None = None) -> list[dict]:
    """Load forecast JSONs via centralized paths module."""
    if retrodict:
        all_data = load_all_retrodict_jsons()
    else:
        all_data = load_all_forecast_jsons(version=version)
    if version and retrodict:
        all_data = [d for d in all_data if d.get("agent_version", "") == version]
    return all_data  # type: ignore[return-value]


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
        for f in _load_jsons(version=version):
            if (
                f.get("question_type") == "binary"
                and f.get("resolution") in ("yes", "no")
                and f.get("probability") is not None
            ):
                forecasts.append(f)

    if source in ("all", "retrodict"):
        retro = _load_jsons(retrodict=True, version=version)
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
    """Load resolved numeric/discrete forecasts."""
    forecasts: list[dict] = []

    if source in ("all", "live"):
        for f in _load_jsons(version=version):
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
        retro = _load_jsons(retrodict=True, version=version)
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

    results: list[tuple[dict[int, float], float, tuple[float, float] | None]] = []
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
    """Approximate CDF(actual) by interpolating between stored percentiles."""
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
    lines = [f"  Reliability Diagram (n={cal.n_forecasts})", ""]

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
    """ASCII PIT histogram."""
    lines = [f"  PIT Histogram (n={pit.n_forecasts})", ""]

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
# CLI commands — comprehensive analysis
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
            "Run 'aib-devtools resolution check' or retrodict some questions first."
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


# ---------------------------------------------------------------------------
# CLI commands — basic report (from calibration_report.py)
# ---------------------------------------------------------------------------


def _load_resolved_binary() -> list[dict]:
    """Load all resolved binary forecasts (live only, latest per post)."""
    forecasts: list[dict] = []

    for post_dir in iter_forecast_dirs():
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                if (
                    data.get("question_type") == "binary"
                    and data.get("resolution") in ("yes", "no")
                    and data.get("probability") is not None
                ):
                    forecasts.append(data)
            except (json.JSONDecodeError, OSError):
                continue
    return forecasts


def _get_calibration_bucket(probability: float) -> str:
    if probability < 0.1:
        return "0-10%"
    elif probability < 0.2:
        return "10-20%"
    elif probability < 0.3:
        return "20-30%"
    elif probability < 0.4:
        return "30-40%"
    elif probability < 0.5:
        return "40-50%"
    elif probability < 0.6:
        return "50-60%"
    elif probability < 0.7:
        return "60-70%"
    elif probability < 0.8:
        return "70-80%"
    elif probability < 0.9:
        return "80-90%"
    else:
        return "90-100%"


@app.command("report")
def report_cmd() -> None:
    """Basic calibration report: Brier/log scores and bucket table."""
    forecasts = _load_resolved_binary()
    if not forecasts:
        typer.echo("No resolved binary forecasts found")
        raise typer.Exit(1)

    typer.echo(f"\n=== Calibration Report ({len(forecasts)} resolved binary) ===\n")

    brier_scores_list = []
    log_scores_list = []
    for f in forecasts:
        prob = f["probability"]
        outcome = 1 if f["resolution"] == "yes" else 0
        brier_scores_list.append((prob - outcome) ** 2)
        p = max(0.001, min(0.999, prob))
        log_scores_list.append(math.log(p) if outcome == 1 else math.log(1 - p))

    avg_brier = sum(brier_scores_list) / len(brier_scores_list)
    avg_log = sum(log_scores_list) / len(log_scores_list)

    typer.echo(f"Average Brier Score: {avg_brier:.4f} (lower is better, 0.25 = random)")
    typer.echo(f"Average Log Score:   {avg_log:.4f} (higher is better, -0.69 = random)")

    buckets: dict[str, dict[str, int | float]] = defaultdict(
        lambda: {"count": 0, "yes": 0, "total_prob": 0.0}
    )

    for f in forecasts:
        bucket = _get_calibration_bucket(f["probability"])
        buckets[bucket]["count"] += 1
        if f["resolution"] == "yes":
            buckets[bucket]["yes"] += 1
        buckets[bucket]["total_prob"] += f["probability"]

    typer.echo("\n--- Calibration by Bucket ---\n")
    typer.echo(
        f"{'Bucket':<12} {'Count':>6} {'Actual%':>10} {'Predicted%':>12} {'Gap':>8}"
    )
    typer.echo("-" * 50)

    bucket_order = [
        "0-10%",
        "10-20%",
        "20-30%",
        "30-40%",
        "40-50%",
        "50-60%",
        "60-70%",
        "70-80%",
        "80-90%",
        "90-100%",
    ]

    for bucket in bucket_order:
        if bucket not in buckets:
            continue
        data = buckets[bucket]
        count = data["count"]
        actual_pct = 100 * data["yes"] / count if count > 0 else 0
        pred_pct = 100 * data["total_prob"] / count if count > 0 else 0
        gap = actual_pct - pred_pct
        gap_indicator = ""
        if abs(gap) > 15:
            gap_indicator = " !"
        typer.echo(
            f"{bucket:<12} {count:>6} {actual_pct:>9.1f}% {pred_pct:>11.1f}% {gap:>+7.1f}%{gap_indicator}"
        )


@app.command("detail")
def detail_cmd(
    limit: int = typer.Option(20, "-n", "--limit", help="Max forecasts to show"),
) -> None:
    """Show detailed forecast-by-forecast results."""
    forecasts = _load_resolved_binary()
    if not forecasts:
        typer.echo("No resolved binary forecasts found")
        raise typer.Exit(1)

    scored = []
    for f in forecasts:
        prob = f["probability"]
        outcome = 1 if f["resolution"] == "yes" else 0
        bs = (prob - outcome) ** 2
        scored.append(
            {
                "post_id": f.get("post_id") or f.get("question_id"),
                "title": (f.get("question_title") or "Unknown")[:40],
                "prob": prob,
                "outcome": f["resolution"],
                "brier": bs,
            }
        )

    scored.sort(key=lambda x: -x["brier"])

    typer.echo("\n=== Forecast Details (sorted by Brier, worst first) ===\n")
    typer.echo(f"{'Post':<8} {'Prob':>6} {'Outcome':>8} {'Brier':>8} Title")
    typer.echo("-" * 70)

    for item in scored[:limit]:
        typer.echo(
            f"{item['post_id']:<8} {item['prob']:>5.0%} {item['outcome']:>8} "
            f"{item['brier']:>7.3f}  {item['title']}"
        )


# ---------------------------------------------------------------------------
# CLI commands — CDF sharpness (from cdf_sharpness.py)
# ---------------------------------------------------------------------------


def _load_numeric_with_cdf(base: Path, source: str) -> list[dict[str, object]]:
    """Load numeric forecasts that have CDF data and resolutions."""
    results: list[dict[str, object]] = []
    if not base.exists():
        return results

    for post_dir in base.iterdir():
        if not post_dir.is_dir():
            continue
        for filepath in post_dir.glob("*.json"):
            try:
                data = json.loads(filepath.read_text())
            except (json.JSONDecodeError, OSError):
                continue

            qtype = data.get("question_type", "")
            if qtype not in ("numeric", "discrete"):
                continue

            resolution = data.get("resolution")
            if resolution is None:
                comp = data.get("comparison", {})
                if isinstance(comp, dict):
                    resolution = comp.get("actual_value")
            if resolution is None:
                continue

            try:
                res_val = float(str(resolution).replace(",", ""))
            except (ValueError, TypeError):
                continue

            results.append(
                {
                    "post_id": data.get("post_id"),
                    "version": data.get("agent_version", "?"),
                    "title": str(data.get("question_title", ""))[:60],
                    "resolution": res_val,
                    "median": data.get("median"),
                    "ci": data.get("confidence_interval"),
                    "cdf": data.get("cdf"),
                    "percentiles": data.get("percentiles"),
                    "source": source,
                }
            )

    return results


def _compute_pit(data: dict[str, object]) -> float | None:
    """Compute PIT value: where does resolution fall in the CDF?"""
    percentiles = data.get("percentiles")
    if isinstance(percentiles, dict) and percentiles:
        res = float(str(data["resolution"]))
        sorted_pcts = sorted((int(k), float(v)) for k, v in percentiles.items())

        if res <= sorted_pcts[0][1]:
            return sorted_pcts[0][0] / 100.0
        if res >= sorted_pcts[-1][1]:
            return sorted_pcts[-1][0] / 100.0

        for i in range(len(sorted_pcts) - 1):
            p1, v1 = sorted_pcts[i]
            p2, v2 = sorted_pcts[i + 1]
            if v1 <= res <= v2:
                if v2 == v1:
                    return (p1 + p2) / 200.0
                frac = (res - v1) / (v2 - v1)
                return (p1 + frac * (p2 - p1)) / 100.0

    return None


@app.command("cdf")
def cdf_cmd(
    version: str | None = typer.Option(None, "--version", "-v"),
    source: str | None = typer.Option(None, "--source", "-s"),
) -> None:
    """Analyze CDF sharpness across numeric forecasts."""
    all_data: list[dict[str, object]] = []
    for base in {d.parent for d in iter_retrodict_dirs()}:
        all_data.extend(_load_numeric_with_cdf(base, "retrodict"))
    for base in {d.parent for d in iter_forecast_dirs()}:
        all_data.extend(_load_numeric_with_cdf(base, "live"))

    if version:
        all_data = [d for d in all_data if d.get("version") == version]
    if source:
        all_data = [d for d in all_data if d.get("source") == source]

    if not all_data:
        typer.echo("No numeric forecasts with resolutions found.")
        raise typer.Exit(1)

    pit_values: list[tuple[dict[str, object], float]] = []
    for d in all_data:
        pit = _compute_pit(d)
        if pit is not None:
            pit_values.append((d, pit))

    if not pit_values:
        typer.echo("No forecasts with percentile data for PIT analysis.")
        raise typer.Exit(1)

    typer.echo(f"\n=== CDF Sharpness Analysis ({len(pit_values)} forecasts) ===\n")

    bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    bin_labels = ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]
    counts = [0] * 5
    for _, pit in pit_values:
        for i in range(5):
            if bins[i] <= pit < bins[i + 1] or (i == 4 and pit == 1.0):
                counts[i] += 1
                break

    expected = len(pit_values) / 5
    typer.echo("PIT Histogram (should be uniform if well-calibrated):")
    typer.echo(f"  Expected per bin: {expected:.1f}")
    for label, count in zip(bin_labels, counts):
        bar = "\u2588" * count + "\u2591" * max(0, int(expected) - count)
        typer.echo(f"  {label:>8}: {count:>3} {bar}")

    center_count = counts[2]
    center_frac = center_count / len(pit_values)
    typer.echo(f"\n  Center concentration (40-60%): {center_frac:.0%} (ideal: 20%)")
    if center_frac > 0.35:
        typer.echo("  CDFs are too WIDE — resolutions cluster near the median")
    elif center_frac < 0.10:
        typer.echo("  CDFs are too NARROW — resolutions avoid the center")

    typer.echo("\n--- Effective CI Coverage ---")
    for target_pct in [50, 80, 90]:
        lo_pct = (100 - target_pct) / 2 / 100
        hi_pct = 1 - lo_pct
        in_range = sum(1 for _, pit in pit_values if lo_pct <= pit <= hi_pct)
        actual_pct = in_range / len(pit_values) * 100
        delta = actual_pct - target_pct
        flag = " OVER-DISPERSED" if delta > 15 else ""
        typer.echo(
            f"  {target_pct}% CI covers {actual_pct:.0f}% of outcomes "
            f"(delta: {delta:+.0f}pp){flag}"
        )

    typer.echo("\n--- Individual PIT Values (sorted) ---")
    pit_values.sort(key=lambda x: x[1])
    for d, pit in pit_values:
        ci = d.get("ci")
        ci_str = ""
        if isinstance(ci, (list, tuple)) and len(ci) >= 2:
            ci_str = f" CI=[{ci[0]}, {ci[1]}]"
        typer.echo(
            f"  PIT={pit:.2f} v{d['version']} post={d['post_id']} "
            f"median={d['median']} res={d['resolution']}{ci_str}"
        )
        typer.echo(f"    {d['title']}")
