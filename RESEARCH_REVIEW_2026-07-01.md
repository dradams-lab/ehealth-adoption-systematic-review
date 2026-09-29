# Full Research Review — *Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis*

**Author:** Joshua Adams, D.I.T. (Independent Researcher)
**Core contribution:** The U-T-I-O Model — User Readiness, Technical Interoperability, Institutional Alignment, Organizational Execution
**Reviewed:** 1 July 2026
**Materials examined:** full LaTeX manuscript (all sections, tables, figures, supplements S1–S4), the raw search exports in `data/searches/`, `prisma/prisma-counts.xlsx`, `analysis/coding.xlsx`, `data/final/evidence_extraction_table.csv`, `notes/`, the prior 30-May publication-readiness review, Josh's comments, and the git history.

---

## Bottom line

The intellectual work is genuinely strong: the U-T-I-O model is cleanly derived from DeLone & McLean and TOE, the writing is publication-grade, and the compliance scaffolding (structured abstract, PRISMA checklist, CRediT, AI declaration, ethics, competing interests, summary table) is complete. The reliability handling is unusually transparent for a single-author review.

**But the manuscript cannot be submitted in its current state, and the reason is more serious than the 30-May review recorded.** Between that review and now, the formal searches *were actually executed* (git commit `e03482d`, "Execute formal database searches"; real exports are committed to `data/searches/`). That should have closed the central blocker. Instead it opened a worse one: **the manuscript body was never reconciled to the search that was run.** The paper now reports one set of numbers (a seed-set estimate) while its own Supplementary File S1 and its raw data report a completely different, contradictory set. A reviewer who opens the supplement will see the paper contradict itself on the single most important fact in a systematic review — how many records the search returned.

This is fixable in days, not weeks, because the real data exist. But it must be fixed before this goes anywhere.

---

## Blocker 1 — The PRISMA numbers in the paper contradict the search that was actually run

This is the defining issue. There are two incompatible accounts of the search inside the same repository:

**What the manuscript body reports** (abstract, Methods, `prisma_flow.tex`, `prisma_tikz.tex`, summary table):
- "Three primary databases — PubMed, IEEE Xplore, Scopus — supplemented by Web of Science, CINAHL, Google Scholar, hand-search, expert recommendations"
- **424 records identified** across 8 sources → 30 duplicates → 394 screened → 351 excluded at title/abstract → 43 sought → 41 assessed → 24 excluded → **17 included**
- Per-database (from `prisma-counts.xlsx` and `notes/search-strategy.md`): PubMed 142, IEEE 28, Scopus 97, WoS 84, CINAHL 31, Scholar 24, hand 12, expert 6

**What actually happened** (Supplementary File S1 §4, plus the raw exports I counted in `data/searches/`):
- Only **two** databases were searched — PubMed and IEEE. Scopus, Web of Science, and CINAHL "could not be searched, as institutional subscription access was unavailable." Google Scholar returned 0 unique in-window records.
- **PubMed = 1,591 records** (I counted: 1,591 PMID entries in `pubmed_results.nbib`, 1,591 TY entries in the RIS — they agree)
- **IEEE = 97 records** (I counted: 97 rows in `ieee_results.csv`, 97 TY entries in the RIS)
- S1's own totals: **1,688 identified → 22 duplicates (Rayyan) → 1,666 screened**

So the headline identification number is off by a factor of four (424 vs 1,688), the database list is wrong (8 sources claimed; 2 actually searched, 3 explicitly inaccessible), and the two accounts cannot both be true. **The 424/394/351/43/41 chain in the manuscript is a stale seed-set estimate that predates the real search and was never replaced.**

Downstream consequences that a reviewer will immediately catch:
- **The screening arithmetic is now internally impossible.** If 1,666 unique records went to title/abstract screening (S1), the manuscript's "351 excluded at T/A, 43 sought for full text" cannot hold — that pathway was built for 394 screened records, not 1,666. There is currently **no documented screening pathway from 1,666 → 41 full-text → 17 included.** The T/A screening decisions for ~1,650 records do not exist in the repo (`data/screened/` is empty; `notes/screening-log.md` is an empty stub; the workbook's screening-log tab is a blank template).
- **The abstract and Methods claim Scopus** as one of three primary databases. S1 says Scopus was never searched. These are in direct conflict within one submission.

**What must happen:** pick one true account and propagate it everywhere. Given the real exports exist, the honest path is to rebuild the PRISMA flow from the actual 1,688 → 1,666 numbers, then **actually perform and log the title/abstract screening** of those 1,666 records down to the full-text set and the final 17. Every count in the abstract, Methods, `prisma_flow.tex`, `prisma_tikz.tex`, the summary table, `prisma-counts.xlsx`, and `notes/search-strategy.md` must be regenerated from that log. The database list must be corrected to PubMed + IEEE (with Scopus/WoS/CINAHL moved to Limitations as an access constraint — which S1 already does, but the abstract/Methods/PRISMA figure do not).

