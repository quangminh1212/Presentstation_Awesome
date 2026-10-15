# animus-document-engine

An **MCP (stdio) service** that renders, parses, converts, and edits Office
documents — **Excel (.xlsx), PowerPoint (.pptx), Word (.docx)** — from a
structured JSON **spec**. It is identity-free and stateless: it never touches
subjects, S3, or users. The [animus-launchapp](https://github.com/launchapp-dev/animus-launchapp)
portal orchestrates it (storage + scoping + subjects); this engine is the reusable
rendering core.

Part of **REQUIREMENT-053** — Documents as subjects.

## Why a spec

The **spec is the source of truth**. An AI authors a spec (not raw OOXML); a
deterministic renderer turns it into a real file. Editing = mutate the spec and
re-render — lossless, reviewable, and diffable. Binary payloads cross the MCP
boundary as base64.

## Tools

| Tool | In | Out |
|------|-----|-----|
| `render_document` | `format`, `spec` | base64 OOXML bytes |
| `parse_document` | `format`, `bytes_base64` | spec (**xlsx only** in v1) |
| `apply_edits` | `format`, `spec`, `ops[]` | edited, re-validated spec |
| `convert_document` | `bytes_base64`, `to` | base64 converted bytes (e.g. `pdf`) |
| `preview_document` | `bytes_base64`, `kind` (`pdf`\|`png`), `page` | base64 PDF or PNG thumbnail |

`convert_document` / `preview_document` use **LibreOffice compiled to WebAssembly**
(`@matbee/libreoffice-converter`) — no native `soffice` needed. The ~112 MB WASM
lives in this service, never in the portal image.

## Spec shapes (v1)

```jsonc
// xlsx
{ "sheets": [ { "name": "Revenue",
                "columns": [ { "header": "Month" }, { "header": "USD" } ],
                "rows": [ ["Jul", 1200], ["Aug", 1500] ] } ] }

// pptx
{ "title": "Kickoff",
  "slides": [ { "title": "Agenda", "bullets": ["Scope", "Timeline"] },
              { "title": "Next", "body": "…", "notes": "speaker note" } ] }

// docx
{ "title": "Spec",
  "blocks": [ { "type": "heading", "level": 1, "text": "Overview" },
              { "type": "paragraph", "text": "…" },
              { "type": "bullets", "items": ["a", "b"] },
              { "type": "table", "rows": [["a","b"],["c","d"]] } ] }
```

`apply_edits` ops: `{op:"set",path,value}`, `{op:"append",target,value}`,
`{op:"remove",target,index}`, `{op:"replace",value}` (`target` = `sheets`\|`slides`\|`blocks`).

## Run

```bash
npm install
npm run build
node dist/index.js        # MCP stdio server
```

Wire it into an Animus workflow phase (or any MCP client) as a stdio server:

```jsonc
{ "mcpServers": { "document-engine": { "command": "node", "args": ["dist/index.js"] } } }
```

## Dev

```bash
npm run dev        # tsx watch (stdio server)
npm run typecheck  # tsc --noEmit
npm run smoke      # render all 3 formats + xlsx parse/edit round-trip
tsx scripts/mcp-smoke.ts   # spawn the built server, call tools over MCP
```

## Scope (v1) & roadmap

- **Generate** all three formats — solid (pptxgenjs / docx / exceljs).
- **Parse** — xlsx (data + headers). **pptx/docx in-place parsing is DEFERRED** to
  a future Python worker (python-pptx / python-docx are the only libraries that
  faithfully round-trip arbitrary decks/docs); the engine errors loudly rather than
  silently dropping content.
- **Convert/preview** — via LibreOffice-WASM.
