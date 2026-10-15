#!/usr/bin/env python3
# Fetch README of every repo (top-500 per category) and save to a folder
# outside the git repo. Filename = repo link (owner__repo.md).
import json, os, re, sys, time, urllib.request, urllib.error

BASE = r"C:\Dev\PresentstationTool\readmes"
SRC = r"C:\Dev\PresentstationTool\research\classified_full.json"
LOG = r"C:\Dev\PresentstationTool\research\fetch_readmes.log"
PER_CAT = 500

def sanitize(s):
    s = re.sub(r'[^A-Za-z0-9_]+', '_', s)
    return s.strip('_') or 'x'

def cat_folder(cat):
    return sanitize(cat)

def parse_owner_name(url):
    # https://github.com/owner/repo
    m = re.match(r'https?://github\.com/([^/]+)/([^/?#]+)', url or '')
    if m:
        return m.group(1), m.group(2)
    return None, None

def main():
    tok = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not tok:
        sys.exit("GH_TOKEN not set")
    with open(SRC, encoding='utf-8') as f:
        data = json.load(f)

    # group by category, sort by stars desc
    cats = {}
    for r in data:
        cats.setdefault(r.get("category", "Other"), []).append(r)
    for c in cats:
        cats[c].sort(key=lambda r: -(r.get("stargazersCount") or 0))

    # build work list: top PER_CAT per category
    work = []
    for c, items in cats.items():
        for r in items[:PER_CAT]:
            owner, name = parse_owner_name(r.get("url"))
            if not owner:
                continue
            folder = os.path.join(BASE, cat_folder(c))
            fname = f"{owner}__{name}.md"
            path = os.path.join(folder, fname)
            work.append((c, owner, name, path))

    total = len(work)
    done = skipped = ok = no_readme = failed = 0
    start = time.time()
    logf = open(LOG, 'w', encoding='utf-8')

    def log(msg):
        ts = time.strftime('%H:%M:%S')
        line = f"[{ts}] {msg}"
        logf.write(line + "\n")
        logf.flush()

    log(f"TOTAL={total}")

    for i, (cat, owner, name, path) in enumerate(work, 1):
        if os.path.exists(path):
            skipped += 1
            done += 1
            if done % 200 == 0:
                log(f"progress {done}/{total} ok={ok} no_readme={no_readme} failed={failed} skip={skipped}")
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        api = f"https://api.github.com/repos/{owner}/{name}/readme"
        req = urllib.request.Request(api, headers={
            "Authorization": f"Bearer {tok}",
            "Accept": "application/vnd.github.raw+json",
            "User-Agent": "presentstation-fetch",
        })
        attempt = 0
        while True:
            attempt += 1
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = resp.read()
                with open(path, 'wb') as wf:
                    wf.write(body)
                ok += 1
                break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    # no readme; write empty marker file so we skip next time
                    open(path, 'wb').close()
                    no_readme += 1
                    break
                elif e.code == 403 and 'rate limit' in (e.headers.get('X-RateLimit-Remaining','') or ''):
                    rem = e.headers.get('X-RateLimit-Remaining','')
                    reset = e.headers.get('X-RateLimit-Reset')
                    wait = max(1, int(reset or time.time()+60) - int(time.time())) if reset else 60
                    log(f"RATE LIMIT hit at {i}/{total}; sleeping {wait}s")
                    time.sleep(wait)
                    continue
                elif e.code in (500, 502, 503, 504) and attempt < 4:
                    time.sleep(3 * attempt)
                    continue
                else:
                    failed += 1
                    log(f"FAIL {owner}/{name} HTTP {e.code}: {e.reason}")
                    # write a small error marker so it's not retried as empty
                    with open(path + ".err", 'w', encoding='utf-8') as ef:
                        ef.write(f"HTTP {e.code}: {e.reason}\n")
                    break
            except Exception as e:
                if attempt < 4:
                    time.sleep(3 * attempt)
                    continue
                failed += 1
                log(f"FAIL {owner}/{name}: {e}")
                with open(path + ".err", 'w', encoding='utf-8') as ef:
                    ef.write(f"{e}\n")
                break
        done += 1
        if done % 50 == 0:
            el = time.time() - start
            rate = done / el if el else 0
            log(f"progress {done}/{total} ok={ok} no_readme={no_readme} failed={failed} skip={skipped} ({rate:.1f}/s)")

    log(f"DONE {done}/{total} ok={ok} no_readme={no_readme} failed={failed} skip={skipped} elapsed={time.time()-start:.0f}s")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback
        try:
            with open(r"C:\Dev\PresentstationTool\research\fetch_readmes.crash", 'w', encoding='utf-8') as cf:
                cf.write(traceback.format_exc())
        except Exception:
            pass
        raise
