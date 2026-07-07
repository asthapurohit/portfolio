# Portfolio UI / Design Context

## 1) Tech Stack

- **App framework:** Flask (Python) server-rendered templates (`app.py` + Jinja in `templates/`).
- **Frontend architecture:** Plain HTML templates + one global stylesheet (`public/style.css`) + inline vanilla JS per template.
- **Styling system:** Custom CSS (no Tailwind, no CSS modules, no styled-components, no UI component library).
- **Animation system:**
  - Vanilla CSS transitions.
  - `IntersectionObserver` in `templates/index.html` and `templates/thoughts.html` for reveal effects.
  - JS-driven scroll progress + embed lifecycle in Work section.
- **Fonts and loading:**
  - Loaded from Google Fonts via `<link>`:
    - `DM Serif Display`
    - `DM Mono`
    - `Lato`
- **UI libraries:** None.
- **Deployment target:** Vercel (Python function) via `vercel.json` with `app.py` max duration 30s.

## 2) Design Tokens

All tokens are defined in `public/style.css` `:root`.

### Core color tokens (exact values)

- **Background/surfaces**
  - `--color-bg: #0F1117`
  - `--color-surface-header: #0d0d0f`
  - `--color-bg-elevated: #1A1F2E`
  - `--color-bg-card-end: #161B26`
  - `--color-bg-hover: #1F2533`
  - `--color-bg-hover-alt: #252D3D`
- **Text tiers**
  - `--color-text: #E5E7EB`
  - `--color-text-body: rgba(255, 255, 255, 0.78)`
  - `--color-text-heading: #FFFFFF`
  - `--color-text-strong: #FFFFFF`
  - `--color-text-muted: #9CA3AF`
  - `--color-text-subtle: #6B7280`
  - `--color-text-faint: #4B5563`
  - `--color-text-process: #D1D5DB`
- **Accent palette**
  - `--color-accent-primary: #EA580C`
  - `--color-accent-primary-hover: #F97316`
  - `--color-accent-primary-border: #C2410C`
  - `--color-accent-primary-light: color-mix(in srgb, var(--color-accent-primary) 8%, var(--color-bg))`
  - `--color-accent-secondary: #0EA5E9`
  - `--color-accent-secondary-hover: #38BDF8`
  - `--color-accent-secondary-dark: #7DD3FC`
  - `--color-accent-secondary-light: color-mix(in srgb, var(--color-accent-secondary) 12%, var(--color-bg))`
  - `--color-accent-secondary-border: color-mix(in srgb, var(--color-accent-secondary) 28%, var(--color-bg))`
  - `--color-accent-pink: #EC4899`
  - `--gradient-brand: linear-gradient(135deg, #F97316, #EC4899)`
- **Borders**
  - `--color-border: #2D3748`
  - `--color-border-subtle: #252D3D`
  - `--color-border-muted: #374151`
  - `--color-border-hover: #4B5563`
  - `--color-border-insight: #374151`
  - `--color-border-insight-hover: #4B5563`
- **Special badges/chips**
  - Live: `#142819 / #4ADE80 / #22543D`
  - Progress/PRD/Teardown badge tokens are all present (see CSS root).
- **Hardcoded literals outside root**
  - `#141416` used directly in embed placeholder/fallback panel backgrounds.
  - `rgba(255,255,255,0.08)` used for section/header/chapter divider lines.
  - `rgba(255,255,255,0.1)` used for frame borders/rails.

### Color consistency notes

- Orange family uses multiple explicit values (`#EA580C`, `#F97316`, `#C2410C`, `#FB923C`, `#FDBA74`) intentionally as hierarchy.
- Some older token groups still exist for legacy Thoughts/card styles; not all are actively rendered after redesign.

### Typography system

- **Display serif:** `DM Serif Display`
  - Hero name, chapter titles, chapter serial watermark, pull quotes, major headings.
