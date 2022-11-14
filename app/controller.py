import os
import datetime
import logging

from api_inova import sync_db

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
    await logger.warning(f"Update {update} caused error {context.error}")


async def schedule_sync_db(update, context):
    context.job_queue.run_daily(
        sync_db, datetime.time(hour=5, minute=0, second=0), days=(0, 1, 2, 3, 4, 5, 6)
    )
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Agendado",
    )


async def stop_notify(update, context):
    chat_id = update.message.chat_id
    jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in jobs:
        job.schedule_removal()
    await context.bot.send_message(
        chat_id=chat_id, text="Tarefas agendadas interrompidas!"
    )


async def teste(update, context):
    chat_id = update.message.chat_id
    await context.bot.send_message(
        chat_id=chat_id,
        text="ON",
    )
