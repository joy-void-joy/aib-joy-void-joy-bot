# Reasoning Log: Will Discord publicly file an S-1 prospectus on SEC EDGAR before May 31, 2026?

*Generated: 2026-05-18T09:18:38.374619+00:00*


## 💭 Thinking

Let me analyze this question carefully.

## Step 1: Parse the Resolution Criteria

**What must happen for YES resolution?**
- A Form S-1 or S-1/A filed by Discord Inc. (CIK 0001763840) must appear publicly on SEC EDGAR
- Filing date must be on or before May 30, 2026
- The window is January 1, 2026 to 11:59 PM ET on May 30, 2026

**Key details:**
- Today is May 18, 2026
- The question closes on May 18, 2026 at 10:33:16Z (so it's closing very soon!)


- With only about 12 days left until the May 30 deadline and no S-1 filing visible on EDGAR yet, the current trajectory points toward a NO resolution unless Discord files imminently.

The March 2026 window that was initially expected to see an IPO filing has already passed without any action, and there's been no confidential submission either—just the public EDGAR record to consider.

Let me check what's actually happening with Discord's IPO timeline right now.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


## 🔧 Tool: mcp__research__research


```json
{
  "post_id_list": [
    43533
  ]
}
```

### 📋 Result

```
{"post_id": 43533, "title": "Will Discord publicly file an S-1 prospectus on SEC EDGAR before May 31, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43533", "background_info":
"Discord Inc., the communication platform with 200M+ monthly active users, confidentially submitted a draft registration statement to the U.S. Securities and Exchange Commission in early January 2026,
in preparation for an initial public offering. Goldman Sachs and JPMorgan are reported underwriters. Under the JOBS Act, emerging growth companies can submit draft S-1 registration statements
confidentially; these only become visible on EDGAR (as Form S-1) when the company decides to launch the marketing phase of the IPO, typically 2-4 weeks before pricing.\n\nEarly reporting floated a
possible March 2026 debut, but that window has passed without any public S-1. As of mid-May 2026, EDGAR's filings index for Discord Inc. (CIK 0001763840) shows no S-1 filing. Market attention in
spring 2026 has been heavily occupied by other high-profile IPOs (notably SpaceX), and reported private/secondary valuation estimates for Discord have ranged widely from ~$6.6B to $25B+.\n\nDiscord's
EDGAR page: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001763840&type=S-1&dateb=&owner=include&count=40\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3,
\"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves YES if, at any time between January 1, 2026 and 11:59 PM ET on May 30, 2026, a Form S-1
(or S-1/A) registration statement filed by Discord Inc. (CIK 0001763840) appears publicly on SEC EDGAR. The resolver will check Discord's EDGAR filings page: https://www.sec.gov/cgi-bin/browse-
edgar?action=getcompany&CIK=0001763840&type=S-1&dateb=&owner=include&count=40 \u2014 if one or more rows with Filing Type \"S-1\" or \"S-1/A\" are listed with a Filing Date on or before May 30, 2026,
the question resolves YES. Otherwise it resolves NO.", "fine_print": "A previously-confidential DRS (Draft Registration Statement) that has not been made public on EDGAR does NOT count; only filings
publicly visible as Form S-1 or S-1/A on EDGAR count. If Discord is filing under a different parent entity name but the SEC EDGAR system links the S-1 to Discord's business (e.g., the registrant's
prospectus identifies Discord Inc. as the issuer of the registered securities), that filing counts. If SEC EDGAR is unavailable on the resolution date, the resolver may use SEC EDGAR's full-text
search (https://efts.sec.gov/LATEST/search-index?q=%22Discord+Inc%22&forms=S-1) or [credible sources](https://www.metaculus.com/faq/#definitions) confirming a public S-1 filing.", "num_forecasters":
2, "community_prediction": null}
```

```json
{
  "questions": [
    {
      "query": "Discord IPO S-1 filing SEC EDGAR status May 2026",
      "ttl": "6h"
    },
    {
      "query": "Discord IPO timeline 2026 latest news update",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Discord IPO S-1 filing SEC EDGAR status May 2026", "entry": {"slug": "discord-ipo-s-1-filing-sec-edgar-status-may-2026-633a24aa", "query": "Discord IPO S-1 filing SEC EDGAR
status May 2026", "answer": "Now I have comprehensive data from SEC EDGAR. Let me compile the final research report.\n\n---\n\n## Research Report: Discord IPO / S-1 Filing Status \u2014 SEC EDGAR (as
of May 18, 2026)\n\n### Key Finding: No S-1 Filing Exists\n\n**Discord Inc. (CIK: 0001763840) has NOT filed an S-1 registration statement with the SEC as of May 18, 2026.** This was verified through
multiple direct queries to the SEC EDGAR database.\n\n---\n\n### 1. SEC EDGAR Filing Record for Discord Inc.\n\nDiscord Inc. is registered with the SEC under **CIK 0001763840**, incorporated in
**Delaware**, headquartered at **444 De Haro St., Suite 200, San Francisco, CA 94107**. CEO **Jason Citron** is listed as Executive Officer and Director.\n\nDiscord's complete SEC filing history
consists of **only 6 filings \u2014 all Form D** (Notice of Exempt Offering of Securities), indicating private placement fundraising rounds:\n\n| Filing Date | Form | Description |\n|---|---|---|\n|
2023-03-15 | D | Exempt offering \u2014 $15,749,250 total sold |\n| 2021-09-17 | D | Exempt offering |\n| 2021-07-13 | D | Exempt offering |\n| 2020-12-21 | D | Exempt offering |\n| 2020-07-02 | D |
Exempt offering |\n| 2019-01-08 | D | Exempt offering |\n\n**No S-1, S-1/A, F-1, DRS, or DRS/A filings** have been made by Discord Inc. (CIK 0001763840). The company has:\n- **No ticker symbol**
assigned\n- **No exchange listing**\n- **No SIC code** registered (consistent with a private company that has not gone through the IPO registration process)\n\n### 2. Verification Methods\n\nThe
finding was cross-validated through four independent SEC EDGAR queries:\n\n1. **Direct CIK lookup** (`data.sec.gov/submissions/CIK0001763840.json`): Shows only 6 Form D filings. No S-1.\n2. **Full-
text search for \"Discord Inc\" filtered to S-1/S-1/A forms**: **0 results**.\n3. **CIK number search in DRS/S-1 forms**: **0 results** (ruling out confidential filings).\n4. **Broad \"Discord\"
keyword search in S-1 filings since 2025**: 46 results, but **none** from Discord Inc. itself \u2014 all are other companies that merely mention Discord in their filings (e.g., Gameverse Interactive,
Collab Z, etc.).\n\n### 3. Latest Known Private Fundraising\n\nDiscord's most recent SEC filing (Form D, March 15, 2023) reports:\n- **Total amount sold**: $15,749,250\n- **Industry**: Other
Technology\n- **Revenue range**: Declined to disclose\n- **Offering completed**: Yes (total remaining = $0)\n\n### 4. Background Context (pre-knowledge-cutoff)\n\n- Discord's last known private
valuation was approximately **$15 billion** (2021 funding round).\n- The company rejected a reported **$12 billion acquisition offer from Microsoft** in April 2021.\n- Discord generated an estimated
**$600M+ in annual revenue** by 2023-2024, primarily from Nitro subscriptions.\n- The company conducted **17% workforce layoffs** in January 2024 as part of cost-cutting.\n- Discord began
experimenting with advertising revenue (promoted \"Quests\").\n- CEO Jason Citron had not made a definitive public commitment to an IPO timeline as of early 2025.\n\n### 5. Funds Holding Discord
Equity\n\nSEC filings from investment funds confirm Discord remains a private holding:\n- **Destiny Tech100 Inc. (DXYZ)** \u2014 Regularly reports Discord as a portfolio holding in NPORT-P filings
(most recent: March 2026).\n- **ARK Venture Fund** \u2014 Also holds Discord in its portfolio (most recent filing: March 2026).\n\nThese fund filings confirm Discord remains a **private company** with
equity held by institutional investors in private-market vehicles.\n\n### 6. Important Caveats\n\n- A **confidential S-1 filing** (submitted under the JOBS Act) would NOT appear in public EDGAR
searches until the company chooses to make it public (typically ~15 days before an IPO roadshow). Discord could theoretically have filed confidentially without any public trace.\n- The absence of
public S-1 filings does not rule out that Discord may be actively preparing for an IPO.\n- The most recent Discord-specific filing is from **March 2023** (over 3 years ago), which is an unusually long
gap for a company of this size \u2014 potentially indicating they are either self-funding or conducting fundraising that doesn't require SEC disclosure.\n\n---", "sources": [{"url":
"https://data.sec.gov/submissions/CIK0001763840.json", "title": "SEC EDGAR Company Submissions - Discord Inc. (CIK 0001763840)", "domain": "data.sec.gov", "accessed_at": "2026-05-18T00:00:00Z",
"snippet": "Shows 6 Form D filings only. No S-1, no ticker, no exchange listing. Most recent filing: 2023-03-15."}, {"url": "https://efts.sec.gov/LATEST/search-
index?q=%22Discord+Inc%22&forms=S-1,S-1/A,F-1,F-1/A", "title": "SEC EDGAR Full-Text Search - Discord Inc S-1/F-1 Filings", "domain": "efts.sec.gov", "accessed_at": "2026-05-18T00:00:00Z", "snippet":
"Total S-1 hits for 'Discord Inc': 0. No registration statement filings found."}, {"url": "https://efts.sec.gov/LATEST/search-index?q=%221763840%22&forms=DRS,DRS/A,S-1,S-1/A", "title": "SEC EDGAR CIK
Search - Discord CIK in DRS/S-1 Filings", "domain": "efts.sec.gov", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "CIK 1763840 in DRS/S-1 filings: 0 results. No confidential or public registration
filings."}, {"url": "https://www.sec.gov/Archives/edgar/data/1763840/000156761923005083/primary_doc.xml", "title": "Discord Inc. Form D Filing - March 15, 2023 (Primary Document XML)", "domain":
"www.sec.gov", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Total amount sold: $15,749,250. Industry: Other Technology. Revenue range: Decline to Disclose. Issuer: Discord Inc., Delaware
corporation."}, {"url": "https://efts.sec.gov/LATEST/search-index?q=%22Discord+Inc%22&startdt=2024-01-01&enddt=2026-05-18", "title": "SEC EDGAR Full-Text Search - All Discord Inc Mentions Since 2024",
"domain": "efts.sec.gov", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Most mentions of Discord Inc in recent filings are from Destiny Tech100 (DXYZ) NPORT-P filings and ARK Venture Fund,
reporting Discord as a private portfolio holding."}], "key_facts": ["Discord Inc. (CIK 0001763840) has NOT filed an S-1 or any IPO registration statement with the SEC as of May 18, 2026", "Discord's
entire SEC filing history consists of only 6 Form D filings (exempt offerings), with the most recent dated March 15, 2023", "Discord has no ticker symbol, no exchange listing, and no SIC code on EDGAR
\u2014 confirming private company status", "Discord's most recent Form D (March 2023) reported $15,749,250 in total securities sold, with the offering fully completed", "Zero results were returned
when searching EDGAR for Discord Inc. S-1, S-1/A, F-1, DRS, or DRS/A filings", "Destiny Tech100 (DXYZ) and ARK Venture Fund continue to report Discord as a private portfolio holding in NPORT-P filings
through March 2026", "Discord is incorporated in Delaware, headquartered at 444 De Haro St., Suite 200, San Francisco, CA 94107", "Jason Citron is listed as Executive Officer and Director on Discord's
SEC filings", "A confidential S-1 filing under the JOBS Act would not appear in public EDGAR searches until ~15 days before an IPO roadshow", "Discord's last known private valuation was approximately
$15 billion from its 2021 funding round", "Discord rejected a reported $12 billion acquisition offer from Microsoft in April 2021", "Discord conducted 17% workforce layoffs in January 2024 as part of
cost-cutting measures"], "data_points": [{"metric": "Discord Inc. S-1 filings on SEC EDGAR", "value": 0.0, "unit": "filings", "as_of": "2026-05-18", "source_url": "https://efts.sec.gov/LATEST/search-
index?q=%22Discord+Inc%22&forms=S-1,S-1/A,F-1,F-1/A"}, {"metric": "Discord Inc. total SEC filings (all Form D)", "value": 6.0, "unit": "filings", "as_of": "2026-05-18", "source_url":
"https://data.sec.gov/submissions/CIK0001763840.json"}, {"metric": "Discord Inc. most recent Form D total amount sold", "value": 15749250.0, "unit": "USD", "as_of": "2023-03-15", "source_url":
"https://www.sec.gov/Archives/edgar/data/1763840/000156761923005083/primary_doc.xml"}, {"metric": "Discord Inc. confidential (DRS) filings on SEC EDGAR", "value": 0.0, "unit": "filings", "as_of":
"2026-05-18", "source_url": "https://efts.sec.gov/LATEST/search-index?q=%221763840%22&forms=DRS,DRS/A,S-1,S-1/A"}, {"metric": "Discord last known private valuation", "value": 15000000000.0, "unit":
"USD", "as_of": "2021-09-17", "source_url": "https://data.sec.gov/submissions/CIK0001763840.json"}], "created_at": "2026-05-18T09:15:29.326593Z", "updated_at": "2026-05-18T09:15:29.326593Z",
"stale_after": "2026-05-18T15:15:29.326593Z", "state": "fresh", "revision_history": [], "session_id": "4ce7cc97-47f5-4360-96a9-6959d797dca6", "follow_up_count": 0}, "is_follow_up": false}, {"query":
"Discord IPO timeline 2026 latest news update", "entry": {"slug": "discord-ipo-timeline-2026-latest-news-update-5c919d03", "query": "Discord IPO timeline 2026 latest news update", "answer": "##
Discord IPO Timeline \u2014 Research Report (as of May 2026)\n\n> **Note:** Live web search tools were unavailable in this session. The findings below are based on publicly available information
through my knowledge cutoff. Key data points that should be verified with live sources are flagged.\n\n---\n\n### Executive Summary\n\nDiscord has been widely expected to pursue an IPO in the
2025\u20132026 timeframe, but **no S-1 filing had been confirmed** as of the latest verified information. The company has been taking concrete steps to position itself for a public offering \u2014
including significant layoffs, cost-cutting, and aggressive monetization \u2014 but has not publicly committed to a specific date.\n\n---\n\n### 1. IPO Timeline & Key Signals\n\n| Date | Event |
Significance |\n|---|---|---|\n| **Early 2021** | Rejected Microsoft's ~$12B acquisition offer | Signaled preference for independent path (likely IPO) |\n| **Sep 2021** | Series H at **$15B
valuation** ($500M raised) | Peak private valuation |\n| **2022** | IPO plans cooled | Tech IPO market froze amid rate hikes |\n| **Aug 2023** | Laid off **17% of staff (~170 employees)** | Shift
toward profitability / pre-IPO cost discipline |\n| **2024** | Focused on monetization; reportedly hired financial advisors | Pre-IPO preparations |\n| **2025\u20132026** | Widely expected IPO window
| Contingent on profitability and market conditions |\n\n- **No S-1 filing** had been made with the SEC as of the most recent confirmed reports.\n- CEO **Jason Citron** has historically avoided
committing to a specific IPO date, emphasizing product and growth focus.\n- Analyst consensus placed a potential IPO in **2025 or 2026**, depending on whether the company achieved sustainable
profitability.\n\n---\n\n### 2. Valuation & Funding History\n\n- **Total funding raised**: ~**$1.0\u20131.1 billion** across 8+ rounds\n- **Peak valuation**: **$15 billion** (Series H, September
2021)\n- **Recent implied valuation**: Some 2023\u20132024 secondary market transactions reportedly marked Discord down from the $15B peak, though late 2024 tech valuation recoveries may have
stabilized or improved this figure.\n- **Key investors**: Dragoneer, Greenoaks, Index Ventures, Greylock, Benchmark, Accel, General Atlantic, Tiger Global\n\n---\n\n### 3. Revenue & Financial
Performance\n\n| Year | Estimated Revenue | Key Driver |\n|---|---|---|\n| 2020 | ~$130M | Nitro subscriptions |\n| 2021 | ~$350\u2013400M | Rapid user growth |\n| 2022 | ~$445M | Nitro expansion |\n|
2023 | ~$600M | Nitro Basic launch, server subscriptions |\n| 2024 | ~$700\u2013800M (est.) | Continued monetization growth |\n\n- **Primary revenue**: Discord Nitro ($9.99/mo), Nitro Basic
($2.99/mo), Server Boosts, Server Subscriptions\n- **Profitability**: Discord was **not yet profitable** as of latest confirmed data; reaching breakeven was considered a prerequisite for IPO\n- **User
base**: Over **200 million MAUs** as of 2024\n\n---\n\n### 4. Context & Market Conditions\n\n- The broader **tech IPO market** began reopening in 2024\u20132025 after a prolonged freeze, with major
names (Reddit went public in March 2024) testing investor appetite.\n- Discord's IPO timing is likely influenced by peer companies' reception in the public markets.\n- The company's pivot toward
profitability (layoffs, new revenue streams) mirrors the playbook of other late-stage startups preparing for public listings.\n\n---\n\n### 5. Key Uncertainties (Requiring Live
Verification)\n\n\u26a0\ufe0f The following should be checked with live news sources for May 2026 updates:\n- Whether Discord has **filed an S-1** with the SEC\n- Any **underwriter appointments**
(Goldman Sachs, Morgan Stanley, etc.)\n- **2025 full-year revenue** and whether profitability was achieved\n- Updated **secondary market valuation** or new funding rounds\n- Any **public statements**
by Jason Citron on IPO timing in 2025\u20132026\n\n---", "sources": [{"url": "https://www.bloomberg.com/news/articles/2021-03-23/microsoft-is-said-to-be-in-talks-to-buy-discord-for-more-than-10b",
"title": "Microsoft in Talks to Buy Discord for More Than $10 Billion", "domain": "bloomberg.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Microsoft was in talks to acquire Discord for more
than $10 billion before Discord rejected the offer."}, {"url": "https://www.theverge.com/2021/4/20/22394301/discord-no-sale-microsoft", "title": "Discord ends acquisition talks with Microsoft",
"domain": "theverge.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Discord ended acquisition discussions with Microsoft, choosing to remain independent."}, {"url":
"https://www.cnbc.com/2023/08/10/discord-lays-off-17-percent-of-employees.html", "title": "Discord lays off 17% of employees", "domain": "cnbc.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet":
"Discord laid off 17% of its workforce, approximately 170 employees, in August 2023."}, {"url": "https://www.crunchbase.com/organization/discord", "title": "Discord Funding Rounds and Investors -
Crunchbase", "domain": "crunchbase.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Discord has raised approximately $1.1 billion in total funding with a last known valuation of $15
billion."}, {"url": "https://www.wsj.com/articles/discord-raises-500-million-boosting-valuation-to-15-billion-11631728200", "title": "Discord Raises $500 Million, Boosting Valuation to $15 Billion",
"domain": "wsj.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Discord raised $500 million in September 2021 at a $15 billion valuation."}], "key_facts": ["Discord has not filed an S-1 with
the SEC as of the latest verified information (through early 2025)", "Discord rejected Microsoft's ~$12 billion acquisition offer in early 2021, preferring an independent path", "Peak private
valuation was $15 billion from September 2021 Series H round ($500M raised)", "Total funding raised across all rounds is approximately $1.0-1.1 billion", "Discord laid off 17% of staff (~170
employees) in August 2023 as part of pre-IPO cost discipline", "Estimated 2024 revenue was ~$700-800 million, up from ~$130M in 2020", "Discord was not yet profitable as of latest confirmed data;
profitability considered prerequisite for IPO", "User base exceeded 200 million monthly active users as of 2024", "Analyst consensus placed potential IPO in 2025 or 2026, contingent on profitability
and market conditions", "CEO Jason Citron has historically avoided committing to a specific IPO date", "CAVEAT: Live web search was unavailable; 2025-2026 developments could not be verified with
current sources"], "data_points": [{"metric": "Peak Private Valuation", "value": 15.0, "unit": "billion USD", "as_of": "2021-09-15", "source_url": "https://www.wsj.com/articles/discord-
raises-500-million-boosting-valuation-to-15-billion-11631728200"}, {"metric": "Series H Funding Raised", "value": 500.0, "unit": "million USD", "as_of": "2021-09-15", "source_url":
"https://www.wsj.com/articles/discord-raises-500-million-boosting-valuation-to-15-billion-11631728200"}, {"metric": "Total Funding Raised", "value": 1100.0, "unit": "million USD", "as_of":
"2024-12-31", "source_url": "https://www.crunchbase.com/organization/discord"}, {"metric": "Microsoft Acquisition Offer (Rejected)", "value": 12.0, "unit": "billion USD", "as_of": "2021-03-23",
"source_url": "https://www.bloomberg.com/news/articles/2021-03-23/microsoft-is-said-to-be-in-talks-to-buy-discord-for-more-than-10b"}, {"metric": "Staff Layoff Percentage (Aug 2023)", "value": 17.0,
"unit": "percent", "as_of": "2023-08-10", "source_url": "https://www.cnbc.com/2023/08/10/discord-lays-off-17-percent-of-employees.html"}, {"metric": "Estimated Revenue 2020", "value": 130.0, "unit":
"million USD", "as_of": "2020-12-31", "source_url": "https://www.crunchbase.com/organization/discord"}, {"metric": "Estimated Revenue 2022", "value": 445.0, "unit": "million USD", "as_of":
"2022-12-31", "source_url": "https://www.crunchbase.com/organization/discord"}, {"metric": "Estimated Revenue 2023", "value": 600.0, "unit": "million USD", "as_of": "2023-12-31", "source_url":
"https://www.crunchbase.com/organization/discord"}, {"metric": "Estimated Revenue 2024", "value": 750.0, "unit": "million USD", "as_of": "2024-12-31", "source_url":
"https://www.crunchbase.com/organization/discord"}, {"metric": "Monthly Active Users", "value": 200.0, "unit": "million", "as_of": "2024-12-31", "source_url":
"https://www.crunchbase.com/organization/discord"}], "created_at": "2026-05-18T09:13:13.479501Z", "updated_at": "2026-05-18T09:13:13.479501Z", "stale_after": "2026-05-18T15:13:13.479501Z", "state":
"fresh", "revision_history": [], "session_id": "ae1c7f1b-35fb-48cb-99d9-239977824513", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

Now let me search for the very latest news about Discord's IPO and check the EDGAR page directly.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "Discord IPO S-1 filing May 2026"
}
```

### 📋 Result

```
{"query": "Discord IPO S-1 filing May 2026", "results": [{"title": "Chat Platform Discord Files Confidentially for IPO - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-01-06/chat-
platform-discord-is-said-to-file-confidentially-for-ipo", "snippet": null, "api_data": null, "hint": null}, {"title": "Discord races to IPO in Q1: Can it fetch $25B valuation after rejecting
Microsoft? \u2014 TFN", "url": "https://techfundingnews.com/discord-ipo-q1-25bn-valuation-microsoft-rejection/", "snippet": "Discord has confidentially filed for a US IPO, targeting a Q1 2026 debut
after years of private funding, according to industry reports. The S-1 filing keeps financials confidential for now, but a public filing is expected soon, potentially next month.\nWorking with
[Goldman Sachs](https://techfundingnews.com/goldman-sachs-to-acquire-industry-ventures-in-deal-worth-up-to-965m/) and [JPMorgan](https://techfundingnews.com/founder-with-4m-fake-customers-duped-
jpmorgan-for-175m-worth-of-acquisition/),", "api_data": null, "hint": null}, {"title": "Discord IPO Filing: What 2026 Means for Nitro and User Data", "url": "https://www.remio.ai/post/discord-ipo-
filing-what-2026-means-for-nitro-and-user-data", "snippet": "Discord IPO Filing: What 2026 Means for Nitro and User Data\n[Olivia Johnson](https://www.remio.ai/members-area/olivia/profile)- Jan 9\n- 6
min read\n![Discord IPO Filing: What 2026 Means for Nitro and User Data](https://static.wixstatic.com/media/80334c_5e58ae244e2645698a6324ca902e4274~mv2.png/v1/fill/w_49,h_26,al_c,q_85,usm_0.66_1.00_0.
01,blur_2,enc_avif,quality_auto/80334c_5e58ae244e2645698a6324ca902e4274~mv2.png)\nIf you have opened Discord anytime in the last six months, the subtle shifts in th", "api_data": null, "hint": null},
{"title": "When Is the Discord IPO Date? The Popular Chat Platform Is Going Public | CoinCodex", "url": "https://coincodex.com/article/81997/discord-ipo/", "snippet": "When it comes to the Discord IPO
date, the \"going public\" headlines aren't clickbait. Discord reportedly made a real move on January 6 or 7, 2026, when it confidentially filed [IPO paperwork with the U.S. Securities and Exchange
Commission (SEC)](https://www.reuters.com/business/chat-platform-discord-confidentially-file-us-ipo-bloomberg-news-reports-2026-01-06/).\nThat filing stays private at first, so you can't read the full
document yet. As of mid-February 2026, there's also no public S-1 on fi", "api_data": null, "hint": null}, {"title": "Discord's IPO could happen in March | TechCrunch", "url":
"https://techcrunch.com/2026/01/07/discords-ipo-could-happen-in-march/", "snippet": "Wall Street is once again whispering about a potential Discord IPO. Discord, the popular chat and community
platform, filed confidential IPO paperwork with the SEC and has pinned its hopes on a debut in March, [sources told Bloomberg](https://www.bloomberg.com/news/articles/2026-01-06/chat-platform-discord-
is-said-to-file-confidentially-for-ipo). The company hired top-tier tech IPO bankers Goldman Sachs and JPMorgan Chase as its underwriters. Should the tea leaves continue to look positive for t",
"api_data": null, "hint": null}, {"title": "Discord Confidentially Files for IPO, Targeting Potential ...", "url": "https://mlq.ai/news/discord-confidentially-files-for-ipo-targeting-
potential-2026-debut/", "snippet": "Discord Inc. has confidentially filed for an initial public offering with U.S. regulators and is working with Goldman Sachs and JPMorgan Chase on a potential U.S.
listing as early as March 2026, positioning the fast-growing communications platform as one of the larger consumer-technology offerings currently in the IPO pipeline.[1][2][4][5]\nDiscord
Confidentially Files for IPO, Targeting Potential 2026 Debut\nKey Points\n- Discord has confidentially filed IPO paperwork with the U.S. Securities and ", "api_data": null, "hint": null}, {"title":
"Discord IPO Watch: Will Discord Stock Trade in 2026?", "url": "https://accessipos.com/discord-stock-ipo/", "snippet": "Discord IPO Watch: Will Discord Stock Trade in 2026?\nThis page contains links
to our partners. We may be compensated when a link is clicked. [Read the disclosures](https://accessipos.com/legal/) to learn more.\n![Discord logo. Learn how to prepare for the upcoming Discord IPO
and explore ways to buy Discord stock. Follow along as the company approaches its IPO date.](https://accessipos.com/wp-content/uploads/2021/09/DiscordLogo750px.png)\nExplore opportunities to invest in
the Discord IPO, anticip", "api_data": null, "hint": null}, {"title": "Discord IPO Closing Market Cap Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/discord-ipo-closing-
market-cap", "snippet": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\", \"probability\": 0.057, \"volume\": 298539.3585510005, \"url\": \"https://polymarket.com/event/discord-
ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on Discord's market capitalization at the closing price on its first day of trading.\\n\\nIf no
IPO occurs by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30, 2026\\\".\\n\\nMarket capitalization expresses the monetary valu", "api_data": {"content": [{"type": "text",
"text": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\", \"probability\": 0.057, \"volume\": 298539.3585510005, \"url\": \"https://polymarket.com/event/discord-ipo-closing-
market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on Discord's market capitalization at the closing price on its first day of trading.\\n\\nIf no IPO occurs
by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30, 2026\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in
its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two
brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on Discord\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111615694922589471518709913330752256579066965027597319186712737482564226971621\", \"recent_history\": [{\"date\": \"2026-05-11\", \"probability\": 0.13}, {\"date\": \"2026-05-12\", \"probability\":
0.154}, {\"date\": \"2026-05-13\", \"probability\": 0.152}, {\"date\": \"2026-05-14\", \"probability\": 0.151}, {\"date\": \"2026-05-15\", \"probability\": 0.072}, {\"date\": \"2026-05-16\",
\"probability\": 0.067}, {\"date\": \"2026-05-17\", \"probability\": 0.048}, {\"date\": \"2026-05-18\", \"probability\": 0.058}]}], \"query\": \"discord ipo closing market cap\"}"}]}, "hint": null},
{"title": "Discord IPO: $15B Platform Files for March 2026 Debut | byteiota", "url": "https://byteiota.com/discord-ipo-15b-platform-files-for-march-2026-debut/", "snippet":
"![](https://byteiota.com/wp-content/uploads/2026/01/discord-ipo-featured-image-800x400.jpg)\nDiscord confidentially filed for a US IPO on January 6, 2026, working with Goldman Sachs and JPMorgan to
target a March 2026 public debut. The San Francisco-based chat platform has grown from a gaming voice app to a 200-million-user community tool used by developers, gamers, and tech professionals, now
valued at $15 billion. The filing comes nearly five years after Discord rejected Microsoft\u2019s $12 billion", "api_data": null, "hint": null}, {"title": "The Discord IPO May Arrive in Q1 2026.",
"url": "https://www.youtube.com/shorts/mGV4SJBBMZg", "snippet": "- Fran\u00e7aisFrance\n- Deutsch\n- English\n- Espa\u00f1ol\n- Italiano\n- \u0627\u0644\u0639\u0631\u0628\u064a\u0629\n- Toutes les
langues\n- Afrikaans\n- az\u0259rbaycan\n- bosanski\n- catal\u00e0\n- \u010ce\u0161tina\n- Cymraeg\n- Dansk\n- Deutsch\n- eesti\n- EnglishUnited Kingdom\n- EnglishUnited States\n-
Espa\u00f1olEspa\u00f1a\n- Espa\u00f1olLatinoam\u00e9rica\n- euskara\n- Filipino\n- Fran\u00e7aisCanada\n- Gaeilge\n- galego\n- Hrvatski\n- Indonesia\n- isiZulu\n- \u00edslenska\n- Italiano\n-
Kiswahili\n- latvie\u0161u\n- lietuvi\u0173\n- magyar\n- Melayu\n- Nederlands\n- norsk\n- o\u2018zbek\n- polski\n- Portugu\u00easBrasil\n- Portugu\u00easPo", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Discord IPO delay postponed 2026"
}
```

### 📋 Result

```
{"query": "Discord IPO delay postponed 2026", "results": [{"title": "Discord Age Verification Delayed: Why the Platform Is Stalling on Child Safety \u2014 and What Parents Need to Know | IBTimes UK",
"url": "https://www.ibtimes.co.uk/discord-delays-age-verification-ipo-concerns-1781375", "snippet": "Discord Age Verification Delayed: Why the Platform Is Stalling on Child Safety \u2014 and What
Parents Need to Know\nAs lawsuits pile up and an IPO looms, the platform's safety promises ring hollow for millions of families\n![Discord Age
Verification](https://d.ibtimes.co.uk/en/full/1792913/discord-age-verification.png?w=736&f=a2071f6b79fa939b8cb142d8467fd3f5)\nDiscord's promise to tighten age checks has hit another delay, and the
timing raises questions about whether child safety or corporate prioritie", "api_data": null, "hint": null}, {"title": "Discord Alternatives 2026: Where to Go as the Platform Faces Backlash Over
Delayed Age Checks and Child Safety Failures | IBTimes UK", "url": "https://www.ibtimes.co.uk/discord-age-verification-delay-user-backlash-1781380", "snippet": "Discord Alternatives 2026: Where to Go
as the Platform Faces Backlash Over Delayed Age Checks and Child Safety Failures\nA 2025 data breach exposed 70,000 government IDs, and now users are flooding TeamSpeak, Signal and open-source
platforms\n![Discord Alternatives](https://d.ibtimes.co.uk/en/full/1792921/discord-alternatives.png?w=736&f=c67d599206e873ff2e905de923d78643)\nDiscord just bought itself more time. But users aren't
waiting around.\nThe company [announced](https://discord.com/blog/getting-", "api_data": null, "hint": null}, {"title": "When Is the Discord IPO Date? The Popular Chat Platform Is Going Public |
CoinCodex", "url": "https://coincodex.com/article/81997/discord-ipo/", "snippet": "When it comes to the Discord IPO date, the \"going public\" headlines aren't clickbait. Discord reportedly made a
real move on January 6 or 7, 2026, when it confidentially filed [IPO paperwork with the U.S. Securities and Exchange Commission (SEC)](https://www.reuters.com/business/chat-platform-discord-
confidentially-file-us-ipo-bloomberg-news-reports-2026-01-06/).\nThat filing stays private at first, so you can't read the full document yet. As of mid-February 2026, there's also no public S-1 on
fi", "api_data": null, "hint": null}, {"title": "Discord IPO: When Will It Go Public? | Ultima Markets", "url": "https://www.ultimamarkets.com/academy/discord-ipo-when-will-it-go-public/", "snippet":
null, "api_data": null, "hint": null}, {"title": "When Will Discord Officially Announce an IPO?", "url": "https://www.actionnetwork.com/prediction-markets/when-will-discord-officially-announce-an-
ipo", "snippet": "Tyler Jacobsma is the founder of [Flowframe.xyz](https://flowframe.xyz/), which provides in-depth content and tools for prediction market traders.\nThe market prices a 48% chance
that Discord files its public S-1 before July 1. The evidence puts the real probability closer to 20-25%. Here's the NO ladder trade across May, June, and July contracts.\nPosition: NO ladder: May,
Jun, Jul contracts\nFair Value: ~90% (vs. 53c market price)\nEdge: +$0.37 per share on Jul contract\nConviction: 8.2/10 \u2014 data q", "api_data": null, "hint": null}, {"title": "When will Discord
officially announce an IPO | Octagon AI", "url": "https://octagonai.co/markets/companies/ipos/when-will-discord-officially-announce-an-ipo/", "snippet": "![When will Discord officially announce an
IPO? prediction market](https://kalshi-public-docs.s3.amazonaws.com/series-images-webp/KXIPODISCORD.webp)\nWhen will Discord officially announce an IPO?\n[1. Executive
Verdict](https://octagonai.co#verdict)\n[2. Market Behavior & Price Dynamics](https://octagonai.co#chart)\n[3. Significant Price Movements](https://octagonai.co#movements)\n[4. Market
Data](https://octagonai.co#market-data)\n[5. What are Discord's revenue, cash burn, and IPO outlook?](https://o", "api_data": null, "hint": null}, {"title": "Discord IPO \u2013 how to trade Discord
shares", "url": "https://capital.com/en-int/learn/ipo/discord-ipo", "snippet": "Discord IPO \u2013 how to trade Discord
shares\n![](https://img.capital.com/imgs/blocks/1920x1140x0/shutterstock_2353907093_compressed-rsz_0.jpg)\nLearn about Discord and its upcoming IPO, with its potential price drivers, and how to trade
Discord stock via CFDs when it lists.\nWhen is the Discord IPO date?\nAs of April 2025, Discord has not officially announced a date for its [initial public offering (IPO)](https://capital.com/en-
int/learn/essentials/what-is-an-ipo). However, reports suggest the company", "api_data": null, "hint": null}, {"title": "When will Discord officially announce an IPO?", "url":
"https://kalshi.com/markets/kxipodiscord/when-will-discord-ipo", "snippet": "{\"markets\": [], \"query\": \"when will discord ipo\"}", "api_data": {"content": [{"type": "text", "text": "{\"markets\":
[], \"query\": \"when will discord ipo\"}"}]}, "hint": null}, {"title": "Discord IPO: When (Date), Where & What to Expect / Axi", "url": "https://www.axi.com/int/blog/education/stocks/discord-ipo",
"snippet": "Login with
email\n[Home](http://www.axi.com/int)/\n[Blog](http://www.axi.com/int/blog)/\n[Education](http://www.axi.com/int/blog/education)/\n[Stocks](http://www.axi.com/int/blog/education/stocks)/ Discord
IPO\nWhile there is still no date announced, Discord going public is one of the most widely anticipated IPOs on Wall Street. A listing is likely to occur on the New York Stock Exchange (NYSE) or
NASDAQ, and the fundraising round in August 2021 put Discord\u00b4s value at $15 billion.\nThe current market ", "api_data": null, "hint": null}, {"title": "Discord IPO Closing Market Cap Predictions
& Odds 2026 | Polymarket", "url": "https://polymarket.com/event/discord-ipo-closing-market-cap", "snippet": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\", \"probability\":
0.057, \"volume\": 298539.3585510005, \"url\": \"https://polymarket.com/event/discord-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
Discord's market capitalization at the closing price on its first day of trading.\\n\\nIf no IPO occurs by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30,
2026\\\".\\n\\nMarket capitalization expresses the monetary valu", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\",
\"probability\": 0.057, \"volume\": 298539.3585510005, \"url\": \"https://polymarket.com/event/discord-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve
based on Discord's market capitalization at the closing price on its first day of trading.\\n\\nIf no IPO occurs by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30,
2026\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on Discord\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"111615694922589471518709913330752256579066965027597319186712737482564226971621\", \"recent_history\":
[{\"date\": \"2026-05-11\", \"probability\": 0.13}, {\"date\": \"2026-05-12\", \"probability\": 0.154}, {\"date\": \"2026-05-13\", \"probability\": 0.152}, {\"date\": \"2026-05-14\", \"probability\":
0.151}, {\"date\": \"2026-05-15\", \"probability\": 0.072}, {\"date\": \"2026-05-16\", \"probability\": 0.067}, {\"date\": \"2026-05-17\", \"probability\": 0.048}, {\"date\": \"2026-05-18\",
\"probability\": 0.059}]}], \"query\": \"discord ipo closing market cap\"}"}]}, "hint": null}]}
```

```json
{
  "url": "https://efts.sec.gov/LATEST/search-index?q=%22Discord+Inc%22&forms=S-1",
  "prompt": "Are there any S-1 filings from Discord Inc?"
}
```

### 📋 Result

```
{"url": "https://efts.sec.gov/LATEST/search-index?q=%22Discord+Inc%22&forms=S-1", "content": "Based on the search results, **no, there are no S-1 filings from Discord Inc**. \n\nThe search query for
\"Discord Inc\" with form type S-1 returned only 1 result, but it is for **Neutron Holdings, Inc.** (CIK 0001699963), not Discord Inc. Neutron Holdings filed an S-1 on May 8, 2026.\n\nThe search found
no S-1 filings actually from Discord Inc.\n\nRelevant links:\n- [Neutron Holdings, Inc. S-1 Filing](https://www.sec.gov/cgi-bin/browse-
edgar?action=getcompany&CIK=0001699963&type=S-1&dateb=&owner=exclude&count=100) - The company that appeared in search results (not Discord)"}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.actionnetwork.com/prediction-markets/when-will-discord-officially-announce-an-ipo",
  "prompt": "What are the prediction market probabilities for Discord filing S-1 by various dates? What is the analysis?"
}
```

### 📋 Result

```
{"url": "https://www.actionnetwork.com/prediction-markets/when-will-discord-officially-announce-an-ipo", "content": "## Prediction Market Probabilities\n\n**Current Market Prices (Kalshi):**\n- Before
May 1: 29% YES / 71% NO\n- Before June 1: 31% YES / 69% NO\n- Before July 1: 47% YES / 53% NO\n\n**Overall:** 48% chance Discord files S-1 before July 1, 2026.\n\n## Analysis\n\n**Author's
Assessment:** The market is significantly overpricing the probability. Real probability estimated at **20-25%** for pre-July filing (vs. 48% market price).\n\n**Key Reasons for Skepticism:**\n\n1.
**Compliance Delay:** Discord postponed age verification rollout to H2 2026 after February backlash. They must:\n   - Deploy new on-device biometric systems and credit card verification\n   - Collect
user retention data\n   - Amend SEC filing with this material risk data\n   - Complete SEC review process\n\n2. **Valuation Gap:** Secondary market prices Discord at $7.23B (down 51.8% from 2021's
$15B). IPO would require institutional buyers to pay ~100% premium over current trading price.\n\n3. **Revenue Metrics:** Discord generates only $3.52-$3.63 per user annually vs. Snap's $9/user,
creating weak unit economics for the roadshow.\n\n**Recommended Trade:** Ladder NO positions with July contract having largest edge (+$0.37 per share, author's fair value ~90% vs 53% market
price).\n\n**Risk Factors:** Emergency down-round filing, accelerated engineering timeline, or SEC regulatory carve-out.\n\n---\n\n**Relevant links:**\n- [Flowframe.xyz](https://flowframe.xyz/) -
Author's prediction market tools and content\n- [Kalshi promo code](https://www.actionnetwork.com/online-sports-betting/reviews/prediction-market-apps)\n- [Discord confidential filing news
(Bloomberg/Reuters via FNEX)](https://fnex.com/discord-confidentially-files-for-ipo/)\n- [Discord age verification announcement](https://www.gamedeveloper.com/business/-we-failed-at-our-most-basic-
job-discord-delays-age-verification-rollout)\n- [Persona UK scrutiny](https://www.thehindu.com/sci-tech/technology/discord-postpones-age-verification-rollout-amid-criticism-promises-
transparency/article70678131.ece)\n- [Forge Global valuation data](https://forgeglobal.com/insights/discord-upcoming-ipo-news/)\n- [Discord revenue
statistics](https://www.businessofapps.com/data/discord-statistics/)\n- [Kalshi explainer video](https://www.youtube.com/watch?v=DNy25eaEPWs)", "title": "When Will Discord Officially Announce an
IPO?"}
```

```json
{
  "query": "Discord IPO S-1 public filing news May 2026 latest"
}
```

### 📋 Result

```
{"query": "Discord IPO S-1 public filing news May 2026 latest", "results": [{"title": "When Is the Discord IPO Date? The Popular Chat Platform Is Going Public | CoinCodex", "url":
"https://coincodex.com/article/81997/discord-ipo/", "snippet": "When it comes to the Discord IPO date, the \"going public\" headlines aren't clickbait. Discord reportedly made a real move on January 6
or 7, 2026, when it confidentially filed [IPO paperwork with the U.S. Securities and Exchange Commission (SEC)](https://www.reuters.com/business/chat-platform-discord-confidentially-file-us-ipo-
bloomberg-news-reports-2026-01-06/).\nThat filing stays private at first, so you can't read the full document yet. As of mid-February 2026, there's also no public S-1 on fi", "api_data": null, "hint":
null}, {"title": "Chat Platform Discord Files Confidentially for IPO - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-01-06/chat-platform-discord-is-said-to-file-confidentially-for-
ipo", "snippet": null, "api_data": null, "hint": null}, {"title": "Discord races to IPO in Q1: Can it fetch $25B valuation after rejecting Microsoft? \u2014 TFN", "url":
"https://techfundingnews.com/discord-ipo-q1-25bn-valuation-microsoft-rejection/", "snippet": "Discord has confidentially filed for a US IPO, targeting a Q1 2026 debut after years of private funding,
according to industry reports. The S-1 filing keeps financials confidential for now, but a public filing is expected soon, potentially next month.\nWorking with [Goldman
Sachs](https://techfundingnews.com/goldman-sachs-to-acquire-industry-ventures-in-deal-worth-up-to-965m/) and [JPMorgan](https://techfundingnews.com/founder-with-4m-fake-customers-duped-jpmorgan-
for-175m-worth-of-acquisition/),", "api_data": null, "hint": null}, {"title": "Discord\u2019s IPO bid spotlights community spaces as ad opportunities", "url":
"https://www.emarketer.com/content/discord-s-ipo-bid-spotlights-community-spaces-ad-opportunities", "snippet": "The news: Discord has confidentially filed for an IPO, signaling the company is
preparing for a potential public debut as US tech listings rebound, per Bloomberg.\nDiscord 101: The messaging platform counts more than 200 million monthly users as of December 2025, extending well
beyond gaming into communities built around investing, music, fandoms, and creator-driven culture.\n- The company was last valued near $15 billion in 2021, but secondary-market trading and analyst
estimates suggest a public", "api_data": null, "hint": null}, {"title": "Report: Discord confidentially files for IPO", "url": "https://www.gamedeveloper.com/business/report-discord-confidentially-
files-for-ipo", "snippet": "![A number of Discord mascots and characters showcased in imagery from the Discord website A number of Discord mascots and characters showcased in imagery from the Discord
website](https://eu-
images.contentstack.com/v3/assets/blt740a130ae3c5d529/bltd7354cb342398658/695e4aa79bc72b4ca92f4dcb/Discord_Header.png?width=1280&auto=webp&quality=80&format=jpg&disable=upscale)\nPopular video game
community and chat platform, Discord, has confidentially filed for an initial public offering (IPO).\n[As report", "api_data": null, "hint": null}, {"title": "Discord IPO Watch: Will Discord Stock
Trade in 2026?", "url": "https://accessipos.com/discord-stock-ipo/", "snippet": "Discord IPO Watch: Will Discord Stock Trade in 2026?\nThis page contains links to our partners. We may be compensated
when a link is clicked. [Read the disclosures](https://accessipos.com/legal/) to learn more.\n![Discord logo. Learn how to prepare for the upcoming Discord IPO and explore ways to buy Discord stock.
Follow along as the company approaches its IPO date.](https://accessipos.com/wp-content/uploads/2021/09/DiscordLogo750px.png)\nExplore opportunities to invest in the Discord IPO, anticip", "api_data":
null, "hint": null}, {"title": "Discord IPO Filing: What 2026 Means for Nitro and User Data", "url": "https://www.remio.ai/post/discord-ipo-filing-what-2026-means-for-nitro-and-user-data", "snippet":
"Discord IPO Filing: What 2026 Means for Nitro and User Data\n[Olivia Johnson](https://www.remio.ai/members-area/olivia/profile)- Jan 9\n- 6 min read\n![Discord IPO Filing: What 2026 Means for Nitro
and User Data](https://static.wixstatic.com/media/80334c_5e58ae244e2645698a6324ca902e4274~mv2.png/v1/fill/w_49,h_26,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/80334c_5e58ae244e2645698a6
324ca902e4274~mv2.png)\nIf you have opened Discord anytime in the last six months, the subtle shifts in th", "api_data": null, "hint": null}, {"title": "Insights: Discord Upcoming IPO & Private Stock
Price - Forge", "url": "https://forgeglobal.com/insights/discord-upcoming-ipo-news/", "snippet": null, "api_data": null, "hint": null}, {"title": "Discord's IPO could happen in March | TechCrunch",
"url": "https://techcrunch.com/2026/01/07/discords-ipo-could-happen-in-march/", "snippet": "Wall Street is once again whispering about a potential Discord IPO. Discord, the popular chat and community
platform, filed confidential IPO paperwork with the SEC and has pinned its hopes on a debut in March, [sources told Bloomberg](https://www.bloomberg.com/news/articles/2026-01-06/chat-platform-discord-
is-said-to-file-confidentially-for-ipo). The company hired top-tier tech IPO bankers Goldman Sachs and JPMorgan Chase as its underwriters. Should the tea leaves continue to look positive for t",
"api_data": null, "hint": null}, {"title": "Discord Confidentially Files for IPO, Targeting Potential ...", "url": "https://mlq.ai/news/discord-confidentially-files-for-ipo-targeting-
potential-2026-debut/", "snippet": "Discord Inc. has confidentially filed for an initial public offering with U.S. regulators and is working with Goldman Sachs and JPMorgan Chase on a potential U.S.
listing as early as March 2026, positioning the fast-growing communications platform as one of the larger consumer-technology offerings currently in the IPO pipeline.[1][2][4][5]\nDiscord
Confidentially Files for IPO, Targeting Potential 2026 Debut\nKey Points\n- Discord has confidentially filed IPO paperwork with the U.S. Securities and ", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "\"Discord\" \"S-1\" OR \"IPO\" site:sec.gov OR site:reuters.com OR site:bloomberg.com May 2026"
}
```

### 📋 Result

```
{"query": "\"Discord\" \"S-1\" OR \"IPO\" site:sec.gov OR site:reuters.com OR site:bloomberg.com May 2026", "results": [{"title": "Discord races to IPO in Q1: Can it fetch $25B valuation after
rejecting Microsoft? \u2014 TFN", "url": "https://techfundingnews.com/discord-ipo-q1-25bn-valuation-microsoft-rejection/", "snippet": "Discord has confidentially filed for a US IPO, targeting a Q1
2026 debut after years of private funding, according to industry reports. The S-1 filing keeps financials confidential for now, but a public filing is expected soon, potentially next month.\nWorking
with [Goldman Sachs](https://techfundingnews.com/goldman-sachs-to-acquire-industry-ventures-in-deal-worth-up-to-965m/) and [JPMorgan](https://techfundingnews.com/founder-with-4m-fake-customers-duped-
jpmorgan-for-175m-worth-of-acquisition/),", "api_data": null, "hint": null}, {"title": "Discord IPO: When (Date), Where & What to Expect / Axi", "url":
"https://www.axi.com/int/blog/education/stocks/discord-ipo", "snippet": "Login with
email\n[Home](http://www.axi.com/int)/\n[Blog](http://www.axi.com/int/blog)/\n[Education](http://www.axi.com/int/blog/education)/\n[Stocks](http://www.axi.com/int/blog/education/stocks)/ Discord
IPO\nWhile there is still no date announced, Discord going public is one of the most widely anticipated IPOs on Wall Street. A listing is likely to occur on the New York Stock Exchange (NYSE) or
NASDAQ, and the fundraising round in August 2021 put Discord\u00b4s value at $15 billion.\nThe current market ", "api_data": null, "hint": null}, {"title": "Discord IPO \u2013 how to trade Discord
shares", "url": "https://capital.com/en-int/learn/ipo/discord-ipo", "snippet": "Discord IPO \u2013 how to trade Discord
shares\n![](https://img.capital.com/imgs/blocks/1920x1140x0/shutterstock_2353907093_compressed-rsz_0.jpg)\nLearn about Discord and its upcoming IPO, with its potential price drivers, and how to trade
Discord stock via CFDs when it lists.\nWhen is the Discord IPO date?\nAs of April 2025, Discord has not officially announced a date for its [initial public offering (IPO)](https://capital.com/en-
int/learn/essentials/what-is-an-ipo). However, reports suggest the company", "api_data": null, "hint": null}, {"title": "Discord IPO Closing Market Cap Predictions & Odds 2026 | Polymarket", "url":
"https://polymarket.com/event/discord-ipo-closing-market-cap", "snippet": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\", \"probability\": 0.057, \"volume\": 298539.3585510005,
\"url\": \"https://polymarket.com/event/discord-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on Discord's market capitalization at the
closing price on its first day of trading.\\n\\nIf no IPO occurs by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30, 2026\\\".\\n\\nMarket capitalization expresses the
monetary valu", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"Discord IPO Closing Market Cap\", \"probability\": 0.057, \"volume\": 298539.3585510005, \"url\":
\"https://polymarket.com/event/discord-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on Discord's market capitalization at the closing price
on its first day of trading.\\n\\nIf no IPO occurs by June 30, 2026, 11:59 PM ET, the market will resolve to \\\"No IPO by June 30, 2026\\\".\\n\\nMarket capitalization expresses the monetary value of
a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the
relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In
the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on Discord\\u2019s first day
of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market
will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111615694922589471518709913330752256579066965027597319186712737482564226971621\", \"recent_history\": [{\"date\": \"2026-05-11\", \"probability\": 0.13}, {\"date\": \"2026-05-12\", \"probability\":
0.154}, {\"date\": \"2026-05-13\", \"probability\": 0.152}, {\"date\": \"2026-05-14\", \"probability\": 0.151}, {\"date\": \"2026-05-15\", \"probability\": 0.072}, {\"date\": \"2026-05-16\",
\"probability\": 0.067}, {\"date\": \"2026-05-17\", \"probability\": 0.048}, {\"date\": \"2026-05-18\", \"probability\": 0.059}]}], \"query\": \"discord ipo closing market cap\"}"}]}, "hint": null},
{"title": "Discord\u2019s IPO bid spotlights community spaces as ad opportunities", "url": "https://www.emarketer.com/content/discord-s-ipo-bid-spotlights-community-spaces-ad-opportunities",
"snippet": "The news: Discord has confidentially filed for an IPO, signaling the company is preparing for a potential public debut as US tech listings rebound, per Bloomberg.\nDiscord 101: The
messaging platform counts more than 200 million monthly users as of December 2025, extending well beyond gaming into communities built around investing, music, fandoms, and creator-driven culture.\n-
The company was last valued near $15 billion in 2021, but secondary-market trading and analyst estimates suggest a public", "api_data": null, "hint": null}, {"title": "Insights: Discord Upcoming IPO &
Private Stock Price - Forge", "url": "https://forgeglobal.com/insights/discord-upcoming-ipo-news/", "snippet": null, "api_data": null, "hint": null}, {"title": "Discord IPO 2026: The First Major Tech
IPO Signal of the Year - This with Krish", "url": "https://thiswithkrish.com/discord-ipo-2026-tech-ipo-news/", "snippet": "![Discord confidential IPO filing signals first major tech IPO of
2026](https://thiswithkrish.com/wp-content/uploads/2026/01/Discord-IPO-2026-Tech-Market-Signal.jpg)\nDiscord\u2019s IPO filing may mark the reopening of the tech public markets in 2026.\nDiscord has
officially stepped onto the public-markets runway. The company has confidentially filed for an initial public offering (IPO) in the United States, marking what many analysts are calling the first
major tech IPO headline of 2026.\nAfter several", "api_data": null, "hint": null}, {"title": "Discord Confidentially Files for IPO, Targeting Potential ...", "url": "https://mlq.ai/news/discord-
confidentially-files-for-ipo-targeting-potential-2026-debut/", "snippet": "Discord Inc. has confidentially filed for an initial public offering with U.S. regulators and is working with Goldman Sachs
and JPMorgan Chase on a potential U.S. listing as early as March 2026, positioning the fast-growing communications platform as one of the larger consumer-technology offerings currently in the IPO
pipeline.[1][2][4][5]\nDiscord Confidentially Files for IPO, Targeting Potential 2026 Debut\nKey Points\n- Discord has confidentially filed IPO paperwork with the U.S. Securities and ", "api_data":
null, "hint": null}, {"title": "Discord IPO Watch: Will Discord Stock Trade in 2026?", "url": "https://accessipos.com/discord-stock-ipo/", "snippet": "Discord IPO Watch: Will Discord Stock Trade in
2026?\nThis page contains links to our partners. We may be compensated when a link is clicked. [Read the disclosures](https://accessipos.com/legal/) to learn more.\n![Discord logo. Learn how to
prepare for the upcoming Discord IPO and explore ways to buy Discord stock. Follow along as the company approaches its IPO date.](https://accessipos.com/wp-
content/uploads/2021/09/DiscordLogo750px.png)\nExplore opportunities to invest in the Discord IPO, anticip", "api_data": null, "hint": null}, {"title": "Discord IPO... The price of platforms in the AI
era is changing - \ub354\ubc00\ud06c | The Miilk", "url": "https://themiilk.com/articles/a6530f91a", "snippet": "Discord IPO... The price of platforms in the AI era is changing\n[CEO Focus] Companies
expected to go public in 2026: Discord\nIn 2026, the IPO market will be divided into two segments: A 'blockbuster' year centered on AI startups\nThe trend of the IPO market in 2026 is reviving. It is
not just a phase of resumption of listing. As AI and platform companies prepare to return to the public market, it is said that the market has entered the beginning of a new growth cycle. This year,
large tech \u00b7 It i", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://forgeglobal.com/insights/discord-upcoming-ipo-news/",
  "prompt": "What is the latest news about Discord IPO timeline? Any updates from May 2026? What is the current secondary market valuation?"
}
```

### 📋 Result

```
HTTP 403 for https://forgeglobal.com/insights/discord-upcoming-ipo-news/. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 💭 Thinking

Let me now synthesize all the evidence I've gathered and form my forecast.

## Key Facts:

1. **Today's date**: May 18, 2026
2. **Deadline**: May 30, 2026 (only ~12 days remain)
3. **Current status**: NO S-1 filing on EDGAR as of May 18, 2026 (verified via direct EDGAR search)
4. **Confidential filing**: Discord confidentially filed IPO paperwork in early January 2026
5. **Originally targeted**: March 2026 debut - that window passed without public filing


6. **Underwriters**: Goldman Sachs and JPMorgan

## Prediction Market Data:

The prediction markets are signaling skepticism about a near-term IPO. Polymarket's "No IPO by June 30, 2026" option has been climbing sharply, with the probability of any specific market cap bracket dropping from around 15% on May 12 to under 6% by May 18—suggesting very low odds of an imminent launch. Kalshi's "Before June 1" contract was trading at 31% YES / 69% NO, and expert analysis on ActionNetwork estimated the real probability considerably lower than the market prices.

The main headwinds are age verification compliance delays pushing into late 2026, a significant valuation gap between secondary market pricing (~$7.23B) and Discord's previous peak (~$15B), and weak unit economics that lag far behind competitors like Snap. With other major IPOs like SpaceX capturing market attention, the timing looks increasingly unfavorable.

For Discord to file an S-1 by May 30, they'd need to have already committed to the roadshow phase, which typically precedes pricing by 2-4 weeks. With only 12 days remaining, the window for a decision has essentially closed if they want to hit that deadline.

The evidence pointing to a NO resolution is overwhelming: no S-1 filing yet despite the approaching deadline, the March target already missed, prediction markets showing declining probability from 15% down to under 6%, and zero signals of an imminent filing announcement. A surprise filing in the next 12 days would be the only path to YES, but nothing suggests that's coming.

I'm settling on around 4% probability for a YES outcome, given the multiple headwinds and lack of any positive indicators. Now let me work through the reflection and premortem analysis.

## 💬 Response

Now I have a comprehensive picture. Let me synthesize and run my reflection.

**Key findings:**
- Discord confidentially filed in January 2026, targeting March debut
- March window passed with NO public S-1
- As of May 18, 2026: ZERO S-1 filings on EDGAR (verified via direct search)
- Only 12 days remain until the May 30 deadline
- Polymarket shows IPO probability plummeting: from ~15% on May 12 to ~5.8% on May 18
- Kalshi "Before June 1" was at 31% YES but expert analysis estimated true probability at much lower
- Multiple headwinds: age verification delays to H2 2026, valuation gap ($7.23B secondary vs $15B peak), weak unit economics

## 💬 Response

The reflection shows a large logit gap (4.0) between factor sum (-7.2) and my tentative estimate (-3.2). The factors overwhelmingly point to NO, but factor-implied probability (0.07%) is unrealistically low. My 4% estimate is more reasonable as it accounts for the small but nonzero possibility of a surprise filing. The factors are somewhat correlated (multiple aspects of the same "IPO is delayed" narrative), so the raw sum overestimates their collective weight.
