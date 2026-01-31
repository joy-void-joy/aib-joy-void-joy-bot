#!/usr/bin/env python3
"""Collect feedback data from resolved forecasts.

Fetches resolved questions from Metaculus, matches them to our past forecasts,
computes accuracy metrics (Brier score, log loss), and saves structured output
for analysis by the feedback-loop command.

Examples:
    uv run python .claude/scripts/feedback_collect.py
    uv run python .claude/scripts/feedback_collect.py --tournament spring-aib-2026
    uv run python .claude/scripts/feedback_collect.py --since 2026-01-01
"""

import json
import logging
import math
from datetime import datetime
from pathlib import Path
from typing import Annotated, Any

import typer
from pydantic import BaseModel
from forecasting_tools import ApiFilter, MetaculusClient, MetaculusQuestion

# Resolve imports from src/aib
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from src.aib.agent.history import load_past_forecasts

app = typer.Typer(help="Collect feedback data from resolved forecasts")
logger = logging.getLogger(__name__)

FEEDBACK_PATH = Path("./notes/feedback_loop")
LAST_RUN_FILE = FEEDBACK_PATH / "last_run.json"

# Tournament IDs
TOURNAMENTS = {
    "spring-aib-2026": 32916,
    "fall-aib-2025": "fall-aib-2025",
    "metaculus-cup": 32921,
}


class ForecastResult(BaseModel):
    """A forecast matched with its resolution."""

    question_id: int
    question_title: str
    question_type: str
    forecast_timestamp: str
    forecasted_probability: float | None = None
    forecasted_median: float | None = None
    forecasted_percentiles: dict[int, float] | None = None
    resolution: bool | float | str | None = None
    resolution_time: datetime | None = None
    brier_score: float | None = None
    log_score: float | None = None


class FeedbackMetrics(BaseModel):
    """Aggregated metrics from resolved forecasts."""

    collection_timestamp: str
    since_timestamp: str | None
    tournaments: list[str]
    total_resolved_questions: int
    questions_with_forecasts: int
    binary_forecasts: int
    numeric_forecasts: int
    avg_brier_score: float | None = None
    avg_log_score: float | None = None
    calibration_buckets: dict[str, dict[str, float]] | None = None
    results: list[ForecastResult]


def compute_brier_score(probability: float, resolved_true: bool) -> float:
    """Compute Brier score for a binary forecast."""
    outcome = 1.0 if resolved_true else 0.0
    return (probability - outcome) ** 2


def compute_log_score(probability: float, resolved_true: bool) -> float:
    """Compute log score for a binary forecast.

    Returns negative log probability of the correct outcome.
    Lower is better. Capped to avoid -inf for p=0 or p=1.
    """
    p = max(0.001, min(0.999, probability))
    if resolved_true:
        return -math.log(p)
    else:
        return -math.log(1 - p)


def compute_calibration_buckets(
    results: list[ForecastResult],
) -> dict[str, dict[str, float]]:
    """Compute calibration data by probability bucket.

    Returns buckets like {"0.0-0.1": {"count": 5, "avg_forecast": 0.05, "resolution_rate": 0.0}}
    """
    buckets: dict[str, list[tuple[float, bool]]] = {
        "0.0-0.1": [],
        "0.1-0.2": [],
        "0.2-0.3": [],
        "0.3-0.4": [],
        "0.4-0.5": [],
        "0.5-0.6": [],
        "0.6-0.7": [],
        "0.7-0.8": [],
        "0.8-0.9": [],
        "0.9-1.0": [],
    }

    for r in results:
        if r.forecasted_probability is None or r.resolution is None:
            continue
        if not isinstance(r.resolution, bool):
            continue

        p = r.forecasted_probability
        bucket_idx = min(9, int(p * 10))
        bucket_name = list(buckets.keys())[bucket_idx]
        buckets[bucket_name].append((p, r.resolution))

    output = {}
    for bucket_name, entries in buckets.items():
        if entries:
            avg_forecast = sum(p for p, _ in entries) / len(entries)
            resolution_rate = sum(1 for _, resolved in entries if resolved) / len(entries)
            output[bucket_name] = {
                "count": len(entries),
                "avg_forecast": round(avg_forecast, 3),
                "resolution_rate": round(resolution_rate, 3),
            }

    return output


