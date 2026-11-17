#!/usr/bin/env python3
"""Build offline indexes and comparisons from the saved Chrome MCP evidence.

This does not make network requests or interact with the browser.
"""

import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw/browser"
API = ROOT / "raw/api/browser"


def read_json(path):
    return json.loads(path.read_text())


def dump(name, value):
    (RAW / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def body_file(run, reqid, kind):
    for ext in ("json", "body"):
        path = API / f"{run}-{reqid}.{kind}.{ext}"
        if path.exists():
            return path
    return None


def relative(path):
    return str(path.relative_to(ROOT)) if path else None


def network_entry(run, reqid, method, url, status):
    entry = {"run": run, "reqid": reqid, "method": method,
             "listed_url": url, "status": status}
    meta = RAW / f"{run}-{reqid}.network.txt"
    if meta.exists():
        text = meta.read_text()
        found = re.search(r"^## Request (\S+)", text, re.M)
        entry["url"] = found[1] if found else url
        entry["metadata_file"] = relative(meta)
        headers = re.search(r"### Request Headers\n(.*?)(?:\n### |\Z)", text, re.S)
        entry["request_headers_text"] = headers[1] if headers else None
        entry["response_body_unavailable"] = "<Response body not available anymore>" in text
    else:
        entry["url"] = url
    parsed = urlparse(entry["url"])
    entry["host"] = parsed.netloc
    entry["path"] = parsed.path
    entry["query"] = parse_qs(parsed.query, keep_blank_values=True)
    entry["fragment"] = parsed.fragment
    for kind in ("request", "response"):
        path = body_file(run, reqid, kind)
        entry[kind + "_body_file"] = relative(path)
        if path and kind == "request":
            try:
                entry["request_json"] = read_json(path)
            except (ValueError, UnicodeError):
                entry["request_body_note"] = (
                    "Gzip payload exported through MCP as lossy UTF-8 text; cannot decode events."
                    if "clarity.ms" in parsed.netloc else "Non-JSON body; see saved body file."
                )
    return entry


inventory = []
for run in ("A", "B"):
    text = (RAW / f"{run}-network-final.txt").read_text()
    for line in text.splitlines():
        m = re.match(r"reqid=(\d+) (\S+) (.*?) \[([^]]+)\]$", line)
        if m:
            inventory.append(network_entry(run, int(m[1]), m[2], m[3], m[4]))

# These two setup events fell out of the three-navigation preserved window.
prelude = [network_entry("A", i, "POST", "https://webpromo.kinedu.com/api/track", "200")
           for i in (16, 28)]
for entry in prelude:
    entry["phase"] = "viewport_setup_prelude"
for entry in inventory:
    entry["phase"] = ("assessment" if entry["run"] == "B" or entry["reqid"] < 88
                      else "return_from_paywall" if entry["reqid"] >= 114 else "paywall")
dump("network-inventory.json", {"cutoffs": {"A": 115, "B": 59},
                                "setup_prelude": prelude, "requests": inventory})
tracks = [e for e in prelude + inventory if e["path"] == "/api/track"]
facebook = [e for e in inventory if e["host"] == "www.facebook.com" and e["path"] == "/tr/"]
dump("track-events.json", tracks)
dump("facebook-events.json", facebook)
dump("tracker-inventory.json", [e for e in inventory
                               if any(x in e["host"] for x in ("facebook", "clarity", "stripe"))])

start = read_json(API / "A-start.response.json")
groups = []
for index, section in enumerate(start["sections"]):
    qs = ([section["anchor"]] if section.get("anchor") else []) + section["items"]
    if index < len(start["calibration"]):
        qs = qs + [start["calibration"][index]]
    groups.append((section["area"], qs))
served = [(q["id"], q["rate"], q["title"]) for _, qs in groups for q in qs]
age12 = (ROOT / "questions-by-age.md").read_text().split("## 12 months —")[1].split("\n## 13 months")[0]
static = []
for line in age12.splitlines():
    m = re.match(r"- (?:\*\*anchor\*\* |\*calibration \([^)]*\)\* )?(\d+) · ([\d.]+) · (.*)", line)
    if m:
        static.append((int(m[1]), float(m[2]), m[3]))

question_md = []
dom_checks = {}
for area, qs in groups:
    snapshot = RAW / ("A-area-" + area.lower() + ".snapshot.txt")
    text = snapshot.read_text()
    positions = [text.find(json.dumps(q["title"], ensure_ascii=False)) for q in qs]
    dom_checks[area] = all(p >= 0 for p in positions) and positions == sorted(positions)
    question_md += [f"### {area}", "", "| Order | ID | Rate | Run A answer | Exact on-screen question |",
                    "| --- | --- | --- | --- | --- |"]
    for i, q in enumerate(qs, 1):
        answer = "Yes" if q["rate"] >= 0.5 else "Not yet"
        note = f" (calibration; API area {q['area']})" if q in start["calibration"] else ""
        question_md.append(f"| {i} | {q['id']}{note} | {q['rate']:g} | {answer} | {q['title']} |")
    question_md += [""]
(RAW / "question-comparison.md").write_text("\n".join(question_md))

verification = {"ageMonths": start["ageMonths"], "corrected": start["corrected"],
                "question_count": len(served), "age12_id_rate_title_order_equal": static == served,
                "area_dom_text_and_order_equal": dom_checks,
                "A_B_start_bytes_equal": (API / "A-start.response.json").read_bytes() == (API / "B-start.response.json").read_bytes(),
                "phase2_start_json_equal": start == read_json(ROOT / "raw/api/start_age13_gw-null.json"),
                "results": {}, "screenshots": []}
for run, reference in (("A", "C_age12_rate_ge50.json"), ("B", "E_age12_extension_all_one.json")):
    path = API / f"{run}-result.response.json"
    req = read_json(API / f"{run}-result.request.json")
    verification["results"][run] = {
        "answers": len(req["answers"]), "yes": sum(q["y"] for q in req["answers"]),
        "extended": req["extended"], "phase3_reference": "raw/api/scoring/" + reference,
        "phase3_bytes_equal": path.read_bytes() == (ROOT / "raw/api/scoring" / reference).read_bytes(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "byte_length": path.stat().st_size,
        "basic": read_json(path)["basic"], "detail": read_json(path)["detail"]}
for path in sorted((ROOT / "screenshots").glob("*.png")):
    data = path.read_bytes()
    width, height = struct.unpack(">II", data[16:24])
    verification["screenshots"].append({"file": relative(path), "width": width, "height": height,
                                        "sha256": hashlib.sha256(data).hexdigest()})
dump("verification.json", verification)
print(json.dumps({"requests": len(inventory), "tracks_including_setup": len(tracks),
                  "facebook_events": len(facebook), "screenshots": len(verification["screenshots"]),
                  "question_match": static == served,
                  "result_byte_matches": {k: v["phase3_bytes_equal"] for k, v in verification["results"].items()}}, indent=2))
