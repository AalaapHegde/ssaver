from django.apps import AppConfig

#configuring database to the 'base' foldeer
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'