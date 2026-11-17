# usage: python3 -I embedded.py <html> <out.txt> <source-url>
# Saves human-readable text found in embedded JSON/props of a saved HTML file (verbatim, unescaped).
import sys,re,json,html as H,datetime
src,out,url=sys.argv[1:4]
s=open(src,encoding='utf-8',errors='replace').read()
seen=[];
def add(t):
    t=H.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t).strip()
    if len(t)>=8 and re.search(r'[A-Za-z]{3,} [A-Za-z]{2,}',t) and t not in seen: seen.append(t)
for m in re.finditer(r'"((?:[^"\\]|\\.){8,4000})"',s):
    raw=m.group(1)
    try: t=json.loads('"'+raw+'"')
    except Exception: continue
    if re.search(r'(function|=>|\{|\}|;base64|https?://|\.css|\.js\b|class=)',re.sub(r'<[^>]+>','',t)): continue
    add(t)
open(out,'w',encoding='utf-8').write(f"SOURCE: {url}\nFINAL: text embedded in saved HTML {src.split('/')[-1]}\nHTTP: 200  FETCHED: {datetime.date.today()}\nTITLE: embedded strings\n"+"-"*70+"\n"+"\n".join(seen)+"\n")
print(len(seen))
