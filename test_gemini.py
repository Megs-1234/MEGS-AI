from providers.gemini import ask_gemini

messages = [
    {
        "role": "user",
        "content": "Say hello in one sentence."
    }
]

print(ask_gemini(messages))