# Generated by Django 3.0.5 on 2020-04-29 22:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y%m%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 29, 17, 55, 25, 589937)),
        ),
    ]
