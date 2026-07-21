from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(messages):

    prompt = ""

    for message in messages:

        role = message["role"]
        content = message["content"]

        if role == "system":
            prompt += f"System: {content}\n"

        elif role == "user":
            prompt += f"User: {content}\n"

        elif role == "assistant":
            prompt += f"Assistant: {content}\n"

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text