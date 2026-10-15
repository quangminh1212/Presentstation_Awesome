# PPTX MCP Server

An MCP server that creates PowerPoint presentations with automatic image lookup using [PptxGenJS](https://gitbrent.github.io/PptxGenJS/).

## Installation

```bash
npm install
chmod +x index.js
```

## Setup

1. **Create output directory:**
   ```bash
   mkdir -p /tmp/pptx
   ```

2. **Start local file server:**
   ```bash
   cd /tmp/pptx
   python3 -m http.server 8080
   ```
   Keep this running in a separate terminal.

3. **Configure Claude Desktop:**

   Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

   ```json
   {
     "mcpServers": {
       "pptxgenjs": {
         "command": "/path/to/node",
         "args": ["/path/to/pptx-mcp/index.js"],
         "env": {
           "PPTX_OUTPUT_DIR": "/tmp/pptx",
           "PPTX_URL_PREFIX": "http://localhost:8080",
           "UNSPLASH_ACCESS_KEY": "optional_key_for_images"
         }
       }
     }
   }
   ```

   Find your node path with: `which node`

4. **Restart Claude Desktop**

## Usage

Ask Claude to create presentations:
- "Create a presentation about AI with 3 slides"
- "Make a PowerPoint about coffee"

Claude will provide a clickable download URL.

## Optional: Unsplash API Key

For automatic image search, get a free API key at [unsplash.com/developers](https://unsplash.com/developers)