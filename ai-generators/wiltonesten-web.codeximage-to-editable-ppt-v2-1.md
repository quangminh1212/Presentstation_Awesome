# codeximage-to-editable-ppt-v2-1

**简体中文** | [English](README.en.md)

这是一个 Codex Skill，用于将图片型 PowerPoint 演示文稿和幻灯片截图重建为忠于原图、
可编辑的 PPTX 文件，并采用“验证失败即停止交付”的严格校验机制。

本 Skill 面向扁平化栅格幻灯片，包括整页截图、仅包含图片的 PPT/PPTX、扫描幻灯片，
以及大部分可见内容并非 PowerPoint 原生对象的演示文稿。它采用混合保真重建策略：

- 将可识别文字转换为可编辑 PowerPoint 文本框；
- 将简单结构转换为 PowerPoint 原生形状；
- 将复杂或对样式敏感的视觉内容保留为独立的语义 PNG 资源；
- 复杂整页背景可能需要经过检查的 Image Gen 重建；
- 在清单、裁剪、背景及 PowerPoint 最终渲染质量门未通过前，禁止完成交付。

自动拆解脚本用于生成基线结果和检查证据，不能单独视为已经完成的 V2.1 精细交付。

## V1 与 V2 如何选择

- **[V1：节省 Token 版本](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v1)。**
  复杂图片以原图裁剪和复用为主，重点将文字与简单结构转换为可编辑对象，
  能以较低的 Token 和时间成本完成可编辑化，适合一般组会汇报、内部交流和快速整理。
- **V2：精细版本。** 对视觉质量和结构拆分要求更高；复杂图片会按需调用 `imagegen`
  进行修复、清理背景，必要时甚至重绘相关视觉元素。它适合正式答辩、对外汇报和高保真交付，
  但通常需要更多 Token 和处理时间。

