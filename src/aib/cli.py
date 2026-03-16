"""Metaculus Forecasting Bot - CLI Entry Point."""

import asyncio
import json
import logging
import math
from pathlib import Path
import time
from datetime import datetime, timezone
from typing import Annotated, TypedDict

import httpx
import typer

from aib.agent import ContextOverrides, ForecastOutput, run_forecast
from aib.config import TOURNAMENTS as TOURNAMENT_IDS
from aib.agent.history import (
    RetrodictComparison,
    commit_forecast,
    is_submitted,
    load_latest_for_submission,
    mark_submitted,
    update_retrodict_comparison,
)
from aib.retrodict_context import forecasted_post_id, retrodict_cutoff
from aib.clients.metaculus import get_client as get_metaculus_client
from metaculus import (
    BinaryQuestion,
    DateQuestion,
    DiscreteQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
)
from aib.agent.models import CreditExhaustedError
from aib.submission import (
    SubmissionError,
    format_reasoning_comment,
    list_open_tournament_questions,
    post_comment,
    submit_forecast,
)

app = typer.Typer(
    help="Metaculus AI Benchmarking Forecasting Bot",
    pretty_exceptions_show_locals=False,
)
logger = logging.getLogger(__name__)


class NumericCP(TypedDict):
    median: float
    ci_lower: float
    ci_upper: float
    range_min: float
    range_span: float
    cdf: list[float] | None


class QuestionMeta(TypedDict):
    resolution: str | None
    binary_cp: float | None
    numeric_cp: NumericCP | None
    published_at: datetime | None
    title: str
    question_type: str
    description: str
    resolution_criteria: str
    fine_print: str
    close_time: datetime | None
    scheduled_resolution_time: datetime | None
    num_forecasters: int
    num_predictions: int


_TYPE_EMOJI_MAP = {
    "binary": "✅",
    "numeric": "📊",
    "discrete": "🔢",
    "multiple_choice": "🎲",
    "date": "📅",
}


def _compute_crps(
    cdf: list[float], actual: float, range_min: float, range_span: float
) -> float:
    """CRPS from a 201-point CDF. Lower is better, 0 = perfect."""
    n = len(cdf)
    dx = range_span / (n - 1)
    total = 0.0
    for i in range(n):
        x = range_min + i * dx
        step = 0.0 if x < actual else 1.0
        total += (cdf[i] - step) ** 2
    return total * dx


def _crps_emoji(crps: float, range_span: float) -> str:
    if range_span <= 0:
        return "❓"
    pct = crps / range_span * 100
    if pct < 1:
        return "🎯"
    if pct < 5:
        return "👌"
    if pct < 15:
        return "😬"
    return "🫠"


def _percentile_from_cdf(
    cdf: list[float], p: float, range_min: float, range_span: float
) -> float:
    """Extract the p-th percentile (0–100) from a CDF."""
    target = p / 100
    n = len(cdf)
    for i in range(n):
        if cdf[i] >= target:
            return range_min + i * range_span / (n - 1)
    return range_min + range_span


def _truncate(text: str, max_len: int = 300) -> str:
    if not text or len(text) <= max_len:
        return text
    return text[:max_len].rsplit(" ", 1)[0] + "..."


def _extract_numeric_cp(q: NumericQuestion) -> NumericCP | None:
    """Extract community prediction median, CI, and range from api_json."""
    try:
        qdict = q.api_json.get("question") or {}
        scaling = qdict.get("scaling") or {}
        agg = qdict.get("aggregations") or {}
        method = qdict.get("default_aggregation_method", "unweighted")
        history = (agg.get(method) or {}).get("history", [])
        if not history:
            return None
        latest = history[-1]
        range_min = scaling["range_min"]
        range_max = scaling["range_max"]
        span = range_max - range_min
        cp_cdf: list[float] | None = latest.get("forecast_values")
        return NumericCP(
            median=range_min + latest["centers"][0] * span,
            ci_lower=range_min + latest["interval_lower_bounds"][0] * span,
            ci_upper=range_min + latest["interval_upper_bounds"][0] * span,
            range_min=range_min,
            range_span=span,
            cdf=cp_cdf,
        )
    except (KeyError, IndexError, TypeError):
        return None


def _lookup_cached_resolution(post_id: int) -> str | None:
    """Look up resolution from the latest forecast JSON when the API returns null."""
    from aib.paths import find_latest_forecast_file

    latest = find_latest_forecast_file(post_id)
    if latest is None:
        return None
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
        resolution = data.get("resolution")
        return str(resolution) if resolution is not None else None
    except (json.JSONDecodeError, OSError):
        return None