- **Monospace UI/meta:** `DM Mono`
  - Labels, counters, nav links, metadata rows, badges, captions, pills.
- **Body copy:** `Lato`
  - Paragraphs, narratives, descriptions.

### Font sizes in use (unique values found)

`8px`, `9px`, `10px`, `11px`, `12px`, `13px`, `14px`, `15px`, `17px`, `18px`, `20px`, `24px`, `26px`, `42px`, `48px`, `52px`, `68px`, `120px`, plus clamps:

- `clamp(1.25rem, 2.5vw, 1.65rem)` (pull quotes)
- `clamp(1.25rem, 2.8vw, 1.75rem)` (fallback title)
- `clamp(1.35rem, 5vw, 1.85rem)` (chapter title mobile)
- `clamp(1.35rem, 6vw, 1.75rem)` (thoughts row mobile)
- `clamp(1.5rem, 3vw, 2.25rem)` (chapter title desktop)
- `clamp(1.5rem, 6.5vw, 2rem)` (featured thoughts title mobile)
- `clamp(1.75rem, 4vw, 3rem)` (thoughts title row)
- `clamp(2rem, 4.5vw, 3.5rem)` (featured thoughts row title)
- `clamp(2.5rem, 12vw, 4rem)` (chapter serial mobile)
- `clamp(4rem, 8vw, 7rem)` (chapter serial desktop)

### Spacing patterns (representative)

- Section paddings: `62px`, `67px`, `72px`, `77px`, `86px`.
- Major chapter rhythm: `gap 32px`, chapter divider margin `120px`.
- Container: `--container-max: 1200px`, `--container-padding: 24px`.
- Common micro spacing: `4px`, `6px`, `8px`, `10px`, `12px`, `14px`, `16px`.

### Radius, z-index, transitions, breakpoints

- **Radii:** `1px`, `8px`, `10px`, `12px`, `14px`, `20px`, `50%`.
- **z-index values:** `-2, -1, 0, 1, 2, 4, 5, 10, 50`.
- **Transition durations/easing:**
  - `0.15s ease-out` (rail fill)
  - `0.2s`/`0.25s` for hover state changes
  - `0.3s cubic-bezier(0.22, 1, 0.36, 1)` for logo transform
  - `0.4s`, `0.45s`, `0.5s`, `0.6s` for reveal motion
- **Breakpoints:**
  - `@media (max-width: 640px)`
  - `@media (max-width: 768px)`
  - `@media (max-width: 1024px)`
  - `@media (min-width: 1025px)`
  - `@media (prefers-reduced-motion: reduce)`

## 3) Layout Architecture

### Shared container

```css
.container {
  width: 100%;
  max-width: var(--container-max); /* 1200px */
  margin: 0 auto;
  padding: 0 var(--container-padding); /* 24px */
}
```

Used by header, hero, work section, about/contact, and thoughts page content.

### Page structure (home)

1. **Header (`.site-header`)**
   - Sticky, full-width, `height: 72px`, `z-index: 50`.
   - Inner container is flex row (logo + nav).
2. **Hero (`.hero`)**
   - Single-column content, quote slider + dots.
3. **Work (`#work .case-files`)**
   - Scrollytelling chapter stack with optional desktop rail.
   - Each chapter uses two-column grid (`40%/60%`, alternates to `60%/40%`).
   - Sticky left panel at `top: 96px`.
4. **About + Contact (`.about-contact`)**
   - Two-column grid on desktop, stacks on mobile.
5. **Footer note** inside Contact column.

### Thoughts page structure

- Header (same shared header).
- `thoughts-page-wrap` + container.
- Editorial index list with sticky-like rhythm but no pinned panels.

## 4) Component Inventory

> This codebase is template-driven; there are no React/Vue component files. “Components” below refer to template/CSS/JS modules.

- **`templates/index.html`**
  - Home page scaffold; renders hero, Work case-file chapters, about/contact.
  - Reads `case_files` from Flask context.
