"""Forecast history storage and retrieval.

Provides functions to save forecasts to disk and load past forecasts
for a given question. Used for historical learning and calibration.
"""

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

import sh
from pydantic import BaseModel, Field

from aib.agent.models import TokenUsage
from aib.paths import (
    forecasts_dir,
    find_latest_forecast_file,
    iter_forecast_dirs,
    iter_forecast_files,
    iter_retrodict_dirs,
    iter_retrodict_files,
    iter_session_dirs,
    iter_trace_log_files,
    parse_timestamp,
    retrodict_dir,
)
from aib.retrodict_context import effective_now
from aib.version import AGENT_VERSION

if TYPE_CHECKING:
    from aib.agent.models import ForecastOutput

logger = logging.getLogger(__name__)


class RetrodictComparison(BaseModel):
    """Comparison between retrodict prediction and actual resolution."""

    actual_value: float | str | None = None
    predicted_value: float | str | None = None
    difference: float | None = None
    difference_pct: float | None = None
    within_ci: bool | None = None
    score: float | None = None
    score_name: str | None = None


def commit_forecast(post_id: int, question_title: str) -> bool:
    """Stage and commit forecast, meta, and log files for a question.

    Args:
        post_id: Metaculus post ID.
        question_title: Question title for the commit message.

    Returns:
        True if a commit was created, False if nothing to commit.
    """
    paths_to_stage: list[str] = []

    for d in iter_forecast_dirs(post_id):
        paths_to_stage.append(str(d))

    for d in iter_retrodict_dirs(post_id):
        paths_to_stage.append(str(d))

    for d in iter_session_dirs(post_id):
        paths_to_stage.append(str(d))

    for f in iter_trace_log_files(post_id):
        paths_to_stage.append(str(f))

    if not paths_to_stage:
        logger.warning("No forecast files found to commit for post %d", post_id)
        return False

    try:
        env = {**os.environ, "GIT_PAGER": ""}
        git = sh.Command("git")

        for path in paths_to_stage:
            try:
                git.add(path, _tty_out=False, _env=env)
            except sh.ErrorReturnCode:
                logger.debug("Skipping git add for %s (ignored or missing)", path)

        diff = str(
            git.diff("--cached", "--name-only", _tty_out=False, _env=env)
        ).strip()
        if not diff:
            logger.info("Nothing to commit for post %d (already committed?)", post_id)
            return False

        slug = question_title[:50].strip().rstrip(".")
        git.commit("-m", f"data(forecasts): {slug}", _tty_out=False, _env=env)
        logger.info("Committed forecast for post %d", post_id)
        return True
    except Exception as e:
        logger.warning("Git commit failed for post %d: %s", post_id, e)
        return False


class SavedForecast(BaseModel):
    """A saved forecast with metadata."""

    question_id: int  # Actual question ID (for submission API)
    post_id: int | None = None  # Post ID (for URLs, legacy: equals question_id if None)
    question_title: str
    question_type: str
    timestamp: str
    probability: float | None = None
    logit: float | None = None
    probabilities: dict[str, float] | None = None
    median: float | None = None
    confidence_interval: tuple[float, float] | None = None
    percentiles: dict[int, float] | None = None
    summary: str
    factors: list[dict[str, Any]]
    resolution: str | float | None = None
    submitted_at: str | None = None  # ISO timestamp when submitted to Metaculus
    comment_posted_at: str | None = None  # ISO timestamp when comment was posted
    # Programmatic tracking fields
    tool_metrics: dict[str, Any] | None = None  # Tool call counts, durations, errors
    token_usage: TokenUsage | None = None  # Token usage: input, output, cache
    log_path: str | None = None  # Path to reasoning log file
    # Cadence tracking fields (when question published vs when we forecast)
    question_published_at: str | None = (
        None  # ISO timestamp when question was published
    )
    question_close_time: str | None = None  # ISO timestamp when question closes
    question_scheduled_resolve_time: str | None = (
        None  # ISO timestamp when resolution expected
    )
    reasoning: str = ""
    sources_consulted: list[str] = Field(default_factory=list)
    agent_version: str | None = None
    # Retrodict tracking
    retrodict_date: str | None = None  # YYYY-MM-DD cutoff date if retrodicted
    # Retrodict comparison (actual vs predicted)
    comparison: RetrodictComparison | None = None


