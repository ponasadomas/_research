#!/usr/bin/env python3
"""Check that every quote in voice/*.jsonl really appears in the raw file it cites.

A quote may be trimmed with " […] "; each piece must be found, in order, in raw_file
(only whitespace and HTML entities are normalised; case and punctuation are exact). Run from anywhere:

    python3 verify_quotes.py            # all files
    python3 verify_quotes.py voice/x.jsonl
"""
import json, sys, os, re, glob, html, gzip

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REQUIRED = ["id", "source", "url", "speaker", "stage", "type", "themes", "quote", "context", "raw_file"]
_cache = {}
_structured = {}


def norm(s):
    # Compare original spelling, case and punctuation. Only decode entities and
    # normalize whitespace so extraction line wrapping does not change a quote.
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()


def raw(path):
    if path not in _cache:
        full = os.path.join(ROOT, path)
        _cache[path] = norm(open(full, encoding="utf-8", errors="replace").read()) if os.path.exists(full) else None
    return _cache[path]


def strings(value):
    """Decode stored JSON strings without changing their spelling/punctuation."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def source_text(q):
    path = q['raw_file']
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        return None
    if path.endswith('.jsonl.gz'):
        # A compressed archive is not a text file. Match the native submission,
        # never an unrelated post elsewhere in the same archive.
        if path not in _structured:
            with gzip.open(full, 'rt', encoding='utf-8') as stream:
                _structured[path] = {str(row['id']): row for line in stream
                                     if line.strip() for row in [json.loads(line)]}
        native = q.get('post_id') or q.get('unit_id')
        match = re.search(r'/comments/([^/]+)', q.get('url', ''))
        native = native or (match[1] if match else None)
        row = _structured[path].get(str(native))
        if row is None:
            return ''
        return norm(row.get('title', '') + '\n\n' + row.get('selftext', ''))
    if path.endswith('.json'):
        if path not in _structured:
            with open(full, encoding='utf-8') as stream:
                _structured[path] = json.load(stream)
        data = _structured[path]
        if isinstance(data, dict) and isinstance(data.get('posts'), list) and q.get('post_id'):
            wanted = set(map(str, q.get('post_ids') or [q['post_id']]))
            posts = [post for post in data['posts']
                     if str(post.get('post_id')) in wanted]
            title = data.get('title', '') if any(post.get('role') == 'original_post' for post in posts) else ''
            return norm(title + '\n' + '\n'.join(post.get('body', '') for post in posts))
        # Older records may cite the serialized capture itself. Preserve that
        # representation too; decoded values cover quotes with JSON escapes.
        return raw(path) + '\n' + norm('\n'.join(strings(data)))
    if path.endswith('.jsonl') and q.get('evidence_kind') == 'listing_excerpt':
        if path not in _structured:
            with open(full, encoding='utf-8') as stream:
                _structured[path] = [json.loads(line) for line in stream if line.strip()]
        native = str(q.get('thread_id') or q.get('unit_id') or '').removeprefix('mse-').removeprefix('geo-')
        records = [row for row in _structured[path]
                   if str(row.get('discussion_id', row.get('thread_id', row.get('id', '')))) == native]
        return norm('\n'.join(strings(records)))
    return raw(path)


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "voice", "*.jsonl")))
    total = bad = 0
    for f in files:
        fbad = n = 0
        for i, line in enumerate(open(f), 1):
            if not line.strip():
                continue
            n += 1
            try:
                q = json.loads(line)
            except Exception as e:
                print(f"{f}:{i} invalid JSON ({e})"); fbad += 1; continue
            missing = [k for k in REQUIRED if k not in q]
            if missing:
                print(f"{f}:{i} missing {missing}"); fbad += 1; continue
            text = source_text(q)
            if text is None:
                print(f"{f}:{i} raw_file not found: {q['raw_file']}"); fbad += 1; continue
            pos = 0
            for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q["quote"]):
                piece = norm(piece)
                if not piece:
                    continue
                at = text.find(piece, pos)
                if at < 0:
                    print(f"{f}:{i} {q['id']} NOT IN SOURCE: {piece[:90]!r}"); fbad += 1; break
                pos = at + len(piece)
        print(f"{os.path.basename(f)}: {n} quotes, {fbad} failed")
        total += n; bad += fbad
    print(f"TOTAL {total} quotes, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
