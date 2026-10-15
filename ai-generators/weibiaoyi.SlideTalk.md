# SlideTalk - 幻灯片说客

> 将 PPT 自动转换为有声视频讲解的桌面客户端

![img.png](resources/img.png)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](package.json)
[![Electron](https://img.shields.io/badge/Electron-33-blue.svg)](https://www.electronjs.org/)
[![Vue](https://img.shields.io/badge/Vue-3.5-green.svg)](https://vuejs.org/)

🌐 **语言切换**: [English](README.en.md)

## 🌟 项目简介

SlideTalk 是一款功能强大的桌面应用，能够将 PowerPoint 演示文稿自动转换为有声视频讲解。通过集成 AI 语音合成和视频编辑功能，让您的演示文稿动起来！

## ✨ 核心功能

| 功能模块 | 描述 |
|---------|------|
| **PPT 导入解析** | 支持 .ppt/.pptx/.pdf 文件，自动提取每页内容和备注，生成高清缩略图 |
| **文案编辑** | 每页独立文案编辑，支持 AI 智能改写、扩写、精简 |
| **语音合成** | 多音色选择，语速/语调/音量可调，支持声音克隆（参考音频） |
| **字幕配置** | 每页字幕内容编辑 + 全局样式设置 |
| **背景音乐** | 内置音乐库 + BGM 全局配置（音量/淡入淡出） |
| **视频导出** | 支持多种格式、分辨率、帧率、画质设置，实时进度展示 |
| **主题切换** | 深色/浅色/跟随系统三种主题，即时生效 |
| **项目管理** | 支持搜索、排序、重命名、删除项目 |

## 🛠️ 技术栈

### 前端
| 技术 | 版本 | 用途 |
|------|------|------|
| Vue | 3.5+ | 前端框架 |
| TypeScript | 5.7+ | 类型安全 |
| Pinia | 2.3+ | 状态管理 |
| Vue Router | 4.5+ | 路由管理 |
| Lucide Vue | 0.469+ | 图标库 |
| Vite | 6.0+ | 构建工具 |

### 桌面
| 技术 | 版本 | 用途 |
|------|------|------|
| Electron | 33+ | 桌面应用框架 |
| electron-builder | 25+ | 打包工具 |

### 后端
| 技术 | 用途 |
|------|------|
| Python | 后端语言 |
| FastAPI | API 框架 |
| PyMuPDF | PDF 解析与图片转换 |
| python-pptx | PPTX 文件解析 |
| ffmpeg | 视频合成与音频混音 |
| comtypes | Windows COM 自动化（PowerPoint/WPS） |

## 📁 项目结构

```
SlideTalk/
├── electron/                    # Electron 主进程
│   ├── main.ts                  # 主进程入口（窗口管理、IPC）
│   ├── preload.ts               # 预加载脚本（contextBridge）
│   ├── shared/
│   │   └── ipc-types.ts         # IPC 类型定义
│   └── services/
│       ├── index.ts             # 服务注册
│       ├── pythonService.ts     # Python 后端进程管理
│       ├── mock/                # Mock 服务实现（开发测试）
│       │   ├── pptParser.ts     # Mock PPT 解析
│       │   ├── ttsService.ts    # Mock 语音合成
│       │   ├── llmService.ts    # Mock AI 改写
│       │   ├── videoExporter.ts # Mock 视频导出
│       │   └── seedData.ts      # 示例项目数据
│       └── real/
│           └── backendClient.ts # 真实后端 API 调用
├── ppt-video-backend/           # Python 后端服务
│   ├── app.py                   # FastAPI 入口
│   ├── core.py                  # 核心业务逻辑
│   └── requirements.txt         # Python 依赖
├── src/                         # 前端渲染层
│   ├── components/
│   │   ├── common/              # 通用组件（Button/Input/Modal 等）
│   │   ├── editor/              # 编辑器组件
│   │   ├── export/              # 导出相关组件
│   │   ├── home/                # 首页组件
│   │   └── layout/              # 布局组件（Titlebar/Sidebar）
│   ├── composables/             # 组合式函数（useTheme/useToast）
│   ├── router/                  # 路由配置
│   ├── stores/                  # Pinia 状态管理
│   ├── services/                # 渲染层服务抽象
│   ├── styles/                  # 全局样式与主题
│   ├── types/                   # TypeScript 类型定义
│   ├── views/                   # 页面视图
│   ├── App.vue                  # 根组件
│   └── main.ts                  # 应用入口
├── public/                      # 静态资源
│   └── voices/                  # 预置音色示例
├── resources/                   # 打包资源（图标）
├── dist/                        # 前端构建产物（自动生成）
├── dist-electron/               # Electron 构建产物（自动生成）
├── release/                     # 打包输出目录（自动生成）
├── package.json                 # 项目依赖与脚本
├── vite.config.ts               # Vite 配置
├── tsconfig.json                # TypeScript 配置
└── README.md                    # 项目说明文档
```

## 🚀 快速开始

### 环境要求

- **Node.js**: >= 20.x
- **Python**: >= 3.10
- **ffmpeg**: 需安装并添加到系统 PATH
- **PPT 转 PDF 引擎**（任选其一）:
  - Microsoft PowerPoint（推荐）
  - WPS Office
  - LibreOffice

### 安装依赖

```bash
# 安装前端依赖
npm install

# 安装后端依赖（进入后端目录）
cd ppt-video-backend
pip install -r requirements.txt
cd ..
```

> **Electron 下载加速**（国内网络）：
> ```bash
> # Windows (PowerShell)
> $env:ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/"
> npm install
> ```

### 开发模式

```bash
npm run dev
```

启动 Vite 开发服务器 + Electron 主进程，支持热更新。

### 类型检查

```bash
npm run typecheck
```

### 构建项目

```bash
npm run build
```

### 打包 Windows 安装包

```bash
npm run build:win
```

产物输出到 `release/` 目录：
- `SlideTalk-Setup-1.0.0.exe` - NSIS 安装包
- `SlideTalk-1.0.0-portable.exe` - 免安装便携版

## 🔌 后端服务配置

### 启动 Python 后端

```bash
cd ppt-video-backend
python app.py
```

默认端口：`17878`

### 健康检查

```bash
curl http://localhost:17878/health
```

返回示例：
```json
{
  "status": "ok",
  "version": "1.0.0",
  "ppt_engines": [
    {"name": "powerpoint", "display": "Microsoft PowerPoint", "available": true, "path": null},
    {"name": "wps", "display": "WPS Office", "available": false, "path": null},
    {"name": "libreoffice", "display": "LibreOffice", "available": true, "path": "C:\\Program Files\\LibreOffice\\program\\soffice.exe"}
  ],
  "ppt_engines_available": ["powerpoint", "libreoffice"],
  "soffice": "C:\\Program Files\\LibreOffice\\program\\soffice.exe",
  "ffmpeg": "ffmpeg"
}
```

### 外部服务配置

#### TTS 服务（OmniVoice）

1. 安装 OmniVoice 服务（参考 [OmniVoice 文档](https://github.com/OmniVoice/OmniVoice)）
2. 启动 TTS 服务（默认端口 8002）
3. 在应用设置中配置 TTS 服务地址

#### LLM 服务

在应用设置中配置：
- API Key
- API Base URL（支持 OpenAI 兼容接口）
- Model 名称

## 📡 API 接口

### 1. PPT 解析

```
POST /api/parse-ppt
Content-Type: application/json

{
  "file_path": "C:/path/to/presentation.pptx",
  "thumb_dir": "C:/path/to/thumbs"
}
```

### 2. 语音合成

```
POST /api/tts-single
Content-Type: application/json

{
  "text": "这是一段测试文本",
  "tts_endpoint": "http://localhost:8002",
  "ref_audio_path": "C:/path/to/reference.wav",
  "language": "zh"
}
```

### 3. AI 改写

```
POST /api/llm-rewrite
Content-Type: application/json

{
  "text": "原始文本",
  "mode": "rewrite",
  "api_key": "your-api-key",
  "api_base": "https://api.example.com/v1",
  "model": "gpt-4"
}
```

### 4. 视频导出

```
POST /api/export-video
Content-Type: application/json

{
  "ppt_path": "C:/path/to/presentation.pptx",
  "narrations": ["第一页旁白", "第二页旁白", "..."],
  "output_path": "C:/path/to/output.mp4",
  "tts_endpoint": "http://localhost:8002",
  "resolution": "1920:1080",
  "bgm_path": "C:/path/to/bgm.mp3",
  "bgm_volume": 0.10
}
```

### 5. 进度查询（WebSocket）

```
GET /ws/progress/{task_id}
```

## 🎨 主题系统

应用内置三套主题：

| 主题 | 描述 |
|------|------|
| **深色** | 剪映青蓝深色风格（默认） |
| **浅色** | 清爽浅色风格 |
| **跟随系统** | 自动适配操作系统主题 |

主题切换采用双写方案（localStorage + IPC 持久化），HTML 内联脚本防闪烁。

## 📝 Mock 模式说明

开发环境默认使用 Mock 模式，所有业务接口均为模拟实现：

| 接口 | Mock 行为 |
|------|-----------|
| PPT 解析 | 接受任意文件，模拟 2-3 秒解析，生成纯色占位缩略图 |
| 语音合成 | 返回模拟音频 URL |
| AI 改写 | 模拟 1-2 秒延迟，返回原文 + 模式后缀 |
| 视频导出 | 4 阶段进度模拟，约 5 秒完成 |

**切换到真实后端**：修改 `electron/services/index.ts` 中的服务注册逻辑。

## 🐛 常见问题

### Q: `npm install` 时 Electron 下载失败？

A: 设置 Electron 镜像：
```bash
$env:ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/"
npm install
```

### Q: PPT 解析失败？

A: 检查是否安装了 PPT 转 PDF 引擎（PowerPoint/WPS/LibreOffice），或尝试将 PPT 另存为 PDF 后直接导入。

### Q: 视频导出失败？

A: 检查：
1. ffmpeg 是否安装并添加到 PATH
2. 输出目录是否有写权限
3. TTS 服务是否正常运行

### Q: 打包后启动白屏？

A: 检查 `package.json` 的 `build.directories.output` 是否为 `release`（不能是 `dist`）。

### Q: 主题切换后样式不生效？

A: 组件内样式必须使用 CSS 变量（`var(--bg-1)` 等），不能硬编码颜色。

## 🤝 贡献指南

欢迎贡献代码！请遵循以下规范：

1. Fork 项目
2. 创建功能分支（`feature/xxx`）
3. 提交代码（遵循 Conventional Commits）
4. 创建 Pull Request

## 讨论群

![my.jpg](resources/my.jpg)

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [Vue.js](https://vuejs.org/) - 前端框架
- [Electron](https://www.electronjs.org/) - 桌面应用框架
- [FastAPI](https://fastapi.tiangolo.com/) - API 框架
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF 处理
- [OmniVoice](https://github.com/OmniVoice/OmniVoice) - 语音合成
- [Lucide](https://lucide.com/) - 图标库

---

**SlideTalk** - 让您的幻灯片开口说话 🎤
