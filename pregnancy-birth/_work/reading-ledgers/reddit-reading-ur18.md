# UR18 — excluded-post reread

Build: Mamivio — Pregnancy, birth preparation and the first weeks. Reading date: 2026-11-16.

Assignment: `scratchpad/unfilter-reread/assign-ur18.tsv`. Output: `voice/reddit-ur18.jsonl`. All 297 assigned rows were read in full: 62 frozen units (including every archived original-poster reply in each unit) and 235 fallback posts decoded from the subreddit `.posts.jsonl` archives. No text was missing. Fallback reading covers the saved post, not replies absent from that file.

Counts: **297 rows assigned; 297 read; 0 not found; 293 rows quoted; 363 quotes written; 363 quotes verified; 0 verification failures.** Four rows have no new quote: three are off-niche and one is an identical crosspost already quoted in this output. Most of the assignment was on-niche; it was not mostly unrelated material. Later-posted accounts were kept where they explicitly describe pregnancy, birth or recovery, rather than rejected merely for the child's current age.

Every quote was verified as an exact contiguous substring of its cited unit or the matching post's decoded `title`/`selftext`, with date and comment provenance checked. The repository verifier was also run with archive decoding supplied in memory: `TOTAL 363 quotes, 0 failed`. No raw files or tools were changed. There are 88 unit quotes and 275 archive quotes; ids are unique and context fields are at most 16 whitespace-separated words.

Ids run from `pbu18-0001` through `pbu18-0364`, with `pbu18-0197` reserved and omitted after crosspost deduplication; it was not reassigned. The final duplicate check compared against 26,078 then-readable records in other voice files and found no exact/contained passage overlap of 55 or more characters. Other readers were active, so this describes the check snapshot. Known pre-existing same-post passages were checked directly, including shorter records. Different passages from the same author or crosspost remain one voice, not independent corroboration.

Only the two assigned output files were written. No network or git was used. Source claims about treatment, risk, law and outcomes are recorded as the speaker's account; the observations below do not validate those claims.

## Assigned-row ledger

