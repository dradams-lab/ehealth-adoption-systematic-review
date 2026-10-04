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

The realized total is 449 records (27% of the frame). If observed agreement in a stratum is >= 0.95, the CI half-width tightens to ~0.035; if agreement falls below 0.80, that stratum is escalated to a full re-screen (Section 7; corrected 29 Sep 2026 from "~0.85" to match the Section 7 decision rule).

## 5. Sample selection

The sample was drawn by **stratified simple random sampling without replacement**, seed = 20260701 (numpy default_rng), fully reproducible from `scripts/build_verification_sample.py`. The realized worklist is `data/screened/human_verification_worklist.csv`.

## 6. Reviewer procedure

1. The reviewer is a credentialed health-informatics researcher who did **not** build the machine rubric.
2. The reviewer applies the **same a priori rubric** (inclusion/exclusion criteria and Stage-2 scope codes X1-X5, plus Stage-1 codes E1-E6) documented in `analysis/screening_rubric.md` and Supplementary File S1.
3. For strata A-B the reviewer assesses on the **same evidence basis** the machine used (full text for A, abstract for B) so agreement is not confounded by evidence access; a secondary pass on stratum B using retrieved full text (where obtainable) tests whether abstract-only inclusion decisions survive full-text confirmation.
4. The worklist presents record metadata and the machine decision + justification. To reduce anchoring, the reviewer is instructed to **form an independent decision first** and record it, then mark AGREE/DISAGREE. (A fully blinded variant — machine decision hidden — is preferable if reviewer time allows; the worklist supports it by ignoring the `machine_decision` column.)
5. For each record the reviewer completes: `reviewer_decision` (AGREE / DISAGREE), and if DISAGREE, `reviewer_corrected_label` (INCLUDE / EXCLUDE + reason code) and `reviewer_notes`.

> **Deviation note (4 October 2026).** The human check is being applied to a 126-record subset of the 449, at title/abstract level for all strata, using a fully blinded sheet (`data/screened/human_adjudication_blinded.xlsx`) in which the reviewer records an independent decision (INCLUDE / EXCLUDE + code / MAYBE) rather than AGREE/DISAGREE. The reasons and the pre-specified analysis are in Section 10.

## 7. Analysis and decision rules

> *For the 126-record adjudication this section is applied as specified in Section 10; per-stratum κ is not estimable there (Section 10, rule 6).*

For each stratum compute: percent agreement, Cohen's kappa on the binary include/exclude call (with 95% CI), and the count and direction of disagreements. Pre-specified thresholds:

- **Agreement >= 0.90 (stratum):** machine decisions for that stratum accepted as reported.
- **0.80 <= agreement < 0.90:** machine decisions accepted, but the disagreement rate and its direction are reported as a sensitivity bound on the affected count in the manuscript.
- **Agreement < 0.80, or any confirmed false exclusion of a clearly eligible study in strata C/D/E:** the stratum is **fully re-screened** by the human reviewer (all N), and the funnel counts are updated from the re-screen.

A single confirmed missed-eligible in the exclusion strata (C/D/E) is treated as a signal to widen verification in that stratum (escalate to census) even if the point agreement clears 0.90, because recall on exclusions is the review's principal validity risk.

## 8. Reporting

> *For the 126-record adjudication, reporting follows Section 10, rule 8.*

Report in the manuscript Methods/Limitations: strata, sampled n, per-stratum percent agreement and kappa with CIs, total disagreements by direction, and any stratum escalated to full re-screen with the resulting count changes. Provide the completed worklist as a supplementary data file. This converts the current qualitative limitation ("machine-assisted, unverified") into a quantified reliability statement.

## 9. Files

- `data/screened/human_verification_worklist.csv` — the 449-record worklist for the reviewer (blank adjudication columns).
- `scripts/build_verification_sample.py` — reproducible sample-draw script (seed 20260701).
- `analysis/screening_rubric.md`, Supplementary File S1 — the rubric the reviewer applies.
- `analysis/verification_results_template.md` — where per-stratum agreement/kappa are tabulated after adjudication.
- `data/screened/two_rater_comparison.csv` — the AI second rater's title/abstract decisions for 447 rated records of the 449 (added July 2026).
- `data/screened/human_adjudication_worklist.csv` — the 126-record subset (unblinded; author use only).
- `data/screened/human_adjudication_blinded.xlsx` — the blinded sheet given to the human reviewer (`reviewer_packet/`).

## 10. Adjudication of the 126-record subset (added 4 October 2026; deviation from Sections 6–7)

