[English](README.md) | [简体中文](README.zh-CN.md)

# ScholarSkill

> This project is currently in the testing stage. Star it, try it, and feel very welcome to share suggestions and feedback.

![ScholarSkill teaser](assets/teaser-owl-final.png)

<p align="center">
  <strong>Build a living research knowledge system in Obsidian.</strong><br/>
  An OpenClaw skill for structured paper reading, knowledge linking, cognitive revision, and critical thinking.
</p>

<p align="center">
  <a href="en/SKILL.md">English Skill Docs</a> ·
  <a href="zh-CN/SKILL.md">中文技能说明</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#core-strengths">Core Strengths</a>
</p>

<p align="center">
  <img alt="OpenClaw Skill" src="https://img.shields.io/badge/OpenClaw-Skill-1f2937?style=flat-square">
  <img alt="Obsidian Workflow" src="https://img.shields.io/badge/Obsidian-Knowledge%20Workflow-6d28d9?style=flat-square">
  <img alt="Bilingual Repo" src="https://img.shields.io/badge/Docs-English%20%2F%20中文-0f766e?style=flat-square">
  <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-b45309?style=flat-square">
</p>

ScholarSkill is an Obsidian-centered academic reading workflow for OpenClaw. It is designed for more than paper collection and note dumping: the goal is to help an agent read papers, extract durable knowledge, connect new ideas to an existing knowledge base, and keep that knowledge system evolving over time.

## Why It Feels Different

Many academic assistants stop at search, summarization, or note capture. ScholarSkill is designed around the next step: turning paper reading into an evolving knowledge workflow inside Obsidian.

- It turns reading into structured notes instead of one-off summaries
- It connects new papers to existing notes and knowledge maps
- It supports revising older understanding as new evidence appears
- It encourages comparison, verification, and critical reflection
- It is built for a research workflow that keeps getting stronger over time

## Installation

### Quick Start

If you want the simplest path, clone the repository locally, open that workspace in OpenClaw, and let the agent finish the setup for you.

Example flow:

```bash
git clone https://github.com/EESJGong/scholar-skill.git
cd scholar-skill
```

Then ask the OpenClaw agent to finish the install, for example:

```text
Please install this repository as an OpenClaw skill, use the Chinese package, and configure it for my Obsidian vault at /your/Obsidian/Vault.
```

or:

```text
Please install this repository as an OpenClaw skill, use the English package, and configure it for my Obsidian vault at /your/Obsidian/Vault.
```

The agent can then place the repository into the correct `skills` directory, pick `zh-CN/` or `en/`, and run the matching `configure.py` with `--vault-path`.

That is the complete quick-start path.

### Manual Install and Detailed Setup

If you prefer to install and configure everything yourself, follow the detailed flow below.

### Step 0: Choose your language package first

This repository ships as two parallel packages:

- `en/`: English workflow, docs, and templates
- `zh-CN/`: Simplified Chinese workflow, docs, and templates

After cloning the repository, always start from the package you want to use, then run that package's setup script with an explicit vault path:

```bash
# English package
python en/scripts/configure.py auto --vault-path "/your/Obsidian/Vault"

# Simplified Chinese package
python zh-CN/scripts/configure.py auto --vault-path "/你的/Obsidian/Vault"
```

Passing `--vault-path` from the start avoids accidentally configuring the wrong vault and keeps templates separated under `9-Templates/en/` or `9-Templates/zh-CN/`.

### Option 1: Clone into the shared skills directory

Use this if you want ScholarSkill to be available across OpenClaw workspaces on the same machine.

```bash
mkdir -p ~/.openclaw/skills
git clone https://github.com/EESJGong/scholar-skill.git ~/.openclaw/skills/scholar-skill

openclaw skills info scholar-skill
openclaw skills check
```

### Option 2: Clone or copy into a specific workspace

Use this if you want ScholarSkill to exist only inside one OpenClaw workspace.

```bash
mkdir -p <your-workspace>/skills
git clone https://github.com/EESJGong/scholar-skill.git <your-workspace>/skills/scholar-skill
```

Or, if you already downloaded the folder:

