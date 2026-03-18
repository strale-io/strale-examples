#!/bin/bash
# Browse all available capabilities
curl -s https://api.strale.io/v1/capabilities | jq '.[] | {slug, category, price_cents, sqs}'
