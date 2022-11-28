from aiogram import Dispatcher

from typing import Dict
from aiogram.types import Update

from .i18n import i18n
from aiogram.contrib.middlewares import logging


class LoggingMiddleware(logging.LoggingMiddleware):

  async def on_pre_process_error(self, update: Update, error: Exception, data: Dict) -> None:
    self.logger.exception('Uncaught Exception')


def setup_middlewares(dispatcher: Dispatcher) -> None:
  dispatcher.middleware.setup(LoggingMiddleware())
  dispatcher.middleware.setup(i18n)
