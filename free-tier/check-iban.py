"""
Validate an IBAN number — no signup required.

Checks structure, country code, check digits, and identifies the bank.
Use case: Payment processing, onboarding forms, financial compliance.

This is a free-tier capability — no API key needed.
Rate limit: 10 calls/day without an API key.

Strale docs: https://strale.dev/docs
"""

import json
import urllib.request

def validate_iban(iban: str) -> dict:
    """Validate an IBAN and get bank identification details."""
    req = urllib.request.Request(
        "https://api.strale.io/v1/do",
        data=json.dumps({
            "capability_slug": "iban-validate",
            "inputs": {"iban": iban}
        }).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


if __name__ == "__main__":
    result = validate_iban("SE3550000000054910000003")

    output = result.get("output", {})
    print(f"IBAN:    {output.get('iban')}")
    print(f"Valid:   {output.get('valid')}")
    print(f"Country: {output.get('country_name', output.get('country_code'))}")
    print(f"Bank:    {output.get('bank_name', 'N/A')}")

    sqs = result.get("sqs", {})
    print(f"\nQuality score: {sqs.get('score')}/100 ({sqs.get('label')})")
    print(f"Transaction:   {result.get('transaction_id')}")
