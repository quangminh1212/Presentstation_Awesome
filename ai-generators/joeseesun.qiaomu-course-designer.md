# qiaomu-course-designer

<p align="center">
  <a href="https://github.com/joeseesun/qiaomu-course-designer/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/joeseesun/qiaomu-course-designer?style=for-the-badge&logo=github" /></a>
  <a href="https://github.com/joeseesun/qiaomu-course-designer/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/joeseesun/qiaomu-course-designer?style=for-the-badge&logo=github" /></a>
  <a href="https://github.com/joeseesun/qiaomu-course-designer/issues"><img alt="Issues" src="https://img.shields.io/github/issues/joeseesun/qiaomu-course-designer?style=for-the-badge&logo=github" /></a>
  <a href="https://github.com/joeseesun/qiaomu-course-designer/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/joeseesun/qiaomu-course-designer?style=for-the-badge&logo=git" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge" /></a>
</p>

> 课程还没想清楚，AI 却已经给你写了 40 页大纲。
>
> `qiaomu-course-designer` 会先持续访谈你：每轮只问最值得问的设计问题，同时给出推荐答案、理由和取舍。它能保存决策来源、暂停后恢复、处理修正与冲突，并在上游变化时只重开真正受影响的设计。只有整门课程达成共识后，才进入课程稿、教案或 PPT。

```bash
npx skills add joeseesun/qiaomu-course-designer
```

