"""Metaculus API client library.

A lightweight async client for the Metaculus API, ported from forecasting-tools
with only the functionality needed for the AIB forecasting bot.
"""

from metaculus.client import AsyncMetaculusClient
from metaculus.models import (
    ApiFilter,
    BinaryQuestion,
    CoherenceLink,
    DateQuestion,
    DetailedCoherenceLink,
    DiscreteQuestion,
    MetaculusQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
    QuestionState,
)

__all__ = [
    "ApiFilter",
    "AsyncMetaculusClient",
    "BinaryQuestion",
    "CoherenceLink",
    "DateQuestion",
    "DetailedCoherenceLink",
    "DiscreteQuestion",
    "MetaculusQuestion",
    "MultipleChoiceQuestion",
    "NumericQuestion",
    "QuestionState",
]
