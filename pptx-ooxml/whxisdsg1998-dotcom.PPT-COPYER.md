# CSCECppt 使用说明

把一份做好的 PowerPoint 当"模板"，让 AI 自动把新内容套进这套版式里——
不转 SVG、不重做设计，保留原 PPT 的字体、配色、版式、装饰，只换文字和图片。

---

## 一、这个 skill 是做什么的

你有一份现成的、做得好看的 PPT（比如公司标准课件），想用**同样的版式**做一份**新主题**的 PPT。

CSCECppt 帮你：
1. 扫描这份模板 PPT，把每一页的文字框、图片位、表格逐个识别出来；
2. 你确认哪些能替换、哪些是固定装饰；
3. AI 按版式写出逐页文案（或你自己给）；
4. 自动生成初稿：文字填好，图片位先放**蓝色编号占位框**（1.1、1.2…）；
5. 你按编号把图片丢进去，生成第二稿成品。

**核心理念**：模板里的公司 logo、标语、底纹、装饰色块、插画**全部原样保留**，只替换正文内容。

---

## 二、安装

1. 把整个 `cscecppt-skill-package` 文件夹拷到电脑上任意位置。
2. 终端运行：
   ```bash
   bash cscecppt-skill-package/install.sh
   ```
   脚本会把 skill 装到 `~/.hermes/skills/productivity/cscecppt`，并装上它依赖的
   最小 PPTX 填充引擎（ppt-master 的 template_fill 子集）。
3. 安装脚本会自动检查依赖：
   - **Python 3.11+**，并需要 `python-pptx`、`Pillow`：
     `pip install python-pptx Pillow`
   - **LibreOffice**（用于把 PPT 渲染成图做视觉审计）：
     macOS `brew install --cask libreoffice`

装好后，在你的 AI agent 里直接说一句话即可触发，见下。

---

## 三、怎么用（最简）

对 AI 说：

> 用 CSCECppt 做这个 PPT：/path/to/你的模板.pptx

AI 会自动加载 skill 并按下面的流程一步步走。中间它会停下来问你两件事：
- 确认模板里哪些元素可替换；
- 你有没有逐页文案稿（有就给它，没有就把"主题+各部分要点"给它，它来写）。

---

## 四、工作流程（AI 内部按此执行）

```
模板PPT
  │
  ├─ ① 扫描         识别每页文字/图片/表格/组合对象 → template_review_compact.md
  │
  ├─ ② 视觉审查     把每页渲染成图，AI 逐页看（强制逐页，不抽样）
  │                 核对：哪些是内容、哪些是固定装饰
  │
  ├─ ③ 你确认       在确认稿里标 可替换=True / 可删除=True
  │
  ├─ ④ 模板规格书   每页能放多少字、几张图、标题在哪 → 定量约束
  │
  ├─ ⑤ 写逐页稿     按版式容量写文案，每页锁定到一个模板页+槽位
  │
  ├─ ⑥ 匹配         逐页稿 ↔ 模板页 对应关系
  │
  ├─ ⑦ 生成初稿     文字填好 + 图片位放蓝色编号占位框(1.1/1.2…)
  │                 → first_draft_xxx_cleaned.pptx + 图片清单
  │
  ├─ ⑧ 对象+视觉QA  逐页检查：旧文字残留?重叠压字?装饰被误删?偏空偏满?
  │
  ├─ ⑨ 你收集图片   按清单编号命名(1.1.png/2.3.jpg)放进 images/ 目录
  │
  └─ ⑩ 回填生成成品 图片按编号填入 → exports/second_draft_xxx.pptx
```

---

## 五、产出物（都在一个项目文件夹里）

每个任务一个独立文件夹（不同模板互不干扰）：
`~/Downloads/AI/CSCECppt/<项目名>/`

```
sources/      模板.pptx、逐页稿 page_script.md
analysis/     扫描结果、确认稿、匹配结果
manifests/    图片清单 image_manifest.md（按编号说明每张图要什么）
drafts/       初稿（蓝色占位框版）   ← 交付看 *_cleaned.pptx
images/        你放图片的地方（文件名以编号开头）
exports/      第二稿成品（图片已填）
validation/   渲染图 + QA 报告
```

---

## 六、几个关键规则（避免踩坑）

- **图片编号 A.B**：A=输出页号，B=该页第几张。例：`1.3` = 第1页第3张图。
  收集图片时文件名必须以编号开头：`1.3.png`、`2.1.jpg`。
- **删除是"确认驱动"**：只有你在确认稿里显式标 `可删除=True` 的元素才会被删。
  空文本框、装饰色块、箭头、插画**默认保留**，不会被自动删。
- **逐页视觉审计是强制的**：AI 必须把每一页都渲染出来看过，不能只抽查几页。
- **每个模板 = 独立文件夹**：不会跨项目乱用别的模板页。
- **交付文件认 `_cleaned`**：初稿目录里 `*_cleaned.pptx` 才是处理完的成品稿。

---

## 七、依赖说明

| 依赖 | 用途 | 安装 |
|---|---|---|
| Python 3.11+ | 运行脚本 | 系统自带或自行安装 |
| python-pptx | 读写 PPTX | `pip install python-pptx` |
| Pillow | 生成蓝色占位图 | `pip install Pillow` |
| LibreOffice | 渲染 PPT 做视觉审计 | `brew install --cask libreoffice` |
| ppt-master(子集) | PPTX 填充引擎 | **已随包附带**，install.sh 自动装 |

---

## 八、包内结构

```
cscecppt-skill-package/
├── install.sh              一键安装脚本
├── README.md               本说明
├── skill/cscecppt/         skill 本体（SKILL.md + 11脚本 + 18参考文档）
└── dependency/ppt-master/  最小填充引擎（cscecppt 调用它做 analyze/apply）
```
