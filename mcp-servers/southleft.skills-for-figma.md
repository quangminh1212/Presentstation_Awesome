# Skills for Figma

A collection of open-source agent skills for the **native [Figma MCP server](https://github.com/figma/mcp-server-guide)**.
Each skill teaches an agent (Claude, Codex, Gemini, Copilot) to perform a focused design-systems task in
Figma — exporting and importing design tokens, analyzing component sets, linting for WCAG and design-system
compliance, auditing accessibility, building Slides and FigJam content, and more.

Every skill runs through the Figma MCP's `use_figma` tool (Plugin API execution) and requires no plan-gated
APIs — token reads use the Plugin API, so they work on any Figma plan.

> These skills are a Figma-MCP-focused subset of [**southleft/figma-console-mcp-skills**](https://github.com/southleft/figma-console-mcp-skills),
> repackaged here with community-friendly names. The full collection (including REST-API-based version history,
> changelog, blame, and comments skills) lives in that repository.

## Requirements

- An agent host with the **Figma MCP server** connected (e.g. Claude Code, Claude Desktop, Codex, Gemini).
- The official **`figma-use`** skill, which teaches the `use_figma` Plugin API conventions. Every skill here
  loads it first.

## Install

### npx — any agent (Claude Code, Codex, Cursor, Gemini CLI, …)

```bash
npx skills add southleft/skills-for-figma          # install all skills
npx skills add southleft/skills-for-figma --list   # preview without installing
npx skills add southleft/skills-for-figma --skill export-tokens-figma   # just one
```

Powered by the [`skills`](https://github.com/vercel-labs/skills) CLI — it detects your agent and drops
each skill into the right directory.

### Claude Code plugin (one command)

```
/plugin marketplace add southleft/skills-for-figma
/plugin install skills-for-figma@skills-for-figma
```

### Manual (any host)

```bash
git clone https://github.com/southleft/skills-for-figma.git
cd skills-for-figma
cp -R skills/* ~/.claude/skills/
```

For other hosts, drop the folders from `skills/` into that tool's skills directory (e.g. `.codex/skills/`,
`.gemini/skills/`). Once installed, an agent auto-selects a skill from your request, or you can invoke one
explicitly with `/skill-name`.

## Skills

### Tokens & variables
- **export-tokens-figma** — Export Figma variables to DTCG, CSS custom properties, Tailwind, SCSS, TypeScript, JSON, Style Dictionary, or Tokens Studio, with multi-mode and alias resolution.
- **import-tokens-figma** — Create and update Figma variables from DTCG token files, with multi-mode values, alias resolution, and non-destructive in-place matching.
- **setup-design-tokens-figma** — Bootstrap a complete token system (a collection, its modes, and all variables with per-mode values) in one atomic operation.
- **manage-variables-figma** — Create, update, rename, and delete variables, collections, and modes, including batch create/update.
- **library-variables-figma** — Discover variables available from subscribed team libraries and import them into the current file by key.

### Components
- **analyze-component-set-figma** — Analyze a component set as a variant state machine, mapping variant properties to CSS pseudo-classes and reporting per-variant visual differences.
- **arrange-component-set-figma** — Arrange a component set's variants into a labeled grid on the canvas.
- **component-properties-figma** — Define a component's property API and instantiate the component with property values applied.
- **deep-component-figma** — Walk a component to unlimited depth and return its full node tree with resolved token bindings, main-component references, and reactions.
- **generate-component-doc-figma** — Generate Markdown documentation for a Figma component, covering anatomy, tokens, states, accessibility, and design-to-code parity.
- **design-system-inventory-figma** — Extract a unified inventory of a file's variables, components, and styles with resolved visual specifications.

### Quality & accessibility
- **lint-design-figma** — Lint a node tree against WCAG 2.2 and design-system rules, flagging contrast failures, hardcoded colors and styles, and detached components.
- **audit-accessibility-figma** — Produce a per-component accessibility scorecard covering interaction-state coverage, focus indicators, target size, and color-blind simulation.
- **scan-code-accessibility-figma** — Run axe-core against HTML in a JSDOM environment and map violations back to the originating Figma design.
- **check-design-parity-figma** — Compare a Figma design node against a code specification and report drift as scored discrepancies by severity.

### Annotations, FigJam & Slides
- **annotations-figma** — Read and write designer annotations and annotation categories on Figma nodes.
- **create-figjam-content** — Author and read FigJam boards: stickies, connectors, shapes with text, sections, tables, and code blocks.
- **build-slides-figma** — Author Figma Slides decks: create and reorder slides, add text and shapes, and set backgrounds, transitions, and view mode.

## License

[MIT](LICENSE).

## Related

- [southleft/figma-console-mcp-skills](https://github.com/southleft/figma-console-mcp-skills) — the full skill collection.
- [Figma Console MCP](https://github.com/southleft/figma-console-mcp) — the MCP server these skills were distilled from.
