# PPT Depot MCP Server

Connect Claude and other AI assistants to [PPT Depot](https://pptdepot.com), a marketplace of professional PowerPoint templates and individual slides for business presentations.

> This is a **remote, hosted MCP server**. There is nothing to install or run from this repository; it documents the public endpoint.

## Public endpoint

```
https://pptdepot.com/mcp
```

- **Transport:** Streamable HTTP (JSON-RPC 2.0 over POST)
- **Auth:** none. All ten tools are free, read-only, and rate limited.
- **Docs:** https://pptdepot.com/mcp

Every result links back to the page it came from on pptdepot.com.

## Tools

| Tool | What it returns |
|---|---|
| `search_templates` | Keyword search of the PowerPoint template-deck catalog |
| `search_slides` | Keyword search of individual slides across templates |
| `get_template` | Full detail for one template deck: slides, tags, previews, pricing |
| `get_slide` | Full detail for one slide: overview, tags, parent template, related slides |
| `list_templates` | Browse the template catalog by category |
| `list_tags` | Management topics and frameworks used to tag slides |
| `get_tag` | The templates and slides filed under one tag |
| `list_free_templates` | Free PowerPoint downloads (country/regional maps and sample packs) |
| `get_pricing` | Single-template price and the subscription plans |
| `get_image` | A template or slide preview image, returned inline |

## Connect from Claude Code

```
claude mcp add --transport http ppt-depot https://pptdepot.com/mcp
```

Any MCP client that supports HTTP transport works the same way.

## About

PPT Depot sells professional PowerPoint templates and slides for consultants and business teams. Browse and preview for free; download with a subscription or a single purchase at [pptdepot.com](https://pptdepot.com).

Questions: support@pptdepot.com
