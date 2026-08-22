# Portfolio UI / Design Context

## 1) Tech Stack

- **App framework:** Flask (Python) server-rendered templates (`app.py` + Jinja in `templates/`).
- **Frontend architecture:** Plain HTML templates + one global stylesheet (`public/style.css`) + inline vanilla JS per template.
- **Styling system:** Custom CSS (no Tailwind, no CSS modules, no styled-components, no UI component library).
- **Visual metaphor:** macOS desktop — menu bar header, window chrome around Work previews and the Thoughts list, Finder-style rows, Dock for contact.
- **Animation system:**
  - Vanilla CSS transitions.
  - `IntersectionObserver` in `templates/index.html` and `templates/thoughts.html` for reveal effects.
  - JS-driven scroll progress rail in the Work section.
- **Fonts and loading:**
  - Loaded from Google Fonts via `<link>`: `DM Serif Display`, `DM Mono`, `Lato`.
  - UI chrome uses the system stack via `--font-ui` (does not require a webfont).
- **UI libraries:** None.
- **Deployment target:** Vercel (Python function) via `vercel.json` with `app.py` max duration 30s.

## 2) Design Tokens

Two layers live in `public/style.css`.

### macOS token layer (new)

Defined in `:root` as dark defaults, then restated in both `prefers-color-scheme: light` and `prefers-color-scheme: dark`. Dark is the fallback if a scheme query does not match.

**Type**

- `--font-ui: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", system-ui, sans-serif` — menu bar, window titles, Finder rows, Dock labels.
- `--font-display: "DM Serif Display", serif` — hero name, case titles in the narrative column, pull quotes.
- `--font-mono: "DM Mono", monospace` — chapter numbers, FIG captions, metadata.

**Surfaces (layered greys, not flat white)**

| Token | Light | Dark |
|---|---|---|
| `--surface-page` | `#E5E5EA` | `#1C1C1E` |
| `--surface-window` | `#F5F5F7` | `#2C2C2E` |
| `--surface-titlebar` | `#EBEBED` | `#3A3A3C` |

**Chrome**

- `--radius-window: 12px`
- `--radius-control: 6px`
- `--hairline: 0.5px solid` at 12% alpha (black in light, white in dark)
- `--shadow-window`: large soft ambient + tight contact shadow, low opacity
- `--accent`: system blue `#007AFF` (light) / `#0A84FF` (dark)
- `--blur: saturate(180%) blur(20px)` — menu bar and Dock `backdrop-filter`

**Focus:** `:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }`. Do not suppress outlines.

`@supports not (backdrop-filter: blur(1px))` falls back to solid `--surface-titlebar` on the menu bar and Dock.

### Legacy color tokens (still used by page body / editorial)

The rest of the page (hero, narrative columns, textures) still uses the original dark tokens in `:root`: `--color-bg`, `--color-text-*`, `--color-accent-primary` (orange), etc. Chrome and page body are not fully unified yet — window/menu/dock/finder use the macOS layer; editorial copy still sits on `--color-bg`.

### Typography roles

- **Display serif (`--font-display` / DM Serif Display):** hero name, case-file `<h3>` titles, pull quotes.
- **System UI (`--font-ui`):** header, window titlebars, Finder, Dock.
- **Mono (`--font-mono`):** Work chapter index in the titlebar, FIG captions, some meta.
- **Body (Lato):** hero paragraph, About, case narrative.

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

### Page structure (home)

1. **Header (`.site-header`)** — sticky macOS menu bar, `height: 38px`, `z-index: 50`. Translucent titlebar + `--blur` + hairline. **AP** is the left mark; nav items get `--accent` hover pills.
2. **Hero (`.hero`)** — name in DM Serif Display, static pull quote (no slider).
3. **Work (`#work .case-files`)** — scrollytelling chapters, desktop rail, two-column grid (`40%/60%`, reversed on even chapters).
4. **About + Contact (`.about-contact`)** — stacked: About column, then a centered Dock, then the footer note.

### Thoughts page structure

- Shared menu bar header.
- One macOS window (`.case-window.thoughts-window`) containing a Finder list (column headers + rows).
- Substack link below the window.

## 4) Window metaphor

Window chrome is presentational. Semantic structure stays `<article>` / `<h1>` / `<h2>` — do not replace real headings with decorative titlebar text as the only name.

Shared classes (Work preview + Thoughts list):

- `.case-window` — `--surface-window`, `--hairline`, `--radius-window`, `--shadow-window`.
- `.case-window__titlebar` — `--surface-titlebar`, hairline bottom.
- Left cluster: `--font-mono` index + traffic-light dots (`#FF5F57` / `#FEBC2E` / `#28C840`). Dots are `aria-hidden="true"`.
- Centered name in `--font-ui` at 13px (Work titlebar name is also `aria-hidden`; the real `<h3>` lives in the narrative panel. Thoughts uses a real `<h1>` as `.case-window__name`).

### Work chapter window

- Preview `img` (`preview_image` from `case_files.py`) sits edge-to-edge under the titlebar.
- Image: `width="1440"` `height="900"` `loading="lazy"` `decoding="async"`.
- **Visit Live ↗** hover pill on the screenshot; FIG caption stays outside the window.
- Pull quote stays editorial (DM Serif Display, no chrome).

