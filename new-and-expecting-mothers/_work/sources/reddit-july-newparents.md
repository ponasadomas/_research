# July 2025 NewParents — complete tier-A cohort reading

Completed 2026-10-24. Reader scope: all eight `July-A-NewParents-*.txt` cards in the frozen July packet, followed by every initially human-kept original post. This is the complete **469-post July tier-A cohort**, not every NewParents July post, every tier, all six months, a representative sample, or a live Reddit census. No rank, score threshold, top-N cut or quote quota was used.

## Provenance and actual reading scope

Source is the independently published public archive `yikeee/reddit-subreddits25`, pinned commit `ea497c510aa68765c07ed744ec9f84d68bbedf7f`. Native source window is July 1, 2025 inclusive to January 1, 2026 exclusive. This assignment selects original posts created July 1 inclusive to August 1 exclusive, UTC. Publisher provenance/rights and live completeness remain unverified; public availability does not establish a redistribution license. See [collection ledger](reddit-deep.md).

All readings used saved local files, with no source network requests or outreach. The publisher has no available NewParents comment archive at this commit. Each fully read unit therefore supports **`full_post` only**. Zero comments or OP replies were read; no complete-thread claim is made. Original post edits already included in the saved body were read. Frozen corpora were not rebuilt or edited.

## Counted from disk

| Pipeline stage | Count |
|---|---:|
| Assigned and human-triaged cards/posts | 469 |
| Complete assigned card chunks read | 8 |
| Dropped during card triage; original body not selected | 117 |
| Initially human-kept original posts | 352 |
| Original posts read in full | 352 |
| Post-read exclusions, initial keep preserved | 30 |
| Retained after full reading | 322 |
| New literal-verified excerpts | 142 |
| Original posts represented by excerpts | 127 |
| Kept original posts left unread | 0 |
| OP replies / other comments read | 0 / 0 |

The 352 full units contain **892,282 UTF-8 bytes**, including **432,108 original-body bytes**. All 469 candidate unit hashes match the frozen manifest; zero mismatches. Quoted-post counts are not unique people or buyers. Several excerpts may describe one household. None of these counts estimates market prevalence.

| Initial triage label | Candidates kept | Retained after full reading |
|---|---:|---:|
| `keep_sleep` | 144 | 133 |
| `keep_postpartum` | 70 | 62 |
| `keep_registry` | 49 | 44 |
| `keep_pumping_work` | 30 | 29 |
| `keep_other` | 28 | 24 |
| `keep_solids` | 16 | 15 |
| `keep_play` | 15 | 15 |
| `drop` | 117 | — |

| Card chunk | Initially kept originals fully read |
|---|---:|
| `July-A-NewParents-001.txt` | 51 |
| `July-A-NewParents-002.txt` | 47 |
| `July-A-NewParents-003.txt` | 51 |
| `July-A-NewParents-004.txt` | 48 |
| `July-A-NewParents-005.txt` | 43 |
| `July-A-NewParents-006.txt` | 51 |
| `July-A-NewParents-007.txt` | 56 |
| `July-A-NewParents-008.txt` | 5 |

## Reviewable artifacts and per-id status

- Initial decisions, one row per assigned id: [`july-newparents.tsv`](../_raw/reddit-deep/triage/july-newparents.tsv). Initial keeps are not overwritten after the full read.
- Per-id reading ledger: [`reading-ledger.tsv`](../scratchpad/reddit-july-newparents/reading-ledger.tsv). All 469 ids have `read`, `not-selected`, or `excluded`, a full-read flag, exact frozen unit path, reason and any new quote ids. An `excluded` row here was read fully before exclusion.
- Exact unselected original paths: [`unread-primary-paths.tsv`](../scratchpad/reddit-july-newparents/unread-primary-paths.tsv), 117 rows.
- Neutral post-read exclusions: [`post-read-exclusions.json`](../scratchpad/reddit-july-newparents/post-read-exclusions.json), 30 ids. No crisis text is republished.
- New evidence: [`reddit-july-newparents.jsonl`](../voice/reddit-july-newparents.jsonl), prefix `rjnp01-`.
- Counts and strict checks: [`audit.json`](../scratchpad/reddit-july-newparents/audit.json).
- Interpretation and counterevidence: [reader notes](../synthesis/reader-notes-reddit-july-newparents.md).

The manifest comparison found **0 missing, 0 unexpected and 0 duplicate triage ids**. Every retained unit was read through its end; there are no unread retained portions. Every quote cites its immutable individual `primary-units/NewParents-<post_id>.txt`, original URL/date and `read_scope=full_post`.

Eight initially drafted quote ids were withdrawn after a source-level safety/context review: `rjnp01-0014`, `rjnp01-0076`, `rjnp01-0092`, `rjnp01-0093`, `rjnp01-0097`, `rjnp01-0118`, `rjnp01-0119`, `rjnp01-0120` (all share the `rjnp01-` prefix). The corresponding units remain fully read and excluded in the ledger. One withdrawal follows the local Welcome Baby promotion-cluster check described in the reader notes. This also includes the reported $500 consultant account and the intensive sleep-program account; their spending is not used as marketing evidence. One exact excerpt, `rjnp01-0112`, was already in another saved reader's file and removed here to avoid duplication. Withdrawn/duplicate ids are never reused. See the neutral [withdrawal audit](../scratchpad/reddit-july-newparents/withdrawn-quote-ids.json) and [duplicate audit](../scratchpad/reddit-july-newparents/duplicate-excerpts.json).

