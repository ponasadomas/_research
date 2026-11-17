# Mamivio — Baby development and play, 0–24 months, age-selected

**State on 2026-11-16:** 2,970 voice quotes in twelve files: 2,806 Reddit and 164 public app/book reviews. UR01–UR05 completed all 1,169 assigned previously excluded posts, writing 1,182 verified quotes; all 1,182 have now been read and integrated into [`synthesis/findings.md`](synthesis/findings.md), which cites 1,086 distinct ids, including 240 UR ids, and adds twelve evidence subsections plus a dated change section. The 237 formerly restricted ids (218 Reddit, 19 reviews) remain ordinary evidence; active restrictions are zero. Both historical safety queues are covered. Four earlier extraction omissions outside the assignments remain explicitly named in [`synthesis/unfilter-report.md`](synthesis/unfilter-report.md); ordinary unread queues are reconciled in [`sources/reddit.md`](sources/reddit.md). Historical ledgers and reader notes record earlier runs and do not govern future research. Plan for all five builds: [`../PLAN-2026-10-25.md`](../PLAN-2026-10-25.md).

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (prefix `dvNN-NNNN`, never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `newborn_0_8_weeks`, `baby_2_4_months`, `baby_4_6_months`, `baby_6_9_months`, `baby_9_12_months`, `toddler_12_18_months`, `toddler_18_24_months`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): `what_to_do_all_day`, `awake_time`, `tummy_time`, `tummy_time_hate`, `floor_play`, `rolling`, `sitting`, `crawling`, `pulling_up`, `walking`, `first_words`, `babbling`, `fine_motor`, `milestone_comparison`, `milestone_anxiety`, `corrected_age`, `pediatrician_checkup`, `cdc_milestones`, `wonder_weeks`, `leaps`, `screen_time`, `toys_too_many`, `montessori`, `play_ideas`, `boredom_mum`, `maternal_guilt`, `not_enough_play`, `container_time`, `baby_classes`, `app_tracking`, `information_overload`, `conflicting_advice`, `reassurance_seeking`, `social_comparison`, `grandparent_comments`, `early_intervention_question`, `personalization`, `price_value`.

The other side of the door: Grandparents and in-laws who compare; paediatricians and physios; parents who say 'babies just develop'; Montessori purists; buyers of apps who cancelled.

## Research principle

Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.

## Resuming

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
