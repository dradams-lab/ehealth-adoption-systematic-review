# Publication-Readiness Review

**Manuscript:** *Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis*
**Author:** Joshua Adams, D.I.T.
**Reviewed:** 30 May 2026
**Core contribution:** The U-T-I-O Model (User Readiness, Technical Interoperability, Institutional Alignment, Organizational Execution)

---

## Status update (30 May 2026 — fixes applied)

The mechanical, consistency, and reference issues have now been fixed and verified by a clean recompile (57 pages, zero undefined references, zero bibtex warnings). Resolved items are marked **✅ RESOLVED** below. Two items remain open because they require the author's real search data and cannot be fabricated:

- **OPEN — Blocker #1:** the search must be executed (or the claim reframed).
- **OPEN — Blocker #2:** Supplementary Files S1 and S2 now exist as **templates with clearly-marked `[[FILL: …]]` placeholders** (`supplements/S1_search_strategy.tex`, `supplements/S2_excluded_studies.tex`) and are wired into the manuscript. They must be completed with real search strings, per-database counts, and the 24 exclusion records before submission.

**Bibliography verification result:** all 27 references are real and confirmed against authoritative sources (PubMed for the 11 biomedical entries; official sources for GAO reports, NIST, the EC Estonia report, DeLone & McLean, and the Walden dissertation). One author-name error (Kruse 2016 co-authors) and two year errors (Parv, HHS) were found and corrected. No fabricated citations.

---

## Verdict: Not yet ready to submit

The manuscript is well-written, theoretically coherent, and structurally complete. The argument is clear, the prose is strong, and the compliance scaffolding (CRediT, AI disclosure, ethics, competing interests, ORCID, keywords, summary table) is in place. All 27 references are cited and resolve.

