"""Numeric distribution utilities for Metaculus CDF generation.

This module handles conversion of percentile estimates (e.g., 10th, 50th, 90th)
into the 201-point CDF format required by the Metaculus API for numeric and
discrete questions.

Also provides mixture distribution support for more flexible multi-scenario modeling.

Ported from to_port/main_with_no_framework.py with improved typing and structure.
"""

import logging
from collections import Counter
from typing import Self

import numpy as np
from pydantic import BaseModel, Field, field_validator, model_validator
from scipy import stats

logger = logging.getLogger(__name__)


class NumericDefaults:
    """Constants and helpers for numeric CDF generation."""

    DEFAULT_CDF_SIZE = 201  # Numeric questions use 201 points
    DEFAULT_INBOUND_OUTCOME_COUNT = DEFAULT_CDF_SIZE - 1
    MAX_NUMERIC_PMF_VALUE = 0.2

    @classmethod
    def get_max_pmf_value(
        cls, cdf_size: int, *, include_wiggle_room: bool = True
    ) -> float:
        """Calculate maximum allowed PMF value for a given CDF size.

        The cap depends on inboundOutcomeCount (0.2 if it is the default 200).
        Discrete questions have fewer points, so the cap scales accordingly.

        Args:
            cdf_size: Number of points in the CDF
            include_wiggle_room: If True, return 95% of the cap for safety margin

        Returns:
            Maximum allowed probability mass between adjacent CDF points
        """
        inbound_outcome_count = cdf_size - 1
        normal_cap = cls.MAX_NUMERIC_PMF_VALUE * (
            cls.DEFAULT_INBOUND_OUTCOME_COUNT / inbound_outcome_count
        )

        if include_wiggle_room:
            return normal_cap * 0.95
        return normal_cap


class Percentile(BaseModel):
    """A single point in a probability distribution.

    Represents "X% of outcomes are below value Y".

    Attributes:
        percentile: Cumulative probability (0 to 1). E.g., 0.9 means "90% are below this"
        value: The real-world value at this percentile
    """

    percentile: float = Field(
        description="Cumulative probability between 0 and 1 (e.g., 0.9 for 90th percentile)"
    )
    value: float = Field(description="The real-world value at this percentile")

    @model_validator(mode="after")
    def validate_percentile(self) -> Self:
        """Ensure percentile is a valid probability."""
        if self.percentile < 0 or self.percentile > 1:
            raise ValueError(
                f"Percentile must be between 0 and 1, got {self.percentile}"
            )
        if np.isnan(self.percentile):
            raise ValueError(f"Percentile must be a number, got {self.percentile}")
        return self


