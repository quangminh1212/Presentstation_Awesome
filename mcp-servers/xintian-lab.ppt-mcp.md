# PPT-MCP

Cross-platform [Model Context Protocol](https://modelcontextprotocol.io) server for Microsoft PowerPoint automation. Tool names and parameters align with [powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp) for cross-platform agent compatibility.

## Platforms

| Platform | Backend | Capabilities |
|----------|---------|--------------|
| **Windows** | pywin32 COM | Full: screenshots, HTML/LaTeX, plots, animations, evaluate |
| **macOS** | AppleScript + python-pptx | Open/save/navigate via app; file edits via python-pptx |

## Requirements

- Python 3.10+
- Microsoft PowerPoint installed
- **macOS**: grant Automation permission for Cursor/terminal in System Settings → Privacy & Security → Automation
- **Windows**: `pip install -e ".[windows]"` and run `pywin32_postinstall.py -install`

## Install

```bash
cd /Users/xintian/Desktop/PPT-MCP
python3 -m pip install -e .
# Windows only:
python3 -m pip install -e ".[windows]"
```

## Cursor integration

Add to `~/.cursor/mcp.json` or use the project config at [`.cursor/mcp.json`](.cursor/mcp.json):

```json
{
  "mcpServers": {
    "ppt-mcp": {
      "command": "python3",
      "args": ["-m", "ppt_mcp"],
      "cwd": "/path/to/PPT-MCP"
    }
  }
}
```

Restart Cursor after configuration.

## Tools (12)

| Tool | Windows | macOS |
|------|---------|-------|
| `manage_presentation` | Full | Full (AppleScript) |
| `slide_snapshot` | Text + screenshot | Text only |
| `switch_slide` | COM | AppleScript |
| `add_speaker_notes` | COM | python-pptx |
| `populate_placeholder` | HTML/LaTeX/plot | Plain text |
| `manage_slide` | COM | python-pptx |
| `list_templates` | Win dirs | macOS dirs |
| `analyze_template` | COM + screenshots | python-pptx |
| `add_slide_with_layout` | COM | python-pptx |
| `add_animation` | COM | Not supported |
| `evaluate` | Python eval | Guidance only |
| **`remap_to_template`** | **Yes** | **Yes** |

## Workspace (remap workflow)

Use the [`workspace/`](workspace/) folder for remap jobs:

```
workspace/input/old/          ← your old .pptx
workspace/input/templates/    ← your .potx / .pptx templates
workspace/output/             ← remapped results
```

See [workspace/README.md](workspace/README.md) for usage.

## Development

```bash
python3 -m ppt_mcp          # run MCP server (stdio)
python3 -c "from ppt_mcp.backends.factory import get_backend; print(type(get_backend()).__name__)"
```

## References

- Windows COM tools adapted from [powerpoint-mcp](https://github.com/Ayushmaniar/powerpoint-mcp) (MIT)
- macOS backends adapted from [macpoint](https://github.com/AndrewIgdal17/macpoint) (MIT)
