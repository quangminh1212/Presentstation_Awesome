# html2pptx-mcp

`html2pptx-mcp` is an MCP server and CLI that converts slide-oriented HTML into
PowerPoint files.

The project is built around a simple responsibility split:

- LLMs generate constrained, fixed-size HTML because HTML and DOM structure are
  easy for agents to reason about.
- `html2pptx-mcp` renders that HTML in Chromium, measures the resulting DOM, and
  writes a PPTX file.
- The converter treats rendered HTML as the source of truth. It does not redesign,
  rebalance, or repair the layout.

This avoids asking an LLM to emit raw PowerPoint instructions directly, which
often leads to screenshots-only slides, broken fonts, inconsistent layout, and
hard-to-edit output.

## Status

This is an early implementation. It is already useful for simple slide templates,
sales decks, proposals, and internal docs where the source can be expressed as
fixed-size HTML.

The current converter supports editable text, editable basic shapes, images, and
element-level raster fallbacks. Advanced CSS is intentionally handled through
raster fallback rather than incomplete PPTX object emulation.

## Features

- `1 HTML slide root = 1 PPTX slide`
- Default slide selector: `[data-html2pptx-slide], [data-slide], section.slide, .slide`
- Chromium-based layout measurement with a fixed viewport
- Editable PPTX text boxes for normal text
- Editable PPTX shapes for simple backgrounds and borders
- Image extraction for `img`, `svg`, `canvas`, `picture`, and `video`
- Hybrid raster fallback for complex visual blocks
- Full-slide raster mode for visual fidelity checks
- MCP tool: `convert_html_to_pptx`
- MCP prompt: `html_slide_authoring_guidelines`
- CLI: `html2pptx`

## What This Is Not

This project is not a design engine. It does not infer better slide composition
from bad HTML.

For example, if a generated HTML slide places a card on top of a heading, the
converter should not move the card. That would make output less deterministic and
would hide authoring mistakes. Instead, the HTML generator should follow the
authoring guidelines below.

## Setup

Requirements:

- Bun
- Node.js `>=22`
- Playwright Chromium

Install dependencies and browser runtime:

```sh
bun install
bunx playwright install chromium
```

## Quick Start

Generate a PPTX from the sample deck:

```sh
bun run convert --input examples/basic.html --output examples/basic.pptx
```

Generate with an explicit mode:

```sh
bun run convert --input examples/basic.html --output examples/basic.pptx --mode hybrid
```

Build and use the compiled CLI:

```sh
bun run build
node dist/cli.js --input examples/basic.html --output examples/basic.pptx
```

## CLI

```sh
bun run convert --input deck.html --output deck.pptx
```

Common options:

```sh
--input <path>                    HTML input file
--html <html>                     HTML document or fragment
--output <path>                   PPTX output path
--mode <editable|hybrid|raster>   Render strategy, default: hybrid
--selector <selector>             Slide root selector
--viewport <WIDTHxHEIGHT>         Chromium viewport, default: 1280x720
--width <inches>                  PPTX slide width, default: 13.333
--height <inches>                 PPTX slide height, default: 7.5
--base-url <url>                  Base URL for relative assets
--wait-until <state>              load, domcontentloaded, or networkidle
--timeout <ms>                    Playwright timeout
```

Examples:

```sh
bun run convert --input deck.html --output deck.pptx --mode editable
bun run convert --input deck.html --output deck.pptx --mode hybrid
bun run convert --input deck.html --output deck.pptx --mode raster
bun run convert --input deck.html --output deck.pptx --viewport 1280x720 --width 13.333 --height 7.5
```

## MCP Setup

During development, point your MCP client at the TypeScript entrypoint:

```json
{
  "mcpServers": {
    "html2pptx": {
      "command": "bun",
      "args": ["run", "/absolute/path/to/html2pptx-mcp/src/index.ts"]
    }
  }
}
```

After building:

```sh
bun run build
```

```json
{
  "mcpServers": {
    "html2pptx": {
      "command": "node",
      "args": ["/absolute/path/to/html2pptx-mcp/dist/index.js"]
    }
  }
}
```

## MCP Tool

### `convert_html_to_pptx`

Converts HTML into a `.pptx` file.

Minimal file-based input:

```json
{
  "htmlFilePath": "/absolute/path/to/deck.html",
  "outputPath": "/absolute/path/to/deck.pptx"
}
```

Inline HTML input:

```json
{
  "html": "<section class=\"slide\"><h1>Hello</h1></section>",
  "outputPath": "/absolute/path/to/hello.pptx"
}
```

Typical full input:

```json
{
  "htmlFilePath": "/absolute/path/to/deck.html",
  "outputPath": "/absolute/path/to/deck.pptx",
  "mode": "hybrid",
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "layout": {
    "width": 13.333,
    "height": 7.5
  },
  "slideSelector": "section.slide"
}
```

Result:

```json
{
  "mode": "hybrid",
  "outputPath": "/absolute/path/to/deck.pptx",
  "slideCount": 2,
  "warnings": []
}
```

## MCP Prompt

### `html_slide_authoring_guidelines`

Returns a prompt fragment that tells an LLM how to generate fixed-size HTML that
converts cleanly to PPTX.

Use this before asking an LLM to create the HTML source for a deck. The prompt is
part of the MCP package because it describes the input contract, but the converter
still does not alter layouts automatically.

## Conversion Model

1. Load HTML from `html` or `htmlFilePath`.
2. Wrap fragments in a minimal document when needed.
3. Inject runtime CSS for fixed slide dimensions.
4. Render in Chromium at the configured viewport.
5. Wait for fonts and images.
6. Find slide roots using `slideSelector`.
7. Measure visible DOM boxes relative to each slide root.
8. Convert simple boxes and text into editable PPTX objects.
9. Rasterize complex elements depending on render mode and hints.
10. Write a PPTX file with one output slide per slide root.

