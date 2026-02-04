"""Forecast history storage and retrieval.

Provides functions to save forecasts to disk and load past forecasts
for a given question. Used for historical learning and calibration.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from aib.agent.models import TokenUsage

if TYPE_CHECKING:
    from aib.agent.models import ForecastOutput

logger = logging.getLogger(__name__)

# Base path for forecast storage
FORECASTS_BASE_PATH = Path("./notes/forecasts")


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
    resolution: str | None = None  # "yes", "no", "ambiguous", or None if unresolved
    submitted_at: str | None = None  # ISO timestamp when submitted to Metaculus
    comment_posted_at: str | None = None  # ISO timestamp when comment was posted
    # Programmatic tracking fields
    tool_metrics: dict[str, Any] | None = None  # Tool call counts, durations, errors
    token_usage: TokenUsage | None = None  # Token usage: input, output, cache
    log_path: str | None = None  # Path to reasoning log file
    # Cadence tracking fields (when question published vs when we forecast)
    question_published_at: str | None = None  # ISO timestamp when question was published
    question_close_time: str | None = None  # ISO timestamp when question closes
    question_scheduled_resolve_time: str | None = None  # ISO timestamp when resolution expected


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
) -> Path:
    """Save a forecast to the history storage.

    Args:
        question_id: Metaculus question ID (for submission API).
        post_id: Metaculus post ID (for URLs, directory structure).
        question_title: Title of the question.
        question_type: Type of question (binary, numeric, multiple_choice).
        summary: Forecast summary/reasoning.
        factors: List of evidence factors.
        probability: For binary questions, the final probability.
        logit: For binary questions, the logit value.
        probabilities: For multiple choice, mapping of option to probability.
        median: For numeric, the median estimate.
        confidence_interval: For numeric, the (low, high) 90% CI.
        percentiles: For numeric, percentile estimates.
        tool_metrics: Programmatic tracking of tool calls, durations, errors.
        token_usage: Token usage stats (input, output, cache tokens).
        log_path: Path to the reasoning log file in logs/.
        question_published_at: ISO timestamp when question was published on Metaculus.
        question_close_time: ISO timestamp when question closes for forecasting.
        question_scheduled_resolve_time: ISO timestamp when question is expected to resolve.

    Returns:
        Path to the saved forecast file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create directory by post_id (what users see in URLs)
    question_dir = FORECASTS_BASE_PATH / str(post_id)
    question_dir.mkdir(parents=True, exist_ok=True)

    # Build forecast data
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
    )

    # Save to file
    filepath = question_dir / f"{timestamp}.json"
    filepath.write_text(forecast.model_dump_json(indent=2), encoding="utf-8")

    logger.info("Saved forecast for question %d to %s", question_id, filepath)
    return filepath


def load_past_forecasts(post_id: int) -> list[SavedForecast]:
    """Load all past forecasts for a question.

    Args:
        post_id: Metaculus post ID (directory structure uses post ID).

    Returns:
        List of SavedForecast objects, sorted by timestamp (oldest first).
    """
    question_dir = FORECASTS_BASE_PATH / str(post_id)

    if not question_dir.exists():
        return []

    forecasts = []
    for filepath in sorted(question_dir.glob("*.json")):
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            forecasts.append(SavedForecast.model_validate(data))
        except Exception as e:
            logger.warning("Failed to load forecast from %s: %s", filepath, e)

    return forecasts


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
    question_dir = FORECASTS_BASE_PATH / str(post_id)

    if not question_dir.exists():
        logger.warning("No forecasts found for post %d", post_id)
        return False

    # Find the latest forecast file
    forecast_files = sorted(question_dir.glob("*.json"))
    if not forecast_files:
        return False

    latest_file = forecast_files[-1]

    try:
        data = json.loads(latest_file.read_text(encoding="utf-8"))
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data["submitted_at"] = timestamp
        latest_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        logger.info("Marked forecast for post %d as submitted at %s", post_id, timestamp)
        return True
    except Exception as e:
        logger.warning("Failed to mark submission for post %d: %s", post_id, e)
        return False


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
    question_dir = FORECASTS_BASE_PATH / str(post_id)

    if not question_dir.exists():
        logger.warning("No forecasts found for post %d", post_id)
        return False

    forecast_files = sorted(question_dir.glob("*.json"))
    if not forecast_files:
        return False

    latest_file = forecast_files[-1]

    try:
        data = json.loads(latest_file.read_text(encoding="utf-8"))
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data["comment_posted_at"] = timestamp
        latest_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        logger.info("Marked comment posted for post %d at %s", post_id, timestamp)
        return True
    except Exception as e:
        logger.warning("Failed to mark comment for post %d: %s", post_id, e)
        return False


def update_resolution(post_id: int, resolution: str) -> None:
    """Update the resolution status for all forecasts of a question.

    Args:
        post_id: Metaculus post ID.
        resolution: Resolution status ("yes", "no", "ambiguous").
    """
    question_dir = FORECASTS_BASE_PATH / str(post_id)

    if not question_dir.exists():
        logger.warning("No forecasts found for post %d", post_id)
        return

    for filepath in question_dir.glob("*.json"):
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            data["resolution"] = resolution
            filepath.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning("Failed to update resolution in %s: %s", filepath, e)

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
        if bounds and bounds.get("range_min") is not None and bounds.get("range_max") is not None:
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
                logger.warning(
                    "Failed to regenerate CDF for post %d: %s", post_id, e
                )
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
        lines.append(f"### {f.timestamp}")

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
