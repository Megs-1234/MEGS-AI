from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from admin.helpers import is_admin


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    # Ignore everyone except the owner
    if not is_admin(user_id):
        return

    keyboard = [
        [
            InlineKeyboardButton("📊 Statistics", callback_data="stats")
        ],
        [
            InlineKeyboardButton("👥 Users", callback_data="users")
        ],
        [
            InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")
        ],
        [
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ],
        [
            InlineKeyboardButton("❌ Close", callback_data="close")
        ],
    ]

    await update.message.reply_text(
        "👑 MEGS AI Admin Panel",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )