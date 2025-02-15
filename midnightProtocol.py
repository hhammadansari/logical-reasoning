# Three agents (Alpha, Bravo, Charlie) are tasked with disarming a bomb hidden in one of three locations:
# Vault, Server Room, or Garage. 
# Each agent has a tool (Wirecutters, Keycard, Explosives) and makes a statement. 
# However, one of them is a double agent whose statements are false. 
# The goal is to determine:

# 1. Where is the bomb?
# 2. Who is the double agent?
# 3. Which tool is needed to disarm it?


# Clue 1: Agent Statements

# Alpha:
# "The bomb is in the Vault if and only if Bravo has the Keycard."

# Bravo:
# "If I’m not the double agent, the bomb is in the Server Room."

# Charlie:
# "The bomb is in the Garage, and I have the Explosives."


# Clue 2: Tool Constraints
# Only one tool is needed to disarm the bomb, depending on its location:

# Vault: Wirecutters
# Server Room: Keycard
# Garage: Explosives

