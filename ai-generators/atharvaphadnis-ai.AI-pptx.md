# Aria — AI PowerPoint Generator

Turn any topic into a beautifully designed, downloadable PowerPoint deck. Aria uses your own AI provider key (OpenRouter or Groq), generates structured slides, illustrates them with Pollinations AI, previews everything live, then builds a real `.pptx` on the server with `pptxgenjs`.

Made by **Atharva Phadnis**.

## Screenshot
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/1aa2c5b8-0a74-4916-85dd-2764ee263896" />

## Features

- Bring-your-own-key: OpenRouter or Groq, stored **only in your browser** (`localStorage`).
- Strict-JSON slide generation with automatic retry.
- Live slide preview before you commit to a download.
- Real `.pptx` generation server-side (title slide + content slides + embedded Pollinations images).
- Regenerate on demand; swap models/providers any time from Settings.
- Modular provider registry — add a new provider in one config object.

## Screenshots

_Add screenshots here:_
- `docs/hero.png` — landing + input
- `docs/preview.png` — live slide preview
- `docs/settings.png` — API key modal

## Tech

Built on TanStack Start (React 19 + Vite). AI calls happen **from the browser** directly to the provider you configure. The only server surface is a single route that builds the `.pptx`:

- Frontend: `src/routes/index.tsx`, `src/components/aria/*`, `src/lib/aria-providers.ts`
- Server route: `src/routes/api/generate-ppt.ts` (POST) — accepts `{ slides, topic }` and returns a downloadable `.pptx`.

## Installation

```bash
npm install       # or: bun install
npm run dev       # start the app (frontend + server route)
```

Open the printed local URL. No `.env` is required — Aria never sees your key.

For production:

```bash
npm run build
npm run preview
```

## How to use

1. Click the **Settings** icon (top-right).
2. Pick a **Provider** (OpenRouter or Groq), paste your **API key**, and set a **Model Name** (defaults are provided).
3. Type a topic (e.g. _"The history of the Roman Empire, for a college class"_).
4. Press **Generate slides**. Review the live preview.
5. Click **Regenerate** to try again, or **Download PPT** to get a real `.pptx`.

## API setup

### OpenRouter
1. Sign up at https://openrouter.ai.
2. Create a key at https://openrouter.ai/keys.
3. Paste it into Aria Settings → **OpenRouter API Key**.
4. Suggested free model: `meta-llama/llama-3.3-70b-instruct:free`.

### Groq
1. Sign up at https://console.groq.com.
2. Create a key at https://console.groq.com/keys.
3. Paste it into Aria Settings → **Groq API Key**.
4. Suggested model: `llama-3.3-70b-versatile`.

## Adding a new provider

Providers are defined in `src/lib/aria-providers.ts`:

```ts
export const providers = {
  openrouter: { id, label, endpoint, defaultModel, docsUrl, keyStorageKey },
  groq:       { id, label, endpoint, defaultModel, docsUrl, keyStorageKey },
  // add yours here:
  // together: {
  //   id: "together",
  //   label: "Together AI",
  //   endpoint: "https://api.together.xyz/v1/chat/completions",
  //   defaultModel: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  //   docsUrl: "https://api.together.xyz/settings/api-keys",
  //   keyStorageKey: "together_api_key",
  // },
};
```

The provider must expose an **OpenAI-compatible** `/chat/completions` endpoint. Extend `AriaSettings` with the new `*_api_key` field and add a matching input in `src/components/aria/SettingsDialog.tsx`.

## Error handling

- Missing API key → warning toast + Settings opens.
- Invalid key / provider error → toast with the provider's error message.
- Non-JSON model output → automatic retry without `response_format`, then array extraction.
- Network error → toast with the failure reason.

## Disclaimer!
The above repository is still under progress if you download this version, the app might not work, check the realeases section if you want the correct app files.

## Privacy

Your API keys never leave your browser. The only network traffic Aria's backend sees is `POST /api/generate-ppt` with the slide JSON you already previewed.
