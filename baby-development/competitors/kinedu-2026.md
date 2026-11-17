# Kinedu — what changed by 2026-10-25, and where its ads land

**Base teardown: [`../../global/competitors/kinedu.md`](../../global/competitors/kinedu.md) and [`kinedu-assessment.md`](../../global/competitors/kinedu-assessment.md) (2026-10-24). This note adds only the changes and the ad funnel.**

Captured 2026-10-25. URLs: https://www.kinedu.com/ (home), https://apps.apple.com/us/app/id741277284 (US App Store, the ads' destination), https://masterclasses.kinedu.com/mastering-motor-development?lang=en (paid masterclass), https://webpromo.kinedu.com/p/assessment-landing (assessment funnel; JavaScript app, 0 words captured — **needs a browser walk**). `courses.kinedu.com` (e-book) failed an SSL handshake; logged.
Raw files: `_raw/competitors/kinedu-2026--home.txt`, `kinedu-2026--appstore-us.txt`, `kinedu-2026--masterclass-motor.txt`, `kinedu-2026--assessment-landing.txt`.
Meta Ad Library 2026-10-25: **208 active ads** on the Kinedu Page, top ads since 2026-07-27. Of the 33 link fields in the Page capture, 30 point to the US App Store listing (id741277284) and 3 to Google Play; none to the website. Ad copy opens "Wondering how to boost your baby's development?" and lists "1,800+ expert-designed play activities personalized to your baby's age and developmental stage", "Daily personalized activity plans that take the guesswork out", milestone/feeding tracking, live classes, masterclasses. Raw: `../../main/_raw/ads-running/page-443378469063877-kinedu-active-2026-10-25.json`.

## What changed or what this niche needs

- **Ad funnel is store-first.** The spend goes to an install, then a 7-day trial inside the app; the website is not the advertised landing page.
- **Three price surfaces disagree.** Website: "Then just $7/month" after a 7-day free trial. US App Store in-app list: Premium Monthly $9.99, "kinedu | premium (monthly)" $12.99, "kinedu | learn (monthly)" $19.99, Monthly Subscription $8.99; yearly $39.99, $69.99 and "premium (yearly promo)" $79.99. A November 2025 App Store reviewer says reviews report users being charged "$80" after cancelling the trial. The applicable offer per user is not observable without onboarding.
- **New paid one-off: masterclasses.** "Mastering Motor Development": US$29.99, anchor US$99.99 ("70% off"), one payment, lifetime access, 30-day money-back guarantee, 31 lessons, "4.9 · loved by 11M parents".
- **Scale claim raised:** "Trusted by 11 million families", "180+ countries", "25K+ 5-star reviews" (global note recorded "millions"). US App Store: 4.6 from 7.1K ratings, chart #164 Education.
- **Free assessment on the home page** compares the baby "to babies their exact age" and shows sample readings "Ahead of pace" / "On track" by area. **Flagged, recorded neutrally:** peer-comparison and ahead/behind framing, outside Mamivio's lines.
- Hook on the home page is unchanged and is the niche's dominant promise: "Exactly what to do with your baby, today."

Verbatim:

> Kinedu gives you a personalized daily plan, simple activities, milestone tracking, and real expert guidance, built around your baby's exact age and stage.

> Trusted by 11 million families. Recommended by pediatricians. Research-based.

> Answer a few simple questions and get a personalized report of your baby's development across 4 key areas, compared to babies their exact age.

> “At 6 months, showing the skills of a typical 7-month-old.”

> Cancel anytime · Then just $7/month

> $99.99 USD$29.99 USD70% off

> 30-day money-back guarantee · One payment, lifetime access

> Yearly Subscription $69.99

## Comparison with Mamivio — interpretation

The biggest advertiser in the niche sells the exact Mamivio promise ("what to do with your baby today, for their exact age") as an app subscription, and has added cheap one-time products ($29.99 masterclasses) beside it. A one-time age-selected guide sits between Kinedu's free trial and its $29.99 masterclass on price. App reviews repeatedly complain about the paywall right after onboarding, confusing UI and charges after cancelling — a "one payment, nothing to cancel, no app" angle answers objections Kinedu creates.

## Gaps

Onboarding and paywall not walked (store app). Assessment funnel is JS and needs a browser walk. E-book (courses.kinedu.com) not reached.

## Assessment walk, 2026-10-25 (owner watching) — interpretation

Raw: `../_raw/competitors/kinedu-assessment-walk/walk-2026-10-25.md`.

- **Shape:** birth date (and prematurity) → 39 Yes/Not-yet milestone items in four areas, picked for the exact age → a free "reading" → a 7-day trial paywall at **€79.99/year** (Stripe, name + email). The offer code in the URL (`p79-t7`) matches.
- **The free reading compares the baby with other babies by design:** "At 7 months, Your baby is showing the skills of a typical 6-month-old." The same screen says "not compare them to others". With half the answers "Not yet" (which the intro tells parents to expect), our test baby read a month "younger" yet was labelled "→ faster" — the label and the number disagree, and the areas show an unexplained "around 88".
- **Paywall mechanics:** three of four areas locked ("Tap to unlock"), two of five "opening up" skills shown, "+3 more in the full profile"; "unlocking adds depth by area, it doesn’t change the number"; "7 days free · no commitment" leading to an annual charge. These are the trial-to-annual mechanics the development review quotes complain about (see `../synthesis/findings.md`).
- **What it does well:** age-exact item lists, a clear two-answer rule, reassurance before the questions ("A Not yet is just as useful as a Yes"), named credibility (2,135 caregivers; a Stanford adviser), a "surveillance, not diagnosis" line on every screen.
- **For Mamivio:** the free "your baby is at the level of an N-month-old" number is the comparison hook the owner brief rules out (§8). Mamivio's development document can use the same intake idea (what the baby does today) to choose activities, without a score and without a trial-to-annual charge — one price, once.
