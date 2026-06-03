#!/usr/bin/env python3
"""Convert the PubMed MEDLINE (.nbib) and IEEE CSV search exports to RIS,
which Rayyan imports reliably. Writes two .ris files into data/searches/."""
import csv
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data" / "searches"


def medline_to_ris(src: Path, dst: Path) -> int:
    """Parse PubMed MEDLINE format into RIS. Returns record count."""
    text = src.read_text(encoding="utf-8", errors="replace")
    # Records are separated by blank lines; fold continuation lines (indented).
    records = re.split(r"\n\s*\n", text.strip())
    out = []
    n = 0
    for rec in records:
        if "PMID-" not in rec:
            continue
        # Fold continuation lines (lines starting with whitespace) into prior tag.
        lines = rec.split("\n")
        folded = []
        for ln in lines:
            if re.match(r"^\s{4,}\S", ln) and folded:
                folded[-1] += " " + ln.strip()
            else:
                folded.append(ln.rstrip())
        fields = {}
        for ln in folded:
            m = re.match(r"^([A-Z]{2,4})\s*-\s*(.*)$", ln)
            if not m:
                continue
            tag, val = m.group(1), m.group(2).strip()
            fields.setdefault(tag, []).append(val)
        title = " ".join(fields.get("TI", []))
        abstract = " ".join(fields.get("AB", []))
        authors = fields.get("AU", [])
        journal = (fields.get("JT") or fields.get("TA") or [""])[0]
        year = ""
        if fields.get("DP"):
            ym = re.match(r"(\d{4})", fields["DP"][0])
            year = ym.group(1) if ym else ""
        doi = ""
        for cand in fields.get("LID", []) + fields.get("AID", []):
            if "[doi]" in cand:
                doi = cand.replace("[doi]", "").strip()
                break
        vol = (fields.get("VI") or [""])[0]
        issue = (fields.get("IP") or [""])[0]
        pages = (fields.get("PG") or [""])[0]
        pmid = (fields.get("PMID") or [""])[0]

        r = ["TY  - JOUR"]
        if title:
            r.append(f"TI  - {title}")
        for a in authors:
            r.append(f"AU  - {a}")
        if year:
            r.append(f"PY  - {year}")
        if journal:
            r.append(f"T2  - {journal}")
        if vol:
            r.append(f"VL  - {vol}")
        if issue:
            r.append(f"IS  - {issue}")
        if pages:
            r.append(f"SP  - {pages}")
        if abstract:
            r.append(f"AB  - {abstract}")
        if doi:
            r.append(f"DO  - {doi}")
        if pmid:
            r.append(f"AN  - {pmid}")
            r.append(f"UR  - https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
        r.append("ER  - ")
        out.append("\n".join(r))
        n += 1
    dst.write_text("\n\n".join(out) + "\n", encoding="utf-8")
    return n


def ieee_csv_to_ris(src: Path, dst: Path) -> int:
    """Convert IEEE Xplore CSV export into RIS. Returns record count."""
    out = []
    n = 0
    with src.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = (row.get("Document Title") or "").strip()
            if not title:
                continue
            authors = [a.strip() for a in (row.get("Authors") or "").split(";") if a.strip()]
            journal = (row.get("Publication Title") or "").strip()
            year = (row.get("Publication Year") or "").strip()
            abstract = (row.get("Abstract") or "").strip()
            doi = (row.get("DOI") or "").strip()
            sp = (row.get("Start Page") or "").strip()
            ep = (row.get("End Page") or "").strip()
            # IEEE conference proceedings vs journals: default CONF is safest for IEEE.
            ty = "CONF" if "conf" in journal.lower() or "proceedings" in journal.lower() or "symposium" in journal.lower() else "JOUR"
            r = [f"TY  - {ty}"]
            r.append(f"TI  - {title}")
            for a in authors:
                r.append(f"AU  - {a}")
            if year:
                r.append(f"PY  - {year}")
            if journal:
                r.append(f"T2  - {journal}")
            if sp:
                r.append(f"SP  - {sp}")
            if ep:
                r.append(f"EP  - {ep}")
            if abstract:
                r.append(f"AB  - {abstract}")
            if doi:
                r.append(f"DO  - {doi}")
            r.append("ER  - ")
            out.append("\n".join(r))
            n += 1
    dst.write_text("\n\n".join(out) + "\n", encoding="utf-8")
    return n


if __name__ == "__main__":
    pm = medline_to_ris(BASE / "pubmed_results.nbib", BASE / "pubmed_results.ris")
    ie = ieee_csv_to_ris(BASE / "ieee_results.csv", BASE / "ieee_results.ris")
    print(f"PubMed -> RIS: {pm} records")
    print(f"IEEE   -> RIS: {ie} records")
