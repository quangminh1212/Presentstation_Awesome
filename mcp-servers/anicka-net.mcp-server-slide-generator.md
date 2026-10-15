# mcp-server-slide-generator

An [MCP](https://modelcontextprotocol.io/) server that generates PowerPoint presentations with auto-generated charts from Excel data. Works with any MCP-compatible host ([mcphost](https://github.com/mark3labs/mcphost), Claude Desktop, etc.).

The model provides slide titles and bullet points in a simple text format. The tool handles all chart creation, column matching, data pivoting, and styling automatically.

## Tools

| Tool | Description |
|------|-------------|
| `create_presentation` | Create a PPTX with auto-generated charts from an Excel data file |

## How it works

The model doesn't need to construct complex chart specifications. It just writes:

```
SLIDE: Revenue Overview
BULLET: Total revenue grew 21% to €457M
BULLET: Americas led growth at 36%
CHART: Revenue

SLIDE: Subscription Trends
BULLET: Subscriptions up 24% across all regions
CHART: Subscriptions

SLIDE: Recommendations
BULLET: Expand Americas sales team
BULLET: Investigate APAC Q2 dip
```

The tool reads the referenced Excel file, auto-detects time columns and grouping columns, and creates multi-series charts with appropriate chart types (column charts for time series, bar charts for categories).

## Installation

```bash
pip install .
```

Or in a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```

An RPM package is available on [OBS](https://build.opensuse.org/package/show/home:anicka/mcp-server-slide-generator) for openSUSE Tumbleweed and SLE 16.

## Usage

### With mcphost

Add to your `mcphost.yml`:

```yaml
mcpServers:
  slide-generator:
    command: mcp-slide-generator
```

Typically used together with [mcp-server-excel-reader](https://github.com/anicka-net/mcp-server-excel-reader):

```yaml
mcpServers:
  excel-reader:
    command: mcp-excel-reader
  slide-generator:
    command: mcp-slide-generator
```

### With Claude Desktop

Add to your Claude Desktop config:

```json
{
  "mcpServers": {
    "slide-generator": {
      "command": "mcp-slide-generator"
    }
  }
}
```

### Standalone

```bash
mcp-slide-generator
```

The server communicates over stdio using the MCP protocol.

## Dependencies

- Python >= 3.11
- [mcp](https://pypi.org/project/mcp/) (MCP Python SDK)
- [python-pptx](https://pypi.org/project/python-pptx/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/)

## License

MIT
