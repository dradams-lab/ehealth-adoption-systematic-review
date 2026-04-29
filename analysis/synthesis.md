# Thematic Synthesis Notes
**Study:** Determinants of eHealth Systems Adoption: A Systematic Review and Multi-Case Analysis  
**Framework:** U-T-I-O Model (User Readiness, Technical Interoperability, Institutional Alignment, Organizational Execution)  
**Evidence Base:** 17 sources (6 systematic/umbrella reviews, 4 scoping/narrative reviews, 4 government/audit reports, 3 policy/framework analyses) + 4 case studies  
**Last updated:** April 29, 2026

---

## U — User Readiness

**Definition:** The extent to which clinicians, administrators, and patients are prepared and willing to engage with an eHealth system, encompassing usability perceptions, workflow fit, training adequacy, and sustained satisfaction.

**Key determinants identified across sources:**
- **Usability** — Kruse et al. (2016): low perceived usefulness and poor interface design cited as top EHR adoption barriers; Aguirre et al. (2020): unintended consequences of EHR use (alert fatigue, workflow disruption) reduce clinician satisfaction
- **Workflow fit** — Holmes et al. (2016): workflow integration failure is a primary HIE adoption barrier; Fennelly et al. (2020): national implementations that embedded EHR into existing clinical workflows had higher uptake rates
- **Training adequacy** — Kruse et al. (2016): insufficient training consistently appears as an adoption inhibitor; Adams (2020): training and support structures are among six core adoption themes identified from senior IT leader interviews
- **Trust and perceived usefulness** — Holmes et al. (2016): provider trust in data accuracy and system reliability is a prerequisite for HIE adoption
- **User satisfaction** — GAO VA EHR (2025): VA clinicians report significant usability and satisfaction deficits with the Oracle Health system post-deployment; GAO DoD EHR (2024): user satisfaction scores remain below targets

**Synthesis:** User readiness is the domain most consistently identified as an implementation failure point in otherwise technically capable systems. The VA/DoD case exemplifies the risk: a fully deployed, nationally mandated system experiencing sustained user resistance due to workflow mismatch and usability deficits.

---

## T — Technical Interoperability

**Definition:** The capacity of eHealth systems to exchange, interpret, and use clinical data across organizational boundaries through standardized interfaces, data models, and integration protocols.

**Key determinants identified across sources:**
- **Semantic interoperability** — Bitar et al. (2023): semantic alignment (shared clinical terminology, SNOMED CT, LOINC, FHIR) is the most technically complex interoperability layer; identified as a prerequisite for meaningful data exchange
- **Syntactic interoperability** — Bitar et al. (2023): HL7 FHIR R4, HL7 v2.x, and CDA standard compliance required for syntactic-level exchange; fragmentation across legacy systems creates integration burden
- **System quality** — DeLone & McLean (2003): system reliability, response time, and availability directly shape user adoption behavior
- **Information quality** — DeLone & McLean (2003): data completeness, accuracy, and timeliness affect clinician trust and adoption; Holmes et al. (2016): data quality concerns cited as a barrier to HIE trust
- **API compliance** — ONC Reports (2025): FHIR-based API mandates under the Cures Act are accelerating interoperability but implementation burden varies by vendor
- **Estonia X-Road** — Estonia eHealth (2026): the X-Road secure data exchange layer provides a technically mature, nationally standardized interoperability backbone enabling cross-provider data access

**Synthesis:** Technical interoperability is a necessary but not sufficient condition for adoption. Bitar et al. and ONC reports consistently show that even technically proficient systems fail to achieve broad adoption without alignment in the user, institutional, and organizational domains.

---

## I — Institutional Alignment

**Definition:** The degree to which the regulatory, policy, governance, and legal environment supports and incentivizes eHealth adoption, including national digital health strategies, interoperability mandates, privacy law frameworks, and information governance structures.

**Key determinants identified across sources:**
- **Regulatory incentives** — ONC Reports (2025): HITECH meaningful use incentives drove U.S. EHR adoption from ~10% to >80% among hospitals; financial incentives are the strongest documented institutional lever
- **Interoperability mandates** — 21st Century Cures Act information blocking prohibition (2021 enforcement): Adler-Milstein et al. (2023) show that information blocking rules have begun reshaping vendor behavior toward data sharing
- **National digital health strategy** — Fennelly et al. (2020): countries with explicit national EHR strategies (Australia, Estonia, UK) show higher implementation coherence; Estonia's eHealth strategy (dating to 2005) is the most mature example
- **Privacy law compliance** — HIPAA de-identification guidance (HHS, 2024); GDPR in EU contexts; Estonia: Personal Data Protection Act provides the legal framework for health data exchange
- **Information governance** — NHS Shared Care Records (2025): information governance frameworks (national data opt-out, data sharing agreements) are cited as the primary enabling condition for cross-organisational record sharing in England
- **Legal mandate** — EU/Estonia EHR Law (2016): mandatory provider upload obligations create a comprehensive, legally enforced data set; no comparable mandate exists in the U.S. (voluntary participation model)

