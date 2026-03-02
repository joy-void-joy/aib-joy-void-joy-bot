"""Forecast scoring.

Scoring functions (Brier, log loss), resolution extraction from saved
forecast JSONs, and score row building for the unified scores table.

Convention: both Brier and log loss are positive, lower-is-better, 0 = perfect.
"""

import math

from aib.paths import load_all_forecast_jsons, load_all_retrodict_jsons


def compute_brier(probability: float, outcome: bool) -> float:
    """Brier score: 0 = perfect, 0.25 = random, 1 = worst."""
    target = 1.0 if outcome else 0.0
    return (probability - target) ** 2


def compute_log_score(probability: float, outcome: bool) -> float:
    """Log loss: 0 = perfect, 0.693 = random. Clamped to [0.001, 0.999]."""
    p = max(0.001, min(0.999, probability))
    return -math.log(p) if outcome else -math.log(1 - p)


def compute_baseline_score(data: dict[str, object]) -> float | None:
    """Metaculus baseline score: rescaled log score vs uniform prior.

    Binary:  100 * (log2(P(outcome)) + 1)
    MC:      100 * (ln(P(outcome)) - ln(1/N)) / ln(N)
    Numeric: 100 * (ln(pdf) - ln(baseline)) / 2

    Positive = better than chance, 0 = chance level, negative = worse.
    """
    qtype = str(data.get("question_type", ""))

    if qtype == "binary":
        prob = data.get("probability")
        resolution = resolve_binary(data)
        if not isinstance(prob, (int, float)) or resolution is None:
            return None
        p_outcome = prob if resolution == "yes" else 1.0 - prob
        p_outcome = max(0.001, min(0.999, p_outcome))
        return 100.0 * (math.log2(p_outcome) + 1.0)

    if qtype == "multiple_choice":
        mc_res = resolve_mc(data)
        probs = data.get("probabilities")
        if not mc_res or not isinstance(probs, dict):
            return None
        p_outcome = probs.get(mc_res, 0)
        if not isinstance(p_outcome, (int, float)) or p_outcome <= 0:
            return None
        n = len(probs)
        if n < 2:
            return None
        p_outcome = max(0.001, p_outcome)
        return 100.0 * (math.log(p_outcome) - math.log(1.0 / n)) / math.log(n)

    if qtype in ("numeric", "discrete"):
        return _baseline_numeric(data)

    return None


def _baseline_numeric(data: dict[str, object]) -> float | None:
    """Baseline score for numeric/discrete questions from stored CDF.

    Uses the Metaculus formula: 100 * (ln(pdf) - ln(baseline)) / 2
    where pdf is in normalized [0,1] space and baseline depends on
    open/closed bounds (1.0 both closed, 0.95 one open, 0.9 both open).
    """
    resolution = resolve_numeric(data)
    cdf = data.get("cdf")
    bounds = data.get("numeric_bounds")
    if resolution is None or not isinstance(cdf, list) or not isinstance(bounds, dict):
        return None

    range_min = bounds.get("range_min")
    range_max = bounds.get("range_max")
    if not isinstance(range_min, (int, float)) or not isinstance(range_max, (int, float)):
        return None
    if range_max <= range_min:
        return None

    n_points = len(cdf)
    if n_points < 2:
        return None

    qrange = float(range_max - range_min)
    frac = (resolution - range_min) / qrange
    idx = frac * (n_points - 1)
    i = max(0, min(n_points - 2, int(idx)))

    pdf = (cdf[i + 1] - cdf[i]) * (n_points - 1)
    pdf = max(0.01, min(pdf, 35.0))

    open_lower = bounds.get("open_lower_bound", False)
    open_upper = bounds.get("open_upper_bound", False)
    n_open = (1 if open_lower else 0) + (1 if open_upper else 0)
    uniform_baseline = 1.0 - 0.05 * n_open

    return 100.0 * (math.log(pdf) - math.log(uniform_baseline)) / 2.0


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


def build_score_row(data: dict[str, object], source: str) -> dict[str, str]:
    """Build a CSV row dict from a forecast JSON."""
    qtype = str(data.get("question_type", ""))
    resolution_str = str(data.get("resolution") or "")
    resolved = False
    brier = ""
    log_score = ""
    abs_error = ""
    norm_error = ""
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
                ci_half = (ci[1] - ci[0]) / 2
                if ci_half > 0 and isinstance(median, (int, float)):
                    norm_error = f"{abs(actual - median) / ci_half:.4f}"

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
        "norm_error": norm_error,
        "within_ci": within_ci,
        "duration_seconds": str(duration) if duration else "",
        "cost_usd": str(cost) if cost else "",
    }


def load_all_score_rows(
    versions: list[str] | None = None,
) -> list[dict[str, str]]:
    """Load forecasts and retrodictions, compute scores, return as row dicts.

    Pass versions from resolve_version(). None means all versions.
    """
    rows: list[dict[str, str]] = []

    for data in load_all_forecast_jsons(versions=versions):
        rows.append(build_score_row(data, "live"))

    for data in load_all_retrodict_jsons(versions=versions):
        rows.append(build_score_row(data, "retrodict"))

    rows.sort(key=lambda r: (r["post_id"], r["source"], r["timestamp"]))
    return rows
