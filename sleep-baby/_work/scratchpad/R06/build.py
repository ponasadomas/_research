# usage: build.py input.jsonl output.jsonl  (input lines: u, sp, st, ty, th, q, c)
import json, re, sys, html, os
NICHE='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby'
def norm(s): return re.sub(r"\s+"," ",html.unescape(s)).strip()
out=[]; n=0
for line in open(sys.argv[1]):
    if not line.strip(): continue
    r=json.loads(line); n+=1
    rf=f"../_shared/_raw/reddit-2026/units/{r['u']}.txt"
    text=open(os.path.join(NICHE,rf),encoding='utf-8').read()
    first=norm(re.split(r"\s*\[(?:…|\.\.\.)\]\s*", r['q'])[0])
    # find header position: iterate blocks
    blocks=[]
    for m in re.finditer(r'^(POST|COMMENT) (\S+) \| (?:r/(\S+) \| )?(\d{4}-\d\d-\d\d) [^|]*\| (\S+)', text, re.M):
        blocks.append((m.start(), m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))
    found=None
    for i,b in enumerate(blocks):
        end=blocks[i+1][0] if i+1<len(blocks) else len(text)
        if first in norm(text[b[0]:end]): found=b; break
    if not found: print('NOTFOUND', n, r['u'], first[:60]); continue
    post=blocks[0]
    rec={"id":f"sb06-{len(out)+1:04d}","source":f"reddit r/{post[3]}","url":found[5],"date":found[4],
         "speaker":r['sp'],"stage":r['st'],"type":r['ty'],"themes":r['th'],"quote":r['q'],"context":r['c'],
         "raw_file":rf,"source_class":"reddit_archive","post_id":post[2]}
    if found[1]=='COMMENT': rec['comment_id']=found[2]
    if len(r['c'].split())>25: print('LONGCTX',n)
    out.append(rec)
with open(sys.argv[2],'w') as f:
    for x in out: f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(len(out),'written')
