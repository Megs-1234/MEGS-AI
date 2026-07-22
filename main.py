from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import TOKEN

# User Commands
from commands.start import start
from commands.help import help_command
from commands.clear import clear
from about import about

# AI Chat
from ai.chat import chat

# Image Generation
from media.image import image

# Admin Commands
from admin.stats import stats
from admin.users import users
from admin.broadcast import broadcast


app = ApplicationBuilder().token(TOKEN).build()

# ==========================
# USER COMMANDS
# ==========================
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("clear", clear))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("image", image))

# ==========================
# ADMIN COMMANDS
# ==========================
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("users", users))
app.add_handler(CommandHandler("broadcast", broadcast))

# ==========================
# AI CHAT
# ==========================
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("✅ MEGS AI is running...")

app.run_polling()