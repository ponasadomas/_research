# Development unfilter report — 2026-11-16

Initial inventory written before changing findings, instructions or tools. Scope: `development/` and `../_shared/_tools/`; no network, no other build changes, no raw mutations. Reader notes, source ledgers and run logs remain historical records. Counts below are selected quotes or units, never people or prevalence.

## Verified baseline, by stage

- **Intake / triage:** `../_shared/_tools/niche_filter.py` assigned any safety-regex hit to a separate `safety` tier before applying A/B/C; only A produced reading cards. `sources/reddit.md` records 938 filter-v1 safety posts untriaged; the latest findings §13 records 349 filter-v2 safety posts unread. These overlap and must not be added. Frozen summary and candidate metadata were counted later to verify these figures; source bodies and full units were not read for the inventory. The id lists are preserved in each `safety-candidates.jsonl`. The sets overlap in 344 ids: 943 distinct routed posts overall, not 1,287. `brief-triage.md` also directed subject-based safety drops. The tighter development-v2 topic regex reduced intake of delay posts; relevance tiers themselves are not a restriction on quoting selected evidence.
- **Reading:** `README.md`, `product/product-brief.md`, shared `brief-reading.md` and `prompt-development-reader-w3.txt` imposed subject exclusions. Six source ledgers document **84 whole-unit exclusions**: DR01 13, DR02 15, DR03 22, DR04 6, DR05 17, DR06 11. Some reasons also mention duplicate/off-age evidence; preserve the reason rather than guessing its effect. DR06 additionally withheld `toddlers-1tjvzoj` because delay worry was already covered. These 85 units have no voice quotes. Lists and recorded reasons follow below.
- **Quote extraction:** DR04 explicitly withheld passages in 13 otherwise quoted units; DR06 lists medical side-details in 9 and a further safe-sleep omission in one more unit (10 unique units). The 23 ids follow below. Lost material includes conditions, medication, therapy, medical and birth history, head injury, reflux and sleep practices. These omissions cannot be restored verbatim from the voice files. DR01 withdrew `dv01-0086`–`dv01-0088` when `toddlers-1vxmiu2` was excluded; those reserved ids are not reissued. DR05 also notes unextracted prices in `beyondthebump-1tnt8fi`, `NewParents-1t8dis1`, and a first-word bet in `beyondthebump-1sdj400`; no subject-based reason is established for those three omissions. Its withheld therapy price belongs to the already excluded `toddlers-1sjjm1v`.
- **Marking:** `synthesis/restricted-ids.md` actually lists **237 unique ids**, all resolving in the 1,788 voice records: **218 Reddit + 19 review ids**, not 218 total. Prefix counts: dv01 34, dv02 70, dv03 31, dv04 26, dv05 32, dv06 25, dvr1 19. Reader notes and `sources/reviews.md` supply the labels. Original `voice/*.jsonl` have no restriction or marketing-eligibility fields. `audit_niche.py` copied the list into active `restricted` flags in `voice-merged/all.jsonl` and counts; `collect_restricted.py` replenished the list from historical notes.
- **Findings:** the original `synthesis/findings.md` cited 669 distinct ids. It cited **60** of the 237 marked ids while withholding their words, and omitted **177** entirely (158 Reddit + all 19 reviews). It also embedded no-quotation and no-wording-leak checks (appendix A6/A7), product/copy prohibitions, and historical quote-eligibility splits that obscured age-fit, referral, self-blame and contrary evidence.
- **Tooling / instructions:** shared `brief-findings.md` prohibited quotation and demanded a grep check; the verifier itself did **not** reject marked ids. `verify_findings_ids.py`, `check_ids.py`, and development `_tools/verify_quotes.py` check provenance/ids, not quote subject. Development `_tools/query.py` offered `--exclude-restricted` against `marketing_eligible=false` (currently zero matching records) and printed an eligibility warning. Shared `scaffold_niches.py` regenerated subject prohibitions; `write_source_maps.py` discouraged condition-source intake. The reader prompts for pregnancy (3), baby sleep (2), mother sleep (1), toddler (1), and development (1), the pregnancy/baby-sleep triage prompts, `brief-books-apps.md`, and the two restricted-review briefs also perpetuated exclusions. Historical scratch programs (`scratchpad/FINDINGS/a7.py`, `a8.py`, per-reader extraction builders and restricted lists) document past runs; do not re-run them to rebuild voice files.

## Historical gaps before the UR01–UR05 re-reading

This section records the initial inventory before UR01–UR05. Its then-unread status is superseded by the closing section below. Removing the rule alone could not recover words never extracted. The following lists come solely from reader ledgers/notes, not a new interpretation of raw units. A later reading must recover the whole excluded units and omitted passages; the precise number of missing quotes and any additional unlogged omissions is unknown. Earlier safety-tier intake remains a separate unread backlog; no claims about its contents are made here.

### DR01 whole-unit exclusions (13) — `sources/reddit-reading-dr01.md`

