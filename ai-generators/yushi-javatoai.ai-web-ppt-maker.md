# AI 网页 PPT 生成器

![License](https://img.shields.io/github/license/yushi-javatoai/ai-web-ppt-maker)
![CI](https://github.com/yushi-javatoai/ai-web-ppt-maker/actions/workflows/ci.yml/badge.svg)
![Node](https://img.shields.io/badge/node-%E2%89%A5%2020-brightgreen)
![Express](https://img.shields.io/badge/Express-5-000000)
![Frontend](https://img.shields.io/badge/frontend-Vanilla%20ES%20Modules-FFDD57)

把一段长文案粘贴进来，AI 大模型自动把它拆解成一份多页网页 PPT：
流式生成实时进度 → 网页全屏演示（键盘翻页 / 触摸滑动）→ 多套配色主题 → 一键导出独立 HTML 文件。

## 功能特性

- **长文一键拆解**：后端调用 OpenAI 兼容协议大模型，将长文案重构为 6~12 页结构化 PPT（封面 / 章节 / 要点 / 数据指标 / 双栏对比 / 金句 / 结尾等 7 种版式）。
- **真正的流式生成**：上游 SSE 逐 token 读取，逐页解析并逐页推送；前端实时显示「AI 深度思考 → 生成第 N/M 页」进度与页标题列表，可随时停止。
- **容错解析器**：大模型输出不规范（代码块围栏、多行 JSON、同行多对象、夹杂说明文字、无效对象）也能稳定提取；格式完全失败时自动用更严格提示词重试一次。
- **网页 PPT 放映**：16:9 幻灯片自动缩放适配任意屏幕，`←`/`→`/空格/PageUp/PageDown/Home/End 翻页，`F` 全屏，`Esc` 退出，支持触摸滑动与点击翻页。
- **4 套配色主题**：极光蓝 / 深海夜 / 森林绿 / 落日橙，编辑页与演示内均可一键切换，选择随导出保存。
- **独立 HTML 导出**：导出文件内联渲染引擎 + 主题样式 + PPT 数据，双击即放映，无需服务器，可分享。
- **响应式多端兼容**：桌面 / 平板 / 手机自适应布局，移动端触摸翻页。
- 断点续用：文案、主题与最近一次生成的 PPT 自动保存到 localStorage。

## 技术栈

| 层 | 技术 |
| --- | --- |
| 后端 | Node.js + Express 5（SSE 流式响应、静态托管） |
| 前端 | 原生 ES Modules + CSS（零构建，渲染引擎与导出 HTML 完全同源） |
| AI | OpenAI 兼容协议 `POST /chat/completions`（stream: true），原生 fetch 解析 SSE |
| 测试 | 解析器单元测试 + jsdom 前端集成测试（真实 HTTP/SSE 链路）+ 内置 Mock LLM 服务 |

> 前端刻意采用零构建方案：演示渲染引擎（`src/deck/renderer.js`）是纯原生 DOM 的
> 自包含脚本，应用内与导出 HTML 共用同一份源码，保证所见即所得；同时规避了
> 复杂构建链在受限环境下的兼容性问题。

## 快速开始

```bash
npm install        # 安装依赖（仅 express；puppeteer-core 仅测试用）
npm start          # 启动：http://127.0.0.1:8787
```

打开页面 → 粘贴长文案（或点「载入示例文案」）→ 点击「✨ AI 生成 PPT」→ 生成完成后「▶ 全屏演示」或「⬇ 导出 HTML」。

## 配置

后端读取 `.env`（不存在时使用内置默认值）：

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com/v1` | OpenAI 兼容接口地址 |
| `DEEPSEEK_API_KEY` | （内置默认） | API Key |
| `DEEPSEEK_MODEL` | `deepseek-v4-pro` | 模型 id；特殊连字符（如 `‑`）会被自动规范化为 ASCII `-` |
| `DEEPSEEK_TIMEOUT_MS` | `180000` | 单次生成超时（毫秒） |
| `PORT` | `8787` | 后端端口 |

## API

### `POST /api/generate`

请求：`{"content": "长文案"}`（10 ~ 30000 字）。响应为 SSE 事件流：

| 事件 | data | 说明 |
| --- | --- | --- |
| `thinking` | `{chars}` | 模型深度思考阶段（推理 token 进度） |
| `outline` | `{title, subtitle, pages[]}` | 提纲：总标题与全部页标题 |
| `page` | `{index, title, layout, blocks[]}` | 每解析完一页立即推送 |
| `done` | `{title, pages, usage}` | 全部完成（含 token 用量） |
| `error` | `{message}` | 出错（上游错误已翻译为可读文案） |

### `GET /api/health`、`GET /api/export-assets`

健康检查与导出资源（渲染引擎源码 + 主题/版式样式）。

## 测试

```bash
npm test          # 流式 JSONL 解析器单元测试（14 例）
npm run mock:llm  # 启动 Mock OpenAI 服务（端口 8788，测试用）
npm run e2e       # 端到端测试（Mock LLM：完整流程 + 错误/重试/超时/停止）
npm run e2e:real  # 端到端测试（真实 DeepSeek API）
```

E2E 采用 jsdom 加载真实前端源码（`src/main.js` 全链路）驱动真实 DOM 事件，
后端与 AI 接口全程真实运行：`jsdom(前端) → HTTP SSE → Express → (Mock | DeepSeek)`，
覆盖流式阶段流转、页数、主题切换、独立 HTML 导出、全屏演示与键盘翻页、
错误/重试/超时/停止路径。

Mock 服务按用户消息标记切换行为：`[[MALFORMED]]` 垃圾输出、`[[RETRY]]` 首次失败二次成功、
`[[HTTP401]]` 鉴权失败、`[[STALL]]` 挂起触发超时。

真实生成数据输出到 `test-artifacts/deck-real.json`。

## 项目结构

```
server/
  index.js           Express：SSE 接口 / 静态托管 / 导出资源
  config.js          环境配置（.env + 默认值 + 模型 id 规范化）
  prompt.js          拆解 PPT 的系统提示词（含严格重试版本）
  llm.js             上游流式调用 + 事件分发 + 页面规范化 + 重试
  jsonl.js           容错流式 JSONL 提取器（括号配对 + 抢救算法）
  mock-openai.js     测试用 Mock OpenAI 服务
src/
  app.js             应用主逻辑（编辑 / 进度 / 缩略图 / 导出 / 主题）
  api.js             前端 SSE 流式客户端（含超时看门狗）
  progress-panel.js  流式进度面板
  present.js         全屏演示挂载层
  deck/
    renderer.js      渲染引擎（应用内与导出共用，window.DeckApp）
    styles.css       版式样式（7 种 layout）
    themes.css       4 套主题变量
    exportHtml.js    独立 HTML 组装（内联引擎 + 样式 + 数据）
scripts/
  test-parser.mjs    解析器单元测试
  e2e.mjs            jsdom 端到端集成测试
```
