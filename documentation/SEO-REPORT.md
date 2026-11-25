# SEO Report

No one can guarantee a ranking or inclusion in AI-generated answers, and nothing here promises either. The work is technical correctness, useful original content and clear attribution.

## 1. What official guidance says (checked 24 Nov 2026)
| Topic | Finding | Source |
|---|---|---|
| Google, AI features | Google's page on AI features states there are **no additional requirements** to appear in AI Overviews or AI Mode and no special optimizations are necessary; normal SEO best practices apply. Pages in these features count in Search Console's overall search traffic. | https://developers.google.com/search/docs/appearance/ai-features |
| Google, generative AI guide | A separate optimisation guide says creating content people find unique, compelling and useful will likely matter more than other suggestions; an SEJ report says it lists llms.txt among tactics that are not needed. | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide ; https://www.searchenginejournal.com/googles-llms-txt-guidance-depends-on-which-product-you-ask/517651/ |
| llms.txt | Google's John Mueller has said no AI system currently uses llms.txt (June 2025) and has since said such files cannot help LLMs choose sites for discovery. Chrome's Lighthouse has an experimental agentic-browsing audit that checks for it. | https://www.seroundtable.com/google-ai-llms-txt-39607.html ; https://www.searchenginejournal.com/googles-mueller-says-llms-txt-cant-help-llms-differentiate-sites/566027/ ; SEJ link above |
| Search Console verification | Verification methods include HTML file upload and an HTML tag for URL-prefix properties; domain properties need DNS. HTML-file verification works for URL-prefix properties only. | https://support.google.com/webmasters/answer/9008080 |
| Bing import | Bing Webmaster Tools can import verified sites and sitemaps from Google Search Console. | https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools |
| Bing and AI | Bing's guidelines were rewritten to cover Copilot; GEO "doesn't guarantee citations", like SEO doesn't guarantee rankings. Bing recommends submitting a complete sitemap with accurate `lastmod`. Bing offers an AI Performance report in Webmaster Tools. | https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442/ ; https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search ; https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview |
| GitHub Pages workflow | Custom workflows use `actions/configure-pages`, `actions/upload-pages-artifact` and `actions/deploy-pages`; the deploy job needs `pages: write` and `id-token: write`. | https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages |

**Not verified in this session** (a dedicated SEO research agent was cut off by a usage limit): Google's current structured-data feature eligibility for Organization/Article, IndexNow specifics for GitHub Pages, and whether GitHub Pages permits custom response headers. The site does not depend on any of them. GitHub Pages does not let you set arbitrary headers as far as the author knows, but this was not confirmed against GitHub's docs.

## 2. Implemented
- Per page: unique `<title>` (≤ 65 characters) and meta description (70 to 170), one H1, logical headings (checked by script), canonical URL, `lang="en"`, robots meta, Open Graph, Twitter `summary_large_image`, descriptive link text, alt text, width/height on images.
- URLs are short, lowercase, hyphenated and end in `/`.
- `sitemap.xml` (9 indexable URLs with the build date as `lastmod`); `robots.txt` allows all and points to it; `404.html` is `noindex` with no canonical.
- **JSON-LD** (all validated as JSON; none invented): `Organization` (name, URL, logo, description, slogan, `sameAs` = the GitHub organization, which was verified), `WebSite`, `WebPage`/`AboutPage`/`ContactPage`, `BreadcrumbList`, and `Article` on essays (headline, description, author and publisher = the organization, image, section). **No `datePublished`, no `author` person, no address, no phone, no `sameAs` beyond GitHub.** Add `datePublished` when each essay is actually published.
- Crawlable static HTML; content is not injected by JavaScript. Internal links connect every page and every research area, with anchors from the home page and essays.
- Social image 1200 × 630 with alt text.
- `llms.txt`: included as an **experimental, optional** summary. It is not a ranking factor and Google says it is not needed; it can be deleted without effect.

## 3. Name disambiguation (important)
Searching "SidEra Labs" returns mostly **Sidero Labs** (a Kubernetes company), plus unrelated "SAI Labs", "Era" and "Aidera". Mitigations in place: always the exact spelling "SidEra Labs", the full tagline in titles, a one-sentence definition on the home page, and `Organization` markup tied to the GitHub organization. Recommended: keep the GitHub profile README and organization description consistent with the site text, and use the same name and tagline everywhere you publish.

## 4. Keyword map
Volumes were not measured (no keyword tool access); clusters are by intent and fit.
| Page | Primary theme | Supporting phrases used naturally |
|---|---|---|
| Home | SidEra Labs; independent engineering and research initiative | intelligent systems; agent systems; advanced computing; robotics |
| About | what SidEra Labs is; engineering philosophy; responsible technology | research approach; responsible AI principles |
| Research | AI and intelligent systems research areas | developer infrastructure; agent systems; advanced computing; robotics and hardware-integrated engineering; applied research |
| Projects | SidEra Labs projects; open-source repository | prototype vs production |
| Insights | engineering essays | applied AI; research methodology |
| Agent-loop essay | AI agent loop design | workflow vs agent; tool contracts; prompt injection; agent verification |
| Results essay | how to evaluate machine learning results | baselines; random seeds; ablation studies; model cards |
| Hardware essay | hardware-software interface contracts | units and frames; latency budget; safe state; Mars Climate Orbiter |
| Contact | contact SidEra Labs | GitHub |
No keyword lists are stuffed; terms the content does not support (for example claims of products or services) are deliberately absent.

## 5. AI-assisted discoverability
Clear definitions up front, consistent terminology, explicit relationships (organization, areas, essays), headings that state the topic, references to primary sources, and no unsupported claims. No content exists solely for retrieval systems.

## 6. Owner setup guide (no credentials needed from you to me)
**Google Search Console**
1. Go to Search Console and add a **URL prefix** property: `https://sidera-labs-hq.github.io/`.
2. Verify ownership by HTML tag or HTML file. For a file, commit the file Google gives you to the repository root unchanged, and add its name to the `cp` line in `.github/workflows/pages.yml` so it is published; for a tag, add it to the `<head>` in `tools/build.py`.
3. Open Sitemaps and submit `sitemap.xml`.
4. Use URL Inspection on the home page and each essay, and request indexing if they are not indexed. Indexing is not instant or guaranteed.
5. Check Performance after a few weeks, and Pages (indexing) for exclusions.
**Bing Webmaster Tools**
1. Sign in and choose Import from Google Search Console (this brings verified sites and sitemaps), or add the site and verify another way.
2. Confirm the sitemap; review the AI Performance report when data appears.
3. Optional: IndexNow for faster change notification (verify current support before relying on it).
**Do not** add analytics or tracking without deciding on a privacy notice first.

## 7. Open items
- Add `datePublished` to the three essays when published.
- Confirm `https://github.com/SidEra-Labs-HQ` is the preferred capitalization (GitHub URLs are case-insensitive).
- Run Lighthouse against the deployed URL once it is live (results here are from a local server).
