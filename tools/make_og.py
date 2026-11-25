#!/usr/bin/env python3
"""Render assets/images/og-sidera-labs.png (1200x630) from HTML using headless Chrome via Playwright."""
import os, sys
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit('Playwright is not installed (pip install playwright). This optional browser test was NOT run.')
from browser_util import launch
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = f'''<!doctype html><meta charset=utf-8><style>
@font-face{{font-family:P;font-weight:300;src:url("file://{ROOT}/assets/fonts/ibm-plex-sans-latin-300-normal.woff2")}}
@font-face{{font-family:P;font-weight:600;src:url("file://{ROOT}/assets/fonts/ibm-plex-sans-latin-600-normal.woff2")}}
@font-face{{font-family:M;font-weight:500;src:url("file://{ROOT}/assets/fonts/ibm-plex-mono-latin-500-normal.woff2")}}
html,body{{margin:0;width:1200px;height:630px;background:#fff;overflow:hidden}}
.f{{position:absolute;inset:36px;border:1px solid #D1D5DB}}
.t{{position:absolute;left:0;right:0;top:0;border-top:3px solid #111827}}
.m{{position:absolute;left:92px;top:130px;width:360px;height:360px}}
svg{{position:absolute;left:40px;top:90px}}
.x{{position:absolute;left:520px;top:150px;width:590px}}
.l{{font:500 18px M;letter-spacing:.1em;text-transform:uppercase;color:#2563EB;margin-bottom:26px}}
h1{{font:300 66px/1.06 P;letter-spacing:-.03em;color:#111827;margin:0}}
.n{{position:absolute;left:520px;bottom:100px;font:600 28px P;color:#111827;letter-spacing:-.01em}} .n i{{font-style:normal;font-weight:300;color:#4B5563}}
.u{{position:absolute;right:76px;bottom:62px;font:500 15px M;color:#6B7280;letter-spacing:.06em}}
</style><div class=f><div class=t></div></div>
<svg width=440 height=440 viewBox="0 0 440 440" fill=none><ellipse cx=220 cy=220 rx=208 ry=84 transform="rotate(-22 220 220)" stroke="#D1D5DB"/><ellipse cx=220 cy=220 rx=176 ry=124 transform="rotate(34 220 220)" stroke="#2563EB" stroke-dasharray="2 5"/></svg>
<img class=m src="file://{ROOT}/assets/brand/sidera-mark-512.png">
<div class=x><div class=l>SidEra Labs</div><h1>Engineering the Next Era of Intelligence.</h1></div>
<div class=n>SidEra <i>Labs</i></div><div class=u>sidera-labs-hq.github.io</div>'''
open('/tmp/og.html','w').write(html)
with sync_playwright() as p:
    b = launch(p, 'make_og', ['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width':1200,'height':630}); pg.goto('file:///tmp/og.html'); pg.wait_for_timeout(600)
    pg.screenshot(path=os.path.join(ROOT,'assets/images/og-sidera-labs.png')); b.close()
print('ok')
