# Google Slides MCP Server

An MCP (Model Context Protocol) server for Google Slides. Enables AI assistants (Claude Code, Cursor, Windsurf, etc.) to create, read, and edit Google Slides presentations directly from chat.

## Features

**39 tools** organized into 4 categories:

### Presentations (4)
| Tool | Description |
|------|-------------|
| `createPresentation` | Create a new presentation |
| `getPresentation` | Get metadata and slide summaries |
| `listPresentations` | Search presentations on Drive |
| `duplicatePresentation` | Copy an entire presentation (template workflow) |

### Slides (10)
| Tool | Description |
|------|-------------|
| `addSlide` | Add a slide with layout (BLANK, TITLE, TITLE_AND_BODY, ...) |
| `deleteSlide` | Delete slide(s) |
| `duplicateSlide` | Duplicate a slide |
| `reorderSlides` | Reorder slides |
| `getSlide` | Get detailed element info for a slide |
| `updateSlideBackground` | Set background color or image |
| `setSpeakerNotes` / `getSpeakerNotes` | Manage speaker notes |
| `copySlideFromPresentation` | Import a slide from another presentation |
| `setSkipSlide` | Show/hide slide in slideshow |

### Elements (25)
| Group | Tools |
|-------|-------|
| **Insert** | insertTextBox, insertImage, insertShape, insertTable, insertVideo, insertLine |
| **Table** | insertTableRow, insertTableColumn, deleteTableRow, deleteTableColumn, updateTableCell, formatTableCell, mergeTableCells, unmergeTableCells |
| **Edit** | updateText, updateTextStyle, updateShapeStyle, setParagraphStyle, moveResizeElement |
| **Other** | deleteElement, groupElements, ungroupElements, replaceAllText, replaceImage, batchUpdate |

### Export (2)
| Tool | Description |
|------|-------------|
| `exportPresentation` | Export to PDF, PPTX, or ODP |
| `getThumbnail` | Get thumbnail image of a slide |

---

## Setup Guide

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select a project** > **New Project**
3. Name your project (e.g., `google-slides-mcp`) > **Create**

### Step 2: Enable APIs

1. Navigate to **APIs & Services** > **Library**
2. Search and **Enable** these 2 APIs:
   - **Google Slides API**
   - **Google Drive API**

### Step 3: Create OAuth Credentials

1. Go to **APIs & Services** > **Credentials**
2. Click **+ CREATE CREDENTIALS** > **OAuth client ID**
3. If you haven't configured the consent screen yet:
   - Click **Configure Consent Screen**
   - Select **External** > **Create**
   - Fill in **App name** (e.g., `Slides MCP`)
   - Add **User support email** and **Developer contact email**
   - Click **Save and Continue** through all steps > **Back to Dashboard**
4. Go back to **Credentials** > **+ CREATE CREDENTIALS** > **OAuth client ID**
5. Application type: **Desktop app**
6. Name it (e.g., `Slides MCP Desktop`)
7. Click **Create**
8. Click **Download JSON** > save as `credentials.json`

### Step 4: Install

```bash
git clone https://github.com/ryanvo162/google-slides-mcp.git
cd google-slides-mcp
npm install
npm run build
```

### Step 5: Authorize

Copy your `credentials.json` (downloaded in Step 3) into the project folder:

```bash
cp /path/to/credentials.json .
```

Run the auth flow:

```bash
node dist/index.js auth
```

A URL will appear in the terminal. Open it in your browser, sign in with your Google account, and grant access. Your token will be saved at `~/.config/google-slides-mcp/token.json`.

> **Note:** If you see "This app isn't verified", click **Advanced** > **Go to Slides MCP (unsafe)**. This is normal for unverified apps.

### Step 6: Configure with Claude Code

Open `~/.claude.json` and add to the `mcpServers` section:

```json
{
  "mcpServers": {
    "google-slides": {
      "command": "node",
      "args": ["/full/path/to/google-slides-mcp/dist/index.js"]
    }
  }
}
```

**Replace `/full/path/to/` with the actual path on your machine.**

macOS example:
```json
"args": ["/Users/username/google-slides-mcp/dist/index.js"]
```

Windows example:
```json
"args": ["C:\\Users\\username\\google-slides-mcp\\dist\\index.js"]
```

Then **restart Claude Code** to load the MCP server.

### Step 7: Test

Open Claude Code and try:

```
Create a new presentation called "Hello World"
```

If Claude creates the presentation and returns a Google Slides link, you're all set!

---

## Other MCP Clients

### Cursor / Windsurf

Add to `.cursor/mcp.json` or `.windsurf/mcp.json`:

```json
{
  "mcpServers": {
    "google-slides": {
      "command": "node",
      "args": ["/path/to/google-slides-mcp/dist/index.js"]
    }
  }
}
```

### Claude Desktop

Add to `claude_desktop_config.json`:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "google-slides": {
      "command": "node",
      "args": ["/path/to/google-slides-mcp/dist/index.js"]
    }
  }
}
```

---

## Environment Variables (optional)

| Variable | Description |
|----------|-------------|
| `GOOGLE_CLIENT_ID` | OAuth client ID (alternative to credentials.json) |
| `GOOGLE_CLIENT_SECRET` | OAuth client secret |
| `SERVICE_ACCOUNT_PATH` | Path to service account key file |
| `GOOGLE_IMPERSONATE_USER` | Email to impersonate (service account only) |
| `GOOGLE_MCP_PROFILE` | Profile name (supports multiple Google accounts) |
| `LOG_LEVEL` | debug, info, warn, error, silent (default: info) |

## Security

- OAuth `state` parameter for CSRF protection
- Token file stored with permission `0600` (owner-only read)
- Client secret not persisted in token file
- Profile name sanitization (prevents path traversal)
- Minimal OAuth scopes: `presentations` + `drive.file`

## Tech Stack

- TypeScript + Node.js (ES2022)
- [FastMCP](https://github.com/jlowin/fastmcp) — MCP server framework
- [googleapis](https://github.com/googleapis/google-api-nodejs-client) — Google APIs client
- [zod](https://github.com/colinhacks/zod) — Schema validation

## Troubleshooting

### "No OAuth credentials found"
Copy `credentials.json` into the project root. See Step 3 and 5.

### "Token might expire"
Run `node dist/index.js auth` again to re-authorize.

### "Google Slides client is not initialized"
Check that `credentials.json` is valid and Google Slides API is enabled (Step 2).

### Claude Code doesn't show the tools
Verify the path in `~/.claude.json` is correct. Restart Claude Code after updating the config.

## License

ISC
