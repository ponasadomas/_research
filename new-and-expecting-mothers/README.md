# new-and-expecting-mothers

Not one buyer: the whole crowd of expecting mothers and mothers of young children. This
research was done in October 2026 to choose which niche mamiVio should enter, and was
re-read without any subject filter on 2026-11-17. It also holds the Reddit archive that
five niche studies drew their posts from. Rules for all research: `../README.md`.

Start with `evidence/findings.md` (5,500 words) and `evidence/niche-opportunities.md`
(the ranking of niches). `summary-2026-10-25.md` compares the five niche studies as they
stood in October; `brief.md` is the idea this research was testing.

## What is here

| Folder | What was collected | State |
|---|---|---|
| `ads/` | Meta Ad Library captures: a census of 43 advertiser pages on 2026-10-25, deeper reads of nine groups of advertisers, and searches by niche (949 saved files) | 11 notes, among them Kinedu, Huckleberry, Lovevery, Pirmi Žingsniai and its Hungarian clone, and spend by niche. The overall write-up is `evidence/advertiser-money-map.md` |
| `books/` | Store pages for 14 books (37 saved files) | 14 notes, one per book; 9 quotes |
| `competitors/` | Seller pages, offer, pricing and terms pages, and the capture of one seller's order flow (435 saved files) | 56 notes, one per seller, plus the observed funnel and sales letter; 92 quotes |
| `forums/` | Mumsnet pages saved for the jargon glossary (746 files, `raw/mumsnet-jargon-2026-07/`), JustParents (505 threads), MoneySavingExpert parents' boards (343 threads), Parenting Stack Exchange (248 questions), and the search for other communities (6,375 saved files) | 1,811 quotes. No notes at the top; the readers' notes are in `evidence/` |
| `marketplaces/` | Listings from ClickBank, BuyGoods and Digistore (18 saved files) | Looked at, no notes written, no quotes |
| `official-guidance/` | CDC, AAP and ACOG pages (25 saved files) | 10 quotes |
| `reddit/` | Four archives (the fourth, `raw/jargon-2026-07/`, 439 MB, was saved in July 2026 for the jargon glossary). The other three: nine communities, July to December 2025 (`raw/reddit-deep/`, 1.3 GB); two more communities (`raw/report-purchase-archive-wave03/`); and the 2026 archive the five niche studies use (`raw/reddit-2026/`, 605 MB) | 4,866 quotes from the first two. Large unread backlogs remain, see `evidence/unfilter-report.md` |
| `reviews/` | App and course reviews, two rounds (151 saved files) | 197 quotes |
| `sales-letters/` | nothing | Not collected |
| `statistics/` | nothing | Not collected |
| `youtube/` | A small probe (6 files) | Nothing usable |
| `quotes/` | 6,991 quotes in 59 files | Every quote checked against its source |
| `evidence/` | `evidence.md` (694,000 words: every quote under its theme), `jargon-glossary.md` (the words mothers use, July 2026), `findings.md`, `niche-opportunities.md`, `purchase-evidence.md`, `niche-map/`, counts, readers' notes, audits | Current as of 2026-11-17 |

Findings page in `_home`: none. This niche is research only; see
`~/GitHub/_home/library/avatars/new-and-expecting-mothers/avatar.md`.

## The four questions

| Question | Answered from | State |
|---|---|---|
| 1. Who is she, and what is her life like? | `evidence/reader-notes-audience.md` only | Hardly: one set of notes from search extracts, marked as hypotheses |
| 2. What hurts, what does she want, and how does she say it? | `reddit/`, `forums/` | Answered across niches, from several communities |
| 3. What is she buying, what does she pay, and how did it go? | `evidence/purchase-evidence.md`, `reviews/`, `marketplaces/` | Partly: purchase mentions were collected and classified, which the niche studies lack; marketplaces were looked at but not written up |
| 4. Who is selling to her, and what is working? | `ads/`, `competitors/` | Best answered here of any folder: ad census, 56 seller notes |

## Checking

Run from this folder. Expected results:

```
python3 -I _tools/check_ids.py              6991 records, 6991 distinct ids, 0 duplicated
python3 -I _tools/verify_quotes.py          6991 quotes, 0 failed, 0 with a missing raw file
python3 -I _tools/verify_part.py quotes evidence/evidence.md 0
                                            ids mentioned 4970, quotes reproduced 4970; OK
```