async def get_question_meta(post_id: int) -> QuestionMeta | None:
    """Fetch question metadata including resolution and community prediction."""
    client = get_metaculus_client()
    try:
        result = await client.get_question_by_post_id(post_id)
        if isinstance(result, list):
            if len(result) > 1:
                logger.warning(
                    "Post %d contains %d questions. Using first: %s",
                    post_id,
                    len(result),
                    result[0].question_text[:50],
                )
            q = result[0]
        else:
            q = result

        if isinstance(q, BinaryQuestion):
            qtype = "binary"
        elif isinstance(q, DiscreteQuestion):
            qtype = "discrete"
        elif isinstance(q, NumericQuestion):
            qtype = "numeric"
        elif isinstance(q, DateQuestion):
            qtype = "date"
        elif isinstance(q, MultipleChoiceQuestion):
            qtype = "multiple_choice"
        else:
            qtype = "unknown"

        binary_cp = None
        numeric_cp: NumericCP | None = None
        if isinstance(q, BinaryQuestion):
            binary_cp = q.community_prediction_at_access_time
        elif isinstance(q, NumericQuestion):
            numeric_cp = _extract_numeric_cp(q)

        return QuestionMeta(
            resolution=q.resolution_string or _lookup_cached_resolution(post_id),
            binary_cp=binary_cp,
            numeric_cp=numeric_cp,
            published_at=q.published_time,
            title=q.question_text,
            question_type=qtype,
            description=q.background_info
            or "MISSING — fetch the Metaculus question page for background info.",
            resolution_criteria=q.resolution_criteria
            or "MISSING — fetch the Metaculus question page to recover. Titles can be misleading; resolution criteria define what actually counts.",
            fine_print=q.fine_print
            or "MISSING — fetch the Metaculus question page to recover.",
            close_time=q.close_time,
            scheduled_resolution_time=q.scheduled_resolution_time,
            num_forecasters=q.num_forecasters or 0,
            num_predictions=q.num_predictions or 0,
        )
    except Exception as e:
        logger.warning(f"Failed to fetch question {post_id}: {e}")
        return None


class RetrodictInfo(TypedDict):
    resolution: str | None
    final_cp: float | None
    cutoff_date: str | None


def display_question_preview(
    meta: QuestionMeta,
    *,
    retrodict_info: RetrodictInfo | None = None,
) -> None:
    """Display question metadata before forecasting."""
    te = _TYPE_EMOJI_MAP.get(meta["question_type"], "❓")
    print(f"\n📋 {meta['title']}")

    stats_parts = [f"{te} {meta['question_type']}"]
    if meta["num_forecasters"]:
        stats_parts.append(f"{meta['num_forecasters']} forecasters")
    if meta["num_predictions"]:
        stats_parts.append(f"{meta['num_predictions']} predictions")
    print(f"   Type:      {' · '.join(stats_parts)}")

    date_parts: list[str] = []
    if meta["published_at"]:
        date_parts.append(f"Published: {meta['published_at'].strftime('%Y-%m-%d')}")
    if meta["close_time"]:
        date_parts.append(f"Closes: {meta['close_time'].strftime('%Y-%m-%d')}")
    if meta["scheduled_resolution_time"]:
        date_parts.append(
            f"Resolves: {meta['scheduled_resolution_time'].strftime('%Y-%m-%d')}"
        )
    if date_parts:
        print(f"   Dates:     {' → '.join(date_parts)}")

    if meta["description"]:
        print(f"\n   Description:\n   {_truncate(meta['description'])}")
    if meta["resolution_criteria"]:
        print(f"\n   Resolution criteria:\n   {_truncate(meta['resolution_criteria'])}")
    if meta["fine_print"]:
        print(f"\n   Fine print:\n   {_truncate(meta['fine_print'], 200)}")

    if retrodict_info is not None:
        print(f"\n{'─' * 60}")
        resolution = retrodict_info["resolution"]
        if resolution:
            print(f"   Resolved:  {resolution}")
            final_cp = retrodict_info["final_cp"]
            if final_cp is not None:
                print(f"   Final CP:  {final_cp:.1%}")
        else:
            print("   ⚠️  Not resolved (question may still be open)")
        cutoff = retrodict_info["cutoff_date"]
        if cutoff:
            print(f"   🔒 Blind mode: data restricted to before {cutoff}")
        print("─" * 60)


def wait_for_credit_reset(error: CreditExhaustedError) -> None:
    """Wait until credit reset time, with progress updates."""
    if error.reset_time is None:
        # No reset time available, use a default wait of 1 hour
        default_wait = 60 * 60
        print("💤 Credit exhausted, waiting 1 hour (no reset time available)...")
        time.sleep(default_wait)
        return

    now = datetime.now(error.reset_time.tzinfo)
    wait_seconds = (error.reset_time - now).total_seconds()

    if wait_seconds <= 0:
        print("⚡ Reset time has passed, continuing...")
        return

    reset_str = error.reset_time.strftime("%H:%M %Z")
    print(
        f"💤 Credit exhausted. Waiting until {reset_str} ({wait_seconds / 60:.0f} minutes)..."
    )

    # Sleep in chunks to show progress
    chunk_size = 300  # 5 minutes
    remaining = wait_seconds
    while remaining > 0:
        sleep_time = min(chunk_size, remaining)
        time.sleep(sleep_time)
        remaining -= sleep_time
        if remaining > 0:
            print(f"   ⏳ {remaining / 60:.0f} minutes remaining...")

    print("⚡ Credit reset time reached, resuming...")


