# Two-Stage Title/Abstract Screening — Method

The full corpus (1,680 unique records) was screened in two documented stages against the a priori rubric.

## Stage 1 — Sensitive title/abstract screen (broad)
Every record classified INCLUDE / EXCLUDE / MAYBE against the base rubric (analysis/screening_rubric.md): eHealth/EHR/EMR/HIE/HIT focus + adoption/implementation/determinants topic + eligible design + 2015+ + English.
Result: 1,247 passed (INCLUDE 1,115 + MAYBE 132); 433 excluded (E1 wrong tech focus 154; E2 wrong outcome 202; E3 setting 2; E4 pub-type 69; E6 pre-2015 window 6).

## Stage 2 — Eligibility refinement (tightened scope)
The 1,247 stage-1 survivors were re-screened against the review's precise construct: **adoption of interoperable eHealth SYSTEMS (EHR/EMR/HIE/health-IT infrastructure) at the ORGANIZATIONAL or NATIONAL/system level.** This removes patient/consumer-facing acceptance-only studies (X1), single-condition digital-health interventions (X2), studies using an EHR only as a data source/channel for a clinical outcome (X3), out-of-scope technology/setting (X4), and non-research publication types (X5).
Result: 549 passed to full-text (INCLUDE 535 + MAYBE 14); 698 excluded at stage 2.

## Final title/abstract funnel
- 1,680 screened
- 433 excluded at stage 1 (off-topic / window / publication type)
- 698 excluded at stage 2 (out of tightened organizational/system scope)
- **549 sought for full-text eligibility assessment**

## Screening method note
Screening was performed with LLM assistance (a classification-grade model) applying the fixed rubric to each record's title + abstract + metadata; every decision carries a reason code and a one-line justification, logged in data/screened/screening_log_combined.csv for audit. Records lacking an abstract (94) were screened on title + venue + document type. This machine-assisted first pass is subject to human verification before finalization.
