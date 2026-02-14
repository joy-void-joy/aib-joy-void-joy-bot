"""Async and sync Metaculus API clients using httpx."""

import asyncio
import json
import logging
import os
import re
import time
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager
from pathlib import Path
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
    AggregationMethod,
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
        min_request_interval: float = 3.0,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.token = token or os.getenv("METACULUS_TOKEN")
        self.min_request_interval = min_request_interval
        self._managed_client: httpx.AsyncClient | None = None
        self._last_request_time: float = 0.0
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

    async def _throttle(self) -> None:
        """Enforce minimum delay between requests to avoid 429s."""
        if self._last_request_time > 0:
            elapsed = time.monotonic() - self._last_request_time
            remaining = self.min_request_interval - elapsed
            if remaining > 0:
                await asyncio.sleep(remaining)
        self._last_request_time = time.monotonic()

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
    async def fetch_aggregation_history(
        self,
        post_id: int,
    ) -> AggregationMethod:
        """Fetch CP history from the aggregation_explorer endpoint.

        Works for both open and resolved questions, unlike the posts API
        which returns null aggregations.
        """
        await self._throttle()
        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/aggregation_explorer/",
                headers=self._get_headers(),
                params={
                    "post_id": post_id,
                    "aggregation_methods": "recency_weighted",
                },
            )
            response.raise_for_status()
            data = response.json()

        recency = data.get("recency_weighted") or data.get("aggregations", {}).get(
            "recency_weighted"
        )
        if recency is None:
            return AggregationMethod()
        return AggregationMethod.model_validate(recency)

    @with_retry()
    async def fetch_post_json(
        self, post_id: int, *, with_cp: bool = False
    ) -> dict[str, Any]:
        """Fetch enriched post JSON by post ID.

        Returns the raw API JSON with content fields (description,
        resolution_criteria, fine_print) populated from the HTML
        fallback if the JSON API returns nulls.

        Args:
            with_cp: If True, include community prediction/aggregation data
                via with_cp and include_conditional_cps params.
        """
        await self._throttle()
        params: dict[str, str] = {}
        if with_cp:
            params["with_cp"] = "true"
            params["include_conditional_cps"] = "true"
        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/posts/{post_id}/",
                headers=self._get_headers(),
                params=params,
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

    async def get_question_by_url(
        self, url: str
    ) -> MetaculusQuestion | list[MetaculusQuestion]:
        """Fetch a question by its Metaculus URL.

        Handles both question and community URLs:
        - https://www.metaculus.com/questions/28841/some-slug/
        - https://www.metaculus.com/c/risk/38787/
        """
        post_id = self._parse_post_id_from_url(url)
        return await self.get_question_by_post_id(post_id)

    @staticmethod
    def _parse_post_id_from_url(url: str) -> int:
        """Extract post ID from a Metaculus question or community URL."""
        question_match = re.search(r"/questions/(\d+)", url)
        if question_match:
            return int(question_match.group(1))

        community_match = re.search(r"/c/[^/]+/(\d+)", url)
        if community_match:
            return int(community_match.group(1))

        raise ValueError(
            f"Could not extract post ID from URL: {url}. "
            "Expected format: /questions/<id>/... or /c/<slug>/<id>/"
        )

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
        return await self.get_questions_matching_filter(api_filter, with_cp=True)

    def _load_posts_override(
        self, api_filter: ApiFilter
    ) -> list[MetaculusQuestion] | None:
        """Load questions from a local JSON file instead of the API.

        Set METACULUS_POSTS_OVERRIDE to a path containing the raw API JSON
        response (the full {"results": [...], "count": N} object). Useful
        when rate-limited (429) — save the response once, then re-use it.
        """
        override_path = os.getenv("METACULUS_POSTS_OVERRIDE")
        if not override_path:
            return None

        path = Path(override_path)
        if not path.exists():
            logger.warning("METACULUS_POSTS_OVERRIDE file not found: %s", path)
            return None

        logger.info("Loading posts from override file: %s", path)
        data = json.loads(path.read_text())

        results = data.get("results", data) if isinstance(data, dict) else data

        questions: list[MetaculusQuestion] = []
        for post_json in results:
            if api_filter.allowed_statuses:
                post_status = post_json.get("status")
                if post_status not in api_filter.allowed_statuses:
                    continue
            parsed = self._parse_post_json(post_json, api_filter.group_question_mode)
            questions.extend(parsed)

        logger.info("Loaded %d questions from override file", len(questions))
        return questions

    @with_retry()
    async def get_questions_matching_filter(
        self,
        api_filter: ApiFilter,
        num_questions: int | None = None,
        *,
        with_cp: bool = False,
    ) -> list[MetaculusQuestion]:
        """Fetch questions matching a filter."""
        override = self._load_posts_override(api_filter)
        if override is not None:
            return override[:num_questions] if num_questions else override

        params = self._build_filter_params(api_filter, with_cp=with_cp)
        questions: list[MetaculusQuestion] = []
        offset = 0
        limit = 100

        async with self._http_client() as client:
            while True:
                params["offset"] = offset
                params["limit"] = limit

                await self._throttle()
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

        await self._throttle()
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
            return self._unpack_conditional(post_json)

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
            enriched_sub = {
                **sub_question_json,
                "fine_print": sub_question_json.get("fine_print")
                or group_json.get("fine_print"),
                "description": sub_question_json.get("description")
                or group_json.get("description"),
                "resolution_criteria": sub_question_json.get("resolution_criteria")
                or group_json.get("resolution_criteria"),
            }
            sub_post_json = {
                **post_json,
                "question": enriched_sub,
            }
            sub_post_json.pop("group_of_questions", None)
            questions.append(MetaculusQuestion.from_api_json(sub_post_json))

        return questions

    @staticmethod
    def _unpack_conditional(post_json: dict[str, Any]) -> list[MetaculusQuestion]:
        """Unpack a conditional post into its question_yes and question_no."""
        cond_json = post_json["conditional"]
        questions: list[MetaculusQuestion] = []

        for key in ("question_yes", "question_no"):
            sub_question_json = cond_json.get(key)
            if sub_question_json is None:
                continue
            sub_post_json = {
                **post_json,
                "question": sub_question_json,
            }
            sub_post_json.pop("conditional", None)
            questions.append(MetaculusQuestion.from_api_json(sub_post_json))

        return questions

    def _build_filter_params(
        self, api_filter: ApiFilter, *, with_cp: bool = False
    ) -> dict[str, Any]:
        """Build query parameters from an ApiFilter."""
        params: dict[str, Any] = {
            "order_by": api_filter.order_by,
        }

        if with_cp:
            params["with_cp"] = "true"
            params["include_conditional_cps"] = "true"

        if api_filter.allowed_statuses:
            params["statuses"] = ",".join(api_filter.allowed_statuses)

        if api_filter.allowed_tournaments:
            params["tournaments"] = ",".join(
                str(t) for t in api_filter.allowed_tournaments
            )

        if api_filter.allowed_types:
            types = list(api_filter.allowed_types)
            if (
                api_filter.group_question_mode == "unpack_subquestions"
                and "group_of_questions" not in types
            ):
                types.append("group_of_questions")
            params["forecast_type"] = ",".join(types)

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

        if api_filter.publish_time_gt:
            params["published_at__gt"] = api_filter.publish_time_gt.isoformat()

        if api_filter.publish_time_lt:
            params["published_at__lt"] = api_filter.publish_time_lt.isoformat()

        if api_filter.open_time_gt:
            params["open_time__gt"] = api_filter.open_time_gt.isoformat()

        if api_filter.open_time_lt:
            params["open_time__lt"] = api_filter.open_time_lt.isoformat()

        if api_filter.community_prediction_exists is not None:
            params["has_community_prediction"] = api_filter.community_prediction_exists

        params.update(api_filter.other_url_parameters)

        return params

    # --- Write Operations ---

    @with_retry()
    async def post_question_prediction(
        self, question_id: int, forecast_payload: dict[str, Any]
    ) -> None:
        """Submit a forecast prediction to Metaculus.

        Args:
            question_id: The question ID to submit the prediction for.
            forecast_payload: Dict with prediction data (e.g. probability_yes,
                continuous_cdf, probability_yes_per_category).
        """
        await self._throttle()
        request_body = [
            {
                "question": question_id,
                "source": "api",
                **forecast_payload,
            }
        ]
        async with self._http_client() as client:
            response = await client.post(
                f"{self.base_url}/questions/forecast/",
                json=request_body,
                headers=self._get_headers(),
            )
            response.raise_for_status()
        logger.info("Posted prediction on question %d", question_id)

    async def post_binary_question_prediction(
        self, question_id: int, prediction: float
    ) -> None:
        """Submit a binary prediction (probability between 0.001 and 0.999)."""
        if prediction < 0.001 or prediction > 0.999:
            raise ValueError("Prediction value must be between 0.001 and 0.999")
        await self.post_question_prediction(
            question_id, {"probability_yes": prediction}
        )

    async def post_numeric_question_prediction(
        self, question_id: int, cdf_values: list[float]
    ) -> None:
        """Submit a numeric/discrete prediction as a CDF."""
        if not all(0 <= x <= 1 for x in cdf_values):
            raise ValueError("All CDF values must be between 0 and 1")
        if not all(a <= b for a, b in zip(cdf_values, cdf_values[1:])):
            raise ValueError("CDF values must be monotonically increasing")
        await self.post_question_prediction(question_id, {"continuous_cdf": cdf_values})

    async def post_multiple_choice_question_prediction(
        self, question_id: int, options_with_probabilities: dict[str, float]
    ) -> None:
        """Submit a multiple choice prediction."""
        await self.post_question_prediction(
            question_id,
            {"probability_yes_per_category": options_with_probabilities},
        )

    @with_retry()
    async def post_question_comment(
        self,
        post_id: int,
        comment_text: str,
        *,
        is_private: bool = True,
        included_forecast: bool = True,
    ) -> None:
        """Post a comment on a Metaculus question."""
        await self._throttle()
        async with self._http_client() as client:
            response = await client.post(
                f"{self.base_url}/comments/create/",
                json={
                    "on_post": post_id,
                    "text": comment_text,
                    "is_private": is_private,
                    "included_forecast": included_forecast,
                },
                headers=self._get_headers(),
            )
            response.raise_for_status()
        logger.info("Posted comment on post %d", post_id)

    @with_retry()
    async def post_question_link(
        self,
        question1_id: int,
        question2_id: int,
        direction: int,
        strength: int,
        link_type: str,
    ) -> int:
        """Create a coherence link between two questions.

        Args:
            question1_id: First question ID.
            question2_id: Second question ID.
            direction: +1 for positive, -1 for negative.
            strength: 1 for low, 2 for medium, 5 for high.
            link_type: Link type (e.g., "causal").

        Returns:
            ID of the created link.
        """
        await self._throttle()
        async with self._http_client() as client:
            response = await client.post(
                f"{self.base_url}/coherence/links/create/",
                json={
                    "question1_id": question1_id,
                    "question2_id": question2_id,
                    "direction": direction,
                    "strength": strength,
                    "type": link_type,
                },
                headers=self._get_headers(),
            )
            response.raise_for_status()
            content = response.json()
        logger.info(
            "Created link between questions %d and %d", question1_id, question2_id
        )
        return content["id"]

    @with_retry()
    async def delete_question_link(self, link_id: int) -> None:
        """Delete a coherence link by ID."""
        await self._throttle()
        async with self._http_client() as client:
            response = await client.delete(
                f"{self.base_url}/coherence/links/{link_id}/delete/",
                headers=self._get_headers(),
            )
            response.raise_for_status()
        logger.info("Deleted link %d", link_id)

    @with_retry()
    async def fetch_question_json(self, question_id: int) -> dict[str, Any]:
        """Fetch raw question JSON by question ID (not post ID).

        Useful for resolving a question_id to its post_id.
        """
        await self._throttle()
        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/questions/{question_id}/",
                headers=self._get_headers(),
            )
            response.raise_for_status()
            return response.json()

    @with_retry()
    async def fetch_posts_list(self, params: dict[str, Any]) -> list[dict[str, Any]]:
        """Fetch a list of posts with arbitrary query parameters.

        Handles a single page of results. For pagination, call repeatedly
        with different offset values.
        """
        await self._throttle()
        async with self._http_client() as client:
            response = await client.get(
                f"{self.base_url}/posts/",
                headers=self._get_headers(),
                params=params,
            )
            response.raise_for_status()
            data = response.json()
            return data.get("results", [])


