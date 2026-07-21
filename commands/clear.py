from telegram import Update
from telegram.ext import ContextTypes

from database.database import clear_memory


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    clear_memory(user_id)

    await update.message.reply_text(
        "🗑️ Your conversation memory has been cleared."
    )