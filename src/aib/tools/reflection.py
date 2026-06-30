"""Reflection tool for forecasting sessions.

Fast checkpoint: takes the agent's current factors and tentative
estimate, computes factor-consistency metrics, appends to reflection.yaml,
and caches the input in ReviewState so premortem() can retrieve it.

No reviewer call — that lives in premortem.py. The StructuredOutput gate
requires both reflection() to have been called and premortem() to have
approved.
"""

import json
import logging
import math
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import aiofiles
from pydantic import BaseModel, Field, model_validator

from claude_agent_sdk import tool

from aib.agent.models import (
    BinaryEstimate,
    Factor,
    MultipleChoiceEstimate,
    NumericEstimate,
    NumericSupport,
)
from aib.agent.session import ReviewState
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

NEUTRAL_THRESHOLD = 0.1


# --- Input Model ---


class ReflectionInput(BaseModel):
    """Structured input for the reflection tool."""

    factors: list[Factor] = Field(
        description=(
            "Key evidence items with logit values and confidence. "
            "Same format as your final forecast factors."
        )
    )
    tentative_estimate: BinaryEstimate | NumericEstimate | MultipleChoiceEstimate = (
        Field(
            description=(
                "Your synthesized estimate. "
                "Binary: {logit, probability}. "
                "Numeric/discrete: {center, low, high}. "
                "MC: {probabilities: {option: probability}}."
            ),
        )
    )

    @model_validator(mode="before")
    @classmethod
    def deserialize_json_fields(cls, data: dict[str, object]) -> dict[str, object]:
        """Deserialize structured fields passed as JSON strings.

        The agent sometimes serializes complex fields (factors,
        tentative_estimate) to a string instead of nested JSON; coerce them
        back so validation sees real objects.
        """
        if isinstance(data, dict):
            for field in ("factors", "tentative_estimate"):
                value = data.get(field)
                if isinstance(value, str):
                    data = {**data, field: json.loads(value)}
        return data

    anchor: str | None = Field(
        default=None,
        description=(
            "Your reference class base rate with source — the probability "
            "you'd assign before question-specific analysis. "
            "E.g. 'Conditional base rate: 65% (stock_conditional_returns, "
            "137 episodes at 30%+ drawdown)'"
        ),
    )
    assessment: str = Field(
        description=(
            "Freeform narrative assessment of the evidence. Structure however "
            "fits the question: pro/con for binary, scenario analysis for "
            "numeric, uncertainty decomposition, key tensions, etc."
        ),
    )
    calibration_notes: str | None = Field(
        default=None,
        description="Base rates, anchor divergence check, hedging check.",
    )
    key_uncertainties: str | None = Field(
        default=None,
        description="What you're most uncertain about and what would change your mind.",
    )
    tool_audit: str = Field(
        description=(
            "Which tools provided useful information, which returned "
            "empty results, and which had actual failures."
        ),
    )
    update_triggers: str | None = Field(
        default=None,
        description="Events that would move your forecast significantly.",
    )
    process_reflection: str = Field(
        description=(
            "How did the forecasting system feel to use — not what you "
            "did, but how the scaffolding supported you. What felt rigid "
            "or lacking, what felt smooth? What tools are missing that "
            "would have helped? What subagents would have been useful? "
            "Did the prompt guide you well or lead you astray for this "
            "question type? Where did you hit friction — a tool returning "
            "junk, a forced workaround, a missing capability?"
        ),
    )


# --- Output Models ---


class FactorBreakdown(BaseModel):
    """Per-factor effective logit computation."""

    description: str
    supports: str | float | NumericSupport | None = None
    logit: float
    confidence: float
    effective_logit: float
    conditional: str | None = None


class OutcomeBreakdown(BaseModel):
    """Per-outcome factor aggregation for MC questions."""

    outcome: str
    factor_count: int
    logit_sum: float
    factors: list[FactorBreakdown]


class NumericDistributionMetrics(BaseModel):
    """Distribution-level consistency metrics for numeric/discrete questions."""

    implied_median: float
    implied_p10: float
    implied_p90: float
    median_gap: float
    median_gap_pct: float
    spread_ratio: float
    precision: float | None = None


class MCDistributionMetrics(BaseModel):
    """Softmax gap metrics for multiple choice questions."""

    implied_probabilities: dict[str, float]
    tentative_probabilities: dict[str, float]
    per_option_gap_pp: dict[str, float]
    max_gap_pp: float
    max_gap_option: str


class ReflectionOutput(BaseModel):
    """Computed feedback from a reflection checkpoint."""

    factor_count: int
    factor_sum: float
    tentative_logit: float | None = None
    logit_gap: float | None = None
    neutral_factor_count: int
    factor_breakdown: list[FactorBreakdown]
    dominant_factor: str | None = None
    dominant_effective_logit: float | None = None

    # Binary-specific
    factor_implied_probability: float | None = None
    tentative_probability: float | None = None
    gap_pp: float | None = None

    # MC: per-outcome aggregation and softmax gap metrics
    outcome_breakdown: list[OutcomeBreakdown] | None = None
    mc_distribution_metrics: MCDistributionMetrics | None = None

    # Numeric/discrete: distribution-level metrics
    distribution_metrics: NumericDistributionMetrics | None = None

    # Sources consulted so far (populated from infrastructure)
    sources: list[str] = Field(default_factory=list)


