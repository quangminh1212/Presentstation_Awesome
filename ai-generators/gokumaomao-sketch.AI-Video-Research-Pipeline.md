# AI Video Research Pipeline

## AI 多模态知识萃取平台

一个本地优先的 AI 多模态知识生产工作流，将公开视频、公开免登录的微信公众号文章、本地视频、音频、PowerPoint 和 Word 转换为可追溯、可继续使用的 Markdown 知识资产。

项目面向研究、学习和知识管理场景。它负责内容解析、证据提取、AI 分析、知识精炼和本地归档；不提供自动投资建议，不宣称自主 Agent 决策能力，也不绕过登录、付费、DRM 或私有内容访问控制。

> **English Summary**
> AI Video Research Pipeline is a local-first multimodal workflow for turning authorized public videos, public no-login WeChat articles, local media, PowerPoint, and Word documents into traceable Markdown knowledge assets with ASR, Vision, LLM analysis, and Knowledge Refinement.

![AI 多模态知识萃取平台工作台](docs/screenshots/01-content-center.png)

## 为什么做这个项目

传统内容整理需要反复播放、手工摘录、复制图表，再把零散笔记重新组织。V2.2 把过程拆成可观察、可复用的流水线：

~~~text
公开视频 / 微信公众号公开文章 / 本地视频 / 音频 / PPTX / DOCX
                    ↓
              统一输入预检
                    ↓
           ASR / Vision / 文档解析
                    ↓
                AI Analysis
                    ↓
           Knowledge Refinement
                    ↓
         01 / 02 / 03 三层知识资产
                    ↓
       可选 Word / PowerPoint 派生导出
~~~

运行资料与最终知识资产严格分离：媒体、帧、JSON、数据库和日志留在本地 runtime；知识库只接收最终 Markdown。

## 核心能力

| 模块 | V2.2 能力 |
| --- | --- |
| 统一多输入 | 多个公开 URL 与多个本地文件可一次预检，支持混合输入、重复检查、50 项上限和队列容量检查。 |
| 公共视频 URL | 支持 Bilibili、抖音、YouTube、Vimeo 以及其他 yt-dlp 可解析且公开可访问的单视频页面；抖音可直接粘贴分享文案或短链。 |
| 微信公众号公开文章 | 支持公开、免登录的 `mp.weixin.qq.com/s/...` 文章：安全获取、正文解析、正文图片、Vision、AI 分析、知识精炼和三层知识资产。 |
| 本地媒体 | 支持常见本地视频和音频；通过 ffprobe 验证，安全导入隔离工作区。 |
| PowerPoint | 支持 .pptx 的文字、表格、图片、Chart、Notes、隐藏页、页面渲染和可选 Vision。 |
| Word | 支持 .docx 的 Heading、Paragraph、List、Table、Image、Caption、Hyperlink、Header/Footer。 |
| Whisper ASR | 使用本地 faster-whisper，支持模型目录、运行时诊断和进度记录。 |
| Vision | 对视频帧或文档视觉项进行筛选、压缩和分批理解。 |
| AI Analysis | 基于可用文本与视觉证据生成完整分析稿，不把来源主张自动视为事实。 |
| Knowledge Refinement | 删除寒暄、宣传、重复和 AI 套话，保留数字、条件、风险、不确定表达与来源。 |
| 三层知识资产 | 01 原始追溯层、02 完整 AI 分析层、03 正式知识资产层。 |
| Word 知识报告 | 从 03 最终知识稿确定性生成可编辑 DOCX，不额外调用 AI。 |
| PowerPoint 导出 | 本地确定性学术汇报导出；页数由知识结构与可读性自适应决定，支持可追溯的图表、流程、框架、层级、关系和矩阵表达。 |
| 桌面客户端 | 可选 Tauri 2 macOS 客户端，负责本机服务健康检查、受控启动与原生 WebView 承载，不打包模型、数据库或密钥。 |
| FIFO Worker | Unified Batch 提交后拆分为普通 Task，由单 Worker 按 FIFO 顺序处理。 |
| 产品工作台 | 内容萃取中心、任务中心、知识资产库、成本中心和设置。 |
| 成本中心 | 将请求用量、理论成本与 Provider 实际账单分开记录；当前汇总只统计成本核算起点之后的请求。 |

