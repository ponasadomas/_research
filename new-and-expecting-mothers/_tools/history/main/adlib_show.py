import json,sys,datetime,collections
d=json.load(open(sys.argv[1]))
print("count:",d.get("count"),"| ads parsed:",len(d["ads"]))
pc=collections.Counter(a["page_name"] for a in d["ads"])
for p,c in pc.most_common(12):
    a=[x for x in d["ads"] if x["page_name"]==p]
    sd=min(int(x["start_date"]) for x in a if x["start_date"]) if any(x["start_date"] for x in a) else None
    print(f"  {c:2d} {p} (pid {a[0]['page_id']}) since {datetime.date.fromtimestamp(sd) if sd else '?'} active={a[0]['is_active']} | {(a[0]['title'] or '')[:60]} | {(a[0]['link_url'] or '')[:70]}")
if not d["ads"]: print(d["visible_text"][:600])
