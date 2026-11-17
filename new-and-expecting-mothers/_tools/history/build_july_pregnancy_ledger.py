#!/usr/bin/env python3
"""Reconcile this isolated human-read cohort into source ledgers without touching global counts."""
from pathlib import Path
import csv,json,collections
r=Path(__file__).resolve().parents[1];d=r/'scratchpad/reddit-july-pregnancy';tri=list(csv.DictReader((r/'_raw/reddit-deep/triage/july-pregnancy.tsv').open(),delimiter='\t'));out={x['post_id']:x for x in map(json.loads,(r/'sources/reddit-july-pregnancy-fullread-outcomes.jsonl').read_text().splitlines())};qs=[json.loads(x) for x in (r/'voice/reddit-july-pregnancy.jsonl').read_text().splitlines()];idx={x['post_id']:x for x in map(json.loads,(r/'_raw/reddit-deep/july-2025-wave-v1/primary-index.jsonl').read_text().splitlines())};qby=collections.defaultdict(list)
for x in qs:qby[x['post_id']].append(x['id'])
fields=['post_id','subreddit','date','human_card_label','card_reason','full_original_read','final_status','full_read_reason','quote_ids','quote_outcome','read_scope','comments_available','OP_followups_available','raw_file','sha256','url'];rows=[]
for t in tri:
 i=t['post_id'];u=idx[i];o=out.get(i);rows.append(dict(zip(fields,[i,u['subreddit'],u['post_date'],t['label'],t['reason'],bool(o),o['final_status'] if o else 'drop_at_card',o['reason'] if o else '',','.join(qby[i]),'quoted' if qby[i] else ('read_not_quoted' if o and o['final_status']=='retain' else 'excluded_no_quote'),'full_post' if o else 'card_only',False,False,u['raw_file'],u['sha256'],u['url']])))
p=r/'sources/reddit-july-pregnancy-per-id.tsv'
with p.open('w') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
s=json.loads((r/'synthesis/reddit-july-pregnancy-verification.json').read_text())['stats'];counts=collections.Counter((x['subreddit'],x['final_status']) for x in rows)
text='''# July2025 Reddit pregnancy and preparation cohort

Completed2026-10-24. This is a frozen archive reading wave, not a live Reddit harvest or a market-prevalence sample. All495 assigned calendar-July tier-A cards in BabyBumps, BabyBumpsCanada and BabyBumpsandBeyondAu were read and individually triaged. Exact IDs match the nine assigned card files; no ranking or top-N cap. The artifact/tool regex that produced tierA already selects for planning language, so job frequencies cannot estimate population demand.

Human triage dropped222 cards and retained273 complete archived originals. All273 originals were read in17 frozen groups. Full-body review excluded32 more;241 retained originals are fully read,0 retained originals unread. Forty-two excerpts were selected from42 retained posts; distinct authors/people are not verified. The posts are not complete live threads: no comment archive exists for these three communities at this pinned publisher version, so0 comments/OP follow-ups are claimed read. Linked images, spreadsheets, videos and external pages were not fetched in this reading-only assignment; in particular birth-template images at1mcap52 remain unread. Reported native comment counts are metadata, not comments inspected.

## Exact reconciliation

| Community | Assigned cards | Card drops | Provisional originals read | Post-read drops | Final retained/read |
|---|---:|---:|---:|---:|---:|
'''
for com in ['BabyBumps','BabyBumpsCanada','BabyBumpsandBeyondAu']:
 rr=[x for x in rows if x['subreddit']==com];card=sum(x['final_status']=='drop_at_card' for x in rr);dropped=sum(x['final_status']=='drop' for x in rr);ret=sum(x['final_status']=='retain' for x in rr);text+=f'| {com} | {len(rr)} | {card} | {len(rr)-card} | {dropped} | {ret} |\n'
