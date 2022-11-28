from .settings import I18N_DOMAIN, LOCALES_DIR
from aiogram.contrib.middlewares.i18n import I18nMiddleware

i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
_ = i18n.gettext
