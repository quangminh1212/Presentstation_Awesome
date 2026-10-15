# pptx-builder — presentations from a YAML file

Describe a talk in a YAML file, run one command, get a real `.pptx` with
embedded, playable video, native tables, rendered equations, and a working
clickable table of contents. Open it in PowerPoint and tweak anything by
hand afterward.

```
YAML (content)  ──►  build_deck.py (layout logic)  ──►  pptx_helpers.py (python-pptx)  ──►  talk.pptx
                                                    └─►  media_tools.py (ffmpeg, matplotlib, Inkscape)
```

## Reason of existence

I got tired of PowerPoint's editor. Dragging boxes around, re-nudging a
caption back under a figure after every "helpful" autofit, rebuilding the
same layout for the fortieth time slide after slide, it doesn't scale, and
it eats time that should go into the actual content.

The obvious alternative, LaTeX/Beamer, wasn't actually an option: I needed
embedded, clickable video in the deck, and I still needed to open the
result five minutes before a talk and manually nudge a caption or swap a
figure. A PDF can't do either of those.

What really sold me on building this was the repetitive case: a dozen
slides sharing the exact same layout, a couple of bullets, one figure ,
where only the figure changes from slide to slide. Re-running an analysis,
regenerating a plot, and rebuilding the whole deck should be one command,
not twenty clicks per slide. With a YAML file and this tool, it is. Point
the slide at the new figure, rerun `build_deck.py`, and the deck rebuilds
looking exactly the way you designed it.

## 1. Setup

```bash
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
ffmpeg -version                                        # must work (ffprobe too)
```

