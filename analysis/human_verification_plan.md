# Human Verification Sampling Plan for Machine-Assisted Screening

**Study:** Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis
**Prepared:** 1 July 2026
**Purpose:** Provide a statistically defensible plan for a credentialed human second reviewer to verify a stratified sample of the LLM-assisted screening decisions, so that the review's screening reliability can be reported quantitatively rather than asserted.

---

## 1. Background and rationale

Title/abstract screening (two stages) and full-text eligibility assessment were performed with the assistance of a large language model applying a fixed a priori rubric, with every decision logged with a reason code and justification (Supplementary File S1). No independent human reviewer adjudicated the decisions during the primary review, and 277 of the 549 full-text eligibility decisions rested on abstracts rather than retrieved full text. PRISMA 2020 and journal expectations (IJMI) favour dual review; where full dual review is infeasible, a **validated sample** with reported agreement is the accepted mitigation. This plan specifies that sample.

## 2. Objective and estimand

Estimate, per decision stratum, the **agreement rate** between the machine screening decision and an independent human reviewer applying the same rubric, and the associated **chance-corrected agreement** (Cohen's kappa) on the binary include/exclude call. Agreement rates and their confidence intervals determine whether the machine-driven funnel is reliable as reported or requires a full re-screen of one or more strata.

## 3. Sampling frame and strata

The frame is all 1,680 deduplicated records. Decisions are partitioned into five mutually exclusive, exhaustive strata reflecting where each record exited the funnel and on what evidence basis. Strata are verified separately because their error profiles and stakes differ: false exclusions (missed eligible studies) are the highest-risk error, and abstract-only inclusions are the least-evidenced decisions.

| Stratum | Definition | N | Sampled | Basis for n |
|---|---|---|---|---|
| A — Included, full text | Included; eligibility assessed on retrieved full text | 261 | 91 | precision sample |
| B — Included, abstract only | Included; eligibility assessed on abstract only | 240 | 88 | precision sample (highest-priority inclusions) |
| C — Full-text exclusions | Sought at full text, then excluded | 48 | 48 | **census** (small, high-stakes) |
| D — Stage-2 exclusions | Excluded at T/A Stage 2 (scope refinement) | 698 | 116 | precision sample |
| E — Stage-1 exclusions | Excluded at T/A Stage 1 (off-topic/window/type) | 433 | 106 | precision sample |
| **Total** | | **1,680** | **449** | |

## 4. Sample-size justification

Within each stratum the sample size targets a **95% confidence interval of half-width ~0.05** on the agreement proportion, using the conservative planning value p = 0.90 (expected high agreement, which maximises required n near p = 0.9 while remaining realistic):

- Uncorrected: n0 = 1.96^2 x 0.9 x 0.1 / 0.05^2 = 138.
- Finite-population correction n = n0 / (1 + (n0-1)/N) is applied per stratum, giving 91, 88, 116, and 106 for A, B, D, E respectively.
- Stratum C (48 records) is verified as a **complete census** because it is small and false full-text exclusions are the costliest error.

The realized total is 449 records (27% of the frame). If observed agreement in a stratum is >= 0.95, the CI half-width tightens to ~0.035; if agreement falls below ~0.85, that stratum is escalated to a full re-screen (Section 7).

## 5. Sample selection

The sample was drawn by **stratified simple random sampling without replacement**, seed = 20260701 (numpy default_rng), fully reproducible from `scripts/build_verification_sample.py`. The realized worklist is `data/screened/human_verification_worklist.csv`.

## 6. Reviewer procedure

1. The reviewer is a credentialed health-informatics researcher who did **not** build the machine rubric.
2. The reviewer applies the **same a priori rubric** (inclusion/exclusion criteria and Stage-2 scope codes X1-X5, plus Stage-1 codes E1-E6) documented in `analysis/screening_rubric.md` and Supplementary File S1.
3. For strata A-B the reviewer assesses on the **same evidence basis** the machine used (full text for A, abstract for B) so agreement is not confounded by evidence access; a secondary pass on stratum B using retrieved full text (where obtainable) tests whether abstract-only inclusion decisions survive full-text confirmation.
4. The worklist presents record metadata and the machine decision + justification. To reduce anchoring, the reviewer is instructed to **form an independent decision first** and record it, then mark AGREE/DISAGREE. (A fully blinded variant — machine decision hidden — is preferable if reviewer time allows; the worklist supports it by ignoring the `machine_decision` column.)
5. For each record the reviewer completes: `reviewer_decision` (AGREE / DISAGREE), and if DISAGREE, `reviewer_corrected_label` (INCLUDE / EXCLUDE + reason code) and `reviewer_notes`.

## 7. Analysis and decision rules

For each stratum compute: percent agreement, Cohen's kappa on the binary include/exclude call (with 95% CI), and the count and direction of disagreements. Pre-specified thresholds:

- **Agreement >= 0.90 (stratum):** machine decisions for that stratum accepted as reported.
- **0.80 <= agreement < 0.90:** machine decisions accepted, but the disagreement rate and its direction are reported as a sensitivity bound on the affected count in the manuscript.
- **Agreement < 0.80, or any confirmed false exclusion of a clearly eligible study in strata C/D/E:** the stratum is **fully re-screened** by the human reviewer (all N), and the funnel counts are updated from the re-screen.

A single confirmed missed-eligible in the exclusion strata (C/D/E) is treated as a signal to widen verification in that stratum (escalate to census) even if the point agreement clears 0.90, because recall on exclusions is the review's principal validity risk.

## 8. Reporting

Report in the manuscript Methods/Limitations: strata, sampled n, per-stratum percent agreement and kappa with CIs, total disagreements by direction, and any stratum escalated to full re-screen with the resulting count changes. Provide the completed worklist as a supplementary data file. This converts the current qualitative limitation ("machine-assisted, unverified") into a quantified reliability statement.

## 9. Files

- `data/screened/human_verification_worklist.csv` — the 449-record worklist for the reviewer (blank adjudication columns).
- `scripts/build_verification_sample.py` — reproducible sample-draw script (seed 20260701).
- `analysis/screening_rubric.md`, Supplementary File S1 — the rubric the reviewer applies.
- `analysis/verification_results_template.md` — where per-stratum agreement/kappa are tabulated after adjudication.
