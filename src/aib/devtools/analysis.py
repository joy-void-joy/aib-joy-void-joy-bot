"""Analysis devtools for feedback loop support.

Commands for reviewing forecasts, aggregating tool health data,
tracking analysis state, and checking data completeness.
"""

import asyncio
import json
import subprocess
from collections import Counter, defaultdict
from collections.abc import Iterator
from pathlib import Path

import typer

from aib.agent.models import ForecastSummary
from aib.paths import (
    FEEDBACK_PATH,
    TRACES_PATH,
    iter_forecast_files,
    _version_dirs,
)
from aib.version import AGENT_VERSION

app = typer.Typer(no_args_is_help=True)

ANALYZED_FILE = FEEDBACK_PATH / "analyzed.json"


# ── Helpers ──────────────────────────────────────────────────────────


def _load_analyzed() -> set[int]:
    """Load the set of already-analyzed post IDs."""
    if not ANALYZED_FILE.exists():
        return set()
    data = json.loads(ANALYZED_FILE.read_text())
    return set(data.get("analyzed", []))


def _save_analyzed(post_ids: set[int]) -> None:
    FEEDBACK_PATH.mkdir(parents=True, exist_ok=True)
    ANALYZED_FILE.write_text(
        json.dumps({"analyzed": sorted(post_ids)}, indent=2) + "\n"
    )


def _iter_session_timestamp_dirs(
    version: str | None = None,
    post_id: int | None = None,
) -> Iterator[Path]:
    """Iterate session timestamp directories (the actual session folders).

    Yields paths like: notes/traces/3.6.0/sessions/42163/20260315_120000/
    """
    if version:
        ver_dirs = [TRACES_PATH / version]
    else:
        ver_dirs = _version_dirs()

    for ver_dir in ver_dirs:
        sessions_base = ver_dir / "sessions"
        if not sessions_base.exists():
            continue
        if post_id is not None:
            post_dir = sessions_base / str(post_id)
            if post_dir.exists():
                for ts_dir in sorted(post_dir.iterdir()):
                    if ts_dir.is_dir():
                        yield ts_dir
        else:
            for post_dir in sorted(sessions_base.iterdir()):
                if not post_dir.is_dir():
                    continue
                for ts_dir in sorted(post_dir.iterdir()):
                    if ts_dir.is_dir():
                        yield ts_dir


def _version_for_session(session_dir: Path) -> str:
    """Extract version string from a session directory path."""
    # sessions_base = .../notes/traces/<version>/sessions/<post_id>/<timestamp>/
    # session_dir.parent.parent.parent = .../notes/traces/<version>
    return session_dir.parent.parent.parent.name


def _post_id_for_session(session_dir: Path) -> str:
    """Extract post_id string from a session directory path."""
    return session_dir.parent.name


def load_summaries(
    version: str | None = None,
    post_id: int | None = None,
) -> list[tuple[ForecastSummary, Path]]:
    """Load all summary.json files, returning (summary, session_dir) pairs."""
    results: list[tuple[ForecastSummary, Path]] = []
    for session_dir in _iter_session_timestamp_dirs(version=version, post_id=post_id):
        summary_file = session_dir / "summary.json"
        if not summary_file.exists():
            continue
        try:
            data = json.loads(summary_file.read_text())
            summary = ForecastSummary.model_validate(data)
            results.append((summary, session_dir))
        except (json.JSONDecodeError, ValueError, OSError):
            continue
    return results


def _load_forecasts(version: str | None = None) -> list[dict]:
    """Load forecast JSONs with file metadata."""
    forecasts: list[dict] = []
    for f in iter_forecast_files(version=version):
        try:
            data = json.loads(f.read_text())
            data["_file"] = str(f)
            data["_post_id"] = f.parent.name
            data["_version"] = f.parent.parent.parent.name
            forecasts.append(data)
        except (json.JSONDecodeError, OSError):
            continue
    return forecasts


def _find_project_root() -> Path:
    current = Path(__file__).resolve().parent
    for parent in [current, *current.parents]:
        if (parent / "pyproject.toml").exists():
            return parent
    raise RuntimeError("Could not find project root")


# ── Commands ─────────────────────────────────────────────────────────


