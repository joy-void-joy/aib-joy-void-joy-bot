# Reasoning Log: Will the World Health Organization classify an Iran health event before May 1, 2026?

*Generated: 2026-04-03T07:44:21.832792+00:00*


## 💭 Thinking

Let me analyze this forecasting question carefully.

## Step 1: Parse the Resolution Criteria

**What must happen for YES?** WHO's public emergency dashboard at https://extranet.who.int/publicemergency must report a health event in Iran before May 1, 2026.

**Resolution source:** WHO's public emergency dashboard at the specific URL.

**Deadline:** May 1, 2026.

**Key observations:**
- Published: April 3, 2026 at 07:30 UTC
- Scheduled close: April 3, 2026 at 09:00 UTC (only 1.5 hours after publication!)


- Scheduled resolve: May 1, 2026

The forecasting window closes almost immediately, but resolution happens nearly a month later. The critical issue is whether the WHO dashboard currently displays an Iranian health event or will show one by the deadline. I need to check the fine print since there's ambiguity about whether this covers events that already occurred or only future ones—the question doesn't specify a clear start date, so I need to determine if "before May 1, 2026" includes events from any point in time or just from publication onward.

## 💬 Response

I'll analyze this question systematically. Let me start by understanding the resolution criteria and researching the WHO dashboard and Iran health events.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43046
  ]
}
```

### 📋 Result

```
{"post_id": 43046, "title": "Will the World Health Organization classify an Iran health event before May 1, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43046",
"background_info": "This question tracks whether WHO reports a health event in Iran on its public emergency
dashboard.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"672f4d855ec2365c\",\"sheet_id\":501.1}}`", "resolution_criteria": "This question resolves to yes if WHO's public
emergency dashboard at https://extranet.who.int/publicemergency reports an event in Iran before May 1, 2026. Otherwise, this question resolves to no.", "fine_print": "", "num_forecasters": 3,
"community_prediction": null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://extranet.who.int/publicemergency",
  "prompt": "List all health events currently displayed on this dashboard. Is there any event related to Iran?"
}
```

### 📋 Result

```
{"url": "https://extranet.who.int/publicemergency", "content": "Based on the content provided, **I cannot list any specific health events** because the text you shared contains only the disclaimer and
general information about the WHO Health Emergency Dashboard - not the actual dashboard data itself.\n\nThe content explains:\n- The dashboard displays a subset of public health events reported
through official IHR (2005) channels\n- Data is refreshed every 30 minutes\n- It is not comprehensive of all events WHO is aware of\n\n**Regarding Iran:** There is no mention of Iran or any specific
country's health events in the provided text.\n\nTo see actual current health events (including any related to Iran), you would need to access the interactive dashboard itself at the URL, not just
read the disclaimer text.\n\n---\n\n**Relevant links:**\n- [HeRAMS platform](https://herams.org/) - Health Resources and Services Availability Monitoring System\n- [HeRAMS account
request](https://herams.org/user/request-account) - To access individual projects", "title": "WHO Health Emergency Dashboard"}
```

```json
{
  "query": "WHO public emergency dashboard Iran health event 2026"
}
```

### 📋 Result

```
{"query": "WHO public emergency dashboard Iran health event 2026", "results": [{"title": "WHO Health Emergency Dashboard - Extranet Systems", "url": "https://extranet.who.int/publicemergency/",
"snippet": "The World Health Organization (WHO) Health Emergency Dashboard is a platform which aims to share information about public health events and emergencies. The data on the dashboard is
refreshed every thirty (30) minutes and data is accurate as at time of refreshing.\nThe WHO Health Emergency Dashboard is not a comprehensive representation of all the events and emergencies that WHO
is aware of and responding to. The events displayed are a subset of those reported through official channels as mandate", "api_data": null, "hint": null}, {"title": "WHO in Islamic Republic of Iran",
"url": "https://www.emro.who.int/iran/news/", "snippet": "WHO in Islamic Republic of Iran\n[A global model for mental health: How the Iranian integrated care system is saving
lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-saving-lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet
transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists, physicians, psychologists, dedicated social workers, and community voluntee",
"api_data": null, "hint": null}, {"title": "Conflict deepens health crisis across Middle East, WHO says", "url": "https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-
east--who-says", "snippet": "More than ten days into the latest escalation of conflict in the Middle East, health systems across the Region are coming under strain as injuries and displacement rise,
attacks on health care continue, and public health risks increase.\nNational health authorities in Iran report more than 1300 deaths and 9000 injuries, and in Lebanon report at least 570 deaths and
more than 1400 injuries. In Israel, authorities report 15 deaths and 2142 injuries.\nAt the same time, the conflict is affecting the v", "api_data": null, "hint": null}, {"title": "Health impact of
the escalation of conflict in the Middle East", "url": "https://www.who.int/news-room/feature-stories/detail/health-impact-of-the-escalation-of-conflict-in-the-middle-east", "snippet": "NOTE: In his
introductory remarks at the media briefing on 5 March 2026, the Director-General said that an estimated 100 000 people have left Iran. The text below has been corrected to show that an estimated 100
000 people have left the city of Tehran, not Iran.\n________________________\nWHO is concerned over the expansion of the conflict in the Middle East which is putting health systems and lives at risk
in the region and beyond.\nAt a press conference earlier today, Dr Tedros Adhanom Ghebreyesu", "api_data": null, "hint": null}, {"title": "News | Iran site - WHO EMRO", "url":
"https://www.emro.who.int/iran/news/index.html", "snippet": "WHO in Islamic Republic of Iran\n[A global model for mental health: How the Iranian integrated care system is saving
lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-saving-lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet
transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists, physicians, psychologists, dedicated social workers, and community voluntee",
"api_data": null, "hint": null}, {"title": "Assessing Iran\u2019s health system according to the COVID-19 strategic preparedness and response plan of the World Health Organization: health policy and
historical implications - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7888405/", "snippet": "Summary\nBackground\nThe role of health systems in the management of disasters, including
natural hazards like outbreaks and pandemics, is crucial and vital. Healthcare systems which are unprepared to properly deal with crises are much more likely to expose their public health workers and
health personnel to harm and will not be able to deliver healthcare provisions in critical situations. This can lead to a drammatic toll of deaths, even in developed countries. The possible occurrence
of global c", "api_data": null, "hint": null}, {"title": "Islamic Republic of Iran Country Overview | World Health Organization", "url": "https://www.who.int/countries/irn", "snippet": "![Country
presence banner Country presence banner](https://cdn.who.int/media/images/default-source/cover-images/decorative-images/who-cpr-2025-cp-banner.png?sfvrsn=730ecc69_5)\nNews and features\nCountry
profiles\nHealth profiles\nCountry profiles present selected data, statistics and information to provide national health profiles at given points in time.\nPublications\n2 July 2024\nSurveillance and
control of Anopheles stephensi\nAnopheles stephensi is an invasive mosquito species which has been found", "api_data": null, "hint": null}, {"title": "World Health Organization Prepares for Nuclear
Scenario, Including Weapons Use, in Iran \u2014 UNITED24 Media", "url": "https://united24media.com/latest-news/world-health-organization-prepares-for-nuclear-scenario-including-weapons-use-in-
iran-16995", "snippet": "Illustrative image showing a nuclear explosion diagram overlaid with the WHO emblem. (Source: UNITED24 Media/Oleksandr Manukians)\nThe World Health Organization (WHO) is
preparing for the possibility of a nuclear-related incident as tensions continue to escalate in the Middle East, including scenarios involving strikes on nuclear facilities or the potential use of
nuclear weapons.\nWe bring you stories from the ground. Your support keeps our team in the field.\nAccording to Politico on March 18, WH", "api_data": null, "hint": null}, {"title": "WHO EMRO -
Islamic Republic of Iran", "url": "https://www.emro.who.int/countries/iran/home.html", "snippet": "WHO Representative for Islamic Republic of Iran\nDr Awad Mataria\nWHO Representative\nPO Box
14665-1565\nTehran\n11516\nemail:\n[{{{type}}}] {{{reason}}}\n{{/data.error.root_cause}}\n{{texts.summary}}\n{{#options.result.rssIcon}}\n[RSS](https://www.emro.who.int/{{{data.rssUrl}}})\n{{/options.
result.rssIcon}}\n{{{_source.displayDate}}}\n{{/_source.showDate}}{{{_source.description}}}\n{{#_source.additionalInfo}}{{#_source.additionalFields}} {{#title}} {{{label}}}: {{{title}}} {{/title}}
{{/_source.additionalFiel", "api_data": null, "hint": null}, {"title": "2026 Iran massacres - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Iran_massacres", "snippet": "Since the beginning of
the 2025\u20132026 Iranian protests, the government of Iran has perpetrated widespread massacres of civilians, deploying both its own security forces and also imported foreign militias to suppress
widespread public dissent across the country. As of 25 January 2026, the total death toll estimates ranged from 7,007 people to upwards of ~36,500 people, including 209 government-affiliated military
and non-military personnel, making these among the largest massacres in the modern hi", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Iran massacres\", \"url\":
\"https://en.wikipedia.org/wiki/2026_Iran_massacres\", \"extract\": \"Since the beginning of the 2025\\u20132026 Iranian protests, the government of Iran has perpetrated widespread massacres of
civilians, deploying both its own security forces and also imported foreign militias to suppress widespread public dissent across the country. As of 25 January 2026, the total death toll estimates
ranged from 7,007 people to upwards of ~36,500 people, including 209 government-affiliated military and non-military personnel, making these among the largest massacres in the modern history of
Iran.\\nIranian authorities have supposedly imposed a near-total internet shutdown as part of their crackdown on the protests, restricting communication inside the country and limiting the flow of
information about the killings to the outside world. On 12 January 2026, Esmaeil Baghayi, the spokesperson for the Iranian Ministry of Foreign Affairs, confirmed that security forces had directly shot
at protesters.\\nOn 25 January, Time reported that a specific list included 30,304 protest-related deaths registered in civilian hospitals for 8 and 9 January alone. The same day, Iran International
estimated the total number of deaths at ~36,500. On 28 January, The Guardian reported that the death toll could be more than 30,000, and that less than 10% of deaths may have been officially
registered. AP News reported that the government's overwhelming use of violence had caused despair among the Iranian public and had given rise to hopes among some citizens for an American attack.
Several scholars have argued that the Iranian government now faces a fragile state that could lead to its demise.\\nAli Larijani, the secretary of the Supreme National Security Council, has been
described as the mastermind of the massacres, according to former Iranian government officials, while the crackdown was initiated in pursuit of orders from Supreme Leader Ali Khamenei and senior
officials to use live fire on protesters; Khamenei himself had ordered \\\"to crush the protests by any means necessary\\\". As of 19 January 2026, the Iranian government had reasserted control over
the protests. Worldwide support protests took place on 14 February, and protest waves restarted in western Iran on 16 February and in universities on 21 February.\\nKhamenei acknowledged that
\\\"thousands of people\\\" had been killed during the protests, blaming American president Donald Trump for the massacre and calling all protesters \\\"rioters and terrorists\\\" affiliated with the
United States and Israel. The Iranian government put the death toll at 3,117, stating that 2,447 were civilians and security forces, and the rest were \\\"terrorists\\\". The government published an
official list of 2,986 victims. Human Rights Activists in Iran (HRANA) described the official list as mostly unverifiable due to the lack of sufficient identifying details. Iran International stated
on 3 February that it had its own confirmed list of 6,634 deaths, of which less than 100 were on the official list. HRANA published a full report on 23 February 2026, including a detailed named list
of 7,007 deaths.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

## 💬 Response

This is very informative. There's a major conflict in Iran with significant health implications. Let me get more details on the WHO dashboard and the current situation.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-east--who-says",
  "prompt": "What specific health events or emergencies has WHO classified in Iran? What does WHO report about Iran's health situation? Is there mention of the WHO Health Emergency Dashboard listing Iran?"
}
```

### 📋 Result

```
{"url": "https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-east--who-says", "content": "Based on the content provided:\n\n**WHO has NOT classified any specific
health events or emergencies in Iran** in this document. The article does not mention WHO classifying or declaring a health emergency in Iran.\n\n**What WHO reports about Iran's health situation:**\n-
More than 1,300 deaths and 9,000 injuries from the conflict (as reported by Iranian national health authorities)\n- WHO has verified 18 attacks on health care facilities since February 28, resulting
in 8 deaths among health workers\n- Over 100,000 people have been internally displaced due to insecurity\n- Petroleum fires and smoke from damaged infrastructure have exposed communities to toxic
pollutants, causing breathing problems, eye and skin irritation, and potentially contaminating water and food sources\n\n**Regarding the WHO Health Emergency Dashboard:**\nThere is **no mention** of
the WHO Health Emergency Dashboard listing Iran in this content.\n\nThe article focuses on the humanitarian and health impacts of the ongoing conflict rather than formal WHO emergency
classifications.\n\n---\n\n**Relevant links:**\nThe provided content does not contain any embedded hyperlinks to additional resources.", "title": "Conflict deepens health crisis across Middle East,
WHO says"}
```

```json
{
  "url": "https://www.who.int/news-room/feature-stories/detail/health-impact-of-the-escalation-of-conflict-in-the-middle-east",
  "prompt": "What is WHO reporting about the health impact in Iran? Has WHO classified this as a health emergency? What events are described?"
}
```

### 📋 Result

```
{"url": "https://www.who.int/news-room/feature-stories/detail/health-impact-of-the-escalation-of-conflict-in-the-middle-east", "content": "Based on the content provided, here is what WHO is
reporting:\n\n## Health Impact in Iran\n\n**Casualties and Attacks:**\n- Almost 1,000 deaths reported in Iran\n- WHO has verified 13 attacks on health care facilities in Iran\n- The conflict is part
of a broader Middle East crisis affecting 16 countries\n\n**Displacement:**\n- An estimated 100,000 people have left the city of Tehran\n\n**Specific Concerns:**\n- The threat of nuclear facilities
being impacted, which could have serious public health consequences\n- Under international humanitarian law, health care must be protected and not attacked\n\n## Emergency Classification\n\nThe
content does **not explicitly state** that WHO has classified this as a formal \"health emergency.\" However, WHO expresses being \"deeply concerned\" and is actively monitoring and responding to the
situation.\n\n## Events Described\n\n- Escalation of conflict in the Middle East involving 16 countries (as of March 5, 2026)\n- Deaths reported across multiple countries: Iran (~1,000), Lebanon (50),
Israel (13), other Gulf countries (11)\n- Displacement in Tehran and Lebanon (60,000+ displaced, potentially 1 million may move)\n- WHO's Logistics Hub in Dubai suspended operations due to
insecurity\n- Supply chain disruptions affecting $18 million in humanitarian health supplies and blocking emergency requests from 25 countries\n- Critical supplies for Gaza ($6 million in medicines)
and polio laboratory supplies ($1.6 million) are held up\n\n---\n\n**Relevant links:**\n\nThe provided content does not contain any embedded links to additional resources.", "title": "Health impact of
the escalation of conflict in the Middle East"}
```

```json
{
  "query": "WHO \"public emergency\" dashboard Iran event classified 2026 site:who.int"
}
```

### 📋 Result

```
{"query": "WHO \"public emergency\" dashboard Iran event classified 2026 site:who.int", "results": [{"title": "News", "url": "https://www.who.int/news", "snippet": "News\nBrowse selected WHO news
below.\n30 March 2026\nJoint external evaluation of the International Health Regulations (2005) core capacities of Vanuatu\nDuring the JEE mission, which took place in Port Vila from 16 to 20 June
2025, Vanuatu\u2019s capacities in 19 technical areas were evaluated through...\n26 March 2026\nWorld report on promoting the health of refugees and migrants: Monitoring progress on the WHO
global...\nThe World report on promoting the health of refugees and migrants: Monitoring progr", "api_data": null, "hint": null}, {"title": "WHO EMRO | WHO Health Emergencies Programme | Priority
areas | Iran site", "url": "https://www.emro.who.int/iran/priority-areas/who-health-emergency.html", "snippet": "Who we are\nWHE works closely with the Ministry of Health and Medical Education and
other national and international health partners to build and improve IHR capacities required for preparedness and detection and ensure a rapid and effective response to natural and public health
emergencies to decrease their impact.\nThe WHO country office is the technical lead in public health and the COVID-19 response, as it coordinates and collaborates with a wide range of national and
international health part", "api_data": null, "hint": null}, {"title": "WHO EMRO - Islamic Republic of Iran", "url": "https://www.emro.who.int/countries/iran/home.html", "snippet": "WHO Representative
for Islamic Republic of Iran\nDr Awad Mataria\nWHO Representative\nPO Box 14665-1565\nTehran\n11516\nemail:\n[{{{type}}}] {{{reason}}}\n{{/data.error.root_cause}}\n{{texts.summary}}\n{{#options.result
.rssIcon}}\n[RSS](https://www.emro.who.int/{{{data.rssUrl}}})\n{{/options.result.rssIcon}}\n{{{_source.displayDate}}}\n{{/_source.showDate}}{{{_source.description}}}\n{{#_source.additionalInfo}}{{#_so
urce.additionalFields}} {{#title}} {{{label}}}: {{{title}}} {{/title}} {{/_source.additionalFiel", "api_data": null, "hint": null}, {"title": "News | Iran site - WHO EMRO", "url":
"https://emro.who.int/iran/news/index.html", "snippet": null, "api_data": null, "hint": null}, {"title": "Iran (Islamic Republic of) - Data", "url":
"https://www.who.int/data/gho/data/countries/country-details/GHO/iran-(islamic-republic-of)?countryProfileId=e16ed800-9300-444e-a085-f75f5f93cc24", "snippet": "The Global Health Observatory\nExplore a
world of health data\nThis is a deprecated page. If the desired country fails to load, please go directly to [https://data.who.int/countries](https://data.who.int/countries)\nName: Iran (Islamic
Republic of)\nCountry ISO Code: IRN\nCountry ISO Code: IRN", "api_data": null, "hint": null}, {"title": "Islamic Republic of Iran Country Overview | World Health Organization", "url":
"https://www.who.int/countries/irn", "snippet": "![Country presence banner Country presence banner](https://cdn.who.int/media/images/default-source/cover-images/decorative-images/who-cpr-2025-cp-
banner.png?sfvrsn=730ecc69_5)\nNews and features\nCountry profiles\nHealth profiles\nCountry profiles present selected data, statistics and information to provide national health profiles at given
points in time.\nPublications\n2 July 2024\nSurveillance and control of Anopheles stephensi\nAnopheles stephensi is an invasive mosquito species which has been found", "api_data": null, "hint": null},
{"title": "WHO in Islamic Republic of Iran", "url": "https://www.emro.who.int/iran/news/", "snippet": "WHO in Islamic Republic of Iran\n[A global model for mental health: How the Iranian integrated
care system is saving lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-saving-lives.html)\n23 February 2026 \u2013 In a south Tehran
neighborhood, a quiet transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists, physicians, psychologists, dedicated social workers, and
community voluntee", "api_data": null, "hint": null}, {"title": "WHO EMRO - Iran site", "url": "https://www.emro.who.int/iran/", "snippet": "[\nIran site-
News](https://www.emro.who.int/iran/news/)\nArticle Count:\n150\n[\nPriority areas](https://www.emro.who.int/iran/priority-areas/)\nArticle Count:\n29\n[\nInformation
resources](https://www.emro.who.int/iran/information-resources/)\nArticle Count:\n12\n[\nWHO Representative](https://www.emro.who.int/iran/who-representative/)\nArticle Count:\n1\n[\nDonors and
partners](https://www.emro.who.int/iran/donors-partners/)\nArticle Count:\n2", "api_data": null, "hint": null}, {"title": "WHO country cooperation strategy at a glance: Islamic Republic of Iran",
"url": "https://www.who.int/publications/i/item/WHO-CCU-17.01-Iran", "snippet": "WHO country cooperation strategy at a glance: Islamic Republic of Iran\nAt a glance\n15 March 2017\n| Country
Cooperation Strategy\nOverview\nAll countries with a WHO office have a Country Cooperation Strategy (CCS). CCSs are flexible to align with the national health planning cycle (generally 4-5
years).\nAfter the WHO country office and the government finalize the CCS, the country office develops a CCS Brief. The 2-page brief is updated each year, in advance of the World Health Assembly. It
summariz", "api_data": null, "hint": null}, {"title": "WHO EMRO | News | News | Iran site", "url": "https://www.emro.who.int/iran/news/news.html", "snippet": "[{{{type}}}] {{{reason}}}\n{{/data.error.
root_cause}}\n{{texts.summary}}\n{{#options.result.rssIcon}}\n[RSS](https://www.emro.who.int/{{{data.rssUrl}}})\n{{/options.result.rssIcon}}\n{{{_source.displayDate}}}\n{{/_source.showDate}}{{{_source
.description}}}\n{{#_source.additionalInfo}}{{#_source.additionalFields}} {{#title}} {{{label}}}: {{{title}}} {{/title}} {{/_source.additionalFields}}\n{{/_source.additionalInfo}}[{{{type}}}]
{{{reason}}}\n{{/data.error.root_cause}}\n{{texts.summary}}\n{{#options.result.", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "WHO health emergency dashboard Iran listed event March April 2026"
}
```

### 📋 Result

```
{"query": "WHO health emergency dashboard Iran listed event March April 2026", "results": [{"title": "WHO Health Emergency Dashboard - Extranet Systems", "url":
"https://extranet.who.int/publicemergency/", "snippet": "The World Health Organization (WHO) Health Emergency Dashboard is a platform which aims to share information about public health events and
emergencies. The data on the dashboard is refreshed every thirty (30) minutes and data is accurate as at time of refreshing.\nThe WHO Health Emergency Dashboard is not a comprehensive representation
of all the events and emergencies that WHO is aware of and responding to. The events displayed are a subset of those reported through official channels as mandate", "api_data": null, "hint": null},
{"title": "Islamic Republic of Iran Country Overview | World Health Organization", "url": "https://www.who.int/countries/irn", "snippet": "![Country presence banner Country presence
banner](https://cdn.who.int/media/images/default-source/cover-images/decorative-images/who-cpr-2025-cp-banner.png?sfvrsn=730ecc69_5)\nNews and features\nCountry profiles\nHealth profiles\nCountry
profiles present selected data, statistics and information to provide national health profiles at given points in time.\nPublications\n2 July 2024\nSurveillance and control of Anopheles
stephensi\nAnopheles stephensi is an invasive mosquito species which has been found", "api_data": null, "hint": null}, {"title": "Conflict deepens health crisis across Middle East, WHO says", "url":
"https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-east--who-says", "snippet": "More than ten days into the latest escalation of conflict in the Middle East, health
systems across the Region are coming under strain as injuries and displacement rise, attacks on health care continue, and public health risks increase.\nNational health authorities in Iran report more
than 1300 deaths and 9000 injuries, and in Lebanon report at least 570 deaths and more than 1400 injuries. In Israel, authorities report 15 deaths and 2142 injuries.\nAt the same time, the conflict is
affecting the v", "api_data": null, "hint": null}, {"title": "WHO in Islamic Republic of Iran", "url": "https://www.emro.who.int/iran/news/", "snippet": "WHO in Islamic Republic of Iran\n[A global
model for mental health: How the Iranian integrated care system is saving lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-saving-
lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists,
physicians, psychologists, dedicated social workers, and community voluntee", "api_data": null, "hint": null}, {"title": "News | Iran site - WHO EMRO", "url":
"https://www.emro.who.int/iran/news/index.html", "snippet": "WHO in Islamic Republic of Iran\n[A global model for mental health: How the Iranian integrated care system is saving
lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-saving-lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet
transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists, physicians, psychologists, dedicated social workers, and community voluntee",
"api_data": null, "hint": null}, {"title": "Assessing Iran\u2019s health system according to the COVID-19 strategic preparedness and response plan of the World Health Organization: health policy and
historical implications - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7888405/", "snippet": "Summary\nBackground\nThe role of health systems in the management of disasters, including
natural hazards like outbreaks and pandemics, is crucial and vital. Healthcare systems which are unprepared to properly deal with crises are much more likely to expose their public health workers and
health personnel to harm and will not be able to deliver healthcare provisions in critical situations. This can lead to a drammatic toll of deaths, even in developed countries. The possible occurrence
of global c", "api_data": null, "hint": null}, {"title": "WHO EMRO - Islamic Republic of Iran", "url": "https://www.emro.who.int/countries/iran/home.html", "snippet": "WHO Representative for Islamic
Republic of Iran\nDr Awad Mataria\nWHO Representative\nPO Box 14665-1565\nTehran\n11516\nemail:\n[{{{type}}}] {{{reason}}}\n{{/data.error.root_cause}}\n{{texts.summary}}\n{{#options.result.rssIcon}}\n
[RSS](https://www.emro.who.int/{{{data.rssUrl}}})\n{{/options.result.rssIcon}}\n{{{_source.displayDate}}}\n{{/_source.showDate}}{{{_source.description}}}\n{{#_source.additionalInfo}}{{#_source.additio
nalFields}} {{#title}} {{{label}}}: {{{title}}} {{/title}} {{/_source.additionalFiel", "api_data": null, "hint": null}, {"title": "Health impact of the escalation of conflict in the Middle East",
"url": "https://www.who.int/news-room/feature-stories/detail/health-impact-of-the-escalation-of-conflict-in-the-middle-east", "snippet": "NOTE: In his introductory remarks at the media briefing on 5
March 2026, the Director-General said that an estimated 100 000 people have left Iran. The text below has been corrected to show that an estimated 100 000 people have left the city of Tehran, not
Iran.\n________________________\nWHO is concerned over the expansion of the conflict in the Middle East which is putting health systems and lives at risk in the region and beyond.\nAt a press
conference earlier today, Dr Tedros Adhanom Ghebreyesu", "api_data": null, "hint": null}, {"title": "Iran\u2019s health system strains as 15,000 wounded flood hospitals", "url":
"https://www.newarab.com/news/irans-health-system-strains-15000-wounded-flood-hospitals", "snippet": "Breadcrumb\nAs US-Israel war enters third week, Iran's health system strains as 15,000 wounded
flood hospitals\nIranian hospitals have received roughly 15,000 war wounded since the US-Israeli military coalition launched strikes 16 days ago, according to [health ministry officials and Iranian
media reports](https://tasnimnews.ir/en).\nThe surge is overwhelming a health system already stretched thin after [a security crackdown](https://edition.cnn.com/2026/01/10/middleeast/tehran-iran-
protests-deaths", "api_data": null, "hint": null}, {"title": "World Health Organization Prepares for Nuclear Scenario, Including Weapons Use, in Iran \u2014 UNITED24 Media", "url":
"https://united24media.com/latest-news/world-health-organization-prepares-for-nuclear-scenario-including-weapons-use-in-iran-16995", "snippet": "Illustrative image showing a nuclear explosion diagram
overlaid with the WHO emblem. (Source: UNITED24 Media/Oleksandr Manukians)\nThe World Health Organization (WHO) is preparing for the possibility of a nuclear-related incident as tensions continue to
escalate in the Middle East, including scenarios involving strikes on nuclear facilities or the potential use of nuclear weapons.\nWe bring you stories from the ground. Your support keeps our team in
the field.\nAccording to Politico on March 18, WH", "api_data": null, "hint": null}]}
```

```json
{
  "query": "WHO classify Iran health emergency event",
  "hours_back": 168,
  "string_guarantee": [
    "Iran",
    "WHO"
  ]
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

```json
{
  "query": "site:extranet.who.int/publicemergency Iran"
}
```

### 📋 Result

```
{"query": "site:extranet.who.int/publicemergency Iran", "results": [{"title": "Iran's tallest bridge collapses after reported US airstrikes; Iran threatens American allies in retaliation", "url":
"https://www.foxnews.com/world/irans-tallest-bridge-collapses-reported-us-airstrikes-iran-threatens-american-allies-retaliation", "snippet": "[Massive strike reportedly sends Iranian bridge collapsing
in dramatic blast caught on video](https://www.foxnews.com/video/6392463207112)\nFootage captures the moment a key span gives way after a reported strike, as tensions in Iran continue to escalate.
(@realDonaldTrump/Truth Social)\nIran\u2019s biggest bridge near Tehran has crashed down in a stunning scene captured on camera following reports of U.S. airstrikes, President [Donald
Trump](https://www.foxnews.com/category/person/donald-trump) announ", "api_data": null, "hint": null}, {"title": "Trump says U.S. hasn't even started destroying what's left in Iran", "url":
"https://www.cbsnews.com/live-updates/iran-war-trump-oil-prices-israel-iranian-president-letter-american-people/", "snippet": "Live Updates: As Iran war rages on and oil prices rise, Trump says U.S.
\"hasn't even started destroying what's left\"\nWhat to know about the Iran war today:\n- President Trump warned late Thursday the U.S. \"hasn't even started destroying what's left in Iran,\" and
previewed that strikes on bridges and power plants could be next.\n- A day earlier, the president\n[asserted in a prime-time speech](https://www.cbsnews.com/news/trump-primetime-speech-iran-
today-2026-04-01/)that the U.S.'s objectives in th", "api_data": null, "hint": null}, {"title": "Iran war live: Trump claims goals nearing completion, vows to \u2018finish job\u2019", "url":
"https://www.aljazeera.com/news/liveblog/2026/4/2/iran-war-live-trump-to-address-nation-tehran-denies-seeking-ceasefire?traffic_source=rss", "snippet": "Live updatesLive updates,\nIran war updates:
US, Israel step up strikes; Tehran pledges retaliation\nTrump says US will bomb Iran \u2018back to the stone ages\u2019, but Iranian military warns it will escalate retaliatory attacks.\nlive![People
attend a funeral ceremony for the Revolutionary Guards Navy Commander Alireza Tangsiri, who was killed in strikes, amid the U.S.-Israeli conflict with Iran, in Tehran, Iran, April 1, 2026.](/wp-
content/uploads/2026/04/2026-04-01T125124Z_1787453965_RC2BGKATGGHQ_RTRMADP", "api_data": null, "hint": null}, {"title": "What you need to know: 5 key takeaways from Trump\u2019s Iran address", "url":
"https://www.foxnews.com/politics/what-you-need-know-5-key-takeaways-from-trumps-iran-address", "snippet": "[WATCH: Trump says he was 'honored' to rip up Obama's Iran nuclear deal, lists it among top
achievements](https://www.foxnews.com/video/6392400907112)\nPresident Donald Trump said ending former President Barack Obama's Iran nuclear deal from 2017 was among his top achievements against Iran
as president, telling the nation Wednesday night he was 'honored' to do it.\nPresident [Donald Trump](https://www.foxnews.com/category/person/donald-trump) addressed the nation Wednesday night, saying
the United", "api_data": null, "hint": null}, {"title": "Trump says Iran \u2018no longer a threat\u2019 after 32 days \u2014 outlines next phase of US war", "url":
"https://www.foxnews.com/politics/trump-says-iran-no-longer-threat-after-32-days-outlines-next-phase-us-war", "snippet": "[President Trump vows US is 'very close' to finishing the job on Iran: We hold
'all the cards'](https://www.foxnews.com/video/6392400810112)\nPresident Donald Trump gives the public an update on the war in Iran from the White House.\nPresident [Donald
Trump](https://www.foxnews.com/category/person/donald-trump) declared Iran is \"essentially really no longer a threat\" after a 32-day U.S. military campaign, telling Americans in a primetime address
Wednesday that the country has been \"eviscerated\" fo", "api_data": null, "hint": null}, {"title": "Inside Supreme Court: How Trump heard birthright citizenship arguments", "url":
"https://www.foxnews.com/politics/inside-supreme-court-how-trump-heard-birthright-citizenship-arguments", "snippet": "[Supreme Court concludes oral arguments in birthright citizenship
case](https://www.foxnews.com/video/6392361159112)\nFox News legal editor Kerri Urbahn breaks down oral arguments in the Supreme Court\u2019s birthright citizenship case on
\u2018Outnumbered.\u2019\nPresident Donald Trump made an extraordinary appearance Wednesday for [Supreme Court arguments](https://www.foxnews.com/politics/trump-makes-historic-scotus-appearance-
birthright-citizenship-case) \u2014 an American presidential first \u2014 as his administratio", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me piece together what I've learned so far:

1. There is an active US-Israel military conflict with Iran as of early April 2026
2. WHO has reported significant health impacts: 1,300+ deaths, 9,000+ injuries, 18 attacks on healthcare facilities, 100,000 displaced from Tehran
3. WHO has published multiple articles about the health crisis in Iran
4. WHO is preparing for nuclear scenarios in Iran
5. Iran's health system is strained with 15,000 wounded flooding hospitals

The key question is whether the WHO public emergency dashboard specifically lists an event for Iran. The dashboard is a specific tool - it displays events reported through IHR channels. 

Given the scale of this crisis—thousands of casualties, healthcare infrastructure under attack, mass displacement, and nuclear concerns—it would be surprising if WHO hadn't formally listed an event on their public dashboard. I should check the dashboard directly and see what types of events typically appear there.

## 💬 Response

Let me search for more specific information about what's currently on the WHO dashboard and whether Iran is listed.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"WHO Health Emergency Dashboard\" events countries listed 2026"
}
```

### 📋 Result

```
{"query": "\"WHO Health Emergency Dashboard\" events countries listed 2026", "results": [{"title": "World Health Organization Emergencies Programme", "url": "https://www.who.int/emergencies/overview",
"snippet": "![crowd_ambulances A crowd of people milling around ambulances in a street](https://cdn.who.int/media/images/default-source/emergencies-and-disasters/2023---conflict-in-israel-and-the-
occupied-palestinian-territory/crowd_ambulances.jpg?sfvrsn=dd0fcf04_19)\nEmergency news\n[All \u2192](https://www.who.int/news?publishingoffices=df302c0e-1f59-4efb-b276-d154122d3760,c3266c2c-ff09-
491c-8653-3a366ec1f5a6,0b0d1c8d-65d7-4517-813b-cd5f8713b310,8391662a-9628-438a-890e-a39632ea4da5&speechtypes=)\nOur emergency wo", "api_data": null, "hint": null}, {"title": "WHO Health Emergency
Dashboard - Extranet Systems", "url": "https://extranet.who.int/publicemergency/", "snippet": "The World Health Organization (WHO) Health Emergency Dashboard is a platform which aims to share
information about public health events and emergencies. The data on the dashboard is refreshed every thirty (30) minutes and data is accurate as at time of refreshing.\nThe WHO Health Emergency
Dashboard is not a comprehensive representation of all the events and emergencies that WHO is aware of and responding to. The events displayed are a subset of those reported through official channels
as mandate", "api_data": null, "hint": null}, {"title": "Health Emergencies - PAHO/WHO | Pan American Health Organization", "url": "https://www.paho.org/en/health-emergencies", "snippet": "The
objective of the Pan American Health Organization's (PAHO) work in Health Emergencies is to increase the health sector resilience to emergencies and disasters. Our priority is to deliver rapid,
predictable, and comprehensive support to Member States in terms of prevention, risk reduction, preparedness, surveillance, response, and early recovery in case of any threat to human health,
including outbreaks or disasters caused by natural phenomena, biological, chemical or radiological agent, huma", "api_data": null, "hint": null}, {"title": "WHO launches 2026 appeal to help millions
of people in health emergencies and crisis settings", "url": "https://www.who.int/news/item/03-02-2026-who-launches-2026-appeal-to-help-millions-of-people-in-health-emergencies-and-crisis-settings",
"snippet": "The World Health Organization (WHO) today launched its 2026 global appeal to ensure that millions of people living in humanitarian crises and conflicts can access health care.\nIn 2025,
WHO and partners supported 30 million people funded through its annual emergency appeal. These resources helped deliver life-saving vaccination to 5.3 million children, enabled 53 million health
consultations, supported more than 8000 health facilities, and facilitated the deployment of 1370 mobile clinics.\nThe 20", "api_data": null, "hint": null}, {"title": "Stronger together - milestones
that mattered in 2025", "url": "https://www.who.int/news-room/spotlight/stronger-together-milestones-that-mattered-in-2025", "snippet": "Stronger together: milestones that mattered in 2025\nThe
conclusion of discussions on the Pandemic Agreement in Committee at the World Health Assembly 2025.\nLooking back on 2025, the year has been marked by immense achievements and profound challenges for
global health. In the face of major funding cuts and increasing threats to science and solidarity, WHO continued to lead and champion global efforts to confront the biggest health challenges of our
time.\nFrom governments adopting the world\u2019s fir", "api_data": null, "hint": null}, {"title": "New WHO Guidance Helps Countries to Institutionalize Simulation Exercises to Strengthen Health
Emergency Readiness", "url": "https://www.who.int/news/item/24-03-2026-new-who-guidance-helps-countries-to-institutionalize-simulation-exercises-to-strengthen-health-emergency-readiness", "snippet":
"From pandemics to radiological threats, countries are better prepared when they move from ad-hoc drills to structured programs\nIn an increasingly unpredictable world, emergencies are no longer rare
events, they are recurring tests of national resilience. From pandemics and climate-driven disasters to chemical and radiological and nuclear incidents, countries face a growing spectrum of public
health threats.\nTo support countries prepare more systematically against emergencies, WHO has recently re", "api_data": null, "hint": null}, {"title": "World Health Organization strategy (2022-2026)
for National Action Plan for Health Security", "url": "https://www.who.int/publications/b/66386", "snippet": "Digital publications\nThis page and linked pages display WHO publications in various
digital formats, over and above what is available on [Publications](https://www.who.int/publications).\nThis publication page will eventually replace
[Publications](https://www.who.int/publications).\nIf you are unable to find a publication through the search function on this page, please try the search bar by clicking on the magnifying glass at
the top right of the site.", "api_data": null, "hint": null}, {"title": "Disease Outbreak News (DONs)", "url": "https://www.who.int/emergencies/disease-outbreak-news", "snippet": "Emergencies\nDisease
Outbreak News (DONs)\nLatest WHO Disease Outbreak News (DONs), providing information on confirmed acute public health events or potential events of concern.\nAccording to Article 11.4 of the
International Health Regulations (2005) [IHR (2005)], WHO may make information on acute public health events available, if other information about the same event has already become publicly available
and there is a need for the dissemination of authoritative and independent information. The", "api_data": null, "hint": null}, {"title": "News", "url": "https://www.who.int/news", "snippet":
"News\nBrowse selected WHO news below.\n30 March 2026\nJoint external evaluation of the International Health Regulations (2005) core capacities of Vanuatu\nDuring the JEE mission, which took place in
Port Vila from 16 to 20 June 2025, Vanuatu\u2019s capacities in 19 technical areas were evaluated through...\n26 March 2026\nWorld report on promoting the health of refugees and migrants: Monitoring
progress on the WHO global...\nThe World report on promoting the health of refugees and migrants: Monitoring progr", "api_data": null, "hint": null}, {"title": "2026", "url":
"https://www.who.int/emergencies/funding/health-emergency-appeals/2026", "snippet": "![HEA landing page flash appeal, oPt, 2026 A health worker in a headscarf is holding a baby lying on a bed in a
temporary clinic.](https://cdn.who.int/media/images/default-source/products/emergency-appeals/2026/hea-landing-page-flash-appeal--opt--2026.jpg?sfvrsn=a0cc47e0_7)\nWHO's Health Emergency Appeal
2026\nPatients gathered at Al-Mawasi Field Hospital as they prepared for medical evacuation outside Gaza to T\u00fcrkiye and the UK.\nA world in crisis: confronting the drivers of health
emergencies\nSev", "api_data": null, "hint": null}]}
```

```json
{
  "query": "WHO public emergency dashboard Iran health event classified March April 2026"
}
```

### 📋 Result

```
[{"title": "Conflict deepens health crisis across Middle East, WHO says", "url": "https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-east--who-says", "snippet":
"Conflict deepens health crisis across Middle East, WHO says Skip to main content\n\n \n\n \n\n \n\n \n\n\u00a9 WHO WHO Representative and team in Lebanon visit a shelter housing internally displaced
people, run by health partner Caritas Lebanon.\n\n\u00a9 Credits\n\n# Conflict deepens health crisis across Middle East, WHO says\n\nMore than ten days into the latest escalation of conflict in the
Middle East, health systems across the Region are coming under strain as injuries and displacement rise, attacks on health care c", "highlights": ["Conflict deepens health crisis across Middle East,
WHO says Skip to main content   ...    \u00a9 Credits\n\n# Conflict deepens health crisis across Middle East, WHO says More than ten days into the latest escalation of conflict in the Middle East,
health systems across the Region are coming under strain as injuries and displacement rise, attacks on health care continue, and public health risks increase. National health authorities in Iran
report more than 1300 deaths and 9000 injuries, and in Lebanon report at least 570 deaths and more than 1400 injuries. In Israel, authorities report 15 deaths and 2142 injuries. At the same time, the
conflict is affecting the very services meant to save lives. In Iran, WHO has verified 18 attacks on health care since 28 February, resulting in 8 deaths among health workers. Over the same period in
Lebanon, 25 attacks on health care have resulted in 16 deaths and 29 injuries. These attacks not only cost lives but deprive   ...    under international humanitarian law. Beyond the immediate impact,
the conflict is creating wider public health risks. Current estimates indicate more than 100 000 people in Iran have relocated to other areas of the country due to insecurity, and up to 700 000 people
have been internally displaced in Lebanon, with many in crowded collective shelters under deteriorating public health conditions, with limited access to safe water, sanitation and hygiene. These
conditions increase the risk of respiratory infections, diarrhoeal diseases, and other communicable illnesses, especially for the most vulnerable populations, such as women and children. Environmental
hazards are also a raising concern. In Iran, petroleum fires and smoke from damaged infrastructure exposed nearby communities to toxic pollutants that potentially cause breathing problems, eye and
skin irritation, and   ...    Access to health services is becoming increasingly constrained across several countries. In Lebanon, 49 primary health   ...    maternal and neonatal services, and
management of communicable diseases. Temporary airspace restrictions have disrupted the movement of medical supplies from WHO\u2019s global logistics hub in Dubai. More than 50 emergency supply
requests, intended to benefit over 1.5 million people across 25 countries, are   ...    supplies for Mozambique, is expected to depart from the hub in the coming week. The escalation comes at a time
when humanitarian needs in the Eastern Mediterranean Region were already among the highest in the world. Across the Region, 115 million people require humanitarian assistance \u2013 almost half of all
people in need globally \u2013 while humanitarian health emergency appeals remain 70% underfunded. Without protection for health care, sustained humanitarian access and stronger financial and
operational support for the humanitarian health response, the strain on vulnerable populations and already fragile health systems will continue to grow. WHO calls on all parties to protect civilians
and health care, ensure unimpeded and sustained humanitarian access, and pursue de-escalation of the conflict so communities can begin to recover and move towards peace. Media Contacts\n\nInas
Hamam\n\nRegional emergency communications World Health Organization\n\nEmail: hamami@who.int WHO Media Team\n\nWorld Health Organization\n\nEmail: mediainquiries@who.int\n\nRelated\n\nConflict in the
Middle East Feature stories\n\nHealth impact of the escalation of conflict in the Middle East 5 March 2026"], "published_date": "2026-03-11T00:00:00.000", "score": null}, {"title": "Middle East
Escalation of Conflict, Global external situation report #1 - 26 March 2026 - Iran (Islamic Republic of) | ReliefWeb", "url": "https://reliefweb.int/report/iran-islamic-republic/middle-east-
escalation-conflict-global-external-situation-report-1-26-march-2026", "snippet": "Middle East Escalation of Conflict, Global external situation report #1 - 26 March 2026 - Iran (Islamic Republic of)
| ReliefWeb\n\n- Download Report (PDF | 189.99 KB)\n\nThis is the first global public WHO situation report on the conflict in the Middle East. It covers the health situation and WHO operational
updates from affected countries in the WHO Eastern Mediterranean and European regions, as well as WHO's global response activities and priorities.\n\nACUTE HEALTH THREATS\n\nAcross the affected are",
"highlights": ["Middle East Escalation of Conflict, Global external situation report #1 - 26 March 2026 - Iran (Islamic Republic of) | ReliefWeb - Download Report (PDF | 189.99 KB) This is the first
global public WHO situation report on the conflict in the Middle East. It covers the health situation and WHO operational updates from affected countries in the WHO Eastern Mediterranean and European
regions, as well as WHO's global response activities and priorities. ACUTE HEALTH THREATS Across the affected area, WHO assesses the main health risks as trauma, injuries and disability; continued
access to health care, especially for people who have been displaced, including for the management of non-communicable diseases, and the potential for diseases to spread in shelters; risks associated
with strikes on desalination plants reducing people\u2019s access to safe water; the potential for a chemical, biological, radiological or nuclear (CBRN) incident with health consequences; heat-
related illnesses as the weather warms; mental health distress; and respiratory diseases. In addition to the immediate health impacts of the conflict, strikes on oil storage facilities and refineries
in Iran, Bahrain and Saudi Arabia raise concerns about air pollution and wider regional environmental exposure; and fuel shortages may affect the functionality of health systems. Attacks on health
care in multiple countries have led to health worker deaths and have wider consequences in reducing access to care in the short, and sometimes longer term, depending on the incident. Disruptions to
supply chains, rising transportation costs and variability in the energy market can have knock-on effects across supply chains and may limit access to essential medicines and supplies. ## Related
Content"], "published_date": "2026-03-26T16:18:00.000", "score": null}, {"title": "Iran war complicates WHO's emergency medical supply routes", "url": "https://www.reuters.com/world/middle-east/iran-
war-complicates-whos-emergency-medical-supply-routes-2026-03-26/", "snippet": "Iran war complicates WHO's emergency medical supply routes | Reuters\n\nExclusive news, data and analytics for financial
market professionalsLearn more aboutRefinitiv\n\nItem 1 of 5 Medical aid shipment from the World Health Organization (WHO) and the U.N. refugee agency, United Nations High Commissioner for Refugees
(UNHCR) arrives at the Beirut-Rafic Hariri International Airport, in Beirut, Lebanon, October 4, 2024. REUTERS/Louisa Gouliamaki\n\n[1/5]Medical aid shipment from the World Health Organiz",
"highlights": ["Iran war complicates WHO's emergency medical supply routes | Reuters   ...    Item 1 of 5 Medical aid shipment from the World Health Organization (WHO) and the U.N. refugee agency,
United Nations   ...    October 4, 2024. REUTERS/Louisa Gouliamaki   ...    - Summary - UAE funds trucking and flights for WHO shipments\n- Rising fuel costs and border delays impact aid logistics -
Some shipping firms waive extra costs for aid GENEVA, March 26 (Reuters) - The \u200bWorld Health Organization is finding other routes to deliver emergency medical supplies \u200cfrom its Dubai hub to
crises such as Lebanon via long overland journeys, an official said, but rising fuel costs could hamper shipments if the Iran war persists. The global health body's aid shipments from \u200bthe United
Arab Emirates were previously completely frozen as air, sea and \u200bland routes were restricted by the Iran conflict, which began on February 28 \u2060with U.S.-Israeli air strikes. Sign up here.
Iran responded by firing drones and missiles at energy and \u200bother infrastructure across the Gulf, while militant group Hezbollah pulled Lebanon into the regional war \u200bby firing on Israel in
support of its patron Iran. To tackle the shipment problems, the UAE has provided funding to truck supplies like insulin and emergency kits to Lebanon - where over 3,000 people \u200bhave been
wounded- via Saudi Arabia, Jordan and Syria as well as funding to \u200bcharter flights to other hotspots like Kabul, Afghanistan, said the WHO official. \"What you're getting is cost increases
\u200cand \u2060lead time increases as we do the workarounds,\" Paul Molinaro, WHO head of   ...    support. But Molinaro said the Dubai backlog has not completely cleared, citing smaller medical
\u200bshipments that remain \u200bstranded. He said two \u2060shipping companies have waived insurance surcharges. The International Federation of Red Cross and Red Crescent Societies said it planned
to truck ambulances \u200bfor Lebanon overland from Dubai but said road costs were up \u200baround 30% \u2060and there were border delays. Asked about the risk of drug shortages, Molinaro said he was
more concerned about oil price hikes leading to exhausted fuel stocks in poorer countries \u2060and aid \u200bstocks becoming stranded. \"You could be seeing serious issues \u200b6 to 8 weeks down the
line,\" he said. \"I think we're going to feel that quicker   ...    (ACANU). ## World\n\n### Somali national army takes control of part of biggest city in South West state Africacategory\u00b7 March
30, 2026 \u00b7 2:47 PM UTC \u00b7 ago Somalia's national army has taken control of part of the biggest city in South West state, two weeks after regional officials said they were severing \u200bties
with the federal government in the capital Mogadishu, local residents \u200csaid. Middle Eastcategory Turkey says NATO defences downed fourth inbound Iranian missile ANALYSIS Ukraine's drone masters
eye Iran war to kickstart export ambitions   ...    Businesscategory US-bound Delta"], "published_date": "2026-03-26T15:52:11.000", "score": null}, {"title": "WHO confirms 18 attacks on healthcare
sites in Iran - WHTC", "url": "https://whtc.com/2026/03/11/who-confirms-18-attacks-on-healthcare-sites-in-iran/", "snippet": "\n\n WHO confirms 18 attacks on healthcare sites in Iran | 1450 AM 99.7 FM
WHTC | Holland \n\n\u00d7\n\n- Sign In\n\nMore\n\n- Obituaries\n- On Air\n- Events\n- Photos\n- Videos\n\n# WHO confirms 18 attacks on healthcare sites in Iran\n\nBy Thomson Reuters Mar 11, 2026 |
11:00 AM\n\nMarch 11 (Reuters) \u2013 The World Health Organization said on Wednesday that it has verified 18 attacks on healthcare centers in Iran since the start \u200bof the U.S. and Israel war on
\u200cIran on February 28, which has resulted in 8 deaths among heal", "highlights": ["WHO confirms 18 attacks on healthcare sites in Iran | 1450 AM 99.7 FM WHTC | Holland \n\n\u00d7\n\n- Sign
In\n\nMore - Obituaries\n- On Air\n- Events\n- Photos\n- Videos\n\n# WHO confirms 18 attacks on healthcare sites in Iran By Thomson Reuters Mar 11, 2026 | 11:00 AM March 11 (Reuters) \u2013 The World
Health Organization said on Wednesday that it has verified 18 attacks on healthcare centers in Iran since the start \u200bof the U.S. and Israel war on \u200cIran on February 28, which has resulted in
8 deaths among health workers. \u201cThese attacks not only cost lives but deprive communities of care when they need it most. Health workers, patients and \u200chealth \u200bfacilities must always be
protected \u2060under international humanitarian law,\u201d \u2060the WHO said in a statement. During the same period, 25 attacks on healthcare centers in Lebanon have resulted in 16 deaths and 29
injuries, the agency \u200bsaid. The conflict has triggered a large-scale population movement, the WHO added. It estimates more than 100,000 people in \u2060Iran have relocated, and up \u2060to
700,000 people in Lebanon have been \u200binternally displaced, many sheltering in crowded buildings with scarce access \u200bto clean water, sanitation and hygiene. Such conditions risk
\u200coutbreaks of respiratory and diarrheal diseases, the WHO warned, particularly among women and children. On Tuesday, the agency said that the \u201cblack rain\u201d and toxic compounds in the air
\u2060in Iran after strikes on its oil facilities could cause respiratory problems, and backed Iran\u2019s advisory urging people to remain \u2060indoors. In Lebanon, \u200c49 primary healthcare
centers and five hospitals \u2060have shut following evacuation orders issued \u200bby Israel\u2019s \u200cmilitary, reducing the availability of essential \u200bservices while \u2060medical needs
rise, the WHO said on Wednesday. Across the eastern Mediterranean region, 115 million people require humanitarian assistance, while 70% of the humanitarian health appeals remain underfunded, the
health organization said. (Reporting by Siddhi Mahatole in Bengaluru; Editing \u200bby Shinjini Ganguli) Holland Police Log Mar. 31-Apr. 1, 2026 4h ago Explosions heard in Damascus area, likely from
Israeli interception of Iranian missiles, state TV says 3h ago US retail sales strong in February; Iran war expected to hurt spending 3h ago Hasbro investigates cybersecurity incident, takes some
systems offline 4h ago ICE agents to work in airports as long as needed, says US transportation secretary 3h ago King Charles to address US Congress on April 28 4h ago\n\n \n\n \n\n \n\n#### On Air
Now\n\nWHTC Midday Report 12:10 PM - 12:"], "published_date": "2026-03-11T15:00:49.000", "score": null}, {"title": "WHO Situation Report No.1: Middle East Escalation of Conflict (11 March 2026) -
Lebanon | ReliefWeb", "url": "https://reliefweb.int/report/lebanon/who-situation-report-no1-middle-east-escalation-conflict-11-march-2026", "snippet": "WHO Situation Report No.1: Middle East
Escalation of Conflict (11 March 2026) - Lebanon | ReliefWeb\n\n- Download Report (PDF | 1.23 MB)\n\nCRISIS IN NUMBERS\n\n21 Countries affected globally\n\n14 Countries affected in the Eastern
Mediterranean Region\n\n115 Million people already needed humanitarian assistance before this current escalation (almost 50% of all people-in-need globally).\n\nKEY HIGHLIGHTS\n\n\u2022 National
authorities report 1255 deaths and more than 15 100 injuries in Iran, and 634 deaths and mor", "highlights": ["WHO Situation Report No.1: Middle East Escalation of Conflict (11 March 2026) - Lebanon |
ReliefWeb - Download Report (PDF | 1.23 MB)\n\nCRISIS IN NUMBERS\n\n21 Countries affected globally 14 Countries affected in the Eastern Mediterranean Region 115 Million people already needed
humanitarian assistance before this current escalation (almost 50% of all people-in-need globally). KEY HIGHLIGHTS \u2022 National authorities report 1255 deaths and more than 15 100 injuries in Iran,
and 634 deaths and more than 1586 injuries in Lebanon. \u2022 Current estimates indicate more than 100 000 people have relocated to other areas in Iran and over 800 000 displaced in Lebanon, with many
sheltering in crowded collective shelters under deteriorating public health conditions. \u2022 WHO has verified 18 attacks on health care in Iran resulting in 8 deaths, and 25 attacks in Lebanon
resulting in 16 deaths and 29 injuries, further disrupting health services. \u2022 In Lebanon, 48 primary health care centres and 5 hospitals have closed following evacuation orders, while in Iraq
road closures are affecting ambulance movement and medicine deliveries. Crossings into the Gaza Strip remain largely closed, and in the West Bank movement restrictions and checkpoints are delaying
ambulance transport and patient referrals. \u2022 In Syria, increased cross-border arrivals from Lebanon are raising demand for health services at border areas, while in Iraq, the evolving security
situation and movement restrictions are placing pressure on hospitals and disease surveillance activities. \u2022 Across GCC countries, health systems remain operational and focused on preparedness,
with national authorities activating emergency plans, strengthening monitoring for environmental and radiological risks. \u2022 Strikes on oil storage facilities and refineries in Iran, Bahrain and
Saudi Arabia are raising concerns about air pollution and wider regional environmental exposure, in addition to the immediate health impacts of the conflict. ## Related Content"], "published_date":
"2026-03-12T03:56:07.000", "score": null}, {"title": "WHO warns war in Iran will lead to regional instability, public health ...", "url": "https://www.cidrap.umn.edu/public-health/who-warns-war-iran-
will-lead-regional-instability-public-health-crises", "snippet": "WHO warns war in Iran will lead to regional instability, public health crises | CIDRAP\n\n# WHO warns war in Iran will lead to
regional instability, public health crises\n\nNews brief\n\nStephanie Soucheray, MA\n\nTopics\n\nPublic Health\n\nShare\n\nCopied to clipboard\n\nUnited States Mission Geneva/Flikr\n\nThe World Health
Organization (WHO) is warning that the war in Iran is worsening public health conditions across the Middle East region.\n\nAfter 10 days of bombings and conflict in Iran, national health autho",
"highlights": ["WHO warns war in Iran will lead to regional instability, public health crises | CIDRAP # WHO warns war in Iran will lead to regional instability, public health crises\n\nNews
brief\n\nStephanie Soucheray, MA Topics\n\nPublic Health\n\nShare\n\nCopied to clipboard\n\nUnited States Mission Geneva/Flikr The World Health Organization (WHO) is warning that the war in Iran is
worsening public health conditions across the Middle East region. After 10 days of bombings and conflict in Iran, national health authorities in Iran report more than 1,300 deaths and 9,000 injuries,
and Lebanon reports at least 570 deaths and more than 1,400 injuries. In Israel, authorities have documented 15 deaths and 2,142 injuries. The WHO said eight health care workers have died in Iran.
Moreover, hundreds of thousands of Iranians and Lebanese have moved into collective shelters, which increase the risk of respiratory infections and diarrheal diseases. In Iran, petroleum fires and
smoke from damaged infrastructure exposed nearby communities to toxic pollutants that potentially cause breathing problems, eye and skin irritation, and contaminated water and food sources.
\u201cEnvironmental hazards are also a raising concern. In Iran, petroleum fires and smoke from damaged infrastructure exposed nearby communities to toxic pollutants that potentially cause breathing
problems, eye and skin irritation, and contaminated water and food sources,\u201d the WHO said. ### Airspace restrictions limiting aid The WHO said temporary airspace restrictions have disrupted the
movement of medical supplies from WHO\u2019s global logistics hub in Dubai, resulting in significant backlogs to emergency supply requests. The Middle East region is the most dependent on assistance
and humanitarian need in the world, representing almost half of all people in need globally. \u201cWHO calls on all parties to protect civilians and health care, ensure unimpeded and sustained
humanitarian access, and pursue de-escalation of the conflict so communities can begin to recover and move towards peace,\u201d the organization said. # CDC: Antiviral use low among older COVID
outpatients, despite higher risk for severe disease\n\nNews brief   ...    From June 2023 to September 2025, only 16% to 38% of non-hospitalized US COVID-19 patients aged 65 years and older were   ...
(adjusted odds ratio [aOR], 1.09 and 1.11, respectively), those of Asian (aOR, 1.42) or Hispanic (aOR, 1.24) race, and   ...    (21%), fall and winter 2024-25 (23%), spring 2025 (16%), and summer 2025
(19%) than during other seasons (range, 37% to   ...    # Early detection of kidney injury in E coli outbreak at daycare centers may have improved outcomes\n\nNews brief   ...    A University of
Calgary\u2013led research team finds that only 7% of children infected with Shiga toxin\u2013producing Escherichia coli (STEC) developed hemolytic uremic syndrome (HUS) during a 395-case outbreak at
11 daycare centers in Alberta, Canada, perhaps partly due to daily lab monitoring for kidney injury. The researchers investigated the outbreak among children and adults related to contaminated food
served at the centers in August 2023, publishing the findings yesterday in JAMA Network Open. An estimated 15% to 20% of children infected with STEC develop HUS, more than half of whom require
dialysis. \u201cAlberta,   ...    In total, 326 primary and 33 secondary infections occurred among 288 children and 71 adults. Of the 359 infections,   ...    Only 7% of children infected with STEC
developed HUS, which is lower than reported in most prior outbreaks and sporadic   ...    The study identified significant use of health care resources, the researchers said. \u201cOnly 7% of children
infected with STEC developed HUS, which is lower than reported in most prior outbreaks and sporadic case series,\u201d they wrote. \u201cThese findings highlight the importance of a coordinated public
health response integrated with clinical care and suggest   ...    ALL BRIEFS\n\n## In case you missed it   ...    Of the 1,487 cases, 21% are in children younger than 5 years, and 74% involve
children and young adults up to 19   ...    My March 3 CIDRAP Op-Ed asked whether ACIP would follow the evidence or a political agenda. The meeting didn\u2019t happen.   ...    - Antimicrobial
Resistance\n- COVID-19\n- Chronic Wasting Disease\n- Influenza\n- Public Health Alerts\n- All Topics A-Z   ...    - About CIDRAP\n- CIDRAP in the News\n- Our Staff\n- Our Director\n- Osterholm in the
Press"], "published_date": "2026-03-11T00:00:00.000", "score": null}, {"title": "WHO says it has verified 13 attacks on health sites in Iran - WHBL", "url": "https://whbl.com/2026/03/05/four-medics-
killed-in-iran-ambulances-damaged-who-says/", "snippet": "WHO says it has verified 13 attacks on health sites in Iran | 1330 & 101.5 WHBL\n\n\u00d7\n\n- Sign In\n\nMORE\n\n- PODCASTS\n- ON AIR\n-
LOCAL SPORTS\n- BLOGS\n- AGRICULTURE\n\n5 active school or business cancellations.\n\n# WHO says it has verified 13 attacks on health sites in Iran\n\nBy Thomson Reuters Mar 5, 2026 | 8:07
AM\n\n(Changes headline, paragraphs one and three to show that the WHO is referring to reports from Iranian \u200bauthorities)\n\nGENEVA, March 5 (Reuters) \u2013 The World Health \u200cOrganization
chief said on Th", "highlights": ["WHO says it has verified 13 attacks on health sites in Iran | 1330 & 101.5 WHBL\n\n\u00d7\n\n- Sign In\n\nMORE - PODCASTS\n- ON AIR\n- LOCAL SPORTS\n- BLOGS\n-
AGRICULTURE\n\n5 active school or business cancellations. # WHO says it has verified 13 attacks on health sites in Iran\n\nBy Thomson Reuters Mar 5, 2026 | 8:07 AM (Changes headline, paragraphs one
and three to show that the WHO is referring to reports from Iranian \u200bauthorities) GENEVA, March 5 (Reuters) \u2013 The World Health \u200cOrganization chief said on Thursday that it has verified
13 attacks on health infrastructure in Iran amid a U.S.-Israeli campaign and it was checking \u200creports \u200bthat four medics were \u2060killed and 25 \u2060others injured. \u201cWHO has verified
13 attacks on health care in Iran and one in Lebanon,\u201d World Health Organization Director-General Tedros \u200bAdhanom Ghebreyesus told a press conference, without attributing blame or giving
details. Dr. Hanan \u2060Balkhy added at \u2060the same briefing that four ambulances \u200bin Iran were also affected and that \u200bhospitals and other health sites suffered minor \u200cdamage due
to strikes nearby, citing Iranian authorities. One of these hospitals in the capital Tehran was evacuated as a \u2060result, the U.N. health agency previously said. Iran\u2019s ambassador to the U.N.
in Geneva has alleged that \u206010 facilities \u200chave been hit by \u2060military strikes in a letter to \u200bTedros \u200cearlier this week. Balkhy says that \u200bthe WHO \u2060logistics hub in
Dubai which provides health supplies to dozens of countries is temporarily out of service because of transport restrictions in the region. (Reporting by Christy Santhosh and \u200bEmma Farge) FBI
probes US security official who quit over Iran war, Semafor reports 4h ago US detects drones over base where Rubio, Hegseth live, Washington Post reports 2h ago Trump says Israel attacked Iran gas
field without US and Qatari involvement, warns against attacks on Qatar 2h ago Thailand's Anutin nominated to contest PM vote in parliament 2h ago Who are the top international representatives
attending China's Boao Forum? 3h ago Investors react to BOJ's decision to hold rates 3h ago\n\nADVERTISE WITH US \u00bb\n\n#### On Air Now Coast to Coast AM with George Noory\n\n12:00 AM - 5:00
AM\n\n"], "published_date": "2026-03-05T14:07:47.000", "score": null}, {"title": "WHO says it has verified 13 attacks on health sites in Iran | Reuters", "url": "https://www.reuters.com/world/middle-
east/who-says-has-it-has-verified-13-health-attacks-iran-2026-03-05/", "snippet": "WHO says it has verified 13 attacks on health sites in Iran | Reuters\n\nSkip to main content\n\nExclusive news, data
and analytics for financial market professionalsLearn more aboutRefinitiv\n\nA logo is pictured outside a building of the World Health Organization (WHO) during an executive board meeting on update on
the coronavirus disease (COVID-19) outbreak, in Geneva, Switzerland,... Purchase Licensing Rights, opens new tab Read more\n\nGENEVA, March 5 (Reuters) - The World Health Organization chief",
"highlights": ["WHO says it has verified 13 attacks on health sites in Iran | Reuters\n\nSkip to main content   ...    A logo is pictured outside a building of the World Health Organization (WHO)
during an executive board meeting on update on the coronavirus disease (COVID-19) outbreak, in Geneva, Switzerland,... Purchase Licensing Rights, opens new tab Read more GENEVA, March 5 (Reuters) -
The World Health Organization chief said on Thursday that it \u200chas verified 13 attacks on health infrastructure in Iran amid a U.S.-Israeli campaign and it was checking reports that four
healthcare workers were killed and 25 \u200bothers injured. \"An estimated 100,000 people have left Iran and \u200bin Lebanon, more than 60,000 people have been displaced,\" World Health
\u2060Organization Director-General Tedros Adhanom Ghebreyesus told a press conference, without \u200battributing blame.   ...    Dr. Hanan Balkhy added at the same briefing that four \u200bambulances
in Iran were also affected and that hospitals and other health sites suffered minor damage due to strikes nearby, citing Iranian authorities. One of these hospitals \u200bin the capital Tehran was
evacuated as a result, the U.N. health \u200bagency previously said. \"As of now, for Iran we have verified 13 attacks on \u200chealth \u2060care, resulting in 3 deaths and no injuries. For Lebanon,
we have now verified three attacks resulting in three deaths and six injuries,\" a WHO spokesperson told Reuters. Iran's ambassador to the U.N. in \u200bGeneva in a \u200bletter to Tedros
\u2060earlier this week has alleged that 10 facilities have been hit by military strikes. Balkhy said that the \u200bWHO logistics hub in Dubai, which provides health supplies \u200bto \u2060dozens of
countries, is temporarily out of service because of transport restrictions in the region. A spokesperson from the International Federation of Red Cross \u2060and Red \u200bCrescent Societies also said
on Thursday \u200bthat three of its workers had been injured in military attacks since February 28 \u200bin Iran.   ...    in International Relations. She is currently on the board of the press
association for UN correspondents in Geneva (ACANU). ## World\n\n### The complexities of refueling the war in the sky Middle Eastcategory\u00b7 March 19, 2026 \u00b7 7:42 AM UTC \u00b7 ago An aging
U.S. fleet of KC\u2011135 refueling aircraft underpins airstrikes on Iran, highlighting the risks, mechanics and strain of aerial refueling in crowded skies.   ...    Asia Pacificcategory China's
February youth jobless rate dips to 16.1% Chinacategory Independent Hong"], "published_date": "2026-03-05T13:55:00.000", "score": null}, {"title": "WHO - Emergency situation reports", "url":
"http://www.who.int./emergencies/situation-reports", "snippet": "WHO - Emergency situation reports Skip to main content\n\nEmergencies\n\nOverview Funding Operations Partners Surveillance Research
Training\n\n# Emergency situation reports\n\nAll \u2192\n\nLatest WHO official reports for emergency situations.\n\n#### Public Health Situation Analysis - Afghanistan - March 2026\n\n12 March 2026
Public Health Situation Analysis - Afghanistan - March 2026\n\n#### Public Health Situation Analysis - Somalia\n\n11 March 2026 Public Health Situation Analysis - Somalia\n\n#### Public Health Si",
"highlights": ["WHO - Emergency situation reports Skip to main content\n\nEmergencies Overview Funding Operations Partners Surveillance Research Training\n\n# Emergency situation reports\n\nAll \u2192
Latest WHO official reports for emergency situations. #### Public Health Situation Analysis - Afghanistan - March 2026 12 March 2026 Public Health Situation Analysis - Afghanistan - March 2026 ####
Public Health Situation Analysis - Somalia\n\n11 March 2026 Public Health Situation Analysis - Somalia #### Public Health Situation Analysis - Sudan Conflict and Complex Emergency 25 February 2026
Public Health Situation Analysis - Sudan Conflict and Complex Emergency #### Public Health Situation Analysis - Flooding across Southeast Africa 25 February 2026 Public Health Situation Analysis -
Flooding across Southeast Africa #### Multi-country outbreak of mpox, External situation report #63 - 24 February 2026 24 February 2026 Multi-country outbreak of mpox, External situation report #63 -
24 February 2026 #### Multi-country outbreak of cholera, epidemiological update #34 -21 February 2026 21 February 2026 Multi-country outbreak of cholera, epidemiological update #34 -21 February 2026
#### Multi-country outbreak of cholera, epidemiological update #33 -27 January 2026 27 January 2026 Multi-country outbreak of cholera, epidemiological update #33 -27 January 2026 #### Multi-country
outbreak of mpox, External situation report #62 - 23 January 2026 23 January 2026 Multi-country outbreak of mpox, External situation report #62 - 23 January 2026 #### Public Health Situation Analysis
- Cambodia - Thailand border conflict 5 January 2026 Public Health Situation Analysis - Cambodia - Thailand border conflict #### Public Health Situation Analysis - the Central African Republic 23
December 2025 Public Health Situation Analysis - the Central African Republic\n\n## Related emergency content Emergency list\n\nDisease Outbreak News\n\nTravel advice\n\nWeekly Epidemiological Record
Get the latest Emergency situation reports\n\nSubscribe"], "published_date": null, "score": null}, {"title": "Multi-country outbreak of cholera, epidemiological update #35 -27 March 2026", "url":
"https://www.who.int/publications/m/item/multi-country-outbreak-of-cholera--epidemiological-update--35--27-march-2026", "snippet": "Multi-country outbreak of cholera, epidemiological update #35 -27
March 2026 Skip to main content\n\n \n\n \n\n \n\n \n\n \n\n- Select language - \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u4e2d\u6587 fran\u00e7ais \u0440\u0443\u0441\u0441\u043a\u0438\u0439
espa\u00f1ol portugu\u00eas\n\n \n\nDownload (1.6 MB)\n\n### Overview\n\nIn February 2026 (epidemiological weeks 5 to 8), a total of 18 715 new cholera and acute watery diarrhoea (AWD) cases were
reported from 17 countries, territories, and areas across four WHO regions, showing a 3% increase from January 2026. The African Region registered the highest n", "highlights": ["Multi-country
outbreak of cholera, epidemiological update #35 -27 March 2026 Skip to main content - Select language - \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u4e2d\u6587 fran\u00e7ais
\u0440\u0443\u0441\u0441\u043a\u0438\u0439 espa\u00f1ol portugu\u00eas\n\n \n\nDownload (1.6 MB)\n\n### Overview In February 2026 (epidemiological weeks 5 to 8), a total of 18 715 new cholera and
acute watery diarrhoea (AWD) cases were reported from 17 countries, territories, and areas across four WHO regions, showing a 3% increase from January 2026. The African Region registered the highest
number of cases, followed by the Eastern Mediterranean Region, the Region of the Americas, and the South-East Asia Region. This period also saw 269 cholera-related deaths globally, highlighting a 48%
increase from the previous month. No outbreaks were reported in the Western Pacific Region during this time. Cholera upsurge (2021-present): https://www.who.int/emergencies/situations/cholera-
upsurge/\n\nWHO Team Epidemic and Pandemic Management (EPM), Health Emergency Alert and Response Operations (EOP)\n\nNumber of pages\n\n8"], "published_date": null, "score": null}]
```

```json
{
  "query": "WHO grading Iran health emergency conflict March 2026"
}
```

### 📋 Result

```
{"query": "WHO grading Iran health emergency conflict March 2026", "results": [{"title": "Conflict deepens health crisis across Middle East, WHO says", "url":
"https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-east--who-says", "snippet": "More than ten days into the latest escalation of conflict in the Middle East, health
systems across the Region are coming under strain as injuries and displacement rise, attacks on health care continue, and public health risks increase.\nNational health authorities in Iran report more
than 1300 deaths and 9000 injuries, and in Lebanon report at least 570 deaths and more than 1400 injuries. In Israel, authorities report 15 deaths and 2142 injuries.\nAt the same time, the conflict is
affecting the v", "api_data": null, "hint": null}, {"title": "Health impact of the escalation of conflict in the Middle East", "url": "https://www.who.int/news-room/feature-stories/detail/health-
impact-of-the-escalation-of-conflict-in-the-middle-east", "snippet": "NOTE: In his introductory remarks at the media briefing on 5 March 2026, the Director-General said that an estimated 100 000
people have left Iran. The text below has been corrected to show that an estimated 100 000 people have left the city of Tehran, not Iran.\n________________________\nWHO is concerned over the expansion
of the conflict in the Middle East which is putting health systems and lives at risk in the region and beyond.\nAt a press conference earlier today, Dr Tedros Adhanom Ghebreyesu", "api_data": null,
"hint": null}, {"title": "WHO EMRO - Conflict deepens health crisis across Middle East, WHO says", "url": "https://www.emro.who.int/media/news/conflict-deepens-health-crisis-across-middle-east-who-
says.html", "snippet": "![WHO Representative and team in Lebanon visit a shelter housing internally displaced people, run by health partner Caritas Lebanon](/images/stories/media/WHO-Representative-
and-team-in-Lebanon-visit-a-shelter-housing-internally-displaced-people-3.jpg)\nCairo/Geneva, 11 March 2026 \u2014 More than ten days into the latest escalation of conflict in the Middle East, health
systems across the Region are coming under strain as injuries and displacement rise, attacks on health care continue, and public hea", "api_data": null, "hint": null}, {"title": "WHO EMRO - Update on
escalating conflict in the Eastern Mediterranean Region", "url": "https://www.emro.who.int/media/news/update-on-escalating-conflict-in-the-eastern-mediterranean-region.html", "snippet": "![Update on
the escalating conflict in the Middle East](/images/images/stories/media/Update_on_the_escalating_conflict_in_the_Middle_East.jpg)\n17 March 2026 \u2013 Conflict in the Middle East continues to
escalate, unfolding a multi-layered public health emergency. Increasing numbers of deaths and injuries are being reported, with over 1,440 deaths and more than 18,700 injuries reported in Iran, and
more than 886 deaths and 2105 injuries in Lebanon. Displacement is also rising rapidly, with over 945,", "api_data": null, "hint": null}, {"title": "Why the Middle East crisis demands a global health
response | Arab News PK", "url": "https://www.arabnews.pk/node/2638434", "snippet": "Why the Middle East crisis demands a global health response\n![Under international law, health facilities and
personnel are protected. Yet these protections are being repeatedly violated -AFP Under international law, health facilities and personnel are protected. Yet these protections are being repeatedly
violated -AFP](https://www.arabnews.pk/sites/default/files/styles/n_670_395/public/main-image/opinion/2026/04/01/afp_20260201_94qg73n_v2_highres_palestinianisraelconflict_1.jpg?itok=BuOMdHAY)\nht",
"api_data": null, "hint": null}, {"title": "Iran News in Brief \u2013 March 15, 2026 - NCRI", "url": "https://www.ncr-iran.org/en/news/iran-news-in-brief-news/iran-news-in-brief-march-15-2026/",
"snippet": "![Supporters of the NCRI as well as other political and ethnic groups held a major rally in Hamburg, Germany, on March 14, 2026](https://www.ncr-iran.org/en/wp-
content/uploads/2026/03/iranian-resistance-hamburg-rally-14032026.jpg)\nTHIS PAGE WILL BE UPDATED WITH THE LATEST NEWS\nUPDATE: 08:00 PM CET\nIran\u2019s War Enters a New Domestic Phase as Strikes Hit
Security Sites, Checkpoints and Cities Across the Country\nIran entered the sixteenth day of war with the battlefield pressing deeper into the count", "api_data": null, "hint": null}, {"title": "WHO
warns war in Iran will lead to regional instability, public health crises | CIDRAP", "url": "https://www.cidrap.umn.edu/public-health/who-warns-war-iran-will-lead-regional-instability-public-health-
crises", "snippet": "![WHO badge](/sites/default/files/who.jpg)\nThe World Health Organization (WHO) is warning that the war in Iran is worsening public health conditions across [the Middle East
region. ](https://www.emro.who.int/media/news/conflict-deepens-health-crisis-across-middle-east-who-says.html)\nAfter 10 days of bombings and conflict in Iran, national health authorities in Iran
report more than 1,300 deaths and 9,000 injuries, and Lebanon reports at least 570 deaths and more than 1,400 injuries. In Israel, a", "api_data": null, "hint": null}, {"title": "A Humanitarian Off-
Ramp for the Iran War | Think Global Health", "url": "https://www.thinkglobalhealth.org/article/a-humanitarian-off-ramp-for-the-iran-war", "snippet": "On February 28, 2026, the United States launched
a large-scale offensive against Iran, which could precipitate severe humanitarian consequences. Conflict shatters health systems first. Violence can cause vaccination programs to collapse, maternal
and child health care to suffer, and chronic illnesses to go untreated. Emergency response capacity erodes quickly.\nSince the beginning of the conflict, 18 attacks against health-care sites have
occurred in Iran [as of March 11](https://www.who.int/news", "api_data": null, "hint": null}, {"title": "Islamic Republic of Iran Country Overview | World Health Organization", "url":
"https://www.who.int/countries/irn", "snippet": "![Country presence banner Country presence banner](https://cdn.who.int/media/images/default-source/cover-images/decorative-images/who-cpr-2025-cp-
banner.png?sfvrsn=730ecc69_5)\nNews and features\nCountry profiles\nHealth profiles\nCountry profiles present selected data, statistics and information to provide national health profiles at given
points in time.\nPublications\n2 July 2024\nSurveillance and control of Anopheles stephensi\nAnopheles stephensi is an invasive mosquito species which has been found", "api_data": null, "hint": null},
{"title": "These are the casualties and cost of the war in Iran 2 weeks into the conflict", "url": "https://www.npr.org/2026/03/14/nx-s1-5746623/iran-war-cost-deaths", "snippet": "These are the
casualties and cost of the war in Iran 2 weeks into the conflict\n![An Iranian flag is planted in the rubble of a police station, damaged in airstrikes on March 3, 2026 in Tehran,
Iran.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/6000x4000+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2Feb%2Fc1%2F87607f514265b07679bfc8446568%2Fgettyimages-2263990208.jpg)\nAn Iranian flag is planted in the rubble of a police station, damaged", "api_data": null, "hint":
null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://reliefweb.int/report/iran-islamic-republic/middle-east-escalation-conflict-global-external-situation-report-1-26-march-2026",
  "prompt": "Does this WHO situation report mention the WHO Health Emergency Dashboard or WHO emergency grading for Iran? What is the WHO's emergency classification or grading for the Iran crisis?"
}
```

### 📋 Result

```
{"url": "https://reliefweb.int/report/iran-islamic-republic/middle-east-escalation-conflict-global-external-situation-report-1-26-march-2026", "content": "Based on the provided content, **no**, this
WHO situation report does not mention the WHO Health Emergency Dashboard or any WHO emergency grading for Iran. The document does not specify a WHO emergency classification or grading for the Iran
crisis.\n\nThe report focuses on describing acute health threats and risks across the affected Middle East region, including Iran, but does not include any formal emergency classification or grading
system.\n\nRelevant links:\nNone found in the provided content.", "title": "WHO Global External Situation Report #1: Middle East Escalation of Conflict (26 March 2026) - Iran (Islamic Republic of)"}
```

```json
{
  "query": "WHO emergency grading \"Grade 3\" OR \"Grade 2\" Iran 2026"
}
```

### 📋 Result

```
{"query": "WHO emergency grading \"Grade 3\" OR \"Grade 2\" Iran 2026", "results": [{"title": "Grading", "url": "https://www.who.int/emergencies/grading", "snippet": "Grading\nWHO grading of public
health events and emergencies\nThe world faces an increasing number of emergencies with health consequences from all hazards, including infectious disease outbreaks, conflicts, natural disasters,
chemical or radio-nuclear spills and food contamination.\nMany emergencies can be complex, with more than one cause, and can have significant public health, social, economic and political impacts. WHO
has specific responsibilities and accountabilities for emergency operations", "api_data": null, "hint": null}, {"title": "Table 2 WHO health emergencies programme grade classification Ungraded...",
"url": "https://www.researchgate.net/figure/WHO-health-emergencies-programme-grade-classification-Ungraded-An-event-that-is-being_tbl1_328219897", "snippet": null, "api_data": null, "hint": null},
{"title": "Emergency grade* Grade 3 / Protracted 3 \u00a9 WHO 2022. All rights reserved.", "url": "https://cdn.who.int/media/docs/default-source/documents/emergencies/who_ghea-2022_grade3-emergencies-
map.pdf?sfvrsn=7215a303_7", "snippet": null, "api_data": null, "hint": null}, {"title": "What is WHO grading of emergencies", "url": "https://www.linkedin.com/pulse/what-who-grading-emergencies-jorge-
castilla-echenique-daktari-", "snippet": "What is WHO grading of emergencies\nI've got this question several times so here it goes:\nWhat does it mean to be graded 2\nGrade 2: a single or multiple
country event with moderate public health consequences that requires a moderate WCO response and/or moderate international WHO response. Organizational and/or external support required by the WCO is
moderate. An Emergency Support Team, run out of the regional office, coordinates the provision of support to the WCO.\nWhat criteria or factors have d", "api_data": null, "hint": null}, {"title":
"Grading System in Iran", "url": "https://www.scholaro.com/db/countries/Iran/Grading-System", "snippet": "Grading System in Iran\nGrading scales:\nMost Common\nPassing Grade 10| Grade | Scale | US
Grade |\n|---|---|---|\n| A+ | 18.000 - 20.000 | A+ |\n| A | 17.000 - 17.990 | A |\n| B | 14.000 - 16.990 | B |\n| C | 12.000 - 13.990 | C |\n| D | 10.000 - 11.990 | D |\n| F | 0.000 - 9.990 | F
|\nInternational Baccalaureate Diploma\n| Scale | US Grade |\n|---|---|\n| 6.000 - 7.000 | A |\n| 5.000 - 5.990 | B |\n| 4.000 - 4.990 | C |\n| 3.000 - 3.990 | D |\n| 1.000 - 2.990 | F |\n| 0.000 -
0.990 | F |\nMost Common II\nPassing ", "api_data": null, "hint": null}, {"title": "WHO EMRO - Countries in crisis", "url": "https://www.emro.who.int/eha/countries-in-crisis/index.html", "snippet":
"Countries in crisis\nCountries in crisis\n![Countries in crisis Countries in crisis](/images/stories/eha/countries-in-criris.jpg)\nThe Eastern Mediterranean Region is facing an unprecedented scale of
emergencies, mainly as a result of political conflict in a number of countries. More than 62 million people affected across the Region are in need of health care as a result.\nAlmost 30 million
displaced people \u2013 more than half of all displaced persons globally \u2013 originate from the Region. The Region al", "api_data": null, "hint": null}, {"title": "WHO Grade 3 and Grade 2
Emergencies, Countries Covered by a WHO or Joint Appeal, and WHE Priority Countries - WHO Report - Question of Palestine", "url": "https://www.un.org/unispal/document/who-grade-3-and-
grade-2-emergencies-countries-covered-by-a-who-or-joint-appeal-and-whe-priority-countries-who-report/", "snippet": "Download Document Files:\nDocument Type:\nDocument Sources:\nSubject:\nPublication
Date: 24/05/2017\nURL source:\n[https://www.un.org/unispal/wp-content/uploads/2017/10/WHOContri_2017.pdf](https://www.un.org/unispal/wp-content/uploads/2017/10/WHOContri_2017.pdf)Document
Type:\n[Appeal](https://www.un.org/unispal/document-category/appeal/),[Report](https://www.un.org/unispal/document-category/report/)Document Sources:\n[World Health Organization
(WHO)](https://www.un.org/unispal/document-source/world-hea", "api_data": null, "hint": null}, {"title": "Academic grading in Iran - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Academic_grading_in_Iran", "snippet": "The Iranian grading system is similar to France's and other French-patterned grading systems such as Belgium, Lebanon, Venezuela,
and Peru in secondary schools and universities. Since a grading guideline is not provided by the Iranian Ministry of Education, conversion to the international scales is carried out using conversion
guideline provided for French-patterned grading systems. In specific cases, grades are converted according to the destination institutes' grading policy. The passing grade", "api_data": {"content":
[{"type": "text", "text": "{\"title\": \"Academic grading in Iran\", \"url\": \"https://en.wikipedia.org/wiki/Academic_grading_in_Iran\", \"extract\": \"The Iranian grading system is similar to
France's and other French-patterned grading systems such as Belgium, Lebanon, Venezuela, and Peru in secondary schools and universities. Since a grading guideline is not provided by the Iranian
Ministry of Education, conversion to the international scales is carried out using conversion guideline provided for French-patterned grading systems. In specific cases, grades are converted according
to the destination institutes' grading policy. The passing grade is 10 and usually a grade of more than 14 out of 20 is considered excellent. The following table is most commonly used by world
institutes and universities to convert from the Iranian grading system:\\n\\nThe above table does not corroborate with the scale most U.S. and Canadian institutions use where a grade between 16 and 20
scale to an \\\"A,\\\" 14\\u201316 scale to a \\\"B,\\\" 12\\u201314 scale to a \\\"C,\\\" a grade between 10 and 11 is treated as a \\\"D,\\\" and a score below 10 is considered a failing
grade.\\nThe above is also noted in the Scholaro Database.\\n\\nGradings in some universities might be different, for example in the Islamic Azad University, Grades from 17-20 is known to be \\\"Upper
Class Honors\\\" or A.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Using GRADE in situations of emergencies and urgencies: certainty in evidence and recommendations matters during the
COVID-19 pandemic, now more than ever and no matter what - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/32512187/", "snippet": "Using GRADE in situations of emergencies and urgencies: certainty in
evidence and recommendations matters during the COVID-19 pandemic, now more than ever and no matter what\n- PMID: 32512187\n-\nPMCID:\n[PMC7274969](https://pmc.ncbi.nlm.nih.gov/articles/PMC7274969/)
-\nDOI:\n[10.1016/j.jclinepi.2020.05.030](https://doi.org/10.1016/j.jclinepi.2020.05.030)\nUsing GRADE in situations of emergencies and urgencies: certainty in evidence and recommendations matters
during the COVID-19 pandemic, now more tha", "api_data": null, "hint": null}, {"title": "Primary and Secondary Education in Iran | Grade conversion scale for Iran", "url":
"https://www.evaluationworld.com/school-education-systems/iran.html", "snippet": null, "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.who.int/emergencies/grading",
  "prompt": "What events are currently graded? Is Iran or the Middle East conflict listed as a graded emergency? List all currently graded emergencies."
}
```

### 📋 Result

```
{"url": "https://www.who.int/emergencies/grading", "content": "Based on the provided content, **no currently graded emergencies are listed**. \n\nThe text describes WHO's emergency grading system,
including:\n- The purpose and process of grading\n- The three grade levels (Grade 1, 2, and 3, plus \"Ungraded\")\n- Criteria and timing for grading\n- What each grade level means\n\nHowever, the
content does **not provide a list of actual current emergencies** or their grades. There is no mention of Iran, the Middle East conflict, or any other specific ongoing graded emergencies.\n\nTo find
currently graded emergencies, you would need to access a different page on the WHO website that lists active emergencies and their current grade classifications.\n\n**Relevant links:**\n\nThe provided
content does not contain any clickable links to other pages that would show currently graded emergencies. You may need to navigate to WHO's emergency response pages or situation reports to find that
information.", "title": "Grading"}
```

```json
{
  "query": "WHO graded emergencies list 2026 current Iran Middle East conflict"
}
```

### 📋 Result

```
{"query": "WHO graded emergencies list 2026 current Iran Middle East conflict", "results": [{"title": "WHO EMRO - Middle East conflict", "url": "https://www.emro.who.int/emergencies/middle-east-
conflict/", "snippet": "Middle East conflict\nThe current escalation of conflict is affecting 21 countries globally, including 14 countries in the Eastern Mediterranean Region, raising significant
humanitarian and public health concerns.\nThe most severe health impacts have been reported in the Islamic Republic of Iran and Lebanon where hundreds of deaths and thousands of injuries have placed
immense pressure on hospitals and trauma care services.\nPopulation displacement is increasing, particularly in the Islamic Republi", "api_data": null, "hint": null}, {"title": "Iran | International
Crisis Group", "url": "https://www.crisisgroup.org/middle-east-north-africa/gulf-and-arabian-peninsula/iran", "snippet": null, "api_data": null, "hint": null}, {"title": "Health impact of the
escalation of conflict in the Middle East", "url": "https://www.who.int/news-room/feature-stories/detail/health-impact-of-the-escalation-of-conflict-in-the-middle-east", "snippet": "NOTE: In his
introductory remarks at the media briefing on 5 March 2026, the Director-General said that an estimated 100 000 people have left Iran. The text below has been corrected to show that an estimated 100
000 people have left the city of Tehran, not Iran.\n________________________\nWHO is concerned over the expansion of the conflict in the Middle East which is putting health systems and lives at risk
in the region and beyond.\nAt a press conference earlier today, Dr Tedros Adhanom Ghebreyesu", "api_data": null, "hint": null}, {"title": "Middle East Special Issue: March 2026 | ACLED", "url":
"https://acleddata.com/update/middle-east-special-issue-march-2026", "snippet": "![luca nevola](/sites/default/files/styles/logo/public/2025-07/luca-nevola-edit_0.jpg?itok=LU1JK0Ou)\n[Monthly regional
updates](https://acleddata.com/series/monthly-regional-updates)Update\nMiddle East Special Issue: March 2026\nACLED experts unpack the evolution of the US-Israeli war with Iran and its escalation
throughout the Middle East.\nUS-Israeli strikes on Iran on 28 February triggered a full-scale war that quickly escalated across the Middle East and set off a chain of global repercussions ",
"api_data": null, "hint": null}, {"title": "2026 Iran war - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Iran_war", "snippet": "On 28 February 2026, the United States and Israel started a
war with surprise airstrikes on sites and cities across Iran, assassinating Supreme Leader Ali Khamenei and several other Iranian officials and inflicting dozens of civilian casualties. Iran responded
with missile and drone strikes against Israel, US bases, and US-allied countries in the Middle East, and by closing the Strait of Hormuz.\nAfter the Middle Eastern crisis began in 2023, Iran and
Israel exchanged missile strikes in 2024, and", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Iran war\", \"url\": \"https://en.wikipedia.org/wiki/2026_Iran_war\", \"extract\":
\"On 28 February 2026, the United States and Israel started a war with surprise airstrikes on sites and cities across Iran, assassinating Supreme Leader Ali Khamenei and several other Iranian
officials and inflicting dozens of civilian casualties. Iran responded with missile and drone strikes against Israel, US bases, and US-allied countries in the Middle East, and by closing the Strait of
Hormuz.\\nAfter the Middle Eastern crisis began in 2023, Iran and Israel exchanged missile strikes in 2024, and Israel and the US launched airstrikes against Iran in the Twelve-Day War in June 2025.
In January 2026, Iranian security forces killed thousands of protesters in their crackdown of the largest Iranian protests since the 1979 Islamic Revolution. US president Donald Trump responded by
threatening military action against Iran and launching the largest US military buildup in the region since the US-led 2003 invasion of Iraq. In mid-February, the US and Iran began a new round of
indirect nuclear negotiations.\\nThe surprise US-Israeli attack, launched during the nuclear negotiations, killed Khamenei, other Iranian officials, and civilians. Subsequent attacks damaged military
bases, government facilities, schools, hospitals, and cultural heritage sites. In retaliation, Iran launched hundreds of drones and ballistic missiles at targets in Israel and at US military bases in
Bahrain, Jordan, Kuwait, Qatar, Saudi Arabia, and the United Arab Emirates. A drone struck Britain's Akrotiri military base on Cyprus, and missiles were shot down over Turkey. Other strikes hit
civilian infrastructure including in Azerbaijan, Kurdistan, and Oman. Iran denied striking Azerbaijan, Oman, and Turkey, saying they were false-flag attacks. Two ballistic missiles were reportedly
launched at Diego Garcia military base on the Chagos Islands, which Iran also denied. The conflict between Hezbollah and Israel escalated into the 2026 Lebanon war, killing more than 1,000 militants
and civilians by late March.\\nTrump administration officials have offered diverse and changing explanations for starting the war, such as to pre-empt Iranian retaliation against US assets after an
expected Israeli attack on Iran, to ward off an imminent Iranian threat, to destroy Iran's missile and military capabilities, to prevent Iran obtaining a nuclear weapon, to secure Iran's oil
resources, and to achieve regime change by bringing the Iranian opposition to power. Iranian and some US officials rejected claims that Iran had been preparing an attack. The International Atomic
Energy Agency said that while Iran has an \\\"ambitious\\\" nuclear program and has refused to allow inspections of its damaged sites since the 2025 war, there was no evidence of a structured nuclear
weapons program when the 2026 war began. UN secretary-general Antonio Guterres and several uninvolved countries condemned the US\\u2013Israeli strikes; the United Nations Security Council later passed
a resolution condemning Iran's retaliatory strikes on the Gulf states. Critics of the war, including legal and international relations experts, have described the attacks as illegal under US law, an
act of imperialism and a violation of Iran's sovereignty under international law.\\nThe war's economic impact, described as the world's largest supply disruption since the 1970s energy crisis,
includes surges in oil and gas prices, wide disruptions in aviation and tourism, and volatility in financial markets. Oil and gas shipments were disrupted when Iran closed the Strait of Hormuz and
Israel and Iran attacked energy facilities. On 19 March, the cost of the war to the US military was estimated at US$18 billion, and the Pentagon requested an additional US$200 billion.\", \"mode\":
\"full\"}"}]}, "hint": null}, {"title": "Conflict deepens health crisis across Middle East, WHO says", "url": "https://www.who.int/news/item/11-03-2026-conflict-deepens-health-crisis-across-middle-
east--who-says", "snippet": "More than ten days into the latest escalation of conflict in the Middle East, health systems across the Region are coming under strain as injuries and displacement rise,
attacks on health care continue, and public health risks increase.\nNational health authorities in Iran report more than 1300 deaths and 9000 injuries, and in Lebanon report at least 570 deaths and
more than 1400 injuries. In Israel, authorities report 15 deaths and 2142 injuries.\nAt the same time, the conflict is affecting the v", "api_data": null, "hint": null}, {"title": "US-Israel strikes
on Iran: February/March 2026", "url": "https://researchbriefings.files.parliament.uk/documents/CBP-10521/CBP-10521.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Emergency Meeting
on the Military Escalation in the Middle East : What's In Blue : Security Council Report", "url": "https://www.securitycouncilreport.org/whatsinblue/2026/02/emergency-meeting-on-the-military-
escalation-in-the-middle-east.php", "snippet": "Emergency Meeting on the Military Escalation in the Middle East\nToday (28 February) at 4 pm EST, the Security Council will convene for an emergency
briefing under the agenda item \u201cThe situation in the Middle East\u201d to discuss the US-Israeli attacks on [Iran](https://www.securitycouncilreport.org/iran/) earlier today and the retaliatory
strikes by Iran on Israel and US bases in several other countries in the region.\nThis morning, several Council members requested the Council to convene to discuss ", "api_data": null, "hint": null},
{"title": "Middle East Conflict: Situational Updates and Implications for Global Mobility | Newland Chase", "url": "https://newlandchase.com/middle-east-crisis-situation-update/", "snippet": "![Strait
of Hormuz](https://newlandchase.com/wp-content/uploads/2026/03/alerts-42-1027x720-c-default.jpg)\n| First Issued: | March 4, 2026 (Day 5 of Active Conflict) |\n| Last Updated: | April 1, 2026 |\n|
Conflict Start: | February 28, 2026 |\n| Status: | CRITICAL \u2014 Active Multi-Front Armed Conflict |\n| Audience: | Corporate Mobility Managers, HR Leaders, Global General Counsels |\n| Prepared By:
| Newland Chase Global Crisis Response Team |\n\u26a0\ufe0f CRITICAL NOTICE \u2014 THIS IS AN ACTIVE WAR ZONE \u2013 The Midd", "api_data": null, "hint": null}, {"title": "Iran: What challenges face
the country in 2026? - House of Commons Library", "url": "https://commonslibrary.parliament.uk/research-briefings/cbp-10456/", "snippet": null, "api_data": null, "hint": null}, {"title": "Grading",
"url": "https://www.who.int/emergencies/grading", "snippet": "Grading\nWHO grading of public health events and emergencies\nThe world faces an increasing number of emergencies with health consequences
from all hazards, including infectious disease outbreaks, conflicts, natural disasters, chemical or radio-nuclear spills and food contamination.\nMany emergencies can be complex, with more than one
cause, and can have significant public health, social, economic and political impacts. WHO has specific responsibilities and accountabilities for emergency operations", "api_data": null, "hint":
null}, {"title": "Global Public Health Emergencies - Public Health - MSK Library Guides at Memorial Sloan Kettering Cancer Center", "url": "https://libguides.mskcc.org/publichealth/PHEIC", "snippet":
"The [International Health Regulations (IHR) 2005](https://www.who.int/health-topics/international-health-regulations) are an instrument of international law that is legally-binding on 196 countries,
including the 194 WHO Member States, to build the capability to detect and report potential public health emergencies worldwide. IHR require that all countries have the ability to detect, assess,
report, and respond to public health events.\nThe IHR grew out of the response to deadly epidemics that on", "api_data": null, "hint": null}, {"title": "Emergency grade* Grade 3 / Protracted 3 \u00a9
WHO 2022. All rights reserved.", "url": "https://cdn.who.int/media/docs/default-source/documents/emergencies/who_ghea-2022_grade3-emergencies-map.pdf?sfvrsn=7215a303_7", "snippet": null, "api_data":
null, "hint": null}, {"title": "International Health Regulations | National Notifiable Diseases Surveillance System (NNDSS) | CDC", "url": "https://www.cdc.gov/nndss/what-is-case-
surveillance/international-health-regulations.html", "snippet": null, "api_data": null, "hint": null}, {"title": "Public Health Emergencies - Public Health - MSK Library Guides at Memorial Sloan
Kettering Cancer Center", "url": "https://libguides.mskcc.org/publichealth/PHemergencies", "snippet": "A public health emergency (also called a public health crisis) is a complex or difficult
situation that affects health systems in one or more geographic areas or from a single locality that has spread globally. It can result from disease (Covid-19, HIV/AIDS), natural disaster
(earthquakes, extreme weather), industry (oil spills, lead paint), or policy (housing, war).\nMany different governing bodies can declare public health emergencies, at the global level, national
level, state level, and even ", "api_data": null, "hint": null}, {"title": "WHO health emergencies programme grade classification Ungraded An event... | Download Table", "url":
"https://www.researchgate.net/figure/WHO-health-emergencies-programme-grade-classification-Ungraded-An-event-that-is-being_tbl1_328219897", "snippet": null, "api_data": null, "hint": null}, {"title":
"What is WHO grading of emergencies", "url": "https://www.linkedin.com/pulse/what-who-grading-emergencies-jorge-castilla-echenique-daktari-", "snippet": "What is WHO grading of emergencies\nI've got
this question several times so here it goes:\nWhat does it mean to be graded 2\nGrade 2: a single or multiple country event with moderate public health consequences that requires a moderate WCO
response and/or moderate international WHO response. Organizational and/or external support required by the WCO is moderate. An Emergency Support Team, run out of the regional office, coordinates the
provision of support to the WCO.\nWhat criteria or factors have d", "api_data": null, "hint": null}, {"title": "Quantitative evaluation of China\u2019s public health emergencies response policies: a
PMC index model approach - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11752722/", "snippet": "Abstract\nBackground\nIn recent years, public health emergencies, such as the COVID-19
pandemic and Ebola outbreaks, have occurred with increasing frequency worldwide, posing significant threats to global public health security. Policies serve as the foundation and institutional
framework for effective emergency responses. Consequently, evaluating and optimizing the formulation and implementation of Public Health Emergency Response Policies (PHERPs) to enhance emergency
response capacities has bec", "api_data": null, "hint": null}, {"title": "What is a Global Health Emergency and Who should decide? Africa CDC\u2019s declaration of a \u201cPublic Health Emergency of
Continental Security\u201d in a Crisis-Ridden World | American Journal of International Law | Cambridge Core", "url": "https://www.cambridge.org/core/journals/american-journal-of-international-
law/article/what-is-a-global-health-emergency-and-who-should-decide-africa-cdcs-declaration-of-a-public-health-emergency-of-continental-security-in-a-crisisridden-
world/2207D8C19685F30408B3D3A5C0CF5291", "snippet": "Introduction\nOn August 14, 2024, the upsurge of mpox across more than a dozen African countries was declared a public health emergency of
international concern (PHEIC).[Footnote\n1\n](https://www.cambridge.org#fn1) As is often the case, the World Health Organization\u2019s (WHO) director-general made this determination on the basis of
advice tendered by an expert committee convened under the International Health Regulations (IHR)\u2014the world\u2019s only international agreement on public health emergency preve", "api_data": null,
"hint": null}, {"title": "FAQs \u2022 What do the Emergency Classification Levels mean?", "url": "https://www.monroecounty-fl.gov/Faq.aspx?QID=263", "snippet": "Frequently Asked Questions\nBelow you
will find information that might help you understand how to find things or learn about information you might need to know about your city or town.\nTurkey Point\n9-\nTurkey Point\nAt Home:\nBring
children and pets indoors immediately, tune into the official TV/radio station, close and lock all doors & windows, turn off ventilation systems only if they draw in outside air, cover food/place it
in a refrigerator, move to interior room/basement\nIn a Vehicle\nIf you are", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.emro.who.int/emergencies/middle-east-conflict/",
  "prompt": "What is the WHO emergency classification or grading for the Middle East conflict? Is Iran specifically listed as a health event? Does this page reference the WHO Health Emergency Dashboard or the public emergency dashboard?"
}
```

### 📋 Result

```
{"url": "https://www.emro.who.int/emergencies/middle-east-conflict/", "content": "Based on the provided content:\n\n**WHO emergency classification/grading:** The text does not specify a formal WHO
emergency classification level (e.g., Grade 1, 2, or 3). It only mentions that \"WHO has activated its three-level Incident Management Support System.\"\n\n**Iran as a health event:** Yes, Iran is
specifically listed as experiencing severe health impacts. The content states: \"The most severe health impacts have been reported in the Islamic Republic of Iran and Lebanon where hundreds of deaths
and thousands of injuries have placed immense pressure on hospitals and trauma care services.\" Additionally, six hospitals were evacuated in Iran according to referenced interviews.\n\n**WHO
Dashboard references:** No. The content does not mention or reference the WHO Health Emergency Dashboard or any public emergency dashboard.\n\n---\n\n**Relevant links:**\n\n- [WHO situation report:
Middle East Escalation of Conflict - Number 4, 27 March\u20142 April 2026](https://www.emro.who.int/images/stories/eha/ME-Sitrep-4-2-April-26.pdf)\n- [WHO situation report: Middle East Escalation of
Conflict - Number 3, 26 March 2026](https://www.emro.who.int/images/stories/eha/ME-Sitrep-3-26-March-26.pdf)\n- [WHO situation report: Middle East Escalation of Conflict - Number 2, 18 March
2026](https://www.emro.who.int/images/stories/eha/ME-Sitrep-2-19-March-26.pdf)\n- [WHO launches US$30.3 million flash appeal to respond to escalating health crisis across the Middle
East](https://www.emro.who.int/media/news/who-launches-us-30-3-million-flash-appeal-to-respond-to-escalating-health-crisis-across-the-middle-east.html)\n- [Update on escalating conflict in the Eastern
Mediterranean Region](https://www.emro.who.int/media/news/update-on-escalating-conflict-in-the-eastern-mediterranean-region.html)", "title": "Middle East conflict"}
```

```json
{
  "query": "\"extranet.who.int/publicemergency\" Iran event listed"
}
```

### 📋 Result

```
{"query": "\"extranet.who.int/publicemergency\" Iran event listed", "results": [{"title": "WHO Health Emergency Dashboard - Extranet Systems", "url": "https://extranet.who.int/publicemergency/",
"snippet": "The World Health Organization (WHO) Health Emergency Dashboard is a platform which aims to share information about public health events and emergencies. The data on the dashboard is
refreshed every thirty (30) minutes and data is accurate as at time of refreshing.\nThe WHO Health Emergency Dashboard is not a comprehensive representation of all the events and emergencies that WHO
is aware of and responding to. The events displayed are a subset of those reported through official channels as mandate", "api_data": null, "hint": null}, {"title": "Iran (Islamic Republic of) -
WHO/OMS: Extranet Systems", "url": "https://extranet.who.int/uhcpartnership/country-profile/iran-islamic-republic", "snippet": "Technical Areas\nFilter by\nCompleted/Cancelled activities\nOutcome 1.1
(GPW 13)\nOutput 1.1.1\nProduct/Service: Review and improve PHC for better function\nTechnical Area: Service Delivery\nDeliverables: Training of Stakeholders on PHCMI\nOutput 1.1.1\nProduct/Service:
Capacity Building on Primary Health Care Measurement & Improvement (PHCMI)\nTechnical Area: Service Delivery|Governance\nDeliverables: PHCMI Stakeholders Training Workshop conducted\nOutput
1.1.1\nProduct/Service: Scale up PHCMI in 10 selecte", "api_data": null, "hint": null}, {"title": "News | Iran site - WHO EMRO", "url": "https://www.emro.who.int/iran/news/index.html", "snippet": "WHO
in Islamic Republic of Iran\n[A global model for mental health: How the Iranian integrated care system is saving lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-
iranian-integrated-care-system-is-saving-lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali
Ghofrani Centre, psychiatrists, physicians, psychologists, dedicated social workers, and community voluntee", "api_data": null, "hint": null}, {"title": "WHO EMRO - Islamic Republic of Iran", "url":
"https://www.emro.who.int/countries/iran/home.html", "snippet": "WHO Representative for Islamic Republic of Iran\nDr Awad Mataria\nWHO Representative\nPO Box
14665-1565\nTehran\n11516\nemail:\n[{{{type}}}] {{{reason}}}\n{{/data.error.root_cause}}\n{{texts.summary}}\n{{#options.result.rssIcon}}\n[RSS](https://www.emro.who.int/{{{data.rssUrl}}})\n{{/options.
result.rssIcon}}\n{{{_source.displayDate}}}\n{{/_source.showDate}}{{{_source.description}}}\n{{#_source.additionalInfo}}{{#_source.additionalFields}} {{#title}} {{{label}}}: {{{title}}} {{/title}}
{{/_source.additionalFiel", "api_data": null, "hint": null}, {"title": "WHO in Islamic Republic of Iran", "url": "https://www.emro.who.int/iran/news/", "snippet": "WHO in Islamic Republic of Iran\n[A
global model for mental health: How the Iranian integrated care system is saving lives](https://www.emro.who.int/iran/news/a-global-model-for-mental-health-how-the-iranian-integrated-care-system-is-
saving-lives.html)\n23 February 2026 \u2013 In a south Tehran neighborhood, a quiet transformation in mental health care is unfolding. Inside the Shahid Mohammad Ali Ghofrani Centre, psychiatrists,
physicians, psychologists, dedicated social workers, and community voluntee", "api_data": null, "hint": null}, {"title": "Iran announces arrests, says US and Israel suffering \u2018defeats\u2019 | US-
Israel war on Iran News | Al Jazeera", "url": "https://www.aljazeera.com/amp/news/2026/3/18/iran-announces-arrests-says-us-and-israel-suffering", "snippet": "Iran announces arrests, says US and Israel
suffering \u2018defeats\u2019\nHundreds have been arrested as Iran cracks down on 'traitors' following killing of Larijani, Soleimani.\nIranian authorities have announced hundreds more arrests across
the country, as well as operations to counter what they describe as \u201ctraitors\u201d aligned with the interests of the United States and Israel.\nThe Ministry of Intelligence said in a statement
that 111 \u201cpro-monarchy cells\u201d in 26 of Iran\u2019s 31 provinces were stopped overnight", "api_data": null, "hint": null}, {"title": "WHO EMRO | Home | Iran site | Countries", "url":
"https://www.emro.who.int/countries/iran/index.html", "snippet": "This page cannot be found\nThe page or file you are trying to access cannot be found. This is because the web address is incorrect or
the file has been moved or deleted.\nPlease try the following:\n- Return to the\n[WHO home page](https://www.emro.who.int/index.php). - Check that the web address is correct.\n- Search the WHO website
using the search box at the top.\n- If you still encounter problems, please report these by\n[contacting us](https://www.emro.who.int/contact-us.html).", "api_data": null, "hint": null}, {"title":
"Report on documentation and evaluation of Urban HEART pilot in Tehran,", "url": "https://extranet.who.int/kobe_centre/sites/default/files/pdf/Iran.pdf", "snippet": null, "api_data": null, "hint":
null}, {"title": "Iran\u2019s War With Israel and the United States | Global Conflict Tracker", "url": "https://www.cfr.org/global-conflict-tracker/conflict/confrontation-between-united-states-and-
iran", "snippet": "On February 28, the United States and Israel [attacked Iran](https://www.cfr.org/articles/gauging-the-impact-of-massive-u-s-israeli-strikes-on-iran) after weeks of military buildup
and threats from President Trump. Large-scale strikes targeted Iranian military assets and the Islamic Republic\u2019s top leadership, killing Supreme Leader Ayatollah Ali Khamenei. Tehran\u2019s
Assembly of Experts appointed Ali Khamenei\u2019s son, [Mojtaba Khamenei](https://www.cfr.org/articles/islamic-republics-power-centers), t", "api_data": null, "hint": null}, {"title": "SPAR - Iran
(islamic Republic Of) Submitted(2022) | Strategic Partnership for Health Security and Emergency Preparedness (SPH) Portal", "url": "https://extranet.who.int/sph/spar-iran-islamic-republic-
submitted2022", "snippet": "Region Eastern Mediterranean Region Country Iran (Islamic Republic of) Year 2022 Spar Status Submitted C1: Legislation and financing C1: Average Capacities Score(%) 100
C.1.1 Legislation, laws, regulations, policy, administrative requirements or other government instruments to implement the IHR ( 100 C.1.2 Financing for the implementation of IHR capacities 100 C2:
IHR Coordination And NFP Functions C2: Average Capacities Score(%) 93 C.2.1 NFP functions under IHR 100 C.2.2 Multi-sectoral IHR coor", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me synthesize what I've found and try to directly access the WHO dashboard to check for Iran events. Let me also check the latest WHO situation report for the Middle East conflict which was published just days ago.

Key findings so far:

1. **Active war in Iran** since Feb 28, 2026 - US-Israeli military strikes, massive casualties (1,300+ deaths, 9,000+ injuries as of March 11, growing over time)
2. **WHO is actively responding** - multiple situation reports, WHO Director-General press conferences, WHO EMRO has a dedicated "Middle East conflict" page


3. **WHO has activated its Incident Management Support System** and published at least 4 situation reports, with the most recent from late March/early April 2026, while also launching a $30.3 million flash appeal for the health crisis
4. **Verified healthcare attacks and major health impacts** - 18 attacks on Iranian healthcare facilities resulting in 8 deaths, alongside 1,300+ deaths, 18,700+ injuries, 100,000+ displaced persons, and toxic environmental exposure forcing hospital evacuations

Now I'm checking whether this information appears on the specific WHO Health Emergency Dashboard.

The dashboard displays events reported through official IHR channels and isn't meant to be comprehensive. While the WHO has clearly treated this as a major health emergency with activated incident management and multiple situation reports, the dashboard specifically focuses on disease outbreaks and health events reported through formal International Health Regulations channels, which may not capture conflict-related health emergencies in the same way.

Given the scale of this crisis—thousands of casualties, environmental contamination, attacks on healthcare, mass displacement, and a $30.3 million flash appeal—it would be surprising if it doesn't appear on the dashboard. Similar conflicts like Syria, Ukraine, and Gaza have been listed, and with nearly a month remaining before the resolution date, there's still time for it to be added if it hasn't been already.

Now I'm checking the latest situation reports and looking at comparable prediction market prices to get a clearer picture.

## 💬 Response

Let me check the latest WHO situation report and look for prediction market data.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.emro.who.int/images/stories/eha/ME-Sitrep-4-2-April-26.pdf",
  "prompt": "What is the WHO emergency classification or grading for the Iran/Middle East conflict? Does this report reference the WHO Health Emergency Dashboard? What health events are reported for Iran?"
}
```

### 📋 Result

```
{"format": "pdf", "url": "https://www.emro.who.int/images/stories/eha/ME-Sitrep-4-2-April-26.pdf", "pdf_path": "/home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/43046_20260403_073557/downloads/pdf/17766181367d.pdf", "hint": "PDF downloaded to /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/43046_20260403_073557/downloads/pdf/17766181367d.pdf. Use the Read tool to read the PDF content."}
```

## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "query": "WHO Iran health event"
}
```

### 📋 Result

```
{"markets": [], "query": "WHO Iran health event"}
```

## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "WHO Iran health event classified"
}
```

### 📋 Result

```
{"markets": [], "query": "WHO Iran health event classified"}
```

## 🔧 Tool: Read


```json
{
  "file_path": "/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/43046_20260403_073557/downloads/pdf/17766181367d.pdf"
}
```

### 📋 Result

```
PDF file read: /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/43046_20260403_073557/downloads/pdf/17766181367d.pdf (1.2MB)
```

## 💭 Thinking

Now I have extensive evidence. Let me synthesize what I know:

## Key Facts:

1. **Active war in Iran since February 28, 2026** - US-Israeli strikes on Iran, with massive health consequences
2. **As of April 2, 2026** (the day before this question was published):
   - Iran: 2,150 deaths, 27,931 injuries, 3.2 million displaced
   - 23 WHO-verified attacks on healthcare in Iran
   - 44 hospitals damaged, 212 health facilities damaged, 7 hospitals evacuated
   - 24 healthcare workers killed, 114 injured
   - Environmental contamination from burning oil facilities and destroyed desalination infrastructure, plus damage to the Khondab nuclear facility, with WHO's own Tehran office also struck

3. **WHO Response**:
   - WHO has activated its 3-level Incident Management Support System
   - WHO has published 4 situation reports on the Middle East conflict
   - WHO launched a $30.3 million flash appeal
   - WHO EMRO has a dedicated "Middle East conflict" emergency page
   - WHO Director-General has made multiple public statements
   - WHO Executive Director for Health Emergencies visited Lebanon

4. **The specific question**: Does the WHO Health Emergency Dashboard list an event for Iran?

The dashboard shows events reported through official IHR channels, though it's JavaScript-based and only represents a subset of all emergencies WHO is tracking. Given the scale of this crisis—massive casualties, displacement, healthcare attacks, environmental and CBRN risks affecting 21 countries—it would be virtually impossible for this not to appear on the dashboard, especially considering WHO's full activation of its incident management system and multiple situation reports.

The main uncertainties are whether the dashboard is limited to disease outbreaks rather than conflict-related emergencies, whether Iran has formally reported through IHR channels, or if there are technical/political barriers to listing it. With nearly 28 days until the May 1, 2026 deadline, there's still time for it to appear even if it's not currently visible. that exact URL lists the Iran conflict. The dashboard is described as showing events "reported through official channels as mandated by the International Health Regulations (IHR) (2005)." IHR events are typically disease outbreaks, but the IHR framework also covers "all hazards" including conflicts that pose public health risks.

Given that:
1. WHO is treating this as a major health emergency
2. The scale is enormous (2,150+ deaths, 27,931+ injuries in Iran alone)
3. WHO has activated its incident management system
4. WHO has published situation reports specifically about Iran
5. There are 28 days until the May 1 deadline
6. The conflict is ongoing and the health situation is worsening

I'd put the probability around 0.95 or higher. The remaining uncertainty mostly comes down to whether the dashboard actually tracks conflict-related events versus disease outbreaks, whether I can directly verify what's currently displayed, and potential political or bureaucratic obstacles that might delay reporting.

## 💬 Response

Now I have a comprehensive picture. Let me synthesize my findings and run the reflection.

The evidence is overwhelming: There is an active war in Iran since February 28, 2026, with massive health consequences that WHO is actively responding to. Let me assess the key question: whether this specifically appears on the WHO Health Emergency Dashboard.

## 💭 Thinking

The reviewer gave a WARN, which is fair. The main concern is that I couldn't verify whether the specific dashboard at extranet.who.int/publicemergency lists conflict-related events specifically, vs only disease outbreaks. Let me try to find more information about what types of events appear on this dashboard.

Let me also consider the reviewer's suggestion that 85-92% might be more appropriate. But I think the evidence is very strong - let me try to find what events are currently on this dashboard by looking for cached or archived versions, or finding documentation about what types of events it lists.

## 💬 Response

The reviewer raises a valid point about whether the specific dashboard lists conflict events. Let me try to verify this.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "WHO \"health emergency dashboard\" extranet publicemergency conflict events listed Ukraine Syria Gaza"
}
```

### 📋 Result

```
{"query": "WHO \"health emergency dashboard\" extranet publicemergency conflict events listed Ukraine Syria Gaza", "results": [{"title": "WHO Health Emergency Dashboard - Extranet Systems", "url":
"https://extranet.who.int/publicemergency/", "snippet": "The World Health Organization (WHO) Health Emergency Dashboard is a platform which aims to share information about public health events and
emergencies. The data on the dashboard is refreshed every thirty (30) minutes and data is accurate as at time of refreshing.\nThe WHO Health Emergency Dashboard is not a comprehensive representation
of all the events and emergencies that WHO is aware of and responding to. The events displayed are a subset of those reported through official channels as mandate", "api_data": null, "hint": null},
{"title": "Ukraine emergency", "url": "https://www.who.int/emergencies/situations/ukraine-emergency", "snippet": "WHO is working through our offices in Ukraine and neighboring countries, and with
partners, to respond to the health emergency triggered by the Russian Federation\u2019s invasion of Ukraine. We are delivering specialized medical supplies, coordinating the deployment of medical
teams, and working with health authorities to minimize disruptions to the delivery of critical healthcare services within Ukraine and in countries hosting refugees.\nWHO continues to deliver much-
needed support on urgent health ", "api_data": null, "hint": null}, {"title": "Situation reports (Ukraine-specific)", "url": "https://www.who.int/europe/emergencies/situations/ukraine-
emergency/situation-reports-(ukraine-specific)", "snippet": "Ukraine emergency situation reports (Ukraine-specific)\n[\n](https://www.who.int/europe/publications/i/item/WHO-
EURO-2024-5319-45083-75040)\nWar in Ukraine: situation report from WHO Country Office in Ukraine: issue No. 76, 21 June 2024\n[\n](https://www.who.int/europe/publications/i/item/WHO-
EURO-2024-5319-45083-74681)\nWar in Ukraine: situation report from WHO Country Office in Ukraine: issue No. 75, 30 May 2024\n[\n](https://www.who.int/europe/publications/i/item/WHO-
EURO-2024-5319-45083-74483)\nWar i", "api_data": null, "hint": null}, {"title": "WHO - List of emergencies", "url": "https://www.who.int/europe/emergencies/situations", "snippet": "Emergencies\nHealth
emergencies list\nThe health emergencies list details the disease outbreaks, disasters and humanitarian crises where WHO plays an essential role in supporting countries to respond to and recover from
emergencies with public health consequences.", "api_data": null, "hint": null}, {"title": "2024 emergency annual report: WHO\u2019s health response in Ukraine", "url":
"https://www.who.int/europe/news/item/05-08-2025-2024-emergency-annual-report--who-s-health-response-in-ukraine", "snippet": "In 2024, WHO reached 4.7 million people with essential health
services.\nThe WHO Country Office in Ukraine has released its 2024 annual report on health emergency operations, outlining efforts to sustain and strengthen health-care delivery despite the ongoing
war. These efforts include trauma response, outbreak prevention, mental health support, rehabilitation and primary health care \u2013 demonstrating that even in war, health systems can be
sustained.\nServing as the operational backbone for 114 hea", "api_data": null, "hint": null}, {"title": "Ukraine emergency situation reports (global)", "url":
"https://www.who.int/europe/emergencies/situations/ukraine-emergency/situation-reports-global", "snippet": "Emergencies\nUkraine emergency situation reports
(global)\n[\n](https://www.who.int/europe/publications/i/item/WHO-EURO-2024-5319-45083-74681)\nWar in Ukraine: situation report from WHO Country Office in Ukraine: issue No. 75, 30 May
2024\n[\n](https://www.who.int/europe/publications/i/item/WHO-EURO-2024-5319-45083-74483)\nWar in Ukraine: situation report from WHO Country Office in Ukraine: issue No. 74, 17 May
2024\n[\n](https://www.who.int/europe/publications/i/item/WHO-EURO-2024-5319-45083-74282)\nWar ", "api_data": null, "hint": null}, {"title": "Emergency in Ukraine: external situation report #8,
published 21 April 2022: reporting period: 14\u201320 April 2022", "url": "https://www.who.int/publications-detail-redirect/WHO-EURO-2022-5152-44915-64303", "snippet": "Emergency in Ukraine: external
situation report #8, published 21 April 2022: reporting period: 14\u201320 April 2022\n21 April 2022\n| Situation report\nOverview\nWeekly updates on the current situation in Ukraine and refugee-
receiving countries, priority public health concerns and WHO\u2019s actions to rapidly respond to the health emergency triggered by the conflict and to minimize disruptions to the delivery of critical
health services.", "api_data": null, "hint": null}, {"title": "World Health Organization Emergencies Programme", "url": "https://www.who.int/europe/emergencies/overview", "snippet": "![Mpox banner
Mpox](https://cdn.who.int/media/images/librariesprovider2/default-album/site-banner-images/situations/mpox-banner.jpg?sfvrsn=ca34fa55_2)\nOn 15 August 2024, Sweden became the first country outside the
African continent to confirm mpox clade Ib in an individual with travel history to central Africa. The confirmation of the case came just one day after WHO\u2019s Director-General declared mpox a
public health emergency of international concern (PHEIC) for the second time in 2 years, follow", "api_data": null, "hint": null}, {"title": "Early warning, alert and response to acute public health
events in refugee-hosting countries: Ukraine crisis", "url": "https://www.who.int/europe/publications/i/item/WHO-EURO-2022-5506-45271-64773", "snippet": "Early warning, alert and response to acute
public health events in refugee-hosting countries: Ukraine crisis\n![Early warning, alert and response to acute public health events in refugee-hosting countries: Ukraine
crisis](https://cdn.who.int/media/images/librariesprovider2/default-album/who-euro-2022-5506-45271-64773-eng.pdf.tmb-479v.jpg?sfvrsn=f24119b4_1)\nOverview\nThis document serves as an advocacy and
quick assessment tool for public health responders in refugee-hosting countries to evaluate a", "api_data": null, "hint": null}, {"title": "Stronger together - milestones that mattered in 2025",
"url": "https://www.who.int/news-room/spotlight/stronger-together-milestones-that-mattered-in-2025", "snippet": "Stronger together: milestones that mattered in 2025\nThe conclusion of discussions on
the Pandemic Agreement in Committee at the World Health Assembly 2025.\nLooking back on 2025, the year has been marked by immense achievements and profound challenges for global health. In the face of
major funding cuts and increasing threats to science and solidarity, WHO continued to lead and champion global efforts to confront the biggest health challenges of our time.\nFrom governments adopting
the world\u2019s fir", "api_data": null, "hint": null}]}
```

```json
{
  "query": "WHO Health Emergency Dashboard extranet publicemergency what events are listed types of events shown"
}
```

### 📋 Result

```
[{"title": "WHO Health Emergency Dashboard - Extranet Systems", "url": "https://extranet.who.int/publicemergency", "snippet": "WHO Health Emergency Dashboard \n\nLoading..\n\n \n\n \n\n;\n\n \n\n ;
\n\n ; \n\n ;\n\n0 Filters applied Filters CLEAR\n\nCountry / area Select All\n\n- Map\n\n- Monkeypox\n\n \n\nDownload\n\nLayers\n\n### Events\n\n# for Events (Size determines number of events)\n\n###
Attack On Health\n\n# for Attack On Health (Size determines number of Attack On Health)\n\n### HeRAMS\n\n# for HeRAMS (Size determines number of HeRams)\n\n### Map\n\nGrey areas on the map represent
territories for which there may not yet be full agreement.\n\nWe are no longe", "highlights": ["WHO Health Emergency Dashboard \n\nLoading..\n\n \n\n \n\n;\n\n \n\n ; \n\n ; \n\n ;\n\n0 Filters
applied Filters CLEAR Country / area Select All\n\n- Map\n\n- Monkeypox\n\n \n\nDownload\n\nLayers\n\n### Events # for Events (Size determines number of events)\n\n### Attack On Health # for Attack On
Health (Size determines number of Attack On Health)\n\n### HeRAMS # for HeRAMS (Size determines number of HeRams)\n\n### Map Grey areas on the map represent territories for which there may not yet be
full agreement. We are no longer showing monkeypox data in the emergency dashboard. For data related to monkeypox please use the global trends report News and Publications\n\n- Disease Outbreak
News\n- WHO Publications\n- Useful Links\n\n###### {{item.value1}} {{item.value2}}, {{item.value4}}\n\n###### {{item.value1}}\n\n###### {{item.value1}}\n\n{{item.value3}}, {{item.value5}} ######
{{item.value1}}\n\n{{item.value2}} - {{item.value4}}\n\n \n\n;\n\nSUMMARY\n\n### Number of Events\n\n69\n\nSOURCE ### Number of deaths on healthcare attacks\n\n2.6K\n\nSOURCE\n\nVIEW MORE >>\n\n###
Number of injuries on healthcare attacks 5.5K\n\nSOURCE\n\nVIEW MORE >>\n\n### Total number of healthcare attacks\n\n7.3K\n\nSOURCE\n\n;"], "published_date": null, "score": null}, {"title": "World
Health Organization Emergencies Programme", "url": "https://production-cms.platform.who.int/data/redirect-pages/megamenu/emergencies/health-emergency-dashboard", "snippet": "World Health Organization
Emergencies ProgrammeSkip to main content\n**\n**When autocomplete results are available use up and down arrows to review and enter to select.\n**Select languageSelect
languageEnglish\u0627\u0644\u0639\u0631\u0628\u064a\u0629\u4e2d\u6587Fran&#231;ais\u0420\u0443\u0441\u0441\u043a\u0438\u0439Espa&#241;ol**\nHome\n\n\n* All topics\n* A\n* B\n* C\n* D\n* E\n* F\n* G\n*
H\n* I\n* J\n* K\n* L\n* M\n* N\n* O\n* P\n* Q\n* R\n* S\n* T\n* U\n* V\n* W\n* X\n* Y\n* Z\n* Resources\n* Fact sheets\n* Facts in pictures\n* Multimedia\n* Podcasts\n* Publications\n* Questions and
answers\n* Tools and toolk", "highlights": ["World Health Organization Emergencies ProgrammeSkip to main content\n**   ...    * All topics\n* A\n* B\n* C\n* D\n* E\n* F\n* G\n* H\n* I\n* J\n* K\n*
L\n* M\n* N\n* O\n* P\n* Q\n* R\n* S\n* T\n* U\n* V\n* W\n* X\n* Y\n* Z   ...    * Strengthening country offices\u00a0\n* All news\n* News releases\n* Statements\n* Campaigns\n* Events\n* Feature
stories   ...    * Coronavirus disease (COVID-19)\n* Greater Horn of Africa\n* Israel and occupied Palestinian territory\n* Mpox\n* Sudan * Ukraine\n* Latest\n* Disease Outbreak News\n* Situation
reports\n* Rapid risk assessments\n* Weekly Epidemiological Record * WHO in emergencies\n* Surveillance\n* Alert and response\n* Operations\n* Research\n* Funding\n* Partners * Health emergency
appeals\n* International Health Regulations\n* Independent Oversight and Advisory Committee * Data at WHO\n* Data hub\n* Global Health Estimates\n* Mortality\n* Health inequality\n* Dashboards *
Triple Billion Progress\n* Health Inequality Monitor\n* Delivery for impact\n* COVID-19 dashboard\n* Data collection * Classifications\n* SCORE\n* Surveys\n* Civil registration and vital statistics\n*
Routine health information systems   ...    * External audit\n* Financial statements\n* Internal audit and investigations\u00a0\n* Programme Budget\n* Results reports * Governance\n* Governing
bodies\n* World Health Assembly\n* Executive Board\n* Member States Portal\nEmergencies OverviewFundingOperationsPartnersSurveillanceResearchTraining\nGlobal health emergencies\nAll \u2192 A crowd of
people milling around ambulances in a street \n### Conflict in Israel and the occupied Palestinian territory Nurse wearing mask holding vaccine vial and writing on a sheet of paper \n### Coronavirus
disease (COVID-19) ### Sudan Disease Outbreak News\nSituation reports\nWeekly Epidemiological Record\nHealth Emergency Dashboard Independent Oversight and Advisory Committee\nWHO's health emergency
appeals\n## Emergency news\nAll \u2192 22 August 2025\nJoint News Release\nFamine confirmed for first time in Gaza 30 July 2025\nDepartmental update\nPaying tribute to David Nabarro 29 July 2025\nNote
for Media\nIPC Gaza Strip Food Insecurity and Malnutrition Alert 27 July 2025\nNews release\nMalnutrition rates reach alarming levels in Gaza, WHO warns # Our emergency work in focus\nAll \u2192 4
September 2025\nStrengthening Vanuatu's health resilience with better data collection 13 August 2025\nGOARN impact in the field: Brazil implements Go.Data for enhanced contact tracing 8 July
2025\nStrengthening outbreak response in Vanuatu through Go.Data A health worker is administering oral polio vaccine to a child.\nFeatured meeting report|16 January 2025 ### WHO's Health Emergency
Appeal 2025 Download\nRead More\nPublications\nAll \u2192\nClinical management of COVID-19: living guideline, June 2025\n15 July 2025 ### Clinical management of COVID-19: living guideline, June 2025
The COVID-19 Clinical management: living guidance contains the most up-to-date WHO recommendations for the clinical   ...    ### Clinical characteristics of pregnant and nonpregnant women hospitalized
with suspected or confirmed COVID-19 Download\nRead More\nDocuments\nAll \u2192\nCholera sitrep 29\n28 August 2025 ### Multi-country outbreak of cholera, external situation report #29 -28 August 2025
From 1 January to 27 July 2025, a cumulative total of 382 718 cholera cases and 4478 deaths were reported from 31   ...    Download\nRead More\nMpox Situation Report #57 Thumbnail\n28 August 2025 ###
Multi-country outbreak of mpox, External situation report #57 - 28 August 2025 This is the 57th situation report for the multi-country outbreak of mpox, which provides details on the global   ...
28 August 2025\n### Public Health Situation Analysis - Afghanistan In 2025, an estimated 22.9 million people in Afghanistan \u2500nearly half of the country\u2019\u2019s 46 million   ...    26 August
2025\n### Public Health Situation Analysis - Cambodia - Conflict on Thai Border   ...    Download\nRead More\nMore about our work in emergencies Rapidly detecting and responding to health
emergencies\n\n\nStrengthening national emergency preparedness Tracking SARS-CoV-2 variants\n\n\nMinimizing health risks at airports, ports and ground crossings Communicating risk in public health
emergencies Supporting national implementation of International Health Regulations Building a skilled workforce to prepare for and respond to emergencies Managing environmental health risks in
emergencies\n\n\nTranslating science for better health emergency preparedness Strengthening the global health-security interface\n\n\nStrengthening partnerships with the faith community Safeguarding
biosafety and biosecurity in laboratories Measuring the effectiveness and"], "published_date": "2025-09-04T00:00:00.000", "score": null}, {"title": "WHO - Emergency situation reports", "url":
"https://platform.who.int/data/redirect-pages/megamenu/emergencies/latest/situation-reports", "snippet": "WHO - Emergency situation reports\n\nSkip to main content\n\nEmergencies\n\nOverview Funding
Operations Partners Surveillance Research Training\n\n# Emergency situation reports\n\nAll \u2192\n\nLatest WHO official reports for emergency situations.\n\n#### Public Health Situation...\n\n12
March 2026\n\n#### Public Health Situation...\n\n11 March 2026\n\n#### Public Health Situation...\n\n25 February 2026\n\n#### Public Health Situation...\n\n25 February 2026\n\n#### Multi-country
outbreak of...\n\n24 February 2026\n\n#### Multi-countr", "highlights": ["WHO - Emergency situation reports\n\nSkip to main content\n\nEmergencies Overview Funding Operations Partners Surveillance
Research Training\n\n# Emergency situation reports\n\nAll \u2192 Latest WHO official reports for emergency situations.\n\n#### Public Health Situation...\n\n12 March 2026 #### Public Health
Situation...\n\n11 March 2026\n\n#### Public Health Situation...\n\n25 February 2026 #### Public Health Situation...\n\n25 February 2026\n\n#### Multi-country outbreak of...\n\n24 February 2026 ####
Multi-country outbreak of...\n\n21 February 2026\n\n#### Multi-country outbreak of...\n\n27 January 2026 #### Multi-country outbreak of...\n\n23 January 2026\n\n#### Public Health Situation...\n\n5
January 2026 #### Public Health Situation...\n\n23 December 2025\n\n## Related emergency content\n\nEmergency list\n\nDisease Outbreak News Travel advice\n\nWeekly Epidemiological Record\n\nGet the
latest Emergency situation reports\n\nSubscribe"], "published_date": "2025-09-10T00:00:00.000", "score": null}, {"title": "WHO Health Emergency Dashboard", "url":
"https://repository.gheli.harvard.edu/repository/14284/", "snippet": "WHO Health Emergency DashboardSkip to Main Content\n**\n**\nHome logo\nHOME&#47;RESOURCES&#47;\n# WHO Health Emergency
Dashboard\n2024\nThis data portal from the World Health Organization (WHO) provides a comprehensive data dashboard about worldwide public health events and emergencies. The dashboard includes a
snapshot of all of the public health emergencies and events that the WHO is responding to, with data updated by the hour. Users can explore a visual world map that displays health emergencies an",
"highlights": ["WHO Health Emergency DashboardSkip to Main Content\n**\n**\nHome logo\nHOME/RESOURCES/ # WHO Health Emergency Dashboard\n2024 This data portal from the World Health Organization (WHO)
provides a comprehensive data dashboard about worldwide public health events and emergencies. The dashboard includes a snapshot of all of the public health emergencies and events that the WHO is
responding to, with data updated by the hour. Users can explore a visual world map that displays health emergencies and events, the type of emergency, and the year that occurred. WHO Health Emergency
DashboardLink to URL\nSource: WHO Health Emergency Dashboard. World Health Organization 2024.https://extranet.who.int/publicemergency.\nCopy Source ## Learn more with these Related Resources\n*
\nData\n**\nInteractive 2024 Data Visualization: Lancet Countdown: Tracking Progress on Health and Climate Change This data visualization from The Lancet presents the findings and 2024 report data
from The \u2026This data visualization from*The Lancet*presents the findings and 2024 report data from*The Lancet Countdown: Tracking Progress on Health and Climate Change*at country specific,
regional, and income group levels. The Lancet Countdown is dedicated to monitoring the world\u2019s responses to climate change and the health effects that result from those efforts, providing a
global overview of the relationship between public health and the climate crisis. The data is presented under five categories:\u2026 Environmental Risks|Global Risks|Public Health|Global
Governance|SDGs/Development|Economics/Finance|Government/Law|Climate/Environment|Global * \nData\n**\nWeb Portal 2025\nHealth Inequality Monitor This data portal from the World Health Organization
(WHO) offers data, tools, and resources concerning \u2026This data portal from the World Health Organization (WHO) offers data, tools, and resources concerning health inequality monitoring worldwide.
The portal offers a data repository, which includes datasets of disaggregated data across various topics and inequality indicators, including COVID-19, reproductive, maternal, and child health, HIV,
tuberculosis, and malaria, immunization, and water, sanitation, and hygiene (WASH).Datasets are available for download and can also be explored using the Health Equity Assessment Toolkit (HEAT), a
database tool that\u2026 Infectious Disease|Maternal/Reproductive|Human Rights/Equity|Water/Sanitation|Global * \nReport\n**\nPublication 2021\nNature, Biodiversity and Health: An Overview of
Interconnections This report from the World Health Organization (WHO) provides an overview of the impact of \u2026This report from the World Health Organization (WHO) provides an overview of the
impact of the natural environment on human health worldwide, analyzing the linkages between nature, biodiversity, and health, and methods for protecting global health worldwide. The report
specifically analyzes how environmental change, loss of biodiversity, and changes in animal and plant species pose significant threats to human health, analyzing potential impacts on freshwater
systems, air quality, oceans, agriculture, nutrition and food security, disease,\u2026 Infectious Disease|Global Risks|Water/Sanitation|Public Health|Cities/Urban
Planning|Food/Agriculture|Climate/Environment|Global"], "published_date": "2025-01-01T00:00:00.000", "score": null}, {"title": "Emergency events", "url":
"https://www.who.int/europe/emergencies/emergency-events", "snippet": "Emergency events Skip to main content\n\nEmergencies\n\nOverview Situations Our work in emergencies\n\n# WHO Emergency
events\n\nRead the latest WHO emergency events\n\n2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 2015 2014 2013 2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000 1999 1998 1997
1996 1995 1994 1993 1992 1991 1990\n\nUnfortunately we don't have any results matching your criteria.\n\nYour predefined filter criteria are invalid.", "highlights": ["Emergency events Skip to main
content\n\nEmergencies\n\nOverview Situations Our work in emergencies\n\n# WHO Emergency events Read the latest WHO emergency events 2026 2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 2015 2014
2013 2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000 1999 1998 1997 1996 1995 1994 1993 1992 1991 1990 Unfortunately we don't have any results matching your criteria.\n\nYour
predefined filter criteria are invalid."], "published_date": null, "score": null}, {"title": "World Health Organization Emergencies Programme", "url": "https://www.who.int/emergencies/overview",
"snippet": "World Health Organization Emergencies Programme Skip to main content\n\n \n\n \n\nEmergencies\n\nOverview Funding Operations Partners Surveillance Research Training\n\nGlobal health
emergencies\n\nAll \u2192\n\n \n\n### Conflict in Israel and the occupied Palestinian territory\n\n \n\n \n\n### Coronavirus disease (COVID-19)\n\n \n\n \n\n### Sudan\n\n \n\nDisease Outbreak
News\n\nSituation reports\n\nWeekly Epidemiological Record\n\nHealth Emergency Dashboard\n\nIndependent Oversight and Advisory Committee\n\nWHO's health emergency appeals\n\n#", "highlights": ["World
Health Organization Emergencies Programme Skip to main content\n\n \n\n \n\nEmergencies Overview Funding Operations Partners Surveillance Research Training\n\nGlobal health emergencies\n\nAll \u2192
### Conflict in Israel and the occupied Palestinian territory\n\n \n\n \n\n### Coronavirus disease (COVID-19) ### Sudan\n\n \n\nDisease Outbreak News\n\nSituation reports\n\nWeekly Epidemiological
Record\n\nHealth Emergency Dashboard Independent Oversight and Advisory Committee\n\nWHO's health emergency appeals\n\n## Emergency news\n\nAll \u2192 30 March 2026 StatementTypes of data requested to
inform May 2026 COVID-19 vaccine antigen composition deliberations 24 March 2026 Departmental updateNew WHO Guidance Helps Countries to Institutionalize Simulation Exercises to   ...    19 March 2026
Departmental updateGerman Health Minister Nina Warken and WHO Hub in Berlin highlight 2025 achievements 11 March 2026 News releaseConflict deepens health crisis across Middle East, WHO says\n\n# Our
emergency work in focus   ...    16 March 2026 INITIATE\u00b2. West African countries strengthen outbreak preparedness through regional simulation exercise   ...    3 March 2026 From data to life-
saving action: how Go.Data strengthened outbreak response in Cox\u2019s Bazar, Bangladesh   ...    Featured meeting report | 16 January 2025\n\n### WHO's Health Emergency Appeal
2025\n\nDownload\n\nRead More\n\nPublications All \u2192\n\n23 October 2025\n\n### National health emergency alert and response framework This multi-hazard Health Emergency Alert and Response
Framework provides guidance for coordinating emergency response in countries, under the global Health... Download\n\nRead More\n\n29 September 2025\n\n### Therapeutics and COVID-19: living guideline,
August 2025 The WHO Therapeutics and COVID-19: living guideline contains recommendations for the use of therapeutics in the   ...    Download\n\nRead More\n\n15 July 2025\n\n### Clinical management of
COVID-19: living guideline, June 2025   ...    ### NAPHS for all: a country implementation guide for national action plan for health security (\u200eNAPHS)\u200e A national action plan for health
security (NAPHS) is a country-owned, multi-year, joint planning process that can   ...    Download\n\nRead More\n\nDocuments\n\nAll \u2192\n\n26 March 2026 ### Multi-country outbreak of mpox, External
situation report #64 - 26 March 2026 This is the 64th situation report for the multi-country outbreak of mpox, which provides details on the global   ...    Download\n\nRead More\n\n12 March
2026\n\n### Public Health Situation Analysis - Afghanistan - March 2026 Afghanistan faces a harsh winter at a moment of heightened vulnerability and escalating humanitarian need. After   ...
Download\n\nRead More\n\n11 March 2026\n\n### Public Health Situation Analysis - Somalia In 2025, needs were driven by the complex interaction of climate shocks, prolonged conflict and insecurity,
large-scale   ...    Download\n\nRead More\n\n25 February 2026\n\n### Public Health Situation Analysis - Sudan Conflict and Complex Emergency After more than two and a half years of the conflict,
Sudan remains locked in a humanitarian catastrophe of staggering dimensions. In 2026, 33.7 million... Download\n\nRead More\n\nMore about our work in emergencies\n\nRapidly detecting and responding to
health emergencies Strengthening national emergency preparedness\n\nTracking SARS-CoV-2 variants Minimizing health risks at airports, ports and ground crossings\n\nCommunicating risk in public health
emergencies Supporting national implementation of International Health Regulations Building a skilled workforce to prepare for and respond to emergencies Managing environmental health risks in
emergencies\n\nTranslating science for better health emergency preparedness Strengthening the global health-security interface\n\nStrengthening partnerships with the faith community Safeguarding
biosafety and biosecurity in laboratories Measuring the effectiveness and impact of public health"], "published_date": null, "score": null}, {"title": "WHO Health Emergency Dashboard - ClimaHealth",
"url": "https://climahealth.info/resource-library/who-health-emergency-dashboard/", "snippet": "WHO Health Emergency Dashboard - ClimaHealth Skip to Main Content --\n\nExplore health-relevant side
events, news and resources from the 2025 UN Climate Conference.\n\nHealth at COP30 >\n\n### Explore By\n\n- Climate Service Providers\n- Progress Dashboard\n- Map\n- Themes\n- Hazards\n-
Countries\n\n#### This site uses cookies.\n\nThis site uses cookies to improve your online experience. To learn more about how we use cookies, please see our terms of use.\n\nAccept and Close
--\n\n--\n\nHome| Resources| Tools\n\nWHO, 20", "highlights": ["WHO Health Emergency Dashboard - ClimaHealth Skip to Main Content -- Explore health-relevant side events, news and resources from the
2025 UN Climate Conference.\n\nHealth at COP30 > ### Explore By\n\n- Climate Service Providers\n- Progress Dashboard\n- Map\n- Themes\n- Hazards\n- Countries #### This site uses cookies. This site
uses cookies to improve your online experience. To learn more about how we use cookies, please see our terms of use. Accept and Close --\n\n--\n\nHome| Resources| Tools\n\nWHO, 2019 The World Health
Organization (WHO) Health Emergency Dashboard is a platform which aims to share information about public health events and emergencies. The data on the dashboard is refreshed every fifteen (15)
minutes and data is accurate as at time of refreshing. View Website"], "published_date": "2021-11-03T17:39:08.000", "score": null}, {"title": "Emergency events - World Health Organization (WHO)",
"url": "https://www.who.int/emergencies/emergency-events", "snippet": "Emergency events Skip to main content\n\nEmergencies\n\nOverview Funding Operations Partners Surveillance Research Training\n\n#
WHO Emergency events\n\nRead the latest WHO emergency events\n\n#### Mpox: recombinant virus with genomic elements of clades Ib and IIb\n\n11 February 2026 Diseases and conditions\n\n#### Nipah virus
infection\n\n2 February 2026 Diseases and conditions\n\n#### Nipah virus infection\n\n12 January 2026 Diseases and conditions\n\n#### Avian Influenza A(H5N5)\n\n26 December 2025 Diseases and cond",
"highlights": ["Emergency events Skip to main content\n\nEmergencies\n\nOverview Funding Operations Partners Surveillance Research Training # WHO Emergency events\n\nRead the latest WHO emergency
events #### Mpox: recombinant virus with genomic elements of clades Ib and IIb\n\n11 February 2026 Diseases and conditions #### Nipah virus infection\n\n2 February 2026 Diseases and conditions\n\n####
Nipah virus infection 12 January 2026 Diseases and conditions\n\n#### Avian Influenza A(H5N5)\n\n26 December 2025 Diseases and conditions #### Marburg virus disease\n\n19 November 2025 Diseases and
conditions\n\n#### Nipah virus infection 24 March 2025 Diseases and conditions\n\n#### Ebola virus disease\n\n3 September 2025 Diseases and conditions #### Circulating vaccine-derived poliovirus type
1\n\n13 August 2025 Diseases and conditions\n\n#### Nipah virus infection 21 August 2025 Diseases and conditions\n\n#### Avian Influenza A(H5N1)\n\n4 July 2025 Diseases and conditions ####
Anthrax\n\n22 May 2025 Diseases and conditions\n\n#### Circulating vaccine-derived poliovirus type 2 (cVDPV2) 15 May 2025 Diseases and conditions\n\n#### Avian Influenza A(H5N1)\n\n17 April 2025
Diseases and conditions #### Invasive meningococcal disease\n\n28 March 2025 Diseases and conditions\n\n#### Measles 27 March 2025 Diseases and conditions\n\n#### Sudan virus disease\n\n30 January
2025 Diseases and conditions #### Zika virus disease\n\n29 November 2024 Diseases and conditions\n\n#### Chapare haemorrhagic fever 15 January 2025 Diseases and conditions\n\n#### Outbreak of
suspected Marburg Virus Disease 13 January 2025 Diseases and conditions\n\n#### Undiagnosed disease\n\n8 December 2024 Diseases and conditions"], "published_date": null, "score": null}, {"title": "WHO
- List of emergencies", "url": "https://production-cms.platform.who.int/data/redirect-pages/megamenu/emergencies/focus-on", "snippet": "WHO - List of emergencies Skip to main
content\n\nEmergencies\n\nOverview Funding Operations Partners Surveillance Research Training\n\n# Ongoing health emergencies\n\nThe health emergencies list below details the disease outbreaks,
environmental disasters and other humanitarian crises in which WHO has played or is still playing an essential role in protecting health.\n\n## Outbreaks\n\n### Coronavirus disease (COVID-19)\n\n###
Cholera\n\n### Mpox (monkeypox)\n\n## Humanitarian crises\n\nAfghanistan\n\nIsrael and the", "highlights": ["WHO - List of emergencies Skip to main content\n\nEmergencies Overview Funding Operations
Partners Surveillance Research Training\n\n# Ongoing health emergencies The health emergencies list below details the disease outbreaks, environmental disasters and other humanitarian crises in which
WHO has played or is still playing an essential role in protecting health. ## Outbreaks\n\n### Coronavirus disease (COVID-19)\n\n### Cholera\n\n### Mpox (monkeypox)\n\n## Humanitarian crises
Afghanistan\n\nIsrael and the occupied Palestinian territory and region\n\nNorthern Ethiopia\n\nSomalia\n\nSouth Sudan\n\nSudan Syria\n\nUkraine\n\nYemen\n\nPast health emergencies\n\nAvian influenza
A (H7N9) virus outbreak\n\nDengue upsurge, 2023 - 2024 Drought and food insecurity in the greater Horn of Africa\n\nEbola outbreak, Democratic Republic of the Congo, 2017 Earthquake in T\u00fcrkiye
and the Syrian Arab Republic\n\nEbola outbreak, Democratic Republic of the Congo, 2018 Ebola outbreak, Democratic Republic of the Congo, 2021 Ebola outbreak, Equateur Province, Democratic Republic of
the Congo, 2020 Ebola outbreak, North Kivu, Ituri, Democratic Republic of the Congo, 2018 - 2020 Ebola outbreak, Mbandaka Equateur Province, Democratic Republic of the Congo, 2022 Ebola outbreak,
N'Zerekore, Guinea, 2021\n\nEbola outbreak, Uganda, 2022\n\nEbola outbreak, West Africa, 2014-2016 Humanitarian crisis in Sahel region of Africa\n\nInfluenza A (H1N1) virus, 2009-2010 pandemic\n\nIraq
crisis Marburg virus disease outbreak, Rwanda, 2024\n\nMiddle East respiratory syndrome (MERS-CoV) outbreak\n\nNigeria crisis Pakistan crisis\n\nZika virus disease outbreak, 2015-2016\n\n## Related
emergency content\n\nDisease Outbreak News Situation reports\n\nWeekly Epidemiological Record"], "published_date": "2025-01-01T00:00:00.000", "score": null}, {"title": "WHO - List of emergencies -
World Health Organization (WHO)", "url": "https://www.who.int/emergencies/situations", "snippet": "WHO - List of emergencies\n\nSkip to main content\n\nEmergencies\n\nOverview Funding Operations
Partners Surveillance Research Training\n\n# Ongoing health emergencies\n\nThe health emergencies list below details the disease outbreaks, environmental disasters and other humanitarian crises in
which WHO has played or is still playing an essential role in protecting health.\n\n## Outbreaks\n\n### Coronavirus disease (COVID-19)\n\n### Cholera\n\n### Mpox (monkeypox)\n\n## Humanitarian
crises\n\nAfghanistan\n\nIsrael and th", "highlights": ["WHO - List of emergencies\n\nSkip to main content\n\nEmergencies Overview Funding Operations Partners Surveillance Research Training\n\n#
Ongoing health emergencies The health emergencies list below details the disease outbreaks, environmental disasters and other humanitarian crises in which WHO has played or is still playing an
essential role in protecting health. ## Outbreaks\n\n### Coronavirus disease (COVID-19)\n\n### Cholera\n\n### Mpox (monkeypox)\n\n## Humanitarian crises Afghanistan\n\nIsrael and the occupied
Palestinian territory and region\n\nNorthern Ethiopia\n\nSomalia\n\nSouth Sudan\n\nSudan Syria\n\nUkraine\n\nYemen\n\nPast health emergencies\n\nAvian influenza A (H7N9) virus outbreak\n\nDengue
upsurge, 2023 - 2024 Drought and food insecurity in the greater Horn of Africa\n\nEbola outbreak, Democratic Republic of the Congo, 2017 Earthquake in T\u00fcrkiye and the Syrian Arab
Republic\n\nEbola outbreak, Democratic Republic of the Congo, 2018 Ebola outbreak, Democratic Republic of the Congo, 2021 Ebola outbreak, Equateur Province, Democratic Republic of the Congo, 2020
Ebola outbreak, North Kivu, Ituri, Democratic Republic of the Congo, 2018 - 2020 Ebola outbreak, Mbandaka Equateur Province, Democratic Republic of the Congo, 2022 Ebola outbreak, N'Zerekore, Guinea,
2021\n\nEbola outbreak, Uganda, 2022\n\nEbola outbreak, West Africa, 2014-2016 Humanitarian crisis in Sahel region of Africa\n\nInfluenza A (H1N1) virus, 2009-2010 pandemic\n\nIraq crisis Marburg
virus disease outbreak, Rwanda, 2024\n\nMiddle East respiratory syndrome (MERS-CoV) outbreak\n\nNigeria crisis Pakistan crisis\n\nZika virus disease outbreak, 2015-2016\n\n## Related emergency
content\n\nDisease Outbreak News Situation reports\n\nWeekly Epidemiological Record"], "published_date": null, "score": null}]
```

## 💭 Thinking

Excellent! This is very revealing. Let me analyze what I found:

1. **The Exa search actually rendered some of the dashboard content**: The search_exa result for the dashboard shows:
   - "Number of Events: 69"
   - "Number of deaths on healthcare attacks: 2.6K"
   - "Number of injuries on healthcare attacks: 5.5K"
   - "Total number of healthcare attacks: 7.3K"
   - It has layers for "Events", "Attack On Health", and "HeRAMS"

2. **The dashboard tracks "Attack on Health" data** - which is exactly what WHO has been tracking for Iran (23 verified attacks on healthcare). 

The 2.6K deaths and 5.5K injuries from healthcare attacks align with conflict data from the Iran/Middle East region, including casualties from attacks in Lebanon and Iran itself. The 69 events represent public health emergencies tracked globally, and WHO's ongoing health emergencies list covers humanitarian crises across Afghanistan, Israel/Palestine, Sudan, Syria, Ukraine, Yemen and other regions—the exact type of events this dashboard monitors. The Harvard description indicates it's a comprehensive worldwide health data dashboard.

WHO's Surveillance System for Attacks on Health Care feeds attack data directly into the dashboard, and given the 23+ documented attacks on healthcare in Iran combined with the significant death and injury toll, Iran's conflict would almost certainly be represented among these tracked events. The dashboard clearly encompasses conflict-related healthcare impacts alongside traditional disease outbreaks, which substantially increases my confidence that Iran's situation is included. Wait - I notice the WHO "List of emergencies" page (https://www.who.int/emergencies/situations) lists humanitarian crises but appears to NOT YET include Iran. It lists Afghanistan, Israel/Palestine, Northern Ethiopia, Somalia, South Sudan, Sudan, Syria, Ukraine, Yemen. However, this is a different page from the dashboard, and the snapshot might be from before the Iran war started (Feb 28, 2026). Also, the search_exa crawl of this page might be a cached version.

But the dashboard itself shows 69 events and has "Attack on Health" data with 2.6K deaths and 5.5K injuries - numbers that align with the Middle East conflict data. This is strong circumstantial evidence that Iran is already on the dashboard.

The evidence points toward Iran being tracked on the dashboard through the "Attack on Health" layer, given the scale of the crisis and WHO's systematic monitoring of healthcare attacks through their SSA system. I'm settling on ~0.97 as my confidence level - the dashboard clearly includes conflict events based on its structure and data layers.

## 💬 Response

This is very revealing. The Exa search actually rendered some dashboard content showing:
- **69 events** currently listed
- **"Attack on Health" layer** tracking 2.6K deaths and 5.5K injuries from healthcare attacks  
- **"HeRAMS" layer** for health facility monitoring

The dashboard explicitly tracks "Attacks on Health" — exactly what WHO has been monitoring in Iran (23 verified attacks). This confirms the dashboard includes conflict-related events, not just disease outbreaks. Let me update my reflection with this additional evidence.
