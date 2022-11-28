from aiogram import Dispatcher
from .start_help import start_help


def register_handlers(dispatcher: Dispatcher) -> None:
  dispatcher.register_message_handler(start_help, commands=['start', 'help'])


__all__ = ('register_handlers',)
