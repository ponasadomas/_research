# Phase 1A — archived discovery evidence review

Background review of saved marketplace and directory captures only. No network requests were made by this reviewer. Capture dates establish listing presence, not sales. The main run report and candidate TSV are maintained separately.

## Reviewed captures

| Capture | Observation | Candidate evidence |
|---|---|---|
| [`clickbank-index-2008.txt`](../../_raw/sales-letters/_discovery/clickbank-index-2008.txt) | 2008-07-06 ClickBank marketplace navigation and search form; Home & Family has Kids and Parenting subcategories. | No named infant-development products on this root capture. |
| [`cbengine-index-2008.txt`](../../_raw/sales-letters/_discovery/cbengine-index-2008.txt) | 2008-05-14 CBengine product-research tool home page, category-navigation links, service membership offer. | No named infant-development products; CBengine's own $39.95 membership is an affiliate research service and outside scope. |
| [`cbtrends-index-2008.txt`](../../_raw/sales-letters/_discovery/cbtrends-index-2008.txt) | 2008-04-09 CBtrends tool home page, describes historical marketplace feed and category browse/search. | No named infant-development products. |

## Review rules

- A marketplace category label alone does not verify a product, infant age band, format, sales domain, or price.
- Affiliate payout, average sale, and commission values must not be recorded as the customer price.
- A ClickBank vendor nickname identifies a seller account, not necessarily its domain; domain attribution needs visible URL evidence, saved href evidence, or an archived redirect.
- Products for older children, general discipline, pregnancy/conception, physical merchandise alone, and affiliate marketing courses need explicit scope warnings or exclusion.
- Reading offers need infant/under-two evidence; the local competitor notes describe Reading Head Start as ages two and older, so it should not be treated as a direct baby offer without historical evidence.

## Category routing evidence

The 2008 ClickBank root and its saved href sidecar map Home & Family to `c=21`, Kids to `subc=26`, Parenting to `subc=28`, and Students & School to `subc=32`. These are navigation routes, not product evidence.

[`cbengine-categories-2014.txt`](../../_raw/sales-letters/_discovery/cbengine-categories-2014.txt) (2014-01-08) and its `.links.json` sidecar show the later Parenting & Families taxonomy, each linked through `/res/search.cfm?cat=<reference>`:

| Label | Category reference | Listed product count |
|---|---|---:|
| Parenting & Families | `family` | 242 |
| Education | `family.students` | 41 |
| General | `family.general` | 16 |
| Parenting | `family.parenting` | 63 |
| Pregnancy & Childbirth | `family.pregnancy` | 56 |
| Special Needs | `family.specialneeds` | 21 |
| Languages → Sign Language | `language.sign` | 3 |

These counts describe entire marketplace categories and must not be treated as counts of qualifying baby products. The separate `education` category means Higher Education.

The CB-Analytics 2008 category menu and CBtrends 2008 browse menu likewise contain category navigation without named target products. [`jvzoo-marketplace-2014.txt`](../../_raw/sales-letters/_discovery/jvzoo-marketplace-2014.txt) (2014-08-02) is a server-rendered launch list of 25 products, predominantly marketing/software; no baby product is present in the saved first page. It is not an empty JS app, but it supplied no target leads.

Further product-capture findings will be appended as saved evidence becomes available.

## First product findings

All vendor identifiers below come from the corresponding capture's saved `.links.json` sidecar, matched to the visible product order. Customer prices are not shown. Affiliate percentages and performance values are not customer prices.

| Listing / capture evidence | Vendor ID | Fit assessment |
|---|---|---|
| Sign Language For Babies And Beyond! — [Parenting 2008](../../_raw/sales-letters/_discovery/cbengine-parenting-2008.txt) | `signbaby` | Clear adjacent baby-signing lead; category view alone does not show product format. |
| Raising Smarter Babies — same capture | `sustab` | Strong baby-development title; format and exact age range need checking. |
| How To Develop Your Childs Genius — same capture | `qandrews02` | Plausible adjacent early-learning lead; no infant age evidence on category view. |
| ABC Fun & 1-2-3 — same capture | `shirleyabc` | Age uncertain; could serve preschool/schoolchildren rather than babies. |
| How To Help Your Child Learn To Talk Better In Everyday Activities — [Parenting 2010](../../_raw/sales-letters/_discovery/cbengine-parenting-2010.txt) | `speakebook` | Plausible language-development ebook; exact infant range not shown. |
| GeniusMaker — same capture | `makky668` | Title alone insufficient: school software is possible; low confidence. |
| A Practical Guide To Baby Milestones — [Parenting 2013](../../_raw/sales-letters/_discovery/cbengine-parenting-2013.txt) | `d3w1r35s` | Strong direct lead; listing describes practical advice for baby learning important skills. |
| Baby Can Read — same capture | `figueiredo` | Explicit ebook, teaching a baby to read, adapted Glenn Doman method. Strong adjacent lead. |
| Kidzgrow Online — same capture | `babytodds` | Explicit online child-development tracking program, 0–6 years; includes target ages, membership/software distinction remains. |
| Kidzgrow Online Asia — same capture | `kidzgrowsg` | Same description and age range as Kidzgrow Online; possible duplicate domain/offer. |
| Massage For Happy Babies DVD — same capture | `prd123` | Explicit 30-minute massage/reflexology routine, home learning, digital delivery; plausible development/play adjacent lead. |
| Insight Speech Products — same capture | `speechther` | Speech/language tools for parents/therapists; no infant age evidence in listing. |

