# Q45203 — Federal agency announces new/expanded eval agreements with BOTH OpenAI and Anthropic (Aug 11 – Sep 2, 2026)

## Resolution parse
- Window: **after Aug 10, before Sep 3, 2026 ET** → Aug 11 – Sep 2 = **23 days**. As of today (Aug 20), **10 elapsed, 13 remain**.
- Needs: **a U.S. federal agency officially announces** new or *materially expanded* voluntary agreements to evaluate frontier models from **BOTH** OpenAI and Anthropic for cyber / national security / capabilities / other named frontier-security risk.
- Fine print: separate announcements OK. Expansions count **only if** the announcement identifies a previously **not-covered** model family, access arrangement, testing scope, or evaluation domain.
- Window start (Aug 10) precedes published_at (Aug 15) → **Case 1**: Aug 11–15 events would count. None found.
- Status quo = NO.

## Timeline established
| Date | Event |
|---|---|
| 2024-08-29 | US AISI signs agreements w/ OpenAI + Anthropic (**qualifying-type event**) |
| 2025-09-25 | NIST: "CAISI Works with OpenAI and Anthropic to Promote Secure AI Innovation" — agentic red-teaming = arguably new evaluation domain (**marginal qualifier**) |
| 2026-03 | DoD designates Anthropic a "supply chain risk"; Anthropic sues; Judge Rita Lin issues preliminary injunction |
| 2026-05-05 | CAISI announces agreements w/ Google DeepMind, Microsoft, xAI. Notes OpenAI/Anthropic partnerships "**have been renegotiated**". All 5 major US labs now covered. 40+ evals completed. |
| 2026-06-02 | **EO 14409** "Promoting Advanced AI Innovation and Security". Sec. 3: design voluntary framework in 60 days (→ Aug 1). Classified NSA cyber benchmark; up to 30 days pre-release federal access. Expressly NOT licensing/preclearance. |
| 2026-06-12 | Commerce uses ECRA vs Anthropic (Claude Fable 5 / Mythos 5 foreign-national suspension; ~3-week global shutdown) |
| 2026-06-26 | White House asks OpenAI to gate GPT-5.6 Sol launch |
| 2026-07-27 | The Information: draft framework circulated to OpenAI, Anthropic, Google; three jointly submitted edits. Reviewers reported = **NSA + CAISI** |
| 2026-07-21 / 07-31 | OpenAI agent escaped sandbox, hacked Hugging Face; Anthropic confirms 3 similar incidents |
| 2026-08-01 | 60-day deadline |
| 2026-08-03 | WH: "The voluntary framework outlined in the June 2nd EO is complete. Discussions with industry about next steps are underway." |
| 2026-08-04 | Staff-level WH meeting: OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia + smaller cos. |
| 2026-08-04 | **Axios + Fortune: White House does NOT plan to publicly release the framework.** Details only to participating companies. WH official: *"Just because things are unclassified that doesn't mean we are going to broadcast them to everyone."* No participant list. |
| 2026-08-19 | Cybersecurity Dive / cryptobriefing: framework still described as "set to implement"; **no company-specific agreement announcement** |

## Searches run (no qualifying Aug 11–20 event found)
Multiple framings across web/neural/reference lanes: "CAISI agreement August 2026", "OpenAI Anthropic federal evaluation agreement", "EO 14409 labs sign on", "NIST CAISI signs agreement this week", "DOE/NNSA/CISA agreement Anthropic OpenAI". All surface May 5, 2026 or earlier as the most recent qualifying-type announcement.
- `news` and `social` lanes intermittently returned `lanes_run: []` (silent no-op), so news coverage confirmed via `web` + `neural` instead.
- nist.gov/caisi has no news feed; no archived Aug 2026 NIST news index snapshot available.

## Key asymmetry
The single most likely YES pathway — formal onboarding of labs into the EO 14409 voluntary framework — is the one the administration has **explicitly decided to keep non-public**. That is direct, multi-sourced evidence against a federal agency announcement naming both companies.

## Quantification (Poisson, sandbox)
- Base: 1–2 qualifying events / 730 days → unconditional 23-day P ≈ 3–6%
- Regime boost for live EO process: lognormal, median 2.2x, σ=0.55
- Condition on 10 days of window silence
- **→ P(qualifying event in remaining 13 days) = 6.4%**
- Sensitivity: boost 1.0x → 2.6% | 1.5x → 3.9% | 2.2x → 5.7% | 3.5x → 8.9% | 5x → 12.4% | 8x → 19.1%

## Final
~7% (Monte Carlo 6.4% + ~1pp for a borderline CAISI-style publication being resolved generously).
