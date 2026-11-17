# Reddit reading ledger — R17 (prefix sb17), 2026-10-25

Brief: `../_shared/_tools/brief-reading.md`. Corpus: `_raw/reddit/read-v1b/chunks.jsonl` (second chunk set). Voice file: `voice/reddit-r17.jsonl`. Scratch (spec files, `add.py` builder, chunk dumps, per-chunk log): `scratchpad/R17/`.

## Counts

| step | count |
|---|---|
| chunks assigned | 8 (`read-v1b-keep_core-021` … `-028`) |
| units in those chunks | 142 (18/19/14/20/17/16/22/16) |
| units read in full (post + every OP reply) | 142 |
| units excluded entirely | 5 |
| cross-posts read, quoted from the other copy only | 2 |
| units read, nothing worth quoting | 2 |
| units with passages excluded (rest quoted) | 22 |
| units quoted | 133 |
| quotes written | 372 (sb17-0001 … sb17-0372), `verify_quotes.py` 0 failed |

Counts are of quotes chosen, never of people.

## Units excluded entirely (not quoted)

| unit | chunk | reason |
|---|---|---|
| `NewParents-1wznc4o` | 024 | safe-sleep content: sleepwear fit for an underweight baby close to rolling |
| `NewParents-1x06br2` | 024 | safe-sleep product question and infant-death fear |
| `Mommit-1x1fbhj` | 027 | safe-sleep content: sleep sack twisting on a toddler |
| `sleeptrain-1x212de` | 028 | wording of an urge toward physical force toward a child, plus crisis wording |
| `NewParents-1x2a6fd` | 028 | safe-sleep content: swaddled baby nearly rolling, bed-sharing anxiety |

## Cross-posts and units with nothing to quote

| unit | chunk | note |
|---|---|---|
| `beyondthebump-1wz564w` | 023 | word-for-word cross-post of `NewParents-1wz51rt`; quoted from that copy |
| `beyondthebump-1x1aoyd` | 027 | word-for-word cross-post of `NewParents-1x1aqu9`; quoted from that copy |
| `NewParents-1wyg8dp` | 022 | read; early wakings after a switch from formula, nothing beyond what other posts say better |
| `NewParents-1x1ml2z` | 027 | read; short post about morning crying, nothing distinctive |

## Units with passages excluded (other passages quoted)

| unit | passage not copied | why |
|---|---|---|
| `sleeptrain-1wy1012` | closing wish to walk out and disappear | mental-health wording |
| `beyondthebump-1wy4p5g` | "depressed and hopeless" line; question about giving the child something to stay asleep | mental-health wording; medication advice |
| `beyondthebump-1wyp8ak` | dozing while holding the baby during feeds | safe-sleep incident |
| `AttachmentParenting-1wzhybp` | "how much longer I can keep going"; anxiety detail | mental-health wording |
| `NewParents-1wzmq1i` | quoted only non-crisis lines (the "traumatic/grief" line is quoted and restricted) | mental-health adjacent |
| `NewParents-1wzmwqf` | public breakdown line | mental-health wording |
| `beyondthebump-1wzvmjl` | postpartum-depression sentence; father's bed-sharing detail | mental-health; safe-sleep |
| `sleeptrain-1x0dh04` | "terrified about my mental health", "feel like death"; baby stuck on belly | mental-health; safe-sleep |
| `Mommit-1x0e0p8` | postpartum mental-health line; nightly painkiller | mental-health; medication |
| `NewParents-1x0ei0f` | nightly painkiller use | medication advice |
| `NewParents-1x0f17c` | postpartum anxiety/depression paragraph | mental-health content |
| `NewParents-1x0uzt7` (`peom989`) | father's fear of rolling onto or suffocating the baby | infant-death fear |
| `AttachmentParenting-1x0k0qy` | reflux remedy | medical treatment, never diagnosed |
| `sleeptrain-1x11imt` | pregnancy-loss line | bereavement, never a hook |
| `sleeptrain-1x112zg` (`peu5ay2`) | "very depressed / mental health" line | mental-health wording |
| `NewParents-1x176k6` | medication; PPD/PPA reply | medication; mental-health |
| `beyondthebump-1x1b0v8` | contact-sleep safety worry; loss of a previous baby | safe-sleep; infant-loss |
| `NewParents-1x1ccxd` | "felt like dying" | crisis wording |
| `toddlers-1x1gsbe` | injury during a breath-holding spell | child-injury incident |
| `toddlers-1wxxdyt` (`pexrjge`) | father catching the toddler before she falls off the bed | safety incident |
| `beyondthebumpUK-1x1nna2` | postpartum-rage line | mental-health wording |
| `sleeptrain-1x25qdb` (`pf5nic1`) | PPA aside | mental-health wording |

## What has and hasn't been read

All 142 units in `read-v1b-keep_core-021` … `-028` read in full. Nothing unread.
