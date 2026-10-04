# Human Verification Results (to complete after adjudication)

Fill this in from the returned blinded sheet (`human_adjudication_blinded_<initials>.xlsx`)
joined to `data/screened/human_adjudication_worklist.csv` on `rec_id`, following the
pre-specified rules in `human_verification_plan.md` §10. One row per stratum.

| Stratum | N (frame) | n (sampled) | n human-reviewed (disputed / spot-check / unrated) | Human agrees with machine T/A (of reviewed) | Reconstructed % agreement (ê-adjusted point; lower bound at CP upper limit) | Action |
|---|---|---|---|---|---|---|
| A — Included, full text | 261 | 91 | 39 (35 / 4 / 0) | | | |
| B — Included, abstract only | 240 | 88 | 25 (19 / 6 / 0) | | | |
| C — Full-text exclusions | 48 | 48 | 36 (32 / 3 / 1) | | | descriptive only (§10.5); no re-screen trigger |
| D — Stage-2 exclusions | 698 | 116 | 14 (1 / 13 / 0) | | | |
| E — Stage-1 exclusions | 433 | 106 | 12 (1 / 10 / 1) | | | |
| **Overall** | 1,680 | 449 | 126 (88 / 36 / 2) | | | |

Agreement is with the primary screen's **title/abstract** decision (`machine_ta`). For
stratum C this refers to the title/abstract pass, not to the full-text exclusion.
Unreviewed concordant records per stratum: 52 / 63 / 12 / 102 / 94 (total 323).

**Pooled spot-check error rate** (36 concordant records: 13 PASS-concordant in A/B/C,
23 EXCLUDE-concordant in D/E): ___ / 36 disagreements (PASS side ___ / 13; EXCLUDE side
___ / 23); ê = ___ (two-sided 95% Clopper–Pearson CI ___ – ___). ê is used in the point
estimate and the CP upper limit in the lower bound (plan §10.5). Pooled across direction;
the method used to select the 36 is not recorded, so the bound assumes random selection.

**Cohen's κ (disagreement-enriched; not a population estimate):** human vs primary screen
κ = ___ (n = 126); human vs AI second rater κ = ___ (n = 124; R0552 and R0859 unrated by
the second rater).

**Decision thresholds (sampling plan §7, applied to the reconstructed ê-adjusted point
estimates for strata A, B, D, E; descriptive only for C):** agreement >= 0.90 -> accept;
0.80-0.90 -> accept with reported sensitivity bound; < 0.80 or any human INCLUDE/MAYBE on a
stratum D or E record -> full re-screen of that stratum (MAYBE deliberately counts as a
trigger; plan §10.5).

**Title/abstract false exclusions found (strata D/E), if any:** list rec_id, title, and stratum.
Any such finding triggers escalation per §7.

**Resulting funnel changes (if any stratum re-screened):** individual human decisions do not
alter the 501; record the count deltas only from a §7 re-screen and update
`prisma_counts_final.json`, the PRISMA figures, and the manuscript body accordingly.

**Reviewer:** background line ___ ; consent to naming ___ ; consent to publishing sheet with notes ___ .
