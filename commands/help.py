from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 MEGS AI COMMANDS

/start
Start the bot

/help
Show all commands

/clear
Clear your conversation memory

💬 You can also send me any normal message and I'll reply using AI.

Examples:
• Tell me a joke
• Explain Python
• Write a CV
• Summarize a paragraph
"""

    await update.message.reply_text(text)