The 2013 listings expose product-detail URLs as `http://www.cbengine.com/id/<vendor>` and redirect wrappers as `http://cbengine.co/<vendor>`. Neither alone proves the eventual seller domain.

Sleep-adjacent leads in the same captures: The Baby Sleep Solution Audio Program (`mserv`, 2008 and 2010); Essential Baby Sleep (`pedisales1`, 2013); Sleep Through Baby system (`sleepbaby`, 2013); Magic Lullabies (`maxteiner2`, 2013). The Magic Lullabies listing explicitly describes professional sales copy, making it a useful letter-discovery lead even though its topic is sleep. Baby colic products are soothing/health offers rather than the requested development topic; list only with a clear adjacent/out-of-scope flag.

## Additional category findings and scope cautions

[`cbengine-education-2012.txt`](../../_raw/sales-letters/_discovery/cbengine-education-2012.txt) and its saved original HTML add clear adjacent baby-signing leads: Baby Sign Language (`smoutmedia`) and Discover How Baby Sign Language Can Help You? (`mibtt`). Other named reading products—Children Learning Reading (`1childread`), Learn To Read And Spell Through Play (`nostress2`), and Eye Can Too! Read (`blueducks`)—lack infant age evidence in this category view. Do not silently classify them as baby products. Make Your Baby Smarter Before Birth (`smartbaby`) is explicitly prenatal, and the Spanish-language early-stimulation and infant-reading listings fail the English-only requirement.

[`cbengine-pregnancy-2010.txt`](../../_raw/sales-letters/_discovery/cbengine-pregnancy-2010.txt) adds the ambiguous title Thriving Babies (`nokomisllc`), but not a verified format or topic. Its Increase Your Baby's Intelligence Before Birth (`bornsm135`) is explicitly prenatal. [`cbengine-pregnancy-2013.txt`](../../_raw/sales-letters/_discovery/cbengine-pregnancy-2013.txt) adds the sleep-adjacent audio A MP3 Download - Instant Baby Sleep Sound Track (`lifemusic`). The Complete Guide To Flat Head Syndrome In Infants (`davidsos0`) is explicitly an ebook for infants up to six months, but a therapeutic/prevention offer, not ordinary development/play guidance; retain only as an explicitly flagged possible tummy-time-adjacent lead. The listing itself does not mention tummy time.

Kidzgrow Online and Kidzgrow Online Asia are described as development **tracking programs**, so the category evidence may represent SaaS rather than an ebook/course/DVD/content membership. They should not be counted as confirmed qualifying info products without further evidence.

[`cbtrends-kids-2010.txt`](../../_raw/sales-letters/_discovery/cbtrends-kids-2010.txt) has a Kids-looking original URL, but the rendered page says “Selected Category: Home” and lists gaming/SEO products. Its URL is misleading category evidence. Historical category numeric IDs were reused, so rendered category labels and products must govern interpretation.

The [2010](../../_raw/sales-letters/_discovery/cbengine-specialneeds-2010.txt) and [2013](../../_raw/sales-letters/_discovery/cbengine-specialneeds-2013.txt) Special Needs captures mainly list diagnosis-specific guides, behaviour products, or sensory-diet software. They do not supply strong ordinary baby-development candidates. Baby shower games, nursery decoration, baby modelling, breastfeeding, fertility, and pregnancy exercise products in other categories also fall outside the requested development/play topic even when aimed at mothers.

## Later category and second-page leads

