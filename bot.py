import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# យក Token ពី Environment Variable (យើងនឹងកំណត់វានៅលើ Hosting)
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 ចុះឈ្មោះ", url="https://mk137-cysn.github.io/Exam.githu.io/")],
        [InlineKeyboardButton("📢 តាមដានពួកយើង", url="https://t.me/ONLINE_EXAM13")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌟 សួស្តី! សូមជ្រើសរើសសេវាកម្មខាងក្រោម៖", reply_markup=reply_markup)

if __name__ == '__main__':
    # បង្កើត Application
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    application.run_polling()
  
