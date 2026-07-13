# Reasoning Log: How many EU member states will the AI Act National Implementation tracker classify as having clear market surveillance and notifying authorities on August 31, 2026?

*Generated: 2026-07-07T21:11:46.667747+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "How many EU member states are classified as \"Clear\" for having designated market surveillance authorities and notifying authorities? List the classification categories and counts for each member state."
}
```

### 📋 Result

```
{"url": "https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content, **9 EU Member States** are classified as \"Clear\" for having designated both market
surveillance and notifying authorities.\n\nThe classification categories and their counts are:\n\n1. **Clear** (designated both market surveillance and notifying authorities): **9 Member States**\n2.
**Partial clarity** (pending legislative proposals, announcements, or appointed one competent authority): **12 Member States**\n3. **Unclear** (yet to designate or establish any competent authority):
**6 Member States**\n\n**Total: 27 EU Member States**\n\nNote: The content mentions these are the counts \"as of the date this post was last updated\" (17 June 2026), but does not list which specific
member states fall into each category in the summary tables shown.\n\nFrom the detailed country-by-country information provided, the member states classified as \"Clear\" appear to include: Cyprus,
Denmark, Finland, Hungary, Ireland, Italy, Lithuania, Malta, and Slovenia.\n\n**Relevant links:**\n- [Full Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)\n-
[Commission's consolidated list of authorities](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Commission's list of fundamental rights protection
authorities](https://digital-strategy.ec.europa.eu/en/policies/fundamental-rights-protection-authorities-ai-act)\n- [Contact for updates](mailto:website@futureoflife.org)\n- [AI Act
newsletter](https://artificialintelligenceact.substack.com/)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "History of the artificialintelligenceact.eu national implementation plans tracker: how many EU member states classified as \"Clear\" (designated both market surveillance and notifying authorities) over time in 2025 and 2026. What is the trend/rate of member states moving to \"Clear\" status?",
  "context": "The tracker at https://artificialintelligenceact.eu/national-implementation-plans/ classifies 27 EU member states as Clear, Partial clarity, or Unclear regarding AI Act competent authority designation. As of 17 June 2026 update: 9 Clear, 12 Partial, 6 Unclear. The legal deadline was 2 August 2025. I need the historical trajectory of the \"Clear\" count to project what it will be on 31 August 2026.",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'History of the...ust 2026.', 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "History of the artificialintelligenceact.eu national implementation plans tracker: how many EU member states classified as Clear (designated both market surveillance and notifying authorities) over time in late 2025 and 2026. What is the trend/rate of member states moving to Clear status?",
      "context": "The tracker at https://artificialintelligenceact.eu/national-implementation-plans/ classifies 27 EU member states as Clear, Partial clarity, or Unclear regarding AI Act competent authority designation. As of 17 June 2026 update: 9 Clear, 12 Partial, 6 Unclear. The legal deadline was 2 August 2025. I need the historical trajectory of the Clear count to project what it will be on 31 August 2026.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "History of the artificialintelligenceact.eu national implementation plans tracker: how many EU member states classified as Clear (designated both market surveillance and
notifying authorities) over time in late 2025 and 2026. What is the trend/rate of member states moving to Clear status?", "entry": {"slug": "history-of-the-artificialintelligenceact-eu-
nation-7187597f", "query": "History of the artificialintelligenceact.eu national implementation plans tracker: how many EU member states classified as Clear (designated both market surveillance and
notifying authorities) over time in late 2025 and 2026. What is the trend/rate of member states moving to Clear status?", "answer": "I've completed the research. Here's the key takeaway for your
forecasting purpose:\n\n**The \"Clear\" count is a step-function driven by editorial updates, not a smooth real-time metric.** The tracker sat at **3 Clear (page-dated 19 May 2025) for ~13 months**,
then jumped to **9 Clear** in a single overhaul on **17 June 2026**. The most recent snapshot (3 July 2026) confirms it's stable at 9.\n\n**Verified trajectory:**\n- Aug 2025 \u2192 June 16, 2026:
locked at **3 Clear** (page never refreshed from its 19 May 2025 vintage)\n- June 17, 2026: overhaul to **9 Clear / 12 Partial / 6 Unclear**\n- July 3, 2026: still **9 Clear**\n\n**Implications for
projecting 31 August 2026:**\n- Direction is upward (3\u21929), but the movement happens in infrequent batch revisions, not continuously.\n- The last overhaul was only ~3 weeks before today (7 July
2026), so 9 is the current stable value.\n- A further revision is plausible around the **2 August 2026** high-risk/sandbox deadline, which could push some of the 12 \"Partial\" states (Spain, Germany,
Poland, Netherlands, etc.) into Clear \u2014 but historically the maintainers update rarely, so 9 could also persist through 31 August.\n- There's minor membership churn within the count (Malta vs.
Spain across snapshots) while the total held at 9.\n\nThe biggest caveat: **this tracker lags real-world designations substantially**, so its count reflects when the FLI team refreshes the page more
than the underlying pace of member-state action.", "sources": [{"url": "https://artificialintelligenceact.eu/national-implementation-plans/", "title": "Overview of all AI Act National Implementation
Plans", "domain": "artificialintelligenceact.eu", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update: 17 June 2026. Clear: 9, Partial clarity: 12, Unclear: 6 (27 EU member states)."},
{"url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 2 Aug 2025)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear."}, {"url":
"http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 31 Dec 2025)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 19 May 2025; 3 Clear (Denmark, Hungary, Luxembourg), 10 Partial, 14 Unclear."}, {"url":
"http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 22 Mar 2026)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear."}, {"url":
"http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 4 Jun 2026)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear (still old data)."}, {"url":
"http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 16 Jun 2026)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear (day before overhaul)."}, {"url":
"http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/", "title": "National Implementation Plans (archived 3 Jul 2026)", "domain":
"web.archive.org", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Last update 17 June 2026; 9 Clear, 12 Partial, 6 Unclear."}, {"url": "https://ai-regulation.com/designation-of-national-competent-
authorities-under-the-eu-ai-act/", "title": "Who Oversees AI in the EU? The Designation of National Competent Authorities", "domain": "ai-regulation.com", "accessed_at": "2026-07-07T00:00:00Z",
"snippet": "One week prior to the deadline, the majority of member states were behind schedule."}, {"url": "https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement",
"title": "Governance and enforcement of the AI Act", "domain": "digital-strategy.ec.europa.eu", "accessed_at": "2026-07-07T00:00:00Z", "snippet": "Commission consolidated list of national authorities
designated under the AI Act."}], "key_facts": [], "data_points": [{"metric": "Clear member states (tracker, page-dated 19 May 2025)", "value": 3.0, "unit": "member states", "as_of": "2025-08-02",
"source_url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Clear member states (tracker, page-dated 19 May 2025)",
"value": 3.0, "unit": "member states", "as_of": "2025-12-31", "source_url": "http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric":
"Clear member states (tracker, page-dated 19 May 2025)", "value": 3.0, "unit": "member states", "as_of": "2026-03-22", "source_url":
"http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Clear member states (tracker, page-dated 19 May 2025)", "value": 3.0,
"unit": "member states", "as_of": "2026-06-16", "source_url": "http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Clear member
states (tracker, page-dated 17 June 2026)", "value": 9.0, "unit": "member states", "as_of": "2026-06-17", "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"},
{"metric": "Clear member states (tracker, page-dated 17 June 2026)", "value": 9.0, "unit": "member states", "as_of": "2026-07-03", "source_url":
"http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Partial clarity member states (tracker)", "value": 12.0, "unit": "member
states", "as_of": "2026-06-17", "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Unclear member states (tracker)", "value": 6.0, "unit": "member
states", "as_of": "2026-06-17", "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric": "Partial clarity member states (tracker, old methodology)", "value":
10.0, "unit": "member states", "as_of": "2025-08-02", "source_url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"}, {"metric":
"Unclear member states (tracker, old methodology)", "value": 14.0, "unit": "member states", "as_of": "2025-08-02", "source_url":
"http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"}], "created_at": "2026-07-07T21:10:46.366429Z", "updated_at":
"2026-07-07T21:10:46.366429Z", "stale_after": "2026-07-08T03:10:46.366429Z", "state": "fresh", "revision_history": [], "session_id": "dd1a9b0a-6b1b-4ef3-a04b-27a734a74935", "follow_up_count": 0},
"is_follow_up": false}], "successful_count": 1, "failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: History of the artificialintelligenceact.eu national implementation plans tracker: how many EU member states classified as Clear (designated both market surveillance and notifying authorities) over time in late 2025 and 2026. What is the trend/rate of member states moving to Clear status?