def display_forecast(output: ForecastOutput) -> None:
    """Display forecast results to console."""
    type_emoji = {
        "binary": "✅",
        "numeric": "📊",
        "discrete": "🔢",
        "multiple_choice": "🎲",
    }.get(output.question_type, "❓")

    print(f"\n{'=' * 60}")
    print(f"Question: {output.question_title}")
    print(f"Type: {type_emoji} {output.question_type}")
    print("=" * 60)

    print(f"\nSummary: {output.summary}")

    if output.probability is not None:
        line = f"\n🎯 Forecast: {output.probability * 100:.1f}%"
        if output.logit is not None:
            line += f" (logit: {output.logit:+.2f})"
            if output.probability_from_logit is not None:
                diff = abs(output.probability - output.probability_from_logit)
                if diff > 0.005:  # Show if >0.5% difference
                    line += f" [sigmoid: {output.probability_from_logit * 100:.1f}%]"
        print(line)

    if output.probabilities:
        print("\n🎲 Probabilities:")
        for option, prob in output.probabilities.items():
            print(f"  {option}: {prob * 100:.1f}%")

    if output.median is not None:
        print(f"\n📊 Estimate: {output.median}")
        if output.confidence_interval:
            lo, hi = output.confidence_interval
            print(f"   90% CI: [{lo}, {hi}]")

    if output.factors:
        print("\nFactors:")
        for factor in output.factors:
            sign = "+" if factor.logit >= 0 else ""
            print(f"  [{sign}{factor.logit:.1f}] {factor.description}")

    if output.sources_consulted:
        print(f"\nSources: {len(output.sources_consulted)} consulted")

    print("\n" + "=" * 60)
    if output.duration_seconds:
        minutes, seconds = divmod(output.duration_seconds, 60)
        if minutes >= 1:
            print(f"Duration: {int(minutes)}m {seconds:.0f}s")
        else:
            print(f"Duration: {seconds:.1f}s")
    if output.cost_usd:
        print(f"Cost: ${output.cost_usd:.4f}")
    if output.tool_metrics:
        metrics = output.tool_metrics
        print(
            f"Tools: {metrics.get('total_tool_calls', 0)} calls, "
            f"{metrics.get('total_errors', 0)} errors"
        )
    print()


def setup_logging() -> None:
    """Configure root logger level. File handler is set up by run_forecast."""
    logging.getLogger().setLevel(logging.DEBUG)


def _resolve_text_arg(value: str) -> str:
    """Resolve a text argument: read from file if prefixed with @, else return as-is."""
    if value.startswith("@"):
        return Path(value[1:]).read_text().strip()
    return value


def _build_overrides(
    description: str | None,
    resolution_criteria: str | None,
    fine_print: str | None,
) -> ContextOverrides | None:
    """Build ContextOverrides from optional CLI args, resolving @file references."""
    overrides = ContextOverrides()
    if description is not None:
        overrides["description"] = _resolve_text_arg(description)
    if resolution_criteria is not None:
        overrides["resolution_criteria"] = _resolve_text_arg(resolution_criteria)
    if fine_print is not None:
        overrides["fine_print"] = _resolve_text_arg(fine_print)
    return overrides or None


@app.command()
def test(
    question_id: Annotated[int, typer.Argument(help="Metaculus question/post ID")],
    description: Annotated[
        str | None,
        typer.Option(
            help="Override background description (prefix with @ to read from file)"
        ),
    ] = None,
    resolution_criteria: Annotated[
        str | None,
        typer.Option(
            help="Override resolution criteria (prefix with @ to read from file)"
        ),
    ] = None,
    fine_print: Annotated[
        str | None,
        typer.Option(help="Override fine print (prefix with @ to read from file)"),
    ] = None,
) -> None:
    """Test forecasting on a single question without submitting."""
    meta = asyncio.run(get_question_meta(question_id))
    if meta is not None:
        display_question_preview(meta)

    setup_logging()

    try:
        overrides = _build_overrides(description, resolution_criteria, fine_print)
        output = asyncio.run(run_forecast(question_id, context_overrides=overrides))
        display_forecast(output)
    except CreditExhaustedError as e:
        reset_msg = ""
        if e.reset_time:
            reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
        print(f"❌ Credit exhausted.{reset_msg}")
        raise typer.Exit(1)
    except httpx.HTTPStatusError as e:
        print(f"Failed to fetch question: {e}")
        raise typer.Exit(1)
    except RuntimeError as e:
        print(f"Agent failed: {e}")
        raise typer.Exit(1)


