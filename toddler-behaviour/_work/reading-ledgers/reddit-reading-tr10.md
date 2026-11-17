# Reddit full reads — TR10 (wave 2, 2026-06-25 → 08-24)

Brief: `../_shared/_tools/brief-reading.md`. Reader TR10, id prefix `tb10`, voice file `voice/reddit-tr10.jsonl`, scratch `scratchpad/TR10/`. Read 2026-10-25.

## Chunks assigned (from `_raw/reddit/read-w2/assignments.txt`)

| chunk | units |
|---|---|
| read-w2-keep_purchase-001 | 16 |
| read-w2-keep_purchase-002 | 8 |
| read-w2-keep_success-001 | 14 |
| read-w2-keep_success-002 | 11 |
| read-w2-keep_success-003 | 2 |
| read-w2-keep_otherside-001 | 15 |
| read-w2-keep_otherside-002 | 13 |
| read-w2-keep_otherside-003 | 12 |
| read-w2-keep_otherside-004 | 14 |
| read-w2-keep_otherside-005 | 13 |
| read-w2-keep_otherside-006 | 12 |
| **total** | **130** |

## Counts

- Units in chunks: 130
- Units read in full: 130 (none unfinished)
- Units excluded (not quoted, safety or medical lines): 9
- Units read, no quote (not a safety exclusion): 2
- Units quoted: 119
- Quotes written: 324 (tb10-0001 … tb10-0324), ids unique
- Restricted units (diagnosis / developmental or medical-condition question; only fear or strain quoted): 13 units, 35 quotes (see `synthesis/reader-notes-tr10.md`, "Restricted ids")
- Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr10.jsonl` → 324 quotes, 0 failed

## Units excluded (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/daddit-1ui40gi.txt` | medical treatment details |
| `../_shared/_raw/reddit-2026/units/toddlers-1ufb395.txt` | verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/Parenting-1ugd6ra.txt` | verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1un7twc.txt` | physical punishment of a child |
| `../_shared/_raw/reddit-2026/units/toddlers-1us1ijf.txt` | verbal harshness toward a child; developmental plan mentioned |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uu2khi.txt` | physical restraint; child body and medical topic |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uvuacw.txt` | suspected abuse; child-protection case |
| `../_shared/_raw/reddit-2026/units/Parenting-1uw76km.txt` | verbal harshness toward a child |
| `../_shared/_raw/reddit-2026/units/daddit-1v5nu9q.txt` | verbal harshness toward a child |

## Units read, no quote

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1ug4mmy.txt` | restricted (author's own diagnosis named); nothing qualifying as fear or strain |
| `../_shared/_raw/reddit-2026/units/pottytraining-1uzl5s7.txt` | duplicate cross-post of `Mommit-1uyxemb` (quoted there) |

## Other cross-posts (both copies read; quotes taken from different replies)

`toddlers-1unm0rv` / `pottytraining-1unm4y3`; `Parenting-1v7a9mh` / `pottytraining-1v7cx63`; `Mommit-1v7yguz` / `Parenting-1v7yiss`. Dedupe by post text at merge; quoted replies differ.

## Lines I kept out of quotes inside quoted units

Medication and laxative details, stool tests, ear tubes, rash creams (1ukzeb5, 1uws4j9, 1uzczf7, 1v5v7ph, 1v1o2tq, 1vccdbq update); child body / wiping / changing details (1v2ylps, 1v6be1h, 1vbv7ak, 1vfpv1h, 1v8n700); a partner "playing rough" and a parent carrying a fleeing child to the car seat (1vcsx5y, 1v9axzd); spanking talk in 1uwfc0c comments; a peer push and bruise (1uk0vsn).

## Possibly promotional units (quoted, flagged `possible_promo`)

`pottytraining-1utryn8` (plan found by "googling", a "tool to build a realistic book with him in it", "reach out via DM"), `pottytraining-1ume6jc` (parenting coach selling a toolkit with "parent scripts"; commenters called it an ad), `toddlers-1vg7g81` (Apolosign wall calendar; reads like placement, not tagged in themes beyond context).
