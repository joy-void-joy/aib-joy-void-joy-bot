# Reasoning Log: Will the Polish Senate vote on the Crypto-Assets Market Act (druk 2529) before May 31, 2026?

*Generated: 2026-05-22T01:18:57.040991+00:00*


## 💭 Thinking

Let me analyze this question about the Polish Senate voting on the Crypto-Assets Market Act before May 31, 2026.

Key facts:
1. The Sejm passed the bill on May 15, 2026
2. The Senate has 30 days to act (deadline mid-June 2026)
3. As of May 17, 2026, no Senate plenary vote scheduled yet
4. Today is May 22, 2026
5. The question resolves by May 30, 2026 (scheduled_resolve_time)
6. The question asks if the Senate votes before May 31, 2026

So the question is: will the Senate vote within ~8-9 days of today (by May 30)?


The MiCA transitional period ending July 1 creates some pressure to move quickly, but constitutionally the Senate has until mid-June, so there's no hard deadline forcing a vote before May 31. I should look into the current status and how quickly the Polish Senate typically processes legislation.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43562
  ]
}
```

### 📋 Result

```
{"post_id": 43562, "title": "Will the Polish Senate vote on the Crypto-Assets Market Act (druk 2529) before May 31, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43562",
"background_info": "Poland's **Crypto-Assets Market Act** (ustawa o rynku kryptoaktyw\u00f3w) is the national bill implementing the EU's [Markets in Crypto-Assets Regulation
(MiCA)](https://en.wikipedia.org/wiki/Markets_in_Crypto-Assets), designating the [Polish Financial Supervision Authority (KNF)](https://en.wikipedia.org/wiki/Polish_Financial_Supervision_Authority) as
the competent national supervisor for crypto-asset service providers.\n\nThe bill has had a contentious legislative history. President Karol Nawrocki vetoed the first version on December 1, 2025, and
vetoed a second version in February 2026. A Sejm override attempt failed (243 votes versus the 276 required for the constitutional 3/5 supermajority). On May 15, 2026, the Sejm passed a third version
of the Act (government bill, druk 2529) by 241\u2013200, rejecting most of President Nawrocki's proposed amendments while accepting one (an annual KNF/Ministry of Finance reporting obligation).
Minister Bogucki has signaled that a third presidential veto is likely.\n\nUnder the Polish Constitution, the [Senate](https://en.wikipedia.org/wiki/Senate_of_Poland) has up to 30 days from receiving
a bill from the Sejm to adopt it without amendments, adopt it with amendments, or reject it; the Senate may schedule a plenary vote much sooner. The bill was passed by the Sejm on May 15, 2026, so the
Senate's deadline falls in mid-June 2026. However, the MiCA transitional period for Polish crypto-asset firms registered under the RDWW register expires July 1, 2026, creating significant pressure for
the Senate to act quickly. As of May 17, 2026, the Senate has not yet publicly scheduled a plenary vote on the bill.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 4,
\"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves **YES** if, before May 31, 2026 (Europe/Warsaw time), the Polish Senate holds a plenary
vote on the Crypto-Assets Market Act passed by the Sejm on May 15, 2026 (Sejm druk 2529) \u2014 whether the Senate adopts the bill without amendments, adopts it with amendments, or rejects it. It
resolves **NO** if no such Senate plenary vote has occurred by that date.\n\nThe primary resolution source is the Sejm's official process tracker for druk 2529:
https://www.sejm.gov.pl/sejm10.nsf/PrzebiegProc.xsp?nr=2529 \u2014 which records the date and outcome of Senate action on bills passed by the Sejm. The Senate's own legislative process portal at
https://www.senat.gov.pl may also be consulted. If neither source is accessible, reporting by [credible sources](https://www.metaculus.com/faq/#definitions) confirming the Senate plenary vote and its
date will be used.", "fine_print": "Committee votes within the Senate do not count toward resolution; only a plenary vote of the full Senate counts. A formal Senate resolution not to introduce
objections (\"uchwa\u0142a o nie wnoszeniu zastrze\u017ce\u0144\") adopted in plenary counts as a vote. If the Senate takes no action and the 30-day constitutional deadline lapses without a plenary
vote (which would deem the bill adopted by operation of law), this is NOT a \"vote\" and the question resolves NO.", "num_forecasters": 2, "community_prediction": null}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Polish Senate schedule Crypto-Assets Market Act druk 2529 May 2026, when is the plenary vote scheduled?",
      "ttl": "6h"
    },
    {
      "query": "How quickly does the Polish Senate typically vote on bills passed by the Sejm? What is the typical turnaround time? Senate of Poland legislative process speed",
      "ttl": "7d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Polish Senate schedule Crypto-Assets Market Act druk 2529 May 2026, when is the plenary vote scheduled?", "entry": {"slug": "polish-senate-schedule-crypto-assets-market-act-
dr-73274c82", "query": "Polish Senate schedule Crypto-Assets Market Act druk 2529 May 2026, when is the plenary vote scheduled?", "answer": "## Research Report: Polish Senate \u2013 Crypto-Assets
Market Act (Druk 2529) \u2013 May 2026\n\n**Important caveat:** All web search and URL-fetching tools are unavailable in this session, so I was unable to retrieve live data from the Polish
parliamentary websites or news sources. Below is what I can report based on background knowledge and reasoning, along with direct pointers for verification.\n\n---\n\n### Background Context\n\n-
**Druk 2529** refers to a Sejm (lower house) print number for the *ustawa o rynku kryptoaktyw\u00f3w* (Crypto-Assets Market Act), which is Poland's national legislation complementing the EU's **MiCA
Regulation** (Regulation 2023/1114).\n- The act designates the **KNF** (Polish Financial Supervision Authority) as the national competent authority, establishes transitional provisions for existing
crypto-asset service providers, and sets administrative penalties.\n- MiCA's main provisions applied from **30 December 2024**, meaning Poland's implementing legislation is already significantly
delayed if it is still in the Senate in May 2026.\n\n### Senate Procedure (Constitutional Framework)\n\n- Once the Sejm passes a bill and transmits it to the Senate, the Senate has a **30-day
constitutional deadline** to act (accept, amend, or reject).\n- The bill is typically referred to the **Komisja Bud\u017cetu i Finans\u00f3w Publicznych** (Budget and Public Finance Committee), and
possibly the **Komisja Ustawodawcza** (Legislative Committee).\n- After committee deliberation, the full Senate votes in **plenary session**. The Senate typically holds 2\u20133 day plenary sessions
roughly every two weeks.\n\n### What I Could NOT Verify\n\n| Item | Status |\n|------|--------|\n| Exact plenary vote date in May 2026 | \u274c Unable to retrieve |\n| Senate druk (print) number
assigned | \u274c Unable to retrieve |\n| Committee hearing dates | \u274c Unable to retrieve |\n| Date the Sejm transmitted the bill to the Senate | \u274c Unable to retrieve |\n\n### Direct Sources
to Check\n\n1. **Senate plenary schedule**: `https://www.senat.gov.pl/prace/senat/posiedzenia/` \u2014 lists upcoming session dates and agendas\n2. **Senate legislative tracker**:
`https://www.senat.gov.pl/prace/proces-legislacyjny-w-senacie/` \u2014 search for \"kryptoaktyw\" or the Senate druk number\n3. **Sejm legislative tracker**:
`https://www.sejm.gov.pl/sejm10.nsf/druk.xsp?nr=2529` \u2014 full bill history including Senate transmission date\n4. **KNF website**: `https://www.knf.gov.pl/` \u2014 regulator statements on MiCA
implementation\n\n### Key Reasoning\n\nIf druk 2529 was transmitted to the Senate in late April or early May 2026, the 30-day deadline would place the plenary vote in **late May or early June 2026**.
The Senate's May 2026 plenary sessions (typically held mid-month and end-of-month) would be the likely windows. However, without live access to the parliamentary calendar, I cannot confirm the
specific date.\n\n---", "sources": [{"url": "https://www.senat.gov.pl/prace/senat/posiedzenia/", "title": "Polish Senate Plenary Sessions Schedule", "domain": "senat.gov.pl", "accessed_at":
"2026-05-22T00:00:00Z", "snippet": "NOT ACCESSED - tool unavailable. This is the primary source for Senate plenary session dates and agendas."}, {"url": "https://www.senat.gov.pl/prace/proces-
legislacyjny-w-senacie/", "title": "Polish Senate Legislative Process Tracker", "domain": "senat.gov.pl", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "NOT ACCESSED - tool unavailable. This
tracker would show the status of druk 2529 in the Senate."}, {"url": "https://www.sejm.gov.pl/sejm10.nsf/druk.xsp?nr=2529", "title": "Sejm Druk 2529 - Legislative Process", "domain": "sejm.gov.pl",
"accessed_at": "2026-05-22T00:00:00Z", "snippet": "NOT ACCESSED - tool unavailable. This page would show the full legislative history of the bill including Sejm passage date and Senate
transmission."}, {"url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114", "title": "Regulation (EU) 2023/1114 - Markets in Crypto-Assets (MiCA)", "domain": "eur-lex.europa.eu",
"accessed_at": "2026-05-22T00:00:00Z", "snippet": "NOT ACCESSED - background knowledge. MiCA regulation requiring member state implementing legislation, main provisions applicable from 30 December
2024."}], "key_facts": ["Druk 2529 is the Sejm print number for Poland's Crypto-Assets Market Act (ustawa o rynku kryptoaktyw\u00f3w), the national legislation implementing the EU MiCA Regulation.",
"The Polish Senate has a constitutional 30-day deadline to act on bills transmitted from the Sejm.", "The bill would likely be referred to the Senate's Budget and Public Finance Committee (Komisja
Bud\u017cetu i Finans\u00f3w Publicznych).", "MiCA's main provisions applied from 30 December 2024, meaning Poland's implementing legislation is significantly delayed if still in the Senate in May
2026.", "The KNF (Komisja Nadzoru Finansowego) is designated as the national competent authority under the act.", "The specific May 2026 plenary vote date could NOT be confirmed due to all web search
and fetch tools being unavailable in this session.", "The Senate typically holds 2-3 day plenary sessions approximately every two weeks."], "data_points": [{"metric": "Senate constitutional deadline
to act on Sejm bills", "value": 30.0, "unit": "days", "as_of": "2026-05-22", "source_url": "https://www.sejm.gov.pl/prawo/konst/polski/kon1.htm"}, {"metric": "MiCA main provisions application date",
"value": 20241230.0, "unit": "date (YYYYMMDD)", "as_of": "2024-12-30", "source_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114"}], "created_at":
"2026-05-22T01:17:13.966784Z", "updated_at": "2026-05-22T01:17:13.966784Z", "stale_after": "2026-05-22T07:17:13.966784Z", "state": "fresh", "revision_history": [], "session_id":
"c0506171-701e-4ef4-ae17-580c56e81e74", "follow_up_count": 0}, "is_follow_up": false}, {"query": "How quickly does the Polish Senate typically vote on bills passed by the Sejm? What is the typical
turnaround time? Senate of Poland legislative process speed", "entry": {"slug": "how-quickly-does-the-polish-senate-typically-vote-95648013", "query": "How quickly does the Polish Senate typically
vote on bills passed by the Sejm? What is the typical turnaround time? Senate of Poland legislative process speed", "answer": "The research report above covers the constitutional deadlines (30 days
standard, 20 days budget, 14 days urgent), the practical turnaround patterns (most bills processed in 20\u201328 days, routine bills in 7\u201314 days), and the structural factors that influence
Senate processing speed. Note that web-based sources were unavailable during this session, so the findings rely on established constitutional provisions and well-documented legislative practices.",
"sources": [{"url": "https://www.sejm.gov.pl/prawo/konst/angielski/kon1.htm", "title": "Constitution of the Republic of Poland (1997) - English translation", "domain": "sejm.gov.pl", "accessed_at":
"2026-05-22T00:00:00Z", "snippet": "Article 121(2): The Senate shall consider a bill passed by the Sejm within 30 days. Article 223: Senate has 20 days for budget. Article 123: 14 days for urgent
legislation."}, {"url": "https://en.wikipedia.org/wiki/Senate_of_Poland", "title": "Senate of Poland - Wikipedia", "domain": "en.wikipedia.org", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "The
Senate reviews legislation passed by the Sejm within constitutionally mandated deadlines."}, {"url": "https://www.senat.gov.pl", "title": "Senat Rzeczypospolitej Polskiej - Official Website",
"domain": "senat.gov.pl", "accessed_at": "2026-05-22T00:00:00Z", "snippet": "Official records of Senate proceedings and legislative activity."}], "key_facts": ["The Polish Senate has a constitutional
deadline of 30 days to act on standard bills passed by the Sejm (Article 121(2), 1997 Constitution)", "For budget bills, the Senate deadline is shortened to 20 days (Article 223)", "For urgent bills
(tryb pilny), the Senate deadline is 14 days (Article 123)", "If the Senate fails to act within the deadline, the bill is automatically deemed adopted as passed by the Sejm", "In practice, most bills
are processed within 20\u201328 days of receipt from the Sejm", "Routine or uncontroversial bills may be processed within 7\u201314 days", "Senate plenary sessions occur approximately every 2\u20133
weeks, which is a major scheduling constraint", "Committee review of bills typically takes 1\u20132 weeks before plenary consideration", "The Senate can adopt a bill without changes, propose
amendments, or reject it entirely", "During divided government (e.g., 2019\u20132023 opposition Senate), the Senate more frequently used the full 30-day window", "The automatic adoption mechanism
(lapse of deadline without vote) is rarely triggered intentionally"], "data_points": [{"metric": "Constitutional deadline for standard bills (Senate)", "value": 30.0, "unit": "days", "as_of":
"1997-04-02", "source_url": "https://www.sejm.gov.pl/prawo/konst/angielski/kon1.htm"}, {"metric": "Constitutional deadline for budget bills (Senate)", "value": 20.0, "unit": "days", "as_of":
"1997-04-02", "source_url": "https://www.sejm.gov.pl/prawo/konst/angielski/kon1.htm"}, {"metric": "Constitutional deadline for urgent bills (Senate)", "value": 14.0, "unit": "days", "as_of":
"1997-04-02", "source_url": "https://www.sejm.gov.pl/prawo/konst/angielski/kon1.htm"}, {"metric": "Typical processing time for most bills (practice)", "value": 24.0, "unit": "days (midpoint of 20-28
range)", "as_of": "2026-05-22", "source_url": "https://www.senat.gov.pl"}, {"metric": "Processing time for routine/uncontroversial bills (practice)", "value": 10.5, "unit": "days (midpoint of 7-14
range)", "as_of": "2026-05-22", "source_url": "https://www.senat.gov.pl"}, {"metric": "Approximate frequency of Senate plenary sessions", "value": 2.5, "unit": "weeks between sessions", "as_of":
"2026-05-22", "source_url": "https://www.senat.gov.pl"}], "created_at": "2026-05-22T01:16:23.963457Z", "updated_at": "2026-05-22T01:16:23.963457Z", "stale_after": "2026-05-29T01:16:23.963457Z",
"state": "fresh", "revision_history": [], "session_id": "1f5627eb-cfa7-4282-9ff6-92d11252cbd9", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

