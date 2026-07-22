from telegram import Update
from telegram.ext import ContextTypes

from ai.ai import ask_ai
from admin.ban import is_banned


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text
    user_id = update.effective_user.id

    if is_banned(user_id):

        await update.message.reply_text(
            "🚫 You are banned from using MEGS AI."
        )
        return

    try:

        answer = ask_ai(
            user_id,
            user_message
        )

        await update.message.reply_text(answer)

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "Something went wrong."
        )