| Assignment id | Quotes | Reading result |
|---|---:|---|
| BabyBumps-1sb0v4d | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1setiq1 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1sj5psp | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1slscti | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1sr8ur0 | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1sv80mi | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1syygvd | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1t390uq | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1t6rzob | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1tazk0u | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1telyjj | 1 | Read in full; hospital-admission passage added; pb63-0128–0131 not repeated. |
| BabyBumps-1tir0pv | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1tm5ix9 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1tpll5r | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1ttge3q | 1 | Read in full; tea question added; itching/ER passage already pbu14-0224 in crosspost pregnant-1ttgctc. |
| BabyBumps-1twri45 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1u0v5mg | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1u5apdr | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1u7pefa | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1ucgkit | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1uguh72 | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1ulmn1n | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1uq5yjy | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1uvndgz | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1v0mwol | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1v6f617 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1vb4int | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1vgzi9l | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1vmev57 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1vs9vc2 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1vwilws | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1w11htr | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1w7sutd | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1wf7me3 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1wnbj09 | 2 | Read in full; new quote(s) extracted. |
| BabyBumps-1wtsxk7 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1x19b77 | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1x7wmid | 1 | Read in full; new quote(s) extracted. |
| BabyBumps-1xdc36d | 3 | Read in full; new quote(s) extracted. |
| FirstTimeMom-1t2nu5o | 1 | Read in full; new quote(s) extracted. |
| FirstTimeMom-1vfpxcp | 1 | Read in full; new quote(s) extracted. |
| Mommit-1sekr60 | 2 | Read in full; new quote(s) extracted. |
| Mommit-1ss49kr | 0 | Off-niche: medical and custody dispute about a one-year-old; no pregnancy, birth-preparation or first-weeks experience is developed. |
| Mommit-1t6cmtk | 1 | Read in full; new quote(s) extracted. |
| Mommit-1th61l5 | 1 | Read in full; new quote(s) extracted. |
| Mommit-1tvnrfa | 1 | Read in full; new quote(s) extracted. |
| Mommit-1u996vz | 0 | Off-niche: possible neglect and support needs of an eleven-and-a-half-month-old. |
| Mommit-1ulj9nd | 1 | Read in full; new quote(s) extracted. |
| Mommit-1uzf10b | 1 | Read in full; new quote(s) extracted. |
| Mommit-1v90abj | 1 | Read in full; new quote(s) extracted. |
| Mommit-1vltryj | 1 | Read in full; new quote(s) extracted. |
| Mommit-1w1c083 | 0 | Off-niche: disagreement about future toddler tantrum discipline; pregnancy is incidental. |
| Mommit-1wkxzu3 | 2 | Read in full; new quote(s) extracted. |
| Mommit-1wy5f9b | 1 | Read in full; new quote(s) extracted. |
| Mommit-1xc31h9 | 1 | Read in full; new quote(s) extracted. |
| NewParents-1sp8min | 1 | Read in full; new quote(s) extracted. |
| NewParents-1tdu8lv | 1 | Read in full; pregnancy/nursing history added; bleeding passage already pbu09-0061 in crosspost Mommit-1tdu1v6. |
| NewParents-1u7d1vy | 1 | Read in full; new quote(s) extracted. |
| NewParents-1v4oaqm | 1 | Read in full; new quote(s) extracted. |
| NewParents-1vq9l0f | 1 | Read in full; new quote(s) extracted. |
| NewParents-1wlqlqr | 2 | Read in full; new quote(s) extracted. |
| PregnancyUK-1sblldh | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1sjhxr7 | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1stk83t | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1t4bn9m | 2 | Read in full; new quote(s) extracted. |
| PregnancyUK-1tggwte | 2 | Read in full; loss history and repair costs added; pb63-0244 not repeated. |
| PregnancyUK-1tsag53 | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1u1d037 | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1uclc0s | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1un2v4a | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1ux8q2h | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1v5n5cp | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1vg4k2g | 3 | Read in full; new quote(s) extracted. |
| PregnancyUK-1vpbhp8 | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1vzyf9r | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1wbtnv6 | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1wnfdv1 | 2 | Read in full; new quote(s) extracted. |
| PregnancyUK-1wxcsto | 1 | Read in full; new quote(s) extracted. |
| PregnancyUK-1x6oxnv | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1sbyf3f | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1smzad9 | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1t0w8sf | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1tazkh2 | 2 | Read in full; new quote(s) extracted. |
| beyondthebump-1tqfbah | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1u2norr | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1ueooy2 | 2 | Read in full; new quote(s) extracted. |
| beyondthebump-1us12ce | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1v5hlug | 3 | Read in full; injury, treatment and recovery passages added; pb25-0124–0127 not repeated. |
| beyondthebump-1vimm4g | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1vse7sy | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1w6gnz9 | 1 | Read in full; new quote(s) extracted. |
| beyondthebump-1wmizse | 3 | Read in full; new quote(s) extracted. |
| beyondthebump-1wy30dt | 0 | nothing new beyond existing quotes: identical crosspost of Mommit-1wy5f9b, quoted in this file as pbu18-0064. |
| beyondthebumpUK-1sa83vn | 2 | Read in full; new quote(s) extracted. |
| beyondthebumpUK-1uk0284 | 1 | Read in full; new quote(s) extracted. |
| beyondthebumpUK-1w67ssc | 1 | Read in full; new quote(s) extracted. |
| daddit-1sdwug1 | 1 | Read in full; new quote(s) extracted. |
| daddit-1tfmdzy | 2 | Read in full; new quote(s) extracted. |
| daddit-1ubzyxq | 1 | Read in full; new quote(s) extracted. |
| daddit-1vdnh5z | 1 | Read in full; new quote(s) extracted. |
| daddit-1wb0uve | 1 | Read in full; new quote(s) extracted. |
| pregnant-1s969f0 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1s9zu8n | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sasj8f | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sbr3dk | 1 | Read in full; new quote(s) extracted. |
| pregnant-1scptm9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sdieux | 2 | Read in full; new quote(s) extracted. |
| pregnant-1seiuu5 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sfnndg | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sggo9l | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sh65uh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1shzflm | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sis7ji | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sjszwh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1skk0ho | 1 | Read in full; new quote(s) extracted. |
| pregnant-1slgf5u | 1 | Read in full; new quote(s) extracted. |
| pregnant-1smcyn3 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1sn8st3 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1so6s4q | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sp6cqd | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sqbajl | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sr3va4 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1srwnfh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ssqxkl | 1 | Read in full; new quote(s) extracted. |
| pregnant-1stinrj | 1 | Read in full; new quote(s) extracted. |
| pregnant-1su4khv | 1 | Read in full; new quote(s) extracted. |
| pregnant-1suyftw | 2 | Read in full; new quote(s) extracted. |
| pregnant-1svsxbi | 1 | Read in full; new quote(s) extracted. |
| pregnant-1swpb27 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sxl69a | 1 | Read in full; new quote(s) extracted. |
| pregnant-1sycame | 1 | Read in full; new quote(s) extracted. |
| pregnant-1szaaxe | 2 | Read in full; new quote(s) extracted. |
| pregnant-1t09fdw | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t151xq | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t23j1w | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t2yb4f | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t3uqpi | 2 | Read in full; new quote(s) extracted. |
| pregnant-1t4z006 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t5pkw5 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t6tajv | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t7t2u8 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1t98r7y | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ta6r1r | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tb6zvf | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tc35h2 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tct119 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tdw9cs | 1 | Read in full; new quote(s) extracted. |
| pregnant-1teukmr | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tfqxx1 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1th0z0y | 1 | Read in full; prior loss and new regimen added; recurrence-fear passage already pbu02-0016 in BabyBumps-1th0zfe. |
| pregnant-1ti0yrf | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tivdtp | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tjwziz | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tksyi7 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tlwdyy | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tmv8sj | 1 | Read in full; new quote(s) extracted. |
| pregnant-1to4b5t | 1 | Read in full; new quote(s) extracted. |
| pregnant-1toygso | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tpmuz6 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1tqetbu | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tr85n9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ts2hpr | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tsohun | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ttjmn9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tue5tv | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tvaw84 | 1 | Read in full; body image/work incapacity added; symptom list, remedies and exercise passage already pbu01-0033–0035 in BabyBumps-1tvay39. |
| pregnant-1tw28rp | 1 | Read in full; new quote(s) extracted. |
| pregnant-1twy1lf | 1 | Read in full; new quote(s) extracted. |
| pregnant-1txullc | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tylvo0 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1tzs4o5 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u0hu2h | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u19bak | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u21f2a | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u2ury2 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u3yhaj | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u52nvi | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u6itul | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u78nok | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u7uegb | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u8n3oh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1u9noo9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uala1c | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ubigcz | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ucnpzx | 1 | Read in full; new quote(s) extracted. |
| pregnant-1udjumc | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ueivcu | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ufbb4p | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ug6cnj | 2 | Read in full; new quote(s) extracted. |
| pregnant-1uh41x9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ui4p9p | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uj8l1a | 3 | Read in full; new quote(s) extracted. |
| pregnant-1uk2ueg | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ukt8wl | 2 | Read in full; new quote(s) extracted. |
| pregnant-1ulqniy | 1 | Read in full; new quote(s) extracted. |
| pregnant-1umivw5 | 19 | Read in full; new quote(s) extracted. |
| pregnant-1und4ru | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uo7j4n | 1 | Read in full; new quote(s) extracted. |
| pregnant-1up0c4e | 1 | Read in full; new quote(s) extracted. |
| pregnant-1upotuw | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uqchr6 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ur2a5a | 1 | Read in full; new quote(s) extracted. |
| pregnant-1urph6a | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ussgku | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uu25hh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uuzpek | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uvovu1 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uwd6b3 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1ux98t1 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uy8qnk | 1 | Read in full; new quote(s) extracted. |
| pregnant-1uz3lrm | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v06olg | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v133w9 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v23aus | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v31aoz | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v42d5l | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v4vxak | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v632ht | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v7bhed | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v8k9no | 1 | Read in full; new quote(s) extracted. |
| pregnant-1v9by6v | 1 | Read in full; new quote(s) extracted. |
| pregnant-1va7dus | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vb4i5t | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vc305u | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vd8txp | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vegw0c | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vfmtb4 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vglz3t | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vhfsv3 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vidl2v | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vj9ile | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vkan3w | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vlc4q3 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vmjq45 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vnca6d | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vob8nl | 2 | Read in full; new quote(s) extracted. |
| pregnant-1vpg66a | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vqeazh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vr9b0r | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vs4aqx | 2 | Read in full; new quote(s) extracted. |
| pregnant-1vt4bfi | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vua3ak | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vv49nh | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vw342i | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vx8nlo | 2 | Read in full; childcare burnout detail and loss reply added; pb45-0238–0239 from BabyBumps-1vx88tb not repeated. |
| pregnant-1vycgay | 1 | Read in full; new quote(s) extracted. |
| pregnant-1vz5llx | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w02u7z | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w12ys4 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w1tuwf | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w2y3ux | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w4dspg | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w5k1xe | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w6p0e2 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1w7q8pa | 1 | Read in full; new quote(s) extracted. |
| pregnant-1w99sl0 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wa4ebj | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wb3tvm | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wc19qm | 3 | Read in full; new quote(s) extracted. |
| pregnant-1wcykog | 1 | Read in full; new quote(s) extracted. |
| pregnant-1we1gas | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wf8bxs | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wgg6t0 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wh836e | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wi644d | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wj9qkc | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wkluya | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wlow15 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1wmkm05 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wnc0q5 | 2 | Read in full; diagnosis/medication passages added; pb13-0098–0100 not repeated. |
| pregnant-1wo7n7d | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wp5ucc | 2 | Read in full; new quote(s) extracted. |
| pregnant-1wq4j3g | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wr7kgl | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wso8un | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wtl7j0 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wudn5p | 2 | Read in full; new quote(s) extracted. |
| pregnant-1wv8zzb | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wwb656 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wxixks | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wyh5dj | 1 | Read in full; new quote(s) extracted. |
| pregnant-1wz7k6f | 2 | Read in full; new quote(s) extracted. |
| pregnant-1x05a5z | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x0zfyz | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x1orsi | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x344jo | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x4inkd | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x5ir4t | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x6t4nu | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x7y813 | 1 | Read in full; sobriety/friends passage added; pb20-0094–0098 not repeated. |
| pregnant-1x8rk49 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1x9jmuw | 1 | Read in full; new quote(s) extracted. |
| pregnant-1xa7wzi | 2 | Read in full; new quote(s) extracted. |
| pregnant-1xb3pa4 | 1 | Read in full; new quote(s) extracted. |
| pregnant-1xc1pl6 | 2 | Read in full; new quote(s) extracted. |
| pregnant-1xcxzby | 1 | Read in full; new quote(s) extracted. |
| pregnant-1xdxrt8 | 1 | Read in full; new quote(s) extracted. |

