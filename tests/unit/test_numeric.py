"""Tests for aib.agent.numeric — CDF generation and PMF cap handling."""

import numpy as np
import pytest

from aib.agent.numeric import (
    NumericDefaults,
    percentiles_to_cdf,
    redistribute_capped_pmf,
    standardize_cdf,
)

CAP_201 = NumericDefaults.get_max_pmf_value(201)


class TestRedistributeCappedPmf:
    def test_no_cap_exceeded_returns_unchanged(self) -> None:
        pmf = np.full(203, 1.0 / 203)
        result = redistribute_capped_pmf(pmf, cap=0.19)
        np.testing.assert_array_almost_equal(result, pmf)

    def test_single_peak_capped(self) -> None:
        pmf = np.full(203, 0.001)
        pmf[100] = 0.5  # inner bin with huge mass
        pmf /= pmf.sum()
        result = redistribute_capped_pmf(pmf, cap=0.19)
        assert result[100] <= 0.19 + 1e-10
        assert result[99] > pmf[99]  # adjacent bins received excess
        assert result[101] > pmf[101]

    def test_tail_mass_preserved(self) -> None:
        pmf = np.full(203, 0.001)
        pmf[100] = 0.5
        pmf[0] = 0.05
        pmf[-1] = 0.05
        pmf /= pmf.sum()
        original_tails = (pmf[0], pmf[-1])
        result = redistribute_capped_pmf(pmf, cap=0.19)
        assert result[0] == pytest.approx(original_tails[0])
        assert result[-1] == pytest.approx(original_tails[1])

    def test_inner_mass_conserved(self) -> None:
        pmf = np.full(203, 0.001)
        pmf[100] = 0.5
        pmf /= pmf.sum()
        result = redistribute_capped_pmf(pmf, cap=0.19)
        assert result[1:-1].sum() == pytest.approx(pmf[1:-1].sum())

    def test_all_bins_respect_cap(self) -> None:
        pmf = np.full(203, 0.001)
        pmf[50] = 0.4
        pmf[150] = 0.3
        pmf /= pmf.sum()
        result = redistribute_capped_pmf(pmf, cap=0.19)
        assert np.all(result[1:-1] <= 0.19 + 1e-10)

    def test_bimodal_both_peaks_create_plateaus(self) -> None:
        pmf = np.full(203, 0.0001)
        pmf[50] = 0.35
        pmf[150] = 0.35
        pmf[0] = 0.01
        pmf[-1] = 0.01
        pmf /= pmf.sum()
        result = redistribute_capped_pmf(pmf, cap=0.19)
        # Adjacent bins near each peak should have received mass
        assert result[49] > pmf[49]
        assert result[51] > pmf[51]
        assert result[149] > pmf[149]
        # Bins far from both peaks should be ~unchanged
        assert result[100] == pytest.approx(pmf[100], abs=1e-6)

    def test_tight_distribution_concentrates_near_peak(self) -> None:
        """The SOFR scenario: almost all mass in 1-2 bins, wide range."""
        pmf = np.full(203, 0.00005)
        pmf[0] = 0.001
        pmf[-1] = 0.001
        pmf[58] = 0.95
        pmf /= pmf.sum()
        result = redistribute_capped_pmf(pmf, cap=0.19)
        # Mass near peak (within ±5 bins)
        near_peak = result[54:64].sum()
        assert near_peak > 0.8
        # Distant bins stay at noise floor
        assert result[10] < 0.001
        assert result[190] < 0.001


class TestStandardizeCdf:
    def test_tight_distribution_not_flattened(self) -> None:
        """A tight CDF should produce a peaked PMF, not a uniform one."""
        n = 201
        cdf = np.zeros(n)
        # Step function: 0 up to bin 100, then 1
        cdf[:100] = 0.0
        cdf[100:] = 1.0
        result = standardize_cdf(
            cdf.tolist(),
            open_lower_bound=True,
            open_upper_bound=True,
        )
        result_arr = np.array(result)
        pmf = np.diff(result_arr)
        # Bins far from the step should have very low PMF
        assert pmf[10] < 0.005
        assert pmf[190] < 0.005
        # Peak region should have high PMF
        assert pmf[99] > 0.05

    def test_wide_distribution_mostly_unchanged(self) -> None:
        """A distribution within cap should pass through with minimal change."""
        n = 201
        # Linear CDF (uniform distribution) — all PMF = 1/200 = 0.005, well under cap
        cdf = np.linspace(0, 1, n).tolist()
        result = standardize_cdf(cdf, open_lower_bound=True, open_upper_bound=True)
        # Should be close to the original (just apply_minimum adjustments)
        np.testing.assert_allclose(result, cdf, atol=0.02)

    def test_monotonic_cdf(self) -> None:
        """CDF must be non-decreasing after standardization."""
        n = 201
        cdf = np.zeros(n)
        cdf[:80] = 0.0
        cdf[80:] = 1.0
        result = standardize_cdf(
            cdf.tolist(),
            open_lower_bound=True,
            open_upper_bound=True,
        )
        diffs = np.diff(result)
        assert np.all(diffs >= -1e-10)

    def test_boundary_values_for_open_bounds(self) -> None:
        """Open bounds should have small but nonzero tail mass."""
        n = 201
        cdf = np.linspace(0, 1, n).tolist()
        result = standardize_cdf(cdf, open_lower_bound=True, open_upper_bound=True)
        assert result[0] > 0
        assert result[-1] < 1
        assert result[0] < 0.01
        assert result[-1] > 0.99


class TestPercentilesToCdfEndToEnd:
    def test_sofr_scenario(self) -> None:
        """SOFR-like: tight percentiles on a wide range."""
        cdf = percentiles_to_cdf(
            {10: 3.6596, 20: 3.6615, 40: 3.6631, 60: 3.6642, 80: 3.6656, 90: 3.6665},
            lower_bound=3.109313,
            upper_bound=5.042268,
            open_lower_bound=True,
            open_upper_bound=True,
        )
        assert len(cdf) == 201
        arr = np.array(cdf)
        pmf = np.diff(arr)
        # All PMF values respect cap
        assert np.all(pmf <= CAP_201 + 1e-6)
        # CDF is monotonic
        assert np.all(pmf >= -1e-10)
        # Mass should be concentrated: ≥80% within 10 bins of peak
        peak_bin = np.argmax(pmf)
        lo = max(0, peak_bin - 10)
        hi = min(len(pmf), peak_bin + 11)
        near_peak_mass = pmf[lo:hi].sum()
        assert near_peak_mass > 0.80

    def test_wide_percentiles_unchanged(self) -> None:
        """Percentiles spanning most of the range should not be distorted."""
        cdf = percentiles_to_cdf(
            {10: 110, 20: 120, 40: 140, 60: 160, 80: 180, 90: 190},
            lower_bound=50,
            upper_bound=250,
            open_lower_bound=True,
            open_upper_bound=True,
        )
        arr = np.array(cdf)
        pmf = np.diff(arr)
        # No bin should be at cap for a wide distribution
        assert np.all(pmf < CAP_201 - 0.01)
