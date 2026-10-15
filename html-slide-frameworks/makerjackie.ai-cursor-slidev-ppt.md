# 用 Cursor + Slidev 制作精美演示文稿

这个仓库提供了一套简单有效的流程，让你能够利用 AI 和 Slidev 快速创建专业级演示文稿。通过 Cursor 的 AI 功能和 Slidev 的强大特性，你可以在几分钟内完成原本需要数小时的 PPT 制作过程。

效果演示网站： https://danyun.vercel.app/1

## 快速开始

```bash
# 安装依赖
pnpm install

# 启动演示文稿
pnpm dev

# 构建生产版本
pnpm build

# 部署到线上（使用 Vercel 或 Netlify）
pnpm deploy
```

## 完整制作流程

### 第一步：准备内容

1. 准备你的演示文稿内容（可以是简单的 Markdown 文件）
2. 收集需要用到的图片，放在 `public` 文件夹下
   - 品牌 Logo 放在根目录
   - 其他图片可以按主题分类放在子文件夹中（如 `images/events/`）

### 第二步：创建 Slidev 项目

```bash
# 创建新的 Slidev 项目
pnpm create slidev

# 按照提示完成设置
```

### 第三步：使用 Cursor 编辑器

1. 使用 Cursor 打开项目文件夹
2. 选择 `slides.md` 文件
3. 删除 sliceds.md 里头的默认内容（PPT 内容会放在这个文档中）

### 第四步：利用 AI 生成演示文稿

1. 创建一个 `info.md` 文件，包含活动/演示文稿的基本信息
2. 使用 `prompt.md` 中的模板，指导 AI 生成内容
3. 在 Cursor 中，使用 AI 命令生成演示文稿内容，例如：
   ```
   /ai 请按照 prompt.md 中的要求，使用 info.md 中的信息为我创建一个 Slidev 演示文稿
   ```

### 第五步：优化演示文稿

1. 预览生成的演示文稿 (`pnpm dev`)
2. 根据需要调整布局、颜色、文字大小等
3. 添加过渡动画和交互元素
4. 使用 Slidev 的高级功能如代码高亮、Markdown 扩展等

### 第六步：部署演示文稿

> 前提是先注册 vercel 或者 Netlify

1. 使用 Vercel 或 Netlify 一键部署
   ```bash
   # Vercel 部署
   pnpm dlx vercel
   
   # 或 Netlify 部署
   pnpm dlx netlify deploy
   ```
运行示例:
![](./image.png)


## 演示案例

本仓库包含以下示例：

1. **社区活动宣传**：适合技术社区活动宣传
2. **产品发布会**：产品特性与价值展示
3. **技术分享**：代码展示与技术原理讲解
4. **企业培训**：结构化知识传递

## 扩展功能

- **定制主题**：`npm init slidev theme`
- **导出为 PDF**：`pnpm export`
- **录制演示**：`pnpm record`
- **添加演讲者注释**：使用 `<!-- -->` 添加不显示在幻灯片上的注释

## 学习资源

- [Slidev 官方文档](https://sli.dev/)
- [Markdown 基础语法](https://www.markdownguide.org/basic-syntax/)
- [Cursor 编辑器](https://cursor.sh/)
