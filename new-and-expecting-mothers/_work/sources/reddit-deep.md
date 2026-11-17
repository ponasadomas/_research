# Real Reddit archive corpus — collection and reading ledger

**Current completed update — 2026-10-25:** main nine-community H2 coverage is6,476 distinct full posts,2,150 identifiableOPreplies,43 exactothercomments and1,066 selected native excerpts. All 847 preparedcountryBcards and all 584 keeps are now complete;five additional duplicate originals and eight new IDs from root commercial reinspection are separately logged. Older Areading and comparison scopes remain complete. These are archived record counts, not independent people or transactions.

**Current unread main scope:**2,531 A /50,530 B /38,463 C readable bodies,14,665 unavailable;145,386 availablecomments unread and seven comment sources absent. Current exact inventories `_raw/reddit-deep/wave03-v1/`; older inventories remain frozen. Separate additional-community commercial reading adds122 full posts, and targeted historical native-ID lookups add7, for6,605 distinct archived posts globally. Those additions do not silently change main A/B/C denominators. [Session ledger](../synthesis/session-report.md).

The collection/handoff counts below describe earlier preparation snapshots; current reading completion comes from named per-ID ledgers and current inventories, not capture-time zero-progress fields.

## Historical collection handoff

The zero-read counts below describe the collection handoff before reader assignment; they are preserved for provenance and are superseded by the completed reading update above.

Reopened 2026-10-24 after the owner rejected the initial pass's lack of real Reddit/forum depth. This source is separate from the frozen initial 418 quotes and the `community_index` excerpts. **Real archived original posts and comments have now been collected in bulk. No new Reddit quotes or human full reads are claimed at this collection handoff.**

## What was actually collected

Eleven complete published compressed files, **905,244,436 bytes**, containing **2,949,821 original JSON records**: 1,384,162 submissions and 1,565,659 comments. Entire files were decompressed/scanned to EOF: no JSON parse errors or missing creation timestamps. Timestamp inversions exist, especially in BabyBumps/beyondthebump, so the date filter does not stop early based on ordering.

The frozen common window is **2025-07-01 00:00:00 UTC inclusive through 2026-01-01 00:00:00 UTC exclusive**. It contains **112,665 submissions across nine communities** and **147,579 comments across two communities**. These are all records in that window in the downloaded published files, not search results, a relevance ranking or a live Reddit census. Source files contain removed/deleted records and unknown capture gaps. Coverage ends in 2025, not October 2026.

## Publisher, access and provenance

