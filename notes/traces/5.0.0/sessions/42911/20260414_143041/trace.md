# Reasoning Log: Will an AdaptyvBio protein-binder competition have >75% of tested designs be classified as binders before 2030?

*Generated: 2026-04-14T14:56:10.744933+00:00*


## 💭 Thinking

Let me analyze this forecasting question about AdaptyvBio protein-binder competitions achieving >75% success rate before 2030.

Let me start by understanding the question, then research the current state of protein design and AdaptyvBio competitions.

## 💬 Response

I'll start by fetching the full question details and researching the current state of protein design competitions.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


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

## 🔧 Tool: mcp__research__research


## 🔧 Tool: mcp__metaculus__get_coherence_links


```json
{
  "questions": [
    {
      "query": "AdaptyvBio protein binder competition results history success rates 2024 2025 2026",
      "ttl": "3d"
    },
    {
      "query": "Computational protein design binder success rates state of the art 2025 2026 RFdiffusion AlphaFold",
      "ttl": "7d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"slug": "adaptyvbio-protein-binder-competition-results-hist-05d5592d", "query": "AdaptyvBio protein binder competition results history success rates 2024 2025 2026", "answer": "Now I
have comprehensive data to compile a thorough report. Let me produce the structured output.\n\n## AdaptyvBio Protein Binder Competition: Complete Results History (2024\u20132026)\n\n###
Overview\n\nAdaptyv Bio (based in Switzerland) has run a series of open, crowdsourced protein binder design competitions since mid-2024, rapidly scaling in scope and participation. Their platform,
Proteinbase, hosts all experimental data open-source. As of April 2026, they have experimentally validated over 2,000 prot", "key_facts": ["Adaptyv Bio has run 3 completed protein binder design
competitions (EGFR Round 1, EGFR Round 2, Nipah) and has a 4th (RBX1) currently active as of April 2026", "EGFR Round 1 (Oct 2024): 201 designs tested, 2.5% binding hit rate, 73-76% expression rate,
~50 participants, best KD 6.6 nM", "EGFR Round 2 (Dec 2024): 400 designs tested, 13-14% binding hit rate (5x improvement over Round 1), 95-96% expression rate, 130 participants, best KD 1.21 nM
(Cradle, 8x better than Cetuximab)", "Nipah Competition (Jan 2026): 1,030 designs characterized out of 1,200 selected, 9.6% hit rate (99 binders), 86% expression rate, 680+ participants, 10,000+
submissions, best KD 370 pM", "Nipah was a significantly harder target than EGFR (tetrameric protein with little prior binder work), explaining the lower hit rate vs EGFR Round 2", "In Nipah
competition, Escalante's Mosaic tool achieved 88.8% hit rate (n=9), RFdiffusion 21.4% (n=42), BindCraft 5.68% (n=88), BoltzGen 1.23% (n=163)", "Nick Boyd (Escalante) won de novo category in Nipah with
9/10 designs binding (90% success rate) using gradient-based optimization directly on Boltz-2 loss without inverse folding or filtering", "Participation grew dramatically: ~50 designers (EGFR R1)
\u2192 130 (EGFR R2) \u2192 680+ (Nipah)", "Submissions grew from ~726 (EGFR R1) to 10,000+ (Nipah) \u2014 a 14x increase", "Cumulative across all Proteinbase data: ~2,100+ proteins validated, ~340+
binders found across targets including EGFR, Nipah, PD-L1, IL-7Ra, HSA"], "sources_count": 19, "data_points_count": 30, "is_follow_up": false}, {"slug": "computational-protein-design-binder-success-
rates-caee394e", "query": "Computational protein design binder success rates state of the art 2025 2026 RFdiffusion AlphaFold", "answer": "\n\nBased on all the data gathered across multiple rounds of
research, here is my comprehensive synthesis:\n\n---\n\n# Computational Protein Binder Design: State-of-the-Art Success Rates (2024\u20132026)\n\n## Executive Summary\n\nThe field of computational
protein binder design has undergone a dramatic transformation since 2023. Experimental success rates have improved from <0.1% (Rosetta-era methods) to routinely 10\u201390%+ with the latest ML-based
approaches. The key inflection point was the introduction of di", "key_facts": ["Rosetta-era de novo binder design had experimental success rates below 0.1%, typically requiring screening of tens of
thousands of designs", "RFdiffusion (2023) achieved 0-33.7% experimental success rates across targets, with best affinities of 14-370 nM; IL-7R\u03b1 17%, PD-L1 13.4%, TrkA 0%", "AlphaProteo (Sep
2024, DeepMind) achieved 9-88% experimental success rates across 7 targets with picomolar affinities (best: 82 pM for IL-7R\u03b1), but failed on TNF\u03b1 (0%) and remains closed-source", "BindCraft
(Nature 2025) achieved 10-100% experimental success rates across 12 targets (avg ~46.3%), is open-source, and leverages AlphaFold2 weights", "\u03b2-pairing targeted RFdiffusion (Nature Comms, Jan
2026) improved in silico success ~9-fold over standard RFdiffusion (9.2% vs 0.98%) and achieved sub-nanomolar affinities on previously intractable targets", "RFdiffusion antibody (VHH) design achieved
only 0-2% experimental success rates with 9,000 designs screened per target", "Latent-X (Jul 2025 preprint) claims 90-100% macrocyclic hit rates and 10-64% mini-binder hit rates with sub-picomolar
affinities, but is not peer-reviewed and is closed-source", "Proteina-Complexa (Mar 2026 preprint) achieved 14.4 avg unique in silico successes vs 4.68 for RFdiffusion across 19 targets, including 15
successes on TNF\u03b1 where AlphaProteo got 0, but lacks wet-lab validation", "BECraft (May 2025 preprint) outperforms BindCraft, RFdiffusion, and ESM3 on 7/8 targets in silico; ESM3 achieved 0%
success across all 8 targets", "A meta-analysis of 3,766 experimentally tested binders found an overall 11.6% confirmed binding rate, with AF3 ipSAE_min as the best in silico predictor of binding
success"], "sources_count": 9, "data_points_count": 28, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

```json
{
  "post_id": 42911
}
```

### 📋 Result

```
[]
```

## 💬 Response

Excellent - very rich data. Let me now get more details on the specific tools and trends, particularly the Nipah competition results and what's coming next.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "AdaptyvBio RBX1 competition 2026 protein binder"
}
```

### 📋 Result

```
{"query": "AdaptyvBio RBX1 competition 2026 protein binder", "results": [{"title": "RBX-1 Binder Design Competition 2026 - GEM Workshop", "url": "https://www.gembio.ai/gemadaptyv2026", "snippet":
"About\nThe [GEM](https://www.gembio.ai/) \u00d7 [Adaptyv](https://www.adaptyvbio.com) RBX-1 Binder Design Competition 2026 brings together the computational protein design community to tackle a
challenging and biologically significant target. Submit your designs\u2014we'll test a total of 300 binders in the wet lab and announce results at ICLR 2026.\nWhy RBX-1?\nBiology: RBX-1 (RING Box
Protein 1), also known as ROC1, is a 108-amino acid E3 ubiquitin ligase component essential for the SCF (SKP1-CUL1-F-box) c", "api_data": null, "hint": null}, {"title": "Adaptyv Bio (@adaptyvbio) /
Posts / X", "url": "https://x.com/adaptyvbio?lang=en", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to
continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null,
"hint": null}, {"title": "The Protein Design Competition Is Back! - Adaptyv Bio", "url": "https://adaptyvbio.substack.com/p/the-protein-design-competition-is", "snippet": "The Protein Design
Competition Is Back!\n\ud83c\udf0d The biggest decentralized science experiment of 2025 starts now!\nThe protein design competition returns: we\u2019re inviting scientists, engineers, and hackers from
around the world to help design new proteins capable of neutralizing the Nipah virus, a pathogen with up to 75% mortality and no effective treatment.\nAll you need is a laptop to participate: submit
your computational protein designs, and [Adaptyv](https://adaptyvbio.com/) will synthesize and exper", "api_data": null, "hint": null}, {"title": "Protein Design Competition - RESULTS - Adaptyv Bio",
"url": "https://adaptyvbio.substack.com/p/protein-design-competition-results", "snippet": "Protein Design Competition - RESULTS\nThe long awaited results are here -- and they don\u2019t
disappoint!\nThe long awaited results are here -- and they don\u2019t disappoint!\n\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400!\n\ud83e\uddec Out of those 400
proteins, 378 expressed (95% expression rate!)\n\ud83d\ude80 Out of those 378 expressed proteins, 53 did successfully bind the target protein EGFR (that\u2019s a 14% success rate, more than 5x of the
success rate of the previous round just 2 months ago!)\n\ud83d\udcaa Th", "api_data": null, "hint": null}, {"title": "Protein Design Competition - Adaptyv Bio", "url":
"https://design.adaptyvbio.com/", "snippet": "All-atom diffusion-based generative model developed for de novo design of protein and peptide binders across a wide array of target types\nA flexible de
novo binder design workflow using RFdiffusion for backbone generation\nProtein binder design pipeline that can be used to design miniprotein and peptide binders\nprotein\n1030\nProteins
validated\n103\nBinders\nNipah Virus Glycoprotein G mediates viral attachment to host cells. Changes in its expression or function can influence viral spread and disease", "api_data": null, "hint":
null}, {"title": "Adaptyv Bio", "url": "https://www.adaptyvbio.com/blog", "snippet": "For our Nipah Binder competition, we give a short overview of the submitted designs, examine which design methods
were most widely adopted, and highlight several noteworthy and creative community contributions. Plus, we opened a prediction market on Manifold for this competition so you can bet on hit rates, best
performing models, and more\nTong Chen and colleagues from Pranam Chatterjee\u2019s Programmable Biology Group at the University of Pennsylvania are showcasing their most recent model MOG-DFM ",
"api_data": null, "hint": null}, {"title": "8x improvement in EGFR binding affinity: winning the Adaptyv Bio protein design competition | Cradle", "url": "https://www.cradle.bio/blog/adaptyv-protein-
design-competition", "snippet": "![](https://framerusercontent.com/images/4UdCTbTNeeNo0TyNDeXL0GNKa1k.jpg?width=2400&height=1280)\n8x improvement in EGFR binding affinity: winning the Adaptyv Bio
protein design competition\n130 teams competed in Adaptyv Bio\u2019s protein design competition to create novel EGFR-binding proteins. Cradle's platform achieved first place with a binding affinity of
1.21nM, which is 8.2 times stronger than Merck's commercial antibody Cetuximab*.\nWe are proud to announce that Cradle\u2019s submission [took the to", "api_data": null, "hint": null}, {"title":
"Introducing BenchBB and the community paper of the Protein Design Competition", "url": "https://www.adaptyvbio.com/blog/benchbb/", "snippet": "Introducing BenchBB and the community paper of the
Protein Design Competition\nlaunch\n/Article\n/TL;DR\n-We wrote a community paper about our Protein Design Competition, teaming up with your favourite protein designers from both rounds.\n-We aimed to
explore the competition data in as many ways as we could, take stock of the state of the field, what SotAs have been established across the rounds, and which metric is most predictive of binding and
expression.\nThe community paper after the Protein Desi", "api_data": null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url":
"https://www.adaptyvbio.com/blog/po104/", "snippet": "We released the [results of our second Protein Design Competition](https://foundry.adaptyvbio.com/competition) just about 2 weeks ago\u2026 and
they were great!\nA quick recap of what this was all about:\nAnd the designers did not disappoint. In our previous analysis [here](https://www.adaptyvbio.com/blog/po103), we went through how the meta
shifted from the first round, in particular how close the race was in the last few days as some submitters tried to increase their chances of landing in the top 10", "api_data": null, "hint": null},
{"title": "Protein Optimization 102: Lessons from the protein design competition", "url": "https://www.adaptyvbio.com/blog/po102/", "snippet": "In our [last
](https://www.adaptyvbio.com/blog/po101)[blog](https://www.adaptyvbio.com/blog/po101) post, we looked at the different ways you can optimize a protein for a given task using machine learning
models.\nWe made the distinction between [fixed](https://www.adaptyvbio.com/blog/po101#:~:text=Supplementary%20-%20Fixed%20model%20optimization) and
[sequential](https://www.adaptyvbio.com/blog/po101#:~:text=sequentially-optimized%20models) model optimization and further split the latter into [mo", "api_data": null, "hint": null}]}
```

```json
{
  "query": "BindCraft protein binder success rate 100% experimental 2025 2026"
}
```

### 📋 Result

