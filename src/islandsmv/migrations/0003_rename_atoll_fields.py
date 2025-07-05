from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('islandsmv', '0002_dhivehi_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atoll',
            old_name='code',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='atoll',
            name='name',
            field=models.CharField(max_length=250, primary_key=True),
        ),
        migrations.RenameField(
            model_name='atoll',
            old_name='code_dv',
            new_name='name_dv',
        ),
    ]