"""Tests for aib.agent.numeric."""

import pytest

from aib.agent.numeric import (
    DistributionComponent,
    MixtureDistributionConfig,
    NumericDefaults,
    NumericDistribution,
    Percentile,
    mixture_components_to_cdf,
    percentiles_to_cdf,
)


class TestPercentile:
    """Tests for the Percentile model."""

    def test_valid_percentile(self) -> None:
        """Valid percentile is accepted."""
        p = Percentile(percentile=0.5, value=100.0)
        assert p.percentile == 0.5
        assert p.value == 100.0

    def test_percentile_must_be_between_0_and_1(self) -> None:
        """Percentile must be in [0, 1] range."""
        with pytest.raises(ValueError, match="between 0 and 1"):
            Percentile(percentile=1.5, value=100.0)

        with pytest.raises(ValueError, match="between 0 and 1"):
            Percentile(percentile=-0.1, value=100.0)

    def test_boundary_percentiles_valid(self) -> None:
        """Boundary percentiles (0 and 1) are valid."""
        p0 = Percentile(percentile=0.0, value=0.0)
        p1 = Percentile(percentile=1.0, value=100.0)
        assert p0.percentile == 0.0
        assert p1.percentile == 1.0


class TestNumericDefaults:
    """Tests for NumericDefaults constants and helpers."""

    def test_default_cdf_size(self) -> None:
        """Default CDF size is 201."""
        assert NumericDefaults.DEFAULT_CDF_SIZE == 201

    def test_get_max_pmf_value_default_size(self) -> None:
        """Max PMF value for default size (201) is 0.2 * 0.95."""
        expected = 0.2 * 0.95
        actual = NumericDefaults.get_max_pmf_value(201, include_wiggle_room=True)
        assert actual == pytest.approx(expected)

    def test_get_max_pmf_value_without_wiggle_room(self) -> None:
        """Max PMF value without wiggle room is exactly 0.2."""
        actual = NumericDefaults.get_max_pmf_value(201, include_wiggle_room=False)
        assert actual == pytest.approx(0.2)

    def test_get_max_pmf_value_scales_with_cdf_size(self) -> None:
        """Max PMF scales inversely with CDF size."""
        # Smaller CDF = higher max PMF
        small_cdf = NumericDefaults.get_max_pmf_value(51, include_wiggle_room=False)
        large_cdf = NumericDefaults.get_max_pmf_value(201, include_wiggle_room=False)

        # 51 points = 50 intervals, 201 points = 200 intervals
        # Cap scales as 200/50 = 4x for smaller CDF
        assert small_cdf == pytest.approx(large_cdf * 4)


class TestNumericDistribution:
    """Tests for NumericDistribution CDF generation."""

    def test_requires_at_least_two_percentiles(self) -> None:
        """Distribution requires at least 2 percentiles."""
        with pytest.raises(ValueError, match="at least 2 percentiles"):
            NumericDistribution(
                declared_percentiles=[
                    Percentile(percentile=0.5, value=100.0),
                ],
                open_upper_bound=True,
                open_lower_bound=True,
                upper_bound=200.0,
                lower_bound=0.0,
            )

    def test_percentiles_must_be_increasing(self) -> None:
        """Percentiles must be in strictly increasing order."""
        with pytest.raises(ValueError, match="strictly increasing"):
            NumericDistribution(
                declared_percentiles=[
                    Percentile(percentile=0.5, value=100.0),
                    Percentile(percentile=0.3, value=50.0),  # Decreasing percentile
                ],
                open_upper_bound=True,
                open_lower_bound=True,
                upper_bound=200.0,
                lower_bound=0.0,
            )

    def test_values_must_not_decrease(self) -> None:
        """Values must be monotonically increasing."""
        with pytest.raises(ValueError, match="strictly increasing"):
            NumericDistribution(
                declared_percentiles=[
                    Percentile(percentile=0.3, value=150.0),
                    Percentile(percentile=0.5, value=100.0),  # Value decreases
                ],
                open_upper_bound=True,
                open_lower_bound=True,
                upper_bound=200.0,
                lower_bound=0.0,
            )

    def test_log_scaled_values_must_be_above_zero_point(self) -> None:
        """For log-scaled questions, values must be above zero_point."""
        with pytest.raises(ValueError, match="below zero point"):
            NumericDistribution(
                declared_percentiles=[
                    Percentile(percentile=0.1, value=0.5),  # Below zero_point of 1.0
                    Percentile(percentile=0.9, value=100.0),
                ],
                open_upper_bound=True,
                open_lower_bound=False,
                upper_bound=1000.0,
                lower_bound=2.0,  # Must be > zero_point to test percentile validation
                zero_point=1.0,
            )

    def test_log_scaled_lower_bound_above_zero_point(self) -> None:
        """Lower bound must be greater than zero point."""
        with pytest.raises(ValueError, match="must be greater than zero point"):
            NumericDistribution(
                declared_percentiles=[
                    Percentile(percentile=0.1, value=10.0),
                    Percentile(percentile=0.9, value=100.0),
                ],
                open_upper_bound=True,
                open_lower_bound=False,
                upper_bound=1000.0,
                lower_bound=0.5,
                zero_point=1.0,  # Lower bound <= zero_point
            )

    def test_get_cdf_returns_correct_size(self) -> None:
        """CDF has correct number of points."""
        dist = NumericDistribution(
            declared_percentiles=[
                Percentile(percentile=0.1, value=100.0),
                Percentile(percentile=0.5, value=200.0),
                Percentile(percentile=0.9, value=300.0),
            ],
            open_upper_bound=True,
            open_lower_bound=True,
            upper_bound=500.0,
            lower_bound=0.0,
        )
        cdf = dist.get_cdf()
        assert len(cdf) == 201

    def test_get_cdf_respects_custom_size(self) -> None:
        """CDF respects custom cdf_size parameter."""
        dist = NumericDistribution(
            declared_percentiles=[
                Percentile(percentile=0.1, value=100.0),
                Percentile(percentile=0.9, value=300.0),
            ],
            open_upper_bound=True,
            open_lower_bound=True,
            upper_bound=500.0,
            lower_bound=0.0,
            cdf_size=51,
        )
        cdf = dist.get_cdf()
        assert len(cdf) == 51

    def test_cdf_is_monotonically_increasing(self) -> None:
        """CDF values are monotonically increasing."""
        dist = NumericDistribution(
            declared_percentiles=[
                Percentile(percentile=0.1, value=100.0),
                Percentile(percentile=0.5, value=200.0),
                Percentile(percentile=0.9, value=300.0),
            ],
            open_upper_bound=True,
            open_lower_bound=True,
            upper_bound=500.0,
            lower_bound=0.0,
        )
        cdf = dist.get_cdf()

        for i in range(len(cdf) - 1):
            assert cdf[i].percentile <= cdf[i + 1].percentile

    def test_cdf_endpoints_respect_closed_bounds(self) -> None:
        """Closed bounds have CDF values at 0 and 1 at the bounds."""
        dist = NumericDistribution(
            declared_percentiles=[
                Percentile(percentile=0.1, value=50.0),
                Percentile(percentile=0.5, value=150.0),
                Percentile(percentile=0.9, value=250.0),
            ],
            open_upper_bound=False,  # Closed upper
            open_lower_bound=False,  # Closed lower
            upper_bound=300.0,
            lower_bound=0.0,
        )
        cdf = dist.get_cdf()

        # First point should be at lower bound with CDF near 0
        assert cdf[0].value == pytest.approx(0.0)
        # Last point should be at upper bound with CDF near 1
        assert cdf[-1].value == pytest.approx(300.0)

    def test_get_cdf_as_floats(self) -> None:
        """get_cdf_as_floats returns just the CDF values."""
        dist = NumericDistribution(
            declared_percentiles=[
                Percentile(percentile=0.1, value=100.0),
                Percentile(percentile=0.9, value=300.0),
            ],
            open_upper_bound=True,
            open_lower_bound=True,
            upper_bound=500.0,
            lower_bound=0.0,
        )
        cdf_floats = dist.get_cdf_as_floats()

        assert isinstance(cdf_floats, list)
        assert all(isinstance(v, float) for v in cdf_floats)
        assert len(cdf_floats) == 201
        assert all(0 <= v <= 1 for v in cdf_floats)


