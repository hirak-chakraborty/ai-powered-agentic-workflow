# Test script for DirectPromptAgent class

import os
from dotenv import load_dotenv

from workflow_agents.base_agents import DirectPromptAgent

# Load environment variables
load_dotenv()

# Load the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

direct_agent = DirectPromptAgent(openai_api_key)
direct_agent_response = direct_agent.respond(prompt)

print(direct_agent_response)

print("The agent used its built-in knowledge to generate this response.")