- **`templates/thoughts.html`**
  - Thoughts editorial index; loops over `posts` and applies staggered reveal.
- **`case_files.py`**
  - Work chapter data source.
- **`app.py`**
  - Flask routing and data shaping for home/thoughts.
- **`public/style.css`**
  - Global design tokens + all layout/interaction styles.

### Complex logic details

#### A) Case-file chapter

- Markup: `<article class="case-chapter">` with sticky `<aside>` panel and scrolling `.case-chapter__content`.
- Alternation: `case-chapter--reverse` on even chapters.
- Divider: separate `<div class="case-chapter__divider">`.

#### B) Live iframe embed lifecycle (current)

- Data attributes per chapter embed:
  - `data-live-url`, `data-embed`, `data-fallback-image`, `data-has-fallback-image`, `data-domain`, `data-project-title`.
- Scaling:
  - Fixed stage size `1440x900`.
  - `ResizeObserver` computes scale `frameWidth / 1440`.
  - Scaled stage placed in 16:10 viewport.
- Mounting:
  - `updateEmbeds()` runs on scroll/resize.
  - Desktop-only (`window.innerWidth >= 1024`).
  - Chooses nearest 2 in-range embed cards to mount.
- Load/fallback:
  - `load` listener attached before `src`.
  - Timeout `6000ms`; if no load, unmount + fallback.
  - Retry counter (`maxRetries = 2`) before permanent block.
- Unmount:
  - Only when out of view by >50% and mounted >3s.
- Security:
  - `sandbox="allow-scripts allow-same-origin"`, `referrerPolicy="no-referrer"`, `loading="lazy"`.

Key snippet:

```js
iframe.addEventListener('load', () => {
  clearTimeout(timeoutId);
  retryCount = 0;
  blocked = false;
  showLive();
}, { once: true });
iframe.src = card.dataset.liveUrl;
timeoutId = window.setTimeout(() => {
  if (!loaded) { unmount(); showFallback(); }
}, 6000);
```

#### C) Scroll progress rail

- Rail shown only at `min-width: 1025px`.
- Fill height computed from Work section scroll percentage.
- Dot buttons smooth-scroll to chapter IDs.

#### D) Thoughts editorial rows

- Each row has index/title/deck/meta/tags/arrow.
- Hover behavior: title shifts+orange italic; deck expands; siblings dim via parent hover selectors.
- `IntersectionObserver` in `thoughts.html` with `80ms` row stagger via CSS custom property.

## 5) Data Shapes

### Work project object shape (`case_files.py`)

```python
{
  'title': str,
  'deck': str,
  'role': str,
  'stack': str,
  'year': str,
  'link': str,
  'liveUrl': str,
  'liveDomain': str,
  'embed': bool,
  'fallbackImage': str,
  'narrative': list[str],
  'pullQuote': str
}
```

Real example:

```python
{
  'title': 'Groww Weekly Review Pulse',
  'deck': 'AI dashboard that turns 1,499 real app reviews into a weekly brief any PM can act on in under 30 seconds.',
  'role': 'Solo Builder',
  'stack': 'React, Groq, Gemini, Vercel',
  'year': '2025',
  'link': 'https://groww-weekly-pulse.vercel.app/',
  'liveUrl': 'https://groww-weekly-pulse.vercel.app/',
  'liveDomain': 'groww-weekly-pulse.vercel.app',
  'embed': True,
  'fallbackImage': '/case-fallback-groww.svg',
  'narrative': [...],
  'pullQuote': 'Real reviews are messy. Keyword matching alone fails — the hardest part wasn’t the AI, it was the data pipeline.',
}
```

Embed status currently:

- `embed: true` → Spotify, Groww
- `embed: false` → HDFC MF FAQ

### Thoughts post shape (`app.py`)

```python
{
  'title': str,
  'url': str,
  'summary': str,
  'date': str,          # e.g. "Mar 2026"
  'reading_time': int,  # minutes
  'tags': list[str],    # max 2
  'series': str | None  # "classism" | None
}
```

