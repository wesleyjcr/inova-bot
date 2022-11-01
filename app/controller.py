import datetime
import logging

from model import sync_db

# Enables logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update, context):
    """Sends a message when the command /start is issued."""
    await update.message.reply_text("Seja bem vindo ao bot do Inovacoop!")


async def error(update, context):
    """Logs Errors caused by Updates."""
    await logger.warning('Update "%s" caused error "%s"', update, context.error)    


async def schedule(update, context):
    context.job_queue.run_daily(sync_db, datetime.time(hour= 5, minute= 0, second= 0), days=(0, 1, 2, 3, 4, 5, 6))