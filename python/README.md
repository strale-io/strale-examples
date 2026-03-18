# Strale Python SDK Examples

Install: `pip install straleio`

These examples use the Strale Python SDK to call capabilities directly.

## Quick Start

```python
from straleio import Strale

strale = Strale(api_key="your_api_key")
result = strale.do("email-validate", {"email": "test@example.com"})
print(result)
```

## Examples

| File | Description |
|------|-------------|
| `validate_email.py` | Validate an email address |
| `company_lookup.py` | Look up a company by org number |
| `dry_run.py` | Preview cost before executing |
| `error_handling.py` | Handle errors gracefully |
| `batch_validate.py` | Validate multiple IBANs in a loop |
