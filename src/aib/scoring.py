"""Forecast scoring and CSV generation.

Scoring functions (Brier, log loss), resolution extraction from saved
forecast JSONs, and CSV row building for the unified scores table.

Convention: both Brier and log loss are positive, lower-is-better, 0 = perfect.
"""

import csv
import json
import math
from pathlib import Path

FORECASTS_PATH = Path("./notes/forecasts")
RETRODICT_PATH = Path("./notes/retrodict")
SCORES_CSV_PATH = Path("./notes/scores.csv")

CSV_COLUMNS = [
    "post_id",
    "question_id",
    "source",
    "agent_version",
    "question_type",
    "question_title",
    "timestamp",
    "retrodict_date",
    "probability",
    "median",
    "ci_lower",
    "ci_upper",
    "resolution",
    "resolved",
    "brier",
    "log_score",
    "abs_error",
    "within_ci",
    "duration_seconds",
    "cost_usd",
]


def compute_brier(probability: float, outcome: bool) -> float:
    """Brier score: 0 = perfect, 0.25 = random, 1 = worst."""
    target = 1.0 if outcome else 0.0
    return (probability - target) ** 2


def compute_log_score(probability: float, outcome: bool) -> float:
    """Log loss: 0 = perfect, 0.693 = random. Clamped to [0.001, 0.999]."""
    p = max(0.001, min(0.999, probability))
    return -math.log(p) if outcome else -math.log(1 - p)


def resolve_binary(data: dict[str, object]) -> str | None:
    """Extract binary resolution from forecast data, checking both fields."""
    resolution = data.get("resolution")
    if resolution in ("yes", "no"):
        return str(resolution)
    comp = data.get("comparison")
    if not isinstance(comp, dict):
        return None
    actual = comp.get("actual_value")
    if actual is None:
        return None
    s = str(actual).lower()
    if s in ("true", "yes", "1", "1.0"):
        return "yes"
    if s in ("false", "no", "0", "0.0"):
        return "no"
    return None


def resolve_numeric(data: dict[str, object]) -> float | None:
    """Extract numeric resolution value."""
    resolution = data.get("resolution")
    if resolution is not None:
        try:
            return float(str(resolution).replace(",", ""))
        except (ValueError, TypeError):
            pass
    comp = data.get("comparison")
    if not isinstance(comp, dict):
        return None
    actual = comp.get("actual_value")
    if actual is not None:
        try:
            return float(str(actual).replace(",", ""))
        except (ValueError, TypeError):
            pass
    return None


def resolve_mc(data: dict[str, object]) -> str | None:
    """Extract multiple choice resolution."""
    resolution = data.get("resolution")
    if resolution and isinstance(resolution, str):
        return resolution
    comp = data.get("comparison")
    if not isinstance(comp, dict):
        return None
    actual = comp.get("actual_value")
    if actual and isinstance(actual, str):
        return actual
    return None


def load_forecast_jsons(base_path: Path) -> list[dict[str, object]]:
    """Load all forecast JSON files from a directory tree."""
    results: list[dict[str, object]] = []
    if not base_path.exists():
        return results
    for post_dir in base_path.iterdir():
        if not post_dir.is_dir():
            continue
        for filepath in post_dir.glob("*.json"):
            try:
                data = json.loads(filepath.read_text())
                if "question_type" in data and "timestamp" in data:
                    results.append(data)
            except (json.JSONDecodeError, OSError):
                continue
    return results


