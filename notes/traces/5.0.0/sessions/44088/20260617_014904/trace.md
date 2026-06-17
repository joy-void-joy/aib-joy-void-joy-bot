# Reasoning Log: How many confirmed Ebola (Bundibugyo virus) deaths will the WHO report in the DRC as of its latest update near June 28, 2026?

*Generated: 2026-06-17T02:05:35.958890+00:00*


## 💭 Thinking

Let me analyze this forecasting question about Ebola (Bundibugyo virus) deaths in the DRC.

Key details:
- Question asks for cumulative confirmed deaths in DRC from the latest WHO DON article published on or before June 27, 2026
- Range: min 91, max 400 (open upper bound)
- As of May 27 DON: 17 confirmed deaths
- As of June 6 DON: 91 confirmed deaths
- CDC/ECDC reported 136-139 confirmed deaths as of June 11
- The outbreak was declared a PHEIC on May 17
- No vaccine or therapeutic for Bundibugyo virus
- The outbreak is showing intense community transmission with expanding geographic reach, which suggests the death toll could continue climbing significantly before June 27.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    44088
  ]
}
```

### 📋 Result

```
{"post_id": 44088, "title": "How many confirmed Ebola (Bundibugyo virus) deaths will the WHO report in the DRC as of its latest update near June 28, 2026?", "type": "numeric", "url":
"https://www.metaculus.com/questions/44088", "background_info": "In mid-May 2026, the Democratic Republic of the Congo (DRC) and Uganda declared an outbreak of Ebola disease caused by the Bundibugyo
virus (BDBV), one of the Ebola virus species. On 17 May 2026, the WHO Director-General declared the outbreak a Public Health Emergency of International Concern (PHEIC). The outbreak is centered in
eastern DRC across Ituri, North Kivu, and South Kivu Provinces, with a smaller, epidemiologically linked cluster in Uganda.\n\nUnlike Zaire ebolavirus outbreaks, there is no licensed vaccine or
specific therapeutic for Bundibugyo virus; the licensed Ervebo vaccine targets Zaire ebolavirus and WHO guidance states it should not be used programmatically for BDBV. The response therefore relies
on surveillance, case management, infection prevention and control, contact tracing, and safe burials, with only candidate countermeasures under evaluation.\n\nWHO publishes Disease Outbreak News
(DON) articles for this event that report cumulative confirmed cases and confirmed deaths, separated by country. Reported DRC confirmed deaths grew from 17 (as of 27 May, DON 29 May) to 91 (as of 6
June, DON 6 June), a case fatality rate of about 17.7% among confirmed cases. Other agencies using ministry-of-health data (e.g., CDC and ECDC) reported higher figures around 136\u2013139 confirmed
deaths in DRC as of 11 June 2026, reflecting later cut-off dates than the most recent WHO DON. The outbreak has been characterized by WHO as intense community transmission with increasing geographic
spread.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question asks for the
cumulative number of confirmed deaths in the Democratic Republic of the Congo (DRC only, excluding Uganda) attributed to the ongoing Ebola disease (Bundibugyo virus) outbreak, as reported in the most
recent World Health Organization Disease Outbreak News (DON) article on this outbreak published on or before June 27, 2026. The relevant DON articles are listed at
https://www.who.int/emergencies/disease-outbreak-news (filter by 2026 / Ebola). Report the figure as the integer count of confirmed deaths (e.g., a report of 158 confirmed deaths resolves as 158). The
\"confirmed deaths\" figure for DRC is the number of deaths among laboratory-confirmed cases stated for the DRC in that DON.", "fine_print": "\"Confirmed deaths\" refers to deaths among laboratory-
confirmed cases, not deaths among suspected or probable cases; if the DON reports a combined \"confirmed and probable\" death tally for DRC alongside a confirmed-only figure, use the confirmed-only
figure. Only the DRC figure counts; Uganda or any other country's deaths are excluded, and any \"combined\" cross-country total is not used. If multiple qualifying DON articles are published on or
before June 27, 2026, use the most recently published one. If, as of June 27, 2026, no DON article on this outbreak has been published later than the 6 June 2026 DON, the question resolves to the DRC
confirmed-death figure from that most recent available DON (91). If the WHO DON page is unavailable, the same figure may be taken from the corresponding WHO situation report or from [credible
sources](https://www.metaculus.com/faq/#definitions) reporting the WHO DON figure. If the outbreak is officially declared over and WHO reports a final DRC confirmed-death total, that final figure is
used.", "num_forecasters": 5, "community_prediction": null, "lower_bound": 91.0, "upper_bound": 400.0}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "WHO Disease Outbreak News Ebola Bundibugyo virus DRC June 2026 confirmed deaths latest update",
      "ttl": "6h"
    },
    {
      "query": "DRC Ebola Bundibugyo outbreak June 2026 death toll trajectory cases",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "WHO Disease Outbreak News Ebola Bundibugyo virus DRC June 2026 confirmed deaths latest update", "entry": {"slug": "who-disease-outbreak-news-ebola-bundibugyo-virus-d-46f85a72",
"query": "WHO Disease Outbreak News Ebola Bundibugyo virus DRC June 2026 confirmed deaths latest update", "answer": "\n\nI've exhausted all available web search and fetch tools. Let me provide my
findings based on what I can report.", "sources": [], "key_facts": ["All web search and fetch tools were unavailable; no live data could be retrieved for this query.", "Bundibugyo ebolavirus (BDBV)
was first identified in Uganda in 2007 (149 cases, 37 deaths, ~25% CFR).", "The only prior Bundibugyo virus outbreak in DRC occurred in 2012 in Isiro, Orientale Province (57 cases, 29 deaths, ~51%
CFR).", "Whether there is an active Bundibugyo virus outbreak in DRC in June 2026 could not be confirmed or denied due to tool unavailability.", "The DRC has historically been the most Ebola-affected
country, though most outbreaks have been caused by Zaire ebolavirus rather than Bundibugyo virus."], "data_points": [{"metric": "Bundibugyo virus outbreak cases (Uganda 2007)", "value": 149.0, "unit":
"confirmed and probable cases", "as_of": "2007-12-31", "source_url": "https://www.who.int/emergencies/disease-outbreak-news"}, {"metric": "Bundibugyo virus outbreak deaths (Uganda 2007)", "value":
37.0, "unit": "deaths", "as_of": "2007-12-31", "source_url": "https://www.who.int/emergencies/disease-outbreak-news"}, {"metric": "Bundibugyo virus outbreak cases (DRC 2012)", "value": 57.0, "unit":
"confirmed and probable cases", "as_of": "2012-12-31", "source_url": "https://www.who.int/emergencies/disease-outbreak-news"}, {"metric": "Bundibugyo virus outbreak deaths (DRC 2012)", "value": 29.0,
"unit": "deaths", "as_of": "2012-12-31", "source_url": "https://www.who.int/emergencies/disease-outbreak-news"}], "created_at": "2026-06-17T01:52:19.113823Z", "updated_at":
"2026-06-17T01:52:19.113823Z", "stale_after": "2026-06-17T07:52:19.113823Z", "state": "fresh", "revision_history": [], "session_id": "eaff6cfa-cbc8-42b0-938e-41702d02f0c8", "follow_up_count": 0},
"is_follow_up": false}, {"query": "DRC Ebola Bundibugyo outbreak June 2026 death toll trajectory cases", "entry": {"slug": "drc-ebola-bundibugyo-outbreak-june-2026-death-toll-6b6a656d", "query": "DRC
Ebola Bundibugyo outbreak June 2026 death toll trajectory cases", "answer": "I now have a comprehensive picture. Let me compile the final synthesis.\n\n---\n\n# DRC Ebola Bundibugyo Outbreak \u2013
June 2026: Research Findings\n\n## Overview\n\nThe Democratic Republic of the Congo is currently experiencing its **17th Ebola outbreak**, caused by the **Bundibugyo ebolavirus (BDBV)** \u2014 a
strain for which **no approved vaccine or treatment** currently exists. The outbreak was officially declared on **15 May 2026** and was designated a **Public Health Emergency of International Concern
(PHEIC)** by WHO on **16\u201317 May 2026**, just two days after the declaration. The outbreak has also spread to **Uganda** via cross-border transmission.\n\n## Case and Death Trajectory
(Chronological)\n\nThe outbreak has grown extremely rapidly. Key data points from official sources:\n\n| Date | Confirmed Cases (DRC) | Confirmed Deaths (DRC) | CFR (DRC) | Uganda Cases | Source
|\n|------|----------------------|----------------------|-----------|-------------|--------|\n| 5 May 2026 | Initial alert (unknown illness, 4 HCW deaths in Mongbwalu) | \u2014 | \u2014 | \u2014 | WHO
Sitrep 01 |\n| 15 May 2026 | Outbreak declared (lab confirmation of BDBV) | \u2014 | \u2014 | 2 imported | WHO Sitrep 01 |\n| 18 May 2026 | (WHO Sitrep 01 published \u2013 exact case count not in
abstract) | \u2014 | \u2014 | \u2014 | WHO Sitrep 01 |\n| 19 May 2026 | **33** | \u2014 | \u2014 | \u2014 | ReliefWeb community engagement report |\n| 30 May 2026 | **282** | \u2014 | \u2014 | 5
(incl. 1 death) | ReliefWeb report; WHO risk assessment |\n| 31 May 2026 | **291** | **43** | ~14.8% | \u2014 | Project HOPE Sitrep #3 |\n| 2 June 2026 | **321** | **48** | ~14.9% | \u2014 | DRC
Ministry of Health via OCHA |\n| 6 June 2026 | **515** | \u2014 | \u2014 | \u2014 | Mongbwalu epi report (baseline) |\n| 10 June 2026 | **676** | **136** | **20.1%** | 19 (incl. 2 deaths) | WHO DON607
(13 June) |\n| 13 June 2026 | **782** | **181** | **23.1%** | \u2014 | Mongbwalu epi trends report (16 June); Save the Children (15 June) |\n\n### Growth Rate\n- **May 19 \u2192 May 30**: 33 \u2192
282 cases = **~8.5-fold increase in 11 days**\n- **June 6 \u2192 June 13**: 515 \u2192 782 cases = **+267 cases (+51.8%) in one week**\n- **Overall first month (May 15 \u2192 June 15)**: 0 \u2192 782
confirmed cases, 181 confirmed deaths\n\n## Geographic Spread\n\n- **Epicenter**: Ituri Province (~91.6% of confirmed cases as of 13 June)\n  - Main hotspots: **Bunia** (185 cases), **Rwampara** (137
cases), **Mongbwalu** (132 cases), **Nyankunde** (33 cases) \u2014 as of 10 June\n- **Total health zones affected**: **31** across three provinces (Ituri: 19/36 HZ; North Kivu: 9/35 HZ; South Kivu:
1/34 HZ) \u2014 as of 13 June\n- **Uganda**: 19 confirmed cases (14 imported, 5 secondary), 2 deaths \u2014 from Kampala and Wakiso districts. No new cases for 6 days as of 11 June. No documented
community transmission.\n- **Regional preparedness**: Burundi, Rwanda, South Sudan (Priority 1); Angola, CAR, Ethiopia, Kenya, Congo, Tanzania, Zambia (Priority 2)\n\n## Key Contextual Factors\n\n-
**No approved vaccine or treatment** for Bundibugyo ebolavirus exists. Clinical trials are being organized for **MBP134** and **REGN3479** (treatment) and **obeldesivir** (post-exposure
prophylaxis).\n- **Third-largest Ebola outbreak ever recorded in DRC** (Save the Children, 15 June).\n- **IASC System-Wide Scale-Up** activated on 7 June for initial 3-month period.\n- **159 health
zones** categorized as affected or at risk (WHO, 8 June).\n- **5,768 contacts** under follow-up as of 10 June (4,703 in Ituri, 841 in North Kivu, 224 in South Kivu). Follow-up rate: ~72%.\n- **16
healthcare worker infections** confirmed as of 10 June.\n- **Children disproportionately affected**: 52 children infected (including 16 toddlers/infants), 19 child deaths. Children under 14 have
**more than twice** the case fatality rate of patients aged 15\u201344.\n- **Water/sanitation crisis**: Only 20% of people in Mongbwalu have access to clean water; only 1 in 5 health facilities in
Ituri has adequate clean water access (Oxfam).\n- **Outbreak likely underestimated** per Oxfam; MSF warns most patients arrive at treatment centers at a late stage and were never identified as
contacts.\n- **Complex conflict environment**: Armed conflict in Ituri, displaced populations, and security incidents at health facilities hinder response.\n\n## Response Status\n\n- WHO risk
assessment: **Very high** for DRC, **high** for Uganda and bordering countries, **low** for rest of Africa and globally.\n- Response described as \"outpacing the response effort\" (MSF, 15 June). Gaps
in surveillance, diagnosis, contact tracing, and community engagement persist.\n- Africa CDC and WHO launched a joint continental response plan on 5 June.\n- Logistics Cluster established transport
corridors from Entebbe to Bunia.\n\n---", "sources": [{"url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607", "title": "Disease Outbreak News: Ebola disease caused by
Bundibugyo virus, DRC & Uganda (13 June 2026)", "domain": "who.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "As of 10 June, 676 confirmed cases including 136 deaths (CFR 20.1%) reported
from DRC. Uganda: 19 confirmed cases including 2 deaths."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/unicef-ebola-virus-disease-outbreak-flash-update-no-3-democratic-republic-
congo-uganda-12-june-2026", "title": "UNICEF Ebola Virus Disease Outbreak Flash Update No. 3 (DRC & Uganda), 12 June 2026", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet":
"As of 11 June 2026, 676 confirmed cases and 136 confirmed deaths in DRC, 19 confirmed cases and 2 deaths in Uganda. IASC Scale-Up activated 7 June."}, {"url":
"https://reliefweb.int/report/democratic-republic-congo/young-children-paying-highest-price-one-month-drc-declared-new-ebola-crisis-save-children", "title": "Young children paying the highest price
one month since DRC declared new Ebola crisis \u2013 Save the Children", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "782 confirmed cases and 181 confirmed deaths as
of 15 June. 52 children infected, 19 child deaths. Third-largest Ebola outbreak ever in DRC."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-mongbwalu-and-rwampara-
epidemiological-trends-community-perceptions-and-challenges-community-engagement-response", "title": "Ebola in Mongbwalu and Rwampara: Epidemiological Trends, Community Perceptions and Challenges",
"domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "As of 13 June 2026, 782 confirmed cases and 181 deaths. 51.8% increase from 515 cases on 6 June. 31 health zones affected.
Ituri: 91.6% of cases."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/drc-one-month-msf-warns-dangerous-gaps-persist-ebola-disease-response", "title": "DRC: One month on, MSF warns
dangerous gaps persist in Ebola disease response", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "One month after declaration, outbreak is outpacing the response. Major
gaps in surveillance, diagnosis, contact tracing and community engagement."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/scale-ebola-virus-outbreak-likely-under-estimated-oxfam",
"title": "Scale of Ebola virus outbreak likely under-estimated \u2013 Oxfam", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Only 20% of people in Mongbwalu have clean
water access. Only 1 in 5 health facilities in Ituri has adequate clean water."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-core-response-characterized-security-
instability-and-community-opposition-june-2026", "title": "Ebola outbreak: At the core of a response characterized by security instability and community opposition (June 2026)", "domain":
"reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Cases escalated from 33 on May 19 to 282 on May 30, an eightfold increase in under two weeks."}, {"url":
"https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-3-june-1-2026", "title": "Ebola Outbreak in DRC and Uganda: Situation Report #3 (June 1, 2026)",
"domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "As of May 31, 291 confirmed cases and 43 confirmed deaths in DRC."}, {"url": "https://reliefweb.int/report/democratic-
republic-congo/democratic-republic-congo-ebola-outbreak-overview-context-vulnerabilities-and-response-4-june-2026", "title": "DRC Ebola Outbreak Overview: Context, Vulnerabilities, and Response (4
June 2026)", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "As of 2 June, 321 confirmed cases including 48 deaths and 116 suspected cases under investigation."}, {"url":
"https://reliefweb.int/report/democratic-republic-congo/ebola-bundibugyo-virus-disease-outbreak-democratic-republic-congo-uganda-weekly-external-situation-report-01-data-18-may-2026", "title": "WHO
Weekly External Situation Report 01 (Data as of 18 May 2026)", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Initial alert 5 May regarding unknown illness with 4 HCW
deaths. Lab confirmed BDBV 15 May. PHEIC declared 16 May."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-further-strains-drcs-underfunded-health-system-leaving-
health-workers-limited-critical-supplies", "title": "Ebola outbreak further strains DRC's underfunded health system (4 June 2026)", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z",
"snippet": "Third-largest outbreak on record, driven by Bundibugyo strain with no approved vaccine or treatment."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/ebola-virus-disease-
unicef-emergency-response-and-preparedness", "title": "Ebola Virus Disease: UNICEF Emergency Response and Preparedness", "domain": "reliefweb.int", "accessed_at": "2026-06-17T00:00:00Z", "snippet":
"WHO declared PHEIC on 17 May 2026. Situation as of 21 May 2026."}, {"url": "https://reliefweb.int/report/democratic-republic-congo/iom-multi-country-bundibugyo-ebola-virus-disease-outbreak-situation-
report-no-4-3-9-june-2026", "title": "IOM: Multi-Country Bundibugyo Ebola Virus Disease Outbreak - Situation Report No. 4 (3-9 June 2026)", "domain": "reliefweb.int", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "IOM supporting preparedness and response in Priority 1a (DRC, Uganda) and Priority 1b countries (Burundi, Rwanda, South Sudan)."}], "key_facts": ["DRC declared its
17th Ebola outbreak on 15 May 2026, caused by Bundibugyo ebolavirus (BDBV) \u2014 a strain with no approved vaccine or treatment", "WHO declared a Public Health Emergency of International Concern
(PHEIC) on 16-17 May 2026, just 2 days after outbreak declaration", "As of 13 June 2026: 782 confirmed cases and 181 confirmed deaths in DRC (CFR ~23.1%)", "As of 11 June 2026: 19 confirmed cases and
2 deaths in Uganda (no new cases for 6 days; no community transmission)", "Combined total across both countries: 801 confirmed cases and 183 deaths (as of 10-13 June 2026)", "Outbreak trajectory: 33
cases (May 19) \u2192 282 (May 30) \u2192 321 (June 2) \u2192 515 (June 6) \u2192 676 (June 10) \u2192 782 (June 13)", "Cases increased 51.8% in one week (June 6-13), from 515 to 782", "Third-largest
Ebola outbreak ever recorded in DRC (Save the Children)", "Epicenter is Ituri Province accounting for 91.6% of confirmed cases; 31 health zones affected across Ituri, North Kivu, and South Kivu", "Top
health zones by cases (as of June 10): Bunia (185), Rwampara (137), Mongbwalu (132), Nyankunde (33)", "16 healthcare worker infections confirmed as of 10 June 2026", "5,768 contacts under follow-up
with ~72% follow-up rate as of 10 June", "52 children infected including 16 toddlers/infants; 19 child deaths; children under 14 have more than twice the CFR of patients aged 15-44", "Only 20% of
people in Mongbwalu (population ~140,000) have access to clean water (Oxfam)", "IASC System-Wide Scale-Up activated on 7 June 2026 for initial 3-month period", "Clinical trials being organized for
MBP134 and REGN3479 (treatment) and obeldesivir (post-exposure prophylaxis)", "MSF warns outbreak is 'outpacing the response effort'; Oxfam says true scale is likely underestimated", "WHO risk
assessment: Very High for DRC, High for Uganda and bordering countries, Low globally", "Initial alert was 5 May 2026 regarding unknown illness with high mortality including 4 HCW deaths in Mongbwalu",
"159 health zones categorized as affected or at risk as of WHO analysis dated 8 June"], "data_points": [{"metric": "Confirmed Ebola cases (DRC)", "value": 33.0, "unit": "cases", "as_of": "2026-05-19",
"source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-core-response-characterized-security-instability-and-community-opposition-june-2026"}, {"metric": "Confirmed Ebola
cases (DRC)", "value": 282.0, "unit": "cases", "as_of": "2026-05-30", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-core-response-characterized-security-
instability-and-community-opposition-june-2026"}, {"metric": "Confirmed Ebola cases (DRC)", "value": 291.0, "unit": "cases", "as_of": "2026-05-31", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-3-june-1-2026"}, {"metric": "Confirmed Ebola deaths (DRC)", "value": 43.0, "unit": "deaths",
"as_of": "2026-05-31", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-outbreak-drc-and-uganda-situation-report-3-june-1-2026"}, {"metric": "Confirmed Ebola cases (DRC)",
"value": 321.0, "unit": "cases", "as_of": "2026-06-02", "source_url": "https://reliefweb.int/report/democratic-republic-congo/democratic-republic-congo-ebola-outbreak-overview-context-vulnerabilities-
and-response-4-june-2026"}, {"metric": "Confirmed Ebola deaths (DRC)", "value": 48.0, "unit": "deaths", "as_of": "2026-06-02", "source_url": "https://reliefweb.int/report/democratic-republic-
congo/democratic-republic-congo-ebola-outbreak-overview-context-vulnerabilities-and-response-4-june-2026"}, {"metric": "Confirmed Ebola cases (DRC)", "value": 515.0, "unit": "cases", "as_of":
"2026-06-06", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-mongbwalu-and-rwampara-epidemiological-trends-community-perceptions-and-challenges-community-engagement-
response"}, {"metric": "Confirmed Ebola cases (DRC)", "value": 676.0, "unit": "cases", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"},
{"metric": "Confirmed Ebola deaths (DRC)", "value": 136.0, "unit": "deaths", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric":
"Case fatality rate (DRC)", "value": 20.1, "unit": "percent", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Confirmed
Ebola cases (Uganda)", "value": 19.0, "unit": "cases", "as_of": "2026-06-11", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Confirmed Ebola
deaths (Uganda)", "value": 2.0, "unit": "deaths", "as_of": "2026-06-11", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Confirmed Ebola cases
(DRC)", "value": 782.0, "unit": "cases", "as_of": "2026-06-13", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-mongbwalu-and-rwampara-epidemiological-trends-community-
perceptions-and-challenges-community-engagement-response"}, {"metric": "Confirmed Ebola deaths (DRC)", "value": 181.0, "unit": "deaths", "as_of": "2026-06-13", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/young-children-paying-highest-price-one-month-drc-declared-new-ebola-crisis-save-children"}, {"metric": "Weekly case increase (DRC, June 6-13)",
"value": 51.8, "unit": "percent", "as_of": "2026-06-13", "source_url": "https://reliefweb.int/report/democratic-republic-congo/ebola-mongbwalu-and-rwampara-epidemiological-trends-community-
perceptions-and-challenges-community-engagement-response"}, {"metric": "Health zones affected", "value": 31.0, "unit": "health zones", "as_of": "2026-06-13", "source_url":
"https://reliefweb.int/report/democratic-republic-congo/ebola-mongbwalu-and-rwampara-epidemiological-trends-community-perceptions-and-challenges-community-engagement-response"}, {"metric": "Contacts
under follow-up", "value": 5768.0, "unit": "contacts", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Contact follow-up
rate (Ituri)", "value": 71.4, "unit": "percent", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Healthcare worker
infections (DRC)", "value": 16.0, "unit": "cases", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Cases in Bunia health
zone", "value": 185.0, "unit": "cases", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Cases in Rwampara health zone",
"value": 137.0, "unit": "cases", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Cases in Mongbwalu health zone", "value":
132.0, "unit": "cases", "as_of": "2026-06-10", "source_url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Children infected", "value": 52.0, "unit":
"children", "as_of": "2026-06-15", "source_url": "https://reliefweb.int/report/democratic-republic-congo/young-children-paying-highest-price-one-month-drc-declared-new-ebola-crisis-save-children"},
{"metric": "Child deaths confirmed", "value": 19.0, "unit": "deaths", "as_of": "2026-06-15", "source_url": "https://reliefweb.int/report/democratic-republic-congo/young-children-paying-highest-price-
one-month-drc-declared-new-ebola-crisis-save-children"}, {"metric": "Health zones at risk or affected", "value": 159.0, "unit": "health zones", "as_of": "2026-06-08", "source_url":
"https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "DRC recoveries", "value": 32.0, "unit": "patients", "as_of": "2026-06-10", "source_url":
"https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607"}, {"metric": "Clean water access in Mongbwalu", "value": 20.0, "unit": "percent of population", "as_of": "2026-06-16",
"source_url": "https://reliefweb.int/report/democratic-republic-congo/scale-ebola-virus-outbreak-likely-under-estimated-oxfam"}], "created_at": "2026-06-17T01:54:06.500062Z", "updated_at":
"2026-06-17T01:54:06.500062Z", "stale_after": "2026-06-17T07:54:06.500062Z", "state": "fresh", "revision_history": [], "session_id": "59e72508-990e-44f6-ba36-db9d821c9c63", "follow_up_count": 0},
"is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

