# Helx

**The universal artifact runtime for AI agents.** One engine that reads, creates, edits, validates, diffs and renders the formats agents actually work with — DOCX, XLSX, PPTX, PDF, Markdown, HTML, CSV — plus charts, diagrams, templates, cross-format conversion and CSV data ops. Exposed three ways:

- **CLI** — `helx` for humans and shell scripts
- **MCP server** — 20 tools over stdio for AI agents (Claude, Cursor, etc.)
- **TypeScript SDK** — a clean `Artifact` facade for your own code

[![npm version](https://img.shields.io/npm/v/helx?color=2f81f7&label=npm)](https://www.npmjs.com/package/helx)
[![license](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

```
one model, every file
create → read → edit → save → validate → diff → render → convert
```

## Visual gallery

Every artifact below was **created and edited by Helx itself**, then previewed by Helx. Click any card to open the file.

| | | |
|---|---|---|
| ![DOCX report](examples/demo/previews/report-card.png) | ![XLSX sales](examples/demo/previews/sales-card.png) | ![PPTX deck](examples/demo/previews/investor-deck-card.png) |
| ![PDF quarterly](examples/demo/previews/quarterly-card.png) | ![Markdown playbook](examples/demo/previews/playbook-card.png) | ![HTML landing](examples/demo/previews/landing-card.png) |
| ![CSV customers](examples/demo/previews/customers-card.png) | ![DOCX letter (template merge)](examples/demo/previews/letter-card.png) | ![Diagram](examples/demo/previews/diagram-workflow.png) |

Charts generated with `helx chart`:

![Revenue by region](examples/demo/previews/chart-revenue-bar.png) ![Trend](examples/demo/previews/chart-trend-line.png) ![Mix](examples/demo/previews/chart-mix-pie.png)

The gallery is produced by `npx tsx scripts/make-gallery.ts` — it opens every demo file through the SDK and rasterizes a styled SVG preview to PNG with `@resvg/resvg-js`.

## Why Helx over OfficeCLI

[OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) is a strong Word/Excel/PPT editor for AI agents. Helx goes further:

| Capability | Helx | OfficeCLI |
|---|---|---|
| **Formats** | DOCX, XLSX, PPTX, **PDF, Markdown, HTML, CSV** | Word, Excel, PPT only |
| **Cross-format conversion** | `helx convert report.docx report.md` — DOCX↔MD/HTML/PDF, XLSX↔CSV/HTML/MD, PPTX→MD/HTML/DOCX, PDF→MD/HTML/DOCX, CSV↔XLSX | no |
| **Charts & diagrams** | `helx chart` (bar/line/pie/donut/area/scatter), `helx diagram` (mermaid-style flowcharts) | no |
| **Templates** | `{{var}}`/`{{#each}}`/`{{#if}}` + in-place **DOCX** merge | DOCX merge only |
| **CSV data ops** | `analyze`, `filter`, `sort`, `group`, `aggregate`, `profile`, `dedupe`, `clean` | no |
| **PDF** | create, extract text, merge, split | no |
| **Renders for agent vision** | DOCX/XLSX/CSV→HTML, PPTX→SVG, PDF→text, MD→HTML, charts→SVG | render → PNG |
| **Interfaces** | CLI + MCP (20 tools) + TypeScript SDK | CLI + MCP |
| **Agent paths** | uniform `/p[2]`, `/sheet[X]/cell[C3]`, `css:.hero`, ... across **all** formats | per-format |
| **Validation & diff** | `validate` + semantic `diff` on every engine | no |

Helx also ships `stat` (document statistics) and `move` (reorder paragraphs/rows/slides/shapes) across every interface.

## Install

```bash
npm install -g helx        # CLI + MCP server
# or
npm install helx           # SDK for your own TypeScript/JavaScript project
```

Then `helx --help` or add the MCP server to your AI client:

```json
{
  "mcpServers": {
    "helx": { "command": "helx", "args": ["mcp"] }
  }
}
```

That's it — any AI model or agent (Claude, Cursor, Cline, LangChain, custom
scripts) can create, read, edit and render real office and web documents.

## Build from source

```bash
git clone https://github.com/Asno-dev/Helx.git
cd Helx
npm install
npm run build        # tsc → dist/
npm test             # 71 integration checks (tsx test/smoke.ts)
```

Node >= 18 (dynamic ESM import requires >= 12.20; verified on Node 22).

## Quick start (CLI)

```bash
# Create a DOCX from a JSON spec (type inferred from the extension)
helx create report.docx '{"title":"Q3 Report","paragraphs":["Revenue grew 20% to $52k."],"tables":[{"headers":["Metric","Value"],"rows":[["ARR","4.2M"]]}]}'

# Inspect the structure as a path-addressed tree
helx inspect report.docx

# Read / write a single value via an agent path
helx get report.docx "/p[1]"
helx set report.docx "/table[0]/row[1]/cell[1]" "4.5M"

# Insert / remove / move, then validate and render to HTML for a visual check
helx insert report.docx "/p[2]" '{"text":"New paragraph","style":"Heading 2"}'
helx remove report.docx "/p[4]"
helx move report.docx "/p[2]" "/p[5]" --after
helx stat report.docx
helx validate report.docx
helx render report.docx --out report-preview.html

# Cross-format conversion (any direction, any engine)
helx convert report.docx report.md
helx convert report.md report.pdf
helx convert sales.xlsx sales.csv
helx convert deck.pptx deck.md

# Spreadsheets
helx create data.xlsx '{"sheet":"Revenue","rows":[["Quarter","Amount"],["Q1","10"]]}'
helx get data.xlsx "/sheet[Revenue]/cell[B2]"
helx analyze data.csv
helx filter data.csv '{"col":"score","op":"gt","value":80}'

# Decks
helx create deck.pptx '{"title":"Investor Deck","subtitle":"Q3 2026","bullets":["Market size: $10B"]}'
helx get deck.pptx "/slide[0]/shape[1]"

# PDFs (create via model; merge/split for structure)
helx create a.pdf '{"title":"Doc A","sections":[{"heading":"Intro","text":"Hello."}]}'
helx merge merged.pdf a.pdf b.pdf
helx split page1.pdf merged.pdf --pages 1
helx extract merged.pdf

# Charts, diagrams, templates
helx chart '{"type":"bar","labels":["Q1","Q2"],"values":[10,12]}' --out chart.svg
helx diagram 'graph TD; A[Start] --> B[End];' --out diagram.svg
helx template 'Hello {{name}}' '{"name":"Ada"}'

# Run the MCP server (for AI agents)
helx mcp
```

## Agent paths

Every artifact exposes a stable, path-addressed tree so agents can read/write any value:

| Format   | Example paths |
|----------|---------------|
| DOCX     | `/p[2]`, `/p[1]/text`, `/table[0]/row[1]/cell[0]` |
| XLSX     | `/sheet[Revenue]/cell[C24]`, `/sheet[0]/row[3]` |
| PPTX     | `/slide[0]/shape[1]`, `/slide[0]/shape[2]/text` |
| PDF      | `/page[0]`, `/page[0]/text` |
| Markdown | `/heading[0]`, `/p[2]` |
| HTML     | `css:h1`, `css:.summary > p` |
| CSV      | `/row[3]/cell[1]` |

`set`, `insert`, `remove` and `move` mutate the model and `save()` round-trips it back to the file.

## Cross-format conversion

`convert` walks a real content model — it is **not** string surgery:

| From \ To | DOCX | XLSX | PPTX | PDF | MD | HTML | CSV |
|---|---|---|---|---|---|---|---|
| DOCX | — | | | ✔ | ✔ | ✔ | |
| XLSX | | — | | | ✔ | ✔ | ✔ |
| PPTX | ✔ | | — | | ✔ | ✔ | |
| PDF | ✔ | | | — | ✔ | ✔ | |
| MD | ✔ | | | ✔ | — | ✔ | |
| HTML | ✔ | | | ✔ | ✔ | — | |
| CSV | | ✔ | | | ✔ | ✔ | — |

```ts
const md = await Artifact.create('markdown', { root: { children: [] } });
await md.insert('/node', { type: 'heading', depth: 1, text: 'Hello' });
const docx = await md.convertTo('docx');   // real DOCX bytes
const html = await docx.convertTo('html');
```

## MCP server

`helx mcp` runs a Model Context Protocol server over stdio. It exposes 20 tools:

`create_artifact`, `inspect`, `get`, `set`, `insert`, `remove`, `move`, `convert`, `stat`, `render`, `validate`, `diff`, `merge_pdf`, `split_pdf`, `extract`, `analyze_csv`, `filter_csv`, `chart`, `diagram`, `template`

Tools are filesystem-path based — the agent passes a file path and a JSON value, and the server reads, edits, saves, or renders the artifact. Register it in a client like Claude Desktop:

```json
{
  "mcpServers": {
    "helx": { "command": "node", "args": ["/path/to/helx/dist/cli/index.js", "mcp"] }
  }
}
```

## TypeScript SDK

```ts
import { Artifact, chartToSvg, dataFilter, renderTemplate } from 'helx';

// Create, edit, save
const doc = await Artifact.create('docx', {
  title: 'Report',
  paragraphs: ['Revenue grew 20% to $52k.'],
  tables: [{ headers: ['Metric', 'Value'], rows: [['ARR', '4.2M']] }],
});
await doc.set('/p[0]/text', 'Updated headline');
await doc.insert('/p[1]', { text: 'Inserted paragraph' });
const bytes = await doc.save();
await fs.writeFile('report.docx', bytes);

// Open any file, regardless of format
const art = await Artifact.open('data.xlsx', buffer);
console.log(await art.get('/sheet[Revenue]/cell[B2]'));
console.log(await art.inspect());

// Convert to another format, get stats, move elements
const md = await art.convertTo('markdown');
console.log(await art.stat());
await art.move('/sheet[Revenue]/row[3]', '/sheet[Revenue]/row[1]', 'before');

// Validation and diff
console.log(await art.validate());   // { status, issues[] }
console.log(await art.diff(other));  // DiffEntry[]

// Generator utilities
const svg = chartToSvg({ type: 'pie', labels: ['A', 'B'], values: [3, 7] });
const rows = dataFilter(data, { col: 'score', op: 'gt', value: 80 });
const out = renderTemplate('Hi {{name}}', { name: 'Ada' });
```

Also exported: `convertArtifact`, `canConvert`, `mergePdfs`, `splitPdf`, `dataProfile`, `dataSort`, `dataAggregate`, `dataDedupe`, `dataClean`, `parseDiagram`, `diagramToSvg`, `renderDocxTemplate`, `detectType`, `engineForFile`, `registerEngine`, `engines`.

## Architecture

```
src/
  core/
    types.ts        # shared model contracts (Engine, ArtifactModel, ValidationReport, ...)
    base.ts         # BaseEngine with typed dispatch for set/insert/remove/move
    paths.ts        # agent-path parser (/p[0], /sheet[X], css:..., /row[n]/cell[n])
    utils.ts        # LCS diff, diffText/diffSeqMerged, HTML document shell
    convert.ts      # cross-format converter (content-model based, 19 directions)
    index.ts        # engine registry + Artifact facade (create/open/save/...)
    engines/
      docx.ts       # paragraphs, heading styles, tables
      xlsx.ts       # sheets, cells, formula read-back
      pptx.ts       # slides, shapes, text boxes
      pdf.ts        # create (pdfkit), extract text (pdfjs-dist), merge/split (pdf-lib)
      markdown.ts   # remark/rehype round-trip
      html.ts       # cheerio DOM editing + css: selectors
      csv.ts        # rows + data ops: profile/filter/sort/group/aggregate/clean/dedupe
      chart.ts      # SVG charts (bar, line, pie, donut, area, scatter, grouped bar, stacked bar)
      diagram.ts    # mermaid-style flowchart → SVG
      template.ts   # {{var}}/{{#each}}/{{#if}} + in-place DOCX placeholder merge
  cli/index.ts      # helx CLI (commander)
  mcp/index.ts      # MCP stdio server (20 tools)
  sdk/index.ts      # public package surface
scripts/make-gallery.ts   # README gallery generator
examples/demo/            # all demo files created by Helx itself
```

Each file engine implements one contract: `read(bytes) → model`, `write(model) → bytes`, plus `create(spec)`, `get/set/insert/remove/move(path)`, `inspect()`, `validate()`, `diff(other)`, `render()`. The `Artifact` facade keeps the original bytes so immutable formats (PDF) can still be round-tripped after edits to other formats.

## Notes & design decisions

- **PDF is immutable by model**: text extraction is read-only (`pdfjs-dist`; pdf-parse was dropped because its bundled pdf.js 2.x cannot parse pdfkit output). Structure operations use `pdf-lib`: `mergePdfs` and `splitPdf`.
- **Renders to HTML** for the agent's vision loop: DOCX/XLSX/CSV → HTML tables, PPTX → per-slide SVG, PDF → per-page text, Markdown → HTML, charts/diagrams → SVG.
- `helx chart`, `helx diagram`, `helx template` are generator utilities; they are not registered file engines.
- **Conversion is model-based**: converters read each format's real model (`DocxModel`, `XlsxModel`, ...) and produce another engine's spec, so `convert` preserves structure rather than pasting raw text.

## License

Apache-2.0 — see [LICENSE](LICENSE).

## Contributing

Bug reports, feature requests and pull requests are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the dev workflow, conventions and
Code of Conduct.