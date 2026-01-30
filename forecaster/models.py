"""Pydantic models for forecasting."""

import math

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
    """Forecast for numeric questions."""

    summary: str = Field(
        description="Brief explanation of the forecast and the key reasoning behind it."
    )
    factors: list[Factor] = Field(
        default_factory=list,
        description="Key pieces of evidence that influenced the estimate.",
    )
    median: float = Field(
        description="Median estimate (50th percentile) for the numeric value."
    )
    confidence_interval: tuple[float, float] = Field(
        description=(
            "(lower, upper) bounds of 90% confidence interval. "
            "5th percentile to 95th percentile."
        )
    )


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
