# App and book reviews — RV1 collection and reading ledger

Captured and read 2026-10-25 by reader RV1 under `../../_shared/_tools/brief-books-apps.md`. **449 complete original review units saved and read in full; 281 verbatim quotes** in `../voice/reviews-rv1.jsonl` (`pbr1-0001` to `pbr1-0281`). Verify: `reviews-rv1.jsonl: 281 quotes, 0 failed`. Quote counts are counts of quotes chosen, not of people or of market share. Platform selection (Apple's 10-review shelf, Google's 3 visible reviews) is not a random or recent sample; many reviews are years old and describe the product as it was then.

## Method and access

- **App Store:** public page `https://apps.apple.com/<cc>/app/<slug>/id<id>?see-all=reviews` for us, gb, ca, au, via `../_tools/collect_app_reviews.py` (copy of `global/_tools/collect_app_reviews.py`, apps and storefronts changed, browser UA added). The page's embedded `serialized-server-data` exposes up to 10 review bodies; no continuation route, no API or RSS (robots-disallowed; `../_raw/reviews/apps-robots.txt`). Untouched HTML `../_raw/reviews/<app>-<cc>-reviews.html`; frozen bodies `*-corpus.txt` and `*.units.json`. App ids came from the public pages already captured in `../_raw/competitors/` and a web search for Every Mother, Expect and Expectful.
- **Google Play:** one public detail page per app, `https://play.google.com/store/apps/details?id=<id>&hl=en_US&gl=US`, via `../_tools/fetch_page.py` (`../_raw/reviews/googleplay-<app>.txt`, HTML in `_html/`). About 3 review bodies exposed; `/store/getreviews` and batchexecute routes not used (policy `../_raw/reviews/play-robots.txt`). Developer replies were read with the reviews.
- **Barnes & Noble:** public product pages fetched (`../_raw/books/barnes-<title>.txt`); each page exposes a Yotpo product id and the public store key, and the public Yotpo storefront list `https://api-cdn.yotpo.com/v3/storefront/store/<key>/product/<id>/reviews?page=N&perPage=8` (allowed by `../_raw/books/yotpo-robots.txt`) was paged to its reported total. Raw JSON `barnes-<title>-yotpo-reviews-pN.json`; reading text derived without names as `barnes-<title>-corpus.txt`. No login, cookies or credentials.
- **Apple Books:** public book/audiobook pages per storefront (`../_raw/books/apple-<title>-<cc>.txt`); robots saved as `apple-books-robots.txt`. Customer reviews are per storefront (2–3 visible).
- **Not touched:** Goodreads and Amazon (robots bans, inherited from global/). No purchases, trials, sign-ups or installs.
- **Not re-harvested:** global/ already holds Expecting Better (Apple Books us), The Fourth Trimester (Apple Books us) and The First Forty Days (publisher page + B&N). Here only new storefronts: Expecting Better B&N + Apple Books ca/gb/au, First Forty Days Apple Books us/ca/gb/au, Fourth Trimester B&N + Apple Books gb/ca/au.
- **Ovia note:** the iOS id 570244389 and Play id `com.ovuline.fertility` are Ovia's combined cycle-and-pregnancy app; its reviews are almost all period/fertility tracking. The pregnancy-specific Ovia app was not captured on either store (Play `com.ovuline.pregnancy` 404).

## Ledger

Units = complete original reviews. Every saved unit was read in full; per-unit status and quote ids: `../_raw/reviews/reading-ledger-rv1.tsv` (`../scratchpad/RV1/ledger.py`). App Store rows are app + storefront.

