"""Async Metaculus API client using httpx."""

import json
import logging
import os
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager
from typing import Any, Self

import httpx
from bs4 import BeautifulSoup
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from metaculus.models import (
    ApiFilter,
    DetailedCoherenceLink,
    MetaculusQuestion,
)

logger = logging.getLogger(__name__)

API_BASE_URL = os.getenv("METACULUS_API_BASE_URL", "https://www.metaculus.com/api")


def _parse_html_api_response(html: str) -> dict[str, Any] | None:
    """Parse JSON from the DRF browsable API HTML response.

    The Metaculus API serves a Django REST Framework browsable page when
    Accept: text/html is sent. The page embeds the full JSON response
    (including description fields that the JSON API now omits) inside a
    <div class="response-info"> element.
    """
    soup = BeautifulSoup(html, "html.parser")
    response_div = soup.find("div", class_="response-info")
    if response_div is None:
        return None

    raw = response_div.get_text()
    json_start = raw.find("{")
    if json_start == -1:
        return None

    try:
        return json.loads(raw[json_start:])
    except json.JSONDecodeError:
        return None


def with_retry[T](
    max_attempts: int = 4,
    min_wait: float = 5,
    max_wait: float = 120,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator for retrying async functions with exponential backoff.

    Tuned for Metaculus API rate limits (429s need 30-60s+ cooldown).
    """
    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=2, min=min_wait, max=max_wait),
        retry=retry_if_exception_type(
            (
                httpx.HTTPStatusError,
                httpx.TimeoutException,
                httpx.ConnectError,
            )
        ),
        reraise=True,
        before_sleep=lambda rs: logger.warning(
            "Retry %d/%d for %s after %.1fs. Error: %s",
            rs.attempt_number,
            max_attempts,
            rs.fn.__name__ if rs.fn else "unknown",
            rs.next_action.sleep,  # type: ignore[union-attr]
            rs.outcome.exception() if rs.outcome else "unknown",
        ),
    )


class AsyncMetaculusClient:
    """Async Metaculus API client using httpx."""

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        timeout: float = 30.0,
        token: str | None = None,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.token = token or os.getenv("METACULUS_TOKEN")
        self._managed_client: httpx.AsyncClient | None = None
        if self.token is None:
            logger.warning("METACULUS_TOKEN not set")

    async def __aenter__(self) -> Self:
        self._managed_client = httpx.AsyncClient(timeout=self.timeout)
        return self

    async def __aexit__(self, *_exc: object) -> None:
        if self._managed_client:
            await self._managed_client.aclose()
            self._managed_client = None

    @asynccontextmanager
    async def _http_client(self) -> AsyncIterator[httpx.AsyncClient]:
        if self._managed_client is not None:
            yield self._managed_client
        else:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                yield client

    def _get_headers(self) -> dict[str, str]:
        if self.token is None:
            raise ValueError("METACULUS_TOKEN not set")
        return {
            "Authorization": f"Token {self.token}",
            "Accept-Language": "en",
        }

    async def _enrich_post_json(
        self,
        post_json: dict[str, Any],
        client: httpx.AsyncClient,
        post_id: int,
    ) -> dict[str, Any]:
        """Fill nulls in the JSON API response from the HTML API.

        The Metaculus JSON API may return null for various question fields
        (description, resolution, aggregations, etc.). The DRF browsable
        HTML page still includes them. Use HTML as the base, then overlay
        non-null JSON values on top.
        """
        question = post_json.get("question") or {}
        has_nulls = any(v is None for v in question.values())
        if not has_nulls:
            return post_json

        response = await client.get(
            f"{self.base_url}/posts/{post_id}/",
            headers={**self._get_headers(), "Accept": "text/html"},
        )
        if response.status_code != 200:
            return post_json

        html_data = _parse_html_api_response(response.text)
        if html_data is None:
            return post_json

        html_question = html_data.get("question") or {}
        merged_question = {
            **html_question,
            **{k: v for k, v in question.items() if v is not None},
        }

        return {**post_json, "question": merged_question}

    @with_retry()
    async def fetch_post_json(self, post_id: int) -> dict[str, Any]:
        """Fetch enriched post JSON by post ID.

        Returns the raw API JSON with content fields (description,
        resolution_criteria, fine_print) populated from the HTML
        fallback if the JSON API returns nulls.
        """
        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/posts/{post_id}/",
                headers=self._get_headers(),
            )
            response.raise_for_status()
            post_json = response.json()
            return await self._enrich_post_json(post_json, client, post_id)

    async def get_question_by_post_id(
        self, post_id: int
    ) -> MetaculusQuestion | list[MetaculusQuestion]:
        """Fetch a question by post ID."""
        logger.debug("Fetching question %d", post_id)
        post_json = await self.fetch_post_json(post_id)
        questions = self._parse_post_json(post_json)
        if len(questions) == 1:
            return questions[0]
        return questions

    async def get_all_open_questions_from_tournament(
        self, tournament_id: int | str
    ) -> list[MetaculusQuestion]:
        """Fetch all open questions from a tournament."""
        logger.debug("Fetching questions from tournament %s", tournament_id)

        api_filter = ApiFilter(
            allowed_tournaments=[tournament_id],
            allowed_statuses=["open"],
            group_question_mode="unpack_subquestions",
        )
        return await self.get_questions_matching_filter(api_filter)

    @with_retry()
    async def get_questions_matching_filter(
        self,
        api_filter: ApiFilter,
        num_questions: int | None = None,
    ) -> list[MetaculusQuestion]:
        """Fetch questions matching a filter."""
        params = self._build_filter_params(api_filter)
        questions: list[MetaculusQuestion] = []
        offset = 0
        limit = 100

        async with self._http_client() as client:
            while True:
                params["offset"] = offset
                params["limit"] = limit

                response = await client.get(
                    f"{self.base_url}/posts/",
                    headers=self._get_headers(),
                    params=params,
                )
                response.raise_for_status()
                data = response.json()

                results = data.get("results", [])
                if not results:
                    break

                for post_json in results:
                    # Client-side status filtering (API may not filter correctly)
                    if api_filter.allowed_statuses:
                        post_status = post_json.get("status")
                        if post_status not in api_filter.allowed_statuses:
                            continue

                    parsed = self._parse_post_json(
                        post_json, api_filter.group_question_mode
                    )
                    questions.extend(parsed)

                    if num_questions and len(questions) >= num_questions:
                        return questions[:num_questions]

                # Check if there are more pages
                if not data.get("next"):
                    break

                offset += limit

        return questions

    @with_retry()
    async def get_links_for_question(
        self, question_id: int
    ) -> list[DetailedCoherenceLink]:
        """Fetch coherence links for a question."""
        logger.debug("Fetching coherence links for question %d", question_id)

        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/coherence/question/{question_id}/links/",
                headers=self._get_headers(),
            )
            response.raise_for_status()
            content = response.json()["data"]

        return [DetailedCoherenceLink.from_api_json(link) for link in content]

    def _parse_post_json(
        self,
        post_json: dict[str, Any],
        group_question_mode: str = "exclude",
    ) -> list[MetaculusQuestion]:
        """Parse a post JSON into MetaculusQuestion objects."""
        if "group_of_questions" in post_json:
            if group_question_mode == "exclude":
                return []
            elif group_question_mode == "unpack_subquestions":
                return self._unpack_group_question(post_json)
        elif "conditional" in post_json:
            post_json["question"] = post_json["conditional"]
            post_json["question"]["type"] = "conditional"

        # Skip posts without question data (e.g., notebooks)
        if post_json.get("question") is None:
            logger.debug(
                "Skipping post %s: no question data (may be a notebook)",
                post_json.get("id"),
            )
            return []

        return [MetaculusQuestion.from_api_json(post_json)]

    @staticmethod
    def _unpack_group_question(post_json: dict[str, Any]) -> list[MetaculusQuestion]:
        """Unpack a group question into individual questions."""
        group_json = post_json["group_of_questions"]
        questions: list[MetaculusQuestion] = []

        for sub_question_json in group_json.get("questions", []):
            sub_post_json = {
                **post_json,
                "question": sub_question_json,
            }
            sub_post_json.pop("group_of_questions", None)
            questions.append(MetaculusQuestion.from_api_json(sub_post_json))

        return questions

    def _build_filter_params(self, api_filter: ApiFilter) -> dict[str, Any]:
        """Build query parameters from an ApiFilter."""
        params: dict[str, Any] = {
            "order_by": api_filter.order_by,
        }

        if api_filter.allowed_statuses:
            params["status"] = ",".join(api_filter.allowed_statuses)

        if api_filter.allowed_tournaments:
            params["tournaments"] = ",".join(
                str(t) for t in api_filter.allowed_tournaments
            )

        if api_filter.allowed_types:
            params["forecast_type"] = ",".join(api_filter.allowed_types)

        if api_filter.num_forecasters_gte:
            params["forecaster_count__gte"] = api_filter.num_forecasters_gte

        if api_filter.scheduled_resolve_time_gt:
            params["scheduled_resolve_time__gt"] = (
                api_filter.scheduled_resolve_time_gt.isoformat()
            )

        if api_filter.scheduled_resolve_time_lt:
            params["scheduled_resolve_time__lt"] = (
                api_filter.scheduled_resolve_time_lt.isoformat()
            )

        if api_filter.community_prediction_exists is not None:
            params["has_community_prediction"] = api_filter.community_prediction_exists

        params.update(api_filter.other_url_parameters)

        return params
