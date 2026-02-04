"""Metaculus data models.

Simplified models for Metaculus questions and related data structures.
Only includes fields actually used by the AIB forecasting bot.

IMPORTANT: post_id vs question_id
================================
Metaculus has two different ID systems:

- **post_id** (id_of_post): The ID in the URL (metaculus.com/questions/{post_id}).
  A post is a container that can hold one or more questions. Used for:
  - Fetching questions: GET /api/posts/{post_id}/
  - Building URLs: metaculus.com/questions/{post_id}
  - Local forecast storage: notes/forecasts/{post_id}/

- **question_id** (id_of_question): The internal ID of the actual question.
  Used for:
  - Coherence links: GET /api/coherence/question/{question_id}/links/
  - CP history: GET /api/questions/{question_id}/aggregate-history/
  - Submitting forecasts: POST /api/questions/{question_id}/predict/

For most questions, post_id == question_id, but for group questions
(one post containing multiple sub-questions), they differ.

When in doubt, check which API endpoint you're calling and use the
appropriate ID. The client methods are named to clarify:
- get_question_by_post_id(post_id) - takes post_id
- get_links_for_question(question_id) - takes question_id
"""

import logging
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal, Self

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# Type aliases
QuestionType = Literal[
    "binary", "numeric", "multiple_choice", "date", "discrete", "conditional"
]


class QuestionState(str, Enum):
    """Question lifecycle states."""

    UPCOMING = "upcoming"
    OPEN = "open"
    RESOLVED = "resolved"
    CLOSED = "closed"


class ApiFilter(BaseModel):
    """Filter parameters for Metaculus API queries."""

    allowed_statuses: list[str] = Field(default_factory=list)
    allowed_tournaments: list[int | str] = Field(default_factory=list)
    allowed_types: list[str] = Field(default_factory=list)
    order_by: str = "-published_time"
    num_forecasters_gte: int | None = None
    scheduled_resolve_time_gt: datetime | None = None
    scheduled_resolve_time_lt: datetime | None = None
    community_prediction_exists: bool | None = None
    group_question_mode: str = "exclude"
    other_url_parameters: dict[str, Any] = Field(default_factory=dict)


