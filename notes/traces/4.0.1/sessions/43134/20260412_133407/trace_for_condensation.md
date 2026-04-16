# Reasoning Log: Will any model evaluated by Epoch AI score at least 40.0% on FrontierMath Tier 4 before May 1, 2026?

*Generated: 2026-04-12T13:44:03.606937+00:00*


## 💭 Thinking

Let me analyze this forecasting question about FrontierMath Tier 4 scores reaching 40.0% before May 1, 2026.

Key details:
- Current record: GPT-5.4 Pro at 37.5% (as of March 5, 2026)
- Threshold: 40.0%
- Deadline: May 1, 2026
- Question published: April 12, 2026
- Scheduled close: April 12, 2026 (today!)
- Resolution: May 1, 2026

The question closes TODAY and resolves May 1. So we need to check if 40% has already been achieved or if it's likely to be achieved in the next ~19 days.


I need to look up what the latest FrontierMath Tier 4 performance numbers are to see if anything has surpassed that 37.5% mark recently.

## 💬 Response

I'll research this question systematically. Let me start by fetching the question details and checking the current state of the FrontierMath Tier 4 leaderboard.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43134
  ]
}
```

### 📋 Result

```
{"post_id": 43134, "title": "Will any model evaluated by Epoch AI score at least 40.0% on FrontierMath Tier 4 before May 1, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/43134", "background_info": "FrontierMath Tier 4 is Epoch AI\u2019s set of 50 exceptionally difficult research-level math problems. Epoch\u2019s March 5, 2026
benchmark update says GPT-5.4 Pro set a new record of 37.5% on Tier 4, so 40.0% is not crazy far away but still a substantial jump on a very hard
benchmark.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"e3e89c44cabc20f3\",\"sheet_id\":537.0}}`", "resolution_criteria": "This question resolves Yes if Epoch AI publicly
reports a FrontierMath Tier 4 accuracy score of 40.0% or higher for any model before May 1, 2026. Otherwise it resolves No. According to the Leaderboard here:
[https://epoch.ai/benchmarks/frontiermath-tier-4/](https://epoch.ai/benchmarks/frontiermath-tier-4/)", "fine_print": "", "num_forecasters": 26, "community_prediction": null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://epoch.ai/benchmarks/frontiermath-tier-4/",
  "prompt": "What are the latest scores on FrontierMath Tier 4? Which models scored highest and when were they last updated?"
}
```

### 📋 Result

```
{"url": "https://epoch.ai/benchmarks/frontiermath-tier-4/", "content": "Based on the content, here are the key details about FrontierMath Tier 4 scores:\n\n**Latest Scores:**\n- **Gemini 3 Pro
Preview**: 19% (\u00b16%) - highest score mentioned\n- **Grok 4 (grok-4-0709)**: 2% (\u00b12%) - evaluated July 2025\n\n**Updated Models (from January 2026 corrections):**\nThe content mentions that
on 2026-01-23, issues with two Tier 4 problems were identified and fixed. After re-running affected models:\n- **GPT-5.2 Pro** and **GPT-5.2 (high)**: Got the corrected problem right (but exact
overall Tier 4 scores not provided in the text)\n\n**Last Updates:**\n- January 23, 2026: Problem fixes and re-grading for high-performing models\n- July 2025: Grok 4 evaluation\n- The benchmark
version was bumped to 1.1.4 after the January 2026 fixes\n\nThe content notes that FrontierMath Tier 4 consists of 50 exceptionally difficult problems, with 2 public and 48 private
problems.\n\n**Relevant links:**\n- [FrontierMath main page](https://epoch.ai/frontiermath)\n- [Public problems information](https://epoch.ai/frontiermath/tiers-1-4/benchmark-problems)\n- [Conflict of
interest statement](https://epoch.ai/frontiermath/tiers-1-4/about#:~:text=Conflict%20of%20interest%20statement)\n- [Example log viewer for o4-mini-2025-04-16](https://logs.epoch.ai/inspect-
viewer/c79c08da/viewer.html?log_file=https%3A%2F%2Flogs.epoch.ai%2Finspect_ai_logs%2FE9AfnKpQrDsFWKmXMhBbJS.eval)\n- [FrontierMath paper](https://arxiv.org/abs/2411.04872)\n- [Implementation
code](https://gist.github.com/tadamcz/7b3a45d0d5d35f758bb6deb8000731bb)", "title": "FrontierMath Tier 4"}
```

```json
{
  "query": "FrontierMath Tier 4 latest scores 2026 Epoch AI"
}
```

### 📋 Result

```
{"query": "FrontierMath Tier 4 latest scores 2026 Epoch AI", "results": [{"title": "FrontierMath Tier 4 | Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath", "snippet":
"[FrontierMath](https://epoch.ai/frontiermath) is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover
most major branches of modern mathematics \u2013 from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a
typical problem requires multiple hours of effort from a researcher in the relevant branch of mathematics, a", "api_data": null, "hint": null}, {"title": "New record on FrontierMath Tier 4 - Epoch AI
- Substack", "url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4", "snippet": "New record on FrontierMath Tier 4\nGPT-5.2 Pro (manual run) scored 31%, a substantial jump over the
previous high score of 19%.\nWe evaluated GPT-5.2 Pro manually on the ChatGPT website. We did this after encountering timeout issues with the API in our scaffold. We\u2019re working to resolve these
issues, but a manual evaluation seemed worthwhile in the meantime.\nPrior to this run, 13 problems from Tier 4 had been solved by any model ever. GPT-5.2 Pro solved 11 of those, and 4 more besides.
Its total f", "api_data": null, "hint": null}, {"title": "Data on AI Capabilities and Benchmarking | Epoch AI", "url": "https://epoch.ai/benchmarks/", "snippet": "Our database of benchmark results,
featuring the performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI as well as data collected from external sources. Explore
trends in AI capabilities across time, by benchmark, or by model.\nWe added APEX-Agents, ARC-AGI-2, and HLE to the Epoch Capabilities Index. GPT-5.4 Pro now leads, narrowly ahead of Gemini 3.1
Pro.\nGPT-5.4 Pro set a new record on FrontierMath, scoring 50% on Tiers 1\u20133 an", "api_data": null, "hint": null}, {"title": "FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch
AI", "url": "https://epoch.ai/frontiermath/tiers-1-4/about", "snippet": "To measure AI progress effectively, we need benchmarks that evaluate complex scientific reasoning. Mathematics is an ideal
domain because it involves precise, step-by-step logic, and solutions to closed-form math problems can be automatically verified, avoiding subjective or costly evaluations.\nFrontierMath comprises 350
original mathematics problems spanning from challenging university-level questions to problems that may take expert mathematicians days to solve, covering a wide variety of topi", "api_data": null,
"hint": null}, {"title": "Share of FrontierMath problems solved correctly by AI models - Our World in Data", "url": "https://ourworldindata.org/grapher/ai-frontiermath-over-time", "snippet": "Share of
FrontierMath problems solved correctly by AI models\n![](/grapher/ai-frontiermath-over-time.png)\nWhat you should know about this indicator\n- This indicator shows the share of FrontierMath problems
that AI models solve correctly, based on Epoch AI's evaluation.\n- FrontierMath is a set of 350 original math problems written by experts, covering many areas of advanced mathematics. Many problems
are difficult enough that human specialists might need hours or days to solve them.\n- The benchmar", "api_data": null, "hint": null}, {"title": "The Epoch AI Brief - January 2026 - Epoch AI", "url":
"https://epochai.substack.com/p/the-epoch-ai-brief-january-2026", "snippet": "The Epoch AI Brief - January 2026\nAI Chip Sales data explorer launch! FrontierMath: Open Problems benchmark, global AI
power capacity, OpenAI profitability, how well last year's forecasts did, and a podcast about AI math capabilities\n2026 is off to a fast start! In this edition of the Epoch AI brief:\nWe launched
the\n[AI Chip Sales data explorer](https://epoch.ai/blog/introducing-the-ai-chip-sales-data-explorer), tracking compute capacity across Nvidia, Google, Amazon, AMD, and Huawei - global AI",
"api_data": null, "hint": null}, {"title": "FrontierMath Benchmark 2026: 1 LLM scores | BenchLM.ai", "url": "https://benchlm.ai/benchmarks/frontierMath", "snippet": "An expert-level mathematical
reasoning benchmark by Epoch AI featuring original, research-level problems created by mathematicians including IMO gold medalists and Fields Medal recipients. Problems require deep creativity and
multi-step reasoning.\nAs of April 10, 2026, [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) leads the FrontierMath leaderboard with 50%.\nYear\n2024\nTasks\n350 original research-level math
problems\nFormat\nOpen-ended mathematical reasoning with tool access\nDifficulty\nResea", "api_data": null, "hint": null}, {"title": "Epoch AI on X: \"New record on FrontierMath Tier 4! GPT-5.2 Pro
scored 31%, a substantial jump over the previous high score of 19%. Read on for details, including comments from mathematicians. https://t.co/i5nj1kTcMt\" / X", "url":
"https://x.com/EpochAIResearch/status/2014769359747744200", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to
continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null,
"hint": null}, {"title": "What will be the best FrontierMath Tier 4 score by Dec 31, 2026? | Manifold", "url": "https://manifold.markets/Bayesian/what-will-be-the-best-frontiermath", "snippet": "This
market matches [Mathematics: FrontierMath Tier 4](https://forecast2026.ai/)[ from the AI 2026 Forecasting Survey by AI Digest](https://forecast2026.ai/).\nSee other manifold questions
[here](https://manifold.markets/topic/2026-ai-forecasting-survey-by-ai-di)\n![](https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-
images%2Fdefault%2F8lqPqzZzLn.png?alt=media&token=4e32a80f-b6fe-4c54-afd8-0532c22a4fd8)\nResolution criteria\nResolves to the highest reported accuracy on Fr", "api_data": null, "hint": "Use
manifold_price for market data, or manifold_history for historical prices."}, {"title": "Epoch AI on X: \"GPT-5.4 set a new record on FrontierMath, our benchmark of extremely challenging math
problems! We had pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%. See thread for commentary and additional experiments.
https://t.co/u0JnYOjrLO\" / X", "url": "https://x.com/EpochAIResearch/status/2029626255776395425", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript
or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info
\u00a9 2026 X Corp.", "api_data": null, "hint": null}]}
```

## 💬 Response

Interesting - the search results show some discrepancies. The question description says GPT-5.4 Pro scored 37.5%, but one search result says 38% and another says 50% on Tiers 1-3. Let me get more precise data from the actual leaderboard and recent announcements.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4",
  "prompt": "What are the exact FrontierMath Tier 4 scores mentioned? What models achieved them and when?"
}
```

### 📋 Result

```
{"url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4", "content": "Based on the content, here are the exact FrontierMath Tier 4 scores mentioned:\n\n**Current scores:**\n-
**GPT-5.2 Pro (manual run)**: 31% (15/48 problems)\n  - 5/28 (18%) on non-held-out problems\n  - 10/20 (50%) on held-out problems\n- **Previous high score**: 19% (model not specified, but this was
before GPT-5.2 Pro's evaluation)\n- **Pass@the-kitchen-sink** (all problems ever solved by any model): 35% (17/48 problems)\n\n**Historical mentions:**\n- Before GPT-5.2 Pro's run, only 13 Tier 4
problems had been solved by any model ever\n- GPT-5.2 Pro solved 11 of those 13 previously-solved problems, plus 4 new ones\n\n**Updated scores after problem fixes:**\nThe content mentions that two
problems had issues, and after fixing them, updated scores were posted for:\n- GPT-5.2 Pro\n- GPT-5.2 (high)\n- GPT-5.2 (xhigh)\n- GPT-5.2 (medium)\n- GPT-5 Pro\n\nHowever, the exact numerical scores
for these other models are not provided in the text.\n\n**Timeline:** The specific date of GPT-5.2 Pro's evaluation is not mentioned, only that it was recent (\"a manual evaluation seemed worthwhile
in the meantime\").\n\n**Relevant links:**\n- [FrontierMath website with more info and analysis](https://epoch.ai/frontiermath)", "title": "New record on FrontierMath Tier 4"}
```

```json
{
  "url": "https://epoch.ai/benchmarks/frontiermath",
  "prompt": "What are all the FrontierMath Tier 4 scores listed? Which model has the highest score? When was this last updated?"
}
```

### 📋 Result

```
{"url": "https://epoch.ai/benchmarks/frontiermath", "content": "Based on the content, here are the **FrontierMath Tier 4 scores** listed:\n\n1. **Gemini 3 Pro Preview**: 19% (\u00b16%)\n2. **Grok 4
(grok-4-0709)**: 2% (\u00b12%)\n\n**Highest score**: Gemini 3 Pro Preview with 19% (\u00b16%)\n\n**Last updated**: The most recent Tier 4-related update mentioned is from **July 2025** (when Grok 4
was evaluated on the Tier 4 benchmark released 2025-07-01).\n\nNote: The content mentions that GPT-5.2 Pro and GPT-5.2 (high) solved a corrected Tier 4 problem (per the 2026-01-23 update), but their
overall Tier 4 scores are not provided in this text.\n\n**Relevant links:**\n- [FrontierMath main page](https://epoch.ai/frontiermath)\n- [Public benchmark problems
information](https://epoch.ai/frontiermath/tiers-1-4/benchmark-problems)\n- [Conflict of interest
statement](https://epoch.ai/frontiermath/tiers-1-4/about#:~:text=Conflict%20of%20interest%20statement)\n- [Example log viewer for o4-mini-2025-04-16](https://logs.epoch.ai/inspect-
viewer/c79c08da/viewer.html?log_file=https%3A%2F%2Flogs.epoch.ai%2Finspect_ai_logs%2FE9AfnKpQrDsFWKmXMhBbJS.eval)\n- [FrontierMath paper](https://arxiv.org/abs/2411.04872)\n- [Implementation
code](https://gist.github.com/tadamcz/7b3a45d0d5d35f758bb6deb8000731bb)", "title": "FrontierMath Tier 4"}
```

```json
{
  "query": "FrontierMath Tier 4 score record 2026",
  "hours_back": 720,
  "n_articles": 10
}
```

### 📋 Result

```
Error calling tool 'search_news': APIError: 403015 - You've reached your maximum billable overage limit for 'requests'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

## 💬 Response

The leaderboard page seems to be showing incomplete data. Let me specifically search for the GPT-5.4 Pro score on Tier 4, since the question mentions a March 5, 2026 update and the X post mentions 38%.

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__asknews__search_x_twitter


```json
{
  "query": "GPT-5.4 Pro FrontierMath Tier 4 score 37.5% 38% March 2026 Epoch AI",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "GPT-5.4 set a new record on FrontierMath - Epoch AI | Substack", "url": "https://epochai.substack.com/p/gpt-54-set-a-new-record-on-frontiermath", "snippet": "GPT-5.4 set a new record on
FrontierMath - Epoch AI\n\n# Epoch AI\n\nSubscribeSign in\n\nUpdates\n\n# GPT-5.4 set a new record on FrontierMath\n\n### Solved one Tier 4 problem that no model had solved before\n\nEpoch AI\n\nMar
05, 2026\n\n3\n\n2\n\nShare\n\nGPT-5.4 set a new record on FrontierMath, our benchmark of extremely challenging math problems!\n\nWe had pre-release access to evaluate the model. On Tiers 1\u20133,
GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%.\n\nSee below for commentary and additional experiments.Fr", "highlights": ["GPT-5.4 set a new record on FrontierMath - Epoch AI\n\n# Epoch
AI\n\nSubscribeSign in\n\nUpdates # GPT-5.4 set a new record on FrontierMath\n\n### Solved one Tier 4 problem that no model had solved before\n\nEpoch AI Mar 05, 2026\n\n3\n\n2\n\nShare GPT-5.4 set a
new record on FrontierMath, our benchmark of extremely challenging math problems! We had pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%.
See below for commentary and additional experiments.FrontierMath was funded by OpenAI, who has exclusive access to: all 290 problems in Tiers 1\u20133; solutions to 237 of these problems; 28 of the 48
problems in Tier 4; solutions to these 28 problems. Epoch holds out the rest.On Tiers 1\u20133 GPT-5.4 Pro solved 52% of the non-held-out set and 42% of the held-out set. On Tier 4, GPT-5.4 Pro solved
25% of the non-held-out set and 55% of the held-out set. Neither of these differences is statistically significant.GPT-5.4 Pro solved one Tier 4 problem that no model had solved before. In a
preliminary analysis, it appeared to have found a preprint from 2011 which let it shortcut much of the intended work. The problem author was unaware of this preprint.We ran GPT-5.4 (xhigh) an
additional ten times on Tier 4 to get a pass@10 score. This was 38%. In one of these runs, it solved another problem no model had solved before. This problem was by Bartosz Naskr\u0119cki, who
responded as follows: Across all runs ever, 42% (20/48) of the problems in Tier 4 have now been solved at least once.We also evaluated GPT-5.4 Pro on FrontierMath: Open Problems. It did not solve any
problems. It made some novel observations on one problem, but of a form that the author had anticipated and characterized as relatively uninteresting. More here.Check out our website for more results
and commentary about FrontierMath overall! ---\n\nSubscribe\n\n3\n\n2\n\nShare\n\nPreviousNext\n\n#### Discussion about this post\n\nCommentsRestacks\n\nNo posts ### Ready for
more?\n\nSubscribe\n\n\u00a9 20"], "published_date": "2026-03-05T18:57:39.000", "score": null}, {"title": "FrontierMath - Tier 4 Benchmark Details | LLM Leaderboard | DataLearnerAI", "url":
"http://www.datalearner.com/benchmarks/frontier-math-tier-4", "snippet": "FrontierMath - Tier 4 Benchmark Details | LLM Leaderboard | DataLearnerAI\n\nDataLearner logoDataLearnerAIToggle menu\nSearch
blog\n\u4e2dEN\n\u52a0\u8f7d\u4e2d...\nFrontierMath - Tier 4 Benchmark Details | LLM Leaderboard | DataLearnerAI\n# FrontierMath - Tier 4
\u8bc4\u6d4b\u57fa\u51c6\u8be6\u60c5\nFrontierMath\u662f\u4e00\u4e2a\u7531Epoch AI\u5f00\u53d1\u7684\u57fa\u51c6\u6d4b\u8bd5\u5957\u4ef6\uff0c\u5305\u542b\u6570\u767e\u4e2a\u539f\u521b\u7684\u6570\u5b
66\u95ee\u9898\u3002\u8fd9\u4e9b\u95ee\u9898\u7531\u4e13\u5bb6\u6570\u5b66\u5bb6\u8bbe\u8ba1\u548c\u5ba1\u6838\uff0c\u8986\u76d6\u73b0\u4ee3\u6570\u5b66\u7684\u4e3b\u8981\u5206\u652f\uff0c\u5982\u6570
\u8bba\u3001\u5b9e\u5206\u6790\u3001\u4ee3\u6570\u51e0\u4f55\u548c\u8303\u7574\u8bba\u3002\u6bcf\u4e2a\u95ee\u9898\u901a\u5e38\u9700\u8981\u76f8\u5173\u9886\u57df\u7814\u7a76\u4eba\u5458\u6295\u5165\u
6570\u5c0f\u65f6\u81f3\u6570\u5929\u7684\u52aa\u529b\u6765\u89e3\u51b3\u3002\u57fa\u51c6\u91c7\u7528\u672a\u53d1\u8868\u7684\u95ee\u9898\u548c\u81ea\u52a8\u5316\u9a8c\u8bc1\u673a\u5236\uff0c\u4ee5\u51
cf\u5c11\u6570\u636e\u6c61\u67d3\u98ce\u9669\u5e76\u786e\u4fdd\u8bc4\u4f30\u53ef\u9760\u6027\u3002\u5f53\u524d\u6700\u5148\u8fdb\u7684AI\u6a21\u578b\u5728\u8be5\u57fa\u51c6\u4e0a\u7684\u89e3\u51b3\u73
87\u4f4e\u4e8e2%\uff0c\u8fd9\u53cd\u6620\u51faAI\u5728\u5904\u7406\u4e13\u5bb6\u7ea7\u6570\u5b66\u63a8\u7406\u65f6\u7684\u5c40\u9650\u6027\u3002\u8be5\u57fa\u51c6\u65e8\u5728\u4e3aAI\u7cfb\u7edf\u5411
\u7814\u7a76\u7ea7\u6570\u5b66\u80fd\u529b\u8fdb\u6b65\u63d0\u4f9b\u91cf\u5316\u6307\u6807\u3002\n\u66f4\u65b02026-03-12\nViews739\n", "highlights": ["FrontierMath\u662f\u4e00\u4e2a\u7531Epoch AI\u5f0
0\u53d1\u7684\u57fa\u51c6\u6d4b\u8bd5\u5957\u4ef6\uff0c\u5305\u542b\u6570\u767e\u4e2a\u539f\u521b\u7684\u6570\u5b66\u95ee\u9898\u3002\u8fd9\u4e9b\u95ee\u9898\u7531\u4e13\u5bb6\u6570\u5b66\u5bb6\u8bbe\
u8ba1\u548c\u5ba1\u6838\uff0c\u8986\u76d6\u73b0\u4ee3\u6570\u5b66\u7684\u4e3b\u8981\u5206\u652f\uff0c\u5982\u6570\u8bba\u3001\u5b9e\u5206\u6790\u3001\u4ee3\u6570\u51e0\u4f55\u548c\u8303\u7574\u8bba\u3
002\u6bcf\u4e2a\u95ee\u9898\u901a\u5e38\u9700\u8981\u76f8\u5173\u9886\u57df\u7814\u7a76\u4eba\u5458\u6295\u5165\u6570\u5c0f\u65f6\u81f3\u6570\u5929\u7684\u52aa\u529b\u6765\u89e3\u51b3\u3002\u57fa\u51c
6\u91c7\u7528\u672a\u53d1\u8868\u7684\u95ee\u9898\u548c\u81ea\u52a8\u5316\u9a8c\u8bc1\u673a\u5236 \uff0c\u4ee5\u51cf\u5c11\u6570\u636e\u6c61\u67d3\u98ce\u9669\u5e76\u786e\u4fdd\u8bc4\u4f30\u53ef\u9760
\u6027\u3002\u5f53\u524d\u6700\u5148\u8fdb\u7684AI\u6a21\u578b\u5728\u8be5\u57fa\u51c6\u4e0a\u7684\u89e3\u51b3\u7387\u4f4e\u4e8e2%\uff0c\u8fd9\u53cd\u6620\u51faAI\u5728\u5904\u7406\u4e13\u5bb6\u7ea7\u
6570\u5b66\u63a8\u7406\u65f6\u7684\u5c40\u9650\u6027\u3002\u8be5\u57fa\u51c6\u65e8\u5728\u4e3aAI\u7cfb\u7edf\u5411\u7814\u7a76\u7ea7\u6570\u5b66\u80fd\u529b\u8fdb\u6b65\u63d0\u4f9b\u91cf\u5316\u6307\u
6807\u3002 \u66f4\u65b02026-03-12\nViews739\n\u95ee\u9898\u6570\u91cf\n300\n\u53d1\u5e03\u673a\u6784\nEpoch
AI\n\u8bc4\u6d4b\u7c7b\u522b\n\u6570\u5b66\u63a8\u7406\n\u8bc4\u6d4b\u6307\u6807\nAccuracy\n\u652f\u6301\u8bed\u8a00\n\u82f1\u6587\n\u96be\u5ea6\u7b49\u7ea7\n\u9ad8\u96be\u5ea6\n### \u7b80\u4ecb
FrontierMath \u662f\u4e00\u4e2a\u7528\u4e8e\u8bc4\u4f30\u4eba\u5de5\u667a\u80fd\u9ad8\u7ea7\u6570\u5b66\u63a8\u7406\u80fd\u529b\u7684\u57fa\u51c6\u6d4b\u8bd5\u3002FrontierMath - Tier
4\u662f\u5176\u4e2d\u7814\u7a76\u751f\u7ea7\u522b\u7684\u96be\u9898\uff01\n### \u76f8\u5173\u8d44\u6e90 ## FrontierMath - Tier 4 Model Score Leaderboard\nSource: DataLearnerAI   ...    No parallel
thinking results available\nShow parallel thinking results\n## FrontierMath - Tier 4\u8be6\u7ec6\u6392\u540d\u6570\u636e\u8868\u683c
|\u6392\u540d|\u6a21\u578b|\u5f97\u5206|\u53d1\u5e03\u65f6\u95f4|\u53c2\u6570(\u4ebf)|\n|1|\nGPT-5.4
Pro\u5e38\u89c4\u6a21\u5f0f\uff08\u65e0\u5de5\u5177\uff09\n|38|2026-03-05|\u672a\u77e5|\n|2|\nGPT-5.4 Pro\u601d\u8003\u6a21\u5f0f High\uff08\u65e0\u5de5\u5177\uff09\n|38|2026-03-05|\u672a\u77e5|\n|3|
GPT-5.2 Prothinking\n|31.3|2025-12-11|\u672a\u77e5|\n|4|\nGPT-5.4\u6781\u9ad8\u5f3a\u5ea6\u601d\u8003\uff08\u65e0\u5de5\u5177\uff09\n|27.1|2026-03-05|\u672a\u77e5|\n|5| Gemini 3.0 Pro (Preview
11-2025)thinking\n|18.8|2025-11-18|\u672a\u77e5|\n|6|\nGPT-5-Prothinking\n|14.6|2025-08-07|\u672a\u77e5|\n|7| GPT-5.2\u6781\u9ad8\u5f3a\u5ea6\u601d\u8003\uff08\u5de5\u5177\uff09\n|14.6|2025-12-
11|\u672a\u77e5|\n|8|\nGPT-5high\n|12.5|2025-08-07|\u672a\u77e5|\n|9|\nGPT-5.1high\n|12.5|2025-11-12|\u672a\u77e5|\n|10|   ...    |30|\nGPT-4.1\n|0.01|2025-04-14|\u672a\u77e5|\n1\nGPT-5.4
Pro\u5e38\u89c4\u6a21\u5f0f\uff08\u65e0\u5de5\u5177\uff09\n38\n2\nGPT-5.4 Pro\u601d\u8003\u6a21\u5f0f High\uff08\u65e0\u5de5\u5177\uff09\n38\n3\nGPT-5.2 Prothinking\n31.3\n4
GPT-5.4\u6781\u9ad8\u5f3a\u5ea6\u601d\u8003\uff08\u65e0\u5de5\u5177\uff09\n27.1\n5\nGemini 3.0 Pro (Preview
11-2025)thinking\n18.8\n6\nGPT-5-Prothinking\n14.6\n7\nGPT-5.2\u6781\u9ad8\u5f3a\u5ea6\u601d\u8003\uff08\u5de5\u5177\uff09
14.6\n8\nGPT-5high\n12.5\n9\nGPT-5.1high\n12.5\n10\nGPT-5.1\u601d\u8003\u6a21\u5f0f High\uff08\u5de5\u5177\uff09\n12.5\n11\nGemini 2.5 Deep Think\n10.4\n12 OpenAI o4 -
minihigh\n6.3\n13\nGPT-5medium\n6.3\n14\nOpenAI o3-mini (high)high\n4."], "published_date": null, "score": null}, {"title": "FrontierMath Tier 4 | Epoch AI", "url":
"https://epoch.ai/benchmarks/frontiermath", "snippet": "FrontierMath Tier 4 | Epoch AI\n\n \n\n# FrontierMath Tier 4\n\n \n\nFrontierMath Tier 4\n\nMethodology\n\n### FrontierMath Tier
4\n\nFrontierMath is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern
mathematics \u2013 from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requi",
"highlights": ["FrontierMath Tier 4 | Epoch AI\n\n \n\n# FrontierMath Tier 4\n\n \n\nFrontierMath Tier 4\n\nMethodology\n\n### FrontierMath Tier 4 FrontierMath is a benchmark of hundreds of original,
exceptionally challenging mathematics problems crafted and vetted   ...    The full FrontierMath dataset contains 350 problems. This is split into a base set of 300 problems, which we call Tiers 1-3,
and an expansion set of 50 exceptionally difficult problems, which we call Tier 4. We have made 10 problems from Tiers 1-3 public, calling this`frontiermath-2025-02-28-public`. The remaining 290
problems make up`frontiermath-2025-02-28-private`. Similarly, we have made 2 problems from Tier 4 public, calling this`frontiermath-tier-4-2025-07-01-public`, while the remaining 48 problems make
...    FrontierMath was developed with funding from OpenAI, who has exclusive access to a subset of the benchmark. See our   ...    For FrontierMath, we recommend using the log viewer on the public
questions as the best way to understand the   ...    For each FrontierMath question, the model needs to submit a Python function`answer()` that returns the answer. The   ...    - If your answer is
correct you will get 1 point. If it is incorrect, or if you don\u2019t submit an answer, you will get 0   ...    in`frontiermath-2025-02-28-private`). ### Changelog 2026-01-23. We identified issues
with two Tier 4 problems that affected prior scores. In one case the issue was with our grader, so we could re-grade solutions given by models on prior runs. The models that got this problem right
were: GPT-5.2 Pro, GPT-5.2 (xhigh), GPT-5.2 (high), GPT-5.2 (medium), and GPT-5 Pro. In the other case the issue was with the problem statement itself. Here we re-ran every model that had scored over
10% on Tier 4 on this one problem. Only GPT-5.2 Pro and GPT-5.2 (high) got the corrected problem right. We adjusted the scores of all of these models   ...    We also fixed an error in the problem
statement for public problem`PLD1` in`FrontierMath-2025-02-28-Public`. Several models had in fact been getting the right answer to the mis-stated problem (the answer was 281718171540). Since this
problem set is just for illustrative purposes, we have not updated those scores on our hub. We bumped the benchmark version number to 1.1.4 to reflect these fixes. 2026-01-22. We upgraded our Inspect
dependency, and bumped the benchmark version number to 1.1.3.   ...    We ran this model on Fireworks for data security. We found that, when run on public benchmarks, the model performed   ...
until they completed. This accounts for the larger standard error associated with this model\u2019s score. Gemini 2.5 Pro and Gemini 3 Pro We encountered an unusual number of API errors when trying to
benchmark these models in a timely manner after their   ...    failed, we marked the sample as incorrect. An earlier version of this site included`gemini-2.5.-pro` in this table, but   ...    The
table below shows how many samples were marked as incorrect in this way. | Model | Benchmark | Accuracy | Samples marked as incorrect after retries |\n| --- | --- | --- | --- | | gemini-2.5-pro-
preview-06-05 | FrontierMath-2025-02-28-Private | 10% (\u00b12%) | 21/290 = 7% | | gemini-3-pro-preview | FrontierMath-2025-02-28-Private | 38% (\u00b13%) | 10/290=3% | | gemini-3-pro-preview |
FrontierMath-Tier-4-2025-02-28-Private | 19% (\u00b16%) | 3/48=6% | Grok 4\n\nFor`grok-4-0709`, we experienced timeouts and network errors using the API in July 2025. As a result, as of July 2025, we
evaluated Grok 4 using specific scoring rules: FrontierMath-2025-02-28-Private was evaluated using our standard settings. The record ID is gda5UeWrA8HcbDCRuLJ56H. We used the streaming API. 1/290 was
not scored due to the server not sending any response. (We allow up to 1% of samples   ...    For FrontierMath-Tier-4-2025-07-01-Private, we used a maximum output length per request of 128,000 tokens
(default is   ...    | Benchmark | Accuracy | Samples with API errors | Run ID |\n| --- | --- | --- | --- | | FrontierMath-Tier-4-2025-07-01-Private | 2% (\u00b12%) | 8 out of 48 (16%) |
QxtNUmV2L34UyrySmBLTbv |   ...    The code"], "published_date": null, "score": null}, {"title": "FrontierMath Tier 4 - Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath-tier-4", "snippet":
"FrontierMath Tier 4 | Epoch AI\n\n \n\n# FrontierMath Tier 4\n\n \n\nFrontierMath Tier 4\n\nMethodology\n\n### FrontierMath Tier 4\n\nFrontierMath is a benchmark of hundreds of original,
exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics \u2013 from computationally intensive problems
in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requi", "highlights": ["FrontierMath Tier 4 | Epoch AI\n\n \n\n#
FrontierMath Tier 4\n\n \n\nFrontierMath Tier 4\n\nMethodology\n\n### FrontierMath Tier 4 FrontierMath is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted
and vetted   ...    The full FrontierMath dataset contains 350 problems. This is split into a base set of 300 problems, which we call Tiers 1-3, and an expansion set of 50 exceptionally difficult
problems, which we call Tier 4. We have made 10 problems from Tiers 1-3 public, calling this`frontiermath-2025-02-28-public`. The remaining 290 problems make up`frontiermath-2025-02-28-private`.
Similarly, we have made 2 problems from Tier 4 public, calling this`frontiermath-tier-4-2025-07-01-public`, while the remaining 48 problems make   ...    FrontierMath was developed with funding from
OpenAI, who has exclusive access to a subset of the benchmark. See our   ...    For FrontierMath, we recommend using the log viewer on the public questions as the best way to understand the   ...
For each FrontierMath question, the model needs to submit a Python function`answer()` that returns the answer. The   ...    - If your answer is correct you will get 1 point. If it is incorrect, or if
you don\u2019t submit an answer, you will get 0   ...    in`frontiermath-2025-02-28-private`). ### Changelog 2026-01-23. We identified issues with two Tier 4 problems that affected prior scores. In
one case the issue was with our grader, so we could re-grade solutions given by models on prior runs. The models that got this problem right were: GPT-5.2 Pro, GPT-5.2 (xhigh), GPT-5.2 (high), GPT-5.2
(medium), and GPT-5 Pro. In the other case the issue was with the problem statement itself. Here we re-ran every model that had scored over 10% on Tier 4 on this one problem. Only GPT-5.2 Pro and
GPT-5.2 (high) got the corrected problem right. We adjusted the scores of all of these models   ...    We also fixed an error in the problem statement for public problem`PLD1`
in`FrontierMath-2025-02-28-Public`. Several models had in fact been getting the right answer to the mis-stated problem (the answer was 281718171540). Since this problem set is just for illustrative
purposes, we have not updated those scores on our hub. We bumped the benchmark version number to 1.1.4 to reflect these fixes. 2026-01-22. We upgraded our Inspect dependency, and bumped the benchmark
version number to 1.1.3.   ...    We ran this model on Fireworks for data security. We found that, when run on public benchmarks, the model performed   ...    until they completed. This accounts for
the larger standard error associated with this model\u2019s score. Gemini 2.5 Pro and Gemini 3 Pro We encountered an unusual number of API errors when trying to benchmark these models in a timely
manner after their   ...    failed, we marked the sample as incorrect. An earlier version of this site included`gemini-2.5.-pro` in this table, but   ...    The table below shows how many samples were
marked as incorrect in this way. | Model | Benchmark | Accuracy | Samples marked as incorrect after retries |\n| --- | --- | --- | --- | | gemini-2.5-pro-preview-06-05 |
FrontierMath-2025-02-28-Private | 10% (\u00b12%) | 21/290 = 7% | | gemini-3-pro-preview | FrontierMath-2025-02-28-Private | 38% (\u00b13%) | 10/290=3% | | gemini-3-pro-preview | FrontierMath-
Tier-4-2025-02-28-Private | 19% (\u00b16%) | 3/48=6% | Grok 4\n\nFor`grok-4-0709`, we experienced timeouts and network errors using the API in July 2025. As a result, as of July 2025, we evaluated
Grok 4 using specific scoring rules: FrontierMath-2025-02-28-Private was evaluated using our standard settings. The record ID is gda5UeWrA8HcbDCRuLJ56H. We used the streaming API. 1/290 was not scored
due to the server not sending any response. (We allow up to 1% of samples   ...    For FrontierMath-Tier-4-2025-07-01-Private, we used a maximum output length per request of 128,000 tokens (default is
...    | Benchmark | Accuracy | Samples with API errors | Run ID |\n| --- | --- | --- | --- | | FrontierMath-Tier-4-2025-07-01-Private | 2% (\u00b12%) | 8 out of 48 (16%) | QxtNUmV2L34UyrySmBLTbv |
...    The code"], "published_date": null, "score": null}, {"title": "50% \u043d\u0430 FrontierMath: GPT-5.4 \u0431\u0435\u0440\u0451\u0442 \u0440\u0443\u0431\u0435\u0436,
\u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043a\u0430\u0437\u0430\u043b\u0441\u044f \u043d\u0435\u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u044b\u043c | AI-Stat", "url": "https://www.ai-
stat.ru/news/2026-03-12-gpt54-frontiermath", "snippet": "50% \u043d\u0430 FrontierMath: GPT-5.4 \u0431\u0435\u0440\u0451\u0442 \u0440\u0443\u0431\u0435\u0436,
\u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043a\u0430\u0437\u0430\u043b\u0441\u044f \u043d\u0435\u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u044b\u043c | AI-Stat\n\n###
\u041e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 GPT-5 \u0438 \u0434\u0440\u0443\u0433\u0438\u0435
\u043d\u0435\u0439\u0440\u043e\u0441\u0435\u0442\u0438\n\n\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439 \u043d\u0430 Aijora.ru \u2014 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442
\u0431\u0435\u0437 VPN \u0438 \u0437\u0430\u0440\u0443\u0431\u0435\u0436\u043d\u044b\u0445 \u043a\u0430\u0440\u0442\n\n\u041f\u043e\u043f\u0440\u043e\u0431\u043e\u0432\u0430\u0442\u044c
\u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\n\n### GPT-5 \u0431\u0435\u0437 VPN\n\nAijora.ru \u2014 \u0431\u0435\u0437
\u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439\n\n\u041f\u043e\u043f\u0440\u043e\u0431\u043e\u0432\u0430\u0442\u044c
\u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\n\n\u0412\u0441\u0435
\u043d\u043e\u0432\u043e\u0441\u0442\u0438\n\nopenaigpt-5.4\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430\u0431\u0435\u043d\u0447\u043c\u0430\u0440\u043a\u0438frontiermathepoch-ai\n\n#
50% \u043d\u0430 FrontierMath: GPT-5.4 \u0431\u0435\u0440\u0451\u0442 \u0440\u0443\u0431\u0435\u0436, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043a\u0430\u0437\u0430\u043b\u0441\u044f
\u043d\u0435\u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u044b\u043c\n\nGPT-5.4 Pro \u043d\u0430\u0431\u0440\u0430\u043b 50% \u043d\u0430 \u0442\u0438\u0440\u0430\u0445 1\u20133 \u0438 38%
\u043d\u0430 \u0422\u0438\u0440\u0435 4 \u0431\u0435\u043d\u0447\u043c\u0430\u0440\u043a\u0430 FrontierMath \u2014 \u043f\u0435\u0440", "highlights": ["50% \u043d\u0430 FrontierMath: GPT-5.4
\u0431\u0435\u0440\u0451\u0442 \u0440\u0443\u0431\u0435\u0436, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043a\u0430\u0437\u0430\u043b\u0441\u044f
\u043d\u0435\u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u044b\u043c | AI-Stat   ...    # 50% \u043d\u0430 FrontierMath: GPT-5.4 \u0431\u0435\u0440\u0451\u0442 \u0440\u0443\u0431\u0435\u0436,
\u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043a\u0430\u0437\u0430\u043b\u0441\u044f \u043d\u0435\u0434\u043e\u0441\u0442\u0438\u0436\u0438\u043c\u044b\u043c GPT-5.4 Pro
\u043d\u0430\u0431\u0440\u0430\u043b 50% \u043d\u0430 \u0442\u0438\u0440\u0430\u0445 1\u20133 \u0438 38% \u043d\u0430 \u0422\u0438\u0440\u0435 4 \u0431\u0435\u043d\u0447\u043c\u0430\u0440\u043a\u0430
FrontierMath \u2014 \u043f\u0435\u0440\u0432\u0430\u044f \u043f\u043e\u0431\u0435\u0434\u0430 AI \u043d\u0430\u0434 \u0437\u0430\u0434\u0430\u0447\u0430\u043c\u0438
\u0443\u0440\u043e\u0432\u043d\u044f   ...    \u0412\u043b\u0430\u0434 \u041c\u0430\u043a\u0430\u0440\u043e\u0432\u043f\u0440\u043e\u0432\u0435\u0440\u0438\u043b \u0438
\u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043b\n\n12 \u043c\u0430\u0440\u0442\u0430 2026 \u0433.\n\n8 \u043c\u0438\u043d \u0447\u0442\u0435\u043d\u0438\u044f \u0412
\u043a\u043e\u043d\u0446\u0435 2024 \u0433\u043e\u0434\u0430 Epoch AI \u0432\u044b\u043f\u0443\u0441\u0442\u0438\u043b\u0438 \u0431\u0435\u043d\u0447\u043c\u0430\u0440\u043a FrontierMath \u0438
\u043f\u0440\u043e\u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043b\u0438 \u043d\u0430 \u043d\u0451\u043c \u0432\u0441\u0435 \u0444\u043b\u0430\u0433\u043c\u0430\u043d\u044b
\u0442\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u2014 GPT-4o, o1, Claude 3.5 Sonnet, Gemini 1.5 Pro. \u041d\u0438 \u043e\u0434\u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u044c
\u043d\u0435 \u043f\u0440\u0435\u043e\u0434\u043e\u043b\u0435\u043b\u0430 2%. \u042d\u0442\u043e \u0431\u044b\u043b
\u043d\u0435\u0434\u0432\u0443\u0441\u043c\u044b\u0441\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u0433\u043d\u0430\u043b: \u0432\u044b\u0441\u0448\u0430\u044f
\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u043f\u043e\u043a\u0430 \u043d\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0430 \u0434\u043b\u044f \u043c\u0430\u0448\u0438\u043d.
\u041f\u043e\u043b\u0442\u043e\u0440\u0430 \u0433\u043e\u0434\u0430 \u0441\u043f\u0443\u0441\u0442\u044f GPT-5.4 \u043d\u0430\u0431\u0438\u0440\u0430\u0435\u0442 50%.   ...    FrontierMath \u2014
\u043d\u0435 \u043e\u0447\u0435\u0440\u0435\u0434\u043d\u043e\u0439 \u0442\u0435\u0441\u0442 \u043d\u0430 \"\u043e\u0431\u0449\u0438\u0435 \u0437\u043d\u0430\u043d\u0438\u044f\". \u042d\u0442\u043e
\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0441\u043e\u0442\u0435\u043d \u043e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0445, \u0440\u0430\u043d\u0435\u0435
\u043d\u0438\u0433\u0434\u0435 \u043d\u0435 \u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0432\u0448\u0438\u0445\u0441\u044f   ...    \u0411\u0435\u043d\u0447\u043c\u0430\u0440\u043a
\u0440\u0430\u0437\u0434\u0435\u043b\u0451\u043d \u043d\u0430 \u0443\u0440\u043e\u0432\u043d\u0438. \u0422\u0438\u0440\u044b 1\u20133 \u2014 \u043e\u0442 \u0443\u0440\u043e\u0432\u043d\u044f
\u0445\u043e\u0440\u043e\u0448\u0435\u0433\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430 \u0434\u043e \u0440\u0430\u043d\u043d\u0435\u0439
\u043f\u043e\u0441\u0442\u0434\u043e\u043a\u0442\u043e\u0440\u0430\u043d\u0442\u0443\u0440\u044b. \u0422\u0438\u0440 4 \u2014
\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430:
\u0442\u0438\u043f\u0438\u0447\u043d\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430 \u0437\u0430\u043d\u0438\u043c\u0430\u0435\u0442 \u0443
\u043f\u0440\u043e\u0444\u0435\u0441\u0441\u043e\u0440\u0430 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441\u043e\u0432 \u0438\u043b\u0438
\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0434\u043d\u0435\u0439 \u0440\u0430\u0431\u043e\u0442\u044b.   ...    ## \u041e\u0442 2% \u043a 50%: \u043a\u0430\u043a
\u043c\u0435\u043d\u044f\u043b\u0441\u044f \u0440\u0435\u043a\u043e\u0440\u0434 \u0414\u0432\u0430 \u0433\u043e\u0434\u0430 \u043f\u043e\u043d\u0430\u0434\u043e\u0431\u0438\u043b\u043e\u0441\u044c,
\u0447\u0442\u043e\u0431\u044b \u043f\u0440\u043e\u0439\u0442\u0438 \u043e\u0442 \u043f\u043e\u043b\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0432\u0430\u043b\u0430 \u0434\u043e
\u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u0437\u0430\u0434\u0430\u0447 \u0443\u0440\u043e\u0432\u043d\u044f \u043f\u043e\u0441\u0442\u0434\u043e\u043a\u0430.
\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0431\u044b\u043b \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u044b\u043c: | \u041c\u043e\u0434\u0435\u043b\u044c | \u0422\u0438\u0440 1\u20133 |
\u0422\u0438\u0440 4 |\n| --- | --- | --- |\n| GPT-4o, o1, Claude 3.5 Sonnet (\u043a\u043e\u043d\u0435\u0446 2024) | \u043c\u0435\u043d\u0435\u0435 2% | \u043c\u0435\u043d\u0435\u0435 2% | | o3
(\u043d\u0430\u0447\u0430\u043b\u043e 2025) | ~25% | \u2014 |\n| Gemini 3 Pro (\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u0440\u0435\u043a\u043e\u0440\u0434) | \u2014 | 19% |\n|
GPT-5.2 Pro | >40% | 31% | | GPT-5.4 Pro | 50% | 38% | GPT-5.4 Pro \u0431\u044b\u043b \u043e\u0446\u0435\u043d\u0451\u043d \u043a\u043e\u043c\u0430\u043d\u0434\u043e\u0439 Epoch AI \u0434\u043e
\u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u0440\u0435\u043b\u0438\u0437\u0430 5 \u043c\u0430\u0440\u0442\u0430 2026 \u0433\u043e\u0434\u0430. \u041f\u043e
\u0442\u0438\u0440\u0430\u043c 1\u20133 \u043c\u043e\u0434\u0435\u043b\u044c \u043d\u0430\u0431\u0440\u0430\u043b\u0430 52% \u043d\u0430 \u043e\u0431\u044b\u0447\u043d\u043e\u043c
\u043d\u0430\u0431\u043e\u0440\u0435 \u0438 42% \u043d\u0430 \u0437\u0430\u043a\u0440\u044b\u0442\u043e\u043c (held-out) \u2014 \u0442\u043e\u043c, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 OpenAI
\u043d\u0435 \u0432\u0438\u0434\u0438\u0442 \u043f\u0440\u0438 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0438. \u041d\u0435\u0431\u043e\u043b\u044c\u0448\u043e\u0439
\u0440\u0430\u0437\u0440\u044b\u0432 \u043c\u0435\u0436\u0434\u0443 \u0434\u0432\u0443\u043c\u044f \u043d\u0430\u0431\u043e\u0440\u0430\u043c\u0438 \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u043e
\u0442\u043e\u043c, \u0447\u0442\u043e \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0435\u043b\u044c\u0437\u044f \u0441\u043f\u0438\u0441\u0430\u0442\u044c \u043d\u0430
\"\u0437\u0430\u0443\u0447\u0438\u0432\u0430\u043d\u0438\u0435\". \u041d\u0430 \u0422\u0438\u0440\u0435 4 \u043a\u0430\u0440\u0442\u0438\u043d\u0430
\u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u0435\u0435: 25% \u043d\u0430 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u043d\u0430\u0431\u043e\u0440\u0435 \u0438
\u043d\u0435\u043e\u0436\u0438\u0434\u0430\u043d\u043d\u043e \u0432\u044b\u0441\u043e\u043a\u0438\u0435 55% \u043d\u0430 \u0437\u0430\u043a\u0440\u044b\u0442\u043e\u043c. \u041f\u043e
\u0434\u0435\u0441\u044f\u0442\u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u043c (Pass@10) \u0422\u0438\u0440
4 \u0434\u0430\u043b \u0432 \u0441\u0440\u0435\u0434\u043d\u0435\u043c 38%. ## \u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432 \u0441 \u043f\u0440\u0435\u043f\u0440\u0438\u043d\u0442\u043e\u043c
\u041e\u0434\u0438\u043d \u0438\u0437 \u0440\u0435\u0448\u0451\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447 \u0422\u0438\u0440\u0430 4 \u0440\u0430\u0441\u043a\u0440\u044b\u043b
\u043d\u0435\u043e\u0436\u0438\u0434\u0430\u043d\u043d\u0443\u044e \u0434\u0435\u0442\u0430\u043b\u044c \u043e \u043f\u0440\u0438\u0440\u043e\u0434\u0435 GPT-5.4. \u041c\u043e\u0434\u0435\u043b\u044c
\u043d\u0430\u0448\u043b\u0430 \u043f\u0440\u0435\u043f\u0440\u0438\u043d\u0442 2011 \u0433\u043e\u0434\u0430 \u2014   ...    \u0412 \u0444\u0435\u0432\u0440\u0430\u043b\u0435 2026
\u0433\u043e\u0434\u0430 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442 \u043d\u0430 1stproof.org
\u043f\u043e\u043a\u0430\u0437\u0430\u043b, \u0447\u0442\u043e \u0432\u0435\u0434\u0443\u0449\u0438\u0435 AI-\u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0440\u0435\u0448\u0430\u044e\u0442 5
\u0438\u0437 10 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0445 \u043d\u0435\u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u043b\u0435\u043c\u043c
\u043e\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u043e\u0432.
\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e
\u043e\u0442\u0440\u0435\u0430\u0433\u0438\u0440\u043e\u0432\u0430\u043b\u043e \"\u0441\u043c\u0435\u0441\u044c\u044e \u0432\u043e\u0441\u0445\u0438\u0449\u0435\u043d\u0438\u044f \u0438   ...
\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0440\u0443\u0431\u0435\u0436 \u2014"], "published_date": "2026-03-12T09:00:00.000", "score": null}, {"title": "Data on AI Capabilities and
Benchmarking | Epoch AI", "url": "http://epochai.org/benchmarks", "snippet": "Data on AI Capabilities and Benchmarking | Epoch AI\n\nUpdated Apr. 12, 2026\n\n# AI Capabilities\n\nOur database of
benchmark results, featuring the performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI as well as data collected from external
sources. Explore trends in AI capabilities across time, by benchmark, or by model.\n\nEpoch Capabilities IndexIndividual Benchmarks\n\nSettings\n\nFrontier trend only\n\nExplore
by\n\nNone\n\nCountry\n\nOrg", "highlights": ["Data on AI Capabilities and Benchmarking | Epoch AI\n\nUpdated Apr. 12, 2026\n\n# AI Capabilities Our database of benchmark results, featuring the
performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI as well as data collected from external sources. Explore trends in AI
capabilities across time, by benchmark, or by model. Epoch Capabilities IndexIndividual Benchmarks\n\nSettings\n\nFrontier trend only\n\nExplore by\n\nNone\n\nCountry\n\nOrganization   ...    - All\n-
Mathematics\n- Agent\n- Software engineering\n- Games\n- World knowledge\n- Science\n- Long context - Writing & creativity\n- Multimodal Show benchmarks (4)\u00d7 Clear\n\n#### Epoch AI\u2013run
benchmarks\n\nFrontierMath Tier 4\n\nFrontierMath Tiers 1-3 SWE-bench Verified\n\nChess Puzzles\n\nSimpleQA Verified\n\nGPQA Diamond\n\nOTIS Mock AIME 2024-2025\n\nMATH Level 5 #### Benchmark
creator\u2013run benchmarks\n\nSWE-bench (Bash Only)\n\nAider Polyglot\n\nWeirdML (v2)\n\nSimpleBench\n\nGDPval Terminal-Bench
2.0\n\nPostTrainBench\n\nBALROG\n\nGSO\n\nFiction.liveBench\n\nVPCT\n\nVideo-MME\n\nARC-AGI-1\n\nAPEX-Agents\n\nARC-AGI-2 Humanity's Last Exam\n\n#### Model developer\u2013run
benchmarks\n\nAdversarial NLI\n\nARC AI2\n\nBBH\n\nBoolQ\n\nCadEval CommonSenseQA 2\n\nCybench\n\nGSM8K\n\nHellaSwag\n\nLAMBADA\n\nLiveBench\n\nMMLU\n\nOpenBookQA\n\nOS
World\n\nPIQA\n\nScienceQA\n\nSuperGLUE The Agent Company\n\nTriviaQA\n\nWinoGrande\n\nApply\n\n## Benchmarking updates\n\nMar. 9, 2026 We added APEX-Agents, ARC-AGI-2, and HLE to the Epoch
Capabilities Index. GPT-5.4 Pro now leads, narrowly ahead of Gemini 3.1 Pro. See the update\n\nMar. 5, 2026 GPT-5.4 Pro set a new record on FrontierMath, scoring 50% on Tiers 1\u20133 and 38% on Tier
4. We also evaluated it on FrontierMath: Open Problems. Read the thread\n\nJan. 27, 2026 We released FrontierMath: Open Problems, which tests AI on unsolved math research problems.\n\nDiscover the
benchmark # Trusted by leaders at OpenAI, DeepMind, and governments worldwide Need deeper insights? Our team offers custom research and advisory services.\n\nFeedback"], "published_date": null,
"score": null}, {"title": "Data on AI Capabilities and Benchmarking | Epoch AI", "url": "https://epoch.ai/data/ai-benchmarking-dashboard?view=table", "snippet": "Data on AI Capabilities and
Benchmarking | Epoch AI\n\n \n\nUpdated Apr. 3, 2026\n\n# AI Capabilities\n\nOur database of benchmark results, featuring the performance of leading AI models on challenging tasks. It includes results
from benchmarks evaluated internally by Epoch AI as well as data collected from external sources. Explore trends in AI capabilities across time, by benchmark, or by model.\n\nEpoch Capabilities
IndexIndividual Benchmarks\n\nSettings\n\nFrontier trend only\n\nExplore by\n\nNone\n\nCountry\n\nO", "highlights": ["Data on AI Capabilities and Benchmarking | Epoch AI\n\n \n\nUpdated Apr. 3,
2026\n\n# AI Capabilities Our database of benchmark results, featuring the performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI
as well as data collected from external sources. Explore trends in AI capabilities across time, by benchmark, or by model. Epoch Capabilities IndexIndividual Benchmarks\n\nSettings\n\nFrontier trend
only\n\nExplore by\n\nNone\n\nCountry\n\nOrganization   ...    - All\n- Mathematics\n- Agent\n- Software engineering\n- Games\n- World knowledge\n- Science\n- Long context - Writing & creativity\n-
Multimodal Show benchmarks (4)\u00d7 Clear\n\n#### Epoch AI\u2013run benchmarks\n\nFrontierMath Tier 4\n\nFrontierMath Tiers 1-3 SWE-bench Verified\n\nChess Puzzles\n\nSimpleQA Verified\n\nGPQA
Diamond\n\nOTIS Mock AIME 2024-2025\n\nMATH Level 5 #### Benchmark creator\u2013run benchmarks\n\nSWE-bench (Bash Only)\n\nAider Polyglot\n\nWeirdML (v2)\n\nSimpleBench\n\nGDPval Terminal-Bench
2.0\n\nPostTrainBench\n\nBALROG\n\nGSO\n\nFiction.liveBench\n\nVPCT\n\nVideo-MME\n\nARC-AGI-1\n\nAPEX-Agents\n\nARC-AGI-2 Humanity's Last Exam\n\n#### Model developer\u2013run
benchmarks\n\nAdversarial NLI\n\nARC AI2\n\nBBH\n\nBoolQ\n\nCadEval CommonSenseQA 2\n\nCybench\n\nGSM8K\n\nHellaSwag\n\nLAMBADA\n\nLiveBench\n\nMMLU\n\nOpenBookQA\n\nOS
World\n\nPIQA\n\nScienceQA\n\nSuperGLUE The Agent Company\n\nTriviaQA\n\nWinoGrande\n\nApply\n\n \n\n## Benchmarking updates\n\nMar. 9, 2026 We added APEX-Agents, ARC-AGI-2, and HLE to the Epoch
Capabilities Index. GPT-5.4 Pro now leads, narrowly ahead of Gemini 3.1 Pro. See the update\n\nMar. 5, 2026 GPT-5.4 Pro set a new record on FrontierMath, scoring 50% on Tiers 1\u20133 and 38% on Tier
4. We also evaluated it on FrontierMath: Open Problems. Read the thread\n\nJan. 27, 2026 We released FrontierMath: Open Problems, which tests AI on unsolved math research problems.\n\nDiscover the
benchmark # Trusted by leaders at OpenAI, DeepMind, and governments worldwide Need deeper insights? Our team offers custom research and advisory services.\n\nBook"], "published_date": null, "score":
null}, {"title": "Data on AI Capabilities and Benchmarking | Epoch AI", "url": "http://www.epoch.ai/benchmarks", "snippet": "Data on AI Capabilities and Benchmarking | Epoch AI\n\nUpdated Mar. 21,
2026\n\n# AI Capabilities\n\nOur database of benchmark results, featuring the performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch
AI as well as data collected from external sources. Explore trends in AI capabilities across time, by benchmark, or by model.\n\nEpoch Capabilities IndexIndividual Benchmarks\n\nSettings\n\nFrontier
trend only\n\nExplore by\n\nNone\n\nCountry\n\nOrg", "highlights": ["Data on AI Capabilities and Benchmarking | Epoch AI\n\nUpdated Mar. 21, 2026\n\n# AI Capabilities Our database of benchmark
results, featuring the performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI as well as data collected from external sources.
Explore trends in AI capabilities across time, by benchmark, or by model. Epoch Capabilities IndexIndividual Benchmarks\n\nSettings\n\nFrontier trend only\n\nExplore
by\n\nNone\n\nCountry\n\nOrganization   ...    - All\n- Mathematics\n- Agent\n- Software engineering\n- Games\n- World knowledge\n- Science\n- Long context - Writing & creativity\n- Multimodal Show
benchmarks (4)\u00d7 Clear\n\n#### Epoch AI\u2013run benchmarks\n\nFrontierMath Tier 4\n\nFrontierMath Tiers 1-3 SWE-bench Verified\n\nChess Puzzles\n\nSimpleQA Verified\n\nGPQA Diamond\n\nOTIS Mock
AIME 2024-2025\n\nMATH Level 5 #### Benchmark creator\u2013run benchmarks\n\nSWE-bench (Bash Only)\n\nAider Polyglot\n\nWeirdML (v2)\n\nSimpleBench\n\nGDPval Terminal-Bench
2.0\n\nPostTrainBench\n\nBALROG\n\nGSO\n\nFiction.liveBench\n\nVPCT\n\nVideo-MME\n\nARC-AGI-1\n\nAPEX-Agents\n\nARC-AGI-2 Humanity's Last Exam\n\n#### Model developer\u2013run
benchmarks\n\nAdversarial NLI\n\nARC AI2\n\nBBH\n\nBoolQ\n\nCadEval CommonSenseQA 2\n\nCybench\n\nGSM8K\n\nHellaSwag\n\nLAMBADA\n\nLiveBench\n\nMMLU\n\nOpenBookQA\n\nOS
World\n\nPIQA\n\nScienceQA\n\nSuperGLUE The Agent Company\n\nTriviaQA\n\nWinoGrande\n\nApply\n\n## Benchmarking updates\n\nMar. 9, 2026 We added APEX-Agents, ARC-AGI-2, and HLE to the Epoch
Capabilities Index. GPT-5.4 Pro now leads, narrowly ahead of Gemini 3.1 Pro. See the update\n\nMar. 5, 2026 GPT-5.4 Pro set a new record on FrontierMath, scoring 50% on Tiers 1\u20133 and 38% on Tier
4. We also evaluated it on FrontierMath: Open Problems. Read the thread\n\nJan. 27, 2026 We released FrontierMath: Open Problems, which tests AI on unsolved math research problems.\n\n Discover the
benchmark # Trusted by leaders at OpenAI, DeepMind, and governments worldwide Need deeper insights? Our team offers custom research and advisory services.\n\nBook"], "published_date": null, "score":
null}, {"title": "OpenAI Just Hit a Major Milestone in Research-Grade Mathematics \u2014 The Specialty News", "url": "https://thespecialtynews.com/article/gpt-54-pro-conquers-frontier-math-benchmark",
"snippet": "OpenAI Just Hit a Major Milestone in Research-Grade Mathematics \u2014 The Specialty News\n\nAI\n\n# OpenAI Just Hit a Major Milestone in Research-Grade Mathematics\n\nGPT-5.4 Pro's
performance on the FrontierMath benchmark signals a new era for AI as a legitimate research collaborator.\n\nMarch 6, 2026 at 8:29 AM\u00b75 min read\n\nFor years, AI performance in mathematics felt
like a talented high schooler\u2014great at competitions, but lost when facing the deep, uncharted territory of original research. That ceiling ", "highlights": ["OpenAI Just Hit a Major Milestone in
Research-Grade Mathematics \u2014 The Specialty News\n\nAI # OpenAI Just Hit a Major Milestone in Research-Grade Mathematics GPT-5.4 Pro's performance on the FrontierMath benchmark signals a new era
for AI as a legitimate research collaborator. March 6, 2026 at 8:29 AM\u00b75 min read For years, AI performance in mathematics felt like a talented high schooler\u2014great at competitions, but lost
when facing the deep, uncharted territory of original research. That ceiling has officially been cracked. OpenAI\u2019s newly released GPT-5.4 Pro just achieved a staggering 38% success rate on
FrontierMath, a brutal benchmark designed to test AI against problems that even human experts spend weeks solving.   ...    The true significance of this leap lies in the nature of the FrontierMath
suite. Developed by Epoch AI with input from mathematicians, the collection is comprised of 350 original, unpublished problems. Unlike standard academic tests that an AI might have 'seen' during its
training, these questions are designed to be impossible to Google. Success here cannot be explained away by rote memorization; it demands genuine mathematical reasoning. In Tier 4, the most grueling
category, GPT-5.4 Pro outperformed its predecessors by an order of magnitude. Just a year ago, the best models hovered around 2% accuracy. The fact that OpenAI\u2019s latest can navigate this
complexity suggests the model is developing a kind of mathematical 'taste'\u2014the ability to identify which paths to explore and which to abandon, mirroring the intuition of a human researcher. One
particularly telling moment occurred when the model solved a Tier 4 problem by unearthing an obscure 2011 preprint. By synthesizing this rarely-accessed literature, the AI bypassed the standard,
labor-intensive proof path, demonstrating a capacity to cross-reference vast stores of knowledge in ways that could eventually accelerate   ...    We are witnessing a shift similar to the evolution of
chess engines. Just as AlphaZero moved from merely following   ...    a calculator to a creative partner. While a 38% score on research-level problems is far from perfect, it marks the boundary where
the machine stops being a library of facts and starts acting as an exploratory tool. This creates a massive opportunity for the scientific community. Epoch AI also included 'Open Problems' in the
benchmark\u2014queries that remain unsolved by human mathematicians. While GPT-5.4 Pro hasn't cracked these yet, it has already begun generating novel observations, effectively serving as an tireless
research assistant that never tires of searching for the next breakthrough. The race is now on to see if these models can move from solving known unknowns to   ...    Photo: ASIA CULTURECENTER /
Unsplash\n\n## GPT-5.4 and Mathematical Reasoning\n\nOpen in Excalidraw\n\n## Keep reading   ...    AIInside the Quiet Exodus That Shook Alibaba\u2019s AI EmpireWhen the lead architects behind one of
the world's most   ...    innovation in the era of corporate consolidation.March 5, 2026 at 8:56 PM   ...    AIWhy AI Can Still Be Trusted to Think Out LoudOpenAI's latest evaluation of GPT-5.4
Thinking reveals that even as AI   ...    monitoring.March 5, 2026 at 8:46 PM ### OpenAI Unveils GPT-5.4 As The New Standard For Agentic Reasoning AIOpenAI Unveils GPT-5.4 As The New Standard For
Agentic ReasoningOpenAI\u2019s new flagship model isn't just better at   ...    expert-level precision.March 5, 2"], "published_date": "2026-03-06T08:29:30.000", "score": null}, {"title": "GPT-5.4 Pro
- Epoch AI", "url": "https://epoch.ai/models/gpt-5-4-pro", "snippet": "GPT-5.4 Pro | Epoch AI\n\n# GPT-5.4 Pro\n\nOpenAI\n\n2026-03-05\n\nClosed weights\n\nRank: 1/164157Epoch Capabilities
Index\n\nAbout ECI 90% CI: 154-161\n\nReasoning\n\nBest score across settings\n\n- Best score across settings\n- GPT-5.4 Pro (xhigh)\n- GPT-5.4 Pro (web)\n- GPT-5.4 Pro\n\nGPT-5.4 Pro
performance\n\nTop performing model\n\nFeedback", "highlights": ["GPT-5.4 Pro | Epoch AI\n\n# GPT-5.4 Pro\n\nOpenAI\n\n2026-03-05\n\nClosed weights\n\nRank: 1/164157Epoch Capabilities Index About ECI
90% CI: 154-161\n\nReasoning\n\nBest score across settings - Best score across settings\n- GPT-5.4 Pro (xhigh)\n- GPT-5.4 Pro (web)\n- GPT-5.4 Pro\n\nGPT-5.4 Pro performance Top performing
model\n\nFeedback"], "published_date": null, "score": null}]
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "advanced_search_expression": "FrontierMath Tier 4 GPT-5.4 from:EpochAIResearch"
}
```

### 📋 Result

```
Error calling tool 'search_x_twitter': APIError: 403015 - You've reached your maximum billable overage limit for 'requests'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

```json
{
  "query": "GPT-5.4 Pro FrontierMath Tier 4 score March 2026"
}
```

### 📋 Result

```
{"query": "GPT-5.4 Pro FrontierMath Tier 4 score March 2026", "results": [{"title": "GPT-5.4 Pro Cracks Open Math Problem", "url": "https://winbuzzer.com/2026/03/24/gpt-54-pro-solves-open-math-
problem-epoch-ai-frontiermath-xcxwbn/", "snippet": "- Breakthrough: OpenAI\u2019s GPT-5.4 Pro solved an open mathematical problem that had resisted human efforts since 2019, verified independently by
Epoch AI.\n- Broader Capability: Three other frontier AI models from Anthropic, Google, and OpenAI also solved the same problem, suggesting shared mathematical reasoning capacity.\n- Benchmark
Progress: FrontierMath scores jumped from 5% under GPT-4 in 2024 to 50% under GPT-5.4 Pro in March 2026.\n- Expert Reaction: Mathematicians remain divided, with Terenc", "api_data": null, "hint":
null}, {"title": "FrontierMath Tier 4 | Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath", "snippet": "[FrontierMath](https://epoch.ai/frontiermath) is a benchmark of hundreds of original,
exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics \u2013 from computationally intensive problems
in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of effort from a researcher in the relevant branch
of mathematics, a", "api_data": null, "hint": null}, {"title": "New record on FrontierMath Tier 4 - Epoch AI - Substack", "url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4",
"snippet": "New record on FrontierMath Tier 4\nGPT-5.2 Pro (manual run) scored 31%, a substantial jump over the previous high score of 19%.\nWe evaluated GPT-5.2 Pro manually on the ChatGPT website.
We did this after encountering timeout issues with the API in our scaffold. We\u2019re working to resolve these issues, but a manual evaluation seemed worthwhile in the meantime.\nPrior to this run,
13 problems from Tier 4 had been solved by any model ever. GPT-5.2 Pro solved 11 of those, and 4 more besides. Its total f", "api_data": null, "hint": null}, {"title": "FrontierMath Benchmark 2026: 1
LLM scores | BenchLM.ai", "url": "https://benchlm.ai/benchmarks/frontierMath", "snippet": "An expert-level mathematical reasoning benchmark by Epoch AI featuring original, research-level problems
created by mathematicians including IMO gold medalists and Fields Medal recipients. Problems require deep creativity and multi-step reasoning.\nAs of April 10, 2026, [GPT-5.4
Pro](https://benchlm.ai/models/gpt-5-4-pro) leads the FrontierMath leaderboard with 50%.\nYear\n2024\nTasks\n350 original research-level math problems\nFormat\nOpen-ended mathematical reasoning with
tool access\nDifficulty\nResea", "api_data": null, "hint": null}, {"title": "GPT-5 Pro Edges Ahead in FrontierMath Tier 4 Test, But Marginally | by AI Engineering | Medium", "url": "https://ai-
engineering-trend.medium.com/gpt-5-pro-edges-ahead-in-frontiermath-tier-4-test-but-marginally-a0421f879f11", "snippet": null, "api_data": null, "hint": null}, {"title": "New record on FrontierMath
Tier 4: GPT-5.2 Pro scored 31 ...", "url": "https://www.facebook.com/xixidu/posts/new-record-on-frontiermath-tier-4-gpt-52-pro-scored-316-months-ago-the-max-was-6/10173642681150637/", "snippet": null,
"api_data": null, "hint": null}, {"title": "Data on AI Capabilities and Benchmarking | Epoch AI", "url": "https://epoch.ai/benchmarks/", "snippet": "Our database of benchmark results, featuring the
performance of leading AI models on challenging tasks. It includes results from benchmarks evaluated internally by Epoch AI as well as data collected from external sources. Explore trends in AI
capabilities across time, by benchmark, or by model.\nWe added APEX-Agents, ARC-AGI-2, and HLE to the Epoch Capabilities Index. GPT-5.4 Pro now leads, narrowly ahead of Gemini 3.1 Pro.\nGPT-5.4 Pro
set a new record on FrontierMath, scoring 50% on Tiers 1\u20133 an", "api_data": null, "hint": null}, {"title": "Epoch AI on X: \"GPT-5.4 set a new record on FrontierMath, our benchmark of extremely
challenging math problems! We had pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%. See thread for commentary and additional experiments.
https://t.co/u0JnYOjrLO\" / X", "url": "https://x.com/EpochAIResearch/status/2029626255776395425", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript
or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info
\u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "What will be the best FrontierMath Tier 4 score by Dec 31, 2026? | Manifold", "url": "https://manifold.markets/Bayesian/what-will-be-
the-best-frontiermath", "snippet": "This market matches [Mathematics: FrontierMath Tier 4](https://forecast2026.ai/)[ from the AI 2026 Forecasting Survey by AI Digest](https://forecast2026.ai/).\nSee
other manifold questions [here](https://manifold.markets/topic/2026-ai-forecasting-survey-by-ai-di)\n![](https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-
images%2Fdefault%2F8lqPqzZzLn.png?alt=media&token=4e32a80f-b6fe-4c54-afd8-0532c22a4fd8)\nResolution criteria\nResolves to the highest reported accuracy on Fr", "api_data": null, "hint": "Use
manifold_price for market data, or manifold_history for historical prices."}, {"title": "GPT 5.4 Complete Guide 2026: Features, Pricing, Benchmarks & How to Use | NxCode", "url":
"https://www.nxcode.io/resources/news/gpt-5-4-complete-guide-features-pricing-models-2026", "snippet": "[Start Free](https://studio.nxcode.io?ref=article_top_gpt-5-4-complete-guide-features-pricing-
models-2026)\nKey Takeaways\n- OpenAI's most capable model ever: GPT 5.4 scores 57.7% on SWE-bench Pro, 75% on OSWorld (surpassing the 72.4% human expert baseline), and 83% on GDPval knowledge work --
all in one unified model.\n- Five variants for every workload: Standard ($2.50/$15 per MTok), Thinking (interactive reasoning), Pro ($30/$180 per MTok), Mini (~$0.40/$1.60), and Nano (edge/embedded)
cover eve", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Now I have a clear picture. Let me synthesize the key facts:

1. **Current record on FrontierMath Tier 4**: GPT-5.4 Pro scored **38%** (as of March 5, 2026)
2. **The question asks**: Will any model score **≥40.0%** before May 1, 2026?
3. **The question was published**: April 12, 2026 (today)
4. **Scheduled close**: April 12, 2026 at 15:00 UTC (today!)
5. **Resolution**: May 1, 2026


6. **Tier 4 benchmark details**: 48 private problems out of 50 total, with 42% of them solved at least once across all runs ever

The current best performance is 38% across multiple configurations, so the critical question is whether any model can gain those 2+ percentage points in the remaining time before the deadline. I'm trying to reconcile the different reported scores for GPT-5.4 Pro on Tier 4. The Epoch AI post says 38%, but the Russian article mentions 25% on non-held-out problems and 55% on held-out ones, with an average of 38% across ten runs. Let me work through what these numbers actually represent given that Tier 4 has 48 total problems split between held-out and non-held-out sets.

If 25% of the non-held-out problems and 55% of the held-out problems were solved, that gives me roughly 18 correct answers out of 48, which rounds to 37.5% or approximately 38%. Now I need to figure out what score is actually required to resolve this question—the criteria specify 40.0% or higher, which on 48 problems means at least 20 correct answers to reach 41.67%.

Currently GPT-5.4 Pro is at 18/48 (37.5%), and even with pass@10 scoring across multiple runs, no single model has broken 40% yet. The best collective performance across all models ever tested is 42%, meaning 20 problems have been solved by *some* model at *some* point, but not by one model in one run. For the question to resolve YES by May 1, 2026, either a new model or a new version would need to solve at least two more problems than GPT-5.4 Pro managed.

The timeline is extremely tight—only about 19 days remain, and Epoch AI would need pre-release access or time to run evaluations after a model drops. I'm checking whether any new models are expected in this window or if anything's been evaluated since early March.

## 💬 Response

Now let me check for any very recent model releases or evaluations that might have happened since the March 5 GPT-5.4 result, and check prediction markets.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__markets__polymarket_price


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "FrontierMath Tier 4 new model evaluation April 2026"
}
```

### 📋 Result

```
{"query": "FrontierMath Tier 4 new model evaluation April 2026", "results": [{"title": "FrontierMath Tier 4: Battle Royale - Epoch AI - Substack", "url": "https://epochai.substack.com/p/frontiermath-
tier-4-battle-royale", "snippet": "FrontierMath Tier 4: Battle Royale\nGPT-5 Pro set a new record (13%), edging out Gemini 2.5 Deep Think by a single problem (not statistically significant). Grok 4
Heavy lags.\nWe manually evaluated three compute-intensive model settings (GPT-5 Pro, Gemini 2.5 Deep Think, and Grok 4 Heavy) on our extremely hard math benchmark.\nFrontierMath Tier 4 consists of 50
research-level math problems developed by professional mathematicians. These problems can take experts weeks to solve. Below is one of the ", "api_data": null, "hint": null}, {"title": "FrontierMath
Tier 4 | Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath", "snippet": "[FrontierMath](https://epoch.ai/frontiermath) is a benchmark of hundreds of original, exceptionally challenging
mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics \u2013 from computationally intensive problems in number theory and real
analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of effort from a researcher in the relevant branch of mathematics, a",
"api_data": null, "hint": null}, {"title": "FrontierMath Benchmark 2026: 1 LLM scores | BenchLM.ai", "url": "https://benchlm.ai/benchmarks/frontierMath", "snippet": "An expert-level mathematical
reasoning benchmark by Epoch AI featuring original, research-level problems created by mathematicians including IMO gold medalists and Fields Medal recipients. Problems require deep creativity and
multi-step reasoning.\nAs of April 10, 2026, [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) leads the FrontierMath leaderboard with 50%.\nYear\n2024\nTasks\n350 original research-level math
problems\nFormat\nOpen-ended mathematical reasoning with tool access\nDifficulty\nResea", "api_data": null, "hint": null}, {"title": "FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch
AI", "url": "https://epoch.ai/frontiermath/", "snippet": "FrontierMath includes both carefully crafted challenge problems and open research problems that remain unsolved by mathematicians.\nA
benchmark of several hundred unpublished, highly challenging mathematics problems. Difficulty Tiers 1-3 cover undergraduate through early postdoc level problems, while Tier 4 is research-level
mathematics.\nA collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would meaningfully advance the sta", "api_data": null,
"hint": null}, {"title": "Share of FrontierMath problems solved correctly by AI models - Our World in Data", "url": "https://ourworldindata.org/grapher/ai-frontiermath-over-time", "snippet": "Share of
FrontierMath problems solved correctly by AI models\n![](/grapher/ai-frontiermath-over-time.png)\nWhat you should know about this indicator\n- This indicator shows the share of FrontierMath problems
that AI models solve correctly, based on Epoch AI's evaluation.\n- FrontierMath is a set of 350 original math problems written by experts, covering many areas of advanced mathematics. Many problems
are difficult enough that human specialists might need hours or days to solve them.\n- The benchmar", "api_data": null, "hint": null}, {"title": "FrontierMath - Benchmarks", "url": "https://llm-
stats.com/benchmarks/frontiermath", "snippet": "FrontierMath\nA benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians, covering
most major branches of modern mathematics from number theory and real analysis to algebraic geometry and category theory.\nProgress Over Time\nInteractive timeline showing model performance evolution
on FrontierMath\nState-of-the-art frontier\nOpen\nProprietary\nFrontierMath Leaderboard\n11 models\n| Context | Cost | License | ||||\n|---|---|---|---|---|--", "api_data": null, "hint": null},
{"title": "What will be the best FrontierMath Tier 4 score by Dec 31, 2026? | Manifold", "url": "https://manifold.markets/Bayesian/what-will-be-the-best-frontiermath", "snippet": "This market matches
[Mathematics: FrontierMath Tier 4](https://forecast2026.ai/)[ from the AI 2026 Forecasting Survey by AI Digest](https://forecast2026.ai/).\nSee other manifold questions
[here](https://manifold.markets/topic/2026-ai-forecasting-survey-by-ai-di)\n![](https://firebasestorage.googleapis.com/v0/b/mantic-markets.appspot.com/o/user-
images%2Fdefault%2F8lqPqzZzLn.png?alt=media&token=4e32a80f-b6fe-4c54-afd8-0532c22a4fd8)\nResolution criteria\nResolves to the highest reported accuracy on Fr", "api_data": null, "hint": "Use
manifold_price for market data, or manifold_history for historical prices."}, {"title": "Galois - o3, Frontier Math, and the Future of Mathematics", "url":
"https://www.galois.com/articles/o3-frontier-math-and-the-future-of-mathematics", "snippet": "Over the winter break, OpenAI announced their new model, [o3](https://openai.com/index/early-access-for-
safety-testing/). Much of the media attention rightly focused on its impressive results on the [ARC-AGI benchmark](https://arcprize.org/blog/oai-o3-pub-breakthrough), but for us at Galois, the most
significant result was something else\u2014the model\u2019s [25% score](https://x.com/polynoamial/status/1870172996650053653?mx=2) on a benchmark called Frontier Math.\n[Frontier
Math](https://epoch.ai/frontie", "api_data": null, "hint": null}, {"title": "FRONTIERMATH: A BENCHMARK FOR EVALUATING ADVANCED MATHEMATICAL REASONING IN AI", "url": "https://arxiv.org/pdf/2411.04872",
"snippet": "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI\nAbstract\nWe introduce FrontierMath, a benchmark of hundreds of original, exceptionally challenging
mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics\u2014from computationally intensive problems in number theory and real
analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of e", "api_data": {"content": [{"type": "text", "text": "{\"paper_id\":
\"2411.04872\", \"format\": \"html\", \"url\": \"https://arxiv.org/html/2411.04872\", \"content\": \"FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI\\nAbstract\\nWe
introduce FrontierMath, a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of
modern mathematics\\u2014from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires
multiple hours of effort from a researcher in the relevant branch of mathematics, and for the upper end questions, multiple days. FrontierMath uses new, unpublished problems and automated verification
to reliably evaluate models while minimizing risk of data contamination. Current state-of-the-art AI models solve under 2% of problems, revealing a vast gap between AI capabilities and the prowess of
the mathematical community. As AI systems advance toward expert-level mathematical abilities, FrontierMath offers a rigorous testbed that quantifies their progress.\\n1 Introduction\\nRecent AI
systems have demonstrated remarkable proficiency in tackling challenging mathematical tasks, from achieving olympiad-level performance in geometry [trinh2024solving] to improving upon existing
research results in combinatorics [romera2024mathematical]. However, existing benchmarks face some limitations:\\nSaturation of existing benchmarks\\nCurrent standard mathematics benchmarks such as
the MATH dataset [hendrycks2021measuring] and GSM8K [cobbe2021training] primarily assess competency at the high-school and early undergraduate level. As state-of-the-art models achieve near-perfect
performance on these benchmarks, we lack rigorous ways to evaluate their capabilities in advanced mathematical domains that require deeper theoretical understanding, creative insight, and specialized
expertise. Furthermore, to assess AI\\u2019s potential contributions to mathematics research, we require benchmarks that better reflect the challenges faced by working mathematicians.\\nBenchmark
contamination in training data\\nA significant challenge in evaluating large language models (LLMs) is data contamination\\u2014the inadvertent inclusion of benchmark problems in training data. This
issue leads to artificially inflated performance metrics that mask models\\u2019 true reasoning capabilities [deng2023investigating, xu2024benchmark]. While competitions like the International
Mathematics Olympiad (IMO) or American Invitational Mathematics Examination (AIME) offer fresh test problems created after model training, making them immune to contamination, these sources provide
only a small number of problems and often require substantial manual effort to grade.\\nTo address these limitations, we introduce FrontierMath, a benchmark of original, exceptionally challenging
mathematical problems created in collaboration with over 60 mathematicians from leading institutions. FrontierMath addresses data contamination concerns by featuring exclusively new, previously
unpublished problems. It enables scalable evaluation through automated verification that provides rapid, reproducible assessment. The benchmark spans the full spectrum of modern mathematics, from
challenging competition-style problems to problems drawn directly from contemporary research, covering most branches of mathematics in the 2020 Mathematics Subject Classification (MSC2020).222In
particular, FrontierMath contains problems across 70% of the top-level subjects in the MSC2020 classification excluding \\u201c00 General and overarching topics; collections\\u201d, \\u201c01 History
and biography\\u201d, and \\u201c97 Mathematics education\\u201d.\\nThe problems in FrontierMath demand deep theoretical understanding, creative insight, and specialized expertise, often requiring
multiple hours of effort from expert mathematicians to solve. We provide a set of representative example problems and their solutions (see Appendix B.3 and Figure\\u02dc1). Notably, current state-of-
the-art AI models are unable to solve more than 2% of the problems in FrontierMath, even with multiple attempts, highlighting a significant gap between human and AI capabilities in advanced
mathematics (see Figure 2).\\nTo understand expert perspectives on FrontierMath\\u2019s difficulty and relevance, we interviewed several prominent mathematicians, including Fields Medalists Terence
Tao (2006), Timothy Gowers (1998), and Richard Borcherds (1998), and IMO coach Evan Chen. They unanimously characterized the problems as exceptionally challenging, requiring deep domain expertise and
significant time investment to solve. While they noted that the requirement of numerical answers differs from typical mathematical research practice, these problems nonetheless demand substantial
expertise and time even from experienced mathematicians.\\n2 Data collection\\n2.1 The collection pipeline\\nWe developed the FrontierMath benchmark through collaboration with over 60 mathematicians
from universities across more than a dozen countries. Our contributors formed a diverse group spanning academic ranks from graduate students to faculty members. Many are distinguished participants in
prestigious mathematical competitions, collectively holding 14 IMO gold medals. One contributing mathematician also holds a Fields Medal.\\nTheir areas of expertise collectively span a vast expanse of
modern mathematics\\u2014including but not limited to algebraic geometry, number theory, point set and algebraic topology, combinatorics, category theory, representation theory, partial differential
equations, probability theory, differential geometry, logic, and theoretical computer science. Since many of our contributors are active researchers, the problems naturally incorporate sophisticated
techniques and insights found in contemporary mathematical research.\\nEach mathematician created new problems following guidelines designed to ensure clarity, verifiability, and definitive answers
across various difficulty levels and mathematical domains. Four requirements guided problem creation:\\n-\\n\\u2022\\nOriginality: While problems could build on existing mathematical ideas, they
needed to do so in novel and non-obvious ways\\u2014either through clever adaptations that substantially transform the original concepts, or through innovative combinations of multiple ideas that
obscure their origins. This ensures that solving them requires genuine mathematical insight rather than pattern matching against known problems.\\n-\\n\\u2022\\nAutomated verifiability: Problems had
to possess definitive, computable answers that could be automatically verified. To facilitate automated verification, we often structured problems to have integer solutions, which are straightforward
to check programmatically. We also included solutions that could be represented as arbitrary SymPy objects\\u2014including symbolic expressions, matrices, and more. By utilizing SymPy, we enabled a
wide range of mathematical outputs to be represented and verified programmatically, ensuring that even complex symbolic solutions could be efficiently and accurately checked. This approach allowed us
to support diverse answer types while maintaining verification standards.\\n-\\n\\u2022\\nGuessproofness: Problems were designed to avoid being susceptible to guessing; solving the problem had to be
necessary to find the correct answer. As can be seen from Figure\\u02dc1, problems often have numerical answers that are large and nonobvious, which reduces the vulnerability to guesswork. As a rule
of thumb, we require that there should not be a greater than 1% chance of guessing the correct answer without doing most of the work that one would need to do to \\u201ccorrectly\\\" find the
solution. This is important to ensure that the challenges assessed genuine mathematical understanding and reasoning.\\n-\\n\\u2022\\nComputational tractability: The solution of a computationally
intensive problem must include scripts demonstrating how to find the answer, starting only from standard knowledge of the field.333For example, if a problem requires factoring a large integer, this
must be doable from a standard algorithm. These scripts must cumulatively run less than a minute on standard hardware. This requirement ensures efficient and manageable evaluation times.\\nFor each
contributed problem, mathematicians provided a detailed solution and multiple forms of metadata. Each submission included both a verification script for automated answer checking (see
Section\\u02dc2.2) and comprehensive metadata tags. These tags included subject and technique classifications, indicating both the mathematical domains and specific methodologies required for
solution. Each submission then underwent peer review by at least one mathematician with relevant domain expertise, who evaluated all components: the problem statement, solution, verification code,
difficulty ratings, and classification tags (see Section\\u02dc2.3). Additionally, the problems were securely produced and handled to prevent data contamination, and reviewed for originality (see
Section\\u02dc2.4). Finally, the submissions included structured difficulty ratings that assessed three key dimensions: the required level of background knowledge, the estimated time needed to
identify key insights, and the time required to work through technical details (see Section\\u02dc2.5).\\n2.2 Automated verification\\nFrontierMath focuses exclusively on problems with automatically
verifiable solutions\\u2014primarily numerical answers or mathematical objects that can be expressed as SymPy objects (including symbolic expressions, matrices, sets, and other mathematical
structures). For each problem, the evaluated model submits code that computes and saves its answer as a Python object. A script then automatically verifies this answer. If the problem has a unique
integer solution, it checks for an exact match. If the problem has a unique symbolic real answer, it uses SymPy evaluation to check that the difference between the submitted answer and the actual
answer simplifies to 0. In all other cases, a custom verification script is necessary to check validity of a submitted answer (see Figure 3).\\nThis design choice enables rapid, objective evaluation
of AI models without requiring them to output solutions in formal proof languages like Lean or Coq. The automated verification framework substantially reduces the cost and complexity of evaluation, as
verification can be performed programmatically without human intervention. Furthermore, it eliminates potential human bias and inconsistency in the evaluation process, as the verification criteria are
explicitly defined and uniformly applied.\\nWhile this approach enables efficient and scalable evaluation, it does impose certain limitations. Most notably, we cannot include problems that require
mathematical proofs or formal reasoning steps, as these would demand human evaluation to assess correctness and clarity.444In theory, we could have accepted formalized proofs in Lean or other formal
languages as a problem solution format. However, this presents two challenges. Firstly, current AI models are often not trained to write formalized proofs in specialized languages. We wanted to ensure
that the problems were measuring genuine reasoning skills, rather than skill at writing formalized proofs. Secondly, Lean\\u2019s mathematical library, mathlib, doesn\\u2019t fully cover the
undergraduate math curriculum [mathlib], let alone the scope of research math, which limits the fields such a benchmark could measure. However, even without formal proofs, these problems span a
substantial breadth of modern mathematics and include problems that eminent mathematicians have characterized as exceptionally difficult (see Section\\u02dc6).\\n2.3 Validation and quality
assurance\\nTo maintain high quality standards and minimize errors in the benchmark, we established a rigorous multi-stage review process. Each submitted problem underwent blind peer review by at
least one expert mathematician from our team, who evaluated the following criteria:\\n-\\n\\u2022\\nVerifying the correctness of the problem statement and the provided
solution.\\n-\\n\\u2022\\nChecking for ambiguities or potential misunderstandings in the problem wording.\\n-\\n\\u2022\\nAssessing the problem for guessproofness, ensuring that solutions cannot be
easily obtained without proper mathematical reasoning.\\n-\\n\\u2022\\nConfirming the appropriateness of the assigned difficulty ratings and metadata.\\nVerifying correctness is the most important of
these tasks. For problems with unique solutions\\u2014the majority of our benchmark\\u2014verifying correctness requires checking the mathematical argumentation, computations, and, if applicable,
programming scripts the writer provided to justify their answer. For problems with non-unique solutions, e.g. those which ask for a solution to some system of Diophantine equations or for a
Hamiltonian path in a given graph, the reviewer only checks that the provided verification script matches the problem requirements and test it on the answer.\\nAll problems in the benchmark have
undergone at least one blind peer review. Through this review process, we identify problems with incorrect answers as well as those that fail to meet our guessproofness criterion. Such problems are
only included in the benchmark after authors successfully address these issues through revision.\\nDuring first reviews, our reviewers commonly identify several types of issues with submitted
problems. These include answers that aren\\u2019t easily verifiable, problems where guessing is easier than proving, and cases where simple brute-force methods circumvent the intended difficulty. Such
issues occur predominantly with authors who are new to submitting questions to the benchmark and have not yet fully internalized the guidelines. Beyond these concerns, straightforward errors in
question statements or computational mistakes in solutions leading to incorrect answers are also not uncommon.\\nWe commissioned blind reviews from second reviewers on 30 randomly chosen questions so
far to get some idea about the noise threshold we might expect due to errors, and we also randomly selected 5 questions to be removed from the dataset and serve as a public sample of problems (see
Appendix\\u02dcA). In total, 35 of the accepted problems have received scrutiny beyond the first round of peer review.\\nTwo out of 35 questions had an incorrect answer provided by the author,
undetected in the first review. Assuming that a question being incorrect is a Bernoulli trial with probability and that the second reviewers catch all errors, using a Jeffreys prior on yields a
posterior error rate of for this benchmark. On one hand, the Jeffreys prior is conservative since our prior belief about is likely lower due to the careful construction of the benchmark. On the other
hand, we must account for potential undetected errors that even the second review might have missed. Therefore, estimating a critical error rate of approximately is reasonable. This estimate aligns
with error rates typical in machine learning benchmarks; for instance, [northcutt2021pervasivelabelerrorstest] estimate a label error rate in the ImageNet validation set, while [gema2024we] find that
over of questions in the MMLU benchmark contain errors based on expert review of 3,000 randomly sampled questions.\\nThe second reviews also identified less critical errors. Six out of 35 questions
had missing hypotheses in their statements which technically made them not fully rigorous. While domain experts could reasonably impute this missing context, it might still pose difficulties for
models attempting to solve these problems. For two of the 35 questions, reviewers proposed strategies for guessing the solution with substantially less effort or computation than was necessary for a
rigorous mathematical justification of the answer, violating the guessproofness criterion. In all cases, they proposed adjustments to the problem which corrected the error while preserving the
original mathematical intent of the writer.\\nAlthough the error rate remains low, the mistakes we have spotted highlight the issues of a passive review system, in which the reviewer sees the full
solution document and simply has to state their approval in order for a problem to be accepted into the benchmark. Going forward, we are adopting a more active review process, and will henceforth
require concrete confirmation of a problem\\u2019s soundness before it is accepted. For problems which seek a solution with some easily verified characteristic, such as a tuple of integers satisfying
a Diophantine equation, it is enough to test that criterion directly. If a problem seeks a symbolic real number or some efficiently computed value, then it would be strong evidence if a heuristically
determined guess approximates the given solution. For more abstract problems, it may be necessary to have a reviewer solve the problem themselves, given only the key steps and ideas of the solution
rather than the full write-up.\\nAdditionally, we observed inconsistent difficulty ratings between first and second reviewers; due to the subjective nature of this task, ratings rarely matched and
often showed substantial differences.555See Section 2.5 for discussion on our ongoing effort to normalize these ratings. In several cases, second reviewers found no fundamental problems with the
questions but suggested ways to increase their difficulty, indicating potential room to improve the difficulty of the remaining questions if reviewers were to spend more time on refining them.\\n2.4
Originality and data contamination prevention\\nContributors were explicitly instructed to develop novel mathematical problems. While they could build upon existing mathematical ideas, they were
required to do so in non-obvious ways\\u2014either through clever adaptations that substantially transformed the original concepts, or through novel and innovative combinations of multiple ideas. This
approach ensured that solving the problems required genuine mathematical insight rather than pattern matching against known problems.\\nTo minimize the risk of problems and solutions being
disseminated online, we encouraged all submissions to be conducted through secure, encrypted channels. We employed encrypted communication platforms to coordinate with contributors and requested that
any written materials stored online be encrypted\\u2014for instance, by placing documents in password-protected archives shared only via secure methods.666While we endeavored to adhere strictly to
these protocols, we acknowledge that, in some cases, standard email clients were used when communicating about a subset of the problems outside our immediate team.\\nOur primary method for validating
originality relied on expert review by our core team of mathematicians. Their extensive familiarity with competition and research-level problems enabled them to identify potential similarities with
existing problems that automated systems might miss. The team conducted thorough manual checks against popular mathematics websites, online repositories, and academic publications. This expert review
process was supplemented by verification using plagiarism detection software.\\nTo provide further confidence in our problems\\u2019 originality, we ran them through the plagiarism detection tools
Quetext and Copyscape. Across the entire dataset, the verification process revealed no significant matches to existing content, with minimal flags attributed only to standard mathematical terminology
or software oversensitivity.777We limited our plagiarism checking to problem statements only, excluding solutions to minimize online exposure. We specifically chose Quetext and Copyscape over more
widely-used tools like Turnitin because they posed the lowest risk of our problems being stored in databases that might later be used to train AI models.\\n2.5 Problem difficulty\\nEstimates of
mathematical problem difficulty are useful for FrontierMath\\u2019s goal of evaluating AI mathematical capabilities, as such estimates would provide more fine-grained information about the performance
of AI models. To assess problem difficulty, each problem author provided ratings along three key dimensions:\\n-\\n1.\\nBackground: This rating ranges from 1 to 5 and indicates the level of
mathematical background required to approach the problem. A rating of 1 corresponds to high school level, 2 to early undergraduate level, 3 to late undergraduate level, 4 to graduate level, and 5 to
research level.\\n-\\n2.\\nCreativity: Estimated as the number of hours an expert would need to identify the key ideas for solving the problem. This measure has no upper limit.\\n-\\n3.\\nExecution:
Similarly estimated as the number of hours required to compute the final answer once the key ideas are found, including time writing a script if applicable. This measure also has no upper limit.\\nTo
verify and refine the initial difficulty assessments, each difficulty assessment underwent a peer-review process. Reviewers assessed the accuracy of the initial difficulty ratings. Any discrepancies
between the authors\\u2019 ratings and the reviewers\\u2019 assessments were discussed, and adjustments were made as needed to ensure that the difficulty ratings accurately reflected the
problem\\u2019s demands in terms of background, creativity, and execution.\\nAccurately assessing the difficulty of mathematics problems presents significant challenges [Chen2024, Chen2024Mistake].
Problems that seem impossible may become trivial after exposure to certain techniques, and multiple solution paths of varying complexity often exist. Moreover, while we designed our problems to
require substantial mathematical work rather than allow solutions through guessing or pattern matching, the possibility of models finding unexpected shortcuts could undermine such difficulty
estimates.\\nGiven these challenges, we view our difficulty ratings as providing rough guidance. More rigorous validation, such as through systematic data collection on human solution times, would be
needed to make stronger claims about these difficulty assessments.888In unpublished preliminary work, we found that problems rated as more difficult correlate with lower solution rates by GPT-4o,
providing some support for our difficulty assessment system. However, more systematic validation would be needed to make strong claims about the reliability of these ratings.\\n3 Dataset
composition\\nThe FrontierMath benchmark covers a broad spectrum of contemporary mathematics, spanning both foundational areas and specialized research domains. This comprehensive coverage is crucial
for effectively evaluating AI systems\\u2019 mathematical capabilities across the landscape of modern mathematics. Working with over 60 mathematicians across different specializations, we captured
most top-level MSC 2020 classification codes, reflecting the breadth of mathematics from foundational fields to emerging research areas.\\n| MSC Classification | Percentage | MSC Classification |
Percentage |\\n| 11 Number theory | 17.8% | 57 Manifolds and cell complexes | 2.1% |\\n| 05 Combinatorics | 15.8% | 13 Commutative algebra | 2.1% |\\n| 20 Group theory and generalizations | 8.9% | 54
General topology | 1.4% |\\n| 60 Probability theory and stochastic processes | 5.1% | 35 Partial differential equations | 1.4% |\\n| 15 Linear and multilinear algebra; matrix theory | 4.8% | 53
Differential geometry | 1.4% |\\n| 14 Algebraic geometry | 4.8% | 42 Harmonic analysis on Euclidean spaces | 1.4% |\\n| 33 Special functions | 4.8% | 41 Approximations and expansions | 1.4% |\\n| 55
Algebraic topology | 3.1% | 52 Convex and discrete geometry | 1.4% |\\n| 12 Field theory and polynomials | 2.4% | 82 Statistical mechanics, structure of matter | 1.0% |\\n| 30 Functions of a complex
variable | 2.4% | 44 Integral transforms, operational calculus | 1.0% |\\n| 68 Computer science | 2.4% | 17 Nonassociative rings and algebras | 1.0% |\\n| 18 Category theory; homological algebra |
2.4% | Other (< 3 problems each) | 9.9% |\\nNumber theory and combinatorics are most prominently represented, collectively accounting for approximately 34% of all MSC2020 tags. This prominence
reflects both our contributing mathematicians\\u2019 expertise and these domains\\u2019 natural amenability to problems with numerical solutions that can be automatically verified. The next most
represented fields are algebraic geometry and group theory (together about 14% of MSC tags), followed by algebraic topology (approximately 3%), linear algebra (5%), and special functions (5%).
Problems involving probability theory and stochastic processes constitute about 5% of the MSC tags, with additional significant representation in complex analysis, category theory, and partial
differential equations, each comprising between 1-3% of the MSC tags.\\nThe network visualization (Figure 4) reveals how mathematical subjects combine within individual problems. Number theory and
combinatorics appear together most frequently, with 13% of problems requiring both subjects, followed by combinatorics-group theory (9%) and number theory-group theory (8%). These three
fields\\u2014number theory (44% of all problems), combinatorics (39%), and group theory (22%)\\u2014form the core of the benchmark, each combining with more than a dozen other mathematical domains in
novel ways.\\nThere is a wide range of techniques required to solve the problems in our dataset. In particular, there are over 200 different techniques listed as being involved in the solutions of our
problems. Although generating functions, recurrence relations, and special functions emerge as common techniques, they each appear in less than 5% of problems, underscoring the benchmark\\u2019s
methodological diversity. Even the most frequently co-occurring techniques appear together in at most 3 problems, highlighting how problems typically require unique combinations of mathematical
approaches.\\n4 Evaluation\\n4.1 Experiment-enabled evaluation framework\\nTo evaluate AI models on FrontierMath problems, we developed a framework that allows models to explore and verify potential
solution approaches through code execution, mirroring how mathematicians might experiment with ideas when tackling challenging problems. This framework enables models to test hypotheses, receive
feedback, and refine their approach based on experimental results, as illustrated in Figure 5.\\nThe evaluation process follows an iterative cycle where the model analyzes the mathematical problem,
proposes solution strategies, implements these strategies as executable Python code, receives feedback from code execution results, and refines its approach based on the experimental outcomes. For
each problem, the model interacts with a Python environment where it can write code blocks that are automatically executed, with outputs and any error messages being fed back into the conversation.
This allows the model to verify intermediate results, test conjectures, and catch potential errors in its reasoning.\\nWhen submitting a final answer, models must follow a standardized format by
including a specific marker comment (# This is the final answer\\n), saving the result using Python\\u2019s pickle module, and ensuring the submission code is self-contained and independent of
previous computations. The interaction continues until either the model submits a correctly formatted final answer or reaches the token limit, which we set to 10,000 tokens in our experiments. If a
model reaches this token limit without having submitted a final answer, it receives a final prompt requesting an immediate final answer submission. If the model still fails to provide a properly
formatted final answer after this prompt, the attempt is marked as incorrect.\\n4.2 Results\\n4.2.1 Accuracy on FrontierMath\\nWe evaluated six leading language models on our existing subset of
FrontierMath problems: o1-preview ([o1-preview]), o1-mini ([o1-mini]), and GPT-4o (2024-08-06 version) ([GPT-4o]), Claude 3.5 Sonnet (2024-10-22 version) ([sonnet3-5]), Grok 2 Beta ([grokbeta]), and
Google DeepMind\\u2019s Gemini 1.5 Pro 002 ([gemini15pro002]). All models had a very low performance on FrontierMath problems, with no model achieving even a 2% success rate on the full benchmark (see
Figure 6). This stands in stark contrast to other mathematics evaluations such as GSM8K ([cobbe2021training]), MATH ([hendrycks2021measuring]), AIME 2024 ([o1-learningtoreason]), or Omni-MATH
([gao2024omni]), which are closer to saturation (see Figure 2).\\nBased on a single evaluation of the full benchmark, we found that models solved very few problems (less than 2% success rate). Given
this low success rate and the fact that we ran only one evaluation, the precise ordering of model performance should be interpreted with significant caution, as individual successes can have an
outsized impact on rankings. To better understand model behavior on solved problems, we identified all problems that any model solved at least once\\u2014a total of four problems\\u2014and conducted
repeated trials with five runs per model per problem (see Appendix B.2). We observed high variability across runs: only in one case did a model solve a question on all five runs (o1-preview for
question 2). When re-evaluating these problems that were solved at least once, o1-preview demonstrated the strongest performance across repeated trials (see Section B.2).\\nMoreover, even when a model
obtained the correct answer, this does not mean that its reasoning was correct. For instance, on one of these problems running a few simple simulations was sufficient to make accurate guesses without
any deeper mathematical understanding. However, models\\u2019 low overall accuracy shows that such guessing strategies do not work on the overwhelming majority of FrontierMath problems. We also ran
each model five times per problem on our five public sample problems (see Appendix A), and made the transcripts publicly available.999The transcripts can be downloaded at
https://epochai.org/files/sample_question_transcripts.zip\\n4.2.2 Number of responses and token usage\\nOur evaluation framework allows models to run experiments and reflect on their results multiple
times before submitti\"}"}]}, "hint": null}, {"title": "FrontierMath | AI Wiki", "url": "https://aiwiki.ai/wiki/frontiermath", "snippet": "| FrontierMath | |\n|---|---|\n| Overview | |\n| Full name |
FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI |\n| Abbreviation | FrontierMath |\n| Description | A benchmark of research-level mathematics problems designed to
evaluate advanced mathematical reasoning in AI systems |\n| Release date | 2024-11 |\n| Latest version | 2025-02-28 |\n| Benchmark updated | 2025-02 |\n| Authors | Elliot Glazer, Ege Erdil, Tamay
Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Carol", "api_data": null, "hint": null}]}
```

```json
{
  "query": "FrontierMath Tier 4 40%"
}
```

### 📋 Result

```
{"markets": [], "query": "FrontierMath Tier 4 40%"}
```

```json
{
  "query": "new AI model release April 2026 Claude Gemini GPT"
}
```

### 📋 Result

```
{"query": "new AI model release April 2026 Claude Gemini GPT", "results": [{"title": "New AI Model Releases News | April, 2026 (STARTUP EDITION)", "url": "https://blog.mean.ceo/new-ai-model-releases-
news-april-2026/", "snippet": "TL;DR: New AI Model Releases News, April, 2026\nApril 2026 introduced groundbreaking AI tools, including Anthropic\u2019s Claude Mythos 5 with 10 trillion parameters for
advanced cybersecurity and coding, and the accessible Capabara model. Google DeepMind\u2019s Gemini 3.1 adds real-time voice and image analysis, while Google\u2019s compression algorithm slashes AI
costs by reducing memory needs by six times.\n\u2022 Entrepreneurs can use Gemini 3.1 for customer service and lightweight AI systems for affordability.\n\u2022", "api_data": null, "hint": null},
{"title": "AI Updates Today (April 2026) \u2013 Latest AI Model Releases", "url": "https://llm-stats.com/llm-updates", "snippet": "AI UpdatesToday\nTrack AI model updates and LLM releases in real
time. Version launches, API changes, and notable improvements across GPT, Claude, Gemini, Llama, and 500+ language models.\nModel Version Timeline\nTrack all LLM releases and version
updates\nUnderstanding LLM Versioning\nAI model versioning follows patterns that help developers understand capabilities and stability. Major versions (GPT-3 \u2192 GPT-4, Claude 2 \u2192 Claude 3)
indicate significant capability improvements and may require prompt a", "api_data": null, "hint": null}, {"title": "AI Models in 2026: Which One Should You Actually Use?", "url":
"https://gurusup.com/blog/ai-comparisons", "snippet": "[Artificial Intelligence](https://gurusup.com/blog/category/artificial-intelligence)\nAI Models in 2026: Which One Should You Actually Use?\n![AI
Models in 2026: Which One Should You Actually
Use?](/_next/image?url=https%3A%2F%2Fres.cloudinary.com%2Fdhqzl4gpk%2Fimage%2Fupload%2Fv1771362322%2Ffeatured_comparativas_ia_c451d8fc4e.jpg&w=3840&q=75)\nThe AI landscape in 2026 looks nothing like
it did two years ago. Four frontier models now compete across coding, reasoning, writing, and business automatio", "api_data": null, "hint": null}, {"title": "AI Models in April 2026: Every Major
Release, Leak, and What Comes Next", "url": "https://renovateqr.com/blog/ai-models-april-2026", "snippet": "AI Models in April 2026: Every Major Release, Leak, and What Comes Next\nYour definitive
reference for AI model releases in April 2026. From the Claude Mythos leak to GPT-5.5 Spud, Gemini 3.1 Pro, Grok 4.20, and Llama 4, here is everything that matters this month.\n![A split-panel
visualization of the major AI labs competing in April 2026: Anthropic, OpenAI, Google, Meta, and xAI](/images/blog/ai-models-april-2026.webp)\nTL;DR\nThe Claude Mythos data leak (March 26) confirmed
Anthropic's most powerf", "api_data": null, "hint": null}, {"title": "LLM News Today (April 2026) \u2013 AI Model Releases", "url": "https://llm-stats.com/ai-news", "snippet": "![Claude Mythos
Preview: Benchmarks, Pricing & Project Glasswing](/_next/image?url=%2Fblog%2Fclaude-mythos-preview-launch%2Fbanner.webp&w=2048&q=75)\nClaude Mythos Preview: Benchmarks, Pricing & Project
Glasswing\nAnthropic's unreleased Claude Mythos Preview scores 93.9% on SWE-bench Verified, 94.6% on GPQA Diamond, and found thousands of zero-day vulnerabilities across every major OS and
browser.\n![Jonathan Chavez](/_next/image?url=%2Fblog%2Fjona.jpg&w=48&q=75)\nYour daily source for LLM news, ope", "api_data": null, "hint": null}, {"title": "Best AI Models April 2026: Ranked by
Benchmarks", "url": "https://www.buildfastwithai.com/blogs/best-ai-models-april-2026", "snippet": "Best AI Models April 2026: Every Major Release Ranked by Real Benchmarks\nTwelve significant AI model
releases in a single week. That happened in March 2026. Not a month -- a week.\nI tracked every launch, ran the benchmark numbers, and compared the specs across GPT-5.4, Gemini 3.1 Pro, Claude Opus
4.6, GLM-5, DeepSeek V4, Llama 4, and a dozen others. The short version: the gap between open-source and proprietary AI has nearly closed. The longer version is what this guide is for.\nLLM Stats,
which ", "api_data": null, "hint": null}, {"title": "AI Model Benchmarks Apr 2026 | Compare GPT-5, Claude 4.5, Gemini 2.5, Grok 4 | LM Council", "url": "https://lmcouncil.ai/benchmarks", "snippet":
"18 benchmarks - the world's most-followed benchmarks, curated by [AI Explained](https://www.youtube.com/@aiexplained-official), author of [SimpleBench](https://simple-bench.com)\nIndependently-run
benchmarks by Epoch, Scale and others, so may not match self-reported scores by AI orgs.\n| Models (no tools) | Score | |\n|---|---|---|\n| 1 | Gemini 3 Pro Preview | 37.52% \u00b11.90 |\n| 2 | Claude
Opus 4.6 (max) | 34.44% \u00b11.86 |\n| 3 | GPT-5 Pro | 31.64% \u00b11.82 |\n| 4 | GPT-5.2 | 27.80% \u00b11.76 |\n| 5 | GPT-5 (Aug", "api_data": null, "hint": null}, {"title": "Claude vs GPT-5.2 vs
Gemini 3: I Tested All Three for Real Coding Projects (2026 Results)", "url": "https://www.cosmicjs.com/blog/best-ai-for-developers-claude-vs-gpt-vs-gemini-technical-comparison-2026", "snippet":
"[BlogBack to\nblog](https://www.cosmicjs.com/blog)\nClaude vs GPT-5.2 vs Gemini 3: I Tested All Three for Real Coding Projects (2026 Results)\n![Tony Spiro's
avatar](https://imgix.cosmicjs.com/1eaf6d80-f101-11f0-8762-271eb77ff3d5-tony.jpeg?w=100&h=100&auto=format&dpr=2)\n![Tony Spiro's
avatar](https://imgix.cosmicjs.com/1eaf6d80-f101-11f0-8762-271eb77ff3d5-tony.jpeg?w=100&h=100&auto=format&dpr=2)\nTony Spiro\nJanuary 30, 2026\n![Claude vs GPT-5.2 vs Gemini 3: I Tested All Three for
Real Coding Projects", "api_data": null, "hint": null}, {"title": "OpenAI's Secret Weapon Has a Codename. It's Called 'Spud.' And It's Coming This Month. \u2014 LumiChats Blog", "url":
"https://lumichats.com/blog/gpt-5-5-spud-openai-release-date-features-april-2026-complete-guide", "snippet": "Why a Potato Codename Is the Most Important Thing in AI Right Now\nGoogle uses desserts.
Microsoft uses cities. OpenAI apparently uses root vegetables. The codename 'Spud' is a placeholder \u2014 confirmed by multiple sources including The Information, which first reported the pretraining
completion on March 24, 2026 \u2014 that carries almost none of the strategic weight of what it represents. What it represents is this: for the first time since the original
[GPT-5](https://lumichats.com/glossary/gpt-4-gp", "api_data": null, "hint": null}, {"title": "The Best AI Models So Far in 2026 | Design for Online\u00ae", "url": "https://designforonline.com/the-
best-ai-models-so-far-in-2026/", "snippet": "February 2026 has been a major month for AI model releases, too many to count but we have been able to test a few and review some which are upcoming. With
seven major model releases in a single month, Google, Anthropic, OpenAI, xAI, and Alibaba all dropped significant updates within weeks of each other, with benchmark records being broken again and
frontier performance continuing on all fronts. If you are trying to work out what any of it means for your business, your workflows, or your budget, ", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Now I have a much clearer picture. Let me check some key details:

1. **Current record on Tier 4**: GPT-5.4 Pro scored 38% (which is actually 18/48 = 37.5%, reported rounded as 38%). This was published March 5, 2026.

2. **The question asks for 40.0%**: On 48 problems, that's 19.2, so a model needs at least 20/48 = 41.67% to hit 40.0%. Wait, actually, they might report exact percentages. 

So 19/48 gives 39.58%, which falls short of 40%, while 20/48 equals 41.67%, which exceeds it. Looking back at the DataLearner leaderboard, I see GPT-5.4 Pro at 38 and GPT-5.2 Pro at 31.3, which corresponds to 15/48 = 31.25% when rounded.

The Epoch report states GPT-5.4 scored 38%, and breaking down the performance: 25% on non-held-out problems (7 correct out of 28) plus 55% on held-out problems (11 correct out of 20) gives 18/48 = 37.5%, which rounds to 38%. There might be a slight discrepancy depending on whether we're counting 48 or 50 total problems. The pass@10 score for GPT-5.4 (xhigh) was also 38%, and across all runs combined, 42% of problems have been solved at least once—meaning no single attempt has broken the 40% threshold. The real question is whether a new model will be evaluated on Tier 4 between now and May 1st, and I'm seeing some candidates: Claude Mythos leaked in late March with preview scores, and GPT-5.5 "Spud" reportedly finished pretraining in late March as well.

Looking at the LM Council benchmarks, I see Gemini 3.1 Pro from April 2026 and Claude Opus 4.6 mentioned, but those scores appear to be on the combined Tiers 1-3, not Tier 4 specifically. For the forecast to hit, I need a model that's both released and evaluated by Epoch AI on Tier 4 before May 1st, and it has to score 40% or higher.

The challenge is tight: with only about 19 days left, and considering Epoch AI typically needs several days between getting pre-release access and publishing results, there's barely enough time. Even if GPT-5.5 "Spud" finishes pretraining or Claude Mythos launches, getting an evaluation published in that window would be cutting it extremely close. The score gap itself is small—just 2 more problems out of 48—but the real bottleneck is whether Epoch AI can turn around a Tier 4 evaluation that quickly. of 48 (from ~18 to ~20)
4. **The pass@the-kitchen-sink is already 42%** (20/48 across all models ever), so the problems that would get us to 40% have been solved individually

Wait, the question description says "37.5%" but the official report says "38%." This is actually a meaningful discrepancy. 

If the exact score is 37.5% (18/48), then getting to 40% means 20/48 = 41.67%, which is ≥40%. That requires solving 2 more problems.

If 19/48 = 39.58%, that's still below 40%. So we need 20/48 = 41.67%.

But actually, the question says "at least 40.0%." If Epoch reports with one decimal place, then even 40.0% would qualify. On 48 problems, there's no way to get exactly 40.0% (the closest are 39.58% = 19/48 and 41.67% = 20/48). So effectively, the model needs to get 20/48 correct.

Current best is 18/48 from GPT-5.4 Pro, so we need 2 more problems solved. Looking at potential candidates, GPT-5.5 "Spud" finished pre-training around late March and would need post-training before evaluation, making an April-May release timeline uncertain for Epoch's assessment. Claude Mythos has been previewed and could launch soon, though I'm not seeing Claude models historically evaluated on Tier 4 benchmarks in the leaderboard data.

Gemini 3.1 Pro released in April 2026 and might get evaluated, but Gemini 3 Pro Preview only managed 19% on Tier 4, so a massive improvement would be needed. I'm also seeing references to Claude Opus 4.6 scoring 34.44% on LM Council benchmarks, but that's on a combined FrontierMath metric rather than specifically Tier 4. Checking the Epoch AI benchmarks page, the most recent updates are from March 9 and March 5, 2026, with no newer Tier 4 evaluations since then.

The timeline is extremely tight—the question closes today and resolves May 1. GPT-5.5 Spud finished pretraining March 24, but post-training typically takes weeks to months, so even a late April release would be cutting it close for Epoch AI to evaluate it. I'm also checking if there have been any April updates I missed on the benchmarks page or other sources for recent Tier 4 results.

Looking at the LM Council results more carefully, I'm seeing scores around 30-37% that appear to be FrontierMath benchmarks—Gemini 3 Pro Preview at 37.52%, Claude Opus 4.6 at 34.44%, and GPT-5 Pro at 31.64%—but I need to verify whether these are specifically Tier 4 scores or combined across tiers.

The discrepancies are throwing me off. GPT-5 Pro shows 31.64% on this list but only 14.6% on Tier 4, so these can't be Tier 4 scores. They're more likely Tiers 1-3 combined, though the exact numbers don't quite align with what I'd expect. Regardless, what matters is that the current Tier 4 best remains 38% from GPT-5.4 Pro as of March 5, still below the 40% threshold with about 19 days left and no new evaluations published since then.

For this to resolve YES, I need a new model released and evaluated on Tier 4 before May 1 that scores at least 40%. The key question is whether a sufficiently capable model will emerge and get tested in time—GPT-5.5 seems unlikely to launch and be evaluated that quickly, and while Claude Mythos could theoretically be released, Epoch AI appears to focus primarily on OpenAI models based on what I see on the leaderboard.

Looking at recent performance, even GPT-5.4's best attempt only reached 38% on Tier 4, so any new model would need to be a meaningful step forward to hit 40%. Gemini 3.1 Pro was just released but its predecessor only scored 19%, suggesting even a significant upgrade might fall short.

Weighing the constraints—the tight timeline of roughly 19 days, the rarity of major model releases, Epoch AI's evaluation capacity, and the performance ceiling we're seeing—I'd estimate around 20-30% chance a qualifying model gets released and evaluated in time.

There's also the possibility Epoch AI already has a pre-release model under evaluation that we don't know about, which could shift these odds somewhat. And I notice the official score shows 38% while the underlying data might be 37.5%, though that distinction doesn't affect whether 40% gets crossed.

Looking at the timeline more carefully—the question closes April 12, 2026 at 15:00 UTC, which is essentially now, with resolution on May 1. That's only 19 days for a new model to emerge, get evaluated by Epoch on Tier 4 specifically, and hit 40% or higher. Given how rapidly the frontier is moving, I'd estimate this at around 15-25% probability, though the tight window and specific requirements make it a challenging bar to clear. new models are being released frequently
- GPT-5.5 "Spud" has reportedly completed pretraining
- Claude Mythos is potentially very capable
- The gap from 38% to 40% (needing ~2 more correct problems) is not huge
- 20/48 problems have already been solved across all models ever (pass@kitchen-sink = 42%), so the problems are solvable
- Epoch AI has demonstrated willingness to evaluate models with pre-release access

**Factors pushing toward NO:**
- Only ~19 days remain
- No new Tier 4 evaluation has been published since March 5 (over 5 weeks ago)
- Epoch AI primarily evaluates OpenAI models on Tier 4; other models may not be prioritized
- Even pass@10 for GPT-5.4 was only 38%, suggesting the current architecture plateau
- GPT-5.5 is likely still in post-training and may not be ready in time
- Claude and Gemini models have historically underperformed on Tier 4

I'm settling on around 20% probability, though I should double-check for any recent Epoch AI updates I might have missed. I notice their capabilities page was updated in mid-April, and there's mention of Gemini 3.1 Pro in the recent releases, so let me see if there's anything new on the benchmarks that changes my assessment. Looking at the LM Council scores more carefully, those appear to be combined metrics across multiple tiers rather than Tier 4 specifically. The historical data shows that as of March 5, 2026, only 20 out of 48 Tier 4 problems have ever been solved by any model, which means a 20/48 score would require solving every previously-solved problem—something that seems unlikely for a new model attempting the benchmark. any single model - GPT-5.4 Pro solved 18/48 but not necessarily the same 18 that make up the "pass@kitchen-sink" set.

Wait, looking at the data more carefully:
- GPT-5.4 Pro solved 18/48 in its standard run
- In the pass@10 (10 additional runs of GPT-5.4 xhigh), one additional problem was solved (the one by Bartosz Naskręcki), bringing the total unique to 19 from GPT-5.4 alone
- The overall pass@kitchen-sink across ALL models is 20/48

So GPT-5.4 solved 18-19 problems across its runs, and 1-2 more have been solved by other models but not by GPT-5.4. For a new model to hit 20/48, it would need to solve at least 20 unique problems in a single run.

This is a significant jump - the best single run was 18/48, so a new model would need to solve 2 more problems than that. Given the improvement trajectory from GPT-5.2 to GPT-5.4 (19% to 31% to 38%), a next-gen model could plausibly reach 40%+, but the real question is whether it'll be released and evaluated in time. The key uncertainties are whether a new model like GPT-5.5 or Claude will be available before the Tier 4 evaluation deadline around April 25, and whether Epoch AI will have time to run it. usually takes weeks to months
- Could conceivably have a preview or early access in late April
- But this seems optimistic

For Claude Mythos:
- Leaked/previewed but may not be officially released
- Epoch AI might not prioritize evaluating it on Tier 4 (they've never evaluated Claude on Tier 4 as far as I can see)

For Gemini 3.1 Pro:
- Already released in April
- Gemini 3 Pro scored only 19% on Tier 4
- Even a significant improvement likely wouldn't reach 40%

I think I should lower my estimate. Maybe 12-18% probability.

Let me set it at 15%.

Actually, let me think about this more carefully. The question was just published today (April 12). It was likely created because the author thought there was a non-trivial but not high probability. The question description says "40.0% is not crazy far away but still a substantial jump."

There's another constraint I need to factor in: Epoch AI's leaderboard is the resolution source, so even if a model gets released and hits 40% elsewhere, it only counts if Epoch AI evaluates it on their framework. That's a meaningful additional hurdle. Weighing everything together, I'm settling on around 15-20% as my estimate.

## 💬 Response

Let me check for any very recent Epoch AI evaluations and prediction markets for context.

## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "FrontierMath Tier 4 score 2026"
}
```

### 📋 Result

```
{"markets": [{"market_title": "What will be the best FrontierMath Tier 4 score by Dec 31, 2026?", "probability": 0.5, "volume": 35840.85144069823, "url": "https://manifold.markets/Bayesian/what-will-
be-the-best-frontiermath", "source": "manifold", "description": null, "market_id": "qd9CuLsOZN", "recent_history": [{"date": "2026-04-07", "probability": 0.11}]}], "query": "FrontierMath Tier 4 score
2026"}
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Epoch AI FrontierMath Tier 4 new evaluation April 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "The Epoch Brief - March 2026", "url": "https://epochai.substack.com/p/the-epoch-brief-march-2026", "snippet": "The Epoch Brief - March 2026 - Epoch AI\n\n# Epoch AI\n\nSubscribeSign
in\n\nThe Epoch Brief\n\n# The Epoch Brief - March 2026\n\n### AI solves an open research math problem, growth in high-bandwidth chip memory, what job postings reveal about frontier labs' plans, and
more\n\nEpoch AI\n\nApr 02, 2026\n\n15\n\n1\n\nShare\n\nWelcome to this edition of the Epoch AI Brief! This month:\n\nWe published three new Data Insights: Microsoft\u2019s AI-driven capex,
bottlenecks in AI chip production, and AI chip memory bandwidth growt", "highlights": ["The Epoch Brief - March 2026 - Epoch AI\n\n# Epoch AI\n\nSubscribeSign in\n\nThe Epoch Brief\n\n# The Epoch
Brief - March 2026 ### AI solves an open research math problem, growth in high-bandwidth chip memory, what job postings reveal about frontier labs' plans, and more Epoch AI\n\nApr 02,
2026\n\n15\n\n1\n\nShare\n\nWelcome to this edition of the Epoch AI Brief! This month: We published three new Data Insights: Microsoft\u2019s AI-driven capex, bottlenecks in AI chip production, and AI
chip   ...    We published two new Gradient Updates: final training runs account for a minority of R&D compute spending, and what job postings reveal about the plans of frontier AI labs. We saw
notable AI achievements on our mathematics benchmarks: a solution to a problem in our FrontierMath: Open Problems, and a new record on FrontierMath: Tiers 1\u20134. We\u2019re hiring a Data Scientist
(Contract) and a Special Projects Associate.\n\n# Publications\n\n## Data Insights   ...    Total AI chip memory bandwidth has grown 4.1\u00d7 per year, now reaching 70 million terabytes per second.
As of Q4 2025,   ...    around 300,000\u00d7 more data per second than global internet traffic. Figures are drawn from financial disclosures of five   ...    in 2025. We estimate that the four largest
AI chip designers collectively consumed around 90% of global CoWoS capacity and HBM supply by value in 2025, while consuming only 12% of advanced logic die production.   ...    Final training runs
account for a minority of R&D compute spending. We estimate that less than 30% of R&D compute spending by MiniMax and Z.ai goes to final training runs. This corroborates previous findings for OpenAI
from 2024 and   ...    What do frontier AI companies\u2019 job postings reveal about their plans? AI companies guard their strategies closely, but their hiring pages are public. An analysis of job
postings shows a fast increase in go-to-market roles, and hints about upcoming products. ## FrontierMath Benchmarks AI has solved a problem in FrontierMath: Open Problems, our benchmark of real
research problems that mathematicians have tried and failed to solve. The problem is from the Moderately Interesting tier. The contributing mathematician, Will Brian, is excited to write up the
solution for publication, along with Kevin Barreto and Liam Price, who first elicited the solution from GPT-5.4 Pro. We removed a different problem from FrontierMath: Open Problems after determining
that it did not meet our bar for mathematical notability. Earlier in March, GPT-5.4 set a new record on FrontierMath: Tiers 1\u20134, our benchmark of extremely challenging math problems with known
solutions. We had pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4, it scored 38%, including a solution to one Tier 4 problem that no model had solved
before. ## Other quick takes and updates We updated the epoch.ai website design. Our goal is to make it easier to find and use our work, whether you\u2019re a policymaker, researcher, or just curious
about where AI is headed. We\u2019d love to hear what you think \u2014 email us at design@epoch.ai We\u2019ve updated the Epoch Capabilities Index with three new benchmarks (APEX-Agents, ARC-AGI-2,
and HLE) and several new models. GPT-5.4 Pro is the current state-of-the-art, with a narrow lead over Gemini 3.1 Pro. # Organizational Updates\n\n## Careers We\u2019re hiring for a Data Scientist
(Contract) to assist with our AI research efforts. This role involves reviewing   ...    and receive only the updates"], "published_date": "2026-04-02T17:17:04.000", "score": null}, {"title": "New
record on FrontierMath Tier 4 - Epoch AI | Substack", "url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4", "snippet": "New record on FrontierMath Tier 4 - Epoch AI\n\n# Epoch
AI\n\nSubscribeSign in\n\nUpdates\n\n# New record on FrontierMath Tier 4\n\n### GPT-5.2 Pro (manual run) scored 31%, a substantial jump over the previous high score of 19%.\n\nJan 23,
2026\n\n15\n\n1\n\nShare\n\nWe evaluated GPT-5.2 Pro manually on the ChatGPT website. We did this after encountering timeout issues with the API in our scaffold. We\u2019re working to resolve these
issues, but a manual evaluation seemed worthwhile in the meantime.\n\nPrior to this run, ", "highlights": ["New record on FrontierMath Tier 4 - Epoch AI\n\n# Epoch AI\n\nSubscribeSign
in\n\nUpdates\n\n# New record on FrontierMath Tier 4 ### GPT-5.2 Pro (manual run) scored 31%, a substantial jump over the previous high score of 19%.\n\nJan 23, 2026\n\n15\n\n1 Share We evaluated
GPT-5.2 Pro manually on the ChatGPT website. We did this after encountering timeout issues with the API in our scaffold. We\u2019re working to resolve these issues, but a manual evaluation seemed
worthwhile in the meantime. Prior to this run, 13 problems from Tier 4 had been solved by any model ever. GPT-5.2 Pro solved 11 of those, and 4 more besides. Its total for this run is thus 15/48
(31%), and the pass@the-kitchen-sink for Tier 4 (all problems solved ever) is now 17/48 (35%). OpenAI has exclusive access to 28 Tier 4 problems and their solutions, with Epoch holding out the other
20 problems. GPT-5.2 Pro solved 5 (18%) of the non-held-out set and 10 (50%) of the held-out set. In other words: no evidence of over-fitting. During evaluation we found issues with two problems.
GPT-5.2 Pro and GPT-5.2 (high) should have been credited with solving both, and GPT-5.2 (xhigh), (medium), and GPT-5 Pro should have been credited with solving one. We\u2019ve fixed the issues and
updated the scores on our hub. One of the newly-solved problems was from Joel Hass, whose research is in low-dimensional topology and geometry. Afterward, he suggested we try a different, more
challenging formulation of the same problem. GPT-5.2 Pro solved that too. Another problem, by number theorist Ken Ono was initially solved by GPT-5.2 (xhigh), and also by GPT-5.2 Pro. Ken gave   ...
Another newly-solved problem was by number theorist Dan Romik. He was impressed. A pair of problems by Jay Pantone, who works in analytic combinatorics, were solved earlier: one by GPT-5 and one by
GPT-5.1. GPT-5.2 Pro solved these as well. The solutions were both valid, but Jay noted that both used numerical shortcuts that he didn\u2019t intend. What remains unsolved? One author thinks models
get his problem wrong because they make a plausible assumption without trying to prove it. If they tried to prove it \u2014 as he had to, when he encountered the problem in his own research \u2014
they might realize the truth is more subtle. Check our website for more info on FrontierMath and analysis of AI math capabilities! Thanks for reading! Subscribe to receive the latest from Epoch
AI.\n\nSubscribe\n\n15\n\n1\n\nShare\n\nPreviousNext #### Discussion about this post\n\nCommentsRestacks\n\nNo posts\n\n### Ready for more?\n\nSubscribe \u00a9 2"], "published_date":
"2026-01-23T19:14:14.000", "score": null}, {"title": "FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI", "url": "https://epoch.ai/frontiermath/tier-4", "snippet": "FrontierMath:
LLM Benchmark for Advanced AI Math Reasoning | Epoch AI\n\n# FrontierMath: Benchmarking AI against advanced mathematical research\n\nFrontierMath includes both carefully crafted challenge problems and
open research problems that remain unsolved by mathematicians.\n\n### FrontierMath Tiers 1\u20134\n\nA benchmark of several hundred unpublished, highly challenging mathematics problems. Difficulty
Tiers 1-3 cover undergraduate through early postdoc level problems, while Tier 4 is research-level ma", "highlights": ["FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI #
FrontierMath: Benchmarking AI against advanced mathematical research FrontierMath includes both carefully crafted challenge problems and open research problems that remain unsolved by mathematicians.
### FrontierMath Tiers 1\u20134 A benchmark of several hundred unpublished, highly challenging mathematics problems. Difficulty Tiers 1-3 cover undergraduate through early postdoc level problems,
while Tier 4 is research-level mathematics. ### Open Problems A collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would
meaningfully advance the state of human mathematical knowledge. Feedback"], "published_date": null, "score": null}, {"title": "GPT-5.4 set a new record on FrontierMath - Epoch AI", "url":
"https://epochai.substack.com/p/gpt-54-set-a-new-record-on-frontiermath", "snippet": "GPT-5.4 set a new record on FrontierMath - Epoch AI\n\n# Epoch AI\n\nSubscribeSign in\n\nUpdates\n\n# GPT-5.4 set
a new record on FrontierMath\n\n### Solved one Tier 4 problem that no model had solved before\n\nEpoch AI\n\nMar 05, 2026\n\n3\n\n2\n\nShare\n\nGPT-5.4 set a new record on FrontierMath, our benchmark
of extremely challenging math problems!\n\nWe had pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%.\n\nSee below for commentary and
additional experiments.Fr", "highlights": ["GPT-5.4 set a new record on FrontierMath - Epoch AI\n\n# Epoch AI\n\nSubscribeSign in\n\nUpdates # GPT-5.4 set a new record on FrontierMath\n\n### Solved
one Tier 4 problem that no model had solved before\n\nEpoch AI Mar 05, 2026\n\n3\n\n2\n\nShare GPT-5.4 set a new record on FrontierMath, our benchmark of extremely challenging math problems! We had
pre-release access to evaluate the model. On Tiers 1\u20133, GPT-5.4 Pro scored 50%. On Tier 4 it scored 38%. See below for commentary and additional experiments.FrontierMath was funded by OpenAI, who
has exclusive access to: all 290 problems in Tiers 1\u20133; solutions to 237 of these problems; 28 of the 48 problems in Tier 4; solutions to these 28 problems. Epoch holds out the rest.On Tiers
1\u20133 GPT-5.4 Pro solved 52% of the non-held-out set and 42% of the held-out set. On Tier 4, GPT-5.4 Pro solved 25% of the non-held-out set and 55% of the held-out set. Neither of these differences
is statistically significant.GPT-5.4 Pro solved one Tier 4 problem that no model had solved before. In a preliminary analysis, it appeared to have found a preprint from 2011 which let it shortcut much
of the intended work. The problem author was unaware of this preprint.We ran GPT-5.4 (xhigh) an additional ten times on Tier 4 to get a pass@10 score. This was 38%. In one of these runs, it solved
another problem no model had solved before. This problem was by Bartosz Naskr\u0119cki, who responded as follows: Across all runs ever, 42% (20/48) of the problems in Tier 4 have now been solved at
least once.We also evaluated GPT-5.4 Pro on FrontierMath: Open Problems. It did not solve any problems. It made some novel observations on one problem, but of a form that the author had anticipated
and characterized as relatively uninteresting. More here.Check out our website for more results and commentary about FrontierMath overall! ---\n\nSubscribe\n\n3\n\n"], "published_date":
"2026-03-05T18:57:39.000", "score": null}, {"title": "FrontierMath Tier 4 | Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath", "snippet": "FrontierMath Tier 4 | Epoch AI\n\n \n\n#
FrontierMath Tier 4\n\n \n\nFrontierMath Tier 4\n\nMethodology\n\n### FrontierMath Tier 4\n\nFrontierMath is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted
and vetted by expert mathematicians. The questions cover most major branches of modern mathematics \u2013 from computationally intensive problems in number theory and real analysis to abstract
questions in algebraic geometry and category theory. Solving a typical problem requi", "highlights": ["FrontierMath Tier 4 | Epoch AI\n\n \n\n# FrontierMath Tier 4\n\n \n\nFrontierMath Tier
4\n\nMethodology\n\n### FrontierMath Tier 4 FrontierMath is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted   ...    The full FrontierMath
dataset contains 350 problems. This is split into a base set of 300 problems, which we call Tiers 1-3, and an expansion set of 50 exceptionally difficult problems, which we call Tier 4. We have made
10 problems from Tiers 1-3 public, calling this`frontiermath-2025-02-28-public`. The remaining 290 problems make up`frontiermath-2025-02-28-private`. Similarly, we have made 2 problems from Tier 4
public, calling this`frontiermath-tier-4-2025-07-01-public`, while the remaining 48 problems make up`frontiermath-tier-4-2025-07-01-private`. Unless explicitly mentioned otherwise, all the numbers on
this hub correspond to evaluations on the private sets. You can find more information about the public problems here. FrontierMath was developed with funding from OpenAI, who has exclusive access to a
subset of the benchmark. See our   ...    For FrontierMath, we recommend using the log viewer on the public questions as the best way to understand the evaluation settings (e.g. click here
for`o4-mini-2025-04-16` with high reasoning effort).   ...    This implementation is different from the code we used to run preliminary evaluations in the paper. It is also not the   ...    different
subset of FrontierMath (the 180 problems in`frontiermath-2024-11-26` vs the 290 problems in`frontiermath-2025-02-28-private`). ### Changelog 2026-01-23. We identified issues with two Tier 4 problems
that affected prior scores. In one case the issue was with our grader, so we could re-grade solutions given by models on prior runs. The models that got this problem right were: GPT-5.2 Pro, GPT-5.2
(xhigh), GPT-5.2 (high), GPT-5.2 (medium), and GPT-5 Pro. In the other case the issue was with the problem statement itself. Here we re-ran every model that had scored over 10% on Tier 4 on this one
problem. Only GPT-5.2 Pro and GPT-5.2 (high) got the corrected problem right. We adjusted the scores of all of these models accordingly. We also fixed an error in the problem statement for public
problem`PLD1` in`FrontierMath-2025-02-28-Public`. Several models had in fact been getting the right answer to the mis-stated problem (the answer was 281718171540). Since this problem set is just for
illustrative purposes, we have not updated those scores on our hub. We bumped the benchmark version number to 1.1.4 to reflect these fixes. 2026-01-22. We upgraded our Inspect dependency, and bumped
the benchmark version number to 1.1.3. 2025-12-05. We upgraded our Inspect dependency, and bumped the benchmark version number to 1.1.2. 2025-11-19. We changed our default settings to allow 2% of
samples to fail in a given run without the run as a whole   ...    2025-11-13. We increased the token budget given to models by 10\u00d7. This was in response to observing models increasingly
exceeding the token budget limit. With this change, we bumped the benchmark version number to 1.1.0. We reran a   ...    We ran this model on Fireworks for data security. We found that, when run on
public benchmarks, the model performed   ...    | gemini-3-pro-preview | FrontierMath-2025-02-28-Private | 38% (\u00b13%) | 10/290=3% |   ...    Grok 4\n\nFor`grok-4-0709`, we experienced timeouts and
network errors using the API in July 2025. As a result, as of July 2025, we evaluated Grok 4 using specific scoring rules: FrontierMath-2025-02-28-Private was evaluated using our standard settings.
The record ID is gda5UeWrA8HcbDCRuLJ56H. We used the streaming API. 1/290 was not scored due to the server not sending any response. (We allow up to 1% of samples to fail without being scored). For
FrontierMath-Tier-4-2025-07-01-Private, we used a maximum output length per request of 128,000 tokens (default is no maximum), as recommended by xAI. If any requests failed due to network errors or
timeouts, we moved the   ...    incorrect). This was due to the highly time-sensitive nature of the evaluations. | Benchmark | Accuracy | Samples with API errors | Run ID |\n| --- | --- | --- | --- |
| FrontierMath-Tier-4-2025-07-01-Private | 2% (\u00b12%) | 8 out of 48 (16%) | QxtNUmV2L34UyrySmBLTbv | xAI compensated us for this evaluation and provided compute credits. We signed"],
"published_date": null, "score": null}]
```

```json
{
  "query": "\"GPT-5.5\" OR \"Claude Mythos\" FrontierMath evaluation Epoch AI April 2026"
}
```

### 📋 Result

```
{"query": "\"GPT-5.5\" OR \"Claude Mythos\" FrontierMath evaluation Epoch AI April 2026", "results": [{"title": "AI Model Benchmarks Apr 2026 | Compare GPT-5, Claude 4.5, Gemini 2.5, Grok 4 | LM
Council", "url": "https://lmcouncil.ai/benchmarks", "snippet": "18 benchmarks - the world's most-followed benchmarks, curated by [AI Explained](https://www.youtube.com/@aiexplained-official), author
of [SimpleBench](https://simple-bench.com)\nIndependently-run benchmarks by Epoch, Scale and others, so may not match self-reported scores by AI orgs.\n| Models (no tools) | Score |
|\n|---|---|---|\n| 1 | Gemini 3 Pro Preview | 37.52% \u00b11.90 |\n| 2 | Claude Opus 4.6 (max) | 34.44% \u00b11.86 |\n| 3 | GPT-5 Pro | 31.64% \u00b11.82 |\n| 4 | GPT-5.2 | 27.80% \u00b11.76 |\n| 5 |
GPT-5 (Aug", "api_data": null, "hint": null}, {"title": "FrontierMath Benchmark 2026: 1 LLM scores | BenchLM.ai", "url": "https://benchlm.ai/benchmarks/frontierMath", "snippet": "An expert-level
mathematical reasoning benchmark by Epoch AI featuring original, research-level problems created by mathematicians including IMO gold medalists and Fields Medal recipients. Problems require deep
creativity and multi-step reasoning.\nAs of April 10, 2026, [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) leads the FrontierMath leaderboard with 50%.\nYear\n2024\nTasks\n350 original research-
level math problems\nFormat\nOpen-ended mathematical reasoning with tool access\nDifficulty\nResea", "api_data": null, "hint": null}, {"title": "Claude Mythos Preview: Inside Anthropic's Most Capable
Frontier Model | TechPlanet", "url": "https://techplanet.today/post/claude-mythos-preview-inside-anthropics-most-capable-frontier-model", "snippet": "A New Era of AI Capabilities\nOn April 7, 2026,
Anthropic released the System Card for Claude Mythos Preview, providing unprecedented transparency into one of the most advanced AI models ever created. This comprehensive technical document reveals
not just the capabilities of the model, but also the rigorous safety evaluation processes that accompany frontier AI development.\nUnprecedented Performance Across Benchmarks\nClaude Mythos Preview
represents a significant leap forward in AI capabilities. ", "api_data": null, "hint": null}, {"title": "Best AI Models April 2026: Ranked by Benchmarks", "url":
"https://www.buildfastwithai.com/blogs/best-ai-models-april-2026", "snippet": "Best AI Models April 2026: Every Major Release Ranked by Real Benchmarks\nTwelve significant AI model releases in a
single week. That happened in March 2026. Not a month -- a week.\nI tracked every launch, ran the benchmark numbers, and compared the specs across GPT-5.4, Gemini 3.1 Pro, Claude Opus 4.6, GLM-5,
DeepSeek V4, Llama 4, and a dozen others. The short version: the gap between open-source and proprietary AI has nearly closed. The longer version is what this guide is for.\nLLM Stats, which ",
"api_data": null, "hint": null}, {"title": "New record on FrontierMath Tier 4 - Epoch AI - Substack", "url": "https://epochai.substack.com/p/new-record-on-frontiermath-tier-4", "snippet": "New record
on FrontierMath Tier 4\nGPT-5.2 Pro (manual run) scored 31%, a substantial jump over the previous high score of 19%.\nWe evaluated GPT-5.2 Pro manually on the ChatGPT website. We did this after
encountering timeout issues with the API in our scaffold. We\u2019re working to resolve these issues, but a manual evaluation seemed worthwhile in the meantime.\nPrior to this run, 13 problems from
Tier 4 had been solved by any model ever. GPT-5.2 Pro solved 11 of those, and 4 more besides. Its total f", "api_data": null, "hint": null}, {"title": "LLM News Today (April 2026) \u2013 AI Model
Releases", "url": "https://llm-stats.com/ai-news", "snippet": "![Claude Mythos Preview: Benchmarks, Pricing & Project Glasswing](/_next/image?url=%2Fblog%2Fclaude-mythos-preview-
launch%2Fbanner.webp&w=2048&q=75)\nClaude Mythos Preview: Benchmarks, Pricing & Project Glasswing\nAnthropic's unreleased Claude Mythos Preview scores 93.9% on SWE-bench Verified, 94.6% on GPQA
Diamond, and found thousands of zero-day vulnerabilities across every major OS and browser.\n![Jonathan Chavez](/_next/image?url=%2Fblog%2Fjona.jpg&w=48&q=75)\nYour daily source for LLM news, ope",
"api_data": null, "hint": null}, {"title": "GPT-5.5 Review (Spud) 2026: Everything We Know About OpenAI's Most Powerful Model Yet - PrimeAIcenter", "url": "https://primeaicenter.com/gpt-5-5-review/",
"snippet": "On March 24, 2026, The Information broke a story that reset the entire AI landscape: OpenAI had completed pre-training on a new model internally codenamed \u201cSpud.\u201d CEO Sam Altman
told employees it was a \u201cvery strong model\u201d that could \u201creally accelerate the economy.\u201d OpenAI President Greg Brockman went further, describing it on the Big Technology podcast as
the result of \u201ctwo years worth of research\u201d that would set a new benchmark for AI models \u2014 coining the evocative phrase \u201cbig model smell\u201d to c", "api_data": null, "hint":
null}, {"title": "GPT-5.4 Pro Cracks Open Math Problem", "url": "https://winbuzzer.com/2026/03/24/gpt-54-pro-solves-open-math-problem-epoch-ai-frontiermath-xcxwbn/", "snippet": "- Breakthrough:
OpenAI\u2019s GPT-5.4 Pro solved an open mathematical problem that had resisted human efforts since 2019, verified independently by Epoch AI.\n- Broader Capability: Three other frontier AI models from
Anthropic, Google, and OpenAI also solved the same problem, suggesting shared mathematical reasoning capacity.\n- Benchmark Progress: FrontierMath scores jumped from 5% under GPT-4 in 2024 to 50%
under GPT-5.4 Pro in March 2026.\n- Expert Reaction: Mathematicians remain divided, with Terenc", "api_data": null, "hint": null}, {"title": "New AI Model Releases News | April, 2026 (STARTUP
EDITION)", "url": "https://blog.mean.ceo/new-ai-model-releases-news-april-2026/", "snippet": "TL;DR: New AI Model Releases News, April, 2026\nApril 2026 introduced groundbreaking AI tools, including
Anthropic\u2019s Claude Mythos 5 with 10 trillion parameters for advanced cybersecurity and coding, and the accessible Capabara model. Google DeepMind\u2019s Gemini 3.1 adds real-time voice and image
analysis, while Google\u2019s compression algorithm slashes AI costs by reducing memory needs by six times.\n\u2022 Entrepreneurs can use Gemini 3.1 for customer service and lightweight AI systems for
affordability.\n\u2022", "api_data": null, "hint": null}, {"title": "FrontierMath Tier 4 | Epoch AI", "url": "https://epoch.ai/benchmarks/frontiermath", "snippet":
"[FrontierMath](https://epoch.ai/frontiermath) is a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover
most major branches of modern mathematics \u2013 from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a
typical problem requires multiple hours of effort from a researcher in the relevant branch of mathematics, a", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Key findings from this round:

1. **Manifold Market**: "What will be the best FrontierMath Tier 4 score by Dec 31, 2026?" - This is a numeric market, showing 0.11 probability on April 7. But this is a different question format (numeric, by end of year). Not directly comparable but shows market sentiment.

2. **No new Tier 4 evaluation since March 5, 2026**: The Epoch AI brief from April 2 summarizes March activities and mentions the GPT-5.4 record but no newer evaluation.
   
3. **BenchLM.ai reports GPT-5.4 Pro at 50% on overall FrontierMath as of April 10**, though this covers the full 350-problem set rather than Tier 4 specifically.

4. **Claude Mythos Preview** released its system card on April 7 with strong performance on SWE-bench Verified and GPQA Diamond, but there's no indication it's been tested on FrontierMath Tier 4 by Epoch AI yet.

5. **GPT-5.5 "Spud" finished pre-training March 24** and is currently in post-training with no evaluation results available.

6. **Epoch AI's FrontierMath leaderboard shows OpenAI's funding influence**—they have pre-release access to OpenAI models and have tested Gemini and Grok as well, but the Tier 4 results are dominated by GPT models with minimal representation from competitors.

For YES to occur before May 1, a new model needs to be evaluated on Tier 4 and score at least 41.67%, and GPT-5.5 "Spud" is the main candidate to watch.

Looking at the actual contenders: GPT-5.5 "Spud" is still in post-training and unlikely to be ready by May 1 given the typical timeline. Claude Mythos is very capable but Epoch AI has structural bias toward OpenAI models and hasn't evaluated any Claude model on Tier 4. Gemini 3.1 Pro is already released but even with significant improvement from Gemini 3 Pro's 19%, it probably won't reach 40%. Other potential models like DeepSeek V4 or Llama 4 are unlikely to get Tier 4 evaluation from Epoch AI.

The only realistic path to YES is if Epoch AI gets pre-release access to GPT-5.5 and evaluates it on Tier 4 before May 1. But the timing is extremely tight—if post-training takes 4-6 weeks from the March 24 completion, that puts release at late April to early May. Even assuming Epoch AI would evaluate it given their OpenAI access agreements, the question remains whether GPT-5.5 can jump from GPT-5.4's 38% to 40%, which requires solving just 2 more problems.

Looking at the progression from 19% to 31% to 38%, the next version could plausibly reach 42-45%, so capability-wise it's feasible. But timing is the real bottleneck. I'm estimating roughly 10-15% chance that GPT-5.5 gets released and evaluated before May 1, with about 50-60% odds it scores ≥40% if evaluated, plus maybe 3-5% for other models hitting the threshold. That puts the overall probability around 13-17%.

I should also factor in whether Epoch AI might re-evaluate existing models with different approaches.

Actually, wait—the question closes today but resolves May 1, so there's still a window. The benchmark page was updated today, though that could be routine. I don't see any new Tier 4 results yet, but there's a chance an evaluation is already underway or results haven't been published. Accounting for these possibilities, I'm settling on around 15-20% probability. Looking at the evaluation cadence more carefully, there's roughly a two-month gap between assessments, with the last one in early March. That would put the next evaluation around early May, cutting it very close to the deadline. The key question is whether OpenAI has already given Epoch AI early access to GPT-5.5 or a successor model, similar to what happened with GPT-5.4.

Thinking about this more systematically through base rates: Epoch AI runs about 5-6 Tier 4 evaluations annually, and while new records get set fairly often in the AI space, the specific confluence of having a capable new model, getting it evaluated by this particular organization on this particular benchmark before May 1st, is a tighter constraint. I'm settling on 18% as my estimate.

Now I'm examining whether there's actually a model in development that could plausibly hit 40% or higher. GPT-5.5 would be the obvious candidate given the performance trajectory, but the timing is precarious—based on OpenAI's release cadence of every 2-3 months, GPT-5.5 would likely arrive around May-June 2026, right at the boundary. The pretraining for GPT-5.5 finished in late March, so the question becomes whether post-training could wrap up quickly enough for an Epoch evaluation before the deadline. Looking at the timeline more carefully—pre-training finished March 24, and if post-training takes 4-6 weeks, that puts us at late April or early May. There's a real possibility Epoch AI could get early access and publish results before the May 1 deadline, similar to what happened with GPT-5.4. But there's also uncertainty around whether post-training finishes on time or if GPT-5.5 will show the kind of improvement needed to cross 40%. I'm settling on 20% as my estimate.

## 💬 Response

Now let me do some quantitative analysis to understand the scoring dynamics.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Analysis of FrontierMath Tier 4 scoring\n# 48 private problems total\n\nimport numpy as np\n\n# Current best scores (exact fractions)\nscores = {\n    \"Gemini 3 Pro Preview (Nov 2025)\": 9/48,    # ~19%\n    \"GPT-5.2 Pro (Jan 2026)\": 15/48,            # ~31%\n    \"GPT-5.4 Pro (Mar 2026)\": 18/48,            # ~37.5%, reported as 38%\n}\n\n# Print exact fractions\nfor model, score in scores.items():\n    print(f\"{model}: {score:.4f} ({score*100:.1f}%) = {int(score*48)}/48\")\n\nprint()\n\n# Threshold analysis\nthreshold = 0.40\nmin_correct = int(np.ceil(threshold * 48))\nprint(f\"Threshold: {threshold*100}%\")\nprint(f\"Minimum correct answers needed: {min_correct}/48 = {min_correct/48*100:.2f}%\")\nprint(f\"Current best (GPT-5.4 Pro): 18/48 = {18/48*100:.2f}%\")\nprint(f\"Gap: need {min_correct - 18} more correct answers\")\nprint()\n\n# Pass@kitchen-sink: 20/48 problems solved across all models\nprint(f\"Pass@kitchen-sink (all models, all runs): 20/48 = {20/48*100:.2f}%\")\nprint(f\"This means 20 unique problems have been solved at least once\")\nprint()\n\n# Progression analysis\nfrom datetime import datetime\ndates = [datetime(2025, 7, 1), datetime(2025, 11, 18), datetime(2026, 1, 23), datetime(2026, 3, 5)]\nscores_list = [2, 19, 31, 38]  # reported percentages\n\nprint(\"Progression of Tier 4 scores:\")\nfor d, s in zip(dates, scores_list):\n    print(f\"  {d.strftime('%Y-%m-%d')}: {s}%\")\n\n# Time between evaluations\nfor i in range(1, len(dates)):\n    delta = (dates[i] - dates[i-1]).days\n    score_jump = scores_list[i] - scores_list[i-1]\n    print(f\"  Gap: {delta} days, score jump: {score_jump}pp\")\n\nprint()\n# Time from last evaluation to deadline\ndeadline = datetime(2026, 5, 1)\nlast_eval = datetime(2026, 3, 5)\ntoday = datetime(2026, 4, 12)\nprint(f\"Days from last eval to deadline: {(deadline - last_eval).days}\")\nprint(f\"Days from today to deadline: {(deadline - today).days}\")\nprint(f\"Days since last eval: {(today - last_eval).days}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Gemini 3 Pro Preview (Nov 2025): 0.1875 (18.8%) = 9/48\nGPT-5.2 Pro (Jan 2026): 0.3125 (31.2%) = 15/48\nGPT-5.4 Pro (Mar 2026): 0.3750 (37.5%) = 18/48\n\nThreshold:
40.0%\nMinimum correct answers needed: 20/48 = 41.67%\nCurrent best (GPT-5.4 Pro): 18/48 = 37.50%\nGap: need 2 more correct answers\n\nPass@kitchen-sink (all models, all runs): 20/48 = 41.67%\nThis
means 20 unique problems have been solved at least once\n\nProgression of Tier 4 scores:\n  2025-07-01: 2%\n  2025-11-18: 19%\n  2026-01-23: 31%\n  2026-03-05: 38%\n  Gap: 140 days, score jump: 17pp\n
Gap: 66 days, score jump: 12pp\n  Gap: 41 days, score jump: 7pp\n\nDays from last eval to deadline: 57\nDays from today to deadline: 19\nDays since last eval: 38\n", "stderr": "", "duration_ms": 174}
```

## 💭 Thinking

Now I have a very clear picture. Let me synthesize everything and prepare my reflection.

Key facts:
1. **Current best**: GPT-5.4 Pro scored 18/48 = 37.5% on Tier 4 (reported as 38%), evaluated March 5, 2026
2. **Threshold**: 40.0%, which requires 20/48 = 41.67% (need 2 more correct problems)
3. **Pass@kitchen-sink**: 20/48 = 41.67% across all models and all runs ever
4. **Time remaining**: 19 days (April 12 to May 1)


5. **Evaluation frequency**: Every 41-140 days, with decreasing intervals

The score progression shows a clear pattern of diminishing returns—jumping from 2% to 19% to 31% to 38%—with each improvement getting smaller. GPT-5.5 "Spud" finished pre-training on March 24 and is still in post-training, while Claude Mythos launched as a preview on April 7 but hasn't been evaluated on Tier 4 yet, and Gemini 3.1 Pro released in April though its predecessor only achieved lower scores.

Now I'm mapping out the probability pathways. For GPT-5.5 to be evaluated before May 1, I need to estimate the chance its post-training wraps up by late April—roughly 25%—then factor in Epoch AI's likelihood of running the evaluation given their OpenAI connections and pre-release access, around 70%, and the probability it scores 40% or higher based on the trend of 7+ percentage point improvements per generation, which I'd put at 55%.

For other models like Claude Mythos or Gemini 3.1, Epoch AI historically hasn't prioritized non-OpenAI models on Tier 4, so that's only about 10%, and even if evaluated, the scores would likely fall short at 20% probability. There's also a small chance something's already been evaluated but the results are under embargo, maybe 5%, with a 40% shot at hitting the threshold if that's the case.

Combining these paths gives me a total probability around 14%.

But I should probably dial back some of these estimates—I might be too optimistic. Let me reconsider the GPT-5.5 timeline more carefully. If pretraining wrapped up March 24, and post-training typically takes 4-8 weeks based on the pattern between GPT-5.2 and GPT-5.4, that puts us looking at an April completion window.

For evaluation by May 1, I'm looking at a narrow window—best case late April, worst case mid-May or beyond. That feels like maybe 15-20% probability for readiness and evaluation by May 1. If the model scores 40% or higher given it's evaluated, I'd estimate 50-60% odds, which gives me roughly 8-12% from this path alone.

Combining all the paths I've considered, I'm landing around 12-16% total, so I'll go with 15% as my estimate. Though I should note that the Manifold market data from April 7 showing 0.11 for Tier 4 performance by year-end adds another data point to consider, even if it's not directly comparable since that's a numeric market.

Actually, reconsidering the specific May 1 deadline, I think 15-18% is more appropriate, so I'll adjust to 17%. I'm also wondering whether a GPT-5.4 variant with tools or a different approach could potentially break through—but the pass@10 for GPT-5.4 at xhigh was already 38%, so without a fundamentally new evaluation method, the same model family probably won't exceed that threshold.

I'll stick with 17% as my final estimate.

## 💬 Response

Now I have a comprehensive picture. Let me run my reflection and finalize the forecast.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Current record is 38% (18/48), threshold requires 20/48 (41.67%) - need 2 more problems solved in a single run",
      "logit": -0.3,
      "confidence": 0.9
    },
    {
      "description": "Pass@10 for GPT-5.4 (xhigh) was also 38%, suggesting current architecture plateau at this level",
      "logit": -0.8,
      "confidence": 0.8
    },
    {
      "description": "GPT-5.5 'Spud' pre-training completed March 24, still in post-training - could be ready by late April but timeline is very tight",
      "logit": 0.5,
      "confidence": 0.5
    },
    {
      "description": "Only 19 days remain until resolution deadline (May 1, 2026)",
      "logit": -1,
      "confidence": 0.95
    },
    {
      "description": "No new Tier 4 evaluation has been published since March 5 (38 days ago)",
      "logit": -0.5,
      "confidence": 0.85
    },
    {
      "description": "Epoch AI has pre-release access agreements with OpenAI and evaluates new models quickly",
      "logit": 0.4,
      "confidence": 0.7
    },
    {
      "description": "Score progression shows rapid improvement: 2% \u2192 19% \u2192 31% \u2192 38% in ~8 months, though jumps are diminishing (17pp \u2192 12pp \u2192 7pp)",
      "logit": 0.3,
      "confidence": 0.7
    },
    {
      "description": "20/48 problems already solved across all models ever (pass@kitchen-sink = 42%), so the problems ARE solvable",
      "logit": 0.2,
      "confidence": 0.8
    },
    {
      "description": "Claude Mythos Preview released April 7 but Epoch AI has never evaluated Claude models on Tier 4",
      "logit": -0.3,
      "confidence": 0.7
    },
    {
      "description": "Epoch AI primarily evaluates OpenAI models on Tier 4 (funded by OpenAI), limiting candidate models",
      "logit": -0.4,
      "confidence": 0.8
    }
  ],
  "tentative_estimate": {
    "logit": -1.5,
    "probability": 0.18
  },
  "assessment": "The core tension is between (a) the rapid pace of AI capability improvement and (b) the extremely tight timeline. The current best score is 38% (18/48), and reaching 40% requires 20/48. This is a small absolute gap (2 problems) but represents a meaningful capability jump that even pass@10 couldn't bridge for the current best model.\n\nThe most likely YES path is GPT-5.5 being evaluated by Epoch AI before May 1. Pre-training completed March 24, so if post-training takes 4-6 weeks (finishing mid-April to early May), there's a plausible but uncertain window. Epoch AI has demonstrated pre-release access to OpenAI models.\n\nThe most likely NO scenario: GPT-5.5 isn't ready until after May 1, and no other model is evaluated on Tier 4 in the meantime. Given that the last evaluation was March 5 and evaluations happen roughly every 2 months, the next one might not arrive until May.\n\nCounter-argument to my estimate: The AI ecosystem is moving extremely fast, with multiple frontier models released in April 2026. However, the specific constraint is that Epoch AI must evaluate the model on Tier 4 specifically - this is a narrow bottleneck. They can't just use any lab's self-reported scores.",
  "calibration_notes": "Base rate for new Tier 4 evaluations: ~4-5 per year based on history. P(evaluation in next 19 days) \u2248 19/365 \u00d7 5 \u2248 26%, but conditional on a sufficiently capable model existing. Status quo is NO - if nothing changes (no new model evaluated), question resolves No. The 18% probability accounts for the possibility that GPT-5.5 or another model is evaluated in this narrow window AND scores high enough.",
  "key_uncertainties": "1. When will GPT-5.5 'Spud' post-training be complete? This is the biggest unknown.\n2. Will Epoch AI evaluate any non-OpenAI model (like Claude Mythos) on Tier 4?\n3. Could there be an evaluation already underway that hasn't been published yet?\n4. How much capability improvement will GPT-5.5 show on this specific benchmark?",
  "update_triggers": "- Announcement of GPT-5.5 release or Epoch AI pre-release evaluation would push toward 50-60%\n- Announcement of Epoch AI evaluating Claude Mythos on Tier 4 would push toward 25-30%\n- Confirmation that GPT-5.5 post-training won't be done until May+ would push toward 5-8%",
  "tool_audit": "Useful: fetch_url (Epoch AI leaderboard and Substack), search_exa (detailed GPT-5.4 results), web_search (model release timeline, Claude Mythos), manifold_price (market context), execute_code (quantitative analysis). Empty/failed: polymarket_price (no markets found), asknews tools (hit API quota limit). No actual tool failures beyond the AskNews quota issue.",
  "process_reflection": "The research flow worked well for this question. I was able to piece together the full picture from multiple sources. The key friction point was that the Epoch AI leaderboard page didn't render the full chart (JavaScript-dependent), but the Exa search and Substack posts filled in the gaps. The AskNews quota limit was frustrating but not critical - I had enough information from other sources. The execute_code tool was helpful for the quantitative analysis of scoring thresholds and timelines."
}
```

### 📋 Result

```
{"factor_count": 10, "factor_sum": -1.915, "tentative_logit": -1.5, "logit_gap": 0.41500000000000004, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Current record is 38% (18/48),
threshold requires 20/48 (41.67%) - need 2 more problems solved in a single run", "logit": -0.3, "confidence": 0.9, "effective_logit": -0.27}, {"description": "Pass@10 for GPT-5.4 (xhigh) was also
38%, suggesting current architecture plateau at this level", "logit": -0.8, "confidence": 0.8, "effective_logit": -0.6400000000000001}, {"description": "GPT-5.5 'Spud' pre-training completed March 24,
still in post-training - could be ready by late April but timeline is very tight", "logit": 0.5, "confidence": 0.5, "effective_logit": 0.25}, {"description": "Only 19 days remain until resolution
deadline (May 1, 2026)", "logit": -1.0, "confidence": 0.95, "effective_logit": -0.95}, {"description": "No new Tier 4 evaluation has been published since March 5 (38 days ago)", "logit": -0.5,
"confidence": 0.85, "effective_logit": -0.425}, {"description": "Epoch AI has pre-release access agreements with OpenAI and evaluates new models quickly", "logit": 0.4, "confidence": 0.7,
"effective_logit": 0.27999999999999997}, {"description": "Score progression shows rapid improvement: 2% \u2192 19% \u2192 31% \u2192 38% in ~8 months, though jumps are diminishing (17pp \u2192 12pp
\u2192 7pp)", "logit": 0.3, "confidence": 0.7, "effective_logit": 0.21}, {"description": "20/48 problems already solved across all models ever (pass@kitchen-sink = 42%), so the problems ARE solvable",
"logit": 0.2, "confidence": 0.8, "effective_logit": 0.16000000000000003}, {"description": "Claude Mythos Preview released April 7 but Epoch AI has never evaluated Claude models on Tier 4", "logit":
-0.3, "confidence": 0.7, "effective_logit": -0.21}, {"description": "Epoch AI primarily evaluates OpenAI models on Tier 4 (funded by OpenAI), limiting candidate models", "logit": -0.4, "confidence":
0.8, "effective_logit": -0.32000000000000006}], "dominant_factor": "Only 19 days remain until resolution deadline (May 1, 2026)", "dominant_effective_logit": -0.95, "factor_implied_probability":
0.12842016947472976, "tentative_probability": 0.18, "gap_pp": 5.157983052527023, "sources": ["[(Metaculus) Will any model evaluated by Epoch AI score at least 40.0% on FrontierMath Tier 4 before May
1, 2026?](https://www.metaculus.com/questions/43134)", "[FrontierMath Tier 4](https://epoch.ai/benchmarks/frontiermath-tier-4/)", "[New record on FrontierMath Tier
4](https://epochai.substack.com/p/new-record-on-frontiermath-tier-4)", "[FrontierMath Tier 4](https://epoch.ai/benchmarks/frontiermath)", "[FRONTIERMATH: A BENCHMARK FOR EVALUATING ADVANCED
MATHEMATICAL REASONING IN AI](https://arxiv.org/pdf/2411.04872)", "[(Manifold) What will be the best FrontierMath Tier 4 score by Dec 31, 2026?](https://manifold.markets/Bayesian/what-will-be-the-
best-frontiermath)"], "reviewer_critique": "## Verification Summary\n\nI verified each factor against the research trace:\n\n**Factor 1: Current record is 38% (18/48), threshold requires 20/48
(41.67%)**\n\u2713 VERIFIED. The trace shows multiple sources confirming GPT-5.4 Pro scored 38% on Tier 4 (March 5, 2026), which corresponds to 18/48. The Epoch AI Substack article states: \"On Tier 4
it scored 38%.\" The agent correctly calculates that 40.0% requires at least 20/48 = 41.67%.\n\n**Factor 2: Pass@10 for GPT-5.4 (xhigh) was also 38%**\n\u2713 VERIFIED. The trace shows the Epoch AI
source stating: \"We ran GPT-5.4 (xhigh) an additional ten times on Tier 4 to get a pass@10 score. This was 38%.\"\n\n**Factor 3: GPT-5.5 'Spud' pre-training completed March 24, still in post-
training**\n\u2713 VERIFIED. Multiple trace sources confirm this, including: \"OpenAI had completed pre-training on a new model internally codenamed 'Spud.' ... confirmed by multiple sources including
The Information, which first reported the pretraining completion on March 24, 2026.\"\n\n**Factor 4: Only 19 days remain until resolution**\n\u2713 VERIFIED. Published April 12, resolves May 1. 19
days is correct.\n\n**Factor 5: No new Tier 4 evaluation since March 5 (38 days ago)**\n\u2713 VERIFIED. The trace confirms: \"The most recent updates are from March 9 and March 5, 2026, with no newer
Tier 4 evaluations since then.\" The Epoch AI benchmarks page update shows March 5 for Tier 4.\n\n**Factor 6: Epoch AI has pre-release access agreements with OpenAI**\n\u2713 VERIFIED. The trace
shows: \"We had pre-release access to evaluate the model\" from Epoch AI's announcement about GPT-5.4.\n\n**Factor 7: Score progression 2% \u2192 19% \u2192 31% \u2192 38% with diminishing jumps (17pp
\u2192 12pp \u2192 7pp)**\n\u2713 VERIFIED. The trace Python computation output confirms: \"Progression of Tier 4 scores: 2025-07-01: 2%, 2025-11-18: 19%, 2026-01-23: 31%, 2026-03-05: 38%\" with gaps
of 140/66/41 days and score jumps of 17/12/7pp.\n\n**Factor 8: 20/48 problems solved across all models ever (pass@kitchen-sink = 42%)**\n\u2713 VERIFIED. The trace shows the Epoch AI Substack article:
\"Across all runs ever, 42% (20/48) of the problems in Tier 4 have now been solved at least once.\"\n\n**Factor 9: Claude Mythos Preview released April 7 but Epoch AI has never evaluated Claude models
on Tier 4**\n\u26a0\ufe0f PARTIALLY VERIFIED. The Claude Mythos April 7 release is confirmed. The claim that Epoch AI has \"never evaluated Claude on Tier 4\" is inferred from the agent's observation:
\"I'm not seeing Claude models historically evaluated on Tier 4 benchmarks in the leaderboard data\" \u2014 this is an inference from absence in the leaderboard, not a direct statement from Epoch AI.
However, this inference appears reasonable given the OpenAI funding relationship and the trace evidence that Epoch AI \"primarily evaluates OpenAI models on Tier 4.\"\n\n**Factor 10: Epoch AI
primarily evaluates OpenAI models on Tier 4 (funded by OpenAI)**\n\u2713 VERIFIED. The trace shows: \"FrontierMath was funded by OpenAI, who has exclusive access to: all 290 problems in Tiers
1\u20133; solutions to 237 of these problems; 28 of the 48 problems in Tier 4.\" The leaderboard data in the trace shows predominantly GPT models on Tier 4.\n\n**Resolution Criteria Check**\n\u2713
The resolution criteria are present and clear: \"resolves Yes if Epoch AI publicly reports a FrontierMath Tier 4 accuracy score of 40.0% or higher for any model before May 1, 2026.\" The factors
correctly engage with this threshold requirement.\n\n**Adversarial Reasoning Check**\n\u2713 The assessment acknowledges the counterargument: \"Counter-argument to my estimate: The AI ecosystem is
moving extremely fast, with multiple frontier models released in April 2026. However, the specific constraint is that Epoch AI must evaluate the model on Tier 4 specifically - this is a narrow
bottleneck.\"\n\n**Probability Assessment**\nThe 18% estimate appears reasonable given the evidence:\n- Path 1 (GPT-5.5): ~15-25% chance ready and evaluated by May 1 \u00d7 ~50-60% chance it scores
\u226540% = ~8-15%\n- Path 2 (other models): ~10% Epoch AI evaluates \u00d7 ~20% scores high enough = ~2%\n- Path 3 (embargo/surprise): ~5% \u00d7 ~40% = ~2%\n- Total: ~12-19%\n\nThe agent's 18% sits
within this range and reflects appropriate uncertainty given the tight timeline, the narrow 2-problem gap, and the evaluation bottleneck.\n\n**No Issues Found:**\n- No hallucinated evidence\n- No
double-counting (factors address distinct aspects: current record, pass@10 plateau, GPT-5.5 timeline, time remaining, evaluation frequency, access agreements, progression, solvability, Claude
exclusion, OpenAI funding)\n- No wrong-direction factors (all logit signs match descriptions)\n- No contradictory assessment\n- Resolution criteria present and engaged with correctly"}
```

## 💬 Response

The reflection passed with all factors verified. Let me finalize my forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "The current FrontierMath Tier 4 record is 38% (18/48) by GPT-5.4 Pro, set March 5, 2026. Reaching 40.0% requires solving at least 20/48 problems (41.67%). With only 19 days until the May 1 deadline, the question hinges on whether a new model (most likely GPT-5.5 \"Spud\", whose pre-training completed March 24) will be evaluated by Epoch AI on Tier 4 in time. The pass@10 for GPT-5.4 was also 38%, suggesting the current model family has plateaued. While the AI capability frontier is advancing rapidly, the specific bottleneck is Epoch AI's evaluation process - no new Tier 4 evaluation has been published since March 5. The most plausible YES path requires GPT-5.5 post-training to complete by ~April 25 AND Epoch AI to evaluate it promptly, both of which are uncertain.",
  "logit": -1.5,
  "probability": 0.18,
  "factors": [
    {
      "description": "Current record is 38% (18/48), threshold requires 20/48 (41.67%) - need 2 more problems solved in a single run",
      "logit": -0.3,
      "confidence": 0.9
    },
    {
      "description": "Pass@10 for GPT-5.4 (xhigh) was also 38%, suggesting current architecture plateau at this level",
      "logit": -0.8,
      "confidence": 0.8
    },
    {
      "description": "GPT-5.5 'Spud' pre-training completed March 24, still in post-training - could be ready by late April but timeline is very tight",
      "logit": 0.5,
      "confidence": 0.5
    },
    {
      "description": "Only 19 days remain until resolution deadline (May 1, 2026)",
      "logit": -1,
      "confidence": 0.95
    },
    {
      "description": "No new Tier 4 evaluation has been published since March 5 (38 days ago)",
      "logit": -0.5,
      "confidence": 0.85
    },
    {
      "description": "Epoch AI has pre-release access agreements with OpenAI and evaluates new models quickly",
      "logit": 0.4,
      "confidence": 0.7
    },
    {
      "description": "Score progression shows rapid improvement: 2% to 19% to 31% to 38% in ~8 months, though jumps are diminishing (17pp to 12pp to 7pp)",
      "logit": 0.3,
      "confidence": 0.7
    },
    {
      "description": "20/48 problems already solved across all models ever (pass@kitchen-sink = 42%), so the problems ARE solvable",
      "logit": 0.2,
      "confidence": 0.8
    },
    {
      "description": "Claude Mythos Preview released April 7 but Epoch AI has never evaluated Claude models on Tier 4",
      "logit": -0.3,
      "confidence": 0.7
    },
    {
      "description": "Epoch AI primarily evaluates OpenAI models on Tier 4 (funded by OpenAI), limiting candidate models",
      "logit": -0.4,
      "confidence": 0.8
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**Forecast: 18% probability (logit: -1.5)**

Key reasoning:

- **Current state**: GPT-5.4 Pro holds the record at 38% (18/48 problems). Reaching 40.0% requires 20/48 (41.67%), meaning a model must solve 2 more problems than the current best in a single run.
- **Plateau signal**: Even with 10 attempts (pass@10), GPT-5.4 couldn't break past 38%, suggesting the current model generation has hit a ceiling.
- **Timeline is the binding constraint**: Only 19 days remain. The most likely candidate (GPT-5.5 "Spud") completed pre-training March 24 and is still in post-training. Whether it can be ready, evaluated by Epoch AI on Tier 4, and results published before May 1 is highly uncertain.
- **Evaluation bottleneck**: Epoch AI must conduct the evaluation — no other source counts. They've only done ~4-5 Tier 4 evaluations ever, and none since March 5.
- **IF a next-gen model IS evaluated**, the trend (2%→19%→31%→38%) suggests it could plausibly reach 40%+, but the probability of the evaluation happening in time is the dominant uncertainty.
