# Advertiser continuation — session ledger and audit

Completed October 25, 2026, Europe/Vilnius. [Commercial answer across seven contenders](advertiser-money-map.md) · [Complete Page census](../ads-running/census-2026-10-25.md).

The owner asked which main players actually advertise in each shortlisted niche. Root followed the supplied Chrome MCP startup document, confirmed the configured 9225 endpoint and drove a dedicated visible browser tab. Three reused readers mapped current official offers and fully read retained text; a fresh independent reader audited the interpretation. The browser was not shared with those readers. No product work, accounts, payment, outreach or advertising campaigns occurred.

## Exact advertiser reading ledger

| Source / finite scope | Captured or prepared | Matched / retained native IDs | Kept | Fully text-read | New voice quotes |
|---|---|---:|---:|---:|---:|
| Sleep/play advertiser Pages |7 positive Page captures |199 |199 |199 |0 |
| Food/safety/broader meal planners |7 positive Page captures |149 |149 |149 |0 |
| Leave/registry/household coordination |10 positive Page captures |141 |141 |141 |0 |
| Good Inside and selected First Step discovery |1 positive Page +2 discovery captures;24 selected occurrences |22 distinct |22 |22 |0 |
| Happy Eaters/My Little Eater |2 positive Pages +1 discovery capture;42 selected occurrences |33 distinct |33 |33 |0 |
| Root babyproofing-retail reading |2 positive Page captures |60 |60 |60 |0 |
| Other named advertiser Pages |14 correctly resolved zero-result captures |0 |0 |0 |0 |

These rows cover **43 valid distinct named Pages:29 with active results and 14 zero**. The Page sources supply **603 distinct loaded native IDs**; one separately selected First Step instructor-training ad makes **604 unique IDs fully read**. All kept texts are complete; none remains unread. Across sources,615 native reading occurrences were checked, including two Good Inside and nine food discovery/Page duplicates. Those repeats add no unique-ad credit. Images, video/audio and alternate variants remain unviewed.

Root made 47 captured Page attempts: four are explicitly excluded and preserved as superseded identity/SPA captures008,013,017,047. The 43 valid captures govern the census. There are also 47 saved UI-lookup records, seven selection-provenance records and 16 initial keyword/category discovery captures with 431 native record occurrences. No broad keyword count is attributed to a particular brand. [All query/lookup/selection records](../sources/advertiser-wave04-query-ledger.jsonl) · [valid Page rows](../sources/advertiser-wave04-page-census.jsonl).

## Current offer/price source work

These additional primary sources establish advertised supply, not buyer payments or ad-attributed revenue. Counts describe saved responses/inspected text, with shells/denials separate; client assets are not additional sales pages. Official store catalogs are not tested account paywalls.

| Source packet | Requests / retained scope | Completed inspection and boundary | Source note |
|---|---|---|---|
| Sleep/play |14 robots +21 offer/store/client responses | Current official prices, app catalog variants and Little Ones' written-plan/human bundle; Wonder Weeks direct homepage403; Baby Sleep Answers current shell |[Offer map](reader-notes-advertiser-map04-sleep-play.md) |
| Food/safety |33 permitted HTTP200 primary pages | Current offers, prices, site-linked identities and three separately labeled physical meal firms; guessed TLS/DNS failures not bypassed |[Offer map](reader-notes-advertiser-map04-food-safety.md) |
| Broader family meal planners |6 HTTP200 captures plus a separately saved primary rendered eMeals cost article | eMeals/Plan to Eat pricing; Mealime's closure; native cost-page shell does not pretend to contain rendered prices |[Offer map](reader-notes-advertiser-map04-food-planners.md) |
| Leave/registry/household software |28 target responses +24 policy responses |26 complete saved HTML texts, one MyMatLeave shell, one Tilt403; current pricing plus clearly dated reused consultancy offers |[Offer map](reader-notes-advertiser-map04-leave-registry.md) |
| Good Inside/First Step |4 robots +9 offer/client/price HTTP200 responses | Exact USD 175 base bundle price and human-session terms; First Step professional training's EUR 500 registration fee is not full tuition |[Direct discovery](reader-notes-advertiser04-direct-discovery.md) |
| Happy Eaters/My Little Eater |3 HTTP200 official offer/store captures +1 failed TLS policy probe | US app catalog variants; current USD 39.99 fixed downloadable plan/85 course bundle; no Happy Eaters homepage fetched after failed probe |[Meal-guide follow-up](reader-notes-advertiser04-meal-guides.md) |

No new review/buyer observations or voice quotations arise from these maps. Seller credentials, efficacy, safety, savings, testimonials and personalization functions were not tested. The prior **2,162 quotes,1,144 bank IDs and 141 research-only records** remain unchanged.

## Verification

The [independent native/coverage audit](../_raw/advertiser-census-wave04-2026-10-25/audit/native-and-coverage-verification.json) joins all six reading ledgers to original browser records: exact native IDs, outer advertiser Page, active flag, source hashes and own-body hashes across 615 occurrences. The 603-ID Page set is complete in the reading union; the only additional ID is the explicitly selected instructor-training discovery. There are **0 retained unread IDs,0 duplicate reading IDs and0 final machine failures**. All 46 committed voice-file hashes and 43 prior frozen voice/inventory hashes are unchanged. No source file reaches100 MB.

