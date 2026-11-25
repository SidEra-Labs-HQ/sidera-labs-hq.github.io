# SidEra Labs website

Official public website for SidEra Labs, an independent engineering and research initiative exploring artificial intelligence, agent systems, software infrastructure, advanced computing, and robotics.

Published at https://sidera-labs-hq.github.io/.

## What this is

SidEra Labs investigates useful technology properly: pick a question, build the smallest thing that can answer it, measure the result, and publish what was found. The site presents the lab's mission, its areas of interest, its projects, and technical essays.

This is a fully static site. There is no backend, database, server code, cookies, analytics, or third-party scripts. It works as plain files served by GitHub Pages.

## Pages

| Page | Purpose |
|------|---------|
| Home | What SidEra Labs is, its areas of interest, listed projects, and working approach |
| About | Identity, mission, engineering philosophy, responsible technology principles, and the limits of the site's claims |
| Research | Six research areas, each with what it investigates, why it matters, open questions, and current status |
| Projects | Verified public projects only, plus the listing standard |
| Insights | Long-form engineering essays with cited sources |
| Contact | The one verified contact route: the SidEra Labs GitHub organization |

## Technology stack

- HTML5, CSS (custom properties, no framework), vanilla JavaScript (~3 KB, progressive enhancement)
- Python 3.8+ standard library build script (`tools/build.py`)
- Fonts: IBM Plex Sans and IBM Plex Mono (SIL Open Font License 1.1, bundled under `assets/fonts/`)
- Icons and illustrations: original, created for SidEra Labs

## Build

```
python3 tools/build.py
```

Reads `src/pages/**/*.html` (front matter plus body), wraps each page in the shared layout, and writes `index.html`, section `index.html` files, `404.html`, `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, and `llms.txt` to the project root.

Set `SIDERA_BUILD_DATE=YYYY-MM-DD` for a reproducible footer year.

## Checks

```
python3 tools/check_site.py      # links, anchors, assets, metadata, JSON-LD, sitemap
python3 tools/test_check_site.py # regression test for path exclusion
```

## Deployment

The site deploys to GitHub Pages via GitHub Actions (`.github/workflows/pages.yml`). The workflow builds, runs checks, stages only public files, and publishes to `main`.

Pushes to `main` trigger an automatic build and deploy.

## Repository

- Source: `SidEra-Labs-HQ/sidera-labs-hq.github.io`
- Live site: https://sidera-labs-hq.github.io/

## License

The site code and content are copyright SidEra Labs. No reuse license has been applied yet. Contact the GitHub organization before reusing any part of this site.

The IBM Plex font files under `assets/fonts/` are licensed separately under the SIL Open Font License 1.1; their license texts are bundled in the same directory.

## Contact

Use the SidEra Labs GitHub organization: https://github.com/SidEra-Labs-HQ

For corrections to this website, open an issue in this repository.