| unit | recorded reason |
|---|---|
| `toddlers-1vxmiu2` | centred on a suspected diagnosis (sign-by-sign checklist) |
| `toddlers-1vxoowa` | centred on a suspected diagnosis (symptom checklist) |
| `beyondthebumpUK-1w040a1` | centred on a diagnosed condition and hospital tests |
| `Mommit-1w104oa` | centred on the parent's own medical condition and treatment |
| `toddlers-1w29ymc` | centred on a motor-delay referral, therapy start and named conditions |
| `NewParents-1w5p0hm` | centred on the parent's own mental health and treatment |
| `beyondthebump-1waecge` | centred on a diagnosis and therapy start |
| `NewParents-1wb6l1q` | centred on therapy sessions, provider and cost of treatment |
| `Mommit-1wdpl5u` | centred on a referral, birth history and a named condition |
| `Mommit-1wwoggg` | centred on a child's diagnosed condition and its services |
| `Mommit-1wq4845` | centred on older siblings' diagnoses and therapy; babies in it are background |
| `toddlers-1xbs1zf` | centred on therapy sessions (treatment details) |
| `toddlers-1wgar73` | centred on diagnosis, assessments and therapy (treatment details) |

### DR02 whole-unit exclusions (15) — `sources/reddit-reading-dr02.md`

| unit | recorded reason |
|---|---|
| `NewParents-1wh9jb6` | centred on a diagnosis referral; excluded |
| `Mommit-1wis5hu` | centred on diagnosis and therapies; excluded |
| `Mommit-1wmqdvl` | centred on a suspected condition and family diagnoses; excluded |
| `beyondthebumpUK-1wo9ry6` | centred on a night-time rolling and choking safe-sleep worry; excluded |
| `NewParents-1wwabxw` | centred on an injury incident during tummy time; excluded |
| `toddlers-1wxanhg` | centred on a possible diagnosis and evaluation; excluded |
| `toddlers-1x5849j` | centred on a possible condition and evaluation; excluded |
| `toddlers-1x5ctzl` | centred on delays, therapies and an injury requiring treatment; excluded |
| `NewParents-1x5s4o4` | centred on a diagnosis and medical history; excluded |
| `toddlers-1x60dzr` | centred on a speech-delay label and ongoing therapy; excluded |
| `Mommit-1x67ezs` | centred on a possible diagnosis checklist; excluded |
| `toddlers-1xb16wc` | centred on an evaluation with delay scores and therapies; excluded |
| `NewParents-1xbouyz` | centred on medical symptoms and possible conditions; excluded |
| `NewParents-1xbtpx3` | centred on a safe-sleep question about rolling in a bedside crib; excluded |
| `toddlers-1xcr7r1` | centred on an assessment referral and self-injury; excluded |

### DR03 whole-unit exclusions (22) — `sources/reddit-reading-dr03.md`

| unit | recorded reason |
|---|---|
| `beyondthebumpUK-1uizx8k` | centred on a suspected condition and paediatric referral; excluded |
| `NewParents-1veir62` | centred on head shape and a medical device; excluded |
| `NewParents-1ugd2rt` | centred on medical history and head-shape treatment; excluded |
| `beyondthebumpUK-1ujs5go` | centred on bath falls and a water-safety incident; excluded |
| `NewParents-1ul7zt2` | centred on a sudden loss of a motor skill under a doctor's watch; excluded |
| `Mommit-1uojnck` | centred on delays, medical history and therapies; excluded |
| `daddit-1up34sw` | centred on an early-intervention evaluation with delay results; excluded |
| `NewParents-1upkkiv` | centred on a therapy referral and a medical diagnosis; excluded |
| `NewParents-1uq9t89` | centred on motor delays and therapists' decisions; excluded |
| `toddlers-1usd6ah` | centred on a communication delay, therapy and diagnosis questions; excluded |
| `NewParents-1usv1yg` | safe-sleep question about rolling and swaddling; excluded |
| `NewParents-1utlmik` | centred on repeated head-bump injuries; excluded |
| `daddit-1uxhuvm` | centred on an early-intervention referral after a check-up; excluded |
| `NewParents-1uykt8x` | centred on a suspected condition and specialist visits; excluded |
| `toddlers-1uz5zsg` | centred on a developmental evaluation and behaviour at daycare; excluded |
| `beyondthebump-1uzyvam` | centred on medical and genetic worry and the parent's mental-health treatment; excluded |
| `NewParents-1v001hm` | centred on medical history and delay worry; excluded |
| `beyondthebump-1v2oaua` | centred on a feared neurological symptom; excluded |
| `NewParents-1v34t3n` | centred on therapy, surgery and a helmet; excluded |
| `toddlers-1utsjav` | centred on a speech evaluation; excluded |
| `toddlers-1v2cxlw` | centred on a suspected condition in a relative's child; excluded |
| `toddlers-1vgmn0n` | centred on a speech-therapy referral question, child over 24 months; excluded |

### DR04 whole-unit exclusions (6) — `sources/reddit-reading-dr04.md`

