"""One-time data migration commands for versioned trace storage."""

import json
import re
import shutil
from pathlib import Path

import typer

app = typer.Typer(no_args_is_help=True)

_OLD_FORECASTS = Path("./notes/forecasts")
_OLD_SESSIONS = Path("./notes/sessions")
_OLD_LOGS = Path("./notes/logs")
_OLD_RETRODICT = Path("./notes/retrodict")
_OLD_ARCHIVE = Path("./notes/archive")
_TRACES = Path("./notes/traces")
_DEFAULT_VERSION = "0.0.0"


def _read_version_from_json(filepath: Path) -> str:
    """Read agent_version from a forecast JSON, falling back to default."""
    try:
        data = json.loads(filepath.read_text())
        return data.get("agent_version") or _DEFAULT_VERSION
    except (json.JSONDecodeError, OSError):
        return _DEFAULT_VERSION


def _build_version_map() -> dict[tuple[str, str], str]:
    """Build (post_id, timestamp) -> version mapping from forecast JSONs."""
    version_map: dict[tuple[str, str], str] = {}
    if not _OLD_FORECASTS.exists():
        return version_map
    for post_dir in _OLD_FORECASTS.iterdir():
        if not post_dir.is_dir():
            continue
        for f in post_dir.glob("*.json"):
            ts = f.stem
            version = _read_version_from_json(f)
            version_map[(post_dir.name, ts)] = version
    return version_map


def _version_for_post(version_map: dict[tuple[str, str], str], post_id: str) -> str:
    """Get version for a post_id (any timestamp), falling back to default."""
    for (pid, _), ver in version_map.items():
        if pid == post_id:
            return ver
    return _DEFAULT_VERSION


@app.command("traces")
def migrate_traces(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be moved"
    ),
) -> None:
    """Migrate flat notes/{forecasts,sessions,logs} to notes/traces/<version>/."""
    version_map = _build_version_map()
    moved = 0

    if _OLD_FORECASTS.exists():
        for post_dir in sorted(_OLD_FORECASTS.iterdir()):
            if not post_dir.is_dir():
                continue
            for f in post_dir.glob("*.json"):
                version = version_map.get((post_dir.name, f.stem), _DEFAULT_VERSION)
                dest = _TRACES / version / "forecasts" / post_dir.name / f.name
                if dry_run:
                    typer.echo(f"  {f} -> {dest}")
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(f), str(dest))
                moved += 1

    if _OLD_SESSIONS.exists():
        for post_dir in sorted(_OLD_SESSIONS.iterdir()):
            if not post_dir.is_dir():
                continue
            for ts_dir in post_dir.iterdir():
                if not ts_dir.is_dir():
                    continue
                version = version_map.get(
                    (post_dir.name, ts_dir.name),
                    _version_for_post(version_map, post_dir.name),
                )
                dest = _TRACES / version / "sessions" / post_dir.name / ts_dir.name
                if dry_run:
                    typer.echo(f"  {ts_dir}/ -> {dest}/")
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(ts_dir), str(dest))
                moved += 1

    if _OLD_LOGS.exists():
        for log_file in sorted(_OLD_LOGS.glob("*.md")):
            parts = log_file.stem.split("_", 1)
            post_id = parts[0] if parts else ""
            ts = parts[1] if len(parts) > 1 else ""
            version = version_map.get(
                (post_id, ts),
                _version_for_post(version_map, post_id),
            )
            dest = _TRACES / version / "logs" / log_file.name
            if dry_run:
                typer.echo(f"  {log_file} -> {dest}")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(log_file), str(dest))
            moved += 1

    if not dry_run:
        for old_dir in (_OLD_FORECASTS, _OLD_SESSIONS, _OLD_LOGS):
            if old_dir.exists():
                try:
                    shutil.rmtree(old_dir)
                except OSError:
                    pass

    verb = "Would move" if dry_run else "Moved"
    typer.echo(f"\n{verb} {moved} items")


_SIBLING_RE = re.compile(r"^(\d+)_(\d{8}_\d{6})$")


def _build_retrodict_version_map(root: Path) -> dict[tuple[str, str], str]:
    """Build (post_id, run_timestamp) -> version from retrodict forecast JSONs.

    Retrodict filenames are <cutoff_date>_<run_timestamp>.json.
    The run_timestamp portion matches the sibling dir suffix.
    """
    version_map: dict[tuple[str, str], str] = {}
    if not root.exists():
        return version_map
    for post_dir in root.iterdir():
        if not post_dir.is_dir() or _SIBLING_RE.match(post_dir.name):
            continue
        for f in post_dir.glob("*.json"):
            parts = f.stem.split("_", 1)
            run_ts = parts[1] if len(parts) > 1 else f.stem
            version = _read_version_from_json(f)
            version_map[(post_dir.name, run_ts)] = version
    return version_map


