# core3-mcp-presentation

A short (~12 slide) [Marp](https://marp.app/) deck arguing that web3 should run **pre-mortems**, not
just post-mortems — and that Claude Code + the CORE3 MCP server is the practical way to do it, for
product teams, retail investors, and autonomous agents.

## Usage

```bash
npm install
npm run theme      # regenerate theme/core3.css (only needed after editing theme-src/)
npm start          # serve on http://localhost:8081 with watch
npm run build      # -> index.html
npm run pdf        # -> core3-mcp-presentation.pdf
```

Open **http://localhost:8081/presentation.md** — not `/`, which serves the stale built
`index.html` and won't live-reload.

Slides live in `presentation.md`. Speaker notes are the `<!-- ... -->` HTML comments — press `P` in
the Marp preview to see them.

Port 8081 rather than Marp's default 8080, which is occupied on this machine. Marp has no
`--port` flag; it reads the `PORT` env var, which is why the script sets it.

## Theme

`theme/core3.css` is **generated** — edit `theme-src/core3.css` and run `npm run theme`.

The theme ports core3-frontend's design tokens: **PP Mori** (headings), **Aeonik** (body),
**JetBrains Mono** (code), on the app's light palette — cream `#FFFAE6`, black text, yellow
`#FFEE00` accent, with score chips using the frontend's badge tint pairs and rating-band colors.
Sources are cited at the top of `theme-src/core3.css`.

Two constraints worth knowing before you touch it:

- **Fonts are base64-embedded** (~862 KB CSS). Marp injects theme CSS as an inline `<style>`, so
  relative `url()` paths resolve against the HTML rather than the CSS file, and Chrome blocks
  `file://` font fetches anyway. Data URIs are the only form that works in all four output modes.
  The `.otf`/`.ttf` originals in `fonts/` are copies from
  `core3-frontend/packages/ui-components/public/fonts` and exist only as input to `npm run theme`.
- **The source lives outside `theme/`** because `--theme-set ./theme` loads every `.css` in that
  directory; two files both declaring `/* @theme core3 */` collide and the theme silently fails to
  apply (symptom: everything renders as unstyled serif on white).

PP Mori and Aeonik are commercial licensed fonts. Fine for internal/company use under core3's
licence; check before publishing the built `index.html` somewhere public, since the embedded
base64 distributes the font data.

## Trying the demo live

The deck's slide 8 command is real:

```bash
claude mcp add --transport http core3 https://api.core3.io/v1/mcp
```

Then ask Claude for a pre-mortem on a project or exchange.

## Sources cited in the deck

- Daniel Kahneman — <https://en.wikiquote.org/wiki/Daniel_Kahneman>, *Thinking, Fast and Slow*
  (2011) Ch. 20 (overconfidence) and Ch. 24 (the pre-mortem, devised by Gary Klein)
- ERC-8004 — [Everstake, *ERC-8004 Explained*](https://everstake.one/resources/blog/erc-8004-explained-building-a-unified-framework-for-data-verification)
- Q2 2026 figures (67 incidents / $763.9M / 88.3% operational) —
  [Hacken, *Q2 2026 Security Report*](https://hacken.io/insights/q2-2026-security-report/)
- CORE3 — <https://core3.io/>, methodology <https://docs.core3.io>
- zondacrypto scores (solvency 0, transparency 0, security 24) —
  <https://core3.io/exchanges/zondacrypto>, read live via the CORE3 MCP
  `get_exchange_categories_scores_dynamic` tool on 2026-07-29
