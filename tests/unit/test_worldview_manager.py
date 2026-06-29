"""Tests for worldview manager MCP tool wrappers.

The maintenance sub-agent itself is not unit-tested (it requires an LLM
client); these tests exercise the MCP tools it calls.
"""

from collections.abc import Iterator
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


# ── trajectory preservation ──────────────────────────────────────


def test_save_research_archives_prior_snapshot(worldview_dir: Path) -> None:
    save_research_entry(
        make_research("traj").model_copy(update={"answer": "first-value"})
    )
    save_research_entry(
        make_research("traj").model_copy(update={"answer": "second-value"})
    )

    live = (worldview_dir / "research" / "traj.json").read_text(encoding="utf-8")
    assert "second-value" in live

    snapshots = list((worldview_dir / "archive").glob("traj_*.json"))
    assert len(snapshots) == 1
    assert "first-value" in snapshots[0].read_text(encoding="utf-8")


def test_save_research_new_slug_keeps_no_snapshot(worldview_dir: Path) -> None:
    save_research_entry(make_research("brand-new"))
    assert not list((worldview_dir / "archive").glob("brand-new_*.json"))


# ── add_issue + survey collector ─────────────────────────────────


@pytest.mark.asyncio
async def test_add_issue_registers_to_collector(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import Issue, add_issue, survey_issues

    collected: list[Issue] = []
    token = survey_issues.set(collected)
    try:
        result = await add_issue.handler(
            {
                "kind": "contradiction",
                "description": "A and B disagree on X",
                "slugs": ["a", "b"],
                "claim": "What is X now?",
            }
        )
        assert result.get("is_error") is not True
    finally:
        survey_issues.reset(token)

    assert len(collected) == 1
    assert collected[0].kind == "contradiction"
    assert collected[0].slugs == ["a", "b"]


@pytest.mark.asyncio
async def test_add_issue_outside_survey_errors(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import add_issue

    result = await add_issue.handler(
        {"kind": "outdated", "description": "stale", "slugs": ["c"]}
    )
    assert result.get("is_error") is True


# ── wv_refresh ───────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_wv_refresh_replaces_entry(
    worldview_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import aib.tools.research as research_mod
    from aib.tools.research import ResearchResult
    from aib.tools.worldview_manager import wv_refresh

    save_research_entry(make_research("to-refresh", query="current X?"))
    refreshed = make_research("to-refresh", query="current X?").model_copy(
        update={"answer": "fresh data"}
    )

    async def fake_refresh(entry: WorldviewResearchEntry) -> ResearchResult:
        return ResearchResult(query=entry.query, entry=refreshed)

    monkeypatch.setattr(research_mod, "refresh_research_entry", fake_refresh)

    result = await wv_refresh.handler({"slug": "to-refresh"})
    assert result.get("is_error") is not True
    assert "to-refresh" in result["content"][0]["text"]


@pytest.mark.asyncio
async def test_wv_refresh_missing_entry_errors(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_refresh

    result = await wv_refresh.handler({"slug": "nope"})
    assert result.get("is_error") is True


# ── run_worldview_refresh (survey → fan out) ─────────────────────


@pytest.mark.asyncio
async def test_run_worldview_refresh_dry_run_skips_fixes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from contextlib import contextmanager

    import aib.tools.worldview_manager as wv_mod
    from aib.tools.worldview_manager import Issue, run_worldview_refresh

    issues = [Issue(kind="outdated", description="stale", slugs=["x"])]
    fix_calls: list[Issue] = []

    async def fake_survey() -> list[Issue]:
        return issues

    async def fake_fix(issue: Issue) -> str:
        fix_calls.append(issue)
        return "fixed"

    @contextmanager
    def fake_session() -> Iterator[None]:
        yield

    monkeypatch.setattr(wv_mod, "run_survey", fake_survey)
    monkeypatch.setattr(wv_mod, "fix_issue", fake_fix)
    monkeypatch.setattr(wv_mod, "worldview_research_session", fake_session)

    report = await run_worldview_refresh(dry_run=True)

    assert report.dry_run is True
    assert len(report.issues_found) == 1
    assert fix_calls == []


@pytest.mark.asyncio
async def test_run_worldview_refresh_fans_out_a_fix_per_issue(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from contextlib import contextmanager

    import aib.tools.worldview_manager as wv_mod
    from aib.tools.worldview_manager import Issue, run_worldview_refresh

    issues = [
        Issue(kind="outdated", description="a", slugs=["x"]),
        Issue(kind="duplicate", description="b", slugs=["y", "z"]),
    ]
    fixed: list[str] = []

    async def fake_survey() -> list[Issue]:
        return issues

    async def fake_fix(issue: Issue) -> str:
        fixed.append(issue.kind)
        return f"fixed {issue.kind}"

    @contextmanager
    def fake_session() -> Iterator[None]:
        yield

    monkeypatch.setattr(wv_mod, "run_survey", fake_survey)
    monkeypatch.setattr(wv_mod, "fix_issue", fake_fix)
    monkeypatch.setattr(wv_mod, "worldview_research_session", fake_session)
    monkeypatch.setattr(wv_mod, "commit_worldview", lambda msg: False)

    report = await run_worldview_refresh()

    assert set(fixed) == {"outdated", "duplicate"}
    assert len(report.fixes) == 2


# ── wv_reconcile ─────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_reconcile_supersedes_conflicting_entries(
    worldview_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import aib.tools.research as research_mod
    from aib.tools.research import ResearchQuestion, ResearchResult
    from aib.tools.worldview_manager import wv_reconcile
    from aib.worldview.lookup import load_research_entry

    save_research_entry(make_research("claim-a", query="X is 100"))
    save_research_entry(make_research("claim-b", query="X is 200"))
    fresh = make_research("x-current-abc123", query="What is X now?")

    async def fake_research(
        question: ResearchQuestion, existing_slugs: set[str]
    ) -> ResearchResult:
        save_research_entry(fresh)
        return ResearchResult(query=fresh.query, entry=fresh)

    monkeypatch.setattr(research_mod, "run_single_research", fake_research)

    result = await wv_reconcile.handler(
        {
            "claim": "What is the current value of X?",
            "conflicting_slugs": ["claim-a", "claim-b"],
            "ttl": "1d",
        }
    )
    assert result.get("is_error") is not True

    for slug in ("claim-a", "claim-b"):
        reloaded = load_research_entry(slug)
        assert reloaded is not None
        assert reloaded.state == EntryState.superseded
        assert reloaded.superseded_by == "x-current-abc123"


@pytest.mark.asyncio
async def test_reconcile_missing_slug_errors(worldview_dir: Path) -> None:
    from aib.tools.worldview_manager import wv_reconcile

    result = await wv_reconcile.handler(
        {"claim": "Y?", "conflicting_slugs": ["does-not-exist"], "ttl": "1d"}
    )
    assert result.get("is_error") is True
