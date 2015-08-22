# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 22, 4, 32, 6, 971302, tzinfo=utc), verbose_name=b'update date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='update_time',
            field=models.TimeField(),
        ),
    ]
