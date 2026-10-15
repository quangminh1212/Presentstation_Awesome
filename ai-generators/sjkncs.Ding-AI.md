# Ding-AI

**Ding-AI** 是一个强大的本地化 AI PPT 生成工具。以"项目文件夹"为单位管理内容，利用 AI 自动生成大纲、风格、每页内容，并调用图像生成接口创建精美的 16:9 PPT 图片；最终可导出 **PDF / PPTX（图片页）**。

**Ding-AI** is a powerful local AI-powered PPT generation tool. It manages content on a per-project-folder basis, leveraging AI to automatically generate outlines, styles, and per-slide content, while calling image generation APIs to create stunning 16:9 PPT slides. The final output can be exported as **PDF / PPTX (image pages)**.

<img src="main.png" width="400" height="300" alt="Screenshot 1">            <img src="main2.png" width="400" height="300" alt="Screenshot 2">

---

## 致谢 / Acknowledgments

本项目借鉴了 [兴河PPT](https://github.com/xinghe-lu/xinghe-ppt) 项目的优秀设计与实现思路，并在此基础上进行了优化与改进。在此向兴河PPT的作者及所有贡献者表示衷心的感谢！

This project is inspired by and built upon the excellent [兴河PPT (XingHe PPT)](https://github.com/xinghe-lu/xinghe-ppt) project. We have optimized and improved upon the original design. Sincere thanks to the authors and all contributors of XingHe PPT for their outstanding work!

---

## 重要 / Important

- **Chat API**：需要用到 OpenAI 范式接口的对话模型，自行选择即可。
  - Requires a chat model compatible with the OpenAI API format. Choose any provider you prefer.
- **Image API**：需要用到生图接口 API，目前采用的是 `https://api.vectorengine.ai/`。使用请注册并获取令牌。
  - Requires an image generation API. Currently uses `https://api.vectorengine.ai/`. Register and obtain an access token to use.
- **下载 / Download**：我提前打包了 Windows 和 macOS 的版本，可以前往 Releases 直接下载。
  - Pre-built binaries for Windows and macOS are available in the [Releases](https://github.com/sjkncs/Ding-AI/releases) section.

---

## 功能 / Features

- **多项目 / Multi-project**：创建/打开本地项目文件夹（可搬移/备份） — Create/open local project folders (portable & backupable)
- **AI 生成 / AI Generation**：大纲（章节/页标题/概要）、主题风格、单页内容（要点/讲稿/配图描述） — Outlines, theme styles, per-slide content (key points, speaker notes, image descriptions)
- **生图与版本 / Image Generation & Versioning**：按页生成图片，支持编辑提示词、重新生成、版本回退 — Generate images per slide, edit prompts, regenerate, and rollback versions
- **导出 / Export**：PDF / PPTX（图片铺满页面；PPTX 会写入 speaker notes） — PDF / PPTX (full-page images; PPTX includes speaker notes)

---

## 运行环境 / Requirements

- Node.js >= 20.19 (required by Vite 7)
- pnpm (this repo uses pnpm workspace)

---

## 开发 / Development（Web 模式 / Web Mode）

```bash
pnpm install
pnpm dev
```

- Web (Vite): `http://127.0.0.1:5173`
- Server (Fastify): `http://127.0.0.1:8787`

## 开发 / Development（桌面端 / Electron）

```bash
pnpm install
pnpm dev:electron
```

---

## 构建与运行 / Build & Run（生产 / Production: Web + Server）

```bash
pnpm build
NODE_ENV=production pnpm start
```

打开 / Open: `http://127.0.0.1:8787`

> 如果你想显式指定 Web 静态资源目录，可设置 / To specify the web static assets directory:
> `DINGAI_WEB_DIST_DIR=/abs/path/to/apps/web/dist`

---

## 打包桌面端 / Build Electron Desktop App

```bash
pnpm build:electron
pnpm dist:electron
```

- 安装包输出目录 / Installer output: `apps/electron/release`
- 主要构建产物 / Build artifacts:
  - Web: `apps/web/dist`
  - Server: `apps/server/dist`
  - Electron: `apps/electron/dist`

本地预览（生产形态） / Local preview (production mode):

```bash
pnpm start:electron
```

---

## 配置 / Configuration（API Key / 模型 / Model / 生图 / Image）

首次运行后，在界面「设置」中填写：
After first run, configure in the Settings panel:

- **OpenAI**: `baseURL` / `model` / `apiKey`
- **生图接口 / Image API**: `baseURL` / `apiKey` (authenticated via `Authorization: Bearer <token>`)
- **可选 / Optional**: HTTP 代理 / proxy (applies to both OpenAI and image requests)

配置会落到本机，不写入项目目录。
Configuration is stored locally and not written to the project directory.

---

## 本地数据位置 / Local Data Paths

- 默认项目目录 / Default project directory: `~/Documents/Ding-AI Projects`
  - 可通过 / Override with: `DINGAI_PROJECTS_DIR`
- 全局配置文件 / Global config file: `<configDir>/config.json`
  - macOS: `~/Library/Application Support/Ding-AI/config.json`
  - Windows: `%APPDATA%\Ding-AI\config.json`
  - Linux: `~/.config/Ding-AI/config.json`
  - 可通过 / Override with: `DINGAI_CONFIG_DIR`

项目目录结构（示例） / Project directory structure (example):

```text
<project>/
  project.json
  aippt.sqlite
  images/
  exports/
  cache/        # 可选 / Optional: image cache
```

---

## License

MIT
