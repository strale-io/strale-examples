"""
Check email deliverability for a domain — one API call.

Verifies SPF, DKIM, DMARC records, MX configuration, and blacklist status.
Use case: Email marketing agents, domain setup verification, reputation monitoring
Price: ~€0.10 per check (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/check-email-deliverability.py
"""

import json
import os
import urllib.request


def check_deliverability(domain: str) -> dict:
    """Check email deliverability configuration for a domain."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "email-deliverability-check",
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
    result = check_deliverability("stripe.com")

    output = result.get("output", {})
    print(f"Domain:      {output.get('domain')}")
    print(f"SPF:         {'Pass' if output.get('spf_valid') else 'Fail/Missing'}")
    print(f"DKIM:        {'Configured' if output.get('dkim_configured') else 'Not found'}")
    print(f"DMARC:       {'Pass' if output.get('dmarc_valid') else 'Fail/Missing'}")
    print(f"MX records:  {'Present' if output.get('has_mx') else 'Missing'}")
    print(f"Blacklisted: {'Yes' if output.get('is_blacklisted') else 'No'}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
