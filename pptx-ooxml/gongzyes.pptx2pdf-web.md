# PPT转PDF 在线转换工具

一个简洁美观的在线 PPTX → PDF 转换工具，基于 Flask + LibreOffice。

## 功能

- 📁 拖拽或点击上传 PPTX 文件
- 📦 支持批量上传和转换
- ⏱ 实时转换进度和计时
- ⬇️ 单个下载或全部打包 ZIP 下载
- 🧹 自动清理临时文件（1小时）
- 📱 移动端自适应

## 快速开始

### 前置条件

- Python 3.8+
- LibreOffice

### 安装

```bash
# macOS
brew install --cask libreoffice
pip install flask

# Ubuntu/Debian
sudo apt install libreoffice
pip install flask
```

### 运行

```bash
python app.py
```

访问 http://localhost:5050

## 技术栈

- **后端**: Flask (Python)
- **前端**: 原生 HTML/CSS/JS（无外部依赖）
- **转换引擎**: LibreOffice headless mode

## 项目结构

```
pptx2pdf-web/
├── app.py              # Flask 后端
├── templates/
│   └── index.html      # 前端页面
├── uploads/            # 临时上传目录（自动创建）
├── outputs/            # 转换输出目录（自动创建）
└── static/             # 静态资源
```

## API

| 端点 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 首页 |
| `/api/convert` | POST | 上传并转换 PPTX 文件 |
| `/api/download/<job_id>/<filename>` | GET | 下载单个 PDF |
| `/api/download-all/<job_id>` | GET | 下载全部 PDF（ZIP） |

## License

MIT