class MetaculusClient:
    """Sync wrapper around AsyncMetaculusClient."""

    def __init__(
        self,
        base_url: str = API_BASE_URL,
        timeout: float = 30.0,
        token: str | None = None,
        min_request_interval: float = 3.0,
    ) -> None:
        self._async = AsyncMetaculusClient(
            base_url=base_url,
            timeout=timeout,
            token=token,
            min_request_interval=min_request_interval,
        )

    @property
    def token(self) -> str | None:
        return self._async.token

    def _run(self, coro: Any) -> Any:
        return asyncio.run(coro)

    def fetch_post_json(self, post_id: int, *, with_cp: bool = False) -> dict[str, Any]:
        return self._run(self._async.fetch_post_json(post_id, with_cp=with_cp))

    def get_question_by_post_id(
        self, post_id: int
    ) -> MetaculusQuestion | list[MetaculusQuestion]:
        return self._run(self._async.get_question_by_post_id(post_id))

    def get_question_by_url(
        self, url: str
    ) -> MetaculusQuestion | list[MetaculusQuestion]:
        return self._run(self._async.get_question_by_url(url))

    @staticmethod
    def parse_post_id_from_url(url: str) -> int:
        return AsyncMetaculusClient._parse_post_id_from_url(url)

    def get_all_open_questions_from_tournament(
        self, tournament_id: int | str
    ) -> list[MetaculusQuestion]:
        return self._run(
            self._async.get_all_open_questions_from_tournament(tournament_id)
        )

    def get_questions_matching_filter(
        self,
        api_filter: ApiFilter,
        num_questions: int | None = None,
        *,
        with_cp: bool = False,
    ) -> list[MetaculusQuestion]:
        return self._run(
            self._async.get_questions_matching_filter(
                api_filter, num_questions, with_cp=with_cp
            )
        )

    def get_links_for_question(self, question_id: int) -> list[DetailedCoherenceLink]:
        return self._run(self._async.get_links_for_question(question_id))

    def fetch_aggregation_history(self, post_id: int) -> AggregationMethod:
        return self._run(self._async.fetch_aggregation_history(post_id))

    def post_question_prediction(
        self, question_id: int, forecast_payload: dict[str, Any]
    ) -> None:
        self._run(self._async.post_question_prediction(question_id, forecast_payload))

    def post_binary_question_prediction(
        self, question_id: int, prediction: float
    ) -> None:
        self._run(self._async.post_binary_question_prediction(question_id, prediction))

    def post_numeric_question_prediction(
        self, question_id: int, cdf_values: list[float]
    ) -> None:
        self._run(self._async.post_numeric_question_prediction(question_id, cdf_values))

    def post_multiple_choice_question_prediction(
        self, question_id: int, options_with_probabilities: dict[str, float]
    ) -> None:
        self._run(
            self._async.post_multiple_choice_question_prediction(
                question_id, options_with_probabilities
            )
        )

    def post_question_comment(
        self,
        post_id: int,
        comment_text: str,
        *,
        is_private: bool = True,
        included_forecast: bool = True,
    ) -> None:
        self._run(
            self._async.post_question_comment(
                post_id,
                comment_text,
                is_private=is_private,
                included_forecast=included_forecast,
            )
        )

    def post_question_link(
        self,
        question1_id: int,
        question2_id: int,
        direction: int,
        strength: int,
        link_type: str,
    ) -> int:
        return self._run(
            self._async.post_question_link(
                question1_id, question2_id, direction, strength, link_type
            )
        )

    def delete_question_link(self, link_id: int) -> None:
        self._run(self._async.delete_question_link(link_id))

    def fetch_question_json(self, question_id: int) -> dict[str, Any]:
        return self._run(self._async.fetch_question_json(question_id))

    def fetch_posts_list(self, params: dict[str, Any]) -> list[dict[str, Any]]:
        return self._run(self._async.fetch_posts_list(params))
