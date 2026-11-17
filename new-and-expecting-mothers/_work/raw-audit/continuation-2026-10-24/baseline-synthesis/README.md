# Mamivio — global mother-and-baby research database

**State on 2026-10-24: expanded reading pass completed; broader queues remain.** The database contains **1,296 exact-source excerpts across 10 source classes**, including 878 additions to the original 418. The **977 language-bank entries** carry context and source links. Full reading includes **1,063 Reddit posts plus 449 OP replies and seven other comments, 605 complete visible forum discussions, 119 complete saved Q&A threads, and 219 original reviews**. Fifteen additional forum discussions have explicit safety boundaries. All eligible assigned reading is complete. [Exact ledger and remaining work](synthesis/session-report.md).

**Leading test:** a weekly baby-meal/lunch and preparation report for mothers who already have feeding information but lack a workable household routine. Confident cooks and experienced parents belong in the test. This replaces the earlier first-time/low-cooking restriction; it does not validate demand, a PDF format or profit. [Decision and falsification test](synthesis/niche-opportunities.md) · [Findings](synthesis/findings.md).

Start with those two documents, then [the language bank](synthesis/quote-index.md), [source map](sources/source-map.md), [competitors](competitors/README.md), [reader notes](synthesis/reader-notes.md), [counts](synthesis/counts.md) and [audit](synthesis/audit.md). The original pre-integration synthesis remains in `_raw/pre-integration-synthesis-2026-10-24/`.

The records include 1,075 original user/community excerpts, 155 legacy search-index extracts, 50 seller/resource descriptions, six advertising excerpts and 10 official-guidance excerpts. These are selected records, not counts of people, verified purchasers or prevalence. A reported paid Huckleberry analysis/plan is evidence of buying bundled personalized help; no Mamivio sale or standalone report-only purchase is verified. The owner supplied no existing customer data and selected English-speaking markets; launch country is unresolved.

Reddit collection covers 112,665 post records in July–December 2025 across nine communities, not a live census. The reading wave completed all 1,661 July A cards and all 1,031 initially kept originals, with 933 eligible contexts after full reading. A separate 39-post cohort brings distinct full reads to 1,063 after overlap is removed. Comments are missing for seven communities. **6,597 outside-July A candidates remain unhandled**, plus 625 card-dropped July A bodies and the larger B/C queues. Source provenance, license uncertainty and exact remaining paths are recorded; the full playbook definition of global completion is not claimed.

## Layout and evidence rules

`product/`: observed offer and funnel. `voice/*.jsonl`: exact excerpts. `sources/`: access, provenance, counts and unread material. `_raw/`: saved source responses before quoting. `competitors/`, `books/`, `ads-running/`: market evidence. `synthesis/`: interpretation citing quote ids and source documents. `_tools/`: reproducible capture, query and verification scripts. `scratchpad/<task>/`: isolated agent work.

Raw first; never invent quotes, review counts, prices, views, sales, prevalence or unread completion. Search-index extracts are explicitly marked and cannot count as full reads of original threads. Save HTTP/access failures. No captcha solving, bot-wall workarounds, cookie extraction or private-group access. Check robots instructions before bulk collection. Do not infer ad profitability from longevity.

Every quote has `id`, `source`, `url`, `date` (empty when unknown), `speaker`, `stage`, `type`, `themes`, `quote`, `context` (25 words maximum), `raw_file` relative to this folder. Add `segment`, `source_class`, `evidence_kind`, `engagement` when useful. No names or usernames in excerpt/context; no inference of age, gender, diagnosis or credentials. Quote ids are unique and never reused. Copy exact wording; trim only with ` […] `. No rebuilding cited raw/corpus files. Run `_tools/verify_quotes.py` after every batch. Counts describe selected evidence, never market prevalence.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `parent_unspecified`, `partner`, `relative_caregiver`, `recovered_parent`, `gave_up_parent`, `advisor`, `professional`, `reviewer`, `skeptic`. Use parent_unspecified if the author does not identify as mother. An advisor's instructions are not verified clinical guidance. The other side includes partners, daycare caregivers and mothers who stopped following programs.