## 适合谁使用

- 需要把公开视频、课程和访谈整理为可追溯笔记的研究人员。
- 需要从本地音视频、PPTX 或 DOCX 中提取结构化知识的学习者与知识管理用户。
- 希望将 Markdown 结果继续导入 Obsidian、飞书或其他知识库的本地优先用户。

本项目是内容处理与知识生产工具，不生成自动投资建议，也不替代事实核验和专业判断。

## 系统架构

![AI 多模态知识萃取平台 V2.1 系统架构图](docs/architecture.png)

V2.2 采用统一输入适配、多模态处理、三层知识资产与可选导出层架构：

1. 内容输入层接收公共视频 URL、微信公众号公开文章 URL、本地视频、音频、PPTX 和 DOCX。
2. 输入适配层通过 InputAdapterRegistry、PublicVideoAdapter、WebArticleAdapter、Local Media Adapter 和 Document Adapter 生成统一内容契约。
3. 微信公众号文章依次经过 ArticleFetcher、WeChatArticleExtractor 和 ArticleImageFetcher；随后复用现有 Document Pipeline、Vision、AI Analysis 与 Knowledge Refinement，不使用独立的微信 Worker 或 AI 服务。
4. 普通 Task 经 Unified Preflight 后由单一 FIFO Worker 调度；媒体任务可使用 ASR 与 Vision，图文文章按可用正文和图片进入后续处理。
5. 知识生产层发布 01 原始内容、02 AI 分析、03 最终知识稿 Markdown；内容萃取中心、任务中心、知识资产库、成本中心和设置提供统一入口。
6. 导出层只读取既有 03 最终知识稿和已保存视觉资产，生成可编辑 DOCX 或 PPTX，不改变 01/02/03 Markdown 结构，也不重跑上游任务。

详细说明见 [V2.1 架构文档](docs/architecture-v2.1.md) 与 [V2.2 导出架构文档](docs/architecture-v2.2.md)。

## Demo

以下页面全部使用合成数据，不含真实 URL、BV 号、作者、任务、成本、用户名、路径或 API Key。

| 内容萃取中心 | 统一预检 |
| --- | --- |
| ![内容萃取中心](docs/screenshots/01-content-center.png) | ![统一预检](docs/screenshots/02-unified-preflight.png) |

| 任务中心 | 知识资产库 |
| --- | --- |
| ![任务中心](docs/screenshots/03-task-center.png) | ![知识资产库](docs/screenshots/04-knowledge-assets.png) |

| 最终知识稿 | AI 成本中心 |
| --- | --- |
| ![最终知识稿](docs/screenshots/05-final-knowledge.png) | ![AI 成本中心](docs/screenshots/06-cost-center.png) |

![设置](docs/screenshots/07-settings.png)

### 微信公众号文章（合成演示）

| 文章预检 | 文章任务与资产 |
| --- | --- |
| ![微信公众号文章预检](docs/screenshots/v2.1/01-wechat-preflight.png) | ![微信公众号文章任务](docs/screenshots/v2.1/02-wechat-task.png) |

![微信公众号文章最终知识稿](docs/screenshots/v2.1/03-wechat-final-knowledge.png)

## 快速开始

### 环境要求

- Python 3.11+
- ffmpeg 与 ffprobe：媒体处理必需，Web 本身可在缺失时启动
- yt-dlp：公开单视频页面解析所需
- LibreOffice：PPTX/DOCX 页面渲染的增强型可选依赖；缺失时结构解析仍可运行

