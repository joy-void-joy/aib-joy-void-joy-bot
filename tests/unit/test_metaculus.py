"""Tests for src/metaculus models and client parsing logic.

All tests are pure unit tests — no API calls, no httpx mocking.
They test static/parsing methods directly using crafted JSON fixtures.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pytest

from metaculus.client import AsyncMetaculusClient
from metaculus.models import (
    ApiFilter,
    BinaryQuestion,
    DateQuestion,
    DiscreteQuestion,
    MetaculusQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
    _parse_datetime,
    _question_from_question_json,
)


# --- JSON Fixtures ---


def _make_post_json(
    question_type: str = "binary",
    post_id: int = 100,
    question_id: int = 200,
    **question_overrides: Any,
) -> dict[str, Any]:
    """Build a minimal post JSON matching the Metaculus API shape."""
    question: dict[str, Any] = {
        "id": question_id,
        "title": "Test question",
        "type": question_type,
        "status": "open",
        "resolution_criteria": "Resolves YES if ...",
        "fine_print": "Some fine print",
        "description": "Background info",
        "scheduled_close_time": "2026-12-31T00:00:00Z",
        "scheduled_resolve_time": "2027-01-01T00:00:00Z",
        "open_time": "2026-01-01T00:00:00Z",
        "aggregations": {
            "recency_weighted": {
                "latest": {"centers": [0.65], "means": [0.64]},
            },
        },
        "my_forecasts": None,
        **question_overrides,
    }
    return {
        "id": post_id,
        "question": question,
        "nr_forecasters": 42,
        "forecasts_count": 100,
        "published_at": "2026-01-15T12:00:00Z",
        "status": "open",
        "projects": {
            "tournament": [{"slug": "aib-spring-2026"}],
        },
    }


def _make_group_post_json(
    sub_types: list[str] | None = None,
    group_fine_print: str = "Group fine print",
    group_description: str = "Group description",
    group_resolution_criteria: str = "Group resolution criteria",
) -> dict[str, Any]:
    """Build a group question post JSON."""
    if sub_types is None:
        sub_types = ["binary", "binary"]
    sub_questions = [
        {
            "id": 300 + i,
            "title": f"Sub-question {i + 1}",
            "type": t,
            "status": "open",
            "resolution_criteria": None,
            "fine_print": None,
            "description": None,
            "scheduled_close_time": "2026-12-31T00:00:00Z",
            "scheduled_resolve_time": "2027-01-01T00:00:00Z",
            "open_time": "2026-01-01T00:00:00Z",
            "aggregations": {
                "recency_weighted": {
                    "latest": {"centers": [0.5], "means": [0.5]},
                },
            },
            "my_forecasts": None,
        }
        for i, t in enumerate(sub_types)
    ]
    return {
        "id": 100,
        "group_of_questions": {
            "questions": sub_questions,
            "fine_print": group_fine_print,
            "description": group_description,
            "resolution_criteria": group_resolution_criteria,
        },
        "nr_forecasters": 42,
        "forecasts_count": 100,
        "published_at": "2026-01-15T12:00:00Z",
        "status": "open",
        "projects": {},
    }


def _make_conditional_post_json() -> dict[str, Any]:
    """Build a conditional post JSON."""
    return {
        "id": 100,
        "conditional": {
            "question_yes": {
                "id": 301,
                "title": "If yes",
                "type": "binary",
                "status": "open",
                "resolution_criteria": None,
                "fine_print": None,
                "description": None,
                "scheduled_close_time": "2026-12-31T00:00:00Z",
                "scheduled_resolve_time": "2027-01-01T00:00:00Z",
                "open_time": "2026-01-01T00:00:00Z",
                "aggregations": {},
                "my_forecasts": None,
            },
            "question_no": {
                "id": 302,
                "title": "If no",
                "type": "binary",
                "status": "open",
                "resolution_criteria": None,
                "fine_print": None,
                "description": None,
                "scheduled_close_time": "2026-12-31T00:00:00Z",
                "scheduled_resolve_time": "2027-01-01T00:00:00Z",
                "open_time": "2026-01-01T00:00:00Z",
                "aggregations": {},
                "my_forecasts": None,
            },
        },
        "nr_forecasters": 10,
        "forecasts_count": 20,
        "published_at": "2026-01-15T12:00:00Z",
        "status": "open",
        "projects": {},
    }


# --- Model Tests ---


class TestFromApiJson:
    """Tests for MetaculusQuestion.from_api_json factory."""

    def test_binary(self) -> None:
        q = MetaculusQuestion.from_api_json(_make_post_json("binary"))
        assert isinstance(q, BinaryQuestion)
        assert q.get_question_type() == "binary"

    def test_numeric(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "numeric",
                scaling={"range_min": 0, "range_max": 100, "zero_point": None},
            )
        )
        assert isinstance(q, NumericQuestion)
        assert q.get_question_type() == "numeric"

    def test_discrete(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "discrete",
                scaling={"range_min": 0, "range_max": 10, "inbound_outcome_count": 10},
            )
        )
        assert isinstance(q, DiscreteQuestion)
        assert q.get_question_type() == "discrete"

    def test_date(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "date",
                scaling={"range_min": "2025-01-01", "range_max": "2027-01-01"},
            )
        )
        assert isinstance(q, DateQuestion)
        assert q.get_question_type() == "date"

    def test_multiple_choice_string_options(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json("multiple_choice", options=["A", "B", "C"])
        )
        assert isinstance(q, MultipleChoiceQuestion)
        assert q.options == ["A", "B", "C"]

    def test_multiple_choice_dict_options(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "multiple_choice",
                options=[{"label": "X"}, {"label": "Y"}],
            )
        )
        assert isinstance(q, MultipleChoiceQuestion)
        assert q.options == ["X", "Y"]

    def test_unknown_type_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown question type"):
            MetaculusQuestion.from_api_json(_make_post_json("unknown_type"))

    def test_common_fields(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json("binary", post_id=42, question_id=99)
        )
        assert q.id_of_post == 42
        assert q.id_of_question == 99
        assert q.question_text == "Test question"
        assert q.resolution_criteria == "Resolves YES if ..."
        assert q.fine_print == "Some fine print"
        assert q.background_info == "Background info"
        assert q.page_url == "https://www.metaculus.com/questions/42"
        assert q.tournament_slugs == ["aib-spring-2026"]


class TestBinaryQuestion:
    """Tests for BinaryQuestion community prediction extraction."""

    def test_extracts_cp_from_recency_weighted(self) -> None:
        q = MetaculusQuestion.from_api_json(_make_post_json("binary"))
        assert isinstance(q, BinaryQuestion)
        assert q.community_prediction_at_access_time == 0.65

    def test_cp_none_when_no_aggregations(self) -> None:
        q = MetaculusQuestion.from_api_json(_make_post_json("binary", aggregations={}))
        assert isinstance(q, BinaryQuestion)
        assert q.community_prediction_at_access_time is None

    def test_cp_none_when_no_latest(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json("binary", aggregations={"recency_weighted": {}})
        )
        assert isinstance(q, BinaryQuestion)
        assert q.community_prediction_at_access_time is None


class TestNumericQuestion:
    """Tests for NumericQuestion field extraction."""

    def test_extracts_bounds(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "numeric",
                scaling={"range_min": 10, "range_max": 500, "zero_point": 0},
                open_upper_bound=True,
                open_lower_bound=False,
            )
        )
        assert isinstance(q, NumericQuestion)
        assert q.lower_bound == 10.0
        assert q.upper_bound == 500.0
        assert q.open_upper_bound is True
        assert q.open_lower_bound is False
        assert q.zero_point == 0

    def test_cdf_size_from_inbound_outcome_count(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "discrete",
                scaling={"range_min": 0, "range_max": 10, "inbound_outcome_count": 10},
            )
        )
        assert isinstance(q, DiscreteQuestion)
        assert q.cdf_size == 11

    def test_cdf_size_default(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json("numeric", scaling={"range_min": 0, "range_max": 100})
        )
        assert isinstance(q, NumericQuestion)
        assert q.cdf_size == 201


class TestDateQuestion:
    """Tests for DateQuestion datetime bounds."""

    def test_parses_date_bounds(self) -> None:
        q = MetaculusQuestion.from_api_json(
            _make_post_json(
                "date",
                scaling={
                    "range_min": "2025-01-01T00:00:00Z",
                    "range_max": "2027-06-01T00:00:00Z",
                },
            )
        )
        assert isinstance(q, DateQuestion)
        assert q.lower_bound is not None
        assert q.lower_bound.year == 2025
        assert q.upper_bound is not None
        assert q.upper_bound.year == 2027


class TestParseDatetime:
    """Tests for _parse_datetime helper."""

    def test_none(self) -> None:
        assert _parse_datetime(None) is None

    def test_iso_string(self) -> None:
        dt = _parse_datetime("2026-06-15T12:00:00+00:00")
        assert dt is not None
        assert dt.year == 2026
        assert dt.month == 6

    def test_iso_string_with_z(self) -> None:
        dt = _parse_datetime("2026-06-15T12:00:00Z")
        assert dt is not None
        assert dt.year == 2026

    def test_unix_timestamp(self) -> None:
        dt = _parse_datetime(1738886400.0)
        assert dt is not None
        assert dt.year == 2025

    def test_unix_int(self) -> None:
        dt = _parse_datetime(1738886400)
        assert dt is not None
        assert dt.year == 2025


class TestQuestionFromQuestionJson:
    """Tests for _question_from_question_json (coherence link parsing)."""

    def test_creates_binary_from_inner_json(self) -> None:
        inner = {
            "id": 500,
            "post_id": 501,
            "title": "Linked question",
            "type": "binary",
            "status": "open",
        }
        q = _question_from_question_json(inner)
        assert isinstance(q, BinaryQuestion)
        assert q.id_of_question == 500
        assert q.id_of_post == 501

    def test_falls_back_to_base_for_unknown_type(self) -> None:
        inner = {
            "id": 600,
            "title": "Unknown",
            "type": "some_new_type",
            "status": "open",
        }
        q = _question_from_question_json(inner)
        assert isinstance(q, MetaculusQuestion)


# --- Client Parsing Tests ---


class TestParsePostJson:
    """Tests for AsyncMetaculusClient._parse_post_json."""

    def _client(self) -> AsyncMetaculusClient:
        return AsyncMetaculusClient(token="fake")

    def test_regular_question(self) -> None:
        result = self._client()._parse_post_json(_make_post_json("binary"))
        assert len(result) == 1
        assert isinstance(result[0], BinaryQuestion)

    def test_group_exclude(self) -> None:
        result = self._client()._parse_post_json(
            _make_group_post_json(), group_question_mode="exclude"
        )
        assert result == []

    def test_group_unpack(self) -> None:
        result = self._client()._parse_post_json(
            _make_group_post_json(), group_question_mode="unpack_subquestions"
        )
        assert len(result) == 2

    def test_conditional_unpack(self) -> None:
        result = self._client()._parse_post_json(_make_conditional_post_json())
        assert len(result) == 2
        assert result[0].question_text == "If yes"
        assert result[1].question_text == "If no"

    def test_notebook_skipped(self) -> None:
        post_json: dict[str, Any] = {
            "id": 999,
            "question": None,
            "status": "open",
            "projects": {},
        }
        result = self._client()._parse_post_json(post_json)
        assert result == []


class TestUnpackGroupQuestion:
    """Tests for group question unpacking with field inheritance."""

    def test_copies_group_fields_to_subquestions(self) -> None:
        post_json = _make_group_post_json(
            group_fine_print="Group FP",
            group_description="Group desc",
            group_resolution_criteria="Group RC",
        )
        result = AsyncMetaculusClient._unpack_group_question(post_json)
        assert len(result) == 2
        for q in result:
            assert q.fine_print == "Group FP"
            assert q.background_info == "Group desc"
            assert q.resolution_criteria == "Group RC"

    def test_preserves_subquestion_fields_when_present(self) -> None:
        post_json = _make_group_post_json()
        sub_q = post_json["group_of_questions"]["questions"][0]
        sub_q["fine_print"] = "Sub-specific FP"
        sub_q["description"] = "Sub-specific desc"
        sub_q["resolution_criteria"] = "Sub-specific RC"

        result = AsyncMetaculusClient._unpack_group_question(post_json)
        assert result[0].fine_print == "Sub-specific FP"
        assert result[0].background_info == "Sub-specific desc"
        assert result[0].resolution_criteria == "Sub-specific RC"
        # Second sub-question still gets group fields
        assert result[1].fine_print == "Group fine print"


class TestUnpackConditional:
    """Tests for conditional question unpacking."""

    def test_unpacks_both_branches(self) -> None:
        result = AsyncMetaculusClient._unpack_conditional(_make_conditional_post_json())
        assert len(result) == 2
        assert result[0].id_of_question == 301
        assert result[1].id_of_question == 302

    def test_handles_missing_branch(self) -> None:
        post_json = _make_conditional_post_json()
        post_json["conditional"]["question_no"] = None
        result = AsyncMetaculusClient._unpack_conditional(post_json)
        assert len(result) == 1
        assert result[0].id_of_question == 301


# --- Filter Params Tests ---


class TestBuildFilterParams:
    """Tests for _build_filter_params."""

    def _client(self) -> AsyncMetaculusClient:
        return AsyncMetaculusClient(token="fake")

    def test_includes_group_type_when_unpacking(self) -> None:
        api_filter = ApiFilter(
            allowed_types=["binary"],
            group_question_mode="unpack_subquestions",
        )
        params = self._client()._build_filter_params(api_filter)
        assert "group_of_questions" in params["forecast_type"]

    def test_no_group_type_when_excluding(self) -> None:
        api_filter = ApiFilter(
            allowed_types=["binary"],
            group_question_mode="exclude",
        )
        params = self._client()._build_filter_params(api_filter)
        assert "group_of_questions" not in params["forecast_type"]

    def test_does_not_mutate_allowed_types(self) -> None:
        types = ["binary"]
        api_filter = ApiFilter(
            allowed_types=types,
            group_question_mode="unpack_subquestions",
        )
        self._client()._build_filter_params(api_filter)
        assert types == ["binary"]

    def test_uses_statuses_plural(self) -> None:
        api_filter = ApiFilter(allowed_statuses=["open"])
        params = self._client()._build_filter_params(api_filter)
        assert "statuses" in params
        assert "status" not in params

    def test_publish_time_params(self) -> None:
        dt = datetime(2026, 1, 15, tzinfo=timezone.utc)
        api_filter = ApiFilter(publish_time_gt=dt, publish_time_lt=dt)
        params = self._client()._build_filter_params(api_filter)
        assert "published_at__gt" in params
        assert "published_at__lt" in params

    def test_open_time_params(self) -> None:
        dt = datetime(2026, 1, 15, tzinfo=timezone.utc)
        api_filter = ApiFilter(open_time_gt=dt, open_time_lt=dt)
        params = self._client()._build_filter_params(api_filter)
        assert "open_time__gt" in params
        assert "open_time__lt" in params

    def test_with_cp_param(self) -> None:
        api_filter = ApiFilter()
        params = self._client()._build_filter_params(api_filter, with_cp=True)
        assert params["with_cp"] == "true"
        assert params["include_conditional_cps"] == "true"

    def test_tournaments_param(self) -> None:
        api_filter = ApiFilter(allowed_tournaments=[32916, "minibench"])
        params = self._client()._build_filter_params(api_filter)
        assert params["tournaments"] == "32916,minibench"


# --- URL Parsing Tests ---


class TestParsePostIdFromUrl:
    """Tests for URL-to-post-ID parsing."""

    def test_question_url(self) -> None:
        url = "https://www.metaculus.com/questions/28841/some-slug/"
        assert AsyncMetaculusClient._parse_post_id_from_url(url) == 28841

    def test_question_url_no_slug(self) -> None:
        url = "https://www.metaculus.com/questions/12345/"
        assert AsyncMetaculusClient._parse_post_id_from_url(url) == 12345

    def test_community_url(self) -> None:
        url = "https://www.metaculus.com/c/risk/38787/"
        assert AsyncMetaculusClient._parse_post_id_from_url(url) == 38787

    def test_invalid_url(self) -> None:
        with pytest.raises(ValueError, match="Could not extract post ID"):
            AsyncMetaculusClient._parse_post_id_from_url("https://example.com/invalid")

    def test_question_url_with_query_params(self) -> None:
        url = "https://www.metaculus.com/questions/28841/slug/?ref=share"
        assert AsyncMetaculusClient._parse_post_id_from_url(url) == 28841
