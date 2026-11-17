#!/usr/bin/env python3
"""Extract the checklist sentences from the saved CDC HTML (offline, stdlib only)."""

import csv
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw/cdc"
AGES = [(2, "2mo"), (4, "4mo"), (6, "6mo"), (9, "9mo"),
        (12, "1yr"), (15, "15mo"), (18, "18mo"), (24, "2yr"),
        (30, "30mo"), (36, "3yr"), (48, "4yr")]
DOMAINS = {"Social/Emotional": "SE", "Language/Communication": "LC",
           "Cognitive": "CO", "Movement/Physical": "MP"}


class ChecklistParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active = False
        self.domain = None
        self.heading = None
        self.heading_text = []
        self.item = None
        self.anchor = ""
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("h2", "h3"):
            self.heading = tag
            self.heading_text = []
        if tag == "li" and self.active and self.domain:
            assert self.item is None, "Unexpected nested checklist item"
            self.item = []
            self.anchor = ""
        if tag == "a" and self.item is not None:
            self.anchor = attrs.get("href", "")

    def handle_data(self, data):
        if self.heading:
            self.heading_text.append(data)
        if self.item is not None:
            self.item.append(data)

    def handle_endtag(self, tag):
        if tag == self.heading:
            heading = " ".join("".join(self.heading_text).split())
            if tag == "h2":
                self.active = heading.lower().startswith("what most ")
                self.domain = None
            elif self.active:
                self.domain = next((d for d in DOMAINS if heading.startswith(d)), None)
            self.heading = None
            self.heading_text = []
        if tag == "li" and self.item is not None:
            sentence = " ".join("".join(self.item).split())
            self.rows.append((self.domain, sentence, self.anchor))
            self.item = None


def extract():
    fetches = {r["slug"]: r for r in json.loads((RAW / "legacy-fetch-manifest.json").read_text())}
    rows, manifest = [], []
    for age, slug in AGES:
        path = RAW / ("15mo.html" if slug == "15mo" else f"legacy-{slug}.html")
        url = ("https://www.cdc.gov/act-early/milestones/15-months.html" if slug == "15mo"
               else fetches[slug]["status_and_effective_url"].split(" ", 1)[1])
        parser = ChecklistParser()
        parser.feed(path.read_text())
        counts = {d: 0 for d in DOMAINS}
        for domain, sentence, anchor in parser.rows:
            counts[domain] += 1
            rows.append({"cdc_id": f"CDC-{age:02d}-{DOMAINS[domain]}-{counts[domain]:02d}",
                         "age_months": age, "domain": domain, "milestone": sentence,
                         "source_url": url + anchor, "source_file": str(path.relative_to(ROOT))})
        assert all(counts.values()), (age, counts)
        assert 10 <= len(parser.rows) <= 30, (age, len(parser.rows))
        manifest.append({"age_months": age, "source_url": url,
                         "source_file": str(path.relative_to(ROOT)),
                         "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                         "milestone_count": len(parser.rows), "domains": counts})
    with (RAW / "cdc-milestones.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (RAW / "checklist-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    for m in manifest:
        print(m["age_months"], m["milestone_count"], m["domains"])
    print("Total:", len(rows))


if __name__ == "__main__":
    extract()
