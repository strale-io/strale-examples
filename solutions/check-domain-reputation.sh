#!/bin/bash
# Check a domain's reputation — spam score, blacklists, abuse history
#
# Returns spam score, blacklist matches, abuse reports, and overall reputation grade.
# Use case: Email security agents, vendor assessment, phishing detection
# Price: ~€0.10 per check (covered by €2 free signup credit)
#
# Requires: STRALE_API_KEY environment variable
# Get a free key at https://strale.dev (€2 free credit included)
#
# Run: STRALE_API_KEY=sk_live_... bash solutions/check-domain-reputation.sh example.com

if [ -z "$STRALE_API_KEY" ]; then
  echo "Error: Set STRALE_API_KEY first"
  echo "  Get a free key at https://strale.dev (€2 free credit)"
  echo "  Then: export STRALE_API_KEY=sk_live_..."
  exit 1
fi

DOMAIN="${1:-stripe.com}"

echo "Domain reputation check: $DOMAIN"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -d "{
    \"capability_slug\": \"domain-reputation\",
    \"inputs\": {
      \"domain\": \"$DOMAIN\"
    },
    \"max_price_cents\": 15
  }" | python3 -m json.tool
