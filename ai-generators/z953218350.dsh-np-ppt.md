# DSH NP-PPT 演示文稿专家插件 (dsh-np-ppt)

> 🌐 **中文** · [English](#english)
>
> DSH（DeepSeek Harness）原生专用的全功能 **PPT 演示文稿专家** 插件。内置 PPTD DSL 引擎、55173 所见即所得可视化编辑器服务、Python-PPTX 高保真离线编译内核与一键导出 PPTX 功能。

<p align="center">
  <a href="https://github.com/topics/deepseek-harness"><img src="https://img.shields.io/badge/topic-deepseek--harness-blue" alt="deepseek-harness"></a>
  <a href="https://github.com/topics/dsh"><img src="https://img.shields.io/badge/topic-dsh-8A2BE2" alt="dsh"></a>
  <a href="https://github.com/topics/dsh-plugin"><img src="https://img.shields.io/badge/topic-dsh--plugin-2EA043" alt="dsh-plugin"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-22c55e" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-22c55e" alt="license">
</p>

---

## ✨ 核心特性

1. **🎭 9 大专业视觉风格体系**
   - 👔 商务管理风（墨绿+黄铜金）
   - 💻 深浅代码风（极客终端黑/蓝灰+亮绿）
   - 🚀 高能增长风（活力橙+稳重深蓝）
   - 🔮 炫光紫绿风（暗黑底色+电光紫绿）
   - 📑 冷白调研风（瑞士极简白底+细黑线+红点缀）
   - 📱 轻拟态风（柔和浅灰白+微质感卡片+科技蓝）
   - 👑 黑金实验风（曜石黑+奢华哑光金）
   - 📊 色谱图表风（纯净白底+多维对比色谱）
   - 📖 深蓝杂志风（深海蓝底+金句引述+画册感）

2. **🛠️ 模块化 PPTD 架构与标准 16:9 画布**
   - 采用清晰的 YAML 语法 DSL，解耦 OOXML 复杂逻辑，单个页面（`01_cover.page` ~ `XX_final.page`）完全独立自洽；
   - 自动添加淡入淡出（Fade）幻灯片平滑切换过渡。

3. **🖥️ 55173 所见即所得可视化编辑器**
   - 内置轻量级本地 Web 编辑器（`http://127.0.0.1:55173/`）；
   - 支持多层嵌套富文本修改、自由拖拽对齐与实时渲染；
   - **无缝集成**：点击右上角「导出」弹窗中的「下载」即可直接触发本地高保真 Python-PPTX 编译引擎下载文件；选择「图片」时保持原生图片切图下载。

4. **⚡ 高保真离线原生编译内核（Python-PPTX）**
   - 基于 `RichTextHTMLParser` 状态机，完美支持无限层级嵌套 HTML 标签（`<span>`、`<strong>`、`<b>`、`<em>`、`<i>`、`<u>`、`<br/>`）与全格式颜色（`#HEX`、`rgb()`、`rgba()`、`$theme`）；
   - 微软雅黑字族锁定（`Microsoft YaHei`）、DrawingML 渐变背景、`noAutofit` 文本框防缩放。

---

## 📦 目录结构

```text
dsh-np-ppt/
├── package.json                   # 插件元信息与导出入口
├── tsconfig.json                  # TypeScript 编译配置（输出至 lib/）
├── cordis.patch.yml               # DSH / Cordis 插件注册清单
├── src/                           # TypeScript 源码
│   ├── index.ts                   # 插件 Host 入口（Prompt 注入、服务治理、工具导出）
│   ├── service.ts                 # 55173 编辑器 Web 服务与 Python 编译桥接
│   ├── tools.ts                   # 原生 Agent Tools（ppt_export, ppt_serve 等）
│   └── client/                    # DSH Web 前端插件扩展
├── lib/                           # 预编译 ESM 代码（即装即用，无需构建）
├── compiler/
│   └── export_pptx.py             # 高保真 Python-PPTX 离线编译引擎
├── editor/                        # 55173 本地可视化编辑器静态资源
│   ├── index.html                 # 编辑器宿主页面
│   ├── app.js                     # 前端交互逻辑
│   ├── lib.js                     # 编辑器辅助库
│   └── styles.css                 # 编辑器样式
├── presets/                       # Agent 预设（Persona & System Prompt）
│   ├── preset.yml                 # 「PPT 演示文稿专家」预设定义
│   └── agent.cordis.yml           # 完整 Agent 配置（persona、工具、plan mode 等）
└── README.md                      # 本文件（中文 + English）
```

---

## 🧩 环境要求

| 依赖项 | 要求 | 说明 |
|---|---|---|
| **DSH (DeepSeek Harness)** | 已安装并能运行 `dsh` 命令 | 插件通过 `dsh plugin --profile web add` 挂载到 web profile，依赖 DSH 提供的 Cordis loader、systemPrompt 注入、Agent 工具等宿主能力 |
| **Node.js** | 与你的 DSH 版本自带/要求的 Node 一致（插件代码使用 ESM，需 Node 16+，推荐 18+） | 插件加载与 55173 编辑器服务由 Node.js 驱动；`lib/` 为预编译 ESM，无需自行构建 |
| **pnpm** | DSH profile 默认使用的 pnpm（随 DSH 自带） | 挂载安装走 `dsh plugin` → pnpm link；workspace 根目录需加 `-w` 标志 |
| **Python** | 3.x（需可在命令行通过 `py -3` / `python3` / `python` 之一调用） | 高保真离线 PPTX 编译内核由 Python 驱动；插件会自动探测可用的 Python 命令 |
| **Python 依赖** | `pyyaml`、`python-pptx` | 首次运行编译器时会自动通过 pip 安装到临时目录（缺网/缺 pip 时可手动 `pip install pyyaml python-pptx`） |
| **浏览器** | 推荐 Chrome / Edge 等支持 File System Access API 的现代桌面浏览器 | 55173 编辑器使用 `window.showDirectoryPicker()` 等能力授权本地目录读写；不支持该 API 的浏览器会降级为只读上传模式 |

> 💡 仅做"对话生成 + 命令行编译导出 PPTX"时，浏览器不是必须；但要在 55173 可视化编辑器中拖拽对齐、实时渲染并一键下载，建议使用 Chrome/Edge 桌面版。

---

## 🔌 安装与激活方法

> 以下示例中 `<项目路径>` 表示本插件在你本机的目录路径，安装时请按实际位置替换。

### 方式一：通过 DSH 命令行挂载（推荐）
在终端中指定 `--profile web` 执行安装挂载：
```bash
dsh plugin --profile web add link:<项目路径>
```
> 在 pnpm workspace 根目录下添加时可能需要附加 `-w/--workspace-root` 参数，例如：
> `dsh plugin --profile web add -w link:<项目路径>`

### 方式二：手动配置到 DSH 配置文件
在 `~/.dsh/profiles/web/cordis.patch.yml` 中添加：
```yaml
- insert:
    - id: dsh-np-ppt
      name: 'dsh-np-ppt'
```
并在 `~/.dsh/profiles/web/node_modules/` 下建立指向 `<项目路径>` 的符号链接（Windows 用 Junction / mklink /J，macOS·Linux 用 ln -s）。

安装完成后，重启当前 web profile（在运行 `dsh web` 的终端按 `Ctrl+C` 后重新执行 `dsh web`）即可加载插件。

---

## 🚀 使用指南

插件装载成功后，DSH Web GUI 中会新增一个自定义 Agent 预设 —— **「PPT 演示文稿专家」**。该预置内置了完整的 PPTD DSL 编写规范、9 大风格主题说明、本地编译与 55173 编辑器联动指引，并自动注入到系统提示词，使 AI 直接具备演示文稿创作能力；脚本同时把预设文件复制到 `~/.dsh/.agent-presets/np-ppt/` 以便离线复用。

### 1. 对话驱动生成
在 DSH Web GUI 中切换到 **PPT 演示文稿专家** 预设，直接与 AI 对话：
> "帮我用科技蓝风格做一份 8 页的《微服务架构重构技术方案》"

### 2. 本地可视化编辑与导出
1. 在浏览器中打开 `http://127.0.0.1:55173/`；
2. 点击「打开 PPTD 文件夹」，授权选择包含 `deck.pptd` 的项目目录；
3. 直接在页面中进行文字修改、排版调整；
4. 点击右上角「导出」-> 选择 PPT -> 点击「下载」，即可下载高保真 PPTX 幻灯片。

### 3. 命令行直接编译
在 PPTD 项目目录下直接运行内置编译器：
```bash
py -3 <项目路径>/compiler/export_pptx.py deck/deck.pptd --output deck/deck.pptx --force
```
> macOS / Linux 下请使用 `python3`：
> `python3 <项目路径>/compiler/export_pptx.py deck/deck.pptd --output deck/deck.pptx --force`
> 首次运行若无 `pyyaml` / `python-pptx`，脚本会自动通过 pip 安装。

---

<br>

---

# English

> ⬆️ [中文](#dsh-np-ppt-演示文稿专家插件-dsh-np-ppt)

A native full-featured **Presentation & Slide Design Expert** plugin for [DSH (DeepSeek Harness)](https://github.com/topics/deepseek-harness).
Built-in PPTD DSL engine, 55173 WYSIWYG visual editor service, Python-PPTX high-fidelity offline compiler, and 1-click PPTX export.

---

## ✨ Key Features

1. **🎭 9 Preset Professional Visual Design Systems**
   - 👔 Business Management (Emerald + Brass Gold)
   - 💻 Geek / Code Theme (Terminal Slate + Bright Green)
   - 🚀 High-Energy Growth (Vibrant Orange + Deep Navy)
   - 🔮 Electric Violet (Cyber Dark + Neon Violet/Cyan)
   - 📑 Swiss Minimalist (Pure White + Fine Black Line + Red Accent)
   - 📱 Neomorphic Tech (Soft Light Gray + Card Glass + Tech Blue)
   - 👑 Obsidian & Gold (Matte Black + Luxury Satin Gold)
   - 📊 Metric Spectrum (Pure White + Multidimensional Spectrum)
   - 📖 Deep Blue Pictorial (Deep Sea Blue + Quote Callouts + Editorial Feel)

2. **🛠️ Modular PPTD DSL Architecture (16:9 Canvas)**
   - Clean YAML DSL abstracting OOXML, self-contained modular slides (`01_cover.page` ~ `XX_final.page`).
   - Automatic slide-level fade transitions.

3. **🖥️ 55173 WYSIWYG Visual Editor**
   - Integrated lightweight local Web editor at `http://127.0.0.1:55173/`.
   - Multi-level nested rich-text editing, free drag-and-drop alignment, real-time rendering.
   - Seamless export interception: clicking "Download" inside the top-right "Export" dialog directly triggers the local high-fidelity Python-PPTX compiler; choosing "Image" keeps the native image-slice download.

4. **⚡ High-Fidelity Python-PPTX Native Compiler**
   - Integrated `RichTextHTMLParser` supporting infinite nesting HTML tags (`<span>`, `<strong>`, `<b>`, `<em>`, `<i>`, `<u>`, `<br/>`) and CSS colors (`#HEX`, `rgb()`, `rgba()`, `$theme`).
   - Microsoft YaHei font locking, DrawingML gradient backgrounds, and `noAutofit` text frames.

---

## 📦 Directory Structure

```text
dsh-np-ppt/
├── package.json                   # Plugin metadata & export entry
├── tsconfig.json                  # TypeScript build config (outputs to lib/)
├── cordis.patch.yml               # DSH / Cordis plugin registration manifest
├── src/                           # TypeScript sources
│   ├── index.ts                   # Plugin Host entry (prompt injection, service, tools export)
│   ├── service.ts                 # 55173 editor web service & Python compiler bridge
│   ├── tools.ts                   # Native Agent Tools (ppt_export, ppt_serve, etc.)
│   └── client/                    # DSH Web front-end plugin extension
├── lib/                           # Pre-compiled ESM (ready to use, no build needed)
├── compiler/
│   └── export_pptx.py             # High-fidelity Python-PPTX offline compiler
├── editor/                        # 55173 local visual editor static assets
│   ├── index.html                 # Editor host page
│   ├── app.js                     # Front-end interaction logic
│   ├── lib.js                     # Editor helper library
│   └── styles.css                 # Editor styles
├── presets/                       # Agent presets (Persona & System Prompt)
│   ├── preset.yml                 # "Presentation Expert" preset definition
│   └── agent.cordis.yml           # Full agent config (persona, tools, plan mode, etc.)
└── README.md                      # This file (中文 + English)
```

---

## 🧩 Requirements

| Dependency | Requirement | Notes |
|---|---|---|
| **DSH (DeepSeek Harness)** | Installed and the `dsh` command runnable | The plugin mounts via `dsh plugin --profile web add` and relies on DSH's Cordis loader, systemPrompt injection, Agent tools, etc. |
| **Node.js** | Match the Node bundled/required by your DSH version (plugin is ESM, needs Node 16+, 18+ recommended) | Plugin loading and the 55173 editor service are Node-driven; `lib/` ships pre-compiled ESM, no build needed |
| **pnpm** | The pnpm used by the DSH profile (bundled with DSH) | Mounting goes through `dsh plugin` → pnpm link; adding in a workspace root needs the `-w` flag |
| **Python** | 3.x (callable via one of `py -3` / `python3` / `python`) | The high-fidelity offline PPTX compiler is Python-driven; the plugin auto-detects an available Python command |
| **Python deps** | `pyyaml`, `python-pptx` | Auto-installed via pip to a temp dir on first compiler run (offline / no pip: manually `pip install pyyaml python-pptx`) |
| **Browser** | Modern desktop browser with the File System Access API (Chrome / Edge recommended) | The 55173 editor uses `window.showDirectoryPicker()` for local folder read-write; browsers without it fall back to read-only upload |

> 💡 A browser is not required for "conversation + CLI export"; it's recommended only for the 55173 visual editor (drag-align, real-time render, 1-click download).

---

## 🔌 Installation

> Replace `<plugin-path>` below with your actual local plugin directory.

### Option 1: Mount via the DSH CLI (recommended)
```bash
dsh plugin --profile web add link:<plugin-path>
```
> In a pnpm workspace root you may need the `-w/--workspace-root` flag:
> `dsh plugin --profile web add -w link:<plugin-path>`

### Option 2: Manual config
Add to `~/.dsh/profiles/web/cordis.patch.yml`:
```yaml
- insert:
    - id: dsh-np-ppt
      name: 'dsh-np-ppt'
```
Then create a symlink in `~/.dsh/profiles/web/node_modules/` pointing to `<plugin-path>`
(Windows: `mklink /J`; macOS/Linux: `ln -s`).

After installing, restart the web profile (`Ctrl+C` in the `dsh web` terminal, then run `dsh web` again) to load the plugin.

---

## 🚀 Usage

Once the plugin is loaded, a custom Agent preset — **"Presentation Expert"** — is added to the DSH Web GUI. It bundles the full PPTD DSL authoring spec, 9 visual style themes, and local compiler / 55173 editor orchestration guidance, and is auto-injected into the system prompt so the AI can draft presentations out of the box; the preset files are also copied to `~/.dsh/.agent-presets/np-ppt/` for offline reuse.

### 1. Conversation-driven generation
Switch to the **Presentation Expert** preset in the DSH Web GUI and just talk to the AI:
> "Make an 8-page Microservice Refactoring proposal in Tech-Blue style."

### 2. Local visual editing & export
1. Open `http://127.0.0.1:55173/` in your browser.
2. Click "Open PPTD folder" and authorize the directory containing `deck.pptd`.
3. Edit text and layout directly on the page.
4. Click the top-right "Export" → choose PPT → "Download" to get a high-fidelity PPTX.

### 3. CLI compilation
Run the built-in compiler inside your PPTD project directory:
```bash
py -3 <plugin-path>/compiler/export_pptx.py deck/deck.pptd --output deck/deck.pptx --force
```
> On macOS/Linux use `python3`. First run auto-installs `pyyaml` / `python-pptx` via pip.
