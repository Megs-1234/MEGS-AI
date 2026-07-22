from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from admin.helpers import is_admin
from database.database import cursor


async def admin_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    if not is_admin(user_id):
        return

    data = query.data

    # ==========================
    # Statistics
    # ==========================

    if data == "stats":

        cursor.execute(
            "SELECT COUNT(DISTINCT user_id) FROM memory"
        )
        total_users = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM memory"
        )
        total_messages = cursor.fetchone()[0]

        keyboard = [
            [InlineKeyboardButton("⬅ Back", callback_data="home")]
        ]

        await query.edit_message_text(
            text=(
                "📊 MEGS AI Statistics\n\n"
                f"👥 Users: {total_users}\n"
                f"💬 Messages: {total_messages}\n\n"
                "🟢 Bot Status: Online"
            ),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # ==========================
    # Home
    # ==========================

    if data == "home":

        keyboard = [
            [InlineKeyboardButton("📊 Statistics", callback_data="stats")],
            [InlineKeyboardButton("👥 Users", callback_data="users")],
            [InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")],
            [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
            [InlineKeyboardButton("❌ Close", callback_data="close")],
        ]

        await query.edit_message_text(
            "👑 MEGS AI Admin Panel",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # ==========================
    # Close
    # ==========================

    if data == "close":

        await query.edit_message_text(
            "✅ Admin panel closed."
        )