class TestPercentilesToCdf:
    """Tests for the percentiles_to_cdf convenience function."""

    def test_basic_usage(self, sample_percentiles: dict[int, float]) -> None:
        """Basic usage with sample percentiles."""
        cdf = percentiles_to_cdf(
            sample_percentiles,
            upper_bound=500.0,
            lower_bound=0.0,
            open_upper_bound=True,
        )

        assert len(cdf) == 201
        assert all(0 <= v <= 1 for v in cdf)

    def test_returns_monotonic_cdf(self, sample_percentiles: dict[int, float]) -> None:
        """Returned CDF is monotonically increasing."""
        cdf = percentiles_to_cdf(
            sample_percentiles,
            upper_bound=500.0,
            lower_bound=0.0,
            open_upper_bound=True,
        )

        for i in range(len(cdf) - 1):
            assert cdf[i] <= cdf[i + 1]

    def test_custom_cdf_size(self, sample_percentiles: dict[int, float]) -> None:
        """Respects custom CDF size for discrete questions."""
        cdf = percentiles_to_cdf(
            sample_percentiles,
            upper_bound=500.0,
            lower_bound=0.0,
            cdf_size=51,
        )

        assert len(cdf) == 51

    def test_log_scaled_question(self) -> None:
        """Handles log-scaled questions with zero_point."""
        cdf = percentiles_to_cdf(
            {10: 10.0, 20: 20.0, 40: 50.0, 60: 100.0, 80: 500.0, 90: 1000.0},
            upper_bound=10000.0,
            lower_bound=1.0,
            zero_point=0.0,
            open_upper_bound=True,
        )

        assert len(cdf) == 201
        assert all(0 <= v <= 1 for v in cdf)


class TestDistributionComponent:
    """Tests for DistributionComponent validation."""

    def test_valid_component(self) -> None:
        """Valid component is accepted."""
        comp = DistributionComponent(
            scenario="Base case",
            mode=150.0,
            lower_bound=100.0,
            upper_bound=200.0,
            weight=0.6,
        )
        assert comp.mode == 150.0

    def test_lower_less_than_upper(self) -> None:
        """lower_bound must be less than upper_bound."""
        with pytest.raises(ValueError, match="lower_bound.*must be less than"):
            DistributionComponent(
                scenario="Bad",
                mode=150.0,
                lower_bound=200.0,
                upper_bound=100.0,
                weight=0.5,
            )

    def test_mode_within_bounds(self) -> None:
        """mode must be within [lower_bound, upper_bound]."""
        with pytest.raises(ValueError, match="mode.*must be between"):
            DistributionComponent(
                scenario="Bad",
                mode=50.0,  # Below lower_bound
                lower_bound=100.0,
                upper_bound=200.0,
                weight=0.5,
            )


