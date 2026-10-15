
把任意文档、文章或一段文字自动转换成精美的 **PDF** 或可编辑的 **PowerPoint (.pptx)** 演示文稿。

- **输入**：本地 Markdown/txt 文件、直接粘贴的文本、或网页文章 URL
- **输出**：16:9 幻灯片 PDF、A4 文档 PDF、可在 PowerPoint / Keynote / WPS 继续编辑的 `.pptx`
- **主题**：light / dark / corporate 三套开箱即用

---

## 文件结构

```
doc-to-deck/
├── scripts/
│   ├── build.py          # 核心转换脚本（Markdown → PDF / PPTX）
│   ├── fetch.py          # 抓取网页正文并输出 Markdown
│   └── setup.py          # 环境检查与依赖安装
├── templates/
│   ├── base.css          # 排版基础样式
│   ├── doc.css           # A4 文档模式样式
│   ├── slides.css        # 16:9 幻灯片模式样式
│   ├── theme-light.css   # 亮色主题
│   ├── theme-dark.css    # 暗色主题
│   └── theme-corporate.css  # 商务主题
└── README.md
```

---

## 快速开始

### 1. 检查环境

```bash
python3 scripts/setup.py           # 检查 + 安装必需依赖（python-pptx）
python3 scripts/setup.py --full    # 同上，额外安装可选增强包
python3 scripts/setup.py --check   # 仅检查，不安装
```

**依赖说明：**

| 依赖 | 类型 | 用途 |
|------|------|------|
| `python-pptx` | 必需 | 生成可编辑 `.pptx` |
| Google Chrome / Edge | 必需（PDF） | 无头打印导出 PDF，无法 pip 安装 |
| `markdown` | 可选 | 更好的 Markdown → HTML（支持表格/脚注） |
| `readability-lxml` + `html2text` | 可选 | 更高质量的网页正文提取 |

> 可选包缺失时脚本会自动回退到内置实现，不会报错。

---

### 2. 准备内容

成品质量取决于输入结构。**推荐整理成带层级的 Markdown**：

- `#` 一级标题 → 封面标题
- `##` 二级标题 → **每个二级标题开启一页新幻灯片**
- 独立一行的 `---` → 强制分页
- 列表 / 段落 / 引用 / 代码块 → 幻灯片正文

如果是网页文章，先用 `fetch.py` 抓取：

```bash
python3 scripts/fetch.py "https://example.com/article" --out article.md
```

---

### 3. 生成成品

```bash
python3 scripts/build.py \
  --input article.md \
  --format both \        # pdf | pptx | both
  --mode slides \        # doc（A4文档）| slides（16:9幻灯片，仅影响PDF）
  --theme corporate \    # light | dark | corporate
  --title "演示标题" \
  --output-dir ./out
```

脚本执行成功后会打印 `OK` 和生成文件的完整路径。

---

## 参数说明

| 参数 | 取值 | 默认 | 说明 |
|------|------|------|------|
| `--input` | 文件路径 | — | `.md` / `.markdown` / `.txt` 源文件 |
| `--text` | 字符串 | — | 直接传入内容（与 `--input` 二选一） |
| `--format` | `pdf` / `pptx` / `both` | `pdf` | 输出格式 |
| `--mode` | `doc` / `slides` | `doc`（PDF）| 仅影响 PDF 版式 |
| `--theme` | `light` / `dark` / `corporate` | `light` | 配色主题 |
| `--title` | 字符串 | 取首个 `#` 标题 | 覆盖标题 |
| `--output-dir` | 目录 | 当前目录 | 输出目录 |

> PPTX 始终为幻灯片结构，`--mode` 对其无效。

---

## 常用示例

```bash
# 文章 → 同时生成可编辑 PPT + 幻灯片 PDF（商务主题）
python3 scripts/build.py --input a.md --format both --mode slides --theme corporate --output-dir ./out

# 长文档 → 精排 A4 PDF 报告（亮色）
python3 scripts/build.py --input report.md --format pdf --mode doc --theme light

# 只要可编辑 PPT（暗色主题）
python3 scripts/build.py --input a.md --format pptx --theme dark

# 从网页直接转换
python3 scripts/fetch.py "https://example.com/post" --out tmp.md
python3 scripts/build.py --input tmp.md --format both --mode slides --theme light
```

---

## 主题预览

| 主题 | 背景 | 强调色 | 适合场景 |
|------|------|--------|---------|
| `light` | 白色 | 蓝色 | 通用、清爽 |
| `dark` | 深蓝黑 | 青色 | 科技感、产品发布 |
| `corporate` | 白色 | 深蓝+红 | 商务汇报、提案 |

---

## 工作原理

```
输入（文件 / 文本 / URL）
   └─（URL 时）fetch.py 抓正文 → Markdown
        └─ build.py：
             ├─ PDF：Markdown → 主题化 HTML → Chrome 无头打印 → .pdf
             └─ PPTX：Markdown 按标题拆页 → python-pptx 逐页绘制 → .pptx（可编辑）
```

---

