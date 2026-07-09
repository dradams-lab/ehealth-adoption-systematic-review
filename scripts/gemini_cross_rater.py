#!/usr/bin/env python3
"""
Cross-model third rater (Gemini) for the eHealth-adoption systematic review.

Runs Google Gemini as an INDEPENDENT third title/abstract rater over the
449-record stratified verification sample, using the SAME eligibility rubric
already applied by the first screen and the Claude second rater. It then builds
a three-way agreement table and collapses the human worklist to only the
records where the three raters do NOT unanimously agree.

WHAT THIS DOES AND DOES NOT DO
------------------------------
- It STRENGTHENS the reliability evidence: Gemini is a different model family
  from Claude, so its errors are less correlated -> agreement means more.
- It SHRINKS the manual pile: you only hand-adjudicate the non-unanimous set.
- It does NOT replace human adjudication. The records where the models still
  disagree are yours to decide; that residual human step is what makes the
  screen "human-validated" rather than "fully automated."

USAGE
-----
    export GEMINI_API_KEY='...your key...'        # do NOT hard-code it here
    python scripts/gemini_cross_rater.py

Resumable: progress is checkpointed to data/screened/_gemini_partial.json after
every chunk, so you can Ctrl-C and rerun without losing work.

OUTPUTS (written to data/screened/)
    gemini_ratings.csv          - Gemini's PASS/EXCLUDE + reason per record
    three_way_comparison.csv     - rater1 (first screen) | rater2 (Claude) | gemini
    final_human_worklist.csv     - ONLY the records needing your adjudication
    cross_rater_stats.txt        - agreement %, pairwise + Fleiss kappa, summary
"""

import os, sys, json, time, re, csv
from pathlib import Path

# ----------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------
MODEL = "gemini-2.5-flash"        # cheap + capable; change to gemini-2.5-pro for max quality
CHUNK = 25                        # records per checkpoint flush
SLEEP_BETWEEN = 1.0               # seconds between calls (free-tier rate-limit friendly)
MAX_ABSTRACT_CHARS = 2500

REPO = Path(__file__).resolve().parent.parent
SCREENED = REPO / "data" / "screened"
WORKLIST = SCREENED / "human_verification_worklist.csv"     # 449-record stratified sample
CORPUS   = SCREENED / "corpus_combined.csv"                 # for abstracts
TWORATER = SCREENED / "two_rater_comparison.csv"            # rater1 (machine_ta) + rater2 (Claude)
PARTIAL  = SCREENED / "_gemini_partial.json"

# ----------------------------------------------------------------------
# The rubric — IDENTICAL to the first screen and the Claude second rater
# ----------------------------------------------------------------------
SYSTEM = """You are screening titles/abstracts for a systematic review with this SCOPE:
Determinants of ADOPTION or IMPLEMENTATION of INTEROPERABLE eHealth systems at the
ORGANIZATIONAL, INSTITUTIONAL, or NATIONAL/SYSTEM level - electronic health records
(EHR/EMR), health information exchange (HIE), and health-IT interoperability.

INCLUDE (label PASS) a record if ALL hold:
- Technology is EHR/EMR/HIE/health-IT interoperability (not a single-disease app, wearable, or telemedicine-only tool).
- Topic is adoption, implementation, uptake, readiness, or determinants/barriers/facilitators thereof.
- Level is organizational/institutional/national (not solely an individual patient/consumer acceptance study).
- Design is empirical, review, or framework; English; 2015 or later.

EXCLUDE (label EXCLUDE) otherwise - e.g. patient/consumer-only acceptance, single-condition
digital-health interventions, EHR used merely as a data source for a clinical study, wrong
technology, editorial/protocol/poster, non-English, or pre-2015.

Judge independently on the text shown. Output EXACTLY one line:
DECISION: PASS   or   DECISION: EXCLUDE
then a second line:
REASON: <=15 words."""


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_prompt(row, abstract):
    ab = (abstract or "")[:MAX_ABSTRACT_CHARS]
    if len(ab) < 40:
        ab = "(no abstract available; judge on title and year)"
    return f"TITLE: {row.get('title','')}\nYEAR: {row.get('year','')}\nABSTRACT: {ab}"


def parse(text):
    if not text:
        return ("PARSE_FAIL", "")
    m = re.search(r"DECISION:\s*(PASS|EXCLUDE)", text, re.I)
    r = re.search(r"REASON:\s*(.+)", text)
    return (m.group(1).upper() if m else "PARSE_FAIL",
            (r.group(1).strip() if r else "")[:120])


def fleiss_kappa(rows_of_counts):
    """rows_of_counts: list of [n_pass, n_exclude] per item, each summing to n_raters."""
    N = len(rows_of_counts)
    n = sum(rows_of_counts[0])
    p_cat = [sum(r[j] for r in rows_of_counts) / (N * n) for j in range(2)]
    P_bar = sum((sum(r[j] ** 2 for j in range(2)) - n) / (n * (n - 1))
                for r in rows_of_counts) / N
    P_e = sum(p ** 2 for p in p_cat)
    return (P_bar - P_e) / (1 - P_e) if (1 - P_e) else float("nan")


