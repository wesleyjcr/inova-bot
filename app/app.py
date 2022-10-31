import os 

from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ApplicationBuilder,
)
from dotenv import load_dotenv
from controller import start


def main():
    """"Starts the bot"""
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    #CHANEL = os.getenv("CHANNEL")

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()


if __name__ == "__main__":
    main()