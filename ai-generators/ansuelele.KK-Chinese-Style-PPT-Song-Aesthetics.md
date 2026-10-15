# KK中国风PPT生成系统：宋代美学版

> 使用 ChatGPT Images 2.0 生成完整 16:9 PPT 页面图，再封装为 PPTX、PDF、网页 PPT 三件套。

![KK中国风PPT生成系统：宋代美学版](assets/hero.png)

## 这是什么

**KK中国风PPT生成系统：宋代美学版** 不是普通的“背景图 + 后贴文字”PPT 工具，而是一套 **整页视觉生成系统**。

默认工作方式是：

1. 先为每一页设计标题、文案、构图和视觉叙事。
2. 使用 **ChatGPT Images 2.0** 直接生成完整的 16:9 PPT 页面图。
3. 将每一页完整页面图封装进 PPTX。
4. 同步交付 PDF 和网页 PPT。

也就是说，用户拿到的 PPTX 默认是“每页一张完整视觉图”的演示文稿。这样能最大程度保留 ChatGPT Images 2.0 的排版、字体、光影、材质和整体美感。

## 默认交付

```text
output/
  deck.pptx
  deck.pdf
  web/
    index.html
    assets/
      slides/
        01.png
        02.png
        ...
  notes.md
```

- `deck.pptx`：每页放入一张完整 16:9 页面图，适合演讲和分享。
- `deck.pdf`：锁版展示文件，视觉最稳定。
- `web/index.html`：网页 PPT，用于在线浏览。
- `notes.md`：保存每页标题、正文、整页图提示词、修改建议。

## 重要说明

本系统默认 **不把 ChatGPT Images 2.0 生成的图当背景，再用普通文本框后贴文字**。

原因很简单：后贴文字很容易破坏整体设计，变成“漂亮图片 + 丑文字框”。本系统追求的是 ChatGPT Images 2.0 一次性生成的整页视觉效果。

如果用户明确要求“文字可编辑”，才启用可编辑模式。可编辑模式会牺牲一部分美感。

## 推荐用法

### 方式一：把本仓库交给支持读取 GitHub 的智能体

适合 Codex、Claude Code、OpenClaw，以及其他可以读取 GitHub 仓库、运行代码或生成文件的 AI 智能体。

把下面这段话发给你的智能体：

```text
请读取这个 GitHub 仓库：
https://github.com/ansuelele/KK-Chinese-Style-PPT-Song-Aesthetics

请使用仓库中的 SKILL.md、universal-prompt.md 和 references/ 规则，为我生成一套「宋代茶文化」主题 PPT。

要求：
- 风格：KK中国风PPT生成系统：宋代美学版
- 默认模式：ChatGPT Images 2.0 整页生成模式
- 页数：12 页
- 比例：16:9
- 语言：中文
- 受众：高中生
- 用途：课堂展示
- 交付：PPTX、PDF、网页 PPT 三件套

请为每一页先设计标题、文案、构图和视觉说明，然后优先使用 ChatGPT Images 2.0 直接生成完整 16:9 PPT 页面图。不要默认生成背景图后再用普通文本框叠加文字。PPTX 中每页应放入对应的完整页面图。

如果当前环境不能调用 ChatGPT Images 2.0，请输出每页完整页面图提示词，并继续生成可复现的交付包。
```

### 方式二：在 Codex / Claude Code 中作为 Skill 使用

让智能体读取本仓库根目录的 `SKILL.md`，并按 `references/` 中的规则执行。核心要求是：**整页图优先，文件封装其次**。

### 方式三：普通 AI 工具复制通用提示词

适合 ChatGPT、Claude、Kimi、豆包、通义千问、腾讯元宝、Minimax 等普通对话式 AI 工具。

如果 AI 工具不能读取 GitHub 仓库，就打开 [`universal-prompt.md`](universal-prompt.md)，复制完整内容，再补充主题、受众、页数和用途。

## 它不是只靠一段提示词

本项目的核心是：

- ChatGPT Images 2.0 整页 PPT 视觉生成协议
- 宋代美学视觉系统
- 页面叙事与整页图提示词规则
- PPTX / PDF / 网页 PPT 三件套封装规则
- 多智能体能力降级机制
- 示例图风格校准

