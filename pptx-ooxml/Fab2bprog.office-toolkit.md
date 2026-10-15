# office-toolkit

[![Crates.io](https://img.shields.io/crates/v/office-toolkit.svg)](https://crates.io/crates/office-toolkit)
[![docs.rs](https://docs.rs/office-toolkit/badge.svg)](https://docs.rs/office-toolkit)
[![CI](https://github.com/Fab2bprog/office-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Fab2bprog/office-toolkit/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Word, Excel, and PowerPoint files — read, written, and edited from pure Rust, through one library built on consistent, shared conventions.**

No Microsoft Office installation, no COM automation, no VBA, no shelling out to LibreOffice, no unsafe FFI bindings to a C library. Just a `Cargo.toml` line and typed Rust structs that map directly onto a document, a workbook, or a presentation.

```rust
use office_toolkit::prelude::*;
use office_toolkit::SaveToFile;

let document = Document::new().with_paragraph(Paragraph::with_text("Hello, world!"));
document.save_to_file("hello.docx")?;
# Ok::<(), office_toolkit::Error>(())
```

That's a real, valid `.docx` file that opens in Word — five lines, no boilerplate.

## Why office-toolkit?

**Shared conventions, three formats.** Word, Excel, and PowerPoint each keep their own types (`Document`, `Workbook`, `Presentation`) because their content genuinely differs — but they share the same DrawingML shapes, the same chart model, the same package format, and the same builder-style API (`with_*` methods, `Option`/`Result`) underneath. `office-toolkit` models that shared structure once and reuses it, so if you already know how to add an image to a slide, adding one to a document or a worksheet feels familiar rather than foreign. You're not learning three unrelated libraries with three different conventions.

**Read *and* write, not just one direction.** A lot of tooling in this space only goes one way — generate a report, or parse a spreadsheet, but not both. Every format here supports full round-trips: open a real file, inspect or change it, save it back out, and nothing you didn't touch gets silently dropped or corrupted.

**Tested against real Office files, not just itself.** Beyond the round-trip tests every feature ships with, the test suite also opens actual `.docx`/`.xlsx`/`.pptx` files produced by real Word/Excel/PowerPoint installations and checks the result — the kind of real-world formatting quirks a library that only ever tests against its own output tends to miss.

**A genuinely original implementation.** No code copied from another OOXML library, and no dependency on any crate that itself understands Word/Excel/PowerPoint's file formats — every line that parses or writes WordprocessingML, SpreadsheetML, PresentationML, DrawingML, or embedded charts is this project's own. The only external dependencies are generic, format-agnostic infrastructure: an XML tokenizer, a ZIP reader/writer, error-enum boilerplate (see [`docs/About_dependencies.md`](docs/About_dependencies.md) for the full, honest list).

**Idiomatic Rust, not a C library wearing a trench coat.** `Option`/`Result` everywhere instead of null checks or exceptions, builder methods (`with_*`) instead of mutating a dozen fields by hand, and no `unsafe` in the format-parsing logic. Pick only the formats you need — `office-toolkit`'s Word/Excel/PowerPoint support are each an opt-in Cargo feature, so a project that only ever touches spreadsheets doesn't compile a line of Word or PowerPoint code.

**Cross-platform by construction.** Pure Rust, no OS-specific automation APIs — CI builds and tests every commit on Linux, macOS, and Windows.

## Status

Word, Excel, and PowerPoint (the modern Open XML formats) are functional today — see the feature lists below, or the full [`docs/API_Reference_docx.md`](docs/API_Reference_docx.md) / [`_xlsx.md`](docs/API_Reference_xlsx.md) / [`_pptx.md`](docs/API_Reference_pptx.md) for exactly what's covered.

## Quick tour

Three formats, three equally short examples. Each one writes a real file and reads it back to prove it round-trips correctly.

**Word:**

```rust
use office_toolkit::prelude::*;
use office_toolkit::{OpenFile, SaveToFile};

let document = Document::new().with_paragraph(Paragraph::with_text("Hello, world!"));
document.save_to_file("hello.docx")?;

let reopened = Document::open_file("hello.docx")?;
println!("{:?}", reopened.paragraphs().next().map(|p| p.text()));
# Ok::<(), office_toolkit::Error>(())
```

**Excel:**

```rust
use office_toolkit::excel::Sheet;
use office_toolkit::prelude::*;
use office_toolkit::{OpenFile, SaveToFile};

let workbook = Workbook::new().with_sheet(Sheet::new("Sheet1").with_row(Row::new().with_text("Hello, world!")));
workbook.save_to_file("hello.xlsx")?;

let reopened = Workbook::open_file("hello.xlsx")?;
println!("{:?}", reopened.sheets[0].rows[0].cells[0].value);
# Ok::<(), office_toolkit::Error>(())
```

**PowerPoint:**

```rust
use office_toolkit::drawing::{ShapeProperties, TextBody, TextParagraph, TextRun, Transform2D};
use office_toolkit::powerpoint::{AutoShape, Shape};
use office_toolkit::prelude::*;
use office_toolkit::SaveToFile;

let text_box = AutoShape::new(2, "Hello box")
    .with_properties(ShapeProperties::new().with_transform(Transform2D::new().with_extent(7_772_400, 1_200_150)))
    .with_text_body(TextBody::new().with_paragraph(TextParagraph::new().with_run(TextRun::text("Hello, world!"))));

let presentation = Presentation::new().with_slide(Slide::new().with_shape(Shape::AutoShape(text_box)));
presentation.save_to_file("hello.pptx")?;
# Ok::<(), office_toolkit::Error>(())
```

**Opening a file without knowing its format ahead of time:**

```rust
let opened = office_toolkit::open("mystery-file")?; // sniffs .docx/.xlsx/.pptx from the package contents
opened.save_to_file("resaved")?;
# Ok::<(), office_toolkit::Error>(())
```

More complete, runnable examples for every feature below live in [`crates/office-toolkit/examples/`](crates/office-toolkit/examples/) — tables, images, charts, themes, protection, conditional formatting, and more, one focused example file per topic.

## What you can do with each format

**Word (`.docx`)** — building documents from paragraphs, runs, and tables; character formatting (bold, italic, color, font); paragraph formatting (alignment, indentation, spacing, borders); page/column/line breaks and dynamic fields; images; embedded charts; hyperlinks and bookmarks; comments; footnotes and endnotes; tables; named styles; bulleted and numbered lists; structured document tags (content controls); themes; document properties; page setup; document protection.

**Excel (`.xlsx`)** — workbooks, sheets, and cells; every cell value kind (text, numbers, formulas, dates, rich text); character formatting; borders and fills; conditional formatting; data validation; named ranges; columns/rows/frozen panes/grouping; autofilter and sorting; printing; protection; hyperlinks and cell comments; structured tables; calculation settings; scenarios, external links, ignored errors; sheet visibility and views; document properties; pictures and embedded charts.

**PowerPoint (`.pptx`)** — presentations and slides; autoshapes, text boxes, and placeholders; position/size/rotation and shape outlines; fills and colors; lines/strokes; visual effects (shadow, glow, reflection, soft edge); rich text inside shapes; pictures; video and audio; embedded charts; grouped shapes; connectors; tables; slide comments; themes; document properties; embedded fonts.

The exact method to call for each of these lives in the per-format API reference docs linked above.

## Usage

Add the facade crate — it re-exports Word, Excel, and PowerPoint support behind a single `use`:

```toml
[dependencies]
office-toolkit = "1.0"
```

By default you get all three formats. If you only need one or two, turn off the default feature and opt in — this keeps compile times down and means a spreadsheet-only tool never pulls in Word or PowerPoint code:

```toml
[dependencies]
office-toolkit = { version = "1.0", default-features = false, features = ["excel"] }
```

```rust
use office_toolkit::prelude::*;
use office_toolkit::SaveToFile;

// Build a minimal Word document and save it. `Document` and `Paragraph`
// both come straight from the prelude; `save_to_file` needs its own
// `SaveToFile` trait imported, like any trait method.
let document = Document::new().with_paragraph(Paragraph::with_text("Hello, world!"));
document.save_to_file("hello.docx")?;

// Open any .docx/.xlsx/.pptx without knowing its format ahead of time.
let opened = office_toolkit::open("hello.docx")?;
# Ok::<(), office_toolkit::Error>(())
```

## Workspace layout

This is a Cargo workspace, split into focused crates so consumers only compile what they need:

| Crate | Role |
|---|---|
| `xml-core` | Low-level generic XML reading/writing (built on `quick-xml`) |
| `opc` (published as `opc-ooxml`) | Open Packaging Conventions: ZIP container, `[Content_Types].xml`, relationships |
| `drawing` (published as `drawingml`) | Shared DrawingML (shapes, fills, lines, text bodies, images) used by all three formats |
| `chart` | Shared embedded charts (ChartML) used by Excel, Word, and PowerPoint |
| `word-ooxml` | `.docx` reading and writing |
| `excel-ooxml` | `.xlsx` reading and writing |
| `powerpoint-ooxml` | `.pptx` reading and writing |
| `office-toolkit` | Facade crate — single entry point re-exporting the format crates (see Usage above; this is the crate most users should depend on) |

Most users should only ever depend on `office-toolkit`; the other crates exist so it can be assembled from focused, independently testable pieces.

## Documentation

- [`docs/Architecture.md`](docs/Architecture.md) — how the workspace is put together: crate dependency graph, the reading/writing pipeline, the facade's feature flags and prelude, testing setup.
- [`docs/API_Reference_docx.md`](docs/API_Reference_docx.md) / [`_xlsx.md`](docs/API_Reference_xlsx.md) / [`_pptx.md`](docs/API_Reference_pptx.md) — per-feature reference for each format: what each feature does and the exact code to call it.
- [`docs/About_dependencies.md`](docs/About_dependencies.md) — every external crate this project depends on and why.
- [`CHANGELOG.md`](CHANGELOG.md) — release history.

## License

Licensed under the [MIT license](LICENSE).