**Context.** Before any human reviewed the sample, an AI second rater (Anthropic Claude) re-screened all 449 records at title/abstract level (`two_rater_comparison.csv`; agreement with the primary screen 80.3%, κ = 0.61, n = 447). The human check is therefore applied to a 126-record subset rather than to the full 449: all **88** records on which the primary screen and the AI second rater disagreed, the **2** records the second rater did not rate, and **36** records on which the two agreed (a concordance spot-check). The method used to select the 36 is not recorded in the repository. [Author: state it here if known.]

**Rules fixed before unblinding.**

1. **Evidence basis.** The human decides from title and abstract for all strata, not from full text for stratum A as Section 6.3 specifies, because the 126 were defined by title/abstract disagreement and the comparator is the primary screen's title/abstract decision (`machine_ta`). For strata A and C, "agreement" therefore refers to the title/abstract pass, and the full-text eligibility decisions remain not human-verified; the manuscript states this.
2. **Decision mapping.** MAYBE counts as PASS, as in the rubric.
3. **Disputed and unrated records (88 + 2).** The human decision is final for the agreement computation: it determines whether each of these records counts as agreeing with `machine_ta`, and the AI second rater's label is not used as a tie-break. The 2 unrated records are treated as reviewed records. Individual human decisions do not change the included-study count (501) or the PRISMA funnel; counts change only if a stratum is re-screened under Section 7.
4. **Spot-check (36).** These estimate the residual error rate *e* among the 359 concordant records, pooled across strata (the per-stratum spot-check counts, 4 / 6 / 3 / 13 / 10, are too small to estimate separately) and across decision direction (13 PASS-concordant records in strata A/B/C; 23 EXCLUDE-concordant in D/E), with a two-sided 95% Clopper–Pearson interval. Pooling assumes a common error rate in both directions, which is a stated limitation given that the second rater was stricter than the primary screen; the direction-specific counts are reported beside the pooled estimate. The interval, and the bound built on it, assume the 36 were drawn at random from the 359 concordant records, which cannot be verified because the selection method is not recorded (see Context).
5. **Reconstructed per-stratum agreement.** Agreement with the primary screen is reconstructed over the stratified sample sizes of Section 3 (91 / 88 / 48 / 116 / 106): point estimate = (unreviewed concordant records × (1 − ê) + reviewed records on which the human agrees with `machine_ta`) / n, where ê is the pooled spot-check error rate from rule 4 and the unreviewed concordant counts are 52 / 63 / 12 / 102 / 94. Lower sensitivity bound = (unreviewed concordant records × (1 − the upper limit of the two-sided 95% Clopper–Pearson interval for *e*) + reviewed agreements) / n. If ê = 0 the point estimate equals the figure obtained by treating all unreviewed concordant records as agreed. The Section 7 thresholds are applied to the point estimate for strata A, B, D, and E, with the bound reported alongside. For stratum C the thresholds are reported descriptively only and do not trigger a re-screen: every C record has `machine_ta` = PASS and was excluded at full text, so a human title/abstract EXCLUDE agrees with the record's final disposition, and a re-screen could not change the included-study count. The Section 7 missed-eligible trigger is operationalised at title/abstract level as any human INCLUDE or MAYBE on a stratum D or E record. This is deliberately wider than Section 7's "confirmed false exclusion of a clearly eligible study": under the rubric MAYBE counts as PASS, so a human MAYBE against a machine EXCLUDE means the record should have reached full text, and because this check does not retrieve full text (rule 1) eligibility cannot be confirmed here. Stratum C exclusions were made at full text and are not assessed by this check.
6. **Kappa.** Cohen's κ is reported on the whole 126 (human vs primary screen) and on the 124 records the second rater rated (human vs AI second rater; R0552 and R0859, rater2 = PARSE_FAIL, are excluded from that κ), labelled as computed on a disagreement-enriched set. Per-stratum κ is not reported: the primary label is constant within each stratum of the 126, so κ is undefined there, and a reconstructed stratum κ is not estimable.
7. **Reviewer.** The planned rater is an independent reviewer with health-IT or implementation-science background who did not build the rubric (`reviewer_packet/`); background is recorded on return. If the author adjudicates instead, the paper discloses that as a further deviation.
8. **Reporting.** Methods, Supplementary File S1, PRISMA item 8, and the cover letter state that the human reviewed 126 of the 449 (enriched for AI disagreement), the reconstruction rule, and the bound. The completed sheet is published with the reproducibility bundle; the free-text notes column is removed from the public copy if the reviewer asks.
