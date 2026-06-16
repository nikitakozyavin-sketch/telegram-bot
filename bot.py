import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def handle(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Здравствуйте! Чем могу помочь?")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
print("Бот запущен...")
app.run_polling()

