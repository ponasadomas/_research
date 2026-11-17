# Reddit reading ledger — PR54 (wave 3, keep_core chunks 024–031)

Reader PR54, id prefix pb54, written 2026-10-25. Brief: `_shared/_tools/prompt-pregnancy-reader-w3.txt` and `_shared/_tools/brief-reading.md`.

| step | count |
|---|---|
| chunks assigned | 8 (read-w3-keep_core-024 … read-w3-keep_core-031) |
| units in them | 151 (19+19+19+16+19+20+23+16) |
| units read in full | 151 |
| units with at least one quote | 91 |
| units excluded under the lines not to cross | 29 |
| units read, nothing quoted (thin, medical-only or off-niche) | 28 |
| units flagged (possible bait / embellished) | 3 (one quoted as one voice) |
| crossposts (same author, same text) | 2 (post text quoted once; one copy's own replies also quoted) |
| quotes written | 205 (pb54-0001 … pb54-0205) |
| restricted quotes | 17 (listed in `synthesis/reader-notes-pr54.md`) |
| verify | `python3 -I _tools/verify_quotes.py voice/reddit-pr54.jsonl` → 205 quotes, 0 failed |

Posts dated 9–13 April 2026 (one follow-up comment from 3 June). Unit list: `scratchpad/PR54/units.txt`. Quote source records: `scratchpad/PR54/recs/rec-0NN.py`, built by `scratchpad/PR54/build.py` (rebuilds the voice file from the records; never append by hand).

The row counts overlap by two units (1siwrbd is flagged and quoted; 1shmn7g is a crosspost whose replies are quoted), so 91 + 29 + 28 + 3 + 2 = 153 rows for 151 units. Nothing is unread.

## Excluded (neutral reason; not quoted)

| chunk | unit | reason |
|---|---|---|
| 024 | pregnant-1sgz69b | centred on a screening finding and specialist referral |
| 024 | pregnant-1sgzkt6 | mental-health post with medication |
| 024 | pregnant-1sh110y | weighs whether to continue the pregnancy |
| 024 | pregnant-1sh65uh | mental-health post with medication |
| 025 | pregnant-1shc6rg | acute medical condition found in pregnancy |
| 025 | PregnancyUK-1shgm9w | weighs whether to continue the pregnancy |
| 025 | pregnant-1shjocs | partner just left; hopeless wording, relationship crisis |
| 026 | BabyBumps-1shq9c5 | centred on alcohol and substance use around early pregnancy |
| 026 | pregnant-1shv8q5 | untreated mental-health and substance wording |
| 026 | beyondthebump-1shv5cb | severe mental-health post after an emergency birth |
| 026 | pregnant-1si4b2o | author describes trying to conceive as a minor |
| 027 | BabyBumps-1si7i6c | centred on a birth emergency and its aftermath |
| 027 | pregnant-1sifsdf | weighs not continuing the pregnancy; diagnosed mental-health condition |
| 027 | pregnant-1sigj99 | centred on alcohol use in pregnancy and parental substance use |
| 027 | Mommit-1sim5x4 | severe mental-health and partner-conduct wording; near-drop of baby |
| 027 | beyondthebump-1sim8ag | crosspost of Mommit-1sim5x4; same reason |
| 028 | pregnant-1sirir0 | fear of loss and fetal harm after a food exposure |
| 028 | pregnant-1sizpzk | same author as BabyBumps-1shq9c5; alcohol and medication wording |
| 028 | pregnant-1sj5ohx | eating disorder, alcohol recovery and severe mental-health wording |
| 028 | pregnant-1sj7q4w | mental-health medication post |
| 028 | pregnant-1sje2ak | antenatal depression; likely same author as pregnant-1sifsdf |
| 029 | pregnant-1sjn18v | substance use in pregnancy |
| 029 | pregnant-1sjnvyb | substance exposure worry |
| 029 | beyondthebump-1sjsdk0 | postpartum mental-health medication decision |
| 029 | pregnant-1sjtlad | centred on expected pregnancy loss |
| 029 | pregnant-1sjum0i | crisis wording |
| 030 | pregnant-1sk2ih2 | alcohol craving and recovery in pregnancy |
| 030 | pregnant-1sk4uup | sexual-assault history and severe mental-health wording |
| 031 | PregnancyUK-1ske2p4 | acute bleeding and hospital visit |

## Read in full, nothing quoted

| chunk | unit | reason |
|---|---|---|
| 025 | BabyBumps-1shdudc | medication question only |
| 025 | pregnant-1shk6pa | medication and symptom-loss worry only |
| 025 | pregnant-1shpsrt | supplement question; mentions prior loss and low mood |
| 026 | pregnant-1sht1t6 | too thin |
| 026 | PregnancyUK-1shu2c8 | medication injection question |
| 026 | pregnant-1si5pll | not pregnant; workplace rivalry |
| 027 | NewParents-1sihb36 | six-week dummy question, nothing for this niche |
| 027 | pregnant-1sijy7x | chemical exposure question only |
| 028 | pregnant-1siw68z | too thin |
| 028 | pregnant-1sixtvh | symptom and medication question only |
| 028 | pregnant-1sj0sdm | chronic condition and medication only |
| 029 | pregnant-1sjfnik | shoe sizing; nothing for niche |
| 029 | PregnancyUK-1sjg75e | triage visit, gender slip; thin |
| 029 | PregnancyUK-1sjltjz | relationship conflict with control wording |
| 029 | BabyBumps-1sjrllt | early caffeine worry only |
| 029 | pregnant-1sjtm6k | bleeding worry, medical |
| 029 | pregnant-1sjuia7 | medication side-effect question |
| 030 | pregnant-1sjy30n | food rule question, thin |
| 030 | pregnant-1sjyqvk | symptom question, medical |
| 030 | BabyBumps-1sjxe4b | haircut question |
| 030 | pregnant-1sk3wgz | relationship suspicion; nothing for niche |
| 030 | BabyBumps-1sk51a0 | illness at 38 weeks, medical |
| 030 | PregnancyUK-1sk7f1f | swollen ring question |
| 031 | pregnant-1skjzk9 | induction for a medical reason with severe health-anxiety wording |
| 031 | pregnant-1skcq7g | cat waking her; nothing for niche beyond insomnia |
| 031 | pregnant-1skdo3u | surprise-shower etiquette |
| 031 | pregnant-1skhky4 | symptom-easing worry, thin |
| 031 | pregnant-1skihfl | early bloating question |

## Flagged

| chunk | unit | note |
|---|---|---|
| 026 | BabyBumps-1shvfzr | engagement-bait style prompt, possibly AI-written; not quoted |
| 027 | pregnant-1sim7ot | new account, spontaneous triplets; possibly embellished; not quoted |
| 028 | pregnant-1siwrbd | 'unpopular opinion' framing, possible engagement bait; quoted as one voice |

## Crossposts

| chunk | unit | note |
|---|---|---|
| 025 | pregnant-1shmn7g | same author/text as BabyBumps-1shnat6; quoted once per reply |
| 026 | pregnant-1shys7b | same author/text as PregnancyUK-1shtnyi; quoted once |
