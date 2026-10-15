# OpenKitty Skills

OpenKitty 社区技能仓库。**173 个 SKILL.md，218 个 Python 脚本，21 个类目，26MB。**

## 使用方式

```bash
git clone https://github.com/niqinggood/openkitty-skills.git
```

在 `openkitty-config.yaml` 中配置：

```yaml
agents:
  - name: Researcher
    external_skills:
      - ./openkitty-skills   # GitHub 同步的社区技能
      - ./skills              # 你自己的定制技能（优先）
```

更新：`cd openkitty-skills && git pull`

## 类目

| 目录 | 内容 | 数量 |
|------|------|------|
| `business-finance/` | 投资框架、量化数据、AlphaEar 实时财经、选股、组合管理 | 40+ |
| `research/` | 学术研究、论文写作/审稿/润色、数据分析、统计、基金申请 | 25+ |
| `documents/` | PDF/DOCX/Markdown 转换、提取、编辑 | 7 |
| `presentation/` | PPT 生成、LaTeX 海报、HTML 演示 | 12+ |
| `coding/` | 代码开发、调试、TDD、code review | 5 |
| `devops/` | 部署、监控、K8s、ML 工程 | 8 |
| `design/` | Web 设计、审美系统 | 4 |
| `web-tools/` | 多引擎搜索、浏览器自动化、网页抓取 | 6 |
| `content-creation/` | 内容创作、Moltbook | 2 |
| `media/` | 语音识别、OCR、截图 | 4 |
| `legal/` | 合同审查、法律助手 | 2 |
| `teamwork/` | 团队协作、Agent 编配 | 4 |
| `skill-tools/` | 技能创建/审查工具 | 2 |
| 其他 | memory, monitoring, nova-community, obsidian-sync, sendmail, spike, dhdna-profiler, life-note | 各 1-3 |

## Skill 格式

每个 Skill 是一个目录，包含 `SKILL.md`：

```
my-skill/
  SKILL.md          # 必需：技能定义+指令
  scripts/          # 可选：Python/Shell 脚本
  references/       # 可选：参考文档
```

## 贡献

1. Fork 本仓库
2. 在对应类目下创建新 skill 目录
3. 提交 PR

Skill 必须有清晰的 name + description + 使用场景 + IRON RULES。

## 许可

MIT
