# Auto PPT Studio

[English](./README.md) | [简体中文](./README.zh-CN.md)

Auto PPT Studio is a local-first AI presentation builder that turns long-form documents into chapter-aware slide outlines, generates per-slide visuals, supports reference images, and exports editable `.pptx` decks.

The current UI is still Chinese-first, but this repository has been cleaned up so other people can install and run it locally.

## Highlights

- Paste or upload `.txt`, `.md`, `.docx`, and `.pdf` source material
- Generate a chapter-aware slide outline instead of a flat page split
- Keep per-slide `narrativeRole`, `designIntent`, `layoutLogic`, and `textPlacement`
- Generate one image per slide with optional reference-image input
- Export `image_only`, `editable_overlay`, or `experimental_editable_rebuild` PPTX
- Run locally and release the dev port automatically after the last browser tab closes

## One-Click Windows Start

If you are on Windows, this is the recommended path.

1. Install Node.js 20 or later.
2. Double-click [启动网站.bat](./启动网站.bat) or [start-local.bat](./start-local.bat).
3. On first run, the launcher will:
   - create `.env` from `.env.example`
   - run `npm install` automatically if dependencies are missing
   - start the local server
   - open the browser for you
4. Fill `TEXT_API_KEY` and `OPENAI_API_KEY` in `.env`, or paste them into the runtime config fields in the UI.
5. If you change `.env`, restart once to apply the new values.

To stop the server manually, use [停止网站.bat](./停止网站.bat) or [stop-local.bat](./stop-local.bat).

## Manual Start

If you prefer the CLI path:

```bash
npm install
cp .env.example .env
npm start
```

PowerShell:

```powershell
Copy-Item .env.example .env
npm start
```

Default URL:

[http://localhost:3000](http://localhost:3000)

If `3000` is busy, the server retries `3001`, `3002`, and so on.

## Typical Workflow

1. Paste or upload source content.
2. Set audience, target slide count, and visual direction.
3. Generate the outline.
4. Review and refine the generated slide structure.
5. Upload optional reference images per slide.
6. Generate or regenerate visuals.
7. Export the final PPTX.

## API Configuration

You can configure APIs in two places:

- `.env` for persistent local defaults
- the runtime config fields in the browser for temporary testing

Minimum setup:

```env
TEXT_API_KEY=your_text_api_key
OPENAI_API_KEY=your_image_api_key
```

Common variables:

- `TEXT_API_BASE_URL`
- `TEXT_API_MODEL`
- `OPENAI_BASE_URL`
- `OPENAI_IMAGE_MODEL`
- `OPENAI_IMAGE_SIZE`
- `OPENAI_IMAGE_RESOLUTION`
- `OPENAI_IMAGE_QUALITY`
- `OPENAI_IMAGE_COUNT`
- `IDLE_SHUTDOWN_DELAY_MS`

Backward-compatible aliases are still supported:

- `QWEN_API_KEY`
- `QWEN_API_BASE_URL`
- `QWEN_MODEL`

## Helpful Scripts

```bash
npm run check
npm run verify:parser
npm run verify:planner
```

## Known Limitations

- Planning quality still depends on the upstream text model returning stable JSON.
- Reference-image generation is implemented against an EvoLink-compatible upload-plus-`image_urls` flow.
- `experimental_editable_rebuild` depends on `pdf2slides` OCR quality.
- The UI copy is currently Chinese-first.

## Project Layout

```text
public/   Browser UI
scripts/  Local helper and verification scripts
src/      HTTP server and core libraries
DESIGN.md Default design system input for planning and prompting
```

## License

[MIT](./LICENSE)

## Publishing Notes

See [PUBLISHING_CHECKLIST.md](./PUBLISHING_CHECKLIST.md) before pushing this copy to a public repository.
