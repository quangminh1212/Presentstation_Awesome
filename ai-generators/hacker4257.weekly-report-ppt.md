# git-report-skill

> 基于 Git 仓库变更，自动生成「程序员周报 / 迭代汇报 / PPT 汇报大纲」的 Claude Skill。

`git-report-skill` 是一个面向程序员的 Claude Code Skill。  
它通过**扫描 Git 仓库的真实代码变更**（提交、文件、diff 统计），
自动整理为**按功能/模块归类**的工作汇报内容，适合向技术负责人或管理者汇报。

---

## ✨ 功能特点

- 🔍 扫描 Git 提交记录、变更文件、代码增删统计
- 🧩 按「功能 / 业务模块」而非文件名进行归类
- 📝 自动生成领导可读的文字版周报
- 📊 输出可直接制作 PPT 的汇报大纲
- 🔒 只读扫描，不修改任何代码或仓库状态
- 🧠 基于 Claude Code Skills 机制设计，可复用、可扩展

---

## 📁 项目结构

```text
git-report-skill/
├── SKILL.md                     # Claude Skill 核心规则
├── scripts/
│   ├── scan_repo.sh             # Git 仓库扫描脚本（只读）
│   └── summarize_changes.py     # 按功能归类变更文件
├── config/
│   └── feature_map.example.yml  # 功能/模块映射示例
├── README.md
└── LICENSE
