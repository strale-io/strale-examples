"""Validate multiple IBANs in a loop."""
import os
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])

ibans = [
    "DE89370400440532013000",
    "GB29NWBK60161331926819",
    "FR7630006000011234567890189",
    "INVALID_IBAN",
]

for iban in ibans:
    try:
        result = strale.do("iban-validate", {"iban": iban}, max_price_cents=10)
        valid = result["output"]["is_valid"]
        print(f"{iban[:8]}... -> {'✓ Valid' if valid else '✗ Invalid'}")
    except Exception as e:
        print(f"{iban[:8]}... -> Error: {e}")
