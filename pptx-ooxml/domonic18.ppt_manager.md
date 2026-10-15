# PPT 管理器

这是一个用于加载、解析、编辑和导出PowerPoint (PPTX) 文件的Python库。

## 功能

- PPTX文件管理功能
  - 加载PPTX文件并提取详细信息
  - 将演示文稿转换为JSON结构化数据
  - 获取幻灯片布局(Layout)信息
- PPTX文件渲染功能
  - 将幻灯片渲染为高质量图片
  - 支持单页或整份文档渲染
- PPTX文件幻灯片编辑功能
  - 基于布局(Layout)信息创建新幻灯片
  - 复制现有幻灯片
  - 删除单个或批量幻灯片
- PPTX文件幻灯片-文本编辑功能
  - 精确定位和修改文本元素
  - 调整文本字体大小
  - 调整文本位置
  - 调整文本颜色
- PPTX文件幻灯片-形状编辑功能
  - 获取幻灯片中的形状元素
  - 替换幻灯片中的形状
  - 调整形状大小
  - 调整形状位置
  - 调整形状颜色
- PPTX文件幻灯片-图片编辑功能
  - 获取幻灯片中的图片元素
  - 替换幻灯片中的图片
  - 调整图片大小
  - 调整图片位置
- PPTX文件保存功能
  - 保存修改后的PPTX文件
## 快速开始

### 安装依赖

```bash
# 从项目目录安装
pip install -e .
```

安装soffice组件

```bash
# 安装soffice组件
brew install soffice
```

安装pdf2image组件

```bash
# 安装pdf2image组件
pip install pdf2image
```

### 代码实现

PPT管理器提供了以下接口，方便用户快速实现常见功能。

### 1. PPTX文件管理功能
#### 1.1 获取整个演示文稿的JSON结构
将PPTX文件转换为JSON格式，方便进行结构化分析和处理。

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 这种方式可以重复使用已加载的演示文稿，而不需要多次读取文件
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")
ppt_json = ppt_manager.get_presentation_json(
    presentation=presentation,
    include_details=True  # 是否包含元素详细信息
)

# 输出基本信息
print(f"演示文稿宽度: {ppt_json['width']}, 高度: {ppt_json['height']}")
print(f"幻灯片数量: {ppt_json['slide_count']}")
print(f"元数据-标题: {ppt_json.get('metadata', {}).get('title', '无标题')}")
```

#### 1.2 获取指定幻灯片的JSON结构

```python
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")
# 获取指定幻灯片的JSON结构
slide_json = ppt_manager.get_slide_json(
    presentation=presentation,
    slide_index=0  # 第一张幻灯片，索引从0开始
)


# 获取所有幻灯片的JSON结构
all_slides_json = ppt_manager.get_slide_json(
    presentation=presentation,
    slide_index=None  # None表示获取所有幻灯片
)
```

#### 1.3 获取PPT中模板中的所有Layout

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")
layouts_json = ppt_manager.get_layouts_json(presentation)
```

#### 1.4 获取指定幻灯片的Layout
```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取指定幻灯片的Layout信息
slide_index = 0  # 第一张幻灯片的索引
layout_json = ppt_manager.get_slide_layout_json(presentation, slide_index)
```

### 2. PPTX文件渲染显示功能
#### 2.1 渲染所有幻灯片为图片

将PPT幻灯片渲染为高质量图片，支持渲染指定页或全部页面。

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 方法1: 渲染所有幻灯片 - 从文件路径
image_files = ppt_manager.render_pptx_file(
    pptx_path="path/to/your/presentation.pptx",
    output_dir="output/images",
    format="png"  # 支持"png"、"jpg"、"pdf"
)

print(f"共渲染 {len(image_files)} 张幻灯片图片:")
for img_file in image_files:
    print(f"  - {os.path.basename(img_file)}")

# 方法2: 渲染所有幻灯片 - 从已加载的演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")
image_files = ppt_manager.render_presentation(
    presentation=presentation,
    output_dir="output/images",
    format="png"  # 支持"png"、"jpg"、"pdf"
)
```

#### 2.2 渲染指定幻灯片为图片

```python
# 方法1: 从文件路径渲染指定幻灯片
image_paths = ppt_manager.render_pptx_file(
    pptx_path="path/to/your/presentation.pptx",
    output_dir="output/images",
    slide_index=2,  # 索引为2的幻灯片（第3张）
    format="png"
)

# 方法2: 从已加载的演示文稿渲染指定幻灯片
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")
image_paths = ppt_manager.render_presentation(
    presentation=presentation,
    output_dir="output/images",
    slide_index=2,  # 索引为2的幻灯片（第3张）
    format="png"
)
```

### 3. PPTX文件幻灯片编辑功能
#### 3.1 根据Layout创建新的幻灯片

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 首先加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 可选：获取并查看可用的layout
layouts_json = ppt_manager.get_layouts_json(presentation)
print("可用的layout名称：")
for layout in layouts_json:
    print(f"- {layout['layout_name']}")

# 使用指定layout创建新的幻灯片（添加到末尾）
result = ppt_manager.create_slide_with_layout(
    presentation=presentation,
    layout_name="Title Slide",  # 使用您需要的layout名称
    insert_position=-1  # -1表示添加到末尾
)
```

#### 3.2 复制幻灯片

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取要复制的幻灯片索引（例如第三张幻灯片）
slide_index = 2

# 复制幻灯片到末尾
duplicate_result = ppt_manager.duplicate_slide(
    presentation=presentation,
    slide_index=slide_index
)

