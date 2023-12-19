from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    class Meta:
        verbose_name = 'Hisob'
        verbose_name_plural = 'Hisoblar'
