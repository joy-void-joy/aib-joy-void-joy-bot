"""Tests for the condensed tool surface.

What these pin is the machinery that makes one wide tool safe to prefer over
several narrow ones: a lane that fails must cost its own line rather than the
answer, a lane that cannot honour a cutoff must not be asked during a
backtest, and a merged tool must send each request to the right one of the
implementations it now stands in front of.
"""

import asyncio
from datetime import date
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
from pydantic import BaseModel

from aib.retrodict_context import retrodict_cutoff
from aib.tools.fanout import LaneFailure, run_lane
from aib.tools.financial import (
    FredSeriesInfo,
    FredSeriesInput,
    FredSeriesOutput,
    SeriesInput,
    year_bound,
)
from aib.tools.exa import ExaResult
from aib.tools.fetch_http import abridged, downloads_dir
from aib.tools.government import BLSSeriesInput, BLSSeriesOutput
from aib.tools.search import (
    SEARCH_LANES,
    FetchInput,
    NewsArticle,
    SearchExaOutput,
    SearchInput,
    available_lanes,
    lane_neural,
    parse_asknews_items,
    search,
)
from lup.mcp import ToolError


class TestLaneMetrics:
    """Nine sources behind one tool still have to be countable separately."""

    @pytest.mark.asyncio
    async def test_a_lane_that_runs_records_itself(self) -> None:
        """`search`'s own row counts the fan-out, not the sources inside it."""
        from lup.telemetry.metrics import collector

        answer = SearchExaOutput(query="x", results=[])
        collector.reset()
        with patch("aib.tools.search.search_exa", new=AsyncMock(return_value=answer)):
            await lane_neural(SearchInput(query="x"))

        by_tool = collector.get_summary()["by_tool"]
        assert by_tool["search_lane_neural"]["call_count"] == 1

    @pytest.mark.asyncio
    async def test_a_lane_that_fails_records_the_failure(self) -> None:
        """A lane down for a week is otherwise visible only inside a payload."""
        from lup.telemetry.metrics import collector

        collector.reset()
        with patch("aib.tools.search.search_exa", new=AsyncMock(side_effect=OSError)):
            await search(SearchInput(query="x", lanes=["neural"]))

        assert collector.get_summary()["by_tool"]["search_lane_neural"]["error_count"]

    @pytest.mark.asyncio
    async def test_the_news_lane_is_the_asknews_meter(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """AskNews is metered per request and no longer has a tool name.

        `lup-devtools usage` reads these rows for the monthly and tournament
        quotas, so a lane that stopped recording would read as spend that
        never happened — while the lane fires on every search.
        """
        from aib.config import settings as live_settings
        from aib.devtools.usage import asknews_tool_names
        from lup.telemetry.metrics import collector

        monkeypatch.setattr(live_settings, "asknews_api_key", "k")
        collector.reset()

        payload = AsyncMock(return_value='[{"title": "T", "snippet": "S"}]')
        with patch("aib.tools.asknews._call_remote", new=payload):
            out = await search(SearchInput(query="x", lanes=["news"]))

        assert [a["title"] for a in out.news] == ["T"]
        counted = sum(
            collector.get_summary()["by_tool"].get(name, {}).get("call_count", 0)
            for name in asknews_tool_names()
        )
        assert counted == 1


class TestRunLane:
    """One source's outage costs a line, not the answer."""

    @pytest.mark.asyncio
    async def test_a_lane_that_answers_returns_its_answer(self) -> None:
        failures: list[LaneFailure] = []

        async def works() -> list[int]:
            return [1, 2]

        assert await run_lane("w", works(), [], failures) == [1, 2]
        assert failures == []

    @pytest.mark.asyncio
    async def test_a_lane_that_raises_is_recorded_not_propagated(self) -> None:
        failures: list[LaneFailure] = []

        async def breaks() -> list[int]:
            raise ValueError("upstream is down")

        assert await run_lane("b", breaks(), [], failures) == []
        assert failures == [LaneFailure(lane="b", reason="upstream is down")]

    @pytest.mark.asyncio
    async def test_a_silent_exception_still_names_itself(self) -> None:
        """`str(exc)` is empty for plenty of exceptions; the type is not."""
        failures: list[LaneFailure] = []

        async def breaks() -> list[int]:
            raise RuntimeError

        await run_lane("b", breaks(), [], failures)
        assert failures[0]["reason"] == "RuntimeError"

    @pytest.mark.asyncio
    async def test_a_lane_past_its_deadline_reports_itself_cold(self) -> None:
        """A source whose own backoff outlasts the tool asking it."""
        failures: list[LaneFailure] = []

        async def slow() -> list[int]:
            await asyncio.sleep(5)
            return [1]

        assert await run_lane("s", slow(), [], failures, deadline=0.01) == []
        assert failures[0]["lane"] == "s"
        assert "within" in failures[0]["reason"]


class TestAbridged:
    """A page is opened inline and finished from disk."""

    def test_a_short_page_is_carried_whole(self, tmp_path: Path) -> None:
        """Nothing is written for a page that already fits."""
        token = downloads_dir.set(tmp_path)
        try:
            assert abridged("https://example.org", "short", keep=100) == "short"
        finally:
            downloads_dir.reset(token)
        assert not (tmp_path / "pages").exists()

    def test_a_long_page_is_previewed_and_pointed_at(self, tmp_path: Path) -> None:
        token = downloads_dir.set(tmp_path)
        try:
            text = abridged("https://example.org", "a" * 500, keep=100)
        finally:
            downloads_dir.reset(token)

        assert text.startswith("a" * 100)
        assert "[... continued in " in text
        assert len(text) < 500

    def test_the_path_it_names_holds_the_whole_page(self, tmp_path: Path) -> None:
        """The preview is only honest if the rest is really there."""
        whole = "".join(f"line {i}\n" for i in range(500))
        token = downloads_dir.set(tmp_path)
        try:
            text = abridged("https://example.org", whole, keep=100)
        finally:
            downloads_dir.reset(token)

        named = text.rsplit("[... continued in ", 1)[1].rstrip("]")
        assert Path(named).read_text(encoding="utf-8") == whole

    def test_one_url_lands_in_one_place(self, tmp_path: Path) -> None:
        """Named by the URL, so the same page twice is one file."""
        token = downloads_dir.set(tmp_path)
        try:
            abridged("https://example.org", "b" * 500, keep=10)
            abridged("https://example.org", "b" * 500, keep=10)
        finally:
            downloads_dir.reset(token)

        assert len(list((tmp_path / "pages").iterdir())) == 1


class TestAvailableLanes:
    """A lane is asked only where it could answer."""

    def test_every_lane_is_a_declared_lane(self) -> None:
        assert set(available_lanes()) <= set(SEARCH_LANES)

    def test_a_lane_without_its_credential_is_not_asked(self) -> None:
        """Absent key means the lane is dropped, not reported failed.

        `failed` says "this source had something to say and could not say
        it", which an unconfigured key is not.
        """
        with patch("aib.tools.search.settings") as fake:
            fake.exa_api_key = None
            fake.asknews_api_key = "k"
            fake.reddit_client_id = "i"
            fake.reddit_client_secret = "s"
            fake.metaculus_token = "t"
            assert "neural" not in available_lanes()
            assert "news" in available_lanes()

    def test_reddit_needs_both_halves_of_its_credential(self) -> None:
        with patch("aib.tools.search.settings") as fake:
            fake.exa_api_key = "e"
            fake.asknews_api_key = "k"
            fake.reddit_client_id = "i"
            fake.reddit_client_secret = None
            fake.metaculus_token = "t"
            assert "social" not in available_lanes()

    def test_the_undateable_lanes_are_withheld_from_a_backtest(self) -> None:
        """News and social carry no date this can filter on.

        The web lane is reachable under a cutoff because it runs Wayback
        validation; these two have nothing equivalent, so asking them during
        a backtest would answer with today's world.
        """
        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            with patch("aib.tools.search.settings") as fake:
                fake.exa_api_key = "e"
                fake.asknews_api_key = "k"
                fake.reddit_client_id = "i"
                fake.reddit_client_secret = "s"
                fake.metaculus_token = "t"
                lanes = available_lanes()
                assert "news" not in lanes
                assert "social" not in lanes
                assert "web" in lanes
        finally:
            retrodict_cutoff.reset(token)


class TestSearchLaneSelection:
    """`lanes` narrows; omitting it asks everything reachable."""

    @pytest.mark.asyncio
    async def test_an_unknown_lane_is_refused_by_name(self) -> None:
        with pytest.raises(ToolError, match="Unknown lane"):
            await search(SearchInput(query="x", lanes=["telepathy"]))

    @pytest.mark.asyncio
    async def test_only_the_named_lane_runs(self) -> None:
        with patch(
            "aib.tools.search.lane_markets", new=AsyncMock(return_value=[])
        ) as m:
            with patch(
                "aib.tools.search.lane_web", new=AsyncMock(return_value=[])
            ) as w:
                out = await search(SearchInput(query="x", lanes=["markets"]))

        m.assert_awaited_once()
        w.assert_not_awaited()
        assert out.lanes_run == ["markets"]

    @pytest.mark.asyncio
    async def test_a_failing_lane_leaves_the_others_standing(self) -> None:
        async def breaks(_: SearchInput) -> list[NewsArticle]:
            raise ValueError("polymarket 503")

        hit = ExaResult(
            title="T",
            url="https://example.org",
            snippet="S",
            highlights=None,
            published_date=None,
            score=None,
        )
        with patch("aib.tools.search.lane_markets", new=breaks):
            with patch(
                "aib.tools.search.lane_neural", new=AsyncMock(return_value=[hit])
            ):
                out = await search(SearchInput(query="x", lanes=["markets", "neural"]))

        assert out.neural == [hit]
        assert out.markets == []
        assert [f["lane"] for f in out.failed] == ["markets"]


class TestParseAskNewsItems:
    """The vendor names its list three ways and its body three more."""

    def test_reads_a_bare_list(self) -> None:
        payload = '[{"title": "T", "snippet": "S", "url": "U"}]'
        assert parse_asknews_items(payload) == [
            NewsArticle(title="T", snippet="S", url="U")
        ]

    def test_reads_whichever_key_holds_the_list(self) -> None:
        for key in ("results", "articles", "data"):
            payload = '{"%s": [{"title": "T", "summary": "S", "url": "U"}]}' % key
            assert parse_asknews_items(payload)[0]["snippet"] == "S"

    def test_an_unparseable_payload_is_no_articles_rather_than_a_raise(self) -> None:
        assert parse_asknews_items("not json") == []

    def test_an_item_without_a_title_is_not_an_article(self) -> None:
        assert parse_asknews_items('[{"snippet": "S"}]') == []


class TestFetchRouting:
    """A ref that is not a URL is a paper id; `at` is the archived copy."""

    @pytest.mark.asyncio
    async def test_a_url_goes_to_the_page_fetcher(self) -> None:
        from aib.tools.search import FetchedPage

        page = FetchedPage(url="https://example.org/a", content="body", title="T")
        with patch("aib.tools.search.fetch_url", new=AsyncMock(return_value=page)):
            out = await fetch_ref("https://example.org/a")

        assert out.content == "body"
        assert out.paper is None

    @pytest.mark.asyncio
    async def test_a_bare_id_goes_to_arxiv(self) -> None:
        from aib.tools.arxiv_search import ArxivHtmlPaper

        paper = ArxivHtmlPaper(
            paper_id="2301.12345", url="https://arxiv.org/abs/2301.12345", content="C"
        )
        with patch("aib.tools.search.fetch_arxiv", new=AsyncMock(return_value=paper)):
            out = await fetch_ref("2301.12345")

        assert out.paper is not None
        assert out.content == "C"
        assert out.title == "2301.12345"

    @pytest.mark.asyncio
    async def test_an_arxiv_url_is_not_special_cased(self) -> None:
        """`fetch_url` already routes arxiv.org to `fetch_arxiv` itself."""
        from aib.tools.search import FetchedPage

        page = FetchedPage(url="https://arxiv.org/abs/2301.12345", routed={"id": "x"})
        with patch(
            "aib.tools.search.fetch_url", new=AsyncMock(return_value=page)
        ) as page_fetch:
            with patch("aib.tools.search.fetch_arxiv", new=AsyncMock()) as arxiv_fetch:
                await fetch_ref("https://arxiv.org/abs/2301.12345")

        page_fetch.assert_awaited_once()
        arxiv_fetch.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_a_date_asks_the_archive(self) -> None:
        from aib.tools.wayback import WaybackSnapshotResult

        snapshot = WaybackSnapshotResult(
            url="https://example.org",
            requested_date="20260601",
            snapshot_date="20260530",
            snapshot_url="https://web.archive.org/…",
            content="as it stood",
        )
        with patch(
            "aib.tools.search.wayback_snapshot", new=AsyncMock(return_value=snapshot)
        ):
            out = await fetch_ref("https://example.org", at="2026-06-01")

        assert out.content == "as it stood"
        assert out.archived_at == "20260530"


async def fetch_ref(ref: str, at: str | None = None):
    """Call `fetch` the way an agent would, without repeating the model."""
    from aib.tools.search import fetch

    return await fetch(FetchInput(ref=ref, at=at))


class TestYearBound:
    """A window bound is a date for FRED and a year for the other two."""

    def test_a_year_parses(self) -> None:
        assert year_bound("2024", "start") == 2024

    def test_absent_stays_absent(self) -> None:
        assert year_bound(None, "start") is None

    def test_a_date_is_refused_with_the_field_that_was_wrong(self) -> None:
        """Refused rather than sliced: guessing the year out of a date string
        would be reading structure off characters."""
        with pytest.raises(ToolError, match="start='2024-01-01'"):
            year_bound("2024-01-01", "start")


def sole_argument[T: BaseModel](call: AsyncMock, model: type[T]) -> T:
    """The one input model a merged tool sent on to its implementation.

    Naming the model is half the assertion: a merged tool's job is to build
    the right request, and sending a well-formed one to the wrong publisher
    would otherwise read as a pass.
    """
    awaited = call.await_args
    assert awaited is not None, "expected the implementation to be awaited"
    sent = awaited.args[0]
    assert isinstance(sent, model)
    return sent


class TestSeriesDispatch:
    """Each publisher is asked in its own namespace."""

    @pytest.mark.asyncio
    async def test_the_world_bank_needs_a_country(self) -> None:
        with pytest.raises(ToolError, match="needs a country"):
            await series_call(
                SeriesInput(source="worldbank", series_ids=["NY.GDP.MKTP.KD.ZG"])
            )

    @pytest.mark.asyncio
    async def test_fred_reads_the_first_id_and_the_dates(self) -> None:
        answer = FredSeriesOutput(
            series=FredSeriesInfo(
                id="UNRATE",
                title="Unemployment Rate",
                frequency="Monthly",
                units="Percent",
                seasonal_adjustment="SA",
                last_updated="2026-08-01",
            ),
            observation_start="2020-01-01",
            observation_end="2026-08-01",
            data_points=0,
            observations=[],
        )
        with patch(
            "aib.tools.financial.fred_series", new=AsyncMock(return_value=answer)
        ) as call:
            out = await series_call(
                SeriesInput(source="fred", series_ids=["UNRATE"], start="2020-01-01")
            )

        sent = sole_argument(call, FredSeriesInput)
        assert sent.series_id == "UNRATE"
        assert sent.observation_start == "2020-01-01"
        assert out.source == "fred"
        assert out.bls is None

    @pytest.mark.asyncio
    async def test_bls_reads_every_id_at_once(self) -> None:
        answer = BLSSeriesOutput(
            start_year=2024, end_year=2026, series_count=0, series=[]
        )
        with patch(
            "aib.tools.financial.bls_series", new=AsyncMock(return_value=answer)
        ) as call:
            out = await series_call(
                SeriesInput(source="bls", series_ids=["A", "B"], start="2024")
            )

        sent = sole_argument(call, BLSSeriesInput)
        assert sent.series_ids == ["A", "B"]
        assert sent.start_year == 2024
        assert out.source == "bls"
        assert out.fred is None


async def series_call(params: SeriesInput):
    """Call `series` without repeating the import at every use."""
    from aib.tools.financial import series

    return await series(params)


class TestRefusedCredential:
    """A key that is present and rejected is not a working lane."""

    def test_a_refusal_retires_the_news_lane(self, monkeypatch: object) -> None:
        """The case the configuration gate cannot see.

        An absent key is left out rather than asked. A key the account may
        not use reads as configured, so the lane wires in and answers 403
        to every question the run asks — the same refusal bought again per
        search. The first one retires it.
        """
        from aib.tools import asknews
        from aib.tools.search import available_lanes

        asknews.refusals.clear()
        try:
            assert asknews.account_refused() is None
            asknews.refusals.append("403000 - reserved for higher tiers")
            assert asknews.account_refused() is not None
            assert "news" not in available_lanes()
        finally:
            asknews.refusals.clear()


class TestUnreachableWebLane:
    """A lane that could not ask is not a lane that found nothing."""

    async def test_an_unreachable_lane_is_recorded_as_failed(self) -> None:
        """`failed` is what tells the agent whether to ask again.

        A lane whose provider refused the request answers with an empty
        list, which reads in the payload exactly like a query the web had
        nothing for unless the refusal is carried alongside it.
        """
        failures: list[LaneFailure] = []

        async def unreachable() -> list[str]:
            raise ValueError("Exa API client error 401: invalid key")

        result = await run_lane("web", unreachable(), [], failures)

        assert result == []
        assert [f["lane"] for f in failures] == ["web"]
        assert "401" in failures[0]["reason"]
