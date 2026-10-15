# Office-PowerPoint-MCP-Server
[![smithery badge](https://smithery.ai/badge/@GongRzhe/Office-PowerPoint-MCP-Server)](https://smithery.ai/server/@GongRzhe/Office-PowerPoint-MCP-Server)
![](https://badge.mcpx.dev?type=server 'MCP Server')

A comprehensive MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. **Version 2.0** provides 32 powerful tools organized into 11 specialized modules, offering complete PowerPoint creation, management, and professional design capabilities. The server features a modular architecture with enhanced parameter handling, intelligent operation selection, and comprehensive error handling.

## 中文说明：PPT 生成 + MinIO 下载

本项目基于开源项目 `GongRzhe/Office-PowerPoint-MCP-Server` 做最小业务扩展。PPT 生成能力仍然来自原开源 MCP 和 `python-pptx`，本项目只补充“本地 artifact 管理 + 上传 MinIO + 返回下载链接”的能力。

### 推荐工具边界

现在不再建议把所有动作都塞进一个大工具里。MCP 同时提供分步工具和兼容的一键工具：

| 工具 | 用途 |
| --- | --- |
| `create_pptx_artifact` | 只生成 PPTX，并保存到隔离的本地 artifact 目录，返回 `artifact_id` |
| `upload_pptx_artifact_to_minio` | 只上传已生成的 `artifact_id`，返回 MinIO presigned 下载链接 |
| `get_pptx_artifact_info` | 查询 artifact 是否存在、页数、文件名、状态等信息 |
| `cleanup_pptx_artifact` | 删除本地 artifact 临时目录 |
| `generate_pptx_upload_minio` | 兼容工具，内部执行“生成 -> 上传 -> 清理” |

简单场景可以继续使用 `generate_pptx_upload_minio`。复杂 PPT、长 PPT、多风格 PPT、或者 Agent 容易把参数拼坏的场景，推荐使用 `create_pptx_artifact` + `upload_pptx_artifact_to_minio`。

### 推荐架构

```text
Java Agent / Spring AI
        |
        | MCP streamable-http
        v
pptx-minio-mcp
        |
        | create_pptx_artifact
        v
local artifact dir
        |
        | upload_pptx_artifact_to_minio
        v
MinIO / S3-compatible storage
        |
        | presigned url
        v
User browser download
```

### 为什么要拆分

拆分之后，PPT 生成失败、JSON 参数失败、MinIO 配置失败、上传失败会分开暴露，Agent 更容易恢复。

如果上传失败但生成成功，返回里会包含 `artifact_id`，这时只需要重试 `upload_pptx_artifact_to_minio`，不需要重新生成 PPT。

上传成功后默认清理本地文件，避免并发用户长期堆积临时 PPT。调试时可以传 `keep_local: true` 保留本地文件。

### 环境变量

可以通过系统环境变量、Docker 环境变量、平台 Secret 或 env 文件注入。示例文件见 `pptx-minio.env.example`。

```env
MINIO_ENDPOINT=your-minio-host.example.com
MINIO_PORT=9000
MINIO_USE_SSL=false
MINIO_ACCESS_KEY=REPLACE_ME
MINIO_SECRET_KEY=REPLACE_ME
MINIO_BUCKET_NAME=your-bucket
MINIO_PUBLIC_ENDPOINT=
MINIO_PRESIGN_EXPIRES=604800
PPTX_OBJECT_PREFIX=presentations
PPTX_MINIO_WORK_DIR=
PPTX_CLEANUP_LOCAL=true
DEBUG_MCP_ECHARTS=true
```

配置加载优先级：

```text
系统环境变量 > PPTX_MINIO_ENV_FILE 指定文件 > 当前目录 .env > 当前目录 pptx-minio.env > ~/.codex/pptx-minio.env > /etc/pptx-minio.env > 项目目录 pptx-minio.env > 项目目录 pptx-minio.env.example
```

变量说明：

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `MINIO_ENDPOINT` | 是 | MCP 服务上传文件时访问的 MinIO API 地址 |
| `MINIO_PORT` | 否 | MinIO API 端口 |
| `MINIO_USE_SSL` | 否 | 是否使用 HTTPS |
| `MINIO_ACCESS_KEY` | 是 | MinIO access key，不要返回给用户 |
| `MINIO_SECRET_KEY` | 是 | MinIO secret key，不要返回给用户 |
| `MINIO_BUCKET_NAME` | 是 | 上传使用的 bucket 名称 |
| `MINIO_PUBLIC_ENDPOINT` | 否 | 用户浏览器下载时访问的外部地址 |
| `MINIO_PRESIGN_EXPIRES` | 否 | 下载链接有效期，单位秒，最大 `604800` |
| `PPTX_OBJECT_PREFIX` | 否 | MinIO object key 前缀，默认 `presentations` |
| `PPTX_MINIO_WORK_DIR` | 否 | 本地 artifact 工作目录，默认系统临时目录 |
| `PPTX_CLEANUP_LOCAL` | 否 | 上传成功后是否删除本地 artifact，默认 `true` |
| `PPTX_MINIO_ENV_FILE` | 否 | 显式指定 env 配置文件路径 |

### 内外网地址说明

`MINIO_ENDPOINT` 是 MCP 服务端上传文件时使用的地址。

`MINIO_PUBLIC_ENDPOINT` 是最终用户浏览器下载文件时使用的地址。

如果 MCP 服务和 MinIO 在同一个 Docker 网络内，而用户从公网下载，建议这样配置：

```env
MINIO_ENDPOINT=minio
MINIO_PORT=9000
MINIO_USE_SSL=false
MINIO_PUBLIC_ENDPOINT=https://files.example.com
```

如果 MCP 服务直接通过公网 MinIO 地址上传和下载，可以不配置 `MINIO_PUBLIC_ENDPOINT`：

```env
MINIO_ENDPOINT=your-minio-public.example.com
MINIO_PORT=9000
MINIO_USE_SSL=true
MINIO_PUBLIC_ENDPOINT=
```

### 本地启动

Windows PowerShell：

```powershell
cd C:\Users\28582\Desktop\dev\mcp\mcp_server\pptx-minio-mcp
pip install -r requirements.txt
Copy-Item .\pptx-minio.env.example .\pptx-minio.env
notepad .\pptx-minio.env
python ppt_mcp_server.py --transport http --host 0.0.0.0 --port 8000
```

Linux / macOS：

```bash
cd /path/to/pptx-minio-mcp
pip install -r requirements.txt
cp pptx-minio.env.example pptx-minio.env
vi pptx-minio.env
python ppt_mcp_server.py --transport http --host 0.0.0.0 --port 8000
```

默认情况下，`--host` 是 `127.0.0.1`，只允许本机访问。如果需要让局域网、Docker 容器或 Spring AI 服务访问，请使用 `--host 0.0.0.0`。

如果访问时报：

```text
HTTP 421 Invalid Host header
```

说明请求里的 `Host` 头没有通过 MCP SDK 的 DNS rebinding 保护校验。生产环境可以通过 `--allowed-hosts` 和 `--allowed-origins` 显式配置白名单。

### Spring AI 连接示例

推荐使用 streamable HTTP，不推荐生产环境使用 stdio。

```yaml
spring:
  ai:
    mcp:
      client:
        toolcallback:
          enabled: true
        streamable-http:
          connections:
            pptx-minio:
              url: http://pptx-minio-mcp:8000
              endpoint: /mcp
```

### 分步工具示例

先生成本地 artifact：

```json
{
  "title": "人工智能发展历程",
  "topic": "AI 从规则系统到大模型的发展路径",
  "language": "zh-CN",
  "user_id": "user-123",
  "filename": "人工智能发展历程.pptx",
  "visual_style": "timeline_blue",
  "slides": []
}
```

返回示例：

```json
{
  "artifact_id": "pptx_20260618_ab12cd34ef56",
  "filename": "人工智能发展历程.pptx",
  "slide_count": 8,
  "status": "generated"
}
```

再上传 artifact：

```json
{
  "artifact_id": "pptx_20260618_ab12cd34ef56",
  "user_id": "user-123"
}
```

返回示例：

```json
{
  "download_url": "https://files.example.com/...?X-Amz-Signature=...",
  "object_key": "presentations/users/user-123/2026/06/18/pptx_20260618_ab12cd34ef56/人工智能发展历程.pptx",
  "bucket": "your-bucket",
  "filename": "人工智能发展历程.pptx",
  "slide_count": 8,
  "expires_at": "2026-06-25T00:00:00Z",
  "status": "uploaded"
}
```

### 一键工具示例

简单场景仍然可以使用：

```text
generate_pptx_upload_minio
```

它内部会执行：

```text
create_pptx_artifact -> upload_pptx_artifact_to_minio -> cleanup_pptx_artifact
```

如果上传失败但生成成功，会返回 `artifact_id`，Agent 应该复用这个 `artifact_id` 重试上传。

### 受控设计系统

默认生成引擎已经切换为受控中文设计系统：

```json
{
  "layout_engine": "design_system",
  "theme": "dark_tech",
  "design_profile": "auto",
  "layout_diversity": "high"
}
```

`design_system` 会使用稳定的中文商业 PPT 布局函数生成页面，避免上游演示模板中的 `Image 1`、`Metric/Q1/Q2`、默认 Contact、英文 placeholder 等内容泄露到最终 PPT。

如果需要回退到旧版手写高级布局，可以传：

```json
{
  "layout_engine": "premium_simple"
}
```

如果需要实验性调用开源 MCP 自带的 `slide_layout_templates.json` 模板库，可以传：

```json
{
  "layout_engine": "upstream_templates"
}
```

`upstream_templates` 不建议用于生产默认路径，因为上游模板库包含演示占位内容，需要非常完整的字段映射才能避免 placeholder 泄露。

如果需要回退到原开源基础模板映射，可以传：

```json
{
  "layout_engine": "classic_template"
}
```

复杂 PPT 建议让 Agent 先规划每页信息类型，再交给 `design_system` 决定最终布局。不要把所有内容页都写成 `bullets`。

### 支持的 slide type

| type | 说明 |
| --- | --- |
| `title` | 封面页 |
| `agenda` | 目录页 |
| `bullets` | 要点页 |
| `two-column` | 双栏内容页 |
| `three-column` | 三栏结构页 |
| `metrics` | 数据指标页 |
| `timeline` | 时间线页 |
| `process` | 流程步骤页 |
| `comparison` | 对比页 |
| `before-after` | 前后对比页 |
| `quote` | 引用观点页 |
| `table` | 数据表格页 |
| `team` | 团队介绍页 |
| `product` | 产品或方案展示页 |
| `chapter` | 章节过渡页 |
| `closing` | 结束页 |

生产默认不建议让 Agent 显式指定上游 `template_id`。只有在 `layout_engine` 为 `upstream_templates` 的实验模式下，才考虑使用 `template_id`，例如：

```json
{
  "type": "metrics",
  "title": "AI 应用价值指标",
  "template_id": "key_metrics_dashboard",
  "metrics": [
    {"label": "效率提升", "value": "40%"},
    {"label": "成本下降", "value": "25%"},
    {"label": "响应速度", "value": "3x"}
  ]
}
```

常用模板包括：

| template_id | 用途 |
| --- | --- |
| `title_slide` | 标准封面 |
| `minimalist_hero` | 极简封面 |
| `neon_cyberpunk` | 科技感封面 |
| `agenda_slide` | 目录 |
| `chapter_intro` | 章节过渡 |
| `text_with_image` | 图文要点 |
| `three_column_layout` | 三栏分析 |
| `two_column_text` | 双栏分析 |
| `key_metrics_dashboard` | 指标看板 |
| `timeline_slide` | 时间线 |
| `process_flow` | 流程图 |
| `before_after_comparison` | 前后对比 |
| `split_screen_comparison` | 左右对比 |
| `quote_testimonial` | 引用观点 |
| `data_table_slide` | 数据表格 |
| `team_introduction` | 团队介绍 |
| `product_showcase` | 产品展示 |
| `thank_you_slide` | 结束页 |

### 视觉风格

| visual_style | 说明 |
| --- | --- |
| `auto` | 默认，根据主题自动选择 |
| `timeline_blue` | 发展历程、时间线、阶段演进 |
| `executive_dark` | 商业战略、企业汇报、管理层汇报 |
| `academic_clean` | 研究报告、课程、教育、学术内容 |
| `warm_story` | 品牌、营销、故事型内容 |
| `premium_ai` | 通用 AI / 科技商业风 |
| `minimalist` | 极简黑白灰风格 |
| `creative_gradient` | 创意、活动、设计提案 |
| `classic_template` | 回退到开源 MCP 基础模板 |

### 并发与清理

每次生成都会创建独立 `artifact_id`，本地目录和 MinIO object key 都包含该 ID，避免并发用户互相覆盖。

默认 object key 格式：

```text
presentations/users/<user_id>/YYYY/MM/DD/<artifact_id>/<filename>.pptx
```

上传成功后默认删除本地 artifact。如果需要调试，可以传：

```json
{
  "keep_local": true
}
```

### 常见问题

如果 Spring AI 只能连接 `127.0.0.1`，说明 MCP 服务只监听本机地址。生产环境建议监听 `0.0.0.0`，并通过服务器 IP、Docker service name、Kubernetes Service 或 Nginx 域名访问。

如果上传成功但用户无法下载，优先检查 `MINIO_PUBLIC_ENDPOINT` 是否是用户浏览器可以访问的公网或内网地址。

如果返回 `Missing required MinIO configuration`，说明 `MINIO_ACCESS_KEY`、`MINIO_SECRET_KEY` 或 `MINIO_BUCKET_NAME` 没有注入到 MCP 服务进程。

如果 bucket 不存在，需要先在 MinIO 中创建 bucket，或者给当前 access key 分配创建 bucket / 写入 object 的权限。

如果下载链接过期，重新调用上传工具生成新的 presigned URL，或者调大 `MINIO_PRESIGN_EXPIRES`。
----

# **Not so ugly anymore with new slide_layout_templates**

<img width="1509" alt="截屏2025-06-20 15 53 45" src="https://github.com/user-attachments/assets/197d82cb-017a-4c00-b969-6e40440ffa36" />

----

### Example

#### Prompt

<img width="1280" alt="650f4cc5d0f1ea4f3b1580800cb0deb" src="https://github.com/user-attachments/assets/90633c97-f373-4c85-bc9c-a1d7b891c344" />

#### Output

<img width="1640" alt="084f1cf4bc7e4fcd4890c8f94f536c1" src="https://github.com/user-attachments/assets/420e63a0-15a4-46d8-b149-1408d23af038" />

#### Demo's GIF -> (./public/demo.mp4)

## Skill（配套说明）

仓库内已内置与本 MCP 匹配的 Skill：

`./.codex/skills/pptx-minio-upload/SKILL.md`

你可以直接将该目录作为配套文档发布，或在本机按需复制到：

- `C:\Users\<user>\.codex\skills\`
- `~/.codex/skills/`

Skill 的目标是让 Agent 只关心“生成 + 下载”两个动作，不直接接触 MinIO 底层细节和本地文件路径。

![demo](./public/demo.gif)

## Features

### Core PowerPoint Operations
- **Round-trip support** for any Open XML presentation (.pptx file) including all elements
- **Template support** with automatic theme and layout preservation
- **Multi-presentation management** with global state tracking
- **Core document properties** management (title, subject, author, keywords, comments)

### Content Creation & Management
- **Slide management** with flexible layout selection
- **Text manipulation** with placeholder population and bullet point creation
- **Advanced text formatting** with font, color, alignment, and style controls
- **Text validation** with automatic fit checking and optimization suggestions

### Visual Elements
- **Image handling** with file and base64 input support
- **Image enhancement** using Pillow with brightness, contrast, saturation, and filter controls
- **Professional image effects** including shadows, reflections, glows, and soft edges
- **Shape creation** with 20+ auto shape types (rectangles, ovals, flowchart elements, etc.)
- **Table creation** with advanced cell formatting and styling

### Charts & Data Visualization
- **Chart support** for column, bar, line, and pie charts
- **Data series management** with categories and multiple series support
- **Chart formatting** with legends, data labels, and titles

### Professional Design Features
- **4 professional color schemes** (Modern Blue, Corporate Gray, Elegant Green, Warm Red)
- **Professional typography** with Segoe UI font family and size presets
- **Theme application** with automatic styling across presentations
- **Gradient backgrounds** with customizable directions and color schemes
- **Slide enhancement** tools for existing content
- **25 built-in slide templates** with dynamic sizing and visual effects
- **Advanced template features** including auto-wrapping, dynamic font sizing, and professional animations

### Advanced Features
- **Font analysis and optimization** using FontTools
- **Picture effects** with 9 different visual effects (shadow, reflection, glow, bevel, etc.)
- **Comprehensive validation** with automatic error fixing
- **Template search** with configurable directory paths
- **Professional layout calculations** with margin and spacing management

## Installation

### Installing via Smithery

To install PowerPoint Manipulation Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@GongRzhe/Office-PowerPoint-MCP-Server):

```bash
npx -y @smithery/cli install @GongRzhe/Office-PowerPoint-MCP-Server --client claude
```

### Prerequisites

- Python 3.6 or higher (as specified in pyproject.toml)
- pip package manager
- Optional: uvx for package execution without local installation

### Installation Options

#### Option 1: Using the Setup Script (Recommended)

The easiest way to set up the PowerPoint MCP Server is using the provided setup script, which automates the installation process:

```bash
python setup_mcp.py
```

This script will:
- Check prerequisites
- Offer installation options:
  - Install from PyPI (recommended for most users)
  - Set up local development environment
- Install required dependencies
- Generate the appropriate MCP configuration file
- Provide instructions for integrating with Claude Desktop

The script offers different paths based on your environment:
- If you have `uvx` installed, it will configure using UVX (recommended)
- If the server is already installed, it provides configuration options
- If the server is not installed, it offers installation methods

#### Option 2: Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GongRzhe/Office-PowerPoint-MCP-Server.git
   cd Office-PowerPoint-MCP-Server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make the server executable:
   ```bash
   chmod +x ppt_mcp_server.py
   ```

## Usage

Display help text:
```bash
python ppt_mcp_server.py -h
```

### Starting the Stdio Server

Run the stdio server:

```bash
python ppt_mcp_server.py
```

### Starting the Streamable-Http Server

Run the streamable-http server on port 8000:

```bash
python ppt_mcp_server.py --transport http --port 8000
```

Run in Docker
```bash
docker build -t ppt_mcp_server .
docker run -d --rm -p 8000:8000 ppt_mcp_server -t http
```


### MCP Configuration

#### Option 1: Local Python Server

Add the server to your MCP settings configuration file:

```json
{
  "mcpServers": {
    "ppt": {
      "command": "python",
      "args": ["/path/to/ppt_mcp_server.py"],
      "env": {}
    }
  }
}
```

#### Option 2: Using UVX (No Local Installation Required)

If you have `uvx` installed, you can run the server directly from PyPI without local installation:

```json
{
  "mcpServers": {
    "ppt": {
      "command": "uvx",
      "args": [
        "--from", "office-powerpoint-mcp-server", "ppt_mcp_server"
      ],
      "env": {}
    }
  }
}
```

## 🚀 What's New in v2.0

### **Comprehensive Tool Suite (32 Tools)**
- **Complete PowerPoint manipulation** with 34 specialized tools
- **11 organized modules** covering all aspects of presentation creation
- **Enhanced parameter handling** with comprehensive validation
- **Intelligent defaults** and operation-based interfaces

### **Built-in Slide Templates**
- **25+ professional slide templates** with dynamic features built-in
- **Advanced template system** with auto-generation capabilities
- **Auto-sizing text** that adapts to content length and container size
- **Professional visual effects** including shadows, glows, and gradients
- **Complete presentation generation** from template sequences

### **Modular Architecture**
- **11 specialized modules**: presentation, content, structural, professional, template, hyperlink, chart, connector, master, and transition tools
- **Better maintainability** with separated concerns
- **Easier extensibility** for adding new features
- **Cleaner code structure** with shared utilities

## Available Tools

The server provides **34 specialized tools** organized into the following categories:

### **Presentation Management (7 tools)**
1. **create_presentation** - Create new presentations
2. **create_presentation_from_template** - Create from templates with theme preservation
3. **open_presentation** - Open existing presentations
4. **save_presentation** - Save presentations to files
5. **get_presentation_info** - Get comprehensive presentation information
6. **get_template_file_info** - Analyze template files and layouts
7. **set_core_properties** - Set document properties

### **Content Management (8 tools)**
8. **add_slide** - Add slides with optional background styling
9. **get_slide_info** - Get detailed slide information
10. **extract_slide_text** - ✨ **NEW** Extract all text content from a specific slide
11. **extract_presentation_text** - ✨ **NEW** Extract text content from all slides in presentation
12. **populate_placeholder** - Populate placeholders with text
13. **add_bullet_points** - Add formatted bullet points
14. **manage_text** - ✨ **Unified text tool** (add/format/validate/format_runs)
15. **manage_image** - ✨ **Unified image tool** (add/enhance)

### **Template Operations (7 tools)**
16. **list_slide_templates** - Browse available slide layout templates
17. **apply_slide_template** - Apply structured layout templates to existing slides
18. **create_slide_from_template** - Create new slides using layout templates
19. **create_presentation_from_templates** - Create complete presentations from template sequences
20. **get_template_info** - Get detailed information about specific templates
21. **auto_generate_presentation** - Automatically generate presentations based on topic
22. **optimize_slide_text** - Optimize text elements for better readability and fit

### **Structural Elements (4 tools)**
23. **add_table** - Create tables with enhanced formatting
24. **format_table_cell** - Format individual table cells
25. **add_shape** - Add shapes with text and formatting options
26. **add_chart** - Create charts with comprehensive customization

### **Professional Design (3 tools)**
27. **apply_professional_design** - ✨ **Unified design tool** (themes/slides/enhancement)
28. **apply_picture_effects** - ✨ **Unified effects tool** (9+ effects combined)
29. **manage_fonts** - ✨ **Unified font tool** (analyze/optimize/recommend)

### **Specialized Features (5 tools)**
30. **manage_hyperlinks** - Complete hyperlink management (add/remove/list/update)
31. **manage_slide_masters** - Access and manage slide master properties and layouts
32. **add_connector** - Add connector lines/arrows between points on slides
33. **update_chart_data** - Replace existing chart data with new categories and series
34. **manage_slide_transitions** - Basic slide transition management

## 🌟 Key Unified Tools

### **`manage_text`** - All-in-One Text Management
```python
# Add text box
manage_text(slide_index=0, operation="add", text="Hello World", font_size=24)

# Format existing text
manage_text(slide_index=0, operation="format", shape_index=0, bold=True, color=[255,0,0])

# Validate text fit with auto-fix
manage_text(slide_index=0, operation="validate", shape_index=0, validation_only=False)
```

### **`manage_image`** - Complete Image Handling
```python
# Add image with enhancement
manage_image(slide_index=0, operation="add", image_source="logo.png", 
            enhancement_style="presentation")

# Enhance existing image
manage_image(slide_index=0, operation="enhance", image_source="photo.jpg",
            brightness=1.2, contrast=1.1, saturation=1.3)
```

### **`apply_picture_effects`** - Multiple Effects in One Call
```python
# Apply combined effects
apply_picture_effects(slide_index=0, shape_index=0, effects={
    "shadow": {"blur_radius": 4.0, "color": [128,128,128]},
    "glow": {"size": 5.0, "color": [0,176,240]},
    "rotation": {"rotation": 15.0}
})
```

### **`apply_professional_design`** - Theme & Design Management
```python
# Add professional slide
apply_professional_design(operation="slide", slide_type="title_content", 
                         color_scheme="modern_blue", title="My Presentation")

# Apply theme to entire presentation  
apply_professional_design(operation="theme", color_scheme="corporate_gray")

# Enhance existing slide
apply_professional_design(operation="enhance", slide_index=0, color_scheme="elegant_green")
```

## Examples

### Creating a New Presentation

```python
# Create a new presentation
result = use_mcp_tool(
    server_name="ppt",
    tool_name="create_presentation",
    arguments={}
)
presentation_id = result["presentation_id"]

# Add a title slide
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 0,  # Title slide layout
        "title": "My Presentation",
        "presentation_id": presentation_id
    }
)
slide_index = result["slide_index"]

# Populate subtitle placeholder
result = use_mcp_tool(
    server_name="ppt",
    tool_name="populate_placeholder",
    arguments={
        "slide_index": slide_index,
        "placeholder_idx": 1,  # Subtitle placeholder
        "text": "Created with PowerPoint MCP Server",
        "presentation_id": presentation_id
    }
)

# Save the presentation
result = use_mcp_tool(
    server_name="ppt",
    tool_name="save_presentation",
    arguments={
        "file_path": "my_presentation.pptx",
        "presentation_id": presentation_id
    }
)
```

### Creating a Professional Presentation with v2.0

```python
# Create a professional slide with modern styling - CONSOLIDATED TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="apply_professional_design",
    arguments={
        "operation": "slide",
        "slide_type": "title_content",
        "color_scheme": "modern_blue",
        "title": "Quarterly Business Review",
        "content": [
            "Revenue increased by 15% compared to last quarter",
            "Customer satisfaction scores reached all-time high of 94%",
            "Successfully launched 3 new product features",
            "Expanded team by 12 new talented professionals"
        ]
    }
)

