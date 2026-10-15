# md2pre

> Markdown → Presentation. One command, one HTML file per slide.

[中文](./README-zh.md)

live demo deriving from showcase.md: https://woyeyao.github.io/md2pre/showcase/index.html

A lightweight Python tool that converts Markdown files into Material Design HTML presentations. Each slide is an independent HTML file — edit freely, present anywhere.

There are many Markdown-based presentation tools available. What makes md2pre unique:

1. Stable output with a simple structure — The script processes Markdown in a specific, well-defined format, producing consistent results. The project structure is straightforward and easy to modify, making it simple to personalize and extend.
2. Token-efficient and fast — Minimal token usage, quick conversion.
3. No agent required — Users can directly use a web-based AI with the prompt template from prompt.md to generate properly formatted Markdown, then convert it to HTML slides. No complex agent setup needed.
4. Ideal for quick, informal presentations — Perfect for low-stakes class group presentations, lab group quick-share sessions, and similar use cases where you need slides fast without fuss.

## Design

- **Material Design** — Google brand colors, elevation shadows, clean typography
- **High density** — every pixel counts; text, tables, images, code, and math share the same stage
- **Dark / Light** — one click to toggle, URL-parameter driven, zero flicker
- **Serif titles, sans-serif body** — Noto SC for seamless Chinese-English typesetting

## Dependencies

```
pip install mistune jinja2 click pygments Pillow
```

| Package | Role |
|---------|------|
| mistune | Markdown → AST |
| jinja2 | HTML templating |
| click | CLI |
| pygments | Code highlighting |
| Pillow | Image orientation detection |

Math rendering uses [KaTeX](https://katex.org/) via CDN — **requires internet connection**. No local install needed. Slides without math formulas load no external resources.

## Workflow

1. Use `prompt.md` as a system prompt for your AI assistant to generate presentation-ready Markdown
2. Save the output as a `.md` file
3. Run the converter:

```bash
python md2pre.py your-slides.md
```

4. Open `your-slides/index.html` in a browser

Output structure:

```
your-slides/
  index.html        # open this
  style.css
  main.js
  slides/
    slide-000.html
    slide-001.html
    ...
  images/
```

## Markdown Syntax

```markdown
# Title Slide

Presenter Name · year

## Chapter Slide

Optional subtitle text for the chapter

### Content Slide Heading

#### Subsection — auto multi-column when 2–4

Body text with **bold** and `code`.

> Blockquotes render as green note cards.

| Col A | Col B |
|-------|-------|
| 1     | 2     |

Inline math $E = mc^2$, display math:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

![image](path/to/image.png)

[red]red tag[/red] and [yellow]yellow tag[/yellow]
```

- `#` → title slide (centered, four-color bar; first paragraph below as subtitle)
- `##` → chapter slide (left border accent; first paragraph below as subtitle)
- `###` → content slide heading (top-left, blue underline)
- `####` → subsection (red → yellow → green rotation)
- `>` → green rounded card
- Images: landscape centered, portrait floats right
- `[red]...[/red]` / `[yellow]...[/yellow]` → color tags

## Navigation

| Key | Action |
|-----|--------|
| `←` `↑` `PageUp` | Previous slide |
| `→` `↓` `Space` `PageDown` | Next slide |
| `Home` / `End` | First / Last |
| `F` | Toggle fullscreen |

Click left 15% edge → previous, right 15% → next.

## License

MIT
