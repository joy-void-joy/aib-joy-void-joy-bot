# Reasoning Log: Will Alphabet, Microsoft, Apple, Amazon, or Nvidia announce layoffs of 5,000 or more employees between May 1 and May 16, 2026?

*Generated: 2026-05-09T05:34:58.102707+00:00*


## 💭 Thinking

Let me analyze this forecasting question carefully.

The question asks: Will Alphabet, Microsoft, Apple, Amazon, or Nvidia announce layoffs of 5,000 or more employees between May 1 and May 16, 2026?

Key details:
- Window: May 1-16, 2026 (inclusive)
- Today is May 9, 2026
- The question closes May 9 at 06:48:31 UTC
- Resolution: May 17, 2026
- Must be involuntary layoffs (not voluntary buyouts/retirement)
- Must be a single round of 5,000+


- I should check Layoffs.fyi and other sources to see if any announcements have already been made in this window, and assess the likelihood of any coming in the remaining days.

## 💬 Response

I'll start by parsing the question carefully and then research the current state of layoffs for these companies.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43428
  ]
}
```

### 📋 Result

```
{"post_id": 43428, "title": "Will Alphabet, Microsoft, Apple, Amazon, or Nvidia announce layoffs of 5,000 or more employees between May 1 and May 16, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/43428", "background_info": "2026 has been an exceptionally heavy year for Big Tech workforce reductions, with companies citing cost-cutting, restructuring, and AI-
driven efficiency. Notable announcements earlier in 2026 include Amazon eliminating ~16,000 corporate roles in January, Meta announcing ~8,000 layoffs (with cuts beginning May 20, 2026), and Oracle
reportedly cutting tens of thousands of roles. On April 23, 2026, Microsoft announced a voluntary retirement program affecting roughly 8,750 U.S. employees (under a 'Rule of 70' formula), with package
details to be released May 7, 2026 \u2014 but this is voluntary separation, not a forced layoff. Reports also indicate Alphabet/Google plans further headcount reductions in 2026, with prior voluntary
exit packages offered in February 2026.\n\nLayoffs.fyi (https://layoffs.fyi) maintains a live, public tracker of tech layoffs with company name, headcount, and date columns, and is widely cited by
Reuters, CNBC, Bloomberg, and the WSJ. As of late April 2026, no single forced-layoff announcement of 5,000+ employees has been made by Alphabet, Microsoft, Apple, Amazon, or Nvidia in the May
1\u201316, 2026 window.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question
resolves YES if, between May 1, 2026 and May 16, 2026 (inclusive, end of day May 16 UTC), Alphabet/Google, Microsoft, Apple, Amazon, or Nvidia publicly announces a single involuntary workforce
reduction action affecting 5,000 or more employees of that company or its subsidiaries. The announcement may come via the company itself (press release, SEC filing, internal memo reported by media, or
WARN notice) or be reported by [credible sources](https://www.metaculus.com/faq/#definitions). The 5,000+ figure must refer to a single announced round (not a cumulative year-to-date total combining
prior rounds), though multiple simultaneous regional/divisional cuts announced together as one program count as one round.\n\nThe primary reference for verifying headcount and dates is the Layoffs.fyi
tracker (https://layoffs.fyi), filtered to the five listed companies between 5/1/2026 and 5/16/2026. If Layoffs.fyi shows an entry for one of these companies dated within the window with '# Laid Off'
\u2265 5,000, the question resolves YES. Otherwise it resolves NO.", "fine_print": "- 'Layoff' means involuntary workforce reduction. Purely voluntary buyouts, voluntary retirement programs, or
voluntary exit packages do NOT count, even if 5,000+ employees ultimately accept them. Microsoft's April 23, 2026 voluntary retirement program therefore does not count toward resolution. If a
previously voluntary program is converted into mandatory cuts via a new announcement in the window, that new announcement counts.\n- The announcement date (not the effective separation date) must fall
within May 1\u201316, 2026. Re-reporting or restatement of a layoff announced before May 1, 2026 does not count.\n- 'Alphabet' includes Google and all Alphabet subsidiaries; 'Amazon' includes AWS,
Whole Foods, and all Amazon subsidiaries; similarly for the other named companies and their subsidiaries.\n- If reports give a range (e.g., 'up to 7,000'), the lower bound of the range is used for the
threshold check.\n- If Layoffs.fyi is unavailable or has not updated by May 17, 2026, the resolver may rely on direct reporting from credible sources to determine the headcount.", "num_forecasters":
0, "community_prediction": null}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Alphabet Google Microsoft Apple Amazon Nvidia layoffs May 2026",
      "ttl": "6h"
    },
    {
      "query": "Layoffs.fyi tracker big tech May 2026 latest entries",
      "ttl": "6h"
    },
    {
      "query": "Microsoft layoffs 2026 involuntary workforce reduction May",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Alphabet Google Microsoft Apple Amazon Nvidia layoffs May 2026", "entry": {"slug": "alphabet-google-microsoft-apple-amazon-nvidia-layo-abcaaa23", "query": "Alphabet Google
Microsoft Apple Amazon Nvidia layoffs May 2026", "answer": "Now I have enough data to compile a comprehensive report. Here is my synthesis:\n\n---\n\n# Big Tech Layoffs: Alphabet/Google, Microsoft,
Apple, Amazon, Nvidia \u2014 May 2026 Research Report\n\n## Overall 2026 Tech Layoff Landscape\n\nAccording to **layoffs.fyi**, the leading tech layoff tracker (last updated Feb 3, 2026 on the site's
metadata, but data is live via an embedded Airtable), as of early May 2026:\n\n- **101,550 tech employees** have been laid off across **120 tech companies** in 2026 so far\n- This compares to
**124,281** layoffs across 272 companies in all of 2025, **152,922** across 551 companies in 2024, and the peak of **264,320** across 1,193 companies in 2023\n\nThe dominant theme is **AI-driven
restructuring**: companies are citing AI productivity gains as justification for workforce reductions, even during periods of revenue growth.\n\n---\n\n## Company-by-Company Findings\n\n### 1.
Alphabet / Google\n\n**No major layoffs announced in 2026 so far.** No TechCrunch, CNBC, or other major outlet has reported a significant Google/Alphabet layoff event in 2026 (through May 9,
2026).\n\n**2025 context** (from TechCrunch's 2025 layoff tracker):\n- Google cut **100+ design roles** in its cloud division, hitting U.S.-based teams especially hard, as the company shifted focus
toward AI investments (late 2025)\n- Google **downsized its smart TV division** (Google TV / Android TV) by 25% of its ~300-member team; funding cut by 10%, but AI investment was raised (2025)\n-
Google **laid off hundreds** in its platforms and devices division (Android, Pixel, Chrome browser) per The Information (2025)\n- Google offered a **voluntary exit program** to U.S.-based People
Operations employees and cut employees in cloud organization teams in a reorganization (early 2025)\n- Alphabet CEO **Sundar Pichai dismissed AI job fears** and emphasized expansion plans (June
2025)\n\n**Assessment:** Google/Alphabet has not announced new layoffs in 2026 as of May 9, 2026, but conducted multiple rounds of targeted cuts throughout 2025.\n\n---\n\n### 2. Microsoft\n\n**Key
2026 event \u2014 Voluntary Retirement Buyouts (April 23, 2026):**\n- Microsoft offered **voluntary retirement buyouts for the first time** in its 51-year history (reported by CNBC and Bloomberg)\n-
Eligibility: employees whose age + years of service \u2265 70 (e.g., a 52-year-old with 18 years' service)\n- The buyouts reportedly apply to **up to 7% of the U.S. workforce** (~8,750 employees out
of ~125,000 U.S. employees as of June 2025)\n- Microsoft's severance included **accelerated stock vesting**, a minimum of 8 weeks' pay, and 1-2 additional weeks per 6 months of service (per the
Seattle Times)\n\n**2025 context:**\n- Microsoft cut **9,000 employees** (less than 4% of global workforce) in a major round in late 2025\n- Earlier in 2025: cut <1% in January, **6,000+** in May,
**300+** in June, and more in mid-2025\n- Total 2025 headcount stood at ~228,000 globally\n- Microsoft also exited China operations, affecting ~2,000 employees\n\n**Assessment:** Microsoft has not
conducted involuntary mass layoffs in 2026, but the voluntary buyout program (covering up to 8,750 U.S. employees) is the most significant workforce reduction action among the five companies
specifically in 2026.\n\n---\n\n### 3. Apple\n\n**No major layoffs reported in 2026 so far.**\n\n**2025 context:**\n- Apple cut **several sales positions** handling accounts for businesses, schools,
and government agencies as it streamlined its enterprise sales approach (Bloomberg, 2025)\n- These were described as targeted cuts rather than mass layoffs\n\n**Assessment:** Apple has been the most
conservative among the five companies regarding layoffs. No 2026 layoffs have been reported as of May 9, 2026.\n\n---\n\n### 4. Amazon\n\n**Major layoff event \u2014 January 28, 2026:**\n- Amazon
announced **16,000 job cuts** across the company\n- This came just 3 months after laying off **14,000 people** in October 2025\n- SVP of People Experience Beth Galetti said layoffs were for \"reducing
layers, increasing ownership, and removing bureaucracy\"\n- Amazon said some teams hadn't finished their restructuring from the earlier round\n- Galetti stated this is not meant to be a \"new rhythm\"
of broad reductions every few months\n- Amazon CEO Andy Jassy had previously stated the company would need fewer people doing certain jobs due to AI\n- Amazon closed physical Amazon Go and Amazon
Fresh stores, focusing on same-day grocery delivery; plans to open 100 new Whole Foods stores\n- Amazon had 1.57 million employees as of October 2025\n\n**2025 context:**\n- Amazon announced plans to
eliminate **up to 30,000 corporate jobs** (~10% of ~350,000 corporate employees), ultimately pursuing ~14,000 roles\n- Cut **84 jobs** in Seattle/Bellevue (engineering, recruiting, software
development, product management) in late 2025\n- Cut **660 employees** across multiple New York City offices\n- Cut ~**100 employees** from devices and services division (Alexa, Echo, Ring, Zoox)\n-
Cut **100 jobs** at Wondery; reorganized audio operations under Audible\n- Laid off dozens in communications department\n- Total workforce reductions of ~27,000 since start of 2022\n\n**Assessment:**
Amazon conducted the largest single layoff action among these five companies in 2026, with 16,000 cuts in January 2026. No additional May 2026 layoffs have been reported.\n\n---\n\n### 5.
Nvidia\n\n**No layoffs announced in 2026.** In fact, the opposite is the case:\n\n- On **May 4, 2026**, CEO Jensen Huang said at a Milken Institute event that **\"AI creates jobs\"** and called AI the
\"United States' best opportunity to re-industrialize\"\n- Huang dismissed \"AI doomers\" and argued that automating a specific task doesn't replace entire jobs\n- He said his greatest concern is that
people will become \"so afraid of [AI] that they don't actually engage it\"\n- Huang's company continues to benefit from massive AI infrastructure spending\n\n**Assessment:** Nvidia has not conducted
any layoffs in 2026. Jensen Huang has actively argued against the narrative that AI eliminates jobs, though reputable organizations have estimated that up to 15% of U.S. jobs could be eliminated over
the next several years due to AI.\n\n---\n\n## Broader Context: AI as Layoff Justification\n\nA major theme across 2026 is companies citing AI productivity gains as the primary justification for
workforce reductions:\n\n- **Cloudflare** (May 8, 2026): Cut 20% / 1,100 employees, citing 600% increase in internal AI usage in 3 months; CEO said \"these are not cost-cutting exercises\"\n- **Meta**
(April 23, 2026): Planning to cut 10% / 8,000 employees; cuts to begin May 20, 2026\n- **Coinbase** (May 5, 2026): Laid off 14% / ~700 employees; experimenting with \"one-person teams\" using AI\n-
**Oracle** (March 31, 2026): Cut 20,000-30,000 employees\n- **Block** (Jack Dorsey): Halved employee base citing AI\n- **Atlassian**: Cut staff \"in the name of AI\"\n- **Snap** (April 15, 2026): Cut
1,000 jobs (16% of workforce)\n- **Pinterest** (January 27, 2026): Cut 15% of staff, redirecting resources to AI\n\n---\n\n## Summary Table\n\n| Company | 2026 Layoffs (as of May 9) | Key Action |
Date |\n|---------|--------------------------|------------|------|\n| **Amazon** | ~16,000 | Mass layoff (corporate) | Jan 28, 2026 |\n| **Microsoft** | Up to ~8,750 (voluntary) | First-ever voluntary
retirement buyout | Apr 23, 2026 |\n| **Alphabet/Google** | None reported in 2026 | (Multiple rounds in 2025) | N/A |\n| **Apple** | None reported in 2026 | (Minor sales cuts in 2025) | N/A |\n|
**Nvidia** | None | CEO argues AI creates jobs | N/A |", "sources": [{"url": "https://layoffs.fyi/", "title": "Layoffs.fyi - Tech and Startup Layoff Tracker", "domain": "layoffs.fyi", "accessed_at":
"2026-05-09T00:00:00Z", "snippet": "101,550 tech employees laid off across 120 tech companies in 2026; 124,281 in 2025; 152,922 in 2024; 264,320 in 2023"}, {"url":
"https://techcrunch.com/2026/01/28/amazon-says-it-is-laying-off-16000-employees/", "title": "Amazon says it is laying off 16,000 employees", "domain": "techcrunch.com", "accessed_at":
"2026-05-09T00:00:00Z", "snippet": "Amazon cutting 16,000 jobs, coming just 3 months after laying off 14,000 in October 2025. SVP Beth Galetti cited 'reducing layers, increasing ownership, and
removing bureaucracy.'"}, {"url": "https://techcrunch.com/2026/04/23/microsoft-offers-buyout-for-up-to-7-of-u-s-employees/", "title": "Microsoft offers buyout for up to 7% of US employees", "domain":
"techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Microsoft offered voluntary retirement buyouts for the first time in its 51-year history; eligibility: age + years of service >=
70; applies to up to 7% of U.S. workforce (~8,750 employees)"}, {"url": "https://techcrunch.com/2026/05/04/as-workers-worry-about-ai-nvidias-jensen-huang-says-ai-is-creating-an-enormous-number-of-
jobs/", "title": "As workers worry about AI, Nvidia's Jensen Huang says AI is 'creating an enormous number of jobs'", "domain": "techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet":
"Nvidia CEO Jensen Huang at Milken Institute event said 'AI creates jobs' and called AI 'United States' best opportunity to re-industrialize.' Dismissed AI doomers."}, {"url":
"https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/", "title": "Cloudflare says AI made 1,100 jobs obsolete, even as revenue hit a record
high", "domain": "techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Cloudflare cut 20% of workforce (1,100 people); reported record $639.8M quarterly revenue (+34% YoY); CEO said
internal AI usage up 600% in 3 months"}, {"url": "https://techcrunch.com/2026/04/23/meta-job-cuts-10-percent-8000-employees/", "title": "Meta to cut 10% of jobs, or 8,000 employees, report says",
"domain": "techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Meta planning to cut 10% of workforce (8,000 employees); cuts to begin May 20, 2026; also not filling 6,000 open roles"},
{"url": "https://techcrunch.com/2026/05/05/coinbase-to-lay-off-14-of-staff-as-part-of-broader-restructuring/", "title": "Coinbase to lay off 14% of staff as part of broader restructuring", "domain":
"techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Coinbase laying off ~700 employees (14% of staff); expects $50-60M in severance costs; experimenting with 'one-person teams'
combining engineering, design, and product management using AI"}, {"url": "https://techcrunch.com/2026/05/08/laid-off-oracle-workers-tried-to-negotiate-better-severance-oracle-said-no/", "title":
"Laid-off Oracle workers tried to negotiate better severance. Oracle said no.", "domain": "techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Oracle cut estimated 20,000-30,000 people
via email on March 31, 2026. Article compares severance packages across big tech: Microsoft offered accelerated stock vesting, 8+ weeks pay; Cloudflare offered base pay through end of 2026 plus
accelerated vesting through Aug 15"}, {"url": "https://techcrunch.com/2025/12/22/tech-layoffs-2025-list/", "title": "A comprehensive list of 2025 tech layoffs", "domain": "techcrunch.com",
"accessed_at": "2026-05-09T00:00:00Z", "snippet": "Comprehensive 2025 list: Google cut 100+ cloud design roles, downsized smart TV division by 25%, laid off hundreds in platforms/devices. Microsoft
cut 9,000 in late 2025, 6,500+ in May 2025. Amazon cut 14,000+. Apple cut several sales positions."}], "key_facts": ["As of early May 2026, 101,550 tech employees have been laid off across 120 tech
companies in 2026 (layoffs.fyi tracker)", "Amazon announced 16,000 job cuts on January 28, 2026, just three months after laying off 14,000 in October 2025; Amazon had 1.57 million total employees as
of October 2025", "Microsoft offered voluntary retirement buyouts for the first time in its 51-year history on April 23, 2026, covering up to 7% of U.S. workforce (~8,750 employees); eligibility
requires age + years of service \u2265 70", "Microsoft's severance included accelerated stock vesting, minimum 8 weeks' pay, plus 1-2 additional weeks per 6 months of service", "Alphabet/Google has
NOT announced any major layoffs in 2026, though it conducted multiple targeted rounds in 2025 (100+ cloud design roles, 25% of smart TV division, hundreds in platforms & devices)", "Apple has NOT
announced any layoffs in 2026; it made only minor targeted sales cuts in 2025", "Nvidia has NOT announced any layoffs in 2026; CEO Jensen Huang stated on May 4, 2026 that 'AI creates jobs' and called
AI the U.S.'s best opportunity to re-industrialize", "Meta announced plans to cut 10% / 8,000 employees on April 23, 2026, with cuts beginning May 20", "Oracle cut an estimated 20,000-30,000 employees
on March 31, 2026", "Cloudflare cut 20% / 1,100 employees on May 8, 2026, citing 600% increase in internal AI usage in 3 months", "Coinbase laid off 14% / ~700 employees on May 5, 2026, experimenting
with 'one-person teams' using AI", "AI-driven restructuring is the dominant theme: companies are citing AI productivity gains as justification for workforce reductions even during revenue growth
periods", "Microsoft had ~228,000 global employees and ~125,000 U.S. employees as of mid-2025", "In 2025, Microsoft cut a total of ~9,000+ employees across multiple rounds", "Reputable financial and
academic organizations have estimated that up to 15% of U.S. jobs could be eliminated over the next several years due to AI"], "data_points": [{"metric": "Total tech employees laid off in 2026 (YTD)",
"value": 101550.0, "unit": "employees", "as_of": "2026-05-09", "source_url": "https://layoffs.fyi/"}, {"metric": "Total tech companies with layoffs in 2026 (YTD)", "value": 120.0, "unit": "companies",
"as_of": "2026-05-09", "source_url": "https://layoffs.fyi/"}, {"metric": "Total tech employees laid off in 2025", "value": 124281.0, "unit": "employees", "as_of": "2025-12-31", "source_url":
"https://layoffs.fyi/"}, {"metric": "Total tech employees laid off in 2024", "value": 152922.0, "unit": "employees", "as_of": "2024-12-31", "source_url": "https://layoffs.fyi/"}, {"metric": "Total
tech employees laid off in 2023", "value": 264320.0, "unit": "employees", "as_of": "2023-12-31", "source_url": "https://layoffs.fyi/"}, {"metric": "Amazon layoffs announced January 2026", "value":
16000.0, "unit": "employees", "as_of": "2026-01-28", "source_url": "https://techcrunch.com/2026/01/28/amazon-says-it-is-laying-off-16000-employees/"}, {"metric": "Amazon layoffs October 2025",
"value": 14000.0, "unit": "employees", "as_of": "2025-10-01", "source_url": "https://techcrunch.com/2026/01/28/amazon-says-it-is-laying-off-16000-employees/"}, {"metric": "Amazon total employees (as
of Oct 2025)", "value": 1570000.0, "unit": "employees", "as_of": "2025-10-01", "source_url": "https://techcrunch.com/2026/01/28/amazon-says-it-is-laying-off-16000-employees/"}, {"metric": "Microsoft
voluntary buyout eligibility (% of U.S. workforce)", "value": 7.0, "unit": "percent", "as_of": "2026-04-23", "source_url": "https://techcrunch.com/2026/04/23/microsoft-offers-buyout-for-up-to-7-of-u-
s-employees/"}, {"metric": "Microsoft estimated U.S. employees eligible for buyout", "value": 8750.0, "unit": "employees", "as_of": "2026-04-23", "source_url":
"https://techcrunch.com/2026/04/23/microsoft-offers-buyout-for-up-to-7-of-u-s-employees/"}, {"metric": "Microsoft estimated U.S. employees (as of June 2025)", "value": 125000.0, "unit": "employees",
"as_of": "2025-06-01", "source_url": "https://techcrunch.com/2026/04/23/microsoft-offers-buyout-for-up-to-7-of-u-s-employees/"}, {"metric": "Microsoft global employees (as of June 2025)", "value":
228000.0, "unit": "employees", "as_of": "2025-06-01", "source_url": "https://techcrunch.com/2025/12/22/tech-layoffs-2025-list/"}, {"metric": "Microsoft layoffs in late 2025", "value": 9000.0, "unit":
"employees", "as_of": "2025-12-01", "source_url": "https://techcrunch.com/2025/12/22/tech-layoffs-2025-list/"}, {"metric": "Meta planned layoffs (10% of workforce)", "value": 8000.0, "unit":
"employees", "as_of": "2026-04-23", "source_url": "https://techcrunch.com/2026/04/23/meta-job-cuts-10-percent-8000-employees/"}, {"metric": "Cloudflare layoffs (20% of workforce)", "value": 1100.0,
"unit": "employees", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/"}, {"metric": "Cloudflare Q1
2026 revenue", "value": 639.8, "unit": "million USD", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-
high/"}, {"metric": "Oracle estimated layoffs March 2026", "value": 25000.0, "unit": "employees (estimated 20,000-30,000)", "as_of": "2026-03-31", "source_url":
"https://techcrunch.com/2026/05/08/laid-off-oracle-workers-tried-to-negotiate-better-severance-oracle-said-no/"}, {"metric": "Coinbase layoffs (14% of staff)", "value": 700.0, "unit": "employees",
"as_of": "2026-05-05", "source_url": "https://techcrunch.com/2026/05/05/coinbase-to-lay-off-14-of-staff-as-part-of-broader-restructuring/"}, {"metric": "Coinbase expected severance costs", "value":
55.0, "unit": "million USD (range $50-60M)", "as_of": "2026-05-05", "source_url": "https://techcrunch.com/2026/05/05/coinbase-to-lay-off-14-of-staff-as-part-of-broader-restructuring/"}, {"metric":
"Snap layoffs (16% of workforce)", "value": 1000.0, "unit": "employees", "as_of": "2026-04-15", "source_url": "https://techcrunch.com/tag/layoffs/"}], "created_at": "2026-05-09T05:28:46.968901Z",
"updated_at": "2026-05-09T05:28:46.968901Z", "stale_after": "2026-05-09T11:28:46.968901Z", "state": "fresh", "revision_history": [], "session_id": "70c57145-0a31-43f7-b943-eb002bd70ff7",
"follow_up_count": 0}, "is_follow_up": false}, {"query": "Layoffs.fyi tracker big tech May 2026 latest entries", "entry": {"slug": "layoffs-fyi-tracker-big-tech-may-2026-latest-entri-8b01fe2a",
"query": "Layoffs.fyi tracker big tech May 2026 latest entries", "answer": "\n\n## Layoffs.fyi Tracker: Big Tech Layoffs \u2014 May 2026 Latest Entries\n\n### Layoffs.fyi Cumulative Statistics (as of
~May 9, 2026)\n\n| Year | Tech Employees Laid Off | Companies with Layoffs |\n|------|------------------------|----------------------|\n| **2026** | **101,550** | **120** |\n| 2025 | 124,281 | 272
|\n| 2024 | 152,922 | 551 |\n| 2023 | 264,320 | 1,193 |\n| 2022 | 165,269 | 1,064 |\n\nAs of approximately May 8\u20139, 2026, over **101,550 tech employees** have been laid off across **120
companies** in 2026. Broader counts (including adjacent industries) reach **128,000+** per Yahoo Tech.\n\n---\n\n### May 2026 Specific Entries\n\n**Cloudflare** \u2014 May 8, 2026\n- **1,100
employees** cut (~20% of workforce)\n- CEO Matthew Prince cited AI making jobs \"obsolete\"; internal AI usage up 600% in three months\n- Record Q1 revenue of $639.8M (up 34% YoY) despite cuts\n-
Sources: TechCrunch, San Francisco Chronicle\n\n**Coinbase** \u2014 May 5, 2026\n- **~700 employees** cut (14% of staff)\n- CEO Brian Armstrong cited crypto market volatility and AI-driven
efficiency\n- Severance costs: $50\u201360 million; flattening org structure\n- Source: TechCrunch\n\n**Meta** \u2014 Announced April 23; first wave targets **May 20, 2026**\n- **8,000 employees** to
be cut (10% of workforce)\n- 6,000 open roles frozen/unfilled\n- Earlier 2026 rounds: ~1,000 (Reality Labs, January), several hundred (March)\n- **Total Meta 2026 layoffs: ~10,000+**\n- Sources:
TechCrunch, Reuters, Bloomberg, CNBC\n\n**Truecaller** \u2014 May 8, 2026\n- **70 employees** (~15% of workforce)\n- Ad revenue down 44% YoY; net sales down 27%\n- Source: TechCrunch\n\n**Disney**
\u2014 Early May 2026\n- Layoffs reported, company touting \"Culture of Efficiency\"\n- Source: Deadline (May 6)\n\n---\n\n### Big Tech 2026 Year-to-Date Summary (through May 9)\n\n| Company | 2026
Total Layoffs | Key Details |\n|---------|-------------------|-------------|\n| **Amazon** | ~30,000\u201332,000 | 16,000 (Jan 28) + 16,000 (Apr 21); plans to hire 11,000 engineers |\n| **Meta** |
~10,000+ | Multiple rounds; largest wave (8,000) starts May 20 |\n| **Microsoft** | Up to ~8,750 | Voluntary buyouts/retirement (\"Rule of 70\") offered Apr 23 |\n| **Block (Square)** | 4,000+ | ~50%
of workforce (Feb 26); AI cited |\n| **Atlassian** | 1,600 | Mar 11\u201312; AI and enterprise pivot |\n| **Cloudflare** | 1,100 | May 8; AI-driven restructuring |\n| **Snap** | 1,000 | Apr 15 (16% of
workforce); AI cited |\n| **Epic Games** | 1,000 | Mar 24; Fortnite engagement decline |\n| **eBay** | 800 | Feb 26 |\n| **Coinbase** | ~700 | May 5; crypto volatility + AI |\n\n---\n\n### Macro
Context\n\n- **AI is the dominant driver**: 26% of April 2026 job cuts were explicitly attributed to AI (CBS News, May 8). Companies report record revenues while cutting staff, citing AI productivity
gains.\n- **Tech is an outlier**: Overall corporate layoffs are down 10% YoY, but tech layoffs are accelerating (WSJ, May 8).\n- **Spending shift**: Headlines note \"tens of thousands\" of tech
workers replaced by $725 billion in AI infrastructure spending directed at just four companies (24/7 Wall St, May 7).\n- **Scale concern**: CNBC (May 1) flagged 20,000+ job cuts at Meta and Microsoft
alone as evidence the \"AI-driven labor crisis is here.\"", "sources": [{"url": "https://layoffs.fyi", "title": "Layoffs.fyi - Tech Layoff Tracker", "domain": "layoffs.fyi", "accessed_at":
"2026-05-09T00:00:00Z", "snippet": "Tracks 101,550 tech employees laid off across 120 companies in 2026; cumulative data from 2022-2026."}, {"url": "https://techcrunch.com/tag/layoffs/", "title":
"TechCrunch Layoffs Coverage", "domain": "techcrunch.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Coverage of Cloudflare (1,100), Coinbase (~700), Truecaller (70), Meta (8,000) layoffs in
May 2026."}, {"url": "https://www.cbsnews.com", "title": "CBS News - AI accounts for 26% of April job cuts", "domain": "cbsnews.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "AI emerges as a
top cause of layoffs, accounting for 26% of April's job cuts (May 8, 2026)."}, {"url": "https://www.wsj.com", "title": "WSJ - Corporate Layoffs Down 10% but AI Reckoning in Tech", "domain": "wsj.com",
"accessed_at": "2026-05-09T00:00:00Z", "snippet": "Corporate Layoffs Are Down 10% This Year, but the AI Reckoning Has Come for Tech (May 8, 2026)."}, {"url": "https://www.cnbc.com", "title": "CNBC -
20,000 job cuts at Meta, Microsoft raise AI labor crisis concern", "domain": "cnbc.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "20,000 job cuts at Meta, Microsoft raise concern that AI-
driven labor crisis is here (May 1, 2026)."}, {"url": "https://www.reuters.com", "title": "Reuters - Meta Layoffs Coverage", "domain": "reuters.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet":
"Coverage of Meta's 8,000-person layoff announcement and restructuring."}, {"url": "https://www.bloomberg.com", "title": "Bloomberg - Tech Layoffs 2026", "domain": "bloomberg.com", "accessed_at":
"2026-05-09T00:00:00Z", "snippet": "Coverage of major tech layoffs including Meta, Amazon, and Microsoft in 2026."}, {"url": "https://247wallst.com", "title": "24/7 Wall St - $725B Replacing Tens of
Thousands of Tech Workers", "domain": "247wallst.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Tens of thousands of tech workers being replaced by $725 billion in AI infrastructure spending
going to four companies (May 7, 2026)."}, {"url": "https://www.deadline.com", "title": "Deadline - Disney Layoffs May 2026", "domain": "deadline.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet":
"Disney layoffs reported with company touting 'Culture of Efficiency' (May 6, 2026)."}, {"url": "https://finance.yahoo.com", "title": "Yahoo Finance - Layoffs Accelerate in May 2026", "domain":
"finance.yahoo.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "More than 128,000 people laid off in tech in 2026; layoffs accelerating as firms restructure around AI."}], "key_facts":
["Layoffs.fyi tracks 101,550 tech employees laid off across 120 companies in 2026 as of ~May 9, 2026.", "Cloudflare cut 1,100 employees (~20% of workforce) on May 8, 2026, citing AI making jobs
obsolete; internal AI usage up 600% in three months.", "Coinbase cut ~700 employees (14% of staff) on May 5, 2026, citing crypto volatility and AI efficiency.", "Meta announced 8,000 layoffs (10% of
workforce) on April 23, with first wave targeting May 20, 2026; total 2026 Meta layoffs ~10,000+.", "Truecaller cut 70 employees (~15% of workforce) on May 8, 2026, due to 44% YoY decline in ad
revenue.", "Amazon has cut ~30,000-32,000 jobs in 2026 (16,000 in January + 16,000 in April), making it the largest big tech layoff of the year.", "Microsoft offered voluntary buyouts to ~8,750 U.S.
employees using 'Rule of 70' (age + years of service >= 70) around April 23, 2026.", "26% of April 2026 job cuts were explicitly attributed to AI according to CBS News (May 8).", "Overall corporate
layoffs are down 10% YoY, but tech sector layoffs are accelerating (WSJ, May 8).", "Broader counts including adjacent industries place 2026 layoffs at 128,000+ (Yahoo Tech).", "Block (Square/Cash App)
cut 4,000+ employees (~50% of workforce) in February 2026, one of the most dramatic single cuts.", "Companies are simultaneously reporting record revenues while cutting staff, citing AI productivity
gains as justification."], "data_points": [{"metric": "Total tech employees laid off in 2026 (Layoffs.fyi)", "value": 101550.0, "unit": "employees", "as_of": "2026-05-09", "source_url":
"https://layoffs.fyi"}, {"metric": "Number of companies with layoffs in 2026 (Layoffs.fyi)", "value": 120.0, "unit": "companies", "as_of": "2026-05-09", "source_url": "https://layoffs.fyi"},
{"metric": "Cloudflare layoffs (May 2026)", "value": 1100.0, "unit": "employees", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Cloudflare workforce
reduction percentage", "value": 20.0, "unit": "percent", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Cloudflare Q1 2026 revenue", "value": 639.8, "unit":
"million USD", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Cloudflare Q1 2026 revenue YoY growth", "value": 34.0, "unit": "percent", "as_of": "2026-05-08",
"source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Coinbase layoffs (May 2026)", "value": 700.0, "unit": "employees", "as_of": "2026-05-05", "source_url":
"https://techcrunch.com/tag/layoffs/"}, {"metric": "Coinbase workforce reduction percentage", "value": 14.0, "unit": "percent", "as_of": "2026-05-05", "source_url":
"https://techcrunch.com/tag/layoffs/"}, {"metric": "Meta layoffs announced April 2026 (first wave May 20)", "value": 8000.0, "unit": "employees", "as_of": "2026-04-23", "source_url":
"https://techcrunch.com/tag/layoffs/"}, {"metric": "Meta total 2026 layoffs (all rounds)", "value": 10000.0, "unit": "employees", "as_of": "2026-05-09", "source_url":
"https://techcrunch.com/tag/layoffs/"}, {"metric": "Amazon total 2026 layoffs", "value": 32000.0, "unit": "employees", "as_of": "2026-05-09", "source_url": "https://layoffs.fyi"}, {"metric":
"Microsoft voluntary buyouts offered", "value": 8750.0, "unit": "employees", "as_of": "2026-04-23", "source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Truecaller layoffs (May 2026)",
"value": 70.0, "unit": "employees", "as_of": "2026-05-08", "source_url": "https://techcrunch.com/tag/layoffs/"}, {"metric": "Percentage of April 2026 job cuts attributed to AI", "value": 26.0, "unit":
"percent", "as_of": "2026-05-08", "source_url": "https://www.cbsnews.com"}, {"metric": "YoY change in overall corporate layoffs", "value": -10.0, "unit": "percent", "as_of": "2026-05-08",
"source_url": "https://www.wsj.com"}, {"metric": "Block (Square) layoffs Feb 2026", "value": 4000.0, "unit": "employees", "as_of": "2026-02-26", "source_url": "https://layoffs.fyi"}, {"metric": "Snap
layoffs Apr 2026", "value": 1000.0, "unit": "employees", "as_of": "2026-04-15", "source_url": "https://layoffs.fyi"}, {"metric": "Atlassian layoffs Mar 2026", "value": 1600.0, "unit": "employees",
"as_of": "2026-03-12", "source_url": "https://layoffs.fyi"}, {"metric": "Epic Games layoffs Mar 2026", "value": 1000.0, "unit": "employees", "as_of": "2026-03-24", "source_url":
"https://layoffs.fyi"}, {"metric": "2025 total tech layoffs (Layoffs.fyi)", "value": 124281.0, "unit": "employees", "as_of": "2025-12-31", "source_url": "https://layoffs.fyi"}, {"metric": "2024 total
tech layoffs (Layoffs.fyi)", "value": 152922.0, "unit": "employees", "as_of": "2024-12-31", "source_url": "https://layoffs.fyi"}, {"metric": "2023 total tech layoffs (Layoffs.fyi)", "value": 264320.0,
"unit": "employees", "as_of": "2023-12-31", "source_url": "https://layoffs.fyi"}], "created_at": "2026-05-09T05:28:32.550914Z", "updated_at": "2026-05-09T05:28:32.550914Z", "stale_after":
"2026-05-09T11:28:32.550914Z", "state": "fresh", "revision_history": [], "session_id": "8cd71db6-6353-4e3a-bb96-3c3215b96ae3", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Microsoft
layoffs 2026 involuntary workforce reduction May", "entry": {"slug": "microsoft-layoffs-2026-involuntary-workforce-reduc-6c51042e", "query": "Microsoft layoffs 2026 involuntary workforce reduction
May", "answer": "Now I have enough information to compile a comprehensive report. Let me synthesize all findings.\n\n---\n\n# Microsoft Workforce Reductions 2026: Comprehensive Research Report\n\n##
Executive Summary\n\nAs of May 9, 2026, Microsoft's 2026 workforce reduction strategy has primarily centered on a **voluntary retirement buyout program** \u2014 the first in the company's history
\u2014 rather than involuntary mass layoffs. However, this is occurring alongside broader industry-wide cuts, with Bloomberg reporting that **Meta and Microsoft together may affect up to 23,000
jobs**. The evidence for a specific *involuntary* workforce reduction at Microsoft in May 2026 is limited; the dominant story is the voluntary program announced in late April 2026.\n\n## Key
Findings\n\n### 1. Voluntary Retirement Buyout Program (Announced April 23, 2026)\n\n- **Scale**: Microsoft plans to offer voluntary buyouts to approximately **8,750 U.S. employees**, representing
about **7% of its U.S. workforce** (~125,000 U.S. employees implied).\n- **Announcement**: Microsoft's Chief People Officer **Amy Coleman** sent an internal memo announcing the voluntary retirement
plan on **April 23, 2026** (CNBC, GeekWire, NYT, CNN, Al Jazeera all confirmed).\n- **Program Name**: Referred to as the **\"Rule of 70\"** retirement buyout, where eligibility is based on the sum of
an employee's age + years of service equaling 70 or more.\n- **Offers to be made**: In **early May 2026**, with details shared with eligible employees on **May 7, 2026** (GeekWire, published May
7).\n- **This is a first**: Multiple outlets (CNBC, CNN, GeekWire, Engadget, NYT) confirm this is the **first time** Microsoft has offered a voluntary retirement/buyout program.\n\n### 2. Buyout
Package Details (as of May 7, 2026)\n\nPer the GeekWire article (May 7, 2026) and Business Insider's internal document report (May 7, 2026):\n- **Cash payments**: Up to **9 months of base pay**\n-
**Healthcare coverage**: Up to **5 years** of continued healthcare (COBRA)\n- **Stock vesting**: Continued stock vesting as part of the package\n- Key executives mentioned: **Amy Coleman** (Chief
People Officer), **Amy Hood** (CFO)\n\n### 3. Motivation: AI Spending Pivot\n\n- Multiple sources (CNBC, The Guardian, Al Jazeera, Bloomberg, Forbes) cite **AI investment** as the primary driver.
Microsoft has spent billions on data centers and AI infrastructure.\n- CNBC headline (April 24, 2026): \"20,000 job cuts at Meta, Microsoft raise concern that AI-driven labor crisis is here\"\n-
Fortune (April 26, 2026): Explored why companies like Microsoft are offering voluntary buyouts *instead* of laying off workers\n- Forbes (April 24, 2026): \"Microsoft Offers Soft Landing While Others
Lay Off In The Age Of AI\"\n\n### 4. Involuntary Layoffs: What We Know\n\n- **No confirmed reports of a specific involuntary mass layoff in May 2026** have been found in the news coverage as of May 9,
2026.\n- The overwhelming coverage frames Microsoft's approach as *voluntary* rather than involuntary, contrasting it with Meta's involuntary layoffs (8,000 jobs cut).\n- **March 2026**: AI CERTs
reported on \"Microsoft's Tech Corporate Restructuring: Quiet Cuts Unpacked\" (March 11, 2026), suggesting some smaller-scale, unreported reductions were happening.\n- **March 2026**: Business Insider
reported \"Microsoft Makes Sweeping Overhaul of HR Organization\" (March 25, 2026).\n- **January 2026**: Rumors of massive involuntary layoffs circulated, but Microsoft's communications VP **Frank
Shaw** called them **\"100% made up\"** (GameSpot, Yahoo Finance, Seattle Times, January 7-8, 2026).\n- **Earlier layoffs for context**: Microsoft cut approximately **6,300 jobs in 2025**
(CapacityGlobal, October 2025).\n\n### 5. Industry Context\n\n- **Bloomberg** (April 23, 2026): \"Meta, Microsoft Plan Cuts, Buyouts That May Affect 23,000 Jobs\" \u2014 this combined number includes
Meta's ~15,000 (8,000 immediate) and Microsoft's ~8,750 buyout offers.\n- **Tech Times** (May 4, 2026): \"Big Tech Slashed 80,000 Jobs in Early 2026\"\n- **Times of India** (May 2, 2026): \"Tech
Layoffs cross 92,000 in April, making 2026 the worst year for tech employees ever\"\n- **CNBC** (April 24, 2026): Combined 20,000+ job cuts at Meta and Microsoft\n\n### 6. Timeline of Microsoft 2026
Workforce Events\n\n| Date | Event | Source |\n|------|-------|--------|\n| Jan 5-8, 2026 | Rumors of mass layoffs circulate; Microsoft denies | HR Digest, Seattle Times, GameSpot |\n| Mar 11, 2026 |
Reports of \"quiet cuts\" / restructuring | AI CERTs |\n| Mar 25, 2026 | Sweeping HR organization overhaul | Business Insider |\n| Apr 21, 2026 | Reports: \"Microsoft may announce massive layoffs in
coming weeks\" | Instant Gaming News |\n| Apr 23, 2026 | Amy Coleman memo announcing voluntary retirement buyout program | CNBC, NYT, Bloomberg, CNN, Guardian, Al Jazeera |\n| Apr 24, 2026 | Combined
Meta+Microsoft cuts framed as AI-driven crisis | CNBC, Forbes, Fast Company |\n| May 7, 2026 | Eligible employees learn details of buyout offer | GeekWire, Business Insider |\n| May 9, 2026 |
InformationWeek updates 2026 tech layoffs tracker | InformationWeek |\n\n## Assessment: Involuntary vs. Voluntary\n\nThe current evidence strongly suggests that Microsoft's May 2026 workforce
reduction is **primarily voluntary**, structured as the \"Rule of 70\" retirement buyout. This contrasts notably with Meta's simultaneous involuntary layoffs. However:\n\n1. There may be **involuntary
layoffs that follow** if insufficient numbers of employees accept the voluntary buyout\n2. \"Quiet cuts\" and smaller-scale involuntary reductions may be ongoing but unreported at scale\n3. The April
21 report of \"massive layoffs in coming weeks\" has not yet materialized as a distinct involuntary event separate from the buyout program\n4. Some reporting (especially non-US outlets) blurs the
voluntary/involuntary distinction\n\n---", "sources": [{"url": "https://www.cnbc.com/2026/04/23/microsoft-plans-first-ever-voluntary-employee-buyout.html", "title": "Microsoft plans first-ever
voluntary employee buyout for up to 7% of U.S. workforce", "domain": "cnbc.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Microsoft's chief people officer Amy Coleman announcing the
voluntary retirement plan targeting 7% of US workforce."}, {"url": "https://www.geekwire.com/2026/microsoft-employees-learn-details-of-voluntary-retirement-package-heres-what-the-company-is-
offering/", "title": "Microsoft employees learn details of voluntary retirement package: Here's what the company is offering", "domain": "geekwire.com", "accessed_at": "2026-05-09T00:00:00Z",
"snippet": "Microsoft employees eligible for the company's first-ever voluntary retirement program learned the details Thursday, including cash payments of up to nine months of base pay, up to five
years of healthcare coverage, and continued stock vesting."}, {"url": "https://www.aljazeera.com/economy/2026/4/23/meta-lines-up-layoffs-while-microsoft-offers-buyouts", "title": "Meta lines up
layoffs while Microsoft offers buyouts", "domain": "aljazeera.com", "accessed_at": "2026-05-09T00:00:00Z", "snippet": "Meta will lay off 8,000 workers while Microsoft is offering buyouts to 8,750
people, a first for the Windows maker. The software giant plans to make the offers in early May to about 8,750 people, or 7 percent of its US workforce."}, {"url":
"https://www.nytimes.com/2026/04/23/technology/microsoft-buyout-workers.html", "title": "Microsoft Targets About 7% of Its U.S. Workers With Buyout Offer", "domain": "nytimes.com", "accessed_at":
"2026-05-09T00:00:00Z"}, {"url": "https://www.bloomberg.com/news/articles/2026-04-23/meta-microsoft-plan-cuts-buyouts-that-may-affect-23000-jobs", "title": "Meta, Microsoft Plan Cuts, Buyouts That May
Affect 23,000 Jobs", "domain": "bloomberg.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.cnn.com/2026/04/24/tech/microsoft-voluntary-retirement-buyout", "title": "Microsoft to
offer voluntary retirement to thousands of US employees for the first time", "domain": "cnn.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url":
"https://www.theguardian.com/technology/2026/apr/23/microsoft-meta-layoffs-ai", "title": "Microsoft and Meta announce large staff reductions as they spend big on AI", "domain": "theguardian.com",
"accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.cnbc.com/2026/04/24/20000-job-cuts-meta-microsoft-ai-labor-crisis.html", "title": "20,000 job cuts at Meta, Microsoft raise concern that
AI-driven labor crisis is here", "domain": "cnbc.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.businessinsider.com/microsoft-buyout-offer-internal-document-2026", "title":
"Internal Microsoft document spells out the company's buyout offer", "domain": "businessinsider.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.forbes.com/2026/04/24/microsoft-soft-
landing-layoffs-ai/", "title": "Microsoft Offers Soft Landing While Others Lay Off In The Age Of AI", "domain": "forbes.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url":
"https://fortune.com/2026/04/26/microsoft-voluntary-buyouts-instead-of-laying-off-workers/", "title": "Here's why companies like Microsoft are offering voluntary buyouts instead of laying off
workers", "domain": "fortune.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.informationweek.com/it-leadership/2026-tech-company-layoffs", "title": "2026 tech company layoffs",
"domain": "informationweek.com", "accessed_at": "2026-05-09T00:00:00Z"}, {"url": "https://www.geekwire.com/2026/microsoft-will-offer-voluntary-retirement-to-thousands-of-employees-in-a-first-for-tech-
giant/", "title": "Microsoft will offer voluntary retirement to thousands of employees in a first for tech giant", "domain": "geekwire.com", "accessed_at": "2026-05-09T00:00:00Z"}], "key_facts":
["Microsoft announced its first-ever voluntary retirement buyout program on April 23, 2026, via an internal memo from Chief People Officer Amy Coleman.", "The buyout targets approximately 8,750 U.S.
employees, representing about 7% of Microsoft's U.S. workforce.", "Eligibility uses the 'Rule of 70': employee's age plus years of service must equal 70 or more.", "Buyout package includes up to 9
months of base pay, up to 5 years of healthcare coverage (COBRA), and continued stock vesting (details shared May 7, 2026).", "Bloomberg reported Meta and Microsoft together may affect up to 23,000
jobs (April 23, 2026).", "CNBC reported 20,000+ combined job cuts at Meta and Microsoft, raising concerns about an 'AI-driven labor crisis' (April 24, 2026).", "No confirmed involuntary mass layoff at
Microsoft has been reported in May 2026 as of May 9.", "In January 2026, Microsoft's Frank Shaw called mass layoff rumors '100% made up'.", "Microsoft reportedly conducted 'quiet cuts' and an HR
organization overhaul in March 2026.", "Big Tech collectively slashed approximately 80,000-92,000 jobs in early 2026 according to industry trackers.", "Microsoft's primary stated motivation is
pivoting resources toward AI infrastructure and data centers.", "Forbes characterized Microsoft's approach as offering a 'soft landing' compared to involuntary layoffs at other tech companies.",
"Microsoft had approximately 125,000 U.S. employees (implied by 7% = 8,750 figure).", "Microsoft cut approximately 6,300 jobs in 2025."], "data_points": [{"metric": "Microsoft voluntary buyout target
(U.S. employees)", "value": 8750.0, "unit": "employees", "as_of": "2026-04-23", "source_url": "https://www.cnbc.com/2026/04/23/microsoft-plans-first-ever-voluntary-employee-buyout.html"}, {"metric":
"Percentage of U.S. workforce targeted for buyout", "value": 7.0, "unit": "percent", "as_of": "2026-04-23", "source_url": "https://www.nytimes.com/2026/04/23/technology/microsoft-buyout-
workers.html"}, {"metric": "Buyout cash payment (maximum)", "value": 9.0, "unit": "months of base pay", "as_of": "2026-05-07", "source_url": "https://www.geekwire.com/2026/microsoft-employees-learn-
details-of-voluntary-retirement-package-heres-what-the-company-is-offering/"}, {"metric": "Buyout healthcare coverage (maximum)", "value": 5.0, "unit": "years", "as_of": "2026-05-07", "source_url":
"https://www.geekwire.com/2026/microsoft-employees-learn-details-of-voluntary-retirement-package-heres-what-the-company-is-offering/"}, {"metric": "Combined Meta + Microsoft jobs at risk", "value":
23000.0, "unit": "jobs", "as_of": "2026-04-23", "source_url": "https://www.bloomberg.com/news/articles/2026-04-23/meta-microsoft-plan-cuts-buyouts-that-may-affect-23000-jobs"}, {"metric": "Combined
Meta + Microsoft confirmed job cuts", "value": 20000.0, "unit": "jobs", "as_of": "2026-04-24", "source_url": "https://www.cnbc.com/2026/04/24/20000-job-cuts-meta-microsoft-ai-labor-crisis.html"},
{"metric": "Big Tech jobs slashed in early 2026", "value": 80000.0, "unit": "jobs", "as_of": "2026-05-04", "source_url": "https://www.techtimes.com/articles/big-tech-slashed-80000-jobs-
early-2026.htm"}, {"metric": "Tech layoffs in April 2026", "value": 92000.0, "unit": "jobs", "as_of": "2026-05-02", "source_url": "https://timesofindia.indiatimes.com/technology/tech-news/tech-
layoffs-92000-april-2026"}, {"metric": "Microsoft job cuts in 2025", "value": 6300.0, "unit": "jobs", "as_of": "2025-10-10", "source_url": "https://www.capacityglobal.com/microsoft-job-cuts-
reach-6300-in-2025"}], "created_at": "2026-05-09T05:29:50.191402Z", "updated_at": "2026-05-09T05:29:50.191402Z", "stale_after": "2026-05-09T11:29:50.191402Z", "state": "fresh", "revision_history": [],
"session_id": "d0e4ab1b-2828-44a7-9d15-cf436d74291d", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 3, "failed_count": 0}
```

## 💬 Response

I have extensive research data. Let me note a critical finding from the second research result — Amazon apparently had an additional 16,000 layoff round on April 21. Let me verify this and check for any very recent announcements in the May 1-16 window.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Amazon layoffs April 21 2026 16000"
}
```

### 📋 Result

```
{"query": "Amazon layoffs April 21 2026 16000", "results": [{"title": "Tech layoffs 2026: More than 128,000 people have been laid off this year from companies like PayPal, Meta, Cloudflare and more",
"url": "https://tech.yahoo.com/general/article/tech-layoffs-2026-more-than-128000-people-have-been-laid-off-this-year-from-companies-like-paypal-meta-cloudflare-and-more-144545060.html", "snippet":
"Tech layoffs in May are continuing to rise, as companies like [Cloudflare](https://tech.yahoo.com/ai/article/cloudflare-cuts-more-than-1100-employees-as-ai-induced-tech-layoffs-
continue-145517548.html), PayPal and Coinbase have announced they\u2019re cutting thousands of jobs. So far this year, there have been over 128,000 layoffs in tech, [according to data from
Trueup](https://www.trueup.io/layoffs). The layoffs seem to be moving at a faster rate than last year \u2014 over 245,000 workers in tech were l", "api_data": null, "hint": null}, {"title": "Layoffs
down in 2026 \u2014 except in one field | KRON4", "url": "https://www.kron4.com/news/technology-ai/layoffs-down-in-2026-except-in-one-field/", "snippet": null, "api_data": null, "hint": null},
{"title": "Met Gala 2026 sees protests against Jeff Bezos over Amazon layoffs - Storyboard18", "url": "https://www.storyboard18.com/trending/protesters-target-jeff-bezos-at-met-gala-over-amazon-
layoffs-ws-l-97284.htm", "snippet": "ADVERTISEMENT\nThe Met Gala 2026 witnessed protests outside the venue as demonstrators targeted Jeff Bezos, the lead sponsor of this year\u2019s event, over
concerns regarding workforce treatment at Amazon. Protesters reportedly left bottles containing urine at the venue as a form of demonstration, signalling anger over recent layoffs and corporate
policies.\nAccording to a report by Firstpost, protest groups displayed messages criticising both [Jeff Bezos ](https://storyboard18.com/brand-marketing/ves", "api_data": null, "hint": null},
{"title": "Amazon to Conduct Biggest Layoffs in Its History, Cutting 16,000 Corporate Roles | Salesforce Ben", "url": "https://www.salesforceben.com/amazon-to-conduct-biggest-layoffs-in-its-history-
cutting-16000-corporate-roles/", "snippet": "Amazon has [confirmed](https://www.aboutamazon.com/news/company-news/amazon-layoffs-corporate-jan-2026) that approximately 16,000 white-collar workers have
been laid off during their second round of job cuts. This has pushed the company closer to its reported target of cutting roughly 30,000 corporate roles worldwide \u2013 the largest job reduction in
its history.\nThe latest cuts impact teams across Amazon Web Services (AWS), retail, and HR, following the [14,000 white-collar roles](https://www.sale", "api_data": null, "hint": null}, {"title":
"Amazon layoffs: 16000 jobs to be cut in latest anti ...", "url": "https://www.cnbc.com/2026/01/28/amazon-layoffs-anti-bureaucracy-ai.html", "snippet": "![Amazon laying off about 16,000 corporate
workers in latest anti-bureaucracy
push](https://image.cnbcfm.com/api/v1/image/108258097-17696013751769601372-43727291574-1080pnbcnews.jpg?v=1769601374&w=750&h=422&vtcrop=y)\n[Amazon](https://www.cnbc.com/quotes/AMZN/) said Wednesday
it plans to eliminate about 16,000 corporate jobs, marking its second round of mass job cuts since last October.\nIn [a blog post](https://www.aboutamazon.com/news/company-news/amazon-layoffs-
corporate-jan-2026?utm_source=rss", "api_data": null, "hint": null}, {"title": "Update on our organization", "url": "https://www.aboutamazon.com/news/company-news/amazon-layoffs-corporate-jan-2026",
"snippet": "The message below was shared with Amazon employees earlier today.\nI want to let you know that we're making additional organizational changes across Amazon that will impact some of our
teammates. I recognize this is difficult news, which is why I\u2019m sharing what\u2019s happening and why.\nAs I shared in October, we've been working to strengthen our organization by reducing
layers, increasing ownership, and removing bureaucracy. While many teams finalized their organizational changes in October, other te", "api_data": null, "hint": null}, {"title": "After 16,000 layoffs,
Amazon may cut 14,000 more jobs in second phase", "url": "https://americanbazaaronline.com/2026/03/12/after-16000-layoffs-amazon-may-cut-14000-more-jobs-in-second-phase-476695/", "snippet": "According
to a post on[ X](https://x.com/TechLayoffLover/status/2031904439653597419?s=20), the sprawling corporate offices of Amazon are undergoing a silent, algorithmic transformation. While the company
recently confirmed 16,000 layoffs, internal reports and accounts from high-level leadership suggest this is merely the opening \u201cphase\u201d of a much deeper institutional purge.\nDocuments
circulating within the company\u2019s upper management point toward an additional 14,000 job cuts slated for the secon", "api_data": null, "hint": null}, {"title": "Amazon Layoffs 2026: AWS Cloud and
Engineering Hiring Impact - KORE1", "url": "https://www.kore1.com/amazon-layoffs-2026/", "snippet": "Amazon Layoffs 2026: What 16,000 Cuts Mean for AWS Cloud and Engineering Hiring\nAmazon has
eliminated more than 16,000 positions in 2026, making it the single largest contributor to the year\u2019s tech layoff wave, with cuts concentrated in AWS professional services, Alexa AI, Prime Video
and Studios, and Amazon Pharmacy. The displaced pool includes production-scale AWS engineers, data platform builders, and MLOps specialists the cloud hiring market has been trying to source for three
consecutive ye", "api_data": null, "hint": null}, {"title": "Amazon Layoffs Continue; 16000 More To Lose Jobs", "url": "https://www.indmoney.com/blog/us-stocks/amazon-layoffs-continue-16000-more-to-
lose-jobs", "snippet": "![Amazon Layoffs Continue; 16,000 More To Lose Jobs Amazon Layoffs Continue; 16,000 More To Lose Jobs](https://strapi-cdn.indmoney.com/cdn-
cgi/image/quality=80,format=auto,metadata=copyright,width=700/https://strapi-cdn.indmoney.com/xlarge_Amazon_layoffs_7777db080f.png)\n- Who Is Impacted by the Latest Amazon Layoffs?\n- What Employees
Are Feeling Amazon Layoffs\n- Why is Amazon Laying Off 30,000 People?\n- What Amazon Layoffs Mean for Investors\n- The Bigger Picture: Not Just an Amazon Story\nFor a l", "api_data": null, "hint":
null}, {"title": "Amazon announces 16000 layoffs as business booms", "url": "https://www.king5.com/article/news/local/amazon-announces-16000-layoffs-business-
booms/281-1a74f90c-3091-4e2b-bf03-e33caade2bea", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "Google Alphabet layoffs May 2026 involuntary"
}
```

### 📋 Result

```
{"query": "Google Alphabet layoffs May 2026 involuntary", "results": [{"title": "\u2018Big tech\u2019 Q1 results: Meta leads on growth as layoffs loom and AI begins to pay off for Google | Campaign
US", "url": "https://www.campaignlive.com/article/big-tech-q1-results-meta-leads-growth-layoffs-loom-ai-begins-pay-off-google/1957369", "snippet": "The first quarter of 2026 is in the books and the
latest round of earnings reports from some of adland\u2019s biggest platforms are available.\nAgainst the backdrop of ongoing AI innovation, perceived job vulnerability and increasing geopolitical
uncertainty, the figures behind the likes of Amazon, Alphabet, Meta, Apple and Microsoft offer insight into how Silicon Valley is attempting to find success in the present while planning for the
future.\nMeta continues to drive results despite challenging trad", "api_data": null, "hint": null}, {"title": "Alphabet Inc. (Google) Layoffs - TheLayoff.com", "url":
"https://www.thelayoff.com/google", "snippet": "Is it true that at Google employees over 50 are viewed as not being in touch with technology and thus, forced out or laid off? I\u2019ve heard this
affects women more.\n[UK layoffs will crack down on remote workers first](https://www.thelayoff.com/t/1kn5a40mq)\nAs the Alphabet soup continues to do mini layoffs to avoid UK government thresholds.
Looks like they will pick out people that work remotely, going as far to include peeps working 2 days a week from home.\n[PIPs Are Even Worse Now; Comp Discourag", "api_data": null, "hint": null},
{"title": "Google Layoffs 2026: The Engineering Hiring Window - KORE1", "url": "https://www.kore1.com/google-layoffs-2026/", "snippet": "Google Layoffs 2026: What the Rolling AI Restructuring Means
for Engineering Hiring\nGoogle has displaced an estimated 1,500\u20133,000+ engineers in 2026 through rolling performance cuts, Platform and Devices restructuring, and manager delayering, without ever
announcing a number. That invisibility is why most hiring pipelines are not positioned for this pool. The talent is real and in the market right now.\nLast updated: April 29, 2026\nEvery other major
layoff in this cycle had a headline. Oracle gav", "api_data": null, "hint": null}, {"title": "Layoffs Tracker - All Tech and Startup Layoffs", "url": "https://www.trueup.io/layoffs", "snippet": null,
"api_data": null, "hint": null}, {"title": "Google Layoffs Discussions - Blind", "url": "https://www.teamblind.com/company/Google/posts/google-layoffs", "snippet": "Join Google's internal discussion
for verified employees only!\nTech Industry\n7d\n27216\nI HATE being oncall as a software engineer - advice?\nPersonal Finance\n5d\n6261\nDo I REALLY need $5m to retire?\nTech Industry\n4d\n13495\nIs
Microsoft still a decent place to work for?\nTech Industry\n11h\n8324\nDid the JP morgan s** slave guy lie? Or was it actually true?? lmao\nLayoffs\nApr 29\n19680\nHOT TAKE: Firing is just as hard as
getting fired", "api_data": null, "hint": null}, {"title": "Google mass layoffs 2026 | Tech Industry", "url": "https://www.teamblind.com/post/google-mass-layoffs-2026-q6rzmlg3", "snippet": "No idea
how Google has held out so long. Expect a bloodbath in 2026.\nSoftware Engineering Career\nApr 27\n6407\nWhen will dev market improve for entry level?\nTech Industry\nYesterday\n14958\nGet out while
you have the chance\nTech Industry\n2d\n21990\nHow to survive big tech\nSF Bay Area\n3d\n7076\n37 - Cried after failing Apple interview.\nSoftware Engineering Career\n3d\n30466\nAnthropic has a type
and it's painfully visible\nWe did bro, they just didn't announce it\nThere's been rolling Org specific layoffs thro", "api_data": null, "hint": null}, {"title": "Google Employee Statistics 2026",
"url": "https://www.makerstations.io/google-employee-statistics/", "snippet": "Alphabet closed 2025 with 190,820 full-time employees worldwide \u2014 a 4.09% increase from the 183,323 it reported at
year-end 2024. This article covers Google\u2019s total headcount over time, layoff history, work-hour policies, workforce demographics, employee breakdown by business segment and geography, and how
its headcount compares to other large tech companies.\nGoogle Employee Statistics 2026\n- 190,820 \u2014 Alphabet\u2019s total full-time employees as of December 31, 2025, per SEC filings.\n- 12,000
\u2014 empl", "api_data": null, "hint": null}, {"title": "Tens of Thousands of Tech Workers Are Being Laid Off in 2026. The $725 Billion That Replaced Them Is Going to Four Companies. - 24/7 Wall
St.", "url": "https://247wallst.com/investing/2026/05/07/tens-of-thousands-of-tech-workers-are-being-laid-off-in-2026-the-725-billion-that-replaced-them-is-going-to-four-companies/", "snippet": "You
are being shown one number. Mark Zuckerberg told 8,000 Meta employees in early May that their jobs were a casualty of the company\u2019s AI infrastructure budget. Amazon has cut roughly 30,000 roles
in the last five months. Microsoft has shed about 125,000 through \u201cvoluntary\u201d departures. Alphabet is in the middle of an ongoing 1,500.\nThe headlines compress into a single phrase: AI is
taking jobs.\nThat phrase is not wrong. It is just the wrong number.\n$145 billion vs $27 billion: the math behind t", "api_data": null, "hint": null}, {"title": "Alphabet Workers Union-CWA", "url":
"https://www.alphabetworkersunion.org/campaigns/job-security", "snippet": "Campaign\nStatus Update (Sept 9, 2025): This year after our organizing, voluntary exit packages (VEPs) have been offered to
over 60,000 Googlers, giving individual Googlers more agency and significantly reducing layoffs. As Sundar said, leadership responded because thousands of Googlers like you spoke up. But we\u2019re
not done yet \u2013 we're still growing our movement so we can win stronger policies! We\u2019re also adding a new demand to our campaign in efforts to address concerns specific to visa holders ",
"api_data": null, "hint": null}, {"title": "Google Layoffs: Alphabet Reportedly Cuts Hundreds From Platform & Devices Unit, Retail Stuck In Neutral Mode", "url": "https://stocktwits.com/news-
articles/markets/equity/google-layoffs-alphabet-reportedly-cuts-hundreds-of-jobs/chfrQD9Rb9I", "snippet": "Advertisement|[Remove ads.](https://stocktwits.com/subscriptions)\nAlphabet, Inc. (GOOGL)
(GOOG) unit Google has reportedly cut jobs again, with the ax falling this time on the platforms and devices unit.\nGoogle's Platform business includes Android and Chrome, while the Devices unit
comprises the Pixel family of devices. Following a reorganization in April 2024, these were combined as a single division.\nAn Information report said Google laid off hundreds of employees from this
unit on Thursday, R", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Microsoft involuntary layoffs May 2026 forced cuts"
}
```

### 📋 Result

```
{"query": "Microsoft involuntary layoffs May 2026 forced cuts", "results": [{"title": "Microsoft Layoffs 2026: What Hiring Managers Need to Know - KORE1", "url": "https://www.kore1.com/microsoft-
layoffs-2026/", "snippet": "Microsoft Layoffs 2026: What the Rule of 70 Buyout Means for Hiring Managers\nMicrosoft announced on April 23, 2026, that it will offer voluntary retirement packages to
approximately 8,750 US employees (7% of its domestic workforce) under a \u201cRule of 70\u201d formula, the first program of its kind in the company\u2019s 51-year history, with notifications going
out May 7 and a 30-day decision window.\nLast updated: April 24, 2026\nNobody has written this for the person staring at an open Azure architect req wi", "api_data": null, "hint": null}, {"title":
"More than 90,000 tech workers have been laid off this year. But here\u2019s why companies like Microsoft are offering voluntary buyouts instead | Fortune", "url": "https://fortune.com/2026/04/26/why-
did-microsoft-do-buyouts-layoffs-tech-workers/", "snippet": "It\u2019s been a tough year for tech workers. Some [92,000 employees](https://layoffs.fyi/) have been laid off from tech companies as they
look to [cut overhead ](https://fortune.com/2026/04/15/data-centers-hyperscalers-spending-billions-on-hardware-thats-worthless-in-3-years/)costs and invest heavily in
AI.\n[Meta](https://fortune.com/company/facebook/) [announced](https://fortune.com/2026/04/24/meta-cuts-workers-ai-intel-earnings-grok-spacex-apple-ceo-age/) on Thursday that it plans to cut 10% of
wo", "api_data": null, "hint": null}, {"title": "Microsoft Layoffs Discussions - Blind", "url": "https://www.teamblind.com/company/Microsoft/posts/microsoft-layoffs", "snippet": "Join Microsoft's
internal discussion for verified employees only!\nTech Industry\n7d\n27216\nI HATE being oncall as a software engineer - advice?\nPersonal Finance\n5d\n6261\nDo I REALLY need $5m to retire?\nTech
Industry\n4d\n13495\nIs Microsoft still a decent place to work for?\nTech Industry\n11h\n8324\nDid the JP morgan s** slave guy lie? Or was it actually true?? lmao\nLayoffs\nApr 29\n19680\nHOT TAKE:
Firing is just as hard as getting fired", "api_data": null, "hint": null}, {"title": "Microsoft Voluntary Buyout Playbook 2026 \u2014... | Metaintro", "url": "https://www.metaintro.com/blog/microsoft-
voluntary-buyout-playbook-2026", "snippet": "Microsoft Voluntary Buyout Playbook 2026 \u2014 How 8750 Workers Can Cash Out Without a Layoff Notice\nMicrosoft's first-ever voluntary buyout targets 8750
US workers. Inside the severance math, healthcare extension, equity vesting, and how to negotiate.\n[April 29, 2026](https://www.metaintro.com/blog/archive/2026/04)\n![Microsoft Voluntary Buyout
Playbook 2026 \u2014 How 8750 Workers Can Cash Out Without a Layoff Notice](https://cdn.metaintro.com/rs:fill:1200:675/q:85/plain/images/kai.VpahhwFW.png)\nTL;DR S", "api_data": null, "hint": null},
{"title": "Microsoft plans first-ever voluntary employee buyout for up to 7% of U.S. workforce", "url": "https://www.cnbc.com/2026/04/23/microsoft-plans-first-voluntary-retirement-program-for-us-
employees.html", "snippet": "[Microsoft](https://www.cnbc.com/quotes/MSFT/) will offer voluntary buyouts to some U.S. employees, a first for the 51-year-old software giant, as the tech industry
grapples with major changes sparked by the artificial intelligence boom.\nAbout 7% of U.S. employees are eligible, according to a person familiar with the plans who asked not to be named because the
number isn't being made public. The one-time retirement program, announced in a memo on Thursday, will be available to U.S. workers at th", "api_data": null, "hint": null}, {"title": "Microsoft
Employee \"Voluntary\" Buyouts - Senior Technical Staff Being Dumped - YouTube", "url": "https://www.youtube.com/watch?v=tzjoXcmZHv4", "snippet": "Pr\u00e9sentation\nPresse\nDroits d'auteur\nNous
contacter\nCr\u00e9ateurs\nPublicit\u00e9\nD\u00e9veloppeurs\nR\u00e9silier vos abonnements\nConditions d'utilisation\nConfidentialit\u00e9\nR\u00e8gles et s\u00e9curit\u00e9\nPremiers pas sur
YouTube\nTester de nouvelles fonctionnalit\u00e9s\n\u00a9 2026 Google LLC", "api_data": null, "hint": null}, {"title": "Microsoft wants 8,750 workers gone \u2014 and its 'Rule of 70' reveals exactly
who's on the chopping block", "url": "https://finance.yahoo.com/sectors/technology/articles/microsoft-wants-8-750-workers-090500948.html", "snippet": "Microsoft wants 8,750 workers gone \u2014 and its
'Rule of 70' reveals exactly who's on the chopping block\nCole Tretheway\n6 min read\nSilicon Valley has a job-security problem. The tech sector has ramped-up voluntary layoffs since Google's
Platforms & Devices buyout in January 2025. For the first time, Microsoft appears poised to board the train of tech companies offering buyout packages to employees.\nThe company is offering about
8,750 people \u2014 7% of its workforce \u2014 a buyout package. Those eligible c", "api_data": null, "hint": null}, {"title": "20,000 job cuts at Meta, Microsoft raise concern that AI-driven labor
crisis is here", "url": "https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html", "snippet": "The more than 20,000 potential job cuts
[Meta](https://www.cnbc.com/quotes/META/) and [Microsoft](https://www.cnbc.com/quotes/MSFT/) revealed on Thursday, months after [Amazon](https://www.cnbc.com/quotes/AMZN/) announced its most
widespread layoffs ever, may only be the beginning.\nThe same companies that are collectively spending hundreds of billions of dollars a year to build out artificial intelligence infrastructure to
meet soaring demand for AI services are seeking efficiencies from AI by s", "api_data": null, "hint": null}, {"title": "Tens of Thousands of Tech Workers Are Being Laid Off in 2026. The $725 Billion
That Replaced Them Is Going to Four Companies. - 24/7 Wall St.", "url": "https://247wallst.com/investing/2026/05/07/tens-of-thousands-of-tech-workers-are-being-laid-off-in-2026-the-725-billion-that-
replaced-them-is-going-to-four-companies/", "snippet": "You are being shown one number. Mark Zuckerberg told 8,000 Meta employees in early May that their jobs were a casualty of the company\u2019s AI
infrastructure budget. Amazon has cut roughly 30,000 roles in the last five months. Microsoft has shed about 125,000 through \u201cvoluntary\u201d departures. Alphabet is in the middle of an ongoing
1,500.\nThe headlines compress into a single phrase: AI is taking jobs.\nThat phrase is not wrong. It is just the wrong number.\n$145 billion vs $27 billion: the math behind t", "api_data": null,
"hint": null}, {"title": "Microsoft Layoffs 2026: Targeting Non-Core Roles", "url": "https://www.linkedin.com/posts/teamblind_is-microsoft-preparing-for-mass-layoffs-in-
activity-7414718818150932480-cDY0", "snippet": "As we enter the first quarter of the year, Microsoft [#layoffs](https://www.linkedin.com/signup/cold-
join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Flayoffs&trk=public_post-text) in 2026 are fast-becoming a focal point of industry concern.\nBased on Blind threads and past
precedents, Microsoft layoffs are likely to target non-core or overlapping roles rather than frontline [#AI](https://www.linkedin.com/signup/cold-
join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffee", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"Amazon layoffs\" \"April 2026\" OR \"May 2026\" second round"
}
```

### 📋 Result

```
{"query": "\"Amazon layoffs\" \"April 2026\" OR \"May 2026\" second round", "results": [{"title": "Tech layoffs 2026: More than 128,000 people have been laid off this year from companies like PayPal,
Meta, Cloudflare and more", "url": "https://tech.yahoo.com/general/article/tech-layoffs-2026-more-than-128000-people-have-been-laid-off-this-year-from-companies-like-paypal-meta-cloudflare-and-
more-144545060.html", "snippet": "Tech layoffs in May are continuing to rise, as companies like [Cloudflare](https://tech.yahoo.com/ai/article/cloudflare-cuts-more-than-1100-employees-as-ai-induced-
tech-layoffs-continue-145517548.html), PayPal and Coinbase have announced they\u2019re cutting thousands of jobs. So far this year, there have been over 128,000 layoffs in tech, [according to data
from Trueup](https://www.trueup.io/layoffs). The layoffs seem to be moving at a faster rate than last year \u2014 over 245,000 workers in tech were l", "api_data": null, "hint": null}, {"title":
"Layoffs down in 2026 \u2014 except in one field | KRON4", "url": "https://www.kron4.com/news/technology-ai/layoffs-down-in-2026-except-in-one-field/", "snippet": null, "api_data": null, "hint":
null}, {"title": "Met Gala 2026 sees protests against Jeff Bezos over Amazon layoffs - Storyboard18", "url": "https://www.storyboard18.com/trending/protesters-target-jeff-bezos-at-met-gala-over-
amazon-layoffs-ws-l-97284.htm", "snippet": "ADVERTISEMENT\nThe Met Gala 2026 witnessed protests outside the venue as demonstrators targeted Jeff Bezos, the lead sponsor of this year\u2019s event, over
concerns regarding workforce treatment at Amazon. Protesters reportedly left bottles containing urine at the venue as a form of demonstration, signalling anger over recent layoffs and corporate
policies.\nAccording to a report by Firstpost, protest groups displayed messages criticising both [Jeff Bezos ](https://storyboard18.com/brand-marketing/ves", "api_data": null, "hint": null},
{"title": "Amazon To Layoff 14,000 Employees In May? Find Out What Tech Giant Has To Say | Republic World", "url": "https://www.republicworld.com/tech/amazon-may-2026-layoffs-second-round-may-
cut-14000-jobs-after-16000-already-axed-total-could-hit-30000", "snippet": "Amazon To Layoff 14,000 Employees In May? Find Out What Tech Giant Has To Say\nAmazon had axed 16,000 employees in January
this year. This is what Amazon has to say about the rumoured May layoffs.\n![Amazon To Layoff 14,000 Employees In May? Find Out What Tech Giant Has To Say Amazon To Layoff 14,000 Employees In May?
Find Out What Company Has To Say](https://img.republicworld.com/all_images/2026/04/amazon-may-2026-layoffs-second-round-may-cut-14000-jobs-after-16000-already-axed-total-could-hit-30", "api_data":
null, "hint": null}, {"title": "After 16,000 layoffs, Amazon may cut 14,000 more jobs in second phase", "url": "https://americanbazaaronline.com/2026/03/12/after-16000-layoffs-amazon-may-
cut-14000-more-jobs-in-second-phase-476695/", "snippet": "According to a post on[ X](https://x.com/TechLayoffLover/status/2031904439653597419?s=20), the sprawling corporate offices of Amazon are
undergoing a silent, algorithmic transformation. While the company recently confirmed 16,000 layoffs, internal reports and accounts from high-level leadership suggest this is merely the opening
\u201cphase\u201d of a much deeper institutional purge.\nDocuments circulating within the company\u2019s upper management point toward an additional 14,000 job cuts slated for the secon", "api_data":
null, "hint": null}, {"title": "A wave of layoffs at some of the country\u2019s largest companies has intensified in 2026. Read more: https://www.newsweek.com/amazon-lose-warehouse-mass-layoffs-
homestead-florida-11853404", "url": "https://www.threads.com/@newsweek/post/DXZB0GBDpps/a-wave-of-layoffs-at-some-of-the-countrys-largest-companies-has-intensified-in", "snippet": "###
Result\n\"\\n\\n\\n\\n\\n\\n\\n\\nA wave of layoffs at some of the country\u2019s largest companies has intensified in 2026.\\n\\nRead more: https://www.newsweek.com/amazon-lose-warehouse-mass-
layoffs-homestead-florida-11853404\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n \\n\\n \\n\nThe Virginia
Supreme Court overthrew the will of voters on a minor technical argument, proving once again that judges are now just partisan politicians.\nPG went from amazing to garbage ", "api_data": null,
"hint": null}, {"title": "Amazon to cut 14,000 jobs globally, China operations may face deep impact \u00b7 TechNode", "url": "https://technode.com/2026/04/08/amazon-to-cut-14000-jobs-globally-china-
operations-may-face-deep-impact/", "snippet": "Amazon plans to launch a new round of global layoffs in May 2026, with about 14,000 employees expected to be affected. The cuts will span several core
business units, including AWS cloud services, retail, and human resources, while some teams in China could face complete shutdowns. The most controversial aspect of the layoffs is that the selection
process is reportedly not based on objective criteria such as performance or projects, but instead involves managers making random picks, leaving affe", "api_data": null, "hint": null}, {"title":
"Amazon denies reports of 14,000 more layoffs in May", "url": "https://www.msn.com/en-us/news/other/amazon-denies-reports-of-14000-more-layoffs-in-may/gm-GMLD7D168D", "snippet": "Microsoft and our
third-party vendors use cookies to store and access information such as unique IDs and personal data/personal information to deliver, maintain, and improve our services and ads. If you agree, MSN and
Microsoft Bing will personalise the content and ads that you see. You can select 'I Accept' to consent to these uses or click on 'Manage preferences' to review your options and exercise your right to
object to Legitimate Interest where used. You can change your selection or withdra", "api_data": null, "hint": null}, {"title": "Amazon denies reports of 14,000 more layoffs, calls claims
\u2018false\u2019", "url": "https://americanbazaaronline.com/2026/04/08/amazon-denies-reports-of-14000-more-layoffs-calls-claims-false-478531/", "snippet": "Amazon has denied media reports claiming
around 14,000 more employees would be fired in May. This comes after a recent report that went viral claimed that after laying off 16,000 employees in January, the company is going for another round
of mass layoffs which will see 14,000 of its employees losing their jobs. It was first reported on the job forum Blind and then taken up by Lei Feng, a Chinese-language tech portal.\n\u201cThese
reports are false and not based in fact,\u201d Amazon said.\nThe post on Blin", "api_data": null, "hint": null}, {"title": "Amazon layoffs: 16,000 jobs to be cut in latest anti-bureaucracy push",
"url": "https://www.cnbc.com/2026/01/28/amazon-layoffs-anti-bureaucracy-ai.html", "snippet": "![Amazon laying off about 16,000 corporate workers in latest anti-bureaucracy
push](https://image.cnbcfm.com/api/v1/image/108258097-17696013751769601372-43727291574-1080pnbcnews.jpg?v=1769601374&w=750&h=422&vtcrop=y)\n[Amazon](https://www.cnbc.com/quotes/AMZN/) said Wednesday
it plans to eliminate about 16,000 corporate jobs, marking its second round of mass job cuts since last October.\nIn [a blog post](https://www.aboutamazon.com/news/company-news/amazon-layoffs-
corporate-jan-2026?utm_source=rss", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Apple Nvidia layoffs May 2026"
}
```

### 📋 Result

```
{"query": "Apple Nvidia layoffs May 2026", "results": [{"title": "Nvidia, Apple and Microsoft may be trading at best valuations in years", "url": "https://www.gurufocus.com/news/8846372/nvidia-apple-
and-microsoft-may-be-trading-at-best-valuations-in-years", "snippet": null, "api_data": null, "hint": null}, {"title": "Top Tech News Today, May 7, 2026 - Tech Startups", "url":
"https://techstartups.com/2026/05/07/top-tech-news-today-may-7-2026/", "snippet": "![](https://techstartups.com/wp-content/uploads/2024/07/Google.jpg)\nAI\u2019s compute wars just hit escape velocity
\u2014 with SpaceX powering Anthropic\u2019s next models, Nvidia pouring billions into optical fiber, and floating data centers testing the ocean itself. It\u2019s Thursday, May 7, 2026, and here are
the top tech stories making waves today \u2014 from frontier AI infrastructure and quantum breakthroughs to Big Tech retreats, cybersecurity shocks, and the global race for energy and
talent.\nSomething bigger ", "api_data": null, "hint": null}, {"title": "Coinbase CEO Warns American Workers: Mass Layoffs Are Coming to 'Every Company' - 24/7 Wall St.", "url":
"https://247wallst.com/investing/2026/05/06/coinbase-ceo-warns-american-workers-mass-layoffs-are-coming-to-every-company/", "snippet": "The stock market spent much of the past two years celebrating
artificial intelligence as the next great productivity boom. Companies from Nvidia ([NASDAQ:NVDA](https://247wallst.com/companies/nvda/) | [NVDA Price
Prediction](https://247wallst.com/companies/nvda/price-prediction)) to Microsoft ([NASDAQ:MSFT](https://247wallst.com/companies/msft/)) raced higher as investors poured money into anything tied to AI
infrastructure. But there\u2019s another side to that story beginning to emerge. What happen", "api_data": null, "hint": null}, {"title": "Layoffs Accelerate in May 2026 as Firms Restructure Around
AI", "url": "https://finance.yahoo.com/sectors/technology/articles/layoffs-accelerate-may-2026-firms-040430218.html", "snippet": "More layoffs swept across industries in early May 2026 as a fresh wave
of firms announced job cuts.\nMany of the cuts share a common driver. Companies are rebuilding around artificial intelligence (AI).\nCloudflare Announces Layoffs in May 2026\nCloudflare announced
Thursday it would cut more than 1,100 jobs globally, about 20% of its 5,156-person workforce, as reported at the end of 2025. The firm revealed that internal AI usage increased by more than 600% in
three months.\n\"We have to be intention", "api_data": null, "hint": null}, {"title": "Big Tech is slashing jobs. Why Apple Is the exception - Newsweek", "url": "https://www.newsweek.com/big-tech-is-
slashing-jobs-why-apple-is-the-exception-11914945", "snippet": "Even as its peers slash roles and redirect funds to other aspects of their business, Apple has largely sidestepped the wave of layoff
announcements sweeping the rest of the tech sector and troubling America\u2019s white-collar workers.\nOver the past few years, tech has become especially vulnerable to mass layoff, leading in
private-sector job cuts in 2025, according to the outplacement firm Challenger, Gray & Christmas, and accounting for 154,445 of the 1.2 million announcements made last year. And 2", "api_data": null,
"hint": null}, {"title": "Apple and Nvidia are the only ones that have not done ...", "url": "https://www.teamblind.com/post/apple-and-nvidia-are-the-only-ones-that-have-not-done-layoffs-so-far-
jdnx2k1c", "snippet": "Bravo!\nApple had multiple layoffs. Everything at Apple is org based and not company wide including hiring and layoffs. They have also reduced new hire headcounts and not
filling backfills.\nThey have been running on super scrappy mode for a while, even senior devs get old macbooks to work on lol\nThe layoffs were relatively very minimal and it was because they closed
a dept, not some bs ai reason. They also gave them a few months to try and transfer internally. Im not a fan of working here but cre", "api_data": null, "hint": null}, {"title": "Layoffs Tracker - All
Tech and Startup Layoffs", "url": "https://www.trueup.io/layoffs", "snippet": null, "api_data": null, "hint": null}, {"title": "Nvidia Layoffs Discussions - Blind", "url":
"https://www.teamblind.com/company/NVIDIA/posts/nvidia-layoffs", "snippet": "Join NVIDIA's internal discussion for verified employees only!\nTech Industry\n7d\n27216\nI HATE being oncall as a software
engineer - advice?\nPersonal Finance\n5d\n6261\nDo I REALLY need $5m to retire?\nTech Industry\n4d\n13495\nIs Microsoft still a decent place to work for?\nTech Industry\n11h\n8324\nDid the JP morgan
s** slave guy lie? Or was it actually true?? lmao\nLayoffs\nApr 29\n19680\nHOT TAKE: Firing is just as hard as getting fired", "api_data": null, "hint": null}, {"title": "What to Expect From Apple
Layoffs in 2026: The Company That Rarely Cuts Staff Faces a Changing Industry - AppleMagazine", "url": "https://applemagazine.com/apple-layoffs-2026-expectations-analysis/", "snippet": "What to Expect
From Apple Layoffs in 2026: The Company That Rarely Cuts Staff Faces a Changing IndustryAs layoffs sweep through the tech sector, Apple remains one of the few major players to resist large-scale cuts.
But with automation, AI integration, and global economic pressure reshaping the workforce, 2026 may test the company\u2019s resilience.\nThe technology industry has entered another period of
contraction. From San Francisco to Seattle, once-untouchable giants are shedding thousands of worke", "api_data": null, "hint": null}, {"title": "Apple is prepared to sever ties with Nvidia", "url":
"https://appleinsider.com/articles/24/12/24/apples-bad-blood-with-nvidia-continues-after-decades-of-fighting", "snippet": "Apple is ramping up research and development of its own AI chip to reduce its
reliance on third-party developers, potentially finally completely ending its decades-long unhappy relationship with Nvidia.\nIn November 2020, Apple announced the
[M1](https://appleinsider.com/inside/m1) chip, its first foray into in-house designed processors for its [Mac](https://appleinsider.com/inside/mac) lineup. The move effectively severed ties between
Apple and Intel, the latter responsible for previous processo", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.republicworld.com/tech/amazon-may-2026-layoffs-second-round-may-cut-14000-jobs-after-16000-already-axed-total-could-hit-30000",
  "prompt": "What does Amazon say about the rumored May 2026 layoffs of 14,000? Has Amazon confirmed or denied a second round of layoffs in May 2026?"
}
```

### 📋 Result

```
{"url": "https://www.republicworld.com/tech/amazon-may-2026-layoffs-second-round-may-cut-14000-jobs-after-16000-already-axed-total-could-hit-30000", "content": "Amazon has **denied** the rumored May
2026 layoffs of 14,000 employees. \n\nA spokesperson for the company stated: **\"These reports are false and not based on fact.\"**\n\nAmazon has not confirmed a second round of layoffs in May 2026
and explicitly dismissed the claims as untrue.\n\n---\n\n**Relevant links:**\nNo additional links are provided in the text content beyond the article itself.", "title": "Amazon To Layoff 14,000
Employees In May? Find Out What Tech Giant Has To Say"}
```

```json
{
  "query": "site:layoffs.fyi Amazon Google Microsoft Apple Nvidia May 2026"
}
```

### 📋 Result

```
{"query": "site:layoffs.fyi Amazon Google Microsoft Apple Nvidia May 2026", "results": [{"title": "Layoffs.fyi - Tech and Startup Layoff Tracker", "url": "https://layoffs.fyi/", "snippet": "101,550
tech employees laid off \u2219 120 tech companies w/ layoffs\n124,281 tech employees laid off \u2219 272 tech companies w/ layoffs\n152,922 tech employees laid off \u2219 551 tech companies w/
layoffs\n264,320 tech employees laid off \u2219 1,193 tech companies w/ layoffs\n165,269 tech employees laid off \u2219 1,064 tech companies w/ layoffs\n\u2219\n[apr field=\u201d# Companies Excluding
Public\u201d] tech companies w/ layoffs \u2219 [apr field=\u201d# Employees Excluding Public\u201d] tech employees laid off \u2219 Since 3/11/20\n[LIVE] [I\u2019m a startu", "api_data": null, "hint":
null}, {"title": "Tech Startup Layoffs - Layoffs.fyi Blog", "url": "https://layoffs.fyi/blog/page/5/", "snippet": "Below is a recap of the layoffs from this past week. Check out the [Layoffs.fyi
Tracker](https://layoffs.fyi/tracker/) for a complete list of all tech layoffs during the coronavirus pandemic.\n\ud83c\udfe2 Katerra \u2219 \ud83c\udf0e SF Bay Area \u2219 \ud83d\udc69 400 employees
(7%) \u2219 \ud83d\udd17[Source](https://www.theinformation.com/articles/softbank-backed-katerra-lays-off-more-than-400-employees)\n- A tech-driven construction company, Katerra cut 400 employees
following a CEO change. The SoftBank-backed company previously laid off 240 employees", "api_data": null, "hint": null}, {"title": "Layoff list - Page 3 of 12 - Layoffs.fyi", "url":
"https://layoffs.fyi/category/layoff-list/page/3/", "snippet": "\ud83c\udf0e London \u2219 \ud83d\udc69 Hundreds of employees \u2219 \ud83d\udda5 Multiple departments\nA London-based digital bank,
Monzo [laid off 120 of its U.K. employees](https://techcrunch.com/2020/06/03/monzo-lay-offs/) in June and [165 of its Las Vegas employees](https://techcrunch.com/2020/04/09/monzo-to-shutter-las-
vegas/) in April. The company also previously furloughed 295 U.K. employees.\nTo help its laid-off employees find new roles, Monzo created a talent directory (see link \ud83d\udc47) . It\u2019s not
clear whether the directory is meant", "api_data": null, "hint": null}, {"title": "San Francisco Startup Layoffs - Layoffs.fyi", "url": "https://layoffs.fyi/tag/san-francisco/", "snippet":
"\ud83c\udf0e Multiple locations \u2219 \ud83d\udc69 960 employees (6%) \u2219 \ud83d\udda5 Multiple departments\nLinkedIn, the professional networking site, laid off 960 employees (6%) across its
Global Sales and Talent Acquisition teams in late July. Today the company launched an opt-in talent directory featuring hundreds of its recently-departed alumni (see link \ud83d\udc47).\nThe directory
includes people with experience in customer success, recruitment, and sales management in North and South America, Europe, and the Asia-Pacific regions, accord", "api_data": null, "hint": null},
{"title": "Layoffs.fyi, Author at Layoffs.fyi - Page 5 of 16", "url": "https://layoffs.fyi/author/webmasterlayoffs-fyi/page/5/", "snippet": "Below is a recap of the layoffs from this past week. Check
out the [Layoffs.fyi Tracker](https://layoffs.fyi/tracker/) for a complete list of all tech layoffs during the coronavirus pandemic.\n\ud83c\udfe2 Katerra \u2219 \ud83c\udf0e SF Bay Area \u2219
\ud83d\udc69 400 employees (7%) \u2219 \ud83d\udd17[Source](https://www.theinformation.com/articles/softbank-backed-katerra-lays-off-more-than-400-employees)\n- A tech-driven construction company,
Katerra cut 400 employees following a CEO change. The SoftBank-backed company previously laid off 240 employees", "api_data": null, "hint": null}, {"title": "Support Startup Layoffs - Layoffs.fyi",
"url": "https://layoffs.fyi/tag/support/", "snippet": "The number of newly-reported startup layoffs [continues to decline](https://layoffs.fyi/2020/05/18/startup-layoffs-slowing-down-but-more-
employees-laid-off-on-average/), though each one is now affecting 3x more employees on average. This past week saw a [massive layoff from Uber](https://layoffs.fyi/2020/05/18/uber-lays-off-3000-more-
employees-on-top-of-the-3700-laid-off-earlier-this-month/), alongside other notable cuts mentioned below. The total count is now up to 58,000+ startup employees lai", "api_data": null, "hint": null},
{"title": "Analysis - Layoffs.fyi", "url": "https://layoffs.fyi/category/analysis/", "snippet": "It\u2019s been a roller coaster year for tech \ud83c\udfa2. In the month of April alone, 269 startups
laid off 26,651 employees, unsure if they\u2019d ever be able to raise money again.\nNow? Fundraising and IPO markets are at their frothiest levels since the dot-com era. We end the year with just 4
recorded layoffs in December.\nEven startups that cut employees earlier in the year have rebounded. Here are our Top 10 layoff comeback stories of 2020 \u2013 or, view the [Layoffs.fyi
Tracker](https://layoffs.fyi/tracker/) to ", "api_data": null, "hint": null}, {"title": "Marketing Startup Layoffs - Layoffs.fyi", "url": "https://layoffs.fyi/tag/marketing/", "snippet": "Below is a
recap of the layoffs from this past week. Check out the [Layoffs.fyi Tracker](https://layoffs.fyi/tracker/) for a complete list of all tech layoffs during the pandemic.\nIn case you missed it \u2014
we recently looked at usage data from the [Layoffs.fyi List](https://list.layoffs.fyi/) to see what types of laid-off employees were getting the most attention from recruiters. Among the findings:
there are 4x as many searches for laid-off engineers as there are for the next most popular functio", "api_data": null, "hint": null}, {"title": "Uber Startup Layoffs - Layoffs.fyi", "url":
"https://layoffs.fyi/tag/uber/", "snippet": "The cumulative damage of startup layoffs has been severe: [500 tech companies](https://layoffs.fyi/tracker/) have now laid off 64,000+ employees during the
pandemic. I wanted to find out \u2014 what have these companies been doing to mitigate the impact on laid-off employees?\n![](https://layoffs.fyi/wp-content/uploads/2020/06/Layoffs.fyi-Severance-
Tracker-1024x538.png)\n![](https://layoffs.fyi/wp-content/uploads/2020/06/Layoffs.fyi-Severance-Tracker-1024x538.png)\nI\u2019m excited to announce the new [Layof", "api_data": null, "hint": null},
{"title": "Greenhouse Startup Layoffs - Layoffs.fyi", "url": "https://layoffs.fyi/tag/greenhouse/", "snippet": "The cumulative damage of startup layoffs has been severe: [500 tech
companies](https://layoffs.fyi/tracker/) have now laid off 64,000+ employees during the pandemic. I wanted to find out \u2014 what have these companies been doing to mitigate the impact on laid-off
employees?\n![](https://layoffs.fyi/wp-content/uploads/2020/06/Layoffs.fyi-Severance-Tracker-1024x538.png)\n![](https://layoffs.fyi/wp-content/uploads/2020/06/Layoffs.fyi-Severance-
Tracker-1024x538.png)\nI\u2019m excited to announce the new [Layof", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me now synthesize all the research I've gathered and analyze this question carefully.

## Step 1: Parse the Resolution Criteria

**What must happen for YES?**
- Between May 1-16, 2026 (inclusive, end of day May 16 UTC)
- One of: Alphabet/Google, Microsoft, Apple, Amazon, or Nvidia
- Publicly announces a single involuntary workforce reduction
- Affecting 5,000+ employees
- Must be a single announced round (not cumulative YTD)
- Primary verification: Layoffs.fyi tracker

**Key exclusions:**
- Voluntary buyouts/retirement DON'T count (Microsoft's Rule of 70 explicitly excluded)


- The announcement date itself must fall in the window, not the effective date
- Re-reporting of earlier layoffs doesn't qualify
- I'm using the lower bound of any reported ranges to determine if the threshold is met

**Current snapshot:** As of May 9, 2026, none of the five companies have announced an involuntary reduction of 5,000+ employees during this window. The question closes May 9 at 06:48:31 UTC but resolves May 17.

## Step 2: Company-by-Company Assessment

### Amazon
- January 2026 saw 16,000 cuts
- May rumors of 14,000 additional layoffs were publicly denied by Amazon
- Given the scale of recent cuts and the explicit denial, another announcement seems unlikely in this timeframe
- Public pressure from protests adds to the unlikelihood

### Microsoft
- The voluntary retirement program explicitly doesn't count as involuntary layoffs
- No involuntary mass reductions reported in 2026
- They've positioned the voluntary approach as a deliberate alternative to forced cuts

### Alphabet/Google
- Ongoing pattern of smaller rolling reductions between 1,500-3,000 throughout the year
- No single announcement reaching 5,000+
- February's voluntary exit packages further suggest they're avoiding large involuntary announcements

### Apple
- Zero layoffs reported in 2026
- Stands out as the outlier among major tech firms
- Maintains a historically cautious approach to workforce reductions

### Nvidia
- No layoffs announced
- CEO remains bullish on growth prospects tied to AI expansion

Now I'm looking at the timeline constraints. We're essentially at the close of the forecasting window on May 9, with only about a week remaining until the May 16 resolution deadline. The critical question is whether any of these five companies would announce 5,000+ involuntary layoffs in that narrow window. Given that none have done so yet and the patterns I'm seeing across each company, the baseline expectation is that this doesn't happen.

Amazon seems like the most plausible candidate, but they've already denied plans for additional May cuts. Microsoft's reductions are voluntary, which doesn't meet the criteria. Google tends to execute layoffs in smaller rolling tranches rather than single large announcements. Apple and Nvidia are essentially off the table—Apple has a historical aversion to layoffs while Nvidia is riding the AI boom. The broader tech sector is certainly aggressive with headcount reductions, which introduces some tail risk of a surprise announcement, but the short remaining timeframe works against it.

Looking at the base rates, across these five companies in 2026 so far, there's been just one qualifying event—Amazon's 16,000-person cut in January. That translates to roughly a 12% probability per 16-day window if we extrapolate linearly. But that's too generous because Amazon has already made its move and explicitly denied further plans, the other companies lack any pattern of 5,000+ involuntary reductions, and we're already nine days into the window with nothing announced. Let me reconsider what the research actually showed.

I need to be more careful about Amazon's numbers. The sources conflict—some outlets reported a second round of 14,000 cuts planned for May, but Amazon denied those reports. The 24/7 Wall St article mentioned 30,000 total cuts across five months, but when I trace back to primary sources, only the January 16,000 is solidly confirmed. The April reports of additional layoffs came from outlets like TechNode and were contradicted by Amazon's own statements.

For the Microsoft angle, their voluntary severance program just launched on May 7, and there's nothing suggesting they'd convert it to mandatory layoffs within the next week. Given that Amazon has explicitly denied the second round and we're already into May with no announcement, the likelihood of new involuntary cuts in the next seven days seems low. Now I'm assigning individual probabilities to each company based on their recent behavior and statements, then combining them to get an overall likelihood. Amazon's denial makes a 5K+ announcement unlikely but not impossible at 3-5%, Microsoft's voluntary approach suggests minimal risk at 1-2%, Google's rolling cuts pattern points to maybe 2-3%, while Apple and Nvidia are essentially off the table at under 1% each.

Working through the math, that compounds to roughly 8.4%, but I'm second-guessing myself—we're already halfway through the window with no real signals, Amazon explicitly denied it, and something this big would almost certainly leak beforehand. I'm settling on around 7% as my estimate.

Though I should double-check the May 7 Wall Street article that mentioned Amazon cutting 30,000 roles over five months—that phrasing suggests there might have been a second wave of cuts that wasn't announced as a single event, which could affect how I'm interpreting the resolution criteria.

Looking at the data more carefully, the 30,000 figure appears to be combining January's 16,000 with the October 2025 round of 14,000, not a new April announcement. With nine days left in the window and no qualifying event yet, plus explicit denials from all five companies and no signs of imminent large-scale cuts, I'm landing on a final estimate around 5-7%.

## 💬 Response

Now I have a comprehensive picture. Let me synthesize my analysis and run through the reflection process.

**Key findings:**
1. **No qualifying event has occurred yet** in the May 1-9 window (9 of 16 days elapsed)
2. **Amazon** denied rumors of additional 14,000 layoffs in May (their 16,000 were in January)
3. **Microsoft's** voluntary retirement program is explicitly excluded by the fine print
4. **Google/Alphabet** is doing rolling "quiet cuts" of ~1,500-3,000 total in 2026 — not single 5,000+ rounds
5. **Apple** is described as "the exception" — no layoffs in 2026
6. **Nvidia** is in growth mode — CEO says "AI creates jobs"
7. Only 7 days remain in the window

## 💬 Response

The reflection shows my factors sum to a more extreme position (~1.4%) than my tentative estimate (7%). The gap is because my factors are all strongly negative but I'm maintaining some tail risk. Let me note that the factor-implied probability of ~1.4% seems too extreme — there's genuine residual uncertainty about Amazon and the remaining 7 days. My 7% accounts for that, but the reflection is telling me I might be slightly too generous. Let me settle around 5-7%.
