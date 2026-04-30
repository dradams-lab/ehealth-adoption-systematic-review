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

### 3.1 AI-assisted second rater (Anthropic Claude Opus 4.7, 2026-04-30)

The AI rater was given the rubric criteria (§§U–O of `utio-scoring-rubric.md`, lines 1–78 only) and the blinded case definitions in §2 above. The rater operated in a fresh agent context with no exposure to the original ratings. The rater self-confirmed compliance with the read-range constraints (rubric lines 1–78 + 121–129; protocol §§1–2 only).

**Audit-trail note.** A first AI pass was discarded after the rater reported it had inadvertently encountered original ratings in §3 of an earlier draft of this protocol file. §3 was redacted of originals, and a fresh rater was invoked. The ratings below are the clean pass; the discarded pass is not retained.

| Case | Domain | AI second rater | Justification (≤2 sentences, constructs from rubric) |
|---|---|---|---|
| A — U.S. ONC HIE | U | L–M | Usability and Workflow integration mixed across the federated HIE landscape with documented clinician burden in `eden2016barriers` and `kruse2016adoption`; Patient engagement via portals exists but adoption is variable and Training adequacy varies widely across participating organizations. |
| A — U.S. ONC HIE | T | M | Syntactic interoperability advancing under FHIR/USCDI and the API/exchange layer is federated (TEFCA QHINs, eHealth Exchange) and operational, but Semantic interoperability and Data completeness remain voluntary and uneven, with non-trivial Integration burden across vendors — fits "federated/standards-based but voluntary → M". |
| A — U.S. ONC HIE | I | M | Strong Interoperability mandate (Cures Act information-blocking) and Incentive alignment (HITECH/MIPS) plus HIPAA Privacy law alignment are in place, but no unified statutory mandate to participate in HIE and Information governance varies state-by-state; fits "strong incentives + interop rules without mandate". |
| A — U.S. ONC HIE | O | M | Leadership commitment at federal ONC level is sustained and Implementation planning is documented across multi-year reports to Congress, but Stakeholder engagement and Change management at the provider level are uneven and Vendor governance is only partially effective. |
| B — NHS Shared Care | U | M | Workflow integration and Trust improving as ShCRs embed into clinician workflows across ICSs, but Usability scores mixed across regional implementations and Patient engagement (NHS App linkage) and Training adequacy vary across the 42 ICS footprints per `fennelly2020national` themes. |
| B — NHS Shared Care | T | M | Syntactic interoperability uses FHIR UK Core and Semantic interoperability leverages SNOMED CT (a clear strength), with a federated regional API/exchange layer operational, but Data completeness and System quality vary across ICS-level instances rather than functioning as a single national backbone. |
| B — NHS Shared Care | I | H | National digital health strategy is documented and funded (NHS Long Term Plan, ShCR programme), Privacy law alignment is strong (UK GDPR + Data Protection Act + Caldicott), and Information governance is mature with national IG frameworks; Regulatory mandate sits between strong policy direction and statutory obligation, supporting H. |
| B — NHS Shared Care | O | M | Leadership commitment at NHS England and Implementation planning are documented, but Stakeholder engagement and Change management vary by ICS and Resource capacity is acknowledged as constrained in `fennelly2020national`, with Issue management reactive rather than proactive in some regions. |
| C — Estonia | U | M | Patient engagement is genuinely high (patient portal usage well above 50%) and Trust among clinicians is generally favourable, but published Usability scores and Training adequacy detail are limited in the cited sources, preventing a confident H across all five constructs. |
| C — Estonia | T | H | National X-Road API/exchange layer is the canonical example of a national exchange backbone, with enforced Semantic and Syntactic interoperability standards, mandated Data completeness via the national EHR obligation, and documented high System quality / uptime — meets the H decision rule cleanly. |
| C — Estonia | I | H | Statutory Regulatory mandate (national EHR law since 2008) plus a documented multi-year national digital health strategy, mature Information governance with patient opt-out, GDPR-aligned Privacy law, and an enforced Interoperability mandate — satisfies "statutory mandate + enforced governance + national strategy → H". |
| C — Estonia | O | M | Leadership commitment and Implementation planning sustained over 15+ years with stable Vendor governance and Resource capacity, but the cited sources provide limited evidence on Change management capacity and Issue management practices at the operator level, holding the rating below H. |
| D — VA/DoD | U | L | GAO findings document a persistent Usability crisis (clinician dissatisfaction at deployed VA sites), Workflow disruption with productivity loss, and Training adequacy gaps — meets the explicit "Documented persistent user-satisfaction crisis (e.g., GAO findings)" trigger for L. |
| D — VA/DoD | T | L–M | Oracle Health/Cerner and MHS GENESIS use HL7/FHIR standards (Syntactic interoperability) so this is not "no common standards", but System quality issues (outages, patient-safety incidents) and Data completeness / Integration burden problems are documented in GAO reports, indicating substantial integration debt → L–M. |
| D — VA/DoD | I | M | Statutory direction via FY2018 NDAA and federal Privacy law alignment (HIPAA + federal records statutes) provide strong policy scaffolding, but Information governance and Interoperability mandate enforcement between VA, DoD, and community providers remain partially realized per GAO, fitting strong-incentives-without-full-mandate M. |
| D — VA/DoD | O | L | GAO documents severe execution failures — cost overruns, schedule slips, deployment pauses, Vendor governance disputes with Oracle, and audit findings of inadequate Change management, Issue management, and Resource capacity — meets the L decision rule for "documented severe execution failures". |

