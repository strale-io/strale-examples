#!/bin/bash
# Run a full website security audit — one API call
#
# Checks 7 security dimensions in parallel:
#   1. SSL certificate (validity, expiry, chain)
#   2. HTTP security headers (CSP, HSTS, X-Frame-Options)
#   3. DNS security (DNSSEC, SPF, DMARC)
#   4. Domain reputation (blacklists, spam score)
#   5. WHOIS data (registrar, creation date)
#   6. Technology stack (server, framework, CDN)
#   7. US company data (if applicable)
#
# Use case: Vendor assessment, security compliance, procurement agents
# Price: ~€1.80 per audit (covered by €2 free signup credit)
#
# Requires: STRALE_API_KEY environment variable
# Get a free key at https://strale.dev (€2 free credit included)

if [ -z "$STRALE_API_KEY" ]; then
  echo "Error: Set STRALE_API_KEY first"
  echo "  Get a free key at https://strale.dev (€2 free credit)"
  echo "  Then: export STRALE_API_KEY=sk_live_..."
  exit 1
fi

DOMAIN="${1:-stripe.com}"

echo "Security audit: $DOMAIN"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -d "{
    \"capability_slug\": \"website-security-audit\",
    \"inputs\": {
      \"company\": \"$DOMAIN\",
      \"domain\": \"$DOMAIN\"
    },
    \"max_price_cents\": 200
  }" | python3 -m json.tool
