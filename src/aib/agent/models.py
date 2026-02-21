"""Pydantic models for forecasting."""

import math
import re
from datetime import date, datetime, timedelta
from enum import StrEnum
from typing import Self, TypedDict, cast

from pydantic import BaseModel, Field, computed_field, create_model, model_validator
import zoneinfo


class ServerToolUse(TypedDict, total=False):
    """Server-side tool usage counts."""

    web_search_requests: int
    web_fetch_requests: int


class CacheCreation(TypedDict, total=False):
    """Cache creation token breakdown."""

    ephemeral_1h_input_tokens: int
    ephemeral_5m_input_tokens: int


class TokenUsage(TypedDict, total=False):
    """Token usage from the Anthropic API.

    Uses total=False since fields vary by API version and request type.
    """

    input_tokens: int
    output_tokens: int
    cache_read_input_tokens: int
    cache_creation_input_tokens: int
    server_tool_use: ServerToolUse
    service_tier: str
    cache_creation: CacheCreation


class CreditExhaustedError(Exception):
    """Raised when API credits are exhausted.

    Includes reset time so callers can wait appropriately.
    """

    def __init__(self, message: str, reset_time: datetime | None = None):
        super().__init__(message)
        self.reset_time = reset_time

    @classmethod
    def from_message(cls, message: str) -> "CreditExhaustedError | None":
        """Parse a credit exhaustion message and extract reset time.

        Expected patterns:
        - "out of extra usage · resets 6pm (Europe/Paris)"
        - "out of extra usage · resets 2pm (America/New_York)"

        Returns None if the message doesn't match the expected pattern.
        """
        # Check if this is a credit exhaustion message
        if (
            "out of extra usage" not in message.lower()
            and "out of usage" not in message.lower()
        ):
            return None

        # Try to extract reset time
        # Pattern: "resets <time> (<timezone>)"
        match = re.search(
            r"resets?\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\s*\(([^)]+)\)",
            message,
            re.IGNORECASE,
        )

        reset_time: datetime | None = None
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2)) if match.group(2) else 0
            am_pm = match.group(3)
            tz_name = match.group(4)

            # Convert to 24-hour format
            if am_pm:
                if am_pm.lower() == "pm" and hour != 12:
                    hour += 12
                elif am_pm.lower() == "am" and hour == 12:
                    hour = 0

            try:
                tz = zoneinfo.ZoneInfo(tz_name)
                now = datetime.now(tz)
                reset_time = now.replace(
                    hour=hour, minute=minute, second=0, microsecond=0
                )

                # If reset time is in the past, assume it's tomorrow
                if reset_time <= now:
                    reset_time += timedelta(days=1)
            except (KeyError, ValueError):
                # Invalid timezone, proceed without reset time
                pass

        return cls(message, reset_time)


class BinaryEstimate(BaseModel):
    """Tentative estimate for binary questions."""

    logit: float = Field(description="Synthesized log-odds estimate.")
    probability: float = Field(description="Probability estimate (0.0-1.0).")


class NumericEstimate(BaseModel):
    """Tentative estimate for numeric/discrete questions."""

    center: float = Field(description="Best-guess median value.")
    low: float = Field(description="10th percentile estimate.")
    high: float = Field(description="90th percentile estimate.")


class NumericSupport(BaseModel):
    """Distributional evidence for numeric/discrete questions.

    Each factor contributes a mini-distribution rather than a point estimate,
    preventing point-estimate anchoring and enabling distribution-level
    consistency checks in reflection.
    """

    center: float = Field(description="Best guess from this evidence alone.")
    low: float = Field(description="10th percentile from this evidence alone.")
    high: float = Field(description="90th percentile from this evidence alone.")