def _migrate_retrodict_dir(root: Path, dry_run: bool) -> tuple[int, int]:
    """Move retrodict data from root into notes/traces/<version>/."""
    version_map = _build_retrodict_version_map(root)
    moved_forecasts = 0
    moved_sessions = 0

    for post_dir in sorted(root.iterdir()):
        if not post_dir.is_dir() or _SIBLING_RE.match(post_dir.name):
            continue
        for f in post_dir.glob("*.json"):
            parts = f.stem.split("_", 1)
            run_ts = parts[1] if len(parts) > 1 else f.stem
            version = version_map.get((post_dir.name, run_ts), _DEFAULT_VERSION)
            dest = _TRACES / version / "retrodict" / post_dir.name / f.name
            if dry_run:
                typer.echo(f"  {f} -> {dest}")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), str(dest))
            moved_forecasts += 1

    for sibling_dir in sorted(root.iterdir()):
        if not sibling_dir.is_dir():
            continue
        m = _SIBLING_RE.match(sibling_dir.name)
        if not m:
            continue
        post_id, run_ts = m.group(1), m.group(2)
        version = version_map.get((post_id, run_ts), _DEFAULT_VERSION)

        sess_root = sibling_dir / "sessions"
        if sess_root.exists():
            for pid_dir in sess_root.iterdir():
                if not pid_dir.is_dir():
                    continue
                for ts_dir in pid_dir.iterdir():
                    if not ts_dir.is_dir():
                        continue
                    dest = _TRACES / version / "sessions" / pid_dir.name / ts_dir.name
                    if dry_run:
                        typer.echo(f"  {ts_dir}/ -> {dest}/")
                    else:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if dest.exists():
                            shutil.rmtree(dest)
                        shutil.move(str(ts_dir), str(dest))
                    moved_sessions += 1

        struct_dir = sibling_dir / "structured"
        if struct_dir.exists():
            struct_dest = _TRACES / version / "retrodict" / post_id / "structured"
            for f in struct_dir.glob("*.json"):
                dest = struct_dest / f.name
                if dry_run:
                    typer.echo(f"  {f} -> {dest}")
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(f), str(dest))

    return moved_forecasts, moved_sessions


@app.command("retrodict")
def migrate_retrodict(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be moved"
    ),
) -> None:
    """Migrate notes/retrodict/ into notes/traces/<version>/retrodict/."""
    if not _OLD_RETRODICT.exists():
        typer.echo("No notes/retrodict/ directory found — nothing to migrate.")
        return

    forecasts, sessions = _migrate_retrodict_dir(_OLD_RETRODICT, dry_run)

    if not dry_run and _OLD_RETRODICT.exists():
        try:
            shutil.rmtree(_OLD_RETRODICT)
        except OSError:
            pass

    verb = "Would move" if dry_run else "Moved"
    typer.echo(f"\n{verb} {forecasts} forecast files, {sessions} session dirs")


_ARCHIVE_SESSION_RE = re.compile(r"^(\d+)_(.+)$")


@app.command("archive")
def migrate_archive(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be moved"
    ),
) -> None:
    """Migrate notes/archive/ into notes/traces/<version>/."""
    if not _OLD_ARCHIVE.exists():
        typer.echo("No notes/archive/ directory found — nothing to migrate.")
        return

    moved_forecasts = 0
    moved_sessions = 0
    moved_structured = 0

    retro_dir = _OLD_ARCHIVE / "retrodict"
    if retro_dir.exists():
        version_map = _build_retrodict_version_map(retro_dir)
        f, s = _migrate_retrodict_dir(retro_dir, dry_run)
        moved_forecasts += f
        moved_sessions += s
    else:
        version_map = {}

    sess_dir = _OLD_ARCHIVE / "sessions"
    if sess_dir.exists():
        for entry in sorted(sess_dir.iterdir()):
            if not entry.is_dir():
                continue
            m = _ARCHIVE_SESSION_RE.match(entry.name)
            if not m:
                continue
            post_id, ts = m.group(1), m.group(2)
            version = version_map.get(
                (post_id, ts), _version_for_post(version_map, post_id)
            )
            dest = _TRACES / version / "sessions" / post_id / ts
            if dry_run:
                typer.echo(f"  {entry}/ -> {dest}/")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.move(str(entry), str(dest))
            moved_sessions += 1

    struct_dir = _OLD_ARCHIVE / "structured"
    if struct_dir.exists():
        for f in sorted(struct_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                post_id = str(data.get("question_id") or "unknown")
            except (json.JSONDecodeError, OSError):
                post_id = "unknown"
            version = _version_for_post(version_map, post_id)
            dest = _TRACES / version / "retrodict" / post_id / "structured" / f.name
            if dry_run:
                typer.echo(f"  {f} -> {dest}")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), str(dest))
            moved_structured += 1

    if not dry_run:
        try:
            shutil.rmtree(_OLD_ARCHIVE)
        except OSError:
            pass

    verb = "Would move" if dry_run else "Moved"
    typer.echo(
        f"\n{verb} {moved_forecasts} retrodicts, {moved_sessions} sessions, "
        f"{moved_structured} structured files"
    )
