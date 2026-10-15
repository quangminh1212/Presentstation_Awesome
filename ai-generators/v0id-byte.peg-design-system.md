# Peg Design System — Minimal Slide & Presentation Framework

> A type-led, data-first design system for slide decks, web presentations, and React UI components. Built on restraint: one background, one accent, no shadows.

**[English](#english) · [中文](#中文)**

---

## Preview

| Title slide | Types comparison |
|---|---|
| ![Title slide](docs/screenshots/01-title.png) | ![Types comparison](docs/screenshots/02-types.png) |

| Data comparison table | Mechanism slide |
|---|---|
| ![Data comparison table](docs/screenshots/03-comparison.png) | ![Mechanism slide](docs/screenshots/04-mechanism.png) |

![Depeg chart — pure SVG + CSS, no chart library](docs/screenshots/05-depeg-chart.png)

---

## English

### What is Peg?

**Peg** is an open-source design system and slide framework extracted from a production presentation deck. It gives you a complete, opinionated visual language for building beautiful, readable presentations in HTML/CSS and React — without touching a design tool. Ships with a Claude Skill (`SKILL.md`) for direct import into **Claude Design**.

Key characteristics:
- **Minimal palette** — 6 tokens, one warm-white background, one jade accent
- **Type-led hierarchy** — Inter variable font, aggressively negative tracking, no decorative elements
- **Data-first** — tabular numerals, SVG 2px chart lines, count-up animations built in
- **Flat & fast** — no shadows, no gradients, no card chrome; content lives directly on paper
- **Accessible by default** — all animations respect `prefers-reduced-motion`; DOM always shows final state

---

### Use Cases

| Scenario | What to use |
|---|---|
| Build a slide deck in HTML | `slides/` templates + `slides/slide-base.css` |
| Prototype a data-heavy UI | `components/core/` React components |
| Adopt the design tokens only | `tokens/*.css` |
| Browse the design language | `guidelines/*.card.html` |

---

### Eight Slide Templates

| Template | Purpose |
|---|---|
| **Title** | Deck opener — wordmark + $1.00 peg line |
| **Headline** | One bold claim + supporting sentence |
| **Stats** | Two key figures with short descriptors |
| **Flow** | Left-to-right value or process chain |
| **Chips** | Labelled category grid with context |
| **Attr List** | Define something with 3–4 bold-term properties |
| **Moment** | Centred full-frame question or provocation |
| **Media / Proof** | Show real renders, CAD, PCB, photos, screenshots — full-bleed, split (text + figure), or a 2–4 figure proof wall |

#### Media / Proof slides

Three image layouts, all on-language (hairline frames, no shadows, captions in caption type):

- `<section class="media-full">` — the image **is** the slide (Night letterbox). Children: `<img class="media-img contain">` (use `contain` to show a whole part, drop it to fill/crop), optional `.media-scrim`, `.media-label`, `.media-title`, `.media-cap`.
- `<section class="paper media-split">` — text on the left (`.media-text`), one framed `<figure class="media-figure">` on the right.
- `<section class="paper media-wall">` — a `.wall` of 2–4 `<figure class="cell">`, each with a `.fig` and a `<figcaption>`.

Every image slide should carry an evidence tag (`.evi` → RENDER / CAD / PCB / PROTOTYPE / APP) and a one-line caption, so the audience knows what they're looking at and that it's real.

`media-wall`'s row height and headline size are both pinned by CSS for real photography, not just curated screenshots: the wall's single grid row is forced to `1fr` (real product photos with mixed aspect ratios could otherwise inflate the row past the wall's own box and clip captions), and `.media-wall .headline` is stepped down to 56px so a two-line title never runs into the wall below it. Don't override these back to `auto` / the default 92px unless every image and headline on that slide has been checked at full length.

---

### Five Core React Components

| Component | Purpose |
|---|---|
| `PegLine` | The signature $1.00 horizontal baseline |
| `FlowBand` | Arrow-chained flow diagram |
| `Chip` | Bordered pill for key/value metadata |
| `StatBlock` | Large formatted number + descriptor |
| `AttrList` | Stacked property definition rows |

---

### Design Tokens

```
tokens/
  colors.css      — 6 palette values + semantic aliases
  typography.css  — 7 type roles, tracking, weight
  spacing.css     — spacing scale + 1920×1080 canvas geometry
  effects.css     — line weights, radii, motion curves
  fonts.css       — Inter variable @font-face
```

---

### Colour Palette

| Token | Value | Role |
|---|---|---|
| `--color-paper` | `#FAFAF8` | Only background — warm, never cold |
| `--color-ink` | `#16181D` | Primary text and lines |
| `--color-night` | `#0B0B0C` | Stage chrome, outer letterbox |
| `--color-jade` | `#00A878` | Default accent — one use per slide |
| `--color-alert` | `#E5484D` | Danger only — losses, risk, collapse |
| `--color-mute` | `#8A8A8E` | Labels, footnotes, secondary text |

**Topic accents (muted, meaning-bearing).** For a multi-section deck, give each section its own *calm* hue instead of jade everywhere — set `--accent: var(--topic-…)` on the `<section>` and every accent utility (`.jade` text, `.evi` tag, diagram strokes `.s-jade`/`.box-j`/`.t-j`/`.f-jade`) follows it automatically. Keep them muted (Apple-keynote, never neon) and consistent per module (eyebrow = keyword = diagram = same hue).

| Token | Value | Meaning |
|---|---|---|
| `--topic-control` | `#128A6B` | teal — real-time control / signal |
| `--topic-silicon` | `#3A6AA0` | blue — electronics / PCB |
| `--topic-material` | `#8C6B38` | bronze — material / industrial design |
| `--topic-safety` | `#AC5A3C` | clay — safety-critical (not alarm-red) |
| `--topic-algo` | `#6A57A0` | violet — algorithm / intelligence |
| `--topic-growth` | `#4F8A52` | sage — data / growth |

**Layout patterns.** `.headline.with-fig` steps the headline down a size when it shares the slide with a diagram; `.media-split .media-text .headline` does the same for a narrow text column; `.summary` is a centered one-line takeaway placed *below* a diagram so the eye reads the diagram then drops to the conclusion; **`.plain`** is a one-sentence *plain-language explainer* (accent left-rule) placed under the headline for a non-expert audience — the slide keeps its technical content, this line just makes it land for everyone (bold the one phrase that matters; on a headline+figure slide cap its `max-width` to the text column; mind 2-line headlines when setting `top`). See template 11 in `slides/`. **`.compare`** is a before→after / problem→solution table (rows of *old limitation* → *what we now do*) — the clearest way to show **iteration** at a glance; `.badge-first` flags genuinely first-of-kind rows (use sparingly, back the claim). See template 12.

---

### Typography Scale

| Role | Size | Tracking | Weight |
|---|---|---|---|
| Wordmark | 248px | −0.04em | 700 |
| Hero | 300px | −0.04em | 700 |
| Headline | 92px | −0.03em | 600 |
| Subhead | 60px | −0.02em | 600 |
| Support | 44px | −0.01em | 400 |
| Caption | 28px | 0 | 400 |

---

### Quick Start

```html
<!-- Link the token chain -->
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="slides/slide-base.css">

<!-- Use a slide template -->
<div class="slide slide--headline">
  <div class="frame">
    <p class="label">SECTION LABEL</p>
    <h1 class="headline">A bold one-line claim.</h1>
    <p class="support">Supporting sentence that adds context.</p>
  </div>
</div>
```

---

### File Structure

```
styles.css              Entry point (@import chain)
tokens/                 CSS custom properties
components/core/        React components (.jsx + .d.ts + .prompt.md)
slides/                 7 HTML slide templates + base CSS
guidelines/             Visual documentation cards
assets/                 Inter variable font
```

---

### Design Principles

1. **One background.** Paper (`#FAFAF8`) only. No dark slides, no gradients.
2. **One accent.** Jade once per slide, maximum. Never decorative.
3. **Alert is earned.** `#E5484D` for genuine bad news only.
4. **No shadows.** No elevation. Content lands on paper.
5. **Final state first.** Screenshots and PDFs always show complete slides.
6. **Tabular numerals everywhere.** No column-width jitter.
7. **Negative tracking on display text.** Tight, not loose.

---

### Motion & Animation

Peg includes a built-in animation engine (`peg-animate.js`) for Keynote-like entrance effects and slide transitions.

#### How it is put together

The engine is not a set of CSS animations with Keynote-ish names. Keynote is closer to a small motion-graphics renderer, and reproducing it needed two things CSS keyframes alone do not give you: **segmented time** (builds overshoot and settle, each segment on its own curve) and **material layers** (masks, specular sweeps — not just geometry).

```
Apple bundle (*.parameterGroup / deck protobuf)
        ↓   tools/keynote-params.py · tools/keynote-effects.py
   effect fact database
        ↓
   effect descriptor
        ↓
     Motion IR            ← peg-animate.d.ts defines the contract
        ↓
 ┌──────┴──────┐
 Geometry   Material      ← Geometry owns `transform`. Material owns
 compositor compositor       everything else and may NEVER write transform.
 └──────┬──────┘
      WAAPI
```

Two properties are worth knowing because they are what keep this maintainable:

- **The compositors never see an effect name.** They handle `Target → Track → property`. Adding an effect means adding a descriptor that emits tracks — not touching a renderer. If you find yourself writing `if (effect === '…')` inside a compositor, the abstraction has already failed.
- **Compositor ownership is machine-checked**, not documented and hoped for. `motion-regression/fixtures/*/ownership.json` records which compositor wrote which property, and its `violations` list must stay empty. A material track reaching `transform` silently corrupts the geometry compositor's own composition, so it is caught by the harness rather than by review.

Each compositor emits its **own** animation. Keynote gives every channel a separate curve — Fade and Move travels on `cubic-bezier(.311,.208,.2013,1)` while its opacity runs `cubic-bezier(.7028,0,.3007,.9992)` — and a WAAPI keyframe carries one easing for the whole segment. Merging them would make the transform quietly adopt the opacity's curve, which is exactly the flattening this design removes.

#### Where the numbers come from

Not from taste, and not from Keynote's HTML export. Two extractors read the source of truth directly:

| Tool | Reads | Gives |
|---|---|---|
| `tools/keynote-params.py` | Apple's `*.parameterGroup` archives inside Keynote.app | every effect's parameters and its per-segment Bézier curves, with a version lock |
| `tools/keynote-effects.py` | a `.key` file's Snappy/protobuf payload | which effects a deck uses, and each one's exact duration |

Both label evidence. Parameters, curves, effect counts and durations are `exact`; the mapping from a parameter name to an animation phase is `inferred` and says so, because the file does not record it.

> **Do not use Keynote's HTML export as a reference.** Its own `kpfAnimationFallbacks.plist` downgrades `FromDarkness`, `LineDraw`, `LineDrawForLine` and `wipe` to a plain `apple:dissolve`. Timings measured from that export describe a dissolve, not the effect your deck actually uses — which is how those effects went missing from this library in the first place.

#### Verifying a change

```bash
node motion-regression/capture-frame.js
```

See [motion-regression/README.md](motion-regression/README.md). Failures are classified by which artefact disagrees — IR, compositor, ownership contract, or just browser rendering.

#### Motion Tokens (in `tokens/effects.css`)

| Token | Value | Purpose |
|---|---|---|
| `--ease-reveal` | `cubic-bezier(0.2, 0.65, 0.2, 1)` | Standard entrance easing |
| `--ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | Fast deceleration, snappy entries |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Overshoot spring, for hero numbers |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric, for slide transitions |
| `--dur-fast` | `200ms` | Quick micro-interactions |
| `--dur-normal` | `400ms` | Standard UI transitions |
| `--dur-slow` | `820ms` | Default build animation duration |
| `--dur-draw` | `1400ms` | SVG path drawing (e.g., depeg chart) |
| `--dur-page` | `500ms` | Slide transition duration |

**Keynote-parity tokens.** These were measured from Keynote's own HTML export of the source decks, not guessed — see `tools/keynote-effects.py`.

| Token | Value | Purpose |
|---|---|---|
| `--ease-keynote` | `cubic-bezier(0.42, 0, 0.58, 1)` | CAMediaTimingFunction easeInEaseOut — Keynote's default on 5977 of 7242 measured animations. Symmetric, unlike `--ease-reveal` |
| `--dur-build` | `500ms` | Dominant Keynote build duration |
| `--dur-zoom-big` | `350ms` | `apple:bc-zoom-big`, measured |
| `--dur-transition` | `1000ms` | Keynote slide transition |
| `--spread-delivery` | `333ms` | Per-unit delivery window (see Delivery below) |
| `--move-distance` | `28px` | `fade-move` offset |
| `--zoom-big-from` | `10` | `zoom-big` starts this many × size |

#### Build Animations (Entrance Effects)

Add `data-peg-animate` to any element inside a slide:

| Type | Keyframes | Best For |
|---|---|---|
| `fade-up` | `opacity 0→1, translateY(22px)→0` | Default for text, containers |
| `scale-in` | `opacity 0→1, scale(0.8)→1` | Hero numbers, wordmarks |
| `blur-in` | `opacity 0→1, filter blur(8px)→0` | Background elements |
| `reveal-right` | `opacity 0→1, translateX(30px)→0` | Flow nodes, list items |
| `letter-spring` | each character `opacity 0→1, translateY(0.72em)→0` with spring overshoot | One-line title or moment slides |
| `text-flip` | `opacity 0→1, translateY(0.42em)→0, rotateX(-82deg)→0` | Calm single-line text reveal |
| `draw` | SVG stroke draws on along its own path (`stroke-dashoffset` len→0) | **Lines, waveforms, chart curves, flow connectors** — a transient left-to-right *sweep*, never a perpetual loop |

**Keynote-parity builds.** Reproductions of the effects actually used in the source decks — run `tools/keynote-effects.py` on a `.key` to see which ones a deck uses.

| Type | Keynote effect | Keyframes | Best for |
|---|---|---|---|
| `fade-move` | `apple:fade and move` | `opacity 0→1` + offset `--move-distance` along `data-peg-direction` | Titles and body lines. The single most-used effect in the source decks (117×) |
| `zoom-big` | `apple:bc-zoom-big` | `opacity 0→1, scale(10)→1` | Numbers, one key word. Loud — once per slide |
| `pop` | `apple:bc-pop` | `opacity 0→1, scale(0.6)→1` with spring | Small cards, chips, legends; pairs with `data-peg-stagger` |
| `wipe` | `apple:wipe` | directional `clip-path: inset()` | Bars, rules, colour blocks. Restrained — nothing moves |
| `cube` | `apple:bc-3D-cube` | `rotateX(-90°)→0` with 1200px perspective, backface hidden | Section titles, anything wanting a "turn over" reading |
| `from-darkness` | `com.apple.iWork.Keynote.FromDarkness` — **Fade and Scale / 渐变和缩放** | scale + late opacity + a gradient reveal + a 70° specular sweep | Hero lines and cards **on a dark ground**. The second most-used effect in the source decks (89×) |
| `line-draw` | `com.apple.iWork.Keynote.LineDrawForLine` — **Line Draw / 画线** | SVG stroke draws on, start cap pops to 1.3×, pen tip rides the path | Charts, flow connectors, signatures, hand-drawn marks (32×) |
| `keyboard` | `apple:keyboard` — **Keyboard / 键盘** | text types out chunk by chunk behind a blinking caret | One line you want the room to read *with* you (5×) |

**These effects are why the library exists.** Keynote's own HTML export throws them away: `kpfAnimationFallbacks.plist` inside the app bundle downgrades `FromDarkness`, `LineDraw`, `LineDrawForLine` and `wipe` to a plain `apple:dissolve`. Reproducing them from Apple's `*.parameterGroup` definitions gets closer to the original deck than Apple's own exporter does.

**Builds are not single eases.** Every Keynote build overshoots and settles, each segment on its own curve, and that is what makes the motion feel like Keynote rather than like CSS:

| Effect | Measured path |
|---|---|
| `zoom-big` | `10 → 1.08 @62% → 0.95 @82% → 1` |
| `pop` | `0.6 → 1.125 @43% → 0.952 @66.7% → 1` |
| `cube` | `−90° → −6.02° @52% → +2.86° @60% → 0°` |
| `clothesline` | five damped bounces: `0.31 / −0.21 / 0.07 / −0.014 / 0.0017` |

Run `tools/keynote-params.py <Effect>` to see any effect's own numbers and curves.

#### Fade and Scale — dark ground required

`from-darkness` reveals through a gradient mask, so it only reads as "emerging from darkness" against a dark surface. On a light slide it degrades to a scale-and-fade. Where `mask-image` is unsupported the reveal is skipped and the build still plays as scale + opacity + shine rather than failing to appear.

#### Line Draw — SVG only

Put it on a `<path>`/`<line>` with a stroke. The pen tip and start cap are created inside the path's own `<svg>` and **removed when the build settles**, so the resting DOM is a plain finished stroke for screenshots, PDF and PPTX export. Path geometry is sampled once and cached; the cache invalidates on resize or `viewBox` change so the tip cannot drift off its line.

`draw` (the original, simpler sweep) is unchanged and still available.

#### Keyboard — deterministic by design

Chunk lengths vary, but from a seeded generator, so a replay types at exactly the same rhythm — Keynote behaves the same way, and a truly random rhythm could never be regression-tested. Override with `data-peg-seed`. `data-peg-cursor="off"` drops the caret and clamps chunks to 0.05–2.5s absolute, matching Keynote's cursorless mode. The caret is **3% of the line height** wide and blinks on a 0.4s half-cycle.

`data-peg-direction` (`top` / `bottom` / `left` / `right`) steers `fade-move` and `wipe`; `data-peg-distance` overrides the offset.

#### Delivery — per character or per word

`data-peg-delivery="character"` (or `"word"`) animates each unit separately.

```html
<h1 data-peg-animate="fade-move" data-peg-delivery="character">逐字淡入并移动。</h1>
```

Splitting uses `Intl.Segmenter` where available, so whole grapheme clusters survive — family emoji (`👨‍👩‍👧‍👦`), skin-tone modifiers (`👍🏽`), flags, combining marks. Word mode is segmented too, so a Chinese sentence is not treated as one word.

**Timing is a spread, not a fixed per-unit delay.** A line always lands within its `duration` no matter how many characters it has; each unit runs for the remainder after `--spread-delivery`. A fixed delay would drag a long sentence out over seconds. Set `data-peg-spread` to change the window, or `data-peg-letter-stagger` to force a fixed per-unit delay instead.

> Keynote's own per-character rhythm is **not** recoverable — its HTML export rasterizes text builds into image sequences. The spread model is Peg's design decision, not a measured Keynote value.

**Rich text is not split.** An element containing child markup (`<strong>`, `<a>`, …) keeps its structure, animates as one object, and logs a warning. Split spans get `aria-hidden`, and the parent gets an `aria-label` so screen readers read the line once.

#### Build steps — click to advance

Put `data-peg-step="N"` on anything that should wait for a click. `→` walks the steps on the current slide first and only turns the page once they are exhausted; `←` rewinds one step.

```html
<h1 data-peg-animate="fade-move">Now</h1>
<div class="card" data-peg-animate="fade-move" data-peg-step="1">Then</div>
<div class="card" data-peg-animate="fade-move" data-peg-step="2">Finally</div>
```

- Missing or invalid `data-peg-step` is treated as **0** (plays on slide entry). Invalid values warn.
- Numbers may **skip** — `1, 3, 7` compresses to three consecutive logical steps.
- Elements sharing a step fire **together**; per-character delivery inside each still staggers independently.
- Rewinding restores that step's before-state instantly; earlier steps stay built. Backward animation reads as a glitch, so Peg does not play one.
- Un-revealed content gets `visibility: hidden` and `pointer-events: none`, so it is never clickable, focusable, or read by assistive tech before its turn.
- Jumping by number key or thumbnail lands **fully built**, as does stepping back to an earlier slide.

#### Actions — animating something already on screen

| Action | Keynote effect | Attributes |
|---|---|---|
| `data-peg-action="move"` | `apple:action-motion-path` | `data-peg-x` / `data-peg-y` (px), optional `data-peg-path` |
| `data-peg-action="scale"` | `apple:action-scale` | `data-peg-scale` |
| `data-peg-action="opacity"` | `apple:action-opacity` | `data-peg-opacity` |

An element carries at most one action, so chain several by pointing separate directive elements at the same target with `data-peg-target`. The directive never renders, and the engine accumulates the changes — step 2 keeps step 1's move:

```html
<div class="dot" id="d"></div>
<i data-peg-action="move"    data-peg-target="#d" data-peg-x="700" data-peg-step="1"></i>
<i data-peg-action="scale"   data-peg-target="#d" data-peg-scale="1.8" data-peg-step="2"></i>
<i data-peg-action="opacity" data-peg-target="#d" data-peg-opacity="0.25" data-peg-step="3"></i>
```

`data-peg-path` (an SVG path `d`) is **progressive enhancement**: it uses CSS `offset-path` in the element's own coordinate system, with `offset-rotate: 0deg` so the object does not rotate along the curve. Where `offset-path` is unsupported it falls back to the straight `data-peg-x`/`-y` move, so the end state is identical either way.

**Author transforms are preserved.** A `transform` you already set — `rotate(-3deg)`, `translateX(-50%)` — is captured before the engine touches the element and composed as a prefix, so animation never swallows it. It is captured once, at compile time; a transform that changes responsively afterwards will not be picked up.

**Drawing lines & flows (the silky bit).** Put `data-peg-animate="draw"` on a **solid** SVG `<path>`/`<line>` (not an intentionally-dashed one) and it sweeps on left-to-right; duration follows `--dur-draw`, override with `data-peg-duration`. For a **flow / timeline that reveals left-to-right**, draw the baseline/connector with `draw` and stagger the nodes one-by-one (`data-peg-stagger` on the parent `<g>`, `data-peg-animate="fade-up"` on each node) with increasing `data-peg-delay`. The resting DOM is the full solid stroke, so screenshots / PDF export always show the finished line.

**Delays:** Use `data-peg-delay="80"` (ms) for individual timing.<br>
**Stagger:** Add `data-peg-stagger="100"` to a parent for automatic sibling delays.<br>
**Letter stagger:** Use `data-peg-letter-stagger="34"` (ms) for per-character timing.

```html
<div class="headline" data-peg-animate="fade-up" data-peg-delay="80">Title</div>
<div class="hero" data-peg-animate="scale-in" data-peg-delay="200">$306B</div>
<div class="headline" data-peg-animate="letter-spring">A one-line moment.</div>
<div class="chips" data-peg-stagger="100">
  <div class="chip" data-peg-animate="fade-up">Item 1</div>
  <div class="chip" data-peg-animate="fade-up">Item 2</div>
</div>
```

Open `letter-spring-demo.html` to preview the per-character title reveal.

**Backward compatible:** `.build.d1` through `.build.d5` classes still work (mapped to `fade-up` with 80/200/320/440/560ms delays).

#### Count-Up Numbers

Add `data-peg-count` or use `.count` class with data attributes:

```html
<div class="stat-n count" data-to="306" data-pre="$" data-suf="B" data-cdelay="360">$306B</div>
```

#### Data Bars

Add `data-peg-bar` to bars or use `.bar-fill` / `.progress-fill`. Horizontal bars grow left-to-right; vertical bars grow bottom-to-top.

```html
<div class="bar-fill" style="width:72%;"></div>
<div data-peg-bar="vertical" style="height:180px;"></div>
```

Use `data-peg-bar-duration`, `data-peg-bar-delay`, and `data-peg-bar-easing` for local timing overrides. The resting DOM remains the final value for screenshots, PDF, and PPTX export.

#### Slide Transitions

Add `data-peg-transition` to `<section>` (slide) elements:

| Value | Effect |
|---|---|
| `dissolve` | Crossfade (old fades out, new fades in) — `apple:dissolve` |
| `clothesline` | Pages swing and dip as they are pushed sideways, settling with a spring — `apple:ClotheslinePush`. Direction follows forward/back |
| `push-left` | New slides in from right, old slides out left |
| `text-flip` | Old slide flips upward while the new slide flips in from below on the same timeline |
| `none` | Instant cut (default) |

> Keynote's `apple:bc-3D-cube` is a **build**, not a transition — the `bc-` prefix means build. It is `data-peg-animate="cube"` above, applied per object.

#### Magic Move — `data-peg-transition="magic-move"`

The most-used transition in the source decks: `$apple:magic-move-implied-motion-path`, 70 instances, on **28 of PianoTuner's 48 slides**. Objects the two slides share travel from where they were to where they are going; everything else cross-fades.

Pair objects with the same `data-peg-id` on both slides:

```html
<section class="paper">
  <div class="card" data-peg-id="hero">PCB v1</div>
  <div class="version" data-peg-id="ver">V1.0</div>
</section>

<section class="paper" data-peg-transition="magic-move">
  <div class="card wide" data-peg-id="hero">主控 + 电机</div>
  <div class="version" data-peg-id="ver">Now</div>   <!-- morphs in place -->
</section>
```

| Attribute | Default | Purpose |
|---|---|---|
| `data-peg-magic-duration` | `900` | Morph duration (ms) |
| `data-peg-magic-easing` | `--ease-keynote` | Timing function |
| `data-peg-magic-stagger` | auto | Per-item delay for *unmatched* content only |
| `data-peg-magic-match="text"` | off | Also pair plain-text elements with identical text |

**The rule that makes it read as Apple rather than busy: things that travel, travel together; things that merely appear, stagger.** Matched objects all move simultaneously so the eye reads one coherent spatial event — staggering them reads as chaos. Only unmatched content, which has no prior position, arrives in sequence (auto-derived, capped at 150ms per item and 600ms total — the 150ms figure is Apple's own, measured from the `StaggeredFadeIn` component on apple.com).

Text that changes size morphs by **`font-size`**, not by transform scale, so glyphs stay crisp instead of blurring or thickening. Position uses centre-based FLIP, so any `transform` you already set still composes.

Matching is by explicit `data-peg-id` because a silent mismatch is worse than no morph. `data-peg-magic-match="text"` opts into text pairing per slide (the same tiered approach reveal.js auto-animate takes).

#### The finale — modules converging on a lockup

Magic Move is what makes the Apple-style summary slide work, where the modules introduced through the deck reassemble around a central lockup. Ground truth from the source deck: that slide has **no builds at all** — the entire collage arrives through the transition, with the shared centre element anchored and everything else fading in around it.

So it needs no new engine feature: give the centre element a `data-peg-id` shared with the previous slide, lay the modules around it, and set `data-peg-transition="magic-move"`. See the last slide of `motion-library-demo.html`.

Layout guidance, from analysis of Apple's published summary slides: cap at **~12 tiles**, exactly one hero; encode hierarchy by **tile area, not font size**; make the number the loudest thing on the slide (labels should be ignorable); keep one accent colour, everything else monochrome.

```html
<section class="paper" data-label="Title" data-peg-transition="text-flip">...</section>
```

Transitions respect `prefers-reduced-motion` and are disabled when `noscale` is set on `<deck-stage>`. Open `transition-demo.html` to compare cut, dissolve, push-left, and text-flip.

#### Auditing a Keynote deck

`tools/keynote-effects.py` reads a `.key` directly (it is a zip of Snappy-compressed protobuf) and reports which animation effects it uses — useful when porting a deck to Peg and you need to know what to reproduce. Pure standard library, no dependencies.

```bash
python3 tools/keynote-effects.py deck.key --per-slide
```

Output labels its own **evidence level**, because the claims are not equally well founded: effect counts and slide association are `exact` (the identifier string is literally present in a given slide's payload), while durations are `heuristic` — doubles found near the identifier, which proximity alone does not prove are that effect's duration. `--strict` drops the heuristic section; `--json` emits machine-readable output for tooling; `--debug-iwa` reports per-block decode diagnostics.

For exact timing, export the deck from Keynote as HTML instead and read the per-slide JSON — that is how the Keynote-parity tokens above were measured. Note that the HTML export rasterizes text builds, so per-character timing is not recoverable from it.

`tools/fixtures/effect-counts.json` pins the counts for four reference decks, so a change to the Snappy/IWA decoding cannot regress silently.

#### Initialization

```html
<script src="deck-stage.js"></script>
<script src="peg-animate.js"></script>
<script>
  PegAnimate.init('deck-stage');
</script>
```

---

### Designing for Chinese (中文)

Peg is bilingual. Latin (Inter) is tuned for tight negative tracking and compact
leading; Chinese needs the opposite — square em-box glyphs collide under negative
tracking and cramp under tight leading. `tokens/cjk.css` re-tunes the type tokens
**only** when the document language is Chinese, so Latin decks are unaffected.

- Set `lang="zh-CN"` (or any `zh-…`) on `<html>` — the CJK layer activates
  automatically: tracking relaxes toward zero, display leading opens up
  (`--lh-tight` 1.12 / `--lh-snug` 1.20 / `--lh-body` 1.7).
- Chinese glyphs render in **Noto Sans SC**; Latin/numerals stay in **Inter**
  (per-glyph fallback), so a mixed line like “重写 ESP-IDF” looks right.
- Use the `.latin` class on a pure-Latin element inside a Chinese deck to restore
  Inter's tight tracking just for that element (e.g. a wordmark).
- For an offline / portable / PDF-exported Chinese deck, bundle the font with the
  deck (or a `pyftsubset` subset of the used glyphs) — don't rely on system fonts.

### Fonts & Licenses

The design system's code is **MIT**. The bundled fonts are **not** MIT — they ship
under the **SIL Open Font License 1.1 (OFL)** and are redistributed here with their
license text, as the OFL requires:

| Font | Role | License | Source |
|---|---|---|---|
| **Inter** by Rasmus Andersson | Latin / numerals | SIL OFL 1.1 — [`assets/Inter-OFL.txt`](assets/Inter-OFL.txt) | github.com/rsms/inter |
| **Noto Sans SC** by Google | Chinese (简体) | SIL OFL 1.1 — [`assets/NotoSansSC-OFL.txt`](assets/NotoSansSC-OFL.txt) | fonts.google.com/noto |

Under the OFL you may use, embed, and redistribute both fonts (incl. commercially)
provided the license text travels with them and the fonts are not sold on their own.
Keep the `*-OFL.txt` files alongside `assets/*.ttf` in any redistribution.

> Repo size note: `assets/NotoSansSC.ttf` is a full variable font (~17 MB). For a
> shipped deck, subset it to the glyphs you actually use to stay lean.

### License

**Code & design tokens:** MIT — use freely in commercial and personal projects.
**Bundled fonts (`assets/*.ttf`):** SIL OFL 1.1 (see *Fonts & Licenses* above).

---

---

## 中文

### Peg 是什么？

**Peg** 是一套开源设计系统与幻灯片框架，从一套生产级演示文稿中提炼而来。它为你提供完整、有主张的视觉语言，让你用 HTML/CSS 和 React 构建美观、可读性强的演示文稿——无需打开任何设计工具。包含 Claude Skill（`SKILL.md`），可直接导入 **Claude Design** 使用。

核心特点：
- **极简配色** — 6 个色彩 token，一种暖白背景，一种翠绿强调色
- **以字排版为核心** — Inter 可变字体，强负字间距，零装饰元素
- **数据优先** — 等宽数字、SVG 2px 图表线、内置数字滚动动画
- **扁平快速** — 无阴影、无渐变、无卡片边框；内容直接落在纸面上
- **默认可访问** — 所有动画尊重 `prefers-reduced-motion`；DOM 始终展示最终状态

---

### 适用场景

| 场景 | 使用内容 |
|---|---|
| 用 HTML 制作幻灯片 | `slides/` 模板 + `slides/slide-base.css` |
| 原型设计数据密集型 UI | `components/core/` React 组件 |
| 仅引入设计 token | `tokens/*.css` |
| 浏览设计语言规范 | `guidelines/*.card.html` |

---

### 八种幻灯片模板

| 模板 | 用途 |
|---|---|
| **Title（标题页）** | 封面——品牌字标 + $1.00 基准线 |
| **Headline（主张页）** | 一句粗体核心论点 + 补充说明 |
| **Stats（数据页）** | 两组关键数字 + 简短描述 |
| **Flow（流程页）** | 从左到右的价值/流程链 |
| **Chips（分类页）** | 带标签的分类网格 |
| **Attr List（属性页）** | 3–4 条粗体术语定义列表 |
| **Moment（转场页）** | 居中全屏问句或论点 |
| **Media / Proof（实证页）** | 放真实渲染图/CAD/PCB/实物照/截图——整幅、图文左右分栏、或 2–4 图实证墙 |

#### 实证 / 图片页

三种图片版式,均遵循设计语言(细线边框、无阴影、说明用 caption 字号):

- `<section class="media-full">` — 整幅:图片**就是**整页(Night 信箱底)。子元素:`<img class="media-img contain">`(`contain` 显示完整零件,去掉则填满裁切)、可选 `.media-scrim`、`.media-label`、`.media-title`、`.media-cap`。
- `<section class="paper media-split">` — 左文右图:左侧 `.media-text`,右侧一个带框 `<figure class="media-figure">`。
- `<section class="paper media-wall">` — 实证墙:一个 `.wall` 里放 2–4 个 `<figure class="cell">`,每个含 `.fig` + `<figcaption>`。

每张图片页都应带**证据标签**(`.evi` → RENDER / CAD / PCB / PROTOTYPE / APP)和一句说明,让观众清楚自己看到的是什么、且确为真实产物。

`media-wall` 的行高与标题字号都是为**真实产品照片**(而不只是精挑细选的截图)特意钉死的:墙内单行网格强制 `1fr`(否则不同长宽比的真实照片会把行高撑爆,超出墙自身的框、切掉下方说明文字);`.media-wall .headline` 也降到了 56px,防止两行标题压到下方的墙。除非已经用完整长度的图片和标题走过一遍效果,否则不要把它们改回 `auto` / 默认的 92px。

---

### 五个核心 React 组件

| 组件 | 用途 |
|---|---|
| `PegLine` | 标志性 $1.00 水平基准线 |
| `FlowBand` | 带箭头的流程图 |
| `Chip` | 带边框的键值标签胶囊 |
| `StatBlock` | 大字号数字 + 描述文字 |
| `AttrList` | 堆叠式属性定义行 |

---

### 设计 Token

```
tokens/
  colors.css      — 6 个调色板值 + 语义别名
  typography.css  — 7 种文字角色、字间距、字重
  spacing.css     — 间距比例 + 1920×1080 画布几何
  effects.css     — 线宽、圆角半径、动效曲线
  fonts.css       — Inter 可变字体 @font-face
```

---

### 配色方案

| Token | 色值 | 用途 |
|---|---|---|
| `--color-paper` | `#FAFAF8` | 唯一背景色，暖白 |
| `--color-ink` | `#16181D` | 主文本与线条 |
| `--color-night` | `#0B0B0C` | 舞台边框、外侧信箱区 |
| `--color-jade` | `#00A878` | 单一强调色，每张幻灯片最多使用一次 |
| `--color-alert` | `#E5484D` | 仅用于危险/损失/风险场景 |
| `--color-mute` | `#8A8A8E` | 标签、注脚、次要文本 |

---

### 设计原则

1. **只有一种背景**：Paper (`#FAFAF8`)，无深色页、无渐变页。
2. **只有一种强调色**：Jade 每页最多出现一次，不用于装饰。
3. **Alert 色需要理由**：`#E5484D` 仅用于真实的坏消息。
4. **无阴影**：无高程层级，内容直接落在纸面。
5. **最终状态优先**：截图与 PDF 导出始终显示完整幻灯片。
6. **等宽数字无处不在**：防止列宽抖动。
7. **标题文字强负字间距**：紧凑而非松散。

---

### 快速开始

```html
<!-- 引入 token 链 -->
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="slides/slide-base.css">

<!-- 使用幻灯片模板 -->
<div class="slide slide--headline">
  <div class="frame">
    <p class="label">章节标签</p>
    <h1 class="headline">一句醒目的核心论点。</h1>
    <p class="support">补充一句上下文说明。</p>
  </div>
</div>
```

---

### 动效补充

大标题页的一行字可用 `data-peg-animate="letter-spring"`，每个字母/汉字会从下方逐个弹性甩入并渐现，适合 Keynote 风格的 moment slide。用 `data-peg-letter-stagger="34"` 调整逐字间隔。

```html
<div class="headline" data-peg-animate="letter-spring">A one-line moment.</div>
```

如果需要更克制、无弹性的单行文字翻入，可用 `data-peg-animate="text-flip"`。

**Keynote 对齐的一套动效。** 参数不是拍脑袋定的——是从本机 Keynote 15.3 应用包里 Apple 自己的 `*.parameterGroup` 定义解出来的，见 `tools/keynote-params.py`。

| 类型 | Keynote 中文菜单名 | 适合用在哪 |
|---|---|---|
| `fade-move` | 渐变和移动 | 标题、要点句。四个 deck 里共 117 次，你最常用的一个 |
| `from-darkness` | **渐变和缩放** | 主标题、卡片，**必须深色底**。第二常用（89 次）：渐变揭开 + 70° 光泽扫过 |
| `zoom-big` | 放大 | 数字、单个关键词。冲击力强，一页最多一次 |
| `pop` | 弹入 | 小卡片、标签、图例。配 `data-peg-stagger` 依次弹入 |
| `wipe` | 划变 | 条状图形、分隔线、色块。沿一个方向擦出，不动位置 |
| `cube` | 立体翻转 | 章节标题、需要「翻面」隐喻的单个对象 |
| `line-draw` | **画线** | 图表、流程连线、手写标注（32 次）。起点弹跳 + 笔尖跟随 |
| `keyboard` | **键盘** | 想让全场跟着你一起读的那一行（5 次）。打字机 + 闪烁光标 |

**这三个新效果正是这套库存在的理由：** Keynote 自己的 HTML 导出会把 `FromDarkness` / `LineDraw` / `wipe` **降级成普通 `apple:dissolve`**（见应用包里的 `kpfAnimationFallbacks.plist`）。从 Apple 的参数定义重建，比 Apple 自己的导出更接近你的原稿。

**build 不是单条缓动。** 每个 Keynote build 都会过冲再回落，每段还有各自的曲线——这才是「像 Keynote」而不是「像 CSS」的原因：

| 效果 | 实测路径 |
|---|---|
| `zoom-big` | `10 → 1.08 @62% → 0.95 @82% → 1` |
| `pop` | `0.6 → 1.125 @43% → 0.952 @66.7% → 1` |
| `cube` | `−90° → −6.02° @52% → +2.86° @60% → 0°` |
| `clothesline` | 五段衰减回弹 `0.31 / −0.21 / 0.07 / −0.014 / 0.0017` |

用 `python3 tools/keynote-params.py <效果名>` 可以查任意效果的原始参数和曲线。

**画线**只能用在带描边的 SVG `<path>` / `<line>` 上。笔尖和起点圆点建在该 path 自己的 `<svg>` 里，**动画结束后自动移除**，静止 DOM 仍是一条完整实线（截图 / PDF / PPTX 导出干净）。路径只采样一次并缓存，resize 或改 viewBox 会自动失效重建，笔尖不会飘。

**键盘**的节奏是**有种子的伪随机**，不是真随机——重播时打字节奏完全一致（Keynote 也是确定性的，真随机没法做回归）。用 `data-peg-seed` 改种子；`data-peg-cursor="off"` 关光标并把每段钳到 0.05–2.5s。光标宽度是**行高的 3%**，闪烁半周期 0.4s。

方向用 `data-peg-direction="top|bottom|left|right"`，位移量用 `data-peg-distance`。

**逐字 / 逐词投递。** 加 `data-peg-delivery="character"`（或 `"word"`）：

```html
<h1 data-peg-animate="fade-move" data-peg-delivery="character">逐字淡入并移动。</h1>
```

用 `Intl.Segmenter` 拆分，所以完整的字素簇不会被拆坏——家庭 emoji `👨‍👩‍👧‍👦`、肤色修饰 `👍🏽`、国旗、组合音标都安全；`word` 模式也走分词，不会把整句中文当成一个词。

**节奏是「铺开」而不是固定每字延迟**：一行字无论多长都在 `duration` 内落完。固定延迟会让长句拖到好几秒。用 `data-peg-spread` 调投递窗口，或 `data-peg-letter-stagger` 强制固定间隔。

> Keynote 真正的逐字节奏取不到——它的 HTML 导出把文字 build 栅格化成了图片序列。这个铺开模型是 Peg 的设计决定，不是 Keynote 实测值。

**富文本不拆。** 元素里有子标签（`<strong>`、`<a>`…）时保持原结构、整体做动画并给出警告。拆出来的 span 带 `aria-hidden`，父元素补 `aria-label`，读屏只念一遍。

**页内逐步构建。** 给需要「点一下才出现」的元素加 `data-peg-step="N"`：方向键先在页内推进 build，走完才翻页；`←` 回退一步。

- 不写或写错 → 当作 `0`（进页即播），写错会警告
- 序号可以跳号：`1, 3, 7` 会压缩成三个连续的逻辑 step
- 同一 step 的元素**同时**出现；元素内部的逐字节奏各自独立
- 回退是瞬时复原该 step 的前态，前面的 step 保持终态——倒放动画看起来像 bug，所以不做
- 未出现的内容带 `visibility: hidden` + `pointer-events: none`，不会被点到、被 focus、被读屏念到
- 数字键 / 缩略图跳页、以及往回翻到之前的页，都直接落终态

**Action（页内动作）：** `data-peg-action="move|scale|opacity"`。一个元素只能带一个 action，要连着做就用 `data-peg-target` 让多个指令元素指向同一个目标——指令元素本身不渲染，引擎会**累加**状态（step 2 的缩放保留 step 1 的位移）：

```html
<div class="dot" id="d"></div>
<i data-peg-action="move"    data-peg-target="#d" data-peg-x="700" data-peg-step="1"></i>
<i data-peg-action="scale"   data-peg-target="#d" data-peg-scale="1.8" data-peg-step="2"></i>
<i data-peg-action="opacity" data-peg-target="#d" data-peg-opacity="0.25" data-peg-step="3"></i>
```

**你自己写的 transform 不会被吃掉。** 元素上已有的 `rotate(-3deg)`、`translateX(-50%)` 会在引擎接手前被捕获、作为前缀参与合成。注意它只在编译期捕获一次，之后随断点变化的 transform 不会被跟进。

**Magic Move（神奇移动）—— `data-peg-transition="magic-move"`。** 你三个 deck 里用得第二多的效果（70 次，PianoTuner 48 页里有 28 页在用）。两页共有的对象会从原位置「走」到新位置，其余内容交叉淡入淡出。用 `data-peg-id` 配对：

```html
<div class="version" data-peg-id="ver">V1.0</div>
<!-- 下一页 -->
<section data-peg-transition="magic-move">
  <div class="version" data-peg-id="ver">Now</div>   <!-- 原地形变 -->
</section>
```

**让它像苹果而不像杂耍的那条规则：会「走」的一起走，只是「出现」的才错开。** 配对上的对象**同时**移动——眼睛才能读成一个连贯的空间事件，错开就是混乱；只有没有前一位置的新内容才依次淡入（自动推导，每项上限 150ms、总计 600ms —— 150ms 是从 apple.com 的 `StaggeredFadeIn` 组件里量出来的苹果自己的值）。

字号变化的文字走 **`font-size` 插值**而不是 transform 缩放，笔画不会糊也不会变粗。位置用中心对齐的 FLIP，你自己写的 transform 依然保留。

配对只认显式的 `data-peg-id`——配错比不配更糟。要按文字内容配可以在该页加 `data-peg-magic-match="text"` 单独打开。

**总结模块合并页（苹果风格结尾）。** 这一页靠的就是 Magic Move：实测你的原稿里那一页**一个 build 都没有**——整个模块拼贴全是靠转场进来的，中间的主体锁定不动，其余模块在它周围淡入。所以不需要新功能：给中间元素一个和上一页共享的 `data-peg-id`，模块摆在四周，转场设成 `magic-move` 即可。见 `motion-library-demo.html` 最后一页。

版式建议（来自对苹果公开总结页的分析）：**最多 ~12 块**，只留一个 hero；层级用**色块面积**而不是字号来表达；数字要是全页最响的东西（标签应该可以被忽略）；只用一个强调色，其余全部单色。

打开 `motion-library-demo.html` 可以逐页试所有效果。

**线条 / 波形 / 流程图的丝滑动效。** 给**实线** SVG `<path>`/`<line>`(不要给本就虚线的)加 `data-peg-animate="draw"`，它会沿自身路径**从左到右扫出**(`stroke-dashoffset`，时长跟随 `--dur-draw`)——用于折线、波形、图表曲线、流程连线;是一次性的扫入,不是无限循环(无限循环是廉价感来源)。**让流程/路程图从左到右依次出现**:基线/连线用 `draw`,节点用 `data-peg-stagger`(父 `<g>`)+ `data-peg-animate="fade-up"`(每个节点)配合递增 `data-peg-delay`。静止 DOM 始终是完整实线,截图 / PDF 导出显示成品。

**多幕配色:** 给每个 `<section>` 设 `--accent: var(--topic-…)`(见上方主题色表),该页所有强调元素(关键词、`.evi`、图表线)自动跟随;低饱和、每页一种、同页一致。**图文同页**用 `.headline.with-fig` 把标题降一档;**图下结论**用 `.summary` 居中放在图的下方做引导;**`.plain`(大白话行)** 放在标题下、带主题色竖条,给非专业观众一句人话——幻灯片保留技术内容,这行只让所有人都看懂(加粗最关键那半句;图文同页要限 `max-width` 到文字栏;两行标题时注意 `top` 别压住)。样本见 `slides/` 模板 11。**`.compare`(前后对比表)** 每行「过去的局限 → 现在怎么做」,是给非专业观众**一眼看懂"迭代了什么"**最有效的形式;`.badge-first` 给真正"行业首创"的行打徽标(少用、且要有依据)。样本见模板 12。

```html
<div class="headline" data-peg-animate="text-flip">A calm upward reveal.</div>
```

打开 `letter-spring-demo.html` 可预览逐字标题动效。

数据柱、横条、进度条可加 `data-peg-bar`，或直接使用 `.bar-fill` / `.progress-fill`。横向默认从左到右增长；竖向使用 `data-peg-bar="vertical"`，从底部向上增长。

```html
<div class="bar-fill" style="width:72%;"></div>
<div data-peg-bar="vertical" style="height:180px;"></div>
```

可用 `data-peg-bar-duration`、`data-peg-bar-delay`、`data-peg-bar-easing` 单独调整时长、延迟和曲线。DOM 保持最终数值，截图、PDF、PPTX 导出不显示半成品。

页面切换可在 `<section>` 上添加 `data-peg-transition="dissolve"`、`data-peg-transition="clothesline"`（`apple:ClotheslinePush`，摆动+下坠，方向跟随前进/后退）、`data-peg-transition="push-left"` 或 `data-peg-transition="text-flip"`；`text-flip` 会让旧画面向上翻出，同时新画面从下方翻入，两个动作在同一时间轴上连贯进行。不设置时为默认瞬切。切换动效尊重 `prefers-reduced-motion`，并在 `noscale` 导出模式下关闭。打开 `transition-demo.html` 可对比 cut、dissolve、push-left、text-flip。

```html
<section class="paper" data-label="Title" data-peg-transition="text-flip">...</section>
```

---

### 中文排版

Peg 双语可用。拉丁字体(Inter)为强负字距 + 紧凑行高而调;中文恰好相反——方块字在负字距下会相互挤撞、在紧行高下多行会发闷。`tokens/cjk.css` **仅在文档语言为中文时**重新调校排版 token,英文 deck 不受影响。

- 在 `<html>` 上设 `lang="zh-CN"`(或任意 `zh-…`),中文排版层自动生效:字距放松趋近 0,显示行高打开(`--lh-tight` 1.12 / `--lh-snug` 1.20 / `--lh-body` 1.7)。
- 汉字用 **Noto Sans SC** 渲染,拉丁字母/数字仍用 **Inter**(逐字回退),所以「重写 ESP-IDF」这种中英混排也对。
- 中文 deck 里若有纯拉丁元素(如品牌字标),给它加 `.latin` 类即可单独恢复 Inter 的紧字距。
- 离线/换机/导 PDF 的中文 deck:把字体随 deck 打包(或用 `pyftsubset` 子集化到实际用字),**不要**依赖系统字体。

### 字体与许可

设计系统的**代码是 MIT**;但随附字体**不是 MIT**——它们以 **SIL 开源字体许可 1.1(OFL)** 发布,并按 OFL 要求随附了许可证全文:

| 字体 | 用途 | 许可 | 来源 |
|---|---|---|---|
| **Inter**(Rasmus Andersson) | 拉丁 / 数字 | SIL OFL 1.1 — [`assets/Inter-OFL.txt`](assets/Inter-OFL.txt) | github.com/rsms/inter |
| **Noto Sans SC**(Google) | 简体中文 | SIL OFL 1.1 — [`assets/NotoSansSC-OFL.txt`](assets/NotoSansSC-OFL.txt) | fonts.google.com/noto |

OFL 允许自由使用、嵌入、再分发(含商用),前提是**许可证文本随字体一同保留**、且不得单独售卖字体本身。再分发时请把 `*-OFL.txt` 与 `assets/*.ttf` 一起带上。

> 仓库体积提示:`assets/NotoSansSC.ttf` 是完整可变字体(~17 MB);打包成 deck 时请子集化到实际用字以保持精简。

### 许可证

**代码与设计 token:** MIT — 可自由用于商业及个人项目。
**随附字体(`assets/*.ttf`):** SIL OFL 1.1(见上方「字体与许可」)。
