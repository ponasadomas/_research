#!/usr/bin/env python3
"""Fetch a web page with a browser User-Agent and save its visible text.

    python3 -I fetch_page.py <name> <url> [--dir competitors]

Writes  _raw/<dir>/_html/<name>.html  (as served) and  _raw/<dir>/<name>.txt  (extracted text).
The .txt starts with a 3-line header (URL, final URL, HTTP status, fetch date) and keeps light
structure markers so quotes can be located: "# "/"## "/"### " for h1-h3 (h4-h6 -> "#### "),
"- " for list items, "[img alt: ...]" for image alt text, "[iframe: ...]"/"[video: ...]" for embeds.
Stdlib only; pages are treated as data, nothing in them is executed.
"""
import sys, os, re, subprocess, datetime, html
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_raw")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")
SKIP = {"script", "style", "noscript", "svg", "template", "head"}
BLOCK = {"p", "div", "br", "tr", "table", "section", "article", "header", "footer", "ul", "ol",
         "blockquote", "form", "nav", "main", "aside", "figure", "figcaption", "hr", "td", "th",
         "option", "button", "label", "dt", "dd", "center", "pre"}
HEAD = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "#### ", "h6": "#### "}


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.title, self.in_title = [], 0, "", False
        self.meta = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            k = a.get("name") or a.get("property") or ""
            if k.lower() in ("description", "og:title", "og:description") and a.get("content"):
                self.meta.append(f"[meta {k}: {a['content'].strip()}]")
        if tag in SKIP and tag != "head":
            self.skip += 1
            return
        if self.skip:
            return
        if tag in HEAD:
            self.out.append("\n\n" + HEAD[tag])
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in BLOCK:
            self.out.append("\n")
        elif tag == "img" and (a.get("alt") or "").strip():
            self.out.append(f" [img alt: {a['alt'].strip()}] ")
        elif tag in ("iframe", "video", "source", "embed") and (a.get("src") or a.get("data-src")):
            self.out.append(f"\n[{tag}: {a.get('src') or a.get('data-src')}]\n")
        elif tag == "input" and a.get("type") in ("submit", "button") and a.get("value"):
            self.out.append(f"\n[button: {a['value']}]\n")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in SKIP and tag != "head":
            self.skip = max(0, self.skip - 1)
            return
        if not self.skip and (tag in HEAD or tag in BLOCK or tag == "li"):
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif not self.skip:
            self.out.append(data)


def extract(raw_html):
    p = Text()
    try:
        p.feed(raw_html)
    except Exception as e:  # malformed markup: keep what we have
        p.out.append(f"\n[parser stopped: {e}]\n")
    t = "".join(p.out).replace("\xa0", " ").replace("\r", "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n(#+ |- )\n+", r"\n\1", t)      # marker glued to its text
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return p.title.strip(), p.meta, t


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sub = "competitors"
    if "--dir" in sys.argv:
        sub = sys.argv[sys.argv.index("--dir") + 1]
        args = [a for a in args if a != sub]
    name, url = args[0], args[1]
    d = os.path.join(ROOT, sub)
    os.makedirs(d, exist_ok=True)
    os.makedirs(os.path.join(d, "_html"), exist_ok=True)
    hpath, tpath = os.path.join(d, "_html", name + ".html"), os.path.join(d, name + ".txt")
    r = subprocess.run(["curl", "-sS", "-L", "--compressed", "--max-time", "40", "-A", UA,
                        "-H", "Accept-Language: en-US,en;q=0.9",
                        "-H", "Accept: text/html,application/xhtml+xml,*/*;q=0.8",
                        "-o", hpath, "-w", "%{http_code} %{url_effective}", url],
                       capture_output=True, text=True)
    status = r.stdout.strip() or ("ERR " + r.stderr.strip())
    raw = open(hpath, encoding="utf-8", errors="replace").read() if os.path.exists(hpath) else ""
    title, meta, text = extract(raw)
    code, _, final = status.partition(" ")
    with open(tpath, "w", encoding="utf-8") as f:
        f.write(f"SOURCE: {url}\nFINAL: {final}\nHTTP: {code}  FETCHED: {datetime.date.today()}\n"
                f"TITLE: {title}\n" + "\n".join(meta) + "\n" + "-" * 70 + "\n" + text + "\n")
    print(f"{name}: http {code} | {len(raw)} bytes html | {len(text.split())} words | {title[:70]}")


if __name__ == "__main__":
    main()
