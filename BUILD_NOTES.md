# Local Compile Notes

The manuscript is normally compiled on Overleaf (pdflatex + bibtex, natbib
`unsrtnat` style). For a local compile without Overleaf:

- Engine: pdflatex (pdfTeX) + bibtex, 3 passes (pdflatex, bibtex, pdflatex x2).
- `manuscript/unsrtnat.bst` is vendored so bibtex finds the natbib style.
- `orcidlink.sty` (used for the author ORCID icon) must be available; Overleaf
  provides it. A minimal local stub suffices if the package is absent.
- Output: `ehealth_adoption_systematic_review.pdf` (repo root), 75 pages.

Last local compile: 2 July 2026 — clean (bibtex no errors; zero undefined
references or citations; 95 overfull-hbox warnings, all cosmetic margin
overruns from long DOIs/URLs and wide table columns, none breaking layout).
