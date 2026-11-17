# Mamivio — main research (niche decision layer)

**See also `../PLAN-2026-10-25.md`: five full builds now run in sibling folders (sleep-baby, sleep-mother, development, toddler-behaviour, pregnancy-birth).**

**State on 2026-10-25: step 1 done — the sub-niche map — plus an Ad Library read of the Pirmi Žingsniai machine (see `ads-running/`).** No harvesting into this folder yet. Read [`synthesis/sub-niche-map.md`](synthesis/sub-niche-map.md) first; it ends with a shortlist and a Phase 2 source map per candidate, waiting for the owner's pick.

## How this folder relates to `../global/`

`../global/` is the frozen source database built on 2026-10-24: 2,162 verified excerpts, 112,665 harvested Reddit posts (July–December 2025, nine communities), 605 forum discussions, 119 Q&A threads, 219 app/book reviews, 47 competitor teardowns, 20 Ad Library searches, and a decision document (`global/synthesis/niche-opportunities.md`) that ranked niches on one strict criterion: *a verified standalone purchase of a customized report*. That bar pushed it toward a very narrow workflow idea (baby-lunch preparation and caregiver handoff).

`main/` is the layer above it. The owner's reframed question (this session) is wider: **which problems inside "new and expecting mothers" are big and intense enough to focus on, and solvable with a personalized report or another info product, with the Pirmi Žingsniai age-selector PDF explicitly allowed as a model.** Width and intensity count here; "no verified report sale yet" is a caveat, not a veto.

Rules for this folder:

Research records what people actually say and do, in their own words, whatever the subject. The owner decides later what to use in copy; no subject is withheld from research.

- Preserve `../global/voice/` and all raw sources. Cite or reproduce its quotes verbatim with ids as `[id]`; `python3 ../global/_tools/query.py --id <id>` resolves them.
- Once a sub-niche is chosen, the playbook (`templates/00 - Deep Research Playbook.md`) runs here from Phase 0: `product/`, `sources/`, `_raw/`, `voice/`, `competitors/`, `synthesis/`, with new quote prefixes. `global/` material can be filtered into it by id, never copied without its `raw_file`.
- Counts in this folder are counts of posts or quotes selected, never of people.

## Layout so far

| path | what |
|---|---|
| `synthesis/sub-niche-map.md` | the deliverable: criteria, the map, the shortlist, Phase 2 per candidate |
| `synthesis/width-reddit-mention-share.md` / `.csv` | width proxy: share of the 103,719 available harvested post bodies matching one wide regex per sub-niche |
| `sources/width-proxies-external.md` | subreddit sizes, app-store listings, search-result shapes, and the failed Amazon Best Sellers attempts (agent, 2026-10-24) |
| `ads-running/spend-footprint-by-subniche-2026-10-25.md` | the Ad Library sweep: 15 exact-phrase searches and 12 seller Pages, active-ad counts per sub-niche; sleep and potty are the info-product spend clusters |
| `ads-running/pirmi-zingsniai-and-elsolepesekmama.md` | Ad Library read of both Pirmi Pages (LT 116 ads, 0 active; HU 206 ads, 72 active), landing pages, catalogues, ad formats; Dawnly and BedtimeCoach have no ads |
| `_raw/ads-running/`, `_raw/competitors/` | raw Library result pages, both shops' products.json, the two Hungarian advertorial pages |
| `_tools/subniche_mention_share.py` | regenerates the width table from `../global/_raw/reddit-deep/windows/2025-h2-v1/` |
| `_tools/verify_map_ids.py` | checks every `[id]` and quoted fragment in a Markdown file against `../global/voice/` |

## Resuming

Read the map's shortlist and "What's unmeasured". The next session starts by the owner choosing one or two candidates; then Phase 0 (product brief from the niche title, owner data) and Phase 2 (source map) for that candidate.
