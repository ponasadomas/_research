1. [questions.csv](/home/thinkpad/GitHub/mamiVio.com/research/kinedu-aq-assessment/questions.csv): **408 unique IDs**.
2. [age-map.md](/home/thinkpad/GitHub/mamiVio.com/research/kinedu-aq-assessment/age-map.md): ordered questions and counts for every supported age.
3. [ENUMERATION.md](/home/thinkpad/GitHub/mamiVio.com/research/kinedu-aq-assessment/ENUMERATION.md): method, curl, correction formula, diagram, and findings.
4. **373 IDs** appear initially; **35 additional IDs** appear only in observed reports.
5. One shared bank produces **49 distinct initial lists**, with adjacent ages sharing 16–35 IDs.
6. Supported API ages are **0–48 months**; ages 49–51 return HTTP 422.
7. Birthdates use `YYYY-MM-DD`; question localization happens client-side.
8. Day-15 filenames differ from returned ages; the future-birthdate failure is preserved.
9. GW28/GW32/GW36 subtract **3/2/1 whole months**, clamped at zero.
10. Correction stops at chronological age **24 months**; GW37 remains uncorrected.
11. Initial lists contain **22–39 questions**; calibration disappears at age 37.
12. All-yes answers expose eight extension questions at ages 0–41.
13. Unexpectedly, all-no at age 1 returns `on_pace`; a repeat was identical.
14. **229 responses** saved: 223 successes and six preserved HTTP errors; validation passed.
15. Recovered IDs match both 408-ID client dictionaries; unreferenced server IDs remain unproven.