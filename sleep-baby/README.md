# sleep-baby

Baby and toddler sleep, 0–36 months. Research on this buyer, collected October to November 2026 while choosing a
niche for mamiVio. The questions it set out to answer are in `brief.md`.
Rules for all research: `../README.md`.

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

## What is here

| Folder | What was collected | State |
|---|---|---|
| `ads/` | nothing in this niche's own folder | Not collected here. The October 2026 Ad Library sweep covered all mother-and-baby niches at once and belongs to the niche-selection research |
| `books/` | store pages and reader reviews of books (140 saved files) | 67 quotes |
| `competitors/` | seller pages (171 saved files) | 26 notes |
| `reddit/` | 8747 posts handed to readers in the first reading, plus the 2026-11-16 re-reading of posts a subject filter had kept out; all from the shared archive | 33957 quotes. What is still unread is in `reddit/reddit.md` |
| `reviews/` | app and course reviews (113 saved files) | 167 quotes |
| `sales-letters/` | nothing | Not collected |
| `youtube/` | nothing | Not collected |
| `statistics/` | nothing | Not collected |
| `forums/`, `marketplaces/`, `official-guidance/` | nothing | Not collected in this niche. The niche-selection research in `../new-and-expecting-mothers/` has all three for the whole market |
| `quotes/` | 34191 quotes, one record each, in 88 files; `merged/all.jsonl` is a generated copy | Every quote checked against its source |
| `evidence/` | `evidence.md`: the quotes sorted under themes with conclusions (320,167 words, cites 4,407 quotes); counts; readers' notes; the unfilter report; 7 theme digests from the re-reading | Current as of 2026-11-17 |

Findings page (the short one): not written. It will be
`findings/` in this folder. `evidence/evidence.md` is too long to read end to end; start with its last section, on what the re-reading changed, and with the digests.

## The four questions

| Question | Answered from | State |
|---|---|---|
| 1. Who is she, and what is her life like? | nothing collected for it | **Not answered.** Pieces are scattered through the Reddit quotes |
| 2. What hurts, what does she want, and how does she say it? | `reddit/` | Answered; one source only |
| 3. What is she buying, what does she pay, and how did it go? | `reviews/`, `books/` | Half answered. Reviews were read (167 quotes from apps and courses, 67 from books), but nobody first mapped what she spends on, so the products were picked without it |
| 4. Who is selling to her, and what is working? | `competitors/`, the Ad Library sweep | Partly: 26 competitor notes; ads only in the shared sweep |

## Reddit originals are not in this folder

The Reddit posts were downloaded once for all mother-and-baby niches and five niches
picked their posts from that one archive. It is kept once, at
`../new-and-expecting-mothers/reddit/raw/reddit-2026/`. Every Reddit quote here points
into it, so this folder cannot be checked without that one beside it. What this niche
selected from the archive, and who read what, is in `_work/reddit-selection/` and
`_work/reading-ledgers/`.

## Checking

Run from this folder. All four must report these counts and no failures.

```
python3 -I _tools/check_ids.py                  34191 records, 34191 distinct ids, 0 duplicated
python3 -I _tools/verify_quotes.py              TOTAL 34191 quotes, 0 failed, 0 with a missing raw file
python3 -I _tools/verify_evidence_ids.py        4407 distinct ids cited, 0 unresolved; 4235 verbatim fragments paired with an id, 0 failed
python3 -I _tools/audit.py read-v1a read-v1b read-w2 read-w3
                                                8747 assigned, 0 unexplained
```

`_tools/history/` holds the scripts and agent briefs used to collect and read this
material. They are kept as a record and still use the old paths; they are not meant to
be run from here.

## Paths in older files

This folder was moved here on 2026-11-17 from `ads/mamivio.com/research/sleep-baby/`.
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

Every record: `id` (original Reddit `sbNN-NNNN`, re-reading `sbuNN-NNNN`, reviews `sbr1-NNNN`; never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `new_mother`, `experienced_mother`, `expecting_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `newborn_0_8_weeks`, `baby_2_4_months`, `regression_4_months`, `baby_5_8_months`, `baby_9_12_months`, `toddler_12_24_months`, `toddler_24_36_months`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `evidence/reader-notes-*.md`): `night_wakings`, `contact_naps`, `short_naps`, `wake_windows`, `early_waking`, `bedtime_battle`, `regression_4_month`, `feeding_to_sleep`, `dream_feed`, `night_weaning`, `cosleeping`, `bedsharing`, `room_sharing`, `transition_to_cot`, `sleep_training_values`, `cry_it_out`, `ferber`, `gentle_method`, `chair_method`, `pick_up_put_down`, `consistency_failure`, `partner_split_nights`, `partner_disagreement`, `daycare_naps`, `nap_transition`, `drop_nap`, `sleep_props`, `pacifier`, `swaddle_transition`, `white_noise`, `schedule_rigidity`, `sleep_consultant`, `course_purchase`, `app_tracking`, `information_overload`, `conflicting_advice`, `maternal_exhaustion`, `resentment`, `guilt`, `comparison_other_babies`, `safe_sleep_fear`, `money_back`, `price_value`, `personalization`.

The other side of the door: The partner who disagrees on sleep training; the daycare carer whose naps 'just work'; the parents who refused sleep training and are content; the ones who paid for a course and quit.

