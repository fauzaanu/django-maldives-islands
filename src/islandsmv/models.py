from django.db import models
from django.conf import settings
from urllib.parse import urlparse
import base64
import hmac
import hashlib


# Create your models here.
class Atoll(models.Model):
    code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.code


class Island(models.Model):
    ADMIN_ISLAND = ("admin_island", "ADMIN ISLAND")
    MAALE = ("maale", "MAALE")

    ISLAND_TYPES = [
        ADMIN_ISLAND, MAALE
    ]

    name = models.CharField(max_length=250)
    island_name = models.CharField(max_length=250)
    atoll = models.ForeignKey(Atoll, on_delete=models.CASCADE)
    type = models.CharField(max_length=250, choices=ISLAND_TYPES)
    longitude = models.FloatField()
    latitude = models.FloatField()

    @property
    def lat_long_combined(self):
        return self.latitude, self.longitude

    def get_static_map_url(self, zoom: int = 15, size: tuple[int, int] = (600, 300)) -> str:
        """Return a signed Google Static Map preview URL for this island."""
        lat, lng = self.lat_long_combined
        key = settings.MAPS_API_KEY
        base = (
            "https://maps.googleapis.com/maps/api/staticmap"
            f"?center={lat},{lng}"
            f"&zoom={zoom}"
            f"&size={size[0]}x{size[1]}"
            f"&key={key}"
        )

        # URL-signing (using the private signing secret)
        secret = settings.MAPS_PRIVATE_KEY
        secret += "=" * (-len(secret) % 4)
        parsed = urlparse(base)
        url_to_sign = parsed.path + "?" + parsed.query
        decoded_key = base64.urlsafe_b64decode(secret)
        sig = hmac.new(decoded_key, url_to_sign.encode(), hashlib.sha1).digest()
        signature = base64.urlsafe_b64encode(sig).decode()

        return f"{base}&signature={signature}"

    def __str__(self):
        return self.name
