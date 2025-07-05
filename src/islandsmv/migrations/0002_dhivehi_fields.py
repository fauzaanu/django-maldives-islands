from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islandsmv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='island',
            name='island_name_dv',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='atoll',
            name='code_dv',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
