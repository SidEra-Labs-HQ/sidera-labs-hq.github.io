# Research Audit: 50-site competitive study

Prepared 24 November 2026 for the SidEra Labs website. **50 unique sites** were studied by five research agents working in parallel (10 sites each) and consolidated by the coordinator.

## 1. Method and honest limits

Read this section first. It determines how far the conclusions can be trusted.

- **Tooling.** Sites were read with a web-fetch tool that returns a *summarised text rendering* of a page, plus web search. It does not return pixels, computed CSS or a live DOM. **No site was inspected visually in a browser.** Colours, typefaces and exact layouts were therefore *not observed*; where a note mentions them it is labelled "inferred from general knowledge". Findings about navigation, content structure, copy, metadata and accessibility signals come from fetched text.
- **Allowlist.** Direct fetches of many bare homepage URLs were refused by the session's network allowlist. The agents located pages through web search and fetched the returned links. Several "PARTIAL" entries therefore describe an inner page (an article, an About page, an archive), not the homepage. Each entry's `Status` line names what was actually read.
- **Status vocabulary.** DIRECT = page content was fetched and read (for most this was the homepage only). PARTIAL = only part of the site, or only metadata, was reachable. INFERRED = could not be fetched; the note says what it rests on.
- **Tally.** DIRECT 23, PARTIAL 25, INFERRED 2. Two sites are INFERRED or near it: Stripe Press (nothing usable returned) and ETH Zurich Robotic Systems Lab (blocked; only a third-party page was read).
- **Not studied.** Responsive behaviour, real rendering performance, hover and animation behaviour were not tested on any competitor.
- **Independence of conclusions.** Cross-site patterns below are the agents' reports, spot-checked by the coordinator against the per-site files. They are suggestive, not statistical.

## 2. The 50 sites

| # | Site | URL | Status | Group |
|---|------|-----|--------|-------|
| 1 | OpenAI | https://openai.com | PARTIAL | AI research organizations |
| 2 | Anthropic | https://www.anthropic.com | DIRECT | AI research organizations |
| 3 | Google DeepMind | https://deepmind.google | PARTIAL | AI research organizations |
| 4 | NVIDIA Research | https://research.nvidia.com | DIRECT | AI research organizations |
| 5 | Microsoft Research | https://www.microsoft.com/en-us/research/ | PARTIAL | AI research organizations |
| 6 | IBM Research | https://research.ibm.com | PARTIAL | AI research organizations |
| 7 | Amazon Science | https://www.amazon.science | PARTIAL | AI research organizations |
| 8 | Apple Machine Learning Research | https://machinelearning.apple.com | DIRECT | AI research organizations |
| 9 | Meta AI | https://ai.meta.com | PARTIAL | AI research organizations |
| 10 | Mistral AI | https://mistral.ai | PARTIAL | AI research organizations |
| 11 | MIT CSAIL | https://www.csail.mit.edu | PARTIAL | Academic, independent and education |
| 12 | Stanford HAI | https://hai.stanford.edu/ | DIRECT | Academic, independent and education |
| 13 | Berkeley AI Research (BAIR) | https://bair.berkeley.edu | PARTIAL | Academic, independent and education |
| 14 | Allen Institute for AI (Ai2) | https://allenai.org/ | DIRECT | Academic, independent and education |
| 15 | Hugging Face | https://huggingface.co | PARTIAL | Academic, independent and education |
| 16 | DeepLearning.AI | https://www.deeplearning.ai/?lang=us | DIRECT | Academic, independent and education |
| 17 | EleutherAI | https://www.eleuther.ai | PARTIAL | Academic, independent and education |
| 18 | Distill | https://distill.pub | PARTIAL | Academic, independent and education |
| 19 | Epoch AI | https://epoch.ai | PARTIAL | Academic, independent and education |
| 20 | Cohere Labs | https://cohere.com/research | PARTIAL | Academic, independent and education |
| 21 | Vercel | https://vercel.com | DIRECT | Developer infrastructure and software |
| 22 | Linear | https://linear.app/about | PARTIAL | Developer infrastructure and software |
| 23 | Stripe | https://stripe.com/payments/features | PARTIAL | Developer infrastructure and software |
| 24 | Cloudflare | https://www.cloudflare.com/ | DIRECT | Developer infrastructure and software |
| 25 | GitHub | https://github.blog/news-insights/company-news/how-we-designed-and-wrote-the-narrative-for-our-homepage/ | PARTIAL | Developer infrastructure and software |
| 26 | Mozilla | https://www.mozilla.org/en-US/ | DIRECT | Developer infrastructure and software |
| 27 | Tailscale | https://tailscale.com/ | DIRECT | Developer infrastructure and software |
| 28 | Fly.io | https://fly.io/ | DIRECT | Developer infrastructure and software |
| 29 | Supabase | https://supabase.com/ | DIRECT | Developer infrastructure and software |
| 30 | JetBrains | https://jetbrains.com/company | PARTIAL | Developer infrastructure and software |
| 31 | Boston Dynamics | https://bostondynamics.com | DIRECT | Robotics, hardware and advanced computing |
| 32 | Toyota Research Institute | https://tri.global/ | DIRECT | Robotics, hardware and advanced computing |
| 33 | Adobe Research | https://research.adobe.com/ | DIRECT | Robotics, hardware and advanced computing |
| 34 | Qualcomm Research | https://www.qualcomm.com/research | PARTIAL | Robotics, hardware and advanced computing |
| 35 | Intel Labs | https://www.intel.com/content/www/us/en/research/overview.html | DIRECT | Robotics, hardware and advanced computing |
| 36 | Google Quantum AI | https://quantumai.google | DIRECT | Robotics, hardware and advanced computing |
| 37 | Physical Intelligence | https://www.pi.website/ | DIRECT | Robotics, hardware and advanced computing |
| 38 | Open Robotics | https://openrobotics.org/ | DIRECT | Robotics, hardware and advanced computing |
| 39 | Raspberry Pi | https://www.raspberrypi.com/ | DIRECT | Robotics, hardware and advanced computing |
| 40 | ETH Zurich Robotic Systems Lab | https://rsl.ethz.ch | INFERRED | Robotics, hardware and advanced computing |
| 41 | Quanta Magazine | https://www.quantamagazine.org | PARTIAL | Editorial publications and independent engineering |
| 42 | Stripe Press | https://press.stripe.com | INFERRED | Editorial publications and independent engineering |
| 43 | The Gradient | https://thegradient.pub | PARTIAL | Editorial publications and independent engineering |
| 44 | Ink & Switch | https://www.inkandswitch.com | DIRECT | Editorial publications and independent engineering |
| 45 | Oxide Computer | https://oxide.computer | PARTIAL | Editorial publications and independent engineering |
| 46 | fast.ai | https://www.fast.ai | PARTIAL | Editorial publications and independent engineering |
| 47 | Thoughtworks Technology Radar | https://www.thoughtworks.com/radar | PARTIAL | Editorial publications and independent engineering |
| 48 | Santa Fe Institute | https://www.santafe.edu | DIRECT | Editorial publications and independent engineering |
| 49 | Arc Institute | https://arcinstitute.org | PARTIAL | Editorial publications and independent engineering |
| 50 | Ladybird browser | https://ladybird.org | DIRECT | Editorial publications and independent engineering |

