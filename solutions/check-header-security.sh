#!/bin/bash
# Audit HTTP security headers for any domain — one API call
#
# Checks: Content-Security-Policy, HSTS, X-Frame-Options,
# X-Content-Type-Options, Referrer-Policy, Permissions-Policy
# Use case: Security compliance, penetration testing agents, vendor assessment
# Price: ~€0.05 per check (covered by €2 free signup credit)
#
# Requires: STRALE_API_KEY environment variable
# Get a free key at https://strale.dev (€2 free credit included)
#
# Run: STRALE_API_KEY=sk_live_... bash solutions/check-header-security.sh stripe.com

if [ -z "$STRALE_API_KEY" ]; then
  echo "Error: Set STRALE_API_KEY first"
  echo "  Get a free key at https://strale.dev (€2 free credit)"
  echo "  Then: export STRALE_API_KEY=sk_live_..."
  exit 1
fi

DOMAIN="${1:-stripe.com}"

echo "Security headers audit: $DOMAIN"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -d "{
    \"capability_slug\": \"header-security-check\",
    \"inputs\": {
      \"domain\": \"$DOMAIN\"
    },
    \"max_price_cents\": 10
  }" | python3 -m json.tool