Excellent research results. I now have detailed data on the outbreak trajectory. Let me check for the latest WHO DON and search for any more recent data, then run a simulation.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "WHO Disease Outbreak News Ebola Bundibugyo DRC June 2026 DON607"
}
```

### 📋 Result

```
{"query": "WHO Disease Outbreak News Ebola Bundibugyo DRC June 2026 DON607", "results": [{"title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the Congo & Uganda", "url":
"https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607", "snippet": "Situation at a glance\nDescription of the situation\nSince the last [Disease Outbreak
News](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON606) was published on 8 June 2026, the number of confirmed cases and deaths have increased rapidly in the Democratic Republic
of the Congo. In total, 695 confirmed cases; 676 from the Democratic Republic of the Congo and 19 from Uganda; and 138 deaths including two from Uganda, have been reported from both countries, while
at least 37 people", "api_data": null, "hint": null}, {"title": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda", "url": "https://www.ecdc.europa.eu/en/ebola-outbreak-
democratic-republic-congo-and-uganda", "snippet": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more information becomes available. It was last
updated 16 June at 15:10.\nAs of 16 June 2026, the Ebola disease outbreak caused by Bundibugyo virus is affecting the Democratic Republic of the Congo (DRC) and Uganda.\nOn 15 June, the [DRC Ministry
of Health reported](https://insp.cd/sitrep-n31-mvb_14-06-2026/) a total of 808 confirmed cases, including 192 confirmed related deaths, and 363 individuals ", "api_data": null, "hint": null},
{"title": "Ebola Outbreak Reaches 598 Confirmed Cases and 115 Deaths in DRC \u2014 U.S. Pledges $220 Million as WHO Emergency Escalates", "url": "https://www.medicaldaily.com/ebola-bundibugyo-
outbreak-2026-drc-uganda-who-emergency-us-response-475582", "snippet": "Ebola Outbreak Reaches 598 Confirmed Cases and 115 Deaths in DRC \u2014 U.S. Pledges $220 Million as WHO Emergency
Escalates\nThe deadliest active infectious disease outbreak in the world has rapidly escalated over the past three weeks. The 2026 Bundibugyo virus [Ebola outbreak](https://www.medicaldaily.com/ebola-
outbreak-dr-congo-spirals-amid-conflict-who-warns-catastrophic-collision-475457) in the Democratic Republic of the Congo (DRC) and Uganda \u2014 declared a Public Health Emergency of International",
"api_data": null, "hint": null}, {"title": "Ebola Disease Outbreak in the Democratic Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html",
"snippet": "At a glance\n- Distributed via the CDC Health Alert Network\n- May 19, 2026\n- CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-
Health-Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and
travelers about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and Uganda caused by the Bundib", "api_data": null, "hint": null}, {"title": "Ebola virus outbreak 2026 -
Public Health - European Commission", "url": "https://health.ec.europa.eu/health-security-and-infectious-diseases/crisis-management/ebola-virus-outbreak-2026_en", "snippet": "On 17 May 2026, the World
Health Organization (WHO) determined that the Ebola virus disease outbreak caused by Bundibugyo virus in the Democratic Republic of the Congo (DRC) and Uganda constitutes [a public health emergency of
international concern (PHEIC)](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602). This means that the outbreak poses a serious, unusual, cross-border risk that requires
coordinated international action.\nThe European Centre for Disease Prevention and C", "api_data": null, "hint": null}, {"title": "Ebola outbreak in Africa - preparedness in the WHO European Region",
"url": "https://www.who.int/europe/emergencies/situations/ebola-outbreak-in-africa-preparedness-in-the-who-european-region", "snippet": "Epidemic of Ebola disease caused by Bundibugyo virus in the
Democratic Republic of the Congo (DRC) and Uganda 2026: preparedness in the WHO European Region\nOverview\nOn 15 May 2026, the Ministry of Public Health, Hygiene and Social Welfare of the Democratic
Republic of the Congo (DRC) and the Ministry of Health of Uganda declared an outbreak of Ebola disease following the confirmation of Bundibugyo virus disease (BVD) in both countries. On 17 May 2026,
WHO\u2019s Director-General determined that Ebola", "api_data": null, "hint": null}, {"title": "2026 Central Africa Ebola epidemic", "url":
"https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic", "snippet": "In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It
is the 17th Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of
Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo provin",
"api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Ebola epidemic\", \"url\": \"https://en.wikipedia.org/wiki/2026_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola
was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early
infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A
case in South Kivu was reported to have been imported from Tshopo province on 21 May.\\nThe epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola
treatments were created for a different strain, the Zaire ebolavirus. The outbreak was declared a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16
May 2026.\\nThere have been 192 confirmed deaths in D.R. Congo, and two deaths in Uganda, as of 14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection,
treatment and prevention of the disease; it is considered likely that the true scale of the outbreak could considerably exceed the confirmed numbers.\", \"mode\": \"full\"}"}]}, "hint": null},
{"title": "CDC Mobilizes International Response Following Ebola Disease Outbreak in DRC and Uganda | CDC Newsroom", "url": "https://www.cdc.gov/media/releases/2026/cdc-mobilizes-international-ebola-
response.html", "snippet": "Statement\nThe Centers for Disease Control and Prevention (CDC) has mobilized response activities following confirmation of an Ebola outbreak in Ituri Province, Democratic
Republic of the Congo (DRC) and cases in Uganda. Through existing relationships with the DRC and Uganda Ministries of Health, CDC was notified of the ongoing outbreak as soon as cases were confirmed
and have been actively working to support needs. Last night, the WHO followed this notification with a declaration of a public hea", "api_data": null, "hint": null}, {"title": "Ebola outbreak - DRC
2026", "url": "https://www.who.int/emergencies/situations/ebola-outbreak---drc-2026", "snippet": "![EbolaDRC2026_Supplies2 Emergency supplies being loaded off
plane](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2026---ebola-outbreak---
drc/eboladrc2026_supplies2.jpg?sfvrsn=da475c39_2)\n![](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2026---ebola-outbreak---
drc/ebolaresponse_drc_2026.tmb-1920v.jpg?sfvrsn=15234691_6)\nEbola\nThe Democratic Republic of the Congo, 2026\nOverview\nAn Ebola outbreak was confirmed in the Democratic Republic of th", "api_data":
null, "hint": null}]}
```

```json
{
  "query": "DRC Ebola confirmed deaths June 16 17 2026 latest update"
}
```

### 📋 Result

```
{"query": "DRC Ebola confirmed deaths June 16 17 2026 latest update", "results": [{"title": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda", "url":
"https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda", "snippet": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more
information becomes available. It was last updated 16 June at 15:10.\nAs of 16 June 2026, the Ebola disease outbreak caused by Bundibugyo virus is affecting the Democratic Republic of the Congo (DRC)
and Uganda.\nOn 15 June, the [DRC Ministry of Health reported](https://insp.cd/sitrep-n31-mvb_14-06-2026/) a total of 808 confirmed cases, including 192 confirmed related deaths, and 363 individuals
", "api_data": null, "hint": null}, {"title": "Ebola Outbreak 2026: Latest Updates and Response \u2014 Ebola Map", "url": "https://ebolamap.org/blog/ebola-outbreak-2026-latest-updates/", "snippet":
"[Back to Blog](https://ebolamap.org/blog)\nEbola Outbreak 2026: Latest Updates and Response\nLive updates on the 2026 Ebola outbreak in the Democratic Republic of Congo and Uganda. Case counts, WHO
PHEIC declaration, geographic spread, and international response.\nCurrent Situation (11 June 2026)\nAn Ebola outbreak caused by Bundibugyo ebolavirus was declared in the Democratic Republic of Congo
on 15 May 2026. As of 11 June: DRC has 608 confirmed cases and 102 confirmed deaths (revised from earlier ", "api_data": null, "hint": null}, {"title": "Ebola Disease Outbreak in the Democratic
Republic of the Congo and Uganda | HAN | CDC", "url": "https://www.cdc.gov/han/php/notices/han00530.html", "snippet": "At a glance\n- Distributed via the CDC Health Alert Network\n- May 19, 2026\n-
CDCHAN-00530\n![Image with text 'this is an official CDC health advisory.](/han/media/images/2025/03/HAN-Health-Advisory.png)\nSummary\nThe Centers for Disease Control and Prevention (CDC) is issuing
this Health Alert Network (HAN) Health Advisory to alert clinicians, public health practitioners, and travelers about a new outbreak of Ebola disease in the Democratic Republic of the Congo (DRC) and
Uganda caused by the Bundib", "api_data": null, "hint": null}, {"title": "2026 Central Africa Ebola epidemic", "url": "https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic", "snippet": "In
May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of
the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's
capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo provin", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Ebola epidemic\", \"url\":
\"https://en.wikipedia.org/wiki/2026_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th
Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with
imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo province on 21 May.\\nThe
epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola treatments were created for a different strain, the Zaire ebolavirus. The outbreak was declared
a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16 May 2026.\\nThere have been 192 confirmed deaths in D.R. Congo, and two deaths in Uganda, as of
14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection, treatment and prevention of the disease; it is considered likely that the true scale of the
outbreak could considerably exceed the confirmed numbers.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "2026 Ebola epidemic - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Ebola_epidemic", "snippet": "In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th
Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with
imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo provin", "api_data": {"content":
[{"type": "text", "text": "{\"title\": \"2026 Ebola epidemic\", \"url\": \"https://en.wikipedia.org/wiki/2026_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola was reported in the
Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been
theorized to have occurred in February 2026 in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was
reported to have been imported from Tshopo province on 21 May.\\nThe epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola treatments were created
for a different strain, the Zaire ebolavirus. The outbreak was declared a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16 May 2026.\\nThere have
been 192 confirmed deaths in D.R. Congo, and two deaths in Uganda, as of 14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection, treatment and prevention
of the disease; it is considered likely that the true scale of the outbreak could considerably exceed the confirmed numbers.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "History of Ebola
Outbreaks | Ebola | CDC", "url": "https://www.cdc.gov/ebola/outbreaks/index.html", "snippet": "At a glance\n- Ebola disease was first identified in 1976 after an outbreak in what is now the Democratic
Republic of Congo.\n- Since then, these viruses have emerged periodically from the unknown animal that carries them and infected people in several African countries.\n- Expand the sections below to
read a brief summary of all known cases and outbreaks, organized by year.\nOutbreaks by species and size, since 1976\n![A map of Africa showing all known Ebola
outbreaks](/ebola/media/images/2026/01/we", "api_data": null, "hint": null}, {"title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the Congo & Uganda", "url":
"https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON606", "snippet": "Situation at a glance\nDescription of the situation\nSince the last [Disease Outbreak
News](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON605) was published on 29 May 2026, the number of confirmed cases and deaths have increased rapidly in the Democratic Republic
of the Congo and Uganda. In total, 534 confirmed cases including 93 deaths (case fatality rate [CFR] 17.4%) have been reported from both countries, while at least 17 people have recovered from the
disease.\nFigure 1. D", "api_data": null, "hint": null}, {"title": "Ebola disease outbreak 2026: How MSF is responding", "url": "https://www.doctorswithoutborders.org/latest/ebola-disease-
outbreak-2026-how-msf-responding", "snippet": "Developing story\nEbola disease outbreak 2026: How MSF is responding\nHundreds of MSF staff are responding in DR Congo and Uganda, treating patients,
setting up Ebola treatment centers and isolation units, and delivering supplies.\nDeveloping story\nHundreds of MSF staff are responding in DR Congo and Uganda, treating patients, setting up Ebola
treatment centers and isolation units, and delivering supplies.\nJune 15, 2026 \u2014 One month after the Ebola disease outbreak was declared in Democratic Republi", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607",
  "prompt": "What are the exact numbers for DRC confirmed cases and confirmed deaths? What is the data cutoff date? When was this DON published?"
}
```

### 📋 Result

```
{"url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607", "content": "Based on the content:\n\n**DRC Confirmed Cases and Deaths:**\n- 676 confirmed cases\n- 136 confirmed
deaths\n- Case Fatality Rate (CFR): 20.1%\n\n**Data Cutoff Date:** 10 June 2026\n\n**DON Publication Date:** 13 June 2026\n\n**Relevant links:**\n\n- [Disease Outbreak News | Ebola disease caused by
Bundibugyo virus, Democratic Republic of the Congo and Uganda 8 June 2026](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON606) (Previous update)\n- [Weekly External Situation
Report 04, Data as of 7 June 2026](https://iris.who.int/server/api/core/bitstreams/a296c3f1-0338-4a05-9ee8-6cf93ad7c292/content)\n- [Epidemiological update on BVD outbreak (Daily
updates)](https://www.who.int/emergencies/alert-and-response)\n- [Daily situation report, Ministry of Health, Democratic Republic of the Congo](https://insp.cd/category/sitrep/)\n- [WHO Rapid Risk
Assessment v3](https://www.who.int/publications/m/item/who-rapid-risk-assessment-ebola-disease-caused-by-bundibugyo-virus--democratic-republic-of-the-congo--uganda-and-countries-with-land-borders-
adjoining-countries-with-documented-bdbv-detection-v3)", "title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the Congo & Uganda"}
```

```json
{
  "url": "https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda",
  "prompt": "What are the latest DRC confirmed cases and confirmed deaths numbers? What is the most recent data date?"
}
```

### 📋 Result

```
{"url": "https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda", "content": "Based on the content:\n\n**Latest DRC numbers (as of 14 June 2026):**\n- **808 confirmed
cases**\n- **192 confirmed deaths**\n\n**Most recent data date:** 14 June 2026\n\n(Note: The page itself was last updated on 16 June 2026 at 15:10, but the DRC data reported is as of 14 June
2026)\n\n**Relevant links:**\n- [DRC Ministry of Health SITREP N31](https://insp.cd/sitrep-n31-mvb_14-06-2026/) - Official situation report with the latest case numbers\n- [ECDC weekly Communicable
disease threats report](https://www.ecdc.europa.eu/en/publications-and-data/monitoring/weekly-threats-reports) - Weekly updates on the outbreak\n- [Uganda Ministry of Health EVD Daily
Updates](https://evd-daily.health.go.ug/) - Uganda case tracking\n- [WHO Disease Outbreak News](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON605) - Additional outbreak
information", "title": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda"}
```

```json
{
  "url": "https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic",
  "prompt": "What are the latest case and death numbers for DRC? Is there a timeline table showing the progression of cases and deaths? Extract all data points with dates."
}
```

### 📋 Result

```
{"title": "2026 Ebola epidemic", "url": "https://en.wikipedia.org/wiki/2026_Ebola_epidemic", "extract": "In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic
of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026
in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo
province on 21 May.\nThe epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola treatments were created for a different strain, the Zaire ebolavirus.
The outbreak was declared a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16 May 2026.\nThere have been 192 confirmed deaths in D.R. Congo, and two
deaths in Uganda, as of 14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection, treatment and prevention of the disease; it is considered likely that the
true scale of the outbreak could considerably exceed the confirmed numbers.", "mode": "full"}
```

## 💬 Response

Now let me compile the death trajectory data and run a simulation to project forward.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\n# Confirmed deaths trajectory for DRC\n# Format: (date_string, confirmed_deaths)\ndeath_data = [\n    (\"2026-05-27\", 17),    # WHO DON 29 May (data as of 27 May)\n    (\"2026-05-31\", 43),    # Project HOPE Sitrep #3\n    (\"2026-06-02\", 48),    # DRC MoH via OCHA\n    (\"2026-06-06\", 91),    # WHO DON 6 June (data as of 6 June)\n    (\"2026-06-10\", 136),   # WHO DON607 (data as of 10 June)\n    (\"2026-06-13\", 181),   # Save the Children / Mongbwalu report\n    (\"2026-06-14\", 192),   # ECDC / Wikipedia (DRC MoH sitrep n31)\n]\n\n# Convert to numerical days from start\nstart_date = datetime(2026, 5, 27)\ndays = [(datetime.strptime(d, \"%Y-%m-%d\") - start_date).days for d, _ in death_data]\ndeaths = [v for _, v in death_data]\n\nprint(\"Death trajectory:\")\nfor d, v, date_str in zip(days, deaths, [x[0] for x in death_data]):\n    print(f\"  Day {d:3d} ({date_str}): {v} confirmed deaths\")\n\n# Calculate daily growth rates between consecutive points\nprint(\"\\nGrowth rates between consecutive data points:\")\nfor i in range(1, len(days)):\n    delta_days = days[i] - days[i-1]\n    ratio = deaths[i] / deaths[i-1]\n    daily_rate = ratio ** (1/delta_days) - 1\n    print(f\"  {death_data[i-1][0]} -> {death_data[i][0]}: {deaths[i-1]} -> {deaths[i]} ({delta_days} days), daily growth rate = {daily_rate:.3%}\")\n\n# Calculate average daily new deaths in recent period\nprint(\"\\nAverage daily new deaths:\")\nfor i in range(1, len(days)):\n    delta_days = days[i] - days[i-1]\n    new_deaths = deaths[i] - deaths[i-1]\n    avg_daily = new_deaths / delta_days\n    print(f\"  {death_data[i-1][0]} -> {death_data[i][0]}: {new_deaths} new / {delta_days} days = {avg_daily:.1f} per day\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Death trajectory:\n  Day   0 (2026-05-27): 17 confirmed deaths\n  Day   4 (2026-05-31): 43 confirmed deaths\n  Day   6 (2026-06-02): 48 confirmed deaths\n  Day  10
(2026-06-06): 91 confirmed deaths\n  Day  14 (2026-06-10): 136 confirmed deaths\n  Day  17 (2026-06-13): 181 confirmed deaths\n  Day  18 (2026-06-14): 192 confirmed deaths\n\nGrowth rates between
consecutive data points:\n  2026-05-27 -> 2026-05-31: 17 -> 43 (4 days), daily growth rate = 26.112%\n  2026-05-31 -> 2026-06-02: 43 -> 48 (2 days), daily growth rate = 5.654%\n  2026-06-02 ->
2026-06-06: 48 -> 91 (4 days), daily growth rate = 17.341%\n  2026-06-06 -> 2026-06-10: 91 -> 136 (4 days), daily growth rate = 10.567%\n  2026-06-10 -> 2026-06-13: 136 -> 181 (3 days), daily growth
rate = 9.997%\n  2026-06-13 -> 2026-06-14: 181 -> 192 (1 days), daily growth rate = 6.077%\n\nAverage daily new deaths:\n  2026-05-27 -> 2026-05-31: 26 new / 4 days = 6.5 per day\n  2026-05-31 ->
2026-06-02: 5 new / 2 days = 2.5 per day\n  2026-06-02 -> 2026-06-06: 43 new / 4 days = 10.8 per day\n  2026-06-06 -> 2026-06-10: 45 new / 4 days = 11.2 per day\n  2026-06-10 -> 2026-06-13: 45 new / 3
days = 15.0 per day\n  2026-06-13 -> 2026-06-14: 11 new / 1 days = 11.0 per day\n", "stderr": "", "duration_ms": 214}
```

## 💭 Thinking

Let me now run a more sophisticated simulation to project the deaths forward to the resolution date. I need to consider:

1. The question resolves based on the latest WHO DON published on or before June 27, 2026
2. WHO DONs have been published roughly weekly (May 29, June 6/8, June 13)
3. The data cutoff in the DON is typically a few days before publication
4. The most recent DON (DON607) was published June 13 with data as of June 10

So the key question is: what will the next DON report as DRC confirmed deaths?
Based on the publication pattern, I'd expect another DON around June 18-20 with data through mid-June, and potentially one more around June 24-27 that would be the final report used for resolution. The resolution will hinge on what those upcoming DONs show for confirmed deaths in the DRC.

I'll run a Monte Carlo simulation to model the uncertainty around future DON releases and their reported death counts.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\n# Key question: What will the WHO DON report as DRC confirmed deaths?\n# Resolution: Latest WHO DON published on or before June 27, 2026\n\n# WHO DON publication pattern:\n# DON605: published ~May 29, data as of May 27\n# DON606: published June 8, data as of June 6  \n# DON607: published June 13, data as of June 10\n# Pattern: DONs every ~5-7 days, data cutoff 2-3 days before publication\n\n# Most likely scenario: 1-2 more DONs before June 27\n# Next DON: ~June 18-20, data cutoff ~June 16-18\n# Following DON: ~June 24-27, data cutoff ~June 22-25\n\n# Current state (as of June 14, from ECDC/MoH): 192 confirmed deaths in DRC\n# Latest WHO DON (DON607, June 13): 136 deaths (data as of June 10)\n\n# Let me model the death trajectory\n# Recent growth rates (daily multiplicative):\n# June 2 -> June 6: 17.3% daily\n# June 6 -> June 10: 10.6% daily  \n# June 10 -> June 13: 10.0% daily\n# June 13 -> June 14: 6.1% daily (single day, noisy)\n\n# Recent absolute daily additions:\n# June 6-10: ~11.2/day\n# June 10-13: ~15.0/day\n# June 13-14: ~11.0/day\n\n# Let's also look at case growth and apply CFR\n# Cases: 515 (Jun 6) -> 676 (Jun 10) -> 782 (Jun 13) -> 808 (Jun 14)\n# Recent CFR has been rising: 17.7% -> 20.1% -> 23.1% -> 23.8%\n\n# Two approaches:\n# 1. Exponential growth model on deaths directly\n# 2. Project cases forward, apply CFR\n\n# Let's fit an exponential model to the more recent data (June 6 onward, when\n# growth stabilized somewhat)\n\nfrom scipy.optimize import curve_fit\n\n# Use data from June 6 onward for the more stable growth phase\n# Day 0 = June 6 for this analysis\nrecent_data = [\n    (0, 91),    # June 6\n    (4, 136),   # June 10\n    (7, 181),   # June 13\n    (8, 192),   # June 14\n]\n\ndays_r = np.array([d for d, _ in recent_data])\ndeaths_r = np.array([v for _, v in recent_data])\n\n# Fit exponential: deaths = a * exp(b * t)\ndef exp_model(t, a, b):\n    return a * np.exp(b * t)\n\npopt, pcov = curve_fit(exp_model, days_r, deaths_r, p0=[91, 0.1])\na_fit, b_fit = popt\nprint(f\"Exponential fit: deaths = {a_fit:.1f} * exp({b_fit:.4f} * t)\")\nprint(f\"Implied daily growth rate: {np.exp(b_fit)-1:.2%}\")\nprint(f\"Implied doubling time: {np.log(2)/b_fit:.1f} days\")\n\n# Also fit linear model for comparison\nfrom numpy.polynomial import polynomial as P\ncoeffs = np.polyfit(days_r, deaths_r, 1)\nprint(f\"\\nLinear fit: deaths = {coeffs[0]:.1f} * t + {coeffs[1]:.1f}\")\nprint(f\"Daily addition rate: {coeffs[0]:.1f}\")\n\n# Check residuals\nfor d, actual in recent_data:\n    exp_pred = exp_model(d, *popt)\n    lin_pred = np.polyval(coeffs, d)\n    print(f\"  Day {d}: actual={actual}, exp_pred={exp_pred:.0f}, lin_pred={lin_pred:.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Exponential fit: deaths = 92.8 * exp(0.0928 * t)\nImplied daily growth rate: 9.73%\nImplied doubling time: 7.5 days\n\nLinear fit: deaths = 12.8 * t + 89.1\nDaily addition
rate: 12.8\n  Day 0: actual=91, exp_pred=93, lin_pred=89\n  Day 4: actual=136, exp_pred=135, lin_pred=140\n  Day 7: actual=181, exp_pred=178, lin_pred=179\n  Day 8: actual=192, exp_pred=195,
lin_pred=192\n", "stderr": "", "duration_ms": 830}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\nnp.random.seed(42)\n\n# Monte Carlo simulation\n# Current known: 192 confirmed deaths as of June 14 (MoH data)\n# Latest WHO DON: DON607 = 136 deaths (data as of June 10, published June 13)\n\n# Key modeling decisions:\n# 1. When will the next DON(s) be published?\n# 2. What data cutoff will they use?\n# 3. What will the death count be at that cutoff?\n\n# WHO DON publication schedule analysis:\n# DON602: published May 17 (PHEIC declaration)\n# DON605: published ~May 29\n# DON606: published June 8 (10 days later)\n# DON607: published June 13 (5 days later)\n# During PHEIC with active outbreak, frequency appears to be every 5-7 days\n\n# Likely DON schedule:\n# Next DON: June 18-20 (5-7 days after DON607)\n# Following DON: June 24-27 (5-7 days after that)\n\n# Simulation approach:\n# 1. Simulate daily death counts from June 14 (day 8 in our June 6 baseline) forward\n# 2. Model DON publication dates probabilistically\n# 3. DON data cutoff = publication date - 2 to 3 days\n# 4. Report what the latest DON before June 27 would show\n\nN_SIM = 50000\n\n# Parameters from exponential fit on June 6-14 data\n# deaths = 92.8 * exp(0.0928 * t) where t=0 is June 6\n# But growth could slow as response scales up\n\n# Model 3 scenarios:\n# 1. Continued exponential growth at current rate (~9.7%/day)\n# 2. Decelerating growth (growth rate declining by ~0.5%/day)\n# 3. Linear growth at current rate (~13 deaths/day, potentially accelerating slightly)\n\n# Given that:\n# - No vaccine/treatment available\n# - Response is \"outpacing\" the outbreak (MSF)\n# - Geographic spread continuing (31 health zones)\n# - Underreporting likely\n# - But also: international response scaling up, IASC activation\n# The most likely scenario is continued growth but with some deceleration\n\n# Base death count as of June 14 (day 8 from June 6 baseline): 192\n# We need to project to the data cutoff of the last DON before June 27\n\n# Let's simulate from June 14 forward\ncurrent_deaths = 192\ncurrent_date = datetime(2026, 6, 14)\nresolution_date = datetime(2026, 6, 27)\n\n# DON publication model:\n# Next DON is likely June 18-20 (mode June 19)\n# Following DON is likely June 24-27 (mode June 25-26)\n\n# For each simulation:\n# 1. Draw DON publication dates\n# 2. Draw daily death growth parameters\n# 3. Compute death count at data cutoff of last qualifying DON\n\nresults = []\n\nfor sim in range(N_SIM):\n    # Draw growth parameters\n    # Recent daily growth rate: ~9.7% exponential\n    # But there's evidence of potential deceleration\n    # Model: daily multiplicative growth rate drawn from distribution\n    \n    # Scenario mixture:\n    # 60% probability: moderate deceleration (response takes effect gradually)\n    # 25% probability: continued rapid growth (response fails to contain)\n    # 15% probability: sharp deceleration (response succeeds, cases plateau)\n    \n    scenario = np.random.random()\n    \n    if scenario < 0.60:\n        # Moderate deceleration: growth rate starts at ~8-10% and declines\n        initial_growth_rate = np.random.normal(0.09, 0.015)\n        daily_decel = np.random.uniform(0.002, 0.005)  # growth rate declines by this much per day\n    elif scenario < 0.85:\n        # Continued rapid growth\n        initial_growth_rate = np.random.normal(0.095, 0.02)\n        daily_decel = np.random.uniform(-0.001, 0.002)  # minimal deceleration\n    else:\n        # Sharp deceleration\n        initial_growth_rate = np.random.normal(0.07, 0.015)\n        daily_decel = np.random.uniform(0.005, 0.01)\n    \n    # Simulate deaths forward from June 14\n    deaths = float(current_deaths)\n    deaths_by_day = [deaths]  # deaths_by_day[0] = June 14\n    \n    for day in range(1, 20):  # simulate through ~July 3\n        growth_rate = max(0.01, initial_growth_rate - daily_decel * day)\n        # Add noise\n        daily_growth = growth_rate + np.random.normal(0, 0.02)\n        daily_growth = max(0, daily_growth)\n        deaths = deaths * (1 + daily_growth)\n        deaths_by_day.append(deaths)\n    \n    # DON publication dates\n    # Next DON (DON608): June 17-21, mode ~June 19\n    don608_pub_day = int(np.random.choice([3, 4, 5, 6, 7], p=[0.05, 0.25, 0.40, 0.20, 0.10]))\n    # Data cutoff is typically 2-3 days before publication\n    don608_cutoff_day = don608_pub_day - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # Following DON (DON609): 5-8 days after DON608\n    don609_offset = np.random.choice([5, 6, 7, 8], p=[0.2, 0.35, 0.3, 0.15])\n    don609_pub_day = don608_pub_day + don609_offset\n    don609_cutoff_day = don609_pub_day - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # Possible DON610 if timing works out\n    don610_offset = np.random.choice([5, 6, 7, 8], p=[0.2, 0.35, 0.3, 0.15])\n    don610_pub_day = don609_pub_day + don610_offset\n    don610_cutoff_day = don610_pub_day - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # Resolution cutoff: June 27 = day 13 from June 14\n    resolution_day = 13\n    \n    # Find the last DON published on or before June 27\n    latest_don_cutoff = None\n    \n    if don610_pub_day <= resolution_day:\n        latest_don_cutoff = don610_cutoff_day\n    elif don609_pub_day <= resolution_day:\n        latest_don_cutoff = don609_cutoff_day\n    elif don608_pub_day <= resolution_day:\n        latest_don_cutoff = don608_cutoff_day\n    else:\n        # No new DON published - falls back to DON607 = 136\n        results.append(136)\n        continue\n    \n    # Ensure cutoff is valid\n    latest_don_cutoff = max(0, min(latest_don_cutoff, 19))\n    \n    # Get death count at that cutoff\n    reported_deaths = int(round(deaths_by_day[latest_don_cutoff]))\n    \n    # Apply a small reporting lag/adjustment (WHO DON might slightly differ from MoH)\n    # WHO DON has historically been slightly lower than MoH figures\n    # e.g., MoH June 14 = 192, but WHO DON607 (June 10 cutoff) = 136 vs MoH ~136\n    # Actually the WHO and MoH seem aligned on the same cutoff dates\n    # So no adjustment needed\n    \n    results.append(reported_deaths)\n\nresults = np.array(results)\n\n# Clamp to minimum of 91 (as per question bounds)\nresults = np.maximum(results, 91)\n\nprint(f\"Monte Carlo simulation results (N={N_SIM}):\")\nprint(f\"  Mean: {np.mean(results):.0f}\")\nprint(f\"  Median: {np.median(results):.0f}\")\nprint(f\"  Std Dev: {np.std(results):.0f}\")\nprint()\n\npercentiles = [1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 99]\nprint(\"Percentile distribution:\")\nfor p in percentiles:\n    val = np.percentile(results, p)\n    print(f\"  P{p:2d}: {val:.0f}\")\n\n# Check how often we get the fallback (DON607 = 136)\nfallback_rate = np.mean(results == 136)\nprint(f\"\\nFallback to DON607 (136 deaths) rate: {fallback_rate:.1%}\")\n\n# Check what the data cutoff date distribution looks like\nprint(f\"\\nP(result > 400): {np.mean(results > 400):.1%}\")\nprint(f\"P(result > 300): {np.mean(results > 300):.1%}\")\nprint(f\"P(result > 250): {np.mean(results > 250):.1%}\")\nprint(f\"P(result < 200): {np.mean(results < 200):.1%}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Monte Carlo simulation results (N=50000):\n  Mean: 354\n  Median: 344\n  Std Dev: 83\n\nPercentile distribution:\n  P 1: 222\n  P 5: 241\n  P10: 256\n  P15: 269\n  P20:
282\n  P25: 294\n  P30: 305\n  P40: 325\n  P50: 344\n  P60: 364\n  P70: 386\n  P75: 399\n  P80: 414\n  P85: 434\n  P90: 461\n  P95: 505\n  P99: 607\n\nFallback to DON607 (136 deaths) rate:
0.0%\n\nP(result > 400): 24.6%\nP(result > 300): 72.1%\nP(result > 250): 91.8%\nP(result < 200): 0.0%\n", "stderr": "", "duration_ms": 2347}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also think more carefully about the DON timing and data cutoff.\n# The question resolves to the most recent WHO DON published on or before June 27.\n# \n# Today is June 17. Let me reconsider:\n# DON607 was published June 13 with data as of June 10.\n# \n# Key issue: WHO DON has a specific pattern. Let me check if there might already be\n# a newer DON or one about to be published.\n#\n# Also, I should be more careful about the data cutoff vs what the DON reports.\n# The DON607 said 136 deaths (data as of June 10).\n# But MoH data as of June 14 = 192 deaths.\n# The GAP between WHO DON and actual MoH data grows with time.\n#\n# Let me re-examine: the question asks for the confirmed deaths figure IN the DON.\n# So I need to figure out what date the DON data cutoff will be, and what\n# the confirmed deaths will be at THAT date.\n#\n# Let me reconsider the simulation more carefully.\n\n# The fundamental question has these layers:\n# 1. How many DONs will be published between now (June 17) and June 27?\n# 2. What data cutoff will the last qualifying DON use?\n# 3. What will confirmed deaths be at that data cutoff?\n\n# From the DON pattern:\n# DON602: May 17 (PHEIC declaration)\n# DON605: May 29 (12 days later)\n# DON606: June 8 (10 days later) - data as of June 6\n# DON607: June 13 (5 days later) - data as of June 10\n# \n# Frequency appears to be increasing (reasonable for escalating outbreak).\n# Recent interval: 5-10 days.\n#\n# If we expect a DON roughly every 5-7 days:\n# DON608: ~June 18-20 (most likely), data cutoff ~June 16-18\n# DON609: ~June 23-27, data cutoff ~June 21-25\n#\n# Very likely at least one more DON; possibly two.\n\n# Let me also verify: what would deaths be at various cutoff dates based on\n# the trajectory?\n\n# From the data:\n# June 14: 192 deaths (known MoH)\n# If I project forward with exponential model:\n# deaths = 92.8 * exp(0.0928 * t), t from June 6 baseline\n\nfrom datetime import datetime\nimport numpy as np\n\na, b = 92.8, 0.0928\nbase_date = datetime(2026, 6, 6)\n\n# Exponential model projection (no deceleration scenario)\nprint(\"Exponential projection (no deceleration):\")\nfor date_str in [\"2026-06-14\", \"2026-06-16\", \"2026-06-18\", \"2026-06-20\", \n                  \"2026-06-22\", \"2026-06-24\", \"2026-06-25\", \"2026-06-27\"]:\n    d = datetime.strptime(date_str, \"%Y-%m-%d\")\n    t = (d - base_date).days\n    pred = a * np.exp(b * t)\n    print(f\"  {date_str} (t={t:2d}): {pred:.0f} deaths\")\n\n# Linear model projection\nm, c = 12.8, 89.1  # from earlier fit\nprint(\"\\nLinear projection (12.8 deaths/day):\")\nfor date_str in [\"2026-06-14\", \"2026-06-16\", \"2026-06-18\", \"2026-06-20\", \n                  \"2026-06-22\", \"2026-06-24\", \"2026-06-25\", \"2026-06-27\"]:\n    d = datetime.strptime(date_str, \"%Y-%m-%d\")\n    t = (d - base_date).days\n    pred = m * t + c\n    print(f\"  {date_str} (t={t:2d}): {pred:.0f} deaths\")\n\n# Let me also compute with moderate deceleration\nprint(\"\\nExponential with moderate deceleration (growth rate declining 0.3%/day from 9.3%):\")\ndeaths_decel = 192  # June 14\ngrowth_rate = 0.093\nfor day_offset in range(1, 14):\n    growth_rate_today = max(0.02, growth_rate - 0.003 * day_offset)\n    deaths_decel *= (1 + growth_rate_today)\n    d = datetime(2026, 6, 14) + timedelta(days=day_offset)\n    print(f\"  {d.strftime('%Y-%m-%d')}: {deaths_decel:.0f} deaths (growth={growth_rate_today:.1%})\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Exponential projection (no deceleration):\n  2026-06-14 (t= 8): 195 deaths\n  2026-06-16 (t=10): 235 deaths\n  2026-06-18 (t=12): 283 deaths\n  2026-06-20 (t=14): 340
deaths\n  2026-06-22 (t=16): 410 deaths\n  2026-06-24 (t=18): 493 deaths\n  2026-06-25 (t=19): 541 deaths\n  2026-06-27 (t=21): 651 deaths\n\nLinear projection (12.8 deaths/day):\n  2026-06-14 (t= 8):
192 deaths\n  2026-06-16 (t=10): 217 deaths\n  2026-06-18 (t=12): 243 deaths\n  2026-06-20 (t=14): 268 deaths\n  2026-06-22 (t=16): 294 deaths\n  2026-06-24 (t=18): 320 deaths\n  2026-06-25 (t=19):
332 deaths\n  2026-06-27 (t=21): 358 deaths\n\nExponential with moderate deceleration (growth rate declining 0.3%/day from 9.3%):\n  2026-06-15: 209 deaths (growth=9.0%)\n  2026-06-16: 227 deaths
(growth=8.7%)\n  2026-06-17: 247 deaths (growth=8.4%)\n  2026-06-18: 267 deaths (growth=8.1%)\n  2026-06-19: 287 deaths (growth=7.8%)\n  2026-06-20: 309 deaths (growth=7.5%)\n  2026-06-21: 331 deaths
(growth=7.2%)\n  2026-06-22: 354 deaths (growth=6.9%)\n  2026-06-23: 377 deaths (growth=6.6%)\n  2026-06-24: 401 deaths (growth=6.3%)\n  2026-06-25: 425 deaths (growth=6.0%)\n  2026-06-26: 449 deaths
(growth=5.7%)\n  2026-06-27: 474 deaths (growth=5.4%)\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\nnp.random.seed(42)\nN_SIM = 100000\n\n# Refined simulation\n# Key realization: The question resolves to the CONFIRMED DEATHS figure in the DON,\n# which uses a specific data cutoff date.\n\n# Known anchors:\n# June 6 data cutoff -> DON published June 8 -> 91 confirmed deaths (DON for DRC: ~91 deaths with ~515 cases)\n# June 10 data cutoff -> DON published June 13 -> 136 confirmed deaths\n# June 14 MoH data -> 192 confirmed deaths (NOT in a DON yet)\n\n# The simulation needs to:\n# 1. Project the actual MoH death count forward from June 14 (192)\n# 2. Determine when DONs will be published and their data cutoffs\n# 3. The resolution value = deaths at the data cutoff of the last qualifying DON\n\n# Death growth model from June 14:\n# Recent data shows growth rate of ~8-10% per day (exponential phase)\n# But the trajectory suggests some deceleration already:\n# Early: ~26%/day (May 27-31)\n# Mid: ~17%/day (June 2-6)\n# Recent: ~10%/day (June 6-14)\n# \n# Reasonable to expect continued deceleration as response scales up\n\ncurrent_deaths = 192  # As of June 14\ntoday = datetime(2026, 6, 14)\n\nresults = []\n\nfor sim in range(N_SIM):\n    # Growth model parameters\n    # Starting daily growth rate: draw from distribution centered on recent rates\n    initial_growth = np.random.normal(0.085, 0.02)  # ~8.5% with uncertainty\n    \n    # Daily deceleration rate: how fast the growth rate declines\n    # Weight toward some deceleration but uncertain magnitude\n    scenario = np.random.random()\n    if scenario < 0.15:\n        # Rapid containment scenario (unlikely without vaccine)\n        decel_rate = np.random.uniform(0.005, 0.008)\n    elif scenario < 0.65:\n        # Moderate deceleration (response gradually working)\n        decel_rate = np.random.uniform(0.002, 0.005)\n    elif scenario < 0.90:\n        # Slow deceleration (response struggling)\n        decel_rate = np.random.uniform(0.0, 0.002)\n    else:\n        # Acceleration scenario (outbreak overwhelms response)\n        decel_rate = np.random.uniform(-0.002, 0.0)\n    \n    # Simulate daily deaths from June 14 through June 27\n    deaths_by_day = [current_deaths]  # index 0 = June 14\n    deaths = float(current_deaths)\n    \n    for day in range(1, 14):  # June 15 through June 27\n        growth = initial_growth - decel_rate * day\n        growth = max(0.005, growth)  # minimum 0.5% daily growth (outbreak still active)\n        \n        # Add daily noise\n        noise = np.random.normal(0, 0.015)\n        effective_growth = max(0, growth + noise)\n        \n        deaths *= (1 + effective_growth)\n        deaths_by_day.append(deaths)\n    \n    # DON publication schedule\n    # DON607 published June 13. Next publications:\n    \n    # DON608: days after June 14 (index)\n    # Most likely June 18-20 (index 4-6 from June 14)\n    don608_pub_idx = np.random.choice([3, 4, 5, 6, 7], p=[0.05, 0.30, 0.35, 0.20, 0.10])\n    don608_cutoff_idx = don608_pub_idx - np.random.choice([2, 3], p=[0.5, 0.5])\n    don608_cutoff_idx = max(0, don608_cutoff_idx)\n    \n    # DON609: 5-8 days after DON608\n    don609_offset = np.random.choice([5, 6, 7, 8], p=[0.20, 0.35, 0.30, 0.15])\n    don609_pub_idx = don608_pub_idx + don609_offset\n    don609_cutoff_idx = don609_pub_idx - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # Resolution: last DON published on or before June 27 (index 13 from June 14)\n    resolution_idx = 13\n    \n    if don609_pub_idx <= resolution_idx:\n        # DON609 qualifies\n        cutoff_idx = min(don609_cutoff_idx, 13)\n        cutoff_idx = max(0, cutoff_idx)\n        reported = deaths_by_day[cutoff_idx]\n    elif don608_pub_idx <= resolution_idx:\n        # Only DON608 qualifies\n        cutoff_idx = min(don608_cutoff_idx, 13)\n        cutoff_idx = max(0, cutoff_idx)\n        reported = deaths_by_day[cutoff_idx]\n    else:\n        # No new DON - fallback to DON607 = 136\n        reported = 136\n    \n    results.append(int(round(reported)))\n\nresults = np.array(results)\nresults = np.maximum(results, 91)  # Lower bound\n\nprint(f\"Refined Monte Carlo simulation (N={N_SIM}):\")\nprint(f\"  Mean: {np.mean(results):.0f}\")\nprint(f\"  Median: {np.median(results):.0f}\")\nprint(f\"  Std Dev: {np.std(results):.0f}\")\n\npercentiles = [1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 99]\npct_vals = {}\nprint(\"\\nPercentile distribution:\")\nfor p in percentiles:\n    val = np.percentile(results, p)\n    pct_vals[str(p)] = round(float(val))\n    print(f\"  P{p:2d}: {val:.0f}\")\n\nprint(f\"\\nP(DON607 fallback): {np.mean(results == 136):.2%}\")\nprint(f\"P(result > 400): {np.mean(results > 400):.1%}\")\nprint(f\"P(result > 300): {np.mean(results > 300):.1%}\")\nprint(f\"P(result > 250): {np.mean(results > 250):.1%}\")\nprint(f\"P(result < 200): {np.mean(results < 200):.1%}\")\n\n# Break down by scenario: what does the DON cutoff date distribution look like?\nprint(\"\\nScenario analysis:\")\nprint(f\"  DON609 qualifies: {np.mean([don609_pub_idx <= 13 for _ in range(1000)]):.1%}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Refined Monte Carlo simulation (N=100000):\n  Mean: 347\n  Median: 336\n  Std Dev: 77\n\nPercentile distribution:\n  P 1: 223\n  P 5: 243\n  P10: 259\n  P15: 271\n  P20:
281\n  P25: 291\n  P30: 300\n  P40: 318\n  P50: 336\n  P60: 355\n  P70: 377\n  P75: 390\n  P80: 406\n  P85: 424\n  P90: 450\n  P95: 491\n  P99: 580\n\nP(DON607 fallback): 0.00%\nP(result > 400):
21.6%\nP(result > 300): 69.8%\nP(result > 250): 92.9%\nP(result < 200): 0.0%\n\nScenario analysis:\n  DON609 qualifies: 100.0%\n", "stderr": "", "duration_ms": 3270}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also check: could the growth rate already be lower than my model suggests?\n# The data point from June 13->14 (single day) showed 6.1% growth.\n# But single-day data is very noisy.\n# \n# More importantly, let me look at the CASE trajectory and CFR separately,\n# since deaths lag cases.\n\n# Case data:\n# May 19: 33 cases\n# May 30: 282 cases  \n# May 31: 291 cases\n# June 2: 321 cases\n# June 6: 515 cases\n# June 10: 676 cases\n# June 13: 782 cases\n# June 14: 808 cases\n\n# Case growth June 10-14: 808/676 = 1.195 over 4 days = 4.56%/day\n# Case growth June 6-10: 676/515 = 1.313 over 4 days = 7.02%/day\n# Case growth June 6-13: 782/515 = 1.519 over 7 days = 6.15%/day\n\n# So case growth IS decelerating from ~7%/day to ~4.6%/day\n\n# Death growth:\n# June 6-10: 136/91 = 1.494 over 4 days = 10.6%/day\n# June 10-14: 192/136 = 1.412 over 4 days = 9.0%/day\n\n# Deaths growing FASTER than cases \u2192 CFR is rising\n# CFR: 17.7% (June 6) \u2192 20.1% (June 10) \u2192 23.8% (June 14)\n# This is expected as earlier cases die\n\n# For projecting deaths: use case growth rate + rising CFR\n# Or more directly, just use the death growth rate and account for deceleration\n\n# Let me reconsider: is my growth rate estimate too high?\n# Recent death growth: ~9% per day (June 10-14)\n# But cases are growing at only ~4.5% per day (June 10-14)\n# Deaths will eventually track cases, with a lag\n\n# A more careful model:\n# 1. Project cases at decelerating rate\n# 2. Apply time-lagged CFR\n\n# Case growth has decelerated from ~7%/day to ~4.5%/day over the last week\n# This deceleration of ~0.36%/day is significant\n\n# Let me try this approach too\nprint(\"Case-based projection:\")\nprint(f\"Recent case growth: June 6-10 = 7.0%/day, June 10-14 = 4.6%/day\")\nprint(f\"Growth deceleration: ~0.6%/day\")\nprint(f\"Current CFR: ~23.8% (192/808)\")\nprint()\n\n# If case growth continues decelerating at 0.3-0.6%/day:\ncases = 808  # June 14\ndeaths_total = 192\ncfr = 0.238\n\nfor day in range(1, 14):\n    # Case growth decelerating\n    case_growth = max(0.01, 0.045 - 0.003 * day)\n    cases *= (1 + case_growth)\n    \n    # CFR stabilizes around 25-27%\n    cfr_target = 0.26\n    cfr = cfr + 0.3 * (cfr_target - cfr)\n    \n    deaths_total = cases * cfr\n    \n    d = datetime(2026, 6, 14) + timedelta(days=day)\n    print(f\"  {d.strftime('%Y-%m-%d')}: cases={cases:.0f}, CFR={cfr:.1%}, deaths={deaths_total:.0f}, case_growth={case_growth:.1%}\")\n\n# This gives us another estimate. The case-based approach suggests somewhat\n# lower death totals because case growth is already decelerating.\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Case-based projection:\nRecent case growth: June 6-10 = 7.0%/day, June 10-14 = 4.6%/day\nGrowth deceleration: ~0.6%/day\nCurrent CFR: ~23.8% (192/808)\n\n  2026-06-15:
cases=842, CFR=24.5%, deaths=206, case_growth=4.2%\n  2026-06-16: cases=875, CFR=24.9%, deaths=218, case_growth=3.9%\n  2026-06-17: cases=906, CFR=25.2%, deaths=229, case_growth=3.6%\n  2026-06-18:
cases=936, CFR=25.5%, deaths=238, case_growth=3.3%\n  2026-06-19: cases=964, CFR=25.6%, deaths=247, case_growth=3.0%\n  2026-06-20: cases=990, CFR=25.7%, deaths=255, case_growth=2.7%\n  2026-06-21:
cases=1014, CFR=25.8%, deaths=262, case_growth=2.4%\n  2026-06-22: cases=1035, CFR=25.9%, deaths=268, case_growth=2.1%\n  2026-06-23: cases=1054, CFR=25.9%, deaths=273, case_growth=1.8%\n  2026-06-24:
cases=1070, CFR=25.9%, deaths=277, case_growth=1.5%\n  2026-06-25: cases=1083, CFR=26.0%, deaths=281, case_growth=1.2%\n  2026-06-26: cases=1093, CFR=26.0%, deaths=284, case_growth=1.0%\n  2026-06-27:
cases=1104, CFR=26.0%, deaths=287, case_growth=1.0%\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\nnp.random.seed(42)\nN_SIM = 100000\n\n# Refined simulation v2\n# Now using TWO approaches and mixing them:\n# Approach A: Direct death trajectory projection  \n# Approach B: Case projection + CFR\n\n# IMPORTANT insight: The case growth rate has ALREADY decelerated significantly\n# from ~7%/day to ~4.5%/day. Death growth will follow with a lag.\n# My initial simulation may have overestimated growth.\n\n# Let me use a more data-driven approach:\n# - Death growth rate as of June 10-14: ~9%/day \n# - But case growth is ~4.5%/day and decelerating\n# - Deaths will catch up to the case deceleration with maybe a 5-7 day lag\n# - So death growth should start declining from ~9% toward ~4-5% over next week\n\ncurrent_deaths = 192  # June 14\ntoday = datetime(2026, 6, 14)\n\nresults = []\n\nfor sim in range(N_SIM):\n    # Model choice\n    model = np.random.random()\n    \n    if model < 0.4:\n        # Model A: Death-based exponential with deceleration \n        # Starts at ~8-9%/day, decelerates\n        init_rate = np.random.normal(0.085, 0.015)\n        decel = np.random.uniform(0.002, 0.006)  # per day\n        min_rate = np.random.uniform(0.01, 0.03)\n        \n        deaths = float(current_deaths)\n        deaths_by_day = [deaths]\n        for day in range(1, 14):\n            rate = max(min_rate, init_rate - decel * day)\n            noise = np.random.normal(0, 0.015)\n            deaths *= (1 + max(0, rate + noise))\n            deaths_by_day.append(deaths)\n    \n    elif model < 0.7:\n        # Model B: Case-based with CFR\n        # Case growth starts at ~4.5% and decelerates\n        init_case_rate = np.random.normal(0.045, 0.01)\n        case_decel = np.random.uniform(0.001, 0.004)\n        min_case_rate = np.random.uniform(0.005, 0.02)\n        \n        cases = 808.0\n        cfr = np.random.normal(0.238, 0.01)\n        cfr_target = np.random.normal(0.26, 0.02)\n        cfr_speed = np.random.uniform(0.1, 0.3)\n        \n        deaths_by_day = [current_deaths]\n        for day in range(1, 14):\n            case_rate = max(min_case_rate, init_case_rate - case_decel * day)\n            noise = np.random.normal(0, 0.01)\n            cases *= (1 + max(0, case_rate + noise))\n            cfr = cfr + cfr_speed * (cfr_target - cfr)\n            deaths = cases * cfr\n            deaths_by_day.append(deaths)\n    \n    else:\n        # Model C: Continued high growth (outbreak worsening)\n        # Less likely but accounts for tail risk\n        init_rate = np.random.normal(0.09, 0.02)\n        decel = np.random.uniform(-0.001, 0.003)\n        \n        deaths = float(current_deaths)\n        deaths_by_day = [deaths]\n        for day in range(1, 14):\n            rate = max(0.02, init_rate - decel * day)\n            noise = np.random.normal(0, 0.02)\n            deaths *= (1 + max(0, rate + noise))\n            deaths_by_day.append(deaths)\n    \n    # DON publication schedule\n    # Index 0 = June 14\n    # DON608: most likely index 4-6 (June 18-20)\n    don608_pub = np.random.choice([3, 4, 5, 6, 7], p=[0.05, 0.30, 0.35, 0.20, 0.10])\n    don608_cutoff = max(0, don608_pub - np.random.choice([2, 3], p=[0.5, 0.5]))\n    \n    # DON609: 5-8 days after DON608\n    don609_offset = np.random.choice([5, 6, 7, 8], p=[0.20, 0.35, 0.30, 0.15])\n    don609_pub = don608_pub + don609_offset\n    don609_cutoff = don609_pub - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # June 27 = index 13\n    resolution_idx = 13\n    \n    if don609_pub <= resolution_idx:\n        cutoff = min(max(0, don609_cutoff), 13)\n        reported = deaths_by_day[cutoff]\n    elif don608_pub <= resolution_idx:\n        cutoff = min(max(0, don608_cutoff), 13)\n        reported = deaths_by_day[cutoff]\n    else:\n        reported = 136  # DON607 fallback\n    \n    results.append(int(round(reported)))\n\nresults = np.array(results)\nresults = np.maximum(results, 91)\n\nprint(f\"Refined Monte Carlo v2 (N={N_SIM}):\")\nprint(f\"  Mean: {np.mean(results):.0f}\")\nprint(f\"  Median: {np.median(results):.0f}\")\nprint(f\"  Std Dev: {np.std(results):.0f}\")\n\npercentiles = [1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 99]\npct_vals = {}\nprint(\"\\nPercentile distribution:\")\nfor p in percentiles:\n    val = np.percentile(results, p)\n    pct_vals[str(p)] = round(float(val))\n    print(f\"  P{p:2d}: {val:.0f}\")\n\nprint(f\"\\nP(result > 400): {np.mean(results > 400):.1%}\")\nprint(f\"P(result > 300): {np.mean(results > 300):.1%}\")\nprint(f\"P(result > 250): {np.mean(results > 250):.1%}\")\nprint(f\"P(result < 200): {np.mean(results < 200):.1%}\")\nprint(f\"P(DON607 fallback): {np.mean(results == 136):.2%}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Refined Monte Carlo v2 (N=100000):\n  Mean: 330\n  Median: 315\n  Std Dev: 76\n\nPercentile distribution:\n  P 1: 219\n  P 5: 238\n  P10: 249\n  P15: 258\n  P20: 267\n
P25: 274\n  P30: 282\n  P40: 298\n  P50: 315\n  P60: 333\n  P70: 355\n  P75: 369\n  P80: 384\n  P85: 403\n  P90: 429\n  P95: 474\n  P99: 573\n\nP(result > 400): 15.7%\nP(result > 300): 58.5%\nP(result
> 250): 89.4%\nP(result < 200): 0.1%\nP(DON607 fallback): 0.00%\n", "stderr": "", "duration_ms": 3415}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also check if there's already been a DON608 published (it's June 17 today)\n# The DON607 was June 13, so a new DON could be out by now\n\n# Let me also do a sanity check on my growth assumptions\n# The most recent reliable data points for deaths:\n# June 6: 91 (WHO DON)\n# June 10: 136 (WHO DON607)  \u2192 4 days, +45, 10.6%/day\n# June 14: 192 (MoH/ECDC)   \u2192 4 days, +56, 9.0%/day\n\n# Daily new deaths:\n# June 6-10: 11.2/day average\n# June 10-14: 14.0/day average\n\n# So daily new deaths are INCREASING (even though growth rate is declining)\n# This is typical of early exponential - absolute numbers rise even as \n# the rate of growth declines\n\n# The key question for the DON data cutoff is:\n# - If DON608 has data through ~June 16-17, deaths are probably ~230-250\n# - If DON609 has data through ~June 22-24, deaths could be ~280-380\n\n# Let me verify my models against the known data points\nprint(\"Model validation against known data:\")\nprint(f\"  June 6 actual: 91\")\nprint(f\"  June 10 actual: 136\")\nprint(f\"  June 14 actual: 192\")\nprint()\n\n# Let's check what my models would have predicted for June 14 starting from June 10\n# Model A: 136 * (1.085)^4 = 136 * 1.389 = 189 \u2713\n# Model B: 676 cases * 4.5% growth for 4 days = 676*1.045^4 = 807 cases, CFR 23.8% = 192 \u2713\nprint(\"Forward validation from June 10 (136 deaths, 676 cases):\")\nprint(f\"  Model A (8.5%/day): 136 * 1.085^4 = {136 * 1.085**4:.0f}\")\nprint(f\"  Model B (4.5%/day cases, 23.8% CFR): {676 * 1.045**4 * 0.238:.0f}\")\nprint()\n\n# Now let me think about what's most likely:\n# Given that DONs come every 5-8 days (recent pattern accelerating),\n# and DON607 was June 13:\n# DON608 very likely by June 18-20 \u2192 data cutoff June 16-18\n# DON609 possible by June 24-27 \u2192 data cutoff June 22-25\n\n# If the last DON has a June 16-18 cutoff:\n# Deaths ~230-260 (from deceleration model)\n# If the last DON has a June 22-24 cutoff: \n# Deaths ~270-400 (wide range due to growth uncertainty)\n\n# The most likely scenario is that DON609 is published before June 27,\n# giving us a cutoff around June 22-24.\n\n# Let me see what fraction of my simulations have DON609 qualifying\nn_don609 = 0\nn_don608_only = 0\nfor sim in range(10000):\n    don608_pub = np.random.choice([3, 4, 5, 6, 7], p=[0.05, 0.30, 0.35, 0.20, 0.10])\n    don609_offset = np.random.choice([5, 6, 7, 8], p=[0.20, 0.35, 0.30, 0.15])\n    don609_pub = don608_pub + don609_offset\n    \n    if don609_pub <= 13:\n        n_don609 += 1\n    elif don608_pub <= 13:\n        n_don608_only += 1\n\nprint(f\"DON609 published before June 27: {n_don609/10000:.1%}\")\nprint(f\"Only DON608 (not DON609): {n_don608_only/10000:.1%}\")\nprint(f\"Neither (fallback to DON607): {(10000-n_don609-n_don608_only)/10000:.1%}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Model validation against known data:\n  June 6 actual: 91\n  June 10 actual: 136\n  June 14 actual: 192\n\nForward validation from June 10 (136 deaths, 676 cases):\n  Model
A (8.5%/day): 136 * 1.085^4 = 188\n  Model B (4.5%/day cases, 23.8% CFR): 192\n\nDON609 published before June 27: 92.9%\nOnly DON608 (not DON609): 7.1%\nNeither (fallback to DON607): 0.0%\n",
"stderr": "", "duration_ms": 98}
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"WHO\" \"Disease Outbreak News\" \"Ebola\" \"DON608\" OR \"DON609\" site:who.int 2026"
}
```

### 📋 Result

```
{"query": "\"WHO\" \"Disease Outbreak News\" \"Ebola\" \"DON608\" OR \"DON609\" site:who.int 2026", "results": [{"title": "Ebola outbreak in Africa - preparedness in the WHO European Region", "url":
"https://www.who.int/europe/emergencies/situations/ebola-outbreak-in-africa-preparedness-in-the-who-european-region", "snippet": "Epidemic of Ebola disease caused by Bundibugyo virus in the Democratic
Republic of the Congo (DRC) and Uganda 2026: preparedness in the WHO European Region\nOverview\nOn 15 May 2026, the Ministry of Public Health, Hygiene and Social Welfare of the Democratic Republic of
the Congo (DRC) and the Ministry of Health of Uganda declared an outbreak of Ebola disease following the confirmation of Bundibugyo virus disease (BVD) in both countries. On 17 May 2026, WHO\u2019s
Director-General determined that Ebola", "api_data": null, "hint": null}, {"title": "2026 Central Africa Ebola epidemic", "url": "https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic",
"snippet": "In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months
after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province,
and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo provin", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Ebola
epidemic\", \"url\": \"https://en.wikipedia.org/wiki/2026_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo
(DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of
Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo province on 21
May.\\nThe epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola treatments were created for a different strain, the Zaire ebolavirus. The outbreak
was declared a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16 May 2026.\\nThere have been 192 confirmed deaths in D.R. Congo, and two deaths in
Uganda, as of 14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection, treatment and prevention of the disease; it is considered likely that the true scale
of the outbreak could considerably exceed the confirmed numbers.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Ebola outbreak - DRC 2026", "url":
"https://www.who.int/emergencies/situations/ebola-outbreak---drc-2026", "snippet": "![EbolaDRC2026_Supplies2 Emergency supplies being loaded off plane](https://cdn.who.int/media/images/default-
source/emergencies-and-disasters/2026---ebola-outbreak---drc/eboladrc2026_supplies2.jpg?sfvrsn=da475c39_2)\n![](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2026---ebola-
outbreak---drc/ebolaresponse_drc_2026.tmb-1920v.jpg?sfvrsn=15234691_6)\nEbola\nThe Democratic Republic of the Congo, 2026\nOverview\nAn Ebola outbreak was confirmed in the Democratic Republic of th",
"api_data": null, "hint": null}, {"title": "Joint statement by the Government of the Democratic Republic of the Congo and WHO concerning the outbreak of Ebola disease caused by the Bundibugyo virus",
"url": "https://www.who.int/news/item/31-05-2026-joint-statement-by-the-government-of-the-democratic-republic-of-the-congo-and-who-concerning-the-outbreak-of-ebola-disease-caused-by-the-bundibugyo-
virus", "snippet": "The Government of the Democratic Republic of the Congo (DRC) and the World Health Organization (WHO) reaffirm their strong partnership and shared commitment to protect the health
and well-being of the people of Ituri Province and the nation at large, following the joint mission to Bunia led by Dr Samuel Roger Kamba, Minister of Health, Mr. Patrick Muyaya Katembwe, Minister of
Communication and Medias, and the visit of WHO Director-General Dr Tedros Adhanom Ghebreyesus.\nThis high-level visit come", "api_data": null, "hint": null}, {"title": "Ebola disease caused by
Bundibugyo virus, Democratic Republic of the Congo & Uganda", "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607", "snippet": "Situation at a glance\nDescription of the
situation\nSince the last [Disease Outbreak News](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON606) was published on 8 June 2026, the number of confirmed cases and deaths have
increased rapidly in the Democratic Republic of the Congo. In total, 695 confirmed cases; 676 from the Democratic Republic of the Congo and 19 from Uganda; and 138 deaths including two from Uganda,
have been reported from both countries, while at least 37 people", "api_data": null, "hint": null}, {"title": "Africa CDC and WHO launch joint continental Ebola response plan", "url":
"https://www.who.int/news/item/05-06-2026-africa-cdc-and-who-launch-joint-continental-ebola-response-plan", "snippet": "The Africa Centres for Disease Control and Prevention (Africa CDC) and the World
Health Organization (WHO) today launched a joint [continental preparedness and response plan](https://www.afro.who.int/publications/bundibugyo-ebola-virus-continental-preparedness-and-response-plan-
june-november-2026) on the ongoing Ebola outbreak caused by the Bundibugyo virus. The plan aims to raise US$ 518 million to support African countries together with partners to prepare for, rapidly
detect and respond to th", "api_data": null, "hint": null}, {"title": "Ongoing outbreak in the Democratic Republic of the Congo | WHO | Regional Office for Africa", "url":
"https://www.afro.who.int/health-topics/ebola-disease/outbreak-drc-26", "snippet": "Bundibugyo virus disease outbreak Democratic Republic of the Congo\nThe Democratic Republic of the Congo is
responding to an outbreak of Ebola disease caused by Bundibugyo virus in the north-eastern Ituri Province \u2014 the country's 17th Ebola outbreak since the virus was first identified in 1976. The WHO
Director-General has determined that the outbreak, which was declared on 15 May 2026, constitutes a Public Health Emergency of International Concern (PHEIC), requiring international coordination an",
"api_data": null, "hint": null}, {"title": "First meeting of the IHR Emergency Committee regarding the epidemic of Ebola Bundibugyo virus disease in the Democratic Republic of the Congo and Uganda
2026 \u2013 Temporary recommendations", "url": "https://www.who.int/news/item/22-05-2026-first-meeting-of-the-ihr-emergency-committee-regarding-the-epidemic-of-ebola-bundibugyo-virus-disease-in-the-
democratic-republic-of-the-congo-and-uganda-2026-temporary-recommendations", "snippet": "On 17 May 2026, pursuant to paragraph 2 of Article 12 - Determination of a public health emergency of
international concern, including a pandemic emergency of the [International Health Regulations (2005)](https://apps.who.int/gb/bd/pdf_files/IHR_2014-2022-2024-en.pdf) (IHR), the Director-General (DG)
of the World Health Organization (WHO), after having consulted the States Parties where the event was known to be occurring, determined that the epidemic of Ebola disease caused by Bundibugyo virus ",
"api_data": null, "hint": null}, {"title": "WHO Director-General's opening remarks at the media briefing on the Bundibugyo Ebola outbreak \u2013 3 June 2026", "url": "https://www.who.int/news-
room/speeches/item/who-director-general-s-opening-remarks-at-the-media-briefing---3-june-2026", "snippet": "Good afternoon to everyone in the room, and good morning, good afternoon and good evening to
those joining us online.\nYesterday I returned from a visit to the Democratic Republic of the Congo, including to the epicentre of the Ebola outbreak in the province of Ituri.\nI met with political
leaders, senior health officials, Ambassadors, partners, WHO colleagues, frontline responders, community and faith leaders, women\u2019s groups, business leaders, traditional healers and
more.\nI\u2019m very encouraged by ", "api_data": null, "hint": null}, {"title": "Ebola disease", "url": "https://www.who.int/news-room/fact-sheets/detail/ebola-disease", "snippet": "Key facts\n-
Ebola disease is a severe, often fatal illness in humans.\n- Three different viruses are known to cause large Ebola disease outbreaks: Ebola virus, Sudan virus and Bundibugyo virus.\n- The average
Ebola disease case fatality rate is around 50%. Case fatality rates have varied from 25\u201390% in past outbreaks.\n- Early intensive supportive care with rehydration and the treatment of symptoms
improves survival.\n- Approved vaccines and treatments are only available for one of the viruses (Ebol", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.who.int/emergencies/disease-outbreak-news",
  "prompt": "List the most recent Disease Outbreak News articles about Ebola in 2026. What are their DON numbers and publication dates? Is there anything newer than DON607?"
}
```

### 📋 Result

```
{"url": "https://www.who.int/emergencies/disease-outbreak-news", "content": "Based on the provided content, I cannot answer your specific questions about:\n- The most recent Disease Outbreak News
articles about Ebola in 2026\n- Their DON numbers and publication dates\n- Whether there is anything newer than DON607\n\n**Why:** The content you provided is only the introductory/header text of the
WHO Disease Outbreak News page. It explains what DONs are and their purpose under the International Health Regulations (2005), but it does not contain any actual list of disease outbreak articles,
dates, DON numbers, or specific information about Ebola outbreaks.\n\nTo answer your questions, I would need access to the actual list of DON articles published on that page, which would typically
appear below this introductory text.\n\n**Relevant links:**\n- The content mentions you can find this information at: https://www.who.int/emergencies/disease-outbreak-news", "title": "Disease Outbreak
News"}
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "WHO Disease Outbreak News Ebola June 17 18 2026 latest DON"
}
```

### 📋 Result

```
{"query": "WHO Disease Outbreak News Ebola June 17 18 2026 latest DON", "results": [{"title": "Ebola virus outbreak 2026 - Public Health - European Commission", "url":
"https://health.ec.europa.eu/health-security-and-infectious-diseases/crisis-management/ebola-virus-outbreak-2026_en", "snippet": "On 17 May 2026, the World Health Organization (WHO) determined that
the Ebola virus disease outbreak caused by Bundibugyo virus in the Democratic Republic of the Congo (DRC) and Uganda constitutes [a public health emergency of international concern
(PHEIC)](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON602). This means that the outbreak poses a serious, unusual, cross-border risk that requires coordinated international
action.\nThe European Centre for Disease Prevention and C", "api_data": null, "hint": null}, {"title": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda", "url":
"https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda", "snippet": "Ebola disease outbreak in the Democratic Republic of the Congo and Uganda\nThis page is updated as more
information becomes available. It was last updated 16 June at 15:10.\nAs of 16 June 2026, the Ebola disease outbreak caused by Bundibugyo virus is affecting the Democratic Republic of the Congo (DRC)
and Uganda.\nOn 15 June, the [DRC Ministry of Health reported](https://insp.cd/sitrep-n31-mvb_14-06-2026/) a total of 808 confirmed cases, including 192 confirmed related deaths, and 363 individuals
", "api_data": null, "hint": null}, {"title": "WHO and Africa CDC declare the 2026 Ebola disease outbreak a public health emergency - The Lancet", "url":
"https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01101-3/fulltext", "snippet": null, "api_data": null, "hint": null}, {"title": "Ebola outbreak in Africa - preparedness in the WHO
European Region", "url": "https://www.who.int/europe/emergencies/situations/ebola-outbreak-in-africa-preparedness-in-the-who-european-region", "snippet": "Epidemic of Ebola disease caused by
Bundibugyo virus in the Democratic Republic of the Congo (DRC) and Uganda 2026: preparedness in the WHO European Region\nOverview\nOn 15 May 2026, the Ministry of Public Health, Hygiene and Social
Welfare of the Democratic Republic of the Congo (DRC) and the Ministry of Health of Uganda declared an outbreak of Ebola disease following the confirmation of Bundibugyo virus disease (BVD) in both
countries. On 17 May 2026, WHO\u2019s Director-General determined that Ebola", "api_data": null, "hint": null}, {"title": "Ebola disease caused by Bundibugyo virus, Democratic Republic of the Congo &
Uganda", "url": "https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607", "snippet": "Situation at a glance\nDescription of the situation\nSince the last [Disease Outbreak
News](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON606) was published on 8 June 2026, the number of confirmed cases and deaths have increased rapidly in the Democratic Republic
of the Congo. In total, 695 confirmed cases; 676 from the Democratic Republic of the Congo and 19 from Uganda; and 138 deaths including two from Uganda, have been reported from both countries, while
at least 37 people", "api_data": null, "hint": null}, {"title": "2026 Central Africa Ebola epidemic", "url": "https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic", "snippet": "In May
2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th Ebola outbreak in the DRC and began only five months after the end of the
previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with imported cases from Ituri reported in North Kivu Province, and in Uganda's
capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo provin", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Ebola epidemic\", \"url\":
\"https://en.wikipedia.org/wiki/2026_Ebola_epidemic\", \"extract\": \"In May 2026, an epidemic of Ebola was reported in the Ituri Province of the Democratic Republic of the Congo (DRC). It is the 17th
Ebola outbreak in the DRC and began only five months after the end of the previous outbreak. Early infections have been theorized to have occurred in February 2026 in the town of Mongbwalu, with
imported cases from Ituri reported in North Kivu Province, and in Uganda's capital city of Kampala. A case in South Kivu was reported to have been imported from Tshopo province on 21 May.\\nThe
epidemic is caused by the Bundibugyo ebolavirus, which may complicate response efforts as existing Ebola treatments were created for a different strain, the Zaire ebolavirus. The outbreak was declared
a public health emergency of international concern (PHEIC) by the World Health Organization (WHO) on 16 May 2026.\\nThere have been 192 confirmed deaths in D.R. Congo, and two deaths in Uganda, as of
14 June. Poor healthcare infrastructure in the region and an ongoing armed conflict hinder detection, treatment and prevention of the disease; it is considered likely that the true scale of the
outbreak could considerably exceed the confirmed numbers.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Ebola outbreak - DRC 2026", "url": "https://www.who.int/emergencies/situations/ebola-
outbreak---drc-2026", "snippet": "![EbolaDRC2026_Supplies2 Emergency supplies being loaded off plane](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2026---ebola-outbreak---
drc/eboladrc2026_supplies2.jpg?sfvrsn=da475c39_2)\n![](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2026---ebola-outbreak---
drc/ebolaresponse_drc_2026.tmb-1920v.jpg?sfvrsn=15234691_6)\nEbola\nThe Democratic Republic of the Congo, 2026\nOverview\nAn Ebola outbreak was confirmed in the Democratic Republic of th", "api_data":
null, "hint": null}, {"title": "Ebola virus disease", "url": "https://www.who.int/emergencies/emergency-events/item/ebola", "snippet": "Ebola virus disease\nDisease Outbreak News\n19 June 2021 | Ebola
virus disease - Guinea\nDisease Outbreak News\n4 May 2021 | Ebola virus disease - Democratic Republic of the Congo\nDisease Outbreak News\n17 February 2021 | Ebola virus disease - Guinea\nDisease
Outbreak News\n10 February 2021 | Ebola virus disease - Democratic Republic of the Congo\nDisease Outbreak News\n18 November 2020 | Ebola virus disease - Democratic Republic of the Congo\nDisease
Outbreak News\n3 September 2020 | Ebola virus disease -", "api_data": null, "hint": null}]}
```

## 💭 Thinking

It seems DON607 (June 13) is still the latest DON as of now (June 17). No DON608 found yet. Let me now proceed with my analysis and reflection. Let me consolidate what I know and run the reflection/premortem pipeline.

Key findings:
1. Latest WHO DON is DON607 (published June 13, data as of June 10): 136 confirmed deaths in DRC
2. Latest MoH data (June 14): 192 confirmed deaths, 808 confirmed cases in DRC
3. Wikipedia says 192 deaths as of June 14
4. ECDC (updated June 16): 808 confirmed cases, 192 deaths as of June 14
5. No DON608 yet as of June 17

Based on the pattern of releases, I'm expecting DON608 to arrive within the next few days and DON609 by late June. My Monte Carlo simulation suggests a median around 315 deaths, though there's considerable uncertainty. The critical question is what data cutoff date the final qualifying DON will have and how many deaths are reported at that point—if DON608 arrives soon, it might still be using relatively recent data from mid-June.

## 💬 Response

Now let me consolidate my analysis. The latest WHO DON is still DON607 (June 13). Let me run the final simulation with sensitivity testing.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\nnp.random.seed(123)\nN_SIM = 200000\n\n# FINAL SIMULATION - incorporating all evidence\n# \n# Key known data:\n# DON607: published June 13, data as of June 10 -> 136 confirmed deaths (DRC)\n# MoH as of June 14: 192 confirmed deaths, 808 confirmed cases\n# Today: June 17\n# Resolution: latest WHO DON on or before June 27\n# \n# DON publication pattern: DON605(May29), DON606(Jun8), DON607(Jun13)\n# Intervals: 10 days, 5 days \u2192 frequency appears to be increasing\n# No DON608 yet as of June 17\n\ncurrent_deaths = 192  # MoH as of June 14\ncurrent_cases = 808   # MoH as of June 14\n\nresults = []\ncutoff_dates = []\n\nfor sim in range(N_SIM):\n    # --- GROWTH MODEL ---\n    # Mix of approaches, weighted by plausibility\n    model = np.random.random()\n    \n    if model < 0.35:\n        # Model A: Death trajectory with moderate deceleration\n        # Recent death growth: ~9%/day (June 10-14), already down from ~10.6% (June 6-10)\n        init_rate = np.random.normal(0.08, 0.015)\n        decel = np.random.uniform(0.002, 0.005)\n        min_rate = np.random.uniform(0.01, 0.025)\n        \n        deaths = float(current_deaths)\n        deaths_by_day = [deaths]\n        for day in range(1, 14):\n            rate = max(min_rate, init_rate - decel * day)\n            noise = np.random.normal(0, 0.015)\n            deaths *= (1 + max(0.005, rate + noise))\n            deaths_by_day.append(deaths)\n    \n    elif model < 0.65:\n        # Model B: Case-driven with CFR approach\n        # Case growth: ~4.5%/day and decelerating\n        init_case_rate = np.random.normal(0.043, 0.008)\n        case_decel = np.random.uniform(0.001, 0.003)\n        min_case_rate = np.random.uniform(0.005, 0.015)\n        \n        cases = float(current_cases)\n        cfr = np.random.normal(0.238, 0.01)\n        cfr_target = np.random.normal(0.26, 0.02)\n        cfr_speed = np.random.uniform(0.15, 0.3)\n        \n        deaths_by_day = [current_deaths]\n        for day in range(1, 14):\n            case_rate = max(min_case_rate, init_case_rate - case_decel * day)\n            noise = np.random.normal(0, 0.01)\n            cases *= (1 + max(0.003, case_rate + noise))\n            cfr = cfr + cfr_speed * (cfr_target - cfr)\n            deaths = cases * cfr\n            deaths_by_day.append(deaths)\n    \n    elif model < 0.85:\n        # Model C: Sustained high growth (outbreak continues expanding rapidly)\n        init_rate = np.random.normal(0.085, 0.02)\n        decel = np.random.uniform(0.0, 0.002)\n        \n        deaths = float(current_deaths)\n        deaths_by_day = [deaths]\n        for day in range(1, 14):\n            rate = max(0.03, init_rate - decel * day)\n            noise = np.random.normal(0, 0.02)\n            deaths *= (1 + max(0.01, rate + noise))\n            deaths_by_day.append(deaths)\n    \n    else:\n        # Model D: Rapid deceleration (strong response effect)\n        init_rate = np.random.normal(0.065, 0.015)\n        decel = np.random.uniform(0.005, 0.01)\n        min_rate = np.random.uniform(0.005, 0.015)\n        \n        deaths = float(current_deaths)\n        deaths_by_day = [deaths]\n        for day in range(1, 14):\n            rate = max(min_rate, init_rate - decel * day)\n            noise = np.random.normal(0, 0.012)\n            deaths *= (1 + max(0.003, rate + noise))\n            deaths_by_day.append(deaths)\n    \n    # --- DON PUBLICATION SCHEDULE ---\n    # DON607 published June 13 (day -1 from our June 14 base)\n    # It's June 17 now (day 3) and no DON608 yet\n    # DON608: likely June 18-22 (day 4-8 from June 14)\n    # Skewing later since it hasn't come by June 17\n    don608_pub = np.random.choice([4, 5, 6, 7, 8], p=[0.15, 0.30, 0.30, 0.15, 0.10])\n    don608_cutoff = max(0, don608_pub - np.random.choice([2, 3], p=[0.5, 0.5]))\n    \n    # DON609: 5-8 days after DON608\n    don609_offset = np.random.choice([5, 6, 7, 8], p=[0.20, 0.35, 0.30, 0.15])\n    don609_pub = don608_pub + don609_offset\n    don609_cutoff = don609_pub - np.random.choice([2, 3], p=[0.5, 0.5])\n    \n    # June 27 = day 13 from June 14\n    resolution_idx = 13\n    \n    if don609_pub <= resolution_idx:\n        cutoff = min(max(0, don609_cutoff), 13)\n        reported = deaths_by_day[cutoff]\n        cutoff_dates.append(cutoff + 14)  # June day\n    elif don608_pub <= resolution_idx:\n        cutoff = min(max(0, don608_cutoff), 13)\n        reported = deaths_by_day[cutoff]\n        cutoff_dates.append(cutoff + 14)\n    else:\n        # Fallback to DON607\n        reported = 136\n        cutoff_dates.append(10)  # June 10\n    \n    results.append(int(round(reported)))\n\nresults = np.array(results)\nresults = np.maximum(results, 91)\n\nprint(f\"FINAL Monte Carlo simulation (N={N_SIM}):\")\nprint(f\"  Mean: {np.mean(results):.0f}\")\nprint(f\"  Median: {np.median(results):.0f}\")\nprint(f\"  Std Dev: {np.std(results):.0f}\")\n\npercentiles = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 98, 99]\npct_vals = {}\nprint(\"\\nPercentile distribution:\")\nfor p in percentiles:\n    val = np.percentile(results, p)\n    pct_vals[str(p)] = round(float(val))\n    print(f\"  P{p:2d}: {val:.0f}\")\n\nprint(f\"\\nP(DON607 fallback = 136): {np.mean(results == 136):.2%}\")\nprint(f\"P(result > 400): {np.mean(results > 400):.1%}\")\nprint(f\"P(result > 300): {np.mean(results > 300):.1%}\")\nprint(f\"P(result > 250): {np.mean(results > 250):.1%}\")\nprint(f\"P(result < 200): {np.mean(results < 200):.1%}\")\n\n# Data cutoff date distribution\ncutoff_dates = np.array(cutoff_dates)\nprint(f\"\\nData cutoff date distribution (June day):\")\nfor d in sorted(set(cutoff_dates)):\n    pct = np.mean(cutoff_dates == d) * 100\n    if pct > 0.5:\n        print(f\"  June {d}: {pct:.1f}%\")\n\n# What fraction get DON609?\ndon609_fraction = np.mean(cutoff_dates > 20)\ndon608_only = np.mean((cutoff_dates >= 14) & (cutoff_dates <= 20))\nprint(f\"\\nDON609 as latest: ~{don609_fraction*100:.1f}%\")\nprint(f\"DON608 as latest: ~{don608_only*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "FINAL Monte Carlo simulation (N=200000):\n  Mean: 307\n  Median: 290\n  Std Dev: 69\n\nPercentile distribution:\n  P 1: 214\n  P 2: 219\n  P 5: 227\n  P10: 236\n  P15:
244\n  P20: 250\n  P25: 257\n  P30: 263\n  P40: 276\n  P50: 290\n  P60: 307\n  P70: 327\n  P75: 340\n  P80: 355\n  P85: 373\n  P90: 399\n  P95: 441\n  P98: 495\n  P99: 536\n\nP(DON607 fallback = 136):
0.00%\nP(result > 400): 9.7%\nP(result > 300): 43.5%\nP(result > 250): 79.9%\nP(result < 200): 0.0%\n\nData cutoff date distribution (June day):\n  June 17: 2.2%\n  June 18: 5.6%\n  June 19: 7.4%\n
June 20: 5.5%\n  June 21: 7.1%\n  June 22: 16.2%\n  June 23: 22.8%\n  June 24: 22.8%\n  June 25: 10.4%\n\nDON609 as latest: ~79.3%\nDON608 as latest: ~20.7%\n", "stderr": "", "duration_ms": 6891}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Sensitivity analysis: What if growth is slower than I think?\n# Let me also check what the scenario-specific outputs look like\n\nimport numpy as np\nnp.random.seed(456)\n\n# Sensitivity 1: What if daily growth has already dropped to ~5%?\ndeaths = 192\nprint(\"Sensitivity: Low growth scenario (5%/day, decelerating to 2%)\")\nfor day in range(1, 14):\n    rate = max(0.02, 0.05 - 0.003 * day)\n    deaths *= (1 + rate)\n    d_day = 14 + day\n    print(f\"  June {d_day}: {deaths:.0f} (rate={rate:.1%})\")\n\nprint()\n\n# Sensitivity 2: What if growth stays high at ~8%?\ndeaths = 192\nprint(\"Sensitivity: High growth scenario (8%/day, slow deceleration)\")\nfor day in range(1, 14):\n    rate = max(0.04, 0.08 - 0.002 * day)\n    deaths *= (1 + rate)\n    d_day = 14 + day\n    print(f\"  June {d_day}: {deaths:.0f} (rate={rate:.1%})\")\n\nprint()\n\n# Sensitivity 3: Linear growth at 14 deaths/day (recent absolute rate)\ndeaths = 192\nprint(\"Sensitivity: Linear growth (14 deaths/day)\")\nfor day in range(1, 14):\n    deaths += 14\n    d_day = 14 + day\n    print(f\"  June {d_day}: {deaths:.0f}\")\n\nprint()\n# Key cutoff dates:\n# If DON608 data cutoff ~June 18 (day 4): \n#   Low: ~232, Mid: ~259, High: ~254, Linear: ~248\n# If DON609 data cutoff ~June 23 (day 9):\n#   Low: ~280, Mid: ~342, High: ~363, Linear: ~318\n# If DON609 data cutoff ~June 25 (day 11):\n#   Low: ~302, Mid: ~391, High: ~413, Linear: ~346\n\nprint(\"\\nSummary at key cutoff dates:\")\nprint(f\"{'Scenario':<15} {'June 18':<10} {'June 23':<10} {'June 25':<10}\")\nfor name, init_rate, decel, min_r in [\n    (\"Low (5%)\", 0.05, 0.003, 0.02),\n    (\"Mid (7%)\", 0.07, 0.003, 0.025),\n    (\"High (8%)\", 0.08, 0.002, 0.04),\n]:\n    vals = {}\n    deaths = 192.0\n    for day in range(1, 14):\n        rate = max(min_r, init_rate - decel * day)\n        deaths *= (1 + rate)\n        d_day = 14 + day\n        vals[d_day] = deaths\n    print(f\"{name:<15} {vals[18]:<10.0f} {vals[23]:<10.0f} {vals[25]:<10.0f}\")\n\nprint(f\"{'Linear (14/d)':<15} {192+14*4:<10.0f} {192+14*9:<10.0f} {192+14*11:<10.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Sensitivity: Low growth scenario (5%/day, decelerating to 2%)\n  June 15: 201 (rate=4.7%)\n  June 16: 210 (rate=4.4%)\n  June 17: 218 (rate=4.1%)\n  June 18: 227
(rate=3.8%)\n  June 19: 235 (rate=3.5%)\n  June 20: 242 (rate=3.2%)\n  June 21: 249 (rate=2.9%)\n  June 22: 256 (rate=2.6%)\n  June 23: 262 (rate=2.3%)\n  June 24: 267 (rate=2.0%)\n  June 25: 272
(rate=2.0%)\n  June 26: 278 (rate=2.0%)\n  June 27: 283 (rate=2.0%)\n\nSensitivity: High growth scenario (8%/day, slow deceleration)\n  June 15: 207 (rate=7.8%)\n  June 16: 223 (rate=7.6%)\n  June 17:
239 (rate=7.4%)\n  June 18: 256 (rate=7.2%)\n  June 19: 274 (rate=7.0%)\n  June 20: 293 (rate=6.8%)\n  June 21: 312 (rate=6.6%)\n  June 22: 332 (rate=6.4%)\n  June 23: 353 (rate=6.2%)\n  June 24: 374
(rate=6.0%)\n  June 25: 396 (rate=5.8%)\n  June 26: 418 (rate=5.6%)\n  June 27: 441 (rate=5.4%)\n\nSensitivity: Linear growth (14 deaths/day)\n  June 15: 206\n  June 16: 220\n  June 17: 234\n  June
18: 248\n  June 19: 262\n  June 20: 276\n  June 21: 290\n  June 22: 304\n  June 23: 318\n  June 24: 332\n  June 25: 346\n  June 26: 360\n  June 27: 374\n\n\nSummary at key cutoff dates:\nScenario
June 18    June 23    June 25   \nLow (5%)        227        262        272       \nMid (7%)        245        311        335       \nHigh (8%)       256        353        396       \nLinear (14/d)
248        318        346       \n", "stderr": "", "duration_ms": 0}
```

## 💬 Response

Good. My simulation results look well-calibrated. Let me now run the reflection.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Outbreak actively growing with no vaccine/treatment - deaths were 91 on June 6 and 192 on June 14 (doubling in 8 days). No licensed countermeasure for BDBV means outbreak will continue.",
      "supports": {
        "center": 320,
        "low": 260,
        "high": 420
      },
      "logit": 1.5,
      "confidence": 0.9
    },
    {
      "description": "Case growth rate already decelerating from ~7%/day to ~4.5%/day (June 6-14). Death growth will follow case deceleration with lag. International response scaling up (IASC, $518M response plan).",
      "supports": {
        "center": 275,
        "low": 240,
        "high": 320
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "DON publication timing uncertainty: most likely 2 more DONs before June 27 (DON608 ~June 18-20, DON609 ~June 24-27), but the data cutoff is 2-3 days before publication. If only DON608 qualifies, deaths much lower (~230-260) vs DON609 (~290-400).",
      "supports": {
        "center": 290,
        "low": 230,
        "high": 400
      },
      "logit": 0.8,
      "confidence": 0.6
    },
    {
      "description": "Response struggling: MSF says outbreak 'outpacing response', Oxfam says scale likely underestimated, conflict environment, poor water/sanitation, low contact tracing rate (72%). These factors suggest death growth remains high.",
      "supports": {
        "center": 340,
        "low": 280,
        "high": 450
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Rising CFR from 17.7% to 23.8% over June 6-14 increases deaths even if case growth slows. CFR likely stabilizes around 25-27%.",
      "supports": {
        "center": 310,
        "low": 270,
        "high": 370
      },
      "logit": 0.5,
      "confidence": 0.8
    }
  ],
  "tentative_estimate": {
    "center": 290,
    "low": 236,
    "high": 399
  },
  "assessment": "This is a rapidly growing Ebola outbreak with no vaccine/treatment. The question resolves to the confirmed DRC death count in the latest WHO DON published by June 27. The latest DON (DON607, June 13) reported 136 deaths as of June 10. MoH data as of June 14 shows 192 deaths. We expect 1-2 more DONs before the deadline.\n\nThe key tension is between:\n1. Continued rapid death growth (~8-9%/day exponential) which would push deaths to 300-400+ by the DON609 data cutoff\n2. Evidence that case growth is already decelerating (from 7% to 4.5%/day), which death growth will follow with a lag\n3. DON publication timing: ~80% chance DON609 qualifies (data cutoff ~June 22-25), ~20% chance only DON608 (cutoff ~June 16-18)\n\nMonte Carlo simulation (200K runs) mixing multiple growth models gives median ~290, with P10=236 and P90=399. The distribution is right-skewed reflecting the possibility of sustained high growth.",
  "tool_audit": "research() - Excellent, returned comprehensive outbreak data with timeline and sources. web_search - Useful for finding latest DON and ECDC data. fetch_url - Successfully extracted key data from WHO DON607 and ECDC pages. execute_code - Essential for Monte Carlo simulation and growth analysis.",
  "process_reflection": "The research tool worked well for this outbreak question, pulling from ReliefWeb and WHO sources systematically. The main friction was inability to directly check the WHO DON listing page (it returned only introductory text). The Monte Carlo framework handles the compound uncertainty (growth rate \u00d7 DON timing \u00d7 data cutoff) well. A dedicated epidemic modeling tool would help - something that could fit SIR/SEIR models to case data automatically.",
  "anchor": "No strong prior anchor for this specific question type. Starting from the trajectory extrapolation: deaths doubling roughly every 7-8 days from 192 on June 14 would give ~384 by June 22, but deceleration is expected.",
  "key_uncertainties": "1. DON publication timing and data cutoff dates are the largest source of uncertainty\n2. Whether death growth rate has already started declining (lagging the observed case deceleration)\n3. Potential for response to dramatically slow transmission vs outbreak overwhelming response capacity",
  "calibration_notes": "The lower bound of 91 is the fallback to DON607 if no new DON is published, which is extremely unlikely given the PHEIC status and weekly DON pattern. The simulation gives essentially 0% probability of this. Distribution seems well-calibrated: P10=236 corresponds to a scenario where only DON608 qualifies with a June 16-17 cutoff, P90=399 corresponds to DON609 with sustained high growth."
}
```

### 📋 Result

```
{"factor_count": 5, "factor_sum": 3.63, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Outbreak actively growing with no vaccine/treatment - deaths were 91 on June 6 and 192 on June
14 (doubling in 8 days). No licensed countermeasure for BDBV means outbreak will continue.", "supports": {"center": 320.0, "low": 260.0, "high": 420.0}, "logit": 1.5, "confidence": 0.9,
"effective_logit": 1.35}, {"description": "Case growth rate already decelerating from ~7%/day to ~4.5%/day (June 6-14). Death growth will follow case deceleration with lag. International response
scaling up (IASC, $518M response plan).", "supports": {"center": 275.0, "low": 240.0, "high": 320.0}, "logit": 1.0, "confidence": 0.7, "effective_logit": 0.7}, {"description": "DON publication timing
uncertainty: most likely 2 more DONs before June 27 (DON608 ~June 18-20, DON609 ~June 24-27), but the data cutoff is 2-3 days before publication. If only DON608 qualifies, deaths much lower (~230-260)
vs DON609 (~290-400).", "supports": {"center": 290.0, "low": 230.0, "high": 400.0}, "logit": 0.8, "confidence": 0.6, "effective_logit": 0.48}, {"description": "Response struggling: MSF says outbreak
'outpacing response', Oxfam says scale likely underestimated, conflict environment, poor water/sanitation, low contact tracing rate (72%). These factors suggest death growth remains high.",
"supports": {"center": 340.0, "low": 280.0, "high": 450.0}, "logit": 1.0, "confidence": 0.7, "effective_logit": 0.7}, {"description": "Rising CFR from 17.7% to 23.8% over June 6-14 increases deaths
even if case growth slows. CFR likely stabilizes around 25-27%.", "supports": {"center": 310.0, "low": 270.0, "high": 370.0}, "logit": 0.5, "confidence": 0.8, "effective_logit": 0.4}],
"dominant_factor": "Outbreak actively growing with no vaccine/treatment - deaths were 91 on June 6 and 192 on June 14 (doubling in 8 days). No licensed countermeasure for BDBV means outbreak will
continue.", "dominant_effective_logit": 1.35, "distribution_metrics": {"implied_median": 310.1101928374656, "implied_p10": 257.1349862258953, "implied_p90": 398.34710743801656, "median_gap":
-20.110192837465604, "median_gap_pct": -14.241123683183792, "spread_ratio": 1.154291845493562, "precision": 0.5620689655172414}, "sources": ["[(Metaculus) How many confirmed Ebola (Bundibugyo virus)
deaths will the WHO report in the DRC as of its latest update near June 28, 2026?](https://www.metaculus.com/questions/44088)", "[2026 Central Africa Ebola
epidemic](https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic)", "[2026 Ebola epidemic - Wikipedia](https://en.wikipedia.org/wiki/2026_Ebola_epidemic)", "[Ebola disease caused by
Bundibugyo virus, Democratic Republic of the Congo & Uganda](https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON607)", "[Ebola disease outbreak in the Democratic Republic of the Congo
and Uganda](https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda)", "[Disease Outbreak News](https://www.who.int/emergencies/disease-outbreak-news)"]}
```

## 💬 Response

The reflection shows my tentative center (290) is about 7% below the factor-implied median (310), and my spread ratio is 1.15 (slightly wider than factor-implied). This seems reasonable - the factor-implied median might be slightly high because I'm weighting the DON timing uncertainty carefully. Let me now run the premortem.

## 🔧 Tool: mcp__premortem__premortem


```json
{
  "counterargument": "The strongest case against my median of ~290 is that the growth rate may already be substantially lower than my model assumes. The most recent daily data point (June 13\u219214) showed only 6.1% daily death growth, and case growth has already decelerated to ~4.5%/day. If deaths follow cases with only a short lag, the actual daily death growth by mid-June could be ~4-5%, not the 7-9% I'm centered on. With 4% daily growth from 192 on June 14, deaths would be only ~233 by June 18 and ~283 by June 23. If DON608's data cutoff is June 16-17 and DON609's is June 22-23, the reported figure could be closer to 250-280, not 290-320.\n\nAdditionally, my DON609 timing model may be overconfident about a second DON qualifying before June 27. If WHO shifts to slightly longer intervals (8-10 days between DONs rather than 5-7), DON609 might not be published until June 27-28, potentially falling outside the window. In that scenario, only DON608 would qualify with a lower data cutoff, resolving closer to 230-260.\n\nThe case growth deceleration is an empirical fact, not speculation, and deaths will eventually track it. My model may be systematically biased upward by anchoring too heavily on the June 6-14 death growth rate rather than the leading indicator of case growth deceleration.",
  "what_would_change_my_mind": "1. If a DON608 is published in the next 1-2 days with specific death figures, that would directly anchor my projection - if it shows e.g. 220 deaths as of June 16, I would revise down toward 260-280 median.\n2. If DRC MoH daily sitreps show daily new deaths dropping below 10 (vs the recent 11-15/day average), that would shift me down ~15-20pp on P(>300).\n3. If a DON609 is published by June 24 showing 350+ deaths, that would shift me up by 30+ on the median.\n4. If the outbreak spreads to new provinces (e.g., Tshopo, Haut-Uele) causing a step increase in new cases, that could push the high tail up to 500+.\n5. If WHO switches to a different publication cadence (e.g., weekly situation reports replacing DONs), the resolution source could change the figure reported.",
  "confidence_in_estimate": 0.4
}
```

### 📋 Result

```
{"verdict": "approve", "assessment": "## Verification Summary\n\n**Hallucinated evidence:** None found. All key factual claims in the 5 factors are grounded in the research trace:\n- Factor 1: Deaths
91 (June 6) and 192 (June 14) confirmed via WHO DON607 and ECDC/MoH data in trace. No licensed countermeasure for BDBV confirmed in question background and multiple trace sources.\n- Factor 2: Case
growth deceleration from ~7%/day to ~4.5%/day confirmed by agent's own computation in trace (June 6-10: 7.0%/day, June 10-14: 4.6%/day). $518M response plan confirmed via Africa CDC/WHO joint plan in
search results.\n- Factor 3: DON publication timing model based on documented DON602 (May 17), DON605 (May 29), DON606 (June 8), DON607 (June 13) pattern from trace. Simulation correctly shows ~79%
DON609 qualifying, ~21% DON608 only.\n- Factor 4: MSF \"outpacing response\" quote, Oxfam \"underestimated\" claim, and 72% contact tracing rate all confirmed by ReliefWeb sources in trace and
worldview research entry.\n- Factor 5: CFR progression from 17.7% (DON606/June 6) to 20.1% (DON607/June 10) to 23.8% (192/808, June 14) confirmed in trace.\n\n**Double-counting:** Minor overlap
between Factor 1 (growth trajectory) and Factor 4 (response quality), as both push toward higher death estimates. However, they draw on distinct evidence \u2014 Factor 1 uses quantitative growth data
while Factor 4 uses qualitative response assessments from different organizations. Not materially problematic for a numeric forecast.\n\n**Wrong-direction factors:** None. All factor logits are
positive and all central estimates (275-340) are above the current known death count (192), which is directionally correct for projecting forward.\n\n**Contradictory assessment:** No. The assessment's
center of 290 is consistent with the factor-implied average (~307) and the Monte Carlo simulation median (290).\n\n**Resolution criteria alignment:** Excellent. The agent correctly identified that
resolution depends on the DRC confirmed-death figure in the latest WHO DON published on or before June 27, modeled DON publication timing probabilistically, and accounted for the data cutoff lag (2-3
days before publication).\n\n**Counterargument quality:** Strong. The counterargument identifies specific evidence (case growth deceleration as a leading indicator, DON609 timing uncertainty) and
constructs a coherent alternative scenario that would yield a lower median (~250-280). This is a genuine challenge to the forecast, not a token gesture.\n\n**Confidence calibration:** The 0.40
confidence is appropriate given dual sources of uncertainty (growth trajectory AND DON publication timing). No overconfidence issue.\n\n**Probability assessment:** The center of 290 with range 236-399
appears well-calibrated. The agent ran 200K Monte Carlo simulations mixing four growth models (moderate deceleration 35%, case-based 30%, sustained high growth 20%, rapid deceleration 15%), validated
against known data points, and produced results that are internally consistent. The sensitivity analysis further confirms the range is reasonable across different growth assumptions and DON cutoff
dates.\n\n**Tool audit:** No discrepancies between the narrative tool audit and actual tool metrics. All tools reported 0% error rates, consistent with the agent's characterization."}
```

## 💬 Response

Approved. Let me now produce the final structured output.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "This question asks for the cumulative confirmed DRC Ebola deaths in the latest WHO DON published by June 27, 2026. The most recent DON (DON607, June 13) reported 136 deaths as of June 10. MoH data as of June 14 shows 192 deaths with 808 confirmed cases. Death growth has been ~9%/day (June 10-14) though case growth is already decelerating from ~7% to ~4.5%/day. No vaccine or treatment exists for Bundibugyo virus.\n\nThe resolution hinges on (1) how many more DONs are published before June 27 and their data cutoff dates, and (2) the death trajectory. Monte Carlo simulation (200K runs) mixing exponential decay, case-based CFR, and sustained growth models, combined with probabilistic DON timing, gives a median of ~290. About 80% of simulations have DON609 qualifying (data cutoff ~June 22-25), while ~20% have only DON608 (cutoff ~June 16-18). The distribution is moderately right-skewed reflecting tail risk from sustained rapid growth in a response-overwhelmed setting.",
  "anchor": "No direct base rate. Trajectory extrapolation from 192 deaths (June 14) with ~7.5-day doubling time suggests ~384 by June 22, but deceleration expected. Anchoring on simulation output.",
  "factors": [
    {
      "description": "Outbreak actively growing with no vaccine/treatment - deaths doubled from 91 to 192 in 8 days (June 6-14). No licensed countermeasure for BDBV means outbreak continues.",
      "supports": {
        "center": 320,
        "low": 260,
        "high": 420
      },
      "logit": 1.5,
      "confidence": 0.9
    },
    {
      "description": "Case growth rate already decelerating from ~7%/day to ~4.5%/day (June 6-14). Death growth will follow case deceleration with a lag. International response scaling up (IASC activation, $518M response plan).",
      "supports": {
        "center": 275,
        "low": 240,
        "high": 320
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "DON publication timing uncertainty: ~80% chance DON609 qualifies (data cutoff ~June 22-25, deaths ~290-400), ~20% chance only DON608 (cutoff ~June 16-18, deaths ~230-260). This is the primary source of bimodality.",
      "supports": {
        "center": 290,
        "low": 230,
        "high": 400
      },
      "logit": 0.8,
      "confidence": 0.6
    },
    {
      "description": "Response struggling: MSF says outbreak 'outpacing response', Oxfam says scale likely underestimated, 72% contact tracing rate, conflict environment. Supports sustained higher growth.",
      "supports": {
        "center": 340,
        "low": 280,
        "high": 450
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Rising CFR from 17.7% to 23.8% (June 6-14) increases deaths even if case growth slows. CFR likely stabilizes around 25-27%.",
      "supports": {
        "center": 310,
        "low": 270,
        "high": 370
      },
      "logit": 0.5,
      "confidence": 0.8
    }
  ],
  "percentile_values": {
    "1": 214,
    "2": 219,
    "5": 227,
    "10": 236,
    "15": 244,
    "20": 250,
    "25": 257,
    "30": 263,
    "40": 276,
    "50": 290,
    "60": 307,
    "70": 327,
    "75": 340,
    "80": 355,
    "85": 373,
    "90": 399,
    "95": 441,
    "98": 495,
    "99": 536
  }
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

## Forecast Summary

**Question:** How many confirmed Ebola (Bundibugyo virus) deaths will the WHO report in the DRC as of its latest update near June 28, 2026?

**Median estimate: 290 confirmed deaths**

### Key Distribution Points
| Percentile | Deaths |
|-----------|--------|
| P10 | 236 |
| P25 | 257 |
| P50 (median) | 290 |
| P75 | 340 |
| P90 | 399 |

### Key Reasoning

1. **Current trajectory:** Deaths doubled from 91 (June 6) to 192 (June 14) — an 8-day doubling time with no licensed vaccine or treatment available for Bundibugyo virus.

2. **Growth deceleration signal:** Case growth has already slowed from ~7%/day to ~4.5%/day, and death growth should follow with a lag, suggesting the exponential phase is beginning to moderate.

3. **DON timing is the biggest uncertainty:** The resolution depends on which WHO DON is the latest published by June 27. ~80% of simulations have DON609 qualifying (data cutoff ~June 22-25, higher death counts), while ~20% have only DON608 (cutoff ~June 16-18, lower counts).

4. **Response challenges persist:** No vaccine/treatment, conflict environment, low contact tracing rates (72%), and organizations reporting the outbreak is "outpacing the response."

5. **Monte Carlo simulation** mixed 4 growth models (exponential with deceleration, case-based with CFR, sustained high growth, rapid response) across 200K runs with probabilistic DON timing to produce the final distribution.
