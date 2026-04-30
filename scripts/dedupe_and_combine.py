#!/usr/bin/env python3
"""
dedupe_and_combine.py — Combine and deduplicate raw database exports.

Reads every CSV/TSV/RIS file in data/raw/, normalizes columns into a
common schema (Title / FirstAuthor / Year / DOI / SourceDB), deduplicates
by exact DOI match (primary) plus title+year+first-author match
(secondary), and writes:

    data/screened/screening_log_combined.csv  (one row per unique record)
    data/screened/duplicates_removed.csv      (audit trail of dropped rows)

Usage:
    python scripts/dedupe_and_combine.py

Expected raw filenames (mapped to source labels via prefix):
    pubmed_*.csv   scopus_*.csv   ieee_*.csv   wos_*.txt|*.tsv|*.csv
    cinahl_*.csv   scholar_*.csv  handsearch_*.csv  expert_recs.csv

Adjust the COLUMN_MAP dict if your export uses different column names.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "data" / "screened"

# Map a raw-export column name (lower-cased) to the canonical schema.
# Add entries here when a new database's export uses different column names.
COLUMN_MAP = {
    "title": "Title", "document title": "Title", "ti": "Title",
    "authors": "Authors", "author full names": "Authors", "au": "Authors",
    "first author": "FirstAuthor",
    "year": "Year", "publication year": "Year", "py": "Year",
    "doi": "DOI", "di": "DOI",
    "journal": "Journal", "source title": "Journal", "publication title": "Journal", "so": "Journal",
}

def _label_from_filename(p: Path) -> str:
    stem = p.stem.lower()
    for prefix in ("pubmed", "scopus", "ieee", "wos", "cinahl", "scholar", "handsearch", "expert_recs"):
        if stem.startswith(prefix):
            return prefix
    return stem

def _read_one(p: Path) -> pd.DataFrame:
    if p.suffix.lower() in {".tsv", ".txt"}:
        df = pd.read_csv(p, sep="\t", dtype=str, on_bad_lines="skip")
    elif p.suffix.lower() == ".ris":
        try:
            import rispy
        except ImportError:
            sys.exit("rispy not installed — run: pip install -r scripts/requirements.txt")
        with p.open(encoding="utf-8") as f:
            entries = rispy.load(f)
        df = pd.DataFrame(entries)
        # Normalize RIS keys
        df = df.rename(columns={"primary_title": "Title", "authors": "Authors",
                                "year": "Year", "doi": "DOI", "journal_name": "Journal"})
    else:
        df = pd.read_csv(p, dtype=str, on_bad_lines="skip")
    df.columns = [COLUMN_MAP.get(c.lower().strip(), c) for c in df.columns]
    df["SourceDB"] = _label_from_filename(p)
    return df

def _norm_title(t: object) -> str:
    if pd.isna(t):
        return ""
    return re.sub(r"[^a-z0-9 ]+", " ", str(t).lower()).strip()

def _first_author(authors: object) -> str:
    if pd.isna(authors):
        return ""
    s = str(authors).split(";")[0].split(",")[0]
    return re.sub(r"[^a-z]", "", s.lower())[:20]

def main() -> int:
    if not RAW_DIR.exists() or not any(RAW_DIR.iterdir()):
        sys.exit(f"No files in {RAW_DIR}. Place raw exports there and re-run.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    frames = []
    for p in sorted(RAW_DIR.iterdir()):
        if p.suffix.lower() not in {".csv", ".tsv", ".txt", ".ris"}:
            continue
        df = _read_one(p)
        # Keep only the canonical columns we know about (plus everything else)
        for col in ("Title", "Authors", "FirstAuthor", "Year", "DOI", "Journal"):
            if col not in df.columns:
                df[col] = ""
        if "FirstAuthor" not in df or df["FirstAuthor"].fillna("").eq("").all():
            df["FirstAuthor"] = df["Authors"].map(_first_author)
        df["_norm_title"] = df["Title"].map(_norm_title)
        frames.append(df)
        print(f"  {p.name:40s} {len(df):5d} rows  ({df['SourceDB'].iloc[0]})")

    combined = pd.concat(frames, ignore_index=True)
    print(f"\nTotal records identified (pre-dedup): {len(combined)}")

    # Dedupe: DOI exact match first, then norm-title + year + first-author
    combined["DOI_clean"] = combined["DOI"].fillna("").str.strip().str.lower()
    combined["_dedup_key"] = combined.apply(
        lambda r: r["DOI_clean"] if r["DOI_clean"]
        else f"{r['_norm_title']}|{r['Year']}|{r['FirstAuthor']}",
        axis=1,
    )

    duplicates_mask = combined.duplicated(subset=["_dedup_key"], keep="first")
    duplicates = combined[duplicates_mask].copy()
    unique = combined[~duplicates_mask].copy()
    print(f"Duplicates removed:                   {len(duplicates)}")
    print(f"Unique records after dedup:           {len(unique)}\n")

    # Build screening log (one row per unique record, screening columns blank)
    log = unique[["Title", "FirstAuthor", "Year", "DOI", "Journal", "SourceDB"]].copy()
    log.insert(0, "Record_ID", [f"R{i:04d}" for i in range(1, len(log) + 1)])
    for col in ("TA_Decision", "TA_Reason", "FullText_Decision", "FullText_Reason", "Notes"):
        log[col] = ""
    log_path = OUT_DIR / "screening_log_combined.csv"
    log.to_csv(log_path, index=False)
    print(f"Wrote: {log_path.relative_to(ROOT)}")

    # Audit trail of duplicates
    dup_path = OUT_DIR / "duplicates_removed.csv"
    duplicates[["Title", "FirstAuthor", "Year", "DOI", "Journal", "SourceDB"]].to_csv(dup_path, index=False)
    print(f"Wrote: {dup_path.relative_to(ROOT)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
