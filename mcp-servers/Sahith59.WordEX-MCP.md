<p align="center">
  <img src="https://raw.githubusercontent.com/Sahith59/WordEX-MCP/main/logo.svg" width="140" alt="WordEX logo"/>
</p>

<h1 align="center">WordEX MCP</h1>

<p align="center">
  <strong>Read, write, and edit Word, Excel, PDF & PowerPoint files directly from GitHub Copilot — with zero copy-paste.</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/wordex-mcp"><img src="https://img.shields.io/npm/v/wordex-mcp?color=0f6b5c&label=npm" alt="npm version"/></a>
  <a href="https://www.npmjs.com/package/wordex-mcp"><img src="https://img.shields.io/npm/dm/wordex-mcp?color=1a3a5c&label=downloads" alt="npm downloads"/></a>
  <img src="https://img.shields.io/badge/tools-20-4ecdc4" alt="20 tools"/>
  <img src="https://img.shields.io/badge/local%20only-100%25-green" alt="100% local"/>
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"/>
</p>

<p align="center">
  Works with · <strong>GitHub Copilot</strong> · <strong>Claude Desktop</strong> · <strong>Cursor</strong> · <strong>Windsurf</strong> · <strong>Continue.dev</strong>
</p>

---

## 🔒 100% Local & Private

No data ever leaves your machine. No API keys. No cloud. No telemetry. Built for teams handling sensitive company documents.

---

## The Problem It Solves

Without WordEX, every AI-assisted document task looked like this:
1. Ask the AI to generate content
2. Manually copy the output
3. Open Word / Excel / Acrobat
4. Paste and reformat
5. Save

**With WordEX:**
```
Read ~/docs/api-tracker.xlsx and summarise the Status column
Create ~/docs/sprint-23.docx documenting my recent git changes
Extract all tables from ~/contracts/agreement.pdf
Read my pitch deck at ~/Presentations/Q4.pptx and give me key takeaways
OCR the scanned receipt at ~/Desktop/receipt.png
```

---

## Quick Start

```bash
npx wordex-mcp init
```

That's it. This single command detects every MCP-compatible editor on your machine and configures each one automatically. Then restart your editor.

### Install for all editors at once
```bash
npx wordex-mcp init --global
```

### Install for a specific editor
```bash
npx wordex-mcp init --vscode      # VS Code only
npx wordex-mcp init --claude      # Claude Desktop only
npx wordex-mcp init --cursor      # Cursor only
npx wordex-mcp init --windsurf    # Windsurf only
npx wordex-mcp init --continue    # Continue.dev only
```

---

## 20 Tools at a Glance

### 📄 Word Documents (.docx)
| Tool | Description |
|---|---|
| `read_document` | Read any .docx file from any path |
| `create_document` | Create a new .docx with markdown or plain text |
| `edit_document` | Append, prepend, replace, or replace-all in a .docx |
| `merge_documents` | Combine multiple .docx files into one |
| `fill_template` | Replace `{{variable}}` placeholders in a .docx template |
| `convert_to_markdown` | Export .docx → .md file |
| `document_stats` | Word count, reading time, Flesch readability score |
| `search_in_document` | Search inside a .docx with context lines |

### 📊 Excel Spreadsheets (.xlsx)
| Tool | Description |
|---|---|
| `read_document` | Read any .xlsx sheet or all sheets |
| `create_document` | Create a new .xlsx from row data |
| `edit_document` | Append rows, update cells, or add a sheet |
| `list_sheets` | List all worksheets in an .xlsx file |

### 📑 PDF Files (.pdf)
| Tool | Description |
|---|---|
| `read_pdf` | Extract text with metadata and page range support |
| `search_in_pdf` | Search inside a PDF with context |
| `extract_pdf_tables` | Detect and extract tables using spatial analysis |
| `extract_pdf_images` | Extract embedded JPEG images to a folder |
| `chunk_pdf` | Split large PDFs into labelled sections |

### 📊 PowerPoint (.pptx)
| Tool | Description |
|---|---|
| `read_pptx` | Extract all slides, bullets, and speaker notes |

### 🔍 OCR
| Tool | Description |
|---|---|
| `ocr_document` | OCR any image (PNG/JPG/TIFF/BMP/WebP) using Tesseract.js — fully local WASM |

### 🗂️ Filesystem & Git
| Tool | Description |
|---|---|
| `list_documents` | Find .docx, .xlsx, and .pdf files in any directory |
| `get_git_diff` | Get current git diff |
| `get_git_status` | See changed/staged/untracked files |
| `auto_document` | Save AI-generated git diff docs as .docx |

---

## Slash Commands

Type `/` in Copilot Chat to trigger structured prompts:

| Command | What it does |
|---|---|
| `/doc-read` | Read and summarise a document |
| `/doc-write` | Write content to a new document |
| `/doc-edit` | Edit an existing document |
| `/doc-autodoc` | Generate docs from git diff → .docx |
| `/doc-list` | List documents in a directory |
| `/doc-search` | Search inside a document |
| `/doc-pdf` | Read a PDF with metadata |
| `/doc-pptx` | Read a PowerPoint presentation |
| `/doc-template` | Fill a .docx template with variables |
| `/doc-merge` | Merge multiple .docx files |
| `/doc-stats` | Get word count and readability stats |

---

## Supported Path Formats

WordEX resolves paths intelligently on both Mac and Windows:

| Format | Example |
|---|---|
| Home shorthand | `~/Documents/report.docx` |
| Environment variable | `$PROJECT_DOCS/spec.docx` |
| Relative path | `./docs/notes.docx` |
| Absolute path (Mac) | `/Users/name/work/tracker.xlsx` |
| Absolute path (Windows) | `C:\Users\name\Documents\report.docx` |

---

## Manual Config

If `init` doesn't detect your editor, add this manually:

**VS Code** — `.vscode/mcp.json`
```json
{
  "servers": {
    "wordex": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "wordex-mcp"]
    }
  }
}
```

**Claude Desktop / Cursor / Windsurf** — their respective config files:
```json
{
  "mcpServers": {
    "wordex": {
      "command": "npx",
      "args": ["-y", "wordex-mcp"]
    }
  }
}
```

---

## Team Onboarding

Each team member runs one command in the project directory:
```bash
npx wordex-mcp init
```

Or commit `.vscode/mcp.json` to your repo — everyone on the team gets WordEX automatically when they open the project.

No accounts. No API keys. Nothing to share or rotate.

---

## Building from Source

```bash
git clone https://github.com/Sahith59/WordEX-MCP.git
cd WordEX-MCP
npm install
npm run build
node dist/cli.js init
```

---

## Privacy & Security

- **No network calls** — WordEX is a pure local stdio process. Zero HTTP requests.
- **No telemetry** — Nothing is tracked or reported.
- **No API keys** — No accounts or credentials of any kind.
- **Offline capable** — Works fully offline after the first `npx` download.
- **Your data stays on your machine** — always.

---

## Requirements

- Node.js 18+
- Any MCP-compatible editor (VS Code + Copilot, Claude Desktop, Cursor, Windsurf, or Continue.dev)

---

## License

MIT © [Sahith Reddy Thummala](https://github.com/Sahith59)