Until the screening of the real corpus is done and logged, the "17 included" endpoint is not connected to the "1,666 screened" starting point by any auditable trail — and that gap is exactly what a systematic-review reviewer exists to find.

---

## Blocker 2 — Supplementary File S1 openly contradicts itself

S1 is in a self-contradictory half-migrated state:

- Its header comment (updated 4 June) and a red **"DRAFT — not for submission as-is"** banner both say the searches "have **not yet been executed**" and the evidence base "is a provisional seed set."
- Three `[[TO RECORD: ...]]` placeholder markers remain in the body (e.g., "Search executed: [[TO RECORD: date(s) each database was searched]]").
- **Yet §4 of the same file states the searches "were executed on June 4, 2026"** and gives the real per-database counts (PubMed 1,591, IEEE 97, total 1,688, 22 duplicates, 1,666 screened).

So S1 simultaneously says the search was not run and reports the results of running it. If submitted as-is, the very first supplement a reviewer opens announces in a red box that the study is not ready. The DRAFT banner and the three `[[TO RECORD]]` markers must be removed, and S1's own §4 numbers must become the numbers the whole manuscript uses.

---

## Blocker 3 — The analysis workbook names different studies than the manuscript

`analysis/coding.xlsx` is the underlying thematic-coding artifact — the actual record of which sources were coded into U-T-I-O. Its author names do **not** match the manuscript's evidence tables (`evidence_extraction_table.csv`, `determinant_matrix.tex`) for the same row positions:

| Row | `coding.xlsx` (the analysis) | Manuscript evidence table |
|---|---|---|
| 1 | **Adler-Milstein** et al. 2023 | Holmgren et al. 2023 |
| 2 | **Holmes** et al. 2016 | Eden et al. 2016 |
| 5 | Aguirre et al. **2020** | Aguirre et al. **2019** |
| 6 | **Bitar** et al. 2023 | Torab-Miandoab et al. 2023 |

The U-T-I-O checkmark pattern is identical row-for-row, which means the domain coding was kept but the *source identities were relabeled* in the manuscript without updating the workbook. This matters for two reasons: (a) it signals the citations may have been swapped late without re-verifying that each renamed source actually supports the coded domains, and (b) if a reviewer or a journal's reproducibility check requests the coding workbook (routine for systematic reviews), it will name studies that appear nowhere in the reference list. The 30-May review confirmed the 27 references themselves are real and correctly attributed — so the manuscript side is probably the correct one — but the workbook must be reconciled to it so the analysis trail is internally consistent. (Note the Research Plan also cites "Bitar et al. 2023" as journal-alignment evidence; that name should be checked wherever it appears.)

---

## Should-fix (will draw reviewer comments)

1. **AI is still the only second rater.** Both reliability checks — the 16 case-domain rubric cells (within-one-band 15/16 = 93.8%; exact 6/16 = 37.5%; weighted κ = 0.27) and the 17-source domain-presence coding (6/8 = 75%) — rest entirely on an AI (Claude Opus 4.7) second-rater pass. The manuscript is admirably candid about this and correctly reports κ "for transparency rather than inference" at N=16. But medical-informatics reviewers may discount AI-as-rater for inter-rater reliability. Recruiting even one credentialed human to re-rate the 16 cells is the single highest-value scientific addition available and would convert the study's biggest methodological soft spot into a strength. The manuscript already names this as an outstanding limitation — good — but it remains the central empirical vulnerability.

2. **Methods are still written partly in protocol/present tense.** "Records *are included* if…", "Title and abstract screening *is applied*…". Once the real screening is done, rewrite in past tense throughout so the Methods describe what was done, not what is planned.

3. **The "PRISMA 2020 Flow Summary *Template*" caption** still contains the word "Template" (`prisma_flow.tex`). Remove it — that single word tells a reviewer the numbers are placeholders.

4. **Conclusion tone.** The closing section shifts into strong normative rhetoric (interoperability as "ethical imperative," "shared obligation to patients," fragmentation "measured in diagnostic delay"). It is well-argued, but for a systematic review some reviewers will read it as reaching beyond the evidence. Consider trimming or explicitly flagging it as a normative reflection.

5. **Source typology arithmetic.** Results describes the 17 as "4 systematic/umbrella + 3 scoping/narrative + 4 government/institutional + 6 policy/framework." The prior review flagged that Adams (2020), a qualitative case study, and DeLone & McLean (an IS-theory paper) sit awkwardly in "scoping/narrative reviews." The `prisma-counts.xlsx` "Included in synthesis" note even gives a *different* breakdown ("6 systematic/umbrella + 4 scoping/narrative + 4 government/audit + 3 policy/framework"). Pick one typology and make it consistent across Results, the workbook, and S1.

---

## Substantive/design issues raised by Josh (still partly unaddressed)

Josh's comments identify a genuine conceptual tension that the current draft manages rhetorically rather than resolving:

