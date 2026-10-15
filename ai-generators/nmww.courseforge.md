<h1 align="center">CourseForge · 把 PPT 课件升级成「可互动的网页课件」</h1>

<p align="center">
  <b>一个离线单文件 HTML 编辑器</b> —— 把传统 PPT 变成「基础层 + AI 互动层」的网页课件，<b>离线、零安装、零服务器</b>，配合本地 WorkBuddy 一键生成互动 H5。
</p>

<p align="center">
  <a href="https://nmww.github.io/courseforge/"><b>在线体验</b></a> ·
  <a href="https://github.com/nmww/courseforge/releases/latest"><b>下载单文件</b></a> ·
  <a href="https://github.com/nmww/courseforge/discussions"><b>讨论区</b></a> ·
  <a href="README_EN.md"><b>English</b></a>
</p>

---

> 🌐 **在线体验（无需下载，浏览器直接打开）：[courseforge 在线版](https://nmww.github.io/courseforge/)**
> 基础编辑、PPT 导入、内置互动组件（答题 / 投票 / 拖拽）即开即用；「调用 WorkBuddy 生成新互动」需本机运行 WorkBuddy。

**下载即用：** 从 [GitHub Releases](https://github.com/nmww/courseforge/releases/latest) 取走单个 `CourseForge.standalone.html`（约 1.4 MB，**不用注册、不用安装、不用联网**）。用任意现代浏览器打开它，它**本身就是编辑器** —— 没有安装步骤，因为没有需要安装的东西。

**10 秒上手：** 打开后 → 选一套模板 / 导入你的 PPT → 在需要互动的页面拖一个「🌐 HTML 交互容器」→ 点「调用 WorkBuddy 生成」或直接「插入内置组件」。全程不需要装任何软件，断网也能用。

**发给学生：** 点「🚀 导出课件包」得到一个单 HTML，U 盘 / 微信直接发，对方双击就能播放，**断网可运行**，不需要装任何东西。

---

## 为什么做这个（Why this exists）

老师的课件长期被困在两个极端之间：

- **PPT 很好编辑，但动不起来** —— 想插个答题、仿真、摄像头检测？PPT 做不到，只能另开网页、另切窗口。
- **网页互动很灵活，但失控** —— 把课件整体交给 AI 去转，排版错乱、版本混乱、AI 不可控，老师反而不敢改。

CourseForge 走中间路线，核心是一个**分层设计**：

- **底层基础层（固定、可控）**：PPT 导入的文字 / 图表 / 图片，或栅格化后的图片，不受 AI 影响，永久可编辑。
- **上层互动层（可替换）**：AI 生成的 HTML 交互容器是独立图层，可增删改、可清空重生成，**一键删除不破坏课件主体**。

> 它不把复杂的 PPT 转换逻辑塞进 AI 助手 —— WorkBuddy 只负责「生成互动 HTML 素材」这一件单一职责。课件编辑、PPT 解析、排版统一全部交给这个离线编辑器。这样老师操作简单、管控统一、迭代成本低。

## 里面有什么（What's inside）

| 能力 | 说明 |
|---|---|
| **PPT 标准化导入** | 内置统一解析内核（pptxjs），字体 / 尺寸 / 图层渲染规则全局锁定；导入后提供「全局统一样式」一键抹平不同 PPT 的风格差异。 |
| **分层课件模型** | 基础层（PPT 内容）+ 互动层（HTML 容器）完全解耦。AI 出错 = 删一个互动框，主体毫发无损。 |
| **拖拽式画布** | 仿 PPT 操作：左侧幻灯片缩略图增删页、中间主画布拖拽排版、任意元素都是图层。 |
| **AI 互动生成** | 选中容器 → 调用本地 WorkBuddy → 输入需求生成互动 H5 → 预览确认后回填；支持重生成 / 更换 / 清空 / 复制复用。 |
| **内置离线组件** | 答题 / 投票 / 拖拽三类合规 H5 离线即用，无需联网、无需 WorkBuddy，打开就看效果。 |
| **本地安全通信** | 编辑器与 WorkBuddy 通过本地 WebSocket（`127.0.0.1`）通信，AI **只回传 HTML 片段**，不持有完整课件，数据全程不上云。 |
| **工程 / 导出分离** | 「保存工程」= JSON（便于二次编辑）；「导出课件包」= 单 HTML（互动内联为 iframe `srcdoc`，便于离线分发）。 |
| **真·单文件** | `CourseForge.standalone.html` 把所有 JS/CSS 内联，零外部依赖，双击即开，适合统一下发给所有老师。 |

## 与 AI 协作（Use it with AI）

CourseForge 的互动内容由**本地 WorkBuddy** 生成，二者通过本地 WebSocket 通信（仅本机 `127.0.0.1`，默认 `ws://127.0.0.1:7788`）。

编辑器发请求：

```json
{
  "type": "generate",
  "requestId": 1,
  "prompt": "做一个浮力知识点的选择题小测验，3道题",
  "theme": { "primary": "#2563eb", "bodyFont": "Microsoft YaHei" },
  "size": { "w": 340, "h": 200 }
}
```

WorkBuddy 回传自包含的 HTML 片段（内联 CSS/JS，可离线 `srcdoc` 加载）：

```json
{ "type": "result", "requestId": 1, "title": "浮力小测验", "html": "<!doctype html>…完整自包含HTML…" }
```

- 未连接 WorkBuddy 时，内置 **Mock 生成器** 按关键词返回可用的答题 / 投票 / 拖拽小游戏，先体验后接入。
- 互动组件遵循 [`WIDGET_SPEC.md`](course-editor/WIDGET_SPEC.md)：接收 `--cf-*` 主题变量、响应 `cf:activate/deactivate` 生命周期、回传 `cf:event`。
- 给 AI 助手的完整集成指南见 [`docs/agents.md`](docs/agents.md)。

## 架构一句话（Architecture）

`course-editor/index.html` 是编辑器主体（Fabric.js 拖拽画布 + 分层渲染），PPT 解析走浏览器端 pptxjs，互动容器用受控 `iframe sandbox` 加载 WorkBuddy 生成的 H5；`build_singlefile.js` 把依赖内联成 `CourseForge.standalone.html`；`workbuddy-bridge.js` 是 WorkBuddy 侧 WebSocket 服务端的参考实现。详见 [`course-editor/README.md`](course-editor/README.md)。

## 安全防护（Security model）

- 互动 iframe 默认 `sandbox="allow-scripts allow-forms allow-popups allow-modals allow-same-origin"`；需要摄像头 / 麦克风时，老师在容器属性里**显式开启**「摄像头 / 麦克风 / 允许同源」，开启后追加 `allow-same-origin` 与 `allow="camera; microphone"`。
- AI 生成的内容只存在独立容器，**不写入底层基础层**；出错一键清空即可，不污染课件主体。
- 编辑器与 WorkBuddy 的通信仅限本机回环地址（`127.0.0.1`），互动素材生成后立刻回传，AI 不持有完整课件数据、不上云。
- 导出的课件包把互动 H5 内联为 `iframe srcdoc`，不引用任何外部 CDN —— 断网可运行，也意味着**不会偷偷加载第三方脚本**。

**已知短板（我们自己先说）：**

- **互动 HTML 由 AI 生成，本质是可执行代码。** 我们用 sandbox 限制它，但一旦老师手动勾选「允许同源」，隔离就被打开了 —— 这个开关只在你确实需要摄像头 / 本地存储时才开。
- **PPT 导入是浏览器端解析，不是像素级还原。** 复杂动画、SmartArt、嵌入视频会丢失或走样，复杂版式建议用「栅格化导入」（路线图中）或先在 PPT 里转成图片。
- **编辑体验是桌面优先。** 手机 / 平板上可以播放和查看，但拖拽排版不好用。
- **没有多人协作、没有版本历史。** 工程文件是本地 JSON，靠你自己的网盘 / Git 做版本管理。这是离线单文件路线的代价，暂不打算改。

## 从源码构建（Build from source）

**先说清楚：用这个工具不需要构建。** 直接打开 `course-editor/index.html` 就能跑，源码即产品，没有编译步骤。

构建只做一件事 —— 把 `libs/` 里的依赖内联进 HTML，生成便于单文件分发的 `CourseForge.standalone.html`：

```bash
cd course-editor
node build_singlefile.js     # → CourseForge.standalone.html（约 1.4 MB，零外部依赖）
```

只需要 Node（20+ 即可），没有后端、没有 npm 依赖要装、没有服务要起。改完 `index.html` 重新跑一次这条命令，单文件版就同步了。

## 延伸阅读（Where to read more）

| 文档 | 里面有什么 |
|---|---|
| [`course-editor/README.md`](course-editor/README.md) | **开发者主入口** —— 编辑器架构、数据模型、WebSocket 协议、扩展方式的详细说明。 |
| [`course-editor/WIDGET_SPEC.md`](course-editor/WIDGET_SPEC.md) | **互动组件规范 v0.1** —— 想自己写组件先看这个：主题变量 `--cf-*`、生命周期 `cf:activate/deactivate`、事件回传 `cf:event`。 |
| [`docs/agents.md`](docs/agents.md) | **给 AI 助手看的集成指南** —— 把这一页丢进任何模型的上下文，它就知道该生成什么格式的互动 HTML。 |
| [`docs/borrowing-bento.md`](docs/borrowing-bento.md) | **竞品分析台账** —— 逐条拆解 [bento](https://github.com/nyblnet/bento) 值得借鉴的设计，标注已落地 / 待做 / 主动跳过及原因。 |
| [`CHANGELOG.md`](CHANGELOG.md) | 版本历史，每个版本改了什么、修了什么。 |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`SECURITY.md`](SECURITY.md) | 如何贡献代码 / 如何私下报告安全问题（**安全问题请勿公开提 Issue**）。 |

**代码在哪：** `course-editor/` 是编辑器本体（`index.html` 主体 + `libs/` 离线依赖 + `widgets/` 内置组件 + `build_singlefile.js` 打包脚本 + `workbuddy-bridge.js` 桥接参考实现）；`docs/` 是文档；`assets/` 放仓库用图。整个项目没有第三方构建体系，翻起来很快。

## 路线图（Roadmap）

CourseForge 想成为的东西很具体：**老师用得起、管得住、带得走的课件工具** —— 不联网能用、不注册能用、导出的文件十年后还能打开。凡是要求上云、要求登录、要求装客户端的方向，都不在路线里。

按当前进度：

**✅ 已发布** —— 分层课件模型（基础层 + 互动层）、PPT 导入、拖拽画布、内置离线组件、单文件导出、示例画廊、页面缩略图、编辑器内放映模式。

**🚧 正在做** —— 「文档即文件」：让导出的课件包内嵌工程 JSON，双击即可回编辑器二次编辑，消灭「导出后改不了」的痛点。

**📋 计划中**（按性价比排，不承诺时间表）

| 方向 | 要解决的问题 |
|---|---|
| PPT 导入栅格化 | 用 LibreOffice Headless 每页转 PNG 作基础层，复杂版式不再走样 |
| 原生图表元素 | 零依赖图表引擎，老师不写代码就能出内嵌 SVG 图表，导出不依赖 CDN |
| `window.courseforge` 编排 API | 让 WorkBuddy 从「做互动素材」升级为「编排整本课件」 |
| 自动保存 + 恢复 | IndexedDB 静默缓存，防误关丢稿 |
| 互动模板市场 | 优质 H5 沉淀成可复用模板，单独导入导出 |
| 打印 / PDF 导出 | 老师发纸质讲义的刚需 |

**⚪ 主动不做** —— 多人实时协作、云端账号体系、自动更新通道。这些都要求常驻服务器，和「离线可控」的定位冲突。

> 想推动某一项？欢迎在 [Discussions → Ideas](https://github.com/nmww/courseforge/discussions/categories/ideas) 说明你的教学场景 —— **真实使用场景是我们排优先级的第一依据**。

## 致谢与参考（Acknowledgments & References）

本项目在设计与开发过程中参考了以下优秀开源项目，特此致谢：

| 项目 | 参考/借鉴内容 | 许可证 |
|---|---|---|
| [nyblnet/bento](https://github.com/nyblnet/bento) | 编辑器 UI 交互范式（缩略图预览、示例画廊、放映模式）、斜杠命令菜单、主题令牌等设计思路 | MIT |
| [pptxjs](https://github.com/nickmoss404/pptxjs) | 浏览器端 PPTX 文件解析渲染核心 | MIT |
| [Fabric.js](http://fabricjs.com/) | 画布拖拽、图层管理、对象序列化 | MIT |
| [jQuery](https://jquery.com/) | DOM 操作与事件处理 | MIT |
| [D3.js](https://d3js.org/) | 数据可视化绑定（图表/时间轴等组件底层） | BSD-3-Clause |
| [JSZip](https://stuk.github.io/jszip/) | PPTX ZIP 包解析 | MIT / GPLv3 |

> **著作权声明**：如果您在项目中引用了 CourseForge 的代码或设计思路，请在您的项目中保留本仓库链接及上述致谢信息，注明参考来源。尊重原创，共同推动教育工具生态发展。

## 社区（Community）

**不确定去哪说？按你要做的事对号入座：**

| 你想…… | 去这里 |
|---|---|
| ❓ **提问 / 求助** —— 装不上、导入乱了、组件不显示 | [Discussions → Q&A](https://github.com/nmww/courseforge/discussions/categories/q-a) |
| 💡 **提想法 / 功能建议** —— "要是能……就好了" | [Discussions → Ideas](https://github.com/nmww/courseforge/discussions/categories/ideas) |
| 🎨 **晒作品** —— 用它做了课件，想给别人抄作业 | [Discussions → Show and tell](https://github.com/nmww/courseforge/discussions/categories/show-and-tell) |
| 💬 **随便聊聊** —— 教学场景、AI 课件的想法 | [Discussions → General](https://github.com/nmww/courseforge/discussions/categories/general) |
| 🐛 **报 Bug** —— 有明确的复现步骤 | [提一个 Issue](https://github.com/nmww/courseforge/issues/new)（附复现步骤 + 截图 + 浏览器版本） |
| 🔒 **安全问题** | 走 [SECURITY.md](SECURITY.md) 的私下渠道，**不要公开提 Issue** |

> 📣 **特别想听一线教师说话。** 你不需要懂代码 —— 把"我备课时卡在哪一步"讲清楚就是最有价值的输入。真实教学痛点在我们的优先级排序里权重最高，高于任何技术上"看起来很酷"的功能。

## 参与贡献（Contributing）

欢迎 Fork 后提交 Pull Request，完整约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**打算做比较大的改动？请先开个 Issue 或 Discussion 说一声再动手。** 这个项目的架构有几条硬约束（离线可用、零外部依赖、基础层与互动层解耦），不先对齐的话，可能你写完了却因为撞上定位而没法合并 —— 那是双方都不想看到的浪费。小修小补（错别字、明显 Bug、文档改进）直接提 PR 就行，不用问。

## ☕ 打赏支持（Support the Project）

如果 CourseForge 对你的教学工作有帮助，欢迎打赏鼓励持续创作！

<p align="center">
  <img src="assets/tip-qrcode.png" alt="微信打赏" width="160" />
</p>
<p align="center">
  <small>微信扫一扫 · 每一份打赏都是创作的动力 🙏</small>
</p>

## License

CourseForge 基于 [MIT License](LICENSE) 开源 —— © 2026 The CourseForge authors。内置运行时组件（jQuery、D3、JSZip、pptxjs、Fabric.js）各自保留其开源许可证。