class NumericDistribution(BaseModel):
    """Converts percentile estimates to Metaculus-compatible CDF format.

    Takes a sparse set of percentile estimates (e.g., 10th, 50th, 90th) and
    generates a full 201-point CDF that satisfies Metaculus API requirements.

    Attributes:
        declared_percentiles: Sparse percentile estimates from the forecaster
        open_upper_bound: If True, outcomes can exceed the upper bound
        open_lower_bound: If True, outcomes can be below the lower bound
        upper_bound: Maximum value in the question's range
        lower_bound: Minimum value in the question's range
        zero_point: For log-scaled questions, the point where log scale anchors
        cdf_size: Number of CDF points (201 for numeric, fewer for discrete)
        standardize_cdf: If True, apply Metaculus standardization rules
        strict_validation: If True, apply all validation checks

    Example:
        >>> dist = NumericDistribution(
        ...     declared_percentiles=[
        ...         Percentile(percentile=0.1, value=100),
        ...         Percentile(percentile=0.5, value=150),
        ...         Percentile(percentile=0.9, value=250),
        ...     ],
        ...     open_upper_bound=True,
        ...     open_lower_bound=False,
        ...     upper_bound=500,
        ...     lower_bound=0,
        ...     zero_point=None,
        ... )
        >>> cdf = dist.get_cdf()
        >>> cdf_values = [p.percentile for p in cdf]  # 201-point CDF
    """

    declared_percentiles: list[Percentile]
    open_upper_bound: bool
    open_lower_bound: bool
    upper_bound: float
    lower_bound: float
    zero_point: float | None = None
    cdf_size: int | None = None  # None means use DEFAULT_CDF_SIZE (201)
    standardize_cdf: bool = True
    strict_validation: bool = True

    @model_validator(mode="after")
    def validate_distribution(self) -> Self:
        """Validate the distribution configuration."""
        self._check_percentiles_increasing()
        self._check_log_scaled_fields()

        if not self.strict_validation:
            return self

        self._check_percentile_spacing()

        if self.standardize_cdf:
            self._check_too_far_from_bounds(self.declared_percentiles)
        if self.standardize_cdf and len(self.declared_percentiles) == self.cdf_size:
            self._check_distribution_too_tall(self.declared_percentiles)

        self.declared_percentiles = self._check_and_update_repeating_values(
            self.declared_percentiles
        )
        return self

    def _check_percentiles_increasing(self) -> None:
        """Ensure percentiles and values are strictly increasing."""
        percentiles = self.declared_percentiles
        if len(percentiles) < 2:
            raise ValueError("NumericDistribution must have at least 2 percentiles")

        for i in range(len(percentiles) - 1):
            if percentiles[i].percentile >= percentiles[i + 1].percentile:
                raise ValueError("Percentiles must be in strictly increasing order")
            if percentiles[i].value > percentiles[i + 1].value:
                raise ValueError("Values must be in strictly increasing order")

    def _check_percentile_spacing(self) -> None:
        """Ensure percentiles aren't too close together."""
        percentiles = self.declared_percentiles
        for i in range(len(percentiles) - 1):
            spacing = abs(percentiles[i + 1].percentile - percentiles[i].percentile)
            if spacing < 5e-05:
                raise ValueError(
                    f"Percentiles at indices {i} and {i + 1} are too close. "
                    f"CDF must increase by at least 5e-05 at every step. "
                    f"Got {percentiles[i].percentile} and {percentiles[i + 1].percentile} "
                    f"at values {percentiles[i].value} and {percentiles[i + 1].value}."
                )

    def _check_log_scaled_fields(self) -> None:
        """Validate log-scaled question constraints."""
        if self.zero_point is not None and self.lower_bound <= self.zero_point:
            raise ValueError(
                f"Lower bound {self.lower_bound} must be greater than "
                f"zero point {self.zero_point} for log-scaled questions."
            )

        for percentile in self.declared_percentiles:
            if self.zero_point is not None and percentile.value < self.zero_point:
                raise ValueError(
                    f"Percentile value {percentile.value} is below zero point "
                    f"{self.zero_point}. Values below zero point are not supported."
                )

    def _check_and_update_repeating_values(
        self, percentiles: list[Percentile]
    ) -> list[Percentile]:
        """Handle repeated values by adding small offsets."""
        unique_value_count = Counter(p.value for p in percentiles)
        final_percentiles = []

        for percentile in percentiles:
            value = percentile.value
            count = unique_value_count[value]

            if count == 1:
                # Not repeated, keep as-is
                final_percentiles.append(percentile)
                continue

            # Handle repeated values with small offsets
            value_in_bounds = self.lower_bound < value < self.upper_bound
            value_above_bound = value >= self.upper_bound
            value_below_bound = value <= self.lower_bound
            epsilon = 1e-10

            if value_in_bounds:
                # Slightly smaller epsilon for values in bounds
                greater_epsilon = 1e-6
                modification = (1 - percentile.percentile) * greater_epsilon
                final_percentiles.append(
                    Percentile(
                        value=value - modification,
                        percentile=percentile.percentile,
                    )
                )
            elif value_above_bound:
                modification = epsilon * percentile.percentile
                final_percentiles.append(
                    Percentile(
                        value=self.upper_bound + modification,
                        percentile=percentile.percentile,
                    )
                )
            elif value_below_bound:
                modification = epsilon * (1 - percentile.percentile)
                final_percentiles.append(
                    Percentile(
                        value=self.lower_bound - modification,
                        percentile=percentile.percentile,
                    )
                )
            else:
                raise ValueError(
                    f"Unexpected state: value {value} repeated {count} times. "
                    f"Bounds: [{self.lower_bound}, {self.upper_bound}]"
                )

        return final_percentiles

    def _check_too_far_from_bounds(self, percentiles: list[Percentile]) -> None:
        """Ensure percentiles aren't completely outside the question range."""
        range_size = self.upper_bound - self.lower_bound
        wiggle_percent = 0.25
        wiggle_room = range_size * wiggle_percent

        upper_with_wiggle = self.upper_bound + wiggle_room
        lower_with_wiggle = self.lower_bound - wiggle_room

        within_bounds = [
            p for p in percentiles if lower_with_wiggle <= p.value <= upper_with_wiggle
        ]
        if len(within_bounds) == 0:
            raise ValueError(
                f"No percentiles within {wiggle_percent * 100}% of question range. "
                f"Range: [{self.lower_bound}, {self.upper_bound}]. "
                f"Percentiles: {percentiles}"
            )

        # Check for values far outside bounds
        max_buffer = range_size * 2
        far_outside = [
            p
            for p in percentiles
            if p.value < self.lower_bound - max_buffer
            or p.value > self.upper_bound + max_buffer
        ]
        if len(far_outside) > 0:
            raise ValueError(
                f"Some percentiles far exceed question bounds. "
                f"Range: [{self.lower_bound}, {self.upper_bound}]. "
                f"Far outliers: {far_outside}"
            )

    def _check_distribution_too_tall(self, cdf: list[Percentile]) -> None:
        """Ensure distribution isn't too concentrated (PMF too tall)."""
        if len(cdf) != self.cdf_size:
            raise ValueError(
                f"CDF size mismatch: expected {self.cdf_size}, got {len(cdf)}"
            )

        cap = NumericDefaults.get_max_pmf_value(len(cdf), include_wiggle_room=False)

        for i in range(len(cdf) - 1):
            pmf_value = cdf[i + 1].percentile - cdf[i].percentile
            if pmf_value > cap:
                raise ValueError(
                    f"Distribution too concentrated. PMF between values "
                    f"{cdf[i].value} and {cdf[i + 1].value} is {pmf_value:.4f}, "
                    f"exceeds max {cap:.4f}."
                )

    def get_cdf(self) -> list[Percentile]:
        """Generate full CDF from declared percentiles.

        Converts sparse percentile estimates into a full 201-point (or cdf_size-point)
        CDF that satisfies Metaculus API requirements.

        Returns:
            List of Percentile objects representing the full CDF.
            The percentile field of each contains the CDF height (y-value),
            and the value field contains the corresponding real-world value (x-value).
        """
        cdf_size = self.cdf_size or NumericDefaults.DEFAULT_CDF_SIZE

        continuous_cdf: list[float] = []
        cdf_xaxis: list[float] = []

        # Evaluate CDF at evenly-spaced locations
        cdf_eval_locations = [i / (cdf_size - 1) for i in range(cdf_size)]
        for location in cdf_eval_locations:
            continuous_cdf.append(self._get_cdf_at(location))
            cdf_xaxis.append(self._cdf_location_to_nominal_location(location))

        if self.standardize_cdf:
            continuous_cdf = self._standardize_cdf(continuous_cdf)

        percentiles = [
            Percentile(value=value, percentile=pct)
            for value, pct in zip(cdf_xaxis, continuous_cdf, strict=True)
        ]

        # Validate the generated CDF
        NumericDistribution(
            declared_percentiles=percentiles,
            open_upper_bound=self.open_upper_bound,
            open_lower_bound=self.open_lower_bound,
            upper_bound=self.upper_bound,
            lower_bound=self.lower_bound,
            zero_point=self.zero_point,
            standardize_cdf=self.standardize_cdf,
            strict_validation=True,
        )

        return percentiles

    def get_cdf_as_floats(self) -> list[float]:
        """Generate CDF and return just the percentile values.

        This is the format required by the Metaculus API's continuous_cdf field.

        Returns:
            List of floats representing CDF heights (y-values) at each point.
        """
        return [p.percentile for p in self.get_cdf()]

    @classmethod
    def _percentile_list_to_dict(
        cls, percentiles: list[Percentile], *, multiply_by_100: bool
    ) -> dict[float, float]:
        """Convert percentile list to dict mapping percentile -> value."""
        return {
            (p.percentile * 100 if multiply_by_100 else p.percentile): p.value
            for p in percentiles
        }

    @classmethod
    def _dict_to_percentile_list(
        cls, percentile_dict: dict[float, float], *, divide_by_100: bool
    ) -> list[Percentile]:
        """Convert dict to percentile list."""
        return [
            Percentile(
                percentile=pct / 100 if divide_by_100 else pct,
                value=value,
            )
            for pct, value in percentile_dict.items()
        ]

    def _add_explicit_upper_lower_bound_percentiles(
        self,
        input_percentiles: list[Percentile],
    ) -> list[Percentile]:
        """Add explicit boundary percentiles based on open/closed bounds."""
        range_max = self.upper_bound
        range_min = self.lower_bound
        range_size = abs(range_max - range_min)
        buffer = 1 if range_size > 100 else 0.01 * range_size

        return_percentiles = self._percentile_list_to_dict(
            input_percentiles, multiply_by_100=True
        )
        percentile_max = max(return_percentiles.keys())
        percentile_min = min(return_percentiles.keys())

        # Adjust values at bounds
        for pct, value in list(return_percentiles.items()):
            if not self.open_lower_bound and value <= range_min + buffer:
                return_percentiles[pct] = range_min + buffer
            if not self.open_upper_bound and value >= range_max - buffer:
                return_percentiles[pct] = range_max - buffer

        # Handle upper bound
        if self.open_upper_bound:
            if range_max > return_percentiles[percentile_max]:
                halfway = 100 - (0.5 * (100 - percentile_max))
                return_percentiles[halfway] = range_max
        else:
            return_percentiles[100] = range_max

        # Handle lower bound
        if self.open_lower_bound:
            if range_min < return_percentiles[percentile_min]:
                halfway = 0.5 * percentile_min
                return_percentiles[halfway] = range_min
        else:
            return_percentiles[0] = range_min

        sorted_percentiles = dict(sorted(return_percentiles.items()))
        return self._dict_to_percentile_list(sorted_percentiles, divide_by_100=True)

    def _nominal_location_to_cdf_location(self, nominal_value: float) -> float:
        """Convert real-world value to CDF x-axis location (0 to 1).

        Handles both linear and log-scaled questions.
        """
        range_max = self.upper_bound
        range_min = self.lower_bound
        zero_point = self.zero_point

        if zero_point is not None:
            # Log-scaled question
            deriv_ratio = (range_max - zero_point) / (range_min - zero_point)
            if nominal_value == zero_point:
                nominal_value += 1e-10  # Avoid log(0)
            unscaled_location = (
                np.log(
                    (nominal_value - range_min) * (deriv_ratio - 1)
                    + (range_max - range_min)
                )
                - np.log(range_max - range_min)
            ) / np.log(deriv_ratio)
        else:
            # Linear question
            unscaled_location = (nominal_value - range_min) / (range_max - range_min)

        return float(unscaled_location)

    def _cdf_location_to_nominal_location(self, cdf_location: float) -> float:
        """Convert CDF x-axis location (0 to 1) to real-world value.

        Inverse of _nominal_location_to_cdf_location.
        """
        range_max = self.upper_bound
        range_min = self.lower_bound
        zero_point = self.zero_point

        if zero_point is None:
            # Linear question
            scaled_location = range_min + (range_max - range_min) * cdf_location
        else:
            # Log-scaled question
            deriv_ratio = (range_max - zero_point) / (range_min - zero_point)
            scaled_location = range_min + (range_max - range_min) * (
                deriv_ratio**cdf_location - 1
            ) / (deriv_ratio - 1)

        if np.isnan(scaled_location):
            raise ValueError(f"Scaled location is NaN for CDF location {cdf_location}")
        return float(scaled_location)

    def _get_cdf_at(self, cdf_location: float) -> float:
        """Get CDF height at a given x-axis location via linear interpolation."""
        bounded_percentiles = self._add_explicit_upper_lower_bound_percentiles(
            self.declared_percentiles
        )

        # Build mapping of (cdf_location, percentile_height)
        location_to_height: list[tuple[float, float]] = []
        for p in bounded_percentiles:
            location = self._nominal_location_to_cdf_location(p.value)
            location_to_height.append((location, p.percentile))

        # Linear interpolation
        previous = location_to_height[0]
        for i in range(1, len(location_to_height)):
            current = location_to_height[i]
            epsilon = 1e-10
            if previous[0] - epsilon <= cdf_location <= current[0] + epsilon:
                # Interpolate
                result = previous[1] + (current[1] - previous[1]) * (
                    cdf_location - previous[0]
                ) / (current[0] - previous[0])
                if np.isnan(result):
                    raise ValueError(f"NaN result for CDF location {cdf_location}")
                return float(result)
            previous = current

        raise ValueError(f"CDF location {cdf_location} not found in range")

    def _standardize_cdf(self, cdf: list[float]) -> list[float]:
        """Apply Metaculus standardization rules to the CDF.

        See: https://metaculus.com/api/ "CDF generation details" section

        This:
        - Assigns no mass outside closed bounds
        - Assigns minimum mass outside open bounds
        - Ensures minimum increase between points (0.01 / 200)
        - Caps maximum growth to 0.2
        """
        cdf_array = np.array(cdf, dtype=np.float64)
        lower_open = self.open_lower_bound
        upper_open = self.open_upper_bound

        # Apply lower bound & enforce boundary values
        scale_lower_to = 0.0 if lower_open else cdf_array[0]
        scale_upper_to = 1.0 if upper_open else cdf_array[-1]
        rescaled_inbound_mass = scale_upper_to - scale_lower_to

        def apply_minimum(f: float, location: float) -> float:
            """Apply minimum offset based on bound configuration."""
            rescaled_f = (f - scale_lower_to) / rescaled_inbound_mass
            if lower_open and upper_open:
                return 0.988 * rescaled_f + 0.01 * location + 0.001
            elif lower_open:
                return 0.989 * rescaled_f + 0.01 * location + 0.001
            elif upper_open:
                return 0.989 * rescaled_f + 0.01 * location
            return 0.99 * rescaled_f + 0.01 * location

        for i in range(len(cdf_array)):
            cdf_array[i] = apply_minimum(cdf_array[i], i / (len(cdf_array) - 1))

        # Apply PMF cap in PMF space
        pmf = np.diff(cdf_array, prepend=0, append=1)
        cap = NumericDefaults.get_max_pmf_value(len(cdf_array))

        def cap_pmf(scale: float) -> np.ndarray:
            return np.concatenate(
                [pmf[:1], np.minimum(cap, scale * pmf[1:-1]), pmf[-1:]]
            )

        def capped_sum(scale: float) -> float:
            return float(cap_pmf(scale).sum())

        # Binary search for scale that makes capped sum = 1
        lo = hi = scale = 1.0
        while capped_sum(hi) < 1.0:
            hi *= 1.2

        for _ in range(100):
            scale = 0.5 * (lo + hi)
            s = capped_sum(scale)
            if s < 1.0:
                lo = scale
            else:
                hi = scale
            if s == 1.0 or (hi - lo) < 2e-5:
                break

        # Apply scale and renormalize
        pmf = cap_pmf(scale)
        inner_sum = pmf[1:-1].sum()
        if inner_sum > 0:
            pmf[1:-1] *= (cdf_array[-1] - cdf_array[0]) / inner_sum

        # Back to CDF space
        cdf_array = np.cumsum(pmf)[:-1]

        # Round to minimize floating point errors
        cdf_array = np.round(cdf_array, 10)
        return cdf_array.tolist()


