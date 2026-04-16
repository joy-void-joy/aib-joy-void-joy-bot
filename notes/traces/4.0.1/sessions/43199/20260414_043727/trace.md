# Reasoning Log: Will the community prediction be higher than 7.50% on 2026-04-21 for the Metaculus question "Will Lisa Cook cease to be a member of the Federal Reserve Board of Governors before November 3, 2026?"?

*Generated: 2026-04-14T04:44:40.968298+00:00*


## 💭 Thinking

Let me analyze this meta-prediction question carefully.

**Question**: Will the community prediction (CP) for "Will Lisa Cook cease to be a member of the Federal Reserve Board of Governors before November 3, 2026?" be higher than 7.50% on 2026-04-21?

**Key details**:
- Current CP as of 2026-04-13: 7.50% (exactly at the threshold)
- Threshold: higher than 7.50%
- Resolution date: 2026-04-21 20:53:47
- Historical CP:
  - 2026-03-09: 10.00%
  - 2026-03-16: 14.00%
  - 2026-03-23: 11.00%
  - 2026-03-30: 10.00%
  - 2026-04-06: 10.00%
  - 2026-04-13: 7.50%

The prediction has been declining steadily from 14% down to the current 7.50%, so I need to assess whether it's likely to tick above that threshold in the next week or stay below it.

## 💬 Response

I'll analyze this meta-prediction question step by step. Let me gather the necessary information.

## 🔧 Tool: mcp__markets__get_metaculus_questions


## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__markets__get_cp_history


```json
{
  "post_id_list": [
    39711
  ]
}
```

### 📋 Result

```
{"post_id": 39711, "title": "Will Lisa Cook cease to be a member of the Federal Reserve Board of Governors before November 3, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/39711", "background_info": "[Lisa DeNell Cook](https://en.wikipedia.org/wiki/Lisa_Cook) is an American economist and a member of the Federal Reserve Board of
Governors. She was first appointed to a partial term in May 2022 and later confirmed in September 2023 to a full 14-year term ending January 31, 2038.\n\nIn August 2025, [Trump attempted to remove
Cook](https://apnews.com/article/federal-reserve-cook-trump-e9933d518af5155250bebbdc29fd3f2b) from her position alleging that she commited mortgage fraud before she became a member of the Fededral
Reserve Board. Under the Federal Reserve Act, Governors serve staggered 14-year terms and may be removed by the President [only \"for
cause\"](https://www.federalreserve.gov/aboutthefed/section10.htm). Such a removal [has never happened](apnews.com/article/federal-reserve-cook-trump-e9933d518af5155250bebbdc29fd3f2b) in the Federal
Reserve's history.\n\nAccording to the [Associated Press](https://apnews.com/article/federal-reserve-cook-trump-e9933d518af5155250bebbdc29fd3f2b):\n\n> Trump has repeatedly criticized the Fed \u2014
and its chair, Jerome Powell \u2014 for refusing to cut interest rates. The central bank has left its benchmark rate unchanged this year, partly because it is waiting to see whether the big taxes
\u2014 tariffs \u2014 that Trump is slapping on foreign products will push inflation higher. Cook has voted against a cut, along with most board members.\n\nLisa Cook filed a lawsuit to challenge her
firing and the August court hearing [concluded without a ruling](https://www.reuters.com/legal/government/hearing-ends-without-ruling-trumps-firing-fed-governor-cook-2025-08-29/), meaning that Cook
would stay in place for now.", "resolution_criteria": "This question will resolve as **Yes** if Lisa Cook ceases to be as a member of the Federal Reserve Board of Governors at any time before November
3, 2026 EST, according to [credible sources](https://www.metaculus.com/faq/#definitions).", "fine_print": "In case of ambiguity, the [Federal Reserve page of board
members](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm) will be used to resolve this question.", "num_forecasters": 143, "community_prediction": null}
```

```json
{
  "query": "Lisa Cook Federal Reserve Board removal firing 2026",
  "hours_back": 168,
  "n_articles": 10
}
```

### 📋 Result

```
Error calling tool 'search_news': APIError: 403015 - You've reached your maximum billable overage limit for 'requests'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

```json
{
  "post_id": 39711,
  "days": 60
}
```

### 📋 Result

```
Failed to fetch CP history: Client error '403 Forbidden' for url 'https://www.metaculus.com/api/aggregation_explorer/?post_id=39711&aggregation_methods=recency_weighted'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
```

## 💬 Response

The CP history is blocked (AIB tournament question) and news search hit a limit. Let me search for the latest news on Lisa Cook through other channels.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "query": "Lisa Cook Federal Reserve Board governor removal 2026 latest"
}
```

### 📋 Result

```
{"query": "Lisa Cook Federal Reserve Board governor removal 2026 latest", "results": [{"title": "SCOTUS allows Lisa Cook to stay on Fed board into 2026, accepts case for January argument - ABC News",
"url": "https://abcnews.com/Politics/scotus-allows-lisa-cook-stay-fed-2026-accepts/story?id=126118156", "snippet": "SCOTUS allows Lisa Cook to stay on Fed board into 2026, accepts case for January
argument\nThe Supreme Court moved to allow Lisa Cook to remain on the central bank board.\nThe Supreme Court on Wednesday moved to allow Federal Reserve governor Lisa Cook to remain on the central
bank board into 2026, saying it would take up President Donald Trump's appeal seeking to remove her for cause during a hearing in January.\nThe Court did not explain its decision. There were no noted
dissents.\nThe decision to", "api_data": null, "hint": null}, {"title": "Lisa Cook - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lisa_Cook", "snippet": "Lisa DeNell Cook (born 1964) is an
American economist who was sworn in as a member of the Federal Reserve Board of Governors in 2022. She is the first black woman to sit on the board. Before her appointment to the Federal Reserve
Board, she was elected in January 2022 to the board of directors of the Federal Reserve Bank of Chicago. She was also a research associate at the National Bureau of Economic Research.\nCook was
previously a professor of economics and international relations at Michigan S", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Lisa Cook\", \"url\":
\"https://en.wikipedia.org/wiki/Lisa_Cook\", \"extract\": \"Lisa DeNell Cook (born 1964) is an American economist who was sworn in as a member of the Federal Reserve Board of Governors in 2022. She is
the first black woman to sit on the board. Before her appointment to the Federal Reserve Board, she was elected in January 2022 to the board of directors of the Federal Reserve Bank of Chicago. She
was also a research associate at the National Bureau of Economic Research.\\nCook was previously a professor of economics and international relations at Michigan State University and a member of the
American Economic Association's Executive Committee. An authority on international economics, especially the Russian economy, she has been involved in advising policymakers from the Obama
Administration to the Nigerian and Rwandan governments. Her research is at the intersection of macroeconomics and economic history, with recent work in African-American history and innovation
economics. Cook is regarded as one of the few prominent black female economists and has attracted attention within academia for her efforts in mentoring black women and advocating for their inclusion
in the field of economics.\\nOn January 14, 2022, Joe Biden nominated Cook to serve as Federal Reserve governor; she was confirmed by the U.S. Senate on May 10 after a 50\\u201350 vote was broken by a
tie breaker vote by Kamala Harris, and took office on May 23, 2022.\\nOn August 15, 2025, Federal Housing Finance Agency director Bill Pulte accused Cook of committing mortgage fraud, and sent a
referral letter to Attorney General Pam Bondi regarding the matter, encouraging that an investigation be launched by the Department of Justice. In September 2025, U.S. Pardon Attorney Ed Martin
started a Department of Justice criminal investigation of Cook over allegations of mortgage fraud. However, on September 12, Reuters published an analysis of \\\"loan [and] job-vetting forms\\\"
submitted by Cook, as well as property records, which directly contradict the Trump administration's allegations against her.\\nOn August 25, 2025, President Donald Trump announced that he was
removing Cook from the Federal Reserve Board of Governors, citing alleged \\\"deceitful and potentially criminal conduct\\\". Federal law allows governors to be removed only \\\"for cause\\\", a
provision intended to protect the central bank\\u2019s independence. Cook disputed the allegations and filed suit in federal court, arguing that her dismissal was unlawful and politically motivated.
As litigation proceeds, she remains legally considered an active governor, pending a judicial ruling on whether the president had authority to remove her.\\n\\n\", \"mode\": \"full\"}"}]}, "hint":
null}, {"title": "It\u2019s showdown time for the Fed's independence at the Supreme Court : NPR", "url": "https://www.npr.org/2026/01/21/nx-s1-5674893/supreme-court-federal-reserve-lisa-cook",
"snippet": "It's showdown time for the Fed's independence at the Supreme Court\nSCOTUS to hear case on president's power to fire Federal Reserve Governor Lisa Cook\n![Fed Chair Jerome Powell speaks
with Lisa Cook, a member of the Board of Governors of the Federal Reserve, during a meeting in Washington on June
25.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/6575x4383+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2Ffe%2F8c%2F89f82ed24e2f9701a493e0279", "api_data": null, "hint": null}, {"title": "Firing Federal Reserve Governor Lisa Cook", "url":
"https://www.epi.org/policywatch/firing-federal-reserve-governor-lisa-cook/", "snippet": null, "api_data": null, "hint": null}, {"title": "Supreme Court to weigh Trump's bid to oust Federal Reserve
governor Lisa Cook", "url": "https://spectrumlocalnews.com/me/maine/politics/2026/01/20/lisa-cook-oral-arguments-preview", "snippet": "The Supreme Court is scheduled to hear oral arguments Wednesday
about President Donald Trump\u2019s efforts to fire Federal Reserve governor Lisa Cook. The country\u2019s top court agreed last year to take the case several weeks after Trump moved to fire Cook
\u2014 [the first time a president has sought to oust a sitting Fed governor in the body\u2019s 112-year history](https://apnews.com/article/supreme-court-trump-federal-reserve-lisa-
cook-5a48941a9e30017b0ed3e5837492d288).\nCook sued over her removal, and the ca", "api_data": null, "hint": null}, {"title": "Trump v. Cook: an explainer - SCOTUSblog", "url":
"https://www.scotusblog.com/2026/01/trump-v-cook-an-explainer/", "snippet": "Trump v. Cook: an explainer\n![Amy Howe Amy Howe's Headshot](https://www.scotusblog.com/wp-content/uploads/2020/09/amy-
howe-thumbnail.jpg?w=100&h=100)\n[Amy Howe](https://www.scotusblog.com/author/amy-howe/)\n![Chairman of the US Federal Reserve Jerome Powell speaks with Lisa Cook, member of the Board of Governors of
the Federal Reserve, as he chairs a Federal Reserve Board open meeting discussing proposed revisions to the board's supplementary leverage ratio standards at the Federal Reserve Board ", "api_data":
null, "hint": null}, {"title": "Supreme Court doubtful of Trump claim he can fire Fed governors by fiat : NPR", "url": "https://www.npr.org/2026/01/21/nx-s1-5683968/supreme-court-federal-reserve-lisa-
cook", "snippet": "Supreme Court doubtful of Trump claim he can fire Fed governors by fiat\nSupreme Court appears wary of allowing Trump to fire Federal Reserve\u2019s Cook\n![An exterior photo of the
Supreme Court.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5566x3711+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2Fee%2F63%2F49ef03a04d73882b9075c1bca7fe%2Fgettyimages-2157829281-25.jpg)\nThe Supreme Court Andrew Harnik/Getty Images hide caption\nThe Supreme Court", "api_data": null,
"hint": null}, {"title": "Fed Governor Lisa Cook seems safe from Trump firing after Supreme Court arguments", "url": "https://www.cnbc.com/2026/01/21/supreme-court-trump-fed-lisa-cook-powell.html",
"snippet": "![Supreme Court considers Trump\u2019s effort to fire Fed\u2019s Lisa
Cook](https://image.cnbcfm.com/api/v1/image/108255128-1769017474518-gettyimages-2256857707-COOK_SUPREME_COURT.jpeg?v=1769017504&w=750&h=422&vtcrop=y)\n[Federal Reserve](https://www.cnbc.com/federal-
reserve/) Governor [Lisa Cook](https://www.cnbc.com/2025/08/28/trump-fed-lisa-cook-lawsuit-powell.html)'s job seemed safe from firing by President [Donald Trump](https://www.cnbc.com/donald-trump/)
after [Supreme Court](https://www.cnbc.com/su", "api_data": null, "hint": null}, {"title": "Supreme Court to weigh Trump's bid to oust Fed governor Lisa Cook", "url":
"https://spectrumlocalnews.com/us/snplus/politics/2026/01/20/lisa-cook-oral-arguments-preview", "snippet": "The Supreme Court is scheduled to hear oral arguments Wednesday about President Donald
Trump\u2019s efforts to fire Federal Reserve governor Lisa Cook. The country\u2019s top court agreed last year to take the case several weeks after Trump moved to fire Cook \u2014 [the first time a
president has sought to oust a sitting Fed governor in the body\u2019s 112-year history](https://apnews.com/article/supreme-court-trump-federal-reserve-lisa-
cook-5a48941a9e30017b0ed3e5837492d288).\nCook sued over her removal, and the ca", "api_data": null, "hint": null}, {"title": "Trump\u2019s Firing of a Fed Governor | Washington Monthly", "url":
"https://washingtonmonthly.com/2026/02/03/trumps-firing-of-a-fed-governor/", "snippet": "If you listened to the January 21 [oral
argument](https://www.supremecourt.gov/oral_arguments/argument_transcripts/2025/25a312_c0nd.pdf) in [Trump v. Cook](https://www.nytimes.com/2026/01/21/us/politics/lisa-cook-mortgage-fraud-
accusation.html?searchResultPosition=1), you may have wondered, as I did, \u201cWhere did our stuck-in-the-18th-century-don\u2019t-talk-to-us-about-the-real-world\u201d Supreme Court go to? Except for
Justice Clarence Thomas\u2019s initial question, \u201cOn what basis are we to conclude that the", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Lisa Cook Federal Reserve firing lawsuit Supreme Court 2026"
}
```