@app.command()
def retrodict(
    question_ids: Annotated[
        list[int], typer.Argument(help="Metaculus post IDs of resolved questions")
    ],
    forecast_date: Annotated[
        str | None,
        typer.Option(
            "--forecast-date",
            "-d",
            help="Restrict data access to this date (YYYY-MM-DD). Enables blind mode.",
        ),
    ] = None,
    blind: Annotated[
        bool,
        typer.Option(
            "--blind/--no-blind",
            help="Enable blind mode (restrict to question published_at if no --forecast-date)",
        ),
    ] = True,
) -> None:
    """Run forecasts on resolved questions for calibration.

    Forecasts resolved questions to build calibration data. Does not submit.
    Shows the actual resolution and computes Brier score for binary questions.

    By default, runs in "blind mode" which restricts all tools to data
    available before the question's published_at date. This prevents
    "future leak" where the agent finds out the answer by searching.

    Use --forecast-date to specify a custom cutoff date, or --no-blind
    to disable time restrictions entirely (useful for testing).

    Examples:
        uv run forecast retrodict 41835 41521
        uv run forecast retrodict 41835 --forecast-date 2026-01-15
        uv run forecast retrodict 41835 --no-blind  # No time restriction
    """
    parsed_forecast_date: datetime | None = None
    if forecast_date:
        try:
            parsed_forecast_date = datetime.strptime(forecast_date, "%Y-%m-%d")
        except ValueError:
            print(f"❌ Invalid date format: {forecast_date}. Use YYYY-MM-DD.")
            raise typer.Exit(1)

    def _brier_emoji(score: float) -> str:
        if score < 0.05:
            return "🎯"
        if score < 0.15:
            return "👌"
        if score < 0.35:
            return "😬"
        return "🫠"

    def _err_emoji(pct: float) -> str:
        if pct < 1:
            return "🎯"
        if pct < 5:
            return "👌"
        if pct < 15:
            return "😬"
        return "🫠"

    def _mc_emoji(prob: float) -> str:
        if prob >= 0.5:
            return "🎯"
        if prob >= 0.25:
            return "👌"
        if prob >= 0.1:
            return "😬"
        return "🫠"

    def _vs_community(our_err: float, cp_err: float) -> str:
        """Scaled emoji comparison against community prediction."""
        if our_err == 0 and cp_err == 0:
            return "🤝 tied"
        if our_err == 0:
            return "🏆🏆🏆 perfect"
        if cp_err == 0:
            return "📉📉📉 CP was perfect"
        if our_err < cp_err:
            ratio = cp_err / our_err
            if ratio >= 3.0:
                return f"🏆🏆🏆 {ratio:.1f}x closer"
            if ratio >= 2.0:
                return f"🏆🏆 {ratio:.1f}x closer"
            if ratio >= 1.2:
                return f"🏆 {ratio:.1f}x closer"
            return f"🤝 ~tied ({ratio:.2f}x)"
        else:
            ratio = our_err / cp_err
            if ratio >= 3.0:
                return f"📉📉📉 {ratio:.1f}x further"
            if ratio >= 2.0:
                return f"📉📉 {ratio:.1f}x further"
            if ratio >= 1.2:
                return f"📉 {ratio:.1f}x further"
            return f"🤝 ~tied ({1 / ratio:.2f}x)"

    results: list[dict] = []

    for i, qid in enumerate(question_ids, 1):
        meta = asyncio.run(get_question_meta(qid))
        title_part = f": {meta['title'][:50]}..." if meta else ""
        print(f"\n[{i}/{len(question_ids)}] Retrodicting #{qid}{title_part}")

        if meta is None:
            print("❌ Could not fetch question metadata")
            results.append({"post_id": qid, "error": "fetch_failed"})
            continue

        resolution = meta["resolution"]
        final_cp = meta["binary_cp"]
        numeric_cp = meta["numeric_cp"]
        published_at = meta["published_at"]

        cutoff_date = None
        if blind:
            if parsed_forecast_date:
                cutoff_date = parsed_forecast_date.date()
            elif published_at:
                cutoff_date = published_at.date()

        display_question_preview(
            meta,
            retrodict_info=RetrodictInfo(
                resolution=resolution,
                final_cp=final_cp,
                cutoff_date=str(cutoff_date) if cutoff_date else None,
            ),
        )

        if blind and not cutoff_date:
            print("   ⚠️  No published_at found, running without blind mode")

        setup_logging()

        # Run forecast (set ContextVar for retrodict mode)
        try:
            token = retrodict_cutoff.set(cutoff_date)
            pid_token = forecasted_post_id.set(qid)
            try:
                output = asyncio.run(run_forecast(qid))
            finally:
                forecasted_post_id.reset(pid_token)
                retrodict_cutoff.reset(token)
            display_forecast(output)

            # Compute and display comparison between prediction and actual
            comparison: RetrodictComparison | None = None
            brier = None

            print(f"\n{'═' * 60}")
            print("📊 RETRODICT COMPARISON")
            print("═" * 60)

            if output.probability is not None and resolution in ("yes", "no"):
                outcome = 1.0 if resolution == "yes" else 0.0
                brier = (output.probability - outcome) ** 2
                our_abs_err = abs(output.probability - outcome)
                diff_pp = (output.probability - outcome) * 100

                res_emoji = "✅" if resolution == "yes" else "❌"
                print(f"\n   🎯 Reality:       {res_emoji} {resolution.upper()}")

                cp_abs_err: float | None = None
                if final_cp is not None:
                    cp_brier = (final_cp - outcome) ** 2
                    cp_abs_err = abs(final_cp - outcome)
                    cp_clamped = max(0.001, min(0.999, final_cp))
                    cp_log = (
                        -math.log(cp_clamped)
                        if outcome == 1.0
                        else -math.log(1 - cp_clamped)
                    )
                    print(f"\n   👥 Community:     {final_cp:.1%}")
                    print(
                        f"      score:         {_brier_emoji(cp_brier)} "
                        f"Brier: {cp_brier:.4f}  ·  log: {cp_log:.4f}"
                    )
                else:
                    print("\n   👥 Community:     (not available)")

                our_clamped = max(0.001, min(0.999, output.probability))
                our_log = (
                    -math.log(our_clamped)
                    if outcome == 1.0
                    else -math.log(1 - our_clamped)
                )
                print(f"\n   🤖 Us:            {output.probability:.1%}")
                print(
                    f"      score:         {_brier_emoji(brier)} "
                    f"Brier: {brier:.4f}  ·  log: {our_log:.4f}"
                )

                if cp_abs_err is not None:
                    print(
                        f"\n   ⚔️  vs Community: {_vs_community(our_abs_err, cp_abs_err)}"
                    )

                comparison = RetrodictComparison(
                    actual_value=resolution,
                    predicted_value=output.probability,
                    difference_pct=diff_pp,
                    score=brier,
                    score_name="brier",
                )

            elif output.median is not None and resolution:
                within_ci = None
                difference = None

                if output.confidence_interval:
                    lo, hi = output.confidence_interval
                    try:
                        actual_val = float(resolution.replace(",", ""))
                        difference = actual_val - output.median
                        our_abs_err = abs(difference)
                        range_span = numeric_cp["range_span"] if numeric_cp else None

                        print(f"\n   🎯 Reality:       {actual_val:,.1f}")

                        cp_abs_err_num: float | None = None
                        if numeric_cp is not None:
                            cp_median = numeric_cp["median"]
                            cp_abs_err_num = abs(actual_val - cp_median)
                            print(
                                f"\n   👥 Community:     {cp_median:,.1f}"
                                f"  [{numeric_cp['ci_lower']:,.1f} – {numeric_cp['ci_upper']:,.1f}]"
                            )
                            if range_span and range_span > 0:
                                cp_pct = cp_abs_err_num / range_span * 100
                                print(
                                    f"      error:         {_err_emoji(cp_pct)} "
                                    f"off by {cp_abs_err_num:,.1f}  ({cp_pct:.1f}% of range)"
                                )
                                cp_cdf = numeric_cp.get("cdf")
                                if cp_cdf:
                                    cp_crps = _compute_crps(
                                        cp_cdf,
                                        actual_val,
                                        numeric_cp["range_min"],
                                        range_span,
                                    )
                                    print(
                                        f"      score:         {_crps_emoji(cp_crps, range_span)} "
                                        f"CRPS: {cp_crps:,.2f}  ({cp_crps / range_span * 100:.1f}% of range)"
                                    )
                        else:
                            print("\n   👥 Community:     (not available)")

                        crps_score: float | None = None
                        if output.cdf and numeric_cp and range_span and range_span > 0:
                            crps_score = _compute_crps(
                                output.cdf,
                                actual_val,
                                numeric_cp["range_min"],
                                range_span,
                            )

                        print(
                            f"\n   🤖 Us:            {output.median:,.1f}  [{lo:,.1f} – {hi:,.1f}]"
                        )
                        if range_span and range_span > 0:
                            our_pct = our_abs_err / range_span * 100
                            print(
                                f"      error:         {_err_emoji(our_pct)} "
                                f"off by {our_abs_err:,.1f}  ({our_pct:.1f}% of range)"
                            )
                            if crps_score is not None:
                                print(
                                    f"      score:         {_crps_emoji(crps_score, range_span)} "
                                    f"CRPS: {crps_score:,.2f}  ({crps_score / range_span * 100:.1f}% of range)"
                                )
                        else:
                            print(f"      error:         off by {our_abs_err:,.1f}")

                        if cp_abs_err_num is not None:
                            print(
                                f"\n   ⚔️  vs Community: {_vs_community(our_abs_err, cp_abs_err_num)}"
                            )

                        ci_levels: list[tuple[int, float, float]] = []
                        if output.cdf and numeric_cp and range_span and range_span > 0:
                            rm = numeric_cp["range_min"]
                            for level, p_lo, p_hi in [
                                (90, 5, 95),
                                (80, 10, 90),
                                (50, 25, 75),
                            ]:
                                ci_lo = _percentile_from_cdf(
                                    output.cdf, p_lo, rm, range_span
                                )
                                ci_hi = _percentile_from_cdf(
                                    output.cdf, p_hi, rm, range_span
                                )
                                ci_levels.append((level, ci_lo, ci_hi))
                        else:
                            ci_levels.append((90, lo, hi))

                        within_ci = None
                        ci_parts: list[str] = []
                        for level, ci_lo, ci_hi in ci_levels:
                            gap = max(0.0, ci_lo - actual_val, actual_val - ci_hi)
                            ref = (
                                range_span
                                if range_span and range_span > 0
                                else (ci_hi - ci_lo)
                            )
                            ok = gap == 0 or (ref > 0 and gap / ref < 0.001)
                            if within_ci is None:
                                within_ci = ok
                            ci_parts.append(f"{'✅' if ok else '❌'} {level}%")
                        print(f"\n   📍 CI:              {'  '.join(ci_parts)}")

                        comparison = RetrodictComparison(
                            actual_value=actual_val,
                            predicted_value=output.median,
                            difference=difference,
                            within_ci=within_ci,
                            score=crps_score,
                            score_name="crps" if crps_score is not None else None,
                        )
                    except (ValueError, TypeError):
                        print("   (Could not parse resolution as numeric)")
                        comparison = RetrodictComparison(
                            actual_value=resolution,
                            predicted_value=output.median,
                        )

            elif output.probabilities and resolution:
                print(f"\n   🎯 Reality:       {resolution}")

                print("\n   👥 Community:     (not available)")

                print("\n   🤖 Us:")
                for option, prob in sorted(
                    output.probabilities.items(), key=lambda x: -x[1]
                ):
                    marker = (
                        " ← correct" if option.lower() == resolution.lower() else ""
                    )
                    print(f"      {option}: {prob:.1%}{marker}")

                correct_prob = output.probabilities.get(resolution, 0)
                log_score = math.log(correct_prob) if correct_prob > 0 else None
                score_str = (
                    f"  ·  log score: {log_score:.4f}" if log_score is not None else ""
                )
                print(
                    f"      on correct:    {_mc_emoji(correct_prob)} {correct_prob:.1%}{score_str}"
                )

                comparison = RetrodictComparison(
                    actual_value=resolution,
                    predicted_value=correct_prob,
                    score=log_score,
                    score_name="log_score",
                )

            else:
                print(f"\n   🎯 Reality:       {resolution or 'Unknown'}")
                print("   👥 Community:     (not available)")
                print(
                    f"   🤖 Us:            {output.probability or output.median or 'N/A'}"
                )

            print(f"\n{'═' * 60}")

            # Save comparison to retrodict file
            if comparison is not None:
                update_retrodict_comparison(qid, comparison, resolution)

            results.append(
                {
                    "post_id": qid,
                    "resolution": resolution,
                    "our_forecast": output.probability or output.median,
                    "final_cp": final_cp,
                    "brier": brier,
                    "question_type": output.question_type,
                    "comparison": comparison.model_dump() if comparison else None,
                }
            )

        except CreditExhaustedError as e:
            reset_msg = ""
            if e.reset_time:
                reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
            print(f"❌ Credit exhausted.{reset_msg}")
            results.append({"post_id": qid, "error": "credit_exhausted"})
        except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
            print(f"❌ Failed to fetch question: {e}")
            results.append({"post_id": qid, "error": str(e)})
        except RuntimeError as e:
            print(f"❌ Agent failed: {e}")
            results.append({"post_id": qid, "error": str(e)})

    # Summary
    print(f"\n{'═' * 60}")
    print("📊 RETRODICT SUMMARY")
    print("═" * 60)

    binary_results = [r for r in results if r.get("brier") is not None]
    if binary_results:
        avg_brier = sum(r["brier"] for r in binary_results) / len(binary_results)
        print(f"\nBinary questions: {len(binary_results)}")
        print(f"Average Brier score: {avg_brier:.4f}")

        # Compare to CP
        cp_briers = [
            (r.get("final_cp", 0.5) - (1.0 if r["resolution"] == "yes" else 0.0)) ** 2
            for r in binary_results
            if r.get("final_cp") is not None
        ]
        if cp_briers:
            avg_cp_brier = sum(cp_briers) / len(cp_briers)
            print(f"Average CP Brier: {avg_cp_brier:.4f}")
            diff = avg_brier - avg_cp_brier
            print(
                f"Difference: {diff:+.4f} ({'worse' if diff > 0 else 'better'} than CP)"
            )

    errors = [r for r in results if "error" in r]
    if errors:
        print(f"\nErrors: {len(errors)}")
        for r in errors:
            print(f"  {r['post_id']}: {r['error']}")


