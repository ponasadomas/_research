# Reddit reading ledger — R13 (prefix sb13), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (second chunk set). Voice file: `voice/reddit-r13.jsonl`. Scratch (spec scripts, build helper, chunk dumps): `scratchpad/R13/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1b-keep_purchase-001` … `-006`, `read-v1b-keep_success-001`, `-002`) |
| units in those chunks | 125 (purchase 16/15/17/17/18/15; success 15/12) |
| units read in full (post + every OP reply) | 125 |
| units excluded entirely | 5 |
| units with passages excluded (rest quoted) | 15 |
| units read, nothing worth quoting | 0 |
| quotes written | 320 (sb13-0001 … sb13-0320), `verify_quotes.py` 0 failed |

Counts are of quotes chosen, never of people.

## Units excluded entirely (not quoted)

| unit | reason |
|---|---|
| `beyondthebump-1wykpw5` | post is about infant-death fear as the purchase reason (monitor sock) |
| `NewParents-1wzd6i8` | monitor alarm and hospital admission for a respiratory illness: medical/safety incident |
| `NewParents-1x34xct` | weighted sleep blanket and breathing risk: safe-sleep content |
| `beyondthebumpUK-1x5mqu0` | travel-cot mattress gap and entrapment fear: safe-sleep content |
| `beyondthebump-1xctqsr` | swaddled and clipped into a smart bassinet while showing rolling signs: safe-sleep content |

## Units with passages excluded (other passages quoted)

| unit | passage not copied | why |
|---|---|---|
| `NewParents-1wshay4` | lines about spiralling mood and seeing a doctor (post + `pclj4an`) | mental-health wording |
| `NewParents-1wvytj6` | newborn hard to wake; fear something will happen when left in bassinet | safe-sleep / infant-harm fear |
| `sleeptrain-1wwlawg` | baby found on belly, nose/breathing scare that prompted the purchase | safe-sleep incident |
| `beyondthebumpUK-1wzqvuy` | self-reported diagnosis and anxiety-treatment lines | mental-health content |
| `NewParents-1x0vxy1` | adult bed, blanket, head on rails | unsafe sleep surfaces |
| `NewParents-1x2fpzu` | adding a mattress to a travel cot | safe-sleep risk |
| `NewParents-1x2wzz2` | "nervous breakdown" and "mental state" lines | mental-health wording (tracking-app lines quoted instead) |
| `beyondthebumpUK-1x3ir5j` | parent falling asleep in unsafe positions with first baby | safe-sleep incident |
| `NewParents-1x4no2l` | SIDS-peak and weighted-sack worry | infant-death fear / safe-sleep |
| `sleeptrain-1wxy229` | "PPD" wording trimmed out of sb13-0057 | mental-health wording |
| `sleeptrain-1x92yfi`, `NewParents-1x2pein`, `sleeptrain-1x9c6j8` | mental-health mentions (PPA/PPD, "mental health"); swaddle-rolling safety argument in 1x9c6j8; floor-mattress bedsharing in 1x2pein | mental-health / safe-sleep |
| `sleeptrain-1x9g9fd` | coughing from crying; a study claim | distress detail; claim would need fact-checking |
| `FirstTimeMom-1xcpe2h` | monitor-sock tip, lip-tie and probiotic tips | safety monitoring; medical advice |

Medical causes mentioned (reflux, ear tubes, apnoea query, iron test, dairy intolerance) were noted, never quoted as causes.

Duplicate cross-posts read in full but quoted once: `sleeptrain-1x55uj8` / `beyondthebump-1x552qz`; `sleeptrain-1x7f8sz` / `NewParents-1x7fbyb`; `sleeptrain-1wu1aof` / `beyondthebump-1wu2fqt` (one added line quoted from the second).

## Per-unit table (chunk · unit · quotes)

