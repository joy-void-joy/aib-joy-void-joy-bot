# Reasoning Log: How many executions will be carried out in the United States between June 25 and June 28, 2026 (inclusive)?

*Generated: 2026-06-17T09:20:54.973845+00:00*


## 💭 Thinking

Let me analyze this forecasting question about US executions between June 25-28, 2026.

Key facts from the question:
1. The window is June 25-28, 2026 (4 days, inclusive)
2. Only one execution is currently scheduled: Dusty Ray Spencer in Florida, June 25, 2026
3. The discrete range is -0.5 to 4.5, with open upper bound
4. Resolution based on DPIC records

This is a discrete question with possible values 0, 1, 2, 3, 4, or more.
Now I'm thinking through the probability breakdown. Spencer's execution in Florida is the only confirmed case, but last-minute stays are common. The main scenarios are whether Spencer's execution proceeds and whether any other executions happen in that narrow window—which seems unlikely given nothing else is currently scheduled. I need to look into the current status and historical patterns for execution stays.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    44093
  ]
}
```

### 📋 Result

```
{"post_id": 44093, "title": "How many executions will be carried out in the United States between June 25 and June 28, 2026 (inclusive)?", "type": "discrete", "url":
"https://www.metaculus.com/questions/44093", "background_info": "Capital punishment in the United States is administered by individual states (and the federal government). As of mid-June 2026, roughly
15 executions have been carried out in the US in 2026. Execution dates are set by state death warrants but are frequently stayed, postponed, or reprieved by courts or governors on short notice.\n\nIn
June 2026: Andrew Richard Lukehart was executed in Florida on June 2; Jeffrey James Lee's June 11 Alabama execution was stayed after the US Supreme Court blocked the state's nitrogen hypoxia protocol;
Gerald Robert Hand's Ohio date was reprieved (Ohio's governor has indicated no executions will proceed without a new method). For the four-day window of June 25\u201328, 2026, the only execution
currently scheduled is that of Dusty Ray Spencer in Florida, set for June 25, 2026 at 6:00 p.m. Eastern Time at Florida State Prison by lethal injection. The next confirmed executions after that are
in July (Florida July 14, Ohio mid-July) and beyond.\n\nThe Death Penalty Information Center (DPIC) maintains an \"Upcoming Executions\" tracker and a year-by-year list of executions carried out,
which is the standard reference for US execution counts.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`",
"resolution_criteria": "This question asks how many executions of condemned prisoners are carried out (i.e., the prisoner is put to death) in the United States \u2014 by any state or the federal
government \u2014 on the calendar dates June 25, 26, 27, or 28, 2026 (US local time of the executing jurisdiction). An execution counts only if it is actually carried out during the window; a
scheduled execution that is stayed, postponed, reprieved, commuted, or otherwise not completed does not count. Report the integer count; for example, if exactly one execution is carried out, the value
is 1. Resolution will be based on the Death Penalty Information Center's records of 2026 executions (https://deathpenaltyinfo.org/executions/upcoming-executions and its 2026 execution list). If DPIC's
records are unavailable or unclear, official state Department of Corrections statements or [credible sources](https://www.metaculus.com/faq/#definitions) will be used.", "fine_print": "Only executions
of human prisoners under a death sentence count; this excludes deaths from other causes (e.g., natural death, suicide). The relevant date is the date on which the prisoner is pronounced dead, using
the local calendar date of the executing jurisdiction. Both lethal-injection and any other method (e.g., nitrogen hypoxia, electrocution) count equally. If an execution scheduled within the window
begins before midnight local time but is completed shortly after, it counts toward whichever date the prisoner is pronounced dead.", "num_forecasters": 1, "community_prediction": null, "lower_bound":
-0.5, "upper_bound": 4.5}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Dusty Ray Spencer Florida execution June 25 2026 status - any stays, appeals, or postponements?",
      "ttl": "6h"
    },
    {
      "query": "US executions scheduled June 25-28 2026 Death Penalty Information Center upcoming executions",
      "ttl": "6h"
    },
    {
      "query": "What is the historical rate of last-minute stays or postponements of Florida executions? How often do scheduled Florida executions actually proceed?",
      "ttl": "7d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Dusty Ray Spencer Florida execution June 25 2026 status - any stays, appeals, or postponements?", "entry": {"slug": "dusty-ray-spencer-florida-execution-
june-25-2026-s-8e7f5a83", "query": "Dusty Ray Spencer Florida execution June 25 2026 status - any stays, appeals, or postponements?", "answer": "The research agent was able to gather substantial
information. Here is my comprehensive synthesis:\n\n---\n\n## Dusty Ray Spencer \u2014 Florida Execution Status (June 25, 2026)\n\n### Execution Status: **Still Scheduled**\n- **Date:** June 25, 2026,
at 6:00 PM, Florida State Prison Complex\n- **Death Warrant:** Signed by Governor Ron DeSantis on **May 26, 2026**\n- **No stay has been granted** as of June 17, 2026\n- If carried out, Spencer (age
**74**) would be the **oldest person Florida has ever executed** and approximately the 8th\u20139th execution in Florida in 2026\n- He has been on death row for **over 34 years**\n\n### Active Legal
Challenges\n\n| Stage | Status | Details |\n|-------|--------|---------|\n| **Successive Postconviction Motion (Circuit Court)** | **Denied** (~June 10\u201311, 2026) | Filed in the 9th Judicial
Circuit Court |\n| **Florida Supreme Court Appeal** | **Open / Pending** | Docketed as **SC2026-0880** on June 9, 2026; classified as \"Mandatory Review \u2013 Death Penalty Appeal \u2013 3.851
Successor\" |\n| **Stay of Execution** | **Not yet granted** | No court has issued a stay as of mid-June 2026 |\n\n### Key Legal Arguments Raised\n- **Advanced age & medical conditions:** Spencer's
attorneys argue his age (74) and deteriorating health (including a \"failing liver\") combined with the lethal injection protocol could violate the **Eighth and Fourteenth Amendments** (cruel and
unusual punishment)\n- **Expired lethal drugs:** Challenge to the state's alleged use of **expired drugs** in its execution protocol\n- **Lethal injection protocol constitutionality** and **Florida's
execution secrecy laws**\n\n### Case Background\n- **Crime:** January 18, 1992 \u2014 First-degree murder of his wife, **Karen Spencer**, in Orange County, Florida. Karen was brutally beaten, stabbed,
and killed. Her teenage son **Timothy** witnessed the attack and attempted to intervene but was threatened with a knife.\n- **Conviction:** November 1992; sentenced to death\n- **Extensive appellate
history** spanning 30+ years, with cases reaching the **Florida Supreme Court** multiple times (1994, 1996, 2003, 2009, 2018) and the **U.S. Supreme Court** (certiorari denied in 2011 and 2019). His
cases have been cited hundreds of times in Florida death penalty jurisprudence.\n\n### Bottom Line\nThe execution remains on schedule for **June 25, 2026**. The only active pending matter is the
**Florida Supreme Court appeal (SC2026-0880)**, which is still **open**. With 8 days until the scheduled execution, the Florida Supreme Court has not yet ruled. No stay has been issued by any
court.\n\n---", "sources": [{"url": "https://deathpenaltyinfo.org/executions/upcoming-executions", "title": "Upcoming Executions - Death Penalty Information Center", "domain": "deathpenaltyinfo.org",
"accessed_at": "2026-06-17T00:00:00Z", "snippet": "June 25 - FL - Dusty Ray Spencer listed on upcoming executions page (last updated June 12, 2026)"}, {"url": "https://www.floridasupremecourt.org/",
"title": "Florida Supreme Court Docket - Case SC2026-0880", "domain": "floridasupremecourt.org", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "SC2026-0880, Mandatory Review - Death Penalty Appeal
- 3.851 Successor, docketed June 9, 2026, status: Open"}, {"url": "https://www.tampafreepress.com/", "title": "Tampa Free Press - Expired Drugs And A Failing Liver: 74-Year-Old Florida Inmate Fights
Looming Execution", "domain": "tampafreepress.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Reports on Spencer's legal challenges citing expired drugs and failing liver, approximately June
14, 2026"}, {"url": "https://www.tampafreepress.com/", "title": "Tampa Free Press - Florida Supreme Court Clears Way For June Execution", "domain": "tampafreepress.com", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "Florida Supreme Court rejected initial appeals after death warrant signed, reported May 27, 2026"}, {"url": "https://www.dc.state.fl.us/ci/execlist.html", "title":
"Florida Department of Corrections - Execution List", "domain": "dc.state.fl.us", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Florida DOC execution information"}], "key_facts": ["Dusty Ray
Spencer's execution is scheduled for June 25, 2026 at 6:00 PM at Florida State Prison Complex", "Death warrant signed by Governor Ron DeSantis on May 26, 2026", "No stay of execution has been granted
as of June 17, 2026", "Spencer's successive postconviction motion was denied by the 9th Judicial Circuit Court around June 10-11, 2026", "Appeal to the Florida Supreme Court (Case No. SC2026-0880) was
docketed June 9, 2026 and remains open/pending", "Spencer is 74 years old and would be the oldest person Florida has ever executed if carried out", "Spencer has been on death row for over 34 years,
convicted November 1992 for the January 18, 1992 murder of his wife Karen Spencer in Orange County", "Legal challenges cite his advanced age, failing liver, state's use of allegedly expired lethal
injection drugs, and constitutional violations (8th and 14th Amendments)", "Spencer would be approximately the 8th or 9th person executed by Florida in 2026", "His cases have reached the Florida
Supreme Court multiple times (1994, 1996, 2003, 2009, 2018) and U.S. Supreme Court (cert denied 2011, 2019)"], "data_points": [{"metric": "Spencer's age at scheduled execution", "value": 74.0, "unit":
"years", "as_of": "2026-06-25", "source_url": "https://www.tampafreepress.com/"}, {"metric": "Years on death row", "value": 34.0, "unit": "years", "as_of": "2026-06-17", "source_url":
"https://deathpenaltyinfo.org/executions/upcoming-executions"}, {"metric": "Florida executions in 2026 (Spencer would be approx.)", "value": 9.0, "unit": "execution number", "as_of": "2026-06-17",
"source_url": "https://deathpenaltyinfo.org/executions/upcoming-executions"}, {"metric": "Days until scheduled execution from today", "value": 8.0, "unit": "days", "as_of": "2026-06-17", "source_url":
"https://deathpenaltyinfo.org/executions/upcoming-executions"}, {"metric": "Death warrant signed date (days before execution)", "value": 30.0, "unit": "days before execution", "as_of": "2026-05-26",
"source_url": "https://www.tampafreepress.com/"}], "created_at": "2026-06-17T09:17:23.428574Z", "updated_at": "2026-06-17T09:17:23.428574Z", "stale_after": "2026-06-17T15:17:23.428574Z", "state":
"fresh", "revision_history": [], "session_id": "defb4fdb-28cd-4c7c-9d73-5c44a48620d2", "follow_up_count": 0}, "is_follow_up": false}, {"query": "US executions scheduled June 25-28 2026 Death Penalty
Information Center upcoming executions", "entry": {"slug": "us-executions-scheduled-june-25-28-2026-death-pena-0bd36421", "query": "US executions scheduled June 25-28 2026 Death Penalty Information
Center upcoming executions", "answer": "\n\nBased on my research attempts, all web access tools (WebSearch, WebFetch, ToolSearch) are unavailable in this session, preventing me from retrieving live
data from the Death Penalty Information Center or any other online source.\n\n## Research Report: US Executions Scheduled June 25\u201328, 2026\n\n### Data Availability\n\n**I was unable to retrieve
live data for this query.** All web search and fetch tools were blocked in this session, meaning I could not access:\n\n- The Death Penalty Information Center's upcoming executions page
(`deathpenaltyinfo.org/executions/upcoming-executions`)\n- Wikipedia's list of scheduled US executions\n- Any news sources covering late-June 2026 execution schedules\n\n### Background Context (from
training data, not live)\n\n- The Death Penalty Information Center (DPIC) maintains the most authoritative, regularly updated list of upcoming US executions at the federal and state level.\n-
Execution schedules are frequently subject to last-minute changes due to stays, appeals, clemency decisions, or procedural delays.\n- States that most frequently carry out executions include Texas,
Oklahoma, Alabama, Missouri, and Florida.\n- The federal government resumed executions in 2020 under the Trump administration; federal execution scheduling has varied with administration changes.\n-
Execution dates within a specific 4-day window (June 25\u201328) are highly specific and volatile \u2014 they are typically only confirmed weeks in advance and subject to change.\n\n### Recommended
Primary Sources\n\n1. **Death Penalty Information Center**: [https://deathpenaltyinfo.org/executions/upcoming-executions](https://deathpenaltyinfo.org/executions/upcoming-executions)\n2.
**Wikipedia**:
[https://en.wikipedia.org/wiki/List_of_people_scheduled_to_be_executed_in_the_United_States](https://en.wikipedia.org/wiki/List_of_people_scheduled_to_be_executed_in_the_United_States)\n3. **State
Departments of Corrections** (e.g., Texas TDCJ, Oklahoma DOC) for state-level confirmations.\n\n### Limitations\n\n- **No live data retrieved** \u2014 all findings below are null due to tool
unavailability.\n- Execution schedules are inherently volatile and can change on very short notice.\n- Any data older than a few days may already be outdated for this query.", "sources": [{"url":
"https://deathpenaltyinfo.org/executions/upcoming-executions", "title": "Upcoming Executions - Death Penalty Information Center", "domain": "deathpenaltyinfo.org", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "Unable to access \u2014 WebFetch tool was unavailable. This is the primary recommended source for upcoming US execution schedules."}, {"url":
"https://en.wikipedia.org/wiki/List_of_people_scheduled_to_be_executed_in_the_United_States", "title": "List of people scheduled to be executed in the United States - Wikipedia", "domain":
"en.wikipedia.org", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Unable to access \u2014 WebFetch tool was unavailable. Wikipedia maintains a community-edited list of scheduled US
executions."}], "key_facts": ["All web access tools (WebSearch, WebFetch, ToolSearch) were unavailable, preventing live data retrieval.", "The Death Penalty Information Center (DPIC) at
deathpenaltyinfo.org/executions/upcoming-executions is the primary authoritative source for upcoming US execution schedules.", "Execution schedules are highly volatile \u2014 subject to stays,
appeals, clemency, and procedural delays, often changing on short notice.", "States most frequently scheduling executions include Texas, Oklahoma, Alabama, Missouri, and Florida.", "No specific
execution names, dates, or states could be confirmed for June 25-28, 2026 due to inability to access live sources."], "data_points": [], "created_at": "2026-06-17T09:09:13.387923Z", "updated_at":
"2026-06-17T09:09:13.387923Z", "stale_after": "2026-06-17T15:09:13.387923Z", "state": "fresh", "revision_history": [], "session_id": "d7e9d3a0-424b-4c45-a842-e219f3d0eeec", "follow_up_count": 0},
"is_follow_up": false}, {"query": "What is the historical rate of last-minute stays or postponements of Florida executions? How often do scheduled Florida executions actually proceed?", "entry":
{"slug": "what-is-the-historical-rate-of-last-minute-stays-o-14c03302", "query": "What is the historical rate of last-minute stays or postponements of Florida executions? How often do scheduled
Florida executions actually proceed?", "answer": "The web search tools are not available in my current environment. Let me compile a thorough research report based on available knowledge, clearly
noting the provenance of each data point.\n\n---\n\n# Florida Execution Stays, Postponements, and Completion Rates\n\n## Executive Summary\n\nFlorida has been one of the most active death penalty
states since 1976, but its path from death sentence to execution is marked by extensive litigation, stays, and delays. The state has carried out approximately **105 executions** since 1976 (through
mid-2025), while having imposed roughly **1,000+ death sentences** in the same period. Stays and postponements of scheduled executions have been a recurring feature, particularly during periods of
legal upheaval (lethal injection protocol challenges, the *Hurst v. Florida* decision, etc.).\n\n---\n\n## 1. Total Executions Carried Out\n\n- **First post-reinstatement execution**: John Spenkelink,
May 25, 1979\n- **Total executions (1979\u2013~2025)**: Approximately **105\u2013110**\n- Florida ranks **4th or 5th nationally** in total executions behind Texas (~590), Oklahoma (~125), and Virginia
(~113)\n- Florida's death row population has historically been among the nation's largest, typically **300\u2013330 inmates**\n\n## 2. Death Warrant Signing vs. Execution Completion\n\nA critical
distinction in Florida is between **death warrants signed** by the Governor and **executions actually carried out**:\n\n- Under **Governor Bob Graham (1979\u20131987)**, a large number of death
warrants were signed \u2014 many more than resulted in actual executions. Estimates suggest Graham signed over **100 death warrants** during his tenure, while only approximately **16 executions** were
carried out. This implies a **stay/postponement rate of roughly 80\u201385%** for signed warrants during that era.\n- Under **Governor Bob Martinez (1987\u20131991)**, the pattern continued with
numerous warrants signed and many stayed.\n- In **more recent decades**, governors have become more selective about signing warrants, generally waiting until appeals are more fully exhausted. This has
improved the \"completion rate\" for signed warrants considerably \u2014 likely to **70\u201380%+ completion** in recent years.\n\n## 3. Sources and Mechanisms of Stays\n\nStays of Florida executions
have come from multiple sources:\n\n- **U.S. Supreme Court**: Emergency applications (often filed within 24\u201348 hours of scheduled execution)\n- **Eleventh Circuit Court of Appeals**: Federal
habeas corpus proceedings\n- **Florida Supreme Court**: State post-conviction proceedings under Rule 3.851\n- **Trial courts**: Competency-to-be-executed hearings under *Ford v. Wainwright*\n-
**Governor/Clemency Board**: Executive stays (rare but possible)\n\n### Common Grounds for Stays:\n1. **Competency to be executed** \u2014 Florida has had several landmark cases (*Ford v. Wainwright*,
John Ferguson, Thomas Provenzano)\n2. **Lethal injection protocol challenges** \u2014 Particularly 2006\u20132008 (after the Angel Diaz botched execution) and ongoing drug availability issues\n3.
**Newly discovered evidence or innocence claims** \u2014 Florida leads the nation with ~30 death row exonerations\n4. **Intellectual disability claims** \u2014 Under *Atkins v. Virginia* (2002) and
*Hall v. Florida* (2014, a Florida case)\n5. **Sentencing procedure challenges** \u2014 Especially after *Hurst v. Florida* (2016)\n\n## 4. Notable Stays and Postponements\n\n| Inmate | Year(s) |
Circumstances |\n|--------|---------|--------------|\n| **Alvin Ford** | 1986 | Stayed; led to *Ford v. Wainwright* (SCOTUS ruled insane prisoners cannot be executed) |\n| **Thomas Provenzano** |
Multiple stays, executed 2000 | Prolonged competency disputes |\n| **Angel Diaz** | 2006 | Execution proceeded but was badly botched (34 minutes), leading to a moratorium |\n| **Post-Diaz moratorium**
| 2007\u20132008 | All Florida executions effectively stayed while protocols were revised |\n| **John Ferguson** | Multiple stays, executed 2013 | Extensive competency litigation over decades |\n|
**Askari Abdullah Muhammad** | Multiple stays, executed 2014 | Lethal injection protocol challenges |\n| **Jerry Correll** | Stay lifted, executed 2015 | Brief stay related to drug sourcing |\n|
**Mark Asay** | 2017 | Nearly stayed over new drug (etomidate); execution proceeded |\n| **Jos\u00e9 Jimenez** | 2023 | Received a stay, execution did not proceed |\n| **Duane Owen** | 2023 |
Temporary stay before execution proceeded June 15, 2023 |\n\n## 5. Period-Specific Patterns\n\n### 1979\u20131999: High Warrant Volume, Many Stays\n- Governors signed warrants aggressively, often to
\"start the clock\" on federal habeas litigation\n- A **large proportion** of signed warrants (estimated 60\u201380%+) resulted in stays\n- Many inmates received **multiple warrants** over the years
before eventual execution\n\n### 2000\u20132006: More Selective Warranting\n- Improved completion rate as the state became more strategic\n- Still occasional stays for method-of-execution
challenges\n\n### 2007\u20132008: De Facto Moratorium\n- Following the botched Angel Diaz execution (December 2006), Governor Charlie Crist imposed an executive moratorium\n- All scheduled executions
were effectively postponed\n- New lethal injection protocols adopted in 2008\n\n### 2009\u20132015: Resumed but Slow\n- Executions resumed but at a modest pace (1\u20133/year)\n- Occasional stays for
drug-sourcing and protocol issues\n\n### 2016\u20132019: Hurst v. Florida Disruption\n- The January 2016 SCOTUS ruling in *Hurst v. Florida* invalidated the state's sentencing procedure\n- This
created massive legal uncertainty; very few executions carried out\n- Florida executed **only 3 people** from 2016 through 2019\n\n### 2020\u20132022: COVID and Continued Slowdown\n- Zero executions
in 2020 and 2021 (partly COVID-related)\n- Executions resumed in 2022\u20132023\n\n### 2023\u2013Present: Acceleration Under DeSantis\n- Governor DeSantis signed multiple death warrants in 2023\n- At
least **5\u20136 executions** carried out in 2023 alone\n- Included Louis Gaskin, Dayle Merrell, Duane Owen, Michael Duane Zack III, and others\n- Florida also passed a law reducing the jury unanimity
requirement for death sentences (8-4 sufficient)\n\n## 6. Overall Completion Rates\n\n| Metric | Estimate | Notes |\n|--------|----------|-------|\n| Death sentences to execution (all-time) |
~10\u201315% | Most sentences overturned, commuted, or inmate dies of other causes |\n| Signed warrants to execution (1979\u20131990s) | ~20\u201340% | Many warrants stayed; aggressive warrant-signing
era |\n| Signed warrants to execution (2010s\u2013present) | ~70\u201385% | More selective warranting after appeals exhausted |\n| Exonerations from death row | ~30 people | Highest of any U.S. state
|\n\n## 7. Key Contextual Factors\n\n- **Florida's clemency process is unusually restrictive**: The Governor must initiate clemency proceedings; inmates cannot apply independently. This means
executive clemency stays are extremely rare.\n- **Florida leads the nation in death row exonerations** (~30), suggesting the system has historically had significant error rates, which partly drives
the high appeal/stay rate.\n- **The *Hurst* decision** was enormously disruptive, calling into question hundreds of death sentences and effectively pausing executions for years.\n- **Drug
availability** has been an ongoing issue; Florida has had to change its lethal injection protocol multiple times due to inability to source drugs.\n\n## Limitations of This Report\n\n- **No live web
data could be retrieved** \u2014 all web search and fetch tools were unavailable in this session. All figures are drawn from training knowledge (cutoff: early 2025).\n- Exact aggregate statistics on
stays vs. completions are not maintained in any single public database; the estimates above are synthesized from multiple academic and journalistic sources.\n- Data for 2025\u20132026 execution
activity is not available.\n- The \"warrant completion rate\" figures are estimates based on historical reporting and may vary by source.\n\n---", "sources": [{"url":
"https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida", "title": "Death Penalty Information Center - Florida", "domain": "deathpenaltyinfo.org", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "Comprehensive state-by-state data on Florida executions, death row population, and exonerations. Unable to fetch live data; referenced from training knowledge."},
{"url": "https://www.dc.state.fl.us/ci/execlist.html", "title": "Florida Department of Corrections - Execution List", "domain": "dc.state.fl.us", "accessed_at": "2026-06-17T00:00:00Z", "snippet":
"Official Florida DOC execution list with all names and dates. Unable to fetch live data; referenced from training knowledge."}, {"url":
"https://en.wikipedia.org/wiki/List_of_people_executed_in_Florida", "title": "Wikipedia - List of people executed in Florida", "domain": "en.wikipedia.org", "accessed_at": "2026-06-17T00:00:00Z",
"snippet": "Comprehensive list of Florida executions with dates, methods, and case details. Unable to fetch live data; referenced from training knowledge."}, {"url":
"https://en.wikipedia.org/wiki/Capital_punishment_in_Florida", "title": "Wikipedia - Capital punishment in Florida", "domain": "en.wikipedia.org", "accessed_at": "2026-06-17T00:00:00Z", "snippet":
"Overview of Florida death penalty legal history, procedures, and statistics. Unable to fetch live data; referenced from training knowledge."}, {"url":
"https://supreme.justia.com/cases/federal/us/477/399/", "title": "Ford v. Wainwright, 477 U.S. 399 (1986)", "domain": "supreme.justia.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Landmark
SCOTUS case originating from Florida establishing that insane prisoners cannot be executed."}, {"url": "https://supreme.justia.com/cases/federal/us/577/136-01/", "title": "Hurst v. Florida, 577 U.S.
92 (2016)", "domain": "supreme.justia.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "SCOTUS decision invalidating Florida's death sentencing procedure, causing years of disruption to the
state's execution schedule."}], "key_facts": ["Florida has carried out approximately 105-110 executions since reinstating the death penalty in 1976 (through ~mid-2025)", "Florida's first post-
reinstatement execution was John Spenkelink on May 25, 1979", "During the 1980s-1990s warrant-signing era, an estimated 60-80%+ of signed death warrants resulted in stays rather than executions",
"Governor Bob Graham signed over 100 death warrants but only ~16 executions were carried out during his tenure (1979-1987)", "In recent years, the warrant-to-execution completion rate has improved to
an estimated 70-85% as governors became more selective about signing warrants", "Only roughly 10-15% of all Florida death sentences ultimately result in execution", "Florida leads the nation with
approximately 30 death row exonerations since 1973", "A de facto execution moratorium existed from 2007-2008 following the botched Angel Diaz execution", "The Hurst v. Florida (2016) SCOTUS decision
disrupted Florida executions for years by invalidating the sentencing procedure", "Florida executed only 3 people from 2016 through 2019 due to Hurst-related uncertainty", "Zero executions were
carried out in Florida in 2020 and 2021 (COVID-related delays)", "Florida accelerated executions in 2023 under Governor DeSantis with 5-6 executions carried out", "Florida passed legislation in 2023
allowing non-unanimous (8-4) jury death recommendations", "Florida's death row population has been approximately 300-330 inmates, among the largest in the nation", "Florida's clemency process is
unusually restrictive - the Governor must initiate proceedings; inmates cannot apply independently", "Common grounds for stays include competency challenges, lethal injection protocol disputes, newly
discovered evidence, and intellectual disability claims"], "data_points": [{"metric": "Total Florida executions since 1976", "value": 107.0, "unit": "executions", "as_of": "2025-01-01", "source_url":
"https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida death row population", "value": 310.0, "unit": "inmates", "as_of": "2024-07-01", "source_url":
"https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida death row exonerations since 1973", "value": 30.0, "unit": "exonerees", "as_of": "2025-01-01",
"source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Death warrants signed by Gov. Graham (1979-1987)", "value": 100.0, "unit": "warrants", "as_of":
"1987-01-01", "source_url": "https://en.wikipedia.org/wiki/Capital_punishment_in_Florida"}, {"metric": "Executions carried out under Gov. Graham", "value": 16.0, "unit": "executions", "as_of":
"1987-01-01", "source_url": "https://en.wikipedia.org/wiki/Capital_punishment_in_Florida"}, {"metric": "Estimated warrant-to-execution completion rate (1980s era)", "value": 20.0, "unit": "percent",
"as_of": "1990-01-01", "source_url": "https://en.wikipedia.org/wiki/Capital_punishment_in_Florida"}, {"metric": "Estimated warrant-to-execution completion rate (2010s-present)", "value": 77.0, "unit":
"percent", "as_of": "2024-01-01", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Estimated death sentence to execution rate (all-time)",
"value": 12.0, "unit": "percent", "as_of": "2024-01-01", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida executions in 2023", "value":
6.0, "unit": "executions", "as_of": "2023-12-31", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida executions 2016-2019 (post-Hurst)",
"value": 3.0, "unit": "executions", "as_of": "2019-12-31", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida executions in 2020",
"value": 0.0, "unit": "executions", "as_of": "2020-12-31", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}, {"metric": "Florida executions in 2021",
"value": 0.0, "unit": "executions", "as_of": "2021-12-31", "source_url": "https://deathpenaltyinfo.org/state-and-federal-info/state-by-state/florida"}], "created_at": "2026-06-17T09:13:26.175999Z",
"updated_at": "2026-06-17T09:13:26.175999Z", "stale_after": "2026-06-24T09:13:26.175999Z", "state": "fresh", "revision_history": [], "session_id": "6cf3d29f-a27e-4a3f-ab0e-383d7e1a4af4",
"follow_up_count": 0}, "is_follow_up": false}], "successful_count": 3, "failed_count": 0}
```

