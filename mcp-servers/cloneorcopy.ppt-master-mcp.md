# Copy this to your AI — the zero-technical PPT guide

This document does not teach you commands. It teaches you **what to say**. Every boxed block below is
a prompt: copy it, paste it into your AI assistant, send it, wait. You never have to understand what
it is doing.

What you get at the end: a real PowerPoint file where every word, box and picture is an object you can
click and edit — not a screenshot pasted on each slide.

> **This project is AI-generated.** An agent wrote the code, the scripts, the docs and the tests; a
> human set the requirements and accepted the result. It ships under MIT as-is — no support line, and
> nobody to page when it breaks.

**You need exactly two things**

1. The project folder, from <https://github.com/cloneorcopy/ppt-master-mcp>. Press the green **Code**
   button and **Download ZIP**, or ask your AI to clone that address. However it arrives, the folder is
   named `ppt-master-mcp`. **You do not copy its path around** — drag it into the chat, or let the AI
   search for that name. Want to type it? Click once in the file manager's address bar and the path
   turns into copyable text.
2. An AI assistant that can **operate your computer** — Qoder CLI, Claude Code, Codex, anything that
   runs commands and edits its own config.

Python, git, tokens, environment variables — **none of that is your problem**. If something is missing,
the AI installs it or tells you exactly which button to press.

---

## ① Install it: one prompt, the AI does the whole deploy (once)

Send the whole block. **One blank to deal with, and you can leave it alone** — dragging the
folder into the chat is the easiest way:

```text
I am not technical, so you will do all of this. I have a folder called ppt-master-mcp, and it is here:
[drag the folder into this chat / paste its path / if you know neither, leave this line as it is and
search for that folder name yourself — and if it turns out to be missing, clone
https://github.com/cloneorcopy/ppt-master-mcp]

Everything below happens inside that one folder, in this order:

1. Read README.md inside it, then read the "Manual install" section of docs\TECHNICAL.md,
   and follow it.
2. Check whether this machine has Python 3.10+ and git. Install git yourself if it is missing.
   If Python is missing, stop and tell me in plain words what to download and which option to tick
   during install; I will reply "done" when I have clicked through it.
3. Confirm the ppt-master subfolder inside it is the upstream repository itself; if it is missing
   or is not, clone https://github.com/hugohe3/ppt-master into that location. Never modify any
   file inside it.
4. Build the environment and install dependencies: bin\install.cmd on Windows,
   bash bin/install.sh on macOS/Linux.
5. Start the service and leave it running in the background: bin\start.cmd or
   .venv\Scripts\python.exe -m pptmaster_mcp.server on Windows, ./bin/serve.sh on macOS/Linux.
   While it is alive, run this self-check and paste me its raw output:
   Windows:      .venv\Scripts\python.exe bin\smoke.py
   macOS/Linux:  .venv/bin/python bin/smoke.py
6. Keep the service running afterwards. Finish with at most 5 lines, no jargon: where it is installed,
   whether the self-check passed, and what I should do next.
```

**What success looks like**: the AI pastes a self-check result saying 26 checks passed (or all green),
and tells you the next step in plain words. If it asks you to install Python, do what it says, come
back to the same conversation and reply just: **done**.

**If it fails**, send this:

```text
Paste the last 10 lines of the failing command's output, then say plainly: which step is stuck, what
you need from me, what you will do next. Do not reinstall and do not delete anything yet.
```

---

## ② Start it: once per day before you work

Two routes, pick one — you do not need both.

**A. Click it yourself**: open your `ppt-master-mcp` folder and double-click `bin\start.cmd`
(macOS/Linux: `cd` into that folder, then `./bin/serve.sh`). A window full of text appears — **leave it open**; its last line is the board
address. To stop: `Ctrl+C`, or close the window.

**B. Let the AI start it**:

```text
Start the PPT Master service in the background: working directory is that ppt-master-mcp folder we
just used, command .venv\Scripts\python.exe -m pptmaster_mcp.server. Once it is up, call http://127.0.0.1:8730/health to
prove it is alive, then tell me in two lines: the health result and the board address.
If the port is busy or it will not start, paste me the last 5 error lines and explain in plain words.
```

One caveat: a service the AI started for you usually lives as long as that session. **Tomorrow, send
this prompt again** — or switch to route A.

---

## ③ Connect your AI to the tools (once)

```text
Add this MCP server to your own configuration: name ppt-master, URL http://127.0.0.1:8730/mcp,
local use, no key needed. If you have to restart to see the tool list, tell me what to restart.
Then answer one thing: how many ppt-master tools can you see? (the expected answer is 122)
```

**122 tools** means it is connected. Wrong number or "I can't find them"? Send:

```text
Call the service_status tool and explain its output in plain words: what is not loaded, and why.
```

---

## ④ Build a new deck (copy this, change only the bold bits)

Your material needs no tidying. Word, PDF, Markdown, an old deck, images, web links — mixed together
is fine.

```text
My material is in D:\my-stuff (do ask me for this one — it is my files, not the program). If you
cannot read that folder, copy the genuinely relevant files into the ppt-master\inputs\ folder inside
the program folder (create inputs if it is not there) and continue.

Use the ppt-master tools to build a **10-slide** deck titled **"Quarterly technical review"**, for
**executives who have never seen the technical detail**, style **clean, more diagrams less text**.

Rules:
- Follow the ppt_master_route workflow. Show me the outline and the design proposal first;
  only start drawing pages after I say yes.
- Before page one, open the live preview and send me both URLs (live preview + board) so I can paste
  them into my browser.
- Report progress in non-technical sentences, one line at a time. No jargon, no walls of text.
- When you need a decision, write "your answer needed:" and give me 2-3 options in plain words.
- When done, run the final quality gate; if it passes, export the .pptx and give me the full path.
```

