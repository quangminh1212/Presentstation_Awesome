# OpenPPTX AI

An open-source PowerPoint task pane assistant that builds and edits decks with **your own model API key**. There is no backend. The pane talks directly to whichever endpoint you configure, and nothing else.

- Generates decks from a description, using **your** template's layouts, theme fonts and theme colours
- Edits individual slides without regenerating the deck
- Produces **native, editable** PowerPoint charts — not pictures of charts
- Draws diagrams as real grouped shapes
- Snapshots every slide before it writes, with one-click revert
- Skills, MCP connectors, chat history, dictation, persistent instructions
- Runs as static HTTPS files. Fork it, change one CSS file, deploy it on GitHub Pages or an internal CDN

---

## Quick start (development)

```bash
npm install
npm run certs      # installs the Office dev certificates for https://localhost:3000
npm run dev
```

Then sideload `manifest.xml`:

- **Windows** — [Sideload an add-in in Office on Windows](https://learn.microsoft.com/office/dev/add-ins/testing/create-a-network-shared-folder-catalog-for-task-pane-and-content-add-ins): share a folder containing `manifest.xml`, add it as a trusted catalog under **File → Options → Trust Center → Trusted Add-in Catalogs**, then **Insert → My Add-ins → Shared Folder**.
- **Mac** — copy `manifest.xml` into `~/Library/Containers/com.microsoft.Powerpoint/Data/Documents/wef`, restart PowerPoint, then **Insert → My Add-ins**.
- **Web** — **Insert → Add-ins → Upload My Add-in**.

Open the pane, then **Settings → Provider** and paste a key.

> If `npm install` fails with `UNABLE_TO_GET_ISSUER_CERT_LOCALLY`, you are behind a TLS-inspecting proxy. Run `NODE_OPTIONS=--use-system-ca npm install` so Node trusts your OS certificate store.

## Deploying

```bash
ADDIN_BASE_URL=https://your-host.example.com/addin npm run build
```

`dist/` is then a complete, self-contained deployment: static assets plus `manifest.xml` and `manifest.json` with the URLs rewritten. Serve it over HTTPS. Nothing runs server-side.

For organisations with the Office Store disabled, upload `dist/manifest.xml` through **Microsoft 365 admin center → Settings → Integrated apps → Upload custom apps**.

A GitHub Actions workflow (`.github/workflows/pages.yml`) publishes `dist/` to GitHub Pages on every push to `main`.

## Supported hosts

| Platform | Minimum |
| --- | --- |
| PowerPoint on Windows (Microsoft 365) | Build 16.0.13127.20296 |
| PowerPoint on Mac | 16.46 |
| PowerPoint on the web | Supported |

The add-in requires PowerPointApi 1.3 to load and feature-detects everything above that, degrading rather than throwing. Perpetual and volume-licensed 2016/2019, iPad and Android are out of scope.

| Requirement set | What you lose without it |
| --- | --- |
| 1.4 | Adding shapes, lines and text boxes |
| 1.5 | Reading the selection |
| 1.8 | Snapshots and revert, thumbnails, tables, grouping, reordering, speaker notes |
| 1.9 | Table cell formatting |

## Providers

Model access is a set of adapters behind one interface. Base URL, model id and protocol are all user-editable.

| Provider | Auth | Notes |
| --- | --- | --- |
| Anthropic | `x-api-key` | Sends `anthropic-dangerous-direct-browser-access: true` — browser calls without it are rejected |
| Amazon Bedrock | SigV4 over WebCrypto | Use scoped IAM or short-lived STS credentials. Decodes AWS's binary event stream |
| Google Vertex AI | Bearer token | `gcloud auth print-access-token`; expires hourly |
| Azure AI Foundry | `api-key` | Anthropic Messages shape at your Foundry endpoint |
| OpenAI-compatible | Bearer | Any `/chat/completions` endpoint |
| Local gateway | optional | Ollama, LiteLLM, vLLM, LM Studio — must send permissive CORS headers |

Models are enumerated at runtime from the endpoint. **There is no hardcoded model list anywhere in this codebase.** When an endpoint does not list models — Bedrock, Vertex, most gateways — you type the id and get a record with capabilities marked unknown rather than invented.

Prices are not hardcoded either, for the same reason a stale price table is worse than no number. If the endpoint reports pricing it is used; otherwise set per-model prices under Settings and the per-turn cost readout starts working.

## Where your key lives

Your key is stored in the task pane webview's `localStorage`. **That is not a secret store.** It is not encrypted, and anything with access to that browser profile can read it. Use a key scoped to this purpose and revoke it if the machine is shared. The pane says this out loud before you paste anything.

The add-in emits no telemetry, no analytics, and no outbound traffic beyond the endpoints you configure. See [PRIVACY.md](PRIVACY.md).

## How it works

### Template awareness

Before generating, the add-in builds a catalog from two sources:

1. **The live API** gives authoritative layout ids and names. `slides.add` needs the id and only the host can supply it.
2. **`getFileAsync(Compressed)`** gives what the API does not expose: placeholder names, types and geometry, theme fonts, the colour scheme, and the real slide size. The pptx is unzipped and parsed in the browser.

The second is slow on the web and fails outright in some builds, so it is strictly enrichment — losing it costs placeholder geometry, not the ability to build a deck. The catalog is cached per document and rebuilt only when the deck's layout fingerprint changes.

### Native charts

Office.js has no chart-creation API for PowerPoint, and `setSelectedDataAsync` has no OOXML coercion. So a chart is built as a real DrawingML chart part — plus the embedded workbook PowerPoint opens from "Edit Data" — wrapped in a single-slide `.pptx` and inserted with `insertSlidesFromBase64` using the destination theme.

Consequence: **a chart always arrives as its own new slide.** Series are filled with `schemeClr accent1..6`, so charts adopt the destination deck's palette on landing.

### Speaker notes

The PowerPoint JavaScript API has no notes surface at any requirement set. Reading notes unzips the package. Writing them exports the slide, grafts a `notesSlide` part on, deletes the original and re-inserts the rebuilt one in place.

Consequence: **setting notes recreates the slide, so its id and its shapes' ids change.** The tool description tells the model this, and to set notes last when it is also editing content.

### Undo

The host undo stack is not used. Every write captures the affected slides as standalone `.pptx` payloads first, and Revert rebuilds from those. A snapshot is single-use — restoring re-inserts slides, which gives them new ids.

### Selection

`onSlideSelectionChanged` is preview-only and, per Microsoft's own note, does not fire when the shape selection inside a slide changes. So polling is the primary mechanism and the event, where available, is an accelerator. The selection is re-read at send time and stored with the message, so the transcript records what each turn was actually scoped to.

## Skills

A skill is a markdown file with front matter:

```markdown
---
name: Tighten bullets
slug: tighten-bullets
description: Rewrites bullets to five words or fewer
scope: personal
---

Rewrite every bullet on the selected slides so that:

- the verb comes first
- no bullet exceeds five words
- numbers keep their units

Leave titles and speaker notes alone.
```

Invoke it from the composer with `/tighten-bullets slides 4 to 9`. Both the body and the arguments go to the model. Export writes exactly what import reads, so sharing a skill with a colleague is sending them a `.md`.

## Dictation

Two independent paths:

1. **OS dictation** — Windows Voice typing and macOS Dictation write straight into the composer. No configuration, no permissions, no speech provider. The composer is a native `<textarea>` that is never re-rendered or replaced while text is being injected; `test/dictation.test.ts` asserts no character loss under simulated injection while the selection poller fires.
2. **In-pane microphone** — `getUserMedia` + `MediaRecorder` posted to a speech-to-text endpoint you configure. Adapters for Azure Speech, Deepgram and Whisper-family endpoints. Deepgram streams interim text; the others transcribe on stop.

Speech is configured separately from the model, and deliberately never routed through Anthropic: there is no public Anthropic transcription endpoint, and the first-party dictation service is account-gated and unreachable with a direct API key, Bedrock, Vertex or Foundry.

On Office for the web, microphone permission goes through `Office.context.devicePermission`, which requires the `DevicePermissionService 1.1` requirement set — **web and Chromium only**. Declaring it as a hard manifest requirement would stop the add-in activating on desktop entirely, so it is detected at runtime instead. `manifest.xml` carries the declaration commented out for anyone shipping a web-only build.

## Connectors

An MCP client over HTTP and SSE. stdio servers cannot be reached from a sandboxed task pane, so they are not supported and not pretended about.

Adding a server exposes nothing. Its tools are listed and each must be enabled by name before the model sees it. Connector output is fenced and labelled as untrusted data, and connector tools that write go through the same confirmation gate as edits to your deck.

## Not implemented

Stated plainly rather than left to be discovered:

- **Shared context across Excel, Word and Outlook** — needs sibling add-ins that do not exist here
- **Reapplying a template or theme to existing slides** — no Office.js API supports it
- **SSO, audit logging, a compliance API** — this is a BYOK build with no server
- **Text-to-speech and conversational voice mode**
- **Local on-device speech recognition, Web Speech API**
- **Separate planner and executor models**
- **OCR for scanned PDFs** — a PDF with no text layer is reported as such
- **Bedrock and Vertex have not been exercised against live endpoints.** The SigV4 signer is verified against AWS's published `post-vanilla` test vector, and the event-stream decoder is written to the documented framing, but neither has been run against the real service.

## Layout

```
src/
  lib/        DOM helper, storage, IndexedDB, OOXML plumbing
  ppt/        Everything that touches PowerPoint: catalog, selection, tools,
              charts, diagrams, notes, snapshots, capability probes
  providers/  Model adapters, SigV4, AWS event stream, SSE, model records
  agent/      System prompt, tool loop, compaction
  skills/     Markdown-backed skill store
  mcp/        MCP client
  speech/     Permission, recorder, STT adapters
  ingest/     PDF, XLSX, CSV, text, URL
  ui/         Thread, composer, panels — no component framework
  styles/     tokens.css holds every design decision
```

`src/styles/tokens.css` is the whole design system. Change the values there and the pane rebrands without touching a component.

## Contributing

```bash
npm run typecheck
npm test
npm run build
```

Tests cover the parts where a mistake is silent or catastrophic: chart part structure and schema element order (PowerPoint rejects an entire deck rather than skipping a bad chart), SigV4 against the published AWS vector, selection string formatting, skill markdown round-trips, context compaction, and dictation character loss.

## Licence

MIT. See [LICENSE](LICENSE).

This project is not affiliated with or endorsed by Microsoft or Anthropic.
