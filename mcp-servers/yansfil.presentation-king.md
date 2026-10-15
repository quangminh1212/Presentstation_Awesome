# presentation-king

**Agents draft. You finish.**

A BYO-agent presentation tool for developers who make slides with coding agents (Claude Code, Codex, …).
Your agent writes the deck over MCP; you finish it by hand in a local web editor — drag, snap, restyle — without typing another prompt.
Free, open source, no built-in AI: the reasoning always comes from the agent subscription you already pay for.

![The editor: slide sidebar, canvas with snap-guided editing, token-scoped inspector, and the agent prompt bar](docs/screenshots/editor.png)

> **Status:** pre-release — not on npm yet. Everything below works today when run from source; see [INSTALL.md](INSTALL.md). Once published, the `npx presentation-king …` commands become the real interface.

## Why

- Stop describing pixel nudges in prose ("move that box left… no, the other box").
- Human edits and agent edits coexist without destroying each other.
- One renderer: what you edit is exactly what exports to HTML and PDF.

## Quick start

> Full guide for running from source, MCP registration, and the Claude Code skill/hook: [INSTALL.md](INSTALL.md).

```sh
# 1. Create a deck (pick one of three design sets)
npx presentation-king init my-talk

# 2. Let your agent draft it (MCP, see below), or edit right away
npx presentation-king serve my-talk

# 3. Ship it
npx presentation-king export my-talk        # static bundle + PDF
```

## How it works

- **`deck.json` is the source of truth** — a JSON scene graph: fixed 1280×720 canvas, absolute coordinates, stable element ids, typed elements (`text` / `image` / `shape` / `html-embed`), design-token styles. HTML is only ever a render artifact.
- **One deck server per deck** (`.pk/server.json`) owns the state; every write — your edits, agent ops, undo — goes through a single serialized write queue.
- **MCP is the agent's primary path.** The stdio MCP server is a thin client that auto-starts the deck server headless, so `apply_ops` works even when no editor is open. Direct file edits are an exception path: the schema validator quarantines broken elements, the editor renders them visibly broken, and saving never destroys them.
- **Blast radius**: pin a selection in the editor and the agent's `apply_ops` is rejected at write time if it touches anything outside the pin. No pin = whole deck writable.
- **Two undo lanes**: `Cmd+Z` only walks *your* edits. Agent changes are checkpoints, reverted only via checkpoint restore.
- **Change digest**: the agent reads a semantic summary of what you changed since its last checkpoint (`get_user_changes` / `ack_user_changes`), so it never bulldozes your manual polish.
- **Diff view**: inspect every agent checkpoint and each of your edit sessions as a semantic diff — change list, canvas highlights, and a before-state preview toggle.

## Agent setup (MCP)

Register the MCP server with your agent, per deck:

```sh
# Claude Code
claude mcp add presentation-king -- npx presentation-king mcp /path/to/my-talk
```

Tools: `get_deck`, `get_selection`, `apply_ops`, `get_screenshot`, `get_guidelines`, `get_user_changes`, `ack_user_changes`, `wait_for_prompt`, `get_deck_info`.
Agent-facing usage guide: [`agent/SKILL.md`](agent/SKILL.md).

### Waiting mode

Have the agent open the editor and listen:
the agent calls `wait_for_prompt`; whatever you type into the editor's prompt bar (plus your pinned selection) is delivered straight to it.
The tool times out with `no_prompt` (default 55 s) — the agent simply calls it again to keep waiting.

### Session-start hook (optional)

Inject unconsumed user changes at the start of every Claude Code session — add to your project's `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "node node_modules/presentation-king/hooks/inject-digest.mjs my-talk"
          }
        ]
      }
    ]
  }
}
```

The script is standalone and silent when there is nothing to report.

## Design sets

Three built-in sets — `minimal-light`, `dark-tech`, `bold-business` — each with four layers: design tokens, an element style dictionary, layout templates, and agent instructions.
Decks reference tokens (`token:accent`, style `heading-1`), so switching themes restyles every slide without moving a single element.
Raw hex values remain available as an escape hatch.

![A slide from an agent-drafted deck in the dark-tech set](docs/screenshots/agent-deck-dark-tech.png)

## User guides (2 layers)

- Global: `~/.presentation-king/guide.md` — rules for all your presentations
- Per deck: `<deck>/guide.md` — audience/tone for this one

Both are editable in the editor's Guide panel and merged into `get_guidelines` together with the active design set's agent instructions.

## Editing features (v1)

Move/resize with snap guides (drag threshold, cursor feedback) · inline text editing · html-embed source editing · multi-select (shift-click, containment marquee) · right-click context menus (canvas + slides) · element clipboard (Cmd+C/X/V) · image insert via file, URL, drag-&-drop, or paste · token-scoped styling with hex escape hatch · z-order · slide add/duplicate/delete/drag-reorder with range/toggle multi-select · zoom (fit/50/75/100%) · human-lane undo/redo · align/distribute · play mode (fullscreen + keyboard) · presenter view (notes + next slide) · agent chat sidebar with checkpoint diff cards, selection pin, and waiting-mode prompts · change diff view.

Non-goals (v1): hosting/sharing service, PPTX, realtime collaboration, animations, freeform drawing, cell-level table editing (use `html-embed`), desktop app, built-in AI, mid-deck layout-reflow switching.

## Development

```sh
pnpm install
pnpm dev              # editor (5173) + deck server on the sample deck
pnpm build && pnpm typecheck && pnpm lint
pnpm test:schema && pnpm test:history && pnpm test:mcp
pnpm test:export && pnpm test:hook
pnpm test:e2e         # Playwright
```

Monorepo: `packages/schema` (scene graph, validator, ops, history, diff) · `packages/design-sets` · `packages/renderer` (single renderer for editor = export = PDF) · `packages/server` (deck server + MCP) · `packages/editor` (React) · `packages/cli`.

[MIT](LICENSE).