class TestMixtureDistributionConfig:
    """Tests for MixtureDistributionConfig validation."""

    def test_valid_config(self) -> None:
        """Valid config is accepted."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="Base",
                    mode=150.0,
                    lower_bound=100.0,
                    upper_bound=200.0,
                    weight=0.6,
                ),
                DistributionComponent(
                    scenario="Upside",
                    mode=250.0,
                    lower_bound=200.0,
                    upper_bound=350.0,
                    weight=0.4,
                ),
            ],
            question_lower_bound=0.0,
            question_upper_bound=500.0,
        )
        assert len(config.components) == 2

    def test_requires_at_least_one_component(self) -> None:
        """At least one component is required."""
        with pytest.raises(ValueError, match="At least one component"):
            MixtureDistributionConfig(
                components=[],
                question_lower_bound=0.0,
                question_upper_bound=500.0,
            )

    def test_weights_must_sum_to_one(self) -> None:
        """Component weights must sum to 1.0."""
        with pytest.raises(ValueError, match="weights must sum to 1.0"):
            MixtureDistributionConfig(
                components=[
                    DistributionComponent(
                        scenario="A",
                        mode=100.0,
                        lower_bound=50.0,
                        upper_bound=150.0,
                        weight=0.3,
                    ),
                    DistributionComponent(
                        scenario="B",
                        mode=200.0,
                        lower_bound=150.0,
                        upper_bound=250.0,
                        weight=0.3,  # Total = 0.6, not 1.0
                    ),
                ],
                question_lower_bound=0.0,
                question_upper_bound=300.0,
            )


class TestMixtureComponentsToCdf:
    """Tests for mixture_components_to_cdf function."""

    def test_basic_mixture(self) -> None:
        """Basic mixture distribution generates valid CDF."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="Base",
                    mode=150.0,
                    lower_bound=100.0,
                    upper_bound=200.0,
                    weight=0.6,
                ),
                DistributionComponent(
                    scenario="Upside",
                    mode=250.0,
                    lower_bound=200.0,
                    upper_bound=350.0,
                    weight=0.4,
                ),
            ],
            question_lower_bound=0.0,
            question_upper_bound=500.0,
            open_upper_bound=True,
        )

        cdf = mixture_components_to_cdf(config)

        assert len(cdf) == 201
        assert all(0 <= v <= 1 for v in cdf)

    def test_mixture_is_monotonic(self) -> None:
        """Mixture CDF is monotonically increasing."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="Low",
                    mode=50.0,
                    lower_bound=20.0,
                    upper_bound=100.0,
                    weight=0.3,
                ),
                DistributionComponent(
                    scenario="High",
                    mode=200.0,
                    lower_bound=150.0,
                    upper_bound=280.0,
                    weight=0.7,
                ),
            ],
            question_lower_bound=0.0,
            question_upper_bound=300.0,
        )

        cdf = mixture_components_to_cdf(config)

        for i in range(len(cdf) - 1):
            assert cdf[i] <= cdf[i + 1] + 1e-9  # Small tolerance for floating point

    def test_single_component_mixture(self) -> None:
        """Single component mixture works."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="Only",
                    mode=150.0,
                    lower_bound=100.0,
                    upper_bound=200.0,
                    weight=1.0,
                ),
            ],
            question_lower_bound=0.0,
            question_upper_bound=300.0,
        )

        cdf = mixture_components_to_cdf(config)
        assert len(cdf) == 201

    def test_custom_cdf_size_mixture(self) -> None:
        """Mixture respects custom CDF size."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="A",
                    mode=100.0,
                    lower_bound=50.0,
                    upper_bound=150.0,
                    weight=1.0,
                ),
            ],
            question_lower_bound=0.0,
            question_upper_bound=200.0,
        )

        cdf = mixture_components_to_cdf(config, cdf_size=51)
        assert len(cdf) == 51

    def test_lognormal_mixture(self) -> None:
        """Mixture with log-normal distributions works."""
        config = MixtureDistributionConfig(
            components=[
                DistributionComponent(
                    scenario="Base",
                    mode=100.0,
                    lower_bound=50.0,
                    upper_bound=200.0,
                    weight=1.0,
                ),
            ],
            question_lower_bound=1.0,
            question_upper_bound=1000.0,
            use_lognormal=True,
        )

        cdf = mixture_components_to_cdf(config)
        assert len(cdf) == 201
        assert all(0 <= v <= 1 for v in cdf)
