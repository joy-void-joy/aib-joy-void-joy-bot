# Reasoning Log: Will the community prediction be higher than 12.00% on 2026-04-10 for the Metaculus question "Will a federal judge be impeached by Republican Representatives in a partisan vote before January 3, 2027?"?

*Generated: 2026-03-31T16:52:40.288073+00:00*


## 💭 Thinking

Let me analyze this meta-prediction question carefully.

## Step 1: Parse the Resolution Criteria

This is a meta-prediction question asking: Will the community prediction (CP) on Metaculus question #36348 be **higher than 12.00%** on 2026-04-10 19:09:37?

Key details:
- Current CP (as of 2026-03-29): 12.00%
- The threshold is **strictly higher than** 12.00%
- Resolution date: 2026-04-10 (about 10 days from now)
- The target question is about whether a federal judge will be impeached by Republican Representatives in a partisan vote before January 3, 2027


- Looking at the historical CP snapshots, the prediction has hovered between 9-10% for most of the past month before jumping to 12% recently, so I need to assess whether this latest movement will push it above the threshold in the next 10 days.

## 💬 Response

I'll analyze this meta-prediction question about whether the Metaculus CP will be above 12% on April 10, 2026. Let me gather data.

## 🔧 Tool: mcp__markets__get_metaculus_questions


## 🔧 Tool: mcp__markets__get_cp_history


## 🔧 Tool: mcp__search__web_search


```json
{
  "post_id_list": [
    36348
  ]
}
```

### 📋 Result

```
{"post_id": 36348, "title": "Will a federal judge be impeached by Republican Representatives in a partisan vote before January 3, 2027?", "type": "binary", "url":
"https://www.metaculus.com/questions/36348", "background_info": "[Impeachment](https://en.wikipedia.org/wiki/Federal_impeachment_in_the_United_States) of federal judges in the United States is a rare
and serious action, typically reserved for cases involving significant misconduct or ethical violations. The process requires a majority vote in the House of Representative to impeach and a two-thirds
majority in the Senate to convict and remove the judge from office. [Historically](https://en.wikipedia.org/wiki/Federal_impeachment_in_the_United_States#List_of_federal_impeachments), very few
federal judges have been impeached and removed, and none solely for their judicial decisions.\n\nIn March 2025, President Donald Trump [called for](https://apnews.com/article/trump-judge-boasberg-
musk-impeachment-1019459fc9517231204b814fd6f36127) the impeachment of US District Judge James Boasberg after Boasberg issued a temporary restraining order halting deportations under the Alien Enemies
Act of 1798. Chief Justice John Roberts [responded](https://apnews.com/article/donald-trump-federal-judges-impeachment-29da1153a9f82106748098a6606fec39) by stating that impeachment is not an
appropriate response to disagreements over judicial decisions.\n\n*This forecast question was created by Bright Line Watch, a nonpartisan watchdog group. Forecast on their other questions*
[*here*](https://www.metaculus.com/c/brightlinewatch/)*.*&#x20;", "resolution_criteria": "This question will resolve as **Yes** if, before January 3, 2027, a United States federal judge is impeached
by the US House of Representatives with fewer than half of Democratic representatives voting for the impeachment.", "fine_print": "The reason for impeachment is immaterial for the purposes of this
question.\n\nConviction in the US Senate, which at the time of this question [requires](https://www.senate.gov/about/powers-procedures/impeachment.htm) a two-thirds vote to convict, is not necessary
for this question to resolve as **Yes**.&#x20;", "num_forecasters": 486, "community_prediction": null}
```

```json
{
  "post_id": 36348,
  "days": 60
}
```

### 📋 Result

```
Failed to fetch CP history: Client error '403 Forbidden' for url 'https://www.metaculus.com/api/aggregation_explorer/?post_id=36348&aggregation_methods=recency_weighted'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
```

```json
{
  "query": "federal judge impeachment Republican 2026"
}
```

### 📋 Result

```
{"query": "federal judge impeachment Republican 2026", "results": [{"title": "Republican senators ramp up impeachment rhetoric against judges", "url":
"https://www.nbcnews.com/politics/congress/republican-senators-impeachment-rhetoric-judges-judiciary-hearing-rcna247082", "snippet": "WASHINGTON \u2014 Republican senators on Wednesday increased their
scrutiny of federal judges whose rulings they've opposed, with some pushing for them [to be impeached](https://www.nbcnews.com/politics/congress/can-congress-impeach-federal-judge-why-it-wont-happen-
rcna196937).\nAttention at the Senate Judiciary Committee hearing focused on two judges: Washington-based U.S. District Judge James Boasberg and Maryland-based Deborah Boardman, both of whom have
[fallen foul of MAGA world](https://www.nbcn", "api_data": null, "hint": null}, {"title": "Senate Republicans Call to Impeach Federal Judges Over Rulings", "url": "https://news.bloomberglaw.com/us-
law-week/senate-republicans-call-to-impeach-federal-judges-over-rulings", "snippet": "Senate Judiciary Committee Republicans ramped up calls for the House to impeach a pair of federal judges caught in
President Donald Trump\u2019s crosshairs for rulings they issued seen as unfavorable to the administration.\nThe lawmakers at a hearing on Wednesday tore into Chief Judge James \u201cJeb\u201d
Boasberg of the Washington federal trial court for orders he signed related to former Special Counsel Jack Smith\u2019s probe of Trump\u2019s efforts to overturn the 2020 election.\n\u201cNo republic
can survive if its judge", "api_data": null, "hint": null}, {"title": "Impeachment and Removal of Judges, Explained | Brennan Center for Justice", "url": "https://www.brennancenter.org/our-
work/analysis-opinion/impeachment-and-removal-judges-explainer", "snippet": "Impeachment and Removal of Judges, Explained\nJudicial impeachment shouldn\u2019t be used to punish judges for their
rulings. Here\u2019s why.\nPart of\nFederal court decisions against some Trump administration policies have led to calls from the president\u2019s supporters to impeach judges, and in March 2025
President Trump himself said that a federal judge who ruled against the administration\u2019s deportation plans should be impeached. Chief Justice John Roberts
[responded](https://apnews.com/article/donald-trump", "api_data": null, "hint": null}, {"title": "GOP senators threaten to impeach judges who rule against Trump - Democracy Docket", "url":
"https://www.democracydocket.com/news-alerts/gop-senators-threaten-to-impeach-judges-who-rule-against-trump/", "snippet": "GOP senators threaten to impeach judges who rule against
Trump\n![](https://www.democracydocket.com/wp-content/uploads/2025/12/GettyImages-2244343280-1024x683.jpg)\nThe GOP ratcheted up their criticism of \u2014 and pressure on \u2014 the federal judiciary
Wednesday, arguing at a Senate Judiciary Committee panel that some of the judges who have ruled against President Donald Trump\u2019s administration deserve to be impeached.\nEven as the judiciary
faces increasing threats of violence, Republicans on the Federal", "api_data": null, "hint": null}, {"title": "Impeachment of Federal Judges", "url":
"https://constitutionallawreporter.com/article-03-section-01/impeachment-of-federal-judges/", "snippet": "United States Constitution\nPREAMBLE : We the People of the United States, in Order to form a
more perfect Union, establish Justice, insure\ndomestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty\nto ourselves and our Posterity,
do ordain and establish this Constitution\nImpeachment of Federal Judges\n| Introduction |\n|\nImportant Cases |\nIn the United States, the word \u201cimpeachment\u201d is merely the term for the
proceeding that begins the pr", "api_data": null, "hint": null}, {"title": "White House supports GOP impeachment efforts against 'rogue' federal judges | Fox News", "url":
"https://www.foxnews.com/politics/scoop-white-house-backs-impeaching-rogue-judges-accused-partisan-rulings", "snippet": "[Mike Johnson backs impeaching judges over 'egregious
abuses'](https://www.foxnews.com/video/6388047458112)\nSpeaker Mike Johnson said he would support judicial impeachments during his weekly House GOP leadership press conference.\nFIRST ON FOX: The
White House fully supports efforts on Capitol Hill to impeach [federal judges](https://www.foxnews.com/category/politics/federal-judges) who have gone \"totally rogue\" with partisan rulings, Fox News
Digital learned.\nA White House official told Fox News", "api_data": null, "hint": null}, {"title": "Impeaching Judges Over Politics Will Damage Courts, Both Parties", "url":
"https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/impeaching-judges-over-politics-will-damage-both-parties-courts", "snippet": "The House speaker expressed support recently for
efforts to impeach two judges whose rulings have angered the Trump administration. Should this occur, it would dramatically lower the bar to impeaching a judge, which legislators urging this action
may come to regret. Control of the House could change as soon as next year and judges whose rulings lawmakers agree with could find themselves in the crosshairs of impeachment proceedings simply for
doing their job.\nSpeaker Mike Johnson\u2019s [comments](htt", "api_data": null, "hint": null}, {"title": "Impeachment of federal judges - Ballotpedia", "url":
"https://ballotpedia.org/Impeachment_of_federal_judges", "snippet": "[Click here to see who's on your ballot](https://ballotpedia.org/Sample_Ballot_Lookup)\nImpeachment of federal judges\nArticle III
federal judges are appointed to life terms while serving \"during good Behaviour,\" as stated in Section 1 of [Article III](https://ballotpedia.org/Article_III) of the [United States
Constitution](https://ballotpedia.org/United_States_Constitution). Though it does not expressly state in the Constitution that judges may be impeached and removed from office, they fall unde",
"api_data": null, "hint": null}, {"title": "Bribery, corruption and intoxication: Here are some of the ways federal judges have been impeached", "url":
"https://news.northeastern.edu/2025/03/19/federal-judge-impeachment-history/", "snippet": "Bribery, corruption and intoxication: Here are some of the ways federal judges have been impeached\nCalls for
the impeachment of a federal judge have arisen in response to a decision against a Trump administration policy.\n![The Supreme Court building seen at sunset.](https://news.northeastern.edu/wp-
content/uploads/2025/03/Courts1400.jpg?w=1024)\nPresident Donald Trump and his supporters are calling for the impeachment of a federal judge who ordered a halt to the administration\u2019s effort to
deport ", "api_data": null, "hint": null}, {"title": "Judges and Judicial Administration \u2013 Journalist\u2019s Guide", "url": "https://www.uscourts.gov/data-news/reports/handbooks-
manuals/a-journalists-guide-federal-courts/judges-and-judicial-administration-journalists-guide", "snippet": "On this page\nThe Judiciary is an independent branch of government. Here is how judges are
appointed and how they administer the Third Branch.\nFederal Judges\nArticle III of the Constitution governs the appointment, tenure, and payment of Supreme Court justices, and federal circuit and
district judges. These judges, often referred to as \u201cArticle III judges,\u201d are nominated by the President and confirmed by the U.S. Senate. Article III states that these judges \u201chold
their office during good behavior", "api_data": null, "hint": null}]}
```

## 💬 Response

Let me get more recent news on whether impeachment proceedings have actually advanced in the House.

## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "query": "federal judge impeachment House Republicans 2026",
  "hours_back": 720,
  "string_guarantee": [
    "impeach"
  ],
  "categories": [
    "Politics"
  ]
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

