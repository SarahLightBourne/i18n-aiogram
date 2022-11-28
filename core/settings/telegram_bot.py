from .settings import TG_TOKEN

import logging
from sys import exit
from aiogram import Bot
from aiogram.utils.exceptions import ValidationError

logger = logging.getLogger(__name__)

try:
  telegram_bot = Bot(TG_TOKEN)
except ValidationError:
  logger.fatal('Token is invalid')
  exit(1)
