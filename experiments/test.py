from dotenv import load_dotenv
import os

load_dotenv()

# Read a value
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)