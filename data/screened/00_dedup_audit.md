# Corpus Build & Deduplication Audit

**Date:** 2026-07-01
**Inputs (raw database exports, executed 2026-06-04):**
- PubMed/MEDLINE: `data/searches/pubmed_results.nbib` — 1,591 records
- IEEE Xplore: `data/searches/ieee_results.csv` — 97 records
- Total identified (pre-deduplication): **1,688**

**Databases NOT searched** (institutional subscription access unavailable, per S1 §4): Scopus, Web of Science, CINAHL. Google Scholar run as a supplementary recall check returned 0 unique in-window records.

## Deduplication method
Exact match on normalized DOI, then exact match on normalized title (case-folded, ASCII-transliterated, punctuation-stripped). Cross-database ties resolved by keeping the PubMed record. This is a conservative exact-match protocol; near-duplicate detection at a fuzzy-similarity threshold was not used.

- Duplicate pairs identified & removed: **8** (all within-PubMed title duplicates)
- **Unique records for title/abstract screening: 1,680** (PubMed 1,583; IEEE 97)

## Data completeness
- Records missing an abstract: 94 (all PubMed; ~6%; the raw pre-dedup export had 97, of which 3 were removed as duplicates). These are screened on title + metadata only, flagged in the screening log.

## Outputs
- `data/screened/corpus_combined.csv` — 1,680 unique records (rec_id R0001–R1680)
- `data/screened/corpus_with_dupflags.csv` — all 1,688 with duplicate-audit flags

*Note:* This exact-match count (8 removed) differs from the earlier S1 draft figure (22 removed via Rayyan fuzzy matching at 97% similarity). The figure reported in the manuscript will be regenerated from this documented method.
