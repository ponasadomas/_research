"""Rebuild the Phase 1B report from frozen discovery evidence; no network."""
import csv,json
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[2]; logs=root/'sales-letters/logs'
results=json.loads((logs/'p1b-query-results.json').read_text())
by_domain={r['domain']:r for r in results}
positive=[r for r in results if r['captures']]
negative=[r for r in results if not r['captures']]
audit=[json.loads(line) for line in (logs/'p1b-wayback-requests.jsonl').read_text().splitlines() if line.strip()]
requests=sum(a.get('event') in ('request','redirect') for a in audit)
counts=Counter(r['topic'] for r in positive)
post=[r for r in positive if min(c['timestamp'][:4] for c in r['captures'])>'2022']
core=[r for r in positive if r['topic'] not in ('other','landing-page-only') and min(c['timestamp'][:4] for c in r['captures'])<='2022']
top=[
('brightestbeginning.com','20220926061658','Core development; strong page-specific lead','Exact Play, Develop, Thrive sales path exists in 2022. The current search-indexed seller page presents a paid 0–12-month programme and a 30-day refund. [Seller source](https://brightestbeginning.com/courses/play-develop-thrive/).'),
('babypillars.com','20160504183614','Core development; strong product-domain lead','0–24-month development video programme; early homepage capture is a useful first version to inspect. Current seller index shows a paid programme and annual-plan refund, not historical proof. [Seller source](https://www.babypillars.com/).'),
('childrenlearningreading.com','20150102045337','Adjacent older-child reading; strong hypothesis','Known reading info-product domain with multiple pre-2023 captures. The 2015 original URL is preserved exactly, including port and query marker. Offer/letter identity is still untested.'),
('babysignlanguage.com','20210419062700','Adjacent infant signing; strong page-specific lead','Exact full-screen kit-sales path captured in 2021; current indexed seller copy includes a satisfaction/refund promise. Physical/video hybrid, so format must be checked. [Seller source](https://babysignlanguage.com/basic-full-screen/).'),
('readingheadstart.com','20190118035236','Adjacent age-2+ reading; strong hypothesis','ClickBank reading offer named in the seed research. This is an actual 2019 homepage record, not an invented timestamp for a guessed product path. [Seed](../../competitors/README.md).'),
('babysleepmiracle.com','20170101164901','Sleep-adjacent; text/VSL ambiguity','ClickBank ebook/guide in the existing sleep research. Inspect this older root before the smaller later roots; a VSL wrapper remains possible. [Seed](../../../sleep-baby/competitors/baby-sleep-miracle.md).'),
('sleepbabysleep.com','20120103223147','Sleep-adjacent; promising older ebook lead','Seller search index explicitly identifies an ebook and a 30-day refund; many old homepage captures are available. The index crawl is old, not a new live-page inspection. [Seller source](https://www.sleepbabysleep.com/).'),
('activebabiessmartkids.com.au','20160101144840','Core development; exploratory','Historical infant movement/early-stimulation programme domain; 2016 root is a first discovery fetch. No specific sales path, price or guarantee has been verified.'),
('milestonesandmotherhood.com','20220414165451','Core milestones; exploratory','Known parent masterclass seller with a 2022 homepage capture. Fetch to locate historical course links; the homepage itself may be a short landing page. [Current course index](https://www.milestonesandmotherhood.com/courses).'),
('brillkids.com','20110113193546','Adjacent infant reading/math/music; exploratory','Little Reader/Little Math seller domain captured in 2011. Use the homepage to discover product sales links; it may be a catalogue rather than a letter.')]
lines=[
'# Phase 1B — seeds, historical brands and web-search candidates',
'',
'Run date: 2026-11-03. Discovery only; no archived pages fetched and no live sales pages opened or scraped.',
'',
f'**Result:** {len(positive)} CDX-backed candidate rows in [candidates-B.tsv](../candidates-B.tsv), from {len(results)} unique domain/seller-host queries. {len(core)} topical candidates have at least one successful capture in 2008–2022; this verifies archive presence, not that their named offer or a qualifying letter existed then. {len(negative)} queries returned no matching captures. No row is yet confirmed to meet the ≥1,200-word letter definition.',
'',
'## Method and coverage',
'',
'1. Read [sales-letter rules](../README.md), [development competitor index](../../competitors/README.md) and its linked seller notes, [sleep competitor index](../../../sleep-baby/competitors/README.md), [global competitor index](../../../global/competitors/README.md), and [sub-niche map §0](../../../main/synthesis/sub-niche-map.md). A background researcher traced the sleep/global sellers to the existing first-party capture notes; its [inventory](p1b-seed-inventory.md) records service and topic exclusions.',
'2. Queried the seed sellers first, including broader document/course references as `other`. Then checked recalled historical brands, then used live search queries and checked newly discovered domains or exact product URLs. Repeated sellers were deduplicated by domain; a separate hosted sales domain is distinguishable from a parent seller domain.',
'3. Every archive request went through `python3 -I _tools/wayback.py cdx`, with `--from 2008 --to 2024 --limit 30`. Queries ran sequentially, using the helper’s shared four-second throttle. There were no `fetch` commands, archive page opens, or alternative archive APIs.',
'4. Except for the first Baby Acrobatics query, added the backward-compatible helper option `--collapse timestamp:4`, retaining one successful capture per calendar year instead of the first 30 distinct digests. This prevents the row limit from truncating later years. All queries use exact matching: homepages for ordinary domains, and seller-specific URLs for selected hosted/product pages. None returned 30 rows.',
'5. `first_capture` and `last_capture` mean the first/last **HTTP-200 capture years of the queried URL within 2008–2024**, not the domain’s first-ever/last-ever capture, product launch or sales dates. The requested command does not cover 2005–2007. A homepage query does not establish the capture history of a guessed product path or every URL on that domain.',
'6. All retained names have a positive saved CDX result. App/subscription and physical-product landing references are explicitly separated from prospective letters. Current 2026 prices and refund language are dated leads, not historical observations. No archived headlines, claims, price or guarantee are quoted.',
'',
'## Request accounting',
'',
f'- **{len(results)} CDX invocations**: one initial successful query plus {requests} instrumented HTTP requests. The initial invocation preceded request instrumentation; its saved stdout is [001-babyacrobatics.com.tsv](p1b-cdx/001-babyacrobatics.com.tsv), and it emitted no retry diagnostic. Its transport redirects were not logged, so the nominal total is 97 and three requests were left unused as budget reserve.',
f'- Instrumented audit: {requests} request events, {sum(a.get("event")=="response" for a in audit)} response events, all HTTP 200; {sum(a.get("event")=="redirect" for a in audit)} redirects and {sum(a.get("event")=="error" for a in audit)} errors. There were no retry attempts in the audit. [HTTP audit](p1b-wayback-requests.jsonl).',
'- **0 archive page fetches; 0 live sales-page fetches.** Live web research used 20 search queries in five batches. Search-indexed text was used for lead discovery; it was not saved or represented as an archived capture. [Search ledger](p1b-web-searches.json).',
'- Reproducible evidence: [query plan](p1b-query-plan.json), [results with exact timestamp/original-URL pairs](p1b-query-results.json), and individual CDX TSV/stderr files in [p1b-cdx/](p1b-cdx/).',
'',
'| Route | Queries | Positive rows | No matching captures |',
'|---|---:|---:|---:|']
for route,name in [(1,'Existing research seeds'),(2,'Brand recall'),(3,'Web-search leads')]:
 r=[x for x in results if x['route']==route];n=sum(bool(x['captures']) for x in r)
 lines.append(f'| {name} | {len(r)} | {n} | {len(r)-n} |')
