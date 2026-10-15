# 超星学习通 PDF/PPT 课件下载助手

自动嗅探并提取超星学习通页面中的 PDF / PPT / PPTX 课件下载链接，提供悬浮控制面板进行单个或批量下载。

## 安装

1. 安装 [Userscripts](https://apps.apple.com/app/userscripts/id1463298887)（Safari）或 Tampermonkey（Chrome/Edge）
2. 点击 [安装脚本](https://github.com/canvas-fr/chaoxing-course-downloader/raw/main/%E9%80%9A%E7%94%A8%E8%B6%85%E6%98%9F%E5%AD%A6%E4%B9%A0%E9%80%9A%20PDF%20%E8%AF%BE%E4%BB%B6%E8%87%AA%E5%8A%A8%E5%97%85%E6%8E%A2%E4%B8%8E%E4%B8%8B%E8%BD%BD%E5%8A%A9%E6%89%8B.user.js)

## 支持网站

- `*.chaoxing.com`
- `*.edu.cn`
- `*.nbdlib.cn`
- `*.hnsyu.net`
- `*.gdhkmooc.com`

## 功能

- 🔍 自动嗅探页面中的 PDF / PPT / PPTX 课件链接（包括 XHR / fetch 拦截和静态扫描）
- 📋 悬浮控制面板，支持拖动，显示已发现的课件列表
- ⬇️ 单个「拉取下载」：将文件拉取为本地 Blob 后存盘，绕过浏览器跨域限制
- 📦 「全部下载」批量触发所有课件下载
- 🏷️ 自动使用章节标题作为文件名

## 修改说明（v1.5）

在 [风雨梦呓原版](https://greasyfork.org/zh-CN/scripts/570126) 基础上的改动：

- 修复 Safari 下 PPTX 文件被错误识别为 PDF 的问题（MIME 类型与扩展名修正）
- 修复中文文件名在 Safari 下导致文件存为 `.com` 的 bug（白名单字符过滤策略）
- 修复文件名包含 `\xa0` 等不可见字符引发的崩溃

## 致谢

本脚本基于 [风雨梦呓](https://greasyfork.org/zh-CN/scripts/570126) 的原版修改，感谢原作者的工作。

## License

MIT
