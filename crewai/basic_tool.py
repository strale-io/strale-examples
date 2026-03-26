# Simplest possible Strale + CrewAI usage — call a single capability directly.
# No agent, no LLM — just get the tool and call it.
#
# Requirements:
#   pip install crewai-strale
#   export STRALE_API_KEY=sk_live_...
#
# Note: iban-validate is free-tier — no credits consumed.

import os
from crewai_strale import StraleToolkit

toolkit = StraleToolkit(api_key=os.environ["STRALE_API_KEY"])
tools = toolkit.get_tools()

print(f"Loaded {len(tools)} tools")

# Find iban-validate by name
iban_tool = next(t for t in tools if t.name == "iban-validate")
print(f"Using tool: {iban_tool.name}")

# Call it directly — no agent needed
result = iban_tool._run(iban="GB82WEST12345698765432")
print(f"\nResult: {result}")
