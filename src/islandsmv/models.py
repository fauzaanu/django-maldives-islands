from django.db import models


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

    def __str__(self):
        return self.name
