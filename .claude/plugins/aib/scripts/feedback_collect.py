#!/usr/bin/env python3
"""Collect feedback data from resolved forecasts and community prediction comparisons.

Fetches resolved questions from Metaculus, matches them to our past forecasts,
computes accuracy metrics (Brier score, log loss), and compares our forecasts
to community predictions as an early calibration signal.

Examples:
    uv run python .claude/scripts/feedback_collect.py
    uv run python .claude/scripts/feedback_collect.py --tournament spring-aib-2026
    uv run python .claude/scripts/feedback_collect.py --since 2026-01-01
"""

import asyncio
import json
import logging
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated, Any

import typer
from pydantic import BaseModel

# Resolve imports from src/
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))
from metaculus import ApiFilter, AsyncMetaculusClient, BinaryQuestion, MetaculusQuestion
from aib.agent.history import (
    load_past_forecasts,
    load_retrodict_forecasts,
    FORECASTS_BASE_PATH,
)

app = typer.Typer(help="Collect feedback data from resolved forecasts")
logger = logging.getLogger(__name__)

FEEDBACK_BASE_PATH = Path("./notes/feedback_loop")


def get_current_branch() -> str:
    """Get the current git branch name."""
    import subprocess

    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or "main"
    except subprocess.CalledProcessError:
        return "main"


def get_feedback_path() -> Path:
    """Get the feedback path for the current branch."""
    branch = get_current_branch()
    return FEEDBACK_BASE_PATH / branch


def get_last_run_file() -> Path:
    """Get the last run file for the current branch."""
    return get_feedback_path() / "last_run.json"


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
    community_prediction: float | None = None
    cp_divergence: float | None = None  # Our forecast - CP (positive = we're higher)
    resolution: bool | float | str | None = None
    resolution_time: datetime | None = None
    brier_score: float | None = None
    log_score: float | None = None


class CPComparison(BaseModel):
    """Community prediction comparison for an unresolved forecast."""

    question_id: int
    question_title: str
    question_type: str
    forecast_timestamp: str
    our_probability: float
    community_prediction: float
    divergence: float  # Our forecast - CP
    question_status: str


class RetrodictResult(BaseModel):
    """A retrodicted forecast with its known resolution."""

    post_id: int
    question_title: str
    question_type: str
    retrodict_date: str
    forecast_timestamp: str
    forecasted_probability: float | None = None
    forecasted_median: float | None = None
    actual_value: float | str | None = None
    predicted_value: float | str | None = None
    difference: float | None = None
    within_ci: bool | None = None
    brier_score: float | None = None
    score: float | None = None
    score_name: str | None = None


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
    # Community prediction comparison (early signal)
    cp_comparisons: list[CPComparison] = []
    avg_cp_divergence: float | None = None
    cp_comparison_count: int = 0
    # Retrodiction results (known ground truth)
    retrodict_results: list[RetrodictResult] = []
    retrodict_count: int = 0
    retrodict_avg_brier: float | None = None


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
            resolution_rate = sum(1 for _, resolved in entries if resolved) / len(
                entries
            )
            output[bucket_name] = {
                "count": len(entries),
                "avg_forecast": round(avg_forecast, 3),
                "resolution_rate": round(resolution_rate, 3),
            }

    return output


def get_resolution_value(question: MetaculusQuestion) -> bool | float | str | None:
    """Extract typed resolution from a question.

    The resolution_string from the API can be:
    - "yes" / "no" for binary questions
    - A numeric string for numeric/discrete questions
    - An option label for multiple choice
    - "ambiguous" or "annulled" for special cases
    """
    res = question.resolution_string
    if res is None:
        return None

    res_lower = res.lower().strip()

    # Binary resolutions
    if res_lower == "yes":
        return True
    if res_lower == "no":
        return False

    # Special cases
    if res_lower in ("ambiguous", "annulled"):
        return res_lower

    # Try parsing as numeric
    try:
        return float(res)
    except ValueError:
        pass

    # Return as string (e.g., multiple choice option)
    return res


