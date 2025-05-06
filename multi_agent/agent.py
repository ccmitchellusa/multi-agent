from .host_agent import HostAgent

remote_agent_addresses = [
    'https://elf-agent.1uo9xqkaspg3.us-east.codeengine.appdomain.cloud',
    'https://orc-agent.1uo9xqkaspg3.us-east.codeengine.appdomain.cloud'
]

# First argument is the array of agent URLs that this agent will be the host for.
root_agent = HostAgent(remote_agent_addresses).create_agent()
print("Created agent:", root_agent.name)