# Reasoning Log: Will the European Court of Human Rights list at least one entry labeled “Grand Chamber Judgment” on its Delivery of Judgments page?

*Generated: 2026-03-20T04:43:31.614770+00:00*


## 💭 Thinking

Let me analyze this forecasting question about the European Court of Human Rights (ECHR) delivering at least one Grand Chamber Judgment between March 15-April 30, 2026.

Let me parse the resolution criteria carefully:
1. The ECHR's Delivery of Judgments page must show at least one entry dated March 15, 2026 through April 30, 2026
2. The entry must be labeled "Grand Chamber Judgment"
3. This must happen before April 30, 2026
4. Don't count hearings, chamber judgments, decisions, or press releases

Let me research this.

## 💬 Response

I'll analyze this question about the ECHR delivering at least one Grand Chamber Judgment between March 15 - April 30, 2026.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42647
  ]
}
```

### 📋 Result

```
{"post_id": 42647, "title": "Will the European Court of Human Rights list at least one entry labeled \u201cGrand Chamber Judgment\u201d on its Delivery of Judgments page?", "type": "binary", "url":
"https://www.metaculus.com/questions/42647", "background_info": "This forecasts whether the ECHR will deliver at least one Grand Chamber judgment during the rest of March and April
2026.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"0845537c738fd21e\",\"sheet_id\":387.1}}`", "resolution_criteria": "This question resolves to yes if the ECHR\u2019s Delivery
of Judgments page at https://www.echr.coe.int/delivery-of-judgments shows at least one entry dated March 15, 2026 through April 30, 2026 inclusive that is labeled \u201cGrand Chamber Judgment\u201d
before April 30, 2026. Otherwise, it resolves to no.", "fine_print": "Count only entries on the named page that are explicitly labeled \"Grand Chamber Judgment.\" Do not count Grand Chamber hearings,
chamber judgments, decisions, or press releases unless the entry itself is labeled that way. If the page is temporarily unavailable, use the directly linked case page for the same delivered judgment.
Candidate Sources: the specific judgment entry linked from the Delivery of Judgments page ; ECHR homepage at https://www.echr.coe.int.", "num_forecasters": 0, "community_prediction": null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.echr.coe.int/delivery-of-judgments",
  "prompt": "List all entries on this page, especially any labeled \"Grand Chamber Judgment\". What dates are shown? What types of judgments are listed?"
}
```

### 📋 Result

```
HTTP 403 for https://www.echr.coe.int/delivery-of-judgments. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series, company_financials,
world_bank_indicator).
```

```json
{
  "query": "ECHR Grand Chamber Judgment 2026 schedule delivery"
}
```

### 📋 Result

```
{"query": "ECHR Grand Chamber Judgment 2026 schedule delivery", "results": [{"title": "Delivery of judgments - ECHR Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/delivery-of-
judgments", "snippet": null, "api_data": null, "hint": null}, {"title": "Calendar of hearings - ECHR Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/calendar-of-hearings", "snippet":
null, "api_data": null, "hint": null}, {"title": "ECHR - Homepage of the European Court of Human Rights - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/", "snippet": null, "api_data": null,
"hint": null}, {"title": "Forthcoming judgments and decisions 17-19.03.2026 - HUDOC", "url": "https://hudoc.echr.coe.int/eng-press", "snippet": "\\t\\t\\n\\t\\t\\n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\
n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t
\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t
\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t
\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t", "api_data": null, "hint": null}, {"title": "All webcasts - ECHR Hearings - ECHR - ECHR /
CEDH", "url": "https://www.echr.coe.int/all-webcasts", "snippet": null, "api_data": null, "hint": null}, {"title": "The Grand Chamber \uf0d8 When does the Grand Chamber hear a case?", "url":
"https://www.echr.coe.int/documents/d/echr/faq_gc_eng", "snippet": null, "api_data": null, "hint": null}, {"title": "Forthcoming delivery - ECHR / CEDH", "url":
"https://www.echr.coe.int/w/forthcoming-delivery-12", "snippet": null, "api_data": null, "hint": null}, {"title": "HUDOC - European Court of Human Rights", "url": "https://hudoc.echr.coe.int/",
"snippet": "\\t\\t\\n\\t\\t\\n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\
t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t \\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\
\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t
\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t", "api_data": null, "hint": null},
{"title": "Cases pending before the Grand Chamber - ECHR Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/cases-pending-before-the-grand-chamber", "snippet": null, "api_data": null,
"hint": null}, {"title": "issued by the Registrar of the Court ECHR 004 (2026) 08.01.2026", "url":
"https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-8423564-11921102&filename=Judgments+and+decisions+of+08.01.2026.pdf", "snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

The delivery page returned a 403. Let me try alternative approaches to get the data.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.echr.coe.int/w/forthcoming-delivery-12",
  "prompt": "What forthcoming judgments are listed? Are any Grand Chamber Judgments scheduled? What dates are shown?"
}
```

### 📋 Result

```
HTTP 403 for https://www.echr.coe.int/w/forthcoming-delivery-12. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series, company_financials,
world_bank_indicator).
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.echr.coe.int/cases-pending-before-the-grand-chamber",
  "prompt": "What cases are pending before the Grand Chamber? How many cases are listed? Are any scheduled for delivery soon?"
}
```

### 📋 Result

```
HTTP 403 for https://www.echr.coe.int/cases-pending-before-the-grand-chamber. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "ECHR Grand Chamber judgment delivery March April 2026",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "MANJANI v. ALBANIA - 32283/23 (Article 8 - Right to respect for private and family life : Third Section) [2026] ECHR 44 (10 March 2026)", "url":
"https://www.bailii.org/eu/cases/ECHR/2026/44.html", "snippet": "MANJANI v. ALBANIA - 32283/23 (Article 8 - Right to respect for private and family life : Third Section) [2026] ECHR 44 (10 March
2026)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> MANJANI v. ALBANIA - 32283/23 (Article 8 - Right to respect for private and
family life : Third Section) [2026] ECHR 44 (10 March 2026) URL: https://www.bailii.org/eu/cases/ECHR/2026/44.html Cite as: [2026] ECHR 44\n\n---\n\n| [Home] [Databases] [World Law] [M", "highlights":
["here: BAILII>> Databases>> European Court of Human Rights>> MANJANI v. ALBANIA - 32283/23 (Article 8 - Right to respect for private and family life : Third Section) [2026] ECHR 44 (10 March 2026)
URL: https://www.bailii.org/eu/cases/ECHR/2026/44.html Cite as: [2026] ECHR 44  ...    | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New search] [Contents list]
[Help]\n\n---\n\nTHIRD SECTION CASE OF MANJANI v. ALBANIA\n\n(Application no. 32283/23)\n\nJUDGMENT Art 8 \u2022 Private life \u2022 Disproportionate refusal of the applicant's admission to the School
of Magistrates for training as a prosecutor on the basis of a juvenile theft conviction for which he had been legally rehabilitated \u2022 Art 8 applicable following both reason-based and consequence-
based approaches \u2022 Absolute and permanent ban on admission had a clear and serious impact on the applicant's personal choice as to the way he wished to pursue his professional and private life,
shape his social identity and develop relationship with others \u2022 Disregard of the applicant's age at the time of the offence and insufficient consideration of relevant circumstances \u2022
Impugned measure imposed at an early stage of his professional life having a significant effect in terms of its duration \u2022 Failure to carry out a thorough and sufficiently individualised
assessment of the applicant's personal situation Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n10 March 2026 This judgment will become final in the circumstances set out in
Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In the case of Manjani v. Albania, The European Court of Human Rights (Third Section), sitting as a Chamber composed of:
Ioannis Ktistakis, President, L\u0259tif H\u00fcseynov, Darian Pavli, \u00dana N\u00ed Raifeartaigh, Mateja \u0110urovi\u0107, Can\u00f2lic Mingorance Cairat, Vasilka Sancin, judges, and Milan
Bla\u0161ko, Section Registrar, Having regard to: the application (no. 32283/23) against the Republic of Albania lodged with the Court under Article 34 of the Convention for the Protection of Human
Rights and Fundamental Freedoms (\"the Convention\") by an Albanian national, Mr Shiqiri Manjani (\"the applicant\"), on 21 August 2023; the decision to give notice to the Albanian Government (\"the
Government\") of the complaint concerning the decision not to admit the applicant to the School of Magistrates on the basis of a spent juvenile conviction, and to declare inadmissible the remainder of
the application; the parties' observations;\n\nHaving deliberated in private on 10 February 2026, Delivers the following judgment, which was adopted on that date:\n\nINTRODUCTION 1. The case concerns
the refusal of the applicant's admission to the School of Magistrates for training as a prosecutor  ...    8. The applicant appealed against the Administrative Court of Appeal's decision. On 17 March
2022 the Supreme Court  ...    55. The approach of the national authorities stands in tension with the Court's case-law, in which special attention has been given to age in cases involving
interference with private life. In the case of Maslov, for example, which concerned the expulsion of a foreigner as a result of convictions for offences committed between 14 and 15 years of age, the
Grand Chamber held that when assessing the nature and seriousness of offences committed by an applicant, it must be taken into account whether he or she committed them as a juvenile or as an adult
(see Maslov v. Austria [GC], no. 1638/03, \u00a7 72, ECHR 2008). The decisive feature of that case was the young age at which the applicant committed the offences and, with one exception, their
non\u2011violent nature (ibid., \u00a7 81). Where the reason for an  ...    82\u201183)."], "published_date": null, "score": null}, {"title": "[PDF] Forthcoming judgments and decisions Tuesday 17
March 2026", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Forthcoming+judgments+and+decisions+17-19.03.2026.pdf&id=003-8480784-12021925&library=ECHR", "snippet": "issued by the
Registrar of the Court\nECHR 060 (2026)\n11.03.2026\nForthcoming judgments and decisions\nThe European Court of Human Rights will be notifying in writing eight judgments on Tuesday \n17 March 2026 and
eight judgments and / or decisions on Thursday 19 March 2026.\nPress releases and texts of the judgments and decisions will be available at 10 a.m. (local time) on \nthe Court\u2019s Internet site
(www.echr.coe.int).\nTuesday 17 March 2026\nB\u00fclent Ak\u00e7ay v. T\u00fcrkiye (application no. 41669/21) \nThe ap", "highlights": ["issued by the Registrar of the Court\nECHR 060
(2026)\n11.03.2026\nForthcoming judgments and decisions The European Court of Human Rights will be notifying in writing eight judgments on Tuesday 17 March 2026 and eight judgments and / or decisions
on Thursday 19 March 2026. Press releases and texts of the judgments and decisions will be available at 10 a.m. (local time) on the Court\u2019s Internet site (www.echr.coe.int).\nTuesday 17 March
2026\nB\u00fclent Ak\u00e7ay v. T\u00fcrkiye (application no. 41669/21) The applicant, Mr B\u00fclent Ak\u00e7ay, is a Turkish national who was born in 1975 and lives in Istanbul.  ...    Article 1 of
Protocol No. 1 (protection of property) and/or Article 8 (right to respect for private and \nfamily life). Thursday 19 March 2026\nB.G. v. France (no. 70945/17) The applicant, B.G. is a French
national who was born in 2000 and lives in Nieul (France). The case concerns the alleged failure to comply with the guarantees of the right to a fair trial and the  ...    Relying on Article 6
\u00a7\u00a7 1 and 2 of the Convention, the applicant complains of a breach of her right to  ...    M.A. v. France (no. 34324/24)  ...    the child\u2019s father lives, violated her right to respect
for her private and family life and her right to a fair hearing.\nThe Court will give its rulings in writing on the following cases, some of which concern issues which have already been submitted to
the Court, including excessive length of proceedings. These rulings can be consulted from the day of their delivery on the Court\u2019s online database HUDOC. They will not appear in the press release
issued on that day.\nTuesday 17 March 2026\nName Main application number Vill\u00e1s v. Hungary 33134/21\n3\nName Main application number\n\u00c7akar and Others v. T\u00fcrkiye 2541/19 G\u00fcrmen v.
T\u00fcrkiye 34365/22\n\u00d6zt\u00fcrk v. T\u00fcrkiye 50205/20\nYaman and Others v. T\u00fcrkiye 58473/17\nThursday 19 March 2026 Name Main application number\nN\u00e9meth v. Hungary 54323/22\nN.W.
v. Iceland 31606/19\nDubjago v. Latvia 47658/22 Jeremejevs v. Latvia 44644/21\nI.H. v. Norway 19628/21\nKave\u010dansk\u00fd v. Slovakia 43341/22 This press release is a document produced by the
Registry. It does not bind the Court. Decisions, judgments and further information about the Court can be found on www.echr.coe.int. Follow the Court on Bluesky @echr.coe.int, X ECHR_CEDH, LinkedIn,
and YouTube. Contact ECHRPress to subscribe to the press-release mailing list. Where can the Court\u2019s press releases be found? HUDOC - Press collection\nPress contacts echrpress@echr.coe.int |
tel.: +33 3 90 21 42 08  ...    Tracey Turner-Tretz (tel.: + 33 3 88 41 35 30)\nDenis Lambert (tel.: + 33 3 90 21 41 09) Inci Ertekin (tel.: + 33 3 90 21 55 30)\nJane Swift (tel.: + 33 3 88 41 29
04)\nClaire Windsor (tel.: + 33 3 88 41 24 01) The European Court of Human Rights was set up in Strasbourg by the Council of Europe member States in 1959 to deal with alleged violations of the 1950
European Convention on Human Rights."], "published_date": null, "score": null}, {"title": "Forthcoming judgments and decisions 17-19.03.2026 - HUDOC", "url": "https://hudoc.echr.coe.int/eng-press",
"snippet": "Judgment Arnar Helgi Larusson v. Iceland - No discrimination in wheelchair access to municipal cultural buildings\n\nTERMINATOR\n\nTERMINATOR\n\nresultCountPhrase\n\nKeyword Search (Press
Enter)\n\nAdvanced Search (Press Enter)\n\nFilters (Press Enter)\n\nTERMINATOR\n\nGo Back (Press Enter)\n\nFilters - Language (Press Enter)\n\nFilters - Press Collection (Press Enter)\n\nFilters -
Date (Press Enter)\n\nFilters - Judges (Press Enter)\n\nFilters - Organisations (Press Enter)\n\nFilters - Organisations (Press Enter)\n\nTERMINA", "highlights": ["Judgment Arnar Helgi Larusson v.
Iceland - No discrimination in wheelchair access to municipal cultural buildings  ...    Filters (Press Enter)\n\nTERMINATOR\n\nGo Back (Press Enter)\n\nFilters - Language (Press Enter) Filters -
Press Collection (Press Enter)\n\nFilters - Date (Press Enter)\n\nFilters - Judges (Press Enter) Filters - Organisations (Press Enter)\n\nFilters - Organisations (Press Enter)\n\nTERMINATOR\n\nSort
(Press Enter) Results (Press Enter)\n\nTERMINATOR\n\nTERMINATOR\n\nTERMINATOR\n\nGo Back (Press Enter)\n\nNavigator - View (Press Enter) Navigator - Case Details (Press Enter)\n\nNavigator - Related
(Press Enter)\n\nTERMINATOR This site uses cookies. Read our policy\u00d7 Please Note: Only currently visible results are printed. To print more you can either scroll to reveal more results or  ...
### Keyword Search\n\nTERMINATOR Go Back (Press Enter) SEARCH\n\nTERMINATOR\n\nFilters A\n\nAa Aa Aa Useful links| Advanced Search | Case-Law References| Other Languages | Contact Council of Europe|
European Court of Human Rights| Contact| Privacy| Help| Disclaimer Back to top\n\n## NARROW YOUR SEARCH\n\n## FILTERS ### LANGUAGELanguage filter to search by document language.This filter is
displayed in descending order of the number of documents in each language. Click on More\u2026 to open a full list of the available languages. Please note: Translations into non-official languages are
not made by the Registry of the Court, which does not check their accuracy or linguistic quality. They are published in HUDOC for information purposes only and the Court accepts no responsibility  ...
### STATEState filter to search for cases against a particular State or States. The filter is displayed in descending order of the number of documents by State. Click on More\u2026 to open a full list
of the States.\" data-original-title=\"\"  ...    TERMINATOR Go Back (Press Enter)\n\nTERMINATOR\n\n### DOCUMENT TYPE\n\nTERMINATOR Go Back (Press Enter)\n\nTERMINATOR ### DATEDate filter to search by
period.Examples: Before 27/04/2003; From 27/04/2003 to 17/12/2006, etc.This filter is displayed in ascending order of the number of documents by date.\" data-original-title=\"\" title=\"\" TERMINATOR
Go Back (Press Enter)\n\nTERMINATOR\n\nHUDOC Collection\n\n## MORE FILTERS\n\n0 Results Found Print Export\n\nRSS TERMINATOR Go Back (Press Enter) Sort By: Relevance Date (Newest) Date (Oldest) Case
Title (A-Z) Case Title (Z-A) State (A-Z) State (Z-A) App Number Ascending App Number Descending Date (Newest) then State Date (Oldest) then State TERMINATOR CRITERIA\n\nCLEAR ALL\n\nItem Id:
003-7348528-10034680\n\n\u00d7\n\nItem Id : 003-7348528-10034680 TERMINATOR Go Back (Press Enter)\n\n### This exact word or phrase\n\n### All of these words\n\n### Any of these words ### None of these
words\n\n### Near these words\n\n### Boolean Search\n\nOK CANCEL CLEAR\n\n\ufeff \ufeff"], "published_date": null, "score": null}, {"title": "GREEN ALLIANCE v. BULGARIA - 6580/22 (Art 8 - Home -
Correspondence - Shortcomings in the legal framework permitting the infiltration of \"agents on cover\" into private organisations and \"liberal professions\" Preliminary objections joined to merits
and dismissed : Third Section) [2026] ECHR 30 (17 February 2026)", "url": "http://www.bailii.org/eu/cases/ECHR/2026/30.html", "snippet": "GREEN ALLIANCE v. BULGARIA - 6580/22 (Art 8 - Home -
Correspondence - Shortcomings in the legal framework permitting the infiltration of \"agents on cover\" into private organisations and \"liberal professions\" Preliminary objections joined to merits
and dismissed : Third Section) [2026] ECHR 30 (17 February 2026)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> GREEN ALLIANCE v.
BULGARIA - 6580/22 (Art 8 - Home - Correspondence - Shortcomi", "highlights": [": Third Section) [2026] ECHR 30 (17 February 2026) # European Court of Human Rights\n\n--- You are here: BAILII>>
Databases>> European Court of Human Rights>> GREEN ALLIANCE v. BULGARIA - 6580/22 (Art 8 - Home - Correspondence - Shortcomings in the legal framework permitting the infiltration of \"agents on
cover\" into private organisations and \"liberal professions\" Preliminary objections joined to merits and dismissed : Third Section) [2026] ECHR 30 (17 February 2026) URL:
https://www.bailii.org/eu/cases/ECHR/2026/30.html Cite as: [2026] ECHR 30 --- | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New search] [Contents list] [Help]\n\n---\n\nTHIRD
SECTION CASE OF GREEN ALLIANCE v. BULGARIA\n\n(Application no. 6580/22)\n\nJUDGMENT Art 8 \u2022 Home \u2022 Correspondence \u2022 Shortcomings in the legal framework permitting the infiltration of
\"agents on cover\" into private organisations and \"liberal professions\" \u2022 Application by analogy of case-law principles developed in relation to covert surveillance \u2022 Work of an \"agent
on cover\" could interfere with the applicant association's rights \u2022 Mere existence of the relevant regulations amounting to an interference with the applicant association's rights \u2022
Examination of the legal framework in the abstract \u2022 Lack of minimum safeguards against arbitrariness and abuse \u2022 Quality-of-law requirement not met Prepared by the Registry. Does not bind
the Court.\n\nSTRASBOURG\n\n17 February 2026 This judgment will become final in the circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to  ...    TABLE OF
CONTENTS\n\nINTRODUCTION.. 1\n\nTHE FACTS. 2\n\nI. THE APPLICANT ASSOCIATION.. 2 II. THE REGULATIONS ON \"AGENTS ON COVER\". 2\n\nA. As originally issued in 2008. 2\n\nB. The 2018 amendments. 4  ...
2. Judgment of the Supreme Administrative Court 9\n\nB. On appeal 9\n\n1. Course of the proceedings. 9  ...    B. Costs and expenses. 43\n\nOPERATIVE PROVISIONS. 43\n\nIn the case of Green Alliance v.
Bulgaria, The European Court of Human Rights (Third Section), sitting as a Chamber composed of: Ioannis Ktistakis, President, Peeter Roosma, Darian Pavli, \u00dana N\u00ed Raifeartaigh, Mateja
\u0110urovi\u0107, Vasilka Sancin, judges, Mira Raycheva, ad hoc judge, and Milan Bla\u0161ko, Section Registrar, Having regard to: the application (no. 6580/22) against the Republic of Bulgaria
lodged with the Court under Article 34 of the Convention for the Protection of Human Rights and Fundamental Freedoms (\"the Convention\") by an association with a registered office in Bulgaria, Green
Alliance (\"the applicant association\" or \"the association\"), on 19 January 2022; the decision to give the Bulgarian Government (\"the Government\") notice of the application;  ...    the decision
of the President of the Section to exempt Diana Kovatcheva, the judge elected in respect of Bulgaria, from sitting in this case and his ensuing decision to appoint Mira Raycheva to sit as ad hoc judge
in the case; Having deliberated in private on 27 January 2026,\n\nDelivers the following judgment, which was adopted on that date:  ...    1. Under regulations issued in 2008 and amended in 2018,
Bulgaria's State Agency for National Security (\"the Agency\")  ...    2. The main issues in the case are (a) whether the association can claim to be a victim of interference with its rights  ...
no. 251-B; Wieser and Bicos Beteiligungen GmbH v. Austria, no. 74336/01, \u00a7 45, ECHR 2007-IV; Bernh Larsen  ...    Soci\u00e9t\u00e9 Colas Est and Others v. France, no. 37971/97, \u00a7 41, ECHR
2002-III; Buck v. Germany, no. 41604/98, \u00a7 31, ECH"], "published_date": null, "score": null}, {"title": "MORAWIEC v. POLAND - 46238/20 (Art 6 s 1 (civil and criminal) - Tribunal established by
law - Lifting of judge's immunity from prosecution and suspension from judicial duties by Supreme Court's Disciplinary Chamber : Preliminary objections partially dismissed : First Section) [2026] ECHR
28 (05 February 2026)", "url": "https://www.bailii.org/eu/cases/ECHR/2026/28.html", "snippet": "MORAWIEC v. POLAND - 46238/20 (Art 6 s 1 (civil and criminal) - Tribunal established by law - Lifting of
judge's immunity from prosecution and suspension from judicial duties by Supreme Court's Disciplinary Chamber : Preliminary objections partially dismissed : First Section) [2026] ECHR 28 (05 February
2026)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> MORAWIEC v. POLAND - 46238/20 (Art 6 s 1 (civil and criminal) - Tribunal
establis", "highlights": ["[2026] ECHR 28 (05 February 2026) # European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human Rights>> MORAWIEC v. POLAND - 46238/20
(Art 6 s 1 (civil and criminal) - Tribunal established by law - Lifting of judge's immunity from  ...    partially dismissed : First Section) [2026] ECHR 28 (05 February 2026) URL:
https://www.bailii.org/eu/cases/ECHR/2026/28.html Cite as: [2026] ECHR 28 --- | [Home] [Databases] [World Law] [Multidatabase Search] [Help] [Feedback] [DONATE] |  ...    [New search] [Contents list]
[Help]\n\n---\n\nFIRST SECTION CASE OF MORAWIEC v. POLAND\n\n(Application no. 46238/20)\n\nJUDGMENT Art 6 \u00a7 1 (civil and criminal) \u2022 Tribunal established by law \u2022 Lifting of judge's
immunity from prosecution and suspension from judicial duties by Supreme Court's Disciplinary Chamber \u2022 Art 34 \u2022 In specific case-circumstances,  ...    Case distinguished from Tuleya v.
Poland in that respect \u2022 Art 6 \u00a7 1 applicable under its civil limb to the applicant's  ...    Art 10 \u2022 Freedom of expression \u2022 Art 34 \u2022 Victim status \u2022 Actions aimed at
lifting the applicant's judicial immunity prompted by her views and criticisms, publicly expressed in her professional capacity, of the legislative reforms affecting the judiciary \u2022 Lack of
proper safeguards against arbitrariness \u2022 Interference not \"in accordance with the law\" and not pursuing any legitimate aim Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n5
February 2026 This judgment will become final in the circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In the case of Morawiec v. Poland, The
European Court of Human Rights (First Section), sitting as a Chamber composed of: Ivana Jeli\u0107, President, Erik Wennerstr\u00f6m, Raffaele Sabato, Fr\u00e9d\u00e9ric Krenc, Davor
Deren\u010dinovi\u0107, Alain Chablais, Anna Adamska-Gallant, judges, and Ilse Freiwirth, Section Registrar, Having regard to: the application (no. 46238/20) against the Republic of Poland lodged with
the Court under Article 34 of the  ...    Beata Morawiec (\"the applicant\"), on 20 October 2020; the decision to give notice to the Polish Government (\"the Government\") of the complaints under
Article 6 \u00a7 1, Article  ...    the parties' observations;\n\nHaving deliberated in private on 13 January 2026, Delivers the following judgment, which was adopted on that date:\n\nINTRODUCTION 1.
The case concerns a decision of the Disciplinary Chamber of the Supreme Court to lift the applicant's immunity from prosecution and suspend her from judicial duties. The applicant submitted that the
Disciplinary Chamber had not  ...    the Disciplinary Chamber's decision had amounted to a breach of her right to respect for her private life and her right  ...    On 12 October 2020 the Disciplinary
Chamber operating within the Supreme Court building - an entity which is not and  ...    2. The Court's assessment  27. The Court refers to the general principles concerning the application of the
...    39325/20, \u00a7 47, 3 February 2022). It reiterates that in assessing the severity of a violation, both the  ...    (ibid., see also Gagliano Giorgi v. Italy, no. 23563/07, \u00a7 55, ECHR"],
"published_date": null, "score": null}, {"title": "RAMISHVILI v. GEORGIA - 4100/24 (Article 8 - Right to respect for private and family life : Fourth Section) [2026] ECHR 21 (03 February 2026)",
"url": "http://beta.bailii.org/eu/cases/ECHR/2026/21.html", "snippet": "RAMISHVILI v. GEORGIA - 4100/24 (Article 8 - Right to respect for private and family life : Fourth Section) [2026] ECHR 21 (03
February 2026)\n\nRAMISHVILI v. GEORGIA - 4100/24 (Article 8 - Right to respect for private and family life : Fourth Section) [2026] ECHR 21 (03 February 2026)\nBAILII\nBritish\nand Irish Legal
Information Institute\nFreely Available British and Irish Public Legal Information\n[Home]\n[Databases]\n[World Law]\n[Multidatabase Search]\n[Help]\n[Feedback]\n# European Court of Human Righ",
"highlights": ["Right to respect for private and family life : Fourth Section) [2026] ECHR 21 (03 February 2026)  ...    RAMISHVILI v. GEORGIA - 4100/24 (Article 8 - Right to respect for private and
family life : Fourth Section) [2026] ECHR 21 (03 February 2026) URL: *http://www.bailii.org/eu/cases/ECHR/2026/21.html*\nCite as:\n[2026] ECHR 21\n[New search] [Contents list]\n[Help]\n\u00a0\nFOURTH
SECTION\nCASE OF RAMISHVILI v. GEORGIA (Application no. 4100/24)\n\u00a0\n\u00a0\nJUDGMENT Art 8 \u2022 Private life \u2022 Unsuccessful civil defamation claim in respect of statements made by a
prominent  ...    of being an informer and provocateur who fed information to the State Security Services \u2022 Impugned statements  ...    professional and social environments \u2022 Art 8
applicable \u2022 Domestic courts' failure to establish a factual basis for the accusations \u2022 Unattainable burden of proof imposed on the applicant to rebut the accusations \u2022 Failure to
strike fair balance between competing interests \u00a0\nPrepared by the Registry. Does not bind the Court.\n\u00a0\nSTRASBOURG\n3 February 2026\n\u00a0\n\u00a0 *This judgment will become final in the
circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision.* \u00a0\nIn the case of Ramishvili v. Georgia, The European Court of Human Rights (Fourth
Section), sitting as a Chamber composed of:\n Jolien Schukking*, President*, Lado Chanturia,\n Lorraine Schembri Orland,\n Anja Seibert-Fohr,\n Ana Maria Guerra Martins,\n Anne Louise Bormann,
Sebastian R\u0103dule\u0163u*, judges*,\nand Simeon Petrovski, *Deputy Section Registrar*,\nHaving regard to: the application (no.\u00a04100/24) against Georgia lodged with the Court under
Article\u00a034 of the Convention for the Protection of Human Rights and Fundamental Freedoms (\"the Convention\") by a Georgian national, Mr\u00a0Mikheil Ramishvili (\"the applicant\"), on 7 February
2024; the decision to give notice of the application to the Georgian Government (\"the Government\"); the parties' observations;\nHaving deliberated in private on 13 January 2026, Delivers the
following judgment, which was adopted on that date:\nINTRODUCTION 1.\u00a0\u00a0The case concerns civil defamation proceedings brought by the applicant, a publicly known defence counsel, in respect of
several statements made by Father I., a prominent clergyman of the Georgian Orthodox Church, during a televised interview. The applicant complained under Article\u00a08 of the Convention that the
domestic courts  ...    8.\u00a0\u00a0On 11 December 2018 the Tbilisi City Court ruled in the applicant's favour, ordering Father I. to  ...    2.\u00a0\u00a0\u00a0\u00a0 The Court's
assessment\n(a)\u00a0\u00a0\u00a0 General principles 29.\u00a0\u00a0The relevant general principles were summarised in *Jishkariani v.\u00a0Georgia* (cited above, \u00a7\u00a7 41-46; see also *Couderc
and Hachette Filipacchi Associ\u00e9s v. France* [GC], no. 40454/07, \u00a7\u00a7\u00a082-91, ECHR 2015  ...    30.\u00a0\u00a0The Court observes that in cases such as the present one, what is in
issue is not"], "published_date": null, "score": null}, {"title": "", "url":
"https://hudoc.echr.coe.int/app/conversion/docx/pdf?filename=CASE+OF+GREEN+v.+THE+UNITED+KINGDOM.pdf&id=001-242635&library=ECHR", "snippet": "FOURTH SECTION\nCASE OF GREEN v. THE UNITED
KINGDOM\n(Application no. 22077/19)\nJUDGMENT\nArt 8 \u2022 Positive obligations \u2022 Private life \u2022 Use of parliamentary privilege by a Member of \nParliament to disclose on the floor of the
House the applicant\u2019s identity subject to an interim \nprivacy injunction pending trial \u2022 Disclosure with serious consequences for the applicant \u2022 \nFirst and foremost for national
parliaments to assess the need to restrict their Members\u2019 \nconduct \u2022 Rule on parliamentary privile", "highlights": ["for national parliaments to assess the need to restrict their
Members\u2019 conduct \u2022 Rule on parliamentary privilege not entirely devoid of ex ante and ex post controls \u2022 Parliamentary privilege, in the majority of Member States, afforded absolute
protection from external legal actions to statements made by parliamentarians in Parliament or in the exercise of their parliamentary duties \u2022 Wide margin of appreciation not exceeded \u2022 Lack
of sufficiently strong reasons to justify requiring the introduction of further ex ante and ex post controls to prevent Members of Parliament from revealing information subject to privacy injunctions
\u2022 Respondent State to regularly review the need for appropriate controls, given serious impact of disclosure of information subject to privacy injunctions Prepared by the Registry. Does not bind
the Court.\nSTRASBOURG\n8 April 2025\nFINAL\n08/07/2025 This judgment has become final under Article 44 \u00a7 2 of the Convention. \nIt may be subject to editorial revision. GREEN v. THE UNITED
KINGDOM JUDGMENT\n1\nIn the case of Green v. the United Kingdom, The European Court of Human Rights (Fourth Section), sitting as a \nChamber composed of:\nLado Chanturia, President, Tim
Eicke,\nLorraine Schembri Orland,\nAna Maria Guerra Martins,\nAnne Louise Bormann,\nSebastian R\u0103dule\u0163u, Andr\u00e1s Jakab, judges,\nand Simeon Petrovski, Deputy Section Registrar,\nHaving
regard to: the application (no. 22077/19) against the United Kingdom of Great Britain and Northern Ireland lodged with the Court under Article 34 of the Convention for the Protection of Human Rights
and Fundamental Freedoms (\u201cthe Convention\u201d) by a British national, Mr Philip Nigel Ross Green (\u201cthe \napplicant\u201d), on 23 April 2019; the decision to give notice to the United
Kingdom Government (\u201cthe Government\u201d) of the complaints concerning Article 6, Article 8 (in respect of the regulation of parliamentary privilege) and Article 13 of the Convention and to
declare inadmissible the remainder of the application;\nthe parties\u2019 observations; Having deliberated in private on 4 March 2025,\nDelivers the following judgment, which was adopted on that date:
INTRODUCTION\n1. Invoking parliamentary privilege, a Member of the House of Lords made a personal statement in the chamber identifying the applicant as the subject of an anonymised newspaper article
even though the Court of Appeal had granted an interim injunction and anonymity orders to prevent the \npublication of his identity. 2. Before the Court the applicant relies on Articles 6 \u00a7 1, 8
and 13 of the \nConvention.\nTHE FACTS 3. The applicant is a British national who was born in 1952 and lives in Monaco. He is represented before the Court by Mr I.R. Burton of \nBCL Solicitors in
London.  ...    5. The facts of the case may be summarised as follows.\nGREEN v. THE UNITED KINGDOM JUDGMENT\n2  ...    Lord Hain had failed to declar  parliamentary privilege and making
recommendations. In its Report on Parliamentary Privilege 1999 (Session 1998-99, HL 43, HC 214), it explained \n[references omitted]:  ...    1689. Members are not exposed to any civil or criminal
liabilities in respect of what  ...    a Parliamentary Privileges Act be enacted to codify parliamentary privilege  ...    37. A Joint Committee of both Houses of Parliament on Privacy and Injunctions
was appointed in 2011. The Committee published its report in March 2012 (Session 2010-12, HL 273, HC 1443). It noted that there had  ...    \u201c214. Article IX [of the Bill of Rights] means that it
would not be constitutionally  ...    anonymity cannot be regained: the effect of the anonymity order is set at nought.  ...    \u201c230. We regard freedom of speech in Parliament as a fundamental
constitutional principle. Over the last couple of years a few members have revealed in Parliament  ...    GREEN v. THE UNITED KINGDOM JUDGMENT\n9\n231. If the revelation of injuncted information
becomes more commonplace, if  ...    39. In April 2012 the Government published a Green Paper on  ...    Paper. The Committee published its Report on Parliamentary Privilege on  ...    safeguard the
effective functioning of Parliament. It is agreed that immunity applies to that core"], "published_date": null, "score": null}, {"title": "O.H. AND OTHERS v. SERBIA - 57185/17 (Art 4 P4 - Prohibition
of collective expulsion of aliens - Arbitrary removal by police of irregular migrants from Serbia to Bulgarian side of the border : Remainder inadmissible : Third Section) [2026] ECHR 20 (03 February
2026)", "url": "http://knyvet.bailii.org/eu/cases/ECHR/2026/20.html", "snippet": "O.H. AND OTHERS v. SERBIA - 57185/17 (Art 4 P4 - Prohibition of collective expulsion of aliens - Arbitrary removal by
police of irregular migrants from Serbia to Bulgarian side of the border : Remainder inadmissible : Third Section) [2026] ECHR 20 (03 February 2026)\n\n# European Court of Human Rights\n\n---\n\nYou
are here: BAILII>> Databases>> European Court of Human Rights>> O.H. AND OTHERS v. SERBIA - 57185/17 (Art 4 P4 - Prohibition of collective expulsion of aliens - Arbitrary removal by police ",
"highlights": ["ECHR 20 (03 February 2026) # European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human Rights>> O.H. AND OTHERS v. SERBIA - 57185/17 (Art 4 P4 -
Prohibition of collective expulsion of aliens - Arbitrary removal by police of irregular migrants from Serbia to Bulgarian side of the border : Remainder inadmissible : Third Section) [2026] ECHR 20
(03 February 2026) URL: https://www.bailii.org/eu/cases/ECHR/2026/20.html Cite as: [2026] ECHR 20  ...    | [Home] [Databases] [World Law] [Multidatabase Search] [Help] [Feedback] [DONATE] |  ...
[New search] [Contents list] [Help]\n\n---\n\nTHIRD SECTION CASE OF O.H. AND OTHERS v. SERBIA\n\n(Application no. 57185/17)\n\nJUDGMENT Art 4 P4 \u2022 Prohibition of collective expulsion of aliens
\u2022 Arbitrary removal by police of irregular migrants from Serbia to Bulgarian side of the border despite domestic court's acknowledgment of their asylum claims, ordering the  ...    procedure in
Bulgaria Art 5 \u00a7 1 \u2022 Unlawful and arbitrary detention from the discontinuation of the misdemeanour  ...    Applicants deprived of their liberty in a deceptive way Art 5 \u00a7 2 \u2022
Information in language understood \u2022 Authorities engaged the services of an interpreter at the police station following the applicants' arrest Art 5 \u00a7 4 \u2022 Police's failure to provide
applicants with legal assistance deprived them of the possibility of challenging the lawfulness of their detention Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n3 February 2026
This judgment will become final in the circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In the case of O.H. and Others v. Serbia, The European
Court of Human Rights (Third Section), sitting as a Chamber composed of: Ioannis Ktistakis, President, Peeter Roosma, L\u0259tif H\u00fcseynov, Darian Pavli, Mateja \u0110urovi\u0107, Can\u00f2lic
Mingorance Cairat, Vasilka Sancin, judges, and Milan Bla\u0161ko, Section Registrar, Having regard to: the application (no. 57185/17) against the Republic of Serbia lodged with the Court under Article
34 of the Convention for the Protection of Human Rights and Fundamental Freedoms (\"the Convention\") by 17 Afghan nationals on 1 August 2017 (\"the applicants\" - see appended list); the decision to
give notice of the application to the Serbian Government (\"the Government\"); the decision not to have the applicants' names disclosed;\n\nthe parties' observations; Having deliberated in private on
16 December 2025,\n\nDelivers the following judgment, which was adopted on that date:  ...    1. The case concerns the removal of migrants from Afghanistan to the Republic of Bulgaria after they had
expressed their intention to seek asylum in Serbia, and a lack of effective domestic remedies against their removal. It also concerns the lawfulness and conditions of their detention prior to their
removal.  ...    2. A list of the applicants, together with their personal details, is set out in the appended table. The President  ...    5. In the early hours of 3 February 2017, at approximately
12.15 a.m., Serbian authorities arrested the applicants near  ...    10. According to the information provided by the applicants, the police asked a Farsi interpreter from the Belgrade Centre for
Human Rights (Beogradski centar za ljudska prava - hereinafter \"the BCHR\") to go to Gradina Police Station  ...    35. The Constitutional Court found no violation of Article 27 \u00a7 1 of the
Constitution and ruled that the deprivation of  ...    40. In a submission dated 9 June 2025, the applicants' representative provided the Court with the second applicant's  ...    109. In that
connection, the Court has previously found violations of Article 3 of the Convention on account of the  ...    111. Therefore, the present case, differs from the factual background of the above-
mentioned judgments primarily  ...    present case (see Labita v. Italy [GC], no. 26772/95, \u00a7 120, ECHR 2000-IV), the Court finds that"], "published_date": null, "score": null}, {"title": "",
"url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Judgment+Green+Alliance+v.+Bulgaria+-+Regulations+in+Bulgaria+on+use+of+informers+did+not+meet+minimum+Convention+safeguards.pdf&id=003-
8461626-11986400&library=ECHR", "snippet": "issued by the Registrar of the Court\nECHR 043 (2026)\n17.02.2026\nRegulations in Bulgaria on use of informers did not meet minimum Convention
\nsafeguards\nIn today\u2019s Chamber judgment1 in the case of Green Alliance v. Bulgaria (application no. 6580/22) the \nEuropean Court of Human Rights held, unanimously, that there had been a
violation of Article 8 (right \nto respect for private and family life) of the European Convention on Human Rights.\nThe case concerned regulations issued in 2008 and amended i", "highlights":
["issued by the Registrar of the Court\nECHR 043 (2026)\n17.02.2026  ...    In today\u2019s Chamber judgment1 in the case of Green Alliance v. Bulgaria (application no. 6580/22) the European Court of
Human Rights held, unanimously, that there had been a violation of Article 8 (right  ...    \u043f\u0440\u0438\u043a\u0440\u0438\u0442\u0438\u0435), into private entities or as members of a
\u201cliberal profession\u201d. Such agents conceal that  ...    In the present judgment, the Court found that the regulations governing the use of \u201cagents on cover\u201d  ...    to their
unlawful or unjustified use. A legal summary of this case will be available in the Court\u2019s database HUDOC (link)\nPrincipal facts  ...    (\u201cthe Agency\u201d) can infiltrate \u201cagents on
cover\u201d (\u0441\u043b\u0443\u0436\u0438\u0442\u0435\u043b\u0438 \u043d\u0430 \u043f\u0440\u0438\u043a\u0440\u0438\u0442\u0438\u0435) into private entities or as  ...    In October 2018 Green
Alliance sought judicial review of the regulations as amended in 2018, arguing  ...    and disproportionate interferences with rights protected under Article 8 of the Convention. On 19 July 2021 a
five-judge panel of the Supreme Administrative Court found, among other things, that the work  ...    1. Under Articles 43 and 44 of the Convention, this Chamber judgment is not final. During the
three-month period following its delivery, any party may request that the case be referred to the Grand Chamber of the Court. If such a request is made, a panel of five judges considers whether the
case deserves further examination. In that event, the Grand Chamber will hear the case and deliver a final judgment. If the referral request is refused, the Chamber judgment will become final on that
day. Once a judgment becomes final, it is transmitted to the Committee of Ministers of the Council of Europe for supervision of its execution. Further information about the execution process can be
found here: www.coe.int/t/dghl/monitoring/execution.\n2  ...    in various respects, especially in terms of safeguards, and thus enabled the Agency to deploy such agents in an arbitrary and abusive
manner. The application was lodged with the European Court of Human Rights on 19 January 2022. Judgment was given by a Chamber of seven judges, composed as follows:\nIoannis Ktistakis (Greece),
President, Peeter Roosma (Estonia),\nDarian Pavli (Albania),\n\u00dana N\u00ed Raifeartaigh (Ireland),\nMateja \u0110urovi\u0107 (Serbia), Mira Raycheva (Bulgaria),\nVasilka Sancin (Slovenia),\nand
also Milan Bla\u0161ko, Section Registrar.\nDecision of the Court  ...    The Court went on to hold that the regulations governing the use of \u201cagents on cover\u201d fell short of the  ...
There had therefore been a violation of Article 8 of the Convention.\nJust satisfaction (Article 41) The Court held that the finding of a violation of Article 8 of the Convention amounted to
sufficient just satisfaction in respect of any non-pecuniary damage suffered by Green Alliance. The judgment is available only in English. This press release is a document produced by the Registry. It
does not bind the Court. Decisions, judgments and further information about the Court can be found on www.echr.coe.int. Follow the Court on Bluesky @echr.coe.int, X ECHR_CEDH, LinkedIn, and YouTube.
Contact ECHRPress to subscribe to the press-release mailing list. Where can the Court\u2019s press releases be found? HUDOC - Press collection\nPress contacts echrpress@echr.coe.int | tel.: +33 3 90
21 42 08  ...    Tracey Turner-Tretz (tel: + 33 3 88 41 35 30)\nDenis Lambert (tel: + 33 3 90 21 41 09) Inci Ertekin (tel: + 33 3 90 21 55 30)\nJane Swift (tel: + 33 3 88 41 29 04) The European Court
of Human Rights was set up in Strasbourg by the Council of Europe member States in 1959 to deal"], "published_date": null, "score": null}, {"title": "SIMONCINI v. SAN MARINO - 14396/24 (Article 6 -
Right to a fair trial : Fifth Section) [2026] ECHR 34 (19 February 2026)", "url": "https://www.bailii.org/eu/cases/ECHR/2026/34.html", "snippet": "SIMONCINI v. SAN MARINO - 14396/24 (Article 6 - Right
to a fair trial : Fifth Section) [2026] ECHR 34 (19 February 2026)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> SIMONCINI v. SAN
MARINO - 14396/24 (Article 6 - Right to a fair trial : Fifth Section) [2026] ECHR 34 (19 February 2026) URL: https://www.bailii.org/eu/cases/ECHR/2026/34.html Cite as: [2026] ECHR 34\n\n---\n\n|
[Home] [Databases] [World Law] [Multidatabase Search] [Help] [F", "highlights": ["here: BAILII>> Databases>> European Court of Human Rights>> SIMONCINI v. SAN MARINO - 14396/24 (Article 6 - Right to a
fair trial : Fifth Section) [2026] ECHR 34 (19 February 2026) URL: https://www.bailii.org/eu/cases/ECHR/2026/34.html Cite as: [2026] ECHR 34  ...    | [Home] [Databases] [World Law] [Multidatabase
Search] [Help] [Feedback] [DONATE] |  ...    [New search] [Contents list] [Help]\n\n---\n\nFIFTH SECTION CASE OF SIMONCINI v. SAN MARINO\n\n(Application no. 14396/24)\n\nJUDGMENT Art 6 \u00a7 1
(civil) \u2022 Fair hearing \u2022 Annulment ex officio by the Judicial Council (CGP) of the applicant's appointment to  ...    right to private life to a very significant degree \u2022 Domestic
courts' failure to acknowledge that right or balance it appropriately against other alleged competing interests \u2022 Lawfulness requirement not met \u2022 Absence of relevant and sufficient reasons
justifying the necessity of the impugned measure in a democratic society Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n19 February 2026 This judgment will become final in the
circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In the case of Simoncini v. San Marino, The European Court of Human Rights (Fifth Section),
sitting as a Chamber composed of: Kate\u0159ina \u0160im\u00e1\u010dkov\u00e1, President, Mar\u00eda El\u00f3segui, Georgios A. Serghides, Gilberto Felici, Andreas Z\u00fcnd, Diana S\u00e2rcu,
S\u00e9bastien Biancheri, judges, and Victor Soloveytchik, Section Registrar, Having regard to: the application (no. 14396/24) against the Republic of San Marino lodged with the Court under Article 34
of the Convention for the Protection of Human Rights and Fundamental Freedoms (\"the Convention\") by a San Marinese national, Mr Massimiliano Simoncini (\"the applicant\"), on 9 May 2024; the
decision to give notice to the San Marinese Government (\"the Government\") of the complaints concerning Article 6  ...    the decision to reject the Government's request for the recusal of Mr
Gilberto Felici, the judge elected in respect of San Marino, in September 2025 (Rule 28 \u00a7\u00a7 3 and 4 of the Rules of Court); Having deliberated in private on 27 January 2026,\n\nDelivers the
following judgment, which was adopted on that date:  ...    1. The application concerns proceedings related to the annulment of the applicant's appointment to Commissario della Legge (a judicial organ
in the ordinary courts of first instance). It raises complaints under Articles 6 and 8 of the  ...    2. The applicant was born in 1963 and lives in Montegiardino. He was represented by Mr E. Santi, a
lawyer practising in  ...    4. The facts of the case may be summarised as follows.\n\nThe CIRCUMSTANCES OF THE CASE\n\nA. Background to the case  ...    June 2021. On 2 December 2021 the FCLM
dismissed the applicant's preliminary objection concerning the lack of  ...    as amended by Constitutional Law no. 2/2020. The applicant's request concerning a precautionary suspension of the  ...
36. Both interlocutory decisions were confirmed on appeal on 20 June 2022.\n\n1. First-instance judgment 37. By a judgment of 25 January 2023 the FCLM"], "published_date": null, "score": null}]
```

```json
{
  "query": "ECHR \"Grand Chamber Judgment\" 2026 delivery date"
}
```

### 📋 Result

```
{"query": "ECHR \"Grand Chamber Judgment\" 2026 delivery date", "results": [{"title": "Forthcoming judgments and decisions 17-19.03.2026 - HUDOC", "url": "https://hudoc.echr.coe.int/eng-press",
"snippet": "\\t\\t\\n\\t\\t\\n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\
t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t \\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\
\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t
\\t\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t", "api_data": null, "hint": null},
{"title": "HUDOC - European Court of Human Rights", "url": "https://hudoc.echr.coe.int/eng", "snippet": "\\t\\t\\n\\t\\t\\n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\
\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t
\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t
\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\
t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t", "api_data": null, "hint": null}, {"title": "Delivery of judgments - ECHR Hearings - ECHR -
ECHR / CEDH", "url": "https://www.echr.coe.int/delivery-of-judgments", "snippet": null, "api_data": null, "hint": null}, {"title": "ECHR - Homepage of the European Court of Human Rights - ECHR - ECHR
/ CEDH", "url": "https://www.echr.coe.int/", "snippet": null, "api_data": null, "hint": null}, {"title": "issued by the Registrar of the Court ECHR 004 (2026) 08.01.2026", "url":
"https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-8423564-11921102&filename=Judgments+and+decisions+of+08.01.2026.pdf", "snippet": null, "api_data": null, "hint": null}, {"title":
"Calendar of hearings - ECHR Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/calendar-of-hearings", "snippet": null, "api_data": null, "hint": null}, {"title": "All webcasts - ECHR
Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/all-webcasts", "snippet": null, "api_data": null, "hint": null}, {"title": "The Grand Chamber \uf0d8 When does the Grand Chamber hear a
case?", "url": "https://www.echr.coe.int/documents/d/echr/faq_gc_eng", "snippet": null, "api_data": null, "hint": null}, {"title": "European Court of Human Rights - Wikipedia", "url":
"https://en.wikipedia.org/wiki/European_Court_of_Human_Rights", "snippet": "The European Court of Human Rights (ECtHR), also known as the Strasbourg Court, is an international court of the Council of
Europe which interprets the European Convention on Human Rights (ECHR). The court hears applications alleging that a contracting state has breached one or more of the human rights enumerated in the
convention or its optional protocols to which a member state is a party. The court is based in Strasbourg, France.\nThe court was established in 1959 and decided its first case in", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"European Court of Human Rights\", \"url\": \"https://en.wikipedia.org/wiki/European_Court_of_Human_Rights\", \"extract\": \"The European Court of
Human Rights (ECtHR), also known as the Strasbourg Court, is an international court of the Council of Europe which interprets the European Convention on Human Rights (ECHR). The court hears
applications alleging that a contracting state has breached one or more of the human rights enumerated in the convention or its optional protocols to which a member state is a party. The court is
based in Strasbourg, France.\\nThe court was established in 1959 and decided its first case in 1960 in Lawless v. Ireland. An application can be lodged by an individual, a group of individuals, or one
or more of the other contracting states. Aside from judgments, the court can also issue advisory opinions. The convention was adopted within the context of the Council of Europe, and all of its 46
member states are contracting parties to the convention. The court's primary means of judicial interpretation is the living instrument doctrine, meaning that the Convention is interpreted in light of
present-day conditions.\\nInternational law scholars consider the ECtHR to be the most effective international human rights court in the world. Nevertheless, the court has faced challenges with
verdicts not implemented by the contracting parties.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Case Law Database | European Union Agency for Fundamental Rights", "url":
"https://fra.europa.eu/en/case-law-database", "snippet": "Case Law Database\nHere you can find case law of the Court of Justice of the European Union (CJEU) and the European Court of Human Rights
(ECtHR) with direct references to the EU Charter of Fundamental Rights, as well as a selection of national case law with direct references to the Charter from all EU Member States.\nFilter by:\n1849
case law references found\n- Subtitle:European Commission v HungaryDeciding body type:Court of Justice of the European UnionDeciding body:Court (Grand Chamber)ECLI (Eu", "api_data": null, "hint":
null}]}
```

## 💬 Response

Good - I can see the ECHR has been delivering regular Chamber judgments but I need to specifically check for Grand Chamber Judgments. Let me search more specifically for the historical frequency of Grand Chamber Judgments.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "ECHR Grand Chamber judgment 2025 2026 how many per year"
}
```

### 📋 Result

```
{"query": "ECHR Grand Chamber judgment 2025 2026 how many per year", "results": [{"title": "HUDOC - European Court of Human Rights", "url": "https://hudoc.echr.coe.int/", "snippet": "\\t\\t\\n\\t\\t\\
n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\
\t\\t\\n\\t\\t\\t\\t \\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t
\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\
t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t", "api_data": null, "hint": null}, {"title": "Key Cases - 2025 - ECHR-
KS", "url": "https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng", "snippet": null, "api_data": null, "hint": null}, {"title": "All webcasts - ECHR Hearings - ECHR - ECHR / CEDH", "url":
"https://www.echr.coe.int/all-webcasts", "snippet": null, "api_data": null, "hint": null}, {"title": "European Court of Human Rights - Wikipedia", "url":
"https://en.wikipedia.org/wiki/European_Court_of_Human_Rights", "snippet": "The European Court of Human Rights (ECtHR), also known as the Strasbourg Court, is an international court of the Council of
Europe which interprets the European Convention on Human Rights (ECHR). The court hears applications alleging that a contracting state has breached one or more of the human rights enumerated in the
convention or its optional protocols to which a member state is a party. The court is based in Strasbourg, France.\nThe court was established in 1959 and decided its first case in", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"European Court of Human Rights\", \"url\": \"https://en.wikipedia.org/wiki/European_Court_of_Human_Rights\", \"extract\": \"The European Court of
Human Rights (ECtHR), also known as the Strasbourg Court, is an international court of the Council of Europe which interprets the European Convention on Human Rights (ECHR). The court hears
applications alleging that a contracting state has breached one or more of the human rights enumerated in the convention or its optional protocols to which a member state is a party. The court is
based in Strasbourg, France.\\nThe court was established in 1959 and decided its first case in 1960 in Lawless v. Ireland. An application can be lodged by an individual, a group of individuals, or one
or more of the other contracting states. Aside from judgments, the court can also issue advisory opinions. The convention was adopted within the context of the Council of Europe, and all of its 46
member states are contracting parties to the convention. The court's primary means of judicial interpretation is the living instrument doctrine, meaning that the Convention is interpreted in light of
present-day conditions.\\nInternational law scholars consider the ECtHR to be the most effective international human rights court in the world. Nevertheless, the court has faced challenges with
verdicts not implemented by the contracting parties.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Delivery of judgments - ECHR Hearings - ECHR - ECHR / CEDH", "url":
"https://www.echr.coe.int/delivery-of-judgments", "snippet": null, "api_data": null, "hint": null}, {"title": "ECHR - Homepage of the European Court of Human Rights - ECHR - ECHR / CEDH", "url":
"https://www.echr.coe.int/home-prd-", "snippet": null, "api_data": null, "hint": null}, {"title": "Ukraine and the Netherlands v. Russia (Applications nos. 8019/16, 43800/14, 28525/20 and 11055/22) |
Refworld", "url": "https://www.refworld.org/jurisprudence/caselaw/echr/2025/en/150269", "snippet": null, "api_data": null, "hint": null}, {"title": "Case Law Database | European Union Agency for
Fundamental Rights", "url": "https://fra.europa.eu/en/case-law-database", "snippet": "Case Law Database\nHere you can find case law of the Court of Justice of the European Union (CJEU) and the
European Court of Human Rights (ECtHR) with direct references to the EU Charter of Fundamental Rights, as well as a selection of national case law with direct references to the Charter from all EU
Member States.\nFilter by:\n1849 case law references found\n- Subtitle:European Commission v HungaryDeciding body type:Court of Justice of the European UnionDeciding body:Court (Grand Chamber)ECLI
(Eu", "api_data": null, "hint": null}, {"title": "Cases pending before the Grand Chamber - ECHR Hearings - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/cases-pending-before-the-grand-
chamber", "snippet": null, "api_data": null, "hint": null}, {"title": "Composition of the ECHR - Grand Chamber", "url": "https://www.echr.coe.int/grand-chamber", "snippet": null, "api_data": null,
"hint": null}]}
```

```json
{
  "query": "ECHR Grand Chamber judgment delivered 2025 2026",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "Landmark for Justice: Key Legal Takeaways from the ECHR Grand ...", "url": "https://queritius.com/landmark-for-justice-key-legal-takeaways-from-the-echr-grand-chambers-judgment-in-ukraine-
and-the-netherlands-v-russia/", "snippet": "Landmark for Justice: Key Legal Takeaways from the ECHR Grand Chamber\u2019s Judgment in Ukraine and the Netherlands v. Russia - Queritius\n\n# Landmark for
Justice: Key Legal Takeaways from the ECHR Grand Chamber\u2019s Judgment in Ukraine and the Netherlands v. Russia\n\n12. 08. 2025\n\nOn 9 July 2025, the Grand Chamber of the European Court of Human
Rights delivered its landmark judgement in Ukraine and the Netherlands v. Russia (Applications nos. 8019/16, 43800/14, 28525/20 & 11055/22), consolidating four i", "highlights": ["Landmark for
Justice: Key Legal Takeaways from the ECHR Grand Chamber\u2019s Judgment in Ukraine and the Netherlands v.  ...    12. 08. 2025 On 9 July 2025, the Grand Chamber of the European Court of Human Rights
delivered its landmark judgement in Ukraine and the Netherlands v. Russia (Applications nos. 8019/16, 43800/14, 28525/20 & 11055/22), consolidating four inter-State applications concerning
Russia\u2019s annexation of Crimea (since February 2014), the intervention in Donetsk and Luhansk (since April 2014), the downing of MH17 flight (in July 2014), and Russia\u2019s full-scale invasion
of Ukraine (since February 2022). This judgment is remarkable in many ways: from its essence and importance to the number of parties intervened. Given its extensive length and argumentation, it is
hardly possible to summarise all the conclusions and findings in one (or even several) posts. So please see below key points which are, in our view, worth attention. 1. Background and Procedural
Issues\n2. Contact 1. In the spirit of adversarial procedure, the Court engaged in correspondence with the respondent state, although with no significant result. Apart from the short response of 5
March 2022, with \u201ca number of bare assertions not supported by any evidence\u201d, Russia did not provide any further submissions. The Court\u2019s approach, however, shows that the fundamental
principle of equality of arms shall be followed in any dispute, and thus, will be followed in future  ...    2. The Court mentioned several international organs and organisations that condemned the
Russian aggression in the strongest terms. Notably, the Court highlighted the Council of Europe\u2019s achievements in this field, specifically the establishment of the Register of Damage Caused by
the Aggression of the Russian Federation against Ukraine and the preparation of draft legal instruments necessary to create a Special Tribunal for the Crime of Aggression against Ukraine. By doing so,
the Court demonstrated that its decision is not a standalone action but rather part of the  ...    1. Given the character and purpose of Russia\u2019s invasion of Ukraine since 24 February 2022, the
Court distinguished the present case from Georgia v Russia (II) and found that the former \u201cexercised, through its de jure and de facto armed  ...    2. The Court confirmed that the Russian
Federation\u2019s effective control over the areas of the so-called Donetsk People\u2019s Republic (\u201cDPR\u201d) and Luhansk People\u2019s Republic (\u201cLPR\u201d) continued up until 16
September 2022. The initial existence of such control by the Russian Federation was established to have taken place since 11 May 2014 through deployment of  ...    occupied territories. (see paras.
694 and 905 of the Grand Chamber decision of 30 November 2022 in the case of Ukraine and Netherlands v Russia (Applications Nos. 8019/16, 43800/14 and 28525/20)). 3. Following its previous judgements
(Pivkina and Others v Russia; Ukraine v Russia (re Crimea), the Court found its temporal jurisdiction to exist \u201cno further than 16 September 2022\u201d. As regards the facts that occurred later
on, they may have been taken by the Court into account in the \u201coverall context of the case\u201d, that is, for the assessment of the  ...    1. As the violations of the Convention took place at
the time of international armed conflict, the Court could not  ...    claimed to have been relevant. The Court treated the specific provisions of the international humanitarian law as an  ...
independent source of international law when considering the applications in question. In particular, the Court  ...    humanitarian law, cannot be justified by reference to the exceptions listed
Article 2 \u00a7 2\u201d.However, based on the facts of the case the Court found that \u201cthe impugned conduct was not compatible with international humanitarian law\u201d as well  ...    1.
Court\u2019s Findings in Respect of Certain Complaints 1. Additionally, based on Article 13 (Effective Remedy) taken in conjunction with Article 1 of Protocol No. 1 (Property  ...    3. The Court
found that widespread and systemic torture and inhuman or degrading treatment within detention facilities  ...    4. The Court examined violations under Article 2 (Right to Life), attributing the
downing of flight MH17 directly to  ...    civilian deaths. Additionally, the Court concluded that indiscriminate shelling and extrajudicial killings in occupied  ...    V. Conclusions and Insights 1.
A fact worth attention is that the Court decided unanimously on all but one point, with the total number of violations amounting to eighteen. This is a rare case in the ECHR practice where the judges
unanimously found so many  ...    2. In its concluding observations, the Court underscored that state responsibility under the Convention cannot be circumvented by acting through non-state actors or
puppet administrations. The Court established that any material, financial, or logistical support by Russia to such forces directly engaged its Convention obligations. Under Article 41, the Court
prepared grounds for considering just satisfaction and provided clear guidance under Article 46,  ...    international mechanism to ensure the safe return of children unlawfully transferred from
Ukraine. Above all, this ECHR decision sets a definitive precedent: fundamental human rights guarantees are non-derogable,"], "published_date": null, "score": null}, {"title": "The 2025 Escalation of
Pressure Towards the ECtHR \u2013 EJIL: Talk!", "url": "https://www.ejiltalk.org/fromoriginalintentionstounforeseeablechangeofcircumstances/", "snippet": "From \u201cOriginal Intentions\u201d to
\u201cUnforeseeable Change of Circumstances\u201d: The 2025 Escalation of Pressure Towards the ECtHR \u2013 EJIL: Talk!\n\nJanuary 5, 2026\n\n# From \u201cOriginal Intentions\u201d to
\u201cUnforeseeable Change of Circumstances\u201d: The 2025 Escalation of Pressure Towards the ECtHR\n\nWhile \u201c[t]oday, Europe faces the perfect storm\u201d that, in the words of the Secretary
General, \u201cthreatens to undo the peace, stability and hard-won progress the Council of Europe has helped deliver across an entire continent ", "highlights": ["ECtHR  ...    Convention on Human
Rights (ECHR or \u201cthe Convention\u201d) as the \u201c moral compass\u201d to guide them through similar  ...    Indeed, the 22nd May 2025 \u201c open letter of the nine\u201d Governments,
criticising the Court\u2019s interpretation of  ...    ### An Escalation of Pressure on the ECtHR and the Narrative Shift: from \u201cOriginal Intent\u201d to \u201cChanged Circumstances\u201d  ...
increasingly tangible possibility should the Court continue delivering judgments these States find politically  ...    ECHR is broken here and needs fixing]\u201d, the conclusions of the ministerial
conference are more diplomatic and  ...    sic stantibus clause, as codified in Article 62 of the [Vienna Convention on the Law of  ...    ### Strategic Pressure? The Wider Context Behind the Informal
Ministerial Conference Conclusions When considering the timing of these two documents vis-\u00e0-vis three pending key Grand Chamber cases relating to push-backs at the EU-Belarus border (C.O.C.G. and
Others v. Lithuania, H.M.M. and Others v. Latvia, and R.A. and Others v. Poland), one has to wonder whether the participating States are driving a collective, and escalating a strategic pressure
campaign to influence the outcome of these cases to reshape the jurisprudence on rights at the border once and for all. Since 2021, in response to Belarus\u2019s deliberate  ...    forcibly returning
migrants to Belarusian territory without individual assessments of their circumstances. The three pending Grand Chamber cases concern whether these States\u2019 violent pushbacks and denials of access
to asylum procedures  ...    remedy (Article 13), in a context where the respondent states invoke \u201c instrumentalization\u201d by Belarus to justify their actions (see also Baranovska). In the
fall of 2024, the Court relinquished jurisdiction to the Grand Chamber in all three cases, highlighting their broader implications for the interpretation of these core Convention rights. The
subsequent hearings in early 2025 revealed a coordinated effort by Lithuania, Latvia, and Poland to discredit the applicants as undeserving and dishonest, while urging the Court to profoundly
\u201cadjust\u201d its non-refoulement jurisprudence to permit exceptions to its non-derogable character when \u201cinstrumentalization\u201d of migrants is alleged.This at times disturbing to watch
courtroom strategy during the Grand Chamber hearings presaged the wider  ...    the \u201cinstrumentalisation\u201d frame that was already visible at the Grand Chamber hearing before the ECtHR. Now,
in December 2025, looking at all these events collectively, a strategic approach seems to appear: aiming at reframing  ...    ### Conclusion: Defending the Convention From Whom? In this intervention,
we have argued that the trajectory from May\u2019s \u201cletter of the nine\u201d to December\u2019s ministerial conference conclusions exposes a calculated escalation of pressure on the ECtHR.  ...
system\u2019s integrity is far more internal: States systematically seeking to limit their own human rights obligations through coordinated political pressure on the Court\u2019s independence. This
inversion follows a classic authoritarian playbook, recasting rights protection itself as the security threat, rather than recognizing that undermining judicial independence and absolute human rights
guarantees is what actually imperils the rule of law and the Convention system\u2019s foundational architecture. As the Grand Chamber prepares to deliver its judgments in the three instrumentalization
cases, the question is whether it can withstand the insidious pressure from within: Contracting States attempting to instrumentalize veiled withdrawal threats to reshape decades of human rights
jurisprudence in their favour. In short, the analysis of the ministerial conclusions and the joint statement confirms the impression of the CoE Commissioner for Human Rights, which  ...    This post
should be read as a companion piece to [\u201cCountdown to Chi\u0219in\u0103u: The Risk of Politicising the ECHR over  ...    Your comment will be revised by the site if needed.\n\n###
Comments\n\nZsuzsanna Deen-Racsm\u00e1ny says  ...    A while ago, I came across an (editorial) opinion in the Financial Times (\u2018It is time to reform the ECHR\u2019, 12 June 2025,
https://www.ft.com/content/9ee947cf-9c44-4efb-a94d-eb5977ec8beb), which too argued in relation to the May 2025 \u2018open letter of the nine\u2019 that the Court had \u201cusurp[ed] the role of
legislators\u201d, stretching human rights protection under the Convention beyond the drafters\u2019 intentions. However, the opinion invoked in that context (also) the KlimaSeniorinnen judgment
(which dealt with Swiss climate policies and most prominently Article 8 of the Convention), rather than discussing the matter solely with regard to migration and Articles 3 and 8 in relation to that
area. In the documents that you cite, I do not see specific references to issues other than migration and asylum, but several principles mentioned there clearly have a much broader reach. Do the
discussions currently underway (still) focus solely on migration and asylum (as suggested by the 10 December Joint Statement and CoE Doc. DD(2025)300-"], "published_date": "2026-01-05T00:00:00.000",
"score": null}, {"title": "ECHR - Homepage of the European Court of Human Rights - ECHR ...", "url": "https://www.echr.coe.int/", "snippet": "ECHR - Homepage of the European Court of Human Rights -
ECHR - ECHR / CEDH\n\n1. Council of Europe\n\n--\n\nHigh-level conference with Ombudsperson Institutions and National Human Rights Institutions\n\nOn 13 March 2026, the second day of the \u201cON
Forum\u201d, the Council of Europe\u2019s High-level Conference with Ombudsperson Institutions and National Human Rights Institutions, took place at the Court\u2019s premises in Strasbourg.\n\nIn his
opening remarks, the President of the Court, Mattias Guyomar, noted that the p", "highlights": ["March 2026, the second day of the \u201cON Forum\u201d, the Council of Europe\u2019s High-level
Conference with Ombudsperson  ...    work, particularly through third party interventions; and they play an essential role in the execution of the Court\u2019s  ...    the dissemination of the
Court\u2019s case-law, the execution of judgments, and the role of National Human Rights  ...    Sancin, judge elected in respect of Slovenia, and John Darcy, Grand Chamber Registrar. This was the
second edition of  ...    On 4 and 25 March 2026 the Court will be holding two Grand Chamber hearings concerning T\u00fcrkiye. The case of Tergek v. T\u00fcrkiye concerns the withholding of
correspondence to the applicant from his wife by the prison authorities. The correspondence consisted of letters, notes, pictures and printed material from internet websites. The letters were
ultimately given to the applicant, but the printed material was not passed on to him. The case of Kavala v. T\u00fcrkiye (No. 2) concerns the applicant\u2019s detention after the judgment delivered by
the ECHR in 2019 and the ensuing criminal proceedings in which he was sentenced to aggravated life imprisonment. - Calendar of hearings\n- Press release ## High-level conference with Ombudsperson
Institutions and National Human Rights Institutions\n\n--- On 13 March 2026, the second day of the \u201cON Forum\u201d, the Council of Europe\u2019s High-level Conference with Ombudsperson  ...
16/03/26  ...    attempted coup d\u2019\u00e9tat in T\u00fcrkiye will enter into force from 1 January 2026. These measures include: applications having  ...    - More info\n- Press release(in
Turkish)\n- Press release\n\n---\n\nmore... ### Referral requests\n\n16/03/26 On 23 March 2026 a panel of five judges will examine nine Grand Chamber referral requests. - Cases pending before the
Grand Chamber\n- Press release\n\n---\n\nmore... ### Judgment concerning France\n\n12/03/26 In the case of Sekour v. France the Court held that there had been no violation of the prohibition of
inhuman or degrading treatment and no violation of the right to an effective remedy. The case concerned solitary-confinement measures applied to a prisoner and the successive decisions to prolong
them. The Court found that it did not appear that the treatment to which the applicant had been subjected in the context of  ...    Convention. - Press release\n\n---\n\nmore...\n\n## Latest press
releases\n\n--- - Green Alliance v. Bulgaria\n- 7 Judgments\n- 10 Judgments & 25 Decisions - Interim measures summary: 85 requests\n- 8 Judgments View all Press releases\n\n## Transparency and
outreach\n\n---\n\n### Visit by the Harvard Club of France  ...    - Multimedia| Twitter @ECHR_CEDH\n- Recent press releases - Recent judgments| Recent decisions\n- ECHR-KS ## On the
agenda\n\n---\n\n### Forthcoming hearing\n\n18/03/26 The Court will be holding a Grand Chamber hearing in the case of S.O. v. Spain on 1 April 2026. The case concerns the removal of the
applicant\u2019s nipple and areola, allegedly carried out without her consent, during  ...    - Calendar of hearings\n- Press release\n\n---\n\nmore... ### Forthcoming Judgments &
Decisions\n\n---\n\n19/03/2026\n\n- 8 Judgments/Decisions\n\n24-26/03/2026 - 3 Judgments & 32 Judgments/Decisions\n\n## Videos\n\n---\n\n---\n\nVideo gallery ECHR Knowledge Sharing: ECHR-KS\n\nHUDOC
database\n\n[Fact"], "published_date": null, "score": null}, {"title": "ANTI-CORRUPTION FOUNDATION (FBK) AND OTHERS v. RUSSIA - 13505/20 (Art 8 - Private life - Home - Correspondence - Mass searches
of homes and offices of persons and entities associated with Aleksey Navalnyy and seizure of property during searches : Remainder inadmissible : Third Section) [2025] ECHR 277 (16 December 2025)",
"url": "https://knyvet.bailii.org/eu/cases/ECHR/2025/277.html", "snippet": "ANTI-CORRUPTION FOUNDATION (FBK) AND OTHERS v. RUSSIA - 13505/20 (Art 8 - Private life - Home - Correspondence - Mass
searches of homes and offices of persons and entities associated with Aleksey Navalnyy and seizure of property during searches : Remainder inadmissible : Third Section) [2025] ECHR 277 (16 December
2025)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> ANTI-CORRUPTION FOUNDATION (FBK) AND OTHERS v. RUSSIA - 13505/20 (Art ",
"highlights": ["searches : Remainder inadmissible : Third Section) [2025] ECHR 277 (16 December 2025) # European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human
Rights>> ANTI-CORRUPTION FOUNDATION (FBK) AND OTHERS v. RUSSIA - 13505/20 (Art 8 - Private life - Home - Correspondence - Mass searches of homes and offices of persons and entities associated with
Aleksey Navalnyy and seizure of property during searches : Remainder inadmissible : Third Section) [2025] ECHR 277 (16 December 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/277.html Cite as:
[2025] ECHR 277 --- | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New search] [Contents list] [Help]\n\n---\n\nTHIRD SECTION CASE OF ANTI-CORRUPTION FOUNDATION (FBK) AND OTHERS v.
RUSSIA\n\n(Applications nos. 13505/20 and 138 others \u2013 see appended list)\n\nJUDGMENT Art 8 \u2022 Private life \u2022 Home \u2022 Correspondence \u2022 Mass searches of homes and offices of
persons and entities associated  ...    standard-form investigator's applications lacking individualised reasoning \u2022 Domestic court's failure to carry out  ...    Art 18 (+ Art 8, 11 and 1 P1)
\u2022 Restriction for unauthorised purposes \u2022 Existence of ulterior purpose \u2022 Impugned measures were part of a concerted effort on an unprecedented scale to eliminate the organised
democratic opposition centred around Aleksey Navalnyy Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n16 December 2025 This judgment will become final in the circumstances set out
in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In the case of Anti-Corruption Foundation (FBK) and Others v. Russia, The European Court of Human Rights (Third
Section), sitting as a Chamber composed of: Ioannis Ktistakis, President, Peeter Roosma, L\u0259tif H\u00fcseynov, Diana Kovatcheva, \u00dana N\u00ed Raifeartaigh, Mateja \u0110urovi\u0107,
Can\u00f2lic Mingorance Cairat, judges, and Olga Chernishova, Deputy Section Registrar, Having regard to:  ...    excluding the application forms (Rule 33 \u00a7 2 of the Rules of Court); the decision
of the President of the Section to appoint one of the elected judges of the Court to sit as an ad hoc judge, applying by analogy Rule 29 \u00a7 2 of the Rules of Court (see Kutayev v. Russia, no.
17912/15, \u00a7\u00a7 5-8, 24 January 2023); Having deliberated in private on 18 November 2025,\n\nDelivers the following judgment, which was adopted on that date:  ...    1. The present case
concerns various measures taken against Mr Aleksey Navalnyy, organisations affiliated with him, his own family members, his associates and, in some cases, their families. The applicants alleged
violations of Article 8 of the Convention on account of mass searches of their offices and homes and the seizure of property during the  ...    her status as his heir. It further observes that, in
application no. 13505/20, Mr Navalnyy lodged an individual  ...    81. The Court reiterates that, as a general rule, the six-month time-limit runs from the date of the final decision in  ...    157,
ECHR 2009). In cases governed by the Code of Criminal Procedure, the appeal judgment must be considered when  ...    84."], "published_date": null, "score": null}, {"title": "", "url":
"https://hudoc.echr.coe.int/app/conversion/docx/pdf?filename=CASE+OF+GREEN+v.+THE+UNITED+KINGDOM.pdf&id=001-242635&library=ECHR", "snippet": "FOURTH SECTION\nCASE OF GREEN v. THE UNITED
KINGDOM\n(Application no. 22077/19)\nJUDGMENT\nArt 8 \u2022 Positive obligations \u2022 Private life \u2022 Use of parliamentary privilege by a Member of \nParliament to disclose on the floor of the
House the applicant\u2019s identity subject to an interim \nprivacy injunction pending trial \u2022 Disclosure with serious consequences for the applicant \u2022 \nFirst and foremost for national
parliaments to assess the need to restrict their Members\u2019 \nconduct \u2022 Rule on parliamentary privile", "highlights": ["and foremost for national parliaments to assess the need to restrict
their Members\u2019 conduct \u2022 Rule on parliamentary privilege not entirely devoid of ex ante and ex post controls \u2022 Parliamentary privilege, in the majority of Member States, afforded
absolute protection from external legal actions to statements made by parliamentarians in Parliament or in the exercise of their parliamentary duties \u2022 Wide margin of appreciation not exceeded
\u2022 Lack of sufficiently strong reasons to justify requiring the introduction of further ex ante and ex post controls to prevent Members of Parliament from revealing information subject to privacy
injunctions \u2022 Respondent State to regularly review the need for appropriate controls, given serious impact of disclosure of information subject to privacy injunctions Prepared by the Registry.
Does not bind the Court.\nSTRASBOURG\n8 April 2025\nFINAL\n08/07/2025 This judgment has become final under Article 44 \u00a7 2 of the Convention. \nIt may be subject to editorial revision. GREEN v.
THE UNITED KINGDOM JUDGMENT\n1\nIn the case of Green v. the United Kingdom, The European Court of Human Rights (Fourth Section), sitting as a \nChamber composed of:\nLado Chanturia, President, Tim
Eicke,\nLorraine Schembri Orland,\nAna Maria Guerra Martins,\nAnne Louise Bormann,\nSebastian R\u0103dule\u0163u, Andr\u00e1s Jakab, judges,\nand Simeon Petrovski, Deputy Section Registrar,\nHaving
regard to: the application (no. 22077/19) against the United Kingdom of Great Britain and Northern Ireland lodged with the Court under Article 34 of the Convention for the Protection of Human Rights
and Fundamental Freedoms (\u201cthe Convention\u201d) by a British national, Mr Philip Nigel Ross Green (\u201cthe \napplicant\u201d), on 23 April 2019; the decision to give notice to the United
Kingdom Government (\u201cthe Government\u201d) of the complaints concerning Article 6, Article 8 (in respect of the regulation of parliamentary privilege) and Article 13 of the Convention and to
declare inadmissible the remainder of the application;\nthe parties\u2019 observations; Having deliberated in private on 4 March 2025,\nDelivers the following judgment, which was adopted on that date:
INTRODUCTION\n1. Invoking parliamentary privilege, a Member of the House of Lords made a personal statement in the chamber identifying the applicant as the subject of an anonymised newspaper article
even though the Court of Appeal had granted an interim injunction and anonymity orders to prevent the \npublication of his identity. 2. Before the Court the applicant relies on Articles 6 \u00a7 1, 8
and 13 of the \nConvention.\nTHE FACTS 3. The applicant is a British national who was born in 1952 and lives in Monaco. He is represented before the Court by Mr I.R. Burton of \nBCL Solicitors in
London. 4. The Government were represented by their Agent, Mr S. Linehan of the \nForeign, Commonwealth and Development Office. 5. The facts of the case may be summarised as follows.\nGREEN v. THE
UNITED KINGDOM JUDGMENT\n2  ...    Lord Hain had failed to declar  parliamentary privilege and making recommendations. In its Report on  ...    GREEN v. THE UNITED KINGDOM JUDGMENT\n8\n\u201c12.
Freedom of speech is central to Parliament\u2019s role. Members must be able to  ...    protection of \u2018proceedings in Parliament\u2019 guaranteed by article 9 of the Bill of Rights 1689. Members
are not exposed to any civil or criminal liabilities in respect of what  ...    36. After analysing parliamentary privilege, the Report recommended that a Parliamentary Privileges Act be enacted to
codify parliamentary privilege  ...    37. A Joint Committee of both Houses of Parliament on Privacy and  ...    March 2012 (Session 2010-12, HL 273, HC 1443). It noted that there had  ...
\u201c214. Article IX [of the Bill of Rights] means that it would not be constitutionally  ...    has been revealed; Article IX prevents them taking proceedings against the member.\u201d\n38. It
concluded: \u201c230. We regard freedom of speech in Parliament as a fundamental constitutional principle. Over the last couple of years a few members have revealed in Parliament  ...    GREEN v. THE
UNITED KINGDOM JUDGMENT\n9\n231. If the revelation of injuncted information becomes more commonplace, if  ...    39. In April 2012 the Government published a Green Paper on Parliamentary Privilege. A
Joint Committee on Parliamentary Privilege was  ...    Paper. The Committee published its Report on Parliamentary Privilege on  ...    \u201c20. The possibility of tension between parliamentary
privilege and the rule of law  ...    safeguard the effective functioning of Parliament. It is agreed that immunity applies to that core"], "published_date": null, "score": null}, {"title": "Z AND
OTHERS v. FINLAND - 42758/23 (Art 8 - Family life - Order for return of two children from Finland to Russia under the Hague Convention following removal by their father : Remainder inadmissible :
Second Section) [2025] ECHR 281 (16 December 2025)", "url": "https://knyvet.bailii.org/eu/cases/ECHR/2025/281.html", "snippet": "Z AND OTHERS v. FINLAND - 42758/23 (Art 8 - Family life - Order for
return of two children from Finland to Russia under the Hague Convention following removal by their father : Remainder inadmissible : Second Section) [2025] ECHR 281 (16 December 2025)\n\n# European
Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> Z AND OTHERS v. FINLAND - 42758/23 (Art 8 - Family life - Order for return of two children from
Finland to Russia under the Hague Conventio", "highlights": ["(16 December 2025) # European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human Rights>> Z AND
OTHERS v. FINLAND - 42758/23 (Art 8 - Family life - Order for return of two children from Finland to Russia under the Hague Convention following removal by their father : Remainder inadmissible :
Second Section) [2025] ECHR 281 (16 December 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/281.html Cite as: [2025] ECHR 281 --- | [Home] [Databases] [World Law] [Multidatabase Search]  ...
[New search] [Contents list] [Help]\n\n---\n\nSECOND SECTION CASE OF Z AND OTHERS v. FINLAND\n\n(Application no. 42758/23)\n\nJUDGMENT Art 8 \u2022 Family life \u2022 Order for return of two children
from Finland to Russia under the Hague Convention following  ...    Relevant and sufficient reasons \u2022 Domestic courts genuinely took into account the factors capable of constituting an  ...
Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n16 December 2025 This judgment will become final in the circumstances set out in Article 44 \u00a7 2 of the Convention. It may be
subject to editorial revision. In the case of Z and Others v. Finland, The European Court of Human Rights (Second Section), sitting as a Chamber composed of: Arnfinn B\u00e5rdsen, President, Saadet
Y\u00fcksel, Jovan Ilievski, P\u00e9ter Paczolay, Gediminas Sagatys, Juha Lavapuro, Hugh  ...    Having regard to:  ...    two minor sons, X and Y (\"the applicants\"), on 15 December 2023; the
decision to give notice to the Finnish Government (\"the Government\") of the application;  ...    the comments submitted by the AIRE Centre and Ms G., the mother of the second and third applicants,
who were granted leave to intervene as third parties by the President of the Section; Having deliberated in private on 18 November 2025,\n\nDelivers the following judgment, which was adopted on that
date:  ...    1. The case concerns the domestic courts' decision to order the return of the applicant children, who were granted  ...    2. The applicants are Russian nationals. The first applicant,
who was born in 1983, is the father of the second and  ...    III. RULE 39 OF THE RULES OF COURT 64. The Court reiterates that, in accordance with Article 44 \u00a7 2 of the Convention, the present
judgment will not become final until (a) the parties declare that they will not request that the case be referred to the Grand Chamber; or (b) three months after the date of the judgment, if referral
of the case to the Grand Chamber has not been requested; or (c) the Panel of the Grand Chamber rejects any request to refer under Article 43 of the Convention. 65. It considers that the indications
made to the Government under Rule 39 of the Rules of Court should remain in force  ...    FOR THESE REASONS, THE COURT, UNANIMOUSLY, 1. Declares the complaint concerning Article 8 admissible and the
remainder of the application inadmissible; 2. Holds that there has been no violation of Article 8 of the Convention; 3. Decides to continue to indicate to the Government under Rule 39 of the Rules of
Court that it is desirable in the  ...    present judgment becomes final or until further notice. Done in English, and notified in writing on 16 December 2025, pursuant to Rule 77 \u00a7\u00a7 2 and 3
of the Rules of Court. Hasan Bak\u0131rc\u0131 Arnfinn B\u00e5rdsen Registrar President In accordance with Article 45 \u00a7 2 of the Convention and Rule 74 \u00a7 2 of the Rules of Court, the joint
concurring opinion  ...    In the present case, while we agree with the majority's position on the outcome, we respectfully dissociate ourselves  ...    1. In respect of general principles, the
Chamber's reasoning in the present case follows X v. Latvia ([GC], no. 27853/09, ECHR 2013), where the Court imposed a particular procedural obligation on Member States. Domestic courts must  ...
the extent that the Supreme Court in its judgment of 27 September 20"], "published_date": null, "score": null}, {"title": "EUROPA WAY S.R.L. v. ITALY - 64356/19 (Article 10 - Freedom of expression -
{general} : First Section) [2025] ECHR 265 (27 November 2025)", "url": "https://knyvet.bailii.org/eu/cases/ECHR/2025/265.html", "snippet": "EUROPA WAY S.R.L. v. ITALY - 64356/19 (Article 10 - Freedom
of expression - {general} : First Section) [2025] ECHR 265 (27 November 2025)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> EUROPA
WAY S.R.L. v. ITALY - 64356/19 (Article 10 - Freedom of expression - {general} : First Section) [2025] ECHR 265 (27 November 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/265.html Cite as:
[2025] ECHR 265\n\n---\n\n| [Home] [Databases] [World L", "highlights": ["European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human Rights>> EUROPA WAY S.R.L. v.
ITALY - 64356/19 (Article 10 - Freedom of expression - {general} : First Section) [2025] ECHR 265 (27 November 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/265.html Cite as: [2025] ECHR 265
--- | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New search] [Contents list] [Help]\n\n---\n\nFIRST SECTION CASE OF EUROPA WAY S.R.L. v. ITALY\n\n(Application no.
64356/19)\n\nJUDGMENT Art 10 \u2022 Freedom of expression \u2022 Freedom to impart information and ideas \u2022 Suspension by ministerial decree and  ...    television broadcasting which were set out
in regulations by the appropriate regulatory authority \u2022 Annulment of  ...    exercise of the regulatory authority's functions undermined its independence \u2022 Objective of restoring
independent exercise of functions not achieved \u2022 Relevant legal framework not foreseeable and not providing sufficient safeguards against arbitrariness \u2022 Interference did not meet lawfulness
nor \"quality of law\" requirements Prepared by the Registry. Does not bind the Court.\n\nSTRASBOURG\n\n27 November 2025 This judgment will become final in the circumstances set out in Article 44
\u00a7 2 of the Convention. It may be subject to editorial revision. In the case of Europa Way S.r.l. v. Italy, The European Court of Human Rights (First Section), sitting as a Chamber composed of:
Ivana Jeli\u0107, President, Erik Wennerstr\u00f6m, Raffaele Sabato, Fr\u00e9d\u00e9ric Krenc, Davor Deren\u010dinovi\u0107, Alain Chablais, Art\u016brs Ku\u010ds, judges, and Ilse Freiwirth, Section
Registrar, Having regard to: the application (no. 64356/19) against the Italian Republic lodged with the Court under Article 34 of the  ...    company registered in Italy, Europa Way S.r.l. (\"the
applicant company\"), on 12 December 2019; the decision to give notice to the Italian Government (\"the Government\") of the complaint under Article 10 of the  ...    the parties'
observations;\n\nHaving deliberated in private on 4 November 2025, Delivers the following judgment, which was adopted on that date:\n\nINTRODUCTION 1. The case concerns the suspension by ministerial
decree and the subsequent annulment by legislation of a bidding procedure for the allocation of frequencies for digital terrestrial television broadcasting which had been set out in  ...    2. The
applicant company is a limited liability company operating in the television-broadcasting sector. It has its  ...    highest offeror\" (orders no. 10415, 10416 and 10419, deposited at the registry on
1 December 2023). 49. On 11 September 2025 in its judgment in Cairo Network, C\u2011764/23, C-765/23 and C\u2011766/23, EU:C:2025:691, the CJEU reiterated that when regulating how rights to use radio
frequencies should be allocated NRAs should be free of  ...    from those currently before it. The present issue was not legislative intervention that might call into question a  ...    50. The main
developments in the Italian television broadcasting sector, from its origins to the beginning of the digital switchover, are described in Centro Europa 7 S.r.l. and Di Stefano v. Italy [GC], no.
38433/09, \u00a7\u00a7 49\u201168, ECHR 2012. 51. Article 7 of Legislative Decree no. 259 of 1 August 2003 (\"Electronic Communications Code\") as amended by  ...    \"... 3 bis. The [AG"],
"published_date": null, "score": null}, {"title": "BAZHENOV AND OTHERS v. RUSSIA - 8825/22 (Article 14+8 - Discrimination on the basis of sexual orientation : Third Section) [2025] ECHR 31 (04
February 2025)", "url": "https://bruneis.bailii.org/eu/cases/ECHR/2025/31.html", "snippet": "BAZHENOV AND OTHERS v. RUSSIA - 8825/22 (Article 14+8 - Discrimination on the basis of sexual orientation :
Third Section) [2025] ECHR 31 (04 February 2025)\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> BAZHENOV AND OTHERS v. RUSSIA -
8825/22 (Article 14+8 - Discrimination on the basis of sexual orientation : Third Section) [2025] ECHR 31 (04 February 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/31.html Cite as: [2025] ECHR
31", "highlights": ["here: BAILII>> Databases>> European Court of Human Rights>> BAZHENOV AND OTHERS v. RUSSIA - 8825/22 (Article 14+8 - Discrimination on the basis of sexual orientation : Third
Section) [2025] ECHR 31 (04 February 2025) URL: https://www.bailii.org/eu/cases/ECHR/2025/31.html Cite as: [2025] ECHR 31  ...    | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New
search] [Contents list] [Help]\n\n---\n\nTHIRD SECTION CASE OF BAZHENOV AND OTHERS v. RUSSIA\n\n(Applications nos. 8825/22 and 19130/22)\n\nJUDGMENT Art 14 (+ Art 8) \u2022 Discrimination on the basis
of sexual orientation \u2022 Private life \u2022 Domestic authorities' failure to  ...    the LGBTI community in Russia and their need for special protection disregarded Prepared by the Registry. Does
not bind the Court.\n\nSTRASBOURG\n\n4 February 2025 This judgment will become final in the circumstances set out in Article 44 \u00a7 2 of the Convention. It may be subject to editorial revision. In
the case of Bazhenov and Others v. Russia, The European Court of Human Rights (Third Section), sitting as a Chamber composed of: Ioannis Ktistakis, President, Peeter Roosma, L\u0259tif H\u00fcseynov,
Andreas Z\u00fcnd, Oddn\u00fd Mj\u00f6ll Arnard\u00f3ttir, Diana Kovatcheva, \u00dana N\u00ed Raifeartaigh, judges, and Olga Chernishova, Deputy Section Registrar,  ...    Article 34 of the Convention
for the Protection of Human Rights and Fundamental Freedoms (\"the Convention\") by three  ...    the decision of the President of the Section to appoint one of the elected judges of the Court to sit
as an ad hoc judge, applying by analogy Rule 29 \u00a7 2 of the Rules of Court (see Kutayev v. Russia, no. 17912/15, \u00a7\u00a7 5-8, 24 January 2023); Having deliberated in private on 14 January
2025,\n\nDelivers the following judgment, which was adopted on that date:  ...    1. The case concerns alleged failures by the domestic authorities to comply with their positive obligation to respond
...    39. On 5 October 2021 the investigator took a decision refusing to open a criminal investigation, indicating as the reason the absence of a violation of the applicant's privacy.  78. In the
light of the foregoing, the Court concludes that the authorities failed to discharge their positive obligation to respond adequately to the non-consensual  ...    individuals, and to investigate in an
effective manner whether the dissemination of the data in question had been  ...    80. In view of its findings above, the Court considers that it is not necessary to examine separately whether there
has  ...    III. APPLICATION OF ARTICLE 41 OF THE CONVENTION\n\n81. Article 41 of the Convention provides: \"If the Court finds that there has been a violation of the Convention or the Protocols
thereto, and if the internal law  ...    84. The applicants did not claim costs and expenses. Accordingly, there is no call to make an award under this head. FOR THESE REASONS, THE COURT,
UNANIMOUSLY,\n\n1. Decides to join the applications; 2. Holds that it has jurisdiction to deal with the applications as they relate to facts that took place before 16 September 2022 and that the
Government's failure to participate in the proceedings presents no obstacles for the  ...    3. Declares the applications admissible; 4. Holds that there has been a violation of Article 14 taken in
conjunction with Article 8 of the Convention; 5. Holds that there is no need to examine the remainder of the complaints;\n\n6. Holds (a) that the respondent State is to pay the applicants, within
three months from the date on which the judgment becomes final in accordance with Article 44 \u00a7 2 of the Convention, EUR 7,000 (seven thousand euros) each, plus any tax that may  ...    rate
applicable at the date of settlement; (b) that from the expiry of the above-mentioned three months until settlement simple interest shall be payable on the  ...    three percentage points. Done in
English, and notified in writing on 4 February 2025, pursuant to Rule 77 \u00a7\u00a7 2 and 3 of the Rules of Court. Olga Chernishova Ioannis Ktistakis Deputy Registrar President\n\nAPPENDIX\n\nList
of cases:\n\nNo.\n\nApplication no. Case name\n\nLodged on\n\nApplicant Year of birth Place of residence Nationality\n\nRepresented by\n\n1.\n\n8825/22 Bazhenov and Semkin\n\nv.
Russia\n\n03/02/2022\n\nYevgeniy\n\nIgorevich\n\nBAZHENOV 1985 Moscow Russian Aleksandr  ...    BAILII: Copyright Policy| Disclaimers| Privacy Policy| Feedback| Donate to BAILII URL:
https://www.bailii.org/eu/cases/ECHR/2025/"], "published_date": null, "score": null}, {"title": "", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Grand+Chamber+judgment+Semenya+v.+Sw
itzerland+-+Complaint+by+international+athlete+concerning+set+of+World+Athletics+regulations.pdf&id=003-8280639-11659757&library=ECHR", "snippet": "issued by the Registrar of the Court\nECHR 180
(2025)\n10.07.2025\nViolation of international athlete\u2019s right to a fair hearing \non account of Federal Supreme Court\u2019s limited review \nof an arbitral award relating to a set of World
Athletics regulations\nThe case of Semenya v. Switzerland (application no. 10934/21) concerned an international-level South \nAfrican athlete who complained about a set of regulations issued by World
Athletics (\u201cthe DSD \nRegulations\u201d1) requiring her to decrease her natural ", "highlights": ["Semenya v. Switzerland (application no. 10934/21) concerned an international-level South African
athlete who complained about a set of regulations issued by World Athletics (\u201cthe DSD  ...    Switzerland \u2013 and then the Swiss Federal Supreme Court. In today\u2019s Grand Chamber judgment2
in this case the European Court of Human Rights declared, by 13 to 4, inadmissible the applicant\u2019s complaints under Articles 8 (right to respect for private life), 13 (right to an effective
remedy) and 14 (prohibition of discrimination) of the Convention. It found that Ms Semenya did not fall within Switzerland\u2019s jurisdiction in respect of those complaints.\nBy contrast, the Court:
\u2013 declared, unanimously, the application admissible in respect of the complaint under Article 6 \u00a7 1  ...    \u2013 held, by 15 votes to 2, that there had been a violation of Article 6 \u00a7
1 (right to a fair hearing) of the Convention.\nThe Court considered, first, that the appeal lodged by the applicant with the Federal Supreme Court  ...    2 Grand Chamber judgments are final (Article
44 of the Convention). All final judgments are transmitted to the Committee of Ministers of the Council of Europe for supervision of their  ...    information about the execution process can be found
here: www.coe.int/t/dghl/monitoring/execution.\n2 given the Federal Supreme Court\u2019s failure to fulfil the requirement to carry out a particularly rigorous \nexamination. This press release is
accompanied by a Q&A sheet (link). A legal summary of this case will be available in the Court\u2019s database HUDOC (link)\nPrincipal facts  ...    In 2020 the Federal Supreme Court dismissed the
applicant\u2019s appeal, holding that the award in  ...    The application was lodged with the European Court of Human Rights on 18 February 2021. In its judgment of 11 July 2023, a Chamber of the
Court held, by a majority, that there had been a violation of Article 14 of the Convention taken together with Article 8, and a violation of Article 13 in relation to Article 14 taken together with
Article 8. The Chamber held, in particular, that the applicant had not been afforded sufficient institutional and procedural safeguards in Switzerland. On 9 October 2023 the Government requested that
the case be referred to the Grand Chamber under Article 43, and on 6 November 2023 a panel of the Grand Chamber accepted that request. A hearing took place on 15 May 2024.\n3\nNumerous third parties
(including the United Kingdom Government, the United Nations High Commissioner for Human Rights, and World Athletics) were given leave to intervene in the written \nprocedure. Judgment was given by
the Grand Chamber of 17 judges, composed as follows:\nMarko Bo\u0161njak (Slovenia), President, S\u00edofra O\u2019Leary (Ireland),\nArnfinn B\u00e5rdsen (Norway),\nGabriele Kucsko-Stadlmayer
(Austria),\nMattias Guyomar (France), Faris Vehabovi\u0107 (Bosnia and Herzegovina),\nM\u0101rti\u0146\u0161 Mits (Latvia),\nPauliine Koskelo (Finland), Tim Eicke (the United Kingdom),\nJolien
Schukking (the Netherlands),\nErik Wennerstr\u00f6m (Sweden),\nRaffaele Sabato (Italy),  ...    In the Court\u2019s view, the specific characteristics of the sports arbitration to which the applicant
had  ...    Judge \u0160im\u00e1\u010dkov\u00e1 expressed a partly concurring opinion. Judges Bo\u0161njak, Z\u00fcnd, \u0160im\u00e1\u010dkov\u00e1 and  ...    expressed a joint partly dissenting
opinion. These opinions are annexed to the judgment. The judgment is available in English and French. This press release is a document produced by the Registry. It does not bind the Court. Decisions,
judgments and further information about the Court can be found on www.echr.coe.int. To receive the Court\u2019s press releases, please subscribe here: www.echr.coe.int/RSS/en or follow us on X
(Twitter) @ECHR_CEDH and Bluesky @echr.coe.int.\nPress contacts\nechrpress@echr.coe.int | tel.: +33 3 90 21 42 08 We are happy to receive journalists\u2019 enquiries via either email or
telephone.\nInci Ertekin (tel: + 33 3 90 21 55 30)  ...    The European Court of Human Rights was set up in Strasbourg"], "published_date": null, "score": null}, {"title": "European Lotto and Betting
v EUIPO - Multi-State Lottery Association (Powerball) (EU trade mark - Judgment) [2025] EUECJ T-375/24 (29 October 2025)", "url": "https://knyvet.bailii.org/eu/cases/EUECJ/2025/T37524.html",
"snippet": "\ufeff European Lotto and Betting v EUIPO - Multi-State Lottery Association (Powerball) (EU trade mark - Judgment) [2025] EUECJ T-375/24 (29 October 2025)\n\n# Court of Justice of the
European Communities (including Court of First Instance Decisions)\n\n---\n\nYou are here: BAILII>> Databases>> Court of Justice of the European Communities (including Court of First Instance
Decisions)>> European Lotto and Betting v EUIPO - Multi-State Lottery Association (Powerball) (EU trade mark - Judgment) [2025] EUECJ T", "highlights": ["Instance Decisions)\n\n--- You are here:
BAILII>> Databases>> Court of Justice of the European Communities (including Court of First Instance Decisions)>> European Lotto and Betting v EUIPO - Multi-State Lottery Association (Powerball) (EU
trade mark - Judgment) [2025] EUECJ T-375/24 (29 October 2025) URL: https://www.bailii.org/eu/cases/EUECJ/2025/T37524.html Cite as: ECLI:EU:T:2025:998, [2025] EUECJ T-375/24, EU:T:2025:998 --- |
[Home] [Databases] [World Law] [Multidatabase Search]  ...    | --- | [New search] [Contents list] [Help]\n\n--- JUDGMENT OF THE GENERAL COURT (Seventh Chamber)\n\n29 October 2025 (*) ( EU trade mark
- Invalidity proceedings - EU word mark Powerball - Absolute ground for invalidity - Article 52(1)(b) of Regulation (EC) No 207/2009 - Bad faith ) In Case T\u2011375/24, European Lotto and Betting
ltd., established in Birkirkara (Malta), represented by T. Nix and D. Selmi, lawyers,  ...    European Union Intellectual Property Office (EUIPO), represented by M. Chyli\u0144ska, E. Markakis and V.
Ruzek, acting as  ...    Vandezande and F. Verhoestraete, lawyers, THE GENERAL COURT (Seventh Chamber), composed, at the time of the deliberations, of K. Kowalik-Ba\u0144czyk, President, I.
Dimitrakopoulos and B. Ricziov\u00e1 (Rapporteur), Judges, Registrar: G. Mitrev, Administrator,\n\nhaving regard to the written part of the procedure, further to the hearing on 4 July 2025,\n\ngives
the following\n\nJudgment 1 By its action under Article 263 TFEU, the applicant, European Lotto and Betting ltd., seeks the annulment in part of the decision of the First Board of Appeal of the
European Union Intellectual Property Office (EUIPO) of 23 May 2024 (Case R 1915/2022-1) ('the contested decision').  ...    2 On 30 April 2021, the intervener, Multi-State Lottery Association, filed
with EUIPO an application for a declaration  ...    5 On 2 August 2022, the Cancellation Division upheld the application for a declaration of invalidity in its entirety.  ...    dismissed in its
entirety. Costs 43 Under Article 134(1) of the Rules of Procedure of the General Court, the unsuccessful party is to be ordered to pay the costs if they have been applied for in the successful party's
pleadings. 44 Since the applicant has been unsuccessful, it must be ordered to pay the costs, in accordance with the forms of order sought by EUIPO and the intervener. On those grounds,\n\nTHE GENERAL
COURT (Seventh Chamber)\n\nhereby:\n\n1. Dismisses the action; 2. Orders European Lotto and Betting ltd. to pay the costs.\n\nKowalik-Ba\u0144czyk\n\nDimitrakopoulos\n\nRicziov\u00e1 Delivered in open
court in Luxembourg on 29 October 2025.\n\nV. Di Bucci\n\nM. van der Woude\n\nRegistrar\n\nPresident\n\n--- * Language of the case: English. \u00a9 European UnionThe source of this judgment is the
Europa web site. The information on this site is subject  ...    subject to amendment. --- BAILII: Copyright Policy| Disclaimers| Privacy Policy| Feedback| Donate to BAILII URL:
https://www.bailii.org/eu/cases/EUECJ/2025/T375"], "published_date": null, "score": null}]
```

```json
{
  "query": "ECHR Grand Chamber judgment delivery 2026",
  "hours_back": 720,
  "n_articles": 10
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: MidiaNews | TJ barra nova tentativa de ex-procurador da AL de se livrar de júri\n\nSummary: \nThe Third
Criminal Chamber of the Court of Justice of Mato Grosso (TJ-MT), presided over by Judge Gilberto Giraldelli, unanimously rejected a new appeal by Luiz Eduardo Figueiredo Rocha e Silva, a former
prosecutor of the Legislative Assembly, and maintained his referral to the Jury Tribunal (Tribunal do Júri) for the alleged homicide of homeless resident Ney Müller Alves Pereira. The incident
occurred in April 2025 in Cuiabá. The decision was published on Wednesday, March 18, 2026. The defense argued procedural omissions, claiming the court failed to analyze arguments regarding the denial
of evidence, alleged deficiencies in technical defense, and a geolocation study submitted after the initial ruling. However, Judge Giraldelli ruled that the arguments did not meet the requirements of
Article 619 of the Code of Criminal Procedure, noting that the defense had not previously challenged the denial of the simulated reproduction request or the loss of a chance to present evidence. The
court further determined that the alleged deficiency in the previous defense was unsubstantiated, as the previous lawyers acted within professional limits and no concrete procedural damage was proven.
Regarding the geolocation study, the court found it was submitted unilaterally after the pronouncement decision without prior analysis by the trial court, and reviewing it directly would constitute a
suppression of jurisdiction; furthermore, the content was deemed insufficient to refute the evidence of intent (dolo) in the accusation. The court emphasized that maintaining the pronouncement does
not constitute a judgment of guilt, which remains the exclusive competence of the Jury Tribunal.\n\nPublished date: March 19 2026, 21:00\n\nURL: https://www.midianews.com.br/judiciario/tj-barra-nova-
tentativa-de-ex-procurador-da-al-de-se-livrar-de-juri/516465\nImage description: A man identified by the nameplate as 'Gilberto Giraldelli, Desembargador' (Judge), wearing judicial robes with red
trim, a light blue shirt, and a purple patterned tie, speaking into a microphone while seated at a wooden bench.\nSource: MidiaNews\nClassification: Crime\nSentiment: negative\nReporting voice:
Objective\nContinent: South America\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: Câmara terá palavra final sobre os mandatos de deputados do PL condenados pelo STF, diz Motta\n\nSummary: \nOn
Wednesday, March 18, 2026, Câmara dos Deputados President Hugo Motta (Republicanos-PB) stated that the Chamber's plenary must decide on the loss of mandates for PL deputies convicted by the Supreme
Federal Court (STF) for passive corruption. According to Motta, the Chamber will only take action after all judicial appeals are exhausted, as the trial was not fully concluded on Tuesday due to
pending appeals ('embargos') that defendants are expected to file. Motta emphasized that the process will begin only after the 'trânsito em julgado' (final judgment), ensuring due process and
compliance with internal rules. The decision follows the STF's First Chamber's unanimous conviction of deputies Josimar Maranhãozinho (PL-MA) and Pastor Gil (PL-MA), and former deputy João Bosco (PL-
SE), in a case involving the misappropriation of parliamentary amendment funds.\n\nPublished date: March 18 2026, 18:45\n\nURL: https://www.cartacapital.com.br/politica/camara-tera-palavra-final-
sobre-os-mandatos-de-deputados-do-pl-condenados-pelo-stf-diz-motta/\nImage description: A man in a blue suit and purple tie speaking at a podium with a microphone, surrounded by several women and men.
A purple banner behind him reads 'ANTES QUE ACONTEÇA' (Before it happens) and mentions a support network against violence towards women. The setting appears to be an official government
building.\nSource: CartaCapital\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: South America\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle: El Tribunal de
Justicia de la UE deja para mayo su sentencia sobre la amnistía española\n\nSummary: \nThe Court of Justice of the European Union (CJEU) will deliver its judgment on the Spanish amnesty law in May,
according to European sources confirmed by EL PERIÓDICO. This decision comes after the Advocate General, Luxembourg's Dean Spielmann, presented his non-binding opinion on November 13, 2025. The CJEU
will first rule on the status of interim civil servants on April 14, 2026. The Spanish Constitutional Court (TC) has seven pending appeals regarding the refusal to apply the amnesty law to the
embezzlement charge, affecting seven independentist leaders: Oriol Junqueras, Dolors Bassa, Jordi Turull, Toni Comin, Lluís Puig, Carles Puigdemont, and Raül Romeva. The TC has already ruled the
amnesty law constitutional by dismissing appeals from the Partido Popular and the Supreme Court's Second Chamber. Advocate General Spielmann's opinion refutes claims that the law constitutes an 'auto-
amnesty' or violates EU financial interests, countering arguments made by EU Commission lawyers aligned with the PP and judges Manuel Marchena and Pablo Llarena. The TC will proceed with the appeals
after the CJEU's May judgment, a process that may be delayed due to internal disagreements among magistrates. Until these appeals are resolved, the seven leaders remain barred from running for office
due to disqualification sentences valid until 2031, and Carles Puigdemont remains subject to a detention order by Judge Pablo Llarena.\n\nPublished date: March 18 2026, 18:01\n\nURL:
https://www.elperiodico.com/es/politica/20260318/ernesto-ekaizer-vuelve-aplazarse-tjue-sentencia-amnistia-puigdemont-128114701\nSource: El Periódico\nClassification: Politics\nSentiment:
neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: European Court of Human Rights Upheld Six Complaints Against The Czech Republic Last
Year\n\nSummary: \nThe European Court of Human Rights (ECHR) upheld six complaints against the Czech Republic in 2025, one fewer than the previous year, according to Petr Konupka, the government’s
commissioner for the ECHR. In these cases, complainants requested CZK 11 million and were awarded CZK 2 million. The court ruled against the Czech Republic regarding the instruction of people with
intellectual disabilities on procedural rights and the inclusion of lawyer-client communications in criminal files. Conversely, the Czech Republic successfully defended cases concerning child
information rights, residential social services, and the use of cooperating defendants in organized crime prosecutions. A dispute with a Liechtenstein noble family over land and monuments remains
ongoing. Between 2022 and 2025, the Strasbourg Court ruled on 115 cases involving the Czech Republic, finding a Convention violation in 19 cases and no violation in 83, with 13 cases ending in
conciliation or declarations. Across this period, claimants sought CZK 529.5 million and received CZK 6.5 million, representing approximately 1% of the total claim. The court is also reviewing issues
related to pandemic emergency measures, hate crime investigations, and foreign adoption recognition by same-sex couples.\n\nPublished date: March 18 2026, 16:52\n\nURL:
https://brnodaily.com/2026/03/18/news/european-court-of-human-rights-upheld-six-complaints-against-the-czech-republic-last-year/\nSource: brnodaily.com\nClassification: Politics\nSentiment:
neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: Fisco, legittimi gli accessi ai conti terzi senza prove di abuso\n\nSummary: \nOn March 17, 2026,
the Italian Corte di Cassazione issued Ordinance 5971, establishing that tax authorities may legally access third-party bank accounts without violating the European Convention on Human Rights (ECHR),
provided there is concrete evidence of tax evasion and the taxpayer does not contest the privacy violation in the early stages of the trial. According to the ruling, invoking ECHR protections
(specifically Article 8) requires raising specific objections during the initial degrees of judgment; failing to do so prevents the Supreme Court from reviewing the claim. The Court distinguished
between arbitrary 'exploratory' investigations and legitimate 'investigative' actions based on prior evidence. In the specific case examined, a professional challenged a tax assessment based on third-
party accounts but was unsuccessful because their objection was raised for the first time at the Cassation level. The ruling notes that while the ECHR previously criticized Italy in the January 8,
2026, 'Ferrieri and Bonassisa v. Italy' decision for granting excessive power to tax authorities, the Cassation clarified that ECHR principles do not apply automatically if the investigation is
grounded in solid proof of evasion. The decision confirms that accessing accounts of third parties, such as family members or close collaborators, is valid when a link exists suggesting those accounts
were used to manage the taxpayer's proceeds, provided the investigation is not random but a necessary deepening of confirmed suspicions.\n\nPublished date: March 18 2026, 05:42\n\nURL:
https://www.laleggepertutti.it/786391_fisco-legittimi-gli-accessi-ai-conti-terzi-senza-prove-di-abuso\nSource: laleggepertutti\nClassification: Politics\nSentiment: neutral\nReporting voice:
Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [6]\nTitle: Europäischer Gerichtshof: Darf Kirchenaustritt den Job kosten? EU-Urteil erwartet\n\nSummary: \nThe Grand Chamber of the
Court of Justice of the European Union (EuGH) is set to rule on March 17, 2026, at 09:00, regarding a dispute over whether leaving the Catholic Church can justify dismissal from a job. The case
involves a social worker at a Caritas-affiliated pregnancy counseling center in Wiesbaden who was fired after leaving the church, despite church membership not being a prerequisite for the role. The
employee, who stated she remains a 'very believing person' and had no intention to leave, cited the 'special church tax' as her reason; she would have had to pay over €2,000 annually due to her
husband's exit from the church following a financial scandal involving the former Bishop of Limburg. While the employee won in lower German courts, the Federal Labour Court referred the question of
whether this dismissal constitutes discrimination under EU rules to the EuGH. The Church argues that leaving is a 'conscious act of distancing' and a serious violation of loyalty obligations under
canon law. Conversely, the Advocate General at the EuGH has suggested in her opinion that the dismissal amounts to discrimination, noting that if membership is not required for the job and the
employee has not acted against the church's ethos, unequal treatment is unjustifiable under the EU Equal Treatment Directive.\n\nPublished date: March 17 2026, 03:55\n\nURL:
https://www.zeit.de/news/2026-03/17/darf-kirchenaustritt-den-job-kosten-eu-urteil-erwartet\nImage description: A silhouette of a bird perched atop a Christian cross against an orange sunset
sky.\nSource: ZEIT ONLINE\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: Darf Kirchenaustritt den Job
kosten? EU-Urteil erwartet\n\nSummary: \nOn March 17, 2026, the Grand Chamber of the Court of Justice of the European Union (EuGH) is scheduled to deliver a ruling at 9:00 AM regarding a dispute in
Wiesbaden, Germany, where a Caritas counselor was dismissed after leaving the Catholic Church. According to the article, the dismissal occurred despite church membership not being a job requirement,
and two members of the Evangelical Church were working in the same counseling team at the time. The case questions whether a church exit can legally cost an employee their job under EU
law.\n\nPublished date: March 17 2026, 03:55\n\nURL: https://www.stern.de/gesellschaft/regional/hessen/europaeischer-gerichtshof--darf-kirchenaustritt-den-job-kosten--eu-urteil-
erwartet-37227294.html\nImage description: Silhouette of a bird perched atop a Christian cross against an orange sunset sky.\nSource: stern.de\nClassification: World\nSentiment: neutral\nReporting
voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: EU-Gerichtshof urteilt zu Kündigung nach Kirchenaustritt\n\nSummary: \nThe Grand Chamber of the Court of Justice of
the European Union (CJEU) is scheduled to rule at 9:00 AM today (March 17, 2026) on whether a church-affiliated employer can terminate an employee solely for leaving the church. The case involves a
female employee of Caritas in Wiesbaden who was dismissed after resigning from the Catholic Church, despite church membership not being a condition of her employment. At the time of her dismissal, two
other team members in the pregnancy counseling unit were not members of the Catholic Church. The outcome is expected to have significant implications for labor rights within religious organizations in
the EU.\n\nPublished date: March 17 2026, 02:30\n\nURL: https://www.stern.de/gesellschaft/regional/hessen/arbeitsrecht--eu-gerichtshof-urteilt-zu-kuendigung-nach-kirchenaustritt-37227110.html\nImage
description: Silhouette of a bird perched atop a cross against an orange sunset sky\nSource: stern.de\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent:
Europe\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: Cinco jueces decidirán si Estrasburgo revisa el fallo que respaldó la actuación del Supremo en el 'procés'\n\nSummary: \nThe European Court of
Human Rights (TEDH) will decide whether to review a previous ruling that supported the Spanish Supreme Court's handling of the 'procés' case, following a request by former Catalan leaders Oriol
Junqueras, Jordi Turull, and Jordi Sànchez. Five judges will determine if the case should be escalated to the Grand Chamber, which consists of 17 magistrates, with a decision expected by March 23. The
original ruling found no arbitrariness in the defendants' preventive detention, citing the gravity of charges including sedition and embezzlement and the risk of reoffending. The court rejected claims
that the detention was politically motivated, stating there was no persecution and that the Spanish justice system balanced the right to representation with the need to preserve constitutional order.
If the request for review is denied, the original judgments will become final.\n\nPublished date: March 16 2026, 11:32\n\nURL: https://www.abc.es/espana/cinco-jueces-decidiran-estrasburgo-revisa-
fallo-respaldo-20260316123226-nt.html\nSource: ABC ﻿TU DIARIO EN ESPAÑOL\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key:
[10]\nTitle: El fallo cuestionable contra la actualización de los créditos laborales\n\nSummary: \nA Cordoba judge, Ricardo Gileta of the Labor Chamber Sala I, issued a ruling on March 10, 2026,
declaring Article 55 of Labor Modernization Law No. 27.802 unconstitutional. The judge argued that the law's method for updating labor debts in ongoing cases violates the principle of equality by
treating 'new' and 'ongoing' cases differently. The law mandates updating debts using the Consumer Price Index (IPC) plus a 3% annual rate, a mechanism that could reduce final worker payments by
between 20% and 60% compared to previous criteria. Judge Gileta determined that the comparison circumstances are not equal, citing the 'pre and post-pandemic vicissitudes' and 'inflation crises' faced
by ongoing cases versus the 'economic stability' of new cases. Consequently, the judge ordered that credits in the specific case be updated under the original Article 276 of the Labor Contract Law.
This decision contrasts with other rulings, such as the March 9, 2026, non-final judgment in the 'González Villarroel' case (Expte. N°14052/2020), which upheld the application of the new Law 27.802
rates. The article notes that similar applications of Central Bank rates are occurring in Mendoza, Salta, Neuquén, Río Negro, and Jujuy. The author warns that while the Supreme Court has previously
set limits on excessive interest capitalization (e.g., the 'Lacuadra' ruling of August 2024), this specific ruling risks 'annihilating companies, especially SMEs' and their jobs.\n\nPublished date:
March 15 2026, 22:46\n\nURL: https://www.iprofesional.com/legales/450266-el-fallo-cuestionable-contra-la-actualizacion-de-los-creditos-laborales\nSource: Iprofesional.com\nClassification:
Politics\nSentiment: negative\nReporting voice: Analytical\nContinent: South America\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: EUR-Lex - 62024TJ0656 - EN - EUR-Lex\n\nSummary: \nOn 4 March 2026,
the General Court (Chamber giving preliminary rulings) delivered a judgment in Case T-656/24, resolving a dispute between passengers NI and HZ and the air carrier European Air Charter AG regarding
compensation for a flight delay of more than 3 hours. The incident occurred on 23 July 2022, involving a flight rotation from Düsseldorf (Germany) to Varna (Bulgaria). Due to a heavy workload and a
shortage of security staff at Cologne-Bonn Airport, the first flight in the rotation was delayed by more than 5 hours; European Air Charter AG autonomously decided to wait for passengers who had not
yet cleared security, and subsequently rescheduled the subsequent flights (including the one operated by NI and HZ) to a replacement aircraft, resulting in a 3+ hour delay for the passengers. NI and
HZ sought EUR 400 compensation each under Article 7 of Regulation (EC) No 261/2004, but the Amtsgericht Düsseldorf initially dismissed their claim. The Landgericht Düsseldorf referred the case to the
General Court to determine if the security staff shortage constituted an 'extraordinary circumstance' under Article 5(3) that exempted the carrier from compensation, specifically questioning the
causal link. The General Court ruled that while the security shortcomings may be an extraordinary circumstance, the 'autonomous decision' by the air carrier to wait for passengers, if it constitutes
the determining cause of the delay, is capable of breaking the direct causal link required to exempt the carrier from paying compensation. The Court clarified that an air carrier cannot rely on
weighing the interests of various passenger groups in a rotation to circumvent its obligation to compensate, as this would deprive passengers of the protection intended by the Regulation.\n\nPublished
date: March 09 2026, 21:13\n\nURL: https://eur-lex.europa.eu/legal-content/EN/TXT/\nSource: EUR-Lex\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent:
Europe\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: Er terskelen for tvangsmedisinering høy nok?\n\nSummary: \nAccording to a debate article published in Dagsavisen on March 09, 2026, a judgment by
the Borgarting Court of Appeal on January 30, 2026, ruled that the Norwegian state violated Articles 3 and 8 of the European Convention on Human Rights (ECHR) in a case involving forced medication and
isolation in mental health care. The case was brought by Inger-Mari Eidsvik against the state. The court found that the citizen was subjected to treatment contrary to the prohibition of inhuman and
degrading treatment and the right to personal integrity. The author argues this is not merely an 'unfortunate isolated case' but a systemic failure where legal safeguards failed, necessitating
legislative changes rather than just administrative adjustments. The article proposes three immediate measures: separating the state's role in both exercising and controlling coercion, questioning
whether the threshold for forced medication is high enough, and ensuring interventions are strictly necessary and proportionate. The author urges the Norwegian Parliament (Stortinget) to request the
government present a comprehensive review of legal security regarding coercion in mental health care, including proposals for legal amendments, and to consider reviewing ongoing forced decisions in
light of the judgment. The article emphasizes that human rights apply especially when it is difficult and that accepting weak safeguards for those deprived of liberty undermines the rule of law for
everyone.\n\nPublished date: March 09 2026, 05:07\n\nURL: https://www.dagsavisen.no/debatt/er-terskelen-for-tvangsmedisinering-hoy-nok/10239456\nSource: Dagsavisen\nClassification:
Politics\nSentiment: negative\nReporting voice: Advocacy\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [13]\nTitle: OJ C Series : 09/03/2026 (82 acts)\n\nSummary: \nOn 15 January 2026, the
Court of the European Union (Fifth Chamber) delivered a judgment in Case C-641/23, *Dubers*, resolving a request for a preliminary ruling from the Rechtbank Amsterdam in the Netherlands regarding
criminal proceedings against an individual identified as YM. The case concerns the interpretation of the European arrest warrant framework under Framework Decision 2002/584/JHA, specifically
addressing the condition of double criminality under Article 2(4), optional non-execution grounds under Article 4(1), and the surrender of a person subject to a guarantee of return to serve a
custodial sentence under Article 5(3). The judgment also examines Framework Decision 2008/909/JHA regarding the mutual recognition of criminal judgments, focusing on grounds for non-recognition and
non-enforcement due to the absence of double criminality under Article 7(3) and (4) and Article 9(1)(d), as well as the enforcement of sentences following a European arrest warrant under Article 25.
The ruling aims to balance the objectives of social rehabilitation and combating impunity within the Area of freedom, security and justice.\n\nPublished date: March 09 2026, 02:25\n\nURL: https://eur-
lex.europa.eu/oj/daily-view/C-series/default.html\nSource: EUR-Lex\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key:
[14]\nTitle: Justiça marca leitura do acórdão do processo Ajuste Secreto para outubro\n\nSummary: \nThe Espinho Judicial Court has scheduled the reading of the judgment for the 'Ajuste Secreto'
(Secret Adjustment) case for October 12, 2026, according to the collective of judges at the Tribunal Judicial de Espinho. This case involves alleged corruption concerning several former municipal
officials linked to the Oliveira de Azeméis municipal chamber. The trial, which began in November 2023 at the Tribunal de Espinho, includes 65 defendants, comprising former local officials, four
sports clubs, and their respective presidents. The defendants face charges of hundreds of crimes, including corruption, embezzlement, abuse of power, influence peddling, document forgery, breach of
secrecy, economic participation in business, prevarication, and possession of a prohibited weapon. The final defense arguments were delivered by the lawyers for Adolfo Vidal, former vice-president of
the Estarreja Chamber, and businessman Gonçalo Neves. According to the Public Ministry (Ministério Público), a prison sentence of between seven and eight years has been requested for Hermínio Loureiro
and José Oliveira 'Zito', the former president of the Oliveira de Azeméis PSD branch who was part of the municipal support office at the time.\n\nPublished date: March 08 2026, 23:17\n\nURL:
https://sapo.pt/artigo/justica-marca-leitura-do-acordao-do-processo-ajuste-secreto-para-outubro-69ae03f11de149ee796ba16b\nSource: SAPO\nClassification: Crime\nSentiment: negative\nReporting voice:
Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Vietato il prelievo forzoso sul conto corrente: la sentenza che ribalta tutto | Libero Quotidiano.it\n\nSummary: \nOn
January 8, 2026, the European Court of Human Rights (ECHR) in Strasbourg issued a judgment in the case of Ferrieri and Bonassisa v. Italy (applications nos. 40607/2019 and 34583/2020), ruling that the
Italian system allowing the Agenzia delle Entrate (Revenue Agency) to access bank data violates Article 8 of the European Convention on Human Rights, which protects the right to respect for private
and family life. The Court found that the regulations governing bank investigations under Article 32 of DPR 600/1973 (for IRPEF assessment) and Article 51 of DPR 633/1972 (for VAT) grant the tax
authority excessive discretion without sufficient procedural guarantees. Specifically, the Court criticized the lack of precise delimitation of cases, conditions, and limits for these accesses, the
absence of a mandatory and proportionate motivation requirement, and the fact that authorizations remain internal to the Agency, signed by its own directors without prior review by an independent
judicial authority. The applicants, notified by banks only after the fact, receive no advance notice and lack effective means to oppose the intrusion before irreversible effects occur, often
discovering the investigation years later during tax assessments where they face a burdensome and inverted burden of proof. While the Court did not contest the legitimacy of fighting tax evasion, it
emphasized that interference with personal data must be 'in accordance with the law,' foreseeable, and proportionate, with adequate safeguards against arbitrary abuse. The ruling mandates structural
reform in Italy, requiring clear limits, detailed motivations, effective judicial controls (preventive or ex post), and real recourse for citizens. The impact was immediate: on February 5, 2026, the
Court of Cassation issued Ordinance No. 2510/2026, which accepted the ECHR judgment in a pending tax dispute, remitting the parties to a new hearing to debate the relevance of the supranational ruling
and paving the way for potential annulments of assessments based on investigations deemed illegitimate due to lack of guarantees.\n\nPublished date: March 06 2026, 17:10\n\nURL:
https://www.liberoquotidiano.it/news/economia/46690649/prelievo-forzoso-sul-conto-corrente-la-sentenza-che-ribalta-tutto/\nSource: Quotidiano Libero\nClassification: Politics\nSentiment:
negative\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [16]\nTitle: Aferição de idade é medida de maior impacto no ECA Digital, diz representante do governo -
Notícias\n\nSummary: \nThe Digital Statute of the Child and Adolescent (ECA Digital), Law 15.211/25, is scheduled to enter into force on March 17, 2026, implementing protection measures for minors in
digital environments under the coordination of the National Data Protection Agency (ANPD). During a public hearing held on Monday, March 3, 2026, at the National Congress Social Communication Council,
Ricardo de Lins e Horta, Director of Security and Risk Prevention in the Digital Environment at the Ministry of Justice, stated that age verification is the 'measure of greatest impact' and advocated
for restrictions on access to pornography. Horta argued, 'It is inconceivable that today a child or adolescent cannot buy a can of beer in a supermarket, but can order it via a delivery app. That they
cannot buy a gun, but a website selling guns and ammunition only asks if you are over 18. And above all, the issue of pornography, which increasingly studies reveal has a brutal impact on the social,
cognitive, emotional, and sexual development of children and adolescents.' The regulation divides content into three categories: inappropriate content subject to age classification, prohibited content
for minors (such as tobacco, gambling, and pornography) requiring age verification, and illegal content for everyone (such as child sexual abuse and suicide promotion). Renata Tomaz, Adjunct Professor
at the School of Communication, Media and Information at Getulio Vargas Foundation (FGV), emphasized that for the law to be effective, it must use terminology commonly searched by Brazilians, noting
that the expression 'age verification' is searched far more frequently than 'age determination' (aferição), and 'parental control' is more common than 'parental supervision'. Rogéria Santos, President
of the Working Group on the Protection of Children and Adolescents in the Digital Environment in the Chamber of Deputies (Republicans-BA), stressed the critical need for a 'grand partnership' between
public entities, civil society, and families to ensure the protection reaches the entire population. Additionally, several projects approved by the Chamber in October 2025 to expand digital and media
education are currently under analysis in the Senate.\n\nPublished date: March 03 2026, 00:37\n\nURL: https://www.camara.leg.br/noticias/1249302-afericao-de-idade-e-medida-de-maior-impacto-no-eca-
digital-diz-representante-do-governo/\nSource: Portal da Câmara dos Deputados\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: South
America\n\n</doc>\n\n<doc>\nCitation key: [17]\nTitle: Uitspraak BRS.26.000594\n\nSummary: \nOn 27 February 2026, the Administrative Jurisdiction Division of the Council of State (Raad van State)
issued a ruling (Case No. BRS.26.000594; ECLI:NL:RVS:2026:1116) regarding the detention of an appellant by the Minister of Asylum and Migration. The Minister had ordered the appellant's detention on
18 January 2026. On 30 January 2026, the District Court of The Hague (Rotterdam session) had declared the appellant's appeal against the detention unfounded and dismissed the claim for compensation.
The appellant, represented by attorney Mr. N. van Bremen of Rotterdam, filed an appeal against this judgment. The Division ruled that the appeal does not lead to the annulment of the District Court's
judgment because the appeal petition does not contain questions that need to be answered in the interest of legal unity, legal development, or legal protection in general (Article 91, second
paragraph, of the Aliens Act 2000). The Division also saw no reason ex officio to consider the detention unlawful. Consequently, the Division confirmed the District Court's ruling and determined that
the Minister is not required to pay procedural costs. The ruling was established by Mr. B. Meijer, member of the single chamber, in the presence of Mr. T.W.A. Weber, clerk, and was published on 2
March 2026.\n\nPublished date: March 02 2026, 10:05\n\nURL: https://www.raadvanstate.nl/uitspraken/@156772/brs-26-000594/\nSource: Raad van State\nClassification: Politics\nSentiment:
negative\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [18]\nTitle: Il capo può spiare la mia email personale?\n\nSummary: \nAccording to Italian law and European
jurisprudence, an employer is almost strictly prohibited from monitoring an employee's personal email accounts, even if accessed via company devices. The article cites the European Court of Human
Rights (ECHR) and the Italian Corte di Cassazione to establish that electronic correspondence falls under the fundamental right to private life and correspondence (Article 8 of the European Convention
on Human Rights - CEDU). Specifically, the Italian Corte di Cassazione, in judgment n. 24204/2025, ruled that evidence obtained through illegal privacy violations is inadmissible in court.
Consequently, if an employer sues a former employee for unfair competition (Article 2105 of the Italian Civil Code) based solely on such illicitly obtained emails, the employer will lose the case,
even if the emails prove the employee's guilt. The judgment n. 18168/2023 further confirmed that dismissals based on illegal monitoring are void. For any control to be legal, an employer must first
implement a clear, detailed, and transparent policy communicated to all employees before monitoring begins. Controls cannot be mass, indiscriminate, or 'sweeping'; they must adhere to the principles
of necessity, proportionality, and data minimization. The only exception is the 'defensive control,' which applies only when there is a well-founded suspicion of a specific illegal act (e.g., data
theft to competitors) and must be strictly targeted at the suspected individual. The article references the landmark ECHR case Barbulescu v. Romania (Grand Chamber, 2017), which established that
firing an employee based on private chats monitored without prior notice violates Article 8 CEDU.\n\nPublished date: March 02 2026, 07:36\n\nURL: https://www.laleggepertutti.it/754856_il-capo-puo-
spiare-la-mia-email-personale\nSource: laleggepertutti\nClassification: Politics\nSentiment: neutral\nReporting voice: Explanatory\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [19]\nTitle:
Quinn Emanuel Partner Awarded Ukraine’s Order of Merit for Landmark Human Rights Case Against Russia Quinn Emanuel Partner Awarded Ukraine’s Order of Merit for Landmark Human Rights Case Against
Russia -\n\nSummary: \nOn February 27, 2026, four years after Russia's invasion of Ukraine, Quinn Emanuel partner Hughes-Jennett was awarded Ukraine's Order of Merit for her role in a landmark human
rights case against Russia, as reported by LawFuel. The award coincides with the fourth anniversary of the invasion, marking a shift where legal accountability is as critical as battlefield actions.
In July 2025, the Grand Chamber of the European Court of Human Rights (ECHR) ruled in Ukraine's favor on both admissibility and merits, a victory that cleared major hurdles for pursuing state
responsibility for systemic human rights violations. Quinn Emanuel continues to advise Ukraine as the case moves into the damages phase, where legal theory meets 'numbers, evidence and consequences.'
Hughes-Jennett attributed the honor to a collective effort by Quinn Emanuel colleagues in London, Sydney, New York, and beyond, while the Ukrainian Ministry of Justice described the award as
recognition of 'a significant personal contribution to strengthening interstate cooperation and supporting the sovereignty and territorial integrity of Ukraine.' The article notes that the Order of
Merit is rarely bestowed on practicing lawyers, signifying a moment where the legal profession intersects with history.\n\nPublished date: February 27 2026, 21:45\n\nURL:
https://www.lawfuel.com/quinn-emanuel-partner-awarded-ukraines-order-of-merit-for-landmark-human-rights-case-against-russia/\nSource: lawfuel.com\nClassification: Politics\nSentiment:
positive\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [20]\nTitle: Raporda dikkat çeken maddeler! AİHM kararları, kayyum, terör suçları...\n\nSummary: \nA draft
report prepared by a parliamentary commission in the Turkish Grand National Assembly (TBMM) under the goal of achieving a 'Turkey without terrorism' includes notable recommendations. The report
emphasizes full compliance with decisions from the European Court of Human Rights (ECHR) and the Constitutional Court (AYM), calls for the termination of the long-debated 'kayyum' (temporary
administrator) practice, and highlights the need for 'the realization of execution justice'—a reference to the widely discussed 'right to hope' in public discourse. TBMM Speaker Numan Kurtulmuş
described the report as 'a document focused on law and public conscience, not aimed at generating a perception of amnesty,' and noted that the framework proposed in the report raises the issue of the
need for a new constitution. The draft was finalized on February 18, 2026, according to the source 'Haberler'.\n\nPublished date: February 18 2026, 09:29\n\nURL:
https://www.haberler.com/politika/raporda-dikkat-ceken-maddeler-aihm-kararlari-19578915-haberi/\nSource: Haberler\nClassification: Politics\nSentiment: neutral\nReporting voice:
Explanatory\nContinent: Asia\n\n</doc>\n\n------News Summaries End------\n","offset":10,"hit_cache":false}
```

## 💭 Thinking

This is very helpful. Let me analyze what I've found:

1. From the ECHR homepage, I can see key information:
   - "On 4 and 25 March 2026 the Court will be holding two Grand Chamber hearings concerning Türkiye" - these are HEARINGS, not judgments
   - "On 23 March 2026 a panel of five judges will examine nine Grand Chamber referral requests" - these are referral requests, not judgments
   - "Forthcoming hearing: The Court will be holding a Grand Chamber hearing in the case of S.O. v. Spain on 1 April 2026" - again a HEARING
   - The forthcoming judgments listed for 19/03/2026 and 24-26/03/2026 appear to be regular chamber judgments

2. From the search results, I found that the Grand Chamber delivered landmark judgments in Ukraine and Netherlands v. Russia and Semenya v. Switzerland in July 2025, while several pending Grand Chamber cases remain unresolved—particularly the "instrumentalization" cases involving Lithuania, Latvia, and Poland pushbacks. The March-April 2026 calendar shows hearings scheduled, but these are distinct from actual judgments.

3. The question is asking about entries specifically labeled "Grand Chamber Judgment" on the Delivery of Judgments page for March 15 through April 30, 2026. There's typically a significant lag between when the Grand Chamber hears a case and when it delivers judgment—the Semenya case, for instance, had a hearing in May 2024 but the judgment didn't come until July 2025. So while hearings are happening in March-April 2026, those judgments likely won't be delivered until much later. That said, the court could be delivering Grand Chamber judgments for cases that had hearings in prior years, so I should look at what cases might be ready for judgment now.

I'm noticing from the EJIL Talk article that there are three pending Grand Chamber cases about EU-Belarus border pushbacks—C.O.C.G. and Others v. Lithuania, H.M.M. and Others v. Latvia, and R.A. and Others v. Poland—that had hearings in early 2025. Given the typical 6-18 month timeline from hearing to judgment, these could plausibly be scheduled for delivery in the March-April 2026 window.

Looking at the ECHR's judgment delivery patterns, they typically issue 10-20 Grand Chamber judgments annually, which averages to about 1-2 per month. However, the scheduled events I'm seeing for mid-March through April are mostly hearings and referral requests rather than judgment deliveries, and the ECHR usually announces forthcoming Grand Chamber judgments only a week or two in advance, so I'm not finding any confirmed scheduled deliveries yet in that timeframe.

Given the historical frequency, I'd expect roughly 1.5-2.5 Grand Chamber judgments during the March 15 - April 30 window, though they tend to cluster unpredictably. The instrumentalization cases from Lithuania, Latvia, and Poland had hearings in early 2025, putting them within the typical 12-14 month window for judgment delivery, so those could potentially be decided soon.

I should verify whether Grand Chamber judgments actually appear on the Delivery of Judgments page—they're major announcements typically covered by press releases and webcasts, so they should definitely be listed there. Let me refine my estimate using the base rate of 15-20 judgments annually.

Over the 46-day window from March 15 to April 30, that works out to roughly 1.9 to 2.5 expected judgments. Using a Poisson distribution, the probability of zero judgments during this period is about 13.5%, which means there's roughly an 86-87% chance of at least one Grand Chamber judgment appearing. But I need to look at actual historical data to verify this—I'm noticing that recent Grand Chamber judgments like Ukraine v. Russia and Semenya v. Switzerland both came down in July 2025, suggesting they might cluster around certain dates.

Looking at what I know, the base rate of 15-20 Grand Chamber judgments annually supports that 85-91% probability range. I'm also aware of several politically significant cases—the three "instrumentalization" border cases from Lithuania, Latvia, and Poland—that had hearings in early 2025 and would likely see judgments delivered by March-April 2026. The court's activity level in that timeframe suggests there's genuine momentum behind these cases. I'm working through the base rate of Grand Chamber judgments—roughly 10-20 per year—and cross-checking this against historical data, including the Ukraine v. Russia and Semenya cases from 2025, to refine my estimate for whether at least one judgment will be delivered in the March 15 to April 30 window.

The EJIL Talk article from January 5, 2026 specifically mentions three pending instrumentalization cases expected to be decided soon, and the active Grand Chamber referral requests on March 23 suggest the panel is moving forward, which pushes my confidence higher that we'll see at least one judgment in this timeframe.

Looking at the scheduled hearings more closely—there are three Grand Chamber hearings listed for March and April, but the homepage's "Forthcoming Judgments" section doesn't show any Grand Chamber decisions yet, which could mean either no judgment is imminent or the delivery dates simply haven't been announced.

Since Grand Chamber judgments typically come with advance press releases and public hearings, I should try searching the HUDOC database directly to get a better sense of how frequently these judgments are actually delivered.

## 💬 Response

Let me get more specific data on Grand Chamber judgment frequency and any pending cases.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-8423564-11921102&filename=Judgments+and+decisions+of+08.01.2026.pdf",
  "prompt": "What judgments were delivered on this date? Were any Grand Chamber judgments included? List all judgments and their types."
}
```

### 📋 Result

```
{"format": "pdf", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-8423564-11921102&filename=Judgments+and+decisions+of+08.01.2026.pdf", "pdf_path":
"/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/42647_20260320_043042/downloads/pdf/5575d75aaf55.pdf", "hint": "PDF downloaded to /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/42647_20260320_043042/downloads/pdf/5575d75aaf55.pdf. Use the Read tool to read the PDF content."}
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "ECHR Grand Chamber judgment delivered March April 2024 2025 list",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "[PDF] Forthcoming judgments and decisions - HUDOC", "url":
"https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Forthcoming+judgments+and+decisions+08-10.04.2025.pdf&id=003-8196517-11505855&library=ECHR", "snippet": "issued by the Registrar of the
Court\nECHR 083 (2025)\n01.04.2025\nForthcoming judgments and decisions\nThe European Court of Human Rights will be notifying in writing two judgments on Tuesday 8 April \n2025 and six judgments and /
or decisions on Thursday 10 April 2025.\nPress releases and texts of the judgments and decisions will be available at 10 a.m. (local time) on \nthe Court\u2019s Internet site
(www.echr.coe.int).\nTuesday 8 April 2025\nBackovi\u0107 v. Serbia (no. 2) (application no. 47600/17)\nThe applic", "highlights": ["issued by the Registrar of the Court\nECHR 083
(2025)\n01.04.2025\nForthcoming judgments and decisions The European Court of Human Rights will be notifying in writing two judgments on Tuesday 8 April 2025 and six judgments and / or decisions on
Thursday 10 April 2025. Press releases and texts of the judgments and decisions will be available at 10 a.m. (local time) on the Court\u2019s Internet site (www.echr.coe.int).\nTuesday 8 April 2025
Backovi\u0107 v. Serbia (no. 2) (application no. 47600/17) The applicant, \u010cedomir Backovi\u0107, is a Serbian national who was born in 1956 and lives in Sombor \n(Serbia).  ...    The national
courts found that his statements had intended to insult and belittle the first-instance  ...    the judiciary, and that his submissions had not been insulting.\nGreen v. the United Kingdom (no.
22077/19)  ...    Lords whose statement rendered his claim for breach of confidence against the Telegraph futile.\n2 Thursday 10 April 2025\nSahibov v. Azerbaijan (no. 43152/10) The applicant, Kamran
Isgandar oglu Sahibov, is an Azerbaijani national who was born in 1963 and \nlives in Baku. The case concerns the quashing of a first-instance judgment in the applicant\u2019s favour after it had  ...
principle of legal certainty.\nMorabito v. Italy (no. 4953/22)  ...    placement in the Section 41 bis regime despite his cognitive deterioration. The Court will give its rulings in writing on the
following cases, some of which concern issues which have already been submitted to the Court, including excessive length of proceedings. These rulings can be consulted from the day of their delivery
on the Court\u2019s online database HUDOC. They will not appear in the press release issued on that day.\nThursday 10 April 2025\nName Main application number Comunidade Israelita do Porto/Comunidade
Judaica do Porto v. Portugal 40239/23 Costa da Silva and Valadares e Sousa v. Portugal 41069/23\nCust\u00f3dia v. Portugal 37962/22\nG\u00f6z\u00fctok v. T\u00fcrkiye 41412/21 This press release is a
document produced by the Registry. It does not bind the Court. Decisions, judgments and further information about the Court can be found on www.echr.coe.int. To receive the Court\u2019s press
releases, please subscribe here: www.echr.coe.int/RSS/en or follow us on X (Twitter) @ECHR_CEDH and Bluesky @echr.coe.int.\n3\nPress contacts\nechrpress@echr.coe.int | tel.: +33 3 90 21 42 08 We are
happy to receive journalists\u2019 enquiries via either email or telephone. Tracey Turner-Tretz (tel.: + 33 3 88 41 35 30)\nDenis Lambert (tel.: + 33 3 90 21 41 09) Inci Ertekin (tel.: + 33 3 90 21 55
30)\nNeil Connolly (tel.: + 33 3 90 21 48 05)\nJane Swift (tel.: + 33 3 88 41 29 04) The European Court of Human Rights was set up in Strasbourg by the Council of Europe member States in 1959 to deal
with alleged violations of the 1950 European Convention on Human Rights."], "published_date": "2025-04-01T00:00:00.000", "score": null}, {"title": "European Court of Human Rights Delivers Three
Landmark Rulings ...", "url": "https://www.globalelr.com/2024/04/european-court-of-human-rights-delivers-three-landmark-rulings-on-climate-change/", "snippet": "European Court of Human Rights Delivers
Three Landmark Rulings on Climate Change | Environment, Land & Resources\n\nFor the first time, the Court has confirmed that the adverse impacts of climate change fall within the ambit of human rights
protection under the European Convention of Human Rights, obliging States to implement effective mitigation measures.\n\nBy Paul A. Davies, Sophie J. Lamb KC, Michael D. Green, James Bee, and
Stephanie Forrest\n\nOn 9 April 2024, the European Court of Human Rights ", "highlights": ["European Court of Human Rights Delivers Three Landmark Rulings on Climate Change | Environment, Land &
Resources For the first time, the Court has confirmed that the adverse impacts of climate change fall within the ambit of human rights protection under the European Convention of Human Rights,
obliging States to implement effective mitigation measures. By Paul A. Davies, Sophie J. Lamb KC, Michael D. Green, James Bee, and Stephanie Forrest On 9 April 2024, the European Court of Human Rights
delivered three Grand Chamber rulings in climate change-related cases. These three separate judgments are the latest in a number of climate litigation in recent years. While two of the cases were
dismissed as inadmissible on varying grounds, the Court concluded that Switzerland had breached Article 8 of the European Convention of Human Rights (ECHR) by failing to implement effective measures
to combat climate change. This development is highly likely to lead to similar challenges to governments\u2019 climate policies in the near future, and likely influence the litigation strategy of
those bringing actions against both States and companies. Read the Client Alert"], "published_date": "2024-04-11T00:00:00.000", "score": null}, {"title": "Grand Chamber of the European Court of Human
Rights issues ...", "url": "https://www.twentyessex.com/grand-chamber-of-the-european-court-of-human-rights-issues-judgment-in-ukraine-and-the-netherlands-v-russian-federation/", "snippet": "Grand
Chamber of the European Court of Human Rights issues judgment in Ukraine and The Netherlands v Russian Federation - Twenty Essex\n\n< Back To News\n\n###### 10/07/2025\n\n### Grand Chamber of the
European Court of Human Rights issues judgment in Ukraine and The Netherlands v Russian Federation\n\nOn 9 July 2025, the Grand Chamber of the European Court of Human Rights issued its judgment in a
series of inter-state cases brought by Ukraine and The Netherlands against the Russian Federation (applicat", "highlights": ["Grand Chamber of the European Court of Human Rights issues judgment in
Ukraine and The Netherlands v Russian Federation  ...    < Back To News\n\n###### 10/07/2025 ### Grand Chamber of the European Court of Human Rights issues judgment in Ukraine and The Netherlands v
Russian Federation On 9 July 2025, the Grand Chamber of the European Court of Human Rights issued its judgment in a series of inter-state cases brought by Ukraine and The Netherlands against the
Russian Federation (applications 8019/16, 43800/14, 28525/20 and 11055/22). The Court took the opportunity to \u201creflect anew on the exercise of its own jurisdiction under Article 32 to interpret
and apply the Convention and its Protocols\u201d [349]. It concluded that the Russian Federation assumed a degree of responsibility over those individuals affected by its attacks and therefore
exercised authority and control over individuals affected by its military attacks up until 16 September 2022. These individuals fell within the jurisdiction of the Russian Federation for the purposes
of Article 1 of the European Convention [361]. The Court held that the Russian Federation had violated multiple provisions of the European Convention in relation to the conflict in Ukraine in the
period between 11 May 2014 and 16 September 2022. The Court found that the question of compensation was not yet ready for decision. It noted that any future award to Ukraine would have to have due
regard to the establishment of the Register of Damages by the Council of Europe and the  ...    Lord Verdirame KC, Belinda McRae, Philippa Webb, Michal Hain, Courtney Grafton and Brendan Plant acted
for the Government of Ukraine (together with Tim Otty KC and other members of Blackstone Chambers, and Ben Emmerson KC), instructed by Quinn Emanuel Urquhart & Sullivan UK LLP. From the ECHR:
Judgment| Press release\n\n##### Relevant members Lord Verdirame KC Belinda McRae Professor Philippa Webb Michal Hain Courtney Grafton Brendan Plant Share On 9 July 2025, the Grand Chamber of the
European Court of Human Rights issued its judgment in a series\u2026 \" target=\"blank\" rel=\"noopener noreferrer\""], "published_date": "2025-10-07T00:00:00.000", "score": null}, {"title": "Grand
Chamber Judgment in Ukraine and the Netherlands v. Russia ...", "url": "https://www.ejiltalk.org/grand-chamber-judgment-in-ukraine-and-the-netherlands-v-russia-forthcoming-next-week/", "snippet":
"Grand Chamber Judgment in Ukraine and the Netherlands v. Russia Forthcoming Next Week \u2013 EJIL: Talk!\n\nJuly 3, 2025\n\n# Grand Chamber Judgment in Ukraine and the Netherlands v. Russia
Forthcoming Next Week\n\nThis is a short post to flag to readers that on Wednesday next week, 9 July, the Grand Chamber of the European Court of Human Rights will be delivering its much-anticipated
merits judgment in one of the most important interstate cases ever to be decided by that Court, Ukraine and the Netherlands", "highlights": ["Grand Chamber Judgment in Ukraine and the Netherlands v.
Russia Forthcoming Next Week \u2013 EJIL: Talk!\n\nJuly 3, 2025  ...    This is a short post to flag to readers that on Wednesday next week, 9 July, the Grand Chamber of the European Court of Human
Rights will be delivering its much-anticipated merits judgment in one of the most important interstate cases ever to be decided by that Court, Ukraine and the Netherlands v. Russia. The case concerns
hostilities in Ukraine in 2014, the downing of the MH17 airliner, and events in 2022 after the start of Russia\u2019s full-scale invasion of Ukraine, up to the point at which the Convention ceased to
apply to Russia due to its expulsion from the Council of Europe. For more background on the case, readers can consult this two-part post on the Court\u2019s admissibility decision in the case (here
and here), and this post on third party interventions in the case, including an unprecedented number of member states (26) intervening (ostensibly) in support of Ukraine. The Court\u2019s press
release announcing the delivery of the judgment, also containing a summary of the proceedings so far, can be found here. This will inevitably be a very rich judgment \u2013 whether one agrees with it
or not \u2013 on a wide range of issues, including the ECHR\u2019s extraterritorial application and the relationship between the Convention and international humanitarian law (IHL). Here are some of
the most important issues to look out for: (1) The key question remaining in the case from the standpoint of the Convention\u2019s extraterritorial application, and the notion of state jurisdiction in
Article 1 thereof, is how the Court will look at conduct of hostilities issues in the case, in particular in the light of its (rather horrible) Georgia v. Russia No. 2 judgment, in which it excluded
from the scope of the Convention state conduct th at took place in the context of active hostilities during an international armed conflict. If the Court applied GvR strictly, it would have to declare
inadmissible all possible human rights violations arising from \u2018pure\u2019 conduct of hostilities incidents, such as artillery shelling affecting civilians. Thus, the case would be limited to the
downing of the MH17 (which the Court made into something of a special case in its admissibility decision), and to incidents involving persons in the power of the enemy, such as the massacre in Bucha.
If, by contrast, the Court were to overturn GvR, it would cover the entirety of the Russian  ...    (2) The written submissions in the case provide an important window into the possible outcomes of
the case in that  ...    nominally appearing in support of Ukraine, actually argued in favour of Russia by saying, essentially, that only Bucha-type incidents but not the conduct of hostilities
scenarios should be covered. Other intervening states supported  ...    What, then, will the Court decide on this single most important outstanding issue? Obviously I have no idea. But my sense is
that it is unlikely that the Court will completely fail what I called the Mariupol test and just  ...    devastation of Mariupol, would be a human rights problem. But it\u2019s still possible that
this could happen. There seem to be three possible outcomes here: (i) the Court buys into the Anglo-French restrictive argument and follows GvR; (ii) it overturns GvR and says that all incidents in
the application are covered by the Convention \u2013 the right approach, in my view; (iii) it finds a way to rule that Ukraine (or Europe) is somehow special, so that the GvR approach should not be
followed in the Russo-Ukrainian war, but that this approach would remain valid otherwise. This third outcome is probably the likeliest, simply because the Court is wary of provoking backlash by
powerful states who do not want it to sit as a final arbiter of their uses of force in overseas conflicts. But that third outcome will also be the easiest to  ...    (3) What are the other points to
watch out for in this case? First, most importantly, how the Court will apply IHL together with the Convention, especially when it comes to operations that result in the taking of life. It will be
interesting to observe in that regard whether the Court mentions or uses some variant of the lex specialis maxim, and whether it gives any considerations to how the Convention should address mistakes
of fact during war (e.g. in targeting, as arguably happened with the MH17). Note, however, that because of Russia\u2019s non-appearance, and the lack of opposing arguments (especially those of fact),
this case is unlikely to deal with genuinely hard cases in which the rules of the Convention and IHL might go in different directions. Second, how the Court will approach derogations under Article 15
ECHR, or the lack thereof, in managing the relationship between the Convention and IHL. Third, whether the Court will say anything about Russia\u2019s aggression, and about whether ad bellum
illegality has any kind of role to play in a human rights analysis. Finally, whether the Court will discuss and apply the rules of attribution in general international law when analysing Russia\u2019s
responsibility for the conduct of pro-Russian separatists in Ukraine. ### Categories\n\n### Tags\n\n### Leave a Comment\n\nComments for this post are closed\n\n### Comments"], "published_date":
"2025-07-03T00:00:00.000", "score": null}, {"title": "[PDF] Key Cases - 2025 - ECHR-KS", "url": "https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng", "snippet": "KEY CASES\n2025\nList of
cases recommended \nby the Jurisconsult and \napproved by the Bureau\nEuropean Court of \nHuman Rights\nFebruary 2026\nNOTE\nA selection of the most important cases dealt with by the Court (also
\nreferred to as \u201ckey cases\u201d) is made quarterly by the Bureau, upon \nrecommendation by the Jurisconsult (see Title I, Chapters II and III, of \nthe Rules of Court about their respective
roles). This list contains the \nselection of key cases for 2025.\nCases are listed by reference to the rel", "highlights": ["KEY CASES\n2025\nList of cases recommended \nby the Jurisconsult and
\napproved by the Bureau\nEuropean Court of Human Rights\nFebruary 2026\nNOTE\nA selection of the most important cases dealt with by the Court (also referred to as \u201ckey cases\u201d) is made
quarterly by the Bureau, upon recommendation by the Jurisconsult (see Title I, Chapters II and III, of the Rules of Court about their respective roles). This list contains the \nselection of key cases
for 2025. Cases are listed by reference to the relevant Convention Articles and keywords, then alphabetically by respondent State and by applicant. They are also listed under the importance level
\u201cKey cases\u201d in the \nHUDOC case-law database. By default, all references are to Chamber judgments. Grand Chamber cases, whether judgments or decisions, are indicated by
\u201c[GC]\u201d.\nDecisions are indicated by \u201c(dec.)\u201d. Chamber judgments that are not yet \u201cfinal\u201d within the meaning of Article 44 of the Convention are marked \u201c(not
final)\u201d. In the event that any such judgment is accepted for referral to the Grand Chamber in accordance with Article 43, it will not be included in the present list. For information on the
manner of citing the Court\u2019s case-law, please \nsee here.\nArticle 44 \u00a7 2 \u2013 Final judgments The judgment of a Chamber shall become final\n(a) when the parties declare that they will not
request that the case be referred to the Grand Chamber; or\n(b) three months after the date of the judgment, if reference of the case to the Grand Chamber has not \nbeen requested; or (c) when the
panel of the Grand Chamber rejects the \nrequest to refer under Article 43. Article 43 \u2013 Referral to the Grand Chamber\n1. Within a period of three months from the date of the judgment  ...    2.
A panel of five judges of the Grand Chamber shall accept the  ...    3. If the panel accepts the request, the Grand Chamber shall \ndecide the case by means of a judgment.\nContents CASES BY ARTICLE
4\nCASES BY RESPONDENT STATE 16\nCASES BY APPLICANT 18\n4 Key cases 2025\nCases by Article\nARTICLE 1 JURISDICTION OF STATES\nConfinement of Tunisian national on board Italian cruise ship responsible
for returning him to Tunis following refusal-of-entry order issued by Italian authorities: jurisdiction and responsibility \nof respondent State Mansouri v. Italy (dec.) [GC], no. 63386/16, 29 April
2025\nDecision | Legal summary  ...    Ukraine and the Netherlands v. Russia [GC], nos. 43800/14 et al., \n9 July 2025 \nJudgment | Legal summary  ...    Greenpeace Nordic and Others v. Norway, no.
34068/21, \n28 October 2025\nJudgment | Legal summary\nARTICLE 35 Article 35 \u00a7 1\nEXHAUSTION OF DOMESTIC REMEDIES\nEFFECTIVE DOMESTIC REMEDY Remedies available under Italian law for Tunisian
national refused  ...    Tunis: inadmissible\nMansouri v. Italy (dec.) [GC], no. 63386/16, 29 April 2025\nDecision | Legal summary Article 35 \u00a7 3 a\nABUSE OF THE RIGHT OF APPLICATION\nHighly
reproachable conduct on the applicant\u2019s part in the Grand Chamber proceedings: preliminary objection upheld\nKova\u010devi\u0107 v. Bosnia and Herzegovina [GC], no. 43651/22, \n25 June 2025
Judgment | Legal summary\nARTICLE 41\nJUST SATISFACTION\nAward of non-pecuniary damages to applicant Government, for the benefit of identified victims of multiple Convention violations \nfound in the
principal judgment Georgia v. Russia (IV) (just satisfaction), no. 39611/18, \n14 October 2025\nJudgment | Legal summary\n14 Key cases 2025 ARTICLE 46\nArticle 46 \u00a7 2\nGENERAL MEASURES (PILOT
JUDGMENT) Respondent State to take general measures to address the Terra \ndei Fuochi pollution problem within two years from the judgment\u2019s finality\nCannavacciuolo and Others v. Italy, nos.
51567/14 et al., \n30 January 2025 Judgment | Legal summary\nEXECUTION OF JUDGMENT\nINDIVIDUAL MEASURES  ...    ARTICLE 1 OF PROTOCOL 1\nArticle 1 \u00a7 1\nPEACEFUL ENJOYMENT OF POSSESSIONS  ...
15 Key cases 2025\nARTICLE 3 OF PROTOCOL 1\nFREE EXPRESSION OF THE OPINION OF THE PEOPLE  ...    Tomenko v. Ukraine, no. 79340/16, 10 July 2025 \nJudgment | Legal summary  ...    Cases by respondent
State\nBOSNIA AND HERZEGOVINA\nKova\u010devi\u0107 v. Bosnia and Herzegovina [GC], \nno. 43651/22, 25 June 2025 Judgment | Legal summary\nCYPRUS\nGeorgios Papadopoulos v. Cyprus, \nno. 21454/21, 9
October 2025 \nJudgment| Legal summary  ...    A.R.E. v. Greece, no 15783/21, 7 January 2025 \nJudgment | Legal summary\nG.R.J"], "published_date": "2025-07-09T00:00:00.000", "score": null}, {"title":
"", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Judgments+of+04.03.2025.pdf&id=003-8170390-11459391&library=ECHR", "snippet": "issued by the Registrar of the Court\nECHR 061
(2025)\n04.03.2025\nJudgments of 4 March 2025\nThe European Court of Human Rights has today notified in writing 12 judgments1: \nthree Chamber judgments are summarised below;\nnine Committee
judgments, concerning issues which have already been examined by the Court, can \nbe consulted on Hudoc and do not appear in this press release.\nThe judgments summarised below are available only in
English.\nGirginova v. Bulgaria (application no. 4326/18) \nThe applicant", "highlights": ["issued by the Registrar of the Court\nECHR 061 (2025)\n04.03.2025\nJudgments of 4 March 2025 The European
Court of Human Rights has today notified in writing 12 judgments1: three Chamber judgments are summarised below; nine Committee judgments, concerning issues which have already been examined by the
Court, can be consulted on Hudoc and do not appear in this press release. The judgments summarised below are available only in English.\nGirginova v. Bulgaria (application no. 4326/18) The applicant,
Galina Mariova Girginova, is a Bulgarian national who was born in 1986 and lives in Sofia. She is one of the journalists at Sadebni Reportazhi, an online media organisation covering the judiciary
(https://judicialreports.bg/).  ...    Minister of Internal Affairs, Tsvetan Tsvetanov, whose criminal case for allegedly allowing unlawful  ...    Just satisfaction: The applicant did not claim any
sum in respect of pecuniary or non-pecuniary damage. The Court awarded her 2,750 euros (EUR) in respect of cost and expenses.\nK.M. v. North Macedonia (no. 59144/16) The applicant, K.M., is a
Macedonian/citizen of the Republic of North Macedonia who was born in \n1999. The case concerns the alleged failure of the State to protect K.M., a 14-year-old girl at the time, from  ...    breasts,
massaged her shoulders and told her that men loved her because she had big breasts. He \n1 Under Articles 43 and 44 of the Convention, Chamber judgments are not final. During the three-month period
following a Chamber judgment\u2019s delivery, any party may request that the case be referred to the Grand Chamber of the Court. If such a request is made, a panel of five judges considers whether the
case deserves further examination. In that event, the Grand Chamber will hear the case and deliver a final judgment. If the referral request is refused, the Chamber judgment will become final on that
day. Under Article 28 of the Convention, judgments delivered by a Committee are final. Once a judgment becomes final, it is transmitted to the Committee of Ministers of the Council of Europe for
supervision of its execution. Further information about the execution process can be found here: www.coe.int/t/dghl/monitoring/execution\n2 had not threatened her, nor had he used any force. A
criminal complaint brought by the applicant  ...    Relying on Article 1 of Protocol No. 12 (general prohibition of discrimination) to the European  ...    non-pecuniary damage: EUR 4,500\nMilashina
and Others v. Russia (no. 75000/17)  ...    which edited and published the national newspaper Novaya Gazeta. The applicant, Yelena Valeryevna Milashina, who was born in 1977, had been a staff
journalist since 1997 and was the editor in the newspaper\u2019s special projects department. The applicant, Dmitriy Andreyevich Muratov, who was born in 1961, was the chair of Novaya Gazeta\u2019s
editorial council (and its former  ...    Ressa). The applicant, Sergey Nikolayevich Kozheurov, who was born in 1955, was one of the  ...    non-pecuniary damage: EUR 7,500 to the applicant company
and EUR 9,800 to each of the individual \napplicants  ...    This press release is a document produced by the Registry. It does not bind the Court. Decisions, judgments and further information about
the Court can be found on https://www.echr.coe.int/home. To receive the Court\u2019s press releases, please subscribe here: www.echr.coe.int/RSS/en or follow us on X (Twitter) @ECHR_CEDH and Bluesky
@echr.coe.int\nPress contacts echrpress@echr.coe.int | tel.: +33 3 90 21 42 08 We are happy to receive journalists\u2019 enquiries via either email or telephone.\n3 Tracey Turner-Tretz (tel.: + 33 3
88 41 35 30)\nDenis Lambert (tel.: + 33 3 90 21 41 09) Inci Ertekin (tel.: + 33 3 90 21 55 30)\nNeil Connolly (tel.: + 33 3 90 21 48 05)\nJane Swift (tel.: + 33 3 88 41 29 04) The European Court of
Human Rights was set up in Strasbourg by the Council of Europe member States in 1959 to deal with alleged violations of the 1950 European Convention on Human Rights."], "published_date": null,
"score": null}, {"title": "BAILII - 2025 European Court of Human Rights", "url": "http://bruneis.bailii.org/cgi-bin/markup.cgi?doc=%2F%2F%2F%2F%2F%2F%2F%2F%2F%2Feu%2Fcases%2FECHR%2F2025%2Findex.html",
"snippet": "BAILII - 2025 European Court of Human Rights\n\n# European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databases>> European Court of Human Rights>> BAILII - 2025 European Court
of Human Rights URL: https://www.bailii.org//////////eu/cases/ECHR/2025/index.html\n\n---\n\n| [Home] [Databases] [World Law] [Multidatabase Search] [Help] [Feedback] [DONATE] |\n| --- |\n\n[New
search] [Contents list] [Printable version] [Help]\n\n---\n\n# 2025 European Court of Human Rights\n\n---\n\nYou are here: BAILII>> Databa", "highlights": ["2025 European Court of Human Rights URL:
https://www.bailii.org//////////eu/cases/ECHR/2025/index.html --- | [Home] [Databases] [World Law] [Multidatabase Search]  ...    [New search] [Contents list] [Printable version] [Help]\n\n--- # 2025
European Court of Human Rights\n\n--- You are here: BAILII>> Databases>> European Court of Human Rights>> 2025 European Court of Human Rights URL: https://www.bailii.org/eu/cases/ECHR/ --- | [Home]
[Databases] [World Law] [Multidatabase Search] [Help] [Feedback] [DONATE] | | --- | ### 2025 European Court of Human Rights\n\nJanuary - ZAFFERANI AND OTHERS v. SAN MARINO - 38127/22 (Article 6 -
Right to a fair trial : Fifth Section) [[2025] ECHR 10](09 January 2025) - YONCHEVA v. BULGARIA - 39127/19 (Article 6 - Right to a fair trial : Third Section) French Text [[2025] ECHR 5](07 January
2025) - VASILE PRUTEANU AND OTHERS v. ROMANIA - 9308/18 (Art 6 \ufffd 1 (criminal) and Art 6 \ufffd 3 (d) - Fair hearing - Examination of witnesses - Equality of arms - Remainder inadmissible : Fourth
Section) [[2025] ECHR 11](14  ...    - [VALEANU AND OTHERS v. ROMANIA - 59012/17 (Award for pecuniary damage sustained in relation to property confiscated  ...    - UAB PROFARMA AND UAB BONA DIAGNOSIS
v. LITHUANIA - 46264/22 (No Article 1 of Protocol No. 1 - Protection of property : Second Section) [[2025] ECHR 4](07 January 2025)  ...    French Text] [[2025] ECHR 27](23 January 2025)  ...
unaccompanied minor - Remainder inadmissible : Fifth Section) French Text] [[2025] ECHR 15](16 January 2025) February - X v. CYPRUS - 40733/22 (Article 3 - Prohibition of torture : First Section)
[[2025] ECHR 57](27 February 2025) - UKRKAVA, TOV v. UKRAINE - 10233/20 (Article 6 - Right to a fair trial : Fifth Section) [[2025] ECHR  ...    - TOTH AND CRISAN v. ROMANIA - 45430/19 (No Article 8 -
Right to respect for private and family life : Fourth  ...    Section) [[2025] ECHR 94](15 April 2025)  ...    - SYTNYK v. UKRAINE - 16497/20 (Article 6 - Right to a fair trial : Fifth Section)
[[2025] ECHR 99](24 April 2025) - SHIPS WASTE OIL COLLECTOR B.V. AND OTHERS v. THE NETHERLANDS - 2799/16 (No Article 8 - Right to respect for private and family life : Grand Chamber) [[2025] ECHR
83](01 April 2025) - SAHIBOV v. AZERBAIJAN - 43152/10 (Article 6 - Right to a fair trial - Higher courts' decisions lacking adequate reasoning : First Section) [[2025] ECHR 93](10 April 2025) - N.D.
v. SWITZERLAND - 56114/18 (Article 2 - Right to life : Fifth Section) French Text [[2025] ECHR  ...    ECHR 100](29 April 2025) May"], "published_date": null, "score": null}, {"title": "", "url":
"https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2024-eng", "snippet": "KEY CASES\n2024\nList of cases recommended \nby the Jurisconsult and \napproved by the Bureau\nEuropean Court of \nHuman
Rights\nMay 2025\nNOTE\nA selection of the most important cases dealt with by the Court (also \nreferred to as \u201ckey cases\u201d) is made quarterly by the Bureau, upon \nrecommendation by the
Jurisconsult (see Title I, Chapters II and III, of \nthe Rules of Court about their respective roles). This list contains the \nselection of key cases for 2024.\nCases are listed by reference to the
relevant", "highlights": ["KEY CASES\n2024\nList of cases recommended \nby the Jurisconsult and \napproved by the Bureau\nEuropean Court of Human Rights\nMay 2025\nNOTE\nA selection of the most
important cases dealt with by the Court (also referred to as \u201ckey cases\u201d) is made quarterly by the Bureau, upon recommendation by the Jurisconsult (see Title I, Chapters II and III, of the
Rules of Court about their respective roles). This list contains the \nselection of key cases for 2024. Cases are listed by reference to the relevant Convention Articles and keywords, then
alphabetically by respondent State and by applicant. They are also listed under the importance level \u201cKey cases\u201d in the \nHUDOC case-law database. By default, all references are to Chamber
judgments. Grand Chamber cases, whether judgments or decisions, are indicated by \u201c[GC]\u201d.\nDecisions are indicated by \u201c(dec.)\u201d. Chamber judgments that are not yet \u201cfinal\u201d
within the meaning of Article 44 of the Convention are marked \u201c(not final)\u201d. In the event that any such judgment is accepted for referral to the Grand Chamber in accordance with Article 43,
it will not be included in the present list. For information on the manner of citing the Court\u2019s case-law, please \nsee here.\nArticle 44 \u00a7 2 \u2013 Final judgments The judgment of a Chamber
shall become final\n(a) when the parties declare that they will not request that the case be referred to the Grand Chamber; or\n(b) three months after the date of the judgment, if reference of the
case to the Grand Chamber has not \nbeen requested; or (c) when the panel of the Grand Chamber rejects the \nrequest to refer under Article 43. Article 43 \u2013 Referral to the Grand Chamber\n1.
Within a period of three months from the date of the judgment  ...    2. A panel of five judges of the Grand Chamber shall accept the  ...    3. If the panel accepts the request, the Grand Chamber
shall \ndecide the case by means of a judgment.\nContents CASES BY ARTICLE 4\nCASES BY RESPONDENT STATE 14\nCASES BY APPLICANT 16\n4 Key cases 2024\nCases by Article\nARTICLE 1 RESPONSIBILITY OF
STATES\nTerritorial jurisdiction of Portugal established in respect of complaints by a group of young Portuguese concerning the harm \ncaused by climate change Lack of extraterritorial jurisdiction of
remaining respondent \nStates: inadmissible Duarte Agostinho and Others v. Portugal and 32 Others (dec.) [GC], \nno. 39371/20, 9 April 2024\nDecision | Legal summary JURISDICTION OF STATES\nFrench
jurisdiction in respect of remote retrieval of EncroChat  ...    A.L. and E.J. v. France (dec.), nos. 44715/20 and 47930/21, \n24 September 2024\nDecision | Legal summary  ...    PROCEDURE PRESCRIBED
BY LAW\nArrest and pre-trial detention of a judge serving at the United  ...    Nealon and Hallam v. the United Kingdom [GC], nos. 32483/19 and \n35049/19, 11 June 2024\nJudgment | Legal summary  ...
Crimea resulting in multiple Convention violations\nUkraine v. Russia (re Crimea) [GC], nos. 20958/14 and 38334/18,  ...    Decision | Legal summary\n12 Key cases 2024\nARTICLE 46\nArticle 46 \u00a7
2\nEXECUTION OF JUDGMENT\nINDIVIDUAL MEASURES  ...    Ukraine v. Russia (re Crimea) [GC], nos. 20958/14 and 38334/18, \n25 June 2024\nJudgment | Legal summary ARTICLE 1 OF PROTOCOL No. 1\nArticle 1
\u00a7 1\nPEACEFUL ENJOYMENT OF POSSESSIONS  ...    ARTICLE 2 OF PROTOCOL No. 4\nArticle 2 \u00a7 1\nFREEDOM OF MOVEMENT  ...    Domenjoud v. France, nos. 34749/16 and 79607/17, 16 May 2024\nJudgment
| Legal summary\n14 Key cases 2024 Cases by respondent State\nBELGIUM\nExecutief van de Moslims van Belgi\u00eb and \nOthers v. Belgium, nos. 16760/22 et al., 13 February 2024 \nJudgment | Legal
summary\nDENMARK\nDian v. Denmark (dec.), no. 44002/22, \n21 May 2024 Decision | Legal summary\nFRANCE\nA.L. and E.J. v. France (dec.), nos. 44715/20 \nand 47930/21, 24 September 2024  ...
Domenjoud v. France, nos. 34749/16 and \n79607/17, 16 May 2024 \nJudgment | Legal summary  ...    SWITZERLAND\nVerein KlimaSeniorinnen Schweiz and Others \nv. Switzerland [GC], no. 53600/20, \n9 April
2024 Judgment | Legal summary\nT\u00dcRKIYE\nAyd\u0131n Sefa Akay v. T\u00fcrkiye, no. 59/17, \n23 April 2024\nJudgment | Legal summary\nUKRAINE  ...    Nealon and Hallam v. the United Kingdom \n[GC],
nos. 32483/19 and 35049/19, \n11 June 2024\nJudgment | Legal summary  ...    Decision | Legal summary\nAyd\u0131n Sefa Akay v. T\u00fcrkiye, no. 59/17, \n23 April 2024\nJudgment | Legal summary\nB
...    17 Key cases 2024\nM\nM. A. and Others v. France, nos. 63664/19 \net al., 17 September 2024\nJudgment | Legal summary\nN Nealon and Hallam v. the United Kingdom \n[GC], nos. 324"],
"published_date": null, "score": null}, {"title": "", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Grand+Chamber+judgment+-
+multiple+violations+in+case+brought+by+Ukraine+against+Russia+concerning+Crimea.pdf&id=003-7981802-11134245&library=ECHR", "snippet": "issued by the Registrar of the Court\nECHR 166
(2024)\n25.06.2024\nMultiple violations in case brought by Ukraine against Russia concerning \nCrimea \nThe case of Ukraine v. Russia (re Crimea) (applications nos. 20958/14 and 38334/18) concerned
\nUkraine\u2019s allegations of a pattern (\u201cadministrative practice\u201d) of violations of the European \nConvention on Human Rights by the Russian Federation in Crimea beginning in February
2014. It also \nconcerned allegations of a pattern of persecution of Ukrainians f", "highlights": ["issued by the Registrar of the Court\nECHR 166 (2024)\n25.06.2024  ...    Crimea to prisons in
Russia.\nIn today\u2019s Grand Chamber judgment1 in the case the European Court of Human Rights held, unanimously, that there had been: violations of Articles 2 (right to life), 3 (prohibition of
inhuman or degrading treatment), 5 (right to liberty and security), 6 (right to a fair trial), 7 (no punishment without law), 8 (right to respect for private and family life), 9 (freedom of religion),
10 (freedom of expression), 11 (freedom of  ...    of movement) to the European Convention. It also held, unanimously, that the Russian Federation had failed to comply with its obligations under  ...
Lastly, the Court held, unanimously, under Article 46 (binding force and implementation of  ...    prisoners transferred from Crimea to penal facilities located on the territory of the Russian
\nFederation.\n*** The Court considered that it had sufficient evidence \u2013 in particular intergovernmental and non\u0002governmental  ...    1. Grand Chamber judgments are final (Article 44 of the
Convention). All final judgments are transmitted to the Committee of Ministers of the Council of Europe for supervision of their  ...    information about the execution process can be found here:
www.coe.int/t/dghl/monitoring/execution.\n2 It emphasised that such practices had taken place within the context of the full-scale application of  ...    developed and publicly promoted by prominent
representatives of the Russian authorities.\n*** Ukraine has four inter-State cases pending against Russia, including one jointly with the Netherlands, and there are approximately 7,400 individual
applications pending before the Court concerning the  ...    territory of Ukraine since 24 February 2022. See Q & A. The procedure for the processing of cases before the Court involving Russia can be
found here. A legal summary of this case will be available in the Court\u2019s database HUDOC (link).\nPrincipal facts and complaints  ...    Articles 7 and 18.\nProcedure and composition of the Court
Application no. 20958/14 originated in two applications lodged on 13 March 2014 and 26 August  ...    lodged on 10 August 2018.\nOn 7 May 2018 the Chamber dealing with application no. 20958/14
relinquished jurisdiction in favour of the Grand Chamber2.\n2. Under Article 30 of the European Convention on Human Rights, \"Where a case pending before a Chamber raises a serious question affecting
the interpretation of the Convention or the Protocols thereto, or where the resolution of a question before the Chamber might have a result inconsistent with a judgment previously delivered by the
Court, the Chamber may, at any time before it has rendered its judgment, relinquish jurisdiction in favour of the Grand Chamber, unless one of the parties to the case objects\".\n4 In its decision of
16 December 2020, the Court declared application no. 20958/14 partly admissible. It also decided to give notice to the Russian Government of the complaint in that application  ...    notice of it to
the Russian Government. Two hearings have been held in the case, on 11 September 2019 and 13 December 2023. In the first hearing the Court examined the admissibility of application no. 20958/14, while
in the second it examined the merits of the complaints already declared admissible and the admissibility and merits of the \u201cUkrainian political prisoners\u201d application (no. 38334/18) and the
transfers of \u201cconvicts\u201d complaint (both applications).\nJudgment was given by the Grand Chamber of 17 judges, composed as follows: S\u00edofra O\u2019Leary (Ireland), President,\nGeorges
Ravarani (Luxembourg),\nMarko Bo\u0161njak (Slovenia), Gabriele Kucsko-Stadlmayer (Austria),\nPere Pastor Vilanova (Andorra),\nArnfinn B\u00e5rdsen (Norway), Krzysztof Wojtyczek (Poland),\nFaris
Vehabovi\u0107 (Bosnia and Herzegovina),\nSt\u00e9phanie Mourou-Vikstr\u00f6m (Monaco), Tim Eicke (the United Kingdom),\nL\u0259tif H\u00fcseynov (Azerbaijan),\nJovan Ilievski (North Macedonia),
Gilberto Felici (San Marino),\nErik Wennerstr\u00f6m (Sweden),\nIoannis Ktistakis (Greece), Diana S\u00e2rcu (the Republic of Moldova),\nMykola Gnatovskyy (Ukraine), and also S\u00f8ren Prebensen,
Deputy Grand Chamber Registrar.\nDecision of the Court\nOverall conclusions Firstly, the Court reiterated its finding at the admissibility stage as concerned application no. 20958/14 that Russia had
exercised extraterritorial jurisdiction over Crimea between  ...    information to contradict that conclusion, the Court found that it continued to be valid after  ...    It also established"],
"published_date": null, "score": null}, {"title": "", "url": "https://hudoc.echr.coe.int/app/conversion/pdf/?filename=Judgments+and+decisions+of+29.04.2025.pdf&id=003-8216922-11543512&library=ECHR",
"snippet": "issued by the Registrar of the Court\nECHR 107 (2025)\n29.04.2025\nJudgments and decisions of 29 April 2025\nThe European Court of Human Rights has today notified in writing eight
judgments1 and one decision2:\nfive Chamber judgments are summarised below;\nthree Committee judgments, concerning issues which have already been examined by the Court, and \nthe decision, can be
consulted on Hudoc and do not appear in this press release.\nThe judgments summarised below are available only in English.\nJaupi v. ", "highlights": ["issued by the Registrar of the Court\nECHR 107
(2025)\n29.04.2025\nJudgments and decisions of 29 April 2025 The European Court of Human Rights has today notified in writing eight judgments1 and one decision2: five Chamber judgments are summarised
below; three Committee judgments, concerning issues which have already been examined by the Court, and the decision, can be consulted on Hudoc and do not appear in this press release. The judgments
summarised below are available only in English.\nJaupi v. Albania (application no. 23369/16) The applicant, Kastriot Jaupi, is an Albanian national who was born in 1975. He is currently serving a  ...
The case concerns Mr Jaupi\u2019s trial in absentia, for which he received a life sentence. He was convicted of the attempted murder of the chief of the criminal police of Berat, I.N., and his driver,
and the  ...    Relying on Article 6 \u00a7\u00a7 1 and 3 (c) and (d) (right to a fair trial) of the European Convention on Human  ...    No violation of Article 6 \u00a7\u00a7 1 and 3 (c) as regards
the applicant\u2019s right to take part in the criminal  ...    No violation of Article 6 \u00a7\u00a7 1 and 3 (d) as regards the applicant\u2019s right to question prosecution  ...    Violation of
Article 6 \u00a7\u00a7 1 and 3 (d) as regards the applicant\u2019s right to question the prosecution witnesses R.B. and B.H. in respect of his conviction for attempted murder Just satisfaction: The
Court held that the finding of a violation constituted in itself sufficient just  ...    was to pay him 1,200 euros (EUR) for costs and expenses.\nAvagyan v. Russia (no. 36911/20) The applicant,
Mariya Anatolyevna Avagyan, is a Russian national who was born in 1985 and lives in \nKrasnodar (Russia). 1 Under Articles 43 and 44 of the Convention, Chamber judgments are not final. During the
three-month period following a Chamber judgment\u2019s delivery, any party may request that the case be referred to the Grand Chamber of the Court. If such a request is made, a panel of five judges
considers whether the case deserves further examination. In that event, the Grand Chamber will hear the case and deliver a final judgment. If the referral request is refused, the Chamber judgment will
become final on that day. Under Article 28 of the Convention, judgments delivered by a Committee are final. Once a judgment becomes final, it is transmitted to the Committee of Ministers of the
Council of Europe for supervision  ...    Further information about the execution process can be found here: www.coe.int/t/dghl/monitoring/execution\n2 Inadmissibility and strike-out decisions are
final.\n2 The case concerns Ms Avagyan\u2019s conviction in 2020 for wilful dissemination of untrue information.  ...    Derrek and Others v. Russia (no. 31712/21)  ...    Kave\u010dansk\u00fd v.
Slovakia (no. 49617/22) The applicant, Vojtech Kave\u010dansk\u00fd, is a Slovak national who was born in 1979 and lives in Ko\u0161ice  ...    Mr Kave\u010dansk\u00fd. Both of these searches, and a
later search of his home, concerned alleged \nembezzlement.  ...    costs and expenses: EUR 7,580.90\nTergek v. T\u00fcrkiye (no. 39631/20)  ...    This press release is a document produced by the
Registry. It does not bind the Court. Decisions, judgments and further information about the Court can be found on https://www.echr.coe.int/home. To receive the Court\u2019s press releases, please
subscribe here: www.echr.coe.int/RSS/en or follow us on X (Twitter) @ECHR_CEDH and Bluesky @echr.coe.int.\nPress contacts\nechrpress@echr.coe.int | tel.: +33 3 90 21 42 08 We are happy to receive
journalists\u2019 enquiries via either email or telephone. Tracey Turner-Tretz (tel.: + 33 3 88 41 35 30)\nDenis Lambert (tel.: + 33 3 90 21 41 09) Inci Ertekin (tel.: + 33 3 90 21 55 30)\nNeil
Connolly (tel.: + 33 3 90 21 48 05)\nJane Swift (tel.: + 33 3 88 41 29 04) The European Court of Human Rights was set up in Strasbourg by the Council of Europe member States in 1959 to deal with
alleged violations of the 1950 European Convention on Human Rights."], "published_date": null, "score": null}]
```

```json
{
  "url": "https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng",
  "prompt": "List all Grand Chamber judgments from 2025. What were the dates of delivery? How many Grand Chamber judgments were there in total?"
}
```

### 📋 Result

```
{"format": "pdf", "url": "https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng", "pdf_path": "/home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/42647_20260320_043042/downloads/pdf/7d33d685036e.pdf", "hint": "PDF downloaded to /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/42647_20260320_043042/downloads/pdf/7d33d685036e.pdf. Use the Read tool to read the PDF content."}
```

## 💬 Response

Excellent! Now I have very rich data. Let me extract the Grand Chamber cases from the key cases lists and check the BAILII index for 2025.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "http://bruneis.bailii.org/cgi-bin/markup.cgi?doc=%2F%2F%2F%2F%2F%2F%2F%2F%2F%2Feu%2Fcases%2FECHR%2F2025%2Findex.html",
  "prompt": "List ALL Grand Chamber cases from 2025. Look for entries that say 'Grand Chamber' in their title or description. List the case name, date, and ECHR number for each one."
}
```

### 📋 Result

```
{"url": "http://bruneis.bailii.org/cgi-bin/markup.cgi?doc=%2F%2F%2F%2F%2F%2F%2F%2F%2F%2Feu%2Fcases%2FECHR%2F2025%2Findex.html", "content": "Based on the provided content, I cannot identify any Grand
Chamber cases from 2025. \n\nThe content shown appears to be just the index page structure for ECHR 2025 cases, displaying only month headings (January through December) and a reference to \"January
2026\" at the bottom. There are no actual case listings, descriptions, or any mentions of \"Grand Chamber\" in the provided text.\n\nTo find Grand Chamber cases from 2025, you would need to access the
actual content within each month's listings, which is not included in the text you've provided.\n\n**Relevant links:**\n- The content references a search functionality [New search] and month-based
organization, but no actual URLs or clickable links with case information are present in the provided text.", "title": "BAILII"}
```

```json
{
  "query": "ECHR annual report 2025 Grand Chamber judgments number statistics"
}
```

### 📋 Result

```
{"query": "ECHR annual report 2025 Grand Chamber judgments number statistics", "results": [{"title": "2025 ANNUAL REPORT E U R O P E A N C O U R T O F H U M A N R I G H T S", "url":
"https://www.echr.coe.int/documents/d/echr/annual-report-2025-eng", "snippet": null, "api_data": null, "hint": null}, {"title": "Statistics - ECHR - ECHR - ECHR / CEDH", "url":
"https://www.echr.coe.int/statistical-reports", "snippet": null, "api_data": null, "hint": null}, {"title": "HUDOC - European Court of Human Rights", "url": "https://hudoc.echr.coe.int/eng",
"snippet": "\\t\\t\\n\\t\\t\\n\\t\\t\\t\n\\n\\t\\t\\t\\t\\n\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\n\\n\\t\\t\\t\\n\\t\\t\\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\
t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t\\n\\t\\t\\t\\t \\n\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\n\\n\\n\\t\\t\\t\\t\\t\n\\t\\t\nNARROW YOUR SEARCH\n\\t\\t\\t\\n\\n\
\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t
\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t\\t\\t\\t\\t\\n\\t\\t\\t", "api_data": null, "hint": null},
{"title": "ECHR Case Law - European Human Rights - Research Guides at Columbia Law School", "url": "https://guides.law.columbia.edu/c.php?g=1306745&p=9669305", "snippet":
"[HUDOC](https://www.echr.coe.int/Pages/home.aspx?p=caselaw/HUDOC&c=) provides access to the case-law of the Court (Grand Chamber, Chamber and Committee judgments and decisions*, communicated cases,
advisory opinions and legal summaries from the Case-Law Information Note), the European Commission of Human Rights (decisions and reports) and the Committee of Ministers (resolutions). Selected
judgments of the Court, selected reports and decisions of the Commission, and settlements and resolutions of", "api_data": null, "hint": null}, {"title": "Key Cases - 2025 - ECHR-KS", "url":
"https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng", "snippet": null, "api_data": null, "hint": null}, {"title": "Annual reports - ECHR - ECHR / CEDH", "url":
"https://www.echr.coe.int/annual-reports", "snippet": null, "api_data": null, "hint": null}, {"title": "European - Human Rights Law - Library Guides at University of Melbourne", "url":
"https://unimelb.libguides.com/c.php?g=928011&p=6704319", "snippet": "The European system of human rights was created under the auspices of the Council of Europe, an intergovernmental organisation
with 46 Member States.\nThe principal regional European human rights instruments are:\n- the European Social Charter (the Charter). Forty-six Member States of the Council of Europe are parties to the
original 1961 Charter or the 1996 revised Charter.\n- the European Convention on Human Rights (ECHR).\nThe principal European bodies responsible for defining and overseeing Stat", "api_data": null,
"hint": null}, {"title": "Annual reports", "url": "https://www.echr.coe.int/pages/home.aspx?p=court/annualreports&c", "snippet": null, "api_data": null, "hint": null}, {"title": "General presentation
of the European Court of Human Rights - ECHR - ECHR / CEDH", "url": "https://www.echr.coe.int/Pages/home.aspx?p=court%2Fannualreports", "snippet": null, "api_data": null, "hint": null}, {"title":
"Analysis of statistics 2024 January 2025", "url": "https://www.echr.coe.int/documents/d/echr/stats-analysis-2024-eng", "snippet": null, "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.echr.coe.int/documents/d/echr/stats-analysis-2024-eng",
  "prompt": "How many Grand Chamber judgments were delivered in 2024? What is the total number of judgments? Provide statistics on Grand Chamber activity."
}
```

### 📋 Result

```
HTTP 403 for https://www.echr.coe.int/documents/d/echr/stats-analysis-2024-eng. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.echr.coe.int/documents/d/echr/annual-report-2025-eng",
  "prompt": "How many Grand Chamber judgments were delivered in 2025? List all Grand Chamber judgments and their dates. What is the total number of Grand Chamber judgments and decisions?"
}
```

### 📋 Result

```
HTTP 403 for https://www.echr.coe.int/documents/d/echr/annual-report-2025-eng. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 💬 Response

Let me compile the Grand Chamber judgments from the data I already have and compute the base rate.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Compile Grand Chamber judgments from the data gathered\n\n# From the Key Cases 2025 document (search results), Grand Chamber cases marked [GC]:\ngc_2025 = [\n    # From key cases 2025 list:\n    (\"Mansouri v. Italy (dec.) [GC]\", \"2025-04-29\", \"decision\"),\n    (\"Ships Waste Oil Collector B.V. and Others v. the Netherlands [GC]\", \"2025-04-01\", \"judgment\"),  # from BAILII: \"No Article 8 : Grand Chamber\"\n    (\"Kova\u010devi\u0107 v. Bosnia and Herzegovina [GC]\", \"2025-06-25\", \"judgment\"),\n    (\"Ukraine and the Netherlands v. Russia [GC]\", \"2025-07-09\", \"judgment\"),\n    (\"Semenya v. Switzerland [GC]\", \"2025-07-10\", \"judgment\"),\n    (\"Georgia v. Russia (IV) (just satisfaction)\", \"2025-10-14\", \"judgment\"),\n    # From key cases 2024 list, Ukraine v. Russia (re Crimea) was June 2024\n]\n\n# Grand Chamber cases from Key Cases 2024:\ngc_2024 = [\n    (\"Duarte Agostinho and Others v. Portugal and 32 Others (dec.) [GC]\", \"2024-04-09\", \"decision\"),\n    # Climate cases - 3 Grand Chamber rulings on April 9, 2024:\n    (\"Verein KlimaSeniorinnen Schweiz and Others v. Switzerland [GC]\", \"2024-04-09\", \"judgment\"),\n    # Car\u00eame v. France [GC] - also April 9, 2024\n    (\"Car\u00eame v. France [GC]\", \"2024-04-09\", \"judgment/decision\"),\n    (\"Nealon and Hallam v. the United Kingdom [GC]\", \"2024-06-11\", \"judgment\"),\n    (\"Ukraine v. Russia (re Crimea) [GC]\", \"2024-06-25\", \"judgment\"),\n    # A.L. and E.J. v. France (dec.) [GC] - September 2024\n    (\"A.L. and E.J. v. France (dec.) [GC]\", \"2024-09-24\", \"decision\"),\n]\n\nprint(\"=== Grand Chamber JUDGMENTS (not decisions) in 2025 ===\")\ngc_judgments_2025 = [x for x in gc_2025 if \"judgment\" in x[2]]\nfor case in gc_judgments_2025:\n    print(f\"  {case[1]}: {case[0]}\")\nprint(f\"  Total GC judgments in 2025: {len(gc_judgments_2025)}\")\n\nprint(\"\\n=== Grand Chamber items (judgments + decisions) in 2025 ===\")\nprint(f\"  Total: {len(gc_2025)}\")\n\nprint(\"\\n=== Grand Chamber JUDGMENTS in 2024 ===\")\ngc_judgments_2024 = [x for x in gc_2024 if \"judgment\" in x[2]]\nfor case in gc_judgments_2024:\n    print(f\"  {case[1]}: {case[0]}\")\nprint(f\"  Total GC judgments in 2024: {len(gc_judgments_2024)}\")\n\n# Note: These are just the KEY cases. There may be more GC judgments not in the key cases list.\n# But this gives us a lower bound.\n\nprint(\"\\n=== Monthly distribution of GC judgments 2024-2025 ===\")\nfrom collections import Counter\nmonths_24 = [x[1][:7] for x in gc_judgments_2024]\nmonths_25 = [x[1][:7] for x in gc_judgments_2025]\nall_months = months_24 + months_25\nprint(Counter(all_months))\n\nprint(\"\\n=== Checking March-April specifically ===\")\nmar_apr_gc = [x for x in gc_judgments_2024 + gc_judgments_2025 \n              if x[1][5:7] in ('03', '04')]\nprint(f\"GC judgments in March-April (2024-2025): {len(mar_apr_gc)}\")\nfor case in mar_apr_gc:\n    print(f\"  {case[1]}: {case[0]}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Grand Chamber JUDGMENTS (not decisions) in 2025 ===\n  2025-04-01: Ships Waste Oil Collector B.V. and Others v. the Netherlands [GC]\n  2025-06-25: Kova\u010devi\u0107
v. Bosnia and Herzegovina [GC]\n  2025-07-09: Ukraine and the Netherlands v. Russia [GC]\n  2025-07-10: Semenya v. Switzerland [GC]\n  2025-10-14: Georgia v. Russia (IV) (just satisfaction)\n  Total
GC judgments in 2025: 5\n\n=== Grand Chamber items (judgments + decisions) in 2025 ===\n  Total: 6\n\n=== Grand Chamber JUDGMENTS in 2024 ===\n  2024-04-09: Verein KlimaSeniorinnen Schweiz and Others
v. Switzerland [GC]\n  2024-04-09: Car\u00eame v. France [GC]\n  2024-06-11: Nealon and Hallam v. the United Kingdom [GC]\n  2024-06-25: Ukraine v. Russia (re Crimea) [GC]\n  Total GC judgments in
2024: 4\n\n=== Monthly distribution of GC judgments 2024-2025 ===\nCounter({'2024-04': 2, '2024-06': 2, '2025-07': 2, '2025-04': 1, '2025-06': 1, '2025-10': 1})\n\n=== Checking March-April
specifically ===\nGC judgments in March-April (2024-2025): 3\n  2024-04-09: Verein KlimaSeniorinnen Schweiz and Others v. Switzerland [GC]\n  2024-04-09: Car\u00eame v. France [GC]\n  2025-04-01:
Ships Waste Oil Collector B.V. and Others v. the Netherlands [GC]\n", "stderr": "", "duration_ms": 0}
```

## 💭 Thinking

Now I have a good picture. Let me compile my findings:

1. Grand Chamber judgments are relatively infrequent - about 5-10 per year based on key cases lists (though there may be more not in key cases)
2. In 2024, there were at least 4 GC judgments (April, June)
3. In 2025, there were at least 5 GC judgments (April, June, July, October)
4. In March-April specifically: 3 GC judgments across 2024-2025 (2 in April 2024, 1 in April 2025)

But wait - these are just from the "key cases" list. 

The key cases list is selective, so there could be additional Grand Chamber judgments not highlighted there. Looking at the BAILII data more carefully, I found a Ships Waste Oil Collector case from April 1, 2025 that confirms another GC judgment. The real question is how many total Grand Chamber judgments happen each year across all cases, not just the prominent ones.

From what I can see in the ECHR statistics, the Court typically delivers around 10-15 Grand Chamber judgments annually, though this varies. The 2024 and 2025 key cases lists show 6 items each, but these are curated selections. I should look at the ECHR's annual report or statistics page to get a more complete picture of the actual volume. Looking at the Key Cases 2025 list more carefully, I can identify six Grand Chamber cases so far: Mansouri v. Italy, Ships Waste Oil Collector v. Netherlands, Kovačević v. Bosnia and Herzegovina, Ukraine and the Netherlands v. Russia, Semenya v. Switzerland, and Georgia v. Russia (IV). I'm cross-referencing with the BAILII index to make sure I'm not missing any additional cases from 2025.

Now I'm thinking about the broader pattern—the ECHR typically delivers around 10-15 Grand Chamber judgments annually, but the key cases lists only capture 4-6 per year, suggesting some less prominent ones don't make the cut. For this forecast, what really matters is estimating the probability of at least one Grand Chamber judgment falling within the March 15 to April 30 window, which means I need to figure out the average frequency of these judgments throughout the year.

Using a Poisson model with different annual rates, if there are 15 judgments per year, the probability jumps to about 85% for the 46-day window; at 10 per year it's around 72%, and at 5 per year it drops to 47%. But Grand Chamber judgments don't arrive uniformly—they cluster in batches, which complicates the calculation.

What's more telling is the specific evidence I have: April 2024 saw two Grand Chamber judgments, April 2025 had one judgment and one decision, and the three instrumentalization cases (C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland) are primed for delivery soon based on the EJIL Talk article from January suggesting judgments are being prepared after their early 2025 hearings.

The question asks specifically about entries labeled "Grand Chamber Judgment" on the Delivery of Judgments page, which I can't access directly due to 403 errors. But the ECHR homepage shows scheduled judgments for mid-to-late March 2026, and the instrumentalization cases could plausibly land in that window or shortly after.

Looking at the base rates and recent patterns, I'd expect somewhere between 0.6 and 2 Grand Chamber judgments in a 46-day window, and given that April 2024 had 2 GC judgments and there are multiple pending cases with completed hearings, it seems reasonably likely at least one will be delivered by April 30. The biggest factor pushing toward YES is:
- Historical pattern: April seems to be a common month for GC judgments (April 2024: 2, April 2025: 1)
- Multiple pending cases ready for judgment delivery
- 46-day window is generous
- Active judicial period

Factors pushing toward uncertainty:
- I can't verify the current state of the Delivery of Judgments page
- GC judgment frequency might be lower than I think (only 5 per year from key cases)
- There's some probability no GC judgment falls in this specific window

Now I'm working through the probability calculations with different assumptions about annual judgment volume. At 10 judgments per year, I get about a 72% chance of at least one judgment in the 46-day window. With 7 per year, that drops to 59%, and with 15 per year it rises to 85%. The key uncertainty is pinning down the actual frequency, so let me review what I can verify about 2025 cases. I'm calculating the probability using a Poisson distribution with the observed rate of 5 judgments per year, which gives about a 47% chance of at least one more judgment in the next 46 days. But I'm realizing the key cases list might not capture all Grand Chamber judgments—it explicitly says it's "a selection of the most important cases"—so the actual rate could be higher. Historical data suggests around 10-15 GC judgments annually, which would significantly change these odds. I'm realizing the search results were incomplete, so I might be missing some 2024-2025 cases. The ECHR typically delivers 10-20 Grand Chamber judgments annually, which means I should expect around 1-2 cases in a 46-day window, giving roughly a 70% probability of seeing at least one.

But looking at the actual data from the key cases list, I'm only finding 5-7 judgments per year, which is lower than the official range. I need to reconsider whether the key cases list is truly comprehensive—the documentation suggests it includes all Grand Chamber cases since they're marked with [GC], so it should be exhaustive. Let me examine the 2024 entries more carefully to count the actual Grand Chamber cases. I'm realizing I may have missed some cases in those truncated results, so let me look for more comprehensive data. The ECHR annual statistics suggest around 8-15 Grand Chamber judgments per year, so using 10 as a baseline estimate gives me roughly a 72% probability of at least one judgment in the next 46 days. Beyond the general rate, there are those three specific instrumentalization cases from Lithuania, Latvia, and Poland that are expected to produce decisions soon, which could shift the odds higher.

But I need to be more precise about timing—the EJIL Talk article mentions the Grand Chamber preparing to deliver judgments in those cases, but doesn't specify when, and deliberations can stretch on for months. Looking at the actual ECHR data, I can see Grand Chamber hearings scheduled for early March and April, along with referral requests from late March, but I'm not seeing any judgments that have already been delivered yet.

The timeline actually makes sense though: if those hearings happened in early 2025, then 12-14 months later would put us right around March-April 2026, which falls squarely within the typical 6-18 month window from hearing to judgment. Combined with the January 2026 article saying the Grand Chamber is preparing to deliver these decisions, and given that a couple months have passed since then, there's a real possibility these judgments could come down in this timeframe.

That said, politically sensitive cases like the instrumentalization ones often face delays due to pressure from member states, so I shouldn't assume they'll follow the standard timeline. Let me try to get more concrete data on Grand Chamber judgment counts by looking at what I can piece together from HUDOC records and annual statistics, rather than relying on estimates.

Looking at 2025, I'm seeing at least 5 Grand Chamber judgments plus 1 decision, and when I cross-reference against the BAILII index, the cases are numbered sequentially with the last entry around ECHR 277 by December, which gives me a better sense of the actual volume.

So roughly 277 total ECHR cases in 2025, with 6 being Grand Chamber cases—that's about 2.2%. I think the realistic annual average for Grand Chamber judgments is probably closer to 8, accounting for cases I might have missed. Using that estimate, I'd expect around 1 Grand Chamber judgment in a 46-day window, which puts the probability of at least one at about 64%. But I need to factor in that these judgments don't distribute evenly throughout the year—they tend to cluster, and April historically has its own pattern of Grand Chamber releases. April consistently shows Grand Chamber judgments across both years, and the three instrumentalization cases pending since early 2025 could plausibly be delivered together like the climate cases were in April 2024—the EJIL Talk article suggesting imminent delivery makes this window particularly promising for a YES resolution.

Let me refine my probability estimate by being more careful about the actual frequency of Grand Chamber judgments per year, rather than relying on rough patterns. I'm working through the probability calculations with different annual judgment rates, and the estimates range from 53% to 85% depending on whether the ECHR delivers 6, 10, or 15 Grand Chamber judgments per year. Given the specific evidence about pending cases and April's historical pattern of judgments, I'm leaning toward the higher end around 85-90%, though I should also verify what exactly counts as an entry on the "Delivery of Judgments" page with that specific label.

Looking at the ECHR's upcoming announcements, I see regular chamber judgments scheduled but no Grand Chamber judgments listed yet. Grand Chamber decisions tend to get announced through separate press releases rather than the standard forthcoming judgments section, so their absence from the regular schedule doesn't tell me much. With the question window starting March 15 and only 41 days remaining through April 30, I need to estimate based on the typical annual frequency of Grand Chamber judgments.

Given that three instrumentalization cases are ready for judgment and April historically sees Grand Chamber deliveries, I should adjust my probability upward from the baseline. The fact that Grand Chamber hearings are actively happening in March and April—including cases like Tergek v. Turkey, Kavala v. Turkey No. 2, and S.O. v. Spain—suggests the court is moving cases through the system, which increases the likelihood of at least one judgment being delivered in this window.

I'm settling on around 85% as my estimate. This accounts for the base rate of roughly 70% for a 46-day window, plus a 15% upward adjustment for the pending cases, April being a typical month for Grand Chamber judgments, and the active session schedule, minus a small 5% downward adjustment for the political sensitivity of these cases and uncertainty about exact delivery timing.

Actually, I should reconsider the base rate itself. If the Grand Chamber delivers 15-20 judgments per year rather than the 5-6 I initially estimated, the baseline probability for any 46-day window would be substantially higher, which would push my final estimate even further up.

But there's a discrepancy here—my key cases data only shows 4-5 Grand Chamber judgments annually, which doesn't align with those higher figures. I'm wondering if the difference comes down to how judgments are categorized: the 15-20 figure might include decisions on inadmissibility or other procedural rulings, whereas my list focuses specifically on substantive judgments.

If I'm looking at roughly 6-10 actual Grand Chamber judgments per year, that shifts my probability estimate down to around 53-72% for a new entry within 46 days, though accounting for pending cases and historical April patterns pushes it back up to 75-85%. And since the question specifies entries before April 30, 2026, I need to make sure any judgment would be dated in March or earlier.

Given the pending instrumentalization cases, the active Grand Chamber session, and April's historical pattern for these judgments, I'm settling on 88% as my final estimate. Looking at the Key Cases 2025 data, I can see there were at least 5 Grand Chamber judgments in 2025 and 4 in 2024, with April appearing consistently as a delivery month in both years. Given the 46-day window and several pending cases with completed hearings, I'm settling on around 90% probability. Let me verify whether the ECHR specifically delivers Grand Chamber judgments in late March or April by checking the historical pattern more carefully. Now I'm running the probability calculations across different annual judgment rates using a Poisson distribution model. At 8 judgments per year, the probability drops to 64%, but it climbs to 78% at 12 per year. Given the specific evidence about pending cases and the historical pattern of April decisions, I'm adjusting upward by 10-15 percentage points, which puts me in the mid-70s range.

My final estimate lands at 88%, though I want to double-check my case counting for 2024 to make sure I'm not double-counting or miscategorizing decisions versus judgments. Looking at the case details more carefully, I can see that Duarte Agostinho was marked as a decision (inadmissible), while KlimaSeniorinnen was a judgment on the same date. The article confirms that two of the climate cases were dismissed as inadmissible decisions, so Carême was also a decision rather than a judgment. This means for 2024 I have just one Grand Chamber judgment from the April 9 climate cases.

Adding the other 2024 judgments—Nealon and Hallam in June, and Ukraine v. Russia regarding Crimea at the end of June—gives me three total for that year. Looking at 2025, I'm counting five Grand Chamber judgments across the major cases. That averages to four judgments per year, so over the next 46 days I'd expect roughly half a judgment, putting the probability of zero at about 60%.

But that calculation gives me only a 39% chance of at least one judgment, which feels too low. I need to reconsider whether the key cases list actually captures all Grand Chamber cases. The document describes itself as a selection of the most important cases, but Grand Chamber cases are inherently the most significant, so they should all be listed. The text explicitly notes that Grand Chamber cases are marked with [GC], suggesting the list is comprehensive for those.

That said, there might be edge cases—like just satisfaction judgments that are technically Grand Chamber but procedural in nature. Still, I think the key cases list is probably complete for GC judgments, even if I can't be entirely certain. Given that base rate of around 39-47%, the specific evidence about what's currently pending becomes much more important to my estimate.

The instrumentalization cases are really the crux here. The January 2026 EJIL Talk article's language about the Grand Chamber "preparing to deliver" these judgments strongly suggests they're coming within weeks to a few months—right in the Q1-Q2 2026 window. Since the question covers March 15 through April 30, that timing aligns almost perfectly with when these three cases are expected to be decided.

Now I'm calculating the probability that at least one judgment lands in that 46-day window. If I assume uniform distribution across the full January-June period, the math gives me around 58.5% for at least one case. But that's probably conservative—the "preparing to deliver" language from January suggests earlier delivery is more likely, which would push the probability higher. I should also consider whether these three cases might be delivered together, similar to how the climate cases came down in April.

For a more complete picture, I need to factor in other potential GC judgments beyond just the instrumentalization cases. If there are roughly four non-instrumentalization judgments per year, I'd expect about 0.5 in a 46-day window, giving roughly a 61% chance of none occurring. So the overall probability depends on combining the likelihood of the instrumentalization cases with the baseline rate of other judgments. Looking at the historical data on Grand Chamber judgments—around 8-12 per year based on recent records—I'm realizing my initial estimate might be too high, so let me recalibrate the probability downward to somewhere in the 60-75% range rather than 80-90%. I'm hitting dead ends trying to access the official ECHR statistics directly, so let me shift my approach and search for cached or archived versions of their recent reports instead of chasing broken links.

The key question is whether Grand Chamber judgments run closer to 5 per year based on my case data or around 10-15 based on broader references. I'll model both scenarios with equal weight: Scenario A gives roughly 47% probability of at least one judgment in 46 days, boosting to 65% with the instrumentalization factor, while Scenario B suggests 78% rising to 88%. This weighted average lands around 76%, though Scenario B seems more credible given the supporting evidence.

I'm adjusting my weights to 30% for Scenario A and 70% for Scenario B, which pushes my estimate to about 81%. Adding in the specific signals from the ECHR homepage about Grand Chamber activity and the EJIL Talk piece on instrumentalization cases being ready, I'm settling on roughly 85% as my final estimate. Though I should double-check whether a judgment might have already been issued in that March 15-19 window based on the homepage data I'm reviewing.

Looking at the ECHR schedule, the March 19 judgments were all Chamber decisions, not Grand Chamber ones, so nothing has been delivered yet in that window. That leaves me with 41 days remaining from March 20 through April 30 to work with for my probability calculation.

Running through the Poisson model at different annual rates—5, 10, and 12 judgments per year—I'm getting expected values ranging from 0.56 to 1.35, which translates to probabilities between 43% and 74%. Factoring in the instrumentalization case bonus and the typical April surge pattern adds another 15 percentage points, pushing my range to 58-89% with a central estimate around 82%.

Let me verify this against historical patterns to make sure it's reasonable. Checking back through 2024 and 2025, I want to see if there's ever been a stretch where the Court went through both March and April without issuing a Grand Chamber judgment.

Looking at the data I have, both years had at least one Grand Chamber judgment during the March-April window—2024 had one in April, and 2025 also had one in April. That's consistent with my model. The sample size is small, but it's pointing in the same direction as my calculations, so I'm feeling more confident about settling on 85%.

Now let me consider what would need to happen for there to be no Grand Chamber judgment at all during this window. The instrumentalization cases would have to stay unresolved until May or later, and no other Grand Chamber judgment could come through in the March 15 to April 30 period. That would mean the Court goes roughly 2.5 months without any Grand Chamber judgment—from mid-January through the end of April. Looking at what I know about 2025, the first judgment came on April 1, so there was already a gap in January with nothing delivered. I need to check what happened in late 2024 to see if such gaps are actually plausible. Looking at my data more carefully, the last Grand Chamber judgment I have from 2024 was Ukraine v. Russia on June 25, which means there's actually a 9-month gap until the April 1, 2025 judgment. But I suspect I'm missing cases from the second half of 2024 since my key cases list appears to be incomplete. Looking at the complete breakdown by respondent state and article, I can see there are 5 Grand Chamber judgments and 2 decisions in 2024, which gives me a clearer picture than my initial count. Comparing this to 2025's 5 judgments and 1 decision, the average works out to about 4 Grand Chamber judgments annually, so I can use that to estimate the expected number in the next 46 days.

With a base rate of 4 judgments per year, the probability of at least one judgment in that window is around 39%, but this doesn't account for the instrumentalization cases that are specifically expected to be decided in early-to-mid 2026. Given the EJIL Talk article from January strongly suggesting these are imminent, I should factor in a conditional probability—if there's roughly a 40% chance one of those cases delivers in my window and a 39% baseline for other judgments, I need to combine these probabilities to get a more accurate estimate. Working through the probability calculation, I get around 60.5% for a judgment in the next 46 days, though that assumes the instrumentalization cases have only a 35% chance of landing in this window. But given the EJIL Talk article's language about the Grand Chamber preparing to deliver these judgments, I should probably weight the timing earlier rather than later. Now I'm conditioning on the fact that delivery hasn't happened yet by March 20, so I need to recalculate using the remaining window from that date forward. If delivery is expected by end of June, that gives me a 102-day window from March 20 through June 30, with our question period covering just 41 of those days through April 30.

So the probability of instrumentalization happening in our window is about 40%. For the overall calculation, I'm combining this with the regular GC rate using a formula that accounts for both scenarios not occurring—with 4 regular GC judgments per year, I get around 61.7%, but that seems conservative. Let me check what happens if the actual rate is closer to 8 or 10 per year instead.

With higher frequencies, the probabilities climb significantly—8 per year gives me 75.6%, and 10 per year pushes it to 80.4%. So realistically I'm looking at somewhere in the 62-80% range depending on which rate assumption is correct.

There's another angle I should consider too: if those three instrumentalization cases aren't all delivered together but arrive independently, each one has that same 40% chance of falling in the window, which means there's only about a 22% chance they all miss it—so at least one landing in the window is actually more likely at 78%.

But that independence assumption probably doesn't hold; these cases are more likely to cluster together or arrive as a batch. So I should split the difference and assume a regular rate of around 6 judgments per year, with the instrumentalization cases having maybe a 50% chance of being delivered as a group.

Working through the weighted probability—half the time they come together with a 40% chance of landing in the window, half the time independently with a 78.4% chance—I get about 59% overall probability for instrumentalization in the window, which brings my final estimate down to around 79-80%. Though I'm realizing this is heavily dependent on my assumptions about clustering and delivery patterns.

Now I should check whether there are other pending GC cases I haven't accounted for yet.

Looking at the ECHR homepage, there are nine Grand Chamber referral requests being examined by a panel on March 23, 2026, which means cases are moving through the system. There are also hearings scheduled for March-April 2026 in cases like Tergek v. Turkey and Kavala v. Turkey No. 2, showing the Grand Chamber is actively working. But I don't see any press release announcing an imminent judgment delivery in the next week or two, which is unusual since they typically announce those ahead of time.

Wrapping up my analysis, I'm settling on around 85% probability for at least one Grand Chamber judgment in April. The base rate suggests 55-72% for a 41-day window depending on annual frequency, the instrumentalization cases add another 10-20% conditional probability, and April has historically been a common month for these judgments. The lack of an immediate announcement is a mild negative signal for March but doesn't really change the April outlook. Looking at 2024 data, there were three Grand Chamber judgments delivered that year, which supports this estimate. So for 2025, I'm seeing five Grand Chamber judgments from the key cases: Ships Waste Oil Collector, Kovačević, Ukraine v. Russia, Semenya, and Georgia v. Russia IV. That gives me an average of about four per year. I'm realizing the key cases list might not be exhaustive though—it explicitly says it's "a selection"—so there could be Grand Chamber judgments I'm missing. That said, it seems unlikely a Grand Chamber judgment wouldn't make it onto the key cases list, so this is probably close to the actual count.

Now I'm looking at the specific window from March 15 to April 30, 2026. With 46 days total and 5 already passed with no judgment, I have 41 days remaining. Using the base rate of 4 per year, I'd expect about 0.45 judgments in that window, which gives roughly a 36% chance of at least one. But this assumes uniform distribution, which isn't realistic—Grand Chamber judgments cluster in certain months, and April has shown up in previous years with multiple judgments.

Looking at the pattern, April had one judgment in both 2024 and 2025, while March has had none in those same years. This suggests April might be more likely than the average would indicate, though with only two data points I shouldn't overweight this. The pending cases on instrumentalization are another factor—three are expected in the first half of 2026, and we're already 2.5 months in with nothing delivered yet, which could mean they're concentrated in the remaining time.

Now I'm calculating the combined probability by considering both sources independently. The regular GC judgments have about a 36% chance in my window, leaving a 64% chance of none. The instrumentalization cases have roughly a 50-60% chance of no delivery in that same period. Multiplying these together and subtracting from 1 gives me the overall probability that at least one judgment occurs.

But I'm realizing I've probably been too conservative here. The actual judgment rate could be higher than my 4-per-year estimate, the instrumentalization cases might be closer to resolution than I'm accounting for, and April historically sees more GC judgments. I'm thinking the real probability is more like 75-80%.

There's also the complication that the ECHR likely has other pending Grand Chamber cases I'm not aware of—cases heard in 2024 or early 2025 that aren't the instrumentalization ones. The pending caseload is probably somewhere between 10-20 cases, which adds another layer of uncertainty I should factor in.

Actually, looking at the timing patterns more carefully—cases like Semenya had a hearing in May 2024 and judgment in July 2025, so cases heard in late 2024 could easily produce judgments by March or April 2026. That pushes my estimate up further. I'm settling on 85% as my final answer.

The main uncertainties are whether I'm overestimating how quickly the instrumentalization case will be decided and whether the true rate of Grand Chamber judgments is lower than my calculations suggest, but the 46-day window through April 30 is fairly generous, and with several high-profile cases pending, I feel confident in this probability.

## 💬 Response

Now let me compute the probability more carefully with the data I've gathered.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom scipy import stats\n\n# === Grand Chamber Judgment Frequency Analysis ===\n\n# From Key Cases lists (likely complete for GC):\n# 2024 GC judgments: KlimaSeniorinnen (Apr 9), Nealon & Hallam (Jun 11), Ukraine v Russia (Jun 25) = 3\n# 2024 GC decisions: Duarte Agostinho (Apr 9), Car\u00eame (Apr 9), A.L. & E.J. (Sep 24) = 3\n# 2025 GC judgments: Ships Waste Oil (Apr 1), Kova\u010devi\u0107 (Jun 25), Ukraine&NL v Russia (Jul 9), \n#                    Semenya (Jul 10), Georgia v Russia IV (Oct 14) = 5\n# 2025 GC decisions: Mansouri (Apr 29) = 1\n\ngc_judgments_per_year = [3, 5]  # 2024, 2025\nmean_gc = np.mean(gc_judgments_per_year)\nprint(f\"Mean GC judgments per year (from key cases): {mean_gc}\")\n\n# Window: March 15 - April 30, 2026 = 46 days\n# Already past March 15-19 with no GC judgment\n# Remaining: March 20 - April 30 = 41 days\nwindow_days = 46\nremaining_days = 41\n\n# === Base rate calculation (Poisson model) ===\nprint(\"\\n=== Base Rate Analysis ===\")\nfor rate in [4, 6, 8, 10, 12]:\n    expected_full = rate * window_days / 365\n    expected_remaining = rate * remaining_days / 365\n    p_at_least_one = 1 - np.exp(-expected_remaining)\n    print(f\"Rate {rate}/yr: Expected in {remaining_days}d = {expected_remaining:.2f}, P(\u22651) = {p_at_least_one:.1%}\")\n\n# === April-specific analysis ===\nprint(\"\\n=== April Pattern ===\")\n# April 2024: 1 GC judgment (KlimaSeniorinnen)\n# April 2025: 1 GC judgment (Ships Waste Oil Collector)\n# So April has had a GC judgment in 2/2 recent years\nprint(\"April had GC judgment: 2024 (1 judgment), 2025 (1 judgment) = 2/2 years\")\nprint(\"March had GC judgment: 2024 (0), 2025 (0) = 0/2 years\")\n\n# === Instrumentalization cases analysis ===\nprint(\"\\n=== Instrumentalization Cases ===\")\nprint(\"3 pending GC cases (Lithuania, Latvia, Poland) on EU-Belarus border pushbacks\")\nprint(\"Hearings held early 2025, EJIL Talk Jan 2026: 'prepares to deliver'\")\nprint(\"Not yet delivered as of March 20, 2026\")\n\n# Model: delivery expected in March-June 2026 window (after Jan article + 2.5 months passed)\n# Remaining delivery window: March 20 - June 30 = ~102 days\n# Question window: March 20 - April 30 = 41 days\ndelivery_window = 102  # days from March 20 to June 30\nquestion_window = 41\n\n# If delivered as one batch (most likely for related cases):\np_batch_in_window = question_window / delivery_window\nprint(f\"\\nP(batch delivery in window): {p_batch_in_window:.1%}\")\n\n# If delivered independently:\np_each_outside = 1 - question_window / delivery_window\np_all_outside = p_each_outside ** 3\np_any_in_window_indep = 1 - p_all_outside\nprint(f\"P(at least one independent delivery in window): {p_any_in_window_indep:.1%}\")\n\n# Weighted: 60% batch, 40% independent\np_instrum = 0.6 * p_batch_in_window + 0.4 * p_any_in_window_indep\nprint(f\"Weighted P(instrumentalization in window): {p_instrum:.1%}\")\n\n# === Combined probability ===\nprint(\"\\n=== Combined Probability ===\")\n# Use adjusted rate of 4 regular GC judgments per year (excl instrumentalization)\n# And separate instrumentalization probability\nfor base_rate in [4, 6, 8]:\n    p_no_regular = np.exp(-base_rate * remaining_days / 365)\n    p_no_instrum = 1 - p_instrum\n    p_no_gc = p_no_regular * p_no_instrum\n    p_yes = 1 - p_no_gc\n    print(f\"Base rate {base_rate}/yr: P(no regular)={p_no_regular:.3f}, P(no instrum)={p_no_instrum:.3f}, P(YES)={p_yes:.1%}\")\n\n# === Monte Carlo simulation ===\nprint(\"\\n=== Monte Carlo Simulation ===\")\nnp.random.seed(42)\nn_sim = 100000\n\n# Simulate under uncertainty about the true rate\nyes_count = 0\nfor _ in range(n_sim):\n    # Sample annual GC rate (uncertain: 4-10, centered around 6)\n    annual_rate = np.random.uniform(4, 10)\n    \n    # Regular GC judgments in 41 days\n    n_regular = np.random.poisson(annual_rate * remaining_days / 365)\n    \n    # Instrumentalization: 50% chance of delivery in window\n    # (based on expected delivery Q1-Q2 2026, conditioned on not yet delivered)\n    instrum_delivered = np.random.random() < p_instrum\n    \n    if n_regular > 0 or instrum_delivered:\n        yes_count += 1\n\np_mc = yes_count / n_sim\nprint(f\"Monte Carlo P(YES): {p_mc:.1%}\")\nprint(f\"(Based on {n_sim} simulations)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Mean GC judgments per year (from key cases): 4.0\n\n=== Base Rate Analysis ===\nRate 4/yr: Expected in 41d = 0.45, P(\u22651) = 36.2%\nRate 6/yr: Expected in 41d = 0.67,
P(\u22651) = 49.0%\nRate 8/yr: Expected in 41d = 0.90, P(\u22651) = 59.3%\nRate 10/yr: Expected in 41d = 1.12, P(\u22651) = 67.5%\nRate 12/yr: Expected in 41d = 1.35, P(\u22651) = 74.0%\n\n=== April
Pattern ===\nApril had GC judgment: 2024 (1 judgment), 2025 (1 judgment) = 2/2 years\nMarch had GC judgment: 2024 (0), 2025 (0) = 0/2 years\n\n=== Instrumentalization Cases ===\n3 pending GC cases
(Lithuania, Latvia, Poland) on EU-Belarus border pushbacks\nHearings held early 2025, EJIL Talk Jan 2026: 'prepares to deliver'\nNot yet delivered as of March 20, 2026\n\nP(batch delivery in window):
40.2%\nP(at least one independent delivery in window): 78.6%\nWeighted P(instrumentalization in window): 55.6%\n\n=== Combined Probability ===\nBase rate 4/yr: P(no regular)=0.638, P(no
instrum)=0.444, P(YES)=71.6%\nBase rate 6/yr: P(no regular)=0.510, P(no instrum)=0.444, P(YES)=77.4%\nBase rate 8/yr: P(no regular)=0.407, P(no instrum)=0.444, P(YES)=81.9%\n\n=== Monte Carlo
Simulation ===\nMonte Carlo P(YES): 79.3%\n(Based on 100000 simulations)\n", "stderr": "", "duration_ms": 1457}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also check sensitivity to the instrumentalization case assumptions\n\nprint(\"=== Sensitivity Analysis ===\\n\")\n\n# Vary instrumentalization probability\nprint(\"Varying instrumentalization case probability:\")\nfor p_i in [0.20, 0.30, 0.40, 0.50, 0.60, 0.70]:\n    base_rate = 6  # central estimate for regular GC judgments\n    p_no_regular = np.exp(-base_rate * 41 / 365)\n    p_no_gc = p_no_regular * (1 - p_i)\n    p_yes = 1 - p_no_gc\n    print(f\"  P(instrum in window) = {p_i:.0%}: P(YES) = {p_yes:.1%}\")\n\nprint(\"\\n\\nVarying base rate with fixed instrumentalization p=0.45:\")\nfor rate in range(3, 13):\n    p_no_regular = np.exp(-rate * 41 / 365)\n    p_no_gc = p_no_regular * 0.55\n    p_yes = 1 - p_no_gc\n    print(f\"  Rate {rate}/yr: P(YES) = {p_yes:.1%}\")\n\n# Also consider: the question asks about March 15 - April 30 entries\n# Not just remaining window. If a GC judgment was delivered March 15-19, \n# it would count even though we haven't found evidence of one.\n# Let's check: the ECHR homepage shows no GC judgment in forthcoming judgments\n# for March 17-19, so it's safe to say no GC judgment was delivered yet.\n\nprint(\"\\n=== Final Assessment ===\")\n# Best estimate: base rate 5-7/yr, instrumentalization P=45-55%\n# Monte Carlo gave 79.3%\n# Combined analytical: 72-82%\n# Additional factor: April has had GC judgments in 2/2 recent years\n# This suggests April-specific rate may be higher than annual average suggests\n\n# Taking into account all factors:\nfinal_p = 0.85\nprint(f\"Final probability estimate: {final_p:.0%}\")\nprint(f\"Rationale:\")\nprint(f\"  - Base rate (6/yr): P(\u22651 in 41 days) = 49%\")\nprint(f\"  - With instrumentalization cases (~50% in window): P(YES) ~77%\")\nprint(f\"  - April historical GC judgment pattern (2/2 years): +5%\")\nprint(f\"  - Active GC session, multiple pending cases: +3%\")\nprint(f\"  - Rounded to 85%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Sensitivity Analysis ===\n\nVarying instrumentalization case probability:\n  P(instrum in window) = 20%: P(YES) = 59.2%\n  P(instrum in window) = 30%: P(YES) = 64.3%\n
P(instrum in window) = 40%: P(YES) = 69.4%\n  P(instrum in window) = 50%: P(YES) = 74.5%\n  P(instrum in window) = 60%: P(YES) = 79.6%\n  P(instrum in window) = 70%: P(YES) = 84.7%\n\n\nVarying base
rate with fixed instrumentalization p=0.45:\n  Rate 3/yr: P(YES) = 60.7%\n  Rate 4/yr: P(YES) = 64.9%\n  Rate 5/yr: P(YES) = 68.6%\n  Rate 6/yr: P(YES) = 72.0%\n  Rate 7/yr: P(YES) = 74.9%\n  Rate
8/yr: P(YES) = 77.6%\n  Rate 9/yr: P(YES) = 80.0%\n  Rate 10/yr: P(YES) = 82.1%\n  Rate 11/yr: P(YES) = 84.0%\n  Rate 12/yr: P(YES) = 85.7%\n\n=== Final Assessment ===\nFinal probability estimate:
85%\nRationale:\n  - Base rate (6/yr): P(\u22651 in 41 days) = 49%\n  - With instrumentalization cases (~50% in window): P(YES) ~77%\n  - April historical GC judgment pattern (2/2 years): +5%\n  -
Active GC session, multiple pending cases: +3%\n  - Rounded to 85%\n", "stderr": "", "duration_ms": 0}
```

## 💬 Response

Now let me run the reflection checkpoint.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Base rate: ECHR delivers ~4-6 Grand Chamber judgments per year (from Key Cases 2024-2025 data). Over a 41-day remaining window, Poisson expectation gives P(\u22651) of 36-49%.",
      "logit": -0.3,
      "confidence": 0.7
    },
    {
      "description": "Three instrumentalization cases (C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland) are pending with hearings held in early 2025. EJIL Talk article from Jan 5, 2026 says Grand Chamber 'prepares to deliver' these judgments. Estimated ~50% chance at least one falls in the March 15 - April 30 window.",
      "logit": 1.5,
      "confidence": 0.6
    },
    {
      "description": "April has been a month with Grand Chamber judgments in both 2024 (KlimaSeniorinnen, April 9) and 2025 (Ships Waste Oil Collector, April 1). The question window includes all of April.",
      "logit": 0.8,
      "confidence": 0.5
    },
    {
      "description": "Grand Chamber is actively in session: hearings scheduled March 4, 25, April 1; referral panel reviewing 9 cases on March 23. Active session increases likelihood of judgment delivery.",
      "logit": 0.3,
      "confidence": 0.4
    },
    {
      "description": "No Grand Chamber judgment delivery has been announced in the 'forthcoming judgments' for the immediate future (March 17-26). GC judgments announced ~1-2 weeks before delivery. Mild negative signal for the next 2 weeks.",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "5 days of the window (March 15-19) have passed with no GC judgment delivered. This mildly reduces the remaining probability.",
      "logit": -0.1,
      "confidence": 0.8
    }
  ],
  "tentative_estimate": {
    "logit": 1.7,
    "probability": 0.85
  },
  "assessment": "The question asks whether the ECHR will list at least one Grand Chamber Judgment on its Delivery of Judgments page between March 15 and April 30, 2026. \n\n**Pro-YES arguments:**\n1. The 46-day window is generous. From the Key Cases lists, the ECHR delivers 3-5 GC judgments per year, so roughly one every 73-122 days. A 46-day window has decent odds.\n2. Three high-profile instrumentalization cases (Lithuania, Latvia, Poland border pushback cases) have completed hearings in early 2025 and are described as being ready for judgment delivery. The EJIL Talk article from January 2026 explicitly says the Grand Chamber is \"preparing to deliver\" these judgments.\n3. April has been a month when GC judgments are delivered in both 2024 and 2025 (100% hit rate in recent years).\n4. The Grand Chamber is actively in session with hearings and referral reviews, indicating an active judicial period.\n\n**Pro-NO arguments:**\n1. GC judgments are infrequent (only ~4/year from key cases data). Over 41 remaining days, the base rate probability is only 36-49%.\n2. No GC judgment delivery has been announced for the immediate future.\n3. Long gaps between GC judgments are possible (the first GC judgment of 2025 was April 1, suggesting a gap from late 2024).\n4. Politically sensitive cases (instrumentalization) could be delayed due to member state pressure on the Court.\n5. Grand Chamber deliberations can take over a year from hearing to judgment.\n\n**Counterargument to my estimate:**\nA smart disagreer might argue that I'm over-weighting the instrumentalization cases. \"Prepares to deliver\" in a January article could mean months more of drafting and finalization. GC judgments in sensitive cases often take 15-18 months from hearing, and if hearings were in January-March 2025, judgments might not come until April-September 2026. The 40-50% probability I'm assigning to instrumentalization delivery in the window could easily be 20-30%, which would bring my estimate down to ~65-70%.\n\n**Monte Carlo result:** 79.3% with uncertainty in base rate (4-10/yr uniform) and 55% instrumentalization probability.\n\nI'm setting my estimate at 85%, slightly above the MC result, reflecting the strong April pattern and the accumulation of several pending cases.",
  "calibration_notes": "Base rate: ~4-6 GC judgments per year from key cases data (2024: 3, 2025: 5). This may undercount if key cases list is not exhaustive. The often-cited 10-20 GC judgments/year may include decisions, advisory opinions, and just satisfaction judgments. Status quo: If nothing changes and no GC judgment is delivered, the question resolves NO. The status quo persistence principle suggests anchoring closer to NO, but the 46-day window is long enough that the base rate alone gives meaningful probability. Hedging check: My 85% is not a lazy 50%. It's driven by specific evidence about pending cases and historical April patterns. However, the sensitivity analysis shows the result is quite dependent on the instrumentalization case timing assumption. If those cases don't come in the window, the base rate alone gives only ~50%.",
  "key_uncertainties": "1. True annual rate of GC judgments: is it 4-6 (from key cases) or 10-15 (from general references)?\n2. Timing of instrumentalization case judgments: imminent or several more months?\n3. Whether key cases lists are exhaustive for GC items.\n4. Whether political pressure delays the instrumentalization judgments.",
  "update_triggers": "1. ECHR announces a Grand Chamber judgment delivery date \u2192 near-certain YES\n2. Instrumentalization case judgment announced \u2192 YES\n3. April passes with no GC judgment delivery \u2192 significant downward revision\n4. Reports of delayed GC deliberations \u2192 downward revision",
  "tool_audit": "Useful tools: Exa search provided rich data on GC judgments and pending cases. ECHR homepage fetch provided key info about GC hearings and forthcoming judgments. AskNews search_news provided context about ECHR activity. Monte Carlo simulation via execute_code was valuable for combining uncertain factors.\n\nTool issues: ECHR website (echr.coe.int) consistently returned 403 errors, blocking direct access to the Delivery of Judgments page, Cases Pending Before the Grand Chamber, statistics, and annual reports. This was the main limitation - I couldn't verify the current state of the resolution source directly.\n\nMissing capabilities: Direct access to HUDOC database to query Grand Chamber judgments by year would have given precise base rates. Access to ECHR statistics PDFs would have provided the exact GC judgment count.",
  "process_reflection": "The main friction was the ECHR website blocking access (403 errors). This forced me to rely on secondary sources (BAILII, Exa, press releases) rather than the primary resolution source. The search tools worked well for finding academic commentary (EJIL Talk) and cached content.\n\nThe base rate estimation was challenging because the Key Cases lists may not be exhaustive, creating uncertainty about whether the GC delivers 4 or 10+ judgments per year. This is a significant source of uncertainty that I couldn't resolve without access to ECHR statistics.\n\nThe decomposition approach (separating regular GC judgments from instrumentalization cases) was helpful for reasoning about the problem. The Monte Carlo simulation combined multiple sources of uncertainty effectively."
}
```

### 📋 Result

```
{"factor_count": 6, "factor_sum": 0.98, "tentative_logit": 1.7, "logit_gap": 0.72, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Base rate: ECHR delivers ~4-6 Grand Chamber
judgments per year (from Key Cases 2024-2025 data). Over a 41-day remaining window, Poisson expectation gives P(\u22651) of 36-49%.", "logit": -0.3, "confidence": 0.7, "effective_logit": -0.21},
{"description": "Three instrumentalization cases (C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland) are pending with hearings held in early 2025. EJIL Talk article from Jan 5, 2026 says Grand
Chamber 'prepares to deliver' these judgments. Estimated ~50% chance at least one falls in the March 15 - April 30 window.", "logit": 1.5, "confidence": 0.6, "effective_logit": 0.8999999999999999},
{"description": "April has been a month with Grand Chamber judgments in both 2024 (KlimaSeniorinnen, April 9) and 2025 (Ships Waste Oil Collector, April 1). The question window includes all of
April.", "logit": 0.8, "confidence": 0.5, "effective_logit": 0.4}, {"description": "Grand Chamber is actively in session: hearings scheduled March 4, 25, April 1; referral panel reviewing 9 cases on
March 23. Active session increases likelihood of judgment delivery.", "logit": 0.3, "confidence": 0.4, "effective_logit": 0.12}, {"description": "No Grand Chamber judgment delivery has been announced
in the 'forthcoming judgments' for the immediate future (March 17-26). GC judgments announced ~1-2 weeks before delivery. Mild negative signal for the next 2 weeks.", "logit": -0.3, "confidence": 0.5,
"effective_logit": -0.15}, {"description": "5 days of the window (March 15-19) have passed with no GC judgment delivered. This mildly reduces the remaining probability.", "logit": -0.1, "confidence":
0.8, "effective_logit": -0.08000000000000002}], "dominant_factor": "Three instrumentalization cases (C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland) are pending with hearings held in early
2025. EJIL Talk article from Jan 5, 2026 says Grand Chamber 'prepares to deliver' these judgments. Estimated ~50% chance at least one falls in the March 15 - April 30 window.",
"dominant_effective_logit": 0.8999999999999999, "factor_implied_probability": 0.7271082163411295, "tentative_probability": 0.85, "gap_pp": 12.289178365887043, "sources": ["[(Metaculus) Will the
European Court of Human Rights list at least one entry labeled \u201cGrand Chamber Judgment\u201d on its Delivery of Judgments page?](https://www.metaculus.com/questions/42647)", "[Delivery of
judgments - ECHR Hearings - ECHR - ECHR / CEDH](https://www.echr.coe.int/delivery-of-judgments)", "[Forthcoming delivery](https://www.echr.coe.int/w/forthcoming-delivery-12)", "[Cases pending before
the Grand Chamber - ECHR Hearings - ECHR - ECHR / CEDH](https://www.echr.coe.int/cases-pending-before-the-grand-chamber)", "[European Court of Human Rights -
Wikipedia](https://en.wikipedia.org/wiki/European_Court_of_Human_Rights)",
"[hudoc.echr.coe.int](https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=003-8423564-11921102&filename=Judgments+and+decisions+of+08.01.2026.pdf)",
"[ks.echr.coe.int](https://ks.echr.coe.int/documents/d/echr-ks/key-cases-2025-eng)", "[BAILII](http://bruneis.bailii.org/cgi-
bin/markup.cgi?doc=%2F%2F%2F%2F%2F%2F%2F%2F%2F%2Feu%2Fcases%2FECHR%2F2025%2Findex.html)", "[echr.coe.int](https://www.echr.coe.int/documents/d/echr/stats-analysis-2024-eng)",
"[echr.coe.int](https://www.echr.coe.int/documents/d/echr/annual-report-2025-eng)"], "reviewer_critique": "## Verification Summary\n\nI reviewed the agent's full research trace to verify factual
claims in the factors.\n\n### Factor-by-Factor Verification\n\n**Factor 1 (Base rate: ~4-6 GC judgments/year):** \u2713 SUPPORTED\n- Trace shows agent computed \"Mean GC judgments per year (from key
cases): 4.0\" based on 3 GC judgments in 2024 and 5 in 2025\n- The factor's \"4-6\" range accurately reflects the trace evidence\n\n**Factor 2 (Instrumentalization cases + EJIL Talk article):** \u2713
SUPPORTED\n- Trace contains the EJIL Talk article from January 5, 2026 with exact quote: \"As the Grand Chamber **prepares to deliver** its judgments in the three instrumentalization cases\"\n- Cases
correctly identified: C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland\n- Article states \"hearings in early 2025\" - confirmed in trace\n\n**Factor 3 (April historical pattern):** \u2713
SUPPORTED\n- Trace confirms: KlimaSeniorinnen delivered April 9, 2024; Ships Waste Oil Collector delivered April 1, 2025\n- Agent's calculation: \"April had GC judgment: 2024 (1 judgment), 2025 (1
judgment) = 2/2 years\"\n\n**Factor 4 (Active Grand Chamber session):** \u2713 SUPPORTED\n- Trace shows ECHR homepage: Grand Chamber hearings March 4, 25 (Tergek, Kavala No. 2), April 1 (S.O. v.
Spain)\n- \"On 23 March 2026 a panel of five judges will examine nine Grand Chamber referral requests\"\n\n**Factor 5 (No GC judgment in forthcoming announcements):** \u2713 SUPPORTED\n- Trace shows
March 17-19 forthcoming judgments were all Chamber judgments\n\n**Factor 6 (5 days passed with no GC judgment):** \u2713 SUPPORTED\n- Agent verified no GC judgment delivered March 15-19\n\n### Double-
Counting Check\nNo double-counting detected. The factors draw on distinct evidence: Factor 1 (base rate calculation), Factor 2 (specific pending cases), Factor 3 (seasonal pattern), Factor 4 (current
activity), Factor 5 (near-term negative signal), Factor 6 (time elapsed).\n\n### Resolution Criteria Alignment\nThe agent correctly focused on \"Grand Chamber Judgment\" entries on the Delivery of
Judgments page, distinguishing from decisions, hearings, and press releases per the fine print. The agent noted 403 errors accessing the delivery page directly but used alternative sources
appropriately.\n\n### Adversarial Reasoning\nThe assessment explicitly engages counterarguments: (1) long deliberation times for politically sensitive cases, (2) \"prepares to deliver\" could mean
months more, (3) only 36-49% base rate probability. This satisfies the adversarial reasoning requirement.\n\n### Probability Assessment\n- Monte Carlo simulation: 79.3%\n- Agent's final estimate:
85%\n- Agent added ~6% for April patterns and active session\n\nThe 85% is at the higher end of the plausible range. The sensitivity analysis shows:\n- At 50% instrumentalization probability + 6/yr
base rate: P(YES) = 74.5%\n- At 60% instrumentalization probability: P(YES) = 79.6%\n- At 70% instrumentalization probability: P(YES) = 84.7%\n\nThe agent's 55.6% weighted instrumentalization
probability is reasonable given the \"prepares to deliver\" language from January. The +6% adjustment for April patterns and active session is a judgment call but defensible given 2/2 recent years
having April GC judgments.\n\nMy independent estimate would be ~78-82%, slightly below the agent's 85%, but not meaningfully different given uncertainty. The agent's reasoning is coherent and
evidence-based, and the gap doesn't constitute a clear error that would change the forecast direction."}
```

## 💬 Response

The reflection reviewer approved with a note that 78-82% might be slightly more accurate than 85%. Let me adjust slightly downward to 82%, which splits the difference between my Monte Carlo result (79.3%) and my initial judgment (85%).

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "The question asks whether the ECHR's Delivery of Judgments page will show at least one entry labeled \"Grand Chamber Judgment\" dated March 15 - April 30, 2026. From Key Cases data, the ECHR delivers ~4-6 Grand Chamber judgments per year, giving a base rate of ~36-49% for a 41-day remaining window. However, three high-profile instrumentalization cases (Lithuania, Latvia, Poland) are pending with hearings completed in early 2025, and an EJIL Talk article from January 2026 says the Grand Chamber is \"preparing to deliver\" these judgments. April has had Grand Chamber judgments in both 2024 and 2025. The Grand Chamber is actively in session with hearings and referral reviews. Monte Carlo simulation combining uncertain base rates (4-10/yr) and instrumentalization case delivery (~50% in window) yields 79.3%. Adjusting upward for April patterns gives ~82%.",
  "logit": 1.5,
  "probability": 0.82,
  "factors": [
    {
      "description": "Base rate: ECHR delivers ~4-6 Grand Chamber judgments per year (from Key Cases 2024-2025 data: 3 in 2024, 5 in 2025). Over 41 remaining days, Poisson model gives P(\u22651) of 36-49%.",
      "logit": -0.3,
      "confidence": 0.7
    },
    {
      "description": "Three instrumentalization cases (C.O.C.G. v. Lithuania, H.M.M. v. Latvia, R.A. v. Poland) pending with hearings held early 2025. EJIL Talk article (Jan 5, 2026) says Grand Chamber 'prepares to deliver' these judgments. Estimated ~50% chance at least one falls in the question window.",
      "logit": 1.5,
      "confidence": 0.6
    },
    {
      "description": "April has had Grand Chamber judgments in both 2024 (KlimaSeniorinnen, April 9) and 2025 (Ships Waste Oil Collector, April 1). Question window includes all of April - 2/2 recent years show GC judgments in April.",
      "logit": 0.8,
      "confidence": 0.5
    },
    {
      "description": "Grand Chamber is actively in session: hearings scheduled March 4, 25, April 1; referral panel reviewing 9 cases on March 23. Active session increases likelihood of concurrent judgment delivery.",
      "logit": 0.3,
      "confidence": 0.4
    },
    {
      "description": "No Grand Chamber judgment delivery announced in forthcoming judgments for March 17-26. GC judgments typically announced 1-2 weeks before delivery. Mild negative signal for late March.",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "5 days of window already passed (March 15-19) with no GC judgment. Mildly reduces remaining probability.",
      "logit": -0.1,
      "confidence": 0.8
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**Forecast: 0.82 (82% probability of YES)**

Key reasoning:

- **Base rate (moderate negative):** The ECHR delivers only ~4-6 Grand Chamber judgments per year based on Key Cases lists (3 in 2024, 5 in 2025). Over the remaining 41-day window, a Poisson model gives just 36-49% probability for at least one.

- **Pending instrumentalization cases (strong positive):** Three high-profile Grand Chamber cases on EU-Belarus border pushbacks had hearings in early 2025. An EJIL Talk article from January 2026 explicitly states the Grand Chamber is "preparing to deliver" these judgments. Estimated ~50% chance at least one falls within the window.

- **April pattern (moderate positive):** April had Grand Chamber judgments in both 2024 (KlimaSeniorinnen, April 9) and 2025 (Ships Waste Oil Collector, April 1). The question window covers all of April.

- **Monte Carlo result:** Simulation combining uncertain base rates and instrumentalization timing gives 79.3%. After adjusting for the April pattern and active GC session, final estimate is 82%.
