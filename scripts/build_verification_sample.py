#!/usr/bin/env python3
"""Reproducibly draw the stratified human-verification sample.

Reproduces data/screened/human_verification_worklist.csv from the screening log.
Seed is fixed (20260701) so the draw is auditable.
"""
import pandas as pd, numpy as np

SEED = 20260701
LOG = "data/screened/screening_log_combined.csv"
INC = "data/final/included_studies_evidence.csv"
FTX = "data/final/fulltext_exclusions.csv"
OUT = "data/screened/human_verification_worklist.csv"

def nsize(N, p=0.90, e=0.05, z=1.96):
    n0 = z**2 * p*(1-p) / e**2
    return int(np.ceil(n0 / (1 + (n0-1)/N)))

def main():
    log = pd.read_csv(LOG)
    inc = pd.read_csv(INC)
    ftx = pd.read_csv(FTX)
    basis = dict(zip(inc.Record_ID, inc.Evidence_Basis))
    inc_ids, ftx_ids = set(inc.Record_ID), set(ftx.Record_ID)

    log["stratum"] = None
    log.loc[log.ta_final == "EXCLUDE_S1", "stratum"] = "E_stage1_excl"
    log.loc[log.ta_final == "EXCLUDE_S2", "stratum"] = "D_stage2_excl"
    for i, r in log[log.ta_final == "PASS_TA"].iterrows():
        rid = r.rec_id
        if rid in inc_ids:
            log.at[i, "stratum"] = "B_incl_abstract" if basis.get(rid) == "abstract" else "A_incl_fulltext"
        elif rid in ftx_ids:
            log.at[i, "stratum"] = "C_fulltext_excl"
        else:
            log.at[i, "stratum"] = "Z_passta_other"

    rng = np.random.default_rng(SEED)
    targets = {}
    for s, N in log.stratum.value_counts().items():
        targets[s] = int(N) if s == "C_fulltext_excl" else min(int(N), nsize(N))

    picks = [log[log.stratum == s].sample(n=n, random_state=int(rng.integers(1e9)))
             for s, n in targets.items()]
    sample = pd.concat(picks).sort_values(["stratum", "rec_id"]).reset_index(drop=True)

    def md(r):
        if r.ta_final == "EXCLUDE_S1": return f"EXCLUDE (Stage 1, {r.reason_code})"
        if r.ta_final == "EXCLUDE_S2": return f"EXCLUDE (Stage 2, {r.s2_reason})"
        if r.stratum == "C_fulltext_excl": return "EXCLUDE (full-text)"
        if r.stratum == "A_incl_fulltext": return "INCLUDE (full text assessed)"
        if r.stratum == "B_incl_abstract": return "INCLUDE (abstract assessed)"
        return "PASS_TA"

    sample["machine_decision"] = sample.apply(md, axis=1)
    sample["machine_justification"] = sample.apply(
        lambda r: r.s2_justification if isinstance(r.s2_justification, str) and r.s2_justification.strip()
        else (r.justification if isinstance(r.justification, str) else ""), axis=1)
    wl = sample[["rec_id", "stratum", "source_db", "title", "year", "doi", "doctype",
                 "machine_decision", "machine_justification"]].copy()
    wl["reviewer_decision"] = ""
    wl["reviewer_corrected_label"] = ""
    wl["reviewer_notes"] = ""
    wl.to_csv(OUT, index=False)
    print(f"Wrote {OUT}: {len(wl)} rows")
    print(wl.stratum.value_counts().sort_index().to_dict())

if __name__ == "__main__":
    main()
