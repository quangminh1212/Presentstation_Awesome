<div align="center">

[English](./README.en.md) | **简体中文**

</div>

<p align="center">
  <img src="assets/icon.svg" width="150" alt="deepPPT icon">
</p>

<h1 align="center">deepPPT</h1>

<p align="center">
  <b>面向科研 PowerPoint 的轻量 Agent 框架</b><br>
  <i>Durable orchestration, editable PPTX, deterministic QA, and rendered review.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.2.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/host-Codex%20%7C%20Claude_Code%20%7C%20OpenClaw-purple" alt="Host">
  <img src="https://img.shields.io/badge/output-editable_PPTX-orange" alt="Output">
</p>

## deepPPT 现在是什么

deepPPT 已从单一 Prompt/Skill 升级为宿主 Agent 原生的科研 PPT 框架。Codex、Claude Code 或 OpenClaw 负责理解材料、规划叙事和生成代码；deepPPT 负责持久化运行状态、约束页面计划、选择本地能力、保存每次 PPTX 修订、执行确定性 QA、渲染逐页预览，并阻止未经视觉复核的文件被标记为完成。

它不捆绑语言模型、本地 OCR 模型、Docker 或 WSL。默认运行仍然轻量，但工作流本身不再依赖 Agent “记得做过什么”。

## 核心能力

- `created -> inspected -> planned -> built -> checked -> rendered -> reviewed -> complete` 的持久化状态机。
- 单一规划器：宿主 Agent 只规划一次；deepPPT 不启动内层模型，也不保存
  对话副本。同一 plan 重复提交是幂等操作，不同 plan 必须显式替换。
- 每次运行保存在工作区 `.deepppt/runs/<run-id>/`，包含 `run.json`、事件日志、来源摘要、计划、每版 PPTX、QA 报告和预览。
- JSON deck-plan 中间表示，要求实质页具有主张、证据、来源引用、视觉策略和红框决策。
- QA 或视觉复核失败后进入 `needs_revision`，允许登记新计划或新 PPTX 后继续同一个 run。
- JSON CLI 提供跨平台、可脚本化的标准接口。
- ImageGen 的“可用”与用户的“要求”分开记录。只有用户明确要求、任务记录该要求、且 Codex 宿主确实提供 ImageGen 时，才可生成最多一张介绍页概念图；否则不生成。
- 百度 OCR 是可选网络 provider。每个任务默认无权上传；用户可授予、查看和撤销该任务的权限，密钥存在本身不等于授权。

## 示例

