<div align="center">

# 🎬 PPTFlux

### Paste your notes. Get a live, interactive, fully-editable HTML deck.
### 粘贴资料，得到一份会动、可改、能直接演示的 HTML 幻灯片。

**No tool-hopping. No copy-paste relay. One page, end to end.**
**不再多工具接力，不再复制粘贴搬运。一个网页，一气呵成。**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://wilingna.github.io/PPTFlux/)
[![No Build](https://img.shields.io/badge/build-zero%20config-blue)](https://github.com/wilingna/PPTFlux)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-purple)](https://openrouter.ai/)
[![Stars](https://img.shields.io/github/stars/wilingna/PPTFlux?style=social)](https://github.com/wilingna/PPTFlux)

[**🔗 Live Demo**](https://wilingna.github.io/PPTFlux/) · [English](#english) · [中文](#中文) · [Quick Start](#-quick-start) · [The Story](#-the-story--三次跃迁)

</div>

---

## 🎯 TL;DR

**EN** — PPTFlux turns raw notes into an animated, interactive HTML deck through 4 specialized AI agents. Unlike Gamma-style tools that give you a static export, PPTFlux outputs **real HTML** — every slide is editable in two layers (the writing layer for content, the HTML layer for everything else). 6 design languages × 18 layout variants, particle backgrounds, animated SVG flows, number rollers. No build step, no backend, no lock-in.

**中文** — PPTFlux 用 4 个专业化 AI Agent 把原始资料变成会动、可交互的 HTML 幻灯片。和 Gamma 那种"导出即定稿"的工具不同，PPTFlux 输出的是**真正的 HTML**——每一页都有两层可编辑（文案层管内容，HTML 层管一切其他东西）。6 套设计语言 × 18 种排版，粒子背景、SVG 动画流程图、数字滚动。无构建、无后端、无平台绑架。

---

<a name="english"></a>
## 🌍 English

### The Problem

To make a decent AI-generated deck today, you need 3 tools in a relay race:
- **NotebookLM** to outline → **Gemini/Claude** to polish → **Gamma** to render

Every handoff drops context. Every handoff demands manual reformatting. And the moment Gamma gives you the slides, you're stuck — change a heading? Re-export. Change the color? Pray Gamma's editor cooperates.

### The PPTFlux Approach

```
Notes → Understand → Structure → Express → Render → Present
              └─── all in ONE page, ZERO context loss ───┘
```

PPTFlux closes the loop. Four agents handle understanding, structuring, writing, and rendering inside a single HTML file. The output is **a real HTML deck you own** — animated, editable, scriptable, and downloadable.

### Why It's Different

| | Gamma & friends | **PPTFlux** |
|---|---|---|
| Output format | Locked-in platform format | **Plain HTML you own** |
| Editability | Their editor only | **Edit text layer → re-render**, OR edit raw HTML |
| Visual feel | Template-y, static | Animated: particles, SVG flows, number rollers |
| Layout variety | A few templates | **6 design languages × 18 layouts**, auto-rotated |
| Data privacy | Through their servers | API call goes browser → OpenRouter, nothing else |
| Cost | Subscription | Pay-per-use via OpenRouter (~$0.10–0.30/deck) |

### Two Layers of Control

> **AI's output is the starting point, not the ending point.**

1. **Writing layer** — After agents draft the deck, edit any line, headline, or bullet, then re-render that slide. Don't like the conclusion on slide 4? Rewrite one sentence and re-run that page.
2. **HTML layer** — The output is real HTML. Open it in any editor, hand it to Cursor or Claude, change colors, layouts, animations, anything. You always have the keys.

---

<a name="中文"></a>
## 🇨🇳 中文

### 痛点

今天想用 AI 做一份像样的 PPT，至少要在 3 个工具之间接力：
- **NotebookLM** 梳理 → **Gemini / Claude** 润色 → **Gamma** 出图

每跳一次丢一次上下文，每跳一次手动对齐一次格式。等 Gamma 把图给你，你就被锁死了——改个标题？重导。改个颜色？祈祷 Gamma 的编辑器给你面子。

### PPTFlux 的思路

```
资料 → 理解 → 结构 → 表达 → 渲染 → 演示
        └──── 全部在一个网页里完成，零上下文损耗 ────┘
```

PPTFlux 把回路闭上了。4 个 Agent 在一个 HTML 文件里搞定从理解到渲染。产出是**一份真正属于你的 HTML 幻灯片**——会动、能改、可脚本化、可下载。

### 和 Gamma 这类工具的对比

| | Gamma 等工具 | **PPTFlux** |
|---|---|---|
| 输出格式 | 锁在平台格式里 | **纯 HTML，你自己拿走** |
| 可编辑性 | 只能用它家编辑器 | **改文案层 → 重渲染**，或直接改 HTML |
| 视觉感受 | 模板感重，静态 | 动态：粒子、SVG 动画、数字滚动 |
| 排版多样性 | 几个模板循环 | **6 套设计语言 × 18 种排版**，智能轮转 |
| 数据隐私 | 经过它家服务器 | 浏览器 → OpenRouter 直连，无中间服务器 |
| 费用 | 订阅制 | OpenRouter 按量计费（约 $0.10–0.30/份）|

### 两层都能改的控制权

> **AI 的产出是起点，不是终点。**

1. **文案层**——Agent 写完后，你可以改任何一句话、标题、bullet，然后单页重渲染。第 4 页结论不满意？改一句话重跑这一页就行
2. **HTML 层**——输出是真 HTML。任何编辑器打开、丢给 Cursor 或 Claude、改色彩布局动效，你永远握着钥匙

---

## 🎨 6 Design Languages · 6 套设计语言

Each style ships with its own typography, spacing, and decorative DNA — not just a recolored palette.
每套都有自己的字体、留白、装饰基因，**不是换配色那种敷衍**。

| Style | Vibe · 适合场景 |
|---|---|
| 🔊 **Bold Signal** | Big-type announcement energy · 大字号强信号，发布会 / 宣讲 |
| 🌿 **Dark Botanical** | Moody, narrative depth · 暗底植物剪影，沉稳叙事 / 深度报告 |
| ⚡ **Creative Voltage** | High-saturation clash · 高饱和撞色，创意提案 |
| 🇨🇭 **Swiss Modern** | Minimal grid, consultancy clean · 极简网格，咨询报告底子 |
| 🎛 **Electric Studio** | Studio / product-launch feel · 工作室感，工具 / 产品介绍 |
| 📓 **Notebook Tabs** | Paper texture, teaching tone · 纸感笔记本，教学 / 复盘 |

Combined with **6 layout types × 3 variants = 18 page templates**, dispatched intelligently so adjacent slides never look the same.
配合 **6 种 layout × 3 种 variant = 18 种排版**，智能轮转派发，相邻页绝不重样。

```
Layouts: hook · data · process · compare · insight · action
Variants: ×3 each → 18 unique page templates
```

---

## 🤖 The 4-Agent Pipeline · 4 Agent 流水线

Not a single-prompt black box. Four agents with clear-cut jobs and engineering safety nets.
不是单一 prompt 黑盒，是 4 个职责明确的 Agent + 工程化兜底。

| Stage | Job · 职责 | Hard Constraint · 关键约束 |
|---|---|---|
| **1. Understand** · 理解 | Identify what the audience actually cares about, surface the spine, suggest tradeoffs · 找受众真正关心什么、提炼主线、给取舍建议 | Outputs *judgment*, not content · 只产判断不产内容 |
| **2. Structure** · 结构 | Page-by-page outline, core question per slide, time budget, narrative arc · 逐页大纲、每页核心问题、时间预算、叙事弧 | One question per slide · 每页只回答一个问题 |
| **3. Express** · 表达 | Conclusion-first, body ≤ 60 chars, bullet ≤ 15 chars, strip "AI smell" · 结论先行、正文≤60字、bullet≤15字、去 AI 味 | Hard char limits + anti-cliché word list · 字数硬上限 + 反套话词表 |
| **4. Render** · 渲染 | Spec-compliant interactive HTML, content unchanged · 按规范出交互式 HTML，内容不变 | Post-processing enforces brand & page numbers · 后处理强制统一品牌/页码 |

### 🛡 Engineering Safety Nets

Real production needs more than happy-path prompts. PPTFlux ships with:

- **Per-page recovery** for missing slides · 漏页单页恢复
- **Slot-map content addressing** to prevent layout drift · slot-map 内容寻址防错位
- **`sanitizeAgentSlide` post-processor** for consistency · 后处理统一格式
- **`isValidSlideHtml` content validator** · 内容有效性校验
- **`retrySinglePage` for one-off failures** · 单页失败重试

See [CHANGELOG.md](./CHANGELOG.md) for what each iteration actually fixed.
迭代细节见 [CHANGELOG.md](./CHANGELOG.md)。

---

## 🚀 Quick Start

### Option A — Use the live demo · 直接用在线 demo

👉 **[wilingna.github.io/PPTFlux](https://wilingna.github.io/PPTFlux/)**

### Option B — Run locally · 本地运行

```bash
git clone https://github.com/wilingna/PPTFlux
cd PPTFlux
open index.html   # macOS · or just double-click
```

That's it. Single HTML file, vanilla JS, zero build, zero dependencies.
就这么简单。单文件 HTML，原生 JS，零构建，零依赖。

### Then · 然后

1. Open Settings, paste your **OpenRouter API key** ([get one](https://openrouter.ai/keys)) · 在设置里填入 OpenRouter API Key
2. Pick a style, paste your notes, hit generate · 选风格、填资料、生成
3. Edit the writing layer → re-render → present, print to PDF, or download the HTML to keep tweaking · 改文案 → 重渲染 → 演示 / 打印 PDF / 下载 HTML 继续魔改

> 💡 **Recommended models**: Claude Opus 4 / Sonnet 4 via OpenRouter. Weaker models tend to break at Agent 3–4 (long context + strict instruction following).
> 💡 **推荐模型**：Claude Opus 4 / Sonnet 4。弱模型在 Agent 3-4 容易翻车（长上下文 + 强指令遵循）。

---

## 📖 The Story · 三次跃迁

If you're also building "AI makes slides" tools, this evolution might resonate.
如果你也在做"AI 做 PPT"这件事，这条演进路径或许能给你启发。

### 🥇 [ai-ppt-toolkit](https://github.com/wilingna/ai-ppt-toolkit) — The Methodology

**Three tools, three jobs**: NotebookLM (outline) + Gemini (polish) + Gamma (render).

Each tool does its part. You learn that "AI for slides" is not a single-prompt problem.
每个工具各司其职。学到了"AI 做 PPT"不是一句 prompt 能解决的事。

### 🥈 [ai-ppt-web](https://github.com/wilingna/ai-ppt-web) — The First Merge

**Claude replaces the first two tools. One web page + Gamma.** Three tools collapsed into two. Manual relay collapsed into auto-handoff. But you still jump out for visuals.
Claude 吃掉前两步，一个网页 + Gamma。三个工具压成两个，但视觉那一步还是断点。

### 🥉 PPTFlux — The Loop Closes

**4 agents. One page. No Gamma.**
The visual layer becomes part of the system itself — 6 design languages, 18 layouts, animated HTML, two layers of editability.
4 个 Agent，一个网页，连 Gamma 都不需要了。视觉层被吸进系统本身——6 套设计、18 种排版、动态 HTML、两层编辑权。

> **toolkit teaches the *why*. ai-ppt-web makes it *faster*. PPTFlux makes it *one-shot and fully controllable*.**
> **toolkit 帮你理解"为什么"，ai-ppt-web 帮你"快一点"，PPTFlux 帮你"一气呵成 + 完全可控"。**

All three repos can coexist — pick the one that fits your stage.
三个仓库可以并存，按你的阶段选。

---

## ❓ FAQ

<details>
<summary><b>Q: Why HTML instead of PPTX / Keynote? · 为什么是 HTML 而不是 PPTX？</b></summary>

**EN** — Because HTML is the only format that's simultaneously presentable, editable, scriptable, and durable. PPTX locks you into PowerPoint's editor and renders animations inconsistently across machines. PPTFlux supports presenting in-browser, printing to PDF, and downloading the HTML — but it intentionally won't export to PowerPoint. That's not the design goal.

**中文** — 因为 HTML 是唯一同时具备「可演示 + 可编辑 + 可脚本化 + 可长期保存」的格式。PPTX 把你锁在 PowerPoint 编辑器里，动画跨机器渲染还不一致。PPTFlux 支持浏览器演示、打印 PDF、下载 HTML——但故意不导 PPTX，这不是这个项目的方向。

</details>

<details>
<summary><b>Q: Is my API key safe? · API Key 安全吗？</b></summary>

Stored in your browser's localStorage only. Code is fully open-source — audit it. No third-party server in the request chain.
只存在你本地浏览器的 localStorage，代码全开源可审计，请求链路里没有任何第三方服务器。

</details>

<details>
<summary><b>Q: How much does one deck cost? · 跑一次多少钱？</b></summary>

Roughly **$0.10–$0.30** per full run, depending on input length and model choice. A $5 OpenRouter top-up lasts a long time.
单次大约 **$0.10-0.30**（看资料长度和模型）。OpenRouter 充 $5 能用很久。

</details>

<details>
<summary><b>Q: Got `API error 401: User not found` · 报 401 错误？</b></summary>

Your OpenRouter key is invalid or your account is out of credit. Regenerate at [openrouter.ai/keys](https://openrouter.ai/keys). Not a PPTFlux bug.
OpenRouter Key 失效或账户余额为零。去 [openrouter.ai/keys](https://openrouter.ai/keys) 重新生成。不是 PPTFlux 的 bug。

</details>

<details>
<summary><b>Q: A slide came out blank · 某页空白？</b></summary>

Post-v0.1 we added per-page retry + local fallback. Weak models can still trip it. Switch to Claude Sonnet 4 or Opus 4 and it should disappear.
v0.1 之后已加单页重试 + 本地兜底，但弱模型仍可能触发。换 Claude Sonnet 4 或 Opus 4 基本不再出现。

</details>

---

## 🛠 Tech Stack

- **Single-file HTML + Vanilla JS** — no build, no framework, no dependencies
- **OpenRouter API Gateway** — one key, all major models
- **Claude Opus / Sonnet** — recommended for Agent 3–4 reliability
- **GitHub Pages deploy** — the entire project is one `index.html`

---

## 🛣 Roadmap

- [ ] More design languages (currently 6, targeting 10+)
- [ ] Live collaboration mode
- [ ] Speaker notes generation
- [ ] Custom theme via JSON config
- [ ] Localization for English-language outputs

Have an idea? [Open an issue](https://github.com/wilingna/PPTFlux/issues) · 有想法？[提个 issue](https://github.com/wilingna/PPTFlux/issues)

---

## 🤝 Contributing

PRs welcome — especially new design languages and layout variants. Each style lives in its own self-contained module, so adding one means adding a file, not refactoring the world.
欢迎 PR，尤其欢迎新的设计风格和排版变体。每套风格是独立模块，加一个不会牵动全局。

---

## 📜 License

MIT — use it, fork it, ship it. Just don't blame me.

---

## 👋 About

Built by **wilingna** ([@wilingna](https://github.com/wilingna))
Big-tech HR turned AI Systems Architect. Building AI workflows and Chinese-aesthetic digital culture for global audiences.
大厂 HR 出身的 AI Systems Architect，做 AI 工作流 / 中国传统美学数字文化出海。

### My Other Projects · 其他项目

| Repo | What it does |
|---|---|
| [ai-ppt-toolkit](https://github.com/wilingna/ai-ppt-toolkit) | The original 3-tool methodology · 三件套工作流原版 |
| [ai-ppt-web](https://github.com/wilingna/ai-ppt-web) | Web-based 2-tool version · 三件套网页版 |
| [ai-decision-5steps](https://github.com/wilingna/ai-decision-5steps) | High-quality decisions in 5 AI-powered steps · 5 步 AI 高质量决策 |
| [ai-content-pipeline](https://github.com/wilingna/ai-content-pipeline) | 7-agent content production pipeline · 7 Agent 内容生产线 |

---

<div align="center">

### ⭐ If PPTFlux saved you a tool-hopping afternoon, drop a star.
### ⭐ 如果 PPTFlux 帮你省了一下午接力搬运，点个 star 吧。

**Better — fork it, remix the design languages, make it yours.**
**更好的方式——fork 它，魔改设计风格，做成你自己的。**

</div>
