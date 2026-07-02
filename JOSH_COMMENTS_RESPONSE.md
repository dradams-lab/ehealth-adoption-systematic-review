# Response to Josh's Comments — How Each Point Was Addressed

*Prepared 2 July 2026. Cross-references the revised manuscript.*

## 1. "Potential fatal flaw" — Is U-T-I-O descriptive or evaluative? If evaluative, it needs measured variables, weights, and a 0–1 scoring equation.

**Addressed in full.** The model is now explicitly framed as serving *both* purposes, and the evaluative side is fully operationalized:

- **New Research Question RQ4** (`research_questions.tex`) asks whether the model can be operationalized into a bounded, reproducible index, and a framing paragraph states the descriptive-vs-evaluative duality directly.
- **New section `scoring_model.tex`** (inserted after the determinant matrix) defines:
  - **Measured variables** — each domain assessed against the construct-level indicators already specified in Supplementary File S3 (e.g., SUS/clinician-satisfaction ≥75, portal adoption ≥50%, FHIR/HL7 conformance, national data-exchange layer).
  - **Numeric encoding** — the four ordinal bands (High/Medium/Low–Medium/Low) map to domain scores {1, 2/3, 1/3, 0}, each on [0,1].
  - **Scoring equation** (Eq. 1) — the U-T-I-O Alignment Index, UAI = w_U·s_U + w_T·s_T + w_I·s_I + w_O·s_O ∈ [0,1], with 1 = perfect alignment (exactly the 0–1 scale Josh requested).
  - **Weights** — two schemes: equal (theory-neutral) and evidence-informed (each weight ∝ the domain's prevalence across the 501-study base: U=0.240, T=0.247, I=0.234, O=0.279). Reporting both shows the ranking is robust to the weighting choice, not an artifact of author judgment.
  - **Non-compensatory floor** — the minimum domain score is reported alongside UAI so a single disqualifying deficit is not masked by a high weighted mean.
- **Grounding on DeLone & McLean / TOE** — the framing paragraph clarifies that U-T-I-O distils these established models into a health-IT-specific instrument; the theory anchors remain in Background.
- **Worked table + figure** — Table `tab:uai` and Figure `fig:uai` apply the equation to the national cases.

## 2. "Why Estonia? Is it a gold standard?"

Estonia scores at the ceiling on the index (UAI = 1.00), which is precisely why it anchors the high-alignment end of the case spectrum — it functions as the empirical reference point (mature national architecture, legal mandate, X-Road, broad participation). The case selection rationale (maximum contextual variation across governance models) is stated in Methods and Limitations. *Remaining author decision:* if you want to assert "gold standard" explicitly rather than "highest observed alignment," that is a stronger claim that would benefit from an external benchmark citation.

## 3. "VA and DoD — you cannot lump them together; they don't share the same system."

**Addressed.** The two programs are now **scored and analysed separately** throughout:
- The Results case table splits the single VA/DoD row into a **VA EHR (Oracle/Cerner)** row and a **DoD MHS GENESIS** row, each with its own citation and interpretation.
- The Alignment Index scores them separately, and this is where the separation earns its keep: **VA = 0.49 (mixed/constrained)** vs **DoD MHS GENESIS = 0.66 (moderate-high)** — a divergence the combined row obscured. The Discussion uses this to make a substantive point: since both run the *same* Oracle Health platform, the gap is attributable to execution/user-domain differences, not the technology.
- Abstract, Introduction, Limitations, and the RQ2 answer now say "four national implementation *contexts*, with VA and DoD analysed separately."
- *Note:* they do share the same *platform* (both migrated to Oracle Health/Cerner under the 2018 mandate); what differs is the program, timeline, governance, and outcomes. The revised text says this precisely rather than implying different vendors.

## 4. "Consider EHR/HIE platforms (Cerner, Epic, and 3–4 others) — you're arguing for a NEW system that will be compared to incumbents."

**Partially addressed; flagged for your decision.** The Discussion now makes the platform point explicitly for VA/DoD (same Oracle Health platform, divergent outcomes → platform is not destiny). What is *not* yet added is a dedicated treatment of the commercial platform landscape (Epic, Oracle Health/Cerner, MEDITECH, etc.) and how U-T-I-O positions a new entrant against incumbents. This is a substantive scoping decision:
- **Option A** — add a short Discussion subsection positioning U-T-I-O as a *platform-agnostic evaluation instrument* (it scores any system, incumbent or new, on the same four domains), which sidesteps the "new vs incumbent" competition framing.
- **Option B** — add a comparative paragraph on how major platforms score on the domains, which requires platform-level evidence the current 501-study base may not directly support.

I recommend Option A (defensible with current evidence). Say the word and I'll draft it.

## 5. RQ wording edits

All three applied in a prior revision and retained:
- **RQ1** — "consistently" → "most significantly."
- **RQ2** — dropped "real-world"; now "national eHealth implementations."
- **RQ3** — "synthesized into a reusable" → "integrated into a broadly applicable" (removed "reusable").

## Summary of files changed for this response
- New: `sections/scoring_model.tex`, `figures/utio_alignment_index.png`, `data/final/utio_alignment_index.csv`
- Edited: `main.tex` (input hook), `sections/results.tex` (VA/DoD split + caption), `sections/discussion.tex` (index + separation + RQ4), `sections/research_questions.tex` (RQ4 + framing), `sections/abstract.tex`, `sections/introduction.tex`, `sections/limitations.tex`, `tables/summary_table.tex`, `references.bib` (Ahmed year reconciled to 2019).

## Still open (your call)
- Platform-landscape treatment (point 4, Option A vs B above).
- "Gold standard" claim for Estonia (point 2) — currently framed as "highest observed alignment."
- The Discussion worked-example uses a 2018-era *pre-deployment* VA/DoD profile [I(H),T(M),U(L–M),O(L)] that predates the current case-table ratings; this is intentional (illustrating pre-deployment diagnosis) but you may want to harmonize the narrative so the two profiles are clearly distinguished as "2018 pre-deployment" vs "current."
