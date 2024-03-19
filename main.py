import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import scrape

STEAM_URL = f"https://steamcommunity.com/market/search?appid=730&q={scrape.ITEM}"
CURRENCY_URL = "https://www.forbes.com/advisor/money-transfer/currency-converter/usd-idr/"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# TELE BOT CONFIG
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=scrape.scrape(s_url=STEAM_URL, cur_url=CURRENCY_URL)
                                   )


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    show_handler = CommandHandler('show', show)
    application.add_handler(show_handler)

    # Run the bot until you send a signal to stop it
    application.run_polling()
