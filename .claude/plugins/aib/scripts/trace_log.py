"""Extract agent reasoning from noisy forecast logs.

Filters log files to show only agent reasoning (thinking, text, tool calls,
tool results) — stripping Docker setup, HTTP headers, and debug noise.

Usage:
    uv run python .claude/plugins/aib/scripts/trace_log.py show <post_id>
    uv run python .claude/plugins/aib/scripts/trace_log.py show <post_id> --full
    uv run python .claude/plugins/aib/scripts/trace_log.py show <post_id> --tools-only
    uv run python .claude/plugins/aib/scripts/trace_log.py list
"""

import json
import re
from pathlib import Path

import typer

app = typer.Typer(no_args_is_help=True)

LOGS_DIR = Path("logs")

STREAM_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
    r"INFO aib\.agent\.stream: "
    r"(THINKING|TEXT|TOOL_USE|TOOL_RESULT|SYSTEM|USER_MESSAGE)"
    r"(.*)"
)

COLORS = {
    "THINKING": typer.colors.CYAN,
    "TEXT": typer.colors.WHITE,
    "TOOL_USE": typer.colors.YELLOW,
    "TOOL_RESULT": typer.colors.GREEN,
    "SYSTEM": typer.colors.MAGENTA,
}

MAX_RESULT_LEN = 500


def _find_log(post_id: int) -> Path | None:
    """Find the log file for a given post ID."""
    candidates = sorted(LOGS_DIR.glob(f"{post_id}_*/*.log"), reverse=True)
    return candidates[0] if candidates else None


def _parse_stream_lines(log_path: Path) -> list[tuple[str, str, str]]:
    """Parse log file into (timestamp, event_type, content) tuples."""
    events: list[tuple[str, str, str]] = []
    current_event: tuple[str, str, str] | None = None
    continuation_lines: list[str] = []

    for line in log_path.read_text().splitlines():
        match = STREAM_PATTERN.match(line)
        if match:
            if current_event:
                full_content = current_event[2] + "\n".join(continuation_lines)
                events.append((current_event[0], current_event[1], full_content))
                continuation_lines = []

            timestamp = match.group(1)
            event_type = match.group(2)
            rest = match.group(3).strip()
            current_event = (timestamp, event_type, rest)
        elif (
            current_event and not line.startswith("2026-") and not line.startswith("20")
        ):
            continuation_lines.append(line)

    if current_event:
        full_content = current_event[2] + "\n".join(continuation_lines)
        events.append((current_event[0], current_event[1], full_content))

    return events


def _format_tool_use(content: str) -> str:
    """Format TOOL_USE event for display."""
    match = re.match(r"\[(\w+)\] ([\w_]+): (.*)", content, re.DOTALL)
    if match:
        tool_name = match.group(2)
        args_str = match.group(3).strip()
        try:
            args = json.loads(args_str)
            args_compact = json.dumps(args, separators=(",", ":"))
            if len(args_compact) > 120:
                args_compact = args_compact[:117] + "..."
            return f"{tool_name}({args_compact})"
        except (json.JSONDecodeError, ValueError):
            return f"{tool_name}({args_str[:120]})"
    return content[:200]


def _format_tool_result(content: str, max_len: int) -> str:
    """Format TOOL_RESULT event for display."""
    match = re.match(r"\[(\w+)\]: (.*)", content, re.DOTALL)
    if match:
        result = match.group(2).strip()
        if len(result) > max_len:
            result = result[:max_len] + f"... [{len(result)} chars total]"
        return result
    if len(content) > max_len:
        return content[:max_len] + f"... [{len(content)} chars total]"
    return content


@app.command()
def show(
    post_id: int = typer.Argument(help="Post ID to show trace for"),
    full: bool = typer.Option(False, help="Show full tool results (no truncation)"),
    tools_only: bool = typer.Option(
        False, "--tools-only", help="Show only tool calls and results"
    ),
    no_color: bool = typer.Option(False, "--no-color", help="Disable colored output"),
) -> None:
    """Show filtered reasoning trace for a forecast."""
    log_path = _find_log(post_id)
    if not log_path:
        typer.echo(f"No log found for post {post_id}")
        raise typer.Exit(1)

    events = _parse_stream_lines(log_path)

    result_max = 100_000 if full else MAX_RESULT_LEN
    skip_types = {"USER_MESSAGE"}
    if tools_only:
        skip_types |= {"THINKING", "TEXT", "SYSTEM"}

    typer.echo(f"--- Trace: {log_path} ({len(events)} events) ---\n")

    for timestamp, event_type, content in events:
        if event_type in skip_types:
            continue
        if event_type == "SYSTEM" and "[init]" in content:
            continue

        color = None if no_color else COLORS.get(event_type)
        time_short = timestamp.split(",")[0].split(" ")[1]

        if event_type == "THINKING":
            header = f"[{time_short}] THINKING"
            text = content[:2000] if not full else content
            typer.secho(header, fg=color, bold=True)
            typer.echo(text)
            typer.echo()

        elif event_type == "TEXT":
            header = f"[{time_short}] AGENT"
            typer.secho(header, fg=color, bold=True)
            typer.echo(content[:2000] if not full else content)
            typer.echo()

        elif event_type == "TOOL_USE":
            formatted = _format_tool_use(content)
            typer.secho(f"[{time_short}] CALL ", fg=color, bold=True, nl=False)
            typer.echo(formatted)

        elif event_type == "TOOL_RESULT":
            formatted = _format_tool_result(content, result_max)
            if "error" in formatted.lower() or "failed" in formatted.lower():
                typer.secho(f"  => ERROR: {formatted}", fg=typer.colors.RED)
            else:
                typer.secho("  => ", fg=color, nl=False)
                typer.echo(formatted[:200] if not full else formatted)


@app.command("list")
def list_logs() -> None:
    """List all available log directories."""
    if not LOGS_DIR.exists():
        typer.echo("No logs directory found")
        raise typer.Exit(1)

    dirs = sorted(LOGS_DIR.iterdir())
    for d in dirs:
        if d.is_dir():
            logs = list(d.glob("*.log"))
            size = sum(f.stat().st_size for f in logs)
            typer.echo(f"  {d.name}  ({len(logs)} logs, {size // 1024}KB)")


if __name__ == "__main__":
    app()
