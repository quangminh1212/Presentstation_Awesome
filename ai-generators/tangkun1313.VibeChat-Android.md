# VibeChat Android

VibeChat 是一个本地优先的 Android 人设聊天 App。它把 GPT-5.5 兼容接口接入到 童锦程 skill、张雪峰 skill、毛选 skill、丁元英 skill、DBS skill、金融研报 skill 六个 persona skill 中，让用户可以在同一个移动端界面里切换不同风格的智能体聊天；其中「金融研报」智能体还额外支持把当前对话材料一键整理成 PowerPoint 文件。

当前仓库包含完整 Android 源码、可直接安装的 debug APK、展示截图、构建配置模板和发布说明。仓库不包含 API key，也不会提交本机真实配置文件。

## 项目定位

VibeChat 的目标不是做一个普通聊天壳，而是把不同的思考方式做成可切换的移动端 agent：

- 用户不需要在多个 prompt 或多个聊天窗口之间来回复制。
- 每个 agent 都有自己的头像、简介、开场提示、系统 skill 和历史记录。
- 模型、API key、测试链接可以在 App 内配置，配置保存在本机。
- 金融研报 agent 针对「研究输出」做了额外能力，可以把对话转成 PPT。

适合的使用场景：

- 手机上快速切换不同风格的 AI 助手。
- 把关系、教育、商业、战略、结构判断、金融研报等不同问题交给不同 agent。
- 用一个本地 App 验证 GPT-5.5 中转站接口、prompt skill、移动端聊天体验和 AI PPT 输出链路。

## 下载与安装

### GitHub Release

