#! python3

import logging
from core import polling, webhook
from argparse import ArgumentParser
from aiogram.utils.exceptions import Unauthorized

logger = logging.getLogger(__name__)


def main() -> None:
  if args.webhook:
    webhook()
  else:
    polling()


parser = ArgumentParser(
  'i18n Aiogram Example Bot',
  description='This is the entry point to run the application',
  epilog='Webhook Server might require additional ENV variables'
)

parser.add_argument('--webhook', action='store_true', default=False, help='use webhook server')
args = parser.parse_args()

if __name__ == '__main__':

  try:
    main()
  except Unauthorized:
    logger.fatal('Token is wrong')
