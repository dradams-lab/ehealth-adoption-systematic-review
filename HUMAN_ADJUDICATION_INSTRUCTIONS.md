# Human Adjudication — How to Work the 126-Record Sheet

**What this is.** Two AI raters screened a 449-record sample and disagreed on
88 records. You decide those 88, plus 36 records they agreed on (a spot-check)
and 2 the second rater didn't rate. Your decisions become the human
reliability result reported in the paper.

**Time:** roughly 1–2 minutes per record, so about 2–4 hours. It's fine to
split this across sessions.

## The file
Open `data/screened/human_adjudication_blinded.csv` in Excel. It is
**blinded**: it doesn't show what either AI decided, which stratum a record
came from, or whether the record is disputed. Rows are shuffled.

**Don't open** `human_adjudication_worklist.csv`, `two_rater_comparison.csv`,
or `three_way_comparison.csv` until you've finished. They show the AI answers.

## For each record
1. Read the title and abstract. Decide on **title + abstract only**, as both AI
   raters did. If there is no abstract, use the title, venue, and document type.
2. Fill `your_decision` with one of:
   - `INCLUDE` — meets all inclusion criteria
   - `EXCLUDE` — fails a criterion (fill `your_reason_code`)
   - `MAYBE` — you can't tell without the full text (counts as passing
     title/abstract, the same as the rubric's MAYBE)
3. For EXCLUDE, fill `your_reason_code` with one code:
   - E1 wrong technology focus · E2 eHealth but not adoption/implementation ·
     E3 out-of-scope setting/population · E4 ineligible publication type ·
     E6 published before 2015
   - X1 patient/consumer acceptance only · X2 single-condition digital-health
     intervention · X3 EHR used only as a data source/channel · X4
     out-of-scope technology/setting · X5 non-research publication
4. `your_notes` is optional. Add a few words when a call is borderline.

Full definitions: `analysis/screening_rubric.md`.

## The scope test (the question most disputes turn on)
Is the record about **adoption or implementation of interoperable eHealth
systems (EHR/EMR/HIE/health-IT infrastructure) at the organizational or
national/system level**? Individual patient acceptance of an app (X1), or a
single-condition digital intervention (X2), is out of scope.

## When you're done
Save the file under the same name and tell Claude. It will then:
- unblind the sheet by rec_id
- compute your agreement with the primary screen and with the AI second rater,
  per stratum, with Cohen's κ
- apply the pre-set rules in `analysis/human_verification_plan.md` §7
  (≥ 0.90 accept; 0.80–0.90 accept and report a sensitivity bound; < 0.80
  re-screen that stratum)
- update the paper wherever it says "UPDATE AFTER"

**Reporting note:** the plan specifies an independent reviewer who did not
build the rubric. If you adjudicate yourself, the paper will state that the
author adjudicated. That's normal for a single-author review; it just has to
be disclosed.