### 3.2 Comparison (post-blind merge with original ratings)

| Case | Domain | Original | AI second rater | Match (exact) | Within-one-band |
|---|---|---|---|---|---|
| A — U.S. ONC HIE | U | M | L–M | No | Yes |
| A — U.S. ONC HIE | T | H | M | No | Yes |
| A — U.S. ONC HIE | I | H | M | No | Yes |
| A — U.S. ONC HIE | O | M | M | **Yes** | Yes |
| B — NHS Shared Care | U | M | M | **Yes** | Yes |
| B — NHS Shared Care | T | H | M | No | Yes |
| B — NHS Shared Care | I | H | H | **Yes** | Yes |
| B — NHS Shared Care | O | M | M | **Yes** | Yes |
| C — Estonia | U | H | M | No | Yes |
| C — Estonia | T | H | H | **Yes** | Yes |
| C — Estonia | I | H | H | **Yes** | Yes |
| C — Estonia | O | H | M | No | Yes |
| D — VA/DoD | U | M | L | No | **No** |
| D — VA/DoD | T | M | L–M | No | Yes |
| D — VA/DoD | I | H | M | No | Yes |
| D — VA/DoD | O | L–M | L | No | Yes |

### 3.3 AI-pass tally

| Statistic | Value |
|---|---|
| N | 16 |
| Exact agreement | 6/16 (37.5%) |
| Within-one-band agreement | 15/16 (93.8%) |
| Linear-weighted Cohen's κ | 0.27 (Landis–Koch: "fair") |
| Marginal distribution — original | L=0, L–M=1, M=6, H=9 |
| Marginal distribution — AI rater | L=2, L–M=2, M=9, H=3 |
| Direction of disagreements | All 10 disagreements: AI more conservative than original (lower band) |
| Cells > 1 band apart | 1/16 (D — VA/DoD U: M vs L) |

**Reproducibility note.** The κ statistic is computed with linear weights w_ij = |i−j|/3 over the four-band ordinal scale (L=1, L–M=2, M=3, H=4). At N=16 the κ point estimate is high-variance; we report it for transparency rather than as an inferential claim. The within-one-band percentage is the more interpretable agreement signal. Computation: `scripts/` (inline in `analysis/second-rater-protocol.md` git history).

