# Contributing to Presentstation_Awesome

Thanks for helping grow the list of AI / agent / CLI / web tools for building
presentations, slides and PowerPoint decks.

## What belongs here

Repositories that help create or manipulate **presentations, slides, or PowerPoint
decks** using AI, agents, MCP servers, CLIs, or web frameworks. This includes:

- AI presentation generators (end-to-end)
- MCP servers for PowerPoint / Google Slides / web decks
- Agent skills, editor plugins and extensions
- HTML slide frameworks (reveal.js, Slidev, impress.js, ...)
- Markdown → Slides tooling (Marp, Quarto, Typst/Touying, Pandoc, Org, RISE)
- PPTX / OOXML libraries and CLI converters
- Themes, templates and curated awesome-lists
- Knowledge bases, datasets and agent frameworks for presentations

## What does NOT belong here

- Image carousels / sliders / "awesome slider" UI components
- Anki / flashcard decks
- Trading-card / game decks (MTG, poker, stream-deck macros, ...)

## How to add a repository

1. Open an issue or pull request.
2. Add the entry under the correct category, sorted by star count (highest first):

   `- [owner/repo](https://github.com/owner/repo) — ★ N — One-line description.`

3. Keep descriptions short (<=160 chars) and English.
4. If you are changing the dataset, update `data/repos.json` as well, or note it
   in the PR and a maintainer will regenerate.

## Regenerating

The README is generated from `data/repos.json` with:

```powershell
python research/gen_readme.py
```

Thank you!
