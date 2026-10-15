# Screencast Slides v3

把技术教程或知识科普逐字稿转换为 1280×720 单文件 HTML 演示。成品包含舞台、联动提词器、在线文字/notes 编辑、图片替换与缓存隔离。

## 设计原则

- 逐字稿是内容主线：事实、主张、步骤、因果、条件、数字、命令和结论必须对应。
- 视觉不是逐词贴标签：构图、媒介、节奏、图内必要文字和环境细节可由 AI 自主设计。
- 第一页必须展示整份演示标题；并列问题保持同级视觉权重，不能拆成大标题与小副标题。
- 不提供视觉参考模板。`assets/runtime-shell.html` 只承担渲染、交互与安全能力，`tests/fixtures/` 只用于测试。
- 只有事实错误、关键逻辑跳步或教程必需信息缺失才先补稿；“不好配图”属于设计问题，不阻断制作。
- 字符数、秒数、字号和版式映射是启发式；安全、事实、真实 UI、无裁切和交互正常是硬合同。

v3 只接受 `schemaVersion: "3.0"`，不兼容 v2 avatar/safeArea。`theme` 指定打开时的默认主题，成品可通过工具栏或 `T` 键在 `keynote`、`terminal`、`notebook` 之间切换。用户口中的“PPT”在本 Skill 中指 HTML 演示；不导出 PPTX/PDF，不做竖屏。

## 构建

```bash
python3 scripts/validate_deck.py path/to/deck.json
python3 scripts/build_deck.py path/to/deck.json -o path/to/output.html
python3 scripts/qa_static.py --built path/to/output.html
```

不要手改输出 HTML 绕过 schema。静态检查后仍需在真实浏览器 1280×720 下逐页检查全部 reveal 状态和交互。

## v3 可控表达空间

- 16 个语义 layout 和受支持 composition 提供安全的结构化渲染。
- Deck 级 `design` 可选 `density`、`surface`、`progress`；slide 可选 `emphasis`。
- compare 允许左右项目数量不同，`tone` 可为 neutral、contrast 或 problem-solution。
- media 分栏可用独立 `insights`；callout 只负责图片目标，不再被迫充当侧栏。
- `visualIntent` 按资产风险选填；简单、用户提供且用途明确的图片无需填完整五项。
- `aspectRatio` 可省略、使用 `auto` 或任意合法 W:H，包括竖图。
- 图片可以包含必要、准确、可读的 UI 文字、短标签、编号和方向词。
- 面向中文观众时，生成图中的解释性文字默认使用中文；每张图先从稿段关系和前后文推导，再生成和验收。

不开放任意 HTML、CSS、SVG 或每页随机换肤。真实截图不得用生成式假 UI 代替；本地 asset 仍受路径、类型、体积与脚本安全校验。

## 交互

- `P` 打开提词器；舞台与提词器联动翻页。
- `E` 编辑舞台文字；notes 在提词器中编辑。
- `H` 隐藏工具条；支持全屏、重置和刷新后保留。
- 缓存按 `deckId + revision` 隔离。
- 无 callout 图片可本地替换；带 callout 图片必须回到 deck.json 重新标定。

详细工作流见 `SKILL.md`，字段见 `references/slide-schema.md`，交付判断见 `references/checklist.md`。
