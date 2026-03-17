"""
Detect the technology stack of any website — one API call.

Identifies frontend framework, CMS, analytics tools, CDN, hosting provider,
and other technologies from HTTP headers and page content.
Use case: Competitive intelligence, lead qualification, market research agents
Price: ~€0.30 per lookup (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/detect-tech-stack.py
"""

import json
import os
import urllib.request


def detect_tech_stack(domain: str) -> dict:
    """Detect the technology stack of a website."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "tech-stack-detect",
            "inputs": {"domain": domain},
            "max_price_cents": 40,
        }).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['STRALE_API_KEY']}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    result = detect_tech_stack("stripe.com")

    output = result.get("output", {})
    print(f"Domain:     {output.get('domain')}")
    print(f"Frontend:   {output.get('frontend_framework', 'N/A')}")
    print(f"CMS:        {output.get('cms', 'N/A')}")
    print(f"CDN:        {output.get('cdn', 'N/A')}")
    print(f"Hosting:    {output.get('hosting', 'N/A')}")
    print(f"Analytics:  {', '.join(output.get('analytics', [])) or 'None detected'}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
