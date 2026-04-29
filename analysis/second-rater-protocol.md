---
name: U-T-I-O case-rating second-rater protocol
description: Independent re-rating protocol for the four-case U-T-I-O domain ratings, with agreement statistics and disagreement adjudication.
---

# Second-Rater Protocol — U-T-I-O Case Ratings

**Purpose:** Mitigate the single-rater limitation on the case-level U-T-I-O ratings (4 cases × 4 domains = 16 ordinal ratings on a four-band scale: H / M / L–M / L). Distinct from `analysis/audit-check.md`, which audits *domain-presence* coding (Y/blank) on the 17-source corpus.

**Scope:** Applies the rubric in `analysis/utio-scoring-rubric.md` to the four cases (U.S. ONC HIE, NHS Shared Care Records, Estonia eHealth, U.S. VA/DoD EHR Modernization). Each case-domain cell is re-rated by a second rater blind to the original ratings, then compared and adjudicated.

---

## 1. Method

### 1.1 Rater independence

The second rater receives:

- The construct-level criteria for U, T, I, and O (the four rubric tables in `analysis/utio-scoring-rubric.md`, §§U–O).
- The case-by-case evidence anchors with citation keys (the per-cell evidence text from §"Application to the four cases"), but **with the original ratings redacted**.
- The bibliography (`manuscript/references.bib`) for source verification.

The second rater does **not** see the original H / M / L–M / L assignments before producing their own.

### 1.2 Rater types reported

This protocol supports two rater types, reported separately:

1. **Human second rater** (preferred; not yet recruited). A credentialed reviewer with health-IT or implementation-science expertise re-rates from the blinded rubric. Status: pending.
2. **AI-assisted second rater** (supplementary; executed). Anthropic Claude Opus 4.7, accessed April 29, 2026. Given the blinded rubric and access to the cited primary sources via web tools. Mirrors the AI-assisted check pattern already used in `analysis/audit-check.md` for the 17-source presence coding. **Does not substitute** for human dual-rating.

### 1.3 Agreement statistics

With N = 16 ordinal cells on a 4-band scale, three statistics are reported jointly because no single statistic is robust at this N:

- **Percent exact agreement** — fraction of cells where second rater matches original exactly (primary, easy to interpret).
- **Percent within-one-band agreement** — fraction where ratings are within one band of each other on the H / M / L–M / L scale (catches "close" disagreements that may reflect rubric-band ambiguity rather than substantive disagreement).
- **Linear-weighted Cohen's κ** — ordinal-aware agreement statistic. Weights: |i−j|/3 where i, j are band indices on a 1–4 scale. Reported with the explicit caveat that **N = 16 yields a high-variance κ point estimate**; we report it for transparency rather than as a robust inferential claim.

Rating bands are coded numerically as L = 1, L–M = 2, M = 3, H = 4 for the κ computation.

### 1.4 Disagreement adjudication

For each disagreement (exact mismatch), the original rater records:

- Which construct(s) within the domain drove the original rating.
- Which construct(s) the second rater appears to have weighted differently.
- Whether the disagreement reflects (a) different evidence interpretation, (b) rubric ambiguity (e.g., the L–M / M boundary is fuzzy), or (c) a defensible rating revision.

If category (c), the original rating is updated in `analysis/utio-scoring-rubric.md` and the change is logged below.

---

## 2. Blinded rubric handed to the second rater

> **Note for second rater:** Use the construct definitions in `analysis/utio-scoring-rubric.md` §§U–O and the rating decision rules. For each case below, read the cited sources and assign one of {H, M, L–M, L} per domain. Do not consult the "Application to the four cases" subsection of the rubric file before completing your ratings.

### Case A — U.S. ONC HIE

Primary sources: `onc2025reports`, `holmgren2023policyhie`, `eden2016barriers`, `kruse2016adoption`.

Context: Federated, market-based HIE infrastructure under HITECH Act incentives and 21st Century Cures Act / TEFCA. Rate U / T / I / O.

### Case B — NHS Shared Care Records (UK)

Primary sources: `nhs2025sharedcare`, `fennelly2020national`.

Context: Centrally coordinated national interoperability program within a single-payer health system. Rate U / T / I / O.

### Case C — Estonia eHealth

Primary sources: `estonia2026ehealth`, `europeancommission2016estoniaehr`, `holmgren2023policyhie`.

Context: Legally mandated national digital health infrastructure on the X-Road exchange platform, operational since 2008. Rate U / T / I / O.

### Case D — U.S. VA/DoD Federal EHR Modernization

Primary sources: `gao2025vaehr`, `gao2024dodehr`.

Context: Large-scale federal EHR replacement (Oracle Health / Cerner; MHS GENESIS) under FY2018 NDAA mandate. Rate U / T / I / O.

### Blank rating sheet

