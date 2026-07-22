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

# AI
from ai.chat import chat

# Images
from media.image import image

# Admin
from admin.stats import stats
from admin.users import users
from admin.broadcast import broadcast
from admin.ban import ban, unban


app = ApplicationBuilder().token(TOKEN).build()

# User Commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("clear", clear))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("image", image))

# Admin Commands
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("users", users))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("unban", unban))

# Chat
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("✅ MEGS AI is running...")

app.run_polling()