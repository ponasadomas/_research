1. Saved [STATIC-ANALYSIS.md](/home/thinkpad/GitHub/mamiVio.com/research/kinedu-aq-assessment/STATIC-ANALYSIS.md) with line-numbered evidence.
2. Beautified copies are separate; all original hashes match.
3. Found six modes: assessment, list, skills, classic, classic-steps, hook.
4. Documented all 15 fetch sites and response fields consumed.
5. Question order is anchor → items → indexed calibration.
6. No client-side answer-dependent question skipping exists.
7. Additional questions come from the API’s `extension` response.
8. Answers are numeric `{id, y}`, with `y` equal to `0` or `1`.
9. Initial results fire after completing base questions, then any extension.
10. The 800 ms debounce applies only to skills-report edits.
11. Developmental ages, bands, and skill values come from the API.
12. Cosmetic elements include fixed range bands and blurred `"88"` placeholders.
13. Randomness generates identifiers, with no random scoring found.
14. `capture=0` bypasses email in every mode.
15. Included 816 question translations and curl examples; no browser or live-site calls were made.