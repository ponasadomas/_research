# Reddit reading ledger — R46 (wave 3, sleep-baby, core chunks)

Reader R46 · id prefix `sb46` · voice file `voice/reddit-r46.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 9 (`read-w3-keep_core-013` … `read-w3-keep_core-021`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 151 (16/14/18/14/23/22/16/11/17; posts dated 2026-04-07 → 2026-04-10; OP replies to 2026-08-17) |
| Units read in full | 151 |
| Units excluded entirely | 15 (11 for safe-sleep, infant-death-fear, crisis-wording or out-of-age content; 4 duplicate cross-posts) |
| Units quoted | 136 |
| Quotes written | 576 (ids sb46-0001 … sb46-0576, unique) |
| Restricted quotes | 5 (listed in `synthesis/reader-notes-r46.md`) |
| possible_promo quotes | 0 (no seeded-looking post in these chunks) |
| verify_quotes.py | 576 quotes, 0 failed |

Per chunk (units / units quoted / quotes): 013 16/15/68 · 014 14/14/69 · 015 18/15/67 · 016 14/13/66 · 017 23/20/65 · 018 22/18/69 · 019 16/16/63 · 020 11/10/60 · 021 17/15/49.

Chunk-to-unit list: `scratchpad/R46/units.txt`. Short-form quote sources: `scratchpad/R46/q013a.jsonl` … `q021b.jsonl`, built into the voice file by `scratchpad/R46/build.py` (types `guilt`/`gave_up` written in the short form are mapped to `pain`/`failure_story`; seed themes are put first). Id index: `scratchpad/R46/index.txt`.

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Mommit-1sem5kl.txt` | sleepwear-near-crawling question is the whole post |
| `../_shared/_raw/reddit-2026/units/NewParents-1sf37dw.txt` | bedsharing detail is the whole post |
| `../_shared/_raw/reddit-2026/units/toddlers-1sf3ukz.txt` | duplicate cross-post of `NewParents-1sf3si2` (identical text, no distinct OP reply) |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sfamtk.txt` | duplicate cross-post of `NewParents-1sfabi4` (identical text, no OP reply) |
| `../_shared/_raw/reddit-2026/units/toddlers-1sfsv4o.txt` | child is over 36 months; post also centres on discipline and harsh words |
| `../_shared/_raw/reddit-2026/units/NewParents-1sfz5nb.txt` | newborn sleep-position detail and a medical question throughout |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sg16s9.txt` | chest-sleeping / cosleeping detail is the core of the post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sg1n6g.txt` | infant-death fear in the parents' bed is the trigger scene |
| `../_shared/_raw/reddit-2026/units/toddlers-1sg9haj.txt` | child is 3.5 years (over 36 months) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sgfuke.txt` | bedsharing plus sleepwear-near-rolling detail throughout |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sgfvf7.txt` | same post as `NewParents-1sgfuke`; same reason |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1sgfz48.txt` | bedsharing with a low-birth-weight baby is the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sgzggk.txt` | falls from an adult bed while cosleeping; safety incident |
| `../_shared/_raw/reddit-2026/units/toddlers-1shc94m.txt` | mental-health crisis wording |
| `../_shared/_raw/reddit-2026/units/NewParents-1shcg0a.txt` | crisis wording plus bedsharing detail |

## Lines read but not quoted inside quoted units (neutral)

- Bedsharing, cosleeping, chest or lounger sleep, and "into our bed at 4am" lines were skipped in: `toddlers-1sehveq`, `Parenting-1selc6c`, `NewParents-1semtix`, `sleeptrain-1seqgqg`, `sleeptrain-1sesycm`, `toddlers-1sesyqw`, `sleeptrain-1seu2k2`, `sleeptrain-1sevoqt`, `sleeptrain-1sexkvr`, `NewParents-1sfaseb`, `toddlers-1sfugnz`, `sleeptrain-1sftz1r`, `NewParents-1sg9g8d`, `sleeptrain-1sgcptc`, `sleeptrain-1sgl4se`, `sleeptrain-1sgmvo2`, `sleeptrain-1sgmug7`, `toddlers-1sgn1an` (a sleep-shift reply), `sleeptrain-1sgo482`, `sleeptrain-1sgu8im`, `sleeptrain-1sgx8fh`, `sleeptrain-1sgxovg`, `AttachmentParenting-1sh3euf`, `NewParents-1sh3upx`, `NewParents-1sh54ld`, `NewParents-1shgs2e`, `Mommit-1shazy4`, `toddlers-1shhvfk`, `NewParents-1sg7cmy`.
- A night incident with the baby and the mother's own medical help-seeking: `sahm-1sewq5d` (only the husband's words and the couple's night arguments quoted).
- Medication, supplements and named conditions (reflux medicine, antibiotics, painkillers, melatonin, gas drops, essential oils, homeopathy, eczema, croup, coeliac, ear tubes, allergy tests) were skipped wherever they appeared; three borderline lines were quoted and restricted.
- A parent's own angry reaction at night: one line in `AttachmentParenting-1sh3euf`, not quoted. A line on how a twin was handled at bedtime: `toddlers-1sgbrvp`, not quoted.
- `FirstTimeMom-1sfp06a`: only one neutral line quoted; the rest is medicine and breathing-check worry.
- Duplicates where only a distinct OP reply was quoted: `beyondthebump-1sfhmsl` (post = `Parenting-1sfh7oq`), `NewParents-1sgn3ck` (post = `toddlers-1sgn1an`), `Parenting-1sgskpz` (post = `sleeptrain-1sgsjmw`), `beyondthebump-1shgt0t` (post = `NewParents-1shgs2e`). Same-author speaker: the `1sfh7oq`/`1sfhmsl` author calls herself "momma" in the replies, so both are `new_mother`.

## How to continue

Nothing in these nine chunks is unread. Do not re-run R46; it appends to its own file only.
