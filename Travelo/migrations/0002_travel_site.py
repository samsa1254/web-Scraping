# Generated by Django 4.0.6 on 2022-08-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='site',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
