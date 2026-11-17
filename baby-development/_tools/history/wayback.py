#!/usr/bin/env python3
"""Throttled Wayback Machine helper. ALL agents must use this; never call web.archive.org any other way.

  python3 -I _tools/wayback.py cdx  <url> [--from 2008] [--to 2020] [--limit 50] [--match prefix|exact|domain]
  python3 -I _tools/wayback.py fetch <timestamp> <url> --out <path.txt>      # raw id_ capture -> text with header
  python3 -I _tools/wayback.py text  <file.html>                            # html -> text

Rate limit: one request every 4 s process-wide (lock file), exponential backoff on 429/5xx, 6 tries.
"""
import sys, time, re, html, json, os, argparse, fcntl, urllib.request, urllib.parse, urllib.error, io, zipfile, gzip
from html.parser import HTMLParser

LOCK = '/tmp/wayback.lock'
MIN_GAP = 4.0
UA = 'mamivio-research-wayback/1.0 (archive study; contact via github)'
SCHEME = os.environ.get('WAYBACK_SCHEME', 'http')

def _request_event(url, **fields):
    path = os.environ.get('WAYBACK_REQUEST_LOG')
    if path:
        cap = int(os.environ.get('WAYBACK_REQUEST_CAP', '0'))
        if cap and fields.get('event') in ('request', 'redirect') and os.path.exists(path):
            with open(path) as f:
                used = sum(json.loads(line).get('event') in ('request', 'redirect') for line in f if line.strip())
            if used >= cap:
                raise SystemExit(f'Wayback request cap reached ({used}/{cap})')
        with open(path, 'a') as f:
            f.write(json.dumps({'url': url, **fields}) + '\n')

class ArchiveRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urllib.parse.urlsplit(newurl).hostname != 'web.archive.org':
            raise urllib.error.HTTPError(req.full_url, code, 'External redirect blocked', headers, fp)
        _throttle()
        _request_event(newurl, event='redirect', status=code)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

OPENER = urllib.request.build_opener(ArchiveRedirect())

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

NO_REDIRECT_OPENER = urllib.request.build_opener(NoRedirect())

def _throttle():
    fd = os.open(LOCK, os.O_RDWR | os.O_CREAT, 0o666)
    fcntl.flock(fd, fcntl.LOCK_EX)
    try:
        try: last = float(os.read(fd, 64).decode() or 0)
        except ValueError: last = 0
        wait = MIN_GAP - (time.time() - last)
        if wait > 0: time.sleep(wait)
        os.lseek(fd, 0, 0); os.ftruncate(fd, 0); os.write(fd, str(time.time()).encode())
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN); os.close(fd)

def get(url, tries=None, follow_redirects=True, headers_out=None):
    tries = tries if tries is not None else int(os.environ.get('WAYBACK_TRIES', '6'))
    delay = 8
    for i in range(tries):
        _throttle()
        _request_event(url, event='request', attempt=i + 1)
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        try:
            opener = OPENER if follow_redirects else NO_REDIRECT_OPENER
            with opener.open(req, timeout=int(os.environ.get('WAYBACK_TIMEOUT', '60'))) as r:
                if headers_out is not None: headers_out.update(dict(r.headers))
                _request_event(url, event='response', status=r.status)
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if headers_out is not None: headers_out.update(dict(e.headers))
            _request_event(url, event='response', status=e.code)
            if 300 <= e.code < 400 and not follow_redirects: return e.code, e.read()
            if e.code in (404, 403): return e.code, b''
            if e.code in (429, 500, 502, 503, 504):
                sys.stderr.write(f'[wayback] {e.code} on {url}; sleeping {delay}s\n'); time.sleep(delay); delay = min(delay*2, 120); continue
            return e.code, b''
        except Exception as e:
            _request_event(url, event='error', detail=str(e))
            sys.stderr.write(f'[wayback] {e}; retry\n'); time.sleep(delay); delay = min(delay*2, 120)
    return 0, b''