@app.command()
def submit(
    question_id: Annotated[int, typer.Argument(help="Metaculus post ID")],
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    use_cache: Annotated[
        bool,
        typer.Option(
            "--use-cache/--no-cache",
            help="Use cached forecast if available instead of re-running agent",
        ),
    ] = True,
    description: Annotated[
        str | None,
        typer.Option(
            help="Override background description (prefix with @ to read from file)"
        ),
    ] = None,
    resolution_criteria: Annotated[
        str | None,
        typer.Option(
            help="Override resolution criteria (prefix with @ to read from file)"
        ),
    ] = None,
    fine_print: Annotated[
        str | None,
        typer.Option(help="Override fine print (prefix with @ to read from file)"),
    ] = None,
) -> None:
    """Forecast a question and submit the prediction to Metaculus."""
    meta = asyncio.run(get_question_meta(question_id))
    if meta is not None:
        display_question_preview(meta)

    output: ForecastOutput | None = None

    # Try to load from cache if requested
    # Use allow_resubmit=True since user explicitly requested submission
    if use_cache:
        output = load_latest_for_submission(question_id, allow_resubmit=True)
        if output is not None:
            from aib.paths import find_latest_forecast_file

            cached_path = find_latest_forecast_file(question_id)
            print(f"📂 Loaded cached forecast from {cached_path}")
            display_forecast(output)
        else:
            print("⚠️  No cached forecast found, running agent...")

    # Run forecast if not loaded from cache
    if output is None:
        setup_logging()

        try:
            overrides = _build_overrides(description, resolution_criteria, fine_print)
            output = asyncio.run(run_forecast(question_id, context_overrides=overrides))
            display_forecast(output)
        except CreditExhaustedError as e:
            reset_msg = ""
            if e.reset_time:
                reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
            print(f"❌ Credit exhausted.{reset_msg}")
            raise typer.Exit(1)
        except httpx.HTTPStatusError as e:
            print(f"Failed to fetch question: {e}")
            raise typer.Exit(1)
        except RuntimeError as e:
            print(f"Agent failed: {e}")
            raise typer.Exit(1)

    print("Submitting forecast to Metaculus...")
    try:
        asyncio.run(submit_forecast(output))
        mark_submitted(output.post_id)
        print(
            f"✅ Forecast submitted (post {output.post_id} → question {output.question_id})"
        )
    except SubmissionError as e:
        print(f"❌ Submission failed: {e}")
        raise typer.Exit(1)

    try:
        if commit_forecast(output.post_id, output.question_title):
            print("  📦 Committed to git")
    except Exception as e:
        print(f"⚠️  Git commit failed: {e}")

    if comment:
        print("Posting reasoning comment...")
        try:
            comment_text = format_reasoning_comment(output)
            # Comments use post_id, not question_id
            asyncio.run(post_comment(output.post_id, comment_text))
            print(f"✅ Comment posted on post {output.post_id}")
        except Exception as e:
            print(f"⚠️  Comment failed (forecast was submitted): {e}")


