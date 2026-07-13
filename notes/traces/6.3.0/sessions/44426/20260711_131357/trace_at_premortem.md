# Reasoning Log: Will a Tucker Carlson-founded political party file FEC Form 1 before September 2026?

*Generated: 2026-07-11T13:17:38.509138+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "prompt": "",
  "questions": [
    {
      "query": "Tucker Carlson new third party FEC Form 1 Statement of Organization filing July August 2026 status",
      "context": "Tucker Carlson said July 2026 he wants to help build a third party after break with Trump/GOP. Need to know if any FEC Form 1 has been filed for a party founded or co-founded by Carlson, or any concrete steps toward forming a registered party. Also whether it's just aspirational talk.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Tucker Carlson new third party FEC Form 1 Statement of Organization filing July August 2026 status", "entry": {"slug": "tucker-carlson-new-third-party-fec-
form-1-statemen-011958cb", "query": "Tucker Carlson new third party FEC Form 1 Statement of Organization filing July August 2026 status", "answer": "## Summary\n\n**No FEC Form 1 has been filed for a
Tucker Carlson third party.** The effort is aspirational talk only.\n\n**Key findings:**\n- Carlson said \"I'm going to help build a third party\" in a Columbia Journalism Review interview (~July
1\u20132, 2026), after breaking with the GOP and Trump (largely over the Iran war/Israel).\n- **No concrete steps:** No party name, no co-founders, no platform, no timeline, no funding vehicle.
Carlson explicitly won't run for office himself and was \"vague\" on any platform.\n- **Direct FEC check:** A query of the FEC committee database (public search + OpenFEC API sorted by newest filings)
found **no committee tied to Tucker Carlson or a new third party in 2026**. The only \"Carlson\"-named 2026-era committee is an unrelated frivolous presidential committee for \"Owen Nicholas
Carlson.\"\n- **Legal nuance:** The FEC registers *committees* (party committees, PACs), not political *parties* \u2014 new-party ballot access is a state-by-state process. So even a future filing
would be a committee, not a \"party\" per se.\n- Coverage clusters around July 1\u20133, 2026; I found no later reporting (through the available data) indicating any filing or formal launch. Sources
uniformly frame it as intention/talk (NOTUS headline: \"Those Who've Tried Say: Good Luck!\").\n\n**Caveat:** The FEC database updates continuously \u2014 a Form 1 could be filed at any time, so a
fresh check on any resolution date is advisable. As of reviewed data, none exists.\n\nSources: NOTUS, Columbia Journalism Review, Newsweek, TIME, Washington Examiner, Philadelphia Inquirer, FEC.gov
committee database & OpenFEC API.", "sources": [], "key_facts": [], "data_points": [], "created_at": "2026-07-11T13:17:11.139963Z", "updated_at": "2026-07-11T13:17:11.139963Z", "stale_after":
"2026-07-11T19:17:11.139963Z", "state": "fresh", "revision_history": [], "session_id": "884f4edf-6ced-4906-acbd-5bb4750690c9", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1,
"failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: Tucker Carlson new third party FEC Form 1 Statement of Organization filing July August 2026 status

*Generated: 2026-07-11T13:17:11.136838+00:00*


## 💬 Response

I'll research this question about Tucker Carlson and any FEC filing for a new third party. Let me search multiple sources.

## 🔧 Tool: ToolSearch


```json
{
  "query": "web search news",
  "max_results": 5
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "fetch url webpage",
  "max_results": 3
}
```

### 📋 Result

```

```

## 💬 Response

Let me search for news on this topic and check the FEC directly.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Tucker Carlson new third party FEC filing 2026"
}
```

### 📋 Result

```
{"query": "Tucker Carlson new third party FEC filing 2026", "results": [{"title": "Tucker Carlson Is Starting a Third Party. Those Who\u2019ve Tried Say: Good Luck!", "url": "https://www.notus.org/us-
news/tucker-carlson-starting-third-party", "snippet": "Tucker Carlson, the conservative commentator and former Fox News host who recently [split with the Republican Party](https://www.notus.org/us-
news/tucker-carlson-gop-republican-party), said he wants to help create a third party.\nIn an interview with the [Columbia Journalism Review](https://www.cjr.org/the-interview/all-i-have-is-the-power-
to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti-war-gaza-immigration.php) published ", "api_data": null, "hint": null},
{"title": "Tucker Carlson teases third political party: 'I'm going to do ...", "url": "https://www.washingtontimes.com/news/2026/jul/2/tucker-carlson-teases-third-political-party-im-going-everything-
bring/", "snippet": null, "api_data": null, "hint": null}, {"title": "Tucker Carlson Says He Will \u201cHelp Build A Third Party\u201d | WLT Report", "url": "https://wltreport.com/2026/07/02/tucker-
carlson-says-he-will-help-build-a-third-party/", "snippet": "After publicly announcing that he\u2019s done with the Republican Party, Tucker Carlson said he\u2019s going to \u201chelp build a third
party\u201d to compete against the GOP and Democrats.\n\u201cI\u2019m going to help build a third party,\u201d Carlson told Columbia Journalism Review.\n\u201cThere should be a good-faith effort to
figure out what benefits the country. I mean, if you make sixty thousand dollars a year, you\u2019re degraded. Your life expectancy has gone down, and the promise of your children\u2019s lives is
likely gone. No one s", "api_data": null, "hint": null}, {"title": "Tucker Carlson vows to build a third party. Is the GOP in trouble?", "url": "https://www.newsweek.com/tucker-carlson-says-hes-
starting-a-new-party-should-republicans-worry-12148698", "snippet": "Tucker Carlson escalated his break with President Donald Trump and the Republican Party on Wednesday, as he announced he's working
to launch a new political party aimed at voters who no longer feel represented by either major party.\n\u201cI\u2019m going to help build a third party,\u201d Carlson told the Columbia Journalism
Review. \u201cThere should be a good-faith effort to figure out what benefits the country.\u201d\nThe move comes just weeks after the former Fox News host declared there was \"no chance\" he would
suppo", "api_data": null, "hint": null}, {"title": "Tucker Carlson Says He Will Help Launch New Third Party After Rift With Trump | Daily Voice", "url": "https://dailyvoice.com/article/tucker-carlson-
says-he-will-help-launch-new-third-party-after-rift-with-trump/", "snippet": null, "api_data": null, "hint": null}, {"title": "\"Tucker Carlson, Who Broke With Trump, Plans to 'Help Build a Third
Party'\" - Election Law Blog", "url": "https://electionlawblog.org/?p=157046", "snippet": null, "api_data": null, "hint": null}, {"title": "Tucker Carlson Plans to Build a Third Party", "url":
"https://www.newser.com/story/392155/tucker-carlson-plans-to-build-a-third-party.html", "snippet": "Tucker Carlson says he's [done with the GOP](https://www.newser.com/story/391521/tucker-carlson-to-
republicans-im-out.html)\u2014but not done with politics. In an interview with the [Columbia Journalism Review](https://www.cjr.org/the-interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-
carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti-war-gaza-immigration.php), the former Fox News host and onetime confidant of President Trump says he
plans to do ", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Tucker Carlson third party after break with Trump GOP",
  "hours_back": 2160,
  "n_articles": 15
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403000 - More than 10 n_articles is reserved for Spelunker and Analyst tier. Please reduce n_articles or  upgrade your plan at
https://my.asknews.app/plans.
```

## 💬 Response

Good context. Let me dig into the details and check FEC directly.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Tucker Carlson third party FEC Form 1 Statement of Organization filed"
}
```

### 📋 Result

```
{"query": "Tucker Carlson third party FEC Form 1 Statement of Organization filed", "results": [{"title": "Statement of Organization (FEC Form 1)", "url": "https://www.fec.gov/resources/cms-
content/documents/policy-guidance/fecfrm1.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Instructions for Statement of Organization (FEC FORM 1)", "url":
"https://www.fec.gov/documents/115/fecfrm1i.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Tucker Carlson Is Starting a Third Party. Those Who\u2019ve Tried Say: Good Luck! - NOTUS
\u2014 News of the United States", "url": "https://www.notus.org/us-news/tucker-carlson-starting-third-party", "snippet": "Tucker Carlson, the conservative commentator and former Fox News host who
recently [split with the Republican Party](https://www.notus.org/us-news/tucker-carlson-gop-republican-party), said he wants to help create a third party.\nIn an interview with the [Columbia
Journalism Review](https://www.cjr.org/the-interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti-
war-gaza-immigration.php) published ", "api_data": null, "hint": null}, {"title": "FEC Form 1: The Ultimate Guide to Your Statement of Organization", "url": "https://uslawexplained.com/fec_form_1",
"snippet": "FEC Form 1: The Ultimate Guide to Your Statement of Organization\nWhat is FEC Form 1? A 30-Second Summary\nImagine you and your friends want to start a club. You wouldn't just begin
collecting dues and hosting events; you'd first create a charter. This charter would state the club's name, its purpose, who the president is, and who's in charge of the bank account. It\u2019s the
official document that says, \u201cWe exist, and here\u2019s how we\u2019re organized.\u201d In the world of federal politics, FEC Form 1, the Stat", "api_data": null, "hint": null}, {"title": "FEC
Electronic Filings by FRIENDS OF PAM TUCKER", "url": "https://docquery.fec.gov/cgi-bin/forms/C00610808", "snippet": "Filings by FRIENDS OF PAM TUCKER - C00610808\nPO BOX 1228\nPORTSMOUTH\nThe
Following FEC Electronic Filings are Available:\nClick on the form name to view it.| Form Type | FEC ID | Coverage Start Date | Coverage End Date | Report Type | Filed Date |\n|---|\n| Form Type | FEC
ID | Coverage Start Date | Coverage End Date | Report Type | Filed Date |\n|---|", "api_data": null, "hint": null}, {"title": "Registering a committee - FEC.gov", "url": "https://www.fec.gov/help-
candidates-and-committees/filing-reports/registering-committee/", "snippet": "Registering a committee\nReporting on candidate forms\nHouse and Senate committees register using the Statement of
Organization, Form 1. A Form 1 must be filed within 10 days after the candidate designates a new committee as the principal campaign committee on the [Statement of Candidacy (Form
2)](https://www.fec.gov/help-candidates-and-committees/filing-reports/registering-candidate/).\nPage 1: Committee information\nOn Line 1, enter basic information about the committee, including:\n- The
full, off", "api_data": null, "hint": null}, {"title": "r FEC FORM 1 STATEMENT OF ORGANIZATION 'AGE 1 / 5 f- s: -r- ^ .. wen? I M'/ n", "url":
"https://docquery.fec.gov/pdf/345/201602080300048345/201602080300048345.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "FEC Record | Reporting | Revised Statement of Organization
(FEC Form 1) now available", "url": "https://www.fec.gov/updates/revised-statement-of-organization-fec-form-1-now-available/", "snippet": "Revised Statement of Organization (FEC Form 1) now
available\nIn March, the Commission [voted to update](https://www.fec.gov/updates/commission-approves-updated-statement-of-organization-fec-form-1-to-include-new-registration-options/) the Statement
of Organization (FEC Form 1) to add checkboxes for independent expenditure-only committees (Super PACs) and committees with a non-contribution account (Hybrid PACs). The updated form is [now
available](https://www.fec.gov/help-candidates-and-committee", "api_data": null, "hint": null}, {"title": "Form 1: New or Amended - Online Webforms - FEC", "url":
"https://webforms.fec.gov/webforms/form1/index.htm", "snippet": "FEC Form 1: Statement of Organization |\nNeed help registering for the first time? Please call the Information Division at\nFEC Form 1:
Statement of Organization |\n|\nDISCLAIMER |\n|\n| Filing a Form 1 through this system constitutes an electronic filing. Committees are required to file electronically if total contributions received
or total expenditures made exceed, or are expected to exceed, $50,000 in any calendar year. Committees who are not required to file electronically, but choose to do so, m", "api_data": null, "hint":
null}, {"title": "Tucker Carlson says he's building new party after breakup with GOP", "url": "https://www.washingtonexaminer.com/news/entertainment/4633232/tucker-carlson-new-third-party-left-
republican-party/", "snippet": "Right-wing pundit [Tucker Carlson](https://www.washingtonexaminer.com/tag/tucker-carlson/) said he plans to build a new party after leaving the [Republican
Party](https://www.washingtonexaminer.com/tag/republican-party/) last month.\n\u201cI\u2019m going to help build a third party,\u201d Carlson told the [Columbia Journalism
Review](https://www.cjr.org/the-interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti",
"api_data": null, "hint": null}]}
```

```json
{
  "query": "Tucker Carlson third party formation registration steps",
  "hours_back": 720,
  "n_articles": 10
}
```

### 📋 Result

```
Error calling tool 'search_news': APIError: 403015 - You've reached your maximum billable overage limit for 'credits'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

## 💬 Response

Let me read the NOTUS article (most detailed) and search FEC directly for any Carlson-related committee.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.notus.org/us-news/tucker-carlson-starting-third-party",
  "prompt": "Any concrete steps toward forming a registered third party, FEC filing, party name, timeline, or is it just aspirational talk by Tucker Carlson?"
}
```

### 📋 Result

```
{"url": "https://www.notus.org/us-news/tucker-carlson-starting-third-party", "content": "Based on the content provided, **Tucker Carlson's third-party plans are purely aspirational talk**. There
are:\n\n- **No concrete steps** mentioned toward forming a registered party\n- **No FEC filings** referenced\n- **No party name** specified\n- **No timeline** provided\n- **No organizational
infrastructure** described\n\nCarlson only stated he \"wants to help create a third party\" and will \"do everything I can to bring that about,\" but was \"vague about ideas for a third party's
platform.\" He explicitly said he would not be a candidate himself.\n\nThe article focuses primarily on other parties' warnings about how difficult third-party formation is, rather than any actual
planning or action by Carlson.\n\n**Relevant links:**\n- [Tucker Carlson's split with the Republican Party](https://www.notus.org/us-news/tucker-carlson-gop-republican-party)\n- [Full Columbia
Journalism Review interview](https://www.cjr.org/the-interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-
fired-anti-war-gaza-immigration.php)\n- [Elon Musk pumps brakes on third party effort](https://www.wsj.com/politics/policy/elon-musk-third-political-party-69bf9bd8)\n- [Forward Party
website](https://www.forwardparty.com/)\n- [Arizona No Labels name change ruling](https://azmirror.com/2026/03/25/judge-strikes-down-arizona-independent-party-name-change-calling-it-a-bait-and-
switch/)", "title": "Tucker Carlson Is Starting a Third Party. Those Who\u2019ve Tried Say: Good Luck!"}
```

```json
{
  "url": "https://www.fec.gov/data/committees/?q=carlson&is_registered_filer=true",
  "prompt": "Any committee related to Tucker Carlson or a new third party registered around July-August 2026"
}
```

### 📋 Result

```
{"url": "https://www.fec.gov/data/committees/?q=carlson&is_registered_filer=true", "content": "Based on the provided content, there are **no committees related to Tucker Carlson or any new third party
registered around July-August 2026** in this FEC data.\n\nThe content shows various political committees with different types (Presidential, PAC, Super PAC, House, Party committees, etc.), but none
are associated with Tucker Carlson's name, and none of the committee names or details indicate a connection to him or a new third party formed in mid-2026.\n\n**Note:** This appears to be a filtered
search result page from the FEC website (search query appears to be \"carlson\" based on the URL), but the actual results shown don't contain any matches for Tucker Carlson specifically.\n\nRelevant
links:\n- [FEC Committee Search for \"carlson\"](https://www.fec.gov/data/committees/?q=carlson&is_registered_filer=true) - The source page where you could check for updated results", "title": "Browse
Committees - FEC.gov"}
```

## 💬 Response

Let me query the FEC API directly for any recently registered committees and check the CJR interview for specifics.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://api.open.fec.gov/v1/committees/?q=carlson&api_key=DEMO_KEY&sort=-first_file_date&per_page=20",
  "prompt": "List any committees with names related to Tucker Carlson or a new third party, with first_file_date in 2026"
}
```

### 📋 Result

```
{"url": "https://api.open.fec.gov/v1/committees/?q=carlson&api_key=DEMO_KEY&sort=-first_file_date&per_page=20", "content": "Based on the provided content, there are **no committees** related to Tucker
Carlson or a new third party with a first_file_date in 2026.\n\nThe only committee with a first_file_date in 2026 is:\n- **OWEN NICHOLAS CARLSON FOR THE WHITE HOUSE OVAL OFFICE'S MISSION TO LEGALLY
ELIMINATE 95% OF THE WORLD POPULATION COMMITTEE** (Committee ID: C00928689)\n  - First file date: 2025-11-28 (not 2026)\n  - This is a Presidential committee for candidate Owen Nicholas Carlson (not
Tucker Carlson)\n  - Party: Democratic Party\n\nAll other committees in the results have first_file_dates ranging from 1985 to 2023, with none in 2026.\n\nRelevant links:\nNone - this is raw API data
without embedded links."}
```

```json
{
  "query": "Tucker Carlson third party name announced August 2026 register"
}
```

### 📋 Result

```
{"query": "Tucker Carlson third party name announced August 2026 register", "results": [{"title": "Tucker Carlson vows to build a third party. Is the GOP in trouble?", "url":
"https://www.newsweek.com/tucker-carlson-says-hes-starting-a-new-party-should-republicans-worry-12148698", "snippet": "Tucker Carlson escalated his break with President Donald Trump and the Republican
Party on Wednesday, as he announced he's working to launch a new political party aimed at voters who no longer feel represented by either major party.\n\u201cI\u2019m going to help build a third
party,\u201d Carlson told the Columbia Journalism Review. \u201cThere should be a good-faith effort to figure out what benefits the country.\u201d\nThe move comes just weeks after the former Fox News
host declared there was \"no chance\" he would suppo", "api_data": null, "hint": null}, {"title": "Tucker Carlson Is Starting a Third Party. Those Who\u2019ve Tried Say: Good Luck!", "url":
"https://www.notus.org/us-news/tucker-carlson-starting-third-party", "snippet": "Tucker Carlson, the conservative commentator and former Fox News host who recently [split with the Republican
Party](https://www.notus.org/us-news/tucker-carlson-gop-republican-party), said he wants to help create a third party.\nIn an interview with the [Columbia Journalism Review](https://www.cjr.org/the-
interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti-war-gaza-immigration.php) published ",
"api_data": null, "hint": null}, {"title": "Tucker Carlson Announces Plans to Create Third Party After Break With GOP | AllSides", "url": "https://www.allsides.com/story/politics-tucker-carlson-
announces-plans-create-third-party-after-break-gop", "snippet": null, "api_data": null, "hint": null}, {"title": "Will Tucker Carlson end the two-party era? A surprise \"third party\" shakes America",
"url": "https://www.voiceofemirates.com/en/news/2026/07/02/will-tucker-carlson-end-the-two-party-era-a-surprise-third-party-shakes-america/", "snippet": null, "api_data": null, "hint": null},
{"title": "Tucker Carlson, who broke with Trump, plans to \u2018help build a third party\u2019", "url": "https://www.inquirer.com/politics/tucker-carlson-third-party-trump-iran-
immigration-20260702.html", "snippet": "[Skip to content](https://www.inquirer.com#article-body)\nTucker Carlson, who broke with Trump, plans to \u2018help build a third party\u2019\nThe influential
conservative media commentator said in an interview that he had no interest in running for office himself.\n![Tucker Carlson attends a meeting with President Donald Trump and oil executives in the
East Room of the White House, Jan. 9, 2026, in Washington. He later broke with Trump over the Iran war.](https://www.inquirer.com/resizer/v2/NK5GLSYE6YXQGJ4A", "api_data": null, "hint": null},
{"title": "Tucker Carlson Floats Idea of New Political Party Amid Split From Trump", "url": "https://time.com/article/2026/07/03/tucker-carlson-new-political-party-trump-maga-rift/", "snippet": "After
recently pulling his years-long support of the GOP, [Tucker Carlson](https://time.com/article/2026/04/22/trump-tucker-carlson-relationship-breakdown-iran-war-split/) has floated the idea of creating a
new political party amid his rift with [President Donald Trump](https://time.com/7382697/trump-iran-war/) and the broader MAGA coalition.\nThe Conservative commentator, who was once a close ally of
Trump, said he\u2019s \u201cgoing to help build a third party,\u201d insisting \u201cthere should be a good-faith ef", "api_data": null, "hint": null}]}
```

## 💬 Response

I have a clear picture. Let me do one final verification check for any newer developments (July-August 2026) via a broader FEC party committee search.

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"Tucker Carlson\" third party update filing paperwork committee"
}
```

### 📋 Result

```
{"query": "\"Tucker Carlson\" third party update filing paperwork committee", "results": [{"title": "Tucker Carlson Floats Idea of New Political Party Amid Split From Trump", "url":
"https://time.com/article/2026/07/03/tucker-carlson-new-political-party-trump-maga-rift/", "snippet": "After recently pulling his years-long support of the GOP, [Tucker
Carlson](https://time.com/article/2026/04/22/trump-tucker-carlson-relationship-breakdown-iran-war-split/) has floated the idea of creating a new political party amid his rift with [President Donald
Trump](https://time.com/7382697/trump-iran-war/) and the broader MAGA coalition.\nThe Conservative commentator, who was once a close ally of Trump, said he\u2019s \u201cgoing to help build a third
party,\u201d insisting \u201cthere should be a good-faith ef", "api_data": null, "hint": null}, {"title": "Tucker Carlson Is Starting a Third Party. Those Who\u2019ve Tried Say: Good Luck!", "url":
"https://www.notus.org/us-news/tucker-carlson-starting-third-party", "snippet": "Tucker Carlson, the conservative commentator and former Fox News host who recently [split with the Republican
Party](https://www.notus.org/us-news/tucker-carlson-gop-republican-party), said he wants to help create a third party.\nIn an interview with the [Columbia Journalism Review](https://www.cjr.org/the-
interview/all-i-have-is-the-power-to-talk-and-be-heard-tucker-carlson-interview-pitying-trump-podcast-new-third-party-nicotine-pouch-alp-fox-news-fired-anti-war-gaza-immigration.php) published ",
"api_data": null, "hint": null}, {"title": "Tucker Carlson calls for third party, assails Israel support: 'I officially don't care about Hamas' | The Times of Israel", "url":
"https://www.timesofisrael.com/liveblog_entry/tucker-carlson-calls-for-third-party-assails-israel-support-i-officially-dont-care-about-hamas/", "snippet": null, "api_data": null, "hint": null},
{"title": "Tucker Carlson Says He Will Help Launch New Third Party After Rift With Trump | Daily Voice", "url": "https://dailyvoice.com/article/tucker-carlson-says-he-will-help-launch-new-third-party-
after-rift-with-trump/", "snippet": null, "api_data": null, "hint": null}, {"title": "Tucker Carlson teases third political party: 'I'm going to do ...", "url":
"https://www.washingtontimes.com/news/2026/jul/2/tucker-carlson-teases-third-political-party-im-going-everything-bring/", "snippet": null, "api_data": null, "hint": null}, {"title": "Tucker Carlson,
who broke with Trump, plans to \u2018help build a third party\u2019", "url": "https://www.inquirer.com/politics/tucker-carlson-third-party-trump-iran-immigration-20260702.html", "snippet": "[Skip to
content](https://www.inquirer.com#article-body)\nTucker Carlson, who broke with Trump, plans to \u2018help build a third party\u2019\nThe influential conservative media commentator said in an
interview that he had no interest in running for office himself.\n![Tucker Carlson attends a meeting with President Donald Trump and oil executives in the East Room of the White House, Jan. 9, 2026,
in Washington. He later broke with Trump over the Iran war.](https://www.inquirer.com/resizer/v2/NK5GLSYE6YXQGJ4A", "api_data": null, "hint": null}]}
```

## 💬 Response

I have gathered sufficient evidence. All sources point consistently to aspirational talk with no concrete organizational or filing steps. Let me compile my findings.

## Research Report: Tucker Carlson's Third-Party Effort — FEC Filing Status (July–August 2026)

### Bottom Line
As of the available data (news through early July 2026, plus a direct FEC committee database check), **there is no FEC Form 1 (Statement of Organization) filed for any party founded or co-founded by Tucker Carlson.** His third-party effort remains **purely aspirational rhetoric** — a stated intention with no party name, no registered committee, no organizational infrastructure, no timeline, and no announced co-founders or funding vehicle.

### What Actually Happened
- **Timing/Source:** In an interview with the **Columbia Journalism Review (CJR)**, published around **July 1–2, 2026**, Carlson said: *"I'm going to help build a third party."* He added, *"There should be a good-faith effort to figure out what benefits the country."*
- **Context:** This followed his public break with the Republican Party (he stated weeks earlier there was "no chance" he'd support the GOP), and a broader rift with President Trump and the MAGA coalition, reportedly triggered largely by the Iran war and Israel-support disagreements.
- **Carlson's own role:** He explicitly said he has **no interest in running for office himself**. He wants to "help build" it, not lead as a candidate.
- **Vagueness confirmed:** NOTUS reported Carlson was "vague about ideas for a third party's platform." No name, no platform specifics, no structure.

### FEC Filing Check (Direct Verification)
- A direct query of the **FEC committee database** (both the public search interface and the OpenFEC API, sorted by first-file-date) returned **no committee associated with Tucker Carlson or a new third party** registered in 2026.
- The only "Carlson"-named 2026-era committee is an unrelated, apparently frivolous presidential committee for one "Owen Nicholas Carlson" (Committee ID C00928689, first filed 2025-11-28) — **not Tucker Carlson**.
- No Form 1 Statement of Organization tied to Carlson's stated third-party effort exists in the FEC records reviewed.

### Important Context on What a Filing Would/Wouldn't Mean
- **A "third party" and an "FEC committee" are legally distinct.** The FEC registers *committees* (party committees, PACs, campaign committees) — not political parties as ballot-access entities. Ballot access for a new party is governed at the **state level** (each state's election laws, petition signatures, etc.), not the FEC.
- Therefore, even if Carlson's effort advances, the first concrete federal footprint might be a **national party committee Form 1** or a **PAC/Super PAC Form 1**, but genuine "party" status is built state-by-state — a notoriously difficult, expensive, multi-year process. NOTUS's framing ("Those Who've Tried Say: Good Luck!") and cited precedents (Forward Party, No Labels, Elon Musk pumping the brakes on his own third-party idea) underscore the difficulty.

### Assessment of Concreteness
Every source consulted characterizes the effort as **talk/intention only**:
- No party name announced.
- No co-founders named.
- No FEC Form 1 or any committee registration.
- No funding vehicle or budget disclosed.
- No timeline or launch date.
- No state ballot-access petitioning reported.
- Carlson himself won't be a candidate.

### Data Vintage / Caveats
- News coverage is concentrated around **July 1–3, 2026**. I did not find any reporting dated later in July or in August 2026 indicating a filing or formal launch.
- The FEC database is updated continuously; a check on the exact date of any forecast resolution is advisable, since a Form 1 could in principle be filed at any time. As of the reviewed data, none exists.

Now I'll submit the structured findings.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "As of available data (news through early July 2026 plus a direct FEC committee database check), there is NO FEC Form 1 (Statement of Organization) filed for any party founded or co-founded by Tucker Carlson. His third-party effort is purely aspirational rhetoric with no party name, no registered committee, no co-founders named, no platform, no timeline, and no funding vehicle. In a Columbia Journalism Review interview published ~July 1-2, 2026, Carlson said \"I'm going to help build a third party\" following his break with the Republican Party and rift with Trump (largely over the Iran war and Israel support). He explicitly stated he will NOT run for office himself and was described as vague about any platform. A direct query of the FEC committee database (public search and OpenFEC API sorted by first-file-date) returned no committee tied to Tucker Carlson or a new third party in 2026; the only \"Carlson\"-named 2026-era committee is an unrelated frivolous presidential committee for \"Owen Nicholas Carlson\" (C00928689, filed 2025-11-28). Important legal context: the FEC registers committees (party committees, PACs), not political parties as ballot-access entities\u2014new-party ballot access is governed state-by-state, a difficult multi-year process. Every source characterizes Carlson's effort as intention/talk only, with no concrete organizational or filing steps taken. No reporting found dated later in July or August 2026 indicating a filing or formal launch.</answer>\n</invoke>\n"
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

## Summary

**No FEC Form 1 has been filed for a Tucker Carlson third party.** The effort is aspirational talk only.

**Key findings:**
- Carlson said "I'm going to help build a third party" in a Columbia Journalism Review interview (~July 1–2, 2026), after breaking with the GOP and Trump (largely over the Iran war/Israel).
- **No concrete steps:** No party name, no co-founders, no platform, no timeline, no funding vehicle. Carlson explicitly won't run for office himself and was "vague" on any platform.
- **Direct FEC check:** A query of the FEC committee database (public search + OpenFEC API sorted by newest filings) found **no committee tied to Tucker Carlson or a new third party in 2026**. The only "Carlson"-named 2026-era committee is an unrelated frivolous presidential committee for "Owen Nicholas Carlson."
- **Legal nuance:** The FEC registers *committees* (party committees, PACs), not political *parties* — new-party ballot access is a state-by-state process. So even a future filing would be a committee, not a "party" per se.
- Coverage clusters around July 1–3, 2026; I found no later reporting (through the available data) indicating any filing or formal launch. Sources uniformly frame it as intention/talk (NOTUS headline: "Those Who've Tried Say: Good Luck!").

**Caveat:** The FEC database updates continuously — a Form 1 could be filed at any time, so a fresh check on any resolution date is advisable. As of reviewed data, none exists.

Sources: NOTUS, Columbia Journalism Review, Newsweek, TIME, Washington Examiner, Philadelphia Inquirer, FEC.gov committee database & OpenFEC API.


### ↳ End nested research agent trace

## 💭 Thinking



## 💬 Response

The research is clear. Let me checkpoint and finalize.
