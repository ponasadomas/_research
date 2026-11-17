# Primary clinical guidance — 2026-10-24

Ten successful first-party HTML captures plus one WHO one-page PDF were saved and their substantive content read. Ten short excerpts are recorded in `voice/guidance-01.jsonl` and `voice/guidance-02.jsonl`. Full nav/footer text is also retained. One NHS play URL returned 404 and supplies no evidence. These professional sources help set report boundaries; they do not demonstrate willingness to pay.

| Downloaded pages | Matched relevant articles | Kept | Article bodies read | Quotes |
|---:|---:|---:|---:|---:|
| 12 responses (11 valid documents, one 404) | 11 | 11 | 11 | 10 |

All successful `.txt` files in `_raw/guidance/` were reviewed in full for their article content. `_html/` files are preserved source markup, not a second reading corpus. WHO’s linked one-page achievement-window table was downloaded, mechanically extracted, rendered and visually inspected. Other linked publications were not downloaded or read. `nhs-baby-play.txt` is an error response, not an unread article.

## Findings and boundaries

- [CDC milestone explanation](https://www.cdc.gov/act-early/milestones/key-points.html), `_raw/guidance/cdc-milestones.txt`, `[guide01-001]`: checklist items are communication aids, not diagnostic tests. The revision places milestones where at least 75% of children are expected to show them to improve action on concerns. That methodological change does not establish that children have become slower developers. The product's historical-decline narrative needs separate longitudinal evidence.
- [NICHD tummy time](https://safetosleep.nichd.nih.gov/reduce-risk/tummy-time), `nih-tummy.txt`, `[guide01-002]`: tummy time means awake and supervised. The page describes short sessions and age-dependent totals. A historical comparison must never blur prone play and infant sleep or imply 12 hours of tummy time is a target.
- [CDC first solids](https://www.cdc.gov/infant-toddler-nutrition/foods-and-drinks/when-what-and-how-to-introduce-solid-foods.html), `cdc-solids.txt`, `[guide01-003]`: starting depends on readiness, food preparation and supervision. Severe eczema or egg allergy requires discussion with the child's clinician about peanut introduction. A household meal-planning tool must not prescribe allergen challenges, assess swallowing or guarantee prevention of choking/allergy.
- [ACOG pregnancy activity](https://www.acog.org/womens-health/faqs/exercise-during-pregnancy), `acog-exercise.txt`, `[guide01-004]`: activity is generally supported for healthy uncomplicated pregnancies, with clinician discussion and stop signs. An automated exercise prescription cannot infer clearance from gestational week alone.
- [OWH work transition](https://womenshealth.gov/breastfeeding/breastfeeding-home-work-and-public/breastfeeding-and-going-back-work), `owh-work.txt`, `[guide01-005]`: planning involves employer, childcare and ongoing adjustment. Its legal summaries are background only; this research does not verify current employment rights from that page.
- [NHS work transition](https://www.nhs.uk/baby/breastfeeding-and-bottle-feeding/breastfeeding-and-lifestyle/back-to-work/), `nhs-work.txt`, `[guide01-006]`: a childcare rehearsal is a concrete planning task. UK-specific advice must not be silently substituted for US guidance; country matters even within an English-language launch.
- [CDC pumping](https://www.cdc.gov/infant-toddler-nutrition/breastfeeding/pumping-breast-milk.html), `cdc-pump.txt`, `[guide01-007]`: frequency relates to the baby's feeding and individual circumstances; personalized pumping support belongs with a lactation provider. A logistics report can organize a clinician-agreed routine, but cannot promise supply outcomes.
- [CDC maternal warning signs](https://www.cdc.gov/hearher/maternal-warning-signs/index.html), `cdc-urgent-maternal.txt`, `[guide01-008]`: a postpartum planning report needs clear routes to care. Crisis narratives and symptoms are excluded from customer targeting and commercial hooks.

The headline statistics on Mamivio and Pirmi Žingsniai remain unverified; this session did not locate primary longitudinal evidence establishing the full claims. No claim is declared false merely because a citation is absent.

To continue: a qualified reviewer should map each proposed report rule to country-specific primary guidance and resolve discrepancies. This is separate from interviewing customers and testing purchase demand.

## Supplemental claim checks

[AAP / HealthyChildren](https://www.healthychildren.org/English/ages-stages/baby/sleep/Pages/Back-to-Sleep-Tummy-to-Play.aspx), `_raw/guidance/aap-tummy.txt`, `[guide02-001]`: full article read. Its September 2026 update keeps awake supervised tummy time separate from back sleeping; no historical-development-decline claim is made.

[WHO motor milestones](https://www.who.int/tools/child-growth-standards/standards/motor-development-milestones), `_raw/guidance/who-motor.txt`, and the [one-page achievement-window table](https://cdn.who.int/media/docs/default-source/child-growth/child-growth-standards/indicators/motor-development-milestones/mm_windows_table.pdf?sfvrsn=cb31ec78_5), `_raw/guidance/who-windows.pdf`, `.txt` and `.png`, `[guide02-002]`: landing page and full table read; PDF render visually inspected. The table references a 2006 study and provides ranges, not a comparison of 1970s and current babies. It therefore does not establish the product’s three-month-decline narrative. The underlying full study was not read.