@app.command()
def tournament(
    tournament_id: Annotated[
        str,
        typer.Argument(
            help="Tournament ID or alias (aib, minibench, cup) or numeric ID"
        ),
    ] = "aib",
    skip_existing: Annotated[
        bool,
        typer.Option(
            "--skip-existing/--no-skip-existing",
            help="Skip questions that already have a local forecast",
        ),
    ] = True,
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="List questions without forecasting"),
    ] = False,
) -> None:
    """Forecast all open questions in a tournament and submit to Metaculus."""
    # Resolve tournament ID alias
    resolved_id: int | str
    if tournament_id in TOURNAMENT_IDS:
        resolved_id = TOURNAMENT_IDS[tournament_id]
    elif tournament_id.isdigit():
        resolved_id = int(tournament_id)
    else:
        resolved_id = tournament_id

    print(f"Fetching open questions from tournament: {resolved_id}")
    try:
        questions = asyncio.run(list_open_tournament_questions(resolved_id))
    except Exception as e:
        print(f"Failed to fetch tournament questions: {e}")
        raise typer.Exit(1)

    print(f"Found {len(questions)} open questions")

    if dry_run:
        for q in questions:
            status = "📝 Already forecast" if q.already_forecast else "⏳ Pending"
            print(f"  [{status}] {q.post_id}: {q.title[:60]}...")
        return

    # Track results
    success_count = 0
    skip_count = 0
    error_count = 0

    for i, q in enumerate(questions, 1):
        print(f"\n[{i}/{len(questions)}] Question {q.post_id}: {q.title[:50]}...")

        # Check for existing forecast (uses Metaculus API data)
        if skip_existing and q.already_forecast:
            print("  ⏭️  Skipping (already forecast on Metaculus)")
            skip_count += 1
            continue

        meta = asyncio.run(get_question_meta(q.post_id))
        if meta is not None:
            display_question_preview(meta)

        setup_logging()

        # Run forecast with credit exhaustion retry
        output: ForecastOutput | None = None
        while True:
            try:
                output = asyncio.run(run_forecast(q.post_id))
                display_forecast(output)
                break
            except CreditExhaustedError as e:
                print(f"  ⚠️  {e}")
                wait_for_credit_reset(e)
                print(f"  🔄 Retrying {q.post_id}...")
            except httpx.HTTPStatusError as e:
                print(f"  ❌ Failed to fetch question: {e}")
                error_count += 1
                break
            except RuntimeError as e:
                print(f"  ❌ Agent failed: {e}")
                error_count += 1
                break
            except Exception as e:
                print(f"  ❌ Unexpected error: {e}")
                logger.exception("Unexpected error forecasting %d", q.post_id)
                error_count += 1
                break

        if output is None:
            continue

        # Submit forecast
        print("  📤 Submitting forecast...")
        try:
            asyncio.run(submit_forecast(output))
            mark_submitted(output.post_id)
            print("  ✅ Forecast submitted")
            success_count += 1
        except SubmissionError as e:
            print(f"  ❌ Submission failed: {e}")
            error_count += 1
            continue

        try:
            if commit_forecast(output.post_id, output.question_title):
                print("  📦 Committed to git")
        except Exception as e:
            print(f"  ⚠️  Git commit failed: {e}")

        # Post comment if requested
        if comment:
            try:
                comment_text = format_reasoning_comment(output)
                asyncio.run(post_comment(q.post_id, comment_text))
                print("  💬 Comment posted")
            except Exception as e:
                print(f"  ⚠️  Comment failed: {e}")

    # Summary
    print(f"\n{'=' * 60}")
    print(
        f"Tournament complete: {success_count} submitted, {skip_count} skipped, {error_count} errors"
    )


