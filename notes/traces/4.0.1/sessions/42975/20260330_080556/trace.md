# Reasoning Log: Will the community prediction be higher than 20.00% on 2026-04-11 for the Metaculus question "Will the Iranian government lose power before 2027?"?

*Generated: 2026-03-30T08:08:57.546102+00:00*


## 💭 Thinking

Let me analyze this meta-prediction question carefully.

**Question**: Will the community prediction (CP) for "Will the Iranian government lose power before 2027?" be higher than 20.00% on 2026-04-11?

Key facts:
- Current CP as of 2026-03-29: 20.00% (exactly at the threshold)
- Historical CP trajectory:
  - 2026-02-22: 33.00%
  - 2026-03-01: 42.00%
  - 2026-03-08: 45.00% (peak)
  - 2026-03-15: 37.50%
  - 2026-03-22: 28.00%
  - 2026-03-29: 20.00%
- Resolution date: 2026-04-11 12:20:36
- Time until resolution: ~12 days

The prediction has been dropping sharply—down 25 percentage points from its March 8 peak to the current level. With only about two weeks remaining until resolution, I need to assess whether this downward momentum will continue or if the prediction might stabilize or reverse.

The question hinges on whether Iran's government loses power before 2027, and the declining probability makes sense as we approach the deadline without the event occurring. I should look into the current situation in Iran to better understand what might drive the prediction in these final days.

## 🔧 Tool: mcp__markets__get_metaculus_questions