| unit | recorded reason |
|---|---|
| `toddlers-1v3hna0` | centred on a diagnosis and screening referral (medical detail); excluded |
| `beyondthebump-1v6cynu` | centred on a parent's mental-health crisis and a delay concern; excluded |
| `NewParents-1vjubgz` | centred on infant sleep position and rolling in sleep (safe-sleep topic); excluded |
| `beyondthebump-1vmvm9v` | centred on a medical history and delay concern with a parent's mental-health crisis; excluded |
| `NewParents-1vuqkpa` | centred on a check-up finding, referral and medical monitoring; excluded |
| `NewParents-1vxebr6` | centred on a suspected condition, physio and osteopath treatment; excluded |

### DR05 whole-unit exclusions (17) — `sources/reddit-reading-dr05.md`

| unit | recorded reason |
|---|---|
| `NewParents-1sanmle` | centred on a condition worry, therapy and a parent's medication; excluded |
| `NewParents-1sd0fl6` | centred on a condition worry; excluded |
| `NewParents-1segz90` | head injury and medication dose; excluded |
| `Parenting-1sfd733` | centred on a speech and walking delay concern; excluded |
| `NewParents-1sfz45v` | centred on a parent's postpartum mental-health diagnosis and medication; excluded |
| `FirstTimeMom-1sg8rkl` | safe-sleep incident (bed-sharing, baby found on stomach); excluded |
| `toddlers-1sjjm1v` | centred on a diagnosis evaluation; a therapy price in it is not quoted; excluded |
| `Mommit-1smixd1` | centred on a developmental evaluation result and an intervention programme; excluded |
| `beyondthebump-1spygnj` | centred on a head-shape condition and hospital history; excluded |
| `Mommit-1sqyv0e` | centred on a medical procedure and hearing concern; excluded |
| `beyondthebump-1szztjf` | infant head injury; excluded |
| `toddlers-1t7bn61` | centred on a speech delay and intervention programme; excluded |
| `toddlers-1t8guw9` | centred on a diagnosis-assessment question; excluded |
| `NewParents-1tb1qj4` | safe-sleep position and a medical condition; excluded |
| `beyondthebump-1t4mgmn` | partner's post centred on a mental-health condition, medication and a diagnosis fear; excluded |
| `daddit-1txrfxv` | centred on an early-intervention evaluation for speech therapy; excluded |
| `toddlers-1s9o7sr` | centred on an early-intervention evaluation result; excluded |

### DR06 whole-unit exclusions (11) — `sources/reddit-reading-dr06.md`

| unit | recorded reason |
|---|---|
| `NewParents-1th1h1i` | centred on a medical condition and its treatment |
| `toddlers-1tkex9t` | centred on a diagnosis and therapy referrals |
| `beyondthebump-1tuo158` | centred on a child's therapy and conditions |
| `NewParents-1tx3k34` | centred on a premature baby's therapy referral and medical tests |
| `toddlers-1u3mzg6` | centred on a possible diagnosis and therapy referral |
| `Mommit-1u4e459` | centred on a medical history and an early-intervention referral after a clinician's finding |
| `toddlers-1u55kub` | centred on fear of a diagnosis and specialist appointments |
| `NewParents-1u5fyp3` | contains a mental-health crisis signal and diagnoses |
| `beyondthebump-1u7lnjh` | centred on therapy and fear of a diagnosis |
| `NewParents-1u7vii0` | same author and text as `1u7lnjh` (crosspost); same reason |
| `Mommit-1ue5ajf` | centred on a developmental-clinic evaluation and therapy referral after a medical history |

DR06 additional no-quote unit: `toddlers-1tjvzoj` (speech-assessment question; reader said usable delay worry was covered elsewhere).

### DR04 passage omissions (13 units) — `sources/reddit-reading-dr04.md`

`toddlers-1v3z3vy`, `NewParents-1vg7gos`, `NewParents-1vh9o73`, `beyondthebump-1vjb8zp`, `beyondthebumpUK-1vjrxym`, `FirstTimeMom-1vjw0hd`, `toddlers-1vmww9u`, `NewParents-1vnhzrd`, `Mommit-1vrtn1b`, `FirstTimeMom-1vsqnlu`, `FirstTimeMom-1vss9qh`, `beyondthebump-1vtkr8u`, `NewParents-1wvxkjn`.

### DR06 passage omissions (10 units) — `sources/reddit-reading-dr06.md`

`beyondthebump-1ttxang`, `beyondthebump-1tv28uu`, `beyondthebump-1tv484w`, `NewParents-1u5a9av`, `NewParents-1uaad37`, `Parenting-1uadc72`, `Mommit-1to2gxt`, `NewParents-1tsiofa`, `FirstTimeMom-1u334xt`, `beyondthebump-1ud3veu`.

`beyondthebump-1ud3veu` is resolved from the ledger's bare post id using the existing voice record, not by opening raw. The 84 exclusions + 1 extra no-quote unit + 23 partially quoted units form **108 named units needing re-reading for known subject-based omissions**. Three additional DR05 price/bet omissions are noted separately above. No missing words have been fabricated or voice ids added/deleted.

## Intake and triage omissions before full reading

Metadata-only inventory verified `_raw/reddit/filter-v1/safety-candidates.jsonl` (938 records) and `filter-v2/safety-candidates.jsonl` (349), with 344 overlapping unit keys (943 distinct). Their `subreddit` + `id` fields give the exact future reading queue. These were routed away from A/B/C by `niche_filter.py`; no source body was re-read and no candidate file was regenerated.

