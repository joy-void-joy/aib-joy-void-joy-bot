"""Tests for source extraction.

What these pin is the coupling that has no compiler: a registry keyed by
tool name against a tool surface that gets renamed. Every entry is checked
against the surface the forecaster is actually granted, because an entry
naming a tool nobody calls matches nothing and says so to no one — which
is how four Metaculus entries sat under a server prefix that had moved.
"""

import json

import pytest
from lup.runtime.models import (
    AnyTurnBlock,
    TurnMessage,
    TurnToolCallBlock,
    TurnToolResultBlock,
)
from lup.types import JsonObject, JsonValue

from aib.agent.sources import (
    AUGMENTED_SEARCH_TOOL,
    FETCH_TOOL,
    SOURCE_TOOLS,
    ApiSourceTool,
    PublishedSourceTool,
    Source,
    extract_sources,
    format_source,
    input_values,
    walk_urls,
)
from aib.agent.tool_policy import ToolPolicy


@pytest.fixture(autouse=True)
def no_title_lookups(monkeypatch: pytest.MonkeyPatch) -> None:
    """`fetch_title` reaches the network, and a unit test must not.

    It also makes the suite order-dependent in a way that hides itself: a
    reachable host answers with the page's own title and an unreachable one
    with nothing, so a test asserting either passes only sometimes.
    """
    monkeypatch.setattr("aib.agent.sources.fetch_title", lambda url: "")


def called(name: str, arguments: JsonObject, call_id: str = "c1") -> TurnMessage:
    """One assistant message carrying one tool call."""
    blocks: list[AnyTurnBlock] = [
        TurnToolCallBlock(id=call_id, name=name, arguments=arguments)
    ]
    return TurnMessage(role="assistant", blocks=blocks)


def answered(payload: JsonValue, call_id: str = "c1") -> TurnMessage:
    """One tool message carrying that call's result."""
    blocks: list[AnyTurnBlock] = [
        TurnToolResultBlock(tool_call_id=call_id, content=json.dumps(payload))
    ]
    return TurnMessage(role="tool", blocks=blocks)


class TestRegistryMatchesTheGrantedSurface:
    """A key that names no granted tool is an entry that never fires."""

    def granted(self) -> set[str]:
        policy = ToolPolicy(
            research="condensed", metaculus_token="t", census_api_key="c"
        )
        return set(policy.orchestrator_allowlist())

    def test_every_registry_key_is_a_tool_the_forecaster_holds(self) -> None:
        assert set(SOURCE_TOOLS) <= self.granted()

    def test_the_two_named_tools_are_held_too(self) -> None:
        """`search` and `fetch` are matched by name rather than by registry."""
        assert {AUGMENTED_SEARCH_TOOL, FETCH_TOOL} <= self.granted()

    def test_the_data_surface_is_not_silently_unattributed(self) -> None:
        """Every granted data tool either names sources or provably has none.

        `census` and `weather` answer with figures rather than documents, so
        they have no URL to attribute — which is a fact worth stating here,
        because the way this file rots is a tool quietly leaving the set.
        """
        sourceless = {
            "mcp__government__census",
            "mcp__weather__weather",
        }
        data_tools = {
            tool
            for tool in self.granted()
            if tool.startswith("mcp__")
            and tool.split("__")[1]
            in ("search", "financial", "markets", "trends", "government", "weather")
        }
        attributed = set(SOURCE_TOOLS) | {AUGMENTED_SEARCH_TOOL, FETCH_TOOL}
        assert data_tools - attributed == sourceless


class TestInputValues:
    """One argument, whether it holds one thing or several."""

    def test_a_scalar_is_one_value(self) -> None:
        assert input_values({"symbol": "MSFT"}, "symbol") == ["MSFT"]

    def test_a_list_is_every_value(self) -> None:
        assert input_values({"terms": ["a", "b"]}, "terms") == ["a", "b"]

    def test_an_absent_argument_is_no_value(self) -> None:
        assert input_values({}, "symbol") == []

    def test_an_empty_argument_is_no_value(self) -> None:
        assert input_values({"symbol": ""}, "symbol") == []


class TestCallNamedSources:
    """Tools whose reference URL follows from what they were asked for."""

    def test_a_ticker_becomes_its_quote_page(self) -> None:
        sources = extract_sources([called("mcp__financial__stock", {"symbol": "MSFT"})])
        assert sources == ["[(yfinance) MSFT](https://finance.yahoo.com/quote/MSFT)"]

    def test_every_term_of_a_trends_call_is_a_source(self) -> None:
        sources = extract_sources(
            [called("mcp__trends__trends", {"terms": ["Milei", "Massa"]})]
        )
        assert len(sources) == 2
        assert "Milei" in sources[0]

    def test_a_term_with_a_space_is_escaped_into_the_url(self) -> None:
        """A raw space makes a link that does not resolve."""
        sources = extract_sources(
            [called("mcp__trends__trends", {"terms": ["dengue Brazil"]})]
        )
        assert "dengue%20Brazil" in sources[0]
        assert "(Google Trends) dengue Brazil" in sources[0]


