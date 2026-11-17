from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, re

R = Path(__file__).resolve().parents[2]
S = Path(__file__).parent
H = lambda b: hashlib.sha256(b).hexdigest()
JH = lambda x: H(json.dumps(x, ensure_ascii=False, sort_keys=True).encode())
manifest = json.loads((S / 'manifest-v2.json').read_text())
decisions = [json.loads(x) for x in (S / 'decisions.jsonl').read_text().splitlines()]
assert len(decisions) == len({x['ad_id'] for x in decisions}) == 141
decision_by_id = {x['ad_id']: x for x in decisions}
units = manifest['units']
assert len(units) == len({x['ad_id'] for x in units}) == 141
assert set(decision_by_id) == {x['ad_id'] for x in units}
fields = ['caption', 'cta_text', 'cta_type', 'title', 'link_description', 'link_url',
          'display_format', 'byline', 'disclaimer_label', 'additional_info',
          'extra_links', 'extra_texts', 'branded_content', 'root_reshared_post']
cardfields = ['body', 'caption', 'title', 'link_description', 'cta_text',
              'cta_type', 'link_url', 'display_format']
native = {}
sources = []
for name, expected in manifest['source_specs']:
    path = R / '_raw/advertiser-census-wave04-2026-10-25/queries' / name
    wrapper = json.loads(path.read_text())
    payload = json.loads(re.search(r'```json\n([\s\S]*?)\n```', wrapper['browser_response']['content'][0]['text']).group(1))
    assert 'view_all_page_id=' + str(wrapper['expected_page_id']) in payload['url']
    ads = [a for c in payload['connections'] for e in c['edges'] for a in e['node']['collated_results']]
    assert len(ads) == expected
    displayed = dict(re.findall(r'Library ID: (\d+)\nStarted running on ([^\n]+)', payload['text']))
    source = dict(source_file=str(path.relative_to(R)), source_file_sha256=H(path.read_bytes()),
                  captured_at=payload['captured_at'], page_id=str(wrapper['expected_page_id']),
                  page_name=ads[0]['page_name'], library_url=payload['url'],
                  native_reported_result_counts=[c['count'] for c in payload['connections']],
                  visible_reported_results=re.findall(r'[^\n]*results[^\n]*', payload['text']),
                  retained_native_ids=len(ads), retained_edges=sum(len(c['edges']) for c in payload['connections']),
                  has_next_page=[c['page_info']['has_next_page'] for c in payload['connections']],
                  ad_ids=[str(a['ad_archive_id']) for a in ads])
    sources.append(source)
    for a in ads:
        ad_id = str(a['ad_archive_id'])
        assert ad_id not in native
        assert str(a['page_id']) == str(wrapper['expected_page_id'])
        assert a['is_active'] is True
        native[ad_id] = (a, source, displayed.get(ad_id))

assert set(native) == set(decision_by_id)
views = {}
for view in manifest['views']:
    path = R / view['file']
    assert H(path.read_bytes()) == view['sha256']
    assert path.stat().st_size == view['bytes']
    text = path.read_text()
    assert re.findall(r'^=== AD (\d+) \|', text, re.M) == view['ad_ids']
    for ad_id in view['ad_ids']:
        assert ad_id not in views
        views[ad_id] = (view, text)
assert set(views) == set(native)

