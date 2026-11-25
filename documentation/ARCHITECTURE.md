# Architecture

## Principles
Fully static. No backend, database, server code, cookies or third-party requests. Works as plain files on GitHub Pages. Progressive enhancement: the site is complete without JavaScript.

## Repository layout
```
index.html, about/, research/, projects/, insights/, contact/, 404.html   generated pages (committed)
css/site.css          single stylesheet with design tokens (CSS custom properties)
js/site.js            ~3 KB: mobile menu, orbit/legend linking, scroll-spy; no libraries
assets/               brand, images, illustrations, icons, fonts
src/pages/**.html     page sources: small front-matter block + HTML body
data/projects.json    verified public projects (rendered on Home and Projects)
tools/build.py        dependency-free Python build
tools/check_site.py   static checks (links, anchors, metadata, JSON-LD, sitemap)
tools/qa_render.py, tools/qa_axe.py, tools/make_og.py   QA and asset scripts (Playwright)
robots.txt, sitemap.xml, llms.txt, manifest.webmanifest, favicon.*, .nojekyll   generated or static
.github/workflows/pages.yml   build, check, publish public files only
documentation/        internal documents (not published)
```
## Build
`python3 tools/build.py` reads `src/pages`, wraps each page in the shared layout (head metadata, JSON-LD, header, footer), generates the hero orbit figure and the research index, and writes pages plus `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, `llms.txt`. Front matter keys: `type` (home, page, about, contact, article, notfound), `path`, `title`, `h1`, `description`, `crumb`, `topic`, `reading`, `order`. Placeholders: `{{root}}`, `{{orbit}}`, `{{legend}}`, `{{areas_index}}`, `{{projects}}`, `{{posts}}`, `{{github}}`.
**Why a script and not a framework:** header, footer, SEO head and JSON-LD must stay identical across ten pages; a 300-line script does that with no dependencies, and the output is plain HTML you can read.

## Paths
Pages use **relative** paths computed from depth, so the site works from the file system, a local server, or a project-site subpath. Canonical URLs, sitemap and Open Graph use the absolute base `https://sidera-labs-hq.github.io/` (constant `BASE` in `build.py`). `404.html` uses root-absolute paths because GitHub Pages serves it at arbitrary URLs.

## GitHub Pages compatibility
User site: repository must be named exactly `sidera-labs-hq.github.io` in the `SidEra-Labs-HQ` account (it already exists and is public, per the organization page read on 24 Nov 2026). `.nojekyll` disables Jekyll. Custom `404.html` at the root. The workflow publishes an **allowlist** of public files (see below) so `src/`, `tools/`, `data/`, `documentation/` and the original logo are not served.

## Performance decisions
The staged public artifact (`_site`, produced by `tools/stage_site.sh`) contained 41 files on 25 Nov 2026. The script removes the original logo and the two unused 1024 px logo derivatives from the staged copy and fails if internal paths or file types are present. One render-blocking CSS file (~25 KB). Two preloaded fonts. Hero image is not lazy; list illustrations are `loading="lazy"` with explicit dimensions (no layout shift). No JavaScript on the critical path (`defer`).

## Dependencies
Runtime: none. Build: Python 3.8+ standard library. QA only: Playwright, a Chrome binary, axe-core, Lighthouse.
## Security and privacy
No forms, storage, cookies, analytics or external hosts. External links use `rel="noopener"` (added by JS and not needed without `target`). No secrets exist in the tree.
## Extending
Add a project: append to `data/projects.json` and rebuild. Add an essay: create `src/pages/insights/<slug>/index.html` with `type: article`, rebuild, and it appears in lists, the sitemap and `llms.txt`.