class MetaculusQuestion(BaseModel):
    """Base class for Metaculus questions.

    Contains fields common to all question types.

    Attributes:
        id_of_post: The post ID (used for URLs, local storage). See module docstring.
        id_of_question: The question ID (used for coherence links, CP history, submissions).
    """

    question_text: str
    id_of_post: int | None = None  # URL/storage ID - see module docstring
    id_of_question: int | None = (
        None  # API ID for coherence/CP/submit - see module docstring
    )
    page_url: str | None = None
    status: QuestionState | None = None
    num_forecasters: int | None = None
    num_predictions: int | None = None
    resolution_criteria: str | None = None
    fine_print: str | None = None
    background_info: str | None = None
    close_time: datetime | None = None
    actual_resolution_time: datetime | None = None
    scheduled_resolution_time: datetime | None = None
    published_time: datetime | None = None
    open_time: datetime | None = None
    tournament_slugs: list[str] = Field(default_factory=list)
    resolution_string: str | None = None
    api_json: dict[str, Any] = Field(default_factory=dict)

    def get_question_type(self) -> QuestionType:
        """Return the question type string."""
        raise NotImplementedError("Subclasses must implement get_question_type")

    @property
    def timestamp_of_my_last_forecast(self) -> datetime | None:
        """Get timestamp of our last forecast from API JSON."""
        try:
            timestamp: float = self.api_json["question"]["my_forecasts"]["latest"][
                "start_time"
            ]
            return datetime.fromtimestamp(timestamp, tz=timezone.utc)
        except (KeyError, TypeError):
            return None

    @classmethod
    def from_api_json(cls, post_json: dict[str, Any]) -> MetaculusQuestion:
        """Create a MetaculusQuestion from API JSON.

        This is a factory method that returns the appropriate subclass
        based on the question type in the JSON.
        """
        question_json = post_json.get("question") or post_json.get("conditional")
        if question_json is None:
            raise ValueError("No question or conditional data in API JSON")

        question_type = question_json.get("type")

        # Map type to subclass
        type_map: dict[str, type[MetaculusQuestion]] = {
            "binary": BinaryQuestion,
            "numeric": NumericQuestion,
            "discrete": DiscreteQuestion,
            "multiple_choice": MultipleChoiceQuestion,
            "date": DateQuestion,
        }

        question_cls = type_map.get(question_type)
        if question_cls is None:
            post_id = post_json.get("id", "unknown")
            raise ValueError(
                f"Unknown question type '{question_type}' for post {post_id}. "
                f"Supported types: {list(type_map.keys())}"
            )
        return question_cls._from_api_json_impl(post_json)

    @classmethod
    def _from_api_json_impl(cls, post_json: dict[str, Any]) -> Self:
        """Internal implementation for parsing API JSON."""
        question_json = post_json.get("question") or post_json.get("conditional", {})

        # Parse tournament slugs
        tournament_slugs: list[str] = []
        projects = post_json.get("projects", {})
        for key in ("tournament", "question_series"):
            if key in projects:
                tournament_slugs.extend(str(t.get("slug", "")) for t in projects[key])

        return cls(
            question_text=question_json.get("title", ""),
            id_of_post=post_json.get("id"),
            id_of_question=question_json.get("id"),
            page_url=f"https://www.metaculus.com/questions/{post_json.get('id')}",
            status=QuestionState(question_json["status"])
            if question_json.get("status")
            else None,
            num_forecasters=post_json.get("nr_forecasters"),
            num_predictions=post_json.get("forecasts_count"),
            resolution_criteria=question_json.get("resolution_criteria"),
            fine_print=question_json.get("fine_print"),
            background_info=question_json.get("description"),
            close_time=_parse_datetime(question_json.get("scheduled_close_time")),
            actual_resolution_time=_parse_datetime(
                question_json.get("actual_resolve_time")
            ),
            scheduled_resolution_time=_parse_datetime(
                question_json.get("scheduled_resolve_time")
            ),
            published_time=_parse_datetime(post_json.get("published_at")),
            open_time=_parse_datetime(question_json.get("open_time")),
            tournament_slugs=tournament_slugs,
            resolution_string=question_json.get("resolution"),
            api_json=post_json,
        )


class BinaryQuestion(MetaculusQuestion):
    """Binary (yes/no) question."""

    community_prediction_at_access_time: float | None = None

    def get_question_type(self) -> QuestionType:
        return "binary"

    @classmethod
    def _from_api_json_impl(cls, post_json: dict[str, Any]) -> Self:
        base = MetaculusQuestion._from_api_json_impl.__func__(cls, post_json)  # type: ignore[attr-defined]

        # Extract community prediction
        community_prediction: float | None = None
        try:
            aggregations = post_json["question"]["aggregations"]
            for agg_type in ("recency_weighted", "unweighted"):
                if agg_type in aggregations and aggregations[agg_type].get("latest"):
                    centers = aggregations[agg_type]["latest"].get("centers", [])
                    if centers:
                        community_prediction = centers[0]
                        break
        except (KeyError, TypeError, IndexError):
            pass

        base.community_prediction_at_access_time = community_prediction
        return base


class NumericQuestion(MetaculusQuestion):
    """Numeric question with continuous range."""

    upper_bound: float = 0.0
    lower_bound: float = 0.0
    open_upper_bound: bool = True
    open_lower_bound: bool = True
    zero_point: float | None = None
    cdf_size: int = 201

    def get_question_type(self) -> QuestionType:
        return "numeric"

    @classmethod
    def _from_api_json_impl(cls, post_json: dict[str, Any]) -> Self:
        base = MetaculusQuestion._from_api_json_impl.__func__(cls, post_json)  # type: ignore[attr-defined]

        question_json = post_json.get("question", {})
        scaling = question_json.get("scaling", {})

        base.upper_bound = float(scaling.get("range_max", 0))
        base.lower_bound = float(scaling.get("range_min", 0))
        base.open_upper_bound = question_json.get("open_upper_bound", True)
        base.open_lower_bound = question_json.get("open_lower_bound", True)
        base.zero_point = scaling.get("zero_point")

        # CDF size
        outcome_count = scaling.get("inbound_outcome_count")
        if outcome_count is not None:
            base.cdf_size = outcome_count + 1
        else:
            base.cdf_size = 201

        return base


