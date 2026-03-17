/**
 * Analyze a website's privacy policy — one API call.
 *
 * Extracts data retention periods, DPO contact, user rights, third-party sharing,
 * cookie usage, and GDPR compliance signals.
 *
 * Use case: Compliance agents, vendor risk assessment, GDPR audits
 * Price: ~€0.25 per analysis (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/analyze-privacy-policy.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function analyzePrivacyPolicy(url: string) {
  const result = await strale.do("privacy-policy-analyze", {
    url,
    max_price_cents: 35,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nPrivacy Policy Analysis: ${url}\n`);
  console.log(`GDPR compliant:   ${output.gdpr_compliant ? "Signals present" : "Issues found"}`);
  console.log(`DPO listed:       ${output.dpo_listed ? "Yes" : "No"}`);
  console.log(`Data retention:   ${output.data_retention ?? "Not specified"}`);
  console.log(`User rights:      ${(output.user_rights ?? []).join(", ") || "Not specified"}`);
  console.log(`Third-party share: ${output.shares_with_third_parties ? "Yes" : "No"}`);

  console.log(`\nTransaction ID:   ${result.transaction_id}`);
  console.log(`Quality score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

analyzePrivacyPolicy("https://stripe.com/privacy");
