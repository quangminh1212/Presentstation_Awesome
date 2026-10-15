# 🤖 DocMind AI

<p align="center">
  <img src="https://img.shields.io/badge/React-18.2+-61DAFB?logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-5.0+-3178C6?logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.4+-06B6D4?logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Vite-5.0+-646CFF?logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-FF6B6B?logo=openai&logoColor=white" alt="RAG">
  <img src="https://img.shields.io/badge/SSE-Server_Sent_Events-00C853?logo=serverless&logoColor=white" alt="SSE">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

<p align="center">
  <b>🚀 下一代 AI 智能办公助手</b> | <b>Next-Gen AI DocMind Assistant</b>
</p>

<p align="center">
  <sub>⚠️ 本项目为前端实现，需要配合后端服务使用</sub>
</p>

<p align="center">
  <a href="#核心亮点">核心亮点</a> •
  <a href="#功能特性">功能特性</a> •
  <a href="#ai技术栈">AI 技术栈</a> •
  <a href="#快速开始">快速开始</a> •
  <a href="#架构设计">架构设计</a>
</p>

---

## 🌟 核心亮点

### 🧠 企业级 RAG 知识库
基于 **Retrieval-Augmented Generation** 技术，实现：
- 📄 **多格式文档解析** - PDF、Word、Excel、PPT、Markdown、JSON、XML 等
- 🔍 **语义检索** - 向量化存储 + 相似度匹配，精准定位知识点
- ⚡ **实时向量化** - 文件上传后自动分块、嵌入、索引
- 🎯 **上下文增强** - 检索结果注入 LLM Prompt，提升回答准确性

### 🌊 流式对话体验
采用 **Server-Sent Events (SSE)** 技术：
- 💬 **实时流式响应** - 打字机效果，无需等待完整回复
- 🧩 **多模态交互** - 支持文本、文件、知识库混合对话
- 🔧 **工具调用可视化** - Agent 思考过程、工具调用实时展示
- 📊 **任务进度追踪** - 复杂任务分步骤展示执行进度

### 🤖 AI Agent 智能体
不仅仅只是聊天机器人，更是你的智能办公助手：
- 📝 **PPT 智能生成** - 一句话生成大纲，自动匹配模板
- 🎤 **演讲稿撰写** - 根据主题自动生成演讲内容
- 📚 **文档智能分析** - 总结、对比、提取关键信息
- 🎓 **面试训练模式** - AI 模拟面试，实时反馈提升

---

## ✨ 功能特性

### 🎯 AI 对话助手
- 支持多轮对话，上下文理解
- 知识库管理，RAG 检索增强
- 文件上传与智能解析（PDF、Word、Excel、PPT 等）
- 实时流式响应，打字机效果
- **Agent 模式** - 支持工具调用、任务分解

### 📊 智能 PPT 生成
- 一句话生成专业演示文稿
- 多种主题模板可选
- 自动大纲生成与编辑
- 在线预览与导出

### 🎤 演讲稿生成
- 根据主题自动生成演讲稿
- 智能优化与润色
- 支持多种演讲风格
- 与 PPT 内容联动

### 📚 知识库管理
- 支持多种文档格式上传
- **自动分块与向量化**（RAG 核心）
- 语义检索，精准定位
- 会话级文件管理
- 文件激活/停用控制

### 🌐 国际化支持
- 完整中英双语界面
- 一键语言切换
- 可扩展更多语言

---

## 🛠 技术栈

### 🤖 AI 核心技术
| 技术 | 说明 | 应用场景 |
|------|------|----------|
| **RAG** | Retrieval-Augmented Generation | 知识库问答、文档检索 |
| **SSE** | Server-Sent Events | 流式对话、实时进度 |
| **Vector DB** | 向量数据库 | 文档向量化存储 |
| **Embedding** | 文本嵌入 | 语义相似度计算 |
| **Agent** | AI 智能体 | 工具调用、任务分解 |

### 前端核心
- **React 18** - 现代化 UI 框架
- **TypeScript** - 类型安全的 JavaScript
- **Vite** - 极速构建工具
- **Tailwind CSS** - 原子化 CSS 框架

### UI 组件
- **Radix UI** - 无障碍 headless 组件
- **shadcn/ui** - 精美的 React 组件库
- **Framer Motion** - 流畅的动画效果
- **Lucide React** - 优雅的图标库

### 状态管理
- **React Context** - 全局状态管理
- **TanStack Query** - 服务端状态管理

### 其他工具
- **i18next** - 国际化方案
- **Axios** - HTTP 客户端
- **date-fns** - 日期处理

---

## 🚀 快速开始

### ⚠️ 前提条件

本项目为**纯前端实现**，需要配合后端服务使用。API 接口遵循 RESTful + SSE 规范。

### 环境要求

