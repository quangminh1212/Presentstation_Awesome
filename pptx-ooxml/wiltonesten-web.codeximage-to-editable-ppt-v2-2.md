# codeximage-to-editable-ppt-v2-2

**简体中文** | [English](README.en.md)

这是 [`codeximage-to-editable-ppt-v2-1`](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v2-1) 的多页并行升级版。它面向由图片或截图构成的多页 PowerPoint，在完整保留 V2.1 单页精细重建、可编辑性和质量校验标准的同时，让多个页面由相互隔离的页面工作单元并行处理，最后按原始顺序合并为一个 PPTX。

当前 Skill 版本为 **2.2.0**，可以并行处理 3、6、9 等数量的图片； 实际并行规模取决于可用的任务树和硬件容量。

## 核心价值：显著提高多页处理效率

V2.1 按页精细重建时，需要完成文字可编辑化、原生形状重建、复杂视觉元素处理、PowerPoint 渲染和质量检查。V2.2 将这些完整步骤分配给多个页面工作单元并行执行，因此在硬件和 Codex 工作单元容量允许、实际任务确实发生重叠时，可以显著缩短多页演示文稿的整体等待时间。

- 2–3 个页面工作单元：在一个 Codex 任务树中并行处理；
- 4–6 个页面工作单元：需要两个独立任务树；7–9 个页面工作单元需要三个独立任务树。创建每个辅助任务前均须获得用户明确授权；
- 根据 CPU、可用内存、PowerPoint 进程和可用工作单元计算保守并行建议；
- 记录真实开始与结束时间，计算实际并发峰值和实测加速比；
- 未测得任务重叠时，不会把顺序执行描述成成功并行。

V2.2 提高的是多页调度效率，不会削弱每一页的 V2.1 质量标准。

## V1、V1.2、V2.1 与 V2.2 如何选择

- **[V1：节省 Token 版本](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v1)。** 复杂图片主要采用原图裁剪和复用，重点将文字与简单结构转换为可编辑对象。Token 和时间成本较低，适合一般组会汇报、内部交流和快速整理。
- **[V1.2：多页并行、节省 Token 版本](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v1-2)。** 它是 V1 的升级编排层，在保留 V1 单页质量标准和裁剪复用策略的同时，通过独立页面工作单元并行处理 3、6、9 等数量的图片。适合需要较低 Token 成本和较高多页处理效率的组会汇报与内部材料。
- **[V2.1：单页精细版本](https://github.com/wiltonesten-web/codeximage-to-editable-ppt-v2-1)。** 对视觉质量和结构拆分要求更高；复杂图片可调用 `imagegen` 修复、清理背景，必要时甚至重绘。适合正式答辩、对外汇报和高保真单页交付。
- **V2.2：多页并行精细版本。** 每一页仍执行完整 V2.1 流程，同时并行处理 2–9 页并有序合并。它适合需要兼顾精细质量和多页效率的任务，但通常比 V1 消耗更多 Token 和计算时间。

## 工作方式

1. 只读预检输入页面、硬件容量和 V2.1 依赖；
2. 展示逐页重建策略、公共页眉处理方案和建议工作单元数量；
3. 获得本次任务的明确确认后，建立互不共享写入目录的页面任务；
4. 为每一页执行完整 V2.1 精细重建与 PowerPoint 质量检查；
5. 复用经过验证的公共品牌页眉，减少重复工作并保证多页一致性；
6. 通过确定性的 OpenXML 合并保持原始页面顺序；
7. 校验页数、画布、对象数量、文件哈希和实际并发记录；
8. 最终只向用户交付一个合并后的 `.pptx` 文件。

## 质量与安全门

- 可识别文字保持为可编辑文本；
- 简单结构使用 PowerPoint 原生对象；
- 复杂、样式敏感的科学视觉内容保留为独立语义 PNG；
- 复杂图片可按需通过 `imagegen` 修复、清理或重绘；
- 每页必须经过 Microsoft PowerPoint 渲染和视觉检查；
- 文本溢出、对象越界、清单缺失或页面质量失败时停止交付；
- 页面任务使用独立目录，禁止多个工作单元写入同一 PPTX；
- 合并后默认只做结构与哈希快速校验，不重复执行无必要的整套渲染。

## 仓库结构

实际 Codex Skill 位于：

```text
skills/codeximage-to-editable-ppt-v2-2
```

V2.2 是编排升级层，运行时会读取同级安装的 V2.1 规范与参考文件。请同时安装 V2.1，并保持两个 Skill 目录同级。

## 安装

先安装 V2.1：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo wiltonesten-web/codeximage-to-editable-ppt-v2-1 `
  --path skills/codeximage-to-editable-ppt-v2-1
```

再安装 V2.2：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo wiltonesten-web/codeximage-to-editable-ppt-v2-2 `
  --path skills/codeximage-to-editable-ppt-v2-2
```

最终目录应类似：

```text
%USERPROFILE%\.codex\skills\
|-- codeximage-to-editable-ppt-v2-1\
`-- codeximage-to-editable-ppt-v2-2\
```

安装完成后重启 Codex，使其重新发现 Skill。

## Python 依赖

```powershell
pip install -r skills\codeximage-to-editable-ppt-v2-2\requirements.txt
```

Windows 上的严格最终质量检查需要 Microsoft PowerPoint；OCR 需要 Tesseract 及相应语言包。图片型 PPT/PPTX 的回退转换可能还需要 LibreOffice 和 Poppler。精细背景或复杂视觉元素的修复需要 Codex `imagegen` Skill。

## 在 Codex 中使用

```text
使用 $codeximage-to-editable-ppt-v2-2 并行处理这些图片型幻灯片，
按 V2.1 精细标准重建为可编辑 PowerPoint，确认逐页策略和工作单元数量后执行，
最终只交付一个按原始顺序合并的 PPTX。
```

Skill 会先完成预检并请求确认，不会仅凭一句“批量处理”就直接创建页面任务。选择 4–9 个页面工作单元时，还需要用户明确同意创建所需的辅助任务。

## 主要脚本

- `parallel_v2_pages.py`：预检、任务准备、计时、完成记录、合并与发布；
- `validate_delivery.py`：复用 V2.1 交付质量门；
- `validate_layout_powerpoint.py`：通过 PowerPoint 渲染检查页面布局；
- `shared_masthead.py`：冻结并校验多页共用品牌页眉；
- `launch_diagnostics.py`：读取调度事件并报告实际启动情况；
- `decompose_visual_elements.py`：生成逐页基线拆解和检查证据。

## 重要限制

- 栅格输入无法完美恢复原始矢量图、隐藏文字、图表数据、字体、动画或对象语义。
- OCR、公式、小字号文字、密集图表和科学插图必须人工视觉检查。
- 并行能力取决于硬件、Codex 可用工作单元和 PowerPoint 环境；不保证固定运行时间或固定加速比。
- 2–9 页是当前一次确认运行的支持范围；更大的演示文稿应拆分为多次受控运行。
- 不要把机密源演示文稿或专有资源上传到公开 Issue 或案例目录。

## 项目状态

本仓库以独立社区项目形式发布，与 OpenAI 或 Microsoft 不存在隶属或官方认可关系。

## 许可证

采用 MIT License，详情参见 [LICENSE](LICENSE)。
