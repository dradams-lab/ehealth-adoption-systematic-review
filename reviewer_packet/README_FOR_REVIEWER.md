# Independent Screening Check — Instructions for the Reviewer

Thank you for doing this. This document is everything you need. It should
take **about 2 to 4 hours**, and you can split it across several sittings.

## 1. What this is

A systematic review on the determinants of eHealth systems adoption
(electronic health records, health information exchange, and related
health-IT infrastructure) used an automated procedure (a large language
model applying written eligibility criteria) to screen 1,680 titles and
abstracts. Before the review is submitted, those screening decisions need an
**independent human check**. You are that check.

You will screen **126 records** using the same written criteria. You decide
each record yourself, from its title and abstract. **You will not be shown how
the automated screen decided any record**, and the records are in random
order. That blinding is deliberate: please do not ask the author about any
specific record until you have finished.

Your decisions will be compared with the automated ones, and the agreement
will be reported in the paper's Methods. With your permission, you will be
named in the Acknowledgments and described by your professional background.

The completed sheet itself (your decisions, reason codes, and any notes,
matched to the record IDs) will also be published in the paper's open-data
archive on Zenodo under a CC-BY-4.0 licence, because the check has to be
reproducible. Since the paper will identify you as the independent reviewer,
those decisions will be attributable to you. If you would prefer your
free-text notes to be left out of the public copy, say so when you return
the sheet; the decisions and reason codes themselves will be published.

## 2. Files in this folder

| File | What it is |
|---|---|
| `human_adjudication_blinded.xlsx` | The 126 records. **Fill in this file.** |
| `screening_rubric.md` | The full written eligibility criteria and reason codes. Reference only. |
| `README_FOR_REVIEWER.md` | This document. |

## 3. Opening the workbook

1. Open `human_adjudication_blinded.xlsx` in Excel.
2. The **Guide** tab has a progress counter. Before you start it should read
   126 records in the sheet, 0 decisions entered, 126 still to do, and
   0 "EXCLUDE with no reason code".
3. The **Adjudication** tab holds the records, one per row. The three
   **yellow** columns on the left are yours: `your_decision`,
   `your_reason_code`, `your_notes`. They stay in view while you scroll right.
4. If the sheet is wider than your screen, zoom out to about 90%.
5. Long abstracts continue in the `abstract_continued` columns. The first
   part ends with "[continues in next column]". Read all parts.
6. Please do not sort or delete rows, and do not edit the white columns.
   Filtering is fine: to see what is left, filter `your_decision` for blanks.

## 4. What to decide on

- Decide from the **title and abstract shown in the sheet**, plus the year,
  venue, and document type. This matches the evidence the automated
  title/abstract screen used, so the comparison is fair.
- **Please do not look up the full paper** before deciding. The `doi_link`
  column is there only in case the abstract text in the sheet is garbled. If
  you do open it, write "used DOI link" in `your_notes`.
- Twenty records have no abstract. For those, decide from the title, venue,
  and document type. If the topic cannot be established, choose MAYBE; do not
  exclude a record only because it has no abstract.

## 5. The question you are answering

**Is this record about the determinants of adopting or implementing an
eHealth system (EHR, EMR, HIE, health-IT infrastructure, or clinical
interoperability) at the organizational or national/system level?**

A record is **INCLUDE** only if **all six** of these hold:

1. **Technology.** It concerns eHealth, EHR/EMR, HIE, health IT, or clinical
   interoperability, not an unrelated clinical topic that merely mentions an
   EHR in passing.
2. **Adoption.** It addresses the determinants of adopting or implementing
   such a system: adoption, implementation, acceptance, barriers,
   facilitators, success factors, readiness, uptake, or the implementation
   process itself. A record does **not** meet this condition if it only
   measures the effects of a system that is already in place (clinical,
   financial, staffing, workflow, or data-quality outcomes), reports an
   algorithm's performance, or makes secondary use of EHR data. "The
   implementation process itself" means how the organization planned,
   prepared for, carried out, or adapted to the rollout: readiness work,
   pre-go-live testing, change management, and problems that arose from
   implementation choices and how they were handled. A study in which the
   rollout is the exposure and the outcome is a change in workflow, roles,
   safety events, or performance is an effects study (E2, as in Example F),
   whether measured before, during, or after go-live. If a record both
   documents such problems and describes what the organization did about
   them, condition 2 is met; if it only documents or measures the change,
   E2; if you cannot tell, MAYBE.
3. **Design.** It is an empirical study, a systematic/scoping/umbrella
   review, or a framework/policy analysis with a stated evidence basis.
