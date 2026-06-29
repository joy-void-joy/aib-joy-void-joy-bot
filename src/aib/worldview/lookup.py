"""CRUD operations for the worldview store.

Provides save, load, amend, state transitions, and iteration for
worldview research and forecast entries.
"""

import json
import logging
import os
from collections.abc import Iterator
from datetime import datetime, timezone
from pathlib import Path

import sh
from pydantic import ValidationError

from aib.paths import (
    WORLDVIEW_ARCHIVE_PATH,
    WORLDVIEW_FORECASTS_PATH,
    WORLDVIEW_PATH,
    WORLDVIEW_RESEARCH_PATH,
    iter_worldview_entries,
    worldview_entry_path,
)
from aib.retrodict_context import retrodict_cutoff
from aib.worldview.models import (
    EntryState,
    Revision,
    WorldviewForecastEntry,
    WorldviewResearchEntry,
)

logger = logging.getLogger(__name__)


# ── Save ───────────────────────────────────────────────────────────


def archive_research_snapshot(slug: str) -> None:
    """Copy the current research entry into the archive as a trajectory snapshot."""
    path = worldview_entry_path(slug, "research")
    if not path.exists():
        return
    old_data = json.loads(path.read_text(encoding="utf-8"))
    ts_raw = old_data.get("updated_at")
    old_ts = (
        datetime.fromisoformat(ts_raw)
        if isinstance(ts_raw, str)
        else datetime.now(timezone.utc)
    )
    WORLDVIEW_ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)
    snapshot = (
        WORLDVIEW_ARCHIVE_PATH / f"{slug}_{old_ts.strftime('%Y%m%d_%H%M%S_%f')}.json"
    )
    snapshot.write_text(json.dumps(old_data, indent=2, default=str), encoding="utf-8")
    logger.info("Archived prior research snapshot to %s", snapshot)


def save_research_entry(entry: WorldviewResearchEntry) -> Path:
    """Write a research entry, archiving any prior version for trajectory history."""
    if retrodict_cutoff.get() is not None:
        return worldview_entry_path(entry.slug, "research")
    WORLDVIEW_RESEARCH_PATH.mkdir(parents=True, exist_ok=True)
    archive_research_snapshot(entry.slug)
    path = worldview_entry_path(entry.slug, "research")
    path.write_text(entry.model_dump_json(indent=2), encoding="utf-8")
    logger.info("Saved research entry %s to %s", entry.slug, path)
    return path


def save_forecast_entry(entry: WorldviewForecastEntry) -> Path:
    """Write a forecast entry, archiving any prior version for calibration history."""
    if retrodict_cutoff.get() is not None:
        return worldview_entry_path(entry.slug, "forecasts")
    WORLDVIEW_FORECASTS_PATH.mkdir(parents=True, exist_ok=True)
    path = worldview_entry_path(entry.slug, "forecasts")

    if path.exists():
        old_data = json.loads(path.read_text(encoding="utf-8"))
        ts_raw = old_data.get("updated_at")
        if isinstance(ts_raw, str):
            old_ts = datetime.fromisoformat(ts_raw)
        else:
            logger.warning(
                "Missing updated_at in %s, using current time for archive", entry.slug
            )
            old_ts = datetime.now(timezone.utc)
        ts_str = old_ts.strftime("%Y%m%d_%H%M%S_%f")
        archive = WORLDVIEW_FORECASTS_PATH / f"{entry.slug}_{ts_str}.json"
        archive.write_text(
            json.dumps(old_data, indent=2, default=str), encoding="utf-8"
        )
        logger.info("Archived prior forecast entry to %s", archive)

    path.write_text(entry.model_dump_json(indent=2), encoding="utf-8")
    logger.info("Saved forecast entry %s to %s", entry.slug, path)
    return path


# ── Load ───────────────────────────────────────────────────────────


def load_research_entry(slug: str) -> WorldviewResearchEntry | None:
    """Load a research entry by slug. Returns None if not found."""
    if retrodict_cutoff.get() is not None:
        return None
    path = worldview_entry_path(slug, "research")
    if not path.exists():
        return None
    return WorldviewResearchEntry.model_validate_json(path.read_text(encoding="utf-8"))


def load_forecast_entry(slug: str) -> WorldviewForecastEntry | None:
    """Load a forecast entry by slug. Returns None if not found."""
    if retrodict_cutoff.get() is not None:
        return None
    path = worldview_entry_path(slug, "forecasts")
    if not path.exists():
        return None
    return WorldviewForecastEntry.model_validate_json(path.read_text(encoding="utf-8"))


# ── Iteration ──────────────────────────────────────────────────────


def iter_research_entries() -> Iterator[WorldviewResearchEntry]:
    """Iterate all research entries, with computed staleness."""
    if retrodict_cutoff.get() is not None:
        return
    now = datetime.now(timezone.utc)
    for path in iter_worldview_entries("research"):
        try:
            entry = WorldviewResearchEntry.model_validate_json(
                path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, ValidationError, OSError):
            logger.debug("Skipping invalid research entry: %s", path)
            continue
        if entry.state == EntryState.fresh and entry.stale_after < now:
            entry = entry.model_copy(update={"state": EntryState.stale})
        yield entry