| chunk | unit | quotes |
|---|---|---|
| keep_purchase-001 | `beyondthebump-1wpvngj` | 3 |
| keep_purchase-001 | `sleeptrain-1wqe5ox` | 1 |
| keep_purchase-001 | `beyondthebump-1wrasjs` | 2 |
| keep_purchase-001 | `sleeptrain-1wrcsar` | 1 |
| keep_purchase-001 | `sleeptrain-1wrqgst` | 4 |
| keep_purchase-001 | `sleeptrain-1ws3m1u` | 1 |
| keep_purchase-001 | `NewParents-1wshay4` | 5 |
| keep_purchase-001 | `sleeptrain-1wsi77i` | 3 |
| keep_purchase-001 | `sleeptrain-1wsr744` | 2 |
| keep_purchase-001 | `sleeptrain-1wt80q0` | 5 |
| keep_purchase-001 | `beyondthebumpUK-1wuervk` | 1 |
| keep_purchase-001 | `sleeptrain-1wullyg` | 2 |
| keep_purchase-001 | `sleeptrain-1wuq7nl` | 1 |
| keep_purchase-001 | `sleeptrain-1wv0c78` | 2 |
| keep_purchase-001 | `sleeptrain-1wvjwsz` | 1 |
| keep_purchase-001 | `sleeptrain-1wvq8xs` | 1 |
| keep_purchase-002 | `NewParents-1wvytj6` | 4 |
| keep_purchase-002 | `Mommit-1wvzsoa` | 1 |
| keep_purchase-002 | `beyondthebumpUK-1ww70o0` | 2 |
| keep_purchase-002 | `sleeptrain-1wwlawg` | 3 |
| keep_purchase-002 | `beyondthebumpUK-1wwz4gp` | 1 |
| keep_purchase-002 | `sleeptrain-1wxqb6k` | 2 |
| keep_purchase-002 | `sleeptrain-1wxrrq3` | 4 |
| keep_purchase-002 | `sleeptrain-1wxy229` | 6 |
| keep_purchase-002 | `sleeptrain-1wy3s76` | 2 |
| keep_purchase-002 | `sleeptrain-1wy7b3w` | 3 |
| keep_purchase-002 | `sleeptrain-1wy96t0` | 5 |
| keep_purchase-002 | `beyondthebump-1wykpw5` | 0 |
| keep_purchase-002 | `NewParents-1wzd6i8` | 0 |
| keep_purchase-002 | `beyondthebumpUK-1wzqvuy` | 4 |
| keep_purchase-002 | `NewParents-1x0vxy1` | 2 |
| keep_purchase-003 | `NewParents-1x0y5kq` | 5 |
| keep_purchase-003 | `beyondthebumpUK-1x0z7ue` | 2 |
| keep_purchase-003 | `sleeptrain-1x1v40b` | 7 |
| keep_purchase-003 | `sleeptrain-1x260fh` | 2 |
| keep_purchase-003 | `beyondthebump-1x28ee6` | 1 |
| keep_purchase-003 | `sleeptrain-1x2akqs` | 2 |
| keep_purchase-003 | `NewParents-1x2fcw7` | 1 |
| keep_purchase-003 | `NewParents-1x2fpzu` | 1 |
| keep_purchase-003 | `sleeptrain-1x2mskb` | 2 |
| keep_purchase-003 | `sleeptrain-1x2qwr4` | 7 |
| keep_purchase-003 | `NewParents-1x2wzz2` | 4 |
| keep_purchase-003 | `NewParents-1x34xct` | 0 |
| keep_purchase-003 | `sleeptrain-1x3h9dx` | 3 |
| keep_purchase-003 | `beyondthebumpUK-1x3ir5j` | 4 |
| keep_purchase-003 | `toddlers-1x3ose5` | 2 |
| keep_purchase-003 | `sleeptrain-1x3pzvm` | 2 |
| keep_purchase-003 | `sleeptrain-1x49d74` | 4 |
| keep_purchase-004 | `Mommit-1x4krb3` | 3 |
| keep_purchase-004 | `toddlers-1x4n2an` | 2 |
| keep_purchase-004 | `NewParents-1x4no2l` | 2 |
| keep_purchase-004 | `sleeptrain-1x4r1ub` | 3 |
| keep_purchase-004 | `sleeptrain-1x4w7t2` | 3 |
| keep_purchase-004 | `beyondthebump-1x552qz` | 2 |
| keep_purchase-004 | `sleeptrain-1x55uj8` | 1 |
| keep_purchase-004 | `sleeptrain-1x5fhps` | 2 |
| keep_purchase-004 | `sleeptrain-1x5foxq` | 2 |
| keep_purchase-004 | `beyondthebumpUK-1x5mqu0` | 0 |
| keep_purchase-004 | `sleeptrain-1x61oof` | 4 |
| keep_purchase-004 | `beyondthebumpUK-1x62noy` | 2 |
| keep_purchase-004 | `beyondthebumpUK-1x6fqgn` | 1 |
| keep_purchase-004 | `sleeptrain-1x7f8sz` | 3 |
| keep_purchase-004 | `NewParents-1x7fbyb` | 2 |
| keep_purchase-004 | `sleeptrain-1x7s3lr` | 4 |
| keep_purchase-004 | `sleeptrain-1x7v29i` | 2 |
| keep_purchase-005 | `sleeptrain-1x89e9i` | 3 |
| keep_purchase-005 | `NewParents-1x8h5ui` | 1 |
| keep_purchase-005 | `sleeptrain-1x8nyvq` | 2 |
| keep_purchase-005 | `sleeptrain-1x8w8so` | 5 |
| keep_purchase-005 | `sleeptrain-1x92yfi` | 3 |
| keep_purchase-005 | `sleeptrain-1x952j9` | 2 |
| keep_purchase-005 | `sleeptrain-1x99yep` | 2 |
| keep_purchase-005 | `sleeptrain-1x9b8en` | 4 |
| keep_purchase-005 | `sleeptrain-1x9c6j8` | 2 |
| keep_purchase-005 | `beyondthebump-1x9ngjg` | 4 |
| keep_purchase-005 | `sleeptrain-1x9vaem` | 4 |
| keep_purchase-005 | `sleeptrain-1xa220s` | 1 |
| keep_purchase-005 | `sleeptrain-1xaixrr` | 4 |
| keep_purchase-005 | `sleeptrain-1xatmjl` | 3 |
| keep_purchase-005 | `NewParents-1xbm9i1` | 2 |
| keep_purchase-005 | `sleeptrain-1xbnld4` | 2 |
| keep_purchase-005 | `NewParents-1xbwaxs` | 1 |
| keep_purchase-005 | `sleeptrain-1xby01p` | 2 |
| keep_purchase-006 | `NewParents-1xc03wo` | 2 |
| keep_purchase-006 | `sleeptrain-1xcbqe0` | 2 |
| keep_purchase-006 | `sleeptrain-1xcddf9` | 2 |
| keep_purchase-006 | `sleeptrain-1xcfrm1` | 1 |
| keep_purchase-006 | `sleeptrain-1xcmw6p` | 2 |
| keep_purchase-006 | `beyondthebump-1xctqsr` | 0 |
| keep_purchase-006 | `sleeptrain-1xcwhi4` | 3 |
| keep_purchase-006 | `sleeptrain-1xcy90v` | 3 |
| keep_purchase-006 | `sleeptrain-1xd2gbc` | 4 |
| keep_purchase-006 | `sleeptrain-1xdfq3r` | 2 |
| keep_purchase-006 | `toddlers-1xdhll2` | 2 |
| keep_purchase-006 | `sleeptrain-1xdhv8a` | 5 |
| keep_purchase-006 | `sahm-1xdtjo3` | 1 |
| keep_purchase-006 | `sleeptrain-1xe5hy6` | 2 |
| keep_purchase-006 | `sleeptrain-1xedvpk` | 1 |
| keep_success-001 | `sleeptrain-1wr0c28` | 2 |
| keep_success-001 | `sleeptrain-1wru3az` | 2 |
| keep_success-001 | `sleeptrain-1wrx8a1` | 6 |
| keep_success-001 | `sleeptrain-1ws58sy` | 3 |
| keep_success-001 | `beyondthebump-1wsb5ix` | 1 |
| keep_success-001 | `sleeptrain-1wu1aof` | 3 |
| keep_success-001 | `beyondthebump-1wu2fqt` | 2 |
| keep_success-001 | `sleeptrain-1wvx58k` | 2 |
| keep_success-001 | `sleeptrain-1ww8p3j` | 5 |
| keep_success-001 | `NewParents-1wwfqr6` | 1 |
| keep_success-001 | `NewParents-1wxygrd` | 1 |
| keep_success-001 | `sleeptrain-1x12k4k` | 3 |
| keep_success-001 | `sleeptrain-1x1amzb` | 2 |
| keep_success-001 | `NewParents-1x2pein` | 2 |
| keep_success-001 | `sleeptrain-1x2t2vp` | 2 |
| keep_success-002 | `sleeptrain-1x3att3` | 2 |
| keep_success-002 | `sleeptrain-1x3gj3r` | 6 |
| keep_success-002 | `sleeptrain-1x3sqmh` | 3 |
| keep_success-002 | `daddit-1x4i0jx` | 2 |
| keep_success-002 | `sleeptrain-1x5k2qu` | 3 |
| keep_success-002 | `sleeptrain-1x7z0r7` | 5 |
| keep_success-002 | `sleeptrain-1x8hv51` | 3 |
| keep_success-002 | `sleeptrain-1x9g9fd` | 5 |
| keep_success-002 | `sleeptrain-1xadgsv` | 4 |
| keep_success-002 | `sleeptrain-1xbuwdk` | 3 |
| keep_success-002 | `sleeptrain-1xchbcv` | 3 |
| keep_success-002 | `FirstTimeMom-1xcpe2h` | 4 |

## How to continue

Nothing assigned is unread. Re-running this reader would duplicate ids: never re-run; a new reader gets a new prefix.
