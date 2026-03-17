#!/bin/bash
# Look up DNS records for any domain — no signup required
#
# Returns A, AAAA, MX, TXT, NS, and CNAME records in one call.
# Use case: Domain verification, email deliverability pre-check, infrastructure recon
#
# This is a free-tier capability — no API key needed.
# Rate limit: 10 calls/day without an API key.
#
# Strale docs: https://strale.dev/docs
# All capabilities: https://strale.dev/capabilities

DOMAIN="${1:-strale.io}"

echo "DNS lookup: $DOMAIN"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d "{
    \"capability_slug\": \"dns-lookup\",
    \"inputs\": {
      \"domain\": \"$DOMAIN\"
    }
  }" | python3 -m json.tool

# Expected output:
#
# {
#   "success": true,
#   "output": {
#     "domain": "strale.io",
#     "a": ["1.2.3.4"],
#     "mx": [{"priority": 10, "exchange": "mail.strale.io"}],
#     "txt": ["v=spf1 include:... ~all"],
#     "ns": ["ns1.strale.io", "ns2.strale.io"]
#   },
#   "transaction_id": "tx_...",
#   "sqs": { "score": 99, "label": "Excellent" }
# }
