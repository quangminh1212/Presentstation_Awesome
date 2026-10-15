# ZeeLin-image2-PPT

**一行命令，把 Markdown 研究报告变成带 AI 配图的专业 PPT。**

🎨 调用 GPT-image-2 自动生成配图 · 📝 输出标准 .pptx 可二次编辑 · 💰 100 页只需几元钱

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[中文](#中文介绍) | [English](#english)

### 为什么选这个工具？

| | Gamma / Tome / ChatGPT 生 PPT | **ZeeLin-image2-PPT** |
|---|---|---|
| **配图** | 无 AI 配图 / 只有模板图库 | ✅ GPT-image-2 按章节语义自动生成，每张 ¥0.04 |
| **可编辑** | 导出 PDF 无法修改 / 在线编辑受限 | ✅ 输出标准 `.pptx`，PowerPoint / Keynote / WPS 随意改 |
| **成本** | 订阅制 $8-25/月 | ✅ 100 页 PPT 配图总成本约 **¥3-5**（按需付费，无订阅） |
| **版式** | 泛用模板，研究报告结构被夷为平地 | ✅ 9 种研究报告专用版式（金字塔/时间线/矩阵/仪表盘...） |
| **风格** | 通用"漂亮"风，不够学术 | ✅ 白底黑蓝红三色学术风，学生/老师/职场/学者通用 |

---

## 效果预览

> 以下全部由 `im2ppt generate -i input.md -t tsinghua_academic -o output.pptx` 一行命令生成，配图由 gpt-image-2 自动生成。

**封面** — 黑色剪影 × 蓝色节点网络 × 红色分割线，现代极简编辑插画风

![封面](docs/preview/slide-01.jpg)

**原创概念页** — 红色大标题 + 红框公式 + 正文 + 编号要点 + AI 配图

![概念页-人机隔离](docs/preview/slide-05.jpg)

![概念页-多版本现实](docs/preview/slide-08.jpg)

**章节扉页** — 大红数字 + 标题 + 简介 + 主题插画

![章节扉页](docs/preview/slide-09.jpg)

**矩阵网格** — 2×2 / 2×3 自动排列，红蓝黑三色 accent bar

![矩阵](docs/preview/slide-04.jpg)

**金字塔架构** — 自动堆叠，顶层红色、中间蓝色、底层黑色

![金字塔](docs/preview/slide-10.jpg)

**时间线** — 交替上下排列，蓝红交替节点

![时间线](docs/preview/slide-11.jpg)

**数据仪表盘** — 自动提取数字，大字号展示

![仪表盘](docs/preview/slide-17.jpg)

**封底**

![封底](docs/preview/slide-39.jpg)

---

## 中文介绍

### 它解决什么问题

你用 Claude Research / OpenAI Deep Research / Perplexity Pro 跑出了一份 Markdown 研究报告。然后呢？

| 方案 | 问题 |
|------|------|
| 复制粘贴给 ChatGPT 让它生 PPT | 16:9 白底黑字的小学生作业，而且导出的是图片/PDF，**无法二次编辑** |
| 用 Gamma / Tome / Beautiful.ai | 漂亮但"通用风"，研究报告该有的章节扉页、数据面板、金字塔架构被夷为平地。**订阅制 $8-25/月** |
| 手动做 PPT | 一份 30 页的报告至少要半天，配图还得自己找 |

**ZeeLin-image2-PPT** 一次性解决三个痛点：

1. **🎨 GPT-image-2 自动配图** — 封面、章节扉页、原创概念页、封底自动生成现代极简编辑插画（黑+蓝+红三色，白底，无文字乱码）。不用上素材网站找图，不用自己 P 图。每张 ¥0.04，100 页 PPT 大约需要 20-25 张配图，**总成本 ¥3-5**。
2. **📝 输出标准 .pptx，完全可编辑** — 不是图片，不是 PDF，不是在线锁定。输出的是真正的 PowerPoint 文件，每个文本框、每个形状、每张图片都能在 PowerPoint / Keynote / WPS 里自由修改。告别"AI 生成但无法修改"的尴尬。
3. **🏗️ 9 种研究报告专用版式** — 不是泛美学模板，而是编码了"研究报告"这一文体的版面惯例：金字塔架构、时间线流程、双栏对比、矩阵网格、飞轮循环、数据仪表盘、概念 hero 页、章节扉页、金句页。

### 设计风格

对标清华大学新媒沈阳团队的学术 + 产业汇报型 PPT。学生、老师、职场人、学者都能用的简约通用风：

- **白底黑字**：纯白背景，不加米色 / 渐变 / 装饰条 / AI slop
- **三色调**：黑（标题正文）+ 蓝 `#1E40AF`（重要内容）+ 红 `#C8102E`（核心定律、视觉锚点）
- **统一字号**：封面 44pt → 章节 36pt → 内容标题 28pt（全局一致）→ 正文 18pt → 页脚 12pt
- **模块化**：一页一个核心观点，行间距宽松，四周留白充足
- **字体**：微软雅黑 / 思源黑体（CJK）+ Calibri（Latin），无衬线，适配投影与远距离观看

### 30 秒上手

```bash
git clone https://github.com/kelcey2023/ZeeLin-image2-PPT.git
cd ZeeLin-image2-PPT
pip install -e .

# 配置 gpt-image-2 配图（可选，不配也能生成纯文字版）
cp .env.example .env
# 编辑 .env，填入 GEZHI_IMAGE_API_KEY（BananaRouter 的 key）

# 一行命令生成
im2ppt generate -i your_research.md -t tsinghua_academic -o deck.pptx
```

不想用配图？设 `GEZHI_GENERATE_IMAGES=0` 即可生成纯文字版 PPT。

### 9 大版式

每个 `## H2` 章节通过 HTML 注释指定版式：

```markdown
## 我的章节标题
<!-- layout: pyramid -->
- 顶层概念
- 中间层
- 基础层
```

| Hint | 版式 | 说明 |
|------|------|------|
| `<!-- concept -->` | 原创概念 hero 页 | 红色大标题 + 红框公式 + 编号要点 + gpt-image-2 配图 |
| `<!-- layout: chapter -->` | 章节扉页 | 大红数字 + 标题 + 简介 + gpt-image-2 配图 |
| `<!-- layout: pyramid -->` | 金字塔架构 | 3-5 层堆叠，顶红中蓝底黑 |
| `<!-- layout: timeline -->` | 时间线 / 路线图 | 3-6 步，蓝红交替节点，上下交错 |
| `<!-- layout: split -->` | 双栏对比 | 左蓝右红，垂直分割线 |
| `<!-- layout: matrix -->` | 矩阵网格 | 2×2 或 2×3，彩色 accent bar |
| `<!-- layout: flywheel -->` | 飞轮 / 循环 | 中心枢纽 + 环绕节点 |
| `<!-- layout: dashboard -->` | 数据仪表盘 | 自动提取数字，72pt 大字展示 |
| `<!-- layout: quote -->` | 金句页 | 红色引号 + 黑体引文 + 蓝色署名 |
| `<!-- layout: closing -->` | 封底 | THANK YOU + 结语 + 配图 |

无 hint 时默认渲染为标准内容页（标题 + 正文 + 列表）。

### AI 配图的工作原理

封面、章节扉页、原创概念页、封底这四类 hero 页会自动获得 AI 配图：

1. **大纲规划阶段**：解析 markdown，识别哪些 slide 属于 hero 类型
2. **Prompt 构建**：根据章节标题关键词匹配语义化的视觉 metaphor（如"推理优化"→ 加速箭头，"自进化框架"→ 递归环）
3. **图片生成**：调用 BananaRouter 的 gpt-image-2 API（OpenAI 兼容协议），1536×1024 px
4. **哈希缓存**：生成结果按 prompt 的 SHA-256 缓存到 `.image_cache/`，改一行代码重跑时所有已有图零成本复用
5. **嵌入渲染**：生成的 PNG 嵌入到 PPTX 的对应 slide 中

图片风格锁定为**现代极简编辑插画**——黑色实心剪影 + 钴蓝线框/节点 + 红色单点高亮，纯白背景，无文字。视觉上对标 NYT op-ed 插图 / The Economist 封面 / Bauhaus 海报。

### Markdown 输入约定

```markdown
---
title: 你的报告标题
subtitle: 副标题
author: 作者名
date: 2026 年 4 月
---

# 报告标题

## 目录
1. 第一章
2. 第二章

## 引言
正文内容，**加粗** 会变蓝色强调。

## 核心概念
<!-- concept -->
概念名 = 公式定义
描述段落。
- 要点一
- 要点二
- 要点三

## 第一章 · 理论基座
<!-- layout: chapter -->
章节引言段落。

## AI 能力四层结构
<!-- layout: pyramid -->
- 物理世界交互层
- 数字世界自主交互层
- 数字内容生成层
- 通用符号推理层

## 关键数据
<!-- layout: dashboard -->
- Qwen3 从 207 提升至 870 tok/s
- 平均提升 4.2x 且保持完全无损

## 结语
<!-- layout: closing -->
结尾金句。
```

详细格式规范见 [docs/markdown_format.md](docs/markdown_format.md)。

### CLI 命令

```bash
im2ppt generate -i input.md -o output.pptx        # 使用默认模板
im2ppt generate -i input.md -t tsinghua_academic   # 指定模板
im2ppt list-templates                              # 查看可用模板
im2ppt check-config                                # 检查 API key 配置
```

### 项目结构

```
ZeeLin-image2-PPT/
├── im2ppt/                          # Python 包
│   ├── cli.py                      # CLI 入口（im2ppt generate）
│   ├── config.py                   # .env 配置加载
│   ├── parsers/markdown.py         # Markdown AST 解析
│   ├── visual/image_gen.py         # BananaRouter gpt-image-2 客户端 + 缓存
│   └── templates/
│       ├── tsinghua_academic/      # 主力模板
│       │   ├── style.py           # 调色板 + 字号 + 布局 token
│       │   ├── schema.py          # 大纲规划器（markdown → SlideSpec 列表）
│       │   ├── layouts.py         # 9 种版式渲染器（~1200 行）
│       │   └── image_prompts.py   # gpt-image-2 prompt 构建器
│       └── deep_research_report/   # 备选模板（深色咨询风）
├── examples/
│   └── shenyang_2026/
│       ├── input.md                # Demo 输入（沈阳团队 2026 年 4 月报告）
│       └── output.pptx            # 生成成品（39 页，14 张 AI 配图，12MB）
├── docs/
│   ├── markdown_format.md         # 输入格式详细说明
│   └── preview/                   # README 预览图
├── pyproject.toml                 # pip install -e .
├── .env.example                   # API key 配置模板
└── LICENSE                        # MIT
```

### 技术栈

| 组件 | 作用 |
|------|------|
| [python-pptx](https://github.com/scanny/python-pptx) | PPTX 原生形状渲染，无 LibreOffice 依赖 |
| [BananaRouter](https://bananarouter.com) gpt-image-2 | AI 配图生成，OpenAI 兼容协议，¥0.04/张 |
| [click](https://click.palletsprojects.com) + [rich](https://rich.readthedocs.io) | CLI 体验 |
| [markdown-it-py](https://github.com/executablebooks/markdown-it-py) | Markdown AST 解析 |

### 路线图

- [x] **v0.1** — `tsinghua_academic` 模板 + 9 大版式 + gpt-image-2 集成 + 哈希缓存
- [ ] v0.2 — OCR 配图核验（确保生成图中无乱码文字）
- [ ] v0.3 — 内置 ZeeLin DeSearch 调用（主题 → 深度报告 → PPT 一条龙）
- [ ] v0.4 — 更多模板：`teaching_deck`（科普向）/ `grant_proposal`（基金本子摘要）
- [ ] v0.5 — 支持 ppt-master 的 SVG → DrawingML 引擎（可编辑矢量图形）

---

## English

### What is it

ZeeLin-image2-PPT is a **Markdown → PPTX** CLI tool purpose-built for research report presentations. Three key advantages:

1. **🎨 GPT-image-2 auto-illustrations** — Cover, chapter dividers, concept pages, and closings get auto-generated editorial illustrations via gpt-image-2. Black silhouettes + cobalt blue nodes + crimson accents on white. ~$0.005/image, **100-page deck costs ~$0.50 total**.
2. **📝 Fully editable .pptx output** — Not images, not PDFs, not locked online editors. Real PowerPoint files where every text box, shape, and image is freely editable in PowerPoint / Keynote / WPS / Google Slides. **No more "AI-generated but can't modify."**
3. **🏗️ 9 research-report-specific layouts** — Not generic "pretty slides." Encodes the conventions of academic presentations: pyramids, timelines, split comparisons, data dashboards, concept hero pages, chapter dividers, pull-quotes, matrix grids, and flywheels.

### Quick Start

```bash
git clone https://github.com/kelcey2023/ZeeLin-image2-PPT.git
cd ZeeLin-image2-PPT
pip install -e .

cp .env.example .env
# Edit .env, add your GEZHI_IMAGE_API_KEY (BananaRouter key)

im2ppt generate -i your_research.md -t tsinghua_academic -o deck.pptx
```

Set `GEZHI_GENERATE_IMAGES=0` in `.env` to generate text-only (no API key needed).

### Design System

- **Pure white background** — no cream, no gradients, no decorative bars
- **Three-color palette** — black (titles/body) + cobalt blue `#1E40AF` (emphasis) + crimson `#C8102E` (core laws / visual anchors)
- **Unified type scale** — cover 44pt → chapter 36pt → slide title 28pt (global) → body 18pt → footer 12pt
- **One core idea per slide** — generous whitespace, modular, no information overload
- **CJK-first typography** — Microsoft YaHei / Source Han Sans + Calibri fallback

### 9 Layout Types

Use HTML comments to specify layout for each `## H2` section:

```markdown
## Chapter Title
<!-- layout: pyramid -->
- Top tier
- Middle tier
- Foundation
```

Supported layouts: `concept` (hero page with formula + image), `chapter` (divider with large number + image), `pyramid`, `timeline`, `split`, `matrix`, `flywheel`, `dashboard`, `quote`, `closing`.

### How AI Illustrations Work

Hero pages (cover, chapter dividers, concept pages, closing) automatically get illustrations:

1. Markdown parsed → slide plan identifies hero-type slides
2. Semantic prompt built from chapter title keywords (e.g., "inference optimization" → thrust arrow, "self-evolution" → recursive rings)
3. gpt-image-2 called via BananaRouter API (1536×1024, OpenAI-compatible)
4. Results SHA-256 cached in `.image_cache/` — re-runs reuse existing images at zero cost
5. PNGs embedded into PPTX at render time

Style: **modern editorial illustration** — NYT op-ed / The Economist cover / Bauhaus poster aesthetic. Strict black + cobalt blue + crimson red on white. No text in images.

---

## 致谢 / Acknowledgments

- Inspired by [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- Design reference: 清华大学新媒沈阳团队 academic presentation style
- Built with [python-pptx](https://github.com/scanny/python-pptx) and [gpt-image-2](https://platform.openai.com/docs/guides/images)

## License

MIT — see [LICENSE](LICENSE)
