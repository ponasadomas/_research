#!/usr/bin/env python3
"""Paced, resumable Phase 3 probes. Only POST /api/assessment is allowed.

Usage: probe_scoring.py initial | extensions | chains | batch FILE | summary
Batch files are JSON arrays of {name, body, experiment?}; saved names are immutable.
All invocations share a 350-attempt budget and a collector lock. No retries hide errors.
"""
import argparse
import csv
import datetime as dt
import fcntl
import hashlib
import json
import random
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "raw/api/scoring"
MANIFEST = OUT / "requests.jsonl"
URL = "https://webpromo.kinedu.com/api/assessment"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
LIMIT = 350


def records():
    return [json.loads(s) for s in MANIFEST.read_text().splitlines()] if MANIFEST.exists() else []


def starts():
    result = {}
    for path in sorted((ROOT / "raw/api").glob("start_age*_gw-null.json")):
        data = json.loads(path.read_text())
        if "sections" in data:
            age = data["ageMonths"]
            assert age not in result, (age, path)
            result[age] = data
    assert set(result) == set(range(49))
    return result


def ordered(data):
    items = []
    for i, section in enumerate(data["sections"]):
        if section.get("anchor"):
            items.append(section["anchor"])
        items.extend(section["items"])
        if i < len(data.get("calibration", [])):
            items.append(data["calibration"][i])
    assert len({q["id"] for q in items}) == len(items)
    return items


def body(age, items, predicate=lambda q: 0, extended=False):
    return dict(action="result", ageMonths=age, extended=extended,
                answers=[dict(id=q["id"], y=int(predicate(q))) for q in items])


def brief(data):
    return dict(stage=data.get("stage"), **data.get("basic", {}),
                areas=data.get("detail", {}).get("areas"), error=data.get("error"),
                extension_ids=[q["id"] for q in data.get("items", [])])


