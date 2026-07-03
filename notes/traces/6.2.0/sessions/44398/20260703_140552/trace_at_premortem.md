# Reasoning Log: What percentage of votes will Hakainde Hichilema receive in the first round of Zambia's 2026 presidential elections?

*Generated: 2026-07-03T14:14:57.834571+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "What is the current state of polling and political dynamics for Zambia's August 2026 presidential election, specifically Hakainde Hichilema's expected vote share?",
  "context": "Zambia holds general elections August 13, 2026. Incumbent Hakainde Hichilema (UPND) is running. An October 2025 poll suggested 60% for HH vs 35% opposition. The election is described as alliance-driven following a 2025 constitutional amendment. I need: recent polls (2025-2026), opposition coalition strength, whether main rival Edgar Lungu/PF is running, historical Zambian polling accuracy, and any factors affecting turnout or vote share.",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': "What is the cu...te share.', 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "query": "Historical first-round vote shares of Zambian presidential elections 2011, 2015, 2016, 2021 for incumbents and winners, and accuracy of Zambian pre-election polls",
  "context": "Need historical base rates for Zambian presidential election vote shares, especially how incumbents performed and how accurate pre-election opinion polls were versus actual results.",
  "ttl": "14d"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'Historical fir...results.', 'ttl': '14d'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "What is the current state of polling and political dynamics for Zambia's August 2026 presidential election, specifically Hakainde Hichilema's expected vote share? Include recent 2025-2026 polls, opposition coalition strength, whether Edgar Lungu/PF is running (note Lungu died in 2025), and turnout factors.",
      "context": "Zambia holds general elections August 13, 2026. Incumbent Hakainde Hichilema (UPND) is running. October 2025 poll suggested 60% for HH vs 35% opposition. Election described as alliance-driven following 2025 constitutional amendment.",
      "ttl": "6h"
    },
    {
      "query": "Historical first-round vote shares of Zambian presidential elections 2011, 2015, 2016, 2021 for incumbents and winners, and accuracy of Zambian pre-election opinion polls versus actual results",
      "context": "Need historical base rates for Zambian presidential election vote shares, especially incumbent performance and pre-election poll accuracy.",
      "ttl": "14d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "What is the current state of polling and political dynamics for Zambia's August 2026 presidential election, specifically Hakainde Hichilema's expected vote share? Include
recent 2025-2026 polls, opposition coalition strength, whether Edgar Lungu/PF is running (note Lungu died in 2025), and turnout factors.", "entry": {"slug": "what-is-the-current-state-of-polling-and-
political-cbf6d26a", "query": "What is the current state of polling and political dynamics for Zambia's August 2026 presidential election, specifically Hakainde Hichilema's expected vote share?
Include recent 2025-2026 polls, opposition coalition strength, whether Edgar Lungu/PF is running (note Lungu died in 2025), and turnout factors.", "answer": "I've completed the research and delivered
both the full markdown synthesis and structured findings. Here's a concise recap of the key findings:\n\n**Bottom line:** Hichilema (UPND) enters the 13 August 2026 election as a strong favorite, but
the race is more competitive than the headline poll suggests.\n\n**Polling:**\n- **October 2025 Mutombo/UNZA poll** (n=1,009, \u00b13.1%): HH **60%** (58\u201363% range) vs. **~35%** combined
opposition \u2014 the headline figure you referenced.\n- Unscientific March 2026 online poll: HH ~52%, Mundubile ~27%.\n- Academic ZERN/IDCPPA survey (March 2026) exists but detailed vote numbers
weren't publicly accessible.\n\n**Opposition/Lungu:**\n- **Edgar Lungu died 5 June 2025** in Pretoria \u2014 he was already barred from running (Dec 2024 ConCourt ruling). His death fractured the PF
and spawned a still-unresolved burial dispute.\n- The opposition has partly consolidated behind **Brian Mundubile** (Tonse\u2013PF \"Pamodzi\" Alliance, running mate Makebi Zulu), who has shown
surprising momentum on ex-PF networks. Fred M'membe (Socialist Party) runs separately after the broader united-opposition effort collapsed.\n\n**Alliance-driven framing:** Confirmed \u2014
**Constitution Amendment Act No. 7 of 2025 (\"Bill 7,\" enacted Dec 2025)** expanded parliament and reserved seats, plus a delimitation exercise critics call gerrymandering. With 14 approved
candidates and a 50%+1 threshold, opposition fragmentation strongly favors HH.\n\n**Turnout:** ~8.7M registered voters; high turnout expected; youth bloc decisive (as in 2021). Economic grievances
(cost of living, jobs, electricity) are the opposition's main opening.\n\n**Key caveat:** Zambian polling is thin and historically unreliable, so figures are directional rather than precise.",
"sources": [{"url": "https://www.mwebantu.com/opinion-poll-shows-president-hakainde-hichilema-headed-for-victory-in-2026/", "title": "Opinion poll shows President Hakainde Hichilema headed for victory
in 2026", "domain": "mwebantu.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Oct 2025 poll (n=1,009, \u00b13.1%): Hichilema 60% (58\u201363%) vs 35% opposition; supervised by Dr Namuunda
Mutombo, UNZA."}, {"url": "https://en.wikipedia.org/wiki/2026_Zambian_general_election", "title": "2026 Zambian general election", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03T00:00:00Z",
"snippet": "Elections due 13 August 2026 for president, National Assembly, councillors and council chairs."}, {"url": "https://en.wikipedia.org/wiki/Death_and_state_funeral_of_Edgar_Lungu", "title":
"Death and state funeral of Edgar Lungu", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Lungu died 5 June 2025 in Pretoria; prolonged burial dispute; Aug 2025
Pretoria court ordered repatriation to Zambia."}, {"url": "https://en.wikipedia.org/wiki/Edgar_Lungu", "title": "Edgar Lungu", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03T00:00:00Z",
"snippet": "Sixth president of Zambia (2015\u20132021); lost 2021 to Hichilema; died June 2025."}, {"url": "https://en.wikipedia.org/wiki/Constitution_of_Zambia_(Amendment)_Act,_No._7_of_2025",
"title": "Constitution of Zambia (Amendment) Act, No. 7 of 2025", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Bill 7 passed 15 Dec 2025 (135\u20130), assented 18
Dec 2025; earlier version struck down by ConCourt 27 June 2025."}, {"url": "https://africacenter.org/spotlight/en-elections-2026/zambia/", "title": "Zambia: The Challenges of Maintaining Democratic
Progress", "domain": "africacenter.org", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "HH seeking second term; expanded Assembly; Tonse Alliance backed away from UKA partnership with PF after
Lungu's death; 8.7M-scale registration and youth turnout factors."}, {"url": "https://allafrica.com/stories/202606080578.html", "title": "Zambia: Elections 2026 - Is Zambia's Democratic Success Story
Beginning to Fray?", "domain": "allafrica.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "ISS analysis (8 June 2026): 26 registered / 14 approved candidates; 8.7M registered voters; 86%
Afrobarometer support elections; delimitation and legal manoeuvring concerns."}, {"url": "https://issafrica.org/iss-today/elections-2026-is-zambia-s-democratic-success-story-beginning-to-fray",
"title": "Elections 2026: is Zambia's democratic success story beginning to fray?", "domain": "issafrica.org", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Risk that voters see the August
outcome as shaped by legal manoeuvring rather than the ballot."}, {"url": "https://www.theafricareport.com/384866/zambia-2026-can-lungu-revive-a-divided-opposition-to-challenge-hichilema/", "title":
"Zambia 2026: Can Lungu revive a divided opposition to challenge Hichilema?", "domain": "theafricareport.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Opposition weakened and disorganised;
PF fractured (Sampa/Chabinga); Tonse Alliance; Hichilema in strong position (article predates Lungu death)."}, {"url": "https://www.lusakatimes.com/2026/05/19/mundubile-succesfully-files-in-with-
makebi-as-running-mate/", "title": "Mundubile Successfully Files In With Makebi As Running Mate", "domain": "lusakatimes.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Tonse Alliance
candidate Brian Mundubile filed presidential nomination with Makebi Zulu after party-ticket switch."}, {"url": "https://diggers.news/local/2026/01/29/tonse-elects-mundubile-as-president/", "title":
"Tonse elects Mundubile as president", "domain": "diggers.news", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Tonse Alliance elected Brian Mundubile as presidential candidate 29 Jan 2026;
alliance split into two factions (Lubinda vs Mundubile)."}, {"url": "https://www.lusakatimes.com/2026/03/04/hichilema-dominates-mwamba-online-poll-with-clear-52-majority/", "title": "Hichilema
dominates Mwamba online poll with clear 52% majority", "domain": "lusakatimes.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Unscientific March 2026 Facebook poll (~40,800 votes): HH ~52%,
Mundubile ~27%, Zulu ~18%, Kalaba ~4%."}, {"url": "https://zambianobserver.com/united-opposition-has-disintegrated-weve-failed-to-choose-a-flag-bearer-mmembe/", "title": "United opposition has
disintegrated, we've failed to choose a flag bearer \u2013 M'membe", "domain": "zambianobserver.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "M'membe: United Opposition Front disintegrated
over failure to choose a single flag-bearer."}, {"url": "https://mg.co.za/thought-leader/2025-09-15-zambias-2026-election-how-hichilema-is-tilting-the-playing-field-against-opponents/", "title":
"Zambia's 2026 election: How Hichilema is tilting the playing field against opponents", "domain": "mg.co.za", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Alleges electoral irregularities,
control of opposition party machinery, and use of police against opposition."}, {"url": "https://humanities.uct.ac.za/cssr/idcppa/publication/bp-03-26", "title": "Main findings from the Zambia
Election Research Network Round 1 Survey", "domain": "humanities.uct.ac.za", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "IDCPPA/UCT academic briefing paper, March 2026 (Beardsworth, Kabinga,
Seekings, Wahman)."}, {"url": "https://zambianobserver.com/mundubile-energy-momentum-the-credibility-gap/", "title": "Mundubile: Energy, Momentum & the Credibility Gap", "domain":
"zambianobserver.com", "accessed_at": "2026-07-03T00:00:00Z", "snippet": "Mundubile drawing sizeable crowds across Copperbelt, Central, Eastern and Muchinga via ex-PF networks."}], "key_facts":
["Zambia's general elections are scheduled for 13 August 2026 (president, National Assembly, councillors, council chairs).", "October 2025 Mutombo/UNZA national poll (n=1,009, all 10 provinces,
\u00b13.1%, fielded 2\u201315 Oct 2025): Hichilema 60% (range 58\u201363%) vs ~35% combined opposition; a related report cited a 75% approval rating.", "Edgar Lungu died 5 June 2025 in Pretoria, South
Africa; he was already barred from running by a December 2024 Constitutional Court ruling on his term limit.", "Lungu's death triggered PF fragmentation and a prolonged, still-unresolved burial
dispute (courts ordered repatriation to Zambia Aug 2025; family granted appeal Dec 2025).", "Brian Mundubile is the main opposition challenger as the Tonse\u2013PF 'Pamodzi' Alliance candidate,
running with Makebi Zulu; elected Tonse candidate 29 Jan 2026, filed nomination 19 May 2026.", "Fred M'membe (Socialist Party, running mate Dolika Banda) runs separately; the broader 'United
Opposition Front' collapsed over failure to agree a single flag-bearer.", "26 presidential candidates registered; 14 approved by the Electoral Commission of Zambia (ECZ).", "Constitution (Amendment)
Act No. 7 of 2025 ('Bill 7') passed 15 Dec 2025 and was assented 18 Dec 2025; it expanded the National Assembly and added 40 reserved/PR seats for women, youth, and persons with disabilities. An
earlier version was struck down by the ConCourt on 27 June 2025.", "A delimitation exercise added roughly 70 constituencies; critics allege gerrymandering favoring UPND strongholds (e.g., Southern
Province 20\u219229 seats).", "Approximately 8.7 million voters are registered; 758,000 new voters registered in late 2025; 86% of Zambians (Afrobarometer) say elections are the best way to choose
leaders, implying high expected turnout.", "Hichilema won the 2021 election with 59%, powered by strong youth turnout; youth remain a decisive bloc.", "Zambia requires 50%+1 to win the presidency
outright; a fragmented opposition splitting the anti-UPND vote structurally favors the incumbent.", "Unscientific March 2026 Mwamba Facebook online poll (~40,800 votes): Hichilema ~52%, Mundubile
~27%, Makebi Zulu ~18%, Harry Kalaba ~4%.", "Mundubile has shown unexpected campaign momentum via former PF networks across Copperbelt, Central, Eastern and Muchinga provinces, but faces
resource/logistical disadvantages (reportedly denied air transport while HH campaigns freely).", "Voter-priority issues are cost of living, unemployment and electricity (72% reported no/irregular
power in 2024), giving the opposition an economic-grievance opening.", "Analysts (ISS, Mail & Guardian) warn the election risks being seen as shaped by legal/constitutional manoeuvring rather than the
ballot; M'membe was arrested under the 2025 Cyber Crimes Act in March 2026."], "data_points": [{"metric": "Hichilema projected vote share (Oct 2025 Mutombo/UNZA poll)", "value": 60.0, "unit":
"percent", "as_of": "2025-10-15", "source_url": "https://www.mwebantu.com/opinion-poll-shows-president-hakainde-hichilema-headed-for-victory-in-2026/"}, {"metric": "Combined opposition vote share (Oct
2025 poll)", "value": 35.0, "unit": "percent", "as_of": "2025-10-15", "source_url": "https://www.mwebantu.com/opinion-poll-shows-president-hakainde-hichilema-headed-for-victory-in-2026/"}, {"metric":
"Poll sample size (Oct 2025 Mutombo/UNZA)", "value": 1009.0, "unit": "respondents", "as_of": "2025-10-15", "source_url": "https://www.mwebantu.com/opinion-poll-shows-president-hakainde-hichilema-
headed-for-victory-in-2026/"}, {"metric": "Poll margin of error (Oct 2025)", "value": 3.1, "unit": "percent (+/-)", "as_of": "2025-10-15", "source_url": "https://www.mwebantu.com/opinion-poll-shows-
president-hakainde-hichilema-headed-for-victory-in-2026/"}, {"metric": "Hichilema approval rating (reported)", "value": 75.0, "unit": "percent", "as_of": "2025-10-15", "source_url":
"https://zambianobserver.com/poll-places-president-hh-at-75-approval-rate/"}, {"metric": "Hichilema 2021 election vote share", "value": 59.0, "unit": "percent", "as_of": "2021-08-16", "source_url":
"https://africacenter.org/spotlight/en-elections-2026/zambia/"}, {"metric": "Registered voters for 2026 election", "value": 8700000.0, "unit": "voters", "as_of": "2026-06-08", "source_url":
"https://allafrica.com/stories/202606080578.html"}, {"metric": "New voters registered late 2025", "value": 758000.0, "unit": "voters", "as_of": "2025-12-31", "source_url":
"https://africacenter.org/spotlight/en-elections-2026/zambia/"}, {"metric": "Presidential candidates registered", "value": 26.0, "unit": "candidates", "as_of": "2026-06-08", "source_url":
"https://allafrica.com/stories/202606080578.html"}, {"metric": "Presidential candidates approved by ECZ", "value": 14.0, "unit": "candidates", "as_of": "2026-06-08", "source_url":
"https://allafrica.com/stories/202606080578.html"}, {"metric": "Afrobarometer: Zambians who see elections as best way to choose leaders", "value": 86.0, "unit": "percent", "as_of": "2026-06-08",
"source_url": "https://allafrica.com/stories/202606080578.html"}, {"metric": "Bill 7 National Assembly vote in favour (Third Reading)", "value": 135.0, "unit": "MPs", "as_of": "2025-12-15",
"source_url": "https://en.wikipedia.org/wiki/Constitution_of_Zambia_(Amendment)_Act,_No._7_of_2025"}, {"metric": "Hichilema share in unscientific Mwamba online poll", "value": 52.0, "unit": "percent",
"as_of": "2026-03-04", "source_url": "https://www.lusakatimes.com/2026/03/04/hichilema-dominates-mwamba-online-poll-with-clear-52-majority/"}, {"metric": "Mundubile share in unscientific Mwamba online
poll", "value": 27.0, "unit": "percent", "as_of": "2026-03-04", "source_url": "https://www.lusakatimes.com/2026/03/04/hichilema-dominates-mwamba-online-poll-with-clear-52-majority/"}, {"metric":
"Presidential win threshold (50%+1)", "value": 50.0, "unit": "percent-plus-one", "as_of": "2026-08-13", "source_url": "https://www.theafricareport.com/384866/zambia-2026-can-lungu-revive-a-divided-
opposition-to-challenge-hichilema/"}], "created_at": "2026-07-03T14:13:56.546599Z", "updated_at": "2026-07-03T14:13:56.546599Z", "stale_after": "2026-07-03T20:13:56.546599Z", "state": "fresh",
"revision_history": [], "session_id": "40f6c4d3-8203-4c5a-8791-cf00a70166ae", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Historical first-round vote shares of Zambian presidential
elections 2011, 2015, 2016, 2021 for incumbents and winners, and accuracy of Zambian pre-election opinion polls versus actual results", "entry": {"slug": "historical-first-round-vote-shares-of-
zambian-pres-f9b91819", "query": "Historical first-round vote shares of Zambian presidential elections 2011, 2015, 2016, 2021 for incumbents and winners, and accuracy of Zambian pre-election opinion
polls versus actual results", "answer": "I've completed the research. Here's a summary of the key findings:\n\n## Zambian Presidential Elections \u2014 First-Round Vote Shares & Poll
Accuracy\n\n**First-round vote shares (winner / incumbent):**\n- **2011** (plurality): Michael Sata (challenger) won ~42.98%; incumbent Rupiah Banda **lost** at ~36%\n- **2015** by-election
(plurality): Edgar Lungu won 48.33% vs Hichilema 46.67% \u2014 margin just **1.68%** (27,757 votes)\n- **2016** (first 50%+1 election): incumbent Lungu **re-elected** with 50.35%, barely clearing
threshold, vs Hichilema 47.63%\n- **2021**: Hichilema (challenger) won a **landslide 59.02%**; incumbent Lungu **lost** at 38.71%\n\n**Key base-rate patterns:**\n- Both recent sitting presidents who
ran (Banda 2011, Lungu 2021) **lost outright**.\n- Lungu's share collapsed ~11.6 pts from 2016\u21922021 amid economic crisis.\n- Outcomes oscillate between razor-thin (2015, 2016) and decisive
(2021).\n\n**Pre-election poll accuracy (2021):** Poor and divergent. Government-aligned polls badly over-stated the incumbent:\n- PSAZ poll: predicted Lungu 40.4% / Hichilema 30.33% (understated the
actual winner by ~29 pts; condemned as flawed/biased)\n- \"Zambia Decides\": predicted a Lungu 56% landslide \u2014 completely inverted\n- Afrobarometer (most credible): gave no headline winner but
flagged declining PF support and a large 45.6% undeclared bloc that broke heavily to Hichilema (a hidden anti-incumbent vote)\n\nThe full report, structured data points, and sources have been
submitted via the StructuredOutput tool.", "sources": [{"url": "https://en.wikipedia.org/wiki/2021_Zambian_general_election", "title": "2021 Zambian general election", "domain": "en.wikipedia.org",
"accessed_at": "2026-07-03", "snippet": "Hakainde Hichilema (UPND) elected president, defeating incumbent Edgar Lungu (PF); Lungu conceded 16 August."}, {"url":
"https://en.wikipedia.org/wiki/2016_Zambian_general_election", "title": "2016 Zambian general election", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03", "snippet": "Edgar Lungu re-elected
with a majority in the first round, defeating Hakainde Hichilema; PF won National Assembly majority."}, {"url": "https://en.wikipedia.org/wiki/2015_Zambian_presidential_election", "title": "2015
Zambian presidential election", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03", "snippet": "Edgar Lungu (PF) won by 27,757 votes (1.68%) over Hakainde Hichilema (UPND)."}, {"url":
"https://en.wikipedia.org/wiki/2011_Zambian_general_election", "title": "2011 Zambian general election", "domain": "en.wikipedia.org", "accessed_at": "2026-07-03", "snippet": "Michael Sata (PF) won
presidency defeating incumbent Rupiah Banda (MMD); PF largest party in National Assembly."}, {"url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf",
"title": "Credibility of an Opinion Poll: The Case of the 2021 General Elections in Zambia (Magasu)", "domain": "rsisinternational.org", "accessed_at": "2026-07-03", "snippet": "PSAZ predicted ECL
40.4%/HH 30.33%; Zambia Decides predicted ECL 56%; actual HH 59.02% (2,852,348) vs ECL 38.71% (1,870,780)."}, {"url": "https://mg.co.za/news/africa/2021-07-09-two-surveys-two-wildly-different-
predictions-for-zambia-s-election/", "title": "Two surveys, two wildly different predictions for Zambia's election", "domain": "mg.co.za", "accessed_at": "2026-07-03", "snippet": "PSAZ poll gave Lungu
44.5% / Hichilema 30.3%; Afrobarometer Dec 2020 gave PF 22.9% / UPND 25.2% with 45.6% DK; PSAZ criticized as flawed/pro-government."}, {"url": "https://www.aljazeera.com/news/2015/1/25/zambias-ruling-
party-candidate-wins-presidential-vote", "title": "Zambia's ruling party candidate wins presidential vote", "domain": "aljazeera.com", "accessed_at": "2026-07-03", "snippet": "Edgar Lungu won the 2015
presidential election with 48.33% of the vote."}, {"url": "https://www.africanews.com/2016/08/13/live-zambia-elections-2016-official-results-announced/", "title": "Zambia Elections: President Lungu
wins by 50.35%, opposition protests", "domain": "africanews.com", "accessed_at": "2026-07-03", "snippet": "Lungu declared winner of 2016 election with 50.35%."}, {"url":
"https://peoplesdispatch.org/2021/08/16/zambia-election-hakainde-hichilema-is-the-president-elect-incumbent-edgar-lungu-defeated/", "title": "Zambia election: Hichilema president-elect, incumbent
Lungu defeated", "domain": "peoplesdispatch.org", "accessed_at": "2026-07-03", "snippet": "Hichilema secured 2,810,757 votes (155/156 constituencies); turnout 70.95%."}, {"url":
"https://www.theafricareport.com/8314/zambia-michael-sata-wins-presidential-elections/", "title": "Zambia: Michael Sata wins presidential elections", "domain": "theafricareport.com", "accessed_at":
"2026-07-03", "snippet": "Sata won 2011 with 43% for PF; Banda (MMD) received 36.1%."}, {"url": "https://www.elections.org.zm/wp-content/uploads/2022/09/2016-PresidentialResults2016.pdf", "title":
"ECZ Public Notice 2016 Presidential Election Results", "domain": "elections.org.zm", "accessed_at": "2026-07-03", "snippet": "Official Electoral Commission of Zambia 2016 presidential results."}],
"key_facts": [], "data_points": [{"metric": "2011 presidential vote share - Michael Sata (PF, winner)", "value": 42.98, "unit": "percent", "as_of": "2011-09-23", "source_url":
"https://en.wikipedia.org/wiki/2011_Zambian_general_election"}, {"metric": "2011 presidential vote share - Rupiah Banda (MMD, incumbent, defeated)", "value": 36.1, "unit": "percent", "as_of":
"2011-09-23", "source_url": "https://www.theafricareport.com/8314/zambia-michael-sata-wins-presidential-elections/"}, {"metric": "2015 presidential vote share - Edgar Lungu (PF, ruling party,
winner)", "value": 48.33, "unit": "percent", "as_of": "2015-01-24", "source_url": "https://www.aljazeera.com/news/2015/1/25/zambias-ruling-party-candidate-wins-presidential-vote"}, {"metric": "2015
presidential vote share - Hakainde Hichilema (UPND)", "value": 46.67, "unit": "percent", "as_of": "2015-01-24", "source_url": "https://en.wikipedia.org/wiki/2015_Zambian_presidential_election"},
{"metric": "2015 winning margin (Lungu over Hichilema)", "value": 1.68, "unit": "percent", "as_of": "2015-01-24", "source_url": "https://en.wikipedia.org/wiki/2015_Zambian_presidential_election"},
{"metric": "2016 presidential vote share - Edgar Lungu (PF, incumbent, re-elected)", "value": 50.35, "unit": "percent", "as_of": "2016-08-15", "source_url":
"https://www.africanews.com/2016/08/13/live-zambia-elections-2016-official-results-announced/"}, {"metric": "2016 presidential vote share - Hakainde Hichilema (UPND)", "value": 47.63, "unit":
"percent", "as_of": "2016-08-15", "source_url": "https://en.wikipedia.org/wiki/2016_Zambian_general_election"}, {"metric": "2021 presidential vote share - Hakainde Hichilema (UPND, winner)", "value":
59.02, "unit": "percent", "as_of": "2021-08-16", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 presidential vote share -
Edgar Lungu (PF, incumbent, defeated)", "value": 38.71, "unit": "percent", "as_of": "2021-08-16", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-
Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 Hichilema total votes", "value": 2852348.0, "unit": "votes", "as_of": "2021-08-16", "source_url":
"https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 Lungu total votes", "value": 1870780.0, "unit": "votes", "as_of": "2021-08-16",
"source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 voter turnout", "value": 70.95, "unit": "percent", "as_of": "2021-08-16",
"source_url": "https://peoplesdispatch.org/2021/08/16/zambia-election-hakainde-hichilema-is-the-president-elect-incumbent-edgar-lungu-defeated/"}, {"metric": "2021 PSAZ poll prediction - Lungu (ECL)",
"value": 40.4, "unit": "percent", "as_of": "2021-07-04", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 PSAZ poll
prediction - Hichilema (HH)", "value": 30.33, "unit": "percent", "as_of": "2021-07-04", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"},
{"metric": "2021 'Zambia Decides' poll prediction - Lungu (ECL)", "value": 56.0, "unit": "percent", "as_of": "2021-07-01", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-
Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 'Zambia Decides' poll prediction - Hichilema (HH)", "value": 41.0, "unit": "percent", "as_of": "2021-07-01", "source_url":
"https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "2021 Afrobarometer (Dec 2020) - UPND/Hichilema support", "value": 25.2, "unit": "percent",
"as_of": "2020-12-31", "source_url": "https://mg.co.za/news/africa/2021-07-09-two-surveys-two-wildly-different-predictions-for-zambia-s-election/"}, {"metric": "2021 Afrobarometer (Dec 2020) -
PF/Lungu support", "value": 22.9, "unit": "percent", "as_of": "2020-12-31", "source_url": "https://mg.co.za/news/africa/2021-07-09-two-surveys-two-wildly-different-predictions-for-zambia-s-
election/"}, {"metric": "2021 Afrobarometer (Dec 2020) - refused/don't know", "value": 45.6, "unit": "percent", "as_of": "2020-12-31", "source_url": "https://mg.co.za/news/africa/2021-07-09-two-
surveys-two-wildly-different-predictions-for-zambia-s-election/"}, {"metric": "PSAZ poll error vs actual for Hichilema (understatement)", "value": 28.69, "unit": "percentage points", "as_of":
"2021-08-16", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}, {"metric": "Lungu vote-share change 2016 to 2021", "value": -11.64, "unit":
"percentage points", "as_of": "2021-08-16", "source_url": "https://rsisinternational.org/journals/ijriss/Digital-Library/volume-5-issue-9/164-168.pdf"}], "created_at": "2026-07-03T14:13:48.698575Z",
"updated_at": "2026-07-03T14:13:48.698575Z", "stale_after": "2026-07-17T14:13:48.698575Z", "state": "fresh", "revision_history": [], "session_id": "f55dfcad-e97e-4f93-a13d-8eee0f539977",
"follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💭 Thinking



