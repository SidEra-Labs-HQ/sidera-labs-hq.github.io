#!/usr/bin/env python3
"""SidEra Labs static site builder. No third-party dependencies (Python 3.8+).

Reads  src/pages/**/*.html   (a small front-matter block, then an HTML body)
Reads  data/projects.json    (verified public projects only)
Writes index.html, <section>/index.html, 404.html, sitemap.xml, robots.txt,
       manifest.webmanifest, llms.txt   into the project root.

Run from anywhere:  python3 tools/build.py
"""
import json, math, os, re, sys, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'pages')
BASE = 'https://sidera-labs-hq.github.io/'
GITHUB_ORG = 'https://github.com/SidEra-Labs-HQ'
SITE = 'SidEra Labs'
TAGLINE = 'Engineering the Next Era of Intelligence.'
# Footer year comes from the build date. Set SIDERA_BUILD_DATE=YYYY-MM-DD for a reproducible build.
BUILD_DATE = os.environ.get('SIDERA_BUILD_DATE', date.today().isoformat())
YEAR = int(BUILD_DATE[:4])

NAV = [('Home', ''), ('About', 'about/'), ('Research', 'research/'),
       ('Projects', 'projects/'), ('Insights', 'insights/'), ('Contact', 'contact/')]

AREAS = [
    dict(n=1, slug='ai-intelligent-systems', title='Artificial Intelligence and Intelligent Systems',
         short='Intelligent Systems', img='ai-intelligent-systems.svg',
         blurb='How learned models behave inside real systems, and how to tell when they can be trusted.'),
    dict(n=2, slug='software-infrastructure', title='Software Engineering and Developer Infrastructure',
         short='Software & Infrastructure', img='software-infrastructure.svg',
         blurb='The build, test and release machinery that decides whether good ideas survive contact with production.'),
    dict(n=3, slug='agent-systems', title='Agent Systems and Intelligent Automation',
         short='Agents & Automation', img='agent-systems.svg',
         blurb='Software that observes, decides and acts in loops, and the controls that keep those loops safe.'),
    dict(n=4, slug='advanced-computing', title='Advanced Computing',
         short='Advanced Computing', img='advanced-computing.svg',
         blurb='Where hardware shape, memory and precision decide what is practical to compute.'),
    dict(n=5, slug='robotics-hardware', title='Robotics and Hardware-Integrated Engineering',
         short='Robotics & Hardware', img='robotics-hardware.svg',
         blurb='Software that has to meet sensors, motors, timing and physics.'),
    dict(n=6, slug='applied-experimental', title='Applied and Experimental Research',
         short='Applied & Experimental', img='applied-experimental.svg',
         blurb='Small, well-posed experiments that turn a hunch into evidence or a clear negative result.'),
]

def esc(s): return html.escape(s, quote=True)

