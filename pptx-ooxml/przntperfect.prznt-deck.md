# prznt-deck — Prznt Perfect presentation generator

A Claude skill that builds **branded, fully editable PowerPoint (`.pptx`) decks**
in the **Prznt Perfect** design system: native slides, exact brand tokens, a
12×26 grid, real native tables, and shape-built charts. Give it a brief and
content, or just a topic — it structures the narrative and hands back a clean,
editable `.pptx`. Slide content is English-only.

## What it does

- **Native, fully editable PPTX** — every shape goes through a python-pptx engine
  (Arial, −1% tracking, exact line pitch); no flattened images.
- **On-brand by construction** — colors, type, spacing, and layout come from the
  design tokens; the deck ships with the brand theme palette in the PowerPoint
  color picker.
- **15 grid-based templates** — cover, agenda, section statements, text + image,
  cards, bar charts (always with a data table), data tables, and side-table
  layouts.
- **Charts as shapes, tables as native tables** — pixel-accurate and editable.
- **Self-check linter** — every generated deck is validated (fonts, sizes,
  colors, flatness) before delivery.

## Install

**Claude Code (terminal / VS Code / desktop):**

```bash
cp -r prznt-deck ~/.claude/skills/prznt-deck
```

Restart the Claude Code session; `/prznt-deck` then appears in autocomplete.

**claude.ai (web / app):** upload the skill as a zip in
**Settings → Capabilities → Skills**.

Requirements: Python 3.9+ (`python-pptx` is installed automatically on first run).

## Use

```
/prznt-deck                      # the skill asks about your content
/prznt-deck pitch for [product]  # with a topic
```

The skill asks one question — **do you have ready content?**

- **Yes** — paste your text / brief / numbers; it lays them out to the system.
- **No** — it invents a plausible product, narrative, and placeholder data
  (replace the placeholders before real use).

It then shows the proposed deck structure for approval and, once you confirm,
returns the `.pptx`. Edit by chatting: "swap slide 5 for a table", "add a
competition slide".

## What's inside

- `SKILL.md` — the workflow, design rules, and the 15-template catalog
- `references/` — design tokens, the design rules, and template anatomy
- `scripts/przntperfect/` — the generation engine (python-pptx)
- `scripts/build_canonical.py` — rebuilds the 15-template reference deck
- `scripts/inspect_pptx.py` — the QA linter for generated decks

## License

MIT — see [LICENSE](LICENSE).
