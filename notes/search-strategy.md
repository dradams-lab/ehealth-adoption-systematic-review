# Search Strategy Documentation
**Study:** Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis
**Date Documented:** April 29, 2026
**Status:** Seed set established (424 records identified, 17 retained); formal database execution pending

---

## Sources Searched

| Source | Type | Platform | Date Range | Date Searched |
|---|---|---|---|---|
| PubMed / MEDLINE | Primary database | NLM | 2015-01-01 onwards | Seed set; formal TBD |
| IEEE Xplore | Primary database | IEEE | 2015 onwards | Seed set; formal TBD |
| Scopus | Primary database | Elsevier | 2015 onwards | Seed set; formal TBD |
| Web of Science | Supplementary database | Clarivate | 2015 onwards | Seed set; formal TBD |
| CINAHL | Supplementary database | EBSCO | 2015 onwards | Seed set; formal TBD |
| Google Scholar | Supplementary | Google | 2015 onwards | Seed set; first 5 pages by relevance |
| Hand-search of reference lists | Supplementary | — | 2015 onwards | Seed set; ongoing |
| Expert recommendations | Supplementary | — | — | Seed set; sources from domain advisors |

The three primary databases capture interdisciplinary literature spanning biomedical informatics, computer science, and health policy. The five supplementary sources broaden coverage into nursing/allied health (CINAHL), high-impact cross-disciplinary outlets (Web of Science), grey literature (Google Scholar, hand-search), and expert-curated material (expert recommendations).

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

**Filters:** Publication type = Journal Article; Language = English
**Seed-set yield:** 142 records

---

### IEEE Xplore

```
("Full Text & Metadata": "electronic health record" OR "EHR" OR "electronic medical record"
OR "health information exchange" OR "HIE" OR "eHealth" OR "e-health"
OR "digital health" OR "health information technology" OR "interoperability")
AND
("Full Text & Metadata": "adoption" OR "implementation" OR "acceptance"
OR "barriers" OR "facilitators" OR "determinants" OR "success factors" OR "uptake")
AND (Publication Year: 2015 onwards)
```

**Filter:** Journals and Conference Papers only
**Seed-set yield:** 28 records

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
**Seed-set yield:** 97 records

---

### Web of Science (supplementary)

```
TS=("electronic health record" OR "EHR" OR "health information exchange"
OR "eHealth" OR "digital health" OR "interoperability")
AND TS=("adoption" OR "implementation" OR "barrier*" OR "facilitator*" OR "determinant*")
```

**Filters:** Core Collection; 2015 onwards; English; Article or Review
**Seed-set yield:** 84 records

---

### CINAHL (supplementary)

```
(MH "Medical Informatics" OR TI eHealth OR TI "EHR" OR TI "electronic health record")
AND (TI adoption OR TI implementation OR TI barrier OR TI facilitator OR TI determinant)
```

**Filters:** 2015 onwards; English; Peer Reviewed
**Seed-set yield:** 31 records

---

### Google Scholar (supplementary)

```
"eHealth adoption" OR "EHR implementation barriers"
OR "health information exchange determinants" OR "digital health adoption framework"
```

**Approach:** First 5 pages by relevance; manually de-duplicated against primary databases
**Seed-set yield:** 24 records

---

### Hand-search and expert recommendations (supplementary)

- Hand-search of reference lists from retained full-text sources
- Citations recommended by domain advisors and experts
- **Seed-set yield:** 12 (hand-search) + 6 (expert recommendations) = 18 records

---

## Inclusion / Exclusion Criteria

### Inclusion
- Peer-reviewed journal articles, systematic reviews, scoping reviews, umbrella reviews
- Government / institutional reports with empirical basis
- Focus on eHealth, EHR, EMR, HIE, health information technology, or clinical interoperability
- Addresses adoption, implementation, barriers, facilitators, or determinants
- Published January 2015 onwards
- English language

### Exclusion
- Opinion editorials, letters, conference abstracts without full methodology
- Non-healthcare IT systems without healthcare application
- Studies involving primary collection of identifiable human subject data
- Published before January 2015 (except foundational theory papers retained as background)
- Non-English publications

---

## Current PRISMA Flow Counts (Seed Set)

| Stage | Count | Notes |
|---|---|---|
| PubMed / MEDLINE | 142 | MeSH + keyword |
| IEEE Xplore | 28 | Full-text search |
| Scopus | 97 | TITLE-ABS-KEY |
| Web of Science | 84 | Core Collection |
| CINAHL | 31 | Peer Reviewed filter |
| Google Scholar | 24 | First 5 pages |
| Hand-search | 12 | Reference-list mining |
| Expert recommendations | 6 | Domain advisor input |
| **Total identified** | **424** | Pre-deduplication |
| Duplicates removed | 30 | Estimated overlap PubMed/Scopus/WoS |
| After deduplication | 394 | Unique records |
| Excluded (T/A) | 351 | Off-topic, language, editorial |
| Sought for full-text | 43 | T/A inconclusive or promising |
| Not retrievable | 2 | After library and ILL requests |
| Full-text assessed | 41 | |
| Excluded (full-text) | 24 | See Supplementary File S2 for reasons |
| **Included in synthesis** | **17** | 6 systematic/umbrella + 4 scoping/narrative + 4 government/audit + 3 policy/framework |
| Public cases | 4 | ONC, NHS, Estonia, VA/DoD (purposive) |

> **Note:** These counts reflect the current seed-set state documented in `prisma/prisma-counts.xlsx`. Final counts will be refreshed following formal database-search execution and full deduplication via Zotero/Rayyan.

---

## Deduplication Protocol (Planned)

1. Export all database results to Zotero in RIS format
2. Use Zotero's duplicate detection + manual review for near-duplicates
3. Export deduplicated library to CSV for screening log (`data/screened/screening_log_combined.csv`)
4. Document removed duplicates with source database noted (`data/screened/duplicates_removed.csv`)

---

## Screening Log

See: `prisma/prisma-counts.xlsx` → "Full Screening Log (template)" tab.
A populated CSV will be placed at `data/screened/screening_log_combined.csv` after formal search execution.

---

## Quality Assessment Notes

The study uses a thematic synthesis approach rather than formal risk-of-bias scoring, appropriate given the heterogeneous study designs included (systematic reviews, empirical studies, government reports). Source credibility was assessed based on:
- Peer review status and journal/publisher reputation
- Government/institutional authority of grey literature sources
- Methodological transparency of included reviews

---

*Last updated: April 29, 2026*
