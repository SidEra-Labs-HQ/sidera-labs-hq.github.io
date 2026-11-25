#!/usr/bin/env python3
"""Run axe-core (WCAG 2.2 A/AA tags) on every page. Usage: AXE=/path/to/axe.min.js python3 tools/qa_axe.py"""
import os, sys, json, threading, http.server, socketserver, functools
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit('Playwright is not installed (pip install playwright). This optional browser test was NOT run.')
from browser_util import launch
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AXE = open(os.environ.get('AXE', '/tmp/axe/node_modules/axe-core/axe.min.js')).read()
PAGES = ['', 'about/', 'research/', 'projects/', 'insights/', 'insights/anatomy-of-an-agent-loop/', 'insights/what-a-result-needs/', 'insights/where-software-meets-hardware/', 'contact/', '404.html']
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT)); threading.Thread(target=srv.serve_forever, daemon=True).start(); PORT = srv.server_address[1]
total = 0
with sync_playwright() as p:
    b = launch(p, 'qa_axe')
    for w in (390, 1280):
        for pg_path in PAGES:
            pg = b.new_page(viewport={'width': w, 'height': 900}, reduced_motion='reduce'); pg.goto(f'http://127.0.0.1:{PORT}/{pg_path}', wait_until='networkidle')
            pg.evaluate(AXE)
            r = pg.evaluate("axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}})")
            for v in r['violations']:
                total += 1; print(f"[{w}] {pg_path or 'home'}: {v['id']} ({v['impact']}) x{len(v['nodes'])} :: {v['nodes'][0]['target']} :: {v['help']}")
            pg.close()
    b.close()
print('axe violations:', total); srv.shutdown()
