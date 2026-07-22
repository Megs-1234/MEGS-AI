from telegram import Update
from telegram.ext import ContextTypes

from admin.helpers import is_admin
from database.database import cursor


async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return

    cursor.execute("""
        SELECT DISTINCT user_id
        FROM memory
        ORDER BY user_id
    """)

    rows = cursor.fetchall()

    if not rows:
        await update.message.reply_text(
            "No users found."
        )
        return

    text = "👥 MEGS AI Users\n\n"

    for number, row in enumerate(rows, start=1):
        text += f"{number}. {row[0]}\n"

    text += f"\nTotal Users: {len(rows)}"

    await update.message.reply_text(text)