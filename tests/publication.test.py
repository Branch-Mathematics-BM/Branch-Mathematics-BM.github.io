#!/usr/bin/env python3
"""Verify the additive publication against source fingerprints and dated archives."""
from pathlib import Path
import hashlib, json, subprocess, zipfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
release=ROOT/'downloads/bm-2026-11-13'
manifest=json.loads((release/'manifest.json').read_text())
assert len(manifest['files'])==len({x['path'] for x in manifest['files']})
for row in manifest['files']:
    p=release/row['path']
    assert p.is_file() and p.stat().st_size==row['bytes'],row['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
for line in (release/'SHA256SUMS.txt').read_text().splitlines():
    digest,name=line.split('  ',1)
    assert hashlib.sha256((release/name).read_bytes()).hexdigest()==digest,name
base=json.loads((ROOT/'downloads/bm-2026-10-23/BM_Completeness_Public_2026-10-23.json').read_text())
supp=json.loads((release/'BM_November_Result_Supplement.json').read_text())
assert len(supp['inventory'])==manifest['november_result_summaries']==32
assert len(base['inventory'])==645
assert not ({x['id'] for x in base['inventory']} & {x['id'] for x in supp['inventory']})
source_map={s['id']:s for s in supp['sources']}
for row in supp['inventory']:
    assert row['sources'] in source_map
    assert all(row[k] for k in ['statement','assumptions','evidence','remaining_work'])
for s in supp['sources']:
    assert hashlib.sha256((ROOT/s['url']).read_bytes()).hexdigest()==s['sha256']
replays=json.loads((release/'Website_Replay_2026-11-13.json').read_text())
assert len(replays['checks'])==14 and all(x['exit_code']==0 for x in replays['checks'])
assert len([x for x in replays['checks'] if '2026-11-01' in x['script']])==8
source_notes=[p for p in release.glob('BM_*.md') if p.name!='BM_Research_Reading_Collection_2026-11-13.md']
assert len(source_notes)==18
# Original ZIPs remain self-verifiable, including their copied dependencies.
archives=0
for p in release.glob('*.zip'):
    if '2026-11-13' in p.name:continue
    with zipfile.ZipFile(p) as z:
        for line in z.read('SHA256SUMS.txt').decode().splitlines():
            if not line.strip():continue
            digest,name=line.split(None,1)
            assert hashlib.sha256(z.read(name.lstrip('* '))).hexdigest()==digest
    archives+=1
assert archives==3
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
locs=[x.text for x in ET.parse(ROOT/'sitemap.xml').findall('.//s:loc',ns)]
assert len(locs)==len(set(locs))
for name in ['updates.html','seed-closure.html']:
    assert 'https://branch-mathematics-bm.github.io/'+name in locs
    assert 'MathJax' in (ROOT/name).read_text()
assert not any(s in json.dumps(manifest) for s in ['libfile_','sandbox:','/workspace/'])
print(json.dumps({'passed':True,'release_files':len(manifest['files']),'dated_source_notes':18,'new_result_summaries':32,'source_replay_commands':14,'original_archives':archives}))
