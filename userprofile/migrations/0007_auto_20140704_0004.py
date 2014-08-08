# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20140704_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='athlete',
            field=models.CharField(default=b'Y', max_length=1),
        ),
    ]
