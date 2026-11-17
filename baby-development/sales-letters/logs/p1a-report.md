# Phase 1A — ClickBank marketplace history

Run date: 2026-11-03. Read `sales-letters/README.md` first. Output: [candidates-A.tsv](../candidates-A.tsv). Evidence review: [p1a-evidence-review.md](p1a-evidence-review.md).

28 offer rows; 14 rows have an evidenced seller domain (14 unique domains); 14 retain unresolved domains. 11 rows are explicitly sleep-adjacent. Several remaining rows have age, format or therapeutic-scope cautions. This is a candidate queue, not a list of verified qualifying sales letters. No seller sales page was fetched.

Request accounting: **110 counted requests**: 109 instrumented request attempts (retries included), 0 instrumented followed redirects, and one initial CDX call before instrumentation. The initial successful HTTP call did not log automatic redirects; reserving the urllib limit of ten additional redirects gives a conservative **maximum of 120 Wayback requests**, within the 120-request cap. The instrumented hard stop was 109 requests, including any logged redirects. Detailed evidence: [`p1a-requests.jsonl`](../../_raw/sales-letters/_discovery/p1a-requests.jsonl), [`p1a-commands.jsonl`](../../_raw/sales-letters/_discovery/p1a-commands.jsonl), [`p1a-helper-stderr.log`](../../_raw/sales-letters/_discovery/p1a-helper-stderr.log).

All Wayback traffic used `python3 -I _tools/wayback.py`, sequentially, with its shared four-second throttle. No live site visits. CDX windows were primarily 2008–2020, extended to 2005–2022 for feed and hop metadata. Actual product observations span 2008–2022; capture years in the TSV are discrete observations, never a claimed continuous sales period.

What worked: CBEngine supplied nearly all early product names, descriptions and vendor IDs. Its 2008 taxonomy was Home & Family → Kids/Parenting; later menus used Parenting & Families → Parenting/Education/Pregnancy/Special Needs. Category samples span 2008, 2009, 2010, 2012, 2013 and 2016. Archived official ClickBank feeds supplied additional 2017 and 2022 observations. Vendor activation dates and tracker “First Seen” dates were not substituted for capture years.

Seller domains were resolved primarily from the `CBRehoppp2` target embedded in saved CDX original URLs under `<vendor>.hop.clickbank.net`, and secondarily from explicit affiliate-resource URLs in feed descriptions. One final domain came from the saved Location header of an archived hop, fetched with redirects disabled. This inspects the archived redirect destination without requesting the seller page. Targets were URL-decoded, never inferred from product titles. Tracking parameters are retained. Redirect destinations are historical metadata and need Phase 2 confirmation. If two rows share an evidenced domain, the later row is marked `DUPLICATE DOMAIN`. The concurrent candidates-B.tsv was checked without editing it; Baby Sleep Miracle is marked as a cross-list duplicate.

What did not work: the ClickBank 2008 index was a static category navigator with no product names; its exact marketplace.htm URL had no 2014–2020 records. CBTrends’ old numerical category IDs were reused for finance categories; those were not treated as parenting evidence. The fetched 2010 Kids URL rendered “Home” and unrelated products. CB-Analytics’ encoded category captures returned broad/default listings or empty categories, and the exact SIGNBABY product lookup returned no records. JVZoo 2014/2019 launch lists and the WarriorForum 2010 affiliate database were populated but contained no useful niche offers. Broad product-index and some hop CDX queries returned 503s/timeouts; failed queries are distinguished from successful empty listings below. No fetched page was classified as a JavaScript-only product app.

The official feeds have **no structured seller-URL field**. Only a few descriptions supply URLs. Their original ZIP payloads are preserved as `.txt.zip`; exact XML members were extracted locally as `clickbank-feed-2017-v1.xml`, `clickbank-feed-2022-v1.xml` and `clickbank-feed-2022-v2.xml`. Use those XML files for title/description evidence: the initial normalized feed `.txt` conversion stripped CDATA. The original capture text and ZIPs were left unchanged. The two 2022 feed formats largely duplicate the same products and were not counted twice.

