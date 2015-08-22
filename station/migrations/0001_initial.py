# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField(verbose_name=b'update date')),
                ('qua_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('longitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('qua_cntu', models.DecimalField(max_digits=4, decimal_places=2)),
                ('qua_cl', models.DecimalField(max_digits=4, decimal_places=2)),
                ('qua_ph', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
        ),
    ]
