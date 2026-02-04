"""Tests for aib.agent.models."""

import math
from datetime import datetime

import pytest
import zoneinfo

from aib.agent.models import (
    CreditExhaustedError,
    Factor,
    Forecast,
    MultipleChoiceForecast,
    NumericForecast,
    ScenarioComponent,
)


class TestFactor:
    """Tests for the Factor model."""

    def test_effective_logit_with_full_confidence(self) -> None:
        """Effective logit equals raw logit when confidence is 1.0."""
        factor = Factor(description="Test factor", logit=2.0, confidence=1.0)
        assert factor.effective_logit == 2.0

    def test_effective_logit_with_partial_confidence(self) -> None:
        """Effective logit is scaled by confidence."""
        factor = Factor(description="Test factor", logit=2.0, confidence=0.5)
        assert factor.effective_logit == 1.0

    def test_effective_logit_with_zero_confidence(self) -> None:
        """Effective logit is zero when confidence is zero."""
        factor = Factor(description="Test factor", logit=2.0, confidence=0.0)
        assert factor.effective_logit == 0.0

    def test_default_confidence_is_one(self) -> None:
        """Default confidence is 1.0 if not specified."""
        factor = Factor(description="Test factor", logit=1.5)
        assert factor.confidence == 1.0
        assert factor.effective_logit == 1.5

    def test_negative_logit(self) -> None:
        """Negative logits work correctly with confidence scaling."""
        factor = Factor(description="Against", logit=-3.0, confidence=0.8)
        assert factor.effective_logit == pytest.approx(-2.4)

    def test_confidence_bounds_validation(self) -> None:
        """Confidence must be between 0 and 1."""
        with pytest.raises(ValueError, match="greater than or equal to 0"):
            Factor(description="Test", logit=1.0, confidence=-0.1)

        with pytest.raises(ValueError, match="less than or equal to 1"):
            Factor(description="Test", logit=1.0, confidence=1.5)


