# RustyPPTX

A high-performance PPTX parser written in Rust. Extracts structured, semantically typed text, metadata, and images from PowerPoint files using parallel slide processing.

## Features

- **Semantic element types** — classifies text as Title, Subtitle, Paragraph, or ListItem with indent depth
- **Heading detection** — identifies title/subtitle placeholder shapes from slide XML
- **Bullet/list detection** — detects `buChar`, `buAutoNum`, `buBlip` markers with nesting depth
- **Markdown output** — renders presentations as clean Markdown with YAML front matter
- **Parallel processing** — slides are parsed concurrently using Rayon
- **Image extraction** — extracts images from `ppt/media/` and maps them to the correct slide via relationship files
- **Metadata parsing** — title, author, dates, application info from `docProps/`
- **Fault tolerant** — corrupted slides are skipped; partial documents are returned
- **Triple output** — plain text, JSON, or Markdown

## Installation

```sh
cargo install --path .
```

Or add as a dependency:

```toml
[dependencies]
rustypptx = { path = "." }
```

## CLI Usage

```sh
# Plain text output (with element type annotations)
rustypptx presentation.pptx

# JSON output (includes element_type and depth fields)
rustypptx presentation.pptx --json

# Markdown output
rustypptx presentation.pptx --markdown

# Extract images to a directory
rustypptx presentation.pptx --output-dir ./images

# Combine flags
rustypptx presentation.pptx --markdown --output-dir ./images
```

### Markdown Output Example

```markdown
---
title: "Q4 Review"
author: "Jane Doe"
created: "2024-12-01T10:00:00Z"
---

## Slide 1: Quarterly Results

### Financial Overview

Revenue grew 15% year-over-year.

- North America: $12M
  - US: $9M
  - Canada: $3M
- Europe: $8M

![chart.png](ppt/media/chart.png)

---

## Slide 2: Next Steps

Action items for Q1.

- Expand into APAC
- Hire 20 engineers
```

## Library Usage

```rust
use std::path::Path;
use rustypptx::ElementType;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let doc = rustypptx::parse_pptx(Path::new("presentation.pptx"))?;

    // Markdown output
    println!("{}", doc.to_markdown());

    // Or work with structured data
    for slide in &doc.slides {
        for elem in &slide.text_elements {
            match elem.element_type {
                ElementType::Title => println!("# {}", elem.text),
                ElementType::Subtitle => println!("## {}", elem.text),
                ElementType::ListItem => {
                    let indent = "  ".repeat(elem.depth.unwrap_or(0) as usize);
                    println!("{}- {}", indent, elem.text);
                }
                ElementType::Paragraph => println!("{}", elem.text),
            }
        }
    }

    Ok(())
}
```

You can also parse from bytes directly:

```rust
let bytes = std::fs::read("presentation.pptx")?;
let doc = rustypptx::parse_pptx_bytes(&bytes)?;
```

## JSON Output

The JSON output includes semantic type information for each text element:

```json
{
  "element_type": "list_item",
  "text": "Sub-bullet item",
  "depth": 1
}
```

Element types: `title`, `subtitle`, `paragraph`, `list_item`. The `depth` field is only present for `list_item` elements (0-based indent level).

## Project Structure

```
src/
├── lib.rs            # Public API
├── main.rs           # CLI (clap)
├── error.rs          # Error types
├── model.rs          # PptxDocument, Slide, TextElement, ElementType, ImageRef
├── parser.rs         # Orchestrator — unzip, parallel dispatch
├── metadata.rs       # docProps/core.xml & app.xml parsing
├── relationships.rs  # .rels file parsing (rId → media path)
├── slides.rs         # Slide XML parsing — text, placeholders, bullets, images
├── markdown.rs       # Markdown rendering
└── images.rs         # Media file extraction from archive
```

## How It Works

1. The entire PPTX (ZIP archive) is read into memory
2. Metadata is parsed from `docProps/core.xml` and `docProps/app.xml`
3. All media files under `ppt/media/` are extracted
4. Slide XML and their `.rels` files are loaded
5. Slides are parsed **in parallel** via Rayon — each worker runs its own `quick-xml` reader
6. Placeholder shapes (`<p:ph type="title"/>`, etc.) are detected to classify text semantically
7. Bullet markers (`buChar`, `buAutoNum`, `buBlip`) and indent levels are tracked per paragraph
8. Image relationship IDs (`r:embed="rId2"`) are resolved to archive paths and matched with extracted media bytes

## Running Tests

```sh
cargo test
```

## License

MIT
