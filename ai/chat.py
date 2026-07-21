from telegram import Update
from telegram.ext import ContextTypes

from ai.ai import ask_ai


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text
    user_id = update.effective_user.id

    try:
        answer = ask_ai(user_id, user_message)

        await update.message.reply_text(answer)

    except Exception as e:

        print("========== CHAT ERROR ==========")
        print(e)
        print("================================")

        await update.message.reply_text(
            f"❌ Error:\n{e}"
        )