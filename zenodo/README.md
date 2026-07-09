# Reproducibility Bundle — Determinants of eHealth Systems Adoption (U-T-I-O Model)

This bundle accompanies the manuscript *Determinants of eHealth Systems
Adoption: A Systematic Review and Multi-Case Analysis* and contains the
machine-readable record of the search, screening, extraction, and scoring, plus
the analysis scripts.

## The funnel (all counts reproducible from the files here)
1,688 identified (PubMed/MEDLINE 1,591 + IEEE Xplore 97)
→ 8 duplicates removed → 1,680 screened (two documented stages)
→ 549 assessed → 48 excluded at full text → **501 included studies** + 4 national cases.

Scopus, Web of Science, and CINAHL could not be searched (institutional access
unavailable); planned strings for them are in the manuscript's Supplementary
File S1.

## Contents

### data/
- `corpus_combined.csv` — unified, deduplicated corpus (1,680 records).
- `screening_log_combined.csv` — **complete 1,680-record decision log**: two-stage
  title/abstract screen with reason codes and one-line justifications per record.
- `included_studies_evidence.csv` — 501 included studies with U-T-I-O domain
  coding, study type, evidence basis (full text vs abstract), and extracted
  determinants/findings.
- `fulltext_exclusions.csv` — 48 full-text exclusions with coded reasons.
- `two_rater_comparison.csv` — independent second-rater vs first screen over the
  stratified verification sample (Cohen's κ = 0.61).
- `human_adjudication_worklist.csv` — 126-record human-adjudication worklist
  (discordant records + concordance spot-check) with blank adjudicator columns.
- `human_verification_worklist.csv` — the full 449-record stratified sample.
- `utio_alignment_index.csv` — UAI scores for the national cases (domain scores,
  equal- and evidence-weighted indices).
- `prisma_counts_final.json` — canonical PRISMA counts.
- `00_dedup_audit.md` — deduplication method and audit.

### scripts/
Python scripts for deduplication (`dedupe_and_combine.py`), PRISMA-count
rendering (`render_prisma_counts.py`, `update_prisma_counts.py`), the
seed-reproducible verification sample draw (`build_verification_sample.py`),
LaTeX table generation (`extraction_to_latex.py`), and RIS export (`to_ris.py`).

### docs/
- `screening_rubric.md` — the a priori inclusion/exclusion rules.
- `human_verification_plan.md` — the stratified sampling and adjudication design.

## Provenance & AI-assistance note
Title/abstract screening and evidence extraction were AI-assisted under the
explicit, human-authored eligibility rules in `docs/screening_rubric.md`. A
two-rater reliability check is included (`two_rater_comparison.csv`). See the
manuscript Methods and Supplementary Files S1–S4 for full detail. The
`human_adjudication_worklist.csv` is provided for the human validation step.

## License
Data and documentation: CC-BY-4.0. Scripts: MIT. Please cite the manuscript
(DOI to be added on publication) and this deposit.