def build_score_row(data: dict[str, object], source: str) -> dict[str, str]:
    """Build a CSV row dict from a forecast JSON."""
    qtype = str(data.get("question_type", ""))
    resolution_str = str(data.get("resolution") or "")
    resolved = False
    brier = ""
    log_score = ""
    abs_error = ""
    within_ci = ""

    if qtype == "binary":
        prob = data.get("probability")
        binary_res = resolve_binary(data)
        if isinstance(prob, (int, float)) and binary_res is not None:
            resolved = True
            resolution_str = binary_res
            outcome = binary_res == "yes"
            brier = f"{compute_brier(prob, outcome):.6f}"
            log_score = f"{compute_log_score(prob, outcome):.6f}"

    elif qtype in ("numeric", "discrete"):
        actual = resolve_numeric(data)
        if actual is not None:
            resolved = True
            resolution_str = str(actual)
            median = data.get("median")
            if isinstance(median, (int, float)):
                abs_error = f"{abs(actual - median):.4f}"
            ci = data.get("confidence_interval")
            if isinstance(ci, list) and len(ci) == 2:
                within_ci = str(ci[0] <= actual <= ci[1])

    elif qtype == "multiple_choice":
        mc_res = resolve_mc(data)
        probs = data.get("probabilities")
        if mc_res and isinstance(probs, dict):
            resolved = True
            resolution_str = mc_res
            correct_prob = probs.get(mc_res, 0)
            if isinstance(correct_prob, (int, float)) and correct_prob > 0:
                log_score = f"{-math.log(max(0.001, correct_prob)):.6f}"

    ci = data.get("confidence_interval")
    ci_lower = str(ci[0]) if isinstance(ci, list) and len(ci) == 2 else ""
    ci_upper = str(ci[1]) if isinstance(ci, list) and len(ci) == 2 else ""

    tool_metrics = data.get("tool_metrics")
    token_usage = data.get("token_usage")
    duration = (
        tool_metrics.get("duration_seconds", "")
        if isinstance(tool_metrics, dict)
        else ""
    )
    cost = token_usage.get("cost_usd", "") if isinstance(token_usage, dict) else ""

    return {
        "post_id": str(data.get("post_id", data.get("question_id", ""))),
        "question_id": str(data.get("question_id", "")),
        "source": source,
        "agent_version": str(data.get("agent_version", "")),
        "question_type": qtype,
        "question_title": str(data.get("question_title", ""))[:80],
        "timestamp": str(data.get("timestamp", "")),
        "retrodict_date": str(data.get("retrodict_date", "")),
        "probability": str(data.get("probability", "")),
        "median": str(data.get("median", "")) if data.get("median") is not None else "",
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "resolution": resolution_str,
        "resolved": str(resolved),
        "brier": brier,
        "log_score": log_score,
        "abs_error": abs_error,
        "within_ci": within_ci,
        "duration_seconds": str(duration) if duration else "",
        "cost_usd": str(cost) if cost else "",
    }


def load_all_score_rows() -> list[dict[str, str]]:
    """Load all forecasts and retrodictions, compute scores, return as row dicts."""
    rows: list[dict[str, str]] = []

    for data in load_forecast_jsons(FORECASTS_PATH):
        rows.append(build_score_row(data, "live"))

    for data in load_forecast_jsons(RETRODICT_PATH):
        rows.append(build_score_row(data, "retrodict"))

    rows.sort(key=lambda r: (r["post_id"], r["source"], r["timestamp"]))
    return rows


def rebuild_scores_csv() -> int:
    """Rebuild the scores CSV from all forecast/retrodict JSONs.

    Returns the number of rows written.
    """
    rows = load_all_score_rows()
    SCORES_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SCORES_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def read_scores_csv() -> list[dict[str, str]]:
    """Read the scores CSV, returning empty list if missing."""
    if not SCORES_CSV_PATH.exists():
        return []
    with SCORES_CSV_PATH.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_scores_for_post(post_id: int) -> list[dict[str, str]]:
    """Read scores for a specific post_id."""
    return [r for r in read_scores_csv() if r.get("post_id") == str(post_id)]


def append_score_row(data: dict[str, object], source: str) -> None:
    """Append a single score row to the CSV. Creates file with header if missing."""
    row = build_score_row(data, source)
    file_exists = SCORES_CSV_PATH.exists()

    SCORES_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SCORES_CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