## What these posts add

These are additions to or qualifications of `synthesis/findings.md` as read on 2026-11-16, especially §§2, 5–6, 9–10 and 17. The restored findings already acknowledge pain, care failures, anxiety, mental health and recovery. The points below name mechanisms and contrary cases the surviving-quote restoration did not establish. They are observations from this assigned set, not prevalence estimates or evidence of willingness to buy the proposed guide.

1. **Control over whether pregnancy continues is a missing part of the partner picture.** §17.7 acknowledges that the earlier rule removed these accounts, but the ordinary partner/task-list interpretation still lacks their words. One author reports being effectively kept under house arrest until an abortion window closed [pbu18-0042]; another agrees to an abortion after an angry partner's threats and withdrawal of comfort [pbu18-0199]. Another describes forced substance use, abortion, strangling and subsequent pregnancies [pbu18-0353]. Pressure to continue and pressure to terminate both appear. A cooperative partner cannot be assumed simply because someone is married, housed or financially stable; practical preparation cannot explain these situations away.

2. **Deciding whether to continue can be about resources and incompatible futures even when attachment is present.** Potential redundancy and homelessness make one parent feel the decision has been taken away [pbu18-0147]. A single professional describes maternal pressure, no maternity leave, childcare costs and anticipatory grief over an abortion she cannot emotionally settle on [pbu18-0274]. Another describes interrupting an abortion attempt, feeling relief at a continuing pregnancy, then renewed doubt about an unhealthy relationship and lost career opportunities [pbu18-0263]. This extends §8 beyond bills influencing birth timing: resources and relationships also shape whether there will be a birth to prepare for.

