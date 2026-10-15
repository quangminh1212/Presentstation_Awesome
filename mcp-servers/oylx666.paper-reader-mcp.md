# Paper Reader MCP

[English](README.md) | [简体中文](README.zh-CN.md)

Paper Reader MCP is a local, read-only Model Context Protocol server for evidence-first analysis of research papers and slide decks. It supports PDF, DOCX, PPT, and PPTX files while minimizing tool round trips, repeated context, and unnecessary visual tokens.

The server converts a document once, stores a content-addressed local cache, and retrieves compact evidence for an entire question batch in one call. Original PDF regions are rendered only when textual evidence is insufficient for a visual claim.

## Highlights

- **Token-efficient retrieval:** one `paper_batch_search` call handles up to 32 questions and returns a deduplicated evidence bank.
- **Long-document support:** adaptive context budgets, ranked chunks, exact numbered-reference routing, and compact wide-table serialization.
- **Selective visual evidence:** exact figure, table, or formula crops are limited to 500,000 pixels each and 1.3 million pixels per batch.
- **Evidence traceability:** results retain source page or slide references and stable evidence identifiers.
- **Local and read-only:** source documents are never modified or uploaded by the server.
- **Persistent cache:** unchanged files reuse Markdown, document structure, evidence indexes, and extracted assets.
- **Weak-model oriented:** the retrieval contract is designed to reduce planning and tool-loop errors in smaller models.

## Supported formats

| Format | Pipeline | Notes |
|---|---|---|
| PDF | Docling + TableFormer + conditional RapidOCR | Preserves page geometry for exact visual crops |
| DOCX | Docling | Extracts structured text, tables, and embedded assets |
| PPTX | Docling | Preserves slide-derived evidence and images |
| PPT | PowerPoint or LibreOffice conversion, then Docling | Requires PowerPoint on Windows or LibreOffice |

## MCP tools

| Tool | Intended use |
|---|---|
| `paper_batch_search` | Primary entry point; ingest or reuse a document and retrieve evidence for all questions in one round trip |
| `paper_search` | One focused follow-up when the batch result reports a genuine evidence gap |
| `paper_ingest` | Explicit pre-ingestion and outline generation |
| `paper_visual` | Render one exact region or a batched set of evidence crops for visual verification |

```text
local document
    -> content hash and cache lookup
    -> Docling conversion
    -> Markdown + structured evidence index + assets
    -> one batched retrieval call
    -> optional single batched visual call
    -> page/slide-grounded answer
```

## Installation

Python 3.10–3.12 is required. Python 3.10 is the tested version.

```powershell
git clone https://github.com/oylx666/paper-reader-mcp.git
cd paper-reader-mcp
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

Download the local PDF models once:

```powershell
.\.venv\Scripts\docling-tools.exe models download layout tableformer rapidocr `
  --output-dir "$env:USERPROFILE\.cache\paper-reader-models"
```

The server deliberately fails instead of silently downloading missing models during a paper-reading request. This keeps first-call latency and network behavior predictable.

## MCP configuration

Add a STDIO server entry to your MCP client, using absolute paths:

```json
{
  "mcpServers": {
    "paper-reader": {
      "command": "C:\\path\\to\\paper-reader-mcp\\.venv\\Scripts\\paper-reader-mcp.exe",
      "env": {
        "PAPER_READER_MODELS": "C:\\Users\\YOUR_NAME\\.cache\\paper-reader-models"
      }
    }
  }
}
```

Ask questions naturally and include the local document path. Compatible clients are instructed to batch questions, avoid redundant follow-ups, and request visual evidence only when needed.

## Configuration

| Variable | Default | Values / purpose |
|---|---|---|
| `PAPER_READER_CACHE` | `%LOCALAPPDATA%\paper-reader-mcp` | Cache directory |
| `PAPER_READER_MODELS` | `~\.cache\paper-reader-models` | Offline Docling model directory |
| `PAPER_READER_PDF_PIPELINE` | `standard` | `standard` or reduced-quality emergency mode `native` |
| `PAPER_READER_TABLE_MODE` | `fast` | `fast` or `accurate`; `fast` is recommended by the local A/B test |
| `PAPER_READER_OCR_MODE` | `auto` | `auto`, `always`, or `off` |
| `PAPER_READER_FORMULA_MODEL` | `off` | `off`, `codeformulav2`, or `granite_docling` |

## Evaluation results

Tests used `gpt-5.6-luna` with low reasoning effort so retrieval and tool-use weaknesses could not be hidden by a stronger model.

### Fifteen-question paper stress test

| Pipeline | Correctness | Gross input tokens | Output tokens | Traceable page coverage | Cold conversion |
|---|---:|---:|---:|---:|---:|
| **Paper Reader MCP** | **56/60 (93.33%)** | 227,113 | 3,925 | **15/15** | 22.32 s |
| Docling Markdown | 54/60 (90.00%) | **30,722** | **2,017** | 0/15 | 85.56 s |
| MarkItDown Markdown | 55/60 (91.67%) | 43,646 | 2,651 | 0/15 | **2.40 s** |
| Raw PDF workflow | 54/60 (90.00%) | 240,665 | 4,221 | **15/15** | 0 s |

The original implementation used 13 retrieval calls. The current batch-first interface reduces the intended path to one retrieval call plus, only when required, one visual call. Gross token counts above therefore describe the conservative pre-batching stress run and are not the optimized lower bound.

### TableFormer A/B on 16 manually reviewed paper tables

| Mode | Weight size | Exact table shapes | Numeric recall | Total full-document time |
|---|---:|---:|---:|---:|
| **fast** | **138.7 MB** | **16/16** | **100%** | **81.92 s** |
| accurate | 202.9 MB | 13/16 | 99.76% | 82.87 s |

The reviewed reference was initially produced by the fast model and then manually checked, so this comparison may still favor that model. A fully independent cell-level HTML corpus and TEDS evaluation would be required for an unbiased model benchmark.

Visual input tokens are not reported because the platform did not expose modality-level token usage. Pixel counts were measured instead; missing visual-token telemetry must not be interpreted as zero usage.

## Accuracy limits

- Reading order on complex multi-column pages is inferred and can be wrong.
- OCR output is unsuitable as sole evidence for exact quotations, formulas, subscripts, or very small table cells.
- Merged cells, dense tables, and chart markers should be verified against rendered source regions.
- Formula decoding is not proof of mathematical correctness; formula evidence remains visually verifiable.
- Office slide/page numbers are parser-derived and may differ from application UI numbering.
- The `native` PDF pipeline sacrifices layout, table, and OCR quality and is intended only as an emergency fallback.

## Development

```powershell
.\.venv\Scripts\python.exe -m pip install -e . pytest
.\.venv\Scripts\pytest.exe -q
```

The current suite contains 36 tests covering validation, caching, retrieval, evidence deduplication, long-context limits, table compaction, visual pixel budgets, and supported Office formats.

## Status

This is an experimental research tool. Treat its output as retrieval evidence, not as an authoritative interpretation of a paper.
