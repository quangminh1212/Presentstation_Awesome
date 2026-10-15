# Adding a Spark of Intelligence to Google Workspace Development: Exploring Gemini Managed Agents in Google Apps Script

> **Exploring the Mechanics of Gemini Spark**  
> At Google I/O 2026, Google introduced **Gemini Spark**—*"your 24/7 personal AI agent that helps you work more efficiently by autonomously taking action on your behalf, under your direction... Spark operates in a fully managed, secure runtime on Google Cloud, meaning you get enterprise-grade security without ever having to manage the underlying infrastructure."*

This project is an experiment exploring how to build that same autonomous agent pattern yourself using **[Gemini Managed Agents](https://ai.google.dev/gemini-api/docs/agents)** (Interactions API / Antigravity Agent powered by `gemini-3.7-flash`) and the [Google Workspace CLI (`gws`)](https://github.com/googleworkspace/cli).

The project takes a selected Google Drive folder containing raw Google Docs (in my case, copies of Google Workspace Updates and Gemini Enterprise announcements). We ask our Managed Agent to inventory the folder, retrieve relevant source documents using server-side query filters, and generate multi-format executive briefing assets (Markdown, Word documents, PowerPoint slides, PNG charts, and CSV data registries), which are then automatically uploaded to an approved destination Google Drive folder.

> **Sandbox-only warning**  
> This project delegates a short-lived OAuth bearer token into a remote Managed Agent sandbox so that `gws` can act as the user. The risks in this project are mitigated by using restricted OAuth scopes (`drive.file` and `drive.readonly`). Additional security controls should be considered if developing this project further.

## What it does

1. An Apps Script web app runs as the accessing user.
2. The user supplies a source folder ID, an output folder ID, and an optional date range filter.
3. Apps Script starts a background Gemini Managed Agent interaction.
4. A remote sandbox environment is prepared with:
   - the `gws` Google Workspace CLI;
   - a Python document and analysis toolchain (`pandas`, `matplotlib`, `python-pptx`, `python-docx`);
   - an agent policy (`AGENTS.md`) and workflow skill (`SKILL.md`);
   - a per-run `.env` file containing the user's OAuth access token, approved folder IDs, and date timestamp boundaries.
5. The agent accesses Drive through `gws` using server-side queries (`modifiedTime >= ...`) and auto-pagination (`--page-all --page-limit 5`) to find and retrieve relevant source documents.
6. It generates multi-format deliverables locally under `/workspace/output`.
7. It uploads the final deliverables to the approved output folder with correct MIME types.
8. **Multi-Turn Continuation**: Users can submit follow-up prompts to refine generated documents in the same sandbox without re-running bootstrap or re-installing packages.

```text
Apps Script web app (user-owned deployment)
            |
            | User OAuth token & folder IDs (per-run transient .env)
            v
Gemini Managed Agent Remote Environment (Ubuntu Sandbox)
  - Pre-installed: Python 3.12, Node 22, gcloud CLI, jq, pandas
  - Runtime Tools: gws CLI + Google Drive APIs
  - Policy & Skills: AGENTS.md, update-intelligence/SKILL.md
            |
            v
Selected source and output folders in Google Drive
```

## Why use a Managed Agent here?

A standard Gemini API call is usually the better choice for short, deterministic workflows (e.g. extracting action items from a meeting note and appending them to a Sheet).

This example is intentionally less deterministic. The agent needs to:
1. Inventory the folder and decide which source documents are relevant to the requested period.
2. Selectively export and parse specific Google Docs.
3. Synthesize key themes and compare related announcements.
4. Generate multiple rich file formats locally using Python.
5. Upload the final assets to Google Drive.

The Managed Agent runtime provides sandboxed code execution, local file persistence, iterative tool loops, and background execution—all coordinated through a single API interaction call.

## Multi-Format Deliverables (Python + `gws`)

One of the key strengths of a Managed Agent environment is access to an isolated Linux sandbox with pre-installed tooling and dynamic package installation via `pip`:

| Output Asset | Tooling / Libraries | Pre-installed vs. Runtime | Purpose |
| :--- | :--- | :--- | :--- |
| `source-register.csv` | `pandas` | **Pre-installed** | Aggregates metadata, sorts, and filters document sources. |
| `updates-summary-chart.png` | `matplotlib` | Installed via `pip` | Visualizes update frequencies and product area breakdowns. |
| `executive-presentation.pptx` | `python-pptx` | Installed via `pip` | Compiles an executive presentation deck formatted into structured slides. |
| `executive-briefing.docx` | `python-docx` | Installed via `pip` | Generates a styled Word document with headers, callouts, and structured tables. |
| `executive-briefing.md` | Plain Text / Markdown | Native Filesystem | Provides a lightweight narrative briefing summary. |
| `run-manifest.json` | JSON / `jq` | **Pre-installed** | Audit record of all actions taken during the run. |

## Repository Contents

| File | Purpose |
| :--- | :--- |
| `Code.js` | Apps Script backend: Gemini Interactions API calls, run lifecycle, multi-turn continuation (`continueRun`), and Drive folder validation. |
| `Assets.js` | Inline assets mounted into the sandbox: system policy (`AGENTS.md`), workflow skill (`SKILL.md`), bootstrap script (`bootstrap.sh`), and Python requirements. |
| `Index.html` | Single-page Apps Script UI with live status polling and follow-up interaction controls. |
| `appsscript.json` | Scoped OAuth permissions (`drive.file`, `drive.readonly`, `script.external_request`) and web app configuration. |

## Setup & Deployment

### 1. Create the Apps Script Project

Create a new standalone Apps Script project under a test/sandbox account. Add the files from this repository (or deploy using `clasp push`):

- `Code.js`
- `Assets.js`
- `Index.html`
- `appsscript.json`

### 2. Review Scopes

The manifest requests only the minimum required OAuth scopes:

```json
{
  "oauthScopes": [
    "https://www.googleapis.com/auth/script.external_request",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file"
  ]
}
```

- `script.external_request`: Allows Apps Script to call the Gemini API.
- `drive.readonly`: Allows Drive discovery and source document export.
- `drive.file`: Scopes write access strictly to files created or opened by the application.

### 3. Deploy the Web App

Deploy as a Web App:
- **Execute as:** User accessing the web app
- **Who has access:** Only yourself initially

*Note: "Execute as user accessing" ensures `ScriptApp.getOAuthToken()` represents the active user.*

### 4. Configure and Run

1. Open the Web App URL.
2. Enter your Gemini API key in **Settings** and save.
3. Enter your Source and Output Drive Folder IDs:
   - **Source Folder ID**: Paste the ID of your source folder containing update documents (or test with the sample source folder: `1OS5sdyp0b8T1l8KoMaSb4YuyWp20JVb8`).
   - **Output Folder ID**: Paste the ID of an empty Drive folder where deliverables should be uploaded.
4. Select a Date Range (e.g. `Last 30 days` triggers server-side `modifiedTime` queries).
5. Click **Start managed-agent run**.
6. Once completed, use the **Follow-up / Refine Run** card to continue the conversation in the same sandbox.

## How Delegation Works

Apps Script retrieves a short-lived user access token:

```javascript
const userToken = ScriptApp.getOAuthToken();
```

`Code.js` injects it into a transient per-run `/workspace/.env` file:

```text
GOOGLE_WORKSPACE_CLI_TOKEN=...
SOURCE_FOLDER_ID=...
OUTPUT_FOLDER_ID=...
SINCE_TIMESTAMP=...
GOOGLE_WORKSPACE_CLI_CONFIG_DIR=/workspace/.gws-config
PYTHONUNBUFFERED=1
```

The `gws` CLI uses this token for authentication, allowing the remote agent to interact with Drive without an interactive login prompt in the headless sandbox.

## Security Considerations

- **OAuth Scopes are the Real Boundary**: System instructions in `AGENTS.md` tell the agent to stay within specific folders, but the real security boundary is the OAuth scope (`drive.file` and `drive.readonly`).
- **Sandbox Token Access**: The token exists only in memory and inside the ephemeral per-run `/workspace/.env` file. It is never stored in Script Properties or database records.
- **Indirect Prompt Injection Defense**: `AGENTS.md` explicitly instructs the model to treat all retrieved Workspace document content as untrusted reference data.

## Google AI Studio vs. Gemini Enterprise Agent Platform (Vertex AI)

| Feature / Capability | Google AI Studio (Developer API) | Gemini Enterprise Agent Platform (Vertex AI) |
| :--- | :--- | :--- |
| **Primary Target** | Prototyping, developer apps, open demos | Enterprise applications, production workloads |
| **Authentication** | API Key (`x-goog-api-key`) | Google Cloud IAM (Service Accounts, OAuth 2.0) |
| **Agent Resources** | Inline configuration or persistent named agents (`POST /v1beta/agents`) | Persistent named agent resources (`POST /agents`) with IAM bindings |
| **Skill & File Mounting** | Inline payload strings, Cloud Storage (`gs://...`), and Git | Cloud Storage (`gs://...`), Git, and central Skill Registry |
| **Network Security** | Domain allowlists (`network.allowlist`) & Egress Proxy | Strict domain allowlists, Egress Proxy, & VPC Service Controls (VPC-SC) |
| **Audit & Governance** | Execution step logs, usage metrics, & Hooks telemetry | Cloud Audit Logs & enterprise compliance controls |
| **Setup Overhead** | **Very Low** (zero GCP IAM setup) | **Moderate** (GCP project, IAM roles, bucket setup) |

## References

- [Gemini Managed Agents Overview](https://ai.google.dev/gemini-api/docs/agents)
- [Building Custom Agents](https://ai.google.dev/gemini-api/docs/custom-agents)
- [Antigravity Agent Capabilities](https://ai.google.dev/gemini-api/docs/antigravity-agent)
- [Agent Environments Documentation](https://ai.google.dev/gemini-api/docs/agent-environment)
- [Google Workspace CLI (`gws`) Repository](https://github.com/googleworkspace/cli)
- [Google Workspace CLI `AGENTS.md`](https://github.com/googleworkspace/cli/blob/main/AGENTS.md)

*Special thanks to Ryota Tokodai ([*ryotat7*](https://github.com/ryotat7)) whose early work inspired this experimental architecture.*