**Interpretation.** The AI rater was systematically more conservative than the original across all 10 disagreements (no case where AI assigned a higher band). The marginal-distribution shift — original modal H, AI modal M — depresses κ even though within-one-band agreement is 94%. Two cells (D-U, D-T) are flagged in §4 as candidates for revision because the rubric's explicit decision-rule trigger language (e.g., "Documented persistent user-satisfaction crisis (e.g., GAO findings) → L") more closely matches the AI's rating than the original's. The remaining 8 disagreements reflect rubric-band ambiguity (M / L–M, H / M boundaries) and competing-evidence interpretation rather than coding errors.

### 3.4 Human second rater

Status: pending recruitment. Same blinded rubric (§2) and rating sheet apply.

---

## 4. Adjudication log

For each of the 10 exact mismatches, classify the disagreement as **(a) different evidence interpretation**, **(b) rubric-band ambiguity**, or **(c) defensible rating revision**, and record the disposition. Disposition options: **kept** (original rating retained, second rater's rating noted as an alternative); **revised** (original updated in `analysis/utio-scoring-rubric.md` with a logged change); **flagged** (left unchanged for the manuscript pending external second-rater confirmation).

| Cell | Original → AI | Δ | Class | Reasoning | Disposition |
|---|---|---|---|---|---|
| A-U | M → L–M | 1 | (b) rubric ambiguity | M / L–M boundary is the fuzziest band on the U domain. Original M cites variable adoption + workflow concerns. AI L–M cites the same evidence and applies the "two or more constructs at L–M with usability or training gaps documented in audits" decision rule. Both defensible. | kept |
| A-T | H → M | 1 | (a) different evidence interpretation | Original weights Cures Act + FHIR API mandate + TEFCA infrastructure as H. AI weights TEFCA's federated/voluntary structure at the QHIN level + non-bound semantic standards as fitting the rubric's "Federated/standards-based but voluntary → M" decision rule. | flagged — borderline H/M; rubric language modestly favours M, but Cures Act enforcement is a defensible H-tipping factor |
| A-I | H → M | 1 | (a) different evidence interpretation | Original weights Cures Act information-blocking enforcement, HITECH incentives, HIPAA as collectively H per the rubric's "Strong incentives + interoperability rules without mandate → M to H depending on enforcement" — original treats enforcement as H-tipping. AI treats absence of statutory participation mandate + state-by-state IG variation as M. | kept — H is consistent with rubric's enforcement clause |
| B-T | H → M | 1 | (a) different evidence interpretation | Original weights national interoperability standards + ShCR platform as H. AI cites federated regional implementation across 42 ICSs and variable Data completeness as M. | flagged — borderline H/M; the federated regional structure is a genuine constraint on H |
| C-U | H → M | 1 | (a) different evidence interpretation | Original weights ~99% patient e-Health Record adoption + clinician advocacy as H. AI cites limited published Usability/Training data in the cited sources as preventing a five-construct H. | kept — patient engagement and trust evidence supports H per the U decision rule |
| C-O | H → M | 1 | (a) different evidence interpretation | Original weights sustained ministry-level governance over 15+ years as H. AI cites limited evidence on Change management and Issue management at operator level. | flagged — H is supported by longevity of execution but evidence on specific O constructs is partial |
| D-U | M → L | 2 | (c) candidate for revision | Rubric U decision rule states explicitly: "Documented persistent user-satisfaction crisis (e.g., GAO findings) → L." `gao2025vaehr` and `gao2024dodehr` are GAO findings of persistent dissatisfaction. The AI applies the trigger; original M is more lenient than the rubric strictly indicates. | **flagged — author decision pending.** Recommendation: revise to L–M (middle ground reflecting GAO-documented crisis plus ongoing remediation activity at deployed sites). |
| D-T | M → L–M | 1 | (c) candidate for revision | Rubric T decision rule: "Standards adopted but with substantial integration debt → L–M." GAO documents Oracle/Cerner integration debt, deployment pauses, system quality issues. AI's L–M tracks the rubric language more directly than original M. | **flagged — author decision pending.** Recommendation: revise to L–M to align with rubric trigger language. |
| D-I | H → M | 1 | (a) different evidence interpretation | Original weights FY2018 NDAA mandate + congressional appropriations as H. AI cites partial mandate-enforcement between VA, DoD, and community providers as M. | kept — statutory mandate + sustained appropriations support H |
| D-O | L–M → L | 1 | (b) rubric ambiguity | L / L–M boundary on O is fuzzy. Original L–M acknowledges audit findings of execution gaps. AI L applies the rubric's "documented severe execution failures (cost overruns, schedule slips, audit findings of inadequate management)" trigger — and the GAO reports do document these. | kept — but the AI's L is defensible and would tighten the case if a third rater confirmed |

### Adjudication summary

| Disposition | Count |
|---|---|
| Kept (original retained) | 5 |
| Flagged — left for external second rater (rubric ambiguity / competing interpretations) | 3 |
| Flagged — candidate for revision (rubric trigger language matched by AI rater) | 2 |

**Author decision points (D-U, D-T).** Two cells in the VA/DoD case have AI ratings that more directly match the rubric's explicit decision-rule trigger language than the original ratings. The recommendation is to revise both from M to L–M, which would change the VA/DoD case row from **U(M) T(M) I(H) O(L–M)** to **U(L–M) T(L–M) I(H) O(L–M)**. This decision belongs to the manuscript author. If accepted, log the change in `analysis/utio-scoring-rubric.md` §"Application to the four cases — U.S. VA/DoD EHR Modernization" with date and reason.

---

## 5. Manuscript drop-in text

**Methods (replaces single-rater sentence in `manuscript/sections/methods.tex` §3.2.2):**

> Domain-level ratings (High / Medium / Low–Medium / Low) were assigned via a preponderance-of-evidence rule using a four-construct rubric per domain; complete construct definitions, decision rules, and per-case justification are in the project repository (`analysis/utio-scoring-rubric.md`). To mitigate single-rater bias, a supplementary AI-assisted second-rater pass (Anthropic Claude Opus 4.7, April 2026) re-rated the 16 case-domain cells blind to the original assignments; the protocol and per-cell justifications are in `analysis/second-rater-protocol.md`. Exact agreement was 6/16 (37.5%) and within-one-band agreement was 15/16 (93.8%); linear-weighted Cohen's κ = 0.27 (with N = 16, the κ point estimate is high-variance and is reported for transparency rather than as an inferential claim). All ten disagreements were in the direction of greater AI-rater conservatism (a lower band on the H–L scale), indicating a systematic — though largely within-one-band — divergence from the original ratings. Independent dual-rating with a credentialed second rater remains an outstanding methodological gap.

**Limitations (replaces ¶4 in `manuscript/sections/limitations.tex`):**

> Fourth, although the U-T-I-O coding framework was applied systematically, ratings were assigned by a single human reviewer. To partially mitigate this, an AI-assisted second-rater pass on the four-case rubric ratings yielded 6/16 (37.5%) exact agreement and 15/16 (93.8%) within-one-band agreement (linear-weighted Cohen's κ = 0.27, N = 16); the AI rater was systematically more conservative than the original, with two cells (VA/DoD U and T) flagged as candidates for revision based on rubric trigger language. A separate 10% self-audit on the 17-source domain-presence coding is documented in `analysis/audit-check.md`. The full audit trail, per-cell reasoning, and adjudication log are in `analysis/second-rater-protocol.md`. Independent dual-rating with a credentialed second rater remains an outstanding methodological gap.

---

*Created: 2026-04-29 — Last updated: 2026-04-29*
