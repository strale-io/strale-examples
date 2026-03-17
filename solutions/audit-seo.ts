/**
 * Run an SEO audit on any webpage — one API call.
 *
 * Checks title tags, meta descriptions, h1 structure, image alt tags,
 * Open Graph tags, schema.org markup, and canonical URLs.
 *
 * Use case: Marketing agents, competitor analysis, content optimization
 * Price: ~€0.30 per audit (covered by €2 free signup credit)
 *
 * Requires: STRALE_API_KEY environment variable
 * Get a free key at https://strale.dev (€2 free credit included)
 *
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx solutions/audit-seo.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function auditSeo(url: string) {
  const result = await strale.do("seo-audit", {
    url,
    max_price_cents: 40,
  });

  const output = result.output as Record<string, any>;

  console.log(`\nSEO Audit: ${url}\n`);
  console.log(`SEO score:        ${output.seo_score}/100`);
  console.log(`Title:            ${output.title ?? "Missing"}`);
  console.log(`Meta description: ${output.meta_description ? "Present" : "Missing"}`);
  console.log(`H1 tags:          ${output.h1_count ?? 0}`);
  console.log(`Images missing alt: ${output.images_missing_alt ?? 0}`);
  console.log(`Open Graph:       ${output.has_open_graph ? "Present" : "Missing"}`);
  console.log(`Schema.org:       ${output.has_schema ? "Present" : "Missing"}`);

  console.log(`\nTransaction ID:   ${result.transaction_id}`);
  console.log(`Quality score:    ${result.sqs?.score}/100 (${result.sqs?.label})`);
}

auditSeo("https://stripe.com");