# Apply professional theme to entire presentation - SAME TOOL, DIFFERENT OPERATION
result = use_mcp_tool(
    server_name="ppt",
    tool_name="apply_professional_design",
    arguments={
        "operation": "theme",
        "color_scheme": "modern_blue",
        "apply_to_existing": True
    }
)

# Add slide with gradient background - ENHANCED ADD_SLIDE
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 0,
        "background_type": "professional_gradient",
        "color_scheme": "modern_blue",
        "gradient_direction": "diagonal"
    }
)
```

### Working with Built-in Slide Templates (New in v2.0)

```python
# List all available slide templates with their features
result = use_mcp_tool(
    server_name="ppt",
    tool_name="list_slide_templates",
    arguments={}
)

# Apply a professional template to an existing slide
result = use_mcp_tool(
    server_name="ppt",
    tool_name="apply_slide_template",
    arguments={
        "slide_index": 0,
        "template_id": "title_slide",
        "color_scheme": "modern_blue",
        "content_mapping": {
            "title": "Quarterly Business Review",
            "subtitle": "Q4 2024 Results",
            "author": "Leadership Team"
        }
    }
)

# Create a new slide using a template
result = use_mcp_tool(
    server_name="ppt",
    tool_name="create_slide_from_template",
    arguments={
        "template_id": "text_with_image",
        "color_scheme": "elegant_green",
        "content_mapping": {
            "title": "Our Revolutionary Solution",
            "content": "• 250% increase in efficiency\n• 98% customer satisfaction\n• Industry-leading performance"
        },
        "image_paths": {
            "supporting": "path/to/product_image.jpg"
        }
    }
)

