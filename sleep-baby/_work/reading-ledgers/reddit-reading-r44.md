# Reddit reading ledger — R44 (wave 3, sleep-baby)

Reader R44 · id prefix `sb44` · voice file `voice/reddit-r44.jsonl` · brief `../_shared/_tools/prompt-sleep-baby-reader-w3.txt` + `../_shared/_tools/brief-reading.md` · date 2026-10-25.

## Counts

| step | count |
|---|---|
| Chunks assigned | 12 (`read-w3-keep_otherside-005` … `-013`, `read-w3-keep_core-001` … `-003`, from `_raw/reddit/read-w3/chunks.jsonl`) |
| Units in those chunks | 163 (14/13/6/16/10/16/18/12/5 other-side; 12/18/23 core). Other-side posts dated 2026-05-01 → 2026-06-24; core posts 2026-04-01 → 2026-04-02; OP replies to 2026-10-14 |
| Units read in full | 163 |
| Units excluded entirely | 16 (10 for content, 6 duplicate cross-posts) |
| Units quoted | 147 |
| Quotes written | 400 (ids sb44-0001 … sb44-0400, unique) |
| Restricted quotes | 7 (listed in `synthesis/reader-notes-r44.md`) |
| possible_promo quotes | 0 (no seeded posts found in these chunks) |
| verify_quotes.py | 400 quotes, 0 failed |