lines += ['', '| Topic | Positive rows |','|---|---:|']
for topic in ['development','play','milestones','early-learning','sleep-adjacent','landing-page-only','other']:
 lines.append(f'| {topic} | {counts[topic]} |')
lines += [
'',
'## Ten first-fetch priorities',
'',
'These are editorial priorities, not ten validated letters. Every timestamp and exact original URL below is copied from a saved CDX row and falls within 2008–2022. The timestamp belongs to the URL shown, not automatically to `likely_sales_url`. Ranks 8–10 are weaker seller-discovery entries. CDX `length` is an archive-record byte length and was never treated as a word count. Phase 2 must confirm one page, headline, body word count, price/buy CTA, guarantee, language and historical product identity.',
'',
'| Rank | Candidate | First-fetch timestamp | Exact captured original URL | Fit / confidence | Why inspect it | CDX evidence |',
'|---:|---|---|---|---|---|---|']
for rank,(domain,ts,fit,why) in enumerate(top,1):
 r=by_domain[domain];c=next(c for c in r['captures'] if c['timestamp']==ts)
 evidence=Path(r['cdx_file']).relative_to('sales-letters/logs')
 lines.append(f'| {rank} | {r["product_name"]} | `{ts}` | `{c["original"]}` | {fit} | {why} | [CDX]({evidence}) |')
