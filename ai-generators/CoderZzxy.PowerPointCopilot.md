## PowerPointCopilot - PowerPoint 智能助手（VSTO 插件）

一个面向 PowerPoint 的本地智能助手：支持通过 AI 一键生成 PPT 大纲、自动排版并生成演示文稿。内置现代化 WebView2 界面，支持多模型配置、PPT 模板管理、Markdown 实时预览。完全本地运行，默认不留存隐私数据；项目将以 MIT 协议开放，免费、无商业限制。

> 当前版本以生成PPT为主，编辑能力在规划中。

### 📢 重要说明

- **作者工作繁忙，精力有限**，维护和更新可能不定期
- **请勿提交 PR**（作者不熟悉 GitHub 操作），建议通过 Issue 或微信反馈
- **可自由用于商业项目**，无需告知作者，无需付费
- 开源初衷：帮助开发者完成工作、为社会创造就业机会
- 如遇问题：提交 Issue 或微信联系（见文末"联系与反馈"）

### 🌟 核心亮点：无缝对接 WordCopilotChat

本项目与兄弟项目 **WordCopilotChat** 深度互通：
- **一键导入模型**：支持直接导入 WordCopilotChat 导出的模型配置文件，无需重复配置 API Key 和参数！
- **统一的体验**：相似的现代化 UI 交互，降低学习成本。

---

## 使用教程（在线阅读）