| 语言 | 高清预览 | 可编辑 PPTX |
| --- | --- | --- |
| 中文 | <a href="https://raw.githubusercontent.com/jiadizhunine/deepPPT/main/assets/previews/deepPPT_intro_zh_contact_sheet.png"><img src="./assets/previews/deepPPT_intro_zh_contact_sheet.png" width="420" alt="中文最新样例预览"></a><br>[打开完整预览](https://raw.githubusercontent.com/jiadizhunine/deepPPT/main/assets/previews/deepPPT_intro_zh_contact_sheet.png) | [直接下载最新样例](https://github.com/jiadizhunine/deepPPT/releases/download/v0.2.0/deepPPT_intro_zh.pptx) |
| English | <a href="https://raw.githubusercontent.com/jiadizhunine/deepPPT/main/assets/previews/deepPPT_intro_en_contact_sheet.png"><img src="./assets/previews/deepPPT_intro_en_contact_sheet.png" width="420" alt="English latest example preview"></a><br>[Open full preview](https://raw.githubusercontent.com/jiadizhunine/deepPPT/main/assets/previews/deepPPT_intro_en_contact_sheet.png) | [Download latest example](https://github.com/jiadizhunine/deepPPT/releases/download/v0.2.0/deepPPT_intro_en.pptx) |

## 完整安装

推荐桌面环境直接安装完整依赖。Python 3.11+、Node.js、PptxGenJS 4.0.1、PowerPoint、LibreOffice 和 Poppler 都应可用，才能发挥完整生成与渲染 QA 能力。

| 运行环境 | 生成与结构 QA | 渲染路线 | 适用结论 |
| --- | --- | --- | --- |
| macOS 原生桌面 | 完整 | PowerPoint 优先，LibreOffice 回退 | 推荐，可做最高保真终检 |
| Windows 原生桌面 | 完整 | PowerPoint COM 优先，LibreOffice 回退 | 推荐，可做最高保真终检 |
| WSL2 | 完整 | WSL 内的 Linux LibreOffice | 可生成和预检；最终应回到 Windows 原生 PowerPoint |
| Linux | 完整 | LibreOffice | 可生成和预检；不能声称完成 PowerPoint 原生保真验证 |

GitHub Actions 会在 Linux、macOS 和 Windows 上运行相同的生成、结构 QA 与示例重建测试。Office 桌面自动化不在无交互 CI 中运行；原生 PowerPoint 实测属于发布前桌面门禁。

### macOS

```bash
git clone https://github.com/jiadizhunine/deepPPT.git deep-ppt
cd deep-ppt
python3.11 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e ".[full]"
npm ci
brew install poppler
brew install --cask libreoffice
```

另行安装 Microsoft PowerPoint desktop。首次渲染可能出现 macOS 自动化权限提示，需要由当前桌面用户允许。作为 Skill 使用时，目录名保持 `deep-ppt`，放入宿主的 Skills 目录即可。

### Windows

```powershell
git clone https://github.com/jiadizhunine/deepPPT.git deep-ppt
Set-Location deep-ppt
py -3.11 -m venv .venv
.venv\Scripts\python -m pip install -U pip
.venv\Scripts\python -m pip install -e ".[full]"
npm ci
```

安装 Microsoft PowerPoint desktop、LibreOffice 和 Poppler，并将命令加入 `PATH`。PowerPoint COM 只用于已登录用户的交互式桌面会话；[Microsoft 不建议或支持无人值守的 Office 自动化](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)，因此不要把它放进 Windows 服务、服务器或 CI。Windows 原生运行即可，不要求 WSL。

如果 LibreOffice 安装在非标准目录，可将 `DEEPPPT_LIBREOFFICE` 设为 `soffice`/`soffice.exe` 的完整路径。

### WSL2

WSL2 是兼容路线，不是最高保真路线。在 WSL 内安装 Python、Node.js、LibreOffice 和 `poppler-utils`，使用 Linux 路径运行 CLI；虽然 [WSL 支持调用 Windows 可执行文件](https://learn.microsoft.com/en-us/windows/dev-environment/wsl-interop)，deepPPT 不会自动跨层调用 Windows PowerPoint。完成生成、结构 QA 和 LibreOffice 预览后，再从 Windows PowerShell 对同一 PPTX 运行原生 PowerPoint 渲染终检。

```bash
sudo apt update
sudo apt install python3 python3-venv nodejs npm libreoffice poppler-utils
python3 -m venv .venv
.venv/bin/python -m pip install -U pip
.venv/bin/python -m pip install -e ".[full]"
npm ci
```

现有 `requirements.txt` 继续保留给旧版安装流程；v0.2.0 推荐使用 `pyproject.toml` extras。

## 快速使用

先查看能力矩阵：

以下多行示例使用 Bash 续行语法。Windows PowerShell 请使用反引号续行，
或直接写成一行；入口是 `.venv\Scripts\deepppt.exe`。例如：

```powershell
.venv\Scripts\deepppt.exe --workspace C:\path\to\work capabilities --runtime codex --host-vision --host-imagegen
```

```bash
.venv/bin/deepppt --workspace /path/to/work capabilities \
  --runtime codex --host-vision --host-imagegen
```

创建并抽取来源：

```bash
.venv/bin/deepppt --workspace /path/to/work init \
  --source paper.pdf \
  --output result.pptx \
  --title "Research update" \
  --audience "Lab meeting" \
  --language Chinese \
  --slides 12 \
  --runtime codex

.venv/bin/deepppt --workspace /path/to/work inspect <RUN_ID>
```

只有用户明确要求介绍页概念图时，才在 `init` 增加
`--request-intro-image`。也可随后执行
`configure <RUN_ID> --intro-image request`；`configure <RUN_ID>` 会显示当前偏好、权限和有效路由。

Agent 根据 run 内的来源摘要生成 deck plan 和 PPTX 后，继续：

```bash
.venv/bin/deepppt --workspace /path/to/work plan <RUN_ID> --file deck-plan.json
.venv/bin/deepppt --workspace /path/to/work build <RUN_ID> --pptx generated.pptx
.venv/bin/deepppt --workspace /path/to/work check <RUN_ID>
.venv/bin/deepppt --workspace /path/to/work render <RUN_ID> --dpi 150
.venv/bin/deepppt --workspace /path/to/work review <RUN_ID> --file visual-review.json
.venv/bin/deepppt --workspace /path/to/work complete <RUN_ID>
```

普通生命周期命令仅返回紧凑交接信息，避免把完整来源和能力快照反复注入
宿主上下文。仅在确实需要完整任务元数据时使用 `status <RUN_ID>`。重复提交
同一 plan 不会重新规划；只有依据 QA 主动修订时才使用
`plan <RUN_ID> --file revised-plan.json --replace`。

`resume <RUN_ID>` 会返回当前阶段、修订号、产物和下一步动作。完整契约见 [架构文档](./docs/architecture.md)、[deck plan 示例](./examples/deck-plan.example.json) 与 [视觉复核示例](./examples/visual-review.example.json)。

## 按需百度 OCR

设置百度 OCR 的访问令牌，或 API Key 与 Secret Key：

```bash
export BAIDU_OCR_ACCESS_TOKEN="..."
# 或同时设置 BAIDU_OCR_API_KEY 与 BAIDU_OCR_SECRET_KEY

.venv/bin/deepppt configure <RUN_ID> --baidu-ocr allow
.venv/bin/deepppt ocr <RUN_ID> scanned-page.png --provider baidu
.venv/bin/deepppt configure <RUN_ID> --baidu-ocr revoke
```

PowerShell 设置方式为
`$env:BAIDU_OCR_ACCESS_TOKEN = "..."`；API Key 与 Secret Key 同理。

`run`/任务是一次 PPT 生成工作，保存在
`.deepppt/runs/<RUN_ID>/`。OCR 权限只对该任务生效，只保存布尔状态，
不保存令牌或 API Key。仅检测到配置、甚至显式执行 `ocr`，都不能绕过
未授权状态；任务完成或取消时会自动撤销网络权限。优先使用宿主已有视觉能力，只有纯图片文字确实需要结构化提取时再调用 OCR。

## 视觉规则

- 所有标准内容页复用同一条深蓝到浅色的 60 段模板横线。
- 图片直接放在白底上，不添加装饰性外框。
- 底部红色 key-finding 默认关闭，只在关键结果、综合判断、建议或最终 take-home 页按需启用。
- 每次启用都必须在 deck plan 中说明理由；总数不得超过 `max(1, floor(总页数 / 3))`，避免隔页滥用绕过连续页检查。
- 封面、目录/大纲、普通背景、方法、工作流、参考文献和致谢页不使用底部红框。
- 只有检查渲染后的每一页，才能提交通过的 visual-review。
- QA 会记录通过检查与渲染时的 PPTX 指纹；文件若随后被改写，旧报告和旧 visual-review 不能被复用。

## 项目结构

```text
src/deepppt/                    # AgentFramework、状态、路由、CLI 与可选 OCR
scripts/deepppt.py              # 从源码仓库直接运行的 CLI wrapper
schemas/                        # deck plan、visual review、run JSON 契约
examples/                       # 最小有效契约示例
SKILL.md                        # Codex / Claude Code / OpenClaw 工作流入口
style_guide.md                  # deepPPT 视觉规范
slide_patterns.md               # 页面模式与坐标
scripts/check_*.py              # 环境和 PPTX 确定性检查
scripts/qa_layout.py            # 页面规则 QA
scripts/render_preview.py       # PowerPoint/LibreOffice 渲染预览
references/example_pptx/        # 公开示例和维护用 builder
```

## 许可证

deepPPT 采用 [MIT 许可证](./LICENSE)。
