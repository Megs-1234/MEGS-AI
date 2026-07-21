from telegram import Update
from telegram.ext import ContextTypes

from together import Together
from config import TOGETHER_API_KEY

client = Together(api_key=TOGETHER_API_KEY)


async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/image your prompt"
        )
        return

    prompt = " ".join(context.args)

    await update.message.reply_text(
        "🎨 Generating image...\nThis may take 10-30 seconds."
    )

    try:
        response = client.images.generate(
            model="stabilityai/stable-diffusion-xl-base-1.0",
            prompt=prompt,
            width=1024,
            height=1024,
            steps=10,
            n=1,
        )

        image_url = response.data[0].url

        await update.message.reply_photo(
            photo=image_url,
            caption=f"🖼 Prompt:\n{prompt}"
        )

    except Exception as e:
        print(e)
        await update.message.reply_text(
            f"❌ Image generation failed.\n\n{e}"
        )