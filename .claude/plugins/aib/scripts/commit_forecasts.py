"""Commit uncommitted forecast, session, and log files to git.

Finds all modified/untracked files under notes/forecasts/, notes/sessions/,
and notes/logs/, groups them by post ID, and creates one commit per question.
"""

import json
from pathlib import Path

import sh
import typer

app = typer.Typer()

FORECASTS_PATH = Path("./notes/forecasts")
SESSIONS_PATH = Path("./notes/sessions")
LOGS_PATH = Path("./notes/logs")


def _get_uncommitted_post_ids() -> set[int]:
    """Find post IDs with uncommitted forecast-related files."""
    git = sh.Command("git")
    post_ids: set[int] = set()

    status = str(git.status("--porcelain", "--", "notes/", _ok_code=[0])).strip()
    if not status:
        return post_ids

    for line in status.splitlines():
        # Format: "XY path" or "XY path -> new_path"
        file_path = line[3:].split(" -> ")[0].strip()
        parts = Path(file_path).parts

        # notes/forecasts/<post_id>/... or notes/sessions/<post_id>/...
        if (
            len(parts) >= 3
            and parts[0] == "notes"
            and parts[1]
            in (
                "forecasts",
                "sessions",
            )
        ):
            try:
                post_ids.add(int(parts[2]))
            except ValueError:
                pass

        # notes/logs/<post_id>_<timestamp>.md
        if len(parts) >= 3 and parts[0] == "notes" and parts[1] == "logs":
            filename = parts[2]
            try:
                post_ids.add(int(filename.split("_")[0]))
            except ValueError:
                pass

    return post_ids


def _get_question_title(post_id: int) -> str:
    """Read question title from the latest forecast JSON."""
    forecast_dir = FORECASTS_PATH / str(post_id)
    if not forecast_dir.exists():
        return f"question {post_id}"

    json_files = sorted(forecast_dir.glob("*.json"))
    if not json_files:
        return f"question {post_id}"

    try:
        data = json.loads(json_files[-1].read_text(encoding="utf-8"))
        return data.get("question_title", f"question {post_id}")
    except Exception:
        return f"question {post_id}"


def _commit_post(post_id: int, *, dry_run: bool = False) -> bool:
    """Stage and commit files for a single post ID."""
    git = sh.Command("git")
    paths: list[str] = []

    forecast_dir = FORECASTS_PATH / str(post_id)
    if forecast_dir.exists():
        paths.append(str(forecast_dir))

    sessions_dir = SESSIONS_PATH / str(post_id)
    if sessions_dir.exists():
        paths.append(str(sessions_dir))

    if LOGS_PATH.exists():
        for log_file in LOGS_PATH.glob(f"{post_id}_*"):
            paths.append(str(log_file))

    if not paths:
        return False

    if dry_run:
        title = _get_question_title(post_id)
        print(f"  Would commit {post_id}: {title[:50]}")
        for p in paths:
            print(f"    {p}")
        return True

    for path in paths:
        try:
            git.add(path)
        except sh.ErrorReturnCode:
            pass

    diff = str(git.diff("--cached", "--stat", _ok_code=[0, 1])).strip()
    if not diff:
        return False

    title = _get_question_title(post_id)
    slug = title[:50].strip().rstrip(".")
    git.commit("-m", f"data(forecasts): {slug}")
    print(f"  Committed {post_id}: {slug}")
    return True


@app.command()
def main(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be committed"
    ),
) -> None:
    """Commit all uncommitted forecast files, one commit per question."""
    post_ids = _get_uncommitted_post_ids()

    if not post_ids:
        print("Nothing to commit.")
        return

    print(f"Found {len(post_ids)} post(s) with uncommitted files")

    committed = 0
    for post_id in sorted(post_ids):
        try:
            if _commit_post(post_id, dry_run=dry_run):
                committed += 1
        except sh.ErrorReturnCode as e:
            print(f"  Failed {post_id}: {e}")

    if dry_run:
        print(f"\nWould commit {committed} question(s)")
    else:
        print(f"\nCommitted {committed} question(s)")


if __name__ == "__main__":
    app()
