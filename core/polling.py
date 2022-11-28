from .settings import dispatcher

import logging
from aiogram import Dispatcher
from aiogram.utils.executor import start_polling

logger = logging.getLogger(__name__)


async def on_startup(dispatcher: Dispatcher) -> None:
  me = await dispatcher.bot.get_me()
  logger.info(f'Polling started for {me.first_name}@{me.username}')


def polling() -> None:
  start_polling(
    dispatcher,
    on_startup=on_startup
  )
