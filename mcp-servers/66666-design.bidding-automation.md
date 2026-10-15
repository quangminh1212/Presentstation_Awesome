# bidding-automation

> 律所招投标与奖项申报材料自动化生成工作流系统

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-green.svg)](CHANGELOG.md)

自动发现律所团队的材料文件（DOCX/PPTX/PDF），识别候选案件，提取字段，生成团队简介 / 投标业绩 / 奖项申报 / 奖项汇报四类产物。提供本地 Web 网站 + CLI + MCP Server 三种入口。

## 目录

- [特性](#特性)
- [快速开始](#快速开始)
- [使用方式](#使用方式)
- [MCP 配置](#mcp-配置)
- [API 参考](#api-参考)
- [项目结构](#项目结构)
- [配置](#配置)
- [贡献](#贡献)
- [许可证](#许可证)

## 特性

- **案件材料自动发现**：扫描文件夹，SHA256 去重，规则驱动分组为候选案件
- **字段提取**：pandoc 优先文本提取，可选 LLM 字段提取（OpenAI 兼容 API）
- **审核工作流**：5 种模式（auto-approve/manual/filtered/batch/skip）
- **4 类产物生成**：
  | 产物 | 格式 | 用途 |
  |------|------|------|
  | 团队简介 | DOCX | 律所/团队介绍 |
  | 投标业绩 | DOCX | 招投标业绩清单 |
  | 奖项申报 | DOCX | 优秀案例申报材料 |
  | 奖项汇报 | PPTX | 案件汇报演示 |
- **3 种入口**：
  - 本地 Web 网站（bottle.py，127.0.0.1:8765，6 Tab 单页应用）
  - CLI（8 个子命令）
  - MCP Server（9 个工具，stdio + SSE 双模式，支持 Claude Code/Cursor/Trae）
- **可移植**：支持移动硬盘工作区，团队任何电脑插上就能用

## 快速开始

### 开发者安装

```bash
# 克隆仓库
git clone https://github.com/66666-design/bidding-automation.git
cd bidding-automation

# 创建虚拟环境（Python 3.13+）
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

# 安装依赖
pip install -e .

# 可选：安装 Web + MCP 依赖
pip install -e ".[web,mcp]"

# 初始化工作区
bidding-cli init --workspace ./my-workspace

# 端到端流程（扫描 → 识别 → 提取 → 审核 → 生成）
bidding-cli pipeline --folder ./cases --target all
```

### 启动 Web 网站

```bash
python app/app.py
# 自动打开浏览器访问 http://127.0.0.1:8765/
```

### 启动 MCP Server

```bash
# SSE 模式（任意 Agent 可连接）
python app/mcp_server_http.py --port 8766

# stdio 模式（Claude Code/Cursor 直接启动）
python app/mcp_server.py
```

## 使用方式

### CLI

```bash
# 环境自检
bidding-cli env-probe

# 扫描文件夹
bidding-cli scan --folder D:\案件材料

# 案件分组
bidding-cli detect

# 字段提取（跳过 LLM）
bidding-cli extract --skip-llm

# 查看待审核案件
bidding-cli review --list --status pending

# 自动批准所有 pending 案件
bidding-cli review --auto-approve --docs team_intro,tender,award

# 生成产物
bidding-cli assemble --target all

# 端到端
bidding-cli pipeline --folder D:\案件材料 --target all --auto-approve
```

### Web 网站

访问 `http://127.0.0.1:8765/`，6 个 Tab：
1. **状态** — 系统信息 + 案件统计
2. **材料库** — 参考材料清单
3. **案件** — 案件列表（按状态过滤）
4. **审核** — 审核 pending 案件
5. **生成** — 生成 DOCX/PPTX 产物
6. **产物** — 下载已生成的产物

### MCP Server

参见 [MCP 配置](#mcp-配置) 章节。

## MCP 配置

### Claude Desktop / Cursor（stdio 模式）

在 MCP 配置文件中添加：

```json
{
  "mcpServers": {
    "bidding": {
      "command": "python",
      "args": ["D:\\path\\to\\bidding-automation\\app\\mcp_server.py"]
    }
  }
}
```

### Trae / 任意 Agent（SSE 模式）

先启动 SSE Server：

```bash
python app/mcp_server_http.py --port 8766
```

客户端配置：

```json
{
  "mcpServers": {
    "bidding-http": {
      "url": "http://127.0.0.1:8766/sse"
    }
  }
}
```

### 9 个 MCP 工具

| 工具 | 用途 |
|------|------|
| `bidding_status` | 系统状态 + 案件统计 |
| `bidding_scan` | 扫描文件夹 |
| `bidding_detect` | 案件分组 |
| `bidding_extract` | 字段提取（可选 LLM） |
| `bidding_list_cases` | 列出案件（含标题回退） |
| `bidding_review_case` | 审核案件 |
| `bidding_build` | 生成 DOCX/PPTX 产物 |
| `bidding_pipeline` | 端到端流程（Agent 一键调用） |
| `bidding_list_outputs` | 列出已生成产物 |

## API 参考

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/status` | 系统状态 + 案件统计 |
| GET | `/api/reference` | 参考材料清单 |
| GET | `/api/output` | 已生成产物 |
| GET | `/api/download/<filename>` | 下载产物 |
| POST | `/api/scan` | 扫描文件夹 |
| POST | `/api/detect` | 案件分组 |
| POST | `/api/extract` | 字段提取 |
| GET | `/api/cases?status=pending` | 案件列表 |
| POST | `/api/cases/<id>/decision` | 更新案件决策 |
| POST | `/api/build` | 生成产物 |
| POST | `/api/pipeline` | 端到端流程 |

## 项目结构

```
bidding-automation/
├── src/bidding_automation/
│   └── case_sync/              # 案件同步核心子包
│       ├── scanner.py          # 文件扫描 + SHA256 去重
│       ├── case_detector.py    # 案件分组
│       ├── extractor.py        # 文本提取 + LLM 字段提取
│       ├── reviewer.py         # 审核工作流
│       ├── assembler.py        # 产物组装协调器
│       ├── assemblers/         # 4 个产物组装器
│       ├── config.py           # 工作区配置 + 工具查找
│       ├── db.py               # SQLite schema
│       ├── models.py           # 数据模型
│       ├── env_probe.py        # 环境自检
│       └── cli.py              # CLI 入口
├── app/                        # Web + MCP 应用
│   ├── app.py                  # bottle.py Web 入口
│   ├── bidding_client.py       # 核心封装（Web + MCP 共用）
│   ├── bidding_mcp_tools.py    # MCP 工具定义
│   ├── mcp_server.py           # stdio MCP Server
│   ├── mcp_server_http.py      # SSE MCP Server
│   └── static/                 # Web 前端
├── scripts/                    # 测试与工具脚本
├── pyproject.toml
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## 配置

### 工作区目录结构

```
my-workspace/
├── cases/          # 待处理的案件材料
├── reference/      # 参考材料（团队简介模板、投标模板等）
├── output/         # 生成的产物
├── state/          # 运行时状态（SQLite db、PID 文件）
└── config.yaml     # 可选：工具配置（LLM API Key、pandoc 路径等）
```

### config.yaml 示例

```yaml
llm:
  api_key: sk-xxx
  base_url: https://api.openai.com/v1
  model: gpt-4o-mini

tools:
  pandoc: D:\tools\pandoc\pandoc.exe
  libreoffice: C:\Program Files\LibreOffice\program\soffice.exe

ocr:
  provider: paddleocr  # 或 siliconflow
  siliconflow_api_key: sk-xxx
```

## 贡献

欢迎提交 Issue 和 Pull Request。

1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/amazing-feature`）
3. 提交变更（`git commit -m 'Add amazing feature'`）
4. 推送分支（`git push origin feature/amazing-feature`）
5. 提交 Pull Request

## 许可证

[Apache-2.0](LICENSE)
