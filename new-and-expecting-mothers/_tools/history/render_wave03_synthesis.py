#!/usr/bin/env python3
"""Render the completed research wave from independently reconciled counts."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];C=json.loads((R/'synthesis/counts.json').read_text());V=json.loads((R/'synthesis/coverage.json').read_text());fmt=lambda n:f'{n:,}'
assert C['total']==sum(C['source_class'].values()) and V['all_reddit_full_original_post_ids_distinct']==6605 and V['reddit_purchase_extension']['unread_keeps']==0
head=f'''# Mamivio findings — report purchases and niche evidence

Compiled 2026-10-25; source capture dates remain as recorded, mostly 2026-10-24 UTC. **Sleep has the strongest observed paid-tailoring evidence; capability-matched play and specialist leave planning are the next contenders. Food remains a hypothesis. No standalone-report niche is validated by this evidence.** [Ranked comparison](niche-opportunities.md) · [Purchase audit](purchase-evidence.md).

The database contains **{fmt(C['total'])} exact-source excerpts**, **{C['total']-1944} added after the 1,944-record committed baseline**, and **{fmt(C['language_bank_entries'])} distinct language-bank entries**. There are {fmt(C['original_user_community_records'])} original user/community excerpts. Research records what people actually say and do, in their own words, whatever the subject. The owner decides later what to use in copy; no subject is withheld from research. Counts describe selected records, not people, prevalence, independent purchasers or sales. [Counts](counts.md) · [Audit](audit.md) · [Session ledger](session-report.md).

| Source class | Selected excerpts |
|---|---:|
'''
head+=''.join(f'| {k} | {fmt(v)} |\n' for k,v in C['source_class'].items())
head+='''
Full reading comprises **6,605 distinct archived Reddit posts + 2,150 identifiable OP replies + 43 exact other comments; 605 complete visible forum discussions; 119 complete saved Q&A threads; 299 original app/book reviews**. The Reddit total is 6,476 in the main nine-community H2 window, 122 in the separate two-community commercial extension, and seven targeted 2021–2024 originals. Fifteen forum discussions have explicit partial safety boundaries. Seller evidence is separate: 73 public offer/pricing/terms page reads across 55 competitor notes, with newly counted hosted testimonials and an affiliate article recorded independently from original buyers. Every retained assigned original in this wave is fully read; broader card-drop/unmatched/source gaps remain.

**How to read this:** `[id]` identifies the JSONL record returned by `_tools/query.py --id ID`. Quotations are verbatim; connecting prose and rankings are interpretation. Source classes, unknown payment status, service bundles and provenance remain visible; historical eligibility fields have no effect. Reported purchases are self-reports without receipts; an offer, subscription access, seller testimonial or hypothetical price is a different observation. The focused sleep extension is intentionally enriched, so quote counts cannot compare market payment rates. The owner selected English-speaking markets and supplied no customer data; no launch country, conversion, acquisition cost or report profitability has been established.

'''
(R/'synthesis/findings.md').write_text(head+(R/'_tools/templates/findings-wave03-body.md').read_text())
p=R/'README.md';old=p.read_text();tail=old[old.index('## Layout and evidence rules'):]
prefix=f'''# Mamivio — global mother-and-baby research database

**State on 2026-10-25: completed and audited this finite research wave; broader research gaps remain.** All four owner-confirmed tasks were pursued: actual report/plan purchases, a fair challenge of the full niche shortlist, all 847 prepared country candidates and every retained original, and competitor/buyer-review gaps plus a ranked recommendation. No product, pilot, recruitment, outreach, accounts or purchases were created.

**Research conclusion:** sleep leads on observed paid tailoring; capability-matched play and specialist leave remain contenders. Food remains a hypothesis. Photo-based childproofing is an additional, thinner report-format contender. No standalone-report niche or price is validated. [Ranked recommendation](synthesis/niche-opportunities.md) · [What parents bought/accessed/considered](synthesis/purchase-evidence.md) · [Findings](synthesis/findings.md).

**{fmt(C['total'])} exact-source excerpts across 10 classes; {fmt(C['language_bank_entries'])} distinct language-bank entries; every stored record included.** The {C['total']-1944}-record increment follows commit34ec30af's 1,944-record baseline. Counts are selected records, not people, independent buyers, prevalence or sales. There are {fmt(C['original_user_community_records'])} original user/community excerpts, 155 legacy search extracts, 67 competitor/resource/hosted/affiliate excerpts, six advertising and ten official-guidance excerpts.

Cumulative full reading: **6,605 distinct Reddit post IDs + 2,150 identifiable OP replies + 43 other comments; 605 complete visible forum discussions; 119 complete saved Q&A threads; 299 original reviews**. Country wave: 847 cards → 584 full keeps, zero unread keeps; commercial extension: 391 cards → 122 full keeps, zero unread keeps. Reinspections and five duplicate-only originals are explicitly separated. [Session ledger](synthesis/session-report.md) · [Country/filter comparison](synthesis/country-comparison-wave03.md) · [Coverage](synthesis/coverage.json).

Main nine-community unread bodies: **2,531 A / 50,530 B / 38,463 C**, plus 14,665 unavailable; 145,386 available comments remain unread and seven comment files are absent. Current exact inventories: `_raw/reddit-deep/wave03-v1/`. The two-community extension separately has **14,966 readable bodies unread** (269 card drops + 14,697 unmatched), 138 unavailable and both comment files absent; exact inventories `_raw/report-purchase-archive-wave03/final-v1/`. Seven targeted 2021–2024 post reads are separate from both H2 windows. No full live-thread completion is claimed.

Seller coverage now includes **55 notes and 73 complete public offer/pricing/terms pages**, plus a complete affiliate article, 22 newly counted hosted testimonials and one process illustration; one external review preview is partial. These are not independent buyer reviews or verified sales. [Source map](sources/source-map.md) · [Competitors](competitors/README.md) · [Language bank](synthesis/quote-index.md) · [Reader notes](synthesis/reader-notes.md) · [Audit](synthesis/audit.md).

All committed baseline voice/raw inventories remain unchanged. Earlier food-first product/pilot recommendations are withdrawn; prior synthesis is preserved under `_raw/audit/wave03-2026-10-24/baseline34ec30af/` and in git. The final audit corrected one Premium-access account's overstated payment classification; verbatim text/raw remained unchanged. [Correction log](_raw/audit/wave03-2026-10-24/semantic-corrections.json).

'''
(R/'README.md').write_text(prefix+tail)
