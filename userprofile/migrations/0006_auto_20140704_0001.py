# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_userprofile_clubs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='athlete',
            field=models.CharField(default=b'1', max_length=1, choices=[(1, b'athlete')]),
        ),
    ]
