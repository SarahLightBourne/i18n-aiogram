from .middlewares import setup_middlewares
from ..handlers import register_handlers

from aiogram import Dispatcher
from .telegram_bot import telegram_bot

dispatcher = Dispatcher(telegram_bot)

setup_middlewares(dispatcher)
register_handlers(dispatcher)
