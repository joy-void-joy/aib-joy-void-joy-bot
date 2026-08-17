"""Reddit search tools for public discussion and sentiment data.

These tools fetch Reddit posts to provide signal for questions about
public sentiment, community reactions, and social trends.
"""

from datetime import datetime, timezone
from typing import Any, TypedDict

from pydantic import BaseModel, Field

from aib.config import settings
from lup.mcp import ToolError, lup_tool


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


class RedditSearchOutput(BaseModel):
    """Posts matching a search, with the query that found them."""

    query: str
    subreddit: str
    sort: str
    time_filter: str
    result_count: int
    posts: list[RedditPost]


class RedditHotOutput(BaseModel):
    """A subreddit's current hot posts."""

    subreddit: str
    result_count: int
    posts: list[RedditPost]


# --- Reddit API ---


# lup: ignore[any-type] — asyncpraw ships no stubs; Submission is untyped
def format_post(submission: Any) -> RedditPost:
    """Format an asyncpraw Submission into a RedditPost dict."""
    selftext = getattr(submission, "selftext", "") or ""
    if len(selftext) > 500:
        selftext = selftext[:500] + "..."

    created = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)

    return RedditPost(
        title=submission.title,
        score=submission.score,
        url=submission.url,
        permalink=f"https://reddit.com{submission.permalink}",
        num_comments=submission.num_comments,
        selftext_snippet=selftext,
        created_utc=created.isoformat(),
        subreddit=str(submission.subreddit),
        author=str(submission.author) if submission.author else "[deleted]",
    )


# lup: ignore[any-type] — asyncpraw ships no stubs; Reddit is untyped
async def open_reddit() -> Any:
    """Create an asyncpraw Reddit instance in read-only mode."""
    import asyncpraw

    return asyncpraw.Reddit(
        client_id=settings.reddit_client_id,
        client_secret=settings.reddit_client_secret,
        user_agent="aib-forecasting-bot/1.0 (by /u/aib-forecaster)",
    )


def require_credentials() -> None:
    """Refuse the call when Reddit's API credentials are not configured."""
    if not settings.reddit_client_id or not settings.reddit_client_secret:
        raise ToolError(
            "Reddit API credentials not configured. "
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET."
        )


@lup_tool(
    "Search Reddit for posts matching a query. "
    "Returns post titles, scores, comment counts, and text snippets. "
    "Useful for gauging public sentiment, finding community discussions, "
    "and understanding reactions to events. "
    "Search all of Reddit or within a specific subreddit. "
    "Common subreddits: economics, worldnews, technology, politics, science, "
    "AskReddit, dataisbeautiful, geopolitics.",
    name="reddit_search",
)
async def reddit_search(args: RedditSearchInput) -> RedditSearchOutput:
    """Search Reddit posts."""
    require_credentials()

    reddit = await open_reddit()
    try:
        subreddit = await reddit.subreddit(args.subreddit or "all")
        posts = [
            format_post(submission)
            async for submission in subreddit.search(
                args.query,
                sort=args.sort,
                time_filter=args.time_filter,
                limit=args.limit,
            )
        ]
    finally:
        await reddit.close()

    return RedditSearchOutput(
        query=args.query,
        subreddit=args.subreddit or "all",
        sort=args.sort,
        time_filter=args.time_filter,
        result_count=len(posts),
        posts=posts,
    )


@lup_tool(
    "Get hot/trending posts from a subreddit. "
    "Returns the most active current discussions. "
    "Useful for understanding what topics are driving conversation right now. "
    "Common subreddits: economics, worldnews, technology, politics, science, "
    "AskReddit, dataisbeautiful, geopolitics, wallstreetbets, Futurology.",
    name="reddit_hot",
)
async def reddit_hot(args: RedditHotInput) -> RedditHotOutput:
    """Get hot posts from a subreddit."""
    require_credentials()

    reddit = await open_reddit()
    try:
        subreddit = await reddit.subreddit(args.subreddit)
        posts = [
            format_post(submission)
            async for submission in subreddit.hot(limit=args.limit)
        ]
    finally:
        await reddit.close()

    return RedditHotOutput(
        subreddit=args.subreddit,
        result_count=len(posts),
        posts=posts,
    )
