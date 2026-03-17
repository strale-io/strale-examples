"""
Convert any webpage to clean markdown — no signup required.

Fetches a URL, strips navigation/ads/boilerplate, returns clean markdown.
Use case: RAG pipelines, content ingestion, research agents.

This is a free-tier capability — no API key needed.
Rate limit: 10 calls/day without an API key.

Strale docs: https://strale.dev/docs
"""

import json
import urllib.request

def url_to_markdown(url: str) -> dict:
    """Fetch a URL and convert to clean markdown."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "url-to-markdown",
            "inputs": {"url": url}
        }).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    result = url_to_markdown("https://example.com")

    output = result.get("output", {})
    markdown = output.get("markdown", "")

    print(f"Word count: {output.get('word_count', len(markdown.split()))}")
    print(f"Preview:\n{markdown[:500]}")
    print(f"\nTransaction: {result.get('transaction_id')}")
