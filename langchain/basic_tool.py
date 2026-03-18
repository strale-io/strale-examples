"""Use Strale capabilities as LangChain tools."""
import os
from langchain_strale import StraleToolkit

toolkit = StraleToolkit(api_key=os.environ["STRALE_API_KEY"])

# Invoke a capability directly
result = toolkit.invoke({
    "capability": "email-validate",
    "params": {"email": "hello@example.com"}
})
print(result)