```
{"query": "BindCraft protein binder success rate 100% experimental 2025 2026", "results": [{"title": "One-shot design of functional protein binders with BindCraft | Nature", "url":
"https://www.nature.com/articles/s41586-025-09429-6", "snippet": "Abstract\nProtein\u2013protein interactions are at the core of all key biological processes. However, the complexity of the structural
features that determine protein\u2013protein interactions makes their design challenging. Here we present BindCraft, an open-source and automated pipeline for de novo protein binder design with
experimental success rates of 10\u2013100%. BindCraft leverages the weights of AlphaFold2 (ref. [1](https://www.nature.com/articles/s41586-025-09429-6#ref-CR1)) to generate binders with n",
"api_data": null, "hint": null}, {"title": "BindCraft: one-shot design of functional protein binders - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11642741/", "snippet":
"Abstract\nProtein\u2013protein interactions (PPIs) are at the core of all key biological processes. However, the complexity of the structural features that determine PPIs makes their design
challenging. We present BindCraft, an open-source and automated pipeline for de novo protein binder design with experimental success rates of 10-100%. BindCraft leverages the weights of AlphaFold2 1
to generate binders with nanomolar affinity without the need for high-throughput screening or experimental optimizati", "api_data": null, "hint": null}, {"title": "BindCraft AI Model Achieves One-Shot
Functional Protein Design", "url": "https://www.genengnews.com/topics/artificial-intelligence/bindcraft-ai-model-achieves-one-shot-functional-protein-design/", "snippet": "![BindCraft Deep learning
structure networks can hallucinate accurate protein binders with high experimental success rates [Martin Pacesa]](https://www.genengnews.com/wp-
content/uploads/2025/08/BindCraft-696x393.png)\n![BindCraft Deep learning structure networks can hallucinate accurate protein binders with high experimental success rates [Martin
Pacesa]](https://www.genengnews.com/wp-content/uploads/2025/08/BindCraft-696x393.png)\nFor the field of drug development, hitting the right target with a", "api_data": null, "hint": null}, {"title":
"BindCraft: one-shot design of functional protein binders | bioRxiv", "url": "https://www.biorxiv.org/content/10.1101/2024.09.30.615802v1", "snippet": null, "api_data": null, "hint": null}, {"title":
"I Went Through BindCraft\u2019s Affinity Data. Here Are the Gaps I Found. | by Engin Yapici | Medium", "url": "https://medium.com/@enginyapici/i-went-through-bindcrafts-affinity-data-here-are-the-
gaps-i-found-7b90e7880b41", "snippet": null, "api_data": null, "hint": null}, {"title": "One-shot design of functional protein binders with BindCraft - PMC", "url":
"https://pmc.ncbi.nlm.nih.gov/articles/PMC12507698/", "snippet": "Abstract\nProtein\u2013protein interactions are at the core of all key biological processes. However, the complexity of the structural
features that determine protein\u2013protein interactions makes their design challenging. Here we present BindCraft, an open-source and automated pipeline for de novo protein binder design with
experimental success rates of 10\u2013100%. BindCraft leverages the weights of AlphaFold2 (ref. [1](https://pmc.ncbi.nlm.nih.gov#CR1)) to generate binders with nanomolar affinity without ",
"api_data": null, "hint": null}, {"title": "BindCraft: The Dawn of One-Shot Protein Design", "url": "https://www.ailurus.bio/post/bindcraft-the-dawn-of-one-shot-protein-design", "snippet":
"Introduction\nProtein binders\u2014molecules engineered to bind specific targets with high affinity and precision\u2014represent a cornerstone of modern medicine and biotechnology. From antibody
therapies that target cancer cells to diagnostic agents that detect pathogens, their potential is immense. However, the traditional path to discovering these binders has been a long and arduous one,
often characterized by brute-force screening of millions of candidates with a frustratingly low probability of succes", "api_data": null, "hint": null}, {"title": "AI-Powered Protein Binder Discovery
With BindCraft | Technology Networks", "url": "https://www.technologynetworks.com/biopharma/news/an-open-source-ai-platform-helps-accelerate-protein-binder-discovery-404221", "snippet": "An Open-
Source AI Platform Helps Accelerate Protein Binder Discovery\nSince its release last year, the open-source platform BindCraft has already disrupted the world of protein design.\n![Close up of a
visualization of a protein molecule showing the directionality of the individual amino acid strands.](https://assets.technologynetworks.com/production/dynamic/images/content/404221/an-open-source-ai-
platform-helps-accelerate-protein-binder-discovery-404221-960x540.jpg?cb=13501936)\nPhysical interacti", "api_data": null, "hint": null}, {"title": "An open-source AI platform to democratize protein
design", "url": "https://phys.org/news/2025-08-source-ai-platform-democratize-protein.html", "snippet": null, "api_data": null, "hint": null}, {"title": "One-shot design of functional protein binders
with BindCraft \u2013 Rosetta Commons", "url": "https://rosettacommons.org/2025/09/25/one-shot-design-of-functional-protein-binders-with-bindcraft/", "snippet": "![](https://rosettacommons.org/wp-
content/uploads/2025/09/AI_protein-design-1024x576.png)\nOne-shot design of functional protein binders with BindCraft\nRead more:
[https://www.nature.com/articles/s41586-025-09429-6](https://www.nature.com/articles/s41586-025-09429-6)\nAuthors: Martin Pacesa, Lennart Nickel, Christian Schellhaas, Joseph Schmidt, Ekaterina
Pyatova, Lucas Kissling, Patrick Barendse, Jagrity Choudhury, Srajan Kapoor, Ana Alcaraz-Serna, Yehlin Cho, Kourosh H. Ghamary, Laura Vinu\u00e9, Brah", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Escalante Mosaic protein binder tool 88% hit rate Nick Boyd"
}
```

### 📋 Result

```
{"query": "Escalante Mosaic protein binder tool 88% hit rate Nick Boyd", "results": [{"title": "~180 lines of code to win the in silico portion of the Adaptyv Nipah binding competition", "url":
"https://blog.escalante.bio/180-lines-of-code-to-win-the-in-silico-portion-of-the-adaptyv-nipah-binding-competition/", "snippet": "~180 lines of code to win the in silico portion of the Adaptyv Nipah
binding competition\nHere's the [script](https://gist.github.com/nboyd/7b30c4033f834fc532a106d902fbdffa?ref=blog.escalante.bio) we used to get 1st place in the in silico portion of the Adaptyv Nipah
competition:\nimport modal\ndef download_boltz2():\nfrom mosaic.models.boltz2 import Boltz2\nBoltz2()\n### Build modal image: install mosaic + deps and download boltz2 model.\nimage =
(\nmodal.Image.debian_slim(python_version=\"3.12\")\n.apt_i", "api_data": null, "hint": null}, {"title": "GitHub - escalante-bio/mosaic: composite-objective protein design \u00b7 GitHub", "url":
"https://github.com/escalante-bio/mosaic", "snippet": "WARNING: Unlike BindCraft (which is a well-tested and well-tuned method for generic binder design),\nmosaic\nmay require substantial hand-holding
(tuning learning rates, etc), often produces proteins that fail simple in-silico tests, should be combined with standard filtering methods, etc. This is not for the faint of heart: the intent is to
provide a framework in which to implement custom objective functions and optimization algorithms for your application.\nWARNING: We rely heavily on just-in-tim", "api_data": null, "hint": null},
{"title": "Brian Naughton on X: \"Another excellent protein design blogpost from Nick Boyd and Sam Guns at Escalante. They got the top scoring design (in silico score that is!) in the Adaptyv Bio
Nipah competition using a very concise script, running mosaic on @modal so anyone can run it https://t.co/4cEKkapV0J\" / X", "url": "https://x.com/btnaughton/status/2009663224330006871", "snippet":
"We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our
Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "Brian Naughton on X: \"Re-posting Nick
Boyd's Mosaic blogpost after his incredible results in the Nipah G competition. https://t.co/4cEKkapV0J\" / X", "url": "https://x.com/btnaughton/status/2014367611468063149", "snippet": "We\u2019ve
detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help
Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "Minibinder design is just not that hard", "url":
"https://blog.escalante.bio/minibinder-design-is-just-not-that-hard/", "snippet": "Minibinder design is just not that hard [[1]]\nMinibinders to PDL1\nOne computational project we've been working on
at Escalante is designing minibinders: small (typically <100 amino acids) protein binders. Minibinders have a huge range of uses from therapeutics to in vitro assay development. There's been a lot of
well-justified excitement in the area of computational de novo design of minibinders: it's (almost) fair to say that in the last 24 months de novo minibinder design went from exceedingly", "api_data":
null, "hint": null}, {"title": "Escalante uses JAX on TPUs for AI-driven protein design | Google Cloud Blog", "url": "https://cloud.google.com/blog/topics/customers/escalante-uses-jax-on-tpus-for-ai-
driven-protein-design", "snippet": "AI Innovators: How JAX on TPU is helping Escalante advance AI-driven protein design\n![https://storage.googleapis.com/gweb-cloudblog-
publish/images/jax.max-2500x2500.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/jax.max-2500x2500.jpg)\nSrikanth Kilaru\nSenior Product Manager, Google ML Frameworks\nAs a Python
library for accelerator-oriented array computation and program transformation, [JAX](http://jax.dev) is widely recognized for its power in training large-scale AI models. Bu", "api_data": null,
"hint": null}, {"title": "Brian Naughton on X: \"Great blogpost by Nick Boyd and Sam Guns from Escalante Bio (posted on the other site!) https://t.co/RfFrbMID0J They introduce mosaic for binder
design, and show some impressive results, with 7/10 and 8/10 binders working for two targets! https://t.co/qwnn2XOczm https://t.co/b0w5auFzzU\" / X", "url":
"https://x.com/btnaughton/status/1962906210417664408", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to
continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null,
"hint": null}, {"title": "Winning the de novo portion of the Adaptyv Nipah binder competition", "url": "https://blog.escalante.bio/winning-the-de-novo-portion-of-the-adaptyv-nipah-binder-
competition/", "snippet": "Winning the de novo portion of the Adaptyv Nipah binder competition\n![Winning the de novo portion of the Adaptyv Nipah binder
competition](/content/images/size/w2000/2026/01/MODEL.png)\nThe Adaptyv Nipah binder competition recently [released results](https://proteinbase.com/collections/nipah-binder-competition-
results?ref=blog.escalante.bio). If you're not familiar with it, the objective was to design protein binders to the Nipah virus G protein. Designs were tested in the wetlab and ranked solel",
"api_data": null, "hint": null}, {"title": "mosaic/README.md at main \u00b7 escalante-bio/mosaic", "url": "https://github.com/escalante-bio/mosaic/blob/main/README.md", "snippet": "WARNING: Unlike
BindCraft (which is a well-tested and well-tuned method for generic binder design),\nmosaic\nmay require substantial hand-holding (tuning learning rates, etc), often produces proteins that fail simple
in-silico tests, should be combined with standard filtering methods, etc. This is not for the faint of heart: the intent is to provide a framework in which to implement custom objective functions and
optimization algorithms for your application.\nWARNING: We rely heavily on just-in-tim", "api_data": null, "hint": null}, {"title": "Nick Boyd - Escalante | LinkedIn", "url":
"https://www.linkedin.com/in/nick-boyd-bb6054328/", "snippet": null, "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://blog.escalante.bio/minibinder-design-is-just-not-that-hard/",
  "prompt": "What success rates did Escalante achieve for protein binder design? What specific hit rates for PDL1 and other targets? How many designs tested and how many were binders?"
}
```

### 📋 Result

```
{"url": "https://blog.escalante.bio/minibinder-design-is-just-not-that-hard/", "content": "Based on the content, Escalante's experimental success rates for protein binder design were:\n\n**Overall
Results:**\n- All three design methods tested produced binders for both targets (PDL1 and IL7RA)\n- Best design method achieved: **8/10 success rate for PDL1** and **7/10 success rate for IL7RA**\n-
**Total designs tested: 10 per target** (for each of the three design methods)\n- Binding affinities ranged from high nanomolar to micromolar range\n\n**Design Process:**\n- For each design method and
target, they generated 2,500 candidate designs\n- These were then inverse folded, filtered, and ranked using BindCraft protocol\n- Top 10 designs per method/target were sent for wet lab
testing\n\n**Important Context:**\n- The minimum detection threshold was approximately 10\u00b5M\n- These results are described as \"on par with some recently published results from closed models and
roughly matches open source work\"\n- Success was achieved with open source tools, without training new models, for a few thousand dollars (mostly wet-lab costs)\n\n**Relevant links:**\n- [Full
experimental results](https://gist.github.com/nboyd/bdb5a7606d19e57ae4565c2c532f4538)\n- [mosaic GitHub repository](https://github.com/escalante-bio/mosaic)\n- [BindCraft GitHub
repository](https://github.com/martinpacesa/BindCraft)\n- [Boolean Biotech overview on protein binder design](https://blog.booleanbiotech.com/protein-binder-design-revisited)\n- [Adaptyv Bio
benchmarking platform](https://beta.adaptyvbio.com/benchbb)\n- [Boltz-2 structure prediction model](https://github.com/jwohlwend/boltz)", "title": "Minibinder design is just not that hard"}
```

```json
{
  "url": "https://www.gembio.ai/gemadaptyv2026",
  "prompt": "What are the details of the RBX-1 competition? How many designs will be tested? What are the rules? When will results be announced?"
}
```

### 📋 Result

```
{"url": "https://www.gembio.ai/gemadaptyv2026", "content": "# RBX-1 Binder Design Competition 2026 - Key Details\n\n## Target: RBX-1 (RING Box Protein 1)\n- 108-amino acid E3 ubiquitin ligase
component\n- N-terminal region (residues 1-39) is intrinsically disordered\n- C-terminal RING-H2 finger domain stabilized by three zinc ions\n- Critical roles in cell cycle regulation, signal
transduction, and cancer biology\n\n## Number of Designs Tested\n**300 total designs** will be tested in wet lab, distributed equally among participating teams (300 \u00f7 number of teams)\n\n##
Submission Rules\n\n**Design Requirements:**\n- De novo designs only (no motif scaffolding or lead optimization, except for antibodies)\n- \u226475% sequence identity to known proteins in UniRef50\n-
For antibodies: CDR loops must have \u226475% sequence identity to known antibodies in SAbDab\n- Standard amino acids only\n- Single-chain proteins, \u2264250 amino acids\n- No tags/signal peptides or
formatting characters\n- Maximum 100 sequences per team\n\n**Submission Format:**\n1. Method description PDF (2 pages max): background, approach, in-silico results\n2. Ranked CSV file with: Rank,
Amino Acid Sequences, optional Name/Score\n3. Optional: predicted structure files (zip)\n\n## Timeline\n- **Submission Open:** February 15, 2026\n- **Submission Deadline:** March 26, 2026 (AoE)\n-
**Results Announcement:** April 26, 2026, at Rio de Janeiro (ICLR 2026)\n\n## Testing & Awards\n- Testing: Expression and binding affinity via bio-layer interferometry\n- **Best Designed Binder:**
$1,000 USD + 3D printed protein structure\n- **Runner-up:** $100 USD + 3D printed protein structure\n- All participants receive experimental data and inclusion in open-source dataset on
Proteinbase\n\n## Data Sharing\nResults will be published openly on Proteinbase under ODC-ODbL license (free to use including commercial/ML training with attribution)\n\n---\n\n**Relevant links:**\n-
[GEM](https://www.gembio.ai/)\n- [Adaptyv](https://www.adaptyvbio.com)\n- [Expression experiment details](https://docs.adaptyvbio.com/docs/experiment-types/expression)\n- [Binding affinity experiment
details](https://docs.adaptyvbio.com/docs/experiment-types/binding)\n- [Lessons from Adaptyv's EGFR Competition](https://www.adaptyvbio.com/blog/po102/)\n- [Proteinbase](https://proteinbase.com/)\n-
Contact: [gembioworkshop@googlegroups.com](mailto:gembioworkshop@googlegroups.com)\n- Wet-lab questions: [support@adaptyvbio.com](mailto:support@adaptyvbio.com)", "title": "Competition-2026 \u2014 GEM
Workshop"}
```

