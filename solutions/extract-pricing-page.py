"""
Extract structured pricing data from any SaaS pricing page — one API call.

Returns plans, features per plan, pricing, billing periods, and trial/free-tier info.
Use case: Competitive intelligence agents, market research, procurement
Price: ~€0.30 per extraction (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/extract-pricing-page.py
"""

import json
import os
import urllib.request


def extract_pricing(url: str) -> dict:
    """Extract structured pricing data from a SaaS pricing page."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "pricing-page-extract",
            "inputs": {"url": url},
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
    result = extract_pricing("https://stripe.com/pricing")

    output = result.get("output", {})
    plans = output.get("plans", [])
    print(f"URL:         {output.get('url')}")
    print(f"Plans found: {len(plans)}")
    for plan in plans:
        price = plan.get("price", "N/A")
        period = plan.get("billing_period", "")
        print(f"  {plan.get('name')}: {price} {period}")
    print(f"Free trial:  {output.get('has_free_trial', False)}")
    print(f"Free tier:   {output.get('has_free_tier', False)}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
