from django.apps import AppConfig


class MarketfaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketface'

    class Meta:
        verbose_name = 'BB Market'
        verbose_name_plural = 'BB Marketlar'
