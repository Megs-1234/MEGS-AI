import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")