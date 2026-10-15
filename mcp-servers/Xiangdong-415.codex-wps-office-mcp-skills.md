# Codex Office + PPT MCP Workflow Skills

Public Codex skills for working with Office-style document, spreadsheet, and presentation workflows.

This repository contains lightweight Codex skills, WPS/Word-focused MCP workflow notes, and a small stdio wrapper for Word/DOCX MCP servers. It helps agents use whatever Office-capable tools are available in their environment: WPS Office, local Microsoft Office, LibreOffice, Codex plugins, MCP servers, Google Workspace import tools, or structured file libraries.

This repository does **not** contain proprietary Office plugin code or a full MCP server implementation.

中文说明见 [README.zh-CN.md](README.zh-CN.md).

## Skills

| Skill | Use it for |
|---|---|
| `office-document-workflow` | Word/DOCX creation, editing, redlines, comments, formatting, document cleanup |
| `office-spreadsheet-workflow` | Excel/XLSX, CSV, formulas, charts, dashboards, workbook validation |
| `ppt-presentation-workflow` | PowerPoint/PPTX deck creation, redesign, editing, slide QA, speaker notes |
| `office-export-qa` | Final export, compatibility checks, metadata/privacy cleanup, visual QA |

## WPS + Word MCP Focus

In local use, the Word/DOCX MCP workflow performed especially well with WPS Office for `.docx` review and editing. This repository therefore includes:

- `wrappers/word_mcp_stdio_wrapper.py`: a small wrapper that keeps FastMCP/stdio startup output from polluting the MCP protocol stream.
- `config/mcp-config.example.json`: a placeholder config showing how to launch a Word MCP server through the wrapper.
- [docs/wps-word-mcp.md](docs/wps-word-mcp.md): setup and publishing notes.

This is the main practical improvement over a plain prompt-only Office workflow: it documents a tested WPS-friendly path and includes a wrapper that makes stdio MCP startup more reliable.

## Why This Exists

Office MCP and plugin setups vary a lot by machine. Some users have local Office automation, some have Codex plugins, some have Google Drive integrations, and some only have local file libraries. These skills provide a stable workflow layer:

- Ask the right setup questions.
- Preserve source files.
- Use structured APIs instead of fragile manual edits.
- Render or inspect final artifacts when possible.
- Keep final deliverables separate from scratch files.
- Avoid uploading proprietary MCP or plugin internals.
- Improve Word/DOCX MCP reliability through a clean stdio wrapper.

## Installation

Clone or download this repository, then copy the skill folders into your Codex skills directory.

### Windows PowerShell

```powershell
.\install.ps1
```

Manual install:

```powershell
$dest = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force -Path $dest
Copy-Item -Recurse .\office-* $dest
Copy-Item -Recurse .\ppt-* $dest
```

### macOS or Linux

```bash
./install.sh
```

Manual install:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R office-* ppt-* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation.

## Example Prompts

```text
Use office-document-workflow to create a polished DOCX report from these notes, then verify layout before delivery.
```

```text
Use ppt-presentation-workflow to turn my thesis outline into a 15-slide defense deck with speaker notes.
```

```text
Use office-spreadsheet-workflow to clean this CSV, build an XLSX dashboard, and check formulas before export.
```

```text
Use office-export-qa to inspect this PPTX before I send it to my supervisor.
```

More examples are in [examples/prompts.md](examples/prompts.md).

## What Is Not Included

This repository intentionally does not include:

- OpenAI plugin source code.
- Microsoft Office binaries.
- Proprietary MCP server implementations.
- API keys, credentials, or machine-specific configuration.
- Cached files from `~/.codex/plugins`.

It does include a small original wrapper script and placeholder configuration for Word/DOCX MCP stdio usage.

See [docs/mcp-notes.md](docs/mcp-notes.md) for safe publishing guidance.

## License

MIT License. See [LICENSE](LICENSE).
