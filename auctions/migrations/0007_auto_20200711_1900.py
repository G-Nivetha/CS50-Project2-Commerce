# Generated by Django 3.0.8 on 2020-07-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200711_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]