| Product | Vendor | Evidence and limits |
|---|---|---|
| Your Child Development System | `ycds1` | [Parenting page 2, 2013](../../_raw/sales-letters/_discovery/cbengine-parenting-page2-2013.txt): explicit parent/carer training, development professionals, 12-month membership; no exact child ages. |
| Mommy Jingles Musical Parenting Program | `angelsong7` | [Parenting, late 2016](../../_raw/sales-letters/_discovery/cbengine-parenting-late-2016.txt): mothers use music in everyday educational activities; demonstration videos, reminder cards, lyrics book, audio clips. No exact age band. |
| Teach Baby To Swim | `babyswim` | Same capture: explicitly for mommy/baby blogs and a sales page; format and precise age not shown. Adjacent rather than direct ordinary milestone guidance. |
| Smart Parents Guide To Choosing Best Toys For Bright Kids | `ycds1` | Same capture: practical manual for buying/using toys, same vendor as the 2013 development membership; potential duplicate domain with a different offer. No exact age band. |
| Make Your Child Multilingual | `multilingo` | [Parenting page 2, 2009](../../_raw/sales-letters/_discovery/cbengine-parenting-page2-2009.txt): title only, no infant age/format evidence. |
| Storybooks That Teach Child Development | `paulmackie` | Same capture: title only; may be child-facing storybooks instead of parent instruction. |
| Imagination Suitcase: Dramatic Play, Music, Dance For Young Children | `marekjc` | [Education, late 2016](../../_raw/sales-letters/_discovery/cbengine-education-late-2016.txt): families and young children, creative play/music/dance/art; no infant range or delivery format. |

Later evidence strengthens two signing leads: the late-2016 education capture explicitly says Sign Language For Babies And Beyond includes video of 250 signs (`signbaby`); Discover How Baby Sign Language Can Help You is explicitly a step-by-step ebook for communicating before speech (`mibtt`).

It also rules out Eye Can Too! Read as a baby offer: it serves pre-K through eighth grade. Learn To Read And Spell Through Play describes early readers and children with dyslexia, with no infant evidence. Preschool Genius Learning Pack (`evilknevil`, 2009 second page) likewise implies an older preschool audience and has no baby-age evidence.

Additional sleep-adjacent products: Stop Feeding, Start Sleeping (`jnorton`, 2013 second page); Your Baby Will Sleep (`ybws7`, same capture, explicitly three hours of MP3 plus ebook with professional video sales letter); Sleeping Angels Downloadable CD (`kimmi777`, 2009 second page); Baby Sleep Tonight (`babysleep`, same capture); Sleepytime Secrets (`sleepyt`, same capture); My Baby Sleeps Through The Night (`pjh1987`, late 2016 parenting, explicitly newborn/infant/toddler audience and video sales letter); Get Your Baby To Sleep (`11elicat`, late 2016 education). These are marked adjacent because sleep is outside the core development/play topic.

## Official ClickBank marketplace-feed review

Reviewed local original ZIP sidecars for [2017 v1](../../_raw/sales-letters/_discovery/clickbank-feed-2017-v1.txt.zip) (capture `20170711053012`), [2022 v1](../../_raw/sales-letters/_discovery/clickbank-feed-2022-v1.txt.zip), and [2022 v2](../../_raw/sales-letters/_discovery/clickbank-feed-2022-v2.txt.zip) (v2 capture `20220611031327`). These are first-party ClickBank marketplace feeds. XML title/description content resides in CDATA; the saved text conversion drops some CDATA, so the ZIP's `marketplace_feed_v1.xml` / `marketplace_feed_v2.xml` records are the full evidence.

Neither v1 nor v2 contains dedicated seller-domain, URL, or hoplink fields. Their descriptions sometimes print affiliate URLs. Performance fields remain affiliate economics, not customer prices. `ActivateDate` is vendor activation metadata, not proof that the product was seen in that year; the observations below are 2017 capture observations. The 2022 versions substantially repeat one another and must not be counted as independent products.

| New 2017 record ID | Product | Assessment | Seller URL printed in record |
|---|---|---|---|
| `SPEECHBRG` | Toddler Talk: Techniques & Games | Strong new language-development info-product lead: parent/professional how-to guide by a speech-language pathologist, first words/vocabulary/directions, games/scripts/checklists. Exact infant ages not stated. | None |
| `EARLYLEARN` | Early Educators Resources And Training | Explicit ages 0–8 and babies/toddlers/preschoolers; includes online video training and resources. Buyer framing is educators/classrooms, so flag buyer mismatch. | None |
| `COORDIKIDS` | Childhood Development Programs | Occupational-therapy foundations; exact ages and format absent. Tentative only. | None |
| `TOTSPEECH` | Toddler Speech Delay: Get Them Talking Now | Parent training for speech-delayed toddlers; therapeutic/diagnostic angle, adjacent to ordinary development. Exact ages absent. | `http://www.toddlerspeechboost.com/affiliatesignup` |
| `ALICEK1` | The Five Minute Sleep Method | New sleep-adjacent lead explicitly aimed at baby/toddler sleep. | `http://fiveminutesleep.com/affiliates` |

