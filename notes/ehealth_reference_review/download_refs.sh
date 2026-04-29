#!/usr/bin/env bash
set -u
BASE=/mnt/data/ehealth_reference_review
ART=$BASE/articles
REP=$BASE/reports
LOG=$BASE/logs/download.log
: > "$LOG"
fetch() {
  url="$1"; out="$2";
  echo "== $out" | tee -a "$LOG"
  curl -L --fail --retry 2 --connect-timeout 20 --max-time 120 -A "Mozilla/5.0" "$url" -o "$out" >> "$LOG" 2>&1 && echo "OK $out" | tee -a "$LOG" || echo "FAIL $out" | tee -a "$LOG"
}
fetch "https://www.bmj.com/content/bmj/372/bmj.n71.full.pdf" "$ART/page2021_prisma_bmj.pdf"
fetch "https://medinform.jmir.org/2016/2/e19/PDF" "$ART/kruse2016_ehr_adoption_jmir.pdf"
fetch "https://www.cureus.com/articles/22651-electronic-health-record-implementation-a-review-of-resources-and-tools.pdf" "$ART/aguirre2019_ehr_implementation_cureus.pdf"
fetch "https://bmcmedinformdecismak.biomedcentral.com/counter/pdf/10.1186/s12911-023-02115-5.pdf" "$ART/torab2023_interoperability_bmc.pdf"
fetch "https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?article=10290&context=dissertations" "$ART/adams2020_strategies_ehealth_systems_adoption.pdf"
fetch "https://www.gao.gov/assets/gao-25-108091.pdf" "$REP/gao2025_va_ehr_modernization.pdf"
fetch "https://www.gao.gov/assets/gao-24-106187.pdf" "$REP/gao2024_dod_ehr.pdf"
fetch "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf" "$REP/nist_sp_800_37_r2.pdf"
fetch "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf" "$REP/nist_sp_800_53_r5.pdf"
fetch "https://health.ec.europa.eu/system/files/2016-11/laws_estonia_en_0.pdf" "$REP/europeancommission2016_estonia_ehr_law.pdf"
fetch "https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf" "$REP/hhs_hipaa_deidentification_guidance.pdf"