3. **After loss, announcement is a conflict between support, privacy and emotional labor.** Early disclosure gave one couple support, but repeating bad news traumatized the partner; now his wish to wait conflicts with visible symptoms and her leadership role at work [pbu18-0005, pbu18-0006]. Another parent would tell fewer people next time because responding to well-meant reactions became work [pbu18-0088]. A physician husband refuses to discuss a new pregnancy until the second trimester [pbu18-0208]. One author hides pregnancy even from her partner and delays booking a doctor because she fears hurting them again [pbu18-0325]. The disclosure problem is wider than employer timing.

4. **Pregnancy number, living children and loss history are different dimensions.** A mother explicitly wants space to celebrate the current baby, grieve the last, and give attention to her living child [pbu18-0351]. Another is grieving one twin while still pregnant with the other, and dreads every scan [pbu18-0275]. A new pregnancy can follow neonatal death and a cesarean [pbu18-0180], or recurrent miscarriage and the partner's suicide, including missing his funeral because of D&C complications [pbu18-0346, pbu18-0347]. §9's first/second/third-pregnancy split needs these distinctions; an apparently experienced parent may never have brought a baby home.

5. **The reassurance loop has observable costs and choices.** §6 already describes the loop; these posts show scans every fortnight helping for only days, long therapy waits and failed distraction/breathing attempts [pbu18-0128]. Blood-pressure checking escalates from once or twice daily to five or six times, with the author recognizing that it creates more stress [pbu18-0289]. Repeat testing can be consciously reduced next time [pbu18-0088]. Reassurance is also sometimes effective: an anatomy scan restores hope and permits planning after loss [pbu18-0261], and a follow-up reply reports a heartbeat after an anxious initial post [pbu18-0334, pbu18-0335]. These are different outcomes of reassurance, rather than a universal claim that scans help or worsen anxiety.