| source | units saved | read | quotes |
|---|---:|---:|---:|
| App Store au babycenter | 10 | 10 | 7 |
| App Store ca babycenter | 10 | 10 | 1 |
| App Store gb babycenter | 10 | 10 | 8 |
| App Store us babycenter | 10 | 10 | 11 |
| App Store au christianhypno | 10 | 10 | 4 |
| App Store ca christianhypno | 10 | 10 | 3 |
| App Store gb christianhypno | 10 | 10 | 9 |
| App Store us christianhypno | 10 | 10 | 9 |
| App Store au everymother | 3 | 3 | 0 |
| App Store ca everymother | 10 | 10 | 7 |
| App Store gb everymother | 8 | 8 | 2 |
| App Store us everymother | 10 | 10 | 6 |
| App Store us expect | 3 | 3 | 4 |
| App Store au flo | 10 | 10 | 2 |
| App Store ca flo | 10 | 10 | 2 |
| App Store gb flo | 10 | 10 | 4 |
| App Store us flo | 10 | 10 | 5 |
| App Store au freya | 10 | 10 | 6 |
| App Store ca freya | 10 | 10 | 3 |
| App Store gb freya | 10 | 10 | 8 |
| App Store us freya | 10 | 10 | 8 |
| App Store au gentlebirth | 10 | 10 | 6 |
| App Store ca gentlebirth | 10 | 10 | 5 |
| App Store gb gentlebirth | 10 | 10 | 9 |
| App Store us gentlebirth | 10 | 10 | 14 |
| App Store ca ovia | 10 | 10 | 0 |
| App Store us ovia | 10 | 10 | 2 |
| App Store au pregnancyplus | 10 | 10 | 6 |
| App Store ca pregnancyplus | 10 | 10 | 4 |
| App Store gb pregnancyplus | 10 | 10 | 12 |
| App Store us pregnancyplus | 10 | 10 | 10 |
| App Store ca thebump | 10 | 10 | 3 |
| App Store us thebump | 10 | 10 | 12 |
| App Store au wte | 10 | 10 | 5 |
| App Store ca wte | 10 | 10 | 3 |
| App Store gb wte | 10 | 10 | 8 |
| App Store us wte | 10 | 10 | 12 |
| Google Play babycenter | 3 | 3 | 2 |
| Google Play christianhypno | 3 | 3 | 2 |
| Google Play everymother | 3 | 3 | 2 |
| Google Play flo | 3 | 3 | 2 |
| Google Play freya | 3 | 3 | 3 |
| Google Play gentlebirth | 3 | 3 | 1 |
| Google Play ovia | 3 | 3 | 0 |
| Google Play pregnancyplus | 3 | 3 | 3 |
| Google Play thebump | 3 | 3 | 2 |
| Google Play wte | 3 | 3 | 1 |
| Barnes & Noble expectingbetter | 5 | 5 | 3 |
| Barnes & Noble inamay | 11 | 11 | 7 |
| Barnes & Noble mamanatural | 3 | 3 | 5 |
| Barnes & Noble wte5 | 27 | 27 | 15 |
| Apple Books birthpartner5-audio-us | 3 | 3 | 1 |
| Apple Books expectingbetter-ca | 3 | 3 | 3 |
| Apple Books first40-us | 1 | 1 | 2 |
| Apple Books hypnobirthing-audio-gb | 1 | 1 | 0 |
| Apple Books inamay-ca | 3 | 3 | 2 |
| Apple Books inamay-us | 3 | 3 | 2 |
| Apple Books realfood-audio-ca | 1 | 1 | 1 |
| Apple Books wte-ca | 1 | 1 | 1 |
| Apple Books wte-us | 3 | 3 | 1 |
| **Total** | **449** | **449** | **281** |

Zero-unit captures (page saved, no review bodies exposed): App Store Expect gb/ca/au; Google Play Expect; B&N The Birth Partner 5th ed., The Positive Birth Book, Hypnobirthing (Siobhan Miller), The Fourth Trimester (Yotpo total 0); Apple Books pages for The Positive Birth Book (us/gb/ca/au), Hypnobirthing ebook (us/ca), Hypnobirthing audiobook us, Mama Natural audiobook (us/ca/gb), Real Food for Pregnancy audiobook (us/gb/au), The Birth Partner 4th ed. us and 6th ed. us/ca/gb, What to Expect 6th ed. gb, Fourth Trimester (gb/ca/au), First Forty Days (ca/gb/au). HTTP failures are in `reviews-not-harvested.md`.

