# External-Reviewer Blind Check — U-T-I-O Domain Coding

**Purpose:** Independent third-party check on a 2-source random subset of the 17 retained sources in this systematic review. The external reviewer applies the U-T-I-O rubric blind to the original coding; results feed the manuscript Limitations as a credible inter-rater check.

**Status:** Sample generated; reviewer not yet contacted.

**Companion checks already complete:**
- Self-audit on 2 different sources (S01 Holmgren, S14 NIST 800-37) → 6/8 (75%) — see `analysis/audit-check.md`
- AI-assisted second-rater pass (same 2 sources) → 6/8 (75%) opposite-direction disagreements
- AI second-rater pass on the 16 case-rubric cells → 15/16 within-one-band — see `analysis/second-rater-protocol.md`

This external-reviewer check is the **strongest** of the four — independent human dual-rating — but kept deliberately small (2 sources) to respect the reviewer's time.

---

## Sample selection

| Parameter | Value |
|---|---|
| Source population | 17 retained sources from `data/final/evidence_extraction_table.csv` |
| Exclusion logic | S01 + S14 (already in self-audit); S07 (author's own dissertation); S08–S13, S15–S16 (lengthy government/institutional grey literature, unsuitable for a 30-minute review); S17 (publisher paywall) |
| Eligible pool | 5 peer-reviewed open-access sources (S02–S06) |
| Sample size | 2 |
| Random seed | `20260430` |
| RNG | Python `random.sample` (seeded) |
| Date generated | April 30, 2026 |
| Selected | **S04 (Fennelly et al. 2020)** and **S05 (Aguirre et al. 2019)** |

To reproduce: see `notes/protocol.md` §14c.

---

# ✂️─── TEAR-OFF PACKET FOR THE EXTERNAL REVIEWER (everything below this line through the next ✂️) ───

## Independent Reviewer Request — Brief U-T-I-O Domain Coding

Hi — thank you for agreeing to do a quick blind cross-check on this systematic review. The whole task is **two short papers, eight yes/no decisions, ~30 minutes**.

### What you're doing

For each of the two papers below, decide whether the paper *substantively* addresses each of four adoption domains (U, T, I, O) defined in the rubric on the next page. Mark each domain **Y** (yes, substantively addressed) or leave blank (not addressed, or only passing mention).

**Important:**
- Please do *not* read the project's existing extraction or any related notes before completing your codes. Your value to this check is your independent judgment.
- "Substantively addresses" means the paper devotes meaningful attention to the topic — typically at least a paragraph or section, not a single passing mention.
- If you're unsure on a borderline case, please mark your judgment and add a one-line note explaining the doubt.

### The U-T-I-O rubric (apply this)

| Code | Domain | Address it as Y if the paper covers… |
|---|---|---|
| **U** | **User Readiness** | clinician usability; workflow integration; training adequacy; trust; perceived usefulness; user satisfaction; clinician burden; patient-portal engagement |
| **T** | **Technical Interoperability** | system quality; semantic interoperability (vocabularies like SNOMED CT, LOINC); syntactic interoperability (HL7 FHIR, HL7 v2.x, CDA); data completeness; API exchange; EHR integration; interface reliability |
| **I** | **Institutional Alignment** | regulatory mandates (HITECH, Cures Act, GDPR); national digital health strategy; information governance frameworks; privacy law; interoperability mandates; incentive alignment |
| **O** | **Organizational Execution** | leadership commitment; implementation planning; change management; stakeholder engagement; vendor governance; resource capacity; project management |

### The two papers

**Paper #1 — Fennelly et al. (2020)**

> Fennelly, O., Cunningham, C., Grogan, L., Cronin, H., O'Shea, C., Roche, M., Lawlor, F., & O'Hare, N. (2020). *Successfully implementing a national electronic health record: a rapid umbrella review*. International Journal of Medical Informatics, 144, 104281. doi:10.1016/j.ijmedinf.2020.104281
>
> **Open access:** https://www.sciencedirect.com/science/article/pii/S1386505620310650
> Or via PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7510429/

**Paper #2 — Aguirre et al. (2019)**

> Aguirre, R. R., Suarez, O., Fuentes, M., & Sanchez-Gonzalez, M. A. (2019). *Electronic health record implementation: a review of resources and tools*. Cureus, 11(9), e5649. doi:10.7759/cureus.5649
>
> **Open access:** https://www.cureus.com/articles/21899-electronic-health-record-implementation-a-review-of-resources-and-tools
> Or via PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6822893/

### Your response form (please fill in and send back)

#### Paper #1 — Fennelly et al. (2020)

| Domain | Your code (Y / blank) | One-line reasoning (optional) |
|---|---|---|
| U |   |   |
| T |   |   |
| I |   |   |
| O |   |   |

#### Paper #2 — Aguirre et al. (2019)

| Domain | Your code (Y / blank) | One-line reasoning (optional) |
|---|---|---|
| U |   |   |
| T |   |   |
| I |   |   |
| O |   |   |

### How to return your response

Please email the filled-in tables back to: **josh@resilientconsultingsolutions.com**
Reply-by date suggestion: **two weeks from receipt** (firmer dates negotiable).

### Disclosure & acknowledgment

Your contribution as an external reviewer will be acknowledged in the published article's Acknowledgements section unless you prefer to remain anonymous. No coauthorship or other commitment is implied or expected. You will not see the project's existing codes for these two papers; once you return your codes I'll share the comparison if you're curious.

If you have any questions or hit ambiguity in the rubric, just email me — I'd rather you ask than guess.

Thank you.

— Joshua Adams, D.I.T.
   Independent Researcher; Enterprise Architecture & Cybersecurity Consultant

# ✂️───────────────────── END OF TEAR-OFF PACKET ─────────────────────

---

## Recording the response (internal — fill in when reviewer returns)

### Paper #1 — S04 Fennelly et al. (2020)

| Domain | External reviewer | Original (CSV) | Match? | Reviewer's reasoning |
|---|---|---|---|---|
| U |   | Y |   |   |
| T |   | Y |   |   |
| I |   | Y |   |   |
| O |   | Y |   |   |

### Paper #2 — S05 Aguirre et al. (2019)

| Domain | External reviewer | Original (CSV) | Match? | Reviewer's reasoning |
|---|---|---|---|---|
| U |   | Y |   |   |
| T |   | Y |   |   |
| I |   | blank |   |   |
| O |   | Y |   |   |

### Tally (compute after both responses are recorded)

| Metric | Value |
|---|---|
| Total domain-decisions checked | 8 (2 sources × 4 domains) |
| Exact matches |   /8 |
| Disagreements |   /8 |
| Percent agreement |   % |

### Disagreement notes (per cell, if any)

Document for each disagreement: which construct(s) drove the original Y/blank decision, what the reviewer flagged differently, and whether this is interpretable as evidence-interpretation difference, rubric-band ambiguity, or a defensible original-coding revision.

| Cell | Original | Reviewer | Type of disagreement | Disposition (kept original / revised CSV / rubric clarified) |
|---|---|---|---|---|
| S04-U |  |  |  |  |
| S04-T |  |  |  |  |
| S04-I |  |  |  |  |
| S04-O |  |  |  |  |
| S05-U |  |  |  |  |
| S05-T |  |  |  |  |
| S05-I |  |  |  |  |
| S05-O |  |  |  |  |

---

## Drop-in manuscript text (after results are recorded)

To go into `manuscript/sections/limitations.tex` §4 (single-reviewer caveat) once results are in. Two variants depending on the agreement level — Claude will help finalise wording and word-budget at that point.

**Strong-agreement variant** (≥ 7/8 = ≥ 87.5%):

> An additional independent external-reviewer cross-check (n=2 sources × 4 domains = 8 cells, blind to the original extraction) yielded N/8 (X%) agreement, supporting the existing domain-presence coding.

**Mixed-agreement variant** (5–6/8):

> An independent external-reviewer cross-check on a 2-source random subset (n=8 cells, blind to the original extraction) yielded N/8 (X%) agreement; disagreements clustered on [domain] and are documented in `analysis/external-reviewer-packet.md`. The check supports the existing extraction at the studied threshold but does not eliminate single-reviewer bias as a residual limitation.

---

*Sample generated: April 30, 2026 — Last updated: April 30, 2026*