| Case | U | T | I | O |
|---|---|---|---|---|
| A — U.S. ONC HIE |   |   |   |   |
| B — NHS Shared Care Records |   |   |   |   |
| C — Estonia eHealth |   |   |   |   |
| D — VA/DoD EHR |   |   |   |   |

---

## 3. Results

### 3.1 AI-assisted second rater (Anthropic Claude Opus 4.7, 2026-04-29)

The AI rater is given the rubric criteria (§§U–O of `utio-scoring-rubric.md`, lines 1–78 only) and the blinded case definitions in §2 above. **The original ratings are deliberately omitted from this section to preserve blinding** — the rater must not see them while producing its own ratings. Original ratings are merged in for comparison only after the blind pass is complete; the populated comparison is in §3.2.

| Case | Domain | AI second rater | Justification (≤2 sentences) |
|---|---|---|---|
| A — U.S. ONC HIE | U |  |  |
| A — U.S. ONC HIE | T |  |  |
| A — U.S. ONC HIE | I |  |  |
| A — U.S. ONC HIE | O |  |  |
| B — NHS Shared Care | U |  |  |
| B — NHS Shared Care | T |  |  |
| B — NHS Shared Care | I |  |  |
| B — NHS Shared Care | O |  |  |
| C — Estonia | U |  |  |
| C — Estonia | T |  |  |
| C — Estonia | I |  |  |
| C — Estonia | O |  |  |
| D — VA/DoD | U |  |  |
| D — VA/DoD | T |  |  |
| D — VA/DoD | I |  |  |
| D — VA/DoD | O |  |  |

### 3.2 Comparison (post-blind merge with original ratings)

To be filled after §3.1 is complete by merging in the originals from `utio-scoring-rubric.md` §"Application to the four cases".

| Case | Domain | Original | AI second rater | Match (exact) | Within-one-band |
|---|---|---|---|---|---|
| A — U.S. ONC HIE | U |  |  |  |  |
| A — U.S. ONC HIE | T |  |  |  |  |
| A — U.S. ONC HIE | I |  |  |  |  |
| A — U.S. ONC HIE | O |  |  |  |  |
| B — NHS Shared Care | U |  |  |  |  |
| B — NHS Shared Care | T |  |  |  |  |
| B — NHS Shared Care | I |  |  |  |  |
| B — NHS Shared Care | O |  |  |  |  |
| C — Estonia | U |  |  |  |  |
| C — Estonia | T |  |  |  |  |
| C — Estonia | I |  |  |  |  |
| C — Estonia | O |  |  |  |  |
| D — VA/DoD | U |  |  |  |  |
| D — VA/DoD | T |  |  |  |  |
| D — VA/DoD | I |  |  |  |  |
| D — VA/DoD | O |  |  |  |  |

### 3.3 AI-pass tally

| Statistic | Value |
|---|---|
| N | 16 |
| Exact agreement | _/16 (__%) |
| Within-one-band agreement | _/16 (__%) |
| Linear-weighted κ | _.__ |

### 3.4 Human second rater

Status: pending recruitment. Same blinded rubric (§2) and rating sheet apply.

---

## 4. Adjudication log

For each exact mismatch, document construct-level reasoning and disposition (kept original / revised / rubric clarified).

(Filled after §3.1 is complete.)

---

## 5. Manuscript drop-in text

To be finalized once §3 is populated. Drafts:

**Methods (replaces single-rater sentence in `manuscript/sections/methods.tex` §3.2.2):**

> Domain-level ratings (High / Medium / Low–Medium / Low) were assigned via a preponderance-of-evidence rule using a four-construct rubric per domain; complete construct definitions, decision rules, and per-case justification are in the project repository (`analysis/utio-scoring-rubric.md`). To mitigate single-rater bias, an AI-assisted second-rater pass (Anthropic Claude Opus 4.7, April 2026) re-rated the 16 case-domain cells blind to the original assignments; agreement was \_/16 (\_\_%) exact and \_/16 (\_\_%) within one band, with linear-weighted Cohen's κ = \_.\_\_ (N = 16 limits κ precision). Independent dual-rating with a credentialed second rater is an outstanding methodological gap.

**Limitations (replaces ¶4 in `manuscript/sections/limitations.tex`):**

> Fourth, although the U-T-I-O coding framework was applied systematically, ratings were assigned by a single human reviewer. To partially mitigate this, an AI-assisted second-rater pass on the four-case rubric ratings yielded \_/16 (\_\_%) exact agreement and \_/16 (\_\_%) within-one-band agreement (linear-weighted κ = \_.\_\_); a separate 10% self-audit on the 17-source domain-presence coding is documented in `analysis/audit-check.md`. Independent dual-rating with a credentialed second rater remains an outstanding methodological gap.

---

*Created: 2026-04-29 — Last updated: 2026-04-29*
