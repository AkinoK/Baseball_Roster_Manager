# Generated by Django 4.2.3 on 2023-08-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster_manager', '0003_remove_player_pitching_records_player_era_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.CharField(max_length=10),
        ),
    ]
