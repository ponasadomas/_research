# Counts — sleep-mother

Rebuilt on 2026-11-16 with the existing `../_shared/_tools/audit_niche.py sleep-mother read-v1 read-w2 read-w3` (run from `mamivio.com/research/`) from `voice/*.jsonl`; merged copy: `voice-merged/all.jsonl`. **Evidence counts are counts of selected quotes, never of people or prevalence.** Coverage rows explicitly count assignment rows, post identities or file paths. Dated wave comparisons in `findings.md` retain their original scope; the totals here describe the current corpus.

| measure | value |
|---|---:|
| quotes | 4243 |
| reader voice files | 14 |
| original-wave assigned unit paths | 1120 |
| distinct quoted `raw_file` paths, all sources | 1246 |
| original-wave assigned paths still without quotes | 22 |
| of those, not named in any reader ledger | 0 |
| historically marked quote ids (no effect) | 486 |
| active quote restrictions | 0 |
| descriptive safety-regex quote hits (see audit-safety-hits.tsv) | 144 |
| of those, not historically marked | 138 |
| speakers relabelled to `partner` in the merged copy | 0 |


### Re-reading and synthesis coverage — 2026-11-16

| reader | assigned rows | read rows | rows with new quotes | rows without new quotes | quotes |
|---|---:|---:|---:|---:|---:|
| UR01 | 230 | 230 | 210 | 20 | 328 |
| UR02 | 230 | 230 | 208 | 22 | 311 |
| UR03 | 229 | 229 | 214 | 15 | 296 |
| UR04 | 229 | 229 | 217 | 12 | 303 |
| total | 918 | 918 | 849 | 69 | 1238 |

| current measure | value |
|---|---:|
| original-wave quotes, Reddit plus reviews | 3005 |
| UR quotes read for this synthesis | 1238 |
| UR Reddit quotes / review quotes | 1226 / 12 |
| current Reddit quotes / review quotes | 4187 / 56 |
| distinct ids cited in findings | 1583 |
| of those, UR ids | 256 |
| UR quotes reproduced in full in the findings | 256 |
| previously cited ids retained | 1327 |
| new evidence subsections / final dated change section | 11 / 1 |
| UR assignment rows not found / unfinished | 0 / 0 |
| UR rows: Reddit identities / saved reviews reassessed | 905 / 13 |
| UR rows: complete frozen Reddit units / archive-only posts | 343 / 562 |
| UR quote-bearing Reddit rows / review rows | 841 / 8 |
| UR quotes citing Reddit units / archive-only records | 528 / 698 |
| original-wave assigned Reddit identities | 1120 |
| original-wave / UR assignment overlap | 223 |
| union of Reddit identities recorded as read | 1802 |
| distinct Reddit post identities supplying quotes | 1719 |
| read Reddit identities with no selected quote | 83 |
| UR quote-bearing Reddit identities also quoted before | 130 |
| original assigned unit paths now supplying quotes (audit) | 1098 |
| historical safety-lane posts covered / total | 425 / 425 |
| remaining full-read tier-A / B / C posts | 1646 / 3694 / 882 |
| further matched posts with removed/deleted bodies | 32 |

The audit counts `raw_file` paths, not post identities. An archive path can contain many quoted posts and review paths are also included. Its 22 original assigned paths without quotes differ from the 83 read Reddit post identities without any selected quote; they are not inconsistent measures. The UR TSV assignments are reconciled separately above. The source ledger explains the identity subtraction used for remaining queues.

The original review run read 279 saved review units and selected 44 quotes. The thirteen review rows were reassessed from that existing material, yielding twelve new quotes from eight rows. Those twelve reside in `reddit-ur*.jsonl` but remain review evidence, including explicitly adjacent adult and child accounts. They do not add thirteen newly collected reviews or establish a postpartum identity.

