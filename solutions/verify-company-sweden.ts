/**
 * Complete KYC check on a Swedish company — one API call.
 *
 * Runs 3 checks in parallel:
 *   1. Swedish company data (Bolagsverket registration, org number, status)
 *   2. EU VAT validation (VIES)
 *   3. Sanctions screening (UN, EU, OFAC consolidated lists)
 *
 * Use case: Onboarding agents, procurement workflows, partner due diligence
 * Price: ~€0.60 per check (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/verify-company-sweden.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function verifySwedishCompany(companyName: string) {
  const result = await strale.do("kyc-sweden", {
    company_name: companyName,
    max_price_cents: 100,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nKYC Check: ${companyName}\n`);
  console.log(`Company:      ${output.company_name ?? "Not found"}`);
  console.log(`Org number:   ${output.org_number ?? "N/A"}`);
  console.log(`Status:       ${output.status ?? "Unknown"}`);
  console.log(`VAT valid:    ${output.vat_valid ? "Yes" : "No"}`);
  console.log(`Sanctioned:   ${output.is_sanctioned ? "YES" : "No"}`);

  console.log(`\nTransaction:  ${result.transaction_id}`);
  console.log(`SQS score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

verifySwedishCompany("Spotify AB");