def request(name, payload, experiment="adaptive"):
    if not name or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for c in name):
        raise ValueError("Use a descriptive alphanumeric filename stem")
    if payload.get("action") != "result":
        raise ValueError("This collector accepts result probes only; start lists are reused")
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / ".collector.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        old = records()
        path = OUT / (name + ".json")
        rel = str(path.relative_to(ROOT))
        if path.exists():
            rec = next((r for r in old if r["file"] == rel), None)
            if not rec or rec["body"] != payload:
                raise FileExistsError("Existing path has no identical manifested request: " + rel)
            assert rec["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
            return json.loads(path.read_text())
        if len(old) >= LIMIT:
            raise RuntimeError(f"Phase 3 request budget exhausted: {len(old)}/{LIMIT}")
        # Sleep after the preceding response, including across script restarts.
        time.sleep(0.5)
        timestamp = dt.datetime.now(dt.timezone.utc).isoformat()
        headers = OUT / (name + ".headers.txt")
        cmd = ["curl", "--request", "POST", URL, "--user-agent", UA,
               "--header", "Content-Type: application/json",
               "--header", "Origin: https://webpromo.kinedu.com",
               "--header", "Referer: https://webpromo.kinedu.com/aq-assessment",
               "--data-raw", json.dumps(payload, separators=(",", ":")),
               "--connect-timeout", "20", "--max-time", "60", "--silent", "--show-error",
               "--dump-header", str(headers), "--output", str(path), "--write-out", "%{http_code}"]
        run = subprocess.run(cmd, capture_output=True, text=True)
        if not path.exists():
            path.write_bytes(b"")
        raw = path.read_bytes()
        rec = dict(timestamp=timestamp, completed_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                   body=payload, file=rel, http_status=int(run.stdout or 0),
                   curl_exit_code=run.returncode, stderr=run.stderr,
                   headers=str(headers.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest(),
                   experiment=experiment)
        with MANIFEST.open("a") as out:
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        try:
            data = json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            raise RuntimeError(f"Preserved invalid response: {rel}")
        print(json.dumps(dict(n=len(old)+1, name=name, http_status=rec["http_status"],
                              **brief(data))), flush=True)
        if run.returncode or rec["http_status"] >= 500 or rec["http_status"] == 429:
            raise RuntimeError("Preserved transport/server/rate-limit failure; stopped")
        return data


def initial():
    bank = starts()
    items = ordered(bank[12])
    mixed = body(12, items, lambda q: q["rate"] >= .5)
    for n in range(1, 4):
        request(f"A_age12_mixed_repeat{n}", mixed, "A")
    shuffled = json.loads(json.dumps(mixed))
    random.Random(1203).shuffle(shuffled["answers"])
    request("A_age12_mixed_shuffled", shuffled, "A")
    request("A_age12_mixed_extended", dict(mixed, extended=True), "A")
    for direction in ["ascending", "descending"]:
        ranked = sorted(items, key=lambda q: (q["rate"], q["id"]), reverse=direction == "descending")
        for k in range(len(ranked)+1):
            yes = {q["id"] for q in ranked[:k]}
            request(f"B_age12_{direction}_{k:02d}", body(12, items, lambda q: q["id"] in yes, True), "B")
    for age in [3, 12, 24, 36]:
        qs = ordered(bank[age])
        for threshold in [.25, .5, .75]:
            name = f"C_age{age:02d}_rate_ge{int(threshold*100):02d}"
            p = body(age, qs, lambda q: q["rate"] >= threshold)
            d = request(name, p, "C")
            if d.get("stage") == "extension":
                request(name+"_extended_bypass", dict(p, extended=True), "C")
    for area in ["Physical", "Cognitive", "Language", "Social-Emotional"]:
        p = body(12, items, lambda q: q["area"] == area)
        name = "D_age12_only_" + area.replace("-", "_")
        request(name, p, "D")
        request(name+"_extended", dict(p, extended=True), "D")
    typical = body(12, items, lambda q: q["rate"] >= .5, True)
    foreign = [q for q in ordered(bank[36]) if q["id"] not in {x["id"] for x in items}]
    request("F_age12_foreign_age36_only", body(12, foreign, lambda q: 1, True), "F")
    request("F_age12_typical_plus_foreign_yes", dict(typical, answers=typical["answers"]+body(12,foreign,lambda q:1)["answers"]), "F")
    request("F_age12_typical_plus_foreign_no", dict(typical, answers=typical["answers"]+body(12,foreign)["answers"]), "F")
    request("F_age12_first10_only", dict(typical, answers=typical["answers"][:10]), "F")
    for val in [2, -1]:
        p = json.loads(json.dumps(typical)); p["answers"][0]["y"] = val
        request(f"F_age12_invalid_y_{str(val).replace('-', 'minus')}", p, "F")
    calib = {q["id"] for q in bank[12]["calibration"]}
    request("F_age12_typical_omit_calibration", dict(typical, answers=[x for x in typical["answers"] if x["id"] not in calib]), "F")
    request("F_age12_empty_answers", dict(typical, answers=[]), "F")
    for age in [0, 1, 2]:
        qs = ordered(bank[age]); calib = {q["id"] for q in bank[age]["calibration"]}
        request(f"G_age{age:02d}_all_zero", body(age, qs), "G")
        request(f"G_age{age:02d}_zero_calibration_yes", body(age, qs, lambda q:q["id"] in calib, True), "G")
        request(f"G_age{age:02d}_zero_omit_calibration", body(age, [q for q in qs if q["id"] not in calib], extended=True), "G")


def extensions():
    bank = starts(); items = ordered(bank[12])
    for direction in ["ascending", "descending", "client_order"]:
        ranked = items if direction == "client_order" else sorted(items, key=lambda q:(q["rate"], q["id"]), reverse=direction=="descending")
        # Binary search means a boundary along this particular nested ordering,
        # not a global fraction-only trigger. Boundary-neighbor evidence is saved.
        low, high = 0, len(ranked)
        for k in [0, len(ranked)]:
            yes = {q["id"] for q in ranked[:k]}
            request(f"E_age12_{direction}_{k:02d}", body(12,items,lambda q:q["id"] in yes), "E")
        while high-low > 1:
            k=(low+high)//2; yes={q["id"] for q in ranked[:k]}
            d=request(f"E_age12_{direction}_{k:02d}",body(12,items,lambda q:q["id"] in yes),"E")
            if d.get("stage")=="extension": high=k
            else: low=k
        print(json.dumps(dict(order=direction, first_extension=high, last_complete=low)),flush=True)
    base=body(12,items,lambda q:1)
    ext=request("E_age12_all_yes_trigger",base,"E")["items"]
    request("E_age12_all_yes_bypass",dict(base,extended=True),"E")
    for label,predicate in [("all_one",lambda q:1),("all_zero",lambda q:0),("mixed",lambda q:q["id"]%2)]:
        answers=base["answers"]+body(12,ext,predicate)["answers"]
        request("E_age12_extension_"+label,dict(base,answers=answers,extended=True),"E")
        request("E_age12_extension_"+label+"_false",dict(base,answers=answers),"E")
    request("E_age12_extension_only_yes",body(12,ext,lambda q:1,True),"E")


def summary():
    rows=[]
    for rec in records():
        data=json.loads((ROOT/rec["file"]).read_text()); b=brief(data)
        rows.append(dict(name=Path(rec["file"]).stem,experiment=rec["experiment"],
                         age=rec["body"]["ageMonths"],extended=rec["body"].get("extended"),
                         n=len(rec["body"]["answers"]),yes=sum(x["y"]==1 for x in rec["body"]["answers"]),
                         http=rec["http_status"],**{k:json.dumps(v) if isinstance(v,(dict,list)) else v for k,v in b.items()}))
    fields=list(dict.fromkeys(k for row in rows for k in row))
    with (OUT/"summary.csv").open("w") as out:
        writer=csv.DictWriter(out,fieldnames=fields);writer.writeheader();writer.writerows(rows)
    print(json.dumps(dict(requests=len(rows),budget=LIMIT,summary=str(OUT/"summary.csv"))))


def chains():
    bank=starts()
    for age in [12,3,24,36]:
        p=body(age,ordered(bank[age]),lambda q:1)
        for depth in range(9):
            d=request(f"E_chain_age{age:02d}_depth{depth:02d}_false",p,"E")
            if depth:
                request(f"E_chain_age{age:02d}_depth{depth:02d}_true",dict(p,extended=True),"E")
            if d.get("stage")!="extension": break
            seen={x["id"] for x in p["answers"]}
            assert not seen.intersection(q["id"] for q in d["items"]), "Repeated extension ID"
            p=dict(p,answers=p["answers"]+[dict(id=q["id"],y=1) for q in d["items"]])
        else:
            raise RuntimeError("Chain depth exceeded safety bound; saved through depth8")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=["initial","extensions","chains","batch","summary"])
    parser.add_argument("file",nargs="?")
    args=parser.parse_args()
    if args.mode=="initial": initial()
    elif args.mode=="extensions": extensions()
    elif args.mode=="chains": chains()
    elif args.mode=="batch":
        for job in json.loads(Path(args.file).read_text()):
            request(job["name"],job["body"],job.get("experiment","adaptive"))
    else: summary()
