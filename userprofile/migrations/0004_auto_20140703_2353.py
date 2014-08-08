# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20140703_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='athlete',
            field=models.CharField(default=b'athlete', max_length=1, choices=[(1, b'athlete')]),
        ),
    ]