## 💭 Thinking

Now I have a good picture of the situation. Let me analyze this carefully.

## Key Facts

### AdaptyvBio Competition History:
1. **EGFR Round 1 (Oct 2024)**: 201 designs tested, 2.5% hit rate
2. **EGFR Round 2 (Dec 2024)**: 400 designs tested, 13-14% hit rate
3. **Nipah (Jan 2026)**: 1,030 designs tested, 9.6% hit rate (harder target)
4. **RBX-1 (2026)**: 300 designs to be tested, results expected April 26, 2026


5. **Individual performers in Nipah varied dramatically**: Escalante's Mosaic achieved 88.8% on a small set of 9 designs, while RFdiffusion hit 21.4% across 42 designs, and BindCraft was much lower—but the question is asking about the overall competition results across all 1,030 tested designs, not individual team performance.

The real challenge becomes clear: for the competition as a whole to exceed 75% success, nearly every participant would need to consistently apply cutting-edge methods across all their designs, which hasn't happened in practice. 2. The target to be relatively "easy"
3. Filtering/selection to be very effective

But in competitions, many participants are newcomers, students, etc. who may use suboptimal methods. The diversity of skill levels pulls the average down.

### Could the competition format change?
- The RBX-1 competition tests only 300 designs (much fewer than Nipah's 1,030)
- Designs are distributed equally among teams
- If teams are better and use more advanced tools, the overall rate could be higher

### Trajectory:
- EGFR R1: 2.5%
- EGFR R2: 14% (5.6x improvement)
- Nipah: 9.6% (lower, but harder target)

The trajectory shows improvement in tools, but the overall competition rates are still far from 75%.

For the YES scenario to materialize, I'd need to see either dramatic tool improvements where state-of-the-art methods reliably hit 90%+ by 2028-2029 and most competitors adopt them, a shift in competition format toward heavy pre-screening or top-team-only events, or a particularly tractable target. The rapid gains we're seeing—jumping from 2.5% to 14% in just two months on EGFR, with methods like BindCraft and individual results like Escalante's 70-80% on other targets—suggest the trajectory is moving in the right direction, though we're still well short of the 75% threshold. /10 = 90% in the Nipah competition

BUT the question is about the ENTIRE competition, not individual participants. The overall rate is dominated by weaker participants.

However... consider:
- As tools improve and become more accessible, the floor rises
- If everyone uses BindCraft or similar tools, even novice users might achieve decent rates
- The RBX-1 competition has only 300 designs across teams - smaller pool

Let me think about what 2027-2029 competitions might look like:
- Tools will continue improving (BindCraft, Mosaic, newer methods)
- More participants will use high-quality open-source tools
- AdaptyvBio might run competitions with different formats

But 75% is still a very high bar for an OVERALL competition. Even if the best tools achieve 90%+, you need the average across ALL participants to exceed 75%.

### Key considerations:
1. **Time horizon**: We're looking at 3.5+ years until the resolution date, and tools have shown dramatic improvement over the past three years—jumping from near-zero to 10-90% success rates. The competition format itself could shift, and as better tools become more widely available, even average participants might see significant gains.

2. **The actual resolution criteria**: I need to focus on what matters—whether >75% of ALL designs selected for experimental testing in a single AdaptyvBio competition qualify as binders, not just top performers. The requirement for novel designs appears to already be standard practice.

3. **The gap problem**: The biggest challenge is that competition-wide hit rates have historically maxed out around 14%, while top performers hit 80-90%. This massive variance suggests that even with better tools, getting the entire field above 75% is a steep climb.

I'm leaning toward NO, but it's not a slam dunk given the rapid pace of improvement and the possibility of format changes.

Now I'm looking at the actual performance distribution from the Nipah competition to ground this in data. The hit rates vary wildly depending on which tool was used—Mosaic dominates at nearly 89%, but most submissions cluster much lower. For an overall rate above 75%, you'd need the vast majority of designs coming from the top-tier tools, which seems unlikely given how many people use the less effective approaches.

Let me think through a more optimistic future scenario. If tools improve significantly by 2028 and participants gravitate toward the best methods, could we hit that 75% threshold? I'm modeling what happens if the best tools reach 95% success, mid-tier tools get to 60%, and even weaker approaches hit 30%—then calculating the weighted average based on how many submissions come from each tier.

That calculation gives me 64.5%, still short of 75%. To actually reach 75%, I'd need the average participant to be performing at 70% or higher, which would require a much more selective competition—maybe something like RBX-1 where only experienced teams submit to a specialized workshop, rather than an open call.

But here's what really matters: the timeline. We're looking at 2028-2029, and the field has been accelerating dramatically. RFdiffusion went from sub-1% in 2022 to 0-34% by 2023-2024, while newer methods like Escalante are already hitting 70-90%. By the time this question resolves, the tools available to participants could be substantially better than what exists today. The real question becomes whether these improved methods become standard enough that average competitors have access to tools reliably hitting 75% success rates.

Looking at the current landscape, open-source tools like BindCraft are already achieving 46% average success, with some targets reaching 100%. If tools like this improve to 70-80% average performance and most participants adopt them, the competition-wide rate could plausibly exceed 75%. The complicating factor is target selection—AdaptyvBio could choose an intrinsically difficult target that even good tools struggle with.

Weighing everything together: the pace of improvement is genuinely remarkable, there's 3.5+ years for further development, and open-source tools are already quite capable. But 75% success across all tested designs is an extremely high bar, and competition-wide rates have never come close to that threshold. I'm settling on around 25-35% probability—the tools are improving fast enough that it's plausible, but the gap between best-case and average-case performance remains substantial.

Actually, I should reconsider a few factors I might be underweighting. Tool democratization is real—as BindCraft and similar tools mature, they become easier to use and more reliable, which could dramatically raise the baseline for average participants. Competition format matters too; if AdaptyvBio runs smaller, more selective competitions like RBX-1, the participant quality shifts upward. And there's something about the trajectory itself—once these tools hit a certain maturity threshold, the improvements could accelerate in ways that are hard to predict.

The cumulative probability angle is important here. Over 3.5 years, AdaptyvBio might run 6-10 competitions total. Even if each individual competition has a modest 5-10% chance of hitting 75% average performance, those odds compound. I'm working through the per-competition probabilities across different years—2026 competitions are probably too early at 1-3% each, but by 2028-2029 we're looking at 10-25% per competition as the tools mature. When I calculate the cumulative probability across multiple attempts, the overall odds become more substantial than my initial 30% estimate suggested. So the cumulative probability works out to 62%, which does feel too optimistic. I'm reconsidering whether my per-competition success estimates are realistic—they might be inflated. The real challenge here is that we're looking at roughly a 5-8x improvement needed in the overall competition rate, jumping from around 14% to over 75%. While the field managed a 5x improvement in two months before, that involved significant learning effects and we're now talking about a fundamentally different scenario where most participants would need to achieve high success rates consistently.

Let me recalibrate with more conservative per-competition estimates across the years, accounting for tool maturation and the widening gap between top and average performers. Running through the math with two competitions annually and these revised rates, the cumulative probability comes out to around 62% by 2029.

But I'm realizing the core issue here: I need to focus on whether the *average* participant will hit that 75% threshold, not just the best performers. Looking at current benchmarks, even state-of-the-art open source tools like BindCraft only manage around 46% success on average across all targets, so there's a substantial gap to close.

Given this reality, I'm revising my probability estimates downward significantly—thinking more like sub-1% for 2026, ramping to maybe 8-12% by 2029—and now I'm calculating what the cumulative probability looks like across multiple competitions per year with these more conservative numbers.

Working through the math, I'm getting around 33% cumulative probability, so I'll settle on the 30-35% range as my estimate. But I'm also reconsidering whether the RBX-1 competition might actually count as an AdaptyvBio event, and wondering if smaller, more specialized competitions with expert participants could shift these numbers higher than my current projections suggest.

The constraint about requiring novel designs is important though—it rules out relying on well-characterized binders. Still, looking at the recent trajectory of improvement in this field, I'm seeing a pretty dramatic acceleration. De novo binder design was barely feasible in 2022, but by late 2024 we're seeing competition success rates jump to 14% overall with top performers hitting 88%, and newer methods like BindCraft, Mosaic, and AlphaProteo are pushing into the 46-90% range depending on the target. This suggests the field is advancing faster than I initially accounted for, so maybe 30% is actually a reasonable middle ground. speed of improvement is remarkable. 3.5 years is a long time in this field. I think 30% is reasonable, maybe even slightly conservative.

Let me also consider: what would happen if tools like BindCraft become the default, and everyone uses them with minimal modification? If BindCraft achieves 46% average, that's still far from 75%. But BindCraft is already a year old, and newer methods may be significantly better.

I'll go with 30% as my estimate.

Actually, let me reconsider once more. I want to make sure I'm not anchoring too much on the current competition-wide rates. The question is asking about a future where tools have continued to improve. The improvement trajectory has been exponential—from 0.1% to 2.5% to 14% in the main competition, and even more dramatic for the best tools. But 75% is still a very high bar for a competition average, and with 3.5 years and potentially 6-10+ more competitions ahead, I need to think through this more rigorously. Let me set up a Monte Carlo simulation to test different growth scenarios.

## 💬 Response

Now let me run some quantitative analysis to model the trajectory and probability.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Model the trajectory of protein binder competition success rates\n# and estimate probability of exceeding 75% before 2030\n\n# Historical data points (competition-wide rates)\n# EGFR R1 (Oct 2024): 2.5% (n=201)\n# EGFR R2 (Dec 2024): 14% (n=400) \n# Nipah (Jan 2026): 9.6% (n=1030, harder target)\n\n# Individual top performers in Nipah:\n# Escalante Mosaic: 88.8% (n=9)\n# RFdiffusion: 21.4% (n=42)\n# BindCraft: 5.68% (n=88)\n# BoltzGen: 1.23% (n=163)\n\n# Key insight: competition-wide rate is dominated by many participants\n# using suboptimal methods, but the best tools already exceed 75%\n\n# Let's model this with a simulation\nnp.random.seed(42)\nn_sims = 100000\n\n# For each competition, model the overall hit rate as a mixture\n# of \"good tool\" users and \"mediocre tool\" users\n\n# Assumptions for tool improvement over time:\n# - Best tools improve from ~90% \u2192 ~95%+ \n# - Average tools improve from ~15% \u2192 ~50%+\n# - Worst tools improve from ~2% \u2192 ~20%+\n# - The fraction of participants using good tools increases over time\n\n# Time points (years from now, April 2026)\n# Competitions likely: ~2 per year = ~7-8 competitions by end of 2029\n\ndef simulate_competition(year_offset, n_designs=500, n_sims=100000):\n    \"\"\"\n    Simulate a single competition at year_offset from now.\n    Returns fraction of simulations where >75% of designs are binders.\n    \"\"\"\n    results = np.zeros(n_sims)\n    \n    for sim in range(n_sims):\n        # Tool quality improves over time (logistic-ish growth)\n        # Best tool hit rate\n        best_rate = min(0.95, 0.88 + 0.02 * year_offset + np.random.normal(0, 0.05))\n        best_rate = np.clip(best_rate, 0.5, 0.99)\n        \n        # Average tool hit rate (significant improvement expected)\n        avg_rate = min(0.85, 0.15 + 0.12 * year_offset + np.random.normal(0, 0.08))\n        avg_rate = np.clip(avg_rate, 0.05, 0.95)\n        \n        # Worst tool hit rate\n        worst_rate = min(0.6, 0.03 + 0.06 * year_offset + np.random.normal(0, 0.05))\n        worst_rate = np.clip(worst_rate, 0.01, 0.8)\n        \n        # Fraction using good tools increases over time\n        frac_best = min(0.5, 0.15 + 0.07 * year_offset + np.random.normal(0, 0.05))\n        frac_best = np.clip(frac_best, 0.05, 0.7)\n        \n        frac_worst = max(0.1, 0.4 - 0.06 * year_offset + np.random.normal(0, 0.05))\n        frac_worst = np.clip(frac_worst, 0.05, 0.5)\n        \n        frac_avg = 1 - frac_best - frac_worst\n        frac_avg = max(frac_avg, 0.1)\n        # renormalize\n        total = frac_best + frac_avg + frac_worst\n        frac_best /= total\n        frac_avg /= total\n        frac_worst /= total\n        \n        # Target difficulty factor (random, some targets are harder)\n        target_difficulty = np.random.uniform(0.5, 1.2)  # multiplier on hit rates\n        \n        # Overall competition hit rate\n        overall_rate = (frac_best * best_rate + frac_avg * avg_rate + frac_worst * worst_rate) * target_difficulty\n        overall_rate = np.clip(overall_rate, 0.01, 0.99)\n        \n        # Add sampling noise (binomial)\n        n_binders = np.random.binomial(n_designs, overall_rate)\n        results[sim] = n_binders / n_designs\n    \n    p_above_75 = np.mean(results > 0.75)\n    return p_above_75, results\n\n# Simulate for each half-year point\nprint(\"Per-competition probability of >75% hit rate:\")\nprint(\"=\" * 60)\n\ncompetitions = [\n    (0.0, \"RBX-1 (Apr 2026)\", 300),\n    (0.5, \"Late 2026\", 400),\n    (1.0, \"Early 2027\", 500),\n    (1.5, \"Late 2027\", 500),\n    (2.0, \"Early 2028\", 500),\n    (2.5, \"Late 2028\", 500),\n    (3.0, \"Early 2029\", 500),\n    (3.5, \"Late 2029\", 500),\n]\n\nper_comp_probs = []\nfor offset, name, n_designs in competitions:\n    p, results = simulate_competition(offset, n_designs)\n    per_comp_probs.append(p)\n    print(f\"  {name} (t+{offset}y): P(>75%) = {p:.4f} ({p*100:.1f}%), \"\n          f\"median rate = {np.median(results):.3f}, \"\n          f\"p90 = {np.percentile(results, 90):.3f}\")\n\n# Cumulative probability (at least one competition exceeds 75%)\np_none = 1.0\nfor p in per_comp_probs:\n    p_none *= (1 - p)\n\np_at_least_one = 1 - p_none\nprint(f\"\\nCumulative P(at least one >75%): {p_at_least_one:.4f} ({p_at_least_one*100:.1f}%)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Per-competition probability of >75% hit rate:\n============================================================\n  RBX-1 (Apr 2026) (t+0.0y): P(>75%) = 0.0000 (0.0%), median
rate = 0.177, p90 = 0.277\n  Late 2026 (t+0.5y): P(>75%) = 0.0000 (0.0%), median rate = 0.233, p90 = 0.343\n  Early 2027 (t+1.0y): P(>75%) = 0.0000 (0.0%), median rate = 0.288, p90 = 0.412\n  Late
2027 (t+1.5y): P(>75%) = 0.0000 (0.0%), median rate = 0.344, p90 = 0.480\n  Early 2028 (t+2.0y): P(>75%) = 0.0000 (0.0%), median rate = 0.398, p90 = 0.548\n  Late 2028 (t+2.5y): P(>75%) = 0.0016
(0.2%), median rate = 0.450, p90 = 0.616\n  Early 2029 (t+3.0y): P(>75%) = 0.0183 (1.8%), median rate = 0.502, p90 = 0.678\n  Late 2029 (t+3.5y): P(>75%) = 0.0811 (8.1%), median rate = 0.550, p90 =
0.740\n\nCumulative P(at least one >75%): 0.0994 (9.9%)\n", "stderr": "", "duration_ms": 13326}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# My model might be too conservative on the rate of tool improvement.\n# Let me also model a more optimistic scenario and a scenario where \n# competition format changes (smaller, more expert competitions)\n\n# Alternative 1: Faster tool improvement (exponential rather than linear)\ndef simulate_competition_v2(year_offset, n_designs=500, n_sims=100000, \n                            scenario=\"base\"):\n    results = np.zeros(n_sims)\n    \n    for sim in range(n_sims):\n        if scenario == \"base\":\n            # Linear improvement\n            best_rate = np.clip(0.88 + 0.02 * year_offset + np.random.normal(0, 0.05), 0.5, 0.99)\n            avg_rate = np.clip(0.15 + 0.12 * year_offset + np.random.normal(0, 0.08), 0.05, 0.95)\n            worst_rate = np.clip(0.03 + 0.06 * year_offset + np.random.normal(0, 0.05), 0.01, 0.8)\n            frac_best = np.clip(0.15 + 0.07 * year_offset + np.random.normal(0, 0.05), 0.05, 0.7)\n            frac_worst = np.clip(0.4 - 0.06 * year_offset + np.random.normal(0, 0.05), 0.05, 0.5)\n            \n        elif scenario == \"fast_improvement\":\n            # Faster improvement - tools become commoditized\n            improvement_factor = 1.5  # 50% faster\n            best_rate = np.clip(0.88 + 0.03 * year_offset + np.random.normal(0, 0.04), 0.6, 0.99)\n            avg_rate = np.clip(0.15 + 0.18 * year_offset + np.random.normal(0, 0.08), 0.05, 0.95)\n            worst_rate = np.clip(0.03 + 0.10 * year_offset + np.random.normal(0, 0.05), 0.01, 0.8)\n            frac_best = np.clip(0.15 + 0.10 * year_offset + np.random.normal(0, 0.05), 0.05, 0.7)\n            frac_worst = np.clip(0.4 - 0.10 * year_offset + np.random.normal(0, 0.05), 0.05, 0.5)\n            \n        elif scenario == \"expert_competition\":\n            # Small competition with only expert teams\n            best_rate = np.clip(0.90 + 0.025 * year_offset + np.random.normal(0, 0.04), 0.6, 0.99)\n            avg_rate = np.clip(0.40 + 0.10 * year_offset + np.random.normal(0, 0.08), 0.1, 0.95)\n            worst_rate = np.clip(0.15 + 0.08 * year_offset + np.random.normal(0, 0.05), 0.05, 0.8)\n            frac_best = np.clip(0.30 + 0.08 * year_offset + np.random.normal(0, 0.05), 0.1, 0.7)\n            frac_worst = np.clip(0.20 - 0.05 * year_offset + np.random.normal(0, 0.03), 0.05, 0.4)\n        \n        frac_avg = max(0.1, 1 - frac_best - frac_worst)\n        total = frac_best + frac_avg + frac_worst\n        frac_best /= total\n        frac_avg /= total\n        frac_worst /= total\n        \n        # Target difficulty\n        target_difficulty = np.random.uniform(0.5, 1.2)\n        \n        overall_rate = (frac_best * best_rate + frac_avg * avg_rate + frac_worst * worst_rate) * target_difficulty\n        overall_rate = np.clip(overall_rate, 0.01, 0.99)\n        \n        n_binders = np.random.binomial(n_designs, overall_rate)\n        results[sim] = n_binders / n_designs\n    \n    return np.mean(results > 0.75), results\n\nprint(\"SCENARIO ANALYSIS\")\nprint(\"=\" * 70)\n\nfor scenario_name in [\"base\", \"fast_improvement\", \"expert_competition\"]:\n    print(f\"\\n--- Scenario: {scenario_name} ---\")\n    per_comp_probs = []\n    for offset, name, n_designs in competitions:\n        # Expert competitions are smaller\n        if scenario_name == \"expert_competition\":\n            n_designs = 200\n        p, results = simulate_competition_v2(offset, n_designs, scenario=scenario_name)\n        per_comp_probs.append(p)\n        if offset in [0.0, 1.0, 2.0, 3.0, 3.5]:\n            print(f\"  {name}: P(>75%) = {p*100:.1f}%, median = {np.median(results):.3f}\")\n    \n    p_none = 1.0\n    for p in per_comp_probs:\n        p_none *= (1 - p)\n    print(f\"  Cumulative P(at least one >75%): {(1-p_none)*100:.1f}%\")\n\n# Combined estimate: weight scenarios\n# Base: 40%, Fast improvement: 35%, Expert competition format: 25%\nbase_probs = []\nfast_probs = []\nexpert_probs = []\n\nfor offset, name, n_designs in competitions:\n    p_base, _ = simulate_competition_v2(offset, n_designs, scenario=\"base\")\n    p_fast, _ = simulate_competition_v2(offset, n_designs, scenario=\"fast_improvement\")\n    p_expert, _ = simulate_competition_v2(offset, 200, scenario=\"expert_competition\")\n    base_probs.append(p_base)\n    fast_probs.append(p_fast)\n    expert_probs.append(p_expert)\n\n# For each scenario, compute cumulative probability\ndef cumulative_p(probs):\n    p_none = 1.0\n    for p in probs:\n        p_none *= (1 - p)\n    return 1 - p_none\n\ncum_base = cumulative_p(base_probs)\ncum_fast = cumulative_p(fast_probs)\ncum_expert = cumulative_p(expert_probs)\n\n# Combined estimate (not independent - some competitions might be both expert AND fast improvement)\n# Take a weighted combination but also account for the possibility that competitions \n# are of different types\nprint(f\"\\n\\nCOMBINED ESTIMATE\")\nprint(f\"  Base scenario cumulative: {cum_base*100:.1f}%\")\nprint(f\"  Fast improvement cumulative: {cum_fast*100:.1f}%\")\nprint(f\"  Expert competition cumulative: {cum_expert*100:.1f}%\")\n\n# P(YES) = weighted by scenario probability\n# But scenarios aren't mutually exclusive - need to think about this differently\n# The real question is: across all competitions, considering all possible scenarios\n\n# Better approach: for each competition, there's some probability it's an expert-only\n# format and some probability tools have improved faster\n# Let's just combine at the per-competition level\n\ncombined_per_comp = []\nfor i in range(len(competitions)):\n    # For each competition, take max of the three scenario probabilities\n    # weighted by scenario likelihood\n    # P(>75% in comp i) = P(base) * P(>75%|base) + P(fast) * P(>75%|fast) + P(expert) * P(>75%|expert)\n    # Scenario weights might change over time\n    p_combined = 0.40 * base_probs[i] + 0.35 * fast_probs[i] + 0.25 * expert_probs[i]\n    combined_per_comp.append(p_combined)\n\ncum_combined = cumulative_p(combined_per_comp)\nprint(f\"\\n  Weighted combined cumulative: {cum_combined*100:.1f}%\")\n"
}
```

### 📋 Result

```
Code execution timed out after 30 seconds
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\n\n# Vectorized simulation for speed\ndef simulate_competition_fast(year_offset, n_designs=500, n_sims=100000, scenario=\"base\"):\n    if scenario == \"base\":\n        best_rate = np.clip(0.88 + 0.02*year_offset + np.random.normal(0, 0.05, n_sims), 0.5, 0.99)\n        avg_rate = np.clip(0.15 + 0.12*year_offset + np.random.normal(0, 0.08, n_sims), 0.05, 0.95)\n        worst_rate = np.clip(0.03 + 0.06*year_offset + np.random.normal(0, 0.05, n_sims), 0.01, 0.8)\n        frac_best = np.clip(0.15 + 0.07*year_offset + np.random.normal(0, 0.05, n_sims), 0.05, 0.7)\n        frac_worst = np.clip(0.4 - 0.06*year_offset + np.random.normal(0, 0.05, n_sims), 0.05, 0.5)\n    elif scenario == \"fast_improvement\":\n        best_rate = np.clip(0.88 + 0.03*year_offset + np.random.normal(0, 0.04, n_sims), 0.6, 0.99)\n        avg_rate = np.clip(0.15 + 0.18*year_offset + np.random.normal(0, 0.08, n_sims), 0.05, 0.95)\n        worst_rate = np.clip(0.03 + 0.10*year_offset + np.random.normal(0, 0.05, n_sims), 0.01, 0.8)\n        frac_best = np.clip(0.15 + 0.10*year_offset + np.random.normal(0, 0.05, n_sims), 0.05, 0.7)\n        frac_worst = np.clip(0.4 - 0.10*year_offset + np.random.normal(0, 0.05, n_sims), 0.05, 0.5)\n    elif scenario == \"expert\":\n        best_rate = np.clip(0.90 + 0.025*year_offset + np.random.normal(0, 0.04, n_sims), 0.6, 0.99)\n        avg_rate = np.clip(0.40 + 0.10*year_offset + np.random.normal(0, 0.08, n_sims), 0.1, 0.95)\n        worst_rate = np.clip(0.15 + 0.08*year_offset + np.random.normal(0, 0.05, n_sims), 0.05, 0.8)\n        frac_best = np.clip(0.30 + 0.08*year_offset + np.random.normal(0, 0.05, n_sims), 0.1, 0.7)\n        frac_worst = np.clip(0.20 - 0.05*year_offset + np.random.normal(0, 0.03, n_sims), 0.05, 0.4)\n\n    frac_avg = np.maximum(0.1, 1 - frac_best - frac_worst)\n    total = frac_best + frac_avg + frac_worst\n    frac_best /= total; frac_avg /= total; frac_worst /= total\n\n    target_difficulty = np.random.uniform(0.5, 1.2, n_sims)\n    overall_rate = (frac_best*best_rate + frac_avg*avg_rate + frac_worst*worst_rate) * target_difficulty\n    overall_rate = np.clip(overall_rate, 0.01, 0.99)\n    \n    n_binders = np.random.binomial(n_designs, overall_rate)\n    hit_rates = n_binders / n_designs\n    \n    return np.mean(hit_rates > 0.75), np.median(hit_rates), np.percentile(hit_rates, 90)\n\ncompetitions = [\n    (0.0, \"RBX-1 Apr 2026\", 300),\n    (0.5, \"Late 2026\", 400),\n    (1.0, \"Early 2027\", 500),\n    (1.5, \"Late 2027\", 500),\n    (2.0, \"Early 2028\", 500),\n    (2.5, \"Late 2028\", 500),\n    (3.0, \"Early 2029\", 500),\n    (3.5, \"Late 2029\", 500),\n]\n\nprint(\"SCENARIO ANALYSIS\")\nprint(\"=\"*70)\n\nall_scenario_probs = {}\nfor scenario in [\"base\", \"fast_improvement\", \"expert\"]:\n    print(f\"\\n--- {scenario} ---\")\n    probs = []\n    for offset, name, n_des in competitions:\n        nd = 200 if scenario == \"expert\" else n_des\n        p, med, p90 = simulate_competition_fast(offset, nd, scenario=scenario)\n        probs.append(p)\n        print(f\"  {name}: P(>75%)={p*100:.1f}%, med={med:.3f}, p90={p90:.3f}\")\n    \n    cum = 1 - np.prod([1-p for p in probs])\n    print(f\"  CUMULATIVE: {cum*100:.1f}%\")\n    all_scenario_probs[scenario] = probs\n\n# Weighted combination\n# P(base)=0.40, P(fast)=0.35, P(expert)=0.25\ncombined_per_comp = []\nfor i in range(len(competitions)):\n    p = (0.40 * all_scenario_probs[\"base\"][i] + \n         0.35 * all_scenario_probs[\"fast_improvement\"][i] + \n         0.25 * all_scenario_probs[\"expert\"][i])\n    combined_per_comp.append(p)\n\ncum_combined = 1 - np.prod([1-p for p in combined_per_comp])\nprint(f\"\\nWEIGHTED COMBINED CUMULATIVE: {cum_combined*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "SCENARIO ANALYSIS\n======================================================================\n\n--- base ---\n  RBX-1 Apr 2026: P(>75%)=0.0%, med=0.180, p90=0.277\n  Late
2026: P(>75%)=0.0%, med=0.233, p90=0.345\n  Early 2027: P(>75%)=0.0%, med=0.290, p90=0.414\n  Late 2027: P(>75%)=0.0%, med=0.346, p90=0.484\n  Early 2028: P(>75%)=0.0%, med=0.400, p90=0.552\n  Late
2028: P(>75%)=0.2%, med=0.454, p90=0.620\n  Early 2029: P(>75%)=2.3%, med=0.504, p90=0.682\n  Late 2029: P(>75%)=9.2%, med=0.554, p90=0.746\n  CUMULATIVE: 11.4%\n\n--- fast_improvement ---\n  RBX-1
Apr 2026: P(>75%)=0.0%, med=0.180, p90=0.277\n  Late 2026: P(>75%)=0.0%, med=0.263, p90=0.380\n  Early 2027: P(>75%)=0.0%, med=0.348, p90=0.486\n  Late 2027: P(>75%)=0.1%, med=0.432, p90=0.590\n
Early 2028: P(>75%)=2.9%, med=0.510, p90=0.690\n  Late 2028: P(>75%)=16.4%, med=0.586, p90=0.788\n  Early 2029: P(>75%)=32.6%, med=0.656, p90=0.878\n  Late 2029: P(>75%)=44.9%, med=0.720, p90=0.960\n
CUMULATIVE: 69.8%\n\n--- expert ---\n  RBX-1 Apr 2026: P(>75%)=0.1%, med=0.420, p90=0.585\n  Late 2026: P(>75%)=0.8%, med=0.475, p90=0.650\n  Early 2027: P(>75%)=4.7%, med=0.525, p90=0.710\n  Late
2027: P(>75%)=13.5%, med=0.575, p90=0.775\n  Early 2028: P(>75%)=23.9%, med=0.620, p90=0.830\n  Late 2028: P(>75%)=33.4%, med=0.660, p90=0.885\n  Early 2029: P(>75%)=40.7%, med=0.700, p90=0.935\n
Late 2029: P(>75%)=46.8%, med=0.735, p90=0.975\n  CUMULATIVE: 86.9%\n\nWEIGHTED COMBINED CUMULATIVE: 59.4%\n", "stderr": "", "duration_ms": 379}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The model assumptions deserve scrutiny. Let me check calibration:\n# 1. Does the model produce ~10% overall rate at t=0 (matching current data)?\n# 2. Is the \"fast improvement\" scenario realistic?\n# 3. What scenario weights make sense?\n\n# Calibration check: the base scenario at t=0 gives median 18%, \n# which is slightly above the Nipah competition (9.6%) and EGFR R2 (14%)\n# This is because my \"base\" model doesn't account well for target difficulty\n# (Nipah was harder), but is in the right ballpark.\n\n# Let me also think about key assumptions:\n# 1. Target difficulty range [0.5, 1.2] - this is crucial\n#    0.5 means the target cuts all rates in half\n#    1.2 means slightly favorable target\n# 2. The \"expert\" scenario assumes only experienced teams participate\n# 3. \"Fast improvement\" assumes tools improve 1.5x faster\n\n# Let me reconsider scenario weights more carefully:\n# - Will AdaptyvBio always run open competitions? Or will some be expert-only?\n# - The RBX-1 is already a workshop competition (GEM x Adaptyv) \u2192 expert-like\n# - But the big competitions (EGFR, Nipah) are open to all\n\n# Key question: will AdaptyvBio run any expert-only competitions?\n# Evidence: RBX-1 IS one. So the probability of at least one more is high.\n# But even expert competitions need >75% overall.\n\n# Revised scenario weights:\n# - Pure base (open competition, linear tool improvement): 30%\n# - Fast improvement (tools commoditize faster): 30%  \n# - Expert competition (smaller, curated): 15%\n# - Expert + fast improvement (best case): 15%\n# - No more competitions / AdaptyvBio stops: 10%\n\n# Let me also consider: does AdaptyvBio continue running competitions?\n# They've run 3 in ~1.5 years, plus RBX-1. Likely to continue.\n# But there's some risk they pivot, run out of funding, etc.\n# P(AdaptyvBio continues running binder competitions through 2029) ~ 80%\n\n# For the \"expert + fast\" scenario\nexpert_fast_probs = []\nfor offset, name, n_des in competitions:\n    best_rate = np.clip(0.90 + 0.03*offset + np.random.normal(0, 0.03, 100000), 0.7, 0.99)\n    avg_rate = np.clip(0.40 + 0.15*offset + np.random.normal(0, 0.07, 100000), 0.15, 0.95)\n    worst_rate = np.clip(0.15 + 0.10*offset + np.random.normal(0, 0.04, 100000), 0.05, 0.85)\n    frac_best = np.clip(0.35 + 0.08*offset + np.random.normal(0, 0.04, 100000), 0.15, 0.7)\n    frac_worst = np.clip(0.15 - 0.04*offset + np.random.normal(0, 0.03, 100000), 0.05, 0.3)\n    frac_avg = np.maximum(0.1, 1 - frac_best - frac_worst)\n    total = frac_best + frac_avg + frac_worst\n    frac_best /= total; frac_avg /= total; frac_worst /= total\n    target_difficulty = np.random.uniform(0.5, 1.2, 100000)\n    overall = (frac_best*best_rate + frac_avg*avg_rate + frac_worst*worst_rate) * target_difficulty\n    overall = np.clip(overall, 0.01, 0.99)\n    hits = np.random.binomial(200, overall) / 200\n    p = np.mean(hits > 0.75)\n    expert_fast_probs.append(p)\n    print(f\"  Expert+Fast {name}: P(>75%)={p*100:.1f}%\")\n\ncum_ef = 1 - np.prod([1-p for p in expert_fast_probs])\nprint(f\"  Expert+Fast cumulative: {cum_ef*100:.1f}%\")\n\n# Final weighted estimate\n# Weights: base=0.30, fast=0.30, expert=0.15, expert_fast=0.15, none=0.10\n# \"none\" scenario means P(>75%) = 0\n\nfinal_per_comp = []\nfor i in range(len(competitions)):\n    p = (0.30 * all_scenario_probs[\"base\"][i] + \n         0.30 * all_scenario_probs[\"fast_improvement\"][i] + \n         0.15 * all_scenario_probs[\"expert\"][i] + \n         0.15 * expert_fast_probs[i] +\n         0.10 * 0)  # no more competitions\n    final_per_comp.append(p)\n\ncum_final = 1 - np.prod([1-p for p in final_per_comp])\n\n# But also need to account for P(AdaptyvBio still running) ~ 80%\n# Actually, the \"none\" scenario already captures this\n\nprint(f\"\\nFINAL WEIGHTED CUMULATIVE: {cum_final*100:.1f}%\")\n\n# Sensitivity analysis\nprint(\"\\nSENSITIVITY: Target difficulty range\")\nfor low, high in [(0.4, 1.0), (0.5, 1.2), (0.6, 1.3), (0.7, 1.4)]:\n    # Just for late 2029 base scenario\n    best_rate = np.clip(0.88 + 0.07 + np.random.normal(0, 0.05, 100000), 0.5, 0.99)\n    avg_rate = np.clip(0.15 + 0.42 + np.random.normal(0, 0.08, 100000), 0.05, 0.95)\n    worst_rate = np.clip(0.03 + 0.21 + np.random.normal(0, 0.05, 100000), 0.01, 0.8)\n    frac_best = np.clip(0.15 + 0.245 + np.random.normal(0, 0.05, 100000), 0.05, 0.7)\n    frac_worst = np.clip(0.4 - 0.21 + np.random.normal(0, 0.05, 100000), 0.05, 0.5)\n    frac_avg = np.maximum(0.1, 1 - frac_best - frac_worst)\n    total = frac_best + frac_avg + frac_worst\n    frac_best /= total; frac_avg /= total; frac_worst /= total\n    td = np.random.uniform(low, high, 100000)\n    overall = (frac_best*best_rate + frac_avg*avg_rate + frac_worst*worst_rate) * td\n    overall = np.clip(overall, 0.01, 0.99)\n    hits = np.random.binomial(500, overall) / 500\n    p = np.mean(hits > 0.75)\n    print(f\"  [{low}, {high}]: P(>75%) = {p*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "  Expert+Fast RBX-1 Apr 2026: P(>75%)=0.2%\n  Expert+Fast Late 2026: P(>75%)=3.2%\n  Expert+Fast Early 2027: P(>75%)=14.0%\n  Expert+Fast Late 2027: P(>75%)=27.1%\n
Expert+Fast Early 2028: P(>75%)=37.7%\n  Expert+Fast Late 2028: P(>75%)=46.2%\n  Expert+Fast Early 2029: P(>75%)=52.4%\n  Expert+Fast Late 2029: P(>75%)=56.3%\n  Expert+Fast cumulative: 95.8%\n\nFINAL
WEIGHTED CUMULATIVE: 65.0%\n\nSENSITIVITY: Target difficulty range\n  [0.4, 1.0]: P(>75%) = 0.1%\n  [0.5, 1.2]: P(>75%) = 9.3%\n  [0.6, 1.3]: P(>75%) = 21.7%\n  [0.7, 1.4]: P(>75%) = 35.7%\n",
"stderr": "", "duration_ms": 158}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me think more carefully about my assumptions and whether the model is well-calibrated\n\n# KEY REALITY CHECK:\n# Current best overall competition rate: 14% (EGFR R2)\n# Current best INDIVIDUAL performer: 90% (9/10, Escalante in Nipah)\n# Gap between best individual and overall: ~76 percentage points\n# \n# For overall >75%, need this gap to shrink dramatically\n#\n# Two paths:\n# 1. Everyone gets better \u2192 floor rises toward ceiling\n# 2. Competition becomes expert-only \u2192 ceiling IS the average\n#\n# The \"target difficulty\" factor is also crucial:\n# - BindCraft achieves 10-100% depending on target\n# - AlphaProteo: 0% on TNF\u03b1, 88% on BHRF1\n# - Some targets are just hard regardless of tool quality\n\n# Let me reconsider my scenario weights:\n# The \"fast improvement\" scenario assumes avg_rate goes from 15% to \n# 15% + 0.18*3.5 = 78% by late 2029. Is this realistic?\n# \n# Currently (2026): average tool user achieves ~10-15% on competition targets\n# BindCraft average across targets: ~46% (but this is best tool, easy targets)\n# \n# For average participants to reach 78% by 2029, tools need to improve substantially\n# AND become easier to use. This IS the trend, but the magnitude is uncertain.\n\n# I think the \"fast improvement\" scenario is plausible but optimistic (30% weight OK)\n# The \"expert\" scenario depends on AdaptyvBio running small expert competitions\n# RBX-1 is evidence they do this sometimes\n\n# Let me also consider: what if the question is asking about something that\n# ALREADY qualifies? Escalante got 9/10 in Nipah. But that's just their \n# individual submission, not the overall competition. The question clearly\n# asks about ALL tested designs.\n\n# Final estimate: ~25-30% seems right\n# My model gives 65% with these scenario weights, but I think my model\n# overestimates the rate of improvement.\n\n# The model's \"avg_rate\" parameter increasing by 12-18 pp per year is aggressive.\n# In reality, tool improvement is fast but uneven, and target difficulty \n# creates a hard ceiling on some competitions.\n\n# Let me try more conservative improvement rates\nprint(\"CONSERVATIVE MODEL\")\nprint(\"=\"*60)\n\nconservative_probs = []\nfor offset, name, n_des in competitions:\n    # Slower improvement\n    best_rate = np.clip(0.88 + 0.015*offset + np.random.normal(0, 0.05, 100000), 0.5, 0.99)\n    avg_rate = np.clip(0.12 + 0.08*offset + np.random.normal(0, 0.10, 100000), 0.03, 0.90)\n    worst_rate = np.clip(0.02 + 0.04*offset + np.random.normal(0, 0.04, 100000), 0.005, 0.6)\n    frac_best = np.clip(0.10 + 0.05*offset + np.random.normal(0, 0.05, 100000), 0.03, 0.6)\n    frac_worst = np.clip(0.45 - 0.05*offset + np.random.normal(0, 0.05, 100000), 0.1, 0.6)\n    frac_avg = np.maximum(0.1, 1 - frac_best - frac_worst)\n    total = frac_best + frac_avg + frac_worst\n    frac_best /= total; frac_avg /= total; frac_worst /= total\n    td = np.random.uniform(0.4, 1.15, 100000)\n    overall = (frac_best*best_rate + frac_avg*avg_rate + frac_worst*worst_rate) * td\n    overall = np.clip(overall, 0.01, 0.99)\n    hits = np.random.binomial(n_des, overall) / n_des\n    p = np.mean(hits > 0.75)\n    conservative_probs.append(p)\n    print(f\"  {name}: P(>75%)={p*100:.2f}%, med={np.median(hits):.3f}\")\n\ncum_cons = 1 - np.prod([1-p for p in conservative_probs])\nprint(f\"  Conservative cumulative: {cum_cons*100:.1f}%\")\n\n# Final synthesis: \n# Conservative model: ~5%\n# Base model: ~11%\n# Fast improvement: ~70%\n# Expert: ~87%\n# Expert + fast: ~96%\n\n# My credences:\n# Conservative (slow tool improvement, hard targets): 25%\n# Base (moderate improvement): 30%\n# Fast improvement: 20%\n# Expert competitions: 10%  \n# Expert + fast: 5%\n# No more competitions: 10%\n\nfinal_p = 0.25 * cum_cons + 0.30 * 0.114 + 0.20 * 0.698 + 0.10 * 0.869 + 0.05 * 0.958 + 0.10 * 0\nprint(f\"\\nFINAL WEIGHTED ESTIMATE: {final_p*100:.1f}%\")\n\n# This gives the probability across all competitions, all scenarios\nprint(f\"\\nScenario breakdown:\")\nprint(f\"  Conservative (25%): {cum_cons*100:.1f}%\")\nprint(f\"  Base (30%):         {0.114*100:.1f}%\")\nprint(f\"  Fast (20%):         {0.698*100:.1f}%\")\nprint(f\"  Expert (10%):       {0.869*100:.1f}%\")\nprint(f\"  Expert+Fast (5%):   {0.958*100:.1f}%\")\nprint(f\"  No more comps (10%): 0.0%\")\nprint(f\"  Weighted:           {final_p*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "CONSERVATIVE MODEL\n============================================================\n  RBX-1 Apr 2026: P(>75%)=0.00%, med=0.117\n  Late 2026: P(>75%)=0.00%, med=0.150\n  Early
2027: P(>75%)=0.00%, med=0.186\n  Late 2027: P(>75%)=0.00%, med=0.222\n  Early 2028: P(>75%)=0.00%, med=0.258\n  Late 2028: P(>75%)=0.00%, med=0.294\n  Early 2029: P(>75%)=0.00%, med=0.330\n  Late
2029: P(>75%)=0.00%, med=0.366\n  Conservative cumulative: 0.0%\n\nFINAL WEIGHTED ESTIMATE: 30.9%\n\nScenario breakdown:\n  Conservative (25%): 0.0%\n  Base (30%):         11.4%\n  Fast (20%):
69.8%\n  Expert (10%):       86.9%\n  Expert+Fast (5%):   95.8%\n  No more comps (10%): 0.0%\n  Weighted:           30.9%\n", "stderr": "", "duration_ms": 111}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me sanity-check my \"fast improvement\" scenario more carefully.\n# Is it realistic that average tool hit rate goes from 15% to 78% in 3.5 years?\n\n# Data points on tool improvement:\n# - Rosetta era (<2022): <0.1% success\n# - RFdiffusion (2023): 0-34% depending on target  \n# - AlphaProteo (Sep 2024): 9-88% but closed source\n# - BindCraft (published 2025): 10-100%, avg ~46%, OPEN SOURCE\n# - Mosaic/Escalante (2025-2026): 70-90% on tested targets\n# - Latent-X (Jul 2025 preprint): claims 90-100% macrocyclic, 10-64% mini-binder\n\n# The improvement from Rosetta to BindCraft in ~3 years is ~100x\n# But further improvement from 46% avg to 80%+ is harder (diminishing returns)\n\n# Key question: will \"average participant\" in a competition use BindCraft \n# or equivalent by default?\n# In Nipah, BindCraft had only 5.68% success. Why so low?\n# - Could be target difficulty (Nipah is hard)\n# - Could be suboptimal usage\n# - Could be that BindCraft published results are cherry-picked\n\n# Actually, BindCraft in the Nipah competition (5.68%, n=88) performed much \n# worse than the paper claims (10-100%). This suggests:\n# 1. Nipah was a hard target\n# 2. Competition settings may not be optimized\n# 3. Published results may be on easier targets\n\n# This is sobering. It means even the BEST OPEN SOURCE TOOL achieved only \n# 5.68% in a real competition setting. Individual optimization (Escalante's\n# approach) matters enormously.\n\n# For the overall rate to reach 75%, you need MOST participants to achieve\n# 70%+ individually. Currently, only 1 team did that in Nipah.\n\n# Revised assessment: I think the \"fast improvement\" scenario is too \n# optimistic in its assumptions. Let me revise it.\n\n# More realistic \"fast improvement\":\n# avg_rate starts at 0.10 (not 0.15) and grows by 0.12/year (not 0.18)\n# This gives avg_rate of 0.10 + 0.42 = 0.52 by late 2029\n\n# And the \"base\" scenario: avg grows by 0.08/year\n# avg_rate = 0.10 + 0.28 = 0.38 by late 2029\n\n# Hmm, but my model already has these values approximately.\n# The issue is more about the scenario weights.\n\n# Let me reconsider: what's the probability of the \"fast improvement\" scenario?\n# This would require:\n# - New open-source tools that are significantly better than BindCraft\n# - These tools being widely adopted\n# - The tools working on diverse targets including hard ones\n\n# I think P(fast improvement) ~ 25-30% over 3.5 years is reasonable\n# The field IS moving fast, and there are many teams working on it\n\n# For \"expert competition\":\n# This requires AdaptyvBio to run a small competition with expert teams\n# RBX-1 is evidence this happens. P ~ 15-20% that at least one \n# future competition is expert-only AND hits >75%\n\n# I think my estimate of ~30% is in the right range.\n# Let me also consider what prediction markets say.\n\n# Summary of my analysis:\nprint(\"SUMMARY OF ANALYSIS\")\nprint(\"=\"*60)\nprint()\nprint(\"Key data points:\")\nprint(\"  - Current best competition-wide rate: 14% (EGFR R2)\")\nprint(\"  - Current best individual performer: 90% (Escalante, Nipah)\")\nprint(\"  - BindCraft on Nipah (competition): 5.7%\")\nprint(\"  - BindCraft claimed avg across targets: ~46%\")\nprint(\"  - Gap from 14% to 75% = 61 percentage points\")\nprint()\nprint(\"Paths to YES:\")\nprint(\"  1. Tools improve so avg participant gets >75% (requires 5x improvement)\")\nprint(\"  2. Expert-only competition with top teams (requires format change)\")\nprint(\"  3. Very easy target where most methods work well\")\nprint()\nprint(\"Key uncertainties:\")\nprint(\"  - Rate of tool improvement (exponential? linear? plateauing?)\")\nprint(\"  - Competition format evolution (open vs expert)\")\nprint(\"  - Target difficulty selection\")\nprint(\"  - Whether AdaptyvBio continues running competitions\")\nprint()\nprint(\"Model estimate: ~30%\")\nprint(\"This accounts for ~3.5 years of rapid field development,\")\nprint(\"the possibility of expert-only competitions,\")\nprint(\"but also the large gap between current rates and the threshold.\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "SUMMARY OF ANALYSIS\n============================================================\n\nKey data points:\n  - Current best competition-wide rate: 14% (EGFR R2)\n  - Current
best individual performer: 90% (Escalante, Nipah)\n  - BindCraft on Nipah (competition): 5.7%\n  - BindCraft claimed avg across targets: ~46%\n  - Gap from 14% to 75% = 61 percentage points\n\nPaths
to YES:\n  1. Tools improve so avg participant gets >75% (requires 5x improvement)\n  2. Expert-only competition with top teams (requires format change)\n  3. Very easy target where most methods work
well\n\nKey uncertainties:\n  - Rate of tool improvement (exponential? linear? plateauing?)\n  - Competition format evolution (open vs expert)\n  - Target difficulty selection\n  - Whether AdaptyvBio
continues running competitions\n\nModel estimate: ~30%\nThis accounts for ~3.5 years of rapid field development,\nthe possibility of expert-only competitions,\nbut also the large gap between current
rates and the threshold.\n", "stderr": "", "duration_ms": 0}
```

## 💬 Response

Now let me check if there are any prediction markets on this question:

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Metaculus AdaptyvBio protein binder 75% prediction market"
}
```

