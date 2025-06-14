from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core import checks


class IslandsmvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'islandsmv'

    def ready(self):
        from .signals import load_islands_fixture
        from django.conf import settings

        post_migrate.connect(load_islands_fixture, sender=self)

        @checks.register(checks.Tags.compatibility)
        def maps_key_check(app_configs, **kwargs):
            if not getattr(settings, "MAPS_API_KEY", None) or not getattr(settings, "MAPS_PRIVATE_KEY", None):
                return [
                    checks.Warning(
                        "Google Maps static preview URLs will not work without MAPS_API_KEY and MAPS_PRIVATE_KEY",
                        id="islandsmv.W001",
                    )
                ]
            return []