class TestPublishedSources:
    """`series` addresses whichever body it was told to."""

    @pytest.mark.parametrize(
        ("source", "series_id", "expected"),
        [
            ("fred", "UNRATE", "https://fred.stlouisfed.org/series/UNRATE"),
            (
                "worldbank",
                "NY.GDP.MKTP.KD.ZG",
                "https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG",
            ),
            ("bls", "LNS14000000", "https://data.bls.gov/timeseries/LNS14000000"),
        ],
    )
    def test_each_publisher_is_addressed_in_its_own_namespace(
        self, source: str, series_id: str, expected: str
    ) -> None:
        sources = extract_sources(
            [
                called(
                    "mcp__financial__series",
                    {"source": source, "series_ids": [series_id]},
                )
            ]
        )
        assert expected in sources[0]

    def test_every_id_of_a_multi_series_call_is_a_source(self) -> None:
        sources = extract_sources(
            [
                called(
                    "mcp__financial__series",
                    {"source": "bls", "series_ids": ["A", "B", "C"]},
                )
            ]
        )
        assert len(sources) == 3

    def test_an_unknown_publisher_names_nothing(self) -> None:
        """A guessed template makes a link that resolves to nothing."""
        entry = SOURCE_TOOLS["mcp__financial__series"]
        assert isinstance(entry, PublishedSourceTool)
        assert entry.sources({"source": "eurostat", "series_ids": ["X"]}) == []


class TestSearchSources:
    """A search names what it read, not everything it listed."""

    def hit(self, url: str, **extra: JsonValue) -> JsonObject:
        base: JsonObject = {
            "title": "T",
            "url": url,
            "snippet": "s",
            "api_data": None,
            "hint": None,
            "text": None,
        }
        return base | extra

    def test_a_hit_whose_page_was_fetched_is_a_source(self) -> None:
        payload: JsonObject = {
            "web": [self.hit("https://example.org/a", text="the page")]
        }
        sources = extract_sources(
            [called(AUGMENTED_SEARCH_TOOL, {"query": "x"}), answered(payload)]
        )
        assert sources == ["[T](https://example.org/a)"]

    def test_a_hit_answered_from_an_api_is_a_source(self) -> None:
        payload: JsonObject = {
            "web": [self.hit("https://example.org/b", api_data={"k": 1})]
        }
        sources = extract_sources(
            [called(AUGMENTED_SEARCH_TOOL, {"query": "x"}), answered(payload)]
        )
        assert sources == ["[T](https://example.org/b)"]

    def test_a_hit_that_was_only_listed_is_not_a_source(self) -> None:
        """Nine lanes of candidates would otherwise read as nine lanes consulted."""
        payload: JsonObject = {"web": [self.hit("https://example.org/c")]}
        sources = extract_sources(
            [called(AUGMENTED_SEARCH_TOOL, {"query": "x"}), answered(payload)]
        )
        assert sources == []

    def test_the_listing_lanes_are_not_sources(self) -> None:
        payload: JsonObject = {
            "web": [],
            "markets": [{"market_title": "M", "url": "https://polymarket.com/x"}],
            "papers": [{"title": "P", "url": "https://arxiv.org/abs/1"}],
        }
        sources = extract_sources(
            [called(AUGMENTED_SEARCH_TOOL, {"query": "x"}), answered(payload)]
        )
        assert sources == []


class TestFetchSources:
    """A fetch names the document it read, not the reference it was given."""

    def test_a_bare_paper_id_is_recorded_as_the_paper_url(self) -> None:
        """`fetch(ref="2301.12345")` — the id is not a source, the paper is.

        `fetch` titles a paper with its id, which is what identifies one and
        spares the extraction a network lookup for a title arXiv's own
        answer never carried.
        """
        payload: JsonObject = {
            "ref": "2301.12345",
            "url": "https://arxiv.org/abs/2301.12345",
            "title": "2301.12345",
        }
        sources = extract_sources(
            [called(FETCH_TOOL, {"ref": "2301.12345"}), answered(payload)]
        )
        assert sources == ["[2301.12345](https://arxiv.org/abs/2301.12345)"]

    def test_an_archived_copy_is_recorded_as_the_archived_url(self) -> None:
        payload: JsonObject = {
            "ref": "https://example.org",
            "url": "https://web.archive.org/web/20260530/https://example.org",
            "archived_at": "20260530",
        }
        sources = extract_sources(
            [
                called(FETCH_TOOL, {"ref": "https://example.org", "at": "2026-06-01"}),
                answered(payload),
            ]
        )
        assert "web.archive.org" in sources[0]

    def test_a_page_keeps_its_own_title(self) -> None:
        payload: JsonObject = {"url": "https://example.org/r", "title": "The Report"}
        sources = extract_sources(
            [called(FETCH_TOOL, {"ref": "https://example.org/r"}), answered(payload)]
        )
        assert sources == ["[The Report](https://example.org/r)"]