## HTML Contract

Use one root element per slide:

```html
<section class="slide">
  <h1>Quarterly Plan</h1>
  <p>Simple HTML becomes editable PowerPoint content.</p>
</section>
```

Slides are rendered in a fixed Chromium viewport, defaulting to `1280x720`, and
mapped to a PPTX layout, defaulting to `13.333 x 7.5` inches.

Recommended slide shell:

```html
<section class="slide">
  <main class="content">
    <!-- slide content -->
  </main>
</section>
```

```css
.slide {
  width: 1280px;
  height: 720px;
  overflow: hidden;
  position: relative;
}

.content {
  inset: 64px;
  position: absolute;
}
```

Prefer:

- predictable layout inside each slide root
- real text for content that should remain editable
- simple backgrounds, borders, border radii, and text
- local or resolvable image assets
- `data-html2pptx-rasterize` on complex visual blocks

Avoid relying on unsupported CSS when editability matters:

- gradients
- filters
- transforms
- shadows
- advanced typography
- pseudo-element-only content
- layout that only works because of accidental overlap

## LLM Authoring Guidelines

The converter intentionally does not repair layout. It treats the rendered HTML
as the source of truth. When an LLM generates HTML, include these rules in the
prompt:

- Treat each slide as a fixed `1280x720` canvas unless another viewport is specified.
- Keep primary content at least `64px` from slide edges unless the element is a
  full-bleed background.
- Keep visual margins balanced. Avoid pushing major panels hard against only one edge.
- Reserve named regions before placing content: header, body, left column, right
  panel, chart area, note area, footer.
- Use grid or flex for primary content.
- Use absolute positioning only when the target frame is explicitly reserved.
- Do not overlap primary text, headings, cards, charts, or panels.
- Overlap only when it is an intentional decoration.
- If decorative overlap is intentional, isolate it in a small element and consider
  `data-html2pptx-rasterize`.
- Leave visible gutters between neighboring regions. A useful default is `32-64px`
  between columns and `64-96px` at the slide edge.
- Keep text boxes within stable bounds.
- Do not rely on CSS auto height for long text that may overflow after conversion.
- Prefer shortening copy, splitting a slide, or changing the layout over shrinking
  text below readable sizes.
- Before returning HTML, check for accidental overlap, clipped text, edge collisions,
  and unbalanced margins.

## Render Modes

### `hybrid`

Default mode. Converts basic DOM content into editable PPTX objects and rasterizes
complex elements such as:

- `img`
- `svg`
- `canvas`
- `picture`
- `video`
- transformed nodes
- filtered nodes
- `background-image` nodes
- nodes marked with `data-html2pptx-rasterize` or `data-rasterize`

Use this for most agent-generated slide decks.

### `editable`

Keeps normal DOM content editable and avoids full-slide screenshots. Intrinsic
visual elements such as images, SVG, and canvas still become images in the PPTX.

Use this when editability matters more than pixel-perfect fidelity.

### `raster`

Screenshots each slide root into one image per PPTX slide.

Use this for visual previews, fallback delivery, or situations where exact
rendering matters more than editability.

## Element Hints

Ignore an element:

```html
<div data-html2pptx-ignore>Not exported</div>
```

Rasterize an element as an image:

```html
<div data-html2pptx-rasterize>
  <!-- complex visual block -->
</div>
```

`data-rasterize` is also supported as a shorter alias.

## Limitations

The converter currently handles common presentation primitives. It does not try
to fully implement the CSS visual formatting model in PPTX.

Known limitations:

- Text extraction is intentionally simple.
- Complex inline rich text may be flattened.
- Shadows, filters, transforms, and gradients should be rasterized.
- Pseudo-element content is not a reliable editable output source.
- Tables and charts are not converted to native PowerPoint table/chart objects yet.
- The converter does not run a visual design critique.
- The converter does not auto-fix overlap, margins, typography, or content density.

## Troubleshooting

### Playwright browser is missing

Run:

```sh
bunx playwright install chromium
```

### The PPTX opens but content is not editable

Check the selected mode. `raster` intentionally writes screenshot slides. Use
`hybrid` or `editable` for editable text and shapes.

Also check whether the element has `data-html2pptx-rasterize`, uses a complex CSS
feature, or is an intrinsic visual element such as `svg` or `canvas`.

### Relative assets do not load

When using `htmlFilePath`, the file directory is used as the base URL. When using
inline `html`, pass `baseUrl`.

### Layout looks wrong after conversion

Inspect the source HTML at the same viewport first. The converter follows
Chromium layout. If the rendered HTML has overlap or unbalanced spacing, fix the
HTML or the LLM authoring prompt.

## Development

This repository uses:

- package manager: Bun
- formatter: `oxfmt`
- linter: `oxlint`
- tests: `vitest`

Commands:

```sh
bun run format
bun run format:check
bun run typecheck
bun run lint
bun run test
bun run check
bun run build
```

Run the sample conversion:

```sh
bun run convert --input examples/basic.html --output /tmp/html2pptx-basic.pptx
unzip -t /tmp/html2pptx-basic.pptx
```

## Repository Layout

```txt
src/
  cli.ts          CLI entrypoint
  converter.ts    HTML rendering and PPTX generation
  css.ts          CSS parsing helpers
  guidelines.ts   LLM-facing HTML authoring prompt
  html.ts         HTML document normalization
  index.ts        MCP server entrypoint
  types.ts        Shared types
examples/
  basic.html      Example two-slide deck
tests/
  *.test.ts       Vitest tests
```