The helper gained optional request logging/cap, HTTPS selection, link/raw/header sidecars, CDX collapse/filter/status options, ZIP/XML handling and `fetch --no-redirect`. Defaults remain compatible. The final hop-index sweep used one attempt per lookup to protect the remaining budget. Empty prices mean no consumer price was evidenced; research-tool membership fees, commission percentages and affiliate earnings were excluded.

Excluded or kept outside the candidate queue: Kidzgrow tracking software (format mismatch); GeniusMaker software/age uncertainty; Eye Can Too! Read (Pre-K–grade 8); generic school reading/spelling materials; prenatal intelligence offers; non-English products; fertility, gender selection, breastfeeding, baby names, baby showers and generic parenting. Early Educators Resources targets classrooms rather than mothers; CoordiKids lacks baby-age/format evidence. Toddler Speech Delay is retained only as explicitly therapeutic adjacent, outside Mamivio claim lines.

Ten priorities for Phase 2, ranked as hypotheses about long-form selling potential. None is yet confirmed to meet the ≥1,200-word/price-or-buy-CTA definition:

| rank | candidate | seller domain / status | why prioritize | discovery evidence |
|---|---|---|---|---|
| 1 | A Practical Guide To Baby Milestones | babydevelopmentnews.com | Direct baby-skill guide; strong core topic and benefit-led offer. | `cbengine-parenting-2013.txt` |
| 2 | Raising Smarter Babies - How To Raise Smart, ... | unresolved; recorded hop retained | Historical baby-brain offer with a direct-parent title; format still needs checking. | `cbengine-parenting-2008.txt` |
| 3 | Your Child Development System | unresolved; recorded hop retained | Twelve-month parent membership and a developed mechanism imply room for an extended pitch. | `cbengine-parenting-page2-2013.txt` |
| 4 | Baby Can Read | unresolved; recorded hop retained | Explicit ebook and named Glenn Doman method; early-learning adjacent. | `cbengine-parenting-2013.txt` |
| 5 | Sign Language For Babies And Beyond! | signing4babies.com | Parent pre-verbal communication offer with 250-sign video package. | `cbengine-education-late-2016.txt` |
| 6 | Discover How Baby Sign Language Can Help You? | unresolved; recorded hop retained | Explicit step-by-step parent ebook with a clear before-speech promise. | `cbengine-education-late-2016.txt` |
| 7 | Mommy Jingles Musical Parenting Program | mommyjingles.com | Multi-format music/learning offer with demos, reminder cards, lyrics and audio. | `cbengine-parenting-late-2016.txt` |
| 8 | Teach Baby To Swim | teachbabytoswim.info | Specific parent how-to outcome; listing advertises an engaging sales page. | `cbengine-parenting-late-2016.txt` |
| 9 | How To Help Your Child Learn To Talk Better In Everyday Activities | helpyourchildspeak.com | Explicit parent book, everyday mechanism and an evidenced seller URL; exact baby ages unverified. | `cbengine-education-late-2016.txt` |
| 10 | How To Develop Your Childs Genius | all-gifted-children.com | Historical brain-development title and an evidenced seller URL; infant fit and format still need checking. | `cbengine-education-2012.txt` |

Fetched captures (one ledger row each; all `letter? = no`). Names below are relative to `_raw/sales-letters/_discovery/`. Navigation, affiliate copy and raw-feed words are not sales-letter word counts.

42 fetches saved: HTTP 200: 39, HTTP 301: 2, HTTP 302: 1.

