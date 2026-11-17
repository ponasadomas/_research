# Reddit reading ledger — R41 (wave 3, sleep-baby, purchase chunks)

Reader R41 · id prefix `sb41` · voice file `voice/reddit-r41.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 8 (`read-w3-keep_purchase-001` … `read-w3-keep_purchase-008`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 167 (25/25/14/20/27/14/18/24; posts dated 2026-04-01 → 2026-05-13; OP replies to 2026-08-25) |
| Units read in full | 167 |
| Units excluded entirely | 10 (7 for safe-sleep or mental-health content, 3 duplicate cross-posts) |
| Units read, nothing quoted | 1 (`NewParents-1t31ciw`, see below) |
| Units quoted | 156 |
| Quotes written | 508 (ids sb41-0001 … sb41-0508, unique) |
| Restricted quotes | 16 (listed in `synthesis/reader-notes-r41.md`) |
| possible_promo quotes | 9, from 6 units (never counted as parent voice) |
| verify_quotes.py | 508 quotes, 0 failed |

Per chunk (units / units quoted / quotes): 001 25/23/79 · 002 25/25/71 · 003 14/14/72 · 004 20/19/65 · 005 27/26/65 · 006 14/12/45 · 007 18/15/47 · 008 24/22/64.

Chunk-to-unit list: `scratchpad/R41/units.txt`. Short-form quote sources: `scratchpad/R41/q01–q10.jsonl`, built into the voice file by `scratchpad/R41/build.py`. Working log (per-batch exclusions, lines not quoted, money): `scratchpad/R41/log.md`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1sdifjn.txt` | duplicate cross-post of `sleeptrain-1sdi7lx` (identical text) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sdlayz.txt` | sleepwear-near-rolling safe-sleep detail is the whole post |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1su4g0o.txt` | swaddle arms-out change because the baby is starting to roll (sleepwear-near-rolling detail throughout) |
| `../_shared/_raw/reddit-2026/units/NewParents-1szpvsc.txt` | safe-sleep detail (rolling) is the whole post; also a 4am monitor purchase, not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1t2unm5.txt` | bassinet safe-sleep fear plus mental-health treatment detail throughout |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1t53rxk.txt` | rolling while in a sleep suit, suit recall (sleepwear-near-rolling detail is the whole post) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1t53sji.txt` | same post as `sleeptrain-1t53rxk` in another sub; same reason |
| `../_shared/_raw/reddit-2026/units/NewParents-1t53sxz.txt` | same post as `sleeptrain-1t53rxk` in another sub; same reason |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tbi8qn.txt` | transition swaddle bought because the baby shows signs of rolling (sleepwear-near-rolling detail is the whole post) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tc6emd.txt` | duplicate cross-post of `sleeptrain-1tc6dpp` (identical text) |

Read, nothing quoted: `../_shared/_raw/reddit-2026/units/NewParents-1t31ciw.txt` (expecting parent asks which bassinet or play-yard setting to buy; the whole ask is about sleep-space suitability, so not quoted).

## Lines read but not quoted inside quoted units (neutral reasons)

Safe-sleep details (bed-sharing, rolling, sleepwear and room temperature, a recliner contact-sleep incident, SIDS-risk replies, an unsupervised tall bed at a grandparent's): `Mommit-1sbmjla`, `sleeptrain-1sdjjdc`, `sleeptrain-1sfh14g`, `sleeptrain-1sdmz51`, `sleeptrain-1sgh9y4`, `sleeptrain-1sgy911`, `sleeptrain-1sibvdu`, `sleeptrain-1sjkeq6`, `sleeptrain-1sl7hpd`, `toddlers-1sm9xtw`, `sleeptrain-1smiwhl`, `NewParents-1sl2ysk`, `sleeptrain-1sldo35`, `sleeptrain-1sn7gb5`, `sleeptrain-1sq5wde`, `NewParents-1sr7riy`, `NewParents-1ssiva7`, `sleeptrain-1staq91`, `beyondthebumpUK-1stgjc6`, `sleeptrain-1sw5g9a`, `NewParents-1swmxvc`, `beyondthebump-1sve9jt`, `NewParents-1syncqa`, `NewParents-1sz7ssw`, `Mommit-1t02fm3`, `NewParents-1t0chhe`, `NewParents-1t1r7np`, `NewParents-1t1pcx3`, `sleeptrain-1t1yth3`, `sleeptrain-1t4ycba`, `NewParents-1t84ulr`, `toddlers-1tb0rhr`, `sleeptrain-1tc5fc7`, `sleeptrain-1tb8mn8`, `Mommit-1tbk9c0`, `sleeptrain-1tc6z12`.
Medical or medication lines (named conditions, devices, pain relievers, gas drops, hospital visits): `sleeptrain-1sar6er`, `sleeptrain-1sbxvt3`, `sleeptrain-1saguit`, `beyondthebump-1skj0qb`, `sleeptrain-1smfuzj`, `sleeptrain-1sn7svy`, `sleeptrain-1sr8lp1`, `sleeptrain-1sqvddg`, `NewParents-1ss1eli`, `sleeptrain-1ssj64r`, `sleeptrain-1swrb4c`, `beyondthebumpUK-1sy0ujs`, `toddlers-1sym6hv`, `NewParents-1szaut5`, `sleeptrain-1t2ak4d`, `sleeptrain-1t4ddea`, `sleeptrain-1tb8wcb`, `NewParents-1tbhpy6`.
Mental-health crisis wording: `sleeptrain-1srdogs` (plus a medication line), `sleeptrain-1t6fzzj`, `sleeptrain-1ta6tfk`, `sleeptrain-1sq5wde`.
Verbal harshness toward a child: `Mommit-1tbo5g1` (one line). Door-holding at bedtime: `sleeptrain-1sq42oo` (one line). Insult exchanges: `NewParents-1t3jlwh`.

## Same-author and cross-post notes

- `beyondthebump-1t3jlem` has the same body as `NewParents-1t3jlwh`; the body is quoted once (from 1t3jlwh) and one distinct reply from 1t3jlem.
- Follow-up posts by one author, each quoted for its own new content: `sleeptrain-1s9ilze` → `sleeptrain-1sagzea`; `sleeptrain-1sdmz51` → `sleeptrain-1sgy911`; `sleeptrain-1sw5ebc` → `sleeptrain-1sxd1e7`; likely `NewParents-1sl2ysk` / `sleeptrain-1sldo35` / `sleeptrain-1sn7gb5` (one 7-month-old, second consultant, illness relapse); likely `sleeptrain-1t41nsu` / `sleeptrain-1t5p86k` (strong-willed 4-month-old).

## What has and hasn't been read

All 167 units in the eight assigned chunks were read in full, including every original-poster reply. Nothing is unfinished.
