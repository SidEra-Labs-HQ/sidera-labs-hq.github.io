# Design System

## 1. Logo analysis (measured, not assumed)
| Property | Finding |
|---|---|
| File | `SidEra-Labs-S-Logo.jpg`, JPEG, RGB, **1024 × 1024 px**, aspect ratio 1:1 |
| Background | Near-black (mean RGB ≈ 1,1,2). About 85% of pixels are background. Not transparent. |
| Mark | A stylised, hand-drawn "S" with an elliptical orbit swoosh. Pencil/crayon texture. The upper half is silver-white with grey hatching; the lower half and orbit are blue. |
| Brand colours | Blue median ≈ **#0770E2** (10th–90th percentile ≈ #003096 to #28ACFF); silver median ≈ #DCE0E4. |
| Edges | JPEG compression noise around the strokes; usable after thresholding but not vector-clean. |
| Suitability for white | **Not suitable as supplied.** On white the silver half would nearly vanish and a black square would be a hole in the page. |

**Derivatives made** (original preserved untouched at `assets/brand/original/SidEra-Labs-S-Logo.jpg`):
- *Light-background mark* (`sidera-mark-*.png`): background removed with a soft alpha threshold and small-speckle cleanup; blue hues kept; silver/white tones remapped to a graphite ramp (≈ #111 to #707070) while preserving their lightness order, so the hatching still reads. Shape is unchanged and not distorted. **This is a colour adaptation for light backgrounds, not a new logo. The owner should approve it.**
- *Original-colour transparent mark* (`sidera-mark-original-colors-transparent-1024.png`): true colours, transparent background, for use on dark surfaces. Not used on this white site.
- Favicon (`favicon.svg` embeds a 96 px PNG; `favicon.ico` 16/32/48), `apple-touch-icon.png` 180, manifest icons 192/512/maskable 512, and the social image.
- **Limitation:** raster only. A true vector mark would need redrawing by a designer; it was deliberately not invented here.

**Is #2563EB appropriate?** Yes. The logo's blue (#0770E2) is lighter and more saturated; #2563EB is in the same hue family, passes AA on white for text (5.17:1) and keeps the page calm. The logo's own blue is never used for text.

## 2. Colour tokens
| Token | Hex | Use | Contrast on white |
|---|---|---|---|
| `--bg` | #FFFFFF | page | n/a |
| `--surface` | #F7F8FA | panels, code | n/a |
| `--ink` | #111827 | primary text | 17.74:1 |
| `--ink-2` | #374151 | body in long text | 10.31:1 |
| `--muted` | #4B5563 | secondary text | 7.56:1 |
| `--faint` | #6B7280 | mono labels | 4.83:1 (4.55:1 on surface) |
| `--accent` | #2563EB | buttons, rules, focus | 5.17:1 |
| `--accent-strong` | #1D4ED8 | links, small accent text | 6.70:1 |
| `--accent-tint` | #EFF4FF | highlight backgrounds | link on tint 6.08:1 |
| `--amber` / tint | #92400E / #FEF6E7 | "Exploratory" status | 6.60:1 |
| `--teal` / tint | #0F766E / #E8F6F4 | "Live"/verified status | 4.93:1 |
| `--line`, `--line-2` | #E5E7EB, #D1D5DB | hairlines | decorative |

Accent is used for: primary buttons, the current-page underline, status chips, the highlighted word in the home H1, in-page indexes, focus rings. No gradients, no shadows, no dark theme, no toggle.

## 3. Typography
Evaluated: Inter, IBM Plex Sans, Manrope, Geist, IBM Plex Mono. **Chosen: IBM Plex Sans + IBM Plex Mono.** Reasons: one coherent family with an engineering heritage; Plex Sans has real weight range down to Light for large display type; Plex Mono gives labels and code the same proportions; Inter is excellent but is the default of generic templates, and Manrope/Geist are less suited to long-form reading in this tone. Both are SIL OFL 1.1 and are **self-hosted** (`assets/fonts`, latin subset WOFF2: Sans 300/400/500/600, Mono 400/500; about 160 KB in total). `font-display: swap`; two fonts preloaded.

| Role | Spec |
|---|---|
| H1 | Sans 300, clamp(2.35rem, 5.4vw + .5rem, 4.6rem), line-height 1.04, tracking −0.035em |
| H2 | Sans 300, clamp(1.8rem, …, 2.9rem), tracking −0.025em |
| H3 | Sans 500, 1.25rem |
| Body | Sans 400, 1.0625rem / 1.65; measure 68ch |
| Lede | clamp(1.15rem, …, 1.35rem), ink-2, max 56ch |
| Label | Mono 500, .75rem, uppercase, tracking .09em, faint |
| Code | Mono 400, .85rem |

## 4. Layout and spacing
Container 1200 px plus fluid gutters `clamp(1.25rem, 4vw, 3rem)`. Spacing scale 0.25 / 0.5 / 0.75 / 1 / 1.5 / 2 / 3 / 4.5 / 5.5 rem. Section pattern: a 1 px ink rule, a mono number and label on the left, a light-weight H2 on the right. Radius 3 px everywhere (no pill shapes). Breakpoints: 480, 560, 760 (menu), 900, 960, 1000.

## 5. Components
Header (sticky, solid white, hairline), mobile menu button, skip link, buttons (primary / secondary, 46 px min height), status chips, definition list ("At a glance"), index rows (stretched title link), numbered steps, principle list, key-value tables, panels (grey / tinted), sub-navigation with scroll-spy, article layout with sticky contents, figure with caption, note callout, reference list, CTA band, footer.

## 6. Art direction
"A lab notebook that has been edited." Hairline rules, figure captions (`FIG. 1`), numbered sections and mono labels borrow from technical papers. **Illustrations** share one style: 1.5 px ink strokes, a single blue accent, a faint 20 px grid, white card, 320 × 240. They depict the subject itself: attention arcs over tokens; a layered stack above a build pipeline; a four-stage control loop around a state block; a compute-tile fabric with a data path; a two-link arm with reach envelope; an experiment plot with error bars and baseline. **Hero figure:** the real mark at the centre of two orbits (echoing the mark's own swoosh) with six numbered nodes; the legend below is the keyboard and screen-reader route.

## 7. Interaction standards
- No hover-only functions; every hover state also has a focus state.
- Focus: 3 px accent outline, 3 px offset; on SVG nodes a fill plus dark ring.
- Motion: only a 1.8 s ring draw-in on the hero and 150 ms colour/translate transitions; all disabled under `prefers-reduced-motion`.
- Mobile menu: button with `aria-expanded`, `aria-controls`; Escape closes and returns focus; without JavaScript the nav is a visible wrapped list.
- Targets ≥ 44 px for primary controls; orbit nodes are 50 px in the SVG (≈ 27 px at 390 px width) and are a mouse convenience; the legend is the keyboard and screen-reader route.
- Tables scroll inside a bordered wrapper; code blocks are focusable when they scroll.
