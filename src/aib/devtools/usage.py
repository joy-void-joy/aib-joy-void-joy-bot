"""Display Claude Code and API key usage."""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Annotated, TypedDict

import httpx
import typer
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

app = typer.Typer(
    help="API usage and rate limit display",
    invoke_without_command=True,
)
console = Console()


# ── constants ──────────────────────────────────────────────

CREDS_PATH = Path.home() / ".claude" / ".credentials.json"
USAGE_API_URL = "https://api.anthropic.com/api/oauth/usage"
ANTHROPIC_BETA = "oauth-2025-04-20"
OPENROUTER_KEY_URL = "https://openrouter.ai/api/v1/key"
EXA_ADMIN_URL = "https://admin-api.exa.ai/team-management/api-keys"
EXA_TOURNAMENT_BUDGET = 200.0
ASKNEWS_MONTHLY_CALLS = 1000
ASKNEWS_TOURNAMENT_CALLS = 4000
TOURNAMENT_START = datetime(2026, 1, 5)
TOURNAMENT_END = datetime(2026, 5, 6)


# ── API response types ─────────────────────────────────────


class UsageBucket(TypedDict):
    utilization: float
    resets_at: str


class ExtraUsage(TypedDict):
    is_enabled: bool
    monthly_limit: int
    used_credits: float
    utilization: float


class UsageResponse(TypedDict):
    five_hour: UsageBucket | None
    seven_day: UsageBucket | None
    seven_day_opus: UsageBucket | None
    seven_day_sonnet: UsageBucket | None
    seven_day_oauth_apps: UsageBucket | None
    seven_day_cowork: UsageBucket | None
    extra_usage: ExtraUsage | None


class OpenRouterUsage(TypedDict):
    label: str
    usage: float
    limit: float | None
    limit_remaining: float | None


class ExaCostItem(TypedDict):
    price_name: str
    quantity: int
    amount_usd: float


class ExaUsage(TypedDict):
    total_cost_usd: float
    cost_breakdown: list[ExaCostItem]


class AskNewsUsage(TypedDict):
    monthly_calls: int
    monthly_limit: int
    tournament_calls: int
    tournament_limit: int


# ── pacing thresholds ──────────────────────────────────────

_PACE_COLOR_THRESHOLDS: list[tuple[float, str]] = [
    (0.7, "bright_green"),
    (1.0, "bright_cyan"),
    (1.3, "bright_yellow"),
]

_PACE_LABELS: list[tuple[float, str, str]] = [
    (0.5, "cruising", "bold bright_green"),
    (0.85, "on track", "bold bright_cyan"),
    (1.0, "on pace", "bold bright_cyan"),
    (1.3, "ahead", "bold bright_yellow"),
    (1.6, "running hot", "bold bright_red"),
]
_PACE_LABEL_DEFAULT = ("heavy usage", "bold red")


# ── API calls ──────────────────────────────────────────────


def fetch_claude_code_usage() -> UsageResponse:
    """Fetch Claude Code usage from the OAuth API."""
    creds = json.loads(CREDS_PATH.read_text())
    oauth = creds["claudeAiOauth"]
    token = oauth["accessToken"]

    resp = httpx.get(
        USAGE_API_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "anthropic-beta": ANTHROPIC_BETA,
            "Content-Type": "application/json",
        },
        timeout=10,
    )
    resp.raise_for_status()
    data: UsageResponse = resp.json()
    return data


