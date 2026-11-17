# Reddit reading ledger — R58 (wave 3, keep_core 125–134)

Reader R58, id prefix `sb58`, voice file `voice/reddit-r58.jsonl`. Brief: `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` → `../_shared/_tools/brief-reading.md`.

| step | count |
|---|---|
| chunks assigned | 10 (`read-w3-keep_core-125` … `read-w3-keep_core-134`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| units in those chunks | 151 |
| units read in full (post + every OP reply in the unit) | 151 |
| units excluded entirely (neutral reason below) | 9 |
| cross-posts read in full, not quoted (the twin was quoted) | 5 |
| read in full, nothing quotable | 1 |
| units quoted | 136 |
| quotes written | 464 (`sb58-0001` … `sb58-0464`, ids unique) |
| restricted quotes | 13 (listed in `synthesis/reader-notes-r58.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-r58.jsonl` → 464 quotes, 0 failed |

Posts are dated 27–31 May 2026; OP replies run to 19 October 2026. Ids are in reading order except `sb58-0462` … `-0464` (unit `sleeptrain-1tpt27t`, chunk 127), added after a coverage check showed the unit had been read but not yet recorded.

## Units excluded entirely

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1towuwn.txt` | safe-sleep detail (rolling to tummy, bedsharing question); no other sleep problem |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tq4fz0.txt` | medical condition (skin) and bedsharing make up the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tqbd8q.txt` | infant-death fear and safe-sleep worry about a crib cover product |
| `../_shared/_raw/reddit-2026/units/toddlers-1tqmtn5.txt` | physical restraint of a child at bedtime is the core of the post |
| `../_shared/_raw/reddit-2026/units/beyondthebumpUK-1trcwmv.txt` | safe-sleep detail (bedsharing toddler standing and rolling near the bed edge) runs through the post |
| `../_shared/_raw/reddit-2026/units/NewParents-1trta2e.txt` | sleepwear near rolling (swaddle drop at signs of rolling) and tummy-sleep line |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tsbfc8.txt` | safe-sleep incident (parent nodding off holding a newborn in a recliner) and mental-health detail run through the thread |
| `../_shared/_raw/reddit-2026/units/NewParents-1tsl5x9.txt` | safe-sleep incident (parents drifting off with the baby on their chests) and medication detail |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tsl6nl.txt` | cross-post of NewParents-1tsl5x9; same safe-sleep and medication detail |

## Read in full, not quoted

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tphn4k.txt` | cross-post of beyondthebumpUK-1tpfwq8 (same text, same day); twin quoted |
| `../_shared/_raw/reddit-2026/units/Parenting-1trcklj.txt` | cross-post of sleeptrain-1tqxwtj (same text); twin quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1trddvb.txt` | cross-post of sleeptrain-1tqxwtj (same text); twin quoted |
| `../_shared/_raw/reddit-2026/units/Parenting-1trohxt.txt` | cross-post of NewParents-1troixj (same text); twin quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tsjl7g.txt` | cross-post of sleeptrain-1tsj9hn (same text); twin quoted |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tqq20t.txt` | read in full; the post turns on medication dosing, nothing quotable without it |

## Passages left out of quoted units (neutral reasons)

| unit | left out |
|---|---|
| `../_shared/_raw/reddit-2026/units/NewParents-1tp9j94.txt` | swaddle-rolling and bedsharing details left out; reflux and anxiety lines not quoted |
| `../_shared/_raw/reddit-2026/units/NewParents-1tpoxji.txt` | supplements, prescriptions, hormone tests and co-sleeping passages left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tpt4gm.txt` | melatonin and cosleeping passages left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1tpv213.txt` | night medication passage left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tpwml3.txt` | gripe water, dairy-cutting and supply passages left out |
| `../_shared/_raw/reddit-2026/units/Parenting-1tq1evi.txt` | a named pain condition, a relative's illness, a low-mood line and bed-holding passages left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1tq1nku.txt` | illness detail, co-sleeping and a fall from the cot (hospital visit) left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tq3w1s.txt` | sleepwear detail left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tq41mg.txt` | medication passage left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tq493b.txt` | bedsharing passages left out |
| `../_shared/_raw/reddit-2026/units/daddit-1tq6i6n.txt` | a low-mood line and medical checks left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tq6kk4.txt` | gripe water and medication passage left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tq84eu.txt` | cosleeping passage left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tq9yoc.txt` | skin-condition and co-sleep background left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tqb0ts.txt` | side-car cot detail left out |
| `../_shared/_raw/reddit-2026/units/Parenting-1tqbnqd.txt` | tongue-tie and gas-remedy passage left out |
| `../_shared/_raw/reddit-2026/units/Parenting-1tqdweh.txt` | OP replies about physical punishment (rejected by OP) left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tqfuqs.txt` | breathing detail and co-sleep passages left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tqkw91.txt` | mental-health, cosleeping and specialist-visit lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tqll3u.txt` | bedsharing line left out |
| `../_shared/_raw/reddit-2026/units/Parenting-1tqpf8v.txt` | swaddle-at-9-months, bed and sleep-sack safety lines left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1tr209t.txt` | mental-health history and floor-bed co-sleeping lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tr5q7o.txt` | illness detail and a mental-health line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tr66zd.txt` | cosleeping line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tr9mn2.txt` | the mother's health line and a tight-blanket detail left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tra6mm.txt` | reflux guess and side-lying sleep line left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1trjysf.txt` | cosleeping line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1trk3ur.txt` | ear-infection and surgery line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1troixj.txt` | bedsharing after the move left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1trppav.txt` | illness and a house-damage incident left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1trqljo.txt` | ear infection, antibiotics and bed-transfer lines left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tr66ih.txt` | baby's weight percentile left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1trvved.txt` | ear-infection line left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1trw38h.txt` | cosleeping and crisis-like wording left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1trx0vw.txt` | medication and bed lines left out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tryo0t.txt` | supplement and test result left out |
| `../_shared/_raw/reddit-2026/units/Mommit-1trzyhv.txt` | named postpartum condition left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ts025t.txt` | gas-drop medication and bed lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ts58m3.txt` | fear of rolling on the baby while cosleeping, self-slapping and anger lines left out |
| `../_shared/_raw/reddit-2026/units/toddlers-1ts8p50.txt` | cosleeping attempts left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1ts9qjh.txt` | reflux, medication and maternal diet lines left out |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tsaivy.txt` | blood test, bed-transfer and physical-symptom lines left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tsf3h7.txt` | co-sleeping line left out |
| `../_shared/_raw/reddit-2026/units/NewParents-1tsivh5.txt` | co-sleeping and medical-appointment lines left out |

## Same author, separate posts (both quoted)

- `sleeptrain-1tp4ids` and `sleeptrain-1tq1pzz` (the second links the first): `sb58-0045` … `-0048`, `sb58-0187` … `-0189`.
- `sleeptrain-1tqpagt` and `sleeptrain-1tskkbj` (same baby, schedule and history): `sb58-0291` … `-0293`, `sb58-0460` … `-0461`.
- `sleeptrain-1tqxwtj` was posted three times (also `Parenting-1trcklj`, `NewParents-1trddvb`); only the first is quoted.

## How to continue

Nothing in this assignment is unread. Never append to `voice/reddit-r58.jsonl` from another session.
