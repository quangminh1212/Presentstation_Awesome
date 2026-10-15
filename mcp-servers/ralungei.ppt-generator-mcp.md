# ppt-generator-mcp

MCP server for generating PowerPoint presentations, exposed over HTTP (JSON-RPC). Decks can be AI-generated from a topic or built slide-by-slide, rendered with `pptxgenjs`, and uploaded to OCI Object Storage.

## Tools

| Tool | Description |
|------|-------------|
| `create_deck` | Create a deck — auto-generate slides from a topic via AI, or pass a manual `slides` array |
| `get_deck` | Get full deck data (all slides) |
| `add_slide` | Add a slide to an existing deck |
| `update_slide` | Update fields on an existing slide |
| `delete_slide` | Remove a slide |
| `reorder_slides` | Change slide order |

21 layouts available: cover, section, icon-point, icon-list, big-number, quote, image-text, comparison, three-icons, focus, timeline, process, stats-grid, pros-cons, agenda, team, gallery, full-image, chart, table, contact, closing.

## Setup

```bash
npm install
npm run build
npm start
```

Copy `.env.example` to `.env` (or create one) with your OCI GenAI + Object Storage config:

| Variable | Description |
|----------|-------------|
| `OCI_GENAI_COMPARTMENT_ID` | OCI compartment for GenAI inference (required) |
| `OCI_OS_NAMESPACE` / `OCI_OS_BUCKET` | Object Storage bucket for generated decks (required) |
| `OCI_CONFIG_FILE` / `OCI_CONFIG_PROFILE` | OCI CLI config (default `~/.oci/config`, `DEFAULT`) |
| `USE_RESOURCE_PRINCIPAL` | Use instance/resource principal auth instead of the config file |
| `UNSPLASH_ACCESS_KEY` / `PEXELS_API_KEY` | Stock photo sources for image slides |
| `PORT` | Server port (default `8086`) |
| `API_KEY` | Optional key required on `/mcp` requests |

## Endpoints

| Method | Path | Description |
|--------|------|--------------|
| `GET` | `/health` | Health check |
| `GET` | `/test-genai` | Verify OCI GenAI connectivity |
| `POST` | `/mcp` | JSON-RPC endpoint (MCP protocol) |

## Docker

```bash
docker build -t ppt-generator-mcp .
docker run -p 8086:8086 --env-file .env ppt-generator-mcp
```
