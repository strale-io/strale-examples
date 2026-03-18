# Strale Examples

Copy-paste examples for [Strale](https://strale.dev) — trust and quality infrastructure for AI agents.

**5 capabilities are free. No signup needed.** Try `email-validate`, `dns-lookup`, `json-repair`, `url-to-markdown`, or `iban-validate` right now.

For all 250+ capabilities: [sign up](https://strale.dev/signup) for €2 in free trial credits.

## Quick Start

```bash
# Free — no API key needed
curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{"capability_slug": "email-validate", "inputs": {"email": "test@example.com"}}' | jq .
```

## Examples by Integration

| Folder | What's inside |
|--------|---------------|
| [`/mcp`](./mcp/) | Config files for Claude Desktop, Cursor, Windsurf, remote MCP |
| [`/python`](./python/) | Python SDK examples — validate, lookup, dry run, error handling |
| [`/typescript`](./typescript/) | TypeScript SDK examples |
| [`/langchain`](./langchain/) | LangChain agent integration |
| [`/curl`](./curl/) | Raw API examples, no SDK needed |

## Examples by Use Case

| Folder | What's inside |
|--------|---------------|
| [`/free-tier`](./free-tier/) | Free capabilities — no API key required |
| [`/solutions`](./solutions/) | Multi-step workflows (KYC, lead enrichment, etc.) |
| [`/agent-patterns`](./agent-patterns/) | Patterns for building agents with Strale |

## Packages

| Package | Install | Description |
|---------|---------|-------------|
| [strale-mcp](https://www.npmjs.com/package/strale-mcp) | `npx -y strale-mcp` | MCP server for Claude, Cursor, Windsurf |
| [straleio](https://www.npmjs.com/package/straleio) | `npm install straleio` | TypeScript SDK |
| [straleio](https://pypi.org/project/straleio/) | `pip install straleio` | Python SDK |
| [langchain-strale](https://pypi.org/project/langchain-strale/) | `pip install langchain-strale` | LangChain integration |
| [crewai-strale](https://pypi.org/project/crewai-strale/) | `pip install crewai-strale` | CrewAI integration |

## Links

- [Documentation](https://strale.dev/docs)
- [Pricing](https://strale.dev/pricing)
- [Quality methodology](https://strale.dev/methodology)
- [Sign up](https://strale.dev/signup)

## License

MIT
