# Reasoning Log: Will CDC’s official U.S. human A(H5N1) case tally increase by at least one before April 30, 2026?

*Generated: 2026-03-25T19:43:05.555076+00:00*


## 💭 Thinking

Let me analyze this forecasting question about whether CDC's official U.S. human A(H5N1) case tally will increase by at least one before April 30, 2026.

Key details:
- Resolution: CDC's official count must be at least 1 higher on April 30, 2026 than on March 16, 2026
- Resolution source: CDC's A(H5) Bird Flu Current Situation page
- Window: March 16, 2026 to April 30, 2026 (about 45 days)
- Published: March 25, 2026
- Scheduled close: March 25, 2026 (today)


- I need to look into the current H5N1 situation in the US to assess the likelihood of at least one new case being reported in this timeframe.

## 💬 Response

I'll analyze this question about H5N1 cases in the US. Let me research the current situation.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42810
  ]
}
```

### 📋 Result

```
{"post_id": 42810, "title": "Will CDC\u2019s official U.S. human A(H5N1) case tally increase by at least one before April 30, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/42810", "background_info": "This question tracks whether the United States records another officially confirmed human H5N1 infection during the resolution
window.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"c762f5838fb32d5d\",\"sheet_id\":449.0}}`", "resolution_criteria": "This question resolves to yes if CDC\u2019s official U.S.
human A(H5N1) case tally is at least one higher on April 30, 2026 than it was on March 16, 2026, using CDC\u2019s A(H5) Bird Flu Current Situation page at [https://www.cdc.gov/bird-flu/situation-
summary/index.html](https://www.cdc.gov/bird-flu/situation-summary/index.html) It resolves to no otherwise.", "fine_print": "Use CDC\u2019s own confirmed U.S. human case count, not state reports or
media reports that CDC has not yet incorporated. If the summary page is unavailable, use CDC\u2019s human-case surveillance chart. Candidate Sources: CDC Global Human Cases with Influenza A(H5N1) page
[https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html](https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html)", "num_forecasters": 7, "community_prediction":
null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "url": "https://www.cdc.gov/bird-flu/situation-summary/index.html",
  "prompt": "What is the current total number of confirmed human H5N1 cases in the US? What is the most recent case date? Any recent updates?"
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/bird-flu/situation-summary/index.html", "content": "Based on the provided content:\n\n**Total confirmed human H5N1 cases in the US:** 71 cases reported since February
2024\n- 64 cases detected through human monitoring\n- 7 cases detected through national flu surveillance\n\n**Most recent case date:** Not specified in the content\n\n**Recent updates:**\n- In January
2025, CDC updated testing requirements: After a public health laboratory's first three H5N1 cases are confirmed by CDC, subsequent detections by that laboratory can be considered confirmatory without
additional CDC confirmation\n- USDA data on HPAI detections in animals is no longer reported on the CDC website (moved to USDA's website)\n- CDC continues to monitor the situation and reports cases
monthly\n\n**Current public health risk:** Low\n\nRelevant links:\n- [A(H5) Bird Flu Surveillance and Human Monitoring | Bird Flu | CDC](https://www.cdc.gov/bird-flu/h5-monitoring/index.html)\n-
[USDA's HPAI Data](https://www.aphis.usda.gov/h5n1-hpai)\n- [FluView](https://www.cdc.gov/fluview/index.html)\n- [CSTE guidance on Novel Influenza
A](https://cdn.ymaws.com/www.cste.org/resource/resmgr/position_statements_files_2023/24-ID-09_Novel_Influenza_A.pdf)\n- [CDC Updated Requirements (January
2025)](https://www.aphl.org/programs/infectious_disease/influenza/Documents/Highly%20Pathogenic%20Avian%20Influenza%20A%28H5N1%29_FAQ_050625.pdf)", "title": "A(H5) Bird Flu: Current Situation"}
```

```json
{
  "query": "H5N1 bird flu human cases United States 2026",
  "n_articles": 10,
  "hours_back": 720,
  "categories": [
    "Health"
  ]
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: Cos'è l'influenza aviaria ed i pericoli per l'uomo - Sanità - Ansa.it\n\nSummary: \nAccording to the
European Centre for Disease Prevention and Control (Ecdc), the risk of avian influenza infection for the general population is 'low', though it may become 'moderate' for workers exposed in confirmed
outbreaks. On March 25, 2026, Italy identified its first-ever human case of avian influenza, caused by the H9N2 strain, in a patient in Lombardy. According to epidemiologist Gianni Rezza, this strain
is 'less aggressive' compared to the high-mortality H5N1 virus, which has a lethality rate of approximately 50% and has caused about 1,000 human cases globally since 2000, mostly in Asia and Africa.
The H9N2 strain has resulted in approximately 170 human cases worldwide to date. The primary transmission route is inhalation of contaminated particles from infected animals, while the European Food
Safety Authority (Efsa) states there is no evidence of transmission through consumption of contaminated meat. Although the H5N1 virus has recently been found in raw milk batches in the USA, the
Italian case involves a low-pathogenicity virus. Surveillance in Italy is managed by veterinary services for animals and the Istituto Superiore di Sanità (ISS) for humans.\n\nPublished date: March 25
2026, 18:42\n\nURL: https://www.ansa.it/canale_saluteebenessere/notizie/sanita/2026/03/25/cose-linfluenza-aviaria-ed-i-pericoli-per-luomo_eea1871a-4d4a-4049-9894-7ad855ada80d.html\nSource:
ANSA.it\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: Influenza aviaria a Monza: cosa sappiamo sul virus e i
pericoli per l'uomo\n\nSummary: \nOn Wednesday, March 25, 2026, the first human case of avian influenza was confirmed in Monza, Lombardy, Italy, involving the low-pathogenicity A(H9N2) virus strain,
according to epidemiologist Gianni Rezza. The infection, identified in a human in Lombardy, marks the first such diagnosis in the country's history. While avian viruses primarily affect
birds—especially wild and aquatic species—and have recently been transmitted to mammals like cattle and cats, there is currently no confirmed evidence of human-to-human transmission. The European
Centre for Disease Prevention and Control (Ecdc) states the risk to the general population is 'low,' though it may become 'moderate' for workers exposed in infected farms. The Italian National
Institute of Health (Iss) notes that while most avian viruses are relatively harmless to humans, mutations could increase their ability to infect other species. Transmission typically occurs through
inhaling contaminated particles from infected animals or products, not via consumption of contaminated meat, as confirmed by the European Food Safety Authority (Efsa). Globally, since the early 2000s,
approximately 1,000 human cases of the high-mortality H5N1 strain have been recorded, primarily in Asia and Africa, with a case fatality rate of around 50%. In contrast, the H9N2 strain identified in
Italy is far less aggressive, with only about 170 human cases reported worldwide to date.\n\nPublished date: March 25 2026, 16:57\n\nURL:
https://www.ilmessaggero.it/salute/medicina/influenza_aviaria_cosa_e_sintomi_come_si_trasmette-9437990.html\nImage description: Personnel wearing white protective suits and red gloves holding several
small yellow chicks behind a wire fence.\nSource: Il Messaggero\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle:
Detectan en Italia el primer caso en Europa de gripe aviar A (H9N2) en humanos\n\nSummary: \nOn March 25, 2026, the Italian Ministry of Health announced the detection of the first human case of avian
influenza A (H9N2) in Europe, located in the Lombardy region. The patient, a person with pre-existing conditions and frailty, contracted the infection in a non-EU country before traveling to Italy and
is currently hospitalized. According to the Ministry, the virus is of animal origin with low pathogenicity, and transmission occurs through direct exposure to infected poultry or contaminated
environments. The World Health Organization notes that global human cases typically present with mild symptoms, and 'no transmission from person to person' has ever been reported for this variant.
Italian authorities, coordinating with the Superior Institute of Health (ISS), have activated surveillance protocols and identified all close contacts for monitoring, concluding that no critical
situations have been detected as of now. In contrast, the article notes that the UK previously recorded isolated cases of the highly pathogenic A(H5N1) strain, and in January 2025, reported another
case of avian flu without specifying the strain, while the US confirmed the first human death from the H5N5 strain in November 2025.\n\nPublished date: March 25 2026, 16:45\n\nURL:
https://www.20minutos.es/internacional/detectan-italia-primer-caso-europa-gripe-aviar-h9n2-humanos_6950752_0.html\nSource: 20 minutos\nClassification: Health\nSentiment: neutral\nReporting voice:
Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: In Lombardia primo caso di aviaria umana nella Ue. Rezza: nessun allarme\n\nSummary: \nOn March 25, 2026, epidemiologist
Gianni Rezza stated that there is 'no alarm' in Italy following the identification of the first human case of avian influenza A(H9N2) in the European Union, which occurred in a man in Lombardy.
According to Rezza, speaking to ANSA, the case is 'imported from abroad' and involves a low-pathogenicity virus with 'no human-to-human transmission,' making it an 'isolated case.' Rezza noted that
while the virus circulates widely in bird populations in Asia and West Africa, it causes mild symptoms in humans and has 'significantly lower virulence' than strains like H5N1 or H7N9. However, he
emphasized that global attention on animal-transmitted viruses must remain high due to the 'possible risk of species jumping.'\n\nPublished date: March 25 2026, 16:06\n\nURL:
https://gazzettadelsud.it/articoli/cronaca/2026/03/25/in-lombardia-primo-caso-di-aviaria-umana-nella-ue-rezza-nessun-allarme-62e53cf2-1db6-4b0f-9eb4-c2cb69bd0812/\nSource: Gazzetta del
Sud\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: Influenza aviaria, la situazione: cos'è, come si trasmette,
quali sono i rischi\n\nSummary: \nThe Italian National Institute of Health (Istituto superiore di sanità) issued a guide on March 25, 2026, following the identification of the first human case of
avian influenza in Europe in Lombardy. According to the One Health Network and experts like virologist Fabrizio Pregliasco, avian influenza is primarily a viral infection in birds, with wild waterfowl
acting as the main transmission vector to farm animals and occasionally humans. While most strains are relatively harmless to humans, some mutations could increase infectivity; however, there is
currently no confirmed evidence of human-to-human transmission. The European Centre for Disease Prevention and Control (ECDC) states the risk to the general population is low, rising to moderate only
for workers in infected farms. Regarding food safety, the European Food Safety Authority (EFSA) notes no evidence that consumption of contaminated meat transmits the virus, though raw milk
contaminated with the H5N1 virus has been recalled in the US. In Italy, over 3,000 cattle tested in areas with bird cases showed negative results. Experts also warn of a low risk to cats and dogs if
they contact infected wild birds, recommending avoidance of such contact and raw meat feeding.\n\nPublished date: March 25 2026, 16:01\n\nURL:
https://laprovinciapavese.gelocal.it/pavia/cronaca/2026/03/25/news/influenza_aviaria_la_situazione_cos_e_come_si_trasmette_quali_sono_i_rischi-15560018/\nSource: La Provincia Pavese\nClassification:
Health\nSentiment: neutral\nReporting voice: Explanatory\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [6]\nTitle: Lombardy man becomes first Italian human bird flu case - Science & Tecnology -
Ansa.it\n\nSummary: \nAccording to epidemiologist Gianni Rezza, a man in Lombardy has become Italy's first confirmed case of human bird flu infection. The patient was infected with the low-
pathogenicity avian influenza A(H9N2) virus, which Rezza described as an 'isolated, imported, non-native case' and 'the first human case of avian influenza ever diagnosed in Italy.' The infection is
not causing alarm because it is caused by a 'much less aggressive strain' than the more well-known H5N1 virus. The case was reported on Wednesday, March 25, 2026, by ANSA.it.\n\nPublished date: March
25 2026, 15:31\n\nURL: https://www.ansa.it/english/news/science_tecnology/2026/03/25/lombardy-man-becomes-first-italian-human-bird-flu-case_eb8d0b46-1108-4f4d-8e8a-3830bb8d64e9.html\nSource:
ANSA.it\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: Aviaria, cos'è il virus H9N2: come si trasmette e i
rischi per l'uomo\n\nSummary: \nThe Italian Superior Health Institute (Iss) has issued a focus document addressing the first human case of avian influenza H9N2 detected in Europe, specifically in
Lombardy. According to the One Health Network, avian influenza is primarily a viral infection in birds, with wild aquatic birds as the main transmission vector, though it can sporadically infect
mammals including cattle and pets like cats. The Iss states that while most avian viruses are relatively harmless to humans, some strains can mutate to infect other species. Currently, human cases are
asymptomatic or mild, and there is no confirmed evidence of human-to-human transmission. According to the European Centre for Disease Prevention and Control (Ecdc), the risk to the general population
is low, rising to moderate only for workers exposed in infected farms. Regarding food safety, the European Food Safety Authority (Efsa) states there is no evidence that avian influenza is transmitted
via consumption of contaminated meat, provided standard hygiene and cooking practices are followed. While raw milk contaminated with H5N1 was recalled in the US, no infected cattle have been found in
Italy; over 3,000 cattle tested in areas with bird cases showed negative results. The Iss advises pet owners to avoid contact with wild birds and raw meat products. Italy's surveillance system
involves veterinary services, the National Reference Centre at the Istituto Zooprofilattico Sperimentale delle Venezie (Izsve), and the RespiVirNet network, which includes 28 laboratories and the
Institute of Biomedical Sciences of Defense (Isbd). This 'One Health' project, funded by the Ministry of Health, involves collaboration between institutions like the Policlinico San Matteo di Pavia
and universities in Parma, Bari, and the Marche, alongside EU bodies including the Ecdc, Efsa, and the European Reference Laboratory (Eurl).\n\nPublished date: March 25 2026, 15:01\n\nURL:
https://www.adnkronos.com/cronaca/aviaria-cose-il-virus-h9n2-come-si-trasmette-e-i-rischi-per-luomo_6A0ZnuGyQ8U55VbfrDLWKc\nImage description: A laboratory setting showing a gloved hand holding a test
tube filled with red blood, with several other test tubes containing red liquid in a metal rack in the background.\nSource: Adnkronos\nClassification: Health\nSentiment: neutral\nReporting voice:
Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: Первый в ЕС случай заражения человека птичьим гриппом H9N2 выявлен в Ломбардии\n\nSummary: \nAccording to Life.ru, the first
case of human infection with the H9N2 avian influenza virus in the European Union was identified in Lombardy, Italy, on March 25, 2026. The patient, who has underlying health conditions, was infected
outside of Europe following contact with infected birds or a contaminated environment. The virus is classified as a low-pathogenicity animal-origin A(H9N2) strain. The patient has been hospitalized
for analysis and contact tracing. Authorities report that no serious health threats have been detected and the situation is under control.\n\nPublished date: March 25 2026, 12:50\n\nURL:
https://life.ru/p/1856047\nSource: Life.ru\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: Aviaria, primo caso
umano di H9N2 in Europa: identificato in Lombardia. Ecco che cosa sapere\n\nSummary: \nOn March 25, 2026, Italian health authorities confirmed the first human case of avian influenza H9N2 in Europe,
identified in Lombardy. According to the Italian Ministry of Health, the patient is a 'fragile person with concomitant diseases' who contracted the low-pathogenicity virus A(H9N2) while abroad in a
non-European country. The patient is currently hospitalized, and the Ministry of Health, in coordination with the Lombardy Region, the Superior Institute of Health (ISS), and international bodies, has
activated surveillance procedures. The Ministry stated that 'all checks provided have been carried out in a timely manner' and that 'contacts of the case have been identified.' Crucially, the article
notes that 'no human-to-human transmission has ever been reported' and that human cases are generally characterized by 'mild disease.' Scientific data from the ISS indicates the virus primarily
affects wild birds, particularly waterfowl, and that transmission to humans occurs via 'direct exposure to infected poultry or contaminated environments.' For the general population, the risk remains
'contained,' with no evidence of interhuman transmission. The Italian control system involves veterinary services, the National Surveillance Plan, and the RespiVirNet network for human monitoring.
Regarding food safety, the article cites evidence that 'there is no proof of transmission through the consumption of contaminated meat,' provided standard hygiene and cooking practices are followed.
The event is described as a 'rare event in the European panorama' and a 'test bench for surveillance systems,' with the situation currently 'under control' and no signs of spread.\n\nPublished date:
March 25 2026, 11:35\n\nURL: https://www.lastampa.it/la-zampa/2026/03/25/news/aviaria_primo_caso_umano_h9n2_lombardia-425244737/\nImage description: A person wearing a white protective hazmat suit
with a clear face shield looking through a glass barrier at a white chicken with a red comb.\nSource: lastampa.it\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent:
Europe\n\n</doc>\n\n<doc>\nCitation key: [10]\nTitle: What to know about bird flu in WA\n\nSummary: \nAccording to the Daily Record News (Ellensburg), a novel Type A H5N1 bird flu outbreak has
affected Washington state, where approximately 2.2 million commercial, backyard, and wild birds have tested positive, including 52 backyard flocks and three commercial ones, as of March 24, 2026.
About 14 Washingtonians, identified as commercial farmworkers, have tested presumptively positive since 2022. While the risk to the general public remains low, Washington state epidemiologist Dr.
Scott Lindquist warns that the virus could mutate to become more infectious to humans, noting, 'We are not seeing that yet — but that's the concern.' The article contextualizes the outbreak by noting
the first human death in the U.S. occurred in Louisiana in January, and the virus has caused millions of animal deaths nationwide over the past three years. Historical context provided by the U.S.
Centers for Disease Control and Prevention (CDC) indicates the disease was first documented in 1878 in northern Italy, with the highly pathogenic strain emerging in China in 1996. Symptoms in birds
include respiratory issues and lethargy, while humans may experience conjunctivitis, fevers, and muscle pain. The CDC recommends testing for those with recent exposure and advises avoiding raw milk or
raw animal products, which pose infection risks. Additionally, Dr. Lindquist states that while seasonal flu vaccines do not prevent bird flu, they may reduce the risk of co-infection and subsequent
mutation.\n\nPublished date: March 24 2026, 16:36\n\nURL: https://www.dailyrecordnews.com/news/what-to-know-about-bird-flu-in-wa/article_265754eb-bb30-49e6-bf5b-3e8130570a7f.html\nSource: Daily Record
News (Ellensburg)\nClassification: Health\nSentiment: negative\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: Cambodia reports 2nd human H5N1
case of year - BNO News\n\nSummary: \nOn Saturday, Cambodia's National Institute of Public Health confirmed a second human case of H5N1 bird flu in 2026, involving a 45-year-old woman from Ropai
Village in Banteay Meanchey Province. The woman, who is hospitalized and under close medical care, reported handling chickens and ducks that had died, with additional reports of dead poultry in her
village. Health officials are collecting samples from close contacts, who are being treated with Tamiflu as a precautionary measure. This follows 19 confirmed human cases in 2025, including eight
fatalities. The previous case this year occurred in Kampot Province involving a man who cooked a dead chicken. While the specific strain of the latest case is unconfirmed, it is likely clade 2.3.2.1c,
endemic to the country, rather than the internationally noted clade 2.3.4.4b.\n\nPublished date: March 16 2026, 20:57\n\nURL: https://bnonews.com/index.php/2026/03/cambodia-reports-2nd-
human-h5n1-case-of-year/\nImage description: A micrograph image showing avian influenza (bird flu) viruses, featuring blue centers with green outer layers against a pinkish background. Credit:
CDC/F.A. Murphy.\nSource: BNO News\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: Avian influenza overview
December 2025-February 2026\n\nSummary: \nBetween 29 November 2025 and 27 February 2026, 2514 highly pathogenic avian influenza (HPAI) A(H5) virus detections were reported in 32 European countries,
including 406 in domestic birds and 2108 in wild birds, according to the European Food Safety Authority. Although weekly detections have been declining since the peak, waterfowl were affected more
than in previous years, and over 90% of poultry cases resulted from primary introduction from wild birds. A large number of backyard farms and several zoos were impacted. High viral circulation in
wild birds led to a slight increase in mammal detections in Europe, with the first potential spillover event to dairy cattle suggested in the Netherlands. In humans, 10 cases were reported across two
countries: one A(H5N1) case in Cambodia and nine cases (eight A(H9N2) and one A(H10N3)) in China, all of which were non-fatal. Most human cases involved exposure to poultry or poultry environments.
The risk of human-to-human transmission remains undocumented, and the risk to the general public in the European Union/European Economic Area is considered low, though low-to-moderate for those
occupationally exposed to infected animals or contaminated environments.\n\nPublished date: March 12 2026, 14:15\n\nURL: https://www.efsa.europa.eu/en/efsajournal/pub/10015\nSource: European Food
Safety Authority\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [13]\nTitle: Caso de influenza aviar en aves silvestres
por ahora no implica cierre de mercados en Chile, según SAG\n\nSummary: \nAccording to the Servicio Agrícola y Ganadero (SAG), Chilean authorities confirmed the presence of highly pathogenic avian
influenza H5N1 in wild birds at the El Yali Wetland in Santo Domingo, Valparaíso Region, on Wednesday, March 4, 2026, following a report of coscoroba swan deaths. The SAG stated that while the virus
is highly contagious and has no cure, the confirmation of cases in wild birds 'does not imply the closure of markets' in Chile, maintaining the country's status as free of highly pathogenic avian
influenza in commercial poultry since August 2023. In response, the National Health Emergency System was activated, and coordination began with public agencies including Sernapesca, Senapred, and the
Ministry of Health, alongside the private sector. A Regional Technical Meeting is scheduled for Thursday to evaluate the situation. The SAG noted that the previous outbreak in August 2023 impacted
over 100,000 wild birds across 52 species, 175 backyard farms, and 12 commercial establishments, resulting in the temporary closure of 78 export markets (now reopened), infections in marine mammals,
and one confirmed human case.\n\nPublished date: March 05 2026, 10:21\n\nURL: https://www.biobiochile.cl/noticias/nacional/region-de-valparaiso/2026/03/05/caso-de-influenza-aviar-en-aves-silvestres-
por-ahora-no-implica-cierre-de-mercados-en-chile-segun-sag.shtml\nSource: BioBioChile\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: South
America\n\n</doc>\n\n<doc>\nCitation key: [14]\nTitle: 鳥インフルエンザが乳牛に感染した原因は何か？米国で広がる酪農経済への打撃、私たちはどう対応すべきか\n\nSummary: \nIn early 2024, the US confirmed the first known infection of high-pathogenicity
avian influenza (H5N1) in dairy cows, a development that defies the historical understanding that the virus primarily affects poultry and wild birds. According to the article, this event marks a
significant shift, as H5N1 was previously known to be fatal mainly to birds. While no cases have been confirmed in Japan as of the report, the article notes the potential impact on the dairy economy
and the need for future countermeasures. The virus naturally circulates in migratory birds like ducks and plovers, which act as reservoirs without severe symptoms. The article explains that influenza
viruses mutate rapidly, particularly through 'genetic reassortment' when different strains infect the same host, potentially creating new variants. This mechanism historically allowed bird viruses to
cross species barriers to humans, a process facilitated by the close contact between humans and livestock. The article highlights that regions in southern China, such as Yunnan and Guangdong
provinces, remain high-risk areas due to traditional practices where birds, pigs, and humans live in close proximity; pigs act as 'mixing vessels' possessing receptors for both bird and human viruses,
facilitating the evolution of pandemic strains. Historical precedents cited include the 1918 Spanish flu, the 1957 Asian flu, and the 1968 Hong Kong flu, all of which originated from avian influenza
viruses. The article was published on March 04, 2026, by WEDGE Infinity.\n\nPublished date: March 04 2026, 20:00\n\nURL: https://wedge.ismedia.jp/articles/-/40299\nSource: WEDGE
Infinity(ウェッジ)\nClassification: Health\nSentiment: neutral\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Bird flu continues to expand in
Wisconsin\n\nSummary: \nThe Wisconsin Department of Agriculture, Trade and Consumer Protection (DATCP) confirmed a highly pathogenic avian influenza (H5N1 HPAI) outbreak in a backyard poultry flock in
Dane County on March 3, 2026. The outbreak involves 55 birds, all of which will be depopulated to prevent disease spread. This is the second case in the state within a week, following a much larger
incident in Jefferson County on Friday where over 1 million chickens were culled. DATCP and U.S. Department of Agriculture officials are conducting a joint incident response, having quarantined the
affected premises in Dane County. The department noted that the H5N1 virus has circulated in North America since December 2021. Historical data cited by the department indicates that bird flu caused
the culling of over 3 million birds in Jefferson County last year, and in 2024, four cases in Wisconsin resulted in the culling of over 54,000 birds. The affected birds from the current Dane County
flock will not enter the food system.\n\nPublished date: March 03 2026, 21:30\n\nURL: https://www.thecentersquare.com/wisconsin/article_46a0f22d-2fdf-43c4-9738-0b9754b705f0.html\nSource: The Center
Square: Wisconsin\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [16]\nTitle: Los virus que serán protagonistas
este 2026, según un médico e investigador de enfermedades infecciosas - La Tercera\n\nSummary: \nAccording to Patrick Jackson, a physician and infectious disease researcher at the University of
Virginia, published in an analysis in The Conversation, evolving viruses pose significant threats in 2026 due to a warmer, more populated planet and rapid global mobility. Jackson warns of the
potential for infections 'in unexpected places or in unexpected quantities.'\n\nFirst, the influenza A virus, specifically the H5N1 subtype, remains a constant threat. The 2009 H1N1 pandemic caused
over 280,000 deaths in its first year, and the virus continues to circulate. H5N1, first detected in humans in southern China in 1997, spread globally via wild birds. In 2024, it was identified in
dairy cattle in the United States, establishing itself in herds across several states and raising alarms over the jump from birds to mammals. Jackson notes that numerous transmissions from cows to
humans have already been documented. The critical question for 2026 is whether H5N1 will acquire the ability to transmit effectively between people, a key step for a new pandemic. Current flu vaccines
likely will not protect against this subtype, though specific formulations are being developed.\n\nSecond, the mpox virus, formerly known as monkeypox, was identified in the 1950s and historically
occurred sporadically in sub-Saharan Africa. It causes fever and a painful rash lasting weeks. The virus has two major genetic variants: clade I, which usually causes more severe illness, and clade
II, which tends to cause milder symptoms. In 2022, a global outbreak of clade II spread to over 100 countries, driven by close contact, often sexual. Although cases have decreased, clade II has
established itself in various regions. Additionally, since 2024, several Central African countries have reported an increase in clade I, and cases were notified in the United States in 2025 without
travel history to Africa. The evolution of these outbreaks remains uncertain for 2026.\n\nThird, the less-known Oropouche virus was identified in the 1950s in Trinidad and is transmitted by mosquitoes
and midges. While some patients experience prolonged weakness and even relapses, it was historically thought to be limited to the Amazon region. However, given that the insect vector is present in
much of the American continent, Jackson warns that the virus's reach could continue to expand in 2026. In the United States, infections are typically detected in travelers.\n\nThis analysis was
published by La Tercera on March 02, 2026.\n\nPublished date: March 02 2026, 09:01\n\nURL: https://www.latercera.com/tendencias/noticia/los-virus-que-seran-protagonistas-este-2026-segun-un-medico-e-
investigador-de-enfermedades-infecciosas/\nSource: LA TERCERA\nClassification: Health\nSentiment: neutral\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key:
[17]\nTitle: Alerta por gripe aviaria: advierten sobre los síntomas que indican un contagio en personas y piden concurrir al médico\n\nSummary: \nFollowing a series of confirmed Avian Influenza H5
cases in wild and domestic birds in the Buenos Aires province (specifically General Madariaga, Rancho, and Lobos) and Buenos Aires city (Reserva Ecológica Costanera Sur), health authorities including
the Servicio Nacional de Sanidad y Calidad Agroalimentaria (Senasa) and the National Ministry of Health have issued an alert. The virus, identified in brown-hooded gulls, coscoroba swans, and black-
necked swans, poses a risk to humans who have had contact with infected animals or contaminated environments. Authorities urge individuals exposed to sick or dead birds, their excretions, or outbreak
areas within the last ten days to seek medical attention immediately if they develop symptoms such as cough, sore throat, respiratory difficulty, or conjunctivitis, noting that fever is not always
present. Protocols established by the Buenos Aires government and Senasa require immediate notification to the Pasteur Institute upon finding dead birds, with a 20-meter exclusion zone and no public
access. While the H5N1 virus primarily affects birds and sustained human-to-human transmission is not occurring in typical environmental settings, the National Ministry of Health has activated
epidemiological surveillance for unusual respiratory events and severe influenza-like illnesses. As of March 1, 2026, no human cases have been confirmed in the jurisdiction; a suspected case
investigated by LA NACION tested negative for avian flu. Historical data from the previous year indicates that out of 51 people under surveillance following exposure to backyard and farm birds, two
contracted the infection.\n\nPublished date: March 01 2026, 23:57\n\nURL: https://www.lanacion.com.ar/sociedad/alerta-por-gripe-aviaria-advierten-sobre-los-sintomas-que-indican-un-contagio-en-
personas-y-piden-nid01032026/\nSource: La Nacion\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: South America\n\n</doc>\n\n<doc>\nCitation key: [18]\nTitle: Bird
Flu Is Back. Here's What You Need To Know.\n\nSummary: \nGovernor Josh Shapiro of Pennsylvania convened a crisis response meeting amid a significant avian influenza outbreak, with nearly 7.6 million
birds infected in the state. The virus, primarily transmitted through bird mucous, saliva, or feces, is not commonly spread person-to-person but can transfer from birds, cows, and other animals to
humans without proper protective equipment. Symptoms include fever, sore throat, cough, nausea, vomiting, and conjunctivitis; severe cases may lead to respiratory failure, especially in
immunocompromised individuals. In Pennsylvania, farmers are culling large flocks to contain the spread, and the state is collaborating with the U.S. Department of Agriculture and 24 avian flu
specialists. Regulatory relief is being sought to expand the number of veterinarians able to diagnose and manage outbreaks, and efforts are underway to advance a potential avian flu vaccine. In
California, the H5N1 strain has killed nearly 30 elephant seals, raising concerns as a related strain caused 17,000 animal deaths in Argentina in 2023. Experts caution the public not to touch or
interact with dead seals or livestock. In the United Kingdom, nearly 30 swans died in London’s Docklands due to an avian flu outbreak, with scientists warning the strain may be particularly lethal.
Authorities have urged tourists and residents to avoid interacting with birds, feeding water animals, or approaching dead animal remains. Although outbreaks appear geographically dispersed and may
involve different viral strains, they collectively signal a growing public health concern. According to the NHS, individuals with exposure or symptoms should immediately consult a trained medical
professional.\n\nPublished date: February 26 2026, 04:00\n\nURL: https://www.forbes.com/sites/saibala/2026/02/25/bird-flu-is-back-heres-what-you-need-to-know/\nSource: Forbes\nClassification:
Health\nSentiment: negative\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [19]\nTitle: H5N1 bird flu found in elephant seals at Año Nuevo State
Park\n\nSummary: \nThe H5N1 bird flu virus has been confirmed in seven weaned northern elephant seal pups at Año Nuevo State Park in California, according to researchers from UC Davis and UC Santa
Cruz. The detection was confirmed by the U.S. Department of Agriculture’s laboratory in Ames, Iowa. This marks the first known case of H5N1 in northern Pacific elephant seals, despite prior concerns
due to the virus's devastating impact on southern elephant seal populations in South America and sub-Antarctic islands, where up to 97% of pups died in some Argentine colonies and breeding females
declined by 47% on South Georgia Island between 2022 and 2024. More than 30,000 sea lions died in Peru and Chile during the same period, and approximately 1,300 sea lions and fur seals perished in
Argentina. While the exact death toll in California has not been disclosed, UC Davis professor Christine Johnson described the detection as 'exceptionally rapid' due to coordinated, high-alert
surveillance. The virus, previously known for infecting dairy cows, wild birds, and poultry across the U.S., has caused 71 human infections and two deaths since 2024, primarily among dairy and poultry
workers. Roxanne Beltran of UC Santa Cruz emphasized the importance of increased monitoring, noting that her lab leads the northern elephant seal research program at Año Nuevo. The outbreak
underscores the virus’s expanding reach into marine mammals despite earlier hopes that prior exposure might have conferred immunity in northern populations.\n\nPublished date: February 25 2026,
14:00\n\nURL: https://www.mercurynews.com/2026/02/25/h5n1-bird-flu-found-in-california-elephant-seals-for-the-first-time/\nSource: San Jose Mercury News\nClassification: Health\nSentiment:
negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [20]\nTitle: Uruguay declaró emergencia sanitaria por gripe aviar tras detectar el virus H5 en la fauna
silvestre\n\nSummary: \nUruguay declared a national sanitary emergency on February 24, 2026, due to the detection of the highly pathogenic H5 avian influenza virus in wild bird populations across
three departments: Maldonado, Rocha, and Canelones. The Ministry of Livestock, Agriculture, and Fisheries (MGAP) confirmed the first case on February 20, involving a coscoroba swan (Coscoroba
coscoroba) found dead in the Laguna Garzón area. Since then, at least two additional dead swans and a dozen infected birds have been confirmed. The emergency measures, which took immediate effect,
include suspending the movement of backyard and unmonitored birds, closing fairs and auctions, and restricting bird transport. Commercial poultry production systems remain authorized to circulate.
Non-compliance may result in penalties, though specific details were not publicly disclosed. Avian influenza, caused by type A influenza viruses, primarily affects birds—both wild and domestic—and
some strains like H5N1 can rarely infect humans, causing symptoms such as fever, cough, and respiratory difficulty. Transmission occurs through contact with infected birds, their secretions, or
contaminated surfaces. Prevention relies on biosecurity, surveillance, and avoiding contact with sick or dead birds.\n\nPublished date: February 24 2026, 23:52\n\nURL:
https://radiomitre.cienradios.com/mundo/uruguay-declaro-emergencia-sanitaria-por-gripe-aviar-tras-detectar-el-virus-h5-en-la-fauna-silvestre/\nSource: Radio Mitre ✋🏽🧼🤚🏽\nClassification:
Health\nSentiment: neutral\nReporting voice: Objective\nContinent: South America\n\n</doc>\n\n------News Summaries End------\n","offset":10,"hit_cache":false}
```

## 💬 Response

Good, I now have the CDC count at 71 cases since February 2024. Let me search specifically for recent US H5N1 human cases and the rate of new cases.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "CDC H5N1 human cases United States 2026 new confirmed"
}
```

### 📋 Result

```
{"query": "CDC H5N1 human cases United States 2026 new confirmed", "results": [{"title": "A(H5) Bird Flu: Current Situation | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/situation-
summary/index.html", "snippet": "What to know\n- A(H5) bird flu is widespread in wild birds worldwide and is causing outbreaks in poultry and U.S. dairy cows with sporadic human cases in U.S. dairy
and poultry workers.\n- While the current public health risk is low, CDC is watching the situation carefully and working with states to monitor people with animal exposures.\n- CDC is using its flu
surveillance systems to monitor for A(H5) bird flu activity in people.\n![H5N1 Bird Flu How is it Spreading?](/bird-flu/media/images/2024/07/", "api_data": null, "hint": null}, {"title": "Global Human
Cases with Influenza A(H5N1), 1997-2026 | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html", "snippet": "What to know\nThis graph shows all human
infections with HPAI A(H5N1) bird flu virus reported to the World Health Organization (WHO), since the first human cases in 1997.\nBackground\nThis graph shows all human infections with HPAI A(H5N1)
bird flu virus reported to the [World Health Organization](https://www.who.int/teams/global-influenza-programme/avian-influenza) (WHO), since the first human cases in 1997.\nA(H5N1) bird flu viruses
first emerged in southern China in 1996. Those viruses caused lar", "api_data": null, "hint": null}, {"title": "Avian Influenza A(H5) Outbreak | Center for Outbreak Response Innovation", "url":
"https://cori.centerforhealthsecurity.org/resources/avian-influenza-ah5-outbreak", "snippet": "Question: I heard that there are house cats dying of H5N1. Should I be concerned?\nAnswer: Bird flu
infection among cats still appears rare, but infections have been fatal. In late 2024,\n[bird flu killed 20 big cats at an animal sanctuary](https://www.npr.org/2024/12/26/nx-s1-5239841/bird-flu-
kills-20-cats-washington-sanctuary)\nin Shelton, Washington, and at least three house cats have died after\n[drinking raw milk](https://www.latimes.com/environment/story/2025-01-03/the-owner-of-two-
cats-who-di", "api_data": null, "hint": null}, {"title": "H5N1 strikes more poultry in 4 states; CDC updates details on recent human cases | CIDRAP", "url": "https://www.cidrap.umn.edu/avian-
influenza-bird-flu/h5n1-strikes-more-poultry-4-states-cdc-updates-details-recent-human-cases", "snippet": "In new H5N1 avian flu confirmations today, the US Department of Agriculture (USDA) Animal and
Plant Health Inspection Service (APHIS) reported that the virus hit more [flocks](https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-influenza/hpai-detections/commercial-backyard-flocks)
in four states, including another massive layer farm in Ohio, the nation\u2019s second biggest poultry producer.\n![egg shortage](/sites/default/files/egg%20shortage.jpg)\nOver the past several weeks,
Ohio has be", "api_data": null, "hint": null}, {"title": "Updated H5N1 Report: 70 Human Cases in the US as of April 2025 | Contagion Live", "url":
"https://www.contagionlive.com/view/updated-h5n1-report-70-human-cases-in-the-us-as-of-april-2025", "snippet": null, "api_data": null, "hint": null}, {"title": "Current Situation: H5N1 Bird Flu in
People | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/situation-summary/inhumans.html", "snippet": "Highlights\n- Sporadic avian influenza A(H5N1) virus infections (\"H5N1 Bird Flu\") in
people have been reported worldwide since 1997.\n- Highly pathogenic avian influenza A(H5N1) viruses are widespread in wild birds worldwide, have caused poultry outbreaks in many countries, and
infected other kinds of animals. H5N1 bird flu has caused outbreaks in U.S. poultry and dairy cows.\n- In the United States, sporadic human infections with A(H5N1) viruses have occurred since 2022
mostly after direct or clos", "api_data": null, "hint": null}, {"title": "Human infections with highly pathogenic avian influenza A(H5N1) viruses in the United States from March 2024 to May 2025 -
PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12477757/", "snippet": "Abstract\nBetween March 2024 and October 2024, 46 human cases of highly pathogenic avian influenza (HPAI) A(H5N1) had
been detected in the United States. The persistent panzootic spread of HPAI A(H5N1) viruses and continued detection of human cases presents an ongoing threat to public health. Between November 2024
and May 2025, an additional 24 cases have been reported for a total of 70 human cases of HPAI A(H5N1): 41 were exposed to dairy cows, 24 to commercial poultry, 2 to backyard poultry, an", "api_data":
null, "hint": null}, {"title": "H5N1 influenza: monthly reported cases - Our World in Data", "url": "https://ourworldindata.org/grapher/h5n1-flu-reported-cases", "snippet": "H5N1 influenza: monthly
reported cases\n![](/grapher/h5n1-flu-reported-cases.png)\nAbout this data\n[with minor processing](https://ourworldindata.org#sources-and-processing)by Our World in Data\nSources and processing\nThis
data is based on the following sources\nHow we process data at Our World in Data\nAll data and visualizations on Our World in Data rely on data sourced from one or several original data providers.
Preparing this original data involves several processing steps. Depending on the data", "api_data": null, "hint": null}, {"title": "Human H5N1 Cases - Avian Influenza - MSK Library Guides at Memorial
Sloan Kettering Cancer Center", "url": "https://libguides.mskcc.org/BirdFlu/H5N1/Humans", "snippet": "| Exposure Associated with Commercial Agriculture & Related Operations | |||||\n| State | Dairy
Herds (Cattle) | Poultry Farms & Culling Operations | Other Animal Exposure | Exposure Source Unknown | State Total |\n| California | 36 | 0 | 0 | 2 | 38 |\n| Colorado | 1 | 9 | 0 | 0 | 10 |\n| Iowa |
0 | 1 | 0 | 0 | 1 |\n| Louisiana | 0 | 0 | 1 | 0 | 1 |\n| Michigan | 2 | 0 | 0 | 0 | 2 |\n| Missouri | 0 | 0 | 0 | 1 | 1 |\n| Nevada | 1 | 0 | 0 | 0 | 1 |\n| Ohio | 0 | 1 | 0 | 0 | 1 |\n| Oregon | 0 |
1 | 0 | 0 | ", "api_data": null, "hint": null}, {"title": "Weekly US Influenza Surveillance Report: Key Updates for Week 50, ending December 13, 2025 | FluView | CDC", "url":
"https://www.cdc.gov/fluview/surveillance/2025-week-50.html", "snippet": "Key points\n- Note: Due to the Christmas Holiday, FluView for Week 51 will be posted on December 30, 2025.\n- Seasonal
influenza activity continues to increase across the country.\nSummary\nViruses\nIllness\nAll data are preliminary and may change as more reports are received.\nDirectional arrows indicate changes
between the current week and the previous week. [Additional information](https://www.cdc.gov/fluview/surveillance/2025-week-50.html#cdc_data_surveillance_section_5-additional-national-and-inte",
"api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html",
  "prompt": "What is the total number of confirmed US human H5N1 cases? When was the most recent case? What is the timeline of cases in 2025 and 2026?"
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html", "content": "Based on the provided content, **I cannot determine the total number of confirmed US human H5N1 cases,
the date of the most recent case, or the specific timeline of cases in 2025 and 2026.**\n\nThe content mentions that \"several recent A(H5) cases have been reported in the U.S.\" but does not
provide:\n- An exact number of US cases\n- Dates of individual cases\n- A breakdown by year (2025/2026)\n\nThe text notes that the data \"will be updated biweekly on Fridays\" and references a graph
showing cases, but the actual numerical data and timeline details are not included in the text excerpt provided.\n\n**Relevant links:**\n- [H5 Bird Flu: Current Situation | Bird Flu |
CDC](https://www.cdc.gov/bird-flu/situation-summary/index.html) - This link is specifically mentioned as containing \"more data on H5 cases in the United States\"\n- [World Health Organization -
Global Influenza Programme](https://www.who.int/teams/global-influenza-programme/avian-influenza) - For global A(H5N1) case reporting", "title": "Global Human Cases with Influenza A(H5N1), 1997-2026"}
```

```json
{
  "query": "H5N1 bird flu human case confirmed United States 2026",
  "n_articles": 10,
  "hours_back": 1440,
  "countries": [
    "US"
  ],
  "string_guarantee": [
    "H5N1",
    "human"
  ]
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: What to know about bird flu in WA\n\nSummary: \nAccording to the Daily Record News (Ellensburg), a
novel Type A H5N1 bird flu outbreak has affected Washington state, where approximately 2.2 million commercial, backyard, and wild birds have tested positive, including 52 backyard flocks and three
commercial ones, as of March 24, 2026. About 14 Washingtonians, identified as commercial farmworkers, have tested presumptively positive since 2022. While the risk to the general public remains low,
Washington state epidemiologist Dr. Scott Lindquist warns that the virus could mutate to become more infectious to humans, noting, 'We are not seeing that yet — but that's the concern.' The article
contextualizes the outbreak by noting the first human death in the U.S. occurred in Louisiana in January, and the virus has caused millions of animal deaths nationwide over the past three years.
Historical context provided by the U.S. Centers for Disease Control and Prevention (CDC) indicates the disease was first documented in 1878 in northern Italy, with the highly pathogenic strain
emerging in China in 1996. Symptoms in birds include respiratory issues and lethargy, while humans may experience conjunctivitis, fevers, and muscle pain. The CDC recommends testing for those with
recent exposure and advises avoiding raw milk or raw animal products, which pose infection risks. Additionally, Dr. Lindquist states that while seasonal flu vaccines do not prevent bird flu, they may
reduce the risk of co-infection and subsequent mutation.\n\nPublished date: March 24 2026, 16:36\n\nURL: https://www.dailyrecordnews.com/news/what-to-know-about-bird-flu-in-wa/article_265754eb-
bb30-49e6-bf5b-3e8130570a7f.html\nSource: Daily Record News (Ellensburg)\nClassification: Health\nSentiment: negative\nReporting voice: Explanatory\nContinent: North
America\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: First cases of deadly avian flu detected among California elephant seals\n\nSummary: \nMultiple northern elephant seal pups along the Northern
California coast have tested positive for the highly pathogenic avian influenza (HPAI) H5N1 subtype, marking the first confirmed outbreak of bird flu in marine mammals in California and the first
detection in northern elephant seals, according to research from the University of California. Scientists from UC Davis and UC Santa Cruz collected samples from seven dead weanling pups at Año Nuevo
State Park in San Mateo County and observed live pups exhibiting tremors and seizure activity. Testing at the California Animal Health & Food Safety lab confirmed the presence of H5N1, with final
confirmation by the U.S. Department of Agriculture’s National Veterinary Services Laboratory. Professor Christine Johnson of UC Davis described the detection as 'exceptionally rapid' due to
coordinated surveillance efforts. This outbreak is significant as H5N1 has previously caused mass die-offs in southern elephant seals in Argentina in 2023 and has spread to wild birds, poultry, and
other mammals across North America, including outbreaks in Washington, Maine, and Florida. As of February 2026, the U.S. Centers for Disease Control and Prevention reported 71 human cases of bird flu
in North America, with 38 in California—nearly all linked to direct contact with infected livestock or poultry—and two fatalities. Health officials emphasize the low risk to the public but advise
against touching live or dead seals and urge reporting of sick, injured, or dead marine mammals to the NOAA Fisheries West Coast Region stranding hotline at (866) 767-6114. Researchers are
collaborating with NOAA, the California Department of Fish and Wildlife, and the West Coast Marine Mammal Stranding Network to monitor coastal marine mammals.\n\nPublished date: February 25 2026,
23:53\n\nURL: https://www.cbsnews.com/sanfrancisco/news/avian-flu-elephant-seals-california-ano-nuevo-state-park-uc-davis/\nSource: CBS News\nClassification: Health\nSentiment: negative\nReporting
voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle: H5N1 bird flu found in elephant seals at Año Nuevo State Park\n\nSummary: \nThe H5N1 bird flu virus has been
confirmed in seven weaned northern elephant seal pups at Año Nuevo State Park in California, according to researchers from UC Davis and UC Santa Cruz. The detection was confirmed by the U.S.
Department of Agriculture’s laboratory in Ames, Iowa. This marks the first known case of H5N1 in northern Pacific elephant seals, despite prior concerns due to the virus's devastating impact on
southern elephant seal populations in South America and sub-Antarctic islands, where up to 97% of pups died in some Argentine colonies and breeding females declined by 47% on South Georgia Island
between 2022 and 2024. More than 30,000 sea lions died in Peru and Chile during the same period, and approximately 1,300 sea lions and fur seals perished in Argentina. While the exact death toll in
California has not been disclosed, UC Davis professor Christine Johnson described the detection as 'exceptionally rapid' due to coordinated, high-alert surveillance. The virus, previously known for
infecting dairy cows, wild birds, and poultry across the U.S., has caused 71 human infections and two deaths since 2024, primarily among dairy and poultry workers. Roxanne Beltran of UC Santa Cruz
emphasized the importance of increased monitoring, noting that her lab leads the northern elephant seal research program at Año Nuevo. The outbreak underscores the virus’s expanding reach into marine
mammals despite earlier hopes that prior exposure might have conferred immunity in northern populations.\n\nPublished date: February 25 2026, 14:00\n\nURL:
https://www.mercurynews.com/2026/02/25/h5n1-bird-flu-found-in-california-elephant-seals-for-the-first-time/\nSource: San Jose Mercury News\nClassification: Health\nSentiment: negative\nReporting
voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: Are there dead geese in your neighborhood? Where mass casualties have been be reported in N.J. and what to
do.\n\nSummary: \nThe New Jersey Department of Environmental Protection's Division of Fish and Wildlife is investigating a widespread outbreak of the H5N1 strain of bird flu, which has caused over
1,100 reported cases of sick or dead wild birds—primarily Canada geese—across the state. The Centers for Disease Control and Prevention (CDC) confirms the H5N1 strain is widespread in wild birds
globally and has led to outbreaks in poultry, U.S. dairy cows, and 71 human cases (with two deaths) since February 2024, most linked to direct contact with infected animals. Although the risk to
humans remains low, health officials warn against handling dead or sick birds. Dr. David J. Cennimo of Rutgers New Jersey Medical School emphasizes that transmission occurs primarily through direct
contact, not airborne exposure. Symptoms in humans include eye redness, fever, cough, sore throat, body aches, and fatigue. Residents are urged to report sick or dead birds via a state reporting form
or hotline (877-927-6337). In response, several county park systems—including Pitman, Monmouth County, and Somerset County—have issued warnings or closed parks and trails due to avian deaths. Due to
the scale of the outbreak, state officials cannot assist with all carcass removals. Hainesport Township advises homeowners to use protective gear and safely remove dead birds on their property, though
private wildlife control or municipal animal control services are available alternatives. As of February 20, 2026, no human cases of bird flu have been reported in New Jersey.\n\nPublished date:
February 20 2026, 12:00\n\nURL: https://www.nj.com/healthfit/2026/02/are-there-dead-geese-in-your-neighborhood-where-mass-casualties-have-been-be-reported-in-nj-and-what-to-do.html\nSource:
NJ.com\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: 1,100 Dead Or Sick Wild Birds Reported Across NJ
Over 3 Days\n\nSummary: \nOver a three-day period in February 2026, officials in New Jersey reported 1,100 dead or sick wild birds across the state, with a resurgence of avian influenza cases observed
since November. The Highly Pathogenic Avian Influenza (H5N1) virus, which has been active since January 2022, continues to impact both wild and domestic birds nationwide. The New Jersey Department of
Environmental Protection (NJDEP) tested brant birds earlier in the month, which returned negative for avian influenza, suggesting the mortality may have been caused by freezing temperatures and food
scarcity. Officials note that wild birds—including waterfowl, raptors, and scavenger birds—are natural reservoirs for avian influenza. Testing for the virus is limited to cases where it has not been
detected in the county or under special circumstances, such as mortality events near poultry facilities. The CDC reports that H5N1 has caused two human deaths in the U.S. since 2024, with outbreaks
also documented in poultry and dairy cows, though the current risk to humans remains low.\n\nPublished date: February 18 2026, 14:35\n\nURL: https://patch.com/new-jersey/baskingridge/1-100-dead-or-
sick-wild-birds-reported-across-nj-over-3-days\nSource: Patch\nClassification: Health\nSentiment: negative\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key:
[6]\nTitle: Deadly H5N1 Bird Flu Confirmed in Antarctica After Mass Skua Die Off\n\nSummary: \nThe highly pathogenic avian influenza virus H5N1 has caused the first confirmed wildlife die-off in
Antarctica, killing over 50 skuas during the 2023 and 2024 austral summers. Researchers from Erasmus MC in the Netherlands and the University of California, Davis, led the study, published in
Scientific Reports on January 14, 2026, which confirmed that H5N1 was the cause of death in nearly all dead skuas found at Beak Island. The virus was detected at three locations: Hope Bay, Devil
Island, and Beak Island, with Beak Island experiencing a major die-off of south polar skuas. Skuas, large seabirds that scavenge and act as ecosystem predators, may have been exposed through infected
carcasses. The study distinguishes this event from earlier detections in January and February 2024, when H5N1 was found in a kelp gull and two skuas, but not confirmed as the cause of death. The virus
causes neurological symptoms such as twisted necks, circling, and falling from the air. Researchers emphasize that human activity contributed to the virus’s emergence and that stronger surveillance is
needed in Antarctica, where reliable population data are scarce—last skua census was in the 1980s, counting about 800 breeding pairs. H5N1, first identified in 1996 in Southeast China, has since
spread globally, affecting over 400 million poultry, dairy cows, mink, foxes, bears, otters, and other mammals and birds. It has also caused approximately 1,000 human cases, with about half being
fatal. The virus is now established in wild bird populations across all continents except Oceania. The study’s authors, including Thijs Kuiken and Ralph Vanstreels, warn that without monitoring, the
spread could go undetected. The HPAI Australis Expedition was funded by IAATO and Ocean Expeditions, with additional support from the European Union, CSIC, and PTI Global Health.\n\nPublished date:
February 14 2026, 21:38\n\nURL: https://scitechdaily.com/\nSource: SciTechDaily\nClassification: Health\nSentiment: negative\nReporting voice: Explanatory\nContinent: South
America\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: A Nasal Vaccine May Stop Bird Flu Before It Becomes the Next Pandemic\n\nSummary: \nA novel intranasal vaccine developed by researchers at
Washington University School of Medicine in St. Louis shows promise in protecting against highly pathogenic H5N1 avian influenza, commonly known as bird flu. Since its first detection in the U.S. in
2014, H5N1 has evolved from a virus primarily affecting wild birds to infecting poultry, dairy cattle, and over 70 humans in the U.S. since 2022, including two deaths. Although sustained human-to-
human transmission has not yet occurred, the virus's continued circulation in animal populations raises concerns about its potential to adapt and trigger a pandemic. The vaccine, tested in a study
published in Cell Reports Medicine, aims to provide stronger mucosal immunity by targeting the virus at the site of entry—through the nose—potentially outperforming traditional flu shots. The research
represents a significant advancement in pandemic preparedness efforts.\n\nPublished date: February 05 2026, 16:14\n\nURL: https://medium.com/technicity/a-nasal-vaccine-may-stop-bird-flu-before-it-
becomes-the-next-pandemic-ef9e6344c99d\nSource: Medium.com\nClassification: Health\nSentiment: positive\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key:
[8]\nTitle: Why scientists are so excited about a nasal spray vaccine for bird flu\n\nSummary: \nA new nasal spray vaccine for H5N1 bird flu has shown promising early results in rodent trials
conducted by scientists at Washington University School of Medicine in Missouri. The vaccine, administered via nasal spray, generated a 'strong immune response' and provided 'near complete protection'
against multiple H5N1 strains, outperforming the same vaccine delivered by injection. Unlike traditional injectable flu vaccines—which prevent severe illness but do not fully stop transmission—nasal
vaccines target the upper airway, where the flu virus first infects and replicates, thereby blocking both infection and onward spread. Dr. Michael Diamond, Professor of Molecular Microbiology at
Washington University and co-author of the study, emphasized that delivering vaccines directly to the upper airway could disrupt the transmission cycle, which is critical for controlling H5N1. The
virus continues to spread globally, causing over nine million bird deaths in the US, Canada, and Europe since October, and has become endemic in US dairy cattle and recently detected in Dutch cows.
Since 2024, at least 70 people in the US have been infected, mostly through contact with sick animals, one of whom died. With a historical case fatality rate of nearly 50% among the nearly 900 human
cases since the late 1990s, and growing concerns that H5N1 could mutate to spread between humans—something the WHO calls an 'enormous concern'—the development of a broadly effective vaccine is urgent.
Current stockpiled H5N1 vaccines, based on older strains from the mid-2000s, are poorly matched to newer, rapidly evolving strains, with effectiveness estimates as low as 45%. Nasal vaccines, by
inducing mucosal immunity in the nose and airways, respond to shared viral features across strains, reducing the need for frequent updates. The findings were published in Cell Reports, a peer-reviewed
scientific journal. However, the vaccine remains in early development and will require extensive human testing and multi-phase clinical trials—potentially taking years—before it can be
deployed.\n\nPublished date: February 02 2026, 17:12\n\nURL: https://www.yahoo.com/news/articles/why-scientists-excited-nasal-spray-171213781.html\nSource: Yahoo\nClassification: Health\nSentiment:
positive\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: Disaster declaration issued for bird flu outbreak in Weld County\n\nSummary: \nA disaster
declaration was issued in Weld County, Colorado, following a presumptive positive case of highly pathogenic avian influenza (HPAI) at a commercial egg farm. Lt. Governor Dianne Primavera (D) verbally
declared the disaster on Thursday evening, with Governor Polis (D) absent in Washington D.C. The Colorado Department of Public Health and Environment (CDPHE) confirmed the case and is awaiting final
confirmation from the U.S. Department of Agriculture in Iowa. The declaration enables state agencies to coordinate mitigation, response, consequence management, and recovery efforts. As of now, there
are no suspected or confirmed human cases of avian influenza, but CDPHE is working with the Colorado Department of Agriculture and the Weld County Health Department to ensure farm workers wear
personal protective equipment and are screened daily for symptoms. The last human cases in Colorado occurred in 2024, involving at least ten people: one dairy farm worker infected with the H5N1 strain
after contact with infected cows, and nine poultry farm workers from two Weld County farms, including those involved in culling infected birds.\n\nPublished date: January 31 2026, 05:52\n\nURL:
https://www.9news.com/article/news/health/disaster-declaration-bird-flu-weld-county/73-01860cf0-434b-4ed1-8032-9b08d1c2c3e0\nSource: 9NEWS\nClassification: Health\nSentiment: negative\nReporting
voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [10]\nTitle: Nasal Vaccine Combats Bird Flu Infection in Rodents\n\nSummary: \nResearchers at Washington University School
of Medicine in St. Louis developed an intranasal adenovirus-vectored vaccine against the H5N1 avian influenza virus, which has caused over 70 human cases and two fatalities in the U.S. since 2022 and
continues to circulate in animals, posing a pandemic risk. The vaccine, tested in hamsters and mice, elicited strong immune responses and provided near-complete protection against infection, even when
administered as a low dose or in animals with prior flu immunity. Unlike traditional intramuscular vaccines, the nasal delivery targets the upper respiratory tract, offering better protection against
initial infection and potentially reducing transmission. The vaccine uses a carefully designed antigen derived from current H5N1 strains and is delivered via a harmless adenovirus vector, a platform
previously used in a COVID-19 nasal vaccine approved in India and under clinical testing in the U.S. The study, published on January 30, 2026, in Cell Reports Medicine, confirmed the vaccine’s
efficacy regardless of pre-existing immunity, a critical factor for real-world use. The team plans further animal and organoid studies, and aims to refine the vaccine to minimize interference from
prior seasonal flu exposure and enhance antiviral responses. Funding was provided by the NIH through the Cooperative Center for Human Immunology and the Center for Research on Structural Biology of
Infectious Diseases. The Boon lab received funding from Novavax Inc., and the Diamond lab from Moderna, among others.\n\nPublished date: January 30 2026, 22:30\n\nURL:
https://www.newswise.com/articles/nasal-vaccine-combats-bird-flu-infection-in-rodents/?sc=rsla\nSource: Newswise - Latest News\nClassification: Science\nSentiment: positive\nReporting voice:
Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: Bird Flu Is Evolving  --  Are Our Vaccines Keeping Up?\n\nSummary: \nBird flu (H5N1) continues to evolve rapidly,
with increasing evidence of infection in mammals, including cattle and humans, raising concerns about pandemic potential. Despite no new human cases globally or in dairy cattle since mid-December
2025, the virus remains a significant threat due to its high fatality rate, broad host range, multiple genetic clades, and spillover risk. A Phase I clinical trial by BlueWillow Biologics tested an
intranasal H5N1 vaccine using a shelf-stable oil-in-water emulsion adjuvant (W805EC), showing strong safety and promising immune responses in 40 healthy adults. Key findings include robust mucosal
immunity in the nose and airways, systemic priming, cellular responses, and broad cross-clade recognition—meaning the immune system responded to multiple H5N1 strains, not just one. The vaccine also
showed potential for dose-sparing, which could stretch stockpiles during outbreaks. Unlike traditional intramuscular vaccines, this intranasal approach offers needle-free delivery, improved patient
acceptance, and targeted protection at the virus’s entry point. While larger trials are needed to confirm prevention of infection or transmission, the results suggest a path toward a universal flu
vaccine with broader, faster, and more scalable protection. Experts emphasize that preparedness must advance during calm periods, not during crises. The NanoVax® platform may also be adapted for other
respiratory viruses like RSV and coronaviruses. The article concludes that as H5N1 evolves, the real question is whether humanity will be ready with next-generation tools.\n\nPublished date: January
29 2026, 21:16\n\nURL: https://medium.com/@jsteier_29203/bird-flu-is-evolving-are-our-vaccines-keeping-up-a83dbf1cf3bd\nSource: Medium.com\nClassification: Health\nSentiment: neutral\nReporting voice:
Explanatory\nContinent: North America\n\n</doc>\n\n------News Summaries End------\n","offset":10,"hit_cache":false}
```

## 💬 Response

Now let me get more specific data on when the last US case was reported and the rate of new cases.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "\"H5N1\" human case United States 2026 new CDC confirmed site:cidrap.umn.edu OR site:cdc.gov"
}
```

### 📋 Result

```
{"query": "\"H5N1\" human case United States 2026 new CDC confirmed site:cidrap.umn.edu OR site:cdc.gov", "results": [{"title": "A(H5) Bird Flu: Current Situation | Bird Flu | CDC", "url":
"https://www.cdc.gov/bird-flu/situation-summary/index.html", "snippet": "What to know\n- A(H5) bird flu is widespread in wild birds worldwide and is causing outbreaks in poultry and U.S. dairy cows
with sporadic human cases in U.S. dairy and poultry workers.\n- While the current public health risk is low, CDC is watching the situation carefully and working with states to monitor people with
animal exposures.\n- CDC is using its flu surveillance systems to monitor for A(H5) bird flu activity in people.\n![H5N1 Bird Flu How is it Spreading?](/bird-flu/media/images/2024/07/", "api_data":
null, "hint": null}, {"title": "Global Human Cases with Influenza A(H5N1), 1997-2026 | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html", "snippet":
"What to know\nThis graph shows all human infections with HPAI A(H5N1) bird flu virus reported to the World Health Organization (WHO), since the first human cases in 1997.\nBackground\nThis graph
shows all human infections with HPAI A(H5N1) bird flu virus reported to the [World Health Organization](https://www.who.int/teams/global-influenza-programme/avian-influenza) (WHO), since the first
human cases in 1997.\nA(H5N1) bird flu viruses first emerged in southern China in 1996. Those viruses caused lar", "api_data": null, "hint": null}, {"title": "Weekly US Influenza Surveillance Report:
Key Updates for Week 51, ending December 20, 2025 | FluView | CDC", "url": "https://www.cdc.gov/fluview/surveillance/2025-week-51.html", "snippet": "Key points\n- Please note: Week 52 FluView will be
posted on Monday January 5 due to the New Year holiday.\n- Seasonal influenza activity is elevated and continues to increase across the country.\nSummary\nViruses\nIllness\nAll data are preliminary
and may change as more reports are received.\nDirectional arrows indicate changes between the current week and the previous week. [Additional
information](https://www.cdc.gov/fluview/surveillance/2025-week-51.html#cdc_data_surveillance_section_5-additional-n", "api_data": null, "hint": null}, {"title": "Weekly US Influenza Surveillance
Report: Key Updates for Week 50, ending December 13, 2025 | FluView | CDC", "url": "https://www.cdc.gov/fluview/surveillance/2025-week-50.html", "snippet": "Key points\n- Note: Due to the Christmas
Holiday, FluView for Week 51 will be posted on December 30, 2025.\n- Seasonal influenza activity continues to increase across the country.\nSummary\nViruses\nIllness\nAll data are preliminary and may
change as more reports are received.\nDirectional arrows indicate changes between the current week and the previous week. [Additional
information](https://www.cdc.gov/fluview/surveillance/2025-week-50.html#cdc_data_surveillance_section_5-additional-national-and-inte", "api_data": null, "hint": null}, {"title": "A(H5) Bird Flu
Surveillance and Human Monitoring | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/h5-monitoring/index.html", "snippet": "At a glance\nOverview\nA(H5) Bird Flu Surveillance in U.S.\nOn July 7,
2025, CDC streamlined A(H5) bird flu updates with routine influenza data updates and updated reporting cadences to reflect the current public health situation. As such, several changes were made to
this page:\n- Data on the number of people monitored and tested for bird flu, as well as animal and epidemiologically linked human cases are reported monthly.\n- Data that are reported in
CDC's\n[FluView](https://www.cdc.gov/fluview/inde", "api_data": null, "hint": null}, {"title": "H5N1 strikes more poultry in 4 states; CDC updates details on recent human cases | CIDRAP", "url":
"https://www.cidrap.umn.edu/avian-influenza-bird-flu/h5n1-strikes-more-poultry-4-states-cdc-updates-details-recent-human-cases", "snippet": "In new H5N1 avian flu confirmations today, the US
Department of Agriculture (USDA) Animal and Plant Health Inspection Service (APHIS) reported that the virus hit more [flocks](https://www.aphis.usda.gov/livestock-poultry-disease/avian/avian-
influenza/hpai-detections/commercial-backyard-flocks) in four states, including another massive layer farm in Ohio, the nation\u2019s second biggest poultry producer.\n![egg
shortage](/sites/default/files/egg%20shortage.jpg)\nOver the past several weeks, Ohio has be", "api_data": null, "hint": null}, {"title": "Current Situation: H5N1 Bird Flu in People | Bird Flu | CDC",
"url": "https://www.cdc.gov/bird-flu/situation-summary/inhumans.html", "snippet": "Highlights\n- Sporadic avian influenza A(H5N1) virus infections (\"H5N1 Bird Flu\") in people have been reported
worldwide since 1997.\n- Highly pathogenic avian influenza A(H5N1) viruses are widespread in wild birds worldwide, have caused poultry outbreaks in many countries, and infected other kinds of animals.
H5N1 bird flu has caused outbreaks in U.S. poultry and dairy cows.\n- In the United States, sporadic human infections with A(H5N1) viruses have occurred since 2022 mostly after direct or clos",
"api_data": null, "hint": null}, {"title": "CDC confirms first severe H5N1 case in US patient | CIDRAP", "url": "https://www.cidrap.umn.edu/avian-influenza-bird-flu/cdc-confirms-first-
severe-h5n1-case-us-patient", "snippet": "The US Centers for Disease Control and Prevention (CDC) today announced that it has confirmed the nation\u2019s first severe H5N1 avian flu case, which
involves a probable illness reported by Louisiana health officials a few days ago.\nThe CDC said the illness also marks the nation's avian flu infection linked to exposure to backyard poultry. At a
briefing today, a top CDC official said the severe clinical picture and the backyard poultry exposure matches the global pattern seen over the years in othe", "api_data": null, "hint": null},
{"title": "CDC A(H5N1) Bird Flu Response Update March 19, 2025 | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/spotlights/h5n1-response-03192025.html", "snippet": "At a glance\nIn this
spotlight, CDC provides laboratory updates on serology testing from close contacts of a confirmed case of influenza A(H5) virus infection in a child in California, as well as sequencing information
for A(H5) viruses related to the most recent Ohio human case. CDC also summarizes findings from recently published studies.\nRisk assessment\nCDC recently published [an updated avian influenza A(H5N1)
virus risk assessment](https://www.cdc.gov/cfa-qualitative-assessments/php/data-res", "api_data": null, "hint": null}, {"title": "First H5 Bird Flu Death Reported in United States | CDC Newsroom",
"url": "https://www.cdc.gov/media/releases/2025/m0106-h5-birdflu-death.html", "snippet": "Statement\nJanuary 6, 2025 -- CDC is saddened by Louisiana's report that a person previously hospitalized with
severe avian influenza A(H5N1) illness (\"H5N1 bird flu\") has passed away. While tragic, a death from H5N1 bird flu in the United States is not unexpected because of the known potential for infection
with these viruses to cause severe illness and death. As of January 6, 2025, there have been 66 confirmed human cases of H5N1 bird flu in the United States since 2024 and 67 since 2022. This ",
"api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.cdc.gov/bird-flu/situation-summary/inhumans.html",
  "prompt": "What is the current total number of confirmed human H5N1 cases in the US? When was the most recent case? What was the last date a new case was added? How many cases in 2025 and 2026? Any cases after December 2025?"
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/bird-flu/situation-summary/inhumans.html", "content": "Based on the provided content, **specific numbers and dates for H5N1 cases are not included in this text**. \n\nThe
content mentions that:\n- Several human cases have been identified in the United States since 2022\n- Most cases have been clinically mild, with a few hospitalizations and one death reported (death
announced on January 6, 2025)\n- The CDC maintains updated case totals on a separate page\n\n**The text does not provide:**\n- Current total number of confirmed cases\n- Date of most recent case\n-
Number of cases in 2025 or 2026\n- Any specific case dates\n\nTo get this information, you would need to check the linked CDC page that tracks current case numbers.\n\n**Relevant links:**\n- [H5 Bird
Flu: Current Situation](https://www.cdc.gov/bird-flu/situation-summary/index.html) - Contains updated totals of human cases with breakdown by exposure source and location\n- [H5N1 Bird Flu
Surveillance and Human Monitoring](https://www.cdc.gov/bird-flu/h5-monitoring/index.html)\n- [CDC spotlight articles on bird flu](https://www.cdc.gov/bird-flu/spotlights/index.html)\n- [Reported Human
Infections with Avian Influenza A Viruses](https://www.cdc.gov/bird-flu/php/surveillance/reported-human-infections.html)", "title": "Current Situation: H5N1 Bird Flu in People"}
```

## 💭 Thinking

Let me gather more specific data about the timeline and rate of H5N1 human cases in the US. I need to understand:
1. The current count (71 as of the CDC page)
2. When the last case was reported
3. The rate of new cases
4. Whether H5N1 is still circulating in US animals (dairy, poultry)

From what I've gathered so far:
- CDC reports 71 total US human H5N1 cases since February 2024
- The PMC article mentions 70 cases through May 2025
- One article from January 29, 2026 says "no new human cases globally or in dairy cattle since mid-December 2025"


- The virus is still actively spreading in poultry with major outbreaks across several states in early 2026, and Washington state has documented 14 presumptively positive farmworkers since 2022

Now I need to search for any confirmed cases after mid-December 2025 to determine whether the count increased between March 16 and April 30, 2026. The key question is whether we've moved from 71 cases to a higher number during that specific timeframe.

## 💬 Response

Let me search for more specific recent data about the pace of new cases and any cases since December 2025.

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "H5N1 bird flu new human case United States 2026 CDC confirmed",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "H5N1 Bird Flu: First Severe US Case Linked to Backyard Birds - CDC Update", "url": "https://time.news/h5n1-bird-flu-first-severe-us-case-linked-to-backyard-birds-cdc-update/", "snippet":
"H5N1 Bird Flu: First Severe US Case Linked to Backyard Birds - CDC Update\n\nHealth\n\n# H5N1 Bird Flu: First Severe US Case Linked to Backyard Birds \u2013 CDC Update\n\nMarch 21, 2026\n\nMarch 21,
2026\n\n\n\n36\n\nThe Centers for Disease Control and Prevention confirmed Friday the first instance of severe illness in the United States linked to the H5N1 avian influenza virus, commonly known as
bird flu. The hospitalized patient, in Louisiana, contracted the virus after exposure to sick and dead birds in a backya", "highlights": ["March 21, 2026\n\nMarch 21, 2026 \n\n36 The Centers for
Disease Control and Prevention confirmed Friday the first instance of severe illness in the United States linked to the H5N1 avian influenza virus, commonly known as bird flu. The hospitalized
patient, in Louisiana, contracted the virus after exposure to sick and dead birds in a backyard flock, marking a new dimension to the ongoing spread of H5N1 in the country. Whereas human cases of
avian influenza are not uncommon, this represents the first severe case identified in the U.S. During the current outbreak, raising public health awareness and prompting renewed calls for vigilance.
Since April 2024, a total of 61 human cases of H5 bird flu have been reported across the United States, according to the CDC. Yet, these prior cases were largely mild or asymptomatic. This new case in
Louisiana is distinct, prompting a deeper investigation into the specific strain and potential for wider transmission. The virus identified in the patient belongs to the D1.1 genotype, which has been
detected in wild birds and poultry in the U.S., as well as in recent human cases in British Columbia, Canada, and Washington state. This is a different genotype than the B3.13 strain that has  ...
The emergence of H5N1 in both poultry and mammals \u2013 including cows \u2013 has been a growing concern for public health officials throughout 2024. The virus typically spreads among birds, but the
recent spillover into mammals raises the possibility of increased opportunities for human exposure. The CDC emphasizes that the current risk to the general public remains low, and no person-to-person
spread has been detected. However, the agency is closely monitoring the situation and conducting genomic sequencing to understand how the virus is evolving. The genetic analysis currently underway at
the CDC is crucial. Understanding the specific characteristics of the D1.1  ...    The Louisiana case highlights a previously under-recognized source of potential exposure: backyard poultry flocks.
...    smaller, non-commercial flocks can often go undetected. The CDC is now emphasizing the importance of biosecurity  ...    Hunters and other bird enthusiasts are as well being urged to take
precautions. The U.S. Department of Agriculture (USDA) provides specific guidance for hunters on how to minimize the risk of spreading the virus while handling wild  ...    The CDC recommends several
key steps to prevent infection with H5N1 bird flu. Avoiding contact with sick or dead  ...    wearing recommended PPE, such as gloves, masks, and eye protection, is essential. It\u2019s also important
to avoid touching  ...    Infected birds shed the virus in their saliva, mucous, and feces. Other animals, like cows, can also shed the virus in  ...    The CDC provides regularly updated information
on the H5N1 situation, including case counts and guidance for the public. You can find the latest information on the CDC\u2019s H5 Bird Flu: Current Situation page. Disclaimer: This information is for
general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare professional for any health concerns or before making
...    The CDC will continue to monitor the situation closely and provide updates as new information becomes available. The next scheduled update from the CDC regarding H5N1 is planned for January 2,
2025, where they will present a comprehensive analysis of the recent cases and any changes to public health recommendations. We encourage readers to  ...    0 comments 0 Facebook Twitter Pinterest
Email\n\nprevious post ##### Minecraft Theme Park: $70M Attraction Coming to Chessington World of Adventures Minecraft Theme Park: $70M Attraction Coming to Chessington World of Adventures\n\nnext
post ##### 2026 Women\u2019s NCAA Tournament: Saturday\u2019s Scores & Schedule 2026 Women\u2019s NCAA Tournament: Saturday\u2019s Scores & Schedule\n\n#### You may also like\n\n ### Ozempic, Wegovy &
Mounjaro: Does Medicaid Cover Weight...\n\n ### Genetic Risk Communication: Study Details Blueprint for Responsible...\n\n ### Sleep Deprivation & Dementia Risk: What the Latest...\n\n ### Cancer
Cells \u2018Addicted\u2019 to Antioxidant Glutathione: New Treatment...\n\n ### NYU Long Island Med Students Match to Residency...\n\n ### GLP-1 Drugs & Weight Loss: Why Lifestyle Changes...\n\n ###
FFR-Guided CABG Improves Outcomes in Valve Surgery Patients...\n\n ### [H1N1 in Mace"], "published_date": "2026-03-21T00:00:00.000", "score": null}, {"title": "Bird Flu (H5N1) in Child: First US Case
& Risk Information", "url": "https://time.news/bird-flu-h5n1-in-child-first-us-case-risk-information/", "snippet": "Bird Flu (H5N1) in Child: First US Case & Risk Information\n\nHealth\n\n# Bird Flu
(H5N1) in Child: First US Case & Risk Information\n\nMarch 23, 2026\n\nMarch 23, 2026\n\n\n\n42\n\nCalifornia health officials have confirmed the first case of avian influenza A(H5N1), commonly known
as bird flu, in a child within the United States. The Centers for Disease Control and Prevention (CDC) announced the case on Wednesday, May 8, 2024, noting that the child experienced mild symptoms and
has been treated with antivira", "highlights": ["2026\n\nMarch 23, 2026\n\n\n\n42 California health officials have confirmed the first case of avian influenza A(H5N1), commonly known as bird flu, in a
child within the United States. The Centers for Disease Control and Prevention (CDC) announced the case on Wednesday, May 8, 2024, noting that the child experienced mild symptoms and has been treated
with antiviral medications. This development comes as health authorities continue to monitor the spread of H5N1, particularly following outbreaks in both wild birds and, more recently, dairy cattle
across several states. The case was identified through routine influenza testing and reported to the California Department of Public Health (CDPH) through established surveillance systems. Whereas
this is the first confirmed pediatric case in the U.S., It\u2019s the second human case detected through national surveillance this year. According to the CDC, the child\u2019s initial test showed low
levels of the virus, and subsequent testing days later was negative for H5N1 but positive for other common  ...    The current outbreak of H5N1 began in 2022, initially impacting wild birds and
domestic poultry. Since August 2024, the virus has spread to dairy herds in California and other states, prompting increased monitoring and testing. As of May 8, 2024, the CDC reports 55 human cases
of H5 bird flu have been identified in the United States this year, with 29 of those cases occurring in California. The CDC\u2019s influenza surveillance systems are actively tracking the virus\u2019s
evolution and spread. What sets this case apart is the age of the patient. Previously confirmed human cases in the U.S. Have generally involved individuals with direct exposure to infected animals.
The CDPH is currently investigating potential sources of exposure for the child, and testing has been conducted on all household members. Importantly, initial results indicate that other members of
the household did not contract H5N1, though some tested positive for other common respiratory viruses. Contact tracing is ongoing to identify any potential further spread, but currently, there is no
evidence of  ...    Health officials emphasize that, to date, there has been no evidence of sustained person-to-person spread of H5N1 in the United States. While limited and sporadic human infections
have been reported in other countries, these cases are uncommon and often linked to close contact with infected poultry. The CDC continues to stress that the overall risk to the general public remains
low. However, individuals who work with or are in close proximity to infected animals \u2013 including birds, poultry, dairy cattle, and other livestock \u2013 are considered to be at higher risk. The
CDC recommends avoiding unprotected contact with sick or dead animals. This includes wild birds, poultry, and livestock. Proper biosecurity measures, such as wearing protective gear and practicing
decent hygiene, are crucial for  ...    \u201cThis case underscores the importance of continued vigilance and surveillance,\u201d says Dr. Demetre Daskalakis, Director  ...    The CDC\u2019s risk
assessment remains focused on those with direct animal exposure. The agency is actively monitoring the virus for any signs of mutation that could increase its transmissibility among humans. While the
current strain of H5N1  ...    The California Department of Public Health has also issued a statement, emphasizing its commitment to protecting public  ...    Dairy cows are among the animals affected
by the current H5N1 outbreak. Image courtesy of the CDC. The situation is evolving, and the CDC will continue to provide updates as more information becomes available. The next scheduled update from
the CDC regarding H5N1 surveillance is expected on May 15, 2024. For the latest information and guidance, please visit the CDC\u2019s website and the California Department of Public Health website.
Disclaimer: This article provides information for general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare
professional for any health concerns  ...    Have questions or thoughts about this developing story? Share your comments below, and please consider sharing this  ...    ##### ASUS & NVIDIA RTX 5000:
Laptopuri Performante pentru Orice Task (2024) ASUS & NVIDIA RTX 5000: Laptopuri Performante pentru Orice Task (2024)\n\nnext post ##### Cal Raleigh: Mariners Catcher\u2019s Intense Spring Training
Push After WBC Cal Raleigh: Mariners Catcher\u2019s Intense Spring Training Push After WBC\n\n#### You may also like \n\n### WHO Urges Faster TB Diagnosis with New Tests...\n\n ### Family
Estrangement: Protecting Your Wellbeing & Healing Grief\n\n ### Healthcare Collapse: Can AI Offer a Solution?\n\n ### Measles Outbreak in Indonesia: Cases Rise Ahead of...\n\n  ...    ### Nasal Swab
Detects Early Alzheimer\u2019s Signs Before Symptoms...\n\n ### [Karlsruhe: Woman Faces Eviction, Hopes for Delay]<"], "published_date": "2026-03-23T00:00:00.000", "score": null}, {"title": "A(H5)
Bird Flu: Current Situation - CDC", "url": "https://www.cdc.gov/bird-flu/situation-summary/index.html", "snippet": "A(H5) Bird Flu: Current Situation | Bird Flu | CDC\n\n# A(H5) Bird Flu: Current
Situation\n\nMar. 6, 2026\n\nEspa\u00f1ol\n\n## What to know\n\n- A(H5) bird flu is widespread in wild birds worldwide and is causing outbreaks in poultry and U.S. dairy cows with sporadic human cases
in U.S. dairy and poultry workers.\n- While the current public health risk is low, CDC is watching the situation carefully and working with states to monitor people with animal exposures.\n- CDC is
using its flu surveillance systems to ", "highlights": ["know - A(H5) bird flu is widespread in wild birds worldwide and is causing outbreaks in poultry and U.S. dairy cows with sporadic human cases
in U.S. dairy and poultry workers. - While the current public health risk is low, CDC is watching the situation carefully and working with states to monitor people with animal exposures. - CDC is
using its flu surveillance systems to monitor for A(H5) bird flu activity in people. ## Current situation\n\n### A(H5) Bird Flu Human Cases in U.S. On July 7, 2025, CDC streamlined A(H5) bird flu
updates with routine influenza data updates and updated reporting cadences to reflect the current public health situation. As such, the following changes were made to this page: Data on the number of
people monitored and tested for bird flu are available at A(H5) Bird Flu Surveillance and Human Monitoring | Bird Flu | CDC and are reported monthly. USDA data on highly pathogenic avian influenza
(HPAI) detections in animals will no longer be reported on the CDC website. These data can be found on USDA's website. CDC will continue to report any additional human cases of A(H5) bird flu here and
in FluView. ### National situation summary since 2024 Footnote: Of the 71 total reported human cases of A(H5) bird flu reported in the United States since February 2024, seven were detected through
national flu surveillance and 64 were detected through human monitoring. ### Resource\n\nNovel flu case data by season and virus subtype are available\n\nFluView Interactive ### Situation summary of
confirmed and probable human cases since 2024 When a case tests positive for A(H5) at a public health laboratory but testing at CDC is not able to confirm A(H5) infection, per Council of State and
Territorial Epidemiologists (CSTE) guidance, a case is reported as probable. In January 2025, CDC updated requirements. After a public health laboratory's first three cases of influenza A(H5) virus
have been confirmed by CDC, subsequent detections by that laboratory can be considered  ...    ### Bird flu surveillance\n\nAdditional A(H5) bird flu surveillance, testing, and people monitoring data
are available. Surveillance & Human Monitoring\n\n### Detections in Animals For data on HPAI detections in animals, visit the USDA website.\n\n## What's New\n\nView More Mar. 6, 2026\n\nSources Print
Share\n\nContent Source: National Center for Immunization and Respiratory Diseases (NCIRD)"], "published_date": "2026-03-06T00:00:00.000", "score": null}, {"title": "Global Human Cases with Influenza
A(H5N1), 1997-2026 | Bird Flu", "url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-ah5n1.html", "snippet": "Global Human Cases with Influenza A(H5N1), 1997-2026 | Bird Flu |
CDC\n\n# Global Human Cases with Influenza A(H5N1), 1997-2026\n\nMar. 20, 2026\n\n## What to know\n\nThis graph shows all human infections with HPAI A(H5N1) bird flu virus reported to the World Health
Organization (WHO), since the first human cases in 1997.\n\n## Background\n\nThis graph shows all human infections with HPAI A(H5N1) bird flu virus reported to the World Health Organization(WHO),
since the first human cases in 1997.\n\nA(H5N1) bir", "highlights": ["Global Human Cases with Influenza A(H5N1), 1997-2026 | Bird Flu | CDC  ...    This graph shows all human infections with HPAI
A(H5N1) bird flu virus reported to the World Health Organization (WHO), since the first human cases in 1997.  ...    This graph shows all human infections with HPAI A(H5N1) bird flu virus reported to
the World Health Organization(WHO), since the first human cases in 1997. A(H5N1) bird flu viruses first emerged in southern China in 1996. Those viruses caused large poultry outbreaks in Hong Kong in
1997, which resulted in 18 human infections. The 1997 bird outbreak was controlled, but the A(H5N1) bird flu viruses were not eradicated in birds and re-surfaced in 2003 to spread widely in birds
throughout Asia, and later in Africa, Europe, and the Middle East, causing poultry outbreaks and sporadic human infections. Since 2003, more than 23 countries have reported more than 890 sporadic
human infections with A(H5N1) bird flu viruses to WHO. A(H5N1) bird flu viruses that are currently circulating in wild birds and poultry in much of the world are genetically different from earlier
versions of the virus and emerged to become the predominant subtype of HPAI H5 in the fall of 2021. These viruses have caused sporadic wild bird infections and poultry outbreaks in many countries,
including the United States, with spillover to mammals in some countries. In contrast to previous A(H5N1) viruses, which still circulate to a lesser extent in several countries, at this time, a small
number of sporadic human cases with current A(H5N1) bird flu viruses have been reported globally. However, illness in humans from all bird flu virus infections has ranged in severity from no symptoms
or mild illness to severe disease that resulted in death. * Several recent A(H5) cases have been reported in the U.S. The CDC has been unable to isolate the virus from the recent human cases. As a
result, CDC has been unable to determine the virus's neuraminidase subtype or whether it is likely an N1. This data will be updated biweekly on Fridays. For more data on H5 cases in the United States,
visit: H5 Bird Flu: Current Situation | Bird Flu | CDC Mar. 20, 2026\n\nSources Print Share\n\nContent Source: National Center for Immunization and Respiratory Diseases (NCIRD)"], "published_date":
"2026-03-19T19:39:15.376", "score": null}, {"title": "Novel H5N1 Bird Flu Outbreak - American Academy of Ophthalmology", "url": "https://www.aao.org/education/bird-flu", "snippet": "Novel H5N1 Bird
Flu Outbreak - American Academy of Ophthalmology\n\nShop\n\nLog In Create an Account\n\n- For Public & Patients\n- For Clinical Teams\n- For Practice Management\n- For Ophthalmologists\n- Medical
Students\n\n- Museum of the Eye\n- Foundation\n- About\n\nAs of December 17, 2025, a total of 71 human cases of highly pathogenic avian influenza have been identified in the United States since 2024.
This ongoing multistate outbreak of influenza A (H5N1) has primarily been limited to exposure to infecte", "highlights": ["- For Practice Management  ...    - Museum of the Eye\n- Foundation\n- About
As of December 17, 2025, a total of 71 human cases of highly pathogenic avian influenza have been identified in the United States since 2024. This ongoing multistate outbreak of influenza A (H5N1) has
primarily been limited to exposure to infected dairy cows and poultry, with cases in California, Colorado, Iowa, Louisiana, Michigan, Missouri, Nevada, Ohio, Oregon, Texas, Washington, Wisconsin, and
Wyoming. There have been 2 associated deaths and 3 reported cases in which the exposure source was unknown. There is no known person-to-person spread, and the CDC still  ...    Because the predominant
symptoms in the majority of patients to date have been related to conjunctivitis, and multiple patients' conjunctival swabs tested positive for the virus, the CDC recommends that clinicians [consider
the  ...    - Highly Pathogenic Avian Influenza A Viruses\n- Precautions for Worker Protection  ...    - Guidelines for Clinicians and Evaluating Patients\n- H5N1 Bird Flu: Current Situation Summary
...    - Gloves, N95 masks or equivalent, and goggles or face shield are recommended for high-risk exposures to H5N1. Hand  ...    cows or livestock. Multiple human H5N1 infections, presumably
transmitted from sick cows and poultry, presented with  ...    - Complications: pneumonia, respiratory failure, acute respiratory distress syndrome, multi-organ failure (respiratory  ...    -
Influenza A H5N1 can be detected by FDA-cleared and approved assays for influenza A. These tests, however, cannot  ...    Waterfowl are the natural reservoir of all known influenza A viruses.
Influenza A viruses belong to the family  ...    Highly pathogenic avian influenza (HPAI) A (H5N1) virus has spread widely through migratory birds to many regions of the world, causing infections of
many wild bird species, poultry outbreaks, with spillover to mammals. Since 1997, multiple outbreaks of avian influenza A H5N1 and H7N9 in domestic poultry have been reported. The most recent outbreak
of H5N1 started at the end of 2020 and killed more than 100 million birds. Human infections were rare and occurred in  ...    (H5N1) viruses since 1997. According to the World Health Organization
(WHO), there have been fewer than 900 cases and 493 deaths (>50%) in humans due to H5N1 from 2003 to April 2024. An animal study of A/Texas/37/2024 HPAI H5N1 that had been isolated from an infected
dairy cattle worker found that the virus was transmissible via respiratory droplets and lethal in 5 of 6 exposed ferrets.Currently, in the US, since February 2022, there have been widespread poultry
outbreaks, with nearly 97 million commercial poultry and backyard flocks dying or culled to contain the spread. In March 2024, the first multistate outbreak of avian influenza A H5N1 in cows was
documented in the United States.  ...    Avian influenza A viruses are classified into two categories: low pathogenic and highly pathogenic. Highly pathogenic  ...    The first human outbreak of avian
influenza A (H5N1) occurred in Hong Kong in 1997. Prior to this outbreak, several avian outbreaks occurred on farms. H5N1 appears to be more readily transmitted from poultry to people than H7N9. This
virus has a strong affinity for \u03b1-2,3-linked sialic acid receptors, which are present in the lower respiratory tract of humans. These receptors are also present on the conjunctiva, which likely
explains the 2 recent cases with only ocular symptoms or signs. H5N1 can be transmitted from birds to cows and can be detected in cow\u2019s milk. There was sero-epidemiologic evidence that H5N1 can
be transmitted from patients to healthcare workers from this 1997 H5N1 outbreak in Hong Kong.The first human case of H5N1 in the United States occurred in 2022. In 2024, a multistate outbreak in
humans began and was primarily related to occupational exposure to sick cows or poultry. In multiple patients, H5N1 viruses were detected at higher levels in conjunctival swabs compared with samples
from the upper respiratory tract. H5N1 in the United States (2022 to 2025) - In February 2025, the CDC published a serosurvey of 150 veterinary practitioners, 3 of whom showed evidence of recent H5N1
infection. All 3 practitioners were asymptomatic. One practiced in a state without any known cattle or human H5N1 infections and had no known or suspected H5N1 exposure. - On January 6, 2025, the CDC
reported the first H5N1-related death%20has%20passed%20away) in the United States in Louisiana. - In November 2024, the first case of H5N1 in a child in the United States was reported in California. -
In October 2024, multiple cases in California were reported in patients with exposure to infected dairy  ...    - One case reported in September 2024 in Missouri was the first to occur without any
known exposure to sick  ...    - A cluster of cases in Colorado were summarized by the CDC on August 29, 2024. These cases occurred in  ...    at these 2 facilities, 109 were tested, and 9 were
positive for H5N1. Only a conjunctival swab was positive in 5  ...    - Three cases were reported in March 2024 (Texas) and May 2024 (Michigan) in adult dairy farm workers exposed to sick  ...    -
The first human case was reported in the United Kingdom in January 2022. The affected person lived with a large flock "], "published_date": null, "score": null}, {"title": "A(H5) Bird Flu Surveillance
and Human Monitoring - CDC", "url": "https://www.cdc.gov/bird-flu/h5-monitoring/index.html", "snippet": "A(H5) Bird Flu Surveillance and Human Monitoring | Bird Flu | CDC\n\n# A(H5) Bird Flu
Surveillance and Human Monitoring\n\nSituation through January 31, 2026\n\nFeb. 6, 2026\n\n## At a glance\n\nCDC influenza (flu) surveillance systems currently show no indicators of unusual influenza
activity in people, including avian influenza A(H5).\n\n## Overview\n\n### A(H5) Bird Flu Surveillance in U.S.\n\nOn July 7, 2025, CDC streamlined A(H5) bird flu updates with routine influenza data
updates and updated reporting ca", "highlights": ["A(H5) Bird Flu Surveillance and Human Monitoring | Bird Flu | CDC\n\n# A(H5) Bird Flu Surveillance and Human Monitoring Situation through January 31,
2026\n\nFeb. 6, 2026\n\n## At a glance CDC influenza (flu) surveillance systems currently show no indicators of unusual influenza activity in people, including avian influenza A(H5). ##
Overview\n\n### A(H5) Bird Flu Surveillance in U.S. On July 7, 2025, CDC streamlined A(H5) bird flu updates with routine influenza data updates and updated reporting cadences to reflect the current
public health situation. As such, several changes were made to this page: - Data that are reported in CDC's FluView, National Wastewater Surveillance System (NWSS), and The National Syndromic
Surveillance Program (NSSP) will not be updated here but can be found on those respective webpages. - Data on the number of people monitored and tested for bird flu, as well as animal and
epidemiologically linked human cases are reported monthly. CDC uses multiple systems to monitor national, state, and local level influenza data during the current avian influenza A(H5) situation. -
CDC is actively looking at multiple flu indicators during the current situation to monitor for influenza A(H5) viruses, including looking for spread of the virus to, or among people, in jurisdictions
where the virus has been identified in people or animals. More information is available: FluView. - Human cases of novel influenza, which are human infections with non-human influenza A viruses that
are different from currently spreading seasonal human influenza viruses, are nationally notifiable. Every identified case is investigated and reported to CDC. - Influenza virus and illness activity
are monitored year-round through a collaborative effort between CDC and many  ...    February 2022 \u2013 Present CDC and state and local health departments monitor people exposed to infected birds,
poultry, dairy cows or other animals for 10 days after exposure. Between February 2022 and January 31, 2026, there have been - At least 1,300 people tested for novel influenza A\n- At least 31,900
people monitored and Current HPAI Outbreak (MMWR Week 40 2025 \u2013 Present) CDC and state and local health departments monitor people exposed to infected birds, poultry, dairy cows and other animals
for 10 days after exposure. Between September 28, 2025 and January 31, 2026 there have been - At least 120 persons tested for novel influenza A\n- At least 2,750 people monitored *CDC numbers are
based on weekly state aggregate reports since 2022. CDC defers to states for updated information on  ...    ## Monitoring for Novel Influenza A virus infections among people, including Influenza A(H5)
Note: Animal and epidemiologically linked human cases will be updated on the first Friday of every month. Data presented through: 1/31/2026; Data as of: 2/4/2026 ### Influenza A(H5) virus infections
in humans exposed to affected animals by state Data presented through: 1/31/2026; Data as of: 2/4/2026 ### Influenza A(H5) affected dairy herds and epidemiologically linked human cases Data presented
through: 1/31/2026; Data as of: 2/4/2026  ...    Data presented through: 1/31/2026; Data as of: 2/4/2026\n\n### Resource  ...    FluView Interactive ## Influenza Surveillance Systems CDC has multiple
surveillance systems that are used year-round to monitor key flu indicators. These data are reviewed comprehensively each week. Case Reporting\n\nFor the latest case counts, please visit the A(H5)
Bird Flu: Current Situation page. Public Health Laboratory Monitoring For more information on Public Health Laboratory testing visit FluView\n\nClinical Laboratory Trends For more information on
Clinical Laboratory trends visit FluView\n\nEmergency Departments For data on emergency department visits visit data.cdc.gov\n\nWastewater Surveillance For more information on wastewater surveillance
visit CDC\u2019s National Wastewater Surveillance System (NWSS) ## Explore Deeper\n\nFluView\n\nWeekly U.S. Influenza Surveillance Report Novel A FluView Interactive\n\nRespiratory Illnesses Data
Channel View data for COVID-19, flu, and RSV activity in your community and across the United States.\n\nFeb. 6, 2026 Sources Print Share\n\nContent Source:\n\n[National Center for Immunization and
Res"], "published_date": "2026-03-06T00:00:00.000", "score": null}, {"title": "Avian Influenza A(H5N5)- United States of America", "url": "https://www.who.int/emergencies/disease-outbreak-
news/item/2025-DON590", "snippet": "Avian Influenza A(H5N5)- United States of America Skip to main content\n\n## Disease Outbreak News\n\n# Avian Influenza A(H5N5) - United States of America\n\nSee
all DONs related to this event\n\n### Situation at a glance\n\nOn 15 November 2025, WHO was notified of the 71st confirmed human case with influenza A(H5) since early 2024 in the United States of
America\u2014 the first human case reported in the United States of America since February 2025. On 20 November, U.S. Centers for Disease Control and Prevent", "highlights": ["On 15 November 2025, WHO
was notified of the 71st confirmed human case with influenza A(H5) since early 2024 in the United States of America\u2014 the first human case reported in the United States of America since February
2025. On 20 November, U.S. Centers for Disease Control and Prevention (CDC) laboratory sequencing verified the virus as influenza A(H5N5), representing the first globally reported human case caused by
an influenza A(H5N5) virus. The investigation by  ...    contacts, and there is currently no evidence of human-to-human transmission. Due to the constantly evolving nature of  ...    On 15 November
2025, WHO was notified of a confirmed human infection with influenza A(H5) in the United States of America\u2014the first reported in the country since February 2025 and the 71st since early 2024. On
20 November, CDC laboratory sequencing verified the virus as influenza A(H5N5), representing the first human case of this subtype reported globally. The patient was an adult with underlying medical
conditions residing in Washington State. The  ...    was an influenza A(H5N5) virus belonging to the H5 haemagglutinin (HA) clade 2.3.4.4b[1].  ...    High pathogenicity avian influenza A(H5) clade
2.3.4.4b A(H5N5) viruses have been detected in North America in wild birds and wild mammals since at least 2023.[2] This is the first laboratory-confirmed human infection with an influenza A(H5N5)
virus in the United States of America and reported globally.  ...    become infected with A(H5) viruses. Influenza A(H5N5) viruses are detected in birds, including wild birds and domestic  ...
human cases are expected. The case had underlying conditions and subsequently died. The investigation by health  ...    amongst contacts, and there is currently no evidence of human-to-human
transmission. This is the 71st confirmed human case of A(H5) in the United States of America since early 2024, and the first since February 2025. To date, no human-to-human transmission has been
identified in any of the A(H5) cases reported in the United States of America. From a global perspective, while a few events with limited human-to-human transmission of zoonotic influenza A(H5) have
been described between 1997 and 2007, sustained human-to-human transmission has not been  ...    Based on available information, the WHO currently assesses the overall public health risk posed by
A(H5) viruses as  ...    [https://www.paho.org/en/documents/epidemiological-update-avian-influenza-ah5n1-americas-region-15-november-2024]<web_l  ...
81-a1af-d5f44f86423a.pdf?sfvrsn=9c68df20_1&download=true]  ...    [https://www.paho.org/en/documents/epidemiological-alert-human-infections-caused-avian-influenza-ah5n1-region-americas-  ...    Health
Organization. Cumulative number of confirmed human cases of avian influenza A(H5N1) reported to WHO. Geneva: WHO; 2025. Available from: https://www.who.int/publications/m/item/cumulative-number-of-
confirmed-human-cases-for-avian-influenza-a(h5n1)-reporte  ...    Animal Health (July 2025). Updated joint FAO/WHO/WOAH assessment of recent influenza A(H5N1) virus events in animals  ...
assessment-july-2025.pdf?sfvrsn=fe76b74e_1&download=true 29. Centers for Disease Control and Prevention (CDC). Weekly US Influenza Surveillance Report: Key Updates for Week 46, ending November 15,
2025. Available from: https://www.cdc.gov/fluview/surveillance/2025-week-46.html 30. Centers for Disease Control and Prevention (CDC). H5 Bird Flu: Current Situation. Available from:
https://www.cdc.gov/bird-flu/situation-summary/index.html  Citable reference: World Health Organization (5 December 2025). Disease Outbreak News; Avian Influenza A(H5N5)- United States of America.
Available at: [https://www/who.int/emergencies/disease-outbreak-news/item/2025-DON590]<web_link"], "published_date": "2025-12-05T00:00:00.000", "score": null}, {"title": "Preliminary human bird flu
case reported in Washington state", "url": "https://www.cidrap.umn.edu/avian-influenza-bird-flu/preliminary-human-bird-flu-case-reported-washington-state", "snippet": "Preliminary human bird flu case
reported in Washington state | CIDRAP\nUniversity of Minnesota\nMain navigation\n**University of Minnesota**\nhttp://twin-cities.umn.edu/\n612-625-5000\nGo to the U of M home page\n# Preliminary human
bird flu case reported in Washington state\nChris Dall, MA\nAvian Influenza (Bird Flu)\nVeterinarian swabbing rooster for avian flu\n> Merrimon / iStock\n> Share\n\nCopied to clipboard\n\nAn
individual in Washington state has preliminarily tested positive for H5N1 avian influenza, s", "highlights": ["# Preliminary human bird flu case reported in Washington state Chris Dall, MA\nAvian
Influenza (Bird Flu)Veterinarian swabbing rooster for avian flu\n> Merrimon / iStock\n> Share \nCopied to clipboard\n An individual in Washington state has preliminarily tested positive for H5N1 avian
influenza, state health officials said yesterday. If confirmed, it will be the first human bird flu case in the United States since February. In anews release, officials with the Washington State
Department of Health said the case-patient is an older adult from Grays Harbor County with underlying health conditions. The person was hospitalized after developing a high fever, confusion, and
respiratory distress in early November and continues to receive treatment. Confirmatory testing from the Washington State Public Health Laboratories is pending, and state and county officials are
working to determine the potential sources of infection. Thelast US human bird flucase was reported on February 14 in Platte County, Wyoming. On February 12, health officials in Ohio reported that
state's firsthuman H5N1 case. Both case patients were exposed through contact with infected poultry. According to theCenters for Disease Control and Prevention(CDC), 70 human H5N1 cases, including one
death, were confirmed in the United States from 2024 through July of this year, primarily in workers on poultry and dairy farms. The latter were sickened by an outbreak strain spreading in dairy
cattle. Person-to-person transmission of avian flu is rare and has never been documented in the United States. \"To ensure that human-to-human spread is not occurring, public health officials are
contacting anyone who has been in  ...    Meanwhile, commercial poultry operations around the country continue to get hit with H5N1 outbreaks. In the  ...    Commercial turkey meat operations and
backyard flocks in Michigan have also been hit by H5N1 outbreaks, along with backyard flocks in New Hampshire and Texas. H5N1 detections are higher in the fall and spring, as wild birds spread the
virus during their migration. Over the last 30 days, 76 confirmed flocks (38 commercial and 38 backyard) have been hit by H5N1 outbreaks, and 1.66 million birds  ...    ## Related news\n\n### Avian
flu has decimated world's largest breeding colony of southern elephant seals  ...    ### Intranasal vaccine against H5 avian flu provokes broad immune response in adults in phase 1 trial\nMary Van
BeusekomIntranasal vaccine\n\n ### Review: Human H5N1 avian flu cases can be asymptomatic, and the virus likely spreads among people\nMary Van BeusekomPerson feeding chickens by hand\n\n ### Avian flu
detections in wild birds, including waterfowl, spike across US\nStephanie SoucherayCanadian geese \n\n ### Cambodia tracks H5N1 avain flu in young girl, as China sees more H9N2 cases\nStephanie
Soucheraybackyard birds\n\n\n### Flurry of H5N1 activity noted in commercial poultry, wild birds Stephanie Soucheray\nturkeys in cages\n\n\n### H5N1 strikes more turkeys in 2 states Lisa
Schnirring\nturkey farm\n\n ### Los Angeles cat H5N1 deaths prompt new warning about raw pet food\nLisa Schnirring  ...    ### With an absent CDC and mismatched 'subclade K' flu strain, experts face
upcoming season with uncertainty Early data from the UK and Japan show that the H3N2 subclade K was represented in 90% of flu samples.  ...    ### Five new avian flu outbreaks confirmed in ducks,
turkeys in 3 US states  ...    Mary Van Beusekom\n\n7. \n### The order of pre-COVID chronic conditions may best predict long-COVID risk  ...    ### Intranasal vaccine against H5 avian flu provokes
broad immune response in adults in phase 1 trial  ...   Bentson Foundation logo\nPrincipal Underwriter\n\n[\nUnorthodox Philanthropy logo  ...    Become an Underwriter\n* News\n* Topics & Projects\n*
Antimicrobial Resistance * COVID-19\n* Chronic Wasting Disease\n* Influenza * Resilient Drug Supply\n* All Topics A-Z\n* Coronavirus Vaccines Roadmap * Influenza Vaccines Roadmap\n* Roadmaps for
Priority Pathogens * Vaccine Integrity Project\n* CIDRAP Leadership Forum\n*.\n*.\n* Podcasts  ...    * Newsletters\n* About\n* About CIDRAP\n* CIDRAP in the News\n* Our Staff * Our Director\n*
Osterholm in the Press\n* [Shop Mer"], "published_date": "2025-11-14T00:00:00.000", "score": null}, {"title": "Highly Pathogenic Avian Influenza Outbreak in the United States", "url":
"https://gisaid.org/resources/gisaid-in-the-news/highly-pathogenic-avian-influenza-outbreak-in-the-united-states/", "snippet": "GISAID - Highly Pathogenic Avian Influenza Outbreak in the United
States\n### **H5N1 Bird Flu continues to take its toll in the United States**\nClade 2.3.4.4b of the highly pathogenic avian influenza (HPAI) virus causing outbreaks in wild and domestic birds around
the world, continues to spread in dairy cows, poultry and other animals across the United States. Since April 2024, the U.S. CDCconfirmed 70 human casesthrough genome sequence analysis. In three of
these cases, the amino acid substituti", "highlights": ["Clade 2.3.4.4b of the highly pathogenic avian influenza (HPAI) virus causing outbreaks in wild and domestic birds around the world, continues
to spread in dairy cows, poultry and other animals across the United States. Since April 2024, the U.S. CDCconfirmed 70 human casesthrough genome sequence analysis. In three of these cases, the amino
acid substitution NA-S247N was identified that may slightly reduce susceptibility to the neuraminidase inhibitor oseltamivir in laboratory tests. The CDC also identified a different change in the
polymerase acidic (PA) protein of a virus collected from a recently confirmed human case of H5N1 bird flu in California. The current outbreak validates the unpredictability of HPAI viruses, as the
route of exposure in dairy cows and mode of virus transmission remains unknown. The virus RNA was found at high concentrations in raw milk. Several animal species at dairy and poultry farms, as well
as a growing number of farm workers are affected. Data from the USDA\u2019s Animal and Plant Health Inspection Service show that the viruses in infected cows, other animals and the farm workers are
closely related. A mammalian adaptation marker (E627K) was noted in only one farm worker so far, with nearly all farm workers developing mild eye symptoms, alongside respiratory symptoms. On 11
February 2025, the USDA released specimen data from the first cases of genotype D1.1 detected in dairy cows. Previously, USDA shared data from deceased animals at a Washingtonwildlife sanctuaryand
from raw feline pet food samples that cluster genetically and are of the same genotype B3.13. On 19 March 2025, the CDC released specimen data from the first human case in Ohio. The specimen sequence
belongs to genotype D1.3. Previously, the CDC released data fromthe firsthuman fatalityinvolving a patient from Louisiana that had been exposed to non-commercial backyard poultry and wild birds. The
CDC had also released specimen data collected from farm workers inIowa and Wisconsin with exposure to infected commercial poultry, with the same D1.1 genotype detected in poultry and wild birds, in
human cases in Washington state and notably a severe human case in British Columbia. The latest trees, based on representative subsamples, are dated to 1 April 2025. H5N1 HA subsampled tree US
2025-04-01H5N1 NA subsampled tree US 2025-04-01H5N1 PB2 subsampled tree 2025-04-01 Subsampled phylogenetic trees with focus on recent U.S. H5N1 samples shown for HA, NA and PB2\n(as of 1 April 2025)
back to: GISAID in the News\nResources\n* Commentary on GISAID * GISAID in the News\n* Human Influenza Vaccine Composition\n* In Focus Archive * hCoV-19 Reference Sequences\n* Statements &
Clarifications\nSearch\n* About us\n* Mission\n* History\n* Governance * Scientific Advisory Council\n* Database Technical Group\n* GISAID Compliance Board  ...    * Acknowledgements\n* Imprint /
Privacy\n* Database Features\n* Audacity Instant App * CoVsurver mutations App\n* FluSurver mutations App\n* Submission Tool CLI4\n* Events * Events Calendar\n* Training Workshops\n* New
Publications\n* Collaborations * Arbovirus Researchers Unite\n* Collaboration on H5 Antigenic Cartography * Global Collaboration on H5N8\n* Equine Influenza Collaboration\n* Resources * Commentary on
GISAID\n* GISAID in the News\n* Human Influenza Vaccine Composition  ...    * Help\n* EPI\\_SET Identifier\n* FAQ\n* Get Help with an Issue * Publish with data in GISAID\n* Recover Username or
Password\n* Sitemap * System Requirements\n* Login\n\n\u00a9\u00a92008-2025 Freunde von GISAID e.V. * Imprint / Privacy\n* Terms of Use\n* Open Access"], "published_date": null, "score": null},
{"title": "CDC Confirms First Severe Case of H5N1 Bird Flu in the United States | CDC Newsroom", "url": "https://cdc.gov/media/releases/2024/m1218-h5n1-flu.html", "snippet": "CDC Confirms First Severe
Case of H5N1 Bird Flu in the United States | CDC Newsroom\n\nEspa\u00f1ol\n\n# CDC Confirms First Severe Case of H5N1 Bird Flu in the United States\n\n## Statement\n\nFor immediate release: December
18, 2024\n\nCDC Media Relations\n\n(404) 639-3286\n\nhttps://www.cdc.gov/media/\n\nDecember 18, 2024-- A patient has been hospitalized with a severe case of avian influenza A(H5N1) virus (\"H5N1 bird
flu\") infection in Louisiana. This marks the first instance of severe illness linked to the virus", "highlights": ["Severe Case of H5N1 Bird Flu in the United States\n\n## Statement For immediate
release: December 18, 2024\n\nCDC Media Relations\n\n(404) 639-3286\n\nhttps://www.cdc.gov/media/ December 18, 2024-- A patient has been hospitalized with a severe case of avian influenza A(H5N1)
virus (\"H5N1 bird flu\") infection in Louisiana. This marks the first instance of severe illness linked to the virus in the United States. The case was confirmed by the Centers for Disease Control
and Prevention (CDC) on Friday, December 13. Since April 2024, there have been a total of 61 reported human cases of H5 bird flu reported in the United States. Partial viral genome data of the H5N1
avian influenza virus that infected the patient in Louisiana indicates that the virus belongs to the D1.1 genotype related to other D1.1 viruses recently detected in wild birds and poultry in the
United States and in recent human cases in British Columbia, Canada, and Washington state. This H5N1 bird flu genotype is different than the B3.13 genotype detected in dairy cows, sporadic human cases
in multiple states, and some poultry  ...    the patient in Louisiana are underway at CDC. While an investigation into the source of the infection in Louisiana is ongoing, it has been determined that
the patient had exposure to sick and dead birds in backyard flocks. This is the first case of H5N1 bird flu in the U.S. that has been linked to exposure to a backyard flock. A sporadic case of severe
H5N1 bird flu illness in a person is not unexpected; avian influenza A(H5N1) virus infection has previously been associated with severe human illness in other countries during 2024 and prior years,
including illness resulting in death. No person-to-person spread of H5 bird flu has been detected. This case does not change CDC's overall assessment of the immediate risk to the public's health from
H5N1 bird flu, which remains low. This case underscores that, in addition to affected commercial poultry and dairy operations, wild birds and backyard flocks also can be a source of exposure. People
with work or recreational exposures to infected animals are at higher risk of infection and should follow CDC's recommended precautions when around animals that are infected or potentially infected
with H5N1 avian influenza virus. This means that backyard flock owners, hunters and other bird enthusiasts should also take precautions. The best way to prevent H5 bird flu is to avoid exposure
whenever possible. Infected birds shed avian influenza A  ...    secretions and other bodily fluids (e.g., in unpasteurized cow milk or 'raw milk'). As a general precaution, whenever possible, people
should avoid contact with sick or dead animals, in particular wild  ...    personal protective equipment (PPE).] Wild birds can be infected with avian influenza A viruses even if they  ...    Do not
touch surfaces or materials (e.g., animal litter or bedding material) contaminated with saliva, mucous, or  ...    infection. For more information on H5 bird flu in the U.S. and CDC's response,
including regularly updated case counts, visit the H5 Bird Flu: Current Situation page. ### U.S. DEPARTMENT OF HEALTH AND HUMAN SERVICES Whether diseases start at home or abroad, are curable or
preventable, chronic or acute, or from human activity or deliberate attack, CDC\u2019s world-leading experts protect lives and livelihoods, national security and the U.S. economy by providing timely,
commonsense information, and rapidly identifying and responding to diseases, including outbreaks and illnesses. CDC drives science, public health research, and data innovation in communities across
the country by  ...    Sources Print Share\n\nContent Source:\n\nOffice of Communications (OC)"], "published_date": null, "score": null}]
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "H5N1 human cases US timeline 2025 2026 last confirmed case CDC total count 71"
}
```

### 📋 Result

```
{"query": "H5N1 human cases US timeline 2025 2026 last confirmed case CDC total count 71", "results": [{"title": "A(H5) Bird Flu: Current Situation | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-
flu/situation-summary/index.html", "snippet": "What to know\n- A(H5) bird flu is widespread in wild birds worldwide and is causing outbreaks in poultry and U.S. dairy cows with sporadic human cases in
U.S. dairy and poultry workers.\n- While the current public health risk is low, CDC is watching the situation carefully and working with states to monitor people with animal exposures.\n- CDC is using
its flu surveillance systems to monitor for A(H5) bird flu activity in people.\n![H5N1 Bird Flu How is it Spreading?](/bird-flu/media/images/2024/07/", "api_data": null, "hint": null}, {"title":
"Updated H5N1 Report: 70 Human Cases in the US as of April 2025 | Contagion Live", "url": "https://www.contagionlive.com/view/updated-h5n1-report-70-human-cases-in-the-us-as-of-april-2025", "snippet":
null, "api_data": null, "hint": null}, {"title": "Global Human Cases with Influenza A(H5N1), 1997-2026 | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/php/surveillance/chart-epi-curve-
ah5n1.html", "snippet": "What to know\nThis graph shows all human infections with HPAI A(H5N1) bird flu virus reported to the World Health Organization (WHO), since the first human cases in
1997.\nBackground\nThis graph shows all human infections with HPAI A(H5N1) bird flu virus reported to the [World Health Organization](https://www.who.int/teams/global-influenza-programme/avian-
influenza) (WHO), since the first human cases in 1997.\nA(H5N1) bird flu viruses first emerged in southern China in 1996. Those viruses caused lar", "api_data": null, "hint": null}, {"title": "Human
infections with highly pathogenic avian influenza A(H5N1) viruses in the United States from March 2024 to May 2025 - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12477757/", "snippet":
"Abstract\nBetween March 2024 and October 2024, 46 human cases of highly pathogenic avian influenza (HPAI) A(H5N1) had been detected in the United States. The persistent panzootic spread of HPAI
A(H5N1) viruses and continued detection of human cases presents an ongoing threat to public health. Between November 2024 and May 2025, an additional 24 cases have been reported for a total of 70
human cases of HPAI A(H5N1): 41 were exposed to dairy cows, 24 to commercial poultry, 2 to backyard poultry, an", "api_data": null, "hint": null}, {"title": "A(H5) Bird Flu Surveillance and Human
Monitoring | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/h5-monitoring/index.html", "snippet": "At a glance\nOverview\nA(H5) Bird Flu Surveillance in U.S.\nOn July 7, 2025, CDC streamlined
A(H5) bird flu updates with routine influenza data updates and updated reporting cadences to reflect the current public health situation. As such, several changes were made to this page:\n- Data on
the number of people monitored and tested for bird flu, as well as animal and epidemiologically linked human cases are reported monthly.\n- Data that are reported in
CDC's\n[FluView](https://www.cdc.gov/fluview/inde", "api_data": null, "hint": null}, {"title": "First H5 Bird Flu Death Reported in United States | CDC Newsroom", "url":
"https://www.cdc.gov/media/releases/2025/m0106-h5-birdflu-death.html", "snippet": "Statement\nJanuary 6, 2025 -- CDC is saddened by Louisiana's report that a person previously hospitalized with severe
avian influenza A(H5N1) illness (\"H5N1 bird flu\") has passed away. While tragic, a death from H5N1 bird flu in the United States is not unexpected because of the known potential for infection with
these viruses to cause severe illness and death. As of January 6, 2025, there have been 66 confirmed human cases of H5N1 bird flu in the United States since 2024 and 67 since 2022. This ", "api_data":
null, "hint": null}, {"title": "Global Summary of Recent Human Cases of H5N1 Bird Flu | Bird Flu | CDC", "url": "https://www.cdc.gov/bird-flu/spotlights/h5n1-summary-08042025.html", "snippet": "At a
glance\n- Between January 1 and August 4, 2025, 26 human infections with avian influenza A(H5N1) viruses (H5 bird flu) have been detected globally, of which 23 were identified in 7 countries outside
of the United States, including 11 infections that resulted in death.\n- The three cases in the United States were previously reported, and there have been no cases reported in the United States since
mid-February 2025.\n- The 11 deaths occurred in Cambodia (8), India (2), and Mexico (1). All of th", "api_data": null, "hint": null}, {"title": "Current Situation: H5N1 Bird Flu in People | Bird Flu |
CDC", "url": "https://www.cdc.gov/bird-flu/situation-summary/inhumans.html", "snippet": "Highlights\n- Sporadic avian influenza A(H5N1) virus infections (\"H5N1 Bird Flu\") in people have been
reported worldwide since 1997.\n- Highly pathogenic avian influenza A(H5N1) viruses are widespread in wild birds worldwide, have caused poultry outbreaks in many countries, and infected other kinds of
animals. H5N1 bird flu has caused outbreaks in U.S. poultry and dairy cows.\n- In the United States, sporadic human infections with A(H5N1) viruses have occurred since 2022 mostly after direct or
clos", "api_data": null, "hint": null}, {"title": "Weekly US Influenza Surveillance Report: Key Updates for Week 49, ending December 6, 2025 | FluView | CDC", "url":
"https://www.cdc.gov/fluview/surveillance/2025-week-49.html", "snippet": "Key points\nSummary\nViruses\nIllness\nAll data are preliminary and may change as more reports are received.\nDirectional
arrows indicate changes between the current week and the previous week. [Additional information](https://www.cdc.gov/fluview/surveillance/2025-week-49.html#cdc_data_surveillance_section_5-additional-
national-and-international-influenza-surveillance-information) on the arrows can be found at the bottom of this page.\nA description of the CDC influenza surveillance system, including ", "api_data":
null, "hint": null}, {"title": "Novel H5N1 Bird Flu Outbreak - American Academy of Ophthalmology", "url": "https://www.aao.org/education/bird-flu", "snippet": "![bird-flu-flock-chicken.png bird-flu-
flock-chicken](/image.axd?id=096a30e6-8f85-4c77-b374-ae5cddbc0b11&t=638527619196900000)\nKey Points for the Ophthalmologist\n- Be alert to H5N1 as a cause of conjunctivitis when a patient presents
with a history of exposure to sick birds, dairy cows or livestock. Multiple human H5N1 infections, presumably transmitted from sick cows and poultry, presented with conjunctivitis as the sole clinical
sign and symptom. Other symptoms included tearing, fever, and chil", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.cdc.gov/bird-flu/h5-monitoring/index.html",
  "prompt": "What is the most recent data on H5N1 human cases in the US? How many total confirmed cases? When was the last new case reported? Any cases in 2026? What is the current monitoring status?"
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/bird-flu/h5-monitoring/index.html", "content": "Based on the provided content, here's what I can extract:\n\n**Data Limitations:**\nThe content does not provide specific
numbers of confirmed H5N1 human cases or dates of individual case reports. It only provides monitoring statistics and indicates that case counts are available elsewhere.\n\n**Monitoring Data (as of
February 28, 2026):**\n- **Since February 2022**: At least 32,600 people monitored; at least 1,320 people tested\n- **September 28, 2025 - February 28, 2026**: At least 3,500 people monitored; at
least 130 people tested\n\n**2026 Cases:**\nThe document references data through February 28, 2026, indicating monitoring continued into 2026, but does not specify if any new cases occurred in
2026.\n\n**Current Monitoring Status:**\n- CDC and state/local health departments continue monitoring people exposed to infected animals for 10 days after exposure\n- As of July 7, 2025, CDC
streamlined reporting: monthly updates for monitoring/testing data and animal-linked human cases\n- Updates occur on the first Friday of every month\n\n**For Actual Case Counts:**\nThe document
explicitly states to visit the \"A(H5) Bird Flu: Current Situation\" page for latest case counts.\n\n**Relevant links:**\n- [A(H5) Bird Flu: Current Situation](https://www.cdc.gov/bird-flu/situation-
summary/index.html#human-cases) - for latest case counts\n- [FluView](https://www.cdc.gov/fluview/index.html) - for surveillance data\n- [National Wastewater Surveillance System
(NWSS)](https://www.cdc.gov/nwss/rv/wwd-h5.html) - for wastewater monitoring\n- [Emergency Department Visit Data](https://data.cdc.gov/Public-Health-Surveillance/NSSP-Emergency-Department-Visit-
Trajectories-by-St/rdmq-nq56/about_data)", "title": "A(H5) Bird Flu Surveillance and Human Monitoring"}
```

## 💭 Thinking

Now I have a much clearer picture. Let me synthesize the key data points:

1. **Total CDC count**: 71 confirmed human H5 cases in the US since 2024 (as of the current CDC page)
2. **Timeline of the 71st case**: The WHO was notified on November 15, 2025 of the 71st case - a patient in Washington state with H5N5 (first globally reported H5N5 case). This was the first US case since February 2025. The patient subsequently died.
3. **Rate of cases**: 
   - The outbreak accelerated early on with 46 cases between March and October 2024, then slowed to 24 additional cases through May 2025
   - After a nine-month gap with no reported cases, the November 2025 case emerged, and surveillance data through January 2026 shows no further activity or unusual influenza patterns in the population
   - As of late January 2026, there haven't been new human cases globally or in dairy cattle since mid-December 2025, though H5N1 remains entrenched in animal populations across multiple states with ongoing poultry outbreaks, wild bird die-offs, and documented infections in marine mammals
   - Thousands of people have been monitored and tested since the Washington state dairy outbreak, but the 71 confirmed human cases as of mid-March 2026 represents the current baseline

Now I'm weighing whether a new case will emerge by the end of April. The virus is still circulating widely in poultry and wild birds with massive ongoing outbreaks, and workers continue to have exposure risk on farms and dairy operations. The historical pace was quite rapid—70 cases accumulated over about 15 months—and the question only needs one new case to occur. On the other hand, there's been a notable slowdown in human infections recently, with no new cases confirmed since mid-December despite continued animal circulation. Looking at the clustering pattern, cases were concentrated early on with a sharp decline, and now we're in a much slower phase where we'd expect roughly 1 case every 4-5 months. For a 45-day window, I need to calculate the probability using a Poisson model with that reduced rate.

But there are several factors that could shift this estimate upward: the ongoing poultry outbreak maintains constant exposure, spring migration is bringing more wild birds into circulation, the virus remains widespread in animal populations, and the CDC tally could increase from previously pending cases being added to their count rather than entirely new infections.

Looking at the CDC's case breakdown by state, I'm trying to reconcile whether those 14 Washington farmworkers mentioned in the article are already included in the official tally, since the numbers don't quite add up—the listed states total around 56 cases, leaving roughly 14-15 unaccounted for, which could represent other states or potentially those Washington cases.

The CIDRAP article mentions 70 confirmed cases through July 2025, then the November Washington H5N5 case brought it to 71, so I'm now considering whether the ongoing poultry outbreaks during this window could lead to additional confirmed human infections. I'm also noticing that CDC monitoring data shows at least 130 people were tested for novel influenza A between late September 2025 and late February 2026, which suggests active surveillance is happening—though if anyone tested positive, they'd likely already be counted.

Looking at the case timeline more carefully, there's been a striking pattern: multiple cases per week in late 2024, a few more in early 2025, then a seven-month quiet stretch through October, one case in November, and another three-month lull through March 2026. The dairy outbreak seems somewhat contained now, worker protections have improved, and poultry exposure tends to produce cases more sporadically. That said, the massive new poultry outbreaks starting in early 2026 across Pennsylvania, Wisconsin, and Colorado are creating fresh exposure risks that could shift this pattern, especially as spring migration season approaches.

Weighing the competing factors: cases have been extremely sparse recently—roughly one every four to ten months during the slowdown—but the ongoing animal circulation and spring migration window create meaningful opportunity. Only a single new case is needed to move the needle, and there's also the possibility of a retroactively confirmed case being added to the CDC tally. Given the current lull but persistent animal-to-human transmission pathways, I'm settling on a probability around 30-45% for at least one new confirmed case within the 45-day window. That's roughly 1 case per 13 months, or about 0.077 cases per month.

P(at least 1 in 1.5 months) = 1 - exp(-0.077 * 1.5) = 1 - exp(-0.116) ≈ 10.9%

But the rate could be accelerating given the poultry outbreaks and spring migration patterns in early 2026. During peak exposure periods, the rate was substantially higher. I'm estimating the current rate is somewhere between the baseline and moderate scenarios, around 0.2-0.5 cases per month:

P(at 0.2/month) = 1 - exp(-0.3) ≈ 26%
P(at 0.5/month) = 1 - exp(-0.75) ≈ 53%

Let me reconsider the timing issue. The resolution criteria asks about cases confirmed between March 16 and April 30, but there's a lag between infection and when cases get added to the CDC tally—exposure, symptoms, testing, lab confirmation, and then the official count update can take weeks. Though the January 2025 update did streamline this for states with 3+ confirmed cases. The key question is whether the tally needs to go from 71 on March 16 to at least 72 by April 30, and whether any already-reported but unconfirmed cases could be added to that count. Washington state preliminary case from November 2025 was already confirmed (as H5N5) and counted as the 71st case. I don't see evidence of any pending cases.

Given:
1. No cases for 4+ months (since November 2025)
2. But massive ongoing poultry outbreaks creating exposure
3. Spring migration increasing wild bird circulation
4. 45-day window
5. CDC surveillance still active but possibly reduced
6. Historical slow-period rate: ~1 case per 13 months

I think my estimate should be around 25-40%. The massive poultry outbreaks are significant - they're among the largest in recent history. But the slowdown in human cases has been dramatic, suggesting either improved worker protections, reduced testing/surveillance, or both.

The DOGE cuts to CDC may have reduced surveillance capacity, which means fewer confirmed cases overall. But I need to weigh this against the scale of current animal outbreaks - Pennsylvania's 7.6 million birds, Wisconsin's million-plus culled in a single incident, plus major commercial farms in Colorado and Ohio, and over a thousand dead wild birds in New Jersey. During the 2024 peak, poultry and dairy workers were getting infected at a moderate rate, so the question becomes whether current protections are holding up against these massive exposure events. Given the 45-day window and the very large outbreak scale, I'm settling on around 35% probability, though the recent case rate has been remarkably low. I'm trying to piece together the timeline more carefully. The CDC August 2025 summary mentions 3 US cases that were already reported between January and August, which were likely from early 2025, so they wouldn't be new additions to the count. Looking at the progression, it seems like there were cases through October, and I need to map out exactly when each one occurred to understand how we got to the current total of 71. Given the current outbreak severity with massive poultry cases and spring migration, I'm adjusting my rate estimate upward to 0.2-0.3 cases per month, which puts the probability of at least one case in the next 1.5 months somewhere in the 25-35% range—I'll settle on around 30%. But now I'm second-guessing whether the 71st case actually counts, since it was A(H5N5) rather than A(H5N1), and the question specifically asks about the H5N1 tally. The resolution criteria actually references the A(H5) page which tracks all H5 subtypes, not just H5N1, so any H5 case would count toward the tally. I'm settling on about 30% as my estimate—the massive poultry outbreaks and spring migration push toward YES, but the extremely low human case rate over the past year and the short 45-day window push toward NO. I should check if there are any recent presumptive or pending cases that might already be in the pipeline, since some of those Washington farmworkers from 2022 onward might have been confirmed by the CDC. → moderate evidence for NO. Looking at the most recent data more carefully, the Medium article from late January and CDC surveillance through January 31st both confirm no new cases since mid-December 2025, which significantly strengthens the case against an outbreak. Given roughly one case per year during this quiet period and only a 1.5-month window from mid-March to end of April, that puts the baseline around 12-13%, though I'm adjusting upward somewhat for the ongoing massive poultry outbreaks creating continued exposure risk.

During the peak period last year, poultry-related cases occurred at roughly 2 per month, and while the dairy situation has stabilized, the poultry situation is actually intensifying in some areas right now.

The fact that we've seen zero cases in the last four months despite massive ongoing poultry outbreaks suggests either improved worker protections, reduced surveillance, or just random variation. I'm settling on 28% as my estimate, though I should probably cross-check this against prediction markets to see if there's additional information I'm missing.

## 💬 Response

Now I have a comprehensive picture. Let me check prediction markets and do some calculations.

## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "query": "H5N1 bird flu human cases United States"
}
```

### 📋 Result

```
{"markets": [], "query": "H5N1 bird flu human cases United States"}
```

## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "H5N1 human case CDC 2026"
}
```

### 📋 Result

```
{"markets": [], "query": "H5N1 human case CDC 2026"}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.cdc.gov/bird-flu/spotlights/h5n1-summary-08042025.html",
  "prompt": "What is the summary about US H5N1 cases? How many cases in 2025? When was the last US case reported? What is the current situation?"
}
```

### 📋 Result

```
{"url": "https://www.cdc.gov/bird-flu/spotlights/h5n1-summary-08042025.html", "content": "## Summary of US H5N1 Cases\n\n**2025 Cases:** 3 cases total in the United States\n\n**Last Case Reported:**
Mid-February 2025 (no cases reported since then)\n\n**Current Situation:**\n- All 3 US cases were previously reported (no new cases)\n- The health risk to the U.S. public remains **low**\n- No person-
to-person spread was identified\n- The US experienced 70 human cases during 2024 and early 2025 combined (per the overview section)\n- The H5N1 virus clade circulating in US wild birds, poultry, and
dairy cattle is **2.3.4.4b**\n\n**Relevant links:**\n- [US H5N1 case tracking (GIS CDC Grasp FluView)](https://gis.cdc.gov/grasp/fluview/Novel_Influenza.html)", "title": "Global Summary of Recent
Human Cases of H5N1 Bird Flu"}
```

## 💭 Thinking

Now I have an even clearer picture. Let me summarize the timeline:

**2024:**
- March - October 2024: 46 cases (dairy cow outbreak mainly)
- November - December 2024: Several more (bringing total to ~61 by Dec 18, 2024)

**2025:**
- January 2025: More cases (66 total by Jan 6, 2025)
- February 2025: Last cases reported (one in Ohio Feb 12, one in Wyoming Feb 14 - total reached 70)
- March - October 2025: No new cases (long gap)


- November 2025: A resurgence with case #71 (H5N5 in Washington state, fatal)
- December 2025 - March 2026: Another gap with no new cases

The CDC's August 2025 statement confirmed no cases since mid-February, but then that November case broke the silence. Now I'm looking at the question window of March 16 - April 30, 2026, which falls right after this second gap ended.

Using the base rate from the slow period gives me roughly 11%, but I need to account for several factors pushing this higher: the massive ongoing poultry outbreaks creating sustained exposure, spring migration season ramping up, and the fact that only one case is needed. On the other hand, better worker awareness and PPE use, plus possible reduced surveillance efforts, would push it lower. Weighing these factors, I'm settling on something in the 20-30% range, with the poultry situation being the dominant driver.

I don't see any prediction markets covering this specific scenario, so I'll move forward with my estimate of around 25%.

## 💬 Response

No prediction markets found for this specific question. Let me now run a quantitative analysis.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom scipy import stats\n\n# Historical data: US H5N1/H5 human case timeline\n# Peak period: March 2024 - February 2025 (~12 months): 70 cases\n# Slow period: February 2025 - March 2026 (~13 months): 1 case (November 2025)\n\n# The question window: March 16 - April 30, 2026 = 45 days = 1.5 months\n\n# Model 1: Based on slow period rate\nslow_rate_per_month = 1 / 13  # 1 case in 13 months\np_at_least_1_slow = 1 - np.exp(-slow_rate_per_month * 1.5)\nprint(f\"Model 1 (slow period rate: {slow_rate_per_month:.4f}/month):\")\nprint(f\"  P(\u22651 in 45 days) = {p_at_least_1_slow:.4f} = {p_at_least_1_slow*100:.1f}%\")\n\n# Model 2: Overall rate since March 2024\n# 71 cases in ~24 months\noverall_rate = 71 / 24\np_at_least_1_overall = 1 - np.exp(-overall_rate * 1.5)\nprint(f\"\\nModel 2 (overall rate: {overall_rate:.2f}/month):\")\nprint(f\"  P(\u22651 in 45 days) = {p_at_least_1_overall:.4f} = {p_at_least_1_overall*100:.1f}%\")\n\n# Model 3: Current regime - weighted toward slow period\n# Given the clear regime change (dairy outbreak contained), \n# the slow period rate is more relevant but with some uplift for current poultry outbreaks\n# Poultry-related cases were roughly 24/70 of total during peak = 34%\n# Poultry-related rate during peak: 24 cases / 12 months = 2/month\n# But during slow period, despite ongoing poultry outbreaks, rate has been near 0\n# Current poultry outbreaks are very large, so some elevation is warranted\n\n# Let's model with different rate assumptions\nrates = [0.077, 0.15, 0.25, 0.35, 0.5]\nprint(\"\\nSensitivity analysis:\")\nprint(f\"{'Rate/month':>12} | {'P(\u22651 in 45 days)':>18}\")\nprint(\"-\" * 35)\nfor r in rates:\n    p = 1 - np.exp(-r * 1.5)\n    print(f\"{r:>12.3f} | {p:>17.1%}\")\n\n# Monte Carlo simulation with regime switching\n# Model: with probability p_burst, we're in a \"burst\" regime with higher rate\n# Otherwise we're in the slow regime\nn_sims = 100000\np_burst = 0.10  # 10% chance we're entering a new burst period\nburst_rate_monthly = 2.0  # Similar to poultry-exposure peak\nquiet_rate_monthly = 0.15  # Slightly elevated from observed slow rate due to current outbreaks\n\ncases_sim = np.zeros(n_sims)\nfor i in range(n_sims):\n    if np.random.random() < p_burst:\n        rate = burst_rate_monthly\n    else:\n        rate = quiet_rate_monthly\n    cases_sim[i] = np.random.poisson(rate * 1.5)\n\np_at_least_1_mc = np.mean(cases_sim >= 1)\nprint(f\"\\nMonte Carlo (regime-switching):\")\nprint(f\"  P(burst regime) = {p_burst*100:.0f}%\")\nprint(f\"  Burst rate = {burst_rate_monthly}/month, Quiet rate = {quiet_rate_monthly}/month\")\nprint(f\"  P(\u22651 in 45 days) = {p_at_least_1_mc:.4f} = {p_at_least_1_mc*100:.1f}%\")\n\n# Also factor in: the CDC tally could increase from a retroactively confirmed case\n# Or from a case that's already been detected but not yet added to the tally\np_retroactive = 0.03  # Small chance of a pending case being added\n\n# Combined probability\np_combined = 1 - (1 - p_at_least_1_mc) * (1 - p_retroactive)\nprint(f\"\\nCombined (including retroactive addition): {p_combined:.4f} = {p_combined*100:.1f}%\")\n\n# Summary\nprint(\"\\n=== SUMMARY ===\")\nprint(f\"Slow period base rate model: {p_at_least_1_slow*100:.1f}%\")\nprint(f\"Regime-switching MC model: {p_at_least_1_mc*100:.1f}%\")\nprint(f\"Combined estimate: {p_combined*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Model 1 (slow period rate: 0.0769/month):\n  P(\u22651 in 45 days) = 0.1090 = 10.9%\n\nModel 2 (overall rate: 2.96/month):\n  P(\u22651 in 45 days) = 0.9882 =
98.8%\n\nSensitivity analysis:\n  Rate/month |   P(\u22651 in 45 days)\n-----------------------------------\n       0.077 |             10.9%\n       0.150 |             20.1%\n       0.250 |
31.3%\n       0.350 |             40.8%\n       0.500 |             52.8%\n\nMonte Carlo (regime-switching):\n  P(burst regime) = 10%\n  Burst rate = 2.0/month, Quiet rate = 0.15/month\n  P(\u22651 in
45 days) = 0.2762 = 27.6%\n\nCombined (including retroactive addition): 0.2979 = 29.8%\n\n=== SUMMARY ===\nSlow period base rate model: 10.9%\nRegime-switching MC model: 27.6%\nCombined estimate:
29.8%\n", "stderr": "", "duration_ms": 1411}
```

## 💭 Thinking

Now let me do my reflection and then provide my final forecast. Let me synthesize all the evidence.

Key facts:
1. CDC official tally: 71 cases as of March 16, 2026 (baseline)
2. Last case: November 2025 (H5N5 in Washington state) - ~4 months ago
3. Slow period rate: ~1 case per 13 months since February 2025
4. Massive ongoing poultry outbreaks in early 2026 (PA, WI, CO, OH, NJ)
5. Spring migration season (March-May) increases wild bird circulation


6. No prediction market data available, and CDC surveillance through January 2026 shows no unusual influenza activity

My quantitative models are pointing in different directions—the pure slow-period rate gives me around 11%, but the regime-switching model pushes higher to 28%, and combining that with retroactive adjustments gets me to about 30%. I'm settling on 25% as my estimate, which feels slightly conservative compared to the regime-switching model since the quiet rate I'm using already factors in elevated poultry risk relative to what we've actually observed.

Now I'm moving into reflection on this analysis.

## 💬 Response

Now let me do my reflection checkpoint.