class DiscreteQuestion(NumericQuestion):
    """Discrete numeric question (integers only)."""

    def get_question_type(self) -> QuestionType:
        return "discrete"


class DateQuestion(MetaculusQuestion):
    """Date question with temporal range."""

    upper_bound: datetime | None = None
    lower_bound: datetime | None = None
    open_upper_bound: bool = True
    open_lower_bound: bool = True
    zero_point: float | None = None
    cdf_size: int = 201

    def get_question_type(self) -> QuestionType:
        return "date"

    @classmethod
    def _from_api_json_impl(cls, post_json: dict[str, Any]) -> Self:
        base = MetaculusQuestion._from_api_json_impl.__func__(cls, post_json)  # type: ignore[attr-defined]

        question_json = post_json.get("question", {})
        scaling = question_json.get("scaling", {})

        base.upper_bound = _parse_datetime(scaling.get("range_max"))
        base.lower_bound = _parse_datetime(scaling.get("range_min"))
        base.open_upper_bound = question_json.get("open_upper_bound", True)
        base.open_lower_bound = question_json.get("open_lower_bound", True)
        base.zero_point = scaling.get("zero_point")

        outcome_count = scaling.get("inbound_outcome_count")
        if outcome_count is not None:
            base.cdf_size = outcome_count + 1
        else:
            base.cdf_size = 201

        return base


class MultipleChoiceQuestion(MetaculusQuestion):
    """Multiple choice question."""

    options: list[str] = Field(default_factory=list)

    def get_question_type(self) -> QuestionType:
        return "multiple_choice"

    @classmethod
    def _from_api_json_impl(cls, post_json: dict[str, Any]) -> Self:
        base = MetaculusQuestion._from_api_json_impl.__func__(cls, post_json)  # type: ignore[attr-defined]

        question_json = post_json.get("question", {})
        options_json = question_json.get("options", [])
        # Options can be strings or dicts with a "label" key
        base.options = [
            opt if isinstance(opt, str) else opt.get("label", "")
            for opt in options_json
        ]

        return base


# --- Coherence Links ---


class CoherenceLink(BaseModel):
    """Basic coherence link between two questions."""

    question1_id: int
    question2_id: int
    direction: int
    strength: int
    type: str
    id: int


class DetailedCoherenceLink(CoherenceLink):
    """Coherence link with full question details."""

    question1: MetaculusQuestion
    question2: MetaculusQuestion

    @classmethod
    def from_api_json(cls, api_json: dict[str, Any]) -> Self:
        """Create from Metaculus coherence API response."""
        return cls(
            question1_id=api_json["question1_id"],
            question2_id=api_json["question2_id"],
            direction=api_json["direction"],
            strength=api_json["strength"],
            type=api_json["type"],
            id=api_json["id"],
            question1=_question_from_question_json(api_json["question1"]),
            question2=_question_from_question_json(api_json["question2"]),
        )


# --- Helper Functions ---


def _parse_datetime(value: str | float | int | None) -> datetime | None:
    """Parse datetime from API response (ISO string or timestamp)."""
    if value is None:
        return None

    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc)

    if isinstance(value, str):
        # Handle ISO format
        try:
            # Remove trailing Z and parse
            if value.endswith("Z"):
                value = value[:-1] + "+00:00"
            return datetime.fromisoformat(value)
        except ValueError:
            logger.warning("Failed to parse datetime: %s", value)
            return None

    return None


def _question_from_question_json(question_json: dict[str, Any]) -> MetaculusQuestion:
    """Create question from inner question JSON (used in coherence links).

    This is for parsing the nested question objects in coherence link responses,
    which have a different structure than the full post JSON.
    """
    question_type = question_json.get("type", "")

    # Build a minimal post_json wrapper
    post_json = {
        "id": question_json.get("post_id"),
        "question": question_json,
    }

    type_map: dict[str, type[MetaculusQuestion]] = {
        "binary": BinaryQuestion,
        "numeric": NumericQuestion,
        "discrete": DiscreteQuestion,
        "multiple_choice": MultipleChoiceQuestion,
        "date": DateQuestion,
    }

    question_cls = type_map.get(question_type, MetaculusQuestion)
    return question_cls._from_api_json_impl(post_json)
