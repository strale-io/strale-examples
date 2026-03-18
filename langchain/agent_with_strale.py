"""Build a LangChain agent that uses Strale for data lookups."""
import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_strale import StraleToolkit

toolkit = StraleToolkit(api_key=os.environ["STRALE_API_KEY"])
llm = ChatOpenAI(model="gpt-4o")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use Strale tools for data lookups."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, [toolkit], prompt)
executor = AgentExecutor(agent=agent, tools=[toolkit])

result = executor.invoke({
    "input": "Validate the IBAN DE89370400440532013000 and tell me if it's valid"
})
print(result["output"])