@app.command()
def loop(
    tournaments: Annotated[
        list[str] | None,
        typer.Argument(
            help="Tournament IDs or aliases to loop over (default: aib minibench)"
        ),
    ] = None,
    interval: Annotated[
        int,
        typer.Option("--interval", "-i", help="Minutes between runs"),
    ] = 10,
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    use_cache: Annotated[
        bool,
        typer.Option(
            "--use-cache/--no-cache",
            help="Use cached forecast if available instead of re-running agent",
        ),
    ] = True,
) -> None:
    """Continuously forecast tournaments in a loop.

    Runs forever, checking each tournament for new questions every INTERVAL minutes.
    Use Ctrl+C to stop.
    """
    if tournaments is None:
        tournaments = ["aib", "minibench"]

    print(f"Starting forecast loop for tournaments: {', '.join(tournaments)}")
    print(f"Interval: {interval} minutes")
    print("Press Ctrl+C to stop\n")

    while True:
        cycle_start = time.time()
        print(f"\n{'=' * 60}")
        print(f"Cycle started at {datetime.now(timezone.utc).isoformat()}")
        print("=" * 60)

        for tid in tournaments:
            # Resolve tournament ID alias
            resolved_id: int | str
            if tid in TOURNAMENT_IDS:
                resolved_id = TOURNAMENT_IDS[tid]
            elif tid.isdigit():
                resolved_id = int(tid)
            else:
                resolved_id = tid

            print(f"\n📊 Tournament: {tid} ({resolved_id})")

            try:
                questions = asyncio.run(list_open_tournament_questions(resolved_id))
            except Exception as e:
                print(f"  ❌ Failed to fetch questions: {e}")
                continue

            # Filter to only unforecast questions
            pending = [q for q in questions if not q.already_forecast]
            print(
                f"  Found {len(pending)} pending questions (of {len(questions)} open)"
            )

            for i, q in enumerate(pending, 1):
                print(f"\n  [{i}/{len(pending)}] {q.post_id}: {q.title[:50]}...")

                # Check if already submitted locally (API doesn't track this in listings)
                if use_cache and is_submitted(q.post_id):
                    print("    ⏭️  Already submitted (from local cache)")
                    continue

                meta = asyncio.run(get_question_meta(q.post_id))
                if meta is not None:
                    display_question_preview(meta)

                output: ForecastOutput | None = None

                # Try cache first
                if use_cache:
                    output = load_latest_for_submission(q.post_id)
                    if output is not None:
                        print("    📂 Loaded from cache")
                        display_forecast(output)

                # Run agent if no cached forecast
                if output is None:
                    setup_logging()

                    # Retry loop for credit exhaustion
                    while True:
                        try:
                            output = asyncio.run(run_forecast(q.post_id))
                            display_forecast(output)
                            break
                        except CreditExhaustedError as e:
                            print(f"    ⚠️  {e}")
                            wait_for_credit_reset(e)
                            print(f"    🔄 Retrying {q.post_id}...")
                        except httpx.HTTPStatusError as e:
                            print(f"    ❌ Failed to fetch: {e}")
                            output = None
                            break
                        except RuntimeError as e:
                            print(f"    ❌ Agent failed: {e}")
                            output = None
                            break
                        except Exception as e:
                            print(f"    ❌ Unexpected error: {e}")
                            logger.exception(
                                "Unexpected error forecasting %d", q.post_id
                            )
                            output = None
                            break

                if output is None:
                    continue

                print("    📤 Submitting...")
                try:
                    asyncio.run(submit_forecast(output))
                    mark_submitted(output.post_id)
                    print("    ✅ Submitted")
                except SubmissionError as e:
                    print(f"    ❌ Submission failed: {e}")
                    continue

                try:
                    if commit_forecast(output.post_id, output.question_title):
                        print("    📦 Committed to git")
                except Exception as e:
                    print(f"    ⚠️  Git commit failed: {e}")

                if comment:
                    try:
                        comment_text = format_reasoning_comment(output)
                        asyncio.run(post_comment(q.post_id, comment_text))
                        print("    💬 Comment posted")
                    except Exception as e:
                        print(f"    ⚠️  Comment failed: {e}")

        cycle_duration = time.time() - cycle_start
        print(f"\n✅ Cycle complete in {cycle_duration:.0f}s")

        sleep_seconds = interval * 60
        next_run = datetime.now(timezone.utc).timestamp() + sleep_seconds
        next_run_str = datetime.fromtimestamp(next_run, timezone.utc).strftime(
            "%H:%M:%S UTC"
        )
        print(f"💤 Sleeping {interval} minutes (next run at {next_run_str})...")

        try:
            time.sleep(sleep_seconds)
        except KeyboardInterrupt:
            print("\n\n👋 Loop stopped by user")
            raise typer.Exit(0)