async def fetch_resolved_questions(
    tournament_ids: list[str | int],
    since: datetime | None = None,
    client: AsyncMetaculusClient | None = None,
) -> list[MetaculusQuestion]:
    """Fetch resolved questions from specified tournaments."""
    all_questions: list[MetaculusQuestion] = []
    if client is None:
        client = AsyncMetaculusClient()

    for tournament_id in tournament_ids:
        logger.info("Fetching resolved questions from tournament %s", tournament_id)

        api_filter = ApiFilter(
            allowed_statuses=["resolved"],
            allowed_tournaments=[tournament_id],
        )

        if since:
            api_filter.scheduled_resolve_time_gt = since

        try:
            questions = await client.get_questions_matching_filter(
                api_filter,
                num_questions=500,
            )
            logger.info(
                "Found %d resolved questions in %s", len(questions), tournament_id
            )
            all_questions.extend(questions)
        except Exception as e:
            logger.warning("Failed to fetch from tournament %s: %s", tournament_id, e)

    return all_questions


async def fetch_cp_for_forecasts(client: AsyncMetaculusClient) -> list[CPComparison]:
    """Fetch community predictions for all our saved forecasts.

    This provides an early calibration signal before questions resolve.
    """
    comparisons: list[CPComparison] = []

    # Get all forecast directories (each is a post_id)
    if not FORECASTS_BASE_PATH.exists():
        return comparisons

    post_ids = [
        int(d.name)
        for d in FORECASTS_BASE_PATH.iterdir()
        if d.is_dir() and d.name.isdigit()
    ]

    logger.info("Fetching CP for %d forecasted questions", len(post_ids))

    for i, post_id in enumerate(post_ids):
        # Rate limiting: small delay between requests
        if i > 0 and i % 5 == 0:
            await asyncio.sleep(1.0)

        # Load our forecast
        forecasts = load_past_forecasts(post_id)
        if not forecasts:
            continue

        latest_forecast = forecasts[-1]

        # Only compare binary forecasts with probability
        if (
            latest_forecast.question_type != "binary"
            or latest_forecast.probability is None
        ):
            continue

        # Fetch current question state
        try:
            question = await client.get_question_by_post_id(post_id)
            if isinstance(question, list):
                question = question[0]

            # Get CP if available (only on BinaryQuestion)
            cp: float | None = None
            if isinstance(question, BinaryQuestion):
                cp = question.community_prediction_at_access_time

            if cp is None:
                continue

            # Calculate divergence
            divergence = latest_forecast.probability - cp

            comparisons.append(
                CPComparison(
                    question_id=post_id,
                    question_title=latest_forecast.question_title[:80],
                    question_type=latest_forecast.question_type,
                    forecast_timestamp=latest_forecast.timestamp,
                    our_probability=latest_forecast.probability,
                    community_prediction=cp,
                    divergence=divergence,
                    question_status=question.status.value
                    if question.status
                    else "unknown",
                )
            )
        except Exception as e:
            logger.debug("Failed to fetch CP for post %d: %s", post_id, e)

    return comparisons


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
            # Skip forecasts made after resolution (hindsight, not valid)
            if question.actual_resolution_time:
                try:
                    forecast_dt = datetime.strptime(forecast.timestamp, "%Y%m%d_%H%M%S")
                    resolution_dt = question.actual_resolution_time.replace(tzinfo=None)
                    if forecast_dt > resolution_dt:
                        logger.info(
                            "Skipping post-resolution forecast for %d (forecast: %s, resolved: %s)",
                            question_id, forecast.timestamp, question.actual_resolution_time,
                        )
                        continue
                except ValueError:
                    pass

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
                    result.brier_score = compute_brier_score(
                        forecast.probability, resolution
                    )
                    result.log_score = compute_log_score(
                        forecast.probability, resolution
                    )

            results.append(result)

    return results


def collect_retrodict_results() -> list[RetrodictResult]:
    """Collect results from all retrodicted forecasts.

    Retrodictions have known resolutions embedded in the comparison field,
    so no API calls are needed.
    """
    forecasts = load_retrodict_forecasts()
    results: list[RetrodictResult] = []

    for f in forecasts:
        if not f.retrodict_date:
            continue

        result = RetrodictResult(
            post_id=f.post_id or 0,
            question_title=f.question_title[:80],
            question_type=f.question_type,
            retrodict_date=f.retrodict_date,
            forecast_timestamp=f.timestamp,
            forecasted_probability=f.probability,
            forecasted_median=f.median,
        )

        if f.comparison:
            result.actual_value = f.comparison.actual_value
            result.predicted_value = f.comparison.predicted_value
            result.difference = f.comparison.difference
            result.within_ci = f.comparison.within_ci
            result.score = f.comparison.score
            result.score_name = f.comparison.score_name

        if (
            f.question_type == "binary"
            and f.probability is not None
            and f.comparison
            and f.comparison.actual_value is not None
        ):
            resolved_true = str(f.comparison.actual_value).lower() in ("true", "yes", "1", "1.0")
            result.brier_score = compute_brier_score(f.probability, resolved_true)

        results.append(result)

    return results