*Generated: 2026-07-07T21:10:46.359473+00:00*


## 💬 Response

I'll research the history of the artificialintelligenceact.eu national implementation plans tracker, focusing on how the "Clear" classification count has changed over time.

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

## 💬 Response

I have the fetch tools loaded. Let me start by fetching the current tracker page and searching for historical versions.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "How many EU member states are classified as Clear, Partial clarity, and Unclear regarding AI Act competent authority designation? What is the last update date? List the status of each member state."
}
```

### 📋 Result

```
{"url": "https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content (last updated **17 June 2026**):\n\n## Overall Classification (27 EU Member States):\n-
**Clear**: 9 member states (designated both market surveillance and notifying authorities)\n- **Partial clarity**: 12 member states (pending legislative proposals, announcements, or appointed one
competent authority)\n- **Unclear**: 6 member states (no competent authority designated yet)\n\n## Status by Member State:\n\n**CLEAR (9):**\n1. Cyprus - Commissioner of Communications\n2. Denmark -
Danish Agency for Digital Government\n3. Finland - Finnish Transport and Communications Agency (Traficom) as single point of contact\n4. Hungary - Minister for Enterprise Development\n5. Ireland -
Decentralised model with 15 authorities\n6. Italy - National Cybersecurity Agency (ACN)\n7. Lithuania - Communications Regulatory Authority\n8. Malta - Malta Digital Innovation Authority (MDIA)\n9.
Slovenia - Agency for Communication Networks and Services\n\n**PARTIAL CLARITY (12):**\n1. Belgium - Federal Institute for Postal Services expected to be main authority\n2. Czechia - Legislative
proposal: Telecommunication Office\n3. France - Decentralised model proposed\n4. Germany - Draft law: Federal Network Agency (Bundesnetzagentur)\n5. Latvia - Report published, Consumer Rights
Protection Centre proposed\n6. Luxembourg - Draft law: National Commission for Data Protection\n7. Netherlands - Draft legislation: 10 sectoral authorities\n8. Poland - Legislative proposal:
Commission on Development and Safety of AI\n9. Portugal - National Communications Authority announced\n10. Romania - Memorandum: National Authority for Administration and Regulation in
Communication\n11. Slovakia - Draft legislation: Office for Digital Integrity\n12. Spain - Spanish AI Supervisory Agency established; draft law pending\n\n**UNCLEAR (6):**\n1. Austria - AI Service
Desk established but authorities not appointed\n2. Bulgaria - Ministry coordinates but no authorities appointed\n3. Croatia - No authorities appointed\n4. Estonia - No authorities appointed\n5. Greece
- No authorities appointed\n6. Sweden - Proposal: Post and Telecom Authority\n\n## Relevant links:\n- [Full Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)\n-
[Commission's consolidated list of authorities](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Commission's list of fundamental rights protection
authorities](https://digital-strategy.ec.europa.eu/en/policies/fundamental-rights-protection-authorities-ai-act)\n- [Contact for contributions](mailto:website@futureoflife.org)\n- [AI Act
newsletter](https://artificialintelligenceact.substack.com/)\n- [Future of Life Institute](https://futureoflife.org/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "query": "artificialintelligenceact.eu national implementation plans tracker Clear Partial Unclear member states"
}
```

### 📋 Result

```
{"query": "artificialintelligenceact.eu national implementation plans tracker Clear Partial Unclear member states", "results": [{"title": "Overview of all AI Act National Implementation Plans | EU
Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/national-implementation-plans/", "snippet": "Last update: 17 June 2026\nSince the AI Act entered into force on 1 August 2024,
the focus for Member States has shifted to national implementation. One of the first tasks for Member States is to designate the relevant authorities. This post gives an overview of the national
authorities designated under the AI Act and what we know about the national implementation plans.*\nThis resource is a work in progress and will be updated when new information is available. Please
help us ensure the completen", "api_data": null, "hint": null}, {"title": "EU Artificial Intelligence Act | Up-to-date developments and analyses of the EU AI Act", "url":
"https://artificialintelligenceact.eu/", "snippet": "The EU Artificial Intelligence Act\nUp-to-date developments and analyses of the EU AI Act\n[AI Act
Explorer](https://artificialintelligenceact.eu/ai-act-explorer/)\nBrowse the full AI Act text online. Search within the Act for parts which are relevant to
you.\n![EU_AI_Act_Coverpage_wide](https://artificialintelligenceact.eu/wp-content/uploads/2024/02/EU_AI_Act_Coverpage_wide.jpg)\n[Compliance
Checker](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/)\nDiscover how the AI A", "api_data": null, "hint": null}, {"title": "AI Act | Shaping Europe's digital future -
European Union", "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", "snippet": "The AI Act is the first-ever legal framework on AI, which addresses the risks of AI and
positions Europe to play a leading role globally.\nThe [AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) (Regulation (EU) 2024/1689 laying down harmonised rules on
artificial intelligence) is the first-ever comprehensive legal framework on AI worldwide. The aim of the rules is to foster trustworthy AI in Europe. For any questions on the AI Act, check out the [AI
Act Single Inform", "api_data": null, "hint": null}, {"title": "AI Regulatory Sandbox Approaches: EU Member State Overview | EU Artificial Intelligence Act", "url":
"https://artificialintelligenceact.eu/ai-regulatory-sandbox-approaches-eu-member-state-overview/", "snippet": "AI regulatory sandboxes are an important part of the implementation of the EU AI Act.
According to [Article 57](https://artificialintelligenceact.eu/article/57/) of the AI Act, each Member State must establish at least one AI regulatory sandbox at the national level by 2 August 2026.
This post provides an overview of how different EU Member States are approaching the design and implementation of these sandboxes, as well as of EU-wide initiatives that support them.\nThis resource
is a work in prog", "api_data": null, "hint": null}, {"title": "Implementation Timeline | EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/implementation-timeline/",
"snippet": "Implementation Timeline\nThis page lists all of the key dates you need to be aware of relating to the implementation of the EU AI Act.\nRelated resources\nTasks and Responbilities\nFor a
summary of all tasks and responsibilities assigned to the [AI Office](https://artificialintelligenceact.eu/responsibilities-of-european-commission-ai-office/) or [Member
States](https://artificialintelligenceact.eu/responsibilities-of-member-states/) by the EU AI Act, see our blog posts and infographics on the topic", "api_data": null, "hint": null}, {"title": "The AI
Act Explorer | EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/ai-act-explorer/", "snippet": "BETA \ud83d\udd14 New: Try the [new AI Act
Explorer](https://explorer.artificialintelligenceact.eu/), rebuilt from the ground up for 2026. Read the official text in all 24 EU languages, including the 'Code of Practice' and other documents.
Compare languages side-by-open, open items in a 'side peek' for easy reference, and share URLs direct to an individual paragraph. Custom AI chatbot to answer your questions (coming soon). [Go to the
new AI Act Explorer \u2192](https://explorer.artificialintelligenceact.eu/)\nT", "api_data": null, "hint": null}, {"title": "Governance and enforcement of the AI Act | Shaping Europe\u2019s digital
future", "url": "https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement", "snippet": "The European AI Office and the national market surveillance authorities are
responsible for implementing, supervising and enforcing the AI Act.\nThe AI Act\u2019s governance will be steered by three advisory bodies:\n- the\n[European Artificial Intelligence
Board](https://digital-strategy.ec.europa.eu/en/policies/ai-board), composed of representatives from the EU Member States, - the\n[Scientific Panel](https://digital-
strategy.ec.europa.eu/en/policies/ai-scientific-panel), composed of independent expert", "api_data": null, "hint": null}, {"title": "State of the Act: EU AI Act implementation in key Member States |
Technology's Legal Edge", "url": "https://www.technologyslegaledge.com/2025/11/state-of-the-act-eu-ai-act-implementation-in-key-member-states/", "snippet": "The dream of directly effective supra-
national legislation, applying in exactly the same way in each EU Member State: an EU Regulation should (in theory) provide the same protections in the same way at the same time to all EU citizens. As
is ever the case, theory and reality rarely align, and the EU AI Act is proving to be a case in point. While the core text Regulation EU 2024/1689 is rolling out to the same timetable in all Member
States, there are many steps that Member States or their design", "api_data": null, "hint": null}, {"title": "EU AI Act - Updates, Compliance, Training", "url": "https://www.artificial-intelligence-
act.com/", "snippet": "What is the EU AI Act?\nThe EU AI Act sets harmonised rules for the development, placement on the market and use of AI systems in the European Union, following a proportionate
risk-based approach.\nThe Act lays down a solid risk methodology to define \u201chigh-risk\u201d AI systems that pose significant risks to the health, safety or fundamental rights of persons. Those AI
systems will have to comply with a set of horizontal mandatory requirements for trustworthy AI, and follow conformity assessment proced", "api_data": null, "hint": null}, {"title": "AI Watch: Global
regulatory tracker - European Union | White & Case LLP", "url": "https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-european-union", "snippet": null, "api_data": null,
"hint": null}]}
```

## 💬 Response

I have the current snapshot (17 June 2026: 9 Clear, 12 Partial, 6 Unclear). Now I need the historical trajectory. The best source is the Wayback Machine (web.archive.org). Let me query the archive for historical snapshots of this page.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/cdx/search/cdx?url=artificialintelligenceact.eu/national-implementation-plans/&output=json&fl=timestamp,original,statuscode&collapse=digest&limit=200",
  "prompt": "List all archived snapshot timestamps of this page"
}
```

### 📋 Result

```
{"url": "http://web.archive.org/cdx/search/cdx?url=artificialintelligenceact.eu/national-implementation-plans/&output=json&fl=timestamp,original,statuscode&collapse=digest&limit=200", "content":
"Based on the content, here are all archived snapshot timestamps of the page:\n\n1. 20241113090344\n2. 20241127235147\n3. 20241205024010\n4. 20241217074650\n5. 20241219035449\n6. 20250117042652\n7.
20250210024329\n8. 20250318010447\n9. 20250322145748\n10. 20250322150728\n11. 20250331231420\n12. 20250426145710\n13. 20250517125958\n14. 20250610122143\n15. 20250802104033\n16. 20250905220355\n17.
20250920033239\n18. 20251107113335\n19. 20251113023342\n20. 20251203173354\n21. 20251231214055\n22. 20260102021207\n23. 20260113234231\n24. 20260204152334\n25. 20260204205326\n26. 20260205091457\n27.
20260206235337\n28. 20260212005543\n29. 20260212150908\n30. 20260220005902\n31. 20260220134442\n32. 20260306180810\n33. 20260313093018\n34. 20260322105019\n35. 20260429053837\n36. 20260604075359\n37.
20260616043104\n38. 20260703043308\n\n**Total: 38 snapshots** ranging from November 13, 2024 to July 3, 2026.\n\nNote: Most snapshots have status code 200 (successful), with a few showing 301
(redirect)."}
```

## 💬 Response

Excellent. I have 38 snapshots. I need to focus on the key ones spanning the period around and after the 2 August 2025 deadline through mid-2026. Let me fetch several key historical snapshots to extract the Clear/Partial/Unclear counts. I'll fetch snapshots strategically across the timeline.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "Count how many EU member states are classified as Clear (both market surveillance and notifying authorities designated), Partial clarity, and Unclear. Give the exact numbers for each category and the last update date shown on the page. List which countries are in the Clear category."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content provided, here is the classification of EU
member states regarding their AI Act authority designations:\n\n**Last update date:** 19 May 2025\n\n**Classification counts:**\n- **Clear** (both authorities designated): 3 Member States\n- **Partial
clarity** (pending legislative proposals or one authority appointed): 10 Member States\n- **Unclear** (no authorities designated yet): 14 Member States\n\n**Countries in the \"Clear\" category:**\nThe
text states that \"three Member States have designated both notifying and market surveillance authorities\" but does not explicitly list which three countries fall into this category in the excerpted
portion. However, based on the detailed table information provided:\n\n1. **Denmark** - Danish Agency for Digital Government designated as coordinating market surveillance authority\n2. **Luxembourg**
- National Commission for Data Protection designated as competent authority\n3. **Malta** - Malta Digital Innovation Authority (MDIA) jointly serving as market surveillance authority with notifying
authority designation\n\nNote: The text mentions that regarding fundamental rights authorities (Art 77), Hungary and Italy had not yet designated authorities as of the last update date.\n\n**Relevant
links:**\n- [Implementation Timeline for all key dates and deadlines for the AI Act](http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/implementation-timeline/)\n-
[Commission consolidated list of authorities](http://web.archive.org/web/20250802104033/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Article 77 of the AI
Act](http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/article/77/)\n- [Article 113 of the AI
Act](http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/article/113/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "url": "http://web.archive.org/web/20250905220355/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "Count how many EU member states are classified as Clear (both market surveillance and notifying authorities designated), Partial clarity, and Unclear. Give the exact numbers for each category and the last update date shown on the page. List which countries are in the Clear category."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20250905220355/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content provided:\n\n**Last Update Date:** 19 May
2025\n\n**Classification Numbers:**\n- **Clear** (both authorities designated): 3 Member States\n- **Partial clarity** (pending legislative proposals or one authority appointed): 10 Member States  \n-
**Unclear** (no authorities designated): 14 Member States\n\n**Countries in the Clear Category:**\nThe text mentions \"three Member States have designated both notifying and market surveillance
authorities\" but does not explicitly list which specific countries fall into this category. Based on the detailed table information provided, the following appear to have designated both
authorities:\n\n1. **Denmark** - Danish Agency for Digital Government designated as coordinating market surveillance authority and single point of contact, with legislative proposal for minister to
designate additional authorities\n2. **Luxembourg** - National Commission for Data Protection designated as competent authority, with draft law outlining three notifying authorities and multiple
market surveillance authorities\n3. **Hungary** - Minister for National Economy designated for market surveillance tasks, National Accreditation Authority as notifying authority (per May 2025
government resolution)\n\n**Note:** The exact three countries are not explicitly stated in a summary section, so this is inferred from the country-by-country details provided.\n\n**Relevant
links:**\n- [Implementation Timeline for the AI Act](http://web.archive.org/web/20250905220355/https://artificialintelligenceact.eu/implementation-timeline/)\n- [Commission consolidated list of
authorities](http://web.archive.org/web/20250905220355/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Contact for
updates](http://web.archive.org/web/20250905220355/mailto:tekla@futureoflife.org)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💬 Response

Both these snapshots reflect the "19 May 2025" update (3 Clear). The pages were captured on 2 Aug and 5 Sep but the content hadn't been updated yet. Let me fetch the later snapshots to trace the trajectory through late 2025 and 2026.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/web/20251107113335/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20251107113335/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content provided:\n\n**Last update date:** 19 May
2025\n\n**Classification of EU Member States:**\n\nAccording to Table 1 in the content, the status breakdown shows:\n- **Clear** (both notifying and market surveillance authorities designated): **3
Member States**\n- **Partial clarity** (pending legislative proposals or one competent authority appointed): **10 Member States**\n- **Unclear** (no competent authority designated): **14 Member
States**\n\n**Countries classified as \"Clear\":**\nThe content states \"three Member States have designated both notifying and market surveillance authorities\" but does not explicitly list which
three countries fall into this category in the excerpted text. However, based on Table 2 details provided:\n- **Denmark** - Danish Agency for Digital Government designated as coordinating market
surveillance authority\n- **Hungary** - Minister for National Economy designated for market surveillance; National Accreditation Authority as notifying authority (per May 2025 government
resolution)\n- **Luxembourg** - National Commission for Data Protection designated as competent authority, with draft law outlining notifying authorities\n\nNote: The full Table 2 content appears
truncated in the provided text, so this list may be incomplete.\n\n**Relevant links:**\n- [Commission consolidated list of authorities](http://web.archive.org/web/20251107113335/https://digital-
strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Implementation Timeline](http://web.archive.org/web/20251107113335/https://artificialintelligenceact.eu/implementation-
timeline/)\n- [Article 77 of the AI Act](http://web.archive.org/web/20251107113335/https://artificialintelligenceact.eu/article/77/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "url": "http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content:\n\n**Last update date:** 19 May
2025\n\n**Classification of EU Member States:**\n- **Clear (both authorities designated):** 3 member states\n- **Partial clarity:** 10 member states  \n- **Unclear:** 14 member states\n\n**Clear
countries (both market surveillance and notifying authorities designated):**\n1. Denmark\n2. Hungary\n3. Luxembourg\n\nNote: The content mentions these numbers in Table 1 but the actual table data
appears incomplete in the provided text. Based on the detailed country entries, Denmark, Hungary, and Luxembourg appear to have designated both types of competent authorities as of the last update
date.\n\n**Relevant links:**\n- [Implementation Timeline](http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/implementation-timeline/)\n- [Commission consolidated list of
designated authorities](http://web.archive.org/web/20251231214055/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Article 70 - National competent
authorities](http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/article/70/)\n- [Article 77 - Fundamental rights
authorities](http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/article/77/)\n- [Article 113 - Entry into force and
application](http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/article/113/)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💬 Response

Interesting — the page still showed "19 May 2025 / 3 Clear" as late as 31 December 2025. This is a critical finding: the tracker was NOT updated between May 2025 and end of 2025. The jump to 9 Clear happened sometime in 2026. Let me pinpoint when the update occurred by checking early-to-mid 2026 snapshots.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content:\n\n**Last update date:** 19 May
2025\n\n**Classification of EU Member States:**\n- **Clear (both authorities designated):** 3 member states\n- **Partial clarity:** 10 member states  \n- **Unclear:** 14 member states\n\n**Clear
countries (both market surveillance and notifying authorities designated):**\n1. Denmark\n2. Hungary\n3. Luxembourg\n\nNote: The document mentions these numbers explicitly in the section \"Timelines
and status of implementation\" but Table 1 referenced in the text appears incomplete in the provided content, showing only the table header without the detailed breakdown.\n\n**Relevant links:**\n-
[Full Implementation Timeline for AI Act](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/implementation-timeline/)\n- [Commission consolidated list of
authorities](http://web.archive.org/web/20260204152334/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Article 3 -
Definitions](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/article/3/)\n- [Article 28 - Notifying
authorities](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/article/28/)\n- [Article 70 - National competent
authorities](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/article/70/)\n- [Article 77 - National public authorities protecting fundamental
rights](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/article/77/)\n- [Article 113 - Implementation
deadlines](http://web.archive.org/web/20260204152334/https://artificialintelligenceact.eu/article/113/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "url": "http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content provided:\n\n**Last update date:** 19 May
2025\n\n**Classification of EU Member States:**\n- **Clear** (both authorities designated): **3 member states**\n  - Denmark\n  - Hungary  \n  - Luxembourg\n\n- **Partial clarity** (pending proposals
or one authority appointed): **10 member states**\n\n- **Unclear** (no authorities designated): **14 member states**\n\n**Note:** The content shows that as of the last update date, Hungary and Italy
had not yet designated fundamental rights authorities (Art 77), but Hungary is still counted as \"Clear\" for the competent authorities (market surveillance and notifying).\n\n**Relevant links:**\n-
[Commission consolidated list of authorities](http://web.archive.org/web/20260322105019/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Full Implementation
Timeline for the AI Act](http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/implementation-timeline/)\n- [AI Act Article
3](http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/article/3/)\n- [AI Act Article
70](http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/article/70/)\n- [AI Act Article
77](http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/article/77/)\n- [AI Act Article
113](http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/article/113/)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💬 Response

Still "19 May 2025 / 3 Clear" as of 22 March 2026. The update to the new dataset (9 Clear, 17 June 2026) must have happened between 22 March 2026 and 16 June 2026. Let me check the remaining 2026 snapshots to find exactly when the tracker was substantially revised.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/web/20260429053837/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260429053837/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content:\n\n**Last Update Date:** 19 May
2025\n\n**Classification of EU Member States:**\n- **Clear** (both authorities designated): **3 member states**\n- **Partial clarity** (pending proposals or one authority appointed): **10 member
states**\n- **Unclear** (no authorities designated): **14 member states**\n\n**The 3 \"Clear\" countries are:**\n1. Denmark\n2. Hungary\n3. Luxembourg\n\nNote: The content references Table 1 showing
these overall statistics but Table 2 (which would show the detailed breakdown by country) appears to be cut off in the provided text, so the specific list of which countries fall into partial/unclear
categories is not fully visible.\n\n**Relevant links:**\n- [Implementation Timeline](http://web.archive.org/web/20260429053837/https://artificialintelligenceact.eu/implementation-timeline/)\n-
[Commission consolidated list of authorities](http://web.archive.org/web/20260429053837/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [AI Act
Newsletter](http://web.archive.org/web/20260429053837/https://artificialintelligenceact.substack.com/)\n- [Article 70 (National Competent
Authorities)](http://web.archive.org/web/20260429053837/https://artificialintelligenceact.eu/article/70/)\n- [Article 77 (Fundamental Rights
Authorities)](http://web.archive.org/web/20260429053837/https://artificialintelligenceact.eu/article/77/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "url": "http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear (both market surveillance and notifying authorities designated), how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content:\n\n**Last update date:** 19 May
2025\n\n**Classification of EU Member States:**\n- **Clear (both authorities designated):** 3 member states\n- **Partial clarity:** 10 member states  \n- **Unclear:** 14 member states\n\n**Countries
classified as \"Clear\":**\nThe content mentions \"three Member States have designated both notifying and market surveillance authorities\" but does not explicitly list which three countries achieve
\"Clear\" status in the text provided. \n\nHowever, based on the detailed table information, the countries that appear to have both authorities designated include:\n- **Denmark** (designated
coordinating market surveillance authority via Danish Agency for Digital Government)\n- **Hungary** (Minister for National Economy for market surveillance; National Accreditation Authority as
notifying authority per May 2025 resolution)\n- **Luxembourg** (National Commission for Data Protection designated; draft law outlines three notifying authorities)\n\nNote: The exact \"Clear\"
designation isn't explicitly stated in the table format provided, but these appear most complete based on the descriptions.\n\n**Relevant links:**\n- [Commission consolidated list of
authorities](http://web.archive.org/web/20260604075359/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Full Implementation
Timeline](http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/implementation-timeline/)\n- [AI Act Article
70](http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/article/70/)\n- [AI Act Article
77](http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/article/77/)\n- [AI Act Article
113](http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/article/113/)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💬 Response

Critical finding confirmed: Even as late as 4 June 2026, the page still showed "19 May 2025 / 3 Clear". The complete overhaul to the new methodology (9 Clear, 12 Partial, 6 Unclear, dated 17 June 2026) happened between 4 June 2026 and 16 June 2026. Let me verify the 16 June 2026 snapshot to confirm the jump, and check the 3 July 2026 snapshot to see if anything changed after 17 June.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear, how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content:\n\n**Last update date:** 19 May
2025\n\n**Member State Classifications:**\n- **Clear:** 3 member states\n- **Partial clarity:** 10 member states  \n- **Unclear:** 14 member states\n\n**Clear countries:** The specific countries with
\"clear\" status are not explicitly listed in the provided text. The text states \"three Member States have designated both notifying and market surveillance authorities ('clear' in the table below)\"
but the actual table identifying which countries fall into this category is referenced but not fully shown in the extracted content.\n\n**Note:** Regarding fundamental rights authorities (Article 77),
the text states that as of the last update, Hungary and Italy had not yet designated authorities, while other member states had done so by the November 2, 2024 deadline.\n\n**Relevant links:**\n-
[Implementation Timeline](http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/implementation-timeline/)\n- [Commission consolidated list of
authorities](http://web.archive.org/web/20260616043104/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [AI Act
newsletter](http://web.archive.org/web/20260616043104/https://artificialintelligenceact.substack.com/)\n- [Future of Life
Institute](http://web.archive.org/web/20260616043104/https://futureoflife.org/)", "title": "Overview of all AI Act National Implementation Plans"}
```

```json
{
  "url": "http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/",
  "prompt": "What is the last update date shown on the page? How many EU member states are classified as Clear, how many Partial clarity, and how many Unclear? Give exact numbers and list the Clear countries."
}
```

### 📋 Result

```
{"url": "http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/", "content": "Based on the content provided:\n\n**Last update date:** 17 June
2026\n\n**Classification of EU Member States (27 total):**\n- **Clear:** 9 member states\n- **Partial clarity:** 12 member states  \n- **Unclear:** 6 member states\n\n**Clear countries (9):**\n1.
Cyprus\n2. Denmark\n3. Finland\n4. Hungary\n5. Ireland\n6. Italy\n7. Lithuania\n8. Slovenia\n9. Spain\n\n**Relevant links:**\n- [Implementation Timeline for all key dates and
deadlines](http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/implementation-timeline/)\n- [Commission's consolidated list of
authorities](http://web.archive.org/web/20260703043308/https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)\n- [Commission's list of fundamental rights protection
authorities](http://web.archive.org/web/20260703043308/https://digital-strategy.ec.europa.eu/en/policies/fundamental-rights-protection-authorities-ai-act)\n- [AI Act Article
3](http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/article/3/)\n- [AI Act Article
70](http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/article/70/)\n- [AI Act Article
75](http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/article/75/)\n- [AI Act Article
77](http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/article/77/)", "title": "Overview of all AI Act National Implementation Plans"}
```

## 💬 Response

I now have the complete picture. Key findings:

- **16 June 2026 snapshot**: still "19 May 2025 / 3 Clear" (old page)
- **17 June 2026**: major overhaul → **9 Clear, 12 Partial, 6 Unclear** (new methodology)
- **3 July 2026 snapshot**: confirms 9 Clear (though the Clear list differs slightly — Cyprus/Spain listed vs Malta/Slovenia in June — showing minor churn but count stable at 9)

The crucial insight is that the "Clear" count is a **measure of how the tracker's authors have updated the page**, not a real-time continuous metric. The tracker was essentially frozen at "3 Clear (19 May 2025)" from May 2025 all the way through 16 June 2026 (~13 months), then jumped to 9 Clear in a single overhaul on 17 June 2026 that reflected accumulated real-world designations.

Let me do a couple of validation checks on the actual underlying reality (Commission's designations) to understand the real trajectory versus the tracker's update cadence.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "EU AI Act member states designated market surveillance notifying authorities 2 August 2025 deadline how many missed"
}
```

### 📋 Result

```
{"query": "EU AI Act member states designated market surveillance notifying authorities 2 August 2025 deadline how many missed", "results": [{"title": "Market Surveillance Authorities under the AI Act
| Shaping Europe\u2019s digital future", "url": "https://digital-strategy.ec.europa.eu/en/policies/market-surveillance-authorities-under-ai-act", "snippet": "Market surveillance authorities supervise
and enforce the rules related to AI systems in the EU Member States.\nThe AI Office and the national market surveillance authorities are responsible for implementing, supervising and enforcing the AI
Act. Market surveillance authorities have powers to investigate and enforce compliance with the rules for AI systems, including prohibitions and rules for high-risk AI, in line with [EU market
surveillance rules](https://single-market-economy.ec.europa.eu/sin", "api_data": null, "hint": null}, {"title": "Governance and enforcement of the AI Act | Shaping Europe\u2019s digital future",
"url": "https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement", "snippet": "The European AI Office and the national market surveillance authorities are responsible for
implementing, supervising and enforcing the AI Act.\nThe AI Act\u2019s governance will be steered by three advisory bodies:\n- the\n[European Artificial Intelligence Board](https://digital-
strategy.ec.europa.eu/en/policies/ai-board), composed of representatives from the EU Member States, - the\n[Scientific Panel](https://digital-strategy.ec.europa.eu/en/policies/ai-scientific-panel),
composed of independent expert", "api_data": null, "hint": null}, {"title": "Overview of all AI Act National Implementation Plans | EU Artificial Intelligence Act", "url":
"https://artificialintelligenceact.eu/national-implementation-plans/", "snippet": "Last update: 17 June 2026\nSince the AI Act entered into force on 1 August 2024, the focus for Member States has
shifted to national implementation. One of the first tasks for Member States is to designate the relevant authorities. This post gives an overview of the national authorities designated under the AI
Act and what we know about the national implementation plans.*\nThis resource is a work in progress and will be updated when new information is available. Please help us ensure the completen",
"api_data": null, "hint": null}, {"title": "Preparing for enforcement: A Guide to the EU AI Act's market surveillance authorities : Clyde & Co", "url":
"https://www.clydeco.com/en/insights/2025/05/preparing-for-enforcement-a-guide-to-the-eu-ai-act", "snippet": "Preparing for enforcement: A Guide to the EU AI Act's market surveillance
authorities\n-\nMarket Insight 13 May 2025 13 May 2025\n-\nUK & Europe\nAs the EU\u2019s AI Act moves toward full implementation, understanding the evolving governance landscape is essential for
companies subject to the regulation. One of the AI Act\u2019s cornerstones is its multi-stakeholder governance \u2013 different bodies are tasked with ensuring compliance, enforcing rules, and
coordinating across the EU. With the deadline to establish", "api_data": null, "hint": null}, {"title": "Article 70: Designation of national competent authorities and a single point of contact | AI
Act Service Desk", "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-70", "snippet": "Article 70: Designation of national competent authorities and a single point of
contact\nSummary\nEach Member State must appoint at least one notifying authority and one market surveillance authority to implement the AI Act, ensuring they operate independently. The market
surveillance authority chosen by each Member State will act as the single point of contact. Member States must provide these authorities with ample resources, including knowledgeable staff in AI and
related fields, and check reso", "api_data": null, "hint": null}, {"title": "AI Act: Overview of EU Market Surveillance Authorities", "url": "https://cms.law/en/deu/legal-updates/there-are-
around-2-000-ai-market-surveillance-authorities-in-the-eu", "snippet": "There are around 2,000 AI market surveillance authorities in the
EU\n![](/assets/build/images_not_versioned/cms/StageArticleDefaultBG.jpg?v=4.49.0)\nThe AI Act is a uniform regulation on AI applicable to all 27 Member States, but it will have to be interpreted,
applied and enforced by around 2,000 market surveillance authorities and by 208 fundamental rights protection authorities, each one with a possible different interpretation.\nIt would be of course
easier to have a unique AI regulator and mar", "api_data": null, "hint": null}, {"title": "EU AI Act Regulatory Directory | IAPP", "url": "https://iapp.org/resources/article/eu-ai-act-regulatory-
directory", "snippet": "EU AI Act Regulatory Directory\n![](https://images.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt46a4119fb1d71f6d/69021a77a53b8c642a9298c8/eu_ai_act_regulatory_directory_thu
mbnail.jpg?width=3840&quality=75&format=pjpg&auto=webp)\nThis tool identifies competent authorities responsible for the implementation and enforcement of the EU AI
Act.\n![](https://images.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt46a4119fb1d71f6d/69021a77a53b8c642a9298c8/eu_ai_act_regulatory_directory_thumbnail.jpg?wi", "api_data": null, "hint": null},
{"title": "AI Act | Shaping Europe's digital future - European Union", "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai", "snippet": "The AI Act is the first-ever
legal framework on AI, which addresses the risks of AI and positions Europe to play a leading role globally.\nThe [AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)
(Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence) is the first-ever comprehensive legal framework on AI worldwide. The aim of the rules is to foster trustworthy AI in
Europe. For any questions on the AI Act, check out the [AI Act Single Inform", "api_data": null, "hint": null}, {"title": "EU AI Act Regulatory Directory - PrivacyEngine Data Protection Software and
Solutions", "url": "https://www.privacyengine.io/eu-ai-act-regulatory-directory/", "snippet": "PrivacyEngine\u2019s AI Act Authority Tracker provides a clear, country-by-country view of the competent
authorities responsible for implementing and enforcing the EU Artificial Intelligence Act. It covers national competent authorities, market surveillance and notifying authorities, as well as national
bodies protecting fundamental rights, and indicates each authority\u2019s current designation status: officially designated, identified in draft legislation or other formal communications but pending
desig", "api_data": null, "hint": null}, {"title": "State of the Act: EU AI Act implementation in key Member States | Technology's Legal Edge", "url":
"https://www.technologyslegaledge.com/2025/11/state-of-the-act-eu-ai-act-implementation-in-key-member-states/", "snippet": "The dream of directly effective supra-national legislation, applying in
exactly the same way in each EU Member State: an EU Regulation should (in theory) provide the same protections in the same way at the same time to all EU citizens. As is ever the case, theory and
reality rarely align, and the EU AI Act is proving to be a case in point. While the core text Regulation EU 2024/1689 is rolling out to the same timetable in all Member States, there are many steps
that Member States or their design", "api_data": null, "hint": null}]}
```

```json
{
  "query": "EU AI Act national competent authorities designation 2026 how many member states completed Spain Italy Ireland"
}
```

### 📋 Result

```
{"query": "EU AI Act national competent authorities designation 2026 how many member states completed Spain Italy Ireland", "results": [{"title": "Overview of all AI Act National Implementation Plans
| EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/national-implementation-plans/", "snippet": "Last update: 17 June 2026\nSince the AI Act entered into force on 1 August
2024, the focus for Member States has shifted to national implementation. One of the first tasks for Member States is to designate the relevant authorities. This post gives an overview of the national
authorities designated under the AI Act and what we know about the national implementation plans.*\nThis resource is a work in progress and will be updated when new information is available. Please
help us ensure the completen", "api_data": null, "hint": null}, {"title": "Article 70: Designation of national competent authorities and a single point of contact | AI Act Service Desk", "url":
"https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-70", "snippet": "Article 70: Designation of national competent authorities and a single point of contact\nSummary\nEach Member State must
appoint at least one notifying authority and one market surveillance authority to implement the AI Act, ensuring they operate independently. The market surveillance authority chosen by each Member
State will act as the single point of contact. Member States must provide these authorities with ample resources, including knowledgeable staff in AI and related fields, and check reso", "api_data":
null, "hint": null}, {"title": "EU AI Act Regulatory Directory | IAPP", "url": "https://iapp.org/resources/article/eu-ai-act-regulatory-directory", "snippet": "EU AI Act Regulatory Directory\n![](http
s://images.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt46a4119fb1d71f6d/69021a77a53b8c642a9298c8/eu_ai_act_regulatory_directory_thumbnail.jpg?width=3840&quality=75&format=pjpg&auto=webp)\nThis
tool identifies competent authorities responsible for the implementation and enforcement of the EU AI
Act.\n![](https://images.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt46a4119fb1d71f6d/69021a77a53b8c642a9298c8/eu_ai_act_regulatory_directory_thumbnail.jpg?wi", "api_data": null, "hint": null},
{"title": "Who Governs AI in the EU? A Breakdown of Authorities in the EU AI Act", "url": "https://www.unesco.org/en/articles/who-governs-ai-eu-breakdown-authorities-eu-ai-act", "snippet":
"Article\nWho Governs AI in the EU? A Breakdown of Authorities in the EU AI Act\nThis also requires a robust enforcement mechanism to protect the potential impact of AI on human rights. The UNESCO
Recommendation advocates for anticipatory governance that proactively monitors the ongoing impacts of AI systems and addresses potential risks before they materialise. During the deployment phase, it
is crucial to continuously assess whether the AI system remains safe, ethical, and compliant with regulato", "api_data": null, "hint": null}, {"title": "Who Oversees AI in the EU? The Designation of
National Competent Authorities under the EU AI Act - MIAI", "url": "https://ai-regulation.com/designation-of-national-competent-authorities-under-the-eu-ai-act/", "snippet": "This study seeks to
provide an overview of current progress in the designation of national competent authorities, and to analyse how national governance architectures are being developed. The study shows that one week
prior to the deadline, the majority of member states were behind schedule. Progress seems to have been fragmented, with many states not having made an announcement about their designation choices, or
not legally enshrining their designation decisions. A few draft governance framewo", "api_data": null, "hint": null}, {"title": "The AI Act Explorer | EU Artificial Intelligence Act", "url":
"https://artificialintelligenceact.eu/ai-act-explorer/", "snippet": "BETA \ud83d\udd14 New: Try the [new AI Act Explorer](https://explorer.artificialintelligenceact.eu/), rebuilt from the ground up
for 2026. Read the official text in all 24 EU languages, including the 'Code of Practice' and other documents. Compare languages side-by-open, open items in a 'side peek' for easy reference, and share
URLs direct to an individual paragraph. Custom AI chatbot to answer your questions (coming soon). [Go to the new AI Act Explorer \u2192](https://explorer.artificialintelligenceact.eu/)\nT",
"api_data": null, "hint": null}, {"title": "Regulation (EU) 2026/XXXX of the European Parliament and of the Council on harmonised rules for Cloud and Artificial Intelligence Development (Cloud and AI
Development Act) - European Union | Regulations.AI - The Site on AI Laws and Regulations | Regulations.ai", "url": "https://regulations.ai/regulations/RAI-EU-NA-RE2026X-2026", "snippet": "EU Cloud and
AI Development Act\nRegulation (EU) 2026/XXXX of the European Parliament and of the Council on harmonised rules for Cloud and Artificial Intelligence Development (Cloud and AI Development
Act)\nEuropean Union\nRAI-EU-NA-RE2026X-2026Regulation 2026/XXXX\nThe EU Cloud and AI Development Act strengthens Europe's digital sovereignty by establishing a cloud sovereignty framework and
boosting AI infrastructure.\nSummary\n[Read full text \u2197](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CEL", "api_data": null, "hint": null}, {"title": "Building a Centralised National AI
Authority", "url": "https://www.interface-eu.org/publications/poland-ai-act-implementation", "snippet": "Policy Brief\nBuilding a Centralised National AI Authority\nPoland's AI Act Implementation
Model in a European Context\nExecutive Summary\nThe EU Artificial Intelligence Act (AI Act) leaves Member States with significant discretion in designing their national enforcement structures. This
paper examines Poland\u2019s approach, one of the most structurally distinctive among the EU-27: the creation of a new, centralised supervisory authority, the Commission for the Development and Safety
of Artificial Intel", "api_data": null, "hint": null}, {"title": "Article 70: Designation of National Competent Authorities and Single Point of Contact | EU Artificial Intelligence Act", "url":
"https://artificialintelligenceact.eu/article/70/", "snippet": "1. Each Member State shall establish or designate as national competent authorities at least one notifying authority and at least one
market surveillance authority for the purposes of this Regulation. Those national competent authorities shall exercise their powers independently, impartially and without bias so as to safeguard the
objectivity of their activities and tasks, and to ensure the application and implementation of this Regulation. The members of those authorities shall refrain from any", "api_data": null, "hint":
null}, {"title": "Federal Government draft bill to implement EU Artificial Intelligence Act | Gleiss Lutz", "url": "https://www.gleisslutz.com/en/know-how/federal-government-draft-bill-implement-eu-
artificial-intelligence-act", "snippet": "![](/sites/default/files/styles/mq_media_21_9_1400_xl_2_full/public/2024-03/sebastian-pichler-25154-unsplash.jpg?h=0d0a9c2a&itok=aTt754JV)\nThe AI Act
(Regulation (EU) 2024/1689) \u2013 the EU\u2019s first comprehensive framework for the development, placing on the market and use of AI systems \u2013 entered into force on 1 August 2024 and will
apply directly from 2 August 2026. Member States were required to comply with certain implementation obligations and define competent authorities and enforcement powers ", "api_data": null, "hint":
null}, {"title": "State of the Act: EU AI Act implementation in key Member States | Technology's Legal Edge", "url": "https://www.technologyslegaledge.com/2025/11/state-of-the-act-eu-ai-act-
implementation-in-key-member-states/", "snippet": "The dream of directly effective supra-national legislation, applying in exactly the same way in each EU Member State: an EU Regulation should (in
theory) provide the same protections in the same way at the same time to all EU citizens. As is ever the case, theory and reality rarely align, and the EU AI Act is proving to be a case in point.
While the core text Regulation EU 2024/1689 is rolling out to the same timetable in all Member States, there are many steps that Member States or their design", "api_data": null, "hint": null},
{"title": "EU AI Act Enforcement: August 2026 Compliance Deadline Explained | ai | informed, clearly", "url": "https://informedclearly.com/en/ai/55795/eu-ai-act-compliance-deadline-2026", "snippet":
"On August 2, 2026, the European Union's Artificial Intelligence Act (Regulation 2024/1689) enters its most consequential enforcement phase, mandating binding compliance rules for high-risk AI systems
and general-purpose AI models. With penalties reaching \u20ac35 million or 7% of global annual turnover \u2014 exceeding even the GDPR's maximum fines \u2014 the world's first comprehensive AI
regulation creates a 'Brussels Effect' that forces technology firms worldwide to restructure their AI development, deploym", "api_data": null, "hint": null}, {"title": "EU AI Act August 2026: your
compliance countdown | RAIL", "url": "https://responsibleailabs.ai/knowledge-hub/articles/eu-ai-act-august-2026-compliance", "snippet": "On August 2, 2026, the EU AI Act's most consequential
obligations take effect: Annex III high-risk AI system requirements, Article 50 transparency obligations, conformity assessments, CE marking, and AI Office enforcement powers. As of April 2026, 78% of
organizations have not taken meaningful steps toward compliance.\nKey Takeaways\n>\n- The August 2, 2026, deadline is 120 days away. It covers high-risk AI systems (Articles 9--15), Article 50
transparency, conformity assessments, and CE marking.\n-", "api_data": null, "hint": null}, {"title": "EU AI Act August 2026: your compliance countdown | RAIL Score Knowledge Hub", "url":
"https://knowledge.responsibleailabs.ai/knowledge-hub/governance/eu-ai-act-august-2026-compliance", "snippet": null, "api_data": null, "hint": null}, {"title": "EU AI Act Enforcement Timeline: 2025 to
2027", "url": "https://compliancestack.ai/penalties/eu-ai-act/enforcement-timeline", "snippet": "EU AI Act Enforcement Timeline: What's Already in Force and What's Coming\nLast updated: 2026-07-07
\u2014 ComplianceStack Editorial Team\nRegulation (EU) 2024/1689 entered into force on August 1, 2024 \u2014 but 'in force' does not mean 'enforceable.' The Act uses a phased application schedule
spread across three years, with different obligations becoming binding on different dates. Companies that assume the EU AI Act is a 2026 problem are already wrong: prohibited practices have been
enforceable since Feb", "api_data": null, "hint": null}, {"title": "AI laws and regulations in Spain| CMS Expert Guide", "url": "https://cms.law/en/int/expert-guides/ai-regulation-scanner/spain",
"snippet": "AI laws and regulation in Spain\n![](https://cms.law/var/dpcontent/storage/images/_aliases/cmsArticleStageBg/3/2/9/4/10914923-4-eng-GB/30dc44481055-Madrid-
Spain-1-.jpg?v=4)\njurisdiction\n-\n[Albania](https://cms.law#) -\n[Austria](https://cms.law#) -\n[Belgium](https://cms.law#) -\n[Bosnia and Herzegovina](https://cms.law#)
-\n[Brazil](https://cms.law#) -\n[Bulgaria](https://cms.law#) -\n[Chile](https://cms.law#) -\n[China](https://cms.law#) -\n[Colombia](https://cms.law#) -\n[Czech Republic](https://cms.la", "api_data":
null, "hint": null}]}
```

## 💬 Response

I have enough to complete a thorough analysis. The context confirms that at the 2 August 2025 deadline, the majority of member states were behind schedule, and the tracker itself only reflected 3 Clear until its June 2026 overhaul. I have all the data needed for the trajectory. Let me write up the synthesis.

## Research Report: History of the artificialintelligenceact.eu National Implementation Plans Tracker — "Clear" Classification Trajectory

### Executive Summary

The critical, and somewhat counterintuitive, finding is that the "Clear" count on this tracker is **not a continuously updated real-time metric**. It is a manually maintained resource by the Future of Life Institute that was **frozen at "3 Clear" (dated 19 May 2025) for approximately 13 months**, then jumped to **9 Clear** in a single comprehensive overhaul on **17 June 2026**. Any projection of the Clear count for 31 August 2026 depends far more on the tracker's editorial update cadence than on a smooth underlying rate of member-state designations.

### The Documented Trajectory (from Wayback Machine snapshots)

| Snapshot date (capture) | "Last update" shown on page | Clear | Partial | Unclear |
|---|---|---|---|---|
| 2 Aug 2025 | 19 May 2025 | 3 | 10 | 14 |
| 5 Sep 2025 | 19 May 2025 | 3 | 10 | 14 |
| 7 Nov 2025 | 19 May 2025 | 3 | 10 | 14 |
| 31 Dec 2025 | 19 May 2025 | 3 | 10 | 14 |
| 4 Feb 2026 | 19 May 2025 | 3 | 10 | 14 |
| 22 Mar 2026 | 19 May 2025 | 3 | 10 | 14 |
| 29 Apr 2026 | 19 May 2025 | 3 | 10 | 14 |
| 4 Jun 2026 | 19 May 2025 | 3 | 10 | 14 |
| 16 Jun 2026 | 19 May 2025 | 3 | 10 | 14 |
| **17 Jun 2026** | **17 Jun 2026** | **9** | **12** | **6** |
| 3 Jul 2026 | 17 Jun 2026 | 9 | 12 | 6 |

Note: Earlier 2024/early-2025 snapshots show the page was being built out; the "3 Clear" methodology (three Member States — Denmark, Hungary, Luxembourg — with both notifying and market surveillance authorities) was in place from the 19 May 2025 update.

### Key Observations About the Trend/Rate

1. **The count is step-wise, not continuous.** The tracker went from 3 → 9 in one discrete editorial revision. Between May 2025 and mid-June 2026 there was zero movement in the recorded numbers. This is a data-vintage artifact, not a reflection of no real-world progress.

2. **The 17 June 2026 overhaul changed the methodology and the total.** The old version tracked ~27 states with 3/10/14 = 27. The new version explicitly frames all 27 states as 9 Clear / 12 Partial / 6 Unclear. It also added new "Clear" entrants (Cyprus, Finland, Ireland, Italy, Lithuania, and others) reflecting designations that had accumulated in reality across late 2025 / early-to-mid 2026 but had not been logged.

3. **There is minor churn within the "Clear" list even at a stable count of 9.** The 3 July 2026 snapshot lists the 9 Clear states as Cyprus, Denmark, Finland, Hungary, Ireland, Italy, Lithuania, Slovenia, **Spain**; the live 17 June page (via direct fetch) lists Cyprus, Denmark, Finland, Hungary, Ireland, Italy, Lithuania, **Malta, Slovenia**. The **count stayed at 9** while individual members shifted — indicating the number is more stable than the specific membership.

4. **Underlying reality vs. tracker.** Independent reporting (MIAI/ai-regulation.com) noted that "one week prior to the [2 Aug 2025] deadline, the majority of member states were behind schedule." So the legal deadline (2 Aug 2025) was widely missed, and real-world designations trickled in over the following year. The tracker's June 2026 jump to 9 is a batch "catch-up" reflecting this accumulated reality.

### Implications for Projecting 31 August 2026 (reporting trajectory only, not a forecast)

- The most recent data point (3 July 2026) confirms the count is **9 and stable** since the 17 June overhaul.
- The tracker's update history shows **long periods of dormancy punctuated by large batch revisions**. Since the last overhaul was just ~3 weeks before the current date (7 July 2026), a further revision before 31 August 2026 is plausible but not guaranteed based on historical cadence (updates were infrequent — roughly the major ones observed: build-out late 2024, 19 May 2025, 17 June 2026).
- The real-world driver is the **2 August 2026 deadline** for high-risk AI obligations and sandboxes, which creates pressure for remaining states to finalize designations. If the tracker is refreshed around that deadline, additional states currently in "Partial" (e.g., Spain, Germany, Poland, Netherlands with draft laws pending) could move to Clear.
- Direction of travel is **upward** (3 → 9), with 12 states in "Partial" representing the near-term pipeline of potential future "Clear" additions.

### Data Caveats

- Counts derive from LLM extraction of archived HTML; the 3/10/14 and 9/12/6 splits are consistent and confirmed across multiple snapshots.
- The "19 May 2025" internal date persisted on the page for over a year — this is the single most important caveat: the tracker's displayed status lags real-world designations substantially.
- No snapshot exists between 4 June 2026 and 16 June 2026 showing an intermediate value; the transition from 3 to 9 is confirmed to have occurred between the 16 June (still 3) and 17 June (9) captures.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "The \"Clear\" count on the artificialintelligenceact.eu National Implementation Plans tracker is not a continuously updated metric. It is a manually maintained Future of Life Institute resource that was frozen at \"3 Clear\" (page-dated 19 May 2025) for roughly 13 months, then jumped to 9 Clear in a single comprehensive overhaul dated 17 June 2026.\n\nDOCUMENTED TRAJECTORY (from Wayback Machine snapshots of the page's displayed status):\n- 2 Aug 2025 capture: 3 Clear / 10 Partial / 14 Unclear (page \"last update\" = 19 May 2025)\n- 5 Sep 2025: 3 / 10 / 14 (19 May 2025)\n- 7 Nov 2025: 3 / 10 / 14 (19 May 2025)\n- 31 Dec 2025: 3 / 10 / 14 (19 May 2025)\n- 4 Feb 2026: 3 / 10 / 14 (19 May 2025)\n- 22 Mar 2026: 3 / 10 / 14 (19 May 2025)\n- 29 Apr 2026: 3 / 10 / 14 (19 May 2025)\n- 4 Jun 2026: 3 / 10 / 14 (19 May 2025)\n- 16 Jun 2026: 3 / 10 / 14 (still 19 May 2025)\n- 17 Jun 2026: 9 Clear / 12 Partial / 6 Unclear (major overhaul; new methodology)\n- 3 Jul 2026: 9 / 12 / 6 (17 June 2026)\n\nKEY INSIGHTS:\n1. The metric is step-wise, not continuous: it went 3 -> 9 in one discrete editorial revision, with zero movement recorded for ~13 months. This is a data-vintage/update-cadence artifact, not an absence of real-world progress.\n2. The transition to 9 is bounded precisely between the 16 June 2026 snapshot (still 3) and 17 June 2026 (9).\n3. Within a stable count of 9 there is minor churn in membership (e.g., 3 July snapshot Clear list includes Spain; the live 17 June page lists Malta instead), but the count held at 9.\n4. Real-world designations lagged the legal deadline (2 August 2025), which the majority of member states missed; the June 2026 overhaul was a batch catch-up.\n5. Direction of travel is upward (3 -> 9), with 12 states in \"Partial\" forming the near-term pipeline. The 2 August 2026 high-risk/sandbox deadline creates pressure that could prompt further tracker revisions.\n\nCAVEAT FOR PROJECTION: The count as of the latest snapshot (3 July 2026) is 9 and stable. Because the tracker updates in infrequent large batches rather than smoothly, projecting 31 August 2026 depends heavily on whether the maintainers issue another revision (plausibly around the 2 Aug 2026 deadline). This is reporting of trajectory only, not a probabilistic forecast.</answer>\n<parameter name=\"key_facts\">[\"The tracker's 'Clear' count was frozen at 3 (page-dated 19 May 2025) from at least August 2025 through 16 June 2026 - roughly 13 months of no change.\", \"On 17 June 2026 the tracker was comprehensively overhauled to 9 Clear / 12 Partial / 6 Unclear (27 EU member states).\", \"The 3->9 jump occurred as a single discrete editorial revision, bounded between the 16 June 2026 snapshot (still 3) and 17 June 2026 (9).\", \"The 3 Clear states under the old methodology were Denmark, Hungary, and Luxembourg.\", \"The 9 Clear states as of 17 June 2026 (direct fetch): Cyprus, Denmark, Finland, Hungary, Ireland, Italy, Lithuania, Malta, Slovenia.\", \"The 3 July 2026 snapshot confirms 9 Clear but lists a slightly different set (Spain instead of Malta), showing membership churn while the count stayed at 9.\", \"The most recent confirmed data point (3 July 2026) shows the count stable at 9 Clear / 12 Partial / 6 Unclear.\", \"Independent analysis (MIAI/ai-regulation.com) reports the majority of member states were behind schedule one week before the 2 August 2025 legal deadline.\", \"The tracker updates in infrequent large batches, not continuously, so the displayed status lags real-world authority designations substantially.\", \"The 2 August 2026 deadline for high-risk AI obligations and regulatory sandboxes creates pressure that could trigger a further tracker revision moving Partial states to Clear.\"]",
  "sources": [
    {
      "url": "https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "Overview of all AI Act National Implementation Plans",
      "domain": "artificialintelligenceact.eu",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update: 17 June 2026. Clear: 9, Partial clarity: 12, Unclear: 6 (27 EU member states)."
    },
    {
      "url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 2 Aug 2025)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear."
    },
    {
      "url": "http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 31 Dec 2025)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 19 May 2025; 3 Clear (Denmark, Hungary, Luxembourg), 10 Partial, 14 Unclear."
    },
    {
      "url": "http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 22 Mar 2026)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear."
    },
    {
      "url": "http://web.archive.org/web/20260604075359/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 4 Jun 2026)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear (still old data)."
    },
    {
      "url": "http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 16 Jun 2026)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 19 May 2025; 3 Clear, 10 Partial, 14 Unclear (day before overhaul)."
    },
    {
      "url": "http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/",
      "title": "National Implementation Plans (archived 3 Jul 2026)",
      "domain": "web.archive.org",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Last update 17 June 2026; 9 Clear, 12 Partial, 6 Unclear."
    },
    {
      "url": "https://ai-regulation.com/designation-of-national-competent-authorities-under-the-eu-ai-act/",
      "title": "Who Oversees AI in the EU? The Designation of National Competent Authorities",
      "domain": "ai-regulation.com",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "One week prior to the deadline, the majority of member states were behind schedule."
    },
    {
      "url": "https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement",
      "title": "Governance and enforcement of the AI Act",
      "domain": "digital-strategy.ec.europa.eu",
      "accessed_at": "2026-07-07T00:00:00Z",
      "snippet": "Commission consolidated list of national authorities designated under the AI Act."
    }
  ],
  "data_points": [
    {
      "metric": "Clear member states (tracker, page-dated 19 May 2025)",
      "value": 3,
      "unit": "member states",
      "as_of": "2025-08-02",
      "source_url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Clear member states (tracker, page-dated 19 May 2025)",
      "value": 3,
      "unit": "member states",
      "as_of": "2025-12-31",
      "source_url": "http://web.archive.org/web/20251231214055/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Clear member states (tracker, page-dated 19 May 2025)",
      "value": 3,
      "unit": "member states",
      "as_of": "2026-03-22",
      "source_url": "http://web.archive.org/web/20260322105019/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Clear member states (tracker, page-dated 19 May 2025)",
      "value": 3,
      "unit": "member states",
      "as_of": "2026-06-16",
      "source_url": "http://web.archive.org/web/20260616043104/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Clear member states (tracker, page-dated 17 June 2026)",
      "value": 9,
      "unit": "member states",
      "as_of": "2026-06-17",
      "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Clear member states (tracker, page-dated 17 June 2026)",
      "value": 9,
      "unit": "member states",
      "as_of": "2026-07-03",
      "source_url": "http://web.archive.org/web/20260703043308/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Partial clarity member states (tracker)",
      "value": 12,
      "unit": "member states",
      "as_of": "2026-06-17",
      "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Unclear member states (tracker)",
      "value": 6,
      "unit": "member states",
      "as_of": "2026-06-17",
      "source_url": "https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Partial clarity member states (tracker, old methodology)",
      "value": 10,
      "unit": "member states",
      "as_of": "2025-08-02",
      "source_url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"
    },
    {
      "metric": "Unclear member states (tracker, old methodology)",
      "value": 14,
      "unit": "member states",
      "as_of": "2025-08-02",
      "source_url": "http://web.archive.org/web/20250802104033/https://artificialintelligenceact.eu/national-implementation-plans/"
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's the key takeaway for your forecasting purpose:

**The "Clear" count is a step-function driven by editorial updates, not a smooth real-time metric.** The tracker sat at **3 Clear (page-dated 19 May 2025) for ~13 months**, then jumped to **9 Clear** in a single overhaul on **17 June 2026**. The most recent snapshot (3 July 2026) confirms it's stable at 9.

**Verified trajectory:**
- Aug 2025 → June 16, 2026: locked at **3 Clear** (page never refreshed from its 19 May 2025 vintage)
- June 17, 2026: overhaul to **9 Clear / 12 Partial / 6 Unclear**
- July 3, 2026: still **9 Clear**

**Implications for projecting 31 August 2026:**
- Direction is upward (3→9), but the movement happens in infrequent batch revisions, not continuously.
- The last overhaul was only ~3 weeks before today (7 July 2026), so 9 is the current stable value.
- A further revision is plausible around the **2 August 2026** high-risk/sandbox deadline, which could push some of the 12 "Partial" states (Spain, Germany, Poland, Netherlands, etc.) into Clear — but historically the maintainers update rarely, so 9 could also persist through 31 August.
- There's minor membership churn within the count (Malta vs. Spain across snapshots) while the total held at 9.

The biggest caveat: **this tracker lags real-world designations substantially**, so its count reflects when the FLI team refreshes the page more than the underlying pace of member-state action.


### ↳ End nested research agent trace

## 💭 Thinking



## 💬 Response

I have strong data. Let me analyze the trajectory and build the distribution.

The tracker is a step-function driven by infrequent editorial updates:
- **3 Clear** for ~13 months (May 2025 → June 16, 2026), unchanged even through the Aug 2, 2025 legal deadline
- **9 Clear** as of June 17, 2026 overhaul, still 9 on July 3, 2026
- Current value (today): **9 Clear**

Key dynamics: Status quo is 9 (→ resolves "≤9"). A refresh could occur around the Aug 2, 2026 applicability milestone, but the team notably did NOT refresh around the prior Aug 2, 2025 deadline — updates are rare and unpredictable. Metaculus checks on/after Aug 31.

## 💭 Thinking



## 💬 Response

My hand-set distribution better reflects the ordinal structure than the softmax (which inflates the >15 tail). Reaching >15 would require +7 in a single refresh, implausible. Proceeding to premortem.
