"""Handle Strale errors gracefully."""
import os
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])

try:
    result = strale.do(
        "iban-validate",
        {"iban": "INVALID"},
        max_price_cents=10
    )
    print(f"Result: {result['output']}")
except Exception as e:
    error_str = str(e)
    if "402" in error_str:
        print("Insufficient balance — top up at strale.dev")
    elif "404" in error_str:
        print("Capability not found — check the slug")
    elif "422" in error_str:
        print(f"Invalid input: {error_str}")
    elif "503" in error_str:
        print("Capability temporarily unavailable — retry later")
    else:
        print(f"Unexpected error: {error_str}")