### 📋 Result

```
{"query": "Metaculus AdaptyvBio protein binder 75% prediction market", "results": [{"title": "Metaculus", "url": "https://www.metaculus.com/", "snippet": "Staff Picks\n[\u2699\ufe0fLabor Automation
Tournament](/tournament/labor-hub/)\n[\ud83e\uddbeFutureEval](https://www.metaculus.com/futureeval/)\n[\ud83d\udca5Iran War](/questions/?topic=2026-iran-
war&for_main_feed=false)\n[\u2694\ufe0fMetaculus Cup](/tournament/metaculus-cup-spring-2026/)\n[\u2753Top Questions](/questions/?topic=top-50&for_main_feed=false)\n[\ud83d\uddde\ufe0fCurrent
Events](/tournament/current-events/)\n[14 comments](/questions/41939/who-will-win-the-2026-california-gubernatorial-election/#comments)\n14 forecasters\nWho will win the 2026 California", "api_data":
null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url": "https://adaptyvbio.substack.com/p/protein-design-competition-has-binder", "snippet": "Protein
Design Competition: Has binder design been solved?\nWe analyze the results of our protein design competition where 130 designers created binders for EGFR. With a 5x improvement in success rates and
some designs outperforming clinical antibodies, we exp\nThe results of our second Protein Design Competition show dramatic progress in the field. Out of 400 tested proteins, 378 expressed successfully
(95%) and 53 of these bound to their target EGFR (14% success rate). This represents a 5x impro", "api_data": null, "hint": null}, {"title": "Protein Optimization 102: Lessons from the protein design
competition", "url": "https://www.adaptyvbio.com/blog/po102/", "snippet": "In our [last ](https://www.adaptyvbio.com/blog/po101)[blog](https://www.adaptyvbio.com/blog/po101) post, we looked at the
different ways you can optimize a protein for a given task using machine learning models.\nWe made the distinction between
[fixed](https://www.adaptyvbio.com/blog/po101#:~:text=Supplementary%20-%20Fixed%20model%20optimization) and [sequential](https://www.adaptyvbio.com/blog/po101#:~:text=sequentially-optimized%20models)
model optimization and further split the latter into [mo", "api_data": null, "hint": null}, {"title": "Protein Design Competition - Adaptyv Bio", "url": "https://design.adaptyvbio.com/", "snippet":
"All-atom diffusion-based generative model developed for de novo design of protein and peptide binders across a wide array of target types\nA flexible de novo binder design workflow using RFdiffusion
for backbone generation\nProtein binder design pipeline that can be used to design miniprotein and peptide binders\nid: noble-bat-topaz\nIL-7Ra\nStrong\n1.4e-9 M\nTrue\n12.5 kDa\n119\nid: lunar-zebra-
topaz\nEGFR\nStrong\n1.9e-9 M\nTrue\n25.9 kDa\n241\nid: brisk-boar-cloud\nMDM2\nStrong\n1.7e-7 M\nTrue\n12.1 kDa\n102\nid: go", "api_data": null, "hint": null}, {"title": "What happened in the Nipah
Protein Design Competition so far? + Prediction markets for protein design", "url": "https://www.adaptyvbio.com/blog/nipah-submissions/", "snippet": "After a busy few weeks with over 680 protein
designers submitting their best binder designs against the surface glycoprotein of the Nipah virus, the submissions and community vote doors have closed and we are waiting in anticipation for the
experimental results to arrive. In the meantime, we want to highlight some interesting new insights and cool protein structures that we have gathered during the course of this competition.\nLet\u2019s
start with a quick recap: Nipah is one of the deadliest viruses ", "api_data": null, "hint": null}, {"title": "Metaculus Forecasting Platform: Complete Guide - Prediction Market Tools | Prediction
Market Tools", "url": "https://www.predictionmarket.tools/news/metaculus-forecasting-platform-guide", "snippet": "Introduction to Metaculus Forecasting Platform\nMetaculus is a community-driven
forecasting platform that has gained prominence for its accuracy and collaborative approach. This Metaculus guide will walk you through its features, usage, and benefits, helping both newcomers and
seasoned forecasters make the most of this unique platform.\nWhat is Metaculus?\nMetaculus is a collective intelligence platform focused on forecasting the likelihood of various future events. It
harnesses the power of both a", "api_data": null, "hint": null}, {"title": "Adaptyv Bio on X: \"What happened in the Nipah Protein Design Competition so far? Plus: Prediction markets for protein
design TLDR: \u2022 We hosted our third installment of the Protein Design Competition on @proteinbase, this time challenging participants to design a binder against the Nipah virus
https://t.co/6vHEeqHKic\" / X", "url": "https://x.com/adaptyvbio/status/2008247016619450474", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser. Please enable JavaScript or
switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9
2026 X Corp.", "api_data": null, "hint": null}, {"title": "Adaptyv Bio", "url": "https://www.adaptyvbio.com/blog", "snippet": "For our Nipah Binder competition, we give a short overview of the
submitted designs, examine which design methods were most widely adopted, and highlight several noteworthy and creative community contributions. Plus, we opened a prediction market on Manifold for
this competition so you can bet on hit rates, best performing models, and more\nTong Chen and colleagues from Pranam Chatterjee\u2019s Programmable Biology Group at the University of Pennsylvania are
showcasing their most recent model MOG-DFM ", "api_data": null, "hint": null}, {"title": "BenchBB - Benchmark for Computational Protein Binder Design | Adaptyv Bio", "url":
"https://start.adaptyvbio.com/benchbb", "snippet": "--\nHigh-throughput protein expression analysis for rapid characterization of protein variants and optimization.\nincludes Expression\nGet accurate
protein-protein interaction data using our BLI and SPR worklflows for binding characterization.\nincludes Expression\nCharacterize the thermostability of your protein variants and optimize their
stability.", "api_data": null, "hint": null}, {"title": "Why I Reject the Comparison of Metaculus to Prediction Markets | by Metaculus | Medium", "url": "https://metaculus.medium.com/why-i-reject-the-
comparison-of-metaculus-to-prediction-markets-4175553bcbb8", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "\"protein binder\" \"success rate\" \"75%\" competition forecast prediction"
}
```

