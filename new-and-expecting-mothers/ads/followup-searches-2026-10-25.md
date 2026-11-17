# Ad Library follow-up searches — 2026-10-25 (evening)

Meta Ad Library in a real browser with the owner watching, country ALL, sorted by impressions. Raw results: `../_raw/ads-running/w2-*.json` (extracted with `../_tools/adlib_extract.js`, summarised with `adlib_show.py`). A control search ("Big Little Feelings", exact, active) returned 80 ads, the same as the morning, so zeros below are real, not throttling. Counts are spend footprints, not spend; spend is not profit; "since" is the earliest start among the top ads shown.

## 1. Competitors found in the research, searched by name and domain

| seller | searches | result |
|---|---|---|
| **Mother Compass** ($29.99 birth-prep PDFs, found via a seller post on Reddit) | "mother compass" exact, all; mothercompass.com | **0 ads, active or past** |
| **Calmer Nights** (UK questionnaire → AI 7-day sleep plan, £9.99; closest Mamivio analogue) | "calmer nights" exact (39,046 hits, all other products using the phrase); "calmer-nights.com" exact | **0 ads under its domain** |
| **Actually Sleeping** ($2,000–4,000 tiers, "guarantee"; a Reddit parent found it via an Instagram ad) | "actually sleeping" exact (50,001, common phrase); "actuallysleeping" exact | **not found** — may run from a person-named Page; the press releases found by web search are company-sourced |

Reading: the two closest document-shaped analogues to Mamivio (Mother Compass, Calmer Nights) do not advertise on Meta, like BedtimeCoach and Dawnly in the morning sweep.

## 2. The mother's own sleep — ten phrases (exact, active)

| phrase | active | who advertises (top ads) |
|---|---:|---|
| "postpartum insomnia" | 13 | a Singapore postnatal-massage clinic (11) |
| "sleep when the baby sleeps" | 93 | baby loungers, a night-nurse service (Edmonton), mattresses, novels |
| "sleep deprived mom" | 11 | products; **Betteroo** (1, to quiz.betteroo.co) |
| "pregnancy insomnia" | 48 | **babybub pillow 14** ("pregnancy insomnia is hurting your baby" — a fear hook Mamivio cannot use), 8 Sheep Organics, Sleepybelly, Femometer ring, BabyCenter app |
| "exhausted mom" | 225 | grounding sheets, coffee, supplements, a baby-sleep gadget, an ADHD-gummies quiz |
| "new mom sleep" | 1 | a hospital |
| "night nanny" | 98 | agencies (Singapore, Canada, Denmark), short-drama ads |
| "postpartum doula" | 313 | doula trainings, local doula services |
| "CBT-I" | 515 | adult insomnia programmes (Resolve Sleep Health "CBT-I. Proven Insomnia Treatment"), a coach's free "fall back asleep after a 3AM wake-up" guide, clinics in Italy/Denmark |
| "mom sleep" | 73 | linen, sleep drops, **Taking Cara Babies** (2), **The Latch Link** infant sleep class |

Reading: **no information product is sold for the mother's own sleep** under any of the ten phrases; the money is pillows and supplements (pregnancy), local night help, and adult insomnia programmes that do not mention babies. This confirms `../../sleep-mother/synthesis/findings.md` §10 (a module inside baby sleep, not a product).

## 3. Pregnancy and birth — phrases and Pages (exact, active)

| phrase | active | information sellers in the top ads |
|---|---:|---|
| "birth course" | 29 | **Built To Birth 12**, Hypnobirthing Australia 3, Montessori pre-birth course, PowerBirth ("Feel Prepared, Not Overwhelmed"), a "low-pain method" free class (epidural-refusal hook, off-limits) |
| "hypnobirthing" | 269 | Happy Parents Happy Baby 7 (in-person UK classes), Mamiflow, local hypnobirthing teachers |
| "pregnancy guide" | 127 | lead magnets: hospital "Free Baby Planning Guide" (Lehigh Valley, Mercy), **Sleepybelly "The Early Pregnancy Guide Every First-Time Mum Needs"** (free, to sell pyjamas/pillows) |
| "labor prep" | 20 | Nātal app "expecting athletes challenge", a pelvic-floor PT course, insurance-covered childbirth education (Made for Birth & Beyond) |
| "second pregnancy" | 914 | products only (babybub, skincare, IVF clinics, a supplement advertorial) |

