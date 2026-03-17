"""
Enrich a lead from just an email address — one API call.

Runs 5 checks in sequence:
  1. Email validation (syntax, MX, disposable detection)
  2. DNS lookup (mail server configuration)
  3. Domain reputation (spam score, blacklist status)
  4. WHOIS lookup (registrar, creation date, owner)
  5. Tech stack detection (frontend, CMS, analytics, hosting)

Use case: SDR agents, CRM enrichment, outbound sales qualification
Price: ~€0.65 per enrichment (covered by €2 free signup credit)

Requires: STRALE_API_KEY environment variable
Get a free key at https://strale.dev (€2 free credit included)

Install: pip install straleio
Run:     STRALE_API_KEY=sk_live_... python solutions/enrich-lead.py
"""

import os
from straleio import Strale

strale = Strale(api_key=os.environ["STRALE_API_KEY"])


def enrich_lead(email: str) -> dict:
    """Enrich a lead from their email address."""
    return strale.do("lead-enrich", inputs={"email": email}, max_price_cents=100)


if __name__ == "__main__":
    result = enrich_lead("jane@stripe.com")
    output = result.output

    print(f"\nLead Enrichment: {output.get('email', 'N/A')}\n")
    print(f"Email valid:      {output.get('valid', 'N/A')}")
    print(f"Domain:           {output.get('domain', 'N/A')}")
    print(f"Has MX:           {output.get('has_mx', 'N/A')}")
    print(f"Reputation:       {output.get('reputation_score', 'N/A')}/100")
    print(f"Registrar:        {output.get('registrar', 'N/A')}")

    print(f"\nTransaction:      {result.transaction_id}")
    print(f"Quality score:    {result.sqs.score}/100 ({result.sqs.label})")
