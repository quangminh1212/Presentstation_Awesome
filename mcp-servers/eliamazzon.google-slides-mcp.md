# Google Slides MCP Server

An [MCP](https://modelcontextprotocol.io) server for Google Slides, focused on **modifying existing
presentations** and **building client decks from templates**: copy a template, read its structure to find
placeholders and element IDs, fill text and swap images, reorder/duplicate/delete slides, and render slides
to a PNG to verify the result.

Built with [mcp-use](https://mcp-use.com), so it speaks Streamable HTTP and works as a remote connector in
both ChatGPT (Plus and above) and Claude -- not just as a local stdio server.

The retry/backoff behavior is ported (not forked -- this project is TypeScript, the source is Go) from
[ngs/google-mcp-server](https://github.com/ngs/google-mcp-server)'s `slides/` package (MIT licensed).

The tools also expose a `slides://guide` resource covering the workflow below in more depth; it's fetched
on demand rather than living in every tool description.

## Template workflow

The core loop for filling a template:

1. **`copy-presentation`** the template into a fresh file (the original is never touched).
2. **`list-slides`** on the copy for an outline -- one line per slide with its position, `slideId`, and a
   derived title. This is how you find the slides you care about.
3. **`read-slides`** on the ones you want, for each element's `objectId` and current text. Scan the text for
   placeholder tokens like `{{client}}`.
4. Fill it: **`replace-text`** for tokens that repeat across the deck, **`set-element-text`** to set one or
   more elements (each by `objectId`) in a single call, **`replace-image`** to swap one or more logos/photos.
5. Fit it: if a filled-in value is longer than the template allowed for, **`format-text`** to shrink the
   font (or restyle it) and/or **`resize-element`** to widen/move the box -- both take a batch of edits so
   you can fix several elements in one call. Read the current geometry with `read-slides` at
   `detail: "layout"`.
6. Arrange it: **`duplicate-slide`** to repeat one or more styled slides, **`move-slides`** to reorder,
   **`group-elements`** + **`resize-element`** to move several elements together, **`delete-slide`** /
   **`delete-element`** to trim one or more at once.
7. **`render-slide`** (one call can render several slides at once) to a PNG to visually confirm before
   sharing.

> **Most edit tools take arrays.** Bundle everything you can into one call -- read-slides once, then one
> set-element-text call carrying every edit, not one call per element. See the `slides://guide` resource for
> the batching model and its atomicity tradeoffs.

> **Text is inserted literally.** Every text tool writes the string as given -- pass real characters (`&`,
> `—`, `"`), not HTML entities like `&amp;`, `&mdash;`, or `&quot;`. Entities are **not** decoded and will
> appear verbatim on the slide.

## Reading large decks

A real template is ~60 slides, and most elements on each are furniture -- a running header, a copyright
line, logos, decorative shapes. Reading all of it costs tens of thousands of tokens and tells you little,
so the read path is split in two:

- **`list-slides`** is the cheap entry point: position, `slideId`, and a derived title per slide, no
  elements. A 59-slide deck costs ~700 tokens. The title is the slide's `TITLE` placeholder if it has one,
  otherwise its largest text (in a designed template the title runs at 60pt+ against a 10pt header, so this
  is reliable), otherwise its longest.
- **`read-slides`** takes explicit `slideIds` and a `detail` level:
  - `"text"` (default) -- `objectId`, kind, placeholder, text, `fontSize`. Enough to edit. ~110 tokens/slide.
  - `"layout"` -- adds position/size in points and `fontFamily`. Roughly doubles the response; ask for it
    only when you're about to call `resize-element` or `format-text`.

Every element is always listed, including empty decorative ones -- they cost ~8 tokens and stay targetable.
Nothing is hidden from the caller by heuristic.

`@block:` / `@tag:` lines in a slide's speaker notes (written with `set-slide-notes`) are parsed out by
`list-slides`, which can filter on them -- useful for pruning a master template down to one client's deck.

## Setup

### 1. Google Cloud project

1. Create or pick a project in the [Google Cloud Console](https://console.cloud.google.com).
2. Enable the **Google Slides API** and **Google Drive API**.
3. Configure the OAuth consent screen (add the `presentations` and `drive` scopes; add yourself as a
   test user if the app is in Testing mode). Full `drive` (not `drive.file`) is required so
   `copy-presentation` can read a template the app didn't create. Note: `drive` is a *restricted* scope --
   free to use in Testing mode, but it adds a security assessment to Google's Production verification (on top
   of the `presentations` sensitive-scope review).
4. Create an **OAuth client ID** of type **Web application** (not Desktop -- this server mediates the OAuth
   flow itself via `oauthProxy`). Leave "Authorized redirect URIs" for now; you'll add it after your first
   deploy (see below).

### 2. Environment variables

Copy `.env.example` to `.env` and fill in the client ID/secret from step 1:

```bash
cp .env.example .env
```

### 3. Run locally

```bash
npm install
npm run dev
```

This serves the MCP endpoint at `http://localhost:3000/mcp` and opens the
[Inspector](http://localhost:3000/inspector) for interactive testing. Add
`http://localhost:3000/oauth/callback` to the OAuth client's authorized redirect URIs to test the OAuth flow
locally.

Try the template loop end-to-end: `copy-presentation` a deck you own, `list-slides` on the copy to find the
slide you want, `read-slides` for its element IDs, `set-element-text` / `replace-text` to fill it, then
`render-slide` to verify. Always work against a copy -- never point the mutating tools at a template or a
client's live deck.

## Deploy

```bash
npm run deploy
```

Deploys to [Manufact Cloud](https://manufact.com) and prints a public `https://<slug>.run.mcp-use.com/mcp`
URL. After the first deploy, add `https://<slug>.run.mcp-use.com/oauth/callback` to the Google OAuth
client's authorized redirect URIs (and set `GOOGLE_CLIENT_ID`/`GOOGLE_CLIENT_SECRET` as environment
variables on the deployed server).

### Add to ChatGPT

Settings → Apps and Connectors → Advanced Settings → enable Developer Mode → Connectors → Create → paste
the deployed URL.

### Add to Claude

Settings → Connectors → Add custom connector → paste the deployed URL.

## Tools

**Templates & files**

| Tool | Description |
|------|-------------|
| `copy-presentation` | Copy a whole presentation to start from a template |
| `create-presentation` | Create a new, empty presentation |
| `share-presentation` | Grant "anyone with the link" access at a given role |
| `export-presentation-pdf` | Validate export access and return the PDF export URL |

**Read**

| Tool | Description |
|------|-------------|
| `list-slides` | Outline the deck: position, `slideId`, derived title per slide. Filterable by `@block`/`@tag` |
| `read-slides` | Read given slides' elements: `objectId`, kind, placeholder, text, `fontSize` (+ geometry at `detail: "layout"`) |
| `render-slide` | Render one or more slides to PNGs (viewable inline) to verify edits, up to 6 per call |

**Edit existing slides**

| Tool | Description |
|------|-------------|
| `replace-text` | Replace a piece of text everywhere (fill a repeated placeholder token) |
| `set-element-text` | Set the full text of one or more elements, each by its `objectId`, in one call. Applies `**bold**`/`*italic*`/`` `code` ``/links |
| `format-text` | Restyle one or more elements' text (font size, bold/italic/underline, color, family) -- e.g. shrink to fit |
| `resize-element` | Resize/reposition one or more elements (w/h/x/y in pt) -- e.g. widen a box for longer content |
| `replace-image` | Swap one or more image elements (by `objectId`) with new image URLs |
| `delete-element` | Remove one or more elements (text box, image, shape, table), each by `objectId` |
| `group-elements` | Group 2+ elements into one group (move/scale/delete as a unit) |
| `ungroup-elements` | Dissolve one or more groups back into independent elements |
| `set-slide-background` | Set a solid background color on one slide, an arbitrary subset, or the whole deck |
| `set-slide-notes` | Replace one or more slides' speaker notes -- also where `@block:`/`@tag:` metadata lives |

**Add slides & elements**

| Tool | Description |
|------|-------------|
| `create-slide` | Insert one or more slides -- blank, or from a built-in layout (`layoutName`), in one call |
| `duplicate-slide` | Duplicate one or more slides (best way to repeat a styled template slide) |
| `delete-slide` | Delete one or more slides |
| `move-slides` | Reorder slides to a new position in the deck |
| `add-text-box` | Add one or more free-positioned text boxes. Returns each new `objectId` |
| `add-image` | Add one or more images from URLs. Returns each new `objectId` |
| `add-table` | Add one or more tables, optionally filling `cells`. Returns each new `objectId` |
| `add-shape` | Add one or more shapes (rectangle, ellipse, ...). Returns each new `objectId` |

## Tests

```bash
npm test
```

Runs offline against a fixture modeled on a real 59-slide deck (`test/fixtures/deck.ts`) -- no network, no
auth. It covers title derivation, the `detail` levels, EMU↔PT geometry, and `@block`/`@tag` parsing, and
asserts a **token budget** on both read tools so the response sizes can't quietly regress.

## Customizing for your organization

Set `EXTRA_INSTRUCTIONS_DIR` to a directory containing `description.md` and/or `guide.md`; their content is
appended to the server's MCP instructions and the `slides://guide` resource, respectively. This is meant for
forks that need organization-specific instructions (e.g. a link to your team's master template, or a
client-type-specific workflow) without editing any tracked source file -- which keeps a fork's diff from
upstream limited to that one directory, so pulling in upstream updates (`git fetch upstream && git merge
upstream/main`) stays conflict-free. Unset by default; the server behaves identically to a stock checkout
when it's not set.

## Contributing

Issues and PRs welcome -- this is a young project, no formal process yet.

## License

MIT, see [LICENSE](LICENSE).
