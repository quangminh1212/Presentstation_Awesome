# MCP Introduction Presentation

An introduction presentation about Model Context Protocol (MCP) with a working example server.

## Contents

- **mcp_introduction.md** - Beamer presentation about MCP (convert to PDF with pandoc)
- **example_mcp_server.py** - Working Notes Manager MCP server in Python
- **README_MCP_SERVER.md** - Detailed documentation for the example server

## Quick Start

### Generate PDF Presentation

```bash
pandoc mcp_introduction.md -t beamer -o mcp_introduction.pdf
```

### Run the MCP Server

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python example_mcp_server.py
```

### Use with Claude Desktop

The server is already configured in `~/.config/Claude/claude_desktop_config.json`

### Use with Claude Code

The server is configured in `.mcp.json` for this project.

## About

**Author:** Barbaros Goren
**Company:** Bidnamic

## MCP Server Features

The Notes Manager server demonstrates:
- **Resources**: Read notes and statistics
- **Tools**: Create, search, update, and delete notes
- **Prompts**: Summarize notes, weekly reviews, brainstorming

Notes are stored in `notes_data/` directory.