具体展示见这个链接：[点击前往抖音观看](https://v.douyin.com/kEuzE5mgFko/)

## 输出内容

- 不可变的源页面图片
- 独立语义 PNG 元素
- CSV 和 JSON 格式的视觉元素清单
- 裁剪与背景视觉审计
- 检查叠加图和棋盘格预览
- 用于参考的基础重组 PPTX
- 通过 Codex 工作流生成的精细可编辑 PPTX
- PowerPoint 渲染预览和逐页质量报告
- 验证失败即停止交付的校验报告
- 确定性批处理摘要和合并后的基线演示文稿

## 案例展示

### 案例 01：C-S-H 神经进化学术幻灯片

左侧图片为原始扁平化幻灯片，右侧图片为 V2.1 在 PowerPoint 中的重建结果。
结果图中的选择框和控制手柄表明，该页面包含多个可独立选择和编辑的对象。

<table>
  <tr>
    <th width="50%">原始扁平化幻灯片</th>
    <th width="50%">可编辑 PowerPoint 结果</th>
  </tr>
  <tr>
    <td width="50%">
      <a href="examples/case-01-csh-neuroevolution-slide/original-slide.png">
        <img src="examples/case-01-csh-neuroevolution-slide/original-slide.png" alt="原始扁平化学术幻灯片" width="100%">
      </a>
    </td>
    <td width="50%">
      <a href="examples/case-01-csh-neuroevolution-slide/editable-powerpoint-view.png">
        <img src="examples/case-01-csh-neuroevolution-slide/editable-powerpoint-view.png" alt="包含独立可选对象的可编辑 PowerPoint 结果" width="100%">
      </a>
    </td>
  </tr>
</table>

[查看案例详情](examples/case-01-csh-neuroevolution-slide/)。

### 案例 02：C-S-H“三难”学术幻灯片

左侧图片为原始扁平化幻灯片，右侧图片为 V2.1 在 PowerPoint 中的重建结果。
结果图中的选择框和控制手柄表明，该页面包含多个可独立选择和编辑的对象。

<table>
  <tr>
    <th width="50%">原始扁平化幻灯片</th>
    <th width="50%">可编辑 PowerPoint 结果</th>
  </tr>
  <tr>
    <td width="50%">
      <a href="examples/case-02-csh-three-challenges-slide/original-slide.png">
        <img src="examples/case-02-csh-three-challenges-slide/original-slide.png" alt="C-S-H 三难页面的原始扁平化学术幻灯片" width="100%">
      </a>
    </td>
    <td width="50%">
      <a href="examples/case-02-csh-three-challenges-slide/editable-powerpoint-view.png">
        <img src="examples/case-02-csh-three-challenges-slide/editable-powerpoint-view.png" alt="C-S-H 三难页面的可编辑 PowerPoint 结果" width="100%">
      </a>
    </td>
  </tr>
</table>

[查看案例详情](examples/case-02-csh-three-challenges-slide/)。

## 仓库结构

实际 Codex Skill 位于：

```text
skills/codeximage-to-editable-ppt-v2-1
```

这是一个独立于 `codeximage-to-editable-ppt-v1` 的 Skill。安装 V2.1 不会修改或替换 V1。

## 安装为 Codex Skill

使用 Codex Skill 安装脚本从 GitHub 安装：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo wiltonesten-web/codeximage-to-editable-ppt-v2-1 \
  --path skills/codeximage-to-editable-ppt-v2-1
```

PowerShell：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo wiltonesten-web/codeximage-to-editable-ppt-v2-1 `
  --path skills/codeximage-to-editable-ppt-v2-1
```

最终安装目录应为：

```text
%USERPROFILE%\.codex\skills\codeximage-to-editable-ppt-v2-1
```

如需手动安装，只需将 `skills/codeximage-to-editable-ppt-v2-1` 文件夹复制到 Codex Skill 目录。
不要将整个仓库根目录作为 Skill 文件夹复制。

安装完成后请重启 Codex，使其重新发现该 Skill。

## Python 依赖

在仓库根目录安装 Python 软件包：

```bash
pip install -r skills/codeximage-to-editable-ppt-v2-1/requirements.txt
```

按需安装的系统依赖：

- `PATH` 中的 LibreOffice：用于 PPT/PPTX 回退转换和预览导出
- 包含 `pdftoppm` 的 Poppler 工具：用于 PDF 或页面栅格化
- Tesseract OCR，以及 `eng`、`chi_sim` 等所需语言包
- Microsoft PowerPoint 或同等高保真渲染器：用于严格的最终质量检查
- 需要重建复杂背景时使用 Codex `imagegen` Skill

Ubuntu/Debian 安装示例：

```bash
sudo apt-get update
sudo apt-get install -y \
  libreoffice \
  poppler-utils \
  tesseract-ocr \
  tesseract-ocr-eng \
  tesseract-ocr-chi-sim
```

## 基线拆解

运行自动化基线拆解：

```bash
python skills/codeximage-to-editable-ppt-v2-1/scripts/decompose_visual_elements.py \
  input.pptx \
  --outdir baseline_output \
  --dpi 300 \
  --granularity fine \
  --ocr \
  --ocr-lang chi_sim+eng \
  --ocr-confidence-threshold 75 \
  --editable-text \
  --review \
  --quality-check
```

使用示例配置运行：

```bash
python skills/codeximage-to-editable-ppt-v2-1/scripts/decompose_visual_elements.py \
  input.pptx \
  --config skills/codeximage-to-editable-ppt-v2-1/config.example.yaml \
  --outdir baseline_output
```

基线输出属于发现和检查产物，不应作为严格的 V2.1 最终交付结果。

## 精细可编辑重建

在 Codex 中使用类似下面的请求调用该 Skill：

```text
使用 $codeximage-to-editable-ppt-v2-1 将 input.pptx 重建为忠于原图的可编辑 PowerPoint，
并通过所有强制交付质量门。
```

该 Skill 会指导 Codex：

1. 原样保留源页面；
2. 仅将自动化基线用于内容发现；
3. 按最终表现形式对每个可见对象进行分类；
4. 将文字和简单结构重建为可编辑 PowerPoint 对象；
5. 将复杂视觉内容隔离为独立语义 PNG；
6. 生成裁剪、背景、清单和质量检查证据；
7. 检查从最终 PPTX 导出的渲染结果；
8. 任何强制校验门未解决时停止交付。

## 交付校验

交付前验证经过整理的精细输出：

```bash
python skills/codeximage-to-editable-ppt-v2-1/scripts/validate_delivery.py \
  refined_output \
  --pptx presentation_refined_editable.pptx
```

退出代码为 `0` 表示可由机器检查的质量门已经通过。非零退出代码表示不得将该演示文稿作为
严格交付完成结果提供。

校验内容包括：

- 源页面与 PPTX 的宽高比一致性；
- 可识别文字的可编辑性和原生简单结构；
- 语义 PNG 的独立性和归属关系；
- 裁剪透明度、残留、重复和重叠证据；
- 大型背景的来源和前景移除证据；
- 尚未解决的检查项；
- PowerPoint 对象越界以及清单与 PPTX 的对应关系；
- 逐页通过/失败状态和必要质量计数器。

## 批量处理

以确定性批次重复运行基线拆解：

```bash
python skills/codeximage-to-editable-ppt-v2-1/scripts/run_batches.py \
  input_folder \
  --outdir batch_output \
  --recursive \
  --batch-size 2 \
  --batch-workers 2 \
  --dpi 300 \
  --granularity fine \
  --ocr \
  --ocr-lang chi_sim+eng \
  --ocr-confidence-threshold 75 \
  --editable-text \
  --review \
  --quality-check
```

批处理成功仅表示基线脚本已经完成。每个经过整理的精细演示文稿仍须单独通过
`validate_delivery.py`。

## 精细输出目录结构

```text
<name>_refined_editable.pptx
<name>_refined_editable_output/
|-- source_pages/
|-- split_png_elements/
|-- split_png_elements.zip
|-- visual_elements_manifest.csv
|-- visual_elements_manifest.json
|-- image_source_report.csv
|-- image_source_report.json
|-- review/
|   |-- <page>_refined_elements_overlay.png
|   |-- background_visual_audit/
|   |   |-- background_audit.csv
|   |   `-- <page>_<background>_audit.png
|   `-- crop_visual_audit/
|       |-- crop_audit.csv
|       |-- crop_audit.json
|       `-- all_crop_audit.png
|-- quality_preview/
|   `-- powerpoint_export/
|-- quality_report/
|   |-- quality_report.csv
|   |-- quality_report.json
|   |-- <page>_original.png
|   |-- <page>_recomposed.png
|   |-- <page>_diff.png
|   |-- delivery_validation.csv
|   `-- delivery_validation.json
`-- recomposed_from_elements.pptx
```

## 重要限制

- 栅格输入无法完美恢复原始矢量图、隐藏文字、图表数据、字体、动画或对象语义。
- OCR 结果必须经过检查，尤其是中文、公式、小字号文字、图表和密集标签。
- 如果原生重绘会降低保真度，复杂视觉内容可以继续保留为栅格资源。
- Image Gen 完成并不代表已经获得合格的清洁背景；仍须进行视觉审计和最终 PowerPoint 渲染检查。
- 不要将机密源演示文稿或专有资源上传到公开 Issue 或案例目录。

## 项目状态

本仓库以独立社区项目的形式发布 V2.1 Skill，与 OpenAI 或 Microsoft 不存在隶属或官方认可关系。

## 许可证

采用 MIT License，详情参见 [LICENSE](LICENSE)。
