# Mamivio — global mother-and-baby research database

**State on 2026-11-17: the re-reading and synthesis merge are complete for all 3,807 assigned units, to the extent of saved text.** Thirteen readers produced **4,829 verified new quotes**; all four digests are integrated into the evidence, conclusions and niche map. Of the assigned units, 3,747 added quotes; 60 added none (49 off topic, five duplicate/already quoted, six without usable text). No assigned saved text remains unread. Full originals, missing endings, images and comments are not reconstructed. [Completion and remaining gaps](synthesis/unfilter-report.md#re-reading-complete--2026-11-17) · [Recovery coverage](synthesis/reread-coverage.json).

**6,991 exact-source excerpts across 10 classes; 6,991 distinct language-bank/catalogue entries; every stored record included.** This is the earlier 2,162 plus 4,829 recovered records. Source-class tags place 6,729 records in community/review collections and 179 in `community_index`, alongside 67 competitor/resource/hosted/affiliate excerpts, six advertising and ten official-guidance excerpts. These platform classes also contain listing fragments, second-hand and creator/commercial speech; evidence-kind and reading-scope labels remain attached. Counts describe selected quote records, not independent people, buyers or prevalence; the recovery units were chosen because they had been excluded.

The [themed evidence](synthesis/evidence.md) reproduces **4,970 distinct complete quote fields**: all 141 earlier restored records plus every new quote. It also retains all **1,017 money-index records** and **2,038 request-index records** from the digests, including prospective/rejected fees, free offers, broader care questions and creator solicitations with their distinctions intact. The four conclusion files select the strongest evidence; their distinct-id counts are rebuilt in [counts](synthesis/counts.md).

**Research conclusion:** sleep still leads on observed paid tailoring; capability-matched play and specialist leave remain next. No standalone customized-report niche or price is validated. The interpretation now includes adult sleep, bodily/time limits, feeding transition and grief, trustworthy care, consent, recovery, reproductive autonomy and clinical access as substantive jobs. The main map’s competing ranking and unsupported sales/format assumptions are replaced by the same conditional global order. [Ranked recommendation](synthesis/niche-opportunities.md) · [Purchase audit](synthesis/purchase-evidence.md) · [Findings and dated changes](synthesis/findings.md#what-the-2026-11-17-re-reading-changed) · [Niche map](../main/synthesis/sub-niche-map.md).

Current reconciled Reddit reading is **8,614 distinct original post ids** (6,605 earlier plus 2,009 newly read originals); re-reading an already-read original does not increase that total. All available assigned saved replies were read, but the old totals of 2,150 identifiable OP replies and 43 other comments are historical counts rather than a new comment-id census. Current main-archive unread bodies are **801 A / 50,286 B / 38,459 C**, with 14,665 unavailable bodies. The separate commercial extension has **14,935 readable bodies unread** (238 card drops + 14,697 unmatched), 138 unavailable bodies and two absent comment sources. Seven main comment sources remain absent. The October inventory of 145,386 unread available comments is preserved as a snapshot; a new exact remainder has not been calculated because saved OP replies overlap it. [Current body differences](synthesis/reread-coverage.json) · [Frozen October coverage](synthesis/coverage.json).

The earlier 411 card-dropped JustParents discussions and all 231 unread posts in 15 partial MSE discussions were read in the recovery. The available saved text is now accounted for across 505 JustParents, 343 MSE and 183 GeoBaby captured discussions; deletion placeholders, absent images and incomplete listings are still limits. Q&A full reads rise from 119 to 228; 20 ordinary card drops and 907 unmatched questions remain outside the assignment. **56 listing-only discussions (17 GeoBaby, 39 MSE) remain unavailable in full.** Earlier review reading remains 299 original app/book reviews. No complete-live-thread claim is made.

The [October advertiser money map](synthesis/advertiser-money-map.md) remains a separate snapshot: 43 named Pages (29 active, 14 zero) and 604 complete retained ad-text reads, with no actual spend/profit figures. Formal seller-teardown coverage included 55 notes and 73 public offer/pricing/terms page reads, plus hosted/affiliate evidence recorded separately. No independent purchase of an inspected customized standalone report, delivered paid Mamivio output or owner customer data was supplied. [Source map](sources/source-map.md) · [Competitors](competitors/README.md).

The 2026-11-16 ruling first restored 141 stored records, then prompted this raw-source recovery. Earlier source ledgers, voice files, all four digests and raw material remain unchanged. Their old restrictions/counts document history, not current rules. The queue and October inventories are frozen inputs; current completion is in the closing report and recovery coverage. [Original decision inventory](scratchpad/unfilter-reread/decisions.tsv) · [Completed assignment queue](scratchpad/unfilter-reread/queue.tsv).

## Layout and evidence rules

`product/`: observed offer and funnel. `voice/*.jsonl`: exact excerpts. `sources/`: access, provenance, counts and unread material. `_raw/`: saved source responses before quoting. `competitors/`, `books/`, `ads-running/`: market evidence. `synthesis/`: interpretation citing quote ids and source documents. `_tools/`: reproducible capture, query and verification scripts. `scratchpad/<task>/`: isolated agent work.

Raw first; never invent quotes, review counts, prices, views, sales, prevalence or unread completion. Search-index extracts are explicitly marked and cannot count as full reads of original threads. Save HTTP/access failures. No captcha solving, bot-wall workarounds, cookie extraction or private-group access. Check robots instructions before bulk collection. Do not infer ad profitability from longevity.

Every quote has `id`, `source`, `url`, `date` (empty when unknown), `speaker`, `stage`, `type`, `themes`, `quote`, `context` (25 words maximum), `raw_file` relative to this folder. Add `segment`, `source_class`, `evidence_kind`, `engagement` when useful. No names or usernames in excerpt/context; no inference of age, gender, diagnosis or credentials. Quote ids are unique and never reused. Copy exact wording; trim only with ` […] `. No rebuilding cited raw/corpus files. Run `_tools/verify_quotes.py` after every batch. Counts describe selected evidence, never market prevalence.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `parent_unspecified`, `partner`, `relative_caregiver`, `recovered_parent`, `gave_up_parent`, `advisor`, `professional`, `reviewer`, `skeptic`. Use parent_unspecified if the author does not identify as mother. An advisor's instructions are not verified clinical guidance. The other side includes partners, daycare caregivers and mothers who stopped following programs.

Stages: `pregnancy_early`, `pregnancy_late`, `newborn_0_6_weeks`, `baby_6_16_weeks`, `baby_4_6_months`, `baby_6_12_months`, `toddler`, `return_to_work`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`.

Seed themes: `information_overload`, `conflicting_advice`, `late_night_search`, `first_time_parent`, `not_enough_time`, `maternal_guilt`, `tummy_time`, `floor_play`, `milestone_comparison`, `corrected_age`, `flat_head_concern`, `feeding_reflux`, `contact_naps`, `sleep_routines`, `sleep_training_values`, `wake_windows`, `first_solids`, `allergen_introduction`, `choking_fear`, `meal_planning`, `food_budget`, `pumping_schedule`, `return_to_work`, `daycare_handoff`, `bottle_refusal`, `milk_supply_concern`, `pregnancy_activity`, `birth_preparation`, `postpartum_recovery`, `household_support`, `partner_mental_load`, `no_village`, `second_baby`, `twins`, `skepticism`, `subscription_fatigue`, `price_value`, `personalization`, `free_alternatives`, `clinical_referral`, `language_access`, `privacy`. Add tags only when needed and document them.

## Research never censors

Research records what people actually say and do, in their own words, whatever the subject. The owner decides later what to use in copy; no subject is withheld from research. Quotes remain attributed claims, with source class, uncertainty and commercial provenance visible.

## Query

`python3 -I mamivio.com/research/global/_tools/query.py --theme tummy_time --type pain`

`python3 -I mamivio.com/research/global/_tools/query.py --stats`

`python3 -I mamivio.com/research/global/_tools/verify_quotes.py`

`python3 -I mamivio.com/research/global/_tools/verify_findings.py`

`python3 -I mamivio.com/research/global/_tools/verify_reread_merge.py`

## Resuming

Read the closing `synthesis/unfilter-report.md` section, `synthesis/reread-coverage.json`, `sources/not-harvested.md` and the source-specific ledgers before launching more work. The October `synthesis/session-report.md` remains historical scope. Use fresh capture names and quote prefixes. Do not rebuild cited corpora or rerun append-only readers. All retained raw sources are available for version control; none is ignored. Prior baselines are commits `2613feb3` and `34ec30af`; current wave03 completion is recorded in the named source ledgers. Scripts copied for future harvesting do not authorize collection from a restricted route; saved policies take precedence.

## Querying original evidence

`python3 -I mamivio.com/research/global/_tools/query.py --original-only --theme-group solids_workload`

`python3 -I mamivio.com/research/global/_tools/query.py --source-class reddit_archive --theme-group personalized_information`

`python3 -I mamivio.com/research/global/_tools/query.py --theme-group gear_and_registry --type objection`

Other groups: `development_play`, `household_coordination`, `first_trips`, `leave_and_childcare`, `free_and_DIY`, `portable_formats`. Exact theme/source/speaker/type filters still work. `--stats` separates source class and evidence kind. The complete language bank and ordinary-record `synthesis/quote-catalogue.jsonl` include every id. Original voice files retain historical eligibility metadata as a record of the earlier run; tools ignore it.

Speaker labels describe the quoted role. `gave_up_parent` means someone who stopped a particular tool/method, never a judgment about parenting. `recovered_parent` has no records; no clinical-recovery market is inferred. Source notes retain added themes and richer reader labels where useful. Do not infer gender or first-child status from pregnancy, a partner reference, or a reply's original poster.

For continuation use `synthesis/reread-coverage.json`, the dated completion section of `synthesis/unfilter-report.md`, and the named frozen inventories. `synthesis/coverage.json` is the October snapshot. Earlier reader/capture indexes are frozen snapshots, not current whole-project read status. New source waves need new filenames/prefixes, full source reads and renewed audits. Prior baseline artifacts are committed and frozen; unrelated workspace files remain unchanged.
