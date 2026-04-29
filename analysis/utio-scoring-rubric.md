# U-T-I-O Scoring Rubric for Multi-Case Analysis

**Purpose:** Provide explicit, reproducible criteria for assigning each case a High / Medium / Low–Medium / Low rating on each of the four U-T-I-O domains. Enables a second rater (or replicator) to reproduce or challenge the case ratings reported in the manuscript.

**Scope of application:** Applied to four cases in this review (U.S. ONC HIE; NHS Shared Care Records; Estonia eHealth; U.S. VA/DoD EHR modernization) but designed to generalize to any national or organizational eHealth implementation.

**Rating scale:** **H** = High; **M** = Medium; **L–M** = Low–Medium (constrained by clear gaps but not absent); **L** = Low.

---

## U — User Readiness

The extent to which clinicians, administrators, and patients are prepared and willing to engage with the eHealth system.

| Construct | High (H) | Medium (M) | Low–Medium (L–M) | Low (L) |
|---|---|---|---|---|
| Usability | Documented favourable usability scores; SUS/clinician-satisfaction surveys consistently ≥75 | Mixed survey results; some pain points but no widespread crisis | Clinician satisfaction below targets in published audits | Persistent, documented usability crisis (e.g., GAO findings of dissatisfaction) |
| Workflow integration | Designed with clinician co-design; embedded in existing workflows | Partial workflow embedding; some retrofit required | Workflow disruption acknowledged in audits | Documented workflow disruption with productivity loss |
| Training adequacy | Funded, multi-modal training programme deployed pre-go-live | Training exists but variable quality across sites | Training gaps identified in audits | No structured training programme |
| Trust / perceived usefulness | Clinician advocates speak publicly in favour of the system | Mixed clinician advocacy | Clinician resistance documented in formal surveys | Active clinician opposition or resistance |
| Patient engagement | Patient portal adoption ≥50% nationally | Patient portal exists; adoption variable | Portal exists but low usage | No patient-facing functionality |

**Rating decision rule:** Two or more constructs meeting H criteria with no constructs at L → **H**. Mix of M with one or two H/L → **M**. Two or more constructs at L–M with usability or training gaps documented in audits → **L–M**. Documented persistent user-satisfaction crisis (e.g., GAO findings) → **L**.

---

## T — Technical Interoperability

The capacity of eHealth systems to exchange, interpret, and use clinical data across organizational boundaries.

| Construct | High (H) | Medium (M) | Low–Medium (L–M) | Low (L) |
|---|---|---|---|---|
| Semantic interoperability | National terminology binding (SNOMED CT, LOINC); enforced | Standards adopted but not nationally bound | Partial standards adoption | No common terminology |
| Syntactic interoperability | HL7 FHIR R4 + CDA mandated; conformance testing | FHIR adoption variable across vendors | Legacy formats predominant | No interoperability standard |
| System quality | Documented uptime ≥99.5%; mature tooling | Acceptable uptime; episodic incidents | Reliability concerns in audits | System reliability crisis |
| Data completeness | National data set obligation enforced | Voluntary upload with high participation | Variable coverage | Sparse coverage |
| API / exchange layer | National exchange backbone deployed (e.g., X-Road) | Federated exchange (HIE network) operational | Bilateral interfaces only | No exchange |
| Integration burden | Vendor agnostic; standards-driven integration | Some vendor lock-in but multiple options | Heavy custom integration required | Vendor monoculture / lock-in |

**Rating decision rule:** National exchange backbone + enforced standards + uptime → **H**. Federated/standards-based but voluntary → **M**. Standards adopted but with substantial integration debt → **L–M**. No common standards / pervasive bilateral interfaces → **L**.

---

## I — Institutional Alignment

The degree to which regulatory, policy, governance, and legal environments support and incentivize eHealth adoption.

