# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20140704_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sports',
            field=models.CharField(default=b'No sports', max_length=75),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='graduation_year',
            field=models.IntegerField(default=2014, max_length=4, choices=[(2015, 2015), (2016, 2016), (2017, 2017)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
    ]
