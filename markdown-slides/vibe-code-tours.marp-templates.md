# Marp Deck Templates

Six ready-to-use [Marp](https://marp.app) slide templates for your project-intro deck.
Each is **self-contained** — the theme (fonts, colors, CSS) lives in the `<style>` block
at the top of the file, so you only copy **one file** into your repo.

| Template | Best for | Look |
|---|---|---|
| `terminal-dark.md` | dev tools, CLIs, anything technical | dark charcoal, green accent, JetBrains Mono |
| `editorial-light.md` | writing, docs, thoughtful products | cream paper, Source Serif headings, indigo |
| `pitch-bold.md` | fast PechaKucha pitch, demo day | black, huge type, yellow accent |
| `minimal-docs.md` | clean, documentation-style | white, lots of whitespace, Inter |
| `product-demo.md` | screenshot-forward product tours | light, teal accent, framed shots |
| `burmese-first.md` | မြန်မာစာ decks | warm, Pyidaungsu / Noto Sans Myanmar |

Previews are in [`previews/`](./previews) (cover slide of each).

## Use one

```bash
# 1. copy a template into your repo
cp terminal-dark.md ~/my-project/slides/intro.md

# 2. edit the content (keep the <style> block)

# 3. render
marp slides/intro.md -o slides.html     # HTML (best for the web)
marp slides/intro.md -o slides.pdf      # PDF
marp slides/intro.md --images png       # one PNG per slide
```

No marp installed? `npm i -g @marp-team/marp-cli` (or `npx @marp-team/marp-cli ...`).

## Fonts

Each template `@import`s its fonts from Google Fonts, so rendering **online** just works.
Offline, it falls back to the closest system font in the stack. Myanmar text uses
`Pyidaungsu` / `Noto Sans Myanmar`.

## Screenshots in your deck

Reference images with a repo-relative path: `![caption](screenshots/01.png)`.
Capture them cleanly with **Chrome DevTools MCP** at a fixed resolution (1280×800).

## Previews

| | |
|---|---|
| **terminal-dark** | **editorial-light** |
| ![terminal-dark](previews/terminal-dark.png) | ![editorial-light](previews/editorial-light.png) |
| **pitch-bold** | **minimal-docs** |
| ![pitch-bold](previews/pitch-bold.png) | ![minimal-docs](previews/minimal-docs.png) |
| **product-demo** | **burmese-first** |
| ![product-demo](previews/product-demo.png) | ![burmese-first](previews/burmese-first.png) |
