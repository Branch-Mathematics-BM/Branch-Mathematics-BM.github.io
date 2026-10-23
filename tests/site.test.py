#!/usr/bin/env python3
"""Static public-link and evidence integrity checks; standard library only."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse,unquote
from collections import Counter
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://branch-mathematics-bm.github.io/'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True);self.refs=[];self.ids=set();self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='a' and a.get('name'):self.ids.add(a['name'])
  for key in ['href','src']:
   if a.get(key):self.refs.append(a[key])
pages={str(p.relative_to(ROOT)):Page(p.read_text()) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
# The previous public ZIP is retained unchanged by the Git tree update.
known_remote={'downloads/Steadman_Yang_Mills_Multi_Plaquette_Review_Bundle_2026-10-09.zip'}
errors=[];checked=0
for path,page in pages.items():
 for ref in page.refs:
  u=urlparse(urljoin(ORIGIN+path,ref))
  if u.scheme not in ['http','https'] or u.netloc!='branch-mathematics-bm.github.io':continue
  p=unquote(u.path).lstrip('/') or 'index.html'
  if p.endswith('/') or (ROOT/p).is_dir():p=p.rstrip('/')+'/index.html'
  if not (ROOT/p).is_file() and p not in known_remote:errors.append({'source':path,'reference':ref,'missing':p});continue
  checked+=1
  if u.fragment and p in pages and unquote(u.fragment) not in pages[p].ids:
   dynamic=p=='theorems.html' and re.fullmatch(r'(?:t\d{2}|w\d{2}|fi\d{2})',u.fragment.lower())
   if not dynamic:errors.append({'source':path,'reference':ref,'missing_anchor':u.fragment})
release=ROOT/'downloads/bm-2026-10-23'
data=json.loads((release/'BM_Completeness_Public_2026-10-23.json').read_text())
assert len(data['inventory'])==645 and len(data['sources'])==23
assert len({r['id'] for r in data['inventory']})==645
assert Counter(r['classification'] for r in data['inventory'])==data['classification_counts']
assert len([r for r in data['inventory'] if r['framework']=='BM'])==336
assert len([r for r in data['inventory'] if r['framework']=='BM' and r['id'].startswith('B-OPEN') and r['classification']=='Hypothesis'])==6
assert not any(s in json.dumps(data) for s in ['/workspace/','libfile_','sandbox:'])
for source in data['sources']:
 p=ROOT/source['url'];assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==source['sha256'],source['id']
checksums=0
for line in (release/'SHA256SUMS.txt').read_text().splitlines():
 digest,name=line.split('  ',1);p=release/name
 assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
 checksums+=1
# Every worker dependency is local and present.
for name in ['bm-core.js','bm-verified.js','verified-worker.js','equation-worker.js','vendor/nerdamer-2.0.0.js']:assert (ROOT/'assets'/name).is_file()
result={'passed':not errors,'html_pages':len(pages),'internal_references_checked':checked,'source_fingerprints':23,'release_checksums':checksums,'errors':errors}
print(json.dumps(result,indent=2))
if errors:sys.exit(1)
