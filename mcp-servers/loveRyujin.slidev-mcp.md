# Slidev MCP Server

一个功能完整的 Slidev MCP (Model Context Protocol) 服务器，支持通过 Cursor 等 AI 工具协同制作精美的 PPT。

## 功能特性

### 项目管理
- `slidev_init_project` - 初始化新的 Slidev 项目
- `slidev_get_project_info` - 获取项目信息

### 幻灯片操作
- `slidev_read_slides` - 读取和解析幻灯片
- `slidev_create_slide` - 创建新幻灯片
- `slidev_update_slide` - 更新幻灯片
- `slidev_delete_slide` - 删除幻灯片
- `slidev_duplicate_slide` - 复制幻灯片
- `slidev_reorder_slides` - 重新排序幻灯片
- `slidev_batch_update` - 批量更新幻灯片

### 主题和样式
- `slidev_list_themes` - 列出可用主题
- `slidev_apply_theme` - 应用主题
- `slidev_set_layout` - 设置幻灯片布局
- `slidev_update_frontmatter` - 更新全局配置

### 导出功能
- `slidev_export_pdf` - 导出为 PDF
- `slidev_export_pptx` - 导出为 PPTX
- `slidev_start_dev_server` - 启动开发服务器

## 安装

```bash
go build -o slidev-mcp .
```

## 配置 Cursor

在 Cursor 的 MCP 配置文件中添加：

```json
{
  "mcpServers": {
    "slidev": {
      "command": "/path/to/slidev-mcp",
      "args": []
    }
  }
}
```

## 使用示例

### 初始化项目
```json
{
  "tool": "slidev_init_project",
  "arguments": {
    "project_path": "./my-presentation"
  }
}
```

### 创建幻灯片
```json
{
  "tool": "slidev_create_slide",
  "arguments": {
    "content": "# Hello World\n\nThis is my first slide!",
    "frontmatter": "{\"layout\": \"cover\"}"
  }
}
```

### 导出 PDF
```json
{
  "tool": "slidev_export_pdf",
  "arguments": {
    "output_path": "./presentation.pdf",
    "with_clicks": false,
    "dark": false
  }
}
```

## 项目结构

```
slidev-mcp/
├── main.go                 # 主入口，MCP server 初始化
├── internal/
│   ├── slidev/            # Slidev 核心功能
│   │   ├── parser.go      # Markdown 解析器
│   │   ├── writer.go      # Markdown 写入器
│   │   ├── project.go     # 项目操作
│   │   └── types.go       # 数据结构定义
│   ├── cli/               # CLI 命令执行器
│   │   └── executor.go
│   └── tools/             # MCP 工具实现
│       ├── create.go     # 创建相关工具
│       ├── edit.go       # 编辑相关工具
│       ├── manage.go      # 管理相关工具
│       ├── theme.go       # 主题相关工具
│       ├── export.go      # 导出相关工具
│       ├── project.go     # 项目相关工具
│       └── utils.go       # 工具函数
└── README.md
```


