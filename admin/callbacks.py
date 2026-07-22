from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from admin.helpers import is_admin
from admin.state import broadcast_waiting
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

        cursor.execute("SELECT COUNT(DISTINCT user_id) FROM memory")
        total_users = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM memory")
        total_messages = cursor.fetchone()[0]

        keyboard = [
            [InlineKeyboardButton("⬅ Back", callback_data="home")]
        ]

        await query.edit_message_text(
            f"📊 MEGS AI Statistics\n\n"
            f"👥 Users: {total_users}\n"
            f"💬 Messages: {total_messages}\n\n"
            f"🟢 Status: Online",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # ==========================
    # Users
    # ==========================

    if data == "users":

        cursor.execute(
            "SELECT DISTINCT user_id FROM memory ORDER BY user_id"
        )

        rows = cursor.fetchall()

        text = "👥 Registered Users\n\n"

        for i, row in enumerate(rows, start=1):
            text += f"{i}. {row[0]}\n"

        text += f"\nTotal Users: {len(rows)}"

        keyboard = [
            [InlineKeyboardButton("⬅ Back", callback_data="home")]
        ]

        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # ==========================
    # Broadcast
    # ==========================

    if data == "broadcast":

        broadcast_waiting.add(user_id)

        keyboard = [
            [InlineKeyboardButton("⬅ Back", callback_data="home")]
        ]

        await query.edit_message_text(
            "📢 Send the message you want to broadcast to everyone.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # ==========================
    # Settings
    # ==========================

    if data == "settings":

        keyboard = [
            [InlineKeyboardButton("🤖 AI: Gemini", callback_data="nothing")],
            [InlineKeyboardButton("🖼 Images: Enabled", callback_data="nothing")],
            [InlineKeyboardButton("🌐 Internet: Coming Soon", callback_data="nothing")],
            [InlineKeyboardButton("⬅ Back", callback_data="home")]
        ]

        await query.edit_message_text(
            "⚙️ MEGS AI Settings",
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
            [InlineKeyboardButton("❌ Close", callback_data="close")]
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

        return

    if data == "nothing":

        await query.answer(
            "🚧 Coming Soon!"
        )