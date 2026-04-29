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

## Application to the four cases — evidence-anchored ratings

For each case, ratings are anchored to specific sources from the bibliography (citation keys in parentheses). This is the audit trail a reviewer or replicator can use to challenge or reproduce any rating.

### U.S. ONC HIE — U(M) T(H) I(H) O(M)

| Domain | Rating | Evidence anchor |
|---|---|---|
| **U** | M | `onc2025reports` Reports to Congress portal documents variable clinician engagement and adoption-rate gaps across participating entities; `eden2016barriers` (IJMI 2016) identifies clinician trust and workflow concerns as persistent HIE barriers; `kruse2016adoption` (JMIR 2016) lists usability and training as adoption inhibitors |
| **T** | H | `onc2025reports` references FHIR API mandates under the Cures Act; `holmgren2023policyhie` (Yearbook MI 2023) describes the U.S. as one of five mature HIE-policy nations; nationwide TEFCA infrastructure deployed |
| **I** | H | HITECH Act incentive program drove U.S. EHR adoption from ~10% to >80% (`onc2025reports`); 21st Century Cures Act information-blocking rules now enforced (`holmgren2023policyhie`); strong statutory framework |
| **O** | M | `onc2025reports` documents variable participation rates across HIEs; organizational uptake heterogeneity is the primary U-T-I-O O-domain weakness (`fennelly2020national` describes execution as the differentiator across national programs) |

### NHS Shared Care Records (UK) — U(M) T(H) I(H) O(M)

| Domain | Rating | Evidence anchor |
|---|---|---|
| **U** | M | `nhs2025sharedcare` (NHS England, 26 March 2025) acknowledges variable local clinician engagement; sustained training and workflow integration cited as central challenges |
| **T** | H | `nhs2025sharedcare` describes national interoperability standards plus a shared-care-record platform; cross-organisational information sharing operational |
| **I** | H | NHS Long Term Plan + national data opt-out + information governance frameworks documented in `nhs2025sharedcare`; central national strategy authority |
| **O** | M | `nhs2025sharedcare` flags local information-governance variability and workflow integration as persistent execution challenges; `fennelly2020national` lists O-domain factors as decisive across national EHR rollouts |

### Estonia eHealth — U(H) T(H) I(H) O(H)

| Domain | Rating | Evidence anchor |
|---|---|---|
| **U** | H | `estonia2026ehealth` reports near-comprehensive coverage and high clinician engagement; 99% patient e-Health Record adoption widely cited |
| **T** | H | `estonia2026ehealth` describes the X-Road secure data-exchange layer; `holmgren2023policyhie` cites Estonia as architectural reference; enforced national standards |
| **I** | H | `europeancommission2016estoniaehr` documents the legal mandate for provider participation; 2008 Estonian Health Information System Act provides statutory backbone |
| **O** | H | `estonia2026ehealth` describes sustained ministry-level governance and evolving operational frameworks; consistent execution across two decades of national infrastructure operation |

### U.S. VA/DoD EHR Modernization — U(M) T(M) I(H) O(L--M)

| Domain | Rating | Evidence anchor |
|---|---|---|
| **U** | M | `gao2025vaehr` (GAO-25-108091, Feb 2025) documents persistent clinician dissatisfaction at deployed VA sites; `gao2024dodehr` (GAO-24-106187, Apr 2024) cites user-satisfaction scores below targets at DoD sites |
| **T** | M | `gao2025vaehr` describes mature commercial Oracle Health platform but substantial configuration burden integrating with legacy VistA and DoD clinical systems; T not High because integration debt remains material |
| **I** | H | Congressional mandate via FY2018 NDAA; sustained appropriations; clear executive-branch authority — `gao2025vaehr`, `gao2024dodehr` both confirm institutional backing |
| **O** | L--M | `gao2025vaehr` flags inadequate vendor governance and slow remediation; `gao2024dodehr` cites issue-management process inadequacies and schedule slips. Persistent execution gaps drive the lowest of any rating in the four-case set |

> **How to reproduce:** A second rater should retrieve the cited source(s) for each cell, apply the rubric criteria above, and assign a rating. Rating disagreements between this rubric and a second rater should be reported as an inter-rater reliability outcome. Single-rater limitation acknowledged in manuscript Limitations.

---

## Limitations of this rubric

1. **Single-rater application.** Ratings in the current manuscript were assigned by one reviewer (the author). Independent dual-rating with inter-rater reliability is not yet performed.
2. **Categorical resolution.** Four bands (H / M / L–M / L) are coarse. A reviewer wanting finer resolution could move to a 5- or 7-point ordinal scale.
3. **Construct weighting.** Each domain treats its constructs as equally informative; in practice, some constructs (e.g., regulatory mandate within I) may dominate the rating. Not formalized here.
4. **Evidence weighting.** Government audit findings and peer-reviewed literature are weighted equally; some reviewers might down-weight grey literature.

---

*Last updated: April 29, 2026*
