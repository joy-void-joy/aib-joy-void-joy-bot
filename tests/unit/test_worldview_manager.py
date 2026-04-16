"""Tests for worldview manager MCP tool wrappers.

The maintenance sub-agent itself is not unit-tested (it requires an LLM
client); these tests exercise the MCP tools it calls.
"""

from datetime import datetime, timezone
from pathlib import Path

import pytest

from aib.worldview.lookup import save_forecast_entry, save_research_entry
from aib.worldview.models import (
    EntryState,
    WorldviewForecastEntry,
    WorldviewResearchEntry,
)


@pytest.fixture
def worldview_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Create a temporary worldview directory and patch all path references."""
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
    slug: str,
    question: str = "Test question?",
    *,
    probability: float | None = 0.6,
    tags: list[str] | None = None,
) -> WorldviewForecastEntry:
    """Helper to create a forecast entry for tests."""
    now = datetime.now(timezone.utc)
    return WorldviewForecastEntry(
        slug=slug,
        question=question,
        question_type="binary",
        probability=probability,
        created_at=now,
        updated_at=now,
        stale_after=now,
        tags=tags or [],
    )


def make_research(slug: str, query: str = "Test query") -> WorldviewResearchEntry:
    """Helper to create a research entry for tests."""
    now = datetime.now(timezone.utc)
    return WorldviewResearchEntry(
        slug=slug,
        query=query,
        answer="answer",
        created_at=now,
        updated_at=now,
        stale_after=now,
    )


# ── wv_list_entries ──────────────────────────────────────────────


@pytest.mark.asyncio
async def test_list_entries_returns_all_kinds(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_list_entries

    save_research_entry(make_research("r-1"))
    save_forecast_entry(make_forecast("f-1"))

    result = await wv_list_entries.handler({"kind": "all"})
    content = result["content"][0]["text"]
    assert "r-1" in content
    assert "f-1" in content


@pytest.mark.asyncio
async def test_list_entries_filters_by_kind(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_list_entries

    save_research_entry(make_research("r-only"))
    save_forecast_entry(make_forecast("f-only"))

    research_only = await wv_list_entries.handler({"kind": "research"})
    text = research_only["content"][0]["text"]
    assert "r-only" in text
    assert "f-only" not in text


@pytest.mark.asyncio
async def test_list_entries_excludes_superseded_by_default(
    worldview_dir: Path,
) -> None:
    from aib.tools.worldview_manager import wv_list_entries

    kept = make_forecast("kept")
    old = make_forecast("old")
    old = old.model_copy(update={"state": EntryState.superseded})
    save_forecast_entry(kept)
    save_forecast_entry(old)

    result = await wv_list_entries.handler({"kind": "forecast"})
    text = result["content"][0]["text"]
    assert "kept" in text
    assert "old" not in text


# ── wv_read_entry ────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_read_entry_returns_full_entry(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_read_entry

    save_forecast_entry(make_forecast("full-entry", question="Detailed?"))

    result = await wv_read_entry.handler({"slug": "full-entry", "kind": "forecasts"})
    text = result["content"][0]["text"]
    assert "Detailed?" in text


@pytest.mark.asyncio
async def test_read_entry_missing_returns_error(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_read_entry

    result = await wv_read_entry.handler({"slug": "nope", "kind": "forecasts"})
    assert result.get("is_error") is True


# ── wv_archive_entry ─────────────────────────────────────────────


@pytest.mark.asyncio
async def test_archive_entry_moves_to_archive(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_archive_entry

    save_forecast_entry(make_forecast("to-archive"))
    assert (worldview_dir / "forecasts" / "to-archive.json").exists()

    result = await wv_archive_entry.handler(
        {"slug": "to-archive", "kind": "forecasts", "reason": "test"}
    )
    assert result.get("is_error") is not True
    assert not (worldview_dir / "forecasts" / "to-archive.json").exists()
    assert (worldview_dir / "archive" / "to-archive.json").exists()


# ── wv_supersede_entry ───────────────────────────────────────────


@pytest.mark.asyncio
async def test_supersede_marks_older_as_superseded(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_supersede_entry
    from aib.worldview.lookup import load_forecast_entry

    save_forecast_entry(make_forecast("older"))
    save_forecast_entry(make_forecast("newer"))

    result = await wv_supersede_entry.handler(
        {
            "older_slug": "older",
            "newer_slug": "newer",
            "kind": "forecasts",
            "reason": "duplicate",
        }
    )
    assert result.get("is_error") is not True

    reloaded = load_forecast_entry("older")
    assert reloaded is not None
    assert reloaded.state == EntryState.superseded
    assert reloaded.superseded_by == "newer"


@pytest.mark.asyncio
async def test_supersede_rejects_self_reference(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_supersede_entry

    save_forecast_entry(make_forecast("self"))

    result = await wv_supersede_entry.handler(
        {
            "older_slug": "self",
            "newer_slug": "self",
            "kind": "forecasts",
            "reason": "invalid",
        }
    )
    assert result.get("is_error") is True


# ── wv_tag_forecast ──────────────────────────────────────────────


@pytest.mark.asyncio
async def test_tag_forecast_merges_tags(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_tag_forecast
    from aib.worldview.lookup import load_forecast_entry

    save_forecast_entry(make_forecast("tagged", tags=["existing"]))

    result = await wv_tag_forecast.handler(
        {"slug": "tagged", "tags": ["research:r-1", "research:r-2"]}
    )
    assert result.get("is_error") is not True

    reloaded = load_forecast_entry("tagged")
    assert reloaded is not None
    assert set(reloaded.tags) == {"existing", "research:r-1", "research:r-2"}


# ── wv_resolve_forecast ──────────────────────────────────────────


@pytest.mark.asyncio
async def test_resolve_forecast_scores_binary(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_resolve_forecast
    from aib.worldview.lookup import load_forecast_entry

    save_forecast_entry(make_forecast("to-resolve", probability=0.7))

    result = await wv_resolve_forecast.handler(
        {"slug": "to-resolve", "resolution": 1.0, "source": "manual"}
    )
    assert result.get("is_error") is not True

    reloaded = load_forecast_entry("to-resolve")
    assert reloaded is not None
    assert reloaded.resolved is True
    assert reloaded.resolution == 1.0
    # Brier score: (0.7 - 1.0)^2 = 0.09
    assert reloaded.score == pytest.approx(0.09)
