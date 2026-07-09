# Cross-Model Third Rater (Gemini) — Step-by-Step

**Goal.** Run Google Gemini as an independent third title/abstract rater over
the 449-record verification sample, using the *same* rubric already applied by
the first screen and the Claude second rater. Result: a three-way agreement
table that (a) shrinks your manual worklist to only the records where the three
models disagree, and (b) gives you a stronger, cross-model-family reliability
statistic for the Methods.

**Time:** ~15–25 min of Gemini runtime (449 records, free tier), then your
adjudication of whatever residual set it produces (expected ~40–70 records).

**What this does NOT do:** it does not remove the human step. The records where
the models still disagree are yours to decide by hand — that residual human
adjudication is what makes the screen "human-validated" rather than automated.

---

## Step 1 — Get a Gemini API key (free)

1. Go to **https://aistudio.google.com/apikey**
2. Sign in with a Google account.
3. Click **"Create API key"** → **"Create API key in new project"**.
4. Copy the key (starts with `AIza...`). Keep it somewhere private — do **not**
   paste it into any chat, commit it, or share it.

Free tier is enough for 449 records. (If you have a paid Google Cloud project
you can select it instead; not required.)

---

## Step 2 — Open Terminal at the repo

```bash
cd ~/Documents/Research/ehealth-adoption-systematic-review
```

---

## Step 3 — Set up Python + install the Gemini library

You need Python 3.9+ (macOS has it). Create a small virtual environment so this
doesn't touch your system Python:

```bash
python3 -m venv .venv-gemini
source .venv-gemini/bin/activate
pip install --upgrade pip
pip install google-genai
```

You'll know it worked if `pip show google-genai` prints a version.

> Every new terminal session, re-run `source .venv-gemini/bin/activate` before
> running the script.

---

## Step 4 — Enter your Gemini key (this is the prompt you asked for)

Paste your key in place of the `...`:

```bash
export GEMINI_API_KEY='AIza...paste-your-key-here...'
```

Verify it's set (this prints only whether it's present, not the value):

```bash
[ -n "$GEMINI_API_KEY" ] && echo "key is set" || echo "key NOT set"
```

> `export` keeps the key only in this terminal session's memory — it is not
> written to disk and disappears when you close the window. That's the safe way
> to do it. Do not put the key inside the script.

---

## Step 5 — Run the rater

```bash
python scripts/gemini_cross_rater.py
```

What you'll see:
- `Loaded 449 sampled records; 1680 corpus abstracts.`
- progress every 25 records: `25/449 rated (checkpointed)` …
- then a stats block, then the list of output files.

**It's resumable.** If you Ctrl-C or your connection drops, just run the same
command again — it reads `data/screened/_gemini_partial.json` and continues
where it left off.

**If you hit a rate-limit error** (free tier is ~15 requests/min): open
`scripts/gemini_cross_rater.py` and change `SLEEP_BETWEEN = 1.0` to `4.0`, then
rerun. It will resume, not restart.

---

## Step 6 — Read the result

The script prints, and writes to `data/screened/cross_rater_stats.txt`:

- **Unanimous (all 3 agree)** — the records you can trust without re-reading.
- **Split (>=1 disagrees)** — **your human worklist**, written to
  `data/screened/final_human_worklist.csv`.
- **Fleiss' kappa** (3-rater agreement) and the three pairwise **Cohen's kappa**
  values — these go straight into the Methods reliability paragraph.

Output files (all in `data/screened/`):
| File | What it is |
|------|-----------|
| `gemini_ratings.csv` | Gemini's PASS/EXCLUDE + reason per record |
| `three_way_comparison.csv` | first screen \| Claude \| Gemini, side by side |
| `final_human_worklist.csv` | **only the disputed records — adjudicate these** |
| `cross_rater_stats.txt` | agreement %, Fleiss + pairwise kappas |

---

## Step 7 — Adjudicate the residual set (the human step)

Open `data/screened/final_human_worklist.csv`. For each row, read the title (and
DOI if you need the abstract), then fill the two blank columns:

- `your_decision` → type `PASS` or `EXCLUDE`
- `your_notes` → one short line if the call was non-obvious

This is the part only you can do. Expected size ~40–70 records; most resolve in
seconds because the disagreement is usually obvious once a human reads it.

---

## Step 8 — Send it back to me

Once `final_human_worklist.csv` has your decisions filled in, tell me and I'll:
- fold your adjudications into the reliability analysis,
- write the Methods paragraph (three-rater design, Fleiss + pairwise kappas,
  human-adjudicated residual, corrected-error rate),
- update Supplementary File S4 (second-rater protocol) to describe the
  cross-model ensemble,
- and note any records your adjudication flips, so the included set stays honest.

---

## Safety notes
- The key lives only in your terminal session (Step 4). It is never written to
  disk, the script, or git.
- If you ever think the key leaked, revoke it at
  https://aistudio.google.com/apikey and make a new one.
- `.venv-gemini/` and `data/screened/_gemini_partial.json` are local scratch;
  add them to `.gitignore` if you don't want them tracked (the script's real
  outputs — the CSVs and stats — are the things worth committing).