It will stop midway to ask you to confirm something ("is this outline right?") — **do not skip that**.
Answer like a normal person: "fine" / "merge slide 4 into 3" / "calmer colours, no bright orange".

---

## ⑤ Watch it work: **<http://127.0.0.1:8730/deck>**

The only address worth memorising. Open it in a browser while the AI works (yourself, or ask the AI to
resend it):

- **Refreshes every two seconds — no F5.** A page appears the moment it is drawn.
- One card per deck: who is building it, how many pages done, what is running, what has been exported.
- **Click a card** for page thumbnails, the tail of its log, and the download buttons.
- Each card links to an **editing page** too. Fix things yourself in the browser — click to retype
  text, drag to move, change colour or size — then press **Apply changes**. It writes straight back;
  no trip through the AI.
- Two AIs building two decks at once? Two cards side by side, never in each other's way.

Want the addresses handed to you again:

```text
Send me the board URL and this deck's live preview URL, bare addresses only, so I can paste them
into a browser myself.
```

Board will not load? Almost always one reason: **the service is not running**. Redo step ② (start it).
The board only opens on this computer and never writes into your files — leave it open all day.

---

## ⑥ Have it revise the deck (you will come back for this)

Not sure which project the AI is holding? Ask first:

```text
List the projects you can see (the cards on the board have an English-looking name). Tell me which one
is the deck we just made, how many pages it has, and where the newest exported file is.
```

Then send whichever revision you need. **The trick: name the page, name the effect, forbid the rest.**

```text
Project: <the name on the card>. Change exactly these three things, touch no other page:
1) Slide 3 title is too long — 12 words max;
2) Slide 5's picture: use a landscape version, do not crop any text;
3) Insert one "next steps" slide before slide 9, three bullets, same visual style as its neighbours.
Then run the final quality gate; if it passes, re-export the .pptx and reply with the full new file
path plus a list of the three things you changed.
```

```text
I left annotations on elements in the preview page. Read the annotation list, apply what I wrote one by
one, and report back per annotation. Anything you are unsure about — ask me before guessing.
```

```text
Words only: make slide 2's speaker notes sound spoken rather than written, two sentences max per slide,
and add a half-sentence explanation after each technical term. Layout, pictures and colours stay as they
are. Re-export and give me the path.
```

```text
The meeting is now 5 minutes long. Cut this to 6 slides, keep the conclusion and that one key data chart,
merge or drop the rest as you judge best. First show me a list of what you plan to change;
do not edit anything until I say go.
```

Want it to hand in its homework cleanly, end any prompt with:

```text
In 5 lines or fewer and no jargon: how many pages now, did the quality gate pass, full path of the
newest exported file.
```

---

## Stuck? Open with this sentence

Don't guess, don't click around, don't reinstall. Fill in the blank:

```text
What I see is: ____________ (say what you actually see, e.g. "the board will not load", "it has not
moved for 10 minutes", "it says the export failed").
Diagnose in this order and answer me in one plain sentence per step:
1) call service_status — are the service and upstream healthy;
2) call local_service_status for this project — are the preview/confirmation pages still alive;
3) read the last 100 lines of this project's workflow log — where did it stop;
4) conclusion: is it the service, a tool, or do I need to do something. Do not delete files, do not
reinstall, do not touch anything inside ppt-master.
```

| What you see | One-line fix |
|---|---|
| Board URL will not load | Most likely the console window got closed. Redo step ② |
| The AI says it has no such tools | Service not running → redo ②; still nothing → redo ③ |
| It keeps asking for confirmation and no page appeared | Ask it again for the URL (last block of step ⑤) and paste it into a browser |
| You dislike one page | Go to step ⑥: say which page and what you want instead |
| Screen full of red text | Copy the last few lines to the AI (or to whoever installed this) and stop clicking |

---

## Three lines to actually remember

| | |
|---|---|
| Every morning | double-click `bin\start.cmd` (or make the AI do step ②) |
| While it works | **<http://127.0.0.1:8730/deck>** |
| Getting the file | the download button on the card; or open `ppt-master\projects\<your deck>\exports\` inside the program folder and double-click the `.pptx` |

If you remember nothing else, keep this one and send it whenever you are lost:

```text
Walk me through README.md step by step: tell me which step I am on, teach me one step at a time,
and skip the explanations of why.
```

A narrated version (voiceover) and an MP4 are also one sentence away — MP4 needs Windows with desktop
PowerPoint installed.

---

## Going deeper (you can ignore this forever)

For whoever actually sets the machine up: the technical reference — [English](docs/TECHNICAL.md) ·
[中文](docs/TECHNICAL_ZH.md) — environment variables, the 122 tools by group, the contract an agent
must honour, security posture, troubleshooting table, known limits.
Upstream capability in full: [PPT-MASTER-FEATURE-GUIDE.md](PPT-MASTER-FEATURE-GUIDE.md).

## License

MIT, same as upstream. Upstream is [ppt-master](https://github.com/hugohe3/ppt-master) (何雨果 Hugo He);
this repository only adds a service shell around it — **not one line of its code is modified**. That
shell, and every word of this documentation, is **AI-generated** as stated at the top of the page.

[中文文档 →](README_ZH.md)