# Generate a complete presentation from multiple templates
result = use_mcp_tool(
    server_name="ppt",
    tool_name="create_presentation_from_templates",
    arguments={
        "template_sequence": [
            {
                "template_id": "title_slide",
                "content": {
                    "title": "2024 Annual Report",
                    "subtitle": "Growth and Innovation",
                    "author": "Executive Team"
                }
            },
            {
                "template_id": "key_metrics_dashboard",
                "content": {
                    "metric_1_value": "94%",
                    "metric_2_value": "$2.4M",
                    "metric_3_value": "247"
                }
            },
            {
                "template_id": "before_after_comparison",
                "content": {
                    "content_left": "Manual processes taking hours",
                    "content_right": "Automated workflows in minutes"
                }
            }
        ],
        "color_scheme": "modern_blue"
    }
)
```

### Enhanced Image Management with v2.0

```python
# Add image with automatic enhancement - CONSOLIDATED TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="manage_image",
    arguments={
        "slide_index": 1,
        "operation": "add",
        "image_source": "company_logo.png",
        "left": 1.0,
        "top": 1.0,
        "width": 3.0,
        "height": 2.0,
        "enhancement_style": "presentation"
    }
)

# Apply multiple picture effects at once - CONSOLIDATED TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="apply_picture_effects",
    arguments={
        "slide_index": 1,
        "shape_index": 0,
        "effects": {
            "shadow": {
                "shadow_type": "outer",
                "blur_radius": 4.0,
                "distance": 3.0,
                "direction": 315.0,
                "color": [128, 128, 128],
                "transparency": 0.6
            },
            "glow": {
                "size": 5.0,
                "color": [0, 176, 240],
                "transparency": 0.4
            }
        }
    }
)
```

### Advanced Text Management with v2.0

```python
# Add and format text in one operation - CONSOLIDATED TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="manage_text",
    arguments={
        "slide_index": 0,
        "operation": "add",
        "left": 1.0,
        "top": 2.0,
        "width": 8.0,
        "height": 1.5,
        "text": "Welcome to Our Quarterly Review",
        "font_size": 32,
        "font_name": "Segoe UI",
        "bold": True,
        "color": [0, 120, 215],
        "alignment": "center",
        "auto_fit": True
    }
)

