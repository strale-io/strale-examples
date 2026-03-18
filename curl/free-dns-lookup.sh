#!/bin/bash
# DNS lookup — FREE, no API key needed
curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "dns-lookup",
    "inputs": {"domain": "strale.dev"}
  }' | jq .