4. **Year.** Published 2015 or later.
5. **Language.** English.
6. **Level and system scope.** The adoption or implementation question
   concerns an eHealth *system* (EHR/EMR/HIE/health-IT infrastructure) at the
   organizational, health-system, or national level. It is not solely an
   individual patient's or consumer's acceptance of an app, portal, or
   service (X1); not a single-condition digital-health intervention (X2); and
   not a study in which the EHR is only a data source or delivery channel
   (X3). Level refers to *what is being adopted*, not to who was surveyed. A
   study of clinicians', nurses', or other staff's acceptance, readiness, or
   intention to use an EHR/EMR/HIE or health-IT system that their
   organization deploys is organizational-level and is INCLUDE when the
   system itself is in scope (condition 1); it is EXCLUDE only when the
   technology is out of scope (X2 or X4) or the respondents are patients or
   consumers (X1).

**What counts as "the system".** The unit of adoption is the eHealth system
itself: an EHR/EMR, an HIE, or health-IT infrastructure (including
interoperability standards). An alert, best-practice advisory, order set,
note template, clinical pathway, or decision-support module built inside an
existing EHR is a feature of that system, not the system. A record about
building such a feature and measuring its clinical effect, or about barriers
to using it, is EXCLUDE (X3; or X2 if it serves one condition) unless the
record also studies the organization's adoption or implementation of the
EHR/HIE itself. The word "implementation" in a title is not enough on its
own: ask *what* is being implemented. A technical paper that designs,
builds, or pilots an HIE architecture, interoperability standard, FHIR
profile or implementation guide, or EHR platform, and reports only that it
works (feasibility, performance, share of data elements covered), is
EXCLUDE, E2: it implements the system but says nothing about what helped or
hindered its adoption. If the abstract also reports barriers, facilitators,
governance or stakeholder factors, or lessons learned from the
implementation, condition 2 is met: INCLUDE, or MAYBE if you cannot tell
how much of the paper is about those.

Reviews of adoption **are** eligible. A study of "digital health adoption" in
a health-system context is eligible even if it is not US-based. The rubric's
phrase "interoperable eHealth systems" names the class of system (EHR/EMR/HIE
and the infrastructure that connects them); it does not require the record
to be about interoperability as such, so a standalone hospital EMR adoption
study meets condition 1. Condition 6 is the same scope test as Step 7 on the
Guide tab; use it as the tie-breaker when a record is borderline.

## 6. The three decisions

Pick one from the dropdown in `your_decision`:

| Decision | Meaning |
|---|---|
| **INCLUDE** | All six conditions in Section 5 hold. |
| **EXCLUDE** | At least one of the six fails. Also pick a reason code (Section 7). |
| **MAYBE** | The title and abstract do not let you tell. MAYBE is treated as "passes the title/abstract stage; needs the full text", so use it for genuinely borderline records, not as a way to avoid a call. |

`your_notes` is optional. A few words help when a call is borderline or
when two reason codes both fit. Notes are published with the sheet (Section
1), so write them as you would a reviewer comment.

## 7. Reason codes (EXCLUDE only)

Pick the **one** code that best describes the main reason. If two fit, choose
the one that is most central and mention the other in `your_notes`. The
INCLUDE/EXCLUDE decision matters more than the choice between two codes.

| Code | Meaning |
|---|---|
| **E1** | Wrong technology focus: not about eHealth/EHR/HIE/health-IT adoption at all. Examples: a purely clinical trial; a wearable-sensor engineering paper; a bioinformatics method; telehealth clinical efficacy with no adoption lens. |
| **E2** | About eHealth, but not about adoption or implementation determinants. Examples: uses EHR data to study a disease; reports a prediction model; evaluates a clinical intervention delivered through an EHR without studying uptake; measures the effect of an already-adopted EHR on an outcome. |
| **E3** | Out-of-scope setting or population. Examples: a single-patient case report; non-health-sector IT; a consumer app with no relevance to health-system adoption. Use sparingly. |
| **E4** | Ineligible publication type: editorial, letter, commentary, opinion, conference abstract without methods, protocol only, poster. |
| **E6** | Published before 2015. |
| **X1** | Patient- or consumer-facing acceptance only, with no organizational or system-level adoption lens. Example: patient satisfaction with a portal or app. |
| **X2** | A single-condition digital-health intervention (for example, an app or telemonitoring program for one disease), rather than adoption of an eHealth system. |
| **X3** | The EHR is used only as a data source or as a delivery channel for a clinical outcome. |
| **X4** | Out-of-scope technology or setting. |
| **X5** | Non-research publication type. |

E1, E2, E4, and E6 are the codes for conditions 1–4 (E3 is a general
setting/population code; E5, for condition 5, is not offered); X1–X4 are the
codes for condition 6 (X5 duplicates E4). They come from two stages of the original screen and
overlap in places (for example, E2 and X3; E4 and X5). That overlap is
expected. Pick whichever reads most naturally. E5 (duplicate or non-English)
is not offered because the original screen never used it; none of your 126
records is non-English.

