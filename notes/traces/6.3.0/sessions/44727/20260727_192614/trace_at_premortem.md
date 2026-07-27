# Reasoning Log: How many cases will Damien Charlotin's AI Hallucination Cases database record for the second half of August 2026?

*Generated: 2026-07-27T19:34:15.665150+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "Damien Charlotin AI Hallucination Cases database - how many cases per month are being added in 2026? What is the recent monthly rate of new legal decisions recorded? Total case count trajectory over 2025-2026.",
  "context": "The database at damiencharlotin.com/hallucinations tracks legal decisions where generative AI produced hallucinated content (fake citations). It reports 1730 cases identified so far as of ~July 2026. I need the rate of new cases being added per half-month, and how many cases had dates in recent months (e.g., first half of August, July 2026, June 2026). Need to understand the growth trend.",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'Damien Charlot...th trend.', 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Damien Charlotin AI Hallucination Cases database - how many cases per month are being added in 2026? What is the recent monthly rate of new legal decisions recorded? Total case count trajectory 2025-2026, and monthly counts for June, July, August 2026.",
      "context": "The database at damiencharlotin.com/hallucinations tracks legal decisions where generative AI produced hallucinated content (fake citations). It reports 1730 cases identified so far as of ~July 2026. I need the rate of new cases per month/half-month, and how many cases had dates in recent months. The question asks how many cases will have a date after Aug 15, 2026 and before Sep 1, 2026 (second half of August 2026). Note there is reporting lag - cases get added to the database weeks/months after their decision date.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Damien Charlotin AI Hallucination Cases database - how many cases per month are being added in 2026? What is the recent monthly rate of new legal decisions recorded? Total case
count trajectory 2025-2026, and monthly counts for June, July, August 2026.", "entry": {"slug": "damien-charlotin-ai-hallucination-cases-database-h-3d2ec8b8", "query": "Damien Charlotin AI
Hallucination Cases database - how many cases per month are being added in 2026? What is the recent monthly rate of new legal decisions recorded? Total case count trajectory 2025-2026, and monthly
counts for June, July, August 2026.", "answer": "I've completed the research. Here's a summary of the key findings on the Damien Charlotin AI Hallucination Cases database:\n\n## Key
findings\n\n**Total-count trajectory (2025\u20132026):**\n- ~200 (mid-2025) \u2192 719 (Jan 2026) \u2192 1,227 (early Apr) \u2192 1,458 (May 22) \u2192 1,598 (Jun 9) \u2192 1,668 (Jul 2) \u2192 1,769
(Jul 17) \u2192 **~1,809 on the live site (late July 2026)**\n- The context figure of 1,730 corresponds to ~early-to-mid July 2026.\n\n**Monthly rate of new cases:**\n- Accelerated from
~75\u201385/month (late 2025) to ~169/month (Jan\u2013Apr 2026) and ~185\u2013190/month (Apr\u2013Jun 2026)\n- July 2026 net additions oscillated ~90\u2013200/month (~3\u20137/day)\n- Charlotin's own
stated pace: **~5 cases/day (~150/month)**\n- The rate appears **plateaued at a high level** (~150\u2013190/month), not still accelerating.\n\n**Critical insight for the August 2026 question:**\nThe
database is dated by **decision date**, not entry date, with a substantial **reporting lag** (\"decisions from pleadings a few months past\"). Since today is **July 27, 2026**, the target window (Aug
15\u2013Sep 1, 2026) is entirely in the **future** \u2014 essentially **zero** such cases exist yet. When eventually backfilled, a saturated half-month bucket at current rates would hold roughly
**~75\u201395 cases**, but any observation shortly after the window closes will show **substantially fewer** because recent weeks are always undercounted until decisions propagate through legal
databases and scrapers.\n\nAll findings are cross-validated across multiple sources and delivered via the structured output with full sourcing and data points.", "sources": [{"url":
"https://www.damiencharlotin.com/hallucinations/", "title": "AI Hallucination Cases Database \u2013 Damien Charlotin", "domain": "damiencharlotin.com", "accessed_at": "2026-07-27", "snippet": "Live
database; JS-rendered page returned '1809 cases identified so far' at time of access."}, {"url": "https://artificialauthority.ai/p/hallucinations-case-database-faq", "title": "Hallucinations Case
Database - FAQ - by Damien Charlotin", "domain": "artificialauthority.ai", "accessed_at": "2026-07-27", "snippet": "Author's FAQ: pre-2025 ~2-3 cases/month; Feb 2026 edit states ~5 cases/day; notes
lag in judicial times, decisions from pleadings a few months past; database is an undercount."}, {"url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit", "title": "AI Hallucination Cases: The
1,598-Case Sanctions Tracker | HAQQ", "domain": "haqq.ai", "accessed_at": "2026-07-27", "snippet": "As of June 9, 2026 the database identified 1,598 cases; ~200 a year ago; record penalty ~$109,700;
May 22 = 1,458 cases."}, {"url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/", "title": "Latest AI Hallucination Rates & Benchmarks (July 2026) | suprmind", "domain":
"suprmind.ai", "accessed_at": "2026-07-27", "snippet": "Legal cases updated to 1,769 as of July 17, 2026; snapshots Jan ~719, early Apr 1,227, Jun 9 1,598; trajectory 10 (2023) \u2192 37 (2024) \u2192
73 (first 5 months 2025)."}, {"url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026", "title": "1,600+ AI Hallucination Cases: What Every Law Firm Should Learn | LegalAI Space",
"domain": "legalaispace.com", "accessed_at": "2026-07-27", "snippet": "As of 2 July 2026 the database holds 1,668 cases; US 1,163; UK 59; responsible party a practising lawyer in 653."}, {"url":
"https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026", "title": "1,227 Fabricated Citations and Counting | PlatinumIDS Blog", "domain": "blog.platinumids.com", "accessed_at":
"2026-07-27", "snippet": "Count 1,227 (April 2026); was 200 a year ago; 719 in January."}, {"url": "https://www.yahoo.com/news/ai-hallucinations-court-documents-growing-103301810.html", "title": "AI
hallucinations in court documents are a growing problem", "domain": "yahoo.com", "accessed_at": "2026-07-27", "snippet": "Charlotin's data shows fake citations growing since 2023; most cases US;
increasingly made by lawyers not laypeople."}], "key_facts": ["Total cases in the Charlotin AI hallucination database grew from ~200 (mid-2025) to 719 (Jan 2026), 1,227 (early Apr 2026), 1,458 (May
22), 1,598 (Jun 9), 1,668 (Jul 2), 1,769 (Jul 17), and ~1,809 on the live site in late July 2026.", "The context figure of 1,730 cases corresponds to approximately early-to-mid July 2026.", "Net
monthly addition rate accelerated from ~75\u201385/month (late 2025) to ~169/month (Jan\u2013Apr 2026) and ~185\u2013190/month (Apr\u2013Jun 2026), then ranged ~90\u2013200/month in July 2026 \u2014
roughly plateaued at ~150\u2013190/month.", "Charlotin's own stated pace (Feb 2026 FAQ) is ~5 cases/day, ~35/week, ~150/month.", "Cases are dated by DECISION date, not database-entry date, and there
is a multi-week-to-multi-month reporting lag ('decisions from pleadings a few months past').", "As of July 27, 2026, cases with decision dates Aug 15\u2013Sep 1, 2026 are in the future and essentially
zero exist yet in the database.", "A fully-backfilled half-month bucket at current rates would eventually hold roughly ~75\u201395 cases (half the ~150\u2013190/month rate), but early observations
undercount recent weeks due to lag.", "US cases dominate (~1,163\u20131,219, ~65\u201369% of total); UK ~59; practicing lawyers are the majority of responsible parties (653 of ~1,668 as of Jul 2,
2026).", "Record single-matter penalty is ~$109,700; the database is explicitly described as 'necessarily an undercount.'", "Cases are added via internet referrals, automated scrapers/bots, and
keyword searches in legal databases; the author relies on court findings, not independent judgment."], "data_points": [{"metric": "Total database cases (mid-2025)", "value": 200.0, "unit": "cases",
"as_of": "2025-06-30", "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"}, {"metric": "Total database cases (January 2026)", "value": 719.0, "unit": "cases", "as_of": "2026-01-15",
"source_url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026"}, {"metric": "Total database cases (early April 2026)", "value": 1227.0, "unit": "cases", "as_of": "2026-04-05",
"source_url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026"}, {"metric": "Total database cases (May 22, 2026)", "value": 1458.0, "unit": "cases", "as_of": "2026-05-22",
"source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"}, {"metric": "Total database cases (June 9, 2026)", "value": 1598.0, "unit": "cases", "as_of": "2026-06-09", "source_url":
"https://www.haqq.ai/blog/ai-legal-hallucination-audit"}, {"metric": "Total database cases (July 2, 2026)", "value": 1668.0, "unit": "cases", "as_of": "2026-07-02", "source_url":
"https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026"}, {"metric": "Total database cases (July 17, 2026)", "value": 1769.0, "unit": "cases", "as_of": "2026-07-17", "source_url":
"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"}, {"metric": "Total database cases (live site, late July 2026)", "value": 1809.0, "unit": "cases", "as_of": "2026-07-27", "source_url":
"https://www.damiencharlotin.com/hallucinations/"}, {"metric": "Net addition rate Jan\u2013Apr 2026", "value": 169.0, "unit": "cases/month", "as_of": "2026-04-05", "source_url":
"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"}, {"metric": "Net addition rate Apr\u2013Jun 2026", "value": 187.0, "unit": "cases/month", "as_of": "2026-06-09", "source_url":
"https://www.haqq.ai/blog/ai-legal-hallucination-audit"}, {"metric": "Net addition rate July 2\u201317, 2026", "value": 200.0, "unit": "cases/month equivalent", "as_of": "2026-07-17", "source_url":
"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"}, {"metric": "Author's stated pace (Feb 2026 FAQ)", "value": 5.0, "unit": "cases/day", "as_of": "2026-02-15", "source_url":
"https://artificialauthority.ai/p/hallucinations-case-database-faq"}, {"metric": "Implied eventual saturated count for a half-month decision-date bucket at current rates", "value": 85.0, "unit":
"cases (range ~75\u201395)", "as_of": "2026-07-27", "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"}, {"metric": "US share of total cases (July 2, 2026)", "value": 1163.0,
"unit": "cases (of ~1668)", "as_of": "2026-07-02", "source_url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026"}, {"metric": "Record single-matter penalty", "value": 109700.0,
"unit": "USD", "as_of": "2026-06-09", "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"}], "created_at": "2026-07-27T19:30:24.168674Z", "updated_at": "2026-07-27T19:30:24.168674Z",
"stale_after": "2026-07-28T01:30:24.168674Z", "state": "fresh", "revision_history": [], "session_id": "943aa63e-d701-4029-9eec-9375d9b8c439", "follow_up_count": 0}, "is_follow_up": false}],
"successful_count": 1, "failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: Damien Charlotin AI Hallucination Cases database - how many cases per month are being added in 2026? What is the recent monthly rate of new legal decisions recorded? Total case count trajectory 2025-2026, and monthly counts for June, July, August 2026.

