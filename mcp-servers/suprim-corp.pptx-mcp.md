# pptx-mcp

An MCP server for reading and editing PowerPoint files. Point an agent at a `.pptx` and it can list the slides, read the
text, edit shapes and check its own work.

Units on every tool are **inches**, never EMU. Slide numbers are **1-based**, matching what PowerPoint shows.

## Requirements

[Bun](https://bun.sh) 1.3 or newer. The server runs `src/index.ts` directly, so there is no build step and no `dist/`.

## Install

```sh
git clone git@github.com:suprim-corp/pptx-mcp.git
cd pptx-mcp
bun install
```

## Configure

Add the server to your MCP client. Use an **absolute path** to `src/index.ts` — the client's working directory is not
necessarily this repository.

```json
{
	"mcpServers": {
		"pptx": {
			"command": "bun",
			"args": [
				"run",
				"/absolute/path/to/pptx-mcp/src/index.ts"
			]
		}
	}
}
```

For Claude Code this goes in `.mcp.json` at the root of the project you are working in. Restart the client afterwards,
then check it connected:

```sh
claude mcp get pptx
```

Pass absolute paths for the `path` argument too, for the same reason.

## Tools

| Tool                                              | What it does                                                     |
|---------------------------------------------------|------------------------------------------------------------------|
| [`pptx_inspect`](docs/tools/inspect.md)           | Map a deck, or list one slide's shapes with their ids and bounds |
| [`pptx_read_text`](docs/tools/read-text.md)       | Read a deck, one slide, its outline or its speaker notes         |
| [`pptx_notes`](docs/tools/notes.md)               | Read or edit one slide's speaker notes                           |
| [`pptx_replace_text`](docs/tools/replace-text.md) | Find and replace text, or fill `{{token}}` placeholders          |
| [`pptx_validate`](docs/tools/validate.md)         | Check a deck after editing it: package errors, layout warnings   |

Each tool has its own page under [`docs/tools/`](docs/tools/). The parameter tables there are generated from the server,
so they cannot drift from what the tools actually accept.

## Typical flow

Inspecting comes first: every editing tool needs a `shape_id`, and `pptx_inspect` is the only tool that reports them.

```
pptx_inspect   { path }                      → which slide do I want?
pptx_read_text { path, scope: "deck" }       → what does the deck say?
pptx_inspect   { path, slide: 12 }           → shape ids and bounds on that slide
```

`pptx_inspect` reports `title: null` on decks that use plain text boxes instead of layout placeholders, which is most
designer-built decks. When the map is too sparse to tell slides apart,
`pptx_read_text` with `scope: "deck"` reads every slide's text, labelled by slide number.

## Development

```sh
bun test              # tests
bun run typecheck     # tsc --noEmit; bun strips types without checking them
bun run lint          # oxlint
bun run format        # oxfmt --write
bun run docs          # regenerate parameter tables in docs/tools/
bun run docs:check    # fail if they are out of date
```

`bun run typecheck` is a separate gate on purpose: Bun executes TypeScript by stripping types, so a type error can pass
the test suite untouched.
