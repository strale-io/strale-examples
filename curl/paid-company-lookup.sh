#!/bin/bash
# Look up a Swedish company — requires API key
curl -s -X POST https://api.strale.io/v1/do \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "swedish-company-data",
    "inputs": {"org_number": "5560125790"},
    "max_price_cents": 50
  }' | jq .