Chunk-to-unit list: `scratchpad/R44/units.txt`. Short-form quote sources: `scratchpad/R44/q01–q12.jsonl`, built by `scratchpad/R44/build.py` (finds each quote's comment id from the unit text).

| chunk | units | quoted |
|---|---|---|
| read-w3-keep_otherside-005 | 14 | 14 |
| read-w3-keep_otherside-006 | 13 | 11 |
| read-w3-keep_otherside-007 | 6 | 6 |
| read-w3-keep_otherside-008 | 16 | 15 |
| read-w3-keep_otherside-009 | 10 | 9 |
| read-w3-keep_otherside-010 | 16 | 15 |
| read-w3-keep_otherside-011 | 18 | 16 |
| read-w3-keep_otherside-012 | 12 | 12 |
| read-w3-keep_otherside-013 | 5 | 5 |
| read-w3-keep_core-001 | 12 | 9 |
| read-w3-keep_core-002 | 18 | 16 |
| read-w3-keep_core-003 | 23 | 19 |

## Units excluded entirely (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/Parenting-1taptjw.txt` | physical force and verbal harshness toward the baby by the caregiver |
| `../_shared/_raw/reddit-2026/units/Mommit-1tduosi.txt` | duplicate cross-post of sleeptrain-1tdu6p1 (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tl1tg2.txt` | verbal harshness toward a toddler at bedtime is the subject of the post |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tu5b15.txt` | bedsharing arrangement is the subject of the post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twx0ig.txt` | duplicate cross-post of NewParents-1twvcne (quoted there) |
| `../_shared/_raw/reddit-2026/units/NewParents-1u13707.txt` | the ask is about bed rails for bedsharing |
| `../_shared/_raw/reddit-2026/units/NewParents-1u1l1xo.txt` | duplicate cross-post of AttachmentParenting-1u1l8ys (quoted there) |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1s97vni.txt` | bedsharing is the setting of the whole post |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1s98con.txt` | bedsharing transition plus a child's seizure history throughout |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1s99q1h.txt` | sleepwear and blanket safety is the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1s9c05u.txt` | duplicate cross-post of NewParents-1s9aev1 (quoted there) |
| `../_shared/_raw/reddit-2026/units/toddlers-1s9ilpm.txt` | verbal harshness toward a toddler is the subject of the post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1s9ripu.txt` | the ask is about bedsharing after early-morning feeds |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9wie9.txt` | duplicate cross-post of Parenting-1s9wd2o (quoted there) |
| `../_shared/_raw/reddit-2026/units/NewParents-1sa46f1.txt` | safe-sleep product limits and SIDS risk are the whole post |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sa4s10.txt` | duplicate cross-post of Mommit-1sa4l6y (quoted there) |

## Units read, passages left out (neutral reasons)

| unit | left out |
|---|---|
| `../_shared/_raw/reddit-2026/units/workingmoms-1t703ue.txt` | child just turned 3 (kept as 36 months); left out the child's aggression at daycare |
| `../_shared/_raw/reddit-2026/units/1t0w40b.txt` | left out: rage/self-regulation and therapy/condition lines; bedsharing detail |
| `../_shared/_raw/reddit-2026/units/1t76sip.txt` | left out: reflux medication, CMPA, headspace lines |
| `../_shared/_raw/reddit-2026/units/1t4atni.txt` | left out: mental-health line, weight/body line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1t7m93p.txt` | left out: bedsharing, pregnancy history, infant medical illness and medication, weight loss |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tady5m.txt` | left out: PPD-risk / mental-health lines |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tdu6p1.txt` | left out: method list naming cosleeping |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tep0ja.txt` | left out: diagnosed mood disorder, medication, panic and breakdown wording, harm-avoidance wording |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1teqkwl.txt` | left out: cosleeping arrangement and an unsafe-sleep-place line |
| `../_shared/_raw/reddit-2026/units/NewParents-1tfkbq5.txt` | left out: anxiety line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tlk3ph.txt` | left out: panic-attack and insomnia lines |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tkocih.txt`, `../_shared/_raw/reddit-2026/units/AttachmentParenting-1tmnw9s.txt`, `../_shared/_raw/reddit-2026/units/NewParents-1tp92hv.txt` | left out: anxiety lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1tqrzh3.txt` | left out: iron supplement, eczema, cosleeping/smothering fear lines |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tr5pcj.txt` | left out: cosleeping and milk-allergy lines |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tsmz4e.txt` | left out: partner yelling at the baby, PPD line, illness detail |
| `../_shared/_raw/reddit-2026/units/toddlers-1tvf3r2.txt` | left out: bereavement, depressive-episode and crying-while-typing lines |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1tvto1m.txt` | left out: "not so good place" line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1twemlp.txt` | left out: cosleeping and rolling-onto-stomach detail |
| `../_shared/_raw/reddit-2026/units/NewParents-1twpo2d.txt` | left out: cosleeping line |
| `../_shared/_raw/reddit-2026/units/toddlers-1txlxmw.txt` | left out: illness, antibiotics, separation-anxiety advice |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1tywe5c.txt` | left out: driving-safety line, cosleeping/bedsharing comments, autism and CMPA lines, mental-health lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1txfpn7.txt` | left out: child's panic-style breathing; mother's meltdown line kept out |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1u1l8ys.txt` | left out: postpartum-anxiety line |
| `../_shared/_raw/reddit-2026/units/NewParents-1u2g6o6.txt` | left out: daycare settling in a bouncy chair |
| `../_shared/_raw/reddit-2026/units/Mommit-1u4xoje.txt` | left out: line naming the baby |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1u5e3xk.txt` | left out: "dark part of my head" line |
| `../_shared/_raw/reddit-2026/units/toddlers-1u786ja.txt` | left out: child's early trauma, family court, terminal illness and hospital lines |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1u7mhi9.txt` | left out: birth complications, PPD, mastitis, sleeping-pillow product, NICU |
| `../_shared/_raw/reddit-2026/units/NewParents-1ud3mla.txt` | left out: medication line and partner-harm reassurance line |
| `../_shared/_raw/reddit-2026/units/NewParents-1s94inq.txt` | left out: "thoughts are starting to get dark" and PPD line |
| `../_shared/_raw/reddit-2026/units/NewParents-1s957ez.txt` | left out: cosleeping and NICU lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9a8zo.txt` | left out: side-sleeping, heating pad, coughing details |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9aev1.txt` | left out: prematurity, IUGR, reflux medication |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1s9ax2g.txt` | left out: anxiety and cosleeping lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9hbzp.txt` | left out: "mental breakdown" title wording, cosleeping, separation-anxiety line |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9ip0v.txt` | left out: crying to near-fainting/coughing detail, night driving, bed-taking |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1s9klf4.txt` | left out: infant medication, bedsharing and "not safe" lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9knzg.txt` | left out: anger-at-baby line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1s9n1be.txt` | left out: cosleeping line |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1s9uohh.txt` | left out: tummy-sleeping and sleep-suit details |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9vznv.txt` | left out: cosleeper-bassinet line |
| `../_shared/_raw/reddit-2026/units/NewParents-1s9wuej.txt`, `../_shared/_raw/reddit-2026/units/sleeptrain-1s9ymx3.txt` | left out: infant medication / reflux lines |
| `../_shared/_raw/reddit-2026/units/sleeptrain-1sa4jsi.txt` | left out: cosleeping and bed-sharing lines |
| `../_shared/_raw/reddit-2026/units/NewParents-1sa4xdq.txt` | left out: cosleeping, bed-sharing, hyperventilating/choking detail |
| `../_shared/_raw/reddit-2026/units/beyondthebump-1sa80k5.txt` | left out: diagnosed condition, PPD/PPA, fainting-while-holding lines |

Age edge: `workingmoms-1t703ue`, `toddlers-1trsiv6` and `toddlers-1u786ja` describe children who have just turned 3; kept as 36 months, consistent with the niche README. No unit was dropped for age.

## Unread

None. Every unit in the 12 chunks was read to its last OP reply.
