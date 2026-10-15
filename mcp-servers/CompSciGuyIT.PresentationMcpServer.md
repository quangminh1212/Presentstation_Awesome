# PresentationMcpServer

An MCP server for the Hermes fleet that autonomously generates **university-level educational
presentations** — interactive, self-contained Reveal.js decks plus time-synced presenter scripts —
from source materials, strictly bounded to a target audience's pedagogical level.

Node 22 · TypeScript (ESM, strict) · stdio MCP transport. Built to the
[`MASTER-BUILD-SPEC.md`](./MASTER-BUILD-SPEC.md) v1.0. **Phases 0–3 complete** — core pipeline,
interactivity (quizzes + runnable code), and rehearsal/HUD/PDF. This is the full v1 surface.

## Quickstart

```bash
npm install
npm run build
npm test          # §17 automated protocol: stdio-clean, schema lockstep, golden render, E2E
npm run verify    # build + lint + test in one shot
```

**Models: free by default, premium opt-in.** Per the fleet operating model, `llm.provider` defaults
to `free` — the Hermes OpenAI-compatible proxy (`http://127.0.0.1:3001/v1`, `FREELLMAPI_KEY`, model
`auto`), which routes to strong free cloud + local models. Set `llm.provider: "anthropic"` (needs
`ANTHROPIC_API_KEY`) only when premium is specifically wanted. Keys are read from `process.env`,
falling back to `~/.hermes/.env` (chmod 600, loaded quietly — never to stdout). Keyless runs return a
clean `LLM_NO_KEY`; the MockLlmProvider E2E is keyless.

The free provider has no vision, so image-only PDFs are handled upstream by the Hermes
`productivity/pdf-text-extraction-and-solution-append` skill (which OCRs to markdown); ingest then
reads the text. An Anthropic vision fallback exists for `llm.provider: "anthropic"`.

## Hermes registration (verified against a running gateway)

Add under `mcp_servers:` in `~/.hermes/config.yaml`:

```yaml
  presentation:
    command: /home/rumble/.local/bin/node
    args:
      - /home/rumble/.hermes/mcp-servers/PresentationMcpServer/dist/index.js
    connect_timeout: 60
    timeout: 900            # generate_deck legitimately runs many minutes
    env:
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
```

`hermes mcp test presentation` → **12 tools** discovered. A gateway `sudo systemctl restart
hermes-gateway` (system unit, never `--user`) surfaces them to Telegram/Discord.

## Tools

| Tool | Purpose |
|---|---|
| `ping` | Liveness check. |
| `ingest_materials` | Extract text + topics from pdf/docx/pptx/md/txt within allowed roots. Image-only PDFs are transcribed via the model's PDF vision. → `materialsId` |
| `define_scope` | Concept graph + Bloom targets + boundary statement; acyclic-prerequisite + exclusion-reason checks enforced in code. → `scopeId` |
| `plan_presentation` | Section outline, time budgets, slide stubs, research gaps. → `planId` |
| `enrich_plan` | Server-side web research of gaps within the boundary, budget-bounded; `skip:true` for offline. → `enrichmentId` |
| `generate_deck` | Draft → Scope-Guard → Render → Script-Sync. Self-contained bundle + script + ledger + cost manifest. → `deckId` |
| `generate_quizzes` | Regenerate misconception-grounded quiz slides on an existing deck and re-render. |
| `render_deck` | Re-render a stored deck from its IR (new theme), or `format:"pdf"` (feature-gated; see below). Also the HUD-retrofit path for older decks. |
| `rehearse_script` | Phase 3 (§11.2). Synthesize each slide's script to audio via Microsoft neural TTS, measure real durations, rebalance timing on >±10% drift, and self-calibrate the WPM for the next deck. |
| `list_decks` / `get_deck` / `delete_deck` | Deck management (`delete_deck` needs `confirm:true`). |

## Deck bundle