def get_resolution_value(question: MetaculusQuestion) -> bool | float | str | None:
    """Extract typed resolution from a question."""
    typed = question.typed_resolution
    if typed is None:
        return None
    if isinstance(typed, bool):
        return typed
    if isinstance(typed, (int, float)):
        return float(typed)
    return str(typed)


def fetch_resolved_questions(
    tournament_ids: list[str | int],
    since: datetime | None = None,
) -> list[MetaculusQuestion]:
    """Fetch resolved questions from specified tournaments."""
    all_questions: list[MetaculusQuestion] = []
    client = MetaculusClient()

    for tournament_id in tournament_ids:
        logger.info("Fetching resolved questions from tournament %s", tournament_id)

        api_filter = ApiFilter(
            allowed_statuses=["resolved"],
            allowed_tournaments=[tournament_id],
        )

        if since:
            api_filter.scheduled_resolve_time_gt = since

        try:
            questions = client.get_questions_matching_filter(
                api_filter,
                num_questions=500,
                error_if_question_target_missed=False,
            )
            logger.info("Found %d resolved questions in %s", len(questions), tournament_id)
            all_questions.extend(questions)
        except Exception as e:
            logger.warning("Failed to fetch from tournament %s: %s", tournament_id, e)

    return all_questions


def match_forecasts_to_resolutions(
    questions: list[MetaculusQuestion],
) -> list[ForecastResult]:
    """Match our past forecasts to resolved questions."""
    results: list[ForecastResult] = []

    for question in questions:
        question_id = question.id_of_post
        if question_id is None:
            continue

        past_forecasts = load_past_forecasts(question_id)
        if not past_forecasts:
            logger.debug("No forecasts found for question %d", question_id)
            continue

        resolution = get_resolution_value(question)
        if resolution is None:
            logger.debug("No resolution for question %d", question_id)
            continue

        for forecast in past_forecasts:
            result = ForecastResult(
                question_id=question_id,
                question_title=question.question_text[:100],
                question_type=forecast.question_type,
                forecast_timestamp=forecast.timestamp,
                forecasted_probability=forecast.probability,
                forecasted_median=forecast.median,
                forecasted_percentiles=forecast.percentiles,
                resolution=resolution,
                resolution_time=question.actual_resolution_time,
            )

            if forecast.question_type == "binary" and forecast.probability is not None:
                if isinstance(resolution, bool):
                    result.brier_score = compute_brier_score(forecast.probability, resolution)
                    result.log_score = compute_log_score(forecast.probability, resolution)

            results.append(result)

    return results


def load_last_run() -> dict[str, Any]:
    """Load last run metadata."""
    if LAST_RUN_FILE.exists():
        return json.loads(LAST_RUN_FILE.read_text())
    return {}


def save_last_run(data: dict[str, Any]) -> None:
    """Save last run metadata."""
    FEEDBACK_PATH.mkdir(parents=True, exist_ok=True)
    LAST_RUN_FILE.write_text(json.dumps(data, indent=2, default=str))


