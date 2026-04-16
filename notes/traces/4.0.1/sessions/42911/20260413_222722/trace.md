# Reasoning Log: Will an AdaptyvBio protein-binder competition have >75% of tested designs be classified as binders before 2030?

*Generated: 2026-04-13T22:31:49.015774+00:00*


## 💭 Thinking

Let me analyze this forecasting question about whether an AdaptyvBio protein-binder competition will have >75% of tested designs classified as binders before 2030.

Let me break this down:

1. **Resolution criteria**: Before 2030, an AdaptyvBio competition must have >75% of experimentally tested computationally generated designs classified as binders
2. **Current state**: The most recent competition (Nipah Virus) had a 9.6% success rate (99/1026 binders)
3. **Time horizon**: ~3.75 years remaining (April 2026 to January 2030)


4. **Fine print**: Only novel designs count

Now I need to look into the trajectory of computational protein design and how AdaptyvBio's competitions have evolved to assess whether we could realistically see a jump from ~10% success to >75% in the remaining timeframe.

## 🔧 Tool: TodoWrite


```json
{
  "todos": [
    {
      "content": "Parse resolution criteria and understand the question",
      "status": "completed",
      "activeForm": "Parsing resolution criteria"
    },
    {
      "content": "Research AdaptyvBio competition history and success rates",
      "status": "in_progress",
      "activeForm": "Researching AdaptyvBio competition history"
    },
    {
      "content": "Research state of computational protein design field",
      "status": "pending",
      "activeForm": "Researching protein design field"
    },
    {
      "content": "Check prediction markets and related questions",
      "status": "pending",
      "activeForm": "Checking prediction markets"
    },
    {
      "content": "Run reflection and produce final forecast",
      "status": "pending",
      "activeForm": "Running reflection and producing forecast"
    }
  ]
}
```

### 📋 Result

```
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42911
  ]
}
```

### 📋 Result

```
{"post_id": 42911, "title": "Will an AdaptyvBio protein-binder competition have >75% of tested designs be classified as binders before 2030?", "type": "binary", "url":
"https://www.metaculus.com/questions/42911", "background_info": "Protein-binders are proteins designed to [attach](https://docs.adaptyvbio.com/docs/experiment-types/binding) to a specific target
molecule, often with high specificity and strength. They are generally used in biotechnology and medicine to block interactions, detect biomarkers, or deliver therapeutic
effects.\n\n[AdaptyvBio](https://www.adaptyvbio.com/) is a biotechnology company focused on experimentally testing computationally generated protein designs. As of March 2026, the company has run 3
competitions in which submitted designs were screened and selectively tested for binding affinity.&#x20;\n\nThe [most recent](https://www.adaptyvbio.com/blog/nipah-submissions/) competition focused on
the Nipah Virus and received over 10k submissions. Of the 1026 designs experimentally tested, 99 designs were classified as binders indicating a [success
rate](https://proteinbase.com/collections/nipah-binder-competition-results) of 9.6%.", "resolution_criteria": "This question will resolve as Yes if, before 2030, an AdaptyvBio protein-binder
competition is conducted in which >75% of the computationally generated designs selected for experimental testing are classified as binders.", "fine_print": "To qualify, the competition must only test
novel designs.", "num_forecasters": 2, "community_prediction": null}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "AdaptyvBio protein binder competition results history success rate"
}
```

### 📋 Result

```
{"query": "AdaptyvBio protein binder competition results history success rate", "results": [{"title": "Protein Design Competition - RESULTS - Adaptyv Bio", "url":
"https://adaptyvbio.substack.com/p/protein-design-competition-results", "snippet": "Protein Design Competition - RESULTS\nThe long awaited results are here -- and they don\u2019t disappoint!\nThe long
awaited results are here -- and they don\u2019t disappoint!\n\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400!\n\ud83e\uddec Out of those 400 proteins, 378 expressed
(95% expression rate!)\n\ud83d\ude80 Out of those 378 expressed proteins, 53 did successfully bind the target protein EGFR (that\u2019s a 14% success rate, more than 5x of the success rate of the
previous round just 2 months ago!)\n\ud83d\udcaa Th", "api_data": null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url":
"https://www.adaptyvbio.com/blog/po104/", "snippet": "We released the [results of our second Protein Design Competition](https://foundry.adaptyvbio.com/competition) just about 2 weeks ago\u2026 and
they were great!\nA quick recap of what this was all about:\nAnd the designers did not disappoint. In our previous analysis [here](https://www.adaptyvbio.com/blog/po103), we went through how the meta
shifted from the first round, in particular how close the race was in the last few days as some submitters tried to increase their chances of landing in the top 10", "api_data": null, "hint": null},
{"title": "Adaptyv Bio", "url": "https://www.adaptyvbio.com/blog", "snippet": "For our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were
most widely adopted, and highlight several noteworthy and creative community contributions. Plus, we opened a prediction market on Manifold for this competition so you can bet on hit rates, best
performing models, and more\nTong Chen and colleagues from Pranam Chatterjee\u2019s Programmable Biology Group at the University of Pennsylvania are showcasing their most recent model MOG-DFM ",
"api_data": null, "hint": null}, {"title": "Introducing BenchBB and the community paper of the Protein Design Competition", "url": "https://www.adaptyvbio.com/blog/benchbb/", "snippet": "Introducing
BenchBB and the community paper of the Protein Design Competition\nlaunch\n/Article\n/TL;DR\n-We wrote a community paper about our Protein Design Competition, teaming up with your favourite protein
designers from both rounds.\n-We aimed to explore the competition data in as many ways as we could, take stock of the state of the field, what SotAs have been established across the rounds, and which
metric is most predictive of binding and expression.\nThe community paper after the Protein Desi", "api_data": null, "hint": null}, {"title": "Protein Optimization 102: Lessons from the protein design
competition", "url": "https://www.adaptyvbio.com/blog/po102/", "snippet": "In our [last ](https://www.adaptyvbio.com/blog/po101)[blog](https://www.adaptyvbio.com/blog/po101) post, we looked at the
different ways you can optimize a protein for a given task using machine learning models.\nWe made the distinction between
[fixed](https://www.adaptyvbio.com/blog/po101#:~:text=Supplementary%20-%20Fixed%20model%20optimization) and [sequential](https://www.adaptyvbio.com/blog/po101#:~:text=sequentially-optimized%20models)
model optimization and further split the latter into [mo", "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein
design", "url": "https://www.adaptyvbio.com/blog/nipah-submissions/", "snippet": "After a busy few weeks with over 680 protein designers submitting their best binder designs against the surface
glycoprotein of the Nipah virus, the submissions and community vote doors have closed and we are waiting in anticipation for the experimental results to arrive. In the meantime, we want to highlight
some interesting new insights and cool protein structures that we have gathered during the course of this competition.\nLet\u2019s start with a quick recap: Nipah is one of the deadliest viruses ",
"api_data": null, "hint": null}, {"title": "8x improvement in EGFR binding affinity: winning the Adaptyv Bio protein design competition | Cradle", "url": "https://www.cradle.bio/blog/adaptyv-protein-
design-competition", "snippet": "![](https://framerusercontent.com/images/4UdCTbTNeeNo0TyNDeXL0GNKa1k.jpg?width=2400&height=1280)\n8x improvement in EGFR binding affinity: winning the Adaptyv Bio
protein design competition\n130 teams competed in Adaptyv Bio\u2019s protein design competition to create novel EGFR-binding proteins. Cradle's platform achieved first place with a binding affinity of
1.21nM, which is 8.2 times stronger than Merck's commercial antibody Cetuximab*.\nWe are proud to announce that Cradle\u2019s submission [took the to", "api_data": null, "hint": null}, {"title":
"Protein Optimization 103: Racing to the Top 100", "url": "https://www.adaptyvbio.com/blog/po103/", "snippet": "In case you missed out, we\u2019re running a [second round of the EGFR binder design
competition](https://design.adaptyvbio.com/). This was in partnership with [Polaris](https://protein.polarishub.io/) and [Dimension Capital](https://www.dimensioncap.com/), and with the help of
[Modal](https://modal.com/), who offered $500 of GPU credits, and [Twist](https://twistbioscience.com/), who helped us cover the costs for DNA synthesis!\nThe rules stayed more or less the same:
participants were tasked with de", "api_data": null, "hint": null}, {"title": "Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition | bioRxiv", "url":
"https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2", "snippet": null, "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? + Prediction
markets for protein design", "url": "https://adaptyvbio.substack.com/p/what-happened-in-the-nipah-protein", "snippet": "What happened in the Nipah Protein Design Competition so far? + Prediction
markets for protein design\nFor our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were most widely adopted, and highlight several noteworthy
and creative community cont\n\u2022 We hosted our third installment of the Protein Design Competition, this time challenging participants to design a binder against the Nipah virus
glycoprotein.\n\u2022 The response was incredible: Over ", "api_data": null, "hint": null}]}
```

```json
{
  "query": "AdaptyvBio protein binder competition results success rate 2024 2025 2026"
}
```

### 📋 Result

