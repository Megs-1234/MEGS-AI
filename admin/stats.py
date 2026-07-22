from telegram import Update
from telegram.ext import ContextTypes

from admin.helpers import is_admin

from database.database import cursor


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return

    cursor.execute(
        "SELECT COUNT(DISTINCT user_id) FROM memory"
    )

    total_users = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM memory"
    )

    total_messages = cursor.fetchone()[0]

    text = (
        "📊 MEGS AI Statistics\n\n"
        f"👥 Total Users: {total_users}\n"
        f"💬 Total Messages: {total_messages}"
    )

    await update.message.reply_text(text)