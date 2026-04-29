# Single-Reviewer Audit Check

**Purpose:** Light mitigation for single-reviewer bias on U-T-I-O domain coding (per `notes/protocol.md` §14). The reviewer (the author) blind-re-codes a randomly sampled subset of retained sources and compares the blind re-coding to the original extraction. Disagreements are documented; the result feeds the manuscript Limitations section.

**Status:** Sample generated; blind re-coding pending.

---

## Sample selection

| Parameter | Value |
|---|---|
| Source population | 17 retained sources from `data/final/evidence_extraction_table.csv` |
| Sample size | 2 (`ceil(0.10 × 17)`) |
| Random seed | `20260429` |
| RNG | Python `random.sample` (seeded) |
| Date generated | April 29, 2026 |

To reproduce the same sample:

```python
import csv, random
with open('data/final/evidence_extraction_table.csv') as f:
    rows = list(csv.DictReader(f))
random.seed(20260429)
sample = random.sample(rows, 2)
for r in sample:
    print(r['Record_ID'], r['Citation_Short'])
```

---

## Sampled sources to blind-re-code

| Sample # | Record ID | Citation | Source category |
|---|---|---|---|
| 1 | **S01** | Holmgren et al. (2023). *Health Information Exchange: Understanding the Policy Landscape and Future of Data Interoperability*. Yearbook of Medical Informatics 32(1):184–194. doi:10.1055/s-0043-1768719 | Policy/framework analysis |
| 2 | **S14** | NIST SP 800-37 Rev. 2 (2018). *Risk Management Framework for Information Systems and Organizations*. NIST. doi:10.6028/NIST.SP.800-37r2 | Policy/framework analysis |

---

## Reviewer protocol

For each sampled source:

1. **Cover the original extraction.** Open `data/final/evidence_extraction_table.csv` and copy the row, or close the file entirely. Do not look at the existing `Domain_U`, `Domain_T`, `Domain_I`, `Domain_O` columns for these two records before re-coding.
2. **Read the source fresh.** Read the abstract + key sections of the paper or report.
3. **Re-code from scratch.** Decide independently whether each of the four U-T-I-O domains is addressed in the source. Mark **Y** (yes, addressed) or blank (not addressed) for each domain. Use the construct definitions in `analysis/utio-scoring-rubric.md` if needed.
4. **Record the blind decision** in the table below.
5. **Reveal the original extraction** for that record.
6. **Compare and tally** matches and disagreements per domain.

---

## Blind re-coding results

Fill in the **Blind** columns first; only after both records are blind-re-coded should the **Original** and **Match?** columns be completed.

### S01 — Holmgren et al. (2023)

| Domain | Blind re-code (Y / blank) | Original (from CSV) | Match? (Y / N) | Notes if disagree |
|---|---|---|---|---|
| U |   |   |   |   |
| T |   |   |   |   |
| I |   |   |   |   |
| O |   |   |   |   |

### S14 — NIST SP 800-37 Rev. 2 (2018)

| Domain | Blind re-code (Y / blank) | Original (from CSV) | Match? (Y / N) | Notes if disagree |
|---|---|---|---|---|
| U |   |   |   |   |
| T |   |   |   |   |
| I |   |   |   |   |
| O |   |   |   |   |

---

## Tally

| Metric | Value |
|---|---|
| Total domain-decisions checked | 8 (2 sources × 4 domains) |
| Exact matches |   /8 |
| Disagreements |   /8 |
| Percent agreement |   % |

---

## Manuscript Limitations text (drop-in)

Once the audit is complete, this sentence (or a variant) goes into `manuscript/sections/limitations.tex` near the existing single-reviewer caveat:

> A 10% self-audit on retained sources (n=2 of 17, seed 20260429) yielded N/8 (X%) exact matches on U-T-I-O domain coding. Discrepancies are documented in `analysis/audit-check.md`.

If percent agreement is high (≥87.5%, i.e. ≥7/8), the audit supports the existing extraction. If lower, the manuscript should disclose the rate plainly and consider re-coding the affected domain across all 17 sources.

---

*Sample generated: April 29, 2026 — Last updated: April 29, 2026*
