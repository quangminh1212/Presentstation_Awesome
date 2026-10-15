# PPT奖状批量生成工具

一个简单易用的工具，可以从Excel文件中读取姓名，并将它们批量填充到PPT模板中，生成个性化的奖状。

## 功能特点

- 批量生成个性化PPT奖状
- 保持原有格式（字体、颜色、大小等）
- 支持可选的PDF转换功能
- 固定占位符 `<<name>>`，简单易用
- 简易Web前端界面
- 支持命令行和Web界面双重操作

## 环境要求

- Python 3.6+

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 命令行使用

1. 准备PPT模板文件，确保包含 `<<name>>` 占位符
2. 准备Excel数据文件，包含姓名信息
3. 运行脚本：

```bash
# 交互式使用
python src/optimized_ppt_certificates.py

# 或指定参数
python src/optimized_ppt_certificates.py --template 模板.pptx --excel 数据.xlsx --pdf
```

### Web界面使用

1. 启动Web服务器：
```bash
python run.py
```

2. 打开浏览器访问 `http://127.0.0.1:5000`

3. 上传PPT模板和Excel文件，点击生成

### Windows一键启动

双击运行 `start.bat` 脚本。

## 参数说明

- `--template` 或 `-t`: 指定PPT模板文件路径
- `--excel` 或 `-e`: 指定Excel数据文件路径
- `--output-dir` 或 `-o`: 指定输出目录（默认为"批量生成的奖状"）
- `--pdf`: 启用PPT到PDF转换功能

## 文件说明

- `src/optimized_ppt_certificates.py`: 主要功能脚本
- `app.py`: Web服务器应用
- `run.py`: 快速启动脚本
- `templates/index.html`: Web前端界面
- `docs/HOW_TO_USE.md`: 详细使用说明
- `requirements.txt`: 项目依赖
- `start.bat`: Windows启动脚本

## 注意事项

- 脚本会自动使用 `<<name>>` 作为占位符
- 如需PDF转换功能，请确保已安装Microsoft PowerPoint
- Excel文件的第一列应包含姓名信息

## 注意事项

- 脚本会自动使用 `<<name>>` 作为占位符
- 如需PDF转换功能，请确保已安装Microsoft PowerPoint
- Excel文件的第一列应包含姓名信息