#!/usr/bin/env python3
"""Analyze CDF sharpness: are numeric distributions too wide?

Computes where resolutions fall in the forecast CDF. If resolutions
cluster near the median (P40-P60), the CDFs are too dispersed.
Well-calibrated CDFs should produce uniformly distributed PIT values.
"""

import json
from pathlib import Path

import typer

app = typer.Typer(help="CDF sharpness analysis for numeric forecasts")

RETRODICT_PATH = Path("./notes/retrodict")
FORECASTS_PATH = Path("./notes/forecasts")


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

            cdf = data.get("cdf")
            ci = data.get("confidence_interval")
            median = data.get("median")
            percentiles = data.get("percentiles")

            results.append(
                {
                    "post_id": data.get("post_id"),
                    "version": data.get("agent_version", "?"),
                    "title": str(data.get("question_title", ""))[:60],
                    "resolution": res_val,
                    "median": median,
                    "ci": ci,
                    "cdf": cdf,
                    "percentiles": percentiles,
                    "source": source,
                }
            )

    return results


def _compute_pit(data: dict[str, object]) -> float | None:
    """Compute PIT value: where does resolution fall in the CDF?

    Returns value in [0, 1]. PIT=0.5 means resolution is at median.
    """
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


@app.callback(invoke_without_command=True)
def analyze(
    version: str | None = typer.Option(None, "--version", "-v"),
    source: str | None = typer.Option(None, "--source", "-s"),
) -> None:
    """Analyze CDF sharpness across numeric forecasts."""
    all_data = _load_numeric_with_cdf(RETRODICT_PATH, "retrodict")
    all_data.extend(_load_numeric_with_cdf(FORECASTS_PATH, "live"))

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

    # PIT histogram (5 bins)
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
        bar = "█" * count + "░" * max(0, int(expected) - count)
        typer.echo(f"  {label:>8}: {count:>3} {bar}")

    center_count = counts[2]  # 40-60% bin
    center_frac = center_count / len(pit_values)
    typer.echo(f"\n  Center concentration (40-60%): {center_frac:.0%} (ideal: 20%)")
    if center_frac > 0.35:
        typer.echo("  ⚠ CDFs are too WIDE — resolutions cluster near the median")
    elif center_frac < 0.10:
        typer.echo("  ⚠ CDFs are too NARROW — resolutions avoid the center")

    # Effective coverage analysis
    typer.echo("\n--- Effective CI Coverage ---")
    for target_pct in [50, 80, 90]:
        lo_pct = (100 - target_pct) / 2 / 100
        hi_pct = 1 - lo_pct
        in_range = sum(1 for _, pit in pit_values if lo_pct <= pit <= hi_pct)
        actual_pct = in_range / len(pit_values) * 100
        delta = actual_pct - target_pct
        flag = " ⚠ OVER-DISPERSED" if delta > 15 else ""
        typer.echo(
            f"  {target_pct}% CI covers {actual_pct:.0f}% of outcomes "
            f"(delta: {delta:+.0f}pp){flag}"
        )

    # Individual forecasts sorted by PIT
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


if __name__ == "__main__":
    app()
