"""Reddit search tools for public discussion and sentiment data.

These tools fetch Reddit posts to provide signal for questions about
public sentiment, community reactions, and social trends.
"""

import logging
from datetime import datetime, timezone
from typing import Any, TypedDict

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.config import settings
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class RedditSearchInput(BaseModel):
    """Input for Reddit search."""

    query: str = Field(min_length=1, description="Search query")
    subreddit: str | None = Field(
        default=None,
        description=(
            "Subreddit to search within (e.g., 'economics', 'worldnews'). "
            "Omit to search all of Reddit."
        ),
    )
    sort: str = Field(
        default="relevance",
        description="Sort order: 'relevance', 'hot', 'top', 'new', 'comments'",
    )
    time_filter: str = Field(
        default="month",
        description="Time filter: 'hour', 'day', 'week', 'month', 'year', 'all'",
    )
    limit: int = Field(default=10, ge=1, le=25, description="Max results to return")


class RedditHotInput(BaseModel):
    """Input for Reddit hot posts."""

    subreddit: str = Field(
        min_length=1,
        description=(
            "Subreddit to fetch from (e.g., 'economics', 'worldnews', 'technology')"
        ),
    )
    limit: int = Field(default=10, ge=1, le=25, description="Max posts to return")


# --- Output Schemas ---


class RedditPost(TypedDict):
    """A Reddit post."""

    title: str
    score: int
    url: str
    permalink: str
    num_comments: int
    selftext_snippet: str
    created_utc: str
    subreddit: str
    author: str


# --- Reddit API ---


def _format_post(submission: Any) -> RedditPost:
    """Format an asyncpraw Submission into a RedditPost dict."""
    selftext = getattr(submission, "selftext", "") or ""
    if len(selftext) > 500:
        selftext = selftext[:500] + "..."

    created = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)

    return {
        "title": submission.title,
        "score": submission.score,
        "url": submission.url,
        "permalink": f"https://reddit.com{submission.permalink}",
        "num_comments": submission.num_comments,
        "selftext_snippet": selftext,
        "created_utc": created.isoformat(),
        "subreddit": str(submission.subreddit),
        "author": str(submission.author) if submission.author else "[deleted]",
    }


async def _get_reddit() -> Any:
    """Create an asyncpraw Reddit instance in read-only mode."""
    import asyncpraw

    return asyncpraw.Reddit(
        client_id=settings.reddit_client_id,
        client_secret=settings.reddit_client_secret,
        user_agent="aib-forecasting-bot/1.0 (by /u/aib-forecaster)",
    )


@tool(
    "reddit_search",
    (
        "Search Reddit for posts matching a query. "
        "Returns post titles, scores, comment counts, and text snippets. "
        "Useful for gauging public sentiment, finding community discussions, "
        "and understanding reactions to events. "
        "Search all of Reddit or within a specific subreddit. "
        "Common subreddits: economics, worldnews, technology, politics, science, "
        "AskReddit, dataisbeautiful, geopolitics."
    ),
    RedditSearchInput.model_json_schema(),
)
@tracked("reddit_search")
async def reddit_search(args: dict[str, Any]) -> dict[str, Any]:
    """Search Reddit posts."""
    try:
        validated = RedditSearchInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    if not settings.reddit_client_id or not settings.reddit_client_secret:
        return mcp_error(
            "Reddit API credentials not configured. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
        )

    try:
        reddit = await _get_reddit()
        try:
            if validated.subreddit:
                subreddit = await reddit.subreddit(validated.subreddit)
            else:
                subreddit = await reddit.subreddit("all")

            posts: list[RedditPost] = []
            async for submission in subreddit.search(
                validated.query,
                sort=validated.sort,
                time_filter=validated.time_filter,
                limit=validated.limit,
            ):
                posts.append(_format_post(submission))
        finally:
            await reddit.close()

        return mcp_success(
            {
                "query": validated.query,
                "subreddit": validated.subreddit or "all",
                "sort": validated.sort,
                "time_filter": validated.time_filter,
                "result_count": len(posts),
                "posts": posts,
            }
        )

    except Exception as e:
        logger.exception("Reddit search failed")
        return mcp_error(f"Reddit search failed for '{validated.query}': {e}")


@tool(
    "reddit_hot",
    (
        "Get hot/trending posts from a subreddit. "
        "Returns the most active current discussions. "
        "Useful for understanding what topics are driving conversation right now. "
        "Common subreddits: economics, worldnews, technology, politics, science, "
        "AskReddit, dataisbeautiful, geopolitics, wallstreetbets, Futurology."
    ),
    RedditHotInput.model_json_schema(),
)
@tracked("reddit_hot")
async def reddit_hot(args: dict[str, Any]) -> dict[str, Any]:
    """Get hot posts from a subreddit."""
    try:
        validated = RedditHotInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    if not settings.reddit_client_id or not settings.reddit_client_secret:
        return mcp_error(
            "Reddit API credentials not configured. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
        )

    try:
        reddit = await _get_reddit()
        try:
            subreddit = await reddit.subreddit(validated.subreddit)

            posts: list[RedditPost] = []
            async for submission in subreddit.hot(limit=validated.limit):
                posts.append(_format_post(submission))
        finally:
            await reddit.close()

        return mcp_success(
            {
                "subreddit": validated.subreddit,
                "result_count": len(posts),
                "posts": posts,
            }
        )

    except Exception as e:
        logger.exception("Reddit hot posts failed")
        return mcp_error(f"Reddit hot posts failed for r/{validated.subreddit}: {e}")


# --- MCP Server ---


def create_reddit_server():
    """Create MCP server with Reddit tools."""
    return create_mcp_server(
        name="reddit",
        version="1.0.0",
        tools=[
            reddit_search,
            reddit_hot,
        ],
    )