### 📋 Result

```
[{"title": "Supreme Court seems likely to let Lisa Cook keep job on Fed Board after Trump's firing - CBS News", "url": "https://www.cbsnews.com/news/supreme-court-lisa-cook-fed-trump-oral-arguments/",
"snippet": "Supreme Court seems likely to let Lisa Cook keep job on Fed Board after Trump's firing - CBS News \n\nWatch CBS News\n\n \n\nWashington \u2014 The Supreme Court on Wednesday appeared
likely to allow Lisa Cook to keep her position on the Federal Reserve Board of Governors and reject President Trump's attempt to fire her for now.\n\nThe high court heard arguments in a high-stakes
case over Mr. Trump's effort to oust Cook, which he attempted last August over allegations she engaged in mortgage fraud. Lower cour", "highlights": ["Supreme Court seems likely to let Lisa Cook keep
job on Fed Board after Trump's firing - CBS News \n\nWatch CBS News Washington \u2014 The Supreme Court on Wednesday appeared likely to allow Lisa Cook to keep her position on the Federal Reserve
Board of Governors and reject President Trump's attempt to fire her for now. The high court heard arguments in a high-stakes case over Mr. Trump's effort to oust Cook, which he attempted last August
over allegations she engaged in mortgage fraud. Lower courts had allowed Cook to remain in her post while she   ...    The Federal Reserve Act of 1913 gives the president the authority to remove a
member of the Fed's Board of Governors   ...    The Fed has an \"unbroken history going back to its founding in 1913 in which no president, from Woodrow Wilson to   ...    Justice Sonia Sotomayor
called the circumstances surrounding Cook's firing-by-social-media \"irregular,\" adding that \"it certainly didn't invite an opportunity to be heard.\" ## Cook's case Lisa Cook during a Fed event in
Washington, D.C., on Friday, March 22, 2024. Al Drago / Bloomberg via Getty Images Cook sued over her removal last year, arguing that the president violated the Federal Reserve Act. She also said she
was entitled to and deprived of notice and the opportunity to a hearing before she was fired. U.S. District Judge Jia Cobb sided with Cook and reinstated her to her post, finding that Mr. Trump had
not validly removed her \"for cause.\" The judge also ruled that Cook was likely to succeed on her argument that she was deprived of her due-process rights because she did not receive the necessary
process before her firing. A divided panel of three appeals court judges continued to block Cook's removal, and the Trump administration sought emergency relief from Supreme Court and asked the
justices to allow the president to oust her. The high court has allowed Cook to remain in her position while it considers whether Mr. Trump can fire her and is hearing the case on an expedited
schedule. Cook has participated in the last two meetings of the Fed's interest-rate-setting committee. Its next meeting is set for later this month. The dispute involving Cook's firing poses a test
for the independence of the Fed, which defenders of the bank argue would be jeopardized if the Supreme Court rules for Mr. Trump. Arguments also come days after Fed Chairman Jerome   ...
investigation into him. The Supreme Court has allowed Mr. Trump to fire members of other independent agencies and appears poised to overturn a 90-year-old decision that allowed Congress to impose
removal protections for officials at multi-member boards and commissions. But it has also signaled that it views the Fed differently from those other entities. In May, the Supreme Court singled out
the Fed as a \"a uniquely structured, quasi-private entity that follows in the   ...    Unlike the case involving removal restrictions for independent agencies, the Justice Department is not
challenging the constitutionality of the Fed's for-cause protection. Instead, the key issues are whether Mr. Trump needed to give Cook notice and a hearing before removing her, if the president had
cause to fire her \u2014 and what constitutes \"cause\" \u2014 and   ...    Sauer argued in Supreme Court filings that the president lawfully ousted Cook after \"concluding that the American   ...
gross negligence in a financial matter,\" the solicitor general said. Cook's lawyers called the allegations against her \"flimsy\" and \"unproven\" and argued in papers that the Fed's   ...    not
constitute \"cause\" for removal under the law. Cook joined the Fed Board in May 2022, and the allegations involve   ...    Constitution's Fifth Amendment, they said. Her lawyers warned that accepting
Mr. Trump's argument that removals from   ...    #### Supreme Court hears case over mail ballots that arrive after Election Day   ...    #### Will the Supreme Court Save the Fed from Trump?\n\n####"],
"published_date": "2026-01-21T14:14:00.000", "score": null}, {"title": "Supreme Court doubtful of Trump claim he can fire Fed governors by ...", "url":
"https://www.npr.org/2026/01/21/nx-s1-5683968/supreme-court-federal-reserve-lisa-cook", "snippet": "Supreme Court doubtful of Trump claim he can fire Fed governors by fiat : NPR \n\nAccessibility
links\n\nSupreme Court doubtful of Trump claim he can fire Fed governors by fiat The Trump administration wants the authority to fire Lisa Cook, a Federal Reserve governor. Experts say that would
undermine the independence of the central bank.\n\n### Law\n\n# Supreme Court doubtful of Trump claim he can fire Fed governors by fiat\n\n \n\n6:48 PM ET\n\nHeard on All Things Considered\n\n \n\n
\n\n \n\n \n\n \n\n \n\n#### Supreme C", "highlights": ["Supreme Court doubtful of Trump claim he can fire Fed governors by fiat : NPR \n\nAccessibility links Supreme Court doubtful of Trump claim he
can fire Fed governors by fiat The Trump administration wants the authority to fire Lisa Cook, a Federal Reserve governor. Experts say that would undermine the independence of the central bank. ###
Law\n\n# Supreme Court doubtful of Trump claim he can fire Fed governors by fiat\n\n \n\n6:48 PM ET Heard on All Things Considered #### Supreme Court appears wary of allowing Trump to fire Federal
Reserve\u2019s Cook\n\nListen \u00b7 5:30 5:30   ...    The Supreme Court Wednesday seemed likely to block President Trump's attempt to immediately remove Lisa Cook from the Federal Reserve's
governing board. In a spirited argument that lasted more than two hours, all nine justices\u2014liberal and conservative--expressed doubts about the president's claim of absolute power to fire members
of the Fed board. Trump announced on Truth Social last August that he was firing Cook from the Fed Board of Governors. In subsequent comments, he accused her of mortgage fraud prior to her appointment
in 2022. Cook, an economist, and the first Black woman appointed to the board, has vehemently denied the charge through her lawyers, and the Supreme Court, which has allowed Trump to remove other
agency heads, balked at the administration's emergency request to allow Trump to fire Cook. On Wednesday's day of reckoning, things did not go well for the president. Solicitor General D. John Sauer
opened with a strong condemnation of Cook. \"Deceit or gross negligence by a financial regulator in financial transactions is cause for removal,\" he said.   ...    Several justices observed that this
is the first time since the Fed was established by Congress 112 years ago that any president has interfered with the statutory independence of the Fed by firing one of its members. \"What is the
evidence that has been presented and considered with respect to Ms. Cook's alleged misconduct?\" Justice Ketanji Brown Jackson asked. General Sauer replied that the firing was justified in a letter to
Cook, but he maintained that the president's decision on the matter is not subject to review, even by the Supreme Court, and that Cook was not entitled to notice or a hearing before being removed.
Given that, Justice Neil Gorsuch wanted to know what would be required. \"Just a meeting across a conference table   ...    Justice Samuel Alito wondered whether the case should be sent back to the
lower courts for fact-finding about the mortgage allegations. But Justice Brett Kavanaugh was far more doubtful about the Trump administration's position. \"Your position that there's no judicial
review, no process required, no remedy available, a very low bar for cause that the president alone determines,\" he said. \"I mean, that would weaken, if not shatter, the independence of the Federal
...    Kavanaugh talked as well about what he called \"the real-world downstream effects\" if Trump were to prevail. \"Just thinking big picture, what goes around comes around. All the current
president's appointees would likely be removed for cause on Jan. 20, 2029, if there's a Democratic president, or Jan. 20, 2033,\" he posited. \"So what are we doing here? If we accept all these no
procedure, no judicial review, no remedy?\" What's more, said Kavanaugh, a ruling for the president's me-only position would incentivize presidents to come up with trivial misdeeds or old and
inconsequential allegations that are very difficult to disprove, in order to get rid of Federal Reserve board governors who are supposed to be independent and won't do the president's bidding. Making
the counter argument for Cook in court was Paul Clement, who served as solicitor general for President George W. Bush. He argued that the president alone cannot determine what is a legitimate cause to
fire a member of the Fed. \"If there's no judicial review, its all kind of a joke,\" Clement told the Court.   ...    So, asked Alito, \"What is the minimum that the executive, in your view, has to
provide?\"   ...    As Clement would put it later: \"This is a situation where Congress, political animals one and all, knew better than   ...    and they tied the president's hand.\" Sitting in the
Supreme Court chamber and listening to the arguments was Federal Reserve Board Chairman Jerome Powell, who very likely would be Trump's next target for removal should the president prevail. Even
though Trump himself   ...    more quickly. A decision in the case is expected by summer.\n\n \n\n"], "published_date": "2026-01-21T17:12:28.000", "score": null}, {"title": "Supreme Court weighs
Trump's firing of the Fed's Lisa Cook by social media | Reuters", "url": "https://www.reuters.com/legal/government/supreme-court-weighs-trumps-firing-feds-lisa-cook-by-social-media-2026-01-20/",
"snippet": "Supreme Court weighs Trump's firing of the Fed's Lisa Cook by social media | Reuters\n\nSkip to main content\n\nExclusive news, data and analytics for financial market professionalsLearn
more aboutRefinitiv\n\nFederal Reserve Board Governor Lisa Cook speaks on \"The Outlook for the Economy and Monetary Policy\" at the Brookings Institution in Washington, D.C., U.S., November 3, 2025.
REUTERS/Kevin... Purchase Licensing Rights, opens new tab Read more\n\n- Summary\n\n- Cook says constitutional due process ri", "highlights": ["Supreme Court weighs Trump's firing of the Fed's Lisa
Cook by social media | Reuters\n\nSkip to main content   ...    - Summary - Cook says constitutional due process rights violated\n- President posted termination letter on social media - Trump sought
to fire Fed's Cook in August WASHINGTON, Jan 20 (Reuters) - In the battle over President Donald Trump's effort to fire Federal Reserve Governor Lisa Cook that is set to go before the U.S. Supreme
Court on Wednesday, the justices may focus on the president's use of social media to carry out this unprecedented action. The justices are due to hear arguments over Trump's request to lift a lower
court judge's decision barring \u200bhim from firing Cook while her legal challenge to the removal continues. The justices in October agreed to hear the dispute, a decision, opens new tab that left
Cook in her role for the time being.   ...    Here too, just after 8 p.m. last August 25, Trump posted to his Truth Social account a letter addressed to Cook informing her that \"you are hereby
removed\" from the role of Fed governor. No president since the central bank's founding in 1913 has ousted a Fed governor. That action, Cook and her lawyers argue, violated her rights under the U.S.
Constitution's Fifth Amendment, which provides that no person may be \"deprived of life, liberty or property without due process of law.\" The case, which could imperil the independence of the world's
most important central bank, prominently tests whether Trump had adequate \"cause\" under federal law to remove Cook. But it also is a \u200cfight over whether the way Trump sought to oust Cook was
fair. Lower courts agreed with Cook that Trump's action likely was not.   ...    The president has based his bid to \u200bfire Cook on allegations by Federal Housing Finance Agency Director Bill
Pulte, a   ...    though the law does not define the term or establish procedures for removal. Cook's case raises thorny questions concerning the scope of presidential power, the \u2060validity of
Trump's decisions that impact the central bank, and the authority of the judiciary to second-guess the president. But the case also offers the court, which has a 6-3 conservative majority and has
backed Trump in numerous decisions since he returned to \u200dthe presidency last year, a way of deciding the case on procedural grounds that could leave some of those contentious, substantive
questions to another day. Cook's lawyers have said that Trump's letter on social media purporting to fire her without either notice in advance or   ...    Trump's Justice Department urged the Supreme
Court to reject Cook's argument, contending that a government officer's   ...    \"Cook had an opportunity to explain why no misconduct occurred, and she spurned it,\" the filing \u200dstated. Cook
sued Trump in August after the president announced he would remove her. U.S. District Judge Jia Cobb in September temporarily blocked Trump from carrying out his directive, ruling that he likely
violated Cook's due process rights and that the mortgage allegations likely were not a legally sufficient cause to remove her under the Federal Reserve Act as they relate to conduct that occurred
before she was confirmed to the post by the Senate. The Washington-based judge called it \"doubtful that Cook should have been required to piece together the evidentiary basis for a 'for cause'
removal from a scattered assortment of social media \u200bposts and news articles.\" The U.S. Court of Appeals for the District of Columbia Circuit refused Trump's bid to put Cobb's order on hold,
prompting \u200dthe administration to seek the Supreme Court's"], "published_date": "2026-01-20T14:17:53.000", "score": null}, {"title": "US Supreme Court appears reluctant to let Trump fire Fed's
Lisa Cook", "url": "https://www.reuters.com/legal/government/us-supreme-court-considers-trumps-bid-fire-feds-lisa-cook-2026-01-21/", "snippet": "US Supreme Court appears reluctant to let Trump fire
Fed's Lisa Cook | Reuters\n\nSkip to main content\n\nExclusive news, data and analytics for financial market professionalsLearn more aboutRefinitiv\n\n- Summary\n\n- Central bank independence at stake
in case\n- Lower courts blocked Cook's removal\n- Trump sought to fire Fed Governor Cook in August\n\nWASHINGTON, Jan 21 (Reuters) - U.S. Supreme Court justices signaled skepticism on Wednesday toward
President Donald Trump's unprecedented bid to fire Federa", "highlights": ["US Supreme Court appears reluctant to let Trump fire Fed's Lisa Cook | Reuters\n\nSkip to main content Exclusive news, data
and analytics for financial market professionalsLearn more aboutRefinitiv\n\n- Summary - Central bank independence at stake in case\n- Lower courts blocked Cook's removal - Trump sought to fire Fed
Governor Cook in August WASHINGTON, Jan 21 (Reuters) - U.S. Supreme Court justices signaled skepticism on Wednesday toward President Donald Trump's unprecedented bid to fire Federal Reserve Governor
Lisa Cook in a case with the central bank's independence at stake. During about two hours of arguments, the justices indicated they are unlikely to grant the Trump administration's request to lift a
judge's order barring \u200bthe Republican president from immediately firing Cook while her legal challenge continues to play out.   ...    Since the Fed was created in \u200b1913, no president has
tried to oust an official from the central bank. Questions posed   ...    The justices expressed unease about the ramifications for the Fed's cherished independence from political influence if   ...
Some pressed U.S. Solicitor General D. John Sauer, arguing for the administration, about why Cook was not given a   ...    inconsequential or old allegations that are very difficult to disprove,\"
Kavanaugh \u200cadded. U.S. District Judge Jia Cobb in September ruled that Trump's attempt to remove Cook without notice or a hearing likely violated her right to due process under the U.S.
Constitution's Fifth Amendment. Cobb also found that the mortgage fraud allegations \u200blikely were not a sufficient cause to remove a Fed governor under the law, noting that the alleged conduct
occurred before Cook held the Fed post. An appeals court declined Trump's request to put Cobb's order on hold. When the Supreme Court, which has a 6-3 conservative majority, agreed in October, opens
new tab to hear the case, it left Cook in her job for the time being. This marks the latest case to reach the top U.S. judicial body involving Trump's expansive view of presidential powers   ...
\"This case is about whether the Federal Reserve will set key interest rates guided by evidence and independent judgment   ...    Cook has called the allegations against her a pretext to remove her
over monetary policy differences as Trump heaps   ...    Item 1 of 4 Federal Reserve Governor Lisa Cook looks on outside the U.S. Supreme Court, as Supreme Court justices consider U.S. President
Donald Trump's effort to fire her, in Washington, D.C., U.S., January 21, 2026. REUTERS/Nathan   ...    Roberts \u200dalso expressed doubts about Sauer's arguments that the president's assertion of a
cause is not reviewable by the courts, or that judges cannot reinstate a fired officer. In creating the Fed, Congress passed a law that included provisions meant to insulate the central bank from
political interference, requiring governors to be removed by a president only \"for cause,\" though the \u200claw does not define \u200cthe   ...    Paul Clement, the lawyer arguing for Cook, said
that the Fed's unique status means that its officers must have greater   ...    \"There's no rational reason to go through all the trouble of creating this unique quasi-private entity that is exempt
...    restriction that is as toothless as the president imagines,\" Clement said. As a Fed governor, Cook helps set U.S. monetary policy with the rest of the central bank's seven-member board and the
heads of the 12 regional Fed banks. Her term in the job runs to 2038. Cook was appointed in 2022 by Democratic former President Joe Biden as the first Black woman to serve in the post. A Supreme Court
ruling is expected by the end of June but could come sooner. It was unclear how narrow or broad a ruling favoring Cook might be or how \u2060the case would proceed if the justices return it to the
lower courts, \u2060leaving open the possibility of the matter returning to the Supreme Court \u200bon appeal.   ...    The president sought to fire Cook on August 25 by posting a termination letter
on social media citing the mortgage   ...    The justices questioned Sauer on his contention that Cook was not entitled to formal notice and a hearing before   ...    admiration for Hitler or for the
Klan?\" Alito asked. The Supreme Court has backed Trump in a series \u200dof"], "published_date": "2026-01-21T11:02:05.000", "score": null}, {"title": "Trump v. Cook | Supreme Court Bulletin | US Law
| LII / Legal Information Institute", "url": "https://supct.law.cornell.edu/supct/cert/25A312", "snippet": "Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information Institute\n\n#
Trump v. Cook\n\n- ADMINISTRATIVE AGENCY\n- due process\n- removal\n- EXECUTIVE POWER\n- equitable relief\n\n## Issues\n\nWhether the president\u2019s removal of a member of the Federal Reserve
comported with the relevant procedural requirements and whether the removal was for sufficient cause.\n\nOral argument:\n\nJanuary 21, 2026\n\nCourt below:\n\nUnited States Court of Appeals for the
D.C. Circuit\n\nThis case considers whether th", "highlights": ["Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information Institute\n\n# Trump v. Cook - ADMINISTRATIVE AGENCY\n- due
process\n- removal\n- EXECUTIVE POWER\n- equitable relief\n\n## Issues Whether the president\u2019s removal of a member of the Federal Reserve comported with the relevant procedural requirements and
whether the removal was for sufficient cause. Oral argument:\n\nJanuary 21, 2026\n\nCourt below:\n\nUnited States Court of Appeals for the D.C. Circuit This case considers whether the removal of Lisa
Cook, a member of the Federal Reserve Board of Governors, by President Donald J. Trump, comported with constitutional and statutory requirements. The Court must address a temporary restraining order
leaving Cook in her position after President Trump sought the first-ever (attempted) presidential removal of a Federal Reserve Board of Governors member, citing an alleged incident of prior fraud by
Cook. The parties disagree about what, if any, cause is required for a president to remove a Board member. Trump argues that he has broad   ...    presidential removal power narrowly, and argues for
robust procedural protections against removal. This dispute could reshape the relationship between the president and the Federal Reserve, potentially limiting or ending the Federal   ...    ##
Questions as Framed for the Court by the Parties Whether the Supreme Court should stay a district court ruling preventing the president from firing a member of the Federal Reserve Board of Governors.
## Facts Congress established the Federal Reserve (\u201cthe Fed\u201d) by the Federal Reserve Act of 1913. The Fed is responsible for   ...    Lisa Cook, respondent, serves on the Board of Governors;
her term of service expires in 2038. On August 25, 2025, President Donald Trump purported to \u201c remove\u201d Cook from her position on the Board of Governors \u201cfor cause.\u201d As cause,   ...
Cook sought a temporary restraining order against President Trump in the United States District Court for the District   ...    The district court treated Cook\u2019s request for a temporary
restraining order as motion for a preliminary injunction. On September 9, 2025, the district court enjoined President Trump from removing Cook, ruling that Cook met the four   ...    for the District
of Columbia Circuit. On September 15, 2025, the Court of Appeals denied the stay request, leaving the District Court\u2019s injunction in effect. The Court of Appeals held that the district court
properly granted the   ...    Appeals agreed that President Trump \u201cvery likely\u201d violated Cook\u2019s due process rights to notice and hearing, but it declined to address whether President
Trump had valid cause to remove Cook. President Trump further sought a stay of the district court\u2019s injunction at the United States Supreme Court. On October 1, 2025, the Supreme Court deferred a
ruling on the stay application pending oral arguments.   ...    President Trump claims that the Due Process Clause does not entitle Cook to a hearing prior to her removal because her   ...    is
confirmed, President Trump asserts, by numerous previous Supreme Court cases holding that public officials serving   ...    President Trump also argues that even if Cook\u2019s removal was in error, a
stay is nonetheless warranted because the   ...    ### THE EQUITIES President Trump asserts that the issues in this case are important enough to eventually grant certiorari\u201cgiven the significance
of the removal power to the President\u2019s ability to supervise the Executive Branch and the importance of the Federal Reserve Board as a federal agency.\u201d President Trump contends that the
government also faces a risk of   ...    argues, outweighs any harm Cook may suffer because she can be made whole through back-pay were she to win the lawsuit. Cook argues that the Supreme Court is
unlikely to eventually grant certiorari because the accelerated litigation has led to an under-developed factual record, making accurate judgement impossible. Cook claims that President Trump will
...    exercising executive powers. On the other hand, Cook asserts that issuing a stay would cause irreparable harm by   ...    ## Discussion\n\n### IMPLICATIONS FOR FEDERAL RESERVE INDEPENDENCE AND
POLICYMAKING In support of President Trump, the New Civil Liberties Alliance(\u201cNCLA\u201d) argues that the Fed\u2019s independence from   ...    Governors, there is no danger that the public will
mistakenly blame (or credit) the president for the nation\u2019s monetary policy. ## Conclusion\n\n### Authors\n\nWritten by: Garrett Taylor and Daniel Lempert\n\nEdited by: Sierra Berry ## Additional
Resources - Jason Albright, Federal Reserve Governor Lisa Cook, removed by Trump, reinstated pending ongoing litigation, VitalLaw (Sept. 10, 2025). - John Fritze, Supreme Court agrees to hear
arguments in case on Federal Reserve independence, leaving Lisa Cook in job   ...    - Ian Millhiser, The Supreme"], "published_date": null, "score": null}, {"title": "Trump v. Cook | Supreme Court
Bulletin | US Law | LII / Legal Information Institute", "url": "http://www.law.cornell.edu/supct/cert/25A312", "snippet": "Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information
Institute\n\n# Trump v. Cook\n\n- equitable relief\n- EXECUTIVE POWER\n- removal\n- due process\n- ADMINISTRATIVE AGENCY\n\n## Issues\n\nWhether the president\u2019s removal of a member of the Federal
Reserve comported with the relevant procedural requirements and whether the removal was for sufficient cause.\n\nOral argument:\n\nJanuary 21, 2026\n\nCourt below:\n\nUnited States Court of Appeals
for the D.C. Circuit\n\nThis case considers whether th", "highlights": ["Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information Institute\n\n# Trump v. Cook - equitable relief\n-
EXECUTIVE POWER\n- removal\n- due process\n- ADMINISTRATIVE AGENCY\n\n## Issues Whether the president\u2019s removal of a member of the Federal Reserve comported with the relevant procedural
requirements and whether the removal was for sufficient cause. Oral argument:\n\nJanuary 21, 2026\n\nCourt below:\n\nUnited States Court of Appeals for the D.C. Circuit This case considers whether the
removal of Lisa Cook, a member of the Federal Reserve Board of Governors, by President Donald J. Trump, comported with constitutional and statutory requirements. The Court must address a temporary
restraining order leaving Cook in her position after President Trump sought the first-ever (attempted) presidential removal of a Federal Reserve Board of Governors member, citing an alleged incident
of prior fraud by Cook. The parties disagree about what, if any, cause is required for a president to remove a Board member. Trump argues that he has broad   ...    presidential removal power
narrowly, and argues for robust procedural protections against removal. This dispute could reshape the relationship between the president and the Federal Reserve, potentially limiting or ending the
Federal   ...    ## Questions as Framed for the Court by the Parties Whether the Supreme Court should stay a district court ruling preventing the president from firing a member of the Federal Reserve
Board of Governors. ## Facts Congress established the Federal Reserve (\u201cthe Fed\u201d) by the Federal Reserve Act of 1913. The Fed is responsible for   ...    Lisa Cook, respondent, serves on the
Board of Governors; her term of service expires in 2038. On August 25, 2025, President Donald Trump purported to \u201c remove\u201d Cook from her position on the Board of Governors \u201cfor
cause.\u201d As cause,   ...    Cook sought a temporary restraining order against President Trump in the United States District Court for the District   ...    The district court treated Cook\u2019s
request for a temporary restraining order as motion for a preliminary injunction. On September 9, 2025, the district court enjoined President Trump from removing Cook, ruling that Cook met the four
...    for the District of Columbia Circuit. On September 15, 2025, the Court of Appeals denied the stay request, leaving the District Court\u2019s injunction in effect. The Court of Appeals held that
the district court properly granted the   ...    Appeals agreed that President Trump \u201cvery likely\u201d violated Cook\u2019s due process rights to notice and hearing, but it declined to address
whether President Trump had valid cause to remove Cook. President Trump further sought a stay of the district court\u2019s injunction at the United States Supreme Court. On October 1, 2025, the
Supreme Court deferred a ruling on the stay application pending oral arguments.   ...    President Trump claims that the Due Process Clause does not entitle Cook to a hearing prior to her removal
because her   ...    is confirmed, President Trump asserts, by numerous previous Supreme Court cases holding that public officials serving   ...    President Trump also argues that even if Cook\u2019s
removal was in error, a stay is nonetheless warranted because the   ...    ### THE EQUITIES President Trump asserts that the issues in this case are important enough to eventually grant
certiorari\u201cgiven the significance of the removal power to the President\u2019s ability to supervise the Executive Branch and the importance of the Federal Reserve Board as a federal agency.\u201d
President Trump contends that the government also faces a risk of   ...    argues, outweighs any harm Cook may suffer because she can be made whole through back-pay were she to win the lawsuit. Cook
argues that the Supreme Court is unlikely to eventually grant certiorari because the accelerated litigation has led to an under-developed factual record, making accurate judgement impossible. Cook
claims that President Trump will   ...    exercising executive powers. On the other hand, Cook asserts that issuing a stay would cause irreparable harm by threatening the Fed\u2019s independence,
leading to unstable economic conditions and market disruptions. ## Discussion\n\n### IMPLICATIONS FOR FEDERAL RESERVE INDEPENDENCE AND POLICYMAKING In support of President Trump, the New Civil
Liberties Alliance(\u201cNCLA\u201d) argues that the Fed\u2019s independence from   ...    policy. ## Conclusion\n\n### Authors\n\nWritten by: Garrett Taylor and Daniel Lempert\n\nEdited by: Sierra
Berry   ...    - Ian Millhiser, The Supreme Court is about to decide one of the biggest economic policy cases ever, Vox (Sept. 15,   ...    - John Fritze, Supreme Court agrees to hear arguments in
case on Federal Reserve independence"], "published_date": null, "score": null}, {"title": "Who is Lisa Cook? Supreme Court takes up Fed governor's case.", "url":
"https://www.usatoday.com/story/money/2026/01/21/federal-reserve-lisa-cook-supreme-court/88282334007/", "snippet": "Who is Lisa Cook? Supreme Court takes up Fed governor's case.\n\nMONEY\n\nLisa
Cook\n\nAdd Topic\n\n# Who is Lisa Cook? Supreme Court takes up Fed governor's case.\n\nRachel Barber\n\nUSA TODAY\n\nJan. 21, 2026, 11:21 a.m. ET\n\nHear this story\n\nThe U.S. Supreme Court is
hearing oral arguments Jan. 21 in a case that will test the Federal Reserve\u2019s independence and determine whether President Donald Trump can follow through on his plans to fire Fed Gov. Lisa
Cook.\n\nIt\u2019s a case drawing the attention of Wall Stree", "highlights": ["Cook? Supreme Court takes up Fed governor's case.\n\nMONEY\n\nLisa Cook\n\nAdd Topic # Who is Lisa Cook? Supreme Court
takes up Fed governor's case.\n\nRachel Barber\n\nUSA TODAY Jan. 21, 2026, 11:21 a.m. ET\n\nHear this story The U.S. Supreme Court is hearing oral arguments Jan. 21 in a case that will test the
Federal Reserve\u2019s independence and determine whether President Donald Trump can follow through on his plans to fire Fed Gov. Lisa Cook. It\u2019s a case drawing the attention of Wall Street,
global markets and historians, as justices consider whether the president has the authority to fire a Federal Reserve official after months of exerting pressure on the institution. Some see the case
as a test of whether the nation's central bank can continue to operate independently of political influence. Trump attempted to fire Cook last August over allegations she had lied on two home mortgage
applications in 2021. At the time, Cook said Trump lacked authority to remove her and vowed to challenge the move in court in a statement from her attorney. In October, the Supreme Court said Trump
could not fire Cook immediately and that it would take up the case in January. Cook hasn't been charged with a crime. The oral arguments come a little more than a week after The New York Times broke
news that federal prosecutors opened an investigation into Federal Reserve Chair Jerome Powell and whether he lied to Congress about the scope of renovations at the Fed\u2019s headquarters. Powell,
whom Trump first nominated in 2017, called the investigation a \"pretext\" in a video statement released Jan. 11. He said the investigation is about whether \"monetary policy will be directed by   ...
The president has pressured Federal Reserve policymakers to lower its federal funds rate, a benchmark for interest rates around the country, since retaking office in 2025.   ...    ## Who is Lisa
Cook? Former President Joe Biden appointed Cook as governor of the Federal Reserve in 2022, making her the first Black woman to serve in the role. She was reappointed in 2023 for a term set to end in
2038. Before joining the Board, Cook served as a senior economist on the Council of Economic Advisers under former President Barack Obama. From 2000 to 2001, she worked as a senior adviser on finance
and development in the U.S. Department of   ...    bachelor's degree in philosophy from Spelman College, a second bachelor's degree in philosophy, politics and economics   ...    ## What does Lisa
Cook do? As one of seven members on the Fed\u2019s Board of Governors, Cook plays a leading role in guiding U.S. monetary policy.   ...    overall U.S. economy. ## Can Donald Trump fire Lisa Cook? In
the termination letter, Trump said he has authority to fire Cook under Article II of the U.S. Constitution and the Federal Reserve Act. The 1913 act does allow the president to remove a Fed official
\"for cause.\" The question of whether the alleged false statements on her past mortgage applications constitute \"cause\" are the subject of the legal battle. ## Does Lisa Cook support interest rate
cuts? Cook voted with the majority of Federal Open Market Committee members to lower rates at their last three meetings. Mike Skordeles, head of U.S. economics at Truist, and Timothy Chubb, chief
investment officer at Girard, previously   ...    Skord"], "published_date": "2026-01-21T16:21:26.000", "score": null}, {"title": "Supreme Court seems skeptical of Trump\u2019s firing of Fed board
member - CSMonitor.com", "url": "https://www.csmonitor.com/USA/Justice/2026/0121/supreme-court-lisa-cook-fed-powell", "snippet": "Supreme Court seems skeptical of Trump\u2019s firing of Fed board
member - CSMonitor.com\n\nSkip to main content Skip to main menu Skip to search Skip to footer\n\nLaw & Courts\n\n|\n\nNathan Howard/Reuters\n\nFederal Reserve governor Lisa Cook, accompanied by
lawyer Abbe Lowell, looks on outside the U.S. Supreme Court as the justices consider President Donald Trump's effort to fire her, in Washington, Jan. 21, 2026.\n\nLoading...\n\nJan. 21, 2026, 6:09
p.m. ET\n\nThe independence of the Federal Reserve appeared fro", "highlights": ["Supreme Court seems skeptical of Trump\u2019s firing of Fed board member - CSMonitor.com   ...    Federal Reserve
governor Lisa Cook, accompanied by lawyer Abbe Lowell, looks on outside the U.S. Supreme Court as the justices consider President Donald Trump's effort to fire her, in Washington, Jan. 21, 2026.
Loading...\n\nJan. 21, 2026, 6:09 p.m. ET The independence of the Federal Reserve appeared front of mind for the U.S. Supreme Court Wednesday as the justices heard oral argument in a case about the
firing of a member of the central bank\u2019s board. While the high court has in other recent cases appeared inclined to give the president of the United States more power   ...    A majority of
Supreme Court justices appeared wary of President Donald Trump\u2019s attempt to remove a member of the Federal Reserve Board, given the central bank\u2019s importance to the U.S. economy.   ...
President Donald Trump criticized board members of the Fed for months for refusing to lower interest rates as much as he would like. Past presidents have done the same, but because federal law held
that they could only dismiss members of   ...    far as they went. In August, Mr. Trump went a step further. He fired Lisa Cook, a member of the Fed\u2019s Board of Governors, over allegations that
she committed mortgage fraud. The mortgage fraud allegations were \u201ccause\u201d for her dismissal, Mr. Trump contended in a social media post. Ms. Cook, who has denied the allegations, has not
been formally charged. Days after her dismissal, she filed a lawsuit challenging it. A District Court judge ruled in her favor in September. The judge temporarily reinstated her to the Fed board,
pending the conclusion of the lawsuit, on the reasoning that her removal likely was unlawful. An appeals court agreed, and Mr. Trump appealed to the Supreme Court. Throughout oral argument on
Wednesday, the lawyers and justices in the courtroom agreed on one point: the Supreme Court\u2019s assertion \u2013 in an unsigned order issued earlier this term in a separate case \u2013 that Fed
governors are entitled to stronger removal protections because the central bank is \u201ca uniquely structured, quasi-private entity.\u201d Among many other things, the justices questioned whether
they should resolve such a weighty case \u2013 with implications for presidential power and for the global economy \u2013 when the case has faced so little scrutiny in the lower courts. \u201cIs there
any reason this whole matter had to be handled ... in such a hurried manner?\u201d asked Justice Samuel Alito, a   ...    Justice Sonia Sotomayor, one of the court\u2019s liberal members, agreed.
\u201cWe know the independence of the agency is very important,\u201d she said. \u201cWaiting, at least for lower courts to look at   ...    Several important questions remain unanswered in the Cook
case, the justices noted. Does Mr. Trump\u2019s social media post   ...    be simple \u201cnegligence\u201d or, as the Trump administration claims, \u201cgross negligence\u201d that justifies removal
from office? John Sauer, the U.S. solicitor general, argued that Ms. Cook, a person who helps to set interest rates for the entire country, appears to be \u201cplaying fast and loose and trying to get
a favorable mortgage rate for herself.\u201d That, he said, is causing \u201cgrievous reputational harm to the Federal Reserve.\u201d Thus, he concluded, the court should remove the temporary
injunction barring Ms. Cook\u2019s termination. And not only that: While Mr. Sauer emphasized that Fed board members can only be removed \u201cfor cause,\u201d he argued that there are limits to when
courts can review a president\u2019s determination of what that \u201ccause\u201d is. \u201cThe President has made a determination, it clearly does relate to conduct, fitness, ability, or competence
for that   ...    Ms. Cook\u2019s lawyer, Paul Clement, countered that there \u201cneeds\u201d to be judicial review, especially of what the president   ...    \u201cIf there\u2019s no judicial
review, then this is all kind of a joke,\u201d he added. As the Supreme Court debates how to resolve this case, external pressure continues to mount. Jerome Powell, the Fed   ...    for lower interest
rates. A decision in the case is expected by the summer.\n\nYou've read of free articles. Subscribe to continue.   ...    Subscribe\n\n## Related stories ### 90 years ago, the Supreme Court limited
whom presidents can fire. Trump wants to reverse that. ### The Explainer Why claims of mortgage fraud are central to Trump\u2019s push to influence Fed ### The Supreme Court has given Trump early
wins. Now, it has to explain why. Read this article in https://www.csmonitor.com/USA/Justice/2026/0121/supreme-court-lisa-cook-fed-powell Start your subscription today
https://www.csmonitor.com/subscribe"], "published_date": "2026-01-21T23:09:30.000", "score": null}, {"title": "Trump Firing of Fed's Lisa Cook: U.S. Supreme Court Hears Oral Arguments", "url":
"https://foreignpolicy.com/2026/01/21/united-states-supreme-court-case-trump-lisa-cook-fed/", "snippet": "Trump Firing of Fed's Lisa Cook: U.S. Supreme Court Hears Oral Arguments\n\nAnalysis\n\n# U.S.
Supreme Court Hears Oral Arguments in Trump-Lisa Cook Case\n\n## Firing central bank governors may prove to be a red line.\n\nThe neoclassical style U.S. Supreme Court building is seen from below,
looming against a deep blue sky. A view of the US Supreme Court in Washington on Jan. 21. Brendan Smialowski / AFP\n\n- United States\n- Economics\n\nJanuary 21, 2026, 3:35 PM\n\nWhile U.S. President
Donald Trump was in Dav", "highlights": ["Trump Firing of Fed's Lisa Cook: U.S. Supreme Court Hears Oral Arguments\n\nAnalysis # U.S. Supreme Court Hears Oral Arguments in Trump-Lisa Cook Case ##
Firing central bank governors may prove to be a red line. The neoclassical style U.S. Supreme Court building is seen from below, looming against a deep blue sky. A view of the US Supreme Court in
Washington on Jan. 21. Brendan Smialowski / AFP - United States\n- Economics\n\nJanuary 21, 2026, 3:35 PM While U.S. President Donald Trump was in Davos, Switzerland, making his case for why Europe
should give him control of Greenland, the U.S. Supreme Court heard another case that has a lot of importance for the dollar, the economy, and the   ...    While U.S. President Donald Trump was in
Davos, Switzerland, making his case for why Europe should give him control of Greenland, the U.S. Supreme Court heard another case that has a lot of importance for the dollar, the economy, and the
...    tremors and bond markets the yips. The case before the Supreme Court is about Trump\u2019s effort to remove Lisa Cook, a Federal Reserve governor, because of alleged irregularities with a
mortgage that she secured before she joined the bank. This matters more than usual because Trump just tried to remove Jerome Powell, the chairman of the Federal Reserve, just last week. The Federal
Reserve is the U.S central bank, which sets interest rates that basically rule the world. Cook, like most other Fed governors, has long resisted Trump\u2019s pressure to cut lending rates to turbo-
boost the economy, because inflation is persistent. Her attempted ouster raised concerns about the central bank\u2019s independence and opened up questions about whether and in what circumstances the
president can legally fire a member of the Fed. That was the focus of hours of oral arguments before the Supreme Court on Wednesday. The government argued that Cook should be fired for cause due to
the mortgage fraud allegations, but not because she opposes an easy-money policy. Her lawyer said those allegations were a boondoggle. The justices seemed skeptical of the government\u2019s arguments,
as well they might, given the precedents of deference toward Fed independence. It\u2019s not clear where this case will come down, but oral arguments did not lean in the government\u2019s direction.
What is more important is the markets\u2019 reaction to Trump\u2019s increasingly off-kilter approach to policymaking, of which his assaults on the Fed form only a part. The U.S. Congress will not
restrain him\u2014but in the past, markets have, most   ...    30-year bonds, which is a sign of flagging confidence in the dollar and the stewardship of it. U.S. Treasury Secretary Scott Bessent said
on Wednesday, after Denmark\u2019s flagship investment fund said it would sell its U.S. assets, that   ...    States worth at least a $20 billion put.) There are other cases\u2014 even bigger
ones\u2014yet to be decided at the Supreme Court, starting with the ruling on Trump\u2019s   ...    waiting to see what happens with Greenland, Venezuela, the trade deals, and the rest. When it comes
to a ruling in the Cook case, the world may not have to wait too long, as the justices\u2019 responses to oral arguments suggest that the decision may be fairly straightforward. However, the court has
until the summer to rule on this case, as it does on the even bigger one on tariffs. - United States\n- Economics   ...    A photo illustration showing six classical Greek or Roman-style columns, plus
a stack of televisions as the seventh   ...    In a handout photo provided by the U.S. Navy, a stealth fighter prepares to launch from the flight deck of the USS   ...    October 28, 2025 in Yokosuka,
Japan. ### What War With Iran Would Look Like\n\nAnalysis\n\n,\n\nLoading graphics"], "published_date": "2026-01-21T20:35:05.000", "score": null}, {"title": "Supreme Court: Trump bid to fire Fed
Governor Lisa Cook", "url": "https://www.cnbc.com/2026/01/21/supreme-court-trump-fed-lisa-cook-powell.html/", "snippet": "Supreme Court: Trump bid to fire Fed Governor Lisa Cook\n\nKey Points\n\n- The
arguments come less than two weeks after Fed Chair Jerome Powell disclosed he was under criminal investigation by the U.S. attorney's office in Washington, D.C., over the central bank's pricey
building renovation project.\n- The case could have long-term effects on the Fed's independence in setting interest rates.\n- Fed Governor Lisa Cook's job seemed safe from firing by President Trump
after Supreme Court justices skeptic", "highlights": ["Supreme Court: Trump bid to fire Fed Governor Lisa Cook\n\nKey Points - The arguments come less than two weeks after Fed Chair Jerome Powell
disclosed he was under criminal investigation by   ...    - The case could have long-term effects on the Fed's independence in setting interest rates. - Fed Governor Lisa Cook's job seemed safe from
firing by President Trump after Supreme Court justices skeptically questioned the Trump administration's lawyers on Wednesday about the grounds for Cook's would-be termination and its   ...    Federal
Reserve Governor Lisa Cook's job seemed safe from firing by President Donald Trump after Supreme Court justices skeptically questioned the Trump administration's lawyers on Wednesday about the grounds
for Cook's would-be   ...    Justice Brett Kavanaugh warned Solicitor General D. John Sauer about the effects of his argument that Trump could fire   ...    Kavanaugh, one of the court's six
conservatives. Cook, who was in the courtroom Wednesday, sued Trump in September, challenging the president's claimed power to summarily remove her for uncharged allegations that she committed
mortgage fraud. \"The real question is to what extent we believe the public is harmed to allow Ms. Cook to remain in post during the pendency of this case?\" asked Justice Ketanji Brown Jackson,
referring to Cook's lawsuit, which remains pending in a federal district court. Jackson is one of the court's three liberal members.   ...    Paul Clement, who represented Cook at the hearing, leaned
in during his arguments on words that the Supreme Court in an   ...    for now. At stake is not only the fate of Cook \u2014 who denies any wrongdoing \u2014 but potentially the Fed's future
independence to   ...    Underscoring those stakes is the recent disclosure by Fed Chairman Jerome Powell that he is the subject of a criminal   ...    When Trump moved to fire Cook in late August
\u2014 the first time a president had ever attempted such a move \u2014 there was   ...    If Cook and Powell were to be removed from the Fed's seven-member board, Trump would be in a position to
appoint a   ...    Trump did not cite Cook's stance on interest rates when he said he was firing her.   ...    Cook, the first Black woman to serve on the Fed board, was reappointed by Biden in 2023
to serve a full 14-year term. Under the Federal Reserve Act of 1913, only the president can terminate a Fed board member, and a governor like Cook can only be terminated \"for cause.\" The law does
not detail what would constitute \"cause,\" but cause has historically been understood to mean malfeasance or dereliction of duty. After Cook sued Trump to block her removal from the Fed, a federal
district court judge in Washington ruled that she could remain with the central bank pending the outcome of her lawsuit. Judge Jia Cobb, in that ruling, wrote that \"Cook has made a strong showing
that her purported removal was done in violation of the Federal Reserve Act's 'for cause' provision.\" Cobb said that \"best reading\" of that provision is that the alleged cause for removal relates
to a governor's actions while \"in office.\" The allegations against Cook relate to actions she took before joining the Fed. The Department of Justice appealed Cobb's ruling, but was unsuccessful. The
DOJ then asked the Supreme Court to take the case. In a filing, the DOJ said that the \"determination of cause\" for termination is subject to \"the unreviewable discretion of the President.\" \"In
any case, the President has identified sufficient cause here,\" the filing says.   ...    \"That the Federal Reserve Board plays a uniquely important role in the American economy only heightens the
government's   ...    \"Put simply, the President may reasonably determine that interest rates paid by the American people should not be set by a Governor who appears to have lied about facts material
to the interest rates she secured for herself\u2014and refuses to explain the apparent misrepresentation,\" the filing said. A general view of U.S. Supreme Court as justices could issue at least one
ruling in several major cases pending including a decision on the legality of President Donald Trump's sweeping global tariffs, in Washington, D.C., U.S., Jan. 20, 2026.   ...    All three former
living Fed chairs \u2014 Alan Greenspan, Ben Bernanke and Janet Yellen \u2014 signed on to a legal brief with the Supreme Court arguing against Cook's removal, along with a group of former Treasury
secretaries, chairs of the   ...    The brief says that Congress \"intentionally\" designed the Fed \"as a uniquely independent entity, largely insulated from political pressures that could otherwise
prioritize short-term economic gain over long-term stability and growth.\" \"Granting the government's request to remove Governor Cook from the Board immediately would upset these longstanding
protections and the essential functions they serve,\" the brief says. \"Doing so would expose the"], "published_date": "2026-01-21T11:00:01.000", "score": null}]
```

