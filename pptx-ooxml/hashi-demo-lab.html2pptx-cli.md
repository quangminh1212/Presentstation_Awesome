# html2pptx-cli

Convert deck-shaped HTML (`#stage` 1280×720, `.slide` sections) to editable 16:9 PowerPoint.

## Quick start

```bash
npm install
npm run build
html2pptx convert fixtures/sample-deck/index.html -o out.pptx
html2pptx diff fixtures/sample-deck/index.html out.pptx
```

## Prerequisites

- Node.js 18+
- Playwright Chromium (`npx playwright install chromium`)
- LibreOffice + Ghostscript (for visual diff / PPTX→PNG)

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Input contract violation |
| 2 | Browser/runtime unavailable |
| 3 | Conversion error |
| 4 | Diff failure (PPTX written) |

## Documentation

- [Input contract](docs/input-contract.md)
- [Validation workflow](docs/validation-workflow.md)
