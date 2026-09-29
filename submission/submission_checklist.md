# JMIR Medical Informatics — Pre-Submission Checklist

Work through top to bottom. Items marked **[ACTION]** need a human decision or
step I cannot complete.

## Content / formatting (done)
- [x] Original Paper structure (IMRD) — Introduction, Methods, Results, Discussion
- [x] Structured abstract, 345 words (< 450 limit), B/O/M/R/C headers
- [x] 5–10 semicolon-separated keywords, MeSH-aligned (see submission_metadata.md)
- [x] Manuscript compiles cleanly (75-page PDF; bibtex clean; 0 undefined refs/cites)
- [x] PRISMA 2020 checklist prepared
- [x] PRISMA-for-Abstracts checklist prepared
- [x] Supplementary Files S1–S4 present and appended
- [x] Generative-AI use disclosed (end-matter + cover letter) — corrected 29 Sep 2026:
      end-matter now lists LLM screening and the AI second rater; cover letter
      no longer calls the screening check human
- [x] Ethics/IRB statement present (secondary public data; not required)
- [x] Cover letter drafted with all JMIR-required disclosures

## [ACTION] — human decisions before you hit submit
- [ ] **Register/verify ORCID** for the author (JMIR requires it; 0000-0002-7185-9125 — confirm it resolves)
- [ ] **Confirm funding statement** (likely "unfunded") in cover letter + form
- [ ] **Confirm competing-interests statement** (likely "none")
- [ ] **Choose preprint status** and fill the cover-letter bracket:
      none / medRxiv / JMIR Preprints — and disclose whichever you pick
- [x] **Model details** — resolved 29 Sep 2026: the models and versions were not
      recorded, so the manuscript, S1, and cover letter now say so (screening
      June–July 2026; Claude second rater July 2026), and the Eighth limitation
      notes that the AI decisions cannot be regenerated exactly. If the
      script/prompt used for the Claude second rater turns up, add it to `scripts/`.
- [ ] **Recompile the PDF on Overleaf** after the edits above (no local TeX).
- [ ] **New Zenodo version needed.** The v1 deposit (10.5281/zenodo.21282519,
      GitHub release v1.0-submission, 9 Jul 2026) has a generic title, no
      description (`.zenodo.json` was not at the repo root), is missing
      `two_rater_comparison.csv` and the adjudication worklist, and contains the
      old cover letter that wrongly called the screening check human. Fixed in
      the repo: `.zenodo.json` moved to root, files now tracked. To publish:
      push, then create a new GitHub release (you do this). The manuscript,
      cover letter, metadata, and PRISMA checklist now cite the **concept DOI
      10.5281/zenodo.21282518**, which always resolves to the latest version.
- [ ] Optional before the next release: `cover_letter.docx` (older Elsevier
      letter) and `manuscript_anonymous.docx` (older draft) are out of date and
      are included in the public archive.
- [ ] **Request APF waiver/discount** at submission if applicable
- [ ] Provide 3–4 suggested reviewers (optional but helpful)

## [ACTION] — the substantive blocker (my standing recommendation)
- [ ] **Run the 126-record human adjudication** — use the blinded sheet
      `data/screened/human_adjudication_blinded.csv` (instructions in
      `HUMAN_ADJUDICATION_INSTRUCTIONS.md`). Until a person works this list, the
      reliability section rests on machine-vs-machine agreement (κ=0.61), and
      the AI second rater would have excluded 54 of 179 sampled included
      studies (30%). A preprint or submission puts your name on the claims —
      finish this first.
      *Reporting note:* `analysis/human_verification_plan.md` specifies an
      independent reviewer who did not build the rubric and all 449 records. If
      you adjudicate the 126 yourself, the paper must say so (author
      adjudication of AI disagreements plus a spot-check) as a deviation from
      that plan.

## Recommended sequence
1. Human adjudication (126 records) → update reliability numbers in Methods,
   Limitations, S1, cover letter, PRISMA item 8, and Zenodo README (search for
   "UPDATE AFTER"); if a stratum falls below 0.80, re-screen it per the plan.
2. Recompile PDF on Overleaf.
3. Push, then new GitHub release → new Zenodo version (concept DOI already cited).
4. Fill cover-letter brackets (funding, COI, preprint).
5. Submit to JMIR MI; request fee waiver if needed.