def cohen_kappa(a, b):
    items = [(x, y) for x, y in zip(a, b) if x in ("PASS", "EXCLUDE") and y in ("PASS", "EXCLUDE")]
    if not items:
        return float("nan")
    n = len(items)
    po = sum(x == y for x, y in items) / n
    cats = ("PASS", "EXCLUDE")
    pe = sum(([x for x, _ in items].count(c) / n) * ([y for _, y in items].count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if (1 - pe) else float("nan")


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("ERROR: set GEMINI_API_KEY in your environment first "
                 "(export GEMINI_API_KEY='...').")
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("ERROR: pip install google-genai")

    client = genai.Client(api_key=key)
    cfg = types.GenerateContentConfig(system_instruction=SYSTEM,
                                      max_output_tokens=120, temperature=0)

    worklist = load_csv(WORKLIST)
    corpus = {r["rec_id"]: r.get("abstract", "") for r in load_csv(CORPUS)}
    print(f"Loaded {len(worklist)} sampled records; {len(corpus)} corpus abstracts.")

    out = json.loads(PARTIAL.read_text()) if PARTIAL.exists() else {}
    todo = [r for r in worklist if r["rec_id"] not in out]
    print(f"Already rated: {len(out)} | remaining: {len(todo)}")

    for i, row in enumerate(todo, 1):
        rid = row["rec_id"]
        prompt = build_prompt(row, corpus.get(rid, ""))
        try:
            resp = client.models.generate_content(model=MODEL, contents=prompt, config=cfg)
            decision, reason = parse(resp.text)
        except Exception as e:
            decision, reason = "PARSE_FAIL", f"api_error: {str(e)[:80]}"
        out[rid] = {"gemini": decision, "reason": reason}
        if i % CHUNK == 0 or i == len(todo):
            PARTIAL.write_text(json.dumps(out))
            print(f"  {i}/{len(todo)} rated (checkpointed)")
        time.sleep(SLEEP_BETWEEN)

    # ---- assemble the three-way table ----
    tw = {r["rec_id"]: r for r in load_csv(TWORATER)}   # has machine_ta, rater2
    rows = []
    for r in worklist:
        rid = r["rec_id"]
        g = out.get(rid, {}).get("gemini", "PARSE_FAIL")
        t = tw.get(rid, {})
        rows.append({
            "rec_id": rid, "stratum": r.get("stratum", ""),
            "title": r.get("title", ""), "year": r.get("year", ""),
            "doi": r.get("doi", ""),
            "rater1_first_screen": t.get("machine_ta", ""),
            "rater2_claude": t.get("rater2", ""),
            "rater3_gemini": g,
            "gemini_reason": out.get(rid, {}).get("reason", ""),
        })

    # keep only rows where all three raters produced a valid label
    valid = [x for x in rows
             if all(x[k] in ("PASS", "EXCLUDE")
                    for k in ("rater1_first_screen", "rater2_claude", "rater3_gemini"))]

    def agree3(x):
        return x["rater1_first_screen"] == x["rater2_claude"] == x["rater3_gemini"]

    unanimous = [x for x in valid if agree3(x)]
    split = [x for x in valid if not agree3(x)]

    # ---- stats ----
    r1 = [x["rater1_first_screen"] for x in valid]
    r2 = [x["rater2_claude"] for x in valid]
    r3 = [x["rater3_gemini"] for x in valid]
    counts = [[[x["rater1_first_screen"], x["rater2_claude"], x["rater3_gemini"]].count("PASS"),
               [x["rater1_first_screen"], x["rater2_claude"], x["rater3_gemini"]].count("EXCLUDE")]
              for x in valid]

    stats = []
    stats.append(f"Cross-model reliability (n={len(valid)} with 3 valid labels; "
                 f"model={MODEL})")
    stats.append(f"  Parse failures (Gemini): {sum(1 for x in rows if x['rater3_gemini']=='PARSE_FAIL')}")
    stats.append(f"  Unanimous (all 3 agree): {len(unanimous)} "
                 f"({len(unanimous)/len(valid):.1%})")
    stats.append(f"  Split (>=1 disagrees):   {len(split)} "
                 f"({len(split)/len(valid):.1%})  <-- YOUR human worklist")
    stats.append(f"  Fleiss' kappa (3 raters): {fleiss_kappa(counts):.3f}")
    stats.append(f"  Cohen kappa r1-r2 (screen vs Claude): {cohen_kappa(r1, r2):.3f}")
    stats.append(f"  Cohen kappa r1-r3 (screen vs Gemini): {cohen_kappa(r1, r3):.3f}")
    stats.append(f"  Cohen kappa r2-r3 (Claude vs Gemini): {cohen_kappa(r2, r3):.3f}")
    stats_txt = "\n".join(stats)
    print("\n" + stats_txt)

    # ---- write outputs ----
    def write(path, dicts):
        if not dicts:
            dicts = [{}]
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(dicts[0].keys()))
            w.writeheader()
            w.writerows(dicts)

    write(SCREENED / "gemini_ratings.csv",
          [{"rec_id": k, **v} for k, v in out.items()])
    write(SCREENED / "three_way_comparison.csv", rows)
    for x in split:
        x["your_decision"] = ""     # blank column for you to fill
        x["your_notes"] = ""
    write(SCREENED / "final_human_worklist.csv", split)
    (SCREENED / "cross_rater_stats.txt").write_text(stats_txt + "\n")

    print(f"\nWrote:\n  gemini_ratings.csv ({len(out)})"
          f"\n  three_way_comparison.csv ({len(rows)})"
          f"\n  final_human_worklist.csv ({len(split)})  <-- adjudicate these"
          f"\n  cross_rater_stats.txt")


if __name__ == "__main__":
    main()