@app.command()
def backfill_comments(
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="List forecasts without posting comments"),
    ] = False,
    force: Annotated[
        bool,
        typer.Option(
            "--force", "-f", help="Post comments even if already marked as posted"
        ),
    ] = False,
) -> None:
    """Post private comments on all saved forecasts.

    Skips forecasts that already have comment_posted_at set (unless --force).
    Safe to run multiple times.
    """
    asyncio.run(_backfill_comments_async(dry_run, force))


async def _backfill_comments_async(dry_run: bool, force: bool) -> None:
    """Async implementation of backfill_comments."""
    from aib.agent.history import (
        get_latest_forecast,
        has_comment,
        mark_comment_posted,
    )
    from aib.agent.models import ForecastOutput, validate_factor
    from aib.clients.metaculus import get_client
    from aib.paths import get_all_forecasted_post_ids

    post_ids = sorted(get_all_forecasted_post_ids())
    if not post_ids:
        print("No forecasts found")
        raise typer.Exit(1)

    print(f"Found {len(post_ids)} forecast directories")

    success_count = 0
    skip_count = 0
    error_count = 0

    metaculus = get_client()

    for post_id in post_ids:
        # Check if already has comment (unless force)
        if not force and has_comment(post_id):
            print(f"  ⏭️  {post_id}: Already has comment")
            skip_count += 1
            continue

        saved = get_latest_forecast(post_id)

        if saved is None:
            print(f"  ⚠️  {post_id}: No forecast files found")
            skip_count += 1
            continue

        print(f"  📝 {post_id}: {saved.question_title[:50]}...")

        if dry_run:
            success_count += 1
            continue

        # Convert SavedForecast to ForecastOutput for format_reasoning_comment
        output = ForecastOutput(
            question_id=saved.question_id,
            post_id=saved.post_id or saved.question_id,
            question_title=saved.question_title,
            question_type=saved.question_type,
            summary=saved.summary,
            factors=[validate_factor(f) for f in saved.factors],
            probability=saved.probability,
            logit=saved.logit,
            probabilities=saved.probabilities,
            median=saved.median,
            confidence_interval=saved.confidence_interval,
            percentiles=saved.percentiles,
            reasoning=saved.reasoning,
            sources_consulted=saved.sources_consulted,
        )

        comment_text = format_reasoning_comment(output)

        try:
            await metaculus.post_question_comment(post_id, comment_text)
            mark_comment_posted(post_id)
            print("    ✅ Comment posted")
            success_count += 1
        except Exception as e:
            print(f"    ❌ Error: {e}")
            error_count += 1

    print(
        f"\nDone: {success_count} comments posted, {skip_count} skipped, {error_count} errors"
    )


if __name__ == "__main__":
    app()
