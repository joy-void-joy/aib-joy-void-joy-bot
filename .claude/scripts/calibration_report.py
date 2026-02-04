#!/usr/bin/env python3
"""Generate calibration reports from resolved forecasts.

Computes Brier scores, log scores, and calibration curves
for binary forecasts that have resolutions.
"""

import json
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import typer

app = typer.Typer(help="Generate calibration reports")

FORECASTS_PATH = Path("./notes/forecasts")
REPORTS_PATH = Path("./notes/feedback_loop")


def load_resolved_binary() -> list[dict]:
    """Load all resolved binary forecasts."""
    forecasts = []
    if not FORECASTS_PATH.exists():
        return forecasts

    for post_dir in FORECASTS_PATH.iterdir():
        if not post_dir.is_dir():
            continue
        # Get the latest forecast for each post
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                # Only binary with resolution and probability
                if (
                    data.get("question_type") == "binary"
                    and data.get("resolution") in ("yes", "no")
                    and data.get("probability") is not None
                ):
                    forecasts.append(data)
            except Exception:
                continue
    return forecasts


def brier_score(probability: float, outcome: int) -> float:
    """Compute Brier score (lower is better, 0-1 scale)."""
    return (probability - outcome) ** 2


def log_score(probability: float, outcome: int) -> float:
    """Compute log score (higher is better, negative values).

    Uses natural log. Clamps probability to [0.001, 0.999] to avoid infinity.
    """
    p = max(0.001, min(0.999, probability))
    if outcome == 1:
        return math.log(p)
    else:
        return math.log(1 - p)


def get_calibration_bucket(probability: float) -> str:
    """Get calibration bucket for a probability."""
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


@app.command("summary")
def summary() -> None:
    """Show calibration summary for resolved forecasts."""
    forecasts = load_resolved_binary()
    if not forecasts:
        typer.echo("No resolved binary forecasts found")
        typer.echo("Run 'resolution_update.py check' to fetch resolutions first")
        raise typer.Exit(1)

    typer.echo(f"\n=== Calibration Summary ({len(forecasts)} resolved binary) ===\n")

    # Compute scores
    brier_scores = []
    log_scores = []
    for f in forecasts:
        prob = f["probability"]
        outcome = 1 if f["resolution"] == "yes" else 0
        brier_scores.append(brier_score(prob, outcome))
        log_scores.append(log_score(prob, outcome))

    avg_brier = sum(brier_scores) / len(brier_scores)
    avg_log = sum(log_scores) / len(log_scores)

    typer.echo(f"Average Brier Score: {avg_brier:.4f} (lower is better, 0.25 = random)")
    typer.echo(f"Average Log Score:   {avg_log:.4f} (higher is better, -0.69 = random)")

    # Calibration buckets
    buckets: dict[str, dict[str, int | float]] = defaultdict(
        lambda: {"count": 0, "yes": 0, "total_prob": 0.0}
    )

    for f in forecasts:
        bucket = get_calibration_bucket(f["probability"])
        buckets[bucket]["count"] += 1
        if f["resolution"] == "yes":
            buckets[bucket]["yes"] += 1
        buckets[bucket]["total_prob"] += f["probability"]

    typer.echo("\n--- Calibration by Bucket ---\n")
    typer.echo(f"{'Bucket':<12} {'Count':>6} {'Actual%':>10} {'Predicted%':>12} {'Gap':>8}")
    typer.echo("-" * 50)

    bucket_order = [
        "0-10%", "10-20%", "20-30%", "30-40%", "40-50%",
        "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"
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
def detail(
    limit: int = typer.Option(20, "-n", "--limit", help="Max forecasts to show"),
) -> None:
    """Show detailed forecast-by-forecast results."""
    forecasts = load_resolved_binary()
    if not forecasts:
        typer.echo("No resolved binary forecasts found")
        raise typer.Exit(1)

    # Sort by Brier score (worst first)
    scored = []
    for f in forecasts:
        prob = f["probability"]
        outcome = 1 if f["resolution"] == "yes" else 0
        bs = brier_score(prob, outcome)
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


@app.command("export")
def export(
    output: Path = typer.Option(None, "-o", "--output", help="Output file path"),
) -> None:
    """Export calibration data to JSON."""
    forecasts = load_resolved_binary()
    if not forecasts:
        typer.echo("No resolved binary forecasts found")
        raise typer.Exit(1)

    # Compute all metrics
    data = {
        "generated_at": datetime.now().isoformat(),
        "forecast_count": len(forecasts),
        "scores": {
            "avg_brier": 0.0,
            "avg_log": 0.0,
        },
        "calibration_buckets": {},
        "forecasts": [],
    }

    brier_scores = []
    log_scores = []
    buckets: dict[str, dict[str, int | float]] = defaultdict(
        lambda: {"count": 0, "yes": 0, "total_prob": 0.0}
    )

    for f in forecasts:
        prob = f["probability"]
        outcome = 1 if f["resolution"] == "yes" else 0
        bs = brier_score(prob, outcome)
        ls = log_score(prob, outcome)

        brier_scores.append(bs)
        log_scores.append(ls)

        bucket = get_calibration_bucket(prob)
        buckets[bucket]["count"] += 1
        if f["resolution"] == "yes":
            buckets[bucket]["yes"] += 1
        buckets[bucket]["total_prob"] += prob

        data["forecasts"].append(
            {
                "post_id": f.get("post_id") or f.get("question_id"),
                "probability": prob,
                "resolution": f["resolution"],
                "brier_score": bs,
                "log_score": ls,
            }
        )

    data["scores"]["avg_brier"] = sum(brier_scores) / len(brier_scores)
    data["scores"]["avg_log"] = sum(log_scores) / len(log_scores)

    for bucket, bdata in buckets.items():
        count = bdata["count"]
        data["calibration_buckets"][bucket] = {
            "count": count,
            "actual_rate": bdata["yes"] / count if count > 0 else 0,
            "predicted_rate": bdata["total_prob"] / count if count > 0 else 0,
        }

    # Output
    if output is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = REPORTS_PATH / f"{timestamp}_calibration.json"

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2))
    typer.echo(f"Exported calibration data to {output}")


if __name__ == "__main__":
    app()
