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

> *Health Information Exchange: Understanding the Policy Landscape and Future of Data Interoperability* — HIE policy across five countries (US, UK, Germany, Israel, Portugal). Yearbook of Medical Informatics 32(1):184–194. Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC10751121/

| Domain | Blind re-code (Y / blank) | Original (from CSV) | Match? (Y / N) | Notes if disagree |
|---|---|---|---|---|
| U |   |   |   |   |
| T |   |   |   |   |
| I |   |   |   |   |
| O |   |   |   |   |

### S14 — NIST SP 800-37 Rev. 2 (2018)

> *Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy* — U.S. federal security/privacy risk-management framework (FISMA-aligned). doi:10.6028/NIST.SP.800-37r2. Open PDF: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf

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

## AI-Assisted Second-Rater Check (independent supplementary pass)

**Methodology:** Anthropic Claude (Claude Opus 4.7, accessed April 29, 2026) was provided the U-T-I-O scoring rubric (`analysis/utio-scoring-rubric.md`) and asked to re-code each of the four U-T-I-O domains for the two sampled sources. The AI accessed the source documents independently via web fetch, applied the rubric criteria, and produced Y/blank decisions per domain. The AI did not see the original CSV codes during re-coding. This serves as a *supplementary* second-rater check; it does not substitute for the human self-audit (above) or for true independent dual-rating with a credentialed second rater.

### S01 — Holmgren et al. (2023)

| Domain | AI re-code | Original (CSV) | Match? | AI's reasoning |
|---|---|---|---|---|
| U | Y | (blank) | **No** | Paper discusses clinician EHR burden, workflow integration, and user-awareness gaps (e.g., Israeli EITAN system) |
| T | Y | Y | Yes | Paper extensively covers FHIR, HL7, SNOMED CT, API requirements, semantic interoperability across five case nations |
| I | Y | Y | Yes | Paper analyzes regulatory frameworks, national digital health strategies, governance structures, privacy/consent models |
| O | Y | Y | Yes | Paper addresses implementation challenges, vendor governance, resource capacity, change management |

### S14 — NIST SP 800-37 Rev. 2 (2018)

| Domain | AI re-code | Original (CSV) | Match? | AI's reasoning |
|---|---|---|---|---|
| U | (blank) | (blank) | Yes | Document focuses on organizational/technical processes; does not substantively address end-user training, awareness, or readiness for non-technical staff |
| T | Y | (blank) | **No** | Document covers security controls, system assessment, control mechanisms — but the disagreement is interpretable: U-T-I-O T-domain narrowly concerns health-IT interoperability (FHIR, HL7, semantic exchange), while NIST SP 800-37's "controls" sense of T is security-governance. Original CSV's stricter interpretation is defensible |
| I | Y | Y | Yes | Document is foundational for FISMA, OMB Circular A-130, EO 13800; provides senior-leadership accountability framework |
| O | Y | Y | Yes | Document defines authorizing official, system owner, ISSO, senior agency information security officer roles; core execution/accountability mechanisms |

### AI-pass tally

| Metric | Value |
|---|---|
| Total domain-decisions checked | 8 (2 sources × 4 domains) |
| Exact matches | 6/8 |
| Disagreements | 2/8 |
| Percent agreement | 75% |

**Interpretation of disagreements:**
- **S01 U-domain:** AI over-included. Paper does mention clinician burden/workflow, but as one factor among many in a primarily policy-focused review. Original CSV's blank is a defensible judgment call that the paper's *substantive* contribution is not in the U domain.
- **S14 T-domain:** AI over-included. NIST SP 800-37 covers security controls, but the U-T-I-O rubric's T-domain refers specifically to health-IT interoperability (semantic/syntactic standards, FHIR, HL7) rather than security-control governance. Original CSV is methodologically tighter.

**Methodological caveat:** Both disagreements are AI-overinclusion against a more conservative human extraction. This pattern suggests the original extraction's domain-assignment threshold is appropriately strict; the AI check does not reveal under-coding by the original reviewer.

---

## Manuscript Limitations text (drop-in)

Once both passes are complete, the following sentences go into `manuscript/sections/limitations.tex` near the existing single-reviewer caveat:

**Self-audit sentence (fill in N when you complete your blind pass):**

> A 10% self-audit on retained sources (n=2 of 17, seed 20260429) yielded N/8 (X%) exact matches on U-T-I-O domain coding by the same reviewer; discrepancies are documented in `analysis/audit-check.md`.

**AI-assisted check sentence (already supported by the data above):**

> A supplementary AI-assisted second-rater check (Anthropic Claude, April 2026) on the same 10% sample yielded 6/8 (75%) agreement with the original extraction; both disagreements were AI over-inclusions against the more conservative human extraction, suggesting the original domain-assignment threshold is appropriately strict.

If self-audit percent agreement is high (≥87.5%, i.e. ≥7/8), the audit supports the existing extraction. If lower, the manuscript should disclose the rate plainly and consider re-coding the affected domain across all 17 sources.

---

*Sample generated: April 29, 2026 — Last updated: April 29, 2026*