提示词只是入口，仓库里的规则和示例才是系统主体。

## 效果预览

以下示例展示系统希望达到的整页视觉气质：克制、暗光、器物、质感、留白、题跋感。

| 封面 | 建盏 |
|---|---|
| ![封面](examples/jianshan-tenmoku/09.png) | ![建盏](examples/jianshan-tenmoku/01.png) |

| 地理 | 铁胎 |
|---|---|
| ![建窑地理](examples/jianshan-tenmoku/02.png) | ![铁胎](examples/jianshan-tenmoku/03.png) |

| 兔毫 | 油滴 |
|---|---|
| ![兔毫](examples/jianshan-tenmoku/04.png) | ![油滴](examples/jianshan-tenmoku/05.png) |

| 曜变 | 斗茶 |
|---|---|
| ![曜变](examples/jianshan-tenmoku/06.png) | ![斗茶](examples/jianshan-tenmoku/07.png) |

## 工作流程

```mermaid
flowchart LR
  A["输入主题与需求"] --> B["读取仓库规则"]
  B --> C["设计整套叙事结构"]
  C --> D["逐页设计标题、文案、构图"]
  D --> E["ChatGPT Images 2.0 生成完整页面图"]
  E --> F["页面图封装为 PPTX"]
  F --> G["导出 PDF 和网页 PPT"]
  G --> H["保存 notes.md 与降级说明"]
```

## 目录说明

```text
.
├─ README.md
├─ universal-prompt.md
├─ SKILL.md
├─ references/
│  ├─ compatibility.md
│  ├─ delivery-rules.md
│  ├─ image-prompts.md
│  ├─ layouts.md
│  └─ style-system.md
├─ assets/
│  └─ hero.png
└─ examples/
   └─ jianshan-tenmoku/
      ├─ 01.png
      ├─ 02.png
      └─ ...
```

## 适配对象

| 当前能力 | 交付结果 |
|---|---|
| 能读取仓库、使用 ChatGPT Images 2.0、生成文件 | 整页图 PPTX + PDF + 网页 PPT + notes.md |
| 能读取仓库、不能调用 ChatGPT Images 2.0 | 每页完整页面图提示词 + 可复现交付包 |
| 能生成图片，不能生成 PPTX | 完整页面图 + 网页 PPT 或制作说明 |
| 只能文字输出 | 页面方案 + 每页整页图提示词 + 交付清单 |

## 宋代美学方向

本系统强调：

- 留白、低声量、高质感
- 器物、纸张、墨色、青瓷、暗金、窑火
- 册页、长卷、题跋、展陈、文人案头
- 中文标题短、慢、稳
- 每页像一张完整设计稿，而不是背景图加文字框

避免：

- 廉价国潮风
- 大红大金堆叠
- 龙纹、祥云、宫廷纹样滥用
- 满屏水墨背景加白字
- 后贴文本框破坏画面
- 过度装饰边框

## 系列计划

这是 **KK中国风PPT生成系统** 的第一套风格包。后续可以扩展为：

- KK中国风PPT生成系统：宋代美学版
- KK中国风PPT生成系统：敦煌美学版
- KK中国风PPT生成系统：唐风华彩版
- KK中国风PPT生成系统：水墨山水版
- KK中国风PPT生成系统：明式雅集版
- KK中国风PPT生成系统：博物馆展陈版
- KK中国风PPT生成系统：新中式商业版

每个风格包都可以复用同一套核心协议：整页图生成、三件套封装、图像降级、风格自检、系列化 README。

## 使用提醒

- 本仓库本身不是在线生成器，需要交给 AI 智能体读取或复制提示词使用。
- 默认 PPTX 是整页图片型 PPT，文字不可直接编辑。
- 如果要修改文字，建议重新生成对应页面图。
- PDF 用于锁版展示，是最终视觉校准版本。
- 网页 PPT 用于高表现力预览和在线演示。
- 若使用历史文物、博物馆图像或外部素材，请自行确认版权与引用规范。

