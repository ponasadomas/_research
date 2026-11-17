# Reddit reading ledger — PR55 (wave 3, keep_core chunks 032–040)

Reader PR55, id prefix pb55, written 2026-10-25. Brief: `_shared/_tools/prompt-pregnancy-reader-w3.txt` and `_shared/_tools/brief-reading.md`.

| step | count |
|---|---|
| chunks assigned | 9 (read-w3-keep_core-032 … read-w3-keep_core-040) |
| units in them | 160 (25+13+16+19+19+12+14+21+21) |
| units read in full | 160 |
| units with at least one quote | 107 |
| units excluded under the lines not to cross | 27 |
| units read, nothing quoted (thin, medical-only or off-niche) | 20 |
| units flagged, not quoted (possible seeding) | 1 |
| crossposts not quoted (same author, same text quoted once from the other copy) | 5 |
| quotes written | 274 (pb55-0001 … pb55-0274) |
| restricted quotes | 44 (listed in `synthesis/reader-notes-pr55.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr55.jsonl` → 274 quotes, 0 failed |

107 + 27 + 20 + 1 + 5 = 160. pregnant-1snvbqi and PregnancyUK-1sm9l7m are counted among the 107 quoted units and also listed below (all-restricted and flagged), so those rows overlap. Posts dated 13–17 April 2026; the latest quoted reply is 30 April 2026. Unit list: `scratchpad/PR55/units.txt`. Quote source records: `scratchpad/PR55/recs/rec-00N.py`, built by `scratchpad/PR55/build.py` (rebuilds the voice file from the records; never append by hand). Per-unit decisions: `scratchpad/PR55/ledger.tsv`.

## Excluded (neutral reason; not quoted)

| chunk | unit | reason |
|---|---|---|
| 032 | pregnant-1skviq6 | severe mental-health post (constant panic, mental health tanked) |
| 032 | BabyBumps-1sl8b01 | mental-health post with medication |
| 032 | pregnant-1sl9qb1 | centred on previous loss and early bleeding |
| 032 | beyondthebump-1slbfwl | severe postpartum mental-health post |
| 033 | pregnant-1slnizm | severe mental-health post with medication |
| 033 | PregnancyUK-1slnjos | severe anxiety post with repeated urgent monitoring |
| 034 | pregnant-1slp3q8 | centred on a scan finding and specialist referral |
| 034 | pregnant-1slpts2 | centred on previous loss and early test results |
| 034 | pregnant-1slrwfu | relationship-safety concern around paternity |
| 034 | pregnant-1slvbdq | severe mental-health post with medication and a medical condition |
| 035 | pregnant-1slxcsr | crisis wording in the author's own reply |
| 035 | PregnancyUK-1sm9ara | mental-health post with medication |
| 035 | pregnant-1smcyn3 | substance use and weighing whether to continue the pregnancy |
| 036 | PregnancyUK-1smf37e | relationship-safety concern (ex-partner behaviour) |
| 036 | pregnant-1smf483 | crosspost of PregnancyUK-1smf37e, same reason |
| 036 | pregnant-1smgftq | severe mental-health post with medication |
| 036 | pregnant-1smhb0m | substance use in the post |
| 036 | NewParents-1smkyav | acute medical recovery post |
| 036 | pregnant-1smp1ld | severe grief/mental-health post with crisis-adjacent wording |
| 036 | pregnant-1smrsgz | partner hostility over sex (relationship safety) |
| 037 | pregnant-1smuwy8 | weighing whether to end the pregnancy |
| 037 | pregnant-1smz5y5 | partner's repeated belittling (relationship safety) |
| 038 | pregnant-1sn65im | centres on sexual-violence content |
| 039 | pregnant-1sngzd5 | early test results with fear of loss |
| 039 | pregnant-1sno01r | relationship-safety concern (coercive partner) |
| 039 | pregnant-1snppm4 | acute medical symptoms |
| 040 | beyondthebumpUK-1so8spi | acute medical emergency at birth |

## Read in full, nothing quoted

| chunk | unit | note |
|---|---|---|
| 032 | BabyBumps-1skrijm | read, medication question only, nothing quoted |
| 032 | pregnant-1skt70p | read, thin, nothing quoted |
| 032 | pregnant-1sl2qnj | read, scan measurements and specialist referral, medical-only, nothing quoted |
| 032 | BabyBumps-1sl77zw | read, thin, nothing quoted |
| 032 | pregnant-1slbnxz | read, medication list, medical-only, nothing quoted |
| 033 | pregnant-1slg918 | read, lab result question, medical-only, nothing quoted |
| 033 | BabyBumps-1slnlnw | read, bowel symptom post, nothing quoted |
| 034 | pregnant-1slrj5l | read, thin, nothing quoted |
| 034 | pregnant-1slwrom | read, thin food question, nothing quoted |
| 035 | BabyBumps-1slzuhs | read, high-risk monitoring and past loss in passing, centred on a sick pet; nothing quoted |
| 035 | pregnant-1sm7ixb | read, supplement question, medical-only, nothing quoted |
| 037 | PregnancyUK-1smz5af | read, pre-existing conditions, medical-only, nothing quoted |
| 038 | Mommit-1sn3gyi | read, thin (singing breath control), nothing quoted |
| 039 | BabyBumps-1snfgfm | read, alcohol-before-knowing question, medical-only, nothing quoted |
| 039 | pregnant-1snfmol | read, scan measurement question, medical-only, nothing quoted |
| 039 | BabyBumps-1snhz2k | read, walking pain, exercise question, nothing quoted |
| 039 | pregnant-1snn7bn | read, thin, nothing quoted |
| 039 | pregnant-1snpdax | read, medication question, nothing quoted |
| 040 | pregnant-1so2h5n | read, thin, nothing quoted |
| 040 | pregnant-1so7ni0 | read, medication tip, nothing quoted |

## Quoted, every quote restricted

| chunk | unit | note |
|---|---|---|
| 039 | pregnant-1snvbqi | violent hyperbole in the post ("commit homocide" as a joke about stock lines); its 4 quotes are restricted |

## Quoted, loss or termination mentioned in passing

| chunk | unit | note |
|---|---|---|
| 032 | pregnant-1skt4xm | an ex-partner's pressure to end the pregnancy mentioned in passing; post centres on bonding at 40 weeks; quotes don't touch it |
| 038 | PregnancyUK-1snb4q3 | a previous infant loss mentioned in passing; post centres on splitting paternity leave; quotes don't touch it |

## Flagged

| chunk | unit | note |
|---|---|---|
| 035 | PregnancyUK-1sm9l7m | stylised, possibly AI-polished; quoted one line as one voice |
| 040 | pregnant-1so2ddd | possible supplement seeding (vitamin-deficiency framing, AI-like phrasing), not quoted |

## Crossposts

| chunk | unit | note |
|---|---|---|
| 032 | pregnant-1skvt0j | crosspost of BabyBumps-1skvkyy (same author, same text), quoted once |
| 035 | beyondthebumpUK-1slwza8 | crosspost of NewParents-1slwy85 (same author, same text); post quoted once from the NewParents copy, nothing else |
| 035 | beyondthebumpUK-1sm9m52 | crosspost of PregnancyUK-1sm9l7m, not quoted |
| 036 | pregnant-1smjjhp | crosspost of BabyBumps-1smjhng (same author, same text), quoted once |
| 037 | beyondthebumpUK-1sn0j3x | crosspost of PregnancyUK-1sn0i20; post text quoted once from the PregnancyUK copy, this copy's own replies quoted |
| 039 | FirstTimeMom-1snlyeh | crosspost of pregnant-1snlg5e (same author, same text), quoted once |
