# Generated by Django 4.0.6 on 2022-08-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelo', '0008_vol'),
    ]

    operations = [
        migrations.CreateModel(
            name='reco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('counter', models.IntegerField(blank=True, max_length=100, null=True)),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
