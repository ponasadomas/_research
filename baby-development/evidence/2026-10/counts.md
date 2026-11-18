# Counts — development

Rebuilt on 2026-11-16 with `../_shared/_tools/audit_niche.py development read-v1 read-w2 read-w3` (run from `mamivio.com/research/`) from `voice/*.jsonl` (merged copy: `voice-merged/all.jsonl`). **Evidence counts are counts of quotes chosen by readers, never of people or prevalence.** Coverage rows explicitly count post ids, assignment rows or file paths. Dated wave counts in `findings.md` retain their historical provenance; the totals below describe the current corpus.

| measure | value |
|---|---:|
| quotes | 2970 |
| reader voice files | 12 |
| original-wave assigned unit paths | 723 |
| distinct `raw_file` paths with quotes, all sources | 757 |
| original-wave assigned unit paths still without quotes | 29 |
| of those, not named in any reader ledger | 0 |
| historically marked quote ids (no effect) | 237 |
| active quote restrictions | 0 |
| descriptive safety-regex quote hits (see audit-safety-hits.tsv) | 86 |
| of those, not historically marked | 85 |
| speakers relabelled to `partner` in the merged copy | 2 |

### Re-reading and current coverage — 2026-11-16

The audit uses `raw_file` paths for coverage. Multiple archive posts share one `.jsonl` path, and the 757 paths also include 32 review source files; that figure is not a count of posts. Its `assigned`/`uncited` figures cover only the three original manifests, not the UR TSV assignments. The following separately reconciles post identities and the readers’ ledgers.

| reader | assigned rows | read rows | rows with quotes | rows without quotes | quotes |
|---|---:|---:|---:|---:|---:|
| UR01 | 113 | 113 | 112 | 1 | 247 |
| UR02 | 113 | 113 | 97 | 16 | 184 |
| UR03 | 315 | 315 | 184 | 131 | 241 |
| UR04 | 314 | 314 | 173 | 141 | 248 |
| UR05 | 314 | 314 | 161 | 153 | 262 |
| total | 1169 | 1169 | 727 | 442 | 1182 |

| current measure | value |
|---|---:|
| Reddit quotes, all eleven Reddit voice files | 2806 |
| app/book-review quotes | 164 |
| original-wave quotes, Reddit plus reviews | 1788 |
| UR quotes read for this synthesis | 1182 |
| distinct ids cited in findings | 1086 |
| of those, UR ids | 240 |
| UR quotes reproduced in full in findings | 229 |
| original findings ids preserved | 846 |
| new evidence subsections / dated change section | 12 / 1 |
| UR assigned posts not found / unfinished | 0 / 0 |
| UR rows read as complete unit files (including archived OP replies) | 127 |
| UR rows read as archive-only title/body records | 1042 |
| UR quotes citing unit files / archive records | 277 / 905 |
| distinct original-wave assigned Reddit post ids | 723 |
| distinct UR assigned post ids | 1169 |
| overlap of those assignment sets | 107 |
| union of post ids assigned and recorded as read | 1785 |
| distinct Reddit post ids supplying quotes, current corpus | 1314 |
| read post ids with no selected quote, current corpus | 471 |
| UR quote-bearing post ids also quoted before the re-reading | 23 |
| original assigned unit paths now supplying quotes (audit) | 694 |
| historical filter-v1 / filter-v2 safety ids covered | 938 / 349 |
| distinct ids in their union, all covered | 943 |

These post identities do not identify people: distinct posts can be crossposts, repeat authors or follow-ups. The quoted-row total includes the explicitly labelled UR05 fiction record, and UR03 has a possible promotion. Quotation totals do not turn either into independent parent evidence. Source ledgers retain the exact relationships and age uncertainties. The merged copy applies the audit’s father convention to `dv25-0217` and `dv25-0218`; the original voice records remain unchanged.

The 86 regex hits are descriptive matches, not a restriction or a severity count. All UR quotes, including the full quotes behind new hits, were read for this synthesis. The generated hit file was refreshed; the historical twenty-quote spot-check worksheet was preserved, with no invented verdicts.

Four extraction gaps remain outside the UR assignments: DR06’s already-read, no-quote `toddlers-1tjvzoj`, and DR05’s unextracted price/bet mentions in `1tnt8fi`, `1t8dis1`, `1sdj400`. They are not unfinished UR assignments. The ordinary unread inventory, including overlap cautions, is in `sources/reddit.md`.

### Quotes per reader file

| value | quotes |
|---|---:|
| reddit-dr02.jsonl | 388 |
| reddit-dr05.jsonl | 299 |
| reddit-dr03.jsonl | 276 |
| reddit-ur05.jsonl | 262 |
| reddit-ur04.jsonl | 248 |
| reddit-ur01.jsonl | 247 |
| reddit-ur03.jsonl | 241 |
| reddit-dr04.jsonl | 235 |
| reddit-dr01.jsonl | 215 |
| reddit-dr06.jsonl | 211 |
| reddit-ur02.jsonl | 184 |
| reviews-rv1.jsonl | 164 |

### Speaker (merged copy)