```json
{
  "query": "judge Boasberg Boardman impeachment House vote 2026",
  "hours_back": 168
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

```json
{
  "post_id_list": [
    43002
  ]
}
```

### 📋 Result

```
{"post_id": 43002, "title": "Will the community prediction be higher than 12.00% on 2026-04-10 for the Metaculus question \"Will a federal judge be impeached by Republican Representatives in a
partisan vote before January 3, 2027?\"?", "type": "binary", "url": "https://www.metaculus.com/questions/43002", "background_info": "Metaculus is a crowdsourced forecast aggregation platform where
humans and bots compete to predict future events. Each question on Metaculus has a community prediction that aggregates all user's forecasts. As of this question launch, this aggregation is calculated
as a median of user forecasts weighted by recency. \n\n--------------------------------\n\nBelow are some details about the original Metaculus question: \n- Question URL:
https://www.metaculus.com/questions/36348\n- Original question title: Will a federal judge be impeached by Republican Representatives in a partisan vote before January 3, 2027?\n- The current
community prediction as of 2026-03-29: 12.00%\n- Historical community prediction (weekly snapshots):\n  - 2026-02-22: 9.00%\n  - 2026-03-01: 10.00%\n  - 2026-03-08: 10.00%\n  - 2026-03-15: 9.00%\n  -
2026-03-22: 10.00%\n\nOriginal resolution criteria: \n> This question will resolve as **Yes** if, before January 3, 2027, a United States federal judge is impeached by the US House of Representatives
with fewer than half of Democratic representatives voting for the impeachment.\n\nOriginal fine print: \n> The reason for impeachment is immaterial for the purposes of this question.\n> \n> Conviction
in the US Senate, which at the time of this question [requires](https://www.senate.gov/about/powers-procedures/impeachment.htm) a two-thirds vote to convict, is not necessary for this question to
resolve as **Yes**.&#x20;\n\nOriginal background: \n> [Impeachment](https://en.wikipedia.org/wiki/Federal_impeachment_in_the_United_States) of federal judges in the United States is a rare and serious
action, typically reserved for cases involving significant misconduct or ethical violations. The process requires a majority vote in the House of Representative to impeach and a two-thirds majority in
the Senate to convict and remove the judge from office. [Historically](https://en.wikipedia.org/wiki/Federal_impeachment_in_the_United_States#List_of_federal_impeachments), very few federal judges
have been impeached and removed, and none solely for their judicial decisions.\n> \n> In March 2025, President Donald Trump [called for](https://apnews.com/article/trump-judge-boasberg-musk-
impeachment-1019459fc9517231204b814fd6f36127) the impeachment of US District Judge James Boasberg after Boasberg issued a temporary restraining order halting deportations under the Alien Enemies Act
of 1798. Chief Justice John Roberts [responded](https://apnews.com/article/donald-trump-federal-judges-impeachment-29da1153a9f82106748098a6606fec39) by stating that impeachment is not an appropriate
response to disagreements over judicial decisions.\n> \n> *This forecast question was created by Bright Line Watch, a nonpartisan watchdog group. Forecast on their other questions*
[*here*](https://www.metaculus.com/c/brightlinewatch/)*.*&#x20;\n\n`{\"format\":\"metaculus_binary_cp_rises\",\"info\":{\"post_id\":36348,\"question_id\":35765,\"last_cp\":0.12}}`",
"resolution_criteria": "This question will resolve based on the community prediction of the Metaculus question found [here](https://www.metaculus.com/questions/36348) (i.e. the 'target question'). If
the community prediction of the target question on 2026-04-10 19:09:37 is higher than 12.00%, this question will resolve to 'Yes'. If it is lower or equal to 12.00%, this question will resolve to
'No'. If the target question has already resolved before this question opens, then this question will be annulled. If the target question resolves after this question opens, but before 2026-04-10
19:09:37, then this question will resolve to the same value as the target question.", "fine_print": "", "num_forecasters": 2, "community_prediction": null}
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "House Republicans impeach federal judge vote 2026 March",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "Kentucky House impeaches Fayette judge in historic vote", "url": "https://www.wuky.org/wuky-news/2026-03-20/kentucky-house-impeaches-fayette-judge-in-historic-vote", "snippet": "Kentucky
House impeaches Fayette judge in historic vote\n\n\n\n\u00a9 2026 WUKY\n\nMenu\n\n\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air Stations\n\n- On Air Now
Playing WUKY\n- On Air Now Playing The Break\n- On Air Now Playing WUKY Programming\n- On Air Now Playing Genre Free\n- On Air Now Playing Pop Rocks\n- On Air Now Playing UniverseCity\n- On Air Now
Playing Wildcat Country\n\nAll Streams\n\nNews\n\n# Kentucky House impeaches Fayette judge in historic vote\n\nWUKY | By Josh James\n\nPubli", "highlights": ["Kentucky House impeaches Fayette judge in
historic vote\n\n\n\n\u00a9 2026 WUKY\n\nMenu\n\n\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00 0:00\n\n0:00 0:00\n\nAvailable On Air Stations - On Air Now Playing WUKY\n- On Air Now Playing The
Break\n- On Air Now Playing WUKY Programming - On Air Now Playing Genre Free\n- On Air Now Playing Pop Rocks\n- On Air Now Playing UniverseCity   ...    All Streams\n\nNews\n\n# Kentucky House
impeaches Fayette judge in historic vote\n\nWUKY | By Josh James Published March 20, 2026 at 3:38 PM EDT\n\n- Facebook\n- Twitter\n- LinkedIn\n- Email\n\nListen \u2022 1:46 LRC Public Information ##
The Kentucky House has taken the rare action to move forward with impeachment proceedings against a Fayette County judge. In matters of judicial impeachment, the Kentucky House acts like a grand jury,
able to send cases to the Senate to be heard and tried. Friday, the House voted 73-14 \u2014 largely down party lines \u2014 to do just that in the petition regarding Fayette Circuit Judge Julie Muth
Goodman. > It would create a precedent for politically motivated removal efforts. Pamela Stevenson, Democratic House Minority Leader Rep. Jason Nemes, chair of the House Impeachment Committee, argued
Goodman's behavior in the cases referenced in the complaint against her constitute willful disregard of the law. \"What is the pattern that connects these six cases across several years. It is this:
Judge Goodman sees herself as a law unto herself,\" he said. \"If she does not like a statute enacted by the General Assembly, she disregards it.\" Democratic Minority Floor Leader Pamela Stevenson
noted the impeachment marks the first against a sitting Kentucky judge in over a century , adding that the downstream effects will be felt in courtrooms across the state. \"It will undermine judicial
independence because now judges will be thinking 'will this opinion cause the legislature to review my actions?' It's a chilling effect,\" she said. \"Then it would create a precedent for politically
motivated removal efforts.\" Lawmakers debated whether the allegations against Goodman involving bias and judicial activism rise to the standard of a misdemeanor \u2014 a term some lawmakers equated
to a crime while others maintained is a broader term in the context of an impeachment. Goodman argued in her hearing that, because most of the cases being discussed remained pending, she was barred
from giving her side of the story, and that her due process rights were violated. The matter now heads to the Kentucky Senate, where a two-thirds vote is necessary to remove Goodman from the bench.
News\n\n- Facebook\n- Twitter\n- LinkedIn\n- Email\n\nJosh James\n\nSee stories by Josh James"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "In unprecedented move, Kentucky
House votes to impeach Fayette Circuit Judge Goodman | Ap | thederrick.com", "url": "https://www.thederrick.com/ap/national/in-unprecedented-move-kentucky-house-votes-to-impeach-fayette-circuit-judge-
goodman/article_d86587de-0e3d-5887-b1ae-843e4c858468.html", "snippet": "In unprecedented move, Kentucky House votes to impeach Fayette Circuit Judge Goodman | Ap | thederrick.com\n\nYou have
permission to edit this article.\n\nEdit\n\n- \n- \n- \n- \n- \n\n- \n- \n- \n- \n- \n- \n\nLEXINGTON, Ky. \u2014 The Kentucky House of Representatives on Friday voted to impeach a Fayette County
judge after a committee issued articles of impeachment against her earlier this week.\n\nIn a 73-14 vote Friday, the House approved the articles of impeachment against Fayette Circuit Judge Julie Muth
Goodman, s", "highlights": ["In unprecedented move, Kentucky House votes to impeach Fayette Circuit Judge Goodman | Ap | thederrick.com You have permission to edit this article.\n\nEdit\n\n- \n- \n-
\n- \n- \n\n- \n- \n- \n- \n- \n- LEXINGTON, Ky. \u2014 The Kentucky House of Representatives on Friday voted to impeach a Fayette County judge after a committee issued articles of impeachment against
her earlier this week. In a 73-14 vote Friday, the House approved the articles of impeachment against Fayette Circuit Judge Julie Muth Goodman, sending the matter to the Senate for a trial. The vote
was largely along party lines. Rep. Daniel Elliott of Danville was the only Republican present to vote against it; state Rep. Adam Moore of Lexington was the only Democrat present to vote in favor.
Killian Timoney, a former Republican lawmaker seeking to win back his Lexington-area House seat this year, filed the petition in January, arguing Goodman had abused her office. The seat is currently
held by Moore. On Monday, the special Impeachment Committee heard testimony from Goodman, who has served as a judge for 18 years, having been elected by Fayette County voters six times. By Wednesday,
the House committee drafted articles of impeachment that say Goodman defied binding precedents and statutes enacted by the General Assembly, and interfered with the rights and powers of judicial
bodies. \u201c(Goodman) was intentionally wrong, she lacked legal authority, yet she proceeded and did it anyway,\u201d Republican state Rep. Jason Nemes of Middletown said Friday. \u201cThis is not a
judge who made a mistake; this is something else entirely.\u201d The impeachment marks the first against a sitting judge in more than 100 years in Kentucky, and the first ever under   ...    Nemes,
the Impeachment Committee chair, laid out six cases mentioned in the petition, all of which claim Goodman abused   ...    \u201cAnd what I want every judge in this commonwealth, every judge walking
watching the proceedings on television or who   ...    You need not fear impeachment for doing your job to the best of your ability.\u201d However, in a minority report from the committee, two
lawmakers said the impeachment proceedings should not continue. Democratic state Reps. Pamela Stevenson and Al Gentry, both of Louisville, signed the report, which argued the original petition was not
complete, the proceedings violated due process and that there was no impeachable conduct alleged. Stevenson, an attorney, spoke against the impeachment Friday, as did Elliott, who said he felt
impeachment was improper. Elliott, the House Judiciary chair and attorney, was a nonvoting member of the impeachment committee.   ...    Democratic state Rep. Joshua Watkins of Louisville said the
House should not vote to impeach Goodman because it was not clear on what the actual \u201cimpeachable offenses\u201d are. \u201cIf I were to ask 10 people in this body to define the impeachable
conduct in this case, I would be a betting man to   ...    What the members could agree on, was that, whatever decision they came to, it would change Kentucky political history,   ...    Goodman and
her attorneys filed a request for an emergency injunction last week in Franklin Circuit Court saying the   ...    President Robert Stivers told reporters in January the Senate was talking with
attorneys and constitutional experts at   ...    We have a lot to think through.\u201d Stivers added the bar to remove an elected official from office isn\u2019t clearly defined because
\u201cnobody\u2019s really done it in 100 years.\u201d The last time the state Senate voted to convict and remove an impeached official was in March 2023, when the body unanimously convicted disgraced
former Eastern Kentucky prosecutor Ronnie Goldy. It was the first impeachment hearing and trial in more than a century. ---\n\n\u00a92026 Lexington Herald-Leader. Visit kentucky.com. Distributed by
Tribune Content Agency, LLC. Copyright 2026 Tribune Content Agency.\n\nLove\n\n0\n\nFunny\n\n0\n\nWow\n\n0\n\nSad\n\n0\n\nAngry\n\n0\n\n(0 Ratings)\n\n- \n- \n- \n- \n- \n- +3\n\nAp\n\nAP\n\n### Iran
threatens to attack Mideast electrical plants powering US bases\n\n- AP\n- 35 mins ago Iran has threatened to attack Mideast electrical plants powering American military bases, as President Donald
Trump\u2019s   ...    ### As Trump\u2019s deadline on Strait of Hormuz approaches, Iran threatens to attack Mideast electrical plants powering US   ...    As Trump\u2019s deadline on Strait of Hormuz
approaches, Iran threatens to attack Mideast electrical plants powering US   ...    Sports\n\nAP\n\n### AP Sports SummaryBrief at 12:40 a.m. EDT\n\n- AP\n- 50 mins ago Defending champion Florida
eliminated from March Madness by tougher, more physical Iowa team\n\n+3\n\nAp\n\nAP   ...    The top commander of the U.S. military\u2019s Central Command says the campaign against Iran is \u201cahead
or on plan,\u201d as the   ...    Tehran without identifying the sites being hit. The death toll from the war has risen to more than 1,500 people in   ...    The Supreme Court is taking up a case from
Mississippi over whether states can count late-arriving mail ballots, a   ...    forgiving deadlines for ballots from military and overseas voters also could be impacted. A ruling is expected by late
June, early enough to govern the counting of ballots in the 2026 midterm congressional elections. State and big-city   ...    offerings worth your time for the week of March 23 as selected by The"],
"published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019", "url":
"https://www.lpm.org/news/2026-03-20/house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet": "House votes to impeach Lexington judge, sponsor says with \u2018heavy
heart\u2019 \n\n\u00a9 2026 Louisville Public MediaPublic Files: 89.3 WFPL\u00b7 90.5 WUOL-FM\u00b7 91.9 WFPK For assistance accessing our public files, please contact info@lpm.org or call
502-814-6500\n\nMenu\n\n89.3 WFPL News | 90.5 WUOL Classical 91.9 WFPK Music | KyCIR Investigations\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air
Stations\n\n- On Air Now Playing LPM News - WFPL\n- On Air Now Playing LPM Music - WFPK\n- On Air No", "highlights": ["House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019
\u00a9 2026 Louisville Public MediaPublic Files: 89.3 WFPL\u00b7 90.5 WUOL-FM\u00b7 91.9 WFPK For assistance accessing our public   ...    PageDefaults>ModulePlacement |
Sites&Settings>PageDefaults>TypeSpecificOverides>Section | Homepage --> \n\nNews # House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019\n\nKentucky Public Radio | By
Sylvia Goodman Published March 20, 2026 at 1:54 PM EDT\n\n- Facebook\n- Bluesky\n- Twitter\n- LinkedIn\n- Email\n\nProvided\n\n/\n\nLRC Rep. Jason Nemes sponsored the resolution to impeach Lexington
Judge Julie Goodman. ## The Kentucky House impeached Fayette County Circuit Court Judge Julie Muth Goodman, with what one Republican calls \u201cno historic precedent.\u201d The Kentucky House voted
Friday in favor of impeaching Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now head to the Senate, where Goodman will be tried and
could be removed from office. The Kentucky House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was impeached on five articles that allege she willfully
ignored existing laws and precedent in her rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for you. We will never have these   ...    the black robe
that you have been entrusted with,\u201d said Rep. Jason Nemes, a Republican from Middletown who chaired the impeachment committee. Goodman has not been accused of criminal wrongdoing, but of breaking
the public trust in her rulings. Nemes said he decided to file articles of impeachment with a \u201cheavy, heavy heart.\u201d Nemes noted Goodman\u2019s conduct in six cases \u2014 out   ...
Goodman, sees herself as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have no evidence that the Judicial Conduct   ...    Rep.
Joshua Watkins, a Democrat from Louisville, said there are already remedies for a bad ruling, and impeachment   ...    ballot box.\u201d There are only eight days remaining in the legislative session,
but Senate President Robert Stivers said the body is allowed to return after that time solely to try indicted officials. Only one Republican voted against the impeachment resolution. Rep. Daniel
Elliot of Danville chairs the House Judiciary Committee and said he did not vote \u201cno\u201d to defend Goodman\u2019s conduct, but because he doesn\u2019t see evidence it rises to the level of
impeachment. \u201cWe've had four impeachments in our history, and most of those have been based upon a crime committed. They've also typically been unanimous in this. This morning, this, this isn't
going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in the history of the Commonwealth that supports impeaching Judge Goodman for the reasons that have been outlined by my
friend in the articles.\u201d Impeachments and convictions are incredibly rare in Kentucky. The state recently witnessed its first impeachment conviction in over a century in 2023, when lawmakers
ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal charges for soliciting nude photos from a woman in exchange for court favors. Rep. T.J. Roberts, a Republican from
Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...    \u201cIf we send a message to a judge that they can know the law, they can rule against the law simply because of
their own personal value system,\u201d Robert said. \u201cThat is not the role of a judge.\u201d Democratic Gov. Andy Beshear said he worried there could be a \u201cchilling effect\u201d on judges.
\u201cThe creation of a precedent where you would impeach a judge from disagreements with rulings when it hasn't gone   ...    On the House floor, Baird\u2019s testimony appeared to weigh heavily with
some lawmakers. GOP Rep. Patrick Flannery from   ...    And I would ask you to read those because I cannot ethically give you my side.\u201d The impeachment committee has considered five other
impeachment petitions as well \u2014 two of which they quickly dismissed without a hearing. The other"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House impeaches Fayette
judge, sending case to Senate for trial | State News | thenewsenterprise.com", "url": "https://www.thenewsenterprise.com/news/state/house-impeaches-fayette-judge-sending-case-to-senate-for-
trial/article_0df78b22-81cd-54a0-805a-aa3ee5a3da60.html", "snippet": "House impeaches Fayette judge, sending case to Senate for trial | State News | thenewsenterprise.com\n\nYou have permission to
edit this article.\n\nEdit\n\n\n\n- \n- \n- \n- \n- \n\nJulie Muth Goodman\n\n- \n- \n- \n- \n- \n- \n\nFRANKFORT \u2013 The Kentucky House of Representatives accepted the report of their impeachment
committee on Fayette Circuit Judge Julie Goodman and voted Friday to send the matter to the Senate for trial.\n\nThe charges and specifications appear in House Resolution 124, which contain five
articles", "highlights": ["House impeaches Fayette judge, sending case to Senate for trial | State News | thenewsenterprise.com You have permission to edit this article.\n\nEdit\n\n\n\n- \n- \n- \n-
\n- \n\nJulie Muth Goodman\n\n- \n- \n- \n- \n- \n- FRANKFORT \u2013 The Kentucky House of Representatives accepted the report of their impeachment committee on Fayette Circuit Judge Julie Goodman and
voted Friday to send the matter to the Senate for trial. The charges and specifications appear in House Resolution 124, which contain five articles of impeachment: kAm\u2022 sFC:?8 96C E6C>[ yF586
v@@5>2? 23FD65 E96 A@H6CD @7 E96 @77:46]k^Am kAm\u2022 v@@5>2? 567:65 3:?5:?8 AC64656?ED 6DE23=:D965 3J E96 9:896DE 4@FCED @7 z6?EF4 2? 567:65 DE2EFE6D 6?24E65 3J E96 v6?6C2= pDD6>3=J 2?5 567:65 CF=6D
@7 E96 z6?EF4 2? :?E6C76C65 H:E9 E96 C:89ED 2?5 A@H6CD @7 E96 8C2?5 ;FCJ[ EC:2= 4@FCE   ...    |2CK:2? D2:5]k^Am kAm}6>6D 925 E9:D >6DD286 7@C z6?EF4 A6249>6?E 7@C 5@:?8 J@FC ;@3 E@ E96 36DE @7 J@FC
23:=:EJ] p ;F586 H9@ HC6DE=6D 9@?6DE=J H:E9 E96 92C5 BF6DE:@?D[ 2AA=:6D E96 =2H 2D D96 F?56CDE2?5D :E 2?5 86ED C6G6CD65 92D 5@?6 ?@E9:?8 HC@?8]\u201dk^Am kAm%96 C6D@=FE:@? A2DD65 fb\\`c 2?5 9625D E@
E96 $6?2E6 7@C 2 EC:2=]k^Am\n\n- \n- \n- \n- \n- \n- \n\n#### Tags - Federal Impeachment In The United States\n- Judge\n- United States House Of Representatives\n- Jury\n- Court\n- Precedent - Public
Law\n- Justice\n- Law\n- Judiciaries\n- Government\n- Separation Of Powers\n- Government Institutions   ...    ### Current E-Edition\n\n\n\ne-Edition\n\n### The News-Enterprise\n\n- 14 hrs ago\n-
0\n\n\n\nKentucky Extra\n\n### Kentucky Extra   ...    \u00a9 Copyright 202"], "published_date": "2026-03-23T00:00:00.000", "score": null}, {"title": "Kentucky House impeaches Fayette Circuit Judge
Julie Goodman | Lexington Herald Leader", "url": "https://www.kentucky.com/news/politics-government/article315126031.html", "snippet": "Kentucky House impeaches Fayette Circuit Judge Julie Goodman |
Lexington Herald Leader \n\n \n\n \n\n \n\n \n\n \n\n## READ MORE\n\n---\n\n### Judge Julie Goodman impeachment\n\nFormer Kentucky state Rep. Killian Timoney filed a petition in January to impeach
Fayette Circuit Judge Julie Goodman over her handling of six different cases in Lexington. Goodman and her legal team deny any misconduct, and other legal professionals have raised concerns about the
possible precedent an impeachment could set.\n\n##### Expand", "highlights": ["Kentucky House impeaches Fayette Circuit Judge Julie Goodman | Lexington Herald Leader \n\n \n\n \n\n \n\n \n\n \n\n##
READ MORE   ...    Former Kentucky state Rep. Killian Timoney filed a petition in January to impeach Fayette Circuit Judge Julie Goodman   ...    The Kentucky House of Representatives on Friday voted
to impeach a Fayette County judge after a committee issued articles of impeachment against her earlier this week. In a 73-to-14 vote Friday, the House approved the articles of impeachment against
Fayette Circuit Judge Julie Muth Goodman, sending the matter to the Senate for a trial. The vote was largely along party lines. Rep. Daniel Elliott, R-Danville, was the only Republican present to vote
against it; Rep. Adam Moore, D-Lexington, was the only Democrat present to vote in favor. Killian Timoney, a former Republican lawmaker seeking to win back his Lexington-area House seat this year,
filed the petition in January, arguing Goodman had abused her office. The seat is currently held by Moore. The Kentucky House of Representatives voted 73-14 on March 20, 2026, to send articles of
impeachment for Fayette Circuit Judge Julie Goodman to the Kentucky Senate. KET On Monday, the special Impeachment Committee heard testimony from Goodman, who has served as a judge for 18 years,
having been elected by Fayette County voters six times. By Wednesday, the House committee drafted articles of impeachment that say Goodman defied binding precedents and statutes enacted by the General
Assembly, and interfered   ...    \u201c(Goodman) was intentionally wrong, she lacked legal authority, yet she proceeded and did it anyway,\u201d Rep. Jason Nemes, R-Middletown, said Friday.
\u201cThis is not a judge who made a mistake; this is something else entirely.\u201d The impeachment marks the first against a sitting judge in more than 100 years in Kentucky, and the first ever
under the state\u2019s modern court system. Robert McBride, one of Goodman\u2019s attorneys, said the vote to impeach \u201cwas expected given the composition of the House.\u201d The body is composed
of 80 Republicans and 20 Democrats. \u201cThe impeachment of Judge Goodman is a historic error and may well serve to undermine the independence of our judicial   ...    Nemes, the Impeachment
Committee chair, laid out six cases mentioned in the petition, all of which claim Goodman abused   ...    House Resolution 124, sponsored by Nemes, spells out five articles of impeachment: - Article
I: Goodman abused the powers of the office she holds. - Article II: Goodman \u201cdefied binding precedents\u201d established by higher courts. - Article III: Goodman did not follow state statutes or
rules set by the Kentucky Court of Justice. - Article IV: Goodman \u201cinterfered with the rights and powers of the grand jury, trial court jurors, attorneys, and   ...    - Article V: The conduct
described in the first four articles constitute a misdemeanor in office, warranting   ...    Goodman and her legal team have argued that several of the cases at issue in the petition are still active,
and   ...    However, in a minority report from the committee, two lawmakers said the impeachment proceedings should not continue. Rep. Pamela Stevenson, D-Louisville, and Rep. Al Gentry,
D-Louisville, signed the report, which argued the original   ...    Stevenson, an attorney, spoke against the impeachment Friday, as did Elliott, who said he felt impeachment was improper. Elliott,
the House Judiciary chair and an attorney, was a non-voting member of the impeachment committee; he   ...    Rep. Joshua Watkins, D-Louisville, said the House should not vote to impeach Goodman
because it was not clear on what   ...    \u201cIf I were to ask 10 people in this body to define the impeachable conduct in this case, I would be a betting man to   ...    What the members could
agree on, was that, whatever decision they came to, it would change Kentucky political history,   ...    Stivers added the bar to remove an elected official from office isn\u2019t clearly defined
because \u201cnobody\u2019s really done it in 100 years.\u201d It takes a two-thirds vote of present Senators to convict, according to the state constitution. The last time the state Senate voted to
convict and remove an impeached official was in March 2023, when the body unanimously convicted disgraced former Eastern Kentucky prosecutor Ronnie Goldy. It was the first Senate impeachment   ...
Goldy has since been convicted on 14 federal counts for his crimes in office and sentenced to more than three years in   ...    Editor\u2019s note: This story has been updated since publication with
additional reporting. This story was originally published March 20, 2026 at 11:30 AM.\n\n \n\n##### Related Stories from Lexington Herald Leader Kentucky\n\n### Officials, lawyers react to KY House
vote to impeach Fayette Judge Julie Goodman\n\nMarch 20, 2026 "], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House votes to impeach Lexington judge, sponsor says with
\u2018heavy heart\u2019", "url": "https://www.wkyufm.org/2026-03-20/house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet": "House votes to impeach Lexington judge, sponsor
says with \u2018heavy heart\u2019\n\n\n\n\u00a9 2026 WKU Public Radio\n\nMenu\n\n\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air Stations\n\n- On Air Now
Playing 88.9 Bowling Green | 89.5 Owensboro | 89.7 Somerset | 90.9 Elizabethtown\n- On Air Now Playing WKU Classical\n\nAll Streams\n\n# House votes to impeach Lexington judge, sponsor says with
\u2018heavy heart\u2019\n\nKentucky Public Radio | By Sylvia Goodman\n\nPublished March 20, 2026 at 12:54 PM CDT\n\n- Tw", "highlights": ["House votes to impeach Lexington judge, sponsor says with
\u2018heavy heart\u2019\n\n\n\n\u00a9 2026 WKU Public Radio\n\nMenu\n\n\n\nDonate   ...    - On Air Now Playing WKU Classical All Streams\n\n# House votes to impeach Lexington judge, sponsor says with
\u2018heavy heart\u2019 Kentucky Public Radio | By Sylvia Goodman\n\nPublished March 20, 2026 at 12:54 PM CDT\n\n- Twitter\n- LinkedIn\n- Email Provided\n\n/\n\nLRC\n\nRep. Jason Nemes sponsored the
resolution to impeach Lexington Judge Julie Goodman. ## The Kentucky House impeached Fayette County Circuit Court Judge Julie Muth Goodman, with what one Republican calls \u201cno historic
precedent.\u201d The Kentucky House voted Friday in favor of impeaching Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now head to
the Senate, where Goodman will be tried and could be removed from office. The Kentucky House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was impeached
on five articles that allege she willfully ignored existing laws and precedent in her rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for you. We
will never have these   ...    the black robe that you have been entrusted with,\u201d said Rep. Jason Nemes, a Republican from Middletown who chaired the impeachment committee. Goodman has not been
accused of criminal wrongdoing, but of breaking the public trust in her rulings. Nemes said he decided to file articles of impeachment with a \u201cheavy, heavy heart.\u201d Nemes noted Goodman\u2019s
conduct in six cases \u2014 out   ...    Goodman, sees herself as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have no evidence
that the Judicial Conduct   ...    Rep. Joshua Watkins, a Democrat from Louisville, said there are already remedies for a bad ruling, and impeachment   ...    ballot box.\u201d There are only eight
days remaining in the legislative session, but Senate President Robert Stivers said the body is allowed to return after that time solely to try indicted officials. Only one Republican voted against
the impeachment resolution. Rep. Daniel Elliot of Danville chairs the House Judiciary Committee and said he did not vote \u201cno\u201d to defend Goodman\u2019s conduct, but because he doesn\u2019t
see evidence it rises to the level of impeachment. \u201cWe've had four impeachments in our history, and most of those have been based upon a crime committed. They've also typically been unanimous in
this. This morning, this, this isn't going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in the history of the Commonwealth that supports impeaching Judge Goodman for the
reasons that have been outlined by my friend in the articles.\u201d Impeachments and convictions are incredibly rare in Kentucky. The state recently witnessed its first impeachment conviction in over
a century in 2023, when lawmakers ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal charges for soliciting nude photos from a woman in exchange for court favors. Rep.
T.J. Roberts, a Republican from Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...    \u201cIf we send a message to a judge that they can know the law, they can rule
against the law simply because of their own   ...    Democratic Gov. Andy Beshear said he worried there could be a \u201cchilling effect\u201d on judges. \u201cThe creation of a precedent where you
would impeach a judge from disagreements with rulings when it hasn't gone   ...    On the House floor, Baird\u2019s testimony appeared to weigh heavily with some lawmakers. GOP Rep. Patrick Flannery
from   ...    And I would ask you to read those because I cannot ethically give you my side.\u201d The impeachment committee has considered five other impeachment petitions as well \u2014 two of which
they quickly dismissed without a hearing. The other"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House votes to impeach Lexington judge, sponsor says with \u2018heavy
heart\u2019 - NewsBreak", "url": "https://www.newsbreak.com/weku-1588671/4550290567299-house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet": "House votes to impeach
Lexington judge, sponsor says with \u2018heavy heart\u2019 - NewsBreak\n\n57K\n\nPosts\n\n235K\n\nFollowers\n\nWEKU\n\nWebsite\n\nLexington, KY\n\nWEKU is a trusted national and regional news source
serving Lexington, Kentucky and beyond. Get the full story at WEKU.org\n\nwww.weku.org\n\nPolitics\n\n# House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019\n\nBy Sylvia
Goodman,\n\n4 days ago\n\nRep. Jason Nemes sponsored the resolution to impeach Lexington Judge Julie Goodman. ( LRC)\n\nThe Kentu", "highlights": ["House votes to impeach Lexington judge, sponsor says
with \u2018heavy heart\u2019 - NewsBreak\n\n57K\n\nPosts\n\n235K\n\nFollowers\n\nWEKU   ...    www.weku.org\n\nPolitics\n\n# House votes to impeach Lexington judge, sponsor says with \u2018heavy
heart\u2019\n\nBy Sylvia Goodman, 4 days ago\n\nRep. Jason Nemes sponsored the resolution to impeach Lexington Judge Julie Goodman. ( LRC) The Kentucky House voted Friday in favor of impeaching
Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now head to the Senate, where Goodman will be tried and could be   ...    The Kentucky
House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was impeached on five articles that allege she willfully ignored existing laws and precedent in her
rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for you. We will never have these   ...    the black robe that you have been entrusted with,\u201d
said Rep. Jason Nemes, a Republican from Middletown who chaired the   ...    Goodman has not been accused of criminal wrongdoing, but of breaking the public trust in her rulings. Nemes said he   ...
Goodman, sees herself as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have no evidence that the Judicial Conduct   ...    Rep.
Joshua Watkins, a Democrat from Louisville, said there are already remedies for a bad ruling, and impeachment   ...    confidence in a judge, there is always, in my opinion, another remedy, and the
highest remedy there is, and that is the ballot box.\u201d There are only eight days remaining in the legislative session, but Senate President Robert Stivers said the body is allowed to return after
that time solely to try indicted officials. Only one Republican voted against the impeachment resolution. Rep. Daniel Elliot of Danville chairs the House Judiciary Committee and said he did not vote
\u201cno\u201d to defend Goodman\u2019s conduct, but because he doesn\u2019t see evidence it rises to the level of impeachment. \u201cWe've had four impeachments in our history, and most of those have
been based upon a crime committed. They've also typically been unanimous in this. This morning, this, this isn't going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in the
history of the Commonwealth that supports impeaching Judge Goodman for the reasons that have been outlined by my friend in the articles.\u201d Impeachments and convictions are incredibly rare in
Kentucky. The state recently witnessed its first impeachment conviction in over a century in 2023, when lawmakers ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal
charges for soliciting nude photos from a woman in exchange for court favors. Rep. T.J. Roberts, a Republican from Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...
\u201cIf we send a message to a judge that they can know the law, they can rule against the law simply because of their own   ...    Democratic Gov. Andy Beshear said he worried there could be a
\u201cchilling effect\u201d on judges. \u201cThe creation of a precedent where you would impeach a judge from disagreements with rulings when it hasn't gone   ...    On the House floor, Baird\u2019s
testimony appeared to weigh heavily with some lawmakers. GOP Rep. Patrick Flannery from   ...    And I would ask you to read those because I cannot ethically give you my side.\u201d The impeachment
committee has considered five other impeachment petitions as well \u2014 two of which they quickly dismissed without a hearing. The other two outstanding petitions are against Supreme Court Justice
Pamela Goodwine and Fayette   ...    5\n\n## Comments / 2\n\nResponse\n\nCommunity Policy\n\n## YOU MAY ALSO LIKE\n\n#### WEKU   ...    Judge Shreds Trump\u2019s $400M Ballroom DefenseA federal judge
just torched Donald Trump\u2019s dream of a $400 million White   ...    Cuba's power grid collapses leaving it without electricity for the 3rd time this monthCuba's power grid collapsed Saturday
leaving the country without electricity for a third time in March as the"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "In unprecedented move, Kentucky House votes to
impeach Fayette Circuit Judge Goodman", "url": "https://www.yahoo.com/news/articles/unprecedented-move-kentucky-house-votes-153052229.html", "snippet": "In unprecedented move, Kentucky House votes to
impeach Fayette Circuit Judge Goodman\n\nAdvertisement\n\nAdvertisement\n\n\n\n\n\n## Top Stories:\n\n- Record-shattering heat wave\n- Play Crushable by Candy Crush\n- ICE to help TSA agents\n- Iran
war funding\n- Cesar Chavez events canceled\n- ICE at the airport?\n- Hawaii flooding\n- Plan for easing gas prices\n- Trump admin sues Harvard\n- Alabama student found dead\n\nThe Kentucky House of
Representatives on Friday voted to impeach a Fayette County judge after a comm", "highlights": ["In unprecedented move, Kentucky House votes to impeach Fayette Circuit Judge
Goodman\n\nAdvertisement\n\nAdvertisement   ...    The Kentucky House of Representatives on Friday voted to impeach a Fayette County judge after a committee issued articles of impeachment against her
earlier this week. In a 73-to-14 vote Friday, the House approved the articles of impeachment against Fayette Circuit Judge Julie Muth Goodman, sending the matter to the Senate for a trial. The vote
was largely along party lines. Rep. Daniel Elliott, R-Danville, was the only Republican present to vote against it; Rep. Adam Moore, D-Lexington, was the only Democrat present to vote in favor.   ...
Killian Timoney, a former Republican lawmaker seeking to win back his Lexington-area House seat this year, filed the petition in January, arguing Goodman had abused her office. The seat is currently
held by Moore. The Kentucky House of Representatives voted 73-14 on March 20, 2026, to send articles of impeachment for Fayette Circuit Judge Julie Goodman to the Kentucky Senate. On Monday, the
special Impeachment Committee heard testimony from Goodman, who has served as a judge for 18 years, having been elected by Fayette County voters six times. By Wednesday, the House committee drafted
articles of impeachment that say Goodman defied binding precedents and statutes enacted by the General Assembly, and interfered with the rights and powers of judicial bodies. \u201c(Goodman) was
intentionally wrong, she lacked legal authority, yet she proceeded and did it anyway,\u201d Rep. Jason Nemes, R-Middletown, said Friday. \u201cThis is not a judge who made a mistake; this is something
else entirely.\u201d The impeachment marks the first against a sitting judge in more than 100 years in Kentucky, and the first ever under   ...    Advertisement\n\nAdvertisement Robert McBride, one of
Goodman\u2019s attorneys, said the vote to impeach \u201cwas expected given the composition of the House.\u201d The body is composed of 80 Republicans and 20 Democrats. \u201cThe impeachment of Judge
Goodman is a historic error and may well serve to undermine the independence of our judicial   ...    impeachment hearing in room 131 at the Capitol Annex Building in Frankfort, Ky, on March 16, 2026.
...    Nemes, the Impeachment Committee chair, laid out six cases mentioned in the petition, all of which claim Goodman abused   ...    You need not fear impeachment for doing your job to the best of
your ability.\u201d House Resolution 124, sponsored by Nemes, spells out five articles of impeachment: Article I: Goodman abused the powers of the office she holds. Article II: Goodman \u201cdefied
binding precedents\u201d established by higher courts. Article III: Goodman did not follow state statutes or rules set by the Kentucky Court of Justice. Article IV: Goodman \u201cinterfered with the
rights and powers of the grand jury, trial court jurors, attorneys, and others   ...    Article V: The conduct described in the first four articles constitute a misdemeanor in office, warranting
impeachment   ...    Goodman and her legal team have argued that several of the cases at issue in the petition are still active, and   ...    However, in a minority report from the committee, two
lawmakers said the impeachment proceedings should not continue. Rep. Pamela Stevenson, D-Louisville, and Rep. Al Gentry, D-Louisville, signed the report, which argued the original   ...    Stevenson,
an attorney, spoke against the impeachment Friday, as did Elliott, who said he felt impeachment was improper. Elliott, the House Judiciary chair and an attorney, was a non-voting member of the
impeachment committee; he chaired the Impeachment Committee in 2023, the last time the House voted to impeach an official. \u201cWe are setting a new standard this morning, if we do this,\u201d
Elliott urged. Rep. Daniel Elliott, R-Danville, speaks against House Resolution 124, which is the articles of impeachment against   ...    Rep. Joshua Watkins, D-Louisville, said the House should not
vote to impeach Goodman because it was not clear on what   ...    \u201cIf I were to ask 10 people in this body to define the impeachable conduct in this case, I would be a betting man to   ...
What the members could agree on, was that, whatever decision they came to, it would change Kentucky political history,   ...    Stivers added the bar to remove an elected official from office
isn\u2019t clearly defined because \u201cnobody\u2019s really done it in 100 years.\u201d It takes a two-thirds vote of present Senators to convict, according to the state
constitution.\n\nAdvertisement Advertisement The last time the state Senate voted to convict and remove an impeached official was in March 2023, when the body unanimously convicted disgraced former
Eastern Kentucky prosecutor Ronnie Goldy. It was the first Senate impeachment trial in more than a century; Goldy did not appear to defend himself. Goldy has since been convicted on 14 federal
counts"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "Kentucky House passes resolution to impeach Fayette Co. judge", "url": "http://www.wkyt.com/2026/03/20/kentucky-house-
passes-resolution-impeach-fayette-co-judge/", "snippet": "Kentucky House passes resolution to impeach Fayette Co. judge\n\nFRANKFORT, Ky. (WKYT) - The Kentucky House has sent a resolution to impeach
Fayette Circuit Judge Julie Goodman to the Senate.\n\nThe resolution passed the House 73-14.\n\nThe Senate will hold a trial to decide whether to remove her from office. She could also be prohibited
from running for any office ever again.\n\nJulie Muth Goodman(WKYT)\n\n\n\nAt the meeting Thursday, lawmakers spelled out very different standards for removing an elected o", "highlights": ["Kentucky
House passes resolution to impeach Fayette Co. judge FRANKFORT, Ky. (WKYT) - The Kentucky House has sent a resolution to impeach Fayette Circuit Judge Julie Goodman to the Senate. The resolution
passed the House 73-14. The Senate will hold a trial to decide whether to remove her from office. She could also be prohibited from running for any office ever again. Julie Muth Goodman(WKYT) At the
meeting Thursday, lawmakers spelled out very different standards for removing an elected official from office. \u201cFollowing the law when you disagree with it is not weakness. It is the foundation
of the rule of law. It is what separates a system of justice from personal preference,\u201d Rep. Jason Nemes said. Rep. Pamela Stevenson disagreed. \u201cImpeachment is an extraordinary
constitutional remedy. It should be exercised with restraint and only upon clear showing of a misdemeanor, a crime, in office under section 68 of the Kentucky constitution. The standard has not been
met here. Where is the crime?\u201d Stevenson said. The original petition accuses Goodman of undermining public confidence in the judicial process, ignoring legal precedent, showing bias, and
disregarding separation of powers in multiple cases. RELATED: Mother of murder victim speaks out as judge faces impeachment Goodman has argued the impeachment petition violates her rights and is
sought injunctive relief in Franklin Circuit Court. On Tuesday, a Franklin Circuit judge denied a motion filed by Goodman that sought to pause impeachment proceedings against her. #### Most
Read\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n#### Latest News"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House votes to impeach Lexington judge, sponsor says with
\u2018heavy heart\u2019 | WEKU", "url": "https://www.weku.org/the-commonwealth/2026-03-20/house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet": "House votes to impeach
Lexington judge, sponsor says with \u2018heavy heart\u2019 | WEKU\n\n\n\n\u00a9 2026 WEKU\n\nMenu\n\n\n\nLexington's Choice for NPR\n\nSupport WEKU!\n\nPlay Live Radio\n\nNext
Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air Stations\n\n- On Air Now Playing WEKU News\n- On Air Now Playing WEKU Classical\n\nAll Streams\n\nThe 1850 campaign is replacing lost federal funds
one supporter at a time. Thanks to our listeners and supporters, we are now just 245 away from reaching this goal of 1850 new supporters donating ", "highlights": ["House votes to impeach Lexington
judge, sponsor says with \u2018heavy heart\u2019 | WEKU\n\n\n\n\u00a9 2026 WEKU\n\nMenu Lexington's Choice for NPR\n\nSupport WEKU!\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00
0:00\n\nAvailable On Air Stations   ...    the campaign! The Commonwealth\n\n# House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019 Kentucky Public Radio | By Sylvia
Goodman\n\nPublished March 20, 2026 at 1:54 PM EDT\n\n- Facebook\n- LinkedIn\n- Email Provided\n\n/\n\nLRC\n\nRep. Jason Nemes sponsored the resolution to impeach Lexington Judge Julie Goodman. ## The
Kentucky House impeached Fayette County Circuit Court Judge Julie Muth Goodman, with what one Republican calls \u201cno historic precedent.\u201d The Kentucky House voted Friday in favor of impeaching
Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now head to the Senate, where Goodman will be tried and could be removed from office.
The Kentucky House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was impeached on five articles that allege she willfully ignored existing laws and
precedent in her rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for you. We will never have these   ...    the black robe that you have been
entrusted with,\u201d said Rep. Jason Nemes, a Republican from Middletown who chaired the impeachment committee. Goodman has not been accused of criminal wrongdoing, but of breaking the public trust
in her rulings. Nemes said he decided to file articles of impeachment with a \u201cheavy, heavy heart.\u201d Nemes noted Goodman\u2019s conduct in six cases \u2014 out   ...    Goodman, sees herself
as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have no evidence that the Judicial Conduct   ...    Rep. Joshua Watkins, a
Democrat from Louisville, said there are already remedies for a bad ruling, and impeachment   ...    confidence in a judge, there is always, in my opinion, another remedy, and the highest remedy there
is, and that is the ballot box.\u201d There are only eight days remaining in the legislative session, but Senate President Robert Stivers said the body is allowed to return after that time solely to
try indicted officials. Only one Republican voted against the impeachment resolution. Rep. Daniel Elliot of Danville chairs the House Judiciary Committee and said he did not vote \u201cno\u201d to
defend Goodman\u2019s conduct, but because he doesn\u2019t see evidence it rises to the level of impeachment. \u201cWe've had four impeachments in our history, and most of those have been based upon a
crime committed. They've also typically been unanimous in this. This morning, this, this isn't going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in the history of the
Commonwealth that supports impeaching Judge Goodman for the reasons that have been outlined by my friend in the articles.\u201d Impeachments and convictions are incredibly rare in Kentucky. The state
recently witnessed its first impeachment conviction in over a century in 2023, when lawmakers ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal charges for soliciting
nude photos from a woman in exchange for court favors. Rep. T.J. Roberts, a Republican from Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...    \u201cIf we send a
message to a judge that they can know the law, they can rule against the law simply because of their own   ...    Democratic Gov. Andy Beshear said he worried there could be a \u201cchilling
effect\u201d on judges. \u201cThe creation of a precedent where you would impeach a judge from disagreements with rulings when it hasn't gone   ...    On the House floor, Baird\u2019s testimony
appeared to weigh heavily with some lawmakers. GOP Rep. Patrick Flannery from   ...    And I would ask you to read those because I cannot ethically give you my side.\u201d The impeachment committee
has considered five other impeachment petitions as well \u2014 two of which they quickly dismissed without a hearing. The other"], "published_date": "2026-03-20T00:00:00.000", "score": null}]
```

```json
{
  "query": "House impeachment federal judge 2026 vote Boasberg Boardman"
}
```

### 📋 Result

```
{"query": "House impeachment federal judge 2026 vote Boasberg Boardman", "results": [{"title": "Text - H.Res.229 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District
Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url": "https://www.congress.gov/bill/119th-congress/house-
resolution/229/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."}, {"title": "Text - H.Res.858 - 119th Congress
(2025-2026): Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url":
"https://www.congress.gov/bill/119th-congress/house-resolution/858/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."},
{"title": "Republican senators ramp up impeachment rhetoric against judges", "url": "https://www.nbcnews.com/politics/congress/republican-senators-impeachment-rhetoric-judges-judiciary-hearing-
rcna247082", "snippet": "WASHINGTON \u2014 Republican senators on Wednesday increased their scrutiny of federal judges whose rulings they've opposed, with some pushing for them [to be
impeached](https://www.nbcnews.com/politics/congress/can-congress-impeach-federal-judge-why-it-wont-happen-rcna196937).\nAttention at the Senate Judiciary Committee hearing focused on two judges:
Washington-based U.S. District Judge James Boasberg and Maryland-based Deborah Boardman, both of whom have [fallen foul of MAGA world](https://www.nbcn", "api_data": null, "hint": null}, {"title":
"Speaker Mike Johnson backs impeachment of two federal judges", "url": "https://thehill.com/homenews/house/5698953-speaker-johnson-impeachment-federal-judges/", "snippet": null, "api_data": null,
"hint": null}, {"title": "Rep. Gill Files Articles of Impeachment Against Activist Judge Boasberg | Representative Brandon Gill", "url": "https://gill.house.gov/media/press-releases/rep-gill-files-
articles-impeachment-against-activist-judge-boasberg", "snippet": "Rep. Gill Files Articles of Impeachment Against Activist Judge Boasberg\nWashington, D.C. \u2014 Congressman Brandon Gill (TX-26)
today introduced articles of impeachment against James E. Boasberg, Chief Judge, United States District Court for the District of Columbia. Chief Judge Boasberg was appointed by former President Obama
and blocked President Trump\u2019s invocation of the Alien Enemies Act. This executive action had set into motion the deportation of violent criminal illegal aliens, including gang", "api_data": null,
"hint": null}, {"title": "White House supports GOP impeachment efforts against 'rogue' federal judges | Fox News", "url": "https://www.foxnews.com/politics/scoop-white-house-backs-impeaching-rogue-
judges-accused-partisan-rulings", "snippet": "[Mike Johnson backs impeaching judges over 'egregious abuses'](https://www.foxnews.com/video/6388047458112)\nSpeaker Mike Johnson said he would support
judicial impeachments during his weekly House GOP leadership press conference.\nFIRST ON FOX: The White House fully supports efforts on Capitol Hill to impeach [federal
judges](https://www.foxnews.com/category/politics/federal-judges) who have gone \"totally rogue\" with partisan rulings, Fox News Digital learned.\nA White House official told Fox News", "api_data":
null, "hint": null}, {"title": "Judges warn against James Boasberg, Deborah Boardman impeachment push", "url": "https://www.newsnationnow.com/politics/judges-impeachment-judicial-system/", "snippet":
null, "api_data": null, "hint": null}, {"title": "Senate Judiciary clashes over judicial impeachments, rising threats against judges | Courthouse News Service", "url":
"https://www.courthousenews.com/senate-judiciary-clashes-over-judicial-impeachments-rising-threats-against-judges/", "snippet": "WASHINGTON (CN) \u2014 Lawmakers on the Senate Judiciary Committee
sparred on Wednesday over a renewed push to impeach a pair of federal judges \u2014 a move which Republicans framed as a justified response to misconduct from the federal bench, but which Democrats
said lent support to increasing threats against jurists.\nThe hearing in the Senate panel\u2019s federal courts subcommittee came hours after its chairman, Texas Senator Ted Cruz, penned a letter to
House Speaker Mike Johnson urging him to advance [im", "api_data": null, "hint": null}, {"title": "Can Judge James Boasberg Be Impeached? How Process Works as GOP Push Grows - Newsweek", "url":
"https://www.newsweek.com/can-judge-james-boasberg-impeached-how-process-works-gop-push-grows-2049018", "snippet": "U.S. District Judge James \"Jeb\" Boasberg, who last week ordered the Trump
administration to pause deportations under the Alien Enemies Act\u2014including flights carrying alleged gang members to El Salvador\u2014is now facing growing calls for impeachment from
[Republican](https://www.newsweek.com/topic/republican) lawmakers. But how does the judicial impeachment process work?\nNewsweek has reached out to some legal scholars for comment via email on
Saturday morning.\nWhy It Matters\nOn Tuesday, President [D", "api_data": null, "hint": null}, {"title": "Donalds Cosponsors Articles Of Impeachment Against Chief Judge James Boasberg | U.S.
Congressman Byron Donalds", "url": "https://donalds.house.gov/news/documentsingle.aspx?DocumentID=2352", "snippet": "WASHINGTON \u2013 This afternoon, Congressman Byron Donalds (R-FL) joined House
Republicans in cosponsoring Articles of Impeachment against D.C. District Court Chief Judge James Boasberg for high crimes and misdemeanors.\nIntroduced by Congressman Brandon Gill (R-TX), the
Articles of Impeachment allege an abuse of power by which Chief Judge Boasberg violated his oath to the Constitution and his duty of impartiality to the people of the United States by engaging in
actions that prioritized political ga", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me analyze what I've found so far. The key question is about whether the CP on the target question (federal judge impeached by Republican Representatives in a partisan vote) will be above 12% on April 10, 2026.

Key findings:
1. The CP has been stable at 9-10% for weeks, then jumped to 12% recently (as of March 29)
2. The question asks about a **federal** judge impeached by the **US House of Representatives** - this is important
3. The Kentucky impeachment is a **state** judge, not a federal judge - so it doesn't count for the underlying question
4. There are articles of impeachment filed against Judge Boasberg (H.Res.229 and H.Res.858), but no vote has occurred


5. Speaker Johnson and Senate Republicans have been pushing the impeachment effort forward with increasingly aggressive rhetoric

Now I need to determine whether the House has actually moved these articles forward through committee or scheduled a vote, since the current price is exactly at 12% and needs to move higher. Let me search for recent developments on the Boasberg impeachment proceedings specifically.

## 💬 Response

Let me check the status of the actual House impeachment proceedings for federal judges, which is what the underlying question asks about.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.congress.gov/bill/119th-congress/house-resolution/229",
  "prompt": "What is the current status of this impeachment resolution against Judge Boasberg? Has it been voted on or referred to committee?"
}
```

### 📋 Result

```
HTTP 403 for https://www.congress.gov/bill/119th-congress/house-resolution/229. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "House Judiciary Committee Boasberg impeachment hearing vote 2026"
}
```

### 📋 Result

```
{"query": "House Judiciary Committee Boasberg impeachment hearing vote 2026", "results": [{"title": "Text - H.Res.229 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District
Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url": "https://www.congress.gov/bill/119th-congress/house-
resolution/229/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."}, {"title": "Text - H.Res.858 - 119th Congress
(2025-2026): Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url":
"https://www.congress.gov/bill/119th-congress/house-resolution/858/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."},
{"title": "Whitehouse \u201cClarifies\u201d Cruz Letter About Chief Judge Boasberg to Speaker Johnson - Senator Sheldon Whitehouse", "url": "https://www.whitehouse.senate.gov/news/release/whitehouse-
clarifies-cruz-letter-about-chief-judge-boasberg-to-speaker-johnson/", "snippet": null, "api_data": null, "hint": null}, {"title": "Republican senators ramp up impeachment rhetoric against judges",
"url": "https://www.nbcnews.com/politics/congress/republican-senators-impeachment-rhetoric-judges-judiciary-hearing-rcna247082", "snippet": "WASHINGTON \u2014 Republican senators on Wednesday
increased their scrutiny of federal judges whose rulings they've opposed, with some pushing for them [to be impeached](https://www.nbcnews.com/politics/congress/can-congress-impeach-federal-judge-why-
it-wont-happen-rcna196937).\nAttention at the Senate Judiciary Committee hearing focused on two judges: Washington-based U.S. District Judge James Boasberg and Maryland-based Deborah Boardman, both of
whom have [fallen foul of MAGA world](https://www.nbcn", "api_data": null, "hint": null}, {"title": "Senator Schmitt Calls for the Impeachment, Senate Trial of Judge Boasberg During Judiciary Hearing
- Senator Schmitt", "url": "https://www.schmitt.senate.gov/media/press-releases/senator-schmitt-calls-for-the-impeachment-senate-trial-of-judge-boasberg-during-judiciary-hearing/", "snippet": null,
"api_data": null, "hint": null}, {"title": "Can Congress impeach a federal judge? Here's how and why it probably won't happen", "url": "https://www.nbcnews.com/politics/congress/can-congress-impeach-
federal-judge-why-it-wont-happen-rcna196937", "snippet": "Donald Trump's allies have been calling for the [impeachment of U.S. District Judge James Boasberg](https://www.nbcnews.com/politics/trump-
administration/trump-officials-raise-stakes-showdowns-judges-rcna196702) after he [blocked the deportation](https://www.nbcnews.com/politics/trump-administration/judge-limits-trumps-ability-deport-
people-alien-enemies-act-rcna196592) of migrants under the Alien Enemies Act. On Tuesday, the push to get rid of Boasberg became more serious when Trump himself wei", "api_data": null, "hint": null},
{"title": "Can Judge James Boasberg Be Impeached? How Process Works as GOP Push Grows - Newsweek", "url": "https://www.newsweek.com/can-judge-james-boasberg-impeached-how-process-works-gop-push-
grows-2049018", "snippet": "U.S. District Judge James \"Jeb\" Boasberg, who last week ordered the Trump administration to pause deportations under the Alien Enemies Act\u2014including flights carrying
alleged gang members to El Salvador\u2014is now facing growing calls for impeachment from [Republican](https://www.newsweek.com/topic/republican) lawmakers. But how does the judicial impeachment
process work?\nNewsweek has reached out to some legal scholars for comment via email on Saturday morning.\nWhy It Matters\nOn Tuesday, President [D", "api_data": null, "hint": null}, {"title": "House
Republicans eye hearings on Judge Boasberg, bill to rein in federal judges - ABC News", "url": "https://abcnews.go.com/Politics/house-republicans-eye-hearings-judge-boasberg-bill-
rein/story?id=120101811", "snippet": "House Republicans eye hearings on Judge Boasberg, bill to rein in federal judges\nBoasberg is at the center of the admin's legal fight over deportation
flights.\nAs President Donald Trump's battle with the judiciary escalates, House Republicans are eyeing ways to rein in judges from blocking parts of his agenda.\nHouse Judiciary Chairman Jim Jordan
said on Monday his panel will hold hearings next week on U.S. District Judge James Boasberg, who is at the center of the administration's legal fight ov", "api_data": null, "hint": null}, {"title":
"Senate Republicans urge Donald Trump, allies to stop threatening courts", "url": "https://thehill.com/homenews/senate/5220772-republican-senators-warn-impeachment-judge-boasberg/", "snippet": null,
"api_data": null, "hint": null}, {"title": "Senate Judiciary clashes over judicial impeachments, rising threats against judges | Courthouse News Service", "url":
"https://www.courthousenews.com/senate-judiciary-clashes-over-judicial-impeachments-rising-threats-against-judges/", "snippet": "WASHINGTON (CN) \u2014 Lawmakers on the Senate Judiciary Committee
sparred on Wednesday over a renewed push to impeach a pair of federal judges \u2014 a move which Republicans framed as a justified response to misconduct from the federal bench, but which Democrats
said lent support to increasing threats against jurists.\nThe hearing in the Senate panel\u2019s federal courts subcommittee came hours after its chairman, Texas Senator Ted Cruz, penned a letter to
House Speaker Mike Johnson urging him to advance [im", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://thehill.com/homenews/house/5698953-speaker-johnson-impeachment-federal-judges/",
  "prompt": "What did Speaker Johnson say about impeaching federal judges? What is the timeline and status?"
}
```

### 📋 Result

```
HTTP 403 for https://thehill.com/homenews/house/5698953-speaker-johnson-impeachment-federal-judges/. Access denied. Try search_exa for cached content, search_news for articles, or a primary data
source (fred_series, company_financials, world_bank_indicator).
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "Speaker Johnson impeach federal judge Boasberg House vote committee action March 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "Text - H.Res.229 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.",
"url": "https://www.congress.gov/bill/119th-congress/house-resolution/229/text", "snippet": "Text - H.Res.229 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District Court
Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress\nskip to main content\nNavigation**\nCongress.gov\n* Advanced Searches\n* Browse\n*
Legislation\n* Congressional Record\n* Committees\n* Members\n* Search Tools\n* Support**\n* Glossary\n* Help\n* Contact\nClose## Support\nSearch the Help Center\nGO**\n* Browse theHelp Center\n*
Glossary\n* Contact\nS", "highlights": ["H.Res.229 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District Court Chief Judge   ...    (118th-119th)Jayapal, Pramila [D-WA]
(115th-119th)Jeffries, Hakeem S. [D-NY] (113th-119th)Johnson, Dusty [R-SD] (116th-119th)Johnson, Henry C. \"Hank\" [D-GA] (110th-119th)Johnson, Julie [D-TX] (119th)Johnson, Mike [R-LA]   ...    Any
House Committees  101-119 (1989-2026)119 (2025-2026)118 (2023-2024)117 (2021-2022)116 (2019-2020)115 (2017-2018)114   ...    Home>Legislation>119th Congress> H.Res.229 # H.Res.229 - Impeaching James
E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.119th Congress (2025-2026) |Get alerts  ## Resolution Hide
Overview**\n|Sponsor:|[Rep. Gill, Brandon [R-TX-26]]|\nCommittees:|House - Judiciary| Latest Action:|House - 03/18/2025 Referred to the House Committee on the Judiciary.(All Actions)|\nTracker:Tip|
This bill has the status Introduced\nHere are the steps for Status of Legislation:\n1. Introduced\nArray\n( [actionDate] => 2025-03-18\n[displayText] => [externalActionCode] => 1000\n[description] =>
Introduced [chamberOfAction] => House\n) 2. Agreed to in House|  Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.
IN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr.Gillof Texas (for himself, Mr.Crane, Mr.Collins, Mr.Carterof Georgia, Mr.Mooreof Alabama, and Mr.Clyde) submitted the following resolution; which was
referred to the Committee on the Judiciary **RESOLUTION**  Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.
*Resolved,*That James E. Boasberg, Chief Judge, United States Court for the District of Columbia, is impeached for high crimes and misdemeanors, and that the following article of impeachment be
exhibited to the United States Senate.  Chief Judge Boasberg, in violation of his oath of office, did knowingly and willfully use his judicial position to advance political gain while interfering with
the President's constitutional prerogatives and enforcement of the rule of law. The Constitution provides that the House of Representatives \u201cshall have the sole Power of Impeachment\u201d and
that \u201ccivil Officers of the United States,\u201d including Federal Judges, are subject to impeachment and removal.  Act because \u201c[t]hese are matters of political judgement for which judges
have neither technical competence nor official responsibility.\u201d Ludecke Y. Watkins, 335 U.S. 160(1948). Yet, notwithstanding this binding precedent from the highest court in the land, Chief Judge
Boasberg has done exactly what the Supreme Court command not be done, and has illegitimately tried to   ...    people of the United States, Chief Judge Boasberg has abused the powers of his judicial
authority, having engaged in actions that prioritize political.gain over the duty of impartiality owed to the public and litigants as follows:  (1) Chief Judge Boasberg has prevented President Trump
from removing aliens associated with Tren de Aragua, a designated   ...    Wherefore"], "published_date": "2025-03-18T00:00:00.000", "score": null}, {"title": "Speaker Johnson Backs Efforts to Impeach
Judges Over Rulings", "url": "https://news.bloomberglaw.com/white-collar-and-criminal-law/speaker-johnson-backs-efforts-to-impeach-judges-over-rulings", "snippet": "Speaker Johnson Backs Efforts to
Impeach Judges Over Rulings\n\nWhite Collar & Criminal\n\nListen Print Email\n\nShare To: Facebook\n\nLinkedIn\n\nHouse Speaker Mike Johnson said he supports efforts to impeach certain federal judges
whose rulings have angered Republicans, endorsing the use of a tool rarely used against judicial officials as tensions climb between President Donald Trump and the courts.\n\nAsked about his response
to Senate Republicans\u2019 calls to bring articles of impeachment against two feder", "highlights": ["Speaker Johnson Backs Efforts to Impeach Judges Over Rulings\n\nWhite Collar & Criminal\n\nListen
Print Email   ...    House Speaker Mike Johnson said he supports efforts to impeach certain federal judges whose rulings have angered Republicans, endorsing the use of a tool rarely used against
judicial officials as tensions climb between President   ...    Asked about his response to Senate Republicans\u2019 calls to bring articles of impeachment against two federal judges in Washington and
Maryland, Johnson (R-La.) told reporters on Wednesday that he\u2019s \u201cfor it,\u201d pointing to what he described   ...    \u201cImpeachment as we have discussed all together many, many times is
an extreme measure, but extreme times call for   ...    His expression of support comes as Senate Republicans have ramped up calls to impeach Chief Judge James \u201cJeb\u201d Boasberg of the US
District Court for the District of Columbia and Judge Deborah Boardman of the District of Maryland. Republican lawmakers have taken issue with orders Boasberg signed related to former Special Counsel
Jack Smith\u2019s probe of Trump\u2019s efforts to overturn the 2020 election. Boasberg has also faced scrutiny for his handling of litigation challenging Trump\u2019s use of a wartime authority to
...    Republicans have also called to impeach Boardman over her decision to give an 8-year prison sentence to the person   ...    penalty. The Republican-controlled Senate Judiciary Committee
centered those two judges at a hearing it held earlier this month with the stated intention of \u201cholding rogue judges accountable.\u201d Sen. Ted Cruz (R-Texas), the top Republican of the
committee\u2019s federal courts panel, wrote to Johnson asking him to \u201cimmediately advance\u201d articles of impeachment against those two judges in his chambers. Fellow Texas Republican Reps.
Brandon Gill and Chip Roy introduced resolutions last year to impeach Boasberg and Boardman, respectively. Roy also attempted to add language to annual spending legislation that would have slashed
funding for Boasberg\u2019s and Boardman\u2019s chambers staff over their rulings. The proposal was shot down on the floor, with more than 40 Republicans voting against it. Johnson has previously
called to rein in judicial power through other means, such as by curbing funding for the courts and restraining judges\u2019 authority to block policies nationwide. He\u2019s stopped short in the past
of advocating directly for impeachment. Johnson faces difficult math in his chamber to usher through an impeachment resolution. He can afford to lose only two Republican votes, assuming all Democrats
vote against the measure. And the effort is all but assured to fail in the Senate, which holds impeachment trials and where a two-third vote is required to convict. Impeachments of federal judges are
rare. Fifteen judges have been impeached throughout US history. The most recent was in 2010, when Louisiana federal judge G. Thomas Porteous Jr. was removed from the bench for accepting bribes and
making   ...    Chief Justice John Roberts said in March that impeachment \u201cis not an appropriate response to disagreement concerning a   ...    House Republicans impeached President Joe
Biden\u2019s homeland security secretary, Alejandro Mayorkas, in 20"], "published_date": "2026-01-21T00:00:00.000", "score": null}, {"title": "Johnson says he would support impeaching two federal
judges, noting 'egregious abuses' | Just The News", "url": "https://www.justthenews.com/government/congress/johnson-says-he-would-support-impeaching-two-federal-judges-noting-egregious", "snippet":
"Johnson says he would support impeaching two federal judges, noting 'egregious abuses' | Just The News \n\n# Johnson says he would support impeaching two federal judges, noting 'egregious
abuses'\n\nJohnson emphasized that he was not in favor of impeaching people lightly, but admitted that some judges have committed \"egregious abuses.\"\n\n \n\nBy Misty Severi\n\nPublished: January
21, 2026 4:24pm\n\n- Article\n- Dig Deeper\n\nHouse Speaker Mike Johnson, R-La., said Wednesday that he would support articles of i", "highlights": ["Johnson says he would support impeaching two
federal judges, noting 'egregious abuses' | Just The News # Johnson says he would support impeaching two federal judges, noting 'egregious abuses' Johnson emphasized that he was not in favor of
impeaching people lightly, but admitted that some judges have committed \"egregious abuses.\" By Misty Severi\n\nPublished: January 21, 2026 4:24pm\n\n- Article\n- Dig Deeper House Speaker Mike
Johnson, R-La., said Wednesday that he would support articles of impeachment against two federal judges who have recently drawn the ire of conservative lawmakers, including U.S. District Judge James
Boasberg. Republican lawmakers have rebuked Boasberg, who has been at the center of several recent high-profile cases, and U.S. District Judge Deborah Boardman, who gave a lenient sentence to Nicholas
Roske last year, who plotted to assassinate Supreme Court Justice Brett Kavanaugh. Johnson emphasized that he was not in favor of impeaching people lightly, but admitted that some judges have
committed \"egregious abuses,\" according to The Hill. \u201cI\u2019m for it,\u201d Johnson told reporters at a press conference. \u201cJudge Boasberg is one who\u2019s been mentioned ... Impeachment,
as we have discussed altogether many times, is an extreme measure. But extreme times call for extreme measures. \"I think some of these judges have gotten so far outside the bounds of where
they\u2019re supposed to operate, it would not be, in my view, a bad thing for Congress to lay down law, so to speak, and, you know, to make an example of some of these egregious abuses,\u201d he
added. Texas GOP Rep. Brandon Gill filed articles of impeachment against Boasberg in November, accusing the judge of weaponizing the judiciary branch against people who criticized the Biden
administration, including those who criticized the Arctic Frost probe. Boasberg had ordered AT&T and Verizon not to notify lawmakers of subpoenas for their phone records as part of former special
counsel Jack Smith's Arctic Frost investigation. The nondisclosure orders were in effect for a year. Johnson declined to commit to bringing the articles of impeachment up for a floor vote. Misty
Severi is a news reporter for Just The News. You can follow her on X for more coverage.   ...    - rebuked\n- lenient sentence\n- according to The Hill\n- filed\n- ordered\n- follow her on X\n\n####
Related Articles ### Congress\n\n## AOC misused about $19k in campaign funds on ketamine-therapy for \u2018personal use,' says complaint   ...    ## Congressional Perks: Senate spending skyrockets by
more than 40% in last few years\n\nBy The Center Square Staff ### Congress\n\n## House digs in on Homeland funding standoff with Senate as Trump intervenes to pay TSA workers   ...    #### Trump turns
up the heat on DEI in federal contracting\n\n#### Courts & Law #### Henry Lee, forensic scientist who testified at O.J. Simpson trial, passes away at 87\n\n#### From the States #### Poll: Data centers
should supply own energy, says 8 in 10\n\n#### From the States   ...    #### Paid family leave receives bipartisan push in Ohio Senate"], "published_date": "2026-01-21T00:00:00.000", "score": null},
{"title": "House Speaker Johnson Supports Impeachment Of Judges - Law360", "url": "https://www.law360.com/articles/2432543/house-speaker-johnson-supports-impeachment-of-judges", "snippet": "House
Speaker Johnson Supports Impeachment Of Judges - Law360\n\nTry our Advanced Search for more refined results\n\n# Law360\n\n|\n\n## The Practice of Law\n\nAccess to Justice Aerospace & Defense
Appellate Asset Management Banking Bankruptcy Benefits California Cannabis Capital Markets Class Action Colorado Commercial Contracts Competition Compliance Connecticut Construction Consumer
Protection Corporate Criminal Practice Cybersecurity & Privacy Delaware Employment\n\nEnergy Environmental Fintech Florida ", "highlights": ["House Speaker Johnson Supports Impeachment Of Judges -
Law360\n\nTry our Advanced Search for more refined results # Law360\n\n|\n\n## The Practice of Law   ...    Energy Environmental Fintech Florida Food & Beverage Georgia Government Contracts Health
Hospitality Illinois   ...    New Jersey New York North Carolina Ohio Pennsylvania Personal Injury & Medical Malpractice Private Equity Product   ...    Telecommunications Texas Transportation Trials
Washington White Collar # Law360 Pulse\n\n|\n\n## Business of Law   ...    Florida Pulse Georgia Pulse In-House Insights Legal Tech & AI Mid-Law Modern Lawyer New Jersey Pulse New York Pulse
Pennsylvania Pulse Small Law Texas Pulse\n\n# Law360 Authority\n\n| ## Deep News & Analysis\n\n## Tax Authority\n\nFederal International State & Local\n\n## Employment Authority Discrimination Labor
Other Wage & Hour\n\n## Insurance Authority\n\nGeneral Liability Other Property Specialty Lines ## Real Estate Authority\n\nCommercial Other Residential\n\n## Bankruptcy Authority\n\nLarge Cap Mid Cap
...    - Law360 Bankruptcy Authority\n- Law360 Healthcare Authority\n- Law360 Real Estate Authority - Law360 Insurance Authority\n- Law360 Tax Authority\n- Law360 Employment Authority\n- Law360
Pulse\n- Law360 UK\n- Law360 - Law360 Podcasts\n- Law360 In-Depth\n- Lexis\u00ae\n- Products - Titans of the Plaintiffs Bar\n- Rising Stars\n- Practice Groups of the Year\n- Diversity Snapshot\n-
Law360 400 - Women in Law Report\n- Law360's MVPs\n- Regional Powerhouses\n- Leaderboard Analytics\n- Rankings - Securities\n- Product Liability\n- Intellectual Property\n- Insurance\n- Expert
Analysis\n- Energy\n- Employment - Competition\n- Class Action\n- Bankruptcy\n- Banking\n- Browse all sections\n- About all sections   ...    - Track judges\n- Track attorneys\n- Track docs\n- Beta
Tools - Help\n- Site Map\n- Resource Library\n- About Law360 Authority\n- Law360 Company\n- Sign up for our newsletters - Contact Law360\n- Read testimonials\n- Learn more about Law360\n- Search legal
jobs\n- Join the Law360 team\n- Site Menu CaseMap\u00ae CLE On-Demand Context CourtLink\u00ae Digital Library Intelligize Law360 Lex Machina Lexis Medical Navigator\u2122 Lexis\u00ae Lexis+\u2122
Lexis\u00ae Tax MLex\u00ae Nexis\u00ae Nexis Diligence\u2122 Nexis Newsdesk\u2122 Practical Guidance Product Liability Navigator Securities Mosaic\u00ae State Net\u00ae Verdict & Settlement Analyzer #
House Speaker Johnson Supports Impeachment Of Judges By Courtney Bubl\u00e9 ( January 21, 2026, 2:49 PM EST) -- House Speaker Mike Johnson, R-La., on Wednesday threw his support behind efforts to
impeach federal judges in Washington, D.C., and Maryland.... ### Law360 is on it, so you are, too. A Law360 subscription puts you at the center of fast-moving legal issues, trends and developments so
you can act with speed and confidence. Over 200 articles are published daily across more than 60 topics, industries, practice areas and jurisdictions. A Law360 subscription includes features such as -
450K+ searchable archived articles\n- Real-time alerts\n- Judge information\n- Advanced search\n- Mobile app   ...    And more!\n\nExperience Law360 today with a free 7-day trial.\n\n### Attached
Documents\n\n- Whitehouse Letter ### Related Sections\n\n- Legal Industry\n\n### Government Agencies - U.S. Supreme Court\n- U.S. District Court for the District of Maryland - U.S. District Court for
the District of Columbia\n- Federal Bureau of Investigation ### Judge Analytics\n\npowered by Lex Machina\u00ae\n\n- James E. Boasberg"], "published_date": "2026-01-21T00:00:00.000", "score": null},
{"title": "Speaker Johnson backs impeachment of 2 federal judges, claiming \u2018egregious abuses\u2019 - AOL", "url": "https://www.aol.com/articles/speaker-johnson-backs-
impeachment-2-164444542.html", "snippet": "Wed, January 21, 2026 at 4:44 PM UTC\n\n0\n\nSpeaker Mike Johnson (R-La.) said he would support impeachment articles against two federal judges, including
one who has ruled against President Trump\u2019s interests in high-profile cases.\n\nJohnson during a press conference Wednesday was asked about calls from some Republicans to bring up articles of
impeachment against Judge James Boasberg of the U.S. District Court for the District of Columbia and Judge Deborah Boardman of the U.S. District Court in Maryl", "highlights": ["21, 2026 at 4:44 PM
UTC\n\n0 Speaker Mike Johnson (R-La.) said he would support impeachment articles against two federal judges, including one who has ruled against President Trump\u2019s interests in high-profile cases.
Johnson during a press conference Wednesday was asked about calls from some Republicans to bring up articles of impeachment against Judge James Boasberg of the U.S. District Court for the District of
Columbia and Judge Deborah Boardman of the U.S. District Court in Maryland. \u201cI\u2019m for it,\u201d Johnson said. \u201cJudge Boasberg is one who\u2019s been mentioned. And these are some
egregious abuses.\u201d Johnson noted that his background is in constitutional law, and he used to sit on the House Judiciary Committee, which would process any impeachment articles.
\u201cImpeachment, as we have discussed all together many, many times, is an extreme measure. But extreme times call for extreme measures. And I think some of these judges have gotten so far outside
the bounds of where they\u2019re supposed to operate, it would not be, in my view, a bad thing for Congress to lay down law, so to speak, and, you know, to make an example of some of these egregious
abuses,\u201d Johnson said. The Speaker, however, did not commit to bringing such articles to the House floor. \u201cWe\u2019ll see where it goes,\u201d Johnson said.\n\nAdvertisement Sen. Ted Cruz
(Texas) is among the Republican lawmakers who have been calling to impeach Boasberg and Boardman, holding a hearing earlier this month that argued they had violated their duties to the Constitution in
their rulings. Cruz took issue with Boasberg issuing a nondisclosure order requiring that phone carriers keep secret for one year subpoenas that were requested by former special counsel Jack Smith in
his Arctic Frost investigation into 2020 election interference, which resulted in the Department of Justice obtaining phone records for several members of Congress. Rep. Brandon Gill (R-Texas) in
March 2025 introduced articles of impeachment against Boasberg over his court decisions blocking Trump from deporting some migrants under the Alien Enemies Act, including an order that directed the
government to turn around planes of migrants who were heading to El Salvador. The resolution impeaching Boasberg for \u201cabuse of power\u201d has 23 co-sponsors. Gill followed up with another
impeachment resolution against Boasberg over the Arctic Frost decision in November, which has 19 co-sponsors. Cruz also took issue with Boardman\u2019s sentencing decision for Sophie Roske, who was
charged under birth name Nicholas   ...    Rep. Chip Roy (R-Texas) in October introduced a resolution to impeach Boardman for \u201cwillful and systemic refusal to   ...    Privacy & Cookie
Settings\n\nAbout Us\n\nAbout our Ads\n\nAdvertising\n\nLicensing\n\nSitemap\n\n- Terms and Privacy Policy Speaker Johnson backs impeachment of 2 federal judges, claiming \u2018egregious abuses\u2019
- AOL"], "published_date": "2026-01-21T00:00:00.000", "score": null}]
```

```json
{
  "query": "House Judiciary Committee federal judge impeachment vote 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "House impeaches Fayette judge, sending case to Senate for trial | State News | thenewsenterprise.com", "url": "https://www.thenewsenterprise.com/news/state/house-impeaches-fayette-judge-
sending-case-to-senate-for-trial/article_0df78b22-81cd-54a0-805a-aa3ee5a3da60.html", "snippet": "House impeaches Fayette judge, sending case to Senate for trial | State News |
thenewsenterprise.com\n\nYou have permission to edit this article.\n\nEdit\n\n\n\n- \n- \n- \n- \n- \n\nJulie Muth Goodman\n\n- \n- \n- \n- \n- \n- \n\nFRANKFORT \u2013 The Kentucky House of
Representatives accepted the report of their impeachment committee on Fayette Circuit Judge Julie Goodman and voted Friday to send the matter to the Senate for trial.\n\nThe charges and specifications
appear in House Resolution 124, which contain five articles", "highlights": ["House impeaches Fayette judge, sending case to Senate for trial | State News | thenewsenterprise.com You have permission
to edit this article.\n\nEdit\n\n\n\n- \n- \n- \n- \n- \n\nJulie Muth Goodman\n\n- \n- \n- \n- \n- \n- FRANKFORT \u2013 The Kentucky House of Representatives accepted the report of their impeachment
committee on Fayette Circuit Judge Julie Goodman and voted Friday to send the matter to the Senate for trial. The charges and specifications appear in House Resolution 124, which contain five articles
of impeachment: kAm\u2022 sFC:?8 96C E6C>[ yF586 v@@5>2? 23FD65 E96 A@H6CD @7 E96 @77:46]k^Am kAm\u2022 v@@5>2? 567:65 3:?5:?8 AC64656?ED 6DE23=:D965 3J E96 9:896DE 4@FCED @7 z6?EF4 2? 567:65 DE2EFE6D
6?24E65 3J E96 v6?6C2= pDD6>3=J 2?5 567:65 CF=6D @7 E96 z6?EF4 2? :?E6C76C65 H:E9 E96 C:89ED 2?5 A@H6CD @7 E96 8C2?5 ;FCJ[ EC:2= 4@FCE   ...    |2CK:2? D2:5]k^Am kAm}6>6D 925 E9:D >6DD286 7@C z6?EF4
A6249>6?E 7@C 5@:?8 J@FC ;@3 E@ E96 36DE @7 J@FC 23:=:EJ] p ;F586 H9@ HC6DE=6D 9@?6DE=J H:E9 E96 92C5 BF6DE:@?D[ 2AA=:6D E96 =2H 2D D96 F?56CDE2?5D :E 2?5 86ED C6G6CD65 92D 5@?6 ?@E9:?8
HC@?8]\u201dk^Am kAm%96 C6D@=FE:@? A2DD65 fb\\`c 2?5 9625D E@ E96 $6?2E6 7@C 2 EC:2=]k^Am\n\n- \n- \n- \n- \n- \n- \n\n#### Tags - Federal Impeachment In The United States\n- Judge\n- United States
House Of Representatives\n- Jury\n- Court\n- Precedent - Public Law\n- Justice\n- Law\n- Judiciaries\n"], "published_date": "2026-03-23T00:00:00.000", "score": null}, {"title": "House votes to impeach
Lexington judge, sponsor says with \u2018heavy heart\u2019", "url": "https://www.lpm.org/news/2026-03-20/house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet": "House votes
to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019 \n\n\u00a9 2026 Louisville Public MediaPublic Files: 89.3 WFPL\u00b7 90.5 WUOL-FM\u00b7 91.9 WFPK For assistance accessing our
public files, please contact info@lpm.org or call 502-814-6500\n\nMenu\n\n89.3 WFPL News | 90.5 WUOL Classical 91.9 WFPK Music | KyCIR Investigations\n\nDonate\n\nPlay Live Radio\n\nNext
Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air Stations\n\n- On Air Now Playing LPM News - WFPL\n- On Air Now Playing LPM Music - WFPK\n- On Air No", "highlights": ["House votes to impeach
Lexington judge, sponsor says with \u2018heavy heart\u2019 \u00a9 2026 Louisville Public MediaPublic Files: 89.3 WFPL\u00b7 90.5 WUOL-FM\u00b7 91.9 WFPK For assistance accessing our public   ...
PageDefaults>ModulePlacement | Sites&Settings>PageDefaults>TypeSpecificOverides>Section | Homepage --> \n\nNews # House votes to impeach Lexington judge, sponsor says with \u2018heavy
heart\u2019\n\nKentucky Public Radio | By Sylvia Goodman Published March 20, 2026 at 1:54 PM EDT\n\n- Facebook\n- Bluesky\n- Twitter\n- LinkedIn\n- Email\n\nProvided\n\n/\n\nLRC Rep. Jason Nemes
sponsored the resolution to impeach Lexington Judge Julie Goodman. ## The Kentucky House impeached Fayette County Circuit Court Judge Julie Muth Goodman, with what one Republican calls \u201cno
historic precedent.\u201d The Kentucky House voted Friday in favor of impeaching Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now
head to the Senate, where Goodman will be tried and could be removed from office. The Kentucky House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was
impeached on five articles that allege she willfully ignored existing laws and precedent in her rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for
you. We will never have these   ...    the black robe that you have been entrusted with,\u201d said Rep. Jason Nemes, a Republican from Middletown who chaired the impeachment committee. Goodman has
not been accused of criminal wrongdoing, but of breaking the public trust in her rulings. Nemes said he decided to file articles of impeachment with a \u201cheavy, heavy heart.\u201d Nemes noted
Goodman\u2019s conduct in six cases \u2014 out   ...    Goodman, sees herself as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have
no evidence that the Judicial Conduct   ...    ballot box.\u201d There are only eight days remaining in the legislative session, but Senate President Robert Stivers said the body is allowed to return
after that time solely to try indicted officials. Only one Republican voted against the impeachment resolution. Rep. Daniel Elliot of Danville chairs the House Judiciary Committee and said he did not
vote \u201cno\u201d to defend Goodman\u2019s conduct, but because he doesn\u2019t see evidence it rises to the level of impeachment. \u201cWe've had four impeachments in our history, and most of those
have been based upon a crime committed. They've also typically been unanimous in this. This morning, this, this isn't going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in
the history of the Commonwealth that supports impeaching Judge Goodman for the reasons that have been outlined by my friend in the articles.\u201d Impeachments and convictions are incredibly rare in
Kentucky. The state recently witnessed its first impeachment conviction in over a century in 2023, when lawmakers ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal
charges for soliciting nude photos from a woman in exchange for court favors. Rep. T.J. Roberts, a Republican from Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...
\u201cIf we send a message to a judge that they can know the law, they can rule against the law simply because of their own   ...    Democratic Gov. Andy Beshear said he worried there could be a
\u201cchilling effect\u201d on judges.   ...    And I would ask you to read those because I cannot ethically give you my side.\u201d The impeachment committee has considered five other impeachment
petitions as well \u2014 two of which they quickly dismissed without a hearing. The other two outstanding petitions are against Supreme Court Justice Pamela Goodwine and Fayette County Board of
Education Chair Tyler Murphy. Both have filed responses to the petitions to defend themselves, and no   ...    Tags\n\nNews politics Kentucky\n\n- Facebook\n- Bluesky\n- Twitter\n"], "published_date":
"2026-03-20T00:00:00.000", "score": null}, {"title": "Kentucky House impeaches Fayette judge in historic vote", "url": "https://www.wuky.org/wuky-news/2026-03-20/kentucky-house-impeaches-fayette-
judge-in-historic-vote", "snippet": "Kentucky House impeaches Fayette judge in historic vote\n\n\n\n\u00a9 2026 WUKY\n\nMenu\n\n\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00
0:00\n\nAvailable On Air Stations\n\n- On Air Now Playing WUKY\n- On Air Now Playing The Break\n- On Air Now Playing WUKY Programming\n- On Air Now Playing Genre Free\n- On Air Now Playing Pop
Rocks\n- On Air Now Playing UniverseCity\n- On Air Now Playing Wildcat Country\n\nAll Streams\n\nNews\n\n# Kentucky House impeaches Fayette judge in historic vote\n\nWUKY | By Josh James\n\nPubli",
"highlights": ["Kentucky House impeaches Fayette judge in historic vote\n\n\n\n\u00a9 2026 WUKY\n\nMenu\n\n\n\nDonate\n\nPlay Live Radio\n\nNext Up:\n\n0:00 0:00\n\n0:00 0:00\n\nAvailable On Air
Stations - On Air Now Playing WUKY\n- On Air Now Playing The Break\n- On Air Now Playing WUKY Programming - On Air Now Playing Genre Free\n- On Air Now Playing Pop Rocks\n- On Air Now Playing
UniverseCity   ...    All Streams\n\nNews\n\n# Kentucky House impeaches Fayette judge in historic vote\n\nWUKY | By Josh James Published March 20, 2026 at 3:38 PM EDT\n\n- Facebook\n- Twitter\n-
LinkedIn\n- Email\n\nListen \u2022 1:46 LRC Public Information ## The Kentucky House has taken the rare action to move forward with impeachment proceedings against a Fayette County judge. In matters
of judicial impeachment, the Kentucky House acts like a grand jury, able to send cases to the Senate to be heard and tried. Friday, the House voted 73-14 \u2014 largely down party lines \u2014 to do
just that in the petition regarding Fayette Circuit Judge Julie Muth Goodman. > It would create a precedent for politically motivated removal efforts. Pamela Stevenson, Democratic House Minority
Leader Rep. Jason Nemes, chair of the House Impeachment Committee, argued Goodman's behavior in the cases referenced in the complaint against her constitute willful disregard of the law. \"What is the
pattern that connects these six cases across several years. It is this: Judge Goodman sees herself as a law unto herself,\" he said. \"If she does not like a statute enacted by the General Assembly,
she disregards it.\" Democratic Minority Floor Leader Pamela Stevenson noted the impeachment marks the first against a sitting Kentucky judge in over a century , adding that the downstream effects
will be felt in courtrooms across the state. \"It will undermine judicial independence because now judges will be thinking 'will this opinion cause the legislature to review my actions?' It's a
chilling effect,\" she said. \"Then it would create a precedent for politically motivated removal efforts.\" Lawmakers debated whether the allegations against Goodman involving bias and judicial
activism rise to the standard of a misdemeanor \u2014 a term some lawmakers equated to a crime while others maintained is a broader term in the context of an impeachment. Goodman argued in her hearing
that, because most of the cases being discussed remained pending, she was barred from giving her side of the story, and that her due process rights were violated. The matter now heads to the Kentucky
Senate, where a two-thirds vote is necessary to remove Goodman from the bench. News\n\n- Facebook\n- Twitter\n- LinkedIn\n- Email\n\nJosh James\n\nSee stories by Josh James"], "published_date":
"2026-03-20T00:00:00.000", "score": null}, {"title": "In unprecedented move, Kentucky House votes to impeach Fayette Circuit Judge Goodman | Ap | thederrick.com", "url":
"https://www.thederrick.com/ap/national/in-unprecedented-move-kentucky-house-votes-to-impeach-fayette-circuit-judge-goodman/article_d86587de-0e3d-5887-b1ae-843e4c858468.html", "snippet": "In
unprecedented move, Kentucky House votes to impeach Fayette Circuit Judge Goodman | Ap | thederrick.com\n\nYou have permission to edit this article.\n\nEdit\n\n- \n- \n- \n- \n- \n\n- \n- \n- \n- \n-
\n- \n\nLEXINGTON, Ky. \u2014 The Kentucky House of Representatives on Friday voted to impeach a Fayette County judge after a committee issued articles of impeachment against her earlier this
week.\n\nIn a 73-14 vote Friday, the House approved the articles of impeachment against Fayette Circuit Judge Julie Muth Goodman, s", "highlights": ["In unprecedented move, Kentucky House votes to
impeach Fayette Circuit Judge Goodman | Ap | thederrick.com You have permission to edit this article.\n\nEdit\n\n- \n- \n- \n- \n- \n\n- \n- \n- \n- \n- \n- LEXINGTON, Ky. \u2014 The Kentucky House of
Representatives on Friday voted to impeach a Fayette County judge after a committee issued articles of impeachment against her earlier this week. In a 73-14 vote Friday, the House approved the
articles of impeachment against Fayette Circuit Judge Julie Muth Goodman, sending the matter to the Senate for a trial. The vote was largely along party lines. Rep. Daniel Elliott of Danville was the
only Republican present to vote against it; state Rep. Adam Moore of Lexington was the only Democrat present to vote in favor. Killian Timoney, a former Republican lawmaker seeking to win back his
Lexington-area House seat this year, filed the petition in January, arguing Goodman had abused her office. The seat is currently held by Moore. On Monday, the special Impeachment Committee heard
testimony from Goodman, who has served as a judge for 18 years, having been elected by Fayette County voters six times. By Wednesday, the House committee drafted articles of impeachment that say
Goodman defied binding precedents and statutes enacted by the General Assembly, and interfered with the rights and powers of judicial bodies. \u201c(Goodman) was intentionally wrong, she lacked legal
authority, yet she proceeded and did it anyway,\u201d Republican state Rep. Jason Nemes of Middletown said Friday. \u201cThis is not a judge who made a mistake; this is something else entirely.\u201d
The impeachment marks the first against a sitting judge in more than 100 years in Kentucky, and the first ever under   ...    Nemes, the Impeachment Committee chair, laid out six cases mentioned in
the petition, all of which claim Goodman abused   ...    Nemes said he brought forth the articles of impeachment with \u201ca heavy heart.\u201d \u201cAnd what I want every judge in this commonwealth,
every judge walking watching the proceedings on television or who   ...    You need not fear impeachment for doing your job to the best of your ability.\u201d However, in a minority report from the
committee, two lawmakers said the impeachment proceedings should not continue. Democratic state Reps. Pamela Stevenson and Al Gentry, both of Louisville, signed the report, which argued the original
petition was not complete, the proceedings violated due process and that there was no impeachable conduct alleged. Stevenson, an attorney, spoke against the impeachment Friday, as did Elliott, who
said he felt impeachment was improper. Elliott, the House Judiciary chair and attorney, was a nonvoting member of the impeachment committee. \u201cWe are setting a new standard this morning, if we do
this,\u201d Elliott urged. Democratic state Rep. Joshua Watkins of Louisville said the House should not vote to impeach Goodman because it was not clear on what the actual \u201cimpeachable
offenses\u201d are. \u201cIf I were to ask 10 people in this body to define the impeachable conduct in this case, I would be a betting man to   ...    What the members could agree on, was that,
whatever decision they came to, it would change Kentucky political history,   ...    Goodman and her attorneys filed a request for an emergency injunction last week in Franklin Circuit Court saying
the   ...    President Robert Stivers told reporters in January the Senate was talking with attorneys and constitutional experts at   ...    Stivers added the bar to remove an elected official from
office isn\u2019t clearly defined because \u201cnobody\u2019s really done it in 100 years.\u201d The last time the state Senate voted to convict and remove an impeached official was in March 2023,
when the body unanimously convicted disgraced former Eastern Kentucky prosecutor Ronnie Goldy. It was the first impeachment hearing and trial in more than a century. ---\n\n\u00a92026 Lexington
Herald-Leader. Visit kentucky.com. Distributed by Tribune Content Agency, LLC.   ...    Iran has threatened to attack Mideast electrical plants powering American military bases, as President Donald
Trump\u2019s   ...    The top commander of the U.S. military\u2019s Central Command says the campaign against Iran is \u201cahead or on plan,\u201d as the   ...    The Supreme Court is taking up a
case from Mississippi over whether states can count late-arriving mail ballots, a   ...    forgiving deadlines for ballots from military and overseas voters also could be impacted. A ruling is
expected by late June, early enough to govern the counting of ballots in the 2026 midterm"], "published_date": "2026-03-20T00:00:00.000", "score": null}, {"title": "House votes to impeach Lexington
judge, sponsor says with \u2018heavy heart\u2019 | WEKU", "url": "https://www.weku.org/the-commonwealth/2026-03-20/house-votes-to-impeach-lexington-judge-sponsor-says-with-heavy-heart", "snippet":
"House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019 | WEKU\n\n\n\n\u00a9 2026 WEKU\n\nMenu\n\n\n\nLexington's Choice for NPR\n\nSupport WEKU!\n\nPlay Live Radio\n\nNext
Up:\n\n0:00\n\n0:00\n\n0:00 0:00\n\nAvailable On Air Stations\n\n- On Air Now Playing WEKU News\n- On Air Now Playing WEKU Classical\n\nAll Streams\n\nThe 1850 campaign is replacing lost federal funds
one supporter at a time. Thanks to our listeners and supporters, we are now just 245 away from reaching this goal of 1850 new supporters donating ", "highlights": ["House votes to impeach Lexington
judge, sponsor says with \u2018heavy heart\u2019 | WEKU\n\n\n\n\u00a9 2026 WEKU\n\nMenu Lexington's Choice for NPR\n\nSupport WEKU!\n\nPlay Live Radio\n\nNext Up:\n\n0:00\n\n0:00\n\n0:00
0:00\n\nAvailable On Air Stations   ...    the campaign! The Commonwealth\n\n# House votes to impeach Lexington judge, sponsor says with \u2018heavy heart\u2019 Kentucky Public Radio | By Sylvia
Goodman\n\nPublished March 20, 2026 at 1:54 PM EDT\n\n- Facebook\n- LinkedIn\n- Email Provided\n\n/\n\nLRC\n\nRep. Jason Nemes sponsored the resolution to impeach Lexington Judge Julie Goodman. ## The
Kentucky House impeached Fayette County Circuit Court Judge Julie Muth Goodman, with what one Republican calls \u201cno historic precedent.\u201d The Kentucky House voted Friday in favor of impeaching
Fayette County Circuit Court Judge Julie Muth Goodman on largely partisan lines. The articles of impeachment will now head to the Senate, where Goodman will be tried and could be removed from office.
The Kentucky House has the power to impeach all civil officers for \u201cmisdemeanors in office.\u201d Goodman was impeached on five articles that allege she willfully ignored existing laws and
precedent in her rulings. \u201cIf you're a judge and you do your job honorably and you get it wrong, we will fight for you. We will never have these   ...    the black robe that you have been
entrusted with,\u201d said Rep. Jason Nemes, a Republican from Middletown who chaired the impeachment committee. Goodman has not been accused of criminal wrongdoing, but of breaking the public trust
in her rulings. Nemes said he decided to file articles of impeachment with a \u201cheavy, heavy heart.\u201d Nemes noted Goodman\u2019s conduct in six cases \u2014 out   ...    Goodman, sees herself
as a law unto herself,\u201d Nemes said. Most Democrats voted against the measure. They pointed to the fact that they have no evidence that the Judicial Conduct   ...    ballot box.\u201d There are
only eight days remaining in the legislative session, but Senate President Robert Stivers said the body is allowed to return after that time solely to try indicted officials. Only one Republican voted
against the impeachment resolution. Rep. Daniel Elliot of Danville chairs the House Judiciary Committee and said he did not vote \u201cno\u201d to defend Goodman\u2019s conduct, but because he
doesn\u2019t see evidence it rises to the level of impeachment. \u201cWe've had four impeachments in our history, and most of those have been based upon a crime committed. They've also typically been
unanimous in this. This morning, this, this isn't going to be unanimous,\u201d Elliot said. \u201cThere's no historic precedent in the history of the Commonwealth that supports impeaching Judge
Goodman for the reasons that have been outlined by my friend in the articles.\u201d Impeachments and convictions are incredibly rare in Kentucky. The state recently witnessed its first impeachment
conviction in over a century in 2023, when lawmakers ousted former prosecutor Ronnie Goldy, who has since been sentenced on 14 federal charges for soliciting nude photos from a woman in exchange for
court favors. Rep. T.J. Roberts, a Republican from Burlington who voted in favor of the measure, said he agreed there isn\u2019t   ...    \u201cIf we send a message to a judge that they can know the
law, they can rule against the law simply because of their own   ...    Democratic Gov. Andy Beshear said he worried there could be a \u201cchilling effect\u201d on judges.   ...    And I would ask
you to read those because I cannot ethically give you my side.\u201d The impeachment committee has considered five other impeachment petitions as well \u2014 two of which they quickly dismissed
without a hearing. The other two outstanding petitions are against Supreme Court Justice Pamela Goodwine and Fayette County Board of Education Chair Tyler Murphy. Both have"], "published_date":
"2026-03-20T00:00:00.000", "score": null}]
```

## 💭 Thinking

Now I have a good picture. Let me synthesize what I know:

**About the underlying question (will a federal judge be impeached by Republican Representatives in a partisan vote before January 3, 2027):**

1. Articles of impeachment have been introduced against Judge Boasberg (H.Res.229 in March 2025, H.Res.858 in November 2025) and Judge Boardman (by Rep. Chip Roy in October 2025)
2. Speaker Johnson said in January 2026 "I'm for it" but did NOT commit to bringing articles to the floor, saying "We'll see where it goes"


3. H.Res.229 remains stuck in the House Judiciary Committee since March 2025 with no hearings or floor votes scheduled, while Johnson's narrow 2-vote margin means he can't afford significant Republican defections—and we've already seen over 40 Republicans vote against related measures
4. The actual power to impeach rests with the House, not the Senate, and state-level impeachments like Kentucky's are irrelevant to this federal question

**About the meta-question (will CP be above 12% on April 10

):**

CP has been hovering around 10% but just jumped to exactly 12% on March 29, possibly driven by the Kentucky state judge impeachment drawing broader attention to judicial impeachment and recent Senate Judiciary Committee rhetoric. With only about 10 days left until April 10 and the threshold requiring strictly above 12%, I need to assess whether this recent uptick will sustain or if it was just a temporary spike from the recent activity.

The case for it climbing higher hinges on continued Republican rhetoric and any concrete procedural moves like committee hearings or vote scheduling, though the underlying obstacles remain substantial—thin House margins, no scheduled floor vote, and the fact that most forecasters likely distinguish between talk and actual legislative action. Against that, the CP sitting exactly at the threshold means it needs to break above, and the metric was remarkably stable at 9-10% for weeks before this recent jump, suggesting the market may be skeptical this momentum holds. before the recent bump to 12%
- With 486 forecasters, large movements require many people to update
- The "noise" from Kentucky is a state, not federal, matter

This is a close call. The CP is RIGHT at the threshold. Small random fluctuations could push it either way. But:

1. The recent trend is upward (from 9-10% to 12%)
2. The underlying dynamics support moderate upward pressure - continued rhetoric and political drama around judges
3. However, the CP being exactly at 12% means it needs to go even slightly above to resolve YES
4. With a large forecaster base (486), the CP is somewhat sticky

Let me think about the probability distribution of where CP might land on April 10.

The CP has been tracking mostly flat at 9-10% for five weeks before jumping to 12% at the end of March. Over the next eleven days, I'm weighing three scenarios: the CP stays put and resolves NO, it continues drifting upward to 13%+ and resolves YES, or it reverts back toward 10-11% and resolves NO. The upward momentum suggests some chance of continued movement, but there's also real possibility of mean reversion or stabilization. Since the threshold sits exactly at the current level, this feels like roughly even odds, though the recent trend does provide some support for the upside. is strictly above 12.00%, so exactly 12.00% resolves NO. The key question is whether the CP is reported in whole percentages or with decimal precision—if it's the latter, even 12.01% counts as YES, but if it's rounded to whole numbers, it needs to reach 13%. The historical snapshots are all whole numbers, but the resolution language specifies "higher than 12.00%", suggesting they're comparing with more precision. I'm considering what could shift the CP: new forecasts being submitted or existing ones decaying in weight.

The upward forces include the ongoing political environment around judicial impeachment and potential new developments like committee action, while downward pressure comes from the lack of concrete federal action, Johnson's refusal to commit to a floor vote, and the fact that over 40 Republicans opposed a related measure. Given that the CP just hit 12% and I have only 10 days until the resolution date, the upward trend is notable but the margin is razor-thin—it's genuinely uncertain whether it breaks above the threshold.

Looking at the exact mechanics here, the CP is currently at 0.12 (12%), and the question resolves YES only if it's strictly higher than 12.00%. This means even a tiny upward movement from forecast activity would push it over. The CP jumped from the 9-10% range to 12% recently, reflecting the heated political environment, and the direction is clearly upward. However, without concrete federal action like a committee hearing or floor vote, I'm estimating around 45-55% probability that it stays above 12% through April 10—the upward momentum gives YES a slight edge, but the exact threshold positioning keeps this genuinely close.

With 10 days remaining and 486 forecasters, the CP can shift but won't swing dramatically. I'm settling on about 48% because the status quo at exactly 12% technically resolves NO, and the "strictly above" requirement means the CP needs active upward pressure to stay in YES territory, not just stability. The recent jump suggests momentum, but mean reversion is also possible without new catalysts.

I'm thinking through what could push this higher or lower. Concrete legislative action like a Judiciary Committee hearing or Johnson committing to a floor vote would drive significant movement upward, while competing priorities like the Iran situation and tariff negotiations could easily pull focus away and let the CP drift back down. The base case seems to be that without major news, the CP probably stays flat or drifts slightly.

The real tension here is that the threshold is exactly at the current level—12.00%—and it needs to be strictly above that to resolve YES. Given the upward trend over the past month, I'm leaning toward slightly better than even odds, maybe around 50-55%, since even a small push from new forecasters could tip it above the line. The meta-question itself might drive attention to the underlying forecast, creating upward pressure, and the recent jump from 10% to 12% could signal genuine shifts rather than noise. Weighing the slight upward momentum against the precision required to stay strictly above 12%, I'm settling on 50% as a genuine coin flip, with maybe a hair toward YES given the recent trend. is likely quite stable. A 2pp jump from 10% to 12% in one week is actually a significant movement. This suggests either a lot of new forecasts or a meaningful shift in the forecaster distribution.

For the CP to go from 12% to above 12%, it needs either:
- Continued new forecasts that are higher than the current median
- Or no significant downward pressure

The political environment suggests this is plausible. I'll go with 50%.

Let me just do a final sanity check on what probability I'd assign to the CP being at various levels on April 10. My initial distribution was too uniform, so let me recalibrate based on the recent jump and overall trajectory. I'm thinking the probability of staying at 12% is around 20%, with meaningful chances of both reversion below 10% and upside movement to 13% or higher, though a major development like committee action could push it above 16%. That gives me roughly a 55% chance of the CP being above 12% by April 10.

But I'm uncertain about whether this recent movement is signal or noise, so I'll be a bit more conservative and settle on 52%.

## 💬 Response

Let me check for very recent developments that could influence the CP.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "federal judge impeachment House Republicans March 2026 latest news"
}
```

### 📋 Result

```
{"query": "federal judge impeachment House Republicans March 2026 latest news", "results": [{"title": "Text - H.Res.939 - 119th Congress (2025-2026): Impeaching Donald John Trump, President of the
United States for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url": "https://www.congress.gov/bill/119th-congress/house-resolution/939/text", "snippet": null, "api_data":
null, "hint": "Use search_exa for cached content, or web_search for legislative information."}, {"title": "White House supports GOP impeachment efforts against 'rogue' federal judges | Fox News",
"url": "https://www.foxnews.com/politics/scoop-white-house-backs-impeaching-rogue-judges-accused-partisan-rulings", "snippet": "[Mike Johnson backs impeaching judges over 'egregious
abuses'](https://www.foxnews.com/video/6388047458112)\nSpeaker Mike Johnson said he would support judicial impeachments during his weekly House GOP leadership press conference.\nFIRST ON FOX: The
White House fully supports efforts on Capitol Hill to impeach [federal judges](https://www.foxnews.com/category/politics/federal-judges) who have gone \"totally rogue\" with partisan rulings, Fox News
Digital learned.\nA White House official told Fox News", "api_data": null, "hint": null}, {"title": "Senate Republicans Call to Impeach Federal Judges Over Rulings", "url":
"https://news.bloomberglaw.com/us-law-week/senate-republicans-call-to-impeach-federal-judges-over-rulings", "snippet": "Senate Judiciary Committee Republicans ramped up calls for the House to impeach
a pair of federal judges caught in President Donald Trump\u2019s crosshairs for rulings they issued seen as unfavorable to the administration.\nThe lawmakers at a hearing on Wednesday tore into Chief
Judge James \u201cJeb\u201d Boasberg of the Washington federal trial court for orders he signed related to former Special Counsel Jack Smith\u2019s probe of Trump\u2019s efforts to overturn the 2020
election.\n\u201cNo republic can survive if its judge", "api_data": null, "hint": null}, {"title": "Republican senators ramp up impeachment rhetoric against judges", "url":
"https://www.nbcnews.com/politics/congress/republican-senators-impeachment-rhetoric-judges-judiciary-hearing-rcna247082", "snippet": "WASHINGTON \u2014 Republican senators on Wednesday increased their
scrutiny of federal judges whose rulings they've opposed, with some pushing for them [to be impeached](https://www.nbcnews.com/politics/congress/can-congress-impeach-federal-judge-why-it-wont-happen-
rcna196937).\nAttention at the Senate Judiciary Committee hearing focused on two judges: Washington-based U.S. District Judge James Boasberg and Maryland-based Deborah Boardman, both of whom have
[fallen foul of MAGA world](https://www.nbcn", "api_data": null, "hint": null}, {"title": "Impeachments of Federal Judges | Federal Judicial Center", "url":
"https://www.fjc.gov/history/judges/impeachments-federal-judges", "snippet": "You are here\nImpeachments of Federal Judges\nJohn Pickering, U.S. District Court for the District of New
Hampshire.\nImpeached by the U.S. House of Representatives, March 2, 1803, on charges of mental instability and intoxication on the bench; Convicted by the U.S. Senate and removed from office, March
12, 1804.\nSamuel Chase, Associate Justice, Supreme Court of the United States.\nImpeached by the U.S. House of Representatives, March 12, 1804, on charges of arbitrary and oppressive conduct of
trial", "api_data": null, "hint": null}, {"title": "House GOP looks to rein in judicial power amid calls for impeachment", "url": "https://thehill.com/homenews/house/5211685-house-republicans-federal-
judges/", "snippet": null, "api_data": null, "hint": null}, {"title": "Bribery, corruption and intoxication: Here are some of the ways federal judges have been impeached", "url":
"https://news.northeastern.edu/2025/03/19/federal-judge-impeachment-history/", "snippet": "Bribery, corruption and intoxication: Here are some of the ways federal judges have been impeached\nCalls for
the impeachment of a federal judge have arisen in response to a decision against a Trump administration policy.\n![The Supreme Court building seen at sunset.](https://news.northeastern.edu/wp-
content/uploads/2025/03/Courts1400.jpg?w=1024)\nPresident Donald Trump and his supporters are calling for the impeachment of a federal judge who ordered a halt to the administration\u2019s effort to
deport ", "api_data": null, "hint": null}, {"title": "Judges warn against James Boasberg, Deborah Boardman impeachment push", "url": "https://www.newsnationnow.com/politics/judges-impeachment-
judicial-system/", "snippet": null, "api_data": null, "hint": null}, {"title": "Speaker Mike Johnson backs impeachment of two federal judges", "url":
"https://thehill.com/homenews/house/5698953-speaker-johnson-impeachment-federal-judges/", "snippet": null, "api_data": null, "hint": null}, {"title": "Impeachment of federal judges - Ballotpedia",
"url": "https://ballotpedia.org/Impeachment_of_federal_judges", "snippet": "[Click here to see who's on your ballot](https://ballotpedia.org/Sample_Ballot_Lookup)\nImpeachment of federal
judges\nArticle III federal judges are appointed to life terms while serving \"during good Behaviour,\" as stated in Section 1 of [Article III](https://ballotpedia.org/Article_III) of the [United
States Constitution](https://ballotpedia.org/United_States_Constitution). Though it does not expressly state in the Constitution that judges may be impeached and removed from office, they fall unde",
"api_data": null, "hint": null}]}
```

```json
{
  "query": "Boasberg Boardman impeachment status House committee April 2026"
}
```

### 📋 Result

```
{"query": "Boasberg Boardman impeachment status House committee April 2026", "results": [{"title": "Text - H.Res.858 - 119th Congress (2025-2026): Impeaching James E. Boasberg, United States District
Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url": "https://www.congress.gov/bill/119th-congress/house-
resolution/858/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."}, {"title": "Text - H.Res.229 - 119th Congress
(2025-2026): Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors. | Congress.gov | Library of Congress", "url":
"https://www.congress.gov/bill/119th-congress/house-resolution/229/text", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."},
{"title": "Donalds Cosponsors Articles Of Impeachment Against Chief Judge James Boasberg | U.S. Congressman Byron Donalds", "url": "https://donalds.house.gov/news/documentsingle.aspx?DocumentID=2352",
"snippet": "WASHINGTON \u2013 This afternoon, Congressman Byron Donalds (R-FL) joined House Republicans in cosponsoring Articles of Impeachment against D.C. District Court Chief Judge James Boasberg
for high crimes and misdemeanors.\nIntroduced by Congressman Brandon Gill (R-TX), the Articles of Impeachment allege an abuse of power by which Chief Judge Boasberg violated his oath to the
Constitution and his duty of impartiality to the people of the United States by engaging in actions that prioritized political ga", "api_data": null, "hint": null}, {"title": "Rep. Gill Files Articles
of Impeachment Against Activist Judge Boasberg | Representative Brandon Gill", "url": "https://gill.house.gov/media/press-releases/rep-gill-files-articles-impeachment-against-activist-judge-boasberg",
"snippet": "Rep. Gill Files Articles of Impeachment Against Activist Judge Boasberg\nWashington, D.C. \u2014 Congressman Brandon Gill (TX-26) today introduced articles of impeachment against James E.
Boasberg, Chief Judge, United States District Court for the District of Columbia. Chief Judge Boasberg was appointed by former President Obama and blocked President Trump\u2019s invocation of the
Alien Enemies Act. This executive action had set into motion the deportation of violent criminal illegal aliens, including gang", "api_data": null, "hint": null}, {"title": "Judges warn against James
Boasberg, Deborah Boardman impeachment push", "url": "https://www.newsnationnow.com/politics/judges-impeachment-judicial-system/", "snippet": null, "api_data": null, "hint": null}, {"title": "Rep.
Gill Files Impeachment Articles Against Judge Boasberg Following Arctic Frost Scandal | Representative Brandon Gill", "url": "https://gill.house.gov/media/press-releases/rep-gill-files-impeachment-
articles-against-judge-boasberg-following-arctic", "snippet": "Rep. Gill Files Impeachment Articles Against Judge Boasberg Following Arctic Frost Scandal\nWashington, D.C. \u2014 Congressman Brandon
Gill (TX-26) today introduced articles of impeachment against James E. Boasberg, Chief Judge, United States District Court for the District of Columbia, for his abuse of judicial authority used to
target conservative Members of Congress, organizations, and patriotic Americans.\n\u201cChief Judge Boasberg has compromised the impartiality of the judiciary and created a consti", "api_data": null,
"hint": null}, {"title": "Senate Judiciary clashes over judicial impeachments, rising threats against judges | Courthouse News Service", "url": "https://www.courthousenews.com/senate-judiciary-
clashes-over-judicial-impeachments-rising-threats-against-judges/", "snippet": "WASHINGTON (CN) \u2014 Lawmakers on the Senate Judiciary Committee sparred on Wednesday over a renewed push to impeach a
pair of federal judges \u2014 a move which Republicans framed as a justified response to misconduct from the federal bench, but which Democrats said lent support to increasing threats against
jurists.\nThe hearing in the Senate panel\u2019s federal courts subcommittee came hours after its chairman, Texas Senator Ted Cruz, penned a letter to House Speaker Mike Johnson urging him to advance
[im", "api_data": null, "hint": null}, {"title": "Republican senators ramp up impeachment rhetoric against judges", "url": "https://www.nbcnews.com/politics/congress/republican-senators-impeachment-
rhetoric-judges-judiciary-hearing-rcna247082", "snippet": "WASHINGTON \u2014 Republican senators on Wednesday increased their scrutiny of federal judges whose rulings they've opposed, with some
pushing for them [to be impeached](https://www.nbcnews.com/politics/congress/can-congress-impeach-federal-judge-why-it-wont-happen-rcna196937).\nAttention at the Senate Judiciary Committee hearing
focused on two judges: Washington-based U.S. District Judge James Boasberg and Maryland-based Deborah Boardman, both of whom have [fallen foul of MAGA world](https://www.nbcn", "api_data": null,
"hint": null}, {"title": "Cosponsors - H.Res.270 - 119th Congress (2025-2026): Removing James E. Boasberg, Chief Judge of the United States District Court for the District of Columbia, for failure to
remain in good behavior pursuant to section 1 of article III of the Constitution. | Congress.gov | Library of Congress", "url": "https://www.congress.gov/bill/119th-congress/house-
resolution/270/cosponsors", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content, or web_search for legislative information."}, {"title": "Sen. Cruz Chairs Hearing on Judicial
Overreach, Urges Impeachment of Judges Boasberg and Boardman | U.S. Senator Ted Cruz of Texas", "url": "https://www.cruz.senate.gov/newsroom/press-releases/sen-cruz-chairs-hearing-on-judicial-
overreach-urges-impeachment-of-judges-boasberg-and-boardman", "snippet": null, "api_data": null, "hint": null}]}
```

## 💭 Thinking

I don't see any very recent news (last few days in March 2026) about concrete action on the federal judge impeachment. The most recent developments seem to be:
- January 21, 2026: Speaker Johnson says he's "for it" but doesn't commit to floor vote
- The Senate Judiciary hearing (sometime in mid-January 2026)
- The articles remain in committee

There are no signs of imminent committee action or floor vote. The House is focused on other priorities (budget, spending, Iran military action, tariffs, etc.).

Now let me also factor in that we're currently on March 31, 2026, and the question resolves April 10 - that's 10 days. The current CP is at exactly 12%.
 
Now I'm analyzing whether the probability will move strictly above 12% by April 10. The upward trend from 9% to 12% over the past five weeks suggests some momentum, but with no scheduled hearings or floor vote commitments and the House preoccupied with other legislative priorities, there's limited catalyst for movement in the next ten days. The 2-point jump from 10% to 12% in a week is substantial and likely reflects genuine shifts in forecaster sentiment rather than noise, given the recent political developments. However, without concrete action materializing, there's limited room for further growth, so I'm settling on 50% as my final estimate.

Now I'm looking at the weekly movement pattern to model expected changes over the next 10 days. The recent data shows volatility—ranging from -1pp to +2pp weekly—with an average change of about 0.6pp per week, though the sample is small and may not be predictive.

Based on this random walk model with slight upward drift, I'd expect CP to reach around 12.9% by April 10th, with a standard deviation of about 1.4 percentage points. That puts the probability of staying above 12% at a certain level, which I'm calculating now.

But I'm realizing this approach has some real limitations—the drift estimate comes from just five data points, and there's no guarantee the recent momentum continues given how volatile political dynamics can be. The jump to 12% itself might have been a one-time shift rather than the start of a sustained trend.

I should probably be more conservative here and assume a smaller drift rate, maybe 0.3 percentage points per week instead of 0.6, to account for these uncertainties.

With that adjustment, I'm getting a probability around 63%, and if I assume no drift at all, it drops to 50%. My best estimate lands somewhere in the 55-60% range, balancing the likelihood that some upward momentum continues against the real possibility that the trend could stall or reverse.

I should also account for measurement precision—if the current value is right at 12.00%, natural fluctuations alone would give roughly even odds of crossing above that threshold, but the upward drift tips the scales toward 55%.

## 💬 Response

Now I have enough data to analyze this question. Let me model the CP dynamics quantitatively.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Historical CP data points (weekly)\ndates = ['Feb 22', 'Mar 1', 'Mar 8', 'Mar 15', 'Mar 22', 'Mar 29']\ncp_values = [9, 10, 10, 9, 10, 12]\n\n# Weekly changes\nchanges = [cp_values[i+1] - cp_values[i] for i in range(len(cp_values)-1)]\nprint(f\"Weekly CP changes: {changes}\")\nprint(f\"Mean weekly change: {np.mean(changes):.2f}pp\")\nprint(f\"SD of weekly changes: {np.std(changes, ddof=1):.2f}pp\")\n\n# Model CP as random walk with drift\nmean_change = np.mean(changes)\nsd_change = np.std(changes, ddof=1)\n\n# Time to resolution: ~10 days \u2248 1.5 weeks\nweeks_ahead = 10/7\n\n# Monte Carlo simulation\nnp.random.seed(42)\nn_sims = 100000\ncurrent_cp = 12.0\n\n# Simulate with full estimated drift\nfinal_cps = current_cp + np.random.normal(mean_change * weeks_ahead, sd_change * np.sqrt(weeks_ahead), n_sims)\n\n# Bound CP at reasonable values (1% to 50%)\nfinal_cps = np.clip(final_cps, 1, 50)\n\np_above_12 = np.mean(final_cps > 12.0)\nprint(f\"\\n--- Full drift model ---\")\nprint(f\"Expected CP: {np.mean(final_cps):.2f}%\")\nprint(f\"P(CP > 12.00%): {p_above_12:.3f}\")\nprint(f\"Median CP: {np.median(final_cps):.2f}%\")\nprint(f\"10th-90th percentile: {np.percentile(final_cps, 10):.1f}% - {np.percentile(final_cps, 90):.1f}%\")\n\n# More conservative: halve the drift\nconservative_cps = current_cp + np.random.normal(mean_change * weeks_ahead * 0.5, sd_change * np.sqrt(weeks_ahead), n_sims)\nconservative_cps = np.clip(conservative_cps, 1, 50)\np_conservative = np.mean(conservative_cps > 12.0)\nprint(f\"\\n--- Conservative drift (half) ---\")\nprint(f\"Expected CP: {np.mean(conservative_cps):.2f}%\")\nprint(f\"P(CP > 12.00%): {p_conservative:.3f}\")\n\n# Zero drift model\nzero_drift_cps = current_cp + np.random.normal(0, sd_change * np.sqrt(weeks_ahead), n_sims)\nzero_drift_cps = np.clip(zero_drift_cps, 1, 50)\np_zero = np.mean(zero_drift_cps > 12.0)\nprint(f\"\\n--- Zero drift model ---\")\nprint(f\"P(CP > 12.00%): {p_zero:.3f}\")\n\n# Sensitivity: what if current CP is actually slightly above 12% (e.g., 12.1%)?\nfor starting_cp in [11.9, 12.0, 12.1, 12.5]:\n    sims = starting_cp + np.random.normal(mean_change * weeks_ahead * 0.5, sd_change * np.sqrt(weeks_ahead), n_sims)\n    sims = np.clip(sims, 1, 50)\n    p = np.mean(sims > 12.0)\n    print(f\"\\nStarting CP={starting_cp}%, half drift -> P(>12%): {p:.3f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Weekly CP changes: [1, 0, -1, 1, 2]\nMean weekly change: 0.60pp\nSD of weekly changes: 1.14pp\n\n--- Full drift model ---\nExpected CP: 12.86%\nP(CP > 12.00%):
0.736\nMedian CP: 12.86%\n10th-90th percentile: 11.1% - 14.6%\n\n--- Conservative drift (half) ---\nExpected CP: 12.43%\nP(CP > 12.00%): 0.626\n\n--- Zero drift model ---\nP(CP > 12.00%):
0.499\n\nStarting CP=11.9%, half drift -> P(>12%): 0.595\n\nStarting CP=12.0%, half drift -> P(>12%): 0.621\n\nStarting CP=12.1%, half drift -> P(>12%): 0.650\n\nStarting CP=12.5%, half drift ->
P(>12%): 0.753\n", "stderr": "", "duration_ms": 238}
```

## 💭 Thinking

Now let me synthesize all the evidence and prepare my reflection.

Key findings:
1. The CP has been trending upward: 9→10→10→9→10→12 over 5 weeks
2. Mean weekly change: +0.6pp, SD: 1.14pp
3. Monte Carlo results:
   - Full drift: P(>12%) = 73.6%
   - Half drift: P(>12%) = 62.6%
   - Zero drift: P(>12%) = 49.9%

4. The underlying question is about federal judge impeachment by Republican Representatives
5. Articles of impeachment have been filed (H.Res.229 and H.Res.858 for Boasberg, plus one for Boardman) but remain in committee


6. Speaker Johnson expressed support for impeachment in January 2026 but hasn't committed to a floor vote, and there are no scheduled committee hearings or votes despite over 40 Republicans opposing a related spending amendment
7. The political environment keeps the issue in circulation, though the Kentucky state judge impeachment may have influenced some forecasters' perceptions

The critical question now is whether the recent upward momentum will persist through April 10, or if the lack of concrete legislative action will cause the probability to stabilize or decline.

I'm weighing the case for continued drift—ongoing political rhetoric and Speaker Johnson's backing could prompt committee action—against the case against it: no actual legislative movement, competing House priorities, and significant Republican opposition. My intuition is that the drift is real but probably overstated, so I'm settling on a 55-60% probability of YES. Running through a weighted scenario where zero drift yields 50%, half drift yields 63%, and full drift yields 74%, I'm allocating 30% weight to zero drift, 50% to half drift, and 20% to full drift to arrive at my final estimate.

But I'm second-guessing myself on the recent jump. The +2 percentage point spike stands out against the earlier pattern of {+1, 0, -1, +1}, and with only five data points, it's hard to tell if this is a genuine signal from political developments or just noise from a few influential forecasters updating. I'm leaning toward 55% as my final answer, though I should account for the possibility that the crowd's precision is higher than it appears.

## 💬 Response

Now let me do the reflection with my analysis.