def save_forecast(
    question_id: int,
    post_id: int,
    question_title: str,
    question_type: str,
    summary: str,
    factors: list[dict[str, Any]],
    *,
    probability: float | None = None,
    logit: float | None = None,
    probabilities: dict[str, float] | None = None,
    median: float | None = None,
    confidence_interval: tuple[float, float] | None = None,
    percentiles: dict[int, float] | None = None,
    tool_metrics: dict[str, Any] | None = None,
    token_usage: TokenUsage | None = None,
    log_path: str | None = None,
    question_published_at: str | None = None,
    question_close_time: str | None = None,
    question_scheduled_resolve_time: str | None = None,
    reasoning: str = "",
    sources_consulted: list[str] | None = None,
    retrodict_date: str | None = None,
) -> Path:
    """Save a forecast to disk.

    When retrodict_date is set, saves to the retrodict directory with the
    cutoff date in the filename. Otherwise saves to the versioned traces
    directory.

    Returns:
        Path to the saved forecast file.
    """
    if retrodict_date:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        question_dir = retrodict_dir() / str(post_id)
    else:
        timestamp = effective_now().strftime("%Y%m%d_%H%M%S")
        question_dir = forecasts_dir() / str(post_id)

    question_dir.mkdir(parents=True, exist_ok=True)

    forecast = SavedForecast(
        question_id=question_id,
        post_id=post_id,
        question_title=question_title,
        question_type=question_type,
        timestamp=timestamp,
        probability=probability,
        logit=logit,
        probabilities=probabilities,
        median=median,
        confidence_interval=confidence_interval,
        percentiles=percentiles,
        summary=summary,
        factors=[f if isinstance(f, dict) else f.model_dump() for f in factors],
        tool_metrics=tool_metrics,
        token_usage=token_usage,
        log_path=log_path,
        question_published_at=question_published_at,
        question_close_time=question_close_time,
        question_scheduled_resolve_time=question_scheduled_resolve_time,
        reasoning=reasoning,
        sources_consulted=sources_consulted or [],
        retrodict_date=retrodict_date,
        agent_version=AGENT_VERSION,
    )

    filename = (
        f"{retrodict_date}_{timestamp}.json" if retrodict_date else f"{timestamp}.json"
    )
    filepath = question_dir / filename
    filepath.write_text(forecast.model_dump_json(indent=2), encoding="utf-8")

    logger.info("Saved forecast for question %d to %s", question_id, filepath)
    return filepath


def _update_forecast_json(
    filepath: Path, **updates: str | float | object | None
) -> bool:
    """Update a forecast JSON file through Pydantic validation.

    Reads the file, validates through SavedForecast, applies updates via
    model_copy, and writes back. Returns True if the file was modified.
    """
    data = json.loads(filepath.read_text(encoding="utf-8"))
    forecast = SavedForecast.model_validate(data)
    updated = forecast.model_copy(update=updates)
    if updated == forecast:
        return False
    filepath.write_text(updated.model_dump_json(indent=2), encoding="utf-8")
    return True


def update_forecast_file(filepath: Path, resolution: str | float) -> bool:
    """Update a single forecast file with resolution data."""
    return _update_forecast_json(filepath, resolution=resolution)


def update_retrodict_comparison(
    post_id: int,
    comparison: RetrodictComparison,
    resolution: str | None = None,
) -> bool:
    """Update the latest retrodict forecast with comparison data.

    Args:
        post_id: Metaculus post ID.
        comparison: Comparison metrics between prediction and actual.
        resolution: Resolution string (e.g., "yes", "no", or numeric value as string).

    Returns:
        True if successfully updated, False otherwise.
    """
    latest_file: Path | None = None
    latest_ts: datetime | None = None
    for f in sorted(iter_retrodict_files(post_id)):
        try:
            ts = parse_timestamp(f.name)
        except ValueError:
            continue
        if latest_ts is None or ts > latest_ts:
            latest_file = f
            latest_ts = ts

    if latest_file is None:
        logger.warning("No retrodict forecasts found for post %d", post_id)
        return False

    updates: dict[str, RetrodictComparison | str | None] = {"comparison": comparison}
    if resolution is not None:
        updates["resolution"] = resolution

    try:
        result = _update_forecast_json(latest_file, **updates)
        if result:
            logger.info("Updated retrodict comparison for post %d", post_id)
        return result
    except Exception as e:
        logger.warning(
            "Failed to update retrodict comparison for post %d: %s", post_id, e
        )
        return False


def load_past_forecasts(post_id: int) -> list[SavedForecast]:
    """Load all past forecasts for a question.

    Args:
        post_id: Metaculus post ID (directory structure uses post ID).

    Returns:
        List of SavedForecast objects, sorted by timestamp (oldest first).
    """
    forecasts = []
    for filepath in sorted(iter_forecast_files(post_id)):
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            forecasts.append(SavedForecast.model_validate(data))
        except Exception as e:
            logger.warning("Failed to load forecast from %s: %s", filepath, e)

    return forecasts


