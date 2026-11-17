# Mamivio — The mother's own sleep

**State on 2026-11-16: UR01–UR04 re-reading complete and integrated. All 918 assigned rows (905 Reddit posts/units and 13 saved reviews) were read; 1,238 verified quotes and all four closing ledger sections were read for the synthesis. The current corpus and rebuilt merged copy contain 4,243 quotes (4,187 Reddit + 56 reviews) in fourteen voice files, with zero active restrictions. Findings cite 1,583 distinct ids, including 256 re-reading quotes reproduced in full, and retain all 1,327 previously cited ids. Eleven new evidence subsections and a dated closing comparison record the changed conclusions. No assigned re-reading remains; ordinary unread queues and archive limitations are reconciled in `sources/reddit.md`, `synthesis/counts.md` and the closing section of `synthesis/unfilter-report.md`. Product positioning remains untested.** Plan for all five builds: [`../PLAN-2026-10-25.md`](../PLAN-2026-10-25.md).

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (original Reddit `smNN-NNNN`, re-reading `smuNN-NNNN`, reviews `smr1-NNNN`; never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `pregnancy_first`, `pregnancy_second`, `pregnancy_third`, `newborn_0_8_weeks`, `baby_2_6_months`, `baby_6_12_months`, `toddler`, `return_to_work`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): `pregnancy_insomnia`, `cant_sleep_when_baby_sleeps`, `hypervigilance`, `listening_for_baby`, `racing_mind`, `night_feeds_split`, `partner_sleeps_through`, `resentment`, `shift_system`, `pumping_at_night`, `formula_for_sleep`, `return_to_work_exhausted`, `cumulative_deprivation`, `naps_for_mum`, `caffeine`, `sleep_aids_question`, `melatonin_question`, `cbti`, `apps_meditation`, `night_nanny`, `family_help`, `no_village`, `body_pain`, `physical_discomfort`, `pregnancy_pillow`, `bathroom_trips`, `anxiety_at_night`, `maternal_guilt`, `self_care_guilt`, `identity_loss`, `baby_in_room`, `bedsharing_mum_sleep`, `white_noise_for_mum`, `early_waking_mum`, `information_overload`, `price_value`, `personalization`.

The other side of the door: The partner who sleeps through or works nights; grandparents who offer help; mothers who say they slept fine; professionals (sleep clinicians, doulas).

## Research principle

Research records what people actually say and do, in their own words, whatever the subject; nothing is withheld, excluded, softened or paraphrased away because of its subject. Readers may label material, but every quote remains ordinary evidence and is quoted like any other. What is usable in copy is the owner's decision, made later; it is never a research decision.

## Resuming

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
