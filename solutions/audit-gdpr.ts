/**
 * Run a full GDPR compliance audit on any website.
 *
 * One API call triggers 5 parallel checks:
 *   1. GDPR website check (consent banners, tracking scripts)
 *   2. Cookie scan (first-party, third-party, categories)
 *   3. Privacy policy analysis (data retention, DPO, rights)
 *   4. SSL certificate check
 *   5. Data protection authority lookup
 *
 * Use case: Compliance agents, vendor assessment, pre-acquisition due diligence
 * Price: ~€1.00 per audit (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/audit-gdpr.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function auditGdpr(url: string, countryCode = "SE") {
  const result = await strale.do("gdpr-audit", {
    url,
    country_code: countryCode,
    max_price_cents: 150,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nGDPR Audit: ${url}\n`);
  console.log(`Overall score:    ${output.gdpr_score}/100 (Grade: ${output.grade})`);
  console.log(`Cookie consent:   ${output.has_cookie_consent ? "Present" : "Missing"}`);
  console.log(`SSL valid:        ${output.ssl_valid ? "Yes" : "No"}`);
  console.log(`Privacy policy:   DPO listed: ${output.privacy_policy?.dpo_listed ?? "unknown"}`);
  console.log(`DPA authority:    ${output.supervisory_authority?.name ?? "N/A"}`);

  console.log(`\nTransaction ID:   ${result.transaction_id}`);
  console.log(`Quality score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

auditGdpr("https://stripe.com", "SE");