```bash
cp -R scholar-skill <your-workspace>/skills/
```

Then verify it:

```bash
cd <your-workspace>
openclaw skills list --eligible
openclaw skills info scholar-skill
openclaw skills check
```

### Install dependency skills with ClawHub

`clawhub install` installs into `./skills` under your current working directory, so run it from the location where you want the dependencies to live.

For shared installation:

```bash
cd ~/.openclaw
clawhub install obsidian-direct
clawhub install obsidian-cli
clawhub install arxiv-watcher
clawhub install academic-research-hub
clawhub install tavily
clawhub install pdf
clawhub install durable-task-runner
```

For workspace-scoped installation:

```bash
cd <your-workspace>
clawhub install obsidian-direct
clawhub install obsidian-cli
clawhub install arxiv-watcher
clawhub install academic-research-hub
clawhub install tavily
clawhub install pdf
clawhub install durable-task-runner
```

After the manual install is complete, start a new OpenClaw session so the new skills are picked up.

## Core Strengths

### Structured Notes

ScholarSkill turns a paper into more than a summary paragraph. It helps produce organized reading notes, extracted insights, reusable knowledge units, and a clearer record of what the paper actually contributes.

Instead of leaving the result as a one-off chat response, the workflow is designed to create notes that can be revisited, expanded, and linked later inside Obsidian.

### Knowledge Network

ScholarSkill treats every new paper as part of a larger research context. New notes can be linked to existing topics, prior papers, domain concepts, and maps of content, so the vault grows as a network rather than a folder of isolated documents.

This makes it easier to see how ideas relate, where a new paper fits, and which parts of an existing knowledge base should be updated or expanded.

### Cognitive Update

ScholarSkill is built around the idea that research understanding should evolve. When a new paper introduces stronger evidence, a better framing, or a contradiction to earlier notes, the workflow encourages revising older understanding instead of simply appending more information.

That makes the knowledge base progressively sharper over time, rather than larger but harder to trust.

### Critical Thinking

ScholarSkill is not meant to passively record papers. It supports comparing claims, checking evidence, spotting assumptions, and asking whether a conclusion is actually well supported.

The goal is to make the reading process more evaluative and research-oriented, so the resulting knowledge system reflects judgment rather than just accumulation.

## What It Supports

### Literature Reading and Note Building

Use ScholarSkill to turn individual papers into structured notes that are easier to search, compare, and reuse later.

### Memory Extraction for Long-Term Knowledge

Capture semantic, episodic, and procedural memories so the system preserves not only what a paper says, but also what was learned from reading it and what can be reused in future work.

### Obsidian-Native Knowledge Growth

Keep the output inside an Obsidian vault, where notes, concept pages, and MOCs can evolve together instead of being trapped in disconnected chat logs.

### Ongoing Research Understanding

Support workflows where reading a new paper can refine topic understanding, reveal gaps, or trigger updates to older notes and interpretations.

### Verification-Oriented Research Workflows

Fit research processes that care about comparison, evidence checking, and synthesis instead of stopping at summarization.

## Repository Structure

This repository is split into two parallel language packages:

- [en/](en/README.md): complete English package
- [zh-CN/](zh-CN/README.md): complete Simplified Chinese package

```text
scholar-skill/
├── README.md
├── README.zh-CN.md
├── SKILL.md                # repository entry
├── requirements.txt
├── en/                     # full English package
└── zh-CN/                  # full Simplified Chinese package
```

## Getting Started

Start from the language-specific package you want to use:

- English package entry: [en/SKILL.md](en/SKILL.md)
- Chinese package entry: [zh-CN/SKILL.md](zh-CN/SKILL.md)

Shared repository files remain at the root:

- [LICENSE](LICENSE)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CHANGELOG.md](CHANGELOG.md)
- [requirements.txt](requirements.txt)

## Suggested Reading Order

1. Read the package-level [README](en/README.md) or [中文版说明](zh-CN/README.md)
2. Open the package-level [SKILL.md](en/SKILL.md) or [中文版 SKILL.md](zh-CN/SKILL.md)
3. Run the setup guide in the corresponding package
4. Install the required dependency skills and connect your Obsidian vault
