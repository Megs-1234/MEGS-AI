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

    # Save user's message
    save_message(
        user_id,
        "user",
        message
    )

    # Load previous conversation
    messages = load_messages(user_id)

    try:

        # Ask Gemini
        answer = ask_gemini(messages)

        # Clean response
        answer = clean_response(answer)

        # Save AI response
        save_message(
            user_id,
            "assistant",
            answer
        )

        return answer

    except Exception as e:

        print("===================================")
        print("GEMINI ERROR")
        print("===================================")
        print(type(e))
        print(e)
        print("===================================")

        return (
            f"❌ GEMINI ERROR\n\n"
            f"{type(e).__name__}\n\n"
            f"{e}"
        )