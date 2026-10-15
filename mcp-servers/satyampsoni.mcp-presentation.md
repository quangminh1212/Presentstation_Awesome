# MCP · Interactive Learning Canvas

An **interactive, browser-based learning experience** that teaches the **Model
Context Protocol (MCP)** — not a slide deck. Built on the **tldraw** infinite
canvas, it's one connected world you travel through, discovering *why MCP exists*
by solving the problem yourself.

Designed for a 30-minute session with university students who each open the link
on their own laptop and interact while the presenter guides the pace.

## The journey (9 chapters, one canvas)

1. **AI is Amazing** — pick a model, give it tasks, everything works.
2. **The Wall** — ask for something real; the AI is sealed in a glass room.
3. **M × N** — wire every model to every tool; watch it explode to 2,500.
4. **Invent MCP** — choose a fix, discover the protocol, M×N collapses to M+N.
5. **Architecture** — drag Host / Client / Server into place; watch it talk.
6. **Tool Calls** — decide: guess, hallucinate, or call a tool? Equip abilities.
7. **Primitives** — sort Tools · Resources · Prompts into their buckets.
8. **Live Build** — code a server line by line; each line lights the pipeline.
9. **Full Journey** — one request, end to end, through every piece you've met.

## Run it

```bash
npm install
npm run dev      # http://localhost:5173
```

Production build / preview:

```bash
npm run build
npm run preview
```

## Controls

| Input | Action |
|-------|--------|
| `→` / `Space` | Reveal next idea |
| `←` | Step back |
| `P` | Toggle Presenter ⇄ Student |
| `R` | Replay current chapter |
| `Home` | Jump to start |
| Drag canvas / scroll | Pan & zoom freely |

**URL params:** `?c=<0-8>` deep-links to a chapter · `?tour=0` skips the intro.

## Deploy (fully static, no backend)

Works on GitHub Pages, Cloudflare Pages, Netlify, or Vercel. Output is `dist/`.
For a project subpath (e.g. GitHub Pages), set the base:

```bash
VITE_BASE=/your-repo/ npm run build
```

## Tech

React · TypeScript · Vite · **tldraw** (canvas + camera) · Tailwind CSS v4 ·
Motion · Lucide.

See [`HANDOFF.md`](./HANDOFF.md) for architecture, conventions, and how to add a
chapter.
