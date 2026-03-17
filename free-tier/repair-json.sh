#!/bin/bash
# Fix broken JSON from LLM outputs — no signup required
#
# LLMs frequently produce invalid JSON: trailing commas, unquoted keys,
# single quotes, markdown fences, comments, missing brackets.
# This capability auto-repairs all of it.
#
# Use case: Agent pipelines that parse LLM structured output
#
# This is a free-tier capability — no API key needed.
# Rate limit: 10 calls/day without an API key.
#
# Strale docs: https://strale.dev/docs

curl -s -X POST https://api.strale.io/v1/do \
  -H "Content-Type: application/json" \
  -d '{
    "capability_slug": "json-repair",
    "inputs": {
      "text": "```json\n{name: \"Alice\", age: 30, active: True, tags: [\"dev\", \"ai\",],}\n```"
    }
  }' | python3 -m json.tool

# What gets fixed:
#
# Input (broken):  ```json\n{name: "Alice", age: 30, active: True, tags: ["dev", "ai",],}\n```
# Output (valid):  {"name": "Alice", "age": 30, "active": true, "tags": ["dev", "ai"]}
#
# Fixes applied:
# - Stripped markdown code fences
# - Added quotes around keys
# - Fixed Python booleans (True → true)
# - Removed trailing commas
