# Reddit reading ledger — PR68 (wave 3, core chunks 145–154)

Reader PR68 · id prefix `pb68` · voice file `voice/reddit-pr68.jsonl` · notes `synthesis/reader-notes-pr68.md` · scratch `scratchpad/PR68/` (`units.tsv`, `ledger.tsv` per-unit status and quote count, `restricted.txt`, `c145.json` … `c154.json` record inputs).

Brief: `../_shared/_tools/prompt-pregnancy-reader-w3.txt` → `../_shared/_tools/brief-reading.md`. Window: posts 3–7 June 2026.

| step | count |
|---|---|
| chunks assigned | 10 (`read-w3-keep_core-145` … `-154`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in them | 165 (13 + 18 + 13 + 19 + 15 + 23 + 12 + 17 + 15 + 20) |
| units read in full (post + every OP reply) | 165 |
| units excluded under the lines not to cross | 17 |
| units read, nothing quotable (medical-only, thin or off-niche) | 34 |
| units with at least one quote | 114 |
| quotes written | 246 (pb68-0001 … pb68-0246), 20 restricted |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr68.jsonl` → 246 quotes, 0 failed |

Unread: none. Every unit in the ten chunks was read to the end.

## Excluded (neutral reasons, never quoted)

| unit | reason |
|---|---|
| pregnant-1tw024p | substance use |
| pregnant-1tw5tt3 | substance use |
| beyondthebump-1tw8x4d | severe mental-health post |
| pregnant-1twrnlj | centred on previous pregnancy loss |
| pregnant-1twu7aw | centred on medical complications and eating-disorder history |
| pregnant-1twzlpi | severe mental-health post with crisis wording |
| pregnant-1tx4202 | severe mental-health post with crisis wording |
| pregnant-1txi64z | centred on previous pregnancy loss |
| beyondthebump-1txlavp | relationship-safety concern |
| beyondthebump-1txr7ln | severe mental-health post with crisis wording |
| beyondthebump-1ty9a71 | substance use |
| pregnant-1tygzm0 | post weighing whether to continue the pregnancy |
| PregnancyUK-1tykaja | acute medical emergency at birth |
| FirstTimeMom-1typf3p | crisis wording |
| pregnant-1tz3p4w | mentions considering ending the pregnancy (excluded under the "pressure or thought of ending the pregnancy, even in passing" rule) |
| pregnant-1tzbxps | centred on early-pregnancy viability uncertainty after a loss |
| pregnant-1tzbzul | possible family-safety concern |

## Read in full, nothing quoted

BabyBumps-1tvymhu, beyondthebump-1tvyuzn, BabyBumps-1tw090z, pregnant-1tw8e5n, pregnant-1tw9am8, pregnant-1twceko, pregnant-1tweliv, pregnant-1twjrjr, pregnant-1tx346v, pregnant-1tx4i37, pregnant-1tx6iad, pregnant-1tx7wg7, pregnant-1txglb3, PregnancyUK-1txhok1, pregnant-1txqt3l, pregnant-1txv3g2, beyondthebump-1txzpn0, pregnant-1ty00bv, pregnant-1ty0g94, pregnant-1ty17gm, pregnant-1ty1m5b, pregnant-1ty6uxd, pregnant-1ty82uu, pregnant-1tyckw0, pregnant-1tydee0, pregnant-1tyfioh, pregnant-1tylvo0, pregnant-1tyxcdl, pregnant-1tz0xv5, pregnant-1tz44k6, BabyBumps-1tz716y, BabyBumps-1tzcr4x, pregnant-1tzdwmg, PregnancyUK-1tzhrl9. Mostly single-symptom or medication questions, sexual-health or intimacy posts, and one resource link (Embryotox, pregnant-1tylvo0).

## How to continue

Nothing left in these chunks. Per-unit status and quote counts are in `scratchpad/PR68/ledger.tsv`. Never append to `voice/reddit-pr68.jsonl` from another agent.