- 语雀：[《PowerPoint 使用教程》](https://www.yuque.com/u10028163/gl9lpg/ngv1qgq22ifrihnf?singleDoc#)

## 功能特性

- **AI 驱动的 PPT 生成**
  - 智能大纲：输入主题和需求，自动调用 AI 生成结构化的 Markdown 大纲
  - 自动排版：一键将大纲转换为精美的 PowerPoint 幻灯片
  - 灵活调整：支持生成前预览和编辑 Markdown 大纲
- **现代化交互界面**
  - 基于 WebView2 的 Web UI，提供流畅的三步向导式体验（配置参数 → 选择模板 → 生成 PPT）
  - 支持 Markdown 实时渲染和代码高亮
- **强大的模型管理**
  - 已适配国产模型：DeepSeek、Kimi、ChatGLM、MiniMax 的最新旗舰模型
  - 支持自定义 BaseUrl / ApiKey / 参数
  - **支持思考模型**：自动过滤 `<think>` 标签，完美适配 DeepSeek-R1 等推理模型
  - **支持流式输出**：实时显示 AI 生成过程，拒绝漫长等待
- **PPT 模板管理**
  - 可视化模板库：支持导入自定义 PPT 模板
  - 模板预览：直观展示模板缩略图
  - 智能适配：自动识别模板布局并填充内容
- **安全与本地化**
  - 数据本地存储（SQLite + FreeSql）
  - 自动保存机制，防止意外丢失

---

### ⚙️ 模型配置注意事项

#### 已适配的国产模型

- **DeepSeek**、**Kimi**、**ChatGLM**、**MiniMax** 的最新旗舰模型
- 支持自定义 API 地址、ApiKey、请求参数
- 也可使用其他兼容 OpenAI API 格式的自定义模型接口
- 已适配 **deepseek-reasoner** 等思考模型，系统会自动处理思维链输出

#### ⚠️ API 地址配置重要说明

**本项目采用 HTTP 直接调用方式，需要填写完整的请求地址（Request URL），不同于使用 OpenAI SDK。**

**关键区别**：

- 🔸 **OpenAI SDK**（如 Python/Node.js） - `base_url` 参数只需填写到版本号，SDK 会自动拼接 `/chat/completions`
- 🔸 **本项目**（HTTP 直接请求） - 需要填写**完整的 API 请求地址**，包含 `/chat/completions` 端点

#### 📌 配置示例对比（以 Qwen 为例）

| 调用方式                     | 填写内容                                                     | 说明            |
| ---------------------------- | ------------------------------------------------------------ | --------------- |
| **OpenAI SDK** 的 `base_url` | `https://dashscope.aliyuncs.com/compatible-mode/v1`          | SDK自动拼接端点 |
| **本项目** 的 API 地址       | `https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions` | 填写完整URL     |

> ⚡ **简单记法**：如果您从模型提供商文档获取的是 SDK 的 `base_url`，在本项目中需要**手动添加** `/chat/completions` 后缀。

#### 🎯 常见模型完整 API 地址

| 模型提供商          | 完整 API 请求地址                                            |
| ------------------- | ------------------------------------------------------------ |
| **DeepSeek**        | `https://api.deepseek.com/chat/completions`                  |
| **Kimi (Moonshot)** | `https://api.moonshot.cn/v1/chat/completions`                |
| **ChatGLM (智谱)**  | `https://open.bigmodel.cn/api/paas/v4/chat/completions`      |
| **通义千问 (Qwen)** | `https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions` |
| **MiniMax**         | `https://api.minimaxi.com/v1/chat/completions`               |

> 💡 **配置提示**：直接复制上表中对应模型的完整地址，粘贴到"模型列表"的 API 地址字段即可。

---

### 运行截图（示意）

- 功能区按钮：打开助手、模型管理、模板管理
- WebView2 生成界面：参数配置、模板选择、大纲预览

> 注：请以实际运行为准，界面持续优化中。

### 演示
以下为部分演示

#### 1. 生成PPT配置配置
![1.配置与生成大纲](PowerPointCopilot/docs/gif/生成PPT配置配置.gif) 

#### 2. 纯生成PPT
![2.纯生成PPT](PowerPointCopilot/docs/gif/纯生成PPT.gif) 

#### 3. 上传模板
![3.上传模板](PowerPointCopilot/docs/gif/上传模板.gif) 

#### 3. 选择模板并生成PPT

![3.选择模板并生成PPT](PowerPointCopilot/docs/gif/选择模板并生成PPT.gif) 

---

## 快速开始

### 环境要求
- 操作系统：Windows 7 Service Pack 1 及以上（Windows 10/11 推荐）。
- Microsoft PowerPoint：最低支持 2013（建议使用 2019 及以上版本）。
- .NET Framework：必须为 4.8 及以上版本（不支持低于 4.8）。下载地址：https://dotnet.microsoft.com/zh-cn/download/dotnet-framework/net48
- Microsoft Edge WebView2 Runtime：
  - Windows 7：最后支持版本为 109（官方已不再提供下载页面，可在第三方渠道获取对应安装包）。
  - Windows 10/11：可从微软官网直接下载并安装：https://developer.microsoft.com/zh-cn/microsoft-edge/webview2/?cs=4112006293&form=MA13LH#download
- Visual Studio 2010 Tools for Office Runtime（VSTO 运行时）：https://www.microsoft.com/zh-cn/download/details.aspx?id=105890

可选（仅限开发者环境）：
- Visual Studio 2019/2022（安装“Office/SharePoint 开发”工作负载）用于编译与调试此 VSTO 插件。

### 获取代码与依赖
1. Clone 仓库：`git clone https://github.com/CoderZzxy/PowerPointCopilot`
2. 双击打开 `PowerPointCopilot.sln`（或使用 VS 打开所在解决方案/文件夹）
3. 还原依赖（NuGet）：FreeSql、Microsoft.Web.WebView2、Newtonsoft.Json 等

### 调试运行
1. 在 VS 中设置启动项目为 `PowerPointCopilot`
2. F5 启动（首次会启动 PowerPoint 并加载该 Add-in）
3. 在 PowerPoint 功能区找到 “PowerPointCopilot” 相关按钮
   - “生成PPT” → 显示右侧 WebView2 面板
   - “模型管理”“模板管理”等

### 首次配置
1. 打开“模型管理”，新增一个模型（或直接导入 WordCopilotChat 的模型配置）
2. 在“模板管理”中添加您常用的 PPT 模板
3. 点击“生成PPT”打开侧边栏，输入主题，选择模型和模板，即可开始生成！

---

## 目录结构（简要）
```
PowerPointCopilot/
  core/              # 核心业务逻辑（Markdown解析、幻灯片构建等）
  forms/             # WinForms 各类设置/管理窗口
  services/          # 模型、模板等服务层（FreeSql + SQLite）
  utils/             # WebView2/OpenAI/PPT 工具、加密等
  wwwroot/           # 前端（WebView2）资源：index.html、css、js
  Ribbon1.*          # PowerPoint 功能区
  ThisAddIn.*        # VSTO 入口，初始化数据库表等
```

---

## 常见问题
### 安装与环境

**Q: PowerPoint 未被正确加载？**  
A: 请确认已安装与 VS 匹配的 VSTO 组件，并以管理员身份启动 VS 再调试

**Q: WebView2 白屏？**  
A: 请安装/更新 WebView2 Runtime；或检查 `Microsoft.Web.WebView2` 依赖是否成功还原

### 功能使用

**Q: 生成的 PPT 格式错乱？**  
A: 请确保您选择的 PPT 模板包含标准的“标题”和“内容”占位符。插件依赖这些占位符来填充内容。

**Q: 思考模型（如 DeepSeek-R1）生成很慢？**  
A: 思考模型需要先输出思维链，插件会自动过滤 `<think>` 标签内容，您可能需要等待一段时间才能看到实际的大纲内容输出。

### 贡献与反馈

**Q: 我发现了 Bug 或想贡献代码，如何处理？**  
A: **请勿提交 PR**。作者对 GitHub 操作不熟，建议通过以下方式：

   - 提交 Issue 详细描述问题或功能需求
   - 添加作者微信（备注"PowerPointCopilot"）
   - 作者会在空闲时间处理您的反馈

**Q: 可以基于此项目开发商业版吗？**  
A: **完全可以，无需告知作者，无需付费。** 本项目采用 MIT 许可证，允许任何形式的商业使用。作者开源的初衷就是帮助更多人，不会收费也不会限制商业化。

---

## 贡献方式（重要说明）

### ⚠️ 请勿提交 Pull Request

由于作者对 GitHub 操作不够熟悉，且工作较忙（经常加班），**暂时无法及时审核和合并他人代码**。

### ✅ 推荐的反馈方式

如果您发现 Bug 或有功能建议，请通过以下方式联系：

1. **提交 Issue**（推荐）- 详细描述问题或需求
2. **添加作者微信**（见文末） - 备注"PowerPointCopilot"并说明来意

作者会在空闲时间处理 Issue 中的 Bug 修复和功能新增。

### 🚀 商业化使用说明

**您可以自由基于本项目开发商业版本，无需告知作者，也无需付费。**

- ✅ 允许基于此代码开发商业产品
- ✅ 允许修改、二次开发、闭源
- ✅ 无需向作者支付任何费用
- ✅ 无需告知作者商业化用途

### 💡 开源初衷

作者开源此插件的目的是：

- 为社会增加一些就业岗位
- 帮助在岗开发人员更好地完成工作任务
- 为有需要的个人和企业提供免费的技术方案

**因此本项目永久免费，不会商业化收费。** 作者会尽最大努力持续迭代更新，除非出现更优秀的替代开源方案。

## 许可协议

本项目采用 **MIT License** 开源。MIT 是宽松、商业友好的许可证，允许：

- ✅ 复制、修改、再发布
- ✅ 商业使用（无需告知作者）
- ✅ 私有使用和闭源修改
- ⚠️ 唯一要求：在分发时保留版权与许可声明

**简而言之：您可以用它做任何事，包括开发商业产品，完全免费。**

---

## 开源组件与许可
本项目依赖以下第三方组件（按字母序），感谢开源社区的贡献。具体许可以各项目官方仓库为准：
- [FreeSql / FreeSql.Provider.Sqlite](https://github.com/dotnetcore/FreeSql)
- [highlight.js](https://highlightjs.org/)
- [Marked](https://marked.js.org/)
- [Microsoft Edge WebView2](https://learn.microsoft.com/microsoft-edge/webview2/)
- [Newtonsoft.Json](https://www.newtonsoft.com/json)

---

## 致谢
感谢所有热心的使用者、贡献者与朋友们的支持与建议；社区的反馈让项目不断变得更好。

---

## 联系与反馈
### 📮 问题反馈方式

本项目为业余开源项目，作者精力有限（经常加班），维护不承诺即时响应。

**如遇 Bug 或有功能需求，请优先选择：**

1. **提交 Issue**（推荐） 
   - 附上详细的复现步骤、截图、日志文件
   - 说明您的环境（Windows版本、PowerPoint版本、.NET版本）

2. **添加作者微信**
   - 备注"PowerPointCopilot + 问题简述"
   - 仅用于严重问题或紧急咨询

**⚠️ 请勿提交 PR**：作者对 GitHub 操作不熟，暂时无法及时处理代码合并。建议通过 Issue 或微信说明需求，作者会在空闲时完成开发。

### 💖 如果觉得有用

- ⭐ 给个 Star 支持一下
- 📢 推荐给有需要的朋友
- 💬 在 Issue 中分享您的使用体验

### 作者微信
> 添加时请备注“PowerPointCopilot”，仅严重问题或合作沟通  
![作者微信](PowerPointCopilot/docs/wechat.png) 

## 📌 最后说明

这个项目凝聚了作者的心血，开源出来是希望能帮助到更多人。虽然作者工作繁忙，但会尽力维护和改进。

**致使用者**：

- 如果这个工具对您有帮助，欢迎点个 Star ⭐
- 如果您发现了问题，请通过 Issue 或微信告诉我
- 如果您想基于此开发商业产品，完全没问题，祝您成功 🎉

**致开发者**：

- 这个项目采用 MIT 协议，您可以自由使用、修改、商业化
- 不需要告知我，不需要付费，不需要分享收益
- 如果您愿意，可以在您的产品中注明原项目出处（不强制）

让技术造福更多人，这就是开源的意义。💪
