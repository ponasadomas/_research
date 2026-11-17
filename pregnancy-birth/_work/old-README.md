# Mamivio — Pregnancy, birth preparation and the first weeks

**State on 2026-11-17:** Re-reading and findings integration are complete under the owner's 2026-11-16 ruling. All 11,880 queued rows were read by UR01–UR40: 11,539 supplied 15,768 new quotes; 341 supplied no new quote, with ledger reasons. The full corpus is 34,346 quotes in 113 voice files, rebuilt into `voice-merged/all.jsonl`. Findings cite 11,273 distinct ids, including 7,961 re-reading ids; all 3,366 earlier explicit ids remain. All 13 digests are integrated, with every indexed money/request passage retained and conclusions revised in place. No assigned re-reading remains unread. The ordinary backlog is 56,212 available A/B/C posts plus 5,838 unavailable bodies; details and other source gaps are in `sources/reddit.md` and findings §13. Counts describe quotes, never people. See `synthesis/unfilter-report.md` for closure and checks. Plan for all five builds: [`../PLAN-2026-10-25.md`](../PLAN-2026-10-25.md).

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (original `pbNN-NNNN`, reviews `pbr1-NNNN`, re-reading `pbuNN-NNNN`; never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `trying`, `first_trimester`, `second_trimester`, `third_trimester`, `birth`, `newborn_0_2_weeks`, `newborn_2_8_weeks`, `second_pregnancy`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): `first_pregnancy`, `second_pregnancy`, `pregnancy_with_toddler`, `nausea`, `fatigue`, `back_pain`, `pelvic_pain`, `sleep_in_pregnancy`, `exercise_in_pregnancy`, `exercise_fear`, `weight_gain`, `gestational_diabetes_question`, `diet_rules`, `what_to_buy`, `registry`, `hospital_bag`, `birth_plan`, `birth_fear`, `tokophobia`, `epidural_decision`, `induction`, `c_section`, `vbac`, `hypnobirthing`, `birth_course`, `perineal_prep`, `doula`, `partner_role`, `birth_trauma_story`, `first_two_weeks`, `postpartum_recovery`, `visitors`, `maternity_leave`, `work_in_pregnancy`, `information_overload`, `app_tracking`, `week_by_week`, `comparison_other_pregnancies`, `previous_birth`, `personalization`, `price_value`.

The other side of the door: Partners; midwives, doulas and OBs; second-time mothers looking back on the first; mothers who say preparation didn't matter.

## Research principle

Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.

## Resuming

This principle supersedes subject restrictions in historical reader notes, ledgers, scratch inputs and run logs; those records describe what happened and must not be reused as instructions. Do not rerun historical extraction builders to reconstruct voice files.

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