- Release 页面：[`v1.0.0-debug`](https://github.com/tangkun1313/VibeChat-Android/releases/tag/v1.0.0-debug)
- APK 附件：`VibeChat-debug.apk`

### 仓库内 APK

- 安装包：[`apk/VibeChat-debug.apk`](apk/VibeChat-debug.apk)
- 包名：`com.nullchat.app`
- 版本名：`1.0.0`
- 版本号：`1`
- APK 类型：debug build
- APK SHA-256：`49903E6D988F051A0F33B4BCC96AAFB22FE7B1508325C1980BAE20DCC5735D40`

> 这是调试版 APK，适合测试和演示。正式发布前应改用 release 签名、混淆、后端鉴权和更完整的密钥管理。

## 界面截图

| 首页与人设切换 | 童锦程聊天风格 |
| --- | --- |
| ![VibeChat 首页](docs/screenshots/home.png) | ![VibeChat 聊天](docs/screenshots/chat.png) |

| 金融研报 Agent | 研报输出与 AI PPT |
| --- | --- |
| ![金融研报 Agent](docs/screenshots/research-agent.png) | ![金融研报输出](docs/screenshots/research-output.png) |

| 输入法适配 | 设置保存提示 |
| --- | --- |
| ![输入法适配](docs/screenshots/keyboard-safe.png) | ![设置保存提示](docs/screenshots/settings-saved.png) |

## 核心功能

### 1. 六个可切换智能体

VibeChat 当前内置六个 agent，每个 agent 都有独立的 persona skill 文件：

| Agent | 定位 | 典型问题 | Skill 文件 |
| --- | --- | --- | --- |
| 童锦程 | 关系与人性 | 关系内耗、恋爱判断、人际困惑、自我成长 | `app/src/main/assets/personas/tong.md` |
| 张雪峰 | 教育与职业选择 | 专业选择、城市选择、就业方向、家庭条件约束 | `app/src/main/assets/personas/zhang.md` |
| 毛选 | 战略与矛盾分析 | 主要矛盾、竞争格局、阶段策略、组织问题 | `app/src/main/assets/personas/maoxuan.md` |
| 丁元英 | 结构与文化属性 | 结构判断、欲望与代价、长期局、资源约束 | `app/src/main/assets/personas/ding.md` |
| DBS | 商业诊断 | 商业模式、定价、产品、执行卡点、错误问题消解 | `app/src/main/assets/personas/dbs.md` |
| 金融研报 | 综合研报与 AI PPT | 公司研究、行业研究、财报公告、券商观点、PPT 输出 | `app/src/main/assets/personas/research.md` |

### 2. 独立聊天历史

每个人设有自己的聊天记录，切换 agent 时不会把不同风格的上下文混在一起。当前实现使用 Android `SharedPreferences` 保存最近历史，适合轻量测试和本地使用。

### 3. 模型配置弹窗

App 右上角提供 `设置` 按钮，可以配置：

- 测试链接，例如 `https://api.namax.ai/v1`
- 模型名，例如 `GPT-5.5`
- API key

点击 `保存并测试连接` 后，App 会保存配置，并通过一次轻量请求检测接口是否可用。配置成功后弹窗会自动关闭，主界面会显示连接状态。

### 4. OpenAI Chat Completions 风格接口

当前请求格式兼容 Chat Completions：

- `POST /chat/completions`
- `Authorization: Bearer <api key>`
- `model`
- `messages`
- `temperature`
- `max_tokens`
- `stream: false`

`https://www.namax.ai/v1` 会在 App 内自动规范化为 `https://api.namax.ai/v1`。如果传入的 URL 已经以 `/chat/completions` 结尾，App 会直接使用该地址。

### 5. 金融研报一键 AI PPT

选择「金融研报」agent 后，顶部会出现 `AI PPT` 按钮。点击后，App 会基于当前研报对话材料生成 PPT 结构，再写成标准 `.pptx` 文件。

PPT 输出路径：

```text
Downloads/VibeChat
```

PPT 生成链路：

1. 收集当前金融研报 agent 最近对话内容。
2. 让模型生成结构化 PPT JSON。
3. 使用 `OfficeFiles.java` 把 JSON 写成 PowerPoint 文件。
4. 如果模型输出不可解析，使用 `FallbackPptDeck.java` 生成兜底演示稿结构。
5. 保存到手机 Downloads 目录。

### 6. 移动端 UI 适配

当前版本针对真机使用做了这些处理：

- 顶部深色区域集中放品牌、设置、清空、人设入口。
- 人设卡片横向滑动，简介跟随卡片显示。
- 输入框底部固定，输入法弹出时尽量保持布局稳定。
- `windowSoftInputMode="adjustResize"` 配合键盘 inset 保护，减少输入法遮挡。
- 发送按钮、设置按钮、清空按钮都为手机触控尺寸做过调整。

## 使用流程

1. 安装 `VibeChat-debug.apk`。
2. 打开 App，输入访问密码进入。
3. 点击右上角 `设置`。
4. 填入测试链接、模型名和 API key。
5. 点击 `保存并测试连接`。
6. 回到主界面，选择一个 agent。
7. 输入问题并发送。
8. 如果选择的是「金融研报」，可点击 `AI PPT` 导出当前研报内容。

## 本地数据与隐私

VibeChat 当前是本地优先实现：

- API key 保存在手机 App 私有配置中。
- 当前人设、模型配置和聊天记录保存在本机。
- PPT 文件保存到用户可见的 `Downloads/VibeChat`。
- 仓库不包含真实 API key。
- 仓库不包含真实 `local.properties`。

需要注意：

- Android 客户端无法真正保护内置访问密码，正式产品应改为服务端鉴权。
- debug APK 不应作为正式分发版本。
- 如果面向更多用户发布，应把 API key 放在服务端，不应让用户共用同一个客户端内置 key。

## 安全与密钥处理

本仓库做了以下处理，避免把敏感信息上传到 GitHub：

- `local.properties` 已加入 `.gitignore`。
- 本地真实访问密码通过 Gradle `BuildConfig` 从 `local.properties` 注入。
- 仓库只保留 `local.properties.example` 模板。
- README 只写接口示例，不写真实 API key。
- 调试日志、手机 XML 抓取、临时 PPT 测试文件、旧 APK 和授权日志都被排除。

本地配置模板：

```properties
sdk.dir=C\:\\Android\\Sdk
vibechat.permanentPassword=VibeChatDemo123
vibechat.tempPassword=VibeChatTemp123
vibechat.tempPasswordExpiresAt=2026-07-29T23:59:59+09:00
```

## 技术结构

```text
app/src/main/java/com/nullchat/app/
  MainActivity.java        # 主界面、登录、设置、聊天、模型请求、AI PPT 入口
  OfficeFiles.java         # PPTX / Office 文件写入
  FallbackPptDeck.java     # PPT 生成失败时的兜底结构

app/src/main/assets/personas/
  tong.md                  # 童锦程 skill
  zhang.md                 # 张雪峰 skill
  maoxuan.md               # 毛选 skill
  ding.md                  # 丁元英 skill
  dbs.md                   # DBS skill
  research.md              # 金融研报 skill

app/src/main/res/drawable-nodpi/
  app_icon.png             # App 图标
  avatar_*.jpg/png         # 各 agent 头像

apk/
  VibeChat-debug.apk       # 当前可安装 debug 包

docs/screenshots/
  *.png                    # GitHub README 展示截图
```

## 关键源码说明

### `MainActivity.java`

负责 App 主流程：

- 访问密码校验
- 人设构建和切换
- 顶部 UI、横向人设卡片、聊天列表和底部输入栏
- 设置弹窗、模型配置保存和连接测试
- 聊天请求组装和结果解析
- 金融研报 AI PPT 按钮显示逻辑
- PPT 文件保存到 Downloads
- 输入法弹出时的布局保护

### `OfficeFiles.java`

负责把结构化内容写成 Office 文件，当前重点是 PPTX：

- 生成 PowerPoint 包结构
- 写入 slide、theme、relationship、content types
- 处理标题、段落、要点、表格和基础视觉样式
- 输出标准 `.pptx` 字节流

### `FallbackPptDeck.java`

当模型没有返回可解析 PPT JSON 时，使用兜底逻辑从对话内容提炼演示稿：

- 封面
- 核心结论
- 研究框架
- 关键发现
- 风险与待验证问题
- 后续行动建议

## 从源码构建

### 环境要求

- Android SDK
- JDK 21
- Gradle Wrapper 已随仓库提交

### 准备本地配置

复制模板：

```powershell
Copy-Item local.properties.example local.properties
```

修改 SDK 路径和本地访问密码配置：

```properties
sdk.dir=C\:\\Android\\Sdk
vibechat.permanentPassword=VibeChatDemo123
vibechat.tempPassword=VibeChatTemp123
vibechat.tempPasswordExpiresAt=2026-07-29T23:59:59+09:00
```

### 构建 debug APK

```powershell
.\gradlew.bat assembleDebug
```

输出文件：

```text
app/build/outputs/apk/debug/app-debug.apk
```

### 安装到已连接 Android 设备

```powershell
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

## 已验证内容

当前仓库发布前已完成这些验证：

- Android debug APK 可以构建成功。
- 真机上可以安装运行。
- 六个人设可以正常切换。
- 设置弹窗可以保存模型配置并测试连接。
- 输入法弹出时底部输入栏不会把页面撑坏。
- 金融研报 agent 可以触发 AI PPT。
- 已生成并验证标准 `.pptx` 文件。
- GitHub 仓库中不存在真实 API key。
- GitHub 仓库中不存在真实 `local.properties`。
- Release 附件 APK SHA-256 与本地 APK 一致。

## 当前限制

- 这是 debug APK，不是正式 release 包。
- 本地聊天历史使用 `SharedPreferences`，适合轻量测试，不适合大量长期数据。
- API key 存在客户端本地，正式产品建议改成服务端代理。
- 访问密码属于客户端保护，只适合演示和轻量限制。
- 当前没有账号体系、云同步、多端同步和后台管理台。
- 金融数据本身仍需要用户核验来源和时点，App 不替代投资判断。

## 后续路线

建议下一步迭代：

1. 增加 release 签名和正式包构建脚本。
2. 把模型请求迁移到服务端代理，避免客户端直接持有 key。
3. 用 Room 数据库替换 `SharedPreferences` 聊天历史。
4. 增加会话管理、搜索、导出 Markdown。
5. 给每个 agent 增加独立参数，例如温度、最大上下文、快捷问题。
6. 金融研报增加来源引用、表格解析和更强的 PPT 模板。
7. 增加 UI 主题、字体大小、深浅色切换。
8. 增加自动化测试和 GitHub Actions 构建。

## 仓库状态

- 默认分支：`main`
- 当前发布：`v1.0.0-debug`
- 仓库可见性：private
- 当前 APK：`apk/VibeChat-debug.apk`
- Release 附件：`VibeChat-debug.apk`