| capture file | timestamp | HTTP | helper words | source URL |
|---|---|---|---|---|
| `cbanalytics-categories-2008.txt` | 20080106092247 | 200 | 127 | http://www.cb-analytics.com:80/category.php |
| `cbanalytics-family-2008.txt` | 20080212084042 | 200 | 500 | http://www.cb-analytics.com:80/category.php?name=%7CHome+%26+Family |
| `cbanalytics-family-2010.txt` | 20100102031852 | 200 | 933 | http://cb-analytics.com/category.php?name=%7CHome+%26+Family |
| `cbanalytics-index-2008.txt` | 20080104185526 | 200 | 447 | http://www.cb-analytics.com:80/ |
| `cbanalytics-parenting-2008.txt` | 20080410213711 | 200 | 484 | http://www.cb-analytics.com:80/category.php?name=%7CHome+%26+Family%7CParenting&param=&start=1 |
| `cbanalytics-parenting-2010.txt` | 20100128015345 | 200 | 120 | http://cb-analytics.com:80/category.php?name=%7CHome+%26+Family%7CParenting&param=&start=1 |
| `cbengine-categories-2008.txt` | 20080604164521 | 200 | 489 | http://cbengine.com:80/res/clickbank_cats.cfm |
| `cbengine-categories-2014.txt` | 20140108184330 | 200 | 1317 | http://cbengine.com:80/res/clickbank_cats.cfm |
| `cbengine-detail-d3w1r35s.txt` | 20111120091103 | 200 | 523 | http://cbengine.com/clickbank/d3w1r35s-a-practical-guide-to-baby-milestones |
| `cbengine-detail-signbaby.txt` | 20120626170020 | 200 | 484 | http://www.cbengine.com:80/id/signbaby |
| `cbengine-education-2008.txt` | 20080508234153 | 200 | 676 | http://www.cbengine.com:80/res/search.cfm?cat=family.students |
| `cbengine-education-2012.txt` | 20120101025651 | 200 | 956 | http://www.cbengine.com:80/res/search.cfm?cat=family.students |
| `cbengine-education-late-2016.txt` | 20160104231339 | 200 | 1599 | http://www.cbengine.com:80/res/search.cfm?cat=family.students |
| `cbengine-index-2008.txt` | 20080514210309 | 200 | 557 | http://www.cbengine.com/ |
| `cbengine-kids-2008.txt` | 20080508234141 | 200 | 679 | http://www.cbengine.com:80/res/search.cfm?cat=family.kids |
| `cbengine-kids-2010.txt` | 20100102103535 | 200 | 857 | http://cbengine.com/res/search.cfm?cat=family.kids |
| `cbengine-parenting-2008.txt` | 20080511031603 | 200 | 691 | http://www.cbengine.com:80/res/search.cfm?cat=family.parenting |
| `cbengine-parenting-2010.txt` | 20100102050126 | 200 | 854 | http://www.cbengine.com:80/res/search.cfm?cat=family.parenting |
| `cbengine-parenting-2013.txt` | 20130116093019 | 200 | 2415 | http://www.cbengine.com/res/search.cfm?cat=family.parenting |
| `cbengine-parenting-late-2016.txt` | 20160104233513 | 200 | 1985 | http://www.cbengine.com:80/res/search.cfm?cat=family.parenting |
| `cbengine-parenting-page2-2009.txt` | 20091126035718 | 200 | 838 | http://www.cbengine.com:80/res/search.cfm?cat=family.parenting&pg=2 |
| `cbengine-parenting-page2-2013.txt` | 20130204135817 | 200 | 1771 | http://www.cbengine.com/res/search.cfm?cat=family.parenting&pg=2 |
| `cbengine-pregnancy-2010.txt` | 20100205124731 | 200 | 885 | http://www.cbengine.com:80/res/search.cfm?cat=family.pregnancy |
| `cbengine-pregnancy-2013.txt` | 20130116093005 | 200 | 2552 | http://www.cbengine.com/res/search.cfm?cat=family.pregnancy |
| `cbengine-signlanguage-2010.txt` | 20100205131802 | 200 | 384 | http://www.cbengine.com:80/res/search.cfm?cat=language.sign |
| `cbengine-signlanguage-2013.txt` | 20130109151615 | 200 | 458 | http://www.cbengine.com:80/res/search.cfm?cat=language.sign |
| `cbengine-specialneeds-2010.txt` | 20100205141824 | 200 | 496 | http://www.cbengine.com:80/res/search.cfm?cat=family.specialneeds |
| `cbengine-specialneeds-2013.txt` | 20130116092412 | 200 | 1152 | http://www.cbengine.com/res/search.cfm?cat=family.specialneeds |
| `cbtrends-browse-2008.txt` | 20080410114559 | 200 | 331 | http://www.cbtrends.com:80/browse-clickbank-marketplace.html |
| `cbtrends-browse-later-2013.txt` | 20130114095653 | 200 | 1305 | http://www.cbtrends.com/browse-clickbank-marketplace.html |
| `cbtrends-index-2008.txt` | 20080409210641 | 200 | 470 | http://www.cbtrends.com:80/ |
| `cbtrends-kids-2010.txt` | 20100123032327 | 200 | 803 | http://www.cbtrends.com:80/browse-clickbank-marketplace/22/24/Home+&+Family+-%3E+Kids/1/gravity |
| `clickbank-feed-2017-v1.txt` | 20170711053012 | 200 | 125468 | https://accounts.clickbank.com/feeds/marketplace_feed_v1.xml.zip |
| `clickbank-feed-2022-v1.txt` | 20220629161141 | 200 | 60569 | https://accounts.clickbank.com/feeds/marketplace_feed_v1.xml.zip |
| `clickbank-feed-2022-v2.txt` | 20220611031327 | 200 | 66043 | https://accounts.clickbank.com/feeds/marketplace_feed_v2.xml.zip |
| `clickbank-index-2008.txt` | 20080706133455 | 200 | 588 | http://www.clickbank.com/marketplace |
| `hop-d3w1r35s.txt` | 20111120085241 | 302 | 9 | http://cbengine.com/visit/d3w1r35s |
| `hopdomain-prd123-header.txt` | 20121124224433 | 301 | 0 | http://cyberzoo.prd123.hop.clickbank.net/ |
| `hopdomain-signbaby.txt` | 20061206050616 | 301 | 0 | http://0.signbaby.hop.clickbank.net:80/? |
| `jvzoo-marketplace-2014.txt` | 20140802124342 | 200 | 950 | http://www.jvzoo.com/marketplace |
| `jvzoo-marketplace-2019.txt` | 20190824032716 | 200 | 939 | https://www.jvzoo.com/marketplace |
| `warriorforum-affiliates-2010.txt` | 20101101202207 | 200 | 685 | http://www.warriorforum.com:80/affiliate-program-database/ |

