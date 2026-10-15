# Qurit PPT - AI驱动的演示文稿生成平台

## 项目概述

Qurit PPT 是一个基于人工智能的演示文稿生成平台，旨在帮助用户快速创建专业、美观的PPT演示文稿。通过先进的AI技术，用户只需提供简单的输入，系统就能自动生成完整的演示文稿。

## 核心功能

- 🤖 **AI智能生成**：基于用户输入自动生成PPT内容和结构
- 🎨 **多样化模板**：提供丰富的专业模板库
- ✏️ **在线编辑器**：强大的在线编辑功能，支持实时预览
- 📤 **多格式导出**：支持PPT、PDF等多种格式导出
- 👥 **协作功能**：支持团队协作和分享
- 💳 **灵活付费**：多种付费方案满足不同需求

## 技术架构

### 前端
- **框架**：Next.js 14 (React 18)
- **样式**：Tailwind CSS
- **状态管理**：Zustand
- **UI组件**：Radix UI + Shadcn/ui
- **图标**：Lucide React
- **测试**：Jest + React Testing Library

### 后端
- **框架**：FastAPI (Python)
- **数据库**：SQLite (开发) / PostgreSQL (生产)
- **ORM**：SQLAlchemy
- **认证**：JWT
- **任务队列**：Celery + Redis
- **AI集成**：OpenAI API

### 开发工具
- **代码规范**：ESLint + Prettier
- **Git钩子**：Husky + lint-staged
- **类型检查**：TypeScript
- **API文档**：Swagger/OpenAPI

## 项目结构

```
Qurit ppt/
├── frontend/                 # 前端应用
│   ├── src/
│   │   ├── app/             # Next.js App Router
│   │   ├── components/      # React组件
│   │   ├── lib/            # 工具库
│   │   ├── hooks/          # 自定义Hooks
│   │   ├── store/          # 状态管理
│   │   ├── types/          # TypeScript类型定义
│   │   └── utils/          # 工具函数
│   ├── public/             # 静态资源
│   └── package.json
├── backend/                  # 后端API
│   ├── app/
│   │   ├── api/            # API路由
│   │   ├── core/           # 核心配置
│   │   ├── models/         # 数据模型
│   │   ├── schemas/        # Pydantic模式
│   │   └── services/       # 业务逻辑
│   ├── tests/              # 测试文件
│   └── requirements.txt
├── design/                   # 设计原型
│   ├── prototypes/         # HTML原型
│   └── specs/              # 设计规范
├── docs/                     # 项目文档
│   ├── PRD.md              # 产品需求文档
│   ├── User_Story_Map.md   # 用户故事地图
│   └── Roadmap.md          # 产品路线图
└── README.md
```

## 快速开始

### 环境要求

- Node.js 18+
- Python 3.8+
- Redis (用于任务队列)
- Git

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd "Qurit ppt"
   ```

2. **安装前端依赖**
   ```bash
   cd frontend
   npm install
   ```

3. **安装后端依赖**
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

4. **环境配置**
   ```bash
   # 复制环境变量文件
   cp .env.example .env
   # 编辑 .env 文件，配置必要的环境变量
   ```

5. **数据库初始化**
   ```bash
   python init_database.py
   ```

6. **启动服务**
   
   启动后端服务：
   ```bash
   cd backend
   python main.py
   ```
   
   启动前端服务：
   ```bash
   cd frontend
   npm run dev
   ```

7. **访问应用**
   - 前端：http://localhost:3000
   - 后端API：http://localhost:8000
   - API文档：http://localhost:8000/docs

## 开发指南

### 代码规范

项目使用统一的代码规范：
- ESLint + Prettier 用于代码格式化
- Husky + lint-staged 用于Git提交前检查
- EditorConfig 用于编辑器配置统一

### 提交规范

使用 Conventional Commits 规范：
```
type(scope): description

[optional body]

[optional footer]
```

类型包括：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 测试

**前端测试**
```bash
cd frontend
npm test
npm run test:coverage
```

**后端测试**
```bash
cd backend
pytest
pytest --cov=app
```

### 构建部署

**前端构建**
```bash
cd frontend
npm run build
npm start
```

**后端部署**
```bash
cd backend
# 使用 uvicorn 或其他 ASGI 服务器
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API文档

后端API遵循RESTful设计原则，主要端点包括：

- `POST /api/auth/login` - 用户登录
- `POST /api/auth/register` - 用户注册
- `GET /api/projects` - 获取项目列表
- `POST /api/projects` - 创建新项目
- `POST /api/projects/{id}/generate` - 生成PPT
- `GET /api/projects/{id}/download` - 下载PPT

详细API文档请访问：http://localhost:8000/docs

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系我们

- 项目主页：[GitHub Repository]
- 问题反馈：[GitHub Issues]
- 邮箱：contact@quritppt.com

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

---

**注意**：本项目仍在积极开发中，功能和API可能会发生变化。建议在生产环境使用前进行充分测试。