from telegram import Update
from telegram.ext import ContextTypes

from admin.helpers import is_admin
from database.database import cursor


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/broadcast Your message"
        )
        return

    message = " ".join(context.args)

    cursor.execute(
        "SELECT DISTINCT user_id FROM memory"
    )

    users = cursor.fetchall()

    sent = 0
    failed = 0

    for row in users:

        try:

            await context.bot.send_message(
                chat_id=row[0],
                text=message
            )

            sent += 1

        except Exception:

            failed += 1

    await update.message.reply_text(
        f"✅ Broadcast Finished\n\n"
        f"Sent: {sent}\n"
        f"Failed: {failed}"
    )