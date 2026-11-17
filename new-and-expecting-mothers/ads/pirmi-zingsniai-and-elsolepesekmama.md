# Pirmi Žingsniai (LT) and Első Lépések / elsolepesekmama.com (HU) — what they advertise

Captured 2026-10-25 in a real browser with the owner watching, Meta Ad Library, country ALL, active + inactive, sorted by impressions. Raw result pages (embedded `search_results_connection` data plus visible text) are in `../_raw/ads-running/`. Storefront product lists come from each shop's public `products.json` (`../_raw/competitors/*-products.json`); the two Hungarian advertorial pages the ads link to are saved as HTML there too. Counts are what the Library reported today; an ad count is not spend, and spend is not profit.

## The two Pages

| site | advertising Page | Page id | ads on record | active today | first seen | last seen |
|---|---|---|---|---|---|---|
| pirmizingsniai.lt (Lithuania) | "Jaunos mamos užrašai" ("A young mom's notes") | 1068806566323158 | 116 | **0** | 2026-05-08 | 2026-08-14 |
| elsolepesekmama.com (Hungary) | "Egy fiatal anya jegyzetei" (same name, Hungarian) | 1191039840766910 | 206 | **72** | 2026-07-02 | still running 2026-10-24 |

Reading: the Lithuanian campaign ran May to mid-August 2026 and stopped. The Hungarian clone started in July, overlapped for six weeks, and is the live operation now with 72 active ads. Same Page naming, same ad formats, same founders' story translated.

## What the ads send people to (top 30 by impressions, each Page)

| landing page | LT, of 30 | HU, of 30 | what it is |
|---|---:|---:|---|
| development guide product page | 15 | 0 | the age-selector PDF (€17.95 LT) |
| pregnancy guide product page | 14 | 10 | the first/second/third-pregnancy PDF (€29.95 LT; 15,000 HUF HU) |
| `/pages/rolunk` ("About us") | – | 14 | **advertorial bridge page** for the development guide: two physiotherapist founders, "babies reach milestones later than a generation ago", Heckman / Abecedarian / Jamaica study numbers, then "see the guide" |
| `/pages/miert` ("Why") | – | 5 | advertorial bridge page for the pregnancy guide: "Rest is not the answer. A prepared body is.", WHO 150 min, Cochrane −28% gestational diabetes |
| sleep guide | **0** | **0** | |
| speech guide | 0 | 0 | |

Among the 72 ads active in Hungary today, the link targets are exactly three: the pregnancy product page, the `/pages/rolunk` development advertorial, and the development product page. **No ad on either Page, active or inactive, links to the sleep or speech guide.** Those two exist in both shops (below) but are catalogue items, not acquisition products. This matches the owner's observation that sleep is not Pirmi's front end.

## The two catalogues (products.json, 2026-10-25)

| shop | product | price | anchor | selector | created |
|---|---|---|---|---|---|
| LT | Personalizuotas Kūdikio Vystimosi Gidas (development) | €17.95 | €24.95 | months 0–12 × weeks 0–3 (56 variants) | 2026-04-30 |
| LT | Nėščiosios gidas (pregnancy) | €29.95 | €59.95 | which pregnancy (3) | 2026-06-09 |
| LT | Kūdikio miego gidas (sleep) | €24.95 | €34.95 | none | 2026-06-12 |
| LT | Kūdikio kalbos vystymosi gidas (speech) | €34.95 | €69.95 | none | 2026-06-15 |
| HU | Várandóssági Útmutató (pregnancy) | 15,000 HUF | 30,000 HUF | which pregnancy (3) | 2026-07-02 |
| HU | Személyre szabott Babafejlődési Útmutató (development) | 12,700 HUF | 18,700 HUF | months × weeks (70 variants) | 2026-08-05 |
| HU | Baba Alvási Útmutató (sleep) | 9,400 HUF | – | none | 2026-10-05 |
| HU | Baba Beszédfejlődési Útmutató (speech) | 13,100 HUF | – | none | 2026-10-05 |
| HU | Személyre szabott Babafejlődési Útmutató (0–12), new SKU | 30,000 HUF | 9,400 HUF shown as compare (likely a data error) | "plan duration" (2 variants) | 2026-10-15 |

The order of creation is the strategy: development first, pregnancy second, then sleep and speech as un-personalized add-ons, and in October a new development SKU sold by plan duration, the same tiering Mamivio uses ($17.95 / $29.95 / $49.95 for 1 / 3 / 6 months).

## The ad formats

All long-form story ads under a persona Page, not brand ads. Three recurring openers across both countries, translated:

- **The clinician's confession.** "I have worked in a children's hospital for twelve years … I have 8–12 minutes per check-up … 'Why did nobody tell us this before?'" (LT and HU, development). "I have been a midwife for 20 years …" (HU, pregnancy, the ad active today). "As a physiotherapist I work with pregnant and postpartum women … it comes down to one thing" (LT and HU, pregnancy).
- **The mother's comparison moment.** "The neighbour said her baby sat up at four months. Mine, at seven, still didn't." / "My friend's daughter of the same age was already rolling over." / "My daughter was ten months old and had not said a single word. Not 'mama', not 'papa'. My sister-in-law's son, same age …" (development; the brief's social sting, verbatim in market).
- **The 2 a.m. scene.** "It's 2 a.m. You're not sleeping again. Your back hurts …" (pregnancy). "I sat at 2 a.m. …" (development).

Headlines seen: "Be sure your baby is developing well" (both languages, the most repeated), "Your baby can do much more", "I understood why my baby is behind", "My baby does nothing. Is that normal?", "Preparation for birth doesn't start at week 36", "Rest is not the answer. This is.", "Pregnancy is not suffering.", "Not more toys. More you.", "The first year happens only once".

Several LT ads open with the unverified statistic "92% of children in 1957 started walking by 12 months" (see `global/sources/guidance.md` on why the historical-decline claim is unsupported).

## What this does and does not establish

- Establishes: a two-product acquisition machine (development + pregnancy), story-ad creative, bridge pages, a country-by-country rollout, and a live spend footprint of 72 ads in Hungary. Sleep and speech are catalogue extensions bought after the first purchase, not what the ads sell.
- Does not establish: spend, revenue, conversion, or that the Lithuanian stop was a failure (it could be seasonality, saturation of a 2.8-million-person market, or the team moving to Hungary).
- The two document-only sleep sellers found earlier (BedtimeCoach $19, Dawnly $67) have **no ads on record at all**; "Dawnly Sleep" returned one inactive ad for an unrelated vibration-alarm wristband. Searches saved alongside.