## 💬 Response

Let me save findings and run a Monte Carlo mixture simulation.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import numpy as np\nnp.random.seed(42)\nN=200000\n\n# Scenario mixture for HH first-round vote share\n# Base case: HH wins comfortably, poll (60%) discounted for Zambian poll unreliability + economic grievances\n# Upside: fragmentation + machinery + delimitation deliver big margin, poll accurate/under\n# Downside: economic discontent, opposition (Mundubile) momentum, HH near runoff threshold\n\ncomps = [\n    (\"base\",   0.50, 56.0, 4.0),\n    (\"upside\", 0.23, 64.0, 4.5),\n    (\"down\",   0.27, 48.5, 5.0),\n]\nlabels=[c[0] for c in comps]\nweights=np.array([c[1] for c in comps]); weights/=weights.sum()\ndraws=np.random.choice(len(comps),size=N,p=weights)\nsamples=np.zeros(N)\nfor i,(name,w,mu,sd) in enumerate(comps):\n    m=draws==i\n    samples[m]=np.random.normal(mu,sd,m.sum())\n\n# clip to plausible physical range (can win with plurality but 50%+1 needed to avoid runoff; share can be <50)\nsamples=np.clip(samples,30,78)\n\npcts=[1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nvals=np.percentile(samples,pcts)\nfor p,v in zip(pcts,vals):\n    print(f\"P{p}: {v:.1f}\")\nprint(\"mean\",round(samples.mean(),2))\nprint(\"P(>50)\",round((samples>50).mean(),3))\nprint(\"P(<50)\",round((samples<50).mean(),3))\nprint(\"P(>60)\",round((samples>60).mean(),3))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P1: 39.5\nP5: 44.0\nP10: 46.6\nP20: 50.0\nP25: 51.2\nP30: 52.3\nP40: 54.2\nP50: 55.8\nP60: 57.5\nP70: 59.4\nP75: 60.5\nP80: 61.7\nP90: 65.0\nP95: 67.6\nP99: 71.7\nmean
55.81\nP(>50) 0.799\nP(<50) 0.201\nP(>60) 0.27\n", "stderr": "", "duration_ms": 291}
```

## 💭 Thinking



## 💬 Response

The simulation gives a well-calibrated distribution. Let me checkpoint via reflection.

## 💭 Thinking


