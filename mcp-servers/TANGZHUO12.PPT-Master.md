# DSH Plugin · PPT Expert

> 给 [DeepSeek Harness (dsh)](https://www.npmjs.com/package/@deepseek-ai/dsh) 装上"只会做 PPT、但做到专家水准"的能力包：247 行幻灯片专家人格 + LibreOffice Impress MCP 服务器（9 个工具）+ matplotlib 图表内核 + **浏览器实时预览页**。一句话需求 → 带动画、带商务图表的成品演示文稿，边做边看。

A standard DSH extension bundle: a presentation-deck expert persona, a LibreOffice Impress MCP server (9 tools), a matplotlib chart kernel, and a live browser preview that follows the agent page by page. Zero npm dependencies.

## 安装（两种用法，都跑一次 setup.sh）

**用法 A · 作为扩展包加进你已有的 profile**（能力包模式，推荐）：

```bash
cd ~/.dsh/profiles/<你的profile>
dsh plugin --profile <你的profile> add https://github.com/TANGZHUO12/ppt-expert.git
# 然后在该 profile 的 package.json 里，把 "dsh-ppt-expert" 加进 dsh.profile.bundles 数组
dsh --profile <你的profile> "做一份 5 页的《XX介绍》PPT"
```

**用法 B · 整仓库直接当一个 profile**（最简单）：

```bash
git clone https://github.com/TANGZHUO12/ppt-expert.git ~/.dsh/profiles/ppt-expert
cd ~/.dsh/profiles/ppt-expert && ./setup.sh
dsh --profile ppt-expert "做一份 5 页的《XX介绍》PPT"
```

`setup.sh` 把 MCP 服务器装配到 `~/.dsh/ppt-expert/` 固定位置（python venv + 依赖）；
patch 里的 MCP command 用 HOME 拼接，全机器可移植。

**前置要求**：macOS / Linux · python3 ≥3.10 · [LibreOffice](https://www.libreoffice.org/download/download/)（MPL-2.0）· 一个大模型 API Key（走 dsh 自身模型配置）。

## 实时预览

模型第一次保存文档时，浏览器自动弹出预览页（`127.0.0.1:18465`）——之后每完成一页自动刷新，它操作哪页预览就翻到哪页（人格的"持续保存纪律"驱动）。不想弹浏览器：环境变量 `PPT_PREVIEW=0`。预览服务空闲 15 分钟自动退出。

## 智能体能力

- **人格**：版式配方（25.4×14.29cm 版面校准坐标库）、11 条红线（含 audit 机器审计对比度检查）、图表数据形状契约、修改轮纪律。改人格：编辑 `prompts/slides-expert-persona.md` 后跑 `python3 scripts/sync-persona.py`
- **工具**（`mcp/mcp_server.py`）：`impress_document/slide/shape/text/animation/transition/export` ×7 + `table_read`（xlsx/xls/ods/csv 智能读表）+ `chart_make`（18 种商务图表 matplotlib 直出，40-120ms/张，中文原生）

## 架构

```
dsh --profile <name>
 ├─ dsh-base + dsh-headless（官方层）
 └─ dsh-ppt-expert（本包，package.json: dsh.bundle.patch → cordis.patch.yml）
     ├─ system-prompt：幻灯片专家人格（内联）
     ├─ mcp-libreoffice 桥 → ~/.dsh/ppt-expert/mcp/mcp-launch → venv python
     │    └─ mcp_server.py（9 工具）→ 无头 LibreOffice / matplotlib
     └─ 权限：danger-full-access + 免审批
         实时预览：文档落盘 → preview_server（soffice→PDF→HTTP）→ 浏览器跟随
```

零 npm 依赖：patch 条目引用的 `@deepseek-ai/dsh-mcp-client` 由 dsh 安装内解析（healProfilesModuleFallback）——**不要**给本包声明 npm 依赖，平铺安装会造成 dsh 内部模块版本遮蔽（API 断裂，实测踩坑）。

## 目录结构

```
├── cordis.patch.yml      # 插件层：MCP 桥 + 人格 + 权限（HOME 可移植）
├── package.json          # dsh.bundle.patch（扩展包）+ dsh.profile.bundles（整仓 profile）双声明
├── setup.sh              # 一键装配（MCP → ~/.dsh/ppt-expert/ + venv + 自检）
├── mcp/                  # MCP 服务器（Python 七件 + preview_server 实时预览 + 启动器）
├── prompts/              # 人格源文件
└── scripts/              # sync-persona.py（人格重内联）· dev-sync.sh（开发同步）
```

## 已知限制

- 需要 LibreOffice 与 python ≥3.10（setup.sh 自动装配/检测）
- 默认权限 `danger-full-access`（智能体需读写文档与工作目录），自行斟酌
- macOS 完整 App 形态（原生壳/实时预览栏/图表库 UI）见同仓库 main 分支

## License

MIT
