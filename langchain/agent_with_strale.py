# Full LangChain agent with access to all Strale tools.
# The agent decides which capability to use based on your natural language request.
#
# Requirements:
#   pip install langchain-strale langchain-openai
#   export STRALE_API_KEY=sk_live_...
#   export OPENAI_API_KEY=sk-...

import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_strale import StraleToolkit

toolkit = StraleToolkit(api_key=os.environ["STRALE_API_KEY"])
tools = toolkit.get_tools()
print(f"Loaded {len(tools)} Strale tools")

llm = ChatOpenAI(model="gpt-4o")

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a business data analyst. Use Strale tools to look up company "
     "data, validate financial identifiers, and check compliance information. "
     "Always report what you found in a clear summary."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Example: validate an IBAN and look up a Swedish company
result = executor.invoke({
    "input": (
        "First, validate IBAN DE89370400440532013000. "
        "Then look up Swedish company 556703-7485 and tell me the company name."
    )
})
print("\n" + result["output"])
