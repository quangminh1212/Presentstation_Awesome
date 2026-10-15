# Office-PowerPoint-MCP

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

**Enterprise-Grade PowerPoint Automation Protocol for AI Assistants**

## Overview

**Office-PowerPoint-MCP** is a robust Model Context Protocol (MCP) server designed to enable advanced PowerPoint presentation processing capabilities for AI assistants like **Claude Code**, **Amazon Q Developer**, and other MCP-compliant clients.

It provides a standardized interface for AI agents to programmatically create, read, manipulate, and analyze Microsoft PowerPoint presentations (`.pptx`). By abstracting complex presentation object models into clean API tools, it empowers AI assistants to generate professional presentations, reports, and visual documentation workflows autonomously.

### Key Benefits

- **Seamless Integration**: Optimized for Claude Code and Amazon Q environments
- **Rich Formatting**: Support for complex layouts, animations, and design controls
- **Enterprise Ready**: Includes template management, media handling, and professional styling
- **Secure**: Runs locally with explicit permission controls

## Features

### 1. Presentation Management

- **Lifecycle Control**: Create, copy, merge, and convert presentations (to PDF)
- **Structure Analysis**: Extract slide content, metadata, and statistics
- **Template System**: Apply and manage custom presentation templates

### 2. Content Engineering

- **Advanced Layouts**: Create complex slide layouts with multiple content areas
- **Rich Media**: Insert images, videos, charts, and tables with precise positioning
- **Dynamic Text**: Precision control over fonts, colors, and paragraph styles
- **Interactive Elements**: Add animations, transitions, and hyperlinks

### 3. Design & Styling

- **Theme Management**: Apply and customize presentation themes
- **Master Slides**: Create and modify slide masters for consistent branding
- **Color Schemes**: Implement corporate color palettes and design systems

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `uv` (recommended) or `pip` package manager
- Microsoft PowerPoint (for advanced features)

### Installation

#### Option 1: Using `uvx` (Recommended for ephemeral use)

No installation required. You can run the server directly using `uvx`.

```bash
uvx --from office-powerpoint-mcp-server ppt_mcp_server
```

#### Option 2: Local Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ihatesea69/Office-PowerPoint-MCP.git
cd Office-PowerPoint-MCP
pip install -r requirements.txt
```

## Integration Guide

### Claude Code

Add the following to your Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "powerpoint-server": {
      "command": "uvx",
      "args": ["--from", "office-powerpoint-mcp-server", "ppt_mcp_server"]
    }
  }
}
```

### Amazon Q Developer (VS Code / JetBrains)

To integrate Office-PowerPoint-MCP with Amazon Q Developer:

1. Open your IDE settings and navigate to **Amazon Q** > **MCP Servers**
2. Add a new server configuration:
   - **Name**: `powerpoint-automation`
   - **Command**: `uvx`
   - **Args**: `--from`, `office-powerpoint-mcp-server`, `ppt_mcp_server`
3. Restart your IDE. Amazon Q will now have access to PowerPoint tools

### Other MCP Clients

Add the following to your MCP configuration file:

```json
{
  "mcpServers": {
    "ppt": {
      "command": "uvx",
      "args": ["--from", "office-powerpoint-mcp-server", "ppt_mcp_server"]
    }
  }
}
```

## API Reference

The server exposes the following tools to the AI assistant.

### Core Operations

| Tool Name                        | Description                                      |
| -------------------------------- | ------------------------------------------------ |
| `create_presentation`            | Create a new blank or template-based presentation |
| `get_presentation_info`          | Extract metadata and structure information        |
| `list_available_presentations`   | Scan directory for valid PowerPoint files        |
| `convert_to_pdf`                | Export .pptx to PDF format                       |

### Content & Formatting

| Tool Name          | Description                                    |
| ------------------ | ---------------------------------------------- |
| `add_slide`        | Insert new slides with specified layouts       |
| `add_text_box`     | Add formatted text boxes to slides            |
| `add_image`        | Insert images with positioning and scaling     |
| `add_table`        | Create structured tables on slides             |
| `add_chart`        | Generate charts and graphs                     |

### Design Management

| Tool Name              | Description                                  |
| ---------------------- | -------------------------------------------- |
| `apply_theme`          | Apply predefined or custom themes           |
| `set_slide_layout`     | Change slide layouts and master templates    |
| `format_text`          | Apply advanced text formatting options       |
| `add_animation`        | Create slide transitions and animations      |

## Example Usage

```python
# Example: Create a business presentation
presentation = create_presentation("Business Report Q4 2024")
add_slide(presentation, "title_slide", title="Q4 Results", subtitle="Company Performance Review")
add_slide(presentation, "content_slide", title="Key Metrics")
add_chart(presentation, slide_index=1, chart_type="bar", data=sales_data)
apply_theme(presentation, "corporate_blue")
save_presentation(presentation, "Q4_Report.pptx")
```

## Troubleshooting

### Common Issues

**Permission Denied**
- **Cause**: The server cannot access the file system
- **Fix**: Ensure the running process has R/W access to the target directory. On Windows, ensure the file isn't open in Microsoft PowerPoint

**Template Not Found**
- **Cause**: Using a template that doesn't exist in the system
- **Fix**: Use `list_available_templates` to see available options, or provide full path to custom templates

**Image Insertion Failures**
- **Cause**: Relative paths may be ambiguous
- **Fix**: Always use **absolute paths** for images

### Debugging

Set the `MCP_DEBUG` environment variable to `1` to enable verbose logging:

```bash
# Windows (PowerShell)
$env:MCP_DEBUG = "1"

# Linux/Mac
export MCP_DEBUG=1
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Roadmap

- [ ] Advanced animation support
- [ ] Integration with online template libraries
- [ ] Collaborative editing features
- [ ] AI-powered design suggestions
- [ ] Support for PowerPoint Online/Office 365

---

_Built for the AI-Powered Productivity Era._