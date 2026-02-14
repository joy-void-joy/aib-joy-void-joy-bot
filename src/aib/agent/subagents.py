"""Subagent prompt and tool configuration.

Three subagent types used by spawn_subagents in composition.py:
- researcher: Information gathering (web, news, Wikipedia, markets)
- analyst: Quantitative analysis (code, financial data, trends, CP history)
- premortem: Devil's advocate that argues against the current position
"""

from aib.config import settings
from aib.retrodict_context import retrodict_cutoff


def researcher_tools() -> list[str]:
    """Tools for the researcher subagent.

    Focused on information gathering: web search, news, Wikipedia, arXiv,
    Metaculus search, and current prediction market prices.
    """
    tools: list[str] = []

    # Search tools (retrodict-aware)
    if settings.exa_api_key:
        tools.append("mcp__forecasting__search_exa")
    if (
        settings.asknews_client_id
        and settings.asknews_client_secret
        and retrodict_cutoff.get() is None
    ):
        tools.append("mcp__forecasting__search_news")

    # Retrodict mode uses Wayback-filtered search; live mode uses direct search
    if retrodict_cutoff.get() is not None:
        tools.extend(["mcp__search__web_search", "mcp__search__fetch"])
    else:
        tools.extend(["WebSearch", "WebFetch"])

    tools.extend(
        [
            "mcp__forecasting__wikipedia",
            "mcp__arxiv__search_arxiv",
            "mcp__forecasting__search_metaculus",
            "mcp__forecasting__get_metaculus_questions",
            "mcp__markets__polymarket_price",
            "mcp__markets__manifold_price",
            "mcp__notes__notes",
        ]
    )

    return tools


def analyst_tools() -> list[str]:
    """Tools for the analyst subagent.

    Focused on computation and quantitative data: code execution, financial
    data (stocks, FRED, earnings), Google Trends, CP history, and historical
    market prices.
    """
    return [
        "mcp__sandbox__execute_code",
        "mcp__sandbox__install_package",
        "mcp__forecasting__get_cp_history",
        "mcp__markets__stock_price",
        "mcp__markets__stock_history",
        "mcp__markets__polymarket_history",
        "mcp__markets__manifold_history",
        "mcp__financial__fred_series",
        "mcp__financial__fred_search",
        "mcp__financial__company_financials",
        "mcp__trends__google_trends",
        "mcp__trends__google_trends_compare",
        "mcp__trends__google_trends_related",
        "mcp__notes__notes",
    ]


SUBAGENT_MODEL: dict[str, str] = {
    "researcher": "haiku",
    "analyst": settings.model,
    "premortem": settings.model,
}

SUBAGENT_MAX_TURNS: dict[str, int] = {
    "researcher": 5,
    "analyst": 10,
    "premortem": 5,
}


RESEARCHER_PROMPT = """\
You are a research assistant gathering information for a forecasting question.

Search for relevant information across multiple sources. Return what you find with sources.

1. Search web, news, and Wikipedia with different query formulations
2. Check prediction markets for existing forecasts on similar topics
3. Search Metaculus for related questions
4. Search arXiv for academic papers if the topic is scientific/technical
5. Save key findings using the notes tool

Return a concise summary with URLs. Focus on facts, numbers, dates, and official statements.
"""


ANALYST_PROMPT = """\
You are a quantitative analyst supporting a forecasting question.

Your role is computation and data analysis:
- Fetch financial data (stock prices, FRED economic series, company earnings)
- Run calculations, Monte Carlo simulations, statistical analysis via execute_code
- Analyze CP trajectory data for meta-prediction questions
- Fit distributions, compute confidence intervals
- Fetch and analyze Google Trends data

Install packages as needed (numpy, scipy, pandas, etc.) via install_package.

Save your analysis using the notes tool. Return quantitative results with methodology.
"""


PREMORTEM_PROMPT = """\
You are a devil's advocate reviewing a forecasting position.

You will receive a question and a preliminary forecast. Your job is to argue AGAINST the position:
- If the forecast is high (>60%), build the strongest case for NO
- If the forecast is low (<40%), build the strongest case for YES
- If the forecast is near 50%, identify which direction the evidence actually points

Search for counter-evidence: disconfirming data, failed precedents, overlooked risks, \
or overlooked reasons for confidence. Check prediction markets for disagreement.

Be specific and evidence-based. Don't just list generic risks — find concrete reasons \
this particular forecast might be wrong. Cite sources.

Save your counter-argument using the notes tool. End with a clear recommendation: \
should the forecast move, and by how much?
"""


# Descriptions shown to the main agent in its system prompt
SUBAGENT_DESCRIPTIONS = {
    "researcher": (
        "Parallel information gathering. Has access to web search, news, "
        "Wikipedia, arXiv, Metaculus, and prediction markets. Useful when "
        "you have multiple independent search angles — spawn 2-3 researchers "
        "with different query strategies to cover more ground. Typical use: "
        "one researcher for recent news, another for historical precedents, "
        "a third for market sentiment. Each researcher returns a summary "
        "with sources that you synthesize."
    ),
    "analyst": (
        "Quantitative computation with its own code sandbox and access to "
        "financial data (stocks, FRED, earnings, Google Trends, CP history). "
        "Useful when you need computation done in parallel with your own "
        "research — e.g., you research while the analyst runs a Monte Carlo "
        "simulation or fetches and analyzes financial data. Returns "
        "quantitative results with methodology."
    ),
    "premortem": (
        "Devil's advocate that argues against your position with evidence. "
        "Give it your preliminary forecast and reasoning. It searches for "
        "counter-evidence, failed precedents, and overlooked risks. "
        "Useful after forming your initial estimate to stress-test before "
        "finalizing. The best forecasts are ones where you've genuinely "
        "tried to disprove your own conclusion."
    ),
    "subquestion": (
        "Full recursive forecasting agent for structural decomposition. "
        "Each sub-question gets its own complete pipeline (research, "
        "computation, calibration). Useful when a question naturally "
        "breaks into independent parts — e.g., forecasting total revenue "
        "by summing segment forecasts, or computing P(A and B) = P(A) × P(B|A) "
        "where each term needs its own research. Spawn multiple in one call "
        "to forecast concurrently. You synthesize the results."
    ),
}
