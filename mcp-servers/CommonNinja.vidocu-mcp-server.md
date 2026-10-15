# Vidocu MCP Server

> The AI Knowledge Platform as MCP tools. Agents turn videos, PDFs, and slides into
> subtitles, voiceovers, translations, docs, and help articles. Free plan works.

Vidocu is the AI Knowledge Platform for teams that move fast: it turns the materials
you have into the knowledge people need. Product videos, SOPs, how-to guides, help
articles, and training material from one upload.

This is the hosted [Model Context Protocol](https://modelcontextprotocol.io) server
that gives AI agents (Claude, Cursor, Windsurf, and any MCP-aware client) the full
Vidocu API as tools: upload a video or connect source material, generate subtitles
in 65+ languages, add AI voiceover, translate the whole asset, and produce
step-by-step documentation with screenshots, all from conversation. Heavy operations
run async with job polling, so agents can fire work and check back. Hosted and
stateless: nothing to deploy.

## Endpoint

```
https://mcp.vidocu.ai/
```

Remote, streamable HTTP.

## Auth

**OAuth 2.1 (recommended, works on any plan including Free).** The server
advertises Vidocu's authorization server via RFC 9728 protected-resource metadata,
with PKCE and dynamic client registration. Clients that support OAuth connect with
no manual key management, and an agent can produce real output without a credit
card.

**API key.** For clients without OAuth support, pass a Vidocu API key
(`vdo_live_...`) as a Bearer token, available on every plan. Mint one at
<https://vidocu.ai/dashboard/developers>.

## Install

Claude Code / CLI (OAuth):

```bash
claude mcp add --transport http vidocu https://mcp.vidocu.ai/
```

Claude Desktop / Cursor / Windsurf (OAuth, any HTTP-transport client):

```json
{
  "mcpServers": {
    "vidocu": {
      "url": "https://mcp.vidocu.ai/"
    }
  }
}
```

API key variant:

```json
{
  "mcpServers": {
    "vidocu": {
      "url": "https://mcp.vidocu.ai/",
      "headers": { "Authorization": "Bearer vdo_live_YOUR_KEY" }
    }
  }
}
```

## Tools (145)

The server exposes the whole Vidocu platform. Grouped by area:

- **Videos and projects** - upload, list, rename, move and delete videos; project folders
- **Processing** - `process_video` (analyze, voiceover, article, export and translate in one call), plus each step on its own, subtitles, scripts and download links
- **AI Recorder** - `start_recording` describes a flow in plain words and an AI agent drives a real browser to record it. When a login asks for a one-time code, the agent pauses and `answer_recording_prompt` passes on the code you give it. Needs a paid plan.
- **Knowledge Center** - sections, articles, publishing a video's article, translation, `ask_knowledge_base` (answers with citations), redirects, analytics and offline exports
- **Courses and training** - courses built from documents, storyboards, generated modules, quizzes, attempts, sign-offs, deadlines and `training_planner`
- **Studio and Remix** - multi-track Studio projects and templates; Remix shorts, blog and social copy from a long video
- **Voices, avatars and brand kit** - voices, AI avatars, brand kit defaults, pronunciations, glossary, brand skills and brand assets
- **Approvals, locks and comments** - request and decide approvals, lock a video through a review, review comments
- **Micro-tools** - `list_tools`, `get_tool`, `execute_tool` (Vidocu's free video tools, programmatically)
- **Jobs, usage and webhooks** - job status, usage, `get_credit_costs` to price work before starting it, webhook subscriptions

The full list with a line on each tool is in the [MCP documentation](https://vidocu.ai/docs/mcp).

## Pricing

The MCP server works on **every Vidocu plan**, with OAuth or an API key, including
the Free plan (no credit card). Plans at <https://vidocu.ai/pricing>.

## Links

- Product: <https://vidocu.ai>
- MCP page: <https://vidocu.ai/features/mcp>
- MCP docs: <https://vidocu.ai/docs/mcp>
- API docs: <https://vidocu.ai/docs>
- Developers: <https://vidocu.ai/developers>
- Registry: `ai.vidocu/vidocu` on <https://registry.modelcontextprotocol.io>