def percentiles_to_cdf(
    percentile_values: dict[int, float],
    *,
    upper_bound: float,
    lower_bound: float,
    open_upper_bound: bool = False,
    open_lower_bound: bool = False,
    zero_point: float | None = None,
    cdf_size: int = 201,
) -> list[float]:
    """Convert percentile estimates to Metaculus CDF format.

    Convenience function for common use case.

    Args:
        percentile_values: Dict mapping percentile (10, 20, 50, etc.) to value
        upper_bound: Question's upper bound
        lower_bound: Question's lower bound
        open_upper_bound: Whether values can exceed upper_bound
        open_lower_bound: Whether values can be below lower_bound
        zero_point: For log-scaled questions, the log anchor point
        cdf_size: Number of CDF points (201 for numeric, fewer for discrete)

    Returns:
        List of 201 (or cdf_size) floats representing the CDF.

    Example:
        >>> cdf = percentiles_to_cdf(
        ...     {10: 100, 20: 120, 40: 150, 60: 180, 80: 220, 90: 280},
        ...     upper_bound=500,
        ...     lower_bound=0,
        ...     open_upper_bound=True,
        ... )
    """
    # Convert percentile keys from 0-100 to 0-1
    percentiles = [
        Percentile(percentile=pct / 100, value=value)
        for pct, value in sorted(percentile_values.items())
    ]

    dist = NumericDistribution(
        declared_percentiles=percentiles,
        open_upper_bound=open_upper_bound,
        open_lower_bound=open_lower_bound,
        upper_bound=upper_bound,
        lower_bound=lower_bound,
        zero_point=zero_point,
        cdf_size=cdf_size,
    )

    return dist.get_cdf_as_floats()


