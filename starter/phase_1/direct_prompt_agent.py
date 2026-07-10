# Test script for DirectPromptAgent class

from workflow_agents.base_agents import DirectPromptAgent  # TODO: 1 - Import the DirectPromptAgent class from BaseAgents


# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = "voc-162453503315987449858456a4cf80da4e419.26965640"

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent = DirectPromptAgent(openai_api_key)
direct_agent_response = direct_agent.respond(prompt)
# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("The agent used its built-in knowledge to generate this response.")
