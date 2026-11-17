# Reddit full reads — TR14 (wave 2, keep_core, posts 2026-07-17 → 07-27)

Brief: `../_shared/_tools/brief-reading.md`. Reader TR14, id prefix `tb14`, voice file `voice/reddit-tr14.jsonl`, scratch `scratchpad/TR14/`. Read 2026-10-25 (resumed once after a usage-limit stop; voice file checked on disk, no id reused).

## Chunks assigned (from `_raw/reddit/read-w2/assignments.txt`)

| chunk | units |
|---|---|
| read-w2-keep_core-024 | 12 |
| read-w2-keep_core-025 | 18 |
| read-w2-keep_core-026 | 16 |
| read-w2-keep_core-027 | 16 |
| read-w2-keep_core-028 | 19 |
| read-w2-keep_core-029 | 16 |
| read-w2-keep_core-030 | 10 |
| read-w2-keep_core-031 | 17 |
| read-w2-keep_core-032 | 14 |
| **total** | **138** |

## Counts

- Units in chunks: 138
- Units read in full: 138 (none unfinished)
- Units excluded (safety or medical; not quoted): 7
- Units read, no quote (thin or off-niche): 3
- Units read, reposts of a quoted unit (no quotes): 2
- Units quoted: 126
- Quotes written: 339 (tb14-0001 … tb14-0339), ids unique
- Restricted quotes: 5 (listed in `synthesis/reader-notes-tr14.md`, "Restricted ids")
- Verify: `python3 -I _tools/verify_quotes.py voice/reddit-tr14.jsonl` → 339 quotes, 0 failed

## Units excluded (neutral reasons)

