"""
Validate an EU VAT number against the VIES database — one API call.

Returns validity, company name, and registered address from the official EU VIES service.
Use case: Invoice validation, B2B onboarding, EU compliance
Price: ~€0.10 per check (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Run: STRALE_API_KEY=sk_live_... python solutions/validate-vat-number.py
"""

import json
import os
import urllib.request


def validate_vat(vat_number: str) -> dict:
    """Validate an EU VAT number via the VIES database."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "eu-vat-validate",
            "inputs": {"vat_number": vat_number},
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
    result = validate_vat("SE556036079301")

    output = result.get("output", {})
    print(f"VAT number:  {output.get('vat_number')}")
    print(f"Valid:       {output.get('valid')}")
    print(f"Company:     {output.get('company_name', 'N/A')}")
    print(f"Address:     {output.get('address', 'N/A')}")
    print(f"Country:     {output.get('country_code')}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