`workspace/decks/<deck-id>/`: `index.html` (self-contained, offline — no CDN), `assets/` (reveal.js
dist + notes plugin + our `deck.js`/`hud.js` + theme CSS + `quiz.js`/`coderunner.js`/mermaid/Pyodide
when needed), **`hud.html`** (the Presenter HUD, a sibling never referenced by `index.html`),
`deck.ir.json`, `script.md`, `script.timing.json`, `scope-ledger.json`, `manifest.json`, and — after a
rehearsal — **`rehearsal/`** (`slide-<id>.mp3` per slide + `measured.json` + `full-run.m3u`).

Two themes: `academic-light` (default) and `stream-dark` (high-contrast, for OBS/streaming).

## Rehearsal, Presenter HUD & PDF (Phase 3)

- **`rehearse_script`** speaks each slide's script with Microsoft's free neural voices (`msedge-tts`).
  This is the server's **one network dependency, used at rehearsal time only** — like enrichment's
  web search. The deck bundle stays fully offline: the mp3s are **local siblings** in `rehearsal/`,
  never referenced by `index.html`. Durations are measured by walking the mp3 frames (no ffmpeg). If
  measured drift exceeds ±10% the timing map is rebalanced to the measured values; the implied
  **effective WPM** is written to the manifest and persisted (`workspace/calibration.json`) so the
  **next** deck is generated at the voice's real rate. An unreachable service returns a structured
  `TTS_UNAVAILABLE` error (per-slide hard timeout) with the deck untouched — never a hang. Listen to
  the whole lecture via `rehearsal/full-run.m3u`.
- **Presenter HUD** (`hud.html`, in every bundle): a teleprompter with auto-scroll at the slide's
  timing rate, per-slide countdown, cumulative ahead/behind, and next-slide preview. The deck drives
  it over `window.open` + `postMessage` (click the **⧉ HUD** button, or press **U**) — an origin-agnostic channel that
  works from `file://`; `BroadcastChannel` is a same-origin-http enhancement. For OBS: window-capture
  the HUD popup, or point a browser source at `hud.html` and press **Start** to run its standalone
  timing-map clock. `render_deck` retrofits the HUD onto decks generated before Phase 3.
- **PDF export** is **feature-gated and Chromium-free by design here**. `render_deck format:"pdf"`
  returns a structured `PDF_UNAVAILABLE` error until you set `features.pdfExport:true` and
  `pdfExport.chromePath` to a Chrome/Chromium binary (e.g. on the workstation); it then drives
  Reveal's print-pdf path via `puppeteer-core`.

## Design notes (decisions where the spec was silent, per §20)

- **Free/local by default (owner directive, 2026-07-12).** The spec's §6 routed everything to
  premium Anthropic models. Per the owner, the fleet runs on free/local models with premium as
  explicit opt-in, so `llm.provider` defaults to `free` (the freellmapi proxy). The `LlmProvider`
  seam made this a clean addition — `AnthropicProvider` is retained and selectable. The §6
  Anthropic-specific features (structured-output API, adaptive thinking, prompt caching, server-side
  web search) don't exist on the free proxy, so the free provider drives structured output via a
  strict JSON instruction + schema-in-prompt + robust JSON extraction, and enrichment (web search)
  is a no-op there. Weaker free models occasionally add extra keys; a deterministic
  strip-unrecognized-keys pass repairs that before spending an LLM retry.
- **Vision-PDF ingest fallback (Anthropic-only).** For `llm.provider: "anthropic"`,
  `ingest_materials` falls back to native PDF vision for image-only scans (recorded as a `transcribe`
  cost stage; API errors surface as `INGEST_UNREADABLE`, not "parse failure"). On the free provider
  it errors clearly and directs you to the `pdf-text-extraction` skill.
- **Prompt builders** live in one cohesive `src/llm/prompts.ts` module (the spec suggested a
  `prompts/` directory of one file per task) — smaller tree, easier to keep the DRAFT cache
  breakpoint consistent.
- **Full-pipeline cost report.** Each upstream artifact (materials/scope/plan/enrichment) stores its
  own per-stage usage; `generate_deck` aggregates all of it plus DRAFT/SCOPE_GUARD into the manifest,
  so the cost report reflects the *entire* pipeline, not just deck generation.
- **Scope-guard "trim"** is applied as one targeted **section** redraft with the rewrite
  instructions (the spec says "one targeted redraft call"); "out" verdicts remove the slide. Both are
  recorded in the scope ledger.