# --- Mixture Distribution Support ---


class DistributionComponent(BaseModel):
    """A single component in a mixture distribution.

    Each component represents a scenario with its own probability distribution.
    Components are combined with weights to form the final mixture.

    Attributes:
        scenario: Human-readable scenario name (e.g., "Base case", "Upside").
        mode: Most likely value (peak of distribution).
        lower_bound: 10th percentile estimate.
        upper_bound: 90th percentile estimate.
        weight: Weight in the mixture (all weights must sum to 1.0).
    """

    scenario: str = Field(
        description="Scenario name: 'Base case', 'Upside', 'Downside', etc."
    )
    mode: float = Field(description="Most likely value (peak of distribution).")
    lower_bound: float = Field(
        description="10th percentile: 90% chance outcome is above this."
    )
    upper_bound: float = Field(
        description="90th percentile: 10% chance outcome is above this."
    )
    weight: float = Field(ge=0.0, le=1.0, description="Weight in mixture (sum to 1.0).")

    @model_validator(mode="after")
    def validate_bounds(self) -> Self:
        """Ensure bounds are ordered correctly."""
        if self.lower_bound >= self.upper_bound:
            raise ValueError(
                f"lower_bound ({self.lower_bound}) must be less than upper_bound ({self.upper_bound})"
            )
        if not self.lower_bound <= self.mode <= self.upper_bound:
            raise ValueError(
                f"mode ({self.mode}) must be between lower_bound ({self.lower_bound}) "
                f"and upper_bound ({self.upper_bound})"
            )
        return self