def cdx(url, frm=None, to=None, limit=50, match='exact', collapse='digest', filters=None, status='200'):
    q = {'url': url, 'output': 'json', 'fl': 'timestamp,original,statuscode,mimetype,length',
         'collapse': collapse, 'limit': str(limit)}
    query_filters = ([] if status == 'any' else ['statuscode:' + status]) + (filters or [])
    if query_filters: q['filter'] = query_filters
    if match != 'exact': q['matchType'] = match
    if frm: q['from'] = str(frm)
    if to: q['to'] = str(to)
    code, body = get(SCHEME + '://web.archive.org/cdx/search/cdx?' + urllib.parse.urlencode(q, doseq=True))
    print(f'[wayback] CDX HTTP {code}: {url}', file=sys.stderr)
    if code != 200 or not body: return []
    rows = json.loads(body)
    return [dict(zip(rows[0], r)) for r in rows[1:]]

def to_text(raw):
    if isinstance(raw, bytes) and raw.startswith(b'\x1f\x8b'):
        raw = gzip.decompress(raw)
    if isinstance(raw, bytes) and raw.startswith(b'PK\x03\x04'):
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            raw = b'\n'.join(archive.read(name) for name in archive.namelist() if name.lower().endswith('.xml'))
    t = raw.decode('utf-8', errors='ignore') if isinstance(raw, bytes) else raw
    t = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', t, flags=re.S)
    t = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<br\s*/?>|</(p|div|h\d|li|tr|section|article|header|footer)>', '\n', t, flags=re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t\r\f\v]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n\n', t)
    return t.strip()

def fetch(ts, url, out, no_redirect=False):
    wb = f'{SCHEME}://web.archive.org/web/{ts}id_/{url}'
    headers = {}
    code, body = get(wb, follow_redirects=not no_redirect, headers_out=headers)
    txt = to_text(body) if body else ''
    words = len(txt.split())
    header = f'SOURCE: {url}\nWAYBACK: {wb}\nTIMESTAMP: {ts}\nHTTP: {code}\nFETCHED: {time.strftime("%Y-%m-%d")}\nWORDS: {words}\n' + '-'*70 + '\n'
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    open(out, 'w').write(header + txt)
    with open(out + '.headers.json', 'w') as f:
        json.dump(headers, f, indent=2)
    if body:
        with open(out + ('.zip' if body.startswith(b'PK\x03\x04') else '.html'), 'wb') as f:
            f.write(body)
        class Links(HTMLParser):
            def __init__(self):
                super().__init__(); self.links = []
            def handle_starttag(self, tag, attrs):
                values = dict(attrs)
                if tag.lower() == 'a' and values.get('href'):
                    self.links.append(values['href'])
        link_body = gzip.decompress(body) if body.startswith(b'\x1f\x8b') else body
        links = Links(); links.feed(link_body.decode('utf-8', errors='ignore'))
        with open(out + '.links.json', 'w') as f:
            json.dump({'source': url, 'timestamp': ts, 'hrefs': links.links}, f, indent=2)
    print(f'{code} {words} words -> {out}')
    return code, words

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('cdx'); a.add_argument('url'); a.add_argument('--from', dest='frm'); a.add_argument('--to'); a.add_argument('--limit', type=int, default=50); a.add_argument('--match', default='exact'); a.add_argument('--collapse', default='digest')
    a.add_argument('--filter', action='append', default=[]); a.add_argument('--status', default='200')
    b = sub.add_parser('fetch'); b.add_argument('ts'); b.add_argument('url'); b.add_argument('--out', required=True)
    b.add_argument('--no-redirect', action='store_true', help='Save a hop response and its headers without following its target')
    c = sub.add_parser('text'); c.add_argument('file')
    ns = ap.parse_args()
    if ns.cmd == 'cdx':
        for r in cdx(ns.url, ns.frm, ns.to, ns.limit, ns.match, ns.collapse, ns.filter, ns.status): print('\t'.join(r.get(k, '') for k in ('timestamp', 'original', 'statuscode', 'mimetype', 'length')))
    elif ns.cmd == 'fetch': fetch(ns.ts, ns.url, ns.out, ns.no_redirect)
    else: print(to_text(open(ns.file, 'rb').read()))
