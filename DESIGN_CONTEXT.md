# Portfolio UI / Design Context

## 1) Tech Stack

- **App framework:** Flask (Python) server-rendered templates (`app.py` + Jinja in `templates/`).
- **Frontend architecture:** Plain HTML templates + one global stylesheet (`public/style.css`). The only JavaScript is the small inline script for the hero chart animation in `templates/index.html`.
- **Styling system:** Custom CSS (no Tailwind, no CSS modules, no styled-components, no UI component library).
- **Visual direction:** Minimal, editorial, dark. Two typefaces, one accent, no decorative chrome.
- **Fonts and loading:** Google Fonts via one `<link>` per template: `DM Serif Display` (regular + italic) and `Lato` (400). Nothing else.
- **Deployment target:** Vercel (Python function) via `vercel.json` with `app.py` max duration 30s.

## 2) Design Tokens

All tokens live in `:root` in `public/style.css`. The site is dark-only.

| Token | Value | Use |
|---|---|---|
| `--color-bg` | `#0F1117` | Page background (flat; no gradients or textures) |
| `--color-surface` | `#161922` | Screenshot frames |
| `--color-text-heading` | `#ECECEA` | Headings, link text, meta values |
| `--color-text-body` | `#A9ADB5` | Body copy, tagline |
| `--color-text-muted` | `#7C818B` | Labels, dates, notes, TODOs |
| `--color-line` | `rgba(255,255,255,0.10)` | Hairlines and frame borders |
| `--color-line-strong` | `rgba(255,255,255,0.28)` | Link underlines |
| `--color-accent` | `#EA580C` | "Open to APM roles", "Latest", focus ring |
| `--color-accent-hover` | `#F97316` | Link and Thoughts-row hover |

- `--font-display` (DM Serif Display): name, page and section titles, project titles, post titles, pull quotes, PRD key metrics.
- `--font-body` (Lato 400): everything else.
- `--radius: 8px`: the only corner radius (screenshot frames).
- `.container`: max 1200px, 24px side padding (20px under 640px). Case-study pages narrow it to 880px.

### Rules

- Sentence case everywhere. No uppercase or letter-spaced labels, no monospace.
- The accent marks availability, hover and focus only — never headings, body text or decoration.
- No numbering (01/02…), captions, window chrome, badges or pills, icons, shadows, gradients or textures.
- One animated moment: the hero chart (see below). No other scroll-triggered or load animations; otherwise only hover color/opacity transitions (≤ 0.2s). Smooth anchor scrolling only under `prefers-reduced-motion: no-preference`.
- Links are underlined text (`.case-chapter__cta`). `↗` marks links that open a new tab; `←`/`→` only for back, previous and next.
- `:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 3px; }`. Do not suppress outlines.

## 3) Layout Architecture

### Home (`templates/index.html`)

1. **Header (`.site-header`)** — static (not sticky). `AP` links home; nav: Work, About, Thoughts, Resume ↗.
2. **Hero (`.hero .hero-grid`)** — two columns (`7fr / 5fr`, stacked under 900px).
   - Left: one intro line (credentials + accent "Open to APM roles", which drops to its own line under 640px), name as `h1`, serif tagline in body color, lede (max 56ch), two text links.
   - Right: `figure.hero-gap`, an SVG chart of the lede's idea — a dashed muted line ("What products assume") and a solid accent line ("What users do"). The script draws both lines, shades "The gap" between them, then raises the accent line to meet the dashed one and shows an end dot. About 3 seconds, starts when the chart is half visible, plays once per browser session (`sessionStorage` key `heroGapPlayed`). Without JavaScript, with reduced motion, or on a repeat view it shows the final frame (lines joined).
3. **Work (`#work .case-files`)** — a compact index, not full write-ups. `h2` "Work", then three `section.work-group`s, each with a small muted `h3` and hairline-separated `article.work-row`s (`4fr / 7fr`: evidence left, text right; stacked under 760px):
   - **Products I've built** (`tag == 'Built'`): left is the screenshot in `.case-window` (16:10, `object-position: top`, links to the live demo); right is the title (`h4`), deck, one meta line (role · year · stack), "Live demo ↗", any `more_links`, "Read case study", optional note.
   - **PRDs, teardowns and concepts** (every other tag): left is the key metric (`cover_metric`, serif) with its label, or empty; right is the title, deck, meta line (`figure_label` · role · year), the `doc_link` (labelled `doc_label`, or a TODO if missing), any `more_links`, and "Read case study" unless `case_page` is False.
   - **Now building**: one row; left is the tag (e.g. 0→1), right is the title, its narrative and a meta line.
   - Narrative paragraphs and pull quotes are not shown on the homepage; they live on the case study pages.