# Validate and fix text fit issues - SAME TOOL, DIFFERENT OPERATION
result = use_mcp_tool(
    server_name="ppt",
    tool_name="manage_text",
    arguments={
        "slide_index": 0,
        "operation": "validate",
        "shape_index": 0,
        "validation_only": False,  # Auto-fix enabled
        "min_font_size": 10,
        "max_font_size": 48
    }
)
```

### Creating a Presentation from Template

```python
# First, inspect a template to see its layouts and properties
result = use_mcp_tool(
    server_name="ppt",
    tool_name="get_template_info",
    arguments={
        "template_path": "company_template.pptx"
    }
)
template_info = result

# Create a new presentation from the template
result = use_mcp_tool(
    server_name="ppt",
    tool_name="create_presentation_from_template",
    arguments={
        "template_path": "company_template.pptx"
    }
)
presentation_id = result["presentation_id"]

# Add a slide using one of the template's layouts
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 1,  # Use layout from template
        "title": "Quarterly Report",
        "presentation_id": presentation_id
    }
)

# Save the presentation
result = use_mcp_tool(
    server_name="ppt",
    tool_name="save_presentation",
    arguments={
        "file_path": "quarterly_report.pptx",
        "presentation_id": presentation_id
    }
)
```

### Adding Advanced Charts and Data Visualization

```python
# Add a chart slide
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 1,  # Content slide layout
        "title": "Sales Data",
        "presentation_id": presentation_id
    }
)
slide_index = result["slide_index"]