@app.command("dashboard")
def dashboard(
    refresh: bool = typer.Option(
        False, "--refresh", help="Run resolution sync + tentative first"
    ),
) -> None:
    """One-screen health check for the feedback loop."""
    if refresh:
        typer.echo("Refreshing resolutions...")
        subprocess.run(
            ["uv", "run", "aib-devtools", "resolution", "sync"],
            check=False,
        )
        subprocess.run(
            ["uv", "run", "aib-devtools", "resolution", "tentative", "--all"],
            check=False,
        )
        typer.echo()

    typer.echo("=== Feedback Loop Dashboard ===\n")
    typer.echo(f"Agent version: {AGENT_VERSION}")

    # Forecast counts
    forecasts = _load_forecasts()
    current_version = _load_forecasts(version=AGENT_VERSION)
    resolved = [f for f in forecasts if f.get("resolution") is not None]
    resolved_current = [f for f in current_version if f.get("resolution") is not None]
    typer.echo(
        f"Forecasts: {len(forecasts)} total, "
        f"{len(current_version)} current version, "
        f"{len(resolved)} resolved ({len(resolved_current)} current)"
    )

    # Analysis state
    analyzed = _load_analyzed()
    all_post_ids = {int(f["_post_id"]) for f in forecasts if f.get("_post_id")}
    unanalyzed = all_post_ids - analyzed
    typer.echo(f"Analyzed: {len(analyzed)}, unanalyzed: {len(unanalyzed)}")

    # Summary.json coverage
    summaries = load_summaries()
    typer.echo(f"Summary.json files: {len(summaries)}")

    # Tool health headline from tool_metrics
    tool_errors: dict[str, int] = defaultdict(int)
    tool_calls: dict[str, int] = defaultdict(int)
    for f in forecasts:
        metrics = f.get("tool_metrics", {})
        for tool_name, data in (metrics.get("by_tool", {}) if metrics else {}).items():
            if isinstance(data, dict):
                tool_calls[tool_name] += data.get("call_count", 0)
                tool_errors[tool_name] += data.get("error_count", 0)

    flagged_tools = [
        name
        for name, calls in tool_calls.items()
        if calls > 0 and tool_errors.get(name, 0) / calls > 0.10
    ]
    if flagged_tools:
        typer.echo(f"Flagged tools (>10% errors): {', '.join(flagged_tools)}")
    else:
        typer.echo("Tool health: all OK")

    # Git status
    result = subprocess.run(
        ["git", "diff", "--stat"], capture_output=True, text=True, check=False
    )
    if result.stdout.strip():
        lines = result.stdout.strip().split("\n")
        typer.echo(f"Git: {lines[-1].strip()}")
    else:
        typer.echo("Git: clean")

    # Previous analysis
    analysis_dir = FEEDBACK_PATH
    if analysis_dir.exists():
        analysis_files = sorted(analysis_dir.glob("*_analysis.md"), reverse=True)
        if analysis_files:
            typer.echo(f"Last analysis: {analysis_files[0].name}")


@app.command("tool-health")
def tool_health(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
    threshold: float = typer.Option(
        10.0, "--threshold", "-t", help="Error rate threshold to flag (%)"
    ),
) -> None:
    """Aggregate tool usage and errors from forecasts and summary.json reviews."""
    # Numerical data from tool_metrics
    forecasts = _load_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    tool_stats: dict[str, dict[str, int | float]] = defaultdict(
        lambda: {"calls": 0, "errors": 0, "total_ms": 0, "posts": 0}
    )
    for f in forecasts:
        metrics = f.get("tool_metrics", {})
        by_tool = metrics.get("by_tool", {}) if metrics else {}
        for tool_name, data in by_tool.items():
            if not isinstance(data, dict):
                continue
            tool_stats[tool_name]["calls"] += data.get("call_count", 0)
            tool_stats[tool_name]["errors"] += data.get("error_count", 0)
            avg_ms = data.get("avg_duration_ms", 0)
            count = data.get("call_count", 0)
            tool_stats[tool_name]["total_ms"] += avg_ms * count
            if count > 0:
                tool_stats[tool_name]["posts"] += 1

    typer.echo(f"\n=== Tool Health ({len(forecasts)} forecasts) ===\n")
    typer.echo(
        f"{'Tool':<30} {'Calls':>8} {'Errors':>8} {'Err%':>8} "
        f"{'Avg ms':>10} {'Posts':>6}"
    )
    typer.echo("-" * 76)

    for tool_name in sorted(tool_stats, key=lambda t: -tool_stats[t]["calls"]):
        stats = tool_stats[tool_name]
        calls = int(stats["calls"])
        errors = int(stats["errors"])
        err_pct = (100 * errors / calls) if calls > 0 else 0
        avg_ms = stats["total_ms"] / calls if calls > 0 else 0
        flag = " !" if err_pct > threshold else ""
        typer.echo(
            f"{tool_name:<30} {calls:>8} {errors:>8} {err_pct:>7.1f}%"
            f"{flag} {avg_ms:>9.0f} {int(stats['posts']):>6}"
        )

    # Qualitative assessments from summary.json
    summaries = load_summaries(version=version)
    if summaries:
        typer.echo(f"\n--- Qualitative Reviews ({len(summaries)} summaries) ---\n")

        # Aggregate capability gaps
        all_gaps: list[str] = []
        all_bugs: list[str] = []
        for summary, _ in summaries:
            all_gaps.extend(summary.tool_audit.capability_gaps)
            all_bugs.extend(summary.tool_audit.subtle_bugs)

        if all_gaps:
            gap_counts = Counter(all_gaps)
            typer.echo("Capability gaps:")
            for gap, count in gap_counts.most_common(10):
                typer.echo(f"  ({count}x) {gap}")

        if all_bugs:
            typer.echo("\nSubtle bugs:")
            for bug in all_bugs[:10]:
                typer.echo(f"  - {bug}")