The 2017 `BBYSLEEP` record supplies `http://babysleepmiracle.com/aff` for Baby Sleep Miracle. `LIFEMUSIC` confirms Instant Baby Sleep is an MP3 soundtrack plus PDF ebook. `MIBTT` confirms the baby-signing ebook. `DAVIDSOS0` repeats the infant flat-head ebook's age up to six months and therapeutic scope.

Rejected apparent new development leads: `METODO360` (Montessori 360) is Spanish; `WFM01` (Web Formation Montessori) is French despite an explicit 0–3 range. `MOMSERIES` is a two-book general mothering series but has no development topic or infant ages in the record. The 2022 feed adds no clearly qualifying baby-development offer beyond those already found; Reading Head Start remains age-unverified in the feed itself.


## Candidate TSV audit

Reviewed all 28 draft rows against their saved lead captures, saved href/HTML associations, and exact XML records. All product/vendor associations and primary source paths are supported. Stated format and age caveats are appropriately conservative. Blank customer prices avoid confusing affiliate economics with retail prices.

One correction was requested: `signbaby` has observed capture years **2008;2012;2016**. The 2010/2013 sign-language category captures list Rocket Languages, not Sign Language For Babies And Beyond. A relisting date mentioned retrospectively in the 2012 detail page does not create a 2010 captured observation.

| Row | Vendor | Supported product-observation years | Audit result |
|---:|---|---|---|
| 1 | `d3w1r35s` | 2011;2013 | Supported; retain stated scope caveats. |
| 2 | `figueiredo` | 2013 | Supported; retain stated scope caveats. |
| 3 | `sustab` | 2008 | Supported; retain stated scope caveats. |
| 4 | `signbaby` | 2008;2012;2016 | Remove 2010 and 2013 if still present. |
| 5 | `smoutmedia` | 2012 | Supported; retain stated scope caveats. |
| 6 | `mibtt` | 2012;2016;2017 | Supported; retain stated scope caveats. |
| 7 | `angelsong7` | 2016 | Supported; retain stated scope caveats. |
| 8 | `babyswim` | 2016 | Supported; retain stated scope caveats. |
| 9 | `prd123` | 2013 | Supported; retain stated scope caveats. |
| 10 | `ycds1` | 2013 | Supported; retain stated scope caveats. |
| 11 | `ycds1` | 2016 | Supported; retain stated scope caveats. |
| 12 | `speakebook` | 2010;2012;2016 | Supported; retain stated scope caveats. |
| 13 | `qandrews02` | 2008;2009;2012 | Supported; retain stated scope caveats. |
| 14 | `nokomisllc` | 2010 | Supported; retain stated scope caveats. |
| 15 | `speechbrg` | 2017 | Supported; retain stated scope caveats. |
| 16 | `marekjc` | 2016 | Supported; retain stated scope caveats. |
| 17 | `mserv` | 2008;2010;2013;2016;2017;2022 | Supported; retain stated scope caveats. |
| 18 | `pedisales1` | 2013;2016 | Supported; retain stated scope caveats. |
| 19 | `sleepbaby` | 2013 | Supported; retain stated scope caveats. |
| 20 | `maxteiner2` | 2013 | Supported; retain stated scope caveats. |
| 21 | `lifemusic` | 2013;2017 | Supported; retain stated scope caveats. |
| 22 | `jnorton` | 2013 | Supported; retain stated scope caveats. |
| 23 | `ybws7` | 2013 | Supported; retain stated scope caveats. |
| 24 | `pjh1987` | 2016 | Supported; retain stated scope caveats. |
| 25 | `11elicat` | 2016 | Supported; retain stated scope caveats. |
| 26 | `bbysleep` | 2017;2022 | Supported; retain stated scope caveats. |
| 27 | `alicek1` | 2017 | Supported; retain stated scope caveats. |
| 28 | `totspeech` | 2017 | Supported; retain stated scope caveats. |

A scan of all target XML records and saved product-detail HTML found no additional seller-domain strings beyond `babysleepmiracle.com`, `fiveminutesleep.com`, and `toddlerspeechboost.com`. Domain guesses based on product names would be unsupported. The two `ycds1` offers are confirmed as the same vendor but cannot yet be marked a confirmed duplicate domain.