# Add a column chart with comprehensive customization
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_chart",
    arguments={
        "slide_index": slide_index,
        "chart_type": "column",
        "left": 1.0,
        "top": 2.0,
        "width": 8.0,
        "height": 4.5,
        "categories": ["Q1", "Q2", "Q3", "Q4"],
        "series_names": ["2023", "2024"],
        "series_values": [
            [100, 120, 140, 160],
            [110, 130, 150, 170]
        ],
        "has_legend": True,
        "legend_position": "bottom",
        "has_data_labels": True,
        "title": "Quarterly Sales Performance",
        "presentation_id": presentation_id
    }
)
```

### Text Validation and Optimization with v2.0

```python
# Validate text fit and get optimization suggestions - USING CONSOLIDATED TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="manage_text",
    arguments={
        "slide_index": 0,
        "operation": "validate",
        "shape_index": 0,
        "text": "This is a very long title that might not fit properly in the designated text box area",
        "font_size": 24,
        "validation_only": True
    }
)

# Comprehensive slide validation with automatic fixes - SAME TOOL, AUTO-FIX ENABLED
result = use_mcp_tool(
    server_name="ppt",
    tool_name="manage_text",
    arguments={
        "slide_index": 0,
        "operation": "validate",
        "shape_index": 0,
        "validation_only": False,  # Auto-fix enabled
        "min_font_size": 10,
        "max_font_size": 48
    }
)
```

### Reading Slide Content with New Text Extraction Tools (v2.1)

```python
# Extract text content from a specific slide - NEW TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="extract_slide_text",
    arguments={
        "slide_index": 0,
        "presentation_id": presentation_id
    }
)

