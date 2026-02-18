# Meta-Reflection: French Municipal Elections 2026 Abstention Rate

## Executive Summary
- **Post ID**: 42101 (synced with original 42035)
- **Question ID**: 41865
- **Final forecast**: Median ~42%, 80% CI [38.5%, 45.6%]
- **Confidence**: Moderate

This is a measurement question about French municipal election abstention. I approached it by: (1) compiling the full historical time series of municipal election abstention rates, (2) fitting trend models to the pre-COVID data, (3) incorporating polling data and expert views on 2026 mobilization, (4) building a scenario-based Monte Carlo simulation, and (5) cross-checking against other recent French election results.

## Evidence Assessment

**Strongest evidence FOR my forecast (median ~42%):**
1. The pre-COVID trend line extrapolates to ~38-42% for 2026, and political context (post-2024 dissolution, general disaffection) suggests landing at the upper end or slightly above.
2. Multiple recent French elections show elevated abstention compared to pre-2020 levels, even when COVID is not a factor (2022 legislative: 52.5%, 2024 European: 48.5%). Only the exceptional 2024 snap legislative with RN threat achieved low abstention (33.3%).
3. Polling shows 60% "certain" to vote (IFOP Nov 2025) and 69% interested (OpinionWay Jan 2026), suggesting participation will be significantly better than 2020 but not necessarily at 2014 levels.

**Strongest argument AGAINST:**
- A smart disagreer might argue that municipal elections are special in France — they have the strongest local attachment, the most personal campaigns, and historically much higher turnout than other local/European elections. The competitive high-profile races (Paris, Marseille, Lyon, Bordeaux) combined with new voting rules could drive turnout closer to 2014 levels (~36-38%). The 69% campaign interest figure is promising, and the return of seniors who skipped 2020 due to COVID is a genuine factor.
- What would change my mind: If polling data from late February/early March showed >65% certain to vote, or if the campaign intensified dramatically with high national attention, I'd shift my median down to ~39%.

## Calibration Check
- **Question type**: Measurement (future value of a known metric)
- **Framework**: Historical trend extrapolation + scenario analysis + polling cross-check
- **Am I hedging?** Somewhat — the 40/35 split between "pre-COVID reversion" and "moderate disaffection" scenarios reflects genuine uncertainty. I could make a stronger directional call toward ~40% (pre-COVID reversion) if I weighted polling data more heavily, but I think the structural disaffection factor deserves significant weight.
- **Are my intervals data-driven?** Yes — the Monte Carlo simulation produces them directly from scenario parameters grounded in historical data.

## Tool Audit
- **get_metaculus_questions**: Useful, provided full question details.
- **search_exa**: Very useful, found multiple French-language articles with historical data and expert commentary.
- **WebFetch**: Mixed — many French news sites blocked. Got good data from france-politique.fr.
- **wikipedia**: Limited — French Wikipedia article on electoral abstention not accessible by title; English Wikipedia article too brief.
- **Prediction markets**: No relevant markets found on Polymarket or Manifold for this specific question.
- **CP history**: Returned 0 data points — no community prediction available for calibration.
- **Capability gap**: Would have benefited from accessing the IFOP/OpinionWay full survey PDFs with detailed participation intention breakdowns.

## Update Triggers
- Late-February polling with specific participation intention numbers
- Major political events in France before March 15 (government crisis, protest movements, etc.)
- Weather forecast for March 15 (significant snow/rain reduces turnout)
- Overseas territory developments that could affect their turnout

**80% CI for my probability estimate**: My median could reasonably be anywhere from 39% to 44%. The 80% interval [38.5%, 45.6%] I'm relatively confident in.
---

## Programmatic Metrics

*Auto-generated - do not edit manually*

- **Post ID**: 42101
- **Question ID**: 41865
- **Session Duration**: 431.2s (7.2 min)
- **Cost**: $5.1108
- **Tokens**: 18,705 total (56 in, 18,649 out)
  - Cache: 1,426,147 read, 80,048 created
- **Log File**: `logs/42101_20260217_154024/20260217-154024.log`

### Tool Calls

- **Total**: 24 calls
- **Errors**: 2 (8.3%)

| Tool | Calls | Errors | Avg Time |
|------|-------|--------|----------|
| execute_code | 4 | 0 | 240ms |
| get_cp_history | 1 | 0 | 6533ms |
| get_metaculus_questions | 2 | 0 | 1580ms |
| get_prediction_history | 1 | 0 | 0ms |
| install_package | 1 | 0 | 3110ms |
| manifold_price | 1 | 0 | 155ms |
| notes | 3 | 0 | 1ms |
| polymarket_price | 1 | 0 | 95ms |
| search_exa | 5 | 0 | 1292ms |
| search_news | 1 | 1 ⚠️ | 964ms |
| wikipedia | 4 | 1 ⚠️ | 233ms |

### Sources Consulted

- https://www.dna.fr/elections/2026/01/24/malgre-la-popularite-des-maires-pourq...
- https://www.24matins.fr/municipales-2026-abstention-parite-et-desinformation-...
- https://elabe.fr/municipales2026/
- https://actu.fr/politique/elections-municipales/municipales-2026-abstention-p...
- https://fr.wikipedia.org/wiki/Abstention_de_vote_en_France
- https://lvsl.fr/labstention-aux-elections-municipales-phenomene-accidentel-te...
- https://www.ifop.com/en/article/how-the-french-feel-about-the-2026-municipal-...
- https://www.opinion-way.com/fr/publications/barometre-municipales-2026-vague-...
- https://ladepeche.fr/2026/02/09/entretien-municipales-2026-faut-il-sattendre-...
- https://www.linternaute.com/actualite/politique/7982831-elections-municipales...
- https://www.france-politique.fr/participation-abstention.htm