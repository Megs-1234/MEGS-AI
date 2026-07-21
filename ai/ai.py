print("🔥 GEMINI VERSION LOADED")

from providers.gemini import ask_gemini

from ai.memory_db import (
    save_message,
    load_messages
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

    save_message(
        user_id,
        "user",
        message
    )

    messages = load_messages(user_id)

    try:

        answer = ask_gemini(messages)

        answer = clean_response(answer)

        save_message(
            user_id,
            "assistant",
            answer
        )

        return answer

    except Exception as e:

        print(e)

        return "Sorry, Gemini is currently unavailable. Please try again in a few minutes."