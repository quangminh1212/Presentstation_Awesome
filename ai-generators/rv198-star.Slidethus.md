# Slidethus v0.8.1+stability.20260906 — Evidence-backed Presentation Engineering

从一个主题到一套有依据、有设计的 PPT。

## 小米 YU7 · 产品介绍

![小米 YU7 产品介绍封面](docs/showcase/yu7-cover.png)

![小米 YU7 续航对比数据页](docs/showcase/yu7-range.png)

## 中国酒店业香薰市场 · 低奢研究报告

![中国酒店业香薰市场研究报告封面](docs/showcase/hotel-scent.webp)

## 五一旅游消费 · 调研报告

![五一旅游消费调研封面](docs/showcase/mayday-cover.png)

案例来自不同阶段的真实任务，并非同一版本的统一验收集。[案例说明与素材出处](docs/showcase/README.md)

## 开始使用

当前为 v0.8.1 基线上的本地稳定性修复版；新增可读策划稿、跨进程续跑修复和受限图片底图。实际验收结论见[执行记录](plans/2026-09-06-v081-stability-rebuild.md)。历史成品不代表本修复版已通过验收。

从本地修复构建安装 Wheel，然后：

```bash
python -m pip install slidethus-0.8.1+stability.20260906-py3-none-any.whl
slidethus plugin install-skill /absolute/path/to/project
```

在支持技能的 Agent 中直接说：

> 使用 $using-slidethus，制作一份介绍小米 YU7 的 PPT。

[发布说明与能力边界](release/v0.8.1.md) · [工作流程](docs/03-workflow-state-machine.md) · [架构](docs/02-architecture.md) · [开发路线](TASKS.md)

包版本：`0.8.1+stability.20260906` · 本轮验证 Python 3.11 · [Apache-2.0](LICENSE)

<details>
<summary>版本与能力边界</summary>

Slidethus 不是生产级端到端 PPT 产品（此处特指内置全部搜索、模型、图像和审阅供应商的一体化产品）；外部能力缺失时必须显式降级或阻断。

既有工程验收记录保持：M2 Exit Gate：PASS（2026-08-27）；M3 Exit Gate：PASS（2026-08-27）；M4 Exit Gate：PASS（2026-08-28）；M5 Exit Gate：PASS（工程边界，2026-08-29）。这些工程边界不等同于本修复版已通过稳定性或发布验收。M6.6 尚未完成，不声明 v1.0 发布就绪。外部工具依赖（capability boundary）与 Office 验收限制见[发布说明](release/v0.8.1.md)。

</details>

案例图片不按代码许可证再授权，第三方权利见[说明](THIRD_PARTY_NOTICES.md)。
