"""ResearchInput accepts both the batch and single-question call shapes."""

import pytest
from pydantic import ValidationError

from aib.tools.research import DEFAULT_TTL, ResearchInput


def test_batch_shape_is_unchanged() -> None:
    parsed = ResearchInput.model_validate(
        {"questions": [{"query": "a"}, {"query": "b"}]}
    )
    assert [q.query for q in parsed.questions] == ["a", "b"]


def test_bare_query_is_lifted_into_questions() -> None:
    parsed = ResearchInput.model_validate({"query": "what is the CPI print?"})
    assert len(parsed.questions) == 1
    assert parsed.questions[0].query == "what is the CPI print?"
    assert parsed.questions[0].ttl == DEFAULT_TTL


def test_bare_query_carries_context_and_ttl() -> None:
    parsed = ResearchInput.model_validate(
        {"query": "outbreak status", "context": "West Africa", "ttl": "6h"}
    )
    assert parsed.questions[0].context == "West Africa"
    assert parsed.questions[0].ttl == "6h"


def test_bare_query_preserves_sibling_fields() -> None:
    parsed = ResearchInput.model_validate({"query": "follow up", "follow_up": "slug-1"})
    assert parsed.follow_up == "slug-1"
    assert parsed.questions[0].query == "follow up"


def test_explicit_questions_wins_over_bare_query() -> None:
    parsed = ResearchInput.model_validate(
        {"query": "ignored", "questions": [{"query": "kept"}]}
    )
    assert [q.query for q in parsed.questions] == ["kept"]


def test_neither_shape_still_raises() -> None:
    with pytest.raises(ValidationError):
        ResearchInput.model_validate({"context": "no query anywhere"})
