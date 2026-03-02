"""Centralized path constants and helpers for forecast data.

All forecast-related paths are routed through this module. Writers use
version-specific directories; readers default to the current AGENT_VERSION
with progressive semver fallback when data is insufficient.

Layout:
    notes/traces/<version>/forecasts/<post_id>/<timestamp>.json
    notes/traces/<version>/retrodict/<post_id>/<retrodict_date>_<timestamp>.json
    notes/traces/<version>/sessions/<post_id>/<timestamp>/meta.md
    notes/traces/<version>/logs/<post_id>_<timestamp>.md
"""

import json
import logging
import re
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path

from aib.version import AGENT_VERSION

logger = logging.getLogger(__name__)


def _find_project_root() -> Path:
    """Find project root by walking up to pyproject.toml."""
    current = Path(__file__).resolve().parent
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    raise RuntimeError("Could not find project root (no pyproject.toml found)")


# ── Root paths ──────────────────────────────────────────────────────
_PROJECT_ROOT = _find_project_root()
NOTES_PATH = _PROJECT_ROOT / "notes"
RUNTIME_LOGS_PATH = _PROJECT_ROOT / "logs"

# ── Versioned trace paths ───────────────────────────────────────────
TRACES_PATH = NOTES_PATH / "traces"

FEEDBACK_PATH = NOTES_PATH / "feedback_loop"

_TIMESTAMP_FMT = "%Y%m%d_%H%M%S"
_TIMESTAMP_RE = re.compile(r"\d{8}_\d{6}")


def parse_timestamp(name: str) -> datetime:
    """Parse the last YYYYMMDD_HHMMSS occurrence from a filename or string.

    Handles both forecast filenames (YYYYMMDD_HHMMSS.json) and retrodict
    filenames (YYYY-MM-DD_YYYYMMDD_HHMMSS.json) by extracting the last
    matching pattern.
    """
    matches = _TIMESTAMP_RE.findall(Path(name).stem)
    if not matches:
        raise ValueError(f"No YYYYMMDD_HHMMSS timestamp found in: {name}")
    return datetime.strptime(matches[-1], _TIMESTAMP_FMT)


REGRESSION_SUITE_PATH = NOTES_PATH / "regression_suite.json"


# ── Write paths (version-specific) ─────────────────────────────────


def forecasts_dir(version: str = AGENT_VERSION) -> Path:
    """Directory for forecast JSONs: notes/traces/<version>/forecasts/"""
    return TRACES_PATH / version / "forecasts"


def retrodict_dir(version: str = AGENT_VERSION) -> Path:
    """Directory for retrodict JSONs: notes/traces/<version>/retrodict/"""
    return TRACES_PATH / version / "retrodict"


def sessions_dir(version: str = AGENT_VERSION) -> Path:
    """Directory for session notes: notes/traces/<version>/sessions/"""
    return TRACES_PATH / version / "sessions"


def trace_logs_dir(version: str = AGENT_VERSION) -> Path:
    """Directory for reasoning logs: notes/traces/<version>/logs/"""
    return TRACES_PATH / version / "logs"


# ── Read paths (cross-version iteration) ────────────────────────────


def _version_dirs() -> list[Path]:
    """Return all version directories under notes/traces/, sorted."""
    if not TRACES_PATH.exists():
        return []
    return sorted(
        d for d in TRACES_PATH.iterdir() if d.is_dir() and not d.name.startswith(".")
    )


def iter_forecast_dirs(
    post_id: int | None = None,
    version: str | None = None,
) -> Iterator[Path]:
    """Iterate over forecast post directories across all (or filtered) versions.

    Yields paths like: notes/traces/1.2.1/forecasts/42163/
    """
    if version:
        ver_dirs = [TRACES_PATH / version]
    else:
        ver_dirs = _version_dirs()

    for ver_dir in ver_dirs:
        forecasts_base = ver_dir / "forecasts"
        if not forecasts_base.exists():
            continue
        if post_id is not None:
            candidate = forecasts_base / str(post_id)
            if candidate.exists() and candidate.is_dir():
                yield candidate
        else:
            for d in forecasts_base.iterdir():
                if d.is_dir():
                    yield d


def iter_forecast_files(
    post_id: int | None = None,
    version: str | None = None,
) -> Iterator[Path]:
    """Iterate over all forecast JSON files across versions."""
    for post_dir in iter_forecast_dirs(post_id, version):
        yield from post_dir.glob("*.json")


def iter_retrodict_dirs(
    post_id: int | None = None,
    version: str | None = None,
) -> Iterator[Path]:
    """Iterate over retrodict post directories across all (or filtered) versions.

    Yields paths like: notes/traces/1.2.1/retrodict/42163/
    """
    if version:
        ver_dirs = [TRACES_PATH / version]
    else:
        ver_dirs = _version_dirs()

    for ver_dir in ver_dirs:
        retrodict_base = ver_dir / "retrodict"
        if not retrodict_base.exists():
            continue
        if post_id is not None:
            candidate = retrodict_base / str(post_id)
            if candidate.exists() and candidate.is_dir():
                yield candidate
        else:
            for d in retrodict_base.iterdir():
                if d.is_dir():
                    yield d


def iter_retrodict_files(
    post_id: int | None = None,
    version: str | None = None,
) -> Iterator[Path]:
    """Iterate over all retrodict JSON files across versions."""
    for post_dir in iter_retrodict_dirs(post_id, version):
        yield from post_dir.glob("*.json")


