# Strale Examples

**Copy-paste examples for AI agent capabilities.** Validate emails, check GDPR compliance, verify companies, enrich leads — all in one API call.

[Strale](https://strale.dev) gives AI agents access to 225+ quality-scored capabilities via MCP, REST API, or SDK. Every capability is continuously tested and scored (Strale Quality Score 0–100). Agents get reliable data. You get audit trails.

## Try it now (no signup needed)

Five capabilities work without an API key. Run this in your terminal:

```bash
curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{"capability_slug":"email-validate","inputs":{"email":"test@example.com"}}' | python3 -m json.tool
```

You'll get a structured JSON response with validation results, provenance metadata, and a quality score — in under a second.

## Examples

### Free tier (no API key required)

| Example | What it does | Language |
|---------|-------------|----------|
| [validate-email.sh](free-tier/validate-email.sh) | Validate any email address — syntax, MX records, disposable detection | Bash/curl |
| [check-iban.py](free-tier/check-iban.py) | Validate IBAN numbers with country and bank identification | Python |
| [repair-json.sh](free-tier/repair-json.sh) | Fix broken JSON from LLM outputs — auto-repair common mistakes | Bash/curl |
| [url-to-markdown.py](free-tier/url-to-markdown.py) | Convert any webpage to clean markdown for RAG pipelines | Python |

### Multi-step solutions (API key required — €2 free credit on signup)

| Example | What it does | Language |
|---------|-------------|----------|
| [audit-gdpr.ts](solutions/audit-gdpr.ts) | Full GDPR compliance audit — cookies, tracking, privacy policy, SSL, DPA | TypeScript |
| [verify-company-sweden.ts](solutions/verify-company-sweden.ts) | Complete KYC check — company data + VAT + sanctions screening | TypeScript |
| [enrich-lead.py](solutions/enrich-lead.py) | Lead enrichment pipeline — email validation, DNS, WHOIS, tech stack | Python |
| [check-website-security.sh](solutions/check-website-security.sh) | Website security audit — SSL, headers, DNS, domain reputation, tech stack | Bash/curl |

### Agent patterns

| Example | What it does | Language |
|---------|-------------|----------|
| [quality-gated-execution.ts](agent-patterns/quality-gated-execution.ts) | Only execute if quality score meets threshold — `min_sqs` pattern | TypeScript |

## Get an API key

1. Go to [strale.dev](https://strale.dev) and create an account
2. You'll get **€2 free credit** — enough for 40+ API calls
3. Set your key: `export STRALE_API_KEY=sk_live_...`
4. Run any example above

## Use with MCP (Claude, Cursor, Windsurf)

Add Strale to your MCP client — no API key needed for free capabilities:

```json
{
  "mcpServers": {
    "strale": {
      "command": "npx",
      "args": ["-y", "strale-mcp"],
      "env": {
        "STRALE_API_KEY": "your_api_key"
      }
    }
  }
}
```

## Use with Python SDK

```bash
pip install straleio
```

```python
from straleio import Strale

strale = Strale(api_key="your_api_key")
result = strale.do("email-validate", inputs={"email": "test@example.com"})
print(result.output)
```

## Use with TypeScript SDK

```bash
npm install straleio
```

```typescript
import { Strale } from 'straleio';

const strale = new Strale({ apiKey: 'your_api_key' });
const result = await strale.do('email-validate', { email: 'test@example.com' });
console.log(result.output);
```

## Why Strale?

- **Quality scores on every capability.** SQS (0–100) across 5 dimensions. Set `min_sqs` thresholds to reject bad data.
- **Audit trails on every call.** Transaction ID, provenance, timing, data source attribution — EU AI Act ready.
- **One API, 225+ capabilities.** Company verification, compliance checks, data extraction, security audits, and more.
- **Growing weekly.** New capabilities ship every Monday through our quality pipeline.

## Links

- [Documentation](https://strale.dev/docs)
- [Trust methodology](https://strale.dev/trust)
- [All capabilities](https://strale.dev/capabilities)
- [All solutions](https://strale.dev/solutions)
- [@strale_io on X](https://x.com/strale_io)
