# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_remove_userprofile_athlete'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='graduation_year',
            field=models.DateField(default=2014, blank=True),
            preserve_default=True,
        ),
    ]
