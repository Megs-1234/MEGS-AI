from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import TOKEN

from commands.start import start
from commands.help import help_command
from commands.clear import clear

from about import about

from ai.chat import chat

from media.image import image

# Admin Commands
from admin.stats import stats


app = ApplicationBuilder().token(TOKEN).build()

# User Commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("clear", clear))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("image", image))

# Admin Commands
app.add_handler(CommandHandler("stats", stats))

# Chat
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("✅ MEGS AI is running...")

app.run_polling()