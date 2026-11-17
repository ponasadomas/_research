# Mamivio — global mother-and-baby research database

**State on 2026-10-24 — research reopened at owner request:** additional original Reddit/forum/oblique collection is active; the earlier recommendation is being reassessed. See `sources/deepening-plan.md`. Initial snapshot:  418 verified excerpts across six source classes; 34 competitor/substitute notes from 41 successful page reads; 216 complete original review units read; 16 Meta Ad Library searches, 63 on-niche ids retained; 13 adjacent book titles. Initial evidence database audited; the playbook's full definition of done is **not met** because main-community bulk access and broad YouTube/comment coverage are missing. No owner customer data supplied, no Mamivio purchases or price tests observed. See `synthesis/session-report.md` for the exact ledger, verification and unread inventory.

Start with `synthesis/findings.md`, then `synthesis/niche-opportunities.md`, `synthesis/quote-index.md`, `competitors/README.md` and `sources/source-map.md`. The playbook is `templates/00 - Deep Research Playbook.md`; SYD scripts were copied into `_tools/` and will be adapted here.

The leading experiment is a short first-month solids shopping/preparation report for mothers with little cooking routine; first-time-mother and recruitment-age restrictions are hypotheses. Existing apps and 28-day PDFs already cover much of this job. Late-pregnancy household coordination is the leading alternative. Neither is commercially validated. The owner chose English-speaking markets; country remains a separate launch decision.

The 418 records comprise 192 original app-review excerpts, 14 original book-review excerpts, 155 partial community-index excerpts, 43 offer/resource descriptions, 10 professional-guidance excerpts and four advertising excerpts. **206 original-review excerpts are not 206 verified purchasers.** All 62 kept community extracts were read, but zero original community threads were read. These distinctions remain attached to records and the generated language bank.

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

Read `synthesis/session-report.md`, `sources/not-harvested.md` and the source-specific ledgers before launching more work. Use fresh capture names and quote prefixes. Do not rebuild cited corpora or rerun append-only readers. All committed-capable raw sources are retained and none is ignored. No commit was made. Scripts copied for future harvesting do not authorize collection from a restricted route; saved policies take precedence.