Real placeholder example:

```python
{
  'title': 'Why stated preferences lie — and what to measure instead',
  'url': 'https://substack.com/@asthadiaries',
  'summary': 'Surveys capture what people think they want. Product decisions need what they actually do under friction, social pressure, and incomplete information.',
  'date': 'Mar 2026',
  'reading_time': 7,
  'tags': ['Behavioral Design'],
  'series': None,
}
```

## 6) Interaction & Motion Map

- **Global section reveals:** `.fade-up` + IntersectionObserver in `index.html`.
- **Hero quote slider:** auto-advances every `4000ms`, clickable dots.
- **Header logo:** scale + glow hover.
- **Nav resume button:** border/background/color hover.
- **Work rail dots:** active state + click scroll.
- **Case blocks:** reveal stagger (`90ms` step, `0.45s` motion).
- **Case embeds:**
  - iframe stage scales to fit frame
  - hover scale `1.02`
  - hover “VISIT LIVE ↗” pill
  - fallback/live indicator dot in caption
- **Thoughts rows:**
  - title translation + color/style change on hover
  - deck expansion on hover
  - sibling dimming while one row hovered
  - stagger reveal (`80ms` step)
- **Reduced motion:** transform-heavy animations disabled or simplified in relevant media query blocks.

## 7) Responsive Behavior

### `<=1024px` (Work chapters)

- Sticky disabled (`position: static` panel).
- Chapter grid collapses to single column.
- Serial/title scale down.
- Embed stage hidden; fallback image shown.
- Rail hidden (rail only appears at `>=1025px`).

### `<=768px` (global)

- Header becomes multi-line/wrapped.
- Nav/link font sizes reduce.
- About/contact grid stacks.
- Hero text scales down.
- Work section vertical padding tightened.

### `<=640px` (Thoughts rows)

- Row layout becomes two-row grid areas (`index/meta` then `main`).
- Title scales down.
- Hover transforms effectively disabled for touch behavior.
- Deck shown (not collapsed by hover).

## 8) Known Issues / TODO

1. **Legacy/unused CSS remains** in `public/style.css`:
   - Old card/tab/thought-list selectors (`.card-*`, `.thought-*`, `.badge-*`, etc.) that are not used by current templates.
2. **Duplicated style intent**:
   - Multiple historical rule blocks for hero/thoughts/quote styles coexist; cascade correctness depends on ordering.
3. **Embed reliability still heuristic-based**:
   - Timeout/retry lifecycle exists but true CSP/X-Frame-Options blocking cannot be deterministically detected client-side.
4. **Work embed configuration intentionally mixed**:
   - HDFC is `embed: false`; expected fallback.
5. **Repository contains legacy `static/style.css`** not used by current deployed pages (`/style.css` from `public/` is used).

## 9) Condensed File Tree

```text
portfolio/
├─ app.py
├─ case_files.py
├─ requirements.txt
├─ vercel.json
├─ templates/
│  ├─ index.html
│  └─ thoughts.html
├─ public/
│  ├─ style.css
│  ├─ case-fallback-spotify.svg
│  ├─ case-fallback-groww.svg
│  ├─ case-fallback-hdfc.svg
│  ├─ AsthaPurohit_Resume.pdf
│  ├─ spotify-taste-bridge-deck.pdf
│  ├─ chatGPT_PRD.pdf
│  ├─ Goodreads-PRD.pdf
│  ├─ Goodreads-ProductTeardown.pdf
│  └─ NL Spotify.pdf
└─ static/              # legacy assets from pre-public setup
   ├─ style.css
   └─ PDFs...
```

---

If you hand this file to another assistant, the most important caveat is: the project is **Flask + Jinja + single global CSS**, with significant historical CSS still present; recommendations should account for cascade cleanup, not just adding new rules.
