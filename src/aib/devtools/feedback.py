"""Collect feedback data from resolved forecasts and community prediction comparisons.

Fetches resolved questions from Metaculus, matches them to our past forecasts,
computes accuracy metrics (Brier score, log loss), and compares our forecasts
to community predictions as an early calibration signal.
"""

import asyncio
import json
import logging
import math
from datetime import datetime
from pathlib import Path
from typing import Annotated, TypedDict

import sh
import typer
from pydantic import BaseModel

from aib.agent.history import (
    FORECASTS_BASE_PATH,
    SavedForecast,
    load_past_forecasts,
    load_retrodict_forecasts,
)
from aib.clients.metaculus import AsyncMetaculusClient, get_client
from metaculus import ApiFilter, BinaryQuestion, MetaculusQuestion

app = typer.Typer(no_args_is_help=True)
logger = logging.getLogger(__name__)

FEEDBACK_BASE_PATH = Path("./notes/feedback_loop")

TOURNAMENTS = {
    "spring-aib-2026": 32916,
    "fall-aib-2025": "fall-aib-2025",
    "metaculus-cup": 32921,
}

CP_CACHE_TTL_HOURS = 6


def get_current_branch() -> str:
    """Get the current git branch name."""
    git = sh.Command("git")
    try:
        return str(git("branch", "--show-current")).strip() or "main"
    except sh.ErrorReturnCode:
        return "main"


def get_feedback_path() -> Path:
    return FEEDBACK_BASE_PATH / get_current_branch()


def get_last_run_file() -> Path:
    return get_feedback_path() / "last_run.json"


def get_state_file() -> Path:
    return get_feedback_path() / "feedback_state.json"


class AnalyzedItem(BaseModel):
    post_id: int
    timestamp: str
    item_type: str
    analysis_session: str


class CachedCP(BaseModel):
    cp: float
    fetched_at: str
    question_status: str


class FeedbackState(BaseModel):
    last_analysis: str | None = None
    last_collection: str | None = None
    analyzed_items: list[AnalyzedItem] = []
    cp_cache: dict[str, CachedCP] = {}
    changes_log: list[dict[str, str]] = []


class ForecastResult(BaseModel):
    question_id: int
    question_title: str
    question_type: str
    forecast_timestamp: str
    agent_version: str | None = None
    forecasted_probability: float | None = None
    forecasted_median: float | None = None
    forecasted_percentiles: dict[int, float] | None = None
    community_prediction: float | None = None
    cp_divergence: float | None = None
    resolution: bool | float | str | None = None
    resolution_time: datetime | None = None
    brier_score: float | None = None
    log_score: float | None = None


class CPComparison(BaseModel):
    question_id: int
    question_title: str
    question_type: str
    forecast_timestamp: str
    agent_version: str | None = None
    our_probability: float
    community_prediction: float
    divergence: float
    question_status: str


class RetrodictResult(BaseModel):
    post_id: int
    question_title: str
    question_type: str
    retrodict_date: str | None = None
    forecast_timestamp: str
    agent_version: str | None = None
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
    cp_comparisons: list[CPComparison] = []
    avg_cp_divergence: float | None = None
    cp_comparison_count: int = 0
    retrodict_results: list[RetrodictResult] = []
    retrodict_count: int = 0
    retrodict_avg_brier: float | None = None


def compute_brier_score(probability: float, resolved_true: bool) -> float:
    outcome = 1.0 if resolved_true else 0.0
    return (probability - outcome) ** 2


def compute_log_score(probability: float, resolved_true: bool) -> float:
    p = max(0.001, min(0.999, probability))
    if resolved_true:
        return -math.log(p)
    else:
        return -math.log(1 - p)


def compute_calibration_buckets(
    results: list[ForecastResult],
) -> dict[str, dict[str, float]]:
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

    output: dict[str, dict[str, float]] = {}
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
    res = question.resolution_string
    if res is None:
        return None

    res_lower = res.lower().strip()
    if res_lower == "yes":
        return True
    if res_lower == "no":
        return False
    if res_lower in ("ambiguous", "annulled"):
        return res_lower

    try:
        return float(res)
    except ValueError:
        pass

    return res


