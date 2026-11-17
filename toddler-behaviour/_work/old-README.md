# Mamivio — Toddler behaviour and potty training, 1–4 years

**State — 2026-11-16: re-reading integrated and verified.** All 2,647 recovery assignments were read; all 3,489 recovered quotes and nine ledger conclusions were read for synthesis. The merged corpus contains **12,782 quotes** (12,620 Reddit + 162 review quotes), across 37 voice files. Findings cite **2,058 distinct bracketed quote ids**, including **379 recovered ids**; all 1,703 earlier id mentions are retained. Added 24 topical subsections and the dated change log. Checks: 0 unresolved ids, 0 duplicate ids, 0 source-verification failures, 0 unexplained original reading assignments. No recovery row is unread or missing. Ordinary unread research remains: 10,431 tier-B posts, 3,174 tier-C posts and 2,661 nonqueued tier-A drops; 982 removed/deleted bodies are unavailable. Current records: `synthesis/counts.md`, `sources/reddit.md`, `sources/reviews.md`, `synthesis/unfilter-report.md`. Plan for all five builds: [`../PLAN-2026-10-25.md`](../PLAN-2026-10-25.md).

Historical collection: three Reddit waves (2,597 + 2,769 + 3,793 quotes), 134 RV1 review quotes, 27 competitor notes covering 34 sellers. The recovery adds 3,461 Reddit + 28 review quotes. Counts of quotes are never counts of people.

Built with `templates/00 - Deep Research Playbook.md`. `../global/` is a frozen earlier database; cite its ids as `[id]` only where they are re-verified, never copy its quotes into `voice/`.

## Layout

`product/` the brief · `sources/` one note per source with a ledger · `_raw/` untouched source text (shared Reddit lives in `../_shared/_raw/`) · `voice/*.jsonl` verbatim quotes · `competitors/` teardowns · `ads-running/` Ad Library write-ups · `books/` · `synthesis/` findings, quote index, reader notes, counts · `_tools/` scripts and agent briefs · `scratchpad/<prefix>/` one folder per agent.

## Quote schema

Every record: `id` (prefix `tbNN-NNNN`, `tbr1-NNNN` or recovery `tbuNN-NNNN`, never reused), `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`, `quote` (verbatim, trims only with ` […] `), `context` (≤25 words), `raw_file` (relative to this folder). Optional: `segment`, `source_class`, `engagement`. No usernames. No inference of age, gender or diagnosis. Legacy `restricted` fields and tags in original records are historical descriptive metadata only; they never affect access, quotation or checks. The merged copy sets `restricted` to false and records the old list as `formerly_restricted`.

## Vocabulary

Speakers: `new_mother`, `experienced_mother`, `recovered_parent`, `parent_unspecified`, `partner`, `relative_caregiver`, `advisor`, `professional`, `reviewer`, `skeptic`, `gave_up_parent`. Use `parent_unspecified` unless the author identifies as a mother.

Stages: `toddler_12_18_months`, `toddler_18_24_months`, `toddler_2_3_years`, `preschool_3_4_years`, `new_sibling`, `daycare_start`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`, `purchase`, `price_signal`. `purchase` = the author says they bought or paid for something for this problem; `price_signal` = what they say it was worth.

Seed themes (agents may add; document additions in `synthesis/reader-notes.md`): `tantrum`, `public_meltdown`, `hitting`, `biting`, `throwing`, `not_listening`, `defiance`, `no_phase`, `transitions`, `bedtime_battle`, `screen_time`, `picky_eating`, `new_sibling`, `daycare_behaviour`, `daycare_report`, `potty_readiness`, `potty_regression`, `potty_refusal`, `poop_withholding`, `accidents`, `night_dryness`, `potty_method_3_day`, `pullups`, `gentle_parenting`, `gentle_parenting_backlash`, `time_out`, `consequences`, `scripts`, `big_little_feelings`, `good_inside`, `partner_disagreement`, `grandparent_undermining`, `maternal_rage`, `maternal_guilt`, `shame_in_public`, `comparison_other_toddlers`, `information_overload`, `course_purchase`, `price_value`, `personalization`.

The other side of the door: Daycare teachers; the partner who is stricter or softer; grandparents; parents who reject gentle parenting; BLF and Good Inside buyers who cancelled.

## Research principle — owner ruling, 2026-11-16

Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label a quote, but it remains ordinary evidence and is quoted like any other. What is usable in copy is the owner's decision, made later; it is never a research decision.

Counts are counts of quotes chosen, never of people or prevalence.

## Resuming

Read `synthesis/unfilter-report.md` and “What the 2026-11-16 re-reading changed” at the end of `synthesis/findings.md` for the completed recovery and current conclusions. Historical reader notes and source ledgers document omissions; their old subject exclusions have no effect. The completed queue is `scratchpad/unfilter-reread/queue.tsv`; its 2,647 rows are accounted for in `sources/reddit-reading-ur01.md` through `ur09.md`. Do not rebuild original voice files or reuse retired ids.

Read this state line, `sources/*.md` ledgers and `synthesis/reader-notes.md`. Never rebuild a corpus once quotes cite it; never re-run an agent that appends to an existing voice file.
