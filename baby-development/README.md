# baby-development

Research on mothers of babies 0 to 24 months who want to know what to do with the baby at
this age and whether the baby is on track. Collected October to November 2026 for the
mamiVio baby-development funnel. A new round began 2026-11-18; `brief.md` describes it and
names no product. The October brief is `_work/2026-10/brief.md`.

**Where the October round is now:** `quotes/2026-10/`, `evidence/2026-10/`,
`findings/2026-10/` (both findings pages and `her-words.md`) and `_work/2026-10/` (reading
ledgers, the Reddit selection). Wherever this page says `quotes/`, `evidence/`, `findings/`,
`her-words.md`, `_work/reddit-selection/` or `_work/reading-ledgers/` below, read it with
`2026-10/` added. The new round's working files are in `_work/2026-11/`.
Rules for all research: `../README.md`.

## The round of November 2026: where it stands (2026-11-20)

How it was run, step by step: `../_tools/README.md`.

| Step | State |
|---|---|
| Random sample of 20,000 posts read and sorted | Done: 2,471 on the niche, 5,534 near, 11,995 off. `evidence/2026-11/second-reading/counts.md` |
| Digests of each pattern | Done: 20, in `evidence/2026-11/second-reading/` |
| Findings sections, one per pattern | Done, not reviewed: `findings/2026-11/patterns/` |
| Findings page and her words | Written 2026-11-20, not reviewed: `findings/what-hurts-and-what-she-wants.md` (163 findings), `her-words.md` (247 phrases). The spec files the page was built from: `_work/2026-11/findings-build/` |
| Avatar | Not written |
| Still unread | 97,521 posts (10 April to 24 October), and all replies by people other than the poster (4.19 million downloaded, on disk only) |

## Not usable for conclusions (marked 2026-11-18)

The Reddit posts read for this niche were chosen by a word list we wrote ourselves
(`_tools/history/shared/niche_filter.py`), and posts that mention buying, paid tools or
brands were ranked first. Posts that describe the problem in other words were never seen.

- **Still good:** the download. It is complete and has no keyword in it
  (`../new-and-expecting-mothers/reddit/raw/reddit-2026/`), so nothing needs downloading
  again. The quotes are real and checked word for word, so they can be used as her words.
- **Not to be used:** the counts, the evidence file, and anything that says what is common
  or central for her.
- **What happens next:** the selection and reading are redone by the method being proven on
  `baby-development` (random sample of everything first, word list from her words after).
  Whether and when this niche is redone is the owner's decision.

For this niche in detail: the brief named a candidate product, only about 1,785 of
24,326 matched posts were read (the top-ranked group's last two months, then all posts
first set aside for hard subjects), and the two findings pages and `her-words.md` rest on
that reading. They are superseded and stay unreviewed.

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
| `evidence/` | `evidence.md`: the quotes sorted under themes with conclusions (44,500 words, cites 1,086 quotes); `who-she-is.md`: the same quotes read for who she is (cites all 2,970); counts; readers' notes; the unfilter report | 2026-11-17 | Current |

Findings (the short version), all written 2026-11-18 and not yet reviewed by the owner:
`findings/who-she-is.md` from `evidence/who-she-is.md`;
`findings/what-hurts-and-what-she-wants.md` from `evidence/evidence.md`; and
`her-words.md`, her phrases from both pages.

## The four questions

| Question | Answered from | State |
|---|---|---|
| 1. Who is she, and what is her life like? | `evidence/who-she-is.md`, `statistics/` | **Partly answered (2026-11-17).** Her daily life, who has a say, what she believes and how she sees herself: answered from the quotes. Her age, income, education and country: the quotes say almost nothing; `statistics/` gives national averages for all mothers, not this buyer. mamiVio's own quiz data does not exist yet |
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

## Checking the October round

Run from this folder. The scripts already point at the `2026-10/` folders. All five must report the counts shown and no failures.

```
python3 -I _tools/check_ids.py                            2970 records, 0 duplicated
python3 -I _tools/verify_quotes.py                        2970 quotes, 0 failed
python3 -I _tools/verify_evidence_ids.py                  1086 ids cited, 0 unresolved; 1008 fragments, 0 failed
python3 -I _tools/audit.py read-v1 read-w2 read-w3        723 assigned, 0 unexplained
python3 -I _tools/verify_part.py quotes/2026-10 evidence/2026-10/who-she-is.md 0.05
                                                          ids mentioned 2970, quotes reproduced 120; OK
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

