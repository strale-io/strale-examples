#!/bin/bash
# Check SSL certificate validity, expiry, and chain — one API call
#
# Returns: validity, days until expiry, issuer, subject, chain completeness, grade
# Use case: Security monitoring agents, vendor assessment, uptime checking
# Price: ~€0.05 per check (covered by €2 free signup credit)
#
# Requires: STRALE_API_KEY environment variable
# Get a free key at https://strale.dev (€2 free credit included)
#
# Run: STRALE_API_KEY=sk_live_... bash solutions/check-ssl-certificate.sh stripe.com

if [ -z "$STRALE_API_KEY" ]; then
  echo "Error: Set STRALE_API_KEY first"
  echo "  Get a free key at https://strale.dev (€2 free credit)"
  echo "  Then: export STRALE_API_KEY=sk_live_..."
  exit 1
fi

DOMAIN="${1:-stripe.com}"

echo "SSL certificate check: $DOMAIN"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -d "{
    \"capability_slug\": \"ssl-check\",
    \"inputs\": {
      \"domain\": \"$DOMAIN\"
    },
    \"max_price_cents\": 10
  }" | python3 -m json.tool
