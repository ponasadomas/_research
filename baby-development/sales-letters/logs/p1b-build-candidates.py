"""Build the requested candidate TSV only from frozen positive CDX results."""
import csv, json
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[2]
logs=root/'sales-letters/logs'
results=json.loads((logs/'p1b-query-results.json').read_text())
columns=['domain','product_name','topic','first_capture','last_capture','lead_source','likely_sales_url','price_if_known','note']
rows=[]
for item in results:
    captures=item['captures']
    if not captures: continue
    years=sorted({c['timestamp'][:4] for c in captures})
    note=item.get('note','')
    # A domain is not proof that a current course existed in the archived year.
    notes=[note] if note else []
    if item['topic']=='other':
        notes.append('Broad seed/reference only; excluded from the topical letter shortlist.')
    if item['topic']=='landing-page-only':
        notes.append('Captured, not letter; retained as a landing-page reference.')
    notes.append('CDX verifies queried URL/domain only; offer identity, historical price, >=1200 words and guarantee unverified.')
    if years[0]>'2022': notes.append('All returned captures are after 2022; outside target sales years.')
    if len(captures)>=30: notes.append('30-row cap reached: first/last years are sampled, not complete coverage.')
    notes.append('CDX evidence: '+item['cdx_file'])
    if item.get('query'): notes.append('Queried exact seller/product URL: '+item['query'])
    row={k:item.get(k,'') for k in columns}
    row.update(first_capture=years[0],last_capture=years[-1],note=' '.join(notes))
    rows.append(row)
with (root/'sales-letters/candidates-B.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=columns,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(queried=len(results),verified_rows=len(rows),by_topic=dict(Counter(r['topic'] for r in rows)),empty=[i['domain'] for i in results if not i['captures']]),indent=2))
