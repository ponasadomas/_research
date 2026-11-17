# Reddit reading ledger — TR21 (wave 3, keep_core chunks 014–022)

Reader TR21, id prefix `tb21`, voice file `voice/reddit-tr21.jsonl`. Brief: `../_shared/_tools/prompt-toddler-reader-w3.txt` and `../_shared/_tools/brief-reading.md`. Posts dated 2026-04-14 to 2026-04-26 (original poster's replies run to 2026-09-11).

| step | count |
|---|---|
| chunks assigned | 9 (`read-w3-keep_core-014` … `-022`) |
| units in those chunks | 155 |
| units read in full | 155 |
| units excluded whole | 25 (5 duplicate cross-posts, 20 under a line not to cross) |
| units read, nothing quotable | 1 (`Parenting-1sncu12.txt`, peer teasing at daycare, little niche content) |
| units quoted | 129 |
| quotes written | 356 (ids tb21-0001 … tb21-0384; 28 ids withdrawn when seven units were excluded on review, never reused) |
| quotes restricted (theme `restricted`) | 4 |
| possible_promo (not counted) | 1 (tb21-0023) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-tr21.jsonl` → 356 quotes, 0 failed |

Unread: none. Every unit in the nine chunks was read in full, including all of the original poster's replies.

Withdrawn ids (not in the voice file): tb21-0024 to tb21-0027, tb21-0084, tb21-0085, tb21-0097 to tb21-0107, tb21-0127, tb21-0128, tb21-0186 to tb21-0188, tb21-0218, tb21-0219, tb21-0251 to tb21-0254.

## Excluded units (neutral reasons)

- `toddlers-1sn2696.txt` — parent describes physical punishment of the child; excluded whole
- `toddlers-1snbhui.txt` — same post text as NewParents-1snb53s (quoted there)
- `toddlers-1sngh7m.txt` — same post text as Parenting-1snhzhx (quoted there)
- `Parenting-1so5d6v.txt` — same post text as toddlers-1snhjud (quoted there)
- `pottytraining-1sojuk4.txt` — child body and medical detail; excluded whole
- `toddlers-1soopky.txt` — bathing-centred post framed around a diagnosis question, parent holds child; excluded whole
- `AttachmentParenting-1sosxay.txt` — parent's medical detail and verbal harshness toward the child at the centre; excluded whole
- `toddlers-1sq2c9i.txt` — parent describes physical force and punishment toward the child; excluded whole
- `toddlers-1sq3huk.txt` — parent describes harsh scolding and forced sitting; excluded whole
- `NewParents-1sqic71.txt` — parent describes yelling at the toddler as the centre of the post (also reads as polished engagement copy); excluded whole
- `Mommit-1sr9afi.txt` — parent's yelling at the child and own childhood at the centre (also reads as polished engagement copy); excluded whole
- `toddlers-1srml5t.txt` — parents describe yelling at the child daily as the centre of the post; excluded whole
- `Parenting-1srrsh8.txt` — same post text as Mommit-1srw01k (quoted there); its one reply read, not quoted
- `Parenting-1srrxjw.txt` — same post text as toddlers-1srrwks (quoted there)
- `toddlers-1sszkx2.txt` — parent describes yelling at a 17-month-old as the centre of the post; excluded whole
- `Parenting-1stocy4.txt` — parent describes striking the child; excluded whole
- `Parenting-1suvgb2.txt` — child body/hygiene incident at the centre; excluded whole
- `NewParents-1svn06c.txt` — child head-banging (self-injury) described; excluded whole
- `toddlers-1smpweu.txt` — parent describes striking the child's hand; excluded whole (quotes tb21-0024 to tb21-0027 withdrawn)
- `Parenting-1soeqoy.txt` — parent describes physical punishment and yelling; excluded whole (tb21-0084, tb21-0085 withdrawn)
- `toddlers-1solau1.txt` — parent describes yelling at the child in replies; excluded whole (tb21-0097 to tb21-0107 withdrawn)
- `pottytraining-1sp513a.txt` — parent describes forcing the child onto the potty; excluded whole (tb21-0127, tb21-0128 withdrawn)
- `toddlers-1sraugr.txt` — parent describes slapping the child; excluded whole (tb21-0218, tb21-0219 withdrawn)
- `pottytraining-1sqwywk.txt` — partner keeps the child in the bathroom until he goes; excluded whole (tb21-0186 to tb21-0188 withdrawn)
- `toddlers-1ssaiw1.txt` — parent describes physical restraint during routines; excluded whole (tb21-0251 to tb21-0254 withdrawn)

## Units quoted only in part (passages left out, neutral reasons)

- `toddlers-1slplzl.txt` — early-intervention detail not quoted
- `toddlers-1sn6884.txt` — parent's medication and therapy passages not quoted
- `Parenting-1snhzhx.txt` — infection check and pain passages not quoted
- `NewParents-1snxfis.txt` — developmental worry and pregnancy passages not quoted
- `toddlers-1so8rsg.txt` — parent's postpartum diagnosis not quoted
- `Mommit-1soif5o.txt` — parent's own family history not quoted
- `Parenting-1souh48.txt` — parent's fear of striking the child not quoted
- `AttachmentParenting-1sox6qq.txt` — parent's own childhood not quoted
- `toddlers-1sp3qmv.txt` — other parent snapping not quoted
- `Parenting-1sp95yf.txt` — developmental and specialist passages not quoted
- `toddlers-1spahuy.txt` — passage where parent carries child to the toilet not quoted
- `toddlers-1spwazj.txt` — motor-delay detail not quoted
- `toddlers-1spwuij.txt` — diagnosis-testing passages not quoted; a relative's childhood punishment not quoted; quotes from this diagnosis-question unit restricted where they touch medical/mental-health words
- `pottytraining-1spy08x.txt` — infection worry not quoted
- `Mommit-1sq5lqx.txt` — parent's mental-health line not quoted
- `Parenting-1sq62pf.txt` — speech-therapy passage not quoted
- `toddlers-1sqjmse.txt` — child separation-worry label not quoted
- `toddlers-1sqso1n.txt` — therapy and milestone passages not quoted
- `toddlers-1sqwk6x.txt` — constipation and panic wording not quoted
- `toddlers-1sqx5a0.txt` — medical treatment and child body (smearing) passages not quoted
- `Mommit-1sqyv0e.txt` — development and medical passages not quoted; one worry quote restricted
- `Mommit-1sr7ot5.txt` — parent's postpartum diagnosis not quoted
- `Mommit-1sr9tqr.txt` — parent yelling passage and dietitian detail not quoted
- `toddlers-1sraisk.txt` — parent's medical detail and own upbringing not quoted
- `toddlers-1srmwz8.txt` — doctor's advice not quoted
- `Mommit-1srr2rt.txt` — parent's raised voice and own childhood not quoted
- `Mommit-1srw01k.txt` — school psychologist reply not quoted
- `toddlers-1srrwks.txt` — speech-therapy line not quoted
- `Parenting-1ss0ydu.txt` — breastfeeding body detail not quoted
- `pottytraining-1ssdhwe.txt` — illness detail not quoted
- `Mommit-1sso2c9.txt` — medical tests passages not quoted
- `Mommit-1ssthtt.txt` — parent's postpartum diagnosis and medication not quoted
- `toddlers-1ssu328.txt` — diaper-rash and immunisation detail not quoted
- `toddlers-1st46wx.txt` — doctor, supplement and weight passages not quoted
- `AttachmentParenting-1st7yym.txt` — parent's mental-health line and medication not quoted
- `NewParents-1st9qab.txt` — parent's own childhood and development worry not quoted
- `Mommit-1stba2k.txt` — parent's mental-health line not quoted
- `pottytraining-1stlbg7.txt` — pain and bowel detail not quoted
- `Parenting-1stm14a.txt` — parent's urge to strike not quoted
- `toddlers-1stm63q.txt` — therapy question not quoted
- `toddlers-1stoscd.txt` — contraception line not quoted
- `toddlers-1stx8ac.txt` — one desperation line quoted (restricted, medical); diet and medication details not quoted
- `Parenting-1stxhne.txt` — parent's raised-voice line not quoted
- `Parenting-1su1l1g.txt` — breastfeeding and injury details not quoted
- `toddlers-1su64pz.txt` — medication and doctor detail not quoted
- `Parenting-1suktb2.txt` — therapist observation not quoted
- `daddit-1sup697.txt` — parent's own diagnosis and bereavement not quoted
- `Parenting-1sveao5.txt` — parent's own upbringing not quoted
- `toddlers-1svk7oj.txt` — medication detail not quoted
- `toddlers-1svwwgv.txt` — nappy-change body detail not quoted
- `workingmoms-1sw1dvo.txt` — fear for child's mental health not quoted

## Units flagged (diagnosis or development question in the unit; only clean words quoted; do not build hooks from them)

- `Mommit-1sswqax.txt` — unit mentions a developmental diagnosis; only home-vs-school and public-judgement words quoted; do not build hooks from it
- `Mommit-1st5q9c.txt` — unit centres on a diagnosed delay; only one price-signal line quoted; do not build hooks from it
- `Mommit-1sqyv0e.txt` — development-question unit; tb21-0194 words are clean but do not build hooks from it
- `NewParents-1snxfis.txt` — development worry unit; quoted words clean (tb21-0070, tb21-0071)
- `toddlers-1spwuij.txt` — diagnosis-question unit; quotes tb21-0143, tb21-0144, tb21-0145, tb21-0146 are not restricted (clean words), tb21-0147 is restricted; do not build hooks from it
- `NewParents-1stoi7a.txt` — a specialist's diagnosis remark, parent's health and upbringing not quoted; other remarks quoted
- `sahm-1sul9w4.txt` — replies name siblings' diagnoses and a therapist's punitive suggestion; neither quoted; clean-word quotes only
- `toddlers-1sw113s.txt` — diagnosis-question unit (sensory); doctor quote restricted, one strain quote clean; do not build hooks from it

## Possible promotion

- `toddlers-1smneoo.txt` — tablet post whose author says they partner with the brand; one quote, tb21-0023, tagged `possible_promo`; never count it.

## How to continue

Nothing left to read in these chunks. The batch inputs in `scratchpad/TR21/b*.json` still contain the withdrawn quotes, so never re-run them (they append). The per-unit decision log is `scratchpad/TR21/ledger.txt`.
