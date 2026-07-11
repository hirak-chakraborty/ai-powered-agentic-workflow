# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = "voc-162453503315987449858456a4cf80da4e419.26965640"

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_agent.respond(prompt)
# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# The agent used the LLM's built-in knowledge to answer the question because
# no external knowledge source was provided.

# The system prompt influenced the response by making the model answer as a
# college professor and begin its response with "Dear students,".