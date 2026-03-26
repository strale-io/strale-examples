# Full CrewAI agent with access to all Strale tools.
# The agent decides which capability to use based on the task description.
#
# Requirements:
#   pip install crewai-strale
#   export STRALE_API_KEY=sk_live_...
#   export OPENAI_API_KEY=sk-...

import os
from crewai import Agent, Task, Crew
from crewai_strale import StraleToolkit

toolkit = StraleToolkit(api_key=os.environ["STRALE_API_KEY"])
tools = toolkit.get_tools()
print(f"Loaded {len(tools)} Strale tools")

analyst = Agent(
    role="EU Business Compliance Analyst",
    goal="Verify European companies and check their compliance status",
    backstory=(
        "You are a compliance analyst specializing in EU business verification. "
        "You use Strale tools to look up company data, validate VAT numbers, "
        "and screen against sanctions lists."
    ),
    tools=tools,
    verbose=True,
)

task = Task(
    description=(
        "Validate the IBAN DE89370400440532013000 and confirm it belongs to a "
        "German bank. Then look up Swedish company 556703-7485 and report the "
        "company name and status."
    ),
    expected_output="A brief report with IBAN validation result and company details",
    agent=analyst,
)

crew = Crew(agents=[analyst], tasks=[task], verbose=True)
result = crew.kickoff()
print(f"\nResult: {result}")
