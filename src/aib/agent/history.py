"""Forecast history storage and retrieval.

Provides functions to save forecasts to disk and load past forecasts
for a given question. Used for historical learning and calibration.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel

logger = logging.getLogger(__name__)

# Base path for forecast storage
FORECASTS_BASE_PATH = Path("./notes/forecasts")


class SavedForecast(BaseModel):
    """A saved forecast with metadata."""

    question_id: int
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


def save_forecast(
    question_id: int,
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
) -> Path:
    """Save a forecast to the history storage.

    Args:
        question_id: Metaculus question/post ID.
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

    Returns:
        Path to the saved forecast file.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create question-specific directory
    question_dir = FORECASTS_BASE_PATH / str(question_id)
    question_dir.mkdir(parents=True, exist_ok=True)

    # Build forecast data
    forecast = SavedForecast(
        question_id=question_id,
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
    )

    # Save to file
    filepath = question_dir / f"{timestamp}.json"
    filepath.write_text(forecast.model_dump_json(indent=2), encoding="utf-8")

    logger.info("Saved forecast for question %d to %s", question_id, filepath)
    return filepath


def load_past_forecasts(question_id: int) -> list[SavedForecast]:
    """Load all past forecasts for a question.

    Args:
        question_id: Metaculus question/post ID.

    Returns:
        List of SavedForecast objects, sorted by timestamp (oldest first).
    """
    question_dir = FORECASTS_BASE_PATH / str(question_id)

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


def get_latest_forecast(question_id: int) -> SavedForecast | None:
    """Get the most recent forecast for a question.

    Args:
        question_id: Metaculus question/post ID.

    Returns:
        The most recent SavedForecast, or None if no forecasts exist.
    """
    forecasts = load_past_forecasts(question_id)
    return forecasts[-1] if forecasts else None


def update_resolution(question_id: int, resolution: str) -> None:
    """Update the resolution status for all forecasts of a question.

    Args:
        question_id: Metaculus question/post ID.
        resolution: Resolution status ("yes", "no", "ambiguous").
    """
    question_dir = FORECASTS_BASE_PATH / str(question_id)

    if not question_dir.exists():
        logger.warning("No forecasts found for question %d", question_id)
        return

    for filepath in question_dir.glob("*.json"):
        try:
            data = json.loads(filepath.read_text(encoding="utf-8"))
            data["resolution"] = resolution
            filepath.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning("Failed to update resolution in %s: %s", filepath, e)

    logger.info(
        "Updated resolution to '%s' for all forecasts of question %d",
        resolution,
        question_id,
    )


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
