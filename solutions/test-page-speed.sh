#!/bin/bash
# Run a PageSpeed test and get Core Web Vitals — one API call
#
# Returns: LCP, FCP, CLS, TBT, performance score, and top optimization opportunities
# Use case: Performance monitoring agents, SEO workflows, competitor benchmarking
# Price: ~€0.10 per test (covered by €2 free signup credit)
#
# Requires: STRALE_API_KEY environment variable
# Get a free key at https://strale.dev (€2 free credit included)
#
# Run: STRALE_API_KEY=sk_live_... bash solutions/test-page-speed.sh https://stripe.com

if [ -z "$STRALE_API_KEY" ]; then
  echo "Error: Set STRALE_API_KEY first"
  echo "  Get a free key at https://strale.dev (€2 free credit)"
  echo "  Then: export STRALE_API_KEY=sk_live_..."
  exit 1
fi

URL="${1:-https://stripe.com}"

echo "Page speed test: $URL"
echo ""

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STRALE_API_KEY" \
  -d "{
    \"capability_slug\": \"page-speed-test\",
    \"inputs\": {
      \"url\": \"$URL\"
    },
    \"max_price_cents\": 15
  }" | python3 -m json.tool
