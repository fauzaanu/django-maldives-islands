from django.core.management import call_command

from islandsmv.apps import IslandsmvConfig


def load_islands_fixture(sender, **kwargs):
    # only run for your app
    if sender.name == IslandsmvConfig.name:
        call_command('loaddata', 'islands.json', app_label='islandsmv', verbosity=0)
