# Nix Anywhere Else

> "The store path isn't a prison. It's a starting point."

A Slidev presentation about the "dark arts" of ELF surgery and Nix, built entirely with Nix. This talk explores how `patchelf` and a deep understanding of the Executable and Linkable Format can make binaries portable in both directions: bringing foreign tools *into* NixOS, and taking Nix-built artifacts *out* to the rest of the world.

Delivered at **Planet Nix @ SCaLE 23x (March 2026)**.

## Quick Start

This repo is a **sealed, reproducible environment**. You don't need to install Slidev or Node globally; Nix handles the entire toolchain.

```bash
# Enter the situated development shell
nix develop

# Start the dev server with hot-reload
slidev

# Perform a pure, offline build
nix build
```

## Viewing the Presentation

**The Artifacts:**
The latest stable build is committed in the `output/` directory for quick reference.

- [**PDF Version**](./output/nix_anywhere_else.pdf) — For offline reading or sharing.
- [**HTML Version**](./output/html/index.html) — The full interactive Slidev experience (requires a local server).

**Local Build:**
If you've run `nix build`, your local result is sitting in `./result/`.

```bash
# Serve the built presentation
nix run .#serve
```

*Note: Slidev assets use absolute paths. You cannot open the HTML files directly from the filesystem; they must be served over HTTP.*

## The Philosophy: Situated Presentations

We treat this talk like a mission-critical service. 

1.  **Hermetic Packaging**: Every theme, font, and dependency is pre-fetched and hashed. No network calls are allowed during the build phase.
1.  **[slidev-nix](https://github.com/noblepayne/slidev-nix)**: We use a custom, Nix-native Slidev expression to ensure the presentation environment is as reproducible as the binaries it describes.

## Commands

| Command | Description |
|---------|-------------|
| `nix develop` | Enter dev shell with Node, NPM, and Slidev CLI |
| `slidev` | Start the Vite-powered dev server |
| `nix build` | Build the final static bundle (pure, offline) |
| `./scripts/update-hash.sh` | Ossify dependencies after a `package.json` change |

---

*“NixOS is a portable binary factory — if you know how to open the door.”*

| Command | Description |
|---------|-------------|
| `nix develop` | Enter dev shell with node + npm + slidev |
| `slidev` | Start dev server (hot reload) |
| `nix build` | Build static HTML (pure, offline) |
| `nix fmt` | Format code |
| `./scripts/update-hash.sh` | Update npm deps hash after changing package.json |

## Updating Dependencies

When you change `package.json` (add themes, etc.):

```bash
# Update the npmDepsHash in flake.nix
./scripts/update-hash.sh

# Rebuild
nix build
```

## Files

- `slides.md` - Your presentation content
- `package.json` - Themes and npm dependencies
- `flake.nix` - Nix build configuration
- `scripts/update-hash.sh` - Helper to update dependencies
