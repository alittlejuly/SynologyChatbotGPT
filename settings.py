import os

# Replace with your OpenAI API key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Replace with your Synology Chat bot details
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")

# Port
PORT = 5008


# This system prompt sets up the character of the chatbot; change it if you want
SYSTEM_PROMPT = '''你是xxx的chatGPT助手'''


# Set maximum conversation exchanges or idle time gap to start a new conversation
MAX_CONVERSATION_LEN = os.getenv("MAX_CON_LEN", default=10)
MAX_TIME_GAP = os.getenv("MAX_TIME_GAP", default=15)  # minutes


# Set temperature -- a parameter in the OpenAI API that controls the randomness of the generated text.
# It is a floating-point value that ranges from 0 to 1. A higher value (e.g., 0.8) will result in more random
# and creative outputs, while a lower value (e.g., 0.2) will produce more focused and deterministic outputs.
# In this case, the temperature is set to 0.5, which provides a balance between creativity and determinism
# in the generated text.
TEMPERATURE = os.getenv("TEMPERATURE", default=0.5)
