# Search Strategy Documentation
**Study:** Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis  
**Date Documented:** April 29, 2026  
**Status:** Planned / Protocol (database exports pending)

---

## Databases Searched

| Database | Platform | Date Range | Date Searched |
|---|---|---|---|
| PubMed / MEDLINE | NLM | 2015-01-01 to 2026-12-31 | TBD |
| IEEE Xplore | IEEE | 2015 to 2026 | TBD |
| Scopus | Elsevier | 2015 to 2026 | TBD |

---

## Search Queries

### PubMed / MEDLINE

```
("electronic health record"[MeSH Terms] OR "medical records systems, computerized"[MeSH Terms]
OR "health information exchange"[MeSH Terms] OR "EHR"[Title/Abstract]
OR "electronic medical record*"[Title/Abstract] OR "health information exchange"[Title/Abstract]
OR "HIE"[Title/Abstract] OR "eHealth"[Title/Abstract] OR "e-health"[Title/Abstract]
OR "digital health"[Title/Abstract] OR "health information technology"[Title/Abstract]
OR "interoperability"[Title/Abstract])
AND
("adoption"[Title/Abstract] OR "implementation"[Title/Abstract] OR "acceptance"[Title/Abstract]
OR "barrier*"[Title/Abstract] OR "facilitator*"[Title/Abstract] OR "determinant*"[Title/Abstract]
OR "success factor*"[Title/Abstract] OR "critical success factor*"[Title/Abstract]
OR "uptake"[Title/Abstract])
AND ("2015/01/01"[PDAT] : "2026/12/31"[PDAT])
```

**Additional PubMed filters:** Publication type = Journal Article; Language = English  
**Expected yield:** ~1,500–3,500 records

---

### IEEE Xplore

```
("Full Text & Metadata": "electronic health record" OR "EHR" OR "electronic medical record"
OR "health information exchange" OR "HIE" OR "eHealth" OR "e-health"
OR "digital health" OR "health information technology" OR "interoperability")
AND
("Full Text & Metadata": "adoption" OR "implementation" OR "acceptance"
OR "barriers" OR "facilitators" OR "determinants" OR "success factors" OR "uptake")
AND (Publication Year: 2015 to 2026)
```

**Additional IEEE filter:** Journals and Conference Papers only  
**Expected yield:** ~300–800 records

---

### Scopus

```
TITLE-ABS-KEY ( "electronic health record" OR "EHR" OR "electronic medical record"
OR "health information exchange" OR "HIE" OR "eHealth" OR "e-health"
OR "digital health" OR "health information technology" OR "interoperability" )
AND TITLE-ABS-KEY ( "adoption" OR "implementation" OR "acceptance"
OR "barriers" OR "facilitators" OR "determinants" OR "success factors" OR "uptake" )
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND DOCTYPE ( ar OR re )
AND LANGUAGE ( english )
```

**Document types:** ar = Article, re = Review  
**Expected yield:** ~1,200–2,500 records

---

## Inclusion / Exclusion Criteria

### Inclusion
- Peer-reviewed journal articles, systematic reviews, scoping reviews, umbrella reviews
- Government / institutional reports with empirical basis
- Focus on eHealth, EHR, EMR, HIE, health information technology, or clinical interoperability
- Addresses adoption, implementation, barriers, facilitators, or determinants
- Published January 2015 – December 2026
- English language

### Exclusion
- Opinion editorials, letters, conference abstracts without full methodology
- Non-healthcare IT systems without healthcare application
- Studies involving primary collection of identifiable human subject data
- Published before January 2015 (except foundational theory papers retained as background)
- Non-English publications

---

## Projected PRISMA Flow Counts

| Stage | Projected Count | Notes |
|---|---|---|
| PubMed records | ~2,000 | MeSH + keyword |
| IEEE Xplore records | ~500 | Full-text search |
| Scopus records | ~1,800 | TITLE-ABS-KEY |
| **Total identified** | **~4,300** | Before deduplication |
| After deduplication | ~2,800 | ~35% duplication rate typical |
| T/A screening | ~2,800 | |
| Excluded (T/A) | ~2,450 | Not adoption, not eHealth, opinion-only |
| Full-text retrieved | ~350 | |
| Excluded (full-text) | ~220 | Technical-only, duplicates, out-of-scope |
| **Included in synthesis** | **~130** | Literature sources + case docs |
| Case studies | 4 | ONC, NHS, Estonia, VA/DoD (purposive) |

> **Note:** These counts are projected based on typical systematic review yields in health informatics.
> Final counts will be updated following formal database export and deduplication.

---

## Deduplication Protocol (Planned)

1. Export all database results to Zotero in RIS format
2. Use Zotero's duplicate detection + manual review for near-duplicates
3. Export deduplicated library to CSV for screening log
4. Document removed duplicates with source database noted

---

## Screening Log

See: `notes/screening-log.md` (to be populated following database exports)

---

## Quality Assessment Notes

The study uses a thematic synthesis approach rather than formal risk-of-bias scoring, appropriate given the heterogeneous study designs included (systematic reviews, empirical studies, government reports). Source credibility was assessed based on:
- Peer review status and journal/publisher reputation
- Government/institutional authority of grey literature sources
- Methodological transparency of included reviews

---

*Last updated: April 29, 2026*
