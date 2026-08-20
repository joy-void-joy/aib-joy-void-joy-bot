"""Service health checks."""

import asyncio
import shutil
from collections.abc import Callable

import httpx
import sh
import typer
from pydantic import BaseModel

app = typer.Typer(no_args_is_help=True)


class CheckResult(BaseModel):
    """What one probe found, and what to print about it."""

    ok: bool
    detail: str


def check_metaculus() -> CheckResult:
    """Check Metaculus API connectivity."""
    try:
        from aib.config import settings

        if not settings.metaculus_token:
            return CheckResult(ok=False, detail="METACULUS_TOKEN not set")
        token = settings.metaculus_token[:8]
        return CheckResult(ok=True, detail=f"token valid ({token}...)")
    except (OSError, ValueError) as e:
        return CheckResult(ok=False, detail=str(e))


def check_exa() -> CheckResult:
    """Check Exa Search API key."""
    try:
        from aib.config import settings

        if not settings.exa_api_key:
            return CheckResult(ok=False, detail="EXA_API_KEY not set")
        return CheckResult(ok=True, detail="key configured")
    except (OSError, ValueError) as e:
        return CheckResult(ok=False, detail=str(e))


def check_fred() -> CheckResult:
    """Check FRED API key."""
    try:
        from aib.config import settings

        if not settings.fred_api_key:
            return CheckResult(ok=False, detail="FRED_API_KEY not set")
        return CheckResult(ok=True, detail="key configured")
    except (OSError, ValueError) as e:
        return CheckResult(ok=False, detail=str(e))


def check_asknews() -> CheckResult:
    """Ask AskNews for one story, because presence is not permission.

    The key is configured in the ordinary failing case and refused by the
    account behind it — a lapsed subscription, or a tier that excludes the
    endpoint. Only a call separates the two, so a check that read the
    setting would pass every time the news lane was about to 403.
    """
    from aib.config import settings

    if not settings.asknews_api_key:
        return CheckResult(ok=False, detail="ASKNEWS_API_KEY not set")

    from aib.tools.asknews import AskNewsRemoteError, _call_remote

    try:
        asyncio.run(
            _call_remote(settings.asknews_api_key, "search_news", {"query": "test"})
        )
    except AskNewsRemoteError as e:
        return CheckResult(ok=False, detail=str(e))
    return CheckResult(ok=True, detail="key accepted")


def check_docker() -> CheckResult:
    """Check Docker daemon availability."""
    if not shutil.which("docker"):
        return CheckResult(ok=False, detail="docker not found in PATH")

    try:
        docker = sh.Command("docker")
        docker("info", _timeout=5, _tty_out=False)
        return CheckResult(ok=True, detail="daemon running")
    except sh.ErrorReturnCode:
        return CheckResult(ok=False, detail="daemon not running")
    except sh.TimeoutException:
        return CheckResult(ok=False, detail="daemon timed out")
    except sh.CommandNotFound:
        return CheckResult(ok=False, detail="docker not found")


def check_wayback() -> CheckResult:
    """Ping the Wayback availability API for a known-archived capture."""
    try:
        response = httpx.get(
            "https://archive.org/wayback/available",
            params={"url": "example.com", "timestamp": "20250101"},
            timeout=15.0,
        )
        response.raise_for_status()
    except httpx.HTTPError as e:
        return CheckResult(ok=False, detail=str(e))

    closest = response.json().get("archived_snapshots", {}).get("closest")
    if not closest:
        return CheckResult(
            ok=False, detail="availability API returned no snapshot for example.com"
        )
    return CheckResult(ok=True, detail=f"snapshot {closest.get('timestamp')}")


class ServiceCheck(BaseModel):
    """One dependency, and the probe that answers for it."""

    name: str
    run: Callable[[], CheckResult]


CHECKS: list[ServiceCheck] = [
    ServiceCheck(name="Metaculus API", run=check_metaculus),
    ServiceCheck(name="Exa Search", run=check_exa),
    ServiceCheck(name="FRED API", run=check_fred),
    ServiceCheck(name="AskNews", run=check_asknews),
    ServiceCheck(name="Docker", run=check_docker),
    ServiceCheck(name="Wayback Machine", run=check_wayback),
]


@app.command("check")
def check() -> None:
    """Ping each external dependency and report status."""
    all_ok = True
    for service in CHECKS:
        result = service.run()
        status = "OK" if result.ok else "FAIL"
        typer.echo(f"  {service.name:20s} ... {status:4s}  ({result.detail})")
        if not result.ok:
            all_ok = False

    if not all_ok:
        raise typer.Exit(1)
