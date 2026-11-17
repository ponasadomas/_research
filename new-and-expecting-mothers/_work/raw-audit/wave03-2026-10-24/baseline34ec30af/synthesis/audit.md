# Audit — completed continuation

2026-10-24. **1,944 excerpt records; 648 added after committed baseline `2613feb3`.** Source containment, metadata and declared reading coverage pass. This does not authenticate authors, purchases, credentials, clinical claims or commercial viability. Baseline audit/prose snapshots and all old voice files remain preserved.

## Exactness, structure and references

```text
TOTAL 1944 quotes, 0 failed
TOTAL 296 id references, 2 exact quote pairs, 0 failed
TOTAL 41 notes, 41 verbatim lines, 0 strict failures
```

Logs are `_raw/audit/continuation-2026-10-24/final-verify-*.txt`. The copied quote verifier preserves case/punctuation while normalizing whitespace/HTML entities and supporting the declared omission marker. The independent native audit additionally compares new excerpts with their own original post/reply bodies, rather than finding them somewhere in a whole discussion.

`audit_continuation.py` reports **zero structural/word-budget failures**: required fields, documented speaker/stage/type, global unique IDs, saved raw paths, context length, aggregate non-Reddit original-work budgets, duplicate excerpts and file sizes. There are 835 non-Reddit work keys; maximum quoted words per original work is 25. Reviews/comments retain separate original-work keys. Zero duplicate-excerpt groups does not prove independent authors.

The bank contains **1,113 distinct IDs**, each used once, with context, original link and frozen-source link. All 67 research-only records are excluded. Its selection/ranking does not change the complete 1,944-record database. Seller/guide sections retain their different evidence class; other selected excerpts are still not automatically approved advertising claims.

## Native provenance and full-reading accounting

`verify_continuation_native.py` independently checks **4,816 additional distinct complete originals,1,700 identifiable OP replies and 648 new quotes** against the saved native window JSON: entire body, immutable unit hash, actual author match, timestamp, own-body quote and canonical permalink. Explicit duplicate inspection of `1nfmfl0` adds one complete original outside the keep set; another inspection was already counted in 02. Its zero available OP replies were verified. This prevents labeling an actually inspected duplicate body as unread while keeping original triage decisions unchanged.

The raw unit contains native CRLF in one unquoted source. The independent auditor reads preserved UTF-8 bytes directly, avoiding Python text-mode newline conversion; no source was normalized to make an equality test pass. Comment quotes use original native permalinks, even where frozen primary-unit metadata contains valid `/_/` aliases. Those frozen sources were not rewritten.

`reconcile_continuation.py` joins exact IDs, not agent running estimates. All 6,597 continuation cards and all 4,689 keeps are accounted for. Donor 01’s 354 unopened keeps went to 05; root 04’s 432 keeps split 60/186/126/60 across 04/06/07/08. Original manifests/chunks remain frozen and revisions document ownership. Eight file stems were produced by three reused agent identities plus root. No transfer is an extra card or new original.

Cumulative Reddit: **5,879 full posts,2,149 OP replies,43 other comments**. Read comments are 2,192 distinct native IDs;145,387 available comment records remain unread. All 8,284 A candidates are handled, but only 8,258 received card triage;26 outside-July candidates were already handled through full payment-cohort reading. **2,532 A bodies remain unread**, including 1,907 continuation drops after the additional audit inspection. B/C and unavailable bodies remain separate. The current versioned inventories are `_raw/reddit-deep/continuation-v1/`; committed baseline `final-*` inventories are unchanged.

## Human semantic and safety checks

Two reproducible 20-record random samples were inspected against complete original/available-OP contexts, covering 39 distinct quote IDs. The independent other-reader sample is in `independent-semantic20/`; root’s stratified all-new-files sample and four whole-source views are in `parent-random20-*`. Root also performed 23 targeted record checks against 21 whole source contexts, especially reported payments, corrections, task ownership and format objections. Reinspection does not increase cumulative unique reading counts.

Conservative parent amendments affected three new records:

- `rad02-0123`: an adjacent free-meal-plan request did not establish infant/pregnancy stage; the context now says so.
- `rad05-0028`: varied solids did not establish general health; the unsupported “healthy” adjective was removed from context/notes.
- `rad02-0041`: childcare start did not establish employment return; stage and theme now identify the six-and-half-month-old/daycare handoff.

Literal excerpts, source files and IDs were unchanged in these amendments. Exact before/after logs are `parent-metadata-corrections-02.json` and`05.json`. Source 02 verification preserves original reader-freeze hashes alongside current hashes; source 05 has explicit post-parent hashes. Global final audits govern current metadata. Root’s initial stage-vocabulary normalization is separately logged. A later duplicate birthday excerpt, `rad04-0019`, was removed without renumbering; its original record/removal reason remain in the audit log.

All **68 expanded safety hits** were manually read:63 in the first queue and five final additions. Ambiguous sources received full-context inspection. `final-safety-review.jsonl` covers the exact final hit-ID set. Existing clinical/research-only restrictions remain; ordinary worry, fatigue, resolved prematurity, therapy history, infant-size numbers and adult family logistics were not automatically labeled acute crisis or minor customers. Unsafe peer sleep/feeding/treatment advice was not adopted.

**67 records are research-only**, including 64 new ones and the baseline three. They remain traceable but visibly restricted in queries and absent from the generated bank. Reasons include individual clinical boundaries, unsupported efficacy/diagnostic beliefs, unverified promotional testimony and sensitive single-perspective context. This is a research restriction, not proof that every unflagged excerpt is appropriate advertising.

## Dependence and historical limits

All 101 machine exact-body flags were reviewed within the assigned readers’ scopes; selected crosspost groups are documented. The final global duplicate-body check must distinguish exact-body copies from independent works. No flag establishes fraud or authentic identity. Among newly quoted post IDs,23 groups share a nondeleted archived-author value; hashes and exact post/date relationships are in `repeated-archived-author-groups.json`. These are database values, not authenticated people or an independent-customer denominator.

Full OP followups matter: the purported paid food list was free, with recipes/app Q&A paid; an apparent app paywall was retracted as a glitch; and an apparent nap success became inconsistent six days later under the same archived author. Interpretation preserves those limits rather than selecting the first favorable sentence.

The baseline forums/API/reviews/offer sources did not receive new human reads in this continuation. Prior parser/full-context repairs, fifteen MSE partial safety boundaries, three GeoBaby original-question uncertainties and prior semantic corrections remain documented in the preserved baseline audit and current source notes. Their 835 non-Reddit work-budget keys and saved sources were still checked in the whole-database structural audit.

Source mix, historical prices/policies, missing comments in seven communities, archive rights/provenance and author authenticity remain material limits. The B comparison is food/date selected; it demonstrates filter misses but does not estimate their frequency globally. Prepared future 847 country B cards are explicitly untriaged/unread. No Mamivio sales, report-price acceptance, CAC, search-volume study or costed fulfillment has been measured.

Final consistency checks cover all bank IDs/contexts/links, restricted exclusions, hashes, native/source totals, exact safety review coverage, body/comment inventories, duplicate groups and raw preservation. New results live in the continuation audit directory; the baseline audit artifacts are untouched. Raw material remains unignored and below 100 MB per file; original oversized archives remain losslessly split with reassembly hashes. The [session ledger](session-report.md) names all remaining work and reading costs.
