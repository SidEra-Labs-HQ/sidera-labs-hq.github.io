#!/usr/bin/env python3
"""Static checks: links, anchors, assets, titles, descriptions, canonicals, headings, alt text, JSON-LD, sitemap, robots.
Usage: python3 tools/check_site.py   (exit code 1 on any failure)"""
import os, re, sys, json
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://sidera-labs-hq.github.io/'
# Exact directory names (matched against path components relative to the project root).
EXCLUDE_DIRS = {'.git', '.github', 'src', 'documentation', 'node_modules', 'tools', 'data', '_site', '__pycache__'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.links=[]; s.srcs=[]; s.ids=set(); s.h=[]; s.imgs=[]; s.meta={}; s.canon=None; s.title=''; s.ld=[]; s._t=None; s._svg=False; s._ld=False; s._h=None; s.htext=''
    def handle_starttag(s,t,a):
        a=dict(a)
        if 'id' in a: s.ids.add(a['id'])
        if t=='a' and 'href' in a: s.links.append(a['href'])
        if t in('img','script') and 'src' in a: s.srcs.append(a['src'])
        if t=='link' and a.get('rel')=='stylesheet': s.srcs.append(a['href'])
        if t=='link' and a.get('rel')=='canonical': s.canon=a['href']
        if t=='link' and a.get('rel') in('icon','manifest','apple-touch-icon','preload'): s.srcs.append(a['href'])
        if t=='img': s.imgs.append(a)
        if t=='meta': s.meta[a.get('name') or a.get('property')]=a.get('content')
        if t=='title' and not s.title and s._t is None and not s._svg: s._t=''
        if t=='svg': s._svg=True
        if t=='script' and a.get('type')=='application/ld+json': s._ld=True; s.ld.append('')
        if re.fullmatch(r'h[1-6]',t): s._h=t; s.htext=''
    def handle_endtag(s,t):
        if t=='title' and s._t is not None: s.title=s._t; s._t=None
        if t=='svg': s._svg=False
        if t=='script': s._ld=False
        if s._h==t: s.h.append((int(t[1]),s.htext.strip())); s._h=None
    def handle_data(s,d):
        if s._t is not None: s._t+=d
        if s._ld: s.ld[-1]+=d
        if s._h: s.htext+=d
pages={}
for dp,_,fs in os.walk(ROOT):
    parts = os.path.relpath(dp, ROOT).split(os.sep)
    if any(x in EXCLUDE_DIRS for x in parts): continue
    for f in fs:
        if f.endswith('.html'): pages[os.path.relpath(os.path.join(dp,f),ROOT)]=P()
fails=[]; 
def fail(m): fails.append(m); print('FAIL',m)
for rel,p in pages.items(): p.feed(open(os.path.join(ROOT,rel),encoding='utf-8').read())
titles={}; descs={}
for rel,p in pages.items():
    is404=rel=='404.html'; here=os.path.dirname(rel)
    if not p.title: fail(f'{rel}: no title')
    titles.setdefault(p.title,[]).append(rel); descs.setdefault(p.meta.get('description'),[]).append(rel)
    if not p.meta.get('description') or len(p.meta['description'])<70 or len(p.meta['description'])>170: fail(f'{rel}: description length {len(p.meta.get("description") or "")}')
    if len(p.title)>65: fail(f'{rel}: title {len(p.title)} chars')
    if sum(1 for l,_ in p.h if l==1)!=1: fail(f'{rel}: h1 count')
    last=0
    for l,t in p.h:
        if l>last+1 and last: fail(f'{rel}: heading jump h{last}->h{l} ({t[:30]})')
        last=l
    for im in p.imgs:
        if 'alt' not in im: fail(f'{rel}: img missing alt {im.get("src")}')
        if not im.get('width') or not im.get('height'): fail(f'{rel}: img missing width/height {im.get("src")}')
    if not is404:
        url_rel=rel.replace('\\','/')
        exp=BASE+(url_rel[:-10] if url_rel.endswith('index.html') else url_rel)
        if p.canon!=exp: fail(f'{rel}: canonical {p.canon} != {exp}')
        for k in ('og:title','og:description','og:url','og:image','twitter:card','twitter:image'):
            if not p.meta.get(k): fail(f'{rel}: missing {k}')
        if p.meta.get('og:url')!=exp: fail(f'{rel}: og:url mismatch')
        if not p.ld: fail(f'{rel}: no JSON-LD')
    for j in p.ld:
        try: json.loads(j)
        except Exception as e: fail(f'{rel}: bad JSON-LD {e}')
    for l in p.links+p.srcs:
        if l.startswith(('mailto:','tel:','javascript:')): continue
        u=urlparse(l)
        if u.scheme in('http','https'):
            # The project entry deliberately links its own domain (exact site root) as an external link.
            if u.netloc=='sidera-labs-hq.github.io' and l!=BASE: fail(f'{rel}: absolute self-link {l}')
            continue
        if is404 and l.startswith('/'): path=l.split('#')[0].lstrip('/')
        else: path=os.path.normpath(os.path.join(here,u.path)) if u.path else rel
        tgt=os.path.join(ROOT,path)
        if os.path.isdir(tgt): tgt=os.path.join(tgt,'index.html')
        if u.path in('','.','./') and not u.fragment: tgt=os.path.join(ROOT,here,'index.html') if here else os.path.join(ROOT,'index.html')
        if not os.path.exists(tgt): fail(f'{rel}: broken target {l}'); continue
        if u.fragment:
            key=os.path.relpath(tgt,ROOT)
            if u.fragment not in pages.get(key,P()).ids: fail(f'{rel}: missing anchor {l}')
for t,r in titles.items():
    if len(r)>1: fail(f'duplicate title {t}: {r}')
for d,r in descs.items():
    if len(r)>1: fail(f'duplicate description: {r}')
sm=open(os.path.join(ROOT,'sitemap.xml')).read(); locs=re.findall(r'<loc>(.*?)</loc>',sm)
exp={BASE+(r[:-10] if r.endswith('index.html') else r).replace('\\','/') for r in pages if r!='404.html'}
if set(locs)!=exp: fail(f'sitemap mismatch: {set(locs)^exp}')
rb=open(os.path.join(ROOT,'robots.txt')).read()
if 'Sitemap: '+BASE+'sitemap.xml' not in rb: fail('robots.txt sitemap line')
for f in ('favicon.svg','favicon.ico','manifest.webmanifest','.nojekyll','404.html','apple-touch-icon.png'):
    if not os.path.exists(os.path.join(ROOT,f)): fail('missing '+f)
json.load(open(os.path.join(ROOT,'manifest.webmanifest')))
print(f'{len(pages)} pages checked, {len(fails)} failures'); sys.exit(1 if fails else 0)
