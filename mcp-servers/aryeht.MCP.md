# Slides (Marp + Kroki)

This folder hosts slides built with [Marp CLI](https://github.com/marp-team/marp-cli) and the Kroki diagram engine.

## Prerequisites

- Node.js (LTS)
- Docker + Docker Compose (for running Kroki locally)

## Install

- Install dependencies (Marp CLI is already listed in `package.json`):

```bash
npm install
```

## Start Kroki locally

- A Docker Compose setup for Kroki is included in this project under `./kroki`.
- Start it before serving the slides (Marp is configured to use `http://localhost:8000`):

```bash
cd kroki
docker compose up -d
# Kroki should now listen on http://localhost:8000
```

## Serve the slides (with local assets allowed)

Run Marp in server mode from this directory so it picks up `marp.config.js` and the `slides/` content:

```bash
npx marp -s -c marp.config.js --allow-local-files
# → Server: http://localhost:8080/
```

Notes:
- The `--allow-local-files` flag is required because slides include local images/assets from `slides/`.
- The short option `-c` must be followed directly by the config file path (`-c marp.config.js`).

## Project layout

- Slides entry: `slides/pres.md`
- Marp config (enables Kroki): `marp.config.js`

## Troubleshooting

- Error: "Could not find or parse configuration file (EISDIR)" — ensure the command uses `-c marp.config.js` before other flags:

```bash
# Correct
npx marp -s -c marp.config.js --allow-local-files

# Common mistake (will fail)
# npx marp -s -c --allow-local-files marp.config.js
```

- Make sure Kroki is up at `http://localhost:8000` before rendering diagrams. The Marp config points Marp/Kroki to this endpoint.