async def fetch_resolved_questions(
    tournament_ids: list[str | int],
    since: datetime | None = None,
    client: AsyncMetaculusClient | None = None,
) -> list[MetaculusQuestion]:
    all_questions: list[MetaculusQuestion] = []
    if client is None:
        client = get_client()

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
        except (OSError, ValueError) as e:
            logger.warning("Failed to fetch from tournament %s: %s", tournament_id, e)

    return all_questions


async def fetch_cp_for_forecasts(
    client: AsyncMetaculusClient,
    state: FeedbackState,
) -> list[CPComparison]:
    comparisons: list[CPComparison] = []

    if not FORECASTS_BASE_PATH.exists():
        return comparisons

    post_ids = [
        int(d.name)
        for d in FORECASTS_BASE_PATH.iterdir()
        if d.is_dir() and d.name.isdigit()
    ]

    now = datetime.now()
    ttl_cutoff = now.timestamp() - CP_CACHE_TTL_HOURS * 3600
    fetched_count = 0
    cached_count = 0

    for post_id in post_ids:
        forecasts = load_past_forecasts(post_id)
        if not forecasts:
            continue

        latest_forecast = forecasts[-1]
        if (
            latest_forecast.question_type != "binary"
            or latest_forecast.probability is None
        ):
            continue

        cache_key = str(post_id)
        cached = state.cp_cache.get(cache_key)
        if cached:
            cached_ts = datetime.fromisoformat(cached.fetched_at).timestamp()
            if cached_ts > ttl_cutoff:
                divergence = latest_forecast.probability - cached.cp
                comparisons.append(
                    CPComparison(
                        question_id=post_id,
                        question_title=latest_forecast.question_title[:80],
                        question_type=latest_forecast.question_type,
                        forecast_timestamp=latest_forecast.timestamp,
                        agent_version=latest_forecast.agent_version,
                        our_probability=latest_forecast.probability,
                        community_prediction=cached.cp,
                        divergence=divergence,
                        question_status=cached.question_status,
                    )
                )
                cached_count += 1
                continue

        if fetched_count > 0:
            await asyncio.sleep(2.0)
        if fetched_count > 0 and fetched_count % 5 == 0:
            await asyncio.sleep(5.0)

        try:
            question = await client.get_question_by_post_id(post_id, include_text=False)
            if isinstance(question, list):
                question = question[0]

            cp: float | None = None
            if isinstance(question, BinaryQuestion):
                cp = question.community_prediction_at_access_time

            if cp is None:
                continue

            q_status = question.status.value if question.status else "unknown"
            state.cp_cache[cache_key] = CachedCP(
                cp=cp,
                fetched_at=now.isoformat(),
                question_status=q_status,
            )

            divergence = latest_forecast.probability - cp
            comparisons.append(
                CPComparison(
                    question_id=post_id,
                    question_title=latest_forecast.question_title[:80],
                    question_type=latest_forecast.question_type,
                    forecast_timestamp=latest_forecast.timestamp,
                    agent_version=latest_forecast.agent_version,
                    our_probability=latest_forecast.probability,
                    community_prediction=cp,
                    divergence=divergence,
                    question_status=q_status,
                )
            )
            fetched_count += 1
        except (OSError, ValueError, AttributeError) as e:
            logger.debug("Failed to fetch CP for post %d: %s", post_id, e)

    logger.info(
        "CP comparison: %d cached, %d fetched from API", cached_count, fetched_count
    )
    return comparisons


