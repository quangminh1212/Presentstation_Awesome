import json, os

raw = open(r"C:\Dev\PresentstationTool\research\classified_full.json", encoding="utf-8", errors="ignore").read()
data = json.loads(raw)

# Display label (shown in README) -> internal category key
SECTIONS = [
    ("AI Presentation Generators (end-to-end)", "AI / LLM Generators (end-to-end)",
     "Turn a topic, document or prompt into a full deck automatically (HTML, PPTX or hosted slides)."),
    ("MCP Servers for Presentations", "MCP Servers",
     "Model Context Protocol servers that let AI agents create / edit PowerPoint, Google Slides or web decks."),
    ("Agent Skills, Plugins & Editor Extensions", "Agent Skills (Claude/Codex/Claude-Fable)",
     "Claude Code / Codex skills, VS Code / Obsidian extensions and plugins that drive slide & deck generation."),
    ("HTML Slide Frameworks", "Slides Frameworks (HTML/Web)",
     "Browser-based presentation frameworks and runtimes for building slide decks with web tech."),
    ("Markdown \u2192 Slides (Marp / Quarto / Typst / Pandoc / Org / Reveal-md)", "Markdown -> Slides (Marp/Quarto/RISE/Org/Pandoc)",
     "Author slides in Markdown / Typst / Org / R and render to reveal.js, Marp, Beamer or HTML."),
    ("PPTX / OOXML Libraries & CLI Tools", "PPTX / OOXML Libraries & Tools",
     "Libraries and command-line tools to build, edit, convert and translate native .pptx files."),
    ("Themes, Templates & Curated Lists", "Editor / Plugin / Theme / Template",
     "Visual themes, starter templates and awesome-lists for presentations and slides."),
    ("Knowledge Bases, Datasets, Agents & Misc", "Other / Knowledge / Datasets / Misc",
     "Agent frameworks, datasets, brand/knowledge skills and related misc tooling."),
]

# global noise (carousels / flashcards / game decks etc.)
GLOBAL_NOISE = ["anki","mtg","commander-deck","sealed-deck","randeck","flashcard","slider-api",
    "imageslider","devrama-slider","neon-slides","stream-deck","node-cards","deck.gl","poker",
    "elgato","node-elgato","kalouki","miya0001/slider"]

# per-section extra exclusion keywords (substring, lower) keyed by INTERNAL category
EXTRA_NOISE = {
    "Editor / Plugin / Theme / Template": ["slider","splash","woocommerce","woo commerce","carousel","zoom in zoom out"],
    "Other / Knowledge / Datasets / Misc": ["clicker","remote presentation control","presentation-client","presentation client"],
    "Slides Frameworks (HTML/Web)": ["slider","splash"],
    "MCP Servers": ["clicker"],
    "Agent Skills (Claude/Codex/Claude-Fable)": ["clicker"],
}

def clean(repo, section):
    name = repo["owner_name"].lower()
    desc = (repo.get("desc") or "").lower()
    blob = name + " " + desc
    for kw in GLOBAL_NOISE:
        if kw in blob: return False
    for kw in EXTRA_NOISE.get(section, []):
        if kw in blob: return False
    return True

# strong presentation signal used to decide which repos belong in "Featured"
STRONG_PRESENT = ["presentation","slides","slide "," ppt","pptx","powerpoint","keynote","beamer",
    "reveal","marp","slidev","impress","quarto","xaringan","pandoc","typst","touying",
    "google-slides","lecture","演示","幻灯","汇报","演讲","プレゼン","프레젠","슬라이드","deck","decks",
    "pitchdeck","pitch-deck","html-slide","html-slides"]
PRESENT_CATS = {"AI / LLM Generators (end-to-end)","MCP Servers","Slides Frameworks (HTML/Web)",
    "Markdown -> Slides (Marp/Quarto/RISE/Org/Pandoc)","PPTX / OOXML Libraries & Tools"}

def is_present_topic(repo):
    if repo["category"] in PRESENT_CATS:
        return True
    blob = (repo["owner_name"]+" "+repo["name"]+" "+(repo.get("desc") or "")).lower()
    return any(k in blob for k in STRONG_PRESENT)

# famous repos that match a weak keyword but are NOT presentation-related
FEATURED_EXCLUDE = {"dujltqzv/some-many-books","owainlewis/awesome-artificial-intelligence",
    "dair-ai/ml-course-notes",
    # off-topic toolkits (office suites, design, NLP, file/markdown parsers, prompt lists)
    "fighting41love/funnlp","iofficeai/officecli","dream-num/univer","onlyoffice/documentserver",
    "onlyoffice/desktopeditors","netease-youdao/lobsterai","genspark-ai/genoffice",
    "opencoworkai/open-codesign","the-vibe-company/megaparse","nexu-io/html-anything",
    "jonschlinkert/gray-matter","joanrod/star-vector","serenakeyitan/awesome-notebooklm-prompts",
    # academic personal-website / portfolio theme (generic web/design, not presentation)
    "hugoblox/hugo-theme-academic-cv",
    # generic online Markdown editor (only incidental PPT preview) + iOS modal-sheet UI lib (Apple "presentation" jargon)
    "nicejade/markdown-online-editor","slackhq/panmodal"}

