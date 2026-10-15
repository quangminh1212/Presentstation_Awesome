# Chris's AI Stack

> Workspace-native AI brain. [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) wired into Google Workspace via 31 MCP servers, 19 reusable skills, 125 memory files, 7 cron jobs, and a Telegram bot for mobile. ~150 EUR/month all-in. ~23 hours per week saved on a tracked sample. Replaces ~1.5 FTE that would have cost 80-110k EUR/year.

This is the public, fork-friendly slice of my actual production setup. Built over multiple business contexts (advisory, real estate, ventures, content, ops). The premise: instead of hiring the team I'd have hired after my last exit, I bet that AI as infrastructure could replace it. Four years in, that bet is still the strategy.

**🇩🇪 Auf Deutsch hier:** Schritt-für-Schritt von null bis laufendes Brain: [`SETUP_DE.md`](SETUP_DE.md). Die Slides zum Talk "Tool Overload & Setup Trap" (#BCD, Juni 2026): [chris1928a.github.io/erler-ventures/talks/2026-06-12-bcd](https://chris1928a.github.io/erler-ventures/talks/2026-06-12-bcd/)

---

## What's in this repo

| Folder / File | What it is |
|---|---|
| [`SETUP_DE.md`](SETUP_DE.md) | 🇩🇪 Die deutsche Anleitung zum Copy-Pasten: Folder-Struktur + Terminal-Schritte, von null bis laufendes Brain. Begleitet den Talk "Tool Overload & Setup Trap". |
| [`SETUP.md`](SETUP.md) | The full architecture spec. 4-Layer Brain, the 31 MCP servers, the 7 cron jobs, the Anti-AI voice rules, the cost story, the 30-day rollout plan, the troubleshooting guide. ~430 lines. Start here. |
| [`slides.html`](slides.html) | The 44-slide deep dive. Body-mapped tour of every layer, every tool. Open in any browser, arrow keys to navigate, print as PDF if you want. |
| [BCD talk slides](https://chris1928a.github.io/erler-ventures/talks/2026-06-12-bcd/) | 🇩🇪 "Tool Overload & Setup Trap", the 20-slide German talk: Second Brain to Company Brain, real costs, governance, autonomy tiers. |
| [`skills/`](skills/) | 8 forkable Claude Code Skills. Each one is a complete `SKILL.md` (~280-380 lines) plus `prompts/`, `examples/`, and `scripts/` subfolders. Drop in `~/.claude/skills/` and go. |
| [`templates/`](templates/) | Foundation files for any Claude Code project: `CLAUDE.md.template`, memory file templates (user, voice, channels, hats, curator rules). Fork these first, takes 15 minutes. |
| [`glossary.md`](glossary.md) | Plain-English definitions for Claude Code, MCP, Skills, Hooks, Memory, ZDR, EU AI Act, and 30+ other terms. For anyone newer to the stack. |

---

## Who this is for

- You operate across multiple domains (advisory, real estate, ventures, content, ops) and want one brain that understands all of them
- You live inside Google Workspace and want AI everywhere, including mobile
- You can pay ~150 EUR/month for the convenience
- You'd rather invest 30-60 hours up-front to own the setup forever than buy a vertical SaaS

If you want a complete opinionated Life OS out of the box, look at [Daniel Miessler's PAI](https://github.com/danielmiessler/Personal_AI_Infrastructure) instead.

---

## The 30-second pitch

```
PRIVATE BRAIN ARCHITECTURE (4 layers)

Layer 4 — Body                     Telegram bot · 31 MCP servers · 7 crons
Layer 3 — Working Memory           Claude Code on AWS Lightsail Frankfurt
Layer 2 — Short-term Memory        125 .md files routed by ~50-line CLAUDE.md
Layer 1 — Long-term Memory         GitHub + Notion + Drive
```

The numbers, tracked over 8 weeks:

| Component | Count |
|---|---|
| MCP servers | 31 |
| Skills (universal + domain) | 19 |
| Memory files | 125 |
| Cron jobs | 7 |
| Hours saved per week | ~23 |
| Total monthly cost | ~150 EUR all-in |
| Replaces | ~1.5 FTE (80-110k EUR/yr at DACH rates) |
| Cost ratio | ~45-60x cheaper |

Full breakdown in [SETUP.md](SETUP.md).

---

## The 8 skills

Five universal (fork as-is, edit personal data) + three domain examples (show the pattern, adapt to your vertical).

### Universal

| Skill | What it does | Tracked time saved |
|---|---|---|
| [`/morning-brief`](skills/morning-brief/) | Daily 7am brief: inbox top 3, calendar, open threads | 2.25h/week |
| [`/diarize-person`](skills/diarize-person/) | 1-page stakeholder dossier with full history | (5.7h/wk meeting prep) |
| [`/draft-by-channel`](skills/draft-by-channel/) | Voice-locked drafts per recipient + channel | 2.7h/week |
| [`/weekly-review`](skills/weekly-review/) | Friday 7-day review across all "hats" | 1.3h/week (90→10 min) |
| [`/memory-curator`](skills/memory-curator/) | Weekly memory hygiene cron | maintenance |

### Domain examples

| Skill | For who | Pattern to copy |
|---|---|---|
| [`/audit-process`](skills/audit-process/) | Advisors / COOs / ops consultants | Diagnostic + Impact-Effort matrix + top-3 |
| [`/sales-script-rewriter`](skills/sales-script-rewriter/) | Sales founders / SDR managers | Transcript-in + 6-dim score + rewritten section |
| [`/property-pricing`](skills/property-pricing/) | Real estate / daily-priced goods | API-in + decision-out + daily cron |

---

## Quick start (5 minutes to a working brain)

```bash
# 1. Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# 2. Clone this repo
git clone https://github.com/chris1928a/chris-ai-stack.git
cd chris-ai-stack

# 3. Fork the templates into your Claude config
mkdir -p ~/.claude/projects/my-brain/memory
cp -r templates/memory-templates/* ~/.claude/projects/my-brain/memory/
cp templates/CLAUDE.md.template ~/.claude/projects/my-brain/CLAUDE.md

# 4. Fork the morning-brief skill
cp -r skills/morning-brief ~/.claude/skills/

# 5. Open a Claude Code session
cd ~/.claude/projects/my-brain && claude
```

Then in Claude Code: edit `memory/user_about.md` (5 min, the highest-impact file you'll write) and type `/morning-brief` to test.

For the full path with MCP servers, cron jobs, and Telegram, see [SETUP.md](SETUP.md).

---

## Anti-AI voice rules

Every output that sounds like AI degrades trust. The voice rules baked into all skills:

**Banned:** delve, leverage, unlock, harness, synergy, robust, seamless, em-dashes, "I hope this finds you well", mega-paragraphs, "happy to help", "great question".

**Required:** direct + terse, German Umlauten always, Sie-Form for PE / corporate counsel, Du-Form for founders / peers, one concrete number per outreach, first-name sign-off in DMs, full sign-off block only in formal external emails.

Full template at [`templates/memory-templates/feedback_voice.md`](templates/memory-templates/feedback_voice.md). Fork it, fill in your own examples.

---

## Background

This stack came out of three years of building, ripping, and rebuilding personal AI infrastructure. v1-v3 are dead (ChatGPT-only, Notion+Zapier, multi-tool-no-architecture). Only v4 (Workspace-native) and v5 (local-first variant) survived.

Most of the public material — the 44-slide deep dive, the 8 skill specs, the 30-day rollout plan, the cost honest breakdown — was originally prepared for a private operator session in May 2026. This repo extracts the parts that are useful regardless of context, with all event-specific framing and other operators' setups removed.

If you want the broader version with two other operator paths (Dom's local-first + Fabian's PAI Life OS), audience pain analysis, and 11 documented solutions to common pain clusters, the full source is at [github.com/chris1928a/eo-ai-exchange](https://github.com/chris1928a/eo-ai-exchange).

---

## Contact

[Christoph Erler](https://erlerventures.org) · Founder, Erler Ventures
chris@erlerventures.org · [linkedin.com/in/christopherler](https://www.linkedin.com/in/christopherler/)

Open issues for questions, suggestions, or "this broke for me" reports: [github.com/chris1928a/chris-ai-stack/issues](https://github.com/chris1928a/chris-ai-stack/issues)

---

## License

MIT. Fork it, modify it, share it. Attribution appreciated, not required.

---

*Last updated: 2026-05-14.*