## Read but not quoted (logged neutrally)

- 12 units centred on pregnancy loss (README line): BabyCenter us/au, What to Expect us/gb/ca ×2, Ovia us/ca, Pregnancy+ us/au ×2, Google Play The Bump. Read, not quoted.
- 5 Flo units by reviewers who are or may be minors; 3 non-English Pregnancy+ ca units (2 French, 1 Spanish).
- The rest: generic one-liners, bug reports, and period/fertility-only Flo and Ovia reviews outside this niche.

## Theme additions (beyond the README seed list)

- `country_care` — differences in maternity care or content by country (NHS self-referral, US-centric app content).
- `faith` — religious framing of birth preparation (Christian Hypnobirthing buyers).
- `relative_role` — a grandparent, parent or sibling following or buying for someone else's pregnancy.

## What was not read

App descriptions, release notes, privacy sections and "similar apps" blocks in the captured HTML; B&N and Apple Books product descriptions and editorial blurbs (seller text, not buyer evidence); full historical review archives on every platform (no permitted route). The books themselves were not read.

## Continuation

Re-capture under new filenames (never overwrite a quoted corpus). Other storefronts (ie, nz, in) would add more Apple-selected units. Pregnancy-specific Ovia app ids, Kobo and other retailers remain unprobed. New quotes go in a new voice file with a new prefix.

**Tooling note for the orchestrator:** `../../_shared/_tools/collect_restricted.py` matches ids with `[a-z]{2}\d{2}-\d{4}`; the `pbr1-NNNN` ids in this file will not be picked up by it (check `check_ids.py` too). The list below has to be merged by hand or the regex widened.

## Restricted ids

Research only, never in ads. Each quote's words touch a medical condition, medication, mental health, a screening, a procedure or pain-relief decision, loss, exercise safety, or a birth-outcome claim. The voice file also carries `"restricted": true` and `restricted_reason` on these rows.

| id | why |
|---|---|
| pbr1-0027 | screening tests and what doctors check |
| pbr1-0043 | IVF pregnancy |
| pbr1-0050 | emotional distress in pregnancy (mental health) |
| pbr1-0058 | fear of pregnancy loss |
| pbr1-0068 | severe sickness and anxiety waiting for doctor |
| pbr1-0090 | names pregnancy conditions and screening |
| pbr1-0113 | birth setting choice; reviewer makes outcome claims |
| pbr1-0119 | exercise safety framed by doctors (no exercise clearance) |
| pbr1-0120 | exercise safety claim (no exercise clearance) |
| pbr1-0123 | labour experience framed as app result (birth-outcome) |
| pbr1-0127 | anxiety (mental health) |
| pbr1-0128 | birth-outcome claim; unmedicated birth |
| pbr1-0137 | birth-outcome claim |
| pbr1-0140 | previous difficult birth |
| pbr1-0153 | pain-relief decision; birth-outcome claim |
| pbr1-0156 | anxiety in labour (mental health) |
| pbr1-0159 | epidural decision; birth-outcome claim |
| pbr1-0160 | epidural; previous hard birth |
| pbr1-0162 | birth-outcome promise (pain-free birth) |
| pbr1-0164 | unmedicated birth goal; pain-relief decision |
| pbr1-0179 | traumatic previous birth |
| pbr1-0186 | birth experience attributed to course (birth-outcome) |
| pbr1-0190 | traumatic previous birth; interventions; reviewer reports outcome |
| pbr1-0196 | birth-outcome attributed to course |
| pbr1-0207 | exercise safety in pregnancy (no exercise clearance); doctor advice |
| pbr1-0240 | unmedicated birth goal; pain-relief decision |
| pbr1-0242 | intervention framed as cause of bad births |
| pbr1-0249 | vaccination stance |
| pbr1-0250 | unmedicated birth goal |
| pbr1-0253 | alcohol in pregnancy (medical claim) |
| pbr1-0268 | homeopathic/alternative medicine |
| pbr1-0269 | home birth plan; unmedicated |
| pbr1-0270 | birth-outcome claim (natural birth best) |