Stages: `pregnancy_early`, `pregnancy_late`, `newborn_0_6_weeks`, `baby_6_16_weeks`, `baby_4_6_months`, `baby_6_12_months`, `toddler`, `return_to_work`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`.

Seed themes: `information_overload`, `conflicting_advice`, `late_night_search`, `first_time_parent`, `not_enough_time`, `maternal_guilt`, `tummy_time`, `floor_play`, `milestone_comparison`, `corrected_age`, `flat_head_concern`, `feeding_reflux`, `contact_naps`, `sleep_routines`, `sleep_training_values`, `wake_windows`, `first_solids`, `allergen_introduction`, `choking_fear`, `meal_planning`, `food_budget`, `pumping_schedule`, `return_to_work`, `daycare_handoff`, `bottle_refusal`, `milk_supply_concern`, `pregnancy_activity`, `birth_preparation`, `postpartum_recovery`, `household_support`, `partner_mental_load`, `no_village`, `second_baby`, `twins`, `skepticism`, `subscription_fatigue`, `price_value`, `personalization`, `free_alternatives`, `clinical_referral`, `language_access`, `privacy`. Add tags only when needed and document them.

## Lines not to cross

Do not use accounts centered on self-harm, abuse, acute crises, pregnancy loss or infant death as marketing material. Do not quote minors as target customers. Keep exclusions in a neutral ledger without republishing identifying crisis content. Do not turn ordinary variation into a diagnosis or promise earlier milestones, safe allergy testing, a milk-supply cure, infant sleep guarantees or pregnancy exercise clearance. Age alone cannot assess a child. Separate awake supervised tummy time from safe sleep. Reports need explicit escalation boundaries and qualified review where they touch health. Any legal, platform-policy or health recommendation must use current primary guidance; country differences matter.

## Query

`python3 mamivio.com/research/global/_tools/query.py --theme tummy_time --type pain`

`python3 mamivio.com/research/global/_tools/query.py --stats`

`python3 mamivio.com/research/global/_tools/verify_quotes.py`

`python3 mamivio.com/research/global/_tools/verify_findings.py`

## Resuming

Read `synthesis/session-report.md`, `sources/not-harvested.md` and the source-specific ledgers before launching more work. Use fresh capture names and quote prefixes. Do not rebuild cited corpora or rerun append-only readers. All retained raw sources are available for version control; none is ignored. No commit was made. Scripts copied for future harvesting do not authorize collection from a restricted route; saved policies take precedence.

## Querying original evidence

`python3 mamivio.com/research/global/_tools/query.py --original-only --exclude-restricted --theme-group solids_workload`

`python3 mamivio.com/research/global/_tools/query.py --source-class reddit_archive --theme-group personalized_information`

`python3 mamivio.com/research/global/_tools/query.py --theme-group gear_and_registry --type objection`

Other groups: `household_coordination`, `first_trips`, `leave_and_childcare`, `free_and_DIY`, `portable_formats`. Exact theme/source/speaker/type filters still work. `--stats` separates source class and evidence kind. Research-only records are marked visibly and excluded from the generated language bank; the remaining records are not automatically suitable advertising claims.

Speaker labels describe the quoted role. `gave_up_parent` means someone who stopped a particular tool/method, never a judgment about parenting. `recovered_parent` has no records; no clinical-recovery market is inferred. Source notes retain added themes and richer reader labels where useful. Do not infer gender or first-child status from pregnancy, a partner reference, or a reply's original poster.

For continuation use `synthesis/coverage.json` and the named final inventories. Earlier reader/capture indexes are frozen snapshots, not current whole-project read status. New source waves need new filenames/prefixes, full source reads and renewed audits. No commits were made; unrelated workspace files were left unchanged.