However, there are **four issues that must be resolved before submission** — one of which (the search execution) goes to the integrity of calling this a "systematic review," and two of which (missing supplements, a won't-compile bug) would cause an immediate desk problem. None are conceptually hard; the model and the writing are the hard parts, and those are done. Estimate: the must-fix list is a few days to a few weeks of work, dominated by whether you run the literature search for real.

There is also a **new and important wrinkle from your fee-free open-access requirement** — your current manuscript is tuned for *International Journal of Medical Informatics* (IJMI), which cannot give you free open access. See the journal section below.

---

## What's working well

- **Compiles to a clean 51-page PDF** once the bug below is fixed — no undefined citations, no unresolved cross-references, no missing bibliography entries.
- **Theoretical grounding is solid.** The U-T-I-O model is cleanly derived from DeLone & McLean and the TOE framework, and the mapping is made explicit.
- **Unusually transparent reliability handling.** The second-rater protocol (S4), the adjudication log, and the honest reporting of low exact agreement (κ = 0.27, reported "for transparency rather than inference") are more rigorous than most single-author reviews.
- **Compliance items present:** structured abstract, 7 keywords, IJMI-style summary table, CRediT statement, Elsevier-format generative-AI declaration, ethics/IRB statement, funding, competing interests, data availability.
- **Clean reference list** — 27 entries, all cited, no orphans.

---

## Must-fix before submission (blockers)

### 1. The systematic search appears not to have been executed
This is the central issue. The Methods are written in the **present/protocol tense** ("Records *are included* if…", "Title and abstract screening *is applied*…"), the PRISMA summary table is literally titled **"PRISMA 2020 Flow Summary *Template*,"** and your own project notes record that "formal database execution and final PRISMA count refresh are pending." Yet the abstract, results, and conclusion present the counts (424 identified → 17 included) as a completed search.

For a paper whose title claims "A Systematic Review," a reviewer who notices the protocol-tense methods and the word "Template" will treat the numbers as placeholder, and that is a credibility (and potentially integrity) problem. You have two honest paths:

- **(a) Execute the search for real** — run the documented Boolean queries in PubMed, IEEE Xplore, Scopus (plus the supplementary sources), record the actual numbers at each PRISMA stage, and rewrite Methods in past tense. This is the route that lets you keep the "systematic review" framing.
- **(b) Reframe honestly** — if you don't want to run the full search, relabel the work (e.g., "a focused/rapid evidence synthesis" or "a structured narrative review with multi-case analysis"), drop the precise PRISMA counts, and state plainly what was and wasn't done.

> Note: your project memory says the seed-set status is "disclosed in the manuscript (compliance_ethics.tex)." It is **not** — there is no such disclosure in the current files. The manuscript currently reads as a fully completed review.

### 2. Supplementary Files S1 and S2 are cited but do not exist — ⚠️ PARTIALLY RESOLVED (templates created; must be completed with real data)
The text refers readers to **Supplementary File S1** (full Boolean query strings, per-database breakdown, inclusion/exclusion criteria, coding framework) and **Supplementary File S2** (reasons for the 24 full-text exclusions) a total of three times. Neither file exists in `manuscript/supplements/` (only S3 and S4 are there), and neither is `\input` in `main.tex`. For a systematic review, the search strings and exclusion reasons are *the* core reproducibility artifacts — their absence will draw a reviewer request immediately. You must create and include both. (This is tightly coupled to issue #1: S1/S2 can only be finalized once the search is actually run or the work is reframed.)

### 3. The manuscript does not compile from a clean checkout — ✅ RESOLVED
`main.tex` triggers a fatal **"Option clash for package xcolor."** `tikz` (line 20) loads `xcolor` with no options, then line 36 reloads it with `[table]`. The `main.pdf` currently in the folder is a stale artifact from an earlier build; a fresh compile produces no PDF.

**Fix (one line):** add `\PassOptionsToPackage{table}{xcolor}` immediately after `\documentclass{...}`. Verified: with that line the document compiles cleanly to 51 pages with zero reference/citation errors.

### 4. Source count is inconsistent (16 vs. 17) — ✅ RESOLVED (DeLone row added to the evidence extraction matrix)
The abstract, results, and conclusion all state **17 included sources**. The *Mapping of Evidence Sources* table (determinant_matrix) lists **17** rows. But the **Evidence Extraction Matrix** — the canonical "here are the included studies" table — lists only **16**. The missing one is **DeLone & McLean (2003)**, which appears in the determinant matrix but not the extraction matrix. Either add a DeLone row to the extraction matrix (making it 17 and consistent), or reconcile the count everywhere. As it stands, the two supplementary tables disagree with each other and with the headline number.

---

## Should-fix (will likely draw reviewer comments)

- **✅ RESOLVED — "S1" means two different things.** The appendix renumbers tables as S1, S2, … so the Evidence Extraction Matrix auto-labels as **"Table S1,"** while the text also refers to a **"Supplementary File S1"** (the search strings). Two different documents both called "S1." Rename one scheme (e.g., call the appendix files "Supplementary File S1: Search Strategy," "…S2: Exclusions," and keep the extraction matrix as "Supplementary Table S3," or use a clearly distinct prefix) so the cross-references are unambiguous.
- **AI as the only second rater.** The reliability check rests entirely on an AI second-rater pass; the human second rater is "pending recruitment." Reviewers in medical informatics may discount AI-as-rater for inter-rater reliability. The manuscript is admirably transparent about this, but recruiting even one credentialed human rater for the 16 case-domain cells would materially strengthen the central empirical claim. This is the single highest-value scientific addition you could make.
- **Tone of the Conclusion.** The closing section shifts into strong normative rhetoric ("human obligation," "shared covenant with patients," "preventable deaths"). It's well-written, but for a systematic review some reviewers will read it as over-reaching beyond what the evidence supports. Consider trimming or clearly flagging it as a normative reflection.
- **Source typology doesn't quite add up.** Results describes the 17 as "4 + 3 + 4 + 6," but Adams (2020), a qualitative case study, doesn't fit cleanly into any of those four buckets. Minor, but a careful reviewer will check the arithmetic.

---

## Minor / polish

- **Reference metadata errors — ✅ RESOLVED (except cosmetic onc key):**
  - `parv2012estoniahie` — ✅ fixed to 2012 (PubMed PMID 22874318 confirms).
  - `hhs2012deidentification` — ✅ fixed to 2012 (issued 26 Nov 2012; accessed-2026 note added).
  - `kruse2016adoption` — ✅ co-author first names corrected (Krysta Kothman, Keshia Anerobi, Lillian Abanaka) to match PubMed.
  - `onc2025reports` — key says 2025, `year = {2023}`. Left as-is (cosmetic; renaming the cite key would touch every `\cite`). Optional cleanup.
  - `estonia2026ehealth` — dated 2026 (web access date). Acceptable for a web source.
- **47 overfull `\hbox` warnings** — cosmetic (lines slightly past the margin, mostly in the wide tables). Worth a pass before camera-ready, not before submission.

---

## Open-access / journal-fee strategy (your no-pay requirement)

You want to publish open access **without you or anyone paying**. This is achievable, but it changes the target — and the current manuscript is formatted specifically for IJMI.

**The key distinction most authors miss:** "open access" and "free to publish" are two different axes.

- **IJMI (Elsevier), your current target** — free to *submit* and free to *publish* via the normal subscription route (you pay nothing), **but** the article is then paywalled. Making it open access at IJMI requires a Gold OA APC (Elsevier list price for IJMI is in the ~US$3,800 range). So IJMI **cannot** give you free open access.

You have two genuinely fee-free routes:

1. **Diamond / Platinum open access** — journals that charge authors *nothing* and are free to read. These exist in health/medical informatics but are a smaller set, and you'd need to reformat to the new journal's template. Find them by filtering the **Directory of Open Access Journals (DOAJ)** for "without fees" in the health-informatics subject area, and verify there are no hidden submission charges. Caveat: some diamond-OA journals have unstable funding and occasionally close, so check the journal is currently active and indexed (Scopus/PubMed) before committing.

2. **Green open access (often the easiest)** — publish in a no-APC journal (this can even include IJMI via its subscription route, where you pay nothing), then **self-archive** the accepted manuscript for free so anyone can read it: a preprint on **medRxiv**, the accepted version in **PubMed Central** or your **institutional repository**. This gives you free publication *and* free public access, and lets you keep a strong, well-indexed journal as the venue.

Watch out for: **"Informatics in Medicine Unlocked"** (Elsevier) and **JMIR Medical Informatics** are full open access but **charge APCs** (~US$2,500+), and the **Online Journal of Public Health Informatics** charges ~US$1,500 — none of these are fee-free. Avoid solicitations from unknown "open access" journals promising fast review; predatory venues target exactly this requirement.

**Recommendation:** Decide the venue *before* the final polish, because the manuscript's summary table, AI-declaration format, and reference style are IJMI-specific and would need adapting for a different journal. If you're open to it, green OA (a no-APC journal + medRxiv/PMC self-archiving) is usually the lowest-friction way to satisfy "open access, no payment" without abandoning a reputable venue.

---

## Prioritized action plan

**Phase 1 — Decisions (do these first; they gate everything else)**
1. Decide the **honesty path** for the search: run it for real (keeps "systematic review") vs. reframe the paper's claim. *(Blocker #1)*
2. Decide the **target journal** given the no-fee constraint: diamond OA vs. green OA (no-APC journal + self-archiving). *(Determines formatting)*

**Phase 2 — Must-fix (blockers)**
3. Apply the one-line **xcolor fix** so the document compiles. *(Blocker #3 — 2 minutes)*
4. **Reconcile the 16-vs-17** source count (add DeLone to the evidence extraction matrix, or correct the count). *(Blocker #4)*
5. Based on the Phase 1 search decision, **create Supplementary Files S1 (search strings + per-database counts) and S2 (24 exclusion reasons)**, and `\input` them. Rewrite Methods in past tense if the search was executed. *(Blockers #1 + #2)*

**Phase 3 — Strengthen (should-fix)**
6. Fix the **"S1" labeling collision** between the appendix table numbering and the cited supplementary files.
7. If feasible, **recruit one human second rater** for the 16 case-domain cells and report the result.
8. **Trim the Conclusion's** normative rhetoric to match evidentiary scope.

**Phase 4 — Polish (pre-submission)**
9. Fix the **reference-year errors** (parv2012, hhs2012, onc2025).
10. Clean up **overfull boxes**; reformat to the chosen journal's template; final proofread.

---

*Bottom line: the intellectual work is done and it's good. What stands between you and submission is (1) being straight about whether the search was actually run, (2) producing the two missing reproducibility supplements, (3) a trivial compile fix, (4) a count reconciliation — and (5) picking a venue that actually gives you free open access, which your current IJMI target does not.*
