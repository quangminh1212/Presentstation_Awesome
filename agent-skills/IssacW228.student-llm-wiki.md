<div align="center">

# 📚 Student LLM Wiki

**用 AI 把课件变成你自己的知识库**
**Turn your course slides into a personal wiki with AI**

[中文](#中文) · [English](#english)

</div>

---

## 中文

### 这是什么？

你把课件 PDF 丢进 `raw/` 文件夹，AI 自动帮你整理成结构化的 wiki 笔记，存在 `wiki/` 里。你用 [Obsidian](https://obsidian.md) 浏览这些笔记，用 AI 工具来复习、出题、检查薄弱环节。**你不需要手写任何笔记。**

基于 [Andrej Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

---

### 你需要准备的东西

**1. Obsidian（用来浏览笔记）**
- 下载地址：[https://obsidian.md/download](https://obsidian.md/download)
- 免费，支持 Windows / macOS / Linux / iOS / Android
- 安装后还需要在社区插件里安装 **Dataview**（用于首页动态面板）

**2. 选一个 AI 工具（任选其一即可）**

| 工具 | 适合人群 | 获取方式 |
|---|---|---|
| Claude Code CLI | 熟悉命令行 | [安装说明](https://docs.anthropic.com/claude-code) |
| Claude Code Web | 不想装任何东西 | [claude.ai/code](https://claude.ai/code) |
| Cursor | 喜欢 IDE 界面 | [cursor.com](https://www.cursor.com) |
| Trae | 国内用户 | [trae.ai](https://www.trae.ai) |
| Cowork | 团队协作 | 参考 Cowork 文档 |
| GitHub Copilot | 已有订阅 | VS Code 插件市场 |

**3. 你的课件**（PDF 或其他文本格式）

---

### 第一步：下载项目，用 Obsidian 打开

```bash
git clone https://github.com/IssacW228/student-llm-wiki.git
cd student-llm-wiki
```

然后打开 Obsidian → 「打开本地仓库」→ 选择 `student-llm-wiki` 文件夹。

> **必须安装 Dataview 插件**：Obsidian 设置 → 社区插件 → 浏览 → 搜索 `Dataview` → 安装并启用。

---

### 第二步：选择你的 AI 工具并打开项目

<details>
<summary><strong>Claude Code CLI（命令行）</strong></summary>

1. 确保已安装 Claude Code CLI 并登录
2. 在项目目录运行：
   ```bash
   claude
   ```
3. 配置文件（`.claude/`）会自动加载，无需额外设置
4. 直接输入命令或自然语言即可开始

</details>

<details>
<summary><strong>Claude Code Web（网页版，无需安装）</strong></summary>

1. 打开 [claude.ai/code](https://claude.ai/code)
2. 将此仓库连接到 Claude Code
3. 配置文件（`.claude/`）自动识别，直接使用

</details>

<details>
<summary><strong>Cursor</strong></summary>

1. 用 Cursor 打开 `student-llm-wiki` 文件夹
2. 规则文件已在 `.cursor/rules/wiki.mdc`，自动生效
3. 在 Cursor 聊天框直接输入命令，无需额外配置

</details>

<details>
<summary><strong>Trae</strong></summary>

1. 用 Trae 打开 `student-llm-wiki` 文件夹
2. Skills 已在 `.trae/skills/`，自动识别
3. 在对话框直接输入命令

</details>

<details>
<summary><strong>Cowork</strong></summary>

1. 将 Cowork 项目指向 `student-llm-wiki` 文件夹
2. `COWORK-INSTRUCTIONS.md` 会自动加载
3. 直接开始对话

</details>

<details>
<summary><strong>GitHub Copilot / OpenAI Codex</strong></summary>

1. 用支持 Copilot 的编辑器打开项目文件夹
2. `AGENTS.md` 会被自动读取
3. 直接在对话框输入命令

</details>

---

### 第三步：导入你的第一份课件

1. 在 `raw/` 下新建文件夹，用你的课程代号命名（如 `raw/MATH1001/`）
2. 把课件 PDF 复制进去
3. 在 AI 工具里输入：
   ```
   ingest raw/MATH1001/L1.pdf
   ```
4. AI 会自动生成概念页、课程总览、来源摘要
5. 回到 Obsidian，打开 `Home.md` 查看结果

> 同一份文件不会被重复导入（通过文件 hash 去重）。

---

### 命令速查

| 命令 | 作用 |
|---|---|
| `ingest raw/XXXX/L1.pdf` | 导入课件，自动生成笔记、课程总览、跨课连接记录 |
| `lint` | 检查笔记健康度：断链、孤立页、过期概念、缺失总览、术语表补全 |
| `review XXXX` | 费曼复习模式：AI 提问，你来回答 |
| `exam-prep XXXX` | 根据薄弱概念自动出练习题 |
| `diagram ConceptName` | 为某个概念页添加 Mermaid 图解（流程图/架构图/时序图等） |

也可以用自然语言，比如「帮我复习这门课」或「把这个文件导入知识库」。

---

### 添加新课程

1. 在 `raw/` 下创建对应课程文件夹（如 `raw/PHYS1001/`）
2. 把课件放进去
3. 运行 `ingest`，课程总览页会自动创建
4. `Home.md` 首页会动态显示新课程，无需手动修改

---

### 项目结构

```
student-llm-wiki/
├── raw/              ← 放课件（只读，AI 不会修改这里）
│   └── XXXX/         ← 按课程分文件夹
├── wiki/             ← AI 生成的笔记（自动维护）
│   ├── concepts/         ← 概念页（每概念一页，含图解）
│   ├── courses/          ← 课程总览（ingest 时自动创建）
│   ├── sources/          ← 课件摘要
│   ├── exam-prep/        ← 练习题
│   ├── connections-log.md  ← 跨课程连接发现记录
│   ├── contradictions.md   ← 矛盾与张力追踪
│   ├── glossary.md         ← 中英术语表（自动填充）
│   ├── overview.md         ← 跨课程综述（自动更新）
│   ├── index.md            ← 总目录
│   └── hot.md              ← AI 上下文缓存（每次 session 首读）
├── Home.md           ← Obsidian 首页仪表盘
│
│   以下为 AI 工具配置文件，无需修改：
├── .claude/          ← Claude Code 配置
├── .cursor/          ← Cursor 配置
├── .trae/            ← Trae 配置
├── AGENTS.md         ← Copilot/Codex 配置
└── COWORK-INSTRUCTIONS.md  ← Cowork 配置
```

---

### 致谢

- [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — 原始模式
- [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — hot cache、manifest 去重、skill 拆分
- [Obsidian](https://obsidian.md) — 知识平台

### 许可证

MIT

---

## English

### What is this?

You drop course PDF slides into the `raw/` folder. The AI automatically organizes them into structured wiki notes in `wiki/`. You browse the notes with [Obsidian](https://obsidian.md), and use AI tools to review, generate practice questions, and surface weak spots. **You never write notes yourself.**

Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

### Prerequisites

**1. Obsidian (for browsing your notes)**
- Download: [https://obsidian.md/download](https://obsidian.md/download)
- Free. Available on Windows / macOS / Linux / iOS / Android
- After installing, also install the **Dataview** community plugin (required for the Home dashboard)

**2. An AI tool (pick just one)**

| Tool | Best for | Get it |
|---|---|---|
| Claude Code CLI | Terminal users | [Install guide](https://docs.anthropic.com/claude-code) |
| Claude Code Web | No install needed | [claude.ai/code](https://claude.ai/code) |
| Cursor | IDE-style interface | [cursor.com](https://www.cursor.com) |
| Trae | — | [trae.ai](https://www.trae.ai) |
| Cowork | Team use | See Cowork docs |
| GitHub Copilot | Existing subscribers | VS Code marketplace |

**3. Your course slides** (PDF or other text formats)

---

### Step 1: Clone the repo and open in Obsidian

```bash
git clone https://github.com/IssacW228/student-llm-wiki.git
cd student-llm-wiki
```

Open Obsidian → "Open folder as vault" → select the `student-llm-wiki` folder.

> **Install the Dataview plugin**: Obsidian Settings → Community plugins → Browse → search `Dataview` → Install and enable.

---

### Step 2: Open the project with your AI tool

<details>
<summary><strong>Claude Code CLI</strong></summary>

1. Make sure Claude Code CLI is installed and you're logged in
2. Run in the project folder:
   ```bash
   claude
   ```
3. The config folder (`.claude/`) is auto-detected — no extra setup needed
4. Type commands or plain English to get started

</details>

<details>
<summary><strong>Claude Code Web (no install needed)</strong></summary>

1. Go to [claude.ai/code](https://claude.ai/code)
2. Connect this repository to Claude Code
3. The `.claude/` config is auto-detected — start typing commands directly

</details>

<details>
<summary><strong>Cursor</strong></summary>

1. Open the `student-llm-wiki` folder in Cursor
2. Rules are pre-configured in `.cursor/rules/wiki.mdc` — auto-applied
3. Type commands in the Cursor chat panel

</details>

<details>
<summary><strong>Trae</strong></summary>

1. Open the `student-llm-wiki` folder in Trae
2. Skills are pre-configured in `.trae/skills/` — auto-detected
3. Type commands in the chat panel

</details>

<details>
<summary><strong>Cowork</strong></summary>

1. Point your Cowork project at the `student-llm-wiki` folder
2. `COWORK-INSTRUCTIONS.md` loads automatically
3. Start chatting

</details>

<details>
<summary><strong>GitHub Copilot / OpenAI Codex</strong></summary>

1. Open the project in an editor with Copilot support
2. `AGENTS.md` is read automatically
3. Type commands in the chat panel

</details>

---

### Step 3: Ingest your first slide deck

1. Create a folder under `raw/` named after your course (e.g. `raw/MATH1001/`)
2. Copy your PDF into that folder
3. In your AI tool, type:
   ```
   ingest raw/MATH1001/L1.pdf
   ```
4. The AI generates concept pages, a course overview, and a source summary
5. Switch to Obsidian and open `Home.md` to see your new notes

> The same file won't be ingested twice — files are tracked by hash.

---

### Commands

| Command | What it does |
|---|---|
| `ingest raw/XXXX/L1.pdf` | Import a slide deck — generates notes, course overview, and cross-course link records |
| `lint` | Check wiki health: broken links, orphan pages, stale concepts, missing overviews, glossary gaps |
| `review XXXX` | Feynman review mode: AI quizzes you |
| `exam-prep XXXX` | Auto-generate practice questions from weak concepts |
| `diagram ConceptName` | Add a Mermaid diagram to a concept page (flowchart / architecture / sequence / etc.) |

You can also use plain English: "quiz me on this course" or "import this file into the wiki".

---

### Adding a new course

1. Create a folder under `raw/` for the course (e.g. `raw/PHYS1001/`)
2. Put your slides in it
3. Run `ingest` — a course overview page is created automatically
4. The `Home.md` dashboard updates dynamically — no manual edits needed

---

### Project structure

```
student-llm-wiki/
├── raw/              ← Your slides (read-only — AI never modifies this)
│   └── XXXX/         ← One folder per course
├── wiki/             ← AI-generated notes (auto-maintained)
│   ├── concepts/         ← Concept pages (one per concept, with diagrams)
│   ├── courses/          ← Course overviews (auto-created on ingest)
│   ├── sources/          ← Slide summaries
│   ├── exam-prep/        ← Practice questions
│   ├── connections-log.md  ← Cross-course link discovery log
│   ├── contradictions.md   ← Contradiction & tension tracker
│   ├── glossary.md         ← Bilingual term index (auto-populated)
│   ├── overview.md         ← Cross-course synthesis (auto-updated)
│   ├── index.md            ← Master catalog
│   └── hot.md              ← AI context cache (read first each session)
├── Home.md           ← Obsidian dashboard
│
│   AI tool config — no need to touch these:
├── .claude/          ← Claude Code config
├── .cursor/          ← Cursor config
├── .trae/            ← Trae config
├── AGENTS.md         ← Copilot/Codex config
└── COWORK-INSTRUCTIONS.md  ← Cowork config
```

---

### Credits

- [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — the original pattern
- [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) — hot cache, manifest dedup, skill decomposition
- [Obsidian](https://obsidian.md) — the knowledge platform

### License

MIT
