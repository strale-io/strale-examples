"""Preview cost before executing a capability."""
import os
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])

# Dry run — no charge, shows what would happen
preview = strale.do(
    "web-extract",
    {"url": "https://example.com"},
    dry_run=True
)

print(f"This would cost: €{preview['price_cents'] / 100:.2f}")
print(f"Capability SQS: {preview['sqs']}")

# Execute if price is acceptable
if preview["price_cents"] <= 50:
    result = strale.do(
        "web-extract",
        {"url": "https://example.com"},
        max_price_cents=50
    )
    print(f"Extracted {len(result['output']['text'])} characters")