class Factor(BaseModel):
    """A piece of evidence that influences the forecast."""

    description: str = Field(description="What this evidence is and why it matters.")
    supports: str | float | NumericSupport | None = Field(
        default=None,
        description="Which outcome this evidence supports (for MC/numeric questions).",
    )
    logit: float = Field(
        description=(
            "Strength and direction of this evidence. "
            "For binary: positive = Yes, negative = No. "
            "For MC/numeric: positive = toward supported outcome, negative = against. "
            "Scale: +/-0.5 mild, +/-1.0 moderate, +/-2.0 strong, +/-3.0 very strong."
        )
    )
    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description=(
            "Confidence in this evidence (0-1). "
            "1.0 = fully confident, 0.5 = half confident. "
            "Effective logit = logit × confidence."
        ),
    )
    conditional: str | None = Field(
        default=None,
        description="Optional condition under which this factor applies.",
    )

    @computed_field
    @property
    def effective_logit(self) -> float:
        """The logit value adjusted for confidence."""
        return self.logit * self.confidence


def create_factor_model(
    question_type: str,
    options: list[str] | None = None,
) -> type[Factor]:
    """Create a Factor model with question-type-specific supports constraint.

    Binary: supports excluded (sign encodes direction).
    MC: StrEnum of option labels. Numeric/discrete: float.
    """
    supports_type: type
    match question_type:
        case "binary":
            return create_model(
                "Factor",
                __base__=Factor,
                supports=(None, Field(default=None, exclude=True)),
            )
        case "multiple_choice" if options:
            supports_type = cast(type, StrEnum("Supports", {o: o for o in options}))
        case "numeric" | "discrete":
            supports_type = NumericSupport
        case _:
            return Factor

    return create_model(
        "Factor",
        __base__=Factor,
        supports=(supports_type, Field(description="Which outcome this evidence supports.")),
    )


def validate_factor(data: dict) -> Factor:
    """Validate a factor dict with backward-compatible deserialization.

    Old JSON forecasts store numeric supports as a bare float. This wraps
    bare floats into NumericSupport(center=x, low=x, high=x) so that
    downstream code can always expect NumericSupport for numeric factors.
    """
    supports = data.get("supports")
    if isinstance(supports, (int, float)):
        data = {
            **data,
            "supports": NumericSupport(
                center=float(supports),
                low=float(supports),
                high=float(supports),
            ).model_dump(),
        }
    return Factor.model_validate(data)


def create_forecast_model(
    question_type: str,
    options: list[str] | None = None,
) -> type[BaseModel]:
    """Create a forecast model with question-type-specific Factor constraints."""
    factor_model = create_factor_model(question_type, options)
    if factor_model is Factor:
        match question_type:
            case "multiple_choice":
                return MultipleChoiceForecast
            case "numeric" | "discrete":
                return NumericForecast
            case _:
                return Forecast

    match question_type:
        case "multiple_choice":
            base: type[BaseModel] = MultipleChoiceForecast
        case "numeric" | "discrete":
            base = NumericForecast
        case _:
            base = Forecast

    return create_model(
        base.__name__,
        __base__=base,
        factors=(list[factor_model], base.model_fields["factors"]),
    )


# --- Forecast Output Models ---


