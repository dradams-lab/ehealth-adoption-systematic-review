# Draft email to the independent reviewer

*For Josh to adapt and send. Attach `reviewer_packet/reviewer_packet_<date>.zip`
(build it with `python3 reviewer_packet/build_packet.py`). Do not attach
anything else from `data/screened/`.*

---

**Subject:** Would you do a 2–4 hour independent screening check for my systematic review?

Hi [Name],

I'm finishing a systematic review on the determinants of eHealth systems
adoption (EHR and health information exchange) for submission to *JMIR
Medical Informatics*, and I need an independent reviewer for one step. I'm
hoping you'd be willing.

**What it is.** The title/abstract screening was done by an automated
procedure (a large language model applying written eligibility criteria).
Before I submit, I need a human who didn't write those criteria to
independently re-screen a sample of records so I can report how well the
automated screen agrees with a person. You'd be that person.

**What it involves.** 126 records, each decided from its title and abstract
using the written criteria. It's a spreadsheet with dropdowns, about 2 to 4
hours in total, and you can split it across sittings. The attached packet has
the spreadsheet, the criteria, and a step-by-step README. You won't see how
the automated screen decided anything, and I'll keep clear of your decisions
until you're done. Questions about the rules are welcome any time.

**Your background is the point.** The check needs someone with health-IT or
implementation-science knowledge who hasn't worked on this review, which is
why I thought of you.

**Recognition.** With your permission, I'd name you in the Acknowledgments and
describe your role and background in the Methods. One thing to know up
front: the paper's open-data archive will include the completed screening
sheet (decisions, reason codes, and notes), so your calls will be public and
attributable to you. If you'd rather your notes stay out of the public file,
just say so. [Delete if not applicable: I'm also happy to offer an honorarium
of $___ for your time.]

**Timing.** It would help me most to have it back by **[date, about two weeks
out]**. If that doesn't work, tell me what does.

If you're up for it, open the README in the attached zip and you can start
right away. If not, no problem at all; a quick no is useful too.

Thanks very much,

Josh

Joshua Adams, D.I.T.
Resilient Consulting Solutions
josh@resilientconsultingsolutions.com

---

## After you send it

- Note the date sent and the agreed return date in
  `submission/submission_checklist.md`.
- When the file comes back, put it in `data/screened/` and tell Claude. It
  will unblind by `rec_id` and analyse per `analysis/human_verification_plan.md`
  §10: the reviewer's decision settles the 88 disputed and 2 unrated records for
  the agreement computation, the 36 spot-checks give the error rate and bound
  for the rest, per-stratum agreement
  is reconstructed over the full 449-record sample, and the §7 thresholds are
  applied to those reconstructed figures.
- Record the reviewer's background line and both consents (naming; publishing
  the sheet with or without notes). If they decline the notes part, drop the
  `your_notes` column from the public copy before the next Zenodo release.
