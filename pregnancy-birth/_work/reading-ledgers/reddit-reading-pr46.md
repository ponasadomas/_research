# Reddit reading ledger — PR46 (wave 3, purchase chunks)

Reader PR46 · id prefix `pb46` · voice file `voice/reddit-pr46.jsonl` · notes `synthesis/reader-notes-pr46.md` · scratch `scratchpad/PR46/` (`units.txt`, `notes.txt`, `restricted.txt`).

Brief: `../_shared/_tools/prompt-pregnancy-reader-w3.txt` → `../_shared/_tools/brief-reading.md`. Window: posts 1 Apr – 3 May 2026 (the first seven purchase chunks of wave 3).

| step | count |
|---|---|
| chunks assigned | 7 (`read-w3-keep_purchase-001` … `-007`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in them | 155 |
| units read in full (post + every OP reply) | 155 |
| units excluded under the lines not to cross | 6 |
| units flagged as likely seeded / AI-written / promo, not quoted | 13 |
| crossposts (same author, same text), quoted once | 2 duplicates not quoted |
| units read, nothing quotable (medical-only or thin) | 13 |
| units with at least one quote | 121 |
| quotes written | 259 (pb46-0001 … pb46-0259), 12 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr46.jsonl` → 259 quotes, 0 failed |

Unread: none. Every unit in the seven chunks was read to the end.

## Excluded (neutral reasons, never quoted)

| unit | reason |
|---|---|
| pregnant-1sexxeq | author promoting own app with a settlement link |
| pregnant-1skr065 | request for a donated item |
| pregnant-1sq58eh | thread turns on a decision to end a pregnancy |
| PregnancyUK-1srjc1r | screening question in the context of repeated loss |
| pregnant-1sqwd6j | author's age unclear ("really young"), possible minor |
| Doulas-1svavdo | child-safety and family-safety content (infant images taken without consent) |

## Flagged, not quoted (likely seeded, promo or AI-written)

BabyBumps-1shky0j, BabyBumps-1svdohq, BabyBumps-1stb5wa (Momcozy belly-band/birthing-ball template); BabyBumps-1sscbii + NewParents-1ssdn5w (one compression-sock text posted twice in 75 minutes); BabyBumps-1so9ezh (BabyRx vitamin); BabyBumps-1soj6b5 (links its own contraction-timer web app); beyondthebumpUK-1sf54de (labour gown); BabyBumps-1sitd27 (Momcozy x2, Grownsy, "(unsponsored)"); NewParents-1su6lvg (bottle-washer, AI-styled); pregnant-1su0uhu (Teva sandals, pasted from a BabyCenter page); pregnant-1svbk2x (Skechers sandals); Mommit-1slwij0 (body pillow, AI-styled). Reasons in `scratchpad/PR46/notes.txt` and the reader notes.

## Crossposts

PregnancyUK-1s9f57h = pregnant-1s9f5t5 (TENS machine; the PregnancyUK copy quoted). BabyBumps-1sg81mx = pregnant-1sg86dg (early boutique scan; the r/pregnant copy quoted).

## Read, nothing quoted

Medical-only: PregnancyUK-1sjh9zj, pregnant-1spty1l, pregnant-1stg7mz, beyondthebumpUK-1syzpj5, pregnant-1t14wcv. Thin: BabyBumps-1sb13yh, BabyBumps-1slwor5, pregnant-1so4lzj, pregnant-1srn04r, beyondthebumpUK-1srugwf, pregnant-1svpdnv, beyondthebumpUK-1t06rzy, BabyBumps-1t2ib0b.

## How to continue

Nothing left in PR46's assignment. Never re-run PR46 against this voice file (append-only, ids would collide).
