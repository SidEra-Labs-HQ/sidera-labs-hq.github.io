#!/usr/bin/env python3
"""Render every page at the required widths in headless Chrome and report layout defects.
Usage: python3 tools/qa_render.py [outdir]   (needs: pip install playwright; a Chrome/Chromium binary)"""
import os, sys, json, threading, http.server, socketserver, functools
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit('Playwright is not installed (pip install playwright). This optional browser test was NOT run.')
from browser_util import launch
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/shots'
os.makedirs(OUT, exist_ok=True)
PAGES = ['', 'about/', 'research/', 'projects/', 'insights/', 'insights/anatomy-of-an-agent-loop/',
         'insights/what-a-result-needs/', 'insights/where-software-meets-hardware/', 'contact/', '404.html']
WIDTHS = [320, 360, 375, 390, 430, 768, 1024, 1280, 1440, 1600, 1920]
SHOT = {390, 1440}
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Q, directory=ROOT)
srv = socketserver.TCPServer(('127.0.0.1', 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start(); PORT = srv.server_address[1]
JS = """() => {
  const de=document.documentElement, r={};
  r.overflowX = de.scrollWidth - de.clientWidth;
  r.wide=[...document.querySelectorAll('body *')].filter(e=>{const b=e.getBoundingClientRect();return b.right>de.clientWidth+1 && b.width>0 && !e.closest('pre,.table-scroll,.subnav,svg,.sr')}).slice(0,5).map(e=>e.tagName+'.'+e.className);
  r.distorted=[...document.querySelectorAll('img')].filter(i=>i.complete&&i.naturalWidth&&Math.abs(i.naturalWidth/i.naturalHeight-i.getBoundingClientRect().width/i.getBoundingClientRect().height)>0.03).map(i=>i.src.split('/').pop());
  r.broken=[...document.querySelectorAll('img')].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.src);
  r.clipped=[...document.querySelectorAll('h1,h2,h3,p,li,a,button,td,th,dd,dt')].filter(e=>{const s=getComputedStyle(e);return !e.classList.contains('sr') && e.scrollWidth>e.clientWidth+2 && s.overflowX!=='visible' && s.display!=='inline'}).slice(0,5).map(e=>e.tagName+':'+(e.textContent||'').slice(0,30));
  r.fonts=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight).length;
  r.h1=document.querySelectorAll('h1').length;
  r.emptyLists=[...document.querySelectorAll('ul,ol')].filter(l=>!l.children.length).length;
  r.emptyImgAlt=[...document.querySelectorAll('img:not([alt])')].length;
  return r;}"""
res = []
with sync_playwright() as p:
    b = launch(p, 'qa_render')
    for pg_path in PAGES:
        for w in WIDTHS:
            ctx = b.new_context(viewport={'width': w, 'height': 900}, reduced_motion='reduce')
            pg = ctx.new_page(); errs = []; fails = []
            pg.on('console', lambda m: errs.append(m.text) if m.type in ('error', 'warning') else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('requestfailed', lambda r: fails.append(r.url))
            pg.on('response', lambda r: fails.append(f'{r.status} {r.url}') if r.status >= 400 and not r.url.endswith('favicon.ico') else None)
            pg.goto(f'http://127.0.0.1:{PORT}/{pg_path}', wait_until='networkidle'); pg.wait_for_timeout(250)
            d = pg.evaluate(JS); d.update(page=pg_path or 'home', width=w, console=errs, failed=fails)
            res.append(d)
            if w in SHOT:
                pg.screenshot(path=f'{OUT}/{(pg_path or "home").strip("/").replace("/","_").replace(".html","")}-{w}.png', full_page=True)
            ctx.close()
    b.close()
bad = [r for r in res if r['overflowX']>0 or r['wide'] or r['distorted'] or r['broken'] or r['clipped'] or r['console'] or r['failed'] or r['h1']!=1 or r['emptyLists'] or r['emptyImgAlt']]
json.dump(res, open(f'{OUT}/results.json', 'w'), indent=1)
print(f'{len(res)} page/width combinations checked; {len(bad)} with findings')
for r in bad[:25]: print({k: v for k, v in r.items() if v not in ([], 0, None) and k not in ('fonts',)})
srv.shutdown()