| unit | reason |
|---|---|
| `../_shared/_raw/reddit-2026/units/toddlers-1v2hxjj.txt` | centred on post-surgery medical recovery and a child biting himself (medical treatment, self-injury) |
| `../_shared/_raw/reddit-2026/units/toddlers-1v37wtj.txt` | parent describes physical discipline of the child |
| `../_shared/_raw/reddit-2026/units/toddlers-1v3iwea.txt` | centred on the parent's own depression and acute distress (mental-health crisis) |
| `../_shared/_raw/reddit-2026/units/pottytraining-1v50bac.txt` | physical punishment of a child considered |
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1v6elva.txt` | centred on a child's hospital treatment (IV, being held down) and therapy plans (medical treatment) |
| `../_shared/_raw/reddit-2026/units/daddit-1v7kcsj.txt` | physical force toward a child; diagnosis-centred replies |
| `../_shared/_raw/reddit-2026/units/toddlers-1v7nr7g.txt` | parent says spanking was tried; behavioural therapy for the child |

## Units read, not quoted

| unit | why |
|---|---|
| `../_shared/_raw/reddit-2026/units/AttachmentParenting-1uzvgj5.txt` | repost of Mommit-1uzg75y; no quotes |
| `../_shared/_raw/reddit-2026/units/toddlers-1uzvlsq.txt` | night sippy cups, weaning-adjacent |
| `../_shared/_raw/reddit-2026/units/toddlers-1v3tvh8.txt` | centred on sudden fears and a planned pediatrician visit; medical worry |
| `../_shared/_raw/reddit-2026/units/Parenting-1v3zkib.txt` | bath fear after a move; thin |
| `../_shared/_raw/reddit-2026/units/toddlers-1v5i3ks.txt` | repost of Mommit-1v5hxgm; no quotes |

## Every unit (chunk, status, quote ids, what was left out)

| chunk | unit | status | ids | note |
|---|---|---|---|---|
| 024 | `Mommit-1uz889p` | quoted | tb14-0001 … tb14-0003 (3) | tb14-0001..0003; yell line not quoted |
| 024 | `Parenting-1uz9ggm` | quoted | tb14-0004 … tb14-0009 (6) |  |
| 024 | `daddit-1uzcyag` | quoted | tb14-0010 … tb14-0013 (4) |  |
| 024 | `Mommit-1uzg75y` | quoted | tb14-0014 (1) |  |
| 024 | `toddlers-1uzjnwh` | quoted | tb14-0015 … tb14-0016 (2) |  |
| 024 | `toddlers-1uzmvxu` | quoted | tb14-0017 … tb14-0019 (3) | medical-centred thread: medication, dose, cleanout passages not quoted; quotes tb14-0017..0019 are non-medical (unit flagged) |
| 024 | `toddlers-1uzu6ar` | quoted | tb14-0020 … tb14-0024 (5) | neurodivergence/eval reply not quoted |
| 024 | `Mommit-1uzvbyr` | quoted | tb14-0025 (1) | child fear response, parent health/therapy, own-parents history not quoted; tb14-0025 clean (unit flagged) |
| 024 | `AttachmentParenting-1uzvgj5` | read-repost | — (0) | repost of Mommit-1uzg75y; no quotes |
| 024 | `toddlers-1uzvlsq` | read-noquote | — (0) | night sippy cups, weaning-adjacent |
| 024 | `pottytraining-1uzvlx7` | quoted | tb14-0026 … tb14-0027 (2) |  |
| 024 | `NewParents-1uzycp1` | quoted | tb14-0028 … tb14-0029 (2) |  |
| 025 | `pottytraining-1v025nr` | quoted | tb14-0030 … tb14-0032 (3) |  |
| 025 | `pottytraining-1v03oi8` | quoted | tb14-0033 … tb14-0034 (2) | bladder-infection worry not quoted |
| 025 | `toddlers-1v04k5n` | quoted | tb14-0035 … tb14-0036 (2) |  |
| 025 | `pottytraining-1v07b8w` | quoted | tb14-0037 … tb14-0038 (2) |  |
| 025 | `daddit-1v07d3y` | quoted | tb14-0039 … tb14-0040 (2) | author's own ADHD diagnosis and therapy not quoted; quotes clean (unit flagged) |
| 025 | `pottytraining-1v091ss` | quoted | tb14-0041 … tb14-0045 (5) |  |
| 025 | `toddlers-1v09arp` | quoted | tb14-0046 … tb14-0047 (2) |  |
| 025 | `Parenting-1v0d6i7` | quoted | tb14-0048 … tb14-0049 (2) |  |
| 025 | `toddlers-1v0ebso` | quoted | tb14-0050 … tb14-0052 (3) | "force her to get dressed" line not quoted |
| 025 | `Mommit-1v0ezhq` | quoted | tb14-0053 … tb14-0056 (4) | parent's childhood abuse, ADHD-inheritance question and chronic illness not quoted; yelling line not quoted (unit flagged) |
| 025 | `pottytraining-1v0lh58` | quoted | tb14-0057 … tb14-0058 (2) | vomiting detail not quoted; tb14-0057 restricted (pediatrician, psychologist) |
| 025 | `workingmoms-1v0rm1v` | quoted | tb14-0059 … tb14-0061 (3) | antidepressant medication passages and yelling line not quoted (unit flagged) |
| 025 | `Parenting-1v0syl5` | quoted | tb14-0062 … tb14-0064 (3) | illness history not quoted |
| 025 | `toddlers-1v0tx11` | quoted | tb14-0065 (1) |  |
| 025 | `daddit-1v0tz56` | quoted | tb14-0066 … tb14-0067 (2) |  |
| 025 | `daddit-1v0vklp` | quoted | tb14-0068 (1) |  |
| 025 | `NewParents-1v0w0bz` | quoted | tb14-0069 (1) |  |
| 025 | `toddlers-1v0w5rl` | quoted | tb14-0070 … tb14-0071 (2) | poop-play passage not quoted |
| 026 | `pottytraining-1v10rks` | quoted | tb14-0072 … tb14-0074 (3) |  |
| 026 | `toddlers-1v1191e` | quoted | tb14-0075 … tb14-0078 (4) | pediatrician reply not quoted |
| 026 | `toddlers-1v1anys` | quoted | tb14-0079 … tb14-0081 (3) |  |
| 026 | `Parenting-1v1fxvx` | quoted | tb14-0082 … tb14-0083 (2) |  |
| 026 | `pottytraining-1v1grwl` | quoted | tb14-0084 … tb14-0088 (5) | speech-delay evaluation and doctor replies not quoted; illness detail not quoted (unit flagged) |
| 026 | `toddlers-1v1mb4g` | quoted | tb14-0089 … tb14-0092 (4) | child undressing/peeing and car-seat passages not quoted |
| 026 | `pottytraining-1v1pxft` | quoted | tb14-0093 … tb14-0094 (2) |  |
| 026 | `AttachmentParenting-1v1rn54` | quoted | tb14-0095 … tb14-0100 (6) |  |
| 026 | `pottytraining-1v23bxb` | quoted | tb14-0101 (1) |  |
| 026 | `toddlers-1v24vbv` | quoted | tb14-0102 … tb14-0106 (5) |  |
| 026 | `NewParents-1v252d5` | quoted | tb14-0107 (1) |  |
| 026 | `pottytraining-1v29m60` | quoted | tb14-0108 … tb14-0109 (2) |  |
| 026 | `pottytraining-1v2bmqg` | quoted | tb14-0110 … tb14-0111 (2) | laxative mention not quoted |
| 026 | `toddlers-1v2bq3i` | quoted | tb14-0112 … tb14-0113 (2) |  |
| 026 | `pottytraining-1v2fqsn` | quoted | tb14-0114 … tb14-0117 (4) |  |
| 026 | `Mommit-1v2fzwu` | quoted | tb14-0118 … tb14-0120 (3) |  |
| 027 | `toddlers-1v2hxjj` | excluded | — (0) | centred on post-surgery medical recovery and a child biting himself (medical treatment, self-injury) |
| 027 | `daddit-1v2iy67` | quoted | tb14-0121 … tb14-0123 (3) | polished, essay-like voice; no product named, not tagged promo |
| 027 | `toddlers-1v2kus0` | quoted | tb14-0124 … tb14-0126 (3) |  |
| 027 | `NewParents-1v2o8or` | quoted | tb14-0127 … tb14-0129 (3) | hospitalisation and vomiting detail not quoted |
| 027 | `toddlers-1v2qd2c` | quoted | tb14-0130 … tb14-0132 (3) | infant digestive/medical history not quoted |
| 027 | `toddlers-1v2r685` | quoted | tb14-0133 … tb14-0135 (3) | speech delay and therapy line not quoted (unit flagged) |
| 027 | `toddlers-1v2rwcq` | quoted | tb14-0136 … tb14-0137 (2) | yelling and holding-the-door passages not quoted |
| 027 | `toddlers-1v2se28` | quoted | tb14-0138 … tb14-0140 (3) | parents' own trauma line not quoted |
| 027 | `toddlers-1v2t1uf` | quoted | tb14-0141 … tb14-0144 (4) |  |
| 027 | `toddlers-1v2t8ht` | quoted | tb14-0145 … tb14-0147 (3) | pediatrician lines not quoted |
| 027 | `GentleParenting-1v2um1k` | quoted | tb14-0148 … tb14-0152 (5) | parents' ADHD line and door-holding passage not quoted (unit flagged) |
| 027 | `pottytraining-1v2uvvi` | quoted | tb14-0153 … tb14-0156 (4) | constipation and diet passage not quoted |
| 027 | `Parenting-1v2w2q9` | quoted | tb14-0157 … tb14-0161 (5) | OT evaluation, psychologist, "underlying issues" and physical-hold description not quoted (unit flagged) |
| 027 | `NewParents-1v31yec` | quoted | tb14-0162 … tb14-0164 (3) |  |
| 027 | `Mommit-1v33t4q` | quoted | tb14-0165 … tb14-0166 (2) |  |
| 027 | `pottytraining-1v34m3v` | quoted | tb14-0167 … tb14-0168 (2) |  |
| 028 | `pottytraining-1v35epu` | quoted | tb14-0169 … tb14-0171 (3) |  |
| 028 | `toddlers-1v37wtj` | excluded | — (0) | parent describes physical discipline of the child |
| 028 | `pottytraining-1v39rlh` | quoted | tb14-0172 … tb14-0177 (6) |  |
| 028 | `AttachmentParenting-1v3esv8` | quoted | tb14-0178 (1) |  |
| 028 | `toddlers-1v3iwea` | excluded | — (0) | centred on the parent's own depression and acute distress (mental-health crisis) |
| 028 | `pottytraining-1v3m790` | quoted | tb14-0179 … tb14-0180 (2) |  |
| 028 | `toddlers-1v3tvh8` | read-noquote | — (0) | centred on sudden fears and a planned pediatrician visit; medical worry |
| 028 | `toddlers-1v3w255` | quoted | tb14-0181 … tb14-0185 (5) | autism mention and parent's/father's own diagnosis reply not quoted (unit flagged) |
| 028 | `toddlers-1v3wtyo` | quoted | tb14-0186 … tb14-0187 (2) |  |
| 028 | `pottytraining-1v3ziou` | quoted | tb14-0188 (1) | child body passage and parent's injury reply not quoted |
| 028 | `Parenting-1v3zkib` | read-noquote | — (0) | bath fear after a move; thin |
| 028 | `Parenting-1v3zv8w` | quoted | tb14-0189 … tb14-0190 (2) |  |
| 028 | `daddit-1v47fo0` | quoted | tb14-0191 … tb14-0193 (3) |  |
| 028 | `toddlers-1v4f7f2` | quoted | tb14-0194 … tb14-0196 (3) | postnatal mental-health history, medication, sibling autism, "walking away" line not quoted (unit flagged) |
| 028 | `toddlers-1v4f80o` | quoted | tb14-0197 … tb14-0198 (2) |  |
| 028 | `daddit-1v4hgqe` | quoted | tb14-0199 (1) | essay-like, possible bot/seeded post; tagged possible_promo; doctor passage not quoted |
| 028 | `Parenting-1v4jm32` | quoted | tb14-0200 (1) |  |
| 028 | `pottytraining-1v4kh6k` | quoted | tb14-0201 … tb14-0202 (2) | pregnancy nausea passages not quoted |
| 028 | `pottytraining-1v3ispm` | quoted | tb14-0203 … tb14-0204 (2) |  |
| 029 | `daddit-1v4n0xh` | quoted | tb14-0205 … tb14-0206 (2) | "take it out on kids" and dragging lines not quoted |
| 029 | `toddlers-1v4quxm` | quoted | tb14-0207 … tb14-0212 (6) | child hitting herself, breastfeeding/weaning detail not quoted; spectrum line restricted (unit flagged) |
| 029 | `pottytraining-1v4t2v7` | quoted | tb14-0213 (1) |  |
| 029 | `toddlers-1v4y43j` | quoted | tb14-0214 … tb14-0215 (2) | OT / sensory finding not quoted (unit flagged) |
| 029 | `pottytraining-1v5056p` | quoted | tb14-0216 … tb14-0218 (3) |  |
| 029 | `pottytraining-1v50bac` | excluded | — (0) | physical punishment of a child considered |
| 029 | `pottytraining-1v51vws` | quoted | tb14-0219 … tb14-0221 (3) |  |
| 029 | `pottytraining-1v5349o` | quoted | tb14-0222 … tb14-0224 (3) |  |
| 029 | `Mommit-1v5bj5x` | quoted | tb14-0225 … tb14-0227 (3) | infant illness lines not quoted |
| 029 | `Mommit-1v5hxgm` | quoted | tb14-0228 … tb14-0229 (2) | baby's medical testing not quoted |
| 029 | `AttachmentParenting-1v5i3dg` | quoted | tb14-0230 … tb14-0232 (3) | pediatrician's socialisation concern not quoted except copay line (restricted) |
| 029 | `toddlers-1v5i3ks` | read-repost | — (0) | repost of Mommit-1v5hxgm; no quotes |
| 029 | `pottytraining-1v5k9v5` | quoted | tb14-0233 (1) |  |
| 029 | `Parenting-1v5ki09` | quoted | tb14-0234 … tb14-0239 (6) |  |
| 029 | `toddlers-1v5my9p` | quoted | tb14-0240 (1) | dentist line not quoted |
| 029 | `NewParents-1v5o4op` | quoted | tb14-0241 (1) |  |
| 030 | `pottytraining-1v5osq0` | quoted | tb14-0242 (1) |  |
| 030 | `Mommit-1v5qoze` | quoted | tb14-0243 … tb14-0246 (4) | replies about parent's own ADHD, medication and genetic testing not quoted (unit flagged) |
| 030 | `toddlers-1v5t7ur` | quoted | tb14-0247 … tb14-0250 (4) | child OT line and anger/profanity lines not quoted |
| 030 | `Parenting-1v5xjyu` | quoted | tb14-0251 … tb14-0254 (4) | parent's therapy/trauma and locking-door replies not quoted |
| 030 | `toddlers-1v663qm` | quoted | tb14-0255 (1) | parent's PMDD, depression and "snapping" not quoted (unit flagged) |
| 030 | `toddlers-1v698yz` | quoted | tb14-0256 … tb14-0261 (6) | autism/learning-difficulties exchange not quoted (unit flagged) |
| 030 | `Parenting-1v6at04` | quoted | tb14-0262 … tb14-0265 (4) | asks about OT/child psychologist; those words not quoted (unit flagged) |
| 030 | `toddlers-1v6au2r` | quoted | tb14-0266 … tb14-0267 (2) |  |
| 030 | `toddlers-1v6b13r` | quoted | tb14-0268 … tb14-0270 (3) |  |
| 030 | `daddit-1v6bd4t` | quoted | tb14-0271 … tb14-0272 (2) | "lose my temper" not quoted |
| 031 | `toddlers-1v6cewu` | quoted | tb14-0273 … tb14-0277 (5) | raised-voice line not quoted |
| 031 | `pottytraining-1v6dd7k` | quoted | tb14-0278 … tb14-0280 (3) |  |
| 031 | `toddlers-1v6ebnt` | quoted | tb14-0281 (1) |  |
| 031 | `Parenting-1v6ecoc` | quoted | tb14-0282 … tb14-0283 (2) | replies about others' abuse/slapping not quoted |
| 031 | `AttachmentParenting-1v6elva` | excluded | — (0) | centred on a child's hospital treatment (IV, being held down) and therapy plans (medical treatment) |
| 031 | `Parenting-1v6hmts` | quoted | tb14-0284 … tb14-0285 (2) | the father's yelling passage not quoted |
| 031 | `pottytraining-1v6m7kj` | quoted | tb14-0286 (1) | laxative/diet line not quoted |
| 031 | `toddlers-1v6mpkm` | quoted | tb14-0287 … tb14-0289 (3) |  |
| 031 | `Mommit-1v6o9lo` | quoted | tb14-0290 … tb14-0292 (3) | yelling line and pediatrician/urine-test lines not quoted |
| 031 | `toddlers-1v6sbfz` | quoted | tb14-0293 (1) |  |
| 031 | `Parenting-1v6uhiz` | quoted | tb14-0294 … tb14-0296 (3) | "stern" passage not quoted |
| 031 | `toddlers-1v6ujm8` | quoted | tb14-0297 (1) | teething detail not quoted |
| 031 | `pottytraining-1v780a8` | quoted | tb14-0298 … tb14-0299 (2) |  |
| 031 | `Parenting-1v79e1k` | quoted | tb14-0300 (1) | child anxiety framing and family mental-health history not quoted (unit flagged) |
| 031 | `daddit-1v7anhe` | quoted | tb14-0301 … tb14-0303 (3) | father's private insult not quoted |
| 031 | `ScienceBasedParenting-1v7fsa5` | quoted | tb14-0304 … tb14-0306 (3) | relative's "bite him back" joke not quoted |
| 031 | `toddlers-1v7he91` | quoted | tb14-0307 … tb14-0308 (2) | medication line not quoted |
| 032 | `toddlers-1v7hzsz` | quoted | tb14-0309 … tb14-0312 (4) | early-intervention speech evaluation and restraint remark not quoted (unit flagged) |
| 032 | `pottytraining-1v7jsis` | quoted | tb14-0313 … tb14-0315 (3) | constipation clause trimmed out |
| 032 | `daddit-1v7kcsj` | excluded | — (0) | physical force toward a child; diagnosis-centred replies |
| 032 | `toddlers-1v7lxg3` | quoted | tb14-0316 … tb14-0317 (2) |  |
| 032 | `toddlers-1v7nr7g` | excluded | — (0) | parent says spanking was tried; behavioural therapy for the child |
| 032 | `toddlers-1v7vr72` | quoted | tb14-0318 … tb14-0320 (3) |  |
| 032 | `Parenting-1v7w8kd` | quoted | tb14-0321 … tb14-0323 (3) | nappy-stripping passage and parent's anxiety line not quoted |
| 032 | `Mommit-1v7xu7l` | quoted | tb14-0324 (1) | pediatrician line not quoted |
| 032 | `Mommit-1v80xf6` | quoted | tb14-0325 … tb14-0326 (2) |  |
| 032 | `toddlers-1v8587n` | quoted | tb14-0327 … tb14-0329 (3) |  |
| 032 | `toddlers-1v87b6m` | quoted | tb14-0330 … tb14-0332 (3) |  |
| 032 | `toddlers-1v87lfi` | quoted | tb14-0333 … tb14-0334 (2) | yelling line not quoted |
| 032 | `toddlers-1v88hnq` | quoted | tb14-0335 … tb14-0337 (3) |  |
| 032 | `Parenting-1v8a6fs` | quoted | tb14-0338 … tb14-0339 (2) |  |

## How to continue

Nothing assigned to TR14 is unread. Do not re-run this reader against `voice/reddit-tr14.jsonl` (append-only; ids would collide). Units marked "unit flagged" above carry a diagnosis, developmental or medical question; only the parent's strain was quoted from them (list in the reader notes).