```json
{
  "query": "Lisa Cook Federal Reserve"
}
```

### 📋 Result

```
{"markets": [], "query": "Lisa Cook Federal Reserve"}
```

## 💬 Response

Good, I have extensive context. Now let me search for the most recent developments — specifically whether the Supreme Court has issued its ruling yet.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Trump v Cook Supreme Court ruling decision 2026 April"
}
```

### 📋 Result

```
{"query": "Trump v Cook Supreme Court ruling decision 2026 April", "results": [{"title": "Trump v. Cook - SCOTUSblog", "url": "https://www.scotusblog.com/cases/case-files/trump-v-cook/", "snippet": "|
09/18/2025 | [Application (25A312) for a stay, submitted to The Chief Justice.](https://www.supremecourt.gov/DocketPDF/25/25A312/374989/20250918113300065_Trump%20v%20Cook%20app.pdf) |\n| 09/18/2025 |
[Opposition to Request for Immediate Administrative Stay filed.](https://www.supremecourt.gov/DocketPDF/25/25A312/375049/20250918150026516_Trump%20v.%20Cook%20et%20al.%2025A312.pdf) |\n| 09/19/2025 |
Response to application (25A312) requested by The Chief Justice, due by 4 p.m. (EDT), on September 2", "api_data": null, "hint": null}, {"title": "Trump v. Cook - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Trump_v._Cook", "snippet": "Donald J. Trump, et al. v. Lisa D. Cook is a lawsuit brought by Lisa Cook, a member of the Federal Reserve Board of Governors, against U.S.
president Donald Trump, the board, and its chairman, Jerome Powell. Cook contended that her \"for cause\" removal, executed by Trump as president, was not justified.\nOn September 9, 2025, District of
Columbia U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the firing of Cook, stating that \"the Court finds that Cook has made a stro", "api_data": {"content": [{"type":
"text", "text": "{\"title\": \"Trump v. Cook\", \"url\": \"https://en.wikipedia.org/wiki/Trump_v._Cook\", \"extract\": \"Donald J. Trump, et al. v. Lisa D. Cook is a lawsuit brought by Lisa Cook, a
member of the Federal Reserve Board of Governors, against U.S. president Donald Trump, the board, and its chairman, Jerome Powell. Cook contended that her \\\"for cause\\\" removal, executed by Trump
as president, was not justified.\\nOn September 9, 2025, District of Columbia U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the firing of Cook, stating that \\\"the
Court finds that Cook has made a strong showing that her purported removal was done in violation of the Federal Reserve Act's 'for cause' provision.\\\" On September 15, the United States Court of
Appeals for the District of Columbia Circuit rejected an emergency appeal by the Trump administration to remove Cook before the September 2025 meeting of the Federal Open Market Committee. On October
1, the Supreme Court rejected an emergency appeal filed by the Trump administration to remove Cook. Oral arguments were held in January 2026.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title":
"Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information Institute", "url": "https://www.law.cornell.edu/supct/cert/25A312", "snippet": "Trump v. Cook\nIssues\nWhether the
president\u2019s removal of a member of the Federal Reserve comported with the relevant procedural requirements and whether the removal was for sufficient cause.\n[United States Court of Appeals for
the D.C. Circuit](https://www.cadc.uscourts.gov/internet/home.nsf)\nThis case considers whether the removal of Lisa Cook, a member of the Federal Reserve Board of Governors, by President Donald J.
Trump, comported with constitutional and statutory requirements. The Court mus", "api_data": null, "hint": null}, {"title": "Search - Supreme Court of the United States", "url":
"https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a312.html", "snippet": "Jeffrey Paul DeSousa\nCounsel of Record\nFlorida Office of the Attorney General\n107 W.
Gaines Street\nTallahassee, FL 32399\njeffrey.desousa@myfloridalegal.com\nPh: 5088018425\nParty name: State of Florida, 21 other States and the Arizona Legislature\nSteven Andrew Engel\nCounsel of
Record\nDechert LLP\n1900 K Street, NW\nWashington, DC 20006\nSTEVEN.ENGEL@DECHERT.COM\nPh: 2022613369\nParty name: The Chamber of Commerce of the United States\nSarah Elaine Harrington\nCounsel of
Record\nCovington & Burling LLP\nOne", "api_data": null, "hint": null}, {"title": "Trump v. Cook", "url": "https://www.oyez.org/cases/2025/25A312", "snippet": "Facts of the case\nIn 2023, President
Joseph Biden nominated Lisa D. Cook for a full 14-year term on the Board of Governors of the Federal Reserve System after she had served a short unexpired term beginning in 2022. The Senate confirmed
her to the new term in September 2023. In August 2025, William Pulte, Director of the Federal Housing Finance Agency, referred allegations against Cook to the Department of Justice, claiming she had
committed mortgage fraud in 2021\u2014before she joined the Board\u2014by ", "api_data": null, "hint": null}, {"title": "Trump v. Cook \u2013 Protecting the Rule of Law and Separation of Powers by
Urging the Supreme Court to Apply the Correct Standard for Claims that the Government is Acting Without Legal Authority - ACLU of DC", "url": "https://www.acludc.org/cases/trump-v-cook-protecting-the-
rule-of-law-and-separation-of-powers-by-urging-the-supreme-court-to-apply-the-correct-standard-for-claims-that-the-government-is-acting-without-legal-authority/", "snippet": "Sign up to be the first
to hear about how to take action.\nBy completing this form, I agree to receive occasional emails per the terms of the ACLU\u2019s [privacy statement.](https://www.aclu.org/about/privacy/statement)\nBy
completing this form, I agree to receive occasional emails per the terms of the ACLU\u2019s [privacy statement](https://www.aclu.org/about/privacy/statement).", "api_data": null, "hint": null},
{"title": "Trump v. Cook after Oral Argument: SCOTUS Spotlight on Separation of Powers | News & Events | Goodwin", "url": "https://www.goodwinlaw.com/en/news-and-events/events/2026/01/practices-cldr-
trump-v-cook-after-oral-argument", "snippet": "Summary\nOn January 21, the Supreme Court heard arguments in Trump v. Cook, addressing President Trump\u2019s removal of Federal Reserve Governor Lisa
Cook, and members of Goodwin\u2019s Supreme Court practice were in the courtroom to see it. This case is one of a long string of removals of agency heads by the Trump Administration, this time
involving an agency that has a massive impact on the American economy. In this webinar, [Jaime Santos](https://www.goodwinlaw.com/en/people/s/santos-jaime), [Jordan Bo", "api_data": null, "hint":
null}, {"title": "Trump v. Cook - Ballotpedia", "url": "https://ballotpedia.org/Trump_v._Cook", "snippet": "[reader survey](https://p5o9e703t70.typeform.com/to/J1GXYZaO?utm_source=sitenotice).\nTrump
v. Cook\n![](https://cdn.ballotpedia.org/images/d/db/SCOTUS-Building_at_an_Angle.jpg)\n![]() |\n[United States Supreme Court](https://ballotpedia.org/United_States_Supreme_Court)[Chief Justice John
Roberts](https://ballotpedia.org/John_Roberts_(Supreme_Court))\u2022[Clarence Thomas](https://ballotpedia.org/Clarence_Thomas_(Supreme_Court))\u2022[Samuel
Alito](https://ballotpedia.org/Samuel_Alito)\u2022[Sonia Sotomayor](https", "api_data": null, "hint": null}, {"title": "Historian\u2019s Amicus Brief in Trump v. Cook | Brennan Center for Justice",
"url": "https://www.brennancenter.org/our-work/research-reports/historians-amicus-brief-trump-v-cook", "snippet": "This case arises from the Trump administration\u2019s attempt to remove Lisa Cook
from the Federal Reserve Board of Governors.\nAfter Cook challenged the removal, the federal district court in Washington, D.C. issued a ruling that would keep her in office until her lawsuit is fully
resolved. The D.C. Circuit allowed that ruling to stand. When the Trump administration appealed to the U.S. Supreme Court, the Justices scheduled oral argument on the issue for January 2026.\nLegal
historian Jane Manners, a ", "api_data": null, "hint": null}, {"title": "Supreme Court remade by Trump ushers in historic defeats for civil rights - The Washington Post", "url":
"https://www.washingtonpost.com/politics/2026/04/09/supreme-court-conservative-trump-rulings/", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "Lisa Cook Federal Reserve Supreme Court decision ruling March April 2026"
}
```

### 📋 Result

```
{"query": "Lisa Cook Federal Reserve Supreme Court decision ruling March April 2026", "results": [{"title": "Supreme Court to Decide Fate of Fed Governor Lisa Cook - Washington Today", "url":
"https://nationaltoday.com/us/dc/washington/news/2026/04/13/supreme-court-to-decide-fate-of-fed-governor-lisa-cook/", "snippet":
"[Today](https://nationaltoday.com/today/)[Holidays](https://nationaltoday.com/national-day-topics/)[Birthdays](https://nationaltoday.com/birthday/)[Reminders](https://nationaltoday.com/reminders/)[Ci
ties](https://nationaltoday.com#)[Atlanta](https://nationaltoday.com/us/ga/atlanta/)[Austin](https://nationaltoday.com/us/tx/austin/)[Baltimore](https://nationaltoday.com/us/md/baltimore/)[Berwyn](htt
ps://nationaltoday.com/us/il/berwyn/)[Beverly Hills](https://nationaltoday.com/us/ca/beverly-hills/)[", "api_data": null, "hint": null}, {"title": "Supreme Court appears likely to allow Lisa Cook to
remain on Fed board - The Washington Post", "url": "https://www.washingtonpost.com/politics/2026/01/21/fed-lisa-cook-supreme-court-trump/", "snippet": null, "api_data": null, "hint": null}, {"title":
"Supreme Court allows the Fed's Lisa Cook to stay in office for now as Trump pushes to fire her", "url": "https://www.nbcnews.com/politics/supreme-court/supreme-court-allows-feds-lisa-cook-stay-
office-trump-fire-case-rcna232933", "snippet": "WASHINGTON \u2014 The Supreme Court on Wednesday deferred action on whether President Donald Trump can immediately fire Federal Reserve board member
Lisa Cook, instead agreeing to hear oral arguments in the case early next year.\nThe move means that Cook can remain in office while the consequential legal question is decided. The court will hear
oral arguments in January, the brief order said, with a ruling likely before the end of June.\nTrump had asked the court to allow him to immediately fire Cook w", "api_data": null, "hint": null},
{"title": "Supreme Court Orders Oral Argument on President's Decision to Remove Federal Reserve Governor Lisa Cook | Insights | Mayer Brown", "url":
"https://www.mayerbrown.com/en/insights/publications/2025/10/supreme-court-orders-oral-argument-on-presidents-decision-to-remove-federal-reserve-governor-lisa-cook", "snippet": "Supreme Court Orders
Oral Argument on President's Decision to Remove Federal Reserve Governor Lisa Cook\nIn an order issued on October 1, the Supreme Court allowed Federal Reserve Governor Lisa Cook to remain in
office\u2014leaving in place for now the lower court orders putting on hold President Trump\u2019s decision to remove her. The President had sought to remove Governor Cook \u201cfor cause\u201d under
the Federal Reserve Act\u2019s for-cause removal provision. The Supreme Court scheduled oral argument on the issue", "api_data": null, "hint": null}, {"title": "Opinion | Lisa Cook\u2019s Supreme
Court win is good sign for Federal Reserve - The Washington Post", "url": "https://www.washingtonpost.com/opinions/2025/10/01/lisa-cook-fed-supreme-court-trump/", "snippet": null, "api_data": null,
"hint": null}, {"title": "SCOTUS allows Lisa Cook to stay on Fed board into 2026, accepts case for January argument - ABC News", "url": "https://abcnews.com/Politics/scotus-allows-lisa-cook-stay-
fed-2026-accepts/story?id=126118156", "snippet": "SCOTUS allows Lisa Cook to stay on Fed board into 2026, accepts case for January argument\nThe Supreme Court moved to allow Lisa Cook to remain on the
central bank board.\nThe Supreme Court on Wednesday moved to allow Federal Reserve governor Lisa Cook to remain on the central bank board into 2026, saying it would take up President Donald Trump's
appeal seeking to remove her for cause during a hearing in January.\nThe Court did not explain its decision. There were no noted dissents.\nThe decision to", "api_data": null, "hint": null}, {"title":
"Supreme Court allows Federal Reserve governor Lisa Cook to keep her job - The Washington Post", "url": "https://www.washingtonpost.com/politics/2025/10/01/trump-supreme-court-lisa-cook-federal-
reserve/", "snippet": null, "api_data": null, "hint": null}, {"title": "Trump v. Cook - Wikipedia", "url": "https://en.wikipedia.org/wiki/Trump_v._Cook", "snippet": "Donald J. Trump, et al. v. Lisa D.
Cook is a lawsuit brought by Lisa Cook, a member of the Federal Reserve Board of Governors, against U.S. president Donald Trump, the board, and its chairman, Jerome Powell. Cook contended that her
\"for cause\" removal, executed by Trump as president, was not justified.\nOn September 9, 2025, District of Columbia U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the
firing of Cook, stating that \"the Court finds that Cook has made a stro", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Trump v. Cook\", \"url\":
\"https://en.wikipedia.org/wiki/Trump_v._Cook\", \"extract\": \"Donald J. Trump, et al. v. Lisa D. Cook is a lawsuit brought by Lisa Cook, a member of the Federal Reserve Board of Governors, against
U.S. president Donald Trump, the board, and its chairman, Jerome Powell. Cook contended that her \\\"for cause\\\" removal, executed by Trump as president, was not justified.\\nOn September 9, 2025,
District of Columbia U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the firing of Cook, stating that \\\"the Court finds that Cook has made a strong showing that her
purported removal was done in violation of the Federal Reserve Act's 'for cause' provision.\\\" On September 15, the United States Court of Appeals for the District of Columbia Circuit rejected an
emergency appeal by the Trump administration to remove Cook before the September 2025 meeting of the Federal Open Market Committee. On October 1, the Supreme Court rejected an emergency appeal filed
by the Trump administration to remove Cook. Oral arguments were held in January 2026.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "US Supreme Court appears reluctant to let Trump fire
Fed\u2019s Lisa Cook | Business and Economy News | Al Jazeera", "url": "https://www.aljazeera.com/economy/2026/1/21/us-supreme-court-appears-reluctant-to-let-trump-fire-feds-lisa-cook", "snippet": "US
Supreme Court appears reluctant to let Trump fire Fed\u2019s Lisa Cook\nDuring two hours of arguments, some justices pressed US lawyer on why Cook was not given a chance to formally
respond.\n![epa12479651 Lisa Cook (R), member of the Federal Reserve Board, departs a board meeting at the Federal Reserve in Washington, DC, USA, 24 October 2025. The government shutdown has
restricted the Federal Reserve\u2019s access to official economic statistics that it relies on to make decisions regarding the economy ", "api_data": null, "hint": null}, {"title": "Supreme Court
keeps Fed's Lisa Cook in role for now, agrees to review case | Fox News", "url": "https://www.foxnews.com/politics/supreme-court-keeps-feds-lisa-cook-role-now-agrees-review-case", "snippet": "[Fed
Board Governor Lisa Cook suing to remain in her position](https://www.foxnews.com/video/6377947182112)\nFormer assistant FBI director Chris Swecker weighs in on the mortgage fraud allegations Lisa
Cook is facing on 'Sunday Night in America.'\nThe [Supreme Court](https://www.foxnews.com/category/politics/judiciary/supreme-court) on Wednesday agreed to review President [Donald
Trump](https://www.foxnews.com/category/person/donald-trump)'s effort to fire Federal Reserve Governor Lisa Cook, and w", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me check for the most recent news - specifically whether the Supreme Court has issued its ruling yet (expected by summer 2026). The search results show oral arguments were in January 2026, and a ruling is expected by summer. Let me also check for the very latest news from April 2026.

## 💬 Response

Let me check for the very latest developments, especially any SCOTUS ruling that may have come in recent days.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://nationaltoday.com/us/dc/washington/news/2026/04/13/supreme-court-to-decide-fate-of-fed-governor-lisa-cook/",
  "prompt": "What is the latest status of the Trump v. Cook Supreme Court case? Has a ruling been issued? What is happening in April 2026?"
}
```

### 📋 Result

```
{"url": "https://nationaltoday.com/us/dc/washington/news/2026/04/13/supreme-court-to-decide-fate-of-fed-governor-lisa-cook/", "content": "Based on the content provided:\n\n**Latest Status (as of April
13, 2026):**\n- The Supreme Court case regarding Trump's attempt to remove Federal Reserve Governor Lisa Cook is **pending** - no ruling has been issued yet\n- The Court is **scheduled to hear oral
arguments on Wednesday, April 17, 2026**\n- The case centers on Trump's August 2025 allegations of mortgage fraud against Cook, which her lawyers dispute as \"cherry-picking\" information and denial
of due process\n\n**What's Happening in April 2026:**\nThe Supreme Court will hear arguments that could redefine presidential power over the Federal Reserve. The decision will determine whether Trump
can remove Cook and could set precedent for future executive influence over the Fed's independence.\n\n**Relevant links:**\n- [Submit story updates](https://forms.nationaltoday.com/news?location=Washi
ngton%2C+DC&city=Washington&type=Update+Existing+Story&headline=Supreme+Court+to+Decide+Fate+of+Fed+Governor+Lisa+Cook&page=https%3A%2F%2Fnationaltoday.com%2Fus%2Fdc%2Fwashington%2Fnews%2F2026%2F04%2F
13%2Fsupreme-court-to-decide-fate-of-fed-governor-lisa-cook%2F)\n- [Washington top stories](https://nationaltoday.com/us/dc/washington/)\n- [Donald Trump birthday
page](https://nationaltoday.com/birthday/donald-trump/)", "title": "Supreme Court to Decide Fate of Fed Governor Lisa Cook - Washington Today"}
```

```json
{
  "query": "\"Trump v Cook\" Supreme Court ruling opinion April 2026"
}
```

### 📋 Result

```
{"query": "\"Trump v Cook\" Supreme Court ruling opinion April 2026", "results": [{"title": "Trump v. Cook - Wikipedia", "url": "https://en.wikipedia.org/wiki/Trump_v._Cook", "snippet": "Donald J.
Trump, et al. v. Lisa D. Cook is a lawsuit brought by Lisa Cook, a member of the Federal Reserve Board of Governors, against U.S. president Donald Trump, the board, and its chairman, Jerome Powell.
Cook contended that her \"for cause\" removal, executed by Trump as president, was not justified.\nOn September 9, 2025, District of Columbia U.S. District Court Judge Jia Cobb issued a preliminary
injunction preventing the firing of Cook, stating that \"the Court finds that Cook has made a stro", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Trump v. Cook\", \"url\":
\"https://en.wikipedia.org/wiki/Trump_v._Cook\", \"extract\": \"Donald J. Trump, et al. v. Lisa D. Cook is a lawsuit brought by Lisa Cook, a member of the Federal Reserve Board of Governors, against
U.S. president Donald Trump, the board, and its chairman, Jerome Powell. Cook contended that her \\\"for cause\\\" removal, executed by Trump as president, was not justified.\\nOn September 9, 2025,
District of Columbia U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the firing of Cook, stating that \\\"the Court finds that Cook has made a strong showing that her
purported removal was done in violation of the Federal Reserve Act's 'for cause' provision.\\\" On September 15, the United States Court of Appeals for the District of Columbia Circuit rejected an
emergency appeal by the Trump administration to remove Cook before the September 2025 meeting of the Federal Open Market Committee. On October 1, the Supreme Court rejected an emergency appeal filed
by the Trump administration to remove Cook. Oral arguments were held in January 2026.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Trump v. Cook - SCOTUSblog", "url":
"https://www.scotusblog.com/cases/case-files/trump-v-cook/", "snippet": "| 09/18/2025 | [Application (25A312) for a stay, submitted to The Chief
Justice.](https://www.supremecourt.gov/DocketPDF/25/25A312/374989/20250918113300065_Trump%20v%20Cook%20app.pdf) |\n| 09/18/2025 | [Opposition to Request for Immediate Administrative Stay
filed.](https://www.supremecourt.gov/DocketPDF/25/25A312/375049/20250918150026516_Trump%20v.%20Cook%20et%20al.%2025A312.pdf) |\n| 09/19/2025 | Response to application (25A312) requested by The Chief
Justice, due by 4 p.m. (EDT), on September 2", "api_data": null, "hint": null}, {"title": "Trump v. Cook | Supreme Court Bulletin | US Law | LII / Legal Information Institute", "url":
"https://www.law.cornell.edu/supct/cert/25A312", "snippet": "Trump v. Cook\nIssues\nWhether the president\u2019s removal of a member of the Federal Reserve comported with the relevant procedural
requirements and whether the removal was for sufficient cause.\n[United States Court of Appeals for the D.C. Circuit](https://www.cadc.uscourts.gov/internet/home.nsf)\nThis case considers whether the
removal of Lisa Cook, a member of the Federal Reserve Board of Governors, by President Donald J. Trump, comported with constitutional and statutory requirements. The Court mus", "api_data": null,
"hint": null}, {"title": "Search - Supreme Court of the United States", "url": "https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a312.html", "snippet": "Jeffrey Paul
DeSousa\nCounsel of Record\nFlorida Office of the Attorney General\n107 W. Gaines Street\nTallahassee, FL 32399\njeffrey.desousa@myfloridalegal.com\nPh: 5088018425\nParty name: State of Florida, 21
other States and the Arizona Legislature\nSteven Andrew Engel\nCounsel of Record\nDechert LLP\n1900 K Street, NW\nWashington, DC 20006\nSTEVEN.ENGEL@DECHERT.COM\nPh: 2022613369\nParty name: The
Chamber of Commerce of the United States\nSarah Elaine Harrington\nCounsel of Record\nCovington & Burling LLP\nOne", "api_data": null, "hint": null}, {"title": "Trump v. Cook", "url":
"https://www.oyez.org/cases/2025/25A312", "snippet": "Facts of the case\nIn 2023, President Joseph Biden nominated Lisa D. Cook for a full 14-year term on the Board of Governors of the Federal Reserve
System after she had served a short unexpired term beginning in 2022. The Senate confirmed her to the new term in September 2023. In August 2025, William Pulte, Director of the Federal Housing Finance
Agency, referred allegations against Cook to the Department of Justice, claiming she had committed mortgage fraud in 2021\u2014before she joined the Board\u2014by ", "api_data": null, "hint": null},
{"title": "Trump v. Cook \u2013 Protecting the Rule of Law and Separation of Powers by Urging the Supreme Court to Apply the Correct Standard for Claims that the Government is Acting Without Legal
Authority - ACLU of DC", "url": "https://www.acludc.org/cases/trump-v-cook-protecting-the-rule-of-law-and-separation-of-powers-by-urging-the-supreme-court-to-apply-the-correct-standard-for-claims-
that-the-government-is-acting-without-legal-authority/", "snippet": "Sign up to be the first to hear about how to take action.\nBy completing this form, I agree to receive occasional emails per the
terms of the ACLU\u2019s [privacy statement.](https://www.aclu.org/about/privacy/statement)\nBy completing this form, I agree to receive occasional emails per the terms of the ACLU\u2019s [privacy
statement](https://www.aclu.org/about/privacy/statement).", "api_data": null, "hint": null}, {"title": "Trump v. Cook after Oral Argument: SCOTUS Spotlight on Separation of Powers | News & Events |
Goodwin", "url": "https://www.goodwinlaw.com/en/news-and-events/events/2026/01/practices-cldr-trump-v-cook-after-oral-argument", "snippet": "Summary\nOn January 21, the Supreme Court heard arguments
in Trump v. Cook, addressing President Trump\u2019s removal of Federal Reserve Governor Lisa Cook, and members of Goodwin\u2019s Supreme Court practice were in the courtroom to see it. This case is
one of a long string of removals of agency heads by the Trump Administration, this time involving an agency that has a massive impact on the American economy. In this webinar, [Jaime
Santos](https://www.goodwinlaw.com/en/people/s/santos-jaime), [Jordan Bo", "api_data": null, "hint": null}, {"title": "Trump v. Cook - Ballotpedia", "url": "https://ballotpedia.org/Trump_v._Cook",
"snippet": "[reader survey](https://p5o9e703t70.typeform.com/to/J1GXYZaO?utm_source=sitenotice).\nTrump v. Cook\n![](https://cdn.ballotpedia.org/images/d/db/SCOTUS-Building_at_an_Angle.jpg)\n![]()
|\n[United States Supreme Court](https://ballotpedia.org/United_States_Supreme_Court)[Chief Justice John Roberts](https://ballotpedia.org/John_Roberts_(Supreme_Court))\u2022[Clarence
Thomas](https://ballotpedia.org/Clarence_Thomas_(Supreme_Court))\u2022[Samuel Alito](https://ballotpedia.org/Samuel_Alito)\u2022[Sonia Sotomayor](https", "api_data": null, "hint": null}, {"title":
"Historian\u2019s Amicus Brief in Trump v. Cook | Brennan Center for Justice", "url": "https://www.brennancenter.org/our-work/research-reports/historians-amicus-brief-trump-v-cook", "snippet": "This
case arises from the Trump administration\u2019s attempt to remove Lisa Cook from the Federal Reserve Board of Governors.\nAfter Cook challenged the removal, the federal district court in Washington,
D.C. issued a ruling that would keep her in office until her lawsuit is fully resolved. The D.C. Circuit allowed that ruling to stand. When the Trump administration appealed to the U.S. Supreme Court,
the Justices scheduled oral argument on the issue for January 2026.\nLegal historian Jane Manners, a ", "api_data": null, "hint": null}, {"title": "Policy Backgrounder: Trump v. Cook: Is the Fed
Special?", "url": "https://www.conference-board.org/research/ced-policy-backgrounders/trump-v-cook-is-the-fed-special", "snippet": "The Supreme Court held oral arguments in the case of Trump v. Cook,
testing on what grounds the President can fire officials of the Federal Reserve. The Court may decide the case on procedural grounds, but questions at oral argument indicated concern both on
procedural questions and support for the independence of the Federal Reserve; in all events, the case has significant implications for the independence of the Fed and for US business. Governors of the
Federal Reserve are appointed to 14-year", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Interesting - one source (nationaltoday.com) says oral arguments are scheduled for April 17, 2026, while other sources show oral arguments already happened in January 2026. The nationaltoday source seems like an AI-generated article that may be unreliable. The Wikipedia entry and all major news sources confirm oral arguments were held in January 2026.

Let me think about this more carefully. The nationaltoday source might be confusing things or might be about a second round of arguments. But the most authoritative sources (Wikipedia, SCOTUSblog, Reuters, NPR, CNBC) all confirm oral arguments were January 21, 2026, with a ruling expected by summer 2026 (end of June).


I'm noticing some conflicting information - that Washington Post headline from April 2026 might have details about the ruling, but the Wikipedia article doesn't mention a decision yet. The NationalToday piece keeps saying the case is pending with April 17 arguments scheduled, which contradicts the January timeline, so it's likely just an unreliable AI-generated article rather than reporting on a second round of arguments.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.scotusblog.com/cases/case-files/trump-v-cook/",
  "prompt": "What is the latest status of Trump v. Cook? Has a ruling or opinion been issued? What is the most recent docket entry?"
}
```

### 📋 Result

```
{"url": "https://www.scotusblog.com/cases/case-files/trump-v-cook/", "content": "Based on the docket entries provided, here is the latest status of Trump v. Cook:\n\n**Latest Status:**\n- The case was
argued before the Supreme Court on **January 21, 2026**\n- **No ruling or opinion has been issued yet** based on these docket entries\n- The case is still pending after oral arguments\n\n**Most Recent
Docket Entry:**\nJanuary 21, 2026 - \"Argued. For applicants: D. John Sauer, Solicitor General, Department of Justice, Washington, D. C. For respondent: Paul D. Clement, Alexandria,
Va.\"\n\n**Background:**\n- This began as an application for a stay (25A312) filed on September 18, 2025\n- On October 1, 2025, the Chief Justice referred the application to the full Court and
deferred it pending oral argument scheduled for January 2026\n- Oral arguments took place on January 21, 2026, as scheduled\n- The Court is now deliberating, with no decision announced as of the last
entry\n\n**Relevant links:**\n- [Application for stay (Sept 18, 2025)](https://www.supremecourt.gov/DocketPDF/25/25A312/374989/20250918113300065_Trump%20v%20Cook%20app.pdf)\n- [Response from Lisa D.
Cook, et al. (Sept 25, 2025)](https://www.supremecourt.gov/DocketPDF/25/25A312/377893/20250925151427957_20250925%20Cook%20SCOTUS%20Stay%20Opposition.pdf)\n- [Reply of Donald J. Trump (Sept 26,
2025)](https://www.supremecourt.gov/DocketPDF/25/25A312/378025/20250926150333128_25A312%20Cook%20Reply.pdf)\n- [Supplemental brief of Donald J. Trump (Nov 19,
2025)](https://www.supremecourt.gov/DocketPDF/25/25A312/385182/20251119160740717_25A312%20--%20Trump%20v.%20Cook%20-%20Supp.%20Br..pdf)\n- [Supplemental brief of Lisa D. Cook, et al. (Nov 19,
2025)](https://www.supremecourt.gov/DocketPDF/25/25A312/385180/20251119155936464_Cook%20Supplemental%20Brief.pdf)", "title": "Trump v. Cook"}
```

```json
{
  "query": "Lisa Cook Federal Reserve still serving April 2026"
}
```

### 📋 Result

```
{"query": "Lisa Cook Federal Reserve still serving April 2026", "results": [{"title": "Federal Reserve Governor Lisa Cook Reflects on the Stakes of Financial Stability | Yale School of Management",
"url": "https://som.yale.edu/story/2026/federal-reserve-governor-lisa-cook-reflects-stakes-financial-stability", "snippet": "![Federal Reserve governor Lisa
Cook](/sites/default/files/styles/scaled_140_/public/2026-04/SOM%20Lisa%20DeNell%20Cook-15.jpg.webp?itok=zYhGNMF9)\nFederal Reserve Governor Lisa Cook Reflects on the Stakes of Financial Stability\nIn
a talk presented by the Yale Program on Financial Stability, Cook discussed the Fed\u2019s approach to monitoring the U.S. financial system and lessons learned from her tenure.\nWhen the Australian
government eradicated feral cats on Macquarie Island, it succeeded in saving ", "api_data": null, "hint": null}, {"title": "SCOTUS allows Lisa Cook to stay on Fed board into 2026, accepts case for
January argument - ABC News", "url": "https://abcnews.com/Politics/scotus-allows-lisa-cook-stay-fed-2026-accepts/story?id=126118156", "snippet": "SCOTUS allows Lisa Cook to stay on Fed board into
2026, accepts case for January argument\nThe Supreme Court moved to allow Lisa Cook to remain on the central bank board.\nThe Supreme Court on Wednesday moved to allow Federal Reserve governor Lisa
Cook to remain on the central bank board into 2026, saying it would take up President Donald Trump's appeal seeking to remove her for cause during a hearing in January.\nThe Court did not explain its
decision. There were no noted dissents.\nThe decision to", "api_data": null, "hint": null}, {"title": "Lisa Cook - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lisa_Cook", "snippet": "Lisa DeNell
Cook (born 1964) is an American economist who was sworn in as a member of the Federal Reserve Board of Governors in 2022. She is the first black woman to sit on the board. Before her appointment to
the Federal Reserve Board, she was elected in January 2022 to the board of directors of the Federal Reserve Bank of Chicago. She was also a research associate at the National Bureau of Economic
Research.\nCook was previously a professor of economics and international relations at Michigan S", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Lisa Cook\", \"url\":
\"https://en.wikipedia.org/wiki/Lisa_Cook\", \"extract\": \"Lisa DeNell Cook (born 1964) is an American economist who was sworn in as a member of the Federal Reserve Board of Governors in 2022. She is
the first black woman to sit on the board. Before her appointment to the Federal Reserve Board, she was elected in January 2022 to the board of directors of the Federal Reserve Bank of Chicago. She
was also a research associate at the National Bureau of Economic Research.\\nCook was previously a professor of economics and international relations at Michigan State University and a member of the
American Economic Association's Executive Committee. An authority on international economics, especially the Russian economy, she has been involved in advising policymakers from the Obama
Administration to the Nigerian and Rwandan governments. Her research is at the intersection of macroeconomics and economic history, with recent work in African-American history and innovation
economics. Cook is regarded as one of the few prominent black female economists and has attracted attention within academia for her efforts in mentoring black women and advocating for their inclusion
in the field of economics.\\nOn January 14, 2022, Joe Biden nominated Cook to serve as Federal Reserve governor; she was confirmed by the U.S. Senate on May 10 after a 50\\u201350 vote was broken by a
tie breaker vote by Kamala Harris, and took office on May 23, 2022.\\nOn August 15, 2025, Federal Housing Finance Agency director Bill Pulte accused Cook of committing mortgage fraud, and sent a
referral letter to Attorney General Pam Bondi regarding the matter, encouraging that an investigation be launched by the Department of Justice. In September 2025, U.S. Pardon Attorney Ed Martin
started a Department of Justice criminal investigation of Cook over allegations of mortgage fraud. However, on September 12, Reuters published an analysis of \\\"loan [and] job-vetting forms\\\"
submitted by Cook, as well as property records, which directly contradict the Trump administration's allegations against her.\\nOn August 25, 2025, President Donald Trump announced that he was
removing Cook from the Federal Reserve Board of Governors, citing alleged \\\"deceitful and potentially criminal conduct\\\". Federal law allows governors to be removed only \\\"for cause\\\", a
provision intended to protect the central bank\\u2019s independence. Cook disputed the allegations and filed suit in federal court, arguing that her dismissal was unlawful and politically motivated.
As litigation proceeds, she remains legally considered an active governor, pending a judicial ruling on whether the president had authority to remove her.\\n\\n\", \"mode\": \"full\"}"}]}, "hint":
null}, {"title": "Federal Reserve Board - Lisa D. Cook", "url": "https://www.federalreserve.gov/aboutthefed/bios/board/cook.htm", "snippet": "Lisa D. Cook\n![Governor Lisa D.
Cook](/aboutthefed/images/Cook_Lisa_8x10_June_29_22-316_pp_rdax_130x162s.jpg)\nLisa D. Cook took office as a member of the Board of Governors of the Federal Reserve System on May 23, 2022, to fill an
unexpired term ending January 31, 2024. She was reappointed to the Board on September 8, 2023, and sworn in on September 13, 2023, for a term ending January 31, 2038.\nPrior to her appointment to the
Board, Dr. Cook was a professor of economics and international relatio", "api_data": null, "hint": null}, {"title": "ABC11 EyewitnessNews on X: \"SCOTUS allows Lisa Cook to stay on Fed into 2026
https://t.co/8Ae2ajzgyR\" / X", "url": "https://x.com/ABC11_WTVD/status/1973621516756566054", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or
switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9
2026 X Corp.", "api_data": null, "hint": null}, {"title": "News Wrap: Supreme Court lets Lisa Cook stay in her role at Federal Reserve for now | PBS News", "url":
"https://www.pbs.org/newshour/show/news-wrap-supreme-court-lets-lisa-cook-stay-in-her-role-at-federal-reserve-for-now", "snippet": "Leave your feedback Share Copy URL
https://www.pbs.org/newshour/show/news-wrap-supreme-court-lets-lisa-cook-stay-in-her-role-at-federal-reserve-for-now Email Facebook Twitter LinkedIn Pinterest Tumblr Share on Facebook Share on Twitter
Transcript Audio In our news wrap Wednesday, the Supreme Court is letting Federal Reserve Governor Lisa Cook stay in her role for now, the White House pulled its nominee to lead the Bureau of Labor
Statistics, residents of a Bronx apartment building were unharmed ", "api_data": null, "hint": null}, {"title": "Supreme Court declines to take action on Trump\u2019s request to fire Fed governor for
now - SCOTUSblog", "url": "https://www.scotusblog.com/2025/10/supreme-court-declines-to-take-action-on-trumps-request-to-fire-fed-governor-for-now/", "snippet": "Supreme Court declines to take action
on Trump\u2019s request to fire Fed governor for now\n![Amy Howe Amy Howe's Headshot](https://www.scotusblog.com/wp-content/uploads/2020/09/amy-howe-thumbnail.jpg?w=100&h=100)\n[Amy
Howe](https://www.scotusblog.com/author/amy-howe/)\n![The U.S. Supreme Court is shown March 17, 2025 in Washington, DC.](https://www.scotusblog.com/wp-
content/uploads/2025/09/GettyImages-2205530609.jpg)\nThe Supreme Court on Wednesday announced that it will hear oral arguments in January ", "api_data": null, "hint": null}, {"title": "Supreme Court
lets Lisa Cook remain as a Federal Reserve governor for now in unsigned order | PBS News", "url": "https://www.pbs.org/newshour/politics/supreme-court-lets-lisa-cook-remain-as-a-federal-reserve-
governor-for-now-in-unsigned-order", "snippet": "By \u2014 Mark Sherman, Associated Press Mark Sherman, Associated Press Leave your feedback Share Copy URL
https://www.pbs.org/newshour/politics/supreme-court-lets-lisa-cook-remain-as-a-federal-reserve-governor-for-now-in-unsigned-order Email Facebook Twitter LinkedIn Pinterest Tumblr Share on Facebook
Share on Twitter Supreme Court lets Lisa Cook remain as a Federal Reserve governor for now in unsigned order Politics Updated on Oct 1, 2025 12:51 PM EDT \u2014 Published on Oct 1, 2025 11:13 AM EDT
WASHING", "api_data": null, "hint": null}, {"title": "It\u2019s showdown time for the Fed's independence at the Supreme Court : NPR", "url": "https://www.npr.org/2026/01/21/nx-s1-5674893/supreme-
court-federal-reserve-lisa-cook", "snippet": "It's showdown time for the Fed's independence at the Supreme Court\nSCOTUS to hear case on president's power to fire Federal Reserve Governor Lisa
Cook\n![Fed Chair Jerome Powell speaks with Lisa Cook, a member of the Board of Governors of the Federal Reserve, during a meeting in Washington on June
25.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/6575x4383+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2Ffe%2F8c%2F89f82ed24e2f9701a493e0279", "api_data": null, "hint": null}, {"title": "Firing Federal Reserve Governor Lisa Cook", "url":
"https://www.epi.org/policywatch/firing-federal-reserve-governor-lisa-cook/", "snippet": null, "api_data": null, "hint": null}]}
```

## 💭 Thinking

Key findings:

1. **Lisa Cook is still serving on the Fed Board** - The Federal Reserve's own website still lists her, and she's been giving talks as recently as April 2026 at Yale.

2. **Supreme Court status**: Oral arguments were held January 21, 2026. No ruling has been issued yet (as of SCOTUSblog's docket). A ruling is expected by end of June 2026.

3. **The justices appeared skeptical** of Trump's attempt to fire Cook during oral arguments. Multiple sources say the Court "seemed likely" to allow Cook to stay.

Now let me analyze the meta-prediction question:


The prediction market is asking whether the Cook removal probability will exceed 7.50% by April 21, 2026. Looking at the weekly history, the CP has been trending downward from 14% in mid-March to exactly 7.50% as of April 13, suggesting the market is pricing in the Court's apparent skepticism about removal. For the threshold to be crossed, we'd need a significant shift in sentiment over the next week. The Supreme Court seemed skeptical of Trump's case against Cook, and with Cook still actively serving and no ruling issued yet, the status quo suggests the CP will likely stay at or below 7.50%. The resolution window is only about 8 days away, so nothing dramatic would need to happen for the NO case to hold. Since the CP is exactly at the threshold right now, I need to clarify whether the question requires it to be strictly above 7.50% or if 7.50% itself counts as meeting the condition. SCOTUS typically releases opinions on Mondays, but a ruling by late April seems unlikely given the January arguments and the complexity of this constitutional case—May or June is more probable. Even if there is a ruling soon, the justices appeared skeptical of Trump's position, so a decision favoring Cook would actually lower the CP rather than raise it, and only a ruling against her would spike it above 7.50%, which seems improbable given their skepticism.

For the CP to move above 7.50%, I'd need either random upward noise from new forecasters, some unexpected breaking news that increases the odds of Cook leaving, or a surprising SCOTUS ruling against her—but the strong downward trend and the recent sharp drop from 10% to 7.5% suggest the market is pricing in Cook's likely continuation, making further decline more probable than a reversal. continued decline
- No obvious catalyst for an increase in the next 8 days
- 143 forecasters - a moderate base, reasonably stable

But the CP is exactly at the threshold. Even a single new forecaster with a higher estimate could push it up slightly. CP fluctuations in this range could easily be ±1-2%.

Actually, let me think about this differently. The CP was at 10% for two straight weeks (Mar 30 and Apr 6), then dropped to 7.5% on Apr 13. This is a significant drop. What caused it? Probably the general assessment that Cook is safe based on SCOTUS oral arguments and the passage of time without a ruling.

For the next week, the question is whether this downward pressure continues or reverses. With no new information expected, I'd expect the CP to stay in the range of 6-9%.

Given the uncertainty, I'd estimate around 40-45% chance the CP exceeds 7.50% by April 21. The downward trend suggests it'll stay at or below that threshold, but being right at the boundary means even minor upward fluctuations could cross it. I need to be careful about the exact resolution criteria though—the question resolves YES only if the CP is strictly higher than 7.50%, not equal to it, so I'm really asking whether it'll move above that precise threshold. The downward trend and lack of catalysts support a NO outcome, but we're sitting right at the threshold where even minor fluctuations could push it above 7.50%. Given the fundamental outlook and consistent downward movement, I'm settling on roughly 40% for YES—acknowledging that the CP could already be below 7.50% by the measurement point, but the thin margin leaves meaningful uncertainty.

Actually, there's a potential SCOTUS catalyst I should factor in. Between now and April 21, the Supreme Court could issue an opinion on Trump v. Cook. A pro-Cook ruling (which seems more likely based on oral arguments) would drop the CP significantly to maybe 3-5%, favoring NO. An anti-Cook ruling would spike it to 30-50%, favoring YES. The asymmetry is notable—the more probable outcome pushes CP lower while the less likely outcome creates a much larger upside move. With maybe a 10-15% chance SCOTUS rules this week, and roughly 85% odds they'd rule for Cook if they do, the expected impact of this catalyst actually leans toward NO.

Factoring everything in—the strong downward trend, lack of positive catalysts, and the likely direction of any SCOTUS ruling—I'm settling on 38% for YES.

## 💬 Response

Now I have a comprehensive picture. Let me synthesize my analysis.

**Key findings:**
1. **Lisa Cook is still actively serving** — she gave a talk at Yale in April 2026 and is listed on the Fed's board page
2. **SCOTUS case pending** — Oral arguments were held January 21, 2026. No ruling issued yet. Expected by end of June 2026.
3. **SCOTUS appeared very skeptical** of Trump's position — justices from both ideological sides expressed doubt about the administration's arguments
4. **CP trend is clearly downward**: 14% → 11% → 10% → 10% → 7.50% over the past 5 weeks
5. **CP is exactly at the threshold** (7.50%), meaning even a tiny fluctuation crosses it

Let me run a quick analysis on the CP dynamics.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# CP history (weekly snapshots)\ndates = ['2026-03-09', '2026-03-16', '2026-03-23', '2026-03-30', '2026-04-06', '2026-04-13']\ncps = [10.0, 14.0, 11.0, 10.0, 10.0, 7.5]\n\n# Calculate week-over-week changes\nchanges = [cps[i+1] - cps[i] for i in range(len(cps)-1)]\nprint(\"Week-over-week changes:\", changes)\nprint(\"Mean change:\", np.mean(changes))\nprint(\"Std of changes:\", np.std(changes))\n\n# The question: will CP be > 7.50% on April 21?\n# Current CP: 7.50% (exactly at threshold)\n# Need: strictly > 7.50%\n\n# Simple random walk model from current CP\n# Using observed weekly changes as basis\nmean_change = np.mean(changes)\nstd_change = np.std(changes)\n\nprint(f\"\\nMean weekly change: {mean_change:.2f} pp\")\nprint(f\"Std weekly change: {std_change:.2f} pp\")\n\n# Monte Carlo: simulate next week's CP\nnp.random.seed(42)\nn_sims = 100000\n\n# Model 1: Normal distribution based on observed changes\nnext_cp_normal = 7.5 + np.random.normal(mean_change, std_change, n_sims)\n# CP can't go below 1% or above 50% realistically\nnext_cp_normal = np.clip(next_cp_normal, 1, 50)\np_above_normal = np.mean(next_cp_normal > 7.5)\nprint(f\"\\nModel 1 (Normal random walk): P(CP > 7.5%) = {p_above_normal:.3f}\")\n\n# Model 2: Sample from observed changes (bootstrap)\nsampled_changes = np.random.choice(changes, size=n_sims, replace=True)\nnext_cp_boot = 7.5 + sampled_changes\nnext_cp_boot = np.clip(next_cp_boot, 1, 50)\np_above_boot = np.mean(next_cp_boot > 7.5)\nprint(f\"Model 2 (Bootstrap): P(CP > 7.5%) = {p_above_boot:.3f}\")\n\n# Model 3: Consider trend (last 3 weeks have been declining)\n# Use only recent changes (last 3) which show clearer downtrend\nrecent_changes = changes[-3:]  # [-1.0, 0.0, -2.5]\nmean_recent = np.mean(recent_changes)\nstd_recent = np.std(recent_changes)\nprint(f\"\\nRecent changes (last 3 weeks): {recent_changes}\")\nprint(f\"Mean recent change: {mean_recent:.2f} pp\")\nprint(f\"Std recent change: {std_recent:.2f} pp\")\n\nnext_cp_trend = 7.5 + np.random.normal(mean_recent, std_recent, n_sims)\nnext_cp_trend = np.clip(next_cp_trend, 1, 50)\np_above_trend = np.mean(next_cp_trend > 7.5)\nprint(f\"Model 3 (Trend-based): P(CP > 7.5%) = {p_above_trend:.3f}\")\n\n# Model 4: Account for SCOTUS ruling possibility\n# P(ruling this week) ~ 10%\n# P(rules for Cook | ruling) ~ 85% -> CP drops to ~4%\n# P(rules against Cook | ruling) ~ 15% -> CP spikes to ~40%\n# P(no ruling) ~ 90% -> random walk\n\np_ruling = 0.10\np_for_cook = 0.85\np_against_cook = 0.15\n\n# No ruling scenario\np_above_no_ruling = p_above_normal  # Use normal model\n# Ruling for Cook -> CP drops\np_above_for_cook = 0.0  # CP goes to ~4%, well below threshold\n# Ruling against Cook -> CP spikes\np_above_against_cook = 1.0  # CP goes to ~40%+\n\np_above_combined = (1 - p_ruling) * p_above_no_ruling + \\\n                    p_ruling * p_for_cook * p_above_for_cook + \\\n                    p_ruling * p_against_cook * p_above_against_cook\n\nprint(f\"\\nModel 4 (With SCOTUS ruling possibility):\")\nprint(f\"  P(CP > 7.5% | no ruling) = {p_above_no_ruling:.3f}\")\nprint(f\"  P(CP > 7.5% | ruling for Cook) = 0.000\")\nprint(f\"  P(CP > 7.5% | ruling against Cook) = 1.000\")\nprint(f\"  Combined P(CP > 7.5%) = {p_above_combined:.3f}\")\n\nprint(f\"\\n--- Summary ---\")\nprint(f\"Model 1 (Normal): {p_above_normal:.3f}\")\nprint(f\"Model 2 (Bootstrap): {p_above_boot:.3f}\")\nprint(f\"Model 3 (Trend): {p_above_trend:.3f}\")\nprint(f\"Model 4 (SCOTUS): {p_above_combined:.3f}\")\nprint(f\"Average: {np.mean([p_above_normal, p_above_boot, p_above_trend, p_above_combined]):.3f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Week-over-week changes: [4.0, -3.0, -1.0, 0.0, -2.5]\nMean change: -0.5\nStd of changes: 2.4899799195977463\n\nMean weekly change: -0.50 pp\nStd weekly change: 2.49
pp\n\nModel 1 (Normal random walk): P(CP > 7.5%) = 0.420\nModel 2 (Bootstrap): P(CP > 7.5%) = 0.200\n\nRecent changes (last 3 weeks): [-1.0, 0.0, -2.5]\nMean recent change: -1.17 pp\nStd recent
change: 1.03 pp\nModel 3 (Trend-based): P(CP > 7.5%) = 0.129\n\nModel 4 (With SCOTUS ruling possibility):\n  P(CP > 7.5% | no ruling) = 0.420\n  P(CP > 7.5% | ruling for Cook) = 0.000\n  P(CP > 7.5% |
ruling against Cook) = 1.000\n  Combined P(CP > 7.5%) = 0.393\n\n--- Summary ---\nModel 1 (Normal): 0.420\nModel 2 (Bootstrap): 0.200\nModel 3 (Trend): 0.129\nModel 4 (SCOTUS): 0.393\nAverage:
0.286\n", "stderr": "", "duration_ms": 221}
```

## 💭 Thinking

The models give a range of 13-42%. Let me think about which model is most appropriate.

Model 1 (Normal random walk with all changes): P = 0.42 - This uses all 5 weekly changes, but the early ones include an uptick that may not be representative.

Model 2 (Bootstrap from observed changes): P = 0.20 - This samples from actual observed changes. Out of 5 changes, only 1 was positive (the 4.0 increase), so 20% makes sense as a rough estimate.


Model 3 (Trend-based, last 3 weeks): P = 0.13 - This captures the clear downtrend in recent weeks but may be too narrow. Model 4 (With SCOTUS): P = 0.39 - This adds the small probability of a SCOTUS ruling, which mostly affects things through the unlikely but impactful anti-Cook ruling scenario.

I'm leaning toward something in the middle—the trend model seems too pessimistic while the normal model doesn't account enough for the recent downward momentum. The recent pattern of the CP sitting at 10% for two weeks before dropping to 7.5% is a strong signal that forecasters are shifting their expectations downward.

The fundamentals support this decline since SCOTUS appeared skeptical of Trump's case, but the CP being right at the threshold means even small movements could push it higher. With 143 forecasters involved, a few new estimates could shift the median, so I'm settling on around 35% as a reasonable middle ground that respects both the downward trend and the genuine uncertainty from the exact-threshold position.

Now I'm thinking through what could trigger a higher CP in the coming week—SCOTUS typically issues opinions on Mondays, and with April 21 being the resolution date, there's a window for a ruling that could significantly impact the outcome.

Most likely though, nothing major happens and the CP either stays flat or continues its gradual decline.

## 💬 Response

Now let me reflect on my analysis.
