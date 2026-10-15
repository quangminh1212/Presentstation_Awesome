#!/usr/bin/env python3
# Split the monolithic README.md into per-category folders, each with its own README.md,
# and rewrite the root README.md into a compact index.
import os, re

ROOT = r"C:\Dev\PresentstationTool"
SRC = os.path.join(ROOT, "README.md")

# heading text -> folder name (only these categories are split out)
SPLIT = {
    "Featured": "featured",
    "AI Presentation Generators (end-to-end)": "ai-generators",
    "MCP Servers for Presentations": "mcp-servers",
    "Agent Skills, Plugins & Editor Extensions": "agent-skills",
    "HTML Slide Frameworks": "html-slide-frameworks",
    "Markdown \u2192 Slides (Marp / Quarto / Typst / Pandoc / Org / Reveal-md)": "markdown-slides",
    "PPTX / OOXML Libraries & CLI Tools": "pptx-ooxml",
    "Themes, Templates & Curated Lists": "themes-templates",
    "Knowledge Bases, Datasets, Agents & Misc": "knowledge-bases",
}
# sections that stay in the root index (not split)
KEEP_IN_ROOT = {"Full dataset", "How this list was built", "Contributing", "License"}

lines = open(SRC, encoding="utf-8").read().split("\n")

# locate heading boundaries
heads = []
for i, l in enumerate(lines):
    if l.startswith("## "):
        heads.append((i, l[3:].strip()))

# build sections {title: (start_line_index_after_heading, end_line_index_exclusive)}
sections = {}
for idx, (ln, title) in enumerate(heads):
    start = ln + 1
    end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
    sections[title] = (start, end)

# header (lines before first '## ') + stats line
header = "\n".join(lines[: heads[0][0]]).rstrip() + "\n"

# 1) write each split folder README
for title, folder in SPLIT.items():
    s, e = sections[title]
    body = "\n".join(lines[s:e]).strip("\n")
    content = "# %s\n\n%s\n\n[<-- Back to main list](../README.md)\n" % (title, body)
    d = os.path.join(ROOT, folder)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(content)
    print("wrote", folder + "/README.md", "(%d lines)" % (e - s))

# 2) build root index
contents_links = "\n".join(
    "- [%s](%s/README.md)" % (t, f) for t, f in SPLIT.items()
)
root_parts = [header, "## Contents\n", contents_links, ""]
for title in KEEP_IN_ROOT:
    s, e = sections[title]
    body = "\n".join(lines[s:e]).strip("\n")
    root_parts.append("## %s\n\n%s\n" % (title, body))
# trim trailing blank lines cleanly
root_text = "\n".join(root_parts).rstrip() + "\n"
open(SRC, "w", encoding="utf-8").write(root_text)
print("wrote README.md (index, %d lines)" % root_text.count("\n"))