### 📋 Result

```
{"query": "\"protein binder\" \"success rate\" \"75%\" competition forecast prediction", "results": [{"title": "Protein Optimization 102: Lessons from the protein design competition", "url":
"https://www.adaptyvbio.com/blog/po102/", "snippet": "In our [last ](https://www.adaptyvbio.com/blog/po101)[blog](https://www.adaptyvbio.com/blog/po101) post, we looked at the different ways you can
optimize a protein for a given task using machine learning models.\nWe made the distinction between
[fixed](https://www.adaptyvbio.com/blog/po101#:~:text=Supplementary%20-%20Fixed%20model%20optimization) and [sequential](https://www.adaptyvbio.com/blog/po101#:~:text=sequentially-optimized%20models)
model optimization and further split the latter into [mo", "api_data": null, "hint": null}, {"title": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein
design", "url": "https://www.adaptyvbio.com/blog/nipah-submissions/", "snippet": "After a busy few weeks with over 680 protein designers submitting their best binder designs against the surface
glycoprotein of the Nipah virus, the submissions and community vote doors have closed and we are waiting in anticipation for the experimental results to arrive. In the meantime, we want to highlight
some interesting new insights and cool protein structures that we have gathered during the course of this competition.\nLet\u2019s start with a quick recap: Nipah is one of the deadliest viruses ",
"api_data": null, "hint": null}, {"title": "Predicting Experimental Success in De Novo Binder Design: A Meta-Analysis of 3,766 Experimentally Characterised Binders | bioRxiv", "url":
"https://www.biorxiv.org/content/10.1101/2025.08.14.670059v1.full", "snippet": null, "api_data": null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url":
"https://www.adaptyvbio.com/blog/po104/", "snippet": "We released the [results of our second Protein Design Competition](https://foundry.adaptyvbio.com/competition) just about 2 weeks ago\u2026 and
they were great!\nA quick recap of what this was all about:\nAnd the designers did not disappoint. In our previous analysis [here](https://www.adaptyvbio.com/blog/po103), we went through how the meta
shifted from the first round, in particular how close the race was in the last few days as some submitters tried to increase their chances of landing in the top 10", "api_data": null, "hint": null},
{"title": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein design", "url": "https://adaptyvbio.substack.com/p/what-happened-in-the-nipah-protein",
"snippet": "What happened in the Nipah Protein Design Competition so far? + Prediction markets for protein design\nFor our Nipah Binder competition, we give a short overview of the submitted designs,
examine which design methods were most widely adopted, and highlight several noteworthy and creative community cont\n\u2022 We hosted our third installment of the Protein Design Competition, this time
challenging participants to design a binder against the Nipah virus glycoprotein.\n\u2022 The response was incredible: Over ", "api_data": null, "hint": null}, {"title": "Predicting Experimental
Success in De Novo Binder Design: A Meta-Analysis of 3,766 Experimentally Characterised Binders | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Predicting-Experimental-Success-in-
De-Novo-Binder-A-Overath-Rygaard/8f814c6523e4a469ac2555b6e0e16fdb9752f50c", "snippet": null, "api_data": null, "hint": null}, {"title": "Protein Design Competition - RESULTS - Adaptyv Bio", "url":
"https://adaptyvbio.substack.com/p/protein-design-competition-results", "snippet": "Protein Design Competition - RESULTS\nThe long awaited results are here -- and they don\u2019t disappoint!\nThe long
awaited results are here -- and they don\u2019t disappoint!\n\ud83d\udcc8 We doubled the number of proteins we tested in our lab from 200 to 400!\n\ud83e\uddec Out of those 400 proteins, 378 expressed
(95% expression rate!)\n\ud83d\ude80 Out of those 378 expressed proteins, 53 did successfully bind the target protein EGFR (that\u2019s a 14% success rate, more than 5x of the success rate of the
previous round just 2 months ago!)\n\ud83d\udcaa Th", "api_data": null, "hint": null}, {"title": "Protein Design Competition: Has binder design been solved?", "url":
"https://adaptyvbio.substack.com/p/protein-design-competition-has-binder", "snippet": "Protein Design Competition: Has binder design been solved?\nWe analyze the results of our protein design
competition where 130 designers created binders for EGFR. With a 5x improvement in success rates and some designs outperforming clinical antibodies, we exp\nThe results of our second Protein Design
Competition show dramatic progress in the field. Out of 400 tested proteins, 378 expressed successfully (95%) and 53 of these bound to their target EGFR (14% success rate). This represents a 5x
impro", "api_data": null, "hint": null}, {"title": "Protein binder design revisited - Boolean Biotech", "url": "https://blog.booleanbiotech.com/protein-binder-design-revisited", "snippet": "I have
written about protein binder design a few times now\n([the Adaptyv competition](https://blog.booleanbiotech.com/adaptyv-binder-design-competition);\n[a follow up](https://blog.booleanbiotech.com/what-
we-learned-adaptyv)).\nCorin Wagen recently wrote a\n[great piece](https://corinwagen.github.io/public/blog/20250303_achilles_and_the_tortoise.html)\nabout protein\u2013ligand binding.\nThis purpose
of this post is to review how well protein binder design is working today,\nand point out some interesting", "api_data": null, "hint": null}, {"title": "(PDF) Crowdsourced Protein Design: Lessons From
the Adaptyv EGFR Binder Competition", "url": "https://www.researchgate.net/publication/391068992_Crowdsourced_Protein_Design_Lessons_From_the_Adaptyv_EGFR_Binder_Competition", "snippet": null,
"api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me now do my reflection and finalize my forecast. I have good data. Let me synthesize my thinking.

Key considerations:

1. **Current state**: Best competition-wide rate is 14% (EGFR R2). Best individual performer achieved 90% (9/10, Escalante in Nipah). The gap is enormous.

2. **The question asks about ALL tested designs in a competition exceeding 75%**. This is a very high bar because competitions include many participants of varying skill levels.

3. **Tool improvement trajectory**: The field has improved dramatically (0.1% → 14% competition-wide in ~2 years). But BindCraft, the best open-source tool, only achieved 5.7% on the Nipah target in competition settings, despite claiming 10-100% in papers. This suggests published numbers overstate competition performance.
   
Over the 3.5+ year timeframe with potentially 6-10 more competitions ahead, I'm weighing several paths to resolution: tools becoming so dominant that even average users exceed 75%, expert-only competitions like RBX-1 where all participants are skilled, or exceptionally easy targets where most methods succeed. My simulation scenarios range from nearly 0% in conservative cases to 96% if both expert-level competition and fast improvement converge, with a weighted estimate around 31%.

But I'm second-guessing my "fast improvement" scenario—the gap between BindCraft's 46% average performance in published results versus just 5.7% in the actual Nipah competition suggests the real-world setting is substantially harder than lab conditions. That said, the field is moving remarkably quickly, and over 3.5 years the democratization of strong tools like BindCraft will likely put more participants in a position to perform well. I'm settling on around 25-30% as my estimate, leaning toward 25%.

Actually, stepping back: the core issue is that top individual performers already hit 75%+ (Escalante at 90%, 9/10), but the question asks about the overall competition rate. For that to exceed 75%, the average participant needs to be near that threshold too—and that's a fundamentally different challenge than having a few standouts.

The real question becomes whether we'll see a competition where the skill floor is high enough to push the weighted average above 75%. There are two plausible paths: either tool commoditization makes everyone capable (BindCraft is already open-source, but the Nipah results show the tool alone isn't sufficient—expertise in deployment matters), or we get an expert-only format like RBX-1 where only experienced teams participate. Even in that workshop setting with 300 designs across teams at ICLR, hitting 75% overall is an extremely high bar. I'm sticking with 25%, which captures genuine optimism about tool improvement while acknowledging how difficult that threshold really is.

Actually, let me reconsider the RBX-1 scenario more carefully. Results come April 26, 2026—just 12 days away. If this is truly an expert-only workshop with only experienced teams, could they hit 75%? Probably not in this round, since even skilled teams using current tools would struggle to all exceed that threshold. But it could establish a precedent for future expert competitions. I'm going with 25%.

Now I'm thinking through the expert competition scenario more carefully. At ICLR with top researchers using advanced tools, I'd expect the best teams to reach 70-90%, average teams around 30-50%, and weaker ones 10-20%—putting the weighted average somewhere in the 40-50% range, still short of 75%. But by 2028-2029, if the best expert teams hit 90-95% and average expert teams achieve 60-75%, the overall average could reach 60-75% depending on whether the competition stays small and selective or includes only the strongest performers. Getting to 75% overall would require either all expert teams performing at very high levels or limiting participation to just the top few teams with a favorable target. I'd estimate the probability of this happening in at least one competition by 2030 at around 20-30%.

I'm settling on 25% as my estimate. But there's another angle I should factor in—the screening process itself. Competitions already pre-screen designs computationally before experimental testing, like how Nipah selects 1,030 designs from over 10,000 submissions. If screening methods improve significantly through better in-silico prediction tools, competitions could test only the most promising designs, which would effectively boost the success rate of tested designs. This is actually a plausible path to hitting 75% that I hadn't fully weighted, though the tradeoff is that fewer total designs get tested if screening becomes too stringent.

My model suggests around 31% with specific scenario weights, but I'm adjusting down to 25% because some of my assumptions feel optimistic, particularly around how quickly improvement happens in the faster scenarios.

## 💬 Response

Now let me reflect on my analysis and produce a final estimate.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Rapid tool improvement trajectory: From <0.1% (Rosetta) to 14% competition-wide (EGFR R2) in ~2 years, and individual performers already achieving 90% (Escalante, 9/10 in Nipah). The field is in an exponential improvement phase.",
      "logit": 1.5,
      "confidence": 0.8
    },
    {
      "description": "Open-source tool democratization: BindCraft (10-100%), Mosaic, and future tools make high-quality design accessible. As tools commoditize, the skill floor rises, narrowing the gap between best and average participants.",
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Expert-only competition format exists: RBX-1 (GEM \u00d7 Adaptyv, ICLR workshop) tests only 300 designs from expert teams. Future small expert competitions could have much higher overall rates than open competitions.",
      "logit": 0.8,
      "confidence": 0.65
    },
    {
      "description": "Long time horizon: 3.5 years with potentially 6-10+ competitions. Even if per-competition probability is modest, cumulative probability benefits from multiple chances.",
      "logit": 0.7,
      "confidence": 0.75
    },
    {
      "description": "Enormous gap between current competition-wide rate (14%) and threshold (75%): Requires ~5x improvement in overall rates. Gap between published tool performance and competition performance is concerning (BindCraft: 46% avg in paper vs 5.7% on Nipah in competition).",
      "logit": -1.5,
      "confidence": 0.85
    },
    {
      "description": "Target difficulty creates hard ceiling: Some targets yield 0% even for best tools (AlphaProteo on TNF\u03b1). Nipah was harder than EGFR, pushing overall rates down from 14% to 9.6% despite better tools. Target selection is unpredictable.",
      "logit": -1,
      "confidence": 0.75
    },
    {
      "description": "Competition diversity drags average down: Open competitions attract many novices, students, and experimenters using suboptimal methods. Even with good tools, improper usage leads to low individual rates.",
      "logit": -0.8,
      "confidence": 0.7
    },
    {
      "description": "Status quo and operational risks: AdaptyvBio might stop running competitions, pivot business model, or face funding issues. 10% probability of no more qualifying competitions before 2030.",
      "logit": -0.5,
      "confidence": 0.5
    }
  ],
  "tentative_estimate": {
    "logit": -1.1,
    "probability": 0.25
  },
  "anchor": "No direct base rate for 'protein design competition exceeding threshold' questions. Using structural reasoning: current best competition-wide rate is 14%, threshold is 75%. In rapidly improving fields, the probability of a 5x improvement in 3.5 years with multiple attempts is meaningful but not dominant. Anchor: ~20% based on the combination of rapid improvement pace and high threshold.",
  "assessment": "The question asks whether ANY AdaptyvBio protein-binder competition before 2030 will have >75% of ALL tested designs classified as binders. This is a high bar because it requires the OVERALL competition average (not just the best performer) to exceed 75%.\n\n**Current state**: Competition-wide rates range from 2.5% to 14%. Individual top performers already achieve 80-90%. The gap between best and average is enormous (~76 percentage points in Nipah).\n\n**Path to YES requires one of**:\n1. Tool commoditization where average users achieve 75%+ (currently average tools get 5-15%)\n2. Expert-only competition format (RBX-1 is a precedent, but even expert teams average well below 75% today)\n3. Very easy target + good tools + skilled participants\n4. Improved in-silico screening that pre-filters to only highly likely binders\n\n**Key tension**: The gap between published tool performance (BindCraft avg 46%) and competition performance (BindCraft 5.7% on Nipah) suggests that target difficulty and user expertise are major factors beyond raw tool capability. Even if tools improve further, competition settings may not reach published benchmarks.\n\n**Monte Carlo analysis**: My simulation across scenarios gives a weighted cumulative probability of ~31%, with strong dependence on scenario weights. Conservative scenarios (slow improvement) give ~0-5%, while optimistic scenarios (fast tool improvement + expert format) give 70-95%.\n\n**Counterargument**: A smart disagreer would note that the improvement trajectory is genuinely exponential, that individual performers ALREADY exceed the threshold, and that 3.5 years in this field is an eternity. They'd point to BindCraft going from concept to widely-used open-source tool in <2 years, and argue that by 2028-2029, the default tools will be dramatically better. They'd also note that in-silico filtering will improve alongside design tools, making it easier to select likely binders before testing.\n\n**My response**: While individual tool improvement is remarkable, the question asks about competition-wide rates. The diversity of participants and target difficulty create structural barriers. Even if the best tools achieve 95%+ by 2029, the variance in participant quality and target selection makes 75% overall unlikely in any single competition. But with 6-10+ tries, it's not negligible.\n\nI settle on 25%, slightly below my model's 31%, because I think my model's improvement rate assumptions in the optimistic scenarios are somewhat too aggressive given the BindCraft competition performance gap.",
  "calibration_notes": "Anchor: ~20% (structural reasoning about field improvement rate vs high threshold). Departure to 25% justified by: the existence of expert-only competition format (RBX-1 precedent), the long time horizon giving multiple chances, and the genuinely exponential pace of tool improvement. Not departing further because: 75% is an extremely high bar for competition-wide rates, current best is 14%, and target difficulty creates unpredictable variance.",
  "key_uncertainties": "1. Rate of computational protein design tool improvement (the dominant factor)\n2. Whether AdaptyvBio will run more expert-only competitions (vs open competitions)\n3. Whether in-silico screening will improve enough to pre-filter tested designs effectively\n4. Whether AdaptyvBio continues running competitions through 2029\n5. Target difficulty selection for future competitions",
  "update_triggers": "1. RBX-1 results (April 26, 2026) showing >30% overall rate would be very bullish\n2. Publication of new tools achieving >80% average across diverse targets\n3. AdaptyvBio announcing a competition format change (smaller, expert-only)\n4. A tool achieving >50% in an open competition would be very significant\n5. AdaptyvBio stopping competitions would push toward NO",
  "tool_audit": "research() provided excellent comprehensive data on AdaptyvBio competition history and tool performance benchmarks. web_search found current RBX-1 competition details. fetch_url extracted key details from Escalante blog and GEM workshop page. execute_code ran Monte Carlo simulations to model improvement trajectories. No tool failures. Missing capability: no prediction market data found for this specific question.",
  "process_reflection": "The research sub-agent was very effective at gathering comprehensive competition data. The Monte Carlo simulation was useful for organizing scenario thinking, though the results are highly sensitive to assumed improvement rates. The scenario-weighting approach (conservative/base/fast/expert) provided good structure for handling deep uncertainty. The main friction was in calibrating improvement rate assumptions - there's no good empirical basis for projecting protein design tool improvement rates forward, so the simulation provides structure but not precision. A specialized biotech forecasting tool with curated improvement trajectories would have helped."
}
```