**[中文](#中文) | [English](#english)**

## 交互预览

```text
你：我想做一门给产品经理的 AI 课，不断访谈我，每问给推荐答案。

AI：当前决策：课程承诺

这门课结束后，你最希望学员在真实工作中多做成哪一件事？

我的推荐：把终点设为“能独立设计、评估并迭代一个 AI 产品方案”，
而不是“了解 AI 产品”。

原因：前者可观察、可评量，也能反向决定后面需要哪些练习。
这会解锁：学习成果、作品证据和内容范围。
```

<a name="中文"></a>
## 中文

### 它解决什么

普通课程生成器很快，但往往过早假设了受众、课程目标、时长、评量方式和交付环境。当你后来改了其中一项，大纲、教案和 PPT 全都要重做。

这个 Skill 把课程设计建模为一张决策依赖图：

- 一次只问一个高价值问题，不丢一整页问卷。
- 每问必须给一个明确推荐，不把所有决定都推回给你。
- 上游决策改变时，自动找出并重开受影响的下游决策。
- 暂停、跨会话恢复或上下文压缩后，先恢复阶段与授权边界，不从头重问，也不凭记忆补答案。
- 用户修正历史时保留修正关系；事实、用户判断、模型推断和推荐不会混成一条“共识”。
- 你对某一问说“OK”，只锁定当前分支，不会被误解为整门课已定稿。
- 必须先展示完整课程蓝图，经你确认“整体 OK”后，才会讨论后续格式；选择格式只授权生成一个产物。

### 你会得到

- 一份可追溯的课程设计状态：来源、决定、假设、冲突、延期项、修正和授权边界。
- 课程承诺、学习者、成果、证据、范围、顺序、练习、评量和约束之间的依赖检查。
- 一份经你确认的课程蓝图，作为后续所有产物的单一依据。
- 共识后的优先产物建议：课程稿、教案、学员手册、练习包、评量包或 PPT。

### 安装

1. 确认本机可使用 Node.js 和 `npx`。当前 Skills CLI 1.5.22 声明需要 Node.js 22.20.0 或更高版本：

   ```bash
   node --version && npx --version
   ```

2. 安装 Skill：

   ```bash
   npx skills add joeseesun/qiaomu-course-designer
   ```

3. 确认可被 Skills CLI 发现：

   ```bash
   npx skills add joeseesun/qiaomu-course-designer --list
   ```

### 前置条件

- [ ] 已安装 Node.js 22.20.0 或更高版本；运行 `node --version` 检查。
- [ ] 使用 Codex、Claude Code 或其他支持 Agent Skills 的工具。
- [ ] 愿意通过多轮对话锁定设计；如果你只想立即生成 PPT，应使用专门的演示文稿 Skill。

运行本 Skill 不需要 API key、付费服务或网络权限。

### 你可以直接这样说

- “我有一个 AI 课程想法，请不断访谈我，直到我们整体达成共识。”
- “帮我逐个分支设计这个培训，每次问我一个问题并给推荐答案。”
- “这是一份半成品大纲，只追问还没有共识的部分，别重问已有答案的事。”
- “继续上次暂停的课程访谈，从保存的状态恢复，先告诉我哪些决定被重开了。”

### 什么情况不会触发

- 已定稿课程的 PPT 生成或美化。
- 纯排版、PDF 转换、翻译或摘要。
- 只解释“什么是逆向课程设计”等概念。
- 只要一份只读审查报告、书单或一次性课程大纲，不希望被访谈。
- 无需访谈的一次性大纲生成。

### 验证证据

- Package validation：通过，包含自包含包检查和 qiaomu-meta-skill 发布检查。
- Trigger evaluation：22/22 通过，0 误触，0 漏触。
- State-transition evaluation：13/13 通过，覆盖局部 OK、级联重开、冲突、暂停恢复、冻结、单一格式授权和冻结后修正。
- Unit tests：15/15 通过。
- Output fixtures：12 个对抗回归场景，覆盖上下文恢复、多节点回答、不确定性、假闭环和已冻结产物失效。

上述是本地契约与回归证据，不等于真实学习效果。试教数据、课程设计师盲评和长期学习转化仍是 `missing evidence`。

维护者可运行：

```bash
python3 scripts/validate_package.py .
python3 scripts/validate_state_transitions.py --cases evals/state_transition_cases.json --output reports/state-transition-eval.json
python3 ~/.agents/skills/qiaomu-meta-skill/scripts/validate_skill.py .
python3 ~/.agents/skills/qiaomu-meta-skill/scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 ~/.agents/skills/qiaomu-meta-skill/scripts/export_skill_ir.py . --output reports/skill-ir.json
python3 -m unittest discover -s tests -v
```

### 自动迭代发布

本仓库已固化维护约定：后续每轮优化完成后，必须先运行包验证、状态转换、触发评估、Skill IR、单元测试、secret 与公开声明检查。全部通过后，通过功能分支和 PR 发布，并重新执行远程发现与临时目录真实安装验证；禁止直推默认分支。详细规则见 [`AGENTS.md`](AGENTS.md)。

### Troubleshooting

| 问题 | 常见原因 | 解决方法 |
|---|---|---|
| `No valid skills found` | `SKILL.md` 未被正确发现或本地 CLI 缓存 | 先运行 `npx skills add joeseesun/qiaomu-course-designer --list`；再确认仓库根目录存在 `SKILL.md` |
| AI 一次问了很多问题 | 未完整加载 Skill，或对话中的要求与 Skill 冲突 | 明确说“使用 `$qiaomu-course-designer`，每轮只问一个问题” |
| 每次只问问题，却没有推荐 | 模型忽略了问题卡合约 | 要求当前问题必须包含“我的推荐”、理由和取舍 |
| 说一次 OK 就开始生成 PPT | 局部 OK 被误认为整体共识 | 要求显示完整蓝图快照；只有快照之后的“整体 OK”才能开启转制 |
| 改了受众却没重新讨论课程 | 下游决策未标记为 `reopened` | 要求重开成果、内容、顺序、练习、评量和媒介中受影响的节点 |
| 暂停后继续却从头再问 | 没有恢复课程设计状态 | 提供状态文件或已有蓝图，要求先恢复阶段、决策、冲突、延期项和授权边界 |
| 改了冻结蓝图却继续沿用旧 PPT | 没有撤销转制授权 | 要求把受影响产物标为 stale，重审相关分支并重新通过整体共识门 |

### 设计参考与原创边界

本 Skill 研究了：

- [`q-educator`](https://github.com/tyrealq/q-skills/tree/main/skills/q-educator)：学习“访谈前不生成”和逐产物审阅。
- [`course-outline-design`](https://github.com/kevintsai1202/teaching-site-skills/tree/main/course-outline-design)：学习课程骨架对下游产物的依赖与完成门。
- [`interview-me` / `syllabus`](https://github.com/pedrohcgs/claude-code-my-workflow/tree/main/.claude/skills)：学习多轮追问和分阶段 sign-off。
- [`adaptive-decision-interviews`](https://github.com/Michael-F-Bryan/skills/tree/main/skills/adaptive-decision-interviews)：学习证据来源、暂停恢复、修正历史、延期项和边际价值停止。
- [`plan-interview`](https://github.com/secondsky/claude-skills/tree/main/plugins/plan-interview/skills/plan-interview)：学习矛盾检测、开放问题追踪和按复杂度调整深度。
- [`educates-course-design`](https://github.com/educates/educates-course-design-skill)：学习按课程规模调整工作流、持续资源登记和既有课程接续。
- [Agent Skills Specification](https://agentskills.io/specification)：遵循标准 frontmatter、兼容性字段、渐进披露和资源引用规范。
- [Carnegie Mellon Eberly Center](https://www.cmu.edu/teaching/assessment/basics/alignment.html)：强化成果、评量和教学活动之间的对齐审计。

本 Skill 不复制上述项目表达。课程决策图、来源感知六状态模型、确定性级联重开、两段授权门、课程蓝图 revision 和状态转换回归，是针对课程共创场景的原创设计。

机器可读上游声明：`TyrealQ/q-skills; secondsky/claude-skills; educates/educates-course-design-skill; Michael-F-Bryan/skills; kevintsai1202/teaching-site-skills; pedrohcgs/claude-code-my-workflow`。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=joeseesun/qiaomu-course-designer&type=Date)](https://star-history.com/#joeseesun/qiaomu-course-designer&Date)

<a name="english"></a>
## English

`qiaomu-course-designer` is an interview-first Agent Skill for designing courses, workshops, training programs, and knowledge products.

Instead of generating a generic syllabus immediately, it asks one high-impact question at a time. Every question includes a concrete recommendation, rationale, trade-offs, and the downstream decisions it unlocks.

It tracks provenance and dependencies between audience, outcomes, evidence, scope, sequencing, practice, assessment, delivery constraints, and risks. It can pause, resume, recover from compacted context, preserve amendments, and reopen only the downstream decisions invalidated by an upstream change.

Most importantly, a local “OK” only approves the current branch. Course content, lesson plans, handbooks, and slides remain blocked until the user reviews the complete blueprint and explicitly approves the whole design. Freezing the blueprint opens format selection; selecting a format authorizes only that one artifact.

### Install

```bash
npx skills add joeseesun/qiaomu-course-designer
```

### Try it

- “Interview me until we agree on the course blueprint. Recommend an answer for every decision.”
- “Ask one question at a time and resolve dependencies before writing the course.”
- “Read this partial syllabus and only interview me about unresolved high-impact decisions.”

### Evidence boundary

The package currently passes 22/22 trigger cases, 13/13 deterministic state-transition cases, and 15/15 contract tests. Provider-backed multi-turn comparisons, expert blind review, and real learner outcome evidence remain missing evidence.

<!-- qiaomu-profile:start -->
## 关于向阳乔木

向阳乔木（乔向阳 / Joe）是一位实践型 AI 产品与内容创作者，长期把前沿 AI 变化转译成可复用的工作流、产品判断、AI 编程实践、AI 搜索实践和 GEO/AI 营销方法。

- 个人网站: https://qiaomu.ai
- 博客: https://blog.qiaomu.ai
- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/
- 微信公众号: 向阳乔木推荐看

### 支持与关注

| 打赏支持 | 微信公众号 |
|---|---|
| <img src="assets/qiaomu-profile/qiaomu_reward_qr.png" alt="向阳乔木打赏二维码" width="180" /> | <img src="assets/qiaomu-profile/qiaomu_wechat_public_account_qr.jpg" alt="向阳乔木推荐看公众号二维码" width="180" /> |
| 感谢支持乔木持续分享 AI 实践 | 扫码关注「向阳乔木推荐看」 |

<!-- qiaomu-profile:end -->

## License

MIT. See [`LICENSE`](LICENSE).

Copyright (c) 向阳乔木  
X: https://x.com/vista8  
GitHub: https://github.com/joeseesun/
