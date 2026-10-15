# Chart-OCR-mcp

基于 PaddleOCR 的图表识别工具，支持从单张图表图片或 PowerPoint 文件中提取图表/表格区域，并输出结构化 JSON 结果。

项目当前提供三种使用方式：

- CLI 命令行工具：适合本地批处理和脚本调用。
- FastAPI Web 服务：适合上传图片或 PPT 后在浏览器中查看结果。
- MCP 本地工具：适合 Claude、Codex 等 Agent 通过 stdio 直接调用。

## 功能特性

- 单张图表图片识别：使用 `PP-Chart2Table` 解析图表并输出表格文本。
- PPT 图表识别：自动将 PPT/PPTX 渲染成图片，检测图表/表格/图形区域，裁剪后批量识别。
- 检测模式：PPT 可只做渲染和候选区域检测，不执行完整 OCR。
- Web API：提供图片 OCR、PPT OCR、示例图片和生成文件访问接口。
- MCP Server：暴露 `health_check`、`ocr_chart_image`、`ocr_ppt_charts` 三个工具，Agent 可直接调用。
- GPU 默认配置：默认使用 `PADDLE_OCR_DEVICE=gpu:0`，也可在 `.env` 中切换设备。

## 运行环境

建议环境：

- Windows 10/11
- Python `>=3.10,<3.13`
- uv
- NVIDIA GPU + CUDA 12.6 相关环境
- Microsoft PowerPoint，PPT 渲染功能需要本机 PowerPoint COM

当前依赖默认安装 GPU 版本：

```toml
paddlepaddle-gpu==3.3.0
```

如果要改用 CPU，需要将依赖中的 `paddlepaddle-gpu` 替换为 PaddlePaddle CPU 版本，并将 `.env` 中的设备改为：

```env
PADDLE_OCR_DEVICE=cpu
```

## 安装

在项目目录执行：

```powershell
cd C:\path\to\chart-ocr-mcp
uv sync
```

首次运行识别时，PaddleOCR 会下载模型到本机缓存目录，耗时取决于网络和模型缓存状态。

## 环境配置

项目会读取 `.env`：

```env
PADDLE_OCR_DEVICE=gpu:0
```

常见取值：

- `gpu:0`：使用第一张 GPU
- `cpu`：使用 CPU

`.env` 不建议提交到 GitHub。

## CLI 使用

### 识别单张图表图片

输出到文件：

```powershell
uv run chart-ocr input\1.png --out result.json --pretty
```

直接在终端输出：

```powershell
uv run chart-ocr input\1.png --pretty
```

### 识别 PPT 中的图表

完整识别：

```powershell
uv run ppt-chart-ocr input\output.pptx --out outputs\ppt_result.json --pretty
```

只检测并裁剪候选图表区域，不执行图表 OCR：

```powershell
uv run ppt-chart-ocr input\output.pptx --detect-only --work-dir outputs\ppt_detect --out outputs\ppt_detect.json --pretty
```

常用参数：

- `--work-dir`：保存渲染幻灯片和裁剪图的目录
- `--detect-only`：只做 PPT 渲染、布局检测和裁剪
- `--render-width` / `--render-height`：控制 PPT 渲染分辨率
- `--labels`：指定保留的布局类型，默认 `chart,table,figure`
- `--min-score`：候选区域最低置信度
- `--min-area-ratio`：候选区域最小面积比例

## Web 服务

启动服务：

```powershell
uv run python server.py
```

默认地址：

```text
http://127.0.0.1:8000
```

主要接口：

- `POST /api/ocr`：上传图片并执行图表 OCR
- `POST /api/ppt/ocr`：上传 `.ppt` 或 `.pptx` 并执行 PPT 图表识别
- `GET /api/demo`：读取本地 `result.json` 示例结果
- `GET /api/sample-images`：列出 `input/` 下的示例图片
- `GET /api/generated/{root_name}/{path}`：访问生成的图片文件

PPT 接口支持 `detect_only` 参数：

```text
POST /api/ppt/ocr?detect_only=true
```

## MCP Agent 工具

本项目已经封装为本地 stdio MCP Server，Agent 可以直接调用项目能力，不需要绕 Web API。

MCP Server 名称：

```text
chart-ocr-mcp
```

启动命令：

```powershell
uv --directory C:\path\to\chart-ocr-mcp run chart-ocr-mcp
```

Agent 配置示例：

```json
{
  "mcpServers": {
    "chart-ocr-mcp": {
      "command": "uv",
      "args": ["--directory", "C:\\path\\to\\chart-ocr-mcp", "run", "chart-ocr-mcp"]
    }
  }
}
```

