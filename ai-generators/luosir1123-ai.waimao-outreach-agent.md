<div align="center">
  <img src="assets/waimao-outreach-agent-banner.svg" alt="Waimao Outreach Agent" width="100%">
</div>

<div align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-2da44e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13-3776ab.svg)](pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-24-339933.svg)](package.json)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688.svg)](apps/api/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-1f2937.svg)](src/outreach_agent/graphs/)

**Evidence-bound customer research, product opportunities, outreach drafts, and editable presentations for foreign-trade teams.**

[中文完整指南](README.zh-CN.md)

</div>

---

## What is Waimao Outreach Agent?

Waimao Outreach Agent is a local-first workbench for turning an approved business account, contact, product evidence, and market sources into reviewable sales material. It supports known-account outreach, product recommendation, single-product market comparison, and standalone customer-presentation workflows.

The system is intentionally human-governed: it drafts and exports approved artifacts, but it has no email-send, campaign-send, or CRM-write capability.

> [!IMPORTANT]
> The default browser stack is a synthetic development fixture. It demonstrates the workflow and its controls; it is not a production release environment. Production remains fail-closed until the documented durable stores, approved sources, authentication, and acceptance evidence are supplied.

## Workflow map

| Workflow | Inputs | Reviewable outputs |
|---|---|---|
| Known-account outreach | official account page, approved contact, target market, 1-3 approved products | account brief, evidence-linked claims, outreach draft variants, editable customer deck |
| Product recommendation | customer context, company catalog, uploaded task materials | ranked product candidates, parameters, gaps, recommendation evidence |
| Market comparison | one approved product, 3-8 approved public sources, price basis | typed price/spec/selling-point matrix, review candidate, verified five-sheet XLSX |
| Standalone presentation | Office documents, images, instructions, optional theme deck | interpreted specification, preview, editable PPTX/PDF after confirmation |

## Evidence and approval flow

```text
Approved inputs and source scope
            |
            v
Bounded account / market research
            |
            v
Claims + Evidence + unknowns
            |
            v
Product match / comparison / draft generation
            |
            v
Human revision and immutable candidate hash
            |
            v
Independent approval
            |
            v
Download-only export (no send or CRM write)
```

Core controls include tenant-scoped sessions, CSRF protection, bounded source policy, evidence lineage, separation of duties, candidate-hash approval, retention rules, and private telemetry allowlists.

## Architecture

```text
React / Vite workbench
          |
          v
FastAPI application API
          |
          +----> PostgreSQL / MinIO / Redis (production-shaped adapters)
          |
          v
LangGraph workflows + policy services
   |          |            |
   v          v            v
Research    RAGFlow      Model gateway
adapters    retrieval    / Ollama
          |
          v
Presentation MCP runtime
  -> LibreOffice / Poppler validation
  -> editable PPTX, PDF, PNG previews
```

## Development fixture demo

Requirements:

- Docker Desktop with Compose v2
- Python 3.13.14
- Node.js 24.18.0
- `uv` 0.11.27

```bash
scripts/toolchain-doctor.sh
docker compose -f deploy/compose.yaml config --quiet
docker compose -f deploy/compose.yaml up -d --build --wait
```

Open:

- <http://localhost:8080> for known-account outreach;
- <http://localhost:8080/market-comparisons/new> for market comparison;
- <http://localhost:8080/presentations/new> for standalone presentation work.

The API starts only when all development guards are explicit: `OUTREACH_ENVIRONMENT=development`, `OUTREACH_AUTH_MODE=development`, and `OUTREACH_FIXTURE_MODE=true`. The fixture uses synthetic `.example` sources and in-memory state.

See the [local runbook](docs/operations/local-runbook.md) for persona switching, diagnostics, contract stubs, and shutdown.

## Production boundary

The repository contains production-shaped domain, policy, persistence, and adapter work, but the default fixture is not a production composition root.

- Non-fixture readiness fails closed when required durable market adapters are absent.
- Production requires governed PostgreSQL/MinIO implementations, approved Source Profiles, file-backed secrets, organization authentication, and recovery evidence.
- A release candidate requires the immutable artifact and real desktop Microsoft PowerPoint validation described in the [acceptance runbook](docs/operations/acceptance-runbook.md).
- Live external market claims require current permitted evidence; uploaded notes and arbitrary social URLs are not automatically trusted.

## Local checks

```bash
uv sync --group dev
uv run pytest --import-mode=importlib
uv run ruff check .
uv run mypy
npm test
npm run build
```

For API-only fixture development:

```bash
OUTREACH_ENVIRONMENT=development \
OUTREACH_AUTH_MODE=development \
OUTREACH_FIXTURE_MODE=true \
uv run uvicorn apps.api.main:app --reload
```

The Compose gateway remains the supported complete browser path because it serves the UI and API from one origin and isolates the presentation runtime.

## Repository map

```text
apps/api/                 FastAPI composition and HTTP surface
apps/web/                 React sales workbench
src/outreach_agent/       domain, application, adapters, workflows, policies
services/presentation/    editable deck generation and validation runtime
deploy/                   development and intranet Compose definitions
docs/operations/          runbooks, acceptance, retention, import procedures
tests/                    unit, contract, integration, E2E, security, evals
```

## Safety principles

- Customer-facing factual claims require current permitted Evidence and deterministic verification.
- Missing values stay unknown; the system must not invent product parameters, prices, contacts, or market facts.
- Final export requires human review and independent approval where configured.
- Production identity is server-derived; callers cannot supply their own tenant override.
- Logs must not contain raw customer documents, prompts, model responses, credentials, or unrestricted payloads.

## Limitations

- Development fixtures do not prove production readiness, recovery, or legal compliance.
- Public web research is bounded by source permissions, static-fetch support, rate limits, and evidence freshness.
- Presentation validation reduces common defects but does not replace human review in desktop PowerPoint.
- The project does not determine lawful basis for outreach or guarantee delivery, replies, or commercial outcomes.

## License

Licensed under the [Apache License 2.0](LICENSE).
