# scripts/ — Reproducibility utilities

Four Python utilities that automate the data-handling pipeline once you run the formal database searches. All four read from / write to existing repo paths; nothing else needs configuration.

## Setup (one time)

```bash
cd /Users/dradams/Documents/Research/ehealth-adoption-systematic-review
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

## The pipeline

Run these in order after each formal-search refresh:

### 1. `dedupe_and_combine.py` — combine raw exports, dedupe

**Input:** `data/raw/*.csv`, `*.tsv`, `*.txt`, `*.ris`
Drop your PubMed / Scopus / IEEE / WoS / CINAHL / Scholar / hand-search / expert-recs exports here. Filename prefixes (e.g., `pubmed_*.csv`) drive the source label.

**Output:**
- `data/screened/screening_log_combined.csv` — one row per unique record, with empty `TA_Decision` and `FullText_Decision` columns ready for screening
- `data/screened/duplicates_removed.csv` — audit trail of what was dropped

```bash
python scripts/dedupe_and_combine.py
```

### 2. (manually screen) — fill in screening decisions

Open `data/screened/screening_log_combined.csv` in Excel / Numbers / Rayyan / Covidence and populate the decision columns:
- `TA_Decision` = `Include` | `Exclude` (title/abstract pass)
- `TA_Reason` = exclusion reason if Exclude
- `FullText_Decision` = `Include` | `Exclude` | `Not retrievable`
- `FullText_Reason` = exclusion reason if Exclude
- `Notes` = anything else

### 3. `update_prisma_counts.py` — recompute PRISMA stage counts

Reads the screening log + duplicates audit, recomputes counts at every PRISMA 2020 stage, and writes them back into `prisma/prisma-counts.xlsx` ("PRISMA Flow Counts" sheet).

```bash
python scripts/update_prisma_counts.py
```

### 4. `render_prisma_counts.py` — produce LaTeX-friendly snippets

Prints two blocks:
- Figure 1 (TikZ) values in `$n = N$` form, ready to paste into `manuscript/figures/prisma_tikz.tex`
- Table 2 Count column values, ready to paste into `manuscript/sections/prisma_flow.tex`

```bash
python scripts/render_prisma_counts.py
```

(After pasting, review and remove the "seed-set estimates pending" footnotes from Figure 1 + Table 2 since the values are now real.)

### Bonus: `extraction_to_latex.py` — regenerate the extraction-table rows

Reads `data/final/evidence_extraction_table.csv` (24 columns) and emits LaTeX rows for `manuscript/tables/evidence_extraction_table.tex`. Useful when you add or revise retained sources.

```bash
python scripts/extraction_to_latex.py                                # print to stdout
python scripts/extraction_to_latex.py --out /tmp/rows.tex            # save to file
```

`KEY_OVERRIDES` at the top of the script maps Citation_Short values to the actual BibTeX keys — extend it when adding new entries.

## End-to-end flow after a formal search

1. Drop database exports in `data/raw/`.
2. `python scripts/dedupe_and_combine.py` — produces the screening log.
3. Screen the log manually (or in Rayyan / Covidence).
4. `python scripts/update_prisma_counts.py` — refreshes the xlsx.
5. `python scripts/render_prisma_counts.py` — gives you the LaTeX values.
6. Paste those values into `manuscript/figures/prisma_tikz.tex` (Figure 1) and `manuscript/sections/prisma_flow.tex` (Table 2). Remove the "seed set" footnote text in both files.
7. (If retained sources changed) re-run `extraction_to_latex.py` and update `manuscript/tables/evidence_extraction_table.tex`.
8. Commit and push; Overleaf will rebuild the PDF.