- Node.js >= 18.0.0
- npm >= 9.0.0 或 yarn >= 1.22.0
- 后端 API 服务（需自行实现或对接）

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/yourusername/smart-office-ai.git
cd smart-office-ai
```

2. **进入客户端目录并安装依赖**

```bash
cd client
npm install
# 或
yarn install
```

3. **配置环境变量**

```bash
cp .env.example .env
# 编辑 .env 文件，配置你的后端 API 地址
# VITE_API_BASE_URL=http://your-backend-api.com/smart-office
```

4. **启动开发服务器**

```bash
npm run dev
# 或
yarn dev
```

5. **打开浏览器访问**

```
http://localhost:5173
```

### 构建生产版本

```bash
npm run build
# 或
yarn build
```

构建后的文件将位于 `dist/` 目录。

---

## 🏗 架构设计

### RAG 流程架构

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  文件上传    │────▶│  文档解析    │────▶│  智能分块    │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
┌─────────────┐     ┌─────────────┐            ▼
│  语义检索    │◀────│  向量数据库  │◀────┌─────────────┐
└──────┬──────┘     └─────────────┘     │  Embedding  │
       │                                 └─────────────┘
       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Prompt构建  │────▶│   LLM推理   │────▶│  流式输出   │
└─────────────┘     └─────────────┘     └─────────────┘
```

### SSE 实时通信

```
Client                  Server
  │                        │
  │  POST /chat/stream     │
  │ ──────────────────────▶│
  │                        │
  │  ◀── SSE: SESSION_START│
  │  ◀── SSE: THINKING     │
  │  ◀── SSE: TOOL_CALL    │
  │  ◀── SSE: CONTENT      │
  │  ◀── SSE: DONE         │
```

---

## 📁 项目结构

```
client/
├── public/                 # 静态资源
├── src/
│   ├── components/
│   │   ├── agent/         # AI 助手组件
│   │   │   ├── ThinkingProcess.tsx    # 思考过程展示
│   │   │   ├── ToolCallCard.tsx       # 工具调用卡片
│   │   │   ├── TaskProgressPanel.tsx  # 任务进度面板
│   │   │   ├── KnowledgeBankPanel.tsx # 知识库面板
│   │   │   └── StreamingContent.tsx   # 流式内容
│   │   ├── common/        # 通用组件
│   │   ├── layout/        # 布局组件
│   │   └── ui/            # UI 基础组件
│   ├── contexts/
│   │   └── AgentContext.tsx   # Agent 状态管理
│   ├── hooks/             # 自定义 Hooks
│   ├── i18n/              # 国际化配置
│   ├── lib/               # 工具函数
│   ├── pages/
│   │   └── Agent.tsx      # AI 助手主页面
│   ├── services/
│   │   └── agentApi.ts    # API 服务（SSE、RAG）
│   └── types/
│       └── agent.ts       # TypeScript 类型
├── .env.example           # 环境变量示例
└── ...
```

---

## 🌍 环境变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `VITE_API_BASE_URL` | 后端 API 基础地址 | `http://localhost:8080/smart-office` |

> **注意**：本项目为前端实现，需要自行开发或对接后端服务。API 接口规范可参考 `src/services/agentApi.ts` 中的定义。

### 后端 API 接口概览

前端期望的后端接口包括：

- **认证相关**：登录、注册、密码重置
- **PPT 生成**：创建任务、查询进度、获取结果
- **演讲稿**：生成、编辑、预览
- **AI 对话**：SSE 流式对话、会话管理
- **RAG 知识库**：文件上传、向量化状态查询
- **用户管理**：设置、通知、订阅

具体接口定义请参考 `client/src/services/` 目录下的 API 服务文件。

---

## 📝 开发指南

### 代码规范

- 使用 TypeScript 严格模式
- 遵循 ESLint 和 Prettier 配置
- 组件使用 PascalCase 命名
- 工具函数使用 camelCase 命名

### 提交规范

```
feat: 新功能
fix: 修复问题
docs: 文档更新
style: 代码格式调整
refactor: 重构代码
test: 测试相关
chore: 构建/工具相关
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

---

## 📸 截图展示

> 截图将在后续版本补充

---

## 🗺 路线图

- [x] RAG 知识库系统
- [x] SSE 流式对话
- [x] AI Agent 工具调用
- [ ] 支持更多文档格式（Markdown、CSV 等）
- [ ] 团队协作功能
- [ ] 移动端适配优化
- [ ] 插件系统
- [ ] 更多语言支持

---

## 📄 许可证

本项目基于 [MIT](LICENSE) 许可证开源。

---

## 🙏 致谢

- [shadcn/ui](https://ui.shadcn.com/) - 精美的 UI 组件
- [Radix UI](https://www.radix-ui.com/) - 无障碍组件基础
- [Lucide](https://lucide.dev/) - 优雅的图标
- [LangChain](https://langchain.com/) - LLM 应用开发框架灵感

---

<p align="center">
  Made with ❤️ by DocMind AI Team
</p>