- Publisher/repository: [yikeee/reddit-subreddits25 on Hugging Face](https://huggingface.co/datasets/yikeee/reddit-subreddits25).
- Pinned commit: `ea497c510aa68765c07ed744ec9f84d68bbedf7f`.
- Metadata/card/manifest saved under `_raw/reddit-deep/probes/yikeee-*`; requests and actual status codes in `sources/reddit-deep-access.jsonl`.
- Public repository is ungated. Hugging Face's robots file permits access. Files were obtained through the publisher's documented public `resolve/<commit>/...` URLs and its normal CDN redirects. No live Reddit endpoint, denied Arctic Shift endpoint, proxy, identity spoofing, cookie extraction, account login or captcha workaround was used.
- The card states the dataset came from a local torrent bundle without provenance/licensing documentation. Its license field is `other`. **Public availability is not a verified redistribution license, authors' consent or proof that the bundle is complete.** No specific permissive content license, independent original capture history or affiliation with Arctic Shift is claimed. The repository does not state an explicit noncommercial-only or AI-input prohibition. Missing provenance/licensing is recorded as a limitation rather than invented permission or an invented categorical access ban.
- Raw native schemas contain original ids, creation timestamps, title/selftext or body, subreddit, score, original permalinks, and comment `link_id`/`parent_id`. Bodies were not rewritten, summarized or typography-cleaned. No claims about individual authors' identity or consent are inferred.

### The card's advertised total is not the published-file total

The manifest lists **79,955** data files. At the pinned commit, the actual repository metadata lists **52,803 entries**, of which **52,800 are data files**. Therefore the advertised archive is not fully published there. The specific comment files for NewParents, BabyBumps, beyondthebump and ExclusivelyPumping are in the manifest but resolve to **404**. Their main submission files are published and were downloaded successfully. Country-community comment files were also absent from actual repository metadata. Do not infer comment completeness from the repository's name or card.

For the two available comment archives, all records are retained before filtering. For selected posts, linked comments are joined by `link_id`; identifiable OP replies use matching nondeleted author ids. `[deleted]` authors are not treated as the same person. Original post `num_comments` is retained separately from observed archived comment count and does not establish collection completeness.

## Routes investigated before choosing this source

| Route | Actual observation | Why it is or is not used |
|---|---|---|
| [Dk587/arctic](https://huggingface.co/datasets/Dk587/arctic) | Card, metadata, file list, stats and rows API return 200; commit `cd44b72689d409b6a881e0b4581d106b9c37a613` | Claims extend through 2026, but actual comment files stop at **2012-08**. Recent submission shards exist. No card-total assumption was used as coverage. |
| [open-index/arctic](https://huggingface.co/datasets/open-index/arctic) | Public metadata/card/stats return 200; commit `da567f9441c5a7ebf02d13eeeaa020b11f321f8d` | Original publisher has more comments than the Dk copy, reaching actual file paths through **2022-08**, while submissions reach 2026-02. Huge monthly files are a possible future historical supplement, not used in this window. Card retains Reddit terms and describes as-is research/education use. |
| [HF documented filter endpoint](https://huggingface.co/docs/dataset-viewer/filter) | Dk filtered request returned 500, index-loading message | Official docs say filtering uses only first 5 GB for a large dataset (`partial=true`). Even a successful filtered response would not establish a complete recent subreddit harvest. No viewer sample was substituted. |
| [Arctic Shift project download documentation](https://github.com/ArthurHeitmann/arctic_shift/blob/master/download_links.md) | GitHub raw documentation 200 | Official links identify monthly torrents and a subreddit-partitioned archive; documentation is not itself source content. |
| Academic Torrents subreddit archive `56aa49f9653ba545f48df2e33679f014d2829c10` | Robots and torrent-download URL both 403, Cloudflare code 1010 | Denial logged; no alternate-host evasion or torrent content download. |
| [HuggingFaceGECLM/REDDIT_threaded](https://huggingface.co/datasets/HuggingFaceGECLM/REDDIT_threaded) | Metadata/card 200 | Actual named splits cover selected large/oblique communities, not the requested mother/baby main sources. Card lacks sufficient provenance; not substituted for them. |
| [fddemarco/pushshift-reddit-comments](https://huggingface.co/datasets/fddemarco/pushshift-reddit-comments) | Metadata/card 200 | Actual files span 2012-01 through 2016-02; not a current six-month mother/baby corpus. Submission companion reaches 2018-12. |
| [mitanshugoel/reddit-2025](https://huggingface.co/datasets/mitanshugoel/reddit-2025) | Public metadata 200, 24 monthly native comment/submission files, approximately 759 GB stored | Legitimate separate published-file route, but no detailed card/terms/provenance were established here; per-subreddit published files supplied a more direct complete-file collection path. Not downloaded or called read. |
| HF dataset searches for NewParents/BabyBumps/beyondthebump | Public API 200, no named-repository matches | Empty discovery results are not claims that these communities or archives do not exist. Broader Reddit/subreddit searches led to the working source. |
| Internet Archive robots | 200 | No content harvested from this route; it did not supply a proven target archive. |

All metadata, documentation and failures remain in `_raw/reddit-deep/probes/` with URL/status logs. Repository license uncertainty is not conflated with an explicit use prohibition. The previous direct Reddit/Arctic host restrictions remain recorded in `sources/communities.md`; these requests were to independently published datasets, not alternate names for that denied service.

## Raw preservation and integrity

Native files are preserved in `_raw/reddit-deep/archive-files/`. The three native files over 100 MB were **split losslessly into pieces of at most 95,000,000 bytes**. Their `.parts/reassembly.json` lists ordered paths, piece hashes, original size and original SHA-256. Concatenating those pieces reproduces the exact downloaded bytes. Unsplit convenience copies are temporarily outside the repository at `/tmp/mamivio-reddit-unsplit/`; the repository pieces are the durable source.

`_raw/reddit-deep/integrity-manifest.json` independently rehashed all eleven logical source files, including reassembly streams: **11 matches, 0 mismatches**. `sources/reddit-deep-downloads.jsonl` records source URL, commit, size, status and download hash. `file-stats/*.json` records full-file dates, schema, text availability and monthly counts. Every file in this new source's repository tree is below the 100 MB GitHub file ceiling; retained raw material is unignored and the original collection is included in baseline commit 2613 feb3.

The date-filtered original JSON lines are stored unchanged inside individual `.jsonl.gz` files under `_raw/reddit-deep/windows/2025-h2-v1/`. Per-file manifests record the exact exclusive time boundary, source rows scanned, selected records, text availability, duplicate counts, bytes and hash. **No duplicate ids were detected within any window file.**

## Ledger at collection handoff

Here, `A` is a machine-filtered candidate count, **not** a human keep decision. No original or comment human read is claimed merely because a script parsed it.

| Source | Full-file original records downloaded/scanned | Records in six-month window | Tier-A candidate posts or comments joined to A posts | Cards human-triaged | Human-kept | Original units read | Quotes |
|---|---:|---:|---:|---:|---:|---:|---:|
| NewParents submissions | 209,808 | 32,170 | 2,555 | 0 | 0 | 0 | 0 |
| BabyBumps submissions | 611,459 | 30,806 | 1,563 | 0 | 0 | 0 | 0 |
| beyondthebump submissions | 367,347 | 18,838 | 1,295 | 0 | 0 | 0 | 0 |
| ExclusivelyPumping submissions | 66,904 | 11,445 | 1,183 | 0 | 0 | 0 | 0 |
| workingmoms submissions | 52,329 | 4,608 | 668 | 0 | 0 | 0 | 0 |
| BabyLedWeaning submissions | 18,466 | 1,996 | 107 | 0 | 0 | 0 | 0 |
| BabyBumpsCanada submissions | 28,881 | 3,924 | 286 | 0 | 0 | 0 | 0 |
| BabyBumpsandBeyondAu submissions | 17,296 | 4,902 | 359 | 0 | 0 | 0 | 0 |
| BeyondTheBumpUK submissions | 11,672 | 3,976 | 268 | 0 | 0 | 0 | 0 |
| **Submissions total** | **1,384,162** | **112,665** | **8,284** | **0** | **0** | **0** | **0** |
| workingmoms comments | 1,344,743 | 125,533 | 17,996 | — | — | 0 | 0 |
| BabyLedWeaning comments | 220,916 | 22,046 | 1,262 | — | — | 0 | 0 |
| **Comments total** | **1,565,659** | **147,579** | **19,258** | — | — | **0** | **0** |

Collection totals are from actual parsed files, not the HF card. Main-community **post** coverage and complete live **thread** coverage are different; seven of the nine sources have no available comment archive in this collection.

## Transparent local tiers and triage queue

Code: `_tools/reddit_deep_filter.py`. Filter input is every submission in the complete window, title and full selftext. Regex definitions are saved in the code, not an opaque model rank.

- **A: 8,284** — an explicit request/need for a plan, schedule, checklist, guide, routine, template or personalization, or an app/book/course/program/planner/coach paid/free/use/value decision. Regex proximity is deliberately wide and produces false positives for human triage.
- **B: 51,253** — broader uncertainty, guilt, difficulty, logistics or advice-seeking without an A artifact/tool match.
- **C: 38,463** — adjacent material outside A/B.
- **Unavailable: 14,665** — empty, `[removed]` or `[deleted]` body; retained on disk, not passed off as full original-body evidence.

The three readable tiers total **98,000** original posts. All topics are retained: play/development, first foods, pumping, sleep, household support, pregnancy/birth, registry/gear and work return. No first-solids preference, score ranking, upvote sort or top-N cap was applied. A safety regex supplies a flag for human review, not automatic clinical classification or automatic deletion.

All **8,284 A cards** are frozen in **131 approximately 40 KB card chunks** at `_raw/reddit-deep/filter-v1/cards/`; `cards-index.jsonl` names every card id. `posts-index.jsonl`, `A-candidates.jsonl`, `B-candidates.jsonl`, `C-candidates.jsonl`, `unavailable-candidates.jsonl` and `summary.json` provide full accounting. Read every assigned A card before a keep/drop decision. Written brief: `_tools/brief-reddit-deep-triage.md`. The next wave must triage **all A cards**, not just a representative handful. B/C are an explicit queue, not claimed read or irrelevant.

## Frozen original candidate corpus and missing relations

Every A candidate already has a frozen complete original unit at `_raw/reddit-deep/corpus-A-v1/units/<subreddit>-<post_id>.txt`; index is `corpus-A-v1/index.jsonl`. A machine candidate unit is not a kept/read unit. Text has not been truncated.

Across A candidates the corpus contains **8,284 complete post bodies**, **19,258 available archived comments** and **2,735 identifiable OP replies**. There are **775 candidate units with an available comment source** and **7,509 post-only units whose comment source is unavailable**. Every unit says which scope it supports. Observed comment-parent references inside the retained full-comment units have **0 missing referenced parent records**; this does not prove live comments or later edits/deletions are complete.

Comments are limited to the archive's frozen end boundary; later 2026 follow-ups are absent. The remaining 128,321 window comments concern non-A or earlier/outside-window posts and are retained in the complete window comment files, not silently discarded. Those are not claimed read. Nothing in this corpus proves a deleted account's identity or enables attributing an arbitrary comment to the OP.

There are **865 frozen original-reading chunks**, **32,426,499 UTF-8 bytes**. **85 single-thread chunks exceed 40 KB** because the full available discussion is preserved instead of cut. Exact paths, ids, size and unread status are in `corpus-A-v1/chunks-index.jsonl` and `_raw/reddit-deep/reading-queue-v1.tsv`.

| Candidate source | Full A posts | Available comments included | Frozen full-reading chunks |
|---|---:|---:|---:|
| NewParents | 2,555 | 0 | 159 |
| BabyBumps | 1,563 | 0 | 107 |
| beyondthebump | 1,295 | 0 | 90 |
| ExclusivelyPumping | 1,183 | 0 | 71 |
| workingmoms | 668 | 17,996 | 352 |
| BabyLedWeaning | 107 | 1,262 | 31 |
| BabyBumpsCanada | 286 | 0 | 16 |
| BabyBumpsandBeyondAu | 359 | 0 | 21 |
| BeyondTheBumpUK | 268 | 0 | 18 |
| **Total** | **8,284** | **19,258** | **865** |

## Historical unread handoff — superseded by current update

At this handoff, **all 131 A card chunks and all 865 candidate full-reading chunks are human-unread**. No quote file `voice/reddit-deep-01.jsonl` has been created with invented or prematurely selected records. The exact current unread names are enumerated in the frozen indexes/queue above. B/C bodies remain in the named source-window `.jsonl.gz` files and are explicitly untriaged/unread. Older raw-file records outside the six-month window are preserved but not researched.

Next: parent allocates all A card chunks in disjoint batches, using the triage brief and distinct TSV filenames. After human keep/drop labels, assign every kept original unit and all available comments for full reading under `_tools/brief-reddit-deep-reading.md`. Each reader gets a new filename/id prefix, its own scratch directory and a source ledger. The initial 418 records remain frozen. New records use `source_class=reddit_archive`, `evidence_kind=archived_original`, original post/comment permalinks and source timestamps, with no names in selected quote/context. Exact speaker/stage must come from the quoted author; OP age never transfers to a commenter.

Work volume is now concrete: **131 card chunks first**, then up to **865 original chunks before triage exclusions**. Divide those counts across available readers rather than claiming the collection is already read. Triage may substantially reduce the full-reading workload; that reduction must be documented per id, not an arbitrary time or top-N cap. Source-specific reader notes will carry read/quoted totals; parent integrates them after verification and a safety audit.

Tools: `_tools/reddit_dataset_pipeline.py` scans, date-filters and splits native files; `_tools/reddit_deep_filter.py` builds the transparent tiers; `_tools/build_reddit_deep_corpus.py` builds the immutable candidate corpus and relations. Zstandard dependency was installed locally for Python 3.12; package/interpreter paths are in the tool docstrings and source. Do not rerun builders over these frozen output directories; use a new version for any changed filter/corpus.
