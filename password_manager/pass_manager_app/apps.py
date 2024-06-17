from django.apps import AppConfig

from .config.cipher_manager_config import configurate_cipher_manager


class PassManagerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pass_manager_app'
    configurate_cipher_manager()