# The result includes:
{
    "success": True,
    "slide_index": 0,
    "text_content": {
        "slide_title": "Quarterly Business Review",
        "placeholders": [
            {
                "shape_index": 1,
                "shape_name": "Subtitle Placeholder 2",
                "text": "Q4 2024 Results",
                "placeholder_type": "SUBTITLE",
                "placeholder_idx": 1
            }
        ],
        "text_shapes": [
            {
                "shape_index": 3,
                "shape_name": "TextBox 4",
                "text": "Revenue increased by 15%"
            }
        ],
        "table_text": [],
        "all_text_combined": "Quarterly Business Review\nQ4 2024 Results\nRevenue increased by 15%"
    },
    "total_text_shapes": 2,
    "has_title": True,
    "has_tables": False
}

# Extract text from all slides in the presentation - NEW TOOL
result = use_mcp_tool(
    server_name="ppt",
    tool_name="extract_presentation_text",
    arguments={
        "presentation_id": presentation_id,
        "include_slide_info": True
    }
)

# The result includes comprehensive text extraction:
{
    "success": True,
    "presentation_id": "pres_123",
    "total_slides": 5,
    "slides_with_text": 4,
    "total_text_shapes": 12,
    "slides_with_titles": 3,
    "slides_with_tables": 1,
    "slides_text": [...],  # Detailed per-slide text content
    "all_presentation_text_combined": "=== SLIDE 1 ===\nTitle Here\nContent here..."
}

