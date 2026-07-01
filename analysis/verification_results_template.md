# Human Verification Results (to complete after adjudication)

Fill this in from the completed `human_verification_worklist.csv`. One row per stratum.

| Stratum | N (frame) | n (sampled) | % agreement | Cohen's kappa (95% CI) | Disagreements (machine INCLUDE / machine EXCLUDE) | Action |
|---|---|---|---|---|---|---|
| A — Included, full text | 261 | 91 | | | | |
| B — Included, abstract only | 240 | 88 | | | | |
| C — Full-text exclusions | 48 | 48 | | | | |
| D — Stage-2 exclusions | 698 | 116 | | | | |
| E — Stage-1 exclusions | 433 | 106 | | | | |
| **Overall** | 1,680 | 449 | | | | |

**Decision thresholds (from the sampling plan §7):** agreement >= 0.90 -> accept; 0.80-0.90 -> accept with reported sensitivity bound; < 0.80 or any confirmed missed-eligible in C/D/E -> full re-screen of that stratum.

**Confirmed missed-eligible studies (if any):** list rec_id, title, and the stratum they were drawn from. Any such finding triggers escalation per §7.

**Resulting funnel changes (if any stratum re-screened):** record the count deltas and update `prisma_counts_final.json`, the PRISMA figures, and the manuscript body accordingly.
