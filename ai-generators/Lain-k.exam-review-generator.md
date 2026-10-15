# exam-review-generator

把课程 PPT、PDF、Word、图片等资料自动整理成期末复习资料的 AI Skill。

`exam-review-generator` 面向真实课程资料场景，而不是简单摘要场景。它适合处理多份课件、重复知识点、混合格式文件、扫描件，以及不同复习目标下的复习资料生成需求。

## 它能做什么

- 把课程资料整理成一份可直接复习的期末资料，而不是只做浅层总结
- 支持 `A / B / C` 三档输出，适配不同时间压力和基础水平
- 合并多份资料中的重复内容，并保留来源追踪
- 标出高频考点、易混点、公式、流程和答题模板
- 生成练习题、解析、冲刺计划和速记版内容
- 支持 `.ppt`、`.pptx`、`.pdf`、`.docx`、图片、压缩包等常见课程资料格式

## 适合谁用

- 手里有很多课件，但没有成体系复习资料的学生
- 临近考试，想快速整理救命小抄的学生
- 听过课，但需要系统梳理知识框架的学生
- 基础薄弱，想要一份从 0 突击版自学讲义的学生

## 三种输出档位

### A 档：考前救命版

适合“明天就考试”“越短越好”的场景。

- 1 到 3 页
- 极简小抄风格
- 只保留核心考点、必背概念、公式、答题模板和高频题

### B 档：系统复习版

默认档位，适合常规期末复习。

- 分章节整理
- 包含重点、难点、公式、对比表、答题模板和练习题
- 适合 3 到 7 天的系统复习

### C 档：零基础突击版

适合“没听懂课”“不想再翻 PPT”“只看文档也要学会”的场景。

- 自学教材型输出
- 先讲人话，再给标准术语和答题表述
- 补全例题、练习题、易错点和学习计划
- 目标是尽量脱离原课件完成复习

## 这个 Skill 和普通总结 Prompt 的区别

很多 AI 学习工具会做总结、问答、卡片和测验，但这个 Skill 的重点是：

- 先确认考试范围、题型、输出格式和详细程度，再开始生成
- 先盘点文件，再抽取内容，再整合生成，避免漏读和乱写
- 对旧版 `.ppt`、扫描件、模糊图片等高风险输入显式标注不确定性
- 要求关键内容保留来源信息，而不是只给结论
- 不只整理知识点，还必须包含题目、解题思路和答题模板
- `C 档` 不是写得更长的提纲，而是一份能拿来直接自学的复习讲义

## 典型用法

```text
Use $exam-review-generator to turn these course files into a B-mode final review guide.
```

```text
我明天考试，帮我把这些课件整理成 A 档救命小抄。
```

```text
我完全没听懂这门课，用 C 档把这些 PPT 整成一份从 0 突击版复习资料。
```

```text
把这几个章节整理成考试复习笔记，带名词解释、简答题模板和计算题讲解。
```

## 工作流程

1. 确认档位、考试范围、题型、输出格式和特殊要求
2. 盘点并读取全部资料文件
3. 抽取文本、表格、重点样式和页级结构
4. 合并重复内容，处理冲突表述
5. 识别高频考点和高风险内容
6. 按指定档位生成复习资料
7. 按交付检查清单核对覆盖率、结构、练习题和来源追踪

## 固定输出结构

生成结果通常包含以下部分：

1. 资料来源说明
2. 复习档位与范围
3. 课程总览
4. 分章节复习
5. 高频对比表
6. 必背答题模板
7. 综合模拟训练
8. 冲刺计划与考场策略
9. 最终速记版

## 安装方式

把该 Skill 放到你的 agent skills 目录中，例如：

```text
~/.codex/skills/exam-review-generator
```

Windows 示例：

```text
C:\Users\<YourName>\.codex\skills\exam-review-generator
```

目录结构至少应包含：

```text
exam-review-generator/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── detail-levels.md
    ├── implementation-checklist.md
    ├── output-structure.md
    └── parsing-rules.md
```

## 使用建议

- 尽量上传完整课件，而不是零散截图
- 明确说明考试范围和不考范围
- 如果知道题型，最好一开始就告诉模型
- 真正需要“讲懂”的场景，直接用 `C 档`
- 内容过长时，允许拆成多个 Markdown 文件输出

## 局限性

- 扫描件、纯图片和模糊资料可能导致抽取不完整
- 旧版 Office 格式可能需要额外转换或本地解析支持
- 如果老师课件前后表述冲突，结果可能会保留一个版本并标注冲突
- 最终质量仍依赖原始资料是否完整

## 仓库定位

这个仓库提供的是一个可复用的 AI Skill，不是一个独立 App。

它更适合被理解为：

- 一个面向期末复习场景的工作流型 Skill
- 一个把课程资料转成考试复习资产的结构化提示包
- 一个强调来源追踪、档位控制和交付质量的复习资料生成器

## English Summary

`exam-review-generator` is an AI skill for turning course materials into structured exam review guides, cram sheets, practice sets, and zero-foundation study notes. It is designed for real multi-file courseware workflows, with traceable sources, fixed output structure, and different detail levels for different study situations.
