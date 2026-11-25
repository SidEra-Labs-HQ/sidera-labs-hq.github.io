# QA Report

All automated results below come from a **local server** (Python `http.server`) using headless Google Chrome via Playwright. Nothing was tested on the deployed site, because nothing has been deployed.

## Results
| Check | Tool | Result |
|---|---|---|
| Links, anchors, titles, descriptions, canonicals, headings, alt text, JSON-LD, sitemap | `tools/check_site.py` | 10 pages checked, 0 failures (re-run 25 Nov 2026 after the final build) |
| Rendering at 320, 360, 375, 390, 430, 768, 1024, 1280, 1440, 1600, 1920 px across all pages (horizontal overflow, distorted or broken images, clipped text, console errors, failed requests, h1 count, empty lists, missing alt) | `tools/qa_render.py` | 110 combinations, 0 findings on the last run |
| Accessibility rules | axe-core via `tools/qa_axe.py` | 0 violations on the last run. Earlier runs found two (an unfocusable scrollable code block; a label/content-name mismatch on row links); both were fixed |
| Lighthouse | Lighthouse on local server | 100 in each category when run on 24 Nov 2026. **Not re-run on 25 Nov**; not run on a real network |
| Independent review | A separate agent, which did not build the site, inspected it in Chrome at 390 and 1440 px | 0 critical, 3 major, 11 minor findings (see below) |

## Independent review: findings and what was done
- **Major, repetitive research blocks:** the layout was alternated and stretched-link rows were reworked; the repetition is partly inherent (six areas with the same structure) and was reduced, not eliminated.
- **Major, orbit figure:** nodes were repositioned onto the two rings, enlarged and made non-focusable (the legend carries the keyboard and screen-reader route).
- **Major, orbit node target size / duplicate tab stops:** fixed by the same change.
- **Minor, honesty and wording:** footer reduced to "© 2026 SidEra Labs"; time-bound project claim reworded; `og:url`/canonical omitted on the noindex 404 page; a fabricated statistic in the research audit was removed.
- **Not changed (accepted):** empty left column beside section headings at wide widths (a deliberate editorial layout, noted as minor); the contact wording "unsponsored collaborations" still needs the owner's confirmation.
- **Reviewer limits:** the reviewer saw only part of the site visually.

## Not tested
- Screen readers (NVDA, JAWS, VoiceOver, TalkBack).
- Safari and Firefox; real mobile devices.
- Lighthouse or WebPageTest against the live URL.
- Crawling external links by script (essay references were checked through search results only).
- The GitHub Actions workflow itself (it has never run).
- Manual WCAG 2.2 audit; the site **targets** AA and automated checks pass, which is not a conformance claim.

## Pre-publication pass, 25 Nov 2026 (all executed in this session)
| Check | Result |
|---|---|
| `python3 tools/build.py` | built 10 pages, 9 in sitemap |
| `python3 tools/check_site.py` | 10 pages checked, 0 failures |
| `python3 tools/test_check_site.py` (project copied beneath `mnt/data/src/`) | PASS, 10 pages checked |
| `bash tools/stage_site.sh` | `_site OK: 41 files`; no `src`, `tools`, `data`, `documentation`, `.github`, original logo, or `.py/.sh/.md` files |
| `tools/qa_render.py` | 110 page/width combinations, 0 with findings |
| `tools/qa_axe.py` | 0 violations |
| Served `_site` locally; screenshots of the project card at 320 and 1440 px | Rendered correctly, no overflow, no console errors; menu button toggles `aria-expanded` |
| Generated titles | All of the form `X | SidEra Labs`; About is exactly `About | SidEra Labs`; home keeps its tagline title |
| Sitemap | 9 indexable URLs, no `lastmod`; 404 excluded |
| External references | OWASP LLM01:2026, ROS 2 Header.msg and the GitHub org page: the OWASP and ROS pages could not be fetched by the tool (not on its allowlist). The NASA Phase I report was read and states the newton-second and pound-force-second mismatch; it says end-to-end testing did not appear to be done and that the root cause "was not caught by the processes in-place" |
| GitHub repository | A logged-out view of the organization page listed `sidera-labs-hq.github.io` as Public. The repository page itself could not be fetched. The live site could not be fetched in this pass |