*Generated: 2026-07-27T19:30:24.165361+00:00*


## 💬 Response

I'll research the Damien Charlotin AI Hallucination Cases database to understand the case addition rate and trajectory.

## 🔧 Tool: ToolSearch


```json
{
  "query": "fetch url web page",
  "max_results": 5
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "web search",
  "max_results": 5
}
```

### 📋 Result

```

```

## 💬 Response

Let me start researching the database.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.damiencharlotin.com/hallucinations/",
  "prompt": "Total number of AI hallucination cases in database, breakdown by date/month, most recent cases and their decision dates, monthly rate of new cases in 2025-2026"
}
```

### 📋 Result

```
{"url": "https://www.damiencharlotin.com/hallucinations/", "content": "Based on the content provided:\n\n## Total Cases\n**180 cases** identified so far (the text states \"1809 cases identified so
far\" but this appears to be a typo, as the context and single-digit case examples suggest the actual number is closer to 180).\n\n**Correction**: The text explicitly states \"1809 cases identified so
far\", so the database tracks **1,809 cases**.\n\n## Breakdown by Date/Month\nThe content only shows **7 specific cases** in the visible table excerpt. Without access to the full database, a complete
monthly breakdown cannot be determined from this text.\n\n## Most Recent Cases (from visible excerpt)\nAll visible cases are from **late 2025**:\n- Case involving falsified Chinese judicial materials
(trial date not specified, but appears recent)\n- Plaintiff vs. defendant case with fabricated citations (date not specified)\n- Erin Rich case with false medical record statements (date not
specified)\n- Tyrone A. Blackburn case with fabricated quotations (follows prior $5,000 sanction in Jakes v. Youngblood)\n- Emergency TRO motion with fabricated \"Corrigan v. City of Scottsdale\"
citation (date not specified)\n\nThe most precisely dated reference is **November 20, 2025** (sanctions reiterated in first case).\n\n## Monthly Rate 2025-2026\nCannot be calculated from the provided
content. The text mentions the database is \"a work in progress and will expand as new examples emerge\" but does not provide statistical breakdowns by month.\n\n---\n\n**Relevant links:**\n-
[PelAIkan automated reference checker](https://pelaikan-app.web.app/)\n- [AI 'hallucinations' are a growing problem for the legal profession](https://www.latimes.com/business/story/2025-05-22/ai-
lawyers-hallucinations-a-growing-problem-for-lawyers) (LA Times, May 22, 2025)\n- [\"AI Hallucination Cases,\" from Courts All Over the World](https://reason.com/volokh/2025/05/18/ai-hallucination-
cases-from-courts-all-over-the-world/) (Volokh Conspiracy, May 18, 2025)\n- [Artificial Authority newsletter](https://www.damiencharlotin.com/hallucinations/) (subscription for weekly case analysis)",
"title": "AI Hallucination Cases"}
```

```json
{
  "query": "Damien Charlotin AI hallucination cases database total count 2026"
}
```

### 📋 Result

```
{"query": "Damien Charlotin AI hallucination cases database total count 2026", "results": [{"title": "AI Hallucination Legal Cases: A Sanctions Tracker (2026) \u2014 GC AI", "url":
"https://gc.ai/blog/ai-hallucination-legal-cases", "snippet": "In June 2023, a New York lawyer named Steven Schwartz stood before a federal judge and tried to explain six court decisions that did not
exist. He had asked ChatGPT to find authority for his client\u2019s claim against the airline Avianca, and ChatGPT produced confident citations, complete with fabricated quotes and invented case
numbers. Judge P. Kevin Castel sanctioned Schwartz, his co-counsel, and their firm $5,000. It was the first widely reported entry in what is now a long and growing list of A", "api_data": null,
"hint": null}, {"title": "Media - Damien Charlotin", "url": "https://www.damiencharlotin.com/media/", "snippet": "Interviews, media mentions, podcasts, op-eds, and conference presentations. This page
currently includes 73 appearances.\nChinese Epoch Times article, translated from Lear Zhou's English report, mentioning Damien Charlotin as a researcher tracking more than 1,000 U.S. legal cases
involving generative AI hallucinated content from Q2 2023 to May 19, 2026. (Media metadata provided by gpt-5.5 with web search)\nHabr article on the first publicly known Russian court sanction for AI
hallucinations in a l", "api_data": null, "hint": null}, {"title": "1,227 Fabricated Citations and Counting: Inside the AI Hallucination Crisis Hitting Courts Worldwide | PlatinumIDS Blog", "url":
"https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026", "snippet": "By [Claude](https://blog.platinumids.com/author/claude) and Gemini with [Sid
Newby](https://blog.platinumids.com/author/sid-newby) | April 2026\nOne thousand two hundred and twenty-seven. That is the running count of fabricated legal citations submitted to courts worldwide by
lawyers and pro se litigants who trusted AI output they did not verify. The number was 200 a year ago. It was 719 in January. A DOJ attorney got fired over it. The Sixth Circuit just imposed $30,000
in sanctions. And the cou", "api_data": null, "hint": null}, {"title": "AI Hallucination Cases: The 1,598-Case Sanctions Tracker | HAQQ", "url": "https://www.haqq.ai/blog/ai-legal-hallucination-
audit", "snippet": "TL;DR. This page is now a tracker, not a one-off audit. As of June 9, 2026, the public AI Hallucination Cases database has identified 1,598 court cases involving AI-fabricated
citations or content, up from roughly 200 a year ago. The record penalty in a single matter is about $109,700. In June 2026 a US federal judge canceled a trial and suspended lawyers on both sides for
it. We re-verify every number on this page monthly. Last verified: June 9, 2026.\nKey facts: AI hallucination cases as of Jun", "api_data": null, "hint": null}, {"title": "1,600+ AI Hallucination
Cases: What Every Law Firm Should Learn | LegalAI Space", "url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026", "snippet": "There is a database that every lawyer using AI
should know about.\nDamien Charlotin, a legal researcher, maintains a public database tracking court decisions where AI-generated hallucinated content has been identified. As of 2 July 2026, it holds
1,668 cases \u2014 spanning multiple jurisdictions, court levels, and practitioner types. The United States dominates at 1,163; the UK sits at 59. And the responsible party is a practising lawyer in
653 of them \u2014 not just self-represented litigants.\nThat numb", "api_data": null, "hint": null}, {"title": "The 2026 Legal AI Reckoning: A Case-by-Case Breakdown of Every Major Hallucination
Incident This Year | ComplianceHub.Wiki", "url": "https://compliancehub.wiki/legal-ai-hallucination-reckoning-2026/", "snippet": "Overview\nSullivan & Cromwell\u2019s April 2026 apology to a federal
bankruptcy judge was the incident that made international headlines. But it was far from an isolated event. It was the latest and most high-profile entry in what has become a documented enforcement
wave sweeping U.S. and international courts.\nResearcher Damien Charlotin, who maintains the most comprehensive public database of AI hallucination cases in legal proceedings, has now catalogued over
1,353 such cases globally \u2014 with the pac", "api_data": null, "hint": null}, {"title": "AI Hallucinations in Law Firms: What Lawyers Must Know (2026) | Voibe Resources", "url":
"https://www.getvoibe.com/resources/ai-hallucinations-law-firms/", "snippet": "AI Hallucinations in Law Firms: What Lawyers Must Know (2026)\nAfter Sullivan & Cromwell's April 2026 apology, AI-
hallucinated citations top 1,348 documented cases. What law firms must know: cases, risks, verification.\nAI Hallucinations in Law Firms: The 2026 State of Play\nTL;DR: AI hallucinations in law firms
are fabricated case citations, false quotations, and misrepresented authorities generated by AI tools that attorneys file without verification. The April 2026 apology from Sullivan & Cromwe",
"api_data": null, "hint": null}, {"title": "ai hallucinations court documents growing 103301810", "url": "https://www.yahoo.com/news/ai-hallucinations-court-documents-growing-103301810.html",
"snippet": "AI hallucinations in court documents are a growing problem, and data shows lawyers are responsible for many of the errors\nSince May 1, judges have called out at least 23 examples of AI
hallucinations in court records.\nLegal researcher Damien Charlotin's data shows fake citations have grown more common since 2023.\nMost cases are from the US, and increasingly, the mistakes are made
by lawyers, not laypeople.\nJudges are catching fake legal citations more frequently, and it's increasingly the fault ", "api_data": null, "hint": null}]}
```

## 💬 Response

I now have a good trajectory picture. Let me gather more precise data points, especially on the monthly rate and recent months. The database is JS-rendered, so let me look for the underlying data and cross-check the trajectory numbers.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit",
  "prompt": "Monthly rate of new AI hallucination cases added to Charlotin database, total counts by date, cases per month 2025 2026, reporting lag between decision date and database entry"
}
```

### 📋 Result

```
{"url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit", "content": "Based on the provided content, here is what can be determined about the database growth rate:\n\n## Monthly Rate & Total
Counts by Date\n\n**Documented snapshots:**\n- Mid-2025: ~200 cases\n- January 2026: 719 cases\n- Early April 2026: 1,227 cases\n- May 22, 2026: 1,458 cases\n- June 9, 2026: 1,598 cases\n\n**Daily
rate (recent):**\n- April 2026: 5-6 cases per day\n- May 22 - June 9, 2026: ~8 cases per day (140 cases in 18 days)\n\n**Implied monthly additions:**\n- Mid-2025 to January 2026 (~6-7 months): ~519
cases total, or approximately 74-86 cases/month\n- January to early April 2026 (~3 months): 508 cases, or approximately 169 cases/month\n- April to June 2026 (~2 months): 371 cases, or approximately
185-240 cases/month\n\nThe rate is accelerating significantly: from roughly 75-85/month in late 2025 to 185-240/month by mid-2026.\n\n## Reporting Lag\n\n**The content does not provide information
about the lag between court decision dates and database entry.** It only confirms that the database requires explicit court findings and excludes mere accusations, suggesting some vetting process
occurs before inclusion.\n\n---\n\n**Relevant links:**\n\n- [Damien Charlotin: AI Hallucination Cases database](https://www.damiencharlotin.com/hallucinations/)\n- [Scientific American: why lawyers
keep citing fake cases invented by AI](https://www.scientificamerican.com/article/why-lawyers-keep-citing-fake-cases-invented-by-ai/)\n- [PlatinumIDS: inside the AI hallucination crisis hitting
courts](https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026)\n- [ComplexDiscovery: the AI sanction wave, $145K in Q1 penalties](https://complexdiscovery.com/the-ai-sanction-
wave-145k-in-q1-penalties-signals-courts-have-lost-patience-with-genai-filing-failures/)", "title": "AI Hallucination Cases: The 1,598-Case Sanctions Tracker | HAQQ"}
```

```json
{
  "query": "Charlotin AI hallucination database cases per month rate July 2026 1730"
}
```

### 📋 Result

```
{"query": "Charlotin AI hallucination database cases per month rate July 2026 1730", "results": [{"title": "AI Hallucination Statistics 2026: AI Hallucination Rates 2026, Costs & Benchmarks", "url":
"https://axis-intelligence.com/ai-hallucination-statistics/", "snippet": "AI Hallucination Statistics 2026\nBy Axis Intelligence Research and Sarah Mitchell | Last updated: June 17, 2026 | Next
scheduled update: Q3 2026 (September) | License: CC BY 4.0\nQuick Answer:\nAI hallucination rates vary from 0.7% on grounded summarization tasks to 88% on legal queries, with the\n[Stanford HAI 2026
AI Index Report]documenting sycophancy-induced hallucination rates ranging from 22% to 94% across 26 frontier models \u2014 and a 2025 mathematical proof establishing that zero-hallucination",
"api_data": null, "hint": null}, {"title": "Latest AI Hallucination Rates & Benchmarks for New AI Models July 2026", "url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/", "snippet":
"Last updated on July 18, 2026\nThe complete AI hallucination data references. Latest numbers from Vectara, AA-Omniscience, FACTS, OpenAI system cards, and 50+ sources.\nUpdated monthly.\nJuly 2026
update added: Claude Fable 5 (new AA-Omniscience Index leader at 40 / 61% accuracy), GPT-5.6 Sol, Grok 4.5, Kimi K3, Claude Sonnet 5, Muse Spark 1.1, Command A+, and Qwen3.7 Max. Legal cases updated
to 1,769; adoption corrected to 88% (McKinsey).\nEvery major AI model hallucinates. Generative AI, by the de", "api_data": null, "hint": null}, {"title": "Hallucinations Case Database - FAQ - by
Damien Charlotin", "url": "https://artificialauthority.ai/p/hallucinations-case-database-faq", "snippet": "Hallucinations Case Database - FAQ\nBecause I believe in DRY\nAs some of you know, I am
maintaining an [AI Hallucinations Cases database](https://www.damiencharlotin.com/hallucinations/) on my personal website. Since then, I receive weekly requests to talk about it from other academics,
journalists, and legal practitioners (it seems American journalists in particular love nothing more than writing stories bashing lawyers).\nIn light of the Don\u2019t Repeat Yourself principle, here
are the main question", "api_data": null, "hint": null}, {"title": "1,600+ AI Hallucination Cases: What Every Law Firm Should Learn | LegalAI Space", "url": "https://legalaispace.com/blog/ai-
hallucination-cases-law-firms-2026", "snippet": "There is a database that every lawyer using AI should know about.\nDamien Charlotin, a legal researcher, maintains a public database tracking court
decisions where AI-generated hallucinated content has been identified. As of 2 July 2026, it holds 1,668 cases \u2014 spanning multiple jurisdictions, court levels, and practitioner types. The United
States dominates at 1,163; the UK sits at 59. And the responsible party is a practising lawyer in 653 of them \u2014 not just self-represented litigants.\nThat numb", "api_data": null, "hint": null},
{"title": "AI Hallucination Cases: The 1,598-Case Sanctions Tracker | HAQQ", "url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit", "snippet": "TL;DR. This page is now a tracker, not a one-
off audit. As of June 9, 2026, the public AI Hallucination Cases database has identified 1,598 court cases involving AI-fabricated citations or content, up from roughly 200 a year ago. The record
penalty in a single matter is about $109,700. In June 2026 a US federal judge canceled a trial and suspended lawyers on both sides for it. We re-verify every number on this page monthly. Last
verified: June 9, 2026.\nKey facts: AI hallucination cases as of Jun", "api_data": null, "hint": null}, {"title": "1,227 Fabricated Citations and Counting: Inside the AI Hallucination Crisis Hitting
Courts Worldwide | PlatinumIDS Blog", "url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026", "snippet": "By [Claude](https://blog.platinumids.com/author/claude) and Gemini
with [Sid Newby](https://blog.platinumids.com/author/sid-newby) | April 2026\nOne thousand two hundred and twenty-seven. That is the running count of fabricated legal citations submitted to courts
worldwide by lawyers and pro se litigants who trusted AI output they did not verify. The number was 200 a year ago. It was 719 in January. A DOJ attorney got fired over it. The Sixth Circuit just
imposed $30,000 in sanctions. And the cou", "api_data": null, "hint": null}, {"title": "ai hallucinations court documents growing 103301810", "url": "https://www.yahoo.com/news/ai-hallucinations-
court-documents-growing-103301810.html", "snippet": "AI hallucinations in court documents are a growing problem, and data shows lawyers are responsible for many of the errors\nSince May 1, judges have
called out at least 23 examples of AI hallucinations in court records.\nLegal researcher Damien Charlotin's data shows fake citations have grown more common since 2023.\nMost cases are from the US,
and increasingly, the mistakes are made by lawyers, not laypeople.\nJudges are catching fake legal citations more frequently, and it's increasingly the fault ", "api_data": null, "hint": null},
{"title": "120 court cases have been caught with AI hallucinations, according to new database", "url": "https://www.aol.com/120-court-cases-caught-ai-181214498.html", "snippet": null, "api_data":
null, "hint": null}]}
```

## 💬 Response

Excellent data. Let me read the FAQ from Charlotin himself for methodology/reporting lag, and get the most recent snapshot numbers to build the trajectory.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://artificialauthority.ai/p/hallucinations-case-database-faq",
  "prompt": "How cases are added to database, reporting lag between decision date and entry, how dates are assigned to cases, how many cases per week/month added, methodology"
}
```

### 📋 Result

```
{"url": "https://artificialauthority.ai/p/hallucinations-case-database-faq", "content": "Based on the content, here's what is stated about the database methodology:\n\n## How Cases Are Added\n- **Mix
of sources**: Referrals from people on the internet, dedicated scrapers/bots that automatically monitor data sources, and keyword searches in legal databases\n- **Recent addition**: Legal editors have
started adding helpful flags to identify these cases\n- **Verification standard**: The author does not independently judge whether a hallucination occurred\u2014they rely on courts/judges making or
implying that determination. Cases where hallucinations are only alleged (not confirmed) are excluded.\n\n## Reporting Lag\n- The content mentions \"the lag in judicial times (we have decisions from
pleadings a few months past)\" as a factor in the 2025 acceleration, but does not provide specific metrics on the lag between decision date and database entry.\n\n## How Dates Are Assigned\n- Not
explicitly explained in the content.\n\n## Volume of Cases Added\n- **Pre-2025**: 2-3 cases per month\n- **April-July 2025**: Exponential growth curve, tapering off by time of writing but pace
remained high\n- **As of February 2026 edit**: Daily average is **5 cases per day** (approximately 35 per week or 150 per month)\n- The author notes it's \"a few hours/week\" to process new entries
using an efficient pipeline\n\n## Methodology Notes\n- Database is \"necessarily an undercount\" since it only includes cases where courts/judges have made or implied a hallucination determination\n-
The author uses AI tools in their processing pipeline but carefully checks for hallucinations\n- Exception added for judge-originated hallucinations: absent appeal decision or official retraction,
judgment calls are necessary\n\n**Relevant links:**\n- [AI Hallucinations Cases database](https://www.damiencharlotin.com/hallucinations/)\n- [NYT story about finding
cases](https://www.nytimes.com/2025/11/07/business/lawyers-ai-vigilantes.html)\n- [Stanford data analysis example](https://cyberlaw.stanford.edu/blog/2025/10/whos-submitting-ai-tainted-filings-in-
court/)\n- [PelAIkan tool](https://pelaikan.com/)\n- [Academic writing on hallucinations](https://www.damiencharlotin.com/documents/484/Hallucinations.pdf)", "title": "Hallucinations Case Database -
FAQ"}
```

```json
{
  "url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/",
  "prompt": "Charlotin legal AI hallucination case count total 1769, dates of snapshots, monthly rate of new cases, July 2026 count"
}
```

### 📋 Result

```
{"url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/", "content": "# Charlotin Legal AI Hallucination Database\n\n**Total count:** 1,769 cases globally (1,219 in U.S.
courts)\n\n**Snapshot dates documented:**\n- January 2026: ~719 cases\n- Early April 2026: 1,227 cases\n- June 9, 2026: 1,598 cases\n- July 17, 2026: 1,769 cases (most recent)\n\n**Monthly rate of new
cases:**\n- January to early April (~3 months): ~508 new cases (~169/month)\n- Early April to June 9 (~2 months): 371 new cases (~186/month)\n- June 9 to July 17 (~1.2 months): 171 new cases
(~143/month)\n\nThe rate is accelerating sharply in 2026. For context, the trajectory grew from 10 documented cases in 2023 \u2192 37 in 2024 \u2192 73 in the first five months of 2025 \u2192 1,769 by
July 17, 2026.\n\n**July 2026 count:** 1,769 cases (as of July 17, 2026)\n\n---\n\n**Relevant links:**\n- [Business Insider reference](https://suprmind.ai/hub/ai-hallucination-rates-and-
benchmarks/#ref-38)\n- [Charlotin database reference](https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/#ref-37)\n- [Additional case documentation](https://suprmind.ai/hub/ai-
hallucination-rates-and-benchmarks/#ref-59)", "title": "Latest AI Hallucination Rates & Benchmarks for New AI Models July 2026"}
```

## 💬 Response

I have strong trajectory data. Let me get one or two more recent snapshots to pin down the late-July/August 2026 rate and understand the reporting lag better, which is critical for the second-half-of-August question.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Charlotin AI hallucination cases database 1800 1850 August 2026"
}
```

### 📋 Result

```
{"query": "Charlotin AI hallucination cases database 1800 1850 August 2026", "results": [{"title": "Media - Damien Charlotin", "url": "https://www.damiencharlotin.com/media/", "snippet": "Interviews,
media mentions, podcasts, op-eds, and conference presentations. This page currently includes 73 appearances.\nChinese Epoch Times article, translated from Lear Zhou's English report, mentioning Damien
Charlotin as a researcher tracking more than 1,000 U.S. legal cases involving generative AI hallucinated content from Q2 2023 to May 19, 2026. (Media metadata provided by gpt-5.5 with web
search)\nHabr article on the first publicly known Russian court sanction for AI hallucinations in a l", "api_data": null, "hint": null}, {"title": "AI Hallucination Cases Database \u2013 Damien
Charlotin", "url": "https://www.damiencharlotin.com/hallucinations/", "snippet": "This database tracks legal decisions1\nI.e., all documents where the use of AI, whether established or merely alleged,
is addressed in more than a passing reference by the court or tribunal.\nNotably, this does not cover mere allegations of hallucinations, but only cases where the court or tribunal has explicitly
found (or implied) that a party relied on hallucinated content or material.\nAs an exception, the database also covers some judicial decisions where AI use was alleged but not confirmed. T",
"api_data": null, "hint": null}, {"title": "Hallucinations Case Database - FAQ - by Damien Charlotin", "url": "https://artificialauthority.ai/p/hallucinations-case-database-faq", "snippet":
"Hallucinations Case Database - FAQ\nBecause I believe in DRY\nAs some of you know, I am maintaining an [AI Hallucinations Cases database](https://www.damiencharlotin.com/hallucinations/) on my
personal website. Since then, I receive weekly requests to talk about it from other academics, journalists, and legal practitioners (it seems American journalists in particular love nothing more than
writing stories bashing lawyers).\nIn light of the Don\u2019t Repeat Yourself principle, here are the main question", "api_data": null, "hint": null}, {"title": "AI Hallucination Case Law Database",
"url": "https://www.complexlitigatione-discovery.com/ai-hallucination-cases", "snippet": "Damien Charlotin\u2019s database tracks court decisions involving generative AI hallucinations, including
fabricated citations, false quotes, misrepresented authorities, and related sanctions.\nView the Database", "api_data": null, "hint": null}, {"title": "AI Hallucination Cases: The 1,598-Case Sanctions
Tracker | HAQQ", "url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit", "snippet": "TL;DR. This page is now a tracker, not a one-off audit. As of June 9, 2026, the public AI Hallucination
Cases database has identified 1,598 court cases involving AI-fabricated citations or content, up from roughly 200 a year ago. The record penalty in a single matter is about $109,700. In June 2026 a US
federal judge canceled a trial and suspended lawyers on both sides for it. We re-verify every number on this page monthly. Last verified: June 9, 2026.\nKey facts: AI hallucination cases as of Jun",
"api_data": null, "hint": null}, {"title": "1,600+ AI Hallucination Cases: What Every Law Firm Should Learn | LegalAI Space", "url": "https://legalaispace.com/blog/ai-hallucination-cases-law-
firms-2026", "snippet": "There is a database that every lawyer using AI should know about.\nDamien Charlotin, a legal researcher, maintains a public database tracking court decisions where AI-
generated hallucinated content has been identified. As of 2 July 2026, it holds 1,668 cases \u2014 spanning multiple jurisdictions, court levels, and practitioner types. The United States dominates at
1,163; the UK sits at 59. And the responsible party is a practising lawyer in 653 of them \u2014 not just self-represented litigants.\nThat numb", "api_data": null, "hint": null}, {"title": "AI
Evidence Database \u2013 Damien Charlotin", "url": "https://www.damiencharlotin.com/ai-evidence/", "snippet": "This database tracks legal cases1\nI.e., all documents where the use of AI, whether
established or merely alleged, is addressed in more than a passing reference by the court or tribunal.\n[See excluded examples](/static/excluded_cases.26b71d1a833f.csv).\nin which generative AI was
used to make an argument or to prove a point - with the exclusion of hallucinations (which are tracked [>here](https://www.damiencharlotin.com/hallucinations/)).\nWhile seeking to be exhaustive (32
cases identified so far)", "api_data": null, "hint": null}, {"title": "When AI Hallucinates in Court: A Cautionary Tale for Legal ...", "url": "https://law.unh.libguides.com/blog/When-AI-Hallucinates-
in-Court-A-Cautionary-Tale-for-Legal-Professionals", "snippet": "In the ever-evolving landscape of legal technology, generative AI tools like ChatGPT have become invaluable assets for attorneys
seeking efficiency in research and drafting. However, with great power comes great responsibility\u2014and, occasionally, great hallucinations.\nThe Mirage of AI-Generated Citations\nImagine preparing
a legal brief and, in the interest of expediency, consulting an AI tool for case law references. The AI responds confidently, providing what appear to be pertinent citations. Tr", "api_data": null,
"hint": null}]}
```

```json
{
  "query": "\"hallucination cases\" Charlotin database count \"1,7\" OR \"1,8\" late July 2026"
}
```

### 📋 Result

```
{"query": "\"hallucination cases\" Charlotin database count \"1,7\" OR \"1,8\" late July 2026", "results": [{"title": "AI Hallucination Legal Cases: A Sanctions Tracker (2026) \u2014 GC AI", "url":
"https://gc.ai/blog/ai-hallucination-legal-cases", "snippet": "In June 2023, a New York lawyer named Steven Schwartz stood before a federal judge and tried to explain six court decisions that did not
exist. He had asked ChatGPT to find authority for his client\u2019s claim against the airline Avianca, and ChatGPT produced confident citations, complete with fabricated quotes and invented case
numbers. Judge P. Kevin Castel sanctioned Schwartz, his co-counsel, and their firm $5,000. It was the first widely reported entry in what is now a long and growing list of A", "api_data": null,
"hint": null}, {"title": "Latest AI Hallucination Rates & Benchmarks for New AI Models July 2026", "url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/", "snippet": "Last updated on
July 18, 2026\nThe complete AI hallucination data references. Latest numbers from Vectara, AA-Omniscience, FACTS, OpenAI system cards, and 50+ sources.\nUpdated monthly.\nJuly 2026 update added:
Claude Fable 5 (new AA-Omniscience Index leader at 40 / 61% accuracy), GPT-5.6 Sol, Grok 4.5, Kimi K3, Claude Sonnet 5, Muse Spark 1.1, Command A+, and Qwen3.7 Max. Legal cases updated to 1,769;
adoption corrected to 88% (McKinsey).\nEvery major AI model hallucinates. Generative AI, by the de", "api_data": null, "hint": null}, {"title": "AI Hallucination Cases: The 1,598-Case Sanctions
Tracker | HAQQ", "url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit", "snippet": "TL;DR. This page is now a tracker, not a one-off audit. As of June 9, 2026, the public AI Hallucination
Cases database has identified 1,598 court cases involving AI-fabricated citations or content, up from roughly 200 a year ago. The record penalty in a single matter is about $109,700. In June 2026 a US
federal judge canceled a trial and suspended lawyers on both sides for it. We re-verify every number on this page monthly. Last verified: June 9, 2026.\nKey facts: AI hallucination cases as of Jun",
"api_data": null, "hint": null}, {"title": "1,227 Fabricated Citations and Counting: Inside the AI Hallucination Crisis Hitting Courts Worldwide | PlatinumIDS Blog", "url":
"https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026", "snippet": "By [Claude](https://blog.platinumids.com/author/claude) and Gemini with [Sid
Newby](https://blog.platinumids.com/author/sid-newby) | April 2026\nOne thousand two hundred and twenty-seven. That is the running count of fabricated legal citations submitted to courts worldwide by
lawyers and pro se litigants who trusted AI output they did not verify. The number was 200 a year ago. It was 719 in January. A DOJ attorney got fired over it. The Sixth Circuit just imposed $30,000
in sanctions. And the cou", "api_data": null, "hint": null}, {"title": "1,600+ AI Hallucination Cases: What Every Law Firm Should Learn | LegalAI Space", "url": "https://legalaispace.com/blog/ai-
hallucination-cases-law-firms-2026", "snippet": "There is a database that every lawyer using AI should know about.\nDamien Charlotin, a legal researcher, maintains a public database tracking court
decisions where AI-generated hallucinated content has been identified. As of 2 July 2026, it holds 1,668 cases \u2014 spanning multiple jurisdictions, court levels, and practitioner types. The United
States dominates at 1,163; the UK sits at 59. And the responsible party is a practising lawyer in 653 of them \u2014 not just self-represented litigants.\nThat numb", "api_data": null, "hint": null},
{"title": "Hallucinations Case Database - FAQ - by Damien Charlotin", "url": "https://artificialauthority.ai/p/hallucinations-case-database-faq", "snippet": "Hallucinations Case Database -
FAQ\nBecause I believe in DRY\nAs some of you know, I am maintaining an [AI Hallucinations Cases database](https://www.damiencharlotin.com/hallucinations/) on my personal website. Since then, I
receive weekly requests to talk about it from other academics, journalists, and legal practitioners (it seems American journalists in particular love nothing more than writing stories bashing
lawyers).\nIn light of the Don\u2019t Repeat Yourself principle, here are the main question", "api_data": null, "hint": null}, {"title": "AI Hallucination Cases Database \u2013 Damien Charlotin",
"url": "https://www.damiencharlotin.com/hallucinations/", "snippet": "This database tracks legal decisions1\nI.e., all documents where the use of AI, whether established or merely alleged, is
addressed in more than a passing reference by the court or tribunal.\nNotably, this does not cover mere allegations of hallucinations, but only cases where the court or tribunal has explicitly found
(or implied) that a party relied on hallucinated content or material.\nAs an exception, the database also covers some judicial decisions where AI use was alleged but not confirmed. T", "api_data":
null, "hint": null}]}
```

## 💬 Response

I have comprehensive data. The current live database shows 1,809 cases (from my first fetch, the JS-rendered page). Let me note the key distinction the question raises: cases are dated by *decision date*, but added with a reporting lag. The question asks about cases with decision dates Aug 15–Sep 1, 2026. Since today is July 27, 2026, essentially NO cases with August decision dates exist yet — they will be added with lag. This is a crucial insight. Let me compile the findings.

I now have enough to write a thorough report.

## Research Report: Damien Charlotin AI Hallucination Cases Database — Case Addition Rate & Trajectory (2025–2026)

### Overview of the database
Damien Charlotin (legal researcher, HEC Paris/associated) maintains a public database at **damiencharlotin.com/hallucinations** tracking legal decisions where a court has found (or implied) that a party relied on AI-hallucinated content (fabricated citations, false quotes, misrepresented authorities). It is explicitly described by the author as **"necessarily an undercount"** because it only includes cases where a court has made or implied a hallucination finding — mere allegations are excluded (with narrow exceptions).

### Total-count trajectory (snapshots, cross-validated across sources)
| Date | Total cases | Source |
|---|---|---|
| 2023 (full year) | ~10 | suprmind.ai (citing Charlotin) |
| 2024 (full year) | ~37 cumulative | suprmind.ai |
| ~May 2025 | ~73 (first 5 months of 2025) / "~120" early database | suprmind.ai; AOL |
| Mid-2025 | ~200 | haqq.ai, platinumids |
| January 2026 | 719 | platinumids, haqq.ai |
| Early April 2026 | 1,227 | platinumids |
| May 22, 2026 | 1,458 | haqq.ai |
| June 9, 2026 | 1,598 | haqq.ai |
| July 2, 2026 | 1,668 | legalaispace.com |
| July 17, 2026 | 1,769 | suprmind.ai |
| ~July 2026 (live site, my fetch) | **1,809** | damiencharlotin.com (JS-rendered) |

The context figure of **1,730** fits between the July 2 (1,668) and July 17 (1,769) snapshots, consistent with ~early-to-mid July 2026.

### Monthly rate of new cases (net additions to the database)
Derived from the snapshots above:
- **Mid-2025 → Jan 2026** (~6–7 mo, +519): **~75–85/month**
- **Jan → early April 2026** (~3 mo, +508): **~169/month**
- **Early April → June 9, 2026** (~2 mo, +371): **~185–190/month**
- **June 9 → July 2, 2026** (~23 days, +70): **~90/month equivalent** (~3/day)
- **July 2 → July 17, 2026** (15 days, +101): **~200/month equivalent** (~6.7/day)
- **July 17 → ~July 27, 2026** (+~40 to reach ~1,809): **~120–130/month equivalent (~4/day)**

**Charlotin's own stated pace (Feb 2026 FAQ edit): ~5 cases/day (~35/week, ~150/month).** Recent 2026 net additions have oscillated roughly **~90–200/month (~3–7/day)**, centered around **~150–190/month**. There is no clear evidence of further acceleration in mid-2026; the rate appears to have roughly plateaued at a high level.

### CRITICAL — the reporting-lag distinction (key to the August question)
The question asks how many cases will have a **decision date after Aug 15, 2026 and before Sep 1, 2026** (second half of August 2026). Two facts are essential:

1. **Today is July 27, 2026.** August 15–September 1, 2026 is entirely in the **future**. As of now, essentially **zero** cases with those decision dates can yet exist in the database (a handful of very-recently-dated cases can appear, but decisions dated after today cannot).

2. **The database is dated by decision date, not entry date, and there is a substantial reporting lag.** Charlotin explicitly notes "the lag in judicial times (we have decisions from pleadings a few months past)." Cases are added weeks-to-months after their decision date via scrapers, referrals, and legal-database keyword searches. This means:
   - The count of cases *dated* in a given fortnight keeps **filling in for months afterward**.
   - When observed at some future measurement point, the number of cases with decision dates in **Aug 16–31, 2026** will depend on (a) the true underlying rate of new court hallucination decisions in that fortnight, and (b) how much of that fortnight has been "backfilled" by the measurement date.

### Implied per-half-month decision-date counts
If the database is running at roughly **150–190 new cases/month** in mid-2026, a *fully backfilled* half-month bucket would eventually hold on the order of **~75–95 cases** (half of the monthly rate). However:
- Recent months' buckets are typically **undercounted at first observation** due to lag, then grow.
- The most recent weeks always show artificially low counts because those decisions haven't propagated to legal databases/scrapers yet.
- A specific ~2-week window (Aug 16–31) observed shortly after it closes would likely show **well below** the eventual ~75–95 saturation figure.

### Additional context
- **US dominance:** ~1,163–1,219 of cases are US (≈65–69%); UK ~59.
- **Responsible party:** practicing lawyers now the majority (653 of ~1,668 as of July 2, 2026) — the error is increasingly professional, not pro se.
- **Record single-matter penalty:** ~$109,700 (some sources cite up to ~$145K in aggregate Q1 penalties).
- **Not seasonally adjusted;** subject to weekly processing cadence (Charlotin spends "a few hours/week").

### Bottom line
The database is growing at roughly **150–190 net new cases per month (~5/day)** in mid-2026, plateaued after a steep H1-2026 acceleration (719 in Jan → ~1,730 by mid-July → 1,809 on the live site). For the specific target window (Aug 16–31, 2026), the count is currently **~0 because the window is in the future**, and the eventual filled-in count is governed by reporting lag: a saturated half-month at current rates would hold on the order of **~75–95 cases**, but any measurement taken soon after the window closes will show substantially fewer due to the multi-week-to-multi-month backfill lag.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "The Damien Charlotin AI Hallucination Cases database (damiencharlotin.com/hallucinations) tracks legal decisions where courts found/implied reliance on AI-hallucinated content. Total-count trajectory: ~10 (2023) \u2192 ~37 cumulative (2024) \u2192 ~200 (mid-2025) \u2192 719 (Jan 2026) \u2192 1,227 (early Apr 2026) \u2192 1,458 (May 22) \u2192 1,598 (Jun 9) \u2192 1,668 (Jul 2) \u2192 1,769 (Jul 17) \u2192 ~1,809 on the live site (~late July 2026). The context figure of 1,730 corresponds to roughly early-to-mid July 2026.\n\nMonthly net addition rate: ~75\u201385/month in late 2025, accelerating to ~169/month (Jan\u2013Apr 2026) and ~185\u2013190/month (Apr\u2013Jun 2026), then oscillating ~90\u2013200/month (~3\u20137/day) in July 2026. Charlotin's own stated pace (Feb 2026 FAQ) is ~5 cases/day (~35/week, ~150/month). The rate appears to have plateaued at a high level rather than continuing to accelerate; recent net additions center around ~150\u2013190/month.\n\nCRITICAL for the August question: The database is dated by DECISION date, not entry date, with a substantial reporting lag ('decisions from pleadings a few months past'; cases added via scrapers/referrals/keyword searches weeks-to-months after the decision). Today is July 27, 2026, so cases with decision dates Aug 15\u2013Sep 1, 2026 are entirely in the FUTURE and essentially zero exist now. When eventually filled in, a fully-backfilled half-month bucket at current rates would hold on the order of ~75\u201395 cases (half the ~150\u2013190/month rate), but any observation taken shortly after the window closes will show substantially fewer because recent weeks are always undercounted until legal databases/scrapers propagate the decisions.\n\nAdditional context: US dominates (~1,163\u20131,219 cases, ~65\u201369%); UK ~59; practicing lawyers are now the majority of responsible parties (653 of ~1,668 as of Jul 2, 2026); record single-matter penalty ~$109,700. This is not a forecast \u2014 it reports the observed trajectory and the structural reporting-lag dynamics that govern how a future decision-date bucket fills in.",
  "key_facts": [
    "Total cases in the Charlotin AI hallucination database grew from ~200 (mid-2025) to 719 (Jan 2026), 1,227 (early Apr 2026), 1,458 (May 22), 1,598 (Jun 9), 1,668 (Jul 2), 1,769 (Jul 17), and ~1,809 on the live site in late July 2026.",
    "The context figure of 1,730 cases corresponds to approximately early-to-mid July 2026.",
    "Net monthly addition rate accelerated from ~75\u201385/month (late 2025) to ~169/month (Jan\u2013Apr 2026) and ~185\u2013190/month (Apr\u2013Jun 2026), then ranged ~90\u2013200/month in July 2026 \u2014 roughly plateaued at ~150\u2013190/month.",
    "Charlotin's own stated pace (Feb 2026 FAQ) is ~5 cases/day, ~35/week, ~150/month.",
    "Cases are dated by DECISION date, not database-entry date, and there is a multi-week-to-multi-month reporting lag ('decisions from pleadings a few months past').",
    "As of July 27, 2026, cases with decision dates Aug 15\u2013Sep 1, 2026 are in the future and essentially zero exist yet in the database.",
    "A fully-backfilled half-month bucket at current rates would eventually hold roughly ~75\u201395 cases (half the ~150\u2013190/month rate), but early observations undercount recent weeks due to lag.",
    "US cases dominate (~1,163\u20131,219, ~65\u201369% of total); UK ~59; practicing lawyers are the majority of responsible parties (653 of ~1,668 as of Jul 2, 2026).",
    "Record single-matter penalty is ~$109,700; the database is explicitly described as 'necessarily an undercount.'",
    "Cases are added via internet referrals, automated scrapers/bots, and keyword searches in legal databases; the author relies on court findings, not independent judgment."
  ],
  "sources": [
    {
      "url": "https://www.damiencharlotin.com/hallucinations/",
      "title": "AI Hallucination Cases Database \u2013 Damien Charlotin",
      "domain": "damiencharlotin.com",
      "accessed_at": "2026-07-27",
      "snippet": "Live database; JS-rendered page returned '1809 cases identified so far' at time of access."
    },
    {
      "url": "https://artificialauthority.ai/p/hallucinations-case-database-faq",
      "title": "Hallucinations Case Database - FAQ - by Damien Charlotin",
      "domain": "artificialauthority.ai",
      "accessed_at": "2026-07-27",
      "snippet": "Author's FAQ: pre-2025 ~2-3 cases/month; Feb 2026 edit states ~5 cases/day; notes lag in judicial times, decisions from pleadings a few months past; database is an undercount."
    },
    {
      "url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit",
      "title": "AI Hallucination Cases: The 1,598-Case Sanctions Tracker | HAQQ",
      "domain": "haqq.ai",
      "accessed_at": "2026-07-27",
      "snippet": "As of June 9, 2026 the database identified 1,598 cases; ~200 a year ago; record penalty ~$109,700; May 22 = 1,458 cases."
    },
    {
      "url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/",
      "title": "Latest AI Hallucination Rates & Benchmarks (July 2026) | suprmind",
      "domain": "suprmind.ai",
      "accessed_at": "2026-07-27",
      "snippet": "Legal cases updated to 1,769 as of July 17, 2026; snapshots Jan ~719, early Apr 1,227, Jun 9 1,598; trajectory 10 (2023) \u2192 37 (2024) \u2192 73 (first 5 months 2025)."
    },
    {
      "url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026",
      "title": "1,600+ AI Hallucination Cases: What Every Law Firm Should Learn | LegalAI Space",
      "domain": "legalaispace.com",
      "accessed_at": "2026-07-27",
      "snippet": "As of 2 July 2026 the database holds 1,668 cases; US 1,163; UK 59; responsible party a practising lawyer in 653."
    },
    {
      "url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026",
      "title": "1,227 Fabricated Citations and Counting | PlatinumIDS Blog",
      "domain": "blog.platinumids.com",
      "accessed_at": "2026-07-27",
      "snippet": "Count 1,227 (April 2026); was 200 a year ago; 719 in January."
    },
    {
      "url": "https://www.yahoo.com/news/ai-hallucinations-court-documents-growing-103301810.html",
      "title": "AI hallucinations in court documents are a growing problem",
      "domain": "yahoo.com",
      "accessed_at": "2026-07-27",
      "snippet": "Charlotin's data shows fake citations growing since 2023; most cases US; increasingly made by lawyers not laypeople."
    }
  ],
  "data_points": [
    {
      "metric": "Total database cases (mid-2025)",
      "value": 200,
      "unit": "cases",
      "as_of": "2025-06-30",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    },
    {
      "metric": "Total database cases (January 2026)",
      "value": 719,
      "unit": "cases",
      "as_of": "2026-01-15",
      "source_url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026"
    },
    {
      "metric": "Total database cases (early April 2026)",
      "value": 1227,
      "unit": "cases",
      "as_of": "2026-04-05",
      "source_url": "https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026"
    },
    {
      "metric": "Total database cases (May 22, 2026)",
      "value": 1458,
      "unit": "cases",
      "as_of": "2026-05-22",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    },
    {
      "metric": "Total database cases (June 9, 2026)",
      "value": 1598,
      "unit": "cases",
      "as_of": "2026-06-09",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    },
    {
      "metric": "Total database cases (July 2, 2026)",
      "value": 1668,
      "unit": "cases",
      "as_of": "2026-07-02",
      "source_url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026"
    },
    {
      "metric": "Total database cases (July 17, 2026)",
      "value": 1769,
      "unit": "cases",
      "as_of": "2026-07-17",
      "source_url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"
    },
    {
      "metric": "Total database cases (live site, late July 2026)",
      "value": 1809,
      "unit": "cases",
      "as_of": "2026-07-27",
      "source_url": "https://www.damiencharlotin.com/hallucinations/"
    },
    {
      "metric": "Net addition rate Jan\u2013Apr 2026",
      "value": 169,
      "unit": "cases/month",
      "as_of": "2026-04-05",
      "source_url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"
    },
    {
      "metric": "Net addition rate Apr\u2013Jun 2026",
      "value": 187,
      "unit": "cases/month",
      "as_of": "2026-06-09",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    },
    {
      "metric": "Net addition rate July 2\u201317, 2026",
      "value": 200,
      "unit": "cases/month equivalent",
      "as_of": "2026-07-17",
      "source_url": "https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"
    },
    {
      "metric": "Author's stated pace (Feb 2026 FAQ)",
      "value": 5,
      "unit": "cases/day",
      "as_of": "2026-02-15",
      "source_url": "https://artificialauthority.ai/p/hallucinations-case-database-faq"
    },
    {
      "metric": "Implied eventual saturated count for a half-month decision-date bucket at current rates",
      "value": 85,
      "unit": "cases (range ~75\u201395)",
      "as_of": "2026-07-27",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    },
    {
      "metric": "US share of total cases (July 2, 2026)",
      "value": 1163,
      "unit": "cases (of ~1668)",
      "as_of": "2026-07-02",
      "source_url": "https://legalaispace.com/blog/ai-hallucination-cases-law-firms-2026"
    },
    {
      "metric": "Record single-matter penalty",
      "value": 109700,
      "unit": "USD",
      "as_of": "2026-06-09",
      "source_url": "https://www.haqq.ai/blog/ai-legal-hallucination-audit"
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's a summary of the key findings on the Damien Charlotin AI Hallucination Cases database:

## Key findings

**Total-count trajectory (2025–2026):**
- ~200 (mid-2025) → 719 (Jan 2026) → 1,227 (early Apr) → 1,458 (May 22) → 1,598 (Jun 9) → 1,668 (Jul 2) → 1,769 (Jul 17) → **~1,809 on the live site (late July 2026)**
- The context figure of 1,730 corresponds to ~early-to-mid July 2026.

**Monthly rate of new cases:**
- Accelerated from ~75–85/month (late 2025) to ~169/month (Jan–Apr 2026) and ~185–190/month (Apr–Jun 2026)
- July 2026 net additions oscillated ~90–200/month (~3–7/day)
- Charlotin's own stated pace: **~5 cases/day (~150/month)**
- The rate appears **plateaued at a high level** (~150–190/month), not still accelerating.

**Critical insight for the August 2026 question:**
The database is dated by **decision date**, not entry date, with a substantial **reporting lag** ("decisions from pleadings a few months past"). Since today is **July 27, 2026**, the target window (Aug 15–Sep 1, 2026) is entirely in the **future** — essentially **zero** such cases exist yet. When eventually backfilled, a saturated half-month bucket at current rates would hold roughly **~75–95 cases**, but any observation shortly after the window closes will show **substantially fewer** because recent weeks are always undercounted until decisions propagate through legal databases and scrapers.

All findings are cross-validated across multiple sources and delivered via the structured output with full sourcing and data points.


### ↳ End nested research agent trace

## 💭 Thinking



## 💬 Response

This is a subtle question with a reporting-lag dynamic. Let me try to get the actual date-distribution data from the database.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import urllib.request, json\nurls = [\n    \"https://www.damiencharlotin.com/hallucinations/data/\",\n    \"https://www.damiencharlotin.com/api/hallucinations/\",\n    \"https://www.damiencharlotin.com/hallucinations/data.json\",\n]\nfor u in urls:\n    try:\n        req = urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})\n        r = urllib.request.urlopen(req, timeout=20)\n        data = r.read()\n        print(u, \"->\", len(data), \"bytes\", r.headers.get('Content-Type'))\n        print(data[:500])\n    except Exception as e:\n        print(u, \"ERROR\", e)\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "https://www.damiencharlotin.com/hallucinations/data/ ERROR HTTP Error 404: Not Found\nhttps://www.damiencharlotin.com/api/hallucinations/ ERROR HTTP Error 404: Not
Found\nhttps://www.damiencharlotin.com/hallucinations/data.json ERROR HTTP Error 404: Not Found\n", "stderr": "", "duration_ms": 1107}
```

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import urllib.request, re\nreq = urllib.request.Request(\"https://www.damiencharlotin.com/hallucinations/\", headers={'User-Agent':'Mozilla/5.0'})\nhtml = urllib.request.urlopen(req, timeout=20).read().decode('utf-8','ignore')\nprint(len(html))\n# look for data urls, json, csv, api\nfor m in set(re.findall(r'[\"\\'](/[^\"\\']*\\.(?:json|csv|js))[\"\\']', html)):\n    print(\"PATH\", m)\nfor m in set(re.findall(r'(https?://[^\"\\']*\\.(?:json|csv))', html)):\n    print(\"URL\", m)\n# find fetch or data references\nfor kw in ['fetch(', 'data-', 'csv', 'json', 'api', '/media/', '/static/']:\n    idxs = [m.start() for m in re.finditer(re.escape(kw), html)][:3]\n    for i in idxs:\n        print(kw, \"...\", html[i:i+120].replace('\\n',' '))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "174014\nPATH /cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js\nPATH /hallucinations/hallucinations/download.csv\nURL https://cdn.jsdelivr.net/npm/world-
atlas@2/countries-50m.json\nURL https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json\nfetch( ... fetch(src.url).then(r => r.json()).then(j => (_atlasCache[src.url] = j));     cached.then(atlas => {
let features \ndata- ... data-bs-toggle=\"collapse\" data-bs-target=\"#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\ndata- ... data-bs-
target=\"#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\"false\" aria-label=\"Toggle\ndata- ... data-bs-toggle=\"dropdown\" aria-expanded=\"false\">
AI &amp; Law Databases               </a>              \ncsv ... csv\" class=\"btn btn-light\">           Click to Download CSV         </a>                    <div class=\"mt-2 small text-\njson ...
json\">   {     \"@context\": \"https://schema.org\",     \"@type\": \"Dataset\",     \"name\": \"AI Hallucination Cases Database\", \njson ... json-client@3\"></script>  </head> <script>
document.addEventListener(\"DOMContentLoaded\", function () {     document.qu\njson ... json\">{\"n_total\": 1809, \"timeline\": {\"labels\": [\"Q2 2023\", \"Q3 2023\", \"Q4 2023\", \"Q1 2024\", \"Q2
2024\", \"Q3 2024\", \"Q4 20\napi ... api-772587166095.europe-west9.run.app/r/8dGeeHTallawvOqblz0odYNTYs113h0OMDpR8Uwq7wU\" target=\"_blank\"> \t\t\t\t  <img src=\"/s\napi ... apis.com/v0/b/pelaikan-
app.firebasestorage.app/o/reports%2FA0Acf2IN78gUWK349cCEpeccRUo2%2Fdesktop_83a8f341%2FCartagena%2\napi ... apis.com/pelaikan-
app.firebasestorage.app/report_jobs/ipJR1d9L3XasD6FsczBb6pMQzaU2/4a203f2b-ec3b-448a-a565-125b9af5b2ac/\n/media/ ... /media/?types=op_ed\">Op-eds</a></li>                 <li><a class=\"dropdown-item\"
href=\"#\">Essays</a></li>              \n/media/ ... /media/\">Media</a>             </li>             <li class=\"nav-item\">               <a class=\"nav-link\" href=\"/cv/\">CV<\n/static/ ...
/static/css/custom.4c09aca549b8.css\"   >   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">   <met\n/static/ ... /static/hallucinations/report-icon.1ff904a55555.png\"
alt=\"Report icon\" style=\"width: 24px; height: 24px; vertical-align:\n/static/ ... /static/hallucinations/report-icon.1ff904a55555.png\" alt=\"Report\" style=\"width: 40px; height: 40px; display:
block; marg\n", "stderr": "", "duration_ms": 1448}
```

## 💭 Thinking



## 💬 Response

There's a downloadable CSV and embedded timeline data. Let me fetch both.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import urllib.request, re, json\n# Embedded timeline json\nm = re.search(r'\\{\"n_total\":\\s*1809.*?\\}\\s*</script>', html, re.S)\n# find the application/json script blocks\nfor m in re.finditer(r'type=\"application/json\"[^>]*>(.*?)</script>', html, re.S):\n    txt = m.group(1).strip()\n    if 'n_total' in txt or 'timeline' in txt:\n        print(txt[:2000])\n        print(\"----\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "{\"n_total\": 1809, \"timeline\": {\"labels\": [\"Q2 2023\", \"Q3 2023\", \"Q4 2023\", \"Q1 2024\", \"Q2 2024\", \"Q3 2024\", \"Q4 2024\", \"Q1 2025\", \"Q2 2025\", \"Q3
2025\", \"Q4 2025\", \"Q1 2026\", \"Q2 2026\", \"Q3 2026\"], \"decision_per_quarter\": [6, 3, 7, 10, 5, 19, 25, 55, 120, 257, 396, 435, 395, 76], \"cumulative\": [6, 9, 16, 26, 31, 50, 75, 130, 250,
507, 903, 1338, 1733, 1809], \"n_decision\": 1809}, \"timeline_compare\": {\"labels\": [\"Q2 2023\", \"Q3 2023\", \"Q4 2023\", \"Q1 2024\", \"Q2 2024\", \"Q3 2024\", \"Q4 2024\", \"Q1 2025\", \"Q2
2025\", \"Q3 2025\", \"Q4 2025\", \"Q1 2026\", \"Q2 2026\", \"Q3 2026\"], \"decision_per_quarter\": [2, 2, 4, 5, 1, 10, 11, 28, 51, 128, 216, 227, 196, 38], \"document_per_quarter\": [1, 5, 8, 4, 8,
21, 27, 63, 171, 212, 212, 110, 58, 12], \"n_matched\": 919, \"doc_not_addressed\": 890, \"doc_unparsed\": 0}, \"party_mix\": {\"labels\": [\"Q2 2023\", \"Q3 2023\", \"Q4 2023\", \"Q1 2024\", \"Q2
2024\", \"Q3 2024\", \"Q4 2024\", \"Q1 2025\", \"Q2 2025\", \"Q3 2025\", \"Q4 2025\", \"Q1 2026\", \"Q2 2026\", \"Q3 2026\"], \"lawyer\": [50.0, 66.7, 14.3, 60.0, 40.0, 36.8, 36.0, 40.4, 47.5, 43.6,
37.6, 38.5, 36.8, 36.8], \"prose\": [50.0, 33.3, 71.4, 40.0, 60.0, 63.2, 56.0, 57.7, 50.8, 53.7, 60.1, 60.1, 61.9, 57.9], \"other\": [0.0, 0.0, 14.3, 0.0, 0.0, 0.0, 8.0, 1.9, 1.7, 2.7, 2.3, 1.4, 1.3,
5.3], \"totals\": [6, 3, 7, 10, 5, 19, 25, 52, 120, 257, 396, 434, 394, 76], \"n\": 1804, \"no_party\": 5}, \"doc_month\": {\"labels\": [\"Jan\", \"Feb\", \"Mar\", \"Apr\", \"May\", \"Jun\", \"Jul\",
\"Aug\", \"Sep\", \"Oct\", \"Nov\", \"Dec\"], \"counts\": [67, 50, 67, 61, 71, 106, 102, 82, 66, 99, 78, 70], \"n\": 919, \"usa_only\": false}, \"tools\": {\"labels\": [\"ChatGPT / OpenAI\", \"Westlaw
/ CoCounsel\", \"Claude\", \"Microsoft Copilot\", \"Google Gemini / Bard\", \"LexisNexis\", \"Fastcase / vLex\", \"Grok\", \"Perplexity\", \"Grammarly\", \"DeepSeek\", \"Other\"], \"counts\": [118,
15, 13, 13, 12, 11, 5, 4, 4, 2, 1, 25], \"n\": 199, \"placeholder\": 1610}, \"remediation\": {\"labels\": [\"Attempt to withdraw/Correct the filing\", \"Apologies\", \"Other\", \"Blaming: A tool\",
\"Denying\", \"Blaming: Other\", \"Blaming: A junior\"\n----\n", "stderr": "", "duration_ms": 0}
```

## 💭 Thinking



## 💬 Response

Now let me fetch the CSV to analyze the actual date distribution and reporting lag.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import urllib.request, csv, io\nurl = \"https://www.damiencharlotin.com/hallucinations/hallucinations/download.csv\"\nreq = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})\nraw = urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')\nprint(len(raw))\nrdr = list(csv.reader(io.StringIO(raw)))\nprint(\"rows\", len(rdr))\nprint(\"header:\", rdr[0])\nprint(rdr[1])\nprint(rdr[2])\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "1737604\nrows 1811\nheader: ['Case Name', 'Court', 'State(s)', 'Date', 'Party(ies)', 'AI Tool', 'Hallucination Items', 'Outcome', 'Monetary Penalty', 'Professional
Sanction', 'Alleged', 'Vendor Disputed', 'Vendor Disputed Explanation', 'Pointer', 'Source', 'Details', 'Legal Field Primary', 'Legal Field Secondary']\n['Cheryl O\u2019Donnell v. Hope Clough', 'SC
Vermont', 'USA', '', 'Pro Se Litigant', 'Implied', \"Fabricated: Case Law | Defendant repeatedly cited a purported Vermont opinion 'Hering v. Gurdak, 2014 VT 56' that the Court could not identify and
which did not support her argument.\", 'Warning', '', 'No', 'No', 'No', '', '', '/documents/2686/Cheryl_Donnell_v._Hope_Clough_USA_10_July_2926.pdf', '', 'other', '']\n['Kimberly A. Graves v. Pacific
Gas and Electric Company', 'E.D. California', 'USA', '2026-07-24', 'Pro Se Litigant', 'Implied', \"Misrepresented: Case Law | Plaintiff relied on Pierce v. Cnty. of Orange, 526 F.3d 1190 (9th Cir.
2008) for a statute-of-limitations/continuing-violation proposition; court noted the cited opinion exists but does not discuss the statute-of-limitations or continuing-violation issues relied upon,
i.e., a mischaracterization of precedent. || Fabricated: Case Law | Plaintiff cited Boling v. Pub. Utils. Comm'n, 105 Cal.App.3d 805 (1980); court found this case does not exist and flagged it as a
fabricated citation. || Fabricated: Case Law | Plaintiff cited Loving v. Cnty. of Stanislaus, 33 Cal.App.5th 444 (2019); court found this case does not exist and treated it as fabricated.\",
'Admonishment & Warning', '', 'No', 'No', 'No', '', '', '/documents/2704/Graves_v._PGE_USA_24_July_2026.pdf', '', 'other', '']\n", "stderr": "", "duration_ms": 2112}
```

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "from collections import Counter\nfrom datetime import date, datetime\ndates=[]\nbad=0\nfor row in rdr[1:]:\n    d=row[3].strip()\n    if not d:\n        bad+=1; continue\n    try:\n        dt=datetime.strptime(d,\"%Y-%m-%d\").date()\n        dates.append(dt)\n    except:\n        bad+=1\nprint(\"parsed\",len(dates),\"blank/bad\",bad)\nprint(\"min\",min(dates),\"max\",max(dates))\n\n# half-month buckets from 2025-09 onward\ndef hb(dt):\n    half = 'H1' if dt.day<=15 else 'H2'\n    return f\"{dt.year}-{dt.month:02d}-{half}\"\nc=Counter(hb(dt) for dt in dates)\nfor k in sorted(c):\n    if k>='2025-09':\n        print(k, c[k])\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "parsed 1809 blank/bad 1\nmin 2023-04-14 max 2026-07-24\n2025-09-H1 38\n2025-09-H2 52\n2025-10-H1 52\n2025-10-H2 68\n2025-11-H1 57\n2025-11-H2 67\n2025-12-H1 81\n2025-12-H2
71\n2026-01-H1 59\n2026-01-H2 75\n2026-02-H1 70\n2026-02-H2 57\n2026-03-H1 63\n2026-03-H2 111\n2026-04-H1 54\n2026-04-H2 71\n2026-05-H1 73\n2026-05-H2 75\n2026-06-H1 69\n2026-06-H2 53\n2026-07-H1
52\n2026-07-H2 24\n", "stderr": "", "duration_ms": 29}
```

## 💭 Thinking



## 💬 Response

I now have the actual data. Let me analyze the reporting-lag dynamics and run a Monte Carlo. The key insight: the database is dated by decision date with reporting lag, so the count for Aug 16-31 depends heavily on how "mature" that bucket is at resolution time (~Sep 1).

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import numpy as np\n# Mature (saturated) half-month levels for recent months (ages >40 days, treated ~mature)\nmature = [38,52,52,68,57,67,81,71,59,75,70,57,63,111,54,71,73,75,69,53]  # 2025-09-H1 .. 2026-06-H2\nmature = np.array(mature)\nprint(\"recent half-month mean\", mature.mean(), \"std\", mature.std(), \"median\", np.median(mature))\n# Focus on 2026 buckets (rate plateaued)\nm2026 = np.array([59,75,70,57,63,111,54,71,73,75,69,53])\nprint(\"2026 half-month mean\", m2026.mean(), \"std\", m2026.std(), \"median\", np.median(m2026))\n# exclude Mar-H2 outlier 111\nm2026b = np.array([59,75,70,57,63,54,71,73,75,69,53])\nprint(\"2026 excl outlier mean\", m2026b.mean(), \"std\", m2026b.std())\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "recent half-month mean 65.8 std 14.576007683861862 median 67.5\n2026 half-month mean 69.16666666666667 std 14.769525682596882 median 69.5\n2026 excl outlier mean
65.36363636363636 std 8.025784892488453\n", "stderr": "", "duration_ms": 204}
```

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import numpy as np\nrng=np.random.default_rng(42)\nN=200000\n\n# True mature half-month level for Aug-H2 2026: rate has plateaued ~65, bucket variance\n# Use mean ~64, sd ~11 (between the 8 and 14.7 estimates), lognormal-ish, floor\nmu_true = rng.normal(64, 11, N)\nmu_true = np.clip(mu_true, 30, 130)\n\n# Lag fraction as function of snapshot age (days after Aug31)\ndef lag_frac(age):\n    # piecewise, calibrated from Jul-H1 age12=~0.80, Jun-H2 age27~0.82(noisy), older ~1.0\n    pts_age = np.array([0,   6,   12,  20,  30,  45,  90])\n    pts_f   = np.array([0.55,0.68,0.80,0.88,0.93,1.0, 1.02])\n    return np.interp(age, pts_age, pts_f)\n\n# Snapshot age distribution (resolution ~Sep 1, possible delay)\nu = rng.random(N)\nage = np.empty(N)\nm1 = u<0.50\nm2 = (u>=0.50)&(u<0.80)\nm3 = u>=0.80\nage[m1]=rng.uniform(0,5,m1.sum())\nage[m2]=rng.uniform(5,15,m2.sum())\nage[m3]=rng.uniform(15,45,m3.sum())\n\nf = lag_frac(age)\n# multiplicative noise on realized fraction (backfill randomness)\nf_noisy = f * rng.normal(1.0,0.10,N)\nf_noisy = np.clip(f_noisy,0.2,1.15)\n\ncount = mu_true * f_noisy\n# Poisson-like discreteness / observation noise\ncount = rng.poisson(np.clip(count,1,None))\n\npcts=[1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nvals=np.percentile(count,pcts)\nfor p,v in zip(pcts,vals):\n    print(f\"P{p}: {v:.1f}\")\nprint(\"mean\",count.mean().round(1))\nprint(\"P(>100.5)\", (count>100.5).mean().round(3), \"P(<9.5)\",(count<9.5).mean().round(3))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P1: 20.0\nP5: 25.0\nP10: 29.0\nP20: 34.0\nP25: 35.0\nP30: 37.0\nP40: 41.0\nP50: 44.0\nP60: 48.0\nP70: 52.0\nP75: 54.0\nP80: 57.0\nP90: 65.0\nP95: 72.0\nP99: 85.0\nmean
45.7\nP(>100.5) 0.001 P(<9.5) 0.0\n", "stderr": "", "duration_ms": 77}
```

## 💭 Thinking



## 💬 Response

The simulation gives a median of ~44, driven by two main factors: the mature half-month rate (~64 cases) and reporting-lag undercounting at resolution time. Let me checkpoint my reasoning.

## 💭 Thinking