Reader-specific audits additionally check supplied cards, text-field bundles, native dates/destinations, immutable views and creator/partner identity. Root read all 119 distinct safety-copy field strings and the 60 native-ID field maps; exact repeated strings were presented once with SHA256 equality. Full per-ID ledgers: [sleep/play](../sources/advertiser04-sleep-play-reading.jsonl), [food/safety](../sources/advertiser04-food-safety-reading.jsonl), [coordination/registry](../sources/advertiser04-coordination-registry-reading.jsonl), [direct discovery](../sources/advertiser04-direct-discovery-reading.jsonl), [meal guides](../sources/advertiser04-meal-guides-reading.jsonl), [root safety](../sources/advertiser04-root-safety-reading.jsonl).

An independent reader saved a reproducible seed2026102504 sample before inspection:20 stratified random ads plus five targeted cases,23 distinct IDs and 28 supplied cards. Every sampled full native body/card/headline/CTA/destination and classification was checked; the money map was read in full. **No material interpretation errors were found within that sample.** Master private-support ads were not assigned the separate USD997 Blueprint price; Nugget's webinar and membership were separated; brand-wide Babylist counts remained brand-wide; Good Inside's human session/ownership limit was preserved; Safetots' advice was correctly free. [Audit note](../scratchpad/advertiser04-independent-audit/audit-note.md) · [audit JSON](../scratchpad/advertiser04-independent-audit/audit.json).

Earlier 68 ad-body reads overlap 48 of this wave's 604 IDs, giving **624 cumulative distinct IDs with completed visible-body reading**. The prior 63-body TSV is hash-verified; the five later query-text reads are also verified natively in this wave. This cumulative body metric does not upgrade earlier media/card coverage or count 624 unique creative concepts.

Whole voice-source verification is preserved in `../_raw/advertiser-census-wave04-2026-10-25/audit/whole-quote-verification.txt`:

```text
TOTAL 2162 quotes, 0 failed
```

The query hashes and source-count derivation are reproducible with `_tools/derive_advertiser_wave04.py` and `_tools/audit_advertiser_wave04.py`. Neither script collects data or authorizes a restricted route. Captured native source files remain unchanged; generated current audits/ledgers are derivatives. Final text-reading audits do not authenticate seller affiliations, receipts, delivery, accepted prices or profit.

## Unread, unresolved and how to continue

- **Unretained discovery:**419 source snapshots were not individually full-read. Of these,315 occurrences represent 310 IDs with no full-text read elsewhere;104 additional snapshots share IDs read in retained Page sources but receive no separate variant-reading credit. Exact lists: [_raw/advertiser-census-wave04-2026-10-25/audit/discovery-occurrences-not-individually-read.jsonl](../_raw/advertiser-census-wave04-2026-10-25/audit/discovery-occurrences-not-individually-read.jsonl) and [unread-discovery-ad-occurrences.jsonl](../_raw/advertiser-census-wave04-2026-10-25/audit/unread-discovery-ad-occurrences.jsonl). Twelve explicitly selected discovery occurrences were fully read. The rest remain discovery, not an exhaustive market census.
- **Whole libraries/media:** unloaded result pages, collated variants, images/videos/audio and historical inactive campaigns remain uninspected. Native reported result counts and loaded IDs are different units, so their difference is not a valid unread-ad total. Exact next-page flags and source paths are in the Page census.
- **Advertiser identity:** MyMatLeave/Bespoke HR Partners, Parentaly, Cocoon, Sparrow, BedtimeCoach, Dawnly and reference pirmizingsniai.lt remain unresolved as advertiser identities; unsuccessful keywords cannot establish zero spending. The current named zero Pages are bounded by Page/filter/time.
- **Google/browser:** saved Google records include five exact domain searches with no listings (two legacy domains), an ambiguous Sparrow name search, one Nike service-control snapshot, and a failed fresh sparrow.com canonical-domain attempt. No verified target-ad inventory or budget follows. The configured Chrome 9225 connection returned ECONNREFUSED near the end; the planned remaining canonical checks/control repeat were not captured. No other automation browser/port was used. A screenshot call also did not complete; no visual credit.
- **Price/delivery/buyer proof:** many paid app SKUs, account-specific checkout/renewal terms, delivered individualized outputs, supplier costs and independent post-use buyers remain uninspected. Offer maps document shell/403/TLS/required-agent-auth boundaries. Clinical, legal and safety claims remain seller claims. The older community/forum/Q&A/media queues are unchanged and listed in the [previous research ledger](session-report.md).

The next bounded research would use **one reader ×2–4 landing/checkout/output-comparison chunks** for the strongest paid-information advertisers, without buying or submitting personal data, plus a short Chrome session for canonical Google identity checks once the documented 9225 connection is restored. Actual spend/profit requires evidence beyond public active-ad counts; more keyword pages cannot manufacture it. No product-building, outreach or paid testing sequence is proposed.