## 💬 Response

Now let me check the DPIC upcoming executions page directly and search for any last-minute updates on Spencer's case.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://deathpenaltyinfo.org/executions/upcoming-executions",
  "prompt": "List all executions scheduled for June 25-28, 2026. Are there any executions besides Dusty Ray Spencer?"
}
```

### 📋 Result

```
{"url": "https://deathpenaltyinfo.org/executions/upcoming-executions", "content": "Based on the content provided, there is **only one execution** scheduled for June 25-28, 2026:\n\n- **June 25,
2026**: Dusty Ray Spencer (Florida)\n\nNo other executions are scheduled for June 26-28, 2026. The next scheduled execution after Spencer is Dennis Sochor in Florida on July 14, 2026.\n\nRelevant
links:\n- [Outcomes of Warrants page](https://deathpenaltyinfo.org/executions/upcoming-executions/outcomes-of-warrants/outcomes-of-death-warrants-in-2025-2) - For more information on all executions
scheduled in 2026", "title": "Upcoming Executions | Death Penalty Information Center"}
```

```json
{
  "query": "Dusty Ray Spencer Florida execution June 25 2026 stay appeal"
}
```

### 📋 Result

```
{"query": "Dusty Ray Spencer Florida execution June 25 2026 stay appeal", "results": [{"title": "STOP the Execution of Dusty Ray Spencer - Catholic Mobilizing Network", "url":
"https://catholicsmobilizing.org/take-action/stop-the-execution-of-dusty-ray-spencer/", "snippet": "STOP the Execution of Dusty Ray Spencer\nPlease contact Governor Ron DeSantis and the Florida Board
of Executive Clemency urging them to grant clemency to Dusty Ray Spencer, and stop his execution.\nFlorida intends to execute Dusty Ray Spencer on June 25, 2026 for the 1992 murder of Karen
Spencer.\nWe oppose this execution as we do every execution. Capital punishment is an act of state sanctioned violence that violates the sacred dignity of every human life. In the words of Saint Pope
John Paul II,", "api_data": null, "hint": null}, {"title": "THE CASE AGAINST EXECUTING DUSTY RAY SPENCER : Scheduled to Be Executed on June 25, 2026 @ Florida State Prison", "url":
"https://executioninterventionproject.substack.com/p/the-case-against-executing-dusty", "snippet": "THE CASE AGAINST EXECUTING DUSTY RAY SPENCER : Scheduled to Be Executed on June 25, 2026 @ Florida
State Prison\nJeff Hood\nTHE CASE AGAINST EXECUTING DUSTY RAY SPENCER\nA Comprehensive Argument for Mercy\nExecution Scheduled: June 25, 2026 | Florida State Prison, Starke\nIntroduction: A Life Worth
Reconsidering\nDusty Ray Spencer, a 74-year-old military veteran, is scheduled to die by lethal injection on June 25, 2026. He has spent more than three decades on Florida\u2019s death row. The crime
he committe", "api_data": null, "hint": null}, {"title": "Expired Drugs And A Failing Liver: 74-Year-Old Florida Inmate Fights Looming Execution - Tampa Free Press", "url":
"https://www.tampafp.com/expired-drugs-and-a-failing-liver-74-year-old-florida-inmate-fights-looming-execution/", "snippet": "Dusty Ray Spencer is scheduled to die by lethal injection on June 25,
2026, but his legal team is fighting to stop the execution, citing his severe medical conditions and the state\u2019s alleged use of expired lethal drugs.\nGovernor DeSantis signed [Spencer\u2019s
death warrant late last month](https://www.tampafp.com/horrific-details-reveal-brutal-1992-attack-ahead-of-dusty-ray-spencers-florida-execution/), expediting a legal battle that has now reached the
Supreme Court of Florida. Spencer was original", "api_data": null, "hint": null}, {"title": "NEW WARRANT: Dusty Ray Spencer's Execution Scheduled 6/25/2026", "url":
"https://fladeathpenalty.substack.com/p/new-warrant-dusty-ray-spencers-execution", "snippet": "NEW WARRANT: Dusty Ray Spencer's Execution Scheduled 6/25/2026\nToday, Gov. DeSantis signed a death
warrant scheduling Dusty Ray Spencer\u2019s execution for June 25, 2026. It is the tenth death warrant he has signed this year.\nToday, Gov. DeSantis signed a death warrant scheduling Dusty Ray
Spencer\u2019s execution for June 25, 2026. The warrant period is exactly 30 days. It is the tenth death warrant he has signed this year. (View the full list, maintained by TFDP,
[here](https://fladeathpenalty.substack", "api_data": null, "hint": null}, {"title": "Things To Know About Dusty Ray Spencer As Florida Sets Execution Date in 1992 Murder Case", "url":
"https://www.ibtimes.sg/things-know-about-dusty-ray-spencer-florida-sets-execution-date-1992-murder-case-87010", "snippet": "![Dusty Ray Dusty Ray](https://data.ibtimes.sg/en/full/89374/dusty-
ray.png?w=736)\nFlorida is preparing to execute Dusty Ray Spencer, a 74-year-old death row inmate convicted of brutally killing his wife in a 1992 domestic violence case that prosecutors said involved
beating, stabbing and repeated threats of murder before the fatal attack.\nGov. Ron DeSantis signed Dusty's death warrant this week, scheduling his execution for June 25 at Florida State Prison in
Starke. The execution window extends ", "api_data": null, "hint": null}, {"title": "Gov. DeSantis signs 10th death warrant of 2026 for Florida man convicted of stabbing his wife to death in 1992 - CBS
Miami", "url": "https://www.cbsnews.com/miami/news/desantis-10th-death-warrant-2026-dusty-ray-spencer/", "snippet": "Gov. DeSantis signs 10th death warrant of 2026 for Florida man convicted of
stabbing his wife to death in 1992\nGov. Ron DeSantis signed his tenth death warrant of 2026 on Tuesday, this time for Dusty Ray Spencer, who has spent more than three decades on [Death
Row](https://www.cbsnews.com/miami/tag/death-row/) for murdering his wife in Orange County.\nSpencer, 74, is scheduled to die by lethal injection on June 25 at Florida State Prison in Stark, according
to the warrant. The window to carry out", "api_data": null, "hint": null}, {"title": "Dusty Spencer Faces Execution on June 25 - Floridians for Alternatives to the Death Penalty", "url":
"https://www.fadp.org/dusty-spencer-faces-execution-on-june-25/", "snippet": "U.S. Marine Corps veteran Lance Corporal Dusty Ray Spencer is scheduled to be executed on June 25, 2026, after spending
more than 34 years on Florida\u2019s death row. He was sentenced to death for the 1992 murder of his wife, Karen Spencer.\nAs Florida continues its unprecedented pace of executions, it is preparing to
execute a 74-year-old Marine Corps veteran whom five jurors believed should receive a life sentence, despite significant mitigating evidence, serious health issues, and more than 34 yea", "api_data":
null, "hint": null}, {"title": "Florida Man Challenges Lethal Injection Protocol, Citing Constitutional Flaws - Davis Vanguard", "url": "https://davisvanguard.org/2026/06/florida-death-row-inmate-
appeal/", "snippet": "![](https://davisvanguard.org/wp-content/uploads/2026/03/Death-Penalty-765x510.webp)\nA Florida death row man scheduled to be executed June 25 has asked a state court to halt his
execution, arguing that his age, medical conditions and Florida\u2019s lethal injection protocol could violate his constitutional rights.\nDusty Ray Spencer, a Florida death row man scheduled to be
executed June 25, filed a successive motion for post-conviction relief June 3 in the Ninth Judicial Circuit Court of Florida, acco", "api_data": null, "hint": null}]}
```

```json
{
  "query": "\"execution\" \"June 2026\" scheduled United States"
}
```

### 📋 Result

```
{"query": "\"execution\" \"June 2026\" scheduled United States", "results": [{"title": "Pending U.S. Executions (as of 06/11/2026) \u2013 Death Penalty News and Updates", "url":
"https://people.smu.edu/rhalperi/pending-u-s-executions/", "snippet": "Please note that these dates are only tentative.\nExecution dates known or thought to be considered SERIOUS are marked\nwith a
*.\nThe designation indicates that an execution is considered\nmore likely to be carried out.\nPlease note that this designation should in no way be construed as\nabsolute. Stays can be granted or
denied at the very last moment prior\nto an execution.\nA name with no * designation may simply mean that not enough information\nis currently available to know whether the execution da", "api_data":
null, "hint": null}, {"title": "List of people scheduled to be executed in the United States", "url": "https://en.wikipedia.org/wiki/List_of_people_scheduled_to_be_executed_in_the_United_States",
"snippet": "As of June 11, 2026, a total of 36 people are scheduled to be executed in the United States. All of these executions are scheduled over four calendar years in six U.S. states.
Additionally, there are 19 pending requests to set an execution date in six U.S. states and by the U.S. military.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of people
scheduled to be executed in the United States\", \"url\": \"https://en.wikipedia.org/wiki/List_of_people_scheduled_to_be_executed_in_the_United_States\", \"extract\": \"As of June 11, 2026, a total of
36 people are scheduled to be executed in the United States. All of these executions are scheduled over four calendar years in six U.S. states. Additionally, there are 19 pending requests to set an
execution date in six U.S. states and by the U.S. military.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Andrew Lukehart is Scheduled for Execution in Florida on June 2, 2026 - Floridians for
Alternatives to the Death Penalty", "url": "https://www.fadp.org/andrew-lukehart-is-scheduled-for-execution-in-florida-on-june-2-2026/", "snippet": "Andrew Lukehart Never Received the Help He Needed.
Florida Plans to Execute Him Anyway.\nAndrew Lukehart is scheduled to be executed by the State of Florida on Tuesday, June 2, 2026, at 6 pm for the 1996 death of Gabrielle Hanshaw. Gabrielle\u2019s
death was a devastating tragedy, and in Andrew\u2019s background diminishes the gravity of that loss or the pain experienced by those who loved her.\nBut Andrew\u2019s execution is yet another example
of an unconstitutional execution in Florida. Despite a nonunanimous", "api_data": null, "hint": null}, {"title": "List of killings by law enforcement officers in the United States, June 2026", "url":
"https://en.wikipedia.org/wiki/List_of_killings_by_law_enforcement_officers_in_the_United_States,_June_2026", "snippet": "This is a list of people reported killed by non-military law enforcement
officers in the United States\nin June 2026, whether in the line of duty or not, and regardless of reason or method. The listing documents the occurrence of a death, making no implications regarding
wrongdoing or justification on the part of the person killed or officer involved. Killings are arranged by date of the incident that caused death. Different death dates, if known, are noted in the
description.\nThe table below lis", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of killings by law enforcement officers in the United States, June 2026\", \"url\":
\"https://en.wikipedia.org/wiki/List_of_killings_by_law_enforcement_officers_in_the_United_States,_June_2026\", \"extract\": \"This is a list of people reported killed by non-military law enforcement
officers in the United States\\nin June 2026, whether in the line of duty or not, and regardless of reason or method. The listing documents the occurrence of a death, making no implications regarding
wrongdoing or justification on the part of the person killed or officer involved. Killings are arranged by date of the incident that caused death. Different death dates, if known, are noted in the
description.\\nThe table below lists 48 people.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "List of people executed in the United States in 2026", "url":
"https://en.wikipedia.org/wiki/List_of_people_executed_in_the_United_States_in_2026", "snippet": "To date, fifteen people, all male, were executed in the United States in 2026, all by lethal
injection.\nJames Ernest Hitchcock, one of Florida's longest-serving prisoners on death row, was executed nearly 50 years after he was convicted of the 1976 rape and murder of his 13-year-old step-
niece Cynthia Driggers.\nCharles Lee Burton was originally scheduled to be executed in Alabama by nitrogen hypoxia on March 12, 2026. His death sentence was commuted to life without parole by Governor
Kay Ivey ju", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of people executed in the United States in 2026\", \"url\":
\"https://en.wikipedia.org/wiki/List_of_people_executed_in_the_United_States_in_2026\", \"extract\": \"To date, fifteen people, all male, were executed in the United States in 2026, all by lethal
injection.\\nJames Ernest Hitchcock, one of Florida's longest-serving prisoners on death row, was executed nearly 50 years after he was convicted of the 1976 rape and murder of his 13-year-old step-
niece Cynthia Driggers.\\nCharles Lee Burton was originally scheduled to be executed in Alabama by nitrogen hypoxia on March 12, 2026. His death sentence was commuted to life without parole by
Governor Kay Ivey just two days before his scheduled execution.\\nTony Von Carruthers, who was originally scheduled to be executed in Tennessee on May 21, 2026, had his execution canceled and received
a one-year stay of execution after the prison officials failed to find a suitable vein. Jeffrey James Lee was originally scheduled to be put to death by nitrogen hypoxia on June 11, 2026, but his
execution was stayed after the federal courts found it likely unconstitutional to execute him by nitrogen hypoxia, and Attorney General Steve Marshall had since sought a new execution date for Lee and
replaced the method with lethal injection.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Jeffrey Lee Scheduled Execution June 11 2026", "url": "https://murderdb.com/jeffrey-lee-scheduled-
execution-june-11-2026/", "snippet": null, "api_data": null, "hint": null}, {"title": "Execution Petitions - Death Penalty Action", "url": "https://deathpenaltyaction.org/take-action/execution-
petitions/", "snippet": null, "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://people.smu.edu/rhalperi/pending-u-s-executions/",
  "prompt": "List ALL executions scheduled for June 25, 26, 27, 28, 2026 with their states and status. Are any marked as serious/likely to proceed?"
}
```

### 📋 Result

```
{"url": "https://people.smu.edu/rhalperi/pending-u-s-executions/", "content": "Based on the provided content, here are the executions scheduled for June 25-28, 2026:\n\n**June 25, 2026:**\n- Dusty Ray
Spencer (Florida) - marked as serious (*) - likely to proceed\n\n**June 26-28, 2026:**\n- No executions scheduled\n\nOnly one execution is listed for the requested date range (June 25-28, 2026). It is
marked with an asterisk (*), indicating it is considered serious and more likely to be carried out.\n\nRelevant links:\n- The content itself is from [https://people.smu.edu/rhalperi/pending-u-s-
executions/](https://people.smu.edu/rhalperi/pending-u-s-executions/) which may contain more current information", "title": "Pending U.S. Executions (as of 06/11/2026)"}
```

```json
{
  "query": "Spencer Florida Supreme Court SC2026-0880 ruling stay execution"
}
```

### 📋 Result

```
{"query": "Spencer Florida Supreme Court SC2026-0880 ruling stay execution", "results": [{"title": "Florida Supreme Court keeps ex-cop's execution on hold after DNA test fails to give a clear answer",
"url": "https://www.foxnews.com/us/florida-supreme-court-keeps-ex-cops-execution-hold-dna-test-fails-give-clear-answer", "snippet": "[Fox News Flash top headlines for August
9](https://www.foxnews.com/video/6310652368112)\nFox News Flash top headlines are here. Check out what's clicking on Foxnews.com.\nThe execution of a former police officer convicted of murdering and
raping a young girl nearly 40 years ago will remain on hold after the [state Supreme Court](https://www.foxnews.com/category/us/us-regions/southeast/florida) on Monday denied the state\u2019s request
to lift the stay, according to court documents.\nJames Duckett, a fo", "api_data": null, "hint": null}, {"title": "Death row inmate appeals execution to Florida court - WFTV", "url":
"https://www.wftv.com/news/local/orange-county-man-convicted-wifes-murder-1992-fights-death-sentence/J2XEL6JYZBGUZNV5VV6XD5RFRU/", "snippet": "We\u2019re Sorry!\nThis website is unavailable in your
location.\nError 451\nIt appears you are attempting to access this website from a country outside of the United States, therefore access cannot be granted at this time.\nThis website is unavailable in
your location.\nIt appears you are attempting to access this website from a country outside of the United States, therefore access cannot be granted at this time.", "api_data": null, "hint": null},
{"title": "Florida Supreme Court declines to lift stay of execution for ex-cop", "url": "https://www.yahoo.com/news/articles/florida-supreme-court-declines-lift-223046481.html", "snippet": "Florida
Supreme Court declines to lift stay of execution for ex-cop\nThe Florida Supreme Court declined Monday to lift the [stay of execution](https://www.tampabay.com/news/crime/2026/03/26/james-duckett-
execution-teresa-mcabee-murder-mascotte/) it granted to James Duckett, ensuring that the former police officer will not be executed Tuesday.\nIn a brief ruling, the state\u2019s high court ordered a
trial judge in Lake County, where the case originated, to provide a status report to them by the end of ", "api_data": null, "hint": null}, {"title": "Supreme Court of Florida THURSDAY, MARCH 26, 2026
James Aren Duckett,", "url": "https://files.deathpenaltyinfo.org/documents/James-Duckett_Stay-of-Execution_03.26.26.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Execution of
James Duckett to stay on hold after Florida Supreme Court denies state request", "url": "https://www.clickorlando.com/news/politics/2026/03/30/execution-of-james-duckett-to-stay-on-hold-after-florida-
supreme-court-denies-state-request/", "snippet": "LAKE COUNTY, Fla. \u2013 Plans to execute a former Mascotte police officer for the death of a girl in 1987 will remain on hold after the Florida
Supreme Court denied the state\u2019s request to allow the execution to proceed.\nLast week, the high court issued a rare stay of execution for James Duckett because the court was still waiting for
the results of new DNA testing.\nDuckett was convicted of killing 11-year-old Teresa McAbee, according to a death warrant signed by Gov. Ron DeSantis.\nThe DNA test resul", "api_data": null, "hint":
null}, {"title": "James Duckett: Execution on hold after Florida Supreme Court denies request to lift stay | FOX 35 Orlando", "url": "https://www.fox35orlando.com/news/james-duckett-execution-hold-
after-florida-supreme-court-denies-request-lift-stay", "snippet": "James Duckett: Execution on hold after Florida Supreme Court denies request to lift stay\nThe execution of a former Florida police
officer for the murder of a girl in 1987 will remain on hold after the Florida Supreme Court denied the state's request for the execution to proceed.\n[CLICK TO DOWNLOAD THE FOX LOCAL
APP](https://www.fox35orlando.com/fox-local)\nJames Duckett, a former Mascotte police officer, was convicted of killing 11-year-old Teresa McAbee nearly 40 years ago.\nWhat we know:\nDuckett",
"api_data": null, "hint": null}, {"title": "Execution on hold for former police officer on sentenced to death - WMNF 88.5 FM", "url": "https://www.wmnf.org/execution-on-hold-for-former-police-officer-
on-sentenced-to-death/", "snippet": "![death penalty law](https://cdn.wmnf.org/wp-content/uploads/2026/02/Death-penalty-by-Kagenmi-via-iStock-for-WMNF-News.jpg)\nListen:\nA scheduled execution in
Florida will not happen on Tuesday.\nIt comes after the Florida Supreme Court refused to lift the stay of execution it granted to the former police officer.\nJames Duckett was convicted of sexual
battery and the murder of an 11-year-old girl in 1987.\nHis legal team requested DNA testing, which they hoped would clear Duckett, and the results we", "api_data": null, "hint": null}, {"title":
"LEONARD SPENCER, Appellant, vs . ...", "url": "https://library.law.fsu.edu/Digital-Collections/flsupct/dockets/69883/op-69883.pdf", "snippet": null, "api_data": null, "hint": null}, {"title":
"20260313110354812 25A1000%20King%20COS%20Resp%20Stay", "url": "https://www.supremecourt.gov/DocketPDF/25/25A1000/400800/20260313110354812_25A1000%20King%20COS%20Resp%20Stay.pdf", "snippet": null,
"api_data": null, "hint": null}, {"title": "20260223112300313 25A926 %20Trotter%20COS%20Resp%20Stay", "url":
"https://www.supremecourt.gov/DocketPDF/25/25A926/396999/20260223112300313_25A926-%20Trotter%20COS%20Resp%20Stay.pdf", "snippet": null, "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"Dusty Spencer\" execution \"Florida Supreme Court\" 2026 ruling"
}
```

### 📋 Result

```
{"query": "\"Dusty Spencer\" execution \"Florida Supreme Court\" 2026 ruling", "results": [{"title": "THE CASE AGAINST EXECUTING DUSTY RAY SPENCER : Scheduled to Be Executed on June 25, 2026 @ Florida
State Prison", "url": "https://executioninterventionproject.substack.com/p/the-case-against-executing-dusty", "snippet": "THE CASE AGAINST EXECUTING DUSTY RAY SPENCER : Scheduled to Be Executed on
June 25, 2026 @ Florida State Prison\nJeff Hood\nTHE CASE AGAINST EXECUTING DUSTY RAY SPENCER\nA Comprehensive Argument for Mercy\nExecution Scheduled: June 25, 2026 | Florida State Prison,
Starke\nIntroduction: A Life Worth Reconsidering\nDusty Ray Spencer, a 74-year-old military veteran, is scheduled to die by lethal injection on June 25, 2026. He has spent more than three decades on
Florida\u2019s death row. The crime he committe", "api_data": null, "hint": null}, {"title": "NEW WARRANT: Dusty Ray Spencer's Execution Scheduled 6/25/2026", "url":
"https://fladeathpenalty.substack.com/p/new-warrant-dusty-ray-spencers-execution", "snippet": "NEW WARRANT: Dusty Ray Spencer's Execution Scheduled 6/25/2026\nToday, Gov. DeSantis signed a death
warrant scheduling Dusty Ray Spencer\u2019s execution for June 25, 2026. It is the tenth death warrant he has signed this year.\nToday, Gov. DeSantis signed a death warrant scheduling Dusty Ray
Spencer\u2019s execution for June 25, 2026. The warrant period is exactly 30 days. It is the tenth death warrant he has signed this year. (View the full list, maintained by TFDP,
[here](https://fladeathpenalty.substack", "api_data": null, "hint": null}, {"title": "Expired Drugs And A Failing Liver: 74-Year-Old Florida Inmate Fights Looming Execution - Tampa Free Press", "url":
"https://www.tampafp.com/expired-drugs-and-a-failing-liver-74-year-old-florida-inmate-fights-looming-execution/", "snippet": "Dusty Ray Spencer is scheduled to die by lethal injection on June 25,
2026, but his legal team is fighting to stop the execution, citing his severe medical conditions and the state\u2019s alleged use of expired lethal drugs.\nGovernor DeSantis signed [Spencer\u2019s
death warrant late last month](https://www.tampafp.com/horrific-details-reveal-brutal-1992-attack-ahead-of-dusty-ray-spencers-florida-execution/), expediting a legal battle that has now reached the
Supreme Court of Florida. Spencer was original", "api_data": null, "hint": null}, {"title": "STOP the Execution of Jeffery Lee - Catholic Mobilizing Network", "url":
"https://catholicsmobilizing.org/take-action/stop-the-execution-of-jeffrey-lee/", "snippet": null, "api_data": null, "hint": null}, {"title": "DeSantis signs death warrant for man convicted of 1992
Orange County murder | WUSF", "url": "https://www.wusf.org/courts-law/2026-05-28/desantis-signs-death-warrant-for-man-convicted-of-1992-orange-county-murder", "snippet": "Gov. Ron DeSantis signed his
10th death warrant of 2026 on Tuesday, this time for Dusty Ray Spencer, who has spent more than three decades on Death Row for murdering his wife in Orange County.\nSpencer, 74, is scheduled to die by
lethal injection on June 25 at Florida State Prison in Stark, according to the warrant. The window to carry out the sentence runs from noon June 25 through noon July 2.\nAccording to court records:\n-
Spencer had a violent history with his wife, Karen, before stabbing her ", "api_data": null, "hint": null}, {"title": "The Case Against Executing Dusty Ray Spencer | The Case Against Executing Dusty
Ray Spencer: Constitutional Failure, Suppressed Mitigation And The Limits Of Finality", "url": "https://www.patheos.com/blogs/jeffhood/the-case-against-executing-dusty-ray-spencer/", "snippet":
"![Dusty Spencer](https://wp-media.patheos.com/blogs/sites/751/2026/06/Dusty-Ray-Spencer.jpg)\nTHE CASE AGAINST EXECUTING DUSTY RAY SPENCER\nA Comprehensive Argument for Mercy\nExecution Scheduled:
June 25, 2026 | Florida State Prison, Starke\nIntroduction: Dusty Ray Spencer\u2019s is a Life Worth Reconsidering\nDusty Ray Spencer, a 74-year-old military veteran, is scheduled to die by lethal
injection on June 25, 2026. He has spent more than three decades on Florida\u2019s death row. The crime he committed was ", "api_data": null, "hint": null}, {"title": "SPENCER WARRANT: Postconviction
claims denied and appeal filed", "url": "https://fladeathpenalty.substack.com/p/spencer-warrant-postconviction-claims-ed0", "snippet": "SPENCER WARRANT: Postconviction claims denied and appeal
filed\nDusty Ray Spencer\u2019s execution is scheduled for June 25. Yesterday, the circuit court denied Spencer\u2019s postconviction claims, and he appealed to the Florida Supreme Court.\nDusty Ray
Spencer\u2019s execution is scheduled for June 25. (Read the background of Spencer\u2019s case [here](https://fladeathpenalty.substack.com/p/new-warrant-dusty-ray-spencers-execution?r=248zyf).)
Yesterday, the circuit court denied Spencer\u2019s postconviction claims, and", "api_data": null, "hint": null}, {"title": "Dusty Ray Spencer: Death warrant signed, execution date set | FOX 35
Orlando", "url": "https://www.fox35orlando.com/news/dusty-ray-spencer-death-warrant-signed-execution-date-set", "snippet": "Dusty Ray Spencer: Death warrant signed, execution date
set\n![](https://images.foxtv.com/static.fox35orlando.com/www.fox35orlando.com/content/uploads/2026/05/764/432/dusty-ray-spencer.jpg?ve=1&tl=1)\nDusty Ray Spencer Credit: Florida Department of
Corrections\nORLANDO, Fla. - A death warrant has been signed, and an execution date set, for a Florida man convicted of brutally beating, stabbing, and cutting his wife outside their home in Orange
County in January 1992.\nGov. Ron DeSantis signed the dea", "api_data": null, "hint": null}, {"title": "Florida Supreme Court Clears Way For February 24 Execution Of Melvin Trotter", "url":
"https://www.aol.com/articles/florida-supreme-court-clears-way-163554318.html", "snippet": "Florida Supreme Court Clears Way For February 24 Execution Of Melvin Trotter\nThe Florida Supreme Court
issued a ruling on Tuesday that paves the way for the execution of Melvin Trotter, a 65-year-old death row inmate scheduled to die by lethal injection on February 24, 2026.\nIn a unanimous decision,
the justices rejected Trotter's latest appeals, which challenged the state's execution protocols and argued that his age should exempt him from the death penalty.\nTrotter was convicted of the 1986
mu", "api_data": null, "hint": null}, {"title": "Spencer v. State", "url": "https://civilrightsopinions.justia.com/2018/11/08/spencer-v-state-2", "snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

Now I have a good picture. Let me check the Florida Supreme Court's recent DeSantis-era execution completion rate more precisely to understand how likely Spencer's is to proceed.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://fladeathpenalty.substack.com/p/spencer-warrant-postconviction-claims-ed0",
  "prompt": "What is the current status of Spencer's appeal to the Florida Supreme Court? Has the court ruled? Any stay granted? When was this posted?"
}
```

### 📋 Result

```
{"url": "https://fladeathpenalty.substack.com/p/spencer-warrant-postconviction-claims-ed0", "content": "Based on the content provided:\n\n**Current Status:**\n- The circuit court denied Spencer's
postconviction claims on the day before this article was posted (at 10:43 a.m.)\n- Spencer appealed to the Florida Supreme Court following the denial\n- His initial brief to the Supreme Court is due
on Friday at 2:00 p.m.\n- **The Florida Supreme Court has NOT yet ruled on the appeal**\n- **No stay of execution is mentioned as being granted**\n- Spencer's execution remains scheduled for June
25\n\n**When Posted:**\nThe article does not contain an explicit publication date, but references \"yesterday\" for the circuit court's order, indicating it was posted the day after that order was
entered.\n\n**Relevant links:**\n- [Background of Spencer's case](https://fladeathpenalty.substack.com/p/new-warrant-dusty-ray-spencers-execution?r=248zyf)\n- [More about Spencer's postconviction
claims](https://fladeathpenalty.substack.com/p/spencer-warrant-postconviction-claims)\n- [Florida Supreme Court case
docket](https://acis.flcourts.gov/portal/court/68f021c4-6a44-4735-9a76-5360b2e8af13/case/df9e8311-d7f1-4b71-b0d3-c320172b8992)", "title": "SPENCER WARRANT: Postconviction claims denied and appeal
filed"}
```

```json
{
  "url": "https://en.wikipedia.org/wiki/List_of_people_executed_in_the_United_States_in_2026",
  "prompt": "List all 15 executions carried out so far in 2026. Also note any that were stayed or postponed. How many were in Florida?"
}
```

### 📋 Result

```
{"title": "List of people executed in the United States in 2026", "url": "https://en.wikipedia.org/wiki/List_of_people_executed_in_the_United_States_in_2026", "extract": "To date, fifteen people, all
male, were executed in the United States in 2026, all by lethal injection.\nJames Ernest Hitchcock, one of Florida's longest-serving prisoners on death row, was executed nearly 50 years after he was
convicted of the 1976 rape and murder of his 13-year-old step-niece Cynthia Driggers.\nCharles Lee Burton was originally scheduled to be executed in Alabama by nitrogen hypoxia on March 12, 2026. His
death sentence was commuted to life without parole by Governor Kay Ivey just two days before his scheduled execution.\nTony Von Carruthers, who was originally scheduled to be executed in Tennessee on
May 21, 2026, had his execution canceled and received a one-year stay of execution after the prison officials failed to find a suitable vein. Jeffrey James Lee was originally scheduled to be put to
death by nitrogen hypoxia on June 11, 2026, but his execution was stayed after the federal courts found it likely unconstitutional to execute him by nitrogen hypoxia, and Attorney General Steve
Marshall had since sought a new execution date for Lee and replaced the method with lethal injection.", "mode": "full"}
```

## 💭 Thinking

Let me now compile my analysis. I have good information:

1. **Only one execution scheduled**: Dusty Ray Spencer in Florida on June 25, 2026
2. **No other executions scheduled** for June 26-28, 2026
3. **Spencer's status**: Execution still scheduled, no stay granted. Circuit court denied postconviction claims, appeal to Florida Supreme Court pending (case SC2026-0880)
4. **Florida's recent completion rate**: ~70-85% for signed warrants in recent years under DeSantis
5. **Florida in 2026**: Very active - DeSantis has signed 10 death warrants, ~8-9 executions already carried out
6. **Spencer marked as "serious"** on the SMU pending executions tracker

Spencer's most likely outcome is execution, though there's a chance the Florida Supreme Court could grant a stay on his pending appeal. His arguments around age, expired drugs, and liver failure are novel but haven't traditionally succeeded in Florida courts, and the state Supreme Court has generally supported executions under DeSantis—though they did issue a stay in the Duckett case, that was based on pending DNA evidence, a much stronger legal position than Spencer's claims.

I'm estimating roughly a 15-20% probability of a stay based on recent Florida patterns. For additional executions beyond Spencer, no others are currently scheduled, and emergency scheduling would be extremely unlikely in this timeframe, so I'm putting that at around 1-2%.

My probability distribution looks like: 15-20% chance of zero executions, 78-83% for one execution, 1-2% for two, and less than 0.5% for three or more. Since this is a discrete question with a range from -0.5 to 4.5, I need to map this to integer values: 0, 1, 2, 3, 4, and 5+ as the open upper bound. Let me reconsider the stay probability more carefully.

Looking at DeSantis's execution record from 2023-2026, Florida has been extremely aggressive—he signed 10 warrants in 2026 alone. Across the US this year, 15 executions have been carried out, with several in Florida proceeding despite some notable stays in other states. For Spencer specifically, his circuit court appeal was denied and his Florida Supreme Court appeal is still pending without a stay. His arguments around age and expired drugs are somewhat novel but courts have generally rejected similar claims. The SMU tracker marks his execution as "serious" and likely to proceed, and after 34 years of appeals, he's exhausted most avenues. Unlike cases with DNA evidence issues, his situation doesn't have that advantage, so I'm estimating the stay probability lower than my initial range. Now I'm calculating the cumulative distribution function values and mapping them to percentiles. Since the distribution is heavily skewed toward 1, the percentiles cluster at 0 for the lower end and at 1 for most of the middle and upper range, with 2 appearing only at the very high end around P99. Let me work through the cumulative distribution function more carefully. With P(X=0) = 0.15, P(X=1) = 0.83, P(X=2) = 0.018, and P(X≥3) = 0.002, the CDF shows that 15% of the distribution is at 0, 98% is at or below 1, and 99.8% is at or below 2. This means percentiles up to 15 map to 0, percentiles 16-98 map to 1, and percentiles 99-99.8 map to 2.

Most percentiles fall in the middle range where the value is 1, with only the highest percentiles reaching 2. Now I can move forward with the reflection and forecast.

## 💬 Response

Now let me compute the probability distribution for this discrete question.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Discrete distribution for number of executions June 25-28, 2026\n# Key facts:\n# - Only 1 execution scheduled: Dusty Ray Spencer (Florida, June 25)\n# - No other executions scheduled for June 26-28\n# - Spencer's appeal to FL Supreme Court is pending but no stay granted\n# - Circuit court denied his postconviction claims\n# - Marked as \"serious\" by SMU tracker\n# - In DeSantis era, FL warrant completion rate ~70-85%\n# - His arguments (age, expired drugs) are novel but generally unsuccessful\n\n# P(Spencer is stayed/postponed)\n# Factors favoring execution proceeding:\n# - Circuit court denied claims\n# - FL Supreme Court hasn't issued stay despite pending appeal\n# - DeSantis-era FL very aggressive with executions\n# - 8-9 FL executions already in 2026\n# - Marked \"serious\" by independent tracker\n# - 34 years of appellate history largely exhausted\n# Factors favoring stay:\n# - FL Supreme Court appeal still open (SC2026-0880)\n# - Novel arguments about age (74, would be oldest FL execution) and expired drugs\n# - Some recent FL stays (Duckett - but DNA evidence, different situation)\n\np_stay_spencer = 0.15  # 15% chance of stay\n\n# P(additional execution in window)\n# - No other executions scheduled June 25-28\n# - Next scheduled is July 14 (FL)\n# - Emergency scheduling essentially never happens in 4-day window\n# - Very small probability of an unscheduled execution\np_additional_one = 0.015  # extremely unlikely\np_additional_two_plus = 0.002\n\n# Distribution\np_0 = p_stay_spencer * (1 - p_additional_one)  # Spencer stayed, no surprise execution\np_1 = (1 - p_stay_spencer) * (1 - p_additional_one) + p_stay_spencer * p_additional_one\np_2 = (1 - p_stay_spencer) * p_additional_one + p_stay_spencer * p_additional_two_plus\np_3_plus = (1 - p_stay_spencer) * p_additional_two_plus\n\n# Normalize\ntotal = p_0 + p_1 + p_2 + p_3_plus\np_0 /= total\np_1 /= total\np_2 /= total\np_3_plus /= total\n\nprint(f\"P(0 executions) = {p_0:.4f}\")\nprint(f\"P(1 execution)  = {p_1:.4f}\")\nprint(f\"P(2 executions) = {p_2:.4f}\")\nprint(f\"P(3+ executions)= {p_3_plus:.4f}\")\n\n# CDF\ncdf = np.cumsum([p_0, p_1, p_2, p_3_plus])\nprint(f\"\\nCDF:\")\nprint(f\"F(0) = {cdf[0]:.4f}\")\nprint(f\"F(1) = {cdf[1]:.4f}\")\nprint(f\"F(2) = {cdf[2]:.4f}\")\nprint(f\"F(3) = {cdf[3]:.4f}\")\n\n# Expected value\nev = 0 * p_0 + 1 * p_1 + 2 * p_2 + 3 * p_3_plus\nprint(f\"\\nExpected value: {ev:.3f}\")\n\n# Generate percentile values\npercentiles = [1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nprint(f\"\\nPercentile values:\")\nfor p in percentiles:\n    p_frac = p / 100.0\n    if p_frac <= cdf[0]:\n        val = 0\n    elif p_frac <= cdf[1]:\n        val = 1\n    elif p_frac <= cdf[2]:\n        val = 2\n    else:\n        val = 3\n    print(f\"  P{p}: {val}\")\n\n# Monte Carlo validation\nnp.random.seed(42)\nn_sims = 100000\nsamples = np.random.choice([0, 1, 2, 3], size=n_sims, p=[p_0, p_1, p_2, p_3_plus])\nprint(f\"\\nMonte Carlo validation ({n_sims:,} samples):\")\nfor v in range(4):\n    print(f\"  P(X={v}) = {np.mean(samples == v):.4f}\")\nprint(f\"  Mean = {np.mean(samples):.3f}\")\nprint(f\"  Median = {np.median(samples):.0f}\")\n\nmc_percentiles = np.percentile(samples, percentiles)\nprint(f\"\\nMC Percentiles:\")\nfor p, v in zip(percentiles, mc_percentiles):\n    print(f\"  P{p}: {v:.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P(0 executions) = 0.1475\nP(1 execution)  = 0.8378\nP(2 executions) = 0.0130\nP(3+ executions)= 0.0017\n\nCDF:\nF(0) = 0.1475\nF(1) = 0.9853\nF(2) = 0.9983\nF(3) =
1.0000\n\nExpected value: 0.869\n\nPercentile values:\n  P1: 0\n  P5: 0\n  P10: 0\n  P15: 1\n  P20: 1\n  P25: 1\n  P30: 1\n  P40: 1\n  P50: 1\n  P60: 1\n  P70: 1\n  P75: 1\n  P80: 1\n  P90: 1\n  P95:
1\n  P99: 2\n\nMonte Carlo validation (100,000 samples):\n  P(X=0) = 0.1474\n  P(X=1) = 0.8381\n  P(X=2) = 0.0128\n  P(X=3) = 0.0017\n  Mean = 0.869\n  Median = 1\n\nMC Percentiles:\n  P1: 0.0\n  P5:
0.0\n  P10: 0.0\n  P15: 1.0\n  P20: 1.0\n  P25: 1.0\n  P30: 1.0\n  P40: 1.0\n  P50: 1.0\n  P60: 1.0\n  P70: 1.0\n  P75: 1.0\n  P80: 1.0\n  P90: 1.0\n  P95: 1.0\n  P99: 2.0\n", "stderr": "",
"duration_ms": 238}
```

## 💬 Response

Now let me run the reflection checkpoint.

## 💬 Response

Good. Now let me run the premortem.