4. **About + Contact (`.about-contact`)** — hairline on top; `h2` About, paragraphs, one interests line; `h2` Contact with a row of text links; footer note.

### Thoughts (`templates/thoughts.html`)

- Same header with `Thoughts` marked `aria-current="page"`.
- `h1` page title. Groups (Featured / Classism Series / Posts) are small muted `h2`s.
- Each post is a full-row link: serif title, summary, date and reading time on the right (stacked under the title below 640px). Hairlines between rows. "Latest" sits above the newest post's title in the accent.

### Case study (`templates/case.html`)

- Same header. Back link, tag, `h1` title, deck, meta rows.
- Sections with serif `h2`s; facts as `dl` rows (label column 140px, stacked below 640px); TODOs as muted notes; previous / next links above a hairline.

## 4) Data Shapes

### Work project object (`case_files.py`)

```python
{
  'title': str,
  'slug': str,
  'tag': 'Built' | 'PRD',
  'deck': str,
  'role': str,
  'stack': str,            # optional
  'year': str,
  'link': str,             # optional; live demo
  'liveUrl': str,          # optional
  'liveDomain': str,       # optional; shown in the fallback cover
  'link_note': str,        # optional
  'preview_image': str,    # e.g. '/previews/spotify-taste-bridge.png' (1440×900)
  'cover_metric': str,     # PRDs without a screenshot
  'cover_label': str,
  'figure_label': str,     # type shown in the row's meta line, e.g. 'PRD & teardown'
  'doc_link': str,         # optional; the PRD/teardown/deck PDF in public/
  'doc_label': str,        # optional; link text for doc_link (default 'Read the PRD')
  'more_links': list[dict],  # optional; [{'label': 'Deck', 'href': '/x.pdf'}]
  'case_page': bool,       # optional; False = the PDF is the write-up, no /work/<slug> page
  'narrative': list[str],
  'pullQuote': str
}
```

Every item with a case page needs a branch in `case_sections()`; `/work/<slug>` returns 404 for `case_page: False` items, and the previous/next links skip them. To capture a new screenshot: `python scripts/capture_previews.py <slug>`.

If a `preview_image` fails to load, the `<img>` removes itself and `.case-cover--fallback` (title + live domain) fills the frame.

### Thoughts post (`app.py`)

```python
{
  'title': str,
  'url': str,
  'summary': str,
  'date': str,          # e.g. "Mar 2026"
  'reading_time': int | None,
  'tags': list[str],    # not shown in the UI
  'series': str | None
}
```

RSS: `https://asthapurohit.substack.com/feed`. Cache TTL 15 minutes. On failure: stale cache if present, else the feed-error message with a Substack link. Only `/thoughts` fetches the feed.

## 5) Responsive Behavior

- `<=900px`: the hero chart stacks under the intro.
- `<=760px`: work rows stack (screenshot or metric above the text).
- `<=640px`: 20px container padding; tighter header, hero and section spacing; Thoughts rows stack date and reading time under the title; case-study facts stack.

## 6) Known issues

1. **Research engine link:** the Blinkit row links the complete research site, `web-three-ashy-40.vercel.app`. The rebuild at `discovery-engine-psi.vercel.app` still shows placeholder data; switch the link once it's populated.
2. **First SIP is a concept:** its deck's research and testing figures are illustrative. Don't quote them on the site as results.

## 7) Condensed File Tree

```text
portfolio/
├─ app.py
├─ case_files.py
├─ requirements.txt
├─ vercel.json
├─ scripts/
│  └─ capture_previews.py
├─ templates/
│  ├─ index.html
│  ├─ thoughts.html
│  └─ case.html
└─ public/
   ├─ style.css
   ├─ previews/
   │  ├─ pehli-baar.png
   │  ├─ spotify-taste-bridge.png
   │  ├─ groww-weekly-pulse.png
   │  └─ hdfc-mf-faq.png
   ├─ AsthaPurohit_Resume.pdf
   ├─ spotify-taste-bridge-deck.pdf
   ├─ chatGPT_PRD.pdf
   ├─ Goodreads-PRD.pdf
   ├─ Goodreads-ProductTeardown.pdf
   ├─ Mastercard-Checkout-Teardown.pdf
   ├─ Passkeys-Card-Checkout-PRD.pdf
   └─ First-SIP-UX-Case-Study.pdf
```
