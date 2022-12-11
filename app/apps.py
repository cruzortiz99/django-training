from django.apps import AppConfig as DjAppConfig


class AppConfig(DjAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
