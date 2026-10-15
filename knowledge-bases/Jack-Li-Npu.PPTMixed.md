# NotebookLM PDF 修复工具

一个基于 AI 的智能工具，用于去除 NotebookLM 生成的 PDF 演示文稿中的水印，并将其超清重绘至 2K/4K 分辨率。

## ✨ 核心功能

- 🎯 **智能去水印**: 自动识别并移除 NotebookLM 右下角的固定水印
- 🔍 **超清重绘**: 基于 AI 模型将模糊文档重绘至 2K/4K 分辨率
- 📝 **文字精准还原**: 修复文字边缘锯齿，保持原有排版布局
- 式导出**: 支📊 **多格持导出为 PDF 和 PPTX 格式

## 🛠️ 技术栈

- **前端框架**: Next.js 16 (App Router) + TypeScript + Tailwind CSS
- **PDF 处理**: PDF.js (渲染) + jsPDF (导出)
- **演示文稿**: PptxGenJS
- **AI 集成**: 
  - IOPaint (Lama 模型) - 水印去除
  - Google Gemini 3 Pro Image Preview - 超清重绘 (2K/4K)

## 📋 前置要求

### 1. 安装 IOPaint (本地 AI 服务)

```bash
# 安装 IOPaint
pip install iopaint

# 启动服务 (CPU 模式)
iopaint start --model=lama --device=cpu --port=8080

# 如果有 NVIDIA 显卡，推荐使用 GPU 加速
iopaint start --model=lama --device=cuda --port=8080
```

### 2. Node.js 环境

确保已安装 Node.js 18+ 版本。

## 🚀 快速开始

### 1. 安装依赖

```bash
cd notebooklm-fixer
npm install
```

### 2. 配置环境变量 (推荐)

**强烈推荐配置 Gemini API** 以启用超清重绘功能：

```bash
cp .env.local.example .env.local
# 编辑 .env.local 文件，填入你的 Gemini API Key
```

详细配置步骤请参考 [GEMINI_SETUP.md](./GEMINI_SETUP.md)

> 💡 **提示**: 如果不配置 Gemini API，系统仍可正常运行，但会跳过超清重绘步骤，仅执行水印去除。

### 3. 启动开发服务器

```bash
npm run dev
```

打开浏览器访问 [http://localhost:3001](http://localhost:3001)

## 📖 使用指南

### 基本流程

1**: 点击 ". **上传 PDFImport PDF" 按钮，选择 NotebookLM 生成的 PDF 文件
2. **选择分辨率**: 在界面上选择 2K (标准) 或 4K (极致) 分辨率
3. **开始修复**: 点击 "Start Restoration" 按钮，等待处理完成
4. **导出结果**: 
   - 点击 "Export PDF" 导出为 PDF 格式
   - 点击 "Export PPTX" 导出为 PowerPoint 格式

### 处理流程说明

```
PDF 上传 → 页面渲染 → 生成水印遮罩 → IOPaint 去水印 → AI 超清重绘 → 导出文件
```

## 🔧 配置说明

### IOPaint 服务配置

默认配置假设 IOPaint 运行在 `localhost:8080`。如需修改，请编辑：

- `next.config.ts` 中的 `rewrites` 配置
- `src/lib/iopaint-client.ts` 中的 `IOPAIN_API_BASE`

### 水印区域调整

如果 NotebookLM 水印位置发生变化，可在 `src/lib/mask-generator.ts` 中调整遮罩坐标：

```typescript
const maskW = width * 0.15;  // 水印宽度占比
const maskH = height * 0.08; // 水印高度占比
const x = width - maskW - (width * 0.01);  // 右边距
const y = height - maskH - (height * 0.02); // 下边距
```

## 📁 项目结构

```
notebooklm-fixer/
├── src/
│   ├── app/
│   │   └── page.tsx              # 主页面
│   ├onents/
│── comp   │   └── RestorationApp.tsx   # 核心 UI 组件
│   └── lib/
│       ├── pdf-utils.ts          # PDF 渲染工具
│       ├── iopaint-client.ts     # IOPaint API 客户端
│       ├── nano-banana-client.ts # Gemini API 客户端
│       ├── mask-generator.ts     # 水印遮罩生成器
│       └── exporter.ts           # PDF/PPTX 导出工具
├── next.config.ts                # Next.js 配置
└── package.json
```

## ⚠️ 注意事项

1. **IOPaint 必须运行**: 确保在使用前启动了本地 IOPaint 服务
2. **Gemini API 配置**: 
   - 已集成真实的 Gemini 3 Pro Image Preview API
   - 需要有效的 API Key 才能使用超清重绘功能
   - 未配置时会自动跳过重绘步骤
3. **浏览器兼容性**: 推荐使用 Chrome/Edge 最新版本
4. **文件大小限制**: 建议单个 PDF 不超过 50 页，以避免浏览器内存溢出
5. **API 费用**: Gemini API 可能产生费用，请查看 [定价说明](https://ai.google.dev/pricing)

## 🐛 常见问题

### Q: 构建时出现 Turbopack 错误？
A: 已在 `next.config.ts` 中添加 `turbopack: {}` 配置，使用 `npm run build` 即可。

### Q: IOPaint 连接失败？
A: 检查 IOPaint 是否正常运行在 8080 端口，可访问 `http://localhost:8080/docs` 验证。

### Q: 导出的 PDF 模糊？
A: 确保在 `pdf-utils.ts` 中的 `scale` 参数设置为 2.0 或更高。同时检查是否正确配置了 Gemini API Key。

### Q: Gemini API 调用失败？
A: 
1. 检查 `.env.local` 文件中的 API Key 是否正确
2. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey) 验证 Key 状态
3. 查看浏览器控制台的详细错误信息
4. 参考 [GEMINI_SETUP.md](./GEMINI_SETUP.md) 排查问题

## 📝 开发计划

- [x] 集成真实的 Gemini 3 Pro Image Preview API
- [x] 支持 2K/4K 分辨率超清重绘
- [ ] 支持批量处理多个 PDF 文件
- [ ] 集成 Vercel KV 实现任务队列
- [ ] 添加处理历史记录功能
- [ ] 优化大文件处理性能
- [ ] 支持自定义水印区域选择

## 📄 许可证

MIT License

## 🙏 致谢

- [IOPaint](https://github.com/Sanster/IOPaint) - 强大的图像修复工具
- [PDF.js](https://mozilla.github.io/pdf.js/) - Mozilla 的 PDF 渲染引擎
- [Next.js](https://nextjs.org/) - React 全栈框架
