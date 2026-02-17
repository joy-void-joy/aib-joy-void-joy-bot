"""Test what the Metaculus API returns for question text fields."""

import asyncio
import json
import os
from pathlib import Path

import httpx
import typer
from bs4 import BeautifulSoup
from dotenv import load_dotenv

app = typer.Typer()


async def _fetch(post_id: int) -> None:
    token = os.getenv("METACULUS_TOKEN")
    base = "https://www.metaculus.com/api"
    headers = {"Authorization": f"Token {token}", "Accept-Language": "en"}

    async with httpx.AsyncClient(timeout=30) as client:
        # 1. JSON API
        r = await client.get(f"{base}/posts/{post_id}/", headers=headers)
        r.raise_for_status()
        data = r.json()
        q = data.get("question") or {}
        desc = q.get("description")
        res_crit = q.get("resolution_criteria")
        fp = q.get("fine_print")
        title = q.get("title")
        opts = q.get("options")
        qtype = q.get("type")

        print(f"=== JSON API (post {post_id}) ===")
        print(f"  title: {title!r}")
        print(f"  type: {qtype!r}")
        print(f"  options: {opts!r}")
        print(f"  description: {_trunc(desc)}")
        print(f"  resolution_criteria: {_trunc(res_crit)}")
        print(f"  fine_print: {_trunc(fp)}")
        print()

        # 2. HTML API
        html_headers = {**headers, "Accept": "text/html"}
        r2 = await client.get(f"{base}/posts/{post_id}/", headers=html_headers)
        print(f"=== HTML API (post {post_id}) ===")
        print(f"  Status: {r2.status_code}")
        if r2.status_code == 200:
            soup = BeautifulSoup(r2.text, "html.parser")
            response_div = soup.find("div", class_="response-info")
            if response_div:
                raw = response_div.get_text()
                json_start = raw.find("{")
                if json_start != -1:
                    html_data = json.loads(raw[json_start:])
                    hq = html_data.get("question") or {}
                    print(f"  description: {_trunc(hq.get('description'))}")
                    print(
                        f"  resolution_criteria: {_trunc(hq.get('resolution_criteria'))}"
                    )
                    print(f"  fine_print: {_trunc(hq.get('fine_print'))}")
                else:
                    print("  No JSON found in HTML")
            else:
                print("  No response-info div found")
        else:
            print(f"  Body (first 300 chars): {r2.text[:300]}")

        # 3. Old API (unauthenticated)
        r3 = await client.get(f"https://www.metaculus.com/api2/questions/{post_id}/")
        print(f"\n=== Old API /api2/ (post {post_id}) ===")
        print(f"  Status: {r3.status_code}")
        if r3.status_code == 200:
            old = r3.json()
            oq = old.get("question") or old
            print(f"  Top-level keys: {list(old.keys())[:15]}")
            print(f"  description: {_trunc(oq.get('description'))}")
            print(f"  resolution_criteria: {_trunc(oq.get('resolution_criteria'))}")
            print(f"  fine_print: {_trunc(oq.get('fine_print'))}")
            # Check all top-level string fields
            for k, v in old.items():
                if isinstance(v, str) and len(v) > 20 and k not in ("title", "url"):
                    print(f"  {k}: {_trunc(v, 100)}")

        # 3b. Try alternative enrichment approaches
        print(f"\n=== Alternative enrichment (post {post_id}) ===")

        # Try ?format=api (DRF browsable format param)
        await asyncio.sleep(2)
        r_fmt = await client.get(
            f"{base}/posts/{post_id}/",
            headers=headers,
            params={"format": "api"},
        )
        print(f"  ?format=api: {r_fmt.status_code}")
        if r_fmt.status_code == 200 and "html" in r_fmt.headers.get("content-type", ""):
            from metaculus.client import _parse_html_api_response

            html_data = _parse_html_api_response(r_fmt.text)
            if html_data:
                hq = html_data.get("question") or {}
                print(f"    description: {_trunc(hq.get('description'))}")
                print(
                    f"    resolution_criteria: {_trunc(hq.get('resolution_criteria'))}"
                )
        elif r_fmt.status_code == 200:
            fq = r_fmt.json().get("question") or {}
            print(f"    description: {_trunc(fq.get('description'))}")
            print(f"    resolution_criteria: {_trunc(fq.get('resolution_criteria'))}")

        # Try Accept: text/html without auth
        await asyncio.sleep(2)
        r_noauth = await client.get(
            f"{base}/posts/{post_id}/",
            headers={"Accept": "text/html", "Accept-Language": "en"},
        )
        print(f"  HTML no-auth: {r_noauth.status_code}")

        # Try with browser-like User-Agent
        await asyncio.sleep(2)
        browser_headers = {
            **headers,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        r_browser = await client.get(
            f"https://www.metaculus.com/questions/{post_id}/",
            headers=browser_headers,
            follow_redirects=True,
        )
        print(f"  Browser UA web page: {r_browser.status_code}")
        if r_browser.status_code == 200:
            bsoup = BeautifulSoup(r_browser.text, "html.parser")
            # Check for Next.js data
            nd_script = bsoup.find("script", id="__NEXT_DATA__")
            if nd_script and nd_script.string:
                nd = json.loads(nd_script.string)
                pp = nd.get("props", {}).get("pageProps", {})
                bp = pp.get("post") or pp.get("question") or {}
                bq = bp.get("question") or {}
                print(f"    __NEXT_DATA__ description: {_trunc(bq.get('description'))}")
                print(
                    f"    __NEXT_DATA__ resolution_criteria: {_trunc(bq.get('resolution_criteria'))}"
                )
                print(f"    __NEXT_DATA__ fine_print: {_trunc(bq.get('fine_print'))}")
            else:
                print("    No __NEXT_DATA__ found")
                # Try extracting from page text
                import trafilatura

                text = trafilatura.extract(r_browser.text)
                if text:
                    print(f"    Trafilatura text (first 300): {text[:300]}")

        # Try ?include_description=true or similar param hacks
        await asyncio.sleep(2)
        for param_name in ("include_description", "expand"):
            rp = await client.get(
                f"{base}/posts/{post_id}/",
                headers=headers,
                params={param_name: "true"},
            )
            if rp.status_code == 200:
                pq = rp.json().get("question") or {}
                desc = pq.get("description")
                rc = pq.get("resolution_criteria")
                if desc or rc:
                    print(f"  ?{param_name}=true WORKS!")
                    print(f"    description: {_trunc(desc)}")
                    print(f"    resolution_criteria: {_trunc(rc)}")
                else:
                    print(f"  ?{param_name}=true: still null")

        # 4. Check the public web page for embedded JSON
        await asyncio.sleep(2)
        r4 = await client.get(
            f"https://www.metaculus.com/questions/{post_id}/",
            headers={"Accept": "text/html", "Accept-Language": "en"},
            follow_redirects=True,
        )
        print(f"\n=== Web page (post {post_id}) ===")
        print(f"  Status: {r4.status_code}")
        if r4.status_code == 200:
            soup = BeautifulSoup(r4.text, "html.parser")
            # Check for Next.js __NEXT_DATA__ JSON
            next_data = soup.find("script", id="__NEXT_DATA__")
            if next_data and next_data.string:
                nd = json.loads(next_data.string)
                props = nd.get("props", {}).get("pageProps", {})
                post_data = props.get("post") or props.get("question") or {}
                wq = post_data.get("question") or {}
                print(f"  [__NEXT_DATA__] description: {_trunc(wq.get('description'))}")
                print(
                    f"  [__NEXT_DATA__] resolution_criteria: {_trunc(wq.get('resolution_criteria'))}"
                )
                print(f"  [__NEXT_DATA__] fine_print: {_trunc(wq.get('fine_print'))}")
            else:
                print("  No __NEXT_DATA__ found")
                # Check meta tags for any description
                meta_desc = soup.find("meta", attrs={"name": "description"})
                if meta_desc:
                    print(f"  meta description: {_trunc(meta_desc.get('content'))}")


def _trunc(val: object, max_len: int = 200) -> str:
    if val is None:
        return "None"
    s = str(val)
    if len(s) > max_len:
        return s[:max_len] + "..."
    return s


@app.command()
def check(
    post_ids: list[int] = typer.Argument(help="Post IDs to check"),
) -> None:
    """Check what the API returns for question text fields."""
    project_root = Path(__file__).resolve().parents[4]
    load_dotenv(project_root / ".env")
    load_dotenv(project_root / ".env.local", override=True)
    for pid in post_ids:
        asyncio.run(_fetch(pid))
        print()


if __name__ == "__main__":
    app()
