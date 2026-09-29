# Title/Abstract Screening Rubric — a priori criteria

Derived verbatim from the manuscript Methods (§Inclusion and Exclusion Criteria) and Supplementary File S1. Applied to all 1,680 unique records.

## Scope of this review
Determinants (barriers, facilitators, success factors) of ADOPTION / IMPLEMENTATION of eHealth systems — EHR, EMR, HIE, health information technology, or clinical interoperability — at the organizational or system/national level.

## INCLUDE only if ALL of the following hold:
1. **Topic — technology:** concerns eHealth / EHR / EMR / HIE / health information technology / clinical interoperability (not an unrelated clinical or biomedical topic that merely mentions an EHR in passing).
2. **Topic — adoption:** addresses adoption, implementation, acceptance, barriers, facilitators, determinants, success factors, or uptake of the system (not solely a clinical outcome, algorithm-performance, or data-secondary-use study).
3. **Design:** empirical study, systematic/scoping/umbrella review, OR framework/policy analysis with a stated basis. 
4. **Window:** 2015 or later (empirical search window). Pre-2015 items are EXCLUDED here (foundational theory, e.g. DeLone & McLean 2003, is handled separately as background, not via this screen).
5. **Language:** English.

## EXCLUDE — reason codes:
- **E1 — wrong focus (technology):** not about eHealth/EHR/HIE/HIT/interoperability adoption; e.g. a purely clinical trial, a wearable/sensor engineering paper, a bioinformatics method, telehealth clinical efficacy with no adoption-determinant lens.
- **E2 — wrong outcome/topic (adoption):** about eHealth but NOT about adoption/implementation determinants; e.g. uses EHR data to study a disease, reports a prediction model, evaluates a clinical intervention delivered via EHR without studying uptake.
- **E3 — wrong setting/population:** out of scope setting (e.g. single-patient case report, non-health-sector IT, consumer app unrelated to health-system adoption) OR narrowly a patient-facing acceptance study with no organizational/system relevance. Use sparingly.
- **E4 — insufficient methodology / publication type:** editorial, letter, commentary, opinion, conference abstract without methods, protocol-only, poster.
- **E5 — duplicate / non-English / not retrievable metadata:** language other than English, or duplicate not caught in dedup.
- **E6 — outside publication window:** published before 2015 (criterion 4 above). *Added 29 Sep 2026 — see note below.*

## Stage-2 (eligibility refinement) — reason codes
Applied to the 1,247 Stage-1 survivors to enforce the review's precise scope: adoption of interoperable eHealth **systems** (EHR/EMR/HIE/health-IT infrastructure) at the **organizational or national/system** level. *Added 29 Sep 2026 — see note below.*
- **X1 — patient/consumer-facing acceptance only:** individual patient or consumer acceptance of an app/portal/service, with no organizational or system-level adoption lens.
- **X2 — single-condition digital-health intervention:** evaluates a digital intervention for one condition rather than adoption of an eHealth system.
- **X3 — EHR as data source/channel only:** uses an EHR only as a data source or delivery channel for a clinical outcome.
- **X4 — out-of-scope technology or setting.**
- **X5 — non-research publication type.**

> **Note on codes E6 and X1–X5 (added 29 Sep 2026).** These codes appear in `screening_log_combined.csv` (E6 in `reason_code`; X1–X5 in `s2_reason`) but were not listed in the original version of this rubric. The definitions above are taken from the stage descriptions in `data/screened/01_screening_method.md`. E6 codes the existing 2015 window criterion. X1–X5 were introduced at Stage 2; whether they were fixed before Stage 2 began was not documented, so they should not be read as part of the a priori rubric. E5 is defined but was not used.

## Decision output per record
- `decision`: INCLUDE | EXCLUDE | MAYBE
- `reason_code`: (blank if INCLUDE) one of E1–E6 (Stage 1); Stage-2 exclusions record X1–X5 in `s2_reason`
- `justification`: one clause grounded in the title/abstract
- MAYBE reserved for genuinely borderline records that need full-text; treated as "sought for full text".

## Notes
- Records lacking an abstract are screened on title + venue + doctype; if topic cannot be established, default to MAYBE (do not exclude for missing abstract alone).
- Reviews of adoption ARE eligible (this review synthesises reviews as well as primary studies).
- A record generically about "digital health adoption" in a health-system context is INCLUDE even if not US-based (English-language only).