def iter_forecast_entries() -> Iterator[WorldviewForecastEntry]:
    """Iterate all forecast entries, with computed staleness."""
    if retrodict_cutoff.get() is not None:
        return
    now = datetime.now(timezone.utc)
    for path in iter_worldview_entries("forecasts"):
        try:
            entry = WorldviewForecastEntry.model_validate_json(
                path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, ValidationError, OSError):
            logger.debug("Skipping invalid forecast entry: %s", path)
            continue
        if entry.state == EntryState.fresh and entry.stale_after < now:
            entry = entry.model_copy(update={"state": EntryState.stale})
        yield entry


def all_slugs() -> set[str]:
    """Return the set of all existing slugs across research and forecasts."""
    if retrodict_cutoff.get() is not None:
        return set()
    slugs: set[str] = set()
    for path in iter_worldview_entries():
        slugs.add(path.stem)
    return slugs


# ── Amend ──────────────────────────────────────────────────────────


def amend_research_entry(
    slug: str,
    updates: dict[str, object],
    reason: str,
) -> WorldviewResearchEntry | None:
    """Patch fields on a research entry with revision tracking."""
    entry = load_research_entry(slug)
    if entry is None:
        logger.warning("Research entry %s not found for amend", slug)
        return None

    now = datetime.now(timezone.utc)
    revision = Revision(
        timestamp=now,
        fields_changed=list(updates.keys()),
        reason=reason,
    )
    updates["updated_at"] = now
    updates["revision_history"] = [*entry.revision_history, revision]

    amended = entry.model_copy(update=updates)
    save_research_entry(amended)
    logger.info("Amended research entry %s: %s", slug, list(updates.keys()))
    return amended


def amend_forecast_entry(
    slug: str,
    updates: dict[str, object],
    reason: str,
) -> WorldviewForecastEntry | None:
    """Patch fields on a forecast entry with revision tracking."""
    entry = load_forecast_entry(slug)
    if entry is None:
        logger.warning("Forecast entry %s not found for amend", slug)
        return None

    now = datetime.now(timezone.utc)
    revision = Revision(
        timestamp=now,
        fields_changed=list(updates.keys()),
        reason=reason,
    )
    updates["updated_at"] = now
    updates["revision_history"] = [*entry.revision_history, revision]

    amended = entry.model_copy(update=updates)
    save_forecast_entry(amended)
    logger.info("Amended forecast entry %s: %s", slug, list(updates.keys()))
    return amended


# ── State transitions ──────────────────────────────────────────────


def supersede_entry(
    slug: str,
    kind: str,
    superseded_by: str,
) -> bool:
    """Mark an entry as superseded by another slug. Returns True if updated."""
    if retrodict_cutoff.get() is not None:
        return False
    path = worldview_entry_path(slug, kind)
    if not path.exists():
        return False

    data = json.loads(path.read_text(encoding="utf-8"))
    data["state"] = EntryState.superseded
    data["superseded_by"] = superseded_by
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    logger.info("Superseded %s entry %s by %s", kind, slug, superseded_by)
    return True


def resolve_forecast_entry(
    slug: str,
    resolution: float | str,
    resolution_source: str,
    score: float | None = None,
) -> WorldviewForecastEntry | None:
    """Mark a forecast entry as resolved and optionally score it."""
    entry = load_forecast_entry(slug)
    if entry is None:
        return None

    now = datetime.now(timezone.utc)
    resolved = entry.model_copy(
        update={
            "state": EntryState.resolved,
            "resolved": True,
            "resolution": resolution,
            "resolved_at": now,
            "resolution_source": resolution_source,
            "score": score,
            "updated_at": now,
        }
    )
    save_forecast_entry(resolved)
    logger.info("Resolved forecast entry %s: %s", slug, resolution)
    return resolved


def archive_entry(slug: str, kind: str) -> bool:
    """Move a resolved entry to the archive directory. Returns True if moved."""
    if retrodict_cutoff.get() is not None:
        return False
    source = worldview_entry_path(slug, kind)
    if not source.exists():
        return False

    WORLDVIEW_ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)
    dest = WORLDVIEW_ARCHIVE_PATH / source.name
    source.rename(dest)
    logger.info("Archived %s entry %s to %s", kind, slug, dest)
    return True


# ── Git integration ────────────────────────────────────────────────


def commit_worldview(message: str) -> bool:
    """Stage and commit all worldview changes."""
    if retrodict_cutoff.get() is not None:
        return False
    if not WORLDVIEW_PATH.exists():
        return False

    try:
        env = {**os.environ, "GIT_PAGER": ""}
        git = sh.Command("git")
        git.add(str(WORLDVIEW_PATH), _tty_out=False, _env=env)

        diff = str(
            git.diff("--cached", "--name-only", _tty_out=False, _env=env)
        ).strip()
        if not diff:
            return False

        try:
            git.commit("-m", message, _tty_out=False, _env=env)
        except sh.ErrorReturnCode:
            git.reset("HEAD", _tty_out=False, _env=env)
            raise
        logger.info("Committed worldview changes: %s", message)
        return True
    except sh.ErrorReturnCode as e:
        logger.warning("Worldview commit failed: %s", e)
        return False
