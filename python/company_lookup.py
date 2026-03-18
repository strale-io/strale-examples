"""Look up a Swedish company by organization number."""
import os
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])

result = strale.do(
    "swedish-company-data",
    {"org_number": "5560125790"},
    max_price_cents=50
)

company = result["output"]
print(f"Name: {company['name']}")
print(f"Status: {company['status']}")
print(f"Quality score: {result['sqs']}")