The frozen `_raw/reddit/triage/wave*-*.tsv` files contain **76 drops explicitly prefixed `safety:`**, all in waves 2–3. Another **43 drop reasons** mention safety, medical topics, diagnosis or crisis without that prefix. Some also have ordinary off-topic, older-child or duplicate reasons; these 43 are review candidates, not 43 proven censorship cases. Wave-1 triage reasons have no matches for these labels. These queues need future full reading/reassessment, in addition to the 108 documented reader omissions; the sets must not be added without deduplication. No words can be recovered from their metadata alone.

### Explicit safety drops (76)

| triage file under `_raw/reddit/triage/` | post id | recorded reason |
|---|---|---|
| `wave2-W2DT1.tsv` | `1vv3djz` | safety: partner dispute over baby's therapy exercises, treatment-centred |
| `wave2-W2DT1.tsv` | `1uio24r` | safety: mental health testimony, not about development |
| `wave2-W2DT1.tsv` | `1ulzc19` | safety: medical treatment of head-turn preference at 9 weeks |
| `wave2-W2DT1.tsv` | `1ut54xo` | safety: head shape helmet treatment decision |
| `wave2-W2DT1.tsv` | `1vndlw1` | safety: oral feeding therapy for a diagnosis |
| `wave2-W2DT1.tsv` | `1ukxg4u` | safety: 4-year-old delay and diagnosis context, older child |
| `wave2-W2DT1.tsv` | `1vx7st4` | safety: 24-month weight and bloodwork, medical |
| `wave2-W2DT1.tsv` | `1ufewmm` | safety: physiotherapy for a medically complex baby; treatment-centred |
| `wave2-W2DT1.tsv` | `1usnf6o` | safety: 15-month surgical condition |
| `wave2-W2DT1.tsv` | `1v1bx06` | safety: baby with medical conditions, fussiness |
| `wave2-W2DT1.tsv` | `1uj3vm6` | safety: cleft palate feeding, medical |
| `wave2-W2DT2.tsv` | `1um6jim` | safety: infant sleep position medical question |
| `wave2-W2DT2.tsv` | `1uyt69l` | safety: 3-year-old evaluation and diagnosis worry, over 24 months |
| `wave2-W2DT2.tsv` | `1v1bxc1` | safety: baby with medical conditions, caregiver rant |
| `wave2-W2DT2.tsv` | `1vbaky8` | safety: medical condition fear from a video |
| `wave2-W2DT2.tsv` | `1vd3ubx` | safety: medical history, parent exhaustion |
| `wave2-W2DT2.tsv` | `1uyfhnf` | safety: physiotherapy for a past condition, treatment disagreement |
| `wave2-W2DT2.tsv` | `1v1bxzm` | safety: baby with medical conditions, parent rant |
| `wave2-W2DT2.tsv` | `1v365mh` | safety: near-duplicate of 1v3e6ht naming a condition |
| `wave2-W2DT2.tsv` | `1v3fwxu` | safety: reflux treatment, medical |
| `wave2-W2DT2.tsv` | `1v4diq2` | safety: weight gain and medical diagnosis |
| `wave2-W2DT2.tsv` | `1v81zs3` | safety: reflux and work-life balance |
| `wave2-W2DT2.tsv` | `1v9r0dw` | safety: diagnosis of poor growth |
| `wave2-W2DT2.tsv` | `1vci6xo` | safety: infant stooling medical |
| `wave2-W2DT2.tsv` | `1vaqfuf` | safety: co-sleeping risk debate |
| `wave2-W2DT2.tsv` | `1vs2jjf` | safety: diagnosis and physiotherapy positioning |
| `wave2-W2DT2.tsv` | `1vknw5y` | safety: postpartum medication experience |
| `wave2-W2DT2.tsv` | `1vel65l` | safety: prenatal screening worry |
| `wave2-W2DT2.tsv` | `1usup5w` | safety: child with diagnosed condition, 2.5 years |
| `wave2-W2DT2.tsv` | `1v75lnz` | safety: screening and evaluation for a condition |
| `wave2-W2DT2.tsv` | `1vrf1i6` | safety: therapy appointments and diagnosis for older child |
| `wave3-W3DT1.tsv` | `1slze79` | safety: caregiver distress about anger at baby; mostly crying/sleep |
| `wave3-W3DT1.tsv` | `1tr8olk` | safety: centred on head-shape medical question and treatment |
| `wave3-W3DT1.tsv` | `1u9o98x` | safety: medical stool symptoms question |
| `wave3-W3DT1.tsv` | `1uappet` | safety: head measurement and scan results worry |
| `wave3-W3DT1.tsv` | `1ubik33` | safety: diagnosis and medical question |
| `wave3-W3DT1.tsv` | `1sdu014` | safety: centred on flat head, chiropractic treatment and helmet claims |
| `wave3-W3DT1.tsv` | `1sqllv5` | safety: 6-year-old autism assessment, older child |
| `wave3-W3DT1.tsv` | `1tc9bqp` | safety: looks back on torticollis, helmet and delay treatment, 2.5-year-old |
| `wave3-W3DT1.tsv` | `1ss9k7k` | safety: neonatal medical history guilt, development absent |
| `wave3-W3DT1.tsv` | `1t8zl4j` | safety: centred on fear of a condition from family history |
| `wave3-W3DT1.tsv` | `1te2mue` | safety: centred on diagnosis and medical history |
| `wave3-W3DT1.tsv` | `1tf8kmq` | safety: centred on cancer treatment of 3-year-old |
| `wave3-W3DT1.tsv` | `1s961qo` | safety: parent mental health crisis, off-topic |
| `wave3-W3DT1.tsv` | `1snzipa` | safety: centred on how to fix head flat spot |
| `wave3-W3DT1.tsv` | `1t657ya` | safety: preterm baby reflux and colic, medical |
| `wave3-W3DT1.tsv` | `1tc4a0h` | safety: feeding and swallowing condition, sleep association |
| `wave3-W3DT1.tsv` | `1tg15cn` | safety: parent's postpartum crisis, off-topic |
| `wave3-W3DT1.tsv` | `1sjqjm0` | safety: 4-year-old with genetic condition |
| `wave3-W3DT1.tsv` | `1s9v3j6` | safety: 2-year-old failed vision and hearing screen, medical |
| `wave3-W3DT1.tsv` | `1saxkoq` | safety: 15-month-old head size percentile, medical measurement |
| `wave3-W3DT1.tsv` | `1setm8c` | safety: vitamin levels and allergy, medical |
| `wave3-W3DT1.tsv` | `1sine8k` | safety: centred on therapist's sensory label and therapy |
| `wave3-W3DT1.tsv` | `1sna9fu` | safety: centred on autism worry from absent words and gestures |
| `wave3-W3DT1.tsv` | `1sqwn0w` | safety: anemia history and daytime sleepiness, medical |
| `wave3-W3DT1.tsv` | `1sr903b` | safety: genetic condition with epilepsy |
| `wave3-W3DT1.tsv` | `1sy9bc5` | safety: speech diagnosis and therapy, 2.5-year-old |
| `wave3-W3DT1.tsv` | `1t2hims` | safety: possible fracture after fall, medical |
| `wave3-W3DT1.tsv` | `1te3prp` | safety: centred on diagnosis and medical history |
| `wave3-W3DT1.tsv` | `1tfpsko` | safety: centred on cancer treatment of 3-year-old |
| `wave3-W3DT2.tsv` | `1u9rwv8` | safety: concern about caregiver handling baby |
| `wave3-W3DT2.tsv` | `1uck2ln` | safety: centred on medical conditions and treatment guilt |
| `wave3-W3DT2.tsv` | `1ss5iw1` | safety: partner anger toward baby |
| `wave3-W3DT2.tsv` | `1tsg8x2` | safety: centred on diagnosis and therapy of a 22-month-old |
| `wave3-W3DT2.tsv` | `1ttf1qv` | safety: medical test for head movements |
| `wave3-W3DT2.tsv` | `1twpar0` | safety: genetic diagnosis and therapy method |
| `wave3-W3DT2.tsv` | `1sme735` | safety: lip and tongue tie, medical |
| `wave3-W3DT2.tsv` | `1smkc08` | safety: sensory regulation linked to diagnoses |
| `wave3-W3DT2.tsv` | `1tuz354` | safety: centred on a condition worry for 12-month-old |
| `wave3-W3DT2.tsv` | `1sxshaf` | safety: growth faltering, medical |
| `wave3-W3DT2.tsv` | `1tm5l0n` | safety: skin infection, medical |
| `wave3-W3DT2.tsv` | `1tszf9q` | safety: weight percentile, medical |
| `wave3-W3DT2.tsv` | `1tv94co` | safety: baby fear after head fall, medical |
| `wave3-W3DT2.tsv` | `1th9bmz` | safety: autism testing question, diagnosis centred |
| `wave3-W3DT2.tsv` | `1tvfq1i` | safety: medical question about water intake |
| `wave3-W3DT2.tsv` | `1u8aod7` | safety: feeding therapy question |