| value | quotes |
|---|---:|
| parent_unspecified | 1384 |
| new_mother | 1092 |
| experienced_mother | 190 |
| reviewer | 164 |
| partner | 119 |
| relative_caregiver | 15 |
| professional | 3 |
| advisor | 2 |
| recovered_parent | 1 |

### Stage

| value | quotes |
|---|---:|
| toddler_12_18_months | 600 |
| baby_9_12_months | 461 |
| baby_6_9_months | 444 |
| toddler_18_24_months | 363 |
| baby_4_6_months | 342 |
| baby_2_4_months | 307 |
| unknown | 269 |
| newborn_0_8_weeks | 113 |
| looking_back | 71 |

### Type

| value | quotes |
|---|---:|
| pain | 834 |
| question | 376 |
| belief | 321 |
| tried_failed | 278 |
| fear | 243 |
| others_said | 237 |
| success_story | 137 |
| desire | 118 |
| trigger_moment | 116 |
| objection | 110 |
| purchase | 77 |
| price_signal | 65 |
| regret | 21 |
| failure_story | 19 |
| advice_given | 18 |

### Source

| value | quotes |
|---|---:|
| reddit r/NewParents | 877 |
| reddit r/toddlers | 447 |
| reddit r/Mommit | 403 |
| reddit r/beyondthebump | 362 |
| reddit r/beyondthebumpUK | 229 |
| reddit r/Parenting | 173 |
| reddit r/sahm | 83 |
| reddit r/ScienceBasedParenting | 62 |
| reddit r/daddit | 61 |
| reddit r/FirstTimeMom | 59 |
| reddit r/Montessori | 41 |
| App Store au Kinedu | 14 |
| App Store us Lovevery | 13 |
| App Store au The Wonder Weeks | 12 |
| App Store au BabySparks | 11 |
| App Store ca The Wonder Weeks | 11 |
| App Store us Sprouty | 11 |
| App Store us CDC Milestone Tracker | 10 |
| reddit r/workingmoms | 9 |
| App Store us Pathways.org | 9 |
| App Store au Sprouty | 8 |
| App Store ca Kinedu | 7 |
| App Store ca BabySparks | 6 |
| App Store ca Lovevery | 6 |
| App Store gb Bloomie | 6 |
| App Store gb Sprouty | 6 |
| App Store ca Sprouty | 5 |
| Google Play The Wonder Weeks | 5 |
| App Store ca CDC Milestone Tracker | 4 |
| App Store gb Pathways.org | 2 |
| App Store us Bloomie | 2 |
| App Store us Little Steps | 2 |
| Google Play Sprouty | 2 |
| Barnes & Noble The Wonder Weeks | 2 |
| App Store ca Pathways.org | 1 |
| App Store au Pathways.org | 1 |
| App Store gb CDC Milestone Tracker | 1 |
| App Store au CDC Milestone Tracker | 1 |
| App Store gb Lovevery | 1 |
| App Store ca Bloomie | 1 |
| App Store au Bloomie | 1 |
| Apple Books ca The Montessori Baby | 1 |
| Apple Books us What to Expect the First Year | 1 |
| Apple Books us Brain Rules for Baby | 1 |

### Top 60 themes

| value | quotes |
|---|---:|
| play_ideas | 496 |
| maternal_guilt | 448 |
| what_to_do_all_day | 339 |
| milestone_anxiety | 324 |
| screen_time | 280 |
| price_value | 249 |
| reassurance_seeking | 212 |
| early_intervention_question | 209 |
| first_words | 208 |
| floor_play | 203 |
| crawling | 199 |
| not_enough_play | 166 |
| social_comparison | 165 |
| wont_play_alone | 164 |
| container_time | 163 |
| pediatrician_checkup | 163 |
| personalization | 149 |
| walking | 146 |
| toys_too_many | 140 |
| conflicting_advice | 139 |
| awake_time | 131 |
| tummy_time | 129 |
| milestone_comparison | 116 |
| boredom_mum | 115 |
| grandparent_comments | 113 |
| baby_classes | 111 |
| independent_play | 108 |
| information_overload | 96 |
| parental_mental_health | 88 |
| rolling | 87 |
| pulling_up | 71 |
| tummy_time_hate | 68 |
| montessori | 65 |
| babbling | 58 |
| toys | 57 |
| sitting | 53 |
| app_tracking | 44 |
| bored_baby | 44 |
| corrected_age | 40 |
| fine_motor | 40 |
| working_parent | 39 |
| daycare | 38 |
| medical_complexity | 38 |
| partner_comments | 35 |
| lovevery | 34 |
| boredom_baby | 33 |
| mobility_frustration | 32 |
| emotional_development | 31 |
| diagnostic_uncertainty | 29 |
| wonder_weeks | 28 |
| leaps | 27 |
| stuck_inside | 23 |
| cdc_milestones | 22 |
| wont_be_put_down | 18 |
| sibling_play | 17 |
| no_village | 16 |
| activity_kits | 15 |
| overstimulation | 15 |
| sibling | 13 |
| household_objects | 13 |
