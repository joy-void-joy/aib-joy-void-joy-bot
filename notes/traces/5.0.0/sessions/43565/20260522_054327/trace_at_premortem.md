# Reasoning Log: How many deaths will be attributed to the 2026 Ebola Bundibugyo outbreak in Ituri Province, DRC, as reported by Africa CDC by May 31, 2026?

*Generated: 2026-05-22T05:58:44.096309+00:00*


## 💭 Thinking

Let me analyze this forecasting question about the 2026 Ebola Bundibugyo outbreak in Ituri Province, DRC.

Key facts from the question:
- Outbreak identified in early May 2026 in Ituri Province, DRC
- WHO confirmed on May 15, 2026
- As of May 15: ~246 suspected cases, ~65 deaths, 13/20 samples positive for BDBV, 4 deaths among lab-confirmed
- ~80 suspected community deaths referenced by WHO AFRO
- No licensed vaccine for Bundibugyo species
- Resolution: cumulative deaths by May 31, 2026 as reported by Africa CDC


- If there's no new data after May 15, I'll use 65 as the baseline, with a plausible range of 50-500 deaths by month-end
- The question closes today on May 22, so I need to assess what's likely happened in the past week and project forward to May 31

## 💬 Response

I'll start by parsing the question and researching the current state of the outbreak.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43565
  ]
}
```

### 📋 Result

```
{"post_id": 43565, "title": "How many deaths will be attributed to the 2026 Ebola Bundibugyo outbreak in Ituri Province, DRC, as reported by Africa CDC by May 31, 2026?", "type": "numeric", "url":
"https://www.metaculus.com/questions/43565", "background_info": "In early May 2026, an outbreak of Ebola virus disease caused by the Bundibugyo species (BDBV) was identified in Ituri Province, north-
eastern Democratic Republic of the Congo (DRC), centered in the Mongbwalu and Rwampara health zones with suspected cases extending into Bunia. WHO officially confirmed the outbreak on 15 May 2026
\u2014 the DRC's 17th recorded Ebola epidemic since 1976 and, according to early commentary, potentially the largest documented Bundibugyo outbreak to date.\n\nAs of an Africa CDC press release dated
15 May 2026 (https://africacdc.org/news-item/africa-cdc-calls-for-urgent-regional-coordination-following-ebola-virus-disease-outbreak-in-ituri-province-drc-and-imported-ebola-bundibugyo-case-reported-
by-uganda/), DRC authorities reported approximately 246 suspected cases and approximately 65 deaths in Ituri, with Ebola virus detected in 13 of 20 samples tested at INRB (Bundibugyo species), and 4
deaths among laboratory-confirmed cases. WHO AFRO communications additionally referenced about 80 suspected community deaths possibly attributable to the outbreak. A separate imported case (a 59-year-
old Congolese male) was reported in Kampala, Uganda, who died on 14 May 2026.\n\nThere is no licensed vaccine for the Bundibugyo species. Response activities (surveillance, contact tracing, IPC, lab
capacity, safe burials, RCCE) are being scaled up by DRC's Ministry of Health, WHO, Africa CDC, and partners, with significant operational constraints due to insecurity, mining-related population
mobility, and limited testing capacity. Historically, the 2007 Bundibugyo outbreak in Uganda had a case-fatality ratio of about 32% (42 deaths among 131 cases).\n\n`{\"format\": \"llm_question\",
\"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves as the total cumulative number of deaths
(combining laboratory-confirmed, probable, and suspected/community deaths) attributed to the 2026 Ebola Bundibugyo outbreak in Ituri Province, DRC, as reported by Africa CDC in its most recent public
update (press release, situation report, or Epidemic Intelligence Weekly Report) published on or before May 31, 2026. The Africa CDC Ebola page (https://africacdc.org/disease/ebola/) and Africa CDC
news page (https://africacdc.org/news/) will be consulted to identify the latest figure. Report the figure as an integer count of deaths (e.g., a reported total of 112 deaths resolves as 112). If
Africa CDC reports a numeric range, the midpoint rounded to the nearest integer is used. If Africa CDC reports both a narrower 'deaths among reported cases' figure and a separate broader 'community
deaths' or 'suspected deaths' figure for this same outbreak, the higher (more inclusive) figure is used. If Africa CDC has not published any update beyond the 15 May 2026 statement, the figure of 65
from that statement will be used.", "fine_print": "Only deaths occurring inside DRC and attributed to the Ituri Bundibugyo outbreak count; the imported case death in Uganda and any other
extraterritorial deaths are excluded. If Africa CDC publishes multiple updates by May 31, 2026, the one with the most recent publication date is used; if multiple updates share the same publication
date, the one with the larger reported death total is used. If Africa CDC's pages are inaccessible at resolution time, the equivalent figure from the WHO Disease Outbreak News page
(https://www.who.int/emergencies/disease-outbreak-news) for this outbreak will be used as a fallback, or, failing that, figures from [credible sources](https://www.metaculus.com/faq/#definitions).",
"num_forecasters": 1, "community_prediction": null, "lower_bound": 50.0, "upper_bound": 500.0}
```

## 🔧 Tool: mcp__research__research


## 🔧 Tool: mcp__metaculus__get_coherence_links


```json
{
  "questions": [
    {
      "query": "Ebola Bundibugyo outbreak Ituri Province DRC May 2026 deaths update Africa CDC",
      "ttl": "6h"
    },
    {
      "query": "WHO Ebola DRC 2026 outbreak Mongbwalu Rwampara cases deaths latest situation report",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Ebola Bundibugyo outbreak Ituri Province DRC May 2026 deaths update Africa CDC", "entry": {"slug": "ebola-bundibugyo-outbreak-ituri-province-drc-may-2-71a94e41", "query":
"Ebola Bundibugyo outbreak Ituri Province DRC May 2026 deaths update Africa CDC", "answer": "\n\nAll web search and fetch tools are unavailable in this session. I must report my findings based on what
I can determine, noting the limitations clearly.", "sources": [], "key_facts": ["All web search and fetch tools were unavailable during this research session; no live data could be retrieved.",
"Bundibugyo ebolavirus (BDBV) was first identified in Uganda in 2007 with a ~25% case fatality rate (149 cases, 37 deaths).", "DRC's Ituri Province was previously affected by the 2018-2020 Ebola
outbreak (Zaire strain, 3,400+ cases).", "Ituri Province faces ongoing armed conflict that complicates public health emergency responses.", "No verified current data on a May 2026 Bundibugyo Ebola
outbreak in Ituri Province could be obtained.", "Africa CDC and WHO Disease Outbreak News are the primary authoritative sources that should be consulted when tools are restored."], "data_points": [],
"created_at": "2026-05-22T05:45:10.725482Z", "updated_at": "2026-05-22T05:45:10.725482Z", "stale_after": "2026-05-22T11:45:10.725482Z", "state": "fresh", "revision_history": [], "session_id":
"81ad614d-5a73-46fb-af60-83fc77784b24", "follow_up_count": 0}, "is_follow_up": false}, {"query": "WHO Ebola DRC 2026 outbreak Mongbwalu Rwampara cases deaths latest situation report", "entry":
{"slug": "who-ebola-drc-2026-outbreak-mongbwalu-rwampara-cas-b01fcb45", "query": "WHO Ebola DRC 2026 outbreak Mongbwalu Rwampara cases deaths latest situation report", "answer": "The research agent
returned comprehensive findings. Let me compile the full report.\n\n---\n\n# WHO Ebola DRC 2026 Outbreak \u2014 Mongbwalu & Rwampara: Research Report\n\n## Overview\n\nThis is the **17th Ebola
outbreak** in the Democratic Republic of the Congo (DRC), caused by the **Bundibugyo ebolavirus** \u2014 only the third known outbreak of this strain (after Uganda 2007\u201308 and DRC 2012). It was
officially declared on **15 May 2026** by DRC's Ministry of Health following laboratory confirmation by INRB in Kinshasa. WHO Director-General declared it a **Public Health Emergency of International
Concern (PHEIC)** on **16 May 2026**.\n\n## Key Epidemiological Data (as of 18\u201320 May 2026)\n\n| Metric | Value | Source / Date |\n|---|---|---|\n| Suspected cases | 536\u2013600+ | CARE (19
May); Project HOPE (20 May) |\n| Probable cases | 105 | CARE (19 May) |\n| Confirmed cases | 34\u201335 | CARE (19 May); Project HOPE (20 May) |\n| Deaths (suspected + confirmed) | 134\u2013139+ |
CARE (19 May); Project HOPE (20 May) |\n| Imported cases (Uganda) | 2 confirmed (1 death) | WHO SitRep 01 (18 May) |\n| Case growth rate | 246 \u2192 500 suspected in 96 hours (103% increase) | IRC
(19 May) |\n| Historical Bundibugyo CFR | 25\u201340% | WHO / historical data |\n| Current crude CFR (suspected) | ~25% | Derived (134/536) |\n\n## Affected Areas\n\n### DRC \u2014 Ituri Province
(epicenter)\n- **Mongbwalu Health Zone** \u2014 the outbreak epicenter; a mining area with high population mobility\n- **Rwampara Health Zone** \u2014 early affected area\n- **Bunia Health Zone**
\u2014 includes provincial capital Bunia\n\n### DRC \u2014 North Kivu Province\n- Cases confirmed including in **Goma**, a densely populated transit hub\n\n### Cross-Border\n- **Uganda**: 2 confirmed
imported cases (confirmed 15\u201316 May; 1 death on 14 May)\n- **Burundi, Rwanda, South Sudan**: Heightened readiness/alert\n\n## Timeline\n\n| Date | Event |\n|---|---|\n| ~29 March 2026 | First
signs of epidemic observed in Bunia region (Caritas) |\n| Early April 2026 | Outbreak likely began; undetected transmission for weeks |\n| Late April 2026 | Presumed index case: a nurse who died at
Evangelical Medical Center, Bunia |\n| 5 May 2026 | WHO alerted about unknown illness with high mortality in Mongbwalu; 4 health workers died within 4 days |\n| 9\u201310 May 2026 | MSF received first
alerts of suspected viral hemorrhagic fever deaths |\n| 14 May 2026 | First Uganda case died |\n| 15 May 2026 | INRB confirmed Bundibugyo virus; DRC officially declared 17th Ebola outbreak; Uganda
confirmed first imported case |\n| 16 May 2026 | Uganda confirmed second imported case; WHO DG declared PHEIC |\n| 17 May 2026 | WHO activated highest internal alert level |\n| 18 May 2026 | WHO
Weekly External Situation Report 01 data cutoff |\n| 19 May 2026 | IRC reported 103% case surge in 96 hours |\n\n## Vaccines & Therapeutics\n\n- **No approved vaccine or treatment** exists for
Bundibugyo ebolavirus (existing Ervebo/rVSV-ZEBOV vaccines target only the Zaire strain)\n- Emergency clinical trial discussions underway at WHO\n- **PCR diagnostic cartridges** for Bundibugyo virus
available in insufficient quantities, slowing confirmation\n\n## Response\n\n- **WHO**: Delivered 11.5 tonnes of medical supplies within 72 hours; 35+ experts deployed\n- **IFRC**: Launched CHF 29
million (~USD 34 million) regional emergency appeal; 200 Red Cross volunteers deployed\n- **MSF**: Mobilizing medical and logistics teams; dispatching supplies\n- **CARE**: Targeting 500,000\u20131
million people in affected/high-risk areas\n- **MONUSCO**: Providing airlift support\n\n## Contributing Factors to Severity\n\n- **US funding cuts** (from March 2025) reduced IRC programming in Ituri
from 5 to 2 health areas, weakening surveillance in the outbreak epicenter\n- Weeks of **undetected transmission** before official declaration\n- Ongoing **conflict and insecurity** in eastern DRC\n-
**Highly mobile populations** (mining, cross-border trade)\n- **Healthcare worker infections/deaths** early in the outbreak\n- Critical **PPE shortages** in health facilities\n- Community attribution
of deaths to **mystical causes**, hindering public health measures\n\n---", "sources": [{"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-bundibugyo-virus-disease-outbreak-
democratic-republic-congo-uganda-weekly-external-situation-report-01-data-18-may-2026", "title": "WHO Weekly External Situation Report 01 - Ebola Bundibugyo Virus Disease Outbreak DRC & Uganda",
"domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "Data as of 18 May 2026. Confirmed Bundibugyo virus disease in Mongbwalu and Rwampara Health Zones. 2 imported cases
confirmed in Uganda."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-1-may-20-2026", "title": "Project HOPE Situation Report #1 -
Ebola Outbreak DRC and Uganda", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "600+ suspected cases, 35 confirmed cases, 139+ suspected deaths as of 20 May 2026."},
{"url": "https://reliefweb.int/report/democratic-republic-congo/funding-cuts-led-delayed-detection-deadly-ebola-outbreak-drc", "title": "IRC: Funding cuts led to delayed detection of deadly Ebola
outbreak in DRC", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "Suspected cases rose from 246 to 500 in 96 hours (103% increase). US funding cuts reduced IRC
programming from 5 to 2 health areas in Ituri."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/who-ramps-support-democratic-republic-congos-ebola-outbreak-response", "title": "WHO
ramps up support for DRC Ebola outbreak response", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "WHO delivered 11.5 tonnes of vital medical supplies within 72 hours.
35+ experts deployed."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/bundibugyo-virus-challenge-why-ebola-disease-outbreak-different", "title": "MSF: The Bundibugyo virus challenge
- why this Ebola outbreak is different", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "Nearly 500 suspected cases. No approved vaccine or treatment for Bundibugyo
virus. Cases confirmed in North Kivu including Goma."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-2026-what-msf-doing-and-how-can-i-help", "title": "MSF: Ebola
outbreak 2026 - what MSF is doing", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "536+ suspected cases, 134+ suspected deaths. MSF mobilizing teams and supplies."},
{"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-ifrc-scales-response-eastern-drc-regional-risks-grow-enar", "title": "IFRC Emergency Appeal - Ebola response in eastern DRC",
"domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "CHF 29 million regional emergency appeal. 200 Red Cross volunteers deployed in Bunia and Rwampara."}, {"url":
"https://reliefweb.int/report/democratic-republic-congo/new-ebola-outbreak-hits-drc-and-uganda-what-you-need-know", "title": "CARE: New Ebola outbreak hits DRC and Uganda", "domain": "reliefweb.int",
"accessed_at": "2026-05-22T00:00:00Z", "snippet": "536 suspected cases, 105 probable cases, 34 confirmed cases, 134 deaths as of 19 May 2026."}, {"url": "https://reliefweb.int/report/democratic-
republic-congo/ebola-democratic-republic-congo-action-against-hunger-warns-virus-impact-communities", "title": "Action Against Hunger: Ebola in DRC warning", "domain": "reliefweb.int", "accessed_at":
"2026-05-22T00:00:00Z", "snippet": "Outbreak believed to have started in early April 2026, undetected for weeks."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/caritas-mobilises-
respond-17th-ebola-outbreak-democratic-republic-congo", "title": "Caritas mobilises to respond to 17th Ebola outbreak in DRC", "domain": "reliefweb.int", "accessed_at": "2026-05-22T00:00:00Z",
"snippet": "First signs of epidemic observed ~29 March 2026 in Bunia region of Ituri Province."}], "key_facts": ["This is the 17th Ebola outbreak in DRC, caused by Bundibugyo ebolavirus (only the 3rd
known outbreak of this strain)", "Outbreak officially declared 15 May 2026 by DRC Ministry of Health after INRB lab confirmation", "WHO Director-General declared it a Public Health Emergency of
International Concern (PHEIC) on 16 May 2026", "Epicenter is Mongbwalu Health Zone in Ituri Province; Rwampara and Bunia health zones also affected", "As of 19-20 May 2026: 536-600+ suspected cases,
105 probable cases, 34-35 confirmed cases, 134-139+ deaths", "Cases confirmed in North Kivu Province including Goma, a major transit hub", "2 confirmed imported cases in Uganda (1 death), confirmed
15-16 May 2026", "Suspected cases surged from 246 to 500 in just 96 hours (103% increase) as of 19 May 2026", "No approved vaccine or treatment exists for Bundibugyo ebolavirus; existing Ebola
vaccines target only the Zaire strain", "Outbreak likely began in early April 2026 but went undetected for weeks; first signs observed ~29 March 2026", "US government funding cuts from March 2025
reduced IRC programming in Ituri from 5 to 2 health areas, weakening surveillance", "WHO delivered 11.5 tonnes of medical supplies within 72 hours and deployed 35+ experts", "IFRC launched CHF 29
million (~USD 34 million) regional emergency appeal", "PCR diagnostic cartridges for Bundibugyo virus available in insufficient quantities, slowing case confirmation", "4 health workers died within 4
days in the initial alert that reached WHO on 5 May 2026"], "data_points": [{"metric": "Suspected cases", "value": 536.0, "unit": "cases", "as_of": "2026-05-19", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/new-ebola-outbreak-hits-drc-and-uganda-what-you-need-know"}, {"metric": "Suspected cases (Project HOPE estimate)", "value": 600.0, "unit":
"cases", "as_of": "2026-05-20", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-1-may-20-2026"}, {"metric": "Probable cases",
"value": 105.0, "unit": "cases", "as_of": "2026-05-19", "source_url": "https://reliefweb.int/report/democratic-republic-congo/new-ebola-outbreak-hits-drc-and-uganda-what-you-need-know"}, {"metric":
"Confirmed cases", "value": 35.0, "unit": "cases", "as_of": "2026-05-20", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-
report-1-may-20-2026"}, {"metric": "Deaths (suspected and confirmed)", "value": 134.0, "unit": "deaths", "as_of": "2026-05-19", "source_url": "https://reliefweb.int/report/democratic-republic-
congo/new-ebola-outbreak-hits-drc-and-uganda-what-you-need-know"}, {"metric": "Deaths (Project HOPE estimate)", "value": 139.0, "unit": "deaths", "as_of": "2026-05-20", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-1-may-20-2026"}, {"metric": "Confirmed imported cases in Uganda", "value": 2.0, "unit": "cases",
"as_of": "2026-05-18", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation-
report-01-data-18-may-2026"}, {"metric": "Uganda confirmed deaths", "value": 1.0, "unit": "deaths", "as_of": "2026-05-18", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-
bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation-report-01-data-18-may-2026"}, {"metric": "Case surge rate (96-hour period)", "value": 103.0, "unit":
"percent increase", "as_of": "2026-05-19", "source_url": "https://reliefweb.int/report/democratic-republic-congo/funding-cuts-led-delayed-detection-deadly-ebola-outbreak-drc"}, {"metric": "Historical
Bundibugyo CFR", "value": 32.5, "unit": "percent (midpoint of 25-40% range)", "as_of": "2026-05-18", "source_url": "https://reliefweb.int/report/democratic-republic-congo/bundibugyo-virus-challenge-
why-ebola-disease-outbreak-different"}, {"metric": "WHO medical supplies delivered", "value": 11.5, "unit": "tonnes", "as_of": "2026-05-19", "source_url": "https://reliefweb.int/report/democratic-
republic-congo/who-ramps-support-democratic-republic-congos-ebola-outbreak-response"}, {"metric": "WHO experts deployed", "value": 35.0, "unit": "personnel", "as_of": "2026-05-19", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/who-ramps-support-democratic-republic-congos-ebola-outbreak-response"}, {"metric": "IFRC emergency appeal", "value": 29.0, "unit": "million
CHF", "as_of": "2026-05-21", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-ifrc-scales-response-eastern-drc-regional-risks-grow-enar"}, {"metric": "Red Cross volunteers
deployed", "value": 200.0, "unit": "volunteers", "as_of": "2026-05-21", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-ifrc-scales-response-eastern-drc-regional-risks-
grow-enar"}, {"metric": "Health worker deaths in initial alert", "value": 4.0, "unit": "deaths", "as_of": "2026-05-05", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-
bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation-report-01-data-18-may-2026"}, {"metric": "CARE target population", "value": 1000000.0, "unit": "people",
"as_of": "2026-05-20", "source_url": "https://reliefweb.int/report/democratic-republic-congo/new-ebola-outbreak-hits-drc-and-uganda-what-you-need-know"}], "created_at": "2026-05-22T05:50:12.102518Z",
"updated_at": "2026-05-22T05:50:12.102518Z", "stale_after": "2026-05-22T11:50:12.102518Z", "state": "fresh", "revision_history": [], "session_id": "5f9313a8-a0de-4a18-88cf-38e06b066d7e",
"follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

```json
{
  "post_id": 43565
}
```

### 📋 Result

```
[]
```

## 💬 Response

Excellent research. Now let me fetch the latest data directly from Africa CDC and WHO to get the most up-to-date figures.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "Africa CDC Ebola Bundibugyo DRC Ituri deaths May 2026 latest update"
}
```

### 📋 Result

```
{"query": "Africa CDC Ebola Bundibugyo DRC Ituri deaths May 2026 latest update", "results": [{"title": "Epidemic of Ebola Disease caused by Bundibugyo virus in the Democratic Republic of the Congo and
Uganda determined a public health emergency of international concern", "url": "https://www.who.int/news/item/17-05-2026-epidemic-of-ebola-disease-in-the-democratic-republic-of-the-congo-and-uganda-
determined-a-public-health-emergency-of-international-concern", "snippet": "Pursuant to paragraph 2 of Article 12 - Determination of a public health emergency of international concern, including a
pandemic emergency of the [International Health Regulations (2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the Director-General of the World Health Organization (WHO),
after having consulted the States Parties where the event is known to be currently occurring, is hereby determining that the Ebola disease caused by Bundibugyo virus in the Democr", "api_data": null,
"hint": null}, {"title": "Africa CDC Calls for Urgent Regional Coordination Following Ebola Outbreak in Ituri Province, DRC, and Imported Ebola Bundibugyo Case Reported by Uganda \u2013 Africa CDC",
"url": "https://africacdc.org/news-item/africa-cdc-calls-for-urgent-regional-coordination-following-ebola-virus-disease-outbreak-in-ituri-province-drc-and-imported-ebola-bundibugyo-case-reported-by-
uganda/", "snippet": "Addis Ababa, Ethiopia / Kinshasa, DRC / Kampala, Uganda, 15 May 2026 \u2014 The Africa Centres for Disease Control and Prevention (Africa CDC) is closely monitoring the confirmed
Ebola outbreak in Ituri Province, Democratic Republic of the Congo (DRC), and the imported Ebola Bundibugyo case reported by the Uganda Ministry of Health. Africa CDC is working with national
authorities and partners to support a rapid, coordinated regional response aimed at interrupting transmission, protecting communities ", "api_data": null, "hint": null}, {"title": "Ebola Disease
Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n- Distributed via the CDC Health Alert
Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-Health-Advisory.png)\nSummary\nThe Centers for Disease Control and
Prevention (CDC) is issuing this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and travelers about a new outbreak of Ebola disease in the Democratic
Republic of the Congo (DRC) and Uganda caused by the Bundib", "api_data": null, "hint": null}, {"title": "Ebola outbreak 2026: Q&A with experts | Imperial News | Imperial College London", "url":
"https://www.imperial.ac.uk/news/articles/2026/ebola-outbreak-2026-qa-with-experts/", "snippet": "Ebola outbreak 2026: Q&A with experts\n![](/news/media/news-images/3000x2000-main-article-
images/Ebola-150526.jpg)\nFollowing African CDC reports of 246 suspected cases and 80 deaths from Ebola virus disease in North Eastern DRC, our experts from the School of Public Health share their
insights in this Q&A.\nLast updated 16-05-2026 at 17.00\nWhat is Ebola, how is it spread, what are the symptoms and how is it treated?\nEbola virus disease is a viral haemorrhagic fever caused by
species of orthoebolav", "api_data": null, "hint": null}, {"title": "2026 Ituri Province Ebola epidemic - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic",
"snippet": "In May 2026, an epidemic of Ebola disease was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in DRC and only 5 months after the
end of the previous outbreak. Imported cases from Ituri have been reported in the capital city of Kinshasa and its North Kivu Province, as well as in Uganda's capital city of Kampala. A case in South
Kivu was also reported to be imported from Tshopo province on 21 May.\nThe epidemic is caused by the Bundibugyo ", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Ituri Province
Ebola epidemic\", \"url\": \"https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola disease was reported in the Ituri Province of the
Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in DRC and only 5 months after the end of the previous outbreak. Imported cases from Ituri have been reported in the capital city
of Kinshasa and its North Kivu Province, as well as in Uganda's capital city of Kampala. A case in South Kivu was also reported to be imported from Tshopo province on 21 May.\\nThe epidemic is caused
by the Bundibugyo ebolavirus, which complicates response efforts as there are no proven vaccines and treatments; existing Ebola treatments are for the Zaire ebolavirus. The outbreak was declared a
Public Health Emergency of International Concern (PHEIC) by the World Health Organization on 16 May 2026. As of 19 May 2026, 543 suspected cases and at least 131 deaths have been reported. It is
considered likely that the true number of infections could considerably exceed the suspected cases.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "CDC Mobilizes International Response Following
Ebola Disease Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-response.html", "snippet": "Statement\nThe Centers for
Disease Control and Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic Republic of the Congo (DRC) and cases in Uganda.
Through existing relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed and have been actively working to support needs.
Last night, the WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "Ebola Disease: Current Situation | Ebola | CDC", "url":
"https://www.cdc.gov/ebola/situation-summary/index.html", "snippet": "Key points\n- CDC is responding to an outbreak of Ebola disease in remote areas of the Democratic Republic of the Congo (DRC) and
Uganda.\n- To date, no cases of Ebola disease have been confirmed in the United States because of this outbreak.\n- The overall risk to the American public and travelers remains low.\n![Micrograph
image of orthoebolavirus virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent Ebola from entering the United States\nOn ", "api_data": null,
"hint": null}, {"title": "Ebola virus disease outbreak in the Democratic Republic of the Congo and Uganda, 19 May 2026", "url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-
republic-congo-and-uganda-19-may-2026", "snippet": "Ebola virus disease outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more information becomes available. It was
last updated 21 May 18:00.\nOn 15 May 2026, Africa CDC reported an outbreak of Ebola disease in Ituri Province, DRC. Laboratory analysis at Institut National de Recherche Biomedicale of DRC identified
Bundibugyo virus (BDBV). BDBV disease is a rare disease but can cause outbreaks with high case fatality rates. Considering the available information, com", "api_data": null, "hint": null}]}
```

```json
{
  "query": "WHO Ebola Bundibugyo DRC 2026 situation report deaths May 21 22"
}
```

### 📋 Result

```
{"query": "WHO Ebola Bundibugyo DRC 2026 situation report deaths May 21 22", "results": [{"title": "Epidemic of Ebola Disease caused by Bundibugyo virus in the Democratic Republic of the Congo and
Uganda determined a public health emergency of international concern", "url": "https://www.who.int/news/item/17-05-2026-epidemic-of-ebola-disease-in-the-democratic-republic-of-the-congo-and-uganda-
determined-a-public-health-emergency-of-international-concern", "snippet": "Pursuant to paragraph 2 of Article 12 - Determination of a public health emergency of international concern, including a
pandemic emergency of the [International Health Regulations (2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the Director-General of the World Health Organization (WHO),
after having consulted the States Parties where the event is known to be currently occurring, is hereby determining that the Ebola disease caused by Bundibugyo virus in the Democr", "api_data": null,
"hint": null}, {"title": "EBOLA BUNDIBUGYO VIRUS DISEASE OUTBREAK Democratic Republic of the Congo | Uganda Weekly External Situation Report 01, Data as of 18 May 2026 | WHO | Regional Office for
Africa", "url": "https://www.afro.who.int/countries/democratic-republic-of-congo/publication/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation",
"snippet": "![Weekly External Situation Report 01, Data as of 18 May 2026](/sites/default/files/2026-05/Wk_Ext_SitRep_0118052026.jpg)\nEBOLA BUNDIBUGYO VIRUS DISEASE OUTBREAK Democratic Republic of
the Congo | Uganda Weekly External Situation Report 01, Data as of 18 May 2026\nEvent description\nOn 5 May 2026, the World Health Organization (WHO) received an alert regarding an unknown illness
with high mortality in Mongbwalu Health Zone (HZ), Ituri Province, Democratic Republic of the Congo (DRC), including rep", "api_data": null, "hint": null}, {"title": "CDC Mobilizes International
Response Following Ebola Disease Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-response.html", "snippet":
"Statement\nThe Centers for Disease Control and Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic Republic of the Congo (DRC)
and cases in Uganda. Through existing relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed and have been actively
working to support needs. Last night, the WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "Ebola virus disease outbreak in the Democratic
Republic of the Congo and Uganda, 19 May 2026", "url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-republic-congo-and-uganda-19-may-2026", "snippet": "Ebola virus disease
outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more information becomes available. It was last updated 21 May 18:00.\nOn 15 May 2026, Africa CDC reported an
outbreak of Ebola disease in Ituri Province, DRC. Laboratory analysis at Institut National de Recherche Biomedicale of DRC identified Bundibugyo virus (BDBV). BDBV disease is a rare disease but can
cause outbreaks with high case fatality rates. Considering the available information, com", "api_data": null, "hint": null}, {"title": "WHO Director-General's opening remarks at the media briefing on
Ebola outbreak in DRC and Uganda \u2013 20 May 2026", "url": "https://www.who.int/news-room/speeches/item/who-director-general-s-opening-remarks-at-the-media-briefing-on-ebola-outbreak-in-drc-and-
uganda-20-may-2026", "snippet": "Good morning to everyone in the room, and hello to everybody joining us online. Thank you for joining us.\nEarly on Sunday, I declared a public health emergency of
international concern over an epidemic of Ebola disease in the Democratic Republic of the Congo and Uganda.\nThis is the first time a Director-General has declared a PHEIC before convening an
Emergency Committee.\nI took this step in accordance with Article 12 of the International Health Regulations, after consulting the Ministers of Hea", "api_data": null, "hint": null}, {"title": "Ebola
disease caused by Bundibugyo virus, Democratic Republic of the Congo & Uganda", "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602", "snippet": "Situation at a
glance\nDescription of the situation\nOn 5 May 2026, WHO received an alert regarding an unknown illness with high mortality reported in Mongbwalu Health Zone, Ituri Province, including four health
workers who died within four days. Following an in-depth investigation by the rapid response team in Mongbwalu and Rwampara health zones (HZ) on 13 May, the outbreak was subsequently confirmed as
Bundibugyo virus disease (BVD) due to Bundibugyo virus (BDBV) (Orthoebolavirus bundibugyoense,", "api_data": null, "hint": null}, {"title": "Ebola Disease: Current Situation | Ebola | CDC", "url":
"https://www.cdc.gov/ebola/situation-summary/index.html", "snippet": "Key points\n- CDC is responding to an outbreak of Ebola disease in remote areas of the Democratic Republic of the Congo (DRC) and
Uganda.\n- To date, no cases of Ebola disease have been confirmed in the United States because of this outbreak.\n- The overall risk to the American public and travelers remains low.\n![Micrograph
image of orthoebolavirus virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent Ebola from entering the United States\nOn ", "api_data": null,
"hint": null}, {"title": "Ebola Disease Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n-
Distributed via the CDC Health Alert Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-Health-
Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and travelers
about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and Uganda caused by the Bundib", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://africacdc.org/disease/ebola/",
  "prompt": "What are the latest reported death figures for the 2026 Ebola Bundibugyo outbreak in Ituri Province DRC? Look for the most recent numbers and dates."
}
```

### 📋 Result

```
{"url": "https://africacdc.org/disease/ebola/", "content": "The content provided does not contain information about a 2026 Ebola Bundibugyo outbreak in Ituri Province, DRC.\n\nThe most recent outbreak
information in the content is from 2019, which mentions an ongoing outbreak in DRC (North Kivu & Ituri provinces) with 2,787 confirmed cases and 1,867 deaths as of August 9, 2019. There is no data
about any 2026 outbreak.\n\nRelevant links:\n- [Africa CDC Ebola Disease Page](https://africacdc.org/disease/ebola/)", "title": "Ebola Virus Disease \u2013 Africa CDC"}
```

## 💬 Response

Let me get more recent data - the Wikipedia article and ECDC updates seem to have more current figures.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic",
  "prompt": "What are the latest reported death figures, case counts, and their dates for this outbreak? Provide all available data points about deaths and cases by date, including any table data."
}
```

### 📋 Result

```
{"title": "2026 Ituri Province Ebola epidemic", "url": "https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic", "extract": "In May 2026, an epidemic of Ebola disease was reported in the
Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in DRC and only 5 months after the end of the previous outbreak. Imported cases from Ituri have been
reported in the capital city of Kinshasa and its North Kivu Province, as well as in Uganda's capital city of Kampala. A case in South Kivu was also reported to be imported from Tshopo province on 21
May.\nThe epidemic is caused by the Bundibugyo ebolavirus, which complicates response efforts as there are no proven vaccines and treatments; existing Ebola treatments are for the Zaire ebolavirus.
The outbreak was declared a Public Health Emergency of International Concern (PHEIC) by the World Health Organization on 16 May 2026. As of 19 May 2026, 543 suspected cases and at least 131 deaths
have been reported. It is considered likely that the true number of infections could considerably exceed the suspected cases.", "mode": "full"}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-republic-congo-and-uganda-19-may-2026",
  "prompt": "What are the latest death and case figures for the 2026 Ebola Bundibugyo outbreak in DRC? Get all numbers including dates and sources."
}
```

### 📋 Result

```
{"url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-republic-congo-and-uganda-19-may-2026", "content": "Based on the content provided, here are the latest figures for the
2026 Ebola Bundibugyo outbreak in DRC:\n\n**As of 20 May 2026** (according to WHO):\n- **Approximately 600 suspected cases**\n- **139 deaths among suspected cases**\n- **51 confirmed cases in DRC**\n-
**2 imported cases in Uganda**\n\n**Key dates:**\n- 15 May 2026: Africa CDC reported the outbreak in Ituri Province, DRC\n- 17 May 2026: WHO declared a Public Health Emergency of International
Concern\n- 18 May 2026: Africa CDC declared a Public Health Emergency of Continental Security\n- 20 May 2026: Latest case/death figures reported\n- 21 May 2026, 18:00: Last page update\n\n**Source:**
World Health Organisation (WHO Director-General's media briefing on 20 May 2026)\n\n**Relevant links:**\n- [WHO Director-General's opening remarks at the media briefing on Ebola outbreak in DRC and
Uganda \u2013 20 May 2026](https://www.who.int/news-room/speeches/item/who-director-general-s-opening-remarks-at-the-media-briefing-on-ebola-outbreak-in-drc-and-uganda-20-may-2026)", "title": "Ebola
virus disease outbreak in the Democratic Republic of the Congo and Uganda"}
```

```json
{
  "query": "\"Ebola\" \"Bundibugyo\" \"DRC\" deaths cases May 21 OR May 22 2026"
}
```

### 📋 Result

```
{"query": "\"Ebola\" \"Bundibugyo\" \"DRC\" deaths cases May 21 OR May 22 2026", "results": [{"title": "Ebola Disease Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC", "url":
"https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n- Distributed via the CDC Health Alert Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC
health advisory.](/han/media/images/2025/03/HAN-Health-Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing this Health Alert Network (HAN) Health Advisory to alert
clinicians, public health practitioners, and travelers about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and Uganda caused by the Bundib", "api_data": null, "hint":
null}, {"title": "Ebola Disease: Current Situation | Ebola | CDC", "url": "https://www.cdc.gov/ebola/situation-summary/index.html", "snippet": "Key points\n- CDC is responding to an outbreak of Ebola
disease in remote areas of the Democratic Republic of the Congo (DRC) and Uganda.\n- To date, no cases of Ebola disease have been confirmed in the United States because of this outbreak.\n- The
overall risk to the American public and travelers remains low.\n![Micrograph image of orthoebolavirus virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing
measures to prevent Ebola from entering the United States\nOn ", "api_data": null, "hint": null}, {"title": "CDC Mobilizes International Response Following Ebola Disease Outbreak in DRC and Uganda |
CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-response.html", "snippet": "Statement\nThe Centers for Disease Control and Prevention (CDC) has
mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic Republic of the Congo (DRC) and cases in Uganda. Through existing relationships with the DRC and
Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed and have been actively working to support needs. Last night, the WHO followed this notification
with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "DR Congo: Ebola Outbreak - May 2026", "url": "https://reliefweb.int/disaster/ep-2026-000071-cod", "snippet":
"![](/sites/default/files/styles/small/public/previews/aa/4c/aa4c2dba-7bdb-559a-b717-d7f27bbfede7.png?2721317-1-0)\nDR Congo: Ebola Outbreak - May 2026\nDisaster description\nOn 5 May 2026, the World
Health Organization (WHO) was alerted of a high-mortality outbreak of unknown illness in Mongbwalu Health Zone, Ituri Province, including deaths among health workers. Laboratory analysis confirmed
Bundibugyo virus disease (BVD), a species of Ebola, in eight samples on 15 May. The case fatality rates in ", "api_data": null, "hint": null}, {"title": "Ebola outbreak in DRC and Uganda: What you
need to know | The IRC", "url": "https://www.rescue.org/article/ebola-outbreak-drc-and-uganda-what-you-need-know", "snippet": "![9:38 AMClaude responded: Health workers in full protective gear stand
outdoors in North Kivu, DRC, during the 2018 Ebola outbreak.Health workers in full protective gear stand outdoors in North Kivu, DRC, during the 2018 Ebola
outbreak.](/sites/default/files/styles/square_1x1_1280px_wide/public/2026-05/20180823_KRyan_DRC_Ebola-45.jpg?itok=rNq9sZsN)\nAs Ebola cases spread across eastern Democratic Republic of Congo (DRC) and
into Uganda, the International Rescue Committee (IRC) has launched a res", "api_data": null, "hint": null}, {"title": "BREAKING: WHO declares major outbreak of rare Ebola virus species an
international emergency | Science | AAAS", "url": "https://www.science.org/content/article/major-outbreak-rare-ebola-virus-species-northern-congo-alarms-scientists", "snippet": null, "api_data": null,
"hint": null}, {"title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the Congo & Uganda", "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602",
"snippet": "Situation at a glance\nDescription of the situation\nOn 5 May 2026, WHO received an alert regarding an unknown illness with high mortality reported in Mongbwalu Health Zone, Ituri
Province, including four health workers who died within four days. Following an in-depth investigation by the rapid response team in Mongbwalu and Rwampara health zones (HZ) on 13 May, the outbreak
was subsequently confirmed as Bundibugyo virus disease (BVD) due to Bundibugyo virus (BDBV) (Orthoebolavirus bundibugyoense,", "api_data": null, "hint": null}, {"title": "Ebola virus disease outbreak
in the Democratic Republic of the Congo and Uganda", "url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-republic-congo-19-may-2026", "snippet": "Ebola virus disease outbreak
in the Democratic Republic of the Congo and Uganda\nThis page is updated as more information becomes available. It was last updated 21 May 18:00.\nOn 15 May 2026, Africa CDC reported an outbreak of
Ebola disease in Ituri Province, DRC. Laboratory analysis at Institut National de Recherche Biomedicale of DRC identified Bundibugyo virus (BDBV). BDBV disease is a rare disease but can cause
outbreaks with high case fatality rates. Considering the available information, com", "api_data": null, "hint": null}, {"title": "Epidemic of Ebola Disease caused by Bundibugyo virus in the Democratic
Republic of the Congo and Uganda determined a public health emergency of international concern", "url": "https://www.who.int/news/item/17-05-2026-epidemic-of-ebola-disease-in-the-democratic-republic-
of-the-congo-and-uganda-determined-a-public-health-emergency-of-international-concern", "snippet": "Pursuant to paragraph 2 of Article 12 - Determination of a public health emergency of international
concern, including a pandemic emergency of the [International Health Regulations (2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the Director-General of the World Health
Organization (WHO), after having consulted the States Parties where the event is known to be currently occurring, is hereby determining that the Ebola disease caused by Bundibugyo virus in the
Democr", "api_data": null, "hint": null}, {"title": "DRC: MSF preparing large-scale response to Ebola outbreak in Ituri province", "url": "https://www.msf.org/msf-preparing-large-scale-response-ebola-
outbreak-ituri-province", "snippet": null, "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me gather more data points to understand the trajectory and build a model. Let me fetch the WHO DON report and the latest Africa CDC news for the most current figures.

## 💬 Response

Let me get the most recent data and the Africa CDC news page for any updates after May 20.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602",
  "prompt": "What are the exact death and case figures reported? Get all numbers with dates."
}
```

### 📋 Result

```
{"url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602", "content": "[Prompt extraction failed, returning raw content]\n\nSituation at a glance\nDescription of the
situation\nOn 5 May 2026, WHO received an alert regarding an unknown illness with high mortality reported in Mongbwalu Health Zone, Ituri Province, including four health workers who died within four
days. Following an in-depth investigation by the rapid response team in Mongbwalu and Rwampara health zones (HZ) on 13 May, the outbreak was subsequently confirmed as Bundibugyo virus disease (BVD)
due to Bundibugyo virus (BDBV) (Orthoebolavirus bundibugyoense, species) on 15 May.\nOn 15 May 2026, the Ministry of Public Health, Hygiene and Social Welfare officially declared the 17th Ebola
Disease outbreak in the DRC, occurring in Rwampara, Mongwalu and Bunia HZ.\nThe first currently known suspected case, a health worker, reported onset of symptoms including fever, hemorrhaging,
vomiting and intense malaise on 24 April 2026. The case died at a medical centre in Bunia.\nAs of 15 May, a total of 246 suspected cases and 80 deaths (four deaths among confirmed cases) have been
reported from three HZ: Rwampara (six health areas affected), Mongbwalu (three health areas affected), and Bunia . Twenty four suspected cases are currently in isolation facilities across the three
HZ. In addition, unusual clusters of community deaths with symptoms compatible with Bundibugyo virus disease (BVD) are being investigated across other HZ in Ituri and North Kivu.\nA further case
reported on 16 May, an individual returning from Ituri to Kinshasa, has tested NEGATIVE for Bundibugyo virus on confirmatory testing by the Institut National de la Recherche Biom\u00e9dicale (INRB) of
DRC, and is therefore not considered a confirmed case.\nMost of the suspected cases are between 20 and 39 years old, with females accounting for over 60%, suggesting significant risks associated with
household and caregiver transmission.\nInitial testing of 20 samples collected in Rwampara HZ and analysed at the Provincial Public Health Laboratory in Bunia using standard Ebola Xpert were negative
for Ebola virus. Samples were sent to INRB for further analysis, of which eight samples analysed were confirmed as Orthoebolavirus by polymerase chain reaction (PCR) on 15 May. Genomic sequencing
confirmed the virus species as Bundibugyo virus (BDBV).\nAs of 15 May, 65 contacts have been listed, with 15 identified as high-risk. However, follow-up remains weak due to insecurity and movement
restrictions. Several listed contacts became symptomatic and died before they could be isolated.\nOn 15 May 2026, the Ministry of Health of Uganda confirmed an outbreak of BVD following the
identification of an imported case from the DRC. The case is an elderly man who was admitted to a private hospital on 11 May with severe symptoms and died on 14 May. The post-mortem transfer of the
body to DRC was completed the same day. A clinical sample collected when the case was admitted on 11 May was tested at the Central Emergency Surveillance and Response Support Laboratory, Wandegeya,
and was confirmed as Bundibugyo virus on 15 May 2026. A second imported case was confirmed on 16 May in Kampala, in an individual returning from DRC with no apparent links to the first case. At the
time of reporting, no local transmission has been identified in Uganda.\nOn 16 May 2026, the Director-General of WHO, after having consulted the States Parties where the event is known to be currently
occurring as defined in the provisions of the International Health Regulations (2005) (IHR), determined that the Ebola disease caused by Bundibugyo virus in DRC and Uganda constitutes a PHEIC.\nIt is
currently thought that the event originated in the Mongbwalu HZ, DRC, a high-traffic mining area, with cases subsequently migrating to Rwampara and Bunia to seek medical care. Ituri province borders
South Sudan and Uganda (and Bunia HZ is less than 500km from Uganda). A full epidemiological investigation and trace back exercise is ongoing.\nIturi\u2019s role as a commercial and migratory hub and
proximity to Uganda and South Sudan increases the risk of regional exportation and cross-border transmission.\nFigure 1. Health Zones affected by Bundibugyo virus disease in Democratic Republic of
Congo, as of 16 May 2026\n![Map_Ebola disease caused by Bundibugyo virus DRC Map_Ebola disease caused by Bundibugyo virus DRC](https://cdn.who.int/media/images/default-source/products/disease-
outbreak-news/map_ebola-disease-caused-by-bundibugyo-virus_drc-(2).png?sfvrsn=db9a40db_3)\nEpidemiology\nBundibugyo virus disease (BVD) is a severe and often fatal form of Ebola disease caused by the
Bundibugyo virus, one of the Orthoebolavirus species. It is a zoonotic disease, with fruit bats suspected to be the natural reservoir. Human infection occurs through close contact with the blood or
secretions of infected wildlife, such as bats or non-human primates, and subsequently spreads from person to person through direct contact with the blood, secretions, organs, or other bodily fluids of
infected individuals or contaminated surfaces. Transmission is particularly amplified in health-care settings when infection prevention and control (IPC) measures are inadequate, and during unsafe
burial practices involving direct contact with the deceased.\nThe incubation period for BVD ranges from 2 to 21 days, and individuals are usually not infectious until symptom onset. Early symptoms are
non-specific, including fever, fatigue, muscle pain, headache, and sore throat, which complicates clinical diagnosis and can delay detection. These progress to gastrointestinal symptoms, organ
dysfunction, and in some cases haemorrhagic manifestations. Case fatality rates in the past two BVD outbreaks, reported in Uganda and in DRC in 2007 and 2012, have ranged from approximately 30% to
50%.\nDifferentiating BVD from other endemic febrile illnesses such as malaria is challenging without laboratory confirmation using PCR or antigen/antibody-based assays. Control relies on rapid case
identification, isolation and care, contact tracing, safe burials, and strong community engagement, as no approved vaccines or specific treatments currently exist for BVD.\nPublic health
response\nHealth authorities in DRC are implementing public health measures, including but not limited to the following:\nCoordination\n- Rapid response teams have been deployed to Rwampara and
Mongbwalu HZ.\n- Provincial coordination and emergency meetings by le centre d\u2019operation des urgences en sante publique (COUSP) have been held.\nSurveillance and Laboratory\n- Surveillance for
suspected and probable cases is ongoing (including at relevant Points of Entry and borders).\n- Operational case definitions have been elaborated in Ituri.\n- Sequencing confirmed Bundibugyo virus in
positive RT-PCR samples.\nRisk Communication and Community Engagement (RCCE)\n- Social mobilization meeting was held with community leaders in the Rural commune of Mongbwalu under the leadership of
the Mayor.\nInfection Prevention and Control (IPC)\n- IPC assessment in key health facilities is ongoing: Bunia Hospital Centre of the Evangelical Medical Centre (CME), Mongbwalu General Referral
Hospital and Abelkozo Health Centre.\n- CME Bunia is maintaining isolation protocols. Healthcare workers have been briefed on the specific diagnostic profile of this strain.\nLogistics\n- Logistical
support has been provided for investigations in Mongbwalu and Rwampara Health Zones.\n- Support has been provided for the transportation of samples to INRB Kinshasa.\nHealth authorities in Uganda are
implementing public health measures, including but not limited to the following:\n- Activating national and district-level emergency measures, including enhanced surveillance, screening at borders,
deployment of rapid response teams, isolation of a high-risk contact, and quarantine of all identified contacts.\n- Strengthening of preparedness activities such as mobile laboratory deployment,
infection prevention, and risk communication.\n- Rapid response readiness teams have been deployed at all official and informal points of entry along the western border, major transit routes, and
pilgrimage corridors.\n- Advising health workers to remain vigilant and adhere strictly to infection prevention measures.\nWHO is supporting the national authorities, including through:\n- Deployment
of technical expertise and rapid response teams to support response efforts.\n- Deployment of IPC, clinical management and sample collection kits.\n- Identification of isolation facilities for case
management in Bunia, Rwampara, and Mongbwalu HZ .\n- Dissemination of WHO case management protocol.\n- In-depth investigations and listing of contacts of suspected/probable cases.\n- Strengthening
epidemiological surveillance, IPC and RCCE at all points of entry.\n- Strengthening Point of Entry (PoE) screening and cross border coordination, including mass gatherings.\n- Supporting the Ministry
of Health in implementation of the Response Plan and WHO internal Response Plan.\n- Following up with the IHR National Focal Points (IHR NFP) in DRC and Uganda on the official IHR notification while
concurrently managing communication across the IHR NFP network to ensure timely coordination.\n- Coordinating the delivery of key supplies.\n- Engaging experts on research and development
priorities.\nWHO risk assessment\nOn 16 May 2026, WHO Director-General, after having consulted the States Parties where the event is known to be currently occurring, determined that the Ebola disease
caused by Bundibugyo virus in the Democratic Republic of the Congo and Uganda constitutes a public health emergency of international concern (PHEIC), as per the provisions of the IHR. Temporary
recommendations for State Parties will be issued. In the meantime, WHO issued advice to countries, as stated below.\nThis is the 17th Ebola disease outbreak in the DRC since 1976. The last Ebola
disease outbreak in the country was declared on 4 September 2025 with total of 64 cases (53 confirmed, 11 probable), in", "title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the
Congo & Uganda"}
```

```json
{
  "url": "https://africacdc.org/news/",
  "prompt": "Find any updates about the 2026 Ebola Bundibugyo outbreak in DRC after May 15. Look for any new press releases, situation reports, or updates about death counts."
}
```

### 📋 Result

```
{"url": "https://africacdc.org/news/", "content": "Based on the provided content, **there is no specific information about a 2026 Ebola Bundibugyo outbreak in DRC** after May 15, 2026.\n\nThe content
only shows headlines and dates of various publications (Media Advisory, Statements, Communiqu\u00e9s, Press Releases, and Articles) from May 18-21, 2026, but does not include the actual titles or
details of these documents. Without access to the full text of these items, I cannot determine if any of them relate to an Ebola outbreak in DRC.\n\n**Relevant links:**\n\nTo find specific information
about the Ebola outbreak, you would need to check the individual items from the date range shown:\n- [20 May 2026 Press Releases](https://africacdc.org/news/) \n- [18 May 2026 Press
Releases](https://africacdc.org/news/)\n- [21 May 2026 Statement](https://africacdc.org/news/)\n- [20 May 2026 Statement](https://africacdc.org/news/)\n- [20 May 2026
Communiqu\u00e9](https://africacdc.org/news/)\n- [19 May 2026 Articles](https://africacdc.org/news/)\n\nNote: These all link to the main news page. You would need to access the specific articles to
see their full titles and content.", "title": "News \u2013 Africa CDC"}
```

```json
{
  "query": "Africa CDC Ebola situation report update DRC deaths \"May 21\" OR \"May 22\" OR \"May 23\" 2026"
}
```

### 📋 Result

```
{"query": "Africa CDC Ebola situation report update DRC deaths \"May 21\" OR \"May 22\" OR \"May 23\" 2026", "results": [{"title": "Ebola Disease: Current Situation | Ebola | CDC", "url":
"https://www.cdc.gov/ebola/situation-summary/index.html", "snippet": "Key points\n- CDC is responding to an outbreak of Ebola disease in remote areas of the Democratic Republic of the Congo (DRC) and
Uganda.\n- To date, no cases of Ebola disease have been confirmed in the United States because of this outbreak.\n- The overall risk to the American public and travelers remains low.\n![Micrograph
image of orthoebolavirus virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent Ebola from entering the United States\nOn ", "api_data": null,
"hint": null}, {"title": "CDC Mobilizes International Response Following Ebola Disease Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-
international-ebola-response.html", "snippet": "Statement\nThe Centers for Disease Control and Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri
Province, Democratic Republic of the Congo (DRC) and cases in Uganda. Through existing relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as
cases were confirmed and have been actively working to support needs. Last night, the WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title":
"Africa CDC Calls for Urgent Regional Coordination Following Ebola Outbreak in Ituri Province, DRC, and Imported Ebola Bundibugyo Case Reported by Uganda \u2013 Africa CDC", "url":
"https://africacdc.org/news-item/africa-cdc-calls-for-urgent-regional-coordination-following-ebola-virus-disease-outbreak-in-ituri-province-drc-and-imported-ebola-bundibugyo-case-reported-by-uganda/",
"snippet": "Addis Ababa, Ethiopia / Kinshasa, DRC / Kampala, Uganda, 15 May 2026 \u2014 The Africa Centres for Disease Control and Prevention (Africa CDC) is closely monitoring the confirmed Ebola
outbreak in Ituri Province, Democratic Republic of the Congo (DRC), and the imported Ebola Bundibugyo case reported by the Uganda Ministry of Health. Africa CDC is working with national authorities
and partners to support a rapid, coordinated regional response aimed at interrupting transmission, protecting communities ", "api_data": null, "hint": null}, {"title": "Ebola Disease Outbreak in the
Democratic Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n- Distributed via the CDC Health Alert Network\n- May 19,
2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-Health-Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is
issuing this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and travelers about a new outbreak of Ebola disease in the Democratic Republic of the Congo
(DRC) and Uganda caused by the Bundib", "api_data": null, "hint": null}, {"title": "Africa CDC Calls Urgent Regional Coordination Meeting Following Ebola Outbreak in Ituri Province, DRC \u2013 Africa
CDC", "url": "https://africacdc.org/news-item/africa-cdc-calls-for-urgent-regional-coordination-meeting-following-ebola-virus-disease-outbreak-in-ituri-province-drc/", "snippet": "Addis Ababa,
Ethiopia / Kinshasa, DRC, 15 May 2026 \u2014 The Africa Centres for Disease Control and Prevention (Africa CDC) is closely monitoring the confirmed Ebola outbreak in Ituri province, Democratic
Republic of the Congo, and is working with national authorities and partners to support a rapid, coordinated response.\nFollowing consultations with the DRC\u2019s Ministry of Health and National
Public Health Institute, preliminary laboratory results from the Institut National de Recherche Biom\u00e9dicale (", "api_data": null, "hint": null}, {"title": "Ebola outbreak 2026: Q&A with experts |
Imperial News | Imperial College London", "url": "https://www.imperial.ac.uk/news/articles/2026/ebola-outbreak-2026-qa-with-experts/", "snippet": "Ebola outbreak 2026: Q&A with
experts\n![](/news/media/news-images/3000x2000-main-article-images/Ebola-150526.jpg)\nFollowing African CDC reports of 246 suspected cases and 80 deaths from Ebola virus disease in North Eastern DRC,
our experts from the School of Public Health share their insights in this Q&A.\nLast updated 16-05-2026 at 17.00\nWhat is Ebola, how is it spread, what are the symptoms and how is it treated?\nEbola
virus disease is a viral haemorrhagic fever caused by species of orthoebolav", "api_data": null, "hint": null}, {"title": "DR Congo: Ebola Outbreak - May 2026", "url":
"https://reliefweb.int/disaster/ep-2026-000071-cod", "snippet": "![](/sites/default/files/styles/small/public/previews/aa/4c/aa4c2dba-7bdb-559a-b717-d7f27bbfede7.png?2721317-1-0)\nDR Congo: Ebola
Outbreak - May 2026\nDisaster description\nOn 5 May 2026, the World Health Organization (WHO) was alerted of a high-mortality outbreak of unknown illness in Mongbwalu Health Zone, Ituri Province,
including deaths among health workers. Laboratory analysis confirmed Bundibugyo virus disease (BVD), a species of Ebola, in eight samples on 15 May. The case fatality rates in ", "api_data": null,
"hint": null}, {"title": "World Health Organization declares Ebola outbreak in Congo a global health emergency : NPR", "url": "https://www.npr.org/2026/05/16/g-s1-122494/a-new-ebola-outbreak-has-
already-killed-87-people", "snippet": "World Health Organization declares Ebola outbreak in Congo a global health emergency\n![Ambulances are parked outside a hospital in Bunia, Congo, Saturday, May
16, 2026.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/1000x564+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2F93%2F5c%2F2e8bd7414ce39bed0a270690b07f%2Fap26136564576497.jpg)\nAmbulances are parked outside a hospital in Bunia, Congo, Saturday, May 16, 2026. Constant Same
Bagalwa/AP", "api_data": null, "hint": null}, {"title": "Africa CDC Declares the Ongoing Bundibugyo Ebola Outbreak a Public Health Emergency of Continental Security \u2013 Africa CDC", "url":
"https://africacdc.org/news-item/africa-cdc-declares-the-ongoing-bundibugyo-ebola-outbreak-a-public-health-emergency-of-continental-security/", "snippet": "Addis Ababa, Ethiopia, 18 May 2026 \u2013
The Africa Centres for Disease Control and Prevention (Africa CDC), acting on the recommendations of its Emergency Consultative Group (ECG), has officially declared the ongoing Bundibugyo ebolavirus
disease outbreak affecting the Democratic Republic of the Congo (DRC) and Uganda a Public Health Emergency of Continental Security (PHECS).\nThis declaration, under Article 3, Paragraph F of the
Africa CDC Statute, empowers the organisation to lead and coordinate r", "api_data": null, "hint": null}]}
```

## 💬 Response

Let me get the Africa CDC PHECS declaration from May 18 and search for any very recent updates.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://africacdc.org/news-item/africa-cdc-declares-the-ongoing-bundibugyo-ebola-outbreak-a-public-health-emergency-of-continental-security/",
  "prompt": "What specific death and case figures are reported in this Africa CDC PHECS declaration? Get exact numbers and dates."
}
```

### 📋 Result

```
{"url": "https://africacdc.org/news-item/africa-cdc-declares-the-ongoing-bundibugyo-ebola-outbreak-a-public-health-emergency-of-continental-security/", "content": "Based on the content, here are the
specific figures reported:\n\n**Case and Death Figures:**\n- **Total (DRC + Uganda):** Approximately 395 suspected cases and 106 associated deaths\n- **DRC:** Main outbreak areas are Mongwalu,
Rwampara, and Bunia Health Zones (specific numbers not broken down)\n- **Uganda (Kampala):** 2 cases and 1 death\n\n**Date:**\n- **Declaration date:** 18 May 2026\n\n**Additional context:** The
outbreak involves the Bundibugyo ebolavirus strain, confirmed through laboratory analysis.\n\n**Relevant links:**\n- [Africa CDC website](http://www.africacdc.org/)\n- [Africa CDC
LinkedIn](https://www.linkedin.com/company/14792760/)\n- [Africa CDC on X/Twitter](https://x.com/AfricaCDC)\n- [Africa CDC Facebook](https://www.facebook.com/africacdc)\n- [Africa CDC
YouTube](https://www.youtube.com/AfricaCDC)", "title": "Africa CDC Declares the Ongoing Bundibugyo Ebola Outbreak a Public Health Emergency of Continental Security \u2013 Africa CDC"}
```

```json
{
  "query": "Ebola DRC Ituri deaths cases latest update today 2026"
}
```

### 📋 Result

```
{"query": "Ebola DRC Ituri deaths cases latest update today 2026", "results": [{"title": "2026 Ituri Province Ebola epidemic - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic", "snippet": "In May 2026, an epidemic of Ebola disease was reported in the Ituri Province of the Democratic Republic of the Congo
(DRC). It is the 17th Ebola outbreak in DRC and only 5 months after the end of the previous outbreak. Imported cases from Ituri have been reported in the capital city of Kinshasa and its North Kivu
Province, as well as in Uganda's capital city of Kampala. A case in South Kivu was also reported to be imported from Tshopo province on 21 May.\nThe epidemic is caused by the Bundibugyo ", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 Ituri Province Ebola epidemic\", \"url\": \"https://en.wikipedia.org/wiki/2026_Ituri_Province_Ebola_epidemic\", \"extract\": \"In May 2026, an
epidemic of Ebola disease was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in DRC and only 5 months after the end of the previous
outbreak. Imported cases from Ituri have been reported in the capital city of Kinshasa and its North Kivu Province, as well as in Uganda's capital city of Kampala. A case in South Kivu was also
reported to be imported from Tshopo province on 21 May.\\nThe epidemic is caused by the Bundibugyo ebolavirus, which complicates response efforts as there are no proven vaccines and treatments;
existing Ebola treatments are for the Zaire ebolavirus. The outbreak was declared a Public Health Emergency of International Concern (PHEIC) by the World Health Organization on 16 May 2026. As of 19
May 2026, 543 suspected cases and at least 131 deaths have been reported. It is considered likely that the true number of infections could considerably exceed the suspected cases.\", \"mode\":
\"full\"}"}]}, "hint": null}, {"title": "Ebola Disease Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet":
"At a glance\n- Distributed via the CDC Health Alert Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-Health-
Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and travelers
about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and Uganda caused by the Bundib", "api_data": null, "hint": null}, {"title": "Epidemic of Ebola Disease caused by
Bundibugyo virus in the Democratic Republic of the Congo and Uganda determined a public health emergency of international concern", "url": "https://www.who.int/news/item/17-05-2026-epidemic-of-ebola-
disease-in-the-democratic-republic-of-the-congo-and-uganda-determined-a-public-health-emergency-of-international-concern", "snippet": "Pursuant to paragraph 2 of Article 12 - Determination of a public
health emergency of international concern, including a pandemic emergency of the [International Health Regulations (2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the
Director-General of the World Health Organization (WHO), after having consulted the States Parties where the event is known to be currently occurring, is hereby determining that the Ebola disease
caused by Bundibugyo virus in the Democr", "api_data": null, "hint": null}, {"title": "Ebola Disease: Current Situation | Ebola | CDC", "url": "https://www.cdc.gov/ebola/situation-summary/index.html",
"snippet": "Key points\n- CDC is responding to an outbreak of Ebola disease in remote areas of the Democratic Republic of the Congo (DRC) and Uganda.\n- To date, no cases of Ebola disease have been
confirmed in the United States because of this outbreak.\n- The overall risk to the American public and travelers remains low.\n![Micrograph image of orthoebolavirus
virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent Ebola from entering the United States\nOn ", "api_data": null, "hint": null}, {"title":
"CDC Mobilizes International Response Following Ebola Disease Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-
response.html", "snippet": "Statement\nThe Centers for Disease Control and Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic
Republic of the Congo (DRC) and cases in Uganda. Through existing relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed
and have been actively working to support needs. Last night, the WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "WHO says 600 suspected
cases, 139 deaths in growing Ebola outbreak | Ebola News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/5/20/who-says-600-cases-139-suspected-deaths-in-growing-ebola-outbreak", "snippet":
"WHO says 600 suspected cases, 139 deaths in growing Ebola outbreak\nNumbers are expected to rise, the WHO warns, as European officials emphasise that the risk of a European outbreak is low.\n![WHO
Director-General Tedros Adhanom Ghebreyesus speaks during a press conference on Ebola outbreak in Democratic Republic of Congo and Uganda, in Geneva, on May 20, 2026.](/wp-
content/uploads/2026/05/afp_6a0da925d9d5-1779280165.jpg?resize=770%2C513&quality=80)\nThe number of suspected Ebola cases in Democrati", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Africa CDC Ebola weekly report Bundibugyo DRC update 2026"
}
```

### 📋 Result

```
{"query": "Africa CDC Ebola weekly report Bundibugyo DRC update 2026", "results": [{"title": "Ebola Disease: Current Situation | Ebola | CDC", "url": "https://www.cdc.gov/ebola/situation-
summary/index.html", "snippet": "Key points\n- CDC is responding to an outbreak of Ebola disease in remote areas of the Democratic Republic of the Congo (DRC) and Uganda.\n- To date, no cases of Ebola
disease have been confirmed in the United States because of this outbreak.\n- The overall risk to the American public and travelers remains low.\n![Micrograph image of orthoebolavirus
virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent Ebola from entering the United States\nOn ", "api_data": null, "hint": null}, {"title":
"Epidemic of Ebola Disease caused by Bundibugyo virus in the Democratic Republic of the Congo and Uganda determined a public health emergency of international concern", "url":
"https://www.who.int/news/item/17-05-2026-epidemic-of-ebola-disease-in-the-democratic-republic-of-the-congo-and-uganda-determined-a-public-health-emergency-of-international-concern", "snippet":
"Pursuant to paragraph 2 of Article 12 - Determination of a public health emergency of international concern, including a pandemic emergency of the [International Health Regulations
(2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the Director-General of the World Health Organization (WHO), after having consulted the States Parties where the event is
known to be currently occurring, is hereby determining that the Ebola disease caused by Bundibugyo virus in the Democr", "api_data": null, "hint": null}, {"title": "Africa CDC Calls for Urgent
Regional Coordination Following Ebola Outbreak in Ituri Province, DRC, and Imported Ebola Bundibugyo Case Reported by Uganda \u2013 Africa CDC", "url": "https://africacdc.org/news-item/africa-cdc-
calls-for-urgent-regional-coordination-following-ebola-virus-disease-outbreak-in-ituri-province-drc-and-imported-ebola-bundibugyo-case-reported-by-uganda/", "snippet": "Addis Ababa, Ethiopia /
Kinshasa, DRC / Kampala, Uganda, 15 May 2026 \u2014 The Africa Centres for Disease Control and Prevention (Africa CDC) is closely monitoring the confirmed Ebola outbreak in Ituri Province, Democratic
Republic of the Congo (DRC), and the imported Ebola Bundibugyo case reported by the Uganda Ministry of Health. Africa CDC is working with national authorities and partners to support a rapid,
coordinated regional response aimed at interrupting transmission, protecting communities ", "api_data": null, "hint": null}, {"title": "CDC Mobilizes International Response Following Ebola Disease
Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-response.html", "snippet": "Statement\nThe Centers for Disease Control and
Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic Republic of the Congo (DRC) and cases in Uganda. Through existing
relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed and have been actively working to support needs. Last night, the
WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "Ebola Disease Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC",
"url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n- Distributed via the CDC Health Alert Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an
official CDC health advisory.](/han/media/images/2025/03/HAN-Health-Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing this Health Alert Network (HAN) Health
Advisory to alert clinicians, public health practitioners, and travelers about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and Uganda caused by the Bundib",
"api_data": null, "hint": null}, {"title": "Ebola Outbreak 2026 Symptoms, How It Spreads, Pandemic Risk and More", "url": "https://www.today.com/health/news/ebola-outbreak-2026-symptoms-spread-
bundibugyo-strain-hantavirus-rcna345662", "snippet": "While the world closely watched an outbreak of hantavirus unfold on a luxury cruise ship earlier this month, another deadly infectious disease was
sweeping through one of Africa\u2019s largest countries and killing dozens: Ebola.\nAn outbreak of a rare type of Ebola in the Democratic Republic of the Congo and neighboring Uganda has caused at
least 600 suspected cases and 139 deaths so far, according to the World Health Organization.\nAmong those infected is an American doctor and missionary working in ", "api_data": null, "hint": null},
{"title": "Ebola virus disease outbreak in the Democratic Republic of the Congo and Uganda", "url": "https://www.ecdc.europa.eu/en/ebola-virus-disease-outbreak-democratic-republic-congo-and-uganda",
"snippet": "Ebola virus disease outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more information becomes available. It was last updated 21 May 18:00.\nOn 15 May
2026, Africa CDC reported an outbreak of Ebola disease in Ituri Province, DRC. Laboratory analysis at Institut National de Recherche Biomedicale of DRC identified Bundibugyo virus (BDBV). BDBV disease
is a rare disease but can cause outbreaks with high case fatality rates. Considering the available information, com", "api_data": null, "hint": null}, {"title": "EBOLA BUNDIBUGYO VIRUS DISEASE
OUTBREAK Democratic Republic of the Congo | Uganda Weekly External Situation Report 01, Data as of 18 May 2026 | WHO | Regional Office for Africa", "url":
"https://www.afro.who.int/countries/democratic-republic-of-congo/publication/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation", "snippet": "![Weekly
External Situation Report 01, Data as of 18 May 2026](/sites/default/files/2026-05/Wk_Ext_SitRep_0118052026.jpg)\nEBOLA BUNDIBUGYO VIRUS DISEASE OUTBREAK Democratic Republic of the Congo | Uganda
Weekly External Situation Report 01, Data as of 18 May 2026\nEvent description\nOn 5 May 2026, the World Health Organization (WHO) received an alert regarding an unknown illness with high mortality in
Mongbwalu Health Zone (HZ), Ituri Province, Democratic Republic of the Congo (DRC), including rep", "api_data": null, "hint": null}, {"title": "This Ebola outbreak raises questions about when it all
began \u2014 and the U.S. response", "url": "https://www.npr.org/2026/05/18/g-s1-122655/ebola-outbreak-democratic-republic-congo-uganda", "snippet": "This Ebola outbreak raises questions about when it
all began \u2014 and the U.S. response\n![A border health officer at the Busunga crossing between Uganda and the Democratic Republic of Congo checks a traveler's temperature using a contactless
infrared thermometer in Bundibugyo, on May 18, 2026. Ugandan officials confirmed that a 59-year-old man from Democratic Republic of Congo had died in Kampala after being admitted earlier in the week.
Tests showed the victim in Uganda was infected with the Bundi", "api_data": null, "hint": null}, {"title": "Africa CDC Declares the Ongoing Bundibugyo Ebola Outbreak a Public Health Emergency of
Continental Security \u2013 Africa CDC", "url": "https://africacdc.org/news-item/africa-cdc-declares-the-ongoing-bundibugyo-ebola-outbreak-a-public-health-emergency-of-continental-security/",
"snippet": "Addis Ababa, Ethiopia, 18 May 2026 \u2013 The Africa Centres for Disease Control and Prevention (Africa CDC), acting on the recommendations of its Emergency Consultative Group (ECG), has
officially declared the ongoing Bundibugyo ebolavirus disease outbreak affecting the Democratic Republic of the Congo (DRC) and Uganda a Public Health Emergency of Continental Security (PHECS).\nThis
declaration, under Article 3, Paragraph F of the Africa CDC Statute, empowers the organisation to lead and coordinate r", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.afro.who.int/countries/democratic-republic-of-congo/publication/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation",
  "prompt": "What are the exact death and case figures in the WHO SitRep 01? Get all numbers including suspected deaths, confirmed deaths, total deaths, with dates."
}
```

### 📋 Result

```
{"url": "https://www.afro.who.int/countries/democratic-republic-of-congo/publication/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation", "content":
"Based on the provided content, **no specific death or case figures are included in this WHO SitRep 01**. \n\nThe document mentions:\n- An alert regarding \"an unknown illness with high mortality\"
\n- \"Four health workers who died within four days\" (reported before 5 May 2026)\n- Uganda confirmed \"two imported cases\" on 15 and 16 May 2026\n\nHowever, the text does not provide:\n- Total
number of suspected cases\n- Total number of confirmed cases\n- Total number of suspected deaths\n- Total number of confirmed deaths\n- Any cumulative figures with specific dates\n\nThe content
appears to be an introductory section describing the outbreak's discovery and declaration, but the actual epidemiological data (case/death counts) that would typically appear in a situation report is
not included in the text provided.\n\n**Relevant links:**\nNo additional links are present in the provided content beyond the image reference for the report header.", "title": "EBOLA BUNDIBUGYO VIRUS
DISEASE OUTBREAK Democratic Republic of the Congo | Uganda Weekly External Situation Report 01, Data as of 18 May 2026"}
```

```json
{
  "url": "https://www.cdc.gov/ebola/situation-summary/index.html",
  "prompt": "What are the latest death and case figures for the 2026 Ebola Bundibugyo outbreak in DRC? Get exact numbers with dates."
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/ebola/situation-summary/index.html", "content": "[Prompt extraction failed, returning raw content]\n\nKey points\n- CDC is responding to an outbreak of Ebola disease in
remote areas of the Democratic Republic of the Congo (DRC) and Uganda.\n- To date, no cases of Ebola disease have been confirmed in the United States because of this outbreak.\n- The overall risk to
the American public and travelers remains low.\n![Micrograph image of orthoebolavirus virion](/ebola/media/images/2024/04/Ebola_virus_purple.jpg)\nCurrent situation\nImplementing measures to prevent
Ebola from entering the United States\nOn May 18, 2026, CDC and DHS implemented enhanced travel screening, entry restrictions, and public health measures to prevent Ebola virus disease from entering
the United States amid ongoing outbreaks in East and Central Africa.\nNew developments\n- To date, no Ebola cases associated with this outbreak have been reported in the United States, and the risk to
the general public remains low.\n- As of May 21, the DRC and Uganda Ministries of Health report the following:\n- A total of 575 suspected cases, 51 confirmed cases, and 148 suspected deaths.\n- These
numbers include 2 confirmed cases including 1 death in Uganda in people who traveled from DRC. No further spread has been reported.\n- This is a rapidly evolving situation, and case counts are subject
to change.\n- On May 17, an American who was exposed as part of work caring for patients in DRC tested positive for Ebola Bundibugyo disease. The patient has been transported to Germany for treatment
and care. In addition to being a shorter flight time, Germany has previous experience caring for Ebola patients.\n- High-risk contacts associated with this exposure are also being moved to Germany and
the Czech Republic.\n- On May 18, CDC, the Department of Homeland Security, and other appropriate federal agencies took\n[proactive public health measures to prevent Ebola](https://www.cdc.gov/port-
health/media/pdfs/2026-05-18-Title-42-Order.pdf)from entering the United States. - More information about enhanced travel security measures is available:\n![Ituri Province and in Nord-Kivu Province
are in the northeastern part of DRC near Uganda](/ebola/media/images/2026/05/May-20-Ebola-map.jpg)\nBackground\n- In early May, a hospital in Bunia Health Zone in northeastern DRC identified a cluster
of severe illnesses affecting healthcare workers.\n- Initial samples tested in DRC were negative for Ebola virus, but by May 15, 8 out of 13 samples tested positive, and 5 were inconclusive. Using
genetic fingerprinting, the illnesses were identified as Bundibugyo (Bun-dee-BOO-joh) virus, one of the\n[4 types of
orthoebolaviruses](https://www.cdc.gov/ebola/about/index.html#cdc_disease_basics_types-types)that cause Ebola disease in people. - There is no vaccine for Bundibugyo virus,
and\n[treatment](https://www.cdc.gov/ebola/about/index.html)consists of supportive care. - There have been 2 previous outbreaks of Bundibugyo virus, 1 in Uganda and 1 in DRC, with death rates of 25%
and 50%, respectively.\n- Patients have experienced classic\n[Ebola disease symptoms](https://www.cdc.gov/ebola/about/index.html)like fever, headache, vomiting, severe weakness, abdominal pain,
nosebleeds, and vomiting blood. - In DRC, most cases to date have been in people between 20 and 39 years old, and two-thirds have been in female patients.\n- This is the 17th outbreak of Ebola in DRC
since 1976. The most recent outbreak ended in December 2025.\nCDC response\nCDC is working with international partners and the Ministries of Health on this evolving situation. CDC is further
supporting response efforts through our country offices in DRC and Uganda to provide technical assistance with:\n- Disease tracking and contact tracing\n- Laboratory sample collection and virus
sequencing\n- Infection prevention and control (IPC) efforts\n- Local border screening\n- Coordinating with affected countries and international public health partners\n- Providing personal protective
equipment (PPE) and infection control supplies\n- Risk communication and community engagement in affected areas\nCDC is working with other U.S. Government agencies and international partners to move
the American who tested positive for Ebola on May 17 and other Americans at high risk out of DRC for care.\nIn the United States\n- CDC has travel health notices in place
for\n[DRC](https://wwwnc.cdc.gov/travel/notices/level2/ebola-democratic-republic-of-the-congo)and[Uganda](https://wwwnc.cdc.gov/travel/notices/level1/ebola-uganda)to help Americans planning travel to
either country in the near future learn how to keep themselves safe from Ebola. - CDC is taking\n[proactive public health measures to prevent Ebola](https://www.cdc.gov/port-
health/media/pdfs/2026-05-18-Title-42-Order.pdf)from entering the United States, including:- Enhancing public health screening and traveler monitoring for individuals arriving from the DRC, Uganda,
and South Sudan\n- Putting entry restrictions on non-U.S. passport holders if they have been in Uganda, DRC, or South Sudan in the previous 21 days\n- Coordinating with airlines, international
partners, and port-of-entry officials to identify and manage travelers who may have been exposed to Ebola\n- Enhancing port health protection response activities, contact tracing, laboratory testing
capacity, and hospital readiness nationwide\n- Continuing deployment of CDC personnel to support outbreak containment efforts in affected regions\n- CDC has extensive\n[clinical
guidance](https://www.cdc.gov/ebola/hcp/clinical-guidance/index.html)and[training](https://www.cdc.gov/ebola/hcp/training/index.html)for both U.S. and non-U.S. settings, including[Infection Prevention
and Control Recommendations for Patients in U.S. Hospitals who are Suspected or Confirmed to have Selected Viral Hemorrhagic Fevers](https://www.cdc.gov/viral-hemorrhagic-fevers/hcp/infection-
control/index.html). - CDC is also coordinating with health departments nationwide to:\n- Follow established patient assessment protocols if BVD is suspected in a patient with concerning clinical and
epidemiologic history.\n- Coordinate patient management, specimen collection, and BVD testing with state, tribal, local, and territorial health departments, CDC, and clinical teams.\n- CDC is also
supporting U.S. Government interagency efforts to coordinate the safe withdrawal of a small number of Americans who are directly affected in outbreak areas.\n- Long-standing laboratory preparedness
efforts are online for suspected viral hemorrhagic fevers like Ebola to allow for testing directly at CDC or through one of 41\n[Laboratory Response Network](https://www.cdc.gov/laboratory-response-
network/php/about/index.html)public health laboratories.", "title": "Ebola Disease: Current Situation"}
```

## 💭 Thinking

Now I have a solid picture of the data. Let me compile the key data points and run a simulation.

Key data points for deaths:
- May 15 (Africa CDC press release): ~65 deaths (among suspected cases), ~80 suspected community deaths (WHO AFRO)
- May 15 (WHO DON): 246 suspected cases, 80 deaths (4 among confirmed)
- May 18 (Africa CDC PHECS declaration): ~395 suspected cases, ~106 deaths (DRC + Uganda combined, so ~105 in DRC)
- May 19 (CARE/MSF): 536 suspected cases, 134 deaths


- May 19 (Wikipedia): 543 suspected cases, at least 131 deaths
- May 20 (WHO DG briefing / Project HOPE): ~600 suspected cases, 139 deaths, 51 confirmed cases
- May 21 (US CDC, data as of May 21): 575 suspected cases, 51 confirmed cases, 148 suspected deaths

Looking at the death trajectory, I see a steady climb from 65-80 deaths on May 15, reaching about 106 by May 18, then continuing to rise through 131-134 by May 19, 139 by May 20, and 148 by May 21. The resolution hinges on what Africa CDC officially reports by May 31.

Africa CDC has only published two updates so far—a May 15 press release showing 65 deaths and a May 18 declaration reporting around 106 deaths (with the DRC portion being roughly 105). Since the question resolves using the higher figure when both narrow and broad estimates exist, any future Africa CDC updates will likely reflect the more inclusive counts. Based on the growth pattern from May 15 to May 21, where deaths increased by 68 over six days, I need to project what the count might reach by May 31. The Africa CDC publishes weekly epidemic reports, so they'll likely release more updates before May 31, and given the rapid growth trajectory with cases doubling every 4-5 days, the lack of available vaccines, and the constrained response efforts due to insecurity and limited testing capacity, I need to project what their official count will capture over the next 10 days from May 21 onward.

Looking at the death growth pattern more closely, the rate appears to be accelerating—roughly 33-40% growth every 3 days in mid-May—which suggests the trajectory could continue climbing, though testing limitations and reporting delays will affect what actually gets documented in the Africa CDC's official reports. of deaths, plus expanding surveillance revealing more cases in previously unreached areas. For Ebola outbreaks, I'm thinking through the typical progression: early exponential growth, a peak around 4-8 weeks after detection and response begins, then decline as interventions take hold. This outbreak was detected in early May and confirmed mid-May, with major response efforts starting around May 15-18, so we're likely still in the growth phase through late May before interventions fully take effect. I should also factor in that Bundibugyo Ebola has a lower case fatality rate (around 25-32%) compared to Zaire strains, and consider that Africa CDC declared PHECS on May 18 and will probably issue regular updates, though the question specifies using 65 deaths if there's no update beyond May 15.

Now I'm setting up a Monte Carlo simulation to model the trajectory properly. The key variables are the current death count around May 21 at roughly 148, an initial daily growth rate of 10-11% that should decelerate over time, and a 10-day window through May 31. I need to account for the fact that Africa CDC's reported figures lag actual deaths by a few days and include suspected, confirmed, and community deaths. There are competing dynamics at play: real deaths accumulating, reporting catching up with previously uncounted community deaths, and the response efforts slowing transmission.

I'm building out different scenarios to capture the range of outcomes. The base case assumes the epidemic continues growing but the response starts taking effect, with deaths accelerating at 7-10% daily for about five days before slowing to 3-5% daily, landing somewhere between 250-350 deaths by May 31. The optimistic scenario models an effective early response where growth drops to around 5% daily and decelerates quickly.

The pessimistic scenario assumes the outbreak maintains near-exponential growth at 10%+ daily across most of the period, pushing toward 350-500+ deaths. I also need to account for reporting lag—Africa CDC's published figure by May 31 might only reflect deaths counted through May 28 or so, not the absolute latest numbers. Let me run a proper simulation to work through these scenarios.

## 💬 Response

Now I have comprehensive data. Let me run a Monte Carlo simulation to model the death trajectory.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Compile the death trajectory data points\n# Using the most inclusive figures from reliable sources\ndata_points = {\n    # (date_offset from May 15, deaths, source)\n    'May 15 WHO DON': (0, 80),      # WHO DON report: 80 deaths\n    'May 15 Africa CDC': (0, 65),    # Africa CDC press release: 65 deaths\n    'May 18 Africa CDC PHECS': (3, 106),  # Africa CDC PHECS: ~106 (DRC+Uganda combined, -1 for Uganda)\n    'May 19 CARE/MSF': (4, 134),     # CARE: 134 deaths\n    'May 19 Wikipedia': (4, 131),    # Wikipedia: at least 131\n    'May 20 WHO DG': (5, 139),       # WHO DG briefing: 139\n    'May 21 US CDC': (6, 148),       # US CDC situation page: 148 suspected deaths\n}\n\nprint(\"Death trajectory data points:\")\nfor name, (day, deaths) in data_points.items():\n    print(f\"  {name}: Day {day} (May {15+day}), {deaths} deaths\")\n\n# Use the best/highest figures for each date to get the trajectory\n# (since question uses \"more inclusive\" figure)\ntrajectory = [\n    (0, 80),    # May 15 (WHO's broader figure)\n    (3, 106),   # May 18\n    (4, 134),   # May 19\n    (5, 139),   # May 20\n    (6, 148),   # May 21\n]\n\n# Calculate daily growth rates between adjacent points\nprint(\"\\nDaily growth rates:\")\nfor i in range(1, len(trajectory)):\n    d0, n0 = trajectory[i-1]\n    d1, n1 = trajectory[i]\n    days = d1 - d0\n    total_growth = n1 / n0\n    daily_growth = total_growth ** (1/days)\n    print(f\"  May {15+d0} to May {15+d1} ({days} days): {n0} \u2192 {n1}, \"\n          f\"total \u00d7{total_growth:.3f}, daily \u00d7{daily_growth:.4f} ({(daily_growth-1)*100:.1f}%/day)\")\n\n# Overall growth rate May 15-21\noverall_growth = (148/80) ** (1/6)\nprint(f\"\\nOverall May 15-21: 80 \u2192 148, daily \u00d7{overall_growth:.4f} ({(overall_growth-1)*100:.1f}%/day)\")\n\n# Recent growth rate (May 18-21) - more representative of current phase\nrecent_growth = (148/106) ** (1/3)\nprint(f\"Recent May 18-21: 106 \u2192 148, daily \u00d7{recent_growth:.4f} ({(recent_growth-1)*100:.1f}%/day)\")\n\n# Very recent (May 19-21)\nvery_recent_growth = (148/134) ** (1/2)\nprint(f\"Very recent May 19-21: 134 \u2192 148, daily \u00d7{very_recent_growth:.4f} ({(very_recent_growth-1)*100:.1f}%/day)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Death trajectory data points:\n  May 15 WHO DON: Day 0 (May 15), 80 deaths\n  May 15 Africa CDC: Day 0 (May 15), 65 deaths\n  May 18 Africa CDC PHECS: Day 3 (May 18), 106
deaths\n  May 19 CARE/MSF: Day 4 (May 19), 134 deaths\n  May 19 Wikipedia: Day 4 (May 19), 131 deaths\n  May 20 WHO DG: Day 5 (May 20), 139 deaths\n  May 21 US CDC: Day 6 (May 21), 148 deaths\n\nDaily
growth rates:\n  May 15 to May 18 (3 days): 80 \u2192 106, total \u00d71.325, daily \u00d71.0983 (9.8%/day)\n  May 18 to May 19 (1 days): 106 \u2192 134, total \u00d71.264, daily \u00d71.2642
(26.4%/day)\n  May 19 to May 20 (1 days): 134 \u2192 139, total \u00d71.037, daily \u00d71.0373 (3.7%/day)\n  May 20 to May 21 (1 days): 139 \u2192 148, total \u00d71.065, daily \u00d71.0647
(6.5%/day)\n\nOverall May 15-21: 80 \u2192 148, daily \u00d71.1080 (10.8%/day)\nRecent May 18-21: 106 \u2192 148, daily \u00d71.1177 (11.8%/day)\nVery recent May 19-21: 134 \u2192 148, daily
\u00d71.0509 (5.1%/day)\n", "stderr": "", "duration_ms": 230}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\n\n# Monte Carlo simulation for cumulative deaths by May 31\n# Current state: ~148 deaths as of May 21\n# Resolution: Africa CDC report by May 31\n\n# Key considerations:\n# 1. Africa CDC will report a figure that could be from data collected up to ~May 28-30\n#    (given reporting lag of 1-3 days)\n# 2. The question uses the \"more inclusive\" figure\n# 3. Response is scaling but no vaccine, insecurity constraints\n\n# Parameters\ncurrent_deaths = 148  # As of May 21\ndays_remaining = 10   # May 21 to May 31\n\n# The death growth has been variable:\n# Overall ~10.8%/day (May 15-21), but showing signs of deceleration recently\n# Very recent: 5.1%/day (May 19-21)\n# The high figure on May 18->19 likely reflects catchup reporting\n\nn_sims = 100000\n\n# Model: daily growth rate that decelerates over time\n# Initial growth rate drawn from a distribution centered on recent observations\n# Growth rate decays as response takes effect\n\n# Scenario mixture approach:\n# Scenario 1 (40%): Moderate growth - response starts working\n#   - Initial daily growth: 6-8%, decelerating to 2-4% by May 31\n# Scenario 2 (30%): Continued rapid growth - response delayed by insecurity\n#   - Initial daily growth: 8-12%, slow deceleration  \n# Scenario 3 (20%): Rapid deceleration - effective response\n#   - Initial daily growth: 4-6%, decelerating to 1-2%\n# Scenario 4 (10%): Explosive growth - spread to new areas\n#   - Initial daily growth: 10-15%, minimal deceleration\n\n# Also need to account for:\n# - Retrospective identification of community deaths (upward revision)\n# - Reporting lag (Africa CDC may report figures from ~2 days before publication)\n# - Africa CDC uses \"more inclusive\" figure\n\nresults = np.zeros(n_sims)\n\nfor i in range(n_sims):\n    # Draw scenario\n    u = np.random.random()\n    \n    if u < 0.40:  # Moderate growth\n        init_growth = np.random.normal(0.07, 0.015)\n        decel_rate = np.random.uniform(0.04, 0.08)  # how much growth decays per day\n    elif u < 0.70:  # Continued rapid growth\n        init_growth = np.random.normal(0.10, 0.02)\n        decel_rate = np.random.uniform(0.02, 0.05)\n    elif u < 0.90:  # Rapid deceleration\n        init_growth = np.random.normal(0.05, 0.015)\n        decel_rate = np.random.uniform(0.06, 0.10)\n    else:  # Explosive growth\n        init_growth = np.random.normal(0.13, 0.03)\n        decel_rate = np.random.uniform(0.01, 0.03)\n    \n    # Simulate day by day\n    deaths = current_deaths\n    for day in range(days_remaining):\n        # Growth rate decays\n        daily_growth = max(0.005, init_growth * np.exp(-decel_rate * day))\n        # Add stochastic variation\n        daily_growth_actual = daily_growth + np.random.normal(0, 0.02)\n        daily_growth_actual = max(0, daily_growth_actual)\n        deaths = deaths * (1 + daily_growth_actual)\n    \n    # Add retrospective community death identification factor\n    # Africa CDC may include community deaths discovered through retroactive investigation\n    retro_factor = 1.0 + np.random.uniform(0, 0.08)  # 0-8% additional from retroactive ID\n    deaths *= retro_factor\n    \n    # Subtract 1-3 days of growth for reporting lag\n    # Africa CDC's figure may be from 1-3 days before May 31\n    # But this is partially offset by them using the \"more inclusive\" figure\n    # Net effect: small negative adjustment already captured in uncertainty\n    \n    results[i] = deaths\n\n# Clip to bounds\nresults = np.clip(results, 50, None)\n\n# Calculate percentiles\npercentiles = [1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 99]\npct_values = np.percentile(results, percentiles)\n\nprint(\"Monte Carlo Results (100,000 simulations):\")\nprint(f\"Mean: {np.mean(results):.0f}\")\nprint(f\"Median: {np.median(results):.0f}\")\nprint(f\"Std Dev: {np.std(results):.0f}\")\nprint()\nprint(\"Percentile Distribution:\")\nfor p, v in zip(percentiles, pct_values):\n    print(f\"  P{p:2d}: {v:.0f}\")\n\nprint(f\"\\nProbability > 500: {np.mean(results > 500)*100:.1f}%\")\nprint(f\"Probability > 300: {np.mean(results > 300)*100:.1f}%\")\nprint(f\"Probability > 200: {np.mean(results > 200)*100:.1f}%\")\nprint(f\"Probability < 100: {np.mean(results < 100)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Monte Carlo Results (100,000 simulations):\nMean: 304\nMedian: 277\nStd Dev: 96\n\nPercentile Distribution:\n  P 1: 182\n  P 5: 200\n  P10: 212\n  P15: 222\n  P20: 230\n
P25: 238\n  P30: 245\n  P40: 260\n  P50: 277\n  P60: 299\n  P70: 328\n  P75: 346\n  P80: 368\n  P85: 394\n  P90: 428\n  P95: 491\n  P99: 646\n\nProbability > 500: 4.5%\nProbability > 300:
39.5%\nProbability > 200: 95.0%\nProbability < 100: 0.0%\n", "stderr": "", "duration_ms": 1404}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also consider what Africa CDC specifically reports vs. what the actual numbers are\n# The question resolves on Africa CDC's reported figure, not necessarily the actual figure\n# Africa CDC may have fewer data points or use figures from a few days before their report\n\n# Key issue: Africa CDC's May 15 report said 65, but WHO/others cite 80 for the same date\n# Africa CDC's May 18 PHECS said ~106 (approx 395 suspected cases, 106 deaths)\n# The question says to use the \"higher (more inclusive) figure\"\n\n# Let me also consider that Africa CDC might NOT update frequently enough\n# Their Epidemic Intelligence Weekly Reports come out weekly\n# They've published on May 15 and May 18 so far\n\n# Scenario A (70%): Africa CDC publishes at least 1-2 more updates by May 31\n#   - These updates will reflect data up to roughly May 25-29\n#   - The reported figure will lag the actual epidemic by 2-4 days\n#   \n# Scenario B (20%): Africa CDC publishes a weekly situation report around May 25\n#   - Data reflects situation as of ~May 23-24\n#   - Figure would be ~170-200 range\n#\n# Scenario C (10%): Africa CDC doesn't publish any new update\n#   - Resolution uses the May 18 figure of 106\n#   - BUT this is very unlikely given PHEIC/PHECS status\n\n# Given PHEIC/PHECS declaration, Africa CDC will almost certainly publish multiple\n# updates. WHO SitRep 02 would come around May 25 (weekly from May 18).\n\n# Let me also think about whether the Africa CDC figure includes the broader \n# \"community deaths\" or just \"deaths among reported cases\"\n# The question says to use the higher figure.\n\n# Actually, let me re-examine. The current data has:\n# - As of May 21 (US CDC): 575 suspected cases, 51 confirmed, 148 deaths\n# - The \"148\" seems to be suspected deaths, not just confirmed deaths\n\n# For the Africa CDC, their May 15 report said \"65 deaths\" which was the narrower figure\n# WHO's DON for the same date said \"80 deaths\" (broader including community)\n# But Africa CDC's May 18 figure of 106 likely already includes broader community deaths\n\n# The key question: what will Africa CDC's latest figure be as of ~May 28-30?\n\n# Let me also check: what's the reporting cadence?\n# Africa CDC declared PHECS May 18\n# They will likely issue weekly Epidemic Intelligence reports\n# Expected: ~May 22 (EIWR), ~May 29 (EIWR)\n# Plus possible ad-hoc situation reports\n\n# Given the high-profile PHEIC/PHECS status, I expect Africa CDC to publish\n# at least 2 more updates (around May 22/23 and May 29/30)\n\n# Let me adjust the simulation to account for the fact that the resolution\n# figure is from Africa CDC's report, which uses data from a reporting cutoff\n\n# The simulation above already captures this broadly through the growth model\n# The main additional consideration is reporting lag\n\n# Let me do a sensitivity test with different initial growth assumptions\n\nprint(\"Sensitivity Analysis:\")\nprint(\"=\" * 60)\n\nfor init_growth_center in [0.04, 0.06, 0.08, 0.10, 0.12]:\n    test_results = np.zeros(50000)\n    for i in range(50000):\n        init_growth = np.random.normal(init_growth_center, 0.015)\n        decel_rate = np.random.uniform(0.03, 0.07)\n        deaths = current_deaths\n        for day in range(days_remaining):\n            daily_growth = max(0.005, init_growth * np.exp(-decel_rate * day))\n            daily_growth_actual = daily_growth + np.random.normal(0, 0.015)\n            daily_growth_actual = max(0, daily_growth_actual)\n            deaths = deaths * (1 + daily_growth_actual)\n        retro_factor = 1.0 + np.random.uniform(0, 0.05)\n        deaths *= retro_factor\n        test_results[i] = deaths\n    \n    p10, p50, p90 = np.percentile(test_results, [10, 50, 90])\n    print(f\"Init growth={init_growth_center*100:.0f}%/day: P10={p10:.0f}, P50={p50:.0f}, P90={p90:.0f}\")\n\n# Also consider Africa CDC's reporting figure vs actual\n# Africa CDC figure typically is a subset of actual deaths\n# But question says use \"more inclusive\" figure\n# Still, reporting lag + undercount could mean Africa CDC reports ~80-90% of actual\n\nprint(\"\\n\\nAdjusted for Africa CDC reporting (80-95% of actual):\")\nadjusted_results = results * np.random.uniform(0.80, 0.95, n_sims)\nadjusted_results = np.clip(adjusted_results, 50, None)\n\npercentiles_adj = [1, 5, 10, 20, 25, 40, 50, 60, 75, 80, 90, 95, 99]\npct_values_adj = np.percentile(adjusted_results, percentiles_adj)\nprint(f\"Adjusted Mean: {np.mean(adjusted_results):.0f}\")\nprint(f\"Adjusted Median: {np.median(adjusted_results):.0f}\")\nfor p, v in zip(percentiles_adj, pct_values_adj):\n    print(f\"  P{p:2d}: {v:.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Sensitivity Analysis:\n============================================================\nInit growth=4%/day: P10=179, P50=208, P90=245\nInit growth=6%/day: P10=207, P50=243,
P90=286\nInit growth=8%/day: P10=241, P50=283, P90=333\nInit growth=10%/day: P10=280, P50=329, P90=387\nInit growth=12%/day: P10=325, P50=381, P90=449\n\n\nAdjusted for Africa CDC reporting (80-95% of
actual):\nAdjusted Mean: 266\nAdjusted Median: 243\n  P 1: 156\n  P 5: 173\n  P10: 184\n  P20: 200\n  P25: 207\n  P40: 228\n  P50: 243\n  P60: 262\n  P75: 303\n  P80: 322\n  P90: 376\n  P95: 432\n
P99: 570\n", "stderr": "", "duration_ms": 3333}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me think more carefully about the appropriate model\n# \n# The key question is: what is the CURRENT growth rate and how will it change?\n#\n# Recent data suggests deceleration:\n# - May 15-18 (3 days): 80\u2192106, ~9.8%/day\n# - May 18-21 (3 days): 106\u2192148, ~11.8%/day  \n# - But May 19-21 specifically: 134\u2192148, ~5.1%/day\n#\n# The jump from 106 to 134 in one day (May 18\u219219) likely reflects\n# reporting catchup, not actual daily deaths.\n#\n# More realistic interpretation:\n# - True daily death accrual is ~10-15 deaths/day (linear, not exponential)\n# - From May 15 to May 21 (6 days): 80\u2192148 = 68 deaths = ~11.3/day\n# - From May 18 to May 21 (3 days): 106\u2192148 = 42 deaths = 14/day\n# - From May 20 to May 21 (1 day): 139\u2192148 = 9 deaths in 1 day\n#\n# This is more consistent with a roughly linear accumulation pattern\n# with some day-to-day noise (especially from reporting batches)\n#\n# For a linear model:\n# If ~12-14 deaths/day and increasing slightly:\n# 10 more days \u00d7 12-14 deaths/day = 120-140 more deaths\n# 148 + 120-140 = 268-288 by May 31\n#\n# But the epidemic is growing (more cases \u2192 more deaths)\n# The 600+ suspected cases with ~25% CFR suggests eventual deaths of ~150+\n# from currently known cases alone\n# New cases are still accumulating\n#\n# Let me model this differently - using both epidemic dynamics AND\n# linear extrapolation as separate approaches\n\n# Approach 1: Simple linear extrapolation\n# Recent daily deaths: 9-14/day\n# Assume this continues or grows slightly\n\n# Approach 2: Epidemic model with growth and deceleration\n# Cases growing, deaths lag by ~5-10 days\n\n# Let me think about it from the case perspective:\n# ~600 suspected cases as of May 20\n# CFR for Bundibugyo: ~25-40%\n# Expected deaths from existing cases: 150-240\n# Current deaths: 148 \u2192 most case-deaths from earliest cases already realized\n# But new cases accumulating at ~30-50/day\n# These will generate deaths with ~7-14 day lag\n\n# Actually, deaths have been 148 out of 600 cases = 24.7% CFR so far\n# This is consistent with the Bundibugyo ~25% historical CFR\n# Some cases are still in progress (may die later)\n\n# Better model: think of it as:\n# 1. Deaths from existing cases not yet dead\n# 2. Deaths from new cases that will accumulate May 21-31\n\n# Existing cases as of May 21: ~575 suspected + 51 confirmed\n# Deaths so far: 148\n# Remaining deaths from existing cases (assuming ~25-30% eventual CFR):\n#   - Total expected deaths from 575-625 cases: 144-188\n#   - Already 148 \u2192 suggests many existing cases have already resolved\n#   - But some cases are recent and still progressing\n#   - Estimate ~20-40 more deaths from existing cases\n\n# New cases May 21-31:\n#   - Current case accrual: ~30-60 cases/day\n#   - If this decelerates to ~20-40/day by late May\n#   - Total new cases: ~250-500 over 10 days\n#   - Deaths from new cases (with lag): ~30-80 (only ~50% of expected deaths\n#     will have occurred by May 31 given 7-14 day time to death)\n\n# Total by May 31: 148 + 20-40 + 30-80 = 198-268\n\n# BUT: there's also retroactive identification of community deaths\n# The initial jump from 65 to 80 to 106 partly reflects this\n# Could add another 20-50 deaths discovered through investigation\n\n# Revised estimate: 198-268 + 20-50 = 218-318\n\n# This is broadly consistent with my Monte Carlo results above\n\n# Let me do a final refined simulation\nnp.random.seed(123)\nn_sims = 200000\n\nfinal_results = np.zeros(n_sims)\n\nfor i in range(n_sims):\n    # Current deaths\n    deaths = 148\n    \n    # Component 1: Deaths from existing ~600 cases not yet dead\n    # Assume ~20-40% of existing cases haven't resolved yet\n    # CFR ~25-35% of those\n    existing_unresolved = np.random.uniform(100, 250)  # unresolved cases\n    cfr = np.random.uniform(0.22, 0.35)\n    additional_from_existing = existing_unresolved * cfr\n    # Not all will die by May 31 - maybe 60-90% resolve by then\n    resolution_fraction = np.random.uniform(0.5, 0.9)\n    deaths += additional_from_existing * resolution_fraction\n    \n    # Component 2: New cases and deaths May 21-31\n    # Daily new cases: starts ~40-60/day, may change\n    u = np.random.random()\n    if u < 0.35:  # Growth slowing significantly\n        daily_new_cases_start = np.random.uniform(25, 45)\n        daily_new_cases_end = np.random.uniform(15, 30)\n    elif u < 0.75:  # Moderate growth continuing\n        daily_new_cases_start = np.random.uniform(40, 65)\n        daily_new_cases_end = np.random.uniform(30, 55)\n    elif u < 0.92:  # Rapid growth continuing\n        daily_new_cases_start = np.random.uniform(55, 90)\n        daily_new_cases_end = np.random.uniform(45, 80)\n    else:  # Explosive growth\n        daily_new_cases_start = np.random.uniform(80, 130)\n        daily_new_cases_end = np.random.uniform(60, 120)\n    \n    # Generate new cases over 10 days with interpolation\n    total_new_cases = 0\n    for day in range(10):\n        frac = day / 9\n        daily_cases = daily_new_cases_start * (1 - frac) + daily_new_cases_end * frac\n        daily_cases += np.random.normal(0, daily_cases * 0.2)  # noise\n        daily_cases = max(5, daily_cases)\n        total_new_cases += daily_cases\n    \n    # Deaths from new cases: lag of 7-14 days from symptom onset\n    # Cases from May 21-24 may die by May 31\n    # Cases from May 25+ mostly won't die by May 31\n    # ~40% of new cases will have had time to die by May 31\n    fraction_dying_by_may31 = np.random.uniform(0.2, 0.5)\n    deaths_from_new = total_new_cases * cfr * fraction_dying_by_may31\n    deaths += deaths_from_new\n    \n    # Component 3: Retroactive community death identification\n    # Ongoing investigation may reveal previously uncounted deaths\n    retro_deaths = np.random.uniform(5, 40)\n    deaths += retro_deaths\n    \n    # Component 4: Africa CDC reporting adjustment\n    # Africa CDC report may use data from 1-3 days before publication\n    # But they use \"more inclusive\" figure\n    # Net effect: slight undercount vs actual\n    reporting_factor = np.random.uniform(0.85, 1.0)\n    deaths *= reporting_factor\n    \n    final_results[i] = max(50, deaths)\n\n# Extract percentiles\npercentiles_full = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 98, 99]\npct_values_full = np.percentile(final_results, percentiles_full)\n\nprint(\"Final Monte Carlo Results (200,000 simulations):\")\nprint(f\"Mean: {np.mean(final_results):.0f}\")\nprint(f\"Median: {np.median(final_results):.0f}\")\nprint(f\"Std Dev: {np.std(final_results):.0f}\")\nprint()\nprint(\"Percentile Distribution:\")\nfor p, v in zip(percentiles_full, pct_values_full):\n    print(f\"  P{p:2d}: {v:.0f}\")\n\nprint(f\"\\nProbability > 500: {np.mean(final_results > 500)*100:.1f}%\")\nprint(f\"Probability > 400: {np.mean(final_results > 400)*100:.1f}%\")\nprint(f\"Probability > 300: {np.mean(final_results > 300)*100:.1f}%\")\nprint(f\"Probability > 200: {np.mean(final_results > 200)*100:.1f}%\")\nprint(f\"Probability < 150: {np.mean(final_results < 150)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Final Monte Carlo Results (200,000 simulations):\nMean: 235\nMedian: 231\nStd Dev: 31\n\nPercentile Distribution:\n  P 1: 180\n  P 2: 185\n  P 5: 192\n  P10: 199\n  P15:
205\n  P20: 209\n  P25: 213\n  P30: 217\n  P40: 224\n  P50: 231\n  P60: 238\n  P70: 246\n  P75: 252\n  P80: 257\n  P85: 265\n  P90: 274\n  P95: 291\n  P98: 311\n  P99: 326\n\nProbability > 500:
0.0%\nProbability > 400: 0.0%\nProbability > 300: 3.3%\nProbability > 200: 89.6%\nProbability < 150: 0.0%\n", "stderr": "", "duration_ms": 3268}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The case-based model gives a pretty narrow distribution (SD=31). \n# This seems too narrow - it doesn't fully capture:\n# 1. Possibility of explosive growth (spreading to Goma, new provinces)\n# 2. Possibility of massive community death undercount being discovered\n# 3. Possibility of Africa CDC not updating beyond May 18 (106 deaths)\n# 4. Uncertainty in actual epidemic dynamics\n#\n# Let me combine the two approaches and add more tail weight\n\nnp.random.seed(456)\nn_sims = 200000\n\ncombined_results = np.zeros(n_sims)\n\nfor i in range(n_sims):\n    # Draw from one of several models with different assumptions\n    model = np.random.random()\n    \n    if model < 0.05:\n        # Scenario 0 (5%): Africa CDC doesn't update beyond May 18\n        # Resolution = 106 deaths (May 18 figure)\n        combined_results[i] = 106\n        continue\n    \n    if model < 0.10:\n        # Scenario 0b (5%): Africa CDC only updates once more with ~May 22 data\n        # Would report ~160-180 deaths\n        combined_results[i] = np.random.uniform(148, 190)\n        continue\n    \n    # For remaining 90%: Africa CDC updates at least through ~May 28-29\n    \n    if model < 0.30:\n        # Scenario 1 (20%): Rapid response effectiveness\n        # Growth decelerates quickly, ~4-6%/day declining\n        init_rate = np.random.normal(0.05, 0.015)\n        decel = np.random.uniform(0.06, 0.12)\n    elif model < 0.65:\n        # Scenario 2 (35%): Moderate - base case\n        # Growth around 6-9%/day with moderate deceleration\n        init_rate = np.random.normal(0.075, 0.02)\n        decel = np.random.uniform(0.04, 0.08)\n    elif model < 0.85:\n        # Scenario 3 (20%): Sustained growth\n        # Growth 8-12%/day with slow deceleration\n        init_rate = np.random.normal(0.10, 0.025)\n        decel = np.random.uniform(0.02, 0.05)\n    elif model < 0.95:\n        # Scenario 4 (10%): Explosive/severe\n        # Spread to major population centers, growth 10-15%/day\n        init_rate = np.random.normal(0.13, 0.03)\n        decel = np.random.uniform(0.01, 0.04)\n    else:\n        # Scenario 5 (5%): Very severe / major community death discovery\n        init_rate = np.random.normal(0.15, 0.04)\n        decel = np.random.uniform(0.005, 0.03)\n    \n    # Simulate 10 days from current 148 deaths\n    deaths = 148.0\n    for day in range(10):\n        rate = max(0.005, init_rate * np.exp(-decel * day))\n        rate_actual = rate + np.random.normal(0, 0.02)\n        rate_actual = max(-0.01, rate_actual)\n        deaths *= (1 + rate_actual)\n    \n    # Add retroactive community death identification\n    retro = np.random.uniform(5, 50)\n    deaths += retro\n    \n    # Africa CDC reporting factor: data cutoff ~2 days before May 31\n    # so effectively ~8 days of growth from current, not 10\n    # Offset: the question uses \"more inclusive\" figure\n    # Apply a small discount\n    lag_factor = np.random.uniform(0.85, 1.0)\n    deaths *= lag_factor\n    \n    combined_results[i] = max(50, deaths)\n\n# Extract percentiles\npercentiles_full = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 98, 99]\npct_values_full = np.percentile(combined_results, percentiles_full)\n\nprint(\"Combined Model Results (200,000 simulations):\")\nprint(f\"Mean: {np.mean(combined_results):.0f}\")\nprint(f\"Median: {np.median(combined_results):.0f}\")\nprint(f\"Std Dev: {np.std(combined_results):.0f}\")\nprint()\nprint(\"Percentile Distribution:\")\nfor p, v in zip(percentiles_full, pct_values_full):\n    print(f\"  P{p:2d}: {v:.0f}\")\n\nprint(f\"\\nProbability > 500: {np.mean(combined_results > 500)*100:.1f}%\")\nprint(f\"Probability > 400: {np.mean(combined_results > 400)*100:.1f}%\")\nprint(f\"Probability > 300: {np.mean(combined_results > 300)*100:.1f}%\")\nprint(f\"Probability > 250: {np.mean(combined_results > 250)*100:.1f}%\")\nprint(f\"Probability > 200: {np.mean(combined_results > 200)*100:.1f}%\")\nprint(f\"Probability < 150: {np.mean(combined_results < 150)*100:.1f}%\")\nprint(f\"Probability < 120: {np.mean(combined_results < 120)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Combined Model Results (200,000 simulations):\nMean: 293\nMedian: 268\nStd Dev: 122\n\nPercentile Distribution:\n  P 1: 106\n  P 2: 106\n  P 5: 106\n  P10: 178\n  P15:
195\n  P20: 209\n  P25: 220\n  P30: 229\n  P40: 248\n  P50: 268\n  P60: 291\n  P70: 320\n  P75: 339\n  P80: 363\n  P85: 396\n  P90: 443\n  P95: 526\n  P98: 635\n  P99: 721\n\nProbability > 500:
6.2%\nProbability > 400: 14.5%\nProbability > 300: 36.4%\nProbability > 250: 58.8%\nProbability > 200: 83.4%\nProbability < 150: 5.3%\nProbability < 120: 5.1%\n", "stderr": "", "duration_ms": 2673}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The P1-P5 values at 106 reflect the scenario where Africa CDC doesn't update.\n# But this may be too likely - given PHEIC/PHECS status, Africa CDC will almost certainly update.\n# Let me reduce that probability.\n\n# Also, the upper tail seems reasonable given cases could spread to Goma (1M+ pop).\n\n# Let me reconsider the probability of Africa CDC not updating beyond May 18:\n# - PHEIC declared May 16\n# - PHECS declared May 18\n# - WHO weekly sitrep started (SitRep 01 on May 18)\n# - Africa CDC is actively coordinating response\n# - This is the biggest health emergency in Africa right now\n# \n# Probability Africa CDC doesn't publish ANY update beyond May 18: very low, ~2%\n# Probability they publish only one more update (with data ~May 22): ~5%\n# Probability they publish multiple updates through May 28+: ~93%\n\n# Let me also reconsider whether the 5% \"no update\" scenario is really 106\n# Actually, re-reading the resolution: \"If Africa CDC has not published any update \n# beyond the 15 May 2026 statement, the figure of 65 from that statement will be used\"\n# But Africa CDC DID publish on May 18 (PHECS declaration with ~106 deaths)\n# So even if they publish nothing more, the May 18 figure of 106 would be used\n\n# Let me re-run with adjusted scenario probabilities\n\nnp.random.seed(789)\nn_sims = 200000\n\nfinal_combined = np.zeros(n_sims)\n\nfor i in range(n_sims):\n    model = np.random.random()\n    \n    if model < 0.02:\n        # Scenario 0 (2%): No Africa CDC update beyond May 18\n        # Resolution = ~106 deaths (PHECS figure)\n        final_combined[i] = np.random.uniform(100, 110)\n        continue\n    \n    if model < 0.07:\n        # Scenario 0b (5%): Africa CDC updates once more with ~May 22-23 data\n        # Would report ~160-185 deaths\n        final_combined[i] = np.random.uniform(155, 195)\n        continue\n    \n    # Remaining 93%: Africa CDC updates through ~May 28-30\n    # Model the growth of reported deaths\n    \n    if model < 0.25:\n        # Scenario 1 (18%): Effective response, rapid deceleration\n        init_rate = np.random.normal(0.05, 0.012)\n        decel = np.random.uniform(0.06, 0.12)\n    elif model < 0.60:\n        # Scenario 2 (35%): Moderate growth, gradual deceleration\n        init_rate = np.random.normal(0.075, 0.018)\n        decel = np.random.uniform(0.04, 0.08)\n    elif model < 0.82:\n        # Scenario 3 (22%): Sustained growth, slow deceleration\n        init_rate = np.random.normal(0.10, 0.02)\n        decel = np.random.uniform(0.02, 0.05)\n    elif model < 0.93:\n        # Scenario 4 (11%): Rapid growth, spread to major cities\n        init_rate = np.random.normal(0.13, 0.025)\n        decel = np.random.uniform(0.01, 0.04)\n    else:\n        # Scenario 5 (7%): Very severe\n        init_rate = np.random.normal(0.16, 0.035)\n        decel = np.random.uniform(0.005, 0.03)\n    \n    # Simulate growth\n    # Use ~8-9 days effective (Africa CDC data cutoff 1-2 days before May 31)\n    effective_days = int(np.random.uniform(7.5, 10.5))\n    deaths = 148.0\n    for day in range(effective_days):\n        rate = max(0.003, init_rate * np.exp(-decel * day))\n        rate_actual = rate + np.random.normal(0, 0.018)\n        rate_actual = max(-0.01, rate_actual)\n        deaths *= (1 + rate_actual)\n    \n    # Retroactive community death discovery\n    retro = np.random.uniform(5, 40)\n    deaths += retro\n    \n    # Africa CDC uses \"more inclusive\" figure - slight upward bias\n    inclusive_factor = np.random.uniform(1.0, 1.08)\n    deaths *= inclusive_factor\n    \n    final_combined[i] = max(50, deaths)\n\n# Extract comprehensive percentiles\npercentiles_full = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 98, 99]\npct_values_full = np.percentile(final_combined, percentiles_full)\n\nprint(\"Final Refined Model Results (200,000 simulations):\")\nprint(f\"Mean: {np.mean(final_combined):.0f}\")\nprint(f\"Median: {np.median(final_combined):.0f}\")\nprint(f\"Std Dev: {np.std(final_combined):.0f}\")\nprint()\nprint(\"Percentile Distribution:\")\nfor p, v in zip(percentiles_full, pct_values_full):\n    print(f\"  P{p:2d}: {v:.0f}\")\n\nprint(f\"\\nKey thresholds:\")\nprint(f\"Probability > 500: {np.mean(final_combined > 500)*100:.1f}%\")\nprint(f\"Probability > 400: {np.mean(final_combined > 400)*100:.1f}%\")\nprint(f\"Probability > 300: {np.mean(final_combined > 300)*100:.1f}%\")\nprint(f\"Probability > 250: {np.mean(final_combined > 250)*100:.1f}%\")\nprint(f\"Probability > 200: {np.mean(final_combined > 200)*100:.1f}%\")\nprint(f\"Probability < 150: {np.mean(final_combined < 150)*100:.1f}%\")\nprint(f\"Probability < 120: {np.mean(final_combined < 120)*100:.1f}%\")\n\n# Dict format for output\npercentile_dict = {}\nfor p, v in zip(percentiles_full, pct_values_full):\n    percentile_dict[str(p)] = round(v)\nprint(f\"\\nPercentile dict: {percentile_dict}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Final Refined Model Results (200,000 simulations):\nMean: 312\nMedian: 287\nStd Dev: 112\n\nPercentile Distribution:\n  P 1: 105\n  P 2: 110\n  P 5: 179\n  P10: 209\n  P15:
223\n  P20: 233\n  P25: 243\n  P30: 251\n  P40: 268\n  P50: 287\n  P60: 309\n  P70: 336\n  P75: 354\n  P80: 376\n  P85: 405\n  P90: 449\n  P95: 527\n  P98: 631\n  P99: 709\n\nKey
thresholds:\nProbability > 500: 6.3%\nProbability > 400: 15.8%\nProbability > 300: 44.0%\nProbability > 250: 70.6%\nProbability > 200: 91.7%\nProbability < 150: 2.0%\nProbability < 120:
2.0%\n\nPercentile dict: {'1': 105, '2': 110, '5': 179, '10': 209, '15': 223, '20': 233, '25': 243, '30': 251, '40': 268, '50': 287, '60': 309, '70': 336, '75': 354, '80': 376, '85': 405, '90': 449,
'95': 527, '98': 631, '99': 709}\n", "stderr": "", "duration_ms": 2670}
```

## 💬 Response

Now let me run the reflection checkpoint.

## 💬 Response

The reflection shows a spread_ratio of 1.62, meaning my distribution is wider than the factor-implied range. This seems appropriate given the genuine epidemic uncertainty. The implied median from factors (266) is close to my tentative estimate (287). Let me now run the premortem.