def load_last_run() -> dict[str, Any]:
    """Load last run metadata."""
    last_run_file = get_last_run_file()
    if last_run_file.exists():
        return json.loads(last_run_file.read_text())
    return {}


def save_last_run(data: dict[str, Any]) -> None:
    """Save last run metadata."""
    feedback_path = get_feedback_path()
    feedback_path.mkdir(parents=True, exist_ok=True)
    last_run_file = get_last_run_file()
    last_run_file.write_text(json.dumps(data, indent=2, default=str))


@app.command()
def main(
    tournament: Annotated[
        list[str] | None,
        typer.Option(
            "--tournament",
            "-t",
            help="Tournament ID or slug (can specify multiple). Default: spring-aib-2026",
        ),
    ] = None,
    since: Annotated[
        str | None,
        typer.Option(
            "--since",
            "-s",
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
    include_retrodict: Annotated[
        bool,
        typer.Option(
            "--include-retrodict",
            help="Include retrodicted forecasts (from notes/retrodict/) in results.",
        ),
    ] = False,
) -> None:
    """Collect feedback metrics from resolved forecasts."""
    asyncio.run(_main_async(tournament, since, all_time, include_retrodict))


async def _main_async(
    tournament: list[str] | None,
    since: str | None,
    all_time: bool,
    include_retrodict: bool = False,
) -> None:
    """Async implementation of the main command."""
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

    # Create client for API calls
    client = AsyncMetaculusClient()

    # Fetch resolved questions
    questions = await fetch_resolved_questions(tournament_ids, since_dt, client)
    logger.info("Total resolved questions found: %d", len(questions))

    # Match to our forecasts
    results = match_forecasts_to_resolutions(questions)
    logger.info("Matched %d forecasts to resolutions", len(results))

    # Fetch community predictions for all our forecasts (early signal)
    cp_comparisons = await fetch_cp_for_forecasts(client)
    logger.info("Fetched CP for %d forecasts", len(cp_comparisons))

    # Collect retrodiction results
    retrodict_results: list[RetrodictResult] = []
    if include_retrodict:
        retrodict_results = collect_retrodict_results()
        logger.info("Collected %d retrodictions", len(retrodict_results))

    # Compute aggregate metrics
    binary_results = [r for r in results if r.brier_score is not None]
    numeric_results = [r for r in results if r.question_type in ("numeric", "discrete")]

    avg_brier = None
    avg_log = None
    if binary_results:
        brier_scores = [
            r.brier_score for r in binary_results if r.brier_score is not None
        ]
        log_scores = [r.log_score for r in binary_results if r.log_score is not None]
        if brier_scores:
            avg_brier = sum(brier_scores) / len(brier_scores)
        if log_scores:
            avg_log = sum(log_scores) / len(log_scores)

    calibration = compute_calibration_buckets(results)

    # Compute retrodict Brier average
    retrodict_avg_brier = None
    retrodict_brier_scores = [r.brier_score for r in retrodict_results if r.brier_score is not None]
    if retrodict_brier_scores:
        retrodict_avg_brier = sum(retrodict_brier_scores) / len(retrodict_brier_scores)

    # Compute CP divergence stats
    avg_cp_divergence = None
    if cp_comparisons:
        divergences = [c.divergence for c in cp_comparisons]
        avg_cp_divergence = sum(divergences) / len(divergences)

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
        cp_comparisons=cp_comparisons,
        avg_cp_divergence=round(avg_cp_divergence, 4) if avg_cp_divergence else None,
        cp_comparison_count=len(cp_comparisons),
        retrodict_results=retrodict_results,
        retrodict_count=len(retrodict_results),
        retrodict_avg_brier=round(retrodict_avg_brier, 4) if retrodict_avg_brier else None,
    )

    # Save metrics
    feedback_path = get_feedback_path()
    feedback_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = feedback_path / f"{timestamp}_metrics.json"
    output_file.write_text(metrics.model_dump_json(indent=2))
    logger.info("Saved metrics to %s", output_file)

    # Update last run
    save_last_run(
        {
            "last_collection": datetime.now().isoformat(),
            "last_metrics_file": str(output_file),
            "tournaments": tournament_names,
        }
    )

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
            print(
                f"  {bucket}: {data['avg_forecast']:.0%} → {data['resolution_rate']:.0%} (n={data['count']})"
            )

    # Report missed questions (resolved but no forecast)
    forecasted_ids = {r.question_id for r in results}
    missed_questions = [
        q
        for q in questions
        if q.id_of_post is not None and q.id_of_post not in forecasted_ids
    ]
    if missed_questions:
        print(
            f"\nMissed Questions ({len(missed_questions)} resolved without forecast):"
        )
        for q in missed_questions:
            res_str = q.resolution_string or "?"
            title = (
                q.question_text[:60] + "..."
                if len(q.question_text) > 60
                else q.question_text
            )
            print(f"  - [{q.id_of_post}] {title} → {res_str}")

    # Report community prediction comparison (early signal)
    if cp_comparisons:
        print("\n" + "-" * 60)
        print("COMMUNITY PREDICTION COMPARISON (Early Signal)")
        print("-" * 60)
        print(f"Forecasts with CP available: {len(cp_comparisons)}")
        if avg_cp_divergence is not None:
            direction = "higher" if avg_cp_divergence > 0 else "lower"
            print(
                f"Average divergence: {avg_cp_divergence:+.1%} (we are {direction} than CP)"
            )

        # Show large divergences (>15pp)
        large_divergences = [c for c in cp_comparisons if abs(c.divergence) > 0.15]
        if large_divergences:
            print(f"\nLarge divergences (>15pp): {len(large_divergences)}")
            # Sort by absolute divergence
            large_divergences.sort(key=lambda c: abs(c.divergence), reverse=True)
            for c in large_divergences[:10]:  # Top 10
                title = (
                    c.question_title[:50] + "..."
                    if len(c.question_title) > 50
                    else c.question_title
                )
                print(
                    f"  [{c.question_id}] {c.our_probability:.0%} vs CP {c.community_prediction:.0%} ({c.divergence:+.0%})"
                )
                print(f"      {title}")

        # Show systematic bias
        higher_count = sum(1 for c in cp_comparisons if c.divergence > 0.02)
        lower_count = sum(1 for c in cp_comparisons if c.divergence < -0.02)
        if higher_count + lower_count > 0:
            print(
                f"\nBias check: {higher_count} forecasts higher than CP, {lower_count} lower"
            )

    # Report retrodiction results
    if retrodict_results:
        print("\n" + "-" * 60)
        print("RETRODICTION RESULTS (Known Ground Truth)")
        print("-" * 60)
        print(f"Retrodictions collected: {len(retrodict_results)}")
        if retrodict_avg_brier is not None:
            print(f"Average Brier (binary retrodictions): {retrodict_avg_brier:.4f}")

        for r in retrodict_results:
            title = r.question_title[:50] + "..." if len(r.question_title) > 50 else r.question_title
            print(f"\n  [{r.post_id}] {title}")
            print(f"    Type: {r.question_type}, Retrodict date: {r.retrodict_date}")
            if r.forecasted_probability is not None:
                print(f"    Forecast: {r.forecasted_probability:.0%}", end="")
            elif r.forecasted_median is not None:
                print(f"    Forecast: median={r.forecasted_median}", end="")
            if r.actual_value is not None:
                print(f"  |  Actual: {r.actual_value}", end="")
            if r.brier_score is not None:
                print(f"  |  Brier: {r.brier_score:.4f}", end="")
            elif r.score is not None:
                print(f"  |  {r.score_name or 'Score'}: {r.score:.4f}", end="")
            if r.within_ci is not None:
                print(f"  |  Within CI: {'Yes' if r.within_ci else 'No'}", end="")
            print()

    print(f"\nMetrics saved to: {output_file}")


if __name__ == "__main__":
    app()
