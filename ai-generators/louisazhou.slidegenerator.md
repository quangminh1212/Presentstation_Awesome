# Slide Generator

Create native PowerPoint and Google Slides directly from Markdown or Python notebooks — and stay focused on your content, not formatting tweaks.

Slide Generator renders your content in a real browser to understand layout, then reproduces it as native slide elements. Tables, columns, images, and speaker notes are handled automatically, so final adjustments are minimal.

Status
- Pre‑release. Packaging as a pip‑installable distribution is our top priority. See [ROADMAP.md](ROADMAP.md) for details. Until the first release is published to PyPI, please install from source (below).

Installation
- From PyPI (planned): `pip install slide-generator`
- From source (today):
  - `python -m venv .venv && source .venv/bin/activate`
  - `pip install -r requirements.txt`

## Features

- Content‑first authoring → native, editable decks (PPTX/Google Slides), not flattened images
- One theme for the whole deck: fonts, colors, sizes — no per‑slide fixes
- Predictable placement: what you preview is what you get in slides
- Native tables and charts remain editable; images scale intelligently to available space
- Notebook workflows: reference chart functions and DataFrames directly — no export/paste

## Why Slide Generator

If you’ve used LaTeX Beamer, you know the ideal: focus on content and let the system handle layout. Slide Generator brings that content‑first experience to PowerPoint/Google Slides while keeping everything editable.

- **Traditional tools fall short.** Most Markdown‑to‑PPT converters export static images or guess at where to place elements. You lose the ability to edit text or tables, and you spend hours nudging images and captions back into place.
- **Stop wrestling with layout math.** Low‑level libraries like `python‑pptx` let you control every pixel—but only if you write dozens of lines of layout code for each slide. Every deck becomes a one‑off script with brittle coordinates and font definitions.
- **A content‑first workflow.** Write slides in simple Markdown (with optional Jinja for notebooks) and focus on the story. Slide Generator measures your content in a real browser, applies your theme, and recreates native PPTX/Slides. Tables remain editable with per‑cell styling, figures scale to fit, and multi‑column layouts stay predictable. Your deck looks exactly like the preview, and you stay focused on analysis rather than formatting.

## Quick Demos

Short examples of the syntax you write and the result you get. 

Find more recipes in [docs/cookbook.pdf](docs/cookbook.pdf) and full decks under [output/](output/).

### Columns with mixed content

```markdown
# Two-column slide 
:::columns

:::column

### 📋 Project Status Table

| Task | Owner | Progress |
|------|-------|----------|
| Authentication | Alice | [100%]{.red} |
| Database | Bob | [80%]{.green} |
| API Docs | Carol | [100%]{.green .underline} |
| Analytics | Dave | 60% |

:::

:::column

### ✍️ Notes

All core features are either complete or in final testing. 
[Performance]{.bold .blue} metrics are excellent.

:::

:::
```

![Columns: table + notes](docs/assets/cb_columns_table_notes.png)

### Figure + Table side‑by‑side

```markdown
# 🖼️ Figure + Table Demo
:::columns

:::column

![Pie Chart](assets/chart_pie.png)

:::

:::column

| Segment | % |
|---------|---|
| Complete | 55 |
| In-Progress | 35 |
| Blocked | 10 |

:::
```

![Columns: figure + table](docs/assets/cb_columns_figure_table.png)

### Speaker notes

```markdown
# 📒 Speaker Notes Demo 2

[A second slide]{.red} to ensure notes mapping is robust.

??? [Speaker note]{.red} for ==slide 2== – keep _eye-contact_ with the [audience](www.google.com).
??? Mention the live ~~demo~~ coming right after this.
```

![Speaker notes](docs/assets/cb_speaker_notes.png)

### Notebook Jinja: figure + table

```jinja2
{% figure "create_sales_chart" width=0.8 caption="Quarterly sales performance vs targets showing steady improvement" %}

{% table "regional_data" 
   order_by="Revenue" desc=true
   rules=[
       ["Growth < 0", {"class": ["red", "bold"]}],
       ["Revenue > 1000000", {"class": ["green"]}]
   ]
   highlight={
       ("East", "Satisfaction"): ["blue", "bold"]
   } %}
```
![Notebook preview](docs/assets/cb_nb_preview.png)
![Notebook figure](docs/assets/cb_nb_figure.png)
![Notebook table](docs/assets/cb_nb_table.png)
![Notebook table](docs/assets/cb_nb_table_style.png)


## Themes
- Switch themes with `--theme default|dark`.
- Customize by copying a CSS file in `themes/` and editing variables (slide size, padding, fonts, colors, table deltas).
![Notebook table](docs/assets/cb_dark_theme.png)

## Google Slides
- Use `examples/gslides_demo.py` and provide credentials via env or a local `credentials.json`.

## Quick Start

CLI (planned console script) — once on PyPI
```bash
pip install slide-generator
slidegen examples/demo_content.md \
  -o output/first_deck.pptx \
  --theme default
```

CLI (from source, today)
```bash
python -m slide_generator.generator examples/demo_content.md \
  -o output/first_deck.pptx \
  --theme default
```

You’ll find the deck under `output/first_deck.pptx`. To also generate a paginated HTML preview for visual verification, add `--debug`.

## Usage

CLI
```bash
python -m slide_generator.generator examples/demo_content.md \
  -o output/presentation.pptx \
  --theme default
```

Python API
```python
import asyncio
from pathlib import Path
from slide_generator.generator import SlideGenerator

markdown = Path("examples/demo_content.md").read_text(encoding="utf-8")

async def build():
    gen = SlideGenerator(output_dir="output", theme="default")
    out = await gen.generate(markdown, "output/from_api.pptx")
    print("Wrote:", out)

asyncio.run(build())
```

Notebook workflow (see examples/notebook_example.ipynb for full demo)
```python
from pathlib import Path
from slide_generator.notebook import SlideNotebook

notebook = SlideNotebook(output_dir="output", theme="default", debug=False, base_dir=Path("examples"))
notebook.new_slide("""
# Quarterly Performance
{% figure "create_sales_chart" width=0.8 caption="Quarterly performance" %}
{% table "regional_data" order_by="Revenue" desc=true %}
""")
notebook.save_sync("output/notebook_example_default.pptx")
```

Examples
- Full feature demo: `python` [examples/comprehensive_demo.py](examples/comprehensive_demo.py)
- Notebook workflow demo: open [examples/notebook_example.ipynb](examples/notebook_example.ipynb)
- Google Slides demo (requires credentials): `python` [examples/gslides_demo.py](examples/gslides_demo.py)

Planned CLI and Extras
- Console script: `slidegen` (equivalent to `python -m slide_generator.generator`)
- Optional extras: `slide-generator[gslides]` for Google Slides dependencies, `slide-generator[math]` for LaTeX/KaTeX rendering
- Supported Python: 3.9+

## Learn More

- Why Slide Generator (and how it compares to similar tools): [docs/why.md](docs/why.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- [docs/cookbook.pdf](docs/cookbook.pdf)
- Jupyter Notebook workflow demo: [examples/notebook_example.ipynb](examples/notebook_example.ipynb)


## Known Limitations

- LaTeX equations currently show as raw LaTeX (rendering planned)
- Code blocks do not include syntax highlighting yet
- In Notebook mode, users can't preview their "two-column" layout: contents are vertically stacked in notebook printouts, though the exported slide decks are fine. 

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
