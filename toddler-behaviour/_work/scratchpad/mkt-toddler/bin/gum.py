import sys,re,html,json
s=open(sys.argv[1]).read()
d=json.loads(html.unescape(re.search(r'data-page="([^"]*)"',s).group(1)))['props']['product']
print(d['name'],'|',d['seller']['name'],'|',d['currency_code'],d['price_cents'],'| ratings',d['ratings']['count'],d['ratings']['average'],'| sales',d.get('sales_count'))
print('SUMMARY:',d.get('summary'))
print('ATTR:',d.get('attributes'))
print('OPTIONS:',[(o.get('name'),o.get('price_difference_cents')) for o in (d.get('options') or [])])
print(re.sub(r'<[^>]+>',' ',d['description_html'])[:2500])