### Additional potentially subject-based drops (43)

| triage file under `_raw/reddit/triage/` | post id | recorded reason |
|---|---|---|
| `wave2-W2DT1.tsv` | `1um6nk3` | preemie sleep position, medical |
| `wave2-W2DT1.tsv` | `1vjnpyn` | pets and baby safety |
| `wave2-W2DT1.tsv` | `1vkkb31` | growth and weight concern; medical |
| `wave2-W2DT1.tsv` | `1vr6bym` | pet safety |
| `wave2-W2DT1.tsv` | `1vvf9wu` | toddler congestion sleep, medical |
| `wave2-W2DT1.tsv` | `1uk1avc` | parent medical injections |
| `wave2-W2DT1.tsv` | `1v2b566` | breastfeeding crisis |
| `wave2-W2DT2.tsv` | `1ve4jw5` | sick baby, medical |
| `wave2-W2DT2.tsv` | `1vlujco` | infant stooling, medical |
| `wave2-W2DT2.tsv` | `1vmfyn0` | baby gate product question, safety gear |
| `wave2-W2DT2.tsv` | `1vkaxln` | wardrobe and floor bed safety for 4-month-old |
| `wave2-W2DT2.tsv` | `1vs2jdc` | school safety observations on tour |
| `wave2-W2DT2.tsv` | `1v3041b` | sick baby, medical |
| `wave2-W2DT2.tsv` | `1vmudlm` | sleep safety, lovey |
| `wave2-W2DT2.tsv` | `1un930m` | travel crib safety incident |
| `wave2-W2DT2.tsv` | `1v1s1bx` | baby gate installation, safety gear |
| `wave3-W3DT1.tsv` | `1t9ox4s` | 6-week-old congestion, medical and sleep |
| `wave3-W3DT1.tsv` | `1u1tukr` | reaction after 12-month vaccinations, medical |
| `wave3-W3DT1.tsv` | `1twgl69` | child nearly 2 falling from bed, safety worry |
| `wave3-W3DT1.tsv` | `1sku9vu` | colic, medical |
| `wave3-W3DT1.tsv` | `1skv7h2` | preterm baby constant crying, medical |
| `wave3-W3DT1.tsv` | `1sld7p7` | newborn bassinet sleep safety |
| `wave3-W3DT1.tsv` | `1t9o0zn` | 6-week-old congestion, medical and sleep |
| `wave3-W3DT1.tsv` | `1tddn0v` | baby asleep on belly with sitter, sleep safety |
| `wave3-W3DT1.tsv` | `1tjtqfo` | 19-week-old gas screaming, medical |
| `wave3-W3DT1.tsv` | `1sj83wb` | 1-year-old screaming and moany since reflux, behaviour and medical history |
| `wave3-W3DT1.tsv` | `1sqywm7` | dog nipped 14-month-old, safety incident |
| `wave3-W3DT1.tsv` | `1scdmmm` | driveway blocking product, outdoor safety |
| `wave3-W3DT1.tsv` | `1svxrsm` | window fall story at 20 months, safety incident |
| `wave3-W3DT2.tsv` | `1u36zli` | toddler behaviour change after fever, medical history |
| `wave3-W3DT2.tsv` | `1taydbm` | 4-year-old with diagnoses |
| `wave3-W3DT2.tsv` | `1tx4v6j` | 3-year-old school tour safety |
| `wave3-W3DT2.tsv` | `1srgt4x` | egg allergy, feeding/medical |
| `wave3-W3DT2.tsv` | `1ssg5oe` | parent's gut worry, medical tests, feeding-centred |
| `wave3-W3DT2.tsv` | `1ssn2ap` | reflux, medical |
| `wave3-W3DT2.tsv` | `1suviqn` | reflux, medical |
| `wave3-W3DT2.tsv` | `1t00k4c` | growth rate, medical |
| `wave3-W3DT2.tsv` | `1tu3ga9` | 8-week-old overwhelm, head-turn medical concern |
| `wave3-W3DT2.tsv` | `1t9o1v4` | 6-week-old congestion, medical |
| `wave3-W3DT2.tsv` | `1smlp3f` | crib safety |
| `wave3-W3DT2.tsv` | `1sxctpp` | pediatrician head size remark, medical |
| `wave3-W3DT2.tsv` | `1tb4ya3` | bassinet safety after rolling, sleep |
| `wave3-W3DT2.tsv` | `1tzhq66` | reflux, medical |