### 📋 Result

```
{"factor_count": 8, "factor_sum": 0.11000000000000021, "tentative_logit": -1.1, "logit_gap": -1.2100000000000004, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Rapid tool
improvement trajectory: From <0.1% (Rosetta) to 14% competition-wide (EGFR R2) in ~2 years, and individual performers already achieving 90% (Escalante, 9/10 in Nipah). The field is in an exponential
improvement phase.", "logit": 1.5, "confidence": 0.8, "effective_logit": 1.2000000000000002}, {"description": "Open-source tool democratization: BindCraft (10-100%), Mosaic, and future tools make
high-quality design accessible. As tools commoditize, the skill floor rises, narrowing the gap between best and average participants.", "logit": 1.0, "confidence": 0.7, "effective_logit": 0.7},
{"description": "Expert-only competition format exists: RBX-1 (GEM \u00d7 Adaptyv, ICLR workshop) tests only 300 designs from expert teams. Future small expert competitions could have much higher
overall rates than open competitions.", "logit": 0.8, "confidence": 0.65, "effective_logit": 0.52}, {"description": "Long time horizon: 3.5 years with potentially 6-10+ competitions. Even if per-
competition probability is modest, cumulative probability benefits from multiple chances.", "logit": 0.7, "confidence": 0.75, "effective_logit": 0.5249999999999999}, {"description": "Enormous gap
between current competition-wide rate (14%) and threshold (75%): Requires ~5x improvement in overall rates. Gap between published tool performance and competition performance is concerning (BindCraft:
46% avg in paper vs 5.7% on Nipah in competition).", "logit": -1.5, "confidence": 0.85, "effective_logit": -1.275}, {"description": "Target difficulty creates hard ceiling: Some targets yield 0% even
for best tools (AlphaProteo on TNF\u03b1). Nipah was harder than EGFR, pushing overall rates down from 14% to 9.6% despite better tools. Target selection is unpredictable.", "logit": -1.0,
"confidence": 0.75, "effective_logit": -0.75}, {"description": "Competition diversity drags average down: Open competitions attract many novices, students, and experimenters using suboptimal methods.
Even with good tools, improper usage leads to low individual rates.", "logit": -0.8, "confidence": 0.7, "effective_logit": -0.5599999999999999}, {"description": "Status quo and operational risks:
AdaptyvBio might stop running competitions, pivot business model, or face funding issues. 10% probability of no more qualifying competitions before 2030.", "logit": -0.5, "confidence": 0.5,
"effective_logit": -0.25}], "dominant_factor": "Enormous gap between current competition-wide rate (14%) and threshold (75%): Requires ~5x improvement in overall rates. Gap between published tool
performance and competition performance is concerning (BindCraft: 46% avg in paper vs 5.7% on Nipah in competition).", "dominant_effective_logit": -1.275, "factor_implied_probability":
0.5274723043445938, "tentative_probability": 0.25, "gap_pp": -27.74723043445938, "sources": ["[(Metaculus) Will an AdaptyvBio protein-binder competition have >75% of tested designs be classified as
binders before 2030?](https://www.metaculus.com/questions/42911)", "[Minibinder design is just not that hard](https://blog.escalante.bio/minibinder-design-is-just-not-that-hard/)", "[Competition-2026
\u2014 GEM Workshop](https://www.gembio.ai/gemadaptyv2026)"], "reviewer_critique": "## Verification Summary\n\n**Resolution criteria**: Recovered correctly. The agent fetched the full Metaculus
question (lines 16-38 of trace), including resolution criteria (\"resolve as Yes if...>75% of the computationally generated designs selected for experimental testing are classified as binders\") and
fine print (\"competition must only test novel designs\"). The agent correctly interprets this as requiring the OVERALL competition rate to exceed 75%, not just the best individual
performer.\n\n**Factual claims verified against trace**:\n\n1. **Factor 1** (rapid improvement trajectory): Rosetta <0.1% \u2192 EGFR R2 14% \u2192 Escalante 90% (9/10 in Nipah). All confirmed by
research results in trace (lines 66-89). Escalante Mosaic achieved 88.8% (n=9), Nick Boyd achieved 9/10 = 90% de novo. \u2713\n\n2. **Factor 2** (BindCraft 10-100%): Confirmed by Nature paper search
results and research cache. \u2713\n\n3. **Factor 3** (RBX-1 tests 300 designs): Confirmed by fetch of gembio.ai/gemadaptyv2026 (lines 288-301). The \"expert teams\" characterization is slightly
imprecise \u2014 it's an ICLR workshop competition open to any team, but the format naturally selects for more experienced participants. Minor imprecision, not hallucination. \u2713\n\n4. **Factor 5**
(BindCraft 46% avg in paper vs 5.7% in competition): Both figures confirmed \u2014 Nature paper states 10-100% (avg ~46%), Deniz Kavi's analysis shows 5.68% (n=88) on Nipah. \u2713\n\n5. **Factor 6**
(AlphaProteo 0% on TNF\u03b1): Confirmed in research results (line 82). \u2713\n\n**Double-counting**: Factors 1 and 2 both draw on tool improvement but from distinct angles (trajectory vs.
accessibility). Factors 5 and 7 both explain why 75% is hard but through different mechanisms (raw gap vs. participant diversity). Mild overlap exists but each factor contributes a distinct analytical
dimension. Not problematic.\n\n**Wrong-direction factors**: All factor signs are correct. Positive factors support YES, negative factors support NO. \u2713\n\n**Contradictory assessment**: No. The net
logit sum is +0.2. From the 20% anchor (logit \u2248 -1.39), adding +0.2 gives ~23%, consistent with the 25% estimate. The narrative assessment aligns with the factors. \u2713\n\n**Adversarial
reasoning**: Present. The assessment explicitly addresses what \"a smart disagreer would say\" \u2014 exponential improvement, individual performers already exceeding threshold, tool commoditization
\u2014 and responds substantively, noting the competition-wide vs. individual distinction. \u2713\n\n**Anchor divergence**: Only 5pp from the 20% anchor. Fully justified by the modest net positive
factors. \u2713\n\n**Probability assessment**: I independently estimate 20-30% based on: (a) the enormous 14% \u2192 75% gap, (b) the BindCraft paper-to-competition performance collapse (46% \u2192
5.7%), (c) 3.5 years of rapid improvement with multiple competition opportunities, (d) expert-only competition precedent (RBX-1). The agent's 25% falls squarely in my range. The Monte Carlo analysis,
while necessarily assumption-dependent, provides useful structure and the agent appropriately discounted it from 31% to 25% based on concerns about optimistic improvement rates.\n\n**Worldview
consistency**: No conflicting forecasts found (no worldview/forecasts directory exists). The worldview research entries are consistent with the factors \u2014 they provide the same data the agent
uses.\n\nNo errors found that would change the forecast direction or magnitude."}
```