## 🔧 Tool: mcp__markets__get_cp_history


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "post_id_list": [
    38770
  ]
}
```

### 📋 Result

```
{"post_id": 38770, "title": "Will the Iranian government lose power before 2027?", "type": "binary", "url": "https://www.metaculus.com/questions/38770", "background_info": "The Islamic Republic of
Iran was established following the [1979 revolution](https://en.wikipedia.org/wiki/Iranian_Revolution) that overthrew the monarchy. Since then, the country has maintained a centralized political
system dominated by clerical leadership, while experiencing periods of both internal unrest and external pressure. Over the past four decades, the government has faced challenges including war,
sanctions, and protests, but has remained in power. As of 2025, heightened international tensions, economic instability, and government unpopularity has left open the possibility of the government
losing power.", "resolution_criteria": "This question will resolve as **Yes** if, before January\u202f1,\u202f2027, a state controlling the majority of internationally recognised Iranian territory as
of July 1, 2025 meets both of the following criteria, according to [credible sources](https://www.metaculus.com/faq/#definitions):\n\n1. Neither Ali Khamenei, Masoud Pezeshkian or the Guardian Council
have formal political authority in the country.\n2. Iran's constitution does not refer to the state as an Islamic Republic.", "fine_print": "This question will resolve as **Yes** if either a foreign
country or no entity controls a majority of internationally recognised Iranian territory, even if the primary criteria has not been met.\n\nIf the relevant state has no constitution, that will be
sufficient to meet criterion 2.\n\nIf the Guardian Council shares no members with its composition as of July 1, 2025, that will be considered sufficient to meet the requirement that it no longer holds
political authority.", "num_forecasters": 205, "community_prediction": null}
```

```json
{
  "post_id": 38770,
  "days": 60
}
```

### 📋 Result

```
Failed to fetch CP history: Client error '403 Forbidden' for url 'https://www.metaculus.com/api/aggregation_explorer/?post_id=38770&aggregation_methods=recency_weighted'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
```

```json
{
  "query": "Iran government regime change 2026",
  "hours_back": 168,
  "n_articles": 10
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: EN DIRECT - Donald Trump a affirmé que les États-Unis ont négocié avec l'Iran le passage imminent de 20
cargos pétroliers dans le détroit d'Ormuz - Un Casque bleu a été tué dans le sud du Liban\n\nSummary: \nOn March 30, 2026, Donald Trump claimed that the United States negotiated with Iran for the
immediate passage of 20 oil tankers through the Strait of Hormuz, a move expected to begin the following morning. Trump also stated that US airstrikes in Iran, conducted in coordination with Israel,
resulted in a 'regime change' by killing Supreme Leader Ali Khamenei and several high-ranking officials, leaving only a 'third regime' in place with whom an agreement might soon be reached. In a
separate development, the Kuwaiti government reported that Iran attacked a desalination plant in Kuwait, causing significant damage and killing one Indian national. Additionally, the United Nations
Interim Force in Lebanon (Finul) announced that one peacekeeper was killed and another seriously wounded in the south of Lebanon after an explosion from a projectile of unknown origin struck their
position near Adchit Al Qusayr during ongoing clashes between Israel and Hezbollah.\n\nPublished date: March 30 2026, 05:28\n\nURL: https://www.jeanmarcmorandini.com/article-636760-en-direct-donald-
trump-a-affirme-que-les-etats-unis-ont-negocie-avec-l-iran-le-passage-imminent-de-20-cargos-petroliers-dans-le-detroit-d-ormuz-un-casque-bleu-a-ete-tue-dans-le-sud-du-liban.html\nSource: Jean Marc
Morandini\nClassification: World\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: Guerre au Moyen-Orient: Donald Trump vante un
\"changement de régime\" en Iran\n\nSummary: \nOn Sunday, March 30, 2026, President Donald Trump claimed that a 'regime change' has occurred in Iran following US and Israeli airstrikes that he stated
killed Supreme Leader Ali Khamenei and numerous high-ranking officials of the Islamic Republic. Speaking on Air Force One, Trump asserted that the original leadership was 'decimated' and that a 'third
regime' is now in place, characterized by different personnel than previously encountered. He further alleged that these new Iranian authorities have agreed to allow 20 oil tankers to pass through the
Strait of Hormuz, a critical maritime route handling 20% of global oil, starting the following morning. Trump expressed near-certainty of concluding a peace deal, stating, 'I think we are going to
conclude an agreement with them, I am almost sure.' These announcements come amid growing US concerns about a potential quagmire in the Middle East, rising oil prices, and a significant drop on Wall
Street, despite thousands of US soldiers being deployed to the region. Trump noted that Khamenei's designated successor, Mojtaba Khamenei, has not been seen since being named to lead the country, with
Iranian authorities only releasing written messages attributed to him.\n\nPublished date: March 30 2026, 04:35\n\nURL: https://www.bfmtv.com/international/guerre-au-moyen-orient-donald-trump-vante-un-
changement-de-regime-en-iran_AD-202603300116.html\nSource: BFMTV\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key:
[3]\nTitle: Trump declares 'regime change' in Iran, assures a deal to end war\n\nSummary: \nOn Sunday, March 30, 2026, US President Donald Trump declared he had achieved 'regime change' in Iran,
stating he is 'pretty sure' a deal to end the war will be struck. According to Trump, the conflict has resulted in a 'whole different group of people' in power. This assertion comes amid pressure to
conclude the war, which has caused oil and gas prices to surge due to strikes on energy sites and the closure of the Strait of Hormuz, cutting off 20% of global supplies. However, contrary to Trump's
claims, the article notes that the Islamic Republic remains in place following the assassination of Supreme Leader Ayatollah Ali Khamenei; his son, Mojtaba Khamenei, has been appointed as the new
Supreme Leader. Despite the loss of top officials from the government and the Islamic Revolutionary Guards Corps (IRGC), the regime continues functioning. Key figures in the ongoing dialogues include
President Masoud Pezeshkian, Foreign Minister Seyed Abbas Aragchi, and Speaker Mohammad-Bagher Ghalibaf. Pakistan is leading mediation efforts, with Egypt and Turkey also involved.\n\nPublished date:
March 30 2026, 03:23\n\nURL: https://www.firstpost.com/world/trump-declares-regime-change-in-iran-assures-a-deal-to-end-west-asia-war-13994500.html\nImage description: A photograph of Donald Trump in
a dark suit and red tie standing on the stairs of an aircraft at night, with the Presidential Seal visible on the plane's fuselage.\nSource: Firstpost\nClassification: Politics\nSentiment:
negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: Трамп заявив, що в Ірані відбулася \"зміна режиму\"\n\nSummary: \nOn Sunday, March 29, 2026, US
President Donald Trump, speaking aboard Air Force One, declared that a 'regime change' has already occurred in Iran following a joint US-Israel military operation that began on February 28. According
to Trump, the previous regime was 'destroyed' and the Supreme Leader, Ayatollah Ali Khamenei, was 'eliminated' in airstrikes. The Council of Experts subsequently elected Khamenei's son, Mojtaba
Khamenei, as the new Supreme Leader on March 8. While the Iranian Foreign Ministry confirmed Mojtaba Khamenei's injuries on March 12, sources told The New York Times on March 11 that he remains in
hiding due to safety concerns. The Israeli Defense Forces warned prior to the election that they would not hesitate to attack anyone attempting to appoint a successor. Trump stated that the new
leadership is behaving 'very prudently' but warned that Mojtaba Khamenei 'will not last long' without White House approval. Meanwhile, Politico reported on March 24 that the Trump administration is
considering Speaker of the Parliament Mohammad Bagher Ghalibaf as a potential negotiation partner or future leader, aiming for a compromise that ensures stable energy supplies in exchange for the new
regime's internal political control.\n\nPublished date: March 30 2026, 02:44\n\nURL: https://nv.ua/ukr/world/geopolitics/donald-tramp-zayaviv-pro-zminu-rezhimu-v-irani-50595885.html\nSource: Новое
Время\nClassification: World\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: Iran varsler nytt regime i Hormuzstredet\n\nSummary:
\nAccording to a statement by Iranian Vice President Mohammad Reza Aref posted on X on Sunday evening, Iranian authorities are implementing changes to the regime in the Strait of Hormuz to secure
economic benefits for Iran. Aref stated that the regime in the strait has changed and will no longer be as it was previously, emphasizing the government's determination to translate achievements on
the ground into sustainable economic and security advantages for the country. The article notes that ongoing conflict between the US and Israel against Iran has led to a significant increase in oil
prices, partly due to a sharp reduction in shipping traffic through the strategic waterway. The Strait of Hormuz is described as one of the world's most important arteries for oil and gas transport.
The report was published by NRK on March 29, 2026, at 20:57.\n\nPublished date: March 29 2026, 20:57\n\nURL: https://www.nrk.no/nyheter/iran-varsler-nytt-regime-i-hormuzstredet--1.17830007\nSource:
NRK\nClassification: World\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [6]\nTitle: Un analista internacional anticipó cómo terminará la guerra
en Medio Oriente: \"Sin cambio de régimen\n\nSummary: \nOn March 29, 2026, international analyst Juan Negri, speaking to LN+, predicted that the ongoing war between the United States, Israel, and Iran
will conclude with a diplomatic agreement between Washington and Tehran without a regime change in Iran. Negri stated that the conflict is lasting longer than Washington anticipated, noting that the
Iranian regime is in 'survival mode' and lacks the capacity to resist the world's leading power. He argued that while the U.S. may suffer significant losses, Iran will emerge 'devastated' and severely
weakened both militarily and economically. Negri identified energy security as a primary consequence, citing that the U.S. has had to lift sanctions on Russia to lower oil prices, and warned that Iran
remains willing to attack traffic passing through the Strait of Hormuz. He suggested that a Gulf monarchy, specifically Oman, which has previously acted as a diplomatic bridge, could mediate the
eventual agreement. Negri further warned that a 'devastated' Iran could foster a 'fanatical, anti-Western' environment, potentially destabilizing the Middle East by fueling resentment that gave rise
to groups like Al Qaeda and Hamas.\n\nPublished date: March 29 2026, 10:30\n\nURL: https://www.lanacion.com.ar/el-mundo/un-analista-internacional-anticipo-como-terminara-la-guerra-en-medio-oriente-
sin-cambio-de-regimen-nid29032026/\nImage description: A large plume of thick grey smoke rising into the sky from an explosion in a city, with modern buildings and a construction crane visible in the
foreground.\nSource: La Nacion\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: Irán y la metamorfosis
de Oriente Próximo\n\nSummary: \nAccording to the article published in Deia on March 29, 2026, the combined attacks by the United States and Israel against the Islamic Republic of Iran are portrayed
as a potential 'turning point' that could lead to the defeat of the Ayatollah regime and a radical reconfiguration of the Middle East, comparable to the geopolitical shifts of 1979. The article,
citing Kim Ghattas's book 'Black Tide', notes that the 1979 Iranian Revolution, the Soviet invasion of Afghanistan, and the Mecca Mosque siege created a conservative religious wave and the rivalry
between Saudi Arabia and Iran. The author argues that following the October 7, 2023, Hamas attacks, Israel has used the opportunity to weaken Hamas in Gaza, Hezbollah in Lebanon, and the Assad regime
in Syria, with Iran now being the 'final prize' to reorganize the regional balance of power under US protection. The article suggests that a direct land invasion is unlikely due to lessons from Iraq
and Afghanistan, citing Iran's population of 90 million, its well-armed Republican Guard, and the Basij militia. Instead, the author posits that regime change must come from within, potentially
through a coup following the assassination of Supreme Leader Khamenei, though the succession of his son complicates this. The text claims Iran's military assets, including ballistic missiles,
underground silos, and Shahed drones, are being depleted by the bombardment. The article asserts that if the regime falls, it would align the Middle East with US and Israeli interests, ending the
'Cold War' between Saudi Arabia and Iran, and dealing a blow to China by removing a major ally and oil source. The author notes that while public criticism focuses on the Trump administration and
Netanyahu, Arab monarchies, particularly Saudi Arabia under Prince Bin Salman, are silently pushing for the intervention to secure economic development and regional dominance.\n\nPublished date: March
29 2026, 05:00\n\nURL: https://www.deia.eus/mundo/2026/03/29/iran-metamorfosis-oriente-proximo-10880814.html\nSource: Deia\nClassification: World\nSentiment: negative\nReporting voice:
Analytical\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: GOP Rep. Gimenez: 'Some' Governmental Change Is Objective in Iran, May Not Be Doable\n\nSummary: \nOn Friday, March 28, 2026,
during a broadcast of C-SPAN's 'Ceasefire', U.S. Representative Carlos Gimenez (R-FL) outlined three objectives for U.S. policy toward Iran. According to Gimenez, the first two objectives are ensuring
Iran can no longer threaten neighbors with ballistic missiles and ensuring Iran never possesses a nuclear weapon. The third objective, which Gimenez noted as potentially unattainable, is 'some kind of
change in the government' or regime change. Gimenez described himself as 'a lot more aggressive' than some colleagues, stating he wants to 'score a touchdown' rather than 'kick a field goal' (which he
equated to going into overtime). He further expressed concern that while the Trump administration might be able to control Iran's regime, a subsequent, less strong administration would face issues
with that outcome.\n\nPublished date: March 28 2026, 21:09\n\nURL: https://www.breitbart.com/clips/2026/03/28/gop-rep-gimenez-some-governmental-change-is-objective-in-iran-may-not-be-doable/\nSource:
Breitbart\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: Anything Short of Regime Change in Iran
Would Be a Failure | Opinion\n\nSummary: \nIn an opinion piece published on March 28, 2026, in Newsweek, authors Pouria Hadjibagheri MBE and Khosro Isfahani argue that any negotiated settlement with
Iran that does not result in regime change would be a failure. The authors contend that the U.S. would be legitimizing terrorists by negotiating with the current leadership trio: Mohammad-Bagher
Ghalibaf (former IRGC air force commander and parliament speaker), Gholam-Hossein Mohseni-Ejei (Interim Leadership Council member and Chief Justice), and Brigadier General Ahmad Vahidi (IRGC
Commander-in-Chief). The article claims that these figures are responsible for a massacre of more than 30,000 unarmed Iranians in two days in January 2026, with Ejei specifically instructing the
judiciary to be 'decisive, maximum' and 'without any legal leniency.' The authors describe the Iranian regime as a 'decapitated system' following the deaths of Supreme Leader Ayatollah Ali Khamenei
and Supreme National Security Council Secretary Ali Larijani. They assert that Vahidi is subject to an Interpol Red Notice for the 1994 bombing of the AMIA Jewish community center in Buenos Aires,
Argentina, which killed 85 people and injured over 300. The authors warn that a settlement leaving this leadership intact would be a 'Biden-level miscalculation' and 'capitulation,' citing the 2021
Afghanistan withdrawal as a precedent for the failure of accommodation with armed movements. Conversely, the article highlights the alternative of supporting the Iranian people, noting that Crown
Prince Reza Pahlavi's call for protests on January 8 and 9 drew millions, and the diaspora responded with 250,000 protesters in Munich alone and hundreds of thousands more in Los Angeles and Toronto
on February 14. The authors conclude that 'Anything short of regime change is not a diplomatic achievement' but rather a decision to live with the consequences of the regime's violence.\n\nPublished
date: March 28 2026, 09:00\n\nURL: https://www.newsweek.com/anything-short-regime-change-iran-would-be-failure-opinion-11742734\nSource: Newsweek\nClassification: Politics\nSentiment:
negative\nReporting voice: Advocacy\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [10]\nTitle: Irán tras un mes de guerra: una República Islámica más radical, cerrada y agresiva\n\nSummary:
\nAccording to a report published by La Provincia on March 28, 2026, Israel's military campaign against Iran over the past month has resulted in the decapitation of the country's political and
military leadership, including the death of Supreme Leader Ali Khamenei and the elimination of much of the Tehran elite. In response, the Islamic Republic has undergone a leadership reshuffle, with
Ali Khamenei's son, Mojtaba Khamenei, assuming the role of Supreme Leader, alongside new heads for the General Staff, the Revolutionary Guard, and the National Security Council. While US President
Donald Trump claimed on Tuesday that the operation successfully changed the regime, experts argue the opposite has occurred. Dennis Citrionowicz of the Atlantic Council states that power in Iran is
now 'much more radicalized' and operates as a decentralized 'mosaic' system centered on the Revolutionary Guard, making negotiations significantly harder. Hamidreza Azizi, an expert on Iranian
security, notes that the new leadership, drawn largely from the Guard, is composed of younger, more intransigent, and nationalist figures who are less willing to negotiate than their predecessors.
Mohammed Bagher Ghalibaf, the Parliament President, is identified as a potential interlocutor for the US, but Citrionowicz clarifies that the Revolutionary Guard holds the ultimate decision-making
power regarding any potential agreement.\n\nPublished date: March 28 2026, 08:21\n\nURL: https://www.laprovincia.es/mundo/2026/03/28/iran-guerra-republica-islamica-mas-radical-cerrada-
agresiva-128513690.html\nImage description: A woman wearing a black hijab holding a large portrait of a man with a beard and glasses, identified in the text as Mojtaba Khamenei, while raising her hand
in a gesture of prayer or supplication at a night gathering with blurred lights and flags in the background.\nSource: La Provincia\nClassification: World\nSentiment: negative\nReporting voice:
Narrative\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: Mark Halperin: My Hunch Is They've Had A \"Secret Plan\" For Iran Regime Change All Along\n\nSummary: \nOn March 26, 2026,
political commentator Mark Halperin appeared on '2WAY Tonight' to express his belief that the U.S. President and Israeli Prime Minister 'Bibi' have had a 'secret plan' for regime change in Iran all
along. Halperin stated, 'That's my hunch based on the totality of what I know,' while noting that while the day was not ideal for peace talks, 'the markets loved today.' He cited specific market
metrics: the Dow rose 305 points, the S&P gained 35 points, the NASDAQ increased by 167, and Brent crude oil remained around $100 a barrel. Halperin argued that the 'extraordinary unauthorized attack'
and assassinations were driven by a desire to replace 'crazy theocratic murderers' with a new government, warning that replacing one such regime with another would not solve the problem. He compared
the potential outcome to World War II, suggesting the target regime could surrender now to 'the president's plan' or face the 'hard way' of further casualties and potential street uprisings. Halperin
clarified that he is not making a definitive prediction nor claiming his sources have confirmed this, but rather that his belief is based on the 'totality of what I know.'\n\nPublished date: March 26
2026, 20:21\n\nURL: https://www.realclearpolitics.com/video/2026/03/26/mark_halperin_my_hunch_is_theyve_had_a_secret_plan_for_iran_regime_change_all_along.html\nSource: Real Clear
Politics\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: Regime change only way to tackle Iran
threat, says former US NSA John Bolton - CNBC TV18\n\nSummary: \nFormer US National Security Advisor John Bolton argued on March 26, 2026, that regime change in Iran is the only viable solution to its
nuclear, economic, and geopolitical threats, dismissing diplomacy as ineffective. According to Bolton, the current regime itself is the core issue, and he stated, 'I don't think you solve any of the
underlying problems, not the nuclear threat, not the terrorist threat, not the threat to close the Strait of Hormuz until that government is gone.' Bolton called for continued military pressure to
destabilize the regime from within, suggesting the US should target key institutions like the Revolutionary Guard and support internal dissent with 'material assistance, with communications, with
finance, with weapons if they want it.' He expressed skepticism over ongoing diplomatic efforts, stating there is 'almost no overlap' between US and Iranian positions and that talks have 'the
slightest chance' of producing an agreement. Bolton also criticized the US administration's handling of the conflict, citing a lack of clear strategy in troop deployment. While calling a recent strike
that killed civilians 'a tragedy,' he insisted it was not intentional and does not alter the strategic calculus, warning that as long as the regime survives, threats to global energy markets will
persist.\n\nPublished date: March 26 2026, 15:41\n\nURL: https://www.cnbctv18.com/world/regime-change-only-way-to-tackle-iran-threat-says-former-us-nsa-john-bolton-ws-l-19875930.htm\nSource:
cnbctv18.com\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [13]\nTitle: White House Declares Mission Accomplished on
Regime Change in Iran\n\nSummary: \nOn March 25, 2026, White House Press Secretary Karoline Leavitt declared 'mission accomplished' regarding regime change in Iran, stating that 'there's been a change
in the regime leadership' and confirming the President was right. However, former National Security Adviser John Bolton disputed this assessment, telling CNN's Anderson Cooper that 'the faces may
change, but the ideology remains the same' and that the regime will only change when 'the ayatollahs and the Revolutionary Guard are gone.' According to The Washington Post, the Iranian Revolutionary
Guard Corps has 'only consolidated power' following U.S. and Israeli airstrikes that killed members of the Iranian regime.\n\nPublished date: March 25 2026, 20:08\n\nURL:
https://newrepublic.com/post/208173/white-house-karoline-leavitt-trump-mission-accomplished-regime-change-iran\nImage description: A photo of Karoline Leavitt standing at a podium with the White House
seal behind her and an American flag to her left.\nSource: The New Republic\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Middle
East\n\n</doc>\n\n<doc>\nCitation key: [14]\nTitle: LIVE MIDDEN-OOSTEN. VS stuurt 15-puntenplan naar Iran om oorlog te beëindigen - Iran laat niet-vijandige schepen weer door straat van Hormuz
varen\n\nSummary: \nOn March 25, 2026, the United States government presented a 15-point plan to Iran, as reported by Het Nieuwsblad and cited by Israel's Channel 12 News, aiming to end the ongoing
war. The plan, which includes a one-month ceasefire proposal, demands that the Iranian regime fully dismantle its nuclear weapons program, surrender its entire stockpile of enriched uranium to the
International Atomic Energy Agency (IAEA), and permanently cease nuclear weapons development. Additionally, Iran must stop arming and financing militias such as Hezbollah and Hamas, and agree to
restrictions on the number and range of its future missile arsenal. In exchange for these concessions, the plan offers the lifting of international sanctions and assistance in developing Iran's
civilian nuclear energy program. The document explicitly states that regime change is not part of the proposal. Regarding the Strait of Hormuz, the plan requires its reopening, a move reportedly
preceded by Iran allowing non-hostile ships to pass. While Axios reports that Iranian negotiators have agreed to certain points, The New York Times notes it remains unclear how Iranian leadership will
react to the full proposal, and Israel's position is currently unknown.\n\nPublished date: March 25 2026, 05:14\n\nURL: https://www.nieuwsblad.be/buitenland/live-midden-oosten.-vs-
stuurt-15-puntenplan-naar-iran-om-oorlog-te-beeindigen-iran-laat-niet-vijandige-schepen-weer-door-straat-van-hormuz-varen/27532402.html\nSource: Het Nieuwsblad\nClassification: World\nSentiment:
neutral\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Trump afirma que houve uma 'mudança de regime no Irã' e que o país fechará um acordo com os
EUA\n\nSummary: \nOn Tuesday, March 24, 2026, US President Donald Trump stated during the swearing-in ceremony of DHS Secretary Markwayne Mullin that the US is negotiating with a 'new group of
leaders' in Iran to conclude a peace deal, which he described as a 'regime change' in the country. Trump claimed these new leaders have agreed never to develop nuclear weapons. However, Trump did not
specify who these leaders are. The Iranian government has not commented on the matter. Iranian Parliament President Mohammad Baqer Qalibafele refuted the claims on social media platform X, stating,
'No negotiations have been held with the US, and fake news is used to manipulate financial and oil markets and escape the quagmire in which the US and Israel are trapped.'\n\nPublished date: March 24
2026, 19:07\n\nURL: https://valor.globo.com/mundo/noticia/2026/03/24/trump-afirma-que-houve-uma-mudana-de-regime-no-ir-e-que-o-pas-fechar-um-acordo-com-os-eua.ghtml\nSource: Valor
Econômico\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [16]\nTitle: Сценарий дал сбой: у США получилось
повторить в Иране иракскую схему\n\nSummary: \nAccording to an article published by Rambler on March 24, 2026, the United States has attempted to replicate a 'regime change' strategy in Iran similar
to those used in Iraq (2003) and Libya. The article claims that US President Donald Trump addressed the Iranian people and military on February 28, 2026, urging them to seize power and stating that
'this is likely their only chance for many generations' and 'the hour of freedom is near'. However, the text reports that this 'scenario failed' as mass rallies in support of the current regime were
observed, demonstrating 'solidarity of the Iranian people around the ruling elite'. Despite this stability, the article cites Semyon Bagdasarov, Director of the Center for the Study of Middle Eastern
Countries, who warns that opposition structures remain. These include the National Council of Iran, a monarchist group led by Crown Prince Reza Pahlavi residing in the US, and the National Council of
Resistance of Iran, led by Maryam Rajavi. Bagdasarov noted that the June 2025 joint US-Israel bombardment of Iran for 12 days revealed the presence of groups willing to cooperate with foreign powers.
The article concludes that the US intends to continue attempts to fragment Iranian society.\n\nPublished date: March 24 2026, 12:50\n\nURL: https://news.rambler.ru/army/56212356-stsenariy-dal-sboy-u-
ssha-poka-ne-poluchilos-povtorit-v-irane-irakskuyu-i-liviyskuyu-shemu/\nSource: Рамблер\nClassification: Politics\nSentiment: negative\nReporting voice: Subjective\nContinent:
Asia\n\n</doc>\n\n<doc>\nCitation key: [17]\nTitle: Funzionari Usa giudicano improbabile la caduta del regime iraniano e l'eliminazione permanente del nucleare\n\nSummary: \nOn March 23, 2026, US
officials, as reported by The Washington Post, have assessed it as 'improbable' that the United States can achieve maximum objectives regarding Iran, specifically the overthrow of the theocratic
regime and the permanent elimination of its nuclear capabilities. This cautious evaluation, cited by sources close to the US administration, reflects the complexity of the Middle East theater,
including Iran's internal resilience, regional alliances, and technical nuclear capacity. Analysts highlight that these ambitious goals carry high costs and risks of escalation, suggesting that
diplomacy remains crucial. The technical challenge of rendering nuclear capabilities 'out of reach' involves not just destroying facilities but controlling knowledge, infrastructure, and supply
chains. Politically, regime change could trigger deep regional consequences involving actors like Hezbollah, Gulf state actors, and Iran's strategic allies. Consequently, the US administration appears
shifting towards defining realistic, measurable goals to reduce escalation risks, prioritizing containment measures, targeted sanctions, financial pressure, cyber operations, and multilateral
initiatives over immediate regime change. This strategic realism aims to protect security interests while avoiding prolonged conflicts, despite fluid public diplomatic exchanges where Tehran has often
denied direct negotiations.\n\nPublished date: March 24 2026, 00:02\n\nURL: https://www.notizie.it/funzionari-usa-giudicano-improbabile-la-caduta-del-regime-iraniano-e-leliminazione-permanente-del-
nucleare/\nSource: Notizie.it\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key: [18]\nTitle: Трамп выразил надежду на
смену власти в Иране\n\nSummary: \nOn March 23, 2026, U.S. President Donald Trump expressed hope for a 'serious regime change' in Iran, telling NBC News that he believes there are 'very reasonable'
and 'very substantial' people within the country who could lead this transition. Trump cited the situation in Venezuela as a successful model, noting his good relations with Venezuelan President Delsi
Rodriguez and suggesting a similar figure might emerge in Iran. Conversely, Iranian Supreme Leader Ayatollah Mojtaba Khamenei, on March 20, dismissed U.S. and Israeli assumptions that they could
overthrow the Iranian government. Intelligence assessments support this view; Reuters reported on March 12 that U.S. intelligence evaluates the current Iranian regime as 'resilient' with no
anticipated regime change. Additionally, closed Israeli officials admitted there is 'no certainty' that war would lead to the collapse of the Iranian government.\n\nPublished date: March 23 2026,
17:33\n\nURL: https://iz.ru/2064735/tramp-vyrazil-nadezhdu-na-smenu-praviashchego-rezhima-v-irane-izi\nImage description: A street scene in an Iranian city featuring a large billboard with the Iranian
flag and figures in clerical robes, with two men in the foreground looking towards the billboard and green and yellow taxis in the street.\nSource: Izvestia.ru\nClassification: Politics\nSentiment:
negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [19]\nTitle: En Iran, le changement de régime a-t-il déjà eu lieu... au profit des Gardiens de la révolution ? -
RTBF Actus\n\nSummary: \nAccording to an article published on March 23, 2026, by RTBF, the Islamic Revolutionary Guard Corps (IRGC) in Iran has consolidated power, potentially marking a regime shift
in favor of the military organization. The IRGC, described as the regime's ideological army established in 1979, gained significant economic and political influence following the 1980-1988 war with
Iraq. By 2026, Mohammad Ghalibaf, the IRGC commander-in-chief, was serving as President of the Parliament. The article claims that in January 2026, the IRGC demonstrated its power through a 'massive
and deadly repression' of popular protests demanding the end of the regime. Furthermore, the text asserts that a war involving the United States and Israel completed the transfer of power to the
organization, which the European Union designates as a terrorist group.\n\nPublished date: March 23 2026, 15:05\n\nURL: https://www.rtbf.be/article/en-iran-le-changement-de-regime-a-t-il-deja-eu-lieu-
au-profit-des-gardiens-de-la-revolution-11698817\nSource: RTBF\nClassification: Politics\nSentiment: negative\nReporting voice: Analytical\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key:
[20]\nTitle: Iranian Opposition Voices Unite: Organized Resistance Presented as Only Path to Change - Iran News Update\n\nSummary: \nOn March 19, 2026, a major gathering of Iranian opposition
supporters took place outside European Union institutions in Brussels, calling for regime change in Iran through organized resistance rather than foreign military intervention or Western appeasement.
According to Reuters, demonstrators rejected both the current clerical regime and a return to monarchy. Shahin Gobadi, spokesperson for the People’s Mojahedin Organization of Iran (PMOI/MEK),
emphasized that neither war nor diplomatic concessions can resolve Iran’s crisis, advocating instead for a democratic transformation driven by the Iranian population. Gobadi called on the European
Union to recognize a transitional political framework based on the Ten-Point Plan proposed by Maryam Rajavi, president-elect of the National Council of Resistance of Iran (NCRI), which aims to
establish a secular, democratic republic. He urged European governments to close Iranian embassies, expel regime operatives, and hold Iranian officials accountable for human rights violations.
Political analyst Ramesh Sepehrrad, speaking to GB News, argued that the Islamic Revolutionary Guard Corps (IRGC) does not maintain unshakable control and highlighted an extensive network of
resistance units across Iranian provinces. She described the proposed transitional government under Rajavi as a structured, time-bound solution to prevent instability and guide the country toward
democratic elections. The coordinated efforts aim to position the organized resistance as a credible political successor to the Iranian regime.\n\nPublished date: March 23 2026, 09:58\n\nURL:
https://irannewsupdate.com/news/iranian-opposition/iranian-opposition-voices-unite-organized-resistance-presented-as-only-path-to-change/\nSource: irannewsupdate.com\nClassification:
Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n------News Summaries End------\n","offset":10,"hit_cache":false}
```

## 💬 Response

This is very informative. The situation in Iran is extremely dynamic. Let me now search for prediction markets and get more context on the CP trajectory.

## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "query": "Iran regime change government"
}
```

### 📋 Result

```
{"markets": [], "query": "Iran regime change government"}
```

## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__markets__get_coherence_links


```json
{
  "query": "Iran war ceasefire peace deal negotiations latest",
  "hours_back": 72,
  "n_articles": 5
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: مصادر: إيران تربط ملف التسوية بوقف الحرب على لبنان\n\nSummary: \nAccording to a source close to ongoing
negotiations, Iran has linked any settlement to an end to the Israeli war on Lebanon and the commencement of negotiations. The source stated that if these conditions are not met, Tehran will proceed
with a step to separate the United States from Israel, which involves committing to a ceasefire and an agreement with the Americans while keeping Israel as a target for Iranian missiles. The source
emphasized that conditions are constantly changing due to new factors influencing negotiations in Iran and subsequently in Lebanon, which was described as a 'appendage' to the Iranian file. The latest
factor cited was the Houthi threat to close the Bab el-Mandeb strait, which would raise the price of a barrel of oil, identified as a major concern for US President Donald Trump in global
markets.\n\nPublished date: March 30 2026, 06:04\n\nURL: https://arabic.rt.com/world/1772835-%D9%85%D8%B5%D8%A7%D8%AF%D8%B1-%D8%A5%D9%8A%D8%B1%D8%A7%D9%86-%D8%AA%D9%87%D8%AF%D8%AF-
%D9%88%D8%A7%D8%B4%D9%86%D8%B7%D9%86-%D9%88%D8%AA%D8%B1%D8%A8%D8%B7-%D9%88%D9%82%D9%81-%D8%A7%D9%84%D8%AD%D8%B1%D8%A8-%D8%A8%D9%84%D8%A8%D9%86%D8%A7%D9%86-%D8%A8%D9%85%D9%84%D9%81-
%D8%A7%D9%84%D8%AA%D9%81%D8%A7%D9%88%D8%B6/\nSource: RT Arabic\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key:
[2]\nTitle: 特朗普：伊朗已同意停火\"15点计划\"中的\"大部分内容\" | 星岛环球网\n\nSummary: \nOn March 29, 2026, former U.S. President Donald Trump told reporters aboard 'Air Force One' that Iran has agreed to 'most of the
content' of a 15-point ceasefire plan proposed by the United States to end the war. According to Trump, 'They agreed to most of the terms; why wouldn't they agree? We will still make a few other
demands.' However, it remains unclear whether formal negotiations are actually taking place. Reports indicate that Iran has publicly rejected the 15 ceasefire conditions delivered via Pakistan as an
intermediary and has instead proposed its own 5 conditions, including maintaining sovereignty over the Strait of Hormuz. Officials from Pakistan, Saudi Arabia, and Turkey held recent talks aimed at
resolving the escalating conflict that began on February 28, though the outcome of those discussions is unknown.\n\nPublished date: March 30 2026, 03:16\n\nURL:
https://www.stnn.cc/c/2026-03-30/4049345.shtml\nImage description: A photograph of Donald Trump wearing a dark suit, white shirt, and green tie, seated in what appears to be the Oval Office, with a
bust visible in the background.\nSource: 星岛环球网\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle: 美伊停戰15項方案
川普：伊朗已同意大部分、將放行20艘油輪 - 國際 - 自由時報電子報\n\nSummary: \nOn March 29, 2026, U.S. President Donald Trump stated that Iran has agreed to the majority of a 15-point ceasefire proposal, which includes limiting
Iran's defense capabilities, ceasing support for proxy groups, and recognizing the State of Israel. According to reports from CNN and Reuters, the deal also involves Iran releasing 20 oil tankers to
the United States, with loading operations set to begin the following day. This initiative, originally conveyed via Pakistan, is described by Trump as a significant step toward negotiations, following
his earlier comments about Iran sending a 'great gift' of 10 tankers, which has now been doubled.\n\nPublished date: March 30 2026, 01:36\n\nURL:
https://news.ltn.com.tw/news/world/breakingnews/5386922\nImage description: A close-up photograph of Donald Trump wearing a dark suit, white shirt, and a pink polka-dot tie, looking downwards with a
serious expression while holding onto a white surface.\nSource: Liberty Times Net\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: North
America\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: Trump dice que las negociaciones con Irán van \"extremadamente bien\" y que podría haber un alto el fuego pronto Por Investing.com\n\nSummary:
\nOn Sunday night, March 30, 2026, U.S. President Donald Trump stated aboard Air Force One that direct negotiations with Iran are 'extremely well' and that an agreement could be reached soon.
According to Trump, a deal is possible following recent U.S. attacks that killed several high-ranking Iranian officials, while he promoted the idea of a 'regime change' in Tehran. Trump claimed that
Tehran has allowed approximately 20 oil tankers to pass through the Strait of Hormuz as a concession to the U.S., with movements reportedly starting the following morning. However, Iran has largely
denied holding direct talks with Washington since the war began in late February, insisting on a ceasefire first. Trump declined to confirm if U.S. ground troops would be deployed, asserting that U.S.
forces are 'weeks ahead of schedule' and have eliminated Iran's air force, navy, and missile launch capabilities. Meanwhile, hostilities continue with Houthi attacks on Israel, exchanges of fire
between Iran and Israel, and the U.S. deploying thousands of troops to the Middle East. Trump noted that while he sees a potential agreement, it is 'possible that we do not' make one, without
providing a specific timeline.\n\nPublished date: March 30 2026, 01:29\n\nURL: https://es.investing.com/news/economy-news/trump-dice-que-las-negociaciones-con-iran-van-extremadamente-bien-y-que-
podria-haber-un-alto-el-fuego-pronto-3582591\nSource: Investing.com Español\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key:
[5]\nTitle: 特朗普：与伊朗“可能”很快达成停火协议\n\nSummary: \nOn March 29, 2026, US President Donald Trump told the UK's Financial Times that indirect negotiations between the United States and Iran, conducted via
Pakistan as an intermediary, are 'proceeding smoothly' (进展顺利). When asked if a ceasefire could be reached in the coming days and the Strait of Hormuz reopened, Trump did not provide specific details.
According to Trump, the US has bombed approximately 13,000 targets, has about 3,000 targets remaining, and has 'a few thousand more targets to strike' (还有几千个目标要打击). He stated that an agreement 'may be
reached very soon' (协议可能很快就能达成).\n\nPublished date: March 30 2026, 00:59\n\nURL: https://stcn.com/article/detail/3709267.html\nSource:
证券时报网_证券时报旗下资讯平台_股票_基金_期货_债券_理财_财经_行情_数据_股吧_博客_论坛\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [6]\nTitle: ترامب يكشف
كواليس التفاوض مع إيران\n\nSummary: \nUS President Donald Trump told the 'Financial Times' that negotiations with Iran are 'proceeding well' and hinted at a potential agreement to ensure a 'ceasefire'
with Iran, which could de-escalate military tensions in the region. Trump stated, 'We are negotiating with Iran directly and indirectly' to open all channels leading to a mutual agreement. These
remarks come amidst a 'military storm' of US-Israeli strikes targeting Tehran's nuclear and strategic sites, coinciding with the handover of power to Mojtaba Khamenei as the new 'Supreme Leader'
following his father's death. The campaign aims to undermine Iran's military capabilities and shift regional power balances.\n\nPublished date: March 30 2026, 00:35\n\nURL: https://www.masrawy.com/new
s/news_publicaffairs/details/2026/3/30/2964341/%D8%AA%D8%B1%D8%A7%D9%85%D8%A8-%D9%85%D9%81%D8%A7%D9%88%D8%B6%D8%A7%D8%AA%D9%86%D8%A7-%D9%85%D8%B9-%D8%A5%D9%8A%D8%B1%D8%A7%D9%86-
%D8%AA%D9%85%D8%B6%D9%8A-%D8%AC%D9%8A%D8%AF-%D8%A7-%D9%88%D8%A7%D8%AA%D9%81%D8%A7%D9%82-%D9%88%D9%82%D9%81-%D8%A7%D9%84%D9%86%D8%A7%D8%B1-%D9%85%D9%85%D9%83%D9%86\nImage description: A medium close-up
photograph of Donald Trump wearing a blue suit, white shirt, and red tie, standing in front of a blurred American flag background.\nSource: مصراوي.كوم\nClassification: Politics\nSentiment:
negative\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: Iran Agrees to Talks with US but Sets Tough Hormuz Condition, Global Tensions Shift |
महायुद्ध पर सबसे बड़ा अपडेट! US से बातचीत को राजी हुआ ईरान, लेकिन 'होर्मुज' पर रख दी ऐसी शर्त, हिल गई दुनिया | News Track in Hindi\n\nSummary: \nIn March 2026, Iran has agreed to ceasefire talks with
the US, but has set a series of strict conditions mediated by Pakistan, Saudi Arabia, and Turkey. According to the report by Harsh Srivastava of News Track, Tehran has presented a '5-point agenda'
which includes an immediate halt to all US and Israeli aerial and ground attacks, and written guarantees that future strikes on Iranian nuclear or military sites will not occur. The most significant
demand is Iran's claim for 'unilateral control' over the Strait of Hormuz, a strategic waterway through which 20% of the world's oil passes. This condition, if accepted by the US, would represent a
major strategic victory for Iran in the Middle East. The article notes that Iran has discarded the old 15-point agreement in favor of these new terms. High-level meetings are scheduled in Islamabad on
March 29-30, involving the foreign ministers of Saudi Arabia, Turkey, and Egypt, to finalize a roadmap. If successful, this could lead to a temporary ceasefire between March 31 and April 7. The
article highlights that Iran is seeking guarantees from Pakistan, Saudi Arabia, Turkey, and Egypt to ensure US compliance, as Tehran no longer trusts the US directly.\n\nPublished date: March 29 2026,
17:51\n\nURL: https://newstrack.com/world/iran-us-talks-ceasefire-hormuz-control-condition-pakistan-mediation-middle-east-588765\nSource: newstrack.com\nClassification: Politics\nSentiment:
neutral\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: थोड़ा नरम पड़ा ईरान, बातचीत को राजी, अब अमेरिका के सामने रखी ये कंडीशन, होर्मुज पर कर दी
ब\n\nSummary: \nIran has signaled a willingness to engage in talks with the United States, but only under specific conditions, as reported by News18 India. According to sources, Iran's primary
condition is an immediate halt to attacks on its territory, along with assurances from the US and Israel that no future attacks will occur. Iran has rejected a previous 15-point agreement proposed by
the US and now demands the acceptance of its own five conditions before resuming negotiations. A high-level meeting is scheduled to take place in Islamabad, Pakistan, on March 29-30, 2026, involving
representatives from Pakistan, Saudi Arabia, Turkey, and Egypt to develop a mediation roadmap. Pakistani Prime Minister Shehbaz Sharif has spoken with Iranian President Masoud Pezeshkian to support
de-escalation efforts, while Foreign Minister Ishaq Dar has discussed the agenda with Iranian Foreign Minister Abbas Araghchi. If positive outcomes emerge from the Islamabad talks, a ceasefire could
be established between March 31 and April 7, 2026.\n\nPublished date: March 29 2026, 12:07\n\nURL: https://hindi.news18.com/world/middle-east-iran-us-war-news-iran-ready-to-talk-with-5-conditions-
what-wants-on-hormuz-from-donald-trump-2-10319940.html\nSource: News18 India\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation
key: [9]\nTitle: 美伊互提\"战胜国\"条件，谁会先妥协？\n\nSummary: \nIran has reportedly responded to the United States' 15-point plan by proposing 5 hard-line conditions, emphasizing that any ceasefire must be based
on the assurance that war will not be repeated, according to a March 28, 2026 report by Phoenix New Media. Ni Xin Chun, Dean of the China-Arab States Research Institute at Ningxia University, stated
that the gap between the two sets of conditions is 'very large,' making it 'impossible' to reach an agreement under the current terms and even suggesting that the likelihood of the parties sitting
down to talk is 'very low.'\n\nPublished date: March 28 2026, 12:55\n\nURL: https://news.ifeng.com/c/8rrr1NBISP6\nImage description: Two military helicopters flying over the ocean with a large naval
aircraft carrier in the background.\nSource: 凤凰网（凤凰新媒体）\nClassification: Politics\nSentiment: negative\nReporting voice: Analytical\nContinent: Middle East\n\n</doc>\n\n<doc>\nCitation key:
[10]\nTitle: 4월 종전 관측에 떠오르는 '美·이란 부분협상' 가능성[美·이란 전쟁 한달]\n\nSummary: \nAmidst rising war costs and a potential one-month conflict between the US and Iran, a scenario for a 'partial agreement' or
'limited truce' by April is gaining traction as a realistic alternative to a comprehensive peace deal. According to the Wall Street Journal (WSJ), experts suggest that while both sides maintain
hardline demands, the prohibitive cost of war may force them to suspend hostilities first and defer core contentious issues—such as nuclear enrichment and missile programs—to future negotiations.
Michael Singh, former Middle East director at the US National Security Council (NSC), noted that the US could pursue a limited truce now, addressing major agendas in subsequent talks. The proposed
framework involves Iran suspending uranium enrichment for a set period in exchange for the US gradually easing sanctions and normalizing navigation in the Strait of Hormuz. Raz Jimti of the Israel
National Security Institute (INSS) stated that while Iran's leadership desires a truce, they are unwilling to accept any conditions, likely requiring a guarantee against further US and Israeli
attacks. The article highlights the 2015 Joint Comprehensive Plan of Action (JCPOA) under the Obama administration as a historical precedent where sensitive issues like missile programs were excluded
to secure a deal. Former US Ambassador to Israel Daniel Shapiro added that while Saudi Arabia and the UAE push for the total elimination of Iran's military threat, a long war makes forcing a complete
surrender difficult, making a compromise agreement feasible. Consequently, a deal prioritizing a ceasefire and reopening the Strait of Hormuz is considered the most likely scenario, while nuclear
stockpiles, missile programs, and militia support remain long-term negotiation points.\n\nPublished date: March 28 2026, 11:47\n\nURL: https://biz.heraldcorp.com/article/10704752\nImage description: A
silhouette of a man resembling Donald Trump pointing at a map projection of the Middle East, specifically highlighting the 'Strait of Hormuz' in blue text.\nSource: 헤럴드경제\nClassification:
Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: Trump On Hold? 3 Reasons Why Iran Isn't Picking Up The Phone For Peace
Talks\n\nSummary: \nAs the war between the United States, Israel, and Iran continues, diplomatic efforts to end hostilities are stalled due to mutual distrust, indirect communication channels, and
security concerns. According to the US government, a 15-point peace proposal has been shared with Iran, demanding a halt to uranium enrichment and other military activities, though Tehran has
criticized the plan as one-sided. Since direct senior-level talks have not resumed since the conflict began, Washington and its partners rely on third-party intermediaries—specifically Pakistan,
Turkey, Egypt, and Oman—to relay messages, as reported by Axios. From Iran's perspective, continuing the war effort remains a priority; Iranian leaders have rejected ceasefire talks, stating they will
not negotiate while under attack. According to Iranian media, the leadership believes the war will conclude on its own terms. Iran's Foreign Minister Abbas Araghchi described the situation as a
'golden, glorious moment' for Iran, claiming that 'no nation in history has stood for nearly a month against the greatest nuclear-armed power on earth and stopped them from achieving a single goal.'
Beyond pride, deep mistrust persists; past indirect talks, such as nuclear negotiations earlier in 2026, occurred through intermediaries because neither side trusted the other. Additionally, US
officials report that Iranian negotiators are avoiding phone use to prevent tracking or assassination, a security fear highlighted by sources at a recent G7 meeting. These factors combined mean it
takes much longer for mediators to get replies and for positions to be clarified, preventing meaningful progress toward direct negotiations or a ceasefire.\n\nPublished date: March 28 2026,
07:59\n\nURL: https://www.news18.com/explainers/trump-on-hold-3-reasons-why-iran-isnt-picking-up-the-phone-for-peace-talks-ws-l-10002254.html\nSource: News18\nClassification: World\nSentiment:
negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: 陸外長：願與巴基斯坦共同促和止戰 | ETtoday大陸新聞 | ETtoday新聞雲\n\nSummary: \nOn March 27, 2026, Chinese Foreign
Minister Wang Yi spoke with Pakistan's Deputy Prime Minister and Foreign Minister, Ahsan Iqbal (referred to as 'Dart' in the text, likely a transcription error for a specific official, but the text
uses 'Dart'), regarding the one-month anniversary of the war between the United States and Iran. According to CCTV reports, the Pakistani official outlined the latest situation in Iran and expressed
gratitude for China's support in mediation efforts, stating that a ceasefire and restoration of peace are shared goals. The Pakistani official emphasized that the current moment is critical for
restarting talks and urged the international community to encourage the US and Iran to return to the negotiating table. Foreign Minister Wang Yi affirmed that China and Pakistan are strategic partners
with aligned objectives and positions, praising Pakistan's efforts to de-escalate the situation and supporting its continued role as a mediator. Wang Yi noted that while initiating talks is difficult,
it is essential to prevent further casualties, stop the spread of conflict, and restore normal navigation in the Strait of Hormuz. Both sides agreed to jointly promote a ceasefire, resume
negotiations, ensure the safety of non-military targets and shipping lanes, and support the United Nations in playing a primary role.\n\nPublished date: March 28 2026, 07:31\n\nURL:
https://www.ettoday.net/news/20260328/3139949.htm\nImage description: A close-up photograph of Chinese Foreign Minister Wang Yi wearing a dark suit and tie, with a headset microphone, standing in
front of a blurred red Chinese flag with yellow stars.\nSource: ETtoday新聞雲\nClassification: World\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key:
[13]\nTitle: США ожидают переговоров с Ираном уже на этой неделе -- Виткофф\n\nSummary: \nUS Special Envoy Steve Witkoff stated that negotiations with Iran could take place 'this week,' citing ongoing
naval movements as a 'very good sign' during a conference in Miami on Friday, March 27. Earlier, US Secretary of State Marco Rubio claimed the war in Iran would end within weeks, noting the US is 'on
the verge of achieving its goals.' President Donald Trump had previously announced on March 23 that the US and Iran were negotiating a cessation of hostilities with 'important points of contact,'
emphasizing that Iran must agree to have no nuclear weapons for a deal to be reached. On March 24, Israeli outlet Ynet reported that new Iranian Supreme Leader Mojtaba Khamenei agreed to negotiations,
following Tehran's initial rejection of such claims. On March 25, The New York Times cited diplomatic sources stating the US sent a 15-point plan via Pakistan to end the war in the Middle East,
covering ballistic missiles and nuclear programs. Iran countered with a ceasefire proposal demanding military reparations and sovereignty over the Strait of Hormuz. On March 26, Trump announced a
10-day delay in strikes on Iranian energy facilities, extending the deadline to Monday, April 6, 2026, at 20:00 ET. On March 27, The Wall Street Journal reported that the Pentagon is considering
deploying up to 10,000 US troops to the Middle East amid rising tensions.\n\nPublished date: March 28 2026, 04:35\n\nURL: https://nv.ua/world/geopolitics/uitkoff-zayavil-o-vozmozhnyh-peregovorah-ssha-
i-irana-uzhe-na-etoy-nedele-50595618.html\nSource: Новое Время\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key:
[14]\nTitle: 中巴就伊朗局势达成共识，共同推动停火止战恢复和谈\n\nSummary: \nOn March 27, 2026, Chinese Politburo member and Foreign Minister Wang Yi spoke with Pakistani Foreign Minister Bilawal Bhutto Zardari regarding the
Iran situation. According to the report, both countries reached a consensus to jointly promote a ceasefire and the resumption of peace talks between the United States and Iran. They agreed that
'political settlement is the only way out' and emphasized the need to replace military pressure with dialogue and negotiation. The report notes that this diplomatic coordination demonstrates the
responsibility of major powers and aims to inject a 'coolant' into the tense regional situation, helping to prevent further escalation of conflict.\n\nPublished date: March 28 2026, 01:05\n\nURL:
https://k.sina.com.cn/article_1411489797_5421a00504003pedi.html\nSource: k.sina.com.cn\nClassification: Politics\nSentiment: neutral\nReporting voice: Analytical\nContinent:
Asia\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Com impasse entre Trump e Irã, petróleo sobe e volta a superar US$ 100\n\nSummary: \nAmidst a diplomatic impasse and uncertainty surrounding
negotiations between the United States and Iran regarding a potential ceasefire in the Middle East, international oil prices surged back above US$100 on Friday morning (March 27). U.S. President
Donald Trump announced on Thursday (March 26) that he would extend a truce on attacks against Iranian energy facilities by an additional 10 days. Trump expressed hesitation regarding a peace deal,
stating, 'I don't know if we will be able to do it. I don't know if we are willing to do it,' while simultaneously claiming that Tehran is 'begging to reach an agreement.' In response to U.S. military
movements, Iranian Foreign Minister Abbas Araghchi alleged on Thursday that U.S. soldiers are using citizens of Gulf Cooperation Council (GCC) countries as 'human shields' by relocating from military
bases to hotels. Araghchi suggested that hotels in GCC nations should refuse reservations to military officers to prevent endangering guests. Meanwhile, German Foreign Minister Johann Wadephul
indicated that direct negotiations between the U.S. and Iran are expected to take place soon in Pakistan.\n\nPublished date: March 27 2026, 12:59\n\nURL: https://www.metropoles.com/negocios/com-
impasse-entre-trump-e-ira-petroleo-sobe-e-volta-a-superar-us-100\nSource: Metrópoles\nClassification: Politics\nSentiment: negative\nReporting voice: Objective\nContinent: Middle East\n\n</doc>\n\n
------News Summaries End------\n","offset":5,"hit_cache":false}
```

```json
{
  "post_id": 38770
}
```

### 📋 Result

```
[]
```

## 💬 Response

Now let me analyze the situation carefully. Let me also check for any Metaculus meta-question data.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let's analyze the CP trajectory and current situation\n\nimport numpy as np\n\n# CP data points (weekly snapshots)\ndates = ['2026-02-22', '2026-03-01', '2026-03-08', '2026-03-15', '2026-03-22', '2026-03-29']\ncp_values = [33.0, 42.0, 45.0, 37.5, 28.0, 20.0]\n\n# Weekly changes\nchanges = [cp_values[i] - cp_values[i-1] for i in range(1, len(cp_values))]\nprint(\"Weekly CP changes:\", changes)\nprint(\"Average weekly change (last 3 weeks):\", np.mean(changes[-3:]))\nprint(\"Current CP:\", cp_values[-1])\nprint(\"Threshold:\", 20.0)\n\n# The question is: will CP be > 20% on April 11?\n# That's about 13 days from March 29, or about 1.8 weeks\n\n# Key situation analysis:\n# 1. The CP has been declining steadily: 45 -> 37.5 -> 28 -> 20 (decline of 8.3/week avg)\n# 2. The US and Israel are bombing Iran since Feb 28\n# 3. Khamenei has been killed, Mojtaba Khamenei is new Supreme Leader\n# 4. Trump claims \"regime change\" happened\n# 5. BUT - the Islamic Republic is STILL in place, Pezeshkian still president,\n#    Guardian Council still exists, constitution still says Islamic Republic\n# 6. Negotiations are ongoing for ceasefire\n# 7. Analysts say regime change is unlikely - IRGC has consolidated power\n# 8. US 15-point plan explicitly says \"regime change is not part of the proposal\"\n\nprint(\"\\n--- Analysis ---\")\nprint(\"The underlying question asks about FULL regime change:\")\nprint(\"- Khamenei, Pezeshkian, AND Guardian Council all must lose power\")  \nprint(\"- Constitution must no longer say 'Islamic Republic'\")\nprint(\"- This is an extremely high bar\")\nprint(\"\\nKey insight: Khamenei was killed, but Mojtaba Khamenei replaced him.\")\nprint(\"Pezeshkian is still president. Guardian Council still exists.\")\nprint(\"Constitution still refers to Islamic Republic.\")\nprint(\"The resolution criteria are NOT met by the current situation.\")\nprint(\"\\nThe CP decline from 45% to 20% reflects this reality:\")\nprint(\"- Initial spike was from the dramatic US/Israel attack\")\nprint(\"- As it became clear the regime survived, CP declined\")\nprint(\"- Ceasefire negotiations suggest the regime will persist\")\n\n# Model: What should the CP be?\n# The regime has survived a month of bombing. If a ceasefire happens,\n# regime change becomes very unlikely before 2027.\n# If no ceasefire, continued bombing could weaken regime further,\n# but even then, full constitutional change is extremely unlikely.\n\n# For the meta-question: will CP > 20% on April 11?\n# Current CP = 20.00% (exactly at threshold)\n# Trend is strongly downward\n# But we need to consider:\n# 1. Possibility of dramatic escalation that could spike CP\n# 2. Possibility of continued decline\n# 3. Possibility of stabilization around current levels\n\nprint(\"\\n--- Scenarios ---\")\nprint(\"Scenario 1: Ceasefire reached (probability ~30-40%)\")\nprint(\"  -> CP likely drops below 20% (regime persists, less time pressure)\")\nprint(\"Scenario 2: War continues, no ceasefire (probability ~50-60%)\")  \nprint(\"  -> CP could go either way, but regime surviving a month suggests resilience\")\nprint(\"  -> CP likely stays around 15-25%\")\nprint(\"Scenario 3: Major escalation / ground invasion (probability ~10%)\")\nprint(\"  -> CP could spike back up\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Weekly CP changes: [9.0, 3.0, -7.5, -9.5, -8.0]\nAverage weekly change (last 3 weeks): -8.333333333333334\nCurrent CP: 20.0\nThreshold: 20.0\n\n--- Analysis ---\nThe
underlying question asks about FULL regime change:\n- Khamenei, Pezeshkian, AND Guardian Council all must lose power\n- Constitution must no longer say 'Islamic Republic'\n- This is an extremely high
bar\n\nKey insight: Khamenei was killed, but Mojtaba Khamenei replaced him.\nPezeshkian is still president. Guardian Council still exists.\nConstitution still refers to Islamic Republic.\nThe
resolution criteria are NOT met by the current situation.\n\nThe CP decline from 45% to 20% reflects this reality:\n- Initial spike was from the dramatic US/Israel attack\n- As it became clear the
regime survived, CP declined\n- Ceasefire negotiations suggest the regime will persist\n\n--- Scenarios ---\nScenario 1: Ceasefire reached (probability ~30-40%)\n  -> CP likely drops below 20% (regime
persists, less time pressure)\nScenario 2: War continues, no ceasefire (probability ~50-60%)\n  -> CP could go either way, but regime surviving a month suggests resilience\n  -> CP likely stays around
15-25%\nScenario 3: Major escalation / ground invasion (probability ~10%)\n  -> CP could spike back up\n", "stderr": "", "duration_ms": 207}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# More detailed probabilistic analysis\n# Current CP = 20.00% (exactly at threshold, need STRICTLY higher)\n# Need to model where CP will be on April 11\n\n# Key considerations:\n# 1. CP has been declining ~8 pts/week for 3 straight weeks\n# 2. But at 20%, the decline may slow (floor effects - can't go much below ~5%)\n# 3. The war is actively ongoing with active ceasefire talks\n# 4. Resolution criteria for underlying Q require constitutional change - very high bar\n\n# Let me think about this differently:\n# What would PUSH CP above 20%?\n# - Ground invasion / major escalation\n# - Regime visibly crumbling (military coups, mass defections)\n# - Iran losing territory\n# - Constitutional crisis\n\n# What would PUSH CP below 20%?  \n# - Ceasefire agreement\n# - Continued regime stability\n# - Peace deal negotiations\n# - Time passing without regime change (closer to Jan 2027 deadline)\n\n# The CP is at EXACTLY 20% and needs to be STRICTLY above 20% to resolve YES\n# With a strong downward trend, the default path pushes below\n\n# However, the situation is genuinely uncertain:\n# - Active war is ongoing\n# - Trump is claiming regime change\n# - There are ceasefire talks but they could fail\n# - If talks fail and war escalates, CP could spike back up\n\n# Let me model this with scenarios:\nnp.random.seed(42)\nn_sims = 100000\n\n# Model weekly change in CP\n# Historical changes: [9.0, 3.0, -7.5, -9.5, -8.0]\n# The first two were upward (war started, dramatic events)\n# Last three were strongly downward (reality setting in)\n\n# For the next ~2 weeks, I'll model different scenarios:\n\nresults = []\n\nfor _ in range(n_sims):\n    cp = 20.0\n    \n    # Determine scenario\n    r = np.random.random()\n    \n    if r < 0.30:\n        # Ceasefire/deal reached - CP drops\n        # ~-5 to -10 from current\n        weekly_drift = -4.0\n        weekly_vol = 3.0\n    elif r < 0.75:\n        # War continues, gradual decline but slowing\n        # Regime proving resilient, trend continues but slower\n        weekly_drift = -2.0\n        weekly_vol = 4.0\n    elif r < 0.90:\n        # Stalemate / talks drag on, uncertainty\n        weekly_drift = 0.0\n        weekly_vol = 5.0\n    else:\n        # Major escalation / ground invasion\n        weekly_drift = 5.0\n        weekly_vol = 6.0\n    \n    # Simulate ~1.8 weeks\n    for week in range(2):\n        change = np.random.normal(weekly_drift, weekly_vol) * (0.9 if week == 1 else 1.0)\n        cp += change\n        cp = max(2, min(80, cp))  # Bound CP\n    \n    results.append(cp)\n\nresults = np.array(results)\nprob_above_20 = np.mean(results > 20.0)\n\nprint(f\"Probability CP > 20% on April 11: {prob_above_20:.3f}\")\nprint(f\"Median CP: {np.median(results):.1f}%\")\nprint(f\"Mean CP: {np.mean(results):.1f}%\")\nprint(f\"10th/90th percentile: {np.percentile(results, 10):.1f}% / {np.percentile(results, 90):.1f}%\")\nprint(f\"25th/75th percentile: {np.percentile(results, 25):.1f}% / {np.percentile(results, 75):.1f}%\")\n\n# Distribution of final CP\nbins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 80]\nhist, _ = np.histogram(results, bins=bins)\nprint(\"\\nCP distribution:\")\nfor i in range(len(bins)-1):\n    pct = hist[i] / n_sims * 100\n    print(f\"  {bins[i]:3d}-{bins[i+1]:3d}%: {pct:5.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Probability CP > 20% on April 11: 0.279\nMedian CP: 15.8%\nMean CP: 16.9%\n10th/90th percentile: 8.8% / 26.5%\n25th/75th percentile: 11.9% / 20.7%\n\nCP distribution:\n
0-  5%:   2.1%\n    5- 10%:  12.9%\n   10- 15%:  29.7%\n   15- 20%:  27.3%\n   20- 25%:  15.2%\n   25- 30%:   6.8%\n   30- 35%:   3.3%\n   35- 40%:   1.7%\n   40- 50%:   0.9%\n   50- 60%:   0.1%\n
60- 80%:   0.0%\n", "stderr": "", "duration_ms": 252}
```

## 💭 Thinking

Let me think more carefully about this. The simulation gives ~28% probability of CP being above 20% on April 11. Let me think about whether my scenario weights are right.

Key factors:
1. CP is exactly at 20% right now (March 29) - the threshold
2. Strong downward trend: -7.5, -9.5, -8.0 per week for 3 weeks
3. Time to resolution: ~13 days (~1.8 weeks)
4. Active US-Iran war ongoing since Feb 28
5. Khamenei killed, but regime survived - Mojtaba Khamenei is new Supreme Leader


6. Ceasefire negotiations are happening with Trump claiming progress, though the US 15-point plan explicitly rules out regime change
7. Intelligence assessments suggest the regime is resilient, but the resolution criteria demand full regime change—a constitution rewrite and removal of all leaders—which sets an extremely high bar
8. The war could still escalate or ground invasion could happen, ceasefire talks might collapse, and some of the 205 forecasters could shift upward on dramatic developments or Trump's rhetoric about regime change

But the downward trend is what stands out to me—the probability has been dropping 8 points per week for three straight weeks and is now right at the 20% threshold. Combined with the regime demonstrating resilience after a month of heavy bombing, the ceasefire talks progressing, and the fundamental reality that constitutional change is something no one realistically expects, I think the momentum carries CP below 20% over the next nine months.

My simulation suggested around 28%, but accounting for the genuine volatility an active war introduces—the possibility of escalation if talks collapse, the unpredictability of the situation—I'm settling on something in the 30-35% range. The trend is clearly downward, but there's enough uncertainty baked into an ongoing conflict that I can't dismiss the tail risks entirely.

The core tension is that CP sits exactly at 20%, so even a modest reversal would push it above that threshold. The ceasefire talks progressing and the regime's demonstrated resilience both point downward, but a ground invasion or complete collapse of negotiations could shift things sharply upward in the next two weeks. I'm weighing whether the most likely scenarios—continued negotiations or a ceasefire agreement—outweigh the plausible shock events that could spike the probability significantly. to be progressing (even if slowly), and the trend is strongly downward, I'll estimate around 30-35% probability.

Let me also consider: even in the "war continues" scenario, the CP has been declining because the regime is surviving. So continued war + regime survival = continued CP decline. Only an escalation that genuinely threatens the regime would push CP up.

I'll go with approximately 35% - acknowledging the genuine uncertainty from an active war but weighting the strong downward trend and fundamentals.

Wait, let me reconsider one more time. The fact that the CP is at EXACTLY 20.00% is important. If it were at 22% or 25%, I'd be more confident it stays above. If it were at 18%, I'd be more confident it stays below. At exactly 20%, even small fluctuations matter.

But the trend is so strongly downward (-8/week for 3 weeks) that "small fluctuations" around 20% seem less likely than a continued move down. The momentum is what matters here, and reversals require something substantial to shift. Given that, I'm settling on roughly 35% for YES on April 11, then I should run a reflection check on this reasoning.

## 💬 Response

Let me now think about this more carefully and run the reflection.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also consider: what does the underlying question's fundamentals suggest?\n# The resolution criteria require:\n# 1. Neither Khamenei, Pezeshkian, NOR Guardian Council have formal political authority\n# 2. Iran's constitution does not refer to Islamic Republic\n# Both must be met before Jan 1, 2027\n\n# Current status:\n# - Ali Khamenei: KILLED (but Mojtaba Khamenei replaced him as Supreme Leader)\n# - Masoud Pezeshkian: Still President\n# - Guardian Council: Still exists and functions\n# - Constitution: Still refers to Islamic Republic\n\n# For the question to resolve YES, ALL of the above must change\n# This is an EXTREMELY high bar - essentially full regime overthrow + constitutional change\n\n# Even in a scenario where the regime falls, getting a new constitution\n# in place before Jan 1, 2027 would be very difficult\n\n# The fine print says \"if no entity controls majority of territory\" it also resolves YES\n# So a complete state collapse would also resolve YES\n\n# What probability should forecasters assign to this?\n# Given:\n# - The regime survived a month of heavy US/Israel bombing\n# - IRGC has consolidated power\n# - US intelligence assesses regime as \"resilient\"  \n# - Ceasefire talks are progressing\n# - No ground invasion yet\n# - US plan explicitly excludes regime change\n\n# A reasonable fundamental probability: 5-15%\n# This suggests CP should be heading toward that range\n\n# If CP is heading toward 10-15%, it will be BELOW 20% by April 11\n\n# The only way CP goes ABOVE 20%:\n# - Major escalation event (ground invasion, mass defections, territory loss)\n# - These are possible but not the base case\n\n# Let me refine my estimate considering the asymmetry\n# The \"floor\" CP is probably around 5-10% (base rate for regime change even with war)\n# The ceiling could be 40-50% if major escalation\n# Current CP of 20% is already above what fundamentals suggest\n\n# Probability that CP ends up above 20%:\n# - Need an escalation event (prob ~15-20%)\n# - OR CP just doesn't move much (possible but trend says unlikely)\n# - OR new forecasters enter with higher estimates (possible but 205 forecasters is decent)\n\nprint(\"Summary assessment:\")\nprint(\"CP at exactly 20.00% with strong downward trend\")\nprint(\"Fundamentals suggest CP should be 10-15% (regime is surviving)\")\nprint(\"Only upside: major escalation event\")\nprint()\nprint(\"P(CP > 20% on Apr 11) \u2248 30-35%\")\nprint(\"- 65-70% chance trend continues and CP drops to 12-18%\")\nprint(\"- 25-30% chance war escalation pushes CP back above 20%\")\nprint(\"- 5% chance dramatic events push CP well above 20%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Summary assessment:\nCP at exactly 20.00% with strong downward trend\nFundamentals suggest CP should be 10-15% (regime is surviving)\nOnly upside: major escalation
event\n\nP(CP > 20% on Apr 11) \u2248 30-35%\n- 65-70% chance trend continues and CP drops to 12-18%\n- 25-30% chance war escalation pushes CP back above 20%\n- 5% chance dramatic events push CP well
above 20%\n", "stderr": "", "duration_ms": 0}
```