macOS 示例：

~~~bash
brew install ffmpeg yt-dlp
~~~

Linux 和 Windows 请使用系统包管理器安装 ffmpeg，并确保 ffmpeg、ffprobe 和 yt-dlp 可由 PATH 解析。

### 安装

~~~bash
git clone https://github.com/gokumaomao-sketch/AI-Video-Research-Pipeline.git
cd AI-Video-Research-Pipeline
python3.11 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
~~~

### 启动

~~~bash
./start.sh
~~~

默认访问 [http://127.0.0.1:8502](http://127.0.0.1:8502)。无 API Key 时 Web 仍能启动，设置页会显示“未配置”。

### 🔑 配置 AI API

项目无需 API Key 即可启动。若需要使用 AI 总结、知识精炼或视觉理解，请在“设置 → API配置”中配置对应 Provider；本地 faster-whisper 语音识别不需要 Whisper API Key。

👉 [面向中文用户的 API Key 配置教程](docs/API-Key配置教程.md)

👉 [微信公众号文章使用教程](docs/微信公众号文章使用教程.md)

### 首次使用

1. 打开“设置”，确认 ffmpeg、ffprobe、yt-dlp 和 Python 环境状态。
2. 如需云端 Vision 或 LLM，在“设置 → API 配置”中配置 DeepSeek 或 DashScope / Qwen；只使用本地解析时可以暂不配置。
3. 回到“内容萃取中心”，粘贴公开单视频 URL、公开免登录的微信公众号文章 URL，或选择本地视频、音频、PPTX、DOCX。
4. 先执行统一预检，确认输入、依赖与任务数量，再提交到 FIFO 队列。
5. 在“任务中心”查看阶段、进度和错误；完成后在“知识资产库”打开 01/02/03 三层 Markdown。

`.env.example` 中的 Key 字段保持为空。不要把真实 Key 写入 Git、截图、Issue 或测试文件。

### 测试

~~~bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/pytest -q
.venv/bin/python -m compileall src scripts tests
.venv/bin/python -m pip check
~~~

更完整的跨平台说明见 [安装文档](docs/setup.md)。

## 输入能力与边界

公共 URL 适配器负责 Provider 识别、SSRF 防护、URL 脱敏、yt-dlp metadata probe 和单视频边界检查。

项目不会提供：

- DRM、付费墙、登录或会员内容绕过
- 私有内容破解或地域限制规避
- 直播录制
- Playlist 批量抓取

实际可用性可能受到登录验证、验证码、出口网络和平台规则影响。

### 微信公众号公开文章

目前网页文章正式支持 **公开、免登录且可正常访问的微信公众号文章**（`mp.weixin.qq.com/s/...`）。处理链路为：

~~~text
微信公众号文章 URL → 安全 Fetch → 正文结构解析 → 正文图片 → Vision → AI 分析 → 知识精炼 → 01 / 02 / 03
~~~

不支持通用网页文章、知乎、雪球、Cookie 绕过、自动登录、浏览器 Cookie 读取、验证码绕过、会员或付费内容破解、私有内容或已删除文章恢复。访问频繁、登录受限、验证码或页面结构异常时会安全失败，不会伪造正文或知识稿。

正式支持常见视频、常见音频、.pptx 和 .docx。当前不直接支持旧格式 .ppt、.doc。

Office 能力边界：

- PPTX：文字、表格、图片、Chart、Notes 和隐藏页可解析；复杂动画与部分嵌入对象属于 partial。
- DOCX：Heading、Paragraph、List、Table、Image、Caption、Hyperlink、Header/Footer 可解析；复杂 TextBox、SmartArt、Comments、Footnotes 属于 partial 或 unavailable。
- PDF 和独立图片任务暂未支持。

## Unified Batch 与 FIFO

~~~text
多个公开 URL + 多个本地文件
              ↓
          统一预检
              ↓
          用户确认提交
              ↓
         多个普通 Task
              ↓
       Single FIFO Worker
~~~

Batch 是一次提交和追踪机制，不代表多个 Worker 并行执行。单个任务内部的 ASR 与 Vision 可按 Pipeline 策略并行。

## 三层知识资产

媒体任务：

~~~text
YYYYMMDD{标题}/
├── 01-{标题}逐字稿.md
├── 02-{标题}AI总结稿.md
└── 03-{标题}最终知识稿.md
~~~

文档任务：

~~~text
YYYYMMDD{标题}/
├── 01-{标题}原始内容整理.md
├── 02-{标题}AI分析稿.md
└── 03-{标题}最终知识稿.md
~~~

- 01 原始追溯层：保留来源结构、逐字稿或文档原始内容整理。
- 02 完整 AI 分析层：保留完整分析、证据和风险信息。
- 03 正式知识资产层：删除噪声并按知识逻辑重组，适合飞书、Obsidian、Markdown 知识库，也可作为后续 RAG / Agent 的输入。

当前项目尚未实现 RAG 或 Agent，只提供可供后续系统使用的知识资产。

## 知识资产导出

Markdown 仍然是默认的核心知识资产。生成 `03 最终知识稿` 后，可以按需导出为 Word 知识报告（DOCX）和 PowerPoint 演示稿（PPTX）。二者都是派生导出物，不改变原有 01 / 02 / 03 三层 Markdown 资产结构。

### Word 学术研究报告

- 基于最终知识稿本地确定性生成，可编辑，采用 A4 学术版式、中文学术字体、标题层级、页眉页脚与页码。
- 表格使用三线表、语义表题、重复表头与防拆行；超宽表自动采用横向页面。
- 可受控引用任务内已有的视频来源截图，并生成图注。
- 不需要额外 AI 或网络调用，不产生额外模型成本。

### PowerPoint 学术汇报导出

- 基于同一份结构化语义、表格、视觉素材和语言规范，本地确定性生成 16:9 学术研究演示稿。
- 支持表格页、图文页、标题与正文去重、稀疏页压缩，以及精简/标准/完整长度。
- PPT 导出为 **0 LLM、0 Provider、0 Network** 的本地流程；不会显示模型或 Provider 选择器。
- 过去实验性的 LLM 演示规划入口已在 V2.2.1 退役；传入旧 `planning_mode=ai` 会安全拒绝，不会读取密钥、调用模型或产生用量。

在 macOS 检测到 WPS Office 时，“打开 PPT”优先使用 WPS；未安装 WPS 或在其他系统时回退到系统默认应用。WPS 不是运行或测试的必需依赖。

## 配置与本地目录

公开默认目录均从项目根目录动态解析，也可以通过环境变量覆盖：

| 配置 | 默认值 | 作用 |
| --- | --- | --- |
| WEBUI_HOST | 127.0.0.1 | 本地监听地址 |
| WEBUI_PORT | 8502 | Web 端口 |
| TASK_WORK_ROOT | ./runtime/task_workspaces | 私有运行工作区 |
| KNOWLEDGE_OUTPUT_ROOT | ./outputs/knowledge_assets | 最终知识资产目录 |
| KNOWLEDGE_EXPORT_ROOT | ./outputs/exports | Word / PowerPoint 派生导出目录 |

本地运行会自动创建 runtime、outputs、logs 和必要的 SQLite；这些内容均被 Git 忽略。

最终知识资产默认位于 `./outputs/knowledge_assets`。任务媒体、帧、日志、数据库和过程 JSON 位于 `./runtime` 或 `./logs`，不会混入知识资产目录。

## 成本中心

成本中心按任务和阶段展示 ASR、Vision、AI Analysis 与 Knowledge Refinement 的用量和成本。**Usage 不等于理论成本，也不等于 Provider 实际账单**：请求级用量账本用于理论成本，实际账单仅在手动或 Provider 对账后显示。不同币种不会自动相加；未对账显示“未对账”，已确认零费用才显示 `0`。DeepSeek 中国账户使用 CNY 价格快照，并按高峰/低谷时段保存请求级价格依据。

当前成本汇总从 Cost Accounting Epoch 开始计算；历史任务、Token、请求与历史货币成本仍保留并可查询，但不会被重新计价或混入当前汇总。详情见 [成本核算说明](docs/cost-accounting.md)。本地模型可以记录运行时长并显示真实 0 成本。成本信息用于使用量管理，不代表模型质量或投资结果。

## 安全与隐私

- 项目本地优先，但 Vision 和 LLM 可调用用户配置的云 Provider，因此不宣称完全离线。
- API Key 不写入 Git、SQLite、任务 metadata、日志或知识资产；Web 设置页使用本地加密文件保存。
- 不要把 .env、config/secrets.enc 或 config/encryption.key 提交到 Git。
- Office 外部资源默认不自动获取。
- 只向用户主动配置的 AI Provider 发送完成任务所需的内容。
- 只处理你有权访问和使用的内容。

## 已知限制

- PDF 和独立图片任务暂未支持。
- .doc、.ppt 不直接支持。
- Playlist 和直播暂未支持。
- 登录受限、DRM 或私有内容不处理。
- 部分 DOCX/PPTX 高级对象只能部分解析。
- 平台访问可能受网络出口、验证码和平台规则影响。
- 部分模型价格无法可靠获取时显示“待定价”。
- AI 输出仍需用户判断和事实核验，不保证绝对无幻觉或 100% 准确。

## 常见问题

### 没有 API Key 能启动吗？

可以。Web、任务管理、本地预检和不依赖云模型的能力可以启动；需要 DeepSeek 或 DashScope / Qwen 时再配置相应 Key。

### 数据是否全部留在本机？

任务数据库、运行文件和知识资产默认留在本机。启用云端 Vision 或 LLM 后，完成任务所需的图片或文本会发送给用户主动配置的 Provider，因此不能把云模型模式理解为完全离线。

### 支持所有视频网站和 Office 文件吗？

不支持。公开视频仅限 yt-dlp 能合法解析的公开单视频页面；Office 当前正式支持 `.pptx` 和 `.docx`，不支持 `.ppt`、`.doc`、PDF 或独立图片任务。

### 批量任务会同时并行处理吗？

不会。Unified Batch 负责统一预检和提交，任务由单 Worker 按 FIFO 顺序执行；单个媒体任务内部的 ASR 与 Vision 可按流水线策略并行。

## 路线图

已完成：统一多输入、本地媒体、PPTX/DOCX、微信公众号公开文章、ASR、Vision、文档 Parser、AI Analysis、Knowledge Refinement、三层知识资产、Word 知识报告、PowerPoint 本地快速生成、Unified Batch、FIFO Worker 和 Balanced Productivity UI。

计划：PDF、独立图片、更完整的 Office 高级对象、质量评测，以及可选 RAG / Agent 下游集成。

## 贡献

欢迎提交 Issue 和 Pull Request。新增 InputAdapter、Document Parser、Knowledge Refinement 或 UI 组件前，请先阅读 [贡献指南](CONTRIBUTING.md)。

## ☕ 支持项目

如果这个项目对你的学习、研究或知识整理有所帮助，欢迎通过 Star、Issue、PR 或分享项目等方式支持它。

如果你愿意，也可以请作者喝杯咖啡 ☕。你的支持会用于项目持续维护、功能完善和文档更新。

<p align="left">
  <img src="docs/support/wechat-appreciation.png"
       width="250"
       alt="微信赞赏支持项目">
</p>

> 赞赏完全自愿，不影响项目的开源使用。

## License

本项目采用 [MIT License](LICENSE)。

---

当前稳定版本：**v2.2.1**
