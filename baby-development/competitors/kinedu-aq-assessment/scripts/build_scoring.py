#!/usr/bin/env python3
"""Rebuild SCORING.md and audit artifacts from saved files, without network calls."""
import collections
import datetime as dt
import hashlib
import itertools
import json
import math
import statistics
import subprocess
import sys
from pathlib import Path

from probe_scoring import ROOT, OUT, records, starts, ordered, summary


def table(headers, rows):
    clean = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(map(clean, headers)) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |"] +
                     ["| " + " | ".join(map(clean, row)) + " |" for row in rows])


def weighted_fit(rows):
    """Constrained least squares on 4 nonnegative weights summing to 1."""
    def solve(matrix, rhs):
        a=[list(row)+[v] for row,v in zip(matrix,rhs)];n=len(a)
        for col in range(n):
            pivot=max(range(col,n),key=lambda i:abs(a[i][col]))
            if abs(a[pivot][col])<1e-10:return None
            a[col],a[pivot]=a[pivot],a[col]
            divisor=a[col][col];a[col]=[x/divisor for x in a[col]]
            for i in range(n):
                if i==col:continue
                multiplier=a[i][col];a[i]=[x-multiplier*y for x,y in zip(a[i],a[col])]
        return [row[-1] for row in a]
    candidates=[]
    # The least-squares minimum is interior to one of the simplex's 15 faces.
    for n in range(1,5):
        for active in itertools.combinations(range(4),n):
            matrix=[[sum(x[i]*x[j] for x,y in rows) for j in active]+[1] for i in active]
            matrix.append([1]*n+[0])
            rhs=[sum(x[i]*y for x,y in rows) for i in active]+[1]
            solution=solve(matrix,rhs)
            if solution is None or min(solution[:n])<-1e-8:continue
            weights=[0.]*4
            for i,w in zip(active,solution[:n]):weights[i]=max(0.,w)
            error=sum((sum(a*w for a,w in zip(x,weights))-y)**2 for x,y in rows)
            candidates.append((error,weights))
    error,weights=min(candidates)
    predictions=[sum(a*w for a,w in zip(x,weights)) for x,y in rows]
    return dict(weights=weights,rmse=math.sqrt(error/len(rows)),total=len(rows),
                rounded_exact=sum(math.floor(p+.5)==y for p,(x,y) in zip(predictions,rows)))