text+='''| **Total** | **495** | **222** | **273** | **32** | **241** |

The [per-ID ledger](reddit-july-pregnancy-per-id.tsv) records all495 card decisions, full-original read status, final reason, quote IDs/outcomes, exact source path/hash and URL. The [273 full-read outcomes](reddit-july-pregnancy-fullread-outcomes.jsonl) preserve the human post-level decisions. Read-but-unquoted retained posts remain in the corpus; no claim is made that every retained post supplies a useful or independent quotation.

## Provenance and permissions limits

The original packet is [_raw/reddit-deep/july-2025-wave-v1](../_raw/reddit-deep/july-2025-wave-v1/), from public ungated HuggingFace dataset `yikeee/reddit-subreddits25`, pinned commit `ea497c510aa68765c07ed744ec9f84d68bbedf7f`. Source records retain post IDs, native URLs/dates and the compressed source-file path. Publisher license is described as “other”; provenance/reuse rights and archive-to-live completeness remain unresolved. Public availability does not establish commercial reuse permission. No live Reddit wall, login, captcha, policy route or private material was bypassed. No new network requests were made for this wave. See [shared archive provenance](reddit-deep.md) and the packet README for the acquisition route and remaining queues.

The whole archive window was inventoried by the producing pipeline, but this child assignment covers only the495 July tier-A cards in these three communities. Other communities, August–December tierA and tierB/C are outside this completion claim. All dropped cards are card-only unless individually listed as full-read; their archived bodies still exist without a claim of human reading.

## What was excluded after reading

Historically, thirty-two complete originals were excluded for mixed subject, scope, duplicate and provenance reasons; those frozen outcomes are recorded below. Research records what people actually say and do, in their own words, whatever the subject. The owner decides later what to use in copy; no subject is withheld from research. Exact neutral reasons are per-ID. Several source cards concealed these issues. Rapid duplicate families include repeated maternity-return, second-shower, costume and alternative-shower posts; identical bodies are not independent voices. A repeated Welcome Baby feature/testimonial cluster across both BabyBumps and Australia was excluded because independent authenticity could not be established, without asserting fraud or affiliation as fact. A Wonderbly referral recommendation was excluded from independent buyer evidence. The unnamed alleged personalized-goods scam did not document a first-person purchase and was not counted as one.

## Reading and verification artifacts

- [Human triage file](../_raw/reddit-deep/triage/july-pregnancy.tsv) and [nine card-read hashes](../scratchpad/reddit-july-pregnancy/triage-reading-ledger.jsonl).
- [Frozen273-unit keep manifest](../scratchpad/reddit-july-pregnancy/kept-manifest.json), [17 full-read records](../scratchpad/reddit-july-pregnancy/fullreading-ledger.jsonl), [lossless reading-view hashes](../scratchpad/reddit-july-pregnancy/fulltext-views-manifest.json). Original title/body/follow-up availability text is unchanged; only repeated packet JSON metadata is omitted in the convenience views.
- [Reusable cohort brief](../_tools/brief-reddit-july-pregnancy.md) and [full-reading brief](../_tools/brief-reddit-july-pregnancy-fullreads.md).
- [Voice file](../voice/reddit-july-pregnancy.jsonl), prefix `rjpg01-`; README vocabulary only, context at most21words. Gestational detail remains separate when an early/late category would require an unspecified boundary.
- [Strict verification](../synthesis/reddit-july-pregnancy-verification.json):42 quotes,0 failures. Exact own-body text, metadata, raw/view/chunk hashes, ID sets, per-ID outcomes and README enums all checked. Ordinary `_tools/verify_quotes.py` also passes42/0.
- [Reader notes](../synthesis/reader-notes-reddit-july-pregnancy.md) separate conditional app interest, actual goods spending, service use, failed expensive services, freebies and missing report-payment evidence.

No report purchase, paid-report conversion, accepted report price or commercial niche validation is established. Source excerpts are research evidence, not authorization to reuse personal stories in advertising. All source claims remain attributed with their country context. Research retains every subject in the speaker’s own words. The owner decides later what goes in copy; historical eligibility never restricts research.
'''

for _old,_new in {'July2025':'July 2025','Completed2026':'Completed 2026','All495':'All 495','dropped222':'dropped 222','retained273':'retained 273','All273':'All 273','in17':'in 17','excluded32':'excluded 32',';241':'; 241',',0':', 0','all495':'all 495','all273':'all 273','nine assigned':'nine assigned','Forty-two excerpts':'Forty-two excerpts','prefix `rjpg01-`':'prefix `rjpg01-`','most21words':'most 21 words','273-unit':'273-unit','Thirty-two complete':'Thirty-two complete',':42':': 42',',0 failures':', 0 failures','passes42/0':'passes 42/0','Exact495':'Exact 495','no-clinical-instruction':'clinical instruction','from42':'from 42','so0':'so 0','at1mcap52':'at `1mcap52`','the495':'the 495','Frozen273':'Frozen 273'}.items(): text=text.replace(_old,_new)
(r/'sources/reddit-july-pregnancy.md').write_text(text);print('Wrote495-row per-ID ledger and source summary.')
