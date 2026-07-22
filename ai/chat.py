from telegram import Update
from telegram.ext import ContextTypes

from ai.ai import ask_ai

from admin.helpers import is_admin
from admin.state import broadcast_waiting

from database.database import cursor


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text
    user_id = update.effective_user.id

    # ==========================
    # ADMIN BROADCAST
    # ==========================

    if user_id in broadcast_waiting and is_admin(user_id):

        broadcast_waiting.remove(user_id)

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
                    text=user_message
                )

                sent += 1

            except Exception:

                failed += 1

        await update.message.reply_text(
            f"✅ Broadcast Complete!\n\n"
            f"Sent: {sent}\n"
            f"Failed: {failed}"
        )

        return

    # ==========================
    # NORMAL AI CHAT
    # ==========================

    try:

        answer = ask_ai(
            user_id,
            user_message
        )

        await update.message.reply_text(answer)

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "❌ Something went wrong."
        )