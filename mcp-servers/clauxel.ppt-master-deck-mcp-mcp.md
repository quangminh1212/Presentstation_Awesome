# PPT Master Deck MCP

PPT Master Deck MCP remote MCP for ppt-master.

Paid remote MCP for ppt-master, structured receipts, usage logs, and audit-ready JSON evidence.

## Public Endpoints

- Website: https://pptmasterdeck.clauxel.com/?utm_source=github&utm_medium=directory&utm_campaign=sbl202605r26_224703
- MCP endpoint: https://pptmasterdeck.clauxel.com/mcp
- Server card: https://pptmasterdeck.clauxel.com/server-card.json
- Registry name: `com.clauxel.pptmasterdeck/pptmasterdeck-mcp`

## Access

This is a paid hosted remote MCP. Production calls require a bearer token issued from the product website.

```http
Authorization: Bearer <token>
```

Unauthenticated browser visits to `/mcp` return a clear JSON error instead of internal details.

## Tools

- `generate_editable_deck`
- `revise_deck_outline`
- `render_deck_preview`
- `export_deck_receipt`

## Quick Start

1. Open the website and choose a plan.
2. Create or request an API token.
3. Add the endpoint to an MCP client that supports Streamable HTTP remote servers.
4. Send JSON-RPC requests with the bearer token.

## Useful Links

- Product page: https://pptmasterdeck.clauxel.com/?utm_source=github&utm_medium=directory&utm_campaign=sbl202605r26_224703
- Pricing: https://pptmasterdeck.clauxel.com/?utm_source=github&utm_medium=directory&utm_campaign=sbl202605r26_224703#pricing
- Server card: https://pptmasterdeck.clauxel.com/server-card.json
- MCP endpoint: https://pptmasterdeck.clauxel.com/mcp

## Status

This repository is a public documentation and directory-submission reference for the hosted service. It does not contain the private production source code.