## 💬 Response

The reflection reviewer approved. Let me now output my final forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "The question asks whether ANY AdaptyvBio protein-binder competition before 2030 will have >75% of ALL tested designs classified as binders. Currently, the best competition-wide rate is 14% (EGFR R2), while individual top performers already achieve 80-90% (Escalante: 9/10 in Nipah). The gap between these is the key challenge: 75% applies to ALL tested designs, not just the best performer.\n\nThe field is improving rapidly (from <0.1% Rosetta-era to 14% competition-wide in ~2 years), and open-source tools like BindCraft and Mosaic are democratizing access. However, BindCraft's competition performance (5.7% on Nipah) is far below its published average (~46%), indicating target difficulty and user expertise are major factors.\n\nWith ~3.5 years and potentially 6-10+ competitions remaining, there are multiple paths to YES: tool commoditization raising the skill floor, expert-only competition formats (precedent: RBX-1 workshop), improved in-silico screening, or favorable target selection. Monte Carlo simulations across scenarios give 0-96% per scenario, with a weighted cumulative of ~31%. I adjust slightly downward to 25% due to concerns about optimistic tool improvement assumptions, particularly the large gap between published and competition performance of current tools.",
  "anchor": "~20% based on structural reasoning: current best competition-wide rate is 14%, threshold is 75%, requiring ~5x improvement in a rapidly advancing field over 3.5 years with multiple attempts. No direct historical base rate available for this type of question.",
  "factors": [
    {
      "description": "Rapid tool improvement trajectory: From <0.1% (Rosetta) to 14% competition-wide (EGFR R2) in ~2 years, and individual performers already achieving 90% (Escalante, 9/10 in Nipah). The field is in an exponential improvement phase.",
      "logit": 1.5,
      "confidence": 0.8
    },
    {
      "description": "Open-source tool democratization: BindCraft (10-100%), Mosaic, and future tools make high-quality design accessible. As tools commoditize, the skill floor rises, narrowing the gap between best and average participants.",
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Expert-only competition format exists: RBX-1 (GEM \u00d7 Adaptyv, ICLR workshop) tests only 300 designs from expert teams. Future small expert competitions could have much higher overall rates than open competitions.",
      "logit": 0.8,
      "confidence": 0.65
    },
    {
      "description": "Long time horizon: 3.5 years with potentially 6-10+ competitions. Even if per-competition probability is modest, cumulative probability benefits from multiple chances.",
      "logit": 0.7,
      "confidence": 0.75
    },
    {
      "description": "Enormous gap between current competition-wide rate (14%) and threshold (75%): Requires ~5x improvement in overall rates. Gap between published tool performance and competition performance is concerning (BindCraft: 46% avg in paper vs 5.7% on Nipah in competition).",
      "logit": -1.5,
      "confidence": 0.85
    },
    {
      "description": "Target difficulty creates hard ceiling: Some targets yield 0% even for best tools (AlphaProteo on TNF\u03b1). Nipah was harder than EGFR, pushing overall rates down from 14% to 9.6% despite better tools. Target selection is unpredictable.",
      "logit": -1,
      "confidence": 0.75
    },
    {
      "description": "Competition diversity drags average down: Open competitions attract many novices, students, and experimenters using suboptimal methods. Even with good tools, improper usage leads to low individual rates.",
      "logit": -0.8,
      "confidence": 0.7
    },
    {
      "description": "Status quo and operational risks: AdaptyvBio might stop running competitions, pivot business model, or face funding issues. ~10% probability of no more qualifying competitions before 2030.",
      "logit": -0.5,
      "confidence": 0.5
    }
  ],
  "logit": -1.1,
  "probability": 0.25
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**My forecast: 25% probability**

**Key reasoning:**

- **Current state**: The best competition-wide binder success rate is 14% (EGFR Round 2). The threshold of 75% requires a ~5x improvement in *overall* competition rates, not just individual performance.

- **Individual performers already exceed 75%**: Escalante achieved 9/10 (90%) in Nipah. But the *competition-wide* rate was only 9.6% because most participants scored much lower.

- **Rapid field improvement**: The field has gone from <0.1% (Rosetta era) to 14% competition-wide in ~2 years. Open-source tools like BindCraft and Mosaic are democratizing access. This exponential trajectory is the strongest argument for YES.

- **Key challenge - paper vs. competition gap**: BindCraft claims 10-100% success in published work, but only achieved 5.7% in the Nipah competition. This suggests target difficulty and user expertise create structural barriers even with good tools.

- **Paths to YES**: (1) Tool commoditization raising the skill floor, (2) expert-only competition formats (RBX-1 precedent), (3) improved in-silico pre-screening, (4) favorable target selection. With 3.5 years and 6-10+ competitions, multiple chances increase cumulative probability.

- **Paths to NO**: Tools plateau or improve linearly rather than exponentially, hard targets keep competition rates below 30%, open competition format persists with many novice participants dragging averages down, or AdaptyvBio stops running competitions.
