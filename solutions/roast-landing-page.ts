/**
 * AI conversion analysis of any landing page — one API call.
 *
 * Scores headline clarity, CTA strength, value proposition, trust signals,
 * social proof, and identifies the top conversion issues.
 *
 * Use case: Marketing agents, A/B testing prep, competitor analysis
 * Price: ~€0.50 per analysis (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/roast-landing-page.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function roastLandingPage(url: string) {
  const result = await strale.do("landing-page-roast", {
    url,
    max_price_cents: 60,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nLanding Page Analysis: ${url}\n`);
  console.log(`Conversion score: ${output.conversion_score}/100`);
  console.log(`Headline:         ${output.headline_score}/100 — ${output.headline_feedback ?? ""}`);
  console.log(`CTA:              ${output.cta_score}/100 — ${output.cta_text ?? "Not found"}`);
  console.log(`Value prop:       ${output.value_prop_score}/100`);
  console.log(`Trust signals:    ${(output.trust_signals ?? []).join(", ") || "None found"}`);
  console.log(`\nTop issues:`);
  (output.issues ?? []).slice(0, 3).forEach((issue: string) => console.log(`  • ${issue}`));

  console.log(`\nTransaction ID:   ${result.transaction_id}`);
  console.log(`Quality score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

roastLandingPage("https://stripe.com");