def parse(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m: sys.exit('missing front matter: ' + path)
    meta = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    return meta, m.group(2)

def orbit(root):
    cx, cy = 300, 280
    def pt(rx, ry, rot, t):
        a, r = math.radians(t), math.radians(rot)
        x, y = rx * math.cos(a), ry * math.sin(a)
        return cx + x * math.cos(r) - y * math.sin(r), cy + x * math.sin(r) + y * math.cos(r)
    A = (275, 112, -22); B = (235, 165, 34)
    place = {1: (A, 20), 3: (A, 140), 5: (A, 260), 2: (B, 20), 4: (B, 140), 6: (B, 260)}
    s = ['<svg class="orbit" viewBox="0 0 600 560" role="group" aria-labelledby="orbit-t" focusable="false">',
         '<title id="orbit-t">Six areas of interest arranged on two orbits around the SidEra Labs mark. Numbered nodes link to the Research page; the list beneath the figure gives the same links.</title>',
         f'<line class="axis" x1="20" y1="{cy}" x2="580" y2="{cy}"/><line class="axis" x1="{cx}" y1="20" x2="{cx}" y2="540"/>',
         f'<ellipse class="ring" cx="{cx}" cy="{cy}" rx="{A[0]}" ry="{A[1]}" transform="rotate({A[2]} {cx} {cy})"/>',
         f'<ellipse class="ring hi" cx="{cx}" cy="{cy}" rx="{B[0]}" ry="{B[1]}" transform="rotate({B[2]} {cx} {cy})"/>',
         f'<circle class="ring" cx="{cx}" cy="{cy}" r="86" style="animation:none;stroke-dasharray:none;stroke-dashoffset:0"/>',
         f'<image href="{root}assets/brand/sidera-mark-192.png" x="{cx-64}" y="{cy-64}" width="128" height="128" alt=""/>']
    for t in (60, 110, 230, 300, 340):
        x, y = pt(*A, t); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="#9CA3AF"/>')
    for t in (20, 140, 250, 290):
        x, y = pt(*B, t); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="#9CA3AF"/>')
    for a in AREAS:
        el, t = place[a['n']]; x, y = pt(*el, t)
        s.append(f'<a class="node" data-node="{a["n"]}" href="{root}research/#{a["slug"]}" tabindex="-1" aria-hidden="true">'
                 f'<circle cx="{x:.1f}" cy="{y:.1f}" r="25"/><text x="{x:.1f}" y="{y+5.5:.1f}">{a["n"]}</text></a>')
    s.append('</svg>')
    return '\n'.join(s)

def legend(root):
    li = ''.join(f'<li><a data-node="{a["n"]}" href="{root}research/#{a["slug"]}"><span aria-hidden="true">{a["n"]:02d}</span>{esc(a["short"])}</a></li>' for a in AREAS)
    return f'<ul class="legend" aria-label="Areas of interest">{li}</ul>'

def areas_index(root):
    out = ['<ol class="index">']
    for a in AREAS:
        out.append(f'''<li><div class="row">
<span class="n" aria-hidden="true">{a['n']:02d}</span>
<div><h3><a href="{root}research/#{a['slug']}">{esc(a['title'])}</a></h3><p>{esc(a['blurb'])}</p>
<span class="meta"><span class="chip explore">Exploratory</span></span></div>
<img src="{root}assets/illustrations/{a['img']}" alt="" width="320" height="240" loading="lazy" decoding="async">
</div></li>''')
    out.append('</ol>')
    return '\n'.join(out)

def load_projects():
    p = os.path.join(ROOT, 'data', 'projects.json')
    return json.load(open(p, encoding='utf-8'))

def projects_block(root, compact=False):
    items = load_projects()
    if not items:
        return '<p>No verified public projects are listed yet.</p>'
    out = []
    for it in items:
        i = esc(it['id'])
        out.append(f'''<article class="project" aria-labelledby="proj-{i}">
<div class="project-top"><p class="label">{esc(it['category'])}</p><p class="project-status"><span class="dot" aria-hidden="true"></span><span class="sr">Status: </span>{esc(it['status'])}</p></div>
<h3 id="proj-{i}">{esc(it['name'])}</h3>
<p class="project-domain"><a class="ext" href="{esc(it['url'])}">{esc(it['domain'])}</a></p>
<p class="project-desc">{esc(it['description'])}</p>
<dl class="project-meta"><div><dt>Platform</dt><dd>{esc(it['platform'])}</dd></div>
<div><dt>Source</dt><dd><a class="ext" href="{esc(it['repo'])}">View repository<span class="sr"> for {esc(it['name'])} on GitHub</span></a></dd></div></dl>
</article>''')
    return '\n'.join(out)

def posts_list(root, articles):
    out = ['<ul class="post-list">']
    for m in articles:
        out.append(f'''<li><a class="post" href="{root}{m['path']}">
<span class="label">{esc(m['topic'])}<br>{esc(m['reading'])} read</span>
<span><h3>{esc(m['h1'])}</h3><p>{esc(m['description'])}</p></span>
<span class="arr" aria-hidden="true">&rarr;</span></a></li>''')
    out.append('</ul>')
    return '\n'.join(out)
def jsonld(meta, url, crumbs):
    org = {'@type': 'Organization', '@id': BASE + '#organization', 'name': SITE, 'url': BASE,
           'logo': {'@type': 'ImageObject', 'url': BASE + 'assets/brand/sidera-mark-512.png', 'width': 512, 'height': 512},
           'description': 'SidEra Labs is an independent engineering and research initiative exploring artificial intelligence, software engineering, agent systems, advanced computing and robotics.',
           'slogan': TAGLINE, 'sameAs': [GITHUB_ORG]}
    site = {'@type': 'WebSite', '@id': BASE + '#website', 'url': BASE, 'name': SITE, 'inLanguage': 'en',
            'publisher': {'@id': BASE + '#organization'}}
    graph = []
    t = meta.get('type', 'page')
    if t == 'home':
        graph += [org, site]
    page = {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': meta['title'],
            'description': meta['description'], 'inLanguage': 'en', 'isPartOf': {'@id': BASE + '#website'},
            'publisher': {'@id': BASE + '#organization'}}
    if t == 'about': page['@type'] = 'AboutPage'
    if t == 'contact': page['@type'] = 'ContactPage'
    if t == 'article':
        art = {'@type': 'Article', '@id': url + '#article', 'headline': meta['h1'], 'description': meta['description'],
               'mainEntityOfPage': {'@id': url + '#webpage'}, 'inLanguage': 'en',
               'author': {'@id': BASE + '#organization'}, 'publisher': {'@id': BASE + '#organization'},
               'image': BASE + 'assets/images/og-sidera-labs.png', 'articleSection': meta.get('topic', '')}
        graph.append(art)
    graph.append(page)
    if crumbs:
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(crumbs)]})
    if t != 'home':
        graph.append({'@id': BASE + '#organization', '@type': 'Organization', 'name': SITE, 'url': BASE})
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)