# 复制幻灯片到指定位置（第2张幻灯片之后）
insert_position = 1  # 索引从0开始，所以这是第2张幻灯片之后
duplicate_result = ppt_manager.duplicate_slide(
    presentation=presentation,
    slide_index=slide_index,
    insert_position=insert_position
)
```

#### 3.3 删除单个幻灯片

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 删除指定索引的幻灯片（例如第三张幻灯片）
slide_index = 2
delete_result = ppt_manager.delete_slide(
    presentation=presentation,
    slide_index=slide_index
)
```

#### 3.4 批量删除幻灯片

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 方法1: 通过索引列表删除多个幻灯片
slide_indices = [1, 3]  # 删除第2张和第4张幻灯片
delete_result = ppt_manager.delete_slides(
    presentation=presentation,
    slide_indices=slide_indices
)

# 方法2: 通过索引范围删除多个幻灯片（删除第2-4张幻灯片）
delete_result = ppt_manager.delete_slides(
    presentation=presentation,
    start_index=1,  # 从0开始计数
    end_index=3
)
```

### 4. PPTX文件幻灯片-文本编辑功能
#### 4.1 更新幻灯片中的文本元素内容

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取幻灯片和元素ID
slide_index = 0  # 第一张幻灯片
# 假设我们要编辑标题元素
title_element = None
for element in presentation.slides[slide_index].elements:
    if hasattr(element, "metadata") and element.metadata.get("shape_name", "").lower().startswith("title"):
        title_element = element
        break

if title_element:
    element_id = title_element.element_id
    # 编辑文本内容
    new_content = "这是新的标题文本"
    edit_result = ppt_manager.update_element_content(
        presentation=presentation,
        slide_index=slide_index,
        element_id=element_id,
        new_content=new_content
    )
```

#### 4.2 调整文本元素字体大小

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取幻灯片和元素ID
slide_index = 0  # 第一张幻灯片
# 假设我们要调整标题元素的字体大小
title_element = None
for element in presentation.slides[slide_index].elements:
    if hasattr(element, "metadata") and element.metadata.get("shape_name", "").lower().startswith("title"):
        title_element = element
        break

if title_element:
    element_id = title_element.element_id
    # 调整字体大小为36磅
    new_font_size = 36
    adjust_result = ppt_manager.adjust_text_font_size(
        presentation=presentation,
        slide_index=slide_index,
        element_id=element_id,
        font_size=new_font_size
    )
```

#### 4.3 调整元素位置和大小

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取幻灯片和元素ID
slide_index = 0  # 第一张幻灯片
element_id = "your-element-id"  # 元素ID，可通过遍历幻灯片元素获取

# 调整元素位置和大小
adjust_result = ppt_manager.adjust_element_position(
    presentation=presentation,
    slide_index=slide_index,
    element_id=element_id,
    left=100,  # 新的左侧位置(Point)
    top=150,   # 新的顶部位置(Point)
    width=400, # 新的宽度(Point)
    height=300 # 新的高度(Point)
)
```

### 5. PPTX文件幻灯片-图片编辑功能
#### 5.1 获取幻灯片中的图片元素

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 获取指定幻灯片中的所有图片元素
slide_index = 0  # 第一张幻灯片
result = ppt_manager.get_image_elements(
    presentation=presentation,
    slide_index=slide_index
)

# 遍历图片元素
if result["success"] and result["image_count"] > 0:
    for image in result["images"]:
        print(f"图片ID: {image['element_id']}, 路径: {image['image_path']}")
```

#### 5.2 替换幻灯片中的图片

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 首先获取幻灯片中的图片元素
slide_index = 0  # 第一张幻灯片
image_result = ppt_manager.get_image_elements(
    presentation=presentation,
    slide_index=slide_index
)

if image_result["success"] and image_result["image_count"] > 0:
    # 找到一个图片元素
    element_id = image_result["images"][0]["element_id"]
    
    # 替换图片
    replace_result = ppt_manager.replace_image(
        presentation=presentation,
        slide_index=slide_index,
        element_id=element_id,
        image_path="path/to/new/image.jpg"  # 新图片路径
    )
```

### 6. 保存修改后的演示文稿

```python
from interfaces.ppt_api import PPTManager

# 初始化PPT管理器
ppt_manager = PPTManager()

# 加载演示文稿
presentation = ppt_manager.load_presentation("path/to/your/presentation.pptx")

# 进行各种编辑操作...

# 保存修改后的演示文稿
output_path = "path/to/output.pptx"
saved_path = ppt_manager.save_presentation(presentation, output_path)
print(f"演示文稿已保存至: {saved_path}")
```

## 项目结构

```
ppt_manager/
├── interfaces/          # 高级API接口
│   ├── __init__.py      # 接口模块初始化
│   └── ppt_api.py       # PPT管理器高级API
├── core/                # 核心功能
│   ├── loader.py        # PPTX文件加载器
│   ├── exporter/        # 导出模块
│   │   ├── __init__.py  # 导出工具函数
│   │   └── pptx_renderer.py # PPT渲染器
│   │   └── json_exporter.py # JSON导出器
│   ├── parser/          # 解析器模块
│   │   ├── shape_parser.py    # 形状解析器
│   │   ├── text_processor.py  # 文本处理器
│   │   └── layout_analyzer.py # 布局分析器
│   └── editor/          # 编辑模块
│       ├── __init__.py  # 编辑模块初始化
│       └── pptx_editor.py     # PPTX编辑器
├── models/              # 数据模型
│   ├── presentation.py  # 演示文稿模型
│   ├── slide.py         # 幻灯片模型
│   └── elements.py      # 元素模型
├── utils/               # 工具函数
│   ├── units.py         # 单位转换
│   ├── style_tools.py   # 样式处理
│   └── resource_manager.py  # 资源管理
└── test/                # 测试用例
    └── testfiles/       # 测试文件
```