## 8. Worked examples

These are **made-up records**, not ones in your sheet.

**Example A: INCLUDE.**
*"Barriers to health information exchange participation among rural
hospitals: a mixed-methods study" (2019, journal article).* Abstract
describes interviews and a survey of hospital administrators about why
hospitals do or do not join a regional HIE. All six conditions hold:
organizational-level adoption determinants of an HIE.

**Example B: EXCLUDE, X1.**
*"Patient satisfaction with a diabetes self-management smartphone app: a
cross-sectional survey" (2022, journal article).* Individual patients' views
of an app. No organizational or system-level adoption question. Note that X2
also fits (single-condition digital-health intervention); either code is
acceptable, with the other mentioned in the notes.

**Example C: EXCLUDE, E2.**
*"Predicting 30-day readmission from electronic health record data: a
machine-learning study" (2021, journal article).* About an EHR, but the EHR
is only the data source for a prediction model. Nothing about adopting or
implementing the system. X3 also fits.

**Example D: MAYBE.**
*"Implementing the national electronic health record: lessons from the first
year" (2018, journal article). No abstract.* The title points to
system-level implementation, which is on topic, but without an abstract you
cannot confirm the design or scope. MAYBE.

**Example E: EXCLUDE, X3.**
*"Implementation of an electronic health record alert to increase statin
prescribing in primary care: a pre-post study" (2020, journal article).* The
EHR is the delivery channel for a prescribing intervention, and the outcome
is prescribing. "Implementation" here refers to the alert, not to the
practice adopting the EHR. Nothing about why or how the organization adopted
the system. X2 also fits if the alert serves one condition.

**Example F: EXCLUDE, E2.**
*"Effect of electronic health record adoption on hospital operating margins:
a national panel analysis" (2019, journal article).* Adoption is the
exposure, not the thing being explained; the study measures a consequence of
adoption, not its determinants. X3 also fits. Compare Example A, where the
record asks *why* hospitals do or do not adopt: that is INCLUDE. A record
that does both (for example, surveys barriers to EHR adoption and then
relates adoption to performance) is INCLUDE, because it addresses
determinants.

**Example G: INCLUDE.**
*"Nurses' acceptance of a hospital electronic health record: a technology
acceptance model survey" (2021, journal article).* Individual nurses answer
the survey, but the question is uptake of the organization's EHR, so the
level condition is met. Compare Example B, where the respondents are
patients and the technology is a single-condition app.

**Example H: EXCLUDE, E2.**
*"Design and pilot implementation of a FHIR-based health information
exchange gateway for primary care clinics" (2021, conference paper).*
Abstract describes the architecture, a prototype, and the proportion of
local data elements the standard can represent. What is being implemented
is the system itself, so the "feature" rule in Section 5 does not apply, but
the record reports only technical feasibility and nothing about why or how
organizations adopt the exchange. E2. Had the abstract also reported
governance barriers or stakeholder lessons from the pilot, it would be
INCLUDE.

## 9. Independence

- Please work alone and do not discuss individual records with the author
  until you have finished.
- Questions about the **rules** are welcome at any time. Send them to the
  author, who will answer the question about the rule without discussing
  how any record was screened.
- You are not expected to agree with the automated screen. Honest
  disagreement is exactly what this check is for.

## 10. When you have finished

1. On the Guide tab, confirm "still to do" is 0 and "EXCLUDE with no reason
   code" is 0.
2. Save the workbook under the same name with your initials added, for
   example `human_adjudication_blinded_JD.xlsx`, and email it to the author.
3. In your email, please also give:
   - roughly how long the task took;
   - one line describing your professional background, to be used in the
     paper's Methods (for example, "a health-informatics researcher with
     clinical implementation experience");
   - whether you agree to be named in the Acknowledgments and described in
     the Methods;
   - whether your completed sheet may be published with your notes included,
     or with the notes column removed from the public copy.

## 11. Confidentiality, and what happens to your work

The records are public bibliographic data (titles and abstracts of published
papers). Nothing in the packet is sensitive. The manuscript itself is not yet
published, so please keep the packet to yourself and do not share it onward.

Your completed sheet will be deposited openly with the paper (Section 1).
Nothing else about you will be published beyond the name and background line
you approve.

---

*Version note (4 October 2026). Sections 5–8 restate the review's existing
written criteria (`screening_rubric.md`) in reviewer-facing form. The
clarifications on what counts as "the system", on studies that measure the
effects of an already-adopted system, on clinician- and staff-level
acceptance of an organizationally deployed system, on technical build papers
and studies conducted during a rollout, and the worked examples were added
before the human check began; they operationalize the rubric's existing
"determinants" and "eHealth systems" language rather than adding criteria.*