class Forecast(BaseModel):
    """Forecast for binary questions. Used as structured output schema."""

    summary: str = Field(
        description="Brief explanation of the forecast and the key reasoning behind it."
    )
    factors: list[Factor] = Field(
        default_factory=list,
        description=(
            "Key pieces of evidence with their directional strength. "
            "Each factor should have a description and a logit value."
        ),
    )
    logit: float = Field(
        description=(
            "Your synthesized log-odds estimate based on the factors. "
            "Reference: 0 = 50%, ±1 = 73%/27%, ±2 = 88%/12%, ±3 = 95%/5%, ±4 = 98%/2%."
        )
    )
    probability: float = Field(
        description=(
            "Your final probability estimate (0.0 to 1.0). "
            "This is your actual forecast - it does not need to equal sigmoid(logit)."
        )
    )

    @computed_field
    @property
    def probability_from_logit(self) -> float:
        """Convert logit to probability via sigmoid (for comparison)."""
        return 1 / (1 + math.exp(-self.logit))

    @computed_field
    @property
    def factors_sum_logit(self) -> float:
        """Sum of effective logits from all factors."""
        return sum(f.effective_logit for f in self.factors)

    @computed_field
    @property
    def probability_from_factors(self) -> float:
        """Probability computed from sum of factor effective logits."""
        return 1 / (1 + math.exp(-self.factors_sum_logit))

    def check_consistency(self, threshold: float = 0.15) -> list[str]:
        """Check for consistency issues between factors and final probability.

        Args:
            threshold: Maximum acceptable difference between factor-implied
                      probability and final probability.

        Returns:
            List of warning messages (empty if consistent).
        """
        warnings = []

        if not self.factors:
            return warnings

        # Check if factors imply significantly different probability
        factor_prob = self.probability_from_factors
        diff = abs(factor_prob - self.probability)
        if diff > threshold:
            warnings.append(
                f"Factor-implied probability ({factor_prob:.1%}) differs from "
                f"final probability ({self.probability:.1%}) by {diff:.1%}. "
                f"Consider adjusting factors or explaining the discrepancy."
            )

        # Check for contradictory strong factors
        strong_positive = [f for f in self.factors if f.effective_logit >= 1.5]
        strong_negative = [f for f in self.factors if f.effective_logit <= -1.5]
        if strong_positive and strong_negative:
            warnings.append(
                f"Strong contradictory evidence: {len(strong_positive)} strong positive "
                f"factors and {len(strong_negative)} strong negative factors. "
                f"Consider if all factors are correctly weighted."
            )

        # Check if final probability contradicts overall factor direction
        net_direction = self.factors_sum_logit
        if net_direction > 0.5 and self.probability < 0.4:
            warnings.append(
                f"Factors sum to positive ({net_direction:+.2f}) but probability is low "
                f"({self.probability:.1%}). Consider if factors are missing or overweighted."
            )
        elif net_direction < -0.5 and self.probability > 0.6:
            warnings.append(
                f"Factors sum to negative ({net_direction:+.2f}) but probability is high "
                f"({self.probability:.1%}). Consider if factors are missing or underweighted."
            )

        return warnings


class MultipleChoiceForecast(BaseModel):
    """Forecast for multiple choice questions."""

    summary: str = Field(
        description="Brief explanation of the forecast and the key reasoning behind it."
    )
    factors: list[Factor] = Field(
        default_factory=list,
        description="Key pieces of evidence that influenced the probability distribution.",
    )
    probabilities: dict[str, float] = Field(
        description=(
            "Mapping of option label to probability. "
            "Values must be between 0 and 1 and sum to 1.0."
        )
    )


class ScenarioComponent(BaseModel):
    """A scenario component for mixture distribution forecasts.

    Describes one possible scenario with its probability distribution.
    Multiple scenarios are weighted together to form the final forecast.
    """

    scenario: str = Field(
        description="Scenario name: 'Base case', 'Upside', 'Downside', etc."
    )
    mode: float = Field(description="Most likely value if this scenario occurs.")
    lower_bound: float = Field(
        description="10th percentile: 90% chance outcome is above this."
    )
    upper_bound: float = Field(
        description="90th percentile: 10% chance outcome is above this."
    )
    weight: float = Field(
        ge=0.0,
        le=1.0,
        description="Probability this scenario occurs (weights sum to 1.0).",
    )


