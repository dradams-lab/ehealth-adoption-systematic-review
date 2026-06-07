# U-T-I-O Hybrid Revision — Response to Harvey & Update Plan

**Prepared for:** Joshua Adams, D.I.T. **Date:** June 7, 2026
**Scope:** Resolves the issues raised in Harvey's review of the eHealth adoption manuscript (UTIO model, target: *IJMI*). Records the manuscript changes already made, the plan to update the Research Plan document, and remaining submission follow-ups.

---

## 1. The decision

We committed to the **hybrid** direction. U-T-I-O remains a **diagnostic framework**, but its categorical domain ratings (High / Medium / Low–Medium / Low) are now expressed as an explicit **U-T-I-O Alignment Index** on a 0–1 scale. The index is deliberately constrained as *ordinal-derived, equal-weighted, illustrative, and descriptive (not predictive, not validated)*. This directly answers Harvey's core objection — that the paper promised a scored model via the `Adoption = f(U,T,I,O)` equation but delivered only categorical ratings — at low cost and without overreaching into claims a 17-source, 4-case review cannot support.

---

## 2. Point-by-point response to Harvey

| Harvey's comment | How it was addressed | Location |
|---|---|---|
| **Model: what are you building on / comparing to? Is UTIO a theoretical framework or a system-evaluation model?** | Resolved by committing to the hybrid. The equation is reframed as a *conceptual* statement of dependence (not a fitted equation); the Alignment Index gives the 0–1 scaled output he asked for, with explicit non-validation disclaimers. | Methods §Analytical Model (Eq. 1–2); Background; Results §U-T-I-O Alignment Index (Table 5) |
| **Distill UTIO from DeLone/TOE *applied to healthcare*.** | The existing theoretical-lineage paragraph (DeLone→U/T, TOE→I/O, extended for healthcare) was retained and now reads as the derivation he asked for. | Background §Synthesis |
| **If it evaluates systems, you need measured variables, weights, and a scaled score.** | Provided as the Alignment Index, *with the honest framing* that equal weights are a deliberate conservative default and a validated weighted instrument is future work — pre-empting the "arbitrary weights" critique. | Methods (Eq. 2); Conclusion (future work) |
| **Why Estonia? Is it a gold standard?** | Added explicit justification: Estonia is the high-alignment *anchor* case, consistently ranked among the most advanced national systems and cited as an architectural reference. (Verified: #1 EC Digital Decade eHealth Index; #1 Bertelsmann Digital Health Index 2024.) | Methods §Case Selection rationale |
| **Don't lump VA and DOD — they don't share the same system.** | **Harvey's premise is outdated.** VA and DoD now run the *same* Oracle Health Millennium platform under one Federal EHR program (DoD as MHS GENESIS, VA as the VA Federal EHR; shared Cerner→Oracle contract lineage). The pairing is now *explicitly justified* on that shared foundation, with deployment/timeline divergence noted. | Methods §Case Selection rationale |
| **Consider the major EHR platforms (Epic, Cerner, +others); you're arguing a new system into that market.** | Added a platform-landscape paragraph (Epic, Oracle Health/Cerner, MEDITECH) and clarified scope: UTIO is *platform-agnostic and diagnostic — not a new product pitch* (correcting that read). Platform choice mapped to the T domain. | Background |
| **RQ1: replace "consistently" with "most significant/impactful".** | RQ1 → "What determinants most **significantly** influence…" | research_questions.tex + Discussion restatement |
| **RQ2: drop "real-world".** | RQ2 → "How are these determinants reflected in **implementations**?" | research_questions.tex + Discussion restatement |
| **RQ3: replace "synthesized"; drop "reuseable".** | RQ3 → "How can these determinants be **consolidated into a broad-based adoption model**?" | research_questions.tex + Discussion restatement |

---

## 3. Manuscript changes made (complete; compiles to 62 pp, no undefined refs)

- **`sections/methods.tex`** — Reframed the equation as conceptual; added the *U-T-I-O Alignment Index* subsection (ordinal→numeric mapping, equal-weight formula Eq. 2, three interpretation constraints); added a case-selection rationale paragraph (Estonia anchor, VA/DoD shared-platform pairing, intermediate cases).
- **`sections/background.tex`** — Equation made inline/conceptual with a pointer to the index; new platform-landscape + scope-clarification paragraph.
- **`sections/results.tex`** — New "U-T-I-O Alignment Index" subsection and **Table 5** (Estonia 1.00, ONC 0.83, NHS 0.83, VA/DoD 0.50); removed the bare repeated equation in Synthesis; wove index values into the synthesis narrative.
- **`sections/research_questions.tex`** — RQ1/RQ2/RQ3 reworded.
- **`sections/discussion.tex`** — "Research Questions Revisited" restatements updated to match; index referenced.
- **`sections/abstract.tex`** — Added one results sentence reporting the index (Estonia 1.00 / VA-DoD 0.50).
- **`sections/conclusion.tex`** — Future-work passage now names replacing the illustrative index with an empirically weighted, calibrated instrument.

---

## 4. Plan to update the Research Plan (`Research_Plan_eHealth_Adoption.docx`)

The plan document predates these revisions and should be reconciled. Recommended edits:

1. **Update note (top):** record the hybrid decision and that the Alignment Index is now a standing methodological element, with the model framed as a diagnostic framework (not a validated predictor).
2. **§1 Executive Summary / "central contribution" paragraph:** add one line stating the framework-vs-evaluation question is resolved via the hybrid index.
3. **§2 Section-by-Section Review table:** update the Methods, Results, and Research Questions rows to reflect the new index subsection, Table 5, and reworded RQs.
4. **Any place the plan restates the RQs:** propagate the RQ1/2/3 wording changes.
5. **§5 Action Plan + §6 Readiness Checklist:** add the two new submission-blockers below (table-budget triage; word-count trim) and the "convert index to figure" task.

---

## 5. Remaining follow-ups & risks (before *IJMI* submission)

These are independent of Harvey but the revision touches them, so flagging now:

- **Table budget (blocker).** The main body now carries **8 tables**; IJMI allows **max 4 tables, max 3 figures**. The manuscript currently has **0 figures**. *Recommended move:* convert the new Alignment Index (Table 5) into a **bar figure** — this both relieves table pressure and gives the paper its first figure — and relocate lower-priority tables (e.g., the Rating Scale, coding-schema, and mapping tables) to the Supplementary Files. Target ≤4 main tables / ≤3 figures.
- **Word count (blocker).** Body text is **~6,750 words** vs. IJMI's **~4,000-word** limit for the review/qualitative article type. A dedicated trimming pass is needed regardless of Harvey; my additions added ~400 words, so this is now slightly tighter.
- **Human second rater (known limitation).** Independent dual-rating with a credentialed human second rater is still outstanding and remains stated in Limitations.
- **Regenerate `manuscript_anonymous.docx`** from the revised LaTeX before submission so the anonymized Word version matches.
- **Citation hygiene.** The VA/DoD shared-platform and Estonia-benchmark statements currently lean on already-cited GAO and policy sources; if you want the external rankings (EC Digital Decade, Bertelsmann 2024) cited explicitly, add those bib entries.

---

## 6. Suggested sequence

1. Convert Alignment Index to a figure + run the table/figure triage (fixes budget).
2. Word-count trim pass to ~4,000.
3. Reconcile the Research Plan doc (§4 above).
4. Regenerate the anonymized .docx; final PRISMA/cover-letter check.