6. **Medication fear can remove the capacity that pregnancy requires.** An author stops citalopram without first asking a doctor, develops withdrawal and returning depression, then faces a partner who calls her a bad mother and threatens lifelong blame even after hearing the doctor's approval [pbu18-0317, pbu18-0318]. Another receives repeated, directly opposing instructions from her OB and psychiatrist [pbu18-0342]. Feeling dismissed precedes self-started progesterone in another account [pbu18-0218]. A positive test on the day of ADHD diagnosis postpones intended treatment, although the diagnosis itself helps the author understand herself [pbu18-0331, pbu18-0332]. This sharpens “care navigation” into conflicting authorities, feared harm and actual lost functioning.

7. **Physical severity and mental capacity do not move together.** The type-one-diabetes author feels demoralized by exceptionally tight targets despite sustained effort [pbu18-0152]. Another describes mild physical symptoms but capacity for almost nothing, productivity guilt and renewed body distress after loss [pbu18-0277]. Prior HG does not secure proactive help; the response that every pregnancy is different feels dismissive precisely because all three pregnancies have had HG [pbu18-0270]. Severe symptoms can also make prescribed treatment impractical: a sole earner cannot easily afford repeated hour-long trips for infusions [pbu18-0153, pbu18-0154]. §17.2's work focus is supported, with more detail about whose account of incapacity is believed.

8. **A preparation failure can be a mismatch with profound incapacity rather than a promise of control.** One detailed author read more than ten recommended pregnancy/birth books, made notes and expanded a plan, yet says none applied to her or her child [pbu18-0249]. Her account specifies why: pain made movement and travel impossible [pbu18-0236, pbu18-0237]; injury prevented carrying or bending, making an adjustable bedside crib essential [pbu18-0242]; a strong willing partner could not manage both injured mother and newborn, so scattered practical help and everything within reach mattered [pbu18-0244]. This adds to §§4 and 10 beyond hypnobirthing outcome promises. All of these records are one author's experience, and her proposed fixes remain her advice.

9. **Feeding can determine medication, sleep and recovery choices.** After ICU care, a mother reports having to pump from regaining consciousness despite good supply and latch, with both continuing and stopping involving suffering [pbu18-0240]. Another says ending pumping and resuming pre-pregnancy medication improved her patience, fatigue and ability to engage with the baby [pbu18-0105]. A newborn-screen result makes apparently successful breastfeeding feel like possibly poisoning the baby, while the author is unsure whether to preserve supply pending retesting [pbu18-0097]. These are sharper conflicts than “feeding pressure” alone.

10. **A free sleep shift does not necessarily produce sleep, and distress can begin immediately.** At four weeks one parent cannot sleep even when her husband takes the baby, hears crying through the small house, and is offered a GP appointment seventeen days away [pbu18-0115, pbu18-0116]. Another describes four hospital nights of severe anxiety after induction and cesarean, unable to sleep even with staff-created time because of panic and anticipated pumping demands [pbu18-0322]. The “six months” triage label on two identical Zoloft posts referred to a proposed treatment duration: the author was thirteen days postpartum, squarely in the first two weeks [pbu18-0064]. The mirrored beyondthebump row is counted once.