## Changes and verification

**Restored:** all 237 historical ids now appear with their full voice wording in the main findings: 60 previously cited without words, 177 previously uncited. All 669 original cited ids remain; findings now cite 846 distinct ids. No original voice record or reserved id changed. Existing direct fragments were also aligned to their source typography; 802 directly paired fragments match exactly, not merely after quote normalization. The historical marking list is retained intact.

**Conclusions moved:** self-blame can consume presence and enjoyment; the age-fit ask and delay worry are directly connected; professional advice ranges from reassurance to monitoring/referral and leaves access questions; the money evidence includes a failed 100 USD physiotherapy session and willingness to pay privately for early intervention; milestone apps can reassure or repeatedly alarm and can mishandle corrected age; comparison is also twins, cousins, daycare, family scrutiny and public questioning; a parent's direct rejection of fear-based toy marketing is evidence too. The dated final section of findings gives the ids behind each. The absence of a demonstrated Reddit guide purchase remains unchanged.

**Future behavior:** research principles replace subject prohibitions in reusable instructions. `niche_filter.py` retains descriptive labels while routing all available matches normally through A/B/C. `collect_restricted.py` only validates/reports the historical list and cannot replenish it. Development `query.py --exclude-restricted` is a compatibility no-op; it cannot hide records. `audit_niche.py` emits no active restrictions; the current derived merged file preserves all record content and historical marks with `formerly_restricted`, with every `restricted` flag false. Counts distinguish historical labels from active restrictions.

