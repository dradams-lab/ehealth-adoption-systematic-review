#!/usr/bin/env python3
"""
extraction_to_latex.py — Generate LaTeX rows for the evidence extraction table
from data/final/evidence_extraction_table.csv.

Reads the 24-column extraction CSV and emits LaTeX-formatted rows that
can be pasted into manuscript/tables/evidence_extraction_table.tex
between the \toprule/\bottomrule markers.

Columns rendered (matching the manuscript table): Source (Citation_Short
+ \\cite key inference), Year, Study_Type, Focus, Context, Domains_List,
Key_Finding.

Usage:
    python scripts/extraction_to_latex.py            # print to stdout
    python scripts/extraction_to_latex.py --out FILE # write to file
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "final" / "evidence_extraction_table.csv"

# Map a Citation_Short like "Adams 2020" to a likely BibTeX key like
# "adams2020strategies". Add overrides here if the auto-derived key
# does not match the actual key in references.bib.
KEY_OVERRIDES = {
    "Adams 2020":            "adams2020strategies",
    "Eden et al. 2016":      "eden2016barriers",
    "Kruse et al. 2016":     "kruse2016adoption",
    "Fennelly et al. 2020":  "fennelly2020national",
    "Aguirre et al. 2019":   "aguirre2019ehr",
    "Torab-Miandoab et al. 2023": "torab2023interoperability",
    "Holmgren et al. 2023":  "holmgren2023policyhie",
    "Bossen et al. 2013":    "bossen2013evaluation",
    "DeLone & McLean 2003":  "delone2003model",
}

def latex_escape(s: object) -> str:
    if pd.isna(s):
        return ""
    s = str(s)
    return (s.replace("\\", "\\textbackslash{}")
             .replace("&", "\\&")
             .replace("%", "\\%")
             .replace("#", "\\#")
             .replace("_", "\\_")
             .replace("$", "\\$"))

def derive_key(citation_short: str) -> str:
    if citation_short in KEY_OVERRIDES:
        return KEY_OVERRIDES[citation_short]
    # Best-effort: lower-case last name + year
    m = re.match(r"^([A-Z][a-zA-Z\-']+)\s.*?(\d{4})", citation_short or "")
    if not m:
        return citation_short.lower().replace(" ", "")
    return f"{m.group(1).lower()}{m.group(2)}"

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, help="write to file instead of stdout")
    args = ap.parse_args()

    if not CSV.exists():
        sys.exit(f"Missing {CSV}")
    df = pd.read_csv(CSV, dtype=str).fillna("")

    lines = []
    for i, r in df.iterrows():
        citation = r.get("Citation_Short", "").strip()
        key = derive_key(citation)
        year = r.get("Year", "")
        study_type = latex_escape(r.get("Study_Type", ""))
        focus = latex_escape(r.get("Focus", ""))
        context = latex_escape(r.get("Context", ""))
        domains = latex_escape(r.get("Domains_List", ""))
        finding = latex_escape(r.get("Key_Finding", ""))
        zebra = "\\rowcolor{rowgray}\n" if i % 2 == 0 else ""
        line = (f"{zebra}{latex_escape(citation)}~\\cite{{{key}}} & "
                f"{year} & {study_type} & {focus} & {context} & {domains} & "
                f"{finding} \\\\")
        lines.append(line)
    output = "\n\n".join(lines) + "\n"

    if args.out:
        args.out.write_text(output)
        print(f"Wrote {args.out} ({len(df)} rows)")
    else:
        print(output)
    return 0

if __name__ == "__main__":
    sys.exit(main())
