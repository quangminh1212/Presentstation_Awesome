import json, os, re
from collections import defaultdict

ROOT = r"C:\Dev\PresentstationTool\research"
# 1) load old 800
old = json.loads(open(os.path.join(ROOT,"all_filtered.json"), encoding="utf-8", errors="ignore").read())
# 2) load expanded 45575
new = []
with open(os.path.join(ROOT,"expanded_raw.jsonl"), encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if not line: continue
        try: new.append(json.loads(line))
        except: pass

# normalize to common shape, dedup by url
def norm(r):
    owner = r.get("owner") or {}
    if isinstance(owner, dict):
        owner_name = owner.get("login") or owner.get("name") or ""
    else:
        owner_name = str(owner)
    return {
        "name": r.get("name") or "",
        "owner_name": owner_name,
        "desc": (r.get("description") or "").strip(),
        "stargazersCount": r.get("stargazersCount") or 0,
        "url": r.get("url") or "",
        "updatedAt": r.get("updatedAt") or "",
    }

merged = {}
for r in old + new:
    n = norm(r)
    if not n["url"]: continue
    if n["url"] not in merged:
        merged[n["url"]] = n
    else:
        # keep the one with more stars
        if n["stargazersCount"] > merged[n["url"]]["stargazersCount"]:
            merged[n["url"]] = n
data = list(merged.values())
print("merged unique:", len(data))

# ---- GLOBAL NOISE (carousels / flashcards / game decks / card games etc.) ----
GLOBAL_NOISE = ["anki","mtg","commander-deck","sealed-deck","randeck","flashcard","flash-cards",
    "slider-api","imageslider","image-slider","devrama-slider","neon-slides","stream-deck","node-cards",
    "deck.gl","poker","elgato","node-elgato","kalouki","miya0001/slider","yugioh","tarot",
    "trading-card","card-game","pokemon deck","mtg-deck","flash-card","flashcards","quizlet",
    "carousel","slider","splash","woocommerce","woo-commerce","clicker","remote presentation control",
    "presentation-client","presentation client","deckbuilding","deck builder game","card collection",
    "swipe","splide","swiper","glide","flickity","slick-carousel","owl-carousel","bootstrap-carousel",
    "splidejs","keen-slider","embla-carousel","nuka-carousel","react-slick","vue-carousel",
    "framer-motion carousel","lightslider","unslider","bxslider","photo slider","image carousel",
    "gallery slider","testimonial slider","banner slider","hero slider"]

# ---- STRONG relevance terms (presence alone => relevant) ----
STRONG = ["presentation","present ","presenting","slideshow","slideshows","slide-show","slide-show",
    "slides","slide"," ppt","pptx","powerpoint","keynote","beamer","reveal","marp","slidev",
    "impress.js","impressjs","quarto","xaringan","pandoc","revealjs","reveal-js","typst","touying",
    "obsidian","google-slides","google slides","html-slides","html-slide","talk","lecture",
    "演示","幻灯","汇报","演讲","プレゼン","프레젠","슬라이드","deck","decks","pitchdeck","pitch-deck",
    "md2pptx","html5slides","remark","decktape","spectacle","pptist","deckset","md2slides",
    "slide-master","slideagent","ai-ppt","aippt","ai ppt","ai slide","ai 幻灯片","智能ppt","智能ppt",
    "ppt生成","ppt 生成","一键生成ppt","自动生成ppt","ppt 演讲稿","ppt制作","ppt-ai","presentation-ai",
    "slides-ai","ai presentation","ai slides","ai deck","ai pitch","ppt agent","presentation agent"]

# ambiguous terms that must be guarded (false positives: game decks, carousels, sliders)
GUARD = {"deck": ["gl","stream","commander","sealed","tarot","poker","yugioh","trading","card-game",
                  "mtg","building","builder game","collection","swipe","deckbuilder","deckbuilding"],
         "slide": ["slider","carousel","splash"],
         "talk": ["talkpython","pycon talk","conference talk","podcast"]}

def is_relevant(r):
    blob = (r["owner_name"]+" "+r["name"]+" "+r["desc"]).lower()
    for term in STRONG:
        if term in blob:
            bad = False
            for key, guards in GUARD.items():
                if key in term:
                    for g in guards:
                        if g in blob:
                            bad = True; break
            if not bad:
                return True
    return False

def is_noise(r):
    blob = (r["owner_name"]+" "+r["name"]+" "+r["desc"]).lower()
    for kw in GLOBAL_NOISE:
        if kw in blob:
            return True
    return False

filtered = [r for r in data if is_relevant(r) and not is_noise(r)]
print("after relevance+noise:", len(filtered))

# ---- classification ----
def classify(r):
    txt = (r["name"]+" "+r["desc"]).lower()
    # MCP
    if any(k in txt for k in ["mcp","model context protocol"]):
        # but only if presentation-ish already (relevance passed)
        return "MCP Servers"
    # AI / LLM generators
    if any(k in txt for k in ["ai presentation","ai-ppt","ai ppt","ai slide","ai-slide","ai deck",
        "ppt generator","presentation generator","slides generator","powerpoint generator",
        "text to ppt","text-to-ppt","text to presentation","llm presentation","llm ppt","llm slides",
        "ai presentation generator","generative presentation","auto generate ppt","automatic presentation",
        "ai pitch deck","ppt ai","intelligent ppt","ppt assistant","smart ppt","ppt generation",
        "auto ppt","ai presentation maker","presentation ai","ppt creator","slide generator",
        "deck generator","presentation maker","slides ai","talk generator","lecture slides generator",
        "ai generate","ai slide","生成","智能ppt","智能ppt","ppt生成","演示文稿","幻灯片生成","ai 演示",
        "ppt ai","ai ppt","ai presentation","gamma","ai deck","presentation-ai","open source ai",
        "ai 幻灯片","一键生成","自动生成ppt","ai 演讲","ppt agent","presentation agent","agentic"]):
        return "AI / LLM Generators (end-to-end)"
    # Agent skills / plugins
    if any(k in txt for k in ["skill","agent skill","claude skill","claude code skill","codex skill",
        "coding agent","pptx-skill","ppt-skill","slide-skill","mcp-skill","claude-fable","plugin",
        "extension","obsidian","vscode","sublime","addon","editor","agentic"]):
        return "Agent Skills (Claude/Codex/Claude-Fable)"
    # HTML frameworks
    if any(k in txt for k in ["reveal.js","reveal-js","impress.js","impressjs","slidev","deck.js",
        "bespoke","shower","s5","html5slides","remark","html slides","html slideshow","html slide",
        "html presentation","presentation framework","web presentation","slides framework",
        "prezi","vanillajs-deck","next-mdx-deck","mdx deck","revealjs","reveal-hugo","reveal-md",
        "presentation engine","slide engine","terminal presentation","cli presentation","tui slides",
        "javascript slides","js presentation","react presentation","vue presentation","svelte slides"]):
        return "Slides Frameworks (HTML/Web)"
    # Markdown -> slides
    if any(k in txt for k in ["marp","quarto","reveal-md","rise","org-reveal","org-re-reveal",
        "asciidoctor-reveal","mdpress","markdown2impress","markdown slides","markdown2deckjs",
        "markdown-slides","markdown to","markdown presentation","pandoc","mkslides","rst2html5",
        "sphinx","xaringan","typst","typslides","touying","minislides","deckrun","slidy",
        "markdown to pptx","md to ppt","md2pptx","markdown pptx","reveal-md"]):
        return "Markdown -> Slides (Marp/Quarto/RISE/Org/Pandoc)"
    # PPTX / OOXML
    if any(k in txt for k in ["python-pptx","pptxgenjs","pptx","office_oxide","openxml","ooxml",
        "python-opc","docx","xlsx","translate-pptx","ppt-to-pdf","pptx-templater","drawio2pptx",
        "html-to-editable-pptx","html2pptx","pptx-maker","automate-powerpoint","python_pptx",
        "pptxgenjs-jsx","pptx-translator","office document","powerpoint library","pptx library",
        "pptx generator","ppt to pdf","pptx to pdf","pptx parser","pptx template","python powerpoint",
        "node powerpoint","go pptx","rust pptx","ooxml","openxml","pptx cli","generate pptx",
        "convert html to pptx","pptx from html","pptx renderer","pptx builder"]):
        return "PPTX / OOXML Libraries & Tools"
    # Themes/templates
    if any(k in txt for k in ["theme","template","templates","awesome","marpstyle","slidev-theme",
        "marp-theme","slidev-templates","beautiful-html","html-templates","meme","ppt template",
        "reveal.js theme","slidev theme","marp theme","reveal theme","beamer theme","keynote template",
        "google slides template","html template presentation","presentation theme","slide template",
        "slides theme","presentation template","slides template"]):
        return "Editor / Plugin / Theme / Template"
    return "Other / Knowledge / Datasets / Misc"

for r in filtered:
    r["category"] = classify(r)
    r["desc"] = r["desc"][:240]

# save classified_full.json
json.dump(filtered, open(os.path.join(ROOT,"classified_full.json"),"w",encoding="utf-8"), ensure_ascii=False)
print("saved classified_full.json:", len(filtered))

# category counts
buckets = defaultdict(list)
for r in filtered: buckets[r["category"]].append(r)
for cat in sorted(buckets, key=lambda c:-len(buckets[c])):
    print(f"  {cat}: {len(buckets[cat])}")
