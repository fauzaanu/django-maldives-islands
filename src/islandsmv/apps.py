from django.apps import AppConfig
from django.db.models.signals import post_migrate


class IslandsmvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'islandsmv'

    def ready(self):
        from .signals import load_islands_fixture
        from django.conf import settings
        import warnings

        post_migrate.connect(load_islands_fixture, sender=self)

        if not getattr(settings, "MAPS_API_KEY", None) or not getattr(settings, "MAPS_PRIVATE_KEY", None):
            warnings.warn(
                "Google Maps static preview URLs will not work without MAPS_API_KEY and MAPS_PRIVATE_KEY",
                RuntimeWarning,
            )