# Extract text without additional slide metadata for cleaner output
result = use_mcp_tool(
    server_name="ppt",
    tool_name="extract_presentation_text",
    arguments={
        "presentation_id": presentation_id,
        "include_slide_info": False
    }
)
```

## Template Support

### Working with Templates

The PowerPoint MCP Server provides comprehensive template support for creating presentations from existing template files. This feature enables:

- **Corporate branding** with predefined themes, layouts, and styles
- **Consistent presentations** across teams and projects  
- **Custom slide masters** and specialized layouts
- **Pre-configured properties** and document settings
- **Flexible template discovery** with configurable search paths

### Template File Requirements

- **Supported formats**: `.pptx` and `.potx` files
- **Existing content**: Templates can contain existing slides (preserved during creation)
- **Layout availability**: All custom layouts and slide masters are accessible
- **Search locations**: Configurable via `PPT_TEMPLATE_PATH` environment variable
- **Default search paths**: Current directory, `./templates`, `./assets`, `./resources`

### Template Configuration

Set the `PPT_TEMPLATE_PATH` environment variable to specify custom template directories:

```bash
# Unix/Linux/macOS
export PPT_TEMPLATE_PATH="/path/to/templates:/another/path"

# Windows  
set PPT_TEMPLATE_PATH="C:\templates;C:\company_templates"
```

### Template Workflow

1. **Inspect Template**: Use `get_template_info` to analyze available layouts and properties
2. **Create from Template**: Use `create_presentation_from_template` with automatic theme preservation
3. **Use Template Layouts**: Reference layout indices from template analysis when adding slides  
4. **Maintain Branding**: Template themes, fonts, and colors are automatically applied to new content

### Professional Color Schemes

The server includes 4 built-in professional color schemes:
- **Modern Blue**: Microsoft-inspired blue theme with complementary colors
- **Corporate Gray**: Professional grayscale theme with blue accents
- **Elegant Green**: Forest green theme with cream and light green accents  
- **Warm Red**: Deep red theme with orange and yellow accents

Each scheme includes primary, secondary, accent, light, and text colors optimized for business presentations.

## 🎨 Built-in Slide Templates (New in v2.0)

The PowerPoint MCP Server now includes **25 professional slide templates** with advanced dynamic features. All templates support:

### **Dynamic Features**
- **Automatic text sizing** based on content length and container dimensions
- **Intelligent text wrapping** to fit within specified areas
- **Visual effects** including shadows, glows, and outlines
- **Gradient backgrounds** with multi-layer compositions
- **Professional animations** ready for presentation delivery
- **Interactive hover effects** for enhanced user experience
- **Smart content overflow handling** with automatic adjustments

### **Available Template Categories**

#### **Title & Introduction Slides**
- `title_slide` - Dynamic title slide with gradient background and text effects
- `chapter_intro` - Section divider with chapter numbering and styling
- `thank_you_slide` - Closing slide with contact information and effects

#### **Content Layout Slides**
- `text_with_image` - Text content with stylized image and interactive elements
- `two_column_text` - Two equal columns of text with dynamic sizing
- `two_column_text_images` - Two columns with text and corresponding images
- `three_column_layout` - Three equal columns with text and images
- `full_image_slide` - Large background image with text overlay

#### **Business & Analytics Slides**
- `key_metrics_dashboard` - Interactive metrics dashboard with animated counters
- `before_after_comparison` - Dynamic comparison layout with visual dividers
- `chart_comparison` - Two charts side by side for performance comparison
- `data_table_slide` - Slide focused on tabular data with professional styling
- `timeline_slide` - Horizontal timeline with milestones and effects

#### **Process & Flow Slides**
- `process_flow` - Step-by-step process visualization with enhanced effects
- `agenda_slide` - Table of contents or agenda overview with styling
- `quote_testimonial` - Featured quote or customer testimonial with effects

#### **Team & Organization Slides**
- `team_introduction` - Team member showcase with photos and roles

### **Template Usage Examples**

```python
# Browse all available templates
templates = use_mcp_tool("ppt", "list_slide_templates", {})

