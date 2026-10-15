# pptx-bilingual-translate

一个 Claude 技能（Claude Skill）：把中文 PPT 课件整章翻译成**英文版**与**中英对照版**两份成品，
自动重排版面、处理 WPS 隐藏内容、防止文字溢出。

方法论来自一套 900 余页、11 个章节的半导体封装教材 PPT 的实战翻译。
`scripts/` 是可直接运行的完整工具链，不是示例代码。

## 为什么需要它

直接用 `python-pptx` 遍历 run 替换文字，会得到四类必然的失败：

- 英文比中文长约一倍，而文本框是固定的 → 满页正文出血到页外、压住下方图片；
- PowerPoint 的 `normAutofit`（"溢出时缩排文字"）**在导出与非 PowerPoint 渲染时不生效**
  → 你以为会自动缩小，实际被裁掉；
- WPS 把大量内容藏在 `<mc:AlternateContent>` 里，**`python-pptx` 完全看不见**
  → 整页正文、整张表格原样留着中文；
- `tf.clear()` 保留首段 `pPr` → 原本带自动编号的单元格渲染出幽灵 `1.`。

这个技能把字号计算、按邻居实测的版面重排、隐藏内容的原始 XML 改写，以及一整套校验固化了下来。

## 安装

### Claude Code（个人技能）

```bash
git clone https://github.com/Xingzaozhan43-ultimate/pptx-bilingual-translate.git ~/.claude/skills/pptx-bilingual-translate
```

Windows PowerShell：

```powershell
git clone https://github.com/Xingzaozhan43-ultimate/pptx-bilingual-translate.git "$env:USERPROFILE\.claude\skills\pptx-bilingual-translate"
```

### 只给某个项目用

克隆到项目的 `.claude/skills/pptx-bilingual-translate/` 即可。

装好后新开一个会话，跟 Claude 说「帮我把这个 pptx 翻译成英文版和中英对照版」就会触发。

### 依赖

```bash
pip install python-pptx Pillow
```

`Pillow` 只有渲染核对（`ink.py` / `lines.py`）用得到。
逐页导 PNG 依赖本机安装的 PowerPoint（通过 COM）；没有的话可以退而用 LibreOffice，
但结论只能当参考——整条流水线之所以要自己算字号，就是因为渲染器不认 `normAutofit`。

## 内容

```
SKILL.md                     工作流主文档（八步）
references/
  pipeline.md                命令速查、目录结构、失败信号对照表
  layout.md                  排版分类器与六种重排策略
  hidden-content.md          mc:AlternateContent 的一切
  translating.md             译写规范、术语、改原文的边界、翻不了的东西
  verification.md            各项检查的含义、已知假阳性、渲染核对
  pitfalls.md                十一章积累的具体坑点清单
scripts/                     可直接运行的工具链（见下）
```

| 脚本 | 作用 |
|---|---|
| `config.py` | 每章唯一需要改的机器配置 |
| `audit.py` | 清点可见文本与表格 → `audit.json` |
| `scan_raw.py` | 原始 XML 侦察：隐藏块、表数、公式中文、页序 |
| `extract_choice.py` | 提取隐藏块两侧文本与矩形 → `choice_audit.json` |
| `dump_geom.py` | 打印每个形状的矩形、字号、首行文字 |
| `gen_skel.py` | 生成逐 run 替换表骨架（`repr` 过的精确键） |
| `gen_acpara.py` | 把按序号的草稿转成按内容匹配的段落表 |
| `build_full.py` | 排版重建：六类形状、六种策略、显式字号 |
| `process_hidden.py` | 改原始 XML 翻译隐藏内容 |
| `ac_fit.py` / `ac_fit_tbl.py` / `apply_scale.py` | 隐藏块字号收敛 |
| `check_coverage.py` / `check_paras.py` / `check_residual.py` | 覆盖率、段落配对、残留中文 |
| `check_overflow.py` / `check_onpic.py` / `check_ac_geom.py` | 溢出、文字压图、块几何 |
| `run_checks.py` | 一次跑完全套并汇总 |
| `export_png.ps1` / `ink.py` / `lines.py` | 渲染核对与行距标定 |
| `translations.py` / `tr_p1.py` / `cn_fix.py` / `ac_draft.py` | 每章要填的内容文件（模板） |

## 状态

工具链在一个 85 页、238 个文本项、含隐藏块与公式的真实章节上验证过：
重跑整条流水线后，产物与已交付成品逐形状比对，**文本与字号零差异**，
矩形仅有 0.01 in 级的浮点差。无隐藏内容的路径（`AC_SLIDES = []`）也单独验证过。

版面常数在 13.333 × 7.5 in（16:9）的 WPS 教材模板上标定。换模板要先用 `dump_geom.py`
量一遍，并用 `lines.py` 重新标定行距——行距差 20% 就是"放得下"和"最后一行掉出页底"的区别。

## 许可

MIT。仓库只包含工具链与方法论，不含任何教材原文或译文。

---

## English

A Claude Skill for translating a Chinese PowerPoint deck into an **English deck** plus a
**Chinese/English bilingual deck**, rebuilding the layout so nothing overflows.

The naive approach — walk the runs with `python-pptx`, swap the text, save — fails four ways:
English is about twice as long as Chinese while the boxes are fixed; PowerPoint's `normAutofit`
is not honoured at export or by non-PowerPoint renderers, so nothing shrinks and text is simply
clipped; WPS hides whole bodies and tables inside `<mc:AlternateContent>`, which `python-pptx`
cannot see at all; and `tf.clear()` keeps the first paragraph's properties, so a cell that
carried automatic numbering renders a phantom "1.".

This skill packages the font-size computation, the neighbour-aware layout rebuild, the raw-XML
rewriting of hidden content, and a full verification suite — distilled from translating an
eleven-chapter, 900-page semiconductor packaging textbook deck.

Install by cloning into `~/.claude/skills/`, then ask Claude to translate a deck.
Requires `python-pptx`; `Pillow` and a local PowerPoint install are used for render checks.
Documentation is in Chinese.