class TestForecast:
    """Tests for the Forecast model (binary questions)."""

    def test_probability_from_logit_zero(self) -> None:
        """Logit of 0 gives probability of 0.5."""
        forecast = Forecast(
            summary="Test",
            factors=[],
            logit=0.0,
            probability=0.5,
        )
        assert forecast.probability_from_logit == pytest.approx(0.5)

    def test_probability_from_logit_positive(self) -> None:
        """Positive logits give probability > 0.5."""
        forecast = Forecast(
            summary="Test",
            factors=[],
            logit=1.0,
            probability=0.73,
        )
        expected = 1 / (1 + math.exp(-1.0))
        assert forecast.probability_from_logit == pytest.approx(expected)

    def test_probability_from_logit_negative(self) -> None:
        """Negative logits give probability < 0.5."""
        forecast = Forecast(
            summary="Test",
            factors=[],
            logit=-2.0,
            probability=0.12,
        )
        expected = 1 / (1 + math.exp(2.0))
        assert forecast.probability_from_logit == pytest.approx(expected)

    def test_factors_sum_logit(self) -> None:
        """factors_sum_logit sums effective logits from all factors."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="A", logit=1.0, confidence=1.0),
                Factor(description="B", logit=-0.5, confidence=0.8),
                Factor(description="C", logit=0.5, confidence=0.5),
            ],
            logit=0.85,
            probability=0.7,
        )
        expected = 1.0 + (-0.5 * 0.8) + (0.5 * 0.5)
        assert forecast.factors_sum_logit == pytest.approx(expected)

    def test_probability_from_factors(self) -> None:
        """probability_from_factors converts summed logits to probability."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="A", logit=1.0),
                Factor(description="B", logit=1.0),
            ],
            logit=2.0,
            probability=0.88,
        )
        assert forecast.probability_from_factors == pytest.approx(
            1 / (1 + math.exp(-2.0))
        )

    def test_check_consistency_empty_factors(self) -> None:
        """check_consistency returns empty list for no factors."""
        forecast = Forecast(
            summary="Test",
            factors=[],
            logit=1.0,
            probability=0.73,
        )
        assert forecast.check_consistency() == []

    def test_check_consistency_consistent(self) -> None:
        """check_consistency returns empty list when factors match probability."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="A", logit=1.0),
            ],
            logit=1.0,
            probability=1 / (1 + math.exp(-1.0)),
        )
        assert forecast.check_consistency() == []

    def test_check_consistency_inconsistent_probability(self) -> None:
        """check_consistency warns when factor-implied probability differs."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="A", logit=2.0),  # implies ~88%
            ],
            logit=2.0,
            probability=0.5,  # significantly different
        )
        warnings = forecast.check_consistency()
        assert len(warnings) >= 1
        assert "differs from final probability" in warnings[0]

    def test_check_consistency_contradictory_strong_factors(self) -> None:
        """check_consistency warns about strong contradictory evidence."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="Strong yes", logit=2.0),  # strong positive
                Factor(description="Strong no", logit=-2.0),  # strong negative
            ],
            logit=0.0,
            probability=0.5,
        )
        warnings = forecast.check_consistency()
        assert any("contradictory" in w.lower() for w in warnings)

    def test_check_consistency_direction_mismatch_positive(self) -> None:
        """check_consistency warns when positive factors yield low probability."""
        forecast = Forecast(
            summary="Test",
            factors=[
                Factor(description="A", logit=1.0),
                Factor(description="B", logit=0.8),
            ],
            logit=1.8,
            probability=0.2,  # Contradicts positive factor sum
        )
        warnings = forecast.check_consistency()
        assert any("positive" in w.lower() and "low" in w.lower() for w in warnings)


class TestMultipleChoiceForecast:
    """Tests for the MultipleChoiceForecast model."""

    def test_valid_probabilities(self) -> None:
        """Valid probabilities are accepted."""
        forecast = MultipleChoiceForecast(
            summary="Test",
            factors=[],
            probabilities={"A": 0.5, "B": 0.3, "C": 0.2},
        )
        assert forecast.probabilities["A"] == 0.5

    def test_factors_preserved(self) -> None:
        """Factors are preserved in multiple choice forecasts."""
        forecast = MultipleChoiceForecast(
            summary="Test",
            factors=[Factor(description="Test", logit=1.0)],
            probabilities={"A": 0.5, "B": 0.5},
        )
        assert len(forecast.factors) == 1


class TestNumericForecast:
    """Tests for the NumericForecast model."""

    def test_valid_percentile_mode(self) -> None:
        """Valid percentiles are accepted in percentile mode."""
        forecast = NumericForecast(
            summary="Test",
            percentile_10=100.0,
            percentile_20=120.0,
            percentile_40=150.0,
            percentile_60=180.0,
            percentile_80=220.0,
            percentile_90=280.0,
        )
        assert forecast.percentile_10 == 100.0
        assert forecast.percentile_90 == 280.0

    def test_percentiles_must_be_strictly_increasing(self) -> None:
        """Percentiles must be strictly increasing."""
        with pytest.raises(ValueError, match="strictly increasing"):
            NumericForecast(
                summary="Test",
                percentile_10=100.0,
                percentile_20=100.0,  # Not strictly increasing
                percentile_40=150.0,
                percentile_60=180.0,
                percentile_80=220.0,
                percentile_90=280.0,
            )

    def test_percentiles_must_not_decrease(self) -> None:
        """Percentiles must not decrease."""
        with pytest.raises(ValueError, match="strictly increasing"):
            NumericForecast(
                summary="Test",
                percentile_10=100.0,
                percentile_20=120.0,
                percentile_40=110.0,  # Decreases
                percentile_60=180.0,
                percentile_80=220.0,
                percentile_90=280.0,
            )

    def test_requires_all_percentiles_or_components(self) -> None:
        """Must provide all percentiles OR components."""
        with pytest.raises(ValueError, match="all 6 percentiles"):
            NumericForecast(
                summary="Test",
                percentile_10=100.0,
                percentile_20=120.0,
                # Missing 40, 60, 80, 90
            )

    def test_median_from_percentiles(self) -> None:
        """Median is interpolated from 40th and 60th percentiles."""
        forecast = NumericForecast(
            summary="Test",
            percentile_10=100.0,
            percentile_20=120.0,
            percentile_40=150.0,
            percentile_60=180.0,
            percentile_80=220.0,
            percentile_90=280.0,
        )
        assert forecast.median == pytest.approx(165.0)

    def test_confidence_interval_from_percentiles(self) -> None:
        """Confidence interval is (10th, 90th) percentile."""
        forecast = NumericForecast(
            summary="Test",
            percentile_10=100.0,
            percentile_20=120.0,
            percentile_40=150.0,
            percentile_60=180.0,
            percentile_80=220.0,
            percentile_90=280.0,
        )
        assert forecast.confidence_interval == (100.0, 280.0)

    def test_get_percentile_dict(self) -> None:
        """get_percentile_dict returns correct format."""
        forecast = NumericForecast(
            summary="Test",
            percentile_10=100.0,
            percentile_20=120.0,
            percentile_40=150.0,
            percentile_60=180.0,
            percentile_80=220.0,
            percentile_90=280.0,
        )
        result = forecast.get_percentile_dict()
        assert result is not None
        assert result[10] == 100.0
        assert result[90] == 280.0

    def test_uses_mixture_mode_false_for_percentiles(self) -> None:
        """uses_mixture_mode is False when using percentiles."""
        forecast = NumericForecast(
            summary="Test",
            percentile_10=100.0,
            percentile_20=120.0,
            percentile_40=150.0,
            percentile_60=180.0,
            percentile_80=220.0,
            percentile_90=280.0,
        )
        assert forecast.uses_mixture_mode is False

    def test_valid_mixture_mode(self) -> None:
        """Valid components are accepted in mixture mode."""
        forecast = NumericForecast(
            summary="Test",
            components=[
                ScenarioComponent(
                    scenario="Base",
                    mode=150.0,
                    lower_bound=100.0,
                    upper_bound=200.0,
                    weight=0.6,
                ),
                ScenarioComponent(
                    scenario="Upside",
                    mode=250.0,
                    lower_bound=200.0,
                    upper_bound=350.0,
                    weight=0.4,
                ),
            ],
        )
        assert forecast.uses_mixture_mode is True
        assert forecast.components is not None
        assert len(forecast.components) == 2

    def test_median_from_mixture(self) -> None:
        """Median from mixture mode is weighted average of modes."""
        forecast = NumericForecast(
            summary="Test",
            components=[
                ScenarioComponent(
                    scenario="A", mode=100.0, lower_bound=50.0, upper_bound=150.0, weight=0.5
                ),
                ScenarioComponent(
                    scenario="B", mode=200.0, lower_bound=150.0, upper_bound=250.0, weight=0.5
                ),
            ],
        )
        assert forecast.median == pytest.approx(150.0)

    def test_confidence_interval_from_mixture(self) -> None:
        """Confidence interval from mixture uses extremes across components."""
        forecast = NumericForecast(
            summary="Test",
            components=[
                ScenarioComponent(
                    scenario="A", mode=100.0, lower_bound=50.0, upper_bound=150.0, weight=0.5
                ),
                ScenarioComponent(
                    scenario="B", mode=200.0, lower_bound=150.0, upper_bound=300.0, weight=0.5
                ),
            ],
        )
        assert forecast.confidence_interval == (50.0, 300.0)

    def test_get_percentile_dict_returns_none_for_mixture(self) -> None:
        """get_percentile_dict returns None when using mixture mode."""
        forecast = NumericForecast(
            summary="Test",
            components=[
                ScenarioComponent(
                    scenario="A", mode=100.0, lower_bound=50.0, upper_bound=150.0, weight=1.0
                ),
            ],
        )
        assert forecast.get_percentile_dict() is None


class TestScenarioComponent:
    """Tests for ScenarioComponent model.

    Note: ScenarioComponent in models.py is a simple model without validation.
    The validated version is DistributionComponent in numeric.py.
    """

    def test_valid_component(self) -> None:
        """Valid component is accepted."""
        comp = ScenarioComponent(
            scenario="Base",
            mode=150.0,
            lower_bound=100.0,
            upper_bound=200.0,
            weight=0.5,
        )
        assert comp.mode == 150.0

    def test_stores_all_fields(self) -> None:
        """All fields are stored correctly."""
        comp = ScenarioComponent(
            scenario="Test",
            mode=150.0,
            lower_bound=100.0,
            upper_bound=200.0,
            weight=0.6,
        )
        assert comp.scenario == "Test"
        assert comp.mode == 150.0
        assert comp.lower_bound == 100.0
        assert comp.upper_bound == 200.0
        assert comp.weight == 0.6

    def test_weight_bounds(self) -> None:
        """Weight must be between 0 and 1."""
        with pytest.raises(ValueError):
            ScenarioComponent(
                scenario="Bad",
                mode=150.0,
                lower_bound=100.0,
                upper_bound=200.0,
                weight=1.5,
            )


class TestCreditExhaustedError:
    """Tests for CreditExhaustedError.from_message()."""

    def test_parses_valid_message_pm(self) -> None:
        """Parses message with PM time correctly."""
        msg = "out of extra usage · resets 6pm (Europe/Paris)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is not None
        assert err.reset_time.hour == 18
        assert err.reset_time.minute == 0

    def test_parses_valid_message_am(self) -> None:
        """Parses message with AM time correctly."""
        msg = "out of extra usage · resets 10am (America/New_York)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is not None
        assert err.reset_time.hour == 10

    def test_parses_message_with_minutes(self) -> None:
        """Parses message with minutes correctly."""
        msg = "out of extra usage · resets 3:30pm (UTC)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is not None
        assert err.reset_time.hour == 15
        assert err.reset_time.minute == 30

    def test_parses_noon(self) -> None:
        """Correctly handles 12pm (noon)."""
        msg = "out of extra usage · resets 12pm (UTC)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is not None
        assert err.reset_time.hour == 12

    def test_parses_midnight(self) -> None:
        """Correctly handles 12am (midnight)."""
        msg = "out of extra usage · resets 12am (UTC)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is not None
        assert err.reset_time.hour == 0

    def test_returns_none_for_unrelated_message(self) -> None:
        """Returns None for messages not about credit exhaustion."""
        msg = "Rate limit exceeded, please retry"
        err = CreditExhaustedError.from_message(msg)
        assert err is None

    def test_handles_invalid_timezone_gracefully(self) -> None:
        """Invalid timezone returns error without reset_time."""
        msg = "out of extra usage · resets 6pm (Invalid/Timezone)"
        err = CreditExhaustedError.from_message(msg)

        assert err is not None
        assert err.reset_time is None  # Couldn't parse timezone

    def test_reset_time_tomorrow_if_past(self) -> None:
        """Reset time is tomorrow if the time has already passed today."""
        tz = zoneinfo.ZoneInfo("UTC")
        now = datetime.now(tz)

        # Create a message for an hour that's already passed
        past_hour = (now.hour - 2) % 24
        am_pm = "am" if past_hour < 12 else "pm"
        display_hour = past_hour if past_hour <= 12 else past_hour - 12
        if display_hour == 0:
            display_hour = 12

        msg = f"out of extra usage · resets {display_hour}{am_pm} (UTC)"
        err = CreditExhaustedError.from_message(msg)

        if err and err.reset_time:
            # Reset time should be tomorrow
            assert err.reset_time > now
            assert err.reset_time.date() >= now.date()

    def test_case_insensitive_matching(self) -> None:
        """Message matching is case insensitive."""
        msg = "OUT OF EXTRA USAGE · resets 6PM (UTC)"
        err = CreditExhaustedError.from_message(msg)
        assert err is not None

    def test_alternative_message_format(self) -> None:
        """Handles 'out of usage' variant."""
        msg = "out of usage · resets 2pm (America/Los_Angeles)"
        err = CreditExhaustedError.from_message(msg)
        assert err is not None
