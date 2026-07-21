from telegram import Update
from telegram.ext import ContextTypes


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 MEGS AI

Version: 1.0

Developer: MEGS 

Powered by:
• Python
• Telegram Bot API
• OpenRouter AI

Thank you for using MEGS AI ❤️
"""

    await update.message.reply_text(text)