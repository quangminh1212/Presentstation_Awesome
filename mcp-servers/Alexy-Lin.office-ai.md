# Office AI

用自然语言操控 Office 三件套：PowerPoint、Excel、Word。

---

## 安装 OpenCode

OpenCode 是一个 AI 编程助手，本项目通过它的 **MCP（模型上下文协议）** 功能来控制 Office 软件。

1. 打开浏览器访问 [opencode.ai](https://opencode.ai)
2. 点击下载 **OpenCode Desktop**（桌面版安装包）
3. 双击安装，按提示完成即可

> 安装完成后，桌面上会出现 OpenCode 的图标。

### 关于权限批准

OpenCode 在操作你的电脑时（比如打开 PowerPoint、修改文件等），会先请求你的**许可**。每次使用时，OpenCode 会弹出一个权限提示，你需要点击 **允许（Approve）** 它才会执行操作。

> 这是为了保护你的电脑安全，防止 AI 未经授权执行任何操作。放心使用，每次都会有明确的提示。

### 关于 AI 额度

OpenCode 首次使用会赠送免费额度，你可以直接使用。

如果免费额度用完了，就需要自己配置 AI 模型的 API 密钥。以 **DeepSeek** 为例：

1. 打开 DeepSeek 官网（platform.deepseek.com），注册账号
2. 在后台创建一个 **API Key**，复制下来
3. 打开 OpenCode 的设置，找到 **Provider（模型提供商）** 设置
4. 选择 **DeepSeek**，把 API Key 粘贴进去
5. 保存即可

> 配置完成后，OpenCode 就会使用你自己的 DeepSeek 额度，不再消耗免费额度。其他 AI 模型（如 ChatGPT、Claude）配置方式类似。

---

## 三大 Office MCP 的作用

### PowerPoint 制作（ppt-mcp）

让 AI 直接控制 PowerPoint，你可以用大白话告诉它：

- "生成一个5页的产品介绍PPT，蓝色主题"
- "把第3页的标题改成红色加粗"
- "给第2页加一个柱状图"

AI 会实时操作 PowerPoint，你马上就能看到效果。

### Excel 数据处理（excel-mcp）

让 AI 直接控制 Excel，你可以说：

- "把这个表格按销售额从高到低排序"
- "用这列数据生成一个饼图"
- "把第1行冻结，加上筛选按钮"

### Word 文档编辑（word-mcp）

让 AI 直接控制 Word，你可以说：

- "把文档里所有的'公司A'替换为'公司B'"
- "给第3段加一个批注"
- "把这篇文章的标题改成黑体 16 号"

---

## 安装 MCP

三个 MCP 的来源不同，安装方式也不一样：

### PowerPoint（ppt-mcp）

**仓库**: <https://github.com/ykuwai/ppt-mcp>

告诉 OpenCode "帮我安装 PowerPoint MCP" 即可自动下载，也可以去仓库查看最新版本和说明。

### Word（word-mcp-live）

**仓库**: <https://github.com/ykarapazar/word-mcp-live>

告诉 OpenCode "帮我安装 Word MCP，作者名字写张三" 即可自动下载。

### Excel（mcp-server-excel）

**仓库**: <https://github.com/sbroenne/mcp-server-excel>
**下载页**: <https://github.com/sbroenne/mcp-server-excel/releases>

Excel MCP 是 Windows 可执行文件，需要让 OpenCode 从 GitHub 下载。对它说：

> 帮我从 GitHub 下载 excel-mcp 并配置好

也可以自己去下载页手动下载最新版的 `mcp-excel.exe`，再告诉 OpenCode 文件位置。

### 快速开始

如果你是新手，直接把下面这段话发给 OpenCode 就行了：

> 帮我安装 ppt-mcp 和 word-mcp-live，其中 Word 的作者设为你的名字。
> 然后从 GitHub 下载 excel-mcp 的 exe 文件，帮我配置好。

OpenCode 会一步步引导你完成。

---

## 系统要求

- **操作系统**: Windows 10 或 11
- **Office**: Microsoft Office 2016 或更新版本（Excel、PowerPoint、Word 必须已安装）
- **网络**: 首次安装 MCP 时需要联网下载

---

## 常见问题

**问：提示找不到 uvx 怎么办？**

答：这是自动安装 MCP 时需要的工具。让 OpenCode 帮你安装即可，它会自动处理。

**问：Excel MCP 报错无法连接？**

答：确保 Excel 已安装，且没有正在打开模态对话框（如另存为窗口）。关闭 Excel 后重新尝试。

**问：Word MCP 怎么让批注和修订显示我的名字？**

答：在配置中修改 `MCP_AUTHOR` 和 `MCP_AUTHOR_INITIALS` 的值，分别填你的姓名和姓名缩写。