| Page | active ads | since | what the ads sell |
|---|---:|---|---|
| **Built To Birth** (365714564273145) | 22 | 2026-07-14 | premium course membership (10 of 22), "Skip the scary birth stories. Learn what actually…" (4), free mini birth class (3) |
| **Hypnobirthing Australia** (360037147148) | 21 | 2026-05-22 | Positive Birth Program online ("The natural approach to a calm and positive birth", "Don't choose your birth course on price alone"), educator training |
| **The Latch Link** (531672490027214) | 223 | 2026-07-25 | insurance-covered breastfeeding consults ("$0 out-of-pocket for most moms") 26 of 30; a 0–12-month infant sleep class (1) |

Reading: **this corrects the morning sweep's "no pregnancy information advertisers"** — that came from "birth plan" and "hospital bag", the wrong door. Birth courses do advertise (Built To Birth, Hypnobirthing Australia), but no one advertises a pregnancy guide by trimester or by pregnancy number; "pregnancy guide" ads are free lead magnets for hospitals and pillow brands. The hook that works for courses is preparation without fear ("Skip the scary birth stories"; "Feel prepared, not overwhelmed").

## 4. Not done in this session

Teardowns of Built To Birth's and Hypnobirthing Australia's sales pages (the pregnancy competitor notes have them from the morning agent run: `../../pregnancy-birth/competitors/built-to-birth.md`; Hypnobirthing Australia is in `hypnobirthing-australia-hypnobubs.md`); Page lookups for Actually Sleeping (needs its Page id).

## 5. Quiz and checkout walks (same evening, owner watching)

Stopped at every email or card field; nothing entered, nothing bought. Screen-by-screen logs sit next to each competitor note.

| seller | walk log | where it stopped | price seen |
|---|---|---|---|
| **Betteroo** (baby sleep, parent-first) | `sleep-baby/_raw/competitors/betteroo-quiz-walk/walk-2026-10-25.md` | email gate after ~47 screens | behind the gate (earlier: "from $1/day") |
| **UpAiry** (potty pants) | `toddler-behaviour/_raw/competitors/upairy-quiz-walk/walk-2026-10-25.md` | no gate; product page | 1 pair €19,95 · 5 €26,00 · 10 €54,00; ebook given free |
| **Big Little Feelings** "Big Feeler" quiz | `toddler-behaviour/_raw/competitors/blf-quiz-walk/walk-2026-10-25.md` | email required to see results | — |
| **Kinedu** assessment | `development/_raw/competitors/kinedu-assessment-walk/walk-2026-10-25.md` | Stripe trial paywall | €79.99/year after a 7-day trial |
| **Calmer Nights** questionnaire | `sleep-baby/_raw/competitors/calmer-nights-walk/walk-2026-10-25.md` | name + email on the first page | (earlier: £9.99) |
| **Tinyhood** | note in `pregnancy-birth/competitors/tinyhood.md` | no quiz exists | gift year $155.40 |

What the walks add:
- **Only Betteroo makes the personalisation visible**, by echoing answers back and changing images; it earns ~45 screens before asking for email. UpAiry's score changed (1/10, then 3/10) for the same answers; Kinedu's reading said "typical 6-month-old" next to "→ faster" for a 7-month-old. These are the slips that make "personalised" look fake.
- **The intake questions are a ready checklist** for Mamivio: the parent's own state (Betteroo), what was tried and temperament (UpAiry), age-exact skills with a two-answer rule (Kinedu), a health-data consent and a "is your baby currently well?" gate (Calmer Nights).
- **Every one uses a claim or mechanic Mamivio rules out:** a dated outcome promise (Betteroo "0 night wakeups by Nov 25"), timelines and an unsourced 1957 statistic (UpAiry), an age-equivalent comparison score and trial-to-annual billing (Kinedu), a diagnostic-sounding label (BLF).

Not walked: Good Inside (its quiz path is disallowed in robots.txt) and Baby Acrobatics (same) — owner's call.

**Update — Betteroo past the email gate (owner's inbox):** 1-Week Trial €26.77, 4-Week Plan €29.00, 12-Week Plan €69.61 ("35% OFF", 10-minute countdown). Checkout: "€29.00 now, then €44.62 every 4 weeks from 22 Nov 2026. Cancel anytime." A subscription with 1:1 human support, not a one-off plan.

**Funnels given incomehero@gmail.com (for forwarding into `_raw/funnels/<name>/emails/`):** Betteroo (quiz.betteroo.ai, name "Research", 2026-10-25).
