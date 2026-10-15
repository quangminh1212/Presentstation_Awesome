import json
raw = open(r"C:\Dev\PresentstationTool\research\all_filtered.json", encoding="utf-8", errors="ignore").read()
data = json.loads(raw)

cats = [
    ("MCP Servers", ["mcp", "model context protocol", "slides-mcp", "pptx-mcp", "office-powerpoint-mcp", "google-slides-mcp"]),
    ("AI / LLM Generators (end-to-end)", ["ai presentation", "ai-ppt", "ppt generator", "presentation generator",
        "ai-presentation", "text to ppt", "text-to-ppt", "slides generator", "generate ppt", "ai generate",
        "presentation-ai", "ai presentation generator", "open source ai presentation", "oh-my-ppt",
        "powerpoint generator", "ai ppt generator", "llm ppt", "gamma alternative", "gamma alt", "deck generator",
        "ai slide", "presentation ai", "create professional slides", "pitch deck generator"]),
    ("Agent Skills (Claude/Codex/Claude-Fable)", ["skill", "agent skill", "claude skill", "claude code skill", "codex skill",
        "coding agent", "pptx-skill", "ppt-skill", "slide-skill", "mcp-skill", "knowledge", "prompt"]),
    ("Slides Frameworks (HTML/Web)", ["reveal.js", "reveal-js", "impress.js", "impressjs", "slidev", "deck.js",
        "bespoke.js", "bespoke", "shower", "s5", "html5slides", "io-2012-slide", "remark", "html slides",
        "html slideshow", "html slide", "html presentation", "presentation framework", "web presentation",
        "slides framework", "struts", "prezi", "awwation", "vanillajs-deck", "next-mdx-deck", "mdx deck"]),
    ("Markdown -> Slides (Marp/Quarto/RISE/Org/Pandoc)", ["marp", "quarto", "reveal-md", "rise", "org-reveal",
        "org-re-reveal", "asciidoctor-reveal", "mdpress", "markdown2impress", "markdown slides", "markdown2deckjs",
        "markdown-slides", "reveal-hugo", "markdown to", "markdown presentation", "pandoc", "mkslides",
        "rst2html5", "sphinx", "xaringan", "typst", "typslides", "touying", "minislides", "deckrun", "slidy"]),
    ("PPTX / OOXML Libraries & Tools", ["python-pptx", "pptxgenjs", "pptx", "office_oxide", "openxml", "ooxml",
        "python-opc", "docx", "xlsx", "translate-pptx", "ppt-to-pdf", "pptx-templater", "drawio2pptx",
        "html-to-editable-pptx", "html2pptx", "pptx-maker", "automate-powerpoint", "python_pptx", "pptxgenjs-jsx",
        "pptx-translator", "office document library"]),
    ("Editor / Plugin / Theme / Template", ["theme", "template", "obsidian", "vscode", "sublime", "plugin", "editor",
        "addon", "extension", "templates", "awesome-marp", "awesome", "marpstyle", "slidev-theme", "marp-theme",
        "slidev-templates", "beautiful-html-templates", "html-templates", "meme"]),
    ("Other / Knowledge / Datasets / Misc", []),
]

def classify(repo):
    txt = (repo.get("name","") + " " + (repo.get("description") or "")).lower()
    for label, kws in cats:
        for kw in kws:
            if kw.lower() in txt:
                return label
    return "Other / Knowledge / Datasets / Misc"

for repo in data:
    repo["category"] = classify(repo)
    repo["owner_name"] = f"{repo['owner']['login']}/{repo['name']}"
    repo["desc"] = (repo.get("description") or "").replace("\n"," ").strip()

from collections import defaultdict
buckets = defaultdict(list)
for repo in data: buckets[repo["category"]].append(repo)

# save each category to a tsv for curation
import os
os.makedirs("cat", exist_ok=True)
for label, lst in buckets.items():
    lst = sorted(lst, key=lambda r:-r["stargazersCount"])
    safe = label.split("(")[0].strip().replace("/","-").replace(" ","_").replace(">","to").replace(":","")
    with open(f"cat/{safe}.tsv","w",encoding="utf-8") as f:
        for r in lst:
            f.write(f"{r['stargazersCount']}\t{r['owner_name']}\t{r['url']}\t{r['desc']}\n")
    print(f"{label}: {len(lst)}")

# also save full data with category
json.dump(data, open("classified_full.json","w",encoding="utf-8"), ensure_ascii=False)
print("total", len(data))