### Thoughts Finder window

- Column header: Title / Date / Reading time (`--font-ui`, hairline).
- Rows: zebra tint, hairline separators, `--accent` selection tint on hover.
- Summary expands on hover; no sibling-dimming.
- Tags are small rounded pills.

### Contact Dock

- `.dock__bar`: centered, translucent, `--blur`, `--radius-window`, hairline.
- Items: LinkedIn, GitHub, Email, Substack, Resume — each with a visible text label and a decorative dot.
- Icon magnification is `transform: scale()` only; disabled under `prefers-reduced-motion: reduce`.

## 5) Component Inventory

- **`templates/index.html`** — home: menu bar, hero, Work windows, About, Dock.
- **`templates/thoughts.html`** — Finder list in a window; staggered row reveal.
- **`case_files.py`** — Work chapter data (`preview_image`, `liveUrl`, narrative, etc.).
- **`app.py`** — Flask routes. `/thoughts` fetches Substack RSS with a 15-minute module cache, 5s socket timeout, stale-cache-then-placeholder fallback.
- **`public/style.css`** — tokens + all layout/interaction styles.

### Work chapter

- Markup: `<article class="case-chapter">` with sticky `<aside>` and `.case-chapter__content`.
- Alternation: `case-chapter--reverse` on even chapters.
- Chapter numbers (`01`, `02`, `03`) come from `loop.index`, not hardcoded values.
- FIG caption hostname is derived from `project.liveUrl` (strip protocol and trailing slash).

### Scroll progress rail

- Shown only at `min-width: 1025px`.
- Fill height from Work section scroll percentage.
- Dot buttons smooth-scroll to chapter IDs.

## 6) Data Shapes

### Work project object (`case_files.py`)

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
  'preview_image': str,   # e.g. '/case-fallback-spotify.svg'
  'narrative': list[str],
  'pullQuote': str
}
```

There is no live iframe embed. `preview_image` currently points at the `case-fallback-*.svg` placeholders until real screenshots are swapped in.

### Thoughts post (`app.py`)

```python
{
  'title': str,
  'url': str,
  'summary': str,
  'date': str,          # e.g. "Mar 2026"
  'reading_time': int,
  'tags': list[str],    # max 2
  'series': str | None
}
```

RSS: `https://asthapurohit.substack.com/feed`. Cache TTL 15 minutes. On failure: stale cache if present, else `PLACEHOLDER_POSTS`.

## 7) Interaction & Motion Map

- **Global section reveals:** `.fade-up` + IntersectionObserver on home.
- **Hero quote:** static; no rotation.
- **Menu bar nav:** `--accent` rounded hover / focus-visible fill.
- **Work rail dots:** active state + click scroll.
- **Case blocks:** reveal stagger (`90ms` step, `0.45s` motion).
- **Case window:** hover “Visit Live ↗” pill on the preview.
- **Thoughts rows:** deck expansion on hover; `--accent` row tint; stagger reveal (`80ms`).
- **Dock:** icon scale `1.32` on hover/focus-visible; off under reduced motion.
- **Focus:** global `--accent` focus ring on `:focus-visible`.
- **Reduced motion:** transform-heavy reveals / dock scale disabled or simplified.

## 8) Responsive Behavior

### `<=1024px` (Work)

- Sticky panel becomes static; chapter grid is one column.
- Reverse order cancelled.
- Rail hidden (rail only at `>=1025px`).

### `<=768px`

- Menu bar stays 38px; nav slightly tighter.
- Hero type scales down.
- About / Dock stack with tighter gap.
- Work vertical padding tightened.

### `<=640px` (Thoughts)

- Finder extra columns hide; date + reading time sit under the title.
- Deck is always visible (no hover-gated summary).

## 9) Known issues

1. **Broken self-referential tokens** (used by live UI, values do not resolve):
   - `--color-divider: var(--color-divider)` — used by `.case-chapter__divider`
   - `--color-border-frame: var(--color-border-frame)` — used by `.case-files__rail-track`
2. **Unused token groups still in `:root`** (no matching template selectors): `--color-badge-*`, `--color-thoughts-*`, `--color-live-*`, `--color-metric-*`, `--shadow-card*`, `--gradient-brand`, `--shadow-logo-hover`. Left in place rather than guessed-deleted.
3. **Unlinked public assets:** `case-fallback-unstick.svg`; PRD/deck PDFs other than `AsthaPurohit_Resume.pdf` are not referenced from templates.
4. **Page body vs chrome:** editorial surfaces still use the old dark `--color-bg` tokens; only chrome uses the macOS surface layer.

## 10) Condensed File Tree

```text
portfolio/
├─ app.py
├─ case_files.py
├─ requirements.txt
├─ vercel.json
├─ templates/
│  ├─ index.html
│  └─ thoughts.html
└─ public/
   ├─ style.css
   ├─ case-fallback-spotify.svg
   ├─ case-fallback-groww.svg
   ├─ case-fallback-hdfc.svg
   ├─ case-fallback-unstick.svg   # unused
   ├─ AsthaPurohit_Resume.pdf
   ├─ spotify-taste-bridge-deck.pdf
   ├─ chatGPT_PRD.pdf
   ├─ Goodreads-PRD.pdf
   └─ Goodreads-ProductTeardown.pdf
```
