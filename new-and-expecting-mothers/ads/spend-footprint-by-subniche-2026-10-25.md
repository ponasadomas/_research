# Who is spending on Meta, by sub-niche — 2026-10-25

Meta Ad Library in a real browser with the owner watching. Country ALL, **active ads only**, sorted by impressions, exact-phrase searches (loose keywords return tens of thousands of unrelated ads; "sleep training" unordered returned 50,001 results of mattresses and supplements, so every row below is an exact phrase). For each search the Library exposes the first ~30 ads with embedded data; advertiser counts per search are therefore counts within that top-30 sample. For every info-product seller that appeared, the Page itself was then opened to get its **total active-ad count** and the earliest start date among its top ads. Raw result pages: `../_raw/ads-running/sweep-*.json` and `page-*.json`.

Rules: an active-ad count is a spend footprint, not spend; spend is not profit; "running since" is the earliest start among the top 30 ads shown, so a Page can be older than that date.

## 1. Phrase searches

| phrase (exact) | active results | info-product sellers in the top 30 | everything else in the top 30 |
|---|---:|---|---|
| "baby sleep" "plan" | 224 | Let's Sleep 7 · Just Chill Baby Sleep 5 · Smart Starts 3 · **Betteroo (quiz funnel) 3** · Good Inside Baby 2 · Taking Cara Babies 2 · Happy Sleep Co 1 · Baby Sleep Solutions by Amelia Hunter (ES) 1 | Cradlewise crib 3 |
| "wake windows" | 293 | Rachel Rothman → quiz.betteroo.ai 2 · Taking Cara 1 · Danielle Greene sleep consulting 1 | Lovevery 13 · Huckleberry 4 · Buma tracker 4 · Napper 1 · Kit & Kin free newborn guide 2 |
| "sleep regression" | 128 | Taking Cara 2 · Sleep Nanny (free guide lead-gen) 1 · Sleep Well With Hannah 1 | Huckleberry 8 · HALO 2 · Dreamland Baby 2 · magnesium 6 |
| "sleep consultant" | 608 | Let's Sleep 6 · Little Slumber Stars 2 · Baby Sleep Consultant (.co) 2 · consultant-training courses 2 | mattresses (Sealy ID 5), Hatch, pillows |
| "sleep through the night" | 32,381 | none in top 30 | Vicks 9, pain, snoring, maternity pillows: the phrase is adult-sleep noise |
| "baby milestones" | 222 | none document-shaped | Pampers 6 · Kinedu (app) 3 · Pathways (free app) 1 · photobooks 5 · Baby Acrobatics 1 |
| "baby development" | 471 | Baby Acrobatics 2 · First Step Method 1 | Kinedu 2 · Bloom Baby Classes (since 2023) 2 · Flo 2 · Wonder Weeks app 1 · Pathways 1 |
| "toddler tantrums" | 86 | parentPRO 2 · Parenting with Rishika 1 | Sarah Mitchell → trysaphire.com 5 (ADHD-kids angle) · Mothercare 3 · noise |
| "gentle parenting" | 457 | MindNest / bloomlittle.com 3 · Jackie Black (parental time bomb) 2 · Parenting with Dr Wendy 1 · Feed Sleep Bond (Lyndsey Hookway) 1 | The Cut article 2 · The Calm Anchor ADHD 2 · noise |
| "Big Little Feelings" | 80 | Big Little Feelings 30 of 30 | |
| "potty training" | 7,159 | **UpAiry and its persona Pages 21 of 30** (Emma's Mom Hacks, Raising Toddlers with Bec) | Pampers Easy Ups, Coterie, Millie Moon, Rascals nappies |
| "potty training" "course" | 294 | Raising Toddlers with Bec → upairy.com 10 · **Big Little Feelings 7** · Kereisa Collens → upairy 2 · Potty Training Consultant (courses.) 2 | |
| "starting solids" | 939 | Tummi app 2 · Slurrp Farm plans 2 | Earth's Best 5 · Little Spoon 4 + two persona Pages · Kendamil 4 · Target 2 |
| "pumping schedule" | 34 | Milky Mama (supply course + supplements) 4 · Nichole McCloy lactation 2 | Latch-well 3 · septic-tank pumping 8 |
| "birth plan" | 816 | none | hospitals (Providence Swedish 8, AdventHealth, Dignity), cord blood (StemCyte, Cordlife, ViaCord), TENS units |
| "hospital bag" | 2,860 | none | Amazon affiliates, maternity wear, Tucks, cord blood |

## 2. Info-product sellers, Page by Page

| Page | sub-niche | active ads | top ads running since | what the ads sell | format |
|---|---|---:|---|---|---|
| **Kinedu** | development | 208 | 2026-07-27 | app installs; "daily activity recommendations tailored to your baby's age", "1,800+ activities", "the app recommended by pediatricians" | app, subscription |
| **Taking Cara Babies** | sleep | 96 | 2026-02-14 | newborn sleep bundle 8 · b.e.s.t. swaddle 8 · toddler sleep training 5 · 5–24 month collection 4 | video courses $129–249 + a physical swaddle |
| **Big Little Feelings** | toddler / potty | 76 | 2025-11-11 | **Potty Training Made Simple 20 of 30** · Winning the Toddler Stage 5 · new "Big Feelers" course 5 | video courses |
| **Első Lépések (Pirmi, HU)** | development + pregnancy | 72 | 2026-07-02 | development guide via advertorial, pregnancy guide | age-selected PDF |
| **Let's Sleep** | sleep | 50 | 2026-08-13 | one product: "7 Day Self-Settling Course" by Jazz, a midwife; headlines "Self Settling Plan", "A Different Approach to Baby Sleep" | course on SamCart |
| **Betteroo** | sleep | 39 | 2026-08-06 | quiz.betteroo.ai → "A personalized sleep plan", "Join the 28-Day Better Sleep Challenge", "Better Sleep Or Your Money Back", "transform sleep in just 15 minutes a day", UGC-style mother testimonials; a second persona Page (Rachel Rothman) feeds the same quiz | **quiz → personalized plan, 28-day program** |
| **Just Chill Baby Sleep (UK)** | sleep + potty | 35 | 2026-07-10 | Sleep Success 6–9 months 14 · Foundations of Sleep 0–5 months 6 · **Guide to Potty Training 9** | age-banded courses + a potty guide |
| **Good Inside Baby** | sleep | 21 | 2026-09-08 | one landing page: baby sleep program bundle; "There's no sleep method that works for every baby. There is an approach that works for yours" | program |
| **Smart Starts for Parents** | newborn / sleep | 10 | 2026-06-17 | Babywise author's new first-year book on Amazon 5 · free "get your kids to listen" guide 5 | book + lead magnet |
| Sleep Nanny Melanie Hastings (UK) | sleep | 4 | 2025-05-29 | two free guides (4-month "progression", 5am waking) | lead-gen for consulting |
| The Happy Sleep Company | sleep | 1 | 2026-07-27 | "often covered by insurance" consulting | service |
| **UpAiry** | potty | 838 | 2024-12-03 | potty-training underwear 25 of 30, plus a "potty-train" method page; three further persona Pages run the same offer ("My toddler had 7 accidents in one day", "Potty train in weeks, not months") | physical product with a method, 22 months running |
| Potty Training Consultant | potty | not opened | 2026-05-12 | courses.pottytrainingconsultant.com | course |
| MindNest / bloomlittle.com | toddler | not opened | 2026-09-28 | emotional-regulation program | program |
| Milky Mama | feeding | not opened | 2026-07-08 | "join 300,000+ moms who've increased their milk supply": courses + lactation products | course + supplements |
| Little Spoon (+2 persona Pages "Starting Solids Stress-Free", "Tiny Eaters Nutrition") | solids | not opened | 2026-09-23 | baby food delivery, sold with a "starting solids is overwhelming" hook | food, not information |
| BedtimeCoach, Dawnly Sleep | sleep | **0** | | the two document-only quiz-PDF sellers | no ads at all |

## 3. What the spend says, sub-niche by sub-niche

**Sleep is where the info-product money is, and it is sold as a course or a quiz-to-plan, not as a static PDF.** Six sellers with 21 to 96 active ads each, all started or scaled in 2026, four of them in the last three months (Let's Sleep, Betteroo, Just Chill, Good Inside), which means the angle is being tested hard right now by people with budgets. Betteroo is the direct analogue of the Mamivio model with money behind it: a quiz, "a personalized sleep plan", a 28-day structure, a guarantee, UGC testimonials from mothers. The two sellers of a bare PDF plan (BedtimeCoach, Dawnly) have never run an ad. Apps (Huckleberry, Napper, Buma) and hardware (Cradlewise, HALO, Nanit) share the same phrases. Earlier conclusion that "sleep is a back-end add-on" was drawn from Pirmi alone and is **withdrawn**: Pirmi keeps sleep on its back end, the English-language market puts it on the front end.

**Potty training is the second cluster, and it was a tier-2 row on the map.** The biggest toddler brand (Big Little Feelings) leads with its potty course, not its toddler course; a UK sleep consultant adds a potty guide to her sleep courses; a physical-product seller has run 838 active ads for 22 months on "potty train in weeks, not months" with persona Pages; a standalone potty-course seller advertises. The Reddit width proxy (0.3%) missed it because no toddler community was harvested and because potty is a short, intense window, not a chronic topic.

**Development is app money, plus Pirmi.** Kinedu runs 208 active install ads on "activities tailored to your baby's age"; Lovevery sells kits on "wake windows"; Pathways advertises a free app. The only paid document-shaped development offer advertising anywhere in this sweep is Pirmi's Hungarian clone. "Baby milestones" as a phrase belongs to Pampers and photobooks.

**Toddler behaviour beyond potty is thinner than expected.** Big Little Feelings' toddler course gets 5 of its top 30; MindNest, parentPRO and a few coaches advertise; the ADHD-kids angle (trysaphire.com, The Calm Anchor) is the one that recurs. The phrase searches may be the wrong door (parents don't type "toddler tantrums" into an ad), so this is a lower bound.

**Pregnancy and birth have no info-product advertisers under these phrases.** "Birth plan" and "hospital bag" are owned by hospitals, cord-blood banks and Amazon affiliates. Pirmi's pregnancy guide in Hungary is again the only document seller found. Hypnobirthing and birth-course brands were not searched by name; that is a gap, not a finding.

**Feeding and solids are product money.** Milky Mama (supply courses plus supplements) is the one info seller on pumping; solids phrases belong to food brands and Little Spoon, which runs persona Pages with an information hook to sell food.

## 4. Caveats

- Top-30 samples per search; a seller with many small ads can be under-counted and a seller with one big ad over-counted. Page active counts are exact.
- Country ALL mixes markets; several sellers are UK (Just Chill, Sleep Nanny) or Australian/Spanish. The owner has not chosen a launch country.
- Not searched: brand names of birth/hypnobirthing courses, breastfeeding courses, "newborn course", "baby schedule", speech-delay courses, and non-English phrases. Not opened: Little Slumber Stars, Baby Sleep Consultant (.co), MindNest, Potty Training Consultant, Milky Mama Pages.
- The owner independently opened Little Ones, Napper, Taking Cara Babies, Babylist, Mindful Return and the Google Ads Transparency Center during the session; those tabs were not captured here.
