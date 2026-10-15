# Office MCP Server

一个功能强大的 MCP 服务器，支持多种 Office 文档格式的读取、生成、编辑，以及邮件发送功能。

## 功能特性

| 格式 | 读取 | 生成 | 编辑 |
|------|:----:|:----:|:----:|
| DOCX (Word) | ✅ | ✅ | ✅ |
| PPTX (PowerPoint) | ✅ | ✅ | 🚧 |
| XLSX (Excel) | ✅ | ✅ | 🚧 |
| PDF | ✅ | ✅ | - |
| HTML | - | ✅ | - |

## 安装

```bash
# 克隆仓库
git clone https://github.com/searaylee/office-mcp-server.git
cd office-mcp-server
bun install
```

## 配置

### Claude Code 配置

创建 `.mcp.json`:

```json
{
  "mcpServers": {
    "office-tools": {
      "command": "bun",
      "args": ["run", "/path/to/office-mcp-server/src/index.ts"],
      "env": {
        "SMTP_HOST": "smtp.163.com",
        "SMTP_PORT": "465",
        "SMTP_USER": "your-email@163.com",
        "SMTP_PASS": "your-auth-code"
      }
    }
  }
}
```

### Claude Desktop 配置

编辑 `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "office-tools": {
      "command": "npx",
      "args": ["-y", "office-mcp-server"],
      "env": {
        "SMTP_HOST": "smtp.163.com",
        "SMTP_PORT": "465",
        "SMTP_USER": "your-email@163.com",
        "SMTP_PASS": "your-auth-code"
      }
    }
  }
}
```

## 工具列表

| 工具 | 功能 |
|------|------|
| `read_docx` | 读取 Word 文档 |
| `create_docx` | 创建 Word 文档 |
| `read_pptx` | 读取 PowerPoint |
| `create_pptx` | 创建 PowerPoint（支持模板） |
| `read_excel` | 读取 Excel |
| `create_excel` | 创建 Excel |
| `read_pdf` | 读取 PDF |
| `create_pdf` | 创建 PDF |
| `create_html` | 创建 HTML |
| `send_email` | 发送邮件（支持附件） |
| `learn_ppt_template` | 学习 PPT 模板 |
| `learn_docx_template` | 学习 Word 模板 |
| `list_templates` | 列出已学习模板 |

## 使用示例

```javascript
// 创建 PPT（使用模板）
{
  "tool": "create_pptx",
  "args": {
    "output_path": "report.pptx",
    "slides": [
      { "title": "季度汇报", "layout": "title" },
      { "title": "项目进展", "content": ["已完成 80%", "进行中 20%"] }
    ],
    "template": "amap-light"
  }
}

// 发送邮件
{
  "tool": "send_email",
  "args": {
    "to": "colleague@company.com",
    "subject": "文档已生成",
    "body": "<h1>通知</h1><p>请查看附件</p>",
    "attachments": ["report.pptx"]
  }
}
```

## 已集成模板

- **amap-light** - 高德地图浅色版 PPT 模板
- **amap-dark** - 高德地图深色版 PPT 模板

## 技术栈

Bun + MCP SDK + docx + pptxgenjs + exceljs + pdfkit + nodemailer

## 许可证

MIT License - Searay Lee