def match_forecasts_to_resolutions(
    questions: list[MetaculusQuestion],
) -> list[ForecastResult]:
    results: list[ForecastResult] = []

    for question in questions:
        question_id = question.id_of_post
        if question_id is None:
            continue

        past_forecasts = load_past_forecasts(question_id)
        if not past_forecasts:
            continue

        resolution = get_resolution_value(question)
        if resolution is None:
            continue

        forecast = past_forecasts[-1]

        if question.actual_resolution_time:
            try:
                forecast_dt = datetime.strptime(forecast.timestamp, "%Y%m%d_%H%M%S")
                resolution_dt = question.actual_resolution_time.replace(tzinfo=None)
                if forecast_dt > resolution_dt:
                    pre_resolution = [
                        f
                        for f in past_forecasts
                        if datetime.strptime(f.timestamp, "%Y%m%d_%H%M%S")
                        < resolution_dt
                    ]
                    if not pre_resolution:
                        continue
                    forecast = pre_resolution[-1]
            except ValueError:
                pass

        result = ForecastResult(
            question_id=question_id,
            question_title=question.question_text[:100],
            question_type=forecast.question_type,
            forecast_timestamp=forecast.timestamp,
            agent_version=forecast.agent_version,
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
                result.log_score = compute_log_score(forecast.probability, resolution)

        results.append(result)

    return results


def collect_retrodict_results() -> list[RetrodictResult]:
    forecasts = load_retrodict_forecasts()

    latest: dict[tuple[int, str], SavedForecast] = {}
    for f in forecasts:
        if not f.retrodict_date:
            continue
        key = (f.post_id or 0, f.retrodict_date)
        existing = latest.get(key)
        if existing is None or f.timestamp > existing.timestamp:
            latest[key] = f

    results: list[RetrodictResult] = []
    for f in latest.values():
        result = RetrodictResult(
            post_id=f.post_id or 0,
            question_title=f.question_title[:80],
            question_type=f.question_type,
            retrodict_date=f.retrodict_date or "",
            forecast_timestamp=f.timestamp,
            agent_version=f.agent_version,
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
            resolved_true = str(f.comparison.actual_value).lower() in (
                "true",
                "yes",
                "1",
                "1.0",
            )
            result.brier_score = compute_brier_score(f.probability, resolved_true)

        results.append(result)

    return results


def load_feedback_state() -> FeedbackState:
    state_file = get_state_file()
    if state_file.exists():
        return FeedbackState.model_validate_json(state_file.read_text())

    last_run_file = get_last_run_file()
    if last_run_file.exists():
        data = json.loads(last_run_file.read_text())
        return FeedbackState(last_collection=data.get("last_collection"))

    return FeedbackState()


def save_feedback_state(state: FeedbackState) -> None:
    feedback_path = get_feedback_path()
    feedback_path.mkdir(parents=True, exist_ok=True)
    get_state_file().write_text(state.model_dump_json(indent=2))


class LastRunData(TypedDict, total=False):
    last_collection: str
    last_metrics_file: str
    tournaments: list[str]


def load_last_run() -> LastRunData:
    last_run_file = get_last_run_file()
    if last_run_file.exists():
        return json.loads(last_run_file.read_text())
    return LastRunData()


def save_last_run(data: LastRunData) -> None:
    feedback_path = get_feedback_path()
    feedback_path.mkdir(parents=True, exist_ok=True)
    get_last_run_file().write_text(json.dumps(data, indent=2, default=str))


@app.command("collect")
def collect(
    tournament: Annotated[
        list[str] | None,
        typer.Option("--tournament", "-t", help="Tournament ID or slug"),
    ] = None,
    since: Annotated[
        str | None,
        typer.Option(
            "--since",
            "-s",
            help="Only fetch questions resolved after this date (YYYY-MM-DD)",
        ),
    ] = None,
    all_time: Annotated[
        bool,
        typer.Option("--all-time", help="Ignore last run timestamp"),
    ] = False,
    include_retrodict: Annotated[
        bool,
        typer.Option("--include-retrodict", help="Include retrodicted forecasts"),
    ] = False,
    new_only: Annotated[
        bool,
        typer.Option(
            "--new-only/--no-new-only", help="Only show new items since last analysis"
        ),
    ] = True,
    version: Annotated[
        str | None,
        typer.Option(
            "--version",
            "-v",
            help="Filter results to a specific agent version (e.g., 1.1.0).",
        ),
    ] = None,
) -> None:
    """Collect feedback metrics from resolved forecasts."""
    asyncio.run(
        _main_async(tournament, since, all_time, include_retrodict, new_only, version)
    )


async def _main_async(
    tournament: list[str] | None,
    since: str | None,
    all_time: bool,
    include_retrodict: bool = False,
    new_only: bool = True,
    version: str | None = None,
) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    state = load_feedback_state()

    tournament_ids: list[str | int] = []
    if tournament:
        for t in tournament:
            if t in TOURNAMENTS:
                tournament_ids.append(TOURNAMENTS[t])
            else:
                try:
                    tournament_ids.append(int(t))
                except ValueError:
                    tournament_ids.append(t)
    else:
        tournament_ids = [TOURNAMENTS["spring-aib-2026"]]

    tournament_names = tournament if tournament else ["spring-aib-2026"]

    since_dt: datetime | None = None
    if not all_time:
        if since:
            since_dt = datetime.fromisoformat(since)
        else:
            last_run = load_last_run()
            last_collection = last_run.get("last_collection")
            if last_collection:
                since_dt = datetime.fromisoformat(last_collection)

    logger.info(
        "Collecting feedback for tournaments %s since %s",
        tournament_names,
        since_dt.isoformat() if since_dt else "all time",
    )

    client = get_client()
    questions = await fetch_resolved_questions(tournament_ids, since_dt, client)
    logger.info("Total resolved questions found: %d", len(questions))
    cp_comparisons = await fetch_cp_for_forecasts(client, state)
    logger.info("Fetched CP for %d forecasts", len(cp_comparisons))

    results = match_forecasts_to_resolutions(questions)
    logger.info("Matched %d forecasts to resolutions", len(results))

    retrodict_results: list[RetrodictResult] = []
    if include_retrodict:
        retrodict_results = collect_retrodict_results()
        logger.info("Collected %d retrodictions", len(retrodict_results))

    already_analyzed = {
        (item.post_id, item.timestamp, item.item_type) for item in state.analyzed_items
    }

    if new_only and state.last_analysis:
        prev_count = len(results)
        results = [
            r
            for r in results
            if (r.question_id, r.forecast_timestamp, "forecast") not in already_analyzed
        ]
        if prev_count != len(results):
            logger.info(
                "Filtered forecasts: %d total -> %d new", prev_count, len(results)
            )

        prev_retro = len(retrodict_results)
        retrodict_results = [
            r
            for r in retrodict_results
            if (r.post_id, r.forecast_timestamp, "retrodict") not in already_analyzed
        ]
        if prev_retro != len(retrodict_results):
            logger.info(
                "Filtered retrodictions: %d total -> %d new",
                prev_retro,
                len(retrodict_results),
            )

    if version:
        results = [r for r in results if r.agent_version == version]
        retrodict_results = [r for r in retrodict_results if r.agent_version == version]
        cp_comparisons = [c for c in cp_comparisons if c.agent_version == version]
        logger.info(
            "Filtered to version %s: %d forecasts, %d retrodictions, %d CP comparisons",
            version,
            len(results),
            len(retrodict_results),
            len(cp_comparisons),
        )

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

    retrodict_avg_brier = None
    retrodict_brier_scores = [
        r.brier_score for r in retrodict_results if r.brier_score is not None
    ]
    if retrodict_brier_scores:
        retrodict_avg_brier = sum(retrodict_brier_scores) / len(retrodict_brier_scores)

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
        retrodict_avg_brier=round(retrodict_avg_brier, 4)
        if retrodict_avg_brier
        else None,
    )

    feedback_path = get_feedback_path()
    feedback_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = feedback_path / f"{timestamp}_metrics.json"
    output_file.write_text(metrics.model_dump_json(indent=2))

    save_last_run(
        {
            "last_collection": datetime.now().isoformat(),
            "last_metrics_file": str(output_file),
            "tournaments": tournament_names,
        }
    )

    now_iso = datetime.now().isoformat()
    for r in results:
        state.analyzed_items.append(
            AnalyzedItem(
                post_id=r.question_id,
                timestamp=r.forecast_timestamp,
                item_type="forecast",
                analysis_session=now_iso,
            )
        )
    for r in retrodict_results:
        state.analyzed_items.append(
            AnalyzedItem(
                post_id=r.post_id,
                timestamp=r.forecast_timestamp,
                item_type="retrodict",
                analysis_session=now_iso,
            )
        )
    state.last_analysis = now_iso
    state.last_collection = now_iso
    save_feedback_state(state)

    print("\n" + "=" * 60)
    print("FEEDBACK COLLECTION SUMMARY")
    print("=" * 60)
    print(f"Tournaments: {', '.join(tournament_names)}")
    if version:
        print(f"Version filter: {version}")
    if new_only and state.last_analysis:
        print(f"Mode: incremental (new since {state.last_analysis[:10]})")
        print(f"Previously analyzed: {len(already_analyzed)} items")
    else:
        print("Mode: all-time")
    print(f"Resolved questions: {len(questions)}")
    print(f"Questions with our forecasts: {metrics.questions_with_forecasts}")
    print(f"Binary forecasts evaluated: {len(binary_results)}")
    print(f"Numeric forecasts: {len(numeric_results)}")

    if avg_brier is not None:
        print(f"\nAverage Brier Score: {avg_brier:.4f}")
        print(f"Average Log Score: {avg_log:.4f}")

    # Show per-version breakdown when no --version filter
    if not version:
        all_scored = [r for r in results if r.brier_score is not None]
        all_retro_scored = [r for r in retrodict_results if r.brier_score is not None]
        scored_items = all_scored + [
            ForecastResult(
                question_id=r.post_id,
                question_title=r.question_title,
                question_type=r.question_type,
                forecast_timestamp=r.forecast_timestamp,
                agent_version=r.agent_version,
                brier_score=r.brier_score,
            )
            for r in all_retro_scored
        ]
        versions: dict[str, list[float]] = {}
        for item in scored_items:
            v = item.agent_version or "(unknown)"
            if item.brier_score is not None:
                versions.setdefault(v, []).append(item.brier_score)
        if len(versions) > 1:
            print("\nAverage Brier by version:")
            for v in sorted(versions.keys()):
                scores = versions[v]
                avg = sum(scores) / len(scores)
                print(f"  v{v}: {avg:.4f} (n={len(scores)})")

    if calibration:
        print("\nCalibration (forecasted -> actual resolution rate):")
        for bucket, data in calibration.items():
            print(
                f"  {bucket}: {data['avg_forecast']:.0%} -> {data['resolution_rate']:.0%} (n={data['count']})"
            )

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
            print(f"  - [{q.id_of_post}] {title} -> {res_str}")

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

        large_divergences = [c for c in cp_comparisons if abs(c.divergence) > 0.15]
        if large_divergences:
            print(f"\nLarge divergences (>15pp): {len(large_divergences)}")
            large_divergences.sort(key=lambda c: abs(c.divergence), reverse=True)
            for c in large_divergences[:10]:
                title = (
                    c.question_title[:50] + "..."
                    if len(c.question_title) > 50
                    else c.question_title
                )
                print(
                    f"  [{c.question_id}] {c.our_probability:.0%} vs CP {c.community_prediction:.0%} ({c.divergence:+.0%})"
                )
                print(f"      {title}")

        higher_count = sum(1 for c in cp_comparisons if c.divergence > 0.02)
        lower_count = sum(1 for c in cp_comparisons if c.divergence < -0.02)
        if higher_count + lower_count > 0:
            print(
                f"\nBias check: {higher_count} forecasts higher than CP, {lower_count} lower"
            )

    if retrodict_results:
        print("\n" + "-" * 60)
        print("RETRODICTION RESULTS (Known Ground Truth)")
        print("-" * 60)
        print(f"Retrodictions collected: {len(retrodict_results)}")
        if retrodict_avg_brier is not None:
            print(f"Average Brier (binary retrodictions): {retrodict_avg_brier:.4f}")

        for r in retrodict_results:
            title = (
                r.question_title[:50] + "..."
                if len(r.question_title) > 50
                else r.question_title
            )
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
