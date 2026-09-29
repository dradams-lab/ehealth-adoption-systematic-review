# Reproducibility Bundle — Determinants of eHealth Systems Adoption (U-T-I-O Model)

This bundle accompanies the manuscript *Determinants of eHealth Systems
Adoption: A Systematic Review and Multi-Case Analysis* and contains the
machine-readable record of the search, screening, extraction, and scoring, plus
the analysis scripts. The archive is a snapshot of the project's GitHub
repository; paths below are relative to the root of the archive.

## The funnel (all counts reproducible from the files here)
1,688 identified (PubMed/MEDLINE 1,591 + IEEE Xplore 97)
→ 8 duplicates removed → 1,680 screened (two documented stages)
→ 549 assessed → 48 excluded at full text → **501 included studies** + 4 national cases.

Scopus, Web of Science, and CINAHL could not be searched (institutional access
unavailable); planned strings for them are in the manuscript's Supplementary
File S1.

## Contents

### Search, screening, and evidence data
- `data/searches/` — raw PubMed and IEEE Xplore exports.
- `data/screened/corpus_combined.csv` — unified, deduplicated corpus (1,680 records).
- `data/screened/screening_log_combined.csv` — **complete 1,680-record decision log**:
  two-stage title/abstract screen with reason codes and one-line justifications
  per record. Reason codes (E1–E6, X1–X5) are defined in `analysis/screening_rubric.md`.
- `data/final/included_studies_evidence.csv` — 501 included studies with U-T-I-O
  domain coding, study type, evidence basis (full text vs abstract), and
  extracted determinants/findings.
- `data/final/fulltext_exclusions.csv` — 48 full-text exclusions with coded reasons.
- `data/final/utio_alignment_index.csv` — UAI scores for the national cases
  (domain scores, equal- and evidence-weighted indices).
- `data/final/prisma_counts_final.json` — canonical PRISMA counts.
- `data/screened/00_dedup_audit.md` — deduplication method and audit.

### Screening reliability check (AI second rater; human adjudication pending)
- `data/screened/human_verification_worklist.csv` — the 449-record stratified
  verification sample (seed-reproducible).
- `data/screened/two_rater_comparison.csv` — the primary LLM screen compared with
  an **AI second rater (Anthropic Claude)** on that sample: 80% agreement,
  Cohen's κ = 0.61 (n = 447; 2 records received no rating). **Both raters are
  AI; no human rater was involved.**
- `data/screened/human_adjudication_worklist.csv` — 126-record human-adjudication
  worklist (88 disputed records, 36 concordance spot-checks, 2 unrated records).
  The adjudicator columns are blank: human adjudication had not been performed
  at the time of this release.
- `data/screened/three_way_comparison.csv`, `gemini_ratings.csv`,
  `cross_rater_stats.txt`, `final_human_worklist.csv` — an attempted third AI
  rater (Google Gemini) that stopped on API quota after rating 10 of 449
  records. Kept for transparency; not used in any reported statistic.

### scripts/
Python scripts for deduplication (`dedupe_and_combine.py`), PRISMA-count
rendering (`render_prisma_counts.py`, `update_prisma_counts.py`), the
seed-reproducible verification sample draw (`build_verification_sample.py`),
LaTeX table generation (`extraction_to_latex.py`), RIS export (`to_ris.py`), and
the Gemini third-rater attempt (`gemini_cross_rater.py`).

### Documentation
- `analysis/screening_rubric.md` — the inclusion/exclusion rules and reason codes.
- `analysis/human_verification_plan.md` — the stratified sampling and adjudication design.
- `manuscript/` — LaTeX source, including Supplementary Files S1–S4.

## Provenance & AI-assistance note
Title/abstract screening, full-text eligibility assessment, and evidence
extraction were performed by a large language model applying the
human-authored eligibility rules in `analysis/screening_rubric.md`; the
Stage-2 scope codes (X1–X5) were introduced at Stage 2. The screening
reliability check compares two AI raters (`two_rater_comparison.csv`); no human
rater was involved. Human adjudication of the disputed records is pending, and
`human_adjudication_worklist.csv` is provided for that step. See the
manuscript Methods and Supplementary Files S1–S4 for full detail.

## License
Data and documentation: CC-BY-4.0. Scripts: MIT. Please cite the manuscript
(DOI to be added on publication) and this deposit.
