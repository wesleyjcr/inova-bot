import os
import datetime
import logging
import requests
import utils 

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from telegram.constants import ParseMode
from api_inova import sync_db

# Enables logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
    utils.url_to_jpg('https://inova.coop.br/inovacoop-api/files/request/9b7763b0-c9df-47aa-8a69-fe01bf73df07-2b0f6693-85f1-4b77-aa5a-a0042fa7a26c-metodos_ageis_detalhe_v2.webp')
    await context.bot.send_photo(
            chat_id=chat_id, 
            photo = open('tmp/image.jpg', 'rb'), 
            caption='<a href="https://inova.coop.br/cursos/scrum-f66153110736">Link</a>',
            parse_mode=ParseMode.HTML
        )



