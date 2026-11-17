# Mamivio — global mother-and-baby research database

**State on 2026-10-24: declared continuation reading completed; broader queues remain.** Baseline committed as `2613feb3`; this continuation follows it. The database contains **1,944 exact-source excerpts across 10 source classes**, **648 added after the committed 1,296-record baseline**, and **1,113 distinct language-bank entries** with context/source links. Counts describe selected records, not people, independent purchasers or prevalence.

**Leading test:** A baby-lunch preparation and caregiver handoff report for mothers already feeding baby meals, using daycare, a nanny or another willing caregiver. This narrows the earlier general weekly-meal idea; a purchase/use test must still establish demand, format and cost. [Decision and falsification test](synthesis/niche-opportunities.md) · [Findings](synthesis/findings.md).

Cumulative full reading: **5,879 distinct Reddit post IDs + 2,149 identifiable OP replies + 43 exact other comments; 605 complete visible forum discussions; 119 complete saved Q&A threads; 219 original reviews**. Fifteen additional forum discussions have explicit partial safety boundaries. All retained originals in the declared assignments are complete. [Exact session ledger](synthesis/session-report.md) · [Coverage](synthesis/coverage.json).

All 8,284 A candidates are now handled: 8,258 cards manually triaged, plus 26 outside-July candidates already fully read in the payment cohort. The continuation covered all 6,597 remaining cards and all 4,689 new keeps; the independent July BabyLedWeaning B comparison added 126 full posts. A duplicate audit fully inspected one additional card-dropped original; its zero available OP replies were verified. **A further 2,532 card-dropped A bodies, 51,126 B bodies and 38,463 C bodies remain unread; 14,665 bodies are unavailable.** Current exact inventories are in `_raw/reddit-deep/continuation-v1/`; baseline final inventories remain frozen. Reddit coverage is July–December 2025, not live; comments are missing for seven communities.

Start with the decision/findings, then [language bank](synthesis/quote-index.md), [source map](sources/source-map.md), [competitors](competitors/README.md), [reader notes](synthesis/reader-notes.md), [counts](synthesis/counts.md), and [audit](synthesis/audit.md). The initial synthesis and committed-baseline synthesis are preserved separately under `_raw/` and the continuation audit directory.

There are 1,723 original user/community excerpts, 155 legacy search extracts, 50 seller/resource descriptions, six advertising excerpts and 10 official-guidance excerpts. **67 records are research-only and excluded from the language bank**; other records still require editorial judgment. The owner supplied no customer data and chose English-speaking markets; launch country remains unselected. Reported app/book/service purchases and the clarified recipe/app/Q&A bundle do not verify a Mamivio sale, standalone customized-report transaction, accepted price, CAC or profit.

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

Read `synthesis/session-report.md`, `sources/not-harvested.md` and the source-specific ledgers before launching more work. Use fresh capture names and quote prefixes. Do not rebuild cited corpora or rerun append-only readers. All retained raw sources are available for version control; none is ignored. The baseline was committed as `2613feb3`; new continuation work follows it. Scripts copied for future harvesting do not authorize collection from a restricted route; saved policies take precedence.

## Querying original evidence

`python3 mamivio.com/research/global/_tools/query.py --original-only --exclude-restricted --theme-group solids_workload`

`python3 mamivio.com/research/global/_tools/query.py --source-class reddit_archive --theme-group personalized_information`

`python3 mamivio.com/research/global/_tools/query.py --theme-group gear_and_registry --type objection`

Other groups: `household_coordination`, `first_trips`, `leave_and_childcare`, `free_and_DIY`, `portable_formats`. Exact theme/source/speaker/type filters still work. `--stats` separates source class and evidence kind. Research-only records are marked visibly and excluded from the generated language bank; the remaining records are not automatically suitable advertising claims.

Speaker labels describe the quoted role. `gave_up_parent` means someone who stopped a particular tool/method, never a judgment about parenting. `recovered_parent` has no records; no clinical-recovery market is inferred. Source notes retain added themes and richer reader labels where useful. Do not infer gender or first-child status from pregnancy, a partner reference, or a reply's original poster.

For continuation use `synthesis/coverage.json` and the named final inventories. Earlier reader/capture indexes are frozen snapshots, not current whole-project read status. New source waves need new filenames/prefixes, full source reads and renewed audits. The baseline is committed; unrelated workspace files remain unchanged.