def repo_key(r):
    return r["url"].replace("https://github.com/","").rstrip("/").lower()

# how many repos to show per section in the README (the full set lives in data/repos.json)
CAP = 500

# build buckets
buckets = {cat: [] for _,cat,_ in SECTIONS}
for repo in data:
    buckets[repo["category"]].append(repo)

# format helper
def fmt(repo):
    n = repo["owner_name"]
    url = repo["url"]
    s = repo["stargazersCount"]
    d = (repo.get("desc") or "").strip()
    if not d: d = "\u2014"
    # trim very long desc
    if len(d) > 160: d = d[:157] + "..."
    stars = f"{s:,}" if s else "0"
    return f"- [{n}]({url}) \u2014 \u2605 {stars} \u2014 {d}"

# write README
out = []
out.append("# Presentstation_Awesome")
out.append("")
out.append("> A curated, aggregated list of **GitHub repositories that help you build presentations, slides and PowerPoint decks with AI, agents, MCP servers, CLIs or web frameworks** \u2014 including AI generators, MCP servers, agent skills, plugins, libraries, themes and knowledge bases.")
out.append("")
out.append(f"**{len(data)} repositories** aggregated from GitHub search (sorted by stars). Filters applied to drop unrelated \"slider/carousel\", flashcard, trading-card and game-deck repos.")
out.append("")
out.append("## Contents")
out.append("")
out.append("1. [Featured](#featured)")
for i,(label,_,_) in enumerate(SECTIONS, start=2):
    anchor = label.lower().replace(" ","-").replace("\u2192","to").replace("/","-").replace("(","").replace(")","").replace(",","")
    anchor = "".join(c for c in anchor if c.isalnum() or c=="-")
    out.append(f"{i}. [{label}](#{anchor})")
out.append(f"{len(SECTIONS)+2}. [Full dataset](#full-dataset)")
out.append("")
out.append("## Featured")
out.append("")
out.append("The highest-starred and most influential repositories across all categories:")
out.append("")
featured = sorted([r for r in data if clean(r, "") and is_present_topic(r)
                     and (repo_key(r) not in FEATURED_EXCLUDE)],
                   key=lambda r:-r["stargazersCount"])[:45]
for r in featured:
    out.append(fmt(r))
out.append("")

for label, cat, blurb in SECTIONS:
    out.append(f"## {label}")
    out.append("")
    out.append(blurb)
    out.append("")
    items = [r for r in buckets.get(cat,[]) if clean(r, cat)]
    items.sort(key=lambda r:-r["stargazersCount"])
    if not items:
        out.append("_No repositories matched._")
        out.append("")
        continue
    shown = items[:CAP]
    for r in shown:
        out.append(fmt(r))
    out.append("")
    if len(items) > CAP:
        out.append(f"_Showing top {CAP} of {len(items)} repos in this category — the full list with all {len(items)} entries is in [`data/repos.json`](data/repos.json)._")
    else:
        out.append(f"_({len(items)} repos in this category)_")
    out.append("")

out.append("## Full dataset")
out.append("")
out.append(f"All {len(data)} matched repositories (with categories and stars) are saved in [`data/repos.json`](data/repos.json).")
out.append("")
out.append("## How this list was built")
out.append("")
out.append("- Repositories were discovered via `gh search repos` across **214 queries** (AI presentation / PPT generators, MCP servers, agent skills, Marp / Slidev / reveal.js frameworks, python-pptx / PptxGenJS, themes & templates, knowledge bases, plus Chinese-language AI-PPT tools and `topic:` filters) — yielding ~45,600 unique repos after de-duplication.")
out.append("- Results were merged, de-duplicated and noise-filtered (card-game decks, flashcards, image sliders/carousels removed).")
out.append("- Each repo was auto-classified into one of 8 categories by keyword; the curated lists above exclude obvious non-presentation noise.")
out.append("")
out.append("## Contributing")
out.append("")
out.append("Found a great repo we missed? Open an issue or PR. Keep entries sorted by stars within each category.")
out.append("")
out.append("## License")
out.append("")
out.append("Content is a curated index; each linked repository retains its own license. This index is released under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).")

text = "\n".join(out)
os.makedirs(r"C:\Dev\PresentstationTool\data", exist_ok=True)
open(r"C:\Dev\PresentstationTool\README.md","w",encoding="utf-8").write(text)
# copy dataset
json.dump(data, open(r"C:\Dev\PresentstationTool\data\repos.json","w",encoding="utf-8"), ensure_ascii=False)
print("README lines:", len(out))
print("Featured:", len(featured))
for label,cat,_ in SECTIONS:
    cnt = len([r for r in buckets.get(cat,[]) if clean(r,cat)])
    print(f"  {cat}: {cnt}")