`verify_part.py` on `evidence/findings.md` reports one unknown id, `wave03-2026`: that is
a folder name that looks like an id, not a quote.

The set's own 141 scripts, including its coverage audits, are in `_tools/history/`. They
were written for the old layout and are kept as a record; they do not run from here.

## Paths in older files

Moved here on 2026-11-17 from `ads/mamivio.com/research/global/` and `main/`. The quote
records and the main documents in `evidence/` use the new paths. Notes, ledgers, logs and
manifests written before the move are left as written:

| Old path | Now |
|---|---|
| `_raw/<round>/` | `<kind>/raw/<round>/`; the round's folder name is unchanged. Which kind: see the table below |
| `voice/` | `quotes/` |
| `synthesis/` | `evidence/` |
| `sources/`, `scratchpad/` | `_work/sources/`, `_work/scratchpad/` |
| `ads-running/`, `books/`, `competitors/` (notes) | `ads/`, `books/`, `competitors/` |
| `product/` | `brief.md`, `competitors/observed-offer-*.md` |
| `../main/synthesis/` | `evidence/niche-map/` |
| `../main/ads-running/`, `../main/_raw/ads-running/` | `ads/`, `ads/raw/main-ads-running/` |
| `../_shared/_raw/reddit-2026/` | `reddit/raw/reddit-2026/` |
| `../development/` and the other niche folders | `../baby-development/`, `../sleep-baby/`, `../sleep-mother/`, `../toddler-behaviour/`, `../pregnancy-birth/` |

| Kind | Rounds under its `raw/` |
|---|---|
| `ads/` | ads, ads-running, advertiser-census-wave04-2026-10-25, advertiser-map04-* (five), advertiser04-meal-guides, probes, main-ads-running |
| `competitors/` | competitors, market-deep, market-wave-03, offer-followups-wave03, report-buyers-wave03, product, main-competitors |
| `forums/` | forums-deep, oblique-deep, qa-deep, communities |
| `reddit/` | reddit-deep, report-purchase-archive-wave03, reddit-2026 |
| `reviews/` | reviews, reviews-followups |
| `youtube/` | youtube, media-deep |
| `books/`, `marketplaces/`, `official-guidance/` | books, marketplaces, guidance |

## Quote fields

Every quote has `id`, `source`, `url`, `date`, `speaker`, `stage`, `type`, `themes`,
`quote`, `context`, `raw_file` (relative to this folder). Some carry `source_class`,
`evidence_kind`, `post_id` and similar. The 141 records that carry
`marketing_eligible: false` were marked by a filter that was removed on 2026-11-17; the
flag is history and has no effect.

## Vocabulary

Speakers: `expecting_mother`, `new_mother`, `experienced_mother`, `parent_unspecified`, `partner`, `relative_caregiver`, `recovered_parent`, `gave_up_parent`, `advisor`, `professional`, `reviewer`, `skeptic`. Use parent_unspecified if the author does not identify as mother. An advisor's instructions are not verified clinical guidance. The other side includes partners, daycare caregivers and mothers who stopped following programs.

Stages: `pregnancy_early`, `pregnancy_late`, `newborn_0_6_weeks`, `baby_6_16_weeks`, `baby_4_6_months`, `baby_6_12_months`, `toddler`, `return_to_work`, `looking_back`, `unknown`.

Types: `trigger_moment`, `pain`, `fear`, `tried_failed`, `desire`, `belief`, `question`, `objection`, `advice_given`, `success_story`, `failure_story`, `regret`, `others_said`.

Seed themes: `information_overload`, `conflicting_advice`, `late_night_search`, `first_time_parent`, `not_enough_time`, `maternal_guilt`, `tummy_time`, `floor_play`, `milestone_comparison`, `corrected_age`, `flat_head_concern`, `feeding_reflux`, `contact_naps`, `sleep_routines`, `sleep_training_values`, `wake_windows`, `first_solids`, `allergen_introduction`, `choking_fear`, `meal_planning`, `food_budget`, `pumping_schedule`, `return_to_work`, `daycare_handoff`, `bottle_refusal`, `milk_supply_concern`, `pregnancy_activity`, `birth_preparation`, `postpartum_recovery`, `household_support`, `partner_mental_load`, `no_village`, `second_baby`, `twins`, `skepticism`, `subscription_fatigue`, `price_value`, `personalization`, `free_alternatives`, `clinical_referral`, `language_access`, `privacy`. Add tags only when needed and document them.