class MixtureDistributionConfig(BaseModel):
    """Configuration for a mixture distribution forecast.

    Attributes:
        components: List of distribution components (scenarios).
        question_lower_bound: Question's minimum value.
        question_upper_bound: Question's maximum value.
        open_lower_bound: Whether values can go below the question's lower bound.
        open_upper_bound: Whether values can exceed the question's upper bound.
        zero_point: For log-scaled questions, the log anchor point.
        use_lognormal: If True, use log-normal distributions. If False, use normal.
    """

    components: list[DistributionComponent]
    question_lower_bound: float
    question_upper_bound: float
    open_lower_bound: bool = False
    open_upper_bound: bool = False
    zero_point: float | None = None
    use_lognormal: bool = False

    @field_validator("components")
    @classmethod
    def validate_weights_sum(
        cls, v: list[DistributionComponent]
    ) -> list[DistributionComponent]:
        """Ensure component weights sum to 1.0."""
        if not v:
            raise ValueError("At least one component is required")
        total_weight = sum(c.weight for c in v)
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Component weights must sum to 1.0, got {total_weight}")
        return v


def _fit_distribution_from_percentiles(
    mode: float,
    p10: float,
    p90: float,
    *,
    use_lognormal: bool = False,
) -> stats.rv_continuous | stats.rv_frozen:
    """Fit a scipy distribution from mode and percentile estimates.

    Uses a skew-normal distribution when mode is not centered,
    or a normal distribution when mode is approximately centered.
    For positive-only quantities, can use log-normal.

    Args:
        mode: Most likely value.
        p10: 10th percentile (90% above this).
        p90: 90th percentile (10% above this).
        use_lognormal: If True, fit a log-normal distribution.

    Returns:
        A frozen scipy distribution.
    """
    if use_lognormal and p10 > 0:
        # Log-normal: work in log space
        log_p10 = np.log(p10)
        log_p90 = np.log(p90)

        # For log-normal: p10 = exp(mu + sigma * z_0.1), p90 = exp(mu + sigma * z_0.9)
        z_90 = stats.norm.ppf(0.9)  # ~1.28
        sigma = (log_p90 - log_p10) / (2 * z_90)
        mu = (log_p10 + log_p90) / 2

        return stats.lognorm(s=sigma, scale=np.exp(mu))

    # Normal or skew-normal
    # For symmetric case, mu = mode, sigma = (p90 - p10) / (2 * z_90)
    z_90 = stats.norm.ppf(0.9)  # ~1.28
    sigma = (p90 - p10) / (2 * z_90)

    # Check if mode is centered (within 10% of median)
    midpoint = (p10 + p90) / 2
    skewness_ratio = (mode - midpoint) / (p90 - p10) if (p90 - p10) > 0 else 0

    if abs(skewness_ratio) < 0.1:
        # Approximately symmetric, use normal
        return stats.norm(loc=mode, scale=sigma)

    # Use skew-normal for asymmetric distributions
    # This is an approximation - proper fitting would require optimization
    # Skewness parameter alpha controls the skew direction
    alpha = -skewness_ratio * 5  # Scale skewness
    alpha = max(-10, min(10, alpha))  # Clamp to reasonable range

    # Adjust location and scale to match percentiles approximately
    return stats.skewnorm(a=alpha, loc=mode, scale=sigma)