def load_retrodict_forecasts(post_id: int | None = None) -> list[SavedForecast]:
    """Load retrodicted forecasts, optionally filtered by post ID.

    Args:
        post_id: If provided, load only retrodictions for this post ID.
                 If None, load all retrodictions across all post IDs.

    Returns:
        List of SavedForecast objects with retrodict_date set, sorted by timestamp.
    """
    forecasts = []
    for filepath in sorted(iter_retrodict_files(post_id)):
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            forecasts.append(SavedForecast.model_validate(data))
        except Exception as e:
            logger.warning("Failed to load retrodict from %s: %s", filepath, e)

    return sorted(forecasts, key=lambda f: parse_timestamp(f.timestamp))


def get_latest_forecast(post_id: int) -> SavedForecast | None:
    """Get the most recent forecast for a question.

    Args:
        post_id: Metaculus post ID.

    Returns:
        The most recent SavedForecast, or None if no forecasts exist.
    """
    forecasts = load_past_forecasts(post_id)
    return forecasts[-1] if forecasts else None


def mark_submitted(post_id: int, timestamp: str | None = None) -> bool:
    """Mark the latest forecast for a question as submitted.

    Args:
        post_id: Metaculus post ID.
        timestamp: ISO timestamp of submission. If None, uses current time.

    Returns:
        True if a forecast was marked, False if no forecast exists.
    """
    latest_file = find_latest_forecast_file(post_id)
    if latest_file is None:
        logger.warning("No forecasts found for post %d", post_id)
        return False

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result = _update_forecast_json(latest_file, submitted_at=timestamp)
    if result:
        logger.info(
            "Marked forecast for post %d as submitted at %s", post_id, timestamp
        )
    return result


def is_submitted(post_id: int) -> bool:
    """Check if the latest forecast for a question has been submitted.

    Args:
        post_id: Metaculus post ID.

    Returns:
        True if the latest forecast has a submitted_at timestamp.
    """
    latest = get_latest_forecast(post_id)
    return latest is not None and latest.submitted_at is not None


def has_comment(post_id: int) -> bool:
    """Check if the latest forecast for a question has a comment posted.

    Args:
        post_id: Metaculus post ID.

    Returns:
        True if the latest forecast has a comment_posted_at timestamp.
    """
    latest = get_latest_forecast(post_id)
    return latest is not None and latest.comment_posted_at is not None


def mark_comment_posted(post_id: int, timestamp: str | None = None) -> bool:
    """Mark the latest forecast for a question as having a comment posted.

    Args:
        post_id: Metaculus post ID.
        timestamp: ISO timestamp of comment posting. If None, uses current time.

    Returns:
        True if a forecast was marked, False if no forecast exists.
    """
    latest_file = find_latest_forecast_file(post_id)
    if latest_file is None:
        logger.warning("No forecasts found for post %d", post_id)
        return False

    if timestamp is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result = _update_forecast_json(latest_file, comment_posted_at=timestamp)
    if result:
        logger.info("Marked comment posted for post %d at %s", post_id, timestamp)
    return result


def update_resolution(post_id: int, resolution: str) -> None:
    """Update the resolution status for all forecasts of a question.

    Args:
        post_id: Metaculus post ID.
        resolution: Resolution status ("yes", "no", "ambiguous").
    """
    files = list(iter_forecast_files(post_id))
    if not files:
        logger.warning("No forecasts found for post %d", post_id)
        return

    for filepath in files:
        _update_forecast_json(filepath, resolution=resolution)

    logger.info(
        "Updated resolution to '%s' for all forecasts of post %d",
        resolution,
        post_id,
    )


async def _fetch_numeric_bounds(post_id: int) -> dict | None:
    """Fetch numeric bounds from Metaculus API for CDF generation.

    Args:
        post_id: Metaculus post ID.

    Returns:
        Dict with range_min, range_max, open_lower_bound, open_upper_bound,
        zero_point, and cdf_size. None if fetch fails or question is not numeric.
    """
    from metaculus import NumericQuestion

    from aib.clients.metaculus import get_client

    try:
        client = get_client()
        question = await client.get_question_by_post_id(post_id)

        # Handle case where multiple questions are returned (shouldn't happen)
        if isinstance(question, list):
            question = question[0]

        if not isinstance(question, NumericQuestion):
            logger.warning(
                "Question %d is not numeric (got %s)", post_id, type(question).__name__
            )
            return None

        return {
            "range_min": question.lower_bound,
            "range_max": question.upper_bound,
            "open_lower_bound": question.open_lower_bound,
            "open_upper_bound": question.open_upper_bound,
            "zero_point": question.zero_point,
            "cdf_size": question.cdf_size,
        }
    except Exception as e:
        logger.warning("Failed to fetch numeric bounds for post %d: %s", post_id, e)
        return None