## 3. What the evidence shows

### Strongest approaches
- **Restraint at the top.** OpenAI, Anthropic, Mistral and Physical Intelligence open with one plain statement and one or two actions. Apple's ML research site uses three parallel lists (highlights, publications, events) with "view all" links. Bare statements read as more credible than slogans over video.
- **Dated, tagged lists for research.** Cohere Labs, Stanford HAI, BAIR, Adobe Research, Apple and Amazon Science present work as cards or rows carrying category, date and sometimes authors. This is the clearest way to show a body of work. Sites without dates or items (Ai2's homepage as read) feel vaguer.
- **A few named families, each with a one-line summary.** EleutherAI, Epoch AI and Intel Labs make research easy to browse by grouping it into a small number of labelled areas.
- **Proof instead of adjectives.** Tailscale, Fly.io, Supabase and Cloudflare use concrete detail (code samples, named capabilities). Ladybird shows a dated progress log; Arc Institute pairs numbers with "read the paper" links; Oxide groups its press kit.
- **Trust signals worth copying for a small initiative.** Epoch AI's cite-this block and open-licence statements; Quanta's published AI policy and independence statement; Mozilla's typed cards (Product, Partnership, Program) and pause controls for animation.
- **Minimal navigation.** BAIR (about four links) and Distill (three) against six to nine items plus mega-menus at larger sites.
- **Text-first articles.** fast.ai, Ladybird and IBM's long annual-letter article use single columns, tables of contents and links to papers and code.

### Generic or overused patterns
- Mega-menus, announcement bars, promo overlays, newsletter blocks and very long legal footers (Microsoft, NVIDIA, DeepMind, Amazon, Intel, Raspberry Pi, Thoughtworks, Cohere).
- Carousels as the hero (TRI, DeepMind, Anthropic, IBM per the agents' notes).
- Interchangeable "agents" hero copy at Vercel, Cloudflare, Fly.io and Tailscale, sometimes contradicting their own meta descriptions.
- Logo walls and customer strips pushing research or substance below the fold (Boston Dynamics, Vercel).
- Research buried in one tile or one menu item (Boston Dynamics' "R&D" tile).

### Common weaknesses
- **Accessibility.** Empty, missing or filename alt text (Stanford HAI, BAIR, Cohere, Boston Dynamics, Adobe, Google Quantum AI, fast.ai, Thoughtworks, Ink & Switch, Linear, Stripe); generic "Read more" or "here" link text; zoom blocked or capped (Hugging Face, Meta, Vercel, JetBrains); "#" links (Boston Dynamics); an interactive piece without a keyboard alternative (Ink & Switch's Tenfold). Skip links were reported on only some of the sites read (for example TRI, Intel, Google Quantum AI, Open Robotics, Ai2 and Cohere); the agents did not tally this precisely.
- **SEO.** No site showed JSON-LD in the fetched text. Weak or missing titles and descriptions: TRI's title and H1 are both "Homepage" with no description; Santa Fe Institute's description is "Welcome to Santa Fe Institute"; The Gradient paginates titles as "(Page 10)"; Thoughtworks' Radar description was "FAQs". Multiple H1s (Stripe) or none (Tailscale). Complete Open Graph and Twitter tags were common, so social metadata is table stakes.
- **Rendering.** Qualcomm Research returned a client-rendered shell with almost no text, which is a discoverability risk.

## 4. What SidEra Labs does differently

| Observed convention | SidEra Labs decision |
|---|---|
| Slogan over video or carousel | One plain headline and a paragraph that says what the initiative explores. No video, no carousel. |
| Research as a feed of dated papers | SidEra Labs has no papers, so it **does not imitate a publication feed.** Research areas are described as interests with open questions, and every area carries the same explicit status: no public work yet. |
| Logo walls, metrics, testimonials | None. They would all be invented. The "At a glance" block states stage and public home instead. |
| Mega-menu and big footer | Six top-level links, no dropdowns; a four-column-at-most footer. |
| Cards in repeated three-up grids | Hairline-ruled index rows, a definition list, numbered steps and a two-column editorial layout. Layouts alternate on the Research page. |
| Generic AI imagery | Original line illustrations of the actual subject (attention arcs, a build pipeline, a control loop, a compute fabric, a two-link arm, an experiment plot) plus an orbit figure built around the real mark. |
| Projects page full of showcases | Lists only verified public work (currently this website's own repository), states a listing standard and status vocabulary, and shows an empty-state honestly. |
| Thin metadata | Unique title and description per page, canonical URLs, JSON-LD limited to facts that are true, Open Graph and Twitter cards, a sitemap. |
| Weak alt text and focus | Decorative images get empty alt, meaningful ones a description; visible 3px focus ring; skip link; 44px minimum control height; reduced-motion support. |
| Citations missing on opinion pieces | Each essay ends with a reference list and says what it is not (not SidEra experiments). |

## 5. Design decisions that follow from the research

1. White editorial layout with hairline rules and mono labels; one accent colour used sparingly.
2. Small, honest navigation; no mega-menu.
3. A hero that states the thing, supported by a figure that explains (six areas on two orbits) rather than decorates.
4. Research presented as questions and status, not as a fake publication list.
5. Essays with a table of contents, references and a visible "what this is not" note.
6. Plain, descriptive link text and heading-led structure for both people and retrieval systems.
7. Fully static, no third-party scripts, system-independent fonts served locally.

## 6. Per-site evidence

The notes below are the research agents' own records, lightly reformatted. Treat any colour, font or styling remark as unverified.

### 1. OpenAI

**URL:** https://openai.com (fetched: https://openai.com/research)
**Status:** PARTIAL (homepage blocked by allowlist; the Research landing page was fetched and read)
**Observations:** Top bar lists Research, Products, Business, Developers, Company, Foundation, plus Log in and a Try ChatGPT button; a skip link targets main content. The Research page opens with an eyebrow label, a mission H1, two buttons (research index, safety) and an illustrated hero. Below sit four "focus area" blocks, each with a short paragraph and article cards (thumbnail, title, category, date, reading time), newest first. Title is "Research | OpenAI"; canonical, robots, full OG and summary_large_image Twitter tags present; no JSON-LD seen. Some card alt text is filename-like. Large multi-column footer with locale selector. No filters or widgets visible in the text. Visual style: inferred from general knowledge only.
Lesson for SidEra: Copy the clear eyebrow, H1, two-button hero and topic-grouped cards with dates and reading time; avoid sloppy filename alt text.

### 2. Anthropic

**URL:** https://www.anthropic.com
**Status:** DIRECT (homepage fetched)
**Observations:** Short top nav (News, Research, Policy, Commitments, Company), a Try Claude button and a search link, with a skip link to main content. Hero is a single mission headline, a short paragraph, an autoplaying looping background video with static fallback, and a featured-model callout. An announcements feed of dated cards follows, each with summary and links to details. Research appears only as a nav label on the homepage; a four-item "Learn more" block has a "01 / 04" counter suggesting a carousel. Meta description, OG and Twitter tags are present; no JSON-LD. Accessibility is mixed: skip link and single H1, but several empty alt attributes and generic "Read more" links. Search page exists. Palette and type: inferred from general knowledge only.
Lesson for SidEra: Lead with one plain statement of purpose and a lean five-link nav; avoid generic "Read more" links and empty alt text.

### 3. Google DeepMind

**URL:** https://deepmind.google (fetched: https://deepmind.google/about)
**Status:** PARTIAL (homepage blocked; About page fetched and read)
**Observations:** Four-section mega-menu (Models, Research, Science, About) with persistent "Build with Gemini" and "Try Gemini" calls to action, plus a skip link. The page stacks H2 sections, each with a "Learn more" link and a list of items. A carousel labelled "Slide 1 of 5" showcases research as image cards with short project names and one-line taglines. About content uses in-page jump links and a pull quote. A six-card news grid carries category tags, and a newsletter form closes the page. OG (1200x630) and Twitter tags present; no JSON-LD. Heading hierarchy is clean, but several thumbnails have empty alt text and the footer leaks stray class-name text.
Lesson for SidEra: Present projects as named cards with a one-line tagline and put jump links on long pages; skip the heavy carousel and mega-menu at SidEra's scale.

### 4. NVIDIA Research

**URL:** https://research.nvidia.com (302 redirect to https://www.nvidia.com/en-us/research/)
**Status:** DIRECT (the redirect target, which is the Research landing page, was fetched and read)
**Observations:** The site is a sub-section of the corporate site: a dense corporate mega-menu on top with a secondary Research bar (Labs, Publications, Applications, Areas, Benchmarks, Licensing, Careers, AI Playground). The hero is an H1, a tagline and a "Watch Video" link; then five "Inside the Work" cards, news with a "Load More" button, open-source libraries with short descriptions, an events table, a newsletter form and a long legal footer. Title and meta description are keyword-rich ("Advancing the Latest Technology"); OG and Twitter tags present; no JSON-LD. Skip link and labelled icons exist, but several links point to "#" placeholders. Video sits behind a cookie-consent gate.
Lesson for SidEra: Make the research hub a short list of entry points (areas, publications, code) with an events or news list; avoid burying it under corporate chrome.

### 5. Microsoft Research

**URL:** https://www.microsoft.com/en-us/research/ (fetched: .../about-microsoft-research)
**Status:** PARTIAL (homepage blocked; About page fetched and read)
**Observations:** The navigation text is a very long flat link list (publications, code/datasets, about 17 research areas, lab sites) followed by a large block of Microsoft product and partner links ending in a sitemap link. The page itself has a full-width hero image with a mission headline, two prose paragraphs, a pull quote from the lab's president, a photo collage with descriptive alt text, five bolded "research culture" principles, and image-topped "Engage with us" cards. No papers or projects are listed on this page; they sit behind links. Meta description, OG (type "article"), Twitter and robots tags present; no JSON-LD. Footer is dense with social, share and privacy links.
Lesson for SidEra: Principle statements and a pull quote give an institutional voice; avoid giant link lists and a footer weighed down by the parent brand.

### 6. IBM Research

**URL:** https://research.ibm.com (fetched: https://research.ibm.com/blog/research-annual-letter-2023)
**Status:** PARTIAL (homepage not fetched; one long article was read, truncated at about 100k of 122k characters, no global header or footer visible)
**Observations:** The article page has a Home / Blog breadcrumb, a nine-item in-page table of contents, a card carousel of roughly ten themed items (some with embedded video), a "Deep Dive" tag, date and a 46-minute reading-time value in Twitter metadata. H1/H2/H3 hierarchy is clear, each H2 has a bold italic summary line, and claims link out to papers, GitHub, demos and a publications database, with quantified results. Metadata is flawed: description tags are empty and a date tag (2021) conflicts with the visible 2024 byline. No JSON-LD. Some figure alt text is a filename and some links read "here".
Lesson for SidEra: Long-form write-ups with a table of contents, summary lines and linked evidence build credibility; keep metadata complete and consistent.

### 7. Amazon Science

**URL:** https://www.amazon.science (fetched: https://www.amazon.science/blog?p=5)
**Status:** PARTIAL (homepage not fetched; blog index page 5 was fetched and read)
**Observations:** Five-part top nav (Research with 13 areas, News & blog, Collaborations, Resources, Careers) with header search; menu text repeats for mobile. The blog index has a lead image, H1, intro and a left facet sidebar (research area with counts, tags with an A-Z index, conference, journal, author, date), a "651 results" header, sort control, card list (thumbnail, title, authors, date, teaser, area label) and pagination to 51. Posts are technical deep-dives, though some have generic "Staff writer" bylines. Description, keywords, canonical, OG and Twitter tags present; no JSON-LD. Several alt texts are filenames and some controls have doubled labels. Footer has nine social links including RSS.
Lesson for SidEra: Faceted filtering and tags make a large archive usable; at SidEra's scale use a simple topic filter and good alt text.

### 8. Apple Machine Learning Research

**URL:** https://machinelearning.apple.com
**Status:** DIRECT (homepage fetched)
**Observations:** Minimal local nav (Overview, Research Highlights, Publications, Events, Work with us) with a menu toggle, an H1 and a breadcrumb. The page is three short, parallel sections: two highlight cards (title, date, conference tag, excerpt), two publication cards (area, conference and year tags, authors, "Read paper" link) and two event cards, each with a "view all" link, ending in a careers banner. Publication filters appear to use query parameters (area, conference, year). Title, description, canonical, robots, OG (1200x630 with alt) and Twitter tags present; no JSON-LD. Footer is only privacy, terms and legal links. No skip link visible in the text; the banner alt is generic. Visual styling: inferred from general knowledge only.
Lesson for SidEra: Emulate the restraint of three parallel sections (highlights, publications, events) with a minimal footer; add a skip link and richer alt text.

### 9. Meta AI

**URL:** https://ai.meta.com (fetched: https://ai.meta.com/research/)
**Status:** PARTIAL (only the page head metadata came back; no body content, navigation, hero or footer could be read)
**Observations:** Supportable only from head metadata: the title and description name current model families and open-sourced models; canonical is ai.meta.com/research; robots allow large image and video previews, with a separate Bing noarchive directive. The viewport caps pinch-zoom at 2x, which can hinder low-vision users. The Twitter card value is a title string instead of a card type, so it may be ignored. No structured data, lang attribute, alt text or navigation could be seen. Search results show a blog, datasets and global search section exist under the domain. Layout and style claims: inferred from general knowledge, not asserted here.
Lesson for SidEra: Never restrict zoom, set twitter:card correctly and make sure meaningful content is in server-rendered HTML, not only metadata.

### 10. Mistral AI

**URL:** https://mistral.ai (fetched: https://www.mistral.ai/about)
**Status:** PARTIAL (homepage blocked; About page fetched and read)
**Observations:** Top bar has a logo, "Get in touch", a Menu toggle and tabs (Research, Sovereign AI, Cloud, Customers, Company), plus a "Start building" call to action and a skip link. The About page runs H1 then H2 sections: mission, lab roots, a roughly 20-entry dated timeline with small illustrated icons, three founder cards, a partner logo grid with light/dark variants, and four tagged news cards. Research and products appear through the nav, timeline and news rather than detail pages. Title, description, OG and Twitter tags present, plus Astro view-transition meta; no JSON-LD. Most decorative images have empty alt, which is acceptable; the footer is multilingual with an animated GIF and a gradient image.
Lesson for SidEra: A dated timeline and founder cards make a small team feel real; keep personality in the footer but keep the main content sober.

### 11. MIT CSAIL

**URL:** https://www.csail.mit.edu (root not fetched; https://csail.mit.edu/about fetched; /people failed with client_error)
**Status:** PARTIAL
**Observations:** Only a text extract of the About page came back. It shows a sequence of short labelled blocks and eight section labels (Mission & History, Leadership, Jobs, Awards, Publications, Spin-offs, Stata Center, Visit). The extract did not reveal whether these are menu links, nor any footer, meta, OG, structured data or accessibility markup. Homepage composition, research presentation and visual style could not be verified. Search results show the site separates people, publications and news onto distinct subpages and subdomains (e.g. publications.csail.mit.edu), which hints at a sprawling, lab-by-lab information architecture (inferred from search listings).
Lesson for SidEra: Avoid a sprawling multi-subdomain structure; keep one short, labelled About page and one canonical publications index.

### 12. Stanford HAI

**URL:** https://hai.stanford.edu/
**Status:** DIRECT
**Observations:** Utility bar (Stanford links) above a main nav with nine items (About, Research, Education, Policy, AI Index, News, Events, Industry, Centers & Labs), search icon and Sign Up; five nav groups have nested sub-lists. Hero is a mission statement with two CTAs, then a featured report block, then Research, Education, Policy sections each with a short blurb and "More on" link. Content cards carry thumbnail, headline, byline, date and category tag; Policy uses named pull quotes. Footer has legal links including Accessibility. Fetch exposed only a viewport tag (no title/description/OG visible). Alt text is mixed, many empty; a "Pause Media" control exists.
Lesson for SidEra: Borrow the labelled card anatomy (tag, date, byline) and pull quotes; avoid the institutional mega-nav and a nine-item menu.

### 13. Berkeley AI Research (BAIR)

**URL:** https://bair.berkeley.edu (fetched /blog/about and /blog/archive; root not fetched)
**Status:** PARTIAL
**Observations:** The blog nav is just four links (Subscribe, About, Archive, BAIR) under a logo link. The Archive page is a plain reverse-chronological bulleted list of date, separator and linked title, running from 2017 to Nov 2026. About page says posts come from students, postdocs and faculty about every two weeks, and notes the design derives from the Jekyll "Pixyll" theme. Meta: title, short description ("The BAIR Blog"), canonical, author, OG tags; no JSON-LD or Twitter card. Logo has empty alt; heading hierarchy H1-H3 is clean. Main BAIR research site was not inspected.
Lesson for SidEra: A minimal four-link nav plus a plain dated archive is enough; but write real meta descriptions and alt text, which BAIR skips.

### 14. Allen Institute for AI (Ai2)

**URL:** https://allenai.org/
**Status:** DIRECT
**Observations:** Skip-to-content link first, then a grouped menu (Open models, Applications, Research, News, Institute) with images in panels. Hero is a single mission headline plus "Latest News" link, followed by a vertical stack of feature blocks, each image, "Topic - subtitle" heading, short paragraph and one CTA. Also partners, careers cards, newsletter form and contact block. Homepage shows no dated article cards. Meta is complete: title, description, canonical, OG with 1200x630 image and alt, Twitter large card; no JSON-LD. Footer has four link groups, legal and consent links. Alt text is partial. Includes an external interactive story and an 8x-speed demo GIF.
Lesson for SidEra: Copy the skip link, one-CTA-per-block rhythm and full OG set; avoid a homepage without dates or concrete research items.

### 15. Hugging Face

**URL:** https://huggingface.co (root not fetched; https://huggingface.co/EleutherAI org page fetched)
**Status:** PARTIAL
**Observations:** Fetched the EleutherAI organization page, not the marketing homepage. Top bar has logo, search with a Ctrl K hint, and links to Models, Datasets, Spaces, Docs, Enterprise, Pricing, plus Log In and Sign Up. Page body is a single column of sections (interests, recent activity, papers, team grid, collections, spaces, models, datasets), each with sort, filter and "View all". Rows show task type, size, update time and counts. Meta: title, description, canonical, OG and Twitter card present. Viewport sets user-scalable=no, which blocks pinch-zoom. Many images have empty alt. System theme option in footer.
Lesson for SidEra: Dense, countable listings with metadata read as credible; do not disable zoom.

### 16. DeepLearning.AI

**URL:** https://www.deeplearning.ai/?lang=us
**Status:** DIRECT
**Observations:** Announcement bar plus header with Courses, News (The Batch, letters, research), Community, Membership, For Business and an external link. Hero is an H1 about learning AI engineering, two CTAs and a founder portrait with quote. Sections follow: three-step explainer, app badges with QR code, featured courses with text star ratings and quotes, a learning-path builder, newsletter promo with subscriber count, and a Free vs Pro comparison. Footer has tagline, social, two link columns. Meta: title, description, OG 1200x630, Twitter, canonical, theme-color white; no JSON-LD. Dismissible membership overlay appears. Alt text is mixed.
Lesson for SidEra: Founder-led trust and a path-builder are effective; avoid the funnel feel of promo bars, overlays and plan comparisons for a research initiative.

### 17. EleutherAI

**URL:** https://www.eleuther.ai (fetched /about and /research; root not fetched)
**Status:** PARTIAL
**Observations:** Nav is Staff, Research, About, Papers, Community, Blog (subdomain) and Donate, with a Research menu grouped into three families (Open Source AI, Science, Safety) of three areas each. Pages are single-column prose with one H1 and H2 sections; the research page is a categorized index with a linked heading and one-sentence summary per area. Footer shows CC BY 4.0 license, email, Discord, GitHub, Twitter, Donate. Meta: title, description, canonical, OG and Twitter with alt text, theme color dark (#07090d); no JSON-LD. No skip link or lang attribute visible in fetched text. Site uses dark theme color (from meta).
Lesson for SidEra: Group work into a few named families with one-line summaries and state the content license in the footer.

### 18. Distill

**URL:** https://distill.pub (fetched /about/ and /journal/; root not fetched)
**Status:** PARTIAL
**Observations:** Header has only About, Prize, Submit; footer lists Archive, RSS, GitHub, Twitter and the ISSN. About is a single column of H2 sections with linked example images and italic captions, and says the journal ran 2016-2021 and is on indefinite hiatus. Journal page uses tables for article types and review criteria and describes GitHub-based review. Page head exposes malformed dates ("Invalid Date", "NaN-NaN-NaN"); OG and Twitter present; no JSON-LD. Image alt text not shown. Interactive diagrams are described, not seen in the fetched text.
Lesson for SidEra: Emulate the radical simplicity and explicit editorial standards; avoid broken date metadata and stale-site risk by showing status honestly.

### 19. Epoch AI

**URL:** https://epoch.ai (fetched /about and /research; root not fetched)
**Status:** PARTIAL
**Observations:** Hamburger-triggered mega-menu (Latest; Our work with Publications, Data explorers, Benchmarks; Navigate by topic; About; Contact) repeated in a condensed list. The About/Research page has an H1, banner, an in-page "Contents" anchor list, and sections for mission, research (Drivers, Progress, Impacts), history, commitments, funding, press. Includes a copyable plain-text and BibTeX citation block with CC BY 4.0, a feedback form with labelled fields, and footer columns with newsletter and socials. Meta is thorough (title, description, canonical, OG, Twitter; Astro and Pagefind tags); no JSON-LD. Charts themselves were not in the fetched text.
Lesson for SidEra: Adopt the cite-this block, in-page contents and CC license; avoid hiding all navigation behind a hamburger on desktop.

### 20. Cohere Labs

**URL:** https://cohere.com/research (fetched https://cohere.com/research/press which returned the research landing content)
**Status:** PARTIAL
**Observations:** Announcement bar, then a header with Products, Solutions, Resources, Blog, Research, Company, sign-in and demo CTAs; dropdowns contain featured callouts; a skip link exists. Hero H1 and mission line lead to featured research cards, four icon-led values, a Recent Papers list (topic tag, title, date), model cards, programs, and an FAQ. Footer has an open-science CTA, many link groups, socials, cookie control and a five-language selector. Meta: title, description, canonical, robots, OG with alt, Twitter; no JSON-LD. Featured card images all share the generic alt "Featured Image". Because the fetched URL was /research/press, treat as partial confirmation of the /research page.
Lesson for SidEra: A tagged, dated Recent Papers list is the strongest pattern; avoid corporate chrome and identical alt text.

### 21. Vercel

**URL:** https://vercel.com (plus https://www.vercel.com/about)
**Status:** DIRECT
**Observations:** Header has a skip-to-content link, a grouped Products mega-menu (Agent Stack / Core Platform / Tools), Resources menu, and an "Ask AI" control. Hero is a short claim headline plus three audience statements and two CTAs; below it, three case-study-led sections (each pairing a customer proof line with four feature names), a "Recently shipped" card row, and an agent-onboarding closer. Footer is very large, with a system/light/dark theme selector. Meta: title, short description, full OG/Twitter large-image, canonical, robots max-image-preview; no JSON-LD visible. Viewport blocks pinch-zoom (maximum-scale=1). About page is thin: tagline, three bullets, long investor list; generic "About Us" title. Theme colour exposed as #000.
Lesson for SidEra: Proof-led sections and a theme control are strong, but avoid a thin About page and a generic title; give research real depth and keep zoom enabled.

### 22. Linear

**URL:** https://linear.app/about and https://linear.app/features (homepage root not fetched)
**Status:** PARTIAL
**Observations:** Nav is compact (Product, Resources, Customers, Pricing, Now, Contact) with skip link; "Now" suggests a running updates/changelog-style section (name only; content not read). About opens with a statement H1 and an embedded video with a custom text player (speed 0.25x-2x; no captions seen), then founding facts, leadership cards plus a long unadorned name list, and investor lists. Features page is sparse: a hero, two primary features, six linked topics, and a closing CTA; images carry empty alt text. Titles follow "Page – Linear" pattern; meta descriptions, OG/Twitter large card present; theme-color #08090a is exposed. Stray text artefacts and duplicated link labels were seen in the footer.
Lesson for SidEra: Plain, consistent "Page – Brand" titles and a "Now" page are worth copying; avoid empty alt text and video without transcript.

### 23. Stripe

**URL:** https://stripe.com/payments/features (Payments features page; homepage not fetched)
**Status:** PARTIAL
**Observations:** Layered navigation: global header with grouped product menu, product-level subnav (Overview, Features, Docs), and in-page anchor nav (Accept, Process, Settle, Manage). Content is dense and structured as a capability catalogue (payment methods, 135+ currencies, fraud, reporting) with a pricing callout and repeated "Learn more" links. Footer is exhaustive, with region/language selector, newsletter form, legal and privacy-choice links. Meta: descriptive title, canonical, OG, Twitter large card; A/B-test tags appear in head; hreflang and structured data not confirmable. Accessibility: heading levels inconsistent (several H1s), flag alt text is bare country codes, generic link text, zoom not disabled.
Lesson for SidEra: Anchor-based in-page nav suits long pages; avoid repeated generic "Learn more" links and multiple H1s.

### 24. Cloudflare

**URL:** https://www.cloudflare.com/
**Status:** DIRECT
**Observations:** Header has primary menu, an "Under attack?" utility link, and a "Start building" CTA, under an event banner. H1 is long and claim-heavy, followed by a network-statistics block, logo carousel with a visible Pause control and a testimonial, a transparent three-tier pricing section, a billing-model comparison visual, a simulated agent demo panel, and a closing CTA. Footer groups include Public interest and Compliance. Meta: title, generic description that differs from the H1, canonical, OG, large Twitter card, generator tag shows Astro; theme-color #ff4801 exposed. Hero video is gated by a quality mode; poster image has empty alt. One H1 with H2/H3 structure.
Lesson for SidEra: A visible pause control and concrete numbers build trust; avoid a meta description that contradicts the headline.

### 25. GitHub

**URL:** https://github.blog/news-insights/company-news/how-we-designed-and-wrote-the-narrative-for-our-homepage/ (github.com root not fetched)
**Status:** PARTIAL
**Observations:** Only the engineering blog was read, so nothing is directly known about the current github.com homepage. The article (2021, with a 2026 page chrome) describes a chapter-based homepage narrative, an interactive globe hero, product interfaces rebuilt as HTML vignettes, and an extended open-source design system; it states that copy avoided buzzwords. Blog structure: category mega-menu with seven categories and search, breadcrumb, byline, date, reading time, share links, series navigation, tags, author bio, related posts, newsletter with consent checkbox, four-column footer with social icons. SEO and accessibility meta were not exposed.
Lesson for SidEra: Publishing the design/writing process, with series links and reading time, makes editorial credibility visible; do not assume homepage details from this sample.

### 26. Mozilla

**URL:** https://www.mozilla.org/en-US/ and /en-US/about/
**Status:** DIRECT
**Observations:** Cookie consent banner with accept/reject at equal weight; nav has Products and About us dropdowns split into "Our Mission" and "Our Work". Homepage: welcoming H1 with a mission tagline, product list, foundation/donate block, issue-led editorial cards, a State of Mozilla report promo, a typed card grid (Product, Partnership, Program), latest news with type/topic tags, and an accessible newsletter form with labels and validation. About page leads with a manifesto link, organisation list, story cards, hiring and community links. Footer: Creative Commons note, language list, policy links. Meta: full OG, Twitter "summary" card, canonical; no JSON-LD seen. Hero animation has pause/play; one H1; zoom allowed.
Lesson for SidEra: Mission-first copy, typed content cards, and labelled forms with pause controls are a model for an editorial, trust-focused site.

### 27. Tailscale

**URL:** https://tailscale.com/
**Status:** DIRECT
**Observations:** Top utility bar with event banner, Blog/Docs/Download; main menu (Platform, Solutions, Customers, Community, Partnerships) with dropdowns, plus Pricing, Login and a free sign-up button. The extract showed no single distinct hero headline, only five product teasers, then a product panel, three customer outcome metrics, repeated logo strips, value points and repeated social-post testimonials. Footer: Company, Help & Support (incl. Changelog, Status), Legal, many social links, trademark notices. Meta: title with keyword list, description, canonical, OG and large Twitter card with differing image URLs. No H1 visible in the extract; repeated "Read case study" labels; zoom allowed.
Lesson for SidEra: Outcome metrics with named sources are persuasive; avoid keyword-stuffed titles and a missing H1.

### 28. Fly.io

**URL:** https://fly.io/ (via a search-result variant URL)
**Status:** DIRECT
**Observations:** Simple header (Products menu, Docs, Customers, Pricing, Resources with Blog, Infra Log, Changelog, Status, Log In/Sign Up); mobile menu has labelled open/close controls. Hero is an agent-oriented H1 with "Start free" and "Onboard your agent" (copy-prompt) CTAs. Sections cover integrations, use cases, frameworks, data services, usage figures and testimonials, security points, templates and a comparison page link. Footer has four columns and a newsletter. Meta: title, description, canonical, OG, large Twitter card, theme colour. The page text included a line addressed to AI agents pointing to llms.txt (not acted on). Single H1, H2/H3; some empty alt; duplicated logo grid.
Lesson for SidEra: An engineering voice and a "compared" page are distinctive; consider llms.txt but avoid duplicated content blocks.

### 29. Supabase

**URL:** https://supabase.com/
**Status:** DIRECT
**Observations:** Skip-to-content link; header with Product, Developers, Solutions menus, direct Pricing/Docs/Blog, a live GitHub star count, and "Start your project". Hero is a two-part headline plus a Postgres-first summary and two CTAs. Sections: feature cards, dashboard tools, a real React code sample, six starter templates linking to GitHub, customer quotes, community/Discord, an open-source statement, and a closing CTA. Footer: compliance badges (SOC2, HIPAA, ISO 27001), newsletter, social, legal and a do-not-sell link. Meta: title, description reused in OG/Twitter, canonical, 800x600 OG image, verification tags. Alt text on logos; H1/H2/H3 structure.
Lesson for SidEra: Showing real code and open-source links as proof is credible; copy that approach for research artefacts, not logo walls.

### 30. JetBrains

**URL:** https://jetbrains.com/company (root and product pages not fetched)
**Status:** PARTIAL
**Observations:** The fetch returned mostly head metadata, so body, navigation, hero and footer are not known. Visible signals: title "Company - JetBrains" with the Twitter title differing from the OG title, canonical set, meta description naming IntelliJ IDEA and Kotlin, OG and large Twitter card, a Twitter data label mentioning "IDEs, Team Tools, Languages" and a tagline value, theme-colour #000000, and a Google Tag Manager reference. The viewport sets maximum-scale=1, limiting zoom. Search results also surfaced corporate-overview PDF resources, which hints at downloadable company material (not read).
Lesson for SidEra: Keep OG and Twitter titles consistent and never block zoom; treat anything else about this site as unverified.

### 31. Boston Dynamics

**URL:** https://bostondynamics.com
**Status:** DIRECT (homepage only)
**Observations:** Navigation is a five-group mega-menu (Products, Solutions, Industries, Customers, Company) plus Resources, Support and a Contact Sales button, with drill-down "Back" controls and a dismissible holiday promo bar. The hero has a bold claim headline, one CTA, and a webinar promo. A client-logo strip follows, then alternating full-width product sections (Spot, Stretch, Atlas, Orbit), a five-tile solutions grid, and three blog cards. Research appears only as one "R&D" tile. Meta tags include OG, a large-image Twitter card and a canonical; no JSON-LD is visible. Many images have empty alt text, and mobile "Back" links point to "#".
**Lesson:** Product-first storytelling and a clear CTA work, but avoid burying research in a single tile and avoid empty alt text and "#" links.

### 32. Toyota Research Institute

**URL:** https://tri.global/
**Status:** DIRECT (homepage only)
**Observations:** The page begins with a skip link and a labeled main nav. "Our Work" lists five research areas, beside Publications, News & Features, an external Technical Blog, About and Careers. The H1 is literally "Homepage" and the title is "Homepage | Toyota Research Institute", which is weak SEO. The hero is a five-slide carousel with taglines, followed by vision and mission text and a muted autoplay video. The research list is bare linked headings with no descriptions; news cards carry dates and categories. No meta description, OG tags or structured data are visible. The footer lists locations and a contact email. Generator is Drupal 10.
**Lesson:** Avoid a generic "Homepage" H1/title, missing meta description and a carousel; do keep the skip link, dated and categorized news, and visible contact details.

### 33. Adobe Research

**URL:** https://research.adobe.com/
**Status:** DIRECT (homepage only)
**Observations:** The primary nav is News, Publications, Research Areas, Careers and People, with a second row for fellowships and internships. The hero is "Invent the Future" with a careers CTA and hero video links. Below are four stacked content modules: news with category tags, publications (date, title, authors, area tags), a researcher roll call of twelve names, and a row of eleven research-area icons. "All ... ↗" links lead to listings. Meta is thorough: og:*, Twitter card, and a large-image-preview robots directive. No JSON-LD is visible. Research-area icons have empty alt text, and the publication dates appeared out of order.
**Lesson:** Surfacing publications, people and tags on the homepage builds credibility; ship with correct alt text and data ordering.

### 34. Qualcomm Research

**URL:** https://www.qualcomm.com/research
**Status:** PARTIAL (metadata and JS shell only)
**Observations:** The fetch returned mostly metadata and a "JavaScript required" shell, so layout, nav, hero and footer could not be read. Visible: title "Research & Development | Invention & Innovation | Qualcomm", a descriptive meta description, og:title/type/url/description/image, a Twitter card, and a permissive viewport tag. The header, mega-menu and footer appear to be loaded from separate JSON endpoints, and a GraphQL endpoint and identity-service login endpoints are referenced. No JSON-LD is visible. No alt text, lang or landmark information could be assessed.
**Lesson:** Avoid a client-rendered shell that hides content from crawlers and no-JS users; render core content server-side.

### 35. Intel Labs

**URL:** https://www.intel.com/content/www/us/en/research/overview.html
**Status:** DIRECT (page; main menu items not exposed)
**Observations:** The page is wrapped in heavy corporate chrome: utility bar, a 12-locale selector, a toggled advanced-search panel and a browser-upgrade banner. The hero is "The Future Begins Here" with a short description. Six research-area cards (AI, Compute, Graphics, Edge, Programming, Security) have titles, short blurbs and links. Narrative sections cite roughly $50M a year in university funding and NSF and SRC partnerships. Four featured articles use headline-plus-summary cards with Show more/Show less. There is a skip link and labeled logo links. Meta covers a canonical, robots (noarchive), OG type "company" and a Twitter card. No JSON-LD is visible. The footer is dense with legal links and disclaimers.
**Lesson:** Six clear research-area cards and a skip link are worth copying; avoid corporate chrome and legal-footer bloat that crowd the research story.

### 36. Google Quantum AI

**URL:** https://quantumai.google
**Status:** DIRECT (homepage only)
**Observations:** The page opens with a skip link. Nav groups Learn, Hardware (Roadmap, Lab) and Software, with Research and Careers links, language options (three) and Sign in. The hero uses the word "mission" with a one-line tagline. Two "Featured" slides follow, the first a looping video, each with outbound links to a blog post, paper and video. A News & Resources section toggles between Recent Posts and Resources (course, PDF, lab tour). Meta includes OG with a 1200x675 image, a Twitter card, a canonical and a theme-color tag. No JSON-LD is visible. Hero images have empty alt text.
**Lesson:** A mission line plus one featured story and a clear resources path works; keep the page focused and give featured images real alt text.

### 37. Physical Intelligence

**URL:** https://www.pi.website/
**Status:** DIRECT (homepage only)
**Observations:** Extremely minimal. The nav has a wordmark and three links: Home, Research (the blog index) and Join Us. The hero is one declarative sentence about general-purpose AI for the physical world, a short team paragraph and a single waitlist CTA. Research is a reverse-chronological list of cards, each with a date, title, one-line summary and link, running from late 2024 to October 2026. The footer thanks investors and links to X. Meta description, OG image and a large-image Twitter card are present. No JSON-LD is visible. Alt text, skip link and ARIA could not be assessed from the extract, and no distinctive interactions were visible.
**Lesson:** The strongest model for SidEra: a one-sentence thesis, a dated research list, and almost no chrome; add the accessibility basics it does not visibly show.

### 38. Open Robotics

**URL:** https://openrobotics.org/
**Status:** DIRECT (homepage only)
**Observations:** A four-item nav (Technology Strategy, Donate, Leadership, News) with a skip link and a cart icon. The hero is "Powering the world's robots" with the subhead "Open platforms for robotics." The body is a stack of plain sections for ROS, Gazebo, Open-RMF, ros-controls and infrastructure, each with a short description and an outbound link. No papers or publications are shown; community work is referenced through a showcase link. The footer links GitHub orgs and socials and carries a 2023 copyright line (stale). Meta includes a clear description, OG, a summary Twitter card and a canonical. Heading hierarchy is clean (one H1, then H2s), though some links are bare URLs.
**Lesson:** A clear one-line identity and project-per-section structure is easy to scan; avoid a stale copyright year and bare-URL links.

### 39. Raspberry Pi

**URL:** https://www.raspberrypi.com/
**Status:** DIRECT (homepage only)
**Observations:** A top bar splits audiences (For industry / For home) above a seven-item main menu (Hardware, Software, Documentation, News, Forums, Foundation, Contact). The hero is the friendly headline "There's a computer for that" with a single "Browse our products" CTA. Two product sections follow with prices and buy buttons, then three story cards (thumbnail, H3 title, one-line summary, "Read more →") and promos for the Store, Events and Foundation. The footer is large: a newsletter link, seven social links, about 18 corporate links and an Accessibility link. Meta includes OG and a Twitter card; the generator tag is Gatsby 5.16.1. Heading hierarchy is H1 > H2 > H3. No JSON-LD is visible, and image alt text could not be verified.
**Lesson:** Warm, plain-language copy and a split-audience bar are memorable; avoid the over-large footer and keep one CTA per section.

### 40. ETH Zurich Robotic Systems Lab

**URL:** https://rsl.ethz.ch
**Status:** INFERRED. The site itself was blocked by the allowlist and did not appear in search results. The only related fetched page was a third-party NCCR Robotics directory entry (https://nccr-robotics.ch/lab/robotic-systems-lab-rsl/).
**Observations:** That third-party page is a bare contact listing of four people affiliated with the lab, with phone, email, institution, lab and funding fields and no narrative, imagery or branding. Nothing about the lab's own navigation, hero, footer, SEO or accessibility was observed. Any claim about the real site's design would come from general knowledge (university lab sites are commonly publication-and-people-centric and plain), and is not supported here.
**Lesson:** Academic lab sites favor people and publication density over presentation; borrow that rigor of attribution and avoid a site so plain that the lab's own story is missing.

### 41. Quanta Magazine

**URL:** https://www.quantamagazine.org (fetched: /a-new-era-for-the-dawn-of-life-20261112/, an article page; homepage not fetched)
**Status:** PARTIAL
**Observations:** Primary nav is four subject sections (Physics, Mathematics, Biology, Computer Science) plus Topics and Archive, with a secondary group of formats (Podcasts, Videos, Qualia Essays, Explainers, Q&As). Search has a labelled input and a hint line; newsletter and login are modal-based. Article metadata is thorough: canonical, OG type "article", large-image Twitter card, published and modified timestamps, a 2500x1312 OG image. No JSON-LD was visible in the fetch. Footer carries an "AI Editorial Policy" link and a Simons Foundation independence statement. Raw-URL link text on some social links is a weak accessibility signal. Article body and homepage hero were not exposed. Typography (serif display) is inferred from general knowledge.
Lesson for SidEra: Steal the format-based taxonomy and visible editorial-independence/AI-policy footer statements; keep modal clutter out of the first screen.

### 42. Stripe Press

**URL:** https://press.stripe.com
**Status:** INFERRED
**Observations:** Direct fetch was blocked by the allowlist and WebSearch returned no press.stripe.com page. Only a Goodreads shelf of Stripe Press-tagged books was fetched, which says nothing about the site itself. Titles on it (Hamming, Waldrop, Munger, Cowen, Gil) show the catalog skews to engineering, computing history and company-building classics. Everything about layout, navigation and interaction is from general knowledge: the site is known as a book-as-object storefront with large cover imagery, one page per book and restrained typography. None of that was verified here.
Lesson for SidEra: Treat each publication or project as a distinct object with its own page and identity, but verify the real site before copying any pattern.

### 43. The Gradient

**URL:** https://thegradient.pub (fetched: /page/10/, an archive listing page)
**Status:** PARTIAL
**Observations:** Header has logo (with alt text) and seven links: About, Articles, Newsletter, Podcast, Subscribe, Write, Support. The archive page lists 11 entries, each with share row, linked h2 title, date (DD.Mon.YYYY), author link and category tag. No excerpts appear in the fetched markup, so scanning relies on titles alone. A tag index of 25 categories sits at the bottom. Generator is Ghost 5.33; footer credits Ghost and a theme and includes a tracking pixel. Pagination links did not appear in the extract. Title is just "The Gradient (Page 10)", a weak SEO pattern.
Lesson for SidEra: Add excerpts, descriptive archive titles and real pagination; avoid template-credit and tracking clutter in the footer.

### 44. Ink & Switch

**URL:** https://www.inkandswitch.com
**Status:** DIRECT
**Observations:** Title and description state the identity plainly: an independent research lab on tools for thought. Homepage order is a Tenfold anniversary interactive piece ("click/drag everywhere"), a short mission, four research areas, Featured Work (essays and lab notebooks with type labels and years), Production Software, Lab Meta and Appearances (dated talks with video links). Research areas are linked H2s with a one-line description. Footer has contact links, RSS, newsletter and archive. Heading hierarchy is present, but many icons have empty alt text and the interactive piece shows no stated keyboard alternative. OG tags are present.
Lesson for SidEra: Organize by research themes, label content type and year, and separate lab output from shipped software; give any playful interaction a keyboard path.

### 45. Oxide Computer

**URL:** https://oxide.computer (fetched: /press)
**Status:** PARTIAL
**Observations:** Header has Product, Solutions, Resources, Company, Podcasts, Blog and two CTAs ("Try now", "Contact sales"). The footer repeats navigation, adds an "Info" column of comparison pages and a long list of social profiles. The press page is a single scroll: About, paginated In The Press list (outlet, date), a featured blog post by the CTO, and a Press Kit split into Logo, Hardware and Software with bulk downloads. Metadata includes canonical, OG, Twitter large-image card and a declared dark color scheme; OG images point to a preview domain, a likely bug. Accessibility is mixed: good alt text on hardware images, generic "Download" labels, nav wrapped in H3s. Homepage not fetched.
Lesson for SidEra: A press/media kit page with grouped downloads builds credibility; keep OG image URLs on the production domain and label download links.

### 46. fast.ai

**URL:** https://www.fast.ai (fetched: /about)
**Status:** PARTIAL
**Observations:** The about page is a plain, text-first document: one H1, H2 sections, an "On this page" table of contents, bulleted press coverage and prose bios with talk lists. Header is minimal: home link, About, GitHub, Twitter/X, RSS feed. No footer content appeared in the fetch. Built with Quarto (generator meta). OG tags, a short tagline description and a zoom-permitting viewport are present; images all have empty alt text, some links show raw URLs and the embedded video has no caption. Homepage and course pages were not fetched. Look is inferred from general knowledge to be spare and blog-like.
Lesson for SidEra: A long-form, low-chrome page with an in-page TOC reads credibly; do not leave images unlabeled or a page without a footer.

### 47. Thoughtworks Technology Radar

**URL:** https://www.thoughtworks.com/radar (fetched: /es/radar/faq, Spanish-locale FAQ, Vol. 35)
**Status:** PARTIAL
**Observations:** Radar sub-navigation is Explore, FAQ, Build your own radar, Archive, nested inside a heavy corporate mega-menu with locale selector, search and an AI assistant link. The FAQ explains the model clearly: four quadrants (Techniques, Platforms, Tools, Languages and Frameworks) and four rings (Adopt, Trial, Assess, Caution), where radial position signals confidence. Page has a banner carousel with pause/play, 19 Q&A entries, PDF downloads and newsletter signup. Metadata is weak: description is just "FAQs". Footer lists an accessibility statement and code of conduct. Empty alt text on many images; duplicated menu markup. The radar visualization itself was not seen.
Lesson for SidEra: Explain any classification scheme in plain words (what each level means) and version/archive publications; avoid placeholder meta descriptions and carousels.

### 48. Santa Fe Institute

**URL:** https://www.santafe.edu
**Status:** DIRECT
**Observations:** Seven top-level menu sections (Research, News + Events, Education, People, Applied Complexity, Give, About) with nested lists. Hero is the heading "Science for a Complex World" with a short tagline, followed by a featured article framed as a question and a Freeman Dyson testimonial. People are organized by category (researchers, faculty, scholars, trustees, artists). News is about 17 plain-text headlines with no dates or images in the fetch. Footer lists seven social channels and a funder credit. Meta description is only "Welcome to Santa Fe Institute"; OG/Twitter large-image card present. Social links display raw URLs. Image alt text could not be assessed.
Lesson for SidEra: A question-framed lead and a clear people taxonomy convey intellectual identity; write a real meta description and show dates on news.

### 49. Arc Institute

**URL:** https://arcinstitute.org (fetched: /about)
**Status:** PARTIAL
**Observations:** The about page has no global menu in the extract, only inline links to programs and a Tools Portal. It is one long scroll: mission, five stat blocks (investigators, centers, 400+ staff), two initiative cards, four program cards with images, early achievements, founders with photos, donors and an FAQ. Research appears as short outcome cards with a one- to two-sentence summary and an external "Read the paper" link to a journal. Tools are collapsed into a single portal link. Metadata is complete (title, description, OG with image alt, Twitter card, canonical, robots). Heading hierarchy is clean and images have alt text. FAQ answers did not appear in the extract. Homepage not fetched.
Lesson for SidEra: Pair numeric proof points with plain-language outcome cards linking to primary sources; make sure FAQ answers are crawlable.

### 50. Ladybird browser

**URL:** https://ladybird.org
**Status:** DIRECT
**Observations:** Header has six links (Download, News, Get involved, Sponsors, FAQ, Donate); footer repeats them and adds Organization, Privacy, Trademark, GitHub, Discord, YouTube, X, RSS. Single-column, text-first page under an H1 "A truly independent web browser", one primary CTA and a screenshot with light and dark variants. Sections stack in fixed order: About, three numbered differentiators, dated news, Get involved (with a clone-and-run code block), tiered Sponsors, Support table, FAQ, newsletter. Progress is shown as a dated newsletter/post list. Meta declares light/dark color scheme; alt text is good, but sponsor tiers skip heading levels and FAQ questions are bold text rather than headings.
Lesson for SidEra: A manifesto-style differentiator list, dated progress log and transparent sponsor tiers build trust; use real headings for FAQ items.