ledger = []
for meta in units:
    ad_id = meta['ad_id']
    a, source, displayed = native[ad_id]
    n = a['snapshot']
    body = n.get('body', {})
    assert not isinstance(body, dict) or set(body) <= {'text'}
    body = body.get('text', '') if isinstance(body, dict) else (body or '')
    bundle = dict(body=body, top={k: n[k] for k in fields if k in n},
                  cards=[{k: c[k] for k in cardfields if k in c} for c in n.get('cards', [])])
    for card in n.get('cards', []):
        assert all(any(z in k.lower() for z in ['image', 'video']) for k in set(card) - set(cardfields))
    # All nonempty scalar text outside the retained copy fields is Page/media metadata.
    allowed_metadata = {'page_id', 'page_name', 'page_profile_picture_url', 'page_profile_uri'}
    assert not {k for k, v in n.items() if isinstance(v, str) and v and k not in fields and k not in allowed_metadata}
    assert not n.get('event')
    unit_path = R / meta['unit_file']
    unit = json.loads(unit_path.read_text())
    assert H(unit_path.read_bytes()) == meta['unit_sha256']
    assert unit['text_bundle'] == bundle
    assert meta['source_file_sha256'] == source['source_file_sha256']
    assert meta['source_file'] == source['source_file']
    assert meta['native_body_sha256'] == H(body.encode())
    assert meta['native_text_bundle_sha256'] == JH(bundle)
    assert meta['native_ad_sha256'] == JH(a)
    assert meta['page_id'] == str(a['page_id'])
    assert meta['snapshot_page_id'] == str(n.get('page_id'))
    assert meta['snapshot_identity_differs'] == (str(n.get('page_id')) != str(a['page_id']))
    assert meta['start_timestamp'] == a['start_date']
    assert meta['start_utc'] == datetime.fromtimestamp(a['start_date'], timezone.utc).isoformat()
    assert meta['displayed_start_date'] == displayed
    assert meta['primary_destination'] == n.get('link_url')
    assert meta['card_destinations'] == [c.get('link_url') for c in n.get('cards', [])]
    view, text = views[ad_id]
    assert '\nBODY\n' + body + '\nTOP TEXT / DESTINATION\n' in text
    assert json.dumps(bundle['top'], ensure_ascii=False, indent=2) in text
    assert json.dumps(bundle['cards'], ensure_ascii=False, indent=2) in text
    decision = decision_by_id[ad_id]
    assert decision['full_available_body_and_card_text_read'] is True
    assert decision['images_viewed'] is False and decision['videos_viewed'] is False
    assert all(decision[k] for k in ['offer_type', 'job', 'product', 'scope', 'note'])
    ledger.append(dict(**meta, **{k: v for k, v in decision.items() if k != 'ad_id'},
                       native_ad_url='https://www.facebook.com/ads/library/?id=' + ad_id,
                       advertiser_library_url=source['library_url'],
                       read_view_file=view['file'], read_view_sha256=view['sha256'],
                       supplied_card_count=len(bundle['cards']),
                       branded_content=n.get('branded_content'),
                       native_body_verified=True, native_cards_and_top_text_verified=True,
                       verification_scope='all retained loaded text; no image/video viewing or unretained variants',
                       independent_purchase_proof=False, spend_revenue_profit_unknown=True))

out = R / 'sources/advertiser04-coordination-registry-reading.jsonl'
assert not (S / 'freeze-manifest.json').exists()
out.write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in ledger))
by_page = []
for source in sources:
    rows = [x for x in ledger if x['source_file'] == source['source_file']]
    by_page.append(dict(**source,
                        read=len(rows), unread=0,
                        oldest_observed_active_start=min(x['start_utc'] for x in rows),
                        newest_observed_active_start=max(x['start_utc'] for x in rows),
                        unique_body_hashes=len({x['native_body_sha256'] for x in rows}),
                        unique_text_bundle_hashes=len({x['native_text_bundle_sha256'] for x in rows}),
                        offer_types=dict(Counter(x['offer_type'] for x in rows)),
                        jobs=dict(Counter(x['job'] for x in rows)),
                        products=dict(Counter(x['product'] for x in rows))))
summary = dict(date='2026-10-25', retained=141, full_text_read=141, unread=0,
               source_files=10, reading_views=20, supplied_cards_read=sum(x['supplied_card_count'] for x in ledger),
               active_native_ids=141, duplicate_native_ids=0,
               snapshot_identity_alias_ids=[x['ad_id'] for x in ledger if x['snapshot_identity_differs']],
               branded_content_ids=[x['ad_id'] for x in ledger if x['branded_content']],
               meaningful_concrete_text_present=141,
               image_video_assets_viewed=0, new_voice_records=0,
               failures=0, ledger_file=str(out.relative_to(R)), ledger_sha256=H(out.read_bytes()),
               source_summaries=by_page,
               offer_types=dict(Counter(x['offer_type'] for x in ledger)),
               jobs=dict(Counter(x['job'] for x in ledger)))
(S / 'verification.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k not in ['source_summaries', 'offer_types', 'jobs']}, indent=2))