def mixture_components_to_cdf(
    config: MixtureDistributionConfig,
    cdf_size: int = 201,
) -> list[float]:
    """Convert mixture distribution components to Metaculus CDF format.

    Creates a weighted mixture of distributions from the component specifications,
    evaluates the mixture CDF at evenly-spaced points, and applies Metaculus
    standardization rules.

    Args:
        config: Mixture distribution configuration.
        cdf_size: Number of CDF points (201 for numeric, fewer for discrete).

    Returns:
        List of floats representing the CDF (same format as percentiles_to_cdf).

    Example:
        >>> config = MixtureDistributionConfig(
        ...     components=[
        ...         DistributionComponent(
        ...             scenario="Base case",
        ...             mode=150,
        ...             lower_bound=100,
        ...             upper_bound=200,
        ...             weight=0.6,
        ...         ),
        ...         DistributionComponent(
        ...             scenario="Upside",
        ...             mode=250,
        ...             lower_bound=200,
        ...             upper_bound=350,
        ...             weight=0.4,
        ...         ),
        ...     ],
        ...     question_lower_bound=0,
        ...     question_upper_bound=500,
        ...     open_upper_bound=True,
        ... )
        >>> cdf = mixture_components_to_cdf(config)
    """
    # Fit distributions for each component
    distributions = []
    weights = []
    for comp in config.components:
        dist = _fit_distribution_from_percentiles(
            mode=comp.mode,
            p10=comp.lower_bound,
            p90=comp.upper_bound,
            use_lognormal=config.use_lognormal,
        )
        distributions.append(dist)
        weights.append(comp.weight)

    # Evaluate CDF at evenly-spaced points across the question range
    lower = config.question_lower_bound
    upper = config.question_upper_bound

    if config.zero_point is not None:
        # Log-scaled question: use log-spaced evaluation points
        deriv_ratio = (upper - config.zero_point) / (lower - config.zero_point)
        locations = np.linspace(0, 1, cdf_size)
        x_values = lower + (upper - lower) * (deriv_ratio**locations - 1) / (
            deriv_ratio - 1
        )
    else:
        # Linear question: use linearly-spaced points
        x_values = np.linspace(lower, upper, cdf_size)

    # Compute mixture CDF at each point
    mixture_cdf = np.zeros(cdf_size)
    for dist, weight in zip(distributions, weights, strict=True):
        mixture_cdf += weight * dist.cdf(x_values)

    # Convert to percentiles for standardization via NumericDistribution
    # Sample enough percentiles to capture the distribution shape
    sampled_percentiles = []
    for i, (x, cdf_val) in enumerate(zip(x_values, mixture_cdf, strict=True)):
        if i % 20 == 0 or i == cdf_size - 1:  # Sample every 20th point plus endpoints
            sampled_percentiles.append(
                Percentile(percentile=float(cdf_val), value=float(x))
            )

    # Ensure percentiles are valid (monotonically increasing)
    cleaned_percentiles = []
    prev_pct = -1e-10
    for p in sampled_percentiles:
        if p.percentile > prev_pct:
            cleaned_percentiles.append(p)
            prev_pct = p.percentile

    if len(cleaned_percentiles) < 2:
        logger.warning("Mixture CDF degenerate, falling back to uniform")
        cleaned_percentiles = [
            Percentile(percentile=0.0, value=lower),
            Percentile(percentile=1.0, value=upper),
        ]

    # Use NumericDistribution for standardization
    try:
        dist = NumericDistribution(
            declared_percentiles=cleaned_percentiles,
            open_upper_bound=config.open_upper_bound,
            open_lower_bound=config.open_lower_bound,
            upper_bound=upper,
            lower_bound=lower,
            zero_point=config.zero_point,
            cdf_size=cdf_size,
            standardize_cdf=True,
            strict_validation=False,  # More lenient for mixture CDFs
        )
        return dist.get_cdf_as_floats()
    except ValueError as e:
        logger.warning("NumericDistribution failed for mixture CDF: %s", e)
        # Fallback: return the raw mixture CDF clamped to [0, 1]
        clamped = np.clip(mixture_cdf, 0.0, 1.0)
        # Apply basic monotonicity fix
        for i in range(1, len(clamped)):
            if clamped[i] < clamped[i - 1]:
                clamped[i] = clamped[i - 1] + 1e-6
        return clamped.tolist()
