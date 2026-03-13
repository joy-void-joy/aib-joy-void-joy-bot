"""Fetch resolutions from Metaculus and update saved forecasts.

Scans both live forecasts and retrodictions under notes/traces/<version>/.
Uses batch tournament listing to minimize API calls.
"""

import asyncio
import json
from pathlib import Path

import typer

from aib.clients.metaculus import get_client
from aib.agent.history import update_forecast_file
from aib.paths import (
    iter_forecast_dirs,
    iter_forecast_files,
    iter_retrodict_dirs,
    iter_retrodict_files,
)

app = typer.Typer(no_args_is_help=True)

TOURNAMENT_IDS = [
    32916,  # AIB Spring 2026
    32715,  # MiniBench
    32585,  # Metaculus Cup
]


def get_resolution(question_data: dict) -> str | float | None:
    """Extract resolution from question data."""
    question = question_data.get("question", {})
    if not question:
        return None

    resolution = question.get("resolution")
    if resolution is None:
        return None

    q_type = question.get("type")
    if q_type == "binary":
        if resolution == 1.0:
            return "yes"
        elif resolution == 0.0:
            return "no"
        else:
            return "ambiguous"

    if q_type in ("numeric", "discrete"):
        if (
            isinstance(resolution, str)
            and not resolution.replace(".", "").replace("-", "").isdigit()
        ):
            return resolution
        return float(resolution)

    if q_type == "multiple_choice":
        return str(resolution)

    return str(resolution) if resolution is not None else None


def find_unresolved(base_path: Path) -> list[dict]:
    """Find all forecast files without resolution in a directory tree."""
    unresolved: list[dict] = []
    if not base_path.exists():
        return unresolved
    for post_dir in base_path.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                if data.get("resolution") is None:
                    unresolved.append(
                        {
                            "post_id": data.get("post_id") or int(post_dir.name),
                            "file": forecast_file,
                            "dir": post_dir,
                            "title": data.get("question_title", "Unknown")[:50],
                        }
                    )
            except (json.JSONDecodeError, OSError, ValueError):
                continue
    return unresolved


async def batch_fetch_resolved_ids(
    tournament_ids: list[int],
) -> set[int]:
    """Fetch post IDs of all resolved questions from tournaments."""
    resolved_ids: set[int] = set()

    mc = get_client()
    for tid in tournament_ids:
        offset = 0
        limit = 100
        while True:
            results = await mc.fetch_posts_list(
                {
                    "order_by": "-resolve_time",
                    "status": "resolved",
                    "tournaments": tid,
                    "offset": offset,
                    "limit": limit,
                }
            )

            if not results:
                break

            for item in results:
                post_id = item.get("id")
                if post_id is not None:
                    resolved_ids.add(post_id)

            if len(results) < limit:
                break
            offset += limit

    return resolved_ids


