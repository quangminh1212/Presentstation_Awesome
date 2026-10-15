# SU-Ray Beamer Theme — User Guide / 中文使用指南

An unofficial adaptive academic presentation theme tailored for **Stockholm University (Department of Computer and Systems Sciences - DSV)**. This theme aligns with SU's official visual identity.

本模板是一款专为**斯德哥尔摩大学计算机与系统科学系 (DSV)** 师生定制的学术报告 Beamer 模板。遵循斯大官方视觉文档。

---

## Language Navigation / 语言快速跳转
* [English Version Documentation](#english-version-documentation)
* [中文版使用说明](#中文版使用说明)

---

# English Version Documentation

[![Open in Overleaf](https://img.shields.io/badge/Open%20in-Overleaf-green.svg)](https://www.overleaf.com/read/jcbkrkrjftwm#a96fba)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.1.0-blue.svg)](https://github.com/raysuzeyu-lgtm/su-dsv-beamer/releases/tag/V1.1.0)

Before using this template, please check the Graphic Profile from SU:
https://medarbetare.su.se/en/our-su/communicate-su/graphic-profile/logotype

* **Author:** Zeyu Su (Ray SU)
* **Release Date:** June 2026
* **Engine Compatibility:** Best compiled with `pdfLaTeX` or `XeLaTeX` (ensure `lmodern` font package is integrated).

##  Required Asset Folder Structure
Before compilation, ensure your root directory contains a `logo/` folder with the following official vector assets. The theme will dynamically invoke them based on your language/theme arguments:


```text
├── main.tex
├── SU-Ray.sty
└── logo/
    ├── su_vert_en_blue.png        # Official English vertical logo (Blue)
    ├── su_vert_en_white.png       # Official English vertical logo (White)
    ├── su_vert_sv_blue.png        # Official Swedish vertical logo (Blue)
    ├── su_vert_sv_white.png       # Official Swedish vertical logo (White)
    ├── su_horiz_en_blue.png       # Official English horizontal logo (Blue)
    ├── su_horiz_en_white.png      # Official English horizontal logo (White)
    ├── su_horiz_sv_blue.png       # Official Swedish horizontal logo (Blue)
    ├── su_horiz_sv_white.png      # Official Swedish horizontal logo (White)
    ├── watermark_olive_blue.png   # Stockholm Olive branch watermark (Blue)
    ├── watermark_olive_white.png  # Stockholm Olive branch watermark (White)
    ├── watermark_flame_blue.png   # Stockholm Flame emblem watermark (Blue)
    └── watermark_flame_white.png  # Stockholm Flame emblem watermark (White)

```

## Package Options

Load the package in your `main.tex` using the following syntax:

```latex
\usepackage[option1, option2]{SU-Ray}

```

### 1. Language Configuration

* **`english`** *(Default)*: Uses English infrastructure, targets English institutional logos, and sets the closing phrase to *"Thank you for your attention!"*.
* **`swedish`**: Switches branding to Swedish templates and updates the closing phrase to *"Tack för er uppmärksamhet!"*.

### 2. Canvas Mode Configuration (Affects Title, Section & End frames)

* **`light`** *(Default)*: Traditional premium theme. Canvas yields a clean white background with official deep-blue elements. Watermark opacities are carefully tuned to a low 0.05 for supreme text legibility.
* **`dark`**: High-end midnight theme. Special frames switch to an immersive SU Deep Blue (`SUblue`) environment. Watermark opacities automatically step up to 0.15 to contrast beautifully with the dark background.

> *Note: Regular text content slides remain strictly white (`bg=white`) across both options to protect reading comfort and mathematical visibility.*

##  Core Macro Commands

### 1. Titlepage Metadata Setup

Place these configuration commands inside the preamble (before `\begin{document}`) to fill the title page slots:

* **`\title{...}`** & **`\subtitle{...}`**: Handles long titles seamlessly without layout collisions.
* **`\author{...}`**: Your name (e.g., `Ray SU`).
* **`\degreeproject{Master/Bachelor}{Program Name}`**: Custom structural block. Separates degree rank from the specialized division.
* **`\supervisor{Supervisor Name}`**: Automatically displays formatted supervisor credentials.
* **`\institute{...}`**: Department identity (e.g., `Department of Computer and Systems Sciences`).
* **`\date{...}`**: Presentation date (e.g., `June 2026`).

### 2. High-Level Page Invocation

* **`\SUtitlepage`**: Clears standard templates, injects the mirror-reflected Stockholm olive branch layout, and prints structural metadata.
* **`\SUtocpage[Title]`**: Renders an asymmetrical magazine-style Agenda frame. Takes an optional parameter to replace the title text (Defaults to `Outline`), bounded by an explicit *SU Fire Orange* pointing anchor line.
* **`\SUthankyou`**: Triggers the concluding frame with the horizontal master logo and automated localized gratitude typography.

##  Advanced Smart Features

### 1. Adaptive Mac OS Code Environment (`macode`)

The theme encapsulates a highly specialized, responsive IDE wrapper resembling a modern macOS code terminal, built on top of `tcolorbox` and `listings`.

* **Syntax:**

```latex
\begin{macode}[listings_options]{virtual_filename}{caption_text}
    // Your code snippets here
\end{macode}

```

* **Dynamic Adapting Matrix:**
* **Inside Frame Alignment:** Code numbers are forced inside the text container grid through precise margin indentation (`xleftmargin=1.8em`).
* **Light Mode:** Wraps codes in a warm `#F6F6F6` box. Comments show up in academic olive green, strings in active fire orange, and keywords in deep blue.
* **Dark Mode:** Swaps directly into a dark-hacker mode (`#1E1E1E` terminal pane). Text turns pure white, strings transition to an outstanding neon amber yellow (`#FFB86C`), and comments light up in soft sage green (`#7AAB7A`).
* **Float Captioning:** The 3rd parameter safely creates an external micro-caption attached cleanly under the window. Leave it empty `{}` to seamlessly mute it.



### 2. Auto-Hierarchical Section Numbers

Slide headers are programmatically aware of their presentation state:

* If no structural scope is opened: Displays title text normally (e.g., `Agenda`).
* If inside a `\section` block: Prepends absolute indexing (e.g., **1. Introduction**).
* If deep inside a `\subsection` block: Automatically calculates two-tier indexing (e.g., **2.1 Proposed Architecture**). Perfect for multiple-frame transitions.

### 3. Automated Section Progress Trackers

Whenever a new `\section{...}` declaration is encountered, the template automatically intercepts compilation to generate an elegant full-screen divider frame carrying the section ordinal index and its corresponding watermark archetype, maintaining narrative tempo.

## Official Color Palette Cheat Sheet

| Token Name | Hex Code | Visual Identity Usage |
| --- | --- | --- |
| `SUblue` | `#002F5F` | Primary branding color, blocks, section titles |
| `SUgrey` | `#333333` | Standard high-readability regular body text |
| `SUlightgrey` | `#F5F5F5` | Adaptive background fills, inner block canvas |
| `SUsky` | `#ACDEE6` | High-contrast dark mode highlighting tokens |
| `SUwater` | `#9BB2CE` | Code line numbers, muted sub-details |
| `SUolive` | `#A3A86B` | Example blocks, listings documentation references |
| `SUfire` | `#EB7125` | Critical alert states, `\alert{}` triggers, agenda accent line |

## Disclaimer & Branding Compliance

> * **Branding Authority:** This template is built with close reference to the Stockholm University Visual Identity Guidelines. Users are highly encouraged to review the official documentation linked above to ensure appropriate usage of university seals and emblems.
> * **Artistic Re-Interpretation:** For advanced presentation aesthetics, the template utilizes custom **deconstructed and mirror-reflected artistic variations** of background auxiliary patterns (the olive branch and flame). These designs are intended solely for graphic style explorations within academic contexts and do not substitute the official, non-deconstructed primary institutional logotypes.
> * **Status:** This is an **unofficial** third-party template developed independently. It is **NOT** officially endorsed, sponsored, or maintained by Stockholm University.
> * **MIT Open Source License Scope:** The MIT License applies **exclusively** to the LaTeX source code architecture (`SU-Ray.sty`). All Stockholm University institutional logos and corporate graphic assets within the `logo/` directory remain the sole intellectual property of Stockholm University.
> 
> 

---

# 中文版使用说明

##  目录结构要求

在编译之前，请确保项目的根目录下有一个 `logo/` 文件夹，并存放以下官方矢量素材。模板会根据你传入的语言和主题参数，自动动态调用它们：

```text
├── main.tex
├── SU-Ray.sty
└── logo/
    ├── su_vert_en_blue.png        # 官方英文竖版 Logo (蓝色)
    ├── su_vert_en_white.png       # 官方英文竖版 Logo (白色)
    ├── su_vert_sv_blue.png        # 官方瑞典文竖版 Logo (蓝色)
    ├── su_vert_sv_white.png       # 官方瑞典文竖版 Logo (白色)
    ├── su_horiz_en_blue.png       # 官方英文横版 Logo (蓝色)
    ├── su_horiz_en_white.png      # 官方英文横版 Logo (白色)
    ├── su_horiz_sv_blue.png       # 官方瑞典文横版 Logo (蓝色)
    ├── su_horiz_sv_white.png      # 官方瑞典文横版 Logo (白色)
    ├── watermark_olive_blue.png   # 斯大橄榄枝水印 (蓝色)
    ├── watermark_olive_white.png  # 斯大橄榄枝水印 (白色)
    ├── watermark_flame_blue.png   # 斯大火焰徽标水印 (蓝色)
    └── watermark_flame_white.png  # 斯大火焰徽标水印 (白色)

```

## 宏包参数配置

在你的 `main.tex` 中通过以下方式引入模板：

```latex
\usepackage[参数1, 参数2]{SU-Ray}

```

### 1. 语言配置 (Language)

* **`english`** *(默认)*: 激活英文教研基础设施，调用英文版校徽，并将尾页致谢自动设为 *"Thank you for your attention!"*。
* **`swedish`**: 切换为瑞典语本地化模式，调用瑞典语校徽，并将尾页致谢设为 *"Tack för er uppmärksamhet!"*。

### 2. 皮肤模式 (Canvas Mode - 仅影响首页、过渡页与尾页)

* **`light`** *(默认)*: 经典的优雅白底风格。特殊页面呈现干净的白底与官方深蓝视觉，水印透明度严格控制在 0.05，提供极佳的阅读呼吸感。
* **`dark`**: 黑色模式。特殊页面一键切换为沉浸式斯大深蓝（`SUblue`）环境。水印透明度自动提升至 0.15，在深色背景下层次分明。

> **重要注记：** 无论选择哪种模式，正文内容页均保持绝对高清晰度的纯白背景 (`bg=white`)，以确保长篇数学公式与学术文本的绝对可读性。

##  核心命令与填空区

### 1. 首页元数据设置

在编译前（即 `\begin{document}` 之前），填写以下命令以生成标准的答辩首页内容：

* **`\title{...}`** & **`\subtitle{...}`**: 支持超长主副标题，内置边界防御，绝不发生排版重叠。
* **`\author{...}`**: 演讲者姓名（例如：`Ray SU`）。
* **`\degreeproject{学位级别}{专业方向}`**: 专属结构化区块。例如 `{Master}{Data Science}`，自动规范化多行排版。
* **`\supervisor{导师姓名}`**: 自动格式化输出导师信息。
* **`\institute{...}`**: 学院/部门名称（例如：`Department of Computer and Systems Sciences`）。
* **`\date{...}`**: 报告日期（例如：`June 2026`）。

### 2. 页面宏

* **`\SUtitlepage`**: 专属首页，包含右下角水平翻转的巨幅半透明橄榄枝镜像系统。
* **`\SUtocpage[自定义标题]`**: 非对称杂志风目录页。参数可选（默认显示 `Outline`），左栏带有标志性的*斯大火橙色*装饰短线。
* **`\SUthankyou`**: 华丽尾页，自动居中横版矢量 Logo，并根据语言输出本地化致谢。

##  核心功能

### 1. 自适应 Mac OS 窗口代码环境 (`macode`)

基于 `tcolorbox` 与 `listings` 深度重构，专为计算机专业师生打造。

* **语法结构:**

```latex
\begin{macode}[代码语言]{顶部窗口文件名}{底部说明题注}
    // 在这里直接粘贴你的源代码
\end{macode}

```

* **智能自适应矩阵:**
* **行号内置**: 通过 `xleftmargin=1.8em` 核心算法，强行将原本挂在框外的行号收进代码板内部，排版极其整齐。
* **浅色模式下**: 代码框呈现微灰（`#F6F6F6`）质感，关键字为官方蓝，注释为学术绿，字符串为火橙色。
* **黑色模式下**: 自动激活 **VS Code 黑色主题**（`#1E1E1E` 极客面板）。文字自动变白，关键字转为明亮的天蓝色，最关键的是，**彻底修复了原生 Listings 字符串在黑底上变黑无法识别的 Bug**，将其升级为高对比度的霓虹琥珀黄（`#FFB86C`）。
* **悬浮题注**: 第三参数 `{底部说明题注}` 会在 Mac 窗口外部正下方生成优雅的居中题注。如果留空 `{}`，则会自动隐藏，不留一丝多余间距。



### 2. 智能多级章节序号抬头

幻灯片正页抬头（Frametitle）具有环境感知功能：

* 未进入章节时：正常显示文本。
* 处于 `\section` 作用域时：抬头自动前缀一级序号（如：**1. Introduction**）。
* 处于 `\subsection` 作用域时：抬头自动升格为双级序号（如：**2.1 Proposed Architecture**）。

### 3. 全自动进度分割页

每当你声明一个新的 `\section{...}`，模板都会自动拦截编译，为你生成一页极具视觉冲击力的全屏数字过渡页，左下角伴有斯大精神徽标（火焰）水印，掌控演说节奏。

## 免责声明与品牌合规说明 (Disclaimer)

> * **品牌合规性:** 本模板的设计与色彩体系严格参考了斯德哥尔摩大学官方视觉识别系统规范（Visual Identity Guidelines）。建议使用者在使用前阅读官方规范，以确保校徽及相关标识的使用处于合理范围内。
> * **艺术化再创作说明:** 为了追求更现代、更具视觉呼吸感的学术演讲效果，本模板对背景中的装饰性辅助图形（如橄榄枝、火焰图案）进行了**半透明艺术化拆分与镜像演变处理**。此类处理仅作为学术讨论环境下的审美探索，不代表官方未经拆解的正式校徽本体。
> * **法律地位:** 本模板为个人独立开发的**非官方**第三方开源项目，并未获得斯德哥尔摩大学官方的正式背书、赞助或维护。
> * **MIT 开源许可证范围:** 本项目的 MIT 开源许可证**仅适用于** LaTeX 源码架构代码（`SU-Ray.sty`）。`logo/` 目录下的所有斯德哥尔摩大学官方校徽、标识及衍生图形资产，其知识产权与最终解释权均归斯德哥尔摩大学官方所有。
> 
> 

---

## Git Repository Configuration (.gitignore)

To keep your GitHub repository clean, it is highly recommended to include a `.gitignore` file in your root folder to automatically ignore LaTeX compilation temporary files:
为了保持 GitHub 仓库的整洁，强烈建议在根目录下创建一个 `.gitignore` 文件，自动忽略以下 LaTeX 编译产生的临时文件：

```text
*.aux
*.log
*.toc
*.nav
*.snm
*.out
*.fdb_latexmk
*.fls
*.synctex.gz
*.bbl
*.blg
*.thm
*.pre

```