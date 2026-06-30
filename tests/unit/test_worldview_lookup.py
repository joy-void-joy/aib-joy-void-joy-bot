"""Tests for worldview store CRUD, amend, and staleness computation."""

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from aib.agent.models import ForecastOutput
from aib.worldview.models import (
    EntryState,
    WorldviewForecastEntry,
    WorldviewResearchEntry,
)


@pytest.fixture
def worldview_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Create a temporary worldview directory and patch paths globally."""
    (tmp_path / "research").mkdir()
    (tmp_path / "forecasts").mkdir()
    (tmp_path / "archive").mkdir()

    from aib import paths
    from aib.worldview import lookup

    monkeypatch.setattr(paths, "WORLDVIEW_PATH", tmp_path)
    monkeypatch.setattr(paths, "WORLDVIEW_FORECASTS_PATH", tmp_path / "forecasts")
    monkeypatch.setattr(paths, "WORLDVIEW_RESEARCH_PATH", tmp_path / "research")
    monkeypatch.setattr(paths, "WORLDVIEW_ARCHIVE_PATH", tmp_path / "archive")
    monkeypatch.setattr(lookup, "WORLDVIEW_PATH", tmp_path)
    monkeypatch.setattr(lookup, "WORLDVIEW_FORECASTS_PATH", tmp_path / "forecasts")
    monkeypatch.setattr(lookup, "WORLDVIEW_RESEARCH_PATH", tmp_path / "research")
    monkeypatch.setattr(lookup, "WORLDVIEW_ARCHIVE_PATH", tmp_path / "archive")

    return tmp_path


def make_forecast(
    slug: str = "test-forecast-abcd1234",
    **overrides: object,
) -> WorldviewForecastEntry:
    now = datetime.now(timezone.utc)
    defaults: dict[str, object] = {
        "slug": slug,
        "question": "Test question?",
        "question_type": "binary",
        "probability": 0.6,
        "summary": "Test summary",
        "created_at": now - timedelta(hours=24),
        "updated_at": now - timedelta(hours=12),
        "stale_after": now + timedelta(hours=24),
        "state": EntryState.fresh,
        "tags": [],
    }
    defaults.update(overrides)
    return WorldviewForecastEntry.model_validate(defaults)


def make_research(
    slug: str = "test-research-abcd1234",
    **overrides: object,
) -> WorldviewResearchEntry:
    now = datetime.now(timezone.utc)
    defaults: dict[str, object] = {
        "slug": slug,
        "query": "Test query?",
        "answer": "Test answer",
        "created_at": now - timedelta(hours=24),
        "updated_at": now - timedelta(hours=12),
        "stale_after": now + timedelta(hours=24),
        "state": EntryState.fresh,
    }
    defaults.update(overrides)
    return WorldviewResearchEntry.model_validate(defaults)


class TestSaveLoadRoundTrip:
    def test_forecast_save_load(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import load_forecast_entry, save_forecast_entry

        entry = make_forecast()
        save_forecast_entry(entry)
        loaded = load_forecast_entry(entry.slug)

        assert loaded is not None
        assert loaded.slug == entry.slug
        assert loaded.probability == entry.probability
        assert loaded.question == entry.question

    def test_research_save_load(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import load_research_entry, save_research_entry

        entry = make_research()
        save_research_entry(entry)
        loaded = load_research_entry(entry.slug)

        assert loaded is not None
        assert loaded.slug == entry.slug
        assert loaded.answer == entry.answer

    def test_load_nonexistent_returns_none(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import load_forecast_entry, load_research_entry

        assert load_forecast_entry("nonexistent-slug-00000000") is None
        assert load_research_entry("nonexistent-slug-00000000") is None


class TestAmend:
    def test_amend_forecast_updates_field(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import amend_forecast_entry, save_forecast_entry

        entry = make_forecast(probability=0.5)
        save_forecast_entry(entry)

        amended = amend_forecast_entry(
            entry.slug,
            updates={"probability": 0.7},
            reason="Adjusted to match CDF",
        )

        assert amended is not None
        assert amended.probability == 0.7
        assert len(amended.revision_history) == 1
        assert amended.revision_history[0].reason == "Adjusted to match CDF"
        assert "probability" in amended.revision_history[0].fields_changed

    def test_amend_research_updates_field(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import amend_research_entry, save_research_entry

        entry = make_research(key_facts=["fact 1"])
        save_research_entry(entry)

        amended = amend_research_entry(
            entry.slug,
            updates={"key_facts": ["fact 1", "fact 2"]},
            reason="Added new findings",
        )

        assert amended is not None
        assert len(amended.key_facts) == 2
        assert len(amended.revision_history) == 1

    def test_amend_nonexistent_returns_none(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import amend_forecast_entry

        result = amend_forecast_entry(
            "nonexistent-00000000",
            updates={"probability": 0.9},
            reason="test",
        )
        assert result is None

    def test_multiple_amends_accumulate_revisions(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import amend_forecast_entry, save_forecast_entry

        entry = make_forecast(probability=0.5)
        save_forecast_entry(entry)

        amend_forecast_entry(entry.slug, {"probability": 0.6}, "first update")
        amended = amend_forecast_entry(
            entry.slug, {"probability": 0.7}, "second update"
        )

        assert amended is not None
        assert amended.probability == 0.7
        assert len(amended.revision_history) == 2
        assert amended.revision_history[0].reason == "first update"
        assert amended.revision_history[1].reason == "second update"


class TestStalenessComputation:
    def test_fresh_entry_stays_fresh(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import iter_forecast_entries, save_forecast_entry

        entry = make_forecast(
            stale_after=datetime.now(timezone.utc) + timedelta(hours=24)
        )
        save_forecast_entry(entry)

        entries = list(iter_forecast_entries())
        assert len(entries) == 1
        assert entries[0].state == EntryState.fresh

    def test_past_stale_after_becomes_stale(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import iter_forecast_entries, save_forecast_entry

        entry = make_forecast(
            stale_after=datetime.now(timezone.utc) - timedelta(hours=1)
        )
        save_forecast_entry(entry)

        entries = list(iter_forecast_entries())
        assert len(entries) == 1
        assert entries[0].state == EntryState.stale

    def test_research_staleness(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import iter_research_entries, save_research_entry

        entry = make_research(
            stale_after=datetime.now(timezone.utc) - timedelta(hours=1)
        )
        save_research_entry(entry)

        entries = list(iter_research_entries())
        assert len(entries) == 1
        assert entries[0].state == EntryState.stale


class TestStateTransitions:
    def test_supersede_entry(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import (
            load_forecast_entry,
            save_forecast_entry,
            supersede_entry,
        )

        old = make_forecast(slug="old-entry-11112222")
        new = make_forecast(slug="new-entry-33334444")
        save_forecast_entry(old)
        save_forecast_entry(new)

        result = supersede_entry(
            "old-entry-11112222", "forecasts", "new-entry-33334444"
        )
        assert result is True

        loaded = load_forecast_entry("old-entry-11112222")
        assert loaded is not None
        assert loaded.state == EntryState.superseded
        assert loaded.superseded_by == "new-entry-33334444"

    def test_archive_entry(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import archive_entry, save_forecast_entry

        entry = make_forecast(slug="to-archive-55556666")
        save_forecast_entry(entry)

        result = archive_entry("to-archive-55556666", "forecasts")
        assert result is True

        # Original file should be gone
        assert not (worldview_dir / "forecasts" / "to-archive-55556666.json").exists()
        # Should be in archive
        assert (worldview_dir / "archive" / "to-archive-55556666.json").exists()

    def test_resolve_forecast_entry(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import (
            load_forecast_entry,
            resolve_forecast_entry,
            save_forecast_entry,
        )

        entry = make_forecast(slug="to-resolve-77778888")
        save_forecast_entry(entry)

        resolved = resolve_forecast_entry(
            "to-resolve-77778888",
            resolution=1.0,
            resolution_source="test",
            score=0.16,
        )

        assert resolved is not None
        assert resolved.resolved is True
        assert resolved.resolution == 1.0
        assert resolved.score == 0.16
        assert resolved.state == EntryState.resolved

        loaded = load_forecast_entry("to-resolve-77778888")
        assert loaded is not None
        assert loaded.resolved is True


class TestAllSlugs:
    def test_collects_from_both_kinds(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import (
            all_slugs,
            save_forecast_entry,
            save_research_entry,
        )

        save_forecast_entry(make_forecast(slug="forecast-slug-aaaa1111"))
        save_research_entry(make_research(slug="research-slug-bbbb2222"))

        slugs = all_slugs()
        assert "forecast-slug-aaaa1111" in slugs
        assert "research-slug-bbbb2222" in slugs


def make_output(**overrides: object) -> ForecastOutput:
    defaults: dict[str, object] = {
        "question_id": 12345,
        "post_id": 41976,
        "question_title": "Will X exceed 2000 by July?",
        "question_type": "binary",
        "summary": "Likely.",
        "reasoning": "Because reasons.",
        "probability": 0.62,
    }
    defaults.update(overrides)
    return ForecastOutput.model_validate(defaults)


class TestRegisterMainForecast:
    def test_registers_depth_zero_entry(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import (
            load_forecast_entry,
            main_forecast_slug,
            register_main_forecast,
        )

        context: dict[str, object] = {
            "scheduled_close_time": "2026-07-01T16:00:00+00:00",
            "scheduled_resolve_time": "2026-07-02T00:00:00+00:00",
        }
        entry = register_main_forecast(make_output(), context, 41976)

        assert entry is not None
        assert entry.slug == main_forecast_slug("Will X exceed 2000 by July?", 41976)
        assert entry.depth == 0
        assert entry.parent_post_id == 41976
        assert "main-forecast" in entry.tags
        assert entry.probability == 0.62
        assert entry.resolvable_after is not None
        assert load_forecast_entry(entry.slug) is not None

    def test_numeric_bounds_attached(self, worldview_dir: Path) -> None:
        from aib.worldview.lookup import register_main_forecast

        output = make_output(question_type="numeric", probability=None, median=1500.0)
        context: dict[str, object] = {
            "numeric_bounds": {"range_min": 0, "range_max": 10000}
        }
        entry = register_main_forecast(output, context, 99)

        assert entry is not None
        assert entry.numeric_bounds is not None
        assert entry.numeric_bounds.range_max == 10000

    def test_reforecast_preserves_created_at_and_archives(
        self, worldview_dir: Path
    ) -> None:
        from aib.worldview.lookup import register_main_forecast

        first = register_main_forecast(make_output(), {}, 41976)
        assert first is not None

        second = register_main_forecast(make_output(probability=0.7), {}, 41976)
        assert second is not None
        assert second.created_at == first.created_at
        assert second.probability == 0.7

        archives = list((worldview_dir / "forecasts").glob(f"{first.slug}_*.json"))
        assert len(archives) == 1

    def test_retrodict_skips_registration(self, worldview_dir: Path) -> None:
        from aib.retrodict_context import retrodict_cutoff
        from aib.worldview.lookup import register_main_forecast

        token = retrodict_cutoff.set(datetime.now(timezone.utc))
        try:
            result = register_main_forecast(make_output(), {}, 41976)
        finally:
            retrodict_cutoff.reset(token)
        assert result is None


class TestForecastSlugAndTimestamp:
    def test_main_forecast_slug_stable_and_keyed_by_post(self) -> None:
        from aib.worldview.lookup import main_forecast_slug

        a = main_forecast_slug("Will X exceed 2000?", 41976)
        b = main_forecast_slug("Will X exceed 2000?", 41976)
        c = main_forecast_slug("Will X exceed 2000?", 99999)
        assert a == b
        assert a.endswith("-41976")
        assert a != c

    def test_parse_api_timestamp(self) -> None:
        from aib.worldview.lookup import parse_api_timestamp

        assert parse_api_timestamp("2026-07-01T16:00:00+00:00") is not None
        assert parse_api_timestamp(None) is None
        assert parse_api_timestamp(12345) is None
        assert parse_api_timestamp("not a date") is None
