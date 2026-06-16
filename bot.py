import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def handle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower().strip()
    
    if any(word in user_text for word in ["привет", "здравствуй", "добрый", "хай"]):
        reply = "Здравствуйте! Чем могу помочь?"
    else:
        reply = "Здравствуйте! Чем могу помочь?"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
print("Бот запущен...")
app.run_polling()
