#!/usr/bin/env python3
"""
Build a blinded human-adjudication sheet from the 126-record worklist.

The unblinded worklist (data/screened/human_adjudication_worklist.csv) shows
the primary screen's decision, the AI second rater's decision, the stratum,
and whether the record is disputed. Seeing those anchors the human rater, so
this script writes a sheet with all of them removed, adds the abstract from
the corpus, and shuffles the row order (fixed seed) so strata are not grouped.

Inputs:
    data/screened/human_adjudication_worklist.csv
    data/screened/corpus_combined.csv
Output:
    data/screened/human_adjudication_blinded.csv  (UTF-8 with BOM, for Excel)

Join the completed sheet back to the worklist on rec_id to unblind.
"""
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKLIST = ROOT / "data/screened/human_adjudication_worklist.csv"
CORPUS = ROOT / "data/screened/corpus_combined.csv"
OUT = ROOT / "data/screened/human_adjudication_blinded.csv"
SEED = 20260929

FIELDS = ["order", "rec_id", "title", "year", "venue", "doctype", "doi_link",
          "abstract", "your_decision", "your_reason_code", "your_notes"]


def main():
    corpus = {r["rec_id"]: r for r in csv.DictReader(open(CORPUS, encoding="utf-8"))}
    rows = list(csv.DictReader(open(WORKLIST, encoding="utf-8")))
    random.Random(SEED).shuffle(rows)

    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for i, r in enumerate(rows, 1):
            c = corpus[r["rec_id"]]
            doi = c["doi"].strip()
            w.writerow({
                "order": i,
                "rec_id": r["rec_id"],
                "title": c["title"],
                "year": c["year"],
                "venue": c["venue"],
                "doctype": c["doctype"],
                "doi_link": f"https://doi.org/{doi}" if doi else "",
                "abstract": c["abstract"].strip() or "[no abstract - screen on title, venue, and document type]",
                "your_decision": "",
                "your_reason_code": "",
                "your_notes": "",
            })
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
