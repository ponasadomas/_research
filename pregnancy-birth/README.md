# pregnancy-birth

Pregnancy, birth preparation and the first weeks. Research on this buyer, collected October to November 2026 while choosing a
niche for mamiVio. The questions it set out to answer are in `brief.md`.
Rules for all research: `../README.md`.

## What is here

| Folder | What was collected | State |
|---|---|---|
| `ads/` | nothing in this niche's own folder | Not collected here. The October 2026 Ad Library sweep covered all mother-and-baby niches at once and belongs to the niche-selection research |
| `books/` | store pages and reader reviews of books (144 saved files) | 43 quotes |
| `competitors/` | seller pages (199 saved files) | 29 notes |
| `reddit/` | 10274 posts handed to readers in the first reading, plus the 2026-11-16 re-reading of posts a subject filter had kept out; all from the shared archive | 34065 quotes. What is still unread is in `reddit/reddit.md` |
| `reviews/` | app and course reviews (222 saved files) | 238 quotes; 11 of the saved files are empty |
| `sales-letters/` | nothing | Not collected |
| `youtube/` | nothing | Not collected |
| `quotes/` | 34346 quotes, one record each, in 113 files; `merged/all.jsonl` is a generated copy | Every quote checked against its source |
| `evidence/` | `evidence.md`: the quotes sorted under themes with conclusions (941,873 words, cites 11,273 quotes); counts; readers' notes; the unfilter report; 13 theme digests from the re-reading | Current as of 2026-11-17 |

Findings page (the short one): not written. It will be
`~/GitHub/_home/library/avatars/pregnancy-birth/findings/`. `evidence/evidence.md` is too long to read end to end; start with its last section, on what the re-reading changed, and with the digests.

## The four questions

| Question | Answered from | State |
|---|---|---|
| 1. Who is she, and what is her life like? | nothing collected for it | **Not answered.** Pieces are scattered through the Reddit quotes |
| 2. What hurts, what does she want, and how does she say it? | `reddit/` | Answered; one source only |
| 3. What is she buying, what does she pay, and how did it go? | `reviews/`, `books/` | Half answered. Reviews were read (238 quotes from apps and courses, 43 from books), but nobody first mapped what she spends on, so the products were picked without it |
| 4. Who is selling to her, and what is working? | `competitors/`, the Ad Library sweep | Partly: 29 competitor notes; ads only in the shared sweep |

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
python3 -I _tools/check_ids.py                  34346 records, 34346 distinct ids, 0 duplicated
python3 -I _tools/verify_quotes.py              TOTAL 34346 quotes, 0 failed, 0 with a missing raw file
python3 -I _tools/verify_evidence_ids.py        11273 distinct ids cited, 0 unresolved; 10180 verbatim fragments paired with an id, 0 failed
python3 -I _tools/audit.py read-v1 read-w2 read-w3
                                                10274 assigned, 0 unexplained
```

`_tools/history/` holds the scripts and agent briefs used to collect and read this
material. They are kept as a record and still use the old paths; they are not meant to
be run from here.

## Paths in older files

This folder was moved here on 2026-11-17 from `ads/mamivio.com/research/pregnancy-birth/`.
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
| `../global/`, `../main/` | `../new-and-expecting-mothers/` once that research is moved |

## Quote schema

Every record: `id` (original `pbNN-NNNN`, reviews `pbr1-NNNN`, re-reading `pbuNN-NNNN`; never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `trying`, `first_trimester`, `second_trimester`, `third_trimester`, `birth`, `newborn_0_2_weeks`, `newborn_2_8_weeks`, `second_pregnancy`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `evidence/reader-notes-*.md`): `first_pregnancy`, `second_pregnancy`, `pregnancy_with_toddler`, `nausea`, `fatigue`, `back_pain`, `pelvic_pain`, `sleep_in_pregnancy`, `exercise_in_pregnancy`, `exercise_fear`, `weight_gain`, `gestational_diabetes_question`, `diet_rules`, `what_to_buy`, `registry`, `hospital_bag`, `birth_plan`, `birth_fear`, `tokophobia`, `epidural_decision`, `induction`, `c_section`, `vbac`, `hypnobirthing`, `birth_course`, `perineal_prep`, `doula`, `partner_role`, `birth_trauma_story`, `first_two_weeks`, `postpartum_recovery`, `visitors`, `maternity_leave`, `work_in_pregnancy`, `information_overload`, `app_tracking`, `week_by_week`, `comparison_other_pregnancies`, `previous_birth`, `personalization`, `price_value`.

The other side of the door: Partners; midwives, doulas and OBs; second-time mothers looking back on the first; mothers who say preparation didn't matter.