CDX listing inventory. “Empty” means HTTP 200 with zero returned records; “failed” means a transport/server failure, not proof of absent captures. Each file preserves the returned index rows.

| CDX file | rows | result / capture-year range |
|---|---|---|
| `cbanalytics-categories.cdx.tsv` | 40 | records; 2008–2008 |
| `cbanalytics-family.cdx.tsv` | 28 | records; 2008–2013 |
| `cbanalytics-parenting.cdx.tsv` | 17 | records; 2008–2010 |
| `cbanalytics-root.cdx.tsv` | 40 | records; 2008–2008 |
| `cbanalytics-signbaby.cdx.tsv` | 0 | empty (HTTP 200) |
| `cbengine-categories-later.cdx.tsv` | 40 | records; 2014–2014 |
| `cbengine-categories.cdx.tsv` | 40 | records; 2008–2010 |
| `cbengine-detail-d3w1r35s.cdx.tsv` | 1 | records; 2011–2011 |
| `cbengine-detail-signbaby-id.cdx.tsv` | 24 | records; 2012–2015 |
| `cbengine-detail-signbaby.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `cbengine-education-late.cdx.tsv` | 40 | records; 2016–2016 |
| `cbengine-education.cdx.tsv` | 40 | records; 2008–2014 |
| `cbengine-kids.cdx.tsv` | 14 | records; 2008–2010 |
| `cbengine-parenting-late.cdx.tsv` | 40 | records; 2016–2016 |
| `cbengine-parenting-page2.cdx.tsv` | 10 | records; 2009–2015 |
| `cbengine-parenting.cdx.tsv` | 40 | records; 2008–2013 |
| `cbengine-pregnancy.cdx.tsv` | 40 | records; 2010–2014 |
| `cbengine-product-detail-index.cdx.tsv` | 0 | failed (transport timeout/error) |
| `cbengine-root.cdx.tsv` | 40 | records; 2008–2009 |
| `cbengine-signlanguage.cdx.tsv` | 40 | records; 2010–2014 |
| `cbengine-specialneeds.cdx.tsv` | 40 | records; 2010–2014 |
| `cbtrends-browse-later.cdx.tsv` | 40 | records; 2013–2014 |
| `cbtrends-browse.cdx.tsv` | 40 | records; 2008–2009 |
| `cbtrends-kids-prefix.cdx.tsv` | 40 | records; 2009–2019 |
| `cbtrends-parenting-prefix.cdx.tsv` | 40 | records; 2011–2020 |
| `cbtrends-root.cdx.tsv` | 40 | records; 2008–2009 |
| `cdx-clickbank-marketplace-https.tsv` | 2 | records; 2008–2008 |
| `cdx-clickbank-marketplace.tsv` | 2 | records; 2008–2008 |
| `clickbank-account-feeds.cdx.tsv` | 3 | records; 2017–2022 |
| `clickbank-feed-prefix.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `clickbank-index-later.cdx.tsv` | 0 | empty (HTTP 200) |
| `clickbank-marketplace-htm.cdx.tsv` | 40 | records; 2008–2009 |
| `clickbank-marketplace-prefix.cdx.tsv` | 40 | records; 2008–2009 |
| `d3w1r35s-clickbank-hop.cdx.tsv` | 0 | empty (HTTP 200) |
| `hop-d3w1r35s.cdx.tsv` | 2 | records; 2011–2012 |
| `hop-signbaby.cdx.tsv` | 0 | empty (HTTP 200) |
| `hopdomain-d3w1r35s.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-signbaby.cdx.tsv` | 40 | records; 2006–2022 |
| `hopdomain-targets-angelsong7.cdx.tsv` | 9 | records; 2014–2020 |
| `hopdomain-targets-babyswim.cdx.tsv` | 7 | records; 2015–2020 |
| `hopdomain-targets-d3w1r35s.cdx.tsv` | 19 | records; 2011–2022 |
| `hopdomain-targets-figueiredo.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-targets-lifemusic.cdx.tsv` | 40 | records; 2013–2022 |
| `hopdomain-targets-marekjc.cdx.tsv` | 0 | failed (transport timeout/error) |
| `hopdomain-targets-maxteiner2.cdx.tsv` | 11 | records; 2013–2014 |
| `hopdomain-targets-mibtt.cdx.tsv` | 0 | failed (transport timeout/error) |
| `hopdomain-targets-mserv.cdx.tsv` | 40 | records; 2011–2022 |
| `hopdomain-targets-nokomisllc.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-targets-pedisales1.cdx.tsv` | 0 | failed (transport timeout/error) |
| `hopdomain-targets-prd123.cdx.tsv` | 1 | records; 2012–2012 |
| `hopdomain-targets-qandrews02.cdx.tsv` | 40 | records; 2007–2022 |
| `hopdomain-targets-sleepbaby.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-targets-smoutmedia.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-targets-speakebook.cdx.tsv` | 33 | records; 2013–2022 |
| `hopdomain-targets-speechbrg.cdx.tsv` | 9 | records; 2019–2022 |
| `hopdomain-targets-sustab.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `hopdomain-targets-ycds1.cdx.tsv` | 0 | failed (HTTP 503; helper exhausted retries) |
| `jvzoo-marketplace-later.cdx.tsv` | 4 | records; 2019–2020 |
| `jvzoo-marketplace.cdx.tsv` | 40 | records; 2014–2014 |
| `warriorforum-affiliates.cdx.tsv` | 40 | records; 2010–2011 |

Local validation passed: the TSV has the required eight columns and 28 distinct offer rows; every cited source exists; all 14 resolved domains match saved CDX, XML or redirect-header evidence; extracted XML members match the original ZIP bytes; and all 42 capture HTTP/word counts and `letter? = no` values match their ledger rows. An independent evidence review checked vendor associations, capture years and resolved URLs. The helper passed Python syntax validation.

Coverage not reached: additional affiliate-directory sites and dedicated clickbank-marketplace-style domains were not fetched; the remaining request budget was used for product-domain resolution.

Limits for the next phase: unresolved domains are genuine unfinished redirect chains, not guessed seller addresses. A named listing proves a product was listed, not that it sold. Descriptions of conversions, guarantees, outcomes and claimed effectiveness were recorded as sellers’ wording, not verified findings. Phase 2 should confirm format, English-language page, baby-age applicability and qualifying letter length, and preserve any out-of-lines wording for tagging rather than reuse.