@app.command()
def main(
    tournament: Annotated[
        list[str] | None,
        typer.Option(
            "--tournament", "-t",
            help="Tournament ID or slug (can specify multiple). Default: spring-aib-2026",
        ),
    ] = None,
    since: Annotated[
        str | None,
        typer.Option(
            "--since", "-s",
            help="Only fetch questions resolved after this date (YYYY-MM-DD). Default: last run.",
        ),
    ] = None,
    all_time: Annotated[
        bool,
        typer.Option(
            "--all-time",
            help="Ignore last run timestamp and fetch all resolved questions.",
        ),
    ] = False,
) -> None:
    """Collect feedback metrics from resolved forecasts."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Resolve tournament IDs
    tournament_ids: list[str | int] = []
    if tournament:
        for t in tournament:
            if t in TOURNAMENTS:
                tournament_ids.append(TOURNAMENTS[t])
            else:
                # Try as numeric ID or slug directly
                try:
                    tournament_ids.append(int(t))
                except ValueError:
                    tournament_ids.append(t)
    else:
        # Default to AIB Spring 2026
        tournament_ids = [TOURNAMENTS["spring-aib-2026"]]

    tournament_names = tournament if tournament else ["spring-aib-2026"]

    # Determine since date
    since_dt: datetime | None = None
    if not all_time:
        if since:
            since_dt = datetime.fromisoformat(since)
        else:
            last_run = load_last_run()
            if last_run.get("last_collection"):
                since_dt = datetime.fromisoformat(last_run["last_collection"])

    logger.info(
        "Collecting feedback for tournaments %s since %s",
        tournament_names,
        since_dt.isoformat() if since_dt else "all time",
    )

    # Fetch resolved questions
    questions = fetch_resolved_questions(tournament_ids, since_dt)
    logger.info("Total resolved questions found: %d", len(questions))

    # Match to our forecasts
    results = match_forecasts_to_resolutions(questions)
    logger.info("Matched %d forecasts to resolutions", len(results))

    # Compute aggregate metrics
    binary_results = [r for r in results if r.brier_score is not None]
    numeric_results = [r for r in results if r.question_type in ("numeric", "discrete")]

    avg_brier = None
    avg_log = None
    if binary_results:
        brier_scores = [r.brier_score for r in binary_results if r.brier_score is not None]
        log_scores = [r.log_score for r in binary_results if r.log_score is not None]
        if brier_scores:
            avg_brier = sum(brier_scores) / len(brier_scores)
        if log_scores:
            avg_log = sum(log_scores) / len(log_scores)

    calibration = compute_calibration_buckets(results)

    metrics = FeedbackMetrics(
        collection_timestamp=datetime.now().isoformat(),
        since_timestamp=since_dt.isoformat() if since_dt else None,
        tournaments=tournament_names,
        total_resolved_questions=len(questions),
        questions_with_forecasts=len(set(r.question_id for r in results)),
        binary_forecasts=len(binary_results),
        numeric_forecasts=len(numeric_results),
        avg_brier_score=round(avg_brier, 4) if avg_brier else None,
        avg_log_score=round(avg_log, 4) if avg_log else None,
        calibration_buckets=calibration if calibration else None,
        results=results,
    )

    # Save metrics
    FEEDBACK_PATH.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = FEEDBACK_PATH / f"{timestamp}_metrics.json"
    output_file.write_text(metrics.model_dump_json(indent=2))
    logger.info("Saved metrics to %s", output_file)

    # Update last run
    save_last_run({
        "last_collection": datetime.now().isoformat(),
        "last_metrics_file": str(output_file),
        "tournaments": tournament_names,
    })

    # Print summary
    print("\n" + "=" * 60)
    print("FEEDBACK COLLECTION SUMMARY")
    print("=" * 60)
    print(f"Tournaments: {', '.join(tournament_names)}")
    print(f"Resolved questions: {len(questions)}")
    print(f"Questions with our forecasts: {metrics.questions_with_forecasts}")
    print(f"Binary forecasts evaluated: {len(binary_results)}")
    print(f"Numeric forecasts: {len(numeric_results)}")

    if avg_brier is not None:
        print(f"\nAverage Brier Score: {avg_brier:.4f}")
        print(f"Average Log Score: {avg_log:.4f}")

    if calibration:
        print("\nCalibration (forecasted → actual resolution rate):")
        for bucket, data in calibration.items():
            print(f"  {bucket}: {data['avg_forecast']:.0%} → {data['resolution_rate']:.0%} (n={data['count']})")

    print(f"\nMetrics saved to: {output_file}")


if __name__ == "__main__":
    app()
