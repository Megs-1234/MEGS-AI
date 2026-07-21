from openai import OpenAI
from config import OPENROUTER_API_KEY

from ai.memory_db import (
    save_message,
    load_messages
)

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def clean_response(text):

    if not text:
        return "Sorry, I couldn't generate a response."

    replacements = {
        "**": "",
        "__": "",
        "`": "",
        "###": "",
        "##": "",
        "#": "",
        "* ": "• ",
        "*": "",
        "_": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.strip()


def ask_ai(user_id, message):

    save_message(user_id, "user", message)

    messages = load_messages(user_id)

    try:

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages
        )

        if not response.choices:
            return "No response from OpenRouter."

        answer = response.choices[0].message.content

        if not answer:
            return "The AI returned an empty response."

        answer = clean_response(answer)

        save_message(user_id, "assistant", answer)

        return answer

    except Exception as e:
        print(e)
        return f"❌ OpenRouter Error:\n{e}"