## Verification and safety

Command: `python3 _tools/verify_quotes.py voice/reddit-july-newparents.jsonl` from this research folder.

```text
reddit-july-newparents.jsonl: 142 quotes, 0 failed
TOTAL 142 quotes, 0 failed
```

Additional strict checks confirm every excerpt is a literal substring of its frozen raw unit, every original URL/date matches the frozen primary index, all contexts are at most 25 words, all new ids are unique across saved voice files, and all 469 frozen candidate hashes match. The shared verifier normalizes whitespace; the independent literal check is stricter.

All 13 candidate safety flags were human-inspected through cards and, where initially kept, full originals. Ordinary worry and guilt were not automatically classified as crisis. Clinical/safeguarding/acute or severe-distress accounts were excluded by source context; seller/maker promotion was not treated as independent customer demand. A remaining choking-related excerpt (`rjnp01-0057`) describes unsuccessful rereading, not first-aid instructions or an efficacy claim. Developmental, physiological and sleep-outcome assertions in any retained quotation remain author beliefs, never clinical guidance. Reported purchases, product problems, prices and outcomes are unverified first-person reports; no fee implies paid-report validation.

## What is unread

- **No assigned human-kept original remains unread.** All 352 were completed, including 30 later excluded.
- The **117 card-dropped July original bodies** were not selected/read; exact paths are in the unread-primary manifest linked above.
- NewParents has **no archived comment file** in this source; comments and OP follow-ups are unavailable, not silently claimed read. There is no NewParents auxiliary-comment queue in the July packet.
- **2,086 NewParents tier-A posts outside July** were outside this reader's assignment and not read by this reader. Exact original unit paths are enumerated in [`outside-july-A-paths.tsv`](../scratchpad/reddit-july-newparents/outside-july-A-paths.tsv). Other source readers may overlap; this is not a global unread claim.
- NewParents B/C/unavailable bodies and other months remain in `_raw/reddit-deep/windows/2025-h2-v1/NewParents_submissions.jsonl.gz`; tiers/id inventory are in `_raw/reddit-deep/filter-v1/posts-index.jsonl`. They were not triaged or read by this reader. This task does not complete the six-month/community research program.

## Added local tags

These tags extend the research README vocabulary for this reader; they classify selected evidence, not segments measured in the market.

| Tags | Meaning |
|---|---|
| `bottle_transition`, `feeding_schedule` | Moving feeding across containers/caregivers; practical timing conflicts, not intake prescriptions |
| `caregiver_coordination`, `communication_gap` | Shared roles, handoffs, missing or unreliable operational information |
| `celebration_pressure`, `gift_logistics` | Celebration expectations, event burden and gift transport/selection |
| `childcare_cost`, `household_budget` | Childcare and wider household affordability constraints |
| `contingency_planning` | Preparation for appliance failure or disrupted care routines |
| `data_portability`, `simple_tracking`, `alert_fatigue` | Record ownership/recovery, minimal memory aids and repetitive notifications |
| `day_structure`, `format_preference`, `information_gap` | Organizing parent days, explicit medium preference and missing actionable detail |
| `failed_purchase`, `paid_help`, `paid_food_service` | Reported disappointing purchase, paid care/service, or prepared-food order; payment is explicit only where recorded |
| `first_outings`, `travel` | Ordinary outings, trip preparation and transport logistics |
| `gear_reuse`, `gear_tradeoffs`, `replacement_parts` | Reused equipment, constraint-based selection and replacing components |
| `meal_preparation` | Ordinary cooking actions and preparation workflow |
| `memory_preservation` | Photo selection, albums, milestone books and printing |
| `pet_transition`, `sleep_clothing` | Pet-care preparation and clothing choices under real home constraints |
| `relationship_connection`, `workload_coverage` | Couple connection outside task management; capacity for protected work breaks |
| `ai_tools` | Existing AI outputs or trials, without assuming clinical accuracy or endorsement |

## Reference correction and memory-product audit

Before handoff, every quote id cited in the reader notes was looked up in the final voice file. Eight claim/reference groups were corrected (nine originally mislinked id references), including the upstairs-grandparent-care claim. The monitor sentence was narrowed to the directly quoted remote-viewing requirement. The full correction and reference audit is in `scratchpad/reddit-july-newparents/notes-reference-audit.json`. `rjnp01-0073` is tagged `belief` for the observed Little Spoon order; no delivered outcome is inferred.

The memory-product comparison scanned all nine saved submission windows and conservatively excluded one potentially promotional Welcome Baby question. The surviving independent-looking photo/printable requests contain no direct pitch and had no substantial text matches under the saved rule. This is not proof of authenticity. Repeated/crossposted originals may exist; reads and selected quote-posts are never distinct-person or independent-case counts.

Parent safety review later marked rjnp01-0060 and rjnp01-0115 research-only: unverified developmental/AI-diagnostic beliefs, excluded from the generated language bank. Record IDs, literal text and raw files unchanged. Latest hash and reasons: `_raw/audit/deep-wave/boundary-only-records.json`.
