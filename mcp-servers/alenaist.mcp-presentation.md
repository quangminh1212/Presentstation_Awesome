# MCP Presentation

Materials for a presentation on **MCP (Model Context Protocol)** — the open standard
that connects AI apps (Cursor, ChatGPT, Claude, VS Code...) to your tools and data.

## Contents

| File | What it is |
|---|---|
| `01-how-mcp-works.md` | Plain-language explanation of MCP (start here) |
| `examples/01-dice-server/` | Minimal server (~50 lines) — the anatomy of MCP |
| `examples/02-weather-server/` | Server calling a real API — stdio *and* HTTP modes |

## Setup

```bash
cd examples/01-dice-server && npm install
cd ../02-weather-server && npm install
```

Requires Node 18+ (uses built-in `fetch`).

---

## Connecting to Cursor (what your team uses)

Cursor reads MCP servers from `~/.cursor/mcp.json` (global) or `.cursor/mcp.json`
(per project). Add both servers:

```json
{
  "mcpServers": {
    "dice": {
      "command": "node",
      "args": ["C:/Users/alena/desktop/projects/mcp-presentation/examples/01-dice-server/server.js"]
    },
    "weather": {
      "command": "node",
      "args": ["C:/Users/alena/desktop/projects/mcp-presentation/examples/02-weather-server/server.js"]
    }
  }
}
```

Then: **Cursor → Settings → MCP** — you should see both servers with a green dot
and their tools listed. In chat (Agent mode), try:

- *"roll 3 twenty-sided dice"*
- *"what's the weather in Buenos Aires right now?"*
- *"compare the weather in Buenos Aires, Madrid and Tokyo — where is it nicest today?"*

Cursor will ask for confirmation before running a tool (that's the security model
in action — good thing to point out during the demo).

## Connecting to ChatGPT

ChatGPT supports MCP through **connectors** (Settings → Connectors, requires
**Developer mode** enabled), but it only talks to **remote HTTP servers** — it
can't launch local processes like Cursor does. The weather server has an HTTP mode
for exactly this:

```bash
cd examples/02-weather-server
npm run start:http        # serves MCP at http://localhost:3333/mcp
```

To reach it from ChatGPT you need a public URL — tunnel it:

```bash
npx ngrok http 3333       # or: cloudflared tunnel --url http://localhost:3333
```

Then in ChatGPT: Settings → Connectors → Create, paste `https://<your-tunnel>/mcp`,
no authentication. Its tools become available in conversation.

> For the live demo, **Cursor is the safer bet** (local, no tunnel, no account
> settings). Mention the ChatGPT path as proof that it's one protocol, many hosts.

## Suggested demo flow (15–20 min)

1. **The pitch** (5 min) — walk through `01-how-mcp-works.md`: the M×N problem,
   the USB-C analogy, host/client/server, the lifecycle diagram.
2. **Show the code** (5 min) — open `01-dice-server/server.js`. Point out it's
   ~50 lines: name the server, register tools (description + schema + handler),
   connect. "The description is the API docs *for the model*."
3. **Live demo** (5 min) — ask Cursor to roll dice (silly on purpose → shows the
   model *deciding* to call a tool), then weather (real API call → shows real-world
   data flowing into the model's answer).
4. **The closer** — open `02-weather-server/server.js` and show the transport
   switch at the bottom: same tools, stdio for Cursor, HTTP for ChatGPT.
   "Now imagine this isn't weather — it's our internal API / DB / ticketing."

## Ideas for "what could WE build?"

- A server exposing your internal REST API (the model stops guessing endpoints)
- Read-only DB access: `query_users`, `get_order(id)`
- Design system lookup: `get_component_docs(name)`
- Jira/Linear: `create_ticket`, `my_open_tickets`
- CI status: `last_deploy_status(env)`
