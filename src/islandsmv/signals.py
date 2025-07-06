from django.core.management import call_command

from .apps import IslandsmvConfig
from .models import Island


def load_islands_fixture(sender, **kwargs):
    if sender.name == IslandsmvConfig.name:

        if Island.objects.all().count() == 0:
            call_command('loaddata', 'islands.yaml', app_label='islandsmv',
                         verbosity=0)
