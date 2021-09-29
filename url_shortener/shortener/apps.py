from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShortenerConfig(AppConfig):
    name = "url_shortener.shortener"
    verbose_name = _("Users")

    def ready(self):
        try:
            import url_shortener.shortener.signals  # noqa F401
        except ImportError:
            pass
