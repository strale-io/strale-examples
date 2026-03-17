"""
WHOIS lookup for any domain — one API call.

Returns registrar, creation date, expiration date, name servers, and owner info
(where available — redacted for privacy-protected domains).
Use case: Domain research, fraud detection, brand protection agents
Price: ~€0.10 per lookup (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/lookup-whois.py
"""

import json
import os
import urllib.request


def whois_lookup(domain: str) -> dict:
    """Run a WHOIS lookup on a domain."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "whois-lookup",
            "inputs": {"domain": domain},
            "max_price_cents": 15,
        }).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['STRALE_API_KEY']}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    result = whois_lookup("stripe.com")

    output = result.get("output", {})
    print(f"Domain:      {output.get('domain')}")
    print(f"Registrar:   {output.get('registrar', 'N/A')}")
    print(f"Created:     {output.get('creation_date', 'N/A')}")
    print(f"Expires:     {output.get('expiration_date', 'N/A')}")
    print(f"Name servers: {', '.join(output.get('name_servers', []))}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