Optional, only if you use SVG figures: [Inkscape](https://inkscape.org/) on
your `PATH` (it rasterizes SVGs to PNG on the fly; nothing else needs it).

## 2. Run the example

```bash
python make_example_assets.py          # synthetic charts, a looping animation, a CSV
python build_deck.py example/talk.yaml # -> example/talk.pptx
python build_deck.py example/talk.yaml -v   # same, with debug logs (ffmpeg commands, boxes, bullets)
```

`example/talk.yaml` is a generic "annual report" deck that exercises every
slide type this tool supports: title, an auto-generated clickable index,
sections, bullet lists with inline markup and footnotes, single and
multi-column figures (with placeholders for figures that aren't ready yet),
mixed image/video layouts, full-width and side-by-side video (including
autoplay), a native table, rendered equations, and a closing slide. Open it
and read `example/talk.yaml` side by side.

**Full field-by-field reference for every slide type: [`CONFIG.md`](CONFIG.md).**

## 3. Project map, and the order to read it

| File | Role | Read |
|---|---|---|
| `example/talk.yaml` | The demo content. Shows every slide type. | 1st |
| `CONFIG.md` | Full YAML reference: every slide type, every field. | 2nd |
| `build_deck.py` | Reads the YAML, one `build_<type>()` per slide type. | 3rd |
| `pptx_helpers.py` | python-pptx building blocks. Top docstring explains the core concepts (layouts, placeholders, EMU, runs). | 4th |
| `media_tools.py` | ffprobe/ffmpeg (transcode, poster frame), image size, SVG rasterization, equation → PNG. | 5th |
| `inspect_template.py` | Lists layouts/placeholders of a template. | when you use your template |
| `check_open.py` | Windows + PowerPoint only: opens a built `.pptx` via real PowerPoint (COM) and reports whether it opens cleanly. Useful when hand-editing `pptx_helpers.py`. | optional, for contributors |
| `bisect_deck.py` | Windows + PowerPoint only: binary-searches a deck's slide list to find the one slide breaking a build. | optional, for contributors |
| `make_example_assets.py` | Only for the demo. | optional |

A good exercise: open `talk.pptx` next to `talk.yaml` and find, for each
slide, the builder function and the helper calls that drew it.

## 4. Using your own template

1. If it's a `.potx`, copy it to a `.pptx` name.
2. `python inspect_template.py your_template.pptx`
3. In the YAML:
   ```yaml
   meta:
     template: "your_template.pptx"
     layouts:
       title: "Title Slide"      # exact names printed by inspect_template.py
       section: "Section Header"
       content: "Title Only"     # a layout with a title and an empty body works best
   ```
4. Check `theme.content_top_in`, `margin_in` and `footer_height_in` against
   where the template's title and logos sit, so content doesn't overlap them.

In template mode, the template's master provides backgrounds, logos and the
title style; the builder fills the title placeholder and draws the rest.
Existing slides in the template are removed. Full details in
[CONFIG.md](CONFIG.md#using-your-own-template).

## 5. Adding a slide type (worked example)

Say you want a "big number" slide:

```python
# in build_deck.py
def build_stat(ctx, spec):
    """type: stat   Fields: title, value, label"""
    t = ctx.theme
    slide = new_slide(ctx, "content", spec)
    box = H.content_box(ctx.prs, t)
    number_box, label_box = box.split_rows([Inches(2.2), None], gap=Inches(0.2))
    H.add_text(slide, number_box, spec["value"], font=t.font_title, size=96,
               color=t.color_accent, bold=True, anchor=MSO_ANCHOR.BOTTOM)
    H.add_text(slide, label_box, spec["label"], font=t.font_body, size=24,
               color=t.color_text)
    H.remove_empty_placeholders(slide)
    return slide

SLIDE_BUILDERS["stat"] = build_stat
```

```yaml
- type: stat
  title: "Headline result"
  value: "+38 %"
  label: "year-over-year growth in active users"
```

## 6. Video notes

- `start: click` (default) plays on click, in PowerPoint on Windows and Mac;
  `start: auto` starts the moment the slide appears.
- The builder re-encodes anything that isn't MP4 + H.264 + yuv420p (ParaView
  AVI/OGV, yuv444 exports) and caches the result in `.deck_cache/`.
- The poster frame (`poster_time`) is what shows before playback and in PDF
  exports.
- Video is embedded, so the `.pptx` is self-contained but grows with each
  video. Use `max_height: 720` to keep it light. Identical videos are
  transcoded only once and reused.

## 7. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `ffprobe was not found` | Install ffmpeg and make sure it's on PATH. |
| `'inkscape' was not found` | Only needed for `.svg` figures; install Inkscape and put it on PATH, or convert the figure to PNG yourself. |
| Black box instead of video | Keep `transcode: true` (default). |
| Speaker icon instead of a frame | Poster extraction failed; run with `-v` to see the ffmpeg error. |
| `layout [...] not found` warning | Put the exact names from `inspect_template.py` in `meta.layouts`. |
| Equation error from matplotlib | mathtext doesn't support that command; simplify, or set `text.usetex` (needs LaTeX). |
| Text overflows | Fewer bullets, or lower `theme.size_body`, or split the slide. |
| PowerPoint says "found a problem with content" and repair doesn't fix it | This means genuinely invalid OOXML slipped through (well-formed XML isn't the same as PowerPoint accepting it) — please open an issue with the YAML that reproduces it. On Windows with PowerPoint installed, `python check_open.py deck.pptx` and `python bisect_deck.py talk.yaml` (see [Project map](#3-project-map-and-the-order-to-read-it)) can help pin down which slide is responsible before reporting. |

## Contributing

Issues and pull requests are welcome — new slide types, layout
improvements, bug reports, or just questions about how something works.
`build_deck.py`'s docstring and [CONFIG.md](CONFIG.md) are the place to
start; the worked example above shows the whole extension mechanism for a
new slide type.

## License and citation

Released under the [MIT License](LICENSE): free to use, modify and
distribute, commercially or otherwise, with no warranty. If you use this
tool for a talk, in a course, or as a base for your own project, a mention
or citation is appreciated (not required), for example:

> *pptx-builder* (2026), https://github.com/Amadeus0k/pptx-builder

---

Parts of this project (including debugging a subtle OOXML validity bug and
drafting this documentation) were built with AI assistance (Claude Code).
