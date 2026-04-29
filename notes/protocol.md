# Systematic Review Protocol (Retrospective)

**Title:** Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis
**Reviewer:** Joshua Adams, D.I.T.
**Affiliation:** Independent Researcher; Enterprise Architecture & Cybersecurity Consultant
**Date drafted:** April 29, 2026
**Status:** Retrospective protocol — not pre-registered. The review was already in progress (purposive seed set established) when this protocol was formalized; this document is intended as a transparent, auditable description of the review's scope, methods, and decision rules so reviewers and replicators can assess the work.
**Registration:** Not registered with PROSPERO or OSF at the time of seed-set work. **Recommended retrospective registration step (see §13 below):** upload this protocol document to the Open Science Framework (osf.io) before journal submission to obtain a stable, time-stamped registration identifier. While retrospective registration does not equal pre-registration, it provides a publicly verifiable record of methods that strengthens the credibility-of-process claim.

---

## 1. Review Question and Objectives

**Primary research question:** What determinants most consistently influence the adoption of interoperable eHealth systems (EHRs, HIEs, broader eHealth infrastructure) across diverse implementation contexts?

**Sub-questions:**
- **RQ1:** Which determinants of eHealth systems adoption are most consistently identified across the peer-reviewed literature, government reports, and grey literature?
- **RQ2:** How are these determinants reflected in real-world national eHealth implementations?
- **RQ3:** Can these determinants be synthesized into a reusable, operationalizable adoption model?

**Primary outcome:** Identification of a parsimonious, evidence-based framework for eHealth adoption — the U-T-I-O Model (User Readiness, Technical Interoperability, Institutional Alignment, Organizational Execution).

---

## 2. Eligibility Criteria

### Inclusion
- Peer-reviewed journal articles, systematic reviews, scoping reviews, or umbrella reviews
- Government / institutional reports with empirical or audit-derived basis
- Foundational frameworks and policy analyses relevant to health-IT adoption
- Focus on eHealth, EHR, EMR, HIE, health information technology, or clinical interoperability
- Addresses adoption, implementation, barriers, facilitators, or determinants
- Published January 2015 onwards (2003 baseline retained for foundational IS theory; final search-execution date to be specified upon execution)
- English language

### Exclusion
- Opinion editorials, letters, conference abstracts without full methodology
- Non-healthcare IT systems with no healthcare application
- Studies involving primary collection of identifiable human-subject data
- Published before January 2015 (except foundational theory papers retained as background)
- Non-English publications (acknowledged limitation)

Inclusion/exclusion is operationalized in `prisma/prisma-counts.xlsx` ("Inclusion-Exclusion Criteria" sheet) and reproduced verbatim in the manuscript Methods.

---

## 3. Information Sources

Three primary databases plus five supplementary sources (full per-source rationale and yield in `notes/search-strategy.md`):

| Source | Type | Platform |
|---|---|---|
| PubMed / MEDLINE | Primary | NLM |
| IEEE Xplore | Primary | IEEE |
| Scopus | Primary | Elsevier |
| Web of Science | Supplementary | Clarivate |
| CINAHL | Supplementary | EBSCO |
| Google Scholar | Supplementary | Google |
| Hand-search of reference lists | Supplementary | — |
| Expert recommendations | Supplementary | — |

**Search dates:** Formal database execution pending. Seed-set yield (current state) documented in `prisma/prisma-counts.xlsx`. Final search dates and per-source counts will be recorded as `data/raw/<source>_export.csv` files when formal searches are run.

---

## 4. Search Strategy

Full Boolean query strings for each source are documented in `notes/search-strategy.md` and will be reproduced as Supplementary File S1 of the manuscript. Strings combine technology-domain terms ("electronic health record," "EHR," "health information exchange," "eHealth," "interoperability") with adoption-related terms ("adoption," "implementation," "barriers," "facilitators," "determinants"), with database-specific MeSH/field tags, document-type filters, and date limits applied.

---

## 5. Study Selection Process

1. Records from each source exported in RIS or CSV format to `data/raw/<source>_export.<ext>`.
2. Combined library imported into Zotero (or Rayyan/Covidence). Deduplication via tool-assisted matching plus manual review of near-duplicates. Removed duplicates logged to `data/screened/duplicates_removed.csv`.
3. Title/abstract screening applied to all unique records using inclusion/exclusion criteria. Decisions logged in `data/screened/screening_log_combined.csv` (template at `prisma/prisma-counts.xlsx` → "Full Screening Log").
4. Full-text retrieval and full-text eligibility screening for all records passing title/abstract screening. Excluded full texts logged with reason in `prisma/prisma-counts.xlsx` → "Excluded Full Texts (S2)" (Supplementary File S2).
5. Single reviewer (the author). **Limitation:** independent dual-review was not feasible. Acknowledged in manuscript Limitations.

---

## 6. Data Extraction

Data extracted from each retained source into the evidence extraction matrix (`data/final/evidence_extraction_table.csv`, 24 columns). Fields include: bibliographic metadata, study type, focus, context, U-T-I-O domain coding (Y / blank per domain), primary determinants identified, key finding, methodological strengths, limitations, role in paper, and case-study flag.

Extraction conducted by single reviewer using the U-T-I-O coding framework defined in the manuscript's Coding Schema table.