# --- Computation ---


def compute_distribution_metrics(
    breakdown: list[FactorBreakdown],
    tentative: NumericEstimate,
) -> NumericDistributionMetrics | None:
    """Compute distribution-level consistency for numeric/discrete factors.

    Uses abs(effective_logit) as the weight for each factor's center/range.
    """
    pairs: list[tuple[NumericSupport, float]] = [
        (fb.supports, abs(fb.effective_logit))
        for fb in breakdown
        if isinstance(fb.supports, NumericSupport)
    ]
    if not pairs:
        return None

    total_weight = sum(w for _, w in pairs)
    if total_weight == 0:
        return None

    implied_median = sum(s.center * w for s, w in pairs) / total_weight
    implied_p10 = sum(s.low * w for s, w in pairs) / total_weight
    implied_p90 = sum(s.high * w for s, w in pairs) / total_weight

    implied_range = implied_p90 - implied_p10
    tentative_range = tentative.high - tentative.low
    median_gap = tentative.center - implied_median
    median_gap_pct = (median_gap / implied_range * 100) if implied_range > 0 else 0.0
    spread_ratio = (tentative_range / implied_range) if implied_range > 0 else 0.0

    precision: float | None = None
    if tentative.center != 0:
        precision = tentative_range / abs(tentative.center)

    return NumericDistributionMetrics(
        implied_median=implied_median,
        implied_p10=implied_p10,
        implied_p90=implied_p90,
        median_gap=median_gap,
        median_gap_pct=median_gap_pct,
        spread_ratio=spread_ratio,
        precision=precision,
    )


def compute_reflection(
    inp: ReflectionInput,
    question_type: str,
) -> ReflectionOutput:
    """Compute factor analysis and return structured feedback."""
    breakdown: list[FactorBreakdown] = []
    for f in inp.factors:
        breakdown.append(
            FactorBreakdown(
                description=f.description,
                supports=f.supports,
                logit=f.logit,
                confidence=f.confidence,
                effective_logit=f.logit * f.confidence,
                conditional=f.conditional,
            )
        )

    factor_sum = sum(fb.effective_logit for fb in breakdown)
    neutral_count = sum(1 for f in inp.factors if abs(f.logit) < NEUTRAL_THRESHOLD)
    dominant = max(breakdown, key=lambda fb: abs(fb.effective_logit), default=None)

    estimate = inp.tentative_estimate
    if isinstance(estimate, BinaryEstimate):
        tentative_logit: float | None = estimate.logit
        logit_gap: float | None = tentative_logit - factor_sum
    else:
        tentative_logit = None
        logit_gap = None

    output = ReflectionOutput(
        factor_count=len(inp.factors),
        factor_sum=factor_sum,
        tentative_logit=tentative_logit,
        logit_gap=logit_gap,
        neutral_factor_count=neutral_count,
        factor_breakdown=breakdown,
        dominant_factor=dominant.description if dominant else None,
        dominant_effective_logit=dominant.effective_logit if dominant else None,
    )

    if question_type == "binary" and isinstance(estimate, BinaryEstimate):
        output.factor_implied_probability = 1 / (1 + math.exp(-factor_sum))
        output.tentative_probability = estimate.probability
        output.gap_pp = (estimate.probability - output.factor_implied_probability) * 100
    elif question_type in ("numeric", "discrete"):
        assert isinstance(estimate, NumericEstimate)
        output.distribution_metrics = compute_distribution_metrics(breakdown, estimate)
    elif question_type == "multiple_choice":
        from collections import defaultdict

        by_outcome: dict[str, list[FactorBreakdown]] = defaultdict(list)
        for fb in breakdown:
            if isinstance(fb.supports, str):
                by_outcome[fb.supports].append(fb)

        output.outcome_breakdown = [
            OutcomeBreakdown(
                outcome=outcome,
                factor_count=len(factors),
                logit_sum=sum(fb.effective_logit for fb in factors),
                factors=factors,
            )
            for outcome, factors in by_outcome.items()
        ]

        if isinstance(estimate, MultipleChoiceEstimate) and output.outcome_breakdown:
            all_options = set(estimate.probabilities) | set(by_outcome)
            logit_sums = {
                opt: sum(fb.effective_logit for fb in by_outcome.get(opt, []))
                for opt in all_options
            }
            max_logit = max(logit_sums.values()) if logit_sums else 0.0
            exp_values = {opt: math.exp(v - max_logit) for opt, v in logit_sums.items()}
            exp_total = sum(exp_values.values())
            implied = {opt: ev / exp_total for opt, ev in exp_values.items()}
            per_option_gap = {
                opt: (estimate.probabilities.get(opt, 0.0) - implied.get(opt, 0.0))
                * 100
                for opt in all_options
            }
            max_gap_opt = max(per_option_gap, key=lambda o: abs(per_option_gap[o]))
            output.mc_distribution_metrics = MCDistributionMetrics(
                implied_probabilities=implied,
                tentative_probabilities=dict(estimate.probabilities),
                per_option_gap_pp=per_option_gap,
                max_gap_pp=per_option_gap[max_gap_opt],
                max_gap_option=max_gap_opt,
            )

    return output