**Synthesis:** The institutional domain is the most consistently differentiated across cases. Estonia's legal mandate produces near-universal participation; the U.S. incentive-based model produces high overall adoption rates but persistent fragmentation; the NHS governance model produces strong interoperability intent but variable local execution.

---

## O — Organizational Execution

**Definition:** The internal organizational capabilities and leadership practices that determine whether an eHealth adoption strategy is planned, resourced, governed, and executed effectively at the enterprise level.

**Key determinants identified across sources:**
- **Leadership commitment** — Fennelly et al. (2020): senior leadership sponsorship is identified as the single most consistent success factor across national EHR implementations; Adams (2020): leadership support is a core adoption theme
- **Change management** — Aguirre et al. (2020): structured change management reduces workflow disruption and clinician resistance; absence of formal change management correlates with higher post-go-live adverse events
- **Stakeholder engagement** — Fennelly et al. (2020): clinician co-design and end-user involvement in system configuration improves both usability and adoption rates
- **Vendor governance** — GAO VA EHR (2025): VA's Oracle Health contract has faced persistent configuration disputes, cost overruns, and schedule delays attributed to inadequate vendor governance and contract management
- **Implementation planning** — GAO DoD EHR (2024): DoD deployment at new sites has accelerated but issue management processes remain insufficient; reactive rather than proactive problem resolution
- **Resource capacity** — Kruse et al. (2016): small and rural healthcare organisations consistently report resource constraints (IT staff, financial capacity) as adoption barriers

**Synthesis:** Organizational execution is the domain most predictive of variation between similarly resourced and mandated systems. The VA/DoD divergence from Estonia — despite comparable institutional mandate strength — is explained primarily by organizational execution gaps: vendor management failures, insufficient change management, and user satisfaction deficits that were not identified and resolved quickly.

---

## Cross-Domain Synthesis: Convergence Findings

### Finding 1: Multi-domain convergence is the decisive predictor
No source in the evidence base identifies a single-domain explanation as sufficient for adoption success. All 6 systematic/umbrella reviews cite multi-domain determinants. The Estonia case is the only case among the four with High ratings across all four domains — and it demonstrates the highest adoption maturity.

### Finding 2: Technical strength without user/organizational alignment yields limited adoption value
ONC HIE programs and the VA/DoD initiative both deployed substantial technical infrastructure (T = High or Medium-High) but neither achieved the adoption breadth or user engagement of Estonia. The gap is attributable to user readiness and organizational execution domain deficits, consistent with the U-T-I-O model's prediction.

### Finding 3: Institutional mandate is necessary but not transformative alone
Both the U.S. (HITECH, Cures Act) and VA/DoD (Congressional mandate) cases demonstrate strong institutional alignment. Yet adoption outcomes differ substantially. Institutional mandate creates the conditions for adoption — it does not guarantee it.

### Finding 4: The U-T-I-O model correctly predicts observed adoption patterns
Applying the model retrospectively to all four cases yields predictions consistent with observed outcomes:
- Estonia: f(H, H, H, H) → Highest adoption maturity ✓
- ONC HIE: f(M, H, H, M) → Broad adoption with variable organizational uptake ✓
- NHS Shared Care: f(M, H, H, M) → Strong national vision, variable local execution ✓
- VA/DoD: f(M, M, H, L-M) → Strong mandate, constrained realised adoption value ✓

---

## Evidence Gaps and Limitations

1. **Single-reviewer coding:** All thematic coding was conducted by a single reviewer; independent verification would strengthen inter-rater reliability
2. **English-language restriction:** Non-English literature (particularly from Nordic, East Asian, and LMIC contexts) not captured
3. **Survivor bias:** Publicly documented cases tend to be politically prominent programs; failed or discontinued implementations are underrepresented
4. **PRISMA counts pending:** Formal database searches not yet executed; evidence base represents a purposive seed set rather than a fully screened systematic corpus
5. **Temporal range:** Rapidly evolving regulatory landscape (AI in healthcare, TEFCA, QHINs) may affect institutional alignment findings post-2026

---

*This synthesis document supports the manuscript results and discussion sections and informs the U-T-I-O Model operationalization.*
