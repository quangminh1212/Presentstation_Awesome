# MCP Marp Framework

This project provides a modular content presentation (MCP) framework that uses [Marp](https://marp.app) as the rendering engine. It converts structured lesson data expressed as JSON or YAML into fully-featured Marp Markdown that retains complete compatibility with the Marp CLI and VS Code extension workflows.

## Features

- Modular parser that maps lesson data to reusable slide templates while preserving Marp front-matter and metadata semantics.
- Automatic insertion of lesson content blocks (title, objectives, discussion, activity, plenary) when present in the lesson schema.
- Support for slide layouts that combine media, callouts, speaker notes, custom classes, and background options.
- Theme, size, header/footer, and pagination options surfaced through Marp-compatible front matter.
- Rendering helpers that wrap the Marp CLI to export Markdown to PPTX, PDF, or HTML with feature parity with manual exports.
- Markdown validator that ensures the generated output adheres to Marp-supported syntax before rendering.

## Installation

```bash
pip install -e .
```

The CLI expects the [Marp CLI](https://github.com/marp-team/marp-cli) (`marp`) to be available on your `PATH`. Install it via `npm install -g @marp-team/marp-cli` or run through `npx`.

## CLI Usage

```bash
# Convert structured lesson data into Marp Markdown
mcp-marp parse examples/pshe.json -o build/pshe.marp.md

# Render an existing markdown file into PPTX, PDF, and HTML
mcp-marp render build/pshe.marp.md --format pptx --format pdf --format html

# Parse and immediately render
mcp-marp build examples/pshe.json --out build/pshe.marp.md --format pptx --format pdf
```

Run `mcp-marp --help` for the full command reference.

## Development

- `src/mcp_marp/parser.py` contains the main `LessonParser` class that converts structured data to Markdown.
- `src/mcp_marp/validator.py` adds a syntax validation layer before rendering.
- `src/mcp_marp/cli.py` exposes parsing and rendering operations through the command line.

Example templates covering different Marp themes and educational scenarios are stored under `examples/`. Copy `src/mcp_marp/templates/lesson.css` next to your generated Markdown (or reference it from Marp front matter) to enable the custom column layouts.