| Construct | High (H) | Medium (M) | Low–Medium (L–M) | Low (L) |
|---|---|---|---|---|
| Regulatory mandate | Statutory obligation to participate (e.g., national EHR law) | Strong incentive programme (HITECH-style) without mandate | Voluntary policy framework | No coordinating policy |
| National digital health strategy | Documented, funded, multi-year national strategy | Policy framework with episodic funding | Strategy in development | No national strategy |
| Information governance | Mature data-sharing agreements; national opt-out | Information governance frameworks exist; local variation | Information governance gaps acknowledged | No coherent governance |
| Privacy law alignment | Health-IT-specific privacy law (HIPAA, GDPR + national act) | Generic privacy law applied to health data | Privacy gaps acknowledged | No applicable framework |
| Interoperability mandate | Information blocking prohibited and enforced | Interoperability standards required (e.g., Cures Act) | Voluntary interoperability targets | No interoperability obligation |
| Incentive alignment | Direct financial incentives for adoption + use | Indirect incentives (quality reporting) | Limited incentive structure | No incentive structure |

**Rating decision rule:** Statutory mandate + enforced governance + national strategy → **H**. Strong incentives + interoperability rules without mandate → **M** to **H** depending on enforcement. Voluntary frameworks with documented gaps → **L–M**. Absent or fragmented regulatory environment → **L**.

---

## O — Organizational Execution

The internal organizational capabilities and leadership practices that determine whether an eHealth adoption strategy is planned, resourced, governed, and executed effectively.

| Construct | High (H) | Medium (M) | Low–Medium (L–M) | Low (L) |
|---|---|---|---|---|
| Leadership commitment | Sustained executive sponsorship; named accountable owners | Leadership engagement at launch; sustainment variable | Leadership turnover or disengagement during execution | No accountable owner |
| Implementation planning | Documented multi-phase plan with milestones; published | Plan exists; milestones missed without remediation | Reactive rather than planned execution | No formal plan |
| Change management | Funded change-management capability throughout lifecycle | Change-management activities at go-live only | Change management identified as gap in audits | No change-management capacity |
| Stakeholder engagement | Clinician co-design + ongoing feedback channels | Stakeholder engagement at launch; episodic after | Stakeholder voice limited in execution | No engagement mechanism |
| Vendor governance | Mature vendor-management practice; contract performance tracked | Contract management functional | Vendor disputes documented in audits | Vendor relationship dysfunctional |
| Resource capacity | IT staff, financial, and clinical-time resources adequate | Resource constraints acknowledged but managed | Resource gaps cited as adoption barrier | Severe resource constraint |
| Issue management | Proactive issue identification and resolution | Reactive issue resolution | Issue backlog documented in audits | No issue-management process |

**Rating decision rule:** All seven constructs meeting at least M, with leadership and change-management at H → **H**. Mixed M/L–M with vendor or change-management weakness → **M**. Two or more constructs at L–M, audit findings of execution gaps → **L–M**. Documented severe execution failures (cost overruns, schedule slips, audit findings of inadequate management) → **L**.

---

## Application to the four cases (as reported in the manuscript)

| Case | U | T | I | O | Justification (one line per domain) |
|---|---|---|---|---|---|
| **U.S. ONC HIE** | M | H | H | M | U: variable clinician engagement; T: FHIR + Cures Act API mandates; I: HITECH + Cures Act statutory framework; O: variable organizational uptake across participating entities |
| **NHS Shared Care Records (UK)** | M | H | H | M | U: variable local clinician engagement; T: national interoperability standards + shared care record platform; I: NHS Long Term Plan + national data opt-out + governance; O: local information-governance variability documented |
| **Estonia eHealth** | H | H | H | H | U: high clinician acceptance + 99% patient adoption; T: X-Road backbone + enforced standards; I: 2008 Health Information System Act mandates participation; O: sustained ministry execution + evolving governance |
| **U.S. VA/DoD EHR Modernization** | M | M | H | L–M | U: documented clinician dissatisfaction (GAO 2024, 2025); T: mature commercial EHR but legacy-integration burden; I: Congressional mandate + appropriations; O: GAO-flagged vendor governance, schedule, change-management gaps |

---

## Limitations of this rubric

1. **Single-rater application.** Ratings in the current manuscript were assigned by one reviewer (the author). Independent dual-rating with inter-rater reliability is not yet performed.
2. **Categorical resolution.** Four bands (H / M / L–M / L) are coarse. A reviewer wanting finer resolution could move to a 5- or 7-point ordinal scale.
3. **Construct weighting.** Each domain treats its constructs as equally informative; in practice, some constructs (e.g., regulatory mandate within I) may dominate the rating. Not formalized here.
4. **Evidence weighting.** Government audit findings and peer-reviewed literature are weighted equally; some reviewers might down-weight grey literature.

---

*Last updated: April 29, 2026*
