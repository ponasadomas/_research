"""Phase 1B: sequential CDX only; all archive access delegated to wayback.py."""
import json, os, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
LOG=ROOT/'sales-letters/logs'
plan=json.loads((LOG/'p1b-query-plan.json').read_text())
state_path=LOG/'p1b-query-results.json'
state=json.loads(state_path.read_text()) if state_path.exists() else []
done={x['domain'] for x in state}
route=int(sys.argv[1])
env=dict(os.environ, WAYBACK_SCHEME='https', WAYBACK_REQUEST_LOG=str(LOG/'p1b-wayback-requests.jsonl'),WAYBACK_REQUEST_CAP='96')
for item in plan:
    if item['route']!=route or item['domain'] in done: continue
    used=sum(json.loads(s).get('event') in ('request','redirect') for s in (LOG/'p1b-wayback-requests.jsonl').read_text().splitlines() if s.strip())
    if used>=96: print('AUDIT CAP reached',flush=True); break
    seq=len(state)+1
    base=LOG/'p1b-cdx'/f"{seq:03d}-{re.sub(r'[^A-Za-z0-9.-]','_',item['domain'])}"
    cmd=['python3','-I','_tools/wayback.py','cdx',item.get('query',item['domain']),'--from','2008','--to','2024','--limit','30','--collapse','timestamp:4']
    with base.with_suffix(base.suffix+'.tsv').open('w') as out, base.with_suffix(base.suffix+'.stderr').open('w') as err:
        result=subprocess.run(cmd,cwd=ROOT,env=env,stdout=out,stderr=err)
    lines=base.with_suffix(base.suffix+'.tsv').read_text().splitlines()
    captures=[]
    for line in lines:
        fields=line.split('\t')
        if len(fields)==5 and re.fullmatch(r'\d{14}',fields[0]): captures.append(dict(zip(['timestamp','original','statuscode','mimetype','length'],fields)))
    entry=dict(item,command=cmd,captures=captures,exit_code=result.returncode,cdx_file=str(base.with_suffix(base.suffix+'.tsv').relative_to(ROOT)),stderr_file=str(base.with_suffix(base.suffix+'.stderr').relative_to(ROOT)))
    state.append(entry)
    state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
    done.add(item['domain'])
    years=sorted(set(c['timestamp'][:4] for c in captures))
    print(f"{seq:02d} route {route} {item['domain']}: {len(captures)} captures, {'-'.join([years[0],years[-1]]) if years else 'NONE'}",flush=True)
    if result.returncode: print('STOP: helper returned nonzero; inspect audit/errors',flush=True); break
