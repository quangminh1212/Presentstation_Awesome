# ai-pitch-deck-mcp

AI-powered pitch deck generation MCP server. Create investor-ready pitch decks, generate individual slides, get structure recommendations, improve existing content, and find the right metrics for your stage.

## Tools

| Tool | Description |
|------|-------------|
| `generate_pitch_deck` | Generate a complete pitch deck with all slides, speaker notes, and export options |
| `generate_slide` | Create content for a single slide (problem, solution, traction, team, ask, etc.) |
| `suggest_deck_structure` | Get optimal slide structure for your stage (seed, Series A, demo day, etc.) |
| `improve_slide_content` | Analyze existing slide content and get specific improvement suggestions |
| `suggest_deck_metrics` | Find the right KPIs for your stage and industry with benchmarks |

## Installation

```bash
npx ai-pitch-deck-mcp
```

## Configuration (Claude Desktop / Cursor / VS Code)

```json
{
  "mcpServers": {
    "ai-pitch-deck": {
      "command": "npx",
      "args": ["-y", "ai-pitch-deck-mcp"]
    }
  }
}
```

## Example Usage

### Generate a full deck
```
Generate a seed round pitch deck for "Acme AI" — we're an AI-powered compliance 
platform for mid-market companies. Our tagline is "Compliance on autopilot." 
Problem: compliance teams spend 60% of time on manual document review. 
We have $50K MRR growing 25% month-over-month. Raising $3M seed.
```

### Get structure advice
```
What slides should I include for a Series A pitch to a growth-stage VC? 
We have revenue and product-market fit.
```

### Improve a slide
```
Improve my problem slide. Heading: "The Problem with Enterprise Compliance"
Bullets: "Compliance is hard", "Companies waste money", "Manual processes are slow"
```

### Find the right metrics
```
I'm a SaaS company raising Series A. We have $120K MRR and 45 paying customers.
What metrics should I highlight in my deck?
```

## Supported Stages

- `seed-round` — 8 slides, vision + team focused
- `series-a` — 10 slides, traction-heavy
- `series-b-plus` — 8 slides, metrics + defensibility
- `demo-day` — 5 slides, story-driven
- `corporate-partnership` — 6 slides, integration focused
- `customer-facing` — 5 slides, outcomes focused

## Slide Types

Title, Problem, Solution, Market, Traction, Business Model, Competition, Team, Financials, Ask

## Powered By

[DeckForge AI](https://deckforge.ai) — Full pitch deck platform with AI generation, 4 visual templates, PPTX export, share links with viewer analytics, and team collaboration. Starting at $9/mo.