**Preserved records:** source ledgers, reader notes, scratch/run artifacts, audit spot-check and safety-hit history remain untouched. Their old prohibitions describe history, not current research policy. `verify_findings_ids.py`, `check_ids.py` and `_tools/verify_quotes.py` retain all checks; none originally rejected restricted ids. No raw files were changed or deleted, no other build was changed, no network was used, and nothing was pushed. The pre-existing untracked `scratchpad/unfilter-2026-11-16.last.md` was left untouched and is excluded from the commit.

### Exact changed-file list (29 files)

- `mamivio.com/research/_shared/_tools/audit_niche.py`
- `mamivio.com/research/_shared/_tools/brief-books-apps.md`
- `mamivio.com/research/_shared/_tools/brief-findings.md`
- `mamivio.com/research/_shared/_tools/brief-reading.md`
- `mamivio.com/research/_shared/_tools/brief-restricted-review-sm-w2.md`
- `mamivio.com/research/_shared/_tools/brief-restricted-review.md`
- `mamivio.com/research/_shared/_tools/brief-triage.md`
- `mamivio.com/research/_shared/_tools/collect_restricted.py`
- `mamivio.com/research/_shared/_tools/niche_filter.py`
- `mamivio.com/research/_shared/_tools/prompt-development-reader-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-pregnancy-reader-w2.txt`
- `mamivio.com/research/_shared/_tools/prompt-pregnancy-reader-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-pregnancy-reader.txt`
- `mamivio.com/research/_shared/_tools/prompt-pregnancy-triage-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-sleep-baby-reader-w2.txt`
- `mamivio.com/research/_shared/_tools/prompt-sleep-baby-reader-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-sleep-baby-triage-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-sleep-mother-reader-w3.txt`
- `mamivio.com/research/_shared/_tools/prompt-toddler-reader-w3.txt`
- `mamivio.com/research/_shared/_tools/scaffold_niches.py`
- `mamivio.com/research/_shared/_tools/write_source_maps.py`
- `mamivio.com/research/development/README.md`
- `mamivio.com/research/development/_tools/query.py`
- `mamivio.com/research/development/product/product-brief.md`
- `mamivio.com/research/development/synthesis/counts.md`
- `mamivio.com/research/development/synthesis/findings.md`
- `mamivio.com/research/development/synthesis/restricted-ids.md`
- `mamivio.com/research/development/synthesis/unfilter-report.md`
- `mamivio.com/research/development/voice-merged/all.jsonl`

### Commands and output

All Python checks ran with `python3 -I`. Audit used the new `--check-only` mode to inspect the frozen assignment manifests without rewriting historical audit notes; it did not open source units. The source verifier mechanically checked only raw files cited by existing voice records, never the 85 withheld whole units. `units_quoted=642` counts all raw-file paths, including 32 review source files; `assigned_units_quoted=610` counts Reddit assignment paths. Neither counts people.

`python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/development/synthesis/findings.md development` — exit 0

```text
846 distinct ids cited, 0 unresolved
802 verbatim fragments paired with an id, 0 failed
```

`python3 -I mamivio.com/research/_shared/_tools/check_ids.py development` — exit 0

```text
1788 records, 1788 distinct ids, 0 duplicated
```

`python3 -I mamivio.com/research/_shared/_tools/audit_niche.py development read-v1 read-w2 read-w3 --check-only` — exit 0

```text
{"quotes": 1788, "assigned": 723, "units_quoted": 642, "assigned_units_quoted": 610, "uncited": 113, "unexplained": 0, "historically_marked": 237, "active_restrictions": 0, "safety_hits": 4}
```

`python3 -I mamivio.com/research/development/_tools/verify_quotes.py` — exit 0

```text
reddit-dr01.jsonl: 215 quotes, 0 failed
reddit-dr02.jsonl: 388 quotes, 0 failed
reddit-dr03.jsonl: 276 quotes, 0 failed
reddit-dr04.jsonl: 235 quotes, 0 failed
reddit-dr05.jsonl: 299 quotes, 0 failed
reddit-dr06.jsonl: 211 quotes, 0 failed
reviews-rv1.jsonl: 164 quotes, 0 failed
TOTAL 1788 quotes, 0 failed
```

`python3 -I mamivio.com/research/_shared/_tools/collect_restricted.py development` — exit 0

```text
development: 237 historical labels, 0 unresolved; no restrictions applied or written
```

`python3 -I /tmp/unfilter_validate.py` — exit 0

```text
237/237 full quotes reproduced verbatim in main findings; 60 formerly cited + 177 formerly omitted; 669/669 original cited ids retained.
1788 voice records unchanged; derived records differ only in active/historical flags; 108 named extraction gaps reconciled.
Query compatibility check: --exclude-restricted retains both fixture records, including marketing_eligible=false and restricted=true.
Intake check: both synthetic matching posts stay in tier A, including the safety-labelled post; no raw output written.
Scope check: no raw files, other builds, original voice files, historical reader notes, ledgers or logs changed.
```

`~/GitHub/_home/check.sh` — exit 0

```text
== skill paths that point outside _home ==
none
== library files not listed in their index ==
none
```

`git diff --check` — exit 0

```text
(no output)
```

