[![English](https://img.shields.io/badge/Language-English-blue)](README.md) [![中文](https://img.shields.io/badge/语言-中文-red)](README_ZH.md)

# 🎨 html-report Skill · PPT Visual Report Generator

> **No idea how to design a PPT? Say one sentence, get a beautiful PPT-style HTML page — automatically.**
> Screenshot it, paste it into any slide deck. Zero manual layout. Zero design experience required.

---

## ✨ What Is It

`html-report` is an AI agent Skill that transforms any text content into **screenshot-ready PPT-style HTML pages**.

Compatible with Claude Code, Doubao (豆包), Cursor, Windsurf, and other major AI coding assistants. Every page is strictly locked to **1017×720px** (aligned to PPT canvas 10.59"×7.499" @96dpi). After screenshotting with Chrome or Puppeteer, the result can be pasted directly as a slide — no PowerPoint software needed.

When you:
- 🤔 **Have no idea how to lay out a PPT** → Describe the topic, get a generated page
- 📊 **Need chart visualization** → 12+ pure SVG chart types, zero dependencies
- 🎨 **Want a polished look** → 6 visual templates × 7 color schemes = 168 combinations
- ⚡ **Are short on time** → ~4 seconds per page, a 10-page report in about 1 minute

---

## 🚀 Quick Start

In any AI agent (Claude Code / Doubao / Cursor etc.), just say:

```
Generate a report: analyze our company's 2025 AI strategy
```

```
Turn this competitive analysis into an HTML report page
```

```
Visualize content: quantum computing technology trends
```

The AI will automatically handle: topic breakdown → template selection → color scheme → layout → content → HTML output

---

## 🐟 HTML → PPT One-to-One Conversion

> **After generating the HTML, send it to Doubao, Claude, or any AI — one prompt converts it to a real PPT!**

Copy the generated HTML content and send it to any AI assistant that supports file or long-text input, with this prompt:

```
Please convert this HTML page into a PowerPoint slide (PPTX format),
reproducing the layout, colors, charts, and content exactly 1:1.
Canvas size is 1017×720px. Keep all visual elements at their exact
position, size, and color.
```

**Workflow:**

```
① AI agent generates HTML files
        ↓
② Send the HTML content/file to Doubao or Claude
        ↓
③ Paste the prompt: "Convert to PPT 1:1 based on page layout"
        ↓
④ Download PPTX, ready to present ✓
```

---

## 🖼️ Style Showcase

The examples below demonstrate the visual styles this Skill can generate — showing how AI freely creates visual languages tailored to each topic:

---

### Theme 1 · Mystery Intrusion · Hacker Terminal Style

> Best for: cybersecurity reports, threat intelligence, CTF presentations, penetration testing analysis

![Theme 1 Mystery Intrusion](demo/theme1-mystery-intrusion.PNG)

**Characteristics:** Pure black background + matrix green `#00ff41` · Share Tech Mono monospace · Scanline animation texture · Terminal command-line style · Ambient glow overlay

---

### Theme 2 · Minecraft · Pixel Block Style

> Best for: game reports, creative showcases, youth education, geek/fun presentations

![Theme 2 Minecraft](demo/theme2-minecraft.PNG)

**Characteristics:** Pixelated rendering style · Minecraft color palette (dirt / grass / sky) · Block borders · Pixel font simulation · In-game UI elements

---

### Theme 3 · Ancient Epic · Chinese Classical Style

> Best for: sinology reports, historical analysis, cultural heritage, classical literature topics

![Theme 3 Ancient Epic](demo/theme3-ancient-epic.PNG)

**Characteristics:** Deep brown-black background `#0a0502` · Gold primary color `#d4a853` · Noto Serif SC · Ancient scroll paper texture · Ink flowing light effect

---

### Theme 4 · Boss Report · Professional Business Style

> Best for: work summaries, quarterly reviews, business analysis, executive presentations

![Theme 4 Boss Report](demo/theme4-boss-report.PNG)

**Characteristics:** High-readability light background `#f5f7fa` · Deep blue professional palette `#0f3460` · System font stack · KPI number cards · Professional chart mix

---

### Theme 5 · Architecture Blueprint · Engineering Blueprint Style

> Best for: system design, technical proposals, microservice architecture, infrastructure planning

![Theme 5 Architecture](demo/theme5-architecture.PNG)

**Characteristics:** Deep sea blue background `#0d1b2a` · Blueprint grid overlay (dual-precision grid lines) · JetBrains Mono monospace · Engineering drawing annotation style · Connection lines and nodes

---

### Theme 6 · New AI Product · Deep Space Tech Style

> Best for: AI product launches, tech startup fundraising, product roadmaps, futuristic demos

![Theme 6 AI Product](demo/theme6-ai-product.PNG)

**Characteristics:** Ultra-deep purple-black background `#06040f` · Star particle effect · Purple-blue gradient glow · Inter modern font · Glassmorphism cards · Tech data visualization

---

## 🧩 Combination Matrix

```
6 Templates  ×  7 Color Schemes  ×  4 Layout Structures  =  168 Combinations
```

### 6 Visual Templates

| Code | Name | Background | Best For |
|------|------|------------|----------|
| **T1** | Dark Luxury | `#05080f` deep black | Tech · AI · Premium business |
| **T2** | Editorial Split | Dark left + light right clip-path | Competition · Contrast · Strong narrative |
| **T3** | Terminal Code | `#0d1117` GitHub Dark | Tech · Code · Security audit |
| **T4** | Data Dashboard | `#f0f4f8` light | Data · Operations · Monthly reports |
| **T5** | Editorial Minimal | `#fafaf8` warm white | Brand · Annual reports · Academic |
| **T6** | Neon Cyberpunk | `#080010` ultra-dark | Security · Geek · Creative |

### 7 Color Schemes

| Color | Primary | Best Templates | Semantic |
|-------|---------|---------------|---------|
| 🔵 Blue | `#3b82f6` | T1 / T4 | Tech · Trust · Data |
| 🔴 Red | `#ef4444` | T2 | Competition · Risk · Urgency |
| 🟠 Orange | `#f59e0b` | T5 | Business · Energy · Growth |
| 🟢 Green | `#10b981` | T3 | Health · Success · Sustainability |
| 🟣 Purple | `#8b5cf6` | T1 / T6 | Creative · AI · Premium |
| 🩵 Cyan | `#06b6d4` | T1 / T4 | Fresh · Efficiency · Digital |
| 🩷 Pink | `#f472b6` | T6 | Geek · Neon · Innovation |

### 4 Layout Structures

| Layout | Structure | Best For |
|--------|-----------|----------|
| **A** | Large left + right 3-row cards | Architecture · Flowcharts · Single-chart focus |
| **B** | 4×2 grid (two rows) | Step-by-step · Four quadrants · Comparison |
| **C** | 3×2 six-cell matrix | Chart library · Multi-dimensional data · Full coverage |
| **D** | 2×2 + right full-height | Mixed dashboard · Hybrid layout · Cover |

---

## 📐 Technical Specs

```
Canvas size:    1017 × 720 px  (= PPT 10.59" × 7.499" @96dpi)
4-zone layout:  Header 72px + Content 580px + Summary 48px + Footer 20px = 720px
Content width:  1017 - 25×2 = 967px (usable area)
Charts:         Pure SVG, zero external dependencies
Screenshot:     Chrome / Puppeteer (pixel-perfect 1:1)
Fonts:          Syne 800 (headings) + DM Sans (body) + monospace (code)
```

---

## ⚙️ Three Iron Rules

> Violating any one of these → the page is scrapped and rebuilt. No exceptions.

**① Canvas locked to 1017×720px**
```css
html, body {
  width: 1017px; height: 720px;
  min-width: 1017px; max-width: 1017px;
  min-height: 720px; max-height: 720px;
  overflow: hidden;
}
```

**② Four-zone heights must sum exactly to 720px**
```
Header   72px  ←  page header
Content 580px  ←  main content
Summary  48px  ←  summary bar
Footer   20px  ←  page footer
──────────────
Total   720px  ✓
```

**③ Content density ≥ 75% per cell**
- 3-layer content structure: title row + body text (≥ 40 chars, ≥ 2 numbers) + bottom enhancement component
- Bottom enhancement: SVG chart / mini number cards / progress bars — pick one

---

## 🗂️ Skill File Structure

```
html-report/
├── SKILL.md              ← Skill entry point (read by AI agent)
├── demo/                 ← Example pages & screenshot previews
│   ├── theme1-mystery-intrusion.html / .PNG  ← Mystery Intrusion · Hacker Terminal Style
│   ├── theme2-minecraft.html / .PNG          ← Minecraft · Pixel Block Style
│   ├── theme3-ancient-epic.html / .PNG       ← Ancient Epic · Chinese Classical Style
│   ├── theme4-boss-report.html / .PNG        ← Boss Report · Professional Business Style
│   ├── theme5-architecture.html / .PNG       ← Architecture · Engineering Blueprint Style
│   └── theme6-ai-product.html / .PNG         ← New AI Product · Deep Space Tech Style
└── references/
    ├── 01-canvas.md        ← Canvas size, 4-zone structure, overflow rules
    ├── 02-design-system.md ← 6 visual templates (T1–T6) CSS snippets
    ├── 03-layout.md        ← 4 layout CSS + space calculations
    ├── 04-color-font.md    ← 7 color schemes, font rules, semantic colors
    ├── 05-content.md       ← Anti-laziness rules, content density, SVG chart library
    └── 06-workflow.md      ← Planning workflow, render verification, quality checklist
```

---

## 📋 Trigger Keywords

Include any of the following in your conversation to activate the skill:

- `generate report` / `make a report`
- `make HTML` / `generate HTML page`
- `visualize content` / `visual report`
- `analysis page` / `PPT page`

---

## 🔄 Generation Flow

```
User inputs topic
      ↓
AI reads Skill spec (6 reference files)
      ↓
Topic breakdown → plan 10 sub-dimensions
      ↓
Per page: select template (T1–T6) → color scheme → layout → write content → QA
      ↓
Output 01.html ... 10.html
      ↓
Option ①: Chrome/Puppeteer screenshot → 1017×720px PNG → paste into PPT slides
Option ②: Send HTML to Doubao/Claude → "Convert to PPT 1:1" → download PPTX ✓
```

---

## 💡 Usage Suggestions

| Scenario | Recommended Combo | Notes |
|----------|-------------------|-------|
| Business plan | T1 Blue + T4 Blue + T5 Orange | Professional, data-credible |
| Technical proposal | T1 Blue + T3 Green + T4 Cyan | Tech feel, code showcase |
| Competitive analysis | T2 Red + T4 Blue | High contrast, data-driven |
| Security report | T6 Pink + T3 Green + T1 Purple | Threat awareness, technical authority |
| Annual summary | T5 Orange + T1 Blue + T4 Blue | Premium, data-rich |
| Product launch | T6 Pink + T1 Purple + T2 Red | Visual impact, memorable |

---

## 📄 License

MIT · Free for commercial and personal use