The 69 zero-new-quote rows have ledger results: 58 off-niche and 11 duplicate/nothing-new rows. They are completed reads. Assignments labelled `post` sometimes had a frozen unit available, which explains why the actual 343 unit reads exceed the 223 Reddit rows labelled `unit` in the queue. All 223 named original reader omissions/trim candidates and all 425 intake safety posts are covered. Different post ids can still be crossposts or repeat authors; quote and post totals do not identify independent people.

The audit's 144 regex hits are descriptive text matches, not severity ratings or restrictions. All UR quote texts were read, including the 124 new hits; the generated hit list was refreshed. The historical twenty-quote spot-check worksheet was preserved with no new verdicts invented. Original voice records and reader ledgers remain unchanged, including `second_pregnancy` stage labels; no retagging was needed for this integration.

### Reproducible current calculations

Run from `mamivio.com/research/`. The audit generates the headline and distribution tables. For post coverage, use `Path(u).stem` over `units` in the three `_raw/reddit/read-*/chunks.jsonl` manifests, unioned with Reddit `id` values in `scratchpad/unfilter-reread/assign-ur*.tsv`. Review ids are separate. For each frozen tier candidate, the key is `subreddit + '-' + id`; remaining full-read posts are that tier's key set minus the read union. This gives A 3023 − 1377 = 1646; B 3694 − 0 = 3694; C 882 − 0 = 882; safety 425 − 425 = 0. All 32 unavailable bodies remain unavailable.

For quote-source totals, classify each `voice/*.jsonl` record by whether `source.startswith('reddit')`, independently of its filename. For citations, use the distinct matches of `r'\[([a-z]+\d{1,2}-\d{4})\]'` in `synthesis/findings.md`; intersect with `id.startswith('smu')` for UR ids. Full reproduction is a literal match of `'"' + quote + '" [' + id + ']'`. Compare the previous 1,327-id set saved before editing to the current set for retention. The final checks found 1,493 all-length immediately paired fragments exact, including short fragments outside the stock check's twelve-character minimum. Eleven new evidence subsections are distinct subsection numbers absent before the revision; renamed existing §10.3 and §10.4 are not counted as new.

### Quotes per reader file

| value | quotes |
|---|---:|
| reddit-mr07.jsonl | 460 |
| reddit-mr08.jsonl | 421 |
| reddit-mr09.jsonl | 377 |
| reddit-mr03.jsonl | 330 |
| reddit-ur01.jsonl | 328 |
| reddit-mr04.jsonl | 321 |
| reddit-ur02.jsonl | 311 |
| reddit-mr02.jsonl | 306 |
| reddit-ur04.jsonl | 303 |
| reddit-ur03.jsonl | 296 |
| reddit-mr05.jsonl | 285 |
| reddit-mr06.jsonl | 263 |
| reddit-mr01.jsonl | 198 |
| reviews-rv1.jsonl | 44 |

### Speaker (merged copy)

| value | quotes |
|---|---:|
| new_mother | 1800 |
| parent_unspecified | 823 |
| expecting_mother | 709 |
| experienced_mother | 566 |
| partner | 265 |
| reviewer | 56 |
| recovered_parent | 15 |
| relative_caregiver | 7 |
| gave_up_parent | 1 |
| advisor | 1 |

### Stage

| value | quotes |
|---|---:|
| newborn_0_8_weeks | 821 |
| baby_2_6_months | 816 |
| baby_6_12_months | 803 |
| toddler | 384 |
| pregnancy_third | 338 |
| unknown | 268 |
| pregnancy_second | 217 |
| return_to_work | 184 |
| pregnancy_first | 161 |
| looking_back | 151 |
| second_pregnancy | 100 |

### Type

| value | quotes |
|---|---:|
| pain | 1904 |
| tried_failed | 431 |
| others_said | 306 |
| belief | 288 |
| desire | 211 |
| fear | 210 |
| trigger_moment | 197 |
| success_story | 189 |
| question | 156 |
| objection | 107 |
| purchase | 89 |
| price_signal | 78 |
| failure_story | 38 |
| regret | 28 |
| advice_given | 11 |

