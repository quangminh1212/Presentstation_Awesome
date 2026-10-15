# pptgenerator-cli

> Slide outline (Markdown / JSON) → HTML preview → PPTX, Manus-style.

`pptgenerator-cli` is a Node.js + TypeScript pipeline that takes a slide outline
and produces:

1. a self-contained **HTML preview** styled with Tailwind (via CDN) and
   [Iconify](https://iconify.design/) icons — the same visual you ship to
   PowerPoint;
2. a real **.pptx** file built from that HTML by screenshotting each slide and
   embedding it full-bleed (the _image strategy_). A future _structured
   strategy_ will produce editable PPT shapes.

The whole flow is designed around a single in-memory contract — the
`SlideDeck` IR — so adding a new input format = new parser, and adding a new
output format = new renderer.

```text
deck.md / deck.json ─▶ parsers/ ─▶ SlideDeck IR ─┬─▶ renderers/html/    ─▶ deck.preview.html
                                                 └─▶ renderers/pptx/    ─▶ deck.pptx
                                                       (image strategy)
```

## Install

```bash
pnpm install
pnpm playwright:install   # downloads chromium for the image strategy
```

## CLI

```bash
# Render the HTML preview (open it directly in any browser)
pnpm render-html examples/deck.md -o out/deck.html

# Build a .pptx (default: image strategy)
pnpm build-pptx examples/deck.md -o out/deck.pptx

# Future: editable shapes (currently throws "not implemented yet")
pnpm build-pptx examples/deck.md -o out/deck.pptx --strategy structured
```

## Library

```ts
import { loadDeck, renderHtml, buildPptx } from "pptgenerator-cli";

const deck = loadDeck("examples/deck.md"); // auto-detects md vs json
const html = renderHtml(deck); // string
await buildPptx(deck, { outputPath: "deck.pptx" }); // image strategy by default
```

## Markdown convention

Slides are separated by a blank-line `---` thematic break. Inside a slide a
blank-line `:::` line splits a two-column layout.

```md
---
title: My Deck
author: Yuki
theme: default
---

# Title slide

## Optional subtitle

---

## Section divider

---

## A content slide

- :icon[lucide:rocket] Bullets can carry an inline icon
- Plain bullet
- More text

---

## Two-column slide

- left bullet 1
- left bullet 2

:::

- right bullet 1
- right bullet 2
```

Theme names accepted by frontmatter: `default`, `dark`, `minimal`.

## JSON shape

`examples/deck.json` mirrors the IR exactly. The IR is validated with `zod`
([src/ir/schema.ts](src/ir/schema.ts)) and the TypeScript types live in
[src/ir/types.ts](src/ir/types.ts).

## Icons (Iconify CDN)

We never bundle SVGs. The HTML renderer emits

```html
<img src="https://api.iconify.design/lucide/rocket.svg?width=48" />
```

so any of Iconify's 200,000+ icons can be referenced via `prefix:slug`
(`lucide:rocket`, `mdi:account`, `tabler:wand`, …). The image strategy
pre-renders the HTML in headless chromium, so the icons end up baked into the
.pptx pixels — your audience never needs internet access.

## Project layout

```
src/
  cli.ts                       # `pptgenerator-cli` binary
  index.ts                     # library exports
  ir/{types,schema}.ts         # SlideDeck IR + zod validator
  parsers/{markdown,json,index}.ts
  renderers/
    html/{render,template,icons}.ts
    pptx/{render,strategy,image-strategy,structured-strategy}.ts
examples/{deck.md,deck.json}
tests/                         # vitest specs
```

## Scripts

| script                    | purpose                                                             |
| ------------------------- | ------------------------------------------------------------------- |
| `pnpm dev <args>`         | run the CLI from source via tsx                                     |
| `pnpm render-html`        | shorthand for `dev render-html`                                     |
| `pnpm build-pptx`         | shorthand for `dev build-pptx`                                      |
| `pnpm build`              | bundle to `dist/` with tsup                                         |
| `pnpm typecheck`          | `tsc --noEmit`                                                      |
| `pnpm test`               | vitest — Layers A, B, B+ unit, D (cheap, default-on)                |
| `pnpm test:integration`   | sets `PPT_INTEGRATION=1` — adds Layer B+ PPTX media audit           |
| `pnpm test:visual`        | sets `PPT_VISUAL=1` — Layer C visual regression (run inside Docker) |
| `pnpm test:watch`         | vitest in watch mode                                                |
| `pnpm lint`               | ESLint over `src/` and `tests/`                                     |
| `pnpm format[:check]`     | Prettier write / check                                              |
| `pnpm playwright:install` | download chromium (one-off, required for image strategy)            |

## Evaluation harness

Because the pipeline is HTML → PNG → PPTX, regressions can hide at multiple
layers. `tests/` is organized as a layered harness so cheap checks run on
every push and expensive ones only when explicitly invoked.

| layer  | what it guards                                             | gate                                          |
| ------ | ---------------------------------------------------------- | --------------------------------------------- |
| **A**  | IR shape after parsing (`tests/snapshots/parsers.snap`)    | always on                                     |
| **B**  | HTML structure / Tailwind class output                     | always on                                     |
| **B+** | PPTX media + structural audit (unzip + magic bytes)        | unit always; chromium leg `PPT_INTEGRATION=1` |
| **C**  | Pixel-level visual regression with pixelmatch              | `PPT_VISUAL=1`, **Docker only**               |
| **D**  | `--evaluation-mode` swaps CDNs for vendored offline assets | always on (static checks)                     |

### `--evaluation-mode`

Both subcommands accept `--evaluation-mode`. When set, the renderer rewrites
Tailwind + Iconify CDN refs to `file://` URLs under `vendored/`:

```bash
pnpm build-pptx examples/deck.md -o out/deck.pptx --evaluation-mode
```

Use it for air-gapped builds, deterministic CI runs, or to make Layer C
visual baselines reproducible across machines.

### Updating Layer C baselines (Docker)

Visual baselines depend on the exact chromium build, system fonts, and the
Linux text-rendering stack — so they are produced and compared inside the
shipped Docker image only:

```bash
docker build -t pptgenerator-cli:dev .
docker run --rm -e PPT_VISUAL_UPDATE=1 \
    -v "$PWD":/work -w /app pptgenerator-cli:dev \
    /app/node_modules/.bin/vitest run tests/visual
```

Commit the regenerated PNGs under `tests/visual/__baseline__/`.

## Distribution

Three publishing tracks ship with `v*` tags:

1. **npm** (`pptgenerator-cli`) — `npx pptgenerator-cli build-pptx ...`
   ([release.yml](.github/workflows/release.yml)).
2. **Docker** (GHCR `ghcr.io/chibayuki347/pptgenerator-cli`) — the canonical
   environment for Layer C; also the engine behind the GitHub Action
   ([docker.yml](.github/workflows/docker.yml)).
3. **GitHub Action** (`ChibaYuki347/pptgenerator-cli@v*`) — Docker-based;
   just declare `input` / `output` and the action handles the rest. See
   [`action.yml`](action.yml).

## License

MIT.