The Instant Baby Sleep (`lifemusic`) row can retain `http://cbengine.co/lifemusic` from the saved [2013 pregnancy-category href sidecar](../../_raw/sales-letters/_discovery/cbengine-pregnancy-2013.txt.links.json), even though its main format evidence is the 2017 feed. A blank URL is accurate but leaves an available archived redirect unrecorded.


## Independent audit of archived hop-target resolution

ClickBank hop URLs archived in CDX sometimes contain a `CBRehoppp2` query parameter. Parsing the saved original URL's query and percent-decoding that value exposes an embedded destination without requesting the seller page. The source hop hostname's vendor segment is checked against the marketplace vendor ID; the embedded destination hostname is lowercased and its leading `www.` removed to populate the domain. Cited timestamps identify the CDX record, not a fetched sales page.

This evidence supports a historical target association. It does not establish seller ownership, show the destination's content, prove an actual successful redirect, or confirm a long-form letter. Retain the original destination URL and its archived affiliate parameters as evidence. Original URLs ending in `/hop/robots.txt` can still carry a useful target parameter; their captured body is not needed for this metadata-only inference.

All resolved-map entries present at this audit matched their exact decoded target, cited timestamp, vendor ID, and normalized domain. All non-ClickBank destination domains per cited CDX file were consistent with the chosen seller domain. `ssl.clickbank.net/order/restricted.html` alternatives are account-restriction pages and were excluded, not treated as alternate seller domains. A malformed `www.babychums.mserv.hop.clickbank.net` row in the MSERV listing points at a different restricted vendor; it is not used for MSERV's valid `abook4you.mserv.hop.clickbank.net` target.

| Vendor | Verified normalized domain | Saved metadata evidence |
|---|---|---|
| `bbysleep` | `babysleepmiracle.com` | [clickbank-feed-2017-v1.xml](../../_raw/sales-letters/_discovery/clickbank-feed-2017-v1.xml) |
| `alicek1` | `fiveminutesleep.com` | [clickbank-feed-2017-v1.xml](../../_raw/sales-letters/_discovery/clickbank-feed-2017-v1.xml) |
| `totspeech` | `toddlerspeechboost.com` | [clickbank-feed-2017-v1.xml](../../_raw/sales-letters/_discovery/clickbank-feed-2017-v1.xml) |
| `signbaby` | `signing4babies.com` | [hopdomain-signbaby.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-signbaby.cdx.tsv) |
| `d3w1r35s` | `babydevelopmentnews.com` | [hopdomain-targets-d3w1r35s.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-d3w1r35s.cdx.tsv) |
| `angelsong7` | `mommyjingles.com` | [hopdomain-targets-angelsong7.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-angelsong7.cdx.tsv) |
| `babyswim` | `teachbabytoswim.info` | [hopdomain-targets-babyswim.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-babyswim.cdx.tsv) |
| `speakebook` | `helpyourchildspeak.com` | [hopdomain-targets-speakebook.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-speakebook.cdx.tsv) |
| `qandrews02` | `all-gifted-children.com` | [hopdomain-targets-qandrews02.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-qandrews02.cdx.tsv) |
| `speechbrg` | `speechtherapytalk.com` | [hopdomain-targets-speechbrg.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-speechbrg.cdx.tsv) |
| `mserv` | `babysleepsolution.com` | [hopdomain-targets-mserv.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-mserv.cdx.tsv) |
| `maxteiner2` | `magiclullabies.com` | [hopdomain-targets-maxteiner2.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-maxteiner2.cdx.tsv) |
| `lifemusic` | `instantbabysleep.com` | [hopdomain-targets-lifemusic.cdx.tsv](../../_raw/sales-letters/_discovery/hopdomain-targets-lifemusic.cdx.tsv) |

The three domains from explicit XML affiliate-resource links remain valid discovery entries when marked **affiliate resource; sales path unverified**. Their URLs must not be described as verified consumer sales-page paths. Target-CDX years are domain-resolution evidence and should not silently replace product-listing observation years.


Final addition audited: `prd123` → `newstorktimes.co.uk`. The [saved archived hop response headers](../../_raw/sales-letters/_discovery/hopdomain-prd123-header.txt.headers.json) contain a Location at capture `20121124224433` for `cyberzoo.prd123.hop.clickbank.net/hop/`, whose `CBRehoppp2` value decodes exactly to `http://www.newstorktimes.co.uk/shop/?hop=cyberzoo`. Vendor segment, timestamp, decoded target, and normalized domain all match the resolved map. This used the archived hop's Location metadata and did not fetch the seller destination. The `/shop/` path may be a catalogue; it is not evidence of a qualifying letter. The final map has **14 audited domain resolutions**.
