# pptx-mcp — Local PowerPoint MCP Server for Claude

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-1.27.0-blueviolet)](https://modelcontextprotocol.io/)

A **fully-auditable, locally-hosted MCP server** that lets Claude create, edit, and export Microsoft PowerPoint presentations on your Windows machine — with full support for **SAP corporate templates**.

Built by Brijesh Shetty. Zero telemetry. No external network calls. All 24 tools visible in a single Python file.

---

## What It Does

| Category | Tools |
|---|---|
| **Presentation** | `create_presentation`, `open_presentation`, `save_presentation`, `close_presentation`, `list_open_presentations`, `get_presentation_info` |
| **SAP Template** | `create_sap_presentation`, `add_sap_cover_slide`, `add_sap_divider_slide`, `add_sap_content_slide` |
| **Slides** | `add_slide`, `delete_slide`, `list_slides`, `get_slide_info` |
| **Content** | `add_text_box`, `add_title_content`, `add_table`, `add_image`, `add_shape` |
| **Formatting** | `set_slide_background`, `set_text_style` |
| **COM (Windows)** | `launch_powerpoint`, `export_pdf`, `export_slide_images` |

---

## Prerequisites

| Requirement | Notes |
|---|---|
| Windows 10/11 | COM automation requires Windows |
| Python 3.10+ | Tested on Python 3.14 |
| Microsoft PowerPoint | Required for `launch_powerpoint`, `export_pdf`, `export_slide_images` |
| Claude Desktop | To use as an MCP server in conversation |

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/brijeshshetty/pptx-mcp.git
cd pptx-mcp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

All four dependencies are **pinned** for reproducibility:

```
mcp==1.27.0
python-pptx==1.0.2
Pillow==12.3.0
pywin32==311
```

### 3. Verify the install

```bash
python -c "from pptx_mcp_server import mcp; print('Tools:', len(mcp._tool_manager._tools))"
# Expected: Tools: 24
```

### 4. Connect to Claude Desktop

Open (or create) your Claude Desktop config file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the `powerpoint` entry:

```json
{
  "mcpServers": {
    "powerpoint": {
      "command": "C:\\Path\\To\\Python\\python.exe",
      "args": [
        "C:\\Path\\To\\pptx-mcp\\pptx_mcp_server.py"
      ]
    }
  }
}
```

Replace both paths with your actual Python executable and clone location.

### 5. Restart Claude Desktop

Quit completely and reopen. You should see **PowerPoint MCP** in the tools panel (hammer icon).

---

## SAP Corporate Template Support

If you have an SAP `.pptx` file with the official slide master (e.g. a DRC setup guidance deck), place its path in the `_SAP_TEMPLATE` constant at the top of `pptx_mcp_server.py`:

```python
# Line ~860 in pptx_mcp_server.py
_SAP_TEMPLATE = r"C:\Path\To\Your\SAP_Template.pptx"
```

This unlocks four extra tools that inherit **all 40 SAP layouts** including:

- `Cover A` — dark blue right panel with chevron graphic
- `Divider Page C` — white top / blue-chevron bottom
- `Title and Text: 2 Columns` — standard content
- `Q & A`, `Thank You A`, `Agenda A/B`, and more

Example prompt to Claude after connecting:

> *"Create an SAP-branded presentation at C:/Users/me/Documents/France_DRC.pptx.
> Add a cover slide titled 'France B2B E-Invoicing — Setup Guidance'.
> Add a divider slide 'Introduction and Latest Status'.
> Add a two-column content slide with the e-invoicing scope on the left and e-reporting scope on the right.
> Save it."*

---

## Example Prompts

### Basic deck

> *"Create a new presentation at C:/Users/me/Documents/MyDeck.pptx.
> Add a slide with a dark blue background. Add a white title 'Hello World'.
> Add a table with 3 columns and 4 rows of sample data. Save it."*

### Export to PDF

> *"Open C:/Users/me/Documents/MyDeck.pptx as 'deck'. Export it as a PDF to C:/Users/me/Documents/MyDeck.pdf."*

### Export slides as images

> *"Open MyDeck.pptx as 'deck'. Export all slides as 1920x1080 PNG images to C:/Users/me/Desktop/slides/."*

---

## Security Model

This server is designed to be **fully auditable**:

- **No external network calls** — verified by source inspection (no `requests`, `urllib`, `socket`, `subprocess`, `eval`, or `exec` in the server code)
- **Path traversal protection** — all file paths are validated against an allowlist (home directory + temp dir)
- **Pinned dependencies** — four packages, all pinned to specific versions
- **Single file** — the entire server is `pptx_mcp_server.py` (~900 lines)

The COM tools (`launch_powerpoint`, `export_pdf`, `export_slide_images`) require Microsoft PowerPoint to be installed and run within your user session — they do not spawn processes with elevated privileges.

---

## Project Structure

```
pptx-mcp/
  pptx_mcp_server.py          # The complete MCP server (24 tools)
  requirements.txt            # 4 pinned dependencies
  claude_desktop_config_snippet.json   # Paste into Claude Desktop config
  build_test_deck.py          # Demo: builds a 5-slide test deck
  build_sap_branded.py        # Demo: builds a 10-slide SAP-branded deck
  gen_sap_pattern.py          # Utility: generates SAP chevron background PNGs
  SETUP.md                    # Detailed setup notes
```

---

## Running the Demos

```bash
# Build a plain 5-slide test deck (no template required)
python build_test_deck.py

# Build a 10-slide SAP-branded deck (requires _SAP_TEMPLATE to be set)
python build_sap_branded.py
```

---

## Shapes Supported by `add_shape`

`rectangle`, `rounded_rectangle`, `oval`, `diamond`, `right_arrow`,
`chevron`, `pentagon`, `hexagon`, `parallelogram`, `triangle`

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Tools: 20` instead of `24` | The SAP template constant `_SAP_TEMPLATE` points to a missing file. Set it to a valid `.pptx` path. |
| `COM automation requires Windows` | Install Microsoft PowerPoint. COM tools only work on Windows with PPT installed. |
| `Path is outside allowed directories` | Move your target file to your home folder (`C:\Users\<you>\`) or Documents subfolder. |
| Claude Desktop doesn't show the server | Check the JSON syntax in `claude_desktop_config.json`, verify both paths, and fully restart Claude Desktop (not just close the window). |
| `UserWarning: Duplicate name` on save | Harmless warning from python-pptx 1.x when overwriting an existing file. Output is valid. |

---

## Changelog

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | July 2026 | Initial release — 20 core tools |
| 1.1.0 | July 2026 | +4 SAP template tools; `create_sap_presentation`, `add_sap_*` |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Contributing

Issues and PRs welcome. If you add support for a new corporate template (KSA, India, etc.), follow the same pattern as the SAP tools: extract the slide master from the reference `.pptx` and expose layout-aware `add_*_slide` helpers.
