#!/bin/bash
# Preview cost without executing
curl -s -X POST https://api.strale.io/v1/do \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "web-extract",
    "inputs": {"url": "https://example.com"},
    "dry_run": true
  }' | jq .