```
[{"title": "Adaptyv Competition Results: AI Protein Design Tools Compared", "url": "https://www.linkedin.com/posts/deniz-kavi_newest-adaptyv-competition-results-are-out-
activity-7420133202150912000-pL15", "snippet": "30% hit rate). Want ~100 designs? top ~10% is ~2\u00d7 baseline hit rate. Binding does not mean function. Only 19 designs have neutralization
annotations, and while the full neutralizers trend tighter, epitope/geometry is the primary factor. Congrats to Julian Englert and the team at Adaptyv on their hard work organizing and running the
experiments. Stay tuned for deeper analysis of the results in the coming days! I'm excited to see what new methods will be published alongside the competition, the to", "highlights": ["hit rate). Want
~100 designs? top ~10% is ~2\u00d7 baseline hit rate. Binding does not mean function. Only 19 designs   ...    through our web interface or programmatic API. | 16 comments on LinkedIn\" Adaptyv
Competition Results: AI Protein Design Tools Compared | Deniz Kavi posted on the topic | LinkedIn   ...    Newest Adaptyv Competition results are out! Let's see how the state of the art AI protein
design tools faired. The task was to design a protein to neutralize Nipah virus (PDB: 2VSM), lots of entrants and new protocols.. The Baker Lab's RFdiffusion/RFantibody remains a contender, with 4 of
the top 10 using the structure-based design method along with   ...    well with the wet lab validation as well. He got number 8 and 17 of the top hits!
\ud835\ude17\ud835\ude33\ud835\ude30\ud835\ude35\ud835\ude30\ud835\ude24\ud835\ude30\ud835\ude2d\ud835\ude34
\ud835\ude30\ud835\ude37\ud835\ude26\ud835\ude33\ud835\ude37\ud835\ude2a\ud835\ude26\ud835\ude38 BoltzGen has a lot of entries (n=163) but a low hit rate around 1.23 percent in this dataset. BindCraft
has moderate volume (n=88) with a hit rate around 5.68 percent. Edit: seen others claim 25-30% hit rates, likely a difference in how we split the tool types will update momentarily. RFdiffusion (n=42)
shows the highest hit rate among the main buckets shown here around 21.4 percent ProteinMPNN (n=29) is close around 20.7 percent. Escalante's Mosaic (n=9) has the highest hit rate at 88.8 percent. I
actually would not necessarily use these datapoints as limitations of the tools themselves, as the quality of the binders would meaningfully differ depending on the team submitting.
\ud835\ude14\ud835\ude26\ud835\ude35\ud835\ude33\ud835\ude2a\ud835\ude24\ud835\ude34 Boltz IPSAE seems to reasonably predictive of binding, although primarily as a filter and not a predictor:
Selecting top 1% by min_ipsae: 63.6% binders   ...    can be a legitimate hard filter for evaluating designs. I would suspect this is true of AF2 min_ipsae as well. Want ~25 designs? pick very top
tail (this dataset suggests you can get >30% hit rate). Want ~100 designs? top ~10% is ~2\u00d7 baseline hit rate. Binding does not mean function. Only 19 designs have neutralization annotations, and
while the full neutralizers trend tighter, epitope/geometry is the primary factor. Congrats to Julian Englert and the team at Adaptyv   ...    days! I'm excited to see what new methods will be
published alongside the competition, the top three protocols have not   ...    16 Comments\n\nLike Comment\n\nDeniz Kavi 1mo\n\n- Report this comment Learn more:
https://proteinbase.com/competitions/adaptyv-nipah-competition\n\nLike\n\nReply 2 Reactions 3 Reactions   ...    Like\n\nReply 1 Reaction\n\nRoland Dunbrack 1mo\n\n- Report this comment Results from
Adaptyv's NIPAH virus protein design competition are out. ipsae_min did a good job at filtering binders from non-binders. From Deniz Kavi's post: \"Selecting top 1% by min_ipsae: 63.6% binders (7/11)
Top 0.5%: 83.3% binders (5/6) Top 10%: 18.4% binders (19/103) Among already-binding designs, these scores don\u2019t strongly correlate with KD (it's better at \u201cbinder vs not\u201d than
\u201cbest binder\u201d).\" A recent paper by Caleb Lareau showed that ipsae_max (default   ...    Very interesting results on the AI protein design tools SOTA. The Rosetta team heads the pack. We are
trying to perfect   ...    and an expert to choose and tweak the final list of candidates. If in some cases you can get a 20% success rate and you   ...    Deniz Kavi\n\nCEO at Tamarind Bio (YC W24) |
We're hiring!\n\n1mo Edited Newest Adaptyv Competition results are out! Let's see how the state of the art AI protein design tools faired. The task was to design a protein to neutralize  Nipah virus
(PDB: 2VSM), lots of entrants and new protocols.. The Baker Lab's RFdiffusion/RFantibody remains a contender, with 4 of the top 10 using the structure-based design method along with rational design
and other models including ESMFold and Sapiens. Nick Boyd and the team at Escalante's Mosaic de novo   ...    well with the wet lab validation as well. He got number 8 and 17 of  the top hits!
\ud835\ude17\ud835\ude33\ud835\ude30\ud835\ude35\ud835\ude30\ud835\ude24\ud835\ude30\ud835\ude2d\ud835\ude34
\ud835\ude30\ud835\ude37\ud835\ude26\ud835\ude33\ud835\ude37\ud835\ude2a\ud835\ude26\ud835\ude38 BoltzGen has a lot of entries (n=163) but a low hit rate around 1.23 percent in this dataset. BindCraft
has moderate volume (n=88) with a hit rate around 5.68 percent. Edit: seen others claim 25-30% hit rates, likely a difference in how we split the tool types will update momentarily. RFdiffusion (n=42)
shows the highest hit rate among the main buckets shown here around 21.4 percent ProteinMPNN (n=29) is close around 20.7 percent. Escalante's Mosaic (n=9) has  the highest hit rate at 88.8 percent. I
actually would not necessarily use these datapoints as limitations of the tools themselves, as the quality of the binders would meaningfully differ depending on the team submitting.
\ud835\ude14\ud835\ude26\ud835\ude35\ud835\ude33\ud835\ude2a\ud835\ude24\ud835\ude34 Boltz IPSAE seems to reasonably predictive of binding, although primarily as a filter and not a predictor:
Selecting top 1% by min_ipsae: 63.6% binders (7/11) Top 0.5%: 83.3% binders (5/6) Top 10%: 18.4% binders (19/103) Among already-binding designs, these scores  don\u2019t strongly correlate with KD
(it's better at \u201cbinder vs not\u201d than \u201cbest binder\u201d). \ud835\ude17\ud835\ude33\ud835\ude22\ud835\ude24\ud835\ude35\ud835\ude2a\ud835\ude24\ud835\ude22\ud835\ude2d
\ud835\ude35\ud835\ude22\ud835\ude2c\ud835\ude26\ud835\ude22\ud835\ude38\ud835\ude22\ud835\ude3a\ud835\ude34 Boltz2 min_ipsae can be a legitimate hard filter for evaluating designs. I would suspect
this is true of AF2 min_ipsae as well. Want ~25 designs? pick very top tail (this dataset suggests you can get >30% hit rate). Want ~100 designs? top ~10% is ~2\u00d7 baseline hit rate. Binding does
not mean function. Only 19 designs have"], "published_date": "2026-01-22T16:00:14.000", "score": null}, {"title": "adaptyvbio/egfr_competition_2", "url":
"https://github.com/adaptyvbio/egfr_competition_2", "snippet": "# Repository: adaptyvbio/egfr_competition_2\n\nThis repo contains the results data for Round 2 of EGFR Protein Design Competition.\n\n-
Stars: 18\n- Forks: 2\n- Watchers: 18\n- Open issues: 3\n- License: Other (NOASSERTION)\n- Default branch: main\n- Homepage: https://foundry.adaptyvbio.com/competition\n- Created:
2024-12-12T19:21:08Z\n- Last push: 2025-03-18T13:29:00Z\n- Contributors: 4 (top: tJala, igoradaptyv, elkoz, DrLeucine)\n\n---\n\nData package\n\nThis repo contains the results data for Round 2 of EGFR
Pr", "highlights": ["# Repository: adaptyvbio/egfr_competition_2 This repo contains the results data for Round 2 of EGFR Protein Design Competition. - Stars: 18\n- Forks: 2\n- Watchers: 18\n- Open
issues: 3\n- License: Other (NOASSERTION)\n- Default branch: main - Homepage: https://foundry.adaptyvbio.com/competition\n- Created: 2024-12-12T19:21:08Z - Last push: 2025-03-18T13:29:00Z\n-
Contributors: 4 (top: tJala, igoradaptyv, elkoz, DrLeucine)   ...    This repo contains the results data for Round 2 of EGFR Protein Design Competition, hosted by Adaptyv Bio in partnership with
Polaris and Dimension. ### \ud83c\udd95 Update: Neutralisation data now available We've performed a neutralisation assay and are now releasing the results. In a neutralisation assay, we measure the
interaction between the competitor protein (here, human EGF) and the target (EGFR), both alone (as a control) and in the presence of a binder. From this signal, we calculate the neutralisation
coefficient, which estimates how effectively the binder prevents the competitor-target interaction. A neutralisation coefficient of 100% means complete inhibition, while a binder with 0% does not
hinder the EGF-EGFR interaction at all. ---\n\n\ud83d\udcca Processed binding affinity characterization data and sequence similarity metrics:\n\n> Results folder \ud83d\udd2c Kinetic curves and raw
data: > https://api.adaptyvbio.com/storage/v1/object/public/egfr_design_competition_2/package.zip\n\n\ud83d\udee1\ufe0f Neutralisation data: >
https://api.adaptyvbio.com/storage/v1/object/public/egfr_design_competition_2/package_neutralisation.zip \ud83e\uddf1 AlphaFold2 Structure predictions (.pdb) for all 400 selected designs:   ...
\ud83c\udf10 Embeddings from a variety of models (ESM C, ESM2, Saprot, Protek) for all submissions: > https://api.adaptyvbio.com/storage/v1/object/public/egfr_design_competition_2/embeddings.zip\n\n#
Methods\n\n## Metrics More details on the metrics that were used for ranking the sequences can be found in the metrics repo.   ...    Two of the metrics that we used for scoring the designs
computationally are derived from AlphaFold2 predictions. To   ...    We checked each sequence against several sequence databases. As part of the initial competition rules, only proteins that were at
least 10 amino acids (AA) away from a published sequence were considered valid and counted in the final leaderboard. The results of that similarity search are stored in the results folder. The
**similarity check** metric is   ...    `similarity_check` value of \u201cnull\u201d indicates that no matches were found in any of the the databases. The databases that we checked are SwisssProt,
THPdb, USPTO, sequences from the first round of the competition and binders designed by Cao et al. (2022). The scripts can be found in the first round data package repo.   ...    We ran DE-STRESS on
the AlphaFold structure predictions for all 400 selected designs from round 2 of the competition, both with EGFR (`destress_binder_with_egfr.csv`) and without (`destress_binder_only.csv`).   ...
### Neutralisation Coefficient In a neutralisation assay, we measure the interaction between the competitor protein (here, human EGF) and the target (EGFR), both alone (as a control) and in the
presence of a binder. From this signal, we calculate the neutralisation coefficient, which estimates how effectively the binder prevents the competitor-target interaction. A neutralisation coefficient
of 100% means complete inhibition, while a binder with 0% does not hinder the EGF-EGFR interaction at all.   ...    The submitted protein sequences were reverse-translated, and the corresponding DNA
sequences were optimized using   ...    systems, mRNA secondary structure stability, and synthesizability factors. Additionally, non-coding regions at the 5' and 3' ends, optimized for cell-free
expression, were incorporated into the coding sequences. Suitable gene constructs   ...    proteins. The template DNA was added, and protein expression was conducted over a defined period. During the
competition, at least two expression batches were performed for each sequence entry, with some sequences tested up to four times under varying conditions. Protein synthesis success was assessed via a
label-free quantification assay.   ...    All code is"], "published_date": "2024-12-12T19:21:08.000", "score": null}, {"title": "Adaptyv EGFR Binder Design Competition 2 | Proteinbase", "url":
"https://foundry.adaptyvbio.com/competition", "snippet": "\n\n \n\n \n\n \n\nAdaptyv EGFR Binder Design Competition 2 | Proteinbase\n\n\nPublish\nDownload\nAdaptyv EGFR Binder Design Competition 2 |
Proteinbase\nCompetition Banner\n# Adaptyv EGFR Binder Design Competition 2\nTask: Protein Binding\nTarget: EGFR\n400 proteins experimentally validated\nDesign novel protein binders targeting and
neutralizing EGFR, a cell-surface receptor that promotes uncontrolled cell growth in many cancers.\nOrganised by:\naAdaptyv Bio\n## Competition Completed\nResults have been released. Vie",
"highlights": ["Adaptyv EGFR Binder Design Competition 2 | Proteinbase   ...    # Adaptyv EGFR Binder Design Competition 2\nTask: Protein Binding\nTarget: EGFR\n400 proteins experimentally validated
Design novel protein binders targeting and neutralizing EGFR, a cell-surface receptor that promotes uncontrolled cell   ...    Organised by:\naAdaptyv Bio\n## Competition Completed Results have been
released. View the winning submissions and explore experimental data\nView Results\n## Overview\n1. Stage 1\nComputational Design Submit your computational antibody designs. 200 designs will be
selected for experimental validation, 100 by the best pAE\\_interaction,100 based on the rule of cool Submissions OpenOct 4, 2024\n/\nSubmissions CloseNov 4, 2024\nView details\n2.\nStage
2\nExperimental Validation Selected designs undergo experimental validation in the Adaptyv Lab. Proteins with the highest binding affinity win the competition. Validation startsNov 5, 2024\n/\nResults
releasedJan 15, 2025\nView details\n1.\nStage 1\nComputational Design Submit your computational antibody designs. 200 designs will be selected for experimental validation, 100 by the best
pAE\\_interaction,100 based on the rule of cool Submissions OpenOct 4, 2024\n/\nSubmissions CloseNov 4, 2024\nView details\n2.\nStage 2\nExperimental Validation Selected designs undergo experimental
validation in the Adaptyv Lab. Proteins with the highest binding affinity win the competition. Validation startsNov 5, 2024\n/\nResults releasedJan 15, 2025\nView details\n## About the Target\n###
EGFR PDB: 1IVO   ...    LEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEI LHGAVRFSNNPALCNVESIQWRDIVSSDFLS... Epidermal Growth
Factor Receptor (EGFR) is a transmembrane protein that plays a critical role in cell growth, differentiation, and survival. It is frequently overexpressed or mutated in various cancers, including non-
small cell   ...    In this competition, you can continue testing your skills as a protein designer by leveraging data from Round 1. The challenge, as before is to find novel grade binders to EGFR"],
"published_date": null, "score": null}, {"title": "Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition", "url": "https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2",
"snippet": "Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition | bioRxiv\nSkip to main content\nbioRxiv\nSearch for this keyword\nAdvanced Search\nNew Results# Crowdsourced
Protein Design: Lessons From the Adaptyv EGFR Binder Competition\nTudor-StefanCotet,IgorKrawczuk,FilippoStocco,NoeliaFerruz,AnthonyGitter,YoichiKurumida,Lucas de AlmeidaMachado,FrancescoPaesani,Cianna
N.Calia,Chance A.Challacombe,NikhilHaas,AhmadQamar,Bruno E.Correia,MartinPacesa,LennartNickel,KarticSubr,Leonardo V.C", "highlights": ["Crowdsourced Protein Design: Lessons From the Adaptyv EGFR
Binder Competition | bioRxiv\nSkip to main content\nbioRxiv   ...    New Results# Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition Tudor-
StefanCotet,IgorKrawczuk,FilippoStocco,NoeliaFerruz,AnthonyGitter,YoichiKurumida,Lucas de   ...    J.Campbell,ConstanceFerragu,PatrickKidger,LoganHallee,Christopher W.Wood,Michael
J.Stam,TadasKluonis,Suleyman   ...    doi:https://doi.org/10.1101/2025.04.17.648362\nTudor-Stefan Cotet\n1Adaptyv;\n* Find this author on Google Scholar   ...    * Search for this author on this
site\n* Abstract\n* Info/History\n* Metrics\n* Data/Code\n* **Preview PDF\nLoading ## Abstract In this report, we summarize and analyze the 2024 Adaptyv EGFR protein design competition. Participants
used computational and ML methods of their choice to design proteins to bind the EGFR, a key drug target that plays a critical role in cell growth, differentiation, and cancer development. Over 1800
designs were submitted to the competition across two rounds. Of these, 601 proteins were selected and characterized for expression and binding affinity to EGFR, with competitors both optimizing
existing binders (achieving 1.21 nM) and creating novel (de novo) binders (achieving 82 nM). All selected designs were experimentally validated with Adaptyv's automated BLI pipeline. This illustrates
the potential of crowdsourced competitions to drive creativity and innovation in protein design. However, the competition also exposed key challenges, such as the lack of standardized benchmarks,
standardized experimental design targets, and robust computational metrics for method comparison. We anticipate that future competitions will allow for addressing these gaps and motivate continued
progress in computational protein design.   ...    L.V.C. has consulted part-time for NEC OncoImmunity AS during the writing stage of this paper. M.J.S. began employment at Biophoundry, Inc. during
the writing stage of this paper. N.H. and C.A.C. are employees of BioLM. T-S.C. and I.K.   ...    employees of Adaptyv.\n## Footnotes\n* - Updated author order, competing interests, funding
acknowledgements - fixed typos in abstract and throughout the paper, as well as formatting - updated the discussion section to flow better, introduce the name of the proposed benchmark *
https://github.com/adaptyvbio/egfr2024\\_post\\_competition\nCopyright The copyright holder for this preprint is the author/funder, who has granted bioRxiv a license to display the preprint in
perpetuity.It is made available under aCC-BY 4.0 International license. Back to top\nPreviousNext\nPostedApril 24, 2025.\nDownload PDF\nData/Code\n**Email   ...    This question is for testing whether
or not you are a human visitor and to prevent automated spam submissions.\nShare Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition   ...
J.Campbell,ConstanceFerragu,PatrickKidger,LoganHallee,Christopher W.Wood,Michael J.Stam,TadasKluonis,Suleyman MertUnal,ElianBelot,AlexanderNaka,Adaptyv Competition Organizers
bioRxiv2025.04.17.648362;doi:https://doi.org/10.1101/2025.04.17.648362\nShare This Article:Copy   ...    bioRxiv2025.04.17.648362;doi:https://doi.org/10.1101/2025.04.17.648362\n## Citation Manager
Formats\n* BibTeX\n* Bookends   ...    * Bioinformatics(34855)\n* Biophysics(17937)\n* Cancer Biology(15066)\n* Cell Biology(21138)\n* Clinical Trials(138) * Developmental Biology(11"],
"published_date": "2025-04-24T00:00:00.000", "score": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url": "https://adaptyvbio.substack.com/p/protein-design-
competition-has-binder", "snippet": "Protein Design Competition: Has binder design been solved?\n\n\n\n# Adaptyv Bio\n\nSubscribeSign in\n\n# Protein Design Competition: Has binder design been
solved?\n\n### We analyze the results of our protein design competition where 130 designers created binders for EGFR. With a 5x improvement in success rates and some designs outperforming clinical
antibodies, we exp\n\n\n\nAdaptyv Bio\n\nDec 24, 2024\n\n5\n\nShare\n\nTL;DR\n\nThe results of our second Protein Design Competition show dramatic progress in the field. O", "highlights": ["We analyze
the results of our protein design competition where 130 designers created binders for EGFR. With a 5x improvement in success rates and some designs outperforming clinical antibodies, we exp Adaptyv
Bio\n\nDec 24, 2024\n\n5\n\nShare\n\nTL;DR The results of our second Protein Design Competition show dramatic progress in the field. Out of 400 tested proteins, 378 expressed successfully (95%) and 53
of these bound to their target EGFR (14% success rate). This represents a 5x improvement in binding success compared to just three months ago. The best designs even matched or exceeded the performance
of Merck's Cetuximab, a clinically approved therapeutic antibody. The competition demonstrated that protein design is becoming more reliable and accessible - 30 out of 130 participants managed to
create at least one successful binder using various approaches, from optimizing existing antibodies to   ...    While we can now generate functional proteins more consistently, a key challenge
remains: predicting which designs will   ...    We released the results of our second Protein Design Competition just about 2 weeks ago\u2026 and they were great!   ...    believe these guidelines,
and the community momentum that was bubbling up the scenes, with \u201cprotein design recipes\u201d, blog posts, and general advice, were the causal factors that led to an increase in both hit rates
and expression: from 2.5% for the former to 13%, and from 76% to 96%. These figures are something to be proud of, and we would like to thank   ...    Now, onto some data analysis!\n\n### How many
binders and expressed designs did we see?   ...    We\u2019ve talked before about how popular the diversified and optimized binder choices were for landing the top 100 spots. M  ost of these were
submitted within a couple of days from the deadline. And yet, all designers choosing these were rightfully doing so: we have a 28% hit rate for diversified binders and 18% for optimized. We\u2019ve
already seen how successful taking an existing binder and redesigning its non-interface regions was: Cradle got a better binder than Cetuximab, Chris Xu had a few strongly binding ones, and Aurelia
Bustos had an 80% hit-rate. The message is clear: if you want to create a better binder, it  helps to have an existing one to start from!  The expression rate for those   ...    We think some people
departed too far from the natural sequence for this, trying to maximize the scores. Yet, this is something worthy of a deeper investigation.  For de novo, hallucination (BindCraft) got 6 out of the 7
binders, with diffusion (RFdiffusion) claiming the final one. The overall success rate of hallucination (9%, 6/65 tested, as seen in   ...    Distribution of binding affinities by design category and
selection status.  There is almost no difference when   ...    predicted \u0394G or maximizing the number of contacts), there is no secret recipe for binder designs and several of these methods
optimize different properties.  ### Conclusion: Has protein binder design been solved? Not yet \u2014 but the rate of progress in protein engineering is astounding. Within just a few months from Round
1 (September) to Round 2 (December), we witnessed dramatic improvements in expression and binding success rates, along with a surge in participation from the protein design community.  Optimization of
existing binders is proving remarkably effective and can systematically yield better proteins than previous candidates. Cradle's success in this   ...    benefit from such tools.  In de novo design,
BindCraft has brought about a significant increase in success rates and has immediately been adopted by the protein design community. It remains to be seen whether this represents a broader   ...
will shift the meta back.  Both in this competition and across the field, we still struggle to predict binding success   ...    represents one of the field's most pressing challenges and we need to
generate more data to build better models here. Thanks again to all participants for making this competition an immense success through sharing your cool designs and interesting approaches. We have
exciting plans for 2025 and can't wait to see what kinds of proteins you'll design   ...    If you want to participate in a paper write-up in the coming weeks about the two rounds of the Protein
Design Competition, you can fill out this form to join.  If you want to stay in the loop about future competitions and   ...    About Adaptyv Adaptyv is the cloud lab for protein designers. Our
platform is the fastest way for you to experimentally   ...    5\n\nShare  #### Discussion about this post\n\nCommentsRestacks\n\nNo posts\n\n### Ready for more?\n\nSubscribe \u00a9 20"],
"published_date": "2024-12-24T23:03:38.000", "score": null}, {"title": "Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition | bioRxiv", "url":
"https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2.full-text", "snippet": "# Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition\n\n- Adaptyv Competition
Organizers\n- Alexander Naka\n- Elian Belot\n- S\u00fcleyman Mert \u00dcnal\n- Tadas Kluonis\n- Michael J. Stam\n- Christopher W. Wood\n- Logan Hallee\n- Patrick Kidger\n- Constance Ferragu\n- Maxwell
J. Campbell\n- Leonardo V. Castorina\n- Kartic Subr\n- Lennart Nickel\n- Martin Pacesa\n- Bruno E. Correia\n- Ahmad Qamar\n- Nikhil Haas\n- Chance A. Challacombe\n- Cianna N. Calia\n- Francesco
Paesani\n- Lucas de Almeida Macha", "highlights": ["In this report, we summarize and analyze the 2024 Adaptyv protein design competition. Participants used computational   ...    (EGFR), a key drug
target involved in cell growth, differentiation, and cancer development. Over 1,800 designs were submitted across two rounds. Of these, 601 proteins were selected and characterized for expression and
binding affinity to EGFR, with competitors both optimizing existing binders (K**D = 1.21 nM) and creating de novo binders (K**D = 82 nM). All selected designs were experimentally validated using
Adaptyv\u2019s automated Bio-Layer Interferometry (BLI) pipeline. This competition illustrates the potential of crowdsourcing to drive creativity and innovation in protein design. However, it also
exposed key challenges, such as the lack of standardized benchmarks, experimental design targets, and robust computational metrics for method comparison. We anticipate that future competitions will
address these gaps and   ...    publicly accessible are: Adaptyv\u2019s EGFR Binder Competition, Liberum Bio\u2019s Protein Design Winter Games, the BioML   ...    In this context, the 2024 Adaptyv
EGFR binder competition provided a unique platform to evaluate a diverse array of   ...    underrepresented folds. Moreover, the unnormalized likelihood was biased towards smaller designs.  experience
in protein design. The 73% expression rate matched typical rates reported in the field, while the binder hit rate was either comparable to or an order of magnitude higher than previous studies
[CK24a]. For instance, earlier work on de novo EGFR binders reported a 0.01% hit rate, compared to the 2.5% (5 out of 201) observed in R1 [Cao+22].  Subsequent changes to the scoring metrics and to
the design strategies [CK24a; CK24b] in R2 were driven by community feedback and made possible through collaborative sharing of expertise within the community. Whether it was these changes, the
knowledge sharing spurred by the first round (see section 2.5), or other factors, R2 saw a 95% expression rate (378 of 400 tested) as well as a much higher binding rate with 53 confirmed binders.
additional sequences to be tested sharing their results on GitHub and X [Nik24; Git25; Suz25].  Other highlights included a Nature news article [Cal24]   ...    (A) Number of submissions leveraging
ESM2 or 3 in their design methodology (not just for log-likelihood scoring) across the competition rounds and (B) total number of ESM binders/non-binders. ## 4 Competition Results  In this section, we
provide an overview of key results from both rounds of the competition, building upon initial analyses previously presented in Adaptyv blog posts [CK24a; CK24b; CK24d]. Overall, we focus on notable
improvements in design strategies, protein expression levels, and the number and quality of successful binders identified. By comparing results across rounds we illustrate how public competitions can
drive methodological optimization, promote promising design approaches, uncover  Overall, these results demonstrate that while the computational metrics used for design filtering cannot accurately
predict binding probabilities, the collective knowledge gained from the first round of the competition helped to improve design strategies going into R2 and increase the overall binder design success
rates. ### 4.2 Shift in choice of design methods  We can see that binder optimization had a 2-fold increase in the number of submissions (Figure 9 A), with a similar increase for the protein
hallucination strategy. This could be attributed to   ...    expressed designs, we see a major increase in de novo strategies, again ascribed to the increased expressibility and solubility of most
submissions due to the usage of redesign tools such as  UMG24a; CRG24]. Further analyses were   ...    this score and the increased hit rate (from 3% to 13%).  The Adaptyv EGFR binder competition
provided a unique and   ...    typical constraints and delays associated with traditional publishing. Such initiatives are especially  One primary insight from the competition is that, while
significant advances have been achieved in computational protein binder design, the challenge remains far from solved. Deep learning-based design methods, such as RFdiffusion or BindCraft, while
achieving high levels of experimental success, can still produce many false positive designs with high in silico scores. This outlines clear limitations in the currently used computational metrics and
methods used for design   ...    computational methods.  Another significant takeaway is the need for standardized benchmark targets within the   ...    PPI\n: Protein-Protein Interaction. 14\nR1\n:
Round 1 of the Adaptyv Bio EGFR Binder Design Competition. 3\u20137, 9, 10, 26\nR2 : Round 2 of the Adaptyv Bio EGFR Binder Design Competition. 3\u20137, 9, 10, 15, 26\nROC AUC  ## A Supplementary
Results   ...    ### A.1 Score distributions shifted across the 2 competition rounds  To explore"], "published_date": null, "score": null}, {"title": "Protein Optimization 102: Lessons from the
protein design competition", "url": "https://www.adaptyvbio.com/blog/po102", "snippet": "Oct 18, 2024\n\n# Protein Optimization 102: Lessons from the protein design competition\n\nThe results of the
first round of the EGFR binder design competition are here! In this blog post, we analyze the most common model and design choices, take a closer look at the strategies that yielded successful
binders, and provide recommendations for your future design campaigns.\n\nTL;DR\n\n\u2022 We analyzed the submissions for the first EGFR competition (results here) for you!\n\n\u2022 Most people
explored RFdiffusion f", "highlights": ["Oct 18, 2024\n\n# Protein Optimization 102: Lessons from the protein design competition The results of the first round of the EGFR binder design competition
are here! In this blog post, we analyze the most common model and design choices, take a closer look at the strategies that yielded successful binders, and provide   ...    TL;DR\n\n\u2022 We analyzed
the submissions for the first EGFR competition (results here) for you! \u2022 Most people explored RFdiffusion for backbone generation, ProteinMPNN for obtaining sequences, with some other interesting
approaches we\u2019ve highlighted. \u2022 Winning combination: AlphaFold2 hallucination and SolubleMPNN inverse-folding. \u2022 We\u2019ve provided actionable   ...    ### Overview of Adaptyv\u2019s
EGFR binder design competition In our competition, creative protein engineers were tasked with designing a new binder to the extracellular domain of EGFR, a cancer-associated drug target. We selected
200(+1) of the most promising sequences for screening. The top 100 were based on the AlphaFold2 interface   ...    because it has been exhaustively used in the communities, including luminaries such
as the Baker lab (Bennett et al., 2023; Watson et al., 2023; Zhang et al., 2024). Most successful designs (in terms of leaderboard placement) aimed to   ...    made great leaps to address this (e.g.,
Google DeepMind\u2019s AlphaProteo, Zambaldi et al., 2024, which has a 24.5% hit   ...    out of 726 total submissions, with 65 of these being selected for validation). Looking more in-depth at the
models represented, we found that RFdiffusion for backbone design followed by ProteinMPNN   ...    motifs. This is a completely valid choice given the iPAE objective and lack of fully characterized
EGFR binder   ...    you\u2019re working with a limited experimental budget. ### Expression rates Not all sequences expressed, leaving some people surprised and some disappointed. This is the reality
of translating in silico designs into experimentally-valid candidates. A 73% (146/201) expression rate is about on par with Wicky and   ...    symmetric assemblies. Goverde and colleagues compared the
designs obtained from the standard ProteinMPNN for an   ...    Recently, a paper from the Baker lab (Gl\u00f6gl et al., 2024) achieved a 98% (94/96) expression rate for TNFR1 binders. With this
context, 73% could be considered on the lower side compared to the Baker lab. However, only half of the   ...    working in a therapeutics biotech). This combined with the wide range of methods
employed and the fact that not many people optimized for expression, only binding/iPAE, makes us at Adaptyv relatively happy with the outcome. For the second round, we are including an expression
proxy in the metrics. We also recommend using SolubleMPNN as a final check before submitting your sequences! ### Hit rates Out of these, 5 were considered strong binders, with a KD between 3e-8 M to
2.3e-5 M, with 2 labelled as weak binders (KD above 1e-5 M). This yields a 2.5% total hit rate (5/201), considerably higher than past EGFR-targeting design campaigns (0.01% previously reported using a
Rosetta protocol, Cao et al., 2022). We should emphasize that hit rates are highly dependent on the design target, with highly accessible, hydrophobic (Cao et al., 2022; Pacesa et al., 2024), and
reduced flexibility epitope regions (Kim, Choi & Kim, 2021) often yielding better results. To ensure you get a lot of binders, **we recommend you target hydrophobic surface regions or the EGFR **
epitope region we provided, especially if you want to succeed in the EGF neutralization assay we are doing!   ...    Seven binders (3 true binders, with 2 disqualified due to similarity to other
therapeutics  , and 2 weak) are too few   ...    expression rate. Sigrid and Adrian used the ProtFlow pipeline (not to be confused with Adaptyv Bio\u2019s ProteinFlow -   ...    binders. bioRxiv.
2024.08.29.610300. doi:10.1101/2024.08.29.610300. # More post ###### Jan 5, 2026  ###### What happened in the Nipah Protein Design Competition so far? + Prediction markets for   ...    ###### Nov 5,
2025   ...    ###### Oct 8, 2025\n\n###### Proteinbase \u2014 the home of protein design data\n\n\u00a9 202"], "published_date": null, "score": null}, {"title": "Adaptyv Bio", "url":
"https://www.adaptyvbio.com/blog", "snippet": "Blog\n\n## Latest posts\n\n\n\nDec 9, 2025\n\n##### What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein
design\n\nFor our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were most widely adopted, and highlight several noteworthy and creative
community contributions. Plus, we opened a prediction market on Manifold for this competition so you can bet on hit rates, best performing models, and more\n\nNov 5, 202", "highlights": ["in the Nipah
Protein Design Competition so far? + Prediction markets for protein design For our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were most
widely adopted, and highlight several noteworthy and creative community contributions. Plus, we opened a prediction market on Manifold for this competition so you can bet on hit rates, best performing
models, and more Nov 5, 2025\n\n##### Designer Spotlight: Navigating the multi-property maze for therapeutic peptide design - Tong Chen Tong Chen and colleagues from Pranam Chatterjee\u2019s
Programmable Biology Group at the University of Pennsylvania are   ...    Oct 6, 2025\n\n##### Proteinbase \u2014 the home of protein design data   ...    across multiple (up to 5) different
properties](./blog/mog-dfm/)   ...    ##### Adaptyv is the cloud lab for protein designers \u2014 and now available for everyone\n\n](./blog/launch/)\n\nSep 1, 2025   ...    Jul 29, 2025\n\n#####
Designer Spotlight: ProtRL - Reinforcement learning and the Move 37 of protein engineering   ...    a melting temperature comparable to the most optimized FGF-1 variants in the literature! Apr 26,
2025\n\n##### Introducing BenchBB and the community paper of the Protein Design Competition We wrote a community paper about our Protein Design Competition, teaming up with your favourite protein
designers from both rounds. We close the paper by creating BenchBB, the Bench-tested B inder B enchmark \u2014 a curated set of 7 protein   ...    Feb 11, 2025\n\n##### Case study: Validating proteins
designed by Microsoft Research\u2019s EvoDiff   ...    EvoDiff, their novel sequence-first protein design model, in just a few weeks. Dec 25, 2024\n\n##### Protein Design Competition: Has binder
design been solved? We analyze the results of our protein design competition where 130 designers created binders for EGFR. With a 5x improvement in success rates and some designs outperforming
clinical antibodies, we explore what worked, what didn't, and what this means for the future of protein engineering Dec 5, 2024\n\n##### Protein Optimization 103: Racing to the Top 100 What a close
race this one was! In this blog post, we look at how submissions evolved throughout our latest EGFR binder design competition. We highlight the most widespread model and design choices, how some
people exploited loopholes in our scoring system, and argue if de novo design is reliable or not. We also have plenty of animations for you to click through! Nov 13, 2024\n\n##### Introducing the
Adaptyv Bio API Imagine if you could let your AI agent design novel proteins, autonomously test them in our wet lab and then improve itself based on the results. Oct 18, 2024\n\n##### Protein
Optimization 102: Lessons from the protein design competition The results of the first round of the EGFR binder design competition are here! In this blog post, we analyze the most common model and
design choices, take a closer look at the strategies that yielded successful binders, and provide recommendations for your future design campaigns. Load More\n\n](./blog/proteinbase/) Imagine if you
could let your AI agent design novel proteins, autonomously test them in our wet lab and then improve itself based on the results. In this case study, we highlight how Microsoft Research used our
automated lab to validate proteins generated by EvoDiff, their novel sequence-first protein design model, in just a few weeks.](./blog/evodiff/) \u00a9 2025 \u2014 Adaptyv Biosystems\n\nFor all
questions:\n\nsupport@adaptyvbio.com\n\nFor all questions: support@adaptyvbio.com   ...    Biopole Life Science Campus\nRoute de la Corniche 5, 1066 Epalinges\nLausanne, Switzerland\n\n---\n\n##
Navigation - ./\n- Services\n- Blog\n- Team\n- Careers\n- Docs\n- API\n- ')\" class=\"framer-ppr6dd\" aria-hidden=\""], "published_date": null, "score": null}, {"title": "Boolean Biotech", "url":
"https://blog.booleanbiotech.com/what-we-learned-adaptyv", "snippet": "Boolean Biotech\n\n# What we learned about binder design from the Adaptyv competition\n\nThis article is a deeper look at
Adaptyv's binder design competition, and some thoughts on what we learned. If you are unfamiliar with the competition, there is background information on the Adaptyv blog and my previous
article.\n\n## The data\n\nAdaptyv did a really nice job of packaging up the data from the competition (both round 1 and round 2). The also did a comprehensive analysis of which metrics predicted
suc", "highlights": ["Boolean Biotech\n\n# What we learned about binder design from the Adaptyv competition This article is a deeper look at Adaptyv's binder design competition, and some thoughts on
what we learned. If you are unfamiliar with the competition, there is background information on the Adaptyv blog and my previous article.   ...    Adaptyv did a really nice job of packaging up the
data from the competition (both round 1 and round 2). The also did a comprehensive analysis of which metrics predicted successful binding in this blogpost. The data from round 2 is more comprehensive
than round 1 \u2014 it even includes Alphafolded structures \u2014 so I downloaded   ...    Three of these metrics (`pae_interaction`,`esm_pll`,`iptm`) were used to determine each entry's rank in the
...    ```\n# get data and script\ngit clone https://github.com/adaptyvbio/egfr_competition_2\ncd egfr_competition_2/results wget
https://gist.githubusercontent.com/hgbrian/1262066e680fc82dcb98e60449899ff9/raw/regress_adaptyv_round_2.py   ...    regress_adaptyv_round_2.py ``` The results are not great! There are a few ways to
slice the data (including replicates or not; including`similarity_check` or not; including non-binders or not). There is a little signal, but I think it's fair to say nothing was strongly predictive.
| Model | R\u00b2 | RMSE (log units) | Median Fold Error |\n| --- | --- | --- | --- | | Linear Regression | 0.150 | 0.729 | 1.8x |\n| Random Forest Regression | 0.188 | 0.712 | 1.4x | | SVM Regression
| 0.022 | 0.781 | 1.2x |\n| XGBoost | 0.061 | 0.766 | 1.2x |\n| Mean Kd only | -0.009 | 0.794 | 1.9x |   ...    Surprisingly, no one feature dominates in terms of predictive power\n\n### Virtual
leaderboard rank vs competition rank If there really is no predictive power in these computational metrics, there should be no correlation between rank in the virtual leaderboard and rank in the
competition. In fact, there is a weak but significant correlation (Spearman correlation ~= 0.2). However, if you constrain to the top 200 (of 400 total), there is no correlation. My   ...    It may be
too much to ask one set of metrics to work for antibodies (poor PLL, poor PAE?), de novo binders (poor PLL),   ...    heuristics are implicit in the weights of the model? ## What did we learn?\n\nI
learned a couple of things: - We do not have a way to predict if a given protein will bind a given target. - Some tools, specifically BindCraft, can consistently generate decent binders, at least
against targets and binding pockets present in its training set (PDB). (The BindCraft paper also shows success with at least one de novo protein not present in the PDB.) I think this is pretty
interesting, and a bit counterintuitive. More evidence that we cannot predict binding comes from   ...    can (yet). The Adaptyv blogpost ends by stating that binder design has not been solved yet.
This is clearly true. So what comes   ...    - We could develop an \"AlphaFold for Kd prediction\". There are certainly attempts at this, e.g., ProAffinity-GNN and the PPB-Affinity dataset to pick two
recent examples, but I don't know if anything works that well. The big problem   ...    - We could find computational metrics that work, based on the current sequence and structure data. For example,
BindCraft includes \"number of unsatisfied hydrogen bonds at the interface\" in its heuristics. I am skeptical that we can do a lot better with this approach. For one thing, Adaptyv has already
iterated once on its ranking metrics, with negligible improvement in prediction. Luckily, progress in this field is bewilderingly fast so I'm sure we'll see a ton of developments in 2025. Kudos to
Adaptyv for helping push things forward. var _gaq=[['_setAccount','G-T78"], "published_date": null, "score": null}, {"title": "Protein Design Competition - RESULTS - Adaptyv Bio", "url":
"https://adaptyvbio.substack.com/p/protein-design-competition-results", "snippet": "Protein Design Competition - RESULTS - Adaptyv Bio\n\n# Adaptyv Bio\n\nSubscribeSign in\n\n# Protein Design
Competition - RESULTS\n\n### The long awaited results are here -- and they don\u2019t disappoint!\n\nAdaptyv Bio\n\nDec 08, 2024\n\n2\n\nShare\n\nThe long awaited results are here -- and they
don\u2019t disappoint!\n\n\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400! \ud83e\uddec Out of those 400 proteins, 378 expressed (95% expression rate!)\ud83d\ude80
Out of those 378 expressed proteins, 53 did successfully bind t", "highlights": ["Protein Design Competition - RESULTS - Adaptyv Bio\n\n# Adaptyv Bio\n\nSubscribeSign in # Protein Design Competition -
RESULTS\n\n### The long awaited results are here -- and they don\u2019t disappoint! Adaptyv Bio\n\nDec 08, 2024\n\n2\n\nShare\n\nThe long awaited results are here -- and they don\u2019t disappoint!
\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400! \ud83e\uddec Out of those 400 proteins, 378 expressed (95% expression rate!)\ud83d\ude80 Out of those 378 expressed
proteins, 53 did successfully bind the target protein EGFR (that\u2019s a 14% success rate, more than 5x of the success rate of the previous round just 2 months ago!)\ud83d\udcaa The best binders
reached single-digit nanomolar affinities which is within the range of the commercially sold Cetuximab antibody by Merck \ud83d\ude0e 30 out of 130 protein designers managed to design at least one
binding protein Check out the full results\n\nWant to join the discussion about the results?\n\nCheck out the thread on X or on LinkedIn Here\u2019s the breakdown: The team at Cradle takes the top
spot in terms of binding affinity by using their protein language models to introduce 10 mutations into the framework regions of the Cetuximab antibody. This way, they generated an scFv with a KD of
1.2 nM which is lower than the original Cetuximab scFv. Congrats!---Tihumab aka Chris Xu aka Xushaoyong (https://lnkd.in/e8Mj8eq3) lands two of his nanobodies on rank 2 & 3 using his antibody
humanization technique. The   ...    prediction and developability index prediction.--- Aurelia Bustos MD, PhD's approach of modifying the TGFa protein with diffusion models to yield an optimized
binder for EGFR was already super successful in our computational ranking, with 8 out of her 10 designs landing in the top 25. This turned out to be also successful in the lab, with all 8 of those
binders working!---Also in the top 10:- Jeff Vogt with his scFv optimization pipeline- Lennart Nickel using BindCraft to generate fully de novo binders- Brian Naughton and Alan Blakely who both had
the idea of using a linker approach to combine binders from previous rounds- Shosuke Suzuki's de novo binder- Yoichi Kurumida\u2019s RFdiffusion scaffolded binder- Young Su Ko who\u2019s using
Raygun+Protrek to filter his sequencesCongrats to everyone that ended up designing one or more of those binders and thanks to everyone that participated! We loved reading about all those interesting
design approaches and tried to give as many shoutouts as possible. The energy in the protein design community is truly amazing and we can\u2019t wait to see how many more cool proteins you'll all be
designing in the future! 2\n\nShare\n\n#### Discussion about this post\n\nCommentsRestacks\n\nNo posts\n\n### Ready for more?\n\nSubscribe \u00a9 2026 Adaptyv Bio \u00b7 Privacy\u2219 Terms\u2219
Collection notice\n\nStart your Substack Get the app Substack is the home for"], "published_date": "2024-12-08T00:00:53.000", "score": null}]
```

## 💬 Response

Excellent. Let me now get more details on the Nipah competition results and research the state of the art in computational protein design.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "AdaptyvBio Nipah binder competition results 2026 success rate"
}
```

### 📋 Result

```
{"query": "AdaptyvBio Nipah binder competition results 2026 success rate", "results": [{"title": "In the Nipah binder competition, which protein designer will have proteins that bind? | Manifold",
"url": "https://manifold.markets/Proteinbase/in-the-nipah-binder-competition-whi-qyqILNdhpI", "snippet": "[https://proteinbase.com/nboyd](https://proteinbase.com/nboyd)\n[https://proteinbase.com/max-
beining](https://proteinbase.com/max-beining)\n[https://proteinbase.com/drleucine](https://proteinbase.com/drleucine)\n[https://proteinbase.com/joan-gimenez](https://proteinbase.com/joan-
gimenez)\n[https://proteinbase.com/alisa-bryantseva](https://proteinbase.com/alisa-bryantseva)\n[https://proteinbase.com/gerard-boxo](https://proteinbase.com/gerard-
boxo)\n[https://proteinbase.com/david-masnou-s-nchez](https:/", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."}, {"title": "Adaptyv Bio on
X: \"The results of the Nipah Protein Design Competition are out! \ud83e\uddec 1200 proteins experimentally validated (3x more than last year) \ud83d\udcc8 99 novel binders against the target protein
(a challenging tetramer with little prior work) \ud83d\udcaa 26 single digit nM or better binders, with the https://t.co/LWwDDx6myY\" / X", "url":
"https://x.com/adaptyvbio/status/2014218665542242568", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to
continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null,
"hint": null}, {"title": "The Protein Design Competition Is Back! - Adaptyv Bio", "url": "https://adaptyvbio.substack.com/p/the-protein-design-competition-is", "snippet": "The Protein Design
Competition Is Back!\n\ud83c\udf0d The biggest decentralized science experiment of 2025 starts now!\nThe protein design competition returns: we\u2019re inviting scientists, engineers, and hackers from
around the world to help design new proteins capable of neutralizing the Nipah virus, a pathogen with up to 75% mortality and no effective treatment.\nAll you need is a laptop to participate: submit
your computational protein designs, and [Adaptyv](https://adaptyvbio.com/) will synthesize and exper", "api_data": null, "hint": null}, {"title": "Protein Design Competition - RESULTS - Adaptyv Bio",
"url": "https://adaptyvbio.substack.com/p/protein-design-competition-results", "snippet": "Protein Design Competition - RESULTS\nThe long awaited results are here -- and they don\u2019t
disappoint!\nThe long awaited results are here -- and they don\u2019t disappoint!\n\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400!\n\ud83e\uddec Out of those 400
proteins, 378 expressed (95% expression rate!)\n\ud83d\ude80 Out of those 378 expressed proteins, 53 did successfully bind the target protein EGFR (that\u2019s a 14% success rate, more than 5x of the
success rate of the previous round just 2 months ago!)\n\ud83d\udcaa Th", "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? + Prediction markets
for protein design", "url": "https://adaptyvbio.substack.com/p/what-happened-in-the-nipah-protein", "snippet": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for
protein design\nFor our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were most widely adopted, and highlight several noteworthy and
creative community cont\n\u2022 We hosted our third installment of the Protein Design Competition, this time challenging participants to design a binder against the Nipah virus glycoprotein.\n\u2022
The response was incredible: Over ", "api_data": null, "hint": null}, {"title": "In the Nipah binder competition, what percentage of proteins will bind? | Manifold", "url":
"https://manifold.markets/Proteinbase/in-the-nipah-binder-competition-wha", "snippet": "Nipah is one of the deadliest viruses in the world and considered one of the top future pandemic risks.\nWe're
hosting a protein design competition on [Proteinbase](https://proteinbase.com/competitions/adaptyv-nipah-competition) where people can design binders against the virus and we will test 1200 of those
designs in our lab to see if they actually work.\nHow many of those 1200 proteins will actually bind to the target? [Last year's EGFR competition had a 13.5% hit rate](https://proteinbase.com/",
"api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."}, {"title": "Adaptyv Bio on X: \"We\u2019ve just added more experimental data to the Nipah
Protein Design Competition results: 1. Off-target HSA binding \u2014 Human Serum Albumin (HSA) is the most abundant protein in blood. For therapeutic applications it\u2019s important that your binders
don\u2019t stick to HSA. We ran https://t.co/PjLgg8G0yA\" / X", "url": "https://x.com/adaptyvbio/status/2015860679769554991", "snippet": "We\u2019ve detected that JavaScript is disabled in this
browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy
Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "In the Nipah binder competition, what protein design model will have the highest hit rate | Manifold",
"url": "https://manifold.markets/Proteinbase/in-the-nipah-binder-competition-wha-6qyPyPuudL", "snippet": "Nipah is one of the deadliest viruses in the world and considered one of the top future
pandemic risks.\nWe're hosting a protein design competition on [Proteinbase](https://proteinbase.com/competitions/adaptyv-nipah-competition) where people can design binders against the virus and we
will test 1200 of those designs in our lab to see if they actually work.\n[Last year's EGFR competition had a 13.5% hit rate overall](https://proteinbase.com/collections/adaptyv-egfr-competition-
round-2) (54 out of 4", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."}, {"title": "What happened in the Nipah Protein Design Competition so
far? + Prediction markets for protein design", "url": "https://www.adaptyvbio.com/blog/nipah-submissions/", "snippet": "After a busy few weeks with over 680 protein designers submitting their best
binder designs against the surface glycoprotein of the Nipah virus, the submissions and community vote doors have closed and we are waiting in anticipation for the experimental results to arrive. In
the meantime, we want to highlight some interesting new insights and cool protein structures that we have gathered during the course of this competition.\nLet\u2019s start with a quick recap: Nipah is
one of the deadliest viruses ", "api_data": null, "hint": null}, {"title": "Winning the de novo portion of the Adaptyv Nipah binder competition", "url": "https://blog.escalante.bio/winning-the-de-
novo-portion-of-the-adaptyv-nipah-binder-competition/", "snippet": "Winning the de novo portion of the Adaptyv Nipah binder competition\n![Winning the de novo portion of the Adaptyv Nipah binder
competition](/content/images/size/w2000/2026/01/MODEL.png)\nThe Adaptyv Nipah binder competition recently [released results](https://proteinbase.com/collections/nipah-binder-competition-
results?ref=blog.escalante.bio). If you're not familiar with it, the objective was to design protein binders to the Nipah virus G protein. Designs were tested in the wetlab and ranked solel",
"api_data": null, "hint": null}]}
```

```json
{
  "query": "computational protein binder design success rate 2025 2026 state of art improvement"
}
```

### 📋 Result

```
{"query": "computational protein binder design success rate 2025 2026 state of art improvement", "results": [{"title": "PXDesign: Fast, Modular, and Accurate De Novo Design of Protein Binders |
bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2025.08.15.670450v3.full", "snippet": null, "api_data": null, "hint": null}, {"title": "Code to complex: AI-driven de novo binder design:
Structure", "url": "https://www.cell.com/structure/fulltext/S0969-2126(25)00311-9", "snippet": null, "api_data": null, "hint": null}, {"title": "Improving de novo protein binder design with deep
learning | Nature Communications", "url": "https://www.nature.com/articles/s41467-023-38328-5", "snippet": "Abstract\nRecently it has become possible to de novo design high affinity protein binding
proteins from target structural information alone. There is, however, considerable room for improvement as the overall design success rate is low. Here, we explore the augmentation of energy-based
protein binder design using deep learning. We find that using AlphaFold2 or RoseTTAFold to assess the probability that a designed sequence adopts the designed monomer structure, and the probability
that this struct", "api_data": null, "hint": null}, {"title": "Code to complex: AI-driven de novo binder design - ScienceDirect", "url":
"https://www.sciencedirect.com/science/article/pii/S0969212625003119", "snippet": null, "api_data": null, "hint": null}, {"title": "Predicting Experimental Success in De Novo Binder Design: A Meta-
Analysis of 3,766 Experimentally Characterised Binders | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2025.08.14.670059v1.full", "snippet": null, "api_data": null, "hint": null},
{"title": "Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design", "url": "https://arxiv.org/html/2507.19375v1", "snippet": "Latent-X: An Atom-level Frontier Model for De Novo
Protein Binder Design\nAbstract\nTraditional drug discovery relies on rounds of screening millions of candidate molecules with low success rates, making drug discovery time and resource intensive. To
overcome this screening bottleneck, we introduce Latent-X, an all-atom protein design model that enables a new paradigm of precision AI design. Given a target protein epitope, Latent-X jointly
generates the all atom structure and sequence of the prote", "api_data": null, "hint": null}, {"title": "Proteina-Complexa: Scaling Atomistic Protein Binder Design with Generative Pretraining and
Test-Time Compute | Research", "url": "https://research.nvidia.com/publication/2026-01_proteina-complexa-scaling-atomistic-protein-binder-design-generative", "snippet": "Proteina-Complexa: Scaling
Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute\n![Publication image Publication
image](/sites/default/files/styles/wide/public/default_images/default.jpeg?itok=gopAYWUX)\nProtein interaction modeling is central to protein design, which has been transformed by machine learning
with applications in drug discovery and beyond. In this landscape, structure-based de novo binder design is cast as either conditional generative modeling or seque", "api_data": null, "hint": null},
{"title": "One-shot design of functional protein binders with BindCraft | Nature", "url": "https://www.nature.com/articles/s41586-025-09429-6", "snippet": "Abstract\nProtein\u2013protein interactions
are at the core of all key biological processes. However, the complexity of the structural features that determine protein\u2013protein interactions makes their design challenging. Here we present
BindCraft, an open-source and automated pipeline for de novo protein binder design with experimental success rates of 10\u2013100%. BindCraft leverages the weights of AlphaFold2 (ref.
[1](https://www.nature.com/articles/s41586-025-09429-6#ref-CR1)) to generate binders with n", "api_data": null, "hint": null}, {"title": "Improving de novo protein binder design with deep learning -
PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10163288/", "snippet": "Abstract\nRecently it has become possible to de novo design high affinity protein binding proteins from target structural
information alone. There is, however, considerable room for improvement as the overall design success rate is low. Here, we explore the augmentation of energy-based protein binder design using deep
learning. We find that using AlphaFold2 or RoseTTAFold to assess the probability that a designed sequence adopts the designed monomer structure, and the probability that this struct", "api_data":
null, "hint": null}, {"title": "Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute | OpenReview", "url": "https://openreview.net/forum?id=qmCpJtFZra", "snippet":
"Keywords: binder design, protein design, flow matching, hallucination, inference-time scaling, generative modeling, diffusion models\nTL;DR: We introduce a novel method for state-of-the-art
structure-based protein binder design that combines flow matching-based generative pretraining with inference-time compute scaling techniques.\nAbstract: Protein interaction modeling is central to
protein design, which has been transformed by machine learning with applications in drug discovery and beyond. In t", "api_data": null, "hint": null}]}
```

```json
{
  "query": "AlphaProteo BindCraft RFdiffusion protein binder design success rate improvement 2025 2026"
}
```

### 📋 Result

```
[{"title": "Improved protein binder design using \u03b2-pairing targeted RFdiffusion | Nature Communications", "url": "http://www.nature.com/articles/s41467-025-67866-3", "snippet": "Improved protein
binder design using \u03b2-pairing targeted RFdiffusion | Nature Communications\n\nDownload PDF\n\n### Subjects\n\n- X-ray crystallography\n- Protein design\n- Kinetics\n\n## Abstract\n\nDesigning
proteins that bind with high affinity to hydrophilic protein target sites remains a challenging problem. Here we show that RFdiffusion can be conditioned to generate protein scaffolds that form
geometrically matched extended \u03b2-sheets with target protein edge \u03b2-strands in which polar groups on the targe", "highlights": ["that bind with high affinity to hydrophilic protein target
sites remains a challenging problem. Here we show that RFdiffusion can be conditioned to generate protein scaffolds that form geometrically matched extended   ...    groups on the design. We use this
approach to design binders against edge-strand target sites on KIT, PDGFR\u0251, ALK-2, ALK-3, FCRL5, NRP1, and \u03b1-CTX, and obtain higher (pM to mid nM) affinities and success rates than
unconditioned RFdiffusion. Despite sharing \u03b2-strand interactions, designs have high specificity, reflecting the precise customization   ...    is nearly identical to the design model, confirming
the accuracy of the design approach. The ability to robustly   ...    timesteps (t), with the tertiary fold determined within 5 timesteps and the final output at t = 50. c Binder design success rates
using \u03b2-strand interface conditioning or RFdiffusion default settings with hotspots indicating the target   ...    indicated in the legend. Bold bordered data points indicate in silico successes
(red circles, pAE interaction <10,   ...    of the TGF-\u03b2 superfamily 57, and KIT and PDGFR\u0251 are type-III receptor-tyrosine kinases 58(Supplementary Fig. 2). In a first in silico benchmark
experiment, we compared the diversity and quality of binders designed using our   ...    generated for each scaffold by ProteinMPNN 59 and each binder candidate complex was predicted with AlphaFold 2
54. Across all eight target sites across the seven target proteins (two sites were targeted for PDGFR\u0251 due to predicted structural variability), \u03b2-strand interface conditioning yielded
design models with improved in silico binding metrics 6 AlphaFold 2 interface predicted aligne  d error (pAE) and Rosetta \u0394\u0394G (Fig. 1b), with over 9.2% of \u03b2-strand interface conditioned
designs meeting reasonable quality metrics, in contrast to 0.98% success rates by RFdiffusion conditioned on target hotspots alone. \u03b2-strand interface conditioning yielded in silico design
successes for all targets, whereas hotspot conditioning alone did not yield any in silico successes for two targets (ALK-3 and FCRL5). \u03b2-strand interface conditioning also yielded more globular
binder designs with 88.7%  outperformed other scaffold types in this in silico   ...    helical bundle binder design success due to its flat, hydrophobic surface (Supplementary Fig. 2b). Structurally
diverse designs with high AlphaFold 2 confidence (interface pAE <8 and pLDDT > 85) designs were selected for experimental screening by yeast surface display. While we ordered libraries including
thousands of designs for  some targets (KIT, PDGFR\u0251, FCRL5, ALK-2, and ALK-3), binder success rates in our screen suggested that it would be possible to design strand pairing binders at smaller
scales (Supplementary Table 1). Indeed, design sets for NRP1 and \u03b1-CTX yielded   ...    yield binders for ALK-3 (see Data Availability). The difficulty of designing binders to these targets is
demonstrated   ...    motif specified by interface conditioning.  \u03b2-strand interface conditioned RFdiffusion resulted in a 5-fold improved in silico success rate for these targets compared to
hotspot directed RFdiffusion which, even without conditioning, generated \u03b2-strand pairing binder designs with up to 20% of outputs (\u03b2-strand pairing designs were generated <5% of the time
for the less exposed edge strand containing targets). Binders for \u03b1-CTX (originally introduced by Vazques-Torres, et. al.) and NRP1 (1.9 nM and 101 nM, respectively) were obtained by  binders may
selectively induce the cognate PDGFR\u0251   ...    pairing h-bond network highlights the power of \u03b2-pairing conditioned RFdiffusion to design complex \u03b2-strand  We show through in silico
modeling and high throughput binding assays that \u03b2-strand interface conditioned RFdiffusion outperforms alpha-helical focused methods for the design of binders against seven edge \u03b2-strand
containing targets. The binders are thermostable and target-specific, and the crystal structure of the KITbp:KIT complex shows the method has high structural accuracy. The higher success rate of
binder design against polar targets containing \u03b2-sheets using the \u03b2-pairing targeted  Our \u03b2-strand targeted RFdiffusion approach should enable facile binder design against many   ...
## About this article\n\n### Cite this article Sappington, I., Toul, M., Lee, D.S. et al. Improved protein binder design using \u03b2-pairing targeted RFdiffusion. Nat Commun 17, 1101 (2026).
https://doi.org/10.1038/s41467-025-67866-3 Download citation\n\nReceived: 20 December 2024\n\nAccepted: 10 December 2025"], "published_date": "2026-01-10T00:00:00.000", "score": null}, {"title": "One-
shot design of functional protein binders with BindCraft - Nature", "url": "https://www.nature.com/articles/s41586-025-09429-6", "snippet": "One-shot design of functional protein binders with
BindCraft | Nature\n\n### Subjects\n\n## Abstract\n\nProtein\u2013protein interactions are at the core of all key biological processes. However, the complexity of the structural features that
determine protein\u2013protein interactions makes their design challenging. Here we present BindCraft, an open-source and automated pipeline for de novo protein binder design with experimental success
rates of 10\u2013100%. BindCraft leverages the weights of AlphaFold2 (ref. 1)", "highlights": ["we present BindCraft, an open-source and automated pipeline for de novo protein binder design with
experimental success rates of 10\u2013100%.   ...    ### Improved protein binder design using \u03b2-pairing targeted RFdiffusion   ...    proteins and binders. The current state-of-the-art methods
involve the use of RFdiffusion 5 for backbone generation coupled with ProteinMPNN sequence generation 6. When applied to binder design, this approach shows significantly improved success rates
compared with previous methods 5. However, RFdiffusion relies on sequence design over   ...    Given the use of AF2 in improving binder filtering success, we proposed that we could harness it directly
for the design of protein binders. We present BindCraft, a user-friendly pipeline for de novo design of protein binders that   ...    network to efficiently hallucinate new binders and interfaces
(Fig. 1a). We demonstrate the efficiency of our pipeline   ...    the predicted designs based on AF2 confidence metrics, as well as Rosetta physics-based scoring metrics (Methods). Each target shows
varying levels of in silico design success, with 16.8\u201362.7% of initial AF2 trajectories showing satisfactory confidence metrics and 0.6\u201365.9% of MPNNsol-optimized designs passing the final
computational filters after AF2 monomer complex reprediction (Supplementary Fig. 1e). In silico design success rates are dependent on the target protein and the length of binders being generated
(Supplementary Fig. 1f). When compared to the state-of-the-art binder design approach RFdiffusion 5, BindCraft yields similar success rates in terms of generation time across several targets and
binder lengths (Extended Data Fig. 1c). Notably, we observe a difference in amino acid distribution at the binder interface, with an underrepresentation of bulky amino acids in RFdiffusion-generated
designs (Extended Data Fig. 1d). We benchmarked BindCraft on 12 targets to assess its generalizability (Fig. 1b). The designs show broad sequence and   ...    critical for capturing binding-induced
structural changes essential for molecular recognition.  We demonstrate BindCraft\u2019s performance across a diverse set of 12 challenging targets. The binder affinities lie predominantly in the
nanomolar range, with success rates from 10% to 100%, with an average success rate of 46.3%, which is remarkable for a purely computational approach. These rates allow for the screening of far fewer
designs experimentally to identify functioning binders, when compared with the current state-of the-art RFdiffusion 5 and the recently described closed-source  AlphaProteo binder design pipeline 45.
Notably, a binder designed with our pipeline recently ranked first in a community-wide binder design competition, showing 82 nM affinity against the challenging epidermal growth factor receptor (EGFR)
target 46.  Despite the successes outlined here, there are limitations to the BindCraft design approach. Backpropagation through AF2 is GPU-intensive, and final design filtering with AF2 monomer in
single sequence mode may exclude prospective high-affinity binders2,3,4, 5, 48(Extended Data Fig. 7a,b). We assessed the possibility of   ...    generated for each instance using otherwise default
settings.  For benchmarks involving design and trajectory success   ...    and target are designated \u2018low confidence\u2019.  RFdiffusion benchmarks were performed as described in the original
...    predicted using AF2 monomer model 1 and two MPNN designed sequences for each backbone were  Benchmarking of designs from other design pipelines was performed using the BindCraft prediction
method of either AF2 monomer or multimer in   ...    AlphaFold3 predictions of designed BindCraft complexes were performed using the AlphaFold3 server 49 with   ...    optimization in a relaxed
sequence space. Science 386, 439\u2013445 (2024). Jendrusch, M. A. et al. AlphaDesign: a de novo protein design framework based on AlphaFold. Mol. Syst. Biol.
https://doi.org/10.1038/s44320-025-00119-z(2025).   ...    Learning Representations (ICLR, Vienna, 2024).  Zambaldi, V. et al. De novo design of high-affinity protein binders with AlphaProteo.
Preprint at https://arxiv.org/abs/2409.08022(2024). Cotet, T.-S. et al. Crowdsourced protein design: lessons from the adaptyv EGFR binder competition. Preprint at bioRxiv
https://doi.org/10.1101/2025.04.17."], "published_date": "2025-08-27T00:00:00.000", "score": null}, {"title": "BindCraft : analysing a full design run \u2013 Protein binder design workshop:
RFdiffusion and BindCraft", "url": "https://australian-protein-design-initiative.github.io/binder-design-workshop/bindcraft_scoring.html", "snippet": "BindCraft : analysing a full design run \u2013
Protein binder design workshop: RFdiffusion and BindCraft\n\n \n\n \n\n \n\nWe\u2019ve run 400 BindCraft trajectories for PDL1 using`nf-binder-design`- the results are
in`/scratch2/pd27/shared/examples/nfbd/pdl1-bindcraft`- this reflects a more realistic number of trajectories for a \u2018production run\u2019.\n\nCautionChallenge - viewing the BindCraft
results\n\nView the table`final_design_stats.csv`- how many accepted designs do we have ? What is the acceptance rate ?\n\nWhat do ", "highlights": ["BindCraft : analysing a full design run \u2013
Protein binder design workshop: RFdiffusion and BindCraft We\u2019ve run 400 BindCraft trajectories for PDL1 using`nf-binder-design`- the results are
in`/scratch2/pd27/shared/examples/nfbd/pdl1-bindcraft`- this reflects a more realistic number of trajectories for a   ...    View the table`final_design_stats.csv`- how many accepted designs do we
have ? What is the acceptance rate ?   ...    BindCraft outputs many scores, but for ranking designs we\u2019d typically focus on: - `Average_i_pTM`- the average ipTM across each Alphafold2 model for
this complex Note that since fairly stringent filters have already been applied, any of the Accepted designs is considered to have a good chance of binding. Here are all the scores you\u2019ll find in
the`final_design_stats.csv` file. The 1_, 2_, 3_, etc scores are for each   ...    Average_pLDDT,          1_pLDDT,2_pLDDT,3_pLDDT,4_pLDDT,5_pLDDT,   ...
DesignTime,Notes,TargetSettings,Filters,AdvancedSettings\n```\n\n#### Default filters Designs that satisfy these criteria are kept as \u2018Accepted\u2019:\n\nAlphaFold2 Metrics - `Average_pLDDT`>
0.8\n- `Average_pTM`> 0.55\n- `Average_i_pTM`> 0.5\n- `Average_i_pAE`< 0.35\n\nRosetta Metrics - `Average_Binder_Energy_Score`< 0\n- `Average_Surface_Hydrophobicity`< 0.35\n-
`Average_ShapeComplementarity`> 0.6 - `Average_dG`< 0\n- `Average_dSASA`> 1\n- `Average_n_InterfaceResidues`> 7\n- `Average_n_InterfaceHbonds`> 3 - `Average_n_InterfaceUnsatHbonds`< 4\n-
`Average_InterfaceAAs: K`< 3\n- `Average_InterfaceAAs: M`< 3   ...    - `Average_Binder_Loop%`< 90\n- `Average_Hotspot_RMSD`< 6\n- `Average_Binder_pLDDT`> 0.8\n- `Average_Binder_RMSD`< 3.5 #
Optimizing BindCraft settings\n\nIt can take \u2018many shots\u2019 in silico to get a \u2018one shot\u2019 binder in the wet lab. Here\u2019s a figure from the BindCraft paper that gives some
insight:\n\n\u2019 Each target required different numbers of trajectories, with a wide range in in silico acceptance rates, to achieve the suggested \u201c100 accepted designs to select 20 for
assay\u201d benchmark. Part f shows the impact of binder length range alone on in silico success rates. What we don\u2019t see here is the trajectories run testing alternative target structures,
trimmings and hotspot combinations - expect to run many more trajectories than you\u2019ll ultimately require for your final \u2018production\u2019 run. The two key parameters you should adjust to get
more \u2018accepted\u2019 designs are:   ...    Modifying the default filters or advanced settings should typically be approached with extreme caution - not all \u2018advanced\u2019 settings have been
systematically tested and may reduce the success rates reported in the BindCraft"], "published_date": null, "score": null}, {"title": "", "url":
"https://www.nature.com/articles/s41586-025-09429-6.pdf", "snippet": "Nature | Vol 646 | 9 October 2025 | 483\nArticle\nOne-shot design of functional protein binders \nwith BindCraft\nMartin
Pacesa1,10\u2009\u2709, Lennart Nickel1,2,10, Christian Schellhaas1,2,10, Joseph Schmidt1, \nEkaterina Pyatova1\n, Lucas Kissling3, Patrick Barendse4, Jagrity Choudhury5, Srajan Kapoor5, \nAna
Alcaraz-Serna6\n, Yehlin Cho7, Kourosh H. Ghamary8, Laura Vinu\u00e98, Brahm J. Yachnin8, \nAndrew M. Wollacott8\n, Stephen Buckley1, Adrie H. Westphal4, Simon Lindhoud4, \nSandrine Georgeon1\n,
Casper A. Goverde1", "highlights": ["Protein\u2013protein interactions are at the core of all key biological processes. However, the   ...    their design challenging. Here we present BindCraft, an
open-source and automated pipeline for de\u00a0novo protein binder design with experimental success rates of 10\u2013100%. BindCraft leverages the weights of AlphaFold2 (ref. 1) to generate binders
with nanomolar   ...    . Deep learning has also been success\u0002fully applied for de\u00a0novo design of proteins and binders. The current state-of-the-art methods involve the use of RFdiffusion5
for backbone generation coupled with ProteinMPNN sequence generation6. When applied to binder design, this approach shows significantly improved success rates compared with previous methods5. However,
RFdiffusion relies on sequence design over side-chain-free backbones placed at a   ...    Given the use of AF2 in improving binder filtering success, we pro\u0002posed that we could harness it
directly for the design of protein bind\u0002ers. We present BindCraft, a user-friendly pipeline for de\u00a0novo design   ...    https://doi.org/10.1038/s41586-025-09429-6\nReceived: 7 December
2024\nAccepted: 17 July 2025   ...    (Fig.\u00a01a). We demonstrate the efficiency of our pipeline on 12 diverse,   ...    interface concurrently (Fig.\u00a01a). In contrast to methods such as
RFdif\u0002fusion5 or RIFdock2,4, which keep the target backbone fixed during   ...    We use AF2 multimer11 for designing initial binders, as this version   ...    model wei  16.8\u201362.7% of
initial AF2 trajectories showing satisfactory confidence metrics and 0.6\u201365.9% of MPNNsol-optimized designs passing the final computational filters after AF2 monomer complex reprediction
(Sup\u0002plementary Fig.\u00a01e). In silico design success rates are dependent on the target protein and the length of binders being generated (Supple\u0002mentary Fig.\u00a01f). When compared to
the state-of-the-art binder design approach RFdiffusion5, BindCraft yields similar success rates in terms  of generation time across several targets and binder lengths (Extended Data Fig.\u00a01c).
Notably, we observe a difference in amino acid distribution at the binder interface, with an underrepresentation of bulky amino acids in RFdiffusion-generated designs (Extended Data Fig.\u00a01d). We
benchmarked BindCraft on 12 targets to assess its generalizability   ...    changes essential for molecular recognition.\nWe demonstrate BindCraft\u2019s performance across a diverse set of 12
challenging targets. The binder affinities lie predominantly in the  nanomolar range, with success rates from 10% to 100%, with an aver\u0002age success rate of 46.3%, which is remarkable for a purely
computa\u0002tional approach. These rates allow for the screening of far fewer designs experimentally to identify functioning binders, when compared with the current state-of the-art RFdiffusion5 and
the recently described closed-source AlphaProteo binder design pipeline45. Notably, a binder designed with our pipeline recently ranked first in a community-wide  2. Cao, L. et\u00a0al. Design of
protein-binding   ...    605, 551\u2013560 (2022).\n3. Gainza, P. et\u00a0al. De\u00a0novo design of protein interactions with learned surface fingerprints. Nature 617, 176\u2013184 (2023).\n4.
Bennett, N. R. et\u00a0al. Improving de\u00a0novo protein binder design with deep learning. Nat. Commun. 14, 2625 (2023). 5. Watson, J. L. et\u00a0al. De\u00a0novo design of protein structure and
function with RFdiffusion. Nature 620, 1089\u20131100 (2023).  6. Dauparas, J. et\u00a0al. Robust deep learning\u2013based protein sequence design using   ...    For benchmarks involving design and
trajectory success rates, we   ...    \u2018passing\u2019, whereas tra\u0002jectories that have a pLDDT below 0.7, more than 1 C\u03b1 backbone clash between chains or fewer than 3 contacts between
the binder and target \nare designated \u2018low confidence\u2019. RFdiffusion benchmarks were performed as described in the original publication5, with the exception of running the pipeline in
deterministic mode for tracking purposes. Briefly, backbones of designated lengths  were sampled using RFdiffusion against selected targets and sequences were designed using original ProteinMPNN
weights with a temperature of 0.0001 and 8 sequences per backbone. Each complex was predicted using AF2 monomer model 1 and two MPNN designed sequences for   ...    publication (pLDDT\u2009>\u20090.8,
i_pAE\u2009<\u20090.32, binder r.m.s.d.\u2009<\u20091.0\u2009\u00c5). The pipeline was run until 100 designs passed filters. The computational  for Sp"], "published_date": null, "score": null},
{"title": "One-shot design of functional protein binders with BindCraft | Nature", "url": "https://preview-www.nature.com/articles/s41586-025-09429-6", "snippet": "One-shot design of functional
protein binders with BindCraft | Nature\n\nDownload PDF\n\n### Subjects\n\n- Protein design\n- Biochemistry\n\n## Abstract\n\nProtein\u2013protein interactions are at the core of all key biological
processes. However, the complexity of the structural features that determine protein\u2013protein interactions makes their design challenging. Here we present BindCraft, an open-source and automated
pipeline for de novo protein binder design with experimental success rates of 10\u2013100%. BindCra", "highlights": ["we present BindCraft, an open-source and automated pipeline for de novo protein
binder design with experimental success rates of 10\u2013100%.   ...    ### Improved protein binder design using \u03b2-pairing targeted RFdiffusion   ...    proteins and binders. The current state-
of-the-art methods involve the use of RFdiffusion 5 for backbone generation coupled with ProteinMPNN sequence generation 6. When applied to binder design, this approach shows significantly improved
success rates compared with previous methods 5. However, RFdiffusion relies on sequence design over   ...    design of protein binders. We present BindCraft, a user-friendly pipeline for de novo
design of protein binders that   ...    network to efficiently hallucinate new binders and interfaces (Fig. 1a). We demonstrate the efficiency of our pipeline   ...    the predicted designs based on
AF2 confidence metrics, as well as Rosetta physics-based scoring metrics (Methods). Each target shows varying levels of in silico design success, with 16.8\u201362.7% of initial AF2 trajectories
showing satisfactory confidence metrics and 0.6\u201365.9% of MPNNsol-optimized designs passing the final computational filters after AF2 monomer complex reprediction (Supplementary Fig. 1e). In
silico design success rates are dependent on the target protein and the length of binders being generated (Supplementary Fig. 1f). When compared to the state-of-the-art binder design approach
RFdiffusion 5, BindCraft yields similar success rates in terms of generation time across several targets and binder lengths (Extended Data Fig. 1c). Notably, we observe a difference in amino acid
distribution at the binder interface, with an underrepresentation of bulky amino acids in RFdiffusion-generated designs (Extended Data Fig. 1d). We benchmarked BindCraft on 12 targets to assess its
generalizability (Fig. 1b). The designs show broad sequence and   ...    molecular recognition.  We demonstrate BindCraft\u2019s performance across a diverse set of 12 challenging targets. The binder
affinities lie predominantly in the nanomolar range, with success rates from 10% to 100%, with an average success rate of 46.3%, which is remarkable for a purely computational approach. These rates
allow for the screening of far fewer designs experimentally to identify functioning binders, when compared with the current state-of the-art RFdiffusion 5 and the recently described closed-source
AlphaProteo binder design pipeline 45. Notably, a binder designed with our pipeline recently ranked first in a community-wide binder design competition, showing 82 nM affinity against the challenging
epidermal growth factor receptor (EGFR) target 46.  Despite the successes outlined here, there are limitations to the BindCraft design approach. Backpropagation through AF2 is GPU-intensive, and final
design filtering with AF2 monomer in single sequence mode may exclude prospective high-affinity binders2,3,4, 5, 48(Extended Data Fig. 7a,b). We assessed the possibility of using the recently released
AlphaFold3 (ref. 49) model for filtering,   ...    generated for each instance using otherwise default settings.  For benchmarks involving design and trajectory success   ...    and target are
designated \u2018low confidence\u2019.  RFdiffusion benchmarks were performed as described in the original   ...    predicted using AF2 monomer model 1 and two MPNN designed sequences for each
backbone were  Benchmarking of designs from other design pipelines was performed using the BindCraft prediction method of either AF2 monomer or multimer in   ...    Jendrusch, M. A. et al.
AlphaDesign: a de novo protein design framework based on AlphaFold. Mol. Syst. Biol. https://doi.org/10.1038/s44320-025-00119-z(2025).   ...    Learning Representations (ICLR, Vienna, 2024).
Zambaldi, V. et al. De novo design of high-affinity protein binders with AlphaProteo. Preprint at https://arxiv.org/abs/2409.08022(2024). Cotet, T.-S. et al. Crowdsourced protein design: lessons from
the adaptyv EGFR binder competition. Preprint at bioRxiv https://doi.org/10.1101/2025.04.17"], "published_date": "2025-08-27T00:00:00.000", "score": null}, {"title": "BindCraft: one-shot design of
functional protein binders | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2024.09.30.615802v1", "snippet": "# BindCraft: one-shot design of functional protein binders\n\n- Bruno E.
Correia\n- Sergey Ovchinnikov\n- Gerald Schwank\n- Yannick D. Muller\n- Pierre G\u00f6nczy\n- Georgios N. Hatzopoulos\n- Casper A. Goverde\n- Sandrine Georgeon\n- Stephen Buckley\n- Andrew M.
Wollacott\n- Brahm J. Yachnin\n- Laura Vinu\u00e9\n- Kourosh H. Ghamary\n- Yehlin Cho\n- Ana Alcaraz-Serna\n- Lucas Kissling\n- Christian Schellhaas\n- Ekaterina Pyatova\n- Joseph Schmidt\n- Lennart
Nickel\n- Martin Pacesa\n\n## Abstract\n\nProtein\u2013protein interactions (", "highlights": ["Protein\u2013protein interactions (PPIs) are at the core of all key biological processes. However, the
complexity of the structural features that determine PPIs makes their design challenging. We present BindCraft, an open-source and automated pipeline for de novo protein binder design with
experimental success rates of 10-100%. BindCraft leverages the trained deep learning weights of AlphaFold21 to generate nanomolar binders without the need for high-throughput   ...    Recent
breakthroughs in deep learning have revolutionized the field of biomolecular modelling, particularly the   ...    and modeling complex PPIs. Indeed, AF2 filtering has been shown to significantly
increase the success rates of binder design by evaluating the plausibility of predicted complexes10,11. Deep learning has also been successfully applied for de novo design of proteins and binders. The
current state-of-the-art methods involve the use of RFdiffusion10 for plausible backbone generation coupled with ProteinMPNN sequence generation13,14. When applied to binder design, this approach has
successfully designed binders against a variety of protein targets, with improved success rates compared to previous methods10. However, this requires the generation of thousands to tens of thousands
designs in silico and   ...    Given the utility of AF2 in improving binder filtering success, we hypothesized that we could harness its trained weights and learned patterns of protein structures
directly for the design of protein binders. We present BindCraft, a   ...    interfaces without the need for extensive sampling (Fig. 1a). We demonstrate the efficiency of our pipeline on ten   ...
concurrently (Fig. 1a). Unlike other design methods, such as RFdiffusion10 or RIFdock7,11, which keep the target   ...    recognition.  Our results demonstrate the effectiveness of BindCraft in
designing binders against a diverse set of 10 challenging targets. The binder affinities lie predominantly in the nanomolar range, with one at the \u03bcM level, and one binder displaying an apparent
Kd even in the subnanomolar range (with avidity). The success rates range from 24.5 to 100%, with an average success rate of 49.5%, which is remarkable for designs resulting from a purely
computational approach. These rates allow for the  screening of far fewer designs experimentally to identify functioning binders, when compared to the current state of the art RFdiffusion10 and the
recently described closed-source AlphaProteo binder design pipeline37. Notably, a binder design from our pipeline recently ranked first in an international binder design competition, displaying
nanomolar affinity against the challenging EGFR target. However, we do expect success rates to vary based on the target protein and binding site.  One of the main challenges of PPI design is the
choice of a favorable target site7,11,38. Prototypical binding sites are often composed of hydrophobic patches with mostly flat   ...    CRISPR-Cas nucleases. In the absence of a defined target
epitope, BindCraft is able to  Despite the design successes outlined here, there are limitations to the BindCraft design approach. Backpropagation through the AF2 network requires   ...    design.
Additionally, since we utilize AF2 monomer in single sequence mode for filtering, it is possible that we reduced in silico design success rates. We hope to improve upon this concept to potentially
generate nanobody-based   ...    19. 39.Pak, M. A. et al. Using AlphaFold to predict the impact of single mutations on protein stability and function.   ...    21. 37.Zambaldi, V., et al. De novo
design of high-affinity protein binders with AlphaProteo. arXiv (2024) doi:10.48550/arxiv.2409.08022. CrossRef  43. 15.Evans, R., et al. Protein complex prediction with AlphaFold-Multimer. Biorxiv
2021.10.04.463034 (2022) doi:10.1101/2021.10.04.463034. Abstract/FREE Full Text 44. 14.Wicky, B. I. M. et al. Hallucinating symmetric protein assemblies. Science 0, eadd1964 (2022).   ...    47.
11.Bennett, N. R. et al. Improving de novo protein binder design with deep learning. Nat Commun 14, 2625 (2023). CrossRef 48. 10.Watson, J. L. et al. De novo design of protein structure and function
with RFdiffusion. Nature 1\u20133 (2023) doi:10.1038/s41586-023-06415-8. CrossRef  49. 9.Chevalier, A. et al. Massively parallel de novo protein design for targeted therapeutics. Nature 550,
74\u201379 (2017"], "published_date": null, "score": null}, {"title": "One-shot design of functional protein binders with BindCraft - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/40866699/",
"snippet": "One-shot design of functional protein binders with BindCraft - PubMed\n\nSave Email\n\nSend to\n\nDisplay options\n\nFull text links Cite\n\nDisplay options\n\n## Abstract\n\nProtein-
protein interactions are at the core of all key biological processes. However, the complexity of the structural features that determine protein-protein interactions makes their design challenging.
Here we present BindCraft, an open-source and automated pipeline for de novo protein binder design with experimental success rates of ", "highlights": ["Protein-protein interactions are at the core of
all key biological processes. However, the complexity of the structural features that determine protein-protein interactions makes their design challenging. Here we present BindCraft, an open-source
and automated pipeline for de novo protein binder design with experimental success rates of 10-100%. BindCraft leverages the weights of AlphaFold2 (ref. 1) to generate binders with nanomolar affinity
without the need for high-throughput screening or experimental optimization, even in the absence of known binding sites. We successfully   ...    cell-surface-receptor-specific binders to redirect
adeno-associated virus capsids for targeted gene delivery. This work represents a significant advancement towards a 'one design-one binder' approach in computational design, with immense   ...    were
excluded. Values in the blue box indicate the number of successful designs, where binding was observed on SPR   ...    beta-sheeted binders. c, Number of GPU hours elapsed to generate 100 binder
designs passing computational filters across different binder lengths and targets. Numbers above bars indicate the number of designs that needed to be sampled. Filtering conditions for BindCraft and
RFdiffusion are described in Methods. d, Amino acid type distribution   ...    by APC-conjugated antibodies. Panel a was created using BioRender (https://biorender.com). Extended Data Fig. 7.
Benchmarking prediction accuracy across design pipelines. Experimentally validated binders and non-binders from previously published binder design pipelines have been repredicted using the BindCraft
prediction pipeline with either AF2 a, monomer (default) or b, multimer models. Of note, EvoPro and RFdiff designs have been already prefiltered by AF2 monomer in their respective publications, and
indicate the presence of false positives. RIFdock and Masif-seed, designs were not prefiltered by AF2. The centre line in box plots represents the median of the data (50th percentile), the box spans
the 25th and 75th percentiles of the data. The whiskers show the minimum and maximum values of the distribution. Outliers (circles) are data points that fall outside the 1.5 interquartile range. c,
The i_pTM values of AlphaFold2 and AlphaFold3 predictions of   ...    All figures (12)\n\nSee this image and copyright information in PMC\n\n## Update of BindCraft: one-shot design of functional
protein binders. Pacesa M, Nickel L, Schellhaas C, Schmidt J, Pyatova E, Kissling L, Barendse P, Choudhury J, Kapoor S, Alcaraz-Serna A, Cho Y, Ghamary KH, Vinu\u00e9 L, Yachnin BJ, Wollacott AM,
Buckley S, Westphal AH, Lindhoud S, Georgeon S, Goverde CA, Hatzopoulos GN, G\u00f6nczy P, Muller YD, Schwank G, Swarts DC, Vecchio AJ, Schneider BL, Ovchinnikov S, Correia BE. Pacesa M, et al.
bioRxiv [Preprint]. 2025 Apr 25:2024.09.30.615802. doi: 10.1101/2024.09.30.615802. bioRxiv. 2025. Update in: Nature. 2025 Oct;646(8084):483-492. doi: 10.1038/s41586-025-09429-6. PMID: 39677777 Free
PMC article. Updated.   ...    1. Bennett, N. R. et al. Improving de novo protein binder design with deep learning. Nat. Commun.14, 2625 (2023). - DOI- PMC- PubMed 1. Watson, J. L. et al. De novo
design of protein structure and function with RFdiffusion. Nature620, 1089\u20131100 (20"], "published_date": null, "score": null}, {"title": "", "url":
"https://www.biorxiv.org/content/10.1101/2024.09.30.615802v3.full.pdf", "snippet": "1\nBindCraft: one-shot design of functional protein binders\nMartin Pacesa1\u2021, Lennart Nickel1,2\u2021,
Christian Schellhaas1,2\u2021, Joseph Schmidt1, \nEkaterina Pyatova1, Lucas Kissling3, Patrick Barendse4 , Jagrity Choudhury5 , Srajan \nKapoor5, Ana Alcaraz-Serna6, Yehlin Cho7, Kourosh H. Ghamary8,
Laura Vinu\u00e98, Brahm \nJ. Yachnin8, Andrew M. Wollacott8, Stephen Buckley1, Adrie H. Westphal4 , Simon \nLindhoud4, Sandrine Georgeon1, Casper A. Goverde1, Georgios N. Hatzopoulos9, Pierre
\nG\u00f6nczy9, Yannick D. Mull", "highlights": ["preprint doi: https://doi.org/10.1101/2024.09.30.615802; this version posted April 25, 2025. The copyright   ...    2\nAbstract:\nProtein\u2013protein
interactions (PPIs) are at the core of all key biological processes.   ...    challenging. We present BindCraft, an open-source and automated pipeline for de novo protein binder design with
experimental success rates of 10-100%. BindCraft leverages the weights of AlphaFold21 to generate binders with nanomolar affinity without the need   ...    bioRxiv preprint doi:
https://doi.org/10.1101/2024.09.30.615802; this version posted April 25, 2025. The copyright   ...    biomolecular modelling, particularly the prediction of protein structure. Models like AlphaFold2
(AF2)1 and RoseTTAFold2 (RF2)12, trained on large protein structure and   ...    protein structures and modeling complex PPIs. Indeed, AF2 filtering has been shown to significantly increase the
success rates of binder design by evaluating the plausibility of predicted complexes10,11. Deep learning has also been successfully applied for de novo design of proteins and binders. The current
state-of-the-art methods involve the use of RFdiffusion10 for backbone generation coupled with ProteinMPNN sequence generation13,14. When applied to binder design, this approach has successfully
designed binders against a variety of protein targets, with improved success rates compared to previous methods10. However, it requires the generation of thousands to tens of   ...    bioRxiv preprint
doi: https://doi.org/10.1101/2024.09.30.615802; this version posted April 25, 2025. The copyright   ...    design of protein binders. We present BindCraft, a user-friendly pipeline for de novo   ...
1a). We demonstrate the efficiency of our pipeline on twelve diverse, challenging, and   ...    concurrently (Fig. 1a). Unlike other design methods, such as RFdiffusion10 or RIFdock7,11,   ...
essential for effective molecular recognition. Our results demonstrate the performance of BindCraft in designing binders against a diverse set of 12 challenging targets. The binder affinities lie
predominantly in the  nanomolar range, with one in the micromolar range. The success rates range from 10 to 100%, with an average success rate of 46.3%, which is remarkable for designs resulting from
a purely computational approach. These rates allow for the screening of far fewer designs experimentally to identify functioning binders, when compared to the current state of the art RFdiffusion10
and the recently described closed-source AlphaProteo binder  design pipeline53. Notably, a binder designed with our pipeline recently ranked first in a community-wide binder design competition,
showing nanomolar affinity against the challenging EGFR target54. However, we do expect success rates to vary based on the target protein and desired binding site. \nOne of the main challenges of PPI
design is the choice of a favorable target site7,11,55. Prototypical binding sites are often composed of hydrophobic patches with  minimizing the risk of potential off-target effects. Despite the
design successes outlined here, there are limitations to the BindCraft   ...    models 1-5 for reprediction. For benchmarks involving   ...    therapeutics. Nature 550, 74\u201379 (2017).\n10. Watson,
J. L. et al. De novo design of protein structure and function with RFdiffusion. Nature 620, 1089\u20131100 (2023).  11. Bennett, N. R. et al. Improving de novo protein binder design with deep   ...
Nat Commun 14, 2625 (2023)."], "published_date": "2025-04-24T00:00:00.000", "score": null}, {"title": "Code to complex: AI-driven de novo binder design - ScienceDirect", "url":
"https://www.sciencedirect.com/science/article/pii/S0969212625003119", "snippet": "Skip to main content Skip to article\n\n- View\u00a0 PDF\n- Download full issue\n\nSearch
ScienceDirect\n\nStructure\n\nVolume 33, Issue 10, 2 October 2025, Pages 1631-1642\n\n\n\n# Review Code to complex: AI-driven de novo binder design\n\nAuthor links open overlay panelDaniel R.Fox12356,
CyntiaTaveneau456, JanikClement1, RhysGrinter123, Gavin J.Knott45\n\nShow more\n\nAdd to Mendeley\n\nCite\n\nhttps://doi.org/10.1016/j.str.2025.08.007 Get rights and content\n\nUnder a Creative
Commons license\n\nOpen access\n\n## Summary\n\nThe", "highlights": ["Skip to main content Skip to article\n\n- View\u00a0 PDF\n- Download full issue\n\nSearch ScienceDirect\n\nStructure Volume 33,
Issue 10, 2 October 2025, Pages 1631-1642\n\n\n\n# Review Code to complex: AI-driven de novo binder design Author links open overlay panelDaniel R.Fox12356, CyntiaTaveneau456, JanikClement1,
RhysGrinter123, Gavin J.Knott45 Show more\n\nAdd to Mendeley\n\nCite\n\nhttps://doi.org/10.1016/j.str.2025.08.007 Get rights and content Under a Creative Commons license\n\nOpen access\n\n## Summary
The application of artificial intelligence to structural biology has transformed protein design from a conceptual challenge into a practical approach for creating new-to-nature proteins. By leveraging
machine learning, researchers can now computationally design proteins with tailored architectures and binding specificities. This has enabled the rapid in silico generation of high-affinity binders to
diverse and previously intractable targets. This approach dramatically reduces binder development time and resource requirements, compared to traditional experimental approaches, while improving hit
rates and designability. Recent successes include the creation of binding proteins that neutralize toxins, modulate immune pathways, and engage disordered targets with high affinity and specificity.
Improvements in model accuracy are expanding the scope of what can be designed, while characterization in preclinical models is paving the way for therapeutic development. De novo binder design
represents a paradigm shift in protein engineering, where custom binders can now be programmed to meet specific biological challenges. ## Graphical abstract\n\n1. Download: Download high-res image
(185KB)\n2. Download: Download full-size image - Previousarticle in issue\n- Nextarticle in issue\n\n## Keywords\n\nDe novo protein design\n\nde novo protein binders computational protein
design\n\nRFdiffusion\n\nChroma\n\nBindCraft\n\nProteinMPNN\n\nAlphaFold2\n\nRoseTTAFold generative diffusion models\n\nhallucination\n\ninpainting\n\nartificial intelligence\n\nmachine
learning\n\nneural networks Recommended articles\n\n6\n\nThese authors contributed equally\n\n\u00a9 2025 The Author(s). Published by Elsevier Inc."], "published_date": "2025-10-02T00:00:00.000",
"score": null}, {"title": "Improving Binder Success Rates with BindCraft - Levitate Bio", "url": "https://levitate.bio/improving-binder-success-rates-with-bindcraft/", "snippet": "Improving Binder
Success Rates with BindCraft - Levitate Bio \n\n# Improving Binder Success Rates with BindCraft\n\nRFDiffusion has successfully generated many de novo binders, but its hit rate for binding could use
improvement and it often requires additional design rounds to achieve optimal affinity. An alternative approach is to start with a native binding site and use RFDiffusion to build a novel protein
around the binding protein. However, the latest AI tool from the Rosetta community is changi", "highlights": ["Improving Binder Success Rates with BindCraft - Levitate Bio \n\n# Improving Binder
Success Rates with BindCraft RFDiffusion has successfully generated many de novo binders, but its hit rate for binding could use improvement and it often requires additional design rounds to achieve
optimal affinity. An alternative approach is to start with a native binding site and use RFDiffusion to build a novel protein around the binding protein. However, the latest AI tool from the Rosetta
community is changing the game\u2014producing strong binders with a high success rate, even without relying on a   ...    BindCraft modifies the ColabFold implementation of AlphaFold2 Multimer (AF2M)
to generate novel binding proteins for   ...    - Score below AF2M confidence threshold (~0.7-0.8).\n- Have <7 interface residues or structural clashes. # When is BindCraft a Better Choice Than
RFdiffusion? Both BindCraft and RFdiffusion are powerful tools for binder design, but BindCraft can be more effective in certain cases due to key advantages: Cofolding for Better Optimization -
BindCraft cofolds the binder and target together, optimizing both structure and sequence simultaneously. - RFdiffusion generates a rigid binder first, then ProteinMPNN fits a sequence, which may lead
to suboptimal interactions. - Best for: Flexible targets, induced fit interactions, intrinsically disordered regions (IDRs). Secondary Structure Control - BindCraft allows biasing toward different
secondary structures, overcoming RFdiffusion\u2019s alpha-helix bias. - Best for: Designing binders with diverse folds, such as beta-sheet-rich interfaces. Avoids Unrealistic Structures -
RFDiffusion\u2019s stochastic diffusion process can create poorly packed or unphysical designs. - BindCraft integrates structure-based refinement, reducing hallucinations. - Best for: Generating
experimentally viable, well-packed binders. Better Sequence-Structure Compatibility - BindCraft optimizes sequence and structure together, leading to stronger binding affinities. - RFdiffusion is used
to generate structures predicted to bind a target, but much of its output will not be good binders and many steps are needed to identify the best hits. - Best for: Designing binders with precise
binding interactions. # Experimental Results: How Well Does BindCraft Work? BindCraft was tested on 10 different target proteins. For each, dozens of binders were experimentally tested via SPR
(Surface Plasmon Resonance). The image below highlights the # of Binders found / # tested for each target and reports the best Kd of the binders for each target. Pacesa et al. 1 Figure 1\n\n## Why
This Is Impressive - These hit rates are significantly better than most de novo binder design methods. - The binding affinities (Kd values) show that many binders achieved sub-nanomolar affinity,
indicating strong binding.   ...    BindCraft was developed through a collaboration between two Rosetta labs; the Correia Lab(EPFL, Switzerland) and the Ovchinnikov Lab(MIT). This partnership combined
deep expertise in AlphaFold-based structure prediction and computational protein design, resulting in a new, highly effective pipeline for de novo binder generation. # Why this Matters & What\u2019s
Next\n\nBindCraft is a major advance in de novo protein design. It enables: \u2705 Binder creation from scratch, eliminating the need for pre-existing motifs or extensive optimization. \u2705
Automated sequence refinement, significantly improving success rates. \u2705 Better experimental success rates, making de novo design more cost-effective. At Levitate Bio, we have already integrated
BindCraft into our computational binder design pipeline. We are excited to   ...    1. Martin Pacesa, Lennart Nickel, Joseph Schmidt, et al. BindCraft: one-shot design of functional protein binders.
https://doi.org/10.1101/2024"], "published_date": "2025-02-20T20:34:28.000", "score": null}]
```

## 🔧 Tool: TodoWrite


```json
{
  "todos": [
    {
      "content": "Parse resolution criteria and understand the question",
      "status": "completed",
      "activeForm": "Parsing resolution criteria"
    },
    {
      "content": "Research AdaptyvBio competition history and success rates",
      "status": "completed",
      "activeForm": "Researching AdaptyvBio competition history"
    },
    {
      "content": "Research state of computational protein design field",
      "status": "completed",
      "activeForm": "Researching protein design field"
    },
    {
      "content": "Check prediction markets and related questions",
      "status": "in_progress",
      "activeForm": "Checking prediction markets"
    },
    {
      "content": "Run reflection and produce final forecast",
      "status": "pending",
      "activeForm": "Running reflection and producing forecast"
    }
  ]
}
```

### 📋 Result

```
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

## 🔧 Tool: mcp__markets__get_coherence_links


```json
{
  "post_id": 42911
}
```

### 📋 Result

```
[]
```

## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "AdaptyvBio protein binder competition 75% success rate"
}
```

### 📋 Result

```
{"markets": [], "query": "AdaptyvBio protein binder competition 75% success rate"}
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Escalante Mosaic protein binder design 88% hit rate Nipah competition"
}
```

### 📋 Result

```
{"query": "Escalante Mosaic protein binder design 88% hit rate Nipah competition", "results": [{"title": "Winning the de novo portion of the Adaptyv Nipah binder competition", "url":
"https://blog.escalante.bio/winning-the-de-novo-portion-of-the-adaptyv-nipah-binder-competition/", "snippet": "Winning the de novo portion of the Adaptyv Nipah binder competition\n![Winning the de
novo portion of the Adaptyv Nipah binder competition](/content/images/size/w2000/2026/01/MODEL.png)\nThe Adaptyv Nipah binder competition recently [released
results](https://proteinbase.com/collections/nipah-binder-competition-results?ref=blog.escalante.bio). If you're not familiar with it, the objective was to design protein binders to the Nipah virus G
protein. Designs were tested in the wetlab and ranked solel", "api_data": null, "hint": null}, {"title": "~180 lines of code to win the in silico portion of the Adaptyv Nipah binding competition",
"url": "https://blog.escalante.bio/180-lines-of-code-to-win-the-in-silico-portion-of-the-adaptyv-nipah-binding-competition/", "snippet": "~180 lines of code to win the in silico portion of the Adaptyv
Nipah binding competition\nHere's the [script](https://gist.github.com/nboyd/7b30c4033f834fc532a106d902fbdffa?ref=blog.escalante.bio) we used to get 1st place in the in silico portion of the Adaptyv
Nipah competition:\nimport modal\ndef download_boltz2():\nfrom mosaic.models.boltz2 import Boltz2\nBoltz2()\n### Build modal image: install mosaic + deps and download boltz2 model.\nimage =
(\nmodal.Image.debian_slim(python_version=\"3.12\")\n.apt_i", "api_data": null, "hint": null}, {"title": "Brian Naughton on X: \"Another excellent protein design blogpost from Nick Boyd and Sam Guns
at Escalante. They got the top scoring design (in silico score that is!) in the Adaptyv Bio Nipah competition using a very concise script, running mosaic on @modal so anyone can run it
https://t.co/4cEKkapV0J\" / X", "url": "https://x.com/btnaughton/status/2009663224330006871", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or
switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9
2026 X Corp.", "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein design", "url":
"https://www.adaptyvbio.com/blog/nipah-submissions/", "snippet": "After a busy few weeks with over 680 protein designers submitting their best binder designs against the surface glycoprotein of the
Nipah virus, the submissions and community vote doors have closed and we are waiting in anticipation for the experimental results to arrive. In the meantime, we want to highlight some interesting new
insights and cool protein structures that we have gathered during the course of this competition.\nLet\u2019s start with a quick recap: Nipah is one of the deadliest viruses ", "api_data": null,
"hint": null}, {"title": "GitHub - escalante-bio/mosaic: composite-objective protein design \u00b7 GitHub", "url": "https://github.com/escalante-bio/mosaic", "snippet": "WARNING: Unlike BindCraft
(which is a well-tested and well-tuned method for generic binder design),\nmosaic\nmay require substantial hand-holding (tuning learning rates, etc), often produces proteins that fail simple in-silico
tests, should be combined with standard filtering methods, etc. This is not for the faint of heart: the intent is to provide a framework in which to implement custom objective functions and
optimization algorithms for your application.\nWARNING: We rely heavily on just-in-tim", "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? +
Prediction markets for protein design", "url": "https://adaptyvbio.substack.com/p/what-happened-in-the-nipah-protein", "snippet": "What happened in the Nipah Protein Design Competition so far? +
Prediction markets for protein design\nFor our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods were most widely adopted, and highlight several
noteworthy and creative community cont\n\u2022 We hosted our third installment of the Protein Design Competition, this time challenging participants to design a binder against the Nipah virus
glycoprotein.\n\u2022 The response was incredible: Over ", "api_data": null, "hint": null}, {"title": "Nipah Binder Competition", "url": "https://proteinbase.com/competitions/adaptyv-nipah-
competition", "snippet": "Design a protein capable of neutralizing the Nipah virus, a pathogen with up to 75% mortality rate and high pandemic potential, currently lacking effective
treatments.\nSubmit your computational protein designs. 1000 designs will be selected for experimental validation, 600 by the best ipSAE score, 200 selected by the community and 200 selected by a
panel of experts.\n/\nSelected designs undergo experimental validation in the Adaptyv Lab. Proteins with the highest binding affinity against Nipah Vir", "api_data": null, "hint": null}, {"title":
"mosaic/README.md at main \u00b7 escalante-bio/mosaic", "url": "https://github.com/escalante-bio/mosaic/blob/main/README.md", "snippet": "WARNING: Unlike BindCraft (which is a well-tested and well-
tuned method for generic binder design),\nmosaic\nmay require substantial hand-holding (tuning learning rates, etc), often produces proteins that fail simple in-silico tests, should be combined with
standard filtering methods, etc. This is not for the faint of heart: the intent is to provide a framework in which to implement custom objective functions and optimization algorithms for your
application.\nWARNING: We rely heavily on just-in-tim", "api_data": null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url":
"https://www.adaptyvbio.com/blog/po104/", "snippet": "We released the [results of our second Protein Design Competition](https://foundry.adaptyvbio.com/competition) just about 2 weeks ago\u2026 and
they were great!\nA quick recap of what this was all about:\nAnd the designers did not disappoint. In our previous analysis [here](https://www.adaptyvbio.com/blog/po103), we went through how the meta
shifted from the first round, in particular how close the race was in the last few days as some submitters tried to increase their chances of landing in the top 10", "api_data": null, "hint": null},
{"title": "Building a Scalable Protein Design Pipeline with Seqera AI for Adaptyv's Nipah Binder Competition", "url": "https://seqera.io/blog/building-a-scalable-nextflow-protein-design-pipeline-for-
adaptyv-s-nipah-binder/", "snippet": "Building a Scalable Protein Design Pipeline with Seqera AI for Adaptyv's Nipah Binder Competition\n\ud83d\udca1Note: This guide shows you how to effectively use
AI to build reproducible pipelines to design proteins. In this tutorial we use three key pieces of technology:\n\u2022[Seqera AI]\n\u2022[Nextflow]\n\u2022[Seqera Cloud]+ Kubernetes\nThese
technologies combined, have allowed us to build a pipeline that designed novel binding proteins for the Nipah Binder competition on Proteinbase. All you need to replicate this workf", "api_data":
null, "hint": null}]}
```

## 💬 Response

Now let me look at the Escalante blog post more closely and check what the actual Nipah competition breakdown was for top performers.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://blog.escalante.bio/winning-the-de-novo-portion-of-the-adaptyv-nipah-binder-competition/",
  "prompt": "What was the hit rate / success rate for Escalante's Mosaic designs? How many designs tested vs how many bound? What were the overall competition results?"
}
```

### 📋 Result

```
{"url": "https://blog.escalante.bio/winning-the-de-novo-portion-of-the-adaptyv-nipah-binder-competition/", "content": "## Hit Rate and Success Rate\n\n**Escalante's Mosaic designs:**\n- **9 out of 10
designs bound** (90% success rate)\n- This was described as \"far better than any other team\"\n\n**Competition results:**\n- **1st, 2nd, 3rd, and 4th place** in the de novo category all went to
Escalante's designs\n- Notable exceptions with lower success rates:\n  - BindCraft2 (pre-release): ~30% hit rate\n  - Latent-X: ~30% hit rate\n\nThe author noted this 90% success rate was \"far better
than I expected\" since the designs were an experiment in removing filtering and ranking from standard design pipelines.\n\n---\n\n**Relevant links:**\n- [Adaptyv Nipah binder competition
results](https://proteinbase.com/collections/nipah-binder-competition-results)\n- [Previous post: 180 lines of code to win the in silico portion](https://blog.escalante.bio/180-lines-of-code-to-win-
the-in-silico-portion-of-the-adaptyv-nipah-binding-competition/)\n- [Architecture and antigenicity of the Nipah virus attachment glycoprotein (Science
paper)](https://www.science.org/doi/10.1126/science.abm5561)\n- [Golden raven fern design (worst performer)](https://proteinbase.com/proteins/golden-raven-fern?from=collection&slug=nipah-binder-
competition-results&sortField=kd&sortOrder=asc)\n- [Shy eagle fern design (bivalent kinetics)](https://proteinbase.com/proteins/shy-eagle-fern?from=collection&slug=nipah-binder-competition-
results&sortField=kd&sortOrder=asc)\n- [Florian W\u00fcnnemann's Nextflow protein design pipeline](https://seqera.io/blog/building-a-scalable-nextflow-protein-design-pipeline-for-adaptyv-s-nipah-
binder/)\n- [PeSTo epitope prediction tool](https://pesto.epfl.ch/)", "title": "Winning the de novo portion of the Adaptyv Nipah binder competition"}
```

```json
{
  "url": "https://proteinbase.com/collections/nipah-binder-competition-results",
  "prompt": "What is the overall success rate of binder designs? How many designs were tested? How many bound? Break down by method or designer if possible."
}
```

### 📋 Result

```
{"url": "https://proteinbase.com/collections/nipah-binder-competition-results", "content": "API Error: Claude Code is unable to respond to this request, which appears to violate our Usage Policy
(https://www.anthropic.com/legal/aup). Try rephrasing the request or attempting a different approach. If you are seeing this refusal repeatedly, try running /model claude-sonnet-4-20250514 to switch
models.", "title": "Results Overview"}
```

## 🔧 Tool: TodoWrite


```json
{
  "todos": [
    {
      "content": "Parse resolution criteria and understand the question",
      "status": "completed",
      "activeForm": "Parsing resolution criteria"
    },
    {
      "content": "Research AdaptyvBio competition history and success rates",
      "status": "completed",
      "activeForm": "Researching AdaptyvBio competition history"
    },
    {
      "content": "Research state of computational protein design field",
      "status": "completed",
      "activeForm": "Researching protein design field"
    },
    {
      "content": "Check prediction markets and related questions",
      "status": "completed",
      "activeForm": "Checking prediction markets"
    },
    {
      "content": "Run reflection and produce final forecast",
      "status": "in_progress",
      "activeForm": "Running reflection and producing forecast"
    }
  ]
}
```

### 📋 Result

```
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

## 💬 Response

Let me now synthesize my findings and run the reflection.

**Key data points gathered:**

1. **AdaptyvBio Competition History (3 rounds):**
   - **EGFR Round 1** (Sep 2024): 201 tested, 5 binders = **2.5% success rate**
   - **EGFR Round 2** (Dec 2024): 400 tested, 53 binders = **14% success rate** (5x improvement in ~3 months)
   - **Nipah** (results ~Jan 2026): 1026 tested, 99 binders = **9.6% overall success rate** (harder target)

2. **Per-method breakdown in Nipah competition:**
   - Escalante's Mosaic: 9/10 = **88.9% hit rate** (but only n=9)
   - BindCraft2 (pre-release): ~30% hit rate
   - Latent-X: ~30% hit rate
   - RFdiffusion: ~21.4% hit rate
   - ProteinMPNN: ~20.7% hit rate
   - BindCraft: ~5.68% hit rate (n=88)
   - BoltzGen: ~1.23% (n=163)

3. **State of the art (published):**
   - BindCraft (Nature 2025): 10-100% success rates, average 46.3% across 12 targets in controlled settings
   - AlphaProteo: ~24.5% hit rate in controlled settings
   - Top 0.5% by min_ipsae filtering: **83.3% binders** (5/6 in Nipah)
   - Top 1% by min_ipsae filtering: **63.6% binders** (7/11 in Nipah)

4. **Critical insight for the question:** The question asks about >75% of **tested** designs being binders. This depends on both the quality of the designs AND the selection/filtering process. Key observations:
   - Even with current tools, when you pick only the very top tail of designs by computational metrics, you can already hit 83.3% binding in the Nipah competition
   - Escalante's Mosaic achieved 88.9% on 9 designs
   - But the question requires the COMPETITION as a whole to have >75% success rate across ALL tested designs, not just one team's subset

5. **Question interpretation:** The question asks if >75% of ALL designs selected for testing in a competition are binders. This is the AGGREGATE success rate across all participants.

Wait — let me re-read: "an AdaptyvBio protein-binder competition is conducted in which >75% of the computationally generated designs selected for experimental testing are classified as binders." This could mean either:
- (a) The overall competition success rate is >75% (all tested designs combined), OR
- (b) Any single participant or team achieves >75% among their tested designs

Given the phrasing "the computationally generated designs selected for experimental testing," this most naturally reads as ALL designs tested in the competition, not a subset. The overall rate needs to be >75%.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let's think about the trajectory and what would need to happen\n\n# Competition-wide success rates over time:\ncompetitions = {\n    \"EGFR R1 (Sep 2024)\": {\"tested\": 201, \"binders\": 5, \"rate\": 5/201},\n    \"EGFR R2 (Dec 2024)\": {\"tested\": 400, \"binders\": 53, \"rate\": 53/400},\n    \"Nipah (Jan 2026)\": {\"tested\": 1026, \"binders\": 99, \"rate\": 99/1026},\n}\n\nfor name, data in competitions.items():\n    print(f\"{name}: {data['rate']*100:.1f}% ({data['binders']}/{data['tested']})\")\n\nprint(\"\\n--- Key observations ---\")\nprint(f\"Current overall rate: 9.6%\")\nprint(f\"Target: 75%\")\nprint(f\"Gap: {75 - 9.6:.1f} percentage points\")\nprint(f\"Multiple needed: {75/9.6:.1f}x improvement from current\")\n\nprint(\"\\n--- But per-method rates show potential ---\")\nprint(\"Escalante Mosaic: 88.9% (9/10) - EXCEEDS 75%\")\nprint(\"BindCraft2/Latent-X: ~30%\")\nprint(\"Top 0.5% by min_ipsae: 83.3% (5/6)\")\nprint(\"Top 1% by min_ipsae: 63.6% (7/11)\")\n\nprint(\"\\n--- What would need to happen ---\")\nprint(\"Option 1: Competition format changes to test only top-filtered designs\")\nprint(\"Option 2: Design methods improve so much that most submissions are binders\")\nprint(\"Option 3: AdaptyvBio applies stringent filtering before testing\")\n\n# The key question is whether AdaptyvBio would change their selection methodology\n# Currently they test ~1000 designs with mixed selection criteria\n# If they shifted to testing only the most promising designs, rates could be much higher\n# But the fine print says \"the competition must only test novel designs\"\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "EGFR R1 (Sep 2024): 2.5% (5/201)\nEGFR R2 (Dec 2024): 13.2% (53/400)\nNipah (Jan 2026): 9.6% (99/1026)\n\n--- Key observations ---\nCurrent overall rate: 9.6%\nTarget:
75%\nGap: 65.4 percentage points\nMultiple needed: 7.8x improvement from current\n\n--- But per-method rates show potential ---\nEscalante Mosaic: 88.9% (9/10) - EXCEEDS 75%\nBindCraft2/Latent-X:
~30%\nTop 0.5% by min_ipsae: 83.3% (5/6)\nTop 1% by min_ipsae: 63.6% (7/11)\n\n--- What would need to happen ---\nOption 1: Competition format changes to test only top-filtered designs\nOption 2:
Design methods improve so much that most submissions are binders\nOption 3: AdaptyvBio applies stringent filtering before testing\n", "stderr": "", "duration_ms": 1}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me think about this more carefully\n# The question is about the COMPETITION as a whole, not individual teams\n\n# Key considerations:\n# 1. AdaptyvBio competitions select designs via multiple criteria (computational scores, \n#    community vote, expert selection). They test a large number (~200-1200)\n# 2. The field is rapidly improving - BindCraft went from concept to 46% average success\n# 3. By 2030, we have ~4 more years of development\n# 4. BUT: competitions are open to all, including novices, so there's always a long tail\n#    of poor designs pulling down the average\n\n# For >75% OVERALL to be achieved, basically ALL or nearly all tested designs need to work\n# This seems very hard when you're testing 1000+ designs from many different teams\n\n# However, there are scenarios where this could happen:\n# Scenario A: AdaptyvBio runs a smaller competition testing only ~20-50 carefully filtered designs\n# Scenario B: Design tools become SO good that even novice submissions work\n# Scenario C: They create a new competition format with much higher filtering thresholds\n\n# Against these scenarios:\n# - AdaptyvBio has been INCREASING the number of designs tested (200 -> 400 -> 1026)\n# - They explicitly want to test diverse approaches (community vote, expert selection, etc.)\n# - Having many participants with varying skill levels is the POINT of a competition\n# - Novel designs only (fine print) means you can't just submit known binders\n\n# The trend in overall rates: 2.5% -> 13.2% -> 9.6% (not monotonically increasing!)\n# The Nipah target was harder, which pulled the rate DOWN\n\n# For the field overall, BindCraft gets 46% average in controlled settings with ideal targets\n# But competitions test against specific (often challenging) targets\n# And include designs from teams using suboptimal methods\n\n# My assessment: This requires a paradigm shift in either:\n# 1. How good EVERYONE's designs are (not just the best teams), OR\n# 2. How AdaptyvBio structures their competition (testing far fewer, pre-filtered designs)\n\n# I think this is possible but not highly likely by 2030\n# The rate of improvement is significant but the gap is large\n# Going from ~10% to >75% requires nearly an order of magnitude improvement\n\nprint(\"Analysis summary:\")\nprint(\"=\" * 60)\nprint(f\"Current best overall rate: 13.2% (EGFR R2)\")\nprint(f\"Target: 75%\")\nprint(f\"Need: ~5.7x improvement in aggregate competition rate\")\nprint()\nprint(\"Favorable factors:\")\nprint(\"- Rapid tool improvement (BindCraft, AlphaProteo, Mosaic)\")  \nprint(\"- Better computational filtering (ipsae_min)\")\nprint(\"- Individual teams already achieving >75%\")\nprint(\"- 3.7 years remaining for further progress\")\nprint(\"- Competition format could change\")\nprint()\nprint(\"Unfavorable factors:\")\nprint(\"- 75% needs ALL participants to be good, not just leaders\")\nprint(\"- AdaptyvBio tests diverse submissions (including weak ones)\")\nprint(\"- Novel designs only = can't use known binders\")\nprint(\"- Target difficulty varies enormously\")\nprint(\"- Overall rates haven't monotonically increased\")\nprint(\"- Gap between best individual (88.9%) and average (9.6%) is huge\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Analysis summary:\n============================================================\nCurrent best overall rate: 13.2% (EGFR R2)\nTarget: 75%\nNeed: ~5.7x improvement in
aggregate competition rate\n\nFavorable factors:\n- Rapid tool improvement (BindCraft, AlphaProteo, Mosaic)\n- Better computational filtering (ipsae_min)\n- Individual teams already achieving >75%\n-
3.7 years remaining for further progress\n- Competition format could change\n\nUnfavorable factors:\n- 75% needs ALL participants to be good, not just leaders\n- AdaptyvBio tests diverse submissions
(including weak ones)\n- Novel designs only = can't use known binders\n- Target difficulty varies enormously\n- Overall rates haven't monotonically increased\n- Gap between best individual (88.9%) and
average (9.6%) is huge\n", "stderr": "", "duration_ms": 0}
```
