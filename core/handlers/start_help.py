from ..settings.i18n import _
from aiogram.types import Message


async def start_help(message: Message) -> None:
  await message.answer(_('Hello'))