@app.command("check")
def check(
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Check for and apply resolution updates (live + retrodict)."""
    unresolved: list[dict] = []
    for base in {d.parent for d in iter_forecast_dirs()}:
        unresolved.extend(find_unresolved(base))
    for base in {d.parent for d in iter_retrodict_dirs()}:
        unresolved.extend(find_unresolved(base))

    if not unresolved:
        typer.echo("All forecasts already have resolutions")
        return

    unresolved_ids = {item["post_id"] for item in unresolved}
    typer.echo(f"Found {len(unresolved)} unresolved forecasts")

    async def check_all() -> tuple[int, int]:
        updated = 0
        still_open = 0

        typer.echo("Batch-fetching resolved question IDs from tournaments...")
        resolved_ids = await batch_fetch_resolved_ids(TOURNAMENT_IDS)
        typer.echo(f"  Found {len(resolved_ids)} resolved questions across tournaments")

        needs_fetch = unresolved_ids & resolved_ids
        skipped = unresolved_ids - resolved_ids
        typer.echo(
            f"  {len(needs_fetch)} of our forecasts have resolved, "
            f"{len(skipped)} still open (skipping)"
        )
        still_open = len(skipped)

        if not needs_fetch:
            typer.echo("  No new resolutions to apply")
            return updated, still_open

        items_by_id = {item["post_id"]: item for item in unresolved}

        typer.echo(f"\nFetching resolution values for {len(needs_fetch)} questions...")
        client = get_client()
        for post_id in sorted(needs_fetch):
            typer.echo(f"  Fetching {post_id}...")
            try:
                question_data = await client.fetch_post_json(post_id)
            except (OSError, ValueError) as e:
                typer.echo(f"    Error: {e}")
                continue

            resolution = get_resolution(question_data)
            if resolution is not None:
                typer.echo(f"    Resolved: {resolution}")
                if not dry_run:
                    post_dir = items_by_id[post_id]["dir"]
                    for f in post_dir.glob("*.json"):
                        if update_forecast_file(f, resolution, source="metaculus"):
                            updated += 1
                else:
                    updated += 1

            await asyncio.sleep(2.0)

        return updated, still_open

    updated, still_open = asyncio.run(check_all())

    typer.echo("\nResults:")
    typer.echo(f"  Updated: {updated} files")
    typer.echo(f"  Still open: {still_open}")
    if dry_run:
        typer.echo("  (dry run - no files changed)")


@app.command("status")
def status() -> None:
    """Show resolution status of all forecasts (live + retrodict)."""
    resolved_yes = 0
    resolved_no = 0
    resolved_other = 0
    unresolved = 0

    seen_posts: set[str] = set()
    for base in [
        *(d.parent for d in iter_forecast_dirs()),
        *(d.parent for d in iter_retrodict_dirs()),
    ]:
        if not base.exists():
            continue
        for post_dir in base.iterdir():
            if not post_dir.is_dir():
                continue
            key = f"{base}:{post_dir.name}"
            if key in seen_posts:
                continue
            seen_posts.add(key)
            for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
                try:
                    data = json.loads(forecast_file.read_text())
                    resolution = data.get("resolution")
                    if resolution == "yes":
                        resolved_yes += 1
                    elif resolution == "no":
                        resolved_no += 1
                    elif resolution is not None:
                        resolved_other += 1
                    else:
                        unresolved += 1
                except (json.JSONDecodeError, OSError):
                    continue

    total = resolved_yes + resolved_no + resolved_other + unresolved

    typer.echo(f"\n=== Resolution Status ({total} forecasts) ===\n")
    typer.echo(f"Resolved YES:   {resolved_yes}")
    typer.echo(f"Resolved NO:    {resolved_no}")
    typer.echo(f"Resolved other: {resolved_other}")
    typer.echo(f"Unresolved:     {unresolved}")


@app.command("set")
def set_resolution(
    post_id: int = typer.Argument(..., help="Post ID"),
    resolution: str = typer.Argument(
        ..., help="Resolution value (yes/no/ambiguous/value)"
    ),
) -> None:
    """Manually set resolution for a forecast."""
    updated = 0
    for f in iter_forecast_files(post_id):
        if update_forecast_file(f, resolution, source="manual"):
            updated += 1
    for f in iter_retrodict_files(post_id):
        if update_forecast_file(f, resolution, source="manual"):
            updated += 1

    if updated == 0:
        typer.echo(f"No forecasts found for post {post_id}")
        raise typer.Exit(1)

    typer.echo(f"Updated {updated} forecast files for post {post_id}")


@app.command("resolve")
def resolve(
    post_ids: list[int] = typer.Argument(
        None, help="Post IDs to resolve (all unresolved if omitted)"
    ),
    min_confidence: float = typer.Option(
        0.7, "--min-confidence", help="Minimum confidence to apply resolution"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Attempt early resolution using AI agents to check criteria."""
    from aib.agent.resolver import (
        QuestionForResolution,
        resolve_batch,
        resolve_question,
    )

    unresolved: list[dict[str, object]] = []
    for base in {d.parent for d in iter_forecast_dirs()}:
        unresolved.extend(find_unresolved(base))

    if post_ids:
        pid_set = set(post_ids)
        unresolved = [u for u in unresolved if u["post_id"] in pid_set]

    if not unresolved:
        typer.echo("No unresolved forecasts found")
        return

    typer.echo(f"Attempting resolution for {len(unresolved)} questions...\n")

    async def run() -> None:
        client = get_client()

        questions: list[QuestionForResolution] = []
        for item in unresolved:
            pid = item["post_id"]
            if not isinstance(pid, int):
                continue
            typer.echo(f"  Fetching criteria for {pid}...")
            try:
                post_data = await client.fetch_post_json(pid)
            except (OSError, ValueError) as e:
                typer.echo(f"    Error fetching {pid}: {e}")
                continue

            question = post_data.get("question", {})
            criteria = question.get("resolution_criteria") or ""
            fine_print = question.get("fine_print") or ""

            if not criteria:
                typer.echo(f"    No resolution criteria for {pid}, skipping")
                continue

            questions.append(
                QuestionForResolution(
                    post_id=pid,
                    question_title=question.get("title") or str(item.get("title", "")),
                    question_type=question.get("type", "binary"),
                    resolution_criteria=criteria,
                    fine_print=fine_print,
                    scheduled_resolve_time=question.get("scheduled_resolve_time"),
                    scheduled_close_time=question.get("scheduled_close_time"),
                )
            )
            await asyncio.sleep(1.0)

        if not questions:
            typer.echo("No questions with resolution criteria to check")
            return

        typer.echo(f"\nRunning {len(questions)} resolver agents...\n")

        if len(questions) == 1:
            results = [(questions[0].post_id, await resolve_question(questions[0]))]
        else:
            results = await resolve_batch(questions)

        applied = 0
        skipped = 0
        for pid, verdict in results:
            status_icon = "Y" if verdict.resolved else "N"
            conf_str = f"{verdict.confidence:.0%}"
            typer.echo(
                f"  [{status_icon}] {pid} (conf={conf_str}): {verdict.reason[:80]}"
            )

            if verdict.sources:
                for src in verdict.sources[:3]:
                    typer.echo(f"      src: {src}")

            if not verdict.resolved or verdict.resolution is None:
                skipped += 1
                continue

            if verdict.confidence < min_confidence:
                typer.echo(
                    f"      -> Skipped (confidence {conf_str} < {min_confidence:.0%})"
                )
                skipped += 1
                continue

            if not dry_run:
                for f in iter_forecast_files(pid):
                    update_forecast_file(
                        f,
                        verdict.resolution,
                        source="tentative",
                        reason=verdict.reason,
                    )
                applied += 1
            else:
                typer.echo(f"      -> Would apply: {verdict.resolution}")
                applied += 1

        typer.echo("\nResults:")
        typer.echo(f"  Applied: {applied}")
        typer.echo(f"  Skipped: {skipped}")
        if dry_run:
            typer.echo("  (dry run - no files changed)")

    asyncio.run(run())
