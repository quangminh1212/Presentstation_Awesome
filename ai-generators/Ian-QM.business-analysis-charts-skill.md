<div align="center">
  <p><strong>简体中文</strong> · <a href="README_EN.md">English</a></p>
  <img src="assets/icon.png" width="160" alt="咨询风数据分析图表图标">

# 咨询风数据分析图表

**把 Excel / CSV 数据，一条命令变成适合 PPT 的中文咨询风图表。**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Charts](https://img.shields.io/badge/Charts-10-red)
![Themes](https://img.shields.io/badge/Themes-4-darkgreen)

中文经营分析图表 Skill · 10 种图表 · 4 套咨询风主题 · 3200×1800 高清输出
</div>

## 它解决什么问题

普通绘图库能画图，但很难直接产出可放进经营分析和管理汇报的成品。本 Skill 将数据校验、图型选择、Action Title、中文字体、数据标签、参考线、主题配色和 16:9 PPT 版式整合为一套可重复执行的流程。

- 自动生成与数据一致的结论型标题
- 支持中文字体回退，不因运行环境不同而乱码
- 自动处理万/亿缩放、百分数与缺失值
- 重点数据单点强调，减少无意义的彩色堆叠
- 默认输出 `3200×1800`、`dpi=200` 的 PNG，也支持 SVG
- 内置示例均已脱敏，只使用“销售额”“渠道A/B/C”等中性术语

## 效果预览

### 贝恩红 · 分类对比

![贝恩红柱状图](assets/previews/bar-bain.png)

### 麦肯锡蓝 · 趋势分析

![麦肯锡蓝折线图](assets/previews/line-mckinsey.png)

### 波士顿绿 · 热力矩阵

![波士顿绿热力图](assets/previews/heatmap-bcg.png)

### 默认蓝 · 变动归因

![默认蓝瀑布图](assets/previews/waterfall-default.png)

## 支持范围

| 图表类型 | `chart_type` | 适用场景 |
|---|---|---|
| 折线图 | `line` | 时间趋势、关键节点 |
| 柱状图 | `bar` | 分类对比、基期与本期 |
| 横向条形图 | `horizontal_bar` | 排名、长标签、多分类 |
| 漏斗图 | `funnel` | 连续转化链路 |
| 双 Y 轴图 | `combo` | 规模与增速 |
| 堆叠柱状图 | `stacked_bar` | 总量与结构变化 |
| 气泡四象限图 | `bubble` | X/Y 定位与规模 |
| 瀑布图 | `waterfall` | 总量变动归因 |
| 热力图 | `heatmap` | 行×列密度矩阵 |
| 饼图 / 环形图 | `pie` / `donut` | 用户明确要求的占比图 |

主题：`default`（默认蓝）、`mckinsey`（麦肯锡蓝）、`bcg`（波士顿绿）、`bain`（贝恩红）。

## 安装

### 作为 Codex Skill 使用

```bash
git clone https://github.com/Ian-QM/business-analysis-charts-skill.git \
  ~/.codex/skills/business-analysis-charts-public
```

重新打开 Codex 后，可以直接描述需求，例如：

> 用贝恩红画一张各渠道销售额本期与基期对比图，突出增速最高的渠道。

### 作为独立 Python 工具使用

```bash
git clone https://github.com/Ian-QM/business-analysis-charts-skill.git
cd business-analysis-charts-skill
python3 -m pip install -r requirements.txt
python3 scripts/render_chart.py \
  --input assets/sample-inputs/bar.json \
  --theme bain \
  --output chart.png
```

输入格式和字段说明见 [`references/input-formats.md`](references/input-formats.md)。

## 快速试跑

```bash
python3 scripts/smoke_test.py
```

测试会在临时目录中渲染全部 10 种图表，不会删除已有输出。

## 项目结构

```text
├── SKILL.md                 # Skill 入口与工作流
├── scripts/                 # 统一渲染入口与各图型实现
├── references/              # 图型、配色、输入与版式规范
├── assets/sample-inputs/    # 脱敏示例数据
└── assets/previews/         # README 效果预览
```

## 设计原则

1. 先判断数据关系，再选择图型。
2. Action Title 必须由数据支持，不能编造结论。
3. 普通系列使用偏深色，关键对象使用同色系亮色。
4. 单张图只突出一个最重要对象。
5. 饼图不作为默认选择，占比优先使用堆叠柱或横向排名。

## 参与贡献

欢迎提交 Issue 分享真实使用场景，也欢迎通过 Pull Request 增加经过验证的图型、输入适配或排版改进。如果这个项目对你的汇报有帮助，欢迎点一个 ⭐，让更多需要中文经营分析图表的人看到它。

## License

[MIT](LICENSE)
