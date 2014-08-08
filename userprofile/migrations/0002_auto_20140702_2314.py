# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='school_name',
            field=models.CharField(default=b'High School', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year_in_school',
            field=models.CharField(max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')]),
        ),
    ]
