# Generated by Django 4.0.6 on 2022-08-29 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travelo', '0011_rename_location_reco_iplocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reco',
            old_name='dest',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='reco',
            old_name='iplocation',
            new_name='location',
        ),
    ]