def load_latest_for_submission(
    post_id: int, *, allow_resubmit: bool = False
) -> "ForecastOutput | None":
    """Load the latest forecast for submission (without re-running the agent).

    For numeric/discrete questions, this regenerates the CDF from percentiles
    by fetching the question bounds from Metaculus.

    Args:
        post_id: Metaculus post ID.
        allow_resubmit: If False (default), returns None for already-submitted
            forecasts. Set to True to load even if already submitted.

    Returns:
        ForecastOutput ready for submission, or None if no forecast exists
        or if already submitted (when allow_resubmit=False).
    """
    import asyncio

    # Import at runtime to avoid circular dependency issues
    from aib.agent import models
    from aib.agent.numeric import percentiles_to_cdf

    latest = get_latest_forecast(post_id)
    if latest is None:
        return None

    # Skip already-submitted forecasts unless explicitly allowed
    if not allow_resubmit and latest.submitted_at is not None:
        logger.info(
            "Skipping already-submitted forecast for post %d (submitted at %s)",
            post_id,
            latest.submitted_at,
        )
        return None

    # Convert SavedForecast to ForecastOutput
    # Note: For legacy forecasts where post_id is None, use question_id as post_id
    effective_post_id = (
        latest.post_id if latest.post_id is not None else latest.question_id
    )

    output = models.ForecastOutput(
        question_id=latest.question_id,
        post_id=effective_post_id,
        question_title=latest.question_title,
        question_type=latest.question_type,
        summary=latest.summary,
        factors=[models.Factor.model_validate(f) for f in latest.factors],
        probability=latest.probability,
        logit=latest.logit,
        probabilities=latest.probabilities,
        median=latest.median,
        confidence_interval=latest.confidence_interval,
        percentiles=latest.percentiles,
    )

    # For numeric/discrete questions with percentiles, regenerate CDF
    if latest.question_type in ("numeric", "discrete") and latest.percentiles:
        bounds = asyncio.run(_fetch_numeric_bounds(effective_post_id))
        if (
            bounds
            and bounds.get("range_min") is not None
            and bounds.get("range_max") is not None
        ):
            try:
                cdf_size = bounds.get("cdf_size", 201)
                output.cdf = percentiles_to_cdf(
                    latest.percentiles,
                    upper_bound=bounds["range_max"],
                    lower_bound=bounds["range_min"],
                    open_upper_bound=bounds.get("open_upper_bound", False),
                    open_lower_bound=bounds.get("open_lower_bound", False),
                    zero_point=bounds.get("zero_point"),
                    cdf_size=cdf_size,
                )
                output.cdf_size = cdf_size
                logger.info(
                    "Regenerated %d-point CDF for cached forecast of post %d",
                    len(output.cdf),
                    post_id,
                )
            except Exception as e:
                logger.warning("Failed to regenerate CDF for post %d: %s", post_id, e)
        else:
            logger.warning(
                "Could not fetch bounds for CDF regeneration (post %d)", post_id
            )

    return output


def format_history_for_context(forecasts: list[SavedForecast]) -> str:
    """Format past forecasts as context for the agent.

    Args:
        forecasts: List of past forecasts.

    Returns:
        Markdown-formatted summary of past forecasts.
    """
    if not forecasts:
        return ""

    lines = ["## Past Forecasts for This Question\n"]

    for f in forecasts:
        version_tag = f" (v{f.agent_version})" if f.agent_version else ""
        lines.append(f"### {f.timestamp}{version_tag}")

        if f.question_type == "binary" and f.probability is not None:
            lines.append(f"**Probability**: {f.probability:.1%}")
            if f.logit is not None:
                lines.append(f"**Logit**: {f.logit:+.2f}")
        elif f.question_type == "multiple_choice" and f.probabilities:
            lines.append("**Probabilities**:")
            for option, prob in f.probabilities.items():
                lines.append(f"  - {option}: {prob:.1%}")
        elif f.question_type in ("numeric", "discrete"):
            if f.median is not None:
                lines.append(f"**Median**: {f.median}")
            if f.confidence_interval:
                lines.append(
                    f"**90% CI**: [{f.confidence_interval[0]}, {f.confidence_interval[1]}]"
                )

        if f.resolution:
            lines.append(f"**Resolution**: {f.resolution}")

        lines.append(f"**Summary**: {f.summary[:200]}...")
        lines.append("")

    return "\n".join(lines)
