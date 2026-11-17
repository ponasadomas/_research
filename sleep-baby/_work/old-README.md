# Mamivio — Baby and toddler sleep, 0–36 months

**State on 2026-11-17: the 2026-11-16 re-reading is integrated. UR01–UR24 completed 7,122/7,122 omission/review reads; 8,772 verified new quotes (6,213 rows quoted, 909 with no new quote and a ledger reason; 0 missing/unfinished). Seven digests are reconciled in findings: 4,407 distinct cited ids, including 2,757 re-reading quotes reproduced completely; all 1,650 earlier cited ids retained. The rebuilt corpus has 34,191 quotes in 88 voice files (33,957 Reddit + 234 reviews), 0 active restrictions. All 1,641 safety-intake posts are read. Remaining ordinary unread Reddit: A 5,540, B 27,352, C 7,324; 1,455 removed/deleted bodies remain unavailable. Public book/app reviews and 26 competitor teardowns are already present; browser walks, wider sources and niche Ad Library searches remain as recorded in findings §13. Counts, source limits and checks: `synthesis/counts.md`, `sources/reddit.md`, `synthesis/unfilter-report.md`.**

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (original Reddit `sbNN-NNNN`, re-reading `sbuNN-NNNN`, reviews `sbr1-NNNN`; never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `new_mother`, `experienced_mother`, `expecting_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `newborn_0_8_weeks`, `baby_2_4_months`, `regression_4_months`, `baby_5_8_months`, `baby_9_12_months`, `toddler_12_24_months`, `toddler_24_36_months`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): `night_wakings`, `contact_naps`, `short_naps`, `wake_windows`, `early_waking`, `bedtime_battle`, `regression_4_month`, `feeding_to_sleep`, `dream_feed`, `night_weaning`, `cosleeping`, `bedsharing`, `room_sharing`, `transition_to_cot`, `sleep_training_values`, `cry_it_out`, `ferber`, `gentle_method`, `chair_method`, `pick_up_put_down`, `consistency_failure`, `partner_split_nights`, `partner_disagreement`, `daycare_naps`, `nap_transition`, `drop_nap`, `sleep_props`, `pacifier`, `swaddle_transition`, `white_noise`, `schedule_rigidity`, `sleep_consultant`, `course_purchase`, `app_tracking`, `information_overload`, `conflicting_advice`, `maternal_exhaustion`, `resentment`, `guilt`, `comparison_other_babies`, `safe_sleep_fear`, `money_back`, `price_value`, `personalization`.

The other side of the door: The partner who disagrees on sleep training; the daycare carer whose naps 'just work'; the parents who refused sleep training and are content; the ones who paid for a course and quit.

## Research principle — 2026-11-16

Research records what people actually say and do, in their own words, whatever the subject; nothing is withheld, excluded, softened or paraphrased away because of its subject. Readers may label a quote, but it remains ordinary evidence and is quoted like any other. What is usable in copy is the owner's decision, made later; it is never a research decision.

Counts are counts of quotes chosen, never people or prevalence. Preserve source provenance and report speakers' beliefs as their beliefs.

**Unfilter update:** all 689 historically marked quotes remain ordinary evidence. The subsequent 7,122-row re-reading/review queue is complete and its 8,772 quotes are integrated through seven digests. `scratchpad/unfilter-reread/queue.tsv` and reader ledgers are preserved historical provenance; a queued reason is no longer a statement that the source is unread. The final section of `synthesis/unfilter-report.md` records completion and the remaining ordinary unread material.

## Resuming

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
