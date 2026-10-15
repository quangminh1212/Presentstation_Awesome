# HTML2PPTX - 智能HTML到PowerPoint转换器

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PowerPoint](https://img.shields.io/badge/PowerPoint-支持-orange.svg)]()

一个强大的Python库，能够将HTML页面智能转换为高质量的PowerPoint演示文稿。采用模块化设计，针对不同页面类型（封面页、目录页、内容页）提供专门化的转换处理。

## ✨ 核心特性

- 🎯 **专门化转换** - 针对不同页面类型提供优化的转换逻辑
- 🎨 **高精度布局** - CSS样式到PowerPoint的精确转换
- 🔄 **模块化架构** - 易于维护和扩展的设计
- 🖼️ **智能图标处理** - 支持FontAwesome图标转换
- 🎭 **动态颜色混合** - 自动处理透明度和渐变效果
- 📐 **精确圆角转换** - 基于实测数据的border-radius公式
- 🔤 **垂直文字支持** - 完美呈现旋转文字效果
- 🎪 **装饰元素处理** - 自动识别和转换装饰性图形

## 📦 支持的页面类型

| 类型 | 说明 | 特色功能 |
|------|------|----------|
| `cover` | 封面页 | 标题框背景、FontAwesome图标、渐变装饰 |
| `catalog` | 目录页 | 编号圆圈、垂直文字、侧边栏 |
| `content` | 内容页 | 图表容器、页码显示、数据可视化 |
| `generic` | 通用页 | 基础文本布局、通用样式处理 |

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基础使用

```python
from HTML2PPTX import HTML2PPTX

# 创建转换器实例
converter = HTML2PPTX()

# 转换封面页
converter.convert_html_to_pptx('cover', 'html/cover.html', 'output/cover.pptx')

# 转换目录页
converter.convert_html_to_pptx('catalog', 'html/catalog.html', 'output/catalog.pptx')

# 转换内容页
converter.convert_html_to_pptx('content', 'html/content.html', 'output/content.pptx')
```

## 📚 API 文档

### HTML2PPTX类

#### `__init__()`
创建转换器实例，初始化所有专门化转换器。

#### `convert_html_to_pptx(page_type, html_file, output_pptx)`
执行HTML到PPTX的转换。

**参数：**
- `page_type` (str): 页面类型，可选值: `'cover'`, `'catalog'`, `'content'`, `'generic'`
- `html_file` (str): 输入HTML文件路径
- `output_pptx` (str): 输出PPTX文件路径

**返回值：**
- `str`: 输出文件路径

**异常：**
- `ValueError`: 当页面类型无效时
- `FileNotFoundError`: 当HTML文件不存在时

## 🏗️ 项目结构

```
html2pptx-backend/
├── HTML2PPTX.py              # 主转换器类
├── converter/               # 转换器模块
│   ├── __init__.py          # 模块初始化
│   ├── BaseConverter.py     # 基础转换器
│   ├── CoverConverter.py    # 封面页转换器
│   ├── CatalogConverter.py  # 目录页转换器
│   └── ContentConverter.py  # 内容页转换器
├── html/                    # HTML测试文件
│   ├── cover.html           # 封面页示例
│   ├── catalog.html         # 目录页示例
│   ├── content_2.html       # 内容页示例
│   └── content_3.html       # 内容页示例
├── requirements.txt         # 项目依赖
├── README.md               # 项目文档
└── .gitignore             # Git忽略配置
```

## 🔧 技术细节

### 转换流程

1. **HTML解析** - 使用BeautifulSoup解析HTML结构
2. **CSS提取** - 通过cssutils提取和解析内嵌样式
3. **页面类型选择** - 根据指定类型选择专门转换器
4. **样式转换** - CSS属性到PowerPoint格式的精确映射
5. **元素定位** - 像素到英寸的精确坐标转换
6. **PPTX生成** - 使用python-pptx创建最终演示文稿

### 核心算法

#### 颜色混合算法
```python
# Alpha混合公式
result = foreground * alpha + background * (1 - alpha)
```

#### Border-radius转换公式
```python
# 基于实测数据的分段线性公式
base_coefficient = 0.00375  # 0.03 / 8px
if border_radius_px <= 15:
    adjustment_value = border_radius_px * base_coefficient
elif border_radius_px <= 30:
    adjustment_value = border_radius_px * base_coefficient * 1.5
else:
    adjustment_value = border_radius_px * base_coefficient * 3
```

#### 坐标转换
```python
# CSS像素到PowerPoint英寸转换
px_to_inch_x = pptx_width / slide_width    # 16 / 1280
px_to_inch_y = pptx_height / slide_height  # 9 / 720
```

## 📋 依赖项

- **python-pptx** (>=0.6.21) - PowerPoint文件操作
- **beautifulsoup4** (>=4.11.1) - HTML解析
- **lxml** (>=4.9.1) - XML处理引擎
- **cssutils** (>=2.7.1) - CSS解析和处理

## 🎯 使用示例

### 批量转换

```python
from HTML2PPTX import HTML2PPTX

def batch_convert():
    converter = HTML2PPTX()
    
    # 转换配置
    conversions = [
        ('cover', 'slides/title.html', 'output/01_title.pptx'),
        ('catalog', 'slides/toc.html', 'output/02_toc.pptx'),
        ('content', 'slides/data1.html', 'output/03_data1.pptx'),
        ('content', 'slides/data2.html', 'output/04_data2.pptx'),
    ]
    
    for page_type, html_file, output_file in conversions:
        try:
            result = converter.convert_html_to_pptx(page_type, html_file, output_file)
            print(f"✅ 成功转换: {result}")
        except Exception as e:
            print(f"❌ 转换失败: {html_file} - {e}")

if __name__ == "__main__":
    batch_convert()
```

### 错误处理

```python
from HTML2PPTX import HTML2PPTX

converter = HTML2PPTX()

try:
    result = converter.convert_html_to_pptx('cover', 'input.html', 'output.pptx')
except ValueError as e:
    print(f"参数错误: {e}")
except FileNotFoundError as e:
    print(f"文件不存在: {e}")
except Exception as e:
    print(f"转换失败: {e}")
```

## 🎨 HTML要求

为了获得最佳转换效果，HTML文件应该：

### 封面页 (cover)
```html
<div class="cover-container">
    <div class="title-box">
        <h1 class="main-title">主标题</h1>
        <p class="subtitle">副标题</p>
        <div class="key-insight">关键洞察</div>
        <div class="footer-info">页脚信息</div>
    </div>
</div>
```

### 目录页 (catalog)
```html
<div class="catalog-container">
    <div class="sidebar">
        <div class="sidebar-title">CONTENTS</div>
    </div>
    <ul class="toc-list">
        <li class="toc-item active">项目1</li>
        <li class="toc-item">项目2</li>
    </ul>
</div>
```

### 内容页 (content)
```html
<div class="content-container">
    <h1 class="page-title">页面标题</h1>
    <div class="chart-container">
        <h2 class="chart-title">图表标题</h2>
        <canvas>图表内容</canvas>
    </div>
</div>
```

## 🛠️ 开发

### 设置开发环境

```bash
# 克隆仓库
git clone <repository-url>
cd html2pptx-backend

# 安装依赖
pip install -r requirements.txt

# 运行测试
python -c "
from HTML2PPTX import HTML2PPTX
converter = HTML2PPTX()
converter.convert_html_to_pptx('cover', 'html/cover.html', 'test.pptx')
print('✅ 测试成功')
"
```

### 添加新的页面类型

1. 在 `converter/` 目录创建新的转换器类
2. 继承 `BaseConverter` 类
3. 实现 `convert()` 方法
4. 在 `__init__.py` 中导出新类
5. 在主转换器中添加类型支持

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙋‍♂️ 支持

如果遇到问题或有功能建议，请：

1. 查看现有的 Issues
2. 创建新的 Issue 描述问题
3. 提供详细的重现步骤和环境信息

## 📈 版本历史

- **v2.0.0** - 模块化重构，显式类型指定
- **v1.5.0** - 动态颜色混合，精确圆角转换
- **v1.0.0** - 初始发布，基础转换功能

---

⭐ 如果这个项目对你有帮助，请给它一个星标！