def main():
    recs=records()
    assert len(recs)<=350
    data={Path(r["file"]).stem:json.loads((ROOT/r["file"]).read_text()) for r in recs}
    rec_by_name={Path(r["file"]).stem:r for r in recs}
    seen=set();gaps=[]
    for i,r in enumerate(recs):
        assert r["file"] not in seen
        seen.add(r["file"])
        raw=(ROOT/r["file"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==r["sha256"]
        assert r["curl_exit_code"]==0 and r["http_status"] in [200,400]
        assert r["body"]["action"]=="result"
        h=(ROOT/r["headers"]).read_text()
        assert str(r["http_status"]) in [s.split()[1] for s in h.splitlines() if s.startswith("HTTP/")]
        if i:
            gap=(dt.datetime.fromisoformat(r["timestamp"])-dt.datetime.fromisoformat(recs[i-1]["completed_at"])).total_seconds()
            assert gap>=.5, gap
            gaps.append(gap)
    assert {str(p.relative_to(ROOT)) for p in OUT.glob("*.json")}==seen
    subprocess.run([sys.executable,str(ROOT/"logs/phase3-offline-analysis.py")],check=True,capture_output=True)
    stats=json.loads((ROOT/"logs/phase3-offline-stats.json").read_text())
    summary()
    audit=dict(requests=len(recs),budget=350,http_status_counts=dict(collections.Counter(r["http_status"] for r in recs)),
               first_request=recs[0]["timestamp"],last_response=recs[-1]["completed_at"],
               minimum_response_to_next_request_gap_seconds=min(gaps),hashes_verified=len(recs),
               raw_files_match_manifest=True,transport_failures=0,
               endpoint="https://webpromo.kinedu.com/api/assessment",all_actions="result")
    (ROOT/"logs/phase3-validation.json").write_text(json.dumps(audit,indent=2)+"\n")

    def d(name): return data[name]
    def basic(name): return d(name).get("basic",{})
    def link(name,label=None):return f'[{label or name}](raw/api/scoring/{name}.json)'
    def areas(name):
        result=[]
        for a in d(name).get("detail",{}).get("areas",[]):
            result.append(str(a["months"])+("+" if a.get("atLeast") else "") if "months" in a else a["state"])
        return ", ".join(result) or "—"
    def result(name):
        b=basic(name)
        return f'{b["devAge"]}{"+" if b.get("capped") else ""} / {b["band"]}' if b.get("state")=="ok" else b.get("state",d(name).get("stage"))
    def count(name):return sum(x["y"]==1 for x in rec_by_name[name]["body"]["answers"])
    bank=starts();qs=ordered(bank[12])

    # Independent predictions: ascending is the training set, descending/random held out.
    held_global=[];held_area=[]; area_map={}
    for k in range(40):
        n=f"B_age12_ascending_{k:02d}"; ans=rec_by_name[n]["body"]["answers"]
        byid={x["id"]:x["y"] for x in ans}
        for a in d(n).get("detail",{}).get("areas",[]):
            ay=sum(byid[q["id"]] for q in qs if q["area"]==a["area"])
            area_map[(a["area"],ay)]=(a["state"],a.get("months"),a.get("atLeast"))
    for k in range(40):
        a=basic(f"B_age12_ascending_{k:02d}");b=basic(f"B_age12_descending_{k:02d}")
        held_global.append(tuple(a.get(f) for f in ["state","devAge","band","capped"])==tuple(b.get(f) for f in ["state","devAge","band","capped"]))
        n=f"B_age12_descending_{k:02d}";byid={x["id"]:x["y"] for x in rec_by_name[n]["body"]["answers"]}
        for ar in d(n).get("detail",{}).get("areas",[]):
            ay=sum(byid[q["id"]] for q in qs if q["area"]==ar["area"])
            if (ar["area"],ay) in area_map:
                held_area.append(area_map[(ar["area"],ay)]==(ar["state"],ar.get("months"),ar.get("atLeast")))
    random_matches=[]
    for k in [17,20,24,28,34,35]:
        a=basic(f"B_age12_ascending_{k:02d}");b=basic(f"M_age12_random_count{k:02d}")
        random_matches.append(all(a.get(f)==b.get(f) for f in ["state","devAge","band","capped"]))
    assert all(held_global+held_area+random_matches)
    assert not stats["area_count_lookup"]["conflict_groups"]
    assert not stats["global_count_lookup"]["conflict_groups"]
    # Read source-derived metric from final analyzer; the fitting set is explicitly named below.
    bandstat=stats["band_formula"]; agg=stats["aggregations"]
    initial_repeat=["A_age12_mixed_repeat1","A_age12_mixed_repeat2","A_age12_mixed_repeat3","A_age12_mixed_shuffled"]
    assert len({rec_by_name[n]["sha256"] for n in initial_repeat})==1
    for n in ['A_age12_mixed_extended','F_age12_typical_plus_unknown','F_age12_duplicate_first','F_age12_duplicate_conflict_first']:
        assert d(n)==d(initial_repeat[0])
    all_numeric=[];all_skills=[]
    for manifest in [ROOT/"raw/api/requests.jsonl",OUT/"requests.jsonl"]:
        for rec in map(json.loads,manifest.read_text().splitlines()):
            p=rec.get('body',rec.get('request'))
            if rec['http_status']!=200 or p.get('action')!='result':continue
            report=json.loads((ROOT/rec['file']).read_text())
            av=[a['months'] for a in report.get('detail',{}).get('areas',[]) if 'months' in a]
            assert all(v%2==0 for v in av)
            if len(av)==4:all_numeric.append((av,report['basic']['devAge']))
            all_skills.extend(report.get('skills',[]))
    assert all(s['total']==len(s['items']) for s in all_skills)
    fit=weighted_fit(all_numeric)
    assert fit['total']==agg['total']
    area_lookup=collections.defaultdict(dict)
    for n,rec in rec_by_name.items():
        answers={a['id']:a['y'] for a in rec['body']['answers']}
        if set(answers)!={q['id'] for q in qs}:continue
        for ar in d(n).get('detail',{}).get('areas',[]):
            if 'months' not in ar:continue
            k=sum(answers[q['id']] for q in qs if q['area']==ar['area'])
            value=(ar['months'],ar['atLeast'])
            if k in area_lookup[ar['area']]:assert area_lookup[ar['area']][k]==value
            area_lookup[ar['area']][k]=value
    (ROOT/'logs/phase3-formula-fit.json').write_text(json.dumps(dict(weighted_mean_fit=fit,age12_area_count_lookup=area_lookup),indent=2)+'\n')

    text=[]
    def add(s):text.append(s.strip()+"\n")
    add(f'''# Kinedu AQ scoring: Phase 3

Collected on **2026-11-02**. **Verdict: PARTLY REAL** — real answer-driven count/norm computation, with an unresolved all-zero anomaly, confirmed nonmonotonic low-score area ages, and cosmetic locked tiles. This establishes computational behavior; it does not establish the medical or psychometric validity of the assessment.

## Method and evidence boundaries

Read [ENUMERATION.md](ENUMERATION.md), [age-map.md](age-map.md), [questions.csv](questions.csv), and the saved Phase 2 results before probing. Reused the 49 initial lists indexed by their **returned** `ageMonths`; returned age 12 is in `start_age13_gw-null.json`. No browser or new start call was used.

Made **{len(recs)} requests out of the 350-request limit**: {audit['http_status_counts'][200]} HTTP 200 and {audit['http_status_counts'][400]} expected HTTP 400 invalid-answer responses, with no transport failures. Every request was a POST `action:result` to `/api/assessment`, using the exact User-Agent, Content-Type, Origin and Referer in ENUMERATION.md. Slept 0.5 seconds before each call; the verified minimum gap from one response completion to the next request was **{min(gaps):.3f} seconds**. No other endpoint was called.

All response bodies and HTTP headers are immutable under [raw/api/scoring/](raw/api/scoring/). The authoritative [requests manifest](raw/api/scoring/requests.jsonl) records UTC `timestamp`, `body`, `file`, `http_status`, completion time, curl status and SHA-256. [summary.csv](raw/api/scoring/summary.csv) records every probe's score, band and area values; [validation](logs/phase3-validation.json) verifies hashes, statuses, pacing, coverage and budget. All HTTP errors remain in the evidence.

The [collector](scripts/probe_scoring.py) supports `initial`, `extensions`, `chains`, `batch FILE`, and `summary`; it resumes only identical manifested requests, refuses overwrites, serializes calls with a lock, and enforces the shared 350-call budget. Additional batch plans are [followups](logs/phase3-followups.json), [followups2](logs/phase3-followups2.json), [followups3](logs/phase3-followups3.json), [rate controls](logs/phase3-rate-controls.json), and [area edge controls](logs/phase3-area-edge-controls.json). Rebuild this report and audit without network calls with `python scripts/build_scoring.py`.

**Observed** below means a saved API response or saved client source directly shows it. **Inferred** means an explanatory model fitted to those observations. The server's source and full item norm tables are unavailable. Fit denominators are named explicitly; repeated-group fits are consistency checks, not independent validation sets. Additional offline calculations and source citations are in [offline findings](logs/phase3-offline-findings.md) and [machine-readable statistics](logs/phase3-offline-stats.json).''')

    add('''## A. Determinism and answer order

Mixed profile: age 12, all 39 IDs, `y=1` iff `rate>=0.5` (28 yes), `extended:false`.''')
    add(table(["Probe","HTTP","devAge / band","Area months P, C, L, S","Identical raw bytes"],[
        [link(n),rec_by_name[n]["http_status"],result(n),areas(n),"yes"] for n in initial_repeat]))
    add('''**Observed:** the three repeats and deterministic shuffle have identical JSON **and identical response bytes/SHA-256**. Changing only `extended` to true also gives the identical complete report ([flag control](raw/api/scoring/A_age12_mixed_extended.json)). JSON field ordering is therefore not masking a difference in these comparisons. These are same-session tests, not evidence of stability after future server updates.''')

    add('''## B. Cumulative monotonicity

Both sweeps use the same 39 age-12 IDs and `extended:true`, to obtain complete scores instead of stopping at extension. Sort by `(rate,id)`, ascending or descending, then flip one additional answer to 1 per row. `+` after overall age means `capped:true`; `+` after an area means `atLeast:true`. Area order is Physical, Cognitive, Language, Social-Emotional. Dashes mean the API omitted ages for `below_floor`, not that those ages are zero. Every row links to its raw report.''')
    b_rows=[];jumps=[];area_drops=[]
    ranks={direction:sorted(qs,key=lambda q:(q["rate"],q["id"]),reverse=direction=="descending") for direction in ["ascending","descending"]}
    for k in range(40):
        a=f"B_age12_ascending_{k:02d}";b=f"B_age12_descending_{k:02d}"
        b_rows.append([k,link(a,"—" if not k else str(ranks['ascending'][k-1]['id'])),link(b,"—" if not k else str(ranks['descending'][k-1]['id'])),result(a),areas(a),areas(b)])
        for direction in ranks:
            if not k:continue
            prev=basic(f"B_age12_{direction}_{k-1:02d}");now=basic(f"B_age12_{direction}_{k:02d}")
            if "devAge" in prev and "devAge" in now:
                jumps.append((now['devAge']-prev['devAge'],direction,k,ranks[direction][k-1]['id']))
                pa=d(f"B_age12_{direction}_{k-1:02d}")['detail']['areas'];na=d(f"B_age12_{direction}_{k:02d}")['detail']['areas']
                area_drops += [(direction,k,p['area']) for p,n in zip(pa,na) if 'months' in p and 'months' in n and n['months']<p['months']]
    assert min(x[0] for x in jumps)>=0 and not area_drops
    add(table(["Yes count","New ID asc / raw","New ID desc / raw","Overall: both","Asc area months","Desc area months"],b_rows))
    maxjump=max(x[0] for x in jumps)
    add(f'''**Observed:** global state/age/band/cap match at **{sum(held_global)}/{len(held_global)}** equal-count pairs. Numeric overall ages and observed area ages never decrease within either sweep. Movement is stepwise, with plateaus, rather than smooth. The largest overall move is **+{maxjump} months at flip 35** (21→33): ascending flips ID {ranks['ascending'][34]['id']}, descending flips ID {ranks['descending'][34]['id']}. The same jump occurring at the same total count for different IDs shows why this cannot be interpreted as an intrinsic weight of either milestone. Other +2 moves occur at flips 33 and 34; entering the numeric range at flip 17 cannot be assigned a numerical jump because the preceding report omits age.

Training the global count lookup on the ascending sweep predicts the descending sweep **40/40** and six separately shuffled vectors **6/6**, including cap and band. Training per-area `(area yes count)→(state,months,atLeast)` on the ascending sweep predicts **{sum(held_area)}/{len(held_area)}** descending area outputs whose counts were present in training. The remaining descending area outputs have no matching training count; they are not counted as failed or successful predictions.''')

    add('''## C. Rate-threshold profiles and a corrected typical-child control

Original probes use `extended:false`; where they return extension, a separately saved bypass with the same answers and `extended:true` supplies the score shown below.''')
    c_rows=[]
    for age in [3,12,24,36]:
        for threshold in [25,50,75]:
            n=f"C_age{age:02d}_rate_ge{threshold:02d}";used=n+"_extended_bypass" if d(n).get('stage')=='extension' else n
            c_rows.append([age,f">={threshold/100:g}",count(n),d(n)['stage'],result(used),areas(used),link(used,"report")])
    add(table(["Age","Rate threshold","Yes / 39","Initial stage","devAge / band","Area months P,C,L,S","Evidence"],c_rows))
    add('''**Observed:** the threshold-0.5 profile does not consistently produce `on_pace`: age 3 is below-floor, age 12 gives 14, age 24 gives 28, and age 36 is capped at 46. These outcomes alone do not disprove a norm model. If `rate` is an age-conditioned achievement probability, `sum(rate)` is the expected total; the count of rates above 0.5 is a different statistic. A deterministic threshold profile is not a random draw of a typical child.

Four controls therefore choose a random set of `round(sum(rate))` yes answers, keeping the full served ID set. This is an aggregate-count control, not a claim that those particular milestones form a realistic child profile:''')
    add(table(["Age","Sum of served rates","Yes count","Result","Evidence"],[[age,f"{sum(q['rate'] for q in ordered(bank[age])):.2f}",count(n:=f"M_age{age:02d}_count_matches_expected_rate_sum"),result(n),link(n,"raw")] for age in [3,12,24,36]]))
    add('''**Observed:** age is recovered exactly and band is `on_pace` in **4/4** controls. **Inference:** equating the observed success count with an expected-count norm curve is a substantially better explanation than weighting individual yes answers by their current displayed rate.''')

    add('''## D. Area independence and overall aggregation

The four requested isolated-area profiles each return `below_floor`, with no area ages to inspect. Both flag values give the same below-floor response. This is an observability limitation, not evidence that the area score fails to respond.''')
    add(table(["Only area set to yes","Yes / 39","Result","Evidence"],[[area,count(n:='D_age12_only_'+area.replace('-','_')),result(n),link(n,"false")+'; '+link(n+'_extended','true')] for area in ["Physical","Cognitive","Language","Social-Emotional"]]))
    add('''To expose area changes, hold all other answers at the 28-yes threshold-0.5 baseline and set one area's answers to all-zero or all-one. The baseline ages are **14,16,12,16**, overall 14.''')
    add(table(["Changed area","Area answers","Overall","Area months P,C,L,S","Evidence"],[[area,val,result(n:='D2_age12_typical_'+area.replace('-','_')+'_all'+str(val)),areas(n),link(n,"raw")] for area in ["Physical","Cognitive","Language","Social-Emotional"] for val in [0,1]]))
    add(f'''**Observed:** all eight interventions change only the targeted area's age/atLeast; the other **24/24** area records remain identical. Global age can change. Across Phase 2 and Phase 3, an area lookup keyed by **that area's effective answered IDs and yes count** has **{stats['area_count_lookup']['prediction_comparisons']}/{stats['area_count_lookup']['prediction_comparisons']}** repeat-key comparisons without conflicts, including cases in which other areas change.

Overall age is **not** a simple mean, median, minimum or maximum of the four published ages. Fit against all **{agg['total']}** complete reports with four numeric area ages:''')
    add(table(["Formula","Exact matches / reports"],[[label,f"{agg['exact_matches'][key]}/{agg['total']}"] for label,key in [("floor(mean)","mean_floor"),("round-half-up(mean)","mean_round_half_up"),("ceil(mean)","mean_ceil"),("floor(median)","median_floor"),("round-half-up(median)","median_round_half_up"),("minimum","min_floor"),("maximum","max_floor")]]))
    add(f'''A constrained least-squares weighted mean (nonnegative weights summing to one) fitted on the same {fit['total']} reports gives weights P,C,L,S = **{', '.join(f'{x:.4f}' for x in fit['weights'])}**. After rounding half up it matches **{fit['rounded_exact']}/{fit['total']}**, with unrounded RMSE **{fit['rmse']:.3f} months**. These are fitted, in-sample metrics, not held-out accuracy. [Fit data](logs/phase3-formula-fit.json).

These aggregate fits pool repeated and deliberately extreme probes; the denominator is not a population sample. At ascending count 17, the four ages are 12,12,8,0 but overall is 11. At all-one, age 3 has overall 18 and areas 10,18,10,8; age 12 has overall 33 and areas 20,16,20,36. The first exact weighted-mean equality would require all weight on Cognitive, which predicts 16 for the second. Even rounding cannot reconcile this pair. The supported explanation is a separate overall norm projection over the answered-ID set.''')

    area_names=['Physical','Cognitive','Language','Social-Emotional']
    add('''**Exact observed per-area lookup for the fixed age-12 ID set.** The complete set contains 9 Physical, 9 Cognitive, 10 Language and 11 Social-Emotional answers, including calibration in its actual domain. Each cell is months, with `+` for atLeast. A dash means the count exceeds that area's item count or was unobserved. All observed entries agree across repeated profiles.''')
    add(table(['Area yes count']+area_names,[[k]+[str(area_lookup[a][k][0])+('+' if area_lookup[a][k][1] else '') if k in area_lookup[a] else '—' for a in area_names] for k in range(12)]))
    add('''**Nonmonotonic area edge behavior:** unlike the numeric portions of the cumulative sweeps, this full lookup reveals low-score drops: Cognitive zero yes gives 8 months, two yes gives 2, three yes gives 0, then four yes gives 12; Social-Emotional zero/two yes gives 6 months, three yes gives 0, then four gives 8. Final controls change only that area's cumulative yes count, holding every other answer at the same typical baseline, and reproduce these drops. See [Cognitive count 2](raw/api/scoring/D3_age12_Cognitive_count02_others_typical.json), [count 3](raw/api/scoring/D3_age12_Cognitive_count03_others_typical.json), [count 4](raw/api/scoring/D3_age12_Cognitive_count04_others_typical.json), [Social count 3](raw/api/scoring/D3_age12_Social_Emotional_count03_others_typical.json), and the zero controls in D2. This is a scoring pathology, not noise in repeated calls. A count lookup explains it exactly but a smooth monotone developmental model does not. The cumulative B tests did not expose it because their early whole reports were below_floor.''')

    add('''## Best-fit scoring model and exact-match limits

**Observed sufficient statistics:** normalize duplicate IDs with the **last value winning**, discard the observed unknown ID, let `S` be the effective known answered IDs, and let `K=sum(y)` over S. For a fixed S and chronological age, overall state/age/cap depends on K in every tested repeated group. Which particular IDs are yes affects skills and area counts, but did not alter global score at fixed K. Adding/removing IDs can change the norm curve, floor and ceiling; it is not just a universal yes percentage.

**Inferred norm projection:** let `p_i(m)` be the bank's underlying probability for item i at age m. A plausible approximate scorer is:

```text
observed_fraction = K / len(S)
expected_fraction_S(m) = mean(p_i(m) for i in S with usable norm data)
raw_age ≈ argmin_m abs(expected_fraction_S(m) - observed_fraction)
```

The valid candidate ages, missing-norm handling and ceiling rule matter. They are not fully recoverable from the rounded, age-local start rates. A Rasch-like norm model with raw count as sufficient statistic is also compatible with the count tests; the probes do not identify a unique server implementation.

**Direct numerical check:** submit the entire 11-ID Secure Attachment inventory at chronological age 0. Its published skill curve supplies the expected mean. Choosing the closest curve pct to `K/11` over positive integer ages predicts every uncapped global result. This is a fitted diagnostic using a complete skill inventory, not a proof that all arbitrary sets use the plotted skill curve.''')
    s_norm=stats['secure_attachment_norm_inverse']['results']
    add(table(["Yes / 11","Nearest positive curve age","Returned overall age","Area months","Capped","Evidence"],[[x['yes'],x['predicted'],x['actual'],x['area_actual'],x['capped'],link(f"M_secure_age00_count{x['yes']:02d}","raw")] for x in s_norm]))
    add(f'''The nearest-curve model fits **11/11 uncapped global** results; including the all-one saturated case gives **11/12**. A naive nearest-mean calculation on even ages fits only **8/11 uncapped area** results, so the area's calibration is separate from this plotted mean. Per-area outputs are consistently count-driven and, in the collected numeric results, fall on a two-month grid; their low-score mapping can be nonmonotonic as shown in D. Their exact general norm/quantization function is unresolved.

The empirically exact age-12 lookup for the full 39-ID set is:''')
    add(table(["K","Global output"],[["0–16","below_floor"],["17–20","11 / building"],["21–24","12 / on_pace"],["25–27","13 / little_ahead"],["28–29","14 / well_ahead"],["30","15 / well_ahead"],["31","16 / well_ahead"],["32","17 / well_ahead"],["33","19 / well_ahead"],["34","21 / well_ahead"],["35–39","33 / well_ahead / capped"]]))
    add(f'''The complete `(chronological age,S,K)→(state,devAge,capped)` consistency model has **{stats['global_count_lookup']['prediction_comparisons']}/{stats['global_count_lookup']['prediction_comparisons']}** repeated-group comparisons without conflict. Conditional on a numeric result, `(S,K)→(devAge,capped)` has **{stats['numeric_count_lookup_ignoring_age']['prediction_comparisons']}/{stats['numeric_count_lookup_ignoring_age']['prediction_comparisons']}**, ignoring chronological age. These are internal consistency checks; the held-out pattern predictions are the 40+6 tests in B.

**Band formula, exact on {bandstat['matches']}/{bandstat['total']} numeric reports** across both phases:

```text
r = devAge / max(ageMonths, 1)
if r > 1.15:        well_ahead
elif r > 1.05:      little_ahead
elif r >= 0.95:     on_pace
else:              building
```

Exact boundary controls return `on_pace` at **0.95** and **1.05**, and `little_ahead` at **1.15**. See [0.95](raw/api/scoring/M_band_age20_count33.json), [1.05](raw/api/scoring/M_band_age20_count34.json), [1.15](raw/api/scoring/M_band_exact_115_dev46_age40.json). The displayed band uses the returned integer age in every checked report.

**Floor:** chronological age changes whether an age is exposed. The same 28-yes age-12 vector yields age 14 at the tested chronological ages 0,1,2,3,6,12–16, but below-floor at 17–24,36,48. An uncapped age 17 is `building` at chronological age 20 (ratio .85), and below-floor at age 21. This supports a lower reporting boundary near **85%** of chronological age. It is an inference about the tested uncapped vectors, not a fully recovered floor algorithm: the underlying pre-rounded age is hidden in floor responses. Capped age 33 is still `building` at chronological age 48 (ratio .6875), so a universal `ratio<.85→below_floor` rule is false. [Boundary .85](raw/api/scoring/M_band_age20_count32.json), [below it](raw/api/scoring/M_band_age21_count32.json), [cap exception](raw/api/scoring/M_age48_same_age12_all_one.json).

**Ceilings:** `capped:true` means saturation for the supplied answered-ID set, rather than a fixed age limit. Ages 3/12/24/36 all-one initial sets cap at 18/33/44/46. At age 12, answering additional extension items can lift the cap to 42,45,53. The identical devAge 33 can be capped before extension and uncapped after eight zero extension answers. An area's `atLeast` is its own saturation flag; it can be true when the global cap is false. The precise ceiling formula remains unresolved.''')

    add('''## E. Extension mechanics

**Observed trigger at age 12, fixed full 39-ID list:** binary search in ascending-rate, descending-rate and client order gives the same boundary. The first two orderings deliberately disagree about which milestones are yes.''')
    add(table(["Ordering","Last complete","First extension","First extension IDs"],[[order,link(f"E_age12_{order}_34","34 / 39 yes; age 21, uncapped"),link(f"E_age12_{order}_35","35 / 39 yes"),", ".join(str(q['id']) for q in d(f"E_age12_{order}_35")['items'])] for order in ["ascending","descending","client_order"]]))
    add('''A fourth randomized ordering confirms 34 complete / 35 extension. Thus all-one in any one area is insufficient, and neither consecutive yes answers, anchors being yes, nor a particular top-rate set is necessary. At the 35-yes boundary the ascending profile has all four anchors at zero, while descending has them at one. Answer order is irrelevant in A. This identifies the minimal yes **count for this fixed full set**; it does not establish a universal percentage threshold.

The cutoff changes with the supplied IDs: **34/38**, **34/37**, **34/36** all trigger extension, and their forced scores cap at 34 instead of 33. Age 36's threshold-0.5 profile triggers at **34/39**, so 35/39 is not a universal rule. Even only eight all-yes IDs at age 12 trigger extension ([subset probe](raw/api/scoring/E_age12_first08_yes_false.json)). Paired complete responses support **global saturation plus available extension candidates** as the trigger; area saturation alone is not sufficient.

Append the eight first age-12 extension IDs to the original all-one answers:''')
    add(table(["Extension answers","Total yes / 47","extended=true result","extended=false result","Evidence"],[[label,count(n:='E_age12_extension_'+label),result(n),d(n+'_false')['stage']+("; "+result(n+'_false') if d(n+'_false')['stage']=='complete' else ''),link(n,"true")+'; '+link(n+'_false','false')] for label in ["all_one","all_zero","mixed"]]))
    add('''Mixed uses `id % 2` on the eight new items (three yes). `extended:true` completes in all three cases, and even with no extension answers supplied ([bypass](raw/api/scoring/E_age12_all_yes_bypass.json)). Therefore the flag is a caller-controlled **stop-extension switch**, not proof that an extension round occurred. With the all-zero extension, false and true produce identical reports; with all-one or mixed, false returns another new batch.

**Full all-one chains, keeping `extended:false` at every round:** each row below lists the number of new items in successive extension stages. At every depth after the first batch, a paired `extended:true` request returns complete. Original answers are retained and new IDs appended.''')
    chain_rows=[]
    for age in [3,12,24,36]:
        sizes=[];ceilings=[];depth=0
        while True:
            name=f"E_chain_age{age:02d}_depth{depth:02d}_false";v=d(name)
            if v['stage']!='extension':break
            sizes.append(len(v['items']))
            companion=f"E_chain_age{age:02d}_depth{depth:02d}_true"
            ceilings.append(str(basic(companion)['devAge']) if depth else str(basic('E_age12_all_yes_bypass' if age==12 else f'E_age{age:02d}_all_one_bypass')['devAge']))
            depth+=1
        chain_rows.append([age,len(sizes),", ".join(map(str,sizes)),len(rec_by_name[name]['body']['answers']),"→".join(ceilings+[str(basic(name)['devAge'])]),link(name,"terminal raw")])
    add(table(["Age","Extension stages","New batch sizes","Final answered IDs","Ceilings before/after batches","Evidence"],chain_rows))
    add('''**Observed selection invariants:** extension batches have **at most two items per area**, contain known bank IDs, never repeat an already answered ID in these chains, and may be shorter than eight when fewer candidates remain. The first age-12 batch is balanced 2/2/2/2 and identical across the four boundary orderings; later batches depend on the enlarged answered-ID set. Its returned rates are evaluated at chronological age 12 (including 0 and .02), so it does not simply choose items closest to displayed .5 at chronological age. At global ceiling 53, extension can still occur (age-12 depth 3), and a later complete result can still be capped. Saturation is therefore not itself a terminal stage.

**Client versus API:** the saved client initially sends false, then sends true after one extension, so its normal path has **at most one extension round**. The API itself allows the longer false-flag chains above. Source: [initial result and stage handling](raw/js/beautified/page-5f182d70f1f24a3d.js:360), [classic handler](raw/js/beautified/page-5f182d70f1f24a3d.js:2291). The per-item ranking/eligibility formula for extension candidates is **not fully recovered**; max-two-per-area, unseen-ID selection, the fixed-set minimal trigger, stop flag, and observed chain depths are established. No claim is made for every possible answer pattern.''')

    add('''## F. Input validation and ID scope

All validation probes use age 12 and, except noted, `extended:true`. Known foreign IDs are taken from the returned-age-36 initial list and exclude overlap with age 12.''')
    f_specs=[('F_age12_foreign_age36_only','Only foreign IDs, all yes'),('F_age12_typical_plus_foreign_yes','Typical baseline plus foreign yes'),('F_age12_typical_plus_foreign_no','Typical baseline plus foreign no'),('F_age12_first10_only','Only first 10 baseline answers'),('F_age12_invalid_y_2','One y=2'),('F_age12_invalid_y_minus1','One y=-1'),('F_age12_typical_omit_calibration','Omit three calibration answers'),('F_age12_empty_answers','Empty answers'),('F_age12_typical_plus_unknown','Append unknown ID 999999=yes'),('F_age12_duplicate_first','Duplicate first ID with same value'),('F_age12_duplicate_conflict','Append conflicting first-ID value 0'),('F_age12_duplicate_conflict_first','Prepend conflicting first-ID value 0')]
    add(table(["Input","Submitted count","HTTP","Result","Area months P,C,L,S","Evidence"],[[label,len(rec_by_name[n]['body']['answers']),rec_by_name[n]['http_status'],d(n).get('error') or result(n),areas(n),link(n,'raw')] for n,label in f_specs]))
    add('''**Observed:** foreign known IDs are accepted and scored, not bound to a remembered start response. Adding foreign yes changes the baseline age 14→46; adding foreign no changes it to 11. The same submitted vector can be sent at multiple chronological ages without a session token. This supports a per-ID bank lookup.

Partial answers can complete. First 1–7 all-yes IDs each return `not_enough`; first **8** complete (age 19, capped), and eight extension-only answers can complete even though every individual area is `not_enough`. A minimum of eight effective usable answers is consistent with these tests. Age 1's seven Language answers are `not_enough`, while its other sufficiently sized areas can expose months. This boundary was tested with these ID sets, not every mix of known/unknown IDs.

Non-binary numbers return HTTP 400 `invalid_body`. Omitting calibration is accepted; the typical baseline global score remains 14 but Social-Emotional `atLeast` changes false→true. Unknown ID 999999 is accepted and the **entire response is unchanged** in this single unknown-ID test. Repeated IDs are accepted; equal duplicates do not change the report, and a conflicting duplicate uses the **last value** (appending no yields age 13, prepending it restores age 14). Thus shuffling contradictory duplicates is a different case from shuffling unique answers.

These are permissive-input observations, not a claim that validation is absent: y=2/-1 are rejected, and minimum-answer gating exists. Gestation and birthdate validation were outside this phase.''')

    add('''## G. The all-zero age-1 anomaly

The age-1 all-zero response is reproduced, identical to both Phase 2 captures. All 39 supplied `y` values really are numeric zero.''')
    add(table(["Chronological age","Profile","Result","Area months P,C,L,S","Evidence"],[[age,label,result(n:=f'G_age{age:02d}_'+suffix),areas(n),link(n,'raw')] for age in [0,1,2] for label,suffix in [('All zero','all_zero'),('Only calibration yes','zero_calibration_yes'),('All zero, omit calibration','zero_omit_calibration')]]))
    add('''Additional isolating probes:

| Change | Observed output | Evidence |
| --- | --- | --- |
| Keep age-1 zero IDs, send chronological age 0 | age 1 / on_pace | [raw](raw/api/scoring/G_age00_age01_zero_ids.json) |
| Keep age-1 zero IDs, send age 2 or 12 | below_floor | [age 2](raw/api/scoring/G_age02_age01_zero_ids.json), [age 12](raw/api/scoring/G_age12_age01_zero_ids.json) |
| Send age-0 zero IDs at age 1 | below_floor | [raw](raw/api/scoring/G_age01_age00_zero_ids.json) |
| Send age-2 zero IDs at age 1 | age 1 / on_pace | [raw](raw/api/scoring/G_age01_age02_zero_ids.json) |
| Remove all four anchors from age-1 zero vector | age 1 / on_pace | [raw](raw/api/scoring/G_age01_zero_omit_anchors.json) |
| Remove the entire Physical domain | below_floor | [raw](raw/api/scoring/G_age01_zero_omit_Physical.json) |
| Remove any single one of the 13 Physical IDs | age 1 / on_pace in all 13 | G_age01_zero_omit_id* in [summary](raw/api/scoring/summary.csv) |
| Only the 13 Physical zeros, age 1 | age 2 / well_ahead | [raw](raw/api/scoring/G_age01_age01_Physical_zero_only.json) |
| First ten Physical zeros, age 1 | age 3 / well_ahead | [raw](raw/api/scoring/G_age01_Physical_first10_zero.json) |
| Age-12 IDs, all zero, sent at age 0 | age 5 / well_ahead | [raw](raw/api/scoring/M_age00_initial12_count00.json) |

**Observed explanation of the label:** once the server emits devAge 1 for chronological age 1, the recovered ratio formula produces `on_pace`. The anomaly is not caused by answer booleans, answer ordering, calibration yes values, or a single mandatory Physical milestone. It follows the answered-ID set and chronological floor behavior. The same low-score problem can produce an even more implausible age when older question IDs are supplied for a newborn.

**Inferred cause, not proven:** projection onto the minimum usable norm age may be clamping scores below the supported range, then the relative reporting floor sees that projected age. This is consistent with count-zero Secure Attachment yielding age 1 and count-zero older IDs yielding age 5. The server's norm support and floor code are unavailable, and the age-0 own-list all-zero response behaves differently. Therefore the causal explanation remains **unexplained**; support/clamping is a hypothesis, not a recovered implementation. This anomaly limits interpretation of the numeric report even though the calculation is reproducible.''')

    add('''## H. Skills curves and childPct

Each skill has an inventory, `from/to` age metadata, `total`, `reached`, `focus`, childPct, and a baseline curve. `from/to` are not the child's achieved ages; the curve can extend beyond them (Secure Attachment from=1,to=16 has ages 0–18). The exact statistical definition of from/to is not exposed. Focus/status selection is answer-sensitive; a complete formula for those selections was not a scoring probe target.''')
    add(table(["Check across saved Phase 2 + Phase 3 reports","Matches / total"],[["reached = count(status in {yes,typical})",f"{stats['skills']['reached_status_matches']}/{stats['skills']['total']}"],["childPct = reached / total",f"{stats['skills']['childPct_matches']}/{stats['skills']['total']}"],["Same skill + inventory gives identical curve",f"{stats['curve_stability']['prediction_comparisons']}/{stats['curve_stability']['prediction_comparisons']} repeated comparisons; {stats['curve_stability']['groups']} distinct groups"]]))
    add('''**Observed:** curves do not vary with a child's answers for the same skill inventory. `childPct` does vary, includes inferred `typical` milestones, and is not explicit yes count divided by questions asked. The age-1 all-zero report still counts six unasked newborn milestones as `typical`, giving that skill childPct=.6. Unasked milestones can also remain `open`. This is report inference, not a direct assertion supplied by the caregiver. [Age-1 raw report](raw/api/scoring/G_age01_all_zero.json).

The source draws `pct` as the baseline line, shades between `lo` and `hi`, and places the child's dot at chronological age and childPct. Its text says the shading spans the skill's milestones from earliest to latest, supporting the extrema interpretation rather than a statistical confidence interval. [Chart rendering](raw/js/beautified/page-5f182d70f1f24a3d.js:152), [explanation copy](raw/js/beautified/page-5f182d70f1f24a3d.js:1261).

| Curve example | Baseline values | Served rate comparison |
| --- | --- | --- |
| One-item Phonetics, ID948, age 47 | pct=lo=hi=.843537 | start rate .84 |
| Same skill, age 48 | pct=lo=hi=.833333 | start rate .83 |
| Two-item Developing peer relationships, age 32 | lo=.617778, hi=.836591, pct=.7271845=(lo+hi)/2 | ID694 rate .62; ID619 absent from that start list |
| Same skill, age 37 | lo=.700981, hi=.890535, pct=.795758 | ID694 rate .70 |
| Developing musical skills, age 12 | pct=.5904693333 | only served skill item ID338 has rate .64; not equal |

Sources: [age-42 complete inventory](raw/api/result_age42_all_yes_numeric.json), [age-6 inventory](raw/api/result_age06_all_yes_extended.json), returned-age start lists [47](raw/api/start_age48_gw-null.json), [48](raw/api/start_age49_gw-null.json), [32](raw/api/start_age33_gw-null.json), [37](raw/api/start_age38_gw-null.json), [12](raw/api/start_age13_gw-null.json). Every observed one-item curve has equal pct/lo/hi and every two-item curve has pct=(lo+hi)/2 to floating-point tolerance, as checked in the offline analysis.

**Inference:** `pct` is the mean of underlying item probabilities across the skill inventory's usable norms, with lo/hi the item extrema; start rates are rounded versions of those probabilities. It is **not** generally the mean of the currently served questions for that skill. Full bank per-item probabilities are not returned, so exact whole-bank averaging cannot be verified for every skill. Some curves dip with increasing age: they are empirical-looking baseline arrays, not universally monotone logistic lines.''')

    add('''## I. Report gating and paywall presentation

The API returns both tiers together without authentication in every successful probe. No paid endpoint or checkout was opened. This table distinguishes response schema from presentation in the saved client; it does not assert what a purchased product contains.

| Data/flag | Basic JSON | Detail/top-level JSON | Free classic/hook presentation in saved source |
| --- | --- | --- | --- |
| state, band, devAge, capped, ageMonths | Present on ok | Repeated in detail | Overall age/gauge and ahead badge visible; capped gets a plus/ceiling treatment |
| tier | basic | detail | Metadata; rendering does not consult tier |
| areasLocked | true | Absent | Declares locking; rendering does not consult this field directly |
| teaserArea | Optional | Absent as a standalone field | Fallback strongest-area label |
| areas[{area,state,months,atLeast}] | Absent | Present; months/atLeast absent for not_enough area | Only one strongest area may show its actual numeric months |
| areasDefaultHidden | Absent | Present | If true, even received area months are hidden and the fallback teaser has no number |
| Three other area tiles | No numeric area values | Actual computed values already returned | Locked/blurred tiles contain literal **around 88**, not the child's actual values |
| skills/curves/items/childPct | Not nested in basic | Top-level skills present on ok | Default skills view can render cards; classic/hook show one milestone, blur more and hand off to the paywall |
| activity | Not nested in basic | Top-level activity on ok | Broader plan is promoted through the paywall; recommendation data is already returned |
| below_floor or not_enough | Only state | Detail only state; no numeric report/skills | Alternative incomplete/floor flow; below_floor includes floorActivities |

Evidence: [state storage](raw/js/beautified/page-5f182d70f1f24a3d.js:2322), [free overall report](raw/js/beautified/page-5f182d70f1f24a3d.js:3354), [area hiding/teaser selection](raw/js/beautified/page-5f182d70f1f24a3d.js:3376), [actual teaser age](raw/js/beautified/page-5f182d70f1f24a3d.js:3493), [literal 88](raw/js/beautified/page-5f182d70f1f24a3d.js:3538), [blurred milestones](raw/js/beautified/page-5f182d70f1f24a3d.js:3596), [paywall handoff](raw/js/beautified/page-5f182d70f1f24a3d.js:1904).

**Observed:** gating is substantially client presentation; detail values are already in the public response. The literal blurred 88 tiles are cosmetic placeholders. That does not imply the actual computed overall/area ages or skills are fabricated.

## Verdict

**PARTLY REAL — real computation with defective low-score behavior and cosmetic gating.** The strongest three pieces of evidence are: **(1)** the ascending count lookup predicts 40/40 descending and 6/6 randomized overall scores, while expected-rate totals recover chronological age in 4/4 controls and a published skill norm predicts 11/11 uncapped ages; **(2)** fixed-answer controls reproduce Cognitive ages 8→2→0→12 as successes rise 1→2→3→4, and all-zero profiles can produce on_pace/ahead ages, establishing material scoring defects rather than random response noise; **(3)** the public API supplies actual answer-sensitive detail and skills, while the saved free client locks those values and inserts literal blurred 88 tiles. Thus the underlying report is substantially computed, not merely a fixed decorative result, but it does not meet a consistent monotone developmental-model interpretation at low scores. A single ratio rule explains every numeric band; extension/foreign answers alter scores and ceilings predictably. The unexplained minimum-age/floor behavior and coarse area calibration limit interpretation, and computational evidence does not establish validated developmental measurement.''')

    (ROOT/"SCORING.md").write_text("\n".join(text))
    print(json.dumps(dict(report="SCORING.md",audit=audit,heldout_global=f"{sum(held_global)}/{len(held_global)}",heldout_area=f"{sum(held_area)}/{len(held_area)}",random_global=f"{sum(random_matches)}/{len(random_matches)}"),indent=2))


if __name__=="__main__":main()
