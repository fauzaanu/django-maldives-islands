from django.test import TestCase, override_settings
from django.core import checks

from .models import Atoll, Island


@override_settings(MAPS_API_KEY="key", MAPS_PRIVATE_KEY="secret")
class StaticMapURLTests(TestCase):
    def test_static_map_url_contains_coordinates_and_signature(self):
        atoll = Atoll.objects.create(code="MLE")
        island = Island.objects.create(
            name="Vilimale",
            island_name="vilimale",
            atoll=atoll,
            type=Island.MAALE[0],
            longitude=73.48527944,
            latitude=4.173394722,
        )

        url = island.get_static_map_url()

        self.assertIn("https://maps.googleapis.com/maps/api/staticmap", url)
        self.assertIn("signature=", url)
        self.assertIn(str(island.latitude), url)
        self.assertIn(str(island.longitude), url)


class MissingKeyTests(TestCase):
    def test_get_static_map_url_without_credentials_raises(self):
        atoll = Atoll.objects.create(code="MLE")
        island = Island.objects.create(
            name="Vilimale",
            island_name="vilimale",
            atoll=atoll,
            type=Island.MAALE[0],
            longitude=73.48527944,
            latitude=4.173394722,
        )

        with self.assertRaises(RuntimeError):
            island.get_static_map_url()


@override_settings(MAPS_API_KEY=None, MAPS_PRIVATE_KEY=None)
class SystemCheckTests(TestCase):
    def test_warning_emitted_when_keys_missing(self):
        errors = checks.run_checks(tags=[checks.Tags.compatibility])
        self.assertTrue(any(e.id == "islandsmv.W001" for e in errors))