The research sub-agent couldn't access live web data. Let me directly check the Senate and Sejm websites, plus search for news about the Senate schedule.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.sejm.gov.pl/sejm10.nsf/PrzebiegProc.xsp?nr=2529",
  "prompt": "What is the current status of druk 2529? Has the bill been sent to the Senate? Has the Senate voted? What dates are listed for each stage?"
}
```

### 📋 Result

```
{"url": "https://www.sejm.gov.pl/sejm10.nsf/PrzebiegProc.xsp?nr=2529", "content": "The provided content does not contain any substantive information about druk 2529 or its legislative status. \n\nThe
page appears to be a CAPTCHA verification screen that blocks automated access to the Polish Sejm website. It only shows:\n- A CAPTCHA image with a \"bottle\" verification test\n- A support ID
number\n- Instructions to use API endpoints (api.sejm.gov.pl or eli.gov.pl) for programmatic requests\n\n**To obtain the actual information about druk 2529, you would need to:**\n1. Access the page
through a web browser and complete the CAPTCHA, or\n2. Use the official Sejm API at api.sejm.gov.pl\n\nThe current content provides no information about:\n- The bill's status\n- Whether it was sent to
the Senate\n- Senate voting results\n- Dates for legislative stages\n\n**Relevant links:**\n- The page suggests using the [Sejm API](https://api.sejm.gov.pl) or [ELI portal](https://eli.gov.pl) for
programmatic access to legislative information"}
```

```json
{
  "query": "Polish Senate vote Crypto-Assets Market Act druk 2529 May 2026"
}
```

### 📋 Result

```
{"query": "Polish Senate vote Crypto-Assets Market Act druk 2529 May 2026", "results": [{"title": "Poland\u2019s parliament revives controversial crypto bill despite presidential veto", "url":
"https://www.coindesk.com/policy/2025/12/19/poland-s-lower-house-approves-crypto-law-again-sends-vetoed-bill-back-to-senate", "snippet": "Poland's parliament approves controversial crypto bill and
sends to senate for vote. (Piotr Cierkosz/Unsplash modified by CoinDesk)\nWhat to know:\nPoland's lower house of parliament passed a crypto regulation bill previously vetoed by President Nawrocki,
sending it to the Senate for further debate.\nThe bill aligns with the EU's MiCA regulation, but is criticized for granting excessive powers to the Polish Financial Supervision Authority.\nPrime
Minister Tusk's government reintroduced the bill unch", "api_data": null, "hint": null}, {"title": "Polish Sejm passes politically charged cryptocurrency act - Cryptopolitan", "url":
"https://www.cryptopolitan.com/polish-sejm-passes-cryptocurrency-act/", "snippet": "Polish Sejm passes politically charged cryptocurrency act\n![Polish Sejm passes politically charged cryptocurrency
act](https://www.cryptopolitan.com/wp-content/uploads/2025/12/ET1TzDer09-768x432.webp)\n- Poland adopts controversial crypto law designed to introduce MiCA rules.\n- The Polish government pushed the
legislation through parliament, overriding the president\u2019s veto.\n- The law is causing political turbulence in Warsaw, with warnings about the future of the market.\nThe Polish parliament has",
"api_data": null, "hint": null}, {"title": "Polish government-backed crypto bill passes after repeated presidential vetoes", "url": "https://cryptobriefing.com/poland-crypto-bill-mica-vetoes/",
"snippet": "![Polish government-backed crypto bill passes after repeated presidential vetoes](https://static.cryptobriefing.com/wp-content/uploads/2026/05/15150227/tusk-s-cabinet-resubmits-crypto-
bill-despite-nawrocki-veto-1-800x420.jpeg)\nPolish government-backed crypto bill passes after repeated presidential vetoes\nPoland's Sejm approved the MiCA implementation bill 241-200, but President
Nawrocki's veto pen looms again.\nPoland\u2019s lower house of parliament just passed a government-backed bill to bring the c", "api_data": null, "hint": null}, {"title": "Poland's Sejm Re-passes
Crypto Market Bill After ...", "url": "https://www.kucoin.com/news/flash/poland-s-sejm-re-passes-crypto-market-bill-after-presidential-veto", "snippet": "According to ChainCatcher, Poland's Sejm
(lower house) has re-approved the 'Markets in Crypto-Assets Act' that was previously vetoed by President Karol Nawrocki. The bill, passed with 241 votes, is identical to the earlier version and aims
to align Polish law with the EU's MiCA framework. Critics argue it grants excessive powers to the KNF, including website blocking and heavy fines. Nawrocki had previously rejected the bill, citing
vague language, overregulation, and high compliance costs. The ", "api_data": null, "hint": null}, {"title": "Polish Parliament Advances Crypto Asset Market Bill ...", "url":
"https://www.binance.com/en/square/post/12-19-2025-polish-parliament-advances-crypto-asset-market-bill-despite-presidential-veto-33926986084801", "snippet": null, "api_data": null, "hint": null},
{"title": "Sejm approves crypto bill | Dudkowiak & Putyra", "url": "https://www.dudkowiak.com/blog/sejm-adopts-selected-senate-amendments-to-the-polish-crypto-asset-market-bill/", "snippet": "Sejm
adopts selected Senate amendments to the polish crypto-asset market bill\nOn 7 November 2025, the Sejm adopted some of the Senate\u2019s amendments to the draft law on the [crypto-asset
market](https://www.dudkowiak.com/blog/cryptoasset-market-act-passed-by-the-sejm/), thus paving the way for the draft to be submitted to the President of Poland for signature.\nThe President has 21
days to sign or refuse to sign (veto) the adopted bill upon receipt from the Marshal of the Sejm. The bill was submitt", "api_data": null, "hint": null}, {"title": "Poland's Sejm Passes Crypto MiCA
Bill Amid Fraud Probe", "url": "https://coinpaprika.com/news/poland-sejm-mica-bill-fraud-probe/", "snippet": "Poland's Sejm Passes Crypto MiCA Bill Amid Fraud Probe\nPoland's lower house passed a MiCA
implementation bill on 15 May 2026 by a vote of 241 to 200. The vote coincides with a fraud probe into Zondacrypto, with estimated user losses of 350 million PLN.\n![Poland's Sejm Passes Crypto MiCA
Bill Amid Fraud Probe](https://content.coinpaprika.com/api/files/news/9mbz1p0p3n1lftf/polands_sejm_passes_crypto_mi_ca_bill_amid_fraud_pr_o6526xrwut.jpg)\nPolish lower house passes crypto regulation
bill\nPoland's ", "api_data": null, "hint": null}, {"title": "Poland's Sejm Passes Vetoed Crypto Law, Aims to Align with EU MiCA by 2026 | KuCoin", "url": "https://www.kucoin.com/news/flash/poland-s-
sejm-passes-vetoed-crypto-law-aims-to-align-with-eu-mica-by-2026", "snippet": "Derived from Cryptofrontnews, Poland\u2019s Sejm passed the previously vetoed Crypto-Asset Market Act on December 22,
2025, by a vote of 241 to 183. The bill, now sent to the Senate, aims to align national regulations with the EU\u2019s MiCA framework by 2026. It grants the Polish Financial Supervision Authority
(KNF) expanded powers, including fines up to 10 million zlotys, website blocks, and prison sentences of up to five years. Critics warn the strict licensing process and oversight could push crypto ",
"api_data": null, "hint": null}, {"title": "Poland\u2019s Crypto Bill Passes Parliament Again After Presidential Veto, Now Heads to Senate | MEXC News", "url": "https://www.mexc.co/en-PH/news/314749",
"snippet": "The Crypto-Asset Market Act, which aims to align Poland with the European Union\u2019s Markets in Crypto-Assets (MiCA) framework, now moves to the Senate for review in what has become one
of Europe\u2019s most contentious regulatory debates.\nThe Crypto-Asset Market Act received 241 votes in favor and 183 against in the Sejm, Poland\u2019s lower house. This marks the second time
lawmakers have approved the identical bill, which the government resubmitted without any changes after the initial veto attempt failed", "api_data": null, "hint": null}, {"title": "Will Poland\u2019s
President Veto Crypto Law for 3rd Time?", "url": "https://www.caml.lt/post/will-poland-s-president-veto-crypto-law-for-3rd-time", "snippet": "Will Poland\u2019s President Veto Crypto Law for 3rd
Time?\n- 1 day ago\n- 4 min read\nPolish politics loves a legislative loop. Some bills move through parliament with the agonizing friction of a bad airport security queue: you step forward, the
machine beeps, you step back, take off your belt, take out your laptop, and lose a bit of dignity\u2014only to realize the issue was just your wallet.\nIn this case, it\u2019s a crypto wallet. And the
security gate is the Presidential Palace.\nThe core question in Warsaw r", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Senat Polska ustawa kryptoaktywa g\u0142osowanie maj 2026"
}
```

### 📋 Result

```
{"query": "Senat Polska ustawa kryptoaktywa g\u0142osowanie maj 2026", "results": [{"title": "Nowa ustawa o rynku kryptoaktyw\u00f3w. Senat podj\u0105\u0142 decyzj\u0119 - Biznes w INTERIA.PL", "url":
"https://biznes.interia.pl/gospodarka/news-nowa-ustawa-o-rynku-kryptoaktywow-senat-podjal-decyzje,nId,23485632", "snippet": "Ustawa w sprawie kryptoaktyw\u00f3w trafi\u0142a do porz\u0105dku obrad
Senatu, kt\u00f3re zaplanowano na 20 i 21 maja 2026 roku. W \u015brod\u0119, 20 maja, odby\u0142a si\u0119 debata w tej sprawie. Senatorowie Prawa i Sprawiedliwo\u015bci zg\u0142osili poprawki do
ustawy, na skutek czego trafi\u0142a ona z powrotem do Komisji Bud\u017cetu i Finans\u00f3w Publicznych, kt\u00f3rej posiedzenie zaplanowano na 21 maja w godzinach porannych. Nast\u0119pnie Senat
g\u0142osowa\u0142 nad ustaw\u0105.\nUstawa o rynku kryptoaktyw\u00f3w. Poprawki i g\u0142osowanie Senatu\nW \u015brod\u0119, 20 maja, w Senacie odb", "api_data": null, "hint": null}, {"title": "Senat
przyj\u0105\u0142 projekt o kryptoaktywach. To ju\u017c trzecia ustawa, kt\u00f3ra trafi do prezydenta", "url": "https://www.rp.pl/prawo-w-polsce/art44430541-ustawa-o-kryptoaktywach-przeszla-przez-
senat-trafi-znow-na-biurko-karola-nawrockiego", "snippet": "Nowa ustawa o kryptoaktywach przesz\u0142a przez Senat bez poprawek. Izba odrzuci\u0142a prezydenckie poprawki, kt\u00f3re przedstawili w
trakcie \u015brodowego posiedzenia senatorowie Prawa i Sprawiedliwo\u015bci. Teraz projekt ustawy trafi na biurko prezydenta, kt\u00f3ry ju\u017c dwukrotnie wetowa\u0142 podobne projekty.\nUstawa o
kryptoaktywach zn\u00f3w trafi na biurko Karola Nawrockiego\nZa przyj\u0119ciem projektu ustawy bez poprawek zag\u0142osowa\u0142o 57 senator\u00f3w, 26 by\u0142o przeciw, nikt z obecnych na sali nie
wstrzyma\u0142 si\u0119 od g\u0142osu. Przyj\u0119ty w c", "api_data": null, "hint": null}, {"title": "Kryptowaluty. Senat zdecydowa\u0142. Ustawa trafi na biurko prezydenta Nawrockiego -
PolsatNews.pl", "url": "https://www.polsatnews.pl/wiadomosc/2026-05-21/senat-zdecydowal-ustawa-trafi-na-biurko-prezydenta-nawrockiego/", "snippet": "Senat zdecydowa\u0142. Rz\u0105dowa ustawa trafi na
biurko prezydenta Nawrockiego\nSenat nie zaproponowa\u0142 poprawek do ustawy o rynku kryptoaktyw\u00f3w i skierowa\u0142 j\u0105 na biurko prezydenta. Izba wy\u017csza odrzuci\u0142a szereg
prezydenckich poprawek, kt\u00f3re zg\u0142osili senatorowie PiS. Wcze\u015bniej Karol Nawrocki dwa razy zawetowa\u0142 przepisy ws. kryptowalut.\n![Fragment sali plenarnej Senatu RP z senatorami
siedz\u0105cymi w \u0142awach, widoczny zbli\u017cenie na twarz m\u00f3wi\u0105cego senatora.](https://ipla.pluscdn.pl/dituel/cp/z8/z8d8py6p344h52im", "api_data": null, "hint": null}, {"title": "Senat
przyj\u0105\u0142 ustaw\u0119 o rynku kryptoaktyw\u00f3w bez poprawek - GazetaPrawna.pl", "url": "https://www.gazetaprawna.pl/wiadomosci/kraj/artykuly/11250534,senat-ustawa-kryptoaktywa-bez-poprawek-
prezydent.html", "snippet": "Senat w czwartek nie wprowadzi\u0142 zmian do ustawy dotycz\u0105cej rynku kryptoaktyw\u00f3w i przekaza\u0142 j\u0105 do dalszego rozpatrzenia przez prezydenta. Izba
wy\u017csza odrzuci\u0142a r\u00f3wnie\u017c cz\u0119\u015b\u0107 poprawek zg\u0142oszonych w imieniu prezydenta przez senator\u00f3w Prawa i Sprawiedliwo\u015bci.\nZa przyj\u0119ciem ustawy bez
wprowadzania poprawek g\u0142osowa\u0142o 57 senator\u00f3w, 26 by\u0142o przeciw, nikt nie wstrzyma\u0142 si\u0119 od g\u0142osu. Teraz ustawa trafi na biurko prezydenta Karola Nawrockiego,
kt\u00f3ry ju\u017c dwa razy wcze\u015bniej zawetowa\u0142 to\u017csame przepisy.\nRz\u0105dow", "api_data": null, "hint": null}, {"title": "Rz\u0105dowy projekt ustawy o rynku kryptoaktyw\u00f3w",
"url": "https://www.sejm.gov.pl/sejm10.nsf/PrzebiegProc.xsp?nr=1424", "snippet": "This question is for testing whether you are a human visitor and to prevent automated spam submission.\nTo pytanie
s\u0142u\u017cy do sprawdzenia, czy jeste\u015b cz\u0142owiekiem i zapobiega automatycznym zg\u0142oszeniom.\n[\n](#)![bottle](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXB
IWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH1QgXEwYEPM59bQAAAAZiS0dEAP8A/wD/oL2nkwAAEnBJREFUaN7FWgdYlNe2/TEmihUFpNeBGTozVKkKKkpVFLGgVwVsqCBIUWSoKmIviBQBRRBsYAOxa9SLir2gSSyJJjExPnNj1NhwvX0OYuzRvPgu33e+ofwz/1ln773
W2vtHACD8X5dr", "api_data": null, "hint": null}, {"title": "Rz\u0105dowy projekt ws. kryptowalut z poparciem sejmowej komisji finans\u00f3w", "url": "https://cyberdefence24.pl/polityka-i-
prawo/polska/sejm-bez-decyzji-o-kryptowalutach-projekty-ustaw-wyslane-do-komisji-finansow", "snippet": "- WIADOMO\u015aCI\nRz\u0105dowy projekt ws. kryptowalut z poparciem sejmowej komisji
finans\u00f3w\nPo wtorkowym pierwszym czytaniu w Sejmie, ju\u017c dzie\u0144 p\u00f3\u017aniej - 13 maja - sejmowa Komisja Finans\u00f3w Publicznych przyst\u0105pi\u0142a do szczeg\u00f3\u0142owych
prac nad czterema projektami ustaw reguluj\u0105cych rynek kryptowalut. Komisja uzna\u0142a projekt rz\u0105dowy za wiod\u0105cy, odrzuci\u0142a niemal wszystkie poprawki zg\u0142oszone przez
prezydenta i Polsk\u0119 2050 oraz przyj\u0119\u0142a ustaw\u0119 do dalszych prac parlamentarnych tylko z jedn\u0105 zaakceptowan\u0105 zmian\u0105.\n![", "api_data": null, "hint": null}, {"title":
"Senat przyj\u0105\u0142 ustaw\u0119 o kryptoaktywach. Decyzja teraz po stronie prezydenta | Strefa Biznesu", "url": "https://strefabiznesu.pl/senat-przyjal-ustawe-o-kryptoaktywach-decyzja-teraz-po-
stronie-prezydenta/ar/c3p2-29020949", "snippet": "Spis tre\u015bci\nZa przyj\u0119ciem ustawy g\u0142osowa\u0142o 57 senator\u00f3w\nZa przyj\u0119ciem ustawy bez wprowadzania poprawek
g\u0142osowa\u0142o 57 senator\u00f3w, 26 by\u0142o przeciw, nikt nie wstrzyma\u0142 si\u0119 od g\u0142osu. Teraz ustawa trafi na biurko prezydenta Karola Nawrockiego, kt\u00f3ry ju\u017c dwa razy
wcze\u015bniej zawetowa\u0142 to\u017csame przepisy.\nW trakcie prac w Sejmie zdecydowano o uznaniu rz\u0105dowego projektu ustawy o rynku kryptoaktyw\u00f3w za wiod\u0105cy. Tym samym prace nad
innymi propozycjami, tj. prezydenta, Polski 2050 i Konfederacji, nie by\u0142y kontyn", "api_data": null, "hint": null}, {"title": "Dwa weta. Trzecia pr\u00f3ba. Ustawa o krypto przyj\u0119ta", "url":
"https://www.money.pl/gospodarka/ustawa-ws-kryptowalut-przeglosowana-bedzie-trzecie-weto-7288311969515680a.html", "snippet": "Dwa weta. Trzecia pr\u00f3ba. Ustawa o krypto przyj\u0119ta\nSenat
przeg\u0142osowa\u0142 bez poprawek ustaw\u0119 ws. kryptoaktyw\u00f3w. Teraz trafi na biurko prezydenta Karola Nawrockiego, kt\u00f3ry ju\u017c dwa razy zawetowa\u0142 wcze\u015bniejsze projekty w
tej sprawie.\nPod koniec posiedzenia Senatu odby\u0142o si\u0119 g\u0142osowanie m.in. nad rozpatrzon\u0105 w \u015brod\u0119 przez izb\u0119 wy\u017csz\u0105 parlamentu ustaw\u0105 o kryptoaktywach.
Celem ustawy jest zapewnienie stosowania unijnego rozporz\u0105dzenia MiCA (The Markets in Crypto-Assets Regulation), kt\u00f3re ma uregulowa\u0107 ryne", "api_data": null, "hint": null}, {"title":
"Senat bez poprawek do ustawy o rynku kryptoaktyw\u00f3w. Teraz czas na ruch prezydenta - Bankier.pl", "url": "https://www.bankier.pl/wiadomosc/Senat-bez-poprawek-do-ustawy-o-rynku-kryptoaktywow-
Teraz-czas-na-ruch-prezydenta-9137451.html", "snippet": "Senat w czwartek nie zaproponowa\u0142 poprawek do ustawy o rynku kryptoaktyw\u00f3w i skierowa\u0142 j\u0105 na biurko prezydenta. Izba
wy\u017csza odrzuci\u0142a szereg prezydenckich poprawek, kt\u00f3re zg\u0142osili senatorowie PiS.\n![Senat bez poprawek do ustawy o rynku kryptoaktyw\u00f3w. Teraz czas na ruch
prezydenta](https://galeria.bankier.pl/p/f/d/d37b80d8e4e8b0-948-568-0-112-3000-1799.jpg)\n![Senat bez poprawek do ustawy o rynku kryptoaktyw\u00f3w. Teraz czas na ruch
prezydenta](https://galeria.bankier.pl/p/f/d/d37b80d8e4e8b0-948-568-", "api_data": null, "hint": null}]}
```

## 💬 Response

This is very clear. The search results confirm that the **Senate has already voted** on this bill. Let me get the exact details:

The Polish-language search results clearly show:
1. The bill was on the Senate agenda for **May 20-21, 2026**
2. The debate happened on Wednesday, May 20, 2026
3. PiS senators proposed amendments on behalf of the President, which sent it back to the Budget and Public Finance Committee
4. The committee met on May 21 (Thursday morning)
5. The **Senate voted on the bill on May 21, 2026** (Thursday) — adopting it **without amendments** (57 in favor, 26 against, 0 abstentions)
6. The bill has now been sent to President Nawrocki's desk

This is before May 31, 2026, so the question resolves **YES**. The Senate plenary vote has already occurred.

Let me verify by fetching one of the most detailed articles:

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.gazetaprawna.pl/wiadomosci/kraj/artykuly/11250534,senat-ustawa-kryptoaktywa-bez-poprawek-prezydent.html",
  "prompt": "What date did the Polish Senate vote on the crypto-assets bill? What was the vote count? Did they adopt it with or without amendments?"
}
```

### 📋 Result

```
{"url": "https://www.gazetaprawna.pl/wiadomosci/kraj/artykuly/11250534,senat-ustawa-kryptoaktywa-bez-poprawek-prezydent.html", "content": "Based on the content:\n\n**Date:** Thursday (czwartek) - the
specific date is not provided in the text, only the day of the week.\n\n**Vote count:** 57 senators voted in favor, 26 against, 0 abstentions.\n\n**Amendments:** The Senate adopted the bill **without
amendments** (bez poprawek). They rejected the amendments proposed by Law and Justice senators on behalf of the president.\n\nThe bill has now been sent to President Karol Nawrocki for further
consideration. This is the third attempt to regulate the crypto-assets market - the president previously vetoed two similar bills.\n\nRelevant links:\n- No external links are present in the provided
text content.", "title": "Przepisy o krypto coraz bli\u017cej wej\u015bcia w \u017cycie. Teraz ruch prezydenta"}
```

## 💬 Response

The evidence is overwhelming. The Senate voted on the bill on May 21, 2026 (Thursday), well before the May 31, 2026 deadline.

Now let me run the reflection and premortem to formalize this.

## 💭 Thinking

The reflection confirms my analysis. Now let me run the premortem and then submit.
