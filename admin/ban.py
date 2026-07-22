from telegram import Update
from telegram.ext import ContextTypes

from admin.helpers import is_admin

banned_users = set()


async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/ban USER_ID"
        )
        return

    target = int(context.args[0])

    banned_users.add(target)

    await update.message.reply_text(
        f"✅ User {target} has been banned."
    )


async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_admin(user_id):
        await update.message.reply_text(
            "❌ You are not authorized."
        )
        return

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/unban USER_ID"
        )
        return

    target = int(context.args[0])

    banned_users.discard(target)

    await update.message.reply_text(
        f"✅ User {target} has been unbanned."
    )


def is_banned(user_id):

    return user_id in banned_users