### Source

| value | quotes |
|---|---:|
| reddit r/NewParents | 850 |
| reddit r/beyondthebump | 654 |
| reddit r/pregnant | 593 |
| reddit r/sleeptrain | 499 |
| reddit r/Mommit | 417 |
| reddit r/BabyBumps | 228 |
| reddit r/beyondthebumpUK | 189 |
| reddit r/daddit | 162 |
| reddit r/Postpartum_Depression | 150 |
| reddit r/Parenting | 112 |
| reddit r/sahm | 88 |
| reddit r/workingmoms | 81 |
| reddit r/FirstTimeMom | 80 |
| reddit r/PregnancyUK | 70 |
| reddit r/postpartumprogress | 14 |
| App Store us Slumber | 5 |
| App Store au Calm | 4 |
| App Store gb Calm | 4 |
| App Store us Headspace | 4 |
| Apple App Store slumber US | 3 |
| App Store au BetterSleep | 3 |
| App Store au Rise | 3 |
| Barnes & Noble Say Good Night to Insomnia | 3 |
| App Store au Slumber | 2 |
| App Store US — RISE | 2 |
| Apple App Store headspace US | 2 |
| App Store ca Stellar Sleep | 2 |
| App Store ca BetterSleep | 2 |
| App Store gb BetterSleep | 2 |
| App Store gb Headspace | 2 |
| App Store us Rise | 2 |
| Apple Books The First Forty Days | 2 |
| Apple Books Say Good Night to Insomnia | 2 |
| App Store AU — Slumber | 1 |
| App Store us RISE | 1 |
| Apple App Store bettersleep US | 1 |
| Apple App Store calm US | 1 |
| App Store us Stellar Sleep | 1 |
| App Store ca Slumber | 1 |
| Apple Books The Sleep Solution | 1 |

### Top 60 themes

| value | quotes |
|---|---:|
| cumulative_deprivation | 1111 |
| night_feeds_split | 559 |
| pregnancy_insomnia | 534 |
| shift_system | 438 |
| resentment | 378 |
| return_to_work_exhausted | 322 |
| maternal_guilt | 292 |
| no_village | 273 |
| anxiety_at_night | 262 |
| body_pain | 241 |
| cant_sleep_when_baby_sleeps | 236 |
| bedsharing_mum_sleep | 232 |
| partner_sleeps_through | 232 |
| physical_discomfort | 222 |
| sleep_aids_question | 212 |
| family_help | 212 |
| price_value | 192 |
| naps_for_mum | 187 |
| hypervigilance | 186 |
| racing_mind | 169 |
| pumping_at_night | 157 |
| information_overload | 137 |
| identity_loss | 131 |
| listening_for_baby | 122 |
| early_waking_mum | 108 |
| self_care_guilt | 90 |
| baby_in_room | 87 |
| wants_to_be_heard | 78 |
| night_nanny | 76 |
| pregnancy_pillow | 69 |
| formula_for_sleep | 51 |
| bathroom_trips | 50 |
| apps_meditation | 37 |
| working_pregnant | 35 |
| white_noise_for_mum | 31 |
| partner_job | 30 |
| sleep_consultant | 27 |
| father_deprivation | 27 |
| caffeine | 26 |
| personalization | 21 |
| possible_promo | 20 |
| separate_rooms | 18 |
| postpartum_insomnia | 16 |
| father_role | 12 |
| father_carries_nights | 11 |
| fathers_deprivation | 11 |
| cbti | 10 |
| melatonin_question | 10 |
| help_arrives_still_awake | 9 |
| protecting_partner_sleep | 9 |
| sleep_tracking | 8 |
| partner_job_safety | 8 |
| partner_doesnt_understand | 8 |
| shift_work_partner | 7 |
| tried_method | 7 |
| ai_chatbot | 7 |
| partner_snoring | 5 |
| rage_at_night | 5 |
| comparison_to_others | 5 |
| revenge_bedtime | 4 |