def fetch_openrouter_usage() -> OpenRouterUsage | None:
    """Fetch OpenRouter credit balance."""
    from aib.config import settings

    key = settings.openrouter_api_key
    if not key:
        return None

    resp = httpx.get(
        OPENROUTER_KEY_URL,
        headers={"Authorization": f"Bearer {key}"},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json().get("data", {})
    return OpenRouterUsage(
        label=data.get("label", "unknown"),
        usage=data.get("usage", 0.0),
        limit=data.get("limit"),
        limit_remaining=data.get("limit_remaining"),
    )


def fetch_exa_usage() -> ExaUsage | None:
    """Fetch Exa search usage from the Admin API since tournament start."""
    from aib.config import settings

    key = settings.exa_admin_key
    if not key:
        return None

    headers = {"x-api-key": key}

    resp = httpx.get(EXA_ADMIN_URL, headers=headers, timeout=10)
    resp.raise_for_status()
    keys = resp.json().get("apiKeys", [])
    if not keys:
        return None

    key_id = keys[0]["id"]

    resp = httpx.get(
        f"{EXA_ADMIN_URL}/{key_id}/usage",
        headers=headers,
        params={"start_date": TOURNAMENT_START.strftime("%Y-%m-%dT%H:%M:%SZ")},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()

    breakdown = [
        ExaCostItem(
            price_name=item.get("price_name", "unknown"),
            quantity=item.get("quantity", 0),
            amount_usd=item.get("amount_usd", 0.0),
        )
        for item in data.get("cost_breakdown", [])
    ]

    return ExaUsage(
        total_cost_usd=data.get("total_cost_usd", 0.0),
        cost_breakdown=breakdown,
    )


def fetch_asknews_usage() -> AskNewsUsage | None:
    """Count AskNews API calls (monthly and tournament) from forecast traces."""
    from aib.paths import iter_forecast_files, parse_timestamp

    now = datetime.now()
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    monthly_calls = 0
    tournament_calls = 0

    for path in iter_forecast_files():
        try:
            ts = parse_timestamp(path.stem)
        except ValueError:
            continue
        if ts < TOURNAMENT_START:
            continue
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        by_tool = data.get("tool_metrics", {}).get("by_tool", {})
        calls = by_tool.get("search_news", {}).get("call_count", 0)
        tournament_calls += calls
        if ts >= month_start:
            monthly_calls += calls

    return AskNewsUsage(
        monthly_calls=monthly_calls,
        monthly_limit=ASKNEWS_MONTHLY_CALLS,
        tournament_calls=tournament_calls,
        tournament_limit=ASKNEWS_TOURNAMENT_CALLS,
    )


# ── formatting helpers ─────────────────────────────────────


def fmt_countdown(dt: datetime) -> str:
    total_seconds = (dt - datetime.now(dt.tzinfo)).total_seconds()
    if total_seconds <= 0:
        return "now"
    h = int(total_seconds // 3600)
    m = int((total_seconds % 3600) // 60)
    if h >= 48:
        return f"{h // 24}d {h % 24}h"
    if h > 0:
        return f"{h}h {m}m"
    return f"{m}m"


def pace_color(ratio: float) -> str:
    for threshold, color in _PACE_COLOR_THRESHOLDS:
        if ratio <= threshold:
            return color
    return "bright_red"


def pace_label(ratio: float) -> tuple[str, str]:
    for threshold, word, style in _PACE_LABELS:
        if ratio <= threshold:
            return word, style
    return _PACE_LABEL_DEFAULT


def _place_label(text: str, position: int, line_width: int) -> str:
    line = [" "] * line_width
    for j, ch in enumerate(text):
        pos = position + j
        if 0 <= pos < line_width:
            line[pos] = ch
    return "".join(line)


# ── rendering ──────────────────────────────────────────────


def render_bar(
    out: Text,
    utilization: float,
    linear_pct: float,
    bar_width: int,
) -> None:
    actual_frac = utilization / 100.0
    linear_frac = linear_pct / 100.0
    fill_color = pace_color(actual_frac / linear_frac if linear_frac > 0 else 0)

    actual_pos = min(int(actual_frac * bar_width), bar_width)
    linear_pos = min(int(linear_frac * bar_width), bar_width - 1)

    out.append("  ")
    for i in range(bar_width):
        if i == linear_pos:
            if i < actual_pos:
                out.append("▎", style="bold white on " + fill_color)
            else:
                out.append("▎", style="bold bright_white")
        elif i < actual_pos:
            out.append("█", style=fill_color)
        else:
            out.append("░", style="bright_black")
    out.append("\n")


def render_bucket(
    out: Text,
    label: str,
    bucket: UsageBucket,
    window_hours: float,
    bar_width: int,
) -> None:
    utilization = bucket["utilization"]
    resets_at = datetime.fromisoformat(bucket["resets_at"])
    window_start = resets_at - timedelta(hours=window_hours)
    now = datetime.now(resets_at.tzinfo)

    elapsed = (now - window_start).total_seconds()
    total = window_hours * 3600
    linear_pct = min((elapsed / total) * 100, 100) if total > 0 else 0
    ratio = (utilization / linear_pct) if linear_pct > 0 else 0

    word, style = pace_label(ratio)

    out.append(f"  {label}", style="bold bright_white")
    out.append(f"  {utilization:.0f}%", style="bold")
    out.append(f"  ◆ {word}", style=style)
    out.append(f"  resets in {fmt_countdown(resets_at)}", style="dim")
    out.append("\n")

    render_bar(out, utilization, linear_pct, bar_width)

    line_width = bar_width + 2

    you_text = f"↑ you ({utilization:.0f}%)"
    you_pos = min(int((utilization / 100) * bar_width), bar_width - len(you_text))
    out.append(_place_label(you_text, you_pos, line_width), style="dim")
    out.append("\n")

    pace_text = f"↑ even ({linear_pct:.0f}%)"
    pace_pos = min(int((linear_pct / 100) * bar_width), line_width - len(pace_text))
    out.append(_place_label(pace_text, pace_pos, line_width), style="dim")
    out.append("\n")


def _tournament_linear_pct() -> float:
    """Percentage of the tournament window elapsed."""
    now = datetime.now()
    total = (TOURNAMENT_END - TOURNAMENT_START).total_seconds()
    elapsed = (now - TOURNAMENT_START).total_seconds()
    return min(max(elapsed / total * 100, 0), 100) if total > 0 else 0


def _monthly_linear_pct() -> float:
    """Percentage of the current calendar month elapsed."""
    now = datetime.now()
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if now.month == 12:
        month_end = month_start.replace(year=now.year + 1, month=1)
    else:
        month_end = month_start.replace(month=now.month + 1)
    total = (month_end - month_start).total_seconds()
    elapsed = (now - month_start).total_seconds()
    return min(max(elapsed / total * 100, 0), 100) if total > 0 else 0


def _render_budget_bar(
    out: Text,
    label: str,
    used_str: str,
    limit_str: str,
    utilization: float,
    linear_pct: float,
    bar_width: int,
) -> None:
    """Render a used/limit bar with pacing indicator."""
    ratio = (utilization / linear_pct) if linear_pct > 0 else 0
    word, style = pace_label(ratio)

    out.append(f"  {label}", style="bold bright_white")
    out.append(f"  {used_str}", style="bold")
    out.append(f" / {limit_str}", style="dim")
    out.append(f"  ({utilization:.0f}%)", style="bold")
    out.append(f"  ◆ {word}", style=style)
    out.append("\n")

    render_bar(out, utilization, linear_pct, bar_width)

    line_width = bar_width + 2
    you_text = f"↑ you ({utilization:.0f}%)"
    you_pos = min(int((utilization / 100) * bar_width), bar_width - len(you_text))
    out.append(_place_label(you_text, you_pos, line_width), style="dim")
    out.append("\n")

    even_text = f"↑ even ({linear_pct:.0f}%)"
    even_pos = min(int((linear_pct / 100) * bar_width), line_width - len(even_text))
    out.append(_place_label(even_text, even_pos, line_width), style="dim")
    out.append("\n")


def _render_openrouter(
    out: Text, usage: OpenRouterUsage, bar_width: int
) -> None:
    limit = usage["limit"]
    if limit is not None and limit > 0:
        pct = usage["usage"] / limit * 100
        linear = _tournament_linear_pct()
        _render_budget_bar(out, "OpenRouter", f"${usage['usage']:.2f}", f"${limit:.2f}", pct, linear, bar_width)
    else:
        out.append("  OpenRouter", style="bold bright_white")
        out.append(f"  ${usage['usage']:.2f} used", style="bold")
        out.append("  (no limit set)", style="dim")
        out.append("\n")


def _render_exa(out: Text, usage: ExaUsage, bar_width: int) -> None:
    used = usage["total_cost_usd"]
    limit = EXA_TOURNAMENT_BUDGET
    pct = (used / limit * 100) if limit > 0 else 0
    linear = _tournament_linear_pct()
    _render_budget_bar(out, "Exa", f"${used:.2f}", f"${limit:.2f}", pct, linear, bar_width)


def _render_asknews(out: Text, usage: AskNewsUsage, bar_width: int) -> None:
    monthly = usage["monthly_calls"]
    mlimit = usage["monthly_limit"]
    mpct = (monthly / mlimit * 100) if mlimit > 0 else 0
    mlinear = _monthly_linear_pct()
    _render_budget_bar(out, "AskNews monthly", f"{monthly:,}", f"{mlimit:,} calls", mpct, mlinear, bar_width)

    out.append("\n")

    total = usage["tournament_calls"]
    tlimit = usage["tournament_limit"]
    tpct = (total / tlimit * 100) if tlimit > 0 else 0
    tlinear = _tournament_linear_pct()
    _render_budget_bar(out, "AskNews tournament", f"{total:,}", f"{tlimit:,} calls", tpct, tlinear, bar_width)


# ── display assembly ───────────────────────────────────────


def build_display(
    usage: UsageResponse | None,
    openrouter: OpenRouterUsage | None,
    exa: ExaUsage | None,
    asknews: AskNewsUsage | None,
    bar_width: int,
) -> Panel:
    out = Text()

    if usage:
        seven_day = usage.get("seven_day")
        if seven_day and seven_day.get("resets_at"):
            render_bucket(out, "Claude Code weekly usage", seven_day, 7 * 24, bar_width)
            out.append("\n")

        for label, bucket in [
            ("opus 7d", usage.get("seven_day_opus")),
            ("cowork 7d", usage.get("seven_day_cowork")),
            ("oauth 7d", usage.get("seven_day_oauth_apps")),
        ]:
            if bucket and bucket.get("resets_at"):
                render_bucket(out, label, bucket, 7 * 24, bar_width)
                out.append("\n")
    else:
        out.append("  Claude Code usage unavailable\n", style="dim italic")
        out.append("  (no credentials at ~/.claude/.credentials.json)\n\n", style="dim")

    has_tournament = exa or asknews or openrouter
    if has_tournament:
        out.append("  Tournament\n", style="bold bright_white")
        out.append("\n")

        if exa:
            _render_exa(out, exa, bar_width)
            out.append("\n")

        if asknews:
            _render_asknews(out, asknews, bar_width)
            out.append("\n")

        if openrouter:
            _render_openrouter(out, openrouter, bar_width)
            out.append("\n")

    return Panel(
        out,
        title="[bold bright_white]Usage[/bold bright_white]",
        border_style="bright_cyan",
        padding=(1, 1),
    )


def _fetch_and_build(bar_width: int) -> Panel:
    usage: UsageResponse | None = None
    openrouter: OpenRouterUsage | None = None
    exa: ExaUsage | None = None
    asknews: AskNewsUsage | None = None

    if CREDS_PATH.exists():
        try:
            usage = fetch_claude_code_usage()
        except (httpx.HTTPStatusError, httpx.ConnectError, KeyError, json.JSONDecodeError):
            pass

    try:
        openrouter = fetch_openrouter_usage()
    except (httpx.HTTPStatusError, httpx.ConnectError):
        pass

    try:
        exa = fetch_exa_usage()
    except (httpx.HTTPStatusError, httpx.ConnectError, KeyError):
        pass

    try:
        asknews = fetch_asknews_usage()
    except (OSError, KeyError):
        pass

    return build_display(usage, openrouter, exa, asknews, bar_width)


def _build_error_panel(message: str) -> Panel:
    out = Text()
    out.append(f"  {message}", style="red")
    out.append("\n  retrying...", style="dim")
    return Panel(
        out,
        title="[bold bright_white]Usage[/bold bright_white]",
        border_style="red",
        padding=(1, 1),
    )


# ── CLI ────────────────────────────────────────────────────


@app.callback(invoke_without_command=True)
def main(
    watch: Annotated[
        bool,
        typer.Option(
            "--watch/--no-watch",
            "-w",
            help="Continuously refresh the display.",
        ),
    ] = True,
    interval: Annotated[
        int,
        typer.Option(
            "--interval",
            "-n",
            help="Refresh interval in seconds (with --watch).",
        ),
    ] = 600,
) -> None:
    """Show Claude Code and API key usage."""
    bar_width = min(console.width - 10, 58)

    if not watch:
        panel = _fetch_and_build(bar_width)
        console.print()
        console.print(panel)
        return

    timestamp = Text(
        f"  updated {datetime.now().strftime('%H:%M:%S')}"
        f"  ·  every {interval}s  ·  ctrl-c to quit",
        style="dim",
    )
    try:
        panel = _fetch_and_build(bar_width)
    except (httpx.HTTPStatusError, httpx.ConnectError):
        panel = _build_error_panel("Initial fetch failed")

    with Live(
        Group(panel, timestamp),
        console=console,
        refresh_per_second=1,
        screen=True,
    ) as live:
        while True:
            try:
                time.sleep(interval)
                panel = _fetch_and_build(bar_width)
            except (httpx.HTTPStatusError, httpx.ConnectError) as e:
                panel = _build_error_panel(str(e)[:120])
            except KeyboardInterrupt:
                break
            timestamp = Text(
                f"  updated {datetime.now().strftime('%H:%M:%S')}"
                f"  ·  every {interval}s  ·  ctrl-c to quit",
                style="dim",
            )
            live.update(Group(panel, timestamp))
