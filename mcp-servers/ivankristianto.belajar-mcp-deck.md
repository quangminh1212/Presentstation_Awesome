# Otomasi AI Agent: Kelola Website dan Hosting pakai MCP

Slides for a Kelas Tanya DomaiNesia webinar on 24 September 2026, on driving a
WordPress site and cPanel hosting through an MCP server instead of clicking around
a control panel.

Live deck: <https://belajarweb.cloud/belajar-mcp/>

27 slides, in Indonesian, built with [Slidev](https://sli.dev) on the `apple-basic`
theme. The deck runs 45 minutes across five segments. Press `d` during the talk to
switch between the light and dark colour schemes.

## Running it

```bash
npm install
npm run dev      # http://localhost:3030
```

`npm run build` produces a root-based static deck in `dist/`. The live deck is served
from a subdirectory, so that build needs `--base /belajar-mcp/`. See Deploying below.

`npm run export` needs `playwright-chromium`, which is not a declared dependency.
Install it first.

## What is where

| Path | What it is |
|---|---|
| `slides.md` | The whole deck. Slides split on `---`, per-slide YAML frontmatter |
| `components/` | Vue components auto-registered by filename: `AgentLoop`, `IntegrationMesh`, `AccessLevel`, `Prompt` |
| `styles/index.css` | The only stylesheet. Accent and tone colours, `--deck-bg` per scheme |
| `setup/mermaid.ts` | Mermaid theming. Separate from the CSS because Slidev renders mermaid in a shadow root |
| `docs/` | Preparation material in English. Start at `docs/README.md` |
| `deploy/.htaccess` | Apache SPA rewrite, copied into the build |

`docs/outline.md` holds the segment timings the deck is built against. Change the deck
and the outline together.

## Deploying

Pushing to `main` runs `.github/workflows/build.yml`: it builds with
`--base /belajar-mcp/`, copies `deploy/.htaccess` into the output, and force-pushes
the result to the `deploy` branch as a single commit.

The hosting side pulls that branch as a tarball:

```bash
curl -sSL https://codeload.github.com/ivankristianto/belajar-mcp-deck/tar.gz/refs/heads/deploy -o deck.tgz
tar xzf deck.tgz -C /home/belaj255/public_html/belajar-mcp --strip-components=1
```

That pull is still manual. `--strip-components=1` is required, since GitHub wraps
tarball contents in a `<repo>-<branch>/` directory.

Changing the base path means updating the workflow, `deploy/.htaccess`, the extraction
target, and `netlify.toml` and `vercel.json` together. Those last two build without
`--base` and so are only correct for a deploy at the domain root.

The repo carries a `deploy-to-domainesia` skill in `.claude/skills/` with the full
procedure, including why files have to reach that server by a pull rather than an
upload.
