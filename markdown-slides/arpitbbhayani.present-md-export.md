# present-md-export

Export [present-md](https://github.com/arpitbbhayani/present-md) markdown presentations to PDF using a headless browser.

## Install globally

```bash
npm install -g present-md-export
```

## Usage

```bash
present-md-export slides.md                          # export to slides.pdf
present-md-export slides.md -o out.pdf               # custom output path
present-md-export slides.md --theme light            # light theme (default: dark)
present-md-export slides.md --width 1280 --height 720  # custom slide dimensions
```

## Options

| Flag                | Default       | Description                         |
| ------------------- | ------------- | ----------------------------------- |
| `-o, --output`      | `<file>.pdf`  | Output PDF path                     |
| `--theme`           | `dark`        | Color theme: `dark` or `light`      |
| `--width`           | `1920`        | Slide width in pixels               |
| `--height`          | `1080`        | Slide height in pixels              |

## How it works

`present-md-export` spins up a local HTTP server, renders your slides in a headless Chromium browser, and captures each slide as a PDF page at the exact viewport dimensions you specify.

If `present-md` is not installed, the tool clones it from GitHub, installs dependencies, and builds it automatically before exporting.

## Running without installation

```bash
npx present-md-export slides.md
```

## Publishing

This package is published as `present-md-export` on npm.

### Pre-publish checklist

- All changes are committed and the working tree is clean
- `npm run build` succeeds without errors
- The `dist/` directory reflects the latest source
- `package.json` has `"files": ["dist"]` so only compiled output is shipped

### Update the version

Edit `package.json` manually or use npm's version command, which also commits and tags:

```bash
# patch: 1.0.0 -> 1.0.1
npm version patch

# minor: 1.0.0 -> 1.1.0
npm version minor

# major: 1.0.0 -> 2.0.0
npm version major
```

`npm version` updates `package.json`, creates a git commit (`v1.2.3`), and tags it. Push both the commit and the tag:

```bash
git push origin master --tags
```

### Build and publish

```bash
npm run build
npm publish --access public
```

`--access public` is required on the first publish. It is safe to include on every subsequent publish.

### Verify the release

```bash
npm info present-md-export
```

Check that `version` and `dist-tags.latest` match what you just published.
