/**
 * Compare two company websites head-to-head — one API call.
 *
 * Analyzes positioning, pricing model, feature set, target audience,
 * trust signals, and content strategy for both companies.
 *
 * Use case: Market research agents, investor due diligence, strategic planning
 * Price: ~€1.00 per comparison (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/compare-competitors.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function compareCompetitors(urlA: string, urlB: string) {
  const result = await strale.do("competitor-compare", {
    url_a: urlA,
    url_b: urlB,
    max_price_cents: 120,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nCompetitor Comparison: ${urlA} vs ${urlB}\n`);
  console.log(`Positioning A: ${output.positioning_a ?? "N/A"}`);
  console.log(`Positioning B: ${output.positioning_b ?? "N/A"}`);
  console.log(`Pricing model A: ${output.pricing_model_a ?? "N/A"}`);
  console.log(`Pricing model B: ${output.pricing_model_b ?? "N/A"}`);
  console.log(`Target audience A: ${output.target_audience_a ?? "N/A"}`);
  console.log(`Target audience B: ${output.target_audience_b ?? "N/A"}`);
  console.log(`\nKey differentiator: ${output.key_differentiator ?? "N/A"}`);

  console.log(`\nTransaction ID:   ${result.transaction_id}`);
  console.log(`Quality score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

compareCompetitors("https://stripe.com", "https://adyen.com");
