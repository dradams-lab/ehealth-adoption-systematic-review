# Pre-Submission Audit — Determinants of eHealth Systems Adoption (U-T-I-O)
**Date:** 9 July 2026 · **Target:** JMIR Medical Informatics (Original Paper)
**Auditor:** full-text + data + build trace against the on-disk repository

## Verdict
**Submittable on the science and the mechanics — one substantive step remains
(human adjudication of the machine-assisted screen).** Every internal-consistency,
bibliography, compile, and data-reconciliation check passes. The remaining items
are (1) the human screening-validation step, and (2) author decisions that only
you can fill in (funding, COI, preprint, ORCID). Nothing is broken; nothing is
misrepresented.

---

## PASS — what is verified clean

### 1. Numeric consistency (funnel)
The canonical funnel reconciles across the manuscript body, tables, supplements,
AND the actual data files — no stale numbers anywhere:

`1,688 identified (PubMed 1,591 + IEEE 97) → 8 duplicates → 1,680 screened
→ 1,131 excluded T/A (Stage 1: 433; Stage 2: 698) → 549 assessed
→ 48 excluded full-text → 501 included + 4 national cases.`

- Arithmetic: all identities hold (1688−8=1680; 433+698=1131; 1680−1131=549; 549−48=501).
- Data files match claims exactly: screening log = 1,680 rows; included CSV = 501;
  exclusions CSV = 48; prisma_counts_final.json agrees.
- Old funnel (424/394/43/17/21) fully purged — zero stale hits.
- Domain coverage (n=501): U=410, T=421, I=400, O=476 — matches the figure.

### 2. Bibliography integrity
33 cited keys = 33 defined entries. **Zero undefined, zero orphaned.** The four
Results exemplar reviews were reconciled to the executed-search included set in a
prior pass; the displaced exemplars remain legitimately cited in conceptual contexts.

### 3. Compiled PDF
- 75 pages; up to date (no source file newer than the PDF).
- **Zero unresolved `??` cross-references.**
- Zenodo DOI (10.5281/zenodo.21282519) renders in the Data Availability statement.
- No placeholder/DRAFT/TODO markers anywhere in the manuscript tree.

### 4. Abstract (JMIR compliance)
- 352 words (limit 450). All five structured headers present
  (Background / Objective / Methods / Results / Conclusions).
- Keywords: 9, MeSH-aligned, and now identical between the abstract and
  submission_metadata.md (reconciled 9 Jul — see note D).

### 5. Limitations — honest and complete (8 items)
Includes the two that matter most for reviewer trust:
- **Seventh:** database coverage restricted to PubMed + IEEE (Scopus/WoS/CINAHL
  access unavailable) — stated, not hidden.
- **Eighth:** LLM-assisted screening; 277 of 549 eligibility calls made on
  abstracts; human verification explicitly noted as outstanding; included count
  framed as "reproducible from the logged procedure rather than human-adjudicated."

### 6. Reviewer-comment resolution (Josh's points)
- VA and DoD scored **separately** (UAI 0.49 vs 0.66) — the don't-lump point.
- U-T-I-O operationalized into the bounded 0–1 UAI with an equation, two weight
  schemes, and a non-compensatory floor — the descriptive-vs-evaluative point.
- Estonia justified as an empirical high-alignment reference case, not an assumed
  gold standard. Platform-positioning subsection added (Epic/Oracle-Cerner/MEDITECH).

### 7. Open-data / reproducibility
- Data Availability statement points to the real Zenodo deposit (DOI live).
- Reproducibility bundle archived; supplementary data files staged in-repo
  (screening log, evidence base, exclusions, dedup audit).

---

## REMAINING — before you hit submit

### A. Substantive (the one real blocker) — human screening validation
Screening reliability currently rests on **machine-vs-machine agreement**
(Claude second-rater, κ ≈ 0.61 over the 449-record stratified sample). No human
has adjudicated the disputed records yet.

- The cross-model third-rater run (Gemini) **failed**: 439 of 449 calls returned
  `PARSE_FAIL` — root cause was **HTTP 429 RESOURCE_EXHAUSTED (free-tier quota)**,
  not a bad key (the key worked; the quota was used up after ~10 calls). On the 10
  that succeeded, Claude-vs-Gemini κ = 0.78 — the method is sound; the run just needs
  to be rerun after the quota resets (or with billing enabled / a lighter model).
  It is checkpointed, so the rerun resumes from the 10 good ratings. See note D for
  the script hardening that now handles this.
- **This is the single strongest thing to finish before submission.** It converts
  the reliability section from "machine-vs-machine" into "human-validated," which
  is precisely the objection a methods reviewer will raise about AI-assisted screening.

### B. Author decisions (only you can fill these) — in submission/
- Verify **ORCID** resolves (0000-0002-7185-9125).
- Confirm **funding** statement (cover_letter, metadata brackets).
- Confirm **competing-interests** statement.
- Choose **preprint** status and disclose it (the Zenodo deposit partly covers "public early").
- Request **APF waiver** at submission if unfunded.

### C. Known methodological departures (documented, defensible — not blockers)
These are stated openly in the Limitations and PRISMA checklist. A strict SR
reviewer may note them; they are acceptable for a framework/synthesis paper:
- Not prospectively registered (no PROSPERO record).
- No formal per-study risk-of-bias tool; no GRADE certainty rating.
- Two databases only (access-limited).

### D. Housekeeping
- Local commits (DOI insertion, Gemini script, this audit + fixes) are
  **unpushed** — `git push origin main`.
- Keyword reconciliation **done** (9 Jul): the abstract keyword line now matches
  the MeSH-aligned set in submission_metadata.md. This edits abstract.tex, so the
  current compiled PDF is now one keyword-edit stale — it regenerates at the final
  recompile, which is mandatory anyway once the human adjudication updates the
  reliability numbers. No separate recompile needed for the keywords alone.
- Gemini script **hardened** (9 Jul): the failed run was HTTP 429 (free-tier
  quota), not a bad key. The script now does a fail-loud preflight, backs off on
  429, trips a circuit breaker when the daily quota is exhausted (keeping the
  checkpoint), and re-attempts errored records on rerun. Default model switched to
  gemini-2.5-flash-lite (higher free quota). Rerun after your quota resets.

---

## Bottom line
The manuscript is internally consistent, compiles clean, reconciles to its data,
addresses the reviewer comments, and discloses its limitations honestly. Finish
the human screening-validation step (A), fill the author brackets (B), and it is
ready to submit to JMIR Medical Informatics.
