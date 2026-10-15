# Designing MCP Tools — Deutsche Bank engineering session

Materials for an internal talk on designing Model Context Protocol (MCP) tools well,
with a runnable Spring AI reference server as the worked example.

## Contents

| Path | What it is |
|---|---|
| `slides/Designing-MCP-Tools-DB.pptx` | The 20-slide deck (Deutsche Bank themed, speaker notes on every slide). |
| `slides/Designing-MCP-Tools-DB.pdf` | PDF render of the deck. |
| `document/Designing-MCP-Tools-Transcript-and-FAQ.docx` | Full speaker transcript plus 18 FAQs. |
| `document/Designing-MCP-Tools-Transcript-and-FAQ.pdf` | PDF render of the document. |
| `db-payments-mcp/` | Runnable Spring Boot + Spring AI MCP server — the reference implementation. |
| `logo/` | Deutsche Bank mark used in the deck. |

## The reference server

`db-payments-mcp` is a mock Deutsche Bank payments copilot. It exists to demonstrate MCP
**tool design**, not banking — every data source is in-memory and deterministic. Five tools,
one resource, one prompt, an `antipatterns` profile showing the bad versions, eight evaluation
tasks, and a `ToolContractTest` that fails the build if a tool breaks the design rules.

```bash
cd db-payments-mcp
mvn test          # run the unit + contract tests
mvn spring-boot:run   # start the Streamable-HTTP MCP server on :8080
```

See `db-payments-mcp/README.md` for the full tour.

## The eight principles

1. Build the workflow, not the API.
2. Search, don't list.
3. Namespace like you expect company.
4. The description is a prompt, not a javadoc.
5. Parameters are prompts too.
6. Return meaning, not identifiers.
7. Say what you withheld — and what to do about it.
8. An error message is an instruction.

## References

- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — Anthropic
- [Spring AI — MCP Server Annotations](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-annotations-server.html)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)