11. **The partner's emotional burden and later improvement need their own account.** One father says he is already doing household work and childcare while becoming the target of hurtful outbursts; more task allocation does not describe the problem he is asking about [pbu18-0120]. Months later he returns to report improvement with medication and a more manageable routine [pbu18-0121]. Other accounts complicate the assumption that the pregnant parent is always the recipient of aggression: one author describes shoving her husband and throwing a cup, takes responsibility, and asks whether the change improves after delivery [pbu18-0252]. These add specifics to §5's other-side voice without equating every relationship conflict.

12. **Trust depends on consent, explanation and the practical ability to obtain care.** A survivor anticipating a cesarean asks for essential staff only, introductions, explanations, consent, a quiet room and her partner present; she also wants arrangements that let her see and hold the baby [pbu18-0225, pbu18-0226, pbu18-0227]. Another describes an unexplained early scan and rapid scheduling of D&C after pregnancy was discovered during preparation for another procedure [pbu18-0328, pbu18-0329]. An induction conversation undermines trust when a provider invokes doubled stillbirth risk but cannot quantify it [pbu18-0306]. Insurance excluding dependent pregnancy leaves a different author without prenatal continuity despite emergency visits [pbu18-0291]. Generic contacts or advocacy scripts only partly describe these gaps.

13. **Some apparently available support constrains rather than helps.** A disabled mother depends on the partner she fears for appointment transport and anticipated cesarean recovery help [pbu18-0082]. Another expects safety boundaries around a relative's newborn diaper comments to be contested, while housing scarcity keeps the family living with that relative [pbu18-0062, pbu18-0063]. A first-time parent finds relatives interested in baby information but not her, unclear gifts and unwanted disclosure, and cancels a shower because of isolation [pbu18-0361, pbu18-0362]. This develops the existing visitor-boundary finding into dependence, privacy and inaccessible alternatives.

14. **There is meaningful contrary evidence to expected repetition of trauma.** A mother describes a much easier second pregnancy, birth and bonding experience, then guilt when her mother treats that enjoyment as replacing the older child [pbu18-0109]. Forceps injury, stitch allergy and failed epidural are followed by treatment, physical therapy, therapy and reported recovery [pbu18-0106, pbu18-0107, pbu18-0108]. Another author describes remote work, family support and cerclage followed by an emergency cesarean and joy three days postpartum after prior loss [pbu18-0358, pbu18-0359]. Unexpected maternal acceptance also turns fear into excitement in an unplanned pregnancy [pbu18-0313]. Difficult histories do not establish inevitable recurrence or inevitable ambivalence.

15. **The former intake flags also removed mundane pregnancy language.** The assignment's “I am 16” hit is an author at 16+3 describing a cat kneading the bump [pbu18-0001]. “13m” refers to a nursing toddler while the author is newly pregnant again [pbu18-0012]. Other flagged posts ask about fasting nausea during glucose screening [pbu18-0083] or bra sizing at fifteen weeks [pbu18-0167]. These source texts show collateral loss beyond the topics the filter purported to identify.

**Commercial evidence and limits.** A partner/app founder says existing tracking tools required several apps plus paper and attributes improved management to his own tool [pbu18-0293]. This is explicitly a promotional founder account, not independent buyer demand or proof that an app caused improvement. The detailed book-failure account names a quantity read, not a price paid [pbu18-0249]. No quote here establishes purchase or valuation of the proposed Mamivio guide.

**Vocabulary outside the README seed list used in this file.** `breastfeeding_in_pregnancy`, `care_navigation`, `child_safety`, `family_expectations`, `feeding_pressure`, `financial_dependence`, `housing_constraints`, `medication_in_pregnancy`, `pregnancy_ambivalence`, `pregnancy_anxiety`, `pregnancy_loss`, `pregnancy_mental_health`, `pregnancy_symptoms`, `reproductive_coercion`, `substance_use`. These are descriptive tags; some already occur elsewhere in the build. They are recorded here because this assignment permits only the voice file and this ledger.

**Source language worth retaining.** “human leaflet” for unhelpful professional reassurance [pbu18-0116]; “Hard Mode birth and PP” [pbu18-0232]; “patchwork of people” [pbu18-0244]; “This new baby deserves my excitement.” and “My last baby deserves my grief.” [pbu18-0351]; “incubator at best” [pbu18-0362]. The last expression is quoted within its full original passage in the voice file.
