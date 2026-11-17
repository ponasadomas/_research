import json,re,os,sys
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
rx=re.compile(r'[$£€]\s?\d|\d\s?[$£€]|\d\s?(k|K)\b|\d+\s?(dollars|pounds|euros|bucks|quid|usd)|thousands? of|hundreds of|\bthousands\b|\bhundreds\b|refund|money back|scam|waste of money|rip.?off|expensive|afford|\$\$|copay|deposit|cost|paycheck|tuition|surcharge|charg|price|\bpaid\b|\bpay\b|waitlist|\d{3,}',re.I)
n=0
for l in open(os.path.join(ROOT,'voice-merged','all.jsonl'),encoding='utf-8'):
    if not l.strip(): continue
    r=json.loads(l)
    if not re.match(r'tb(1[89]|2\d)-',r['id']): continue
    if rx.search(r['quote']) or r['type'] in ('purchase','price_signal'):
        n+=1
        print(r['id'],'R' if r.get('restricted') else '-',r['type'],'|',r['quote'][:300].replace('\n',' '))
print('records',n,file=sys.stderr)
