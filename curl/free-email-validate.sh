#!/bin/bash
# Validate an email — FREE, no API key needed
curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "email-validate",
    "inputs": {"email": "hello@example.com"}
  }' | jq .
