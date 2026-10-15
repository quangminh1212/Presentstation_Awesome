# slidev-mcp

**Create, edit, validate, and export Slidev presentations from your AI agent.**

`slidev-mcp` is a local [Model Context Protocol](https://modelcontextprotocol.io/) server for [Slidev](https://sli.dev/). It gives supported AI clients a focused toolkit for building real presentation projects: initialize decks, import a whole deck or add slides one at a time or in bulk, update slides, apply themes and styles, insert Mermaid diagrams, verify the deck, and export final assets.

## Why It Exists

Slide decks are usually iterative: draft, restructure, style, verify, export, repeat. `slidev-mcp` turns that workflow into MCP tools your agent can call directly inside a trusted local workspace.

## Highlights

- **Built for Slidev**: works with `slides.md`, themes, transitions, Mermaid diagrams, and Slidev exports.
- **Token-efficient bulk authoring**: import a full deck from disk with `import_markdown` (slide content never passes through the model's tokens) or add many slides in a single `add_slides` call.
- **Local-first**: runs over STDIO and operates in the current workspace.
- **Agent-ready**: installer support for OpenCode, Claude Code, Antigravity, and Codex.
- **Safe output behavior**: keeps `stdout` reserved for MCP JSON-RPC and sends logs/errors to `stderr`.
- **No required environment variables**: install, configure, and start using it.

## Requirements

- Node.js `>=18`
- [pnpm](https://pnpm.io/) (recommended; this repo is managed with pnpm and ships a `pnpm-lock.yaml`)
- Python 3, used by the installer to patch JSON/TOML config files

## Quick Start

Clone, install, build, and run the interactive installer:

```bash
git clone <repo-url> slidev-mcp
cd slidev-mcp
pnpm install
pnpm build
bash scripts/install.sh
```

The installer detects whether it can use the local build:

```bash
node /path/to/slidev-mcp/dist/index.js
```

If `node` is unavailable but `deno` is installed, the installer uses the local build through Deno:

```bash
deno run -A /path/to/slidev-mcp/dist/index.js
```

If `dist/index.js` is missing, it falls back to:

```bash
pnpm dlx slidev-mcp
```

## Interactive Installer

Run:

```bash
bash scripts/install.sh
```

The installer can configure:

- OpenCode
- Claude Code
- Antigravity
- Codex

For CI or scripted setup, use non-interactive mode:

```bash
bash scripts/install.sh --non-interactive --target codex --scope global
bash scripts/install.sh --non-interactive --target all --scope project --dry-run
```

Targets are `opencode`, `claude`, `antigravity`, `codex`, or `all`. Scopes are `global`, `project`, or `both`.

It also includes an **Update** option. The menu shows whether the local package appears up to date, has an update available, or could not determine the status.

```text
slidev-mcp interactive installer
Configure MCP once, then get back to making slides.

Runtime
  mode:    local build
  command: node /path/to/slidev-mcp/dist/index.js
  version: update available v0.1.0 -> v0.3.2

Choose what to configure

  1) OpenCode
  2) Claude Code
  3) Antigravity
  4) Codex
  a) All four
  u) Update slidev-mcp [update available v0.1.0 -> v0.3.2]
  q) Quit
```

When updating from a git checkout, the installer runs:

```bash
git pull --ff-only
pnpm install
pnpm build
```

If the working tree has uncommitted changes, it asks before pulling.

## Manual Configuration

Use manual configuration when you prefer to edit client config files yourself or cannot run the installer.

### OpenCode

Config paths:

- Global: `~/.config/opencode/opencode.json`
- Project: `./opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "slidev-mcp": {
      "type": "local",
      "command": ["pnpm", "dlx", "slidev-mcp"],
      "enabled": true
    }
  }
}
```

For a Deno-powered local build, use:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "slidev-mcp": {
      "type": "local",
      "command": ["deno", "run", "-A", "/path/to/slidev-mcp/dist/index.js"],
      "enabled": true
    }
  }
}
```

### Claude Code

Use the Claude CLI:

```bash
claude mcp add --scope user slidev-mcp -- pnpm dlx slidev-mcp
```

For a local build:

```bash
claude mcp add --scope user slidev-mcp -- node /path/to/slidev-mcp/dist/index.js
```

If your environment does not have `node` available, Deno can run the built server:

```bash
claude mcp add --scope user slidev-mcp -- deno run -A /path/to/slidev-mcp/dist/index.js
```

Supported scopes are `user`, `local`, and `project`.

### Antigravity

Config path:

```text
~/.gemini/antigravity/mcp_config.json
```

```json
{
  "mcpServers": {
    "slidev-mcp": {
      "command": "pnpm",
      "args": ["dlx", "slidev-mcp"]
    }
  }
}
```

### Codex

Config paths:

- Global: `~/.codex/config.toml`
- Project: `.codex/config.toml`

```toml
[mcp_servers.slidev-mcp]
command = "pnpm"
args = ["dlx", "slidev-mcp"]
type = "stdio"
```

For a local build:

```toml
[mcp_servers.slidev-mcp]
command = "node"
args = ["/path/to/slidev-mcp/dist/index.js"]
type = "stdio"
```

With Deno:

```toml
[mcp_servers.slidev-mcp]
command = "deno"
args = ["run", "-A", "/path/to/slidev-mcp/dist/index.js"]
type = "stdio"
```

## MCP Tools

| Tool | What it does |
|---|---|
| `init_presentation` | Create or attach to a Slidev project, with `minimal`, `agent-dark`, or `custom` presets; supports safe `dry_run` previews including overwrite plans |
| `import_markdown` | Import a full multi-slide document in one call, from a file `path` (content never passes through the model's tokens) or inline `content`; `replace` swaps `slides.md` (backing up the old file to `slides.md.bak`) or `append` adds after existing slides; validates before writing and supports `dry_run` diff preview |
| `add_slide` | Append or insert a single slide; supports `dry_run` diff preview |
| `add_slides` | Append or insert many slides as one contiguous block in a single call (one parse + write, all-or-nothing); supports `dry_run` diff preview |
| `update_slide` | Replace the content of an existing slide; supports `dry_run` diff preview |
| `delete_slide` | Delete a slide, while protecting the last slide; supports `dry_run` diff preview |
| `list_slides` | Inspect slide order, previews, and frontmatter |
| `get_project_info` | Inspect active project paths, theme, package versions, slide count, and verification status |
| `set_theme` | Change the Slidev theme and optionally install the theme package; supports `dry_run` multi-file diff preview |
| `set_style` | Apply global CSS, per-slide style blocks, or UnoCSS classes; supports `dry_run` diff preview |
| `set_slide_transition` | Configure transitions, `v-click` reveals, and `v-motion` animations; supports `dry_run` diff preview |
| `add_diagram` | Insert Mermaid diagrams; supports `dry_run` diff preview |
| `export_presentation` | Export to PDF, PNG, or a static SPA build with custom output, timeout, dry-run, and syntax preflight |
| `verify_presentation` | Validate `slides.md`; `render` and `full` levels also run a Slidev build check in a cleaned temporary output directory |
| `repair_presentation` | Safely normalize `slides.md` structure, removing BOM/leading whitespace and canonicalizing separators |

### Building a deck efficiently

Building a large deck by calling `add_slide` once per slide is expensive: each call is a separate turn, and the model re-reads every prior tool call, so the accumulated context cost grows roughly with the square of the slide count. Pick the cheapest tool for the job:

1. **`import_markdown(path: "deck.md")`** — cheapest. The Markdown is read on the server, so the slide content never passes through the model's tokens. One call builds the whole deck regardless of slide count. Use `mode: "replace"` to swap `slides.md` (the previous file is backed up to `slides.md.bak`) or `mode: "append"` to add the imported slides after the existing ones, keeping the current global frontmatter. Run `init_presentation` first so a project exists, then import.
2. **`add_slides(slides: [...])`** — when the content must be authored inline (no file on disk yet). One parse and one write cover the whole batch.
3. **`add_slide(content)`** — for single-slide edits only, not for assembling a deck.

A typical bulk flow:

```text
init_presentation  ->  import_markdown(path: "deck.md")  ->  verify_presentation  ->  export_presentation
```

This guidance is also delivered to the client automatically through the MCP server `instructions` field, so a compatible agent receives the recommended workflow on connection — there is no separate "list tools" call, since the protocol's own `tools/list` already advertises every tool and its schema.

### Tool response contract

Tools return a JSON envelope inside the MCP text content:

| Result | Shape |
|---|---|
| Success | `{ "success": true, "data": { ... }, "message"?: "...", "warnings"?: [], "issues"?: [] }` |
| Error | `{ "success": false, "code": "...", "message": "...", "error": "...", "details"?: { ... } }` plus MCP `isError: true` |

### Dry-run previews

For write tools that edit project files, pass `dry_run: true` to preview without writing. The success `data` includes:

| Field | Meaning |
|---|---|
| `dryRun` | Always `true` for preview responses |
| `wouldWrite` | Files that would be changed |
| `diff` | Unified diff preview of the pending file change |
| `diffs` | Per-file unified diff previews for tools that can change multiple files, such as `set_theme` updating both `slides.md` and `package.json` |

`export_presentation` also supports `dry_run`, but it previews the Slidev command/arguments instead of returning a file diff.

`import_markdown` previews include `wouldBackup` (the `slides.md.bak` path that a non-preview `replace` would create) and `importedSlides` (how many slides the source document contains), alongside the standard `diff`.

`init_presentation` supports `dry_run` as a safe scaffold preview. It validates and resolves the target path, builds the expected scaffold in memory, and never creates directories, writes files, deletes existing content, sets the active project path, or runs `pnpm install`. Its preview data includes `mode` (`create`, `attach`, or `overwrite`), `wouldCreate`, `wouldReplace`, `wouldDelete`, `wouldKeep`, per-file `diffs` for existing scaffold files, and `install` command metadata.

### `init_presentation` presets

- `agent-dark` (default): preserves the v1.0 behavior with the opinionated dark style, bundled Vue components, default theme, and starter slides. Its code styling stays clean and lets Slidev/Shiki own syntax-highlighted code blocks; it does not add borders to `code`.
- `minimal`: creates a small standard Slidev project with `slides.md` and `package.json` only.
- `custom`: currently uses the agent-ready scaffold while allowing callers to override theme and skip dependency installation.

`init_presentation` also supports `install_dependencies: false`, `overwrite: true`, and `dry_run: true`. Existing directories are never replaced unless `overwrite` is explicitly set; use `dry_run: true` with `overwrite: true` first to inspect exactly which scaffold files would be replaced and which non-scaffold entries would be deleted.

If behavior differs between documentation and code, treat `src/tools/*.ts` as the source of truth.

## Runtime Behavior

- Transport: STDIO via `@modelcontextprotocol/sdk/server/stdio`
- Working directory: `process.cwd()`
- Project discovery: finds `slides.md` in the current directory or one immediate child directory
- Logging: writes logs and errors to `stderr`
- MCP protocol output: writes JSON-RPC traffic to `stdout`

## Local Development

```bash
pnpm install
pnpm build
pnpm typecheck
pnpm test
pnpm check
node dist/index.js
```

For development without building:

```bash
pnpm dev
```

## Security

Run this server only in trusted local workspaces. Some tools execute local commands such as `pnpm` and `pnpm exec slidev` inside the active project directory. Avoid elevated privileges, review generated files before publishing, and see [SECURITY.md](SECURITY.md) for reporting and operational guidance.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for setup, validation, and pull request guidance.

## License

MIT. See [LICENSE](LICENSE).
