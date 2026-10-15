# html-to-one-pptx

**A Claude Code Skill that converts any HTML page into a pixel-faithful PowerPoint slide.**

> One HTML → One Slide. No manual tweaking. No screenshots.

[中文文档](README.zh.md)

---

## Overview

`html-to-one-pptx` is a Claude Code Skill that automates the entire pipeline from an HTML design file to a `.pptx` slide. Whether it's a data report, product pitch, architecture diagram, or stylized cover — give Claude an HTML file and it produces a presentation-ready PPT slide.

**Key capabilities:**

- **Pixel-accurate coordinates** — HTML pixels map precisely to PPT's EMU coordinate system
- **Native chart rendering** — Automatically detects Chart.js / ECharts data and generates native PPT charts (not screenshots), fully editable in PowerPoint
- **Multi-file merge** — Multiple HTML files are processed independently and merged into a single multi-page PPTX
- **Color fidelity** — A dedicated Color Master phase audits contrast and visibility before any code is written

---

## Demo

Canvas size: **1017 × 720 px** (PPT 10.59" × 7.50" @ 96 dpi)

| Theme | Preview | Description |
|-------|---------|-------------|
| **Mystery Intrusion** | ![](demo/theme1-mystery-intrusion.PNG) | Dark-mode cybersecurity situational report |
| **Minecraft** | ![](demo/theme2-minecraft.PNG) | Pixel-art game-style showcase |
| **Ancient Epic** | ![](demo/theme3-ancient-epic.PNG) | Chinese ink-wash epic cover |
| **Boss Report** | ![](demo/theme4-boss-report.PNG) | Clean business briefing layout |
| **Architecture** | ![](demo/theme5-architecture.PNG) | Multi-column technical architecture diagram |
| **AI Product** | ![](demo/theme6-ai-product.PNG) | Dark-theme AI product introduction |

All HTML source files and PNG previews are in [`demo/`](demo/). The merged output is [`demo/final.pptx`](demo/final.pptx).

---

## Usage

### Trigger phrases

Upload an HTML file in a Claude Code session and say any of the following:

```
convert to PowerPoint
turn this into slides
make a PowerPoint from this HTML
一比一还原为 PPT
把这个 HTML 转成 PPT
```

### Single file

```
User:   [upload slide.html]  convert to PowerPoint
Claude: runs 5 phases → outputs tmp/output.pptx
```

### Multiple files (merged into one PPTX)

```
User:   [upload slide1.html slide2.html slide3.html]  make a PowerPoint
Claude: processes each file individually → merges → outputs tmp/final.pptx
```

---

## Conversion Pipeline (5 Phases)

```
① Parse HTML        Claude reads the HTML and extracts every layout block,
                    shape, text element, and chart.
                    → writes tmp/parsehtml.md  (coordinate tables + nested structure)

② Detect Charts     python3 scripts/detect_charts.py slide.html --out tmp/
                    Extracts Chart.js / ECharts data → tmp/charts.json
                    (skipped if no charts are found)

③ Color Master      Audits every color for contrast ratio and visibility.
                    → writes tmp/colors.md  (corrected color mapping)

④ Write gen.js      Claude authors a PptxGenJS script driven by
                    parsehtml.md + charts.json + colors.md
                    → writes tmp/gen.js

⑤ Execute           node tmp/gen.js  →  tmp/output.pptx  ✅
```

For multiple files, a merge step is added after all slides are built:

```bash
python3 scripts/merge_slides.py --slides-dir ./tmp  →  tmp/final.pptx
```

---

## Design Principles

| Principle | Description |
|-----------|-------------|
| **One HTML = One Slide** | Each HTML file gets its own `tmp/slide_NN/` subfolder — fully isolated |
| **Fit-to-page** | `SCALE = min(slide_w / html_w, slide_h / html_h)` guarantees single-page output |
| **Charts = Native PPT** | `addChart()` instead of screenshots — charts stay editable in PowerPoint |
| **Never Batch** | `gen.js` is written and executed individually per slide, never in a loop |
| **Color Master First** | Color audit always happens before any code, ensuring one-pass quality |

---

## Project Structure

```
html-to-one-pptx/
├── skill.md              # Skill definition (read by Claude Code)
├── pptxgenjs.md          # PptxGenJS full API reference
├── scripts/
│   ├── detect_charts.py  # Extracts chart data from HTML
│   └── merge_slides.py   # Merges per-slide PPTX files into one
├── demo/
│   ├── theme1-mystery-intrusion.html  + .PNG
│   ├── theme2-minecraft.html          + .PNG
│   ├── theme3-ancient-epic.html       + .PNG
│   ├── theme4-boss-report.html        + .PNG
│   ├── theme5-architecture.html       + .PNG
│   ├── theme6-ai-product.html         + .PNG
│   └── final.pptx        # 6-slide merged output
├── README.md             # English (primary)
└── README.zh.md          # Chinese
```

---

## Requirements

| Tool | Purpose | Install |
|------|---------|---------|
| Node.js ≥ 18 | Run gen.js | [nodejs.org](https://nodejs.org) |
| pptxgenjs | PPT generation library | `npm install pptxgenjs` |
| Python ≥ 3.9 | Chart detection & merge scripts | [python.org](https://python.org) |
| python-pptx | PPTX merging | `pip install python-pptx` |
| BeautifulSoup4 | HTML parsing | `pip install beautifulsoup4` |

---

## Pairing with `html-report`

This skill works best alongside the [`html-report`](README.zh.md) skill:

```
html-report        →  generates multi-page HTML data reports
html-to-one-pptx   →  converts each HTML page 1:1 into a PPT slide
```

Use `html-report` to visualize your analysis as HTML, then pipe the output through `html-to-one-pptx` to get a presentation-ready PPTX in one session.

---

## License

MIT
