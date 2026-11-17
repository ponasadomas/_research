#!/usr/bin/env python3
"""Adapted SYD local metadata renderer; performs no network requests.
Usage: yt_top_table.py <meta.tsv> <queries.txt> <out.md> [N]
Columns: id, views, upload_date, comment_count, channel, title.
Only use an allowed, provenance-documented and manually classified candidate pool.
"""
import datetime,sys
meta,qf,out=sys.argv[1:4]
cap=int(sys.argv[4]) if len(sys.argv)>4 else 200
rows={};unknown=0
for line in open(meta,encoding='utf-8'):
    p=line.rstrip('\n').split('\t')
    if len(p)<6:continue
    if not p[1].isdigit():unknown+=1;continue
    r=(int(p[1]),p[0],p[2],p[3],p[4],'\t'.join(p[5:]))
    if p[0] not in rows or r[0]>rows[p[0]][0]:rows[p[0]]=r
ranked=sorted(rows.values(),reverse=True)
esc=lambda x:x.replace('|','\\|')
with open(out,'w',encoding='utf-8') as f:
    f.write('# YouTube — observed views within the supplied candidate pool\n\n')
    f.write(f'Rendered {datetime.date.today()}; {len(ranked)} unique ids with numeric view counts; {unknown} rows lacked a numeric count. ')
    f.write('Counts and dates are only those in the supplied saved metadata; rendering does not refresh them. ')
    f.write('This is not a census, proof of current popularity, medical validation or a profitability measure. ')
    f.write('Videos/transcripts/comments count as read only in a separate reading ledger.\n\n')
    f.write('On-topic classification must concern a documented mother/parent planning problem: ordinary play, first solids, work/feeding handoff, postpartum household support, sleep or pregnancy activity. ')
    f.write('State every collection restriction, candidate-selection rule and excluded item in the source note.\n\n## Executed queries from supplied log\n\n')
    for q in open(qf,encoding='utf-8'):
        if q.strip():f.write(f'- `{q.strip()}`\n')
    f.write(f'\n## {min(cap,len(ranked))} observed entries\n\n| Rank | Views | Title | Channel | Uploaded | Comments | Link |\n|---|---:|---|---|---|---|---|\n')
    for i,(views,id,up,cc,ch,title) in enumerate(ranked[:cap],1):
        up=f'{up[:4]}-{up[4:6]}-{up[6:]}' if len(up)==8 and up.isdigit() else ''
        f.write(f'| {i} | {views:,} | {esc(title)} | {esc(ch)} | {up} | {cc} | https://www.youtube.com/watch?v={id} |\n')
