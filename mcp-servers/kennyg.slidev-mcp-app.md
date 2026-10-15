# Slidev MCP App Server

MCP App Server that creates and previews Markdown-based slide presentations using [Slidev](https://sli.dev) syntax, directly within Claude Desktop.

> Inspired by [excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app)

<!-- TODO: Add demo.gif -->
<!-- ![Demo](demo.gif) -->

## Features

- 📝 **Full Slidev Markdown support** — slides separated by `---`, YAML frontmatter for layouts
- 🎨 **Live slide preview** with smooth transitions and keyboard navigation
- 🖼️ **Multiple layouts** — cover, center, two-cols, section, statement, end
- 💻 **Syntax-highlighted code blocks** via highlight.js
- 🧮 **LaTeX math rendering** via KaTeX — inline `$...$` or block `$$...$$`
- 📊 **Mermaid diagrams** — flowcharts, sequence diagrams, and more
- 🎤 **Speaker notes** — add `<!-- notes -->` comments to slides
- ✏️ **Built-in markdown editor** for manual tweaks
- 📋 **Thumbnail overview** strip for quick navigation
- 🔄 **Iterative editing** — add, update, delete, reorder slides via MCP tools

## Install

### Option 1: Download Extension (Recommended)

1. Download the latest `slidev-mcp-app.mcpb` from [Releases](../../releases)
2. Double-click the `.mcpb` file to install in Claude Desktop
3. Done — start creating presentations in your conversations

### Option 2: Build from Source

```bash
git clone https://github.com/kennyg/slidev-mcp-app.git
cd slidev-mcp-app
bun install
bun run build
```

Then add to your Claude Desktop config:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "slidev": {
      "command": "node",
      "args": ["/path/to/slidev-mcp-app/dist/main.js"]
    }
  }
}
```

Restart Claude Desktop to pick up the new server.

## Usage

Example prompts:

- *"Create a presentation about microservices architecture with 8 slides"*
- *"Make a slide deck covering our Q4 roadmap with a cover slide and section breaks"*
- *"Build a tech talk about Kubernetes with code examples"*
- *"Add a new slide after slide 3 with a two-column layout comparing Docker vs Podman"*

## MCP Tools

| Tool | Description |
|------|-------------|
| `slidev_create` | Create a new presentation from Slidev markdown or structured slides |
| `slidev_add_slide` | Insert a slide at any position |
| `slidev_update_slide` | Modify content or layout of a slide |
| `slidev_delete_slide` | Remove a slide |
| `slidev_get` | Retrieve full markdown and metadata |
| `slidev_list` | List all presentations in the session |
| `slidev_reorder` | Rearrange slide order by index |

## Slidev Markdown Syntax

```markdown
---
theme: default
title: My Presentation
---

---
layout: cover
---

# Welcome

Subtitle here

---

# Regular Slide

- Bullet points
- **Bold text**
- `inline code`

---
layout: two-cols
---

# Two Columns

Left content here

::right::

Right content here

---
layout: section
---

# New Section

---
layout: end
---

# Thank You!
```

### Supported Layouts

| Layout | Description |
|--------|-------------|
| `default` | Standard content slide |
| `cover` | Title/cover slide with gradient background |
| `center` | Centered content |
| `two-cols` | Two-column layout (split with `::right::`) |
| `section` | Section divider with accent gradient |
| `statement` | Large centered statement text |
| `intro` | Introduction slide |
| `end` | Closing slide |

## Development

```bash
bun install
bun run dev          # Watch mode — rebuilds server on changes
bun run dev:app      # Vite dev server for the preview UI
bun run build        # Production build
bun test             # Run parser unit tests
```

### Testing the Preview

Run `bun run dev:app` to start the Vite dev server and preview the slide renderer at `http://localhost:5173`. Use the **✏️ Edit** button to paste Slidev markdown and preview rendering. Arrow keys navigate between slides.

## Releasing

```bash
# 1. Bump version in manifest.json and package.json
# 2. Build
bun run build

# 3. Pack the .mcpb bundle
bun run pack

# 4. Create release
gh release create v0.1.0 slidev-mcp-app.mcpb --title "v0.1.0" --notes "Initial release"
```

## Architecture

```
slidev-mcp-app/
├── main.ts              # Entry point — stdio transport
├── server.ts            # MCP server — 7 tools for CRUD + reorder
├── manifest.json        # MCPB bundle metadata
├── package.json
├── tsconfig.json
├── tsconfig.server.json
├── vite.config.ts       # Vite config for preview UI bundling
├── CLAUDE.md            # Claude Code context
├── LICENSE
├── src/
│   ├── parser.ts        # Shared Slidev markdown parser
│   ├── mcp-app.ts       # Preview UI TypeScript entry
│   ├── mcp-app.html     # Preview UI HTML template
│   └── global.css       # Preview UI styles
├── test/
│   └── parser.test.ts   # Parser unit tests (bun test)
└── dist/                # Build output (gitignored)
```

## Credits

- [Slidev](https://sli.dev) by Anthony Fu — the presentation framework and syntax
- [excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app) — MCP App architecture inspiration
- [highlight.js](https://highlightjs.org/) — code syntax highlighting
- [marked](https://marked.js.org/) — markdown parsing
- [KaTeX](https://katex.org/) — LaTeX math rendering
- [Mermaid](https://mermaid.js.org/) — diagram rendering

## License

[MIT](LICENSE)
