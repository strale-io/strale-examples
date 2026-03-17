"""
Batch processing pattern — process a list of items through Strale with error handling.

Shows how to loop through items, handle per-item errors, collect results, and
respect rate limits in a real agent workflow.

Use case: Bulk validation, batch enrichment, list processing agents

Requires: STRALE_API_KEY environment variable
Install:  pip install straleio
Run:      STRALE_API_KEY=sk_live_... python agent-patterns/batch-processing.py
"""

import os
import time
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])

EMAILS = [
    "alice@stripe.com",
    "bob@example.com",
    "invalid-email",
    "carol@shopify.com",
    "dave@disposablemail.com",
]

DELAY_BETWEEN_CALLS = 0.2  # seconds — adjust based on your plan's rate limit


def process_batch(items: list[str]) -> list[dict]:
    results = []
    for i, email in enumerate(items):
        try:
            result = strale.do("email-validate", inputs={"email": email}, max_price_cents=5)
            results.append({
                "input": email,
                "valid": result.output.get("valid"),
                "sqs": result.sqs.score,
                "transaction_id": result.transaction_id,
                "error": None,
            })
            print(f"[{i+1}/{len(items)}] {email} — valid={result.output.get('valid')} SQS={result.sqs.score}")
        except Exception as e:
            results.append({"input": email, "valid": None, "sqs": None, "error": str(e)})
            print(f"[{i+1}/{len(items)}] {email} — error: {e}")

        if i < len(items) - 1:
            time.sleep(DELAY_BETWEEN_CALLS)

    return results


if __name__ == "__main__":
    print(f"Processing {len(EMAILS)} emails...\n")
    results = process_batch(EMAILS)

    valid = sum(1 for r in results if r["valid"] is True)
    errors = sum(1 for r in results if r["error"])
    print(f"\nDone. {valid}/{len(EMAILS)} valid, {errors} errors")