def find_latest_forecast_file(post_id: int) -> Path | None:
    """Find the most recent forecast JSON for a post_id across all versions."""
    latest: Path | None = None
    latest_ts: datetime | None = None
    for f in iter_forecast_files(post_id):
        try:
            ts = parse_timestamp(f.name)
        except ValueError:
            continue
        if latest_ts is None or ts > latest_ts:
            latest = f
            latest_ts = ts
    return latest


def get_all_forecasted_post_ids(version: str | None = None) -> set[int]:
    """Return the set of post_ids that have forecast directories."""
    post_ids: set[int] = set()
    for d in iter_forecast_dirs(version=version):
        try:
            post_ids.add(int(d.name))
        except ValueError:
            continue
    return post_ids


def _load_jsons_from_files(files: Iterator[Path]) -> list[dict[str, object]]:
    """Load and validate forecast JSONs from an iterator of file paths."""
    results: list[dict[str, object]] = []
    for filepath in files:
        try:
            data = json.loads(filepath.read_text())
            if "question_type" in data and "timestamp" in data:
                results.append(data)
            else:
                logger.debug(
                    "Skipping %s: missing question_type or timestamp key", filepath
                )
        except json.JSONDecodeError:
            logger.debug("Skipping %s: invalid JSON", filepath)
        except OSError as e:
            logger.debug("Skipping %s: %s", filepath, e)
    return results


def load_all_forecast_jsons(
    version: str | None = None,
    versions: list[str] | None = None,
) -> list[dict[str, object]]:
    """Load forecast JSONs. versions overrides version if provided."""
    if versions is not None:
        results: list[dict[str, object]] = []
        for v in versions:
            results.extend(_load_jsons_from_files(iter_forecast_files(version=v)))
        return results
    return _load_jsons_from_files(iter_forecast_files(version=version))


def load_all_retrodict_jsons(
    version: str | None = None,
    versions: list[str] | None = None,
) -> list[dict[str, object]]:
    """Load retrodict JSONs. versions overrides version if provided."""
    if versions is not None:
        results: list[dict[str, object]] = []
        for v in versions:
            results.extend(_load_jsons_from_files(iter_retrodict_files(version=v)))
        return results
    return _load_jsons_from_files(iter_retrodict_files(version=version))


# ── Session/log cross-version helpers ───────────────────────────────


def iter_session_dirs(post_id: int | None = None) -> Iterator[Path]:
    """Iterate session directories: notes/traces/<version>/sessions/<post_id>/"""
    for ver_dir in _version_dirs():
        sessions_base = ver_dir / "sessions"
        if not sessions_base.exists():
            continue
        if post_id is not None:
            candidate = sessions_base / str(post_id)
            if candidate.exists():
                yield candidate
        else:
            for d in sessions_base.iterdir():
                if d.is_dir():
                    yield d


def iter_trace_log_files(post_id: int | None = None) -> Iterator[Path]:
    """Iterate reasoning log files: notes/traces/<version>/logs/<post_id>_*.md"""
    for ver_dir in _version_dirs():
        logs_base = ver_dir / "logs"
        if not logs_base.exists():
            continue
        if post_id is not None:
            yield from logs_base.glob(f"{post_id}_*.md")
        else:
            yield from logs_base.glob("*.md")


# ── Version scope resolution ────────────────────────────────────────

MIN_VERSION_DATAPOINTS = 10

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse_semver(version: str) -> tuple[int, int, int] | None:
    """Parse 'X.Y.Z' into (major, minor, patch), or None if invalid."""
    m = SEMVER_RE.match(version)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def _count_forecasts_for_versions(versions: list[str]) -> int:
    """Count total forecast files across a set of version directories."""
    return sum(sum(1 for _ in iter_forecast_files(version=v)) for v in versions)


def resolve_version(
    version: str | None,
    all_versions: bool = False,
    min_datapoints: int = MIN_VERSION_DATAPOINTS,
) -> tuple[list[str] | None, str | None]:
    """Resolve effective version scope with progressive semver fallback.

    Fallback chain: exact version → X.Y.* → X.* → all versions.

    Returns (version_list, warning_message).
    version_list is None when all versions should be included.
    """
    if all_versions:
        return None, None

    effective = version if version is not None else AGENT_VERSION
    semver = parse_semver(effective)
    available = [d.name for d in _version_dirs()]

    # Level 1: exact version
    exact = [effective] if effective in available else []
    exact_count = _count_forecasts_for_versions(exact)
    if exact_count >= min_datapoints:
        return exact, None

    if semver is None:
        return None, (
            f"v{effective} has only {exact_count} forecasts "
            f"(need {min_datapoints}) — including all versions"
        )

    major, minor, _patch = semver

    # Level 2: same minor (X.Y.*)
    minor_matches = [
        v
        for v in available
        if (sv := parse_semver(v)) is not None and sv[0] == major and sv[1] == minor
    ]
    minor_count = _count_forecasts_for_versions(minor_matches)
    if minor_count >= min_datapoints:
        return minor_matches, (
            f"v{effective} has only {exact_count} forecasts "
            f"— widening to v{major}.{minor}.* ({minor_count} forecasts)"
        )

    # Level 3: same major (X.*)
    major_matches = [
        v for v in available if (sv := parse_semver(v)) is not None and sv[0] == major
    ]
    major_count = _count_forecasts_for_versions(major_matches)
    if major_count >= min_datapoints:
        return major_matches, (
            f"v{major}.{minor}.* has only {minor_count} forecasts "
            f"— widening to v{major}.* ({major_count} forecasts)"
        )

    # Level 4: all versions
    return None, (
        f"v{major}.* has only {major_count} forecasts "
        f"(need {min_datapoints}) — including all versions"
    )
