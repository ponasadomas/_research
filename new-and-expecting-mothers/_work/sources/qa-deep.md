# Parenting Stack Exchange — documented public API collection

**Completed reading, 2026-10-24:** all 248 candidate cards were triaged. All 119 initially kept API threads were read in full, including 298 answers and 713 comments. After 13 full-context exclusions, 106 remained eligible and produced 134 excerpts. No eligible kept thread is unread. See [the per-question reading ledger](qa-deep-reading.md), [reader notes](../synthesis/reader-notes-qa-deep.md) and [strict verification](../synthesis/qa-deep-verification.json).

## Route, policy and provenance

The earlier website crawler probe was restrictive. This separate collection used the documented official read API, whose API terms govern programmatic access. Current documentation, API terms and public terms were saved first under `_raw/qa-deep/policies/`. No website HTML crawl, account, key, private endpoint or denied-route workaround was used.

Primary references: [API documentation](https://api.stackexchange.com/docs), [API terms](https://stackoverflow.com/legal/api-terms-of-use), [public terms](https://stackoverflow.com/legal/terms-of-service/public). The public terms contain an API exception and preserve subscriber-content licensing; no unlimited permission or ownership transfer is inferred. Native per-post licenses and attribution are retained separately from anonymous research excerpts.

## Complete dated collection and local filter

`_tools/harvest_parenting_qa.py` fetched every available question created from 2020-01-01 inclusive to 2026-10-25 exclusive, partitioned by year and exhausting each paginated 100-record list. There were 1,155 questions: 336 in 2020, 265 in 2021, 192 in 2022, 143 in 2023, 117 in 2024, 68 in 2025 and 34 through October 24, 2026.

Full question bodies were saved. A transparent local infant/pregnancy tag/body filter produced 248 candidates. All 514 available answers and 1,356 comments on those candidates/answers were then fetched through documented vectorized endpoints, exhausting pagination. All 38 requests returned 200; quota and backoff rules were honored. The last observed quota was 260. No identical query was repeated within a minute. Untouched responses, headers, URLs, pagination and quotas are in `_raw/qa-deep/request-manifest.jsonl`.

Per-question native JSON bundles and extracted whole text are in `_raw/qa-deep/threads/`, indexed in `thread-index.jsonl`. Complete saved API relations do not mean deleted/private records or the whole site history were recovered.

## Reading ledger and remaining material

| Downloaded | Locally matched / triaged | Initially kept | Fully read | Eligible after reading | Excerpts |
|---:|---:|---:|---:|---:|---:|
| 1,155 questions | 248 | 119 | 119 threads, 298 answers, 713 comments | 106 | 134 |

The other 129 candidate questions were excluded at card triage; their saved bodies are not credited as full reads. Another 907 questions were outside the local filter and remain unread. Exact decisions are in `_raw/qa-deep/reconciliation-qdeep01.tsv`; `all-questions.jsonl` minus `candidates.jsonl` identifies unmatched questions.

These are questions and selected excerpt records, not people or buyers. One author contributes 19 excerpts across 15 questions; independent-customer counts cannot be inferred. All retained assignments are complete. A new expansion must use new reading/output names and an explicit scope, rather than restarting an append-only reader or treating unselected originals as irrelevant.
