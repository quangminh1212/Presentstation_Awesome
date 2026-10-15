# bento-slides (Bento PPT Skill)

让任意 LLM 生成可交互的演示文稿。仓库包含两部分：

1. **Bento Slides MCP Server**（`mcp_server_http.py` / `mcp_server.py`）——把 `generate_bento` 工具暴露给任何 MCP 客户端（Cherry Studio、Claude Desktop、Claude Code…），任意 LLM 都能生成 `.bento.html` 幻灯片并拿到下载链接
2. **bento-slides skill**（`SKILL.md`）——按官方 [Bento](https://bento.page) 格式创作 `.bento.html` deck 的完整方法论（单文件、JSON 文档、自带运行时，完整 schema 见 [bento.page/agents.md](https://bento.page/agents.md)）

仓库里还保留了一条 **SVG 版 Bento Grid PPT 管线**（可导出可编辑 PPTX），见下方 [Legacy SVG 管线](#legacy-svg-管线)。

---

## MCP Server

### 工具

| 工具 | 说明 |
|---|---|
| `generate_bento(title, slides, theme?, output_dir?)` | 生成 `.bento.html`，返回纯 ASCII 短链下载地址 |
| `list_themes()` | 列出可用主题 |

### 服务端兜底（LLM 怎么写都能出正确结果）

- **字段规范化**：`content→html`、`width→w`、`height→h`、`"bold"→700`，自动补齐 `id / rotation / opacity / align / valign / lineHeight` 等必需字段
- **JSON 注入安全**：`<` 转义防 `</script>` 截断，替换时不破坏转义序列
- **防篡改短链**：下载链接为 `/files/dl/deck-<token>.bento.html` 纯 ASCII 路径（中文 URL 会被下游 LLM 逐字改写导致 404，实测教训）

### 快速开始

```bash
pip3 install -r requirements-mcp.txt   # mcp>=2.0, uvicorn
```

**stdio 模式**（Claude Desktop / Claude Code 本地接入）：

```json
{
  "mcpServers": {
    "bento-slides": {
      "command": "python3",
      "args": ["/绝对路径/mcp_server.py"]
    }
  }
}
```

**SSE 模式**（Cherry Studio 等远程接入，推荐）：

```bash
python3 mcp_server_http.py --sse --host 0.0.0.0 --port 8100
```

Cherry Studio 配置：类型 **SSE**，URL `http://<主机>:8100/sse`。

也支持 Streamable HTTP：去掉 `--sse`，URL 为 `http://<主机>:8100/mcp`。

### 部署到服务器

参考 [deploy/bento-slides-mcp.service.example](deploy/bento-slides-mcp.service.example)（systemd，开机自启 + 自动重启）。关键环境变量：

| 变量 | 说明 |
|---|---|
| `BENTO_PUBLIC_BASE_URL` | 客户端可访问的公网基址，下载链接用它拼接（必填） |
| `PPT_DECKS_DIR` | deck 输出目录，默认 `~/ppt-decks` |

### 测试

```bash
# 对一个运行中的 SSE 服务跑端到端 / 规范化兜底测试
BENTO_MCP_URL=http://<主机>:8100/sse python3 tests/test_e2e.py
BENTO_MCP_URL=http://<主机>:8100/sse python3 tests/test_normalize.py
```

---

## bento-slides Skill（Claude Code）

`SKILL.md` 是可直接安装的 Claude Code skill：用户说"做 PPT"时自动触发，从 bento.page 下载最新 Bento 应用，按官方 schema 写入文档 JSON，产出单文件 `.bento.html`（自带运行时，浏览器直接打开即放映/编辑）。

```bash
# 安装到 Claude Code
cp -r . ~/.claude/skills/bento-slides
```

核心原则（详见 SKILL.md）：只用 morph / chart / ken-burns 等原生特性而不是静态文字页；元素字段必须完整（`html` 不是 `content`，`w/h` 不是 `width/height`）。

---

## Legacy SVG 管线

> 以下是仓库早期的 SVG 版 Bento Grid PPT 方案（`scripts/` + `themes/`），
> 产出 SVG/HTML 预览 + 可编辑 PPTX。灵感来自 sandun
> [《应该是目前最强的 PPT Agent，附上完整思路分享》](https://linux.do/t/topic/1782304)。

![cover](examples/dify-intro/shots/01-cover.png)
![data page](examples/dify-intro/shots/05-pre-launch.png)
![mixed grid](examples/dify-intro/shots/07-week-one.png)

## Features

- **7 阶段流水线**：needs（反问） → research → outline（金字塔原理） → planning → fetch → design → review → export
- **6 种 Bento 布局** + **9 种卡片组件**：single-focus / two-col-symmetric / two-col-asymmetric / three-col / major-minor / hero-top / mixed-grid 任选；卡内可放 card-hero / card-stat / **card-stack**（多数据叠加）/ card-list（highlight 焦点项）/ card-quote / card-text / card-image / **card-compare**（多列对比表）/ chart-bar
- **跨组件装饰元素**：胶囊 badges / 三栏 metadata / 半透明装饰大字 / **ghost_text 背景装饰字** / 网格背景纹理
- **双主题**：`bento-tech`（深色科技风）/ `bento-light`（浅色商务风），主题继承机制让新主题只需一个 manifest.json
- **底层 SVG**（viewBox `0 0 1280 720`），双 PPTX 导出路径：
  - **Native**（默认）：`scripts/native_render.py` 用 python-pptx 直接画原生 shape，**100% 可编辑**（单击文字直接改、无需"转换为形状"）。视觉商务平面（无渐变 / 光斑）
  - **SVG**（备选 `--format pptx-svg`）：通过 `asvg:svgBlip` OOXML 注入到 pptx，PowerPoint 2019+/Office 365 显示完美矢量但默认是 picture 对象
- **HTML 翻页预览**：左右键 / 缩略图栏 / 全屏，在浏览器里直接放映
- **图片 provider 协议**：可插拔的 `url_download` / `nanobanana` / `unsplash`，AI 自己决定用搜还是生
- **中文版式 lint**：默认拦截英文标点（公众号/严苛场景可开"中英不空格"）

## Install

```bash
git clone https://github.com/lysong9907/bento-ppt-skill.git ~/.claude/skills/ppt-agent
pip3 install jinja2 python-pptx lxml
```

可选（看你机器上有没有）：

```bash
# 截图依赖：自动探测 Chrome / Chromium / Edge / Brave，找不到再装
# 不依赖 playwright
```

## Use

**新开** Claude Code 窗口（让 description 自动加载），直接说自然语言：

```
帮我做一份 6-8 页的 X 主题 PPT
```

```
把 ./report.md 转成发布会 deck
```

Claude 会自动加载 ppt-agent skill，反问受众/调性/页数，然后跑完 7 阶段流程。产物在 `~/ppt-decks/<date>-<slug>/`：

- `slides/*.svg` — 每页 SVG 矢量
- `deck.html` — 浏览器翻页预览
- `deck.pptx` — PowerPoint 可编辑
- （可选）`deck.pdf`

## Manual CLI

```bash
SKILL=~/.claude/skills/ppt-agent

python3 $SKILL/scripts/ppt.py new "<topic>"
python3 $SKILL/scripts/ppt.py fetch <ws>      # 可选，下载/生成 card-image
python3 $SKILL/scripts/ppt.py scaffold <ws>    # SVG 渲染
python3 $SKILL/scripts/ppt.py shoot <ws>       # 截图 + deck.html
python3 $SKILL/scripts/ppt.py export <ws> --format pptx
```

## Sample

`examples/dify-intro/` 是端到端样本：

- 8 页 deck，覆盖全部 6 种 Bento 布局
- 含 layout.json（输入）、slides/SVG（产物）、shots/PNG（截图）、deck.pptx
- 直接 `open examples/dify-intro/deck.html` 看翻页效果

## 延展开发（Layout / Component / Theme）

完整的接力开发规范见 **[reference/extension-guide.md](reference/extension-guide.md)**，涵盖：

- 新增 Layout：只改 manifest.json，零代码
- 新增 Component：写 1 个 SVG 模板 + 1 个 native 方法
- 新增 Theme：只需 manifest.json，模板自动继承

## 添加新风格

```bash
# 只需创建 manifest.json，模板自动从 bento-tech 继承
mkdir themes/<your-style>
# 复制 bento-tech 或 bento-light 的 manifest.json，修改颜色 / 字号
```

详见 [reference/extension-guide.md](reference/extension-guide.md)。

## 添加新图片 provider

```bash
# 在 scripts/providers/ 下新建一个 .py 文件
# 实现 ImageProvider 接口 + 末尾 register(YourProvider())
# 自动被 fetch 阶段发现
```

详见 [scripts/providers/README.md](scripts/providers/README.md)。

## Architecture

```
bento-slides/
├── SKILL.md                       # bento-slides skill 入口（官方 bento 格式）
├── mcp_server_http.py             # MCP 服务器（SSE / Streamable HTTP，含字段规范化 + 短链下载）
├── mcp_server.py                  # MCP 服务器（stdio 版）
├── requirements-mcp.txt           # MCP 依赖
├── deploy/                        # systemd 部署示例
├── tests/                         # e2e / 规范化兜底测试
├── reference/                     # 渐进披露文档（需要时再读）
│   ├── extension-guide.md         # Layout / Component / Theme 延展规范（接力开发必读）
│   ├── bento-layouts-guide.md     # 6 种布局 + component data schema
│   ├── pyramid-outline-prompt.md  # sandun 开源的金字塔原理 prompt
│   ├── image-providers.md         # AI 怎么写 src / source
│   ├── pptx-rendering.md          # 双 Renderer 路线（native vs svgBlip）
│   └── theme-authoring.md         # 加新主题（简版）
├── scripts/
│   ├── ppt.py                     # 主 CLI
│   ├── render.py                  # SVG 装配 (jinja2 + 主题继承)
│   ├── native_render.py           # Native PPTX 渲染（python-pptx，100% 可编辑）
│   ├── shoot.py                   # Chrome headless 截图 + deck.html
│   ├── export.py                  # SVG → PPTX (svgBlip 备选路线)
│   ├── fetch.py                   # 图片 provider 调度
│   ├── lint_cn.py                 # 中文版式硬约束
│   └── providers/                 # 可插拔图片 provider
│       ├── url_download.py        # 内置（无 API key）
│       ├── nanobanana.py          # Gemini Image (stub)
│       └── unsplash.py            # Unsplash (stub)
├── themes/
│   ├── bento-tech/                # 深色科技风（默认）：渐变光斑 + 玻璃拟态卡片
│   │   ├── manifest.json          # 设计 token + layout 槽位元数据
│   │   ├── slide-base.svg.j2      # 1280×720 容器（背景 / defs / ghost_text / 页脚）
│   │   ├── layouts/_base.svg.j2   # 数据驱动通用 layout
│   │   └── components/            # 9 种 component 模板
│   └── bento-light/               # 浅色商务风：只有 manifest.json，模板继承 bento-tech
└── examples/
    └── dify-intro/                # 端到端跑通样本（8 页，覆盖全部布局）
```

## Credit

- 方法论：[sandun @ linux.do](https://linux.do/t/topic/1782304) — 四步流水线 + Bento Grid + 整页 SVG
- skill 框架：[Anthropic Claude Code](https://code.claude.com/docs/en/skills.md)
- 实现：Claude (Opus 4.7) + 我

## License

MIT
