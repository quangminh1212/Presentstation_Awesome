# command-tower-mcp-presentation

Marp-based slide deck for the Command Tower MCP presentation.

## Setup

```bash
npm install
```

## Build

```bash
# Preprocess (expands ++ fragment syntax into duplicated slides)
node preprocess.js

# Build to HTML (supports video, GIF, inline SVG)
npx @marp-team/marp-cli slides-built.md --html -o slides.html

# Build to PDF
npx @marp-team/marp-cli slides-built.md --html --pdf -o slides.pdf

# Build to PPTX
npx @marp-team/marp-cli slides-built.md --html --pptx -o slides.pptx
```

## Preview

```bash
# Terminal 1: watch slides.md and rebuild slides-built.md on change
node preprocess.js --watch

# Terminal 2: rebuild HTML on change
npx @marp-team/marp-cli slides-built.md --html --watch -o slides.html
```

TODO
- Picture of tons of deck boxes
- Explain about sharing decks / playtesting
- Demo of making a deck on archidekt + searching for cards on scryfall
- Add a poll
- Move the commmand tower banner to big reveal
    - replace with a robot cartoon
- Explain about Commander?
- QR code to add me?
- Part about reverse engineering Archidekt APIs
- 