- **Is U-T-I-O a descriptive framework or a scoring model?** Josh asks directly: if it evaluates systems, it needs measured variables, weights, and an equation yielding a 0–1 score. The manuscript writes "Adoption = f(U, T, I, O)" as a formal equation but never defines f — the "ratings" are qualitative High/Medium/Low-Medium/Low bands assigned by preponderance of evidence. Presenting a function notation for what is actually a four-cell qualitative rubric invites exactly Josh's critique. Either commit to the qualitative diagnostic framing and drop the equation styling, or operationalize f. The manuscript's "U-T-I-O-OM future work" section gestures at this but the present tension remains.
- **Case-selection justification.** Josh asks why Estonia (is it a gold standard?), and objects to lumping VA and DoD together since they don't run the same system. The Methods justify selection by "maximum variation" and documentation availability, which is a defensible purposive-sampling rationale — but the VA/DoD conflation is a fair hit: they are one row in the case table yet the text discusses distinct programs (VA's Oracle/Cerner rollout vs. DoD's MHS GENESIS). Consider splitting them or explicitly justifying the joint treatment (shared federal EHR-modernization contract vehicle).
- **Platform/market context.** Josh notes Epic, Cerner/Oracle, and other major vendors are the foundation of these systems and shape the environment; the paper largely treats platforms implicitly. A short paragraph on the vendor-platform landscape would strengthen the Institutional/Technical framing.
- **RQ wording.** Josh's line edits (RQ1 "consistently" → "most significant/impactful"; RQ2 drop "real-world"; RQ3 drop "reusable," prefer "universal/broad-based") are quick, sensible improvements not yet applied — the RQs still read "consistently," "real-world," and "reusable/synthesized."

---

## Minor / polish

- **`onc2025reports` cite key** says 2025 but `year = {2023}` in the .bib (cosmetic; renaming touches every `\cite`).
- **`estonia2026ehealth`** dated 2026 (web access date) — acceptable for a web source but flag it as an access date.
- **~47 overfull `\hbox` warnings** — cosmetic, mostly in the wide tables; worth a camera-ready pass.
- **Open-access / venue constraint (from the 30-May review, still live):** the manuscript is formatted for IJMI, which is free to submit but cannot give fee-free open access (Gold OA APC ~US$3,800). If the no-fee open-access requirement stands, the realistic routes are (a) a diamond/platinum-OA health-informatics journal (reformat required) or (b) green OA — publish in a no-APC subscription journal and self-archive the accepted manuscript on medRxiv / PubMed Central. Decide the venue *before* final polish, since the summary table, AI-declaration format, and reference style are IJMI-specific.

---

## Prioritized action plan

**Phase 1 — Reconcile the search (the blocker that gates everything)**
1. Perform and log the title/abstract screening of the real 1,666-record corpus down to the full-text set and the final 17; save the screening log to `data/screened/`.
2. Regenerate every PRISMA count from that log; propagate to abstract, Methods, `prisma_flow.tex`, `prisma_tikz.tex`, summary table, `prisma-counts.xlsx`, and `notes/search-strategy.md`.
3. Correct the database list everywhere to PubMed + IEEE; state the Scopus/WoS/CINAHL access limitation in the abstract/Methods, not just S1.

**Phase 2 — Fix the supplements and provenance**
4. Remove S1's DRAFT banner and the three `[[TO RECORD]]` markers; make S1 §4 the single source of truth for counts.
5. Reconcile `analysis/coding.xlsx` author names/years to the manuscript's reference list (Holmgren, Eden, Torab-Miandoab; Aguirre 2019).
6. Complete S2 (the 24 full-text exclusion reasons) against the real screening — it still has 28 `[[...]]` placeholders.

**Phase 3 — Strengthen**
7. Recruit one human second rater for the 16 case-domain cells; report the result.
8. Rewrite Methods in past tense; remove "Template" from the PRISMA caption.
9. Resolve Josh's descriptive-vs-scoring tension (define f or drop the equation styling); split or justify VA/DoD; add a vendor-platform paragraph; apply the RQ wording edits.

**Phase 4 — Polish**
10. Trim Conclusion rhetoric; fix source-typology arithmetic; fix bib cosmetics; clear overfull boxes; confirm venue and reformat if needed.

---

## What is genuinely good (keep)

- The U-T-I-O model is a clean, defensible synthesis with an explicit theoretical lineage (D&M → U,T; TOE → I,O).
- The comparative case table and the "technical interoperability is necessary but insufficient" finding are well-supported by the coded evidence and are the paper's most persuasive empirical result.
- The transparency of the reliability reporting (honest κ, conservative-direction disagreements, disclosed AI-rater limitation) is above the norm for single-author reviews.
- The worked VA/DoD diagnostic example and the "non-measurement of outcomes is itself a governance finding" argument are original and land well.
- The scope discipline — explicitly bounding the model to implementation-readiness validity and *not* claiming clinical-outcome validity — is exactly right and pre-empts an obvious reviewer objection.

**In one sentence:** the model and the prose are ready; the systematic-review machinery underneath them is not yet telling one consistent, auditable story about the search that was actually run, and that must be fixed before submission.
