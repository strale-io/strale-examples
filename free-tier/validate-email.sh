#!/bin/bash
# Validate an email address — no signup required
#
# Checks: syntax, MX records, disposable domain detection, role-based detection
# Use case: Clean your CRM, validate form inputs, pre-screen leads
#
# This is a free-tier capability — no API key needed.
# Rate limit: 10 calls/day without an API key.
#
# Strale docs: https://strale.dev/docs
# All capabilities: https://strale.dev/capabilities

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "email-validate",
    "inputs": {
      "email": "hello@strale.io"
    }
  }' | python3 -m json.tool

# Expected output:
#
# {
#   "success": true,
#   "output": {
#     "email": "hello@strale.io",
#     "valid": true,
#     "has_mx": true,
#     "is_disposable": false,
#     "is_role_based": true,
#     "domain": "strale.io"
#   },
#   "provenance": { ... },
#   "transaction_id": "tx_...",
#   "sqs": { "score": 99, "label": "Excellent" }
# }
#
# Every response includes provenance (data source, timestamp)
# and the capability's current quality score (SQS).
