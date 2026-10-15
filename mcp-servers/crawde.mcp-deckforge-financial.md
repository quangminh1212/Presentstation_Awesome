# deckforge-financial-mcp

AI-powered financial modeling MCP server for pitch deck slides. Generate investor-ready financial projections, unit economics, cap tables, and funding scenarios.

## Tools

### `build_revenue_projection`
Generate month-by-month revenue projections — MRR, ARR, customer count, churn, and milestone tracking over 3-60 months.

### `calculate_unit_economics`
Calculate SaaS unit economics — LTV, CAC, LTV/CAC ratio, payback period, net revenue retention, and contribution margin with health assessment.

### `build_cap_table`
Generate capitalization tables showing ownership distribution across founders, investors, and option pool. Models dilution across multiple funding rounds.

### `model_funding_round`
Model a prospective funding round — pre/post-money valuation, dilution, new shares, implied ARR multiples, with stage-specific benchmarks.

### `analyze_break_even`
Calculate break-even point, monthly burn rate, and cash runway. Shows path to profitability with current growth trajectory.

## Installation

```bash
npx deckforge-financial-mcp
```

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "deckforge-financial": {
      "command": "npx",
      "args": ["-y", "deckforge-financial-mcp"]
    }
  }
}
```

## Examples

**Revenue projection:**
> "Project revenue for a SaaS startup with $5K MRR, 12% monthly growth, $50 ARPU, and 5% churn over 24 months"

**Unit economics:**
> "Calculate unit economics with $100 ARPU, 3% monthly churn, $500 CAC, 80% gross margin"

**Cap table:**
> "Build a cap table for 2 co-founders (60/40 split, 10M shares), 15% option pool, $2M seed at $8M pre-money"

**Funding scenario:**
> "Model a Series A raise of $10M with current ARR of $2M"

**Break-even:**
> "Analyze break-even with $50K/mo fixed costs, $10/user variable cost, $49/user revenue, $15K current MRR, $500K cash"

## License

MIT — Built by [Crawde](https://crawde.com) | [DeckForge](https://deckforgeai.com)