- **Missing images** degrade gracefully (alt text kept, warning logged) rather than failing the whole
  render — the same "never a broken slide" ethos as the mermaid fallback.
- **Model IDs** are config defaults (`config.default.json`), never hardcoded; the §6 premium routing
  (Opus for judgment, Haiku for extraction) is deliberate and must not be downgraded.
- **TTS is an online adapter behind a seam (§11.2).** `msedge-tts` reaches Microsoft's public
  read-aloud service — the deliberate exception to the "no network" ethos, scoped to rehearsal time
  and wrapped in a hard per-slide timeout so an outage is a structured `TTS_UNAVAILABLE`, never a
  hang. `features.tts` stays **false** as the shipped default: `rehearse_script` is an explicit
  opt-in call that runs regardless of the flag, so nothing hangs at startup or during generation, and
  the flag never needs flipping to use it. Duration is measured deterministically from the mp3 frames
  (no ffmpeg — the N100 has no audio out), so audio verification is programmatic; actually *listening*
  is the owner's step via `full-run.m3u` on the workstation.
- **HUD channel: `window.open` + `postMessage`, not `BroadcastChannel`.** Chromium gives `file://`
  documents opaque origins, which silently breaks `BroadcastChannel` exactly where the owner opens a
  deck. The primary channel is therefore a direct window handle (origin-agnostic); `BroadcastChannel`
  is a same-origin-http bonus. Live deck-following into OBS is done by window-capturing the popup —
  two separate browser processes can't share a channel without a server, and the "always-on preview
  server" idea (§14) is out of scope. A browser-source HUD instead runs its own timing-map clock.
- **Self-calibrating WPM persists across decks.** `rehearse_script` writes the measured effective WPM
  to `workspace/calibration.json`; `generate_deck` reads it as its timing default (falling back to the
  config's 140). `render_deck` preserves a deck's stored (possibly rehearsal-measured) timing rather
  than recomputing it, so a re-render/HUD-retrofit never clobbers a calibration.
- **PDF export uses an injected browser launcher** so the success path is unit-tested against a mock
  (no browser installed here); the error path is proven live. DoD is not gated on a live PDF.

## The three invariants (absolute)

1. **stdout is JSON-RPC only** — all logs to stderr via `log.ts`; `no-console` lints `src/`; the
   CRIT-1 stdio-clean test is the regression lock. (It already caught dotenv v17's stdout banner.)
2. **The LLM never emits raw HTML** — everything flows through the Zod-validated SlideDeck IR; the
   renderer is deterministic template code.
3. **Bundles are self-contained and offline** — no CDN/asset URLs; the golden test asserts zero
   external asset references.

## Provenance, numbers & operations

Specified and reviewed by the owner (architect); built P0–P3 by AI agents under
`MASTER-BUILD-SPEC.md` + per-phase kickoffs (contracts-first) — the fleet's first
TypeScript build. Same-day independent reviews re-ran the §17 protocol and inspected
the artifacts (bundles grep-audited for the offline invariant, quiz provenance checked
against source materials).

- **97 tests, 0 skipped**; 12 MCP tools; the stdio-cleanliness regression test caught a
  real offender mid-build (a dependency upgrade printing a stdout banner into what must
  be pure JSON-RPC).
- **Cost engineering as a feature**: real teaching decks generated at **$0** on
  free-tier model routing (an owner-directed reversal of the original premium design —
  the provider seam made it a config default, not a rewrite); per-stage token
  accounting ships in every deck manifest.
- **Trust boundary**: the LLM never emits HTML — everything passes through a
  Zod-validated slide IR into a deterministic renderer; quiz distractors are built from
  *materials-grounded* misconceptions, each carrying a `groundedIn` provenance pointer.
- **A feedback loop that converges**: the TTS rehearsal measures real spoken durations
  and calibrates the timing model — first real deck −6.8% drift, second pass at the
  measured rate **−0.1%**, and the next deck generates calibration-aware from the start.
- Bundles are fully offline (runnable Python ships a locally-vendored Pyodide only when
  a deck needs it); the presenter HUD works from `file://` and as an OBS browser
  source — it was designed for a streaming rig.
