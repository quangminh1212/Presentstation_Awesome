# 10 Free MARP Templates — AI-Powered Presentations

10 ready-to-use MARP Markdown presentation templates, organized across 3 skill levels. Open in VS Code, edit the placeholder content, export to PDF or PPTX in seconds.

Built for the [AI Edge YouTube channel](https://www.youtube.com/@AIEdgeDaniel) — see the full walkthrough: **[coming soon]**

---

## Setup

**1. Install the VS Code extension**
Search for **Marp for VS Code** (by Marp team) in the Extensions panel.

**2. Enable HTML rendering**
Open VS Code Settings and set:
```
markdown.marp.enableHtml: true
markdown.marp.allowLocalFiles: true
```
Or add to `settings.json`:
```json
{
  "markdown.marp.enableHtml": true,
  "markdown.marp.allowLocalFiles": true
}
```

**3. Open any template**
Open a `.md` file from `templates/` — the preview pane shows the live slide deck.

**4. Export**
```bash
# PDF
npx @marp-team/marp-cli templates/01-topic-presentation.md --pdf --allow-local-files

# PowerPoint
npx @marp-team/marp-cli templates/01-topic-presentation.md --pptx --allow-local-files

# HTML (preserves animations and interactive elements)
npx @marp-team/marp-cli templates/01-topic-presentation.md --html --allow-local-files
```

---

## Templates

### Level 1 — Beginner

| # | File | Description | Key Features |
|---|------|-------------|--------------|
| 01 | `01-topic-presentation.md` | Generic topic overview deck | Title slide, section cards, bullet lists |
| 02 | `02-learning-deck.md` | Step-by-step educational content | Concept breakdowns, numbered steps, summary slide |
| 03 | `03-client-proposal.md` | Business proposal for clients | Problem/solution framing, pricing, CTA slide |

### Level 2 — Intermediate

| # | File | Description | Key Features |
|---|------|-------------|--------------|
| 04 | `04-weekly-report.md` | Weekly business performance report | Metric cards, executive summary, trend highlights |
| 05 | `05-financial-dashboard.md` | Personal or team finance overview | Budget breakdown, SVG donut chart, category rows |
| 06 | `06-comparison-table.md` | Head-to-head product/tool comparison | Comparison grid, verdict tags, feature matrix |
| 07 | `07-project-timeline.md` | Project roadmap with milestones | Timeline component, phase labels, status dots |

### Level 3 — Advanced

| # | File | Description | Key Features |
|---|------|-------------|--------------|
| 08 | `08-recipe-cards.md` | Visual recipe / card-style layout | Reusable card grid, image slots, tag labels |
| 09 | `09-interactive-event.md` | Event or conference program | Collapsible details, speaker cards, schedule grid |
| 10 | `10-automated-report.md` | Data-driven report from CSV input | Auto-filled from `data/` CSVs, SVG bar chart, summary KPIs |

---

## Using the AI Edge Dark Theme

All templates embed the dark theme CSS inline. To use it as a standalone file instead:

1. Copy `themes/ai-edge-dark.css` to your project folder
2. Reference it in the frontmatter:
   ```yaml
   ---
   marp: true
   theme: ai-edge-dark
   ---
   ```
3. Add to VS Code settings:
   ```json
   "markdown.marp.themes": ["./themes/ai-edge-dark.css"]
   ```

---

## Using with Claude Code

Have Claude generate slides directly from your content using the `marp-slides` skill.

**Install Claude Code** (free tier available): [claude.ai/code](https://claude.ai/code)

**Prompt to get started:**
```
Create a MARP presentation about [your topic]. Use the AI Edge dark theme
(Outfit headings, Raleway body, #ff6b1a accent). Include a title slide,
3-4 content slides with one idea each, and a closing CTA slide.
Export-ready PDF.
```

Claude will generate the full `.md` file with embedded CSS. Open it in VS Code and export.

---

## Data Files

The `data/` folder contains sample CSVs used by Template 10 (`10-automated-report.md`):

- `sample-report.csv` — baseline weekly business data
- `sample-report-week2.csv` — week-over-week comparison data

Replace with your own CSV data and update the chart values in the template.

---

## License

MIT — free to use, modify, and distribute. See [LICENSE](./LICENSE).
