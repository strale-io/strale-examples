"""
Screen a person or company against global sanctions lists — one API call.

Checks UN, EU, OFAC, and other consolidated sanctions lists for exact and fuzzy matches.
Use case: Compliance agents, KYC workflows, vendor onboarding
Price: ~€0.15 per check (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/screen-sanctions.py
"""

import json
import os
import urllib.request


def screen_sanctions(name: str, country_code: str = None) -> dict:
    """Screen a name against UN, EU, OFAC, and other global sanctions lists."""
    inputs = {"name": name}
    if country_code:
        inputs["country_code"] = country_code

    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "sanctions-check",
            "inputs": inputs,
            "max_price_cents": 20,
        }).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ['STRALE_API_KEY']}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    result = screen_sanctions("Acme Trading LLC", country_code="RU")

    output = result.get("output", {})
    print(f"Name:       {output.get('name')}")
    print(f"Sanctioned: {'YES — BLOCKED' if output.get('is_sanctioned') else 'No match found'}")
    print(f"Lists hit:  {', '.join(output.get('lists_matched', [])) or 'None'}")
    print(f"Match type: {output.get('match_type', 'N/A')}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
