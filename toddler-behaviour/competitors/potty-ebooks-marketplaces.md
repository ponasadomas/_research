# Potty ebooks and printables on marketplaces — Gumroad, Shopify printables (Etsy and Payhip blocked)

Captured 2026-10-25. Public listing pages; nothing purchased. Gumroad pages render from a JSON `data-page` attribute, so their saved .txt files hold only title and meta description; the full listing text was decoded unchanged from that attribute of the saved HTML into the `.data-page.json` files below (declared here so quotes can be checked). Currency per listing in the table.

URLs and raw files:
- https://cernapublishing.gumroad.com/l/Potty_Training_Made_Easy_In_Just_3Days → `_raw/competitors/potty-ebooks-marketplaces--cerna.txt`, `_raw/competitors/potty-ebooks-marketplaces--cerna.data-page.json`
- https://parenttogether.gumroad.com/l/pottylearning → `_raw/competitors/potty-ebooks-marketplaces--parenttogether.txt`, `_raw/competitors/potty-ebooks-marketplaces--parenttogether.data-page.json`
- https://hellohelpfulbooks.gumroad.com/l/bcpun → `_raw/competitors/potty-ebooks-marketplaces--hellohelpful.txt`, `_raw/competitors/potty-ebooks-marketplaces--hellohelpful.data-page.json`
- https://shop.preschoolinspirations.com/products/potty-training-visual-schedule-kit → `_raw/competitors/potty-ebooks-marketplaces--preschool-schedule.txt`; /products/potty-training-bundle → `_raw/competitors/potty-ebooks-marketplaces--preschool-bundle.txt`. The lead "Peaceful Potty Training online course" URL redirected to the shop homepage (saved as `_raw/competitors/preschool-inspirations.txt`): course no longer listed.
- Blocked: https://payhip.com/b/AXCP1 (night-time workbook lead) → HTTP 403 challenge, stub `_raw/competitors/potty-ebooks-marketplaces--payhip-nights.txt`; https://www.etsy.com/listing/4443954652 (withholding PDF lead) → HTTP 403, stub `_raw/competitors/potty-ebooks-marketplaces--etsy-withholding.txt`. Etsy robots.txt disallows `/search?*q=` for `*`, so Etsy search was not fetched; listing paths are allowed but return 403.

Active Meta ads: not in sweep.

| Listing | Seller | Price (exact) | Anchor | Format | Social proof |
|---|---|---|---|---|---|
| Potty Training Made Easy In Just 3 Days | Cerna Publishing (Gumroad, unverified seller) | US$27.99 (`price_cents 2799`, `currency_code usd`) | "from $47.99, limited time only" | 31-page PDF: hour-by-hour plan for each of 3 days, trackers, cheat sheet | 0 ratings; 3 first-name quotes in copy; no refund policy set |
| Potty Training Class ("Potty Mastery") | Maru Rojas — Parenting Together (Gumroad) | £22 class; + troubleshooting consultation +£30 (£52); "Let me hold your hand" +£70 (£92) (`currency_code gbp`) | none | ~80–85 min video in 8 parts + 10-page PDF handbook; includes Naps & Nights, Constipation & Withholding, "How to adapt it to your child" | 19 sales shown; 0 ratings; one long testimonial |
| Potty Training Manual ("Potty Time Made Simple") | Sharina Reese (Gumroad) | US$1.99 (`price_cents 199`) | none | 18-page guide with printable progress charts, ages 18 months–3 | 0 ratings |
| Potty Training Visual Schedule Kit | Preschool Inspirations (Shopify) | €4,95 (shop localized to EUR, `"rate":"0.90600727"`) | none | printable chart, cue cards, potty book | none shown |
| Potty Training Bundle | Preschool Inspirations (Shopify) | €10,95 (localized EUR) | none | Visual Schedule Kit + 50 yoga cards/posters | none shown |

- **Buyer/trigger:** Searcher wanting a fast, cheap fix: a "3 days" plan to print, a chart, or a short class; Parenting Together targets 12 months+ and withholding.
- **Mechanism (≤8 words):** Cerna: hour-by-hour three-day plan; Parenting Together: no-rewards body-learning method.
- **Promise:** Cerna "potty train your toddler confidently in just 3 days"; Parenting Together: decide when to start, transition out of nappies "supporting your child to learn about their body"; Reese: "no pressure, just progress".
- **Proof:** First-name quotes (Cerna: "potty trained in one weekend"); sales count (Parenting Together 19). No ratings on any Gumroad item.
- **Price (exact):** see table; range US$1.99–27.99 for files, £22–92 for the video class tiers.
- **Format:** PDFs and printables; one short video class.
- **Personalization:** None generated. Parenting Together sells personalization as a human add-on (consultation +£30, hand-holding +£70) and a video on "How to adapt it to your child".
- **Guarantee:** None stated on any listing (Cerna `refund_policy` null).
- **Angles and hooks:** "In Just 3 Days", "diaper-free fast", "Proven and parent-tested", fake-urgency anchor (Cerna); "without rewards (or punishments)", "respectful", "research-based" (Parenting Together); cute printables (Reese, Preschool Inspirations).
- **Objections answered:** Parenting Together: tried another method and it failed; withholding; fear or resistance; what to buy.

> Potty Training Made Easy In Just 3 Days - The Proven, Stress - Free Method Parents Everywhere Can Follow
> Potty train your toddler in just 3 days with this 31-page step-by-step guide. Includes a clear hourly plan, printable trackers, a quick-access cheat sheet, and troubleshooting tips.
> Say goodbye to diapers, stress, and endless accidents — with a clear plan that actually works.
> A total of 8 videos (approx 80 min) and a PDF handbook with a summary of a respectful, research-based potty training method.
> If you want a method without rewards (or punishments)
> There is also the option of booking a troubleshooting consultation at a reduced price.
> You’ll get a step-by-step, potty training guide for all families, along with the training guide are printable progress charts made fun for toddlers and parents.
> Eliminate nagging and constant reminders with visuals for children that prompt them to use the bathroom at the appropriate time.

## Comparison with Mamivio — interpretation

The marketplace tail is where the literal "3 days" promise lives: an unrated US$27.99 PDF with a fake US$47.99 anchor and an hour-by-hour plan, i.e. the format of Mamivio's day-by-day output but with the promise Mamivio is not allowed to make. Mamivio's US$17.95 entry undercuts it while being honest about pace; the copy contrast is "a day-by-day plan for your child, at your child's pace" vs "in just 3 days". Parenting Together shows the price ladder Mamivio plans (£22 → £52 → £92) already exists in this market, with the steps sold as human time; Mamivio's ladder replaces the human with a plan that adapts to the answers, so it should be explicit about what each tier adds. Printable charts at €4,95 and US$1.99 set the floor for "a chart"; any chart Mamivio bundles is a bonus, not a reason to buy.

## Gaps

Etsy (the largest pool of 3-day ebooks and charts) and Payhip (night-time workbook and 3-day PDFs) blocked by 403; their prices, review counts and sales could not be captured. Gumroad sales counts hidden on two listings. No item bought, so page quality unknown.