### MCP 工具列表

#### `health_check`

轻量健康检查，不加载 OCR 大模型。

返回内容包括：

- Server 名称和版本
- Python 运行环境
- 当前设备配置
- `paddleocr` 是否可导入
- `mcp` 是否可导入
- PPT 渲染依赖说明

#### `ocr_chart_image`

识别本机图片文件。

参数：

```json
{
  "image_path": "C:\\path\\to\\chart-ocr-mcp\\input\\1.png"
}
```

返回结构：

```json
{
  "success": true,
  "source": "C:\\path\\to\\image.png",
  "device": "gpu:0",
  "data": {},
  "error": null
}
```

支持后缀：

```text
.png, .jpg, .jpeg, .bmp, .webp, .tif, .tiff
```

#### `ocr_ppt_charts`

识别本机 PPT/PPTX 文件。

参数：

```json
{
  "ppt_path": "C:\\path\\to\\chart-ocr-mcp\\input\\output.pptx",
  "detect_only": true,
  "work_dir": "C:\\path\\to\\chart-ocr-mcp\\outputs\\mcp_test"
}
```

字段说明：

- `ppt_path`：PPT/PPTX 文件路径
- `detect_only`：为 `true` 时只检测和裁剪图表区域，不执行 Chart OCR
- `work_dir`：可选，保存幻灯片渲染图和裁剪图；不传时默认写入 `outputs/mcp/<request_id>/`

返回结果中会包含：

- PPT 来源路径
- 工作目录
- 渲染尺寸和页数
- 检测模型信息
- 图表候选数量
- 每页候选区域
- 裁剪图片路径
- OCR 结果，非 `detect_only` 时包含

## MCP 可用性测试

在 PowerShell 中执行：

```powershell
cd C:\path\to\chart-ocr-mcp

@'
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="uv",
        args=["--directory", r"C:\path\to\chart-ocr-mcp", "run", "chart-ocr-mcp"],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([tool.name for tool in tools.tools])

asyncio.run(main())
'@ | .\.venv\Scripts\python.exe -
```

期望输出：

```text
['health_check', 'ocr_chart_image', 'ocr_ppt_charts']
```

## 输出目录

常见输出位置：

- `outputs/`：CLI、MCP 和测试输出
- `uploads/`：Web 上传和处理过程文件
- `input/`：示例图片和 PPT

建议不要将运行输出提交到 GitHub。

## 项目结构

```text
.
├── input/                    # 示例输入文件
├── outputs/                  # 运行输出目录
├── static/                   # Web 前端静态文件
├── uploads/                  # Web 上传和中间文件
├── src/chart_ocr/
│   ├── cli.py                # 单图 OCR CLI
│   ├── ppt_cli.py            # PPT 图表 OCR CLI
│   ├── ppt_pipeline.py       # PPT 渲染、布局检测、裁剪和识别流水线
│   ├── mcp_server.py         # MCP Server 入口
│   └── mcp_worker.py         # MCP OCR worker 子进程
├── server.py                 # FastAPI Web 服务
├── pyproject.toml            # 项目依赖和命令入口
└── uv.lock                   # uv 锁文件
```

## 常见问题

### 1. 首次运行很慢

首次运行会下载并加载 PaddleOCR 模型。后续如果模型已缓存，启动速度会明显变快。

### 2. PPT 识别失败

PPT 渲染依赖 Microsoft PowerPoint COM。请确认：

- 当前系统是 Windows
- 已安装 Microsoft PowerPoint
- PowerPoint 可以正常打开目标 PPT
- 目标文件不是损坏文件或受密码保护文件

### 3. GPU 或 CUDNN 警告

如果看到 CUDNN 版本警告，但识别仍然成功，可以先继续使用。若出现崩溃或结果异常，需要重新匹配 PaddlePaddle、CUDA 和 CUDNN 版本。

### 4. MCP 工具调用卡住

当前 MCP 实现会将 OCR 任务放到独立 worker 子进程中执行，避免 Paddle 日志和模型初始化干扰 stdio MCP 协议。如果仍然卡住，建议先调用 `health_check`，再用 `detect_only=true` 测 PPT 流程。

### 5. 乱码问题

Windows PowerShell 可能使用非 UTF-8 编码显示中文，导致终端输出看起来乱码。JSON 文件本身使用 UTF-8 写入，建议用 VS Code 或支持 UTF-8 的编辑器查看结果。

## License

当前项目未声明开源许可证。公开发布前请根据实际需求补充 License。
