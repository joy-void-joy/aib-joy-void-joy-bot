# Reasoning Log: How many lawsuits will have been filed against the Trump Administration according to the JustSecurity tracker on August 31, 2026?

*Generated: 2026-07-17T09:12:42.779900+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "What is the current number of legal challenges/lawsuits listed on the Just Security Litigation Tracker of legal challenges to Trump Administration actions (justsecurity.org/107087)? Provide the count as of the most recent date available in 2026 and the historical trajectory of how the count has grown over 2025-2026.",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'What is the cu...025-2026.', 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "What is the current number of legal challenges/lawsuits listed on the Just Security Litigation Tracker of legal challenges to Trump Administration actions (justsecurity.org/107087)? Provide the count as of the most recent date available in 2026 and the historical trajectory of how the count has grown over 2025-2026, including monthly counts if possible.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "What is the current number of legal challenges/lawsuits listed on the Just Security Litigation Tracker of legal challenges to Trump Administration actions
(justsecurity.org/107087)? Provide the count as of the most recent date available in 2026 and the historical trajectory of how the count has grown over 2025-2026, including monthly counts if
possible.", "entry": {"slug": "what-is-the-current-number-of-legal-challenges-law-6eba500b", "query": "What is the current number of legal challenges/lawsuits listed on the Just Security Litigation
Tracker of legal challenges to Trump Administration actions (justsecurity.org/107087)? Provide the count as of the most recent date available in 2026 and the historical trajectory of how the count has
grown over 2025-2026, including monthly counts if possible.", "answer": "I've completed the research. Here's a summary of my findings on the Just Security Litigation Tracker:\n\n## Current Count\nAs
of **July 16, 2026** (most recent available), the tracker explicitly states: **\"Total number of cases currently tracked: 900.\"** This is confirmed directly from the live tracker page.\n\n**Breakdown
(900 total):** 285 plaintiff wins, 139 government wins, 414 pending, 62 other/mixed.\n\n## Historical Trajectory (2025\u20132026)\nThe tracker captures cases filed since January 20, 2025, growing at
more than two new cases per day:\n\n| Date | Cases |\n|------|-------|\n| ~June 2025 | ~271 |\n| Aug 6, 2025 | Relaunch (new features) |\n| ~Aug 14, 2025 | ~708 (implied from status snapshot) |\n|
**Feb 10, 2026** | **627** (explicit) |\n| **Apr 9, 2026** | **753** (explicit) |\n| May 2026 | 753 |\n| **Jul 16, 2026** | **900** (explicit) |\n\n**Key caveat:** The methodology appears to have been
recalibrated between the Aug 2025 relaunch (~708 implied) and Feb 2026 (627 explicit), so the cleanest comparable series is 627 \u2192 753 \u2192 900 across 2026 (~+273 cases in ~5 months, ~55/month).
Just Security publishes running totals rather than a monthly filing series, so exact monthly counts must be approximated from these snapshots.\n\n**Other caveats:** The tracker counts only suits
*against* the administration over executive actions (excludes Trump-filed suits and his personal cases). Other trackers report different totals due to differing consolidation methods (Lawfare: ~316
\"active cases\"; NYT: \"more than 800\").", "sources": [], "key_facts": [], "data_points": [], "created_at": "2026-07-17T09:11:35.357009Z", "updated_at": "2026-07-17T09:11:35.357009Z", "stale_after":
"2026-07-17T15:11:35.357009Z", "state": "fresh", "revision_history": [], "session_id": "267c1718-fa66-4737-a7cf-b23edfd38ab2", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1,
"failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: What is the current number of legal challenges/lawsuits listed on the Just Security Litigation Tracker of legal challenges to Trump Administration actions (justsecurity.org/107087)? Provide the count as of the most recent date available in 2026 and the historical trajectory of how the count has grown over 2025-2026, including monthly counts if possible.

*Generated: 2026-07-17T09:11:35.349545+00:00*


## 💬 Response

I'll research the Just Security Litigation Tracker to find the current count of legal challenges and its historical trajectory.

## 🔧 Tool: WebFetch


## 🔧 Tool: ToolSearch


```json
{
  "query": "web search",
  "max_results": 3
}
```

### 📋 Result

```

```

```json
{
  "url": "https://www.justsecurity.org/107087",
  "prompt": "What is the current total number of legal challenges/lawsuits listed on this Litigation Tracker of legal challenges to Trump Administration actions? Look for any stated count, number of cases tracked, last updated date, and any information about how many cases are listed. Report specific numbers and dates."
}
```

### 📋 Result

```
# Litigation Tracker Case Count

According to the document, the tracker currently monitors **900 total cases** tracking legal challenges to Trump administration executive actions.

The page was last updated on **July 16, 2026**.

## Case Status Breakdown:

The tracker provides these outcome snapshots:

- **Plaintiff Wins:** 285 cases (71 government actions blocked, 143 temporarily blocked, 38 blocked pending appeal, 33 closed in plaintiff favor)
- **Government Wins:** 139 cases (62 temporary blocks denied, 46 not blocked pending appeal, 31 dismissed in government favor)
- **Pending:** 414 cases
- **Other:** 62 cases with mixed outcomes or closed without clear resolution

The page notes: *"Total number of cases currently tracked: 900."*
```

## 💬 Response

I have the current count. Let me now research the historical trajectory to find monthly counts across 2025-2026.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Just Security Litigation Tracker Trump administration number of cases lawsuits 2025"
}
```

### 📋 Result

```
{"query": "Just Security Litigation Tracker Trump administration number of cases lawsuits 2025", "results": [{"title": "Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to Trump administration executive
actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-protection#375b4352775d42444344525442455e434e19584550). The Tracker
is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-
actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/", "snippet": "Today we are launching a major update to Just Security\u2019s [Litigation
Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/). We aim for this resource to be the most comprehensive public record of court challenges to
executive actions in the second Trump administration.\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format that allows users to follow both individual dockets
and monitor overall trends in near re", "api_data": null, "hint": null}, {"title": "Trump Administration Litigation Tracker", "url": "https://www.lawfaremedia.org/projects-series/trials-of-the-trump-
administration/tracking-trump-administration-litigation", "snippet": null, "api_data": null, "hint": null}, {"title": "Trackers Archives - Just Security", "url":
"https://www.justsecurity.org/tag/trackers/", "snippet": "Trackers\n5 Articles\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background
as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges
to Trump Admin", "api_data": null, "hint": null}, {"title": "Litigation Tracker Archives - Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet": "Litigation
Tracker\n16 Articles\n![Gavel and scales with a US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-
content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges to ",
"api_data": null, "hint": null}, {"title": "Collection: Just Security\u2019s Coverage of Trump Administration Executive Actions", "url": "https://www.justsecurity.org/106653/collection-trump-
administration-executive-actions/", "snippet": "On Jan. 20, President Donald Trump began his term with [presidential actions](https://www.whitehouse.gov/presidential-actions/) including 26 executive
orders, with more expected to follow. Just Security is covering key developments, including in concise \u201cWhat Just Happened\u201d expert explainers, legal and policy analysis, and
more.\nOriginally published Jan. 21, 2025, and frequently updated.\nTable of Contents\nA. Resources\nB. \u201cWhat Just Happened\u201d Series\nC. Analysis and Perspectives\nD. \u201cWhat Just Happ",
"api_data": null, "hint": null}, {"title": "TRUMP LAWSUITS - Comprehensive Tracker", "url": "https://trumplawsuits.com/", "snippet": "$88.3M judgments \u2022 34 felony convictions \u2022 $45B+ in
active claims \u2022\n328+ admin cases \u2022 30+ total tracked cases\nTrump Defendant - Criminal\n[People of NY v. Trump](https://www.newsweek.com/trump-appeals-stormy-daniels-hush-money-
conviction-2022997)\nCONVICTED: 34 felony counts\nfalsifying business records (Stormy Daniels hush money)\nCONVICTEDAPPEAL ACTIVEUnconditional discharge 1/10/25; Sullivan & Cromwell appealing
\u2022\nNY Supreme Court\n[United States v. Trump (Jan 6)](https://www.justice.gov/storage/", "api_data": null, "hint": null}, {"title": "Dissecting the Litigation: Where Trump Administration Actions
Face Early Roadblocks or Traction", "url": "https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/", "snippet": "Last week we
[relaunched](https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/) Just Security\u2019s [Litigation Tracker: Legal Challenges to Trump Administration
Actions](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/) with new features and stats. The infographics below provide a snapshot of what we are seeing,
i.e. where litigation stands and how courts are ruling on challenges to the administration\u2019s executive actions.\nThe Snapshot\nT", "api_data": null, "hint": null}, {"title": "Courts & Litigation
| Just Security", "url": "https://www.justsecurity.org/category/courts-litigation/", "snippet": "Courts & Litigation\nJust Security\u2019s expert authors offer analysis and informational resources on
key litigation impacting national security, rights, democracy, and the rule of law. Our content spans domestic and international litigation, from cases at the International Court of Justice, the
International Criminal Court, and other international and regional tribunals, to those in U.S. courts involving executive branch actions, transnational litigation, and more.\nHighlights:\n![A bank
with large Co", "api_data": null, "hint": null}, {"title": "Executive Action Trackers | Kathrine R. Everett Law Library", "url": "https://library.law.unc.edu/2025/03/executive-action-trackers/",
"snippet": "Executive Action Trackers\nMarch 10, 2025\nWithin the first two months of his second term, President Donald Trump issued more than 75 executive orders. These executive orders range in
topic, leaving many lawyers and law students struggling to stay informed about evolving laws and the impact on their lives and areas of practice. A large number of these executive orders have already
faced legal challenges. As lawyers work to stay abreast of these executive actions, as well as legal challenges to the", "api_data": null, "hint": null}]}
```

```json
{
  "query": "\"litigation tracker\" Trump legal challenges lawsuits count 2025 how many cases filed"
}
```

### 📋 Result

```
{"query": "\"litigation tracker\" Trump legal challenges lawsuits count 2025 how many cases filed", "results": [{"title": "Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to Trump administration executive
actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-protection#29455d4c69435c5a5d5a4c4a5c5b405d5007465b4e). The Tracker
is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-
actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "Trump Administration Litigation Tracker", "url": "https://www.lawfaremedia.org/projects-series/trials-of-the-trump-
administration/tracking-trump-administration-litigation", "snippet": null, "api_data": null, "hint": null}, {"title": "Trump Administration Faces Record 530 Lawsuits in 2025 \u2014 Far Exceeding
Biden, Obama, and Bush", "url": "https://thefulcrum.us/rule-of-law/supreme-court-rulings-2025", "snippet": "[The Fulcrum](https://thefulcrum.us/) strives to approach news stories with an open mind and
skepticism, striving to present our readers with a broad spectrum of viewpoints through diligent research and critical thinking. As best we can, we remove personal bias from our reporting and seek a
variety of perspectives in both our news gathering and selection of opinion pieces. However, before our readers can analyze varying viewpoints, they must have the facts.\nOn April 22 of this year, I
wrote a co", "api_data": null, "hint": null}, {"title": "Tracking lawsuits challenging Trump\u2019s executive orders and actions - The Washington Post", "url":
"https://www.washingtonpost.com/politics/2025/02/07/trump-lawsuits-executive-orders-actions-legal-challenges/", "snippet": null, "api_data": null, "hint": null}, {"title": "Trump\u2019s Legal Battles:
Tracking Hundreds of US Court Cases", "url": "https://www.bloomberg.com/graphics/2025-lawsuits-against-trump-administration-apple-news/", "snippet": null, "api_data": null, "hint": null}, {"title":
"Just the Facts: Courts\u2019 Actions Against the Trump Administration", "url": "https://thefulcrum.us/rule-of-law/trump-lawsuits-2025", "snippet": "[The Fulcrum](https://thefulcrum.us) strives to
approach news stories with an open mind and skepticism, striving to present our readers with a broad spectrum of viewpoints through diligent research and critical thinking. As best we can, we remove
personal bias from our reporting and seek a variety of perspectives in both our news gathering and selection of opinion pieces. However, before our readers can analyze varying viewpoints, they must
have the facts.\nHow many legal actions have been filed ", "api_data": null, "hint": null}, {"title": "how many lawsuits are against Donald trump right now", "url": "https://factually.co/fact-
checks/politics/current-lawsuits-against-donald-trump-2025-27726a", "snippet": "How many lawsuits are against Donald trump right now\n[Learn more](https://factually.co/faq).\nThis article may be
outdated. Consider refreshing it to get the most current information.\nExecutive summary\nCounting \u201chow many lawsuits are against Donald Trump right now\u201d depends on definition: trackers of
litigation targeting the Trump administration report figures ranging from about 186 suits by April 2025 to a surge later in the year and into December 2025 with multiple outlets citing hundreds of
cas", "api_data": null, "hint": null}, {"title": "What is the current status of Trump\u2019s legal cases as o...", "url": "https://factually.co/fact-checks/justice/trump-legal-cases-status-
november-2025-8a63b3", "snippet": "What is the current status of Trump\u2019s legal cases as of November 2025?\n[Learn more](https://factually.co/faq).\nThis article may be outdated. Consider
refreshing it to get the most current information.\nExecutive summary\nPresident Donald Trump\u2019s slate of criminal prosecutions that shadowed his first term has substantially narrowed: by November
26, 2025, the Fulton County (Georgia) election-interference prosecution was dismissed and prosecutors in several federal special\u2011counsel matters wound down ", "api_data": null, "hint": null}]}
```

## 💬 Response

Let me gather more specific data on the historical trajectory and monthly counts.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: WebFetch


```json
{
  "query": "Just Security litigation tracker cases filed per month 2025 monthly totals Trump executive actions"
}
```

### 📋 Result

```
{"query": "Just Security litigation tracker cases filed per month 2025 monthly totals Trump executive actions", "results": [{"title": "Trackers Archives - Just Security", "url":
"https://www.justsecurity.org/tag/trackers/", "snippet": "Trackers\n5 Articles\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background
as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges
to Trump Admin", "api_data": null, "hint": null}, {"title": "New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/", "snippet": "Today we are launching a major update to Just Security\u2019s [Litigation
Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/). We aim for this resource to be the most comprehensive public record of court challenges to
executive actions in the second Trump administration.\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format that allows users to follow both individual dockets
and monitor overall trends in near re", "api_data": null, "hint": null}, {"title": "Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to Trump administration executive
actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-protection#a3cfd7c6e3c9d6d0d7d0c6c0d6d1cad7da8dccd1c4). The Tracker
is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-
actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "Litigation Tracker Archives - Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet":
"Litigation Tracker\n16 Articles\n![Gavel and scales with a US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-
content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges to ",
"api_data": null, "hint": null}, {"title": "Executive Action Trackers | Kathrine R. Everett Law Library", "url": "https://library.law.unc.edu/2025/03/executive-action-trackers/", "snippet": "Executive
Action Trackers\nMarch 10, 2025\nWithin the first two months of his second term, President Donald Trump issued more than 75 executive orders. These executive orders range in topic, leaving many
lawyers and law students struggling to stay informed about evolving laws and the impact on their lives and areas of practice. A large number of these executive orders have already faced legal
challenges. As lawyers work to stay abreast of these executive actions, as well as legal challenges to the", "api_data": null, "hint": null}, {"title": "Courts & Litigation | Just Security", "url":
"https://www.justsecurity.org/category/courts-litigation/", "snippet": "Courts & Litigation\nJust Security\u2019s expert authors offer analysis and informational resources on key litigation impacting
national security, rights, democracy, and the rule of law. Our content spans domestic and international litigation, from cases at the International Court of Justice, the International Criminal Court,
and other international and regional tribunals, to those in U.S. courts involving executive branch actions, transnational litigation, and more.\nHighlights:\n![A bank with large Co", "api_data": null,
"hint": null}, {"title": "Litigation Trackers - Resources Addressing Trump Executive Orders - LibGuides at American University Washington College of Law", "url":
"https://wcl.american.libguides.com/c.php?g=1450141&p=10778608", "snippet": "[\nFederal Environmental Justice Tracker This link opens in a new window ](https://eelp.law.harvard.edu/tracker-
type/environmental-justice-tracker/)\nWe track regulations, policies, and other federal actions that affect communities' exposure to environmental pollution, including public health protections for
workers, pollution standards for air and water, and environmental enforcement priorities. We also track actions that affect the ability of impacted communities to participate in decisions that",
"api_data": null, "hint": null}, {"title": "Selective Coverage: Just Security\u2019s Litigation Tracker Omits Trump\u2011Filed Civil Suits - GLOBAL LAW TODAY", "url":
"https://www.globallawtoday.com/law/legal-news/2025/06/selective-coverage-just-securitys-litigation-tracker-omits-trump%E2%80%91filed-civil-suits/", "snippet": "Legal Technology | Transparency &
Accountability | Civil Procedure\nJust Security, a respected digital journal on law and policy, recently expanded its Litigation Tracker, now monitoring 271 active lawsuits challenging Trump
administration executive actions . But beneath its comprehensive fa\u00e7ade lies a crucial limitation\u2014cases in which the Trump administration sues as plaintiff are intentionally excluded.\nWhat
the Tracker Tracks\u2014and What It Doesn\u2019t\nThe Tracker focuses exclusively on plaintiffs su", "api_data": null, "hint": null}, {"title": "Survey of Sovereign Standing: Developments in State-Led
Lawsuits", "url": "https://www.justsecurity.org/131434/sovereign-standing-state-lawsuits-against-federal-government/", "snippet": "As state-led lawsuits against the federal government reach record
highs, pressure has mounted to use the standing doctrine to keep these state suits out of court. Scholars and attorneys for the federal government, from both the Trump and Biden administrations, have
argued for narrowing the pathways that allow states to assert their standing to sue. But the Supreme Court has so far declined to take that step. Meanwhile state plaintiffs are winning on the merits
of their claims, with courts granti", "api_data": null, "hint": null}, {"title": "Just Security Litigation Tracker - National Trans Bar Association", "url": "https://transbar.org/just-security-
litigation-tracker/", "snippet": "Just Security Litigation Tracker\n![](https://transbar.org/wp-content/uploads/2025/03/February-37.png)\nGiven light of the overwhelming and ever-changing legal
landscape, the NTBA wanted to share a public resource that tracks legal challenges to Trump administration actions.\nThis tracker is part of run by Just Security, which is an editorially independent,
non-partisan, daily digital law and policy journal that elevates the discourse on national security, democracy and the rule of law, and rights.", "api_data": null, "hint": null}, {"title": "2025
Donald J. Trump Executive Orders", "url": "https://www.federalregister.gov/presidential-documents/executive-orders/donald-trump/2025", "snippet": "Due to aggressive automated scraping of
FederalRegister.gov and eCFR.gov,\nprogrammatic access to these sites is limited to access to our extensive\ndeveloper APIs. Please visit\n[\nFederalRegister.gov
API\n](https://www.federalregister.gov/developers/documentation/api/v1)\ndocumentation or\n[\neCFR.gov API\n](https://www.ecfr.gov/developers/documentation/api/v1)\ndocumentation to learn more about
how to access the API.\nYour request has been flagged as potentially automated. If you are human user receivin", "api_data": null, "hint": null}, {"title": "Trump's 2025 Executive Orders | Holland &
Knight", "url": "https://www.hklaw.com/en/general-pages/trumps-2025-executive-orders-chart", "snippet": "|\nExecutive Order\n|\nDate Issued\n|\nPractice Area/Topic\n|\nShort/Executive
Summary\n|\n|\nAdvancing Regenerative Agriculture and Strengthening American Farm Resilience\n|\n6/25/2026\n|\n|\nThis [executive order](https://www.whitehouse.gov/presidential-
actions/2026/06/advancing-regenerative-agriculture-and-strengthening-american-farm-resilience/) promotes regenerative agriculture and farm modernization by increasing federal support for conservation-
focused farming practices, precision agriculture technologi", "api_data": null, "hint": null}, {"title": "Donald Trump's executive orders and actions, 2025-2026 - Ballotpedia", "url":
"https://ballotpedia.org/Donald_Trump's_executive_orders_and_actions,_2025", "snippet": "Donald Trump's executive orders and actions, 2025-2026\n[Donald Trump's executive orders and actions,
2025](https://ballotpedia.org/wiki/index.php?title=Donald_Trump%27s_executive_orders_and_actions,_2025&redirect=no))\n(second term)\n![]() |\n| Administration\n|\n| Transition\n|\n| First
term\n|\n(second term) |\n[Advancing Regenerative Agriculture and Strengthening American Farm
Resilience](https://ballotpedia.org/Executive_Order:_Advancing_Regenerative_Agriculture_and_Strengthening_American_Farm_Resilie", "api_data": null, "hint": null}, {"title": "Executive and Regulatory
Actions Under the Second Trump Administration | NAFSA", "url": "https://www.nafsa.org/executive-and-regulatory-actions-trump2admin", "snippet": "This NAFSA page links to select executive actions by
the President and administrative actions by federal agencies that relate to international education during the Trump-Vance administration (January 20, 2025 - January 20, 2029).\nQuick-links to content
organized by topic on this page. Jump to:\n[General](https://www.nafsa.org#general)[Government Funding, Staffing, and Operations](https://www.nafsa.org#funding)[DEI and Gender
Related](https://www.nafsa.org#dei)[Antisemitism Related](https://www.na", "api_data": null, "hint": null}, {"title": "Presidential Actions \u2013 The White House", "url":
"https://www.whitehouse.gov/presidential-actions/", "snippet": "Menu\nSearch\nSearch for:\nScroll Left\nNews\nGallery\nLivestream\nElection Integrity\nSAVE America\nTrump
Accounts\nInvestments\nContact\nNews\nContact\nElection Integrity\nSAVE America\nTrump Accounts\nGallery\nLivestream\nInvestments\nScroll Right\nClose\nNews\nFeatured\nReleases\nAliens\nLab Leak: The
True Origins of Covid-19\nJanuary 6: A Date Which Will Live in Infamy\nArrested: Worst of the Worst\nThis Is Our Why\nCriminal Aliens Receiving Medicaid\nThe JFK Files\nThe RFK Files\nBriefings &
Statements\nFact Sheets\nPreside", "api_data": null, "hint": null}, {"title": "Trump Administration Actions: Key Executive Orders and Policies", "url": "https://www.ncsl.org/in-dc/trump-
administration-actions-key-executive-orders-and-policies", "snippet": null, "api_data": null, "hint": null}, {"title": "Trump's 2025 Executive Orders: Updates and Summaries | Holland & Knight", "url":
"https://www.hklaw.com/en/general-pages/trumps-2025-executive-orders-updates-and-summaries", "snippet": "Trump's 2025 Executive Orders: Updates and Summaries\nPresident Donald J. Trump was sworn in as
the nation's 47th president on Jan. 20, 2025. On his first day back in office, President Trump began implementing many of his campaign promises, signing numerous executive orders targeting key areas
such as immigration, trade, energy and federal workforce policies.\nOur Public Policy & Regulation team members are actively monitoring and reviewing President Trump's executive orders and other
actions. Sum", "api_data": null, "hint": null}, {"title": "Project 2025 Executive Action Tracker - Center for Progressive Reform", "url": "https://progressivereform.org/tracking-
trump-2/project-2025-executive-action-tracker/", "snippet": "Updated February 2026: The Center for Progressive Reform and Governing for Impact are monitoring the Trump administration\u2019s
implementation of Project 2025, tracking the authoritarian blueprint\u2019s executive action proposals across 20 federal agencies.\nFebruary 2026 update: The Trump administration has initiated or
completed 53 percent of Project 2025\u2019s domestic administrative policy agenda in the 12 months following the president\u2019s inauguration. In all, 283 of the 532 recommended actions identifie",
"api_data": null, "hint": null}, {"title": "Trump\u2019s 2025 Executive Actions - Bloomberg Government", "url": "https://about.bgov.com/solutions/behind-every-policy-shift-is-an-
opportunity/trumps-2025-executive-actions/", "snippet": null, "api_data": null, "hint": null}, {"title": "List of executive orders in the second Trump presidency - Wikipedia", "url":
"https://en.wikipedia.org/wiki/List_of_executive_orders_in_the_second_Trump_presidency", "snippet": "As the 47th president of the United States, Donald Trump has relied extensively on executive
orders. In his first year of his second presidency he has signed 225 executive orders, surpassing the 220 orders of his entire first term. In the first 100 days of his presidency, Trump signed 143
executive orders, more than any other president had signed in their first 100 days in office. Franklin D. Roosevelt previously held the record, signing 99 executive orders in 1933. \nOn his first day
in office, ", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of executive orders in the second Trump presidency\", \"url\":
\"https://en.wikipedia.org/wiki/List_of_executive_orders_in_the_second_Trump_presidency\", \"extract\": \"As the 47th president of the United States, Donald Trump has relied extensively on executive
orders. In his first year of his second presidency he has signed 225 executive orders, surpassing the 220 orders of his entire first term. In the first 100 days of his presidency, Trump signed 143
executive orders, more than any other president had signed in their first 100 days in office. Franklin D. Roosevelt previously held the record, signing 99 executive orders in 1933. \\nOn his first day
in office, Trump issued 26 executive orders, the most of any president on their first day in office. The executive orders rescinded many of the previous administration's executive actions, began the
withdrawal process from the World Health Organization and Paris Agreement, rolled back federal recognition of gender identity, founded the Department of Government Efficiency, reaffirmed the existing
constitutional right to free speech, reversed the withdrawal of Cuba's designation as a state sponsor of terrorism, reversed sanctions on Israeli settlers, rolled back policy on artificial
intelligence, reversed the Family Reunification Task Force, pardoned over 1,500 January 6 rioters, designated Mexican drug cartels as foreign terrorist organizations, attempted to end birthright
citizenship for new children of illegal immigrants and immigrants legally but temporarily present in the U.S. (such as those on student, work, or tourist visas), delayed the government's ban of
TikTok, and declared a national emergency on the southern border, triggering the deployment of the U.S. military.\\nSeveral of Trump's orders have been considered to have ignored or violated federal
laws, regulations, and the Constitution. Some have been blocked in court for these reasons. Four days into his presidency, an analysis conducted by Time found that nearly two-thirds of his executive
actions \\\"mirror or partially mirror\\\" proposals from Project 2025, which was seconded by analysis from Bloomberg Government.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

```json
{
  "url": "https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/",
  "prompt": "What statistics does this article give about the total number of cases in the litigation tracker, cases filed per month, and monthly trends of legal challenges to Trump administration actions? Report specific numbers, dates, and monthly counts."
}
```

### 📋 Result

```
# Litigation Tracker Statistics

Based on the article provided, here are the specific numbers reported:

## Total Case Counts

The tracker documents **839 total cases** across all categories:
- **Plaintiff wins: 285** (including 71 permanently blocked, 143 temporarily blocked, 38 blocked pending appeal, and 33 closed in plaintiff's favor)
- **Government wins: 139** (including 62 temporary block denials, 46 not blocked pending appeal, and 31 closed in government's favor)
- **Pending cases: 414**
- **Other: 42** closed cases with mixed outcomes

## Key Finding

"When courts have ruled, the plaintiffs win about 60 percent of the time (a ratio of 119 wins by plaintiffs versus 79 wins by the government)."

## Important Limitation

**The article does not provide:**
- Monthly filing statistics
- Specific dates for case filings
- Monthly trend data
- Cases filed per month breakdowns

The piece presents a snapshot of overall litigation status and thematic breakdowns (immigration, civil liberties, structural disputes, etc.) but omits the temporal analysis you requested.
```

## 💬 Response

Let me look at the relaunch article and the historical data points from earlier in 2025 to build the trajectory.

## 🔧 Tool: WebFetch


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/",
  "prompt": "What was the total number of cases in the tracker when it relaunched? What date was this relaunch? Does it mention how cases have grown per month or over time since January 20, 2025? Report specific numbers and dates."
}
```

### 📋 Result

```
# Litigation Tracker Relaunch Details

**Relaunch Date:** August 6, 2025

**Total Cases:** The article does not specify the total number of cases in the tracker at the time of the relaunch.

**Growth Metrics:** The document does not provide specific numbers regarding how many cases have accumulated per month or overall growth trends since January 20, 2025.

The announcement focuses on describing new features—such as updated case status displays and advanced filtering capabilities—rather than reporting quantitative data about the litigation volume. The
authors note that the tracker "captures cases filed since Jan. 20, 2025" and emphasize their commitment to tracking developments through weekday updates, but no numerical case counts are disclosed in
this article.
```

```json
{
  "query": "Just Security litigation tracker \"cases\" Trump April 2025 186 OR 271 lawsuits number tracked"
}
```

### 📋 Result

```
{"query": "Just Security litigation tracker \"cases\" Trump April 2025 186 OR 271 lawsuits number tracked", "results": [{"title": "Litigation Tracker: Legal Challenges to Trump Administration
Actions", "url": "https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to Trump
administration executive actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-
protection#e8849c8da8829d9b9c9b8d8b9d9a819c91c6879a8f). The Tracker is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive
Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "Litigation Tracker Archives -
Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet": "Litigation Tracker\n16 Articles\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background
as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges
to ", "api_data": null, "hint": null}, {"title": "Trump Administration Litigation Tracker", "url": "https://www.lawfaremedia.org/projects-series/trials-of-the-trump-administration/tracking-trump-
administration-litigation", "snippet": null, "api_data": null, "hint": null}, {"title": "New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/", "snippet": "Today we are launching a major update to Just Security\u2019s [Litigation
Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/). We aim for this resource to be the most comprehensive public record of court challenges to
executive actions in the second Trump administration.\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format that allows users to follow both individual dockets
and monitor overall trends in near re", "api_data": null, "hint": null}, {"title": "Trackers Archives - Just Security", "url": "https://www.justsecurity.org/tag/trackers/", "snippet": "Trackers\n5
Articles\n![Gavel and scales with a US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-
content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges to Trump
Admin", "api_data": null, "hint": null}, {"title": "Collection: Just Security\u2019s Coverage of Trump Administration Executive Actions", "url": "https://www.justsecurity.org/106653/collection-trump-
administration-executive-actions/", "snippet": "On Jan. 20, President Donald Trump began his term with [presidential actions](https://www.whitehouse.gov/presidential-actions/) including 26 executive
orders, with more expected to follow. Just Security is covering key developments, including in concise \u201cWhat Just Happened\u201d expert explainers, legal and policy analysis, and
more.\nOriginally published Jan. 21, 2025, and frequently updated.\nTable of Contents\nA. Resources\nB. \u201cWhat Just Happened\u201d Series\nC. Analysis and Perspectives\nD. \u201cWhat Just Happ",
"api_data": null, "hint": null}, {"title": "Litigation Tracker - Just Security | The Democracy Habit", "url": "https://thedemocracyhabit.com/resources/reference/litigation-tracker-just-security",
"snippet": "JavaScript is required to access this website.\nPlease enable JavaScript and disable any ad blockers or browser extensions that may interfere.\nLoading\u2026\nPlease wait while we verify
you're not a bot\u2026", "api_data": null, "hint": null}, {"title": "Trump Lawsuit Tracker 2026: Cases Against & By Trump", "url": "https://lawhighlights.com/trump-lawsuit/", "snippet": "The term
\u201cTrump lawsuit\u201d in 2026 describes not one case but a sprawling legal environment involving over 750 active court battles. President Donald Trump is simultaneously a defendant in hundreds of
lawsuits challenging his executive orders, a plaintiff in multibillion-dollar claims against his own federal agencies, and a party to ongoing civil appeals that could cost him tens of millions of
dollars. As of April 2026, trackers maintained by Just Security and Lawfare count 753 cases challenging T", "api_data": null, "hint": null}, {"title": "Trump Lawsuits 2026, Every Major Case And What's
Happened", "url": "https://allaboutlawyer.com/trump-lawsuits/", "snippet": "Trump Lawsuits 2026, Every Major Case, What Happened, and Where Things Stand\nPrepared by the AllAboutLawyer.com Editorial
Team and reviewed for factual accuracy against Just Security\u2019s Litigation Tracker, Lawfare\u2019s Litigation Tracker, NBC News, CNN Politics, NPR, and court records on April 25, 2026. Last
Updated: April 25, 2026\nIf you have been trying to keep track of the lawsuits surrounding Donald Trump, you are not alone. The numbers are staggering, the categories are different, and the outco",
"api_data": null, "hint": null}, {"title": "Courts & Litigation | Just Security", "url": "https://www.justsecurity.org/category/courts-litigation/", "snippet": "Courts & Litigation\nJust
Security\u2019s expert authors offer analysis and informational resources on key litigation impacting national security, rights, democracy, and the rule of law. Our content spans domestic and
international litigation, from cases at the International Court of Justice, the International Criminal Court, and other international and regional tribunals, to those in U.S. courts involving
executive branch actions, transnational litigation, and more.\nHighlights:\n![A bank with large Co", "api_data": null, "hint": null}]}
```

## 💬 Response

I have gathered strong data. Let me get a few more historical data points to build the trajectory, particularly the earlier 2025 figures.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: WebFetch


```json
{
  "query": "Just Security litigation tracker Trump 300 OR 400 OR 500 OR 600 cases lawsuits December 2025 total challenges"
}
```

### 📋 Result

```
{"query": "Just Security litigation tracker Trump 300 OR 400 OR 500 OR 600 cases lawsuits December 2025 total challenges", "results": [{"title": "Litigation Tracker: Legal Challenges to Trump
Administration Actions", "url": "https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to
Trump administration executive actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-
protection#630f1706230916101710060016110a171a4d0c1104). The Tracker is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive
Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "Litigation Tracker Archives -
Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet": "Litigation Tracker\n16 Articles\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background
as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges
to ", "api_data": null, "hint": null}, {"title": "Trackers Archives - Just Security", "url": "https://www.justsecurity.org/tag/trackers/", "snippet": "Trackers\n5 Articles\n![Gavel and scales with a
US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and
scales with a US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-
content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges to Trump Admin", "api_data": null, "hint": null}, {"title": "New and
Improved Litigation Tracker: Legal Challenges to Trump Administration Actions", "url": "https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/", "snippet": "Today we are launching a
major update to Just Security\u2019s [Litigation Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/). We aim for this resource to be the most
comprehensive public record of court challenges to executive actions in the second Trump administration.\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format
that allows users to follow both individual dockets and monitor overall trends in near re", "api_data": null, "hint": null}, {"title": "Trump Administration Litigation Tracker", "url":
"https://www.lawfaremedia.org/projects-series/trials-of-the-trump-administration/tracking-trump-administration-litigation", "snippet": null, "api_data": null, "hint": null}, {"title": "Litigation
Tracker: Pending Criminal and Civil Cases Against Donald Trump", "url": "https://www.justsecurity.org/75032/litigation-tracker-pending-criminal-and-civil-cases-against-donald-trump/", "snippet":
"Originally published on Feb. 28, 2021; continually updated.\nOn both the criminal and civil litigation fronts, former President Donald Trump faces a bevy of lawsuits and investigations, with more
cases likely to follow. Some are civil suits stemming from his pre-presidential business dealings. Others are defamation claims from women he allegedly assaulted. More still are criminal probes and
civil actions that scrutinize his attempts to overturn the results of the 2020 election. The Chart below tr", "api_data": null, "hint": null}, {"title": "Dissecting the Litigation: Where Trump
Administration Actions Face Early Roadblocks or Traction", "url": "https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/", "snippet": "Last week we
[relaunched](https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/) Just Security\u2019s [Litigation Tracker: Legal Challenges to Trump Administration
Actions](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/) with new features and stats. The infographics below provide a snapshot of what we are seeing,
i.e. where litigation stands and how courts are ruling on challenges to the administration\u2019s executive actions.\nThe Snapshot\nT", "api_data": null, "hint": null}, {"title": "Executive Action
Trackers | Kathrine R. Everett Law Library", "url": "https://library.law.unc.edu/2025/03/executive-action-trackers/", "snippet": "Executive Action Trackers\nMarch 10, 2025\nWithin the first two months
of his second term, President Donald Trump issued more than 75 executive orders. These executive orders range in topic, leaving many lawyers and law students struggling to stay informed about evolving
laws and the impact on their lives and areas of practice. A large number of these executive orders have already faced legal challenges. As lawyers work to stay abreast of these executive actions, as
well as legal challenges to the", "api_data": null, "hint": null}, {"title": "Executive Order Trackers - Executive Materials - Research Guides at UC Davis Mabie Law Library", "url":
"https://libguides.law.ucdavis.edu/c.php?g=1455012&p=10816869", "snippet": "Reference librarians can help you locate resources, develop search strategies, and navigate the research process.\nThe
Federal Register is the official journal of the federal government of the United States that contains government agency rules, proposed rules, and public notices. It is published every weekday, except
on federal holidays. It is also the source for executive orders, proclamations, and other executive documents.", "api_data": null, "hint": null}, {"title": "Courts & Litigation | Just Security",
"url": "https://www.justsecurity.org/category/courts-litigation/", "snippet": "Courts & Litigation\nJust Security\u2019s expert authors offer analysis and informational resources on key litigation
impacting national security, rights, democracy, and the rule of law. Our content spans domestic and international litigation, from cases at the International Court of Justice, the International
Criminal Court, and other international and regional tribunals, to those in U.S. courts involving executive branch actions, transnational litigation, and more.\nHighlights:\n![A bank with large Co",
"api_data": null, "hint": null}]}
```

```json
{
  "url": "https://factually.co/fact-checks/politics/current-lawsuits-against-donald-trump-2025-27726a",
  "prompt": "What specific numbers does this give for the number of lawsuits/legal challenges against the Trump administration on the Just Security litigation tracker at various points in 2025 (e.g., April 2025, later in 2025, December 2025)? Report specific counts with dates."
}
```

### 📋 Result

```
Request failed with status code 403
```

## 💬 Response

Let me get the Fulcrum article data and the factually.co historical data which cited specific numbers.

## 🔧 Tool: WebFetch


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://thefulcrum.us/rule-of-law/trump-lawsuits-2025",
  "prompt": "What specific numbers does this article cite for the number of legal challenges/lawsuits against the Trump administration on the Just Security litigation tracker at various dates in 2025? Report all specific counts with their dates (e.g. February, April, later 2025)."
}
```

### 📋 Result

```
I cannot find specific numbers or dates for legal challenges against the Trump administration cited in this article content. While the page is titled "Courts' Actions Against the Trump Administration"
and contains metadata indicating it was published/modified on April 22, 2025, the actual article text with litigation statistics is not included in the provided content.

The material shown consists primarily of website code, styling information, and structural elements rather than the substantive article content that would contain the lawsuit counts you're asking
about.
```

```json
{
  "query": "Just Security litigation tracker Trump lawsuits count \"as of\" 2025 hundreds cases February March April June"
}
```

### 📋 Result

```
{"query": "Just Security litigation tracker Trump lawsuits count \"as of\" 2025 hundreds cases February March April June", "results": [{"title": "Litigation Tracker: Legal Challenges to Trump
Administration Actions", "url": "https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "This living, searchable resource tracks legal challenges to
Trump administration executive actions. If you think we are missing anything, you can email us at [[email protected]](https://www.justsecurity.org/cdn-cgi/l/email-
protection#9cf0e8f9dcf6e9efe8eff9ffe9eef5e8e5b2f3eefb). The Tracker is part of Just Security\u2019s [Collection: Coverage of the Trump Administration\u2019s Executive
Actions](https://www.justsecurity.org/106653/collection-trump-administration-executive-actions/).\nFor important litigati", "api_data": null, "hint": null}, {"title": "Litigation Tracker Archives -
Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet": "Litigation Tracker\n16 Articles\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background
as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges
to ", "api_data": null, "hint": null}, {"title": "Trump Administration Litigation Tracker", "url": "https://www.lawfaremedia.org/projects-series/trials-of-the-trump-administration/tracking-trump-
administration-litigation", "snippet": null, "api_data": null, "hint": null}, {"title": "New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/", "snippet": "Today we are launching a major update to Just Security\u2019s [Litigation
Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/). We aim for this resource to be the most comprehensive public record of court challenges to
executive actions in the second Trump administration.\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format that allows users to follow both individual dockets
and monitor overall trends in near re", "api_data": null, "hint": null}, {"title": "Trackers Archives - Just Security", "url": "https://www.justsecurity.org/tag/trackers/", "snippet": "Trackers\n5
Articles\n![Gavel and scales with a US flag in the background as symbols of a jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-
content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n![Gavel and scales with a US flag in the background as symbols of a
jurisdiction.](https://i0.wp.com/www.justsecurity.org/wp-content/uploads/2025/01/GettyImages-14867850291-e1738614282494.jpg?fit=1024%2C434&ssl=1)\n[Litigation Tracker: Legal Challenges to Trump
Admin", "api_data": null, "hint": null}, {"title": "Collection: Just Security\u2019s Coverage of Trump Administration Executive Actions", "url": "https://www.justsecurity.org/106653/collection-trump-
administration-executive-actions/", "snippet": "On Jan. 20, President Donald Trump began his term with [presidential actions](https://www.whitehouse.gov/presidential-actions/) including 26 executive
orders, with more expected to follow. Just Security is covering key developments, including in concise \u201cWhat Just Happened\u201d expert explainers, legal and policy analysis, and
more.\nOriginally published Jan. 21, 2025, and frequently updated.\nTable of Contents\nA. Resources\nB. \u201cWhat Just Happened\u201d Series\nC. Analysis and Perspectives\nD. \u201cWhat Just Happ",
"api_data": null, "hint": null}, {"title": "Trump Lawsuits 2026, Every Major Case And What's Happened", "url": "https://allaboutlawyer.com/trump-lawsuits/", "snippet": "Trump Lawsuits 2026, Every
Major Case, What Happened, and Where Things Stand\nPrepared by the AllAboutLawyer.com Editorial Team and reviewed for factual accuracy against Just Security\u2019s Litigation Tracker, Lawfare\u2019s
Litigation Tracker, NBC News, CNN Politics, NPR, and court records on April 25, 2026. Last Updated: April 25, 2026\nIf you have been trying to keep track of the lawsuits surrounding Donald Trump, you
are not alone. The numbers are staggering, the categories are different, and the outco", "api_data": null, "hint": null}, {"title": "Selective Coverage: Just Security\u2019s Litigation Tracker Omits
Trump\u2011Filed Civil Suits - GLOBAL LAW TODAY", "url": "https://www.globallawtoday.com/law/legal-news/2025/06/selective-coverage-just-securitys-litigation-tracker-omits-trump%E2%80%91filed-civil-
suits/", "snippet": "Legal Technology | Transparency & Accountability | Civil Procedure\nJust Security, a respected digital journal on law and policy, recently expanded its Litigation Tracker, now
monitoring 271 active lawsuits challenging Trump administration executive actions . But beneath its comprehensive fa\u00e7ade lies a crucial limitation\u2014cases in which the Trump administration
sues as plaintiff are intentionally excluded.\nWhat the Tracker Tracks\u2014and What It Doesn\u2019t\nThe Tracker focuses exclusively on plaintiffs su", "api_data": null, "hint": null}, {"title":
"TRUMP LAWSUITS - Comprehensive Tracker", "url": "https://trumplawsuits.com/", "snippet": "$88.3M judgments \u2022 34 felony convictions \u2022 $45B+ in active claims \u2022\n328+ admin cases \u2022
30+ total tracked cases\nTrump Defendant - Criminal\n[People of NY v. Trump](https://www.newsweek.com/trump-appeals-stormy-daniels-hush-money-conviction-2022997)\nCONVICTED: 34 felony
counts\nfalsifying business records (Stormy Daniels hush money)\nCONVICTEDAPPEAL ACTIVEUnconditional discharge 1/10/25; Sullivan & Cromwell appealing \u2022\nNY Supreme Court\n[United States v. Trump
(Jan 6)](https://www.justice.gov/storage/", "api_data": null, "hint": null}]}
```

## 💬 Response

I now have solid data points. Let me consolidate. I have: ~271 (June 2025), 839 (Aug 2025 relaunch snapshot), 753 (April 2026 cited by secondary sources), and 900 (July 16, 2026 — current). Let me get one more confirmation on the current figure and any early-2025 data points.

## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "Just Security litigation tracker Trump administration cases count 2026 total challenges",
  "num_results": 8
}
```

### 📋 Result

```
[{"title": "Litigation Tracker: Legal Challenges to Trump ...", "url": "https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/", "snippet": "Litigation Tracker:
Legal Challenges to Trump Administration Actions\n\nJust Security \u2013 JustSecurity.org\n\nJust Security Logo in opposite color link to homepage\n\nSubstack icon opens the Just Security pageFollow
us on BlueSky\n\nBluesky icon opens the Just Security pageFollow us on BlueSky\n\nLinkedin icon opens the Just Security pageFollow us on Linkedin\n\nX (Twitter) icon opens the Just Security pageFollow
us on Twitter X\n\nThreads icon opens the Just Security pageFollow us on Threads\n\nFacebook icon ope", "highlights": ["This living, searchable resource tracks legal challenges to Trump administration
executive actions. If you think we are missing anything, you can email us at [email protected]. The Tracker is part of Just Security\u2019s Collection: Coverage of the Trump Administration\u2019s
Executive Actions.\n...\nTotal number of cases currently tracked: 900.\n...\n+Tracker Totals: Overall Case Status Snapshot\n...\nGovernment Action Blocked: 71Government Action Temporarily Blocked:
143Government Action Blocked Pending Appeal: 38Case Closed in Favor of Plaintiff: 33Total Plaintiff Wins: 285Temporary Block of Government Action Denied: 62Government Action Not Blocked (Pending
Appeal): 46Case Closed/Dismissed in Favor of Government: 31Total Government Wins: 139Case Pending: 414Government Action Temporarily Blocked in Part; Temporary Block Denied in Part: 20Case Closed:
42"], "published_date": "2026-07-16T12:00:19.000", "score": null}, {"title": "New and Improved Litigation Tracker: Legal Challenges to ...", "url": "https://www.justsecurity.org/118505/relaunch-trump-
litigation-tracker/", "snippet": "New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions\n\nJust Security \u2013 JustSecurity.org\n\n\u00d7\n\n\u00d7\n\nPowered by
Algolia\n\n# New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions\n\nBy\n\nand\n\nToday we are launching a major update to Just Security\u2019s Litigation Tracker. We
aim for this resource to be the most comprehensive public record of court challenges to executive actions in the second Trump administration.\n\nThe tracker now captures cases f", "highlights": ["New
and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions\n\nJust Security \u2013 JustSecurity.org\n\n\u00d7\n\n\u00d7\n\nPowered by Algolia\n\n# New and Improved Litigation
Tracker: Legal Challenges to Trump Administration Actions\n\nBy\n\nand\n\nToday we are launching a major update to Just Security\u2019s Litigation Tracker. We aim for this resource to be the most
comprehensive public record of court challenges to executive actions in the second Trump administration.\n\nThe tracker now captures cases filed since Jan. 20, 2025 and presents each case in a format
that allows users to follow both individual dockets and monitor overall trends in near real time.\n\nWhat\u2019s New\n\nThe tracker now allows users to see constantly updated totals of the status of
cases (e.g. \u201cBlocked,\u201d \u201cOn Appeal,\u201d \u201cAwaiting Court Ruling\u201d). It also offers advanced filters that allow users to sort by each case\u2019s listed status.\n\nAs the
litigation proceeds apace, these tools should make it easier to surface emerging litigation patterns and to test assumptions about where \u2013 and how \u2013 courts are placing limits on assertions
of executive power.\n\nStay Informed with Daily Updates\n\nEvery weekday our team screens new lawsuits challenging executive actions and catalogs substantive changes in ongoing cases that we are
already tracking (such as a new court order). You can find a concise digest of these developments every afternoon in our \u201c Today on Just Security\u201d newsletter.\n\nEngage\n\nPlease feel free
to let us know if you think we\u2019re missing anything by dropping us an email at [email protected].\n\nIf you would like to help support our efforts, we appreciate donations of any amount as it
takes a village to produce this work.\n\nWith many thanks to readers for all the engagement and appreciation we have already received.\n\nFEATURED IMAGE: selective focus on gavel hammer on wooden
table top with copy space\n\n### Share\n\n### Filed Under\n\nLitigation, Litigation Tracker\n\n### About the Authors\n\nSend A Letter To The Editor\n\n## Read Next:\n\n## Featured Articles:\n\n###
Will Trump Take the Win at NATO\u2019s Ankara Summit?\n\n### As American as International Law\n\n### Beyond the Battlefield: Governing Civilian AI in Post-Conflict Settings\n\n### A New Security Order
for the Middle East Must Address the Growing Saudi-UAE Rift\n\nDON'T MISS A THING. Stay up to date with Just Security curated newsletters:\n\nEarly Edition\n\nToday on Just Security\n\nFirst Name:
Last Name: Email address: Subscribe\n\nLeave this field empty if you're human:"], "published_date": "2025-08-06T12:34:46.000", "score": null}, {"title": "Where Trump Administration Actions Face Early
Roadblocks or Traction", "url": "https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/", "snippet": "Where Trump Administration Actions Face Early Roadblocks or Traction
\n\nJust Security \u2013 JustSecurity.org\n\n \n\n \n\n \n\n \u00d7\n\n\u00d7\n\nPowered by Algolia\n\n \n\n# Dissecting the Litigation: Where Trump Administration Actions Face Early Roadblocks or
Traction\n\nBy\n\nand\n\nLast week we relaunched Just Security\u2019s Litigation Tracker: Legal Challenges to Trump Administration Actions with new features and stats. The infographics below provide a
snapshot of what we are seeing, i.e. where litigation stands and how courts a", "highlights": ["Last week we relaunched Just Security\u2019s Litigation Tracker: Legal Challenges to Trump
Administration Actions with new features and stats. The infographics below provide a snapshot of what we are seeing, i.e. where litigation stands and how courts are ruling on challenges to the
administration\u2019s executive actions.\n...\nThe vast majority\n...\nimmigration and civil liberties, where\n...\n. But the flipside\n...\nCase Status Summary Government Action Blocked: 59Government
Action Temporarily Blocked: 132Government Action Blocked Pending Appeal: 35Case Closed in Favor of Plaintiff: 12Total Plaintiff Wins: 238Temporary Block of Government Action Denied: 46Government
Action Not Blocked Pending Appeal: 41Case Closed/Dismissed in Favor of Government: 30Total Government Wins: 117Awaiting Court Ruling: 322Government Action Temporarily Blocked in Part; Temporary Block
Denied in Part: 17Case Closed: 36"], "published_date": "2025-08-14T14:49:52.000", "score": null}, {"title": "Litigation Tracker: Legal Challenges to Trump Administration Actions", "url":
"https://myattorneyusa.com/wp-content/uploads/2026/02/legal-challenges-to-trump-administration-actions.pdf", "snippet": "Just Security - JustSecurity.org\n\n## Litigation Tracker: Legal Challenges to
Trump Administration Actions\n\nBy Just Security Published on February 10, 2026 share y X in @ f \u00a7 #\n\nThis living, searchable resource tracks legal challenges to Trump administration executive
actions. If you think we are missing anything, you can email us at lte@justsecurity.org. The Tracker is part of the Collection: Just Security's Coverage of the Trump Administration's Executive
Actions.\n\nFor important litigation upda", "highlights": ["## Litigation Tracker: Legal Challenges to Trump Administration Actions\n...\nThis living, searchable resource tracks legal challenges to
Trump administration executive actions. If you think we are missing anything, you can email us at lte@justsecurity.org. The Tracker is part of the Collection: Just Security's Coverage of the Trump
Administration's Executive Actions.\n...\nTotal number of cases currently tracked: 627.\n...\nTracker Totals: Overall Case Status Snapshot"], "published_date": null, "score": null}, {"title": "262
Court Losses. 753 Lawsuits. The Courts Are Saying the Same Three Things. | Resist Now", "url": "https://resistnow.net/briefs/courts-blocking-analysis/", "snippet": "262 Court Losses. 753 Lawsuits. The
Courts Are Saying the Same Three Things. | Resist Now\n\n# 262 Court Losses. 753 Lawsuits. The Courts Are Saying the Same Three Things.\n\nMay 15, 2026 4 min read\n\n## The numbers\n\nAs of May 2026,
753 lawsuits have been filed against the Trump administration. That averages more than two new cases per day since January 2025.\n\nOf the cases with rulings, the Just Security tracker counts 262
plaintiff wins and 126 government wins. Another 360 cases are still awaiting d", "highlights": ["262 Court Losses. 753 Lawsuits. The Courts Are Saying the Same Three Things. | Resist Now\n\n# 262
Court Losses. 753 Lawsuits. The Courts Are Saying the Same Three Things.\n\nMay 15, 2026 4 min read\n\n## The numbers\n\nAs of May 2026, 753 lawsuits have been filed against the Trump administration.
That averages more than two new cases per day since January 2025.\n\nOf the cases with rulings, the Just Security tracker counts 262 plaintiff wins and 126 government wins. Another 360 cases are still
awaiting decisions. The administration wins about 33% of decided cases.\n\n\u201cAgencies may not conduct large-scale reorganizations and reductions in force in blatant disregard of Congress\u2019s
mandates.\u201d\n\nJudge Susan Illston, U.S. District Court, Northern District of California\n\n## Win rate by area\n\nWhere courts block the most and where the administration has had more
success.\n\n| Policy area | Plaintiff wins | Gov wins | Win rate for admin |\n| --- | --- | --- | --- |\n| Immigration | 100+ | ~30 | ~23% |\n| Federal workforce / DOGE | 40+ | ~15 | ~27% |\n|
Education / DEI | 25+ | ~10 | ~29% |\n| Healthcare / research | 20+ | ~8 | ~29% |\n| Voting / elections | 15+ | ~5 | ~25% |\n| Foreign aid / spending | 10+ | ~15 | ~60% |\n| Energy / environment | 10+
| ~5 | ~33% |\n\nThe administration wins most often on foreign aid and spending cases, where courts are more deferential to executive authority over international affairs. It loses most on immigration
and voting, where constitutional protections are strongest.\n\n## What the courts keep saying\n\nThree themes run through hundreds of rulings:\n\n1. Congress decides how money is spent. Courts block
when the administration freezes funds Congress appropriated, redirects spending without authorization, or eliminates programs that Congress created by statute. The NIH funding fight and the foreign
aid freeze both turned on this principle.\n\n2. You cannot fire civil servants for political reasons. The mass firing of probationary employees and DOGE-driven reorganizations both violated civil
service law. Judge Alsup ordered rehiring at six agencies. A 143-page DOGE ruling found First Amendment violations and no legal authority for DOGE officials to touch NEH grants.\n\n3. Executive orders
cannot override the Constitution. Birthright citizenship and mandatory detention both ran into constitutional limits. 225 judges have ruled the mandatory detention policy likely violates due
process.\n\n## The Supreme Court factor\n\nThe Supreme Court is the escape valve. When lower courts block a policy, the administration appeals to the emergency docket, the busiest in modern
history.\n\n| Supreme Court action | Outcome |\n| --- | --- |\n| Limited universal injunctions | Narrowed scope but judges found workarounds via class actions |\n| Transgender military ban | Lifted
injunctions, administration wins |\n| DOGE reorganization stay | Paused injunction, administration proceeds |\n| NIH indirect cost cap | Block upheld on appeal, plaintiffs win |\n| Birthright
citizenship | Core block held; cert granted Dec 2025, oral arguments expected before July 2026 |\n| Foreign aid freeze | D.C. Circuit reversed; SCOTUS allowed withholding |\n\nThe pattern: lower
courts block, the Supreme Court sometimes narrows or lifts the block, but rarely endorses the underlying policy on the merits. Most stays are procedural, not substantive wins.\n\n## Who is
filing\n\nDemocratic state attorneys general account for 55 of 67 cases with rulings in their favor. Arizona AG Kris Mayes alone has filed 41 lawsuits. If the 2026 AG races flip key states, the
litigation coalition loses its anchor.\n\nThe ACLU and NAACP Legal Defense Fund are leading the nonprofit litigation. Universities filed the NIH cases. Individual plaintiffs brought many of the DOGE
employment cases.\n\n## What you can do\n\n1. Track the cases. Just Security and Lawfare maintain live trackers updated weekly.\n2. Support your AG. State attorneys general lead the largest share of
these cases. Check the AG lawsuit results to see if your state is fighting.\n3. Watch the Supreme Court. Birthright citizenship arguments are expected before July 2026. That ruling will define
executive power for a generation.\n4. Contact your senators through Resist Bot to demand congressional oversight of executive orders that courts keep blocking.\n\nThis brief is part of our Rule of Law
coverage. See also: AG Lawsuit Results and Project 2025 Status.\n\n## Sources (6)\n\nCopy link"], "published_date": "2026-05-15T00:00:00.000", "score": null}, {"title": "Litigation Tracker Archives -
Just Security", "url": "https://www.justsecurity.org/tag/litigation-tracker/", "snippet": "Litigation Tracker Archives - Just Security\n\nJust Security \u2013
JustSecurity.org\n\n\u00d7\n\n\u00d7\n\nFilters\n\nSort by: Newest to OldestOldest to NewestAlphabetical A-ZAlphabetical Z-A\n\n16 Articles\n\nSelect Tags:2020 presidential election2024 US Election
Protection2024 Presidential ElectionAdministrationAdministrative LawAl Hela v. BidenArizonaArticle IIIasylumBiden administrationborder wallBorderscitizenshipCivil LibertiesConstitutioncontent
moderationcourtsdeath penaltyDemocracyDepartment of Homeland Security (", "highlights": ["Litigation Tracker Archives - Just Security\n\nJust Security \u2013
JustSecurity.org\n\n\u00d7\n\n\u00d7\n\nFilters\n\nSort by: Newest to OldestOldest to NewestAlphabetical A-ZAlphabetical Z-A\n\n16 Articles\n\nSelect Tags:2020 presidential election2024 US Election
Protection2024 Presidential ElectionAdministrationAdministrative LawAl Hela v. BidenArizonaArticle IIIasylumBiden administrationborder wallBorderscitizenshipCivil LibertiesConstitutioncontent
moderationcourtsdeath penaltyDemocracyDepartment of Homeland Security (DHS)Department of StateDetentionDomestic ExtremismDonald Trumpelection interferenceelection lawelectionsEmergency Powersexecutive
branchExecutive OrdersFederal Communications Commission (FCC)Federal CourtsfederalismForeign Aid/Foreign AssistanceFox NewsFreedom of Information Act (FOIA)freedom of speechGeorgia (U.S.
State)governanceGuantanamoImmigrationImmigration and Customs Enforcement (ICE)immigration detentionImmunityimmunity for official actsJanuary 6th Attack on US CapitolKu Klux Klan
ActLitigationNevadanews mediaPennsylvaniaRefugeesRule of LawSocial Media PlatformsstandingSupreme Court (SCOTUS)TikTokTrackersTransparencyTrump administration first termTrump administration second
termTrump CampaignTrump FoundationUniform Code of Military JusticeUnited States (US)US Militaryvoting rightsWhen Guardrails Erode: An Anti\u2011Corruption SeriesWisconsin\n\nSelect Authors:Aadhithi
PadmanabhanAdam KlasfeldAmanda TeuscherBethany Davis NollClare BooneDani SchulkinHarrison BlankIva PetkovaJacob ApkonJoyce VanceJust SecurityJustin ColeKarl MihmMadison GeeMargaret ShieldsMari
DugasNicholas TonckensNorman L. EisenRyan GoodmanSamara AngelSofia DeSimoneSruthi VenkatachalamTess Bridgeman\n\nSelect Date Range:\n\nFilter Results\n\n## Litigation Tracker: Legal Challenges to
Trump Administration Actions\n\nA public resource tracking all the legal challenges to the Trump administration's executive orders and actions.\n\n## A Survey of Sovereign Standing: Developments in
State-Led Lawsuits Against the Federal Government\n\nRecent state-led cases against the federal government demonstrate the range of injuries that states are successfully asserting under the current
doctrines of state standing.\n\n## Dissecting the Litigation: Where Trump Administration Actions Face Early Roadblocks or Traction\n\nA snapshot of where litigation stands and how courts are ruling on
challenges to the Trump administration's executive actions.\n\n## New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions\n\nAnnouncing the increased functionality of the
Litigation Tracker, which monitors all lawsuits against Trump administration executive actions.\n\n## The Freedom of Information Act and Deteriorating Federal Transparency Infrastructure\n\nWeakening
FOIA does not merely impair public knowledge \u2014 it also reduces the likelihood that abuses will be detected and deterred.\n\n## The Fox TV Problem with Deporting International Students\n\nThe
SCOTUS decision in FCC v. Fox TV emphasized fair notice, a bedrock requirement of due process that could shield students from removal.\n\n## Election 2024 Real-Time Litigation Tracker\n\nTracking the
most important breaking election cases across the country with implications for the democratic process.\n\n## Top 10 Election Litigation Cases in 2024 Implicating the Rule of Law\n\nIn this top ten
list updated weekly, the most important of hundreds of election-law cases are ranked for their rule of law implications.\n\n## Top 10 Election Litigation Cases in 2024 Implicating the Rule of
Law\n\nIn this top ten list updated weekly, the most important of hundreds of election-law cases are ranked for their rule of law implications.\n\n## Top 10 Election Litigation Cases in 2024
Implicating the Rule of Law\n\nIn this top ten list updated weekly, the most important of hundreds of election-law cases are ranked for their rule of law implications.\n\n## Top 10 Election Litigation
Cases in 2024 Implicating the Rule of Law\n\nIn this top ten list updated weekly, the most important of hundreds of election-law cases are ranked for their rule of law implications.\n\n## Top 10
Election Litigation Cases in 2024 Implicating the Rule of Law\n\nA new, regularly updated tracker for the 2024 election.\n\n1-12 of 16 items\n\n## Explore:\n\n### Executive Branch\n\n### International
Law\n\n### Democracy & Rule of Law\n\nDON'T MISS A THING. Stay up to date with Just Security curated newsletters:\n\nEarly Edition\n\nToday on Just Security\n\nFirst Name: Last Name: Email address:
Subscribe\n\nLeave this field empty if you're human:\n\n\u00d7"], "published_date": null, "score": null}, {"title": "Tracking the Lawsuits Against the Trump Administration: Immigration, Tariffs and
More - The New York Times", "url": "https://www.nytimes.com/interactive/2026/us/trump-administration-lawsuits.html", "snippet": "The Trump administration\u2019s sweeping policy changes face a number
of lawsuits \u2014 more than 800.\n...\nIn more than 450 cases, the courts have let the administration\u2019s policies stay in effect even as they remain in active litigation. In more than 150 cases,
however, the courts have at least partially halted the administration\u2019s policies either through temporary restraining orders or preliminary injunctions.\n...\nHere is a snapshot of where the
lawsuits against President Trump stand, highlighting distr", "highlights": ["The Trump administration\u2019s sweeping policy changes face a number of lawsuits \u2014 more than 800.\n...\nIn more than
450 cases, the courts have let the administration\u2019s policies stay in effect even as they remain in active litigation. In more than 150 cases, however, the courts have at least partially halted
the administration\u2019s policies either through temporary restraining orders or preliminary injunctions.\n...\nHere is a snapshot of where the lawsuits against President Trump stand, highlighting
district court cases where a judge has entered a final order for or against the administration. Many of those cases have been appealed.\n...\n| Active | 481 |\n| --- | --- |\n| Active, policy halted |
165 |\n| Cases with a final decision | 175 |\n...\nThe Supreme Court has also taken action in 31 cases. Six cases are pending action by the court.\n...\nAbout the data\n...\nThe New York Times is
tracking cases filed against Mr. Trump or his administration since the start of his second term on Jan. 20, 2025. The"], "published_date": "2025-02-12T21:17:54.000", "score": null}, {"title": "Trump
Lawsuits 2026, Every Major Case And What's Happened", "url": "https://allaboutlawyer.com/trump-lawsuits/", "snippet": "Trump Lawsuits 2026, Every Major Case And What's Happened\n\nPrepared by the
AllAboutLawyer.com Editorial Team and reviewed for factual accuracy against Just Security\u2019s Litigation Tracker, Lawfare\u2019s Litigation Tracker, NBC News, CNN Politics, NPR, and court records
on April 25, 2026. Last Updated: April 25, 2026\n\nIf you have been trying to keep track of the lawsuits surrounding Donald Trump, you are not alone. The numbers are staggering, the categories are
different, and the outcomes swing in ever", "highlights": ["As of April 9, 2026, Just Security\u2019s litigation tracker counts 753 cases challenging Trump administration actions. Lawfare\u2019s
tracker counts 316 \u201cactive cases,\u201d treating a district court case and its appeals as a single matter. The New York Times tracker reports over 700 total cases filed against the administration
since January 2025.\n...\nThose numbers measure only lawsuits against the Trump administration. They do not count Trump\u2019s personal civil litigation. Add the E. Jean Carroll cases, the New York
fraud appeal, and the roughly 30 lawsuits Trump has filed as plaintiff, and the total easily exceeds 800 active legal matters involving Trump or his administration.\n...\nAs of the latest count, there
are 316 active cases challenging Trump administration actions, 22 suits by the Trump administration challenging state or local laws, 17 Supreme Court stays or orders to vacate lower court orders, and
10 suits where judges ruled against the federal government in a summary judgment or permanent injunction.\n...\n- Quick Reference: Major Trump Lawsuits at a Glance\n- Just Security\u2019s tracker
(justsecurity.org) covers all policy and executive order challenges \u2014 753 cases and counting.\n- Lawfare\u2019s tracker (lawfaremedia.org) tracks 316 active cases with detailed summaries.\n-
PACER (pacer.gov) gives you access to actual court filings for any federal case.\n- AllAboutLawyer.com will update its coverage as major rulings land \u2014 including the May 27 IRS lawsuit hearing,
the Supreme Court\u2019s decision on the Carroll $5 million petition, and the New York Court of Appeals ruling on the fraud finding.\n...\n| Case | Type | Current Status |\n| --- | --- | --- |\n| E.
Jean Carroll \u2014 Carroll I | Personal defamation | $83.3M judgment upheld on appeal (Sept. 2025); Supreme Court petition possible |\n| E. Jean Carroll \u2014 Carroll II | Personal sexual abuse +
defamation | $5M judgment upheld; Supreme Court petition filed; no decision yet |\n| New York Civil Fraud (AG James) | Personal fraud | Fraud finding upheld; $500M+ penalty voided; now at NY Court of
Appeals |\n| Trump v. IRS / Treasury | Trump is plaintiff; $10B sought | Judge questioning jurisdiction; hearing May 27, 2026 |\n| Trump v. Wall Street Journal | Trump is plaintiff; defamation |
Dismissed April 2026 |\n| Trump v. ABC News | Trump is plaintiff; defamation | Settled December 2024; ABC paid $16M to Trump\u2019s library and legal fees |\n| Policy / executive order challenges |
Administration lawsuits | 753 cases active as of April 2026 |\n| Federal criminal cases (Smith) | Criminal | Both dropped November 2024 after Trump\u2019s election win |\n| NY hush money criminal case
| Criminal | Guilty verdict; sentencing indefinitely delayed |"], "published_date": "2026-04-25T16:27:23.000", "score": null}]
```

## 💬 Response

I now have excellent data points spanning the full trajectory. Let me compile the findings.

I now have a comprehensive dataset with multiple confirmed data points from the primary source (Just Security) and corroborating trackers. Let me write up the synthesis.

## Research Report: Just Security Litigation Tracker — Legal Challenges to Trump Administration Actions

### Current Count (Most Recent Available)

As of **July 16, 2026**, Just Security's Litigation Tracker (justsecurity.org/107087) explicitly states: **"Total number of cases currently tracked: 900."** This is confirmed directly from the tracker page's live text.

**Case status breakdown as of July 16, 2026 (total 900):**
- **Plaintiff Wins: 285** — Government Action Blocked: 71; Temporarily Blocked: 143; Blocked Pending Appeal: 38; Case Closed in Favor of Plaintiff: 33
- **Government Wins: 139** — Temporary Block Denied: 62; Not Blocked Pending Appeal: 46; Closed/Dismissed in Favor of Government: 31
- **Case Pending: 414**
- **Other/Mixed: 62** — Temporarily Blocked in Part / Denied in Part: 20; Case Closed: 42

### Historical Trajectory (2025–2026)

The tracker captures cases filed since **January 20, 2025** (Trump's second inauguration). The count has grown at an average pace exceeding two new cases per day. Key documented data points:

| Date | Cases Tracked | Source |
|------|--------------|--------|
| ~June 2025 | 271 (described as "active lawsuits") | Global Law Today (citing Just Security) |
| Aug 6, 2025 | Tracker relaunched with new features (no count stated) | Just Security relaunch article |
| ~Aug 14, 2025 | ~708 (status snapshot: 238 plaintiff wins + 117 gov wins + 322 awaiting + 17 partial + 36 closed) | Just Security "Dissecting the Litigation" |
| Feb 10, 2026 | **627** ("Total number of cases currently tracked: 627") | Just Security tracker (archived PDF) |
| Apr 9, 2026 | **753** | AllAboutLawyer citing Just Security tracker |
| May 2026 | **753** | Resist Now (citing Just Security) |
| Jul 16, 2026 | **900** | Just Security tracker (live) |

**Important note on trajectory consistency:** The tracker's methodology has evolved. The ~708 figure implied by the August 2025 status snapshot appears higher than the 627 explicitly stated in February 2026, suggesting the tracker was recalibrated/reclassified between the August 2025 relaunch and early 2026 (e.g., de-duplicating or reclassifying cases). The most reliable "explicitly stated total" data points are: **627 (Feb 10, 2026) → 753 (Apr 9, 2026) → 900 (Jul 16, 2026)**. This shows roughly **+273 cases over ~5 months in 2026** (~55/month, or ~1.8/day) during that window.

### Corroborating Trackers (context, not the same count)
- **Lawfare tracker:** ~316 "active cases" (April 2026) — uses a narrower definition, consolidating a district case + its appeals into one matter.
- **New York Times tracker:** "more than 800" / "over 700" cases filed since Jan 20, 2025 (2026).

### Key Caveats
- The Just Security tracker counts **only cases where plaintiffs sue the administration** over executive actions; it excludes suits the Trump administration files as plaintiff and Trump's personal civil/criminal litigation.
- Counts differ across trackers due to differing case-consolidation methodologies.

Now I'll submit the structured output.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "As of July 16, 2026, Just Security's Litigation Tracker (justsecurity.org/107087) explicitly states \"Total number of cases currently tracked: 900.\" This is the most recent count available and is confirmed directly from the live tracker page. The 900 cases break down as: 285 plaintiff wins (71 government actions blocked, 143 temporarily blocked, 38 blocked pending appeal, 33 closed in plaintiff's favor); 139 government wins (62 temporary blocks denied, 46 not blocked pending appeal, 31 closed/dismissed in government's favor); 414 pending cases; and 62 other/mixed outcomes (20 temporarily blocked in part/denied in part, 42 closed).\n\nThe tracker captures cases filed since January 20, 2025 (Trump's second inauguration) and grows at an average pace exceeding two new cases per day. Documented data points over 2025-2026 show the growth trajectory: approximately 271 cases (~June 2025), a relaunch with expanded features on August 6, 2025, roughly 708 implied by the August 14, 2025 status snapshot (238 plaintiff wins + 117 gov wins + 322 awaiting + 17 partial + 36 closed), 627 explicitly stated on February 10, 2026, 753 as of April 9, 2026, 753 as of May 2026, and 900 as of July 16, 2026.\n\nNote that the tracker's methodology appears to have been recalibrated between the August 2025 relaunch and early 2026, since the ~708 implied August 2025 figure is higher than the 627 explicitly stated in February 2026 (likely reclassification/de-duplication). The most reliable series of explicitly-stated totals is 627 (Feb 10, 2026) to 753 (Apr 9, 2026) to 900 (Jul 16, 2026), representing roughly +273 cases over about five months in 2026 (~55/month, ~1.8/day).\n\nImportant caveats: The Just Security tracker counts only cases where plaintiffs sue the administration over executive actions; it excludes suits the Trump administration files as plaintiff and Trump's personal civil/criminal litigation. Other trackers report different totals due to differing consolidation methods: Lawfare counts ~316 \"active cases\" (April 2026, consolidating district cases with their appeals), and the New York Times tracker reported \"more than 800\" / \"over 700\" cases (2026). Monthly counts are approximate because Just Security publishes running totals rather than a monthly filing series, and the underlying count evolved with methodology changes.</answer>\n<parameter name=\"key_facts\">[\"Just Security's Litigation Tracker states 'Total number of cases currently tracked: 900' as of July 16, 2026 (most recent available count).\", \"The July 16, 2026 breakdown: 285 plaintiff wins, 139 government wins, 414 pending, 62 other/mixed (total 900).\", \"The tracker captures cases filed since January 20, 2025, the start of Trump's second term.\", \"Explicit total was 627 on February 10, 2026, growing to 753 by April 9, 2026, and 900 by July 16, 2026.\", \"Approximately 271 cases were tracked around June 2025; the tracker was relaunched with expanded features on August 6, 2025.\", \"An August 14, 2025 status snapshot implied roughly 708 cases (238 plaintiff wins + 117 gov wins + 322 awaiting + 17 partial + 36 closed).\", \"Growth averaged more than two new cases per day since January 2025; roughly +273 cases across ~5 months in early-to-mid 2026 (~55/month).\", \"The tracker counts only suits AGAINST the administration over executive actions; it excludes Trump-filed suits and his personal civil/criminal cases.\", \"Other trackers differ: Lawfare counted ~316 'active cases' (April 2026); NYT reported 'more than 800' cases filed (2026), due to differing consolidation methodologies.\", \"Apparent methodology recalibration occurred between the Aug 2025 relaunch (~708 implied) and Feb 2026 (627 explicit), so cross-period comparisons should be treated cautiously.\"]</answer>\n<parameter name=\"sources\">[{\"url\": \"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/\", \"title\": \"Litigation Tracker: Legal Challenges to Trump Administration Actions\", \"domain\": \"justsecurity.org\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"Total number of cases currently tracked: 900. (page last updated July 16, 2026)\"}, {\"url\": \"https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/\", \"title\": \"New and Improved Litigation Tracker: Legal Challenges to Trump Administration Actions\", \"domain\": \"justsecurity.org\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"Relaunch dated Aug. 6, 2025; tracker now captures cases filed since Jan. 20, 2025.\"}, {\"url\": \"https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/\", \"title\": \"Dissecting the Litigation: Where Trump Administration Actions Face Early Roadblocks or Traction\", \"domain\": \"justsecurity.org\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"Aug 14, 2025 status snapshot: 238 plaintiff wins, 117 government wins, 322 awaiting ruling, 17 partial, 36 closed.\"}, {\"url\": \"https://myattorneyusa.com/wp-content/uploads/2026/02/legal-challenges-to-trump-administration-actions.pdf\", \"title\": \"Litigation Tracker: Legal Challenges to Trump Administration Actions (archived Feb 2026 PDF)\", \"domain\": \"myattorneyusa.com\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"Published February 10, 2026: Total number of cases currently tracked: 627.\"}, {\"url\": \"https://allaboutlawyer.com/trump-lawsuits/\", \"title\": \"Trump Lawsuits 2026, Every Major Case And What's Happened\", \"domain\": \"allaboutlawyer.com\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"As of April 9, 2026, Just Security's litigation tracker counts 753 cases challenging Trump administration actions; Lawfare counts 316 active cases.\"}, {\"url\": \"https://resistnow.net/briefs/courts-blocking-analysis/\", \"title\": \"262 Court Losses. 753 Lawsuits. The Courts Are Saying the Same Three Things.\", \"domain\": \"resistnow.net\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"As of May 2026, 753 lawsuits have been filed against the Trump administration, averaging more than two new cases per day since January 2025 (Just Security tracker).\"}, {\"url\": \"https://www.globallawtoday.com/law/legal-news/2025/06/selective-coverage-just-securitys-litigation-tracker-omits-trump%E2%80%91filed-civil-suits/\", \"title\": \"Selective Coverage: Just Security's Litigation Tracker Omits Trump-Filed Civil Suits\", \"domain\": \"globallawtoday.com\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"Tracker monitoring 271 active lawsuits challenging Trump administration executive actions (June 2025); excludes cases where administration is plaintiff.\"}, {\"url\": \"https://www.nytimes.com/interactive/2026/us/trump-administration-lawsuits.html\", \"title\": \"Tracking the Lawsuits Against the Trump Administration: Immigration, Tariffs and More\", \"domain\": \"nytimes.com\", \"accessed_at\": \"2026-07-17T00:00:00Z\", \"snippet\": \"NYT tracker: more than 800 lawsuits; 481 active, 165 active with policy halted, 175 with final decision.\"}]</answer>\n<parameter name=\"data_points\">[{\"metric\": \"Total cases tracked (Just Security)\", \"value\": 900, \"unit\": \"cases\", \"as_of\": \"2026-07-16\", \"source_url\": \"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/\"}, {\"metric\": \"Plaintiff wins\", \"value\": 285, \"unit\": \"cases\", \"as_of\": \"2026-07-16\", \"source_url\": \"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/\"}, {\"metric\": \"Government wins\", \"value\": 139, \"unit\": \"cases\", \"as_of\": \"2026-07-16\", \"source_url\": \"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/\"}, {\"metric\": \"Pending cases\", \"value\": 414, \"unit\": \"cases\", \"as_of\": \"2026-07-16\", \"source_url\": \"https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/\"}, {\"metric\": \"Total cases tracked (Just Security)\", \"value\": 627, \"unit\": \"cases\", \"as_of\": \"2026-02-10\", \"source_url\": \"https://myattorneyusa.com/wp-content/uploads/2026/02/legal-challenges-to-trump-administration-actions.pdf\"}, {\"metric\": \"Total cases tracked (Just Security)\", \"value\": 753, \"unit\": \"cases\", \"as_of\": \"2026-04-09\", \"source_url\": \"https://allaboutlawyer.com/trump-lawsuits/\"}, {\"metric\": \"Total cases tracked (Just Security)\", \"value\": 753, \"unit\": \"cases\", \"as_of\": \"2026-05-15\", \"source_url\": \"https://resistnow.net/briefs/courts-blocking-analysis/\"}, {\"metric\": \"Active lawsuits tracked (Just Security)\", \"value\": 271, \"unit\": \"cases\", \"as_of\": \"2025-06-01\", \"source_url\": \"https://www.globallawtoday.com/law/legal-news/2025/06/selective-coverage-just-securitys-litigation-tracker-omits-trump%E2%80%91filed-civil-suits/\"}, {\"metric\": \"Implied total cases (Aug 2025 status snapshot sum)\", \"value\": 708, \"unit\": \"cases\", \"as_of\": \"2025-08-14\", \"source_url\": \"https://www.justsecurity.org/118995/dissecting-trump-administration-litigation/\"}]"
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's a summary of my findings on the Just Security Litigation Tracker:

## Current Count
As of **July 16, 2026** (most recent available), the tracker explicitly states: **"Total number of cases currently tracked: 900."** This is confirmed directly from the live tracker page.

**Breakdown (900 total):** 285 plaintiff wins, 139 government wins, 414 pending, 62 other/mixed.

## Historical Trajectory (2025–2026)
The tracker captures cases filed since January 20, 2025, growing at more than two new cases per day:

| Date | Cases |
|------|-------|
| ~June 2025 | ~271 |
| Aug 6, 2025 | Relaunch (new features) |
| ~Aug 14, 2025 | ~708 (implied from status snapshot) |
| **Feb 10, 2026** | **627** (explicit) |
| **Apr 9, 2026** | **753** (explicit) |
| May 2026 | 753 |
| **Jul 16, 2026** | **900** (explicit) |

**Key caveat:** The methodology appears to have been recalibrated between the Aug 2025 relaunch (~708 implied) and Feb 2026 (627 explicit), so the cleanest comparable series is 627 → 753 → 900 across 2026 (~+273 cases in ~5 months, ~55/month). Just Security publishes running totals rather than a monthly filing series, so exact monthly counts must be approximated from these snapshots.

**Other caveats:** The tracker counts only suits *against* the administration over executive actions (excludes Trump-filed suits and his personal cases). Other trackers report different totals due to differing consolidation methods (Lawfare: ~316 "active cases"; NYT: "more than 800").


### ↳ End nested research agent trace

## 💭 Thinking



## 💬 Response

Current count is 900 as of July 16, 2026. Resolution is August 31, 2026 (~46 days later). Let me analyze the growth trajectory.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\n\n# Data points 2026: Feb 10 = 627, Apr 9 = 753, Jul 16 = 900\nfrom datetime import date\nd_feb = date(2026,2,10); d_apr = date(2026,4,9); d_jul = date(2026,7,16)\nprint(\"Feb->Apr rate:\", (753-627)/(d_apr-d_feb).days, \"days:\", (d_apr-d_feb).days)\nprint(\"Apr->Jul rate:\", (900-753)/(d_jul-d_apr).days, \"days:\", (d_jul-d_apr).days)\nprint(\"Feb->Jul overall:\", (900-627)/(d_jul-d_feb).days)\n\nhorizon = (date(2026,8,31)-d_jul).days\nprint(\"Horizon days:\", horizon)\n\n# Recent rate ~1.5/day, earlier ~2.17/day. Use uncertain rate.\n# Model rate distribution: mixture centered on recent rate with uncertainty\nN=200000\n# base daily rate: draw from distribution reflecting uncertainty between recent(1.5) and possible accel/decel\nrate = np.random.normal(1.55, 0.45, N)\nrate = np.clip(rate, 0.3, None)\n# daily additions poisson-ish; total additions = sum over horizon with rate noise\n# add day-to-day variance\ntotals = np.zeros(N)\nadds = np.random.poisson(np.clip(rate[:,None]*np.ones((1,horizon)),0,None))\ntotal_adds = adds.sum(axis=1)\nfinal = 900 + total_adds\n\npcts = [1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nfor p in pcts:\n    print(p, round(np.percentile(final,p),1))\nprint(\"mean\", final.mean())\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Feb->Apr rate: 2.1724137931034484 days: 58\nApr->Jul rate: 1.5 days: 98\nFeb->Jul overall: 1.75\nHorizon days: 46\n1 921.0\n5 935.0\n10 943.0\n20 952.0\n25 956.0\n30
959.0\n40 965.0\n50 971.0\n60 977.0\n70 983.0\n75 986.0\n80 990.0\n90 1000.0\n95 1009.0\n99 1025.0\nmean 971.336705\n", "stderr": "", "duration_ms": 535}
```

## 💭 Thinking



## 💬 Response

The Poisson model is too narrow—it ignores rate uncertainty and methodology recalibration risk (the tracker was recalibrated before, dropping from ~708 to 627). Let me widen with these real uncertainty sources.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(7)\nN=300000\nhorizon=46\n\n# Scenario mixture\n# Base case (70%): steady growth, rate uncertain around recent 1.5/day, sd wide\n# Accel (15%): rate higher ~2.2/day (like early 2026 or new policy burst)\n# Decel/recalibration (15%): slower or slight consolidation, rate low or negative net\n\nu=np.random.rand(N)\nrate=np.empty(N)\nbase=u<0.70\naccel=(u>=0.70)&(u<0.85)\ndecel=u>=0.85\nrate[base]=np.random.normal(1.5,0.35,base.sum())\nrate[accel]=np.random.normal(2.3,0.4,accel.sum())\nrate[decel]=np.random.normal(0.6,0.6,decel.sum())  # includes possibility of net stagnation/consolidation\n\ntotal_adds = rate*horizon + np.random.normal(0, np.sqrt(np.clip(rate*horizon,1,None)), N)  # poisson-ish noise\n# small chance of recalibration jump (methodology) affecting level\nrecal = np.random.rand(N)<0.05\nrecal_effect = np.where(recal, np.random.normal(0,40,N), 0)\n\nfinal = 900 + total_adds + recal_effect\n\npcts=[1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nres={p:round(float(np.percentile(final,p)),1) for p in pcts}\nfor p in pcts: print(p, res[p])\nprint(\"mean\",round(final.mean(),1))\nprint(\"P(<899.5)\", round((final<899.5).mean(),3))\nprint(\"P(>1099.5)\", round((final>1099.5).mean(),3))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "1 883.4\n5 912.7\n10 931.0\n20 947.1\n25 951.9\n30 955.9\n40 962.7\n50 968.9\n60 975.3\n70 982.3\n75 986.4\n80 991.2\n90 1005.4\n95 1018.1\n99 1041.9\nmean 968.3\nP(<899.5)
0.026\nP(>1099.5) 0.0\n", "stderr": "", "duration_ms": 78}
```

## 💭 Thinking



## 💬 Response

The distribution centers around 969, grounded in the recent ~1.5 cases/day rate applied over 46 days from the current 900. Let me checkpoint.
