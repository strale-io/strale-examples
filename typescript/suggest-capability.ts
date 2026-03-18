import Strale from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function main() {
  // Use semantic search to find the right capability
  const suggestions = await strale.suggest(
    "verify a Swedish company for KYC"
  );

  console.log("Top matches:");
  for (const match of suggestions.slice(0, 3)) {
    console.log(`  ${match.slug} — ${match.description} (€${match.price_cents / 100})`);
  }
}

main().catch(console.error);
