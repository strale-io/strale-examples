"""Validate an email address using Strale."""
import os
from straleio import Strale

strale = Strale(api_key=os.environ.get("STRALE_API_KEY", ""))

# email-validate is free — no API key needed
result = strale.do("email-validate", {"email": "hello@strale.dev"})

print(f"Valid: {result['output']['is_valid']}")
print(f"Format OK: {result['output']['format_valid']}")
print(f"MX records: {result['output']['mx_valid']}")
print(f"Quality score: {result['sqs']}")
