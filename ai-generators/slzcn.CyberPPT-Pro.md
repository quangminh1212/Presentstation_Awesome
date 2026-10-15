# CyberPPT-Pro

咨询风格 PPT 生成 Skill，基于 [CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) 重构。
一套共享核心逻辑，双平台适配（Claude / Codex）。

## 相对原版的改进

| 维度 | 原版 CyberPPT | CyberPPT-Pro |
|---|---|---|
| 可编辑性 | 混合还原（底图+文字层），图表不可编辑 | **默认全原生可编辑**（文本/形状/原生图表/表格），混合轨降为可选 |
| 样张/蓝图 | 依赖 ImageGen 生成图片蓝图 | **HTML 样张**，零图像生成依赖，跨平台一致 |
| 输入 | 以文本素材为主 | 三类混合输入：文档数据 / **旧PPT与截图还原** / 一句话需求（AI调研补充） |
| 确认门 | 固定多门+逐页验收，交互很重 | **自适应门禁**：按页数/复杂度评分自动增减确认点，支持快速/严格模式覆盖 |
| 主题 | 8 种视觉风格 | **双层主题**：12 种视觉风格 + 10 个场景内容框架（行业研究/尽调/增长/CRM生命周期等） |
| 平台 | Codex 单平台 | core 共享逻辑 + claude/ 与 codex/ 各一份轻适配层 |

## 目录结构

```
CyberPPT-Pro/
├── core/                      # 平台无关核心逻辑
│   ├── PIPELINE.md            # 五阶段流水线总纲
│   ├── INGEST.md              # 混合输入转换规范（含PPT/截图还原）
│   ├── GATES.md               # 自适应确认门禁（复杂度评分模型）
│   ├── RENDER.md              # 双轨渲染规范（原生轨/混合轨 + CJK实践）
│   ├── QA.md                  # 三层质检清单
│   ├── styles/STYLES.md       # 12 种咨询视觉风格 token 库
│   └── frameworks/FRAMEWORKS.md # 10 个场景框架（页面骨架）
├── claude/SKILL.md            # Claude 适配层（claude.ai / Claude Code / Cowork）
├── codex/SKILL.md             # Codex 适配层（CLI / Cloud）
└── examples/
    └── sample-preview.html    # 风格样张示例（门C 交付形态）
```

## 安装

**Claude**：claude.ai 上传 `claude/SKILL.md` 所在目录为自定义 skill（需连同 `core/` 一起打包）；
Claude Code 放入 `~/.claude/skills/consulting-ppt/`。

**Codex**：仓库放入项目目录，在 `AGENTS.md` 添加：
`制作 PPT / 演示文稿相关任务时，读取并遵循 CyberPPT-Pro/codex/SKILL.md`。

## 核心流程

```
摄取 ─► 证据表+故事线(SCR/场景框架) ─► HTML样张选风格 ─► HTML预览全稿 ─► 原生PPTX ─► 三层QA ─► 交付
```

确认点数量由复杂度评分（页数/输入明确度/数据密度/任务类型）自动决定：
轻量档 1 个合并确认，标准档 3 门 + 一次验收，严格档追加分批验收。

## 交付物

- `output.pptx` — 全元素可编辑
- `preview.html` — 逐页预览，二次修改沟通的基准
- 待核实数据清单 — AI 补充的数据逐条列出（如有）

## License

MIT