lines += [
'',
'The preferred fetch syntax is `python3 -I _tools/wayback.py fetch <timestamp> <exact-original-URL> --out <raw-file>`, but **none was executed in Phase 1B**. Catalogue/blog homepages may first reveal a better historical sales path; that later lookup belongs to Phase 2.',
'',
'## Dead ends and limitations',
'',
'All no-result queries below returned HTTP 200 with no matching HTTP-200 captures for the exact queried URL in the chosen window. This is not proof that the seller never existed, that a parent host had no captures, or that a differently spelled/path/versioned URL was not archived. No alternate-path retry was made, preserving the one-query-per-domain rule.',
'',
'| Route | Domain / seller host | Exact query target | Evidence |',
'|---|---|---|---|']
for r in negative:
 evidence=Path(r['cdx_file']).relative_to('sales-letters/logs')
 lines.append(f'| {r["route"]} | `{r["domain"]}` | `{r.get("query",r["domain"])}` | [CDX stderr]({str(evidence).replace(".tsv",".stderr")}) |')
lines += [
'',
'**Only post-2022 captures returned:** '+', '.join('`'+x['domain']+'`' for x in post)+'. These are retained as clearly labelled later leads, not counted among the 42 topical pre-2023 candidates.',
'',
'**Captured, not letter:** Kinedu, BabySparks and Lovevery early landing pages, Monti Kids and The Wonder Weeks are `landing-page-only`. Baby Einstein and Genius Babies are `other` physical-product/catalogue references. Videos/DVDs/flashcard kits can still have long-form selling pages, but the products themselves are not written info products.',
'',
'**Scope controls:** the source indexes contain feeding books, maternity/registry planners, written consultation bundles, local classes and professional training. Broader seed sellers were checked and labelled `other` or explicitly described as human-service bundles; they are not used to substantiate the development/early-learning letter shortlist. Lithuanian/Hungarian Pirmi/Elso references returned no captures and do not enter the English candidate TSV. Exercise-only app memberships, free public guidance and pure app-store listings were not converted into document sellers.',
'',
'**Web-search dead ends:** JVZoo/Warrior queries mostly yielded general niche discussion or unrelated material, with no additional named historical baby-development offer suitable for this shortlist. Milestone-ebook searches included 2023/2025 retail titles, which do not establish 2005–2022 sales letters. Generic “smart baby” results included CPR software, insurance programmes and apps; those were discarded. The October 2015 [MySmartBaby advertisement](https://jfwonline.com/emag/JFWOct2015.pdf) supplied a genuine historical domain lead, but its archived homepage identity and letter format still need inspection.',
'',
'**Unqueried follow-ups:** current Kinedu ebook host `courses.kinedu.com/ebook-landing`, the Strength in Words legacy domain, Therapy Stars and Movement Lesson appeared during discovery but were not given additional queries after the selected ten web leads. The Kinedu seller itself was already checked as a landing-page seed; this does not verify its ebook subdomain. Search-only names lacking traceable domains (Dorothy Waide, Jessie Martin, Heidi Holvoet, Asleep in 12 in the original notes) remain unresolved, rather than guessed into the verified TSV.',
'',
'**What remains for Phase 2:** fetch the exact captured URLs above, save raw text, and reject short landings, blogs, catalogues, VSL-only shells, unrelated historical owners and post-window offer launches. Confirm prices and guarantees from the historical page itself. Archive presence proves existence of an archived URL, never sales, revenue, conversions, efficacy, or that the current offer existed in that year.',
'']
(logs/'p1b-report.md').write_text('\n'.join(lines))
print(f'Wrote report with {len(top)} backed first-fetch targets, {len(negative)} no-result domains and {len(post)} post-window leads.')
