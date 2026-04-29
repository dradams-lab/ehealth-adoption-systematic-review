# eHealth Adoption Systematic Review — Reference Review Started

## Scope
Reviewed current `references/library.bib` and evidence-extraction alignment. The repo contains 22 bibliography records; 17 are mapped in the evidence extraction table as retained evidence sources/cases.

## Immediate Findings
1. Most core systematic-review and government/audit sources are openly accessible.
2. Direct article downloading from this runtime failed because external DNS resolution is blocked in the shell environment.
3. A legal-access manifest has been created with official article/report pages and full-text status.
4. Several citations need cleanup before submission:
   - `onc2025reports` uses key/year language that conflicts with the BibTeX note saying the most recent listed report was 2023.
   - `holmgren2023policyhie` should add DOI `10.1055/s-0043-1768719` and PMC link.
   - `aguirre2019ehr` should verify the final Cureus article URL/PDF path.
   - `estonia2026ehealth` should be cited as an accessed web page with no publication date unless a stable dated source is found.

## Download / Access Status
See `reference_review_manifest.csv`.

## Recommended Next Step
Populate `/data/raw/` with formal RIS/CSV database exports, then archive legally available PDFs in a dedicated `/references/fulltext/` or external Zotero storage folder. Avoid committing copyrighted PDFs directly to GitHub unless license permits redistribution.
