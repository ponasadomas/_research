# July 2025 first-wave packet

Prepared from **all 1,661 tier-A candidates created in calendar July 2025**, across all nine source communities. No relevance ranking, score cut, cap or automatic keep decision. Every card/unit starts **untriaged and unread**. The complete six-month source inventory remains unchanged; **6,623 August–December A candidates** and all B/C material remain queued.

Brief: `_tools/brief-reddit-july-wave.md`. Exact machine counts, including every source/topic combination: `summary.json`.

| Community | July A candidates | Triage card chunks | Primary reading chunks | Available identifiable OP replies |
|---|---:|---:|---:|---:|
| BabyBumps | 357 | 6 | 26 | unavailable |
| BabyBumpsCanada | 58 | 1 | 4 | unavailable |
| BabyBumpsandBeyondAu | 80 | 2 | 5 | unavailable |
| BabyLedWeaning | 17 | 1 | 2 | 26 |
| BeyondTheBumpUK | 43 | 1 | 4 | unavailable |
| ExclusivelyPumping | 233 | 4 | 15 | unavailable |
| NewParents | 469 | 8 | 32 | unavailable |
| beyondthebump | 252 | 4 | 18 | unavailable |
| workingmoms | 152 | 3 | 21 | 592 |
| **Total** | **1,661** | **30** | **127** | **618 available replies** |

Primary topic counts, assigned by the saved broad regex rather than human interpretation: sleep 391; pumping/feeding 347; pregnancy/birth 254; household support 238; other 128; solids/food 93; work return 84; development/play 72; registry/gear 54. Posts can mention multiple topics; overlapping counts are separately recorded in `summary.json`.

1. Triage **all 30 card chunks**, enumerated in `triage-cards-index.jsonl`, before any keep/read claim. `candidates.jsonl` is the exact candidate-id/date inventory. Use distinct reader TSVs and compare ids against the assigned manifest.
2. For human-kept posts, primary units contain the **whole original post plus every identifiable OP reply available through the archive's 2025-12-31 boundary**, including replies written after July. Main-community and country-community comment sources remain unavailable; their units are accurately labeled post-only. `primary-index.jsonl` names individual units, exact reply ids, original URLs/dates and scope.
3. `primary-chunks-index.jsonl` and `primary-reading-queue.tsv` enumerate all candidate primary chunks; they do **not** imply that untriaged candidates should automatically be read/quoted. Primary reading chunks total **4,662,766 UTF-8 bytes**: source post bodies are 1,977,621 bytes and OP reply bodies 187,055 bytes; the remainder is traceability metadata and delimiters.
4. **3,181 other archived comments** are saved as a separate unread auxiliary queue in **164 gzip files**, totaling **979,769 compressed bytes**. `auxiliary-index.jsonl` provides every path and comment id. Do not count them read by reading an OP unit. If necessary to understand an OP reply, read and log the exact parent comment rather than infer context.

All exact quoted text remains in saved originals; no quote extraction or network requests occurred while preparing this packet. No live-thread completeness is claimed. The six-month frozen source/card/corpus indexes and reading queue were hashed before and after preparation; unchanged hashes are saved in `six-month-baseline-hashes.json`.
