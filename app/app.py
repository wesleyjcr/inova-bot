import os 

from telegram import Update
from telegram.ext import (
    CommandHandler,
    ApplicationBuilder,
)
from dotenv import load_dotenv
from controller import schedule_sync_db, start

def main():
    """"Starts the bot"""
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    #CHANEL = os.getenv("CHANNEL")

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sync", schedule_sync_db))
    application.run_polling()


if __name__ == "__main__":
    main()