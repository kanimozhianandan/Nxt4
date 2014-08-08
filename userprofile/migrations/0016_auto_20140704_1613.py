# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0015_auto_20140704_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='graduation_year',
            field=models.DateField(default=2014),
        ),
    ]