# Key templates with their features:
{
  "title_slide": {
    "features": ["Dynamic text sizing", "Gradient backgrounds", "Text effects"],
    "elements": ["title", "subtitle", "author", "decorative_accent"]
  },
  "key_metrics_dashboard": {
    "features": ["Animated counters", "Gradient containers", "Trend visualization"],
    "elements": ["3 metric containers", "trend chart", "insights callout"]
  },
  "before_after_comparison": {
    "features": ["Split gradient background", "VS divider", "Improvement arrow"],
    "elements": ["before/after headers", "comparison content", "improvement metrics"]
  }
}
```

### **Color Scheme Integration**
All templates work seamlessly with the 4 professional color schemes:
- **modern_blue**: Microsoft-inspired theme with dynamic gradients
- **corporate_gray**: Professional grayscale with blue accents
- **elegant_green**: Forest green with cream and light accents
- **warm_red**: Deep red with orange and yellow highlights

### **Dynamic Content Adaptation**
Templates automatically adjust to content:
- **Font sizes** scale based on text length (8pt - 44pt range)
- **Line spacing** adjusts for readability (1.0x - 1.4x)
- **Text wrapping** intelligently breaks lines at optimal points
- **Container sizing** adapts to content overflow
- **Visual effects** scale appropriately with element sizes

## 📁 File Structure

```
Office-PowerPoint-MCP-Server/
├── ppt_mcp_server.py          # Main consolidated server (v2.0)
├── slide_layout_templates.json # 25+ professional slide templates with dynamic features
├── tools/                     # 11 specialized tool modules (32 tools total)
│   ├── __init__.py
│   ├── presentation_tools.py  # Presentation management (7 tools)
│   ├── content_tools.py       # Content & slides (6 tools)
│   ├── template_tools.py      # Template operations (7 tools)
│   ├── structural_tools.py    # Tables, shapes, charts (4 tools)
│   ├── professional_tools.py  # Themes, effects, fonts (3 tools)
│   ├── hyperlink_tools.py     # Hyperlink management (1 tool)
│   ├── chart_tools.py         # Advanced chart operations (1 tool)
│   ├── connector_tools.py     # Connector lines/arrows (1 tool)
│   ├── master_tools.py        # Slide master management (1 tool)
│   └── transition_tools.py    # Slide transitions (1 tool)
├── utils/                     # 7 organized utility modules (68+ functions)
│   ├── __init__.py
│   ├── core_utils.py          # Error handling & safe operations
│   ├── presentation_utils.py  # Presentation management utilities
│   ├── content_utils.py       # Content & slide operations
│   ├── design_utils.py        # Themes, colors, effects & fonts
│   ├── template_utils.py      # Template management & dynamic features
│   └── validation_utils.py    # Text & layout validation
├── setup_mcp.py              # Interactive setup script
├── pyproject.toml            # Updated for v2.0
└── README.md                 # This documentation
```

## 🏗️ Architecture Benefits

### **Modular Design**
- **7 focused utility modules** with clear responsibilities
- **11 organized tool modules** for comprehensive coverage
- **68+ utility functions** organized by functionality
- **32 MCP tools** covering all PowerPoint manipulation needs
- **Clear separation of concerns** for easier development

### **Code Organization**
- **Logical grouping** of related functionality across modules
- **Better discoverability** with organized tool categories
- **Improved testability** with isolated modules
- **Future extensibility** through modular structure

### **Comprehensive Coverage**
- **Complete PowerPoint lifecycle** from creation to presentation
- **Advanced template system** with auto-generation capabilities
- **Professional design tools** with multiple effects and styling options
- **Specialized features** including hyperlinks, connectors, and slide masters

### **Developer Experience**
- **Clear responsibility boundaries** between modules
- **Easier debugging** with smaller, focused files
- **Simpler testing** with isolated functionality
- **Enhanced maintainability** through separation of concerns

## 🔄 What's New in Version 2.0

**Enhanced functionality with comprehensive tool coverage!** The updated server provides:

### **New Specialized Tools Added:**
- **`manage_hyperlinks`** - Complete hyperlink management for text elements
- **`update_chart_data`** - Advanced chart data replacement and updating
- **`add_connector`** - Connector lines and arrows between slide elements
- **`manage_slide_masters`** - Access to slide master properties and layouts
- **`manage_slide_transitions`** - Basic slide transition management
- **`auto_generate_presentation`** - AI-powered presentation generation
- **`optimize_slide_text`** - Text optimization for better readability

### **Enhanced Existing Tools:**
- **`manage_text`** - Now supports text run formatting with `format_runs` operation
- **`create_presentation_from_templates`** - Enhanced template sequence processing
- **`apply_picture_effects`** - Expanded effect combinations and options

## 🔄 What's New in Version 2.1

**Text extraction capabilities added!** Now you can read content from existing presentations:

### **New Text Extraction Tools Added:**
- **`extract_slide_text`** - Extract all text content from a specific slide including titles, placeholders, text shapes, and tables
- **`extract_presentation_text`** - Extract text content from all slides in a presentation with comprehensive statistics and combined output

### **Key Features of Text Extraction:**
- **Complete text coverage** - Extracts from titles, placeholders, text boxes, and table cells
- **Structured output** - Organized by content type (titles, placeholders, shapes, tables)
- **Presentation-wide analysis** - Statistics on text distribution across slides
- **Flexible output options** - Individual slide content or combined presentation text
- **Error handling** - Graceful handling of slides that cannot be processed

## License

MIT