def layout(meta, body, root, url, nav_key, crumbs, noindex=False):
    title = meta['title']
    full_title = title if meta.get('type') == 'home' else f'{title} | {SITE}'
    og_img = BASE + 'assets/images/og-sidera-labs.png'
    nav = ''.join(
        f'<li><a href="{root}{p}"{" aria-current=page" if p == nav_key else ""}>{n}</a></li>' for n, p in NAV)
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large, max-snippet:-1'
    og_type = 'article' if meta.get('type') == 'article' else 'website'
    gsv = ('<meta name="google-site-verification" content="L3Aql-cjZYm9kjBsfjBm2AND7cjTwUi-mxOZi4SjH-U" />\n'
           if meta.get('type') == 'home' else '')
    ld = '' if noindex else f'<script type="application/ld+json">\n{jsonld(meta, url, crumbs)}\n</script>'
    ogurl = '' if noindex else f'<meta property="og:url" content="{url}">'
    canon = '' if noindex else f'<link rel="canonical" href="{url}">'
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(meta['description'])}">
{canon}
<meta name="robots" content="{robots}">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preload" href="{root}assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/ibm-plex-sans-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}css/site.css">{gsv}<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(meta['description'])}">
{ogurl}
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="SidEra Labs mark beside the line: Engineering the Next Era of Intelligence.">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(full_title)}">
<meta name="twitter:description" content="{esc(meta['description'])}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="SidEra Labs mark beside the line: Engineering the Next Era of Intelligence.">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="{root}" aria-label="SidEra Labs, home"><img src="{root}assets/brand/sidera-mark-96.png" width="40" height="40" alt=""><span>SidEra <i>Labs</i></span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav"><span class="bars" aria-hidden="true"></span>Menu</button>
<nav class="nav" id="site-nav" aria-label="Primary"><ul>{nav}</ul></nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<div class="foot">
<div>
<a class="brand" href="{root}" aria-label="SidEra Labs, home"><img src="{root}assets/brand/sidera-mark-96.png" width="40" height="40" alt=""><span>SidEra <i>Labs</i></span></a>
<p style="margin-top:1rem">An independent engineering and research initiative exploring intelligent systems, software, agents, advanced computing and robotics.</p>
<p class="label" style="margin:0">{TAGLINE}</p>
</div>
<nav aria-label="Footer"><h2>Pages</h2><ul>{''.join(f'<li><a href="{root}{p}">{n}</a></li>' for n, p in NAV)}</ul></nav>
<div><h2>Elsewhere</h2><ul>
<li><a class="ext" href="{GITHUB_ORG}">GitHub organization</a></li>
<li><a href="{root}contact/">How to reach us</a></li>
<li><a href="{root}about/#site-notes">Accessibility and site notes</a></li>
<li><a href="{root}sitemap.xml">Sitemap</a></li>
</ul></div>
</div>
<div class="legal"><p>&copy; {YEAR} SidEra Labs</p></div>
</div>
</footer>
<script src="{root}js/site.js" defer></script>
</body>
</html>
'''

def render(rel):
    meta, body = parse(os.path.join(SRC, rel))
    path = meta['path']                      # e.g. '' or 'about/'
    depth = len([p for p in path.split('/') if p])
    root = '/' if meta.get('type') == 'notfound' else '../' * depth
    root_disp = root if root else './'
    if root == '': root_disp = './'
    url = BASE + path
    arts = [parse(os.path.join(dp, f))[0] for dp, _, fs in os.walk(os.path.join(SRC, 'insights')) for f in fs if f.endswith('.html')]
    arts = sorted([m for m in arts if m.get('type') == 'article'], key=lambda m: int(m.get('order', 99)))
    ph = {'{{root}}': root_disp, '{{orbit}}': orbit(root_disp), '{{legend}}': legend(root_disp),
          '{{areas_index}}': areas_index(root_disp), '{{projects}}': projects_block(root_disp),
          '{{posts}}': posts_list(root_disp, arts), '{{year}}': str(YEAR), '{{github}}': GITHUB_ORG}
    for k, v in ph.items(): body = body.replace(k, v)
    crumbs = [('Home', BASE)]
    if path:
        if path.startswith('insights/') and path != 'insights/':
            crumbs += [('Insights', BASE + 'insights/'), (meta.get('h1', meta['title']), url)]
        else:
            crumbs += [(meta.get('crumb', meta['title']), url)]
    else:
        crumbs = []
    nav_key = path.split('/')[0] + '/' if path else ''
    if meta.get('type') == 'notfound': nav_key = '__none__'
    out = layout(meta, body, root_disp, url, nav_key, crumbs, noindex=meta.get('type') == 'notfound')
    dest = os.path.join(ROOT, path, 'index.html') if meta.get('type') != 'notfound' else os.path.join(ROOT, '404.html')
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, 'w', encoding='utf-8').write(out)
    return meta

def main():
    metas = []
    for dp, _, fs in os.walk(SRC):
        for f in sorted(fs):
            if f.endswith('.html'):
                metas.append(render(os.path.relpath(os.path.join(dp, f), SRC)))
    urls = sorted([m for m in metas if m.get('type') != 'notfound'], key=lambda m: (m['path'].count('/'), m['path']))
    # No <lastmod>: per-page modification dates are not tracked, and a build date would misstate them.
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for m in urls:
        sm.append(f'  <url><loc>{BASE}{m["path"]}</loc></url>')
    sm.append('</urlset>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(
        f'# {SITE}: all public pages may be crawled.\nUser-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
    manifest = {'name': SITE, 'short_name': SITE, 'description': TAGLINE, 'start_url': './', 'scope': './',
                'display': 'browser', 'background_color': '#FFFFFF', 'theme_color': '#FFFFFF',
                'icons': [{'src': 'assets/icons/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                          {'src': 'assets/icons/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                          {'src': 'assets/icons/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]}
    open(os.path.join(ROOT, 'manifest.webmanifest'), 'w').write(json.dumps(manifest, indent=2) + '\n')
    ll = [f'# {SITE}', '', f'> {TAGLINE} SidEra Labs is an independent engineering and research initiative. This file is an experimental, optional summary for tools that read it; it is not a ranking signal and the HTML pages are the source of truth.', '', '## Pages']
    for m in urls:
        ll.append(f'- [{m.get("h1", m["title"])}]({BASE}{m["path"]}): {m["description"]}')
    ll += ['', '## Elsewhere', f'- [GitHub organization]({GITHUB_ORG})']
    open(os.path.join(ROOT, 'llms.txt'), 'w').write('\n'.join(ll) + '\n')
    print(f'built {len(metas)} pages, {len(urls)} in sitemap')

if __name__ == '__main__':
    main()
