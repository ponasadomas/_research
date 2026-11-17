# baby-development

Research on mothers of babies 0 to 24 months who want to know what to do with the baby at
this age and whether the baby is on track. Collected October to November 2026 for the
mamiVio baby-development funnel. The questions it set out to answer are in `brief.md`.
Rules for all research: `../README.md`.

## What is here

| Folder | What was collected | When | State |
|---|---|---|---|
| `ads/` | nothing in this niche's own folder | | Not collected here. The October 2026 Ad Library sweep for all mother-and-baby niches is in the niche-selection research (see "Paths" below). |
| `books/` | An attempt at reader reviews for 9 books: store pages saved, but only 5 reviews found | 2026-10-25 | **Nearly empty.** Stores show few reviews; Amazon and Goodreads were not fetched. See `books/README.md` |
| `competitors/` | 21 notes on sellers, from 57 saved pages (115 files) | 2026-10-25 | Done for this round; `not-harvested.md` lists what was skipped |
| `reddit/` | 1,892 posts handed to readers out of the shared archive (723 in the first reading, 1,169 in the re-reading; April to October 2026) | 2026-10-25, re-read 2026-11-16 | 2,806 quotes. About 4,300 candidate posts still unread, see `reddit/reddit.md` |
| `reviews/` | App Store and Google Play reviews of 9 apps, 177 complete reviews (165 files) | 2026-10-25 | 159 quotes |
| `sales-letters/` | Old long-form sales letters from the Wayback Machine (553 files) | from 2026-11-03 | Captured and listed; notes per letter not written yet |
| `youtube/` | nothing | | Not collected |
| `statistics/` | Published figures on American first-time mothers, 17 saved sources | 2026-11-17 | 23 figures; most cover all mothers, not first-time mothers |
| `forums/`, `marketplaces/`, `official-guidance/` | nothing | | Not collected in this niche. The niche-selection research in `../new-and-expecting-mothers/` has all three for the whole market |
| `quotes/` | 2,970 quotes, one record each, in 12 files; `merged/all.jsonl` is a generated copy | | Every quote checked against its source |
| `evidence/` | `evidence.md`: the quotes sorted under themes with conclusions (44,500 words, cites 1,086 quotes); counts; readers' notes; the unfilter report | 2026-11-16 | Current |

Findings page (the short one): not written yet. It will be
`~/GitHub/_home/library/avatars/baby-development/findings/`.

## The four questions

| Question | Answered from | State |
|---|---|---|
| 1. Who is she, and what is her life like? | nothing collected for it | **Not answered.** Pieces are scattered through the Reddit quotes; mamiVio's own quiz data has not been used |
| 2. What hurts, what does she want, and how does she say it? | `reddit/` | Answered; one source only |
| 3. What is she buying, what does she pay, and how did it go? | `reviews/`, `books/` | Half answered. Reviews of 9 apps were read (159 quotes), but nobody first mapped what she spends on, so the apps were picked without it. Books: 5 quotes. Courses, classes, toys: nothing |
| 4. Who is selling to her, and what is working? | `competitors/`, the Ad Library sweep, `sales-letters/` | Partly: competitors done, ads only in the shared sweep |

## Reddit originals are not in this folder

The Reddit posts were downloaded once for all mother-and-baby niches and five niches
picked their posts from that one archive. It is kept once, at
`../new-and-expecting-mothers/reddit/raw/reddit-2026/`. Every Reddit quote here points
into it, so this folder cannot be checked without that one beside it. What this niche
selected from the archive, and who read what, is in `_work/reddit-selection/` and
`_work/reading-ledgers/`.

## Checking

Run from this folder. All four must report the counts shown and no failures.

```
python3 -I _tools/check_ids.py                            2970 records, 0 duplicated
python3 -I _tools/verify_quotes.py                        2970 quotes, 0 failed
python3 -I _tools/verify_evidence_ids.py                  1086 ids cited, 0 unresolved; 1008 fragments, 0 failed
python3 -I _tools/audit.py read-v1 read-w2 read-w3        723 assigned, 0 unexplained
```

`_tools/history/` holds the scripts and agent briefs used to collect and read this
material. They are kept as a record and still use the old paths; they are not meant to
be run from here.

## Paths in older files

This folder was moved here on 2026-11-17 from `ads/mamivio.com/research/development/`.
The quote records, `evidence/evidence.md` and `brief.md` use the new paths. Notes, ledgers
and logs written before the move are left as written and use the old ones:

| Old path | Now |
|---|---|
| `_raw/<kind>/` | `<kind>/raw/` |
| `_raw/reddit/` | `_work/reddit-selection/` |
| `../_shared/_raw/reddit-2026/` | `../new-and-expecting-mothers/reddit/raw/reddit-2026/` |
| `voice/`, `voice-merged/` | `quotes/`, `quotes/merged/` |
| `synthesis/`, `synthesis/findings.md` | `evidence/`, `evidence/evidence.md` |
| `sources/reddit-reading-*.md` | `_work/reading-ledgers/` |
| `sources/` (other files) | the kind folder they describe, or `_work/sources/` |
| `scratchpad/` | `_work/scratchpad/` |
| `product/product-brief.md` | `brief.md` |
| `../_shared/_tools/`, `_tools/` | `_tools/history/shared/`, `_tools/history/` |
| `../global/`, `../main/` | `../new-and-expecting-mothers/` |

## Quote schema

Every record: `id` (prefix `dvNN-NNNN`, never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder; Reddit originals are in the shared archive, see below). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `newborn_0_8_weeks`, `baby_2_4_months`, `baby_4_6_months`, `baby_6_9_months`, `baby_9_12_months`, `toddler_12_18_months`, `toddler_18_24_months`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `evidence/reader-notes-*.md`): `what_to_do_all_day`, `awake_time`, `tummy_time`, `tummy_time_hate`, `floor_play`, `rolling`, `sitting`, `crawling`, `pulling_up`, `walking`, `first_words`, `babbling`, `fine_motor`, `milestone_comparison`, `milestone_anxiety`, `corrected_age`, `pediatrician_checkup`, `cdc_milestones`, `wonder_weeks`, `leaps`, `screen_time`, `toys_too_many`, `montessori`, `play_ideas`, `boredom_mum`, `maternal_guilt`, `not_enough_play`, `container_time`, `baby_classes`, `app_tracking`, `information_overload`, `conflicting_advice`, `reassurance_seeking`, `social_comparison`, `grandparent_comments`, `early_intervention_question`, `personalization`, `price_value`.

The other side of the door: Grandparents and in-laws who compare; paediatricians and physios; parents who say 'babies just develop'; Montessori purists; buyers of apps who cancelled.

