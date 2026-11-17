# Independent semantic/context audit of twenty frozen records

Auditor: reader 01, after completing and freezing own 01 outputs. Fixed seed `2026102405`; two random records per frozen other-reader file 02/03/04/05/B, plus ten random remaining records. Own 01 and unfinished 06/07 excluded. Every full sampled quote/context/metadata record and both intact full source views were manually read, including all eight available identifiable OP replies. This is a finite stratified sample, not the whole continuation or a population estimate.

Results against the frozen sample: **20 checked; 19 supported as written; 1 minor context correction identified; 0 literal, speaker, stage, transaction-attribution or new safety failures; 0 auditor voice edits.** Root has applied the one correction, leaving **0 unresolved findings**. Per-ID decisions and qualifications are in `results.jsonl`.

`rad05-0028`: the source establishes a ten-month-old eating varied solids well, but does not establish general clinical health. Remove the unsupported word “Healthy”. Proposed replacement: “Parent of a ten-month-old who eats varied solids needs hotel-trip meal access. Sodium limits and nutrition prescriptions are outside selected use.” The quote, age and practical meal-access selection remain supported. This is a wording correction, not evidence that the child is unwell.

Root's applied correction is recorded in [parent-metadata-corrections-05.json](../parent-metadata-corrections-05.json). The current reader-05 context was checked against that log and contains no general-health assertion. Frozen sample/context files remain unchanged, preserving the wording that triggered the finding.

The other records preserve conditional affordability versus buying, prior gear purchase versus current consideration, free/nontracking successes, mixed paid-app experiences, provider and benefit dependencies, infant current age versus future handoff age, and qualified-care boundaries. Three sample records already carry research-only restrictions, which are appropriate. No sampled post centers an acute crisis, abuse, loss/death or minor author; the incidental teenage traveler in `rad05-0005` does not turn its airline allowance question into minor-centered material. No independent-buyer total or corpus-wide duplicate clearance was inferred.

No exact parent comment needed additional inspection for the selected claims. Newly read auxiliary comments: **0**. The eight supplied OP replies are context reinspection only and must not be added again to aggregate source coverage. Native byte/date/URL audits are root's separate check; the hashes here fix what was inspected. Rights, author authenticity, self-report truth, live completeness, clinical efficacy and policy currency remain unverified. No sources fetched, outgoing messages or extraction appenders rerun.

Frozen sample SHA-256: `b190434eb0d69f8513c71219b3e3764b99448b9d1b797f2bf0af3a8d248ed8e5`.
Frozen context manifest SHA-256: `52359e95344d6ce9034828780aeb0d20e7a36b0947541c86819a6609e2c569eb`.

| Full view | SHA-256 |
| --- | --- |
| `_raw/audit/continuation-2026-10-24/independent-semantic20/contexts-01.txt` | `f962d260f712b89e57fdc7a72525c34b266a6140b39ffc97bbc8225c967c0581` |
| `_raw/audit/continuation-2026-10-24/independent-semantic20/contexts-02.txt` | `098502190dad23a0fa3d9c5285afbb8c8a2c060af1fb2ee3b6363d56a56df440` |

| Inspected individual source | SHA-256 |
| --- | --- |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1obm3qs.txt` | `a178e4d2eeacc8b3caa1f98dfb67347d16164fdc1aeb21343403817f046e57ca` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/BabyBumpsCanada-1orbhb0.txt` | `81286c57decfdf9fbee10667d9737994d980e12d9f1482ef706621dc003dbea7` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1mx3fm6.txt` | `50361a0fc2a8a3fe46f06d4a8933028e75627877715912e43013859f7b6671c2` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/BabyBumps-1nfi952.txt` | `0d52e59994a942ff57c80c84af76c22fdac374fda937ec80d6298c3533f733c8` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1oq26bh.txt` | `859b03858ead15efc5dd9fca0a14d618a74e26ea2499455c4bf09a271f2b4d81` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1ophayc.txt` | `b1b1b87ee5eca99d2fc92f1b912ae4e749d49d02e43c908d33e930f9caadaa5f` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/beyondthebump-1n6q92l.txt` | `75b0380368a7cfdba8d2283628904d7f16e288e4b055ce751b42e2aebf1cc845` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/beyondthebump-1pjqmcq.txt` | `becffa8d3046605d4013fec046b59f21eef67b44ac521c08d8adeb014551196b` |
| `_raw/reddit-deep/july-B-solids-v1/primary-units/BabyLedWeaning-1m1ez71.txt` | `e668f7b02ecfda6039cea836f7f300e596b5aa084dc76decd0f15da80f8e8926` |
| `_raw/reddit-deep/july-B-solids-v1/primary-units/BabyLedWeaning-1lzqlgx.txt` | `ae89d702e26120c82b11f9a0c2c5d0447b1d38aa347f0e288d2d4e1e51420a49` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/BabyLedWeaning-1q0d6qh.txt` | `df9263368ef6ff8d8824fc01416ded638b2515754490e0ac13ba583561745e1a` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/ExclusivelyPumping-1mf67l2.txt` | `5c3c778d7c98789e3f58ba677a399af26ec060adb368e37587cf7293ca8b796c` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/BabyBumps-1nc3vo2.txt` | `b4c8823e46b6d9e263d0b352ae6fe7e60e966828b7954bce5c7104452a7b0563` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1n2nhso.txt` | `a1ecc7f0164614e192999a3377f5d15cf1c40b7699c9365c5e9ba952d6f1c828` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/beyondthebump-1nid2y8.txt` | `7b7893173dcbe4923f084c1b99d7e8073beba82187c71c17ca003ea8a043fe26` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/BabyLedWeaning-1o9atg9.txt` | `480967b5df0d23dd8cff35ddfdb51efcb15b0180e10196adbfde3408b487cc85` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/workingmoms-1ow5lkr.txt` | `fcfbd407dc3ca56459a24926e1db15f3a4329be9e85ad13a6851179b9ec84cdf` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/beyondthebump-1pmypd8.txt` | `71968571b6d13bcfcc31733fa2b71c1fcaf241ef516d31690ced30c7753a9f74` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/NewParents-1mkb7mm.txt` | `941c15df8203560d0fb2b43b8f2e41b63add1c8df2d489e19469db3908ac056a` |
| `_raw/reddit-deep/aug-dec-2025-wave-v1/primary-units/ExclusivelyPumping-1of0mrj.txt` | `90bbc908df6805b0d78f432efc443b815f05fcb59ef02e94ddfcd308665431d1` |
