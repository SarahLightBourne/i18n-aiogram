from .settings import dispatcher, telegram_bot
from .settings import WEBHOOK_HOST, WEBHOOK_PATH, WEBHOOK_PORT

from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook


async def on_startup(dispatcher: Dispatcher) -> None:
  await telegram_bot.set_webhook(f'{WEBHOOK_HOST}{WEBHOOK_PATH}')


async def on_shutdown(dispatcher: Dispatcher) -> None:
  await telegram_bot.delete_webhook()


def webhook() -> None:
  start_webhook(
    dispatcher,
    webhook_path=WEBHOOK_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    host='localhost',
    port=WEBHOOK_PORT
  )