class NumericForecast(BaseModel):
    """Forecast for numeric questions.

    Supports two modes:
    1. Percentile mode: Provide sparse percentiles (10th, 20th, 40th, 60th, 80th, 90th)
    2. Mixture mode: Provide scenario components with modes and weights

    If components are provided, they take precedence over percentiles.
    """

    summary: str = Field(
        description="Brief explanation of the forecast and the key reasoning behind it."
    )
    factors: list[Factor] = Field(
        default_factory=list,
        description="Key pieces of evidence that influenced the estimate.",
    )

    # Percentile mode fields (traditional approach)
    percentile_10: float | None = Field(
        default=None,
        description="10th percentile estimate: 90% chance the outcome is above this value.",
    )
    percentile_20: float | None = Field(
        default=None,
        description="20th percentile estimate: 80% chance the outcome is above this value.",
    )
    percentile_40: float | None = Field(
        default=None,
        description="40th percentile estimate: 60% chance the outcome is above this value.",
    )
    percentile_60: float | None = Field(
        default=None,
        description="60th percentile estimate: 40% chance the outcome is above this value.",
    )
    percentile_80: float | None = Field(
        default=None,
        description="80th percentile estimate: 20% chance the outcome is above this value.",
    )
    percentile_90: float | None = Field(
        default=None,
        description="90th percentile estimate: 10% chance the outcome is above this value.",
    )

    # Mixture mode fields (scenario-based approach)
    components: list[ScenarioComponent] | None = Field(
        default=None,
        description=(
            "Scenario components for mixture distribution. "
            "Each component has a mode, bounds, and weight. "
            "If provided, takes precedence over percentile fields."
        ),
    )

    @model_validator(mode="after")
    def validate_has_distribution(self) -> Self:
        """Ensure either all percentiles OR components are provided."""
        has_components = self.components is not None and len(self.components) > 0
        has_all_percentiles = all(
            p is not None
            for p in [
                self.percentile_10,
                self.percentile_20,
                self.percentile_40,
                self.percentile_60,
                self.percentile_80,
                self.percentile_90,
            ]
        )

        if not has_components and not has_all_percentiles:
            raise ValueError(
                "NumericForecast requires either all 6 percentiles "
                "(percentile_10, percentile_20, percentile_40, percentile_60, "
                "percentile_80, percentile_90) OR components for mixture mode. "
                "Percentiles must be non-decreasing values."
            )

        # Validate percentiles are non-decreasing if all provided
        if has_all_percentiles:
            percentiles = [
                self.percentile_10,
                self.percentile_20,
                self.percentile_40,
                self.percentile_60,
                self.percentile_80,
                self.percentile_90,
            ]
            for i in range(len(percentiles) - 1):
                if percentiles[i] > percentiles[i + 1]:  # type: ignore[operator]
                    raise ValueError(
                        f"Percentiles must be non-decreasing. "
                        f"Got {percentiles[i]} > {percentiles[i + 1]} at indices {i} and {i + 1}."
                    )

        return self

    @property
    def uses_mixture_mode(self) -> bool:
        """Check if this forecast uses mixture mode."""
        return self.components is not None and len(self.components) > 0

    @computed_field
    @property
    def median(self) -> float | None:
        """Estimated median (interpolated from 40th and 60th percentiles)."""
        if self.uses_mixture_mode:
            # For mixture mode, compute weighted average of component modes
            if self.components:
                return sum(c.mode * c.weight for c in self.components)
            return None
        if self.percentile_40 is not None and self.percentile_60 is not None:
            return (self.percentile_40 + self.percentile_60) / 2
        return None

    @computed_field
    @property
    def confidence_interval(self) -> tuple[float, float] | None:
        """90% confidence interval (10th to 90th percentile)."""
        if self.uses_mixture_mode:
            # For mixture mode, use min lower and max upper across components
            if self.components:
                return (
                    min(c.lower_bound for c in self.components),
                    max(c.upper_bound for c in self.components),
                )
            return None
        if self.percentile_10 is not None and self.percentile_90 is not None:
            return (self.percentile_10, self.percentile_90)
        return None

    def get_percentile_dict(self) -> dict[int, float] | None:
        """Return percentiles as a dict for CDF generation.

        Returns None if using mixture mode (use components instead).
        """
        if self.uses_mixture_mode:
            return None
        if any(
            p is None
            for p in [
                self.percentile_10,
                self.percentile_20,
                self.percentile_40,
                self.percentile_60,
                self.percentile_80,
                self.percentile_90,
            ]
        ):
            return None
        return {
            10: self.percentile_10,  # type: ignore[dict-item]
            20: self.percentile_20,  # type: ignore[dict-item]
            40: self.percentile_40,  # type: ignore[dict-item]
            60: self.percentile_60,  # type: ignore[dict-item]
            80: self.percentile_80,  # type: ignore[dict-item]
            90: self.percentile_90,  # type: ignore[dict-item]
        }