# --- File Writing ---


async def append_reflection(
    session_dir: Path,
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_type: str,
) -> Path:
    """Append a timestamped reflection entry to reflection.yaml."""
    import yaml

    filepath = session_dir / "reflection.yaml"
    session_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = (
        {"timestamp": timestamp, "question_type": question_type}
        | inp.model_dump(exclude_none=True)
        | {"computed": computed.model_dump(exclude_none=True)}
    )

    content = "---\n" + yaml.dump(
        entry, default_flow_style=False, sort_keys=False, allow_unicode=True
    )

    async with aiofiles.open(filepath, "a", encoding="utf-8") as f:
        await f.write(content)

    return filepath


# --- Tool ---

_REFLECTION_DESCRIPTION = """\
Checkpoint your reasoning by committing to factors and a tentative estimate.

Returns: factor-consistency metrics, distribution metrics (for numeric/discrete),
per-outcome breakdowns (for MC), and sources consulted.

Fast and cheap — call freely mid-research whenever you want to pressure-test
your evolving analysis against the numbers. This tool does not run a reviewer;
it only computes metrics and caches your input so the premortem tool can
retrieve it.

**Gate behavior:** You must call reflection() at least once before premortem(),
and premortem() must approve before you can submit the final forecast via
StructuredOutput.

Binary example:
  reflection(
    factors=[
      {"description": "Strong trend in data", "logit": 1.5, "confidence": 0.8},
      {"description": "Status quo persistence", "logit": -0.5, "confidence": 0.7}
    ],
    tentative_estimate={"logit": 0.8, "probability": 0.69},
    assessment="Data shows consistent upward trend, but base rate is only 30%.",
    ...
  )

Numeric example:
  reflection(
    factors=[
      {"description": "Historical avg is 145", "supports": {"center": 145, "low": 140, "high": 150}, "logit": 1.0, "confidence": 0.9},
      {"description": "Recent uptick suggests higher", "supports": {"center": 152, "low": 148, "high": 158}, "logit": 0.8, "confidence": 0.7}
    ],
    tentative_estimate={"center": 148, "low": 142, "high": 155},
    assessment="Historical data centers around 145 but recent trend pushes higher.",
    ...
  )

MC example:
  reflection(
    factors=[
      {"description": "Polls favor candidate A", "supports": "A", "logit": 1.5, "confidence": 0.8},
      {"description": "Endorsement for B", "supports": "B", "logit": 0.8, "confidence": 0.7}
    ],
    tentative_estimate={"probabilities": {"A": 0.55, "B": 0.30, "C": 0.15}},
    assessment="Candidate A leads in polls but B has momentum from endorsements.",
    ...
  )
"""


def create_reflection_tool(
    session_dir: Path | None,
    question_type: str,
    get_sources: Callable[[], list[str]] | None = None,
    review_state: ReviewState | None = None,
):
    """Create the reflection tool with session context."""

    @tool("reflection", _REFLECTION_DESCRIPTION, ReflectionInput)
    @tracked("reflection")
    async def reflection_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Compute and log a reflection checkpoint."""
        try:
            validated = ReflectionInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        if session_dir is None:
            return mcp_error("reflection is not available in this context")

        computed = compute_reflection(validated, question_type)

        if get_sources is not None:
            computed.sources = get_sources()

        if review_state is not None:
            review_state.store_reflection(validated)

        try:
            filepath = await append_reflection(
                session_dir, validated, computed, question_type
            )
            logger.info("Appended reflection entry to %s", filepath)
        except Exception as e:
            logger.exception("Failed to write reflection")
            return mcp_error(f"Failed to write reflection: {e}")

        return mcp_success(computed.model_dump(exclude_none=True))

    return reflection_tool


def create_reflection_server(
    session_dir: Path | None = None,
    question_type: str = "binary",
    get_sources: Callable[[], list[str]] | None = None,
    review_state: ReviewState | None = None,
):
    """Create the reflection MCP server with session context.

    Args:
        session_dir: Session directory for reflection storage.
            If None, reflection is disabled.
        question_type: The question type for this forecast session.
        get_sources: Callback returning sources consulted so far.
            Called at reflection time to inject into output.
        review_state: Shared state for gate coordination with premortem
            and the StructuredOutput hook. Reflection marks reflection_done
            by caching the input here.
    """
    return create_mcp_server(
        name="notes",
        version="6.0.0",
        tools=[
            create_reflection_tool(
                session_dir,
                question_type,
                get_sources,
                review_state,
            )
        ],
    )
