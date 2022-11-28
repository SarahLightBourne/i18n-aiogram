from ..utils import get_env_var

from sys import argv
import logging.config
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
logging.config.fileConfig(BASE_DIR / 'logging.conf')

# i18n
I18N_DOMAIN = 'bot'
LOCALES_DIR = BASE_DIR / 'locales'

# Telegram
TG_TOKEN = get_env_var('TG_TOKEN')

# Webhook
WEBHOOK_HOST = None
WEBHOOK_PATH = None
WEBHOOK_PORT = get_env_var('WEBHOOK_PORT', 3001)

if '--webhook' in argv:
  WEBHOOK_HOST = get_env_var('WEBHOOK_HOST')
  WEBHOOK_PATH = get_env_var('WEBHOOK_PATH')