class ForecastMeta(BaseModel):
    """Lightweight reference to process reflection.

    Full reflection is stored as a markdown file in the session directory.
    """

    meta_file_path: str | None = Field(
        default=None,
        description="Path to meta-reflection markdown file in session directory.",
    )
    tools_used_count: int = Field(
        default=0,
        description="Count of distinct tools used.",
    )
    subagents_used: list[str] = Field(
        default_factory=list,
        description="Subagents invoked during research.",
    )


class ForecastOutput(BaseModel):
    """Full output from a forecasting run, including metadata."""

    question_id: int = Field(description="Metaculus question ID (for submission API).")
    post_id: int = Field(description="Metaculus post ID (for URLs and comments).")
    question_title: str = Field(description="Title of the question.")
    question_type: str = Field(
        description="Type: binary, multiple_choice, numeric, etc."
    )

    # Core forecast fields (type-dependent)
    summary: str = Field(description="Brief explanation of the forecast.")
    factors: list[Factor] = Field(
        default_factory=list,
        description="Key pieces of evidence with their directional strength.",
    )
    logit: float | None = Field(
        default=None,
        description="For binary: synthesized log-odds estimate.",
    )
    probability: float | None = Field(
        default=None,
        description="For binary: Claude's final probability (may differ from sigmoid(logit)).",
    )
    probability_from_logit: float | None = Field(
        default=None,
        description="For binary: probability computed from logit via sigmoid (for auditing).",
    )
    probabilities: dict[str, float] | None = Field(
        default=None,
        description="For multiple choice: mapping of option to probability.",
    )
    median: float | None = Field(
        default=None,
        description="For numeric: median estimate.",
    )
    confidence_interval: tuple[float, float] | None = Field(
        default=None,
        description="For numeric: (lower, upper) 90% confidence interval.",
    )
    percentiles: dict[int, float] | None = Field(
        default=None,
        description="For numeric: percentile estimates (10, 20, 40, 60, 80, 90).",
    )
    cdf: list[float] | None = Field(
        default=None,
        description="For numeric/discrete: CDF for Metaculus submission.",
    )
    cdf_size: int | None = Field(
        default=None,
        description="Expected CDF size (201 for numeric, variable for discrete).",
    )

    # Metadata
    reasoning: str = Field(
        default="",
        description="The agent's full reasoning and analysis text.",
    )
    condensed_reasoning: str | None = Field(
        default=None,
        description="Sonnet-condensed narrative of the agent's research and reasoning.",
    )
    sources_consulted: list[str] = Field(
        default_factory=list,
        description="URLs and data sources the agent consulted.",
    )
    duration_seconds: float | None = Field(
        default=None,
        description="Time taken by the agent in seconds.",
    )
    cost_usd: float | None = Field(
        default=None,
        description="Cost of the agent run in USD.",
    )
    token_usage: TokenUsage | None = Field(
        default=None,
        description="Token usage: input_tokens, output_tokens, cache_read_tokens, etc.",
    )
    tool_metrics: dict[str, object] | None = Field(
        default=None,
        description="Tool call metrics: call counts, durations, error rates.",
    )
    meta: ForecastMeta | None = Field(
        default=None,
        description="Process reflection metadata.",
    )
    question_category: str | None = Field(
        default=None,
        description="Question category: predictive, definitional, meta, or measurement.",
    )
    retrodict_date: date | None = Field(
        default=None,
        description="If set, forecast was made in retrodict mode with data restricted to before this date.",
    )

    @staticmethod
    def classify_category(title: str, question_type: str) -> str:
        """Classify question into category based on title and type heuristics."""
        title_lower = title.lower()

        if "community prediction" in title_lower or "will the cp " in title_lower:
            return "meta"

        if question_type in ("numeric", "discrete"):
            return "measurement"

        if any(
            phrase in title_lower
            for phrase in ("has ", "does ", "did ", "is there", "are there", "qualify")
        ):
            return "definitional"

        return "predictive"
