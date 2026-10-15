import subprocess, json, time, sys, os

QUERIES = [
    # --- broad AI / generative presentations ---
    "ai presentation","ai ppt","ai slide","ai deck","ai slides",
    "ppt generator","presentation generator","slides generator","powerpoint generator",
    "text to ppt","text-to-ppt","llm presentation","llm ppt","llm slides",
    "generative presentation","auto generate ppt","automatic presentation",
    "ai presentation generator","open source ai presentation","gamma alternative",
    "ai pitch deck","ppt ai","AI PPT","intelligent ppt","ppt assistant",
    "smart ppt","ppt generation","auto ppt","AI presentation maker","presentation ai",
    "ppt creator","slide generator","deck generator","presentation maker",
    "slides ai","talk generator","lecture slides generator",
    # --- Chinese-language AI PPT (huge ecosystem) ---
    "\u667a\u80fdPPT","PPT\u751f\u6210","\u81ea\u52a8\u751f\u6210PPT","\u6f14\u793a\u7a3f\u751f\u6210",
    "\u6f14\u793a\u6587\u7a3f","PPT\u667a\u80fd\u751f\u6210","\u5e7b\u706f\u7247\u751f\u6210","ai \u6f14\u793a",
    "ppt \u751f\u6210","\u6f14\u793a\u7a3f ai","\u667a\u80fd\u6f14\u793a\u6587\u7a3f","\u81ea\u52a8ppt",
    # --- MCP ---
    "mcp presentation","mcp ppt","mcp powerpoint","mcp slides","mcp google slides",
    "model context protocol slides","mcp deck","ppt-mcp","slides-mcp","powerpoint-mcp",
    # --- frameworks ---
    "presentation framework","html presentation","slide framework","reveal.js","slidev",
    "impress.js","deck.js","remark slides","bespoke.js","shower presentation","s5 slides",
    "reveal-md","html5 slides","web slides","react presentation","vue presentation",
    "angular presentation","svelte slides","js presentation","terminal presentation",
    "cli presentation","tui slides","pptx framework","javascript slides","node slides",
    # --- markdown / docs ---
    "marp","markdown slides","markdown presentation","markdown to slides","quarto revealjs",
    "quarto slides","xaringan","remarkjs","pandoc reveal","org reveal","typst slides",
    "touying","reveal-md","md to ppt","md2pptx","markdown pptx","mdx deck",
    "markdown to pptx","slides markdown","revealjs theme","asciidoctor reveal",
    # --- pptx / ooxml / office ---
    "python-pptx","pptxgenjs","pptx library","powerpoint library","pptx generator",
    "ppt to pdf","pptx to pdf","pptx parser","pptx template","drawio2pptx","html2pptx",
    "translate pptx","python powerpoint","node powerpoint","go pptx","rust pptx",
    "openxml","ooxml","office document generation","pptx renderer","pptx builder",
    "convert html to pptx","pptx from html","python pptx","generate pptx",
    # --- agent skills / plugins / editor ---
    "claude code skill presentation","claude skill ppt","claude skill slides",
    "agent skill presentation","Claude-Fable skill slides","codex skill ppt",
    "obsidian presentation","obsidian slides","vscode slides","pptx skill","slide skill",
    "claude skill deck","ai agent slides","agentic presentation","presentation agent",
    "ppt agent","slides skill","presentation plugin","slides plugin",
    # --- themes / templates / awesome ---
    "presentation theme","slide template","presentation template","slides theme",
    "awesome slides","awesome presentation","ppt template","reveal.js theme",
    "slidev theme","marp theme","html template presentation","pptx template",
    "google slides template","keynote template","beamer theme","reveal theme",
    # --- knowledge / datasets / models / misc ---
    "presentation dataset","slide dataset","presentation knowledge","slide layout model",
    "presentation llm","diffusion presentation","ppt diffusion","presentation transformer",
    "slide understanding","presentation understanding","ocr slides","slides ocr",
    "presentation tool","slides tool","deck tool","presentation cli","slides cli",
    "pptx cli","presentation api","slides api","pptx api","deck builder",
    "online presentation maker","presentation engine","slide engine","revealjs plugins",
    # --- topic-based (broad, catches a lot) ---
    "topic:presentation","topic:pptx","topic:ppt","topic:powerpoint","topic:slides",
    "topic:slide","topic:marp","topic:slidev","topic:revealjs","topic:reveal.js",
    "topic:mcp","topic:claude","topic:agent","topic:obsidian","topic:html-slides",
    "topic:markdown-slides","topic:deck","topic:presentation-generator","topic:ai",
    "topic:llm","topic:generator","topic:powerpoint-addin","topic:google-slides",
]

JSON_FIELDS = "name,owner,description,stargazersCount,url,updatedAt"
out_path = r"C:\Dev\PresentstationTool\research\expanded_raw.jsonl"
seen = set()
count = 0
os.makedirs(os.path.dirname(out_path), exist_ok=True)

env = dict(os.environ)
env["GIT_CONFIG_COUNT"] = "0"

LOG = r"C:\Dev\PresentstationTool\research\search_log.txt"
if os.path.exists(LOG):
    open(LOG, "w", encoding="utf-8").close()
def log(msg):
    with open(LOG, "a", encoding="utf-8") as fl:
        fl.write(msg + "\n")

# resume: preload already-collected urls
if os.path.exists(out_path):
    with open(out_path, encoding="utf-8") as fprev:
        for line in fprev:
            line = line.strip()
            if not line:
                continue
            try:
                seen.add(json.loads(line).get("url"))
            except Exception:
                pass
    count = len(seen)
    log(f"Resuming: {count} repos already collected")

with open(out_path, "a", encoding="utf-8") as fout:
    for i, q in enumerate(QUERIES):
        ok = False
        for attempt in range(5):
            try:
                cmd = ["gh", "search", "repos", q, "--limit", "1000", "--sort", "stars",
                       "--json", JSON_FIELDS]
                res = subprocess.run(cmd, capture_output=True, timeout=60, env=env)
                if res.returncode != 0:
                    err = res.stderr.decode("utf-8", "ignore").lower()
                    if "rate limit" in err or "429" in err or "secondary" in err:
                        wait = 20 * (attempt + 1)
                        log(f"[ratelimit] attempt {attempt+1}, sleep {wait}s")
                        time.sleep(wait)
                        continue
                    log(f"[err] query #{i+1}: {err[:160]}")
                    ok = True  # give up on this query
                    break
                items = json.loads(res.stdout.decode("utf-8", "ignore") or "[]")
                for it in items:
                    key = it.get("url")
                    if not key or key in seen:
                        continue
                    seen.add(key)
                    fout.write(json.dumps(it, ensure_ascii=False) + "\n")
                    count += 1
                log(f"[{i+1}/{len(QUERIES)}] query #{i+1}: +{len(items)} (total {count})")
                ok = True
                break
            except subprocess.TimeoutExpired:
                log(f"[timeout] query #{i+1} attempt {attempt+1}")
                time.sleep(5)
            except json.JSONDecodeError as e:
                log(f"[json] query #{i+1}: {e}")
                ok = True
                break
        if not ok:
            log(f"[fail] query #{i+1} dropped after retries")
        time.sleep(1.5)

log(f"DONE. Wrote {count} unique repos to {out_path}")