The temporary validation script checked all 237 full literal quotes outside the final change note, preservation of all original cited ids, derived-record equality apart from the two label fields, the 108 reader-gap unit ids, query behavior with synthetic false eligibility/true restriction fields, and intake routing with two synthetic posts differing only in a safety label. Its intake fixture used dry mode outside the repository; no `_raw/` output was created.

Additional in-memory syntax and isolated audit-generation checks — exit 0:

```text
Syntax check: 15 Python files compiled in memory; no bytecode files written.
Audit generation check: 20/20 fixture records retained; 1 historical label, 0 active restrictions; no raw paths created.
```

### Remaining uncertainty

The 108 named reader omissions are a documented minimum, not a reconstruction of all missing material. The 943 routed intake posts and the 76 explicit / 43 potentially subject-based triage drops are separate, overlapping historical queues; metadata alone cannot establish relevance, source wording or how many independent experiences they represent. Some drops also mention older ages, duplicates or off-topic content; those reasons need reassessment without subject exclusions. Three DR05 price/bet omissions are recorded separately because the notes do not establish censorship as their cause. No raw re-reading to recover these gaps was done in this task.

### Commit attempt — blocked by filesystem permissions

On branch `research-unfilter`, staging the exact 29 files failed before any commit could be created. The environment mounts `.git` read-only; no permission escalation is available in this session. Working-tree changes are intact, the pre-existing untracked scratch note remains excluded, and nothing was staged or pushed.

```text
fatal: Unable to create '/home/thinkpad/GitHub/ads/.git/index.lock': Read-only file system
```

The requested commit message is `Remove development research quote restrictions and restore findings`. Creating that commit in this checkout remains the only unfinished step.


## Re-reading closed and findings integrated — 2026-11-16

UR01–UR05 completed **1,169/1,169 assigned reads**, with **0 missing or unfinished**: **727** rows supplied **1,182 quotes**; **442** supplied relevance-only results. All 1,182 quotes and the five closing ledger sections were read for this revision. Findings now cite **1,086 distinct ids**, including **240 UR ids** (**229 UR quotes reproduced in full**), preserving all **846** earlier ids. Twelve evidence subsections and the final dated change section record the revised conclusions. The existing audit rebuilt **2,970 merged quotes** (2,806 Reddit + 164 reviews), with **0 active restrictions**.

Both historical safety queues are complete: **943 distinct ids** across filter-v1 and filter-v2. Ordinary unread queues remain; `sources/reddit.md` gives their exact overlapping totals and subtraction method. Four prior extraction omissions are outside the completed assignments: DR06’s already-read `toddlers-1tjvzoj`, and DR05’s price/bet mentions in `1tnt8fi`, `1t8dis1`, `1sdj400`. Those remain unextracted, not unfinished UR reads. Archive-only reads cannot supply absent replies; UR03’s saved mid-sentence ending remains a source limitation. Reported diagnoses, treatment effects and harm were not independently adjudicated.

Changed for this integration: `README.md`, `synthesis/findings.md`, `synthesis/counts.md`, `sources/reddit.md`, this report, `voice-merged/all.jsonl`, and `synthesis/audit-safety-hits.tsv`. No raw file, original voice record or reader ledger was changed; the historical spot-check worksheet was preserved. No network or git was used.

### Integration checks (all exit 0)

Run from `mamivio.com/research/`:

```text
python3 -I _shared/_tools/verify_findings_ids.py development/synthesis/findings.md development
1086 distinct ids cited, 0 unresolved
1008 verbatim fragments paired with an id, 0 failed

python3 -I _shared/_tools/check_ids.py development
2970 records, 2970 distinct ids, 0 duplicated

python3 -I _shared/_tools/audit_niche.py development read-v1 read-w2 read-w3 --check-only
{"quotes": 2970, "assigned": 723, "units_quoted": 757, "assigned_units_quoted": 694, "uncited": 29, "unexplained": 0, "historically_marked": 237, "active_restrictions": 0, "safety_hits": 86}
```

Additional isolated checks used `/tmp/verify_development_reread.py`. The unchanged development `_tools/verify_quotes.py` was run with an in-memory decoded JSONL source cache, because literal JSON serialization escapes are not source-wording differences. A separate strict check matched each UR quote only to its own `post_id` in its own archive (or its cited unit), without normalization. No shared tool or source was edited. The exact-fragment check additionally includes short immediately paired quotes the stock findings checker does not inspect.

```text
Strict source check: 1182/1182 UR quotes match their own decoded post or cited unit literally; 0 failed.
Build source verifier with read-only JSONL adapter: TOTAL 2970 quotes, 0 failed.
Exact findings check: 1018 paired fragments match voice wording without normalization; 0 failed.
Citation preservation: 846/846 previous ids retained; 1086 current distinct ids; 240 UR ids, 229 reproduced in full.
Merged integrity: 2970/2970 records preserved; only audit flags and 2 documented speaker relabels; 0 active restrictions.
Protected-file integrity: 23 original voice/reader-ledger files unchanged; historical spot-check worksheet unchanged.
```

The audit’s coverage figures count raw-file paths from the original three manifests. They do not measure the UR assignment coverage or distinct archive posts; `counts.md` and `sources/reddit.md` explicitly reconcile those measures. No blank historical spot-check verdict was represented as completed.
