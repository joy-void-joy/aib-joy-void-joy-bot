"""Shared test fixtures and configuration."""

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test (requires API keys)"
    )


@pytest.fixture
def sample_binary_factors() -> list[dict[str, float | str]]:
    """Sample factors for binary forecast testing."""
    return [
        {"description": "Strong evidence toward yes", "logit": 1.5, "confidence": 0.9},
        {"description": "Moderate evidence toward no", "logit": -1.0, "confidence": 0.8},
        {"description": "Weak signal toward yes", "logit": 0.3, "confidence": 0.5},
    ]


@pytest.fixture
def sample_percentiles() -> dict[int, float]:
    """Sample percentile values for numeric forecast testing."""
    return {
        10: 100.0,
        20: 120.0,
        40: 150.0,
        60: 180.0,
        80: 220.0,
        90: 280.0,
    }


@pytest.fixture
def sample_numeric_bounds() -> dict[str, float]:
    """Sample bounds for numeric questions."""
    return {
        "lower_bound": 0.0,
        "upper_bound": 500.0,
    }


@pytest.fixture
def sample_log_scaled_bounds() -> dict[str, float | None]:
    """Sample bounds for log-scaled numeric questions."""
    return {
        "lower_bound": 1.0,
        "upper_bound": 10000.0,
        "zero_point": 0.0,
    }
