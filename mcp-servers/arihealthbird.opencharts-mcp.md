<p align="center">
  <a href="https://www.opencharts.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://www.opencharts.com/brand-v3/emblem/emblem-neon.png" />
      <img src="https://www.opencharts.com/brand-v3/emblem/emblem-black.png" alt="OpenCharts" width="84" />
    </picture>
  </a>
</p>

<h1 align="center">OpenCharts MCP Server</h1>

<p align="center">
  Build flowcharts, notes, slides, sheets, boards, sites, agents, songs, images &amp; video in <a href="https://www.opencharts.com">OpenCharts</a> — straight from your AI client.
</p>

<p align="center">
  <a href="https://www.opencharts.com">Website</a> ·
  <a href="https://www.opencharts.com/help/mcp-server">Documentation</a> ·
  <a href="https://www.opencharts.com/theo-agents/mcp">Get an API key</a> ·
  <a href="https://github.com/arihealthbird/opencharts-mcp/issues">Issues</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC--BY--4.0-blue" alt="License" /></a>
  <a href="https://www.opencharts.com"><img src="https://img.shields.io/badge/website-opencharts.com-brightgreen" alt="Website" /></a>
  <a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/protocol-MCP-purple" alt="MCP" /></a>
</p>

---

## What is this?

[OpenCharts](https://www.opencharts.com) runs a **public, hosted [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server** that puts the whole OpenCharts product inside any MCP-compatible AI client. Connect once with an API key and your assistant can build and manage real OpenCharts projects on your behalf — flowcharts, whiteboards, notes, presentations, spreadsheets (Theo Sheets), Kanban + calendar boards, full websites & apps (Code Canvas), automations (Theo Agents), songs (Theo Symphony), and images & video (Theo Media) — all powered by Theo, the OpenCharts AI. When building a site or app, your assistant can generate real imagery and video clips inline and drop the returned URLs straight into the code instead of leaving placeholders.

It is a **remote server over Streamable HTTP** — there is nothing to install or run locally. Point your client at the endpoint, paste your API key, and go.

This repository is the public documentation for that server. The server itself is hosted by OpenCharts; you don't run it yourself.

> Want to connect in under a minute? Use the in-app guide at **[opencharts.com/help/mcp-server](https://www.opencharts.com/help/mcp-server)** or the setup page at **[opencharts.com/theo-agents/mcp](https://www.opencharts.com/theo-agents/mcp)**.

## Quick start

1. **Create an API key** at [opencharts.com/theo-agents/mcp](https://www.opencharts.com/theo-agents/mcp). Copy it immediately — the full key is shown only once.
2. **Add the server** to your AI client using the matching [config snippet below](#connect-your-ai-client), replacing `{{YOUR_API_KEY}}` with your key.
3. **Verify** the connection by asking your assistant to call the `whoami` tool — it should return your OpenCharts account.

## Endpoint

```
https://www.opencharts.com/api/mcp
```

- **Transport:** Streamable HTTP (`POST`)
- **Auth:** `Authorization: Bearer <API key>` (a JWT from an active OpenCharts session also works)

> ⚠️ **Always use the `www.` host.** The apex `opencharts.com` issues a 307 redirect that strips the `Authorization` header and breaks authentication. Use `https://www.opencharts.com/api/mcp` exactly.

## Connect your AI client

The server works with any MCP-compatible client. Copy the matching snippet and swap in your API key. Prefer to let your assistant wire it up? The [help page](https://www.opencharts.com/help/mcp-server) has a one-paste "AI setup prompt" for every client below.

### Warp

```json
{
  "mcpServers": {
    "opencharts": {
      "type": "http",
      "url": "https://www.opencharts.com/api/mcp",
      "headers": {
        "Authorization": "Bearer {{YOUR_API_KEY}}"
      }
    }
  }
}
```

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "opencharts": {
      "type": "streamable-http",
      "url": "https://www.opencharts.com/api/mcp",
      "headers": {
        "Authorization": "Bearer {{YOUR_API_KEY}}"
      }
    }
  }
}
```

### Cursor

```json
{
  "mcpServers": {
    "opencharts": {
      "url": "https://www.opencharts.com/api/mcp",
      "headers": {
        "Authorization": "Bearer {{YOUR_API_KEY}}"
      }
    }
  }
}
```

### VS Code (GitHub Copilot)

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "opencharts": {
      "type": "http",
      "url": "https://www.opencharts.com/api/mcp",
      "headers": {
        "Authorization": "Bearer ${input:opencharts-key}"
      }
    }
  },
  "inputs": [
    {
      "id": "opencharts-key",
      "type": "promptString",
      "description": "OpenCharts API key",
      "password": true
    }
  ]
}
```

### Windsurf (Codeium)

```json
{
  "mcpServers": {
    "opencharts": {
      "serverUrl": "https://www.opencharts.com/api/mcp",
      "headers": {
        "Authorization": "Bearer {{YOUR_API_KEY}}"
      }
    }
  }
}
```

### Claude Code (CLI)

```bash
claude mcp add --transport http opencharts https://www.opencharts.com/api/mcp --header "Authorization: Bearer {{YOUR_API_KEY}}"
```

### Codex (OpenAI)

```bash
codex mcp add opencharts --url https://www.opencharts.com/api/mcp --header "Authorization: Bearer {{YOUR_API_KEY}}"
```

### Amp

In the VS Code extension `settings.json`:

```json
"amp.mcpServers": {
  "opencharts": {
    "url": "https://www.opencharts.com/api/mcp",
    "headers": {
      "Authorization": "Bearer {{YOUR_API_KEY}}"
    }
  }
}
```

### OpenCode

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "opencharts": {
      "type": "remote",
      "url": "https://www.opencharts.com/api/mcp",
      "oauth": false,
      "headers": {
        "Authorization": "Bearer {{YOUR_API_KEY}}"
      }
    }
  }
}
```

## Tools

The server exposes **59 tools** across 11 groups. Tools that use Theo AI or generation consume AI credits.

### Projects

| Tool | Description |
|------|-------------|
| `list_projects` | List your projects with pagination and filters |
| `get_project` | Get full project data by ID |
| `create_flowchart` | Create a flowchart project with nodes and edges |
| `create_whiteboard` | Create a whiteboard with native shapes and elements |
| `create_notes` | Create a notes project from Markdown |
| `create_presentation` | Create a slide deck from an outline |
| `update_project` | Update metadata or content (notes, flowchart, whiteboard, or presentation) |
| `delete_project` | Soft-delete a project (30-day recovery) |

### Code Canvas

| Tool | Description |
|------|-------------|
| `generate_code_canvas` | Build a full website or app (HTML/React) from a description — returns a job to poll |
| `get_code_canvas_status` | Poll a Code Canvas build; returns the project + open URL when ready |

### AI

| Tool | Description |
|------|-------------|
| `ask_theo` | Send a single-turn AI message (fast or think mode) |
| `extract_flowchart` | Extract a flowchart from an uploaded document (PDF, image, PPTX) |

### Theo Agents

| Tool | Description |
|------|-------------|
| `build_agent` | Build a Theo Agent from a description — runs in the background, notifies you when ready |
| `get_agent_build_status` | Optional poll for a `build_agent` job; returns the agent + open URL when done |
| `create_agent` | Create a Theo Agent deterministically from structured steps + trigger |
| `update_agent` | Patch an agent's name, description, or step list |
| `configure_agent_trigger` | Set an agent's trigger (manual, schedule, webhook, event, telegram) |
| `activate_agent` | Activate an agent (seeds the first scheduled run) |
| `deactivate_agent` | Deactivate an agent so triggers stop firing |
| `delete_agent` | Soft-delete an agent (30-day recovery) |
| `list_agents` | List your Theo Agents with status + step counts |
| `get_agent` | Get an agent's full definition (trigger + ordered steps) |
| `run_agent` | Dispatch an agent now — runs in the background, notifies you on completion |
| `list_agent_runs` | List an agent's recent execution runs |
| `get_agent_run_status` | Get a single run's status + per-node progress |

### Theo Sheets

| Tool | Description |
|------|-------------|
| `list_sheets` | List your Theo Sheets spreadsheet projects |
| `inspect_sheet` | Inspect a sheet — per-tab dimensions, header row, sampled cells + formulas, layout |
| `get_sheet` | Extract a worksheet as structured rows (headers + data rows) |
| `read_sheet_range` | Read an exact A1 range's values (+ optional formulas) as a grid + CSV |
| `create_sheet` | Create a live spreadsheet (Excel-grade grid + formulas) from headers and rows |
| `update_sheet` | Edit a sheet by applying structured spreadsheet edit ops — saved as a rollback-able commit |
| `apply_sheet_ops` | Apply structured spreadsheet edit ops — or propose a merge-gated change |
| `edit_sheet` | Edit a sheet with a natural-language instruction (Theo plans + applies ops) |
| `list_sheet_commits` | List a sheet's git-style change commits (applied / proposed / merged) |
| `diff_sheet_commit` | Show the cell-level diff for a commit or proposal |
| `resolve_sheet_proposal` | Merge or reject a pending change proposal |
| `rollback_sheet` | Roll the live sheet back to a prior commit (reversible) |

### Boards

| Tool | Description |
|------|-------------|
| `create_board` | Create a Kanban + calendar project board |
| `list_boards` | List your project boards |
| `get_board` | Get a board's lists (columns) and cards |
| `update_board` | Update a board's name, description, or list columns |
| `delete_board` | Soft-delete a board (recoverable) |
| `duplicate_board` | Duplicate a board with its lists, rules, and cards |
| `add_board_card` | Add a card (post/task/idea/event) to a board |
| `list_board_cards` | List a board's cards, optionally by schedule range |
| `update_board_card` | Edit a card — move list, reschedule, change status/color |
| `delete_board_card` | Soft-delete a card from a board |

### Theo Symphony

| Tool | Description |
|------|-------------|
| `create_song` | Generate a song with Theo Symphony — returns a job to poll |
| `get_song_status` | Poll a song job; returns audio + cover-art versions when complete |

### Theo Media

| Tool | Description |
|------|-------------|
| `generate_image` | Generate an image from a prompt — returns a public URL to embed or save (use instead of placeholders) |
| `generate_video` | Generate a short video clip from a prompt — returns a job to poll |
| `get_video_status` | Poll a video job; returns the finished clip URL when complete |

### Notes

| Tool | Description |
|------|-------------|
| `get_note_content` | Extract a note's content as Markdown |
| `append_to_note` | Append Markdown content to an existing note |
| `clip_to_note` | Save web content (URL + HTML) as a clip inside a note |

### Templates

| Tool | Description |
|------|-------------|
| `list_templates` | Browse the template gallery |
| `use_template` | Create a new project from a template |

### Account

| Tool | Description |
|------|-------------|
| `whoami` | Get the authenticated user's profile information |
| `get_credits` | Check remaining AI credit balance |

## Resources

Resources provide read-only context an AI client can retrieve without calling a tool.

| Resource | Description |
|----------|-------------|
| `projects` | Paginated list of your recent projects |
| `project` | Full data for a single project by ID |
| `templates` | Browsable template catalog |

## How it works

```
┌────────────────────┐   Streamable HTTP    ┌────────────────────────────┐
│   Your AI client    │   + Bearer API key   │   OpenCharts MCP (hosted)  │
│  Warp · Claude ·    │ ───────────────────► │                            │
│  Cursor · VS Code · │                      │  Projects · Code Canvas ·  │
│  Windsurf · Codex · │ ◄─────────────────── │  Agents · Sheets · Boards ·│
│  Amp · OpenCode     │      tool results    │  Symphony · Notes · AI     │
└────────────────────┘                      └────────────────────────────┘
```

Every request is authenticated by your API key and acts on your own OpenCharts account. Because the server is hosted, the tool surface stays current automatically — no client updates required. Tools that use Theo AI or generation (for example `ask_theo`, `extract_flowchart`, `generate_code_canvas`, `build_agent`, `create_song`, `generate_image`, `generate_video`) consume AI credits from your plan.

## Rate limits & credits

- **120 requests per minute** per user.
- AI and generation tools consume **AI credits** — check your balance any time with the `get_credits` tool.

## Discovery & registry

Machine-readable metadata is published for clients, crawlers, and registries (no secrets):

- `https://www.opencharts.com/.well-known/mcp` — discovery manifest
- `https://www.opencharts.com/.well-known/mcp/server-card.json` — server card
- `https://www.opencharts.com/.well-known/oauth-protected-resource` — protected-resource metadata
- Docs: [opencharts.com/help/mcp-server](https://www.opencharts.com/help/mcp-server)

## Troubleshooting

- **`307` redirect / "no authorization support" / `401`** — make sure the URL is exactly `https://www.opencharts.com/api/mcp` (with `www.`). The apex host strips the `Authorization` header on redirect. Also confirm your key is active and sent with the `Bearer ` prefix.
- **`429 Too Many Requests`** — you've hit the 120 req/min limit; wait and retry.
- **Tools missing in your client** — fully restart the client (or toggle the OpenCharts server off/on) so it re-fetches the tool list. Confirm your key carries the `read`, `write`, and `ai` scopes (default keys include all three).
- **JWT expired mid-session** — session JWTs expire after ~15 minutes; use a persistent API key for long-running integrations.

## Compatible clients

Works with any client that supports the [Model Context Protocol](https://modelcontextprotocol.io), including:

- [Warp](https://www.warp.dev) — agentic development environment
- [Claude Desktop](https://claude.ai) & [Claude Code](https://www.anthropic.com)
- [Cursor](https://www.cursor.com)
- [VS Code](https://code.visualstudio.com) (GitHub Copilot)
- [Windsurf](https://windsurf.com) (Codeium)
- [Codex](https://openai.com) (OpenAI)
- Amp
- [OpenCode](https://opencode.ai)

## Links

- 🌐 **Website**: [opencharts.com](https://www.opencharts.com)
- 📖 **MCP docs**: [opencharts.com/help/mcp-server](https://www.opencharts.com/help/mcp-server)
- 🔑 **Get an API key**: [opencharts.com/theo-agents/mcp](https://www.opencharts.com/theo-agents/mcp)
- 💬 **Community**: [opencharts.com/community](https://www.opencharts.com/community)
- 🐛 **Issues**: [GitHub Issues](https://github.com/arihealthbird/opencharts-mcp/issues)

## License

This documentation is licensed under [CC-BY-4.0](LICENSE). The OpenCharts MCP server is a hosted product — see [opencharts.com](https://www.opencharts.com) for terms and pricing.
