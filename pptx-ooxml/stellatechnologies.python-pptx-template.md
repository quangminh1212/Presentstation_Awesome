## python-pptx-template

PowerPoint templating powered by Jinja2. Templates are standard `.pptx` files edited in PowerPoint, with inline Jinja tokens that are rendered into a new presentation.

### Install

```bash
pip install -r requirements.txt
```

### Features

- **Jinja2 inside PPTX**: variables, loops, and conditionals in text boxes, table cells, and paragraphs.
- **Slide duplication**: whole-slide loops via `{% slide for s in slides %}{% endfor %}` (alias `{% s for ... %}`) with per-slide context.
- **Table helpers**: row-level loops inside `<a:tr>` are expanded; standard `{% for %}...{% endfor %}` patterns also supported in rows and paragraphs.
- **Whitespace control**: `{%- ... -%}` trimming honored for PPTX text runs.
- **Newlines and tabs rendering**: `\n` becomes line breaks, `\t` becomes tabs, `\f` starts a new paragraph.
- **Core properties templating**: `title`, `author`, `subject`, `comments`, `identifier`, `language` render from context.
- **Image replacement by path**: a textbox that renders to an image path (e.g., `{{ s["image"] }}`) is replaced by a centered, aspect-fit picture within the textbox rectangle.
- **Undeclared variables inspection**: detection of variables present in the template but missing from a provided context.
- **CLI and Python API**: render from command line or integrate as a library.

### Supported Jinja tokens (in shapes and tables)

- **Variable**: `{{ name }}`
- **Conditional**: `{% if condition %}...{% endif %}`
- **Loops in paragraphs/cells**:
  - `{% for item in items %}{{ item }}{% endfor %}`
  - Row macro forms are normalized; `{% tr for row in rows %}...{% endfor %}` and standard `{% for row in rows %}...{% endfor %}` inside a table row are both supported.
- **Slide loop**: `{% slide for s in slides %}{% endfor %}` (alias `{% s for ... %}`) on the slide; the body of the slide uses `s`.
- **Whitespace control**: `{%-` and `-%}` behave as in Jinja2.

### Public API

- `pptxtpl.PptxTemplate(template_path)`
  - `render(context: dict, jinja_env: Optional[Environment] = None, autoescape: bool = False) -> None`
  - `save(path_or_file) -> None`
  - `get_undeclared_template_variables(jinja_env: Optional[Environment] = None, context: Optional[dict] = None) -> Set[str]`

- `pptxtpl.RichText` and `pptxtpl.RichTextParagraph`
  - Build rich text runs/paragraphs for advanced scenarios where XML fragments are injected via context.

- `pptxtpl.Listing`
  - Simple escaped text wrapper helpful for newline handling while preserving template styling.

Notes:

- `pptxtpl.InlineImage` and `pptxtpl.Subdoc` are not supported for PPTX and raise `NotImplementedError`.

### Python example

```python
from pptxtpl import PptxTemplate

tpl = PptxTemplate("tests/templates/Bullets.pptx")
ctx = {"items": ["One", "Two", "Three"]}
tpl.render(ctx)
tpl.save("tests/output/out_bullets.pptx")
```

Slide duplication example (template content on a slide):

```text
{% slide for s in slides %}{% endfor %}
Title shape: {{ s["title"] }}
Bullets shape: {% for x in s["bullets"] %}{{ x }}{% endfor %}
Image frame textbox: {{ s["image"] }}
```

### CLI

```bash
python -m pptxtpl TEMPLATE.pptx DATA.json OUTPUT.pptx [--overwrite | -o] [--quiet | -q]
```

- **--overwrite/-o**: overwrite existing output without prompt
- **--quiet/-q**: suppress non-essential messages

### Demos

- Build sample templates: `python tests/build_templates.py`
- Render all demos: `python tests/run_all.py` (outputs written under `tests/`)

### Limitations

- Inline embedded subdocuments and inline images are not provided by this package for PPTX.
- RichText helpers generate XML snippets and require careful placement within paragraph contexts.

### License

See `LICENSE.txt`.


