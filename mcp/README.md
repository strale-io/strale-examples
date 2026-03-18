# Strale MCP Server Examples

Use Strale capabilities directly in Claude Desktop, Cursor, Windsurf, and any MCP-compatible client.

5 capabilities are free — no API key needed: `email-validate`, `dns-lookup`, `json-repair`, `url-to-markdown`, `iban-validate`.

For all 250+ capabilities, sign up at [strale.dev](https://strale.dev) for €2 in free trial credits.

## Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

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

## Cursor

Add to `.cursor/mcp.json` in your project root:

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

## Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

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

## Remote MCP (no install needed)

For clients that support remote MCP servers (Streamable HTTP):

```json
{
  "mcpServers": {
    "strale": {
      "type": "streamableHttp",
      "url": "https://api.strale.io/mcp",
      "headers": {
        "Authorization": "Bearer your_api_key"
      }
    }
  }
}
```

## Available Meta-Tools

Once connected, your agent has access to these tools:

| Tool | Description |
|------|-------------|
| `strale_search` | Find capabilities by keyword (no auth required) |
| `strale_execute` | Run any capability |
| `strale_methodology` | Get quality scoring methodology |
| `strale_trust_profile` | Get detailed quality profile for a capability |
| `strale_balance` | Check wallet balance |
| `strale_transaction` | Look up a past transaction |
| `strale_ping` | Health check |

## Try It

After adding the config, ask your agent:

- "Use Strale to validate the email hello@example.com"
- "Use Strale to check the DNS records for github.com"
- "Search Strale for company data capabilities"
