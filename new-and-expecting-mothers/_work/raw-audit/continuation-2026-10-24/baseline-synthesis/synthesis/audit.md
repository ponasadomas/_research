# Audit — reopened original-source pass

2026-10-24. Final database: **1,296 excerpt records**, including 878 new records beyond the frozen initial 418. Audits establish source containment, metadata consistency and declared reading coverage; they do not verify authors, receipts, clinical claims or commercial viability.

## Exactness and structure

`_tools/verify_quotes.py` preserves spelling, case and punctuation, normalizing only whitespace/HTML entities and supporting the declared omission marker. All records name a saved source.

```text
TOTAL 1296 quotes, 0 failed
```

`audit_deep_wave.py` reports zero structural/word-budget failures. Required fields, README vocabulary, unique quote IDs, raw paths, context length and non-Reddit quotation budgets were checked. All non-Reddit work groups are at most 25 quoted words across selected records. Review IDs/local review keys and comment IDs distinguish individual works; a whole app page is not incorrectly treated as one customer review.

All 41 competitor notes' blockquotes also pass a stricter case/punctuation-preserving comparison in addition to the copied competitor verifier. Reproduce with `_tools/verify_competitors_strict.py`; the final log is `_raw/audit/deep-wave/final-verify_competitors_strict.txt`. Source-specific readers checked actual native author bodies, original dates/URLs, OP attribution and whole-unit hashes. The Q&A audit checks content licenses and separate attribution records. The generated language bank has 977 distinct IDs, each used once, with context plus original/frozen links.

Core-document references:

```text
TOTAL 214 id references, 2 exact quote pairs, 0 failed
```

The literal pairs were generated from actual records. Reference existence is machine-checkable; semantic support was reviewed against the retrieved records and reader notes. Machine checks alone cannot prove it.

## Human source and context checks

Forty reproducible new-record spot checks were inspected against full quoted author posts and original questions/OP context, with two extra targeted checks. The first 20 and later 20 are frozen separately under `_raw/audit/deep-wave/`; the first pass's own sample remains untouched.

Parent corrections affected nine records: an inferred maternal label/context, an inferred success from buying a book, five seller professional/stage labels, and two later maternal labels without explicit self-identification. IDs, literal quotations and source files remained unchanged. Before/after values and hashes are in `parent-metadata-corrections.json` and `later-metadata-corrections.json`. Reader vocabulary corrections are separately logged in source notes.

A NewParents reader-note audit corrected nine mislinked references before integration and looked up all active references again. Current core references were checked independently. The payment cohort's overbroad fatigue exclusion was reconciled with the full focused reading: ordinary exhaustion/disagreement alone did not establish acute crisis; the reported paid-analysis account is retained without instructions or efficacy claims. The prior ledger and correction are preserved.

## Extraction loss and reading truth

The original oblique parser removed every blockquote, not only repeated prior posts. A 48-post full-context supplement was read for the initial 29 MSE discussions. It found one entirely blockquoted, self-written post that had been described as empty; source prose was corrected. Interpretation of the 57 selected excerpts did not change.

All later 313 MSE discussions used newly frozen v2 whole-thread units with `body_with_quotes`; all 183 GeoBaby captures used complete-context units. Original corpora were not rewritten. Quoted earlier posts, manufacturer text, partner remarks and legal/clinical passages are context, not independent parent voices. JustParents and the Reddit/API reading views retained blockquotes already.

`reconcile_deep_coverage.py` joins original IDs rather than adding readers' running totals. The result is 1,063 distinct Reddit post IDs, not 1,031 + 39: seven payment-cohort posts overlap the July full reads. Forums reconcile to 605 complete visible discussions plus 15 explicit partial safety inspections, with 231 later safety-tail posts deliberately unclaimed. Every eligible retained assignment is complete; unselected bodies and unavailable content remain separate.

Three GeoBaby captures have uncertain original-question provenance despite complete visible pagination. The only selected later reply from those has `source_role_uncertain=true`; no missing premise or OP outcome was invented. Known crossposts, including the gifted Lovevery pair, remain annotated and cannot count as independent purchasers. The exact-excerpt check reports zero duplicate groups under URL/post keys; it does not prove independent authors.

## Safety and scope

All 49 new hits from the expanded safety regex were manually reviewed. The final queue and per-ID decisions are `final-safety-hits.jsonl` and `final-safety-review.json`. The initial safety queue is preserved separately; its narrower regex and earlier scope explain different counts in legacy outputs.

Three records are explicitly research-only: `odeep05-0023` (clinical boundary), `rjnp01-0060` (unsupported developmental belief), `rjnp01-0115` (unverified AI-diagnostic belief). They remain traceable research evidence, are visibly marked in query results, and are excluded from `quote-index.md`. `--exclude-restricted` removes them from queries. Remaining records still require editorial judgment; peer/seller words are not medical guidance or advertising approval.

Safety exclusions do not republish crisis passages or turn diagnoses, ordinary fatigue, therapy history or former NICU care into target segments. Historical advice about feeding, sleep, product safety, benefits and employment is not adopted as current guidance. One later diagnosis is evidence against converting every food-refusal question into a meal-plan opportunity, not a general diagnostic claim.

## Balance and remaining limits

Counts by source, speaker, stage and theme are generated in `counts.md`. Most identity/role fields are conservative parent_unspecified; the sources cannot establish a mothers-only purchasing advantage. Repeated Q&A authors and crossposts are explicitly named as dependence issues. The recovered_parent label has no records; normal adaptation appears as other roles/success stories, and clinical recovery was not a researched offer. No missing cell was filled by inference.

The source mix includes originals from Reddit, three forums, Q&A and review platforms, as well as seller, ad and guidance evidence. July A filtering, frugal forums, older Hong Kong archives, visible-review selection and unknown author authenticity limit generalization. Literal verification is not verification of typical outcomes or scientific correctness.

The final consistency report, `_raw/audit/deep-wave/final-state-consistency.json`, independently checks the language bank’s IDs, contexts, links, restricted-record exclusions, source totals and complete safety-review ID set.

No raw file exceeds 100 MB; native oversized compressed archives are losslessly split with reassembly hashes. All retained raw material is unignored. Latest voice hashes are in `final-structural-audit.json`, which supersedes earlier reader freezes after documented parent metadata/scope changes. No commit or external publication occurred. Full playbook gaps, exact unread paths and the next reading cost are in `session-report.md`.