class TestResultWalkedSources:
    """Tools whose URLs are in the answer."""

    def test_a_metaculus_question_is_recorded_from_its_answer(self) -> None:
        payload: JsonObject = {
            "post_id": 44798,
            "question": {"title": "Q", "url": "https://metaculus.com/questions/44798"},
        }
        sources = extract_sources(
            [called("mcp__markets__metaculus", {"post_id": 44798}), answered(payload)]
        )
        assert sources == ["[(Metaculus) Q](https://metaculus.com/questions/44798)"]

    def test_a_kalshi_ladder_is_recorded_from_its_event(self) -> None:
        payload: JsonObject = {
            "source": "kalshi",
            "market_id": "KXFED-26APR-T425",
            "event": {
                "event_ticker": "KXFED-26APR",
                "event_title": "Fed April",
                "url": "https://kalshi.com/markets/KXFED-26APR",
            },
        }
        sources = extract_sources(
            [
                called("mcp__markets__market", {"source": "kalshi", "market_id": "x"}),
                answered(payload),
            ]
        )
        assert "Fed April" in sources[0]

    def test_a_trace_with_no_ladder_names_nothing_new(self) -> None:
        payload: JsonObject = {
            "source": "polymarket",
            "market_id": "7194",
            "history": [],
        }
        sources = extract_sources(
            [
                called("mcp__markets__market", {"source": "polymarket"}),
                answered(payload),
            ]
        )
        assert sources == []


class TestWalkUrls:
    """The recursion that reads a record's own address."""

    def test_a_record_uses_its_own_url_not_its_children(self) -> None:
        data: JsonObject = {
            "title": "Outer",
            "url": "https://example.org/outer",
            "inner": {"url": "https://example.org/inner"},
        }
        assert [s.url for s in walk_urls(data)] == ["https://example.org/outer"]

    def test_a_record_without_a_url_yields_its_children(self) -> None:
        data: JsonObject = {
            "inner": {"title": "In", "url": "https://example.org/inner"}
        }
        assert [s.url for s in walk_urls(data)] == ["https://example.org/inner"]

    def test_a_non_http_value_is_not_a_url(self) -> None:
        assert list(walk_urls({"url": "not-a-url"})) == []


class TestExtractSourcesShape:
    """What the whole pass answers with."""

    def test_a_url_seen_twice_is_written_once(self) -> None:
        messages = [
            called("mcp__financial__stock", {"symbol": "MSFT"}, call_id="a"),
            called("mcp__financial__stock", {"symbol": "MSFT"}, call_id="b"),
        ]
        assert len(extract_sources(messages)) == 1

    def test_a_result_without_its_call_is_ignored(self) -> None:
        """An id nothing registered has no reading, so it is not guessed at."""
        assert extract_sources([answered({"web": []}, call_id="orphan")]) == []

    def test_an_unparseable_result_costs_nothing(self) -> None:
        messages = [
            called(AUGMENTED_SEARCH_TOOL, {"query": "x"}),
            TurnMessage(
                role="tool",
                blocks=[TurnToolResultBlock(tool_call_id="c1", content="not json")],
            ),
        ]
        assert extract_sources(messages) == []

    def test_an_untracked_tool_names_nothing(self) -> None:
        assert extract_sources([called("mcp__sandbox__execute_code", {})]) == []


class TestFormatSource:
    """How a source reads in the comment it is posted in."""

    def test_a_labelled_source_shows_its_label(self) -> None:
        source = Source(url="https://x.org", title="T", label="FRED")
        assert format_source(source) == "[(FRED) T](https://x.org)"

    def test_a_source_without_a_title_falls_back_to_its_domain(self) -> None:
        source = Source(url="https://www.example.org/a")
        assert format_source(source) == "[example.org](https://www.example.org/a)"

    def test_brackets_in_a_title_do_not_break_the_link(self) -> None:
        """A stray bracket would close the link text early."""
        source = Source(url="https://x.org", title="[draft] T")
        assert format_source(source) == "[draft] T](https://x.org)"


def test_the_registry_entries_all_declare_a_reachable_shape() -> None:
    """Every entry is one of the three readings, and none is left unhandled."""
    for name, entry in SOURCE_TOOLS.items():
        assert entry.kind in ("api", "published", "result"), name
        if isinstance(entry, ApiSourceTool):
            assert "{}" in entry.url_template, name
        if isinstance(entry, PublishedSourceTool):
            assert entry.publishers, name
            for publisher in entry.publishers.values():
                assert "{}" in publisher.url_template, name
