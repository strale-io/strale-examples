/**
 * Quality-gated execution — only run if the capability meets your bar.
 *
 * Strale assigns every capability a quality score (SQS, 0-100).
 * Your agent can set a minimum threshold with `min_sqs`.
 * If the capability's current score is below your threshold,
 * the request is rejected — your agent never gets bad data.
 *
 * Use case: Production agents that need reliable data
 *
 * Requires: STRALE_API_KEY environment variable
 * Install: npm install straleio
 * Run:     STRALE_API_KEY=sk_live_... npx tsx agent-patterns/quality-gated-execution.ts
 */

import { Strale } from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function qualityGatedCheck(email: string) {
  try {
    const result = await strale.do("email-validate", {
      email,
      min_sqs: 80,
      max_price_cents: 10,
    });

    console.log(`Quality gate passed (SQS: ${result.sqs?.score})`);
    console.log(`Result: ${JSON.stringify(result.output)}`);
    return result.output;
  } catch (error: any) {
    if (error.message?.includes("min_sqs")) {
      console.log(`Quality gate blocked execution (SQS below threshold)`);
      console.log(`Falling back to manual review queue...`);
      return null;
    }
    throw error;
  }
}

qualityGatedCheck("test@example.com");

// Why this matters for production agents:
//
// Without min_sqs:
//   agent calls API -> gets data -> trusts it blindly -> bad decisions
//
// With min_sqs:
//   agent calls Strale -> quality check passes? -> get data -> trust it
//                       -> quality check fails?  -> fallback -> no bad data
