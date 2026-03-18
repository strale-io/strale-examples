import Strale from "straleio";

const strale = new Strale({ apiKey: process.env.STRALE_API_KEY! });

async function main() {
  // email-validate is free — no API key needed
  const result = await strale.do("email-validate", {
    email: "hello@strale.dev",
  });

  console.log("Valid:", result.output.is_valid);
  console.log("Format OK:", result.output.format_valid);
  console.log("MX records:", result.output.mx_valid);
  console.log("Quality score:", result.sqs);
}

main().catch(console.error);