---

## 7. Risk of Bias and Quality Assessment

No formal per-study risk-of-bias tool (e.g., ROBIS, AMSTAR-2) applied. Source credibility assessed informally based on:
- Peer-review status and journal/publisher reputation
- Government / institutional authority of grey-literature sources
- Methodological transparency of included reviews

**Limitation:** absence of formal risk-of-bias scoring acknowledged in manuscript Limitations.

---

## 8. Synthesis Approach

Qualitative thematic synthesis using framework analysis. The U-T-I-O Model is the organizing framework; codes are assigned to each retained source against each of the four domains (U, T, I, O). Domain-level narrative summaries are synthesized in `analysis/synthesis.md`. Cross-source patterns and convergence findings are reported in the manuscript Results and Discussion.

No meta-analysis (qualitative thematic synthesis is the chosen approach given the heterogeneity of study designs included).

---

## 9. Multi-Case Analysis Component

Four publicly documented national eHealth implementations selected by purposive sampling for U-T-I-O domain rating: U.S. ONC HIE programs; NHS Shared Care Records (UK); Estonia eHealth; U.S. VA/DoD federal EHR modernization.

Each case rated on each of the four domains (U, T, I, O) on a four-level scale (High / Medium / Low–Medium / Low) per the U-T-I-O Scoring Rubric (see `analysis/utio-scoring-rubric.md`). Ratings are derived from the preponderance of evidence in primary source documentation (GAO audits, NHS England policy documents, e-Estonia portal, ONC reports, European Commission EHR-laws survey).

**Single-rater limitation:** ratings were assigned by a single reviewer. Independent verification by a second rater is not yet performed.

---

## 10. Reporting and Dissemination

Reporting follows the PRISMA 2020 statement (Page et al., BMJ 2021;372:n71). Completed PRISMA 2020 checklist is in `prisma/PRISMA_2020_Checklist_Completed.docx`; submission-readiness items are tracked there.

Target journal: International Journal of Medical Informatics (IJMI), Reviews/qualitative-studies article type. Manuscript word counts and table/figure constraints are tracked against the IJMI Reviews limits (4,000-word full text; 300-word abstract; max 4 numbered tables in body; max 3 figures; 2–4 bullet Summary Table; supplementary materials permitted).

---

## 11. Ethics and Compliance

No human-subject data collected. All sources publicly available. No IRB approval required. HIPAA de-identification and HITECH compliance considerations apply only to grey-literature government/audit material referenced; no PHI accessed, stored, or analyzed.

Funding: None. Competing interests: None declared.

---

## 12. Status (as of this document)

| Stage | Current state |
|---|---|
| Eligibility criteria | Defined |
| Information sources | Defined (8 sources) |
| Search strategy | Drafted (`notes/search-strategy.md`); formal execution pending |
| Records identified | Seed set: 424 (estimated; pending formal execution) |
| Screening | Seed-set screening complete; formal screening pending |
| Retained sources | 17 (seed set) |
| Cases | 4 (purposive; selection final) |
| Evidence extraction matrix | Populated for the 17 seed-set sources |
| U-T-I-O scoring rubric | Documented (`analysis/utio-scoring-rubric.md`) |
| Manuscript draft | Complete; under IJMI Reviews limits |
| Submission package | Pending formal-search refresh of PRISMA counts |

---

## 13. OSF Retrospective Registration (Pre-Submission Step)

To strengthen credibility-of-process even though pre-registration was not feasible:

1. Create an OSF project at osf.io (free, requires account).
2. Upload this `protocol.md` (and optionally `notes/search-strategy.md`, `analysis/utio-scoring-rubric.md`) as project files.
3. Register the project as "Open-Ended Registration" (or equivalent), which produces a stable, time-stamped DOI and read-only snapshot.
4. Reference the OSF registration DOI in the manuscript Methods (Item 24a in the PRISMA 2020 checklist), replacing the current "not pre-registered" sentence with: "This review was not pre-registered. A retrospective protocol and supporting materials are deposited at OSF [DOI]."

This is the fastest defensible alternative to PROSPERO pre-registration for a single-author, in-progress review.

---

## 14. Single-Reviewer Audit Check

Independent dual-rating is the strongest mitigation for single-reviewer bias but requires recruiting a second rater. As an interim, lighter mitigation, perform a self-audit on a 10% random sample of retained sources before submission:

1. Generate a 10% random sample of the 17 retained sources (and the 4 cases) using a documented seed (record seed in `analysis/synthesis.md`).
2. Re-extract U-T-I-O domain coding for each sampled source from scratch, blind to original coding (cover the original extraction column).
3. Compare blind re-extraction to the original extraction. Record matches, partial matches, and disagreements in `analysis/audit-check.md`.
4. Report the result in the manuscript Limitations: "A 10% self-audit on retained sources yielded N/N (X%) exact matches on U-T-I-O domain coding; discrepancies are documented in the project repository (`analysis/audit-check.md`)."
5. If a second rater becomes available later, the same sample can be used for an inter-rater reliability statistic (Cohen's kappa or percent agreement).

This does not replace independent dual-rating but does provide a reproducible internal check that is documented and citable.

---

*Last updated: April 29, 2026*
