"""Forecast data paths — the layout that is this project's rather than lup's.

The session kernel lives in :mod:`lup.workspace.paths`: the project root, the
notes and traces directories, the feedback directory, the timestamp format,
and the versioned ``sessions/`` and ``logs/`` directories. Both layouts are
``notes/traces/<version>/…``, so this module reads the same tree lup writes.

What stays here is what forecasting adds on top: the forecast and retrodict
directories, the worldview store, the A/B trace variant, semver version-scope
resolution, and the cross-version iteration those readers need.

Layout:
    notes/traces/<version>/forecasts/<post_id>/<timestamp>.json
    notes/traces/<version>/retrodict/<post_id>/<retrodict_date>_<timestamp>.json
    notes/traces/<version>/sessions/<post_id>/<timestamp>/meta.md
    notes/traces/<version>/logs/<post_id>_<timestamp>.md
"""

import json
import logging
import re
import tempfile
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path

from lup.workspace.paths import (
    agent_version,
    notes_path,
    parse_timestamp,
    traces_path,
)
from lup.workspace.paths import sessions_dir as lup_sessions_dir
from lup.workspace.paths import trace_logs_dir as lup_trace_logs_dir

logger = logging.getLogger(__name__)

# ── Agent SDK spawn cwd: real isolation outside the user's worktree ──
# Lives under the system temp dir, not the notes directory, so the SDK
# subprocess working directory (and anything written relative to it) never
# lands in or gets committed to the git tree.
AGENT_CWD = Path(tempfile.gettempdir()) / "aib-agent-cwd"

# ── Worldview store paths (version-independent) ───────────────────
WORLDVIEW_PATH = notes_path() / "worldview"
WORLDVIEW_RESEARCH_PATH = WORLDVIEW_PATH / "research"
WORLDVIEW_FORECASTS_PATH = WORLDVIEW_PATH / "forecasts"
WORLDVIEW_ARCHIVE_PATH = WORLDVIEW_PATH / "archive"
WORLDVIEW_TRACES_PATH = WORLDVIEW_PATH / "traces"

REGRESSION_SUITE_PATH = notes_path() / "regression_suite.json"


# ── Write paths (version-specific) ─────────────────────────────────


def trace_version() -> str:
    """The version directory this process writes to.

    An A/B run appends its variant label as semver build metadata, so a
    variant's output lands beside the baseline instead of overwriting it.
    `parse_semver` rejects the result, which keeps experimental runs out of
    the released version's calibration aggregates until they are named.
    """
    from aib.config import settings

    if settings.trace_variant is None:
        return agent_version()
    return f"{agent_version()}+{settings.trace_variant}"


def forecasts_dir(version: str | None = None) -> Path:
    """Directory for forecast JSONs: notes/traces/<version>/forecasts/"""
    return traces_path() / (version or trace_version()) / "forecasts"


def retrodict_dir(version: str | None = None) -> Path:
    """Directory for retrodict JSONs: notes/traces/<version>/retrodict/"""
    return traces_path() / (version or trace_version()) / "retrodict"


def sessions_dir(version: str | None = None) -> Path:
    """Directory for session notes: notes/traces/<version>/sessions/

    lup owns the layout; what this adds is the default. lup defaults to the
    released ``agent_version()``, and an A/B arm has to write under its own
    variant directory or overwrite the baseline it is being compared against.
    """
    return lup_sessions_dir(version or trace_version())


def trace_logs_dir(version: str | None = None) -> Path:
    """Directory for reasoning logs: notes/traces/<version>/logs/

    Variant-defaulted for the same reason as :func:`sessions_dir`.
    """
    return lup_trace_logs_dir(version or trace_version())


# ── Read paths (cross-version iteration) ────────────────────────────


def _version_dirs() -> list[Path]:
    """Return all version directories under notes/traces/, sorted."""
    traces = traces_path()
    if not traces.exists():
        return []
    return sorted(
        d for d in traces.iterdir() if d.is_dir() and not d.name.startswith(".")
    )


def iter_forecast_dirs(
    post_id: int | None = None,
    version: str | None = None,
) -> Iterator[Path]:
    """Iterate over forecast post directories across all (or filtered) versions.

    Yields paths like: notes/traces/1.2.1/forecasts/42163/
    """
    if version:
        ver_dirs = [traces_path() / version]
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
        ver_dirs = [traces_path() / version]
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

MIN_CHART_VERSION = "7.0.0"
"""Floor for the views that pool several versions into one picture.

Below it the scores answer a different question: v7.0.0 put the agent on a
new framework and a new SDK, so a point from before it measures an agent
that no longer exists, and a chart carrying both reads as a trend where
there is only a change of subject.
"""

SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")

TRACE_VERSION_RE = re.compile(r"^(?P<release>\d+\.\d+\.\d+)(?:\+(?P<variant>[^+]+))?$")


def parse_semver(version: str) -> tuple[int, int, int] | None:
    """Parse 'X.Y.Z' into (major, minor, patch), or None if invalid."""
    m = SEMVER_RE.match(version)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def parse_trace_version(label: str) -> tuple[int, int, int] | None:
    """The release a trace directory names, ignoring any A/B variant suffix.

    An experiment arm writes under ``<version>+<name>``, and it is the
    release that decides whether the arm belongs in a version scope.
    """
    m = TRACE_VERSION_RE.match(label)
    if m is None:
        return None
    return parse_semver(m.group("release"))


def versions_at_least(min_version: str) -> list[str]:
    """Trace directory names at or above *min_version*, variant arms included."""
    floor = parse_semver(min_version)
    if floor is None:
        raise ValueError(f"minimum version {min_version!r} is not an X.Y.Z version")
    return [
        d.name
        for d in _version_dirs()
        if (release := parse_trace_version(d.name)) is not None and release >= floor
    ]


def _count_forecasts_for_versions(versions: list[str]) -> int:
    """Count total forecast files across a set of version directories."""
    return sum(sum(1 for _ in iter_forecast_files(version=v)) for v in versions)


def match_versions(prefix: str) -> list[str]:
    """Return version directory names matching a prefix (e.g. '4.0' matches '4.0.0', '4.0.1')."""
    available = [d.name for d in _version_dirs()]
    return [v for v in available if v == prefix or v.startswith(prefix + ".")]


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

    effective = version if version is not None else agent_version()
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


# ── Worldview store iteration ──────────────────────────────────────


def iter_worldview_entries(
    kind: str | None = None,
) -> Iterator[Path]:
    """Iterate worldview JSON files.

    kind: "research", "forecasts", or None for both.
    """
    dirs: list[Path] = []
    if kind is None:
        dirs = [WORLDVIEW_RESEARCH_PATH, WORLDVIEW_FORECASTS_PATH]
    elif kind == "research":
        dirs = [WORLDVIEW_RESEARCH_PATH]
    elif kind == "forecasts":
        dirs = [WORLDVIEW_FORECASTS_PATH]

    for d in dirs:
        if d.exists():
            yield from sorted(d.glob("*.json"))


def iter_worldview_archive() -> Iterator[Path]:
    """Iterate archived worldview entries."""
    if WORLDVIEW_ARCHIVE_PATH.exists():
        yield from sorted(WORLDVIEW_ARCHIVE_PATH.glob("*.json"))


def worldview_entry_path(slug: str, kind: str) -> Path:
    """Return the path for a worldview entry by slug and kind."""
    base = WORLDVIEW_RESEARCH_PATH if kind == "research" else WORLDVIEW_FORECASTS_PATH
    return base / f"{slug}.json"
