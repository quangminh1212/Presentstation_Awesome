# MCP presentation

## Quickstart

```bash
# Install slidev globally
npm install -g slidev
npm install
slidev
# open http://localhost:3030
```

## Build and deploy for production
```bash
slidev build

# preview the build `dist/index.html`
npx vite preview
```

## Export to `.pptx` | `.pdf` | `.md`
```bash
# prerequisite: install playwright
npm i -D playwright-chromium

# Export to different formats
slidev export --format pptx
slidev export --format pdf
slidev export --format md
```

## Helpful commands

```bash
npm install @slidev/types
npm i -D prettier prettier-plugin-slidev
npm install monaco-editor
npm install slidev-addon-tldraw

```

---

**Slidev Addon Python Runner (`slidev-addon-python-runner` add in future)**

```bash
# Optional configuration for this runner
python:
# Install packages from PyPI. Default: []
installs: ["cowsay"]
# Code executed to set up the environment. Default: ""
prelude: |
  GREETING_FROM_PRELUDE = "Hello, Slidev!"
# Automatically load the imported builtin packages. Default: true
loadPackagesFromImports: true
# Disable annoying warning from `pandas`. Default: true
suppressDeprecationWarnings: true
# Always reload the Python environment when the code changes. Default: false
alwaysReload: false
# Options passed to `loadPyodide`. Default: {}
loadPyodideOptions: {}
```

---

## Slidev
> Slidev is a presentation tool with a focus on developer experience, and it allows you to create slides using Markdown. It supports various features like themes, transitions, and even interactive components.

```bash
npm install -g slidev

### Create a new Slidev project
slidev init my-presentation
cd my-presentation

### Run the development server
slidev
```