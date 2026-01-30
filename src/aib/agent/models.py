"""Pydantic models for forecasting."""

import math
from datetime import date

from pydantic import BaseModel, Field, computed_field


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
    date: date | None = Field(default=None, description="When it happened.")
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


class QuestionLinkerOutput(BaseModel):
    """Output from the question-linker subagent."""

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


class NumericForecast(BaseModel):
    """Forecast for numeric questions.

    Provides percentile estimates that are converted to a 201-point CDF
    for Metaculus submission. The agent outputs sparse percentiles (10th, 20th,
    40th, 60th, 80th, 90th) and the system interpolates to generate the full CDF.
    """

    summary: str = Field(
        description="Brief explanation of the forecast and the key reasoning behind it."
    )
    factors: list[Factor] = Field(
        default_factory=list,
        description="Key pieces of evidence that influenced the estimate.",
    )
    percentile_10: float = Field(
        description="10th percentile estimate: 90% chance the outcome is above this value."
    )
    percentile_20: float = Field(
        description="20th percentile estimate: 80% chance the outcome is above this value."
    )
    percentile_40: float = Field(
        description="40th percentile estimate: 60% chance the outcome is above this value."
    )
    percentile_60: float = Field(
        description="60th percentile estimate: 40% chance the outcome is above this value."
    )
    percentile_80: float = Field(
        description="80th percentile estimate: 20% chance the outcome is above this value."
    )
    percentile_90: float = Field(
        description="90th percentile estimate: 10% chance the outcome is above this value."
    )

    @computed_field
    @property
    def median(self) -> float:
        """Estimated median (interpolated from 40th and 60th percentiles)."""
        return (self.percentile_40 + self.percentile_60) / 2

    @computed_field
    @property
    def confidence_interval(self) -> tuple[float, float]:
        """90% confidence interval (10th to 90th percentile)."""
        return (self.percentile_10, self.percentile_90)

    def get_percentile_dict(self) -> dict[int, float]:
        """Return percentiles as a dict for CDF generation."""
        return {
            10: self.percentile_10,
            20: self.percentile_20,
            40: self.percentile_40,
            60: self.percentile_60,
            80: self.percentile_80,
            90: self.percentile_90,
        }


class ForecastOutput(BaseModel):
    """Full output from a forecasting run, including metadata."""

    question_id: int = Field(description="Metaculus question/post ID.")
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
        description="For numeric: 201-point CDF for Metaculus submission.",
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
