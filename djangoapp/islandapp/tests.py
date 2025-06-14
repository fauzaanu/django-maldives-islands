import base64

from django.core.management import call_command
from django.test import TestCase, override_settings

from islandsmv.models import Island, Atoll


# Create your tests here.

class TestIslandsMvData(TestCase):

    def test_migration_imports_islands_atolls(self):
        Island.objects.all().delete()
        islands = Island.objects.all().count()
        self.assertEqual(islands, 0)
        call_command("migrate")
        islands = Island.objects.all().count()
        self.assertNotEqual(islands, 0)

class TestModelsIslandsMv(TestCase):

    def setUp(self):
        self.atoll = Atoll.objects.create(code="KA")
        self.island = Island.objects.create(
            name="Test Island",
            island_name="Test",
            atoll=self.atoll,
            type="admin_island",
            longitude=73.5,
            latitude=4.2
        )

    def test_lat_long_combined_property(self):
        self.assertEqual(self.island.lat_long_combined, (4.2, 73.5))

    @override_settings(
        MAPS_API_KEY="test_api_key",
        MAPS_PRIVATE_KEY=base64.urlsafe_b64encode(b'secret_key').decode().rstrip("="),
        MAPS_ZOOM=10,
        MAPS_WIDTH=400,
        MAPS_HEIGHT=200,
    )
    def test_get_static_map_url_returns_valid_url(self):
        url = self.island.get_static_map_url()
        self.assertTrue(url.startswith("https://maps.googleapis.com/maps/api/staticmap"))
        self.assertIn("signature=", url)
        self.assertIn("center=4.2,73.5", url)