@app.command("tool-needs")
def tool_needs(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Aggregate capability gaps from summary.json reviews."""
    summaries = load_summaries(version=version)
    if not summaries:
        typer.echo("No summary.json files found")
        raise typer.Exit(1)

    gap_posts: dict[str, list[str]] = defaultdict(list)
    for summary, session_dir in summaries:
        post_id = _post_id_for_session(session_dir)
        for gap in summary.tool_audit.capability_gaps:
            gap_posts[gap].append(post_id)

    if not gap_posts:
        typer.echo("No capability gaps reported")
        return

    typer.echo(f"\n=== Capability Gaps ({len(summaries)} summaries) ===\n")
    for gap in sorted(gap_posts, key=lambda g: -len(gap_posts[g])):
        posts = gap_posts[gap]
        typer.echo(f"({len(posts)}x) {gap}")
        if len(posts) <= 5:
            typer.echo(f"     Posts: {', '.join(posts)}")


@app.command("flags")
def flags(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Aggregate risk flags from summary.json reviews."""
    summaries = load_summaries(version=version)
    if not summaries:
        typer.echo("No summary.json files found")
        raise typer.Exit(1)

    # Count summaries with new-schema risk_flags
    has_flags_schema = [(s, d) for s, d in summaries if s.classification is not None]
    old_schema = len(summaries) - len(has_flags_schema)

    if old_schema:
        typer.echo(f"({old_schema} old-schema summaries skipped)\n")

    if not has_flags_schema:
        typer.echo("No summaries with risk_flags (all old schema)")
        return

    # Aggregate by category
    category_posts: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    flagged_count = 0
    for summary, session_dir in has_flags_schema:
        post_id = _post_id_for_session(session_dir)
        if summary.risk_flags:
            flagged_count += 1
        for flag in summary.risk_flags:
            category_posts[flag.category].append(
                (post_id, flag.severity, flag.evidence[:80])
            )

    typer.echo(f"=== Risk Flags ({len(has_flags_schema)} summaries) ===\n")
    typer.echo(
        f"Flagged: {flagged_count}/{len(has_flags_schema)} "
        f"({100 * flagged_count / len(has_flags_schema):.0f}%)\n"
    )

    if not category_posts:
        typer.echo("No risk flags found.")
        return

    for category in sorted(category_posts, key=lambda c: -len(category_posts[c])):
        entries = category_posts[category]
        major = sum(1 for _, sev, _ in entries if sev == "major")
        typer.echo(
            f"  {category}: {len(entries)} "
            f"({major} major, {len(entries) - major} minor)"
        )
        for post_id, severity, evidence in entries[:5]:
            typer.echo(f"    [{severity}] {post_id}: {evidence}")
        if len(entries) > 5:
            typer.echo(f"    ... and {len(entries) - 5} more")

    # Reviewer agreement
    agree_count = 0
    disagree_count = 0
    for summary, _ in has_flags_schema:
        if summary.reviewer_estimate:
            if summary.reviewer_estimate.agrees_with_agent:
                agree_count += 1
            else:
                disagree_count += 1
    total_estimates = agree_count + disagree_count
    if total_estimates:
        typer.echo(
            f"\nReviewer agreement: {agree_count}/{total_estimates} "
            f"({100 * agree_count / total_estimates:.0f}%)"
        )
        if disagree_count:
            typer.echo("Disagreements:")
            for summary, session_dir in has_flags_schema:
                if (
                    summary.reviewer_estimate
                    and not summary.reviewer_estimate.agrees_with_agent
                    and summary.reviewer_estimate.divergence_reason
                ):
                    post_id = _post_id_for_session(session_dir)
                    typer.echo(
                        f"  {post_id}: {summary.reviewer_estimate.divergence_reason}"
                    )


@app.command("tracking-gaps")
def tracking_gaps(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
) -> None:
    """Check data completeness across forecasts."""
    forecasts = _load_forecasts(version=version)
    if not forecasts:
        typer.echo("No forecasts found")
        raise typer.Exit(1)

    counts = {
        "total": len(forecasts),
        "tool_metrics": 0,
        "token_usage": 0,
        "factors": 0,
        "resolution": 0,
        "summary_json": 0,
        "reflection": 0,
    }

    for f in forecasts:
        if f.get("tool_metrics"):
            counts["tool_metrics"] += 1
        if f.get("token_usage"):
            counts["token_usage"] += 1
        if f.get("factors"):
            counts["factors"] += 1
        if f.get("resolution") is not None:
            counts["resolution"] += 1

    # Check summary.json coverage
    summaries_by_post: set[str] = set()
    for _, session_dir in load_summaries(version=version):
        summaries_by_post.add(_post_id_for_session(session_dir))
    counts["summary_json"] = len(summaries_by_post)

    # Check reflection coverage
    for session_dir in _iter_session_timestamp_dirs(version=version):
        if (session_dir / "reflection.yaml").exists() or (
            session_dir / "meta.md"
        ).exists():
            counts["reflection"] += 1

    total = counts["total"]
    typer.echo(f"\n=== Data Completeness ({total} forecasts) ===\n")
    for field, count in counts.items():
        if field == "total":
            continue
        pct = 100 * count / total if total > 0 else 0
        marker = " ✗" if pct < 80 else ""
        typer.echo(f"  {field:<20} {count:>5} / {total:<5} ({pct:>5.1f}%){marker}")


@app.command("prompt-health")
def prompt_health(
    since_version: str | None = typer.Option(
        None, "--since-version", help="Count patches since this version"
    ),
) -> None:
    """Analyze the forecasting prompt for size and patch accumulation."""
    root = _find_project_root()
    prompts_file = root / "src" / "aib" / "agent" / "prompts.py"
    if not prompts_file.exists():
        typer.echo("prompts.py not found")
        raise typer.Exit(1)

    content = prompts_file.read_text()
    lines = content.split("\n")
    total_lines = len(lines)

    # Count sections (lines starting with markdown headers in string literals)
    section_count = sum(1 for line in lines if "## " in line or "### " in line)

    typer.echo("\n=== Prompt Health ===\n")
    typer.echo(f"File: {prompts_file.relative_to(root)}")
    typer.echo(f"Total lines: {total_lines}")
    typer.echo(f"Sections: ~{section_count}")

    # Count patches from CHANGELOG since a version
    if since_version:
        changelog = root / "CHANGELOG.md"
        if changelog.exists():
            cl_content = changelog.read_text()
            in_range = False
            patch_entries = 0
            for line in cl_content.split("\n"):
                if line.startswith("## "):
                    if in_range:
                        break
                    if f"v{since_version}" not in line:
                        in_range = True
                elif in_range and line.startswith("- "):
                    if "prompt" in line.lower():
                        patch_entries += 1
            typer.echo(
                f"Prompt-related CHANGELOG entries since v{since_version}: {patch_entries}"
            )


@app.command("version-diff")
def version_diff(
    v1: str = typer.Argument(help="Earlier version (e.g. 3.4.0)"),
    v2: str = typer.Argument(help="Later version (e.g. 3.6.0)"),
) -> None:
    """Show CHANGELOG entries between two versions."""
    root = _find_project_root()
    changelog = root / "CHANGELOG.md"
    if not changelog.exists():
        typer.echo("CHANGELOG.md not found")
        raise typer.Exit(1)

    content = changelog.read_text()
    in_range = False
    output_lines: list[str] = []

    for line in content.split("\n"):
        if line.startswith("## "):
            if f"v{v1}" in line:
                break
            if f"v{v2}" in line:
                in_range = True
            elif in_range:
                # Another version header in range
                pass
        if in_range:
            output_lines.append(line)

    if not output_lines:
        typer.echo(f"No CHANGELOG entries found between v{v1} and v{v2}")
        raise typer.Exit(1)

    typer.echo("\n".join(output_lines))


@app.command("mark")
def mark(
    post_ids: list[int] = typer.Argument(help="Post IDs to mark as analyzed"),
) -> None:
    """Mark forecasts as analyzed."""
    analyzed = _load_analyzed()
    new_ids = set(post_ids) - analyzed
    if not new_ids:
        typer.echo("All specified posts already marked")
        return
    analyzed.update(new_ids)
    _save_analyzed(analyzed)
    typer.echo(f"Marked {len(new_ids)} posts as analyzed: {sorted(new_ids)}")


@app.command("unmark")
def unmark(
    post_ids: list[int] = typer.Argument(help="Post IDs to unmark"),
) -> None:
    """Remove analysis marks from forecasts."""
    analyzed = _load_analyzed()
    removed = analyzed & set(post_ids)
    if not removed:
        typer.echo("None of the specified posts were marked")
        return
    analyzed -= removed
    _save_analyzed(analyzed)
    typer.echo(f"Unmarked {len(removed)} posts: {sorted(removed)}")


@app.command("status")
def status() -> None:
    """Show analysis state: which forecasts have been analyzed."""
    analyzed = _load_analyzed()
    forecasts = _load_forecasts()
    all_post_ids = {int(f["_post_id"]) for f in forecasts if f.get("_post_id")}
    unanalyzed = sorted(all_post_ids - analyzed)

    typer.echo("\n=== Analysis Status ===\n")
    typer.echo(f"Total forecasts: {len(all_post_ids)}")
    typer.echo(f"Analyzed: {len(analyzed)}")
    typer.echo(f"Unanalyzed: {len(unanalyzed)}")

    if unanalyzed:
        typer.echo(
            f"\nUnanalyzed post IDs: {', '.join(str(p) for p in unanalyzed[:20])}"
        )
        if len(unanalyzed) > 20:
            typer.echo(f"  ... and {len(unanalyzed) - 20} more")


@app.command("review")
def review(
    post_id: int | None = typer.Argument(
        None, help="Post ID to review (omit for --backfill)"
    ),
    backfill: bool = typer.Option(
        False, "--backfill", help="Review all forecasts missing summary.json"
    ),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by version"
    ),
) -> None:
    """Run the Opus reviewer on a forecast trace, producing summary.json."""
    from aib.agent.core import review_forecast_trace

    if not post_id and not backfill:
        typer.echo("Provide a post_id or use --backfill")
        raise typer.Exit(1)

    targets: list[Path] = []
    if backfill:
        for session_dir in _iter_session_timestamp_dirs(
            version=version, post_id=post_id
        ):
            trace_file = session_dir / "trace_for_condensation.md"
            summary_file = session_dir / "summary.json"
            if trace_file.exists() and not summary_file.exists():
                targets.append(session_dir)
    elif post_id:
        for session_dir in _iter_session_timestamp_dirs(
            version=version, post_id=post_id
        ):
            trace_file = session_dir / "trace_for_condensation.md"
            if trace_file.exists():
                targets.append(session_dir)

    if not targets:
        typer.echo("No sessions found to review")
        return

    typer.echo(f"Reviewing {len(targets)} session(s)...")

    for session_dir in targets:
        trace_file = session_dir / "trace_for_condensation.md"
        trace = trace_file.read_text(encoding="utf-8")
        pid = _post_id_for_session(session_dir)
        ver = _version_for_session(session_dir)

        # Try to find question title from forecast JSON
        question_title = f"Post {pid}"
        for f in iter_forecast_files(post_id=int(pid), version=ver):
            try:
                data = json.loads(f.read_text())
                if data.get("question_title"):
                    question_title = data["question_title"]
                    break
            except (json.JSONDecodeError, OSError):
                continue

        # Check if retrodict
        is_retrodict = any(
            f.name.count("_") > 1
            for f in iter_forecast_files(post_id=int(pid), version=ver)
        )

        typer.echo(f"  {pid} ({ver}): {question_title[:50]}...")
        result = asyncio.run(
            review_forecast_trace(
                trace=trace,
                question_title=question_title,
                session_dir=session_dir,
                is_retrodict=is_retrodict,
            )
        )
        if result:
            typer.echo("    → summary.json written")
        else:
            typer.echo("    → FAILED")
