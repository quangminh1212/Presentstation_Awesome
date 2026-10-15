# @lifeng688/pptx-mcp

A local MCP server for creating, reading, editing, and exporting PowerPoint `.pptx` files without requiring Microsoft PowerPoint.

Designed for LLM workflows — Claude Desktop, Claude Code, Cursor, VS Code, MCP Inspector, or any MCP-compatible host can use natural language to generate, inspect, and modify PowerPoint files locally.

Pure Node.js. No Microsoft Office required.

## Overview

`@lifeng688/pptx-mcp` lets an AI agent or developer create and manipulate presentations programmatically through a simple tool interface.

### What it can do

- **Create** basic presentations with a cover slide
- **Create** presentations from structured JSON outlines (DeckSpec)
- **Create** presentations from Markdown text
- **Read** presentation metadata and slide text content
- **Add** slides to an existing deck
- **Replace** text across a presentation
- **Apply** theme presets (content-preserving copy)
- **Export** deck content to structured JSON
- **List** and **open** generated presentations in the system viewer

### v0.2.0 positioning

v0.2.0 is a quality and stability release focused on making generated presentations more readable, safer, and more reliable. It improves layout spacing, long-text handling, table rendering, and path safety. It is not a full visual design engine — generated slides prioritise content correctness over pixel-perfect aesthetics.

## What's New in v0.2.0

### Layout and readability

- Improved default slide layout and spacing
- Better long-text fitting and dense bullet handling
- Better mixed Chinese/English content readability
- XML entity decoding fixes for text extraction (e.g. Q&A, R&D)

### New and improved slide types

Additional slide templates beyond the original cover/content/two_column:
- `blank` — empty slide for custom layouts
- `divider` — section-break style page
- `icon_list` — feature or checklist highlights
- `quote` — pull-quote style slide
- `table` — structured data table with header background and alternating rows
- `summary` — wrap-up / key takeaways slide
- `thank_you` — closing slide

Markdown title heuristics now infer slide types (e.g. "Agenda/目录" → agenda, "Summary/总结" → summary, "Thank you/谢谢" → thank_you).

### Table improvements

- Header backgrounds and alternating row colors
- Column width auto-calculation
- Table validation with warnings for oversized tables (>6 columns, >14 rows)
- Improved Markdown table parsing and placement

### Path safety

- Safer nested output path handling
- Invalid output extensions (`.txt`, `.md`, `.json`, `.pdf`) are rejected
- Path traversal, absolute paths, and workspace escape are blocked
- `normalizeOutputPptxPath` — unified helper for all file-writing tools

### apply_theme size support

`apply_theme` now accepts a `size` parameter:
- `preserve` — keep original slide dimensions (default)
- `wide` — record wide format metadata
- `standard` — record 4:3 metadata

Note: this records metadata but does not physically restructure the PPTX — actual dimension changes are reserved for a future release.

### Other reliability improvements

- More reliable read/export behavior after `add_slide`, `replace_text`, and `apply_theme`
- Consistent structured responses across all tools: `{ success, summary, message, data, warnings, error }`

## Installation

No installation needed — run directly via `npx`:

```bash
npx @lifeng688/pptx-mcp
```

Or install globally:

```bash
npm install -g @lifeng688/pptx-mcp
pptx-mcp
```

## MCP Client Configuration

### Via npx (recommended)

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "pptx": {
      "command": "npx",
      "args": ["@lifeng688/pptx-mcp"],
      "env": {
        "PPTX_MCP_WORKSPACE": "./pptx-workspace"
      }
    }
  }
}
```

### Local development

```json
{
  "mcpServers": {
    "pptx-local": {
      "command": "node",
      "args": ["./dist/index.js"],
      "env": {
        "PPTX_MCP_WORKSPACE": "./pptx-workspace",
        "PPTX_MCP_LOG_LEVEL": "debug"
      }
    }
  }
}
```

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `PPTX_MCP_WORKSPACE` | Output workspace directory for generated presentations | `./pptx-workspace` |
| `PPTX_MCP_LOG_LEVEL` | Logging verbosity (`info`, `debug`, `error`) | `info` |

## Available Tools

| Tool | Description |
|------|-------------|
| `ping` | Health check and server identity |
| `list_presentations` | List `.pptx` files in the workspace |
| `create_presentation` | Create an empty PPTX with a cover slide |
| `create_presentation_from_outline` | Generate a presentation from a structured JSON outline (DeckSpec) |
| `create_presentation_from_markdown` | Generate a presentation from Markdown text |
| `read_presentation` | Read metadata and per-slide text content from a PPTX |
| `add_slide` | Append a new slide to an existing presentation |
| `replace_text` | Find and replace text within a presentation |
| `apply_theme` | Apply a theme preset (content-preserving copy with optional size metadata) |
| `export_to_json` | Export presentation content as structured JSON |
| `open_presentation` | Open a presentation in the system's default viewer |

## Example Prompts

Natural language prompts an LLM client might send:

1. **Create a project review deck**

   "Create a 6-slide project review presentation with a business theme. Include a cover, agenda, three progress slides, a summary, and a thank-you slide."

2. **Convert Markdown notes into a presentation**

   "Turn these meeting notes into a presentation: # Meeting Notes\n\n## Agenda\n- Review Q1 results\n- Discuss Q2 plan\n\n## Q1 Results\n- Revenue up 15%\n- Team expanded to 12"

3. **Create a table-heavy business analysis deck**

   "Create a quarterly business review with a table comparing Plan A vs Plan B across cost, timeline, and risk."

4. **Add a summary slide to an existing deck**

   "Add a summary slide to quarterly-report.pptx with three key takeaways."

5. **Replace a term across a generated deck**

   "Replace all occurrences of 'Acme Corp' with 'Acme Inc' in my presentation."

## Quality Notes

v0.2.0 focuses on:

- readable layouts with better spacing
- safer file operations and path handling
- fewer text overflows on dense slides
- improved table rendering and validation
- better mixed Chinese/English text extraction

### Known limitations

- Visual design variety is still basic — generated slides may look simple
- Richer theme presets and more expressive layouts are planned for future versions
- No advanced image, media, or chart support yet
- No full PowerPoint theme XML engine — `apply_theme` currently copies content preserving the original structure
- `add_slide` rebuilds the deck from extracted text; complex original layouts may be simplified

## Development

```bash
npm install
npm run build
npm start
npm run inspect
```

## Testing

The v0.2.0 test suite focuses on regression coverage and content safety, including:

- Layout quality and spacing improvements
- New slide types (blank, divider, icon_list, quote, table, summary, thank_you)
- Long text fitting and dense bullet handling
- Table rendering and validation
- Mixed CJK content extraction
- Markdown-to-PPTX conversion
- `apply_theme` size parameter
- Path safety and extension validation
- Overwrite protection

## Security

- All file operations are constrained to the configured workspace directory
- Path traversal (`../`, `..\`, UNC paths, drive-letter paths) is rejected
- Absolute output paths are rejected
- Invalid output extensions (anything other than `.pptx`) are rejected
- Existing files are protected unless `overwrite=true` is explicitly set
- All logging goes to stderr; stdout is reserved for JSON-RPC protocol traffic only

## Roadmap

See [docs/roadmap.md](./docs/roadmap.md).

## License

MIT
