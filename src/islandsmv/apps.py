from django.apps import AppConfig
from django.db.models.signals import post_migrate


class IslandsmvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'islandsmv'

    def ready(self):
        from .signals import load_islands_fixture
        post_migrate.connect(load_islands_fixture, sender=self)

