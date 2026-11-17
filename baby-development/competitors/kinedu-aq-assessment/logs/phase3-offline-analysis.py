#!/usr/bin/env python3
"""Offline analysis of phase 2/3 manifests; never makes requests."""
import collections
import csv
import json
import math
import pathlib
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]
BANK = {int(r['id']): r['area'] for r in csv.DictReader((ROOT/'questions.csv').open())}


def records():
    result = []
    for manifest in ['raw/api/requests.jsonl', 'raw/api/scoring/requests.jsonl']:
        p = ROOT / manifest
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            r = json.loads(line)
            body = r.get('body', r.get('request'))
            if body.get('action') != 'result' or r['http_status'] != 200:
                continue
            data = json.loads((ROOT / r['file']).read_text())
            result.append((r, body, data))
    return result


def main():
    rows = records()
    global_groups = collections.defaultdict(list)
    numeric_groups = collections.defaultdict(list)
    area_groups = collections.defaultdict(list)
    curve_groups = collections.defaultdict(list)
    bands = collections.defaultdict(list)
    aggregations = collections.Counter()
    band_predictions = []
    norm_predictions = []
    area_total = aggregation_total = skill_total = status_matches = pct_matches = 0
    for r, body, data in rows:
        basic = data.get('basic', {})
        # Duplicate-ID probes establish last value wins; model effective answers.
        answers = list({a['id']: a for a in body['answers']}.values())
        if data.get('stage') == 'complete':
            key = (body['ageMonths'], tuple(sorted(a['id'] for a in answers)), sum(a['y'] for a in answers))
            value = (basic.get('state'), basic.get('devAge'), basic.get('capped'))
            global_groups[key].append((value, r['file']))
        if basic.get('state') == 'ok':
            key = (tuple(sorted(a['id'] for a in answers)), sum(a['y'] for a in answers))
            numeric_groups[key].append(((basic['devAge'], basic['capped']), r['file']))
            bands[basic['band']].append((basic['devAge']/max(basic['ageMonths'],1), r['file']))
            ratio = basic['devAge']/max(basic['ageMonths'],1)
            predicted_band = 'building' if ratio < .95 else 'on_pace' if ratio <= 1.05 else 'little_ahead' if ratio <= 1.15 else 'well_ahead'
            band_predictions.append((predicted_band == basic['band'], predicted_band, basic['band'], ratio, r['file']))
            areas = data.get('detail', {}).get('areas', [])
            vals = [a['months'] for a in areas if 'months' in a]
            if len(vals) == 4:
                aggregation_total += 1
                for name, val in [('mean', statistics.mean(vals)), ('median', statistics.median(vals)), ('min', min(vals)), ('max', max(vals))]:
                    for rnd, func in [('floor',math.floor),('round_half_up',lambda n: math.floor(n+.5)),('ceil',math.ceil)]:
                        aggregations[name+'_'+rnd] += func(val) == basic['devAge']
            for area in areas:
                area_answers = [a for a in answers if BANK.get(a['id']) == area['area']]
                key = (area['area'], tuple(sorted(a['id'] for a in area_answers)), sum(a['y'] for a in area_answers))
                value = (area['state'], area.get('months'), area.get('atLeast'))
                area_groups[key].append((value, r['file']))
                area_total += 1
        for s in data.get('skills', []):
            skill_total += 1
            status_matches += s['reached'] == sum(i['status'] in ['yes', 'typical'] for i in s['items'])
            pct_matches += s['childPct'] == s['reached']/s['total']
            key = (s['skill'], tuple(i['id'] for i in s['items']))
            curve_groups[key].append((json.dumps(s['curve'],sort_keys=True), r['file']))
    def group_summary(groups):
        eligible = {k:v for k,v in groups.items() if len(v)>1}
        conflicts = [{'key':repr(k),'values':v} for k,v in eligible.items() if len({x[0] for x in v})>1]
        return {'groups':len(groups),'records':sum(map(len,groups.values())), 'repeated_groups':len(eligible),'records_in_repeated_groups':sum(map(len,eligible.values())), 'prediction_comparisons':sum(len(v)-1 for v in eligible.values()),'conflict_groups':conflicts}
    result = {
        'records':len(rows),'global_count_lookup':group_summary(global_groups),
        'numeric_count_lookup_ignoring_age':group_summary(numeric_groups),
        'area_count_lookup':group_summary(area_groups),'curve_stability':group_summary(curve_groups),
        'skills': {'total':skill_total,'reached_status_matches':status_matches,'childPct_matches':pct_matches},
        'bands':{k:{'n':len(v),'min':min(v),'max':max(v)} for k,v in bands.items()},
        'aggregations':{'total':aggregation_total,'exact_matches':dict(aggregations)},
        'band_formula': {'total':len(band_predictions),'matches':sum(p[0] for p in band_predictions),'mismatches':[p for p in band_predictions if not p[0]]},
    }
    curve = next(s['curve'] for s in json.loads((ROOT/'raw/api/result_age01_all_no_numeric.json').read_text())['skills'] if s['skill']=='Secure Attachment')
    for r, body, data in rows:
        if '/M_secure_age00_count' not in r['file']:
            continue
        k = sum(a['y'] for a in body['answers'])
        fraction = k/len(body['answers'])
        predicted = max(1,min(curve,key=lambda c:abs(c['pct']-fraction))['age'])
        area_predicted = min((c for c in curve if c['age']%2==0),key=lambda c:abs(c['pct']-fraction))['age']
        actual = data['basic']['devAge']
        area_actual = next(a['months'] for a in data['detail']['areas'] if a['area']=='Social-Emotional')
        norm_predictions.append({'yes':k,'fraction':fraction,'predicted':predicted,'actual':actual,'capped':data['basic']['capped'],'area_predicted':area_predicted,'area_actual':area_actual})
    result['secure_attachment_norm_inverse'] = {'results':norm_predictions,'global_uncapped_matches':sum(p['predicted']==p['actual'] for p in norm_predictions if not p['capped']),'global_uncapped_total':sum(not p['capped'] for p in norm_predictions),'area_uncapped_matches':sum(p['area_predicted']==p['area_actual'] for p in norm_predictions if not p['capped']),'area_uncapped_total':sum(not p['capped'] for p in norm_predictions)}
    start12 = json.loads((ROOT/'raw/api/start_age13_gw-null.json').read_text())
    assert start12['ageMonths'] == 12
    items = [q for sec in start12['sections'] for q in ([sec['anchor']] if sec.get('anchor') else [])+sec['items']] + start12['calibration']
    full_area_lookup = {}
    for area in ['Physical', 'Cognitive', 'Language', 'Social-Emotional']:
        ids = tuple(sorted(q['id'] for q in items if q['area']==area))
        counts = {}
        for k in range(len(ids)+1):
            outputs = sorted(set(v[0] for v in area_groups.get((area,ids,k),[])))
            counts[k] = [{'state':v[0],'months':v[1],'atLeast':v[2]} for v in outputs]
        drops = [k for k in range(1,len(ids)+1) if len(counts[k])==len(counts[k-1])==1 and counts[k][0]['months'] < counts[k-1][0]['months']]
        full_area_lookup[area] = {'ids':ids,'count_to_outputs':counts,'decreasing_transitions_to_count':drops}
    result['age12_full_area_lookup'] = full_area_lookup
    (ROOT/'logs/phase3-offline-stats.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
