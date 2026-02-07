"""Pydantic models for forecasting."""

import math
import re
from datetime import date, datetime, timedelta
from typing import Self, TypedDict

from pydantic import BaseModel, Field, computed_field, model_validator
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


class Factor(BaseModel):
    """A piece of evidence that influences the forecast."""

    description: str = Field(description="What this evidence is and why it matters.")
    logit: float = Field(
        description=(
            "Strength and direction of this evidence. "
            "Positive = toward Yes, negative = toward No. "
            "Scale: ±0.5 mild, ±1.0 moderate, ±2.0 strong, ±3.0 very strong."
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

    @computed_field
    @property
    def effective_logit(self) -> float:
        """The logit value adjusted for confidence."""
        return self.logit * self.confidence


# --- Subagent Output Models ---


class Source(BaseModel):
    """A cited source from research."""

    title: str = Field(description="Title or description of the source.")
    url: str = Field(description="URL of the source.")
    published_date: date | None = Field(
        default=None, description="Publication date if known."
    )
    relevance: str | None = Field(
        default=None, description="Why this source is relevant."
    )


class KeyFactor(BaseModel):
    """A key factor identified during research."""

    text: str = Field(
        description="Specific statement with numbers/dates/quotes when available."
    )
    factor_type: str = Field(description="Type: 'base_rate', 'pro', or 'con'.")
    citation: str = Field(description="Source citation in [Name](url) format.")
    source_publish_date: date | None = Field(
        default=None, description="When the source was published."
    )
    score: float = Field(
        description="Overall quality score based on recency, relevance, etc."
    )


class BaseRateEstimate(BaseModel):
    """A historical base rate estimate."""

    historical_rate: float = Field(description="The calculated historical rate.")
    numerator_count: int = Field(description="Number of events (hits).")
    numerator_definition: str = Field(description="What counts as a hit.")
    denominator_count: int = Field(description="Size of reference class.")
    denominator_definition: str = Field(description="What the denominator represents.")
    denominator_type: str = Field(description="'PER_DAY' or 'PER_EVENT'.")
    date_range_start: date = Field(description="Start of analysis period.")
    date_range_end: date = Field(description="End of analysis period.")
    caveats: list[str] = Field(
        default_factory=list, description="Reasons this rate may not apply."
    )


class EnumeratedItem(BaseModel):
    """An item from a niche list enumeration."""

    item_name: str = Field(description="Short identifier for the item.")
    description: str = Field(description="Context: year, situation, details.")
    is_valid: bool = Field(description="Whether this item passes fact-checking.")
    citation: str = Field(description="Source proving validity.")


class DeepResearchOutput(BaseModel):
    """Output from the deep-researcher subagent."""

    base_rate: BaseRateEstimate | None = Field(
        default=None, description="Base rate estimate if applicable."
    )
    key_factors: list[KeyFactor] = Field(
        default_factory=list, description="PRO/CON factors with scores."
    )
    enumerated_items: list[EnumeratedItem] | None = Field(
        default=None, description="Enumerated items if niche list was requested."
    )
    sources: list[Source] = Field(
        default_factory=list, description="All sources consulted."
    )
    markdown_report: str = Field(
        description="Full report with citations in markdown format."
    )


class Precedent(BaseModel):
    """A historical precedent for comparison."""

    event: str = Field(description="What happened.")
    event_date: date | None = Field(default=None, description="When it happened.")
    outcome: str = Field(description="How it resolved.")
    similarity_score: float = Field(
        description="How similar to the current question (0-1)."
    )
    source: str = Field(description="Source citation.")


class PrecedentFinderOutput(BaseModel):
    """Output from the precedent-finder subagent."""

    precedents: list[Precedent] = Field(
        default_factory=list, description="Similar historical events."
    )
    reference_class: str = Field(
        description="What category these precedents belong to."
    )
    base_rate_from_precedents: float | None = Field(
        default=None, description="Base rate derived from precedent outcomes."
    )
    caveats: list[str] = Field(
        default_factory=list, description="Why precedents may not apply."
    )
    markdown_report: str = Field(description="Full report with precedent analysis.")


class EdgeCase(BaseModel):
    """A potential edge case in resolution criteria."""

    scenario: str = Field(description="What could happen.")
    resolution: str = Field(description="How this would likely resolve.")
    likelihood: str = Field(description="How likely this edge case is.")


class Ambiguity(BaseModel):
    """Unclear language in resolution criteria."""

    phrase: str = Field(description="The ambiguous text.")
    interpretation_a: str = Field(description="One possible interpretation.")
    interpretation_b: str = Field(description="Another possible interpretation.")
    recommendation: str = Field(description="Which interpretation seems more likely.")


class ResolutionAnalystOutput(BaseModel):
    """Output from the resolution-analyst subagent."""

    resolution_criteria_parsed: str = Field(
        description="Plain English summary of what must happen for resolution."
    )
    edge_cases: list[EdgeCase] = Field(
        default_factory=list,
        description="Scenarios that could resolve unexpectedly.",
    )
    ambiguities: list[Ambiguity] = Field(
        default_factory=list, description="Unclear language in criteria."
    )
    clarifying_questions: list[str] = Field(
        default_factory=list, description="Questions to ask the question author."
    )
    likely_resolution_source: str = Field(
        description="Where the resolution will likely come from."
    )
    markdown_report: str = Field(description="Full analysis of resolution criteria.")


class FermiEstimateOutput(BaseModel):
    """Output from the estimator subagent."""

    facts: list[str] = Field(description="Facts with [citation](url) format.")
    reasoning_steps: list[str] = Field(
        description="Step-by-step calculation reasoning."
    )
    answer: int | float = Field(description="Final estimate.")
    confidence_range_low: float = Field(description="Low end of confidence range.")
    confidence_range_high: float = Field(description="High end of confidence range.")
    markdown_report: str = Field(description="Full estimation with steps.")


class LinkedQuestion(BaseModel):
    """A related forecasting question from another platform."""

    title: str = Field(description="Question or market title.")
    probability: float | None = Field(
        default=None, description="Current probability/price."
    )
    volume: float | None = Field(
        default=None, description="Trading volume if available."
    )
    relevance: str = Field(description="Why this question is related.")
    url: str = Field(description="URL to the question/market.")
    platform: str = Field(description="Platform name: metaculus, manifold, polymarket.")


class CoherenceLink(BaseModel):
    """A coherence link between Metaculus questions."""

    post_id: int = Field(description="Related question's post ID.")
    direction: str = Field(description="Relationship type: implies, contradicts, etc.")
    strength: float = Field(description="Strength of relationship (0-1).")


class RelevantNews(BaseModel):
    """News that may affect the question and related questions."""

    headline: str = Field(description="News headline.")
    source: str = Field(description="News source.")
    relevance: str = Field(description="Why this news is relevant.")


class MarketResearcherOutput(BaseModel):
    """Output from the market-researcher subagent.

    This model captures the structured output when using the market-researcher
    subagent to find related questions and market signals across platforms.
    """

    metaculus_questions: list[LinkedQuestion] = Field(
        default_factory=list, description="Related Metaculus questions."
    )
    manifold_markets: list[LinkedQuestion] = Field(
        default_factory=list, description="Related Manifold markets."
    )
    polymarket_markets: list[LinkedQuestion] = Field(
        default_factory=list, description="Related Polymarket markets."
    )
    coherence_links: list[CoherenceLink] = Field(
        default_factory=list, description="Metaculus coherence links."
    )
    relevant_news: list[RelevantNews] = Field(
        default_factory=list, description="Recent news affecting related questions."
    )
    markdown_summary: str = Field(
        description="Brief summary of related questions and market signals."
    )


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
                "Percentiles must be strictly increasing values."
            )

        # Validate percentiles are strictly increasing if all provided
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
                if percentiles[i] >= percentiles[i + 1]:  # type: ignore[operator]
                    raise ValueError(
                        f"Percentiles must be strictly increasing. "
                        f"Got {percentiles[i]} >= {percentiles[i + 1]} at indices {i} and {i + 1}."
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
    sources_consulted: list[str] = Field(
        default_factory=list,
        description="URLs or search queries the agent consulted.",
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
    retrodict_date: date | None = Field(
        default=None,
        description="If set, forecast was made in retrodict mode with data restricted to before this date.",
    )
