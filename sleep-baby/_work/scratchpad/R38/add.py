import json, sys, os, re
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
VOICE = os.path.join(BASE, 'voice', 'reddit-r38.jsonl')
units = {os.path.basename(l.split('\t')[1].strip())[:-4]: l.split('\t')[1].strip() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'units.tsv'))}
n = sum(1 for l in open(VOICE) if l.strip()) if os.path.exists(VOICE) else 0
out = open(VOICE, 'a')
for line in open(sys.argv[1]):
    if not line.strip(): continue
    r = json.loads(line)
    rf = units[r['u']]
    text = open(os.path.join(BASE, rf)).read()
    m = re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', text, re.M)
    pid, sub, date, url = m.groups()
    rec_url, rec_date = url, date
    c = r.get('c')
    if c:
        mc = re.search(r'^COMMENT ' + re.escape(c) + r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', text, re.M)
        rec_date, rec_url = mc.groups()
    n += 1
    rec = {"id": "sb38-%04d" % n, "source": "reddit r/" + sub, "url": rec_url, "date": rec_date,
           "speaker": r['sp'], "stage": r['st'], "type": r['t'], "themes": r['th'], "quote": r['q'],
           "context": r['cx'], "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
    if c: rec["comment_id"] = c
    if r.get('r'): open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'restricted.txt'),'a').write(rec['id']+'\t'+r['r']+'\n')
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(rec['id'], r['u'], len